# Guide: claude-code

*Synthesized 2026-11-02 by Haiku from 192 videos. Open a video: `kb/videos/<id>.md`.*

Most sources here are creator videos (Kai Explains, AI LABS, Better Stack). Conference talks are marked "(talk)". Creator claims are often one speaker's test, and some sit in sponsored segments. Those are flagged below.

## State of the art (what practitioners actually do now — most recent talks weigh most)

- **Claude Code runs as a fleet, not one chat.** A KRAFTON engineer runs agents on three machines with file-backed state and clear-and-reload instead of compaction (`4kYl2_mqmnQ`, talk). A WorkOS workshop runs 8 or more terminal sessions at once (`AgBAOXVxt4A`, talk).
- **Loops need a checkable finish line.** Creators agree `/goal` is the loop primitive, not `/loop` (`PLyRe6Zk--8`). Anthropic's own long-run harness splits a planner, a generator and an evaluator that tests the live app (`mR-WAvEPRwE`, talk).
- **Skills are routers.** Only the name and description load by default. The body and reference files load when needed (`pFsfax19yOM`, `GmAQKINjv1E`, talk). Each model-invoked skill adds its description to every request (`UNzCG3lw6O0`, talk).
- **Token cost is the main creator topic from September to November 2026.** Every message resends the whole conversation (`jwje1JK8Nqs`). Overhead loads before the first prompt: system prompt, CLAUDE.md, memory, skills, and each MCP server (`FWShtLCP4OY`). Tool schemas stay in context all session, while a CLI loads only when called (`jwje1JK8Nqs`).
- **Hidden cost sources.** Background-agent summaries make extra model calls (`F4h3a8HFBSE`). Connectors and artifacts load into every session (`i6Q7bXnWGlM`). Long command output fills context unless it is capped or filtered (`jwje1JK8Nqs`).
- **Cheaper or open models run through the same client.** This works by environment variable or a local proxy (`M48WuCSjmHs`, `vxrZWbZ2fZA`). OpenCode is a separate open-source client that also takes other models (`wOfm7x0i3sw`). Creators say the harness, not the model, is where lock-in sits (`jtWjkdBNqlk`).
- **Mods are a new extension layer.** Mods are in-process TypeScript plugins that can draw panes and status lines (`EiThSVZ8pME`, `ERNqRK6sMJY`). Creators describe them as distinct from hooks, which run outside the process.
- **Security.** Project config is code. A Claude Code SessionStart hook in a repo's settings file can run a payload on folder open (`lNsSxWQDqaU`, single news video).

## Consensus patterns (numbered; each cites videos as `video_id`)

1. Write the verification check before the loop starts, and keep the human in charge of it. Use a loop only where the work needs repeated back-and-forth (`PLyRe6Zk--8`, `qLfSDQ5NGh0`, `5TNXByrtHc4`).
2. Never let the builder judge its own work. Use a fresh-context reviewer, ideally on a different model (`PLyRe6Zk--8`, `92ZDgn8bgLM`, `mR-WAvEPRwE`).
3. Keep always-loaded files small. Move detail into nested CLAUDE.md files, skills and reference files (`D4uBfIe7SzA`, `jwje1JK8Nqs`, `UNzCG3lw6O0`).
4. Build CLAUDE.md from real mistakes. Keep only what the agent cannot learn by reading the code (`D4uBfIe7SzA`, `i6Q7bXnWGlM`).
5. Clear between unrelated tasks, batch related edits into one prompt, and rewind a bad turn instead of correcting it on top (`jwje1JK8Nqs`).
6. Set effort per task. Medium is the usual default. Raise it for hard debugging (`jwje1JK8Nqs`, `SxLUx8-hN1o`, `FWShtLCP4OY`).
7. Log output tokens, tool-call counts and app version with every score (`SxLUx8-hN1o`).
8. Put hooks on the path as hard gates. Run lint, types and tests after writes, and block PR creation until they pass (`AgBAOXVxt4A`). For risky actions, require a plan ID before apply (`HTscIrJhjDs`).
9. Interview the human before planning, and keep a shared glossary (`v4F1gFy-hqg`, talk).
10. Audit the whole setup after each model release. Remove instructions written for older models, such as "think carefully" (`i6Q7bXnWGlM`, `5TNXByrtHc4`, `7au4tWVG8a0`).

