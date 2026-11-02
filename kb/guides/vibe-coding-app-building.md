# Guide: vibe-coding-app-building

*Synthesized 2026-11-02 by Haiku from 137 videos. Open a video: `kb/videos/<id>.md`.*

Scope: 137 videos, mostly creator tutorials from AI LABS and Better Stack (2025-11 to 2026-10). A few AI Engineer conference talks are marked "(conf)". No Kai Explains video appears in these notes. Most creator claims come from one run by one host. Sponsor segments are noted where they matter.

## State of the art (what practitioners actually do now — most recent talks weigh most)

- The working loop now starts from a written spec, not a single prompt. Creators write a PRD, a plan, or a brand file before any build. See `QgA55EnmUp4`, `bBlY5YOsKN8`, `DP7mgLUKN_U`.
- Context is split into an always-loaded file and on-demand files. Project facts go in CLAUDE.md. Visual tokens go in design.md. Long docs load only when a task needs them. See `5lycYTOYbPM`, `DP7mgLUKN_U`, `QgA55EnmUp4`.
- Design quality is steered by skills, rule files and anti-pattern lists, not by the model alone. Creators name the generic defaults to ban: fonts, palettes, centered CTAs. See `5lycYTOYbPM`, `HqD5a2Cae60`, `pHstb0JGGhE`.
- Design runs in stages: layout first, then theme, then polish. Each stage gets variants, and one is picked before the next. See `McJluKfjVGk`, `bBlY5YOsKN8`.
- Design rules are enforced by tools, not only by prose. A shadcn linter turns rules into lint errors (`tPQgw_DPIoM`). Visual diff tests run before code (`5lycYTOYbPM`).
- Agents fetch live library docs before writing UI. shadcn MCP (`V8rGgwQ-VJ0`, `McJluKfjVGk`). Figma MCP reads a design from a link (`FJBLhd23f80`, `zmP8Pl-MJXw`).
- Shipping is git-first. Commit before a risky change, push, and let the host redeploy (`DP7mgLUKN_U`). Backend handoff uses a managed database through MCP with a pre-made schema (`bBlY5YOsKN8`).
- Conference view (conf): designers and builders steer agents with explicit meanings for vague words, not with adjectives alone (`v42opQpCy60`). Teams that ship with AI need an enablement step first (`UcYoMg-8-L8`, conf).

## Consensus patterns (numbered; each cites videos as `video_id`)

1. Write a spec file before generating anything: a PRD, an implementation plan, or design.md. Cited by `QgA55EnmUp4`, `5lycYTOYbPM`, `DP7mgLUKN_U`, `bBlY5YOsKN8`.
2. Keep always-loaded instructions short. Move detail to files that load on demand. Cited by `5lycYTOYbPM`, `QgA55EnmUp4`.
3. Put business goal and product context in CLAUDE.md, not only in the chat. Cited by `DP7mgLUKN_U` (business goal), `HqD5a2Cae60` (verify contract), `pHstb0JGGhE` (AGENTS.md via `/init`).
4. Name the anti-patterns and banned defaults. Creators list banned fonts, off-white palettes and gradient-heavy styles to avoid. Cited by `5lycYTOYbPM` (fonts, anti-patterns), `DP7mgLUKN_U` (off-white palettes), and `7GMKdpLsxwU` (conf; a list of 20-30 recognizable AI tells to ban).
5. Use a structured prompt before the first build. A single-page design prompt covers intent, colors, contrast, layout, sections and anti-patterns (`5lycYTOYbPM`). A spec prompt lists pages, roles, shared components, modals and the stack (`U1_nzjWUpL4`).
6. Iterate in stages with variants, not one-shot. Layout, then theme, then detail. Cited by `McJluKfjVGk`, `bBlY5YOsKN8`.
7. Use plan mode before any build. Cited by `DP7mgLUKN_U`, `VNx9Gy5pHZI`.
8. Commit checkpoints before risky changes, and deploy from the repo. Cited by `DP7mgLUKN_U`.
9. Verify with a second check, not the builder's self-check. Options: a browser loop (`pHstb0JGGhE`), a subagent checking against design.md (`HqD5a2Cae60`), or pixel diffs (`5lycYTOYbPM`).
10. Prefer a lint or check script over prose style rules. Error text should name the allowed values (`tPQgw_DPIoM`).
11. Fetch live docs for libraries rather than trusting memory. Cited by `V8rGgwQ-VJ0`, `McJluKfjVGk`.
12. Name the parallel path explicitly when you want it. Otherwise the model may skip it. Cited by `KvOYDevFGiw`. Parallel agents suit only independent work (`QgA55EnmUp4`).

