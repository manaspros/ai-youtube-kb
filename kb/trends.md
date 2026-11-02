# Trends since 2026-05-18

What changed in AI engineering, for an engineer who builds agent infra. Source: notes on the 713 AI Engineer talks published since 2026-05-18 (319 in the last 60 days). Written 2026-10-18. Talk notes are paraphrased. Vendor numbers are claims, not measurements. Cite a talk by its `video_id`; the note lives at `videos/<video_id>.md`.

## What the creator channels are saying (Kai Explains, AI LABS, Better Stack)

These are single-author demos, reviews and news. Few report measurements, so most numbers below are one creator's test or a vendor's claim. A claim that rests on one video says so. Sponsored segments are flagged. AI LABS videos are rare in these notes, so most evidence is Kai Explains and Better Stack.

### 10 practical shifts

1. **Write the stop check before the loop starts.** Use `/goal` for work with a checkable finish, with a turn cap and a program or file as the check. Use `/loop` only for polling inside one session. Cron tasks there expire after three days. Sources: `guides/claude-code.md`, `guides/coding-agents.md`. Videos: `PLyRe6Zk--8` (sponsored segment), `Xxqu-kz00gw`.
2. **Keep the always-loaded instruction files short, and grow them from real mistakes.** One creator says 200 lines for CLAUDE.md and SKILL.md. Another says 500. Neither is measured. Each mistake should add one rule, and the rules belong in git. Sources: `guides/claude-code.md`, `guides/context-engineering.md`. Videos: `jwje1JK8Nqs`, `D4uBfIe7SzA`.
3. **Count the fixed overhead on every turn, then A/B it.** Tool schemas, CLAUDE.md, memory, skills and each MCP server load before the first prompt. One creator estimates 8,000 to 30,000 tokens of tool and rule text per message. A CLI loads only when called, so prefer one when it does the job. Single-creator estimates. Sources: `guides/token-cost-efficiency.md`, `guides/mcp-and-tools.md`. Videos: `FWShtLCP4OY`, `qXo1P5H2RXk`, `jwje1JK8Nqs`.
4. **Find the hidden agent calls before you cut cost.** Group OpenTelemetry traces by query source. One creator says background summaries fire about every 30 seconds per active agent, and each call resends the whole conversation. The size of this cost is disputed. Community reports say 8 to 20 percent. An Anthropic team member said about 2 percent overall. Source: `guides/claude-code.md`. Video: `F4h3a8HFBSE` (single video).
5. **Rank models and setups by cost per finished task.** List price misleads when one model writes far more output. One creator run gave $4.50 for one model and $27.86 for the other, because the second wrote about six times more output. Single run. Sources: `guides/token-cost-efficiency.md`, `guides/evals.md`. Videos: `Zc72O98x3nk`, `0lBvjhcRqyU`.
6. **Pin the model, harness and config, and log them with each score.** Log effort, the resolved model, the app version, output tokens and tool calls. One creator reports a 4.2-point score move that came with a 26 percent drop in output tokens. A creator cites the public Terminal Bench leaderboard, where a harness wrapper alone moved one score 8.1 points on the same weights (`3DVRznjCIS8`). Sources: `guides/evals.md`, `guides/claude-code.md`. Videos: `SxLUx8-hN1o` (single creator), `3DVRznjCIS8`, `y0BW4hpMpyM`.
7. **Keep the early context bytes stable.** An edit near the start of a context forces the cached suffix to be reprocessed. A paper cited by one creator cut the cache hit rate from 73.9 to 29.9 percent after one such edit. Put summarizer instructions after the cached prefix, and track cache hits per session. Sources: `guides/coding-agents.md`, `guides/token-cost-efficiency.md`. Videos: `9-iiHFQyzuM`, `y0BW4hpMpyM`.
8. **Expire evals and check their numbers before you trust them.** Write the eval before the build. Expect it to go stale after two or three model generations. Plant canary tokens. Re-run any number that looks too good, because one creator found a prefill figure that came from two harness copies warming each other's cache. Report judge agreement per question, not one aggregate. Sources: `guides/evals.md`. Videos: `pGro_uKt-_M` (sponsored segment in the middle), `OlNZCtk100Q` (one run), `GweZqgLxcCo`, `Uihz1NkhFM0`.
9. **Sandbox agents with default-deny network, and keep real keys outside.** Start with no network. Read the denial in the logs. Add one narrow rule per method and endpoint. Per-binary rules and credential injection at the egress proxy are the newer pattern. A command-text firewall is not a sandbox. Creators also warn that a repo's SessionStart hook can run code on folder open. The OpenShell video is a vendor-led demo with stated caveats. Sources: `guides/sandboxing-execution.md`, `guides/security-guardrails.md`. Videos: `SbwckhZkPGs` (Better Stack, vendor tool), `Afm-GNrJbEQ`, `lNsSxWQDqaU` (single news video).
10. **Measure prefill and memory before you buy hardware or quote speed.** Decode tokens per second is the number people quote. Agent work is prefill-bound, so time to first token on a long prompt decides usefulness. Ollama defaults to a 4,096-token context and truncates silently, so raise it to about 64k. Test the harness before blaming the model. Sources: `guides/local-ai.md`, `guides/inference-serving.md`. Videos: `mED-boddeWI` (Kai Explains), `VIm73gaY_hM` (Kai Explains, one microbenchmark), `qS5ZUEaKwNw`.

