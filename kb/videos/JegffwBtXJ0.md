# Gemini 3.5 Flash is just... fine

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `JegffwBtXJ0` · [watch](https://youtu.be/JegffwBtXJ0) · **date:** 2026-06-02 · **length:** 6:48 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Google, Anthropic, OpenAI, Artificial Analysis, Cursor
- **topics:** models-research, token-cost-efficiency, coding-agents · **tags:** gemini-3.5-flash, antigravity, gemini-cli, artificial-analysis, benchmarks, token-usage, agentic-coding, ui-generation, model-pricing, vendor-benchmarks

> Review of Google's Gemini 3.5 Flash and Antigravity 2: very fast and good at agentic tasks and UI, but token-hungry, costly per run and weak on coding versus frontier models.

## Summary
Better Stack reviews Google's Gemini 3.5 Flash, released alongside Antigravity 2 (a standalone agent app) and a rewritten, closed-source Antigravity CLI. The presenter argues Google's headline claims (frontier performance at 4x speed and under half the cost) hold up only partly. Google's own benchmarks put the model near GPT 5.5 on coding, but third-party Artificial Analysis numbers place its coding index below Kimi K2.6 and not above Gemini 3.1 Pro. Its main strength is output speed, about 278 tokens per second, and it is strong on multimodal input and UI generation in the presenter's one-off tests. Its weakness is token use: at $1.50/$9 per million input/output tokens it costs more per run than expected, and it averaged 49 turns per agentic task. The Gemini CLI is being shut down after June 18, which the presenter treats as a bigger practical change for developers than the model itself.

## Key ideas
- **Google's headline claims rest on its own benchmarks, which put Gemini 3.5 Flash near GPT 5.5 on coding and ahead of Opus 4.7 on Terminal-Bench, while Opus leads on SWE-Bench Pro.** — Vendor-run results; the presenter contrasts them with third-party numbers. ([0:00](https://youtu.be/JegffwBtXJ0?t=0))
- **Third-party coding results are much weaker: Artificial Analysis gives a coding index of 45, below Kimi K2.6 and not above Gemini 3.1 Pro, though it is ahead of Gemini 3 Flash.** — The model is described as up with frontier models on general performance but not clearly leading on coding. ([1:00](https://youtu.be/JegffwBtXJ0?t=60))
- **Speed is the clear advantage: about 278 tokens per second, well above Opus 4.7, GPT 5.5 and Haiku.** — The presenter's verdict is that the model is the best choice when intelligence per unit of speed matters most. ([1:00](https://youtu.be/JegffwBtXJ0?t=60))
- **The 'half the cost' claim does not hold up in practice. Input/output pricing is $1.50/$9 per million tokens, three times Gemini 3 Flash, but a full Artificial Analysis intelligence-index run cost $1,552.** — That is about 5.5x Gemini 3 Flash, 75% more than Gemini 3.1 Pro, and more than GPT 5.5 on high reasoning, which the presenter says beats Flash on coding. ([2:16](https://youtu.be/JegffwBtXJ0?t=136))
- **Per-token price hides token burn: the model averaged 49 turns per agentic task, among the highest of any model tested.** — Turn count per task is the presenter's proxy for why cost per run is high even with a low list price. ([2:16](https://youtu.be/JegffwBtXJ0?t=136))
- **In one-off UI tests the model does well: a single-file cafe site looked good, and a full-stack finance dashboard worked but looked generically AI-styled.** — Opus 4.7 produced a more polished dashboard in about 20 minutes, while Gemini took about 5 minutes. ([4:22](https://youtu.be/JegffwBtXJ0?t=262))
- **Antigravity 2 is now a standalone agent app rather than the Antigravity IDE, and its UI looks much like Codex and Cursor (conversations, projects, scheduled tasks, diff view).** — The presenter does not test it deeply, since the interface matches the other agent apps. ([3:24](https://youtu.be/JegffwBtXJ0?t=204))
- **The Gemini CLI is being shut down after June 18. Its replacement, the Antigravity CLI, is a Go rewrite that is closed source.** — The presenter did not install the new CLI and says there is nothing new to show for Gemini itself. ([5:44](https://youtu.be/JegffwBtXJ0?t=344))

## Techniques
- **Cross-check vendor benchmarks against third-party indexes** — Compare the vendor's own benchmark tables (SWE-Bench Pro, Terminal-Bench, MCP and Toolathlon agentic evals) with an independent index such as Artificial Analysis, and treat vendor-only results as provisional. *When:* Before choosing a model for coding work, or before repeating a vendor's cost or performance claim.
- **Judge cost per completed task, not list price per token** — Multiply list price by the real token volume of a run, and watch turn count per task (49 average here) as a proxy for token burn. Use the Artificial Analysis cost-to-run-index figure as a cost check. *When:* When a cheap-per-token model may still be expensive for agent loops, and when comparing models for agentic routing.
- **Run the same one-shot prompt across models for UI quality** — Give identical prompts (for example, a single index.html cafe site, and a full-stack finance dashboard) to each candidate and compare output quality and wall-clock time. *When:* For a quick qualitative check of design and frontend generation. The presenter notes this is a one-off test, not a benchmark.
- **Compare speed against intelligence** — Plot tokens per second against third-party intelligence scores to find the model that fits a latency-sensitive workload, rather than picking the highest-scoring model. *When:* For interactive or high-throughput use cases where latency matters more than top coding scores.

## Numbers
- Context window 1M tokens; max output 64K tokens; accepts text, images, video, audio and PDFs. ([0:00](https://youtu.be/JegffwBtXJ0?t=0))
- Output speed about 278 tokens per second, above Opus 4.7, GPT 5.5, Haiku and open OpenAI models (presenter's measurement). ([1:00](https://youtu.be/JegffwBtXJ0?t=60))
- Artificial Analysis coding index 45 (below Kimi K2.6; ahead of Gemini 3 Flash only by a few points). ([1:00](https://youtu.be/JegffwBtXJ0?t=60))
- Pricing $1.50 per million input tokens and $9 per million output tokens; 3x Gemini 3 Flash list price. ([2:16](https://youtu.be/JegffwBtXJ0?t=136))
- Artificial Analysis intelligence-index run cost $1,552: about 5.5x Gemini 3 Flash and 75% more than Gemini 3.1 Pro. ([2:16](https://youtu.be/JegffwBtXJ0?t=136))
- Average of 49 turns per agentic task, one of the highest of any model tested. ([2:16](https://youtu.be/JegffwBtXJ0?t=136))
- Full-stack dashboard: Gemini about 5 minutes vs Opus 4.7 about 20 minutes. ([4:22](https://youtu.be/JegffwBtXJ0?t=262))
- Google's own benchmarks: Opus 4.7 leads Gemini by about 10% on SWE-Bench Pro; Gemini leads Opus by about 10% on Terminal-Bench. ([0:00](https://youtu.be/JegffwBtXJ0?t=0))
- Gemini CLI shutdown after June 18 (2026). ([5:44](https://youtu.be/JegffwBtXJ0?t=344))

## Hot takes
- Google is unlikely to lead in coding and does not need to; its market is everyday users across Gmail, Search, Workspace and Android.
- The 'half the cost' marketing claim is wrong once measured per completed run, because the model is very token-hungry.
- The Antigravity 2 app looks the same as Codex and Cursor, so the differences between agent apps are shrinking.
- The Gemini CLI shutdown matters more to developers than the model release.
- The UI output looks 'designed by AI', with the generic card and gradient style.

## Tools mentioned
Gemini 3.5 Flash, Antigravity 2, Antigravity CLI, Gemini CLI, Gemini 3 Flash, Gemini 3.1 Pro, Gemini 3.5 Pro, Claude Opus 4.7, GPT 5.5, Kimi K2.6, Haiku, Codex, Cursor, T3 Code, Artificial Analysis, SWE-Bench Pro, Terminal-Bench, MCP benchmark, Toolathlon

## Relevance to our work
- **agentos** (1/3): Model routing by cost and speed matters for AgentOS strategy routing, and this is a concrete case where list price misstates per-run cost because of turn count. → *Add per-run cost and turns-per-task to AgentOS routing metrics, not only per-token price, before choosing a cheap model for a given route.*
