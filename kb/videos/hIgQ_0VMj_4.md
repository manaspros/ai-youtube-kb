# OpenAI FINALLY Goes Open... 2 NEW models (they're good?)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `hIgQ_0VMj_4` · [watch](https://youtu.be/hIgQ_0VMj_4) · **date:** 2025-11-02 · **length:** 8:44 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** OpenAI, Ollama, OpenRouter, Anthropic, Alibaba (Qwen)
- **topics:** models-research, local-ai, coding-agents · **tags:** gpt-oss, open-weight, local-inference, ollama, openrouter, opencode, benchmarks, mixture-of-experts, apache-2-license

> Hands-on test of OpenAI's open-weight gpt-oss-120b and gpt-oss-20b: the 20B runs locally on a MacBook, the 120B runs via OpenRouter, and coding results are mixed against OpenAI's self-reported benchmarks.

## Summary
The presenter introduces gpt-oss-120b and gpt-oss-20b, OpenAI's first open-weight reasoning models under Apache 2.0, and says they are claimed to beat similarly sized open models. He runs the 20B model locally in Ollama on a MacBook and reports fast local throughput, then runs the 120B model through OpenRouter inside OpenCode. On a single-file polygon-with-bouncing-balls prompt, the 20B output had physics glitches and the 120B output was better. On a multi-file Next.js + tRPC dashboard task, both models struggled, and the model put everything into one page.tsx. A frontend-only prompt (index.html with Tailwind) produced an acceptable but unimpressive dashboard that he judged slightly behind Claude Sonnet 4. He concludes the models won't replace Claude Code for him but are useful offline. He then recaps OpenAI's published benchmarks (Codeforces, AIME 2025, GPQA Diamond) without independently checking them.

