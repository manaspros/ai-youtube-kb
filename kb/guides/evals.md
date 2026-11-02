# Guide: evals

*Synthesized by Sonnet from 219 talks since 2026-05-18.*

## State of the art (what practitioners actually do now — most recent talks weigh most)

The loop is now stable across vendors. Trace the agent. Read the traces by hand. Name the failure modes. Write one small evaluator per failure mode. Turn failing traces into a dataset. Change one thing. Re-run. Gate release on the result. Arize, Langfuse, Braintrust and W&B all teach this same loop in September and October 2026 (`SHMCGrNJJGc`, `obfPzbapMIM`, `hfEczxdNyvU`, `BOCjybvJYM4`, `XyV6bSMyq-I`).

Key practices:

- **Evals sit on traces, not on final strings.** A trace is a tree of spans. Code checks grade the output, not the path the agent took (`Xfl50508LZM`, `_zUp6y9bDU8`).
- **Error analysis comes first.** Teams read 10-20% of traces, write free-text notes, then cluster the notes into failure modes. Often an LLM does the clustering (`obfPzbapMIM`, `SHMCGrNJJGc`, `yqF6XhzbWBk`).
- **Judges are binary and narrow.** One yes/no question per failure mode. No 1-10 scores (`-aM2EDTiaMs`, `eAXxdtNlK04`, `hfEczxdNyvU`, `3z2uT5aDx_Y`).
- **Judges are treated as classifiers.** You hand-label a set, split train/dev/test, and report agreement or precision and recall before you trust the judge (`NdrSPm6NCdk`, `3z2uT5aDx_Y`, `McknwOzbmyg`, `SHMCGrNJJGc`).
- **Evals gate CI.** A prompt promotion or skill change triggers an experiment on a fixed dataset, with per-evaluator thresholds (`obfPzbapMIM`, `0vphxNt4wyk`, `NdrSPm6NCdk`).
- **Production feeds the eval set.** Real traffic and real customer signals replace imagined test cases (`Emo5FGGY-wM`, `aHhB3sjGjkI`, `Ib5t2RLtxvM`).
- **Coding agents now run the eval loop.** They pull failing spans, draft evaluators, and propose fixes. Humans keep the goals and the gate (`_zUp6y9bDU8`, `TeErpYBUIeM`, `aHhB3sjGjkI`).
- **Agent benchmarks are environments.** Each task is an instruction, a sandbox and a verifier, run as parallel rollouts. The same unit serves as eval, training data and RL environment (`jRCpXUjz4CI`, `V-EDrhIhHzQ`, `Ib5t2RLtxvM`).
- **Public leaderboards only orient.** Teams build a private, held-out eval from their own work (`Ib5t2RLtxvM`, `q4Tr-DknG2M`, `QuuIywMG4s8`, `hqHC6Z_lXyo`).

## Consensus patterns (numbered; each cites videos as `video_id`)

