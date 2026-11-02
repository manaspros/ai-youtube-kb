# Phi-4: The Smallest Open Source AI Model

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `yzSYIndCWD8` · [watch](https://youtu.be/yzSYIndCWD8) · **date:** 2025-11-02 · **length:** 9:17 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** AI LABS host (name not given in transcript) · **orgs:** Microsoft, OpenRouter
- **topics:** local-ai, coding-agents, vibe-coding-app-building · **tags:** phi-4, small-models, ollama, local-llm, bolt-diy, cline, openrouter, local-coding-agent, model-evaluation

> Single-run hands-on test of Phi-4 (14B, MIT license) through Ollama, bolt.diy and Cline. It runs locally, but it failed to integrate a React component, which the speaker blames on the context window.

## Summary
The host (AI LABS channel) tests Microsoft's 14B open-weight model, which the captions render as "5.4" throughout (the title says Phi-4), on a Spotify-clone front end. He cites the model's published-style figures of 84.8 on MMLU and 82.6 on HumanEval, but says he does not rely on benchmarks alone. Setup walkthroughs cover installing Ollama and pulling the model, getting an OpenRouter key as a fallback, cloning and running bolt.diy with pnpm, and configuring the Cline VS Code extension to use the local Ollama endpoint. On a card-component task, the model in bolt.diy produced a terminal error and did not apply its own suggested fixes, so he used Claude to write the component instead. Cline then repeatedly failed to understand a request to integrate that component into the existing Next.js 14 app, even with explicit file references. A smaller task (a playable synth keyboard in bolt.diy) worked after one follow-up fix. His conclusion is that the model is efficient locally but falls short on complex real-world coding, possibly because of a small context window, which he did not verify.

## Key ideas
- **Phi-4 is presented as a 14B open-weight model released under MIT, so it is commercially usable and can run locally at reasonable speed.** — The speaker frames the model's size and license as the main draw, citing benchmark numbers but saying he wants to test real-world coding himself. ([0:00](https://youtu.be/yzSYIndCWD8?t=0))
- **Local serving is set up with Ollama: install it, pick the model from its library, and run the command copied from the model page.** — The first download is about 9 GB. The speaker suggests OpenRouter as a fallback if the machine cannot run the model. ([1:23](https://youtu.be/yzSYIndCWD8?t=83))
- **Small model in bolt.diy failed a realistic component task, and the model's own fix suggestions were not applied.** — The generation hit a terminal error during npm setup. Asking the model to apply its suggested fix did not work, and the speaker's manual fix did not resolve it either. ([3:43](https://youtu.be/yzSYIndCWD8?t=223))
- **He used a frontier model (Claude) to write the hard component and handed only the integration step to the local model in Cline.** — The integration step still failed. Cline repeatedly asked how to proceed, and explicit file-reference syntax did not help. ([4:42](https://youtu.be/yzSYIndCWD8?t=282))
- **Scoping down rescued the test: the same model built a playable synth keyboard in bolt.diy, and a short follow-up fixed the missing sound.** — The speaker reads this as evidence that small, self-contained tasks suit the model and that multi-file integration does not. ([7:23](https://youtu.be/yzSYIndCWD8?t=443))
- **Speaker's verdict: the model is efficient locally, but the benchmarks did not reflect complex real-world coding, so it may suit non-coding tasks better.** — He attributes the failure to the small context window, a diagnosis he never checked against the model's actual context limit. ([8:45](https://youtu.be/yzSYIndCWD8?t=525))

## Techniques
- **Local model via Ollama** — Install Ollama, check that it is running, open the model's page in the Ollama library, copy the run command shown there, and paste it into a terminal. The first run downloads about 9 GB. Send a test message to confirm it responds. The transcript does not show the exact model tag. *When:* Running a model privately on your own GPU or Mac, for offline or cost-free experiments.
- **OpenRouter key as a hosted fallback** — Open OpenRouter, find the model, open its API section, create a named key with an optional credit limit, and store it safely, since the key cannot be viewed again after creation. *When:* The local machine cannot run the model, or you want to try it without a download.
- **bolt.diy from source** — Clone the GitHub repo, cd into it, run pnpm install, then pnpm run dev, and open the localhost link it prints. *When:* Running a browser-based AI app builder against a model of your choice.
- **Point Cline at local Ollama** — In the VS Code extension, open Settings, set API Provider to Ollama, keep the default base URL (or set your custom one), and select an installed model from the list that appears. *When:* Driving an in-editor coding agent with a local model instead of a cloud API.
- **Frontier model writes, local model integrates** — Generate a self-contained component with a frontier model from a screenshot plus a text prompt. Then paste the code and an integration instruction into the local agent. The speaker used this split and the integration step failed. *When:* Splitting work between an expensive strong model and a cheap local one. Treat the integration step as the risky part to verify.
- **Shrink the task when the agent stalls** — When a large edit stops making progress, ask for a small, isolated feature instead. A single follow-up prompt then fixed a bug in the smaller app. *When:* Evaluating a small model's limits, or recovering a session that is looping on a big change.

## Numbers
- Model size: 14 billion parameters. ([0:00](https://youtu.be/yzSYIndCWD8?t=0))
- Speaker-cited MMLU score of 84.8. ([0:00](https://youtu.be/yzSYIndCWD8?t=0))
- Speaker-cited HumanEval score of 82.6 (captioned as "human evil"). ([0:00](https://youtu.be/yzSYIndCWD8?t=0))
- Ollama model download is about 9 GB. ([1:23](https://youtu.be/yzSYIndCWD8?t=83))
- Single informal run per task. No timings, token counts, costs or repeat trials were reported. ([3:43](https://youtu.be/yzSYIndCWD8?t=223))

## Hot takes
- Benchmarks did not reflect real-world coding: the model handled simple tasks but stalled on multi-file integration in Cline.
- The failure is attributed to a small context window. This is the speaker's guess, not something he checked against the model's documented context length.
- Use case fit: the model may suit non-coding work better than coding-heavy projects.
- Evidence is one anecdotal run per task, with the frontier model doing the hard part. The model name is mis-captioned as "5.4" throughout, which weakens the link to the title.

## Tools mentioned
Phi-4 (Microsoft, 14B open weights, MIT license; captioned as "5.4"), Ollama, OpenRouter, bolt.diy (captioned "BoltDIY" and "bold.diy"), Cline (captioned "Klein"; formerly Claude Dev), Claude (used to write the card component), VS Code, pnpm, Next.js 14, React, TypeScript, Tailwind CSS

## Relevance to our work
- **agentos** (1/3): AgentOS already serves models on vLLM with an RTX 5090. This video only shows Ollama on a laptop-scale setup with one anecdotal run, which adds little to InferCraft.
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, so local-model editing is not the target. The one useful signal is that a small model stalled on an integration step, which argues for keeping edit-heavy steps on frontier models. → *No change needed now. If a local-model fallback is ever added to ProsHarness, gate it on a fixed edit-task eval before enabling it.*
