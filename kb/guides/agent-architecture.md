# Guide: agent-architecture
*Synthesized by Sonnet from 197 talks since 2026-05-18.*

Scope: agent loops, harnesses, frameworks, durable execution, long-running agents. The most recent talks (Aug to Oct 2026) weigh most.

## State of the art

**The harness is the product.** Many talks repeat one claim: the model is rented, the harness is where engineers have control. Production failures are mostly harness failures: lost state, concurrent writers, waits with no end, approvals that outlive their scope (`BInpv7lGp1o`, `xs-ob87TTzg`, `KtBivPzmOM8`). The contract that keeps coming back is "model proposes, harness commits, receipt proves" (`BInpv7lGp1o`, `NaOkR3VSfR4`, `m24UKZomm7k`).

**Brain, hands and session log are separate.** Anthropic's Managed Agents design splits the loop (stateless brain), the sandbox and tools (replaceable hands), and an append-only session log that is the only durable state (`Uv0nAf_7tyU`, `K0X9QDRkIdg`, `9QebvrrY3KY`). Credentials live in a vault or proxy and the model never sees them. Google's Interactions API uses the same shape with an interaction ID and an environment ID (`8aVbXXvJUY4`, `oWTEiYpxl80`). Lazy sandbox start cut time to first token by about 90% (`Uv0nAf_7tyU`).

**Long runs use separate generator and verifier contexts.** Self-evaluation is a trap. A planner, a generator and an evaluator each get their own context. The evaluator drives the live app (Playwright, computer use) against a rubric or a contract agreed before coding (`mR-WAvEPRwE`, `ow1we5PzK-o`, `kiClTcJUnhc`, `9QebvrrY3KY`). The contract is written before any code so tests do not just confirm what the code does.

**Durable execution is the cost of admission for async agents.** Wrap every model call and tool call as a checkpointed step, so a crash replays instead of restarting. Human approval becomes a parked wait plus a signal (`cI7zfqusmFU`, `jc3kbZkuHTo`, `VjEP0xqTUI0`, `NaOkR3VSfR4`, `s4r6nk5WsZw`, `L4I7WgiEquo`). Temporal, Restate and Conductor are the named engines.

**Deterministic code around small model steps.** Rules and code do facts, calculation and gating. The model plans, judges narrowly, or fills parameters (`m24UKZomm7k`, `8g0g1ncwzG0`, `rAUyRDOFyHU`, `Tt2kX2sgQio`, `EUsPvBeIx70`, `u6jJcIFDLE4`).

**Simple topologies win.** One reasoning agent with tools, plus subagents that return findings only. Several teams collapsed multi-agent chains back to one agent (`u6jJcIFDLE4`, `9dYcwOkpCE8`, `mYSRn6PC1mc`). Parallel fan-out is for read-only or isolated per-item work (`kiClTcJUnhc`, `buHC7bQE1X4`, `ow1we5PzK-o`).

**Files and a shell are the default substrate.** A sandbox with list, read and bash tools beat hand-built agents (`9dYcwOkpCE8`). Agents hand off through files (`mYSRn6PC1mc`, `oWTEiYpxl80`). Skills and AGENTS.md or CLAUDE.md files carry procedures and guardrails (`7jjudsEhBtM`, `pyvRID_CZZU`).

**Loops are control systems, not magic.** Ralph loops (fresh context per task, flat ticket files) work solo. Teams need a sensor, a controller and an actuator, with a deterministic baseline and a per-PR ratchet (`2TLXsxkz0zI`, `xIt_mTQp6mY`, `X6l4lpA0_NY`).

**Agents improve through traces.** Production traces become eval tasks, and a teacher agent or an offline "dreaming" pass rewrites skills or memory (`XyV6bSMyq-I`, `p7gaxmCUiIU`, `PXj0p_mW9nI`, `qJtcEDc_WJU`).

## Consensus patterns

