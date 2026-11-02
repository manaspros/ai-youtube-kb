# The Dirty Secret of Forward Deployed Engineering — Natalie Meurer, Sierra

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Byv311hdoHE` · [watch](https://youtu.be/Byv311hdoHE) · **date:** 2026-08-18 · **length:** 16:49 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Natalie Meurer · **orgs:** Sierra, Palantir, Airbus, Google Cloud, OpenAI, Emergence Capital
- **topics:** enterprise-adoption, product-ux · **tags:** forward-deployed-engineering, customer-engineering, palantir, outcome-based-pricing, agent-engineering, org-design, hiring

> Sierra's head of agent engineering traces forward-deployed engineering from Palantir's 2008-2020 eras to today, argues the title is vague, and says customer accountability and outcome pricing make most engineering roles trend toward it.

## Summary
Natalie Meurer (Sierra) argues that "forward-deployed engineer" has become so broad it barely describes a job. She traces the role through Palantir: it began as DevOps and platform stability (her onboarding task was deploying software to an EC2 instance), added data integration and ontology work, then moved to custom dashboards, Foundry, and customer enablement. Her main through-line is that every version of the role is accountable to the customer. She says coding agents make code cheap, so forward-deployed engineers can build end-to-end and product engineering is becoming client-facing. She also links this to pricing moving from seats to usage to outcomes, which requires someone to guarantee the outcome. The talk is mostly history and opinion with little technical detail, and it ends with a hiring pitch.

## Key ideas
- **The forward-deployed engineer title now covers so many jobs that it means little** — The speaker says the role is a term used to describe many different things, so it is hard to define. Her thesis is that the title is not one job. ([0:08](https://youtu.be/Byv311hdoHE?t=8))
- **FDE work began as DevOps and platform stability, and location mattered because of on-prem deployments** — Early Palantir FDEs sat with customers because deployments were on-prem. Her onboarding project was to deploy the software on an EC2 instance, and much of the job was keeping the platform running. ([3:45](https://youtu.be/Byv311hdoHE?t=225))
- **Data integration and an ontology came next** — After the platform stabilized, Palantir sold data integration. FDEs had to connect customer data spread across many systems. The ontology, a taxonomy for that data, was how they modeled it. Custom solutions were built with a drag-and-drop dashboard tool called Slate. ([6:15](https://youtu.be/Byv311hdoHE?t=375))
- **A dashboard that does not write back to the source data decays** — Palantir found that dashboards that only read data became less useful over time. The move to Foundry aimed at going from data to decisions, and FDEs also began enabling customers to do the work themselves, using Airbus Skywise as the example. ([7:42](https://youtu.be/Byv311hdoHE?t=462))
- **Use the FDE vintage as an interview probe** — She proposes asking candidates which era of the role they did: 2008 platform work, 2012 data integration, 2016 custom dashboards, 2020 enablement, or today. The answer shows what work they actually did. ([10:07](https://youtu.be/Byv311hdoHE?t=607))
- **Customer accountability is the one constant across FDE variants** — Job postings combined into one list ask for a very wide mix of skills. The common thread is that every FDE is accountable to the customer, whether for DevOps, enablement, custom solutions, or data integration. ([11:31](https://youtu.be/Byv311hdoHE?t=691))
- **Cheap code blurs product engineering and client-facing work** — When coding agents make code cheap, FDEs can build end-to-end solutions and feed customer signals back into the product. At Sierra, she says, product engineers are also becoming client-facing. ([12:49](https://youtu.be/Byv311hdoHE?t=769))
- **Outcome pricing needs someone accountable for the outcome** — She describes pricing moving from seats to usage to outcomes. Outcome-based pricing is possible only when the product can be credited with the result. That makes the guarantee of the outcome the key requirement, and she argues it is the core of FDE work. ([14:07](https://youtu.be/Byv311hdoHE?t=847))

## Techniques
- **Write-back dashboards** — Let dashboards or analysis tools write decisions, edits, or corrections back to the source system so the data stays current instead of decaying. *When:* When building an internal or customer-facing dashboard whose value depends on the data staying up to date.
- **Ontology-first data modeling** — Before building a solution, define a shared taxonomy for the customer's entities and map each source system onto it. *When:* When integrating data from many customer systems that describe the same things differently.
- **Customer-accountable build loop** — Have engineers who own a customer outcome build the solution end-to-end with coding agents, then route what they learn back into the product. *When:* When fast customer feedback matters more than a clean handoff between sales, solutions, and product teams.
- **Outcome-attribution test for pricing** — Ask whether the outcome can be credibly attributed to the product. Price by seat when it cannot, by usage when attribution is partial, and by outcome when it can be guaranteed. *When:* When deciding how to price an agent product, especially a customer-experience product where the result is measurable.
- **FDE vintage interview question** — Ask candidates which era of forward-deployed work they did (platform, data integration, dashboards, enablement, or AI today) and what they owned in it. *When:* When interviewing for a forward-deployed or customer-engineering role to find out what the candidate actually did.

## Numbers
- Speaker's Palantir tenure was 2016 to 2021, working on the privacy team and as an FDE and infrastructure engineer ([1:22](https://youtu.be/Byv311hdoHE?t=82))
- Speaker's Sierra tenure is about two years, from 2024 to 2026, joining on the deployment team ([1:22](https://youtu.be/Byv311hdoHE?t=82))
- She wrote an article in July 2024 proposing agent engineering as a sub-discipline with the same customer accountability as FDE work ([1:22](https://youtu.be/Byv311hdoHE?t=82))
- The FDE vintages she names are 2008, 2012, 2016, 2020, and today (2026) ([10:07](https://youtu.be/Byv311hdoHE?t=607))
- A combined FDE job-posting example asks for eight years as a staff engineer, six years of direct sales, and four years as a solution architect ([11:31](https://youtu.be/Byv311hdoHE?t=691))

## Hot takes
- The forward-deployed engineer title now means so many things that it means nothing.
- A dashboard that does not write back to its source data decays and becomes less useful.
- Most AI software pricing will move from seats to outcomes, so engineers will have to own customer outcomes.
- Almost everything in engineering is trending toward forward-deployed engineering.

## Tools mentioned
Palantir Foundry, Palantir AIP, Palantir Slate, AWS EC2, Airbus Skywise, Retool (comparison only)

## Relevance to our work
- **general** (1/3): Useful framing for how agent-product roles and pricing are changing, with no technical takeaways. → *Skim only if preparing for customer-engineering or FDE hiring conversations.*
