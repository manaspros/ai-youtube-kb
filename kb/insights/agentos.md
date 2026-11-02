# Insights: agentos

*Synthesized by Sonnet from 303 talks since 2026-05-18.*

Scope note. I checked the project docs first. Built and measured today: Govrix proxy with PII and injection scan, Merkle audit log, exec-gate guardrail, hybrid BM25 plus pgvector with RRF, tiered memory, GraphRAG, RAGAS, the 4-class scheduler with live preemption, native CPU KV offload, celld sandbox, and Locust and Grafana evidence. Planned only (roadmap doc 10): judge calibration, pass^k gate, causal skill admission, sleep-time consolidation, distributed budgets, SSE passthrough, credential-injecting egress proxy. I do not call any of these "missing" below. I call them "planned, not built".

## What we're doing right (validated by talks)

- **Hybrid retrieval with RRF.** Talks back the BM25 plus dense choice. One RAG assistant over rulebooks raised hit rate from 92% to 97% on 63 questions with dense plus BM25 fused by RRF (`gonAewBZxfU`). A knowledge-agent talk reports a hybrid harness near 90% with about 20% fewer tool calls, and says to tune BM25 before judging it (`O84lhGc1OOI`). Multiscale chunking with RRF is the next step (`r9OwPx_HoV0`).
- **Opt-in proxy as the control point.** Uber runs one OpenAI-compatible gateway with an anonymizer and guard under a latency budget (`17-YSUHo6Lk`). Twilio describes the same fallback, timeout and fail-open choices we face (`zrZ1amZBSPw`). Our one-URL adoption matches this pattern.
- **Guardrails in code, not prompts.** Several talks say prompts are not a security boundary and enforcement must be deterministic (`4lXks428C9o`, `YXEqC05WEI0`). Our exec-gate hook is on this side of the line.
- **Append-only audit.** Practitioners call an immutable event log the base of auditability (`mav15aW9lLM`, `KHudyx5wW3U`). Our Merkle log fits, with caveats below.
- **Measuring honestly.** Our H2O result (worse than recency eviction) and the 202 ms versus 200 ms miss are the kind of reporting talks ask for. They say report variance, cost and config, not one number (`YIxzNZDDy1A`). Another suggests turboquant-style 4-bit KV hurt throughput, which supports not defaulting to exotic KV tricks (`75ckHC2LU_0`).
- **Keeping a file-and-tier memory idea in view.** Our tiered memory is close to what practitioners ship: a running profile plus search tools, with nightly consolidation (`5ZGyKWjQDr0`, `xLUQOqjudtA`).

## Where we diverge from what practitioners found (risks)

1. **Budgets fail open, per process, after the call.** Docs admit this. A talk on agent budgets says the proxy should stamp identity and cap every write with a refilling limit, so the agent cannot write its own provenance (`rbjWzZK2LU0`). Our budget check always allows. This is the biggest risk for a governance product.
2. **Frequency as the skill gate.** SkillForge admits skills at support >= 10 and success >= 0.8. Practitioners found that a skill can lower success. One team saw 97% without a skill and 77% with it (`vy7o1g2iHY8`). Another says AI-written skills can hurt and need with/without checks (`0vphxNt4wyk`). Frequent is not useful.
3. **Preemption aborts and never resumes.** Production routing talks stress retry budgets, outlier penalties and keeping a session's KV warm (`sOB3HSiG8vo`, `YXowceUKYJI`). Abort-without-resume wastes the prefill we paid for.
4. **Audit hash covers metadata, not payload.** The compliance talk wants small events that reference immutable payloads, so history can be rebuilt (`mav15aW9lLM`). A run receipt should also record policy version, idempotency key and attempt (`BInpv7lGp1o`). Ours does not yet.
5. **Memory that is never tested for benefit.** A Berkeley talk found plain in-context learning beat costlier memory systems on early results, and measures gain against a stateless run (`iqloyWCGYQQ`). A workshop found keeping full history beat every compaction preset once caching is counted (`WP3hjUXd918`). We ship tiered memory with no paired result yet.
6. **Credentials near the sandbox.** Talks agree the sandbox and model should never hold secrets, and a proxy injects them (`Uv0nAf_7tyU`, `MkRYPFIMCSA`). Our egress is a binary allow or deny. Planned, not built.

