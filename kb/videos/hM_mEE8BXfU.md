# I Ran a 35B Param Model On My iPhone (Local AI)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `hM_mEE8BXfU` · [watch](https://youtu.be/hM_mEE8BXfU) · **date:** 2026-10-02 · **length:** 5:58 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Warren · **orgs:** Better Stack
- **topics:** local-ai, inference-serving · **tags:** mixture-of-experts, ssd-streaming, page-cache, tiered-quantization, iphone, ios, qwen, flash-moe, on-device-inference, xcode

> Better Stack walkthrough of running Qwen 3.5 35B-A3B (a mixture-of-experts model) on an iPhone 17 at about 11 tokens/s by streaming experts from SSD, relying on the OS page cache, and tiered 4-bit/2-bit quantization, with the Flash MoE / Flash iOS setup steps.

## Summary
The presenter runs a 35B-parameter mixture-of-experts model (Qwen 3.5 35B-A3B, about 3B active per token) on an iPhone 17 at roughly 11 tokens per second. Only the always-needed weights (embeddings, attention, routers, shared expert, about 1.4 GB) stay resident in RAM; the roughly 12 GB of routed experts sit on flash and are read on demand, eight per layer per token. The app keeps no expert cache of its own. The authors found that removing their 9.8 GB cache made things 38% faster, because iOS's page cache uses spare RAM better. Tiered quantization keeps the hot experts at 4-bit and drops the cold ones to 2-bit, shrinking the file from about 19 GB to 13 GB. A thinking-loop bug came from a size check that silently skipped the half-size 2-bit experts; the fix is to compare each read against that expert's own size. The engine is Flash MoE (originally a MacBook project by Dan Woods) wrapped by a small iOS port called Flash iOS. The video ends with build and install steps. The results are single-device, single-prompt anecdotes with no quality evaluation, and the presenter notes the phone heats up quickly.