### Where creators and conference talks disagree

- **CLAUDE.md size.** Creators give 200 or 500 lines. The conference view is that instruction capacity has grown, so checking that rules are followed is now the hard part (`XzJD1bvXKjs`). Guides: `context-engineering`, `claude-code`.
- **Compaction.** One creator argues that compaction loses information that compounds over long sessions (`_DZ4kJwQ50s`, single creator). Another says to compact on purpose, with keep-lists, before a break (`jwje1JK8Nqs`). Talks split too. One shows full history winning an eval (`WP3hjUXd918`). Pocock says clear rather than compact (`-QFHIoCo-Ko`). Guide: `context-engineering`.
- **Skills versus passive docs.** One vendor eval found a passive index beat skills, and skills went unused in 56 percent of runs (`i0W90tlKfYg`, single creator). Conference talks treat skills as the standard unit to test and govern (trend 9). Guides: `skills-self-improvement`, `context-engineering`.
- **Judges and labels.** Conference talks calibrate a binary judge on about 30 human labels (`NdrSPm6NCdk`). Creator referee tests use a strong model as judge with no human labels (`Uihz1NkhFM0`, `BwNNcob3-A0`). Guide: `evals`.
- **Trials.** The evals guide asks for at least five trials per cell. Most creator comparisons run each model once (`J8-CdK4215Y`, `Zc72O98x3nk`). Guide: `evals`.
- **Self-hosting economics.** A conference talk reports a 90 percent cut in coding-AI invoices by self-hosting (`Ok6QdZHCcI8`). Creators are more skeptical. They say prefill, RAM and task completion decide the answer, and they warn that a headline figure may be a prefill number (`VIm73gaY_hM`, `mED-boddeWI`). Guide: `models-research`, `local-ai`.
- **MCP versus CLI.** Creators prefer a CLI when it can do the job, because MCP schemas stay in context all session (`jwje1JK8Nqs`). A talk reports MCP and CLI both near 83 percent success, with the CLI far cheaper (`26RtyAm9y_Q`). Another talk says CLIs lack credential injection (`pAnLpiAG6Es`), so this is not settled. Guide: `mcp-and-tools`.

### Watch first (8 creator videos, `video_id`, why)

- `PLyRe6Zk--8`: the three levels of loop engineering, with `/goal`, a reviewer per branch, and the steps shown. Sponsored segment flagged. Single creator.
- `jwje1JK8Nqs`: 24 usage tactics, each with the reason it costs tokens. Mostly the speaker's own unmeasured numbers.
- `SxLUx8-hN1o`: how to tell a model change from a config change. The best method in the creator set.
- `F4h3a8HFBSE`: how to find hidden background-agent calls with OpenTelemetry. Short, and it shows the method. The numbers are disputed.
- `D4uBfIe7SzA`: CLAUDE.md as a failure log. Read it before editing ours. The size claim is disputed.
- `SbwckhZkPGs`: per-request policy, credential injection and audit logs on top of containers. Vendor tool, with caveats the creator lists.
- `Zc72O98x3nk`: cost per finished task against list price. One run per model, so treat it as an illustration.
- `mED-boddeWI`: why the "100 tokens per second" figure was prefill, and why RAM now sets the cost. Kai Explains, 2026-11-01.

