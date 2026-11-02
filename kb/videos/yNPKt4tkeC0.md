# DeepSeek V3: The BEST AI for Coding

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `yNPKt4tkeC0` · [watch](https://youtu.be/yNPKt4tkeC0) · **date:** 2025-11-02 · **length:** 5:19 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** DeepSeek, Meta, OpenAI, Anthropic, NVIDIA
- **topics:** models-research, token-cost-efficiency, evals · **tags:** deepseek-v3, open-weights, openai-compatible-api, pricing, benchmarks, aider-polyglot, aidanbench, chatbot-arena, swe-bench, self-hosting, terms-of-service

> Better Stack overview of DeepSeek V3 as a cheap open-weight coding model: free chat, OpenAI-SDK drop-in use, vendor and independent benchmark rankings, and a Reddit terms-of-service caveat.

## Summary
The video introduces DeepSeek V3 as an open-weight model that the speaker says matches closed models such as GPT-4o and Claude Sonnet on many benchmarks at much lower price. It shows the free web chat at chat.deepseek.com and a single LeetCode-style test. It says the API works with the OpenAI SDK by changing the base URL, API key and model name, and it quotes per-million-token prices and a training cost of about $5.6M. Benchmark coverage is split: DeepSeek's own results are strong on math and Codeforces but second to Claude Sonnet on MMLU-Pro, GPQA Diamond and SWE-bench. Independent results are mixed, with Aider Polyglot second behind o1 and AidanBench 22nd on output diversity, and Chatbot Arena seventh. The speaker concludes it has the best price-to-performance so far and suggests switching from GPT-4o, while noting Reddit concerns about deepseek.com terms and that self-hosting or third-party hosting is possible.

## Key ideas
- **DeepSeek V3 is presented as an open-weight model that competes with closed frontier models at much lower price.** — The speaker says it beats GPT-4o on most benchmarks at a fraction of the cost and matches ChatGPT and Claude tier models; the claim rests on the benchmark sections that follow. ([0:00](https://youtu.be/yNPKt4tkeC0?t=0))
- **Free web chat is available for trying the model without setup.** — The speaker points to chat.deepseek.com, says sign-in is free at the time, and runs one LeetCode-style problem as a test. ([0:00](https://youtu.be/yNPKt4tkeC0?t=0))
- **The API is a drop-in replacement for an existing OpenAI SDK setup.** — The speaker says you change the base URL, the API key and the model name, and nothing else. The video does not show the actual base URL or model string. ([1:22](https://youtu.be/yNPKt4tkeC0?t=82))
- **Pricing is the main argument for switching.** — The speaker quotes about 1.4 cents per million input tokens and 28 cents per million output tokens, against GPT-4o at $2.50 input and $10 output. He suggests checking any LLM in an application on price alone. ([1:22](https://youtu.be/yNPKt4tkeC0?t=82))
- **Training cost is claimed to be far below comparable frontier runs.** — The speaker says V3 (671B parameters) used about 2,000 H800 GPUs for two months, roughly 2.8M GPU hours and $5.6M. He compares this with about 30.8M GPU hours for Llama 3 405B on 16,000 H100s, described as about 11x the compute. ([1:22](https://youtu.be/yNPKt4tkeC0?t=82))
- **Vendor benchmarks put DeepSeek V3 near the top, with clear weak spots.** — On DeepSeek's own numbers it is second on MMLU-Pro and GPQA Diamond behind Claude Sonnet, strong on MATH-500 and AIME, ahead on Codeforces, and behind Claude Sonnet on SWE-bench. ([2:43](https://youtu.be/yNPKt4tkeC0?t=163))
- **Independent benchmarks mostly confirm coding strength, but one shows weak output diversity.** — The speaker cites Aider Polyglot (code editing) with V3 second behind o1 and above Claude. On AidanBench (diverse yet coherent outputs) it ranks 22nd, which the speaker attributes to output diversity, saying it is essentially too low on temperature. He notes each benchmark measures something different. ([2:43](https://youtu.be/yNPKt4tkeC0?t=163))
- **Chatbot Arena places it seventh, among the top proprietary models.** — The speaker reads this as an impressive position for an open model and cites it, together with price, as the basis for calling V3 the best price-to-performance model so far. ([4:04](https://youtu.be/yNPKt4tkeC0?t=244))
- **Terms-of-service concerns exist and open weights allow self-hosting or third-party hosting.** — The speaker says Reddit users raised concerns about deepseek.com terms, links an article without summarizing it, and suggests either self-hosting or a reputable host, while warning that hosting prices could rise. ([4:04](https://youtu.be/yNPKt4tkeC0?t=244))

## Techniques
- **Swap an OpenAI SDK app to DeepSeek V3** — Keep the existing OpenAI SDK client code. Change three things: the base URL, the API key, and the model name to the DeepSeek V3 values. The video does not show the exact base URL or model identifier, so take them from DeepSeek's API docs. *When:* When an existing OpenAI-based app should be tested cheaply against an open-weight model with minimal code change.
- **Price-to-performance check before committing to a model** — For each LLM used in an application, compare the per-million-token input and output prices and the benchmark results for the task. The speaker's example puts DeepSeek V3 against GPT-4o. The check is on price alone. *When:* When choosing or re-evaluating models for cost, especially at high token volume.
- **Cross-check vendor benchmarks against independent leaderboards by task** — Read the vendor's own benchmark results, then look up independent results per task type. The speaker maps coding edits to Aider Polyglot, output diversity to AidanBench, and general preference to Chatbot Arena, since each measures something different. *When:* Before relying on a model for a specific workload such as code editing, creative generation or open-ended chat.

## Numbers
- Quoted DeepSeek API price: about 1.4 cents per 1M input tokens and 28 cents per 1M output tokens (auto-caption; check against DeepSeek's pricing page before relying on it). ([1:22](https://youtu.be/yNPKt4tkeC0?t=82))
- GPT-4o price as quoted: $2.50 per 1M input and $10 per 1M output tokens. ([1:22](https://youtu.be/yNPKt4tkeC0?t=82))
- DeepSeek V3 training as stated: 671B parameters, about 2,000 NVIDIA H800 GPUs, two months, about 2.8M GPU hours, about $5.6M. ([1:22](https://youtu.be/yNPKt4tkeC0?t=82))
- Llama 3 405B training as stated: about 30.8M GPU hours on 16,000 H100s, which the speaker calls 11x the compute. ([1:22](https://youtu.be/yNPKt4tkeC0?t=82))
- Aider Polyglot (edit benchmark): V3 ranked second, behind o1 and above Claude. ([2:43](https://youtu.be/yNPKt4tkeC0?t=163))
- AidanBench: V3 ranked 22nd. ([2:43](https://youtu.be/yNPKt4tkeC0?t=163))
- Chatbot Arena: V3 ranked seventh, in the middle of the top proprietary models. ([4:04](https://youtu.be/yNPKt4tkeC0?t=244))

## Hot takes
- The speaker says DeepSeek V3 has the best price-to-performance of any model yet and that GPT-4o users should switch. The support is mostly vendor benchmarks plus a few leaderboard rankings, and the single coding test shown is anecdotal.
- The title says 'The BEST AI for Coding', but the coding evidence in the video is mixed: second on SWE-bench to Claude Sonnet and second on Aider Polyglot, with 22nd on AidanBench.
- The speaker's explanation for weak AidanBench results ('its temperature is too low') is an untested guess.
- The video says the model sometimes claims to be ChatGPT and may have seen GPT outputs. This is speculation, not evidence the speaker checked.
- The Reddit terms-of-service concern is raised with no detail. The speaker defers to an unsummarized linked article.

## Tools mentioned
DeepSeek V3, DeepSeek Coder, chat.deepseek.com, OpenAI SDK, GPT-4o, Claude Sonnet, o1, Claude, Llama 3 (405B), MMLU-Pro, GPQA Diamond, MATH-500, AIME, Codeforces, SWE-bench, Aider Polyglot, AidanBench, Chatbot Arena, LeetCode

## Relevance to our work
- **agentos** (1/3): AgentOS puts one proxy URL in front of any OpenAI-compatible client and uses strategy routing. The video's OpenAI-SDK swap and per-token price argument apply to that routing layer, but the video does not discuss proxies, budgets or routing. → *Add an OpenAI-compatible DeepSeek V3 endpoint as a candidate backend in AgentOS strategy routing and compare its cost per task against the current models on our own eval set.*