## Gaps: things we should build or change (ranked by impact over effort)

**1. Reserve-then-settle budgets with proxy-stamped identity.** (Roadmap lists it; talks raise its priority.)
- Why: closes the fail-open hole. Identity must come from the proxy's credential mapping, not a client header.
- Evidence: `rbjWzZK2LU0`, `BInpv7lGp1o`, `dSg0pu8d6qg`.
- First step: write a test that a client header cannot reset or spoof a budget. Make it fail first, then fix. Add a per-session id to each audit row.

**2. Paired with/without-skill eval as the SkillForge gate.**
- Why: replaces the frequency gate with an effect measure. Open question Q on success signal gets a concrete answer.
- Evidence: `0vphxNt4wyk` (10 to 20 prompts, half should-not-trigger, repeat runs), `vy7o1g2iHY8` (paired pass rates), `KA5kPbdkK2E` (blank holdout: skip injection on a small sample, compare completion).
- First step: pick one mined skill, run 20 cases three times each with and without it in Crucible, record the pass-rate delta. Flag negatives.

**3. Judge calibration before any eval gates a release.** (Planned in doc 10; do it first, everything else depends on it.)
- Why: our RAGAS scores are unvalidated judges.
- Evidence: `3z2uT5aDx_Y` (about 100 hand labels, train/dev/test, precision and recall), `NdrSPm6NCdk` (about 30 labels, 80 to 85% agreement, flag 100% as overfit), `SHMCGrNJJGc` (judge needs the same retrieval context the agent saw).
- First step: hand-label 100 MemoryMesh traces and report judge precision and recall with intervals.

**4. Resume instead of abort in the scheduler, plus retry budget and outlier weight.**
- Why: turns wasted preempted work into finished work. The 2 ms p99 miss likely sits in this path.
- Evidence: `sOB3HSiG8vo` (retry budget tightens with utilization, reduce weight instead of eject), `YXowceUKYJI` (session pinning, cache-hit tokens counted separately), `woIYJYd_etI` (report TTFT and inter-token latency separately).
- First step: add TTFT and inter-token histograms and cached versus uncached token counts to Grafana, then requeue preempted work and measure completion.

**5. Paired stateful versus stateless eval for MemoryMesh.**
- Why: shows whether memory helps at all, and at what cost.
- Evidence: `iqloyWCGYQQ` (gain = stateful minus stateless reward, Pareto with cost, drift injection), `WP3hjUXd918` (planted-fact probe; keep-all baseline).
- First step: run one fixed task sequence with memory on and reset-per-task, plus a keep-all baseline. Report gain and cost.

**6. Distributed budget correctness proof.** (Roadmap items DS 1 to 4.)
- Why: the next-phase thesis is correctness, not demos. Stale reads are the real risk.
- Evidence: `DqtmZE6Hl0g` (seeded simulator that returns legal stale reads, hidden ground truth in trace events), `BInpv7lGp1o` (one ordered writer per state).
- First step: a small deterministic simulator for the Redis counter with stale reads and failed optimistic writes. Assert "never exceeds budget".

**7. Credential-injecting egress proxy and per-call scoped tokens.**
- Why: removes secrets from Crucible, and fills the egress gap celld cannot.
- First step: give the sandbox a placeholder token and swap it in Govrix. Test that no secret appears in sandbox env or logs.

**8. Eval hygiene and a private end-to-end task suite.**
- Why: we have retrieval evals and load tests but no end-state agent tasks.
- Evidence: `QuuIywMG4s8` (grade end state, triage failing traces), `Ib5t2RLtxvM` (trace-to-task with an oracle solution that must pass), `YIxzNZDDy1A` (five runs per config, mean, worst, solved-every-run, cost).
- First step: one Harbor-style task for a Crucible exec flow with an oracle and a state verifier.

