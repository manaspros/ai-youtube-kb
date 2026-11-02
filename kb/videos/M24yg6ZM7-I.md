# I Can't Believe This AI Model Fits in 14 Megabytes (Needle 2)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `M24yg6ZM7-I` · [watch](https://youtu.be/M24yg6ZM7-I) · **date:** 2026-09-02 · **length:** 9:54 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Andrus · **orgs:** Cactus Compute, Better Stack
- **topics:** local-ai, models-research, inference-serving · **tags:** tiny-llm, tool-calling, function-calling, edge-ai, esp32, microcontroller, 2-bit-quantization, quantization-aware-training, hadamard-transform, on-device-inference

> Hands-on demo of Needle 2, a 45M-parameter, 14 MB tool-call dispatcher from Cactus Compute running offline on an ESP32-S3 microcontroller; it maps natural language to predefined device actions, not general chat.

## Summary
Andrus from Better Stack tests Needle 2, a 45-million-parameter model in a 14 MB file that Cactus Compute released under Apache 2.0. The model is built only as a tool-call dispatcher: you predefine a set of actions, and it picks the right function and arguments from a natural-language prompt. It was trained on device actions (smart home, mobile, wearable) and cannot answer general questions such as "what is the capital of France." The speaker attributes the size to a few architecture changes: hashed lookup tables ("engram") in place of some weight matmuls, a fixed Hadamard transform in place of learned mixing layers, and training natively at 2-bit precision rather than quantizing afterward. He reports Cactus's own benchmarks showing it matching or beating a model five times its size on some tool-calling tests and picking the correct function name 98.3% of the time on a mobile-actions benchmark. He then runs his own inference engine and TUI on an ESP32-S3 with an 8 MB RAM budget, where a light-control call takes about 40 seconds at roughly 1.86 tokens per second, and each output comes with a confidence score (0.46 to 0.57 in the demos). The out-of-scope prompt correctly produced an empty tool call, and the speaker notes the project is reusable: swap the command set by following a three-step README process.

