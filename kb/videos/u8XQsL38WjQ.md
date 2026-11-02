# I Ran a Local LLM on 12-Year-Old Raspberry Pi (It Actually Worked!)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `u8XQsL38WjQ` · [watch](https://youtu.be/u8XQsL38WjQ) · **date:** 2026-06-02 · **length:** 10:11 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Andrus · **orgs:** Better Stack, Technology Innovation Institute, IBM, Raspberry Pi
- **topics:** local-ai, inference-serving · **tags:** raspberry-pi, llama.cpp, quantization, gguf, arm, armv6, cross-compilation, small-models, falcon-h1, edge-inference, mamba, hybrid-architecture

> Better Stack runs the 90M-parameter Falcon H1 Tiny on a 2014 Raspberry Pi 1 by cross-compiling llama.cpp for ARMv6 and testing 2/4/8-bit quants; it works, but is far too slow and thin on knowledge to be useful.

## Summary
The speaker (Andrus, Better Stack) tries to run a small language model on a first-generation Raspberry Pi with 512 MB RAM and an ARMv6 single-core CPU. He picks Falcon H1 Tiny (90M parameters, hybrid transformer plus Mamba) and argues for legacy Q4-style quantization over IQ quants, because IQ formats need CPU instructions the Pi lacks. Compiling llama.cpp on the Pi would take an estimated 18 hours, so he cross-compiles it on a Mac with flags that disable shared libs, NEON and OpenMP, then copies the binary over SSH. He runs with one thread, a 128-token context, a 32-token output cap and mmap disabled for memory stability. The 2-bit model produces near-nonsense at roughly one token every three seconds, the 4-bit model gives a coherent greeting, and the 8-bit model answers a capital-city question wrong for Albania but right for Belgium. His verdict: theoretically possible, but not fast, not precise and not for production.

