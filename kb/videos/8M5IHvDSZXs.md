# NVIDIA Quietly Dropped This POWERFUL AI Model (Nemotron v2)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `8M5IHvDSZXs` · [watch](https://youtu.be/8M5IHvDSZXs) · **date:** 2025-11-02 · **length:** 7:55 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Andrus (Better Stack) · **orgs:** NVIDIA, Better Stack, RunPod, Hugging Face
- **topics:** local-ai, inference-serving, models-research · **tags:** nemotron, nemotron-nano-v2, mamba-2, hybrid-architecture, reasoning-budget, vllm, runpod, self-hosting, model-review, logic-tests

> Better Stack's hands-on look at NVIDIA's 9B Nemotron Nano v2: a hybrid Mamba-2/attention model, a reasoning-budget cap, mixed logic and coding results, and a RunPod + vLLM deployment.

## Summary
The video presents NVIDIA's Nemotron Nano v2 (9B parameters) as a lean reasoning model that keeps only a few attention layers and replaces the rest with Mamba-2 layers, which the speaker says avoids the quadratic cost of attention on long sequences. The speaker highlights a reasoning budget control that caps how many tokens the model spends thinking, presented as a speed-versus-depth knob. Logic tests on NVIDIA's free chatbot (three-legged llama, David's brothers, a students-and-buses problem) mostly pass. The model is then deployed on a rented RunPod A40 pod running vLLM, with a Next.js chat UI connected to it. Coding results are weaker: a bouncing-ball-in-hexagon simulation breaks after the second bounce, and a snake game moves correctly but cannot eat food or grow. The reasoning budget client still solves the logic tasks in very few tokens (78 for the llama question, under 500 for the bus problem). The evidence is one creator's informal tests with no benchmark numbers shown on screen.

## Key ideas
- **Hybrid architecture: few attention layers, rest Mamba-2** — Nemotron Nano v2 keeps only a handful of attention layers and replaces most with Mamba-2 layers, which the speaker says handle long sequences without the quadratic slowdown of attention. He claims similar or better reasoning than attention-heavy Llama 3 or Qwen 3 with far fewer attention layers, and a smaller memory footprint. ([0:00](https://youtu.be/8M5IHvDSZXs?t=0))
- **Reasoning budget control trades speed for depth** — The model exposes a cap on how many tokens it can spend thinking at inference time. The speaker presents this as the way to hold latency down on weaker machines while choosing how deep the reasoning goes. ([1:11](https://youtu.be/8M5IHvDSZXs?t=71))
- **Logic tests mostly pass on NVIDIA's free chatbot** — Three-legged llama, David's brothers, and a students-and-buses optimisation question were answered correctly, with reasoning steps visible in the UI. The bus answer gave alternatives for four buses but prioritised three. The free chatbot has a 2000-token limit, which is too small for coding, so he moved to self-hosting. ([2:13](https://youtu.be/8M5IHvDSZXs?t=133))
- **Coding results are weak, which the speaker admits** — The bouncing-ball-in-rotating-hexagon Python project was missing one wall and the ball escaped after the second bounce. A snake game got movement right but failed on food collision and growth. The speaker concludes it is not in the same class as Claude Code, but notes it is a general reasoning model, not a coding specialist. ([4:45](https://youtu.be/8M5IHvDSZXs?t=285))
- **Reasoning budget keeps logic answers correct at very low token counts** — Using the budget client example from the model card, the three-legged llama question was solved with 78 tokens total, and the harder bus problem was solved under a 500-token limit. The speaker takes this as evidence the model suits tight-resource or strict-latency setups. ([5:45](https://youtu.be/8M5IHvDSZXs?t=345))
- **Deploy from Hugging Face because Ollama did not have the model yet** — At filming time the model was not on Ollama, so the speaker pulled the weights from Hugging Face and served them through vLLM on a rented GPU pod. He positions RunPod as the easy route for anyone without a large local GPU. ([3:25](https://youtu.be/8M5IHvDSZXs?t=205))

## Techniques
- **Serve a Hugging Face model on a RunPod vLLM pod** — 1) On runpod.io, pick a pod (speaker uses an A40). 2) Choose a template for the latest vLLM. 3) Click Edit Template. 4) Change the Container Start command so it points at the Nemotron Nano v2 Hugging Face model ID. 5) Optionally set extra vLLM parameters (the speaker sets some for this model but does not name them on screen). 6) Add a Hugging Face API token. 7) Click Deploy on Demand and wait for RunPod to download the model and expose an HTTP endpoint. *When:* You need a 9B-class model that is not yet on Ollama or your local GPU is too small. Good for quick evaluation rather than production serving.
- **Chat UI on top of a vLLM endpoint** — Run the Next.js vLLM UI project with a single Docker command. Copy the pod's HTTP service link from RunPod and replace the VLLM URL in the command with it. Launch the container and open the UI. *When:* You want a browser chat front end for an OpenAI-compatible vLLM server without writing your own client.
- **Cap thinking with a reasoning budget client** — Use the example client from the Nemotron model card that sets a thinking-token budget on each request. Pick a cap (the speaker used a ~500-token limit for logic problems) and check that answers stay correct. Expect the reasoning block to be cut off at that budget. *When:* Latency or token cost is more important than maximum reasoning depth, for example on modest hardware or in latency-sensitive paths.
- **Quick logic regression prompts** — Test the model with a small set of known tricky logic prompts (three-legged llama, David's brothers, students and buses). The speaker sources them from a public LLM logic-test spreadsheet linked in the description. Compare answers across models. *When:* Shortlisting a small model before a deeper evaluation, as a cheap smoke test for reasoning quality.

## Numbers
- Nemotron Nano v2 has 9 billion parameters ([0:00](https://youtu.be/8M5IHvDSZXs?t=0))
- NVIDIA's free chatbot has a 2000-token limit, too small for coding tasks ([2:13](https://youtu.be/8M5IHvDSZXs?t=133))
- Three-legged llama question solved with 78 tokens total under the reasoning budget client ([5:45](https://youtu.be/8M5IHvDSZXs?t=345))
- Students-and-buses problem solved under a 500-token reasoning budget ([5:45](https://youtu.be/8M5IHvDSZXs?t=345))
- Speaker says Nemotron matches or outperforms Qwen 3 on reasoning, math, and sometimes coding, but no benchmark numbers are shown on screen (the spreadsheet is linked in the description) ([1:11](https://youtu.be/8M5IHvDSZXs?t=71))

## Hot takes
- The speaker calls the model underrated and says NVIDIA, which already controls the hardware stack, could reshape the AI landscape. This is speculation, not evidence.
- Title hype ('quietly dropped', 'POWERFUL') is not matched by the coding results the speaker himself reports as weak.
- Benchmark superiority over Qwen 3 is asserted but not shown; only anecdotal logic prompts are tested.
- Quality capped at 2: hype title and a single informal session with no quantitative evaluation, though the failures are reported honestly.

## Tools mentioned
NVIDIA Nemotron Nano v2 (9B), Mamba-2, vLLM, RunPod, Hugging Face, Ollama, Next.js vLLM UI, NVIDIA chatbot (free web demo), Llama 3, Qwen 3, Claude Code (mentioned for comparison only), Docker

## Relevance to our work
- **agentos** (2/3): Hybrid Mamba-2 plus few-attention models change KV-cache footprint and long-context cost, which is relevant to InferCraft's vLLM and KV-strategy work on the RTX 5090. The reasoning budget is a per-request latency knob the scheduler could use. → *Benchmark Nemotron Nano v2 against a pure-attention 8-9B model on the same vLLM setup, comparing KV-cache memory, tokens/s at long context, and reasoning-budget accuracy, before adding it to InferCraft's model list.*
