# Guide: dev-tools

*Synthesized 2026-11-02 by Haiku from 379 videos. Open a video: `kb/videos/<id>.md`.*

Evidence base: almost all of these notes are Better Stack tool reviews and demos. Kai Explains appears twice (`fOj8TgAdDGE`, `McB108-FExg`). AI LABS has no entries in the notes I read. Conference talks in this category are `AMiyLItEtLA`, `uKUA1a0Kdfc` and `xZX3pmaB8Hk`. Most tool numbers come from the vendor or the author, or from one demo.

## State of the art (what practitioners actually do now — most recent talks weigh most)

- Agent-written code is cheap, so the bottleneck is review and checking. Creators now build tools that check code in place of a human reading every line (`AMiyLItEtLA`, `mmrSYvYKD9g`, `cP5PRDo3u6Q`).
- Enforcement moves from prose to deterministic tools. Lint rules, schema-validated JSON and CLI invariant checks run in CI or in the agent's own loop (`mmrSYvYKD9g`, `tPQgw_DPIoM`, `iuJszJuiuSg`).
- Parallel agents run in one git worktree each, with one status screen over all of them (`mNo24Omj8X4`, `8QgBcI40VC8`, `TK1LvtX-Bqs`).
- Claude Code is being extended from inside. "Mods" are in-process TypeScript plugins that can draw panes and status lines and rewrite events (`EiThSVZ8pME`).
- Plans get approved before anything runs. A plan ID binds the approval to the exact plan (`HTscIrJhjDs`).
- Small local tools are the default for solo work. Examples are PocketBase, Hister, DBX and Floci (`WZoC1HA1vec`, `NMk9XVNTygA`, `b6rVCrBPbe8`, `7s462S-qRY4`).
- Postgres is pitched as the one-service backend for small apps (`MZfhhl6ej-k`, `_0A2BnRYVCo`).

## Consensus patterns (numbered; each cites videos as `video_id`)

1. Turn rules into deterministic checks. Prose rules in CLAUDE.md are easy for agents to skip. Lint or CI failures are not (`mmrSYvYKD9g`, `tPQgw_DPIoM`, `AMiyLItEtLA`).
2. Make lint errors explain the fix. The agent then repairs from the message, not from the full design doc (`mmrSYvYKD9g`, `tPQgw_DPIoM`).
3. Have the model emit a small typed artifact and compile it deterministically. Validate the artifact before anything is rendered (`iuJszJuiuSg`, `xFWhiWe91BE`).
4. Use one worktree per agent task. Add a status view for all worktrees and a one-step merge (`mNo24Omj8X4`, `8QgBcI40VC8`).
5. Split large changes into layered, dependent PRs. Put schema and shared types lowest and UI highest. Review and merge the stack from the top (`3Z1xcfF2xlY`).
6. Keep a human reading gate even when the code is unread. The Boundary talk requires one other person to read each design doc before it ships (`AMiyLItEtLA`).
7. Gate destructive, DNS and production actions behind separate explicit flags. Refuse paid or account-creating steps outright. The flags are a speed bump, not proof of consent (`HTscIrJhjDs`).
8. Give agents read-only, saved connections, not pasted credentials (`b6rVCrBPbe8`, `sZaMmVUmq-I`).
9. Use the right store for the access pattern. Row stores suit point lookups and small updates. Columnar stores suit wide aggregations (`mR06J55fLvo`).
10. Measure before trusting a benchmark. Re-run the README numbers on your own machine (`7s462S-qRY4`, `zf8jpD77sKY`, `uIqjWeO91p4`).
11. Delay new dependency versions and sign artifacts. Both come from security talks and news, not from tool reviews (`xZX3pmaB8Hk`, `sZaMmVUmq-I`).

## Disagreements & open questions

- Rust rewrites. Evan You warns that a Rust plugin inside a JS core can end up no faster, because data crossing the boundary costs time (`LSGZtHafiM4`). Other pieces say Rust is the new default for AI tooling, but mostly on company anecdotes (`R-tLX37Xgx8`). Polars 2.0's 5x speedup is still unbenchmarked (`uHELj20WrOc`).
- Dev-server speed. Lovable's OJ is faster at scale on a 5000-component app. Evan You says it only works because it supports one shape of app (`msSZ4CL_sNg`).
- Mojo. Kai's piece takes vendor numbers as a starting point and flags MoE gaps (`fOj8TgAdDGE`). The Better Stack test calls the headline benchmarks inflated and the APIs unstable (`uIqjWeO91p4`). The two sources disagree on tone more than on facts.
- Agent review. One view says the reader is the gate (`AMiyLItEtLA`). Another says the diagram itself needs checking, because a diagram is a claim (`cP5PRDo3u6Q`). Stacked PRs are offered as a fit for long agent runs, but the presenter did not test this (`3Z1xcfF2xlY`).
- Consent. Confirm flags supplied by the agent are weak controls (`HTscIrJhjDs`). Nobody in these notes shows a strong answer.
- Privacy defaults. Whiteboard telemetry is on by default (`cP5PRDo3u6Q`). Mods can rewrite prompts and call undocumented endpoints (`EiThSVZ8pME`).
- Open question: whether linting beats a good prompt across all teams. Only the lint tool makers and their demos are in the notes.

## How thinking changed over time (dated)

