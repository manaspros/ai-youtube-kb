# "Software Fundamentals Matter More Than Ever" — Matt Pocock

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `v4F1gFy-hqg` · [watch](https://youtu.be/v4F1gFy-hqg) · **date:** 2026-05-18 · **length:** 18:26 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Matt Pocock · **orgs:** ?
- **topics:** testing-verification, context-engineering, coding-agents, claude-code · **tags:** software-fundamentals, deep-modules, ubiquitous-language, grill-me, tdd, feedback-loops, design-concept, spec-to-code, claude-code, codebase-architecture

> Matt Pocock argues software fundamentals (deep modules, shared language, TDD, good feedback loops) matter more with AI agents, because bad code is now the most expensive it has been.

## Summary
Matt Pocock, who teaches a course called "Claude Code for Real Engineers," argues that code is not cheap and that software fundamentals matter more in the AI era. He says spec-to-code loops (regenerate from a spec without reading the code) degrade the codebase each pass, which he calls vibe coding by another name. He frames a good codebase as one that is easy to change, using Ousterhout's complexity and the Pragmatic Programmer's entropy ideas. He then walks through failure modes and a skill for each: a "grill me" interview to reach a shared design concept before planning, a ubiquitous-language glossary generated from the code, and TDD in small steps so feedback keeps pace with change. He links testability to architecture, recommends deep modules with simple interfaces that AI can navigate, and suggests the human designs the interfaces while the AI fills in implementations. Skills are referenced in a public GitHub repo, which he says is "Matt Pocock skills" (caption-level detail only).

## Key ideas
- **Code is not cheap; bad code is now the most expensive it has been.** — In a hard-to-change codebase, the agent cannot deliver its potential. Good codebases matter more with AI, so software fundamentals matter more. ([0:00](https://youtu.be/v4F1gFy-hqg?t=0))
- **Spec-to-code regeneration degrades the codebase.** — Speaker's experiment: regenerating code from a spec and re-running the compiler produced worse code on each pass. Ignoring the code and only editing the spec was described as vibe coding by another name. ([1:11](https://youtu.be/v4F1gFy-hqg?t=71))
- **A bad codebase is one that is hard to change; entropy makes it worse with each unplanned change.** — He leans on Ousterhout's definition of complexity (structure that makes a system hard to understand and modify) and the Pragmatic Programmer's software-entropy chapter. Changes made without thinking about system design compound. ([2:13](https://youtu.be/v4F1gFy-hqg?t=133))
- **Alignment failures come from a missing shared design concept, so interview the human before planning.** — Borrowing Brooks' idea of the design concept, he says the human and the AI don't share one. His grill-me skill makes the AI question the user about every branch of the plan until both agree. He says this beats default plan mode, which is eager to produce an artifact. ([4:37](https://youtu.be/v4F1gFy-hqg?t=277))
- **A ubiquitous-language glossary keeps the AI's language aligned with the team's and makes output less verbose.** — From DDD. A generated markdown file of tables lists the codebase's terms. He keeps it open while planning, and reading the model's thinking traces showed it used less verbose language and implemented closer to the plan. ([8:00](https://youtu.be/v4F1gFy-hqg?t=480))
- **Feedback speed sets the speed limit, so take small TDD steps.** — Left alone, the model produces large amounts of code and only then type-checks or tests it (outrunning your headlights). Static types, browser access for frontend work, and automated tests all help, but TDD (failing test, pass it, refactor) forces small steps. ([10:25](https://youtu.be/v4F1gFy-hqg?t=625))
- **Testability and codebase quality are the same property.** — Test decisions (unit size, what to mock, which behaviors to test) are interlinked. Well-structured codebases are easy to test, and better feedback gives the LLM better code. ([11:50](https://youtu.be/v4F1gFy-hqg?t=710))
- **Prefer deep modules with simple interfaces over many shallow modules, and design the interface yourself while delegating the implementation.** — Shallow modules are hard for an agent to explore and navigate. A skill that explores the codebase and wraps related code into deep modules produces testable boundaries. The human designs and reviews interfaces; the AI handles the inside, treated as a grey box. The PRD should name the module and interface changes. ([12:50](https://youtu.be/v4F1gFy-hqg?t=770))

## Techniques
- **Grill-me interview before planning** — Give the agent a short standing instruction: interview me relentlessly about every aspect of this plan until we reach a shared understanding, walking each branch of the design tree and resolving dependencies one decision at a time. Turn the resulting conversation into a PRD, or into issues for small changes. *When:* At the start of any non-trivial feature, before the agent writes a plan or code, to reach a shared design concept with the human.
- **Generated ubiquitous-language glossary** — A skill scans the codebase for domain terminology and writes a markdown file of tables listing the terms. The human reviews and corrects it, then the file is passed to the agent and used in plans, code, and conversation. *When:* When the agent's output is verbose or drifts from domain terms, or planning and implementation diverge from intent.
- **Small-step TDD with feedback loops** — Write a failing test, make it pass, then refactor. Use static types (TypeScript), automated tests, and browser access for frontend work so the agent gets feedback after each small step rather than after a large batch of code. *When:* When the agent produces large unverified diffs, and the feedback loop has to match the size of the change.
- **Codebase architecture improvement skill** — Explore the codebase, find related code that is spread across shallow modules, and wrap it in a deeper module with a small interface. Each module then has a boundary to test at, and the agent can navigate it. *When:* When the codebase is a sprawl of small modules that the agent cannot navigate or test well.
- **Design the interface, delegate the implementation** — The human designs and owns each module's interface and tests at that boundary. The agent implements inside it, and the human verifies from outside. Put module and interface changes in the PRD. *When:* For modules that are not safety- or finance-critical. The speaker says critical code still needs full review.

## Numbers
- Grill-me skill repo has roughly 13,000 GitHub stars, per the speaker's recollection ("something like 13,000"). It went viral. ([5:35](https://youtu.be/v4F1gFy-hqg?t=335))
- Grill-me sessions typically ask about 40 to 60 questions, and sometimes up to 100 before reaching shared understanding. ([5:35](https://youtu.be/v4F1gFy-hqg?t=335))
- Talk length is 18:26. ([0:00](https://youtu.be/v4F1gFy-hqg?t=0))

## Hot takes
- Code is not cheap; bad code is the most expensive it has ever been.
- Spec-to-code, where you edit the spec and regenerate instead of reading the code, is vibe coding under another name and degrades the codebase.
- Plan mode in coding agents is too eager to create an artifact; reaching a shared design concept first is better.
- Testability and codebase quality are the same thing, so improving the codebase improves the agent's feedback loops.
- Whoever designs the strategy must be a human; the AI is a tactical programmer.

## Tools mentioned
Claude Code

## Relevance to our work
- **prosharness** (2/3): ProsHarness has plan, critique and debate stages around Claude Code. The talk's grill-me interview and its claim that plan mode is too eager map directly onto that front end. → *Evaluate adding a grill-me style interview step before ProsHarness's plan stage, and compare its output against the current plan with a small A/B run.*
- **general** (2/3): Matches recurring interests in context engineering and Claude Code workflows. It gives a concrete reason tests and deep modules matter for agent loops. → *Read the speaker's skills repo (Matt Pocock skills on GitHub) and check the grill-me and improve-architecture skills against the team's own CLAUDE.md conventions.*
- **agentos** (1/3): Idea of a shared glossary and deep modules applies to AgentOS layer boundaries, but the talk does not address proxies, infra or serving. → *Try a grill-me session plus a generated glossary on the next AgentOS planning task, and record whether the plan changes.*