## Key ideas
- **Mixture-of-experts models only activate a small slice per token, so the inactive experts can live on SSD instead of RAM. Qwen 3.5 35B-A3B has 40 layers with 256 experts plus one shared expert, and a router picks 8 per token.** — A 4-bit file is about 20 GB, but only about 1.4 GB (embeddings, attention, routers, shared expert) must stay resident. The roughly 12 GB of routed experts (40 files of about 300 MB) stay on flash. ([0:00](https://youtu.be/hM_mEE8BXfU?t=0))
- **Each token needs 8 expert reads per layer, so about 320 reads per token. Rather than keeping an app-level expert cache, the engine leaves caching to the OS page cache.** — The authors built a 9.8 GB cache of their own, then deleted it, and the result was 38% faster. Any RAM the app grabs is taken from both the GPU and the page cache, and the page cache does most of the work. ([1:57](https://youtu.be/hM_mEE8BXfU?t=117))
- **Streaming every expert from flash would need over 5 GB/s at 11 tok/s, but an iPhone's flash delivers about 1.6 GB/s, so the page cache has to serve most reads.** — This is the bandwidth argument for why the caching behaviour matters at all. ([1:57](https://youtu.be/hM_mEE8BXfU?t=117))
- **Tiered quantization exploits skew in expert usage: about 25% of experts handle about 80% of the work, so hot experts stay at 4-bit and cold ones drop to 2-bit.** — Cold experts are 44% smaller and the whole file shrinks 34%, from about 19 GB to 13 GB. The smaller file fits more of the page cache. Quality impact is not measured in the video. ([3:16](https://youtu.be/hM_mEE8BXfU?t=196))
- **A thinking-loop bug came from an async pre-read size check. Cold 2-bit experts are half the size of hot ones, so they failed the check and were silently skipped.** — The model effectively ran with half its experts and repeated two tokens. The fix is to validate each expert read against that expert's own expected size, not one global size. ([4:28](https://youtu.be/hM_mEE8BXfU?t=268))
- **The on-device setup is a build-and-sideload workflow: clone the repo, patch, build in Xcode with your own team and bundle ID, then push a pre-packed model over USB.** — Requires a paid Apple developer account. The pre-packed tiered model is about 13 GB and took about 7 minutes to transfer over USB. ([4:28](https://youtu.be/hM_mEE8BXfU?t=268))

## Techniques
- **Stream MoE experts from SSD and leave caching to the OS page cache** — Keep attention, embeddings, routers and the shared expert resident in RAM. Memory-map or read each token's selected routed experts from flash per layer. Do not add an app-level expert cache, since it competes with the OS page cache for RAM. The authors measured a 38% speedup from removing their own 9.8 GB cache. *When:* Running a MoE model larger than device RAM, where only a few experts are active per token and the device has fast flash and spare memory.
- **Tiered quantization by expert hotness** — Profile which experts handle most of the routing traffic. Keep the top about 25% (which carry about 80% of the work) at 4-bit and quantize the rest to 2-bit. Pack them into a single tiered model file. *When:* A MoE model needs to fit a memory or storage budget and the routing distribution is skewed. Validate quality afterwards, since the video does not.
- **Validate expert reads against per-expert sizes** — In the async pre-read path (metalinfer.m, function async pre-read weight), check each expert read against that expert's own expected size. Do not use one size for all experts, because mixed-precision experts differ in size. A global check silently skips the smaller ones. *When:* Mixing tensor precisions within one model, where a size-based integrity check would otherwise drop valid data without an error.
- **Build and sideload Flash iOS onto an iPhone (tutorial steps)** — 1) Clone the Flash MoE repo, then apply the pre-read fix to metalinfer.m. 2) Open the Xcode project and set your team and bundle ID. You need a paid Apple developer account. 3) Build a Release build and install it on the iPhone. 4) Download the pre-packed tiered model (about 13 GB). 5) Push the model to the app over USB (about 7 minutes). 6) Open the Flash MoE app, tap the model, and start chatting. *When:* You want to run a large open-weight MoE model locally on an iPhone for experimentation. Expect the phone to heat up under sustained generation.
- **Thinking-loop diagnosis for on-device MoE** — If output repeats the same short token sequence after about 10 words, check whether some expert reads are failing validation and being skipped silently. The model then runs with fewer experts than intended. *When:* Debugging degenerate output from a streamed or partially loaded MoE model.

## Numbers
- Model is 35B total parameters with about 3B active per token. A standard 4-bit file is about 20 GB. ([0:00](https://youtu.be/hM_mEE8BXfU?t=0))
- Resident RAM needed is about 1.4 GB. The routed experts (about 12 GB total, 40 files of about 300 MB) sit on SSD. ([0:55](https://youtu.be/hM_mEE8BXfU?t=55))
- Throughput is about 11 tokens/s on an iPhone 17, with thinking mode enabled. ([0:00](https://youtu.be/hM_mEE8BXfU?t=0))
- Each token needs 320 small expert reads (8 experts across 40 layers). ([1:57](https://youtu.be/hM_mEE8BXfU?t=117))
- Streaming all experts from flash at 11 tok/s would need over 5 GB/s. The iPhone flash delivers about 1.6 GB/s. ([1:57](https://youtu.be/hM_mEE8BXfU?t=117))
- Removing the authors' own 9.8 GB expert cache made inference 38% faster. ([1:57](https://youtu.be/hM_mEE8BXfU?t=117))
- About 25% of experts handle about 80% of the work. Cold experts at 2-bit are 44% smaller, and the whole file shrinks 34% (about 19 GB to 13 GB). ([3:16](https://youtu.be/hM_mEE8BXfU?t=196))
- Pre-packed tiered model is about 13 GB. USB transfer to the phone takes about 7 minutes. ([4:28](https://youtu.be/hM_mEE8BXfU?t=268))

## Hot takes
- The 11 tok/s figure is one device, one model, with thinking mode on. No benchmark or quality comparison against the 4-bit or uniform 2-bit baseline is shown.
- The presenter says the phone heats up noticeably from a single 'hello' prompt, so sustained use may be impractical.
- The 38% speedup from removing the custom cache is presented as a counter-intuitive win. It is a claim about iOS page-cache behaviour, not a controlled experiment.
- The tiered quantization quality cost is not measured. Shrinking the file 34% is shown, but intelligence impact is not.

## Tools mentioned
Flash MoE (Dan Woods; originally written for a MacBook), Flash iOS (iPhone port wrapping the Flash MoE engine), Qwen 3.5 35B-A3B (mixture-of-experts model, 35B total, about 3B active), Xcode, iPhone 17, metalinfer.m (file in the Flash MoE repo), Apple developer account

## Relevance to our work
- **agentos** (1/3): InferCraft (L2B) is built around KV-cache offload and memory-tier strategies on one RTX 5090. The page-cache versus explicit-cache finding and expert-level tiered quantization are adjacent ideas, but this is an iPhone demo with no serving-scale or latency data. → *Read Flash MoE's approach to page-cache-backed weight streaming and compare it with InferCraft's CPU offload, then benchmark an explicit cache against relying on the OS page cache at our memory budget.*
