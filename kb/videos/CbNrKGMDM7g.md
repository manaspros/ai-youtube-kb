# Mojo + Vulkan is INSANE: Run Local AI on ANY GPU (Goodbye CUDA)

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `CbNrKGMDM7g` · [watch](https://youtu.be/CbNrKGMDM7g) · **date:** 2026-08-02 · **length:** 7:59 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Kai (Kai Explains host, not named in transcript) · **orgs:** NVIDIA, AMD, Intel, Apple, Modular, Qualcomm
- **topics:** local-ai, inference-serving, dev-tools · **tags:** vulkan, llama.cpp, mojo, modular, cuda-moat, amd-rocm, local-llm, lm-studio, gpu-portability, strix-halo, mi300x, vllm

> Kai Explains argues Vulkan (llama.cpp) and Mojo are weakening the CUDA lock-in, so local AI runs on AMD, Intel, Apple and iGPU hardware, with CUDA still fastest at the top end.

## Summary
The presenter argues that CUDA's lock-in to NVIDIA hardware is eroding through two routes: Vulkan, a vendor-neutral graphics API that llama.cpp can use to run models on AMD, Intel, and Apple GPUs, and Mojo, a Python-like language from Modular that compiles GPU kernels for multiple vendors. Cited Vulkan numbers include about 190 tokens/s on an AMD 7900 XTX, which beats AMD's own ROCm path on that card and on Strix Halo (about 20% faster). The video concedes that raw CUDA still leads at the top end (about 290 vs 260 tokens/s on the speaker's flagship NVIDIA card). For Mojo, it cites up to 50% more serving throughput than vLLM on AMD MI300X and a hand-tuned NVIDIA library kernel rewritten in Mojo that matches its CUDA version at about 130 TFLOPS on B200 with roughly a quarter of the code. The video frames Qualcomm's reported near-$4B purchase of Modular in June as a market signal. It ends with a practical call to try LM Studio's Vulkan runtime with a small model. Most claims are benchmark headlines with no methodology, model sizes, quantization, or prompt lengths stated, so treat the figures as directional.

## Key ideas
- **CUDA lock-in is the real moat, not NVIDIA's hardware speed** — The presenter says CUDA is genuinely good software, but its NVIDIA-only scope is what locked the AI ecosystem (PyTorch, TensorFlow, JAX, vLLM all sit on it). ([0:00](https://youtu.be/CbNrKGMDM7g?t=0))
- **Vulkan gives one backend that runs on any vendor's GPU** — Vulkan is a cross-vendor graphics API; llama.cpp can use it for matrix math, so one binary runs on NVIDIA, AMD, Intel, and Apple (via MoltenVK) without a vendor toolkit. ([1:24](https://youtu.be/CbNrKGMDM7g?t=84))
- **On AMD, Vulkan beat the vendor's own ROCm stack in the cited tests** — On a 7900 XTX, Vulkan reportedly reaches about 190 tok/s with only the graphics driver installed; on Strix Halo it is about 20% faster than ROCm and steadier. ([2:47](https://youtu.be/CbNrKGMDM7g?t=167))
- **CUDA still wins at the top end, but the gap is now a preference** — The presenter's flagship NVIDIA run reaches about 290 tok/s on CUDA vs about 260 on Vulkan. He frames this as the monopoly becoming a preference rather than a requirement. ([4:07](https://youtu.be/CbNrKGMDM7g?t=247))
- **Mojo compiles one kernel source to each vendor's GPU** — Mojo (from Modular, founded by Chris Lattner) is pitched as Python-like syntax with hand-tuned performance, compiled per vendor at build time. Modular reports one container running unchanged on AMD and NVIDIA datacenter GPUs and later open-sourced the kernel code. ([4:07](https://youtu.be/CbNrKGMDM7g?t=247))
- **A Mojo rewrite of an NVIDIA hand-tuned kernel matched CUDA on NVIDIA hardware** — The presenter says a Mojo version of a NVIDIA library kernel (captioned 'Ciutela S', likely cuBLAS) reached about 130 TFLOPS on B200, level with the hand-tuned CUDA version, at about 770 lines vs about 3,000. ([5:31](https://youtu.be/CbNrKGMDM7g?t=331))
- **Qualcomm's reported near-$4B purchase is cited as a market signal** — The presenter reads the reported June acquisition of the company behind Mojo as a hardware giant paying to make CUDA optional. This is the speaker's interpretation, not a verified deal term. ([5:31](https://youtu.be/CbNrKGMDM7g?t=331))
- **Practical path for non-NVIDIA owners is a Vulkan runtime in LM Studio** — The concrete action is: download LM Studio, switch the runtime to Vulkan, and load a small model, with no account or cost. ([6:57](https://youtu.be/CbNrKGMDM7g?t=417))

## Techniques
- **Run local models on a non-NVIDIA GPU via llama.cpp Vulkan backend** — Use a single Vulkan build of llama.cpp (or LM Studio's Vulkan runtime) instead of a vendor stack; no CUDA, ROCm, or vendor toolkit install is needed beyond the normal graphics driver. Pick a small model file and start generating. *When:* You own an AMD, Intel Arc, Apple Silicon, or integrated/laptop GPU and want local inference without a vendor-specific install.
- **Benchmark Vulkan against the vendor stack on the same hardware** — Run the same model with the Vulkan backend and the vendor backend (ROCm on AMD, CUDA on NVIDIA) and compare tokens per second; the presenter's AMD results show the default assumption can be wrong. *When:* Before assuming the vendor's official AI stack is the fastest option on its own hardware, especially on AMD.
- **Write a GPU kernel once in Mojo and compile per vendor** — Write the kernel in Mojo (Python-like syntax); the compiler emits machine code for each target GPU at build time, so the same source can deploy to AMD and NVIDIA datacenter GPUs with no code changes (per the presenter's cited example). *When:* You need one codebase across GPU vendors, or want to avoid maintaining separate CUDA and ROCm kernels.
- **Compare a rewritten kernel to a vendor-tuned kernel on the same chip** — Rewrite a hand-tuned vendor kernel in another language and benchmark it head to head on the vendor's flagship chip; the presenter's example is a Mojo port of a NVIDIA library kernel reaching parity at about 130 TFLOPS on B200 with about 770 lines vs about 3,000. *When:* Evaluating whether a portable language can match hand-tuned vendor kernels without a performance penalty.

## Numbers
- AMD 7900 XTX on Vulkan: about 190 tok/s, with no ROCm install ([2:47](https://youtu.be/CbNrKGMDM7g?t=167))
- Vulkan about 20% faster than ROCm on AMD Strix Halo, and steadier ([2:47](https://youtu.be/CbNrKGMDM7g?t=167))
- Intel Arc B580 about 70 tok/s ([2:47](https://youtu.be/CbNrKGMDM7g?t=167))
- Apple M3 Ultra via MoltenVK about 115 tok/s ([2:47](https://youtu.be/CbNrKGMDM7g?t=167))
- Top-end NVIDIA: CUDA about 290 tok/s vs Vulkan about 260 tok/s ([4:07](https://youtu.be/CbNrKGMDM7g?t=247))
- Mojo serving stack on AMD MI300X: up to 50% more throughput than vLLM on real models ([4:07](https://youtu.be/CbNrKGMDM7g?t=247))
- Mojo serving stack matched NVIDIA H200 token for token on another AMD chip (per speaker) ([4:07](https://youtu.be/CbNrKGMDM7g?t=247))
- Mojo kernel on NVIDIA B200: about 130 TFLOPS, matching the hand-tuned CUDA library kernel ([5:31](https://youtu.be/CbNrKGMDM7g?t=331))
- Mojo kernel about 770 lines vs about 3,000 lines of CUDA ([5:31](https://youtu.be/CbNrKGMDM7g?t=331))
- Qualcomm reportedly paid nearly $4 billion for the company behind Mojo in June ([0:00](https://youtu.be/CbNrKGMDM7g?t=0))

## Hot takes
- Vulkan beating ROCm on AMD's own hardware means the vendor-neutral path is now ahead of the official vendor stack in some cases.
- CUDA is now a 'moat, not a wall', meaning NVIDIA's lead is a preference at the top end rather than a requirement.
- Qualcomm's reported purchase of the company behind Mojo signals hardware giants betting on making CUDA optional.
- Video title ('INSANE', 'Goodbye CUDA') overstates the result: the video itself concedes CUDA is still faster at the top end and Mojo is young.

## Tools mentioned
CUDA, Vulkan, llama.cpp, ROCm, Metal, SYCL, MoltenVK, Mojo, Modular, PyTorch, TensorFlow, JAX, vLLM, LM Studio, AMD 7900 XTX, AMD MI300X, AMD Strix Halo, Intel Arc B580, Apple M3 Ultra, NVIDIA B200, NVIDIA H200, NVIDIA RTX flagship (caption reads '50-90', likely RTX 5090)

## Relevance to our work
- **agentos** (1/3): InferCraft runs vLLM and Ray Serve on one RTX 5090; this video says CUDA is still fastest on NVIDIA, so the current stack stays. Vulkan or Mojo matter only if we add non-NVIDIA nodes to the local inference tier. → *No change to InferCraft now; if a non-NVIDIA box is ever added for L2B, benchmark a Vulkan llama.cpp build against vLLM/CUDA on the same model first.*
