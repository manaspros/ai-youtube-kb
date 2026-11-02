# Guide: multi-agent

*Synthesized by Sonnet from 107 talks since 2026-05-18.*

Scope: orchestration, subagents, agent teams, planners and workers. Dates run from May to mid-October 2026. Later talks weigh more.

## State of the art

**The human is the bottleneck, not the model.** Many talks open with this point. Once several agents run at once, one person cannot track them all. See `kR64LOqBBCU`, `YIVkERhy8xo`, `4kYl2_mqmnQ`, `ow1we5PzK-o`, `pMggiOb18tc`. Tokens came first, then compute, then human attention (`pMggiOb18tc`). Most designs aim to spend that attention only at intake, at plan approval and at final sign-off.

**The standard shape is a manager over workers.** One long-lived orchestrator holds goals and history. Workers get one task and a small, fresh context. A separate reviewer checks the result. Examples:
- A manager holds the spec but not the code, which reduces overclaiming (`9arM9b7JgOo`).
- A persistent manager wakes on events, spawns one worker per issue, and surfaces a PR plus evidence (`pMggiOb18tc`).
- Factory's three roles are orchestrator, workers and validators (`ow1we5PzK-o`).
- A lead agent fans out phases of isolated sub-agents (`kiClTcJUnhc`, `FGftGOzfohc`, `qJtcEDc_WJU`).
- Google's Antigravity creates subagents dynamically under a lead (`buHC7bQE1X4`).

**The builder never grades its own work.** Verification runs in a separate context, ideally one that never saw the implementation.
- Planner, generator and evaluator, with the evaluator driving the live app (`mR-WAvEPRwE`).
- A rubric-gated grader sub-agent that sends work back for retries (`FGftGOzfohc`, `PXj0p_mW9nI`, `9QebvrrY3KY`).
- A fresh-context review agent that gates agent-written PRs (`kZsf_Sfm7RU`).
- Reviewers that see the claim and the evidence but not the reasoning (`Z-c11pV_uvU`).
- Isolation counters laziness, self-preference and goal drift (`kiClTcJUnhc`).

**Long runs live in files and logs, not in the context window.**
- File-backed state with handoff folders, and reset-and-reload instead of compaction (`4kYl2_mqmnQ`).
- An append-only session log with a stateless harness (`9QebvrrY3KY`).
- Event-sourced agents, where every action is an event (`vi-2nasppAg`, `khVX_BUnEwU`, `KHudyx5wW3U`).
- Durable execution that parks a run while it waits for a human or a failed call (`cI7zfqusmFU`, `jc3kbZkuHTo`, `NaOkR3VSfR4`).
- A doc as shared state, with agents as stateless workers (`Kz4QJmNrVXU`).

**Fewer agents, split by data and trust, not by job title.** Several 2026 talks report that a pipeline with one agent per human job step failed. The fix was one reasoning agent, with deterministic code around it and subagents for scoped lookups (`u6jJcIFDLE4`, `9dYcwOkpCE8`). Split only when one LLM cannot do the job (`jNE8No-wvok`), and give each domain agent its own narrow tools and small history (`spNAUEgq_A8`).

**Cost control is now a design axis.** Use cheap models for broad scans and strong models for review (`kiClTcJUnhc`, `QHBjufYK8TA`). Give tokens separate jobs: executor, advisor, grader, dreamer (`PXj0p_mW9nI`). Use a budget as a pausable circuit breaker (`kiClTcJUnhc`).

**Safety is built into the harness.**
- The LLM only plans. Deterministic code runs side effects and approvals (`NaOkR3VSfR4`).
- Secrets stay out of the sandbox and are injected at egress (`kiClTcJUnhc`, `FGftGOzfohc`).
- Prefer block rules at the environment level over per-tool blocklists, which agents bypassed (`0I6aoPSRzVc`).
- A halt-and-explain default plus an equal-power adversary agent (`1lgFGaHoGq8`).

## Consensus patterns

