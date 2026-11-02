# The 2.3B AI Model that "Thinks" like a 70B (Gemma 4)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ZxQ2DuejRhU` · [watch](https://youtu.be/ZxQ2DuejRhU) · **date:** 2026-05-02 · **length:** 10:26 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Andrus · **orgs:** Google, Better Stack
- **topics:** local-ai, models-research, evals · **tags:** gemma-4, on-device-llm, small-models, lm-studio, cline, litert-lm, ios, multimodal, ocr, apache-2.0, knowledge-cutoff

> Better Stack runs informal local and on-phone tests of Google's Apache 2.0 Gemma 4 E2B and E4B models: fast on iPhone, weak at coding and vision, with Google's benchmark claims left unverified.

## Summary
Andrus from Better Stack tests Google's newly released Gemma 4 small models, the E2B and E4B edge variants under Apache 2.0, which Google says run offline on phones and a Raspberry Pi. He explains the claimed architecture (per-layer embeddings, native multimodality, a thinking mode, 128K context, 140+ languages) and repeats Google's own benchmark numbers without independent checks. He then runs his earlier Qwen 3.5 tests on Gemma 4 through LM Studio and Cline with internet disabled: E2B produces a flawed cafe website with leftover task text and a missing JS file, while E4B gets a working cart but a bland design. On an iPhone, he uses Google's AI Edge Gallery app because there are no MLX or LiteRT-LM iOS bindings yet; responses feel fast, the car-wash logic question is answered correctly but for the wrong reasons, the dog breed is misidentified, Latvian OCR is mostly accurate, and the model names Joe Biden as current president while self-reporting a January 2025 cutoff. The video is a short, single-prompt anecdotal review with no quantitative measurements of its own.

