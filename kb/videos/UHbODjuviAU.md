# The Investor's Edge Lives in Their Head — Anekha Sokhal, Moshi

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `UHbODjuviAU` · [watch](https://youtu.be/UHbODjuviAU) · **date:** 2026-10-20 · **length:** 16:29 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Anekha Sokhal · **orgs:** Moshi
- **topics:** product-ux, governance-compliance, data-engineering · **tags:** vendor-pitch, finance, human-in-the-loop, traceability, hallucination-measurement, accountability, push-vs-pull-data, multi-agent

> Vendor talk from Moshi's founder arguing that an investor's edge is human judgment: machines should do the data grind, while every AI claim stays traceable and the human makes the call.

## Summary
Anekha Sokhal, founder and CEO of Moshi, argues that data volume has outpaced attention, so the scarce asset for financial investors is judgment, not raw information. She says a trader's edge is tacit knowledge built over years and lost when people leave, and that a flood of context does not help unless it is trustworthy. Her proposed split is machines for the grind (gathering, cleaning, cross-checking, watching markets) and humans for the decision. She explains that finance cannot hand the decision loop to agents because someone must be accountable for each decision, and that a tool needs to be something others can trust and trace. Moshi, her product, runs six deterministic agents, measures hallucination per claim, traces each claim to its source, and exposes the assumptions behind a conclusion. The talk is a product pitch with little concrete technical detail, so its value is mainly as a framing of accountability and traceability for high-stakes AI tools.

## Key ideas
- **More data does not mean more information; the gap between data volume and an investor's attention keeps widening.** — The speaker cites about 175 zettabytes of data created in 2025 and argues that synthesis, not access, is what financial professionals are paid for. ([1:09](https://youtu.be/UHbODjuviAU?t=69))
- **An investor's edge is tacit knowledge that cannot be downloaded.** — She defines edge as knowing what is happening before others, seeing second- and third-order blind spots, and having the conviction to size a trade. She argues this lives in people's heads, built by years of sitting beside experienced traders, and leaves the firm when they move or retire. ([3:50](https://youtu.be/UHbODjuviAU?t=230))
- **Shipping an AI tool costs far more than building it, and per-call pricing changes the economics.** — A weekend dashboard becomes a real product only once it needs security, a database, storage, reliability and per-call compute, which she says is the gap people overlook. ([6:33](https://youtu.be/UHbODjuviAU?t=393))
- **Pull tools make the user the context; push tools are a data engineering problem.** — With pull tools, the user must explain the situation to a model frozen in time. Push tools flood the user with streaming information, so the hard part becomes ingestion and filtering. ([6:33](https://youtu.be/UHbODjuviAU?t=393))
- **Accountability is why finance cannot hand decisions to agents.** — Trades have counterparties, and when something goes wrong a human must explain the decision. She contrasts this with an agent that leaks an API key, apologizes and self-corrects, which she says is not acceptable where errors compound. ([7:53](https://youtu.be/UHbODjuviAU?t=473))
- **Split the work: machines do the grind, humans do the judgment.** — Reading, gathering, cross-checking, data cleaning and market watching are the grind, which she says machines do well. Forming the decision is judgment, which she says humans do best. ([9:22](https://youtu.be/UHbODjuviAU?t=562))
- **Make trust measurable: trace every claim, measure hallucination per claim, and show the assumptions.** — She says new context is worthless if its source and reliability are unknown. Moshi measures hallucination on every claim, links each claim to its source, and shows the assumptions behind a conclusion so the user can see how the reasoning was reached. ([10:43](https://youtu.be/UHbODjuviAU?t=643))

## Techniques
- **Split grind from judgment** — Route gathering, cleaning, cross-checking and monitoring to automated components, and keep the final decision step with a human who sees the evidence. The talk gives no implementation detail beyond this split. *When:* Decision workflows that take heavy information work before a judgment call, especially where a person has to own the outcome.
- **Per-claim traceability and measured hallucination** — Attach a source trace to each claim in an answer, measure hallucination per claim rather than per response, and show the assumptions that led to the conclusion alongside it. *When:* High-stakes answers where users must verify reasoning before acting, or where a confident but wrong answer has a real cost.
- **Deterministic multi-agent decomposition** — Moshi runs six agents that the speaker says are built in a deterministic manner, each covering part of the market and document work. Roles, inputs and outputs are not described in the talk. *When:* When reproducibility and auditability matter more than open-ended agent autonomy.

## Numbers
- About 175 zettabytes of data created in 2025, far above two decades earlier (speaker's figure). ([0:08](https://youtu.be/UHbODjuviAU?t=8))
- Human brain runs on about 20 watts with about 86 billion neurons (speaker's comparison to AI systems that need a power plant). ([2:34](https://youtu.be/UHbODjuviAU?t=154))
- Moshi runs a team of six deterministic agents and has read 2.4 billion data points. ([10:43](https://youtu.be/UHbODjuviAU?t=643))
- Moshi learns about 300 new things in the four seconds it takes to read one sentence (speaker's claim). ([10:43](https://youtu.be/UHbODjuviAU?t=643))
- Claimed efficiency gain of up to 35% for traders using the tool (vendor claim, no methodology given). ([12:01](https://youtu.be/UHbODjuviAU?t=721))

## Hot takes
- Edge in investing is what you cannot download; it lives in an investor's head and walks out when they leave.
- Agents should not own decisions in finance, because an agent that errs just apologizes and self-corrects, and that is not an acceptable accountability model.
- Pulling context from an LLM means working from an old model; the real AI problem is push-style data ingestion.
- Quality capped at 2: this is a product pitch for Moshi with a few reusable framing ideas and no reproducible technical detail, and the 35% efficiency and 2.4B data point figures come without methodology.

## Tools mentioned
Moshi (the speaker's own product, described as a 24-7 quant analyst for institutional traders)

## Relevance to our work
- **agentos** (1/3): Speaker stresses per-claim provenance and hallucination measurement. AgentOS MemoryMesh already plans provenance and RAGAS evals, so the framing supports those features without new mechanisms. → *Check that MemoryMesh answers can expose per-claim source provenance and a per-claim faithfulness score, and surface the retrieval assumptions alongside the answer.*
- **prosharness** (1/3): Argues that agent decisions need a human who can explain the reasoning, which matches ProsHarness phone-driven approvals. The talk suggests approvals should show the assumptions behind an action, not just the action itself. → *When designing ProsHarness approval prompts, include the assumptions and source evidence behind each proposed step so the approver can judge the reasoning.*
