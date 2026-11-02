#!/usr/bin/env -S uv run --script --python 3.12
# /// script
# requires-python = ">=3.10,<3.13"
# dependencies = ["faster-whisper>=1.1", "numpy", "nvidia-cublas-cu12", "nvidia-cudnn-cu12>=9,<10"]
# ///
"""Fallback transcript source when YouTube blocks caption requests: download audio, transcribe on the GPU.

Writes data/transcripts/<id>.json in the same format as `aie.py fetch`. Downloading (CPU/network) runs in a
thread pool ahead of the single GPU transcriber, and audio is deleted once transcribed.

  pipeline/whisper_fetch.py --since 20260518            # newest first
  pipeline/whisper_fetch.py --ids abc,def
"""

import argparse
import concurrent.futures as cf
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
TRANSCRIPTS = DATA / "transcripts"
AUDIO = DATA / "audio"


def cuda_libs() -> None:
    # pip-installed cuBLAS/cuDNN aren't on the loader path by default; re-exec once with them added
    if os.environ.get("_AIE_CUDA_OK"):
        return
    import nvidia.cublas.lib, nvidia.cudnn.lib  # noqa: E401
    paths = [list(nvidia.cublas.lib.__path__)[0], list(nvidia.cudnn.lib.__path__)[0]]
    os.environ["LD_LIBRARY_PATH"] = ":".join(paths + [os.environ.get("LD_LIBRARY_PATH", "")])
    os.environ["_AIE_CUDA_OK"] = "1"
    os.execv(sys.executable, [sys.executable] + sys.argv)


def download(vid: str) -> Path | None:
    AUDIO.mkdir(parents=True, exist_ok=True)
    for p in AUDIO.glob(f"{vid}.*"):
        if p.suffix != ".part":
            return p
    r = subprocess.run(["yt-dlp", "-q", "--no-warnings", "-f", "ba[ext=m4a]/ba", "-o", str(AUDIO / "%(id)s.%(ext)s"),
                        f"https://www.youtube.com/watch?v={vid}"], capture_output=True, text=True)
    hits = [p for p in AUDIO.glob(f"{vid}.*") if p.suffix != ".part"]
    if not hits:
        print(f"download failed {vid}: {r.stderr[-200:]}", file=sys.stderr)
    return hits[0] if hits else None


def load_audio(path: Path):
    """16 kHz mono float32 via system ffmpeg (sidesteps PyAV API drift)."""
    import numpy as np
    raw = subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-i", str(path), "-f", "s16le",
                          "-ac", "1", "-ar", "16000", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768.0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", default="", help="YYYYMMDD; only videos uploaded on/after")
    ap.add_argument("--ids", default="")
    ap.add_argument("--channel", default="", help="comma list of channel slugs; videos without one are 'aie'")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--model", default="large-v3-turbo")
    ap.add_argument("--batch", type=int, default=16)
    ap.add_argument("--min-seconds", type=int, default=240)
    ap.add_argument("--keep-audio", action="store_true")
    ap.add_argument("--dl-workers", type=int, default=8, help="parallel audio downloads (the usual bottleneck)")
    args = ap.parse_args()
    cuda_libs()
    from faster_whisper import BatchedInferencePipeline, WhisperModel

    vids = [json.loads(l) for l in (DATA / "videos.jsonl").read_text().splitlines() if l.strip()]
    if args.ids:
        want = set(args.ids.split(","))
        todo = [v for v in vids if v["id"] in want]
    else:
        chans = set(filter(None, args.channel.split(",")))
        todo = [v for v in vids if (v.get("upload_date") or "") >= args.since
                and (v.get("duration") or 0) >= args.min_seconds
                and (not chans or (v.get("channel") or "aie") in chans)]
    todo = [v for v in todo if not (TRANSCRIPTS / f"{v['id']}.json").exists()]
    todo.sort(key=lambda v: v.get("upload_date") or "", reverse=True)
    todo = todo[: args.limit] if args.limit else todo
    print(f"whisper: {len(todo)} videos, {sum(v.get('duration') or 0 for v in todo) / 3600:.0f} h audio", file=sys.stderr)

    model = BatchedInferencePipeline(WhisperModel(args.model, device="cuda", compute_type="float16", download_root=str(DATA / "models")))
    TRANSCRIPTS.mkdir(parents=True, exist_ok=True)
    t0, audio_s = time.time(), 0.0
    with cf.ThreadPoolExecutor(args.dl_workers) as ex:
        futs = [(v, ex.submit(download, v["id"])) for v in todo]  # downloads run ahead of the GPU
        for i, (v, fut) in enumerate(futs, 1):
            path = fut.result()
            if not path:
                continue
            try:
                segs, info = model.transcribe(load_audio(path), language="en", batch_size=args.batch,
                                              vad_filter=True, condition_on_previous_text=False)
                rows = [[round(s.start, 1), s.text.strip()] for s in segs]
            except Exception as e:
                print(f"[{i}/{len(todo)}] fail {v['id']}: {e!r:.200}", file=sys.stderr)
                continue
            (TRANSCRIPTS / f"{v['id']}.json").write_text(json.dumps(
                {"id": v["id"], "lang": "en", "generated": True, "source": f"whisper-{args.model}",
                 "segments": rows}, ensure_ascii=False))
            audio_s += info.duration
            if not args.keep_audio:
                path.unlink(missing_ok=True)
            el = time.time() - t0
            print(f"[{i}/{len(todo)}] {v['id']} {info.duration / 60:.0f}m · {audio_s / el:.0f}x realtime · "
                  f"{el / 60:.0f}m elapsed · {v['title'][:60]}", file=sys.stderr)


if __name__ == "__main__":
    main()