Guides are in `guides/`. Project reviews are in `insights/`. Dates are talk dates where a talk is dated; otherwise a month or phase from the guide.

## The 10 shifts that matter

**1. "Done" is now untrusted. Proof comes from records the model did not write.** (Aug to Oct 2026)
Teams moved from better prompts to verification harnesses. Hash receipts of real test output, Stop hooks that feed failures back, and per-app verifier CLIs are the pattern. A stale receipt cannot pass because it is tied to the current code. The writer and the checker are separate, and the pass criteria are written before the code.
Guides: testing-verification, coding-agents, agent-architecture. Talks: `vy7o1g2iHY8`, `q4WC4TowkBo` (2026-10-18), `MpZzWMdmQCE`, `ow1we5PzK-o`, `mR-WAvEPRwE`.

**2. Review, not writing, is the bottleneck. Review is layered and routed by risk.** (Sep to Oct 2026)
Coding agents write most code at leading teams (about 80% at Anthropic, `ZpK5PWX2YRM`). Practitioners stack cheap deterministic checks, then a separate-context agent reviewer that commits fixes, then humans on risky or irreversible changes. Trust is raised in stages: advisory, blocking, autofix, auto-approve. Recurring review comments become lint rules or skills. Greptile data says agent PRs are about as good as human PRs on proxy metrics, but tests passing is a weak proxy for mergeable.
Guides: pr-code-review, coding-agents, software-factory. Talks: `LlgiOCmFG_w` (2026-09-27), `_mi3alkqy4s` (2026-10-04), `474j-n1Ltxc` (2026-10-04), `EL123UNokkI` (2026-09-18), `U7ZYBCcdJPg` (2026-10-14).

**3. The model is untrusted. Enforcement moved into code, proxies and infrastructure.** (May to Oct 2026; consensus by autumn)
Prompts are not a security boundary. The LLM plans and deterministic code acts. The lethal trifecta (private data, untrusted content, external comms) is the shared threat model. Skills and MCP servers are now treated as supply chain and scanned.
Guides: security-guardrails, governance-compliance. Talks: `4lXks428C9o` (2026-09-18), `ws9XcGGPBDk` (2026-10-13), `NaOkR3VSfR4` (2026-10-09), `YXEqC05WEI0`, `ZyC56eV8sVw`.

**4. Zero credentials in the sandbox. A proxy or gateway injects secrets and stamps identity.** (Sep to Oct 2026)
The sandbox holds a placeholder. The real token is added at the egress proxy. Agents get their own identity and short-lived, per-tool-call tokens, minted only after a policy check. Default-deny egress and one sandbox per task go with it.
Guides: sandboxing-execution, security-guardrails, governance-compliance, mcp-and-tools. Talks: `Uv0nAf_7tyU` (2026-10-12), `MkRYPFIMCSA`, `BM2JX9hqsVQ`, `8aVbXXvJUY4`, `ZUZVNKFSmTM`, `I3znWC3MEXM`.

**5. The agent runtime split: stateless brain, replaceable hands, append-only session log.** (Oct 2026 productised)
Durable execution is the entry fee for async agents. Every model and tool call is a checkpointed step, and human approval is a parked wait plus a signal. Sandboxes get snapshot, pause, resume and fork instead of cold starts. Teams also keep simplifying toward one reasoning agent with deterministic code around it. Multi-agent is a manager over narrow workers plus a verifier, and the over-splitting backlash came in mid-2026.
Guides: agent-architecture, multi-agent, sandboxing-execution. Talks: `Uv0nAf_7tyU`, `9QebvrrY3KY`, `NaOkR3VSfR4`, `u6jJcIFDLE4`, `9dYcwOkpCE8`, `kiClTcJUnhc` (2026-10-17).

**6. Context is a scarce budget. Verification replaced "fit the rules" as the problem.** (Jun to Oct 2026)
Quality drops well before the window fills (rules of thumb: about 100k tokens or 40%). CLAUDE.md stays thin and grows from failures. Skills, tools and docs load progressively. Many builders clear and reload from file handoffs. Instruction capacity rose about 10x in a year, so checking that the model followed the rules is now the hard part.
Guides: context-engineering, coding-agents. Talks: `-QFHIoCo-Ko`, `LC3-P7v3yoI`, `KtBivPzmOM8`, `pqlWNihgdjI` (2026-09-18), `XzJD1bvXKjs`, `shRR1e2HXMk`.