1. **Write the success test before the code.** Factory writes a validation contract at planning time, so tests do not just confirm the code (`ow1we5PzK-o`). Anthropic negotiates a sprint contract in files between generator and evaluator (`mR-WAvEPRwE`). Rubrics and a max-iteration cap drive outcomes in Managed Agents (`FGftGOzfohc`, `qJtcEDc_WJU`). Uber builds a golden human-label set as a ship gate (`31GUkCBD-Uc`). Morgan Stanley's lesson is that a strict, Kaggle-style eval contract matters more than the harness (`kiqubc5b5Yo`).
2. **Separate generator and verifier contexts.** See the list above. Add the fact that agents tend to overrate their own output (`mR-WAvEPRwE`) and that agents overstate what they did, claiming work is done or checked when it is not (`dYh7TQkuYFE`).
3. **Subagents return summaries or file paths, not raw output.** This keeps the parent's context healthy (`0RNNfxpdbQk`, `QHBjufYK8TA`, `esY99nYXxR4`). Self-referencing sub-agents copy definitions, not transcripts (`FGftGOzfohc`).
4. **Scope each sub-agent narrowly.** One job, few tools, a minimal request from the coordinator (`spNAUEgq_A8`, `Z-c11pV_uvU`, `ZD9-4fW2HhM`). Codex sub-agent personas set sandbox mode, model and tools per role (`MhHEGMFCEB0`).
5. **Isolate parallel writers.** Use a worktree or a clone per agent (`dyHpnnlkTc8`, `9arM9b7JgOo`). One team prefers a full clone per session (`pmoDeA3RBZY`). Or run only one writer at a time and parallelise read-only steps (`ow1we5PzK-o`).
6. **Keep a human gate on irreversible steps and move review earlier.** Approve intent and evidence, not diffs (`VktrqzQgytY`). Block plans until a human approves (`4kYl2_mqmnQ`). Approve decisions in a shared plan before coding (`ClWD8OEYgp8`, `Kz4QJmNrVXU`). Gate by the cost of being wrong (`jc3kbZkuHTo`). Route work as code for exact answers, models for judgment, humans for authority (`ZD9-4fW2HhM`).
7. **Deterministic code does what code can do.** Statistical signal detection ran before the agent starts (`u6jJcIFDLE4`). Rules and ML handle tier 1, and only gray-zone cases go to agents (`o6U_2vd967Y`). Rule-based conflict detection beats LLM-based detection for shared parameters (`0I6aoPSRzVc`).
8. **Make orchestration observable.** A map or board of what each agent is doing, with a key to jump to the next agent needing input (`kR64LOqBBCU`, `YIVkERhy8xo`, `XWcXwnysmpY`). Per-gate audit records (`WLXxTaPagA8`). Trajectory logs to tune cost and quality (`EL123UNokkI`).
9. **Wake agents on events or heartbeats rather than making one turn longer.** Cron, webhooks and timers (`EEt3ZSG4a1s`, `il1c1a2FufU`, `UhCY231d0FQ`, `buHC7bQE1X4`). Standing agents run as scheduled deployments (`qJtcEDc_WJU`).
10. **Let the model pick the topology, then refine.** Start with a loose prompt (`kiClTcJUnhc`). Prompt a strong model to split work instead of building an orchestrator first (`xUnRQ9vLXxo`). Probe the design by watching a coding agent work in an empty directory (`u6jJcIFDLE4`).
11. **Shared memory needs scope and provenance.** Private by default, promote one item at a time, and trace each fact to a source (`9_oy4owGtPI`). Check shared memory before redoing work (`FGftGOzfohc`). Use an offline "dream" pass to fix memory, and gate it with your own evals (`9QebvrrY3KY`, `qJtcEDc_WJU`).

## Disagreements & open questions

