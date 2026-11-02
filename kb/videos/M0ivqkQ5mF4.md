# Github Spec Kit FINALLY Fixed AI Coding

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `M0ivqkQ5mF4` · [watch](https://youtu.be/M0ivqkQ5mF4) · **date:** 2025-11-02 · **length:** 8:46 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Unnamed presenter (AI LABS channel) · **orgs:** GitHub, Anthropic, OpenAI, Google
- **topics:** context-engineering, coding-agents, multi-agent, testing-verification · **tags:** spec-driven-development, github-spec-kit, slash-commands, claude-code, parallel-subagents, test-first, feature-branches, chatgpt-requirements

> A walkthrough of GitHub Spec Kit's specify, plan and tasks workflow driving Claude Code on a demo app, with an honest verdict: the spec-first flow works, but tasks run by hand and the UI came out cluttered.

## Summary
The presenter argues that vibe coding fails for the same reasons it would fail for humans, and proposes spec-driven development (SDD): write the exact system specification before any implementation. He walks through GitHub's Spec Kit (which he calls "Specify") used with Claude Code to build a YouTube content management system. The toolkit has three slash commands, specify, plan and tasks, each backed by scripts and templates that create feature branches, numbered feature directories and spec/plan/task files. His main criticism is that the toolkit covers only implementation: requirements and tech-stack research happened in ChatGPT beforehand, and the specify step flags ambiguous areas for the user to answer. The plan step turns the spec into technical details, and tasks splits the plan into 93 tasks, 47 of them parallelizable, with tests written before the implementation phase. Each task had to be triggered by hand, but Claude Code sub-agents ran two tasks in parallel to save time. The resulting app worked end to end, but the layout and UI were cluttered, which he says would need another spec-driven feature to fix. The video is a single-project demo with no benchmarks or comparisons.

## Key ideas
- **Spec-driven development (SDD) as the answer to vibe coding** — Argues vibe coding is flawed because humans would hit the same problems. Fix: write the exact system specification first, treating the user as stakeholder and the agents as devs who must share the same spec. ([0:00](https://youtu.be/M0ivqkQ5mF4?t=0))
- **Spec Kit is split into three phases and covers implementation only** — The slash commands are plan, specify and tasks, mapped to spec, plan and task breakdown. The presenter's main critique is that they do not handle context engineering or research, so requirements have to be written elsewhere first. ([1:06](https://youtu.be/M0ivqkQ5mF4?t=66))
- **The specify step expands requirements and flags its own uncertainty** — It creates a product or feature spec (execution flow, user journey, edge cases) and a feature branch. Where the agent is unsure it inserts a clarification marker and asks the user; in the demo there were four such areas, answered before the spec was finalized. ([2:14](https://youtu.be/M0ivqkQ5mF4?t=134))
- **Scripts own the scaffolding, not the agent** — A create-new-feature script finds the next feature number (001 then 002), creates the git branch and directory, and copies curated templates. Setup is deterministic, so the agent only writes content. ([3:28](https://youtu.be/M0ivqkQ5mF4?t=208))
- **Plan holds technical detail, and the agent does not research the stack** — The spec covers features and UX; the plan covers technical implementation. The presenter again got the tech-stack requirements from ChatGPT because the agent will not structure planning input well by itself. The toolkit targets developers rather than vibe coders. ([5:15](https://youtu.be/M0ivqkQ5mF4?t=315))
- **Tasks are parallel-marked and tests come before code** — The tasks command breaks the plan into 93 tasks in 9 phases, 47 marked parallel. Phase 3.2 writes the tests first, and those tests can run again in CI to guard later changes. ([6:19](https://youtu.be/M0ivqkQ5mF4?t=379))
- **Parallel sub-agents save time, but the flow is manual** — There was no way to run tasks automatically, so each had to be instructed one at a time. Claude Code sub-agents ran tasks 3 and 4 together, which he says cut the wait compared with running them sequentially. ([7:36](https://youtu.be/M0ivqkQ5mF4?t=456))
- **Honest verdict: working functionality, poor UI** — The app's functionality was fully wired up, but the layout was cluttered and not built properly despite following the Notion theme and ShadCN components. He suggests another spec-driven feature pass to fix the UI. ([7:36](https://youtu.be/M0ivqkQ5mF4?t=456))

## Techniques
- **Requirements in a general chat model before spec-kit** — Ask a chat model (he used ChatGPT) for a requirements prompt covering the content types, the workflow and how content is organized. Feed the result to /specify. Do the same for the tech stack before /plan, then adjust the output by hand. *When:* Use when the spec kit's own expansion is too thin, since it does not research or brainstorm on its own. Good for greenfield projects where the domain is new.
- **Run /specify with the requirements and answer the clarification flags** — Run /specify with the requirements text. It creates a product or feature spec on a new git branch, with an execution flow, user journey and edge cases. Flagged ambiguities are marked in the spec; answer them, and the spec is updated. *When:* Use at the start of every feature. For an existing project, run it per feature so each feature gets its own branch and spec.
- **Run /plan after the spec is settled** — Run /plan. A setup script copies the plan template, and the agent generates plan-stage files from the spec and your technical requirements. The plan prompts you to run /tasks next. *When:* Use once the spec is final and the stack is decided, so technical choices are made against a fixed set of features.
- **Run /tasks and write tests before implementation** — /tasks runs a prerequisite check (same branch, plan.md exists), gathers the design docs, and writes tasks.md with numbered tasks, phases and parallel markers. Keep the test-writing phase (3.2 in the demo) before implementation tasks. *When:* Use to turn the plan into units an agent can finish. Tests written up front become the regression suite for later CI runs.
- **Run independent tasks in parallel with sub-agents** — Pick tasks marked parallel that do not touch the same files, then give each one to a Claude Code sub-agent in a separate instruction. In the demo, tasks 3 and 4 ran at the same time. *When:* Use when the task list has many parallel-marked items, such as the 47 of 93 in the demo. Do not use it for tasks that edit shared files.

## Numbers
- Three AI assistants were supported at release: Claude, Gemini and Copilot. ([1:06](https://youtu.be/M0ivqkQ5mF4?t=66))
- Four areas needed user confirmation after the specify step. ([2:14](https://youtu.be/M0ivqkQ5mF4?t=134))
- The tasks step produced 93 tasks in 9 phases, 47 of them parallelizable; only 2 tasks are parallel in the setup phase. ([6:19](https://youtu.be/M0ivqkQ5mF4?t=379))
- Each task had to be started manually; tasks 3 and 4 ran in parallel via sub-agents, and he says one takes about 40 minutes alone while both finished in about 40 minutes together. ([7:36](https://youtu.be/M0ivqkQ5mF4?t=456))

## Hot takes
- Spec Kit only handles implementation, not planning or context engineering; the presenter had to do requirements and tech-stack planning in ChatGPT first.
- The toolkit targets developers, not vibe coders.
- The title says Spec Kit 'FINALLY fixed AI coding', but the video is one demo project with a cluttered UI as the result. It has no benchmarks or comparison against other spec-driven setups.
- Tasks must be triggered manually one at a time, which limits how autonomous the workflow can be.

## Tools mentioned
GitHub Spec Kit ("Specify"), Claude Code, ChatGPT, Gemini (supported assistant), GitHub Copilot (supported assistant), ShadCN UI components, Notion (visual theme followed), git

## Relevance to our work
- **prosharness** (2/3): ProsHarness already plans in a plan → critique → debate sequence and runs loops. The spec → plan → tasks split, with parallel-marked tasks run by sub-agents and a tests-first phase, is a close relative of that pipeline and maps to checkpointing per task. → *Compare ProsHarness's plan step against Spec Kit's spec/plan/tasks artifacts. Try a tasks.md-style file with parallel markers as the checkpoint and resume unit for long Claude Code runs.*
- **agentos** (1/3): Weak link: AgentOS builds infra for agents, and this is a single-project developer workflow. Only the idea of gating implementation behind a written spec and tests is transferable. → *Read GitHub Spec Kit's templates folder to see how the spec and plan templates are structured, as a reference for specs written against AgentOS's own pillars.*
