# Please… Enough with the Sloppy, One-Shot SaaS Replacements — Mahmoud Abdelwahab, Railway

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `oixzVKMAXG0` · [watch](https://youtu.be/oixzVKMAXG0) · **date:** 2026-10-13 · **length:** 13:21 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Mahmoud Abdelwahab · **orgs:** Railway
- **topics:** product-ux, coding-agents, testing-verification, skills-self-improvement · **tags:** internal-tools, optimistic-updates, autosave, undo, url-state, agent-skills, end-to-end-verification, design-engineering, railway, payload-cms, tanstack

> Railway's Mahmoud Abdelwahab on why agent-built internal tools feel broken: agents skip product polish (autosave, optimistic updates, undo, URL state) unless asked, so encode taste in skills, reference existing pages, and force end-to-end verification.

## Summary
The speaker, an engineer at Railway, built an all-in-one internal marketing tool (website content, changelog, blog, email, social posting, media, a mini CRM, task tracking, launch planning, calendar, comments, realtime editing) with coding agents, replacing several SaaS products. He argues the gap between one-shot agent output and software people actually want to use is product polish, which agents rarely add unless told to. He recommends a consistent codebase with solid abstractions so the agent follows existing patterns, and he picks TanStack libraries for web work and Payload for content. He lists UX patterns to request explicitly: autosave with a tab-close guard, optimistic updates with rollback, undo-on-delete via a short delayed commit, archive instead of delete, URL-persisted filters and sort, and infinite scroll. He says telling the agent to copy an existing page as the reference makes results more consistent, though the agent sometimes ignores it. He packages his taste as agent skills (two design-engineering skills plus the Railway skill) and closes by saying a verification loop, where the agent actually runs the feature end to end and fixes failures, made the biggest difference. The talk is short, practitioner-level, and mostly opinion, with few hard numbers.

## Key ideas
- **Agents build working software but not software people enjoy using; the gap is product polish.** — The speaker says the missing piece is the difference between a one-shot result and something you would use daily. Agents rarely add polish like autosave, optimistic updates or undo unless asked. ([0:00](https://youtu.be/oixzVKMAXG0?t=0))
- **A consistent codebase with strong abstractions matters more than the exact stack.** — With solid abstractions the agent reuses existing patterns instead of inventing new ones each time, so results stay consistent. He says framework choice matters less once the structure is sound. ([2:16](https://youtu.be/oixzVKMAXG0?t=136))
- **Ask the agent for the invisible UX patterns by name.** — Autosave in the background, a tab-close guard for unsaved changes, and real-time collaboration all need an explicit request. He says the agent handled real-time collaboration well once asked. ([4:37](https://youtu.be/oixzVKMAXG0?t=277))
- **Optimistic updates and delayed undo make the app feel instant.** — Show the success state at once, sync in the background, and roll back on failure. For deletes, remove the item immediately and commit only after a few seconds, with an undo window. He recommends archive-and-unarchive in place of hard delete. ([6:18](https://youtu.be/oixzVKMAXG0?t=378))
- **Persist list state in the URL and use infinite scroll.** — Filters and sort kept in the URL let a teammate open the exact same view. Infinite scroll replaces load-more and next-page buttons. These are small details agents skip, but they matter for daily use. ([8:30](https://youtu.be/oixzVKMAXG0?t=510))
- **Point the agent at an existing page as the reference.** — Define what good looks like once, in one page covering UI, data fetching and structure, then ask new features to match it. This keeps lists of records consistent, though the agent sometimes ignores the reference. ([9:38](https://youtu.be/oixzVKMAXG0?t=578))
- **Package your taste as agent skills and make verification the final step.** — He uses two design-engineering skills (typography, layout, error messages, animation) and a Railway platform skill. The most important step is a verification loop in which the agent runs the feature end to end, sees failures and iterates. Passing build and tests alone was not enough. ([11:53](https://youtu.be/oixzVKMAXG0?t=713))

## Techniques
- **Pattern-following via existing abstractions** — Give the agent a codebase with clear abstractions and tell it to reuse existing patterns instead of creating new ones for each feature. *When:* Any multi-feature app built with agents, so output stays consistent across features.
- **Named UX patterns as explicit asks** — Request autosave with a non-blocking save, a beforeunload guard for unsaved changes, optimistic updates with rollback, delayed-commit undo for deletes, archive instead of delete, URL-persisted filter/sort state, and infinite scroll. *When:* When building any tool people use daily. Agents do not add these unless the prompt names them.
- **Reference-page anchoring** — Tell the agent to use an existing page as the reference for UI, data fetching and structure. Call out the page explicitly in each new-feature prompt. *When:* Adding lists or CRUD views that should match the rest of the app.
- **Taste packaged as skills** — Put design rules (typography, layout, error messages, animation) and platform know-how (deploy, buckets, databases) into agent skills the agent loads for each build. *When:* When you have repeated opinions that you keep restating in prompts.
- **End-to-end verification loop** — After build and tests pass, tell the agent to run the infrastructure and exercise the feature end to end, then fix what fails and repeat. He used computer-use style checks. *When:* Before accepting any agent-built feature as done, since green builds and tests missed broken UX.

## Numbers
- Real-time collaboration took about 700 million tokens of agent work, with the agent's reasoning and review cycles included. ([5:46](https://youtu.be/oixzVKMAXG0?t=346))
- Speaker says the agent-building breakthrough came with the GPT-6 release and that computer use became reliable enough for verification; he gives no benchmark. ([0:33](https://youtu.be/oixzVKMAXG0?t=33))

## Hot takes
- SaaS is not dead yet: the gap between a one-shot agent build and software people love is what matters, and most of that gap is polish.
- Agents will not add product polish like autosave, optimistic updates or undo unless you name them.
- A green build and passing tests are not proof a feature works; agents need to run the feature end to end.

## Tools mentioned
Railway, Payload CMS, TanStack, Claude Code

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code with checkpoint and resume, and the talk's core finding is that agents need a verification loop after build and test to avoid broken UX. → *Add a verification stage to ProsHarness after the test pass that runs the feature end to end and loops on failures, with a skill that records the team's UX checklist.*
- **general** (2/3): Concrete, reusable checklist for agent-built internal tools: named UX patterns, anchored reference pages, skill-packaged taste, and verification loops. → *Turn the talk's UX list (autosave, optimistic updates, undo, URL state, infinite scroll) into a reusable agent skill and check new features against it.*
- **agentos** (1/3): Points to skills and end-to-end verification as the practices that make agent output reliable, but the talk concerns product UX, not infra. → *Add an end-to-end verification step to the AgentOS dev loop: the agent runs a feature against the live stack before it reports done.*