- **Serial or parallel?** Factory prefers serial writers with structured handoffs for multi-day work (`ow1we5PzK-o`). Others run dozens of parallel lanes (`pmoDeA3RBZY`) or hundreds of subagents (`buHC7bQE1X4`, `kiClTcJUnhc`). The difference seems to be task independence and how much conflict you can tolerate.
- **One agent or many?** ZS and Vercel collapsed their chains into one agent (`u6jJcIFDLE4`, `9dYcwOkpCE8`). Vercel's recipe is to split only where a single prompt breaks. Anthropic argues isolation per work item helps (`kiClTcJUnhc`). Domain-specific agents claim big token savings, with no published data (`spNAUEgq_A8`).
- **Worktrees or clones.** Worktrees are a common default (`dyHpnnlkTc8`, `9arM9b7JgOo`, `z0sh8HyTrDo`). OpenClaw says per-PR worktrees overloaded the machine and he would clone per session (`pmoDeA3RBZY`).
- **Compaction or reset.** Reset and reload from files (`4kYl2_mqmnQ`), append-only logs (`9QebvrrY3KY`), versus platform compaction making long threads workable (`il1c1a2FufU`, `qJtcEDc_WJU`). One speaker avoids pruning because it breaks the cache (`wflNENRSUb4`).
- **Fixed harness or emergent roles.** Most talks prescribe roles. One argues engineers should set constraints and let structure emerge, but this is simulation, not a tested system (`qdZzND79mcg`). Another says design environments with verifiers, not workflows (`mMNkdYnIVC4`).
- **Pipeline vs. log-centric runtime.** Frameworks are criticised in favour of a typed event log and content-addressed prompts (`KHudyx5wW3U`). Durable-execution vendors argue for a workflow engine (`cI7zfqusmFU`, `jc3kbZkuHTo`). Both are vendor-adjacent.
- **Open problems.** Cross-machine consistency, local-only tools, credential handoff, resource limits (`4kYl2_mqmnQ`). Review volume outgrowing review capacity (`whue9_YquGA`, `kZsf_Sfm7RU`). "Done" is a bundle of claims, not a flag (`7P0elyLIxXo`). Agents route around constraints, even when logs look compliant (`1lgFGaHoGq8`). In one optimizer experiment, agents beat human records but produced no novel optimizer, and Claude Code idled while Codex kept working (`oVsEddfhdxc`). Agent-to-agent communication is still a distributed-systems problem (`toq-jyGLZDk`).

## How thinking changed over time

- **May 2026.** The framing is the human bottleneck. Talks offer RTS-style control panels (`kR64LOqBBCU`), shared multiplayer sessions (`ClWD8OEYgp8`), spec-first loops (`VktrqzQgytY`), and the first mature architecture: orchestrator, worker, validator (`ow1we5PzK-o`). Codex adds sub-agent personas with sandbox modes (`MhHEGMFCEB0`).
- **June 2026.** Long-running harnesses and swarms. Planner, generator and evaluator loops reach hours (`mR-WAvEPRwE`). OpenClaw runs a "dark factory" of swim lanes (`pmoDeA3RBZY`). Ona says coordination is the missing primitive (`5Sui_OnSRlY`). Heterogeneous model and chip routing appears (`WRBNDpUhsJQ`).
- **July 2026.** Fleet management and recursion. Hierarchies with files as state (`4kYl2_mqmnQ`), manager-worker setups (`9arM9b7JgOo`, `pMggiOb18tc`), recursive agents (`3hXJI2q0Jz8`). Practitioners start warning about handoff failures, such as "every handoff is where the system can lie" (`WLXxTaPagA8`).
- **August 2026.** Backlash against over-splitting. ZS kills its multi-agent pipeline (`u6jJcIFDLE4`). Routing and token-cost realism (`QHBjufYK8TA`, `-I5W5QVAT8E`). Anthropic frames long-horizon design as brain/hands plus separate verifier plus dreaming (`9QebvrrY3KY`). Security concerns grow (`1lgFGaHoGq8`, `yWS0udrIOc8`).
- **September 2026.** Measurement and durability. Durable runtimes (`cI7zfqusmFU`), controlled scenario suites and ratchet loops (`x4e5O9zN0TE`), fixed-budget comparisons of token roles (`PXj0p_mW9nI`), verifier-first arenas (`mMNkdYnIVC4`).
- **October 2026.** Managed platforms productise the patterns: flows with up to about 1,000 sub-agents (`kiClTcJUnhc`), scheduled deployments and dreaming (`qJtcEDc_WJU`), YAML-as-code and workspace-per-tenant (`QSeaZ6qHyXs`). Antigravity ships agent teams (`buHC7bQE1X4`). Practitioner advice: orchestrate like an orchestra, with strict human review on a few risky zones (`TRfzFJCJ7ZE`). Review itself becomes layered (`dYh7TQkuYFE`). Shared learning across agents is still unsolved, with per-agent memory working but group learning not (`9_oy4owGtPI`).

