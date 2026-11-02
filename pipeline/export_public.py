#!/usr/bin/env python3
"""Build the public copy of this KB in another directory (default ../ai-youtube-kb).

Strips day-job material (the agent-gateway project: its profile section, insight doc, per-video relevance
lines and guide bullets about it), private paths, logs, backups and drafts. Raw transcripts, audio and models
stay out (YouTube content / size). The export dir is its own git repo; this script never touches its .git.

  pipeline/export_public.py [--out DIR]
"""

import argparse
import json
import re
import importlib.util
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

COPY = ["CLAUDE.md", "context/channels.md", "context/categories.md", "context/profile.md",
        "pipeline/aie.py", "pipeline/whisper_fetch.py", "pipeline/workflows", "pipeline/export_public.py",
        "kb/INDEX.md", "kb/latest.md", "kb/trends.md", "kb/guides", "kb/insights", "kb/categories", "kb/channels",
        "kb/videos", "data/videos.jsonl", "data/notes"]
DROP_FILES = {"kb/insights/gateway.md"}

# a line is about the day-job gateway project (not a talk that merely mentions ClickHouse or a gateway product)
OURS = re.compile(r"trace read path|day job|agent registry|insights/gateway|our gateway|\*\*gateway\*\*|"
                  r"^\s*[-*]?\s*(\*\*)?gateway(\*\*)?\s*[:(—-]|/ ?gateway\b|gateway ?/|\bthe gateway'?s?\b", re.I | re.M)
SPECIFIC = re.compile(r"clickhouse|\b503s?\b|\bp95\b|registry", re.I)


OUR_PROBLEM = re.compile(r"\b503\b.{0,12}\bp95\b|\bp95\b.{0,12}\b503\b|read[- ]path|\b503 (bursts?|problems?|reliability)|\b503s\b|blaming clickhouse", re.I)
WE = re.compile(r"\b(our|we|us)\b", re.I)


def about_gateway_project(line: str) -> bool:
    return (bool(OURS.search(line)) or bool(OUR_PROBLEM.search(line))
            or ("gateway" in line.lower() and bool(SPECIFIC.search(line)))
            or (bool(WE.search(line)) and bool(SPECIFIC.search(line))))
PRIVATE = re.compile(r"<local path>`)\"']*")


def depath(text: str) -> str:
    # the repo root becomes a placeholder to edit after cloning; other private paths are dropped
    text = text.replace(str(ROOT), "/path/to/ai-youtube-kb").replace("/path/to/ai-youtube-kb", "/path/to/ai-youtube-kb")
    return PRIVATE.sub("<local path>", text)


def scrub_md(text: str) -> str:
    out = []
    for line in text.splitlines():
        if about_gateway_project(line):
            continue
        out.append(depath(line))
    return "\n".join(out) + "\n"


def scrub_profile(text: str) -> str:
    # drop the "## Agent gateway ..." section entirely
    return re.sub(r"## Agent gateway.*?(?=\n## )", "", text, flags=re.S)


def scrub_note(note: dict) -> dict:
    note["relevance"] = [r for r in note.get("relevance", []) if r.get("project") != "gateway"]
    for r in note["relevance"]:
        for k in ("why", "action"):
            if about_gateway_project(r.get(k, "")):
                r[k] = ""
    return note


def load_aie():
    spec = importlib.util.spec_from_file_location("aie", ROOT / "pipeline" / "aie.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    aie = load_aie()
    vids = aie.video_map()
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT.parent / "ai-youtube-kb"))
    out = Path(ap.parse_args().out)
    out.mkdir(parents=True, exist_ok=True)
    for child in out.iterdir():  # wipe everything but .git so deletions propagate
        if child.name != ".git":
            shutil.rmtree(child) if child.is_dir() else child.unlink()
    for rel in COPY:
        src = ROOT / rel
        files = [src] if src.is_file() else sorted(p for p in src.rglob("*") if p.is_file())
        for f in files:
            r = f.relative_to(ROOT).as_posix()
            if r in DROP_FILES or "__pycache__" in r:
                continue
            dst = out / r
            dst.parent.mkdir(parents=True, exist_ok=True)
            if r == "context/profile.md":
                dst.write_text(scrub_profile(f.read_text()))
            elif r.startswith("data/notes/"):
                note = scrub_note(json.loads(f.read_text()))
                dst.write_text(json.dumps(note, ensure_ascii=False, indent=1))
                # the video page is re-rendered from the scrubbed note, so talk content stays intact
                page = out / "kb" / "videos" / f"{f.stem}.md"
                page.parent.mkdir(parents=True, exist_ok=True)
                page.write_text(depath(aie.render_video_md(f.stem, vids[f.stem], note)))
            elif r.startswith("kb/videos/"):
                continue  # written from the scrubbed note above
            elif f.suffix in (".md", ".js", ".py"):
                dst.write_text(scrub_md(f.read_text()) if f.suffix == ".md" else depath(f.read_text()))
            else:
                shutil.copy2(f, dst)
    n_notes = len(list((out / "data" / "notes").glob("*.json")))
    chans = "\n".join(f"- **{c['name']}** ({c['handle']}): {c['desc']}" for c in aie.CHANNELS.values())
    (out / "README.md").write_text(f"""# AI YouTube knowledge base

Structured, searchable notes on {n_notes} videos from these YouTube channels, organized by topic
(Claude Code, token/cost efficiency, PR review, evals, MCP, local AI, inference, agents, dev tools, ...):

{chans}

Built by a pipeline of Haiku subagents: Whisper transcribes each video on a local GPU, one Haiku agent per
video writes timestamped notes, and Haiku agents write a field guide per topic and fact-check its citations.

## Read it
- `kb/trends.md`: what changed, and what to do now.
- `kb/guides/<topic>.md`: field guide per topic (state of the art, consensus, disagreements, creator playbooks).
- `kb/categories/<topic>.md`: every video on a topic, newest first. Topic list: `context/categories.md`.
- `kb/channels/<channel>.md`: every video from one channel.
- `kb/videos/<id>.md`: one video's notes with timestamp links. `kb/INDEX.md` lists them all.

Notes are model-written paraphrases of auto-transcribed speech. Check the video (timestamp links) before relying
on a specific claim. Raw transcripts are not included.

## Run it
`CLAUDE.md` documents the pipeline (`pipeline/aie.py`, `pipeline/workflows/*.js` for the Claude Code Workflow tool).
Set `ROOT` in the workflow scripts to your clone path. `context/profile.md` describes the projects the notes score
relevance against; replace it with your own.
""")
    (out / ".gitignore").write_text("data/transcripts/\ndata/audio/\ndata/models/\ndata/wf/\ndata/.claude_cwd/\n"
                                    "kb/search.db\n__pycache__/\n*.log\n")
    print(f"exported to {out}")


if __name__ == "__main__":
    main()
