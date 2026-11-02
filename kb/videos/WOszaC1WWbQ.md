# Can AI Understand a Distressed Credit? - Harneet Kaur, Axim Intelligence

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `WOszaC1WWbQ` · [watch](https://youtu.be/WOszaC1WWbQ) · **date:** 2026-10-24 · **length:** 14:15 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Harneet Kaur · **orgs:** Axim Intelligence, iHeart Media, Rogo, Harvey
- **topics:** evals, data-engineering, models-research · **tags:** distressed-credit, finance-domain, layered-evals, model-disagreement, structured-reasoning, probabilistic-forecasting, no-ground-truth

> Founder of Axim Intelligence on testing whether LLMs can forecast distressed credit outcomes; models disagreed until a structured, layer-by-layer reasoning process made them converge, though no ground truth was shown.

## Summary
Harneet Kaur, founder and CEO of Axim Intelligence, explains distressed credit (bankruptcy, liability management exercises, out-of-court restructurings) and why older machine-learning scoring, such as the Altman Z-score, no longer fits a fast-changing, opaque private-credit market. She contrasts benchmarks that test isolated finance facts with a framing where the real skill is producing a probability distribution over what happens next. On one live case, iHeart Media, two frontier models (called "Astra 6" and "Opus 5.5" in the transcript) gave very different bankruptcy probabilities from the same structured data. Her team then benchmarked each reasoning layer (extraction, reconciliation/derivation, judgment, prediction), so disagreements could be traced to specific assumptions. After a structured reasoning process was imposed, the two models converged on similar probabilities (one reported as 62% bankruptcy for Opus and 25% for the other, then both near 25%) and agreed negotiated restructuring was the likeliest path. She is clear that convergence does not prove correctness, since no ground truth exists and historical backtests would carry look-ahead bias. The talk ends with a pitch for her company.

## Key ideas
- **Distressed credit is not binary. Outcomes include bankruptcy, liability management exercises and out-of-court negotiated restructurings, so prediction has to be a probability distribution over paths.** — Stress can come from cyclical, operational or secular (e.g. AI disruption to software) causes. Old default-or-not framing no longer fits. ([1:35](https://youtu.be/WOszaC1WWbQ?t=95))
- **Traditional ML scoring such as the Altman Z-score is static, and the market is opaque, so systematizing analysis is hard. Current analysis is manual: financials, lender-side dynamics and credit documents.** — Private credit has reduced price transparency, and the situation can change monthly, quarterly or yearly. ([2:55](https://youtu.be/WOszaC1WWbQ?t=175))
- **Finance benchmarks that test isolated facts (e.g. which debt is structurally senior) miss the real task, which is predicting what happens next.** — She contrasts her view with broad benchmarking efforts by other AI-for-finance companies. ([4:19](https://youtu.be/WOszaC1WWbQ?t=259))
- **On a live case (iHeart Media, bankrupt in 2018 and with a 2024 stress transaction), two frontier models gave conflicting probability views from the same structured context. No ground truth exists to decide who was right.** — Her reading was that one model's negotiated-restructuring call was the best option while the other favored bankruptcy. ([5:47](https://youtu.be/WOszaC1WWbQ?t=347))
- **Her method is layered benchmarking: test extraction, then reconciliation/derivation (e.g. EBITDA plus debt gives leverage), then judgment (is this distressed?), then prediction. Errors in lower layers corrupt higher-layer judgments.** — Extraction is largely solved for public companies but still hard for private loans in Excel and PDF documents. ([8:13](https://youtu.be/WOszaC1WWbQ?t=493))
- **Imposing a structured reasoning process made the two models converge on similar probabilities and the same likeliest path. Her claim is that the convergence is more interesting than whether it is correct.** — She argues convergence is like a market price: a process that yields consistent probabilities. Correctness can only be judged by live outcomes, since historical tests leak look-ahead bias. ([10:26](https://youtu.be/WOszaC1WWbQ?t=626))
- **Takeaway: with non-verifiable questions and the same organized context, the models showed no clear predictive edge over human analysts, but a structured process made them agree.** — Agreement is not accuracy. Evaluating the reasoning process per layer is the tractable part. ([11:55](https://youtu.be/WOszaC1WWbQ?t=715))

## Techniques
- **Layer-by-layer benchmarking of an LLM analysis pipeline** — Split the task into extraction, reconciliation/derivation, judgment and prediction. Evaluate each layer separately with its own ground truth where possible, and only trust the prediction layer once the layers beneath it pass. *When:* Any multi-step analytical agent where errors compound, especially when the final output is unverifiable and you need to see where the reasoning diverges.
- **Cross-model disagreement as a diagnostic** — Run the same structured context through two or more strong models. Where their probabilities or recommendations diverge, inspect the assumptions behind each run to find which input or step causes the split. *When:* When no ground truth exists and you want to find weak assumptions rather than pick a winner.
- **Structured reasoning scaffold to force convergence** — Give every model the same explicit, organized reasoning process (inputs, derived metrics, judgment, then probabilities) instead of free-form prompting. Measure whether the spread of probability estimates narrows. *When:* When you want consistent, auditable outputs across models, not just a single answer. Convergence is a property of the process, not evidence of accuracy.

## Numbers
- iHeart Media filed for bankruptcy in 2018 and did another stress transaction in 2024, used as the live test case. ([5:47](https://youtu.be/WOszaC1WWbQ?t=347))
- Before the structured process, the two models disagreed sharply on bankruptcy probability: about 62% for one model and about 25% for the other. ([10:26](https://youtu.be/WOszaC1WWbQ?t=626))
- After the structured process, both models put bankruptcy near 25% and both chose negotiated restructuring as the most likely path. ([10:26](https://youtu.be/WOszaC1WWbQ?t=626))

## Hot takes
- Convergence between models is treated as a market-price-like signal, but agreement is not shown to be accurate, and the speaker admits there is no ground truth and no backtest. A single company case (iHeart) is a thin basis for the general claim.
- The talk ends with a QR-code pitch for her company, so the content is partly product marketing. Substance is real but limited to one case study with no published method, data or eval numbers.
- Her claim that the models show no predictive edge over human analysts is a bold conclusion drawn from non-verifiable questions. The talk shows no evidence either way.

## Tools mentioned
Opus (Opus 5.5, as named in transcript), Astra 6 (named in transcript; the model name may be an auto-caption error)

## Relevance to our work
- **agentos** (1/3): Layer-by-layer evaluation of a multi-step LLM pipeline and cross-model disagreement as a signal are relevant to AgentOS evals, but the talk gives no reusable code or metrics. → *Read the layered-evaluation idea and consider per-stage evals (extraction, derivation, judgment, prediction) for agent pipelines in AgentOS, with cross-model disagreement as a debugging signal.*
- **prosharness** (1/3): The structured-process-to-converge idea loosely matches ProsHarness's plan, critique and debate loop with Codex, but the talk does not describe a mechanism for it. → *Consider logging how often the planner and critic models agree on a plan before and after giving them a shared structured template, as a debate-quality metric.*
