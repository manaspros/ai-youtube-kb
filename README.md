# AI YouTube knowledge base

Structured, searchable notes on 1926 videos from these YouTube channels, organized by topic
(Claude Code, token/cost efficiency, PR review, evals, MCP, local AI, inference, agents, dev tools, ...):

- **AI Engineer** (@aiDotEngineer): conference talks and workshops on AI engineering, agents, infra
- **Kai Explains** (@kaiexplainsYT): local AI hardware, open-weight models, inference speedups, AI news
- **AI LABS** (@AILABS-393): Claude Code and AI-coding workflows, new tools, build-with-AI tutorials
- **Better Stack** (@betterstack): dev tools, Claude Code tips, cost/token tricks, logging and observability tutorials

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