1. **Climb the autonomy ladder only as needed.** Prompt, then context or retrieval, then fixed workflow, then agent. Add agents only where steps must branch (`mYSRn6PC1mc`, `FLUoowDJg4I`, `B0fjR3yaZFU`, `rAUyRDOFyHU`).
2. **Put gates in code, not in the prompt.** State machines, hooks, policy checks outside the model, hash-verified test receipts (`vy7o1g2iHY8`, `YXiLj4tJt5A`, `AgBAOXVxt4A`, `q-WOjZhOMCA`, `m24UKZomm7k`).
3. **Brain/hands split with an append-only log and vault-injected credentials.** (`Uv0nAf_7tyU`, `K0X9QDRkIdg`, `9QebvrrY3KY`, `IavxrdVnwXM`, `xn8EsW0wxyc`).
4. **Verify in a fresh context.** Separate verifier, reviewer, or adversary agent with a written rubric and an iteration cap (`mR-WAvEPRwE`, `ow1we5PzK-o`, `kiClTcJUnhc`, `FGftGOzfohc`, `qJtcEDc_WJU`, `2TLXsxkz0zI`).
5. **Fresh context per unit of work; reset and reload beats lossy compaction.** State lives in files or a log (`4kYl2_mqmnQ`, `9QebvrrY3KY`, `Wmp2Tku2PrI`, `2TLXsxkz0zI`).
6. **Keep the context lean.** Deferred tool loading and tool search, a capped skills list, memory pointers for big tool output, retrieval of skills (`shRR1e2HXMk`, `v3Fr2JR47KA`, `DrfyORO8RqA`, `KtBivPzmOM8`, `xo68uCibfm8`). A skills list in the prompt breaks above about 10 skills (`7jjudsEhBtM`).
7. **Fewer, workflow-shaped tools.** One REPL or one CLI beat many tools (`HEFSExa0xl0`). MCP wrappers per endpoint failed in team use (`jJQoVkd5yLg`). A CLI used fewer round trips than MCP for browser tasks (`26RtyAm9y_Q`).
8. **One reasoning owner; subagents return findings, not conclusions.** (`u6jJcIFDLE4`, `9dYcwOkpCE8`, `u6jJcIFDLE4`).
9. **Serialize writes per mutable state.** One ordered writer per session key, a deadline for every external wait, scoped approvals bound to exact arguments (`BInpv7lGp1o`, `cI7zfqusmFU`, `jc3kbZkuHTo`, `rAUyRDOFyHU`, `8g0g1ncwzG0`).
10. **Evals follow architecture and feed on production.** Match eval unit to architecture, use pass^k for reliability, and turn production failures into tasks (`nxokqOq1imY`, `XyV6bSMyq-I`, `31GUkCBD-Uc`, `jRCpXUjz4CI`, `B0fjR3yaZFU`).
11. **Replay and trace everything.** Event logs with causal IDs, content-addressed prompts, run receipts, replay with writes disabled (`KHudyx5wW3U`, `khVX_BUnEwU`, `BInpv7lGp1o`, `dQ-_i1tZiws`).
12. **Design for harness decay.** Harness workarounds go stale as models improve, so abstract the layer and gate swaps on evals (`K0X9QDRkIdg`, `mR-WAvEPRwE`, `sM1iYgz93HI`, `4loPnxvWWhg`).
13. **Move deterministic work out of the agent.** Statistical detection, calculation, and set resolution are done by code (`u6jJcIFDLE4`, `EUsPvBeIx70`, `Tt2kX2sgQio`, `5xi_S1f9sDU`).

## Disagreements & open questions

