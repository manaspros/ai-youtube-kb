# Running LLMs on your iPhone: 40 tok/s Gemma 4 with MLX — Adrien Grondin, Locally AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `a2muGkT4WD4` · [watch](https://youtu.be/a2muGkT4WD4) · **date:** 2026-05-18 · **length:** 10:51 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** Adrien Grondin · **orgs:** Locally AI, LM Studio, Apple, Hugging Face
- **topics:** local-ai, inference-serving · **tags:** on-device, MLX, Apple Silicon, iPhone, quantization, Gemma 4, mlx-swift-lm, Hugging Face, LM Studio, tool calling, Shortcuts

> Adrien Grondin (Locally AI) shows how to run quantized Gemma 4 on iPhone with Apple's MLX, covering the mlx-swift-lm package, picking quantized weights, and speed on phones.

## Summary
The speaker is the developer of Locally AI, an iPhone/iPad/Mac chatbot that runs on-device models with MLX, Apple's framework for Apple Silicon. He says a Gemma 4 model quantized to 4-bit runs at about 40 tokens per second on the latest iPhone, and that around 20 tokens per second is still useful on older phones. For developers, the path is the mlx-swift-lm package inside an iOS/macOS app, which loads a model directly by its Hugging Face ID. He recommends the mlx-community organization on Hugging Face, which posts pre-quantized weights (often within about 30 minutes of a release), and advises staying between 4-bit and 8-bit because quality drops noticeably below 4-bit. He names the model download size (roughly 1 to 3 GB) as the main barrier for users. He says tool calling works in mlx-swift-lm but structured generation does not yet. He also mentions that small on-device models (a Liquid model he describes as about 350 parameters) can power text-processing automations in Apple Shortcuts. The talk ends with a short note that LM Studio acquired Locally AI, and that LM Studio can serve local models over an OpenAI- or Anthropic-compatible server to compare MLX and llama.cpp engines. The talk is a short demo-driven intro with some product promotion.

## Key ideas
- **MLX is Apple's framework for running models on Apple Silicon, and the same stack covers iPhone, iPad and Mac.** — Locally AI is built on MLX, so the app runs models fully on-device. The speaker says the stack is tuned for the chips in these devices. ([0:47](https://youtu.be/a2muGkT4WD4?t=47))
- **Integrating on-device models into a Swift app is quick with mlx-swift-lm.** — The speaker says a working iOS app with a locally running model can take under 10 minutes using this package. Python and macOS users can use mlx-lm, mlx-vlm, and mlx-audio instead. ([1:59](https://youtu.be/a2muGkT4WD4?t=119))
- **Pick pre-quantized weights from the mlx-community Hugging Face org instead of quantizing yourself.** — The speaker says new models usually appear there in several quantized versions, often about 30 minutes after release. You pass the model ID to the framework and it downloads the weights. ([3:14](https://youtu.be/a2muGkT4WD4?t=194))
- **Quantization level is a quality trade-off: stay between 4-bit and 8-bit.** — Full-size weights are too large for phones. The speaker says quality starts to drop noticeably below 4-bit, so 4-bit is his lower bound and 8-bit is his upper bound for small models. ([4:27](https://youtu.be/a2muGkT4WD4?t=267))
- **Gemma 4 at 4-bit is fast enough on a current iPhone for interactive chat.** — He reports about 40 tokens per second, shown live offline with streaming output. He says a non-streaming UI that waits a few seconds also works for long outputs. ([5:39](https://youtu.be/a2muGkT4WD4?t=339))
- **Model download size, not speed, is the main barrier for end users.** — Models are roughly 1 to 3 GB. The speaker expects this to improve as models get smaller and phones get faster. ([6:39](https://youtu.be/a2muGkT4WD4?t=399))
- **Tool calling works on-device, but structured generation is not supported yet.** — In Q&A he says mlx-swift-lm supports tool calling and models have improved at it. Structured generation is not supported in the package and he points to third-party packages. ([8:02](https://youtu.be/a2muGkT4WD4?t=482))
- **Very small local models are useful for automation rather than chat.** — He describes a small Liquid model he calls 350 parameters that runs fast enough in Shortcuts for text processing steps. ([4:27](https://youtu.be/a2muGkT4WD4?t=267))

## Techniques
- **Load quantized models by Hub ID in an on-device Swift app** — Add the mlx-swift-lm package to the app, then pass a Hugging Face model ID from the mlx-community org. The framework downloads the weights and runs them locally. *When:* Shipping a private, offline chat or text feature in an iOS, iPadOS or macOS app.
- **Choose quantization between 4-bit and 8-bit** — Start from a 4-bit build for speed on phones. Move up to 8-bit for small models if quality matters more, and avoid going below 4-bit where quality drops. *When:* Fitting a model into phone memory and latency budget while keeping output usable.
- **Stream tokens to the UI** — Show streamed output so users see tokens as they arrive at about 40 tok/s, or wait for the full answer when outputs are long and streaming adds no value. *When:* Building UI on top of on-device generation with variable output length.
- **Small local model for automation steps** — Use a very small model in a system automation tool such as Shortcuts for text processing steps, not for open-ended chat. *When:* Doing fast, cheap text transforms on the device.
- **Compare inference engines via a local server** — Run LM Studio, load the same model in MLX and llama.cpp builds, and open its local server so an app can point at it through an OpenAI- or Anthropic-compatible API. *When:* Benchmarking engines or testing an app against a local model before moving to a hosted endpoint.

## Numbers
- Gemma 4 at 4-bit runs at about 40 tokens per second on the latest iPhone, streaming, offline (speaker's live demo). ([5:39](https://youtu.be/a2muGkT4WD4?t=339))
- Speaker says about 20 tokens per second on older iPhones is still useful (estimate, not a measurement shown). ([6:39](https://youtu.be/a2muGkT4WD4?t=399))
- Quantized models are typically about 1 to 3 GB to download, which the speaker calls the biggest barrier. ([6:39](https://youtu.be/a2muGkT4WD4?t=399))
- Speaker recommends quantization between 4-bit and 8-bit; below 4-bit output quality drops noticeably. ([4:27](https://youtu.be/a2muGkT4WD4?t=267))
- The mlx-community org hosts almost 4,000 to 5,000 models, and new ones appear about 30 minutes after release. ([3:14](https://youtu.be/a2muGkT4WD4?t=194))
- A working iOS app with an on-device model can be set up in under 10 minutes (speaker's estimate). ([1:59](https://youtu.be/a2muGkT4WD4?t=119))

## Hot takes
- Quantizing below 4-bit makes small models not worth using, so 4-bit is the floor.
- On-device LLMs are already fast enough for interactive chat on current phones, and model size is now the main barrier.
- Integrating an on-device model into a Swift app is easy enough to hand to a coding agent.

## Tools mentioned
MLX, mlx-swift-lm, mlx-lm, mlx-vlm, mlx-audio, Hugging Face, mlx-community, LM Studio, llama.cpp, Apple Shortcuts, Gemma 4, Qwen, Liquid models

## Relevance to our work
- **agentos** (1/3): AgentOS InferCraft targets vLLM on one RTX 5090, not phones, so this talk only touches its quantization trade-off and local-engine comparison. → *When choosing quantized weights for InferCraft tests, reuse the speaker's 4-bit floor as a quality check, and compare MLX vs llama.cpp only if a local-model baseline is needed.*
