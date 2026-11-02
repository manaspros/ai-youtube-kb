# AI-Driven Multi-Document Correlation for Financial Compliance - Varsha Shah, Independent

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Iwe_RY-fYgI` · [watch](https://youtu.be/Iwe_RY-fYgI) · **date:** 2026-07-18 · **length:** 19:00 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Varsha Shah · **orgs:** Tata Consultancy Services, Microsoft
- **topics:** governance-compliance, data-engineering, enterprise-adoption · **tags:** fraud-detection, financial-compliance, entity-correlation, graph, cross-document, risk-scoring, jurisdiction-normalization, feedback-loop, audit

> Varsha Shah proposes a framework that correlates records across payroll, tax, procurement and finance systems with graph-based entity linking, adaptive risk scoring and jurisdiction normalization to catch compliance fraud that per-document checks miss.

## Summary
The speaker argues that most compliance systems validate each document on its own, so fraud that only shows up across payroll, tax, procurement and transaction records goes undetected. The proposed framework has three parts: a graph-based entity correlation engine that links employees, vendors, accounts and transactions, an adaptive probabilistic risk model that combines several risk signals into a confidence score, and a cross-jurisdiction normalization layer that standardizes currency, tax rules, reporting periods and classifications. The risk model is described as learning from completed audits and investigator feedback, so false positives refine scoring over time. The talk reports an evaluation on about 3 million financial records over five years across four jurisdictions, with precision near 91%, recall near 87% and F1 0.89, plus a 76% cut in false positives and about 40% less manual audit effort. The speaker gives no dataset details, method specifics, baseline numbers or architecture, so the results cannot be checked from the talk. Deployment advice covers ERP and tax-platform integration, per-jurisdiction configuration, fitting into existing audit workflows and scale. The talk is a high-level research summary with little reusable technical detail.

## Key ideas
- **Fraud often sits between documents, not inside them** — Each payroll, invoice or tax filing can pass its own checks while the links between them reveal the problem. The speaker says the information already exists and the gap is relationship understanding. ([2:25](https://youtu.be/Iwe_RY-fYgI?t=145))
- **Per-document validation is the core limitation** — Current compliance systems check each record against its own rules (payroll rules, procurement policy, tax regulation). A transaction counts as compliant if every document passes alone. ([3:44](https://youtu.be/Iwe_RY-fYgI?t=224))
- **Three-part pipeline: correlate, score, normalize** — An entity correlation engine builds a unified view across systems, an adaptive probabilistic risk model ranks which connected patterns are real risk, and a normalization layer keeps the risk interpretation consistent across jurisdictions. ([5:04](https://youtu.be/Iwe_RY-fYgI?t=304))
- **Normalize across jurisdictions before scoring** — Currency, tax structure, reporting periods and classification schemes are standardized so the same transaction is not judged differently because of where it happened. ([6:10](https://youtu.be/Iwe_RY-fYgI?t=370))
- **Risk scoring blends several signals instead of one rule** — The model combines anomaly strength, source reliability and historical patterns into a confidence score, so investigators get prioritized cases and fewer unneeded alerts. ([7:32](https://youtu.be/Iwe_RY-fYgI?t=452))
- **Audit outcomes feed back into the model** — Confirmed fraud strengthens future detection and false positives refine scoring, so the system is meant to improve with each audit instead of relying on manual rule updates. ([13:46](https://youtu.be/Iwe_RY-fYgI?t=826))
- **Deployment depends on four things** — The speaker lists integration with existing ERP, payroll, procurement and tax systems, per-jurisdiction configuration, alignment with the audit workflow so investigators see prioritized cases, and scalability to millions of records. ([16:25](https://youtu.be/Iwe_RY-fYgI?t=985))

## Techniques
- **Cross-document entity graph for compliance** — Model employees, vendors, accounts, transactions and regulatory files as nodes in one graph built from separate payroll, tax, procurement and finance systems. Flag structural anomalies in how the entities connect. *When:* Use when each record looks valid alone and risk only shows up in how records relate across systems.
- **Multi-signal risk scoring instead of single rules** — Combine anomaly strength, source reliability and historical pattern signals into one confidence score and rank cases by it before any investigator looks at them. *When:* Use when single-rule alerts create too many false positives and investigators need prioritized queues.
- **Outcome feedback loop** — Record investigator decisions on each flagged case (confirmed fraud or false positive) and feed them back into the scoring model so future ranking improves. *When:* Use when fraud patterns and business rules change often and manual rule maintenance cannot keep up.
- **Normalize before scoring across jurisdictions** — Standardize currency, tax rules, reporting periods and classification schemes first, then run the same risk logic on all records. *When:* Use when one system covers several countries or regulatory regimes and the same event would otherwise be scored differently.

## Numbers
- Evaluation dataset of about 3 million financial records over five years across four regulatory jurisdictions ([1:10](https://youtu.be/Iwe_RY-fYgI?t=70))
- Precision about 91% ([10:37](https://youtu.be/Iwe_RY-fYgI?t=637))
- Recall about 87% ([10:37](https://youtu.be/Iwe_RY-fYgI?t=637))
- F1 score 0.89 ([10:37](https://youtu.be/Iwe_RY-fYgI?t=637))
- 76% reduction in false positives ([11:43](https://youtu.be/Iwe_RY-fYgI?t=703))
- About 40% reduction in manual audit effort ([11:43](https://youtu.be/Iwe_RY-fYgI?t=703))

## Hot takes
- Many of the most significant compliance and fraud risks exist between documents, not within them.
- Compliance should move from reactive audit findings to predictive governance that flags what is likely to go wrong next.

## Relevance to our work
- **agentos** (1/3): The audit-outcome feedback loop and the flag-versus-confirmed signal touch SkillForge's open question about what counts as a success signal, but the talk gives no mechanism. → *Read the talk's feedback-loop section (13:46) only as a framing for SkillForge's success signal; there is no method to copy.*
- **general** (1/3): Cross-source entity linking is the same problem as the entity resolution work, but the talk gives no matching method, thresholds or metrics to compare against. → *Note the claim that linking records across systems finds risk per-record checks miss, and compare it with the ER rule matcher's error profile if a cross-source case comes up; no other reading is needed.*