**7. Evals converged on one loop, and public benchmarks are distrusted.** (Aug to Oct 2026)
Trace the agent, read traces by hand, name failure modes, write one narrow binary evaluator per mode (code first, judge only where code cannot decide). Calibrate each judge on about 30 human labels. Turn production failures into regression sets and gate CI. Observability and evals have merged. Since August, coding agents read traces through CLIs, cluster failures and propose fixes with a human at the merge gate. Static leaderboards are treated as gameable, so teams build private, oracle-validated ones.
Guides: evals, observability, testing-verification. Talks: `SHMCGrNJJGc` (2026-10-17), `NdrSPm6NCdk` (2026-10-06), `xLxhT2ZI7UM` (2026-10-06), `YIxzNZDDy1A` (2026-10-12), `Ib5t2RLtxvM`, `Yk87oUPVaxU`.

**8. Retrieval is a bounded agent loop over a small toolbox. Hybrid BM25 plus dense with RRF is the default.** (Jun to Oct 2026)
Tuned baselines matter: BrowseComp-Plus goes from about 60% (untuned BM25) to about 90% (hybrid harness). One rulebook assistant went from 92% to 97% hit rate with RRF. Tool descriptions are retrieved too (top-K schemas). Parsing and chunking set the ceiling. Graphs pay off only on multi-hop or aggregation questions.
Guides: rag-retrieval, data-engineering, context-engineering. Talks: `gonAewBZxfU` (2026-10-15), `O84lhGc1OOI` (2026-09-18), `ksjwtQop4os`, `X4w2Pkz5tDY`, `vh2VGuQ3zhY`.

**9. Skills are a standard folder format, and the field now proves and governs them. Memory settled on a loop.** (Aug to Oct 2026)
Skills are evaluated with paired with/without runs, trigger tests and CI gates. Short hand-written gotcha skills often beat long generated ones. Self-improvement is a trace-to-edit loop with a gate (PR review, held-out eval, regression suite). Skills carry owner, version and scan status. Memory is write, manage, read, evaluate, govern over typed stores, with nightly "dreaming" consolidation. Per-agent memory is called solved. Shared memory and measuring learning are open.
Guides: skills-self-improvement, memory, mcp-and-tools. Talks: `0vphxNt4wyk`, `vy7o1g2iHY8`, `p7gaxmCUiIU` (2026-10-12), `M05vON8i0aI`, `u-o0sW9nwmk`, `OA-Mc60Rboo` (2026-09-27), `9wZpvF3QleU` (2026-09-18).

**10. Cost and serving became agent-traffic distributed-systems problems.** (Sep to Oct 2026)
Agent prompts reuse 80 to over 90% of their prefix, so KV-aware routing and tiered KV offload are the main levers. Speculative decoding is mainstream but must be measured per workload, and retraining the draft on your own traffic is the top tip. TurboQuant lost on data-center throughput. Gateways added run-level budgets that refill, retry budgets, queue-depth shedding and per-route P99. Teams track cost per successful task and per merged PR. Open-weight models (GLM 5.2, MiniMax M3, Gemma 4) are near frontier, so provider, harness and routing decide results. Small RL-trained models on narrow tasks can beat large generalists (a 4B finance agent beat a 235B model for under $500).
Guides: inference-serving, infra-cost-scaling, models-research, training-finetuning-rl. Talks: `YXowceUKYJI` (2026-09-18), `cQQbJqvZkpo`, `75ckHC2LU_0` (2026-09-20), `sOB3HSiG8vo` (2026-09-20), `7c9FSUVcXR0`, `zrZ1amZBSPw` (2026-09-18), `TyPpSRXGhbc` (2026-10-10), `l1-D89bAuOA`.

## Where the field disagrees

