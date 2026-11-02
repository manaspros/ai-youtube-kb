# Guide: local-ai

*Synthesized 2026-11-02 by Haiku from 216 videos. Open a video: `kb/videos/<id>.md`.*

Sources: mostly Kai Explains, plus Better Stack (`kJppefEh2ZA`, `Wik_JQ-enUA`, `eskgvQYchd0`) and two AI Engineer conference talks (`4n08JHb90hI`, `9-Y_oS9OBLc`). No AI LABS videos show up in these notes. Most claims come from one creator testing one machine. Treat vendor numbers as vendor numbers.

## State of the art

- Local AI now fails on the memory budget and on prompt reading (prefill), not on whether the weights load. Kai makes this case for 16 GB cards, Macs and PS5-class boxes (`i9mRnbdDYxk`, `x_qmqqp6d7s`, `TgmC_VZEKTE`). The conference workshop agrees for vLLM serving (`4n08JHb90hI`).
- Decode speed is capped by memory bandwidth divided by bytes read per token. The cap is a useful sanity check on vendor claims (`qZTmBhKz7b0`, `L7noXCBSObc`, `vLqswKyHS64`).
- Mixture-of-experts models are the main route to big models on small GPUs. Experts sit in system RAM or on SSD, and a cache keeps the hot ones on the GPU (`m0VHx73SAG0`, `shl8FFSoANE`, `mED-boddeWI`). Lookup-table layers can also live off-GPU (`MPrQA-M4Zn4`, `1--PzaHafAU`).
- Qwen 3.8 27B is the default local dense model in this set (`qZTmBhKz7b0`, `h_KqS4GtU3I`, `i9mRnbdDYxk`). Its built-in multi-token-prediction head can act as a draft model (`qZTmBhKz7b0`, `uavLRbbfM94`).
- Local hardware got more expensive while hosted open-weight tokens got cheaper. Memory prices drive the change (`Y226-wwfCSw`, `L4UV6b2Xc64`). Several videos now argue that buying to save on tokens rarely pays (`3hMEcJCGne0`, `Y226-wwfCSw`). `eckOsa0kBkY` finds old V100s still work for decode.
- Local models are not private by default. A GGUF chat template is executable Jinja, and a model file can act on the machine (`3mx84MRj8lY`, Kai, single talk).

## Consensus patterns

1. Measure prefill and decode separately, at the real prompt size. Report time to first token and decode tokens/s as two numbers (`12lxN9NHuHc`, `x_qmqqp6d7s`, `aQKGejbv-Rs`, `IMVjEsKX5UQ`, `dlyic4oco4s`, `4n08JHb90hI`).
2. Estimate the decode ceiling as bandwidth divided by weight bytes read per token. Compare every claimed tok/s against it (`qZTmBhKz7b0`, `ugKAkCVBcz0`, `3hMEcJCGne0`, `vLqswKyHS64`).
3. Compute KV cache bytes per token from the model config. Count only layers that store a cache, not all layers (`LqAxNIalgOw`, `n-_e9bROGHo`, `i9mRnbdDYxk`).
4. Budget memory as weights plus KV cache plus runtime overhead plus headroom. Check the usable GPU share, which is often below the box's advertised memory (`uavLRbbfM94`, `NA9D49kQFuU`, `6tihP50zlcE`, `aQKGejbv-Rs`).
5. Keep the prompt prefix stable for prefix caching. A changing token near the top of a system prompt can make every turn a cache miss (`x_qmqqp6d7s`). Editing early context also breaks the cache (`9-iiHFQyzuM`).
6. Judge a quantized build on your own eval, not the vendor's. Pick the file by uploader and bit allocation, not by name (`ugKAkCVBcz0`, `P1K36q76Uzk`, `JPHT9AvoPSA`, `1--PzaHafAU`).
7. Benchmark with a fixed protocol. Record engine version, file hash, cache state (cold or warm), output length, and whether speculative decoding is on. Use the same settings on both sides (`qZTmBhKz7b0`, `0F63pTS8Gt0`, `eskgvQYchd0`).
8. Fix sampler and reasoning settings before judging a model. A reasoning budget can truncate thinking, and a default repeat penalty can cause loops (`h_KqS4GtU3I`, `Wik_JQ-enUA`).
9. Use local hardware for batch work and hosted endpoints for interactive turns. Time to first token decides which fits (`1--PzaHafAU`, `3R7yba577uA`, `4n08JHb90hI`).
10. Break-even uses hardware price divided by hosted price per million tokens. Include electricity, utilization and resale (`L4UV6b2Xc64`, `3hMEcJCGne0`, `Y226-wwfCSw`, `eckOsa0kBkY`).
11. Check the runtime log for the accelerated path before trusting any number (`12lxN9NHuHc`).
12. Check the interconnect before adding GPUs. Tensor-parallel decode over PCIe can get slower as cards are added (`eckOsa0kBkY`).