## Key ideas
- **Needle 2 is a tool-call dispatcher, not a chatbot** — You predefine a set of device actions and the model maps a natural-language request to the right function and arguments. It was trained only on smart-home, mobile and wearable actions, so it cannot answer general knowledge questions even on fast hardware. ([0:46](https://youtu.be/M24yg6ZM7-I?t=46))
- **Size comes from replacing weight matmuls with lookup tables and fixed transforms** — Per the speaker, part of the knowledge lives in hashed lookup tables that are read rather than multiplied, and the learned MLP mixing is replaced by a fixed Hadamard transform, which spends no parameters on learning the mixing. ([2:53](https://youtu.be/M24yg6ZM7-I?t=173))
- **Trained at 2 bits, not quantized afterward** — The speaker says Needle 2 runs at two bits per weight and was trained against its own compression from the start. He contrasts this with small models that degrade under post-training quantization. ([2:53](https://youtu.be/M24yg6ZM7-I?t=173))
- **Vendor benchmarks claim parity with much larger models** — Cactus reports Needle 2 matching a model five times its size and beating it on some harder tool-calling tests, despite the 2-bit weights versus the comparison model's 16-bit. The speaker presents these as the vendor's own numbers. ([4:21](https://youtu.be/M24yg6ZM7-I?t=261))
- **Confidence score makes the output gateable** — Each tool call comes with a confidence score (0.57 for the purple-light prompt, 0.46 for the yellow one). The speaker suggests branching device behavior on this score, and notes the correct outputs still came with low scores. ([5:47](https://youtu.be/M24yg6ZM7-I?t=347))
- **Out-of-scope prompts yield an empty call** — Asked for the capital of France, the model reasoned that no country-facts tool existed and produced an empty tool call with high confidence. This is the behavior you want from a closed action set. ([5:47](https://youtu.be/M24yg6ZM7-I?t=347))
- **Reusable by swapping the command set** — The speaker built the project to be reusable: replace the flashing-light commands with your own (e.g. servo actions) by following a three-step process documented in the README. ([8:08](https://youtu.be/M24yg6ZM7-I?t=488))

## Techniques
- **Closed-action-set tool dispatch on a small model** — Predefine the executable operations (for example light color, mode and duration). Prompt the model in natural language; it reasons briefly about color, mode and duration, then writes the tool call. Require an explicit no-tool outcome for out-of-scope requests. *When:* Embedded or robotics control where the action space is fixed and latency and memory are tight, and a general chat model is overkill.
- **Gate actions on the dispatcher's confidence score** — Read the per-call confidence the model reports. The speaker suggests programming different device behavior by score band; for example, execute high-confidence calls directly and ask for confirmation below a threshold. *When:* Any agent that turns model output into physical or irreversible actions and needs a cheap pre-check before executing.
- **Native low-bit training instead of post-training quantization** — Per the speaker, Needle 2 was trained against its 2-bit compression from the start (not quantized after training), which he credits for the model still working at 14 MB. He does not show the training recipe. *When:* When the target device has a hard memory budget and a model compressed after training is expected to degrade.
- **Reuse the demo engine by swapping commands** — Keep the inference engine and TUI, replace the predefined action list with your own commands, and follow the three-step README process the speaker describes. The steps themselves are not spoken in the video, so check the repo. *When:* Prototyping a natural-language control layer for your own device or action set.

## Numbers
- Model is 14 MB with 45 million parameters, Apache 2.0 ([0:00](https://youtu.be/M24yg6ZM7-I?t=0))
- Up to 500 tokens/s on a Raspberry Pi 5 (speaker's figure) ([0:46](https://youtu.be/M24yg6ZM7-I?t=46))
- Cactus benchmarks: matches a model 5x its size and beats it on some harder tool-calling tests; 2-bit weights vs the comparison's 16-bit ([4:21](https://youtu.be/M24yg6ZM7-I?t=261))
- Picks the correct function name 98.3% of the time on the mobile actions benchmark, highest of the models compared ([4:21](https://youtu.be/M24yg6ZM7-I?t=261))
- Red-light tool call took about 39 seconds on the ESP32-S3 (8 MB microcontroller, no GPU) ([5:47](https://youtu.be/M24yg6ZM7-I?t=347))
- Confidence scores 0.57 (purple light) and 0.46 (yellow light); average about 1.86 tokens/s and about 40 seconds per tool call on the board ([7:00](https://youtu.be/M24yg6ZM7-I?t=420))
- Board cost about $10 ([9:12](https://youtu.be/M24yg6ZM7-I?t=552))

## Hot takes
- Title overstates it: the model only dispatches a fixed action set, so it is a narrow edge-control model, not a general small LLM.
- All accuracy and size-parity numbers are Cactus's own benchmarks; the video does not reproduce them.
- The on-device demo is a single-prompt, hand-picked run at about 40 seconds per call and 1.86 tokens/s, so it shows feasibility rather than production latency.
- Confidence scores were low (0.46 to 0.57) even for correct outputs, which weakens using them as a hard gate without calibration.

## Tools mentioned
Needle 2 (Cactus Compute, Apache 2.0), ESP32-S3, Raspberry Pi 5, LFM 2.5 (comparison model in Cactus benchmarks, as spoken), Custom inference engine and TUI (speaker's own, GitHub link in description)

## Relevance to our work
- **agentos** (1/3): A tiny closed-action dispatcher is a possible cheap pre-router in front of tool calls, which fits the cheap-model pipeline interest, but the video shows no evaluation against the model we would otherwise use. → *Benchmark a Needle-class tiny tool-router against Haiku on our own tool-selection set, measuring function-name accuracy and empty-call behavior for out-of-scope prompts.*
- **prosharness** (1/3): Confidence-gated action execution is a small idea that could map onto ProsHarness's phone-driven approvals: auto-run high-confidence tool calls and route low-confidence ones to approval. → *Sketch a confidence-threshold policy for ProsHarness approvals, using the model's self-reported confidence only after checking its calibration on logged decisions.*
