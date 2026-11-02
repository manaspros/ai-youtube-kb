# The FASTEST Vision Model for Your Laptop (Liquid AI LFM 2.5)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ZeMuQh9j3dE` · [watch](https://youtu.be/ZeMuQh9j3dE) · **date:** 2026-04-02 · **length:** 5:52 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Andrus · **orgs:** Better Stack, Liquid AI, Hugging Face
- **topics:** local-ai, models-research, voice-multimodal · **tags:** liquid-ai, lfm, webgpu, onnx-runtime, browser-inference, on-device, vision-language-model, hugging-face-spaces, offline-ai, fp16, quantization, webcam-captioning

> Better Stack demos Liquid AI's LFM vision-language model running in the browser via WebGPU and ONNX Runtime; real-time webcam captioning works offline once cached, but no benchmarks are measured.

## Summary
The video walks through a Hugging Face Space demo of Liquid AI's LFM vision-language model running entirely in the browser with WebGPU and ONNX Runtime. The presenter relays the vendor's architecture claims: a hybrid of convolutional blocks and grouped query attention, a 1.6B-parameter model trained on 28T tokens, a 32K context window, native 512x512 image handling with tiling for larger images, and a footprint under 1 GB of RAM. He loads the FP16 variant, waits for the browser download to cache, and then runs real-time webcam captioning. The live test identifies a person, a phone, a peace sign, a thumbs up, a microphone and text on a phone case. He then disables Wi-Fi and the captions keep working. The test is qualitative only: no accuracy, latency, throughput or quantization comparison is shown, and the benchmark claim that it matches models twice its size is not checked.

## Key ideas
- **The LFM model runs fully in the browser (WebGPU plus ONNX Runtime), so images and video are processed locally and the data never leaves the device.** — The presenter says that once the model is cached, no internet connection is needed. He presents this as the main appeal of the demo. ([0:00](https://youtu.be/ZeMuQh9j3dE?t=0))
- **The model is pitched as a 1.6B-parameter vision-language model with a hybrid architecture (convolutional blocks plus grouped query attention), trained on 28T tokens.** — These are vendor claims relayed by the presenter. He also says the model often matches models twice its size on benchmarks, but no benchmark is shown. ([0:00](https://youtu.be/ZeMuQh9j3dE?t=0))
- **The 'efficiency by design' argument: the liquid architecture uses adaptive convolutional blocks as local filters, rather than a KV cache that grows with conversation length.** — The presenter describes the LIV (linear input-varying) design as compressing information as it flows through the model. He contrasts this with pruned or compressed versions of large cloud models, which he says LFM does not use. He presents this as explanation, not as something the video verifies. ([1:13](https://youtu.be/ZeMuQh9j3dE?t=73))
- **Image handling uses native 512x512 resolution, and larger images are tiled into patches with a global thumbnail kept for context.** — The context window is stated as 32,000 tokens. The presenter also says the model runs under 1 GB of RAM. ([2:11](https://youtu.be/ZeMuQh9j3dE?t=131))
- **The concrete test is real-time webcam captioning in the Hugging Face Space demo, after the FP16 model has been downloaded and cached.** — The model recognised a person in a hoodie, a phone, a peace sign, a thumbs up, a microphone and text on a phone case. The video shows no failure cases and no timing numbers. ([3:34](https://youtu.be/ZeMuQh9j3dE?t=214))
- **Offline behaviour was checked by turning off Wi-Fi after the model was cached, and the captions kept working.** — This is a single informal check in one browser session. It supports the local-inference claim for this one case only. ([3:34](https://youtu.be/ZeMuQh9j3dE?t=214))

## Techniques
- **Run a vision-language model in the browser** — 1) Open the Liquid AI LFM Hugging Face Space demo. 2) Choose the model variant; the presenter picks the most powerful one, FP16. 3) Click load and wait for the one-time browser download, which he says takes a considerable time. 4) Click Start to begin real-time webcam captioning. Later loads reuse the browser cache. The demo uses WebGPU and ONNX Runtime in the browser. *When:* Privacy-sensitive image or video understanding where data must stay on the device, or quick local demos without a GPU server or paid API.
- **Native resolution with tiling for large images** — Images up to 512x512 are processed at native resolution without distortion or upscaling. Larger images are split into patches, and a downscaled thumbnail of the whole image is kept as global context. *When:* Feeding a small on-device VLM with mixed-size images where you want to avoid distortion and still keep whole-image context.
- **Offline verification by disabling the network** — After the model is cached in the browser, turn off Wi-Fi and rerun the same input. If results still come back, the pipeline is not making network calls. *When:* Checking a claim that inference is fully local before trusting it for privacy or air-gapped use.

## Numbers
- Model size: 1.6B parameters (vision-language) ([0:00](https://youtu.be/ZeMuQh9j3dE?t=0))
- Training data: 28 trillion tokens (vendor claim) ([0:00](https://youtu.be/ZeMuQh9j3dE?t=0))
- Memory footprint: under 1 GB of RAM (vendor claim, repeated at 2:11) ([1:13](https://youtu.be/ZeMuQh9j3dE?t=73))
- Benchmarks: often matches models about twice its size (vendor claim, no numbers shown) ([1:13](https://youtu.be/ZeMuQh9j3dE?t=73))
- Context window: 32,000 tokens ([2:11](https://youtu.be/ZeMuQh9j3dE?t=131))
- Native image resolution: 512x512, with tiling for larger images ([2:11](https://youtu.be/ZeMuQh9j3dE?t=131))
- Video length: 5:52 ([0:00](https://youtu.be/ZeMuQh9j3dE?t=0))

## Hot takes
- Architecture, training-data, RAM and benchmark claims come from the vendor and are relayed without checking; the video shows no benchmark results.
- The test is a handful of qualitative webcam checks (objects, gestures, text on a case). It gives no accuracy, latency, or FP16 vs. quantized comparison.
- The offline claim rests on one informal Wi-Fi toggle in one browser session after caching.
- Hype framing ('super cool', 'the fastest') outruns the evidence shown. Quality is capped at 2 for thin substance and vendor-demo framing.

## Tools mentioned
Liquid AI LFM (Liquid Foundation Model), vision-language variant, 1.6B parameters (title says LFM 2.5), WebGPU (browser GPU API), ONNX Runtime (transcribed as 'onyx runtime', running in the browser), Hugging Face Spaces (demo host)

## Relevance to our work
- **agentos** (1/3): Shows a small on-device VLM running in a browser; this is adjacent to the local-inference layer (InferCraft on vLLM and one RTX 5090) but does not change it. → *Note LFM as an option for small offline vision tests. Before adopting it, benchmark it against our own vLLM stack on accuracy and latency; the video provides no numbers.*