## Disagreements & open questions

- Prefill or decode? Most of the videos in this set say prefill dominates agent wait time (`x_qmqqp6d7s`, `aQKGejbv-Rs`, `12lxN9NHuHc`). Some pieces still lead with decode bandwidth (`3hMEcJCGne0`, `eckOsa0kBkY`). For agents, prefill is the better number to track.
- Is local ever cheaper than hosted tokens? `3hMEcJCGne0` and `Y226-wwfCSw` say rarely. `eckOsa0kBkY` finds the economics work for cheap used cards. `9-Y_oS9OBLc` (AI Engineer talk) says self-hosting only wins above a GPU utilization threshold that depends on the hardware tier. The answer depends on utilization. Nobody in this set has settled it.
- Headline speed claims shrink under a fair baseline. A "2x" Mac result came from speculative decoding, not the engine (`qZTmBhKz7b0`). The llama.cpp expert-cache "4x" is about 1.5-2.2x against tuned layer splits (`shl8FFSoANE`). The Strata "6x" is about 2-2.5x like-for-like (`m0VHx73SAG0`). A 200 tok/s Mac figure was a projection, with about 80 measured (`L7noXCBSObc`).
- Strata and Avalon disagree. Avalon reports a 47% win over Strata on AMD, but Strata's table was stale when posted (`0F63pTS8Gt0`). Strata's RAM cost is the open issue (`mED-boddeWI`, `Y226-wwfCSw`).
- Quantization retention depends on the test. A 1.75-bit 27B keeps 98% of FP16 on a thinking average but about 75% on agentic tasks (`P1K36q76Uzk`). The 2-bit to 3-bit trade-off depends on workload (`m0VHx73SAG0`, `JPHT9AvoPSA`).
- Opus benchmark numbers differ between videos. `LqAxNIalgOw` gives 78.2 vs 73.0 on Terminal Bench 2.1, and `3R7yba577uA` gives about 89. Check the source before quoting either.
- Vendor scores need a second source. MiniCPM5's SWE-bench number is vendor-reported (`Wik_JQ-enUA`). Phonon 2's speed and accuracy claims rest on its own benchmarks (`eskgvQYchd0`). The independent leaderboard disagrees with the vendor on some sets.
- Long context is still unproven. The recall limit near 400k tokens for one model is anecdotal (`RlRC_6hbBHc`). Context-editing gains are mostly compute, not accuracy (`9-iiHFQyzuM`).

## How thinking changed over time (dated)

- 2026-10-02: Buying advice focused on VRAM per dollar and bandwidth per dollar (`L4UV6b2Xc64`, `12lxN9NHuHc`, `3R7yba577uA`).
- 2026-10-12 to 10-19: Attention moved to prefill, cache hits, and task completion. Kai's pieces argued that a model that loads is not a model that finishes (`i9mRnbdDYxk`, `aQKGejbv-Rs`, `x_qmqqp6d7s`, `eckOsa0kBkY`). Hardware price rises became the main theme (`Y226-wwfCSw`).
- 2026-10-12: The AI Engineer workshop (`4n08JHb90hI`) framed self-hosting as an ops problem: memory budget, concurrency knee, tail latency.
- 2026-10-22 to 10-23: Security became part of local setup (`3mx84MRj8lY`). Expert caches in llama.cpp moved the main speed story to hit rate (`shl8FFSoANE`).
- 2026-10-26 to 11-01: Reviews got stricter about headlines. Speed claims were judged by fair baselines and by time to finish a task (`RmE4G6MhOVU`, `0F63pTS8Gt0`, `mED-boddeWI`).
- 2026-10-31: AI Engineer talk on task-level cost (`9-Y_oS9OBLc`).

## Numbers worth remembering

