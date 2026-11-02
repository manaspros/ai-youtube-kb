# LLM codegen fails and how to stop 'em — Danilo Campos, PostHog

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `juoNbJiZUi0` · [watch](https://youtu.be/juoNbJiZUi0) · **date:** 2026-05-18 · **length:** 19:18 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Danilo Campos · **orgs:** PostHog
- **topics:** coding-agents, context-engineering, skills-self-improvement, security-guardrails · **tags:** posthog-wizard, model-rot, fresh-docs, model-airplanes, breadcrumbing, stop-hook, self-report, secrets-handling, markdown-skills, claude-agent-sdk, prose-over-code

> Danilo Campos (PostHog) on making an autonomous integration agent reliable: feed fresh docs, use thin "model airplane" example apps, breadcrumb the task, interrogate the agent at each stop, and lock down secrets.

## Summary
Danilo Campos from PostHog describes how the PostHog Wizard, a CLI that uses the Claude Agent SDK to install PostHog into users' projects, avoids the common failure modes of LLM codegen. He groups the failures into model rot (stale training data and invented APIs), weird architecture and odd paths, and unsafe handling of user files. His fixes are to serve fresh markdown docs that the agent picks from a menu, and to maintain thin example apps (model airplanes) that show the correct integration shape. The task is breadcrumbed so the agent first finds valuable files, then lists events without writing code, then implements. At the end of every run a stop hook asks the agent what would have helped, which surfaced missing-tool and wrong-language errors. Secrets are protected by tools that can only check a key exists or write a value, never read the file. He argues the wizard is mostly prose (about 90% markdown), because prose improves as models improve while code depreciates. The talk is short, specific to one product, and gives concrete patterns rather than benchmarks.

## Key ideas
- **Model rot is a real problem: a trained model is a frozen snapshot, so fast-moving APIs come out wrong. Fix it by putting current documentation in context at run time.** — Without fresh docs, the agent invented keys, patterns and APIs. The wizard lets the agent pick relevant docs from a menu of fresh markdown and load them into context, which the speaker says beats RAG for this case given current context window sizes. ([2:17](https://youtu.be/juoNbJiZUi0?t=137))
- **Model airplanes: maintain thin, fake example apps that have the right shape of each integration point, so the agent learns a consistent pattern.** — The apps are not production code. Auth can accept any password, but it looks like auth, so the agent learns where event tracking goes. Being smaller, they also cost fewer tokens. A context service flattens them into one markdown reference inside the skill file that the agent can grep. ([5:11](https://youtu.be/juoNbJiZUi0?t=311))
- **Breadcrumb the agent instead of giving the whole plan up front, to stop it improvising its own path.** — Stages: find files with business value, then list candidate events without writing code, then implement with the docs loaded for the target framework. Telling a coding agent the full plan tends to make it take a shortcut through early steps and polish the last one. ([6:38](https://youtu.be/juoNbJiZUi0?t=398))
- **Ask the agent what would have helped at the end of every run, using a stop hook. It is cheap and finds errors you cannot see from outside.** — The team found a tool named in the instructions that did not exist in the MCP server (hundreds of runs), contradictory directives, and a JavaScript instruction given to a Python project. The speaker treats the agent as a user for research. ([10:10](https://youtu.be/juoNbJiZUi0?t=610))
- **Design tool access so secrets never reach the model or the cloud. Give the agent narrow tools instead of raw file reads.** — An early version read .env files, which put user secrets into inference logs. The fix was tools that only check whether a key exists and write a new value. This is a design choice about which reads are allowed, applied to a tool the user trusts with their machine. ([12:31](https://youtu.be/juoNbJiZUi0?t=751))
- **Prose is where durable value lives. Code depreciates as models change, while good instructions get better when a better model reads them.** — The wizard is about 90% markdown, 8% tools for reading and writing markdown, and the rest harness. The speaker argues against heavy scaffolding that constrains the agent, and for giving it information in a sensible order. ([13:57](https://youtu.be/juoNbJiZUi0?t=837))

## Techniques
- **Agent-selected fresh docs menu** — Publish current, framework-specific docs as markdown. Give the agent a menu it can select from by detected stack and load the chosen files into context. Use this when the library or API changes faster than model training. *When:* Integrating a fast-moving SDK or API where models hallucinate outdated keys or patterns.
- **Model airplane example apps** — Keep thin, non-production example apps in each framework and language with realistic shapes (for example an auth route that accepts anything). Flatten them into one reference file the agent can grep, and point to it from the skill. *When:* You need consistent integration patterns across many project shapes without the token cost of real apps.
- **Breadcrumbed multi-stage prompting** — Split the task into stages that do not reveal the end state. Stage 1 finds valuable code, stage 2 proposes events with no code written, stage 3 implements with the loaded docs. Each stage's output is saved to a file the next stage reads. *When:* Long agent tasks where a fully specified plan causes the agent to take shortcuts or drift.
- **Stop-hook self-interrogation** — Add a stop hook that asks the agent at the end of each run what could have been done better to help it succeed. Log the answers and group them to find missing tools, contradictory instructions and wrong assumptions. *When:* Running many agent runs in production and you need failure signals beyond exit codes.
- **Tool-gated secret access** — Do not let the agent read secret files directly. Provide tools that check whether a key exists and write a value, so the contents never enter model context or logs. *When:* Agents that must edit config or env files on a user's machine.

## Numbers
- About 15,000 people run the wizard each month, and it turns about two hours of integration work into roughly eight minutes. ([0:00](https://youtu.be/juoNbJiZUi0?t=0))
- Two unprompted positive posts about the wizard appeared on Bluesky and Twitter within six hours of the talk's reference point. ([1:13](https://youtu.be/juoNbJiZUi0?t=73))
- The wizard's skill content is about 90% markdown, 8% tools for delivering and processing markdown, and the rest agent harness. ([13:57](https://youtu.be/juoNbJiZUi0?t=837))
- A missing-tool instruction (a tool name that was not in the MCP server) caused hundreds of runs to fail before the stop-hook question surfaced it. ([10:10](https://youtu.be/juoNbJiZUi0?t=610))

## Hot takes
- Code is a depreciating asset, and plain-text prose is where most value now lives.
- Do not over-constrain the agent with scaffolding. Give it information and sequence it well instead.
- Asking the agent what went wrong at the end of each run is cheap and finds errors you cannot see otherwise.
- Using the agent's own run feedback is a form of user research, with the agent as the user.

## Tools mentioned
PostHog Wizard, Claude Agent SDK, Claude Code, Cursor, MCP, PostHog LLM gateway

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI and already has checkpoint/resume and zero-token credential handling. A stop hook that asks each run what blocked it, plus tool-gated secret access, fits its existing design. → *Add a Stop hook to the ProsHarness Claude Code wrapper that asks the run what would have helped and saves the answer to the checkpoint log. Then check for missing-tool and contradictory-directive messages across runs.*
- **agentos** (1/3): Mining agent telemetry for skill-worthiness is an open question in SkillForge. The stop-hook self-report is one more run-level signal, but the talk describes a single product, not a telemetry pipeline. → *Consider logging a post-run agent self-report next to telemetry as a candidate input to SkillForge's success-signal question, and check it against real runs.*