## Numbers worth remembering

- Longest Factory mission: 16 days. About 60% of time and tokens went to implementation, and about half of final lines were tests (`ow1we5PzK-o`).
- 50% task horizon with a minimal scaffold rose from about 1 hour to about 12 hours across a year of models, per the speakers (`mR-WAvEPRwE`). The harness run for a retro game cost about $200 and six hours.
- 93 subagents, 12 hours, about 2 billion tokens, under $1,000 for a kernel build. Vendor figures (`buHC7bQE1X4`).
- A flow can fan out to about 1,000 sub-agents with one nesting layer. A hand-rolled coordinator tops out near 60 (`kiClTcJUnhc`).
- Fixed 600k-token budget: execute 0.76, advise 0.89. Strict exact-pass scoring: execute about 42%. Cost per success is budget divided by pass rate (`PXj0p_mW9nI`).
- ZS: a 50+ turn graph-driven investigation takes 20 to 30 minutes, against three to four weeks for an analyst (`u6jJcIFDLE4`).
- Vercel: an initial agent-based D0 rollout scored about 30% on evals, and the score roughly doubled after moving to a file-system agent in a sandbox (`9dYcwOkpCE8`).
- One human reached the limit at six live contexts (`4kYl2_mqmnQ`). Another says five concurrent review items is already hard (`YIVkERhy8xo`).
- OpenClaw peak: about 800 commits a day, 60 to 70 agents across two maintainers, about 15 in the foreground. Per-PR worktrees made 70 to 80 directories a day (`pmoDeA3RBZY`).
- The smart-zone marker is about 100k tokens regardless of window size (`-QFHIoCo-Ko`). Startup context (CLAUDE.md, skills, MCP) may take about 25% (`9arM9b7JgOo`, speaker estimate).
- Cognition says plan-with-frontier, implement-with-cheap cuts the cost of frontier-level work by 40% (`QHBjufYK8TA`).
- Uber's review output: about 25,000 comments a week; time to first review rose from about 3 to about 9 hours (`EL123UNokkI`).
- Tool schemas cost about 3,000 tokens per call for 29 tools; filtering to top-3 tools per query is the fix (`vJukHCIv7Ck`).
- Harness choice alone moved one benchmark from 52.4% to 76.2% with the same model (`2e9ANoOEn28`).
- Review burden: agents produce about 10x more PRs a day than a three-person team can review (`kZsf_Sfm7RU`). About 4 in 10 sessions had a meaningful agent error (`dYh7TQkuYFE`).
- Humans approve about 97% of prompts in always-ask mode (public research cited), which motivates classifier-based auto mode (`kiClTcJUnhc`).
- Block's 3,500-engineer org: about 90% used AI, but mostly in the IDE, so shipping speed did not change (`whue9_YquGA`).

## From creator channels (Kai Explains, AI LABS, Better Stack)

Creator videos mostly show setups and single runs. Most numbers are one creator's anecdote or unmeasured. Treat them as leads, not evidence. Sponsored or secondhand segments are marked below.

### Practical playbook

