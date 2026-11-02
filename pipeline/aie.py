#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["youtube-transcript-api>=1.0"]
# ///
"""YouTube channels (context/channels.md) → transcripts → Haiku notes → guides → searchable context plane.

Every stage is incremental and keyed by video id, so `aie.py run` is safe to re-run any time.
Most commands take `--channel aie,kai,...` (slugs from context/channels.md) to scope the work.

  list     refresh data/videos.jsonl from every channel
  fetch    pull YouTube captions → data/transcripts/<id>.json
  extract  Haiku: structured notes per video → data/notes/<id>.json + kb/videos/<id>.md
  synth    Sonnet: kb/guides/<category>.md and kb/insights/<project>.md
  index    kb/INDEX.md, kb/latest.md, kb/categories/<slug>.md, kb/search.db (SQLite FTS5)
  search   full-text search over notes (+ --transcripts for raw transcript lines)
  show     print one video's notes
  status   progress + spend
  run      list → fetch → extract → index
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import json
import random
import re
import sqlite3
import subprocess
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
KB = ROOT / "kb"
CONTEXT = ROOT / "context"
VIDEOS = DATA / "videos.jsonl"
TRANSCRIPTS = DATA / "transcripts"
NOTES = DATA / "notes"
FAILED = DATA / "fetch_failed.json"
COSTS = DATA / "costs.jsonl"
CLAUDE_CWD = DATA / ".claude_cwd"  # empty dir so no project CLAUDE.md leaks into the prompt
DEFAULT_CHANNEL = "aie"  # videos listed before multi-channel support carry no `channel` field


def load_channels() -> dict[str, dict]:
    chans = {}
    for line in (CONTEXT / "channels.md").read_text().splitlines():
        m = re.match(r"([a-z0-9-]+):\s*(@\S+)\s*\|\s*([^|]+?)\s*\|\s*(.+)", line.strip())
        if m:
            chans[m[1]] = {"slug": m[1], "handle": m[2], "name": m[3], "desc": m[4].strip(),
                           "url": f"https://www.youtube.com/{m[2]}/videos"}
    return chans


CHANNELS = load_channels()


def chan(v: dict) -> str:
    return v.get("channel") or DEFAULT_CHANNEL


def chan_name(v: dict) -> str:
    c = CHANNELS.get(chan(v))
    return c["name"] if c else chan(v)


def want_channels(arg: str | None) -> set[str] | None:
    """--channel a,b → {'a','b'}; empty → None (all). Unknown slugs are an error, not a silent no-op."""
    if not arg:
        return None
    want = {c.strip() for c in arg.split(",") if c.strip()}
    if bad := want - CHANNELS.keys():
        sys.exit(f"unknown channel(s) {sorted(bad)}; known: {sorted(CHANNELS)}")
    return want


def in_channels(v: dict, want: set[str] | None) -> bool:
    return want is None or chan(v) in want


def load_categories() -> dict[str, str]:
    cats = {}
    for line in (CONTEXT / "categories.md").read_text().splitlines():
        m = re.match(r"([a-z0-9-]+):\s*(.+)", line.strip())
        if m:
            cats[m[1]] = m[2]
    return cats


CATEGORIES = load_categories()
TOPICS = list(CATEGORIES)
PROJECTS = ["agentos", "gateway", "prosharness", "general"]

_lock = threading.Lock()


# ---------- helpers ----------

def load_videos() -> list[dict]:
    if not VIDEOS.exists():
        return []
    return [json.loads(l) for l in VIDEOS.read_text().splitlines() if l.strip()]


def video_map() -> dict[str, dict]:
    return {v["id"]: v for v in load_videos()}


def fmt_ts(sec: float) -> str:
    sec = int(sec)
    h, m, s = sec // 3600, sec % 3600 // 60, sec % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def ts_to_sec(t: str) -> int:
    try:
        parts = [int(p) for p in str(t).strip().split(":")]
    except ValueError:
        return 0
    sec = 0
    for p in parts:
        sec = sec * 60 + p
    return sec


def yt_link(vid: str, t: str | None = None) -> str:
    return f"https://youtu.be/{vid}" + (f"?t={ts_to_sec(t)}" if t else "")


def pretty_date(d: str | None) -> str:
    return f"{d[:4]}-{d[4:6]}-{d[6:]}" if d and len(d) == 8 else (d or "unknown")


def log_cost(stage: str, vid: str, model: str, cost: float) -> None:
    with _lock, COSTS.open("a") as f:
        f.write(json.dumps({"stage": stage, "id": vid, "model": model, "usd": cost,
                            "at": dt.datetime.now().isoformat(timespec="seconds")}) + "\n")


def claude(prompt: str, system: str, model: str, schema: dict | None = None, timeout: int = 900) -> dict:
    """One headless Claude Code call (uses the logged-in subscription, no API key needed)."""
    CLAUDE_CWD.mkdir(parents=True, exist_ok=True)
    cmd = ["claude", "-p", "--model", model, "--output-format", "json", "--tools", "",
           "--no-session-persistence", "--setting-sources", "", "--strict-mcp-config",
           "--system-prompt", system]
    if schema:
        cmd += ["--json-schema", json.dumps(schema)]
    r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=timeout, cwd=CLAUDE_CWD)
    try:
        out = json.loads(r.stdout)
    except json.JSONDecodeError:
        raise RuntimeError(f"claude exited {r.returncode}: {(r.stderr or r.stdout)[-400:]}")
    if out.get("is_error"):
        raise RuntimeError(f"claude error: {str(out.get('result'))[:400]}")
    return out


# ---------- list ----------

def list_channel(slug: str) -> list[list[str]]:
    tmpl = "%(id)s\t%(title)s\t%(duration)s\t%(upload_date)s\t%(view_count)s"
    r = subprocess.run(["yt-dlp", "--flat-playlist", "--extractor-args", "youtubetab:approximate_date",
                        "--print", tmpl, CHANNELS[slug]["url"]], capture_output=True, text=True)
    rows = [p for p in (line.split("\t") for line in r.stdout.splitlines()) if len(p) == 5]
    if not rows:
        print(f"  {slug}: listing failed ({r.stderr.strip()[-200:]})", file=sys.stderr)
    return rows


def cmd_list(args) -> None:
    want = want_channels(getattr(args, "channel", None))
    slugs = [s for s in CHANNELS if want is None or s in want]
    print(f"listing {', '.join(slugs)}…", file=sys.stderr)
    with cf.ThreadPoolExecutor(len(slugs) or 1) as ex:
        listed = dict(zip(slugs, ex.map(list_channel, slugs)))
    old = video_map()
    fresh: dict[str, int] = {}
    for slug, rows in listed.items():
        for vid, title, dur, date, views in rows:
            rec = old.get(vid, {"id": vid})
            if vid not in old:
                fresh[slug] = fresh.get(slug, 0) + 1
            rec.update(title=title, channel=slug,
                       duration=int(float(dur)) if dur not in ("NA", "None", "") else None,
                       views=int(views) if views.isdigit() else rec.get("views"))
            # approximate dates drift as videos age; keep the first one we saw unless we never had one
            if date.isdigit() and not rec.get("upload_date"):
                rec["upload_date"] = date
            old[vid] = rec
    DATA.mkdir(exist_ok=True)
    VIDEOS.write_text("".join(json.dumps(v, ensure_ascii=False) + "\n" for v in old.values()))
    print(f"{len(old)} videos; new: " + (", ".join(f"{s} {n}" for s, n in fresh.items()) or "none"))


# ---------- fetch ----------

def cmd_fetch(args) -> None:
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api._errors import (IpBlocked, NoTranscriptFound, RequestBlocked,
                                                TranscriptsDisabled, VideoUnavailable)

    TRANSCRIPTS.mkdir(parents=True, exist_ok=True)
    failed = json.loads(FAILED.read_text()) if FAILED.exists() else {}
    want = want_channels(args.channel)
    todo = [v for v in load_videos()
            if in_channels(v, want) and not (TRANSCRIPTS / f"{v['id']}.json").exists()
            and (args.retry or v["id"] not in failed)
            and (v.get("duration") or 0) >= args.min_seconds
            and (v.get("upload_date") or "") >= args.since]
    if args.oldest_first:  # lets a whisper run work newest-first without colliding
        todo.sort(key=lambda v: v.get("upload_date") or "")
    todo = todo[: args.limit] if args.limit else todo
    print(f"fetching {len(todo)} transcripts", file=sys.stderr)
    api = YouTubeTranscriptApi()
    blocked_streak = 0
    for i, v in enumerate(todo, 1):
        vid = v["id"]
        if (TRANSCRIPTS / f"{vid}.json").exists():
            continue
        try:
            ft = api.fetch(vid, languages=["en", "en-US", "en-GB"])
            segs = [[round(s.start, 1), s.text] for s in ft.snippets]
            (TRANSCRIPTS / f"{vid}.json").write_text(json.dumps(
                {"id": vid, "lang": ft.language_code, "generated": ft.is_generated, "segments": segs},
                ensure_ascii=False))
            failed.pop(vid, None)
            blocked_streak = 0
            print(f"[{i}/{len(todo)}] ok   {vid} {v['title'][:70]}", file=sys.stderr)
        except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable) as e:
            failed[vid] = type(e).__name__
            print(f"[{i}/{len(todo)}] skip {vid} {type(e).__name__}", file=sys.stderr)
        except (RequestBlocked, IpBlocked) as e:
            blocked_streak += 1
            wait = min(60 * 2 ** blocked_streak, 1800)
            print(f"[{i}/{len(todo)}] BLOCKED ({blocked_streak}) — sleeping {wait}s", file=sys.stderr)
            if blocked_streak >= 5:
                print("YouTube keeps blocking; stopping. Re-run later.", file=sys.stderr)
                break
            time.sleep(wait)
        except Exception as e:  # network blips etc. — leave for next run
            print(f"[{i}/{len(todo)}] err  {vid} {e!r:.120}", file=sys.stderr)
        FAILED.write_text(json.dumps(failed, indent=1))
        time.sleep(args.sleep + random.random())


def transcript_text(vid: str, para_seconds: int = 30) -> str:
    """Transcript as [m:ss]-stamped paragraphs so the model can cite times."""
    segs = json.loads((TRANSCRIPTS / f"{vid}.json").read_text())["segments"]
    out, cur, start = [], [], None
    for s, text in segs:
        if start is None:
            start = s
        cur.append(text.replace("\n", " "))
        if s - start >= para_seconds:
            out.append(f"[{fmt_ts(start)}] {' '.join(cur)}")
            cur, start = [], None
    if cur:
        out.append(f"[{fmt_ts(start)}] {' '.join(cur)}")
    return "\n".join(out)


# ---------- extract (Haiku) ----------

FORMATS = ["talk", "workshop", "panel", "keynote", "interview", "demo", "tutorial", "news", "review", "other"]

NOTE_SCHEMA = {
    "type": "object",
    "required": ["one_line", "summary", "speakers", "orgs", "format", "topics", "tags", "key_ideas",
                 "techniques", "tools", "numbers", "hot_takes", "relevance", "quality", "depth"],
    "properties": {
        "one_line": {"type": "string", "description": "What the talk is about + its main takeaway, <=30 words"},
        "summary": {"type": "string", "description": "5-8 sentence summary in plain language"},
        "speakers": {"type": "array", "items": {"type": "string"}},
        "orgs": {"type": "array", "items": {"type": "string"}},
        "format": {"type": "string", "enum": FORMATS},
        "topics": {"type": "array", "items": {"type": "string", "enum": TOPICS}, "minItems": 1, "maxItems": 4},
        "tags": {"type": "array", "items": {"type": "string"}, "description": "3-10 kebab-case specifics"},
        "key_ideas": {"type": "array", "items": {"type": "object", "required": ["idea", "detail", "t"],
                      "properties": {"idea": {"type": "string"}, "detail": {"type": "string"},
                                     "t": {"type": "string", "description": "timestamp m:ss or h:mm:ss"}}}},
        "techniques": {"type": "array", "items": {"type": "object", "required": ["name", "how", "when"],
                       "properties": {"name": {"type": "string"}, "how": {"type": "string"},
                                      "when": {"type": "string"}}}},
        "tools": {"type": "array", "items": {"type": "string"}, "description": "products/libs/models named"},
        "numbers": {"type": "array", "items": {"type": "object", "required": ["claim", "t"],
                    "properties": {"claim": {"type": "string"}, "t": {"type": "string"}}}},
        "hot_takes": {"type": "array", "items": {"type": "string"}, "description": "contrarian or opinionated claims"},
        "relevance": {"type": "array", "items": {"type": "object", "required": ["project", "score", "why", "action"],
                      "properties": {"project": {"type": "string", "enum": PROJECTS},
                                     "score": {"type": "integer", "minimum": 0, "maximum": 3},
                                     "why": {"type": "string"}, "action": {"type": "string"}}}},
        "quality": {"type": "integer", "minimum": 1, "maximum": 5},
        "depth": {"type": "string", "enum": ["intro", "practitioner", "deep"]},
    },
}

EXTRACT_SYSTEM = """You turn YouTube video transcripts (conference talks, tutorials, tool reviews, AI-news roundups)
into dense, accurate research notes for engineers. The header names the channel and title.
Rules:
- Only state what the speaker actually says. No outside knowledge, no hype. Paraphrase; never copy long passages.
- key_ideas: 4-10 of the most important, non-obvious points, each with the [m:ss] timestamp where it starts.
- techniques: concrete, reusable patterns (architecture, prompting, eval method, infra trick) with how + when to use.
  For tutorials and tool reviews, put the actual steps here: exact commands, config keys, settings, prompts,
  flags and file names shown, so a reader can reproduce it without watching.
