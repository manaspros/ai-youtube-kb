# MAX + Mojo Are Quietly Replacing Python in AI

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `fOj8TgAdDGE` · [watch](https://youtu.be/fOj8TgAdDGE) · **date:** 2026-08-02 · **length:** 7:13 · **format:** news · **quality:** 3/5 · **depth:** intro
- **speakers:** Kai Explains host (unnamed in transcript) · **orgs:** Modular, Qualcomm, Oak Ridge National Laboratory, NAND Research, Arduino
- **topics:** inference-serving, dev-tools · **tags:** mojo, modular, max, qualcomm, mlir, llvm, cuda, gpu-kernels, compilers, moe, python, two-language-problem

> Kai Explains argues Mojo, Modular's Python-syntax compiled language, could remove the research-to-kernel handoff, with the Qualcomm acquisition as context and caveats on MoE support and vendor benchmarks.

## Summary
The video says Qualcomm agreed to acquire Modular (reported as $3.9B, announced June 24, 2026) and frames this around Mojo, a language with Python-like syntax that compiles to GPU and accelerator code. The core pitch is removing the "two language problem", where researchers write Python and a specialist rewrites hot paths in C++ or CUDA. The speaker describes Mojo's compiler layer (MLIR rather than plain LLVM) as the real asset, letting it target tensor cores and similar primitives across NVIDIA, AMD, Intel, ARM and Qualcomm hardware. He presents vendor benchmark claims alongside an independent ORNL/SC25 study on memory-bound kernels, a community testimonial about FLUX.2 versus llama.cpp, and a June 2026 academic paper on financial workloads. He is explicit that Mojo is not a Python superset (no classes, uses structs), the compiler is still closed source with open-sourcing promised for fall 2026, and mixture-of-experts models are a gap. He says the title's "replacing Python" framing is wrong and the real implication is that the translation role on ML teams could become optional over time. He ends with a watch list: open-source timing, community neutrality under Qualcomm, and full MoE support.

## Key ideas
- **The two-language problem is the real cost Mojo targets** — ML research is written in Python, then a C++ or CUDA specialist rewrites hot paths. The speaker says this handoff can take months and makes prototype-to-production slow. Mojo's pitch is one file, Python-like syntax, and performance close to hand-tuned kernels. ([1:25](https://youtu.be/fOj8TgAdDGE?t=85))
- **The compiler stack (MLIR, not just LLVM) is the asset Qualcomm bought** — Mojo compiles through MLIR, which lets hardware-specific passes target tensor cores, bfloat16 ops and tiled matmul primitives directly. The speaker argues this portability layer, not the language, is what matters for competing with CUDA's rewrite-cost moat. ([2:41](https://youtu.be/fOj8TgAdDGE?t=161))
- **Mojo is not a Python superset and not yet open** — It has structs instead of Python classes and is not a drop-in replacement. Mojo can call Python modules via CPython, so NumPy and PyTorch calls still work, but Mojo code does not run on the Python interpreter. The compiler is closed source, with open-sourcing committed for fall 2026. Mojo 1.0 Beta 1 shipped May 7. ([4:03](https://youtu.be/fOj8TgAdDGE?t=243))
- **Vendor numbers are separated from third-party evidence** — The speaker lists Modular Platform 26.2's 4x FLUX.2 speedup across NVIDIA Blackwell, AMD RDNA and Apple Silicon. He notes that a community forum testimonial about beating llama.cpp is not a vendor claim. He also cites an ORNL SC25 study (memory-bound kernels competitive with CUDA) and a June 2026 financial-workloads paper reporting C++-level performance. ([4:03](https://youtu.be/fOj8TgAdDGE?t=243))
- **MoE architectures are a real coverage gap** — The speaker says the current frontier models (DeepSeek V3, Llama 4, GLM 5.2 are named) are mostly MoE, and that MoE is not fully supported yet. He adds that the headline benchmarks mostly come from non-MoE workloads, so a portable inference layer that skips MoE is only a partial solution. The caption for this passage is garbled, so treat the exact target platform as unclear. ([4:03](https://youtu.be/fOj8TgAdDGE?t=243))
- **The real shift is team structure, not Python deprecation** — If one ML engineer can write a custom attention kernel at Python speed that runs at CUDA-class speed on NVIDIA, AMD and Qualcomm, the infrastructure engineer who translates research code to production kernels becomes optional. The speaker says this is a direction, not a near-term event. ([5:24](https://youtu.be/fOj8TgAdDGE?t=324))
- **Watch list: open-source timing, neutrality, and MoE support** — Three signals to track over six months: whether the compiler opens on schedule in fall 2026, whether the community treats it as neutral under Qualcomm ownership (Arduino is cited as a precedent), and whether Mac/Apple targets gain full MoE support. ([5:24](https://youtu.be/fOj8TgAdDGE?t=324))

## Techniques
- **Check architecture coverage before trusting a portable-kernel benchmark** — Before adopting a hardware-agnostic kernel or inference stack, confirm it supports the model architecture you actually deploy (for example MoE), then compare its numbers against that architecture rather than against dense-model headline benchmarks. The speaker's argument is that most headline numbers come from non-MoE workloads. *When:* Evaluating a vendor compiler or portability layer for a GPU serving or kernel project.
- **Separate vendor claims from independent evidence** — Sort performance evidence into three buckets: vendor-published numbers (for example a platform release's speedup), third-party academic or lab studies (ORNL SC25, a June 2026 paper), and community testimonials. Weight them differently and name the bucket when quoting a number. *When:* Reading benchmark claims for a new language, compiler or inference runtime before deciding whether to test it.

## Numbers
- Qualcomm acquisition of Modular reported at $3.9B, announced June 24, 2026 ([0:00](https://youtu.be/fOj8TgAdDGE?t=0))
- Mojo performance claim: within 10-20% of hand-tuned C++ or CUDA on most workloads (vendor claim) ([1:25](https://youtu.be/fOj8TgAdDGE?t=85))
- Mojo claimed 3-4 orders of magnitude faster than pure Python and 1-2 orders faster than optimized PyTorch (vendor claim) ([1:25](https://youtu.be/fOj8TgAdDGE?t=85))
- ORNL SC25 (2025) study: Mojo broadly competitive with CUDA on memory-bound GPU kernels on NVIDIA and AMD, with no extra optimization passes ([1:25](https://youtu.be/fOj8TgAdDGE?t=85))
- Modular Platform 26.2 (March) showed a 4x speedup on FLUX.2 image generation across NVIDIA Blackwell, AMD RDNA and Apple Silicon ([4:03](https://youtu.be/fOj8TgAdDGE?t=243))
- Mojo 1.0 Beta 1 shipped May 7; compiler open-source committed for fall 2026 ([4:03](https://youtu.be/fOj8TgAdDGE?t=243))
- Speaker says Qualcomm bought Modular 3 weeks after Mojo 1.0 Beta 1, but the dates stated (May 7 beta, June 24 deal) are about 7 weeks apart ([0:00](https://youtu.be/fOj8TgAdDGE?t=0))

## Hot takes
- The title's 'quietly replacing Python' framing overstates the evidence. The speaker himself says Python is not being deprecated.
- Most headline Mojo benchmarks come from non-MoE workloads, and the speaker says MoE is not fully supported, which weakens the claim for current frontier models.
- The strategic read (Qualcomm buying a CUDA alternative, the timing 'not an accident') is speculation, not sourced reporting.
- Internal inconsistency: 'three weeks' before the June 24 deal vs. a May 7 beta date. Captions also garble terms (MLR, DeepSeq, Moe, Macs), so some specifics are uncertain.
- Caveats are unusually explicit for a hype-adjacent title, and the speaker separates vendor, academic and community evidence.

## Tools mentioned
Mojo (1.0 Beta 1), Modular Platform (26.2), MAX (named in the video title), MLIR (captioned as MLR), LLVM, Clang, Swift, CUDA, PyTorch, NumPy, CPython, llama.cpp, FLUX.2, DeepSeek V3, Llama 4, GLM 5.2, mojolang.org

## Relevance to our work
- **agentos** (1/3): InferCraft (vLLM, KV-cache and attention kernels on one RTX 5090) could eventually be authored in a portable kernel language, but Mojo is beta, closed source, and lacks MoE coverage. → *Track whether Mojo's compiler opens in fall 2026 and whether MoE support lands before considering it for any InferCraft custom kernel. No change now.*
