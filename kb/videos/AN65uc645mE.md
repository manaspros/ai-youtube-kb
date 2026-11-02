# 200 Million Patient Interactions Later — Vivek Muppalla, Hippocratic AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `AN65uc645mE` · [watch](https://youtu.be/AN65uc645mE) · **date:** 2026-09-18 · **length:** 20:40 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Vivek Muppalla · **orgs:** Hippocratic AI
- **topics:** voice-multimodal, inference-serving, evals, multi-agent · **tags:** healthcare, voice-agent, latency, asr, speculative-decoding, kv-cache, quantization, specialist-models, tool-call-verification, statistical-evals, safety-rubric, empathy-benchmark

> Hippocratic AI's engineering lead explains how their clinical voice agent (200M+ patient conversations) hits safety, latency and accuracy at once: a vertically built stack, 31 parallel specialist models, context-fed ASR, and lossless inference tricks.

## Summary
The speaker, who runs AI engineering at Hippocratic AI, describes a voice agent that places outbound clinical calls to patients, with over 200M conversations, a stated zero significant safety incidents, and deployment at 60+ health systems. He argues that latency and intelligence are not a trade-off for them: each latency optimization is reinvested into more checking, which compounds. The architecture ("Polaris") has three parts: an ASR front end that is a decoder-only audio LLM conditioned on conversation context and domain knowledge, a central reasoning model that runs alongside 30 specialist models in parallel (each one short-circuits if it has nothing to say), and a voice and documentation output layer. Background verifiers check tool-call parameters, and some checks run offline so errors can be corrected later. On evals, he works through the statistics: catching a 1% failure rate needs about 450 tests, so they combine roughly 7,000 clinicians with synthetic data, and they grade outputs on a human harm rubric. Inference speedups (4-bit quantization, speculative decoding, a warm KV cache) are kept lossless. Most specific numbers are self-reported, and the talk is a company showcase, so the ideas are more useful than the claims.