- **Should humans still read code?** Pocock and Volkov keep humans on critical paths (`LlgiOCmFG_w`, `ZpK5PWX2YRM`). Voss and Gupta say hand review is at capacity and an engineered harness should replace it (`_mi3alkqy4s`, `AMiyLItEtLA`). For lights-off factories, Boundary says invariant checks are enough, and HumanLayer says they stall. Greptile finds agent PRs roughly even with human PRs, and eBay warns of review debt (`474j-n1Ltxc`, `TJPInBjhE4Q`). Guides: testing-verification, software-factory, coding-agents.
- **How far to trust an LLM judge.** One web-agent judge scored 74% where a stricter verifier scored 38% on the same agent (`xLxhT2ZI7UM`). Others calibrate a binary judge on human labels and use it (`NdrSPm6NCdk`). Proof advocates want no judge at all (`-CnA2lGfymY`, `lRa9sPaMyy4`). Guides: evals, testing-verification, security-guardrails.
- **One agent or many.** ZS and Vercel collapsed chains into one agent (`u6jJcIFDLE4`, `9dYcwOkpCE8`). Anthropic argues for isolation per item and up to about 1,000 sub-agents (`kiClTcJUnhc`). Factory prefers serial writers for multi-day work (`ow1we5PzK-o`). Guide: multi-agent.
- **Compaction or reset.** Summarizing breaks the prompt cache, and full history won one eval (`WP3hjUXd918`). Pocock says clear, do not compact (`-QFHIoCo-Ko`). Codex leans on compaction for weeks-long threads (`il1c1a2FufU`). Guides: context-engineering, multi-agent.
- **MCP, CLI or skills.** One study shows both MCP and CLI near 83% success, with the CLI far cheaper (`26RtyAm9y_Q`). Apify says CLIs lack credential injection (`pAnLpiAG6Es`). LinkedIn serves skills over MCP (`9wZpvF3QleU`). Reducto deleted a one-tool-per-endpoint server (`jJQoVkd5yLg`). Guide: mcp-and-tools.
- **Generated skills and self-edits.** SkillsBench says AI-generated skills can lower scores (`0vphxNt4wyk`). WorkOS found 553 hand-written gotcha lines beat 10k generated ones (`vy7o1g2iHY8`). Runlayer, Neo4j and Vercel auto-distill anyway (`u-o0sW9nwmk`). Reported gains such as 36% to 100% are anecdotes. Guide: skills-self-improvement.
- **Container or microVM.** OpenAI and Docker favour microVMs (`OqM67QG_Ikk`, `OE_lLNCNfQo`). Red Hat and OpenHands ship containers (`F1DYkY1BlfM`, `iH_wV8BbS24`). No talk compares guard placements head to head. GPU access is a weak spot for microVMs. Guide: sandboxing-execution.
- **Human approval as a control.** Many talks use it (`tDArkCqjA-c`). Keycard argues it causes consent fatigue and proposes mission-scoped approval (`ws9XcGGPBDk`). Duolingo saw skilled reviewers accept half of planted false flags. Guides: mcp-and-tools, product-ux.
- **Memory shape.** Graph, files or log: no talk settles it (`Q0VkgCyNVUg`, `ZRM_TfEZcIo`, `khVX_BUnEwU`). One benchmark found plain in-context learning beat costlier memory systems (`iqloyWCGYQQ`). Guide: memory.
- **Grep or vectors for code.** Cursor reports gains from semantic search (`zKk7sDMGDEQ`). Braintrust found equal accuracy at about 4x cost (`T3SS931wU0I`). Guide: rag-retrieval.
- **Fine-tune, RL or skills.** LeaseEnd found fine-tuning became tech debt versus editable skills. GEPA claims text-space reflection beats GRPO on sample efficiency, which is a speaker claim (`OA-Mc60Rboo`). Guide: training-finetuning-rl.
- **Do tools help whole teams?** Amazon: teams that changed how they work got 4.5x deployment velocity, tool-only teams under 3x (`pqlWNihgdjI`). DX org-level data shows modest lifts and bigger PRs (`Se8jHLliLXE`). Guide: enterprise-adoption.


Ranked by impact over effort across the three projects. Each item links to the full ranked list. Items the docs list as planned are "planned, not built", not "missing". Gateway has no repo docs, so every gateway item is "verify, then fix if missing".

