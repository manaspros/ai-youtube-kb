# From 46% to 90%: Fine-Tuning Tiny LLMs for On-Device Agents — Cormac Brick, Google

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `-TiET_K-E_g` · [watch](https://youtu.be/-TiET_K-E_g) · **date:** 2026-06-18 · **length:** 21:01 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Cormac Brick · **orgs:** Google, Google AI Edge, Google DeepMind
- **topics:** training-finetuning-rl, local-ai, inference-serving, skills-self-improvement · **tags:** on-device, small-language-models, LiteRT-LM, Gemma 4, FunctionGemma, function-calling, fine-tuning, synthetic-data, agent-skills, progressive-disclosure, mobile, offline-asr

> Google's Cormac Brick on on-device agents: a prompt-based skill harness on Gemma 4, and fine-tuning FunctionGemma on synthetic data to lift function-calling success from about 46% to 90%+ on most functions.

## Summary
Cormac Brick (Google AI Edge) argues that small models running on the device are worth using when you need latency, privacy, offline use, or savings. He presents two ideas. The first is a simple agent skill harness for Gemma 4 in an app: skill names and descriptions go in the system prompt, and the full skill loads only when the model calls a load-skill tool. Skills can also ship small JavaScript for in-app UI, and the team has used a coding agent (Gemini CLI) to write about 80 skills. The second idea is that tiny models (under about a billion parameters, and far smaller for narrow tasks) become reliable only after fine-tuning on a narrow task. His example is FunctionGemma (270M): with synthetic data made by Gemini Flash for seven functions, function-calling success rose from roughly 46% (his hedged recollection) to over 90% on eight of ten functions, with two in the 80s. He also describes an offline transcription app built from two chained few-hundred-million-parameter models (ASR plus text polishing). He is candid that single-turn chaining of multiple skills is still unreliable. The talk is product-tinged but gives concrete, usable numbers and a fine-tuning workflow.

## Key ideas
- **A skill harness can be just a prompt plus one tool** — Skill names and descriptions sit in the system prompt, so the model knows what exists without seeing every detail. A load-skill tool call fetches the full skill only when needed. He says this is a few lines of code. ([7:34](https://youtu.be/-TiET_K-E_g?t=454))
- **Skills can carry small JavaScript for in-app UI** — A skill can include JS that the app runs to render something in place, such as a map view or a roulette wheel, instead of only returning text. ([7:34](https://youtu.be/-TiET_K-E_g?t=454))
- **Coding agents can write the skills** — The team prompted Gemini CLI to write skills and built about 80 this way. An ADB skill lets the agent test on a connected device. Skills can be published to a GitHub URL and loaded into the app. ([8:46](https://youtu.be/-TiET_K-E_g?t=526))
- **Tiny models need a narrow task and fine-tuning** — Below roughly 100-200M parameters, the model needs a very narrow, focused task. He says fine-tuning on synthetic data is the common workflow for this, and it is more work than prompting a larger model but ships more reliably at scale. ([11:17](https://youtu.be/-TiET_K-E_g?t=677))
- **Fine-tuning moved function calling from about 46% to 90%+** — Baseline FunctionGemma was around 46% (speaker hedged). Flash generated the synthetic dataset for seven functions. Eight of ten functions reached over 90%, and two were in the 80s. The fixed function list moved from the system prompt into the trained weights. ([14:00](https://youtu.be/-TiET_K-E_g?t=840))
- **Chaining tiny models gives a useful offline product** — The transcription app uses an ASR model and a text-polishing model, each a few hundred million parameters, plus a personal dictionary. The polishing step removes filler words like 'um'. He presents it as proof that the approach works in production. ([16:20](https://youtu.be/-TiET_K-E_g?t=980))
- **Multi-skill turns are the open weakness** — Chaining several skills in one answer works only sometimes. Single-skill calls across a conversation are robust. The default 4B model has about eight skills enabled and picks among them reasonably well. ([18:22](https://youtu.be/-TiET_K-E_g?t=1102))

## Techniques
- **Progressive skill disclosure** — Put only skill names and one-line descriptions in the system prompt. Expose a load-skill tool. When the model calls it, return the full skill body (instructions, JS, tool details) into context. *When:* Many skills, small context budget, on-device or any setup where a full skill list would bloat the prompt.
- **In-app JavaScript rendering from a skill** — Let a skill include a JS module the host app runs to draw a UI (for example a map or a wheel) directly in the app, rather than returning plain text. *When:* When the answer is better shown than said, and the host app can execute bundled JS.
- **Coding agent writes the skills** — Prompt a coding CLI (Gemini CLI in the talk) to author each skill, and give it a device or test-harness skill (ADB) so it can test the result on hardware. *When:* Building a large skill library quickly; the team reports this works reliably with a clear prompt.
- **Synthetic-data fine-tune for fixed function calling** — Define the small set of functions. Use a strong LLM (Flash) to generate a labelled dataset of user requests mapped to calls. Fine-tune a small model on it and drop the function list from the system prompt. Check per-function accuracy. *When:* A narrow, fixed set of actions (about 7-10 functions) and you need reliable calls from a tiny model at scale.
- **Export and deploy pipeline for small models** — Start from a transformers checkpoint, export with the litert-torch package, bundle into a single LiteRT-LM file (which includes the tokenizer), test on desktop with the reference runtime, then ship on device. *When:* Shipping a small LLM inside a mobile or web app with a single-file artifact.
- **Chained tiny models for a pipeline** — Split the job into stages (speech to text, then text cleanup), each a small specialised model. Add user-specific vocabulary to the first stage and filler removal to the second. *When:* Offline pipeline where one large model is too heavy and each stage is narrow.

## Numbers
- LiteRT runtime is built into Android and supports over 2.7 billion devices (speaker's figure). ([2:04](https://youtu.be/-TiET_K-E_g?t=124))
- FunctionGemma (270M params) on a Pixel 7 processes about 2,000 tokens/s prefill and 140 tokens/s decode. ([12:32](https://youtu.be/-TiET_K-E_g?t=752))
- FastVLM (about 500M params, Apple) runs on a Qualcomm NPU through the Google stack with hardware acceleration; no latency figure given. ([12:32](https://youtu.be/-TiET_K-E_g?t=752))
- FunctionGemma function-calling success was about 46% out of the box (speaker said 'I think'). ([14:00](https://youtu.be/-TiET_K-E_g?t=840))
- After synthetic-data fine-tuning on seven functions, success exceeded 90% on 8 of 10 functions, and two were in the 80s. ([15:20](https://youtu.be/-TiET_K-E_g?t=920))
- The team has built about 80 skills with a coding agent. ([8:46](https://youtu.be/-TiET_K-E_g?t=526))
- The default 4B model has about eight skills enabled by default. ([17:33](https://youtu.be/-TiET_K-E_g?t=1053))
- The offline transcription app chains two models, each a few hundred million parameters. ([16:20](https://youtu.be/-TiET_K-E_g?t=980))

## Hot takes
- For a narrow, fixed set of functions, a fine-tuned sub-300M model on synthetic data beats prompting a larger model, though it is more work.
- Skill libraries can be authored by a coding agent, which the speaker says works reliably with a clear prompt.
- Multi-skill chaining in a single turn is still unreliable on tiny on-device models.

## Tools mentioned
LiteRT-LM, LiteRT, MediaPipe, Gemma 4, FunctionGemma, Gemma 3, Gemini Nano, Android AICore, Gemini CLI, Gemini Flash, litert-torch, transformers, Hugging Face, ADB, Qualcomm NPU

## Relevance to our work
- **agentos** (1/3): Shows a skill-loading pattern (descriptions in prompt, body fetched on demand) and a synthetic-data fine-tune for a small model; both touch the SkillForge and InferCraft ideas, but this is on-device and vendor-specific. → *Compare the load-skill-on-demand pattern with SkillForge's skill-worthiness design before deciding how skills are injected into agent prompts.*
- **prosharness** (1/3): The on-demand skill load pattern relates to ProsHarness skill ranking, where choosing which skill to inject is the hard part. → *Test whether ProsHarness can list only skill names and descriptions in the prompt and load full skill bodies on a tool call, to cut prompt size on long runs.*