## Disagreements & open questions

- Is design.md worth it for every UI? Most creators say yes (`5lycYTOYbPM`, `bBlY5YOsKN8`, `DP7mgLUKN_U`). `HqD5a2Cae60` says apply it only to marketing pages, after generation, because it hurts functional UI.
- Does a stronger model fix generic design? `HqD5a2Cae60` reports that about two in three sites still look alike with the newest guide. That figure is informal, with no sample size. `DP7mgLUKN_U` says Opus 5.5 is best for design, and `bBlY5YOsKN8` says Haiku is cheaper but needs more refinement.
- Are subagents needed? `HqD5a2Cae60` says a large context makes them unnecessary. `QgA55EnmUp4` keeps them for independent tasks only. Neither measures it.
- Token cost. `KZCKfhjMuOQ` says Opus 4.7 can use up to 35% more tokens for the same prompt. `0lBvjhcRqyU` says a lower per-token price can still mean a higher cost per task. Creators disagree on which number to watch. The per-task view is the stronger one.
- Speed versus quality. Very fast models produced broken apps in `HfRVXadseCo` and `AhVHtwh5k3E`. Creators judge by running the output, not by reading it.
- Sponsor segments: `5lycYTOYbPM` (Zilliz), `DP7mgLUKN_U` (CodeRabbit), `HqD5a2Cae60` (Kimi). Treat their product claims as marketing.
- Single-creator claims with no baseline: "Opus defaults to warm cream palettes" (`DP7mgLUKN_U`), "design comes from the harness, not the model" (`HqD5a2Cae60`).

## How thinking changed over time (dated)

- 2025-11: Context engineering as PRD plus rules plus a staged plan (`QgA55EnmUp4`). Figma and MCP cloning begins (`FJBLhd23f80`, `zmP8Pl-MJXw`).
- 2025-12: Screen-by-screen generation in Stitch, with a multi-phase rules file (`v9Rd_l6gLjU`).
- 2026-02: Design work moves to design tools driven through MCP, with Stitch as an MCP and a UI guide written first (`VNx9Gy5pHZI`). Reflex is tested and rejected for frontend work (`9QmH6DDyLCQ`).
- 2026-03: Parallel agents in git worktrees (`sC4JpJlD3aQ`).
- 2026-06: design.md plus a design-rules skill become standard (`5lycYTOYbPM`).
- 2026-07: Effort level becomes a tuning knob by task type. Skills get refreshed from each model's prompting guide (`HqD5a2Cae60`).
- 2026-08: Brand rules move into AGENTS.md and design.md, so every thread shares them (`pHstb0JGGhE`).
- 2026-09: Design systems are generated from design.md, with cost-aware iteration (`bBlY5YOsKN8`). Cost per task replaces price per token as the metric (`0lBvjhcRqyU`).
- 2026-10: Lint rules for design systems (`tPQgw_DPIoM`). Full six-stage site process (`DP7mgLUKN_U`).

Overall shift: from one-shot prompts (2025) to spec files, skills and lint rules (2026), with cost per task now a main concern.

## Numbers worth remembering

