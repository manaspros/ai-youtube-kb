# YouTube knowledge base (AI Engineer + creator channels)

Every video on the channels in `context/channels.md` → transcript → Haiku notes → guides → markdown KB, organized by topic.
Channels: `aie` AI Engineer (conference talks, since 2026-05-18), `kai` Kai Explains (local AI, hardware, news),
`ailabs` AI LABS (Claude Code / AI-coding workflows), `betterstack` Better Stack (dev tools, Claude Code tips, cost tricks).
Use it to answer "what do practitioners do about X", "what's new", "how do I do X in Claude Code", and
creator videos are where the hands-on commands, settings and tool comparisons live.

## Navigate (cheapest first)
0. `kb/trends.md` — what changed over the window + ranked "do this now" for each project. Read first.
1. `kb/INDEX.md` — every video, newest first: date, channel, title, quality (1-5), categories. Links to channels, categories, insights.
   `kb/channels/<slug>.md` — one channel's videos, newest first.
2. `kb/latest.md` — last 60 days, best first. Start here for "what's new".
3. `kb/insights/<project>.md` — Sonnet review per project (agentos, gateway, prosharness): what we do right, gaps, ideas to steal, reading list.
4. `kb/guides/<category>.md` — field guide per category: state of the art, consensus, disagreements, how thinking changed,
   watch-first; plus "## What's new" (dated, from updates) and "## From creator channels" (playbook, commands, tools).
   Topic examples: `claude-code`, `token-cost-efficiency`, `pr-code-review`, `local-ai`, `vibe-coding-app-building`, `dev-tools`.
5. `kb/categories/<slug>.md` — every video in a category with one-liner, techniques, tools (newest first). Category list + meanings: `context/categories.md`.
6. `kb/videos/<id>.md` — full notes for one video: summary, timestamped key ideas (deep links), techniques, numbers, hot takes, relevance to our projects.
7. Raw transcript only if the notes miss a detail: `data/transcripts/<id>.json` (segments `[start_sec, text]`).

## Search
```bash
./pipeline/aie.py search "kv cache offload"               # notes, ranked (FTS5: AND/OR/NEAR, "phrases", prefix*)
./pipeline/aie.py search "code review" --recent --since 2026-06-01 --min-quality 4
./pipeline/aie.py search "usage limits" --channel betterstack,ailabs        # one or more channels
./pipeline/aie.py search "merkle audit" --transcripts     # raw transcript lines with timestamp links
./pipeline/aie.py show <id>
sqlite3 kb/search.db "select id,date,title from videos where rel_agentos>=2 order by date desc limit 20"
```
`videos` columns: id, channel, title, date, duration, quality, depth, format, topics, tags, speakers, orgs, one_line, rel_agentos, rel_gateway, rel_prosharness (0-3).

## Answering rules
- Cite videos as `title (id, date)` and link timestamps from the notes. Notes are Haiku paraphrases of auto-captions: for a key claim, check the transcript.
- Prefer recent + high-quality videos; say when the evidence is a single anecdotal talk or a vendor pitch.

## Updating (Haiku-only: routine updates never use Sonnet)
- **Routine update = one workflow:** run `pipeline/workflows/kb-update.js` with the Workflow tool (args optional:
  `{since: "20260518", channel: "aie", limit: 60}`). Haiku agents: `update-prep` (list every channel, Whisper the new
  videos, stage a numbered queue) → extract one note per video → `wf-import --latest` + `index` → add each new video to the
  "What's new" section of its guides/insights → refresh `kb/trends.md` "Latest updates".
- Headless fallback (no workflow): `./pipeline/aie.py run` (list → captions → Haiku `claude -p` notes → index).
- `./pipeline/aie.py status` — per-channel counts. Add a channel = one line in `context/channels.md`, then a full build:
  `whisper_fetch.py --channel <slug>` → `wf-prep-extract --channel <slug>` → `kb-extract.js` with `{queue: N, cats, formats}`
  (≤900 per run; use `offset`/`count`) → `wf-import --latest` → `index` → `wf-prep-synth --channel <slug>` →
  `kb-guides.js` with `{jobs, mode: "creators", since, today}`.
- Edit `context/profile.md` (what we build) or `context/categories.md` (taxonomy). After adding a category: mirror it in the
  fallback `CATS` list in `pipeline/workflows/kb-extract.js`, then `wf-prep-retag` → `kb-retag.js` → `wf-import-retag --latest`.
  `context/<project>*.md` files (e.g. the `agentos-roadmap.md` symlink) are fed to that project's insight pass.
- Sonnet rebuild of guides (only when asked): `wf-prep-synth --since 20260518` → `pipeline/workflows/aie-synth.js`.

## Transcripts
YouTube rate-limits (often blocks outright) the caption API (`aie.py fetch`). `pipeline/whisper_fetch.py [--channel ..] [--since YYYYMMDD]`
downloads audio and transcribes on the RTX 5090 (faster-whisper large-v3-turbo, ~280x realtime), newest first.
