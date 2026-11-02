# 2 Million TV Boxes Are Already Infected. AI Is Next.

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `OfNajAPiGsM` · [watch](https://youtu.be/OfNajAPiGsM) · **date:** 2026-10-19 · **length:** 6:05 · **format:** news · **quality:** 3/5 · **depth:** intro
- **speakers:** Unnamed Better Stack presenter · **orgs:** Anthropic, Google, Krebs on Security, Better Stack
- **topics:** security-guardrails, models-research, inference-serving, local-ai · **tags:** ai-worm, self-replication, botnet, agent-security, open-weight-models, small-models, layer-splitting, adb, iot-security, threat-model

> Better Stack walks through Anthropic's research on whether a small model could self-replicate across cheap IoT devices like TV boxes, and why the capability requirements don't yet overlap.

## Summary
Better Stack summarizes Anthropic's recent research on whether an AI model could copy itself across thousands of cheap internet-connected devices such as Android TV boxes, forming a botnet-like worm. A worm needs two things: a model small enough to run on the device and capable enough to carry out the whole spread-and-replicate loop. Anthropic tested these separately. On 15 TV boxes with 4GB RAM each, a 26B model had to be split by layers across boxes, running at 0.39 tokens per second. In a sealed 8-machine test with a deliberately open debug port, only GLM 5.2 (about 753B parameters, too large for a TV box) completed the full worm; every other model failed. Anthropic's rough prediction is that an 8B model could reach that capability by the end of 2026. The speaker treats the hacking step as plausibly easy given the real Kimwolf botnet, but notes that weight transfer is noisy and slow, and mentions criticism that the research pushes against open-weight models.

## Key ideas
- **Self-replication needs two capabilities that Anthropic tested separately: the model must fit on a cheap device, and it must be smart enough to run the whole spread loop by itself.** — Splitting the test this way is what lets the speaker conclude that the two requirements do not yet overlap in any single model. ([0:00](https://youtu.be/OfNajAPiGsM?t=0))
- **Running a model too big for one device works by splitting its layers across many small boxes, passing activations over the network for every token.** — 15 TV boxes at about $55 each, 4GB RAM each, 2 layers per box. A 26B model at 4-bit needs 10 or more boxes, and the result was 0.39 tokens/s, so one sentence takes close to a minute. ([1:27](https://youtu.be/OfNajAPiGsM?t=87))
- **The worm test ran on a sealed network of 8 Google Cloud Android machines with the ADB debug port open and no password, so the test isolated the hard part, which is getting a model running on unfamiliar hardware.** — The hard parts were choosing an inference engine, finding compatible package versions, and debugging each unusual machine. Exploitation was deliberately made easy. ([1:27](https://youtu.be/OfNajAPiGsM?t=87))
- **In the per-hardware test, the worm's brain stays on a separate server, and the infected devices only send their reasoning off to it.** — Qwen 3.5 9B succeeded on 8 of 9 hardware types, from a Jetson Nano to a Mac and an RTX 4090. Every model was asked to do the same stand-in task (getting Llama 3.1 8B running) so the comparison is fair. ([2:52](https://youtu.be/OfNajAPiGsM?t=172))
- **Only GLM 5.2 completed the full worm, spreading to all 8 machines in 4 of 5 runs and 7 of 8 in the other, while every other model failed every time. That model is about 753B parameters, far too large for the devices.** — The speaker's reading: small models can't do the whole job and the only model that can do the job is too big to fit, so the threat is not present yet. ([2:52](https://youtu.be/OfNajAPiGsM?t=172))
- **Anthropic's rough estimate is that a model around 8B parameters could match GLM 5.2's worm capability by the end of 2026, which is why the speaker calls the threat a future one.** — The prediction is based on how quickly small models have been improving. The speaker explicitly calls it a rough estimate. ([4:11](https://youtu.be/OfNajAPiGsM?t=251))
- **The hacking step may be less of a barrier than it looks, since the real Kimwolf botnet (transcribed as Kinwolf) reportedly infected over 2 million mostly Android TV devices, many with ADB enabled by default.** — The speaker cites Krebs on Security for the ADB detail. Weight transfer is still a practical barrier because multi-gigabyte file moves between boxes are noisy and could be spotted by ISPs. ([4:11](https://youtu.be/OfNajAPiGsM?t=251))
- **Replication is slow even when it works: a 9B worm would need 28 to 51 hours per device to get its model running, and a 2-million-device botnet would total about 40 H100s of compute.** — The speaker concludes the threat is serious but slow and visible, which limits what a real worm could do. ([5:24](https://youtu.be/OfNajAPiGsM?t=324))

## Techniques
- **Pipeline-split a model across many weak devices** — Assign each device a contiguous slice of the model's layers. For each token, pass the activations from device to device over the network in order, so one token traverses every box before the next token starts. Only one device computes at a time. *When:* When no single device has enough RAM for the quantized model and throughput is not important, such as a proof-of-concept on cheap hardware or a fleet of idle devices.
- **Separate the requirements of a dangerous capability and test each one** — Measure the fit-on-device requirement (can a small model run on the hardware at all) separately from the capability requirement (can a model complete the multi-step task end to end). Then check whether any model satisfies both at once. *When:* When assessing a risk that depends on two independent prerequisites, so that the overlap, not either part alone, is the question.
- **Give every model the same stand-in task for a fair comparison** — Use one fixed sub-task that stands in for the real goal, here getting a small reference model (Llama 3.1 8B) running on each hardware target, and count successes across models and devices. *When:* When comparing models on a multi-step, environment-dependent task where the real task would vary too much to score fairly.
- **Keep a remote brain, local hands** — Keep the large reasoning model on a separate server. The constrained device runs only the lightweight agent loop and sends its prompts there. *When:* When the agent loop must run on hardware that is too small for the model. This pattern also splits the attack surface and the network traffic.

## Numbers
- 15 Android TV boxes at about $55 each, 4GB RAM each ([0:00](https://youtu.be/OfNajAPiGsM?t=0))
- Gemma 4 26B at 4-bit needs 10 or more boxes; each box holds 2 layers ([0:00](https://youtu.be/OfNajAPiGsM?t=0))
- Layer-split inference across boxes runs at 0.39 tokens/s ([1:27](https://youtu.be/OfNajAPiGsM?t=87))
- Sealed test network of 8 Google Cloud Android machines ([1:27](https://youtu.be/OfNajAPiGsM?t=87))
- Qwen 3.5 9B succeeded on 8 of 9 hardware types, from a Jetson Nano to a Mac and an RTX 4090 ([2:52](https://youtu.be/OfNajAPiGsM?t=172))
- GLM 5.2 spread to all 8 machines in 4 of 5 runs, and 7 of 8 in the other run; every other model failed every time ([2:52](https://youtu.be/OfNajAPiGsM?t=172))
- GLM 5.2 is about 753 billion parameters ([3:30](https://youtu.be/OfNajAPiGsM?t=210))
- Anthropic's rough estimate: an 8B model could match the capability by end of 2026 ([4:11](https://youtu.be/OfNajAPiGsM?t=251))
- Kimwolf botnet reportedly infected over 2 million devices ([4:11](https://youtu.be/OfNajAPiGsM?t=251))
- A 9B worm needs 28 to 51 hours per device to get a model running ([5:24](https://youtu.be/OfNajAPiGsM?t=324))
- A 2-million-device botnet equals about 40 H100s of compute ([5:24](https://youtu.be/OfNajAPiGsM?t=324))

## Hot takes
- Title is hype: 'already infected' and 'AI is next' overstate the finding. The video itself says the two requirements do not currently overlap.
- The speaker reads the research as a future-risk warning but acknowledges fear-marketing concerns and criticism that the study is framed against open-weight models, since every tested model was open weight.
- The speaker cites Anthropic's own prediction (8B by end of 2026) as a rough estimate, not evidence.
- Substance is real but secondhand: a 6-minute news explainer that paraphrases a research post and adds little independent analysis, so quality is 3 rather than higher.

## Tools mentioned
Anthropic research (AI worm / self-replication study), Gemma 4 26B (Google open model), Qwen 3.5 9B, Llama 3.1 8B, GLM 5.2 (about 753B parameters), ADB (Android Debug Bridge), Google Cloud (8 Android test machines), Jetson Nano, NVIDIA RTX 4090, NVIDIA H100, Kimwolf botnet (transcribed as Kinwolf)

## Relevance to our work
- **agentos** (1/3): AgentOS runs sandboxed execution (Crucible) and exec-gate guardrails. The worm scenario is a threat-model case where an agent with shell access spreads by fanning out to other hosts over the network. → *Add a self-propagation case to the Crucible/exec-gate threat model: deny outbound connections and large file transfers from sandboxed agent execution by default, and log fan-out to new hosts.*