- tools: every product, library, model, CLI or repo named (with version if stated).
- numbers: benchmarks, costs, latencies, token counts, prices, adoption stats, with timestamps.
- format: tutorial = step-by-step how-to; review = tool/product walkthrough or comparison; news = roundup of releases.
- quality: 5 = rare insight / hard-won data, 3 = solid practitioner content, 1 = sales pitch, clickbait or no content.
  A sponsored segment or a hype title with thin substance caps quality at 2; say so in hot_takes.
- For news roundups, key_ideas = one item per release/announcement worth knowing, with its timestamp.
- relevance: score every project in the profile below (0 none .. 3 directly changes what we build).
  `action` = one specific thing to try/change/read, or "" when score is 0. Be strict: most talks score 0-1 for most projects.
- topics: pick 1-4 categories from the list below, most central first.
Auto-captions misspell names (e.g. "Claude" as "cloud", "MCP" as "MCB"); fix obvious ones.

CATEGORIES:
""" + "\n".join(f"- {k}: {v}" for k, v in CATEGORIES.items()) + """

PROJECT PROFILE:
"""


def render_video_md(vid: str, v: dict, n: dict) -> str:
    rel = sorted(n.get("relevance", []), key=lambda r: -r["score"])
    lines = [
        f"# {v['title']}",
        "",
        f"- **channel:** [{chan_name(v)}](../channels/{chan(v)}.md)"
        f" · **id:** `{vid}` · [watch]({yt_link(vid)}) · **date:** {pretty_date(v.get('upload_date'))}"
        f" · **length:** {fmt_ts(v.get('duration') or 0)} · **format:** {n['format']}"
        f" · **quality:** {n['quality']}/5 · **depth:** {n['depth']}",
        f"- **speakers:** {', '.join(n['speakers']) or '?'} · **orgs:** {', '.join(n['orgs']) or '?'}",
        f"- **topics:** {', '.join(n['topics'])} · **tags:** {', '.join(n['tags'])}",
        "",
        f"> {n['one_line']}",
        "",
        "## Summary",
        n["summary"],
        "",
        "## Key ideas",
        *[f"- **{k['idea']}** — {k['detail']} ([{k['t']}]({yt_link(vid, k['t'])}))" for k in n["key_ideas"]],
    ]
    if n["techniques"]:
        lines += ["", "## Techniques",
                  *[f"- **{t['name']}** — {t['how']} *When:* {t['when']}" for t in n["techniques"]]]
    if n["numbers"]:
        lines += ["", "## Numbers", *[f"- {x['claim']} ([{x['t']}]({yt_link(vid, x['t'])}))" for x in n["numbers"]]]
    if n["hot_takes"]:
        lines += ["", "## Hot takes", *[f"- {h}" for h in n["hot_takes"]]]
    if n["tools"]:
        lines += ["", "## Tools mentioned", ", ".join(n["tools"])]
    if any(r["score"] for r in rel):
        lines += ["", "## Relevance to our work",
                  *[f"- **{r['project']}** ({r['score']}/3): {r['why']}" + (f" → *{r['action']}*" if r["action"] else "")
                    for r in rel if r["score"]]]
    return "\n".join(lines) + "\n"


def video_header(v: dict) -> str:
    c = CHANNELS.get(chan(v), {})
    return (f"Video id: {v['id']}\nChannel: {chan_name(v)} ({c.get('desc', '')})\nTitle: {v['title']}\n"
            f"Date: {pretty_date(v.get('upload_date'))}\nLength: {fmt_ts(v.get('duration') or 0)}\n")


def extract_one(vid: str, v: dict, model: str, profile: str) -> float:
    text = transcript_text(vid)
    if len(text) > 600_000:  # ~150k tokens; keep head + tail of very long streams
        text = text[:450_000] + "\n[... middle omitted ...]\n" + text[-150_000:]
    prompt = video_header(v) + f"\nTRANSCRIPT:\n{text}"
    out = claude(prompt, EXTRACT_SYSTEM + profile, model, NOTE_SCHEMA)
    note = out.get("structured_output") or json.loads(out["result"])
    note["_model"], note["_usd"] = model, out.get("total_cost_usd", 0)
    note["_at"] = dt.datetime.now().isoformat(timespec="seconds")
    (NOTES / f"{vid}.json").write_text(json.dumps(note, ensure_ascii=False, indent=1))
    (KB / "videos" / f"{vid}.md").write_text(render_video_md(vid, v, note))
    log_cost("extract", vid, model, note["_usd"])
    return note["_usd"]


def cmd_extract(args) -> None:
    NOTES.mkdir(parents=True, exist_ok=True)
    (KB / "videos").mkdir(parents=True, exist_ok=True)
    profile = (CONTEXT / "profile.md").read_text()
    vids = video_map()
    want = want_channels(args.channel)
    todo = [vid for vid in vids
            if in_channels(vids[vid], want)
            and (TRANSCRIPTS / f"{vid}.json").exists() and (args.force or not (NOTES / f"{vid}.json").exists())]
    # newest first, so a partial run still covers the latest thinking
    todo.sort(key=lambda x: vids[x].get("upload_date") or "", reverse=True)
    if args.ids:
        todo = [x for x in args.ids.split(",") if x in vids]
    todo = todo[: args.limit] if args.limit else todo
    print(f"extracting {len(todo)} videos with {args.model} ×{args.workers}", file=sys.stderr)
    spent, done = 0.0, 0
    with cf.ThreadPoolExecutor(args.workers) as ex:
        futs = {ex.submit(extract_one, vid, vids[vid], args.model, profile): vid for vid in todo}
        for f in cf.as_completed(futs):
            vid = futs[f]
            try:
                spent += f.result()
                done += 1
                print(f"[{done}/{len(todo)}] ${spent:.2f} {vid} {vids[vid]['title'][:70]}", file=sys.stderr)
            except Exception as e:
                print(f"FAIL {vid}: {e!s:.200}", file=sys.stderr)
    print(f"extracted {done}/{len(todo)}, ${spent:.2f}")


# ---------- synth (Sonnet) ----------

def load_notes() -> list[tuple[dict, dict]]:
    vids = video_map()
    out = []
    for p in NOTES.glob("*.json"):
        if p.stem in vids:
            out.append((vids[p.stem], json.loads(p.read_text())))
    out.sort(key=lambda vn: vn[0].get("upload_date") or "")
    return out


def compact(v: dict, n: dict, project: str | None = None) -> str:
    s = [f"### [{pretty_date(v.get('upload_date'))}] {v['title']} (`{v['id']}`, q{n['quality']}, "
         f"{chan_name(v)}, {n['format']})",
         n["one_line"],
         "Ideas: " + " | ".join(f"{k['idea']} [{k['t']}]" for k in n["key_ideas"][:6])]
    if n["techniques"]:
        s.append("Techniques: " + " | ".join(f"{t['name']}: {t['how']}" for t in n["techniques"][:4]))
    if n["numbers"]:
        s.append("Numbers: " + " | ".join(x["claim"] for x in n["numbers"][:3]))
    if project:
        s += [f"Why relevant: {r['why']} → {r['action']}" for r in n["relevance"] if r["project"] == project]
    return "\n".join(s)


def budgeted(items: list[tuple[dict, dict]], render, max_chars: int) -> str:
    """Keep the best items that fit, then restore date order (so the model sees evolution over time)."""
    ranked = sorted(items, key=lambda vn: (vn[1]["quality"], vn[0].get("upload_date") or ""), reverse=True)
    keep, total = [], 0
    for vn in ranked:
        block = render(*vn)
        if total + len(block) > max_chars:
            continue
        keep.append((vn[0].get("upload_date") or "", block))
        total += len(block)
    return "\n\n".join(b for _, b in sorted(keep))


TOPIC_SYSTEM = """You are a senior AI engineer writing a field guide from video notes: AI Engineer conference talks plus
creator channels (tutorials, tool reviews, news). Weigh conference talks with data above creator hype; say which is which.
Write Markdown with these sections:
## State of the art (what practitioners actually do now — most recent talks weigh most)
## Consensus patterns (numbered; each cites videos as `video_id`)
## Disagreements & open questions
## How thinking changed over time (dated)
## Numbers worth remembering (with `video_id`)
## Watch first (5-8 best videos: `video_id` — why)
## Implications for our projects (use the profile; concrete, cite `video_id`)
Cite only ids present in the notes. Be specific and dense; no filler. Plain, short sentences.