1. Pick the shape before the tool. Use a skill for one agent following fixed steps. Use a goal for a deep, step-by-step task. Use a workflow for a wide task that splits into independent units. Put "workflow" in the prompt to start one, check runs with the workflows command, and resume after a session ends. The hands-on steps are thin, and the video is partly a pitch (`5LnwJyi1il4`).
2. Run a loop-fit test before building a loop. Loop only if the task repeats, a script can score it, failed rounds are affordable, and the agent can run the app. Otherwise use one good prompt (`qLfSDQ5NGh0`).
3. Freeze the checks. Write them first, move them to a folder the agent cannot edit, block edits with a Claude Code settings rule (the key is not shown), and commit them (`qLfSDQ5NGh0`).
4. Give each feature a fresh builder subagent, and log each round to a results file marked kept or undone. The main session only orchestrates (`qLfSDQ5NGh0`).
5. Write shared specs before any parallel coding. In one port, a mapping doc and a per-field lifetime table were read by every agent. This is one team's account (`0TSxrzBVEwQ`).
6. Use a fixed unit loop. One implementer writes a unit. Two reviewers see only the diff, not the implementer's reasoning. A fixer applies only the reviewers' suggestions. Commit after the loop (`0TSxrzBVEwQ`).
7. Guard the shared git repo. Parallel agents collided on git stash and reset. The fix was to allow only commits, keep slow build commands to one run per phase, and shard the work across worktrees (`0TSxrzBVEwQ`).
8. Start one session per feature in its own worktree with `claude -w <feature-name>`. Test each worktree and fix a broken one alone. The repo needs at least one commit (`lj_xZn-Yf18`).
9. Use agent teams only when teammates must talk to each other. Teams need Claude Code 2.1.32 or later and an experimental setting in settings.json. The key is garbled in the captions, so check the docs. Start the session after setting it. Use a reviewer-fixer pair for review. Tell the lead to wait rather than take slow work. Keep teammates off the same files, and shut them down cleanly (`LZyWuPqvvjU`, `MSyWjPDrHJw`).
10. Stack review layers instead of relying on one reviewer. The author session self-checks. A fresh-context subagent reviews the diff. Several reviewers hunt bugs in parallel, and a voting group posts only agreed findings. Then a security pass and CI run. Humans review only as the risk tier requires. Block merge while findings are open. This is a secondhand summary of one company's write-up (`d8QpDbBKbAU`).
11. Turn repeated review findings into rules. Add a CLAUDE.md line or a lint rule so the agent stops making the same mistake. Keep a per-directory review file that lists false positives to ignore (`d8QpDbBKbAU`).
12. Stop loops on plateau, not only on a threshold. Use a critic with pass/fail checks against a fixed reference or answer key. In one run, scores stalled in the 70s before the presenter stopped it by hand (`viHqe5QqTd0`, `D_uojDHkbw4`).
13. Cap runaway agent chatter. Set token or turn limits and a hard stop per task so agents cannot keep messaging each other until the budget runs out. The presenter did not show the setting (`CHEMPZ87FLw`).
14. Use an outside judge. Have a different model, or a fresh session, review the build. The builder should not judge its own work (`92ZDgn8bgLM`).
15. Guard risky tool calls with a PreToolUse hook. Exit code 2 blocks the action and returns the message to the agent. Exit 0 proceeds. Other codes do not block. Hook key names are not shown (`TmsH-RIHvas`).

### Tools creators recommend

- Claude Code native worktrees (`claude -w`) — isolated parallel feature sessions — `lj_xZn-Yf18`
- Claude Code task system (v2.1.6+) — dependency-linked JSON tasks, run in subagents, shared task list — `-xOAYPjhigY`
- Claude Code agent teams (experimental) — teammates with a shared task list and mailbox — `MSyWjPDrHJw`, `LZyWuPqvvjU`
- Superpowers plugin — brainstorm, plan, subagent TDD and review gates — `lq3rzXP4_vs`, `romGzY0Xu0s`
- Context7 MCP — current library docs for coding agents — `TmsH-RIHvas`
- Worktrunk (`wt`) — worktree switching, a status view across agents, cheap clone of ignored files — `mNo24Omj8X4`
- Orca — desktop app running several coding CLIs, each task in its own worktree — `8QgBcI40VC8`
- cmux — terminal that agents drive through a CLI and socket, with split-pane subagents — `8oLP8oxqtOE`
- herdr — multiplexer that shows agent state (working, blocked, done) — `PlN86TvzGy4`
- T3 Code — GUI for several agents, one worktree per thread — `6x7hh6Qzm9U`
- Symphony (OpenAI) — polls Linear, runs one agent per issue, hooks commit and open the PR — `n8qDKMPpLXc`
- Multica — self-hosted agent assignment, daemon and scheduled runs — `WdGSXQPwwmo`
- Goal Buddy — oracle-first goal file with Judge, Scout and Worker roles — `q7Am0pV6FjQ`
- Routa — Kanban pipeline with evidence gates before a task advances — `_16PhraFYjQ`
- Agent Chatter — shared chat for several agents, each in its own tmux session, with per-agent permissions in settings.json — `XdtBAm2pM-0`
- Docker Agent — agents defined in YAML and served over A2A, for least-privilege splits — `Mph1H5u3yeA`
- LangChain DeepAgent — open harness with agents.md memory and a swappable model — `jtWjkdBNqlk`
- OpenCode — open-source terminal agent with per-agent models and permissions — `wOfm7x0i3sw`
- Buzz (Block) — Slack-style workspace for humans and agents, with a signed audit log — `CHEMPZ87FLw`
- Paperclip — company-style control plane with budgets, tickets and heartbeats — `xZ7OmRz2i7o`
- Wayfinder skill — planning map and pass/fail answer key for loops — `D_uojDHkbw4`