1. **Read traces before writing any eval.** Open coding first, then group into root causes. Rank by severity times frequency. (`SHMCGrNJJGc`, `qZj7sqmidqA`, `Xfl50508LZM`)
2. **Prefer deterministic checks; use an LLM judge only where code cannot decide.** Regex, JSON parse, DB state and test suites come first. (`A48uhxfxbsM`, `_zUp6y9bDU8`, `HEFSExa0xl0`, `T3SS931wU0I`, `0vphxNt4wyk`)
3. **Make judges binary, with a rubric from your own error analysis.** Give observable yes/no criteria, examples, and a request for reasoning before the label. (`qZj7sqmidqA`, `SHMCGrNJJGc`, `hfEczxdNyvU`, `eAXxdtNlK04`)
4. **Calibrate the judge against human labels.** Targets seen: about 30 labels with 80-85% agreement, or about 100 labels split three ways. 100% agreement is a smell. (`NdrSPm6NCdk`, `3z2uT5aDx_Y`)
5. **Give the judge the same context the agent had.** A correctness judge fails on fresh data because it uses its own stale knowledge. A faithfulness judge works. (`SHMCGrNJJGc`, `qZj7sqmidqA`, `Xfl50508LZM`)
6. **Know the judge biases and probe for them.** Position, sycophancy, self-preference and verbosity. Use a stronger judge from a different family. Swap option order. (`NdrSPm6NCdk`, `SHMCGrNJJGc`)
7. **Triage the judge before you triage the agent.** When a score moves, test the judge on contrasting cases first. (`YXEqC05WEI0`, `xLxhT2ZI7UM`)
8. **Simulate users, but make the simulator realistic.** Polite simulators inflate scores. Fine-tune on real messages and add impatient personas. (`3z2uT5aDx_Y`, `McknwOzbmyg`, `Ib5t2RLtxvM`, `XyV6bSMyq-I`)
9. **Turn production failures into regression tasks.** Log prod and offline traces in one format. Keep one agent code path for both. (`XyV6bSMyq-I`, `Ib5t2RLtxvM`, `Emo5FGGY-wM`, `31GUkCBD-Uc`)
10. **Test skills and prompts with and without the change.** Keep a skill only if the pass rate goes up. Also test triggering, with negative cases. (`0vphxNt4wyk`, `GmAQKINjv1E`, `vy7o1g2iHY8`, `k2ClBT4aqAg`)
11. **Protect the eval from the optimizer.** In auto-improvement loops, the agent may not edit the golden set or scorers. Keep a hidden test split. (`aHhB3sjGjkI`, `eAXxdtNlK04`, `7RFJRDYroic`)
12. **Defend the benchmark against cheating.** Strip git history, restrict network, check trajectories, use time-split or original tasks, and audit with replay or data-withheld runs. (`wcUJWP6WpGM`, `Yk87oUPVaxU`, `q4Tr-DknG2M`, `CTLa_p6iOiY`, `mMNkdYnIVC4`)
13. **Report spread, cost and consistency, not one average.** Run at least five trials. Show best, worst, the always-solved floor, and cost. (`YIxzNZDDy1A`, `CTLa_p6iOiY`, `hqHC6Z_lXyo`)
14. **Monitor production with narrow signals, not only offline evals.** Binary classifiers, regex and sampled online judges. Use control groups for rollouts. (`-aM2EDTiaMs`, `hfEczxdNyvU`, `rTojoVotlD8`, `BOCjybvJYM4`)
15. **Verification is the foundation for trusting agents.** Status comes from records and hashes, not from model prose. (`q4WC4TowkBo`, `vy7o1g2iHY8`, `dYh7TQkuYFE`)

## Disagreements & open questions

- **Evals versus monitoring.** Raindrop argues production monitoring should replace evals as the main safety net (`-aM2EDTiaMs`). Lyft, Uber and Ufonia still gate launch on offline simulation or offline golden sets (`3z2uT5aDx_Y`, `31GUkCBD-Uc`, `McknwOzbmyg`). Langfuse says the entry point depends on stakes (`obfPzbapMIM`).
- **LLM judge versus deterministic evaluator.** Pydantic prefers custom code over judge (`A48uhxfxbsM`). Abridge and Composo argue judges are needed when valid answers vary, but they must be rubric-based or retrieval-based (`u6q-byPWUuo`, `yqF6XhzbWBk`).
- **Pointwise versus pairwise.** IBM says pointwise is more reliable (`NdrSPm6NCdk`). Character.ai and Arena train and score on pairwise comparisons (`b_PmGocP4rc`, `R7A8rX-09Zw`).
- **Can auto-research build the eval?** Browserbase's loop rebuilt a verifier in a day but reached about 70% of the human-tuned agreement (`xLxhT2ZI7UM`). Weco says eval design is the most important step and agents reward-hack it (`7RFJRDYroic`). Langfuse warns against fully automated fix loops in high-stakes areas (`obfPzbapMIM`).
- **Rubric versus simple reward in RL.** Snorkel found a simple binary reward beat an engineered rubric (`TyPpSRXGhbc`). Abridge and LatchBio use rubrics for long-horizon work (`u6q-byPWUuo`, `3ZMUiFaQ3qg`).
- **Where does the standard live?** Composo says keep "which error matters" as retrieved expert examples, not in the prompt or weights (`yqF6XhzbWBk`). Others bake it into a clinician-written cost matrix that drives the optimizer (`McknwOzbmyg`).
- **Does automation bias corrupt human labels?** Duolingo found skilled reviewers accepted half of fake AI flags (`CDqzWpwkSls`). Few other talks test for this.
- **Open:** how to evaluate long-horizon, stateful and continual-learning agents. Berkeley found plain in-context learning topped the reward and Pareto ranking (`iqloyWCGYQQ`). Others use controlled scenarios with ground truth (`x4e5O9zN0TE`).
- **Open:** how to measure "automated". Due diligence talks say grader scores can be far too optimistic (`gDRCpTMCqEU`).

