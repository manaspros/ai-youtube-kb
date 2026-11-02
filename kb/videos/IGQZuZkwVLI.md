# Apple Hasn’t Put an LLM on Your Watch. So I Did.

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `IGQZuZkwVLI` · [watch](https://youtu.be/IGQZuZkwVLI) · **date:** 2026-10-02 · **length:** 11:33 · **format:** demo · **quality:** 3/5 · **depth:** intro
- **speakers:** Andres (Better Stack) · **orgs:** Better Stack, Apple
- **topics:** local-ai, inference-serving, dev-tools · **tags:** apple-watch, watchos, llama.cpp, gguf, on-device-inference, state-space-model, mamba-2, core-ml, arm64_32, tool-calling, edge-llm, small-models

> Better Stack runs a 90M-parameter hybrid LLM offline on a 2020 Apple Watch Series 6 via llama.cpp built for watchOS, and explains the ARM64_32 and Core ML limits that shape the port.

## Summary
The speaker gets Falcon H1 (90M parameters, 57 MB GGUF) and a 135M "small M2" model running fully offline on an Apple Watch Series 6, streaming roughly 15 tokens/s on average, with tool calls (Wikipedia, weather) and voice input. He explains why Core ML fails for this model: Falcon H1 runs Mamba-2 state-space layers alongside attention, and Core ML has no scan primitive and wants a fixed graph. llama.cpp does build for watchOS with a few build flags and a one-line source guard, even though watchOS is missing from its official Apple build script. He clarifies that watchOS uses ARM64_32, which keeps the full 64-bit instruction set and NEON but has 32-bit addresses, capping addressable memory near 2 GB regardless of quantization. The demo reports 24 tok/s for Falcon H1 and 14 tok/s for the 135M model, with throughput falling from about 20 to 10 tok/s on long answers as memory fills. The project is in a GitHub repo linked from the video, with models dropped into a models folder. The video is a hobbyist demo with no benchmarks beyond a few tokens/s readings, and the closing question about why Apple has not shipped a general local model is opinion.

## Key ideas
- **Small hybrid LLMs can run offline on a six-year-old watch.** — Falcon H1 (90M params) runs fully on the watch with no cloud streaming, averaging about 15 tokens/s, and supports tool calls and voice prompts. ([0:00](https://youtu.be/IGQZuZkwVLI?t=0))
- **Compute gap versus the earlier Raspberry Pi 1 test is about 50x.** — The Pi 1 managed about 0.3 tokens/s with one 700 MHz core and 512 MB RAM. The Series 6 has two 1.8 GHz cores and 1 GB RAM. The speaker says the result beat his expectations. ([1:10](https://youtu.be/IGQZuZkwVLI?t=70))
- **Core ML cannot convert Falcon H1 because it has no state-space building block.** — Falcon runs attention and Mamba-2 scan layers in parallel. Core ML only converts attention and expects a fixed graph, while the scan loop length depends on conversation length. Carrying state manually risks silently wrong numbers. ([2:07](https://youtu.be/IGQZuZkwVLI?t=127))
- **llama.cpp runs on watchOS with only build flags and a one-line source guard.** — The official build script covers macOS, iOS, tvOS and visionOS but not watchOS. The speaker found no documented prohibition and got it working anyway. ([4:19](https://youtu.be/IGQZuZkwVLI?t=259))
- **ARM64_32 keeps the full 64-bit ISA but limits addresses to 32 bits.** — NEON and the math speed match other ARM chips. The 32-bit address space tops out around 2 GB, so no model size is reachable on the watch, however aggressively it is quantized. Falcon at 57 MB is well under that. ([4:19](https://youtu.be/IGQZuZkwVLI?t=259))
- **Model choice is a folder drop and a file rename, not a port.** — GGUF files go into a models folder in the Xcode project. Renaming the tools sample file registers the tool calls. Users can edit that file to add or remove tools. ([7:01](https://youtu.be/IGQZuZkwVLI?t=421))
- **Throughput degrades on long generations because memory fills.** — Speed drops from about 20 tokens/s to about 10 during a long depth-first search explanation. The speaker judges the watch unsuitable for long multi-paragraph answers. ([9:17](https://youtu.be/IGQZuZkwVLI?t=557))
- **Location is hardcoded in the weather tool, a shortcut the speaker flags.** — The demo hardcodes Ottawa to avoid adding a location permission. He says real apps should read the current location. ([8:07](https://youtu.be/IGQZuZkwVLI?t=487))

## Techniques
- **Build llama.cpp for watchOS (ARM64_32)** — Use the ARM64_32 target and the watchOS build flags, which the speaker says differ from the stock Apple build script. The exact flags are shown on screen only and are not in the transcript. Add a one-line guard in the source for the watchOS case. The repo linked in the description already has a compiled build. *When:* When you want llama.cpp on a watchOS target, or any Apple target missing from the stock build script.
- **Check the 32-bit address ceiling before picking a model** — Under ARM64_32, addressable memory is about 2 GB. Quantization does not lift that ceiling, so reject models whose footprint, including KV cache, exceeds it before tuning. *When:* When sizing models for any 32-bit-pointer target such as a watch.
- **Prefer small hybrid SSM models for memory-bounded edge devices** — The speaker says the hybrid attention plus Mamba-2 design keeps memory constant per token, unlike attention. Falcon H1 at 90M and 57 MB is the example. Core ML lacks an SSM primitive, so the runtime needs a custom path such as llama.cpp. *When:* When the target is a tiny device with a fixed memory budget and the runtime must handle a state-space layer.
- **Register tools by renaming a samples file** — The project ships a tools samples file. Renaming it to tools registers the sample tool calls (Wikipedia lookup, weather). Edit that file to add or remove tools. *When:* When you want a quick on-device tool-calling demo with no extra wiring.
- **Voice as the input channel on a wearable** — Use the watch's own speech input, then tap Done and Ask to send the prompt. The speaker says this makes prompting easy on a device without a keyboard. *When:* When the device has a microphone and no practical keyboard.

## Numbers
- Falcon H1 model size is 90M parameters, file size 57 MB ([0:00](https://youtu.be/IGQZuZkwVLI?t=0))
- Average streaming speed on the Series 6 is about 15 tokens/s ([0:00](https://youtu.be/IGQZuZkwVLI?t=0))
- Series 6 is about 50x faster than the Raspberry Pi 1 test, which ran at about 0.3 tokens/s ([1:10](https://youtu.be/IGQZuZkwVLI?t=70))
- Pi 1: single 700 MHz core, 512 MB RAM. Series 6: two 1.8 GHz cores, 1 GB RAM ([1:10](https://youtu.be/IGQZuZkwVLI?t=70))
- ARM64_32 32-bit addresses cap usable memory at about 2 GB ([5:39](https://youtu.be/IGQZuZkwVLI?t=339))
- Falcon H1 runs at 24 tokens/s on a simple factual question ([8:07](https://youtu.be/IGQZuZkwVLI?t=487))
- 135M model runs at 14 tokens/s on the same question because it is larger ([8:07](https://youtu.be/IGQZuZkwVLI?t=487))
- On a long depth-first search explanation, throughput fell from about 20 tokens/s to about 10 tokens/s ([9:17](https://youtu.be/IGQZuZkwVLI?t=557))

## Hot takes
- Apple has not shipped a general-purpose on-device LLM on Apple Watch, despite having capable hardware and a neural engine (speaker's view).
- The name ARM64_32 suggests a cut-down ARM. The speaker argues it is full 64-bit ARM with only 32-bit addressing, so the math is not slower.
- The industry is stable enough for on-device LLMs, and device makers are being overly hesitant (speaker's opinion, not evidence).

## Tools mentioned
Falcon H1 (90M, hybrid attention + Mamba-2), small M2 135M model (caption-garbled name), llama.cpp, Core ML, Xcode, watchOS / ARM64_32, Mamba 2, GGUF model format, Wikipedia tool call (sample), weather tool call (sample)

## Relevance to our work
- **agentos** (1/3): InferCraft targets a single RTX 5090 with vLLM, not edge devices. The Falcon H1 hybrid SSM and the Core ML limits are a passing note only. → *Read the Falcon H1 / Mamba-2 hybrid architecture notes before adding any SSM-hybrid model to the InferCraft model list.*
