# Is Speculative Decoding Worth It? Profiling vLLM on NVIDIA Blackwell — Akamai

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `XTpyNrEgJQ4` · [watch](https://youtu.be/XTpyNrEgJQ4) · **date:** 2026-10-07 · **length:** 15:17 · **format:** demo · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Sheila · **orgs:** Akamai
- **topics:** inference-serving, infra-cost-scaling · **tags:** speculative-decoding, vllm, blackwell, kv-cache, acceptance-rate, draft-model, benchmarking, llama, eagle, medusa, ngram, akamai

> Akamai's Sheila explains when speculative decoding pays off on vLLM: spare GPU memory and structured, low-temperature workloads, measured by acceptance rate and tokens/s on a single Blackwell GPU.

## Summary
The speaker, a developer advocate at Akamai, explains that LLM generation has a prefill phase that builds the KV cache once and a decode phase that produces one token at a time. Speculative decoding uses a small draft model to propose 3 to 5 tokens per cycle, and the target model verifies them in a single forward pass, so output quality is unchanged. The approach is not free: the second model needs weight memory and its own KV cache, so it only makes sense with spare GPU capacity, and high-concurrency deployments that keep the GPU busy gain little. Draft model choice balances acceptance (accuracy) against speed, with the draft typically 10 to 50 times smaller and sharing the target's tokenizer. Gains depend on the workload: structured outputs such as JSON, SQL or code get high acceptance and a demo ran about 1.6x faster, while high-temperature creative tasks get low acceptance. Long-context workloads like RAG gain little because speculative decoding speeds up generation, not prefill. The demo ran on one GPU by fitting a baseline server and a speculative server side by side, and the speaker recommends vLLM's documentation as the starting point. The demo had technical problems, so most numbers are anecdotal.

## Key ideas
- **Decoding is the slow phase, one token at a time, while prefill builds the KV cache once** — Prompt processing happens once and fills the KV cache. Generation then runs one token per forward pass, which is costly and adds latency for large models. ([0:12](https://youtu.be/XTpyNrEgJQ4?t=12))
- **Speculative decoding: a small draft model proposes tokens and the big model verifies them in one pass** — The draft model proposes about 3 to 5 tokens per cycle. The target model accepts or rejects them in a single forward pass and recomputes from the first rejected token, so the output matches the target model's. ([1:36](https://youtu.be/XTpyNrEgJQ4?t=96))
- **It is not free and needs spare GPU memory** — Two models mean extra weight memory and extra KV cache space for both. If the GPU is already busy serving many concurrent requests, speculative decoding is unlikely to pay off. ([3:05](https://youtu.be/XTpyNrEgJQ4?t=185))
- **Choosing a draft model trades accuracy against speed** — The draft should be 10 to 50 times smaller than the target and ideally share its tokenizer or model family. Check both how often its tokens are accepted and whether it is actually faster. ([3:58](https://youtu.be/XTpyNrEgJQ4?t=238))
- **The workload decides the acceptance rate** — Structured output (JSON, SQL, code) suits speculative decoding. Creative, high-temperature tasks give more varied next tokens and therefore lower acceptance and little gain. ([5:35](https://youtu.be/XTpyNrEgJQ4?t=335))
- **Measure acceptance rate and tokens/s on baseline vs speculative runs per workload** — In the demo, the structured task ran about 1.6x faster with high acceptance. The creative task showed low acceptance. Acceptance rate and throughput are the two metrics to check before enabling it. ([8:53](https://youtu.be/XTpyNrEgJQ4?t=533))
- **Long prompts with short answers (RAG, document analysis) gain little** — Speculative decoding accelerates token generation, not reading the prompt. If the prompt is much longer than the output, prefill dominates and the speedup is small. ([10:13](https://youtu.be/XTpyNrEgJQ4?t=613))
- **vLLM is the simplest starting point; n-gram, Medusa and EAGLE are more advanced options** — The speaker used vLLM with a separate draft model. Other methods such as n-gram, Medusa and EAGLE have more complex internals. Blogs and two research papers are suggested for background. ([13:02](https://youtu.be/XTpyNrEgJQ4?t=782))

## Techniques
- **Draft-model speculative decoding** — Serve a small draft model next to the target model in vLLM. The draft proposes about 3 to 5 tokens per cycle, and the target verifies them in one forward pass. Rejected tokens are recomputed by the target. *When:* When the GPU has spare memory, concurrency is low to moderate, and the output is long or structured.
- **Acceptance-rate-first benchmarking** — For each workload, run baseline and speculative servers with the same prompts. Compare acceptance rate (accepted tokens divided by draft-generated tokens) and tokens/s before deciding. *When:* Before turning speculative decoding on in production, or to compare workload types.
- **Draft model selection checklist** — Pick a draft 10 to 50 times smaller than the target, with the same tokenizer or family. Check accuracy (acceptance) and speed/cost together. *When:* When choosing or swapping the draft model.
- **Side-by-side A/B on one GPU** — Choose a small enough draft so the baseline and speculative servers fit on the same GPU, with the memory split between them. The speaker's example had about 16 GB of target weights and 2.5 GB of draft weights. *When:* When only one GPU is available and you want a direct comparison.
- **Workload triage before enabling** — Ask whether the output is highly structured, whether the GPU has spare VRAM, whether requests are creative or high-temperature, whether concurrency is high, and whether the prompt is much longer than the output. *When:* As a go or no-go check before setting up speculative decoding.

## Numbers
- Draft model proposes about 3 to 5 tokens per speculation cycle ([1:36](https://youtu.be/XTpyNrEgJQ4?t=96))
- Draft model typically 10 to 50 times smaller than the target model ([3:58](https://youtu.be/XTpyNrEgJQ4?t=238))
- In the demo setup, the baseline target model used about 16 GB of weights and the draft model about 2.5 GB, leaving most GPU memory for KV cache ([3:58](https://youtu.be/XTpyNrEgJQ4?t=238))
- Structured-output demo ran about 1.6x faster with speculative decoding, with high acceptance rate and higher tokens/s ([8:53](https://youtu.be/XTpyNrEgJQ4?t=533))
- Creative high-temperature demo showed low acceptance rate and therefore little benefit; no figure given ([10:13](https://youtu.be/XTpyNrEgJQ4?t=613))
- A 70B-class model may need up to hundreds of forward passes for a response without speculation, per the speaker ([0:12](https://youtu.be/XTpyNrEgJQ4?t=12))

## Hot takes
- Speculative decoding is not free: a second model adds memory and KV-cache cost, so it only helps when the GPU has spare room.
- Whether speculative decoding helps depends more on the workload (structured vs creative, output vs prompt length) than on the model choice.
- For long-context RAG or document analysis, speculative decoding speeds up the wrong phase because prefill dominates.

## Tools mentioned
vLLM, Llama 70B, NVIDIA Blackwell GPU, EAGLE, Medusa, n-gram speculative decoding

## Relevance to our work
- **agentos** (2/3): InferCraft (L2B) already plans speculative decoding (EAGLE-3) on one RTX 5090 with vLLM. The talk gives a benchmarking method for that single-GPU setup: acceptance rate and tokens/s split by workload type, and a memory-fit check for running the baseline and speculative servers together. → *Before enabling EAGLE-3 in InferCraft, run structured-output and creative prompts on the 5090 for baseline and speculative servers. Log acceptance rate and tokens/s for each, and check whether there is enough spare VRAM for the draft model's KV cache.*
