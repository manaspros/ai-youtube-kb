# I Was Using Claude Skills Wrong... The Ultimate System

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `fHGMA8hLNt8` · [watch](https://youtu.be/fHGMA8hLNt8) · **date:** 2025-12-02 · **length:** 12:57 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Anthropic, Appify
- **topics:** claude-code, skills-self-improvement, context-engineering · **tags:** claude-skills, use-cases, sponsored, brainstorm, claude-desktop, github-actions, docker

> A list of about 21 to 22 use cases for Claude Skills, from coding tasks like tests and CI/CD to business, personal and content workflows. Mostly unmeasured ideas, with a sponsor segment.

## Summary
The host walks through roughly 21 to 22 ways to use Claude Skills, shown in Claude Code and the Claude Desktop app. Coding examples include a documentation skill, a test-writing skill that ends with a test report, an SEO skill that gives before-and-after results, and a CI/CD skill that generates pipeline files. Non-coding examples cover brand and social posts, pitch decks, data visualization, policy Q&A, document generation from templates, financial analysis, research papers, a resume skill backed by a project database, script-writing in a personal style, and personal planners for travel, schedules and meals. The pattern throughout is a folder with instructions plus references, assets, templates and scripts, and often a set of clarifying questions before output. The video gives no measured results, no SKILL.md contents and no working demo code, so the ideas are a brainstorm rather than tested practice. A sponsored segment for Appify sits in the middle.

## Key ideas
- **A skill is a folder that bundles instructions with references, assets and scripts, so Claude specializes for one task.** — The host says you can add as many skills as you like to a codebase, and each can carry its own assets and reference files. The same structure is said to work for non-code tasks. ([0:54](https://youtu.be/fHGMA8hLNt8?t=54))
- **A test-writing skill writes and runs tests from its reference guidelines, then reports results.** — The skill works step by step through bugs and ends with a test report giving pass counts, percentages, found issues and suggested fixes. The report format is the reusable part. ([0:54](https://youtu.be/fHGMA8hLNt8?t=54))
- **Skills can generate deployment and documentation scaffolding for a project.** — The CI/CD example produces pipeline files for testing, building and deploying, plus GitHub Actions, README and setup guides. The documentation example writes comments or READMEs from the codebase. ([2:05](https://youtu.be/fHGMA8hLNt8?t=125))
- **Scripts in a skill can wrap CLI tools with large command sets, such as Docker.** — The skill runs the scripts and gives guidance on the tool's commands. The video does not show any example of this working. ([2:05](https://youtu.be/fHGMA8hLNt8?t=125))
- **Ask clarifying questions first, then generate, for business documents and decks.** — The pitch-deck and document-template examples both gather requirements through questions and then fill a company template or format. Templates live in a folder the skill draws on. ([5:39](https://youtu.be/fHGMA8hLNt8?t=339))
- **A stateful skill keeps a data file updated as events happen, then regenerates outputs from it.** — In the resume example, each new role or project is written into a maintained database, and later ATS-style resumes are generated from that database. The same pattern is suggested for story and timeline tracking. ([8:45](https://youtu.be/fHGMA8hLNt8?t=525))
- **Store personal preferences once in a skill so recurring planning requests stay short.** — Travel, schedule and nutrition planners use saved preferences such as likes, dislikes, allergies and routines. The host presents this as the way to avoid repeating yourself. ([11:25](https://youtu.be/fHGMA8hLNt8?t=685))
- **The speaker presents these as brainstormed ideas, not tested workflows.** — He says they are ways he could think of and invites viewers to suggest more. No before-and-after measurements are shown, apart from the SEO narration. ([2:05](https://youtu.be/fHGMA8hLNt8?t=125))

## Techniques
- **Skill folder with references, assets and scripts** — Put SKILL instructions in a folder with reference docs, template or asset files and helper scripts. Tell the skill when to load each file. The video names references, assets and scripts as the parts of a skill but does not show a file layout. *When:* Repeated, format-heavy tasks where the same guidelines and templates should apply each time, such as test writing, docs, decks or reports.
- **Test-and-report skill** — Have the skill write tests from reference guidelines, run them, and finish with a report that gives pass count, pass percentage, issues found and suggested fixes. *When:* When you want a repeatable verification pass with a standard output that can be read at a glance. The video gives no details on how the pass count is computed.
- **Clarify then generate** — The skill asks a fixed set of questions about the goal, audience or format before it generates anything. Examples given are pitch decks, startup idea validation and document templates. *When:* When inputs vary from request to request and a wrong first draft would be costly.
- **Template-driven document generation** — Keep the company's frequent document templates in a folder. Give the skill references and scripts that select a template, fill it in and format the result. *When:* Recurring business documents where formatting time is the main cost.
- **Stateful skill with a maintained data file** — Keep a structured file, such as a project and experience database, that the skill updates whenever something changes. Generate later outputs such as resumes from the current file, not from memory. *When:* Long-running personal or project records that must stay current across many generated outputs.
- **Saved personal profile for planners** — Write likes, dislikes, constraints, schedule habits and goals into the skill once. Each new request, such as a trip or meal plan, reads these details automatically. *When:* Recurring personal planning where you do not want to restate preferences.

## Numbers
- Speaker advertises 21 use cases at the start, then says 22 at the end. The video has no benchmarks, costs, latencies or adoption figures. ([0:00](https://youtu.be/fHGMA8hLNt8?t=0))
- Speaker says the coding skills will give '10 times your productivity'. This is an unsupported claim with no measurement shown. ([0:54](https://youtu.be/fHGMA8hLNt8?t=54))

## Hot takes
- Sponsored segment for Appify (a scraping marketplace) sits mid-video at 3:33 to 4:31 and is unrelated to Skills; the $1 million challenge is promoted in the same breath.
- The title promises 'The Ultimate System', but no system is shown. Each use case is described in a sentence or two with no SKILL.md, scripts or commands.
- Claims such as '10 times your productivity' and that a website's SEO was 'greatly improved' are asserted, not measured.
- The research-paper example says the skill makes three output formats, but the transcript cuts off mid-sentence at 8:45, so the list of formats is missing.

## Tools mentioned
Claude Code, Claude Desktop app, Claude Skills, Docker, GitHub Actions, npm package (unnamed), Appify (sponsor)

## Relevance to our work
- **agentos** (1/3): SkillForge aims to turn agent telemetry into governed, reusable skills. This video has only generic skill-folder ideas (references, templates, scripts) with no evidence about skill quality or reuse. → *When defining SkillForge's skill format, keep reference docs and scripts as separate files the skill points to, as this video describes. Do not treat the video's claims as evidence for any design choice.*
- **prosharness** (1/3): ProsHarness does skill ranking around Claude Code. The test-and-report pattern gives a concrete output contract for a skill, though the video does not measure whether it works. → *Use the test-report contract (pass count, percentage, remaining issues) as one candidate output shape for a ProsHarness skill-ranking eval, and check it against real runs before relying on it.*