## Key ideas
- **OpenAI released two open-weight reasoning models under Apache 2.0, billed as its first open model since GPT-2.** — gpt-oss-120b and gpt-oss-20b. The presenter says OpenAI claims they outperform similarly sized open models on reasoning, with the 120B near o4-mini and the 20B near o3-mini. ([0:00](https://youtu.be/hIgQ_0VMj_4?t=0))
- **The 20B model runs locally on a laptop-class machine.** — Its download is about 12.8 GB and it needs roughly 16 GB of memory. The 120B model needs a single 80 GB GPU, so it is not practical on a MacBook here. ([0:00](https://youtu.be/hIgQ_0VMj_4?t=0))
- **Local speed on a MacBook was good, and the model's self-identity is unreliable.** — Ollama stats: total 31 s, load 47 ms, prompt eval 134 tok/s, generation 36.47 tok/s. When asked what model it was, the 20B claimed to be GPT-4. ([1:15](https://youtu.be/hIgQ_0VMj_4?t=75))
- **On a one-shot single-file coding prompt, the 120B result beat the 20B result, but both had visible flaws.** — The bouncing-balls-in-polygon HTML/JS was generated locally by the 20B model. Balls escaped the polygon and the scene drifted off-screen. The 120B run via OpenRouter had better containment but still some breakouts. ([2:34](https://youtu.be/hIgQ_0VMj_4?t=154))
- **Multi-file, framework-heavy tasks exposed the limits: the model stalled on tRPC and collapsed everything into one file.** — In OpenCode, asking it to read a Next.js project and add a finance dashboard with a backend failed to run. It repeatedly misused tRPC, and the output had no components, just one page.tsx. ([4:38](https://youtu.be/hIgQ_0VMj_4?t=278))
- **Narrowing the scope to a frontend mock produced acceptable output, which he judged roughly comparable to Claude Sonnet 4 but slightly weaker.** — The same prompt with 'mock the front end, skip the back end' yielded index.html with Tailwind. He calls it not far off Sonnet 4 and worth the price gap, but not a replacement for Claude Code. ([5:38](https://youtu.be/hIgQ_0VMj_4?t=338))
- **The vendor benchmarks he recaps place the 120B near o4-mini and the 20B above o3-mini on coding and math, but these numbers are OpenAI-reported and he did not verify them.** — Codeforces Elo: 120B 2622, 20B 2516, Qwen3-235B 2056, Qwen3-32B 1922. AIME 2025: 120B 96.6%, 20B about 96%. GPQA Diamond: 20B 71.5%, behind o3 and o3-mini. ([6:45](https://youtu.be/hIgQ_0VMj_4?t=405))

## Techniques
- **Run gpt-oss-20b locally for offline use** — Install Ollama, pick the GPT-OSS 20B entry in its model selector (about 12.8 GB download), and chat. Terminal output after each reply shows total duration, load duration, prompt eval rate and eval rate. Expect tens of tokens/s on a MacBook-class machine. *When:* Offline or privacy-sensitive experiments, quick iteration without API cost, or checking whether a small local model is good enough for a task.
- **Route the 120B model through OpenRouter inside OpenCode** — In OpenCode, activate the OpenRouter GPT OSS 120B model from the model list. The presenter cites $0.15 per 1M input tokens and $0.60 per 1M output tokens. Streaming speed was very fast at the time of the test. *When:* You want the larger open model without local hardware, or want to compare cost and speed against a frontier API.
- **Scope the prompt to what the model can finish** — Split a large full-stack request into a frontend-only prompt (e.g. 'mock the front end in index.html with Tailwind, no back end') before judging the model. Keep the same prompt across models for a fair comparison. *When:* Evaluating open models for coding work. A failed full-stack run may reflect prompt scope rather than model ability.
- **Use a fixed single-file stress prompt for quick model comparisons** — Use one self-contained prompt (bouncing balls in a rotating polygon, physics, sliders for gravity) and check constraint adherence visually, such as whether balls stay inside the container. Compare outputs side by side. *When:* Quick smoke tests of a new model's code generation before deeper evaluation. It is visual and not a rigorous benchmark.

## Numbers
- gpt-oss-20b context length is 128,000 tokens; the model download is about 12.8 GB; it runs in about 16 GB memory ([0:00](https://youtu.be/hIgQ_0VMj_4?t=0))
- Local 20B on a MacBook via Ollama: total 31 s, load 47 ms, prompt eval 134 tok/s, generation 36.47 tok/s ([1:15](https://youtu.be/hIgQ_0VMj_4?t=75))
- Some providers reportedly serve gpt-oss at about 3,000 tok/s (stated by presenter, unverified) ([1:15](https://youtu.be/hIgQ_0VMj_4?t=75))
- 120B runs on a single 80 GB GPU, near o4-mini on core reasoning (OpenAI claim) ([2:34](https://youtu.be/hIgQ_0VMj_4?t=154))
- OpenRouter pricing for gpt-oss-120b: $0.15 per 1M input tokens, $0.60 per 1M output tokens ([3:58](https://youtu.be/hIgQ_0VMj_4?t=238))
- Codeforces: gpt-oss-120b 2622, gpt-oss-20b 2516, Qwen3-235B 2056, Qwen3-32B 1922 (OpenAI-reported) ([6:45](https://youtu.be/hIgQ_0VMj_4?t=405))
- AIME 2025: gpt-oss-120b 96.6%, gpt-oss-20b about 96%, both above o3 and o3-mini (OpenAI-reported) ([6:45](https://youtu.be/hIgQ_0VMj_4?t=405))
- GPQA Diamond: gpt-oss-20b 71.5%, below o3; gpt-oss-120b beats o3-mini and approaches o4-mini (OpenAI-reported) ([6:45](https://youtu.be/hIgQ_0VMj_4?t=405))

## Hot takes
- Open-weight models finally put the 'open' back in OpenAI (presenter's opinion).
- gpt-oss-20b misidentifies itself as GPT-4, so self-reported model identity should not be trusted for local models.
- Benchmark recap is vendor-reported; the presenter's own coding tests were mixed and did not match the benchmark story.
- Speculation that Horizon Beta stealth models on OpenRouter were OpenAI's was not resolved; the presenter judged by UI quality that they are probably not gpt-oss.
- Open models are good enough to run offline for semi-competent answers, but not a replacement for Claude Code / Sonnet 4 in agentic coding.

## Tools mentioned
gpt-oss-120b, gpt-oss-20b, Ollama (auto-caption 'Alarma'), OpenRouter, OpenCode, Next.js, tRPC, Tailwind CSS, Claude Code, Claude Sonnet 4 (auto-caption 'Claude Sonic 4'), o3, o3-mini, o4-mini, Qwen3 235B, Qwen3 32B, Horizon Beta (OpenRouter stealth model, referenced not tested)

## Relevance to our work
- **agentos** (2/3): gpt-oss-20b is an Apache 2.0 open-weight reasoning model that fits on a 16 GB-class machine. It is a candidate model for the InferCraft serving stack (vLLM on one RTX 5090), and the 120B on a single 80 GB GPU informs sizing. → *Benchmark gpt-oss-20b (and 120B if it fits) on the local RTX 5090 under vLLM with the same single-file and frontend prompts, recording tokens/s, and compare against the current local model in InferCraft.*
- **prosharness** (1/3): The video shows open models failing on multi-file framework tasks (tRPC, Next.js) while a frontend-only scoped task worked, which argues for keeping Claude Code as the default executor in long runs. → *When adding a non-Claude model option to the harness, gate it to scoped, single-file tasks and keep Claude Code for multi-file work; run the same scoped prompt set before enabling it.*
