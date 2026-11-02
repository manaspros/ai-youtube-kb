# Deepseek & Huawei Made Local AI Run Without NVIDIA's CUDA (And Why it's Hard)

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `uJcPjrEgppk` · [watch](https://youtu.be/uJcPjrEgppk) · **date:** 2026-10-05 · **length:** 16:42 · **format:** news · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Kai Explains host (name not given in transcript) · **orgs:** DeepSeek, Huawei, NVIDIA, Tile AI, vLLM, llama.cpp, Apache TVM
- **topics:** inference-serving, models-research, local-ai · **tags:** deepseek, huawei-ascend, cuda-alternative, kernel-libraries, deepgemm, flashmla, deepep, tilelang, bf16-utilization, hardware-roadmap, open-weight-models, skepticism

> DeepSeek's Ascend kernel release looks like a CUDA challenger, but its 99.8% figure measures efficiency against Huawei's low ceiling; the stack still depends on Huawei's runtime and the hardware is not yet available.

## Summary
The host walks through DeepSeek's September 30 release of kernel libraries for Huawei Ascend chips, which mirror the February NVIDIA kernel set one-to-one under the same Python import names. The headline 99.8% utilization is measured against the Ascend 950DT's own BF16 ceiling (431 of 432 TFLOPS), and the README's cross-vendor table shows Ascend at roughly 30–35% of a B200 on attention kernels. The host argues the release is a platform-level story rather than a CUDA replacement: TileLang belongs to Tile AI and is built on Apache TVM, and everything below the kernels (compiler, runtime, drivers) is still Huawei's CANN stack. The distributed communication library DeepEP Ascend holds bandwidth up to 32 ranks, but collectives and expert load balancing are unfinished, the bandwidth numbers came from pre-production hardware, and that repo shipped without a license. The 950DT ships in Q4 2026, and the consumer-accessible Ascend parts are several generations older with weak software support. The host's bottom line is that the software excuse is gone but the hardware gap is a fab problem, so this is a long-term story to watch rather than something to deploy now.

## Key ideas
- **DeepSeek's September 30 release mirrors its February NVIDIA kernel set one-to-one for Ascend: GEMM, attention, MoE token dispatch and top-k selection.** — Six libraries: DeepGEMM Ascend, DeepEP Ascend, Ascend kernels inside FlashMLA, and an Ascend backend in TileKernels. The four operations (matmul, attention, token routing, top-k) are what set inference speed. ([1:18](https://youtu.be/uJcPjrEgppk?t=78))
- **Same import names make the swap a drop-in change.** — DeepGEMM Ascend installs under the same Python package name, so existing code using the NVIDIA version needs no import changes. The host frames this as reversing vendor lock-in that lives in small import and call sites. ([2:41](https://youtu.be/uJcPjrEgppk?t=161))
- **The 99.8% figure is utilization of Ascend's own ceiling, not a competitive number.** — BF16 reaches 431 TFLOPS against a 432 ceiling. An H100 does 1,979 dense at the same precision and Blackwell parts are around 10,000. The number shows software quality, not chip size. ([4:06](https://youtu.be/uJcPjrEgppk?t=246))
- **DeepSeek's own cross-vendor table shows the Ascend side at about 30–35% of a B200.** — Sparse attention prefill: 410 TFLOPS on Ascend 950 vs 1,350 on B200. Output writing: 360 vs 1,024. Ascend is near its ceiling (95%) while B200 has headroom, so the gap is hardware size, not effort. ([5:28](https://youtu.be/uJcPjrEgppk?t=328))
- **TileLang is not a DeepSeek language and does not replace CUDA; the release adds an Ascend 950 compiler target.** — TileLang belongs to Tile AI, was created in October 2024, is built on Apache TVM, and already targeted NVIDIA, AMD and Apple Metal. Ascend support lived in a separate repo since September 2025. The host says other videos made this error. ([6:50](https://youtu.be/uJcPjrEgppk?t=410))
- **A kernel library runs on a platform; it does not replace one.** — CUDA is a driver, runtime, compiler, kernel language and libraries. Everything below the kernels in the Ascend release is Huawei's CANN stack, which the repos require at version 9.2.0 and which ships mostly as binaries. ([8:09](https://youtu.be/uJcPjrEgppk?t=489))
- **DeepEP Ascend is the weak point for training-scale use.** — Bandwidth holds 90–95% of the physical limit up to 32 ranks. Reduce, scatter and all-reduce are still being built, and expert load balancing is not implemented. The bandwidth table came from a pre-production HDK with manual configuration, so outsiders cannot reproduce it. ([9:19](https://youtu.be/uJcPjrEgppk?t=559))
- **Availability and licensing are the practical blockers.** — DeepEP Ascend shipped without a license while the other five repos are MIT. The 950DT reaches customers in Q4 2026. Older Ascend generations were not measured. Atlas 300i duo with Ascend 310P gets about 15 tokens/s on a 32B dense model. ([10:35](https://youtu.be/uJcPjrEgppk?t=635))
- **The software stacks are split and lagging.** — llama.cpp's Ascend backend was last updated November 2024 and has no 950 row. vLLM's Ascend plugin is maintained but pins CANN 9.1.0, one minor version behind what the new repos need. ([11:54](https://youtu.be/uJcPjrEgppk?t=714))
- **Memory capacity, not FLOPs, may decide the comparison for large MoE models.** — The Ascend 950DT has 144 GB at 4 TB/s versus H100's 80 GB at 3.35 TB/s. For MoE models that are limited by how many experts fit in memory, Ascend wins on that axis. ([13:09](https://youtu.be/uJcPjrEgppk?t=789))
- **Watch-list for real evidence.** — First benchmark from an outside team, first cluster run outside China, the DeepEP license file, a 950 row in vLLM, and public release of the Atlas 850 firmware would settle the question. ([15:36](https://youtu.be/uJcPjrEgppk?t=936))

## Techniques
- **Read utilization numbers against their denominator** — Check the README's benchmark table for the peak used as the denominator; compare with the same kernel on the other vendor's hardware from the same release, not with a different generation. *When:* Evaluating any vendor claim of percent-of-peak or utilization, including kernel benchmarks for our own InferCraft work.
- **Drop-in kernel swap via identical package/import names** — Install the alternative backend under the same Python package and import name, so model code is unchanged and only the installed library differs. *When:* Porting an inference or training stack across accelerator vendors with minimal code churn.
- **Check hardware provenance and license footnotes before depending on a release** — Look for pre-production or non-public hardware footnotes, unreproducible benchmark setups, missing LICENSE files, and which hardware generations were actually measured. *When:* Deciding whether to adopt a new vendor library or publish benchmark numbers.
- **Pin runtime versions to the vendor stack the kernels require** — Match the inference framework plugin's pinned runtime (e.g. the Ascend CANN minor version) to the one the kernel library requires; a one-minor mismatch can block support. *When:* Running a non-NVIDIA inference stack where kernels, framework plugin and driver/runtime versions must line up.

## Numbers
- DeepGEMM on NVIDIA H800 hit 1,350 TFLOPS with about 300 lines of core logic (February release, as stated). ([1:18](https://youtu.be/uJcPjrEgppk?t=78))
- Ascend 950DT BF16: 431 TFLOPS achieved vs 432 ceiling (99.8%). ([4:06](https://youtu.be/uJcPjrEgppk?t=246))
- H100 dense BF16 is 1,979 TFLOPS; Blackwell is around 10,000 (as stated by the host). ([4:06](https://youtu.be/uJcPjrEgppk?t=246))
- Sparse attention prefill: B200 1,350 TFLOPS vs Ascend 950 410 TFLOPS. ([5:28](https://youtu.be/uJcPjrEgppk?t=328))
- Output writing: B200 1,024 vs Ascend 950 360. Ascend side at 95% of its theoretical peak FP8. ([5:28](https://youtu.be/uJcPjrEgppk?t=328))
- Illustrative: a 10-second prompt on NVIDIA would take about 33 seconds on this Ascend chip, if the chip is the only bottleneck. ([5:28](https://youtu.be/uJcPjrEgppk?t=328))
- DeepEP Ascend holds 90–95% of physical bandwidth up to 32 ranks; larger scales are still under optimization. ([9:19](https://youtu.be/uJcPjrEgppk?t=559))
- Ascend 950DT memory: 144 GB at 4 TB/s vs H100 80 GB at 3.35 TB/s. ([13:09](https://youtu.be/uJcPjrEgppk?t=789))
- China share of NVIDIA revenue went from 8.5% a year earlier to 8.2% last quarter, while NVIDIA's total nearly doubled. ([13:09](https://youtu.be/uJcPjrEgppk?t=789))
- Atlas 300i duo with Ascend 310P: about 15 tokens/s on a 32B dense model; one forum user reported 30 after patching drivers. ([11:54](https://youtu.be/uJcPjrEgppk?t=714))
- Ascend 950DT BF16 ceiling of 432 is 44% of H100's 1,979 at the same precision. ([15:36](https://youtu.be/uJcPjrEgppk?t=936))

## Hot takes
- The 99.8% headline measures how close the software gets to Huawei's own low ceiling, not how competitive the chip is.
- Multiple other videos wrongly called TileLang a DeepSeek-built CUDA replacement; it is a Tile AI project on Apache TVM, and this release only adds an Ascend target.
- The release is a kernel layer on top of Huawei's platform, not a replacement for CUDA's stack.
- DeepEP Ascend is not usable for distributed training yet: collectives and load balancing are missing, numbers come from pre-production hardware, and there is no license.
- Huawei's willingness to let an outside team publish honest profiler numbers is a real openness difference from NVIDIA.
- The memory-capacity argument may favor Ascend 950DT for large MoE models even though it trails on FLOPs.

## Tools mentioned
DeepGEMM, FlashMLA, DeepEP, TileKernels, TileLang, Apache TVM, CANN 9.2.0, vLLM, llama.cpp, NVCC, CUDA, Ascend 950DT, Ascend 910B, Ascend 910C, Ascend 310P, Atlas 300i duo, Atlas 850, NVIDIA H100, NVIDIA H800, NVIDIA B200

## Relevance to our work
- **agentos** (1/3): InferCraft runs vLLM and custom kernels on a single RTX 5090; this video is about non-NVIDIA kernel portability and the need to read benchmark percentages carefully, which is only indirectly relevant. → *When reporting InferCraft kernel or throughput numbers, state the peak they are measured against and compare with same-kernel numbers from another source, using this video's 99.8%-of-own-ceiling example as the cautionary case.*
