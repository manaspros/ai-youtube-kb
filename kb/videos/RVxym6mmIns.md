# How Forward Deployed Engineering is done at Cognition — Jia Wu

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `RVxym6mmIns` · [watch](https://youtu.be/RVxym6mmIns) · **date:** 2026-08-18 · **length:** 17:38 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Jia Wu · **orgs:** Cognition, Windsurf, Nubank
- **topics:** enterprise-adoption, product-ux, software-factory · **tags:** forward-deployed-engineering, devin, enterprise-deployment, roi-measurement, legacy-migration, cobol, customer-feedback-loop, vendor-pitch

> Jia Wu (Cognition) on forward-deployed engineering: embed in enterprise customers, map Devin to real backlog problems, and measure outcomes from agent sessions. Mostly a company pitch, with some case-study numbers.

## Summary
Jia Wu, a deployed engineering lead at Cognition, describes how forward-deployed engineers (FDEs) work with enterprise customers to deploy Devin. The core idea is to maximise the overlap between what the product can do and the problems customers actually have, and to feed field findings back to the product roadmap. She argues that code writing is only about 20% of the problem, and that testing, review, deployment and maintenance are where value is found. The shift she describes is from token usage as a KPI (the "token maxing" era) to outcome metrics such as engineering hours derived from agent sessions and delivery timeline reduction. She gives anonymised case studies (a three-month embed, an ETL migration, a tax-ID system migration in Latin America) with headline numbers, but no methodology is shown. Most of the talk is positioning and culture, so treat the figures as vendor-reported.

## Key ideas
- **Forward-deployed engineers aim to maximise overlap between the product and customer problems. Solving the customer problem alone only covers part of the picture, so the feedback loop back to the product matters too.** — She frames it as two overlapping circles (product and problems). FDEs spend about half their day on customer calls to find high-leverage initiatives and the other half hands-on. ([2:53](https://youtu.be/RVxym6mmIns?t=173))
- **Coding is a mostly solved part of the job. The hard parts are testing, reviewing, deploying and maintaining code across the enterprise.** — She says writing code is only about 20% of the problem. Backlog items, remediation, delayed code, missing tests and alert triage are where she maps the product's capabilities. ([4:20](https://youtu.be/RVxym6mmIns?t=260))
- **Automate the FDE out of the loop: configure agents to run on alerts and events instead of being triggered by hand.** — The goal is for the customer's agent to respond to specific alerts or events, so the deployment runs without someone starting each job. ([5:44](https://youtu.be/RVxym6mmIns?t=344))
- **Field workarounds and customer problems should feed the roadmap. Whether a workaround becomes a feature depends on whether the problem is common across the enterprise or specific to one user.** — She describes FDEs as the bridge between product and customers, de-risking the roadmap. Feedback from the field is presented as half of the loop that makes the next deployment better. ([7:14](https://youtu.be/RVxym6mmIns?t=434))
- **The KPI has moved from token usage to measurable delivery value. Organisations now ask whether they are getting real value or just burning tokens.** — She contrasts an earlier period when budgets were subsidised and token use was the target with the current focus on proving outcomes. She claims the real differentiator is making a whole organisation faster, not just individual engineers. ([10:05](https://youtu.be/RVxym6mmIns?t=605))
- **Each agent run is a session, and session metrics are used to estimate engineering hours generated and productive hours.** — She says the team measures how many of the hours produced by sessions are productive. She argues that tools like single-point CLIs or IDEs cannot achieve org-wide impact. ([11:23](https://youtu.be/RVxym6mmIns?t=683))
- **Hiring favours T-shaped or spiky people, drawing on both product management and deep technical backgrounds.** — She says FDEs need to be broad (people, business, process, customer skills) with one deep spike. Business sense can be taught but technical depth is hard to teach on the job. ([8:39](https://youtu.be/RVxym6mmIns?t=519))

## Techniques
- **Session-based value measurement** — Treat each agent run as a session with a trajectory, derive engineering hours generated and productive hours from session metrics, and compare before and after metrics for the delivery process. *When:* When you need to show an agent's organisational value beyond token counts or raw PR counts.
- **Event-triggered agent automation** — Connect agents to alerts and events so they start on their own (for example, alert triage or remediation), removing the need for manual triggers. *When:* For recurring operational work such as alert triage, remediation and backlog clean-up.
- **Map backlog to capabilities** — List delayed code, untested areas, remediation items and backlog work inside the customer's ecosystem, then match each to a product capability. *When:* When starting an embedded deployment and deciding where the agent should be applied first.
- **Before/after delivery metrics** — Measure the same delivery metrics (tickets, sprints, PR counts, timelines) before and after the agent is introduced, then compare them. *When:* When proving the agent's impact to a customer on Agile-style delivery.
- **Autonomous legacy migration** — Hand whole migrations to the agent (ETL, COBOL, JCL, a tax-ID system) with a smaller human team, as described in her case examples. *When:* For large migrations of legacy code where the work is repetitive and few engineers want to do it.

## Numbers
- Devin scored about 13% on SWE-bench at its 2024 launch (speaker's recollection). ([0:08](https://youtu.be/RVxym6mmIns?t=8))
- Internally, over the last six months, Cognition shipped almost an order of magnitude more good-quality PRs using its own agent, while hiring lagged. ([1:32](https://youtu.be/RVxym6mmIns?t=92))
- A three-month customer embed delivered the equivalent of 150+ headcount, measured by sessions. ([11:23](https://youtu.be/RVxym6mmIns?t=683))
- Delivery timelines were compressed by about 82% across customer delivery projects (before/after comparison). ([12:48](https://youtu.be/RVxym6mmIns?t=768))
- Almost double the PRs per engineer compared with single-point tools before bringing in an agent like Devin. ([12:48](https://youtu.be/RVxym6mmIns?t=768))
- An ETL migration with a 50-engineer staff was delivered in about one-third of the timeline, done autonomously by Devin. ([14:19](https://youtu.be/RVxym6mmIns?t=859))
- A tax-identification system migration at a large Latin American bank needed about half the effort. ([14:19](https://youtu.be/RVxym6mmIns?t=859))
- PR acceptance rate is claimed to be an order of magnitude higher, and the team is said to produce the weekly output of over 10 engineers. ([14:19](https://youtu.be/RVxym6mmIns?t=859))

## Hot takes
- Coding is a mostly solved problem; the bottleneck is testing, review, deployment and maintenance.
- Single-point tools like CLIs or IDEs cannot make an organisation 10x faster, only individual engineers.
- Whoever solves ROI measurement for agents will be worth about $5 trillion.

## Tools mentioned
Devin, Devin Cloud, Windsurf, Claude Code, Cursor

## Relevance to our work
- **agentos** (1/3): Session-level productivity metrics map loosely to SkillForge's open question about the success signal, but the talk gives no method. → *Compare session-derived productive-hours metrics with SkillForge's open question on what counts as a success signal, then decide whether any of the metric definitions are worth borrowing.*
- **prosharness** (1/3): Event-triggered agent runs relate to ProsHarness loops and schedules, but the talk gives no mechanism. → *Check whether ProsHarness loops can be triggered by alerts or events, not only schedules.*
- **general** (1/3): Shows an enterprise adoption pattern where the vendor embeds engineers and ties agent value to measured delivery outcomes. → *Read the talk's session-metrics idea as one reference point when designing how to report agent value to a customer.*
