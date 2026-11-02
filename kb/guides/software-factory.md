# Guide: software-factory

*Synthesized by Sonnet from 65 talks since 2026-05-18.*

Scope: autonomous and background coding agents that ship code end to end. Spec-to-PR pipelines, agent fleets, "dark factories", and the loops and gates around them.

## State of the art (what practitioners actually do now)

**The factory is a loop, not a bigger agent.** The recent talks define a software factory as the whole signal-to-deploy cycle. Signals come in (issues, alerts, bug reports, traces). Agents triage, spec, implement, review and verify. Humans gate the risky or stuck points. Monitoring feeds back into triage (`tUPPVhBBcoM`, `vGCJ7diEtrw`, `exiwa9QbQXI`, `wpOA-UXynoM`). A sandbox plus a coding agent is explicitly not a factory (`HvboD89DyQ8`).

**Humans moved to the outer loop.** Agents run the inner loop: investigate, implement, test, report. Humans own the outer loop: what is worth doing, whether the evidence holds, and what reaches production (`n97BCfyFIvw`, `pMggiOb18tc`, `_ehJyfHg1Vk`). Human attention is named the scarce resource in many talks (`so9l_MwS2yg`, `YIVkERhy8xo`, `ow1we5PzK-o`, `pMggiOb18tc`).

**Verification decides how much autonomy you get.** Factory's view is that agent readiness equals the number of deterministic validation loops in the repo, not model strength (`wpOA-UXynoM`). They score repos on eight pillars before deploying agents (`exiwa9QbQXI`). Ralph-style loops work where a deterministic check can close them (`c35YoMdnI78`).

**Review is the new bottleneck, and the fix is layered.** The common stack is cheap deterministic checks, then an agent reviewer, then a human. The agent reviewer should commit fixes, not just comment (`LlgiOCmFG_w`). Speculative merge queues and tiered auto-approval address CI and merge capacity (`7b9tov5Uc5s`, `uuwDWRbxoYo`, `XqF-IFHBCkM`).

**Cloud sandboxes and VMs are the default place agents run.** Teams move agents off laptops into isolated environments (`rnDm57Py54A`, `5Sui_OnSRlY`, `OL7kfezynJM`, `TRfzFJCJ7ZE`, `L173Z8DpaJg`). Uber keeps a pool of pre-warmed pods with repos and indexes ready (`17-YSUHo6Lk`).

**Platform pieces are converging.** Uber's list is the clearest: one model gateway with PII and safety middleware, one MCP gateway, warm workspaces, a managed skills marketplace, and a context graph (`17-YSUHo6Lk`). Skills and AGENTS.md are the main way to hold institutional judgment (`6MudaeKdBSk`, `GdvKNwMcfd0`, `I2LL_wd89-A`).

**Cost control is moving to routing.** Teams pick the cheapest model that clears a quality bar per task (`vGCJ7diEtrw`, `48YUYDjwfYY`, `TN3mj92oZ8I`, `exiwa9QbQXI`).

**Triggers beyond chat.** Cron, webhooks, alerts and issue events start agents. Examples: nightly outreach agents (`FLUoowDJg4I`), weekly performance agents (`JJGbw4ggaFs`), trace-driven fix agents (`9HbzAWnKbo4`), and daily migration loops (`xIt_mTQp6mY`).

## Consensus patterns

