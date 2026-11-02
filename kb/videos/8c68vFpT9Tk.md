# Google Just Made TensorFlow.js Obsolete (LiteRT.js)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `8c68vFpT9Tk` · [watch](https://youtu.be/8c68vFpT9Tk) · **date:** 2026-08-02 · **length:** 8:10 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Andres · **orgs:** Google, Better Stack
- **topics:** local-ai, inference-serving, dev-tools · **tags:** litert-js, tensorflow-js, webassembly, webgpu, webnn, browser-inference, on-device-ai, pose-estimation, quantization, vibe-coding, claude-code, three-js

> Better Stack walks through LiteRT.js, Google's WebAssembly on-device inference runtime for browsers, and builds a client-side webcam pose-capture app to test its CPU and WebGPU speed against TensorFlow.js.

## Summary
The speaker introduces LiteRT.js, a JavaScript binding that compiles Google's on-device LiteRT runtime to WebAssembly so models run in the browser, and argues it is faster than TensorFlow.js because TF.js relies on JavaScript kernels. He lists three backends: XNNPack for CPU as a universal fallback, ML Drift over WebGPU for GPU, and WebNN for NPUs (still experimental in Chrome and Edge). He cites Google's own benchmarks on a 2024 M4 MacBook Pro, which claim roughly 3x over other web runtimes on CPU and GPU, and 5x to 60x gains for GPU/NPU versus CPU depending on task, while stressing that these are best-case numbers. Existing .tflite models can run directly, PyTorch models can be converted with LiteRT Torch, and AI Edge Quantizer can shrink them. His own test is a vibe-coded webcam app using BlazePose (33 landmarks) to drive a three.js character fully offline, which moved from 38 FPS on CPU to about 120 FPS on WebGPU, a smaller gain than Google's published numbers. A planned LiteRT-LM.js for in-browser LLMs is announced but not yet shipped.

