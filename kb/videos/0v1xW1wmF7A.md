# Grok 4 is the SMARTEST model in the WORLD ($300/month!?)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `0v1xW1wmF7A` · [watch](https://youtu.be/0v1xW1wmF7A) · **date:** 2025-11-02 · **length:** 5:24 · **format:** news · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Anthropic, OpenAI, Google, Cursor, Artificial Analysis, Tesla
- **topics:** models-research, multi-agent, token-cost-efficiency · **tags:** grok-4, grok-4-heavy, benchmarks, arc-agi-2, humanitys-last-exam, aime, livecodebench, pricing, long-context-pricing, multi-agent-best-of-n, voice-mode, news-roundup

> Quick news recap of Grok 4 and Grok 4 Heavy: reasoning-only models, $300/month Heavy tier, and vendor-reported benchmark wins, with the speaker judging them the smartest commercially available model right now.

## Summary
The video recaps the Grok 4 and Grok 4 Heavy launch from a roughly 50-minute livestream. Both models are reasoning-only with a 256k context window. Heavy is described as a multi-agent version that spins up many agents, compares their answers, and picks the best one, and it requires a $300/month plan. The standard model is available on a $30/month subscription and via API at $3 per million input and $15 per million output tokens, with the price reportedly doubling for requests above 128k tokens. The speaker walks through the benchmarks Grok leads: ARC-AGI-2 (16.2 vs Opus 4's 8.6), AIME25, Humanity's Last Exam with tools (44.4% Heavy, 38.6% Grok 4), and LiveCodeBench (82%). Most figures are vendor-reported, with partial independent checks cited (AIME24 by 0.3 points, Artificial Analysis at 23.9% on HLE without tools). Weaknesses the speaker notes are multimodal input, with image and video generation promised later, plus a dedicated coding model said to be coming. The speaker also reports a new voice mode with lower latency and finds Musk's claim that pasting source into Grok beats Cursor hard to believe.

## Key ideas
- **Grok 4 and Grok 4 Heavy launched as reasoning-only models, with no non-reasoning mode.** — Grok 4 has a 256k-token context window and the usual model features. Details on Heavy were thin; the speaker assumes it has the same features. ([0:00](https://youtu.be/0v1xW1wmF7A?t=0))
- **Heavy is positioned as a multi-agent mode gated behind a $300/month plan.** — Heavy spins up many agents on a task and compares their results to pick the best answer, with claimed higher performance. No mechanism detail was given. The speaker notes OpenAI started the super-tier trend. ([0:00](https://youtu.be/0v1xW1wmF7A?t=0))
- **API pricing doubles for long requests.** — Standard Grok 4 is $3 per million input tokens and $15 per million output tokens, priced like Grok 3 and a Claude model (caption 'ClaudeForce'). The price reportedly doubles for requests above 128,000 tokens. The $30/month subscription covers the standard model. ([1:13](https://youtu.be/0v1xW1wmF7A?t=73))
- **ARC-AGI-2 is the headline reasoning benchmark.** — Grok 4 Heavy scored 16.2 against 8.6 for Opus 4, nearly double. The speaker describes ARC-AGI-2 as tasks easy for humans but hard for AI that test generalization and flexibility. ([1:13](https://youtu.be/0v1xW1wmF7A?t=73))
- **Math results are near saturation, with an independent check on AIME24.** — Vendor numbers were 100% for Heavy and 98.8% for Grok 4 on AIME25, just ahead of OpenAI o3. Independent AIME24 results put Grok 4 on top, by only 0.3 points. ([1:13](https://youtu.be/0v1xW1wmF7A?t=73))
- **Humanity's Last Exam is the benchmark the launch leaned on most, and the tool setting matters.** — With tools, Heavy scored 44.4% and Grok 4 38.6%, about 20% above Gemini 2.5 Pro. Artificial Analysis measured 23.9%, which the speaker believes was without tools. ([2:27](https://youtu.be/0v1xW1wmF7A?t=147))
- **Coding was not the focus, but Grok 4 led LiveCodeBench.** — Grok 4 scored 82% on LiveCodeBench and was close on a competitive-programming benchmark (caption 'Psycode') and HumanEval, behind o4 mini and sometimes o3. A dedicated coding model is promised. ([2:27](https://youtu.be/0v1xW1wmF7A?t=147))
- **The launch admitted multimodal capability is a weakness.** — Improved multimodal input was promised soon, and video generation after that. Musk also talked about physics and fluid simulator tools. The speaker found the Cursor comparison claim implausible from a UX standpoint. ([3:34](https://youtu.be/0v1xW1wmF7A?t=214))
- **A new voice mode with lower latency was demoed live.** — The speaker said it beat OpenAI's voice in the live demo, but found the voices uncomfortable. ([3:34](https://youtu.be/0v1xW1wmF7A?t=214))

## Techniques
- **Parallel multi-agent attempts with best-answer selection (Grok 4 Heavy)** — Spin up several agents on the same task, collect their answers, compare them, and return the best one. The video gives no implementation detail, so this is only the vendor's description, not a verified method. *When:* Hard reasoning tasks where extra inference cost is acceptable. Treat as an idea to test, not an established result.

## Numbers
- Grok 4 context window: 256,000 tokens. ([0:00](https://youtu.be/0v1xW1wmF7A?t=0))
- Grok 4 Heavy access requires a $300/month plan. ([0:00](https://youtu.be/0v1xW1wmF7A?t=0))
- Standard Grok 4 subscription: $30/month. API: $3 per million input tokens, $15 per million output tokens, doubling above 128,000-token requests. ([1:13](https://youtu.be/0v1xW1wmF7A?t=73))
- ARC-AGI-2: Grok 4 Heavy 16.2 vs Opus 4 8.6. ([1:13](https://youtu.be/0v1xW1wmF7A?t=73))
- AIME25: Grok 4 Heavy 100%, Grok 4 98.8% (vendor). Independent AIME24: Grok 4 leads by 0.3 points. ([1:13](https://youtu.be/0v1xW1wmF7A?t=73))
- Humanity's Last Exam with tools: Grok 4 Heavy 44.4%, Grok 4 38.6%, about 20% above Gemini 2.5 Pro. Artificial Analysis: 23.9%. ([2:27](https://youtu.be/0v1xW1wmF7A?t=147))
- LiveCodeBench: Grok 4 82%. ([2:27](https://youtu.be/0v1xW1wmF7A?t=147))

## Hot takes
- The title's 'smartest model in the world' claim rests mostly on vendor-reported benchmarks. The speaker softens it to 'appears to be the smartest commercially available model'.
- The $300/month Heavy tier is framed as the new super-tier price point, following OpenAI.
- The Musk claim that pasting source files into Grok beats Cursor is called implausible from a UX standpoint.
- Benchmark leadership is treated as a sign of healthy competition among Google, Meta, Anthropic and OpenAI.
- Independent confirmation is partial: AIME24 by 0.3 points, and HLE without tools at 23.9%.

## Tools mentioned
Grok 4, Grok 4 Heavy, Grok 3, Claude Opus 4, Claude (caption 'ClaudeForce', likely Sonnet), OpenAI o3, o4 mini, Gemini 2.5 Pro, Cursor, VS Code, Artificial Analysis, ARC-AGI-2, AIME, Humanity's Last Exam, GPQA, HMMT, USAMO, LiveCodeBench, HumanEval, Tesla Optimus

## Relevance to our work
- **agentos** (1/3): Tiered per-token pricing (price doubles above 128k input tokens) is relevant to budget accounting in the Scout proxy, but the video gives only one pricing example. → *When modeling budgets in Govrix Scout, check whether the cost table can express a long-context price step (2x above a token threshold) rather than assuming one flat per-token rate.*
- **prosharness** (1/3): Heavy's spin-up-many-agents-and-compare-answers pattern is loosely similar to ProsHarness's plan, critique and debate loop, but the video gives no mechanism detail. → *Treat parallel attempts plus pick-best as a hypothesis to test against ProsHarness's critique step, not as a proven design. Confirm details from primary sources before adopting it.*
