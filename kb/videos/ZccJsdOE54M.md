# The Cost of Accessibility in AI — Jemima Abu, CAIS

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ZccJsdOE54M` · [watch](https://youtu.be/ZccJsdOE54M) · **date:** 2026-10-15 · **length:** 10:02 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Jemima Abu · **orgs:** CAIS, WebAIM, Chrome
- **topics:** context-engineering, skills-self-improvement, product-ux, testing-verification · **tags:** accessibility, a11y, agent skills, semantic HTML, ARIA, vibe coding, frontend, cost, Figma to code, design system

> Jemima Abu (CAIS) argues accessibility is cheaper when built in from the start with AI agents, backed by a one-off experiment (58% lower cost, one-third the time) using a custom accessibility skill.

## Summary
The talk, titled "The Cost of Accessibility in AI" (the speaker is introduced as Rima in the transcript and signs off as Jemima Abu), argues that inaccessible products waste tokens and time. The speaker ran one unguided Figma-to-code prompt twice: once with no skill and once with a custom accessibility skill. The skill run showed a 58% cost reduction and took about a third of the time, though the speaker explicitly calls this a one-off, uncontrolled experiment and not proof. The core claims are that AI agents absorb the biases of the codebase they work in, that they default to verbose reinvented components instead of native semantic elements, and that accessibility added late causes costly regressive rework, lost customers and legal risk. The recommended approach is to define platform-specific requirements, audit the existing codebase first, use a reusable component or design system, and enforce a mandatory accessibility skill (the speaker cites Chrome's Modern Web Guidance skill, plus a lightweight bare-minimum version for vibe-coding). The minimum checklist is semantic HTML first, ARIA only when needed, keyboard operability for everything a mouse can operate, proper labels, and a self-audit before running code. Manual testing is still required.

## Key ideas
- **Accessibility is cheaper to build in from the start, not added at the end** — The speaker argues that retrofitting accessibility means regressive testing and refactoring, and that inaccessible products lose customers and face legal risk (ADA, cited for the US). ([5:30](https://youtu.be/ZccJsdOE54M?t=330))
- **Agents absorb the codebase's biases** — If a codebase was built with a works-on-my-laptop mindset, an agent working in it will copy that and keep producing inaccessible code. ([3:51](https://youtu.be/ZccJsdOE54M?t=231))
- **Agents default to verbose, reinvented components** — Without guidance an agent builds accordions and modals from scratch rather than using native semantic elements, which means more code, more testing and more features to replicate. ([4:24](https://youtu.be/ZccJsdOE54M?t=264))
- **The one-off experiment: a skill cut cost and time** — Same unguided Figma prompt run with and without the speaker's accessibility skill. The skill run was 58% cheaper and took about a third of the time. The speaker says this is a single uncontrolled run and not empirical proof, but the reasons it was slower without the skill are the useful part. ([1:04](https://youtu.be/ZccJsdOE54M?t=64))
- **Give agents guidance the way you would prepare a child for a first errand** — Agents need explicit skills and prompts so they do not take the wrong path. The speaker uses a Netflix show analogy about giving detailed step-by-step instructions. ([2:44](https://youtu.be/ZccJsdOE54M?t=164))
- **Four-step setup: requirements, audit, reusable components, mandatory skill** — Define platform-specific accessibility requirements, audit and fix the existing code before the agent copies its issues, build on a reusable design system or component library so fixes land in one place, and make an accessibility skill mandatory for any UI or code generation. ([7:38](https://youtu.be/ZccJsdOE54M?t=458))
- **Bare-minimum checklist for a lightweight skill** — Use semantic HTML first and ARIA only when HTML cannot express the behavior. Anything operable by mouse must be operable by keyboard. Elements must be labeled for screen readers. The agent audits against these steps before running the code. Manual testing is still needed. ([8:44](https://youtu.be/ZccJsdOE54M?t=524))

## Techniques
- **Accessibility skill for coding agents** — Write or adopt a skill the agent loads on any UI or code task. The speaker names Chrome's Modern Web Guidance skill, which favors newer native HTML and CSS over custom JavaScript, and a lightweight version with a short checklist. *When:* Any agent-driven UI work, especially vibe coding or small codebases where deep research is not practical.
- **Pre-run self-audit against a checklist** — Have the agent check its own output against semantic HTML, keyboard operability, labels and screen-reader readability before running the code. *When:* As a final gate in every agent UI task, as a cheap first pass before manual testing.
- **Audit the codebase before introducing an agent** — Run automated accessibility tools, or have the agent scan the code, and fix existing issues first so the agent does not copy them as best practice. *When:* Before pointing an agent at an existing codebase.
- **Reusable component library as an accessibility lever** — Fix or build accessible components once in a shared design system so every usage inherits the fix. *When:* Any project where the same UI patterns recur across many files.

## Numbers
- 96% of homepages among the top 1 million websites have some accessibility issue (WebAIM study, cited) ([0:32](https://youtu.be/ZccJsdOE54M?t=32))
- 58% reduction in cost with the accessibility skill versus none, on a single unguided Figma-to-code prompt (speaker says this is a one-off, not empirical proof) ([1:04](https://youtu.be/ZccJsdOE54M?t=64))
- Accessibility-skill run took about one-third of the time of the no-skill run ([1:37](https://youtu.be/ZccJsdOE54M?t=97))

## Hot takes
- Building accessibility in is cheaper than retrofitting it, even when AI writes the code.
- Developers with a works-on-my-laptop mindset will leak that bias into an agent working in their codebase.
- Saying that no users rely on assistive tech is a self-fulfilling prophecy, since those users cannot get in.

## Tools mentioned
Figma, Chrome Modern Web Guidance skill, WebAIM (cited study)

## Relevance to our work
- **prosharness** (1/3): Harness around Claude Code could enforce a mandatory skill gate before UI work, as the speaker recommends. → *Consider adding an accessibility skill to ProsHarness's skill set and running a self-audit step before UI tasks are marked done.*
- **general** (1/3): Practical pattern of a mandatory skill plus a pre-run self-audit for agent-written UI. → *If agents write UI in our projects, add a lightweight accessibility checklist skill.*