- **Workflow vs agent.** Many teams run deterministic workflows with small LLM steps (`rAUyRDOFyHU`, `8g0g1ncwzG0`, `FLUoowDJg4I`). Others say rigid pipelines lose to a minimal file-system agent (`9dYcwOkpCE8`) or to a loose prompt where the lead designs the topology (`kiClTcJUnhc`, `qJtcEDc_WJU`).
- **Single agent vs many.** ZS and Vercel collapsed to one agent (`u6jJcIFDLE4`, `9dYcwOkpCE8`). Factory and Anthropic push serial missions or flows with hundreds of isolated sub-agents (`ow1we5PzK-o`, `kiClTcJUnhc`, `buHC7bQE1X4`). Factory prefers serial writers over parallel swarms for multi-day work.
- **Orchestration logic in code or in prompts.** Factory keeps it in prompts and skills (`ow1we5PzK-o`). Others compile plans into graphs with a closed grammar and fail closed (`8g0g1ncwzG0`, `NaOkR3VSfR4`).
- **Compaction.** Append-only log plus re-read (`9QebvrrY3KY`, `K0X9QDRkIdg`) versus summarizing managers with a ratio and keep-last-N (`DrfyORO8RqA`). Platform-handled compaction for long sessions (`qJtcEDc_WJU`).
- **MCP vs CLI vs code mode.** Code mode and progressive discovery are promoted (`v3Fr2JR47KA`, `shRR1e2HXMk`). CLI is argued cheaper and faster (`26RtyAm9y_Q`). Deleting a thin MCP server and rebuilding it was needed (`jJQoVkd5yLg`).
- **Skills.** Skills are "the new features" (`7jjudsEhBtM`), yet 95% of generated skills were deleted for gotcha lists (`vy7o1g2iHY8`). A 12,000-line workflow replaced by a 200-line skill is cited in `FLUoowDJg4I`.
- **Where safety lives.** Deterministic floor plus an equal-power adversary agent (`1lgFGaHoGq8`), versus policy gates outside the model with typed plans (`q-WOjZhOMCA`), versus per-call authorization with budgets (`IavxrdVnwXM`). Open: how to make approvals cheap enough that humans do not rubber-stamp them.
- **Dreaming and self-modification.** Gains are modest and need your own evals (`qJtcEDc_WJU`, `khVX_BUnEwU`, `9QebvrrY3KY`).
- **Open:** harness lifetime is months (`sM1iYgz93HI`), so what to standardize is unclear. Open protocols are early (ACP in `YkNulwcc5jk`, Codex app server in `9WiBJRO84yY`, MCP Tasks in `s4r6nk5WsZw`). The median problem: shared harnesses make products converge (`0JZy5AuuQzc`).

## How thinking changed over time

- **2026-05-18.** The focus is shipping long runs. Raindrop says monitoring must complement evals (`-aM2EDTiaMs`). Ralph loops are reliable only on late-2025 models (`2TLXsxkz0zI`). Factory describes missions that ran 16 days (`ow1we5PzK-o`). Effect apps use lint as back pressure (`Wmp2Tku2PrI`).
- **2026-06-18.** Anthropic frames three limits of long runs and the generator/evaluator split (`mR-WAvEPRwE`). WorkOS shows enforced state-machine gates and gotchas-only skills (`vy7o1g2iHY8`). PostHog turns signals into PRs (`zMiSRliEzv4`).
- **2026-07-18.** Sandboxes and microVMs get a first-principles treatment (`OqM67QG_Ikk`). Fleet pain shows up: the human becomes the bottleneck (`4kYl2_mqmnQ`). A REPL replaces 15 tools (`HEFSExa0xl0`). Planner plus deterministic resolver replaces the agent loop (`EUsPvBeIx70`).
- **2026-08-18.** The big month. Brain/hands, durable session logs and vaults become the shared vocabulary (`K0X9QDRkIdg`, `9QebvrrY3KY`). "Model proposes, harness commits" appears (`BInpv7lGp1o`). Multi-agent failures and rebuilds (`u6jJcIFDLE4`). Loop engineering reframes Ralph (`xIt_mTQp6mY`). Event-sourced runtimes (`khVX_BUnEwU`). Always-on background agents (`vSx5IULvBns`).
- **2026-09-18.** Agents compared to microservices in 2015 (`32nrHU6zHU8`). Frameworks questioned (`KHudyx5wW3U`). Vercel collapses its chain into a file-system agent (`9dYcwOkpCE8`). Box says infrastructure half-life is months (`sM1iYgz93HI`). A fine-tune becomes tech debt versus editable skills (`4loPnxvWWhg`). Cost control moves to the run layer (`GJX19pNhmSw`). Evals must match each architecture generation (`nxokqOq1imY`).
- **2026-10.** Managed-agent surfaces mature: workspaces per tenant, YAML agents in CI, scheduled deployments (`QSeaZ6qHyXs`, `qJtcEDc_WJU`, `FGftGOzfohc`). Self-improving loops: teacher/doer strategy files (`p7gaxmCUiIU`), autoresearch (`7RFJRDYroic`, `vrDvatGtIxs`). Runtime authorization per call (`IavxrdVnwXM`). Open client protocols (`9WiBJRO84yY`, `YkNulwcc5jk`). Software factory with inner, outer and meta loops (`X6l4lpA0_NY`).