## How thinking changed over time (dated)

- **May 2026.** Talks center on golden sets and prompt search. GEPA lifts an extraction prompt from about 87% to 96.7% (`A48uhxfxbsM`). Arize and Incident teach trace-first evals and agent-friendly eval CLIs (`Xfl50508LZM`, `L2r6vLlLgs8`). Raindrop pushes monitoring over evals (`-aM2EDTiaMs`). Arena shows leaderboards hide gaps (`R7A8rX-09Zw`).
- **June 2026.** The focus shifts to trust in public numbers. Cline says to use evals but also vibe-check (`QuuIywMG4s8`). Pruna says leaderboards are statistically thin (`hqHC6Z_lXyo`). Nebius and Snorkel stress task and verifier quality and infra noise (`wcUJWP6WpGM`, `YYH0DMQr30A`). Skills start to get measured with and without (`vy7o1g2iHY8`).
- **July 2026.** Evals become optimizer targets. Auto-agent loops run on branches with rollback (`aHhB3sjGjkI`). DeepMind says do not ship skills without evals (`0vphxNt4wyk`). Cursor stresses private held-out evals and hygiene (`q4Tr-DknG2M`). IRT audits benchmarks (`O3FEoMYvUf8`). Duolingo shows human review can be an eval weakness (`CDqzWpwkSls`).
- **August 2026.** Simulation and judge calibration take over. Lyft finds polite simulators and calibrates judges (`3z2uT5aDx_Y`). Uber builds closed-loop evals with human labels (`31GUkCBD-Uc`). Harbor and Snorkel present environment-as-directory and trace-to-task (`jRCpXUjz4CI`, `Ib5t2RLtxvM`). Replay agents show static benchmarks are gameable (`CTLa_p6iOiY`). Datacurve writes original tasks against contamination (`Yk87oUPVaxU`).
- **September 2026.** Domain-expert judges and safety cases. Abridge, Composo and Ufonia build clinician-calibrated judges (`u6q-byPWUuo`, `yqF6XhzbWBk`, `McknwOzbmyg`). Hinge says verify the judge first (`YXEqC05WEI0`). The IFScale rerun shows an old benchmark ceiling moved about 10x (`XzJD1bvXKjs`). Maersk replays real cases with writes off (`dQ-_i1tZiws`).
- **October 2026.** Consolidation and tooling. Judges are named as "confident liars" and rebuilt with rubrics and evidence (`xLxhT2ZI7UM`). Platform workshops all teach the same loop and let coding agents run it (`hfEczxdNyvU`, `_zUp6y9bDU8`, `SHMCGrNJJGc`, `obfPzbapMIM`). Benchmarks start reporting variance, cost and consistency (`YIxzNZDDy1A`). Verification and receipts become the theme for coding agents (`q4WC4TowkBo`).

## Numbers worth remembering (with `video_id`)

- Judge calibration: about 30 hand labels, 80-85% agreement target, human-human agreement about 80% (`NdrSPm6NCdk`). Lyft uses about 100 labels split three ways (`3z2uT5aDx_Y`). Ufonia judge F1 0.96 on 240 examples from 10 clinicians (`McknwOzbmyg`).
- A built-in correctness judge passed 0 of 13 reports because of stale knowledge. Faithfulness found about half unfaithful (`qZj7sqmidqA`). In the later run, 14 of 16 were flagged unfaithful (`SHMCGrNJJGc`).
- A web-agent judge said 74% success; the rubric verifier said 38%. Verifier-human kappa was 0.58 (`xLxhT2ZI7UM`).
- First simulated eval at Lyft read 90%+, judged too good to be true (`3z2uT5aDx_Y`).
- Rollout-only 95% confidence intervals cover the true score only about 17-20% of the time. A replay script under 1 MB matched frontier models on OSWorld (`CTLa_p6iOiY`).
- GEPA: one reflection round on 3 examples gave about 2x GRPO's gain, which used 25,000 rollouts (`OA-Mc60Rboo`). Prompt accuracy 87% to 96.7% (`A48uhxfxbsM`).
- Auto-agent loop took a toy agent from 18% to 83% in about 10 iterations (`aHhB3sjGjkI`).
- Skills: about 15% average gain across SkillsBench tasks; almost none of about 50,000 indexed skills had evals; keep SKILL.md under about 500 lines (`0vphxNt4wyk`).
- Snorkel: high-quality tasks gave about +6% RL uplift versus +1% for low quality (`YYH0DMQr30A`).
- IRT kept 99% rank correlation using about 97 of 484 items (`O3FEoMYvUf8`).
- Terminal-Bench 2.0 has 89 tasks; run five trials per configuration (`YIxzNZDDy1A`). Cline's harness started near 43% before infra fixes (`QuuIywMG4s8`).
- Vector search cost about 4x agentic search at equal accuracy on about 20 bug tasks (`T3SS931wU0I`).
- Perceived reliability cliff: about 80% feels untrustworthy, about 92% lets customers hand over a workflow (speaker claim) (`Emo5FGGY-wM`).
- A ceiling test: production agreed with itself about 93% over three runs, so judge a cheaper model against that (`8g1N_a3h9H0`).
- Frustration rate fell 37% to 9% after a prompt change, seen via classifier signals (`-aM2EDTiaMs`). Running an LLM judge on every output roughly doubles spend (`-aM2EDTiaMs`).
- Automated grader versus merge decisions had a 24-point gap in one study (`gDRCpTMCqEU`).
- Long-session eval: seed 10 turns, test the 11th (`esY99nYXxR4`).
- SWE-rebench: about 30 models per month; the reference time-split keeps tasks fresh (`wcUJWP6WpGM`).