## Disagreements & open questions

- **CLAUDE.md size.** One creator sets a 500-line ceiling (`D4uBfIe7SzA`). Another says 200 lines for CLAUDE.md and SKILL.md (`jwje1JK8Nqs`). Both are rules of thumb. Neither shows a measurement.
- **Compaction.** One creator argues that compaction loses information that compounds over long sessions (`_DZ4kJwQ50s`, single creator, vendor benchmarks). Another says to compact on purpose, with keep-instructions, before a break (`jwje1JK8Nqs`). Likely both are right. Compact for short gaps, and keep state on disk for long runs.
- **Background-summary cost.** Community reports say 8 to 10 percent of usage, and one team estimate says 15 to 20 percent. Anthropic's team member said about 2 percent overall and about 6 percent in the terminal (`F4h3a8HFBSE`). Open. Measure it yourself with OTel.
- **Effort.** Benchmarks run at max effort, but defaults are lower (`SxLUx8-hN1o`). One creator says to start at low and escalate on evidence (`7au4tWVG8a0`). Open.
- **Harness or model?** One creator says the harness drives much of the score and cost (`qXo1P5H2RXk`). Another says a model swap works only if the model handles tool calls well (`M48WuCSjmHs`). Open.
- **Cheap-model routing.** Creators pitch it as a cost cut (`vxrZWbZ2fZA`, `M48WuCSjmHs`). Both say to send routine work (renames, refactors, glue code) to the cheap model and keep a frontier model for hard bugs.
- **Loops as a productivity claim.** The "10x" claim is not measured (`qLfSDQ5NGh0`). One anecdote reports 19 percent after an overnight loop. Use a loop-fit test first.
- **Price per task.** One review says cost per completed task matters more than list price (`JR9emVyAQTY`). It also warns that promotional pricing changes the answer. Single creator.
- **Firewalls.** A command-text firewall is not a sandbox (`Afm-GNrJbEQ`). A conference talk pushes async scanning hooks instead (`cgimkNGNjvU`, talk, vendor). Not settled.

## How thinking changed over time (dated)

- **2026-04-02.** `/loop` is framed as in-session polling. Cron jobs expire after three days and live only in session memory (`Xxqu-kz00gw`).
- **2026-05-18.** Skill descriptions are treated as routing rules. Constraints beat long prose (`pFsfax19yOM`, `GmAQKINjv1E`, talk).
- **2026-06-18.** Long runs need a separate evaluator. A single agent loop cannot finish multi-hour apps (`mR-WAvEPRwE`, talk).
- **2026-08-02.** Cost per task replaces list price as the frame (`JR9emVyAQTY`). Creators start to treat the harness as a lock-in point (`jtWjkdBNqlk`).
- **2026-09-02.** `/goal` replaces `/loop` as the loop tool (`PLyRe6Zk--8`). CLAUDE.md becomes a failure log (`D4uBfIe7SzA`). Token-limit tactics go mainstream (`jwje1JK8Nqs`).
- **2026-10-02 to 2026-10-12.** Setup hygiene: prune skills and connectors (`i6Q7bXnWGlM`). Effort defaults and the "nerf" debate (`SxLUx8-hN1o`). Opus 5.5 prompting advice (`5TNXByrtHc4`).
- **2026-11-01.** Hidden agent calls and cost gateways (`F4h3a8HFBSE`, `Afm-GNrJbEQ`).

## Numbers worth remembering (with `video_id`)

