# Warp Code Tutorial: Save 90% of Time with Warp AI Agents (vs Claude Code) Agentic Development

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `STd07QswCpk` · [watch](https://youtu.be/STd07QswCpk) · **date:** 2025-11-02 · **length:** 10:08 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** AI LABS host (unnamed) · **orgs:** Warp, OpenAI
- **topics:** coding-agents, context-engineering, multi-agent, mcp-and-tools · **tags:** warp, agentic-development-environment, parallel-agents, prd-planning, saved-prompts, workflows, rules, mcp, context7, playwright-mcp, task-list, diff-review, zod, express-validator, sponsored

> Sponsored walkthrough of building a full-stack notes app with Warp's agentic development environment, covering PRD planning, parallel agents split by API contract, saved prompts and rules, and MCP context.

## Summary
The host argues that AI coding is mostly about filling the context window with the right information at the right time, and uses Warp's new agentic development environment (ADE) as the vehicle. The video is a sponsored partnership: the host opens with unverified benchmark claims (75.8% on SWE-bench, first on Terminal Bench) and closes with a $5 Warp Pro promo. The method is a sequence of principles: write a detailed PRD first (brainstormed with ChatGPT), generate the API contracts, then fan out separate agents for backend, frontend and authentication. Reusable context lives in saved prompts, Warp Drive rules, MCP servers (Context7 and Playwright), starter workflows and notebooks. Agents keep a to-do list because context windows shrink, and rules tell them to fetch current library docs via Context7 before installing. The demo runs the agents in parallel tabs, reviews their diffs, adds auth, validates with Express Validator and Zod, and tests the signup, notes, AI summary and voice-note features. The video shows the workflow but never measures the "save 90% of time" claim from its title.

## Key ideas
- **Context, not prompts, is the core skill: fill the context window with the right information at the right time.** — The host frames the whole video around this claim and presents the workflow principles as ways to manage context. ([0:00](https://youtu.be/STd07QswCpk?t=0))
- **Plan first with a detailed PRD that lists every feature before any agent writes code.** — The host brainstorms the idea with ChatGPT, then produces a PRD. The demo app has three log-entry modes: manual notes, AI summary of an uploaded document, and voice-note transcription. ([1:02](https://youtu.be/STd07QswCpk?t=62))
- **Split work across parallel agents by component, and generate the API contract first so the agents can work independently.** — The host generates all APIs from the PRD, then one agent builds the backend and another the frontend against those APIs. An auth agent follows once both are ready. The host says this keeps any single agent from being overloaded with context. ([2:16](https://youtu.be/STd07QswCpk?t=136))
- **Save prompts, rules, MCP servers, workflows and notebooks so context is reusable rather than retyped.** — Warp Drive holds the MCP servers, rules (for example, keep dependencies mutually compatible), starter prompts, templated workflows (for example, Next.js init), and notebooks, which are markdown docs fed to the agent as needed. ([3:28](https://youtu.be/STd07QswCpk?t=208))
- **Give agents an explicit task list because their context windows shrink over time.** — The host says that without a clear outline the agent works from a degraded context and starts to hallucinate. Warp's built-in to-do list makes the agent work through tasks one by one. ([4:30](https://youtu.be/STd07QswCpk?t=270))
- **Use MCP for external, current context and rules for project-specific behavior.** — The host has a rule that tells the agent to use Context7 whenever it installs a library or framework, so it fetches the latest compatible version and docs from the source. The host says models have training cutoffs, which is why external lookups matter. ([5:50](https://youtu.be/STd07QswCpk?t=350))
- **Run agents in parallel tabs, watch the completion signals, then review and edit their diffs.** — The host runs frontend and backend in separate tabs, uses Warp's management panel and red-dot and toast notifications to track completion, and reviews the changes. The host calls the tool an ADE because the user can edit the agent's code in the same view. ([6:43](https://youtu.be/STd07QswCpk?t=403))
- **Add validation as a separate step after the components exist: Express Validator on the backend, Zod on the frontend.** — The host then tests signup and sign-in, which the validation enforces, followed by the notes, AI summary, document summary and voice-note features. No automated tests or evals are shown. ([7:45](https://youtu.be/STd07QswCpk?t=465))

## Techniques
- **PRD-first, then API contract, then fan out** — Brainstorm the app (the host uses ChatGPT), write a PRD that lists every feature, generate the API endpoints from the PRD, then give separate agents one component each (backend, frontend), with the auth agent starting after the first two are done. *When:* Multi-component full-stack builds where agents need a shared interface to work in parallel without stepping on each other.
- **Saved prompts as reusable commands** — Store frequently used prompts in Warp Drive, then recall them with a backslash or the slash command and run them in a new tab. *When:* Repeating the same kind of task (for example, backend setup or auth) across sessions or team members.
- **Templated workflows for known-hard setup steps** — Create a Warp workflow that encodes the correct command sequence for a task the agent gets wrong (the host cites Next.js project init, which took four attempts because of naming conventions). *When:* Setup steps that agents repeatedly get wrong, such as scaffolding with fixed naming conventions.
- **Rules to pin dependency and library behavior** — Add a standing rule such as: ensure all installed dependencies are compatible with each other; always use the Context7 MCP when installing any library or framework. *When:* Projects where the agent must avoid stale library versions or version conflicts.
- **Notebooks as context documents** — Write an extended README or markdown doc for the project and attach it so the agent can read it when needed. *When:* Project-specific background that is too long for a prompt but needed in some tasks.
- **Explicit task list for long runs** — Let the agent write a to-do list for the whole task so it works through items in order. *When:* Multi-step tasks in which the agent's context is likely to grow long or degrade.
- **Parallel agent tabs with completion monitoring** — Run each agent in its own tab, watch the management panel and the completion indicators, then review each agent's diff and edit code directly before saving. *When:* Independent work streams where you want to supervise several agents at once.

## Numbers
- Warp's agent is claimed to score 75.8% on SWE-bench and rank #1 on Terminal Bench. Vendor-stated and unverified in the video. ([0:00](https://youtu.be/STd07QswCpk?t=0))
- A Next.js project setup used to take about four agent attempts because of naming-convention mistakes. The host's own anecdote, not a measurement. ([4:30](https://youtu.be/STd07QswCpk?t=270))
- Warp Pro promo at $5 for one week. Sponsor offer. ([8:55](https://youtu.be/STd07QswCpk?t=535))
- Video title says 'Save 90% of Time' versus Claude Code; the video does not measure or compare time or cost. ([0:00](https://youtu.be/STd07QswCpk?t=0))

## Hot takes
- Sponsored: the host says they partnered with Warp, and the video ends with a $5 Warp Pro promo, so the praise and benchmarks should be weighed as vendor claims.
- The title's 'Save 90% of Time' versus Claude Code is never measured or compared in the video; the only comparison is the host's general impression.
- The SWE-bench and Terminal Bench figures are stated by the presenter without a source or methodology.
- The principles (PRD, parallel agents by API contract, saved prompts, rules, MCP, task lists, validation) are generic and apply to any agent tool. The Warp-specific part is the UI for saved prompts, notifications and diff review.
- No automated tests, evals or verification of agent output are shown; the host checks the result by manually signing up and using the app.

## Tools mentioned
Warp (agentic development environment and terminal, with a built-in AI agent), Warp Drive (saved prompts, rules, MCP servers, workflows, notebooks), Context7 MCP, Playwright MCP, ChatGPT, Express Validator, Zod, Next.js, SWE-bench (vendor claim: 75.8%), Terminal Bench (vendor claim: #1)

## Relevance to our work
- **prosharness** (1/3): Shares the plan-then-parallelize pattern (PRD and API contract before fan-out) and rules/MCP for context, but the video does not offer a harness design. → *When ProsHarness fans out Claude Code subtasks, have the plan step emit a shared interface or API contract that each subagent receives, and compare with the parallel-agent approach shown here.*
