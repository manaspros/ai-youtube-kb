# How to Leverage Domain Expertise — Chris Lovejoy, Notius Labs

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `kfSDc2eVLo4` · [watch](https://youtu.be/kfSDc2eVLo4) · **date:** 2026-05-18 · **length:** 24:45 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Chris Lovejoy · **orgs:** Notius Labs, Tandem, Anterior, Granola, Gartner
- **topics:** enterprise-adoption, product-ux, evals · **tags:** domain-expertise, vertical-ai, org-design, oracle-evaluator-architect, ai-quality, last-mile, healthcare, prior-authorization, hiring, ownership

> Chris Lovejoy (Notius Labs) argues winning in vertical AI is an organizational problem, and gives a three-role framework (oracle, evaluator, architect) for placing domain experts, with Granola, Tandem and Anterior as cases.

## Summary
Chris Lovejoy, a former doctor turned AI builder who worked at Tandem and Anterior, argues that the main lever in vertical AI is how an organization brings domain expertise into the product, not which model it uses. He frames three roles a domain expert can play: oracle (directly improves outputs by tweaking prompts, documents and tools), evaluator (defines metrics and sets up measurement, while engineers make the changes), and architect (designs systems that improve automatically from usage). A short decision guide asks whether quality can be measured objectively and whether manual iteration is fast enough to choose between them. He recommends starting with an oracle, moving on only when things break at scale and a measurable metric exists, and he walks through Granola, Tandem and Anterior as case studies of this progression. He closes with hiring and ownership advice: name one principal domain expert who is accountable and in the room for decisions, hire for domain depth first and pair it with complementary skills, and let that person's role evolve as the product grows. The talk is a framework with anecdotes rather than hard benchmarks.

## Key ideas
- **Winning in vertical AI is an organizational problem more than a model problem** — The speaker's thesis: the system for getting domain insight into the product matters more than model or pipeline sophistication. Front-end models are good enough; the gap is operationalizing expert judgment around them. ([2:12](https://youtu.be/kfSDc2eVLo4?t=132))
- **Three ways a domain expert can be built in: oracle, evaluator, architect** — Oracle: the expert directly improves outputs (prompts, docs, tools) and does both assessing and fixing. Evaluator: the expert defines quality metrics and measurement, and engineers make the changes. Architect: the expert designs a system that improves itself from user interactions with little human in the loop. ([5:20](https://youtu.be/kfSDc2eVLo4?t=320))
- **Decision guide: measurability and iteration speed pick the role** — If quality cannot be measured in metrics (taste matters more), use an oracle, and one may be enough or several may cover sub-segments. If it can be measured and engineers' manual iteration is fast enough, use an evaluator. If manual iteration is too slow and improvements can be automated, use an architect. ([8:43](https://youtu.be/kfSDc2eVLo4?t=523))
- **Start as an oracle and move on only when there is a trigger** — A startup's domain expert should usually begin as the oracle. Moving to evaluator or architect is necessary only when things break at current scale, and evaluator needs an objective metric to exist first. Roles can progress in different directions depending on the company. ([9:43](https://youtu.be/kfSDc2eVLo4?t=583))
- **Granola and Tandem show oracle at different scales** — Granola's first employee, a writer, wrote the prompts and remains the quality gatekeeper, because no single meeting note is objectively best. Tandem's first clinician-oracle could not keep up, so they hired many doctors by specialty and country, and the platform supports per-customer prompt variants. ([10:43](https://youtu.be/kfSDc2eVLo4?t=643))
- **Anterior's path from oracle to architect came from variation in customer rules** — The speaker first reviewed outputs himself as a clinical oracle, then defined failure modes, built a clinician review dashboard and metrics (evaluator), and then found that variation in how each insurer reads its rules needed a system that learns at the edge (architect). ([15:07](https://youtu.be/kfSDc2eVLo4?t=907))
- **Skills to look for depend on the role; domain depth is the base** — Oracles need direct experience of the exact use case, not just the profession (a doctor is not enough for medical coding). Evaluators need data-science skills to define and collect metrics. Architects need experience with LLM products and some engineering. Prompting and communication are helpful but more learnable. ([17:37](https://youtu.be/kfSDc2eVLo4?t=1057))
- **Appoint one principal domain expert with real ownership** — One accountable person avoids consensus by committee and gives them time to understand the AI deeply. They should be in the room for decisions, not only advise. A failure mode: two senior clinicians with unclear authority were slow, and both left after 12-18 months. ([20:00](https://youtu.be/kfSDc2eVLo4?t=1200))
- **Hire for domain depth first, then breadth, and plan for growth** — Domain expertise is a given, but no one has every skill, so pair the expert with complementary hires such as a statistician. The failure mode is hiring a pure domain expert who cannot grow into evaluator or architect. Keeping the same person through the stages preserves the context they have built up. ([21:23](https://youtu.be/kfSDc2eVLo4?t=1283))

## Techniques
- **Oracle role (domain expert edits the product directly)** — The expert reviews traces and outputs, plays with the product, and tweaks prompts, adds documents or tools, improving outputs themselves in a tight loop. *When:* Early stage or small scale, when quality is hard to measure and taste matters (e.g. meeting notes).
- **Decentralized oracle** — Hire several domain experts, each owning a subset such as a specialty, country or customer segment. The platform supports a long tail of prompt customizations so each expert's version can go live for their segment. *When:* One expert cannot keep up and the output varies by segment, but manual judgment is still needed.
- **Evaluator role (expert defines metrics; engineers improve)** — Define quality metrics and failure modes, build a review dashboard, have domain reviewers grade a sample of outputs, and optionally use LLM-as-judge or customer usage metrics as a north star. Feed the findings to engineers who make the changes. *When:* Quality can be measured objectively and manual engineer iteration is still fast enough.
- **Architect role (self-improving system)** — Design a system that learns from usage and improves automatically with little human review in the loop, using levers such as prompts, documents and tools, and adapting at the customer edge. *When:* Manual iteration is too slow for the variation in customer rules, and improvements can be automated against a metric.
- **Role progression check** — Before advancing, ask whether the current stage is breaking at scale, and whether an objective metric exists for the next stage. *When:* Deciding whether to hire for or move the domain expert to the next role.

## Numbers
- About 100,000 people saw the speaker's previous talk on the last-mile problem across platforms ([1:11](https://youtu.be/kfSDc2eVLo4?t=71))
- Gartner: about 50% of generative AI projects were abandoned last year (speaker's cited figure) ([3:18](https://youtu.be/kfSDc2eVLo4?t=198))
- Vertical SaaS was a roughly $50B-or-so market; AI moving into labor could be a multi-trillion-dollar market (speaker's rough framing) ([3:18](https://youtu.be/kfSDc2eVLo4?t=198))
- Granola passed a $1B valuation (the speaker says 'evaluation') ([10:43](https://youtu.be/kfSDc2eVLo4?t=643))
- Prior auth outputs are binary: approve or escalate to clinician review, judged against medical evidence ([15:07](https://youtu.be/kfSDc2eVLo4?t=907))
- Two senior clinicians with unclear ownership left after about 12-18 months ([20:00](https://youtu.be/kfSDc2eVLo4?t=1200))

## Hot takes
- Winning in vertical AI is an organizational problem, not a best-model problem.
- Front-end models are good enough; the gap is how organizations operationalize expert judgment.
- Hire the principal domain expert early and give them ownership; advisory roles slow progress.
- A pure domain expert hire can become a ceiling if they cannot grow into evaluator or architect roles.

## Tools mentioned
LLM-as-judge, clinician review dashboard

## Relevance to our work
- **agentos** (1/3): The oracle/evaluator/architect ladder maps onto the SkillForge/EvolveCraft self-improvement idea. The talk's rule is that automated improvement only pays once an objective metric exists and manual iteration is too slow. → *Before building automated improvement in EvolveCraft or SkillForge, write down failure modes and one objective metric per agent use case, and check whether the stage should still be manual.*
- **general** (1/3): Useful framing for evals: decide whether a task has an objective metric before investing in automation, and use a named owner for quality decisions. → *Use the talk's measurability test as a checklist before building an eval harness for a new agent task.*