## Key ideas
- **Falcon H1 Tiny is a 90M-parameter model from the Technology Innovation Institute, built to probe the lower bound of language modeling.** — Chosen as the candidate small enough for a 512 MB board. Speaker says it is probably among the smallest AI models available; not verified in the video. ([0:00](https://youtu.be/u8XQsL38WjQ?t=0))
- **The model uses a hybrid transformer plus Mamba architecture, the same family IBM used for its tiny Granite 4 models.** — Speaker presents this as the reason the model can be so small; he links an earlier video on Granite 4. ([1:08](https://youtu.be/u8XQsL38WjQ?t=68))
- **Pick legacy Q4 quantization over IQ quants on old CPUs.** — Falcon ships in 2-, 4- and 8-bit variants. IQ (importance) quants rely on bit manipulation that needs modern CPU instructions, which the ARMv6 Pi lacks. Q4 is the speaker's chosen middle ground for size versus quality. ([1:08](https://youtu.be/u8XQsL38WjQ?t=68))
- **Native compilation on the Pi is impractical, so cross-compile on a laptop.** — Speaker estimates about 18 hours on the Pi, likely ending in out-of-memory failure. He builds on a Mac instead, targeting ARMv6 with VFP enabled, then copies the binary over SSH. ([2:17](https://youtu.be/u8XQsL38WjQ?t=137))
- **Disable mmap when loading the model on a 512 MB 32-bit board.** — Speaker says mmap can fail on 32-bit systems when no contiguous address space is free. Disabling it loads the weights into the heap, which gives more predictable memory use. ([5:50](https://youtu.be/u8XQsL38WjQ?t=350))
- **Quantization level is a sharp quality cliff at this size.** — The 2-bit model gives near-nonsense output at about one token every three seconds. The 4-bit model returns a coherent greeting, which the speaker treats as the proof point. ([7:01](https://youtu.be/u8XQsL38WjQ?t=421))
- **Tiny models lose long-tail facts first.** — The 8-bit model misses the capital of Albania (says it is wrong) but answers Belgium correctly. Speaker attributes this to limited capacity in 90M parameters, so lesser-known facts are dropped. ([8:17](https://youtu.be/u8XQsL38WjQ?t=497))
- **Speaker's bottom line: feasibility demo, not a deployable system.** — He says it is not fast, not precise, and not for production, except perhaps for a very slow robot. The point was that it is theoretically possible. ([8:17](https://youtu.be/u8XQsL38WjQ?t=497))

## Techniques
- **Pick the OS image for a low-RAM board** — Flash Raspberry Pi OS Lite (32-bit) with Raspberry Pi Imager. In the advanced settings, pre-configure Wi-Fi and enable SSH so the board can be managed remotely. Speaker says the desktop OS idles at much more memory than Lite. *When:* Any headless Pi with 512 MB RAM where most memory should go to the model.
- **Cross-compile llama.cpp for ARMv6 on a laptop** — Clone llama.cpp and create a separate build directory. Use a cross-compiler toolchain on the host (the speaker calls it DocCross and says it runs on a Mac and emits Pi-legacy binaries). Target ARMv6 with the VFP math unit enabled. Configure with shared libs off (single portable binary), NEON off (Pi lacks it) and OpenMP off (lower memory). Build (about 2 minutes on his Mac), then scp the binary to a fresh directory on the Pi. Exact CMake flag names are not shown on screen. *When:* Targeting a CPU older than the one your libraries assume (no NEON), where on-device compilation would take hours or run out of memory.
- **Minimal-footprint inference invocation** — Prompt with a short input (speaker uses hello, how are you?). Cap output at 32 tokens. Use exactly one thread. Set context to 128 tokens. Disable mmap so weights load into the heap. Run the cross-built binary against the Q2, Q4 and Q8 Falcon H1 Tiny GGUF files. Flag names beyond the no-mmap option are not given in the transcript. *When:* Checking whether a model fits and runs on very constrained hardware, before tuning for speed.
- **Stepwise quantization sweep with graded probes** — Download the 2-, 4- and 8-bit variants, copy them over one at a time and test in order. Use a simple greeting first to check the model is coherent, then a factual question (capital of Albania, capital of Belgium) to see how much knowledge survived. *When:* Choosing the largest quant that still gives coherent output on a given device, and spotting knowledge loss that a greeting test would miss.

## Numbers
- Raspberry Pi 1 (2014): 700 MHz single-core CPU, 512 MB RAM. ([0:00](https://youtu.be/u8XQsL38WjQ?t=0))
- Falcon H1 Tiny: 90M parameters, released in 2-, 4- and 8-bit quantizations. ([0:00](https://youtu.be/u8XQsL38WjQ?t=0))
- Estimated native llama.cpp compile time on the Pi: about 18 hours, possibly failing with out-of-memory first. ([2:17](https://youtu.be/u8XQsL38WjQ?t=137))
- Cross-build on a Mac took about 2 minutes. ([4:40](https://youtu.be/u8XQsL38WjQ?t=280))
- 2-bit model throughput: about one token every three seconds. ([7:01](https://youtu.be/u8XQsL38WjQ?t=421))
- Test run settings: 1 thread, 32-token output cap, 128-token context. ([5:50](https://youtu.be/u8XQsL38WjQ?t=350))

## Hot takes
- Speaker: a 90M model can run on a 12-year-old Pi but is 'not fast' and 'not precise', and 'the practical implementation is useless' though still cool.
- Small-model knowledge is capacity-limited: lesser-known facts go first, which he uses to explain the Albania miss.
- Claims 'probably the smallest AI models currently out there' without verification in the video.
- Single-prompt, single-machine demo: no quality benchmark, so the 4-bit 'success' rests on one greeting.

## Tools mentioned
llama.cpp, Falcon H1 Tiny (90M, Technology Innovation Institute), Raspberry Pi OS Lite 32-bit, Raspberry Pi Imager, cross-compiler toolchain (spoken as DocCross), ssh / scp, Mamba, IBM Granite 4 (mentioned)

## Relevance to our work
- **agentos** (1/3): InferCraft targets a single RTX 5090 with vLLM and quantization (NVFP4); this video shows CPU-only quant choice depends on the target ISA, which matters only if we add a CPU or edge fallback. → *Low priority: if InferCraft ever needs a CPU or edge tier, check the target CPU instruction set before choosing a quant format; IQ quants need modern CPU instructions.*