- Decode ceiling: 16 GB of 4-bit weights on 614 GB/s gives about 38 tok/s. A measured 30.5 tok/s is about 80% of that (`L7noXCBSObc`).
- A 27B dense model at 6-bit is about 20.5 GB of weights. With 128K context, about 28.5 GB total (`uavLRbbfM94`).
- Qwen 27B-class KV cache is about 64 KB per token. At 262K tokens, about 16 GB (`LqAxNIalgOw`). Devstral Small 2 is about 160 KB per token (`i9mRnbdDYxk`).
- DeepSeek V4.1 Flash KV cache is about 890 bytes per token, against 389,120 for the 2023 V1 model. Kai calls the headline ratio 437x and notes it compares unlike models (`n-_e9bROGHo`).
- Prefill: a 32K prompt at 50 tok/s takes about 10m40s (`1--PzaHafAU`). A 30K prompt at about 325 tok/s takes about 92 s (`IMVjEsKX5UQ`). A cold 128K prompt on a laptop takes about 170 s by Microsoft's own test (`aQKGejbv-Rs`).
- Cache: one M5 Pro session gave 6.1 s to first word on a cache hit and 268 s when about 41k of 188k tokens missed the cache (`x_qmqqp6d7s`). On DeepSeek's API a cache hit costs about $0.003 per million tokens, a miss about $0.15 (`RlRC_6hbBHc`).
- Expert cache: decode went from 9.7 to 37.2 tok/s on one card (`shl8FFSoANE`). Kai's go/no-go cut-offs for hit rate are 85% and 90%.
- Speculative decoding: on a 7-token draft, the video's run accepted about 2.5 tokens per step (`L7noXCBSObc`). A multi-token head moved one 27B setup from 27 to 46 tok/s (`uavLRbbfM94`).
- Quantization agreement with the reference model: 91.2% at 2-bit, 95.1% at 3-bit, 98.5% at 4-bit (`JPHT9AvoPSA`).
- Hosted limits: Kaggle's free tier gives about 30 GPU hours a week. A 100 s proxy timeout returned 524 errors on slow first tokens (`IMVjEsKX5UQ`).
- Hardware prices: DGX Spark went from $3,999 to $6,950, a 74% rise (`Y226-wwfCSw`). A used RTX 3090 rose from $639 to $946 (`L4UV6b2Xc64`).
- Mac Studio M5 Ultra base is $5,499 with 96 GB at 1.2 TB/s (`12lxN9NHuHc`).
- Reasoning load: one GPQA question used about 15k thinking tokens (`h_KqS4GtU3I`). Terminal Bench averaged about 52k tokens per task (`h_KqS4GtU3I`).
- Notes-file handoff and context edits: one agent run rewrote its own memory 163 times while staying under 8k working tokens (`9-iiHFQyzuM`).

## Watch first

- `i9mRnbdDYxk`: the clearest 16 GB budget walkthrough. Shows how KV cache and tool output eat the window.
- `x_qmqqp6d7s`: prefill vs decode on a Mac, with the cache-miss example and the silent cache-breakers.
- `qZTmBhKz7b0`: how to read speed headlines, with the warm and cold benchmark method.
- `4n08JHb90hI`: AI Engineer workshop. Memory budget, concurrency knee, one-flag-at-a-time tuning. Good for serving design.
- `1--PzaHafAU`: why prefill decides local vs hosted for interactive agents, and batch work as the local use case.
- `3mx84MRj8lY`: local model security. Chat templates, exposed ports, runner patches. Single talk, but the checklist is concrete.

## Implications for our projects

AgentOS (InferCraft on one RTX 5090):
- The 5090 has about 1792 GB/s (`vLqswKyHS64`). That gives a rough single-stream decode ceiling near 110 tok/s on a 16 GB 4-bit model. Our own TTFT at 32K to 100K prompts matters more for agents (`x_qmqqp6d7s`, `4n08JHb90hI`, `RlRC_6hbBHc`).
- Use the workshop's memory budget and concurrency sweep for the vLLM path: weights, then KV pool, then the knee (`4n08JHb90hI`).
- Speculative decoding needs a measured acceptance rate. A badly matched drafter can cut throughput (`4n08JHb90hI`, `L7noXCBSObc`). Our planned EAGLE-3 should get the same check.
- Adopt the provenance checklist and cold/warm protocol before publishing any tok/s number (`0F63pTS8Gt0`, `qZTmBhKz7b0`).
- For MoE on one card, the expert-cache idea (`shl8FFSoANE`) is worth a test with its hit-rate gates.

- Check every proxy and tunnel timeout against measured TTFT at real prompt sizes. A 100 s limit returned 524s when first tokens were slow (`IMVjEsKX5UQ`).

ProsHarness (Claude Code harness):
- Keep volatile values out of the system prompt prefix. Log cache-read tokens per turn. A changing token near the top made every turn a miss (`x_qmqqp6d7s`).
- Checkpoint and resume should append, not rewrite old context. An edit near the top cost 7.7x a normal turn and cut the hit rate sharply (`9-iiHFQyzuM`).
- Cap tool output. Tool output is the main source of context growth (`i9mRnbdDYxk`).
- Batch jobs such as bulk classification, embeddings and nightly runs over logs can run on a local model. Keep the interactive turns on hosted endpoints (`1--PzaHafAU`).

Cheap-model (Haiku) pipelines:
- For bulk classification, local models can cut cost. Use a calibrated confidence gate, and tune the cut on labelled data. A 0.8 gate sent most traffic upstream in one test (`Oi4JPj58lUA`).
- Measure the escalation rate, not just accuracy, when a gate is in place (`Oi4JPj58lUA`).

Security:
- If we self-host any model with tool access, keep the server on loopback or behind authentication. Inspect GGUF chat templates before serving (`3mx84MRj8lY`).