## Key ideas
- **Latency savings are reinvested, not banked** — Each latency optimization frees budget that the team spends on more intelligence or checking, so the latency-vs-intelligence tension becomes a compounding flywheel. ([7:09](https://youtu.be/AN65uc645mE?t=429))
- **Parallel specialists with a short-circuit gate** — About 31 models run on every turn in parallel. Each specialist first decides whether it needs to speak, which keeps the latency budget. A central model steers the conversation using specialist input, and the redundancy avoids a single point of failure. ([12:20](https://youtu.be/AN65uc645mE?t=740))
- **Generic benchmarks miss the failures that matter in clinical voice** — Lab-result checks and IVR navigation are not in common benchmarks, and generic models do poorly on them. The team says it needed over 99% on such domain benchmarks. Many apparent reasoning failures were actually mishearing (e.g., drug names, letters vs. numbers). ([7:09](https://youtu.be/AN65uc645mE?t=429))
- **Give ASR the conversation and domain context** — A fine-tuned Whisper-large-turbo encoder feeds an audio LLM that also receives the conversation so far, the domain and policy, and lists such as the patient's medications. Choosing from a finite list cuts word errors. Synthetic patient data is used for contextual biasing on addresses and phone numbers. ([9:56](https://youtu.be/AN65uc645mE?t=596))
- **Re-score single-word answers with full context** — Short replies like 'no' vs 'now' or 'five' vs 'fine' are where transcription errors are most harmful. The team runs a second scoring pass only for single-word utterances, using the whole conversation. ([12:20](https://youtu.be/AN65uc645mE?t=740))
- **Verify tool calls asynchronously, and offline when time allows** — Background verifiers check tool-call parameters and responses. For scheduling, this is said to reach high accuracy. Where time permits, verification runs offline, so an wrong appointment can be corrected by calling the patient back. ([13:39](https://youtu.be/AN65uc645mE?t=819))
- **Do the statistics before trusting an eval** — With 10,000+ calls a day, a 1% error rate means about 100 wrong appointments daily. Catching a 1% rate needs about 450 tests for 99% confidence, and about 1,900 to see 10 hits. Synthetic data alone was judged insufficient, so they combine it with human-graded conversations. ([16:05](https://youtu.be/AN65uc645mE?t=965))
- **Grade safety on a clinical harm scale, not just correctness** — Outputs are graded on correctness, no harm, minor harm, severe harm and death, the same scale used for human clinicians. The speaker reports 99.89% no-harm across five product generations, against about 81% for humans on the same rubric. ([17:12](https://youtu.be/AN65uc645mE?t=1032))
- **Inference optimizations must be lossless** — Quality is the constraint and speed is the work. Three named techniques: 4-bit quantization (described as lossless), speculative decoding with a small draft model, and KV-cache handling that keeps long conversations warm. ([14:47](https://youtu.be/AN65uc645mE?t=887))

## Techniques
- **Parallel specialist models with self-gating** — Run many domain specialists on every turn concurrently. Each one does a fast check on whether it should speak, and only then produces output. A central model integrates the specialist input and decides what to say. *When:* Many domain checks per turn under a tight latency budget, where a single monolithic model is a single point of failure.
- **Context-conditioned ASR** — Use an audio LLM (decoder-only) that takes the audio plus conversation history, domain knowledge and task context such as the medication list or form fields. Constrain candidates to a finite list where one exists. Use synthetic data in training to teach rare entities such as addresses. *When:* Domain speech with rare named entities (drug names, addresses) where generic ASR errors change the meaning.
- **Second-pass rescoring for ambiguous short utterances** — Detect single-word or very short responses and re-score them with the whole conversation as context. *When:* Yes/no or number answers, where one wrong word flips the meaning of the answer.
- **Async and offline verifiers for tool calls** — Run background checks on tool-call parameters and results without blocking the live turn. Where latency allows, re-verify offline and correct the record afterward. *When:* Agents that call scheduling or record-writing tools where a silent wrong call is costly and can be fixed later.
- **Human plus synthetic eval mix with sample-size planning** — Compute how many tests are needed to detect a target failure rate at a given confidence before running them. Use human clinicians on a continuous basis to supply most of the eval data, and synthetic data to scale. *When:* Low-error-rate production agents where synthetic data alone misses real failures.
- **Severity-graded harm rubric** — Grade every output on an ordered scale (correct, no harm, minor harm, severe harm, death), using the same rubric humans are graded on, so AI and human performance can be compared directly. *When:* High-stakes domains where a pass/fail score hides how bad a failure is.
- **Lossless inference stack** — Apply quantization (16-bit to 4-bit), speculative decoding with a smaller draft model that the main model verifies in one pass, and KV-cache retention for long conversations to raise cache hit rate and speed up prefill. *When:* Long multi-turn sessions where prefill cost dominates and output quality cannot drop.

## Numbers
- Over 200 million clinical conversations; zero significant safety incidents (self-reported) ([0:08](https://youtu.be/AN65uc645mE?t=8))
- Deployed in 60+ health systems, patient satisfaction 8.5 out of 10 ([0:08](https://youtu.be/AN65uc645mE?t=8))
- About 31 models run in parallel per conversation ([8:27](https://youtu.be/AN65uc645mE?t=507))
- Over 30% word error rate on some Arabic drug names with off-the-shelf ASR (as stated) ([9:56](https://youtu.be/AN65uc645mE?t=596))
- Medical word error reduced by over 50% vs standard off-the-shelf models; P99 latency claimed 3x faster than others ([12:20](https://youtu.be/AN65uc645mE?t=740))
- Target accuracy of over 99% on lab-result checks and IVR navigation benchmarks ([7:09](https://youtu.be/AN65uc645mE?t=429))
- Over 96% KV-cache hit rate on long conversations; prefill 18x faster ([16:05](https://youtu.be/AN65uc645mE?t=965))
- 10,000+ calls a day; a 1% error rate equals about 100 wrong appointments per day ([16:05](https://youtu.be/AN65uc645mE?t=965))
- About 450 tests needed to be 99% sure of catching a 1% error rate; about 1,900 to see it 10 times ([17:12](https://youtu.be/AN65uc645mE?t=1032))
- Over 7,000 trained clinicians; close to 800,000 clinical conversations used for accuracy evaluation ([17:12](https://youtu.be/AN65uc645mE?t=1032))
- 99.89% no-harm across five product generations (Polaris) vs about 81% for humans on the same rubric ([17:12](https://youtu.be/AN65uc645mE?t=1032))

## Hot takes
- Most real-world voice-agent failures that look like reasoning errors are actually mishearing.
- Latency savings should be spent on more safety checks, not banked as speed.
- Safe is not enough: a clinical voice agent also has to be empathetic enough that people open up to it.
- A 99% accuracy target is still too weak for high-volume scheduling; the 1% tail is the real problem.

## Tools mentioned
Whisper (large-turbo, fine-tuned), speculative decoding, 4-bit quantization, KV cache

## Relevance to our work
- **agentos** (2/3): The statistical sizing of eval sets for rare failures and the rubric-graded harm scoring map onto AgentOS's RAGAS-based evals and its guardrail goals. The parallel gate-then-speak pattern is also close to how a proxy-level guardrail could be structured. → *Before reporting any failure rate from AgentOS evals, compute how many test cases are needed to detect that rate at the chosen confidence, and add a severity-graded (not pass/fail) scoring field for guardrail outcomes.*
- **prosharness** (1/3): Background verification of tool-call parameters, with some checks run offline and results corrected later, is a pattern ProsHarness could use for its loop and schedule steps. → *Consider an async verifier pass over ProsHarness tool-call arguments and results that runs after a step and flags mismatches for the next resume, rather than blocking the run.*
- **general** (1/3): Entity resolution and data quality work can borrow the idea of narrowing candidates to a finite, context-chosen list before matching, as the talk does for medication names. → *In entity resolution, try limiting candidate matches to a context-selected list (e.g., same country or record type) before fuzzy scoring, and measure the effect on error rate.*
