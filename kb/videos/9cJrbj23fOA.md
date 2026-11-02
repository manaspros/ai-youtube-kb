# The Chief AI Officer: Scientist, Architect, Coach — Rania Khalaf, WSO2

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `9cJrbj23fOA` · [watch](https://youtu.be/9cJrbj23fOA) · **date:** 2026-10-04 · **length:** 22:22 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Rania Khalaf · **orgs:** WSO2, IBM
- **topics:** enterprise-adoption, governance-compliance, product-ux · **tags:** chief AI officer, AI leadership, AI adoption metrics, AI fluency, agent-ready products, consumption pricing, open source, org design, AI gateway, agent identity

> WSO2's Chief AI Officer Rania Khalaf on running the role as scientist, architect and coach, with adoption-based metrics instead of token counts.

## Summary
Rania Khalaf, Chief AI Officer at WSO2, describes a role that means very different things depending on company type, AI maturity and the person's background. She splits the job into three focus areas (scientist, architect, coach) and says each has a range that depends on the company. Coaching, both inward to employees and outward to customers, was the part she underestimated. She describes her own career path from IBM Research to an agriculture biotech and then WSO2, and the sliders she uses to place each job. She argues against measuring token usage, which she calls easy to game, and lists the metrics she uses now: workforce AI fluency, builders across functions, depth of adoption, tool availability and whether LLMs can find the company. On the product side she says every WSO2 product must be consumable by agents (LLM-readable docs, MCP server, skills, CLI) and that pricing has moved to consumption. The talk is mostly role experience and leadership perspective, with few technical details.

## Key ideas
- **The Chief AI Officer role means different things by company type, AI maturity and the holder's background** — The speaker says the role varies on these axes and is often shaped around a specific person. Some companies hire for a specific need, and others create the role around a candidate's skills. She has been in the role nearly two years and in a variant of it for about five. ([0:08](https://youtu.be/9cJrbj23fOA?t=8))
- **Split the role into scientist, architect and coach, each with its own range** — Scientist means exploring and experimenting. Architect means building plus strategy and board reporting. Coach means evangelizing and educating. Each area's weight depends on the company: a steward type may need little AI depth, while a strategy type needs to shape the whole company. ([3:00](https://youtu.be/9cJrbj23fOA?t=180))
- **Coaching takes more time than expected, both inward and outward** — She says she forgot how much time evangelizing, educating and over-communicating takes. Inside a non-software company, coaching focuses on teams learning things like hallucination by experiencing them. Outside, it means advising customers without pitching products first. ([4:18](https://youtu.be/9cJrbj23fOA?t=258))
- **Do not measure tokens; measure fluency, builders, adoption depth and visibility** — She rejects token counts because they are easy to game. Her current list covers workforce AI fluency (not just a center of excellence), builders across functions, adoption depth (simple tasks up to changed workflows and agent teammates), tool subscriptions and reimbursement, and whether LLMs can find the company. She says the list should change as maturity grows, because whatever you measure is what people optimize for. ([12:11](https://youtu.be/9cJrbj23fOA?t=731))
- **Use the simplest method that works; do not reach for ML by default** — For a gene-editing team that needed corn embryo size measured cheaply, she used basic blob detection and no machine learning. A BERT-based approach was used only for the gene discovery problem. ([10:54](https://youtu.be/9cJrbj23fOA?t=654))
- **Make every product agent-consumable and move pricing away from seats** — She says each product needs LLM-readable docs, an MCP server, skills and a CLI. Pricing is consumption-based because per-seat pricing breaks when agents do the work. ([14:29](https://youtu.be/9cJrbj23fOA?t=869))
- **Expect to need strong CEO backing, and the role may be merged or moved** — She says the role needs close work with many parts of the company, so it needs strong CEO support. She has seen the chief AI officer combined with the chief product officer, and in one case the head of HR took on AI leadership, which she is unsure about. ([19:35](https://youtu.be/9cJrbj23fOA?t=1175))

## Techniques
- **Three-dimension role mapping** — Place the role on three axes: whether the company sells software, whether the workforce is mostly technical, and the company's AI maturity. Then set the weight of scientist, architect and coach from those answers. *When:* When defining or hiring for an AI leadership role in a company with an unclear mandate.
- **LLM-assisted role analysis** — The speaker fed resumes and job postings for the role into Claude and Gemini, matched them to the slider dimensions, and checked which areas came out. *When:* When a role is new and fuzzy, and you want evidence from many real examples rather than a guess.
- **Adoption depth ladder** — Rank AI use from simple tasks (cleaning an email, code completion) to changed workflows to agents that work alongside a team, and track each team's position. *When:* When reporting AI adoption to a board and tokens or seat counts would mislead.
- **Agent-ready product checklist** — Give each product LLM-readable docs, an MCP server, skills and a CLI, so agents can use it directly. *When:* When products will be called by agents and not only by people.
- **Dogfooding with a closed feedback loop** — Make internal teams use the company's own products and act on their complaints and suggestions. *When:* When internal use is mandated and you want the product to improve from it.

## Numbers
- IBM study figures cited as 11% (2024), 26% (2025) and 76% (latest). The talk does not say what these percentages measure. ([1:38](https://youtu.be/9cJrbj23fOA?t=98))
- At WSO2 her time split is about 20% scientist, 60% architect and 20% coach. ([9:54](https://youtu.be/9cJrbj23fOA?t=594))
- The company is about 75% technical people. ([9:54](https://youtu.be/9cJrbj23fOA?t=594))
- A gene-editing validation cycle took about 10 years of experiments and a large amount of land at her previous biotech employer. ([8:30](https://youtu.be/9cJrbj23fOA?t=510))
- WSO2 is about 20 years old, has about 150 million ARR, and its software is used in over 90 countries on six continents. ([17:16](https://youtu.be/9cJrbj23fOA?t=1036))
- The research group had three publications this year; two were with undergraduates in Sri Lanka and one of those won a best paper award. ([18:15](https://youtu.be/9cJrbj23fOA?t=1095))

## Hot takes
- Measuring tokens is easy to hack and should not be the main AI metric.
- A Chief AI Officer can be a steward who understands the business without deep AI knowledge.
- The web is becoming hard for humans to read because it is now written for LLM readers.
- Per-seat SaaS pricing will break as agents do more of the work, so consumption pricing is needed.
- The role may end up combined with the chief product officer, or even held by the head of HR.

## Tools mentioned
Claude, Gemini, BERT, MCP, Databricks

## Relevance to our work
- **agentos** (1/3): The speaker's adoption-depth ladder and warning against token metrics could shape how AgentOS reports usage, but she gives no technical detail. → *Report AgentOS usage by adoption depth (simple task, workflow change, agent) and not only by token counts.*
- **general** (1/3): The talk gives a usable set of AI-adoption metrics and a point about making products agent-consumable, which applies to any team setting AI KPIs. → *Turn this talk's metric list (fluency, builders across functions, adoption depth, tool availability, LLM visibility) into a draft AI-adoption scorecard for the team.*
