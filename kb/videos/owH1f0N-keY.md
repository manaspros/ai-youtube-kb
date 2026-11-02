# Gemini Nano on device — Florina Muntenescu & Oli Gaymond, Google DeepMind

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `owH1f0N-keY` · [watch](https://youtu.be/owH1f0N-keY) · **date:** 2026-06-18 · **length:** 19:38 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Florina Muntenescu, Oli Gaymond · **orgs:** Google DeepMind, Google
- **topics:** inference-serving, local-ai, product-ux · **tags:** on-device, gemini-nano, android, ml-kit, aicore, hybrid-inference, firebase-ai-logic, litert-lm, battery, privacy, gemma-4

> Google DeepMind's Android team on using Gemini Nano on-device via ML Kit GenAI and Firebase hybrid fallback, with Q&A on battery, shared-model scheduling and device reach.

## Summary
Two Google speakers give a short overview of on-device AI on Android, then take audience questions. They explain the split between on-device models (Gemini Nano through the AICore system service, accessed via ML Kit GenAI APIs) and cloud models, and recommend on-device when available with cloud fallback. The main case for on-device is privacy, offline use and zero per-call cost, with tasks that need short context as the best fit. The speakers say the model is shared system-wide so apps do not each ship a multi-gigabyte model, and that the system schedules requests with foreground apps prioritised over background ones. Battery impact is acknowledged: occasional interactive use is fine, while continuous background batch work drains quickly. Limits discussed include device coverage (the GenAI models need recent flagship devices), no embedding API yet, and custom models requiring the developer to do their own device testing.

## Key ideas
- **Default pattern is hybrid: run on-device when the local model is available, otherwise fall back to cloud.** — Firebase AI Logic hybrid inference (launched a couple of weeks before the talk) makes that choice per request. The speakers frame it as the way to keep reach across devices while still using local inference where possible. ([1:06](https://youtu.be/owH1f0N-keY?t=66))
- **On-device is worth it for privacy, offline use and zero per-call cost, but only for tasks that fit a small model and short context.** — Sensitive data such as banking information stays on the device, and offline work becomes possible. Translation and personalisation are cited as typical fits. ([2:14](https://youtu.be/owH1f0N-keY?t=134))
- **The model is one shared system resource, not a per-app download.** — Gemini Nano is delivered through the AICore system service, so every app calls the same model. Requests are run in isolation and input and output are not stored on the device. The speaker says the smallest useful models are about 1 GB and shipped ones nearer 3-4 GB, which an app developer would find hard to justify shipping alone. ([3:38](https://youtu.be/owH1f0N-keY?t=218))
- **The Prompt API is the general entry point, but it is limited to recent hardware.** — It takes text and image input and returns text only. Task-specific APIs (summarisation, proofreading, rewrite) also exist. Gemini Nano currently runs on Pixel 9 and 10 class devices and some other OEM devices, so the cloud fallback is what extends reach. ([4:57](https://youtu.be/owH1f0N-keY?t=297))
- **Battery cost depends on usage pattern: interactive bursts are fine, continuous background batch work is not.** — Users calling the model 10-20 times a day is not a concern. Batch jobs that are not latency-sensitive are suggested for overnight runs while charging. The speakers say the platform queues and schedules calls, and that the system can attribute battery use to an app, similar to GPS or Wi-Fi. ([9:06](https://youtu.be/owH1f0N-keY?t=546))
- **Foreground calls get priority over background calls on the shared model.** — If another app is using the model, a background request waits in the queue. The app the user is actively using is prioritised. Developers do not manage this themselves. ([11:51](https://youtu.be/owH1f0N-keY?t=711))
- **The on-device layer is meant to be the base that agents and skill systems are built on, not the agent itself.** — When asked about skills, the speakers said skills are effectively prompt content composed by a higher-level app. The APIs are designed as low-level building blocks for others to build on. ([14:30](https://youtu.be/owH1f0N-keY?t=870))
- **RAG is possible now by putting retrieved text into the prompt, but there is no embedding API yet.** — The speakers say an embedding API is planned, which would let developers use an embedding model such as EmbeddingGemma directly. Until then, similarity search needs to be done outside the on-device API. ([15:50](https://youtu.be/owH1f0N-keY?t=950))
- **Device coverage differs by model type: classic ML Kit models reach most devices, GenAI models need recent flagships.** — Classic vision, OCR and text models are said to run on over a billion devices. GenAI APIs need flagship devices from the last couple of years. Custom models via LiteRT-LM require the developer to test across devices and profile battery impact. ([17:22](https://youtu.be/owH1f0N-keY?t=1042))

## Techniques
- **Runtime hybrid routing with cloud fallback** — Check whether the on-device model is available at runtime. Send the request to the on-device model if so, otherwise to a cloud model through Firebase AI Logic, so one feature works across devices. *When:* When the feature must work on devices without the local model, but local inference is preferred for privacy, latency or cost.
- **Use the ML Kit GenAI Prompt API for on-device structured tasks** — Send natural-language prompts with text or image input to Gemini Nano. Use it for entity extraction, content analysis and image understanding. Use the task-specific APIs (summarise, proofread, rewrite) when they match the job. *When:* For short-context, private or offline tasks such as extracting fields from a banking screenshot or summarising text on the device.
- **Offload non-urgent batch work to background, charging-time windows** — Queue large, non-latency-sensitive jobs and run them in the background, for example overnight while the phone charges. Keep interactive calls for user-initiated moments. *When:* When processing many items where each result is not needed immediately, to limit battery impact.
- **Prompt-stuffed retrieval as a stopgap RAG** — Retrieve relevant text with your own search or index outside the on-device API, then pass the retrieved text into the Prompt API as part of the prompt. *When:* Before an on-device embedding API is available, if you need grounded answers over local content.
- **Device testing and profiling for custom models** — For custom models through LiteRT-LM, test across a range of devices and profile battery and latency yourself, since the platform does not do this for custom models. *When:* When you need a model that is not covered by AICore and must reach a wider device range.

## Numbers
- Smallest useful on-device models are about 1 GB; shipped models are close to 3-4 GB in total. ([10:35](https://youtu.be/owH1f0N-keY?t=635))
- Typical user interaction with on-device AI is around 10-20 uses per day, which the speaker says is not a concerning battery load. ([9:06](https://youtu.be/owH1f0N-keY?t=546))
- Classic ML Kit vision, OCR and text models run on a very large device base (described as over a billion devices). ([17:22](https://youtu.be/owH1f0N-keY?t=1042))
- Gemini Nano GenAI APIs currently need recent flagship devices; the speakers name the Pixel 9 and Pixel 10 generation plus some other OEMs. ([4:57](https://youtu.be/owH1f0N-keY?t=297))

## Hot takes
- A 3-4 GB on-device model is not something an app developer should ship alone; a single system-managed model is the right trade-off (speaker's view).
- Continuous background use of on-device AI will drain the battery quickly, so the feature design has to avoid it (speaker's view).

## Tools mentioned
Gemini Nano, AICore, ML Kit GenAI APIs, Prompt API, Firebase AI Logic, LiteRT-LM, AI Edge Gallery, Gemma 4

## Relevance to our work
- **agentos** (1/3): InferCraft covers local inference and scheduling on one GPU; this talk describes the same idea of a shared model with system-level queueing and foreground priority, but for phones. → *Read the AICore scheduling and foreground-priority design as a reference when designing InferCraft's 4-class priority scheduler, then decide whether any of it applies to a single-GPU server.*
- **general** (1/3): Cheap-model pipeline idea: batch non-urgent jobs in off-peak windows and keep interactive calls separate; the same split applies to Haiku batch work. → *Note the batch-versus-interactive split from the battery discussion as a design check for any cheap-model batch pipeline.*