2. **ProsHarness: add a hash-bound deterministic verify receipt.** Verify today leans on a model verdict. Bind a receipt of real test output to the current code and check it at a gate (Stop hook plus work-log). Talks: `vy7o1g2iHY8`, `q4WC4TowkBo`, `MpZzWMdmQCE`. Doc: [insights/prosharness.md](insights/prosharness.md), gap 1.
3. **ProsHarness: isolate headless runs from the user's Claude settings.** The evidence is ProsHarness's own docs (an RTK/org hook broke the allowlist), not a talk. Doc: [insights/prosharness.md](insights/prosharness.md), gap 2.
4. **AgentOS: budgets that reserve, then settle, with identity stamped by the proxy.** Today budgets fail open, per process, after the call. Use refilling run-level limits and a pre-call hold. Talks: `Uv0nAf_7tyU`, `ws9XcGGPBDk`. Doc: [insights/agentos.md](insights/agentos.md), gaps and risk 1.
5. **AgentOS: gate SkillForge with a paired with/without-skill eval, not frequency.** One team saw 97% without a skill and 77% with it. Talks: `0vphxNt4wyk`, `vy7o1g2iHY8`. Doc: [insights/agentos.md](insights/agentos.md), risk 2. The same ablation applies to ProsHarness skill ranking: [insights/prosharness.md](insights/prosharness.md), gap 8.
6. **Calibrate judges before any eval gates a release** (AgentOS judge calibration is planned, not built). Label about 30 cases, aim for 80 to 85% agreement, use binary judges. Do the same for the ProsHarness Codex critique. Talks: `NdrSPm6NCdk`, `SHMCGrNJJGc`, `xLxhT2ZI7UM`. Docs: [insights/agentos.md](insights/agentos.md), [insights/prosharness.md](insights/prosharness.md) gap 4.
7. **ProsHarness: build a task-level eval of the harness itself.** Then add a validation contract in the plan, approvals bound to the exact thing approved, a scheduler watchdog and an end-of-run retrospective. Talks: `QuuIywMG4s8`, `ow1we5PzK-o`, `vGCJ7diEtrw`. Doc: [insights/prosharness.md](insights/prosharness.md), gaps 3 and 5 to 9.
10. **AgentOS: resume instead of abort on preemption, with retry budgets.** Then run a paired memory-on versus memory-off eval, and add a simulation proof of budget correctness. Credential-injecting egress, distributed budgets and sleep-time consolidation are planned, not built. Talks: `sOB3HSiG8vo`, `YXowceUKYJI`, `iqloyWCGYQQ`, `MkRYPFIMCSA`. Doc: [insights/agentos.md](insights/agentos.md).

Caveat on the project reviews. The AgentOS review opened about 30 of its cited transcripts and checked that 12 more exist and match the notes. The security-guardrails guide rests on about 60 of its 117 talks in detail.

## If you watch only 10 talks

1. `Uv0nAf_7tyU` (2026-10-12): Anthropic's brain, hands and session-log split. Covers credentials in a vault and the append-only log.
2. `q4WC4TowkBo` (2026-10-18): WorkOS on making an agent prove it is done with a per-app verifier CLI.
3. `vy7o1g2iHY8`: the hash-receipt gate, and why short hand-written gotchas beat long generated skills.
4. `SHMCGrNJJGc` (2026-10-17): Arize workshop on the full trace, eval, judge calibration, CI gate loop.
5. `ws9XcGGPBDk` (2026-10-13): Keycard on the lethal trifecta, per-call tokens and mission-scoped approval.
6. `NaOkR3VSfR4` (2026-10-09): the LLM plans, a deterministic harness acts, durable state and human gates.
7. `LlgiOCmFG_w` (2026-09-27): Pocock on layering deterministic checks, agent review and humans.
8. `pqlWNihgdjI` (2026-09-18): Amazon's data on changing how teams work versus adding tools.
9. `YXowceUKYJI` (2026-09-18): KV-cache-aware routing and PD disaggregation for agent traffic.
10. `gonAewBZxfU` (2026-10-15): a concrete hybrid BM25 plus dense RRF result with numbers.

Close calls: `kiClTcJUnhc` (running 1,000 sub-agents), `xLxhT2ZI7UM` (why judges mis-grade), `zrZ1amZBSPw` (a production LLM gateway), `75ckHC2LU_0` (inference update).