## From creator channels (Kai Explains, AI LABS, Better Stack)

Basis: 62 creator videos in the evals category. Most are single-run hands-on tests, news recaps or relayed interviews. Few describe a method in full. Numbers below are one creator's unless a note says otherwise.

### Practical playbook

1. Write the eval before you build. A fixed pass/fail check that can say no beats "see if it looks better." (`pGro_uKt-_M`, 4:21. Single creator relaying an interview.)
2. Expect evals to expire. The creator says checks last two or three model generations. When everything passes, rewrite them around current failures. (`pGro_uKt-_M`, 7:07. Same source.)
3. Pin the harness, then attribute failures. Use the same harness, skills, plugins and MCP servers for every model. Hold weights and prompt fixed, and swap only the harness before blaming the model. Rerun the losing side with the same config, because one hidden enabled skill reversed a result. (`y8JWZQpWbxQ`, 1:07; `3DVRznjCIS8`, 0:00.) Count a failure as a model failure only when other models pass the same task. (`v-xnHMwLgAw`, 3:50.)
4. Re-run numbers that look too good. One creator found a 694,630 tok/s prefill figure that came from two harness copies warming each other's cache. Check for a truncation bug before reading a long-context cliff as model behavior. (`GweZqgLxcCo`, 7:56.)
5. Plant canary tokens and score the marker list. Ask the agent for the markers, ignore its prose, and compare with an answer key. Check whether a high score came through a side path your pipeline cannot use. (`OlNZCtk100Q`, 0:00 and 2:13. One run; Kimi 2.5 scored 13/20.)
6. Compute exact truth on your own slice. Run brute-force top-K over exactly the vectors you loaded. Store deep neighbors once and truncate for smaller k. Compare engines at matched recall, not at one setting. (`6Uj6GXIpX9s`, 4:33 and 6:58.)
7. Check for shortcut solutions. Count runs whose tool calls fetched the upstream fix. Re-run in a strict environment: fresh git history, network denied, allowlisted package proxy. These figures are Cursor's research as relayed, not checked. (`pHAbwL7w83Q`, 0:58 and 1:48.)
8. Test memorization with an original-vs-altered quiz. Show the model a real benchmark item and an altered one, then ask which is original. Consistent picks of the real item suggest memorization. The video gives the method only, no results. (`pHAbwL7w83Q`, 2:58.)
9. Use a referee, and report per question. With no human labels, a strong model can referee unlabeled items. One aggregate hid a 49% score on tone, so report agreement per question. Agreement with a model is a proxy, not correctness. (`Uihz1NkhFM0`, 2:22 and 4:28.)
10. Blind the judge and log cost drivers. Hide which model made each output, score separate dimensions, and track output tokens and tool calls. This AI LABS test reports 86 vs 84 without saying which model got which score, so treat it as weak evidence. The segment includes a sponsor ad. (`BwNNcob3-A0`, 0:00 and 1:09.)
11. Judge cost per finished task, not per token. In a single run per model, the cheaper-per-token model cost $4.50 against $27.86, because the other wrote about six times more output. (`Zc72O98x3nk`, 3:10.)
12. Probe premise override and pushback. Change one fact in a famous riddle, then push back on correct answers over several turns. Score whether the model answers from the stated fact and keeps a sound position. Plain riddles saturated at 39/39 for all three models. (`GweZqgLxcCo`, 2:39, 4:04 and 6:42.)
13. Log config drift next to every score. Record effort setting, output tokens, tool calls and app version. In one test a 4.2-point score move came with a 26% drop in output tokens. (`SxLUx8-hN1o`, 2:36. Single creator; not independently replicated.)
14. Calibrate confidence on your own labels. Bin predictions, compare accuracy per bin, and fit a temperature on held-out data. For order bias, run a flip test: swap option order and count changed answers. One 500-headline run flipped 20 answers on raw Qwen3 8B and none after debiasing. (`Oi4JPj58lUA`, 8:41; `hJz7zi17mXA`.)
15. Diff quantized output against full precision. Run fixed greedy prompts on the full model and the quant, then compare. Throughput and error logs cannot show silent drift. Keep the KV cache at Q8 or higher. (`hg26j0erUSo`, 0:00 and 8:29. Single creator.)
16. Count runaway generations separately. In one community test a quant scored about 6, with 92% of generations in a repetition loop. Fix the sampler before judging the model. (`Wik_JQ-enUA`, 4:08 and 5:20.)

