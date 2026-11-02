# Guide: token-cost-efficiency

*Synthesized 2026-11-02 by Haiku from 243 videos. Open a video: `kb/videos/<id>.md`.*

Source note: this guide rests on the 45 detailed entries in the category notes. Most are Kai Explains reviews. The rest are AI Engineer talks. Most numbers are speaker or vendor claims, not independent measurements.

## State of the art (what practitioners actually do now — most recent talks weigh most)

- **Cost per task, not per-token price.** A cheaper list-price model can cost more per task. Vals AI reports Opus 5.5 listing at $4 in and $20 out, yet costing about 14% more per task than a $10/$50 model on one benchmark (`rWtbOgl5FTU`, AI Engineer talk).
- **Cache reads dominate agent bills.** One SemiAnalysis month cited by Kai puts 96.6% of agent tokens in cache reads (`P0i3vYuJZH8`). Cache misses cost far more than hits on DeepSeek's API (`RlRC_6hbBHc`, `zIWxzkO1nak`).
- **Prompt stability is a cost lever.** An edit near the start of a context invalidates the cached suffix. One Meta/UW test saw such an edit cost 7.7x a normal turn (`9-iiHFQyzuM`). A cache miss made one Mac agent about 44x slower to first word, with about 41k tokens reread (6.1 s on a hit, 268 s on a miss). One cause was a changing token at the top of Claude Code's system prompt (`x_qmqqp6d7s`).
- **Local speed is mostly prefill.** Decode tokens/s is the number people quote. Time to first token on a 30k-token agent prompt can run minutes on consumer hardware (`1--PzaHafAU`, `uavLRbbfM94`). A 16GB-card run fell from 45.6 to about 15 tok/s after 20 minutes of agent work (`i9mRnbdDYxk`).
- **Less tool context.** Arize's code-mode approach (search for a tool, then run code) cut tokens 43% and cost 31% in its own Harbor evals (`dAoOYFx7ZYw`). Jellyfish's Ve2bAarPA2I finds the team and process matter more than the model (single vendor dataset).
- **Effort is a cost dial.** Kai reports that medium effort cut output tokens 26% and kept the score under the tracker's detection threshold (`SxLUx8-hN1o`). Reasoning effort is the largest cost lever in the Qwen tests (`LqAxNIalgOw`).
- **Self-hosting pays only at high utilization.** Revolut cut its coding-AI invoice to about a tenth by self-hosting GLM, a vendor-invoice comparison rather than a per-task one. Serving tuning then raised throughput on the same GPUs (`Ok6QdZHCcI8`). imec's threshold check says self-hosting wins only above a GPU utilization level set by hardware tier (`9-Y_oS9OBLc`).

## Consensus patterns (numbered; each cites videos as `video_id`)

1. **Measure cost per task or per merged PR, with a value metric.** `dSg0pu8d6qg`, `U7ZYBCcdJPg`, `rWtbOgl5FTU`.
2. **Log cache hits and misses per turn.** Zero cache tokens deep into a session is the red flag (`x_qmqqp6d7s`). Track cached and uncached input separately (`RlRC_6hbBHc`, `zIWxzkO1nak`).
3. **Keep the prompt prefix stable.** Append new content. Do not edit early context (`9-iiHFQyzuM`, `x_qmqqp6d7s`, `zIWxzkO1nak`).
4. **Set effort on purpose, not at max by default.** Use low or medium for simple work, and high for hard, multi-step work (`SxLUx8-hN1o`, `h_KqS4GtU3I`).
5. **Split keys and speed tiers by workload.** Issue per-team keys. Send interactive calls to fast capacity and background jobs to cheap capacity (`Ti-BmGU1_mQ`, single vendor talk).
6. **Route cheap first, escalate on demonstrated failure.** Escalate only when the cheaper model fails in a way that changes the output (`P0i3vYuJZH8`). Use a cheap model with a rewritten question (`Fa3hQVIKShw`). Reserve the frontier model for heavy reasoning (`8g1N_a3h9H0`).
7. **Prefer search-then-execute over large tool catalogs.** `dAoOYFx7ZYw`, and `aGIUg8zKI8A` (tool search plus CLI wrappers instead of loading every MCP schema).
8. **Pin providers and log which endpoint served each request.** `ZsnFX5mEJ4s`.
9. **Budget VRAM and KV cache before loading a model.** Weights plus KV bytes per token times context, plus runtime headroom (`i9mRnbdDYxk`, `6tihP50zlcE`).
10. **Eval before downsizing.** Test cheaper models on your own cases first (`8g1N_a3h9H0`, `Ti-BmGU1_mQ`, `rWtbOgl5FTU`).
11. **Compare hardware on cost per task, with a break-even formula.** `L4UV6b2Xc64`, `3hMEcJCGne0`, `eckOsa0kBkY`.

## Disagreements & open questions

- **Own the hardware or rent tokens?** Revolut's result (`Ok6QdZHCcI8`) is a high-utilization case. Kai's single-user break-even math (`L4UV6b2Xc64`, `3hMEcJCGne0`, `Y226-wwfCSw`) is a low-utilization case. The gap is mostly utilization. Treat the local-hardware price claims as time-sensitive.
- **Is effort a capability cut?** `SxLUx8-hN1o` says effort is mostly a how-much-work dial. `h_KqS4GtU3I` says xhigh matters for hard tasks. Both can hold: the answer depends on the task.
- **Does the harness still matter?** `7Y4sbZgBdnc` says yes, for runtime and cost. `Ve2bAarPA2I` finds tool and model switches explain under 1% of output variance. Results differ by task type and measure.
- **Context management.** `9-iiHFQyzuM` reports small absolute gains from its CLM technique. It reports larger gains in compute. Single paper, single creator. The summary-failure evidence is one anecdote.
- **Quantization quality.** Headline retention in `P1K36q76Uzk` is near 98%. On agentic benchmarks Kai reports about 75%. Compare against the build you actually run.
- **Coverage gap.** This category file has no AI LABS or Better Stack videos. Creator coverage here is Kai Explains only, plus AI Engineer talks.