1. **Spec and plan first, alignment with a human, then AFK implementation.** Agents interview the author, then a spec or design doc drives tickets (`VMemhtlsoNk`, `-QFHIoCo-Ko`, `W76woOYHlvY`, `Ib5GBkD555M`, `tUPPVhBBcoM`). Planning time is cheaper than review time (`W76woOYHlvY`).
2. **Fresh context per unit of work, with state on disk.** Re-run the agent with a clean session and read progress from files or git. Keep sessions near 100k tokens and clear instead of compacting (`-QFHIoCo-Ko`, `2TLXsxkz0zI`, `c35YoMdnI78`).
3. **Write the definition of done before the code.** Factory writes a validation contract at planning time and has fresh-context validators check against it (`ow1we5PzK-o`, `vGCJ7diEtrw`). Others use acceptance criteria and goal files (`FwiS44-xyYw`, `OL7kfezynJM`, `ojJXgXLUQFc`).
4. **Separate the writer from the checker.** The agent that wrote the code should not review it or write its tests (`ZpK5PWX2YRM`, `LlgiOCmFG_w`, `2TLXsxkz0zI`, `ow1we5PzK-o`).
5. **Make the agent prove its work with the running app.** Computer-use click-throughs, recordings and screenshot diffs (`rnDm57Py54A`, `6MudaeKdBSk`, `I2LL_wd89-A`, `HLTa7Vcs4X0`, `bdHaOXZOhcM`).
6. **Fix the system, not the PR.** When a reviewer catches a repeat mistake, turn it into a rule, skill, lint check or test (`rnDm57Py54A`, `ZpK5PWX2YRM`, `zCJtYuqwm7E`, `X6l4lpA0_NY`, `5Sui_OnSRlY`). Warp adds an observer agent that edits skills through a PR (`TN3mj92oZ8I`, `tUPPVhBBcoM`).
7. **Deterministic code around the LLM.** Plain code does orchestration, vetting, commits and pushes. The agent only reasons, and it does not hold write or CI credentials (`LqLoYksJ6do`, `iQ5xldZ9StU`, `c35YoMdnI78`, `xIt_mTQp6mY`).
8. **Risk-tier the human review.** Auth, money, migrations and irreversible changes get a human line-by-line read. Other changes get proof sized to the risk (`ZpK5PWX2YRM`, `TRfzFJCJ7ZE`, `7b9tov5Uc5s`, `2TLXsxkz0zI`).
9. **Climb a trust ladder.** Advisory review, then blocking, then autofix, then rule-based auto-approve, then auto-merge. Move up only once precision is shown (`XqF-IFHBCkM`, `uuwDWRbxoYo`).
10. **Isolate each agent.** Own VM or clone per agent. Worktrees share databases and caches, and they overloaded machines at scale (`rnDm57Py54A`, `pmoDeA3RBZY`, `5Sui_OnSRlY`).
11. **Measure outcomes, not output.** Customer happiness, defect rate, code survival, and cost per task, not PR counts or token use (`VMemhtlsoNk`, `HvboD89DyQ8`, `I2LL_wd89-A`, `RVxym6mmIns`, `XqF-IFHBCkM`).
12. **Build a readiness layer in the repo.** AGENTS.md, one canonical pattern per concept, fast CI, modular boundaries (`rnDm57Py54A`, `GdvKNwMcfd0`, `6qkzlT962es`, `exiwa9QbQXI`, `Ib5GBkD555M`).

## Disagreements & open questions

- **Review or no review.** Dex says lights-off factories stall after a few months, because training rewards passing tests and not design (`Ib5GBkD555M`). Boundary skips code review. They replaced reading with CLI invariant checks and a required read of design docs (`AMiyLItEtLA`). Alex Volkov sits in between and tiers review by risk (`ZpK5PWX2YRM`).
- **Parallel or serial.** Factory prefers serial writers with read-only parallelism for multi-day work (`ow1we5PzK-o`). Chris Parsons says give parallel agents no dependency graph and run one ticket at a time (`2TLXsxkz0zI`). Pocock and WorkOS use blocking graphs for parallel work (`-QFHIoCo-Ko`, `HvboD89DyQ8`). OpenClaw runs swim lanes (`pmoDeA3RBZY`).
- **Blind loops or control loops.** HumanLayer wants a sensor, controller and actuator, with small daily PRs humans can read (`xIt_mTQp6mY`). The debate panel agrees loops work only on verifiable tasks (`c35YoMdnI78`).
- **Worktrees or clones or VMs.** Worktrees are used in some talks (`z0sh8HyTrDo`, `W76woOYHlvY`). OpenClaw regrets them (`pmoDeA3RBZY`). Ona argues for VMs over containers (`5Sui_OnSRlY`).
- **Heavy harness or thin harness.** Conductor says do not beat the market and stay near the frontier (`TRfzFJCJ7ZE`). Cline says every added prompt instruction can hurt (`yUmS-F9IX90`). Tessl says raw harness engineering fails in practice, because the practice changes too fast and the work is unplanned, and it favours a governed skills registry (`X6l4lpA0_NY`).
- **Open problems.** Review capacity is "not fully solved" at Block (`whue9_YquGA`). Large codebases decay under AI volume, and repo docs barely help at that scale (`Bdrs3uAX0_M`). Prompt injection can only be bounded (`LqLoYksJ6do`). Model routing rules are still art, not science (`TN3mj92oZ8I`). Many productivity claims are self-reported (`17-YSUHo6Lk`, `VMemhtlsoNk`).