## Numbers worth remembering

- Time to first token: about 60% better at P50 and over 90% at P95 after splitting brain from hands (`K0X9QDRkIdg`); about 90% from lazy sandbox start (`Uv0nAf_7tyU`).
- Longest Factory mission: 16 days; about 50% of lines are tests (`ow1we5PzK-o`).
- Harness run: about $200 and six hours for a playable game that a solo run failed to produce (`mR-WAvEPRwE`). 50% task horizon rose from about 1 hour to about 12 hours across a year of Opus models (`mR-WAvEPRwE`).
- Antigravity run: 93 subagents, 12 hours, about 2 billion tokens, under $1,000 (`buHC7bQE1X4`).
- 99% per-step success over 100 steps gives about 36% end to end. A 50% per-run agent reaches about 94% with up to four retries (`5xi_S1f9sDU`).
- Tool replacement: 15 tools to one REPL, 50% to 92% accuracy; 74% after the REPL change alone (`HEFSExa0xl0`).
- Vercel data agent: eval score roughly doubled after moving to a file-system agent in a sandbox; about 100 skills distilled (`9dYcwOkpCE8`).
- Planner plus resolver: correctness 100% at all scales, versus about 80% falling to about 30% for the LLM-only approach (`EUsPvBeIx70`).
- Support agent: 10% to 80% resolution for about $700 a month (`pyvRID_CZZU`).
- ZS investigation: 20 to 30 minutes versus three to four weeks for an analyst (`u6jJcIFDLE4`).
- Skills list capped at about 2% of context in Codex (`shRR1e2HXMk`). Skills and tools can use over 50% of context; each skill is 3,000 to 5,000 tokens (`KtBivPzmOM8`). Prompt-list approach breaks above about 10 skills (`7jjudsEhBtM`).
- Context rot starts around 200k tokens by one rule of thumb (`mYSRn6PC1mc`). Multi-agent split suggested above about 20 tools (`mYSRn6PC1mc`).
- Fixed-budget comparison: execute rose from 0.15 to 0.76 at 600k tokens; advise reached 0.89 (`PXj0p_mW9nI`).
- TokenOps: spend down about 78%, completion 67% to 96% (vendor benchmark, `GJX19pNhmSw`).
- Event-typed runtime: about 20% of early events were rejected by schema (`KHudyx5wW3U`).
- Cache hit rates often exceed 90% on agentic traffic; cached tokens about 10x cheaper (`YXowceUKYJI`).
- Agent calls per task: 1 for chat, 10 to 20 for copilots, about 50 for research agents (`7c9FSUVcXR0`).
- CLI vs MCP: similar success (about 83%), 7 turns versus 71 round trips (`26RtyAm9y_Q`).
- Frustration rate fell from 37% to 9% after a prompt change, as read from monitoring signals (`-aM2EDTiaMs`).
- A Ralph-style loop in CI delivers one small PR per day; 150 procedures would take about six months one by one (`xIt_mTQp6mY`).
- Hill-climbed browser skill: $6.22 to $0.51 and 189 s to 27 s (`p7gaxmCUiIU`).
- Parameter Golf: one agent produced 15% of merged records on 4% of compute (`7RFJRDYroic`).

## From creator channels (Kai Explains, AI LABS, Better Stack)

Creator videos are single-author demos and reviews. Few report measurements. Most numbers are vendor claims or anecdotes, and the sections below say which.

### Practical playbook

