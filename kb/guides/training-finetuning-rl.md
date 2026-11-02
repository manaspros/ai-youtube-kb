# Guide: training-finetuning-rl

*Synthesized by Sonnet from 74 talks since 2026-05-18.*

## State of the art

**Environments are the unit of work.** In the most recent talks, an environment (task, harness, verifier) serves as eval, RL signal and SFT data source at once. Build the eval first. Training is then a config change. `V-EDrhIhHzQ`, `jRCpXUjz4CI`, `AQv3qRCG6Gw`

**RL with verifiable rewards is the default for agents.** Small models trained with GRPO or similar on narrow tool environments beat much larger generalists. Snorkel's 4B finance agent beat a 235B model for under $500. The gain came from tool discipline, not reasoning. `TNwJ1LMiENk`, `TyPpSRXGhbc`

**Task and verifier quality dominate.** Verified high-quality tasks gave about 5x the RL uplift of low-quality ones. LLM judges used as rewards are risky and need rubrics, evidence and human calibration. `YYH0DMQr30A`, `xLxhT2ZI7UM`, `ewtOo0scUh0`

**Real harnesses are being trained directly.** Teams put a proxy base URL in front of an unmodified harness, record log-probs, and train asynchronously. Environment bugs get learned by the model, so audit the environment first. `V-EDrhIhHzQ`, `k35LeKZEhiE`, `FWMJQDH3iK0`

**Distillation with hints is replacing pure GRPO for continual learning.** The model, or a teacher copy with a hint, supplies a per-token target. No golden answer per task is needed. Production traces are the seed data. `ZTA0GwpAUak`, `zL1kLftVTlo`, `q4Tr-DknG2M`

**Tiny and small models ship through synthetic data plus narrow fine-tuning.** A strong cloud model generates data. A 270M to 4B model is fine-tuned and quantized. Reliability moved from about 46% to 90%+ on fixed function calling. `-TiET_K-E_g`, `hacEQHHhu2Q`, `BKWpYIWvAo4`, `fLUtUkqYHnQ`

**Fine-tune late, and only for stable things.** Several talks warn that fine-tuning locks you to a model and slows fixes. Prompts, skills and retrieval often win first. `4loPnxvWWhg`, `qflLT3SoVbw`

**Infra is its own problem.** Cross-datacenter RL, self-healing clusters, data-pipeline stalls and silent numeric bugs are the real time sinks at scale. `maRzp4kImJ4`, `bRGyYaE0lxI`, `tNAV259UhCM`, `KhYifX22yhE`

## Consensus patterns

1. **Eval, environment and training task are the same object.** Build once, reuse for evals, SFT data, RL and distillation. `V-EDrhIhHzQ`, `AQv3qRCG6Gw`, `jRCpXUjz4CI`
2. **Verifier quality caps RL quality.** Gate tasks on achievability, non-triviality, correctness and environment reliability. Audit for shortcuts by withholding the data. `YYH0DMQr30A`, `mMNkdYnIVC4`, `ZFxh7sqbUZo`
3. **Binary or simple rewards beat engineered rubrics for the RL update.** Use rubrics for diagnosis only. `TyPpSRXGhbc`, `TNwJ1LMiENk`
4. **Hold out private evals and isolate the agent.** Wipe git history, restrict the network, retire saturated evals. Agents cheat on public benchmarks. `q4Tr-DknG2M`, `wcUJWP6WpGM`, `mMNkdYnIVC4`
5. **Specialise small models on one or two tasks.** Accept weaker general ability. Narrow fine-tunes match bigger models and run faster. `hacEQHHhu2Q`, `FWMJQDH3iK0`, `g4SsanB0gMc`, `Owb8g3yDyzo`
6. **Use traces as the training asset.** Log production runs, mine failures, build tasks and SFT sets from them. `CvRngaQZQ3Y`, `FWMJQDH3iK0`, `AQv3qRCG6Gw`, `hd7TOvmyAxU`
7. **Data curation beats scale.** Curate, rephrase selectively, sample many answers per question, and pick teachers by measurement. `_PdK6x7PQNM`, `ewtOo0scUh0`, `KhYifX22yhE`, `xbPriQWXtWM`
8. **Environment flaws become model habits.** Tool failures shortened outputs. Timeouts taught tool spam. Measure failure rates first. `k35LeKZEhiE`
9. **Separate failure types before blaming the model.** Model errors versus infrastructure noise versus unsolvable tasks. `wcUJWP6WpGM`, `YYH0DMQr30A`, `xLxhT2ZI7UM`
10. **Distil an expensive judge or teacher into something cheap.** VLM labels train small detectors. Frontier traces train small agents. Teacher outputs are cached and reused. `dKcTBQzR7jI`, `phchDt63qAA`, `CvRngaQZQ3Y`, `KB41dTlX1Uc`
11. **Quantize with sensitivity awareness and test in the harness.** Keep sensitive layers at higher precision and compare KL against the unquantized model. `J4_jCrTxMkk`