### Tools creators recommend (tool — what for — `video_id`)

- Agent Reading Test (agentreadingtest.com) — canary-token check that an agent's web fetch reads full pages — `OlNZCtk100Q`
- Qdrant FineWeb 10B dataset (Hugging Face) — exact nearest-neighbor truth for vector search tests; recompute truth for any subset — `6Uj6GXIpX9s`
- OpenCode — one fixed harness for model-vs-model runs — `nzAT09XolYw`
- LM Studio + Cline — fully local test; disable the internet to confirm — `ZxQ2DuejRhU`
- Claude Code `usage` and `context` commands, plus Anthropic's `doctor` audit — measure setup cost and review proposed changes one by one (invocation not shown) — `pGro_uKt-_M`
- MindWalk — LLM judge over a whole agent session, findings linked to timestamps — `Y_7_rbtQXcs`
- Cloudflare Clef (open weights) and TypeSafe Jev (hosted) — probability-output classifiers for triage; Clef accepts images — `Uihz1NkhFM0`
- Lean 4 build plus a `sorry` grep — check that a formal proof has no gaps; audit the statement separately — `WEwZfkUzBxY`

### Where creators agree or clash with the conference talks

- Agree: benchmarks mislead, and the fix is your own evals. Creators repeat the guide's cheating fixes (no git history, no network) in `pHAbwL7w83Q`, and the exact-truth test in `6Uj6GXIpX9s` is in the same spirit.
- Agree: evals need a fixed definition of done and an expiry check (`pGro_uKt-_M`).
- Clash on trials: the guide asks for at least five trials per cell. Most creator comparisons run each model once (`Zc72O98x3nk`, `J8-CdK4215Y`). Single runs are the weakest part of this set.
- Clash on judges: the guide wants judges calibrated against human labels. Creator referee tests (`Uihz1NkhFM0`, `BwNNcob3-A0`) use a strong model as judge with no human labels.
- Not in the guide's consensus list: harness attribution (`3DVRznjCIS8`, `y0BW4hpMpyM`), config drift (`SxLUx8-hN1o`), and cost per finished task (`Zc72O98x3nk`). These are creator-only angles, and most rest on one video each.

### Watch first (5 `video_id` — why)

- `pGro_uKt-_M` — evals written before building, and why they expire after a few model generations. Sponsored segment in the middle.
- `OlNZCtk100Q` — a concrete canary test, and how agent self-reports inflate scores.
- `6Uj6GXIpX9s` — exact ground truth, recall at matched latency, and why published truth does not transfer to a subset.
- `pHAbwL7w83Q` — shortcut and contamination probes. Numbers are secondhand, but the test designs are clear.
- `Uihz1NkhFM0` — per-question referee agreement, and why an aggregate score hides a failing question.

## Watch first (5-8 best videos: `video_id` — why)