## How thinking changed over time (dated)

- **2026-05-18.** Focus is the loop and the workflow. Ralph loops, grill-me alignment, PRDs and vertical-slice tickets (`-QFHIoCo-Ko`, `2TLXsxkz0zI`). Factory's Missions show multi-day runs with a validation contract (`ow1we5PzK-o`). CI/CD is called broken for agent volume (`VktrqzQgytY`).
- **2026-06-18.** "Dark factory" at scale: OpenClaw's swim lanes and about 800 commits a day (`pmoDeA3RBZY`). The first pipelines from product signals to PRs appear (`zMiSRliEzv4`). Coordination is named the missing primitive (`5Sui_OnSRlY`).
- **2026-07-18.** The question shifts to the human role. Judgment, evidence bundles and accountability (`n97BCfyFIvw`, `ZpK5PWX2YRM`). Org adoption and maturity stages (`whue9_YquGA`). The loops debate sets "verifiability" as the test (`c35YoMdnI78`).
- **2026-08-18.** Skepticism and operations. "Why Software Factories Fail" (`Ib5GBkD555M`). Control-theory loops (`xIt_mTQp6mY`). Production credentials and microVMs (`LqLoYksJ6do`). Telemetry-driven agents (`JJGbw4ggaFs`, `9HbzAWnKbo4`). Forward-deployed engineering talks stress agent readiness (`wpOA-UXynoM`).
- **2026-09-18.** Platforms and org scaling. Uber's building blocks (`17-YSUHo6Lk`). Scaling is an org problem (`zCJtYuqwm7E`). Compound engineering stores learnings in the repo (`_ehJyfHg1Vk`). Review gets its own talk (`LlgiOCmFG_w`, 09-27).
- **2026-10-04 to 10-15.** The "factory" label gets scrutiny and sharpening. Self-improving factories (`TN3mj92oZ8I`, `tUPPVhBBcoM`). Outcome metrics (`HvboD89DyQ8`). Cost routing (`48YUYDjwfYY`, `vGCJ7diEtrw`). Three loops: inner, outer and meta (`X6l4lpA0_NY`). The CI and merge-queue layer is rebuilt for agent volume (`7b9tov5Uc5s`, `uuwDWRbxoYo`).

## Numbers worth remembering

- Release cadence at VS Code went from monthly to weekly. Code survival rose from 55% (GPT-4.1) to 86% (Opus 4.6) (`I2LL_wd89-A`).
- Uber: over 70% of PRs come from agents. Over 250 automated migrations covering about 9M lines. Over 100M model requests a day, with a guard under 100 ms (`17-YSUHo6Lk`). Self-reported.
- About 5 minutes of planning saves about 30 minutes of review (`W76woOYHlvY`).
- Smart-zone context limit is about 100k tokens, whatever the window size (`-QFHIoCo-Ko`, `c35YoMdnI78`).
- Longest Factory mission ran 16 days. About 50% of final lines are tests (`ow1we5PzK-o`).
- OpenClaw peaked near 800 commits a day with 60 to 70 agents. Worktrees made 70 to 80 directories a day and crashed the machine (`pmoDeA3RBZY`).
- Reddit stale-flag agent: 7 of 7 PRs passed CI, about $1.26 per PR (`6MudaeKdBSk`).
- Model routing saves about 25% in a conservative benchmark (`vGCJ7diEtrw`). Code review at half the price on an older model (`exiwa9QbQXI`).
- About 96% of engineers do not fully trust AI code, and only about half always verify (`n97BCfyFIvw`).
- A 5% per-step error rate can reach about 50% failure after 10 to 20 loop iterations (`c35YoMdnI78`).
- Block: about 3,500 engineers. About 90% used AI, mostly in the IDE, with no change in shipping speed (`whue9_YquGA`).
- Sonar and McKinsey: 80 to 90% have deployed AI, fewer than a third have scaled it (`XqF-IFHBCkM`).
- Uber SubmitQueue: serial merging could take up to about 20 days to get everything green. PR volume grows about 25% a month at the speaker's platform (`7b9tov5Uc5s`).
- Atlassian's trained comment filter reaches about 40% resolution against a human baseline of about 45% (`ojJXgXLUQFc`).
- A dependency-bump PR changed about 70,000 lines (`LqLoYksJ6do`).
- A migration of about 150 RPC procedures would take about six months by hand. The loop ships one small PR a day (`xIt_mTQp6mY`).