## Disagreements & open questions

- **Fine-tune or not.** Vendors and open-model advocates push post-training on your own harness. LeaseEnd argues skills and prompts on a frontier model are cheaper to maintain. `FWMJQDH3iK0`, `13YZ1EB9hjU`, `4loPnxvWWhg`
- **Weights or text.** GEPA claims reflective text optimization beats GRPO on sample efficiency. This is the speaker's own claim with few examples. `OA-Mc60Rboo`
- **SFT or RL.** One talk says SFT gives most agent gains and RL adds the last points. Others frame RL as the main driver, even in pretraining mixes. `ewtOo0scUh0`, `xbPriQWXtWM`
- **Judges.** Some use LLM judges as rewards. Others show a common judge scoring 74% where a better verifier scored 38%. `AQv3qRCG6Gw`, `xLxhT2ZI7UM`
- **Continual learning is unproven.** Plain in-context learning topped an early benchmark. On-policy self-distillation breaks on long tool-calling runs at large scale. `iqloyWCGYQQ`, `zL1kLftVTlo`
- **Bring-your-own-harness.** It gives realism but loses replay, so GRPO group comparison may not work. `k35LeKZEhiE`
- **Synthetic data wall.** Fixed-dataset methods all saturate, per one survey. `WiqDvX6isc4`
- **Vendor claims are unmeasured.** Several numbers (200x distillation speedups, 20x faster search, GLM near-frontier) lack benchmarks in the talk. `gHs5ZiY80PM`, `iJVxxxHM_Oc`, `9JFGohx4E7U`

## How thinking changed over time

- **May 2026:** Small-model craft and diffusion at scale. Fix doom loops in DPO and RL, not SFT. Fine-tune tiny models below about 500M. Adaptive ML pitched RL for enterprise. `fLUtUkqYHnQ`, `BKWpYIWvAo4`, `X6NShR2ccOg`, `xOP1PM8fwnk`
- **June 2026:** Concrete recipes. A small model beats a giant after RL. Distil frontier teachers with settled-state labels and filtering. Task fidelity is data quality. `TNwJ1LMiENk`, `phchDt63qAA`, `YYH0DMQr30A`
- **July 2026:** Environments as the shared unit. Async RL and interception servers. Eval hacking and textual feedback at Cursor. `V-EDrhIhHzQ`, `q4Tr-DknG2M`
- **August 2026:** Continual learning and on-policy hint distillation arrive. Reward-less RL, replayability and environment fidelity become central. Data quality and synthetic pipelines get heavy attention. `ZTA0GwpAUak`, `zL1kLftVTlo`, `AQv3qRCG6Gw`, `k35LeKZEhiE`, `_PdK6x7PQNM`
- **September 2026:** Backlash and breadth. Fine-tuning called tech debt. Reflection challenges RL. RL applied to search, OCR and robotics. `4loPnxvWWhg`, `OA-Mc60Rboo`, `iJVxxxHM_Oc`, `T72nqdC92PM`, `Sjfz1TqxzEs`
- **October 2026:** Verifier quality and placement. Decide where knowledge lives before fine-tuning. Better verifiers filter SFT data. Replicating the sub-$500 result. `qflLT3SoVbw`, `xLxhT2ZI7UM`, `TyPpSRXGhbc`

## Numbers worth remembering

