# Inference learning path (after "Inference Engineering", Kiely 2026). Updated 2026-11-12.

Goal: go from survey-level to code/math-level on LLM serving, then kernels; end with a public 5090 benchmark,
one merged SGLang/vLLM PR, and a December flagship (fused Triton decode kernel vs Raft). Pure DL research is not the track:
evidence (2026-11 sweep) says serving/kernel systems is where junior demand outpaces people.
V = page fetched and checked, u = search snippet only.

## What to learn from each (in order)
| # | Resource | Link | Learn this | Skip |
|---|---|---|---|---|
| 1 | JAX scaling book, Inference (V) | https://jax-ml.github.io/scaling-book/inference | FLOPs/token = 2 x active params; KV bytes/token = 2 x bytes x kv_heads x head_dim x layers; decode step = (B x KV + weights) / bandwidth; critical batch | TPU-specific sharding |
| 1 | fleetwood.dev, domain-specific architectures (V) | https://fleetwood.dev/posts/domain-specific-architectures | Why inference is memory-movement bound; KV sizing MHA vs MLA; hardware design consequences | — |
| 2 | zero-to-sglang Part I (V) | https://github.com/datawhalechina/zero-to-sglang | Skim only: GPU arch, metrics (TTFT, TPOT, ITL, goodput) | Concepts the book already covered |
| 2 | zero-to-sglang Part II (V) — **spine** | same | Build mini-sglang: continuous batching, paged KV, RadixAttention, TP, speculative decoding | — |
| 2 | Aleksa Gordic, Inside vLLM (V) | https://aleksagordic.com/blog/vllm | vLLM V1 engine: step loop, scheduler token budget, KV block alloc, chunked prefill, prefix hashing, spec decode, PD connector. Pinned to Aug 2025 commit: check names vs main | Multi-node + serving sections on first pass |
| 2 | nano-vLLM (V, optional) | https://github.com/GeeeekExplorer/nano-vllm | ~1,200-line engine; add chunked prefill yourself | If Part II already done |
| 3 | vllm bench serve (V), GuideLLM (V) | https://docs.vllm.ai/en/latest/benchmarking/cli/ , https://github.com/vllm-project/guidellm | Benchmark protocol: arrival model, concurrency knee P90/P99, goodput; prefix-cache warm-up pitfall | — |
| 4 | Leviathan et al. 2211.17192 (V), EAGLE-3 2503.01840 (u), vLLM spec-decode docs (V) | https://arxiv.org/abs/2211.17192 , https://docs.vllm.ai/en/latest/features/speculative_decoding/ | E[tokens/step] = (1 - a^(g+1)) / (1 - a); acceptance per workload; loses at high concurrency | — |
| 5 | zero-to-sglang Part III + IV (V) | same | Real SGLang internals (attention backends, quant, HiCache); PR workflow | — |
| 6 | Triton-Puzzles (V) | https://github.com/srush/Triton-Puzzles | Block indexing, masking; runs on CPU interpreter (Mac OK) | — |
| 6 | FlashAttention 2205.14135, FA2 2307.08691 (V) | https://arxiv.org/abs/2205.14135 | Tiling, online softmax, HBM traffic argument | — |
| 6 | FlashAttention the Hard Way pt 1 (V) | https://labs.cloudrift.ai (was riftstack.ai/research/learning-flashattention-the-hard-way-part-1) | Online softmax as associative (m, d, o) merge, proof-level. No code | Until writing the kernel |
| 6 | QuACK memory-bound speed-of-light (not evaluated) | https://github.com/Dao-AILab/quack/blob/main/media/2025-07-10-membound-sol.md | Getting memory-bound kernels to peak bandwidth (decode is memory-bound) | — |
| 6 | Twill, arXiv 2512.18134 (abstract only) | https://rohany.github.io/publications/twill.pdf | SMT-solved software pipelining / warp specialization for FA on Hopper/Blackwell | Read last |
| — | Inference-Engineering repo (V) | https://github.com/navaneethkrishnansuresh/Inference-Engineering | — | **Skip**: unfinished, stops at paged KV; zero-to-sglang covers it |

Extra reading (u): PyTorch int4 decoding blog (INT4 KV gave no latency win despite 4x fewer bytes) https://pytorch.org/blog/int4-decoding/ ;
vLLM Triton attention backend deep dive https://vllm.ai/blog/2026-03-04-vllm-triton-backend-deep-dive ;
survey "Taming the Titans" https://arxiv.org/abs/2504.19720 ; CMU 11-868 LLM Systems https://llmsystem.github.io/llmsystem2026fall/

## Overlap (who teaches what; ★ = best single source, read only that one first)
| Topic | Book | JAX | Fleetwood | ZtS I | ZtS II | ZtS III | Gordic vLLM | nano-vLLM | Inf-Eng repo |
|---|---|---|---|---|---|---|---|---|---|
| Prefill vs decode, roofline | x | ★ | x | x | | | x | | x |
| KV cache sizing math | | ★ | x | x | | | | | |
| Paged KV / block manager | x | | | | ★ | | x | x | x |
| Continuous batching / scheduler | x | | | | ★ | | x | x | x |
| Chunked prefill | x | | | | | | ★ | (add it) | |
| Prefix cache / radix tree | x | | | | ★ | | x (hash blocks) | x | |
| Speculative decoding | x | | | | ★ | | x | | |
| Benchmark metrics | x | | | ★ | | | x | | |
| PD disaggregation | x | | | | | x | ★ | | |
| Attention backends / kernels | | | | | | ★ | | | |
| PR / contribution workflow | | | | | | ★ (Part IV) | | | |

Takeaways: zero-to-sglang Part II + Gordic vLLM together cover the whole serving core; nano-vLLM and the Inference-Engineering
repo are redundant once those are done. The book and ZtS Part I overlap almost fully: skim Part I.

## Risks / open
- PR target: SGLang (course Part IV, core-team authors) vs vLLM (more job postings name it). Leaning SGLang.
- RTX 5090 is SM120: Triton sm_120 failures reported (forum, u); SM100 kernels (DeepGEMM, CUTLASS SM100) reported failing on SM120 (community repo, u). Run a tiny kernel first.
- Flagship decision (Triton kernel vs Raft) due December 2026 break.
