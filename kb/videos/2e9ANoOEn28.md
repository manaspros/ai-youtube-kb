# What if the harness mattered more than the model? - Aditya Bhargava, Etsy

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `2e9ANoOEn28` · [watch](https://youtu.be/2e9ANoOEn28) · **date:** 2026-07-18 · **length:** 32:04 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Aditya Bhargava · **orgs:** Etsy, Agency (agencylang.com)
- **topics:** agent-architecture, security-guardrails, multi-agent, evals · **tags:** harness, agent-loop, human-in-the-loop, interrupts, partial-function-application, react, subagents, self-optimization, pause-resume, tool-schema, agency-language, harnessbench

> Aditya Bhargava (Etsy) argues the agent harness, not the model, drives results, especially for weaker models, and walks through building a coding-agent harness step by step in his language Agency.

## Summary
The speaker argues against the idea that strong models mean the harness can stay simple, and says a good harness can lift weaker or local open models. He cites HarnessBench (106 tasks), where the same model scored between 52.4% and 76.2% depending only on the harness. He says existing frameworks did not give him what he needed, so he built a six-month-old language called Agency aimed at harness primitives. He then builds a median-fixing coding agent over seven steps: plain tools, human interrupts, handlers, partial function application for locked arguments, a ReAct test-feedback loop, subagents as tools, and measured prompt self-optimization. The safety and pause/resume features are the most reusable ideas. Most claims about Agency are unverified by the talk itself, and the talk is partly a pitch for the language.

## Key ideas
- **The harness may matter more than the model** — The speaker says the common belief that strong models let you keep the harness minimal pushes people toward proprietary models. He argues that a better harness can make weaker, locally runnable models perform closer to frontier ones. ([1:02](https://youtu.be/2e9ANoOEn28?t=62))
- **Harness choice alone moves benchmark scores a lot** — Citing HarnessBench (106 tasks), he says the same model under the same evaluation scored 52.4% to 76.2% when only the harness changed. He says the harness effect is larger for weaker models. ([2:31](https://youtu.be/2e9ANoOEn28?t=151))
- **He argues a good harness needs language-level support** — He says existing tools and frameworks did not fit what he wanted, so he built Agency, a TypeScript-like language for agents. The stated design goal is that simple things stay simple and complex things stay possible. ([3:28](https://youtu.be/2e9ANoOEn28?t=208))
- **Any function can be a tool** — In Agency, a plain function is automatically exposed to the model as a tool. Its docstring becomes the tool description and a JSON schema is generated from its signature. The speaker presents this as the minimum harness step. ([9:33](https://youtu.be/2e9ANoOEn28?t=573))
- **Safety comes from interrupts, not from trust in the model** — Destructive or sensitive built-in functions raise an interrupt by default. Without a handler the run stops, and a handler can ask a human to approve. He calls this the step that turns an unsafe tool-using agent into a safe one. ([11:42](https://youtu.be/2e9ANoOEn28?t=702))
- **Partial application keeps the agent autonomous and still bounded** — Binding an argument such as the directory in advance hides it from the model, so the agent only sees the remaining parameter. This removes the need for approvals while limiting where it can read and write. ([15:58](https://youtu.be/2e9ANoOEn28?t=958))
- **A reason-act-observe loop is what makes the agent verify its work** — The coding agent reads the files, runs the tests, reads the failure, edits, and reruns until the tests pass. He presents this ReAct loop as the change that moved the agent from proposing a fix to confirming one. ([17:57](https://youtu.be/2e9ANoOEn28?t=1077))
- **Subagents are ordinary tools that reduce context bloat and tool confusion** — A subagent is just a function with its own system prompt and tool set. He argues that splitting tools across subagents keeps the top-level agent's context and tool choice cleaner, and that parallel subagent calls worked in his demo. ([22:32](https://youtu.be/2e9ANoOEn28?t=1352))
- **Prompt self-optimization replaces guess-and-check with a measured objective** — The speaker marks prompt variables for optimization and sets an objective. The optimizer runs the agent for a baseline (0.2 in his example) and iterates. He presents this as the step from trial and error to systematic improvement. The talk names the optimizer 'JEPA', which may be a caption error. ([25:00](https://youtu.be/2e9ANoOEn28?t=1500))
- **Interrupts can pause and resume execution anywhere, even deep in loops or subagents** — He says a pending interrupt inside a for loop, tool call, or subagent pauses the whole run and returns control. Execution can be serialized and resumed later at the same point without changing the code. He says few languages or frameworks support this. ([29:08](https://youtu.be/2e9ANoOEn28?t=1748))

## Techniques
- **Tools as plain functions with docstrings** — Write ordinary functions, and let the framework derive the JSON tool schema from signature and docstring. The speaker says this removes the separate tool-registration step. *When:* Early in building any agent harness, when moving from a bare model call to tool use.
- **Interrupt plus handler for approvals** — Make destructive or sensitive operations raise an interrupt by default. Attach a handler that prompts a human for approval. A tool with no handler fails loudly instead of acting. *When:* When an agent can read sensitive data or mutate files, and you need a safe default before you automate it.
- **Partial function application for capability scoping** — Pre-bind arguments such as a directory or workspace on a tool before passing it to the model. The model sees only the remaining arguments and cannot change the bound ones. *When:* When you want autonomous tool use without approvals, but the tool must stay inside a fixed boundary.
- **ReAct test-feedback loop** — Let the agent read files, run the test suite, observe failures, edit, and rerun until the tests pass. Keep the loop inside the agent rather than having a human re-prompt each step. *When:* For coding tasks with an automatable check, such as a failing test.
- **Subagents as tools with grouped tool sets** — Wrap each specialist as a function that makes its own LLM call with its own system prompt and tools. Let the top-level agent choose among subagents, not raw tools. Parallel calls are supported. *When:* When one agent has many unrelated tools, or when context is bloating and the agent picks the wrong tool.
- **Objective-driven prompt optimization** — Mark prompt variables as optimizable, define an objective such as test pass rate, record a baseline run, and let the optimizer rewrite the prompts while it measures improvement. *When:* When a prompt is hand-tuned by trial and error and you have a scorable outcome.
- **Serializable pause and resume at interrupts** — Raise an interrupt from anywhere in the run, including inside loops or subagents. Serialize the paused state, return control to a human, then resume at the same point later. *When:* For human approvals that may take hours or days, such as phone-driven approvals or long checkpointed runs.

## Numbers
- HarnessBench: 106 tasks; same model and eval, scores range 52.4% to 76.2% depending only on harness (speaker says more than a 20-point gap) ([2:31](https://youtu.be/2e9ANoOEn28?t=151))
- Speaker's language project Agency is about six months old at the time of the talk ([3:28](https://youtu.be/2e9ANoOEn28?t=208))
- Seven progressive harness examples on one median-fixing coding task; the baseline objective for the self-optimization step is 0.2 ([25:00](https://youtu.be/2e9ANoOEn28?t=1500))
- Talk length 32:04; date 2026-07-18 ([0:01](https://youtu.be/2e9ANoOEn28?t=1))

## Hot takes
- Keeping the harness simple because models are good is 'moving in the wrong direction', because it makes us depend on proprietary models.
- Building a good harness requires language-level support, not just frameworks or libraries.
- For weaker models, the harness matters more than the model.
- Agent safety and agent capability go hand in hand, and the harness is where that balance is set.

## Tools mentioned
Agency (agencylang.com, TypeScript-like agent language, installed via pnpm), HarnessBench (harness benchmark, 106 tasks), Claude Code (cited as an example agent: Opus model plus harness), Built-in Agency log viewer, Built-in Agency standard library (includes Wikipedia search tool)

## Relevance to our work
- **agentos** (2/3): Partial function application (locking arguments so the model cannot change them) and interrupts with approval handlers map onto guardrails and exec-gate design in Crucible. The optimizer baseline-then-measure loop also maps onto EvolveCraft. The talk gives no benchmarks that transfer to AgentOS. → *Prototype locked-argument tool binding in Crucible: the sandbox workspace path is pre-bound server-side, so the model never sees or can change it. Measure whether the exec-gate still blocks writes outside the workspace.*
- **prosharness** (2/3): Serializable pause and resume at interrupts is close to the checkpoint/resume and phone-driven approval features in ProsHarness. The talk offers a design reference, though its implementation is in a different language. → *Read the Agency interrupt and resume design and compare it with ProsHarness checkpoint and approval flow. Check whether an approval can pause a Claude Code run mid-tool-call and resume from the same point.*
