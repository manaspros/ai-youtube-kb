# Spec Kit: Github's NEW tool That FINALLY Fixes AI Coding

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `em3vIT9aUsg` · [watch](https://youtu.be/em3vIT9aUsg) · **date:** 2025-11-02 · **length:** 10:33 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Andres · **orgs:** GitHub, Better Stack, Amazon
- **topics:** context-engineering, coding-agents, testing-verification · **tags:** spec-driven-development, spec-kit, github-copilot, claude-code, gemini-cli, kiro, tdd, task-decomposition, model-choice, vibe-coding

> Walkthrough of GitHub's open-source Spec Kit, a four-phase (specify, plan, tasks, implement) spec-driven workflow for AI coding agents, shown building a small Pokedex app.

## Summary
The host argues that vibe coding fails mainly because prompts leave the model guessing, and that treating a written spec as the source of truth fixes this. He introduces GitHub's Spec Kit, which provides a CLI, templates and steering prompts for agents such as GitHub Copilot, Claude Code and Gemini CLI, and frames it as a follow-on to Amazon's Kiro. Spec Kit runs four gated phases: specify (user journeys and outcomes, producing a spec with acceptance scenarios, edge cases and "needs clarification" blocks), plan (tech stack and constraints, producing a data model, research doc and contracts), tasks (a numbered, testable task list), and implement (the agent works through tasks incrementally while the user reviews each change). He demonstrates it on a Pokemon team builder using Grok Code Fast 1 in Copilot, and the default flow is test-first. The result works, but he notes that model choice matters: a GPT-4.1 run gave a worse result than the Grok run. The video is a single-project demo with no benchmarks.

## Key ideas
- **Vibe coding fails from unclear specification, not only from the model; a written spec should be the source of truth that code is generated and checked against.** — Spec-driven development inverts the usual order: write the spec first, then code. The spec is treated as a living artifact that all stakeholders and AI tools align on. ([0:00](https://youtu.be/em3vIT9aUsg?t=0))
- **Broad prompts leave the model guessing thousands of details, so structured guidance is what improves results.** — Using 'add photo sharing to my app' as the example, the speaker says most guessed details will not match intent. The spec is meant to remove that guesswork. ([1:11](https://youtu.be/em3vIT9aUsg?t=71))
- **Spec Kit splits work into four gated phases, each with a validation checkpoint before the next.** — The phases are specify, plan, tasks and implement. The speaker says the toolkit came from frustration with coding models acting like search engines rather than literal-minded pair programmers. ([2:12](https://youtu.be/em3vIT9aUsg?t=132))
- **The specify phase produces the spec with user stories, acceptance scenarios, edge cases, functional requirements and key entities, and marks unresolved decisions in a 'needs clarification' block.** — The user is expected to resolve the clarification blocks and edit the spec file directly if the direction changes. The speaker says he would be too lazy to write these details himself. ([4:18](https://youtu.be/em3vIT9aUsg?t=258))
- **The plan phase turns the spec into a technical plan that respects the stack the user specifies, and writes a research doc explaining framework choices and alternatives.** — Outputs include a data model (with a Zod schema), a research document with rationales and alternatives, and contracts for object types. The speaker says the agent also raises needs the user did not mention. ([5:44](https://youtu.be/em3vIT9aUsg?t=344))
- **The tasks phase breaks the plan into numbered, testable units that can be run one at a time and reviewed.** — Tasks 1 to 4 covered environment setup. After this, the workflow becomes free-flowing: the user asks the agent to implement specific task numbers and checks progress as it goes. ([6:53](https://youtu.be/em3vIT9aUsg?t=413))
- **Spec Kit defaults to test-driven development: the agent writes tests before implementing features, and this can be changed in the spec or plan.** — The speaker observed this behaviour in the template and suggests changing the spec or plan if a different approach is wanted. ([8:03](https://youtu.be/em3vIT9aUsg?t=483))
- **Model choice still matters even with a structured workflow; the same scaffold gave a weaker result with GPT-4.1 than with Grok Code Fast 1.** — This is one anecdotal comparison from a single project, not a benchmark. The speaker says Spec Kit is designed to work with most coding models. ([9:04](https://youtu.be/em3vIT9aUsg?t=544))

## Techniques
- **Four-phase spec-driven loop** — Run the Spec Kit initialiser in the terminal with a project name and pick the agent (the demo uses GitHub Copilot). Open the generated workspace, which contains a scripts folder and a templates folder; the speaker leaves both unchanged. In the agent, run 'specify' followed by a prose description of the goal, basic features and a simple user journey. Review the generated spec file and edit it if needed. Run 'plan' with the stack and technical constraints. Run 'tasks' to produce the numbered task list. Then ask the agent to implement specific task numbers (e.g. 'implement' followed by task numbers), and review each change before moving on. *When:* Greenfield features or small apps where the requirement is vague and you want a reviewable trail of spec, plan and tasks before code is written.
- **Resolve 'needs clarification' blocks before planning** — After specify, scan the spec for the block the agent adds when it cannot choose a path. Answer it in the spec file yourself, then proceed to plan. *When:* Any time the agent flags an ambiguity; treat it as a gate instead of letting the agent pick a default silently.
- **Put performance guardrails in the plan prompt** — The demo adds an explicit instruction in the plan prompt to debounce the search endpoint so the external API is not overwhelmed, alongside stack choices and other technical requirements. *When:* When you have known non-functional requirements (rate limits, latency, dependency constraints) that the agent would not infer from the spec alone.
- **Track progress through the tasks file** — Each task has a unique number and the agent ticks completed tasks in the file. Execute tasks in order and check the file after each batch. *When:* Long implementation runs where you need an audit trail and the ability to pause and resume.

## Numbers
- Four gated phases: specify, plan, tasks, implement ([2:12](https://youtu.be/em3vIT9aUsg?t=132))
- Tasks 1 to 4 were the environment setup tasks in the demo ([8:03](https://youtu.be/em3vIT9aUsg?t=483))
- Single-project comparison: GPT-4.1 produced a weaker result than Grok Code Fast 1 on the same scaffold. No benchmarks, timing or cost data given. ([9:04](https://youtu.be/em3vIT9aUsg?t=544))
- Video length 10:33 ([0:00](https://youtu.be/em3vIT9aUsg?t=0))

## Hot takes
- Spec-driven development is presented as the future of coding and as a paradigm 'we'll be seeing much more of'. This is opinion; the evidence is one demo app.
- Spec-driven workflows improve steering, but the coding model still makes a large difference (GPT-4.1 vs Grok Code Fast 1). Structure does not fully replace model quality.
- The 'vibe coding' label is used for a workflow that is actually spec-first, so the framing is partly marketing.
- No sponsor segment is visible; the content is a substantive walkthrough, so it does not hit the sales-pitch cap.

## Tools mentioned
Spec Kit (GitHub open-source spec-driven toolkit with CLI, templates and steering prompts), GitHub Copilot (agent used in the demo), Claude Code (referred to as 'CloudCode' in the auto-captions; listed as a supported agent), Gemini CLI (listed as a supported agent), Amazon Kiro (earlier spec-driven framework, mentioned only), Grok Code Fast 1 (base model for the demo; auto-captions say 'grokcodefast1'), GPT-4.1 (comparison model, one run), Zod (schema library used in the generated data model), shadcn/ui (likely; auto-captions say 'Shotzi' for the UI library)

## Relevance to our work
- **agentos** (1/3): The gated spec, plan, tasks and implement artifacts are a clear example of structured intermediate artifacts for coding agents, but AgentOS is an infra project and this is a single-app workflow. → *Compare Spec Kit's numbered tasks file with how our planning flows record intermediate state, and consider whether any of the artifact structure is worth borrowing for agent-written work.*
- **prosharness** (1/3): ProsHarness plans, critiques and checkpoints long Claude Code runs. Spec Kit's plan to numbered tasks with per-task review is a similar gated flow, though this is manual, not automated. → *Look at whether ProsHarness's plan step should write a numbered, resumable task list with a review gate per task, similar to Spec Kit's tasks file.*