1. **Write the stop condition before the loop starts.** Pick one: a measurable check, a turn cap, a timer, or an external event. A person owns the check. Skip loops for an MVP whose done state is still unknown. (`pGS7ku-4Fbs`, `PLyRe6Zk--8`)
2. **Use `/goal` for work with a checkable finish and `/loop` for polling.** `/goal` runs an evaluator after every turn until the condition holds. Set a turn cap. Run `/goal` with no arguments to see turns and tokens mid-run. Exact syntax is not shown in the videos. (`PLyRe6Zk--8`, `pGS7ku-4Fbs`)
3. **Make the oracle a file.** Write `goal.md` with the request, the objective and a done check. Prefer a program, such as tests passing or a score over a threshold. For UI work, use observable checks: dev server up, then a browser pass over each section. Single creator demo, no failure rates. (`q7Am0pV6FjQ`)
4. **Track the run in state files, not chat.** Keep `state.yaml` or a queue table with task IDs, status (to do, building, done), an active-task field and a progress file. Stop when no row is left as to do or building. (`q7Am0pV6FjQ`, `PLyRe6Zk--8`)
5. **Split builder and verifier.** The builder works on its own git branch. A separate review agent with fresh context, told to assume a bug exists, checks the branch. A failed check sends the builder back. Only the main-thread manager marks a task done. (`PLyRe6Zk--8`, `q7Am0pV6FjQ`, `pGS7ku-4Fbs`)
6. **Make the pull request the human gate.** Each feature opens a PR with a summary and screenshots. A person merges it, and only merged work deploys. (`PLyRe6Zk--8`)
7. **Use `/loop` only inside one session.** The minimum interval is one minute. Cron tasks expire after three days and live in session memory, so a new session starts with none. Do not use it for listeners that must outlive a session. (`Xxqu-kz00gw`)
8. **Pick the scheduler by where the work must run.** Claude Desktop's Scheduled runs only while the machine is on and the app is open. Cowork's Scheduled runs in a sandbox. Routines (`/schedule`) run on Anthropic cloud infrastructure. (`Xxqu-kz00gw`, `yVnsU-xqng4`, `pGS7ku-4Fbs`)
9. **Write routine prompts for unattended runs.** Tell the routine not to ask for permission or clarification. Forbid horizontal rules in Slack output, since the video reports Slack block validation fails on them. List required connectors up front. (`yVnsU-xqng4`, single creator demo)
10. **Fix cloud network and skills before the first run.** The default routine environment blocks Bash network calls. Use a custom environment with a domain allowlist, or have the prompt use WebFetch. Ship skills and hooks in the repo's `.claude` folder, and add a prompt check that the skill loaded. (`yVnsU-xqng4`, single creator demo)
11. **Pilot big workflows on a small slice and watch spend.** Dynamic workflows can spawn hundreds of agents. Watch with `/usage` for spend, `/workflows` for per-agent tokens and kills. Use a cheap model for triage and a capable one for judgment. (`pGS7ku-4Fbs`)
12. **Set the budget before the agents start.** Paperclip caps company or agent budgets before heartbeats begin, so spend is limited by the control loop, not reviewed afterwards. (`xZ7OmRz2i7o`, single creator review)
13. **Turn a plan into dependency-aware tasks.** Ask Claude Code to convert a plan file into tasks with blocks and blocked-by links. Run each unblocked task in a sub-agent. One demo kept the main session at 18% context. Set the task-list ID variable to share tasks across sessions. The variable name is as transcribed, so check the docs. The video's only documentation was a tweet. (`-xOAYPjhigY`)
14. **Commit task state to git.** Commit the tasks folder and pull it on another machine to resume. (`-xOAYPjhigY`)
15. **Hold the harness fixed when comparing models.** Run the same weights in two harnesses on the same task, and record the harness version with each score. The public Terminal Bench leaderboard shows a wrapper alone moving a score 8.1 points on the same weights. (`y0BW4hpMpyM`, `3DVRznjCIS8`)
16. **Keep earlier bytes stable for cache hits.** Build each request by replaying an append-only log. Put summarizer instructions at the end, after the cached prefix. Track cache-hit share per session. Editing early context forces reprocessing, and one paper's test cut the hit rate from 73.9% to 29.9% after an edit. (`y0BW4hpMpyM`, `9-iiHFQyzuM`)
17. **Measure tool-description overhead per message.** One video cites 8,000 to 30,000 tokens of tool and rule text per message. (`qXo1P5H2RXk`)
18. **Enforce permissions in the harness, not the prompt.** Keep a list of commands that need approval and forbidden directories. Choose sandbox or host execution. Give each concurrent agent its own git worktree. (`qXo1P5H2RXk`)

