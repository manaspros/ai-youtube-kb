# Accelerating AI on Edge — Chintan Parikh and Weiyi Wang, Google DeepMind

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Lm8BLHkxiAo` · [watch](https://youtu.be/Lm8BLHkxiAo) · **date:** 2026-05-18 · **length:** 23:58 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Chintan Parikh, Weiyi Wang · **orgs:** Google DeepMind, Google AI Edge, Qualcomm, MediaTek, Hugging Face
- **topics:** local-ai, inference-serving, models-research · **tags:** on-device, edge-ai, LiteRT, TensorFlow Lite, Gemma 4, NPU, quantization, function-calling, structured-output, agent-skills, Raspberry Pi, AI Edge Portal

> Google DeepMind's pitch for running Gemma 4 E2B/E4B agents on-device through LiteRT, with the conversion, quantization, device-benchmarking and NPU path laid out and vendor speed claims.

## Summary
Chintan Parikh (PM for LiteRT, Google AI Edge) and Weiyi Wang present on-device AI with Gemma 4's 2B and 4B edge models. The talk argues that the models are now aimed at agents rather than chat, with built-in function calling, native structured JSON output and a thinking mode. The speakers motivate edge deployment by latency, privacy, offline use and token cost, and suggest a hybrid split with cloud. They demo on-device skills such as a Wikipedia lookup and a mood-trend tracker in the Google AI Edge Gallery app, which is open source and supports user-written skills. On the framework side, LiteRT (formerly TensorFlow Lite) is presented as the runtime, accepting PyTorch and JAX models converted to its format, with quantization, Model Explorer for graph inspection, and a cloud device lab for fleet benchmarking. They close with NPU integrations (Qualcomm, MediaTek) and vendor performance numbers, most of them without stated benchmark conditions.

## Key ideas
- **Gemma 4 E2B/E4B are pitched as agent models, not chatbots** — The speakers position the edge models around autonomy, reasoning and tool use rather than chat. Function calling is built in, so the model can call external APIs while inference stays on the device. ([0:56](https://youtu.be/Lm8BLHkxiAo?t=56))
- **Edge is a hybrid-cost and privacy argument** — Latency (real-time camera, video calls), privacy for sensitive documents, offline use and token cost are the reasons given. Running some work on device and the rest in the cloud is framed as the way to balance cost against capability. ([2:13](https://youtu.be/Lm8BLHkxiAo?t=133))
- **Structured output and thinking mode are in the model, not the prompt** — Native structured JSON output is said to be part of the architecture rather than achieved through prompt engineering. A thinking mode exposes the model's reasoning steps and is visible in the Gallery app. ([4:29](https://youtu.be/Lm8BLHkxiAo?t=269))
- **Full agent skills run on device in the Gallery app** — Demos include a Wikipedia-query skill and a skill that tracks sleep and mood trends over seven days, plus image understanding and sound generation. Skills can be written inside the app, and community skills are shared on GitHub. ([7:09](https://youtu.be/Lm8BLHkxiAo?t=429))
- **LiteRT is the runtime; models come in via conversion** — LiteRT is built on TensorFlow Lite and keeps the TFLite format. PyTorch and JAX models are converted to it, which the speakers say is why the rebrand happened. The format is said to run on Android, iOS, macOS, Linux, Windows, web and IoT. ([11:10](https://youtu.be/Lm8BLHkxiAo?t=670))
- **Ship pipeline: convert, quantize, inspect the graph, then benchmark on a device fleet** — Conversion and quantization come first, with Model Explorer used to study the graph and pick mixed precision. The cloud AI Edge Portal benchmarks across many devices, which informs the choice between ahead-of-time and just-in-time compilation for a broad fleet. ([13:51](https://youtu.be/Lm8BLHkxiAo?t=831))
- **NPU acceleration is the main performance lever** — CPU and GPU support is described as universal. NPU integrations with Qualcomm and MediaTek are complete, and the speakers say more partners are coming. For camera or AR-style real-time work they expect the NPU to matter most. ([15:57](https://youtu.be/Lm8BLHkxiAo?t=957))
- **Hybrid split with a small local model gating a larger remote one** — In Q&A the speakers describe architectures where a small local model or classifier handles work on the device and an orchestrator decides what runs locally and what goes elsewhere. They gave no concrete examples of this. ([21:46](https://youtu.be/Lm8BLHkxiAo?t=1306))

## Techniques
- **Hybrid local-plus-remote inference via function calling** — Keep inference on device, and let the model call external APIs through its built-in tool calling. The speakers say the core inference stays local and only the tool calls go outside. *When:* Latency-sensitive, privacy-sensitive or offline features where some data must not leave the device.
- **Use native structured JSON output instead of prompt-only formatting** — Request structured output that the model supports natively, rather than relying on prompt instructions to produce JSON. *When:* Small on-device models that must return machine-parseable results to other code.
- **Packaging capabilities as user-authored skills** — Each on-device capability is a skill that can be written in-app, loaded, and shared (the speakers point to a GitHub repo of community skills and a guide linked by QR code, not in the transcript). *When:* When you want a non-developer-friendly way to extend an on-device agent.
- **Bring-your-own-model conversion with graph inspection** — Convert PyTorch or JAX models to the TFLite format, quantize, then use Model Explorer to inspect the graph and choose mixed-precision settings per layer. *When:* Deploying an open-weight model that is not already in an edge-ready format.
- **Fleet-benchmark before shipping** — Run the converted model on a cloud device lab (AI Edge Portal) across many Android devices, then pick AOT or JIT compilation based on the results. *When:* Shipping to a broad, mixed device fleet where older phones may fail.
- **Small local model as a gate in a split architecture** — Use a very small model or classifier on the device to decide whether a request is handled locally or sent to a larger model elsewhere. *When:* You want to cut cloud calls while keeping a cloud fallback for hard requests.

## Numbers
- Gemma 3 family goes down to 270M parameters, for fine-tuning small models ([0:56](https://youtu.be/Lm8BLHkxiAo?t=56))
- Gemma 4 E2B needs roughly 1-2 GB RAM once quantized (speaker estimate); E4B needs more and targets laptops or IoT ([2:13](https://youtu.be/Lm8BLHkxiAo?t=133))
- LiteRT is used in 100,000+ apps with billions of active users, per the speakers ([11:10](https://youtu.be/Lm8BLHkxiAo?t=670))
- NPU acceleration gives at least 3-10x performance improvement (speaker estimate for real-time camera or AR workloads) ([15:57](https://youtu.be/Lm8BLHkxiAo?t=957))
- Up to 13x boost on some new accelerators and NPUs (vendor figure, no benchmark conditions given) ([19:08](https://youtu.be/Lm8BLHkxiAo?t=1148))
- Roughly 56 tokens per second on iOS (speaker did not name the model or device) ([19:08](https://youtu.be/Lm8BLHkxiAo?t=1148))
- Mobile runtime up to 35x faster than Llama; desktop at par; IoT about 3x (vendor claims, conditions not stated) ([19:08](https://youtu.be/Lm8BLHkxiAo?t=1148))

## Hot takes
- On-device agents with function calling and structured output are now practical for phone-class hardware, per the Gemma 4 E2B pitch.
- Vendor speed claims (35x vs Llama on mobile, 13x on NPUs) are presented without benchmark conditions, so treat them as marketing until reproduced.
- Real-time camera, privacy and offline features favour on-device inference, and the speakers frame the hybrid split as the way to cut token spend.

## Tools mentioned
LiteRT, TensorFlow Lite, LiteRT-LM, Gemma 4, Gemma 3, Model Explorer, AI Edge Portal, Google AI Edge Gallery app, Hugging Face, Core ML, Raspberry Pi, Qualcomm NPU, MediaTek NPU, Llama (comparison target)

## Relevance to our work
- **agentos** (1/3): The hybrid local-versus-cloud routing idea could inform the L1 strategy router, but the talk is edge-device focused and gives no independent numbers that apply to the single-box RTX 5090 setup. → *Consider a small local model as a routing target in the Govrix strategy router for latency- or privacy-sensitive calls, and benchmark it before deciding anything.*
