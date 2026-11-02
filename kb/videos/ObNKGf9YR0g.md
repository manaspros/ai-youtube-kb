# Rewiring the State — Eoin Mulgrew, No. 10 (Downing Street)

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ObNKGf9YR0g` · [watch](https://youtu.be/ObNKGf9YR0g) · **date:** 2026-06-18 · **length:** 28:18 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Eoin Mulgrew · **orgs:** No. 10 Downing Street, 10DS (No. 10 data science team), UK Government, AI Safety Institute, Incubator for AI (DSIT), Justice AI (MOJ), Google DeepMind, Tony Blair Institute, Cabinet Office
- **topics:** enterprise-adoption, governance-compliance, product-ux, evals · **tags:** government, forward-deployed-engineers, insurgency-team, policy-simulation, red-teaming, sycophancy, xtract, ai-tutors, recruitment, public-sector

> Eoin Mulgrew of No. 10's data science team describes an outsider "insurgency" unit with forward-deployed engineers that ships small government AI tools in weeks; mostly a recruitment pitch.

## Summary
Eoin Mulgrew, who runs cross-government transformation work for the data science team (10DS) at No. 10 Downing Street, explains why the team was set up as a small central "insurgency" unit with a ministerial mandate, market-rate pay, high autonomy and an unusually hard technical hiring process that recruits only outsiders. The team embeds forward-deployed engineers with policy, legal, comms and polling staff, and reports ideas going from problem to live tool in about two weeks. Examples include a policy simulator for universal credit, a statute-book analysis tool that replaced a planned £1.5M consultancy job, and a delivery red-teaming tool for ministerial reports. He then covers partner work: red-teaming for the AI Safety Institute, the Incubator for AI's Xtract planning-digitisation tool built with DeepMind on Gemini, AI tutor safety benchmarks, and Justice AI's embedded engineers in prisons. In Q&A he says models are red-teamed for sycophancy before users get them, and that the aim is to turn the central team's exemption into a norm and move to horizontal, cross-government processes. Much of the talk is recruitment, and the technical detail is thin.

## Key ideas
- **A small central team with a ministerial mandate, market-rate pay and high autonomy can get around normal government constraints.** — The team calls this an insurgency model. It can go into departments, pick opportunities opportunistically, and recruit through its own technical process. He presents it as a proof point and a workaround that needs to become normal practice. ([1:07](https://youtu.be/ObNKGf9YR0g?t=67))
- **Recruit only outsiders, using a hard technical selection process.** — Standard civil service recruitment is not built for technical talent. The team's own process has a success rate of about 0.7-0.8%. Outsiders from labs, big tech, research institutes and YC are hired, on the view that they are less likely to leave. ([6:16](https://youtu.be/ObNKGf9YR0g?t=376))
- **Forward-deployed engineers embed with non-technical teams and ship in weeks.** — Engineers sit with policy, legal, comms and polling staff, watch their workflows, co-design fixes, and take ideas to implementation in a couple of weeks. He says most of the low-hanging-fruit work is done in-house. ([9:05](https://youtu.be/ObNKGf9YR0g?t=545))
- **Replace a slow, expensive outside analysis with an internal tool that can be rerun.** — A planned £1.5M external review of the statute book would have been out of date by the time it finished, because laws keep changing. One engineer working with in-house lawyers for a couple of weeks produced a tool that the team can rerun on demand and may open-source. ([11:33](https://youtu.be/ObNKGf9YR0g?t=693))
- **Use an AI red-teaming tool as a second opinion on delivery reports.** — The tool flags likely optimism bias, risks rated amber too often, and mitigations that are unlikely to work. It is used daily by delivery teams and flags issues to decision makers. The talk gives no detail on how it works. ([12:33](https://youtu.be/ObNKGf9YR0g?t=753))
- **Red-team models for sycophancy before users get them, and coach users on the risks.** — In Q&A he says a user could push a policy simulator to agree with a bad idea. The team has not seen this much because it red-teamed the models first. They also train the non-technical teams they work with on these risks. ([21:44](https://youtu.be/ObNKGf9YR0g?t=1304))
- **Scale through horizontal, cross-government processes, not only one-off use cases.** — The next 12-24 months aim at processes such as transcription, call centres and back-office work across a workforce of about 400,000. Fixing the wider system needs strategic intervention and new rules, not only small teams. ([24:19](https://youtu.be/ObNKGf9YR0g?t=1459))

## Techniques
- **Insurgency unit with a mandate** — Set up a small central team with explicit ministerial backing, its own hiring process, flexible pay and freedom to choose projects, and treat it as a pilot to show the rest of the organisation what works. *When:* When a large organisation's rules block fast delivery, and leadership will sponsor a sanctioned exception.
- **Forward-deployed engineers embedded in workflows** — Put engineers inside a team for weeks, watch its actual workflow, co-design the tool with its users, and ship it directly to them. *When:* For fast wins on workflow pain points where users cannot describe their needs well in a spec.
- **Internal tool instead of outsourced one-off analysis** — Build a reusable tool with an embedded domain team, so the analysis can be rerun whenever the inputs change, rather than paying for a single report. *When:* When the source material changes often, such as laws, regulations or delivery reports.
- **Policy simulation sandbox** — Let policy teams model the effect of different decisions (for example universal credit changes on household finances) before they commit, as an input to human analysis rather than a replacement. *When:* When policy choices have measurable effects that can be modelled before they are made.
- **Pre-deployment sycophancy red-teaming and user coaching** — Test models for agreeing with users who push flawed premises before giving them to users, and train those users on the risk. *When:* Any tool where non-experts will steer the model toward a conclusion they want to hear.
- **Benchmark-based guardrails for classroom AI** — Evaluate frontier models against metrics such as student cognitive load, and set guardrails schools can use when choosing products, rather than building competing products. *When:* When a public body needs to set standards for third-party AI products used by vulnerable users.

## Numbers
- 7.25 million people on NHS waiting lists ([1:07](https://youtu.be/ObNKGf9YR0g?t=67))
- About 350,000 court cases in backlog ([1:07](https://youtu.be/ObNKGf9YR0g?t=67))
- Only 1 in 5 planning application decisions made on time ([1:07](https://youtu.be/ObNKGf9YR0g?t=67))
- Tony Blair Institute estimate of a £40bn annual productivity prize from AI in government ([2:29](https://youtu.be/ObNKGf9YR0g?t=149))
- Civil service of about 400,000 people ([2:29](https://youtu.be/ObNKGf9YR0g?t=149))
- Recruitment success rate of about 0.7-0.8% ([6:16](https://youtu.be/ObNKGf9YR0g?t=376))
- Planned £1.5M external legal analysis of the UK statute book replaced by an embedded engineer working for a couple of weeks ([11:33](https://youtu.be/ObNKGf9YR0g?t=693))
- Initial model test used 70 teachers role-playing pupils ([25:54](https://youtu.be/ObNKGf9YR0g?t=1554))
- Two government dashboards published in two months, one on the AI Opportunities Action Plan ([13:00](https://youtu.be/ObNKGf9YR0g?t=780))
- Some ideas go from concept to live use in about two months, against a typical year or more in discovery ([14:01](https://youtu.be/ObNKGf9YR0g?t=841))

## Hot takes
- Government is the most ripe industry for AI-driven disruption over the next few years.
- Recruiting outsiders is more important than the tech itself, because insiders tend to stay in the system.
- A paycheck alone does not keep people through hard problems; the team needs missionaries, not mercenaries.
- A small exempt team can prove a point, but it is a hack around the system and must become business as usual.
- An internal tool that can be rerun is better than a one-off outsourced analysis, even when the outside firm would be paid for it.

## Tools mentioned
Gemini, Inspect (AI Safety Institute evaluation tool), Xtract (planning-application digitisation)

## Relevance to our work
- **general** (1/3): Shows a pattern of embedding engineers in a non-technical team and turning a reusable internal tool into the deliverable, which is useful as a delivery model for agent work. → *Read the FDE and embedded-team delivery model for one team-facing agent tool, and note how it is measured by time to first use.*