### Tools creators recommend (tool — what for — video id)

- Claude Code `/goal` — loop until a measurable condition holds, with an evaluator after each turn — `PLyRe6Zk--8`
- Claude Code `/loop` — in-session interval polling, three-day expiry — `Xxqu-kz00gw`
- Claude Code routines (`/schedule`) — cloud scheduled or GitHub- and API-triggered runs, daily cap — `yVnsU-xqng4`
- Claude Code tasks — dependency-aware task files shared across sessions — `-xOAYPjhigY`
- Claude Code mods — in-process TypeScript plugins for status lines and event rewriting — `EiThSVZ8pME`
- Goal Buddy — oracle-first plugin with file state and judge, scout and worker roles, for Claude Code and Codex — `q7Am0pV6FjQ`
- Symphony (OpenAI) — polls Linear, one workspace per issue, after-create and after-run hooks — `n8qDKMPpLXc`
- Multica — self-hosted orchestration of coding CLIs as assignable agents — `WdGSXQPwwmo`
- Paperclip — multi-agent company model with budgets and audit trail, overkill for one agent — `xZ7OmRz2i7o`
- Flue — TypeScript harness framework, one-file agents, skills in workflows — `n5cYS6KuyK8`
- Cloudflare Dynamic Workers — runtime-created JavaScript sandboxes, no filesystem — `7Re3HReM5SQ`
- Cloudflare Artifacts — Git store for fork-per-task agent workspaces, private beta — `PWj6GnTUBnk`
- PG Durable (Microsoft) — durable workflows, timers and approval signals inside Postgres — `4Lmqvn_yz-c`
- AgentMail — email inboxes for agents, no MCP setup needed — `U3TXAdpmvVk`
- llama.cpp llama-server with LlamaSwap, and AnythingLLM — one local OpenAI-compatible endpoint behind chat, RAG and coding tools — `np8booSU7Og`
- Jan — local server on port 1337 that speaks the OpenAI format — `VghawjhiGkw`
- DeepSeek harness — append-only event log, cache-stable context — `y0BW4hpMpyM`
- LangChain DeepAgent — model-agnostic harness, memory in your own Postgres or an agents.md file — `jtWjkdBNqlk`
- Claude Agent SDK, OpenAI Agents SDK, LangGraph — framework comparison by terms, licensing and stability — `8C3LB6TPxwk`
- Prime Agent — persistent Python REPL as the only tool, learned layer over a fixed prompt, MIT licence — `kg3MmLd0qEM`, `_DZ4kJwQ50s`
- Anthropic Managed Agents — hosted sessions billed per session-hour with runtime credential vaulting — `uxHolzq1NcA`
- Model Context Protocol 2026-07-28 spec — stateless requests, explicit state handles — `f4mI3d-nTrI`, `k5f1uID3GcU`
- Hookdeck event gateway and Outpost — queue webhooks, replay, rate-limit delivery — `ElaEGr2t9XQ`
- Docker Agent — agents as YAML, served over A2A, MCP or HTTP — `Mph1H5u3yeA`
- Qwen Audio Agent — voice front end with a slow coding worker over ACP — `blpZ1xgFhCk`
- TEN Framework — graph-of-extensions voice runtime, barge-in test — `ES3HhoYCtIc`
- YC QM — multi-user harness with seven primitive tools and org approval modes, two weeks old at the video — `GrZ-X3-2TVs`
- Goose — goal-driven agent that uses MCP extensions — `VghawjhiGkw`

### Where creators agree or clash with the conference talks

