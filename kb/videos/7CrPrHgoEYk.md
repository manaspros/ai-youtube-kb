# What the Best Agents Share — Mardu Swanepoel, Flinn AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `7CrPrHgoEYk` · [watch](https://youtu.be/7CrPrHgoEYk) · **date:** 2026-06-18 · **length:** 10:21 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Mardu Swanepoel · **orgs:** Flinn AI, Cursor, Harvey, Anthropic, Manus, Microsoft
- **topics:** product-ux, coding-agents, context-engineering · **tags:** agent-ux, focus-modes, planning-mode, transparency, human-in-the-loop, personalization, playbooks, memory, reversibility, undo, cursor, claude-cowork, harvey

> Mardu Swanepoel (Flinn AI) on four UX patterns shared by strong agents: focus modes, transparent execution, personalization, and reversibility, illustrated with Cursor, Claude Cowork, Harvey and Manus.

## Summary
The speaker opens with Picasso's "steal" idea: study strong agents closely, then build something better. He picks four patterns he sees in top agents and, for each, covers what it is, why it helps, and how a product uses it. Focus modes narrow the action and input space, which improves output quality and sets user expectations; Cursor's planning and debug modes are the example. Transparent execution shifts the user from delegation to collaboration by showing steps, tool calls, inputs and outputs, which builds trust and lets users stop bad runs early (Claude Cowork and Manus). Personalization aims for speed to understanding, not just speed to outcome, using playbooks, memory and skills (Harvey, Claude). Reversibility limits the cost of mistakes through granular undo, conversation rollback and parallel candidate outputs (Cursor, and Harvey's native Word add-in), which makes users willing to attempt higher-value tasks. The talk is short and conceptual, with no measured results.

## Key ideas
- **Study the best agents closely and build your own version, in the spirit of Picasso's 'steal'** — The speaker frames the talk as taking four strong agents, understanding their patterns deeply, and adapting them to build better agents. ([0:00](https://youtu.be/7CrPrHgoEYk?t=0))
- **Focus modes constrain the action and input space** — A mode such as planning or research limits tools and inputs. This lets engineers tune the system prompt and evals on a smaller space first, and it tells users what the agent is for, which makes unclear do-anything chat UIs easier to use. ([2:05](https://youtu.be/7CrPrHgoEYk?t=125))
- **Cursor's planning mode writes no code and asks questions; its debug mode is hypothesis-driven** — Each mode has its own behavior and user expectations. Debug mode, for example, spins up a debug server and pushes logs to it to test hypotheses. ([3:22](https://youtu.be/7CrPrHgoEYk?t=202))
- **Transparent execution moves users from delegation to collaboration** — Showing what the agent read, assumed, is unsure of, and which tool calls it made with their inputs and outputs builds trust in the result. It also lets users stop a wrong path early and cut waste. ([3:22](https://youtu.be/7CrPrHgoEYk?t=202))
- **Optimize for speed to understanding, not only speed to outcome** — Generating output fast is useless if it does not match how the user would have done the task. Agents need the user's methods, principles and implicit preferences. ([5:59](https://youtu.be/7CrPrHgoEYk?t=359))
- **Personalization comes from playbooks, memory, skills and connectors** — Harvey lets firms encode review playbooks and builds memories from instructions for later sessions. Claude uses skills and connectors to add knowledge. ([5:59](https://youtu.be/7CrPrHgoEYk?t=359))
- **Reversibility binds the cost of mistakes, which makes users bolder** — When the worst case is known and small, users accept higher-value and riskier tasks. The speaker's argument is that this changes ROI for the user. ([7:16](https://youtu.be/7CrPrHgoEYk?t=436))
- **Undo should work at several granularities and let users compare parallel outputs** — Cursor offers line-level accept/reject, file-level accept, rollback to earlier conversation states, and parallel runs of the same input on different models. Harvey's Word add-in uses the native Word API so that changes appear as tracked edits a reviewer would expect. ([8:37](https://youtu.be/7CrPrHgoEYk?t=517))

## Techniques
- **Mode-scoped agent configuration** — Define named modes (for example planning, research, debug). Each mode limits the available tools and inputs, has its own system prompt and eval set, and tells the user what to expect. *When:* When a general-purpose agent gives inconsistent results or users do not know what to ask.
- **Plan-only mode** — In planning mode the agent produces a plan and asks clarifying questions and writes no code until the user approves. *When:* Before risky or large changes, where the user should confirm direction first.
- **Hypothesis-driven debug mode** — The agent states candidate causes, adds instrumentation or a debug server to gather logs, and tests each hypothesis in turn. *When:* When diagnosing bugs or performance problems in code the agent did not write.
- **Visible execution trace** — Show a live to-do or progress list, the next step, the context and skills in use, and each tool call with its inputs and outputs. Also surface what the agent read, assumed and is unsure about. *When:* For multi-step agent runs where trust and early intervention matter.
- **Playbook and memory personalization** — Let users write down their methods (playbooks), save memories from corrections and instructions, and load them into later sessions through skills or connectors. *When:* In expert domains such as legal review, where the agent should follow a firm's own method.
- **Layered undo** — Offer accept/reject per line and per file, rollback to an earlier conversation state, and re-run the same input on several models in parallel so the user can keep one result. *When:* When the agent edits user artifacts and users need low-risk experimentation.
- **Native host integration for review** — Write agent edits through the host application's own API (the speaker cites Word) so they appear as the reviewer's normal tracked changes. *When:* When the agent works inside a document or editor that people already review in.

## Hot takes
- Agents optimize for speed to outcome but should optimize for speed to understanding of the user's implicit preferences.
- Reversibility is a growth lever: bounding the worst case makes users take on bigger tasks.
- Showing the agent's process is what turns delegation into collaboration.

## Tools mentioned
Cursor, Claude Cowork, Claude skills and connectors, Manus, Harvey, Microsoft Word API

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code runs with plan, critique and checkpoint steps. The talk's plan-only mode, step-level transparency and undo map directly onto those features. → *Add a plan-only mode that blocks file writes until the plan is approved, and log every tool call's inputs and outputs as a step list that can be reviewed and rolled back to a checkpoint.*
- **agentos** (1/3): The talk is about UX of agent products. Only the idea of mode-scoped tool lists maps loosely onto a proxy that enforces per-request policy.
