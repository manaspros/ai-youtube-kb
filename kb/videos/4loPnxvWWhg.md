# Your Fine-Tuned Model Is Tech Debt: A 50x ROI House of Cards — Dan Bjornn, Lease End

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `4loPnxvWWhg` · [watch](https://youtu.be/4loPnxvWWhg) · **date:** 2026-09-18 · **length:** 16:39 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Dan Bjornn · **orgs:** LeaseEnd
- **topics:** training-finetuning-rl, context-engineering, evals, enterprise-adoption · **tags:** fine-tuning, tech debt, intent classification, skills over retraining, model lock-in, cost per message, production regressions, SMS assistant, curated regression set, model-agnostic

> A LeaseEnd data scientist explains how fine-tuning an intent classifier for customer texts became costly tech debt, and how replacing it with editable skills and prompts on a frontier model cut fix time from a week to under an hour.

## Summary
Dan Bjornn, a senior data scientist at LeaseEnd, describes a text-message assistant that helps auto-lease customers reach sales reps. The first version used a RAG workflow over classified messages, which missed nuance, so the team fine-tuned a small model for six-way intent classification. Fine-tuning brought accuracy and revenue gains (he cites $12M in a year at a 50x ROI), but each fix needed data gathering, synthetic examples, manual labeling, and a regression-prone retrain that took about a week. He calls the accumulated rigidity a "calcification tax": the team stayed locked to one model version because switching providers meant reworking training data, and it could not adopt newer architectures. They rebuilt the app as an agentic framework driven by skills, tools and resources, where a fix means editing the affected prompt or skill, validating on a curated production set, and uploading Markdown files to S3. The per-message API cost rose, but accuracy improved, total cost fell, and the system became model-agnostic. His closing checklist says to fine-tune only when a frontier model truly cannot be called, for privacy or offline needs.

## Key ideas
- **Fine-tuning looked like the obvious choice for a narrow, structured intent-classification task, and it did lift accuracy and revenue.** — The team had six intent buckets and thousands of messages a day, and wanted better accuracy plus lower cost and latency from a smaller model. The app reportedly brought in $12M of revenue in its first year. ([1:07](https://youtu.be/4loPnxvWWhg?t=67))
- **Fine-tuned models accumulated hidden debt: each fix was a slow, regression-prone retrain.** — Failures included a confirmer that re-engaged after an appointment confirmation and a model that called a customer right after a greeting. Each fix needed new examples, synthetic data, manual validation, and labeling. Training itself took about an hour, but the full cycle took about a week, and fixing one issue often broke another. ([4:01](https://youtu.be/4loPnxvWWhg?t=241))
- **Triage before retraining: ask how frequent the issue is, how much it hurts customers, and whether a band-aid fix exists.** — Customer-harming bugs were fixed right away. Other issues were batched until enough had built up to justify a retrain, which he calls the calcification tax. ([8:20](https://youtu.be/4loPnxvWWhg?t=500))
- **The fine-tune locked the team in twice, to a model version and to an architecture.** — Switching models meant reworking training data, which differs by provider and even by version. The app was built in late 2024 when workflows were the standard, and the team could not take advantage of newer architectures. ([9:43](https://youtu.be/4loPnxvWWhg?t=583))
- **Moving to skills, tools and resources in an agentic framework made fixes a prompt edit instead of a retrain.** — The team realized, from using Claude Code, that they could change the context instead of the model. The rebuild went out as one of the first production tests of an agentic framework already in progress. ([11:13](https://youtu.be/4loPnxvWWhg?t=673))
- **The fix loop shrank from about a week to under an hour, and the team's deploy step became uploading Markdown files to S3.** — Find a problem, adjust the affected system prompt or skill, validate on a curated set gathered during production, iterate, and deploy. Accuracy rose above the fine-tuned model's, while the per-message API cost went up. ([12:13](https://youtu.be/4loPnxvWWhg?t=733))
- **Judge the decision on total cost, not per-message price, and check the four reasons people give for fine-tuning.** — The speaker's checklist covers accuracy, total cost, latency and vendor control. Smaller-model latency gains were marginal, and the rebuild was cheaper overall because the team spent less time on upkeep. Fine-tuning remains reasonable for privacy or offline needs, but it must still beat the tax. ([13:41](https://youtu.be/4loPnxvWWhg?t=821))

## Techniques
- **Skill and prompt edits as the default fix** — Keep behavior in editable skill and system-prompt files that load context into a frontier model. For a bug, change the affected skill or prompt, then iterate. *When:* When a production LLM system is making recurring errors and retraining would be slow or lock in a model.
- **Curated production regression set as the gate** — Collect real conversations from production over time into a curated set. Run every prompt or skill change against it before deploying, so earlier fixes do not regress. *When:* Whenever you iterate on prompts or skills in production and need a fast, repeatable quality check.
- **Markdown-file deploys to object storage** — Publish prompt and skill changes by uploading Markdown files to an S3 bucket, with no retrain or model deploy step. *When:* When the system's behavior lives in text files and fixes need to ship within the hour.
- **Triage gate before retraining** — Before any retrain, rank issues by frequency and customer pain. Fix severe ones immediately with a band-aid, and batch the rest until a retrain is worth its cost. *When:* When each training cycle is expensive and issues arrive one at a time.
- **Fine-tuning pre-check list** — Before fine-tuning, verify that accuracy, total cost (including upkeep), latency and vendor control would each really be improved. Fine-tune only if none of these can be met by calling a frontier model, such as for privacy or offline needs. *When:* When someone proposes fine-tuning a narrow classifier and wants to know whether it is worth it.
- **LLM-judge labeling with manual review and holdout sets** — Label collected examples with an LLM as judge, have a human review the labels, then hold out a test set before fine-tuning. The speaker used this pipeline and synthesized examples when data was short. *When:* When fine-tuning is chosen and labeled data must be built from production traffic.

## Numbers
- Revenue brought in by the LLM text application within a year of launch, with a 50x ROI (the speaker's claim). ([4:01](https://youtu.be/4loPnxvWWhg?t=241))
- Volume: the app responded to thousands of messages a day in real time. ([2:34](https://youtu.be/4loPnxvWWhg?t=154))
- Intent classification had six categories. ([2:34](https://youtu.be/4loPnxvWWhg?t=154))
- Fine-tuning run itself took about an hour, but the full fine-tune cycle (data gathering, labeling, validation, iteration, deploy) took about a week. ([6:51](https://youtu.be/4loPnxvWWhg?t=411))
- Time from discovering a problem to deploying the fix dropped to under an hour after the skills rebuild. ([12:13](https://youtu.be/4loPnxvWWhg?t=733))
- Per-message API cost rose after the rebuild because better models were used, but total cost went down. ([12:13](https://youtu.be/4loPnxvWWhg?t=733))
- Latency gains from smaller fine-tuned models were marginal (no figures given). ([15:08](https://youtu.be/4loPnxvWWhg?t=908))

## Hot takes
- Fine-tune only when you literally cannot call a frontier model, and even then the decision still has to beat the tax.
- Fine-tuned models that look like textbook cases still become tech debt.
- Teams that judge the cost of a model by per-message price are looking at the wrong cost; total cost includes the upkeep time.
- A data scientist's fine-tuning pipeline can be the thing that locks a team in.

## Tools mentioned
Claude Code, Amazon S3, OpenAI, Anthropic

## Relevance to our work
- **general** (2/3): Context engineering is a recurring interest. The talk is a concrete production case for fixing LLM behavior through context, backed by a validation loop and a triage method. → *Read the talk's triage rules (frequency, customer harm, band-aid first) as a checklist for deciding whether a fix should go into the prompt or into a model change.*
- **agentos** (1/3): SkillForge's governed skills are the same kind of editable artifact the talk relies on, and its deploy and validation loop is directly comparable. Fine-tuning is not part of AgentOS's current scope. → *Compare SkillForge's skill rollout with the talk's loop of edit, validate on a curated production set, then ship as a file, and check whether SkillForge needs a regression gate before a skill goes live.*
- **prosharness** (1/3): ProsHarness drives Claude Code runs with skills, and the talk's argument for keeping behavior in skill files is related to that design. → *Check that ProsHarness keeps its fix path in skill and prompt files that can be changed without a model change, and add a small replayed regression set per skill.*