**9. Run receipts and payload commitments in the audit log.**
- Evidence: `BInpv7lGp1o`, `mav15aW9lLM`, `KHudyx5wW3U`.
- First step: add policy version, idempotency key, attempt number and upstream result to each Merkle entry.

**10. Independent verifier for Crucible-driven checks.**
- Evidence: `imFedndyXYQ` (fresh agent sees only the claim, assumes it false, reproduces it in a fresh sandbox), `k72eLcYpVys` (agent-written workflow tests, results in SQLite, tag interface versus sandbox failures).
- First step: have an agent write about 100 Crucible workflow tests and log failures by layer.

## Ideas to steal

- **Self-agreement ceiling test.** Run production several times on the same input. One team saw about 93% self-agreement, then judged cheaper candidates against that, not against 100% (`8g1N_a3h9H0`). Use it for quantized or speculative variants.
- **Blank-injection holdout.** Skip injecting a skill or memory on a small random slice and compare outcomes (`KA5kPbdkK2E`).
- **Knee benchmarking.** Sweep concurrency 1 to 64 and report where throughput flattens (`4n08JHb90hI`). It fits our 1,700 req/s ceiling story.
- **KL divergence against the unquantized model** to pick quant levels, and test inside the real harness (`J4_jCrTxMkk`). This helps when we unblock NVFP4.
- **Content-addressed prompts.** Store each prompt part by hash, keep requests as hash lists, add a run-diff command (`KHudyx5wW3U`).
- **Failure-to-fix mapping.** Each failed trace maps to a preventive gate, not a "be careful" prompt line (`dQ-_i1tZiws`).
- **Offline "dreaming" pass** that rewrites wrong memories, A/B tested against in-band writes (`9QebvrrY3KY`). Our roadmap has the idea; the talk gives the test shape.
- **Suggest-then-accept memory writes** with a named human author (`0uC6u0lJJl4`).
- **Eval sizing for rare failures.** Compute how many cases you need before quoting a failure rate (`AN65uc645mE`).
- **Cheap-first guard stage.** Regex, then a small classifier, then the model, and count calls saved (`1tpqdglI3T0`).

## From creator channels (Kai Explains, AI LABS, Better Stack)

Input: 36 creator-channel notes (Kai Explains and Better Stack). The input held no AI LABS notes. None of the cited notes flagged a sponsored segment.

### Ideas and tools to try (ranked)

1. **Hard spend caps per upstream key, enforced at the proxy.** Test that a per-key cap stops traffic, not just alerts, and measure how far spend overshoots. Why: the OpenCode breach set each loss by the key's ceiling, and our budget check still fails open (see the risks above). First step: a test that a capped key returns errors after the limit. `0p96nZsRxlY`
2. **Pin upstream providers and log the served endpoint.** Use an allowlist, require supported parameters, set max_tokens explicitly, and record the serving endpoint and any output cap hit on each request. Why: OpenRouter's default routing weights providers by list price, and silent output caps can cut reasoning short. Check whether Scout's strategy router does the same. First step: add served-endpoint and finish-reason fields to the audit row. `ZsnFX5mEJ4s`
3. **Per-binary, per-endpoint, per-method egress rules, with a dry-run check on policy diffs.** Compare Crucible's exec gate with this model. Log every denial with the calling binary. Why: our egress is allow or deny only, and credential injection is still planned. First step: a policy test where one host is allowed for one binary and denied for another. `SbwckhZkPGs`
4. **A/B probe before keeping any self-edited skill or harness rule.** Run each candidate change with and without it on the same tasks, log tokens per run, and require a trigger line on every skill. Why: SkillForge and EvolveCraft currently keep edits by frequency. First step: 20 cases, 3 runs each, with and without one mined skill. `yCgfyQmqhPM`
5. **Check that our own proxy keeps the prompt prefix stable.** Replay a 10-turn session through Govrix and diff the bytes of the prompt prefix on each turn. Log cached and uncached input tokens per request. Why: a changing value near the top of the prompt, or edits to earlier history such as stripping thinking tokens, turns every later turn into a full cache miss. PII redaction could have the same effect; this is untested. First step: the replay diff, run before any L4 latency claims. `x_qmqqp6d7s`
6. **Cost per completed task, weighted by cache-hit pricing.** Track cached, uncached and output tokens per request, then divide cost by tasks that pass. Why: budgets and routing in Govrix should use the real token mix, not list price or decode speed. First step: add the three token counts to the cost accounting. `zIWxzkO1nak`, `P0i3vYuJZH8`
7. **A fixed-task regression tracker.** Keep a set of fixed questions, take several samples per question, and log output tokens, tool calls and model version. Why: it separates a model change from a config change, which fits the telemetry layer. First step: 30 fixed questions, 4 samples each, stored per release. `SxLUx8-hN1o`
8. **Treat model-written memory as untrusted input.** Before any self-editing memory in MemoryMesh, benchmark the cache-hit rate after an early-context edit. Scan memory writes for instruction-like text, since such text can persist across turns. Why: tiered memory is the closest match. First step: a memory-write scanner with a test set. `9-iiHFQyzuM`

