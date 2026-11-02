# OpenCV 5 Is Here - The Biggest Update Since 2018 (We Tested It)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `piHpZWcgQyc` · [watch](https://youtu.be/piHpZWcgQyc) · **date:** 2026-08-02 · **length:** 9:42 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Andrus (Better Stack host) · **orgs:** Better Stack, OpenCV, Microsoft, Google
- **topics:** local-ai, inference-serving, dev-tools · **tags:** opencv, computer-vision, dnn, onnx, cpu-inference, latent-diffusion, inpainting, vlm, yolo, paligemma

> Better Stack tests OpenCV 5's rewritten CPU-only DNN engine (ONNX operator coverage 22% to 80%) on colorization, detection, diffusion inpainting and VLM captioning; only detection looks practical.

## Summary
The host walks through OpenCV 5, presented as the first major release since 2018, and focuses on its rewritten DNN module. He reports ONNX operator coverage rising from about 22% in OpenCV 4 to about 80%, which he attributes to a typed operation graph that runs shape inference, constant folding and operator fusion before execution. OpenCV's own CPU benchmarks against ONNX Runtime are presented as favourable, with an explicit caveat to benchmark your own workload. The new engine is CPU-only for now; GPU support is promised later in the v5 cycle, and the classic engine keeps CUDA and OpenVINO. In demos run locally with no PyTorch, colorization gave imperfect output, real-time object detection ran well on CPU, latent-diffusion inpainting worked but was slow with artifacts at low step counts, and PaliGemma captioning was very slow with mediocre results, which the host says he would not use. He closes by noting that training still happens in PyTorch and that OpenCV targets running models inside vision pipelines.

## Key ideas
- **OpenCV 5 rewrites its DNN module so many neural networks run with no PyTorch or ONNX Runtime installed.** — Headline feature is a new deep learning engine that the host says runs YOLO, inpainting and a full VLM natively. He calls it the biggest update since 2018. ([0:00](https://youtu.be/piHpZWcgQyc?t=0))
- **ONNX operator coverage rises from about 22% in OpenCV 4 to about 80% in OpenCV 5.** — Low coverage meant modern models often failed to load on an unsupported operator. The host credits the rebuild for the jump. ([1:13](https://youtu.be/piHpZWcgQyc?t=73))
- **The new engine works on a whole-graph representation instead of executing layer by layer.** — It builds a typed operation graph, then does shape inference, constant folding and operator fusion before running. The host says this enables dynamic shapes and transformer architectures that the old engine could not handle. ([2:18](https://youtu.be/piHpZWcgQyc?t=138))
- **OpenCV's self-reported CPU benchmarks put the new engine at or above ONNX Runtime on real models.** — Stated speedups are about 11.5% over YOLOv8, almost 37% over OWLv2, and 30% over a third model whose name is garbled in the captions. The host says to treat these as vendor numbers and benchmark your own workload. ([2:18](https://youtu.be/piHpZWcgQyc?t=138))
- **The new engine is CPU-only for now, so GPU inference still needs the classic engine.** — GPU support is promised later in the v5 cycle. The classic engine still provides CUDA and OpenVINO backends. ([3:25](https://youtu.be/piHpZWcgQyc?t=205))
- **Real-time object detection was the one demo the host considers practical.** — It ran on CPU through the new engine with no PyTorch and no GPU. He says this is the kind of model where OpenCV beats ONNX Runtime. ([4:29](https://youtu.be/piHpZWcgQyc?t=269))
- **Latent-diffusion inpainting works on CPU but is slow, and artifacts need more steps or a better model.** — Classic inpainting is a single forward pass, while the LDM denoises iteratively. Results at a few steps still showed artifacts. ([5:44](https://youtu.be/piHpZWcgQyc?t=344))
- **VLM captioning through PaliGemma inside OpenCV is too slow and too weak to use.** — The host says he would not use it for this. He points to a local 12B Gemma model as far faster and better. The demo's value, in his view, is showing that tokenizer, attention and KV cache are built in. ([6:40](https://youtu.be/piHpZWcgQyc?t=400))
- **OpenCV is for running models in a vision pipeline; training still happens in PyTorch.** — The host frames the release as a strong inference choice for vision pipelines, not a training framework. ([8:45](https://youtu.be/piHpZWcgQyc?t=525))

## Techniques
- **Choose the DNN engine by backend need** — Use the new OpenCV 5 engine for CPU-only inference with no extra runtime. Keep the classic OpenCV 4 engine for CUDA or OpenVINO. The host says GPU support for the new engine is still pending. *When:* Deploying vision models on CPU without PyTorch or ONNX Runtime, or when a model failed to load on the old engine because of an unsupported operator.
- **Benchmark a vendor speed claim on your own model before switching** — Run the same model through the new engine and an existing runtime such as ONNX Runtime on your own hardware and inputs. Compare latency. The host explicitly says the published numbers are self-reported. *When:* Before adopting a runtime for a production workload based on release-note speedups.
- **Tune diffusion inpainting steps to trade artifacts for latency** — Increase the number of denoising steps to reduce visible artifacts, or switch to a different diffusion model. The host saw clear artifacts at a low step count. *When:* Running latent-diffusion inpainting on CPU where latency and quality must be balanced.

## Numbers
- OpenCV has more than 86,000 GitHub stars and over one million installs a day. ([0:00](https://youtu.be/piHpZWcgQyc?t=0))
- ONNX operator coverage in the DNN engine rises from about 22% (OpenCV 4) to about 80% (OpenCV 5). ([1:13](https://youtu.be/piHpZWcgQyc?t=73))
- OpenCV-reported CPU speedups against ONNX Runtime: about 11.5% faster than YOLOv8, almost 37% faster than OWLv2, 30% faster than a third model (name garbled in captions). ([2:18](https://youtu.be/piHpZWcgQyc?t=138))
- Host says a local 12B Gemma 4 captioning run is about 100 times faster than the PaliGemma demo (anecdotal, one run). ([6:40](https://youtu.be/piHpZWcgQyc?t=400))

## Hot takes
- The host calls the OpenCV 5 release a massive leap in vision-pipeline inference and a great choice for running models inside it.
- The host says he would not use OpenCV's VLM captioning path for image captioning; better local options exist.
- Caption-level benchmark claims are OpenCV's own numbers; the host says to verify them on your own workload. The demos are single anecdotal runs on one machine, not a measured benchmark.

## Tools mentioned
OpenCV 5, OpenCV 4 (classic DNN engine), ONNX Runtime, PyTorch, YOLOv8, OWLv2, PaliGemma, Gemma 4 (12B, run locally), CUDA, OpenVINO, C++17

## Relevance to our work
- **agentos** (1/3): AgentOS InferCraft serves LLMs on vLLM and Ray Serve on one RTX 5090, so OpenCV 5 is not a serving path for it. A CPU-only, no-PyTorch vision runtime could matter only for vision preprocessing or detection inside a pipeline. → *Only if an AgentOS workload needs CPU-side vision inference, benchmark OpenCV 5's DNN engine against ONNX Runtime on your own model before adopting it.*
- **general** (1/3): A notable CV library release with an operator-coverage claim that is useful background if any project touches image pipelines. → *Skim OpenCV 5's release notes for the operator-coverage and CPU-only limits before relying on it.*