PROJECT PROFILE:
"""

INSIGHT_SYSTEM = """You are a principal engineer reviewing a project against everything the AI Engineer community and
the tracked creator channels have presented. Input: the project profile, optional project docs, and notes from talks flagged relevant.
Write Markdown:
## What we're doing right (validated by talks — cite `video_id`)
## Where we diverge from what practitioners found (risks, cite)
## Gaps: things we should build or change (ranked by impact/effort; each: what, why, evidence `video_id`, first step)
## Ideas to steal (specific techniques, tools, numbers)
## Reading list (top 10 videos for this project, `video_id` — why)
Be concrete and skeptical. Cite only ids present in the notes. Plain, short sentences.

PROJECT PROFILE:
"""


def cmd_synth(args) -> None:
    profile = (CONTEXT / "profile.md").read_text()
    notes = load_notes()
    jobs = []
    if args.what in ("all", "topics"):
        (KB / "guides").mkdir(parents=True, exist_ok=True)
        for t in (args.only.split(",") if args.only else TOPICS):
            items = [vn for vn in notes if t in vn[1]["topics"]]
            if len(items) >= 3:
                jobs.append(("topic", t, items))
    if args.what in ("all", "insights"):
        (KB / "insights").mkdir(parents=True, exist_ok=True)
        for p in (args.only.split(",") if args.only else PROJECTS[:-1]):
            items = [vn for vn in notes
                     if any(r["project"] == p and r["score"] >= 2 for r in vn[1]["relevance"])]
            if items:
                jobs.append(("insight", p, items))

    def run(job):
        kind, name, items = job
        if kind == "topic":
            body = budgeted(items, compact, args.max_chars)
            prompt = f"TOPIC: {name}\n{len(items)} videos tagged; best ones below.\n\n{body}"
            system = TOPIC_SYSTEM + profile
            out_path = KB / "guides" / f"{name}.md"
        else:
            docs = "".join(f"\n\n=== {p.name} ===\n{p.read_text()[:60_000]}"
                           for p in sorted(CONTEXT.glob(f"{name}*.md")))
            body = budgeted(items, lambda v, n: compact(v, n, name), args.max_chars)
            prompt = f"PROJECT: {name}{docs}\n\nRELEVANT TALK NOTES ({len(items)}):\n\n{body}"
            system = INSIGHT_SYSTEM + profile
            out_path = KB / "insights" / f"{name}.md"
        out = claude(prompt, system, args.model, timeout=1800)
        stamp = dt.date.today().isoformat()
        head = (f"# {'Guide' if kind == 'topic' else 'Insights'}: {name}\n\n"
                f"*Synthesized {stamp} by {args.model} from {len(items)} videos. "
                f"Open a video: `kb/videos/<id>.md`.*\n\n")
        out_path.write_text(head + out["result"].strip() + "\n")
        log_cost("synth", f"{kind}:{name}", args.model, out.get("total_cost_usd", 0))
        return name, out.get("total_cost_usd", 0)

    print(f"synthesizing {len(jobs)} docs with {args.model}", file=sys.stderr)
    with cf.ThreadPoolExecutor(args.workers) as ex:
        for f in cf.as_completed([ex.submit(run, j) for j in jobs]):
            try:
                name, usd = f.result()
                print(f"  {name} ${usd:.2f}", file=sys.stderr)
            except Exception as e:
                print(f"  FAIL {e!s:.200}", file=sys.stderr)


# ---------- index ----------

def cmd_index(args) -> None:
    KB.mkdir(exist_ok=True)
    notes = load_notes()
    db_path = KB / "search.db"
    db_path.unlink(missing_ok=True)
    db = sqlite3.connect(db_path)
    db.executescript("""
        CREATE TABLE videos(id TEXT PRIMARY KEY, channel TEXT, title TEXT, date TEXT, duration INT, quality INT,
                            depth TEXT, format TEXT, topics TEXT, tags TEXT, speakers TEXT, orgs TEXT,
                            one_line TEXT, rel_agentos INT, rel_gateway INT, rel_prosharness INT);
        CREATE VIRTUAL TABLE notes_fts USING fts5(id UNINDEXED, title, one_line, body, tags,
                                                   tokenize='porter unicode61');
        CREATE VIRTUAL TABLE lines_fts USING fts5(id UNINDEXED, t UNINDEXED, text,
                                                   tokenize='porter unicode61');
    """)
    for v, n in notes:
        rel = {r["project"]: r["score"] for r in n["relevance"]}
        db.execute("INSERT INTO videos VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                   (v["id"], chan(v), v["title"], pretty_date(v.get("upload_date")), v.get("duration"), n["quality"],
                    n["depth"], n["format"], ",".join(n["topics"]), ",".join(n["tags"]),
                    ", ".join(n["speakers"]), ", ".join(n["orgs"]), n["one_line"],
                    rel.get("agentos", 0), rel.get("gateway", 0), rel.get("prosharness", 0)))
        db.execute("INSERT INTO notes_fts VALUES (?,?,?,?,?)",
                   (v["id"], v["title"], n["one_line"],
                    (KB / "videos" / f"{v['id']}.md").read_text(),
                    " ".join(n["topics"] + n["tags"] + n["tools"])))
    noted = {v["id"] for v, _ in notes}
    for p in TRANSCRIPTS.glob("*.json"):
        if p.stem not in noted:  # lines_fts joins on videos; un-noted transcripts would never match
            continue
        for line in transcript_text(p.stem, para_seconds=20).splitlines():
            m = re.match(r"\[([\d:]+)\] (.*)", line)
            if m:
                db.execute("INSERT INTO lines_fts VALUES (?,?,?)", (p.stem, m[1], m[2]))
    db.commit()

    by_date = sorted(notes, key=lambda vn: vn[0].get("upload_date") or "", reverse=True)
    counts = {c: sum(chan(v) == c for v, _ in notes) for c in CHANNELS}
    row = lambda v, n: (f"| {pretty_date(v.get('upload_date'))} | {chan(v)} | [{v['title']}](videos/{v['id']}.md) "
                        f"| {n['quality']} | {', '.join(n['topics'])} |")
    hdr = ["| date | channel | video | q | topics |", "|---|---|---|---|---|"]
    cat_counts = {t: sum(t in n["topics"] for _, n in notes) for t in TOPICS}
    (KB / "INDEX.md").write_text("\n".join(
        [f"# YouTube knowledge base — {len(notes)} videos with notes", "",
         "Channels: " + " · ".join(f"[{CHANNELS[c]['name']}](channels/{c}.md) ({counts[c]})" for c in CHANNELS), "",
         "Categories: " + " · ".join(f"[{t}](categories/{t}.md) ({cat_counts[t]})" for t in TOPICS),
         "", "Insights: " + " · ".join(f"[{p}](insights/{p}.md)" for p in PROJECTS
                                     if (KB / "insights" / f"{p}.md").exists()), "", *hdr]
        + [row(v, n) for v, n in by_date]) + "\n")

    def entry(v, n, slug=None):
        also = [t for t in n["topics"] if t != slug]
        out = [f"## [{v['title']}](../videos/{v['id']}.md)",
               f"`{v['id']}` · {chan_name(v)} · {pretty_date(v.get('upload_date'))} · q{n['quality']} · {n['depth']} · "
               f"{n['format']} · {'also' if slug else 'topics'}: {', '.join(also) or '—'}",
               f"\n{n['one_line']}"]
        if n["techniques"]:
            out.append("\n- Techniques: " + "; ".join(t["name"] for t in n["techniques"]))
        if n["tools"]:
            out.append("- Tools: " + ", ".join(n["tools"][:12]))
        return out + [""]

    (KB / "categories").mkdir(exist_ok=True)
    for slug, desc in CATEGORIES.items():
        items = [vn for vn in by_date if slug in vn[1]["topics"]]
        guide = KB / "guides" / f"{slug}.md"
        per = {c: sum(chan(v) == c for v, _ in items) for c in CHANNELS}
        page = [f"# {slug} — {len(items)} videos", "", f"*{desc}*", "",
                "By channel: " + " · ".join(f"{CHANNELS[c]['name']} {k}" for c, k in per.items() if k), ""]
        if guide.exists():
            page += [f"**Synthesized guide:** [guides/{slug}.md](../guides/{slug}.md)", ""]
        page += ["Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.", ""]
        for v, n in items:
            page += entry(v, n, slug)
        (KB / "categories" / f"{slug}.md").write_text("\n".join(page) + "\n")

    (KB / "channels").mkdir(exist_ok=True)
    for c, meta in CHANNELS.items():
        items = [vn for vn in by_date if chan(vn[0]) == c]
        listed = sum(chan(v) == c for v in load_videos())
        top = sorted({t for _, n in items for t in n["topics"]},
                     key=lambda t: -sum(t in n["topics"] for _, n in items))
        page = [f"# {meta['name']} ({meta['handle']}) — {len(items)} of {listed} videos have notes", "",
                f"*{meta['desc']}* · [channel]({meta['url']})", "",
                "Top categories: " + " · ".join(
                    f"[{t}](../categories/{t}.md) ({sum(t in n['topics'] for _, n in items)})" for t in top[:12]), "",
                "Newest first.", ""]
        for v, n in items:
            page += entry(v, n)
        (KB / "channels" / f"{c}.md").write_text("\n".join(page) + "\n")

    cutoff = (dt.date.today() - dt.timedelta(days=args.latest_days)).strftime("%Y%m%d")
    recent = [vn for vn in by_date if (vn[0].get("upload_date") or "") >= cutoff]
    (KB / "latest.md").write_text("\n".join(
        [f"# Latest {args.latest_days} days ({len(recent)} videos), best first", ""]
        + [f"- **{pretty_date(v.get('upload_date'))}** [{v['title']}](videos/{v['id']}.md) · {chan_name(v)} · "
           f"q{n['quality']} — {n['one_line']}"
           for v, n in sorted(recent, key=lambda vn: -vn[1]["quality"])]) + "\n")
    print(f"indexed {len(notes)} videos → kb/search.db, kb/INDEX.md, kb/latest.md, kb/channels/, kb/categories/")


# ---------- query ----------

def cmd_search(args) -> None:
    db = sqlite3.connect(KB / "search.db")
    q = args.query
    if args.transcripts:
        rows = db.execute("SELECT l.id, l.t, v.title, snippet(lines_fts, 2, '«', '»', '…', 24) "
                          "FROM lines_fts l JOIN videos v ON v.id = l.id WHERE lines_fts MATCH ? "
                          "ORDER BY rank LIMIT ?", (q, args.limit)).fetchall()
        for vid, t, title, snip in rows:
            print(f"{vid} [{t}] {title[:60]}\n    {snip}\n    {yt_link(vid, t)}")
        return
    where, params = "notes_fts MATCH ?", [q]
    if want := want_channels(args.channel):
        where += f" AND v.channel IN ({','.join('?' * len(want))})"
        params += sorted(want)
    if args.since:
        where += " AND v.date >= ?"
        params.append(args.since)
    if args.min_quality:
        where += " AND v.quality >= ?"
        params.append(args.min_quality)
    order = "v.date DESC" if args.recent else "rank"
    rows = db.execute(f"SELECT v.id, v.date, v.quality, v.channel, v.title, v.one_line FROM notes_fts n "
                      f"JOIN videos v ON v.id = n.id WHERE {where} ORDER BY {order} LIMIT ?",
                      (*params, args.limit)).fetchall()
    for vid, date, q_, ch, title, one in rows:
        print(f"{vid} {date} q{q_} [{ch}] {title}\n    {one}")


def cmd_show(args) -> None:
    print((KB / "videos" / f"{args.id}.md").read_text())


# ---------- Workflow bridge (Claude Code Workflow tool: Haiku extract / Sonnet synth agents) ----------

WF = DATA / "wf"


def cmd_wf_prep_extract(args) -> None:
    """Write data/wf/text/<id>.txt for videos needing notes; print their ids as JSON (the workflow's args)."""
    (WF / "text").mkdir(parents=True, exist_ok=True)
    vids = video_map()
    want = want_channels(args.channel)
    ids = sorted((vid for vid in vids
                  if in_channels(vids[vid], want)
                  and (TRANSCRIPTS / f"{vid}.json").exists() and not (NOTES / f"{vid}.json").exists()
                  and (vids[vid].get("upload_date") or "") >= args.since),
                 key=lambda x: vids[x].get("upload_date") or "", reverse=True)
    ids = ids[: args.limit] if args.limit else ids
    # numbered queue: workflows take a count and each agent reads its id from the file header,
    # so nobody (model or human) has to copy hundreds of ids into the workflow args
    qname = getattr(args, "queue", "") or "queue"
    queue = WF / qname
    queue.mkdir(parents=True, exist_ok=True)
    for old in queue.glob("q*.txt"):
        old.unlink()
    for i, vid in enumerate(ids):
        text = video_header(vids[vid]) + f"\nTRANSCRIPT:\n{transcript_text(vid)}\n"
        (WF / "text" / f"{vid}.txt").write_text(text)
        (queue / f"q{i:04d}.txt").write_text(text)
    (WF / "extract_system.md").write_text(EXTRACT_SYSTEM + (CONTEXT / "profile.md").read_text())
    # the workflow's args: queue size + the live taxonomy (so editing categories.md needs no JS change)
    out = {"queue": len(ids), "queueDir": qname, "ids": ids, "cats": TOPICS, "formats": FORMATS}
    if args.out:
        Path(args.out).write_text(json.dumps(out))
        print(f"{len(ids)} ids → {args.out}", file=sys.stderr)
    print(json.dumps(out))


def cmd_wf_prep_synth(args) -> None:
    """Write one input file per category / project for the Sonnet synth agents; print the job list."""
    out = WF / "synth"
    out.mkdir(parents=True, exist_ok=True)
    want = want_channels(args.channel)
    notes = [vn for vn in load_notes()
             if (vn[0].get("upload_date") or "") >= args.since and in_channels(vn[0], want)]
    if args.ids:  # only categories touched by these videos (incremental refresh after an update)
        fresh = set(args.ids.split(","))
        notes = [vn for vn in notes if vn[0]["id"] in fresh]
    jobs = []
    for slug, desc in CATEGORIES.items():
        items = [vn for vn in notes if slug in vn[1]["topics"]]
        if len(items) >= (1 if args.ids else 3):
            (out / f"cat_{slug}.md").write_text(
                f"CATEGORY: {slug} — {desc}\n{len(items)} videos since {pretty_date(args.since)}; best ones below, "
                f"oldest first.\n\n{budgeted(items, compact, args.max_chars)}\n")
            jobs.append({"kind": "category", "name": slug, "n": len(items),
                         "ids": [v["id"] for v, _ in items] if args.ids else [],
                         "has_guide": (KB / "guides" / f"{slug}.md").exists()})
    for p in PROJECTS[:-1]:
        items = [vn for vn in notes if any(r["project"] == p and r["score"] >= 2 for r in vn[1]["relevance"])]
        if items and not args.no_projects:
            (out / f"proj_{p}.md").write_text(
                f"PROJECT: {p}\n{len(items)} talks flagged relevant (score>=2).\n\n"
                f"{budgeted(items, lambda v, n: compact(v, n, p), args.max_chars)}\n")
            jobs.append({"kind": "project", "name": p, "n": len(items)})
    (out / "topic_system.md").write_text(TOPIC_SYSTEM + (CONTEXT / "profile.md").read_text())
    (out / "insight_system.md").write_text(INSIGHT_SYSTEM + (CONTEXT / "profile.md").read_text())
    print(json.dumps(jobs))


def _find_notes(obj):
    if isinstance(obj, dict):
        if {"id", "one_line", "key_ideas", "topics"} <= obj.keys():
            yield obj
        for v in obj.values():
            yield from _find_notes(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _find_notes(v)
    elif isinstance(obj, str) and obj.lstrip().startswith("{") and '"one_line"' in obj:
        try:
            yield from _find_notes(json.loads(obj))
        except json.JSONDecodeError:
            pass


WF_RUNS = Path.home() / ".claude" / "projects" / str(ROOT).replace("/", "-")


def recent_journals(hours: float = 12) -> list[Path]:
    """This project's workflow journals touched in the last `hours`, oldest first (so newer notes win).

    A running workflow (and any nested child workflow) keeps appending, so its journal is always included.
    """
    cutoff = time.time() - hours * 3600
    js = sorted((p for p in WF_RUNS.glob("*/subagents/workflows/*/journal.jsonl") if p.stat().st_mtime >= cutoff),
                key=lambda p: p.stat().st_mtime)
    if not js:
        sys.exit(f"no workflow journals under {WF_RUNS} in the last {hours}h")
    return js


def cmd_wf_import(args) -> None:
    """Pull Haiku notes out of a workflow journal.jsonl into data/notes + kb/videos."""
    (KB / "videos").mkdir(parents=True, exist_ok=True)
    NOTES.mkdir(parents=True, exist_ok=True)
    vids = video_map()
    only = set(args.ids.split(",")) if args.ids else None
    journals = recent_journals() if args.latest or not args.journal else [Path(args.journal)]
    print(f"importing from {len(journals)} journal(s), newest {journals[-1]}", file=sys.stderr)
    saved = bad = 0
    seen: set[str] = set()
    for line in (l for j in journals for l in j.read_text().splitlines()):
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        for note in _find_notes(rec):
            vid = note.pop("id")
            if only is not None and vid not in only:
                continue
            if vid not in vids:
                bad += 1
                continue
            note["topics"] = [t for t in note["topics"] if t in CATEGORIES] or ["models-research"]
            note.setdefault("_model", "haiku-workflow")
            note["_at"] = dt.datetime.now().isoformat(timespec="seconds")
            try:
                md = render_video_md(vid, vids[vid], note)
            except (KeyError, TypeError) as e:
                print(f"skip {vid}: {e!r}", file=sys.stderr)
                bad += 1
                continue
            (NOTES / f"{vid}.json").write_text(json.dumps(note, ensure_ascii=False, indent=1))
            (KB / "videos" / f"{vid}.md").write_text(md)
            saved += 1
            seen.add(vid)
    print(f"imported {len(seen)} notes ({saved} writes, {bad} skipped)")


def cmd_wf_prep_retag(args) -> None:
    """Batch existing notes for a Haiku re-tag pass (after categories.md gains categories); print the job list."""
    out = WF / "retag"
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("batch_*.md"):
        old.unlink()
    want = want_channels(args.channel)
    notes = [vn for vn in load_notes() if in_channels(vn[0], want)]
    jobs = []
    for i in range(0, len(notes), args.batch):
        chunk = notes[i:i + args.batch]
        body = "\n\n".join(
            f"### `{v['id']}` {v['title']}\nCurrent topics: {', '.join(n['topics'])}\nTags: {', '.join(n['tags'])}\n"
            f"{n['one_line']}\nTechniques: {'; '.join(t['name'] for t in n['techniques'][:6])}\n"
            f"Tools: {', '.join(n['tools'][:12])}" for v, n in chunk)
        path = out / f"batch_{i // args.batch:03d}.md"
        path.write_text(body + "\n")
        jobs.append({"file": str(path), "ids": [v["id"] for v, _ in chunk]})
    (out / "categories.md").write_text("\n".join(f"- {k}: {v}" for k, v in CATEGORIES.items()) + "\n")
    (out / "jobs.json").write_text(json.dumps(jobs))
    print(json.dumps({"batches": len(jobs), "cats": TOPICS}))


def _find_retags(obj):
    if isinstance(obj, dict):
        if isinstance(obj.get("retags"), list):
            yield from obj["retags"]
        for v in obj.values():
            yield from _find_retags(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _find_retags(v)
    elif isinstance(obj, str) and '"retags"' in obj:
        try:
            yield from _find_retags(json.loads(obj))
        except json.JSONDecodeError:
            pass


def cmd_wf_import_retag(args) -> None:
    """Apply topic lists from a retag workflow journal to data/notes and re-render kb/videos."""
    vids = video_map()
    changed = same = bad = 0
    journals = recent_journals() if args.latest or not args.journal else [Path(args.journal)]
    for line in (l for j in journals for l in j.read_text().splitlines()):
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        for r in _find_retags(rec):
            vid, topics = r.get("id"), [t for t in r.get("topics", []) if t in CATEGORIES][:4]
            path = NOTES / f"{vid}.json"
            if vid not in vids or not path.exists() or not topics:
                bad += 1
                continue
            note = json.loads(path.read_text())
            if note["topics"] == topics:
                same += 1
                continue
            note["topics"] = topics
            path.write_text(json.dumps(note, ensure_ascii=False, indent=1))
            (KB / "videos" / f"{vid}.md").write_text(render_video_md(vid, vids[vid], note))
            changed += 1
    print(f"retag: {changed} changed, {same} unchanged, {bad} skipped")


def cmd_rerender(args) -> None:
    """Re-render kb/videos/*.md from data/notes (after a template change)."""
    vids = video_map()
    n = 0
    for p in NOTES.glob("*.json"):
        if p.stem in vids:
            (KB / "videos" / f"{p.stem}.md").write_text(render_video_md(p.stem, vids[p.stem], json.loads(p.read_text())))
            n += 1
    print(f"re-rendered {n} notes")


def cmd_update_prep(args) -> None:
    """Incremental update, step 1: list channels → transcribe new videos (Whisper on GPU) → stage for Haiku.

    Writes the workflow args ({ids, cats, formats, since, today}) to --out and prints them.
    """
    cmd_list(args)
    want = want_channels(args.channel)
    failed = json.loads(FAILED.read_text()) if FAILED.exists() else {}
    need = sorted((v for v in load_videos()
                   if in_channels(v, want) and (v.get("upload_date") or "") >= args.since
                   and (v.get("duration") or 0) >= 240 and v["id"] not in failed
                   and not (TRANSCRIPTS / f"{v['id']}.json").exists()),
                  key=lambda v: v.get("upload_date") or "", reverse=True)[: args.limit]
    if need and not args.no_whisper:
        print(f"transcribing {len(need)} new videos with Whisper…", file=sys.stderr)
        subprocess.run([str(ROOT / "pipeline" / "whisper_fetch.py"), "--ids", ",".join(v["id"] for v in need)],
                       cwd=ROOT, stdout=sys.stderr)
    out_file = args.out
    args.out = ""  # cmd_wf_prep_extract prints; we write the enriched version ourselves
    import contextlib, io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        cmd_wf_prep_extract(args)
    payload = json.loads(buf.getvalue())
    payload.update(since=args.since, today=dt.date.today().isoformat())
    Path(out_file).write_text(json.dumps(payload))
    result = {"queue": payload["queue"], "queueDir": payload["queueDir"], "today": payload["today"]}
    # kb-update.js relies on kb-extract.js's built-in category list; flag drift from context/categories.md
    js = (ROOT / "pipeline" / "workflows" / "kb-extract.js").read_text()
    m = re.search(r"A\.cats \|\| \[(.*?)\]", js, re.S)
    if not m or re.findall(r"'([a-z0-9-]+)'", m[1]) != TOPICS:
        result["warning"] = "kb-extract.js fallback CATS differ from context/categories.md: update the list in kb-extract.js"
    print(json.dumps(result))


def cmd_status(args) -> None:
    vids = load_videos()
    failed = json.loads(FAILED.read_text()) if FAILED.exists() else {}
    costs = [json.loads(l) for l in COSTS.read_text().splitlines()] if COSTS.exists() else []
    spend: dict[str, float] = {}
    for c in costs:
        spend[c["model"]] = spend.get(c["model"], 0) + c["usd"]
    print(f"videos {len(vids)} · transcripts {len(list(TRANSCRIPTS.glob('*.json')))} "
          f"(no captions: {len(failed)}) · notes {len(list(NOTES.glob('*.json')))}")
    for c in CHANNELS:
        vs = [v for v in vids if chan(v) == c]
        long_ = [v for v in vs if (v.get("duration") or 0) >= 240]
        tr = sum((TRANSCRIPTS / f"{v['id']}.json").exists() for v in vs)
        nt = sum((NOTES / f"{v['id']}.json").exists() for v in vs)
        print(f"  {c:12} videos {len(vs):5} (≥4 min {len(long_):5}) · transcripts {tr:5} · notes {nt:5}")
    print("spend (API-equivalent): " + ", ".join(f"{m} ${u:.2f}" for m, u in spend.items()))


def cmd_run(args) -> None:
    cmd_list(args)
    cmd_fetch(args)
    cmd_extract(args)
    cmd_index(args)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def fetch_opts(p):
        p.add_argument("--limit", type=int, default=0)
        p.add_argument("--sleep", type=float, default=1.0)
        p.add_argument("--retry", action="store_true", help="retry videos that had no captions")
        p.add_argument("--min-seconds", type=int, default=240, help="skip shorts/trailers")
        p.add_argument("--since", default="", help="YYYYMMDD upload-date floor")
        p.add_argument("--oldest-first", action="store_true")
        p.add_argument("--channel", default="", help="comma list of channel slugs (context/channels.md)")

    def extract_opts(p):
        p.add_argument("--model", default="haiku")
        p.add_argument("--workers", type=int, default=8)
        p.add_argument("--force", action="store_true")
        p.add_argument("--ids", default="")
        p.add_argument("--extract-limit", dest="limit", type=int, default=0)

    p = sub.add_parser("list"); p.add_argument("--channel", default=""); p.set_defaults(fn=cmd_list)
    fetch_opts(p := sub.add_parser("fetch")); p.set_defaults(fn=cmd_fetch)
    p = sub.add_parser("extract"); extract_opts(p); p.add_argument("--limit", type=int, default=0)
    p.add_argument("--channel", default="")
    p.set_defaults(fn=cmd_extract)
    p = sub.add_parser("synth")
    p.add_argument("what", nargs="?", default="all", choices=["all", "topics", "insights"])
    p.add_argument("--only", default="", help="comma list of topics or projects")
    p.add_argument("--model", default="sonnet")
    p.add_argument("--workers", type=int, default=4)
    p.add_argument("--max-chars", type=int, default=300_000)
    p.set_defaults(fn=cmd_synth)
    p = sub.add_parser("index"); p.add_argument("--latest-days", type=int, default=60); p.set_defaults(fn=cmd_index)
    p = sub.add_parser("search")
    p.add_argument("query")
    p.add_argument("--limit", type=int, default=15)
    p.add_argument("--transcripts", action="store_true", help="search raw transcript lines (with timestamps)")
    p.add_argument("--since", help="YYYY-MM-DD")
    p.add_argument("--min-quality", type=int, default=0)
    p.add_argument("--recent", action="store_true", help="sort by date instead of relevance")
    p.add_argument("--channel", default="", help="comma list of channel slugs")
    p.set_defaults(fn=cmd_search)
    p = sub.add_parser("show"); p.add_argument("id"); p.set_defaults(fn=cmd_show)
    sub.add_parser("status").set_defaults(fn=cmd_status)
    p = sub.add_parser("wf-prep-extract"); p.add_argument("--since", default=""); p.add_argument("--limit", type=int, default=0)
    p.add_argument("--channel", default=""); p.add_argument("--out", default="", help="also write the args JSON here")
    p.add_argument("--queue", default="queue", help="queue dir name under data/wf (one per concurrent extraction run)")
    p.set_defaults(fn=cmd_wf_prep_extract)
    p = sub.add_parser("wf-prep-synth"); p.add_argument("--since", default="")
    p.add_argument("--channel", default=""); p.add_argument("--ids", default="", help="only these new videos (update mode)")
    p.add_argument("--no-projects", action="store_true")
    p.add_argument("--max-chars", type=int, default=250_000); p.set_defaults(fn=cmd_wf_prep_synth)
    p = sub.add_parser("wf-import"); p.add_argument("journal", nargs="?", default="")
    p.add_argument("--latest", action="store_true", help="every journal of this project touched in the last 12h")
    p.add_argument("--ids", default="", help="only import these ids"); p.set_defaults(fn=cmd_wf_import)
    p = sub.add_parser("update-prep"); p.add_argument("--since", default="20260518")
    p.add_argument("--channel", default=""); p.add_argument("--limit", type=int, default=60)
    p.add_argument("--no-whisper", action="store_true"); p.add_argument("--out", default=str(DATA / "wf" / "update_args.json"))
    p.add_argument("--queue", default="queue_update")
    p.set_defaults(fn=cmd_update_prep)
    p = sub.add_parser("wf-prep-retag"); p.add_argument("--channel", default=""); p.add_argument("--batch", type=int, default=25)
    p.set_defaults(fn=cmd_wf_prep_retag)
    p = sub.add_parser("wf-import-retag"); p.add_argument("journal", nargs="?", default="")
    p.add_argument("--latest", action="store_true"); p.set_defaults(fn=cmd_wf_import_retag)
    sub.add_parser("rerender").set_defaults(fn=cmd_rerender)
    p = sub.add_parser("run"); fetch_opts(p); extract_opts(p)
    p.add_argument("--latest-days", type=int, default=60); p.set_defaults(fn=cmd_run)

    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