- `SHMCGrNJJGc` — a recent full workshop (dated 2026-10-17). Covers trace, code eval, faithfulness judge, five-part judge prompt, human-label validation, CI gate.
- `NdrSPm6NCdk` — clearest judge-calibration loop, with named biases and a CI agreement gate.
- `xLxhT2ZI7UM` — shows how wrong a standard judge can be, and a rubric-plus-evidence fix.
- `3z2uT5aDx_Y` — simulation evals done honestly: polite simulators, binary rubrics, judges as classifiers.
- `CTLa_p6iOiY` — why static benchmarks lie, and how to get honest confidence intervals.
- `obfPzbapMIM` — error analysis with experts, mixed evaluators, CI gate on prompt promotion.
- `Ib5t2RLtxvM` — turn production traces into containerized, oracle-validated tasks.
- `0vphxNt4wyk` — a lean harness for testing skills: triggers, regex asserts, with/without ablation.

## Implications for our projects (use the profile; concrete, cite `video_id`)

**AgentOS, MemoryMesh and RAGAS.**
- Add a hybrid-retrieval regression set. Mine bug or question sets from real use, score by deterministic checks, and compare variants per row (`T3SS931wU0I`, `r9OwPx_HoV0`, `gonAewBZxfU`).
- Treat the judge as a classifier. Hand-label about 100 items, keep a dev/test split, and report agreement before trusting any RAGAS score (`3z2uT5aDx_Y`, `NdrSPm6NCdk`).
- For memory, use paired stateful versus stateless runs and a concept-drift injection, to test conflict resolution (`iqloyWCGYQQ`). Add a long-session test: seed 10 turns, probe the 11th (`esY99nYXxR4`).

**InferCraft (vLLM, KV cache, quantization).**
- Test each quantization or KV strategy with KL divergence against the unquantized model, plus a run inside a real agent harness (`J4_jCrTxMkk`).
- Sweep concurrency to find the knee, and report tail latency, not the mean (`4n08JHb90hI`).
- Report variance across at least five trials and cost, not one number (`YIxzNZDDy1A`).

**Crucible (sandboxes).**
- Reuse the environment-as-directory format: instruction, sandbox, verifier. Add history scrubbing and a network allowlist (`jRCpXUjz4CI`, `q4Tr-DknG2M`, `Yk87oUPVaxU`).
- Validate each task with an oracle solution first (`Ib5t2RLtxvM`).

**SkillForge and EvolveCraft.**
- The open "success signal" question has partial answers. Use with/without-skill pass rate, trigger and negative cases, and a CI gate on skill diffs (`0vphxNt4wyk`, `GmAQKINjv1E`, `vy7o1g2iHY8`).
- For skill mining, use a stuck-to-unstuck signal and blank-injection holdouts (`KA5kPbdkK2E`).
- For self-improvement, copy the protected-eval loop: branch per hypothesis, rollback, golden set off-limits to the optimizer, hidden test split (`aHhB3sjGjkI`, `eAXxdtNlK04`, `7RFJRDYroic`).
- Optimize prompts with GEPA-style reflection and a Pareto pool (`OA-Mc60Rboo`, `A48uhxfxbsM`).

**Next-phase thesis: benchmarks and correctness checks.**
- Use a ceiling test (the system against itself) to set the noise floor before comparing variants (`8g1N_a3h9H0`).
- Use hierarchical confidence intervals when variants differ in tasks and runs (`CTLa_p6iOiY`).

- Tag every call with feature, user, model and endpoint (`rTojoVotlD8`). Track p95 time to first audio or token, not medians (`vblnYHzBgS4`).
- Replay real traffic with writes disabled as a regression check on gateway changes (`dQ-_i1tZiws`).

- Write retrospective evals from real outcomes and plot quality against tokens. Treat a stale graph as an eval regression (`k2ClBT4aqAg`).

**ProsHarness.**
- Add receipts and gates in code. Store a hash of the real test output, and block stale proofs (`vy7o1g2iHY8`, `q4WC4TowkBo`).
- Use independent reviewers with a source-anchored adjudicator for the plan, critique and debate steps. Never accept "done" without a check the sender runs (`dYh7TQkuYFE`).
- Plan review before code review keeps PR review short (`Ib5GBkD555M`).

**Entity resolution and Haiku pipelines.**
- Use two cheap models from different families, send only disagreements to a stronger model, and sample the agreed set. Fix the question definition, not the threshold (`Fa3hQVIKShw`).
- Right-size the model: write the golden set, test small to large, and pick the smallest that passes (`fWXJM-J0ZB8`, `Ti-BmGU1_mQ`).
- Compress prompts with an optimizer and check against the ceiling (`8g1N_a3h9H0`).
- Seed an eval set from the real job before building (`DrTdD-ttjCY`), and mine failure modes from production outputs instead of synthetic cases (`yqF6XhzbWBk`).