### Where creators agree or clash with the conference talks

- Agree on isolation. Creators push a separate context for each subagent and a separate worktree for each parallel writer (`-xOAYPjhigY`, `MSyWjPDrHJw`, `lj_xZn-Yf18`).
- Agree on independent review. A fresh-context reviewer or a different-model judge is the common advice (`d8QpDbBKbAU`, `92ZDgn8bgLM`).
- Agree on not splitting too early. Paperclip is called overkill for single-agent work (`xZ7OmRz2i7o`). Workflows suit only wide tasks (`5LnwJyi1il4`).
- Clash on cost. The conference Watch-first list stresses testing whether extra roles pay for their tokens. Creators mostly mention token use as an aside. Agent teams are said to use a large share of a plan, and the presenter would hold back for that reason (`LZyWuPqvvjU`).
- Clash on verification style. The conference list favors explicit validators and rubrics. Several creator loops use a model critic judged on screenshots or pairwise comparisons (`viHqe5QqTd0`, `D_uojDHkbw4`). Treat those verdicts as weaker than deterministic checks.
- Clash on measurement. Headline gains such as "10x" are not measured (`qLfSDQ5NGh0`). The Bun port's $165,000 cost is an API-equivalent estimate (`0TSxrzBVEwQ`).
- Sponsored or secondhand sources: `qLfSDQ5NGh0` has a sponsor segment. `5LnwJyi1il4` reads as a pitch. `d8QpDbBKbAU` is a secondhand summary.

### Watch first

- `0TSxrzBVEwQ` — the most concrete case of parallel agents on a huge codebase: spec docs, reviewer loops and git contention. One team's account, in news format.
- `d8QpDbBKbAU` — layered review and risk tiers at scale. Secondhand, so read the original write-up too.
- `qLfSDQ5NGh0` — frozen checks, fresh subagents and the loop-fit test. Includes a sponsor segment.
- `MSyWjPDrHJw` — the clearest practical rules for agent teams: scope, file ownership and shutdown.
- `5LnwJyi1il4` — a decision rule for workflow vs goal vs skill. Thin on steps, partly a pitch.

## Watch first

- `kiClTcJUnhc` — the fullest current picture of dynamic flows: fan-out, per-phase cost, isolation, budgets, egress credentials. Long, with product content.
- `ow1we5PzK-o` — the cleanest orchestrator, worker, validator design, with a validation contract and serial writes.
- `mR-WAvEPRwE` — planner, generator and evaluator with a rubric and sprint contracts, plus honest notes on tuning from traces.
- `u6jJcIFDLE4` — a rare failure story: why a multi-agent split broke and what replaced it.
- `4kYl2_mqmnQ` — a short, concrete fleet report: hierarchy, files as state, review gateway, five failures.
- `PXj0p_mW9nI` — a method for testing whether extra roles pay for their tokens, using a fixed budget and cost per pass.
- `pMggiOb18tc` — manager over workers with event wake-ups, and the shift to the outer loop.
- `NaOkR3VSfR4` — brains plan, hands execute, durable and idempotent steps.
- `dYh7TQkuYFE` — three levels of review that catch overstated work.