## Key ideas
- **Gemma 4 is an Apache 2.0 open model with edge variants E2B and E4B. The 'E' stands for effective parameters: about 2.3B active at inference, which the speaker says gives the reasoning depth of a 5B model.** — Google's claim as relayed by the speaker. He ties the small active-parameter count to a reported memory footprint under 1.5 GB. ([0:00](https://youtu.be/ZxQ2DuejRhU?t=0))
- **The claimed architectural change is per-layer embeddings: each layer has its own embeddings, so new information can be injected where it is needed, rather than carrying one input embedding through every layer.** — This is the technical shift the speaker says Google highlights. He does not verify it. ([0:00](https://youtu.be/ZxQ2DuejRhU?t=0))
- **Gemma 4 is claimed to be natively multimodal (vision, text, audio) in one architecture, with a thinking mode that checks its own reasoning chain before answering, a 128K context window, and support for 140+ languages.** — The thinking mode is pitched as a way to avoid the loops and logic errors that small models often produce. ([1:19](https://youtu.be/ZxQ2DuejRhU?t=79))
- **Google's own benchmark claims are unverified: E4B scores 42.5% on AIME 2026 (more than double larger previous-generation models) and shows a large jump on T2 bench tool use, with agent skills built on native function calling.** — These are Google's internal tests, which the speaker repeats without independent checks. ([2:29](https://youtu.be/ZxQ2DuejRhU?t=149))
- **On a local coding task (a cafe website in HTML, CSS and JS, reused from the Qwen 3.5 test), E2B was underwhelming and E4B was a clear step up.** — E2B left its task list at the end of the HTML and CSS files and claimed to have written a JS file that did not exist. E4B produced a working cart, though the design was bland. The speaker concludes that small models are not for serious coding. ([3:38](https://youtu.be/ZxQ2DuejRhU?t=218))
- **On an iPhone there are no MLX or LiteRT-LM iOS bindings for Gemma 4 yet, so the only option was Google's AI Edge Gallery app. Responses felt faster than Qwen 3.5 on the same phone.** — The app also reported insufficient storage when downloading E4B, which the speaker suspects is a bug. He attributes the speed to the LiteRT-LM framework, which he has not verified. ([6:02](https://youtu.be/ZxQ2DuejRhU?t=362))
- **Vision and language checks were mixed. The model identified a dog correctly but named the wrong breed. Latvian OCR was mostly accurate, though the Latvian chat grammar was odd.** — The speaker treats Latvian as a stress test for the claimed 140-language support, since it is a small language. ([7:13](https://youtu.be/ZxQ2DuejRhU?t=433))
- **The model's knowledge is inconsistent: it named Joe Biden as the current US president but reported a January 2025 knowledge cutoff when asked directly.** — Useful as a quick probe for any model's cutoff claims, which may not match its actual knowledge. ([8:23](https://youtu.be/ZxQ2DuejRhU?t=503))

## Techniques
- **Offline local test harness with LM Studio and Cline** — Download the model in LM Studio, raise the context window setting, start the LM Studio local server. In Cline (transcribed as 'Klein'), point the provider at the LM Studio server, select the model (E2B or E4B), then disable the internet connection to confirm the run is fully local before testing. *When:* Testing small open-weight models for offline coding or agent work, with a repeatable setup you can rerun on the next model.
- **Fixed-prompt regression comparison across models** — Reuse the same prompt (here, the cafe website prompt from the previous video) across model sizes and generations, then compare output size, time to finish and whether the result works when opened. *When:* Comparing model variants on one task, or checking a new release against a previous baseline.
- **Check model output artifacts for leakage and phantom files** — Open every generated file and check for leftover planning text, and confirm each file the model claims to have written actually exists. *When:* Reviewing output from small models, which may append task lists to files or report work that was not produced.
- **Quick capability probes** — Ask a logic riddle (the 'car wash' question) and check whether the final answer is right and for the right reason. Use a picture with a fine-grained label (dog breed) to probe vision. Ask a non-English question on OCR and chat. Ask for the current president and for the knowledge cutoff to check the model's self-reported date against its answers. *When:* Fast smoke tests for a new small model before deeper evaluation. Single prompts are anecdotal and do not measure reliability.
- **Try on a phone with the vendor's app** — Use Google's AI Edge Gallery app to run the Gemma 4 models on an iPhone, since no iOS bindings exist yet for MLX or LiteRT-LM. *When:* Trying an on-device model before native bindings are available.

## Numbers
- E2B and E4B: about 2.3B active (effective) parameters, a reasoning depth the speaker attributes to a 5B model, under 1.5 GB RAM (Google's claims as relayed) ([1:19](https://youtu.be/ZxQ2DuejRhU?t=79))
- 128K context window and 140+ languages (Google's claims) ([1:19](https://youtu.be/ZxQ2DuejRhU?t=79))
- E4B scores 42.5% on AIME 2026 (Google's internal test), more than double larger previous-generation models ([2:29](https://youtu.be/ZxQ2DuejRhU?t=149))
- Cafe website generation: E2B about 1.5 minutes; E4B about 3.5 minutes. The Qwen 3.5 comparison model in the earlier test had 0.8B parameters. ([3:38](https://youtu.be/ZxQ2DuejRhU?t=218))
- Self-reported knowledge cutoff: January 2025 ([8:23](https://youtu.be/ZxQ2DuejRhU?t=503))

## Hot takes
- The benchmark numbers come from Google's internal tests and the speaker repeats them without independent checks, so the advertised gains are unverified.
- E2B was underwhelming for coding and E4B is still too weak for serious coding work, in the speaker's view.
- The Edge Gallery app's 'insufficient storage' message is probably a bug, according to the speaker.
- The car-wash answer is correct, but the speaker argues the model reasoned about convenience, not the logic of the question, so it passes only partly.

## Tools mentioned
Gemma 4 (E2B, E4B, Google, Apache 2.0), Qwen 3.5 (compared in the speaker's earlier video), LM Studio, Cline (transcribed as 'Klein'), Google AI Edge Gallery app, LiteRT-LM (Google's inference framework), MLX / Swift MLX (no Gemma 4 bindings yet), swift-lm (community project working on unofficial native bindings, as transcribed)

## Relevance to our work
- **agentos** (1/3): A sub-3B on-device model could be a cheap local classifier candidate, for example for PII or prompt-injection screening in the L1 scanner. The video gives no measured accuracy or latency, so it is only a lead. → *Run Gemma 4 E2B and E4B on the same PII and prompt-injection eval set used for the Govrix Scout scanner, and compare accuracy and latency against the current scanner before adopting either.*
