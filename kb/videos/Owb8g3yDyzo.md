# Why Off-the-Shelf AI Doesn't Understand Money — Udi Menkes, Intuit

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Owb8g3yDyzo` · [watch](https://youtu.be/Owb8g3yDyzo) · **date:** 2026-08-18 · **length:** 19:50 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Udi Menkes · **orgs:** Intuit, Princeton
- **topics:** training-finetuning-rl, evals, enterprise-adoption · **tags:** grounding, outcome-data, causal-inference, uplift-modeling, reinforcement-learning, financial-advice, fluent-bluff, business-advisor, long-horizon-simulation

> Intuit's Udi Menkes argues frontier LLMs give fluent but unverified money advice, and that grounding a model in real business outcomes (state, action, outcome) beats model size.

## Summary
The speaker, a principal PM at Intuit, says off-the-shelf LLMs give confident financial advice ("fluent bluff") that is not based on what actually happened to similar businesses. He shows examples from a study of about 100,000 business situations where frontier models suggested risky moves, such as taking on a second rental property or cutting prices on a key customer, while a grounded model suggested safer actions. He cites a Princeton simulation where most frontier models went bankrupt over 500 simulated days and a simple rules-based system did better. His method builds business states from ledger and product data, derives actions and multi-horizon outcomes, and trains an RL model on millions of such trajectories. A frontier LLM proposes candidate actions, the outcome-trained model ranks them, and a second LLM turns the result into an explanation grounded in similar businesses. He claims a mid-size model tuned this way beat frontier models head-to-head, and argues the moat is proprietary outcome data rather than model access. The talk is partly a product pitch for Intuit's advisor, and the headline numbers are not independently checkable from the talk.

## Key ideas
- **Frontier LLMs produce a fluent, confident answer ('fluent bluff') on money questions because they learned from text about money, not from what happened to businesses.** — Speaker's example: a live audience trusted LLM answers but few followed them. Changing one assumption flipped the model's recommendation back and forth, showing the advice sounded sound but was not reliable. ([0:08](https://youtu.be/Owb8g3yDyzo?t=8))
- **Models with full company context still give harmful advice because text knowledge is not experience.** — Landlord case: frontier model said buy a second rental while already cash-flow negative; a model grounded in outcomes of similar businesses said raise rents 5-10% before renewal. Speaker says more context alone does not fix this. ([3:06](https://youtu.be/Owb8g3yDyzo?t=186))
- **Ranking by 'what similar entities did and what happened' exposes bad textbook advice, such as cutting the biggest cost when that cost supplier drives most revenue.** — Apparel case: one vendor was 80% of cost and enabled 97% of revenue. The textbook move would have cut almost all revenue. ([9:46](https://youtu.be/Owb8g3yDyzo?t=586))
- **Raw before/after or group differences overstate the effect of an action because better businesses are more likely to take it.** — Restaurant price-rise example: a raw gap of $1,400/day shrinks to about $1,150/day after matching groups on the propensity to raise prices. The speaker measures this with a conditional average treatment effect. ([10:47](https://youtu.be/Owb8g3yDyzo?t=647))
- **Frontier models should generate candidate actions, while a separately trained outcome model decides which candidates are good.** — Pipeline: the LLM proposes hypotheses; an RL-trained model scores them using outcome data; the speaker says this separates right moves from mistakes that would drive the business down. ([13:19](https://youtu.be/Owb8g3yDyzo?t=799))
- **Build training data as (state, action, outcome) trajectories from many entities across products.** — Business state is a detailed summary at a point in time from the general ledger, P&L, cash flow and invoices. Actions are derived from ledger events such as campaign spend or payroll. Outcomes are measured over several horizons (profit, revenue, cash flow, time). Data comes from QuickBooks, TurboTax, Credit Karma and Mailchimp. ([13:19](https://youtu.be/Owb8g3yDyzo?t=799))
- **A mid-size model grounded in outcomes can beat frontier models, so the defensible asset is proprietary outcome data, not model access.** — Speaker says the model was tested head-to-head against leading models and the mid-size model won. He argues bigger models do not close the gap; embedding verified experience does. ([14:46](https://youtu.be/Owb8g3yDyzo?t=886))
- **A good advisor needs both grounded evidence and an understanding of the user's preferences, and the explanation should show the similar-business reasoning.** — The beta product recommends actions, explains them by pointing to similar businesses and their results, and lets users drill into action plans. ([17:17](https://youtu.be/Owb8g3yDyzo?t=1037))

## Techniques
- **Outcome-grounded trajectory dataset** — Snapshot each entity's state at fixed times, derive actions from logged events, measure outcomes at several horizons, and store (state, action, outcome) tuples across many entities. *When:* You have many similar entities with logged actions and verifiable later outcomes in your own system of record.
- **Propose-then-rank split** — Use a frontier LLM only to generate candidate actions, then rank or veto those candidates with a model trained on recorded outcomes. *When:* Generic LLM suggestions are plausible but may be harmful, and you have outcome labels to train a scorer.
- **Propensity-matched uplift estimate** — Compare groups that were equally likely to take an action, then estimate the conditional average treatment effect instead of the raw difference in outcomes. *When:* You want to know whether an action caused a result, and high-performing entities may self-select into the action.
- **Evidence-grounded explanation** — Have the LLM write the final advice from retrieved outcomes of similar entities (who did what and what happened), not from its own prior knowledge. *When:* Users need to trust a recommendation and can check the cited peer cases.
- **Long-horizon simulation with a rules baseline** — Give models tools and data in a simulated environment over many steps, and compare against a simple rules-based policy; the speaker cites a Princeton study that did this over 500 days. *When:* You need to test whether an agent can make multi-step decisions over time, not just answer single questions.

## Numbers
- Study covers about 100,000 business situations and time frames across thousands of businesses. ([1:38](https://youtu.be/Owb8g3yDyzo?t=98))
- Across the study, about 40% of frontier-model advice was essentially 'acquire a new customer', and another 14% was 'increase revenue from the product'; more than half combined. ([5:10](https://youtu.be/Owb8g3yDyzo?t=310))
- Princeton simulation: each model got $1M and a 500-day harness with tools and data. Most models drove the company bankrupt before day 500. A simple rules-based system beat almost all of them. ([6:12](https://youtu.be/Owb8g3yDyzo?t=372))
- Egg supplier example: one customer was 70% of revenue and one vendor was nearly all costs. Frontier model suggested raising prices 15-20% on the main customer; the grounded model suggested a 5-10% vendor cost cut. ([4:10](https://youtu.be/Owb8g3yDyzo?t=250))
- Restaurant price-raise example: treated group gained $4,200/day vs $2,800/day for the untreated group. Naive difference $1,400/day; after matching, about $1,150/day. ([11:49](https://youtu.be/Owb8g3yDyzo?t=709))
- Apparel example: 80% of cost came from one vendor that enabled 97% of revenue. ([9:46](https://youtu.be/Owb8g3yDyzo?t=586))
- Training data: millions of business trajectories (state, action, outcome) from Intuit products. ([13:19](https://youtu.be/Owb8g3yDyzo?t=799))

## Hot takes
- Off-the-shelf LLMs do not understand money; almost every money answer they give is a fluent bluff.
- You do not close the gap with bigger models; you close it by embedding verified experience from outcomes in your data.
- A simple rules-based system beat almost all frontier models on long-horizon business decisions.
- The moat is the proprietary data and outcomes, not access to the model.

## Tools mentioned
QuickBooks, TurboTax, Credit Karma, Mailchimp, reinforcement learning (Intuit in-house model)

## Relevance to our work
- **agentos** (1/3): L2D SkillForge lists the success signal for mining agent telemetry as an open question. The talk's approach of labelling (state, action, outcome) trajectories with later verified results is one way to define that signal, though the talk is about financial decisions, not coding skills. → *Read the talk's (state, action, outcome) framing and test whether SkillForge can label skill-mined trajectories with downstream task results, such as tests passing or PRs merged, as its success signal.*
- **prosharness** (1/3): The propose-then-rank split (frontier model proposes, a separate outcome-trained model decides) is a loose analogue of ProsHarness's plan, critique and debate steps. The talk gives no coding-agent specifics. → *Consider whether ProsHarness's critique step should be scored against recorded outcomes of past runs, rather than relying only on another model's judgement.*