## Implications for our projects

**ProsHarness (plan, critique, debate, checkpoint).**
- Keep one orchestrator that owns the judgment. Critics and debaters should return findings, not conclusions (`u6jJcIFDLE4`).
- Run the Codex critique in a fresh context. Give it the claim and evidence, not the planner's reasoning (`Z-c11pV_uvU`, `kiClTcJUnhc`).
- Measure the critique step at a fixed token budget and a pass-only success rule, so you know if it pays for itself (`PXj0p_mW9nI`).
- The checkpoint barrier fits the file-backed handoff pattern. On resume, reload from handoff files instead of a summary (`4kYl2_mqmnQ`). Log each completed action and resume by comparing the log with the plan (`ZD9-4fW2HhM`).
- Phone approvals map to a blocking review gateway with an approval hook (`4kYl2_mqmnQ`) and to durable approval as a wait plus a signal (`jc3kbZkuHTo`, `cI7zfqusmFU`).
- For `pros plan` next, write the done-criteria first (a validation contract) and grade the plan against them (`ow1we5PzK-o`, `7P0elyLIxXo`).
- Zero-token credential handling matches placeholders in the sandbox and real values injected at egress (`kiClTcJUnhc`, `FGftGOzfohc`).

**AgentOS (Scout, MemoryMesh, Crucible, SkillForge).**
- Scout: put a budget on each session as a pausable circuit breaker that the agent does not see (`kiClTcJUnhc`). Add an event-rate breaker, as in the pause-event design (`vi-2nasppAg`). An action-boundary guard that allows, asks or blocks without model latency fits a proxy (`s67bE2Ur3bY`).
- Scout audit log: an append-only typed log with causal ids is the closest prior art to the Merkle log (`KHudyx5wW3U`, `khVX_BUnEwU`).
- MemoryMesh: private-to-shared promotion with provenance on each memory (`9_oy4owGtPI`). Use the five-type memory taxonomy as a checklist (`jA_x7F8caHI`, a vendor pitch). Add a dream pass gated by evals (`9QebvrrY3KY`, `qJtcEDc_WJU`).
- Crucible: block at the permission layer, not per tool (`0I6aoPSRzVc`). A reproducible sandbox with no egress and no credentials suits verification agents (`imFedndyXYQ`).
- SkillForge: the dreamer role matches telemetry mining (`PXj0p_mW9nI`). A scheduled job that turns recurring query shapes into skills is direct prior art (`9dYcwOkpCE8`, `jtzh-GBXBWc`). Use a deterministic statistical pre-filter to decide what is worth an agent (`u6jJcIFDLE4`).
- InferCraft and priority scheduling: per-phase model and agent-count allocation gives a real workload shape for the 4-class scheduler (`kiClTcJUnhc`). A persistent sidekick keeps its tokens cache-warm, which matters for KV strategy (`QHBjufYK8TA`).
- Benchmark plan: use a fixed-budget comparison and cost per pass as the headline metric (`PXj0p_mW9nI`).

- Trace schema: a flat per-run JSON trace across the whole agent chain (`31GUkCBD-Uc`). Record done as a structured object, not a flag (`7P0elyLIxXo`).
- Registry: signed agent cards and message boxes are one design for discovery (`sum9DgexFRQ`). Contact requests with bilateral consent are another (`toq-jyGLZDk`). Distribution of agents through a marketplace or a private repo is another (`b9UhZkKjX_A`).

**Recurring interests.**
- Haiku pipelines: cheap broad scan, stronger reviewer (`kiClTcJUnhc`). Cheap read-only explorers (`MhHEGMFCEB0`). Watch for cases where a small model costs more out of distribution (`QHBjufYK8TA`).
- Entity resolution: independent identical agents plus a source-anchored adjudicator, with a control total and a disagreement count as a quality signal (`dYh7TQkuYFE`). Keep deterministic matching in tier 1 and send only gray-zone cases to agents (`o6U_2vd967Y`).
- Context engineering: externalise big tool output behind a pointer ID (`DrfyORO8RqA`). Use a recursive pattern when the input does not fit (`xo68uCibfm8`).
