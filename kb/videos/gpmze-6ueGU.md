# We Let Our Financial Planners Write the Agents — Matthew Ragone, Range

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `gpmze-6ueGU` · [watch](https://youtu.be/gpmze-6ueGU) · **date:** 2026-10-13 · **length:** 8:54 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Matthew Ragone · **orgs:** Range
- **topics:** enterprise-adoption, skills-self-improvement, context-engineering, product-ux · **tags:** skills, non-engineers, financial-planning, regulated, human-review, skill-ownership, subject-matter-experts, claude

> A financial planner at Range explains how non-engineers wrote Claude skills that drafts client work, using a five-step method: pick, teach, pack, test, ship.

## Summary
Matthew Ragone, a certified financial planner who leads AI adoption for the planning team at Range, describes how planners without coding skills built the agents they use daily. He starts from chatbot use, which only saved minutes, and moves to agents that draft cash flow and insurance analyses in the background while the planner is with another client. The agent never sends anything; a planner reviews every recommendation before a client sees it. He says two things made this work: the agent must run inside the tools where the work lives, and it must know the firm's specific way of doing the work, which he calls a skill. He gives a five-step build method (pick a repeated workflow you can judge, teach it with narrated real cases, pack it into a skill with pre-start questions and hard limits, test it on 5 to 10 real cases, then ship with an owner and a separate reviewer). Six months in, the company had 24 skills, 17 in planning, and sales, product and marketing started building their own without a mandate. He ends by saying the bottleneck is no longer model capability but who writes down, tests and owns the firm's method.

## Key ideas
- **The real constraint for planners is being in one place at a time, so the win is work that happens while they are on another call.** — Faster typing did not help. Parallel background drafting does. The planner reviews and sends the recommendation later. ([1:09](https://youtu.be/gpmze-6ueGU?t=69))
- **The agent never sends anything to a client; a planner reviews every recommendation.** — Agent output is a first draft only. The human review step is non-negotiable in a regulated business. ([2:15](https://youtu.be/gpmze-6ueGU?t=135))
- **Two conditions made agents useful: they must work inside the tools where the work lives, and they must know how this firm does the work.** — The model already knows general financial planning. The gap is firm-specific: what to look at first, what to always flag, how to phrase a specific recommendation. ([2:50](https://youtu.be/gpmze-6ueGU?t=170))
- **A skill is the firm's way of doing one specific piece of work, written down so an agent can follow it.** — It is not a list of steps. It holds the judgment behind the steps, which is why the people doing the work should build it. ([3:27](https://youtu.be/gpmze-6ueGU?t=207))
- **Narrating your judgment while working through real cases is what turns generic advice into the firm's method.** — Say why you open a file, what you look for, and what would make you stop and ask a question. ([4:37](https://youtu.be/gpmze-6ueGU?t=277))
- **A skill needs two parts beyond steps: questions it must ask or confirm before starting, and limits it never crosses on its own.** — Steps alone produce something that runs unsupervised. Questions and limits make it trustworthy. The main limit is never sending anything to a client. ([5:12](https://youtu.be/gpmze-6ueGU?t=312))
- **Once a skill is shared, it needs an owner who keeps it current and a reviewer who is not the author.** — Processes and tax rules change, so a skill right in March can be wrong by December. The reviewer habit mirrors how planners already review each other's plans. ([6:20](https://youtu.be/gpmze-6ueGU?t=380))
- **Adoption spread without a mandate once subject-matter experts built skills for their own niches.** — Skills got more specific, and sales, product and marketing staff started building their own agents. ([7:27](https://youtu.be/gpmze-6ueGU?t=447))
- **The bottleneck has moved from whether the model can do the task to who writes down the method, tests it, and owns it.** — This is the speaker's stated conclusion. He says there is little field data on it yet. ([8:01](https://youtu.be/gpmze-6ueGU?t=481))

## Techniques
- **Five-step skill build method** — 1) Pick a workflow you do often and can judge quickly, preferably a simpler one with heavy manual work. 2) Teach it with several real past cases, narrating your judgment aloud. 3) Pack it into a skill that lists the questions to ask before starting and the limits it must respect. 4) Run it 5 to 10 times on real cases, fixing edge cases, missed questions and confident errors after each run. 5) Ship with a named owner and a separate reviewer. *When:* When a domain expert without coding skills needs to turn a repeated expert workflow into an agent others can use.
- **Narrated walkthrough as skill source** — Work through real cases start to finish and say out loud why you open each thing, what you look for, and what would make you stop and ask. *When:* To capture tacit expert judgment that the steps alone do not contain.
- **Ask-first and never-do sections in a skill** — Write the questions the agent must ask or confirm before starting, and an explicit list of actions it never takes alone (e.g. sending to a client). *When:* For any agent whose output is reviewed by a human before it has real-world effect, especially in regulated work.
- **Background drafting while the expert is busy** — The agent works where the work lives and drafts the next job for another client while the expert handles a live call; the expert reviews and adjusts the draft afterwards. *When:* When the expert's scarce resource is attention or presence, not typing speed.
- **Owner plus non-author reviewer for shared skills** — Each shared skill has one owner who maintains it and one reviewer, who is a different person from the author, who checks it before others rely on it. *When:* As soon as other people depend on a skill, so it does not stay a personal shortcut.

## Numbers
- 24 skills across the company after six months, 17 of them in planning ([6:53](https://youtu.be/gpmze-6ueGU?t=413))
- Test each skill with 5 to 10 real runs before anyone else uses it ([5:47](https://youtu.be/gpmze-6ueGU?t=347))
- Roughly 15 to 20 or more people depend on a shared skill, which is why the pre-ship testing matters ([6:20](https://youtu.be/gpmze-6ueGU?t=380))

## Hot takes
- The bottleneck is no longer whether a model can draft the work; it is who writes down how the firm does it, who tests it, and who owns it.
- The people who do the work should build the agents, because the judgment that makes a skill good cannot be handed to developers.
- Writing only the steps of a skill produces something that runs on its own; writing the questions and limits is what makes it trustworthy.

## Tools mentioned
Claude

## Relevance to our work
- **agentos** (1/3): SkillForge mines telemetry into governed reusable skills; the owner and non-author reviewer idea is a governance step it does not yet describe. → *Add owner and reviewer fields to SkillForge skill records, and block promotion until a non-author has reviewed the skill and it has passed a set of real runs.*
- **prosharness** (1/3): ProsHarness ranks and loads skills; the ask-first and never-do sections could be a standard skill template that the harness checks before a run. → *Add a required 'questions before starting' and 'never does alone' section to the skill template, and have the harness pause to ask when a listed question has no answer.*
- **general** (1/3): The narrated-walkthrough method is a practical way to capture expert judgment for any agent skill, and it is a cheap, low-risk idea to try. → *Pick one repeated workflow, record a narrated session on two or three real cases, and turn the narration into a skill with an ask-first section.*