## Key ideas
- **LiteRT.js is the on-device LiteRT runtime compiled to WebAssembly and exposed to JavaScript, not a JS reimplementation.** — The speaker contrasts it with TensorFlow.js, whose JavaScript kernels he calls the main bottleneck versus native performance. LiteRT.js ships its own optimized kernels. ([0:00](https://youtu.be/8c68vFpT9Tk?t=0))
- **TensorFlow.js is framed as legacy, with LiteRT.js as the successor.** — Existing TF.js workflows can be ported, and the speaker says the title's 'obsolete' framing is his reading of the release rather than a statement Google made. ([0:44](https://youtu.be/8c68vFpT9Tk?t=44))
- **Backend choice is tiered: CPU via XNNPack, GPU via ML Drift on WebGPU, NPU via WebNN.** — XNNPack is a multi-threaded CPU kernel library with relaxed SIMD and is the fallback that runs anywhere. ML Drift uses native GPU kernels instead of JS-orchestrated shaders. WebNN targets dedicated neural hardware and is still experimental in Chrome and Edge. ([2:04](https://youtu.be/8c68vFpT9Tk?t=124))
- **Google's speedups are best-case and hardware-dependent.** — The speaker says results depend on the GPU, thermal throttling and driver quality, and that the headline figures are from one 2024 M4 MacBook Pro. ([3:10](https://youtu.be/8c68vFpT9Tk?t=190))
- **Existing model assets carry over.** — A .tflite file runs directly. PyTorch models can be converted to .tflite with LiteRT Torch, and AI Edge Quantizer shrinks model size without a full rewrite. ([3:10](https://youtu.be/8c68vFpT9Tk?t=190))
- **Demos cover vision workloads that run fully client-side.** — Google's demos include real-time YOLO detection, Depth Anything turning a webcam feed into a live 3D point cloud, and Real-ESRGAN image upscaling, all with no backend or API calls. ([3:10](https://youtu.be/8c68vFpT9Tk?t=190))
- **The author's own measurement shows a real but smaller gain than the vendor numbers.** — Moving BlazePose from CPU to WebGPU went from 38 FPS / 23.3 ms inference to about 120 FPS / 8.4 ms, roughly 3x in frame rate and 2.8x lower inference time. He attributes the modest gain partly to BlazePose being a small model with little compute for the GPU to use. ([5:10](https://youtu.be/8c68vFpT9Tk?t=310))
- **LiteRT-LM.js for in-browser LLMs is announced but not yet shipped.** — The speaker says it is expected later this year and was not available to test. ([4:26](https://youtu.be/8c68vFpT9Tk?t=266))

## Techniques
- **Select a backend per device tier** — Use XNNPack (CPU) as the universal fallback, ML Drift over WebGPU for GPU, and WebNN for NPUs where supported. The video shows no code or config keys for selecting them, so check the LiteRT.js docs for the exact API. *When:* Shipping a browser vision or audio model that must run on machines with varying hardware.
- **A/B the backends on your own hardware before trusting vendor numbers** — Run the same pose pipeline once on the CPU backend and once on the WebGPU backend, then compare FPS and per-inference milliseconds, as the speaker did in his demo. *When:* Before claiming a speedup or choosing a backend. Expect gains that depend on model size: a small model like BlazePose gains less.
- **Port existing models instead of rewriting them** — Load an existing .tflite file directly in LiteRT.js. For PyTorch models, convert to .tflite with LiteRT Torch, then shrink with AI Edge Quantizer. *When:* Moving a model from TensorFlow.js or PyTorch into a browser runtime.
- **Client-side webcam pose pipeline** — Feed webcam frames to BlazePose (33 body landmarks) through LiteRT.js on WebGPU, and use the landmarks to drive a three.js character. Nothing leaves the machine. *When:* Privacy-sensitive or offline browser apps that need real-time pose estimation with no backend.
- **Export pose recordings for retargeting** — Record the pose capture and export as JSON or BioVision BVH. Import the BVH into Blender and retarget the animation onto a custom character. The speaker notes that output quality is rough and needs refinement. *When:* Quick motion-capture prototyping when a full mocap rig is not available.

## Numbers
- Google benchmark, 2024 M4 MacBook Pro: about 3x faster inference than other web runtimes on CPU and GPU across vision and audio models ([2:04](https://youtu.be/8c68vFpT9Tk?t=124))
- GPU/NPU versus CPU on tasks like object tracking, audio transcription and image manipulation: about 5x to 60x faster, depending on task (Google figure, best case) ([2:04](https://youtu.be/8c68vFpT9Tk?t=124))
- Author demo, BlazePose on CPU: about 38 FPS, 23.3 ms inference ([5:10](https://youtu.be/8c68vFpT9Tk?t=310))
- Author demo, BlazePose on WebGPU: about 120 FPS, 8.4 ms inference ([5:10](https://youtu.be/8c68vFpT9Tk?t=310))
- Author demo, CPU to WebGPU: roughly 3x frame rate and 2.8x lower inference time, on the modest end of Google's published numbers ([5:10](https://youtu.be/8c68vFpT9Tk?t=310))
- BlazePose model uses 33 body landmarks ([5:10](https://youtu.be/8c68vFpT9Tk?t=310))
- Author says the first working version took about 10 minutes to build ([6:18](https://youtu.be/8c68vFpT9Tk?t=378))

## Hot takes
- The title's claim that TensorFlow.js is made obsolete is overstated. The video itself presents LiteRT.js as the successor and TF.js workflows as portable, not as dead.
- Google's headline speedups come from one 2024 M4 MacBook Pro and best-case workloads. The author's own GPU test showed about 3x FPS and 2.8x lower inference for a small model, below the published range.
- WebNN is experimental and LiteRT-LM.js is not shipped, so only the CPU and WebGPU paths are usable today in practice.
- Quality is capped by thin evidence: one demo app, one machine, and no independent benchmarks. There is no sponsorship segment.

## Tools mentioned
LiteRT.js, LiteRT, TensorFlow.js, WebAssembly, XNNPack, ML Drift, WebGPU, WebNN, LiteRT Torch, AI Edge Quantizer, LiteRT-LM.js (announced, not shipped), BlazePose, three.js, YOLO, Depth Anything, Real-ESRGAN, PyTorch, TensorFlow, Blender, BVH, Chrome, Edge, Claude Code, Fable 5 (model name as transcribed; unverified)

## Relevance to our work
- **agentos** (1/3): Browser-side on-device inference is adjacent to AgentOS's self-hosted serving stack (vLLM on one GPU), but it does not change the proxy, memory or KV-cache work. → *No change now. If InferCraft ever needs an edge or non-GPU fallback, revisit LiteRT.js backend selection and the LiteRT-LM.js LLM release.*