## From creator channels (Kai Explains, AI LABS, Better Stack)

Sources: 11 creator videos cited below, Nov 2025 to Oct 2026. Most steps below come from one video each, so treat them as one creator's tested setup, not consensus. Creator videos are mostly tutorials and news. Most numbers are self-reported or from demos.

### Practical playbook

1. **Write the spec and the check before the loop.** Make `features/<feature>/` with a `spec.md` (what to build, which skills, how to verify) and an empty `verification/` folder. Name the completion check in the spec (`PLyRe6Zk--8`).
2. **Use `/goal` for the completion loop.** The video treats `/goal` as the loop primitive, not `/loop`. A small model judges after every turn whether the goal is met. Pass the spec and say how completion is verified (`PLyRe6Zk--8`).
3. **Track a batch in one queue file.** Use a markdown table with feature and status columns (to do, building, done). A feature-batch skill appends rows and writes each spec folder. Stop when no row is left in to do or building (`PLyRe6Zk--8`).
4. **Split builder and reviewer.** The builder sub-agent works on its own git branch. A separate reviewer with a fresh context is told to assume a bug exists. On failure, restart the builder. Repeat until the row is done (`PLyRe6Zk--8`).
5. **Keep the merge as the human gate.** The agent opens one PR per feature with a summary and screenshots. Only merged work reaches the branch that deploys (`PLyRe6Zk--8`).
6. **Enforce gates with a stop hook.** Register a hook that runs when the agent tries to stop. If the gate is not met, exit with code 2 so the agent keeps going. The video does not show the config or the check script, so read the Claude Code hook docs first (`bBMp5tLxShQ`).
7. **Gate each checkpoint in order.** A planner splits the feature into small checkpoints ordered by complexity and writes them as JSON. A human approves the plan. Do not start checkpoint N+1 until N passes its gates (`bBMp5tLxShQ`).
8. **Write failing tests first for logic gates.** A test-planner writes tests for everything checkable without a UI, and they must fail first. A sub-agent implements. Another runs the suite. The gate passes only when all tests pass (`bBMp5tLxShQ`).
9. **Run an adversarial critic until it is clean.** The critic is told to assume the code is wrong. A fixer addresses its findings. Re-run the critic and stop when it reports nothing (`bBMp5tLxShQ`).
10. **Keep a learnings file for sub-agents.** Each human correction goes into one file that every sub-agent reads before it starts. Each correction also becomes a new checkpoint that runs through all gates (`bBMp5tLxShQ`).
11. **Build the oracle before the loop, and cap retries.** Get a deterministic pass or fail check that prints specific failures. Feed the failure detail back on each attempt. Cap retries; the decompilation loop uses 12 per function. Skip the loop when no grader exists (`hl6VOfzky5E`).
12. **Report pass@1 and pass@k with the budget.** State the attempt budget, harness and grader next to every benchmark number. Rerun vendor tables independently when you can (`hl6VOfzky5E`).
13. **Use a tracker ticket as the trigger.** Symphony polls the tracker. An issue moved to an active state starts a run in its own workspace, named after the issue ID. The workflow file holds YAML front matter (tracker key, active states, workspace root, agent command) and a markdown prompt per issue (`n8qDKMPpLXc`).
14. **Add clone and PR hooks to each run.** The after-create hook clones the repo and checks out a new branch. The after-run hook commits, pushes and opens a PR that links the ticket. The speaker says the default workflow does not work on a real repo without these hooks (`n8qDKMPpLXc`).
15. **Set git rules for parallel agents.** Agents may commit files and nothing else. Forbid stash, reset and pop. Forbid slow builds inside agent loops, and run the expensive check once per phase. Defer git operations to the end of each phase (`0TSxrzBVEwQ`).
16. **Shard parallel work, and give reviewers only the diff.** The port ran four worktrees with about 16 agents each. Reviewers saw the diff, not the implementer's reasoning (`0TSxrzBVEwQ`).