- **Agree: the harness is the lever.** Several creators say the harness, not the model, moves scores and cost. Two of them show the same weights changing outcome with only the harness swapped. Evidence is single-creator demos. (`qXo1P5H2RXk`, `y0BW4hpMpyM`, `3DVRznjCIS8`)
- **Agree: fresh-context verifiers and file state.** Goal Buddy's judge, the builder and reviewer split, and the judge agent in the proactive loop match the conference verifier pattern. The creator versions give no pass-rate data. (`q7Am0pV6FjQ`, `PLyRe6Zk--8`, `pGS7ku-4Fbs`)
- **Agree: vendor numbers need your own test.** Creators flag unverified claims, such as Cloudflare's per-second figure and SkillWeaver's 99% saving, whose benchmark was self-run and whose execution was mocked. (`7Re3HReM5SQ`, `eCZwexfka6E`)
- **Clash: role teams versus one owner.** Goal Buddy, Paperclip, Multica and the queue factory run several role agents. The conference talks above favour one reasoning owner and report multi-agent failures. Creators show demos, not failure rates, so the evidence is weaker on their side. (`q7Am0pV6FjQ`, `xZ7OmRz2i7o`, `WdGSXQPwwmo`, `PLyRe6Zk--8`)
- **Clash: Ralph loops.** The conference view is that Ralph loops work well on bounded task lists. Creators say they suit bounded lists, not open-ended improvement, and that `/loop` and cron are not durable loops. Both can hold, depending on how open-ended the work is. (`-xOAYPjhigY`, `Xxqu-kz00gw`)
- **Clash: managed cloud cost.** The conference talks praise the managed brain and hands split. One Better Stack review calls routines too expensive for most automation and prefers self-hosted webhook agents on cheaper models. Its cap figures come from one account. (`yVnsU-xqng4`, `uxHolzq1NcA`)
- **Agree, with a cost angle: compaction is lossy.** Creators argue summaries lose facts and invent details, and propose externalized state, folding or self-edited context. They add the cache cost of editing old context. These are single-creator papers and demos. (`_DZ4kJwQ50s`, `W3yHP9_jYNk`, `9-iiHFQyzuM`)

### Watch first (creator channels)

- `PLyRe6Zk--8` — three levels of loop engineering: spec as goal, queue factory with adversarial reviewer and PR gate, phone control. Concrete steps. Contains a sponsor read.
- `pGS7ku-4Fbs` — four loop types by who decides when to stop, plus cost monitoring. Secondary explainer of one Anthropic post, no new benchmarks.
- `Xxqu-kz00gw` — exact limits of `/loop` (three-day expiry, session memory) and which durable scheduler to use instead.
- `yVnsU-xqng4` — routine setup gotchas and daily caps, with a PR-review example. One account, one presenter.
- `q7Am0pV6FjQ` — oracle-first runs with file state and read-only judge roles. Two anecdotal runs, no timings or costs.
- `y0BW4hpMpyM` — harness as a variable, append-only logs and cache-stable context. Vendor-led, but the cache design is specific.

## Watch first

- `BInpv7lGp1o` — the cleanest statement of harness failure modes: state ownership, ordered commits, deadlines, scoped approvals, receipts. Has a five-question audit.
- `Uv0nAf_7tyU` — brain/hands/session design and lazy sandboxing, from the team that built it.
- `mR-WAvEPRwE` — planner, generator and evaluator with sprint contracts and a live-app evaluator. Includes the habit of deleting harness parts as models improve.
- `u6jJcIFDLE4` — a candid multi-agent failure and rebuild. Short and specific.
- `ow1we5PzK-o` — Factory's mission design: validation contract first, serial writers, structured handoffs.
- `xIt_mTQp6mY` — loop engineering as a sensor, controller and actuator, with a ratchet in CI.
- `NaOkR3VSfR4` — plan-compile-execute on a durable engine, with approvals and idempotency in code.
- `9dYcwOkpCE8` — decompose then collapse, minimal file-system tools, query-to-skill distillation.

## Implications for our projects