- About 70k tokens of fixed overhead before the first prompt. This is the speaker's own estimate (`FWShtLCP4OY`).
- Tool descriptions for 27 tools are about 33k tokens. This is secondhand (`_DZ4kJwQ50s`).
- Background summaries fire about every 30 seconds per working agent. They were about 12 percent of cost in one sleep test and about 8 percent in an Opus build (`F4h3a8HFBSE`).
- Cache reads cost about a tenth of normal input (speaker's figure, `jwje1JK8Nqs`).
- High to medium effort: output tokens down 26 percent. The score moved 4.2 points, below a 6.6-point detection threshold (`SxLUx8-hN1o`).
- Bash output cap lowered from 30,000 to 10,000 characters (`jwje1JK8Nqs`).
- NASA log test through a gateway: 68 cents direct versus 47 cents, one run each (`Afm-GNrJbEQ`).
- Opus 5.5 per-token price: $5 and $25 per million, cut to $4 and $20 (`SxLUx8-hN1o`).
- Agent horizon for 50 percent task completion: about 1 hour to about 12 hours across model generations (`mR-WAvEPRwE`, talk).
- Semantic code search lifted file precision from about 65 to about 87 percent (`zKk7sDMGDEQ`, talk, vendor).

## Watch first (5-8 best videos: `video_id` — why)

- `PLyRe6Zk--8` — the three levels of loop engineering, with `/goal`, a reviewer per branch and the steps shown. Practical.
- `jwje1JK8Nqs` — 24 usage tactics, each with the reason it costs tokens. Mostly the speaker's own unmeasured numbers.
- `F4h3a8HFBSE` — how to find hidden background-agent calls with OTel. Short, with a measurement method.
- `SxLUx8-hN1o` — how to tell a model change from a config change. The best method in the set.
- `D4uBfIe7SzA` — CLAUDE.md rules. Read it before editing ours. The size claim is disputed.
- `i6Q7bXnWGlM` — hidden settings with exact names. Includes a sponsor segment near 8:34.
- `v4F1gFy-hqg` — grill-me interview and shared glossary (talk, not a creator).

## Implications for our projects

**AgentOS**
- Crucible: a command-text firewall is not a sandbox (`Afm-GNrJbEQ`). Keep policy checks and execution isolation as separate layers.
- SkillForge: the open question is the success signal. Use per-skill usage counts, last-used dates and token cost (`i6Q7bXnWGlM`). Route lessons from a learning log through review before promotion (`jyLKRN36-Dc`).
- InferCraft: agent turns are prefill-bound. A changing token near the top of the prompt breaks the prefix cache (`x_qmqqp6d7s`, `TgmC_VZEKTE`). Add prefill time and cache-hit counts to the benchmarks.
- Observability: tag every model call by query source so cost can be attributed by purpose (`F4h3a8HFBSE`).
- Routing: tiered routing is like the strategy routing in Govrix (`vxrZWbZ2fZA`, `M48WuCSjmHs`). Test each route on a real repo bug, not a demo.

- Fold long tool output and keep the full output in an archive (`Afm-GNrJbEQ`). Check whether our trace path does the same.

**ProsHarness**
- Our plan, critique and debate loop is close to the spec-as-goal pattern with a reviewer per branch (`PLyRe6Zk--8`). Make the verification file read-only to the builder, as in `qLfSDQ5NGh0`.
- Our phone approvals map to the plan-ID gate in `HTscIrJhjDs`. Treat any confirm flag an agent passes as a speed bump, not consent.
- Budget loops and background agents by wall-clock time, not by work done (`F4h3a8HFBSE`).
- Treat hooks in `.claude/settings.json` from cloned repos as code. This matters for our zero-token credential handling (`lNsSxWQDqaU`).
- Save state to disk for checkpoint and resume, not to the context window (`4kYl2_mqmnQ`, talk; `_DZ4kJwQ50s`).