### Tools creators recommend

- Claude Code `/goal`: completion loop with a per-turn judge. `PLyRe6Zk--8`
- Claude Code Stop hook (exit code 2): harness-enforced gates instead of prompt rules. `bBMp5tLxShQ`
- Claude Code sub-agents with fresh context: builder, reviewer and critic roles. `PLyRe6Zk--8`, `bBMp5tLxShQ`
- Paseo app: drives a laptop Claude Code session from a phone. `PLyRe6Zk--8`
- Symphony (OpenAI, open source): Linear-polling dispatcher with per-issue workspaces. Spec is over 2,000 lines, so it can be rebuilt in another language. `n8qDKMPpLXc`
- Linear: the tracker that triggers Symphony runs in the demo. `n8qDKMPpLXc`
- Kiro (Amazon, VS Code fork): stage-gated requirements, design and task files, plus event-driven hooks. Free preview is 50 interactions a month. `Z9fUPyowRLI`
- Archon: YAML DAG workflows that mix AI and fixed steps, with a git worktree per run. No benchmarks shown. `-1BOhPOcEb8`
- Codex cloud: background tasks in isolated containers, with AGENTS.md as repo rules. `nPAXAAbU16w`
- Ghidra and objdiff: reference-match loop for binary work. `hl6VOfzky5E`
- Routa: local-first Kanban with lanes and evidence gates. `_16PhraFYjQ`
- Helix (Shopify, internal, not released): checkpoint-gated migration. You cannot use it yet. `r0u83Ss7QRc`, `bBMp5tLxShQ`

### Where creators agree or clash with the conference talks

- **Agree: the check sets the autonomy.** Creators say a loop needs a check the agent cannot argue with (`PLyRe6Zk--8`, `hl6VOfzky5E`). This matches the verification consensus above.
- **Agree: writer and checker are separate.** Fresh-context reviewers appear in three videos (`PLyRe6Zk--8`, `bBMp5tLxShQ`, `0TSxrzBVEwQ`). This matches the writer-checker consensus above.
- **Agree: deterministic code around the agent.** Hooks and tracker-driven scripts do the commit, push and gating work (`bBMp5tLxShQ`, `n8qDKMPpLXc`).
- **Agree: a person approves the merge.** The PR gate in `PLyRe6Zk--8` and the human-review-only design in `n8qDKMPpLXc` match the risk-tiered review consensus above.
- **Clash: parallel writers.** The Bun port ran up to 64 agents on four worktrees (`0TSxrzBVEwQ`). That goes against the serial-writer preference in the disagreements section. It worked only with strict git rules, and it was a mechanical translation, not feature work.
- **Clash: worktree isolation.** Worktrees alone did not protect the Bun port, because agents ran stash and reset on the shared repo (`0TSxrzBVEwQ`). Archon says each run never touches main (`-1BOhPOcEb8`), but it shows no data. Isolation needs rules on top.
- **Clash: thin evidence for unattended runs.** Level 2 of the loop talk ran for about three hours, and two PRs were merged (`PLyRe6Zk--8`). Gastown's 20 to 50 agent claim has no measured results (`_mrMidIwCzk`). The conference talks ask for measured outcomes. Treat these as demos.
- **Clash: hard gates versus advice.** Creators say a stop hook beats a prompt rule (`bBMp5tLxShQ`). That is the speaker's framing, with no comparison shown. The conference talks lean on deterministic validators, so the idea is close, but the evidence is not there yet.
- **Clash: headline numbers.** One creator shows a 99.2% within-four-attempts score next to an 88% first-try score. Harness, budget and grader moved results by about 25 points (`hl6VOfzky5E`). Read every headline pass rate with the same care.

### Watch first

