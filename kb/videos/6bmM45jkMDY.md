# You Can't Prompt the Room: The Last Skill AI Won't Replace - Balázs Horváth, VisualLabs

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `6bmM45jkMDY` · [watch](https://youtu.be/6bmM45jkMDY) · **date:** 2026-07-18 · **length:** 15:45 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Balázs Horváth · **orgs:** VisualLabs
- **topics:** product-ux, context-engineering · **tags:** requirements-elicitation, story-mapping, user-stories, value-architecture-design, product-discovery, adoption-metrics, business-analysis, spec-driven-agents

> Balázs Horváth (VisualLabs) argues that deciding what to build, through requirements elicitation, story mapping and value-first design, is now the bottleneck, not writing code.

## Summary
The speaker says that once code is cheap to produce, the scarce skill is finding out what is worth building. He ran an internal agent hackathon with 21 ideas, and most were dropped for lack of data access or no clear business sense. He recommends story mapping: a high-level backbone of user steps, an MVP slice of the first few stories, and the rest in the backlog. Each user story uses the persona/what/need/why format, which he says AI handles well, and comes with acceptance criteria that can seed tests. He suggests answering four questions before building: whose problem it is, what winning looks like, what would make the user refuse it, and whether it changes a decision. He wants these answers kept in a markdown file in the repo so the agent has the context. His warnings are about measuring the wrong things: count repeat use of features rather than time on site, and do not treat a demo or an untested PRD as a delivered feature. The talk is a short, opinionated practitioner pitch with few hard numbers and no benchmarks.

## Key ideas
- **The bottleneck has moved from writing code to deciding what to build.** — Building is now cheap, so the expensive part is getting stakeholders in the room and eliciting the right requirements. He says you can prompt the AI but not the room. ([0:00](https://youtu.be/6bmM45jkMDY?t=0))
- **Most ideas from an agent hackathon should be dropped.** — Of 21 agent ideas at an internal hackathon, 17 were abandoned, either for lack of data access or because they did not make business sense. The four that were kept had a large effect on how the team works. The transcript's wording on the reasons is garbled, so treat the exact reasons as approximate. ([0:59](https://youtu.be/6bmM45jkMDY?t=59))
- **AI tends to return the average answer, so value-first framing is needed.** — Using a model to build what already exists gives the most common result. He uses Henry Ford's 'faster horse' remark to argue for asking what people actually need. ([3:35](https://youtu.be/6bmM45jkMDY?t=215))
- **Story maps give a high-level backbone and a small MVP slice.** — Backbone steps (contacting, triaging, resolving, closing) show the process. The first four stories under the backbone form the MVP (capture intent, classify urgency, draft a grounded answer, log to the system of record), and the rest go to the backlog. ([5:05](https://youtu.be/6bmM45jkMDY?t=305))
- **User stories are a structure AI already recognises.** — Each story has persona, what, need and why, plus acceptance criteria that can be turned into test cases. Stories chained together form a coherent system spec, and he says AI does better with this familiar format. ([6:20](https://youtu.be/6bmM45jkMDY?t=380))
- **Four questions test whether a feature is worth building.** — Whose problem is it, what does winning look like for them, what would make them refuse to use it (platform access, cumbersome UX, data security), and does it change a decision. He stores the answers in a repo markdown file so the agent can read them. ([7:44](https://youtu.be/6bmM45jkMDY?t=464))
- **Work through value, then process, then architecture, then design (VAD).** — Value Architecture Design: define how value is created and what the customer wants, map the current process and the architecture beneath it, then design the system and the process changes it needs. He calls this old product management with new economics. ([10:00](https://youtu.be/6bmM45jkMDY?t=600))
- **Measure repeat use, not time on site, and avoid demo-driven delivery.** — High feature velocity with low adoption is a bad pattern. Frequency of an activity is a better signal than time spent. A demo is not a live system, and a PRD that real users have not tested will probably not reach production. ([11:17](https://youtu.be/6bmM45jkMDY?t=677))
- **Replace shipped-feature counts with a used-more-than-twice metric.** — He suggests dropping 'features shipped last quarter' and counting features that are used more than twice. He also says the smartest people should move closer to customers and be included in what gets built. ([12:42](https://youtu.be/6bmM45jkMDY?t=762))
- **Run a mapping session before building and compare with and without user stories.** — Use a story map, business model canvas or similar to show where value sits before building. He suggests building one use case both ways (with and without user stories) and comparing the results. ([14:08](https://youtu.be/6bmM45jkMDY?t=848))

## Techniques
- **Story map MVP slice** — Lay out the process as a backbone of steps, put user stories under each step, and select the first few stories across the backbone as the MVP. Keep the rest in the backlog. *When:* Before starting an agent or software feature, to scope a first release that covers the whole flow.
- **Persona/what/need/why stories with acceptance criteria as agent input** — Write each story in the persona/what/need/why form, add acceptance criteria, and derive test cases from them. Chain related stories into a spec the agent builds from. *When:* When handing a feature spec to a coding agent, so its output can be checked against explicit criteria.
- **Four-question value check kept in the repo** — Answer whose problem, what winning looks like, what would make the user refuse, and what decision it changes. Save the answers as a markdown file in the repo that the agent reads. *When:* At the start of any new agent feature, to give the agent business context beyond the code.
- **Value-first design order (VAD)** — Define value, then the current process, then the architecture beneath it, then the system design and any process changes. *When:* Before designing a system, to avoid building a generic agent that does not match the real workflow.
- **Usage-frequency success metric** — Track how often each feature is used (for example, more than twice) rather than total time spent or features shipped. *When:* When judging whether an internal tool or agent feature is actually adopted.
- **Paired build comparison** — Build the same use case once with user stories and once without, then compare the results. *When:* To test whether the requirements step is changing the output quality.

## Numbers
- Internal agent hackathon produced about 21 ideas; 17 were abandoned and 4 had a large impact on how the team works now. ([0:59](https://youtu.be/6bmM45jkMDY?t=59))
- Speaker has 13 years of experience bridging business, IT and developers, and worked on large ERP and CRM programmes in the US and UK. ([0:59](https://youtu.be/6bmM45jkMDY?t=59))
- Story map MVP is the first four stories under the backbone. ([5:05](https://youtu.be/6bmM45jkMDY?t=305))
- Suggested usage metric: count features used more than twice, not features shipped or time on site. ([12:42](https://youtu.be/6bmM45jkMDY?t=762))

## Hot takes
- You can prompt your AI but you can't prompt the room, so requirements elicitation is the last skill AI won't replace.
- Counting features shipped per quarter is the wrong KPI and should be dropped.
- A demo is not a live system, and a PRD that real users have not tested will probably not reach production.
- Building has become cheap, so the moat is understanding the business need better than others.

## Tools mentioned
Story mapping, Business model canvas, Value canvas, User story templates with acceptance criteria, Markdown files in the repo as agent context

## Relevance to our work
- **agentos** (1/3): The talk's usage-frequency metric (features used more than twice, not time on site) is a practical framing for the open SkillForge question of what success signal to use for skill-worthiness. → *When designing the SkillForge success signal, test a repeat-use frequency metric (for example, how often a mined skill is reused) against time-based signals, and record which predicts reuse.*
- **prosharness** (1/3): The plan stage in ProsHarness could capture persona, win conditions and decision impact before the agent builds, similar to the talk's four-question check kept in a repo file. → *Add an optional plan-stage template that asks for persona, what winning looks like, rejection reasons and the decision the change affects, and store it as a markdown file the agent reads.*
