# Agents in Orbit: Workflows, Not Autopilot — Eduardo Simon & Javier Casal, Flywire

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `rAUyRDOFyHU` · [watch](https://youtu.be/rAUyRDOFyHU) · **date:** 2026-10-13 · **length:** 18:53 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Eduardo Simon, Javier Casal · **orgs:** Flywire
- **topics:** enterprise-adoption, agent-architecture, evals, sandboxing-execution · **tags:** workflows, deterministic-code, YAML, code-review-bot, guardrails, isolated-step-eval, golden-dataset, skills-marketplace, fargate, lambda-microvm, claude-agents-sdk, fintech, PCI

> Flywire's engineers describe Orbit, an internal platform that runs deterministic code with small LLM steps, gated by YAML definitions, per-step permissions and human-reviewed merge requests.

## Summary
Eduardo Simon and Javier Casal of Flywire's AI platform team describe Orbit, an internal platform for agentic workflows used by about 400 engineers in a PCI-regulated payments company. Orbit keeps predictable steps as code and calls a model only where reasoning is needed. Each workflow is a YAML file reviewed like any other code, with triggers from webhooks, schedules, the API or CLI. The team runs the Claude Agents SDK as the harness and restricts each LLM step's network, tools, skills and MCP tools. Orbit's runtime moved from Fargate toward Lambda microVMs and the team is working toward full sandboxing. They evaluate single LLM steps in isolation using golden datasets built from OpenTelemetry traces, not full end-to-end benchmarks. They report about 11,000 executions at a 99% success rate over 30 days and say they still keep a human approving every merge request.

## Key ideas
- **Pair deterministic code with small LLM steps** — Orbit turns repetitive procedures into code and calls a model only for reasoning. The speakers contrast this with open-ended agent loops that run freely. ([2:51](https://youtu.be/rAUyRDOFyHU?t=171))
- **Build in-house because frontier models made it cheap** — They chose to build rather than buy. Their argument: fast feature work from frontier models lowers the cost of a custom platform, and keeping execution inside their own infrastructure keeps PCI/PII/PHI data inside their control and avoids long vendor security reviews. ([3:25](https://youtu.be/rAUyRDOFyHU?t=205))
- **Workflows are YAML files that go through merge request review** — Each agent is one YAML file in a repo. The code review example runs a webhook trigger, then deterministic fetch and risk-tier steps, then a read-only LLM step with a strict output schema, then a deterministic step that posts findings. YAML was chosen because engineers and coding agents already read it. ([3:59](https://youtu.be/rAUyRDOFyHU?t=239))
- **Each LLM step gets a declared capability set** — Per step, the YAML restricts the network the agent can reach, the tools it can call, the skills it can load and which MCP tools it can use. A code review step can read and search but cannot edit or push. ([11:18](https://youtu.be/rAUyRDOFyHU?t=678))
- **Start with a skill, promote to a workflow once the task is proven** — A skill is cheap to write and useful immediately. Skills come from one internal marketplace that both engineers' laptop Claude Code and Orbit's build-time runs use. Once a task is worth automating, it moves into a workflow where predictable parts become code. ([11:52](https://youtu.be/rAUyRDOFyHU?t=712))
- **Evaluate isolated LLM steps instead of whole workflows** — Whole-workflow synthetic benchmarks were noisy and costly. The harness injects historical state into one node to measure output quality and regressions. Production traces from OpenTelemetry become golden datasets stored next to the code and run on demand. ([13:34](https://youtu.be/rAUyRDOFyHU?t=814))
- **Guardrails are needed when agents scale in parallel** — Fargate lets Orbit run very many agents at once, so it adds per-agent timeouts, aggressive run limits by default, and control-plane locks that drop duplicate runs of the same task. Without limits, a broken integration could spawn thousands of agents. ([9:05](https://youtu.be/rAUyRDOFyHU?t=545))

## Techniques
- **Deterministic-first workflow with scoped LLM steps** — Write fetch, classify, and post steps as plain code. Call the model only in a step that needs reasoning, and give it read-only or narrow permissions. *When:* Repetitive engineering tasks where most of the flow is predictable, such as code review, dependency fixes, or ticket triage.
- **Strict JSON output schema with targeted retry** — Every LLM step must return JSON matching a schema. If validation fails, the platform retries or falls back before the next step, so control flow never depends on parsing free text. *When:* Any workflow where the model's output decides branching, error handling, or state changes.
- **Per-step capability allowlist declared in config** — Declare the network, tools, skills and MCP tools (down to individual tool names) for each step in the workflow file, and review them in the same MR process as code. *When:* When agents touch real repos or production data and you need an auditable least-privilege boundary per step.
- **Skill first, then workflow** — Prototype the task as a skill in the developer's own CLI. Share skills through one internal plugin marketplace. Promote to a deterministic workflow after the task proves worth automating. *When:* Early in automating a team task, when the workflow shape is not yet clear.
- **Isolated node evaluation with production-trace golden sets** — Trace every activity, model call and tool call with OpenTelemetry. Save selected real executions as golden sets, inject exact historical state into one node, and compare prompt or model changes on that set. *When:* Comparing prompts or models for a single step, or catching regressions cheaply without a full end-to-end benchmark.
- **Per-step model selection** — Each LLM step declares its own model, so planning and implementation can use different models. A model router is planned. *When:* When cost matters and steps differ in difficulty.
- **Separate orchestration, runtime and session state** — Move from one container that holds harness and sandbox to separate orchestration, agent runtime and session state components. The speakers say an error in the agent no longer kills the sandbox and each part scales on its own. *When:* When agent runs are long, parallel, and need resilience to crashes.

## Numbers
- About 400 software engineers across the company; stacks include Java, Ruby, Go, Python, .NET and PHP ([1:06](https://youtu.be/rAUyRDOFyHU?t=66))
- Over 5,000 clients in more than 240 countries ([0:33](https://youtu.be/rAUyRDOFyHU?t=33))
- AI platform team formed about 6 months earlier, in April; close to 1,000 commits since then ([1:43](https://youtu.be/rAUyRDOFyHU?t=103))
- Claude Code published more than 160 releases in six months, and labs released more than 20 new models ([2:17](https://youtu.be/rAUyRDOFyHU?t=137))
- Code review agent: over 9,700 runs in 30 days, averaging under 3 minutes per merge request ([15:50](https://youtu.be/rAUyRDOFyHU?t=950))
- Audit fixer opened 159 MRs for vulnerable dependencies; Victoria linter fixer fixed 413 projects; merge conflict resolver ran 921 times ([15:50](https://youtu.be/rAUyRDOFyHU?t=950))
- Over 11,000 executions across workflows in the period with a 99% success rate ([15:50](https://youtu.be/rAUyRDOFyHU?t=950))
- AWS Lambda microVMs were released in June, after Orbit started in April on Fargate only ([10:11](https://youtu.be/rAUyRDOFyHU?t=611))

## Hot takes
- With frontier models, building an in-house agent platform is now cheaper than buying one, even in a regulated financial company.
- Most of an agent workflow should be plain code. The model should only be called where reasoning is needed.
- Start with a skill, not a workflow. Promote a task to an automated workflow only after it has been proven by hand.

## Tools mentioned
Claude Agents SDK, Claude Code, AWS ECS Fargate, AWS Lambda microVMs, GitLab, Jira, Sentry, Slack, OpenTelemetry, MCP, YAML, Victoria (internal PaaS)

## Relevance to our work
- **agentos** (2/3): Per-step capability allowlists and deterministic-first LLM steps map onto AgentOS's manifest-driven pillars and its proxy-level controls. → *Add a per-step allowlist (network, tools, skills, MCP tools) to the AgentOS manifest and check whether the proxy can enforce it per call.*
- **prosharness** (2/3): ProsHarness wraps Claude Code for long runs. This talk shows per-step tool restrictions, resumable runs and a skill-to-workflow promotion path that relate to its checkpoint and plan-critique loop. → *Declare allowed tools and skills per phase (plan, critique, implement) in the ProsHarness config and test whether the checkpoint can resume a phase that was cut short.*
- **general** (2/3): Isolated per-step evaluation with golden sets from traces, plus strict JSON schema with retry, applies to cheap-model pipelines like the Haiku ones. → *Pick one Haiku pipeline step, store 20 to 30 real input and output traces as a golden set, and compare prompt or model changes on that step alone.*
