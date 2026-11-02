# What Do Models Still Suck At? - Peter Gostev, Arena.ai, BullshitBench

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `R7A8rX-09Zw` · [watch](https://youtu.be/R7A8rX-09Zw) · **date:** 2026-05-18 · **length:** 20:24 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Peter Gostev · **orgs:** Arena (arena.ai)
- **topics:** evals, models-research · **tags:** benchmark-design, false-premise, sycophancy, llm-as-judge, reasoning-effort, dissatisfaction-rate, arena, domain-slicing

> Peter Gostev (Arena) argues leaderboard line-go-up hides real gaps; uses a nonsense-question "BullshitBench" and Arena's dissatisfaction-rate data to show progress is uneven by domain and that more reasoning can hurt.

## Summary
The speaker argues that headline benchmark charts overstate how close models are to general competence, and that teams should look at where models still fail. He built BullshitBench, about 155 nonsense questions with false premises, graded by an LLM judge that he says he checked by reading outputs himself. Latest Claude Sonnet models push back most often, GPT and Gemini models are roughly a coin flip on accepting nonsense, and even "good" answers often still try to accommodate the premise. Across the Arena data he finds that higher reasoning effort often does not help and can make false-premise handling worse. Using Arena's pairwise votes with a "both bad" option, he tracks a dissatisfaction rate over time among the top 25 models, which fell from about 17% pre-reasoning to about 9% now but never reached zero. Slicing expert-level prompts by domain shows large gains in quantitative work and little movement in finance, law and medicine, with games singled out as still weak. He ends by asking for effort on the bottom of the distribution, not only the frontier.

## Key ideas
- **Headline benchmark trends hide real gaps and can cause hype cycles** — Speaker says line-go-up charts make people expect near-AGI behavior and that this may be self-deception; he wants to look at what models still fail at. ([0:00](https://youtu.be/R7A8rX-09Zw?t=0))
- **Models readily go along with nonsense questions** — On BullshitBench, the test is whether the model pushes back on a false premise or answers anyway. Latest Claude Sonnet models do best; GPT and Gemini are about 50-50; even pushback answers often still try to accommodate. ([2:27](https://youtu.be/R7A8rX-09Zw?t=147))
- **Anthropic models pulled ahead on this probe since Sonnet 4.5** — Plotting top models by lab over time, Anthropic models were middling early and rose after Claude Sonnet 4.5, with Haiku also high. OpenAI and Google stayed well below the top. ([5:03](https://youtu.be/R7A8rX-09Zw?t=303))
- **More reasoning can make false-premise handling worse** — Comparing low vs high reasoning on the same model, low sometimes beats high. Reading GPT-5.4 traces, the model often notes the premise is wrong once, then spends many paragraphs solving anyway. He guesses training rewarded solving at any cost. ([6:25](https://youtu.be/R7A8rX-09Zw?t=385))
- **Pairwise votes with a 'both bad' option give a usable dissatisfaction metric** — Arena users vote A vs B or flag both as bad. Restricting to battles among the top 25 models avoids weak models dragging the average. The rate falls over time but stays above zero (about 9% now). ([9:15](https://youtu.be/R7A8rX-09Zw?t=555))
- **Progress varies a lot by domain and prompt type** — On expert-tagged prompts (about 40k, top-25 battles), quantitative topics like math and physics dropped sharply from late 2024/early 2025. Finance, law and medicine stayed flat. Speaker also notes user expectations shift, so the metric is not static. ([13:11](https://youtu.be/R7A8rX-09Zw?t=791))
- **Overall software dissatisfaction roughly halved, but gaming is not improving** — Software dissatisfaction went from 23.5% in Q2 2024 to 13% in Q1 2026. Speaker says LLM-built games still have poor mechanics and that no good gaming benchmark exists to capture this. ([16:54](https://youtu.be/R7A8rX-09Zw?t=1014))
- **Narrow benchmarks miss the judgment that real work needs** — He argues real white-collar work involves fuzzy judgment that well-specified benchmarks don't measure, and that effort should go to raising the bottom of the distribution, not only the frontier. ([18:19](https://youtu.be/R7A8rX-09Zw?t=1099))

## Techniques
- **False-premise / nonsense probe with LLM-as-judge** — Write a set of plausible-sounding but nonsensical questions (about 155 in BullshitBench), collect responses, and grade each as pushback vs accepting the premise with an LLM judge. Spot-check judgments by reading outputs. Open-source data is published. *When:* When you want to test whether a model or routed model will challenge bad inputs instead of confidently answering them.
- **Dissatisfaction rate from pairwise votes** — Use pairwise comparisons with an explicit 'both bad' option. Count the share of battles where both responses are rejected. Restrict to the top models so weak models do not dominate. *When:* When you need a trend metric on open-ended prompts that a single fixed benchmark cannot capture.
- **Domain and expertise slicing of real prompts** — Classify a large prompt log into categories and subcategories, keep only high-signal expert prompts, then plot the metric per category over time. Compare slopes to see uneven progress. *When:* When an aggregate score hides that some domains improved a lot and others did not.
- **Compare reasoning effort on the same model** — Run the same model at low and high reasoning on the same prompts, and check cases where low beats high. Read the traces, not only the scores. *When:* Before assuming more reasoning will fix a failure; especially for tasks where the premise may be wrong.

## Numbers
- Arena has tracked about 700 text models since Q2 2023 (GPT-4 era onward) ([1:10](https://youtu.be/R7A8rX-09Zw?t=70))
- BullshitBench has about 155 nonsense questions graded by LLM-as-judge ([2:27](https://youtu.be/R7A8rX-09Zw?t=147))
- Text arena has nearly 5.5 million votes ([9:15](https://youtu.be/R7A8rX-09Zw?t=555))
- Top-25 model dissatisfaction rate about 17% pre-reasoning, about 12% after o1, about 9% now ([11:53](https://youtu.be/R7A8rX-09Zw?t=713))
- Math dissatisfaction about 25-27% before a large improvement; creative writing improved only modestly ([13:11](https://youtu.be/R7A8rX-09Zw?t=791))
- Expert subset about 40,000 prompts, top-25 battles only, from about 6 million total prompts ([13:11](https://youtu.be/R7A8rX-09Zw?t=791))
- Software-category dissatisfaction fell from 23.5% (Q2 2024) to 13% (Q1 2026) ([16:54](https://youtu.be/R7A8rX-09Zw?t=1014))

## Hot takes
- Higher reasoning effort often does not help and can make false-premise handling worse.
- LLMs do not really understand how to build games; the mechanics they produce are poor.
- Leaderboard line-go-up charts give a misleading picture of how close models are to general competence.

## Tools mentioned
BullshitBench, Arena text leaderboard

## Relevance to our work
- **agentos** (1/3): Speaker's false-premise probe and dissatisfaction metric are relevant to evaluating model routing in the proxy, but the talk does not cover budgets, retrieval, or serving. → *Add a small nonsense or false-premise prompt set to the AgentOS eval suite and compare routed models on pushback rate, not only answer accuracy.*
- **prosharness** (1/3): Plan critique with a second model is exposed to the same failure: accepting a flawed premise and solving anyway. Talk's low-vs-high reasoning finding applies to the critique step. → *When testing the plan-critique (Codex) step, include a few plans with a wrong premise and compare low vs high reasoning effort on whether the critic pushes back.*
- **general** (1/3): Relevant to cheap-model (Haiku) pipelines and LLM-as-judge grading, with a reusable probe design. No concrete benchmark numbers for those uses. → *Reuse the 'both bad' vote idea or a pushback-rate check when grading Haiku classification outputs on malformed inputs.*