## How thinking changed over time (dated)

- **2026-09-18:** Measuring the token bill is not enough. Measure value and review capacity (`dSg0pu8d6qg`).
- **2026-10-02:** Local-hardware math moves from list price to resale, bandwidth per dollar and break-even (`L4UV6b2Xc64`, `3R7yba577uA`).
- **2026-10-12:** "Nerfed" models are mostly config, routing and default changes, not weight changes (`SxLUx8-hN1o`, `ZsnFX5mEJ4s`).
- **2026-10-13 to 10-17:** Cheap model tiers, per-key tracking and planner-worker splits become the default cost playbook (`Fa3hQVIKShw`, `Ti-BmGU1_mQ`).
- **2026-10-19:** Hardware prices rose while hosted open-weight tokens got cheaper. Buying for token savings now rarely pays (`Y226-wwfCSw`).
- **2026-10-20 to 10-28:** The harness shifts toward runtime and context layers, and toward code mode (`7Y4sbZgBdnc`, `dAoOYFx7ZYw`).
- **2026-10-29 to 10-31:** Subscription allowances and cache economics drive the advice (`P0i3vYuJZH8`, `Ok6QdZHCcI8`).
- **2026-11-01:** A viral "100 tok/s" local result turns out to be prefill, not decode (`mED-boddeWI`).

## Numbers worth remembering (with `video_id`)

- 96.6% of agent tokens are cache reads, per SemiAnalysis data cited by Kai (`P0i3vYuJZH8`).
- A DeepSeek cache miss costs about 50x a hit: about $0.15 vs $0.003 per million input tokens (`RlRC_6hbBHc`).
- An edit at the start of context costs 7.7x a normal turn, and the cache hit rate fell from 73.9% to 29.9% on the next turns (`9-iiHFQyzuM`).
- Code mode: 43% fewer tokens and 31% lower cost in Arize's Harbor evals. Their own result, not independent (`dAoOYFx7ZYw`).
- Medium vs high effort: output tokens down 26%. The score moved less than the tracker's 6.6-point detection threshold (`SxLUx8-hN1o`).
- A 32k-token prompt at 50 tok/s prefill takes about 10 minutes 40 seconds (`1--PzaHafAU`).
- Revolut's 56 GPUs went from about 3 to over 7 requests/s, and time to first token from over 10 s to about 1.6 s (`Ok6QdZHCcI8`).
- AI is about 2.5% of the cost of a merged PR. Salary is about 97.5%. Jellyfish data, August 2026 (`U7ZYBCcdJPg`).
- OpenRouter's default routing favors low price. A $1/M provider is 9x as likely to be chosen as a $3/M one (`ZsnFX5mEJ4s`).
- Next-token agreement with the reference model: 91.2% at 2-bit, 95.1% at 3-bit, 98.5% at 4-bit (`JPHT9AvoPSA`).
- Naive PR review agents cost $3 to $25 per PR. Adding sandbox testing and context brought it to about $3 to $20 (`4UtrRVtUN_g`, vendor data).

## Watch first

- `dAoOYFx7ZYw` — Code mode with search-then-execute. Concrete token and cost numbers, plus open problems. AI Engineer talk.
- `9-iiHFQyzuM` — Context editing and the cache cost of edits. Clear case for stable prefixes.
- `P0i3vYuJZH8` — Cache reads dominate agent cost. Shows how to turn a subscription allowance into per-task cost.
- `x_qmqqp6d7s` — Prefill versus decode, and the cache-breaking defaults that make local agents slow.
- `i9mRnbdDYxk` — KV budget and why a 16GB card runs out of room during real agent sessions.
- `SxLUx8-hN1o` — Effort defaults and output-token cost. Shows why to set effort per task.
- `ZsnFX5mEJ4s` — Provider routing and endpoint pinning. Short and practical.

## Implications for our projects (use the profile; concrete, cite `video_id`)

**AgentOS (L1 gateway, InferCraft, observability):**
- Add cache-hit and cache-miss cost accounting per key, beside the budgets in L1 (`RlRC_6hbBHc`, `Ti-BmGU1_mQ`).
- Pin trusted providers and log the serving endpoint per request (`ZsnFX5mEJ4s`).
- For InferCraft, report prefill tok/s and time to first token at real prompt sizes, not only decode tok/s (`1--PzaHafAU`, `uavLRbbfM94`). Use the KV-budget formula before loading (`i9mRnbdDYxk`). Revolut's prefix-cache target above 90% is a useful benchmark (`Ok6QdZHCcI8`).
- Map speed tiers onto the InferCraft scheduler's background-job priority classes, so batch work runs on cheaper capacity (`Ti-BmGU1_mQ`).


**ProsHarness:**
- Long runs: use a notes-file handoff rather than summary-based compaction (`9-iiHFQyzuM`).
- Plan, critique, debate: give each role its own effort level, and set effort per task (`SxLUx8-hN1o`, `h_KqS4GtU3I`).
- Cheap-model pipelines (Haiku): cross-family disagreement is a cheap audit. Accept agreements, and send disagreements to a stronger model (`Fa3hQVIKShw`).
- Credentials: rotate keys, set provider hard limits and revoke keys at the provider. Keys drained in the OpenCode breach (`0p96nZsRxlY`).

**Context engineering (recurring interest):**
- Search-then-execute tools for large tool sets (`dAoOYFx7ZYw`).
