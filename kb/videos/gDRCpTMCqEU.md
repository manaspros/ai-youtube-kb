# What Technical Due Diligence Finds When the Deck Says “70% Automated” — Soukaïna Abelhad

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `gDRCpTMCqEU` · [watch](https://youtu.be/gDRCpTMCqEU) · **date:** 2026-10-14 · **length:** 6:29 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Soukaïna Abelhad · **orgs:** Faros, Uber, Meta, Builder.ai, Wall Street Journal, Financial Times
- **topics:** evals, governance-compliance, enterprise-adoption · **tags:** due-diligence, automation-claims, llm-as-judge, unit-economics, straight-through-processing, pr-metrics, vendor-evaluation

> A technical due diligence checklist for AI productivity claims: check the arithmetic of workload vs. human labor, define what "automated" means, and verify quality with experts before trusting a number.

## Summary
Soukaina Abelhad, an AI tech lead who evaluates AI systems in production, gives a six-minute talk on checking vendor and investor claims such as "70% automated." She proposes three checks. First, do the arithmetic: compare workload volume with fully loaded human labor, including the people whose jobs exist because of AI, such as reviewers, operators and rework. Second, pin down the definition of automation, using a ladder from AI-drafted to fully autonomous and a straight-through processing boundary. Third, ask who defines quality and whether a judge was validated against experts, because automated graders can be far more optimistic than human reviewers. Surviving claims should then be translated into cost per accepted autonomous task, counting review, escalation and rework. She cites Faros telemetry, a Meta grader-vs-maintainer gap, and the Builder.ai collapse as illustrations, and notes that the Builder.ai case involved financing problems beyond AI claims.

## Key ideas
- **Workload growth without headcount change is a warning sign.** — Faros telemetry showed high-AI-adoption teams merged 98% more PRs, review time rose 91%, and PRs grew 154% larger. She argues that if human labor tracks workload volume, the claim describes assistance, not labor removal. The data is observational, so it is a warning, not proof. ([1:05](https://youtu.be/gDRCpTMCqEU?t=65))
- **Count everyone whose work exists because of AI.** — In diligence, include operators, reviewers, trainers, escalation handlers and rework in the labor figure, not just the people who were cut. ([1:38](https://youtu.be/gDRCpTMCqEU?t=98))
- **AI-attributed and autonomous are different claims.** — Uber's 70% of PRs being AI-attributed does not give the autonomous rate, and the period and total count were not disclosed. Automation claims sit on a ladder: AI-drafted, human-edited, human-approved, or no human intervention. Define a boundary and measure straight-through processing inside it. ([2:11](https://youtu.be/gDRCpTMCqEU?t=131))
- **Automated graders can be far too optimistic.** — Per the speaker, Meta found a 24-point gap between an automated grader and maintainers' merge decisions after adjusting to the human baseline. Four maintainers reviewed 296 AI-generated PRs blind to source. She describes a similar project where all 10 outputs passed automated validation, but few survived expert review. ([3:18](https://youtu.be/gDRCpTMCqEU?t=198))
- **Evaluation maturity is the first credibility signal.** — Ask who labeled ground truth, whether experts agree with each other and whether that agreement is measured, what the automated judge was validated against, and what bad output escaped. ([3:51](https://youtu.be/gDRCpTMCqEU?t=231))
- **Warnings existed but the process did not turn them into a gate.** — She cites a 2019 WSJ questioning of Builder.ai's AI claims and a 2025 FT report that 2024 revenue estimates were revised from $220M to about $55M. She says the insolvency also involved financing and revenue issues beyond AI claims, so the case is not proof that AI positioning alone caused the failure. ([4:23](https://youtu.be/gDRCpTMCqEU?t=263))
- **Finish with unit economics, not the headline percentage.** — Start from eligible workflow value, apply real adoption, straight-through success and accepted quality, then subtract AI cost, human review, escalation and rework. The metric to ask for is cost per accepted autonomous task, where failures and rework count as cost. ([4:56](https://youtu.be/gDRCpTMCqEU?t=296))

## Techniques
- **Workload-vs-labor arithmetic check** — Put workload volume (PRs, tickets, tasks) next to fully loaded human labor, including reviewers, trainers, operators, escalation and rework. If labor scales with volume, the claim is assistance, not removal. *When:* Evaluating any productivity or headcount-reduction claim from an AI vendor or company.
- **Straight-through processing boundary** — Borrow the finance term. Define an end-to-end boundary (draft, approval, or production) and measure the share of tasks completed with no human intervention inside it. Keep the attribution rate and autonomous rate separate. *When:* Before accepting any 'X% automated' or 'X% AI-written' figure.
- **Blind expert review of grader output** — Have maintainers or domain experts judge outputs without knowing their source, then compare their accept/reject decisions with the automated grader. Measure the gap and the agreement among experts. *When:* Validating an LLM-as-judge or automated test suite before trusting its pass rate.
- **Cost per accepted autonomous task** — Take eligible workflow value, multiply by adoption, straight-through success and accepted quality, then subtract AI run cost plus human review, escalation and rework. Failed or escalated tasks stay in the cost. *When:* Turning an automation claim into a unit-economics decision.
- **Diligence questions checklist** — Ask: What is the 18-month theory? Who labeled ground truth? Does the expert agree? What was the judge validated against? What bad output escaped? What is the period and denominator? *When:* Meetings with vendors, investors or internal teams presenting AI productivity numbers.

## Numbers
- High-AI-adoption teams merged 98% more PRs (Faros, 10,000+ developers, 1,255 teams, observational) ([1:05](https://youtu.be/gDRCpTMCqEU?t=65))
- PR review time up 91% and average PR size up 154% for high-adoption teams ([1:05](https://youtu.be/gDRCpTMCqEU?t=65))
- Meta: 24-point gap between automated grader and merge decisions after adjusting to human baseline (296 AI PRs, 4 maintainers, 3 repos) ([3:18](https://youtu.be/gDRCpTMCqEU?t=198))
- Builder.ai 2024 revenue estimate revised from $220M to about $55M (FT, May 2025); Chapter 7 filed June 2 ([4:23](https://youtu.be/gDRCpTMCqEU?t=263))
- Speaker's cited controlled study: 55.8% faster with 95 developers, one JS HTTP server task, 12 visible tests ([0:00](https://youtu.be/gDRCpTMCqEU?t=0))
- Uber: 70% of PRs AI-attributed (period and total count not disclosed) ([2:11](https://youtu.be/gDRCpTMCqEU?t=131))

## Hot takes
- A number can be a genuine measurement and still support a conclusion it cannot back up.
- Automated graders are often far more optimistic than the humans who accept the work.
- Built for the memo, not for the demo.

## Tools mentioned
Faros telemetry, Meta grader study

## Relevance to our work
- **general** (2/3): A practical checklist for judging AI productivity claims, useful for any vendor or internal metric review. → *Apply the three checks (arithmetic, definition, quality validation) to the next vendor AI productivity claim before using it in a plan.*
- **agentos** (1/3): Eval rigor applies to RAGAS and judge-based evals in MemoryMesh, but the talk gives no infra or technical method for AgentOS. → *When reporting AgentOS benchmark numbers, record the validation set for any LLM judge and the expert agreement rate.*
- **prosharness** (1/3): Relevant to ProsHarness's plan critique and approval loops, where automated checks may overstate completion. → *Track rework and escalation as part of the cost of each harness-completed task, and check whether automated pass signals were validated against a human decision.*
