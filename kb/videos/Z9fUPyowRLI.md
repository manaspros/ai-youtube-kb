# Amazon's NEW AI IDE is Actually Different (in a good way!) – Kiro

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Z9fUPyowRLI` · [watch](https://youtu.be/Z9fUPyowRLI) · **date:** 2025-11-02 · **length:** 10:43 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Amazon, Anthropic
- **topics:** coding-agents, context-engineering, software-factory · **tags:** kiro, spec-driven-development, agent-hooks, ai-ide, vs-code-fork, requirements-design-tasks, steering-docs, preview-pricing

> Walkthrough of Amazon's Kiro, a VS Code fork built around spec-driven development (requirements, design, tasks gated by the human) and event-driven agent hooks saved in the repo.

## Summary
Better Stack demos Kiro, Amazon's VS Code-based AI IDE in preview, on a small product-review feature for a three-product website. The core idea is spec-driven development: a short prompt is turned into a requirements file (user stories with acceptance criteria), then a design doc written after the agent reads the existing router and UI code, then a task list linked back to requirements. The user reviews and edits each stage before the agent executes tasks one by one, ticking them off. The second feature is hooks, which fire an agent prompt on file create, save or delete events; they are generated from a natural-language description and stored as files in the repo so a team can share them. The demo's hook updated the README and API docs on save. The presenter treats the spec workflow as the main differentiator and hooks as the feature he likes most, while noting that the rest (steering docs, MCP, model picker, autopilot) is similar to other AI IDEs. The evidence is one unrigorous single-project demo of a preview product, with pricing presented as tentative.

## Key ideas
- **Kiro is Amazon's VS Code fork whose differentiator is spec-driven development: a vague prompt is converted into written specs before any code is changed.** — Two chat modes: Vibe (prompt goes straight to code changes) and Spec (plan first, then build). The presenter argues the spec step makes the agent's assumptions visible before it edits anything. ([0:00](https://youtu.be/Z9fUPyowRLI?t=0))
- **Stage one turns the prompt into a requirements file of user stories with acceptance criteria, which the human can edit or send back to the agent.** — For the demo prompt (anonymous product reviews, total score, star filter, match existing theme), the agent produced five user stories, including matching the existing app design, plus edge-case criteria the presenter did not ask for. ([1:12](https://youtu.be/Z9fUPyowRLI?t=72))
- **Stage two design doc is written only after the agent reads the existing codebase (routers, web app routes), so the design reflects the real architecture.** — The design doc covers overview, tech stack, data flow, TypeScript interfaces, DB schema, API endpoints, and can include Mermaid diagrams. The presenter checked the stack claims against the project before approving. ([2:22](https://youtu.be/Z9fUPyowRLI?t=142))
- **Stage three is a task list with subtasks, each linked to the requirement it satisfies; the demo plan ran to 12 tasks, including unit tests and error handling the user never asked for.** — Plan size grew from a one-line prompt into requirements, design and tasks. The presenter's point is that the user reviews the plan once, then runs tasks individually or queues them. ([4:27](https://youtu.be/Z9fUPyowRLI?t=267))
- **Specs are meant to stay in sync with code: after manual code edits you can ask the agent to update the spec, or edit the spec and refine the task list.** — The presenter frames this as fixing the usual failure where spec docs go stale after the first implementation. ([5:29](https://youtu.be/Z9fUPyowRLI?t=329))
- **Hooks are event-driven agent automations: an event (file create, save, delete) sends a pre-written prompt to the agent in the background.** — Examples given: on save of a React file, update unit tests or Storybook; on save, update docs. Hooks can also be run manually. ([6:54](https://youtu.be/Z9fUPyowRLI?t=414))
- **Hooks are generated from a natural-language description, then stored as files in the repo, so a team can commit and share them to enforce a checklist.** — The hook editor shows title, description, trigger event, a manual trigger option, the file pattern to watch, and the system prompt, all editable. The presenter's demo hook updated the README and added API endpoint docs after a save. ([7:37](https://youtu.be/Z9fUPyowRLI?t=457))
- **Everything beyond specs and hooks is familiar: steering docs (akin to CLAUDE.md or Cursor rules), MCP servers, context attachments, model selector, and an autopilot toggle that removes the approval gate.** — With autopilot off, the agent asks for approval before each change. The model picker offered Claude Sonnet 3.7 and 4 at the time of the video. ([8:02](https://youtu.be/Z9fUPyowRLI?t=482))

## Techniques
- **Staged spec gate before implementation** — Write a short feature prompt, switch to Spec mode, and have the agent produce requirements.md (user stories plus acceptance criteria). Review and edit it, then have the agent write the design doc after reading the existing router and UI code. Review the design (stack, data flow, types, schema, endpoints), then have it produce the task list with each task tied to requirement IDs. Approve the plan, then run tasks one at a time or queue them. Specs live in a .kiro/specs folder in the repo (transcript shows it as 'kero folder specs'). *When:* Features where the agent's assumptions are costly to unwind, or where a human must sign off on the plan before code changes. The gate happens before any edit, so review is cheap.
- **Spec re-sync after manual edits** — After changing code by hand, ask the agent to update the spec. Or edit requirements or design yourself and regenerate the task list from them. *When:* Long-lived features where specs will otherwise drift from the code.
- **Event-driven hook for doc or test upkeep** — In the hook panel, describe the automation in plain language (e.g. when a file is saved, update its docs). Review the generated title, trigger event (file create, save or delete), file pattern, and system prompt, and edit them as needed. Keep the file in the repo so the team shares the hook. Trigger a test by saving a matching file and check the task list. *When:* Recurring checklist steps that people forget after each code change, such as docs, unit tests or Storybook stories.
- **Steering documents** — Keep markdown guidance files that the agent reads on every request to shape its behavior. Kiro calls these agent steering; the presenter likens them to CLAUDE.md or Cursor .mdc rules. *When:* Stable project conventions you would otherwise repeat in every prompt.

## Numbers
- Free preview tier: 50 interactions per month, including specs, hooks, MCP and steering. ([9:10](https://youtu.be/Z9fUPyowRLI?t=550))
- Future price tiers quoted: $19/month for 1,000 interactions; $39/month for 3,000 interactions. The presenter notes everything is free during preview. ([9:10](https://youtu.be/Z9fUPyowRLI?t=550))
- The demo task plan grew to 12 tasks including subtasks from a one-paragraph prompt about a three-product website. ([4:27](https://youtu.be/Z9fUPyowRLI?t=267))
- Requirements for the demo feature were five user stories, including matching the existing app design. ([1:12](https://youtu.be/Z9fUPyowRLI?t=72))
- Platforms: Mac, Windows and Linux. ([0:00](https://youtu.be/Z9fUPyowRLI?t=0))

## Hot takes
- Spec-driven development is 'only new for AI' because developers wrote specs and design docs manually long before AI; the presenter sees automating that as the value.
- The spec workflow is the unique feature; the hooks feature is the one the presenter says he loves most, because it removes the need to remember follow-up steps.
- Kiro is 'a bit lacking in a few features' compared with other AI IDEs; the presenter notes it does not stream diffs live the way Cursor does.
- The agent added unrequested tests and error-handling tasks, which the presenter treats as thoroughness rather than scope creep.
- Pricing is speculative: the stated tiers are future plans during a free preview.

## Tools mentioned
Kiro, VS Code, Claude (Sonnet 3.7 and 4 model options), Cursor (comparison only), React, TypeScript, tRPC, Mermaid, Storybook, MCP servers, GitHub, Google login, Amazon login

## Relevance to our work
- **prosharness** (2/3): ProsHarness plans, critiques and debates before running. Kiro's stage-gated requirements, design and task files, each approved by a human before the next stage, match that plan-first shape and show what a visible gate looks like. → *Add a checkpointed plan stage to ProsHarness with separate requirements, design and task artifacts that the human approves before any execution; compare with the current plan→critique→debate flow.*
