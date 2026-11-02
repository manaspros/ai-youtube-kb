# How Forward Deployed Engineering is done at Decagon — Sunny Rekhi

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `7wu2hsRfvV0` · [watch](https://youtu.be/7wu2hsRfvV0) · **date:** 2026-08-18 · **length:** 18:09 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Sunny Rekhi · **orgs:** Decagon, Hertz
- **topics:** enterprise-adoption, product-ux · **tags:** forward-deployed-engineering, productization, self-serve-integrations, customer-support-agents, agent-builder-role, org-design, hypergrowth, requirements-gathering, customer-success, field-feedback-loop

> Decagon's CTO of Forward Deployed Engineering explains how FDEs configure enterprise AI support agents, funnel customer asks into the product, and productize repeated custom work as the company grew from 50 to 500 people.

## Summary
Sunny Rekhi, CTO of Forward Deployed Engineering at Decagon (an AI customer-service agent company), describes how the FDE motion works as the company grew from about 50 to 500 people in a year. Decagon's FDEs do two jobs: configuring each enterprise's agent (tone, intents, handoff rules, back-end actions) and routing customer asks back into the product. He says FDE and product engineering now share the same bar, reporting line and often the same team. His main lessons are to resist one-off builds even though coding agents make them cheap, to define success metrics and channels in writing before building, to staff same-vertical experts onto related deals, and to productize custom work (after the 25th custom integration, Decagon built a self-serve version). He also argues for proving value fast and acting as an advisor by ranking automation candidates with historical support data. The talk is practitioner-level on org and process, with few hard numbers beyond headcount and a recruiting plug.

## Key ideas
- **An FDE at Decagon does two things: configures each enterprise's agent (tone, voice, intents to hand off, actions on the back end) and routes the problems it hits back into the product.** — Configuration is partly done in the UI. The second job is the one that scales: each enterprise ask is treated as a probable future ask from other customers. ([3:25](https://youtu.be/7wu2hsRfvV0?t=205))
- **Forward deployment engineering is treated as identical to product engineering: same bar, same reporting structure, often the same team, because a customer pain point is usually a feature to build and prioritize.** — The speaker says the line between FDE and product work is 'gone' and that this is reflected in the org chart. ([4:48](https://youtu.be/7wu2hsRfvV0?t=288))
- **With AI coding this cheap, the scarce skill is restraint. Don't prompt a coding agent to ship a one-off request; build it so future customers benefit.** — He warns that a customer-specific build can turn the agent into a 'black box of prompts and patches' that is brittle. Decagon's ethos is that customers own their agents. ([7:41](https://youtu.be/7wu2hsRfvV0?t=461))
- **At 500 people, the agent-software-engineering role was split into two lanes: agent builders (model intuition, configuration, mostly in the UI) and agent software engineers (front-line enterprise asks that go into the product).** — This split came from the need to scale design as headcount grew from 50 to 500 in about a year. ([6:15](https://youtu.be/7wu2hsRfvV0?t=375))
- **Before building, pin down what success means for the customer in the first scoping conversations: metrics, support channel (phone, email, text, WhatsApp) and the ideal outcome, ideally in writing.** — He says the temptation to start building early is strong, and that up-front requirements work is now more important as building gets faster. ([9:04](https://youtu.be/7wu2hsRfvV0?t=544))
- **Staff industry experts onto deals in the same vertical so that knowledge compounds: lingo, credibility, faster ramp, and reusable ways of defining success.** — The goal is that each deployment is faster than the last. Example verticals include financial institutions and mid-market and Fortune 20 brands. ([10:31](https://youtu.be/7wu2hsRfvV0?t=631))
- **Productize custom work. Decagon started building custom integrations for each CRM-type request, then built a self-serve integration after the 25th one. Custom work should become self-serve.** — Repeated manual work anywhere in the business is treated as a signal to bring it back into the product. ([11:57](https://youtu.be/7wu2hsRfvV0?t=717))
- **Prove value fast and act as an advisor, not only an executor: ingest historical support data to rank which automation gives the highest ROI, even when that differs from what the customer asked for.** — Multi-year partnerships expand from an initial deflection use case to revenue workflows. Example: Hertz's support deployment expanded to proactive lease-renewal outreach. ([14:17](https://youtu.be/7wu2hsRfvV0?t=857))

## Techniques
- **Define success in writing at scoping** — In the first deal conversations, get the customer's target metrics, support channels and desired outcome written down before any build starts. Then build against that. *When:* Enterprise deals, especially large ones where miscommunication about scope is likely.
- **Productize on repetition (the 25th-integration rule)** — Track custom builds that repeat across customers. Once the same integration keeps recurring, replace the custom code with a self-serve version that customers or the agent-building team can configure. *When:* A custom integration (for example a CRM connector) has been built many times and the request keeps coming back.
- **Field-to-product feedback loop** — Route anything an FDE has to do manually back to the product team. Improve the agent for all customers after each interaction, not only for the one that raised the issue. *When:* Any repeated manual step in a customer deployment, so that the agent compounds with use.
- **Same-vertical deal staffing** — Assign people who have worked with similar customers (for example, other financial institutions) to a new logo in that vertical, so vertical knowledge carries over. *When:* When the company has enough customers in a vertical to form a repeatable pattern.
- **ROI-ranked first automation** — Ingest the customer's historical support data, identify which intents or workflows would yield the most value if automated first, and sequence the rollout by that ranking, even if it differs from the customer's first ask. *When:* Scoping an automation deployment, when the customer has many possible workflows and needs quick proof of value.
- **Natural-language configuration as a platform rule** — Design the agent so it can be configured entirely through natural language, which lets non-engineers in the business make changes without custom code. *When:* When many teams need to configure the agent and engineers would otherwise be a bottleneck.
- **Two-lane split for scaling agent work** — Separate agent builders (who tune models and configuration, mostly in the UI and flag cases that need product work) from agent software engineers (who turn enterprise asks into product features). *When:* When the forward-deployed team grows large enough that one role can no longer cover both configuration and product work.

## Numbers
- Company headcount grew from about 50 people to about 500 people in roughly a year. ([6:15](https://youtu.be/7wu2hsRfvV0?t=375))
- Restated at the end: 'a year ago we were at 50 people... now we're at 500'. ([15:54](https://youtu.be/7wu2hsRfvV0?t=954))
- Custom CRM-style integrations were built by hand until the 25th one, when Decagon built a self-serve integration. ([11:57](https://youtu.be/7wu2hsRfvV0?t=717))
- Customer deployments are multi-year partnerships that expand from initial support deflection into revenue-generating workflows. No retention or ROI figures are given. ([13:16](https://youtu.be/7wu2hsRfvV0?t=796))

## Hot takes
- Vendor talk: much of it promotes Decagon's own company culture and product, and it closes with a recruiting plug. Treat it as one company's account, not a general study.
- The claim that FDE and product engineering are now the same job is a strong org-design position supported only by Decagon's experience.
- The claim that restraint is the scarce skill in the AI-coding era is asserted, not measured. No data is given on how often one-off builds caused brittleness.
- Headcount is the only quantitative claim; no ROI, deflection rate, or latency numbers are given for any customer.

## Tools mentioned
Decagon, Codex, Claude Code

## Relevance to our work
- **agentos** (1/3): The repeated-manual-work to productized-skill idea maps loosely to SkillForge's open question of when a pattern is skill-worthy. The talk offers no scoring method. → *Use repeated one-off fixes across tenants (the 25th-integration rule) as an input signal for SkillForge's skill-worthiness scoring, and promote a fix to a governed reusable skill only after it recurs.*