- Opus 4.7: up to 35% more tokens for the same prompt, at unchanged per-token price (`KZCKfhjMuOQ`).
- Fable 5.1: cache-read price cut from $1 to $0.25 per million tokens (API). Anthropic estimates 25% cheaper for typical work and up to about 45% for agentic work, API only, as the host reports (`0lBvjhcRqyU`).
- Fable 5.1 max scores 66 on the Artificial Analysis index, four points above Fable 5 (`0lBvjhcRqyU`).
- v0-1.0-md: 128,000-token context, 32,000-token output, beta limit 200 messages per day (`jZB1sXDaOj8`).
- Stitch: 350 designs per month in standard mode, 50 in experimental mode (`v9Rd_l6gLjU`).
- OJ (Lovable's Vite-compatible dev server): on a 5000-component app, about 1.7x faster to the deepest component and about a quarter of the memory (`msSZ4CL_sNg`). On a small app the memory gain is small (380 MB versus 320 MB across processes).
- shadcn MCP lists 46 components (`V8rGgwQ-VJ0`). A GitHub token raises its limit to 5,000 requests per hour.
- Claude Design: usage is capped by a 5-hour window shared with all Claude usage (`bBlY5YOsKN8`).
- Kimi agent swarm claimed at up to 100 sub-agents and 1,500 tool calls, with a 4.5x speedup (vendor claims, `KvOYDevFGiw`).
- CodeRabbit flagged 11 issues on one PR, split across 5 layers (sponsor segment, `DP7mgLUKN_U`).
- Automattic: about 500 people shipped about 794 projects in 30 days (conf, `UcYoMg-8-L8`).

## Watch first (5-8 best videos: `video_id` — why)

- `5lycYTOYbPM` — Three levels of design control: a structured prompt, design.md, and visual tests. Clearest method. No benchmarks. Has a Zilliz sponsor segment.
- `DP7mgLUKN_U` — The full six-stage Claude Code site build: plan mode, CLAUDE.md, design rules, deploy, PR review. Most reproducible tutorial. CodeRabbit section is sponsored.
- `QgA55EnmUp4` — PRD to docs folder to staged plan. The resume-from-file pattern is the most reusable for long agent runs.
- `bBlY5YOsKN8` — Claude Design workflow with a design.md-first step, wireframes, and an MCP handoff. Shows the token cost of iterating in the design tool.
- `HqD5a2Cae60` — Refreshing a design skill from each model's prompting guide, plus a verifier subagent. Mixed evidence. Has a Kimi sponsor segment.
- `tPQgw_DPIoM` — shadcn linter for Tailwind design systems. Deterministic checks with agent-readable errors. One informal eight-task test.
- `0lBvjhcRqyU` — Cost per task versus price per token, with a same-prompt bake-off. Useful for budgeting model choice.

## Implications for our projects

- ProsHarness (most relevant). The plan file as the durable resume point, with verify-before-advance, fits its checkpoint/resume goal (`QgA55EnmUp4`). A verifier subagent that checks against a reference file before a run counts as done (`HqD5a2Cae60`). Commit-as-checkpoint is a candidate default for ProsHarness (`DP7mgLUKN_U`). Plan mode before execution matches its plan step (`DP7mgLUKN_U`).
- AgentOS. Error messages that name the allowed options let an agent self-correct without loading policy docs (`tPQgw_DPIoM`). Check whether Crucible's exec-gate guardrails do this. A small always-loaded routing rule that points to on-demand docs is a pattern to compare with MemoryMesh's context assembly (`QgA55EnmUp4`).
- Cheap-model pipelines (Haiku). Track cost per task, not per token, when comparing models (`0lBvjhcRqyU`, `KZCKfhjMuOQ`). Use a strong model for the first build and a smaller one for iteration (`7GMKdpLsxwU`, conf). Haiku uses fewer tokens but may need more refinement (`bBlY5YOsKN8`).