- `PLyRe6Zk--8`: the most concrete Claude Code loop walkthrough. Covers `/goal`, the queue file, the builder and reviewer split, and the PR gate. Skip the Hedra sponsor read (about 11:20 to 12:47).
- `bBMp5tLxShQ`: checkpoints, a stop-hook gate and a critic loop. Config is thin, and the hype title and Hedra sponsor segment (about 6:24) are not evidence.
- `hl6VOfzky5E`: grader-first loops, and how to read agent benchmark numbers.
- `0TSxrzBVEwQ`: failure modes when many agents share one repo, and the rules that fixed them.
- `n8qDKMPpLXc`: tracker-to-PR dispatch and the hooks a real repo needs.

## Watch first

- `xIt_mTQp6mY`. Best framework for loops: sensor, controller, actuator, baseline plus per-PR ratchet, one small PR a day.
- `Ib5GBkD555M`. The strongest counter-argument to lights-off factories, with a staged planning method.
- `ow1we5PzK-o`. Most concrete multi-agent design: validation contract, fresh validators, structured handoffs.
- `17-YSUHo6Lk`. Full platform blueprint from a large org (gateway, MCP gateway, warm pods, skills).
- `LqLoYksJ6do`. Security model for agents near production: deterministic controller, no credentials, microVM.
- `LlgiOCmFG_w`. Cleanest layered review design, with the reviewer committing fixes.
- `wpOA-UXynoM`. Agent readiness as a count of deterministic validators.
- `7b9tov5Uc5s`. Why CI and merge queues break at agent volume, and what to do about it.
- `I2LL_wd89-A`. A real before and after with a survival metric.

## Implications for our projects

**AgentOS**
- Crucible (sandbox) should follow the isolation lessons: one VM or clone per agent, no write or CI credentials inside, a policed network path (`LqLoYksJ6do`, `iQ5xldZ9StU`, `5Sui_OnSRlY`).
- Govrix Scout is the same shape as Uber's gateway: identity, PII scan and small guard models under a latency budget, with a project ID on every call for attribution (`17-YSUHo6Lk`). Add per-task routing rules to the proxy, using best-of-k runs to learn them (`TN3mj92oZ8I`, `vGCJ7diEtrw`).
- SkillForge has an open question on success signals. Reuse the observer-agent pattern: mine runs, edit a skill, gate it with a PR (`TN3mj92oZ8I`, `X6l4lpA0_NY`). Use reviewer outcomes as labels and log skill traces for per-skill evals (`17-YSUHo6Lk`, `6MudaeKdBSk`).
- MemoryMesh can borrow agent-scoped memory with provenance, where each fact links to its source run and humans can edit it (`TN3mj92oZ8I`). Also the compound-engineering "solution documents" idea (`_ehJyfHg1Vk`).
- Next-phase benchmarks: the autoresearch eval contract (one scalar, time-bounded, hidden validation set) is a good template for correctness checks (`7RFJRDYroic`, `iCj_ATyThvc`).

- Registry: Tessl's governed skills registry (versioned, reviewed on publish, with owners) and Uber's skills marketplace with lint and trace feedback are prior art (`X6l4lpA0_NY`, `17-YSUHo6Lk`, `zCJtYuqwm7E`). Uber's progressive MCP projection (discovery, CLI, generated code) is relevant for MCP server cataloguing and token cost (`17-YSUHo6Lk`).

**ProsHarness**
- Checkpoint and resume matches the Ralph recovery check: inspect git state, and treat a dirty tree with passing tests differently from one with failing tests (`2TLXsxkz0zI`). Use fresh context per step with state on disk (`c35YoMdnI78`).
- Add a validation contract to the plan, critique and debate flow, written before implementation and checked by a fresh-context validator (`ow1we5PzK-o`, `vGCJ7diEtrw`).
- Phone approvals map to remote-controlled sessions and to attention queues (`so9l_MwS2yg`, `YIVkERhy8xo`). Reversibility gate (draft irreversible actions, stop and report) is a ready rule for loops (`2TLXsxkz0zI`).
- Skill ranking: add a meta loop over session logs to find missing skills (`so9l_MwS2yg`, `X6l4lpA0_NY`).

**Recurring interests**
- Haiku pipelines: stage-by-stage agents with a rubric or eval per stage fit entity-resolution style pipelines (`ITMXwI6QL6A`). Binary criteria with calibrated judges are the eval default (`pSto5YaNGUo`, `hfEczxdNyvU`).
- Keep reviewers in a separate context from implementers, and keep coding standards out of the implementer's prompt (`LlgiOCmFG_w`).
