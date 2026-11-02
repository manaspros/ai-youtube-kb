# Insurance Claims Are AI's Messiest Data Problem — Denys Linkov, Wisedocs

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `W4pnzOURwHQ` · [watch](https://youtu.be/W4pnzOURwHQ) · **date:** 2026-10-18 · **length:** 44:31 · **format:** workshop · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Denys Linkov · **orgs:** Wisedocs, Artificial Analysis
- **topics:** data-engineering, evals, enterprise-adoption, governance-compliance · **tags:** insurance-claims, medical-claims, document-extraction, data-quality, deduplication, llm-as-judge, human-in-the-loop, benchmark-design

> Insurance claims data is messy, so AI claims work needs layered extraction, duplicate detection, human verification, and calibrated tiered benchmarks before cross-claim analytics pay off.

## Summary
Denys Linkov, who leads the AI program at Wisedocs, argues that medical and property-casualty claims are among the hardest enterprise data problems, and that most insurers have not finished basic digital transformation. He walks through the messiness: non-standard forms across US states, duplicate and co-mingled patient records (up to 50%+ duplicates depending on jurisdiction), scanned faxes, and single claim files so large (one he saw was 8 GB) that they cannot fit in a context window. His proposed approach is a layered pipeline: OCR and preprocessing, extraction models and VLMs, classifiers, summaries, then human verification, with analytics built on top only once per-claim data is trustworthy. He presents MLCR, a six-tier medical-claims QA benchmark built with Artificial Analysis, scored on accuracy, completeness, and conciseness against expert answers, with a private held-out tier and calibrated triple-judge verification. Frontier accuracy on the hardest tier reportedly rose from about 20% at launch to about 75% a few months later. Once extraction is solid, he says cross-claim analysis (provider networks, diagnosis co-occurrence, cost trends) becomes possible, though he admits most of the industry has not reached that point. The talk is part pitch for Wisedocs and part sincere field report on regulated, human-in-the-loop AI.

## Key ideas
- **Digital transformation is unfinished in most companies, so AI on top of messy data is premature** — Speaker notes that many firms have not finished cloud migration, data lakes, or digitization (faxes still a >$7B market, EHR adoption only reached the 80-90s around COVID). He argues the data prerequisites must come first. ([2:22](https://youtu.be/W4pnzOURwHQ?t=142))
- **Duplicate and co-mingled records are the core data-quality failure** — Duplicates can reach 50%+ depending on jurisdiction, partly because claimants must repeatedly chase status. Records from different patients get mixed (a HIPAA risk), and a single upstream error can break a whole claim. Detection at intake is needed to stop bad data from propagating. ([16:14](https://youtu.be/W4pnzOURwHQ?t=974))
- **Claim files exceed what a single LLM call can handle** — Claims mix images, X-rays, ultrasounds, and scans; one file he saw was 8 GB. Long-context prompting over a whole file is not a practical approach, so the work must be decomposed. ([20:07](https://youtu.be/W4pnzOURwHQ?t=1207))
- **Layered abstraction pipeline with verification at each level** — Pipeline order: OCR and preprocessing, then NLP and extraction models or VLMs, classifiers, per-document summaries, human verification, and finally analysis layers. Information density rises going up, and AI is most useful at the top once lower layers are verified. ([34:02](https://youtu.be/W4pnzOURwHQ?t=2042))
- **MLCR benchmark: tiered difficulty, private held-out tier, three-axis scoring** — Six tiers of claim questions, from injury date to multi-step clinical reasoning. Easy tiers are open-sourced, harder tiers are held privately with Artificial Analysis to limit benchmaxxing. Answers are scored on accuracy, completeness, and conciseness against expert-validated answers. ([24:03](https://youtu.be/W4pnzOURwHQ?t=1443))
- **Frontier accuracy on the hardest tier moved very fast, so evals go stale quickly** — At launch the best high-reasoning accuracy was about 20%. A few months later it was around 75%. He reads this as a reason to keep re-running evals, since it means more of the hard questions can become productized with a human still reviewing. ([25:42](https://youtu.be/W4pnzOURwHQ?t=1542))
- **Calibrate the judges against experts before trusting them** — Accuracy is judged against human-verified answers using a calibrated set of judges (triple-judge verification). He stresses that upstream extraction errors compound downstream, so each step must be calibrated, and this needs domain experts working alongside engineers. ([27:21](https://youtu.be/W4pnzOURwHQ?t=1641))
- **Cross-claim analytics only become possible after per-claim extraction is solid** — Once data is structured, he describes analyses of out-of-area treatment, lawyer/doctor/chiropractor co-working networks, diagnosis co-occurrence (ICD codes), and year-over-year cost changes by provider, used for counterfactual network and billing decisions. ([28:31](https://youtu.be/W4pnzOURwHQ?t=1711))
- **Match the model type to the task, and pick for cost as well as accuracy** — He separates classification, extraction, and decision tasks, says LLMs are not the right tool for everything, and says cost pushed Wisedocs to train its own models for some steps. He criticizes the default of using reasoning tokens on every problem. ([41:41](https://youtu.be/W4pnzOURwHQ?t=2501))

## Techniques
- **Layered extraction with per-level verification** — Chain OCR/preprocessing -> extraction (NLP models or VLMs) -> classifiers -> document summaries -> human check -> analytics. Each layer is verified before the next consumes it, and density of information increases up the stack. *When:* Input documents are too large or heterogeneous for one prompt, and downstream decisions depend on upstream fields being right.
- **Tiered benchmark with a private held-out tier** — Write difficulty tiers of domain questions. Open-source the easy tiers and keep harder tiers private, hosted by a third party. Score each answer on accuracy, completeness, and conciseness against expert-validated answers. *When:* Building document-QA evals where models may hallucinate facts that are absent from the source and where benchmark gaming is a risk.
- **Calibrated multi-judge verification** — Use several LLM judges (triple-judge), but first calibrate them against a set of expert-verified answers so you know their agreement with humans before relying on them. *When:* LLM-as-judge is used to score extraction or QA outputs at scale in a domain where experts disagree or accuracy matters.
- **Back-test on historical samples before pilot** — Run the pipeline on a few sample files from the customer, then review field-by-field alignment with business definitions (e.g., date of injury vs. date of report). Agree definitions before a broader pilot. *When:* Onboarding a new customer or data source where the same field name means different things to different stakeholders.
- **Duplicate and co-mingling detection at intake** — Detect repeat submissions and records from other patients before they enter the claim, so bad data is caught at the source rather than cleaned later. *When:* Ingesting data from many upstream providers that resubmit or follow up repeatedly.
- **Human-in-the-loop surfacing with page references** — The system flags conflicts (e.g., two doctors disagreeing on a diagnosis) with pointers to the page, and a human makes the decision. Keep the pipeline auditable rather than a black box. *When:* Regulated decisions where the system should inform, not decide.

## Numbers
- Global fax market is over $7B ([3:26](https://youtu.be/W4pnzOURwHQ?t=206))
- EHR adoption was about 8% in 2008; hit the 80-90s only around COVID ([4:00](https://youtu.be/W4pnzOURwHQ?t=240))
- 50 US states means roughly 50 different workers' comp intake forms ([4:33](https://youtu.be/W4pnzOURwHQ?t=273))
- Loss ratios hover around 50% for insurers ([5:40](https://youtu.be/W4pnzOURwHQ?t=340))
- Property & casualty is about a $1T premium market ([9:01](https://youtu.be/W4pnzOURwHQ?t=541))
- Plaintiff-side attorney fees: about 9-15% in California workers comp; about one-third to 40% in other jurisdictions ([14:35](https://youtu.be/W4pnzOURwHQ?t=875))
- Duplicate records can be 50% or higher depending on jurisdiction ([16:14](https://youtu.be/W4pnzOURwHQ?t=974))
- A single claim PDF in their database was 8 GB ([20:07](https://youtu.be/W4pnzOURwHQ?t=1207))
- A claims adjuster may handle around 200 claims at a time ([21:49](https://youtu.be/W4pnzOURwHQ?t=1309))
- MLCR has six tiers of questions; accuracy at launch on the hardest tier was about 20%, rising to about 75% a few months later at high reasoning ([25:42](https://youtu.be/W4pnzOURwHQ?t=1542))
- Example insurer: about $1B premiums and roughly 20,000 claims paid per year ([28:31](https://youtu.be/W4pnzOURwHQ?t=1711))
- Large insurers can spend hundreds of millions on legal fees ([40:36](https://youtu.be/W4pnzOURwHQ?t=2436))
- Speaker estimates a human in the loop removes about 70% of regulatory concerns ([38:57](https://youtu.be/W4pnzOURwHQ?t=2337))
- Turnaround requirements: Texas can be a few hours; other states 7 or 21 days ([43:20](https://youtu.be/W4pnzOURwHQ?t=2600))

## Hot takes
- Many companies should finish cloud, data lake, and digitization work before any AI deployment; AI on messy data is premature.
- Ask 'is AI the right solution?' first; the talk argues the business problem should drive the choice.
- LLMs are not the right solution for everything; classifiers remain valuable and cheaper, and token-heavy reasoning on every problem was a costly habit.
- Benchmarks built on clean data overstate real-world performance; real claims need cleanup steps upstream.
- A human in the loop plus auditability addresses most regulatory concerns (speaker's own estimate of about 70%).
- Insurers that stay slow on claims invite fraud and repeat submissions, so digital speed is a fraud control too.

## Tools mentioned
Artificial Analysis MLCR benchmark, GPT models, Anthropic models, ChatGPT, Gemini, Claude

## Relevance to our work
- **agentos** (2/3): The MLCR design (tiered difficulty, private held-out tier, expert-calibrated judges, separate completeness scoring) maps directly onto MemoryMesh's RAGAS evals for retrieval QA. → *Add a private held-out tier and expert-validated answers to MemoryMesh's eval set, and score completeness separately from accuracy and conciseness.*
- **general** (2/3): Calibrating LLM judges to expert answers before trusting them, and choosing classifier vs extractor vs LLM by task type and cost, applies to any cheap-model pipeline. → *Before using an LLM judge in a pipeline, label 50-100 samples with expert or ground-truth answers and measure judge agreement; route simple classification to a small model.*
- **prosharness** (1/3): The talk's pattern of a human decision with page-level citations of the evidence is similar to phone-driven approvals in ProsHarness. → *When a plan or approval is surfaced to the phone, show the specific evidence (file/line/span) the agent relied on, not just the summary.*