### Claims to treat with caution

- **Breach details (`0p96nZsRxlY`).** The attack path was unconfirmed when the video was made. Victim losses come from posts the speaker read. Treat the timeline as a secondary account.
- **OpenRouter routing (`ZsnFX5mEJ4s`).** The fee, weighting and key names come from one talk. Check them against the provider's docs before coding.
- **OpenShell (`SbwckhZkPGs`).** This is one 8-minute review by Better Stack. Its usage numbers are self-reported by the vendor, and the project is early (0.x). Its caveats (telemetry, macOS setup, creation failures) are worth checking first.
- **Harness gains (`yCgfyQmqhPM`).** The +11.5 gain starts from an empty harness and uses a frontier editor. Self-editing gained about +4. Cost runs 8x to 40x a plain run. Several figures were read off charts. The repo is a research release with no merged PRs at recording.
- **Context-as-file (`9-iiHFQyzuM`).** Accuracy gains are small in absolute terms. The paper was relayed, not checked. The cache-miss time comes from a local 3090 example, and the cache-miss cost comes from paid API prices.
- **Mac and local serving (`x_qmqqp6d7s`).** This is one developer's report and a speaker's reading of logs. Ollama's context tiers and the Claude Code fix are speaker claims.
- **Silent model switching (`SxLUx8-hN1o`).** This rests on one talk. The config key was not named, and the usage tool name is unverified.
- **Prices and hit rates (`zIWxzkO1nak`, `P0i3vYuJZH8`).** These are one video's snapshot of Oct 2026 pricing. Recheck before using them in any routing rule.

## Reading list (top 10 for this project)

1. `rbjWzZK2LU0` - budgets as refilling write limits, proxy-stamped identity. Directly attacks our fail-open budget.
2. `0vphxNt4wyk` - the cleanest recipe for a skill-worthiness eval.
3. `vy7o1g2iHY8` - a skill that dropped success from 97% to 77%; paired evals found it.
4. `iqloyWCGYQQ` - how to test whether memory helps, with a cost axis.
5. `3z2uT5aDx_Y` - judge calibration and simulated users, from a production team.
6. `sOB3HSiG8vo` - retry budgets, outlier weights and routing for our scheduler and router.
7. `BInpv7lGp1o` - ordered commit, receipts and scoped approvals for budget and audit state.
8. `DqtmZE6Hl0g` - deterministic simulation with legal stale reads, for the distributed-systems thesis.
9. `MkRYPFIMCSA` - egress proxy with credential injection and rule fixtures.
10. `YXowceUKYJI` - session-aware KV routing and cache metrics for InferCraft.

Caveat. These notes come from talk summaries. Many numbers are speaker claims, not independent results. The skill-gate and memory-benefit points are the best supported. The routing and quantization points are directional, since most talks assume multi-node hardware.