- 2026-03: JS tooling moves to a Rust core (Rolldown, OXC) on the Vite side. Pre-bundling and bundling thresholds get concrete numbers (`LSGZtHafiM4`).
- 2026-08: Wasm is framed as a server and edge runtime, with JavaScript kept for the DOM (`McB108-FExg`). Semantic chart specs replace hand-written chart code (`xFWhiWe91BE`).
- 2026-09: A wave of tool reviews. Stacked PRs, Postgres consolidation, Bun's built-in standard library, and lint gates for agent code (`3Z1xcfF2xlY`, `MZfhhl6ej-k`, `IcoB5AZ6TJ0`, `mmrSYvYKD9g`). The August conference talk "fighting slop with slop" argues the bottleneck is reading, not writing (`AMiyLItEtLA`).
- 2026-10: Tools built for agents. Worktree status views, desktop multi-agent apps, mods, plan-approve-apply deploys, design-system linters (`mNo24Omj8X4`, `8QgBcI40VC8`, `EiThSVZ8pME`, `HTscIrJhjDs`, `tPQgw_DPIoM`). Security news moves to exploit-before-patch (`sZaMmVUmq-I`, `xZX3pmaB8Hk`).
- 2026-11-01: Hardware-control and remote access tools appear, but these are not agent-focused (`jNFv1Lr2Db4`).

## Numbers worth remembering (with `video_id`)

- Evan You's rule of thumb in the talk: unbundled loading is fine near 1,000 modules, and bundling wins past about 3,000 (`LSGZtHafiM4`).
- Columnar vs row store on 100M rows, GROUP BY: Postgres 9.7 s, ClickHouse 0.28 s, DuckDB 0.24 s. Point lookup: Postgres 2 ms, ClickHouse 168 ms (`mR06J55fLvo`).
- Worktree copy-on-write, 14 GB build folder: about 20 s vs 2m14s with a normal copy. Author's figures, not verified (`mNo24Omj8X4`).
- Lint-gated agent fix of one API client took about 2 to 3 minutes (`mmrSYvYKD9g`).
- Status-line mod built in about 5 minutes (`EiThSVZ8pME`).
- Floci startup: about 129 ms measured vs 24 ms claimed. LocalStack about 7 s vs 3.3 s claimed (`7s462S-qRY4`).
- llmfit estimate for one small model: about 141 tokens/s, against about 0.3 measured earlier on the same Raspberry Pi. Off by about 800x (`zf8jpD77sKY`).
- Bundle sizes in one vendor benchmark: TanStack Charts 36 to 43 KB, Chart.js 45 to 58 KB, Recharts 153 to 168 KB (`odbQhwcIo4Q`). Vendor claim.
- Effect v4 minimum bundle about 7 KB vs 35.5 KB in v3. Vendor claim (`OsL9EJWz9UY`).
- Solid 2 test project compile time about 440 ms to 19 ms. Vendor claim (`sr4q-Jj7uiM`).
- DBX: 90+ engines, but the reviewer says most are untested (`b6rVCrBPbe8`).
- Rust memory-bug share in security reports is about 70% (`R-tLX37Xgx8`). Cited figure, from Microsoft and Chrome data as reported in the video.

## Watch first (5-8 best videos: `video_id` — why)

- `LSGZtHafiM4` — Evan You on why the Vite toolchain moved to Rust, and his guardrails for agent-written code. Long, practitioner depth, but much of it is the speaker's own roadmap.
- `mmrSYvYKD9g` — Short, concrete lint gate for agent code, with the generate-lint-repair loop. Single demo, no benchmark behind the speed claim.
- `AMiyLItEtLA` — Conference talk. Invariant files, CLI guard checks, and a reading gate for teams that skip code review.
- `3Z1xcfF2xlY` — The exact gh stack workflow for layered PRs, with a stack merge from the top.
- `EiThSVZ8pME` — How Claude Code mods work and how they differ from hooks. Read the privacy notes before installing.
- `mNo24Omj8X4` — One screen for parallel agents, and copy-on-write for ignored files. Numbers are the author's; verify them yourself.

## Implications for our projects

- ProsHarness: checkpoint and resume of long runs fits the layered PR idea (`3Z1xcfF2xlY`). A plan-approve-apply flow with a bound plan ID matches the approval step (`HTscIrJhjDs`). Mods could show run state in the status line (`EiThSVZ8pME`). Mods can also call undocumented endpoints, so keep them away from credential handling.
- ProsHarness and agent loops: one worktree per agent task, with a status view, is the pattern to copy (`mNo24Omj8X4`, `8QgBcI40VC8`).
- AgentOS registry: `ON CONFLICT DO SELECT` gives atomic get-or-create for skills and MCP servers. Postgres 19 is in beta and the claim comes from one news video (`_0A2BnRYVCo`). Check it against the release notes first.
- AgentOS L2B InferCraft: the llmfit method works as a pre-check for model fit on the RTX 5090. Decode speed is memory-bound, so divide bandwidth by weight size before trusting any tokens/s figure (`zf8jpD77sKY`).
- AgentOS skill mining (L2D): the validated-IR pattern from Archify and Flint suits skill records. Validate the artifact before it is stored (`iuJszJuiuSg`, `xFWhiWe91BE`).
- Any TypeScript code the agents write: a lint gate with messages written for agents is a cheap fix (`mmrSYvYKD9g`, `tPQgw_DPIoM`).
- Cheap-model pipelines: mods can call Haiku through the user's subscription. This is one creator's demo, not a documented API (`EiThSVZ8pME`).
