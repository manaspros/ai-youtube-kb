# Taming the AI Hardware Cambrian Explosion — Abdul Dakkak, Modular

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `7BcQdtRA3Tc` · [watch](https://youtu.be/7BcQdtRA3Tc) · **date:** 2026-10-12 · **length:** 17:08 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Abdul Dakkak · **orgs:** Modular
- **topics:** inference-serving, infra-cost-scaling · **tags:** Mojo, MAX, Modular Cloud, hardware portability, kernels, KV cache, disaggregated inference, heterogeneous hardware, AMD vs NVIDIA cost, image and video generation serving, vendor benchmark, vLLM vs MAX

> Modular's pitch for a single portable stack (Mojo language, MAX inference engine, Modular Cloud) across NVIDIA, AMD and other accelerators, backed by vendor-run speed and cost benchmarks.

## Summary
The speaker from Modular argues that the number of AI accelerators is exploding while the software for programming them is fragmented, with hardware differences leaking up through frameworks like vLLM and SGLang. Modular's answer is a three-part stack: Mojo, a Python-like systems language for CPUs, GPUs and accelerators; MAX, an inference engine built on Mojo kernels that covers text, image, video and speech models; and Modular Cloud for routing, KV-cache offload and disaggregated serving. The talk frames portability, performance and usability as a trade-off that existing options each sacrifice one of, and claims Mojo covers all three. Most of the content is vendor benchmark claims (faster TTFT, higher tokens per minute per GPU, faster image generation) that the speaker says are independently verified via Artificial Analysis, but the talk gives little methodology. The speaker also says the kernels and model definitions are open source and that Mojo 1.0 and Mojo open-sourcing are coming in the next few months. Overall this is a product pitch with a few architectural ideas worth noting.

## Key ideas
- **Hardware proliferation is making AI inference software a mess** — Compute is scarce and new accelerators keep appearing (NVIDIA generations, Intel, Arm, Apple, AMD). Hardware choices leak up through the stack, so each added chip adds integration work across frameworks such as vLLM, SGLang, TensorRT-LLM and llama.cpp. The speaker proposes one unifying layer instead. ([0:08](https://youtu.be/7BcQdtRA3Tc?t=8))
- **Modular rebuilds the stack from the bottom up as three layers** — Mojo is the language layer, MAX is the inference engine on top of it, and Modular Cloud handles routing, KV-cache offload and distributed or disaggregated serving. The speaker presents this as one programmable, hardware-abstracted platform that can run on-prem or in their cloud. ([2:12](https://youtu.be/7BcQdtRA3Tc?t=132))
- **Portability, performance and usability are usually traded off against each other** — The speaker places vendor kernel stacks (CUDA, ROCm) at high performance but low usability and portability, OpenCL at high portability but weaker performance, and Triton at a middle point he puts at about 70% of peak performance. Mojo is pitched as covering all three at once, with low-level access when needed. ([4:39](https://youtu.be/7BcQdtRA3Tc?t=279))
- **The speaker argues PyTorch was not designed for generative inference** — He says PyTorch is about 10 years old and that vLLM and SGLang were built to fill gaps such as KV cache and paged attention, which added layers on top of PyTorch. MAX is presented as a new framework with a graph compiler, eager mode and cross-device fusion, so users can develop and serve a model in one system. ([7:11](https://youtu.be/7BcQdtRA3Tc?t=431))
- **Multi-GPU, multi-node and mixed-hardware serving are part of the model API** — The speaker says MAX lets developers program multi-GPU and multi-node execution from within the API. He notes that prefill and decode could run on different hardware, which is the basis of the heterogeneous serving pitch. ([8:14](https://youtu.be/7BcQdtRA3Tc?t=494))
- **Cost per GPU has to be part of any speed comparison** — The speaker says a raw 7x speedup on one platform versus a 4x speedup on another cannot be compared directly, and that cost per GPU must be factored in. He says AMD is usually about 30% cheaper than the NVIDIA equivalent. ([12:17](https://youtu.be/7BcQdtRA3Tc?t=737))
- **Modular Cloud exposes tunable knobs and a lab to pick a point on the cost/latency frontier** — Endpoints are described as a glass box where users can adjust MAX and Mojo parameters. A Modular Cloud lab is offered to test settings and choose a point on the Pareto frontier for a given model or workload. Custom fine-tuned models and custom speculative decoders can also be hosted. ([9:44](https://youtu.be/7BcQdtRA3Tc?t=584))

## Techniques
- **Heterogeneous prefill/decode split** — Run prefill on one hardware type and decode on another within the same serving system, configured through the framework's multi-GPU and multi-node API. *When:* When a fleet mixes accelerator types and the two phases have different compute or memory needs. The talk only asserts this is possible and gives no measurements.
- **Price-normalized hardware comparison** — Compare inference platforms by throughput per GPU-cost (or per dollar), not by raw speedup on one device. *When:* When choosing between NVIDIA and AMD or other accelerators, or judging any vendor speed claim.
- **Portable kernel development with an open benchmark** — Write kernels once in a Python-like language that targets CPU, NVIDIA and AMD GPUs, then benchmark them on your own machine against vendor libraries such as cuBLAS and hipBLAS. *When:* When you need one codebase across several accelerators and want to verify performance claims yourself rather than trust a vendor slide.
- **AI-assisted porting of kernels** — Use the vendor's published AI skills to port code from a familiar language into Mojo or MAX. *When:* When moving existing CUDA or Python kernels to a new target and you are not yet fluent in the new language.
- **Tuning serving parameters on a Pareto frontier** — Sweep endpoint configuration (hardware, batching, speculative decoding and similar settings) in a lab, then choose the point that fits the latency and cost target for a given model and workload. *When:* When one model must hit a specific latency or cost target and the default configuration is not enough.

## Numbers
- Kimi K2.5: about 5.5x faster time-to-first-token than vLLM (vendor claim) ([10:45](https://youtu.be/7BcQdtRA3Tc?t=645))
- Kimi K2.5: about 1.5x tokens per minute per GPU on B200 vs vLLM (vendor claim) ([10:45](https://youtu.be/7BcQdtRA3Tc?t=645))
- Flux 2: about 7x faster than torch compile with diffusers (vendor claim) ([12:17](https://youtu.be/7BcQdtRA3Tc?t=737))
- AMD MI355: about 4x faster than the equivalent system, with AMD usually about 30% cheaper per GPU (vendor claim) ([12:17](https://youtu.be/7BcQdtRA3Tc?t=737))
- Flux2 dev on Artificial Analysis: about 3x faster than the next competitor, measured as raw speed with no distillation or quantization (vendor claim) ([13:17](https://youtu.be/7BcQdtRA3Tc?t=797))
- Image generation in sub-second times, often about 0.3 seconds, in the live demo ([14:19](https://youtu.be/7BcQdtRA3Tc?t=859))
- Gemma 4: about 6x faster than SambaNova (speaker says 'let's say 6x') ([14:19](https://youtu.be/7BcQdtRA3Tc?t=859))
- Matrix multiplication is faster than cuBLAS/hipBLAS by about 2% in some cases (speaker says 'not by 1%, in some cases by 2%') ([5:38](https://youtu.be/7BcQdtRA3Tc?t=338))
- Over 700,000 lines of kernel code open-sourced ([14:19](https://youtu.be/7BcQdtRA3Tc?t=859))
- Triton is characterized as giving about 70% of peak performance ([4:39](https://youtu.be/7BcQdtRA3Tc?t=279))
- PyTorch is about 10 years old ([5:38](https://youtu.be/7BcQdtRA3Tc?t=338))
- Thousands of model architectures supported in MAX, including Gemma 4, MiniMax and GLM ([7:11](https://youtu.be/7BcQdtRA3Tc?t=431))

## Hot takes
- PyTorch was not designed for generative AI inference and the vLLM and SGLang layers on top of it complicate the ecosystem.
- Mojo competes with CUDA on performance while being more portable and usable.
- Vendor speedup numbers are not comparable without normalizing by cost per GPU.
- Speedups come from raw hardware use, not distillation or quantization (vendor claim).

## Tools mentioned
Mojo, MAX, Modular Cloud, vLLM, SGLang, TensorRT-LLM, llama.cpp, PyTorch, Triton, CUDA, ROCm, OpenCL, Artificial Analysis, Flux 2, Gemma 4, Kimi K2.5

## Relevance to our work
- **agentos** (1/3): InferCraft runs vLLM and Ray Serve on one RTX 5090. The talk's only relevant idea is the claim that prefill and decode can be split across hardware, plus its per-GPU cost framing, and it gives no evidence beyond vendor numbers. → *When benchmarking InferCraft, report throughput per GPU-cost and TTFT separately, and test MAX against vLLM on one model before accepting any speedup claim.*
- **general** (1/3): Useful as a reminder that serving benchmarks need cost normalization and independent verification. Not directly actionable for our current work. → *When writing up any inference benchmark, state the cost basis (per GPU or per dollar) next to every speedup number.*