**AgentOS (Govrix, MemoryMesh, Crucible, SkillForge)**
- Govrix Scout already sits at the egress point. Copy the proxy-side credential injection and per-call authorization with budget feedback (`8aVbXXvJUY4`, `Uv0nAf_7tyU`, `IavxrdVnwXM`). Make the budget a token the agent can read, not just a hard stop. Steer first, halt last (`GJX19pNhmSw`).
- Crucible: use the isolation ladder (containers, then gVisor, then microVMs, in order of increasing isolation) and snapshot/resume with a short idle timeout (`OqM67QG_Ikk`, `fz6-NS7qpZc`). Expose the sandbox as a persistent REPL, not many tools (`HEFSExa0xl0`, `shRR1e2HXMk`). Gate the exec with an out-of-model policy check (`q-WOjZhOMCA`, `1lgFGaHoGq8`).
- SkillForge success signal: use a replayable environment plus a verifiable outcome as the precondition (`p7gaxmCUiIU`, `7RFJRDYroic`). Mine the action log for skills at tool, company and personal level (`xxfMT-bPEmU`, `9dYcwOkpCE8`). Keep a skill only if paired with/without evals improve pass rate (`vy7o1g2iHY8`). Gate adoption of dreamed memory edits with your own evals (`qJtcEDc_WJU`).
- MemoryMesh: treat memory as profile plus on-demand search, with background re-synthesis (`5ZGyKWjQDr0`). Use tiers and a recall step with a distance threshold (`KtBivPzmOM8`, `xs-ob87TTzg`).
- Next-phase thesis (distributed system with correctness checks): a durable session log with explicit states idle, running, rescheduling, terminated is a ready-made correctness model (`K0X9QDRkIdg`). Test ordered commits per session key (`BInpv7lGp1o`). Report cost per successful task, not per token (`7c9FSUVcXR0`). Report pass^k for reliability (`nxokqOq1imY`, `tyFPqtyOK5w`). Use a content-addressed event log for replay (`KHudyx5wW3U`, `khVX_BUnEwU`).
- InferCraft: agent traffic is multi-turn with over 90% cache hits, so session-aware routing and tiered KV matter more than mean latency (`YXowceUKYJI`).

- Registry: skills as governed, versioned units with publish review (`X6l4lpA0_NY`); descriptions as routing signals (`7jjudsEhBtM`); agents as YAML in CI (`QSeaZ6qHyXs`). Add an agent identity card with delegator and revocation path (`q-WOjZhOMCA`). ACP and the Codex app server are worth cataloguing as client-to-harness protocols (`YkNulwcc5jk`, `9WiBJRO84yY`).

**ProsHarness**
- Checkpoint/resume: reset-and-reload from handoff files beats compaction (`4kYl2_mqmnQ`, `9QebvrrY3KY`). Log every step so resume reads the log (`K0X9QDRkIdg`). Wrap steps so a crash replays to the failure point (`cI7zfqusmFU`).
- Plan, critique (Codex), debate: use a separate-context critic and write a validation contract before the build (`ow1we5PzK-o`, `mR-WAvEPRwE`). Cross-model adversarial review is already used in practice (`AgBAOXVxt4A`).
- Loops and schedules: add a sensor, a ratchet and flow control that skips a run while its last PR is open (`xIt_mTQp6mY`). Add the recovery check from git state (`2TLXsxkz0zI`).
- Approvals: bind an approval to the payload hash and recheck before sending (`8g0g1ncwzG0`). A blocking review gateway with a hook matches the phone-driven approval idea (`4kYl2_mqmnQ`). Treat the human as an async API with a timeout (`jc3kbZkuHTo`).
- Zero-token credentials: keep secrets in the runtime or an egress proxy, never in context (`xn8EsW0wxyc`, `Uv0nAf_7tyU`).
- Hash-verified test receipts are cheap to add at each gate (`vy7o1g2iHY8`, `AgBAOXVxt4A`).

**Recurring interests**
- Haiku pipelines: put the harness in a state machine and run narrow steps on a small model (`m24UKZomm7k`). Cheap models plus cross-family disagreement as an audit worked for entity resolution at about 2% of frontier cost (`Fa3hQVIKShw`). Map with a cheap model, reduce with a strong one over agent logs (`jRCpXUjz4CI`).
- Subagents: give the lead one reasoning role and let subagents return findings only (`u6jJcIFDLE4`). Use self-referencing sub-agents that copy the definition, not the transcript (`FGftGOzfohc`).
- Agent evals: build the environment as instruction, sandbox and verifier (`jRCpXUjz4CI`). Replay past cases with writes off (`dQ-_i1tZiws`).