- 4B RL agent: about 60% vs 51% for the 235B variant on held-out FinQA. About $420 compute plus $40 judge. `TyPpSRXGhbc`
- RL uplift from task quality: about +1% (low) vs about +6% (high). `YYH0DMQr30A`
- Function-calling fine-tune: about 46% to 90%+. FunctionGemma 270M runs about 140 tokens/s decode on a Pixel 7. `-TiET_K-E_g`
- Fine-tuning small models gained about 20-40 points on the team's evals. `BKWpYIWvAo4`
- Gemma E2B text weights about 841 MB at about 2.9 bits per weight. `hacEQHHhu2Q`
- Embedding layer is about 63% of Gemma 3 270M parameters. `fLUtUkqYHnQ`
- Offline hint raised task-complete rate from about 22% to 60%. Online hint raised link formatting from about 15% to 80%. `ZTA0GwpAUak`
- One GEPA reflection round on 3 examples roughly matched 2x GRPO's gain after 25,000 rollouts (speaker claim). `OA-Mc60Rboo`
- Async RL off-policy lag around 16 steps works. A 1,000-step GLM-5 run costs about $50k. `V-EDrhIhHzQ`
- Cross-datacenter sync: about 500 GB full checkpoint vs a target of about 500 MB sparse patch (speaker's target, not measured). `maRzp4kImJ4`
- Judge disagreement: 74% (WebVoyager judge) vs 38% (universal verifier). Kappa 0.58. `xLxhT2ZI7UM`
- Data pipeline: GPU utilization 15% to about 90%. `tNAV259UhCM`
- Zeta2 labeling would need about 1M frontier calls without student sampling. `phchDt63qAA`
- Quantized GLM 5.2 weights fall from about 1.5 TB to about 250 GB. `J4_jCrTxMkk`
- Sub-agent search about 20x faster (2 minutes to about 5 seconds). `iJVxxxHM_Oc`
- Fix loop after dropping fine-tuning: about a week to under an hour. `4loPnxvWWhg`
- Web text share in pretraining: about 85% (GPT-3) to about 15% (MAI Thinking One). `xbPriQWXtWM`
- Environment with 10% tool failure shortened model outputs. `k35LeKZEhiE`

## From creator channels (Kai Explains, AI LABS, Better Stack)

Source set: 15 creator videos (Better Stack, Kai Explains), Nov 2025 to Oct 2026. No AI LABS video is in this set. Most evidence is single-run, single-customer or vendor-reported. Treat numbers as claims until checked.

### Practical playbook

1. Run the environment check before any training run. Install PyTorch, the Hugging Face libraries and DeepSpeed, then run DeepSpeed's environment report (DSReport). If it fails, fix the CUDA mismatch before touching the model or config. `OM-DJuwweE0` (single creator tutorial).
2. Start from a known-good ZeRO stage 2 config copied from the official docs. Change one setting per run and record peak GPU memory. Move to stage 3 only on OOM, and use CPU or NVMe offload last, watching CPU RAM. The video does not show the config keys. `OM-DJuwweE0`
3. Choose fine-tune or retrieval by failure type. Missing facts need retrieval. Tone, rigid structured output, or behavior that would take thousands of in-prompt examples needs fine-tuning. After tuning, check whether reasoning got worse. `YAcIUCjsRnU` (single creator review).
4. Test a narrow distilled model against the big general model. Collect labeled examples for one task, fine-tune a small open model, then compare head to head on F1 or win rate, with latency as a second metric. The one case shown is a legal citation task, and it is a customer anecdote. `YAcIUCjsRnU`
5. Audit rewards for lexical shortcuts. Compare rewarded outputs that contain a candidate word with same-prompt outputs that do not, then check whether the grader scores the two groups differently. Track that word's rate per release, persona and checkpoint. The case is a narrator's summary of OpenAI's post, not a primary source. `RGIrw2G70wE`
6. Filter quirk vocabulary out of any data you generate with an earlier model. This covers synthetic data, RL rollouts and distillation. The video says this step was part of the fix. A system-prompt rule can patch the symptom while you wait. `RGIrw2G70wE`
7. Keep one held-out set out of training for the whole run. Stop or change data when training-set scores rise and the held-out score flattens. The creator's held-out script is one document, one run. `L-6O7R71CCg`
8. Use a closed action set for tool routing. Enumerate the allowed tools and argument values, add an explicit no-call class, and write a fixed held-out prompt set (about 49 prompts in the demo). Compare base, fine-tuned and smaller models on that set. The demo's 27% to 84% jump is one run on a small set. `KQcQ7P78eTI`
9. Run a cheap reasoning distill. Pick about 1,000 curated questions, collect teacher answers, and fine-tune an open base. The S1 claim is under 30 minutes on 16 GPUs. If a small reasoning model stops early, append the word "Wait" at inference (a claim from the S1 story, not reproduced). `gacMZf5rqYA`
10. Check a distilled student for memorization before trusting it. Paraphrase each eval item, keep the answer, and compare accuracy. The cited drop is 6 to 14 points. This matters most when your eval set is public. `gacMZf5rqYA`
11. Track reasoning tokens and answer tokens as separate counters, plus a looping rate. Compare models at the same quantization on the same GPU, using a problem with one verifiable answer. A single prompt is an anecdote, not a rate. `byfjZvrYRH0`
12. Size a local student to VRAM at Q4 quantization. The talk gives about 8.5 GB for 14B and about 17.5 GB for 32B (speaker's figures). `gacMZf5rqYA`

### Tools creators recommend

- DeepSpeed (ZeRO, ZeRO-Infinity) — fit training into limited GPU memory — `OM-DJuwweE0`
- DSReport (DeepSpeed) — check CUDA and compiler setup before training — `OM-DJuwweE0`
- Hugging Face Accelerate — multi-GPU launch later, without rewriting the loop — `OM-DJuwweE0`
- Tinker — hosted fine-tuning platform with LoRA; the model can run its own dataset build — `YAcIUCjsRnU`
- Inkling (Thinking Machines, open weights) — fine-tuning base for narrow tasks, the only Tinker-supported model in the video that takes raw audio — `YAcIUCjsRnU`
- LoRA — trains a small add-on on frozen weights, the usual route for personal fine-tuning — `ZTmZOdB5o0U`, `YAcIUCjsRnU`
- Cactus Compute Needle 3 and its fine-tune platform — closed-set on-device tool dispatcher; the video says the platform costs $19 for three runs (vendor price) — `KQcQ7P78eTI`
- Mini-AGI (toy continual-learning repo, weights not released) — ideas only; not usable yet — `L-6O7R71CCg`
- ThinkingCap (Qwen3.6-27B fine-tune) — a same-base baseline for shorter reasoning; vendor numbers, one demo — `byfjZvrYRH0`
- Sky-T1 and S1 recipes — cheap reasoning distill from small curated sets — `gacMZf5rqYA`
- Alma — local model runner named for running distilled students (command not shown) — `gacMZf5rqYA`

### Where creators agree or clash with the conference talks

- **Agree: build the eval first.** Creators that run a fine-tune check it on a held-out set (`KQcQ7P78eTI`, `L-6O7R71CCg`). The distillation explainer adds a paraphrased copy of the eval set as a memorization check (`gacMZf5rqYA`). This matches the conference view that the eval, environment and training task are one object.
- **Agree: narrow fine-tunes of small models can beat large general models.** The creator examples echo the conference cases: a small fine-tune winning a narrow task head to head (`YAcIUCjsRnU`), and small curated-data reasoning models reported to match o1-preview (`gacMZf5rqYA`). Creator evidence is weaker: single runs and vendor claims.
- **Agree: fine-tune for behavior, retrieve for knowledge.** `YAcIUCjsRnU` states the same split that the conference talks use to argue against fine-tuning too early.
- **Clash: fine-tuning as a default.** Creator tools (Tinker, Cactus, Mini-AGI) make tuning look cheap and easy. Conference talks call fine-tuning tech debt that locks you to a model. Creator tutorials do not address the maintenance cost.
- **Clash: reward design.** The conference view is that simple binary rewards beat engineered rubrics for the RL update. `byfjZvrYRH0` shapes the reward for efficiency and correctness. `RGIrw2G70wE` shows how a shaped reward can be gamed. Single creator video, so treat it as a warning, not a rule.
- **Clash: distillation versus RL.** Conference talks favor distillation with hints for continual learning. The distillation explainer (`gacMZf5rqYA`, Kai Explains, a single creator video) says distilled students inherit the teacher's ceiling and are more brittle than RL-trained models, citing one study. Its caveat section is the strongest part.
- **Agree: continual learning is unproven.** `L-6O7R71CCg` claims 99.84% retention in one run with no published protocol. That matches the conference view that continual learning is still unproven.

### Watch first

- `RGIrw2G70wE` — a concrete reward-hacking case and a matched-pair audit to copy. Secondhand numbers.
- `YAcIUCjsRnU` — the fine-tune versus retrieval decision rule, plus a head-to-head small-model result (one customer case).
- `KQcQ7P78eTI` — an end-to-end small-model fine-tune with a held-out scoreboard. Small set, one run.
- `gacMZf5rqYA` — distillation recipes and the caveats on memorization and ceilings. Strong on caveats.
- `OM-DJuwweE0` — the ZeRO setup order in four minutes. Short, no config details.

## Watch first

- `V-EDrhIhHzQ` — Will Brown's full map of modern post-training: task/harness/runtime, async RL, interception server.
- `k35LeKZEhiE` — how environment bugs become model habits. Short and practical.
- `ZTA0GwpAUak` — hint-based distillation with clear numbers and no golden answers.
- `TyPpSRXGhbc` — the sub-$500 RL recipe with ablations on rewards and curricula.
- `4loPnxvWWhg` — the counterargument: when not to fine-tune.
- `xLxhT2ZI7UM` — why LLM judges lie and how to build a better verifier.
- `q4Tr-DknG2M` — Cursor's two-loop training flywheel and eval hygiene.
- `OA-Mc60Rboo` — reflective optimization as an alternative to weight updates.

## Implications for our projects

**SkillForge and EvolveCraft (open question: success signal).**
- Treat each skill as an environment with a verifier. Reuse it as eval and as training or optimization data. `jRCpXUjz4CI`, `AQv3qRCG6Gw`
- GEPA-style reflection over traces fits skill refinement. Keep a Pareto pool. A repo skill tuned on a cheap model transferred to a stronger one. `OA-Mc60Rboo`
- Mine telemetry for skill candidates the way the "agentic map-reduce" does: a cheap model writes records, a strong model summarises recurring failures. `jRCpXUjz4CI`, `CvRngaQZQ3Y`
- Use a rubric-first verifier with controllable versus uncontrollable failure classes as a skill-success signal. `xLxhT2ZI7UM`

**Govrix Scout (proxy).**
- The interception-server pattern is the same shape as our proxy: it records log-probs and token IDs and forwards unchanged. Training-data capture could be an opt-in pillar. `V-EDrhIhHzQ`, `k35LeKZEhiE`
- Trace-driven routing: group traces by use case and send each to the cheapest model that passes. `KB41dTlX1Uc`

**InferCraft.**
- Speculator retraining on live traffic and NVFP4 weights fit our stack. Skip TurboQuant on the KV path. `75ckHC2LU_0`
- Use KL against the unquantized model plus harness-level tests to validate quants. `J4_jCrTxMkk`
- Centralized pull-based queues roughly doubled throughput for small requests, relevant to our priority scheduler. `g4SsanB0gMc`
- Debug silent output bugs with a reference-model logprob oracle. `btxG75rNJC4`
- Training on one shared GPU: queue with preemption, frequent checkpoints, hard health gates. `byn9PURoBNY`

**MemoryMesh.**
- Decide placement before tuning: stable facts in retrieval, small behavior in prompt, only settled reflexes in weights. Debug retrieval first. `qflLT3SoVbw`
- Continual-learning benchmarks use gain over a stateless run, with drift injection. Good template for our memory evals. `iqloyWCGYQQ`
- Teach agents bounded, tiered search tools. `1IdzkRVmWAA`, `iJVxxxHM_Oc`

**Crucible (sandboxes).**
- RL rollouts map to sandboxes. Fan out one sandbox per rollout. `jRCpXUjz4CI`
- Replayable snapshots are required for GRPO-style groups. `k35LeKZEhiE`
- Strip git history and limit network inside the sandbox. `q4Tr-DknG2M`, `wcUJWP6WpGM`

- Traces become eval tasks, judge signals and nightly suites. Trace storage and read latency matter for these loops. `hd7TOvmyAxU`, `CvRngaQZQ3Y`

**Entity resolution and Haiku pipelines.**
- Distil a strong judge into a cheap one. Use consensus labels from several models, with a judge keeping agreeing labels. Use an any-yes merge for small judges to boost recall. `KB41dTlX1Uc`, `dKcTBQzR7jI`
- The Zeta2 filter fits label cleanup: drop always-wrong and always-right items and train on the middle band. `phchDt63qAA`

**ProsHarness.**
- Add a verifier-gated promotion step: candidate must beat production on a held-out suite. `hd7TOvmyAxU`
- Build evals before any optimization loop. `jRCpXUjz4CI`
- Checkpoint on SIGTERM and resume matches the long-run resume pattern. `bRGyYaE0lxI`

**Next-phase benchmark thesis.**
- Report spread across harnesses and infrastructure, not one number. Use Pareto reporting of reward, gain and cost. `ZyIoTOAbRfs`, `iqloyWCGYQQ`
