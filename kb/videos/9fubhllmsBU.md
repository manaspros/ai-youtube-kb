# Field Guide to Fable — Thariq Shihipar, Anthropic

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `9fubhllmsBU` · [watch](https://youtu.be/9fubhllmsBU) · **date:** 2026-07-18 · **length:** 19:28 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Thariq Shihipar · **orgs:** Anthropic
- **topics:** claude-code, coding-agents, context-engineering, models-research · **tags:** Fable, Claude Code, capability overhang, unknown unknowns, system prompt, AskUserQuestion, HTML reports, blind spot pass, agentic coding, trade-offs

> Anthropic's Thariq Shihipar gives a practical field guide to working with the Fable model: unhobble Claude with tools, find your unknowns, stay in the loop, and be less reasonable about trade-offs.

## Summary
Thariq Shihipar (Anthropic, Claude Code) presents a four-part field guide to the new Fable model class: unhobbling Claude, finding your unknowns, dealing with the loss of hand-coding, and being unreasonable about trade-offs. He argues capability is spiky, so tool access (code execution, Bash) unlocks abilities the model already has but cannot recall directly. He says the system prompt should shrink for newer models, with context preferred over "do not" constraints and examples that may limit the model's imagination. He describes the map-versus-territory gap: anything the prompt does not specify becomes a decision point the model must resolve. He offers concrete ways to surface those unknowns (blind-spot passes, brainstorm prototypes, interview mode, reference artifacts, implementation-note logs, and quizzes). The talk ends with a reflection on the gain and loss of agentic coding and a call to treat trade-offs as something to test rather than accept. Most of the content is anecdotal and Anthropic-product flavoured, with few measured results.

## Key ideas
- **Capability overhang: models are spiky, so the same model can fail a simple recall question and still solve it with a tool** — A chat model cannot list the two Pokemon whose names end in AW from memory, but a coding agent can fetch the full list and filter it with a script. The gap is in what the model can reach, not only in what it knows. ([4:13](https://youtu.be/9fubhllmsBU?t=253))
- **Give the model tools so it can build and search its own context instead of pasting large context** — The speaker's view is that a very large context window was not the way to solve coding. Giving the model a Bash tool and ways to work with the environment let it gather and search its own context, which he says led to Claude Code. ([4:13](https://youtu.be/9fubhllmsBU?t=253))
- **Agents are moving from prompt-driven to self-waking, proactive and multiplayer work** — Claude Code previously needed a prompt before doing any work. The speaker says the ability to wake itself up to do work is what he thinks unlocks the next wave of agents. ([5:39](https://youtu.be/9fubhllmsBU?t=339))
- **Newer models want a smaller system prompt, with context in place of constraints** — Anthropic removed about 80% of the Claude Code system prompt. Older models needed many examples and rules, but this class is more imaginative than the examples, which constrain it. The team now tries to explain context rather than write 'do not' rules. ([5:39](https://youtu.be/9fubhllmsBU?t=339))
- **Interaction features scale with model capability: the question tool went from rarely used to whole HTML reports** — The AskUserQuestion tool barely fired on Opus 4 and needed tuning. By Opus 4.5 it could run a 40-question spec interview. With Opus 4.8 and Fable it can build an HTML report with questions embedded in it. ([7:05](https://youtu.be/9fubhllmsBU?t=425))
- **Your unknowns limit the model: Fable goes further into any gap in your spec, so you must find the gaps** — The prompt and spec are the map, and the codebase and real constraints are the territory. Whatever the model meets that the map omits becomes an unknown it resolves by itself. The speaker says Fable is bottlenecked by how well the user matches map to territory. ([8:29](https://youtu.be/9fubhllmsBU?t=509))
- **Use a four-quadrant frame (known knowns, known unknowns, unknown knowns, unknown unknowns) to plan prompts** — Known knowns are what goes in the prompt. Known unknowns are open questions. Unknown knowns are obvious things never written down. Unknown unknowns are what you have not considered at all. The model can help find each of them. ([9:49](https://youtu.be/9fubhllmsBU?t=589))
- **Stay in the loop with the agent through implementation notes and quizzes** — Ask the agent to log every unknown it hits so you can see where deviations happened. Before a PR or merge, have it quiz you on what was done so you can explain the work. The speaker calls staying in the loop the most important part of working with Fable. ([12:36](https://youtu.be/9fubhllmsBU?t=756))
- **Trade-offs are often not real, so test ambitious scope instead of pre-deciding priorities** — The speaker says that with Claude and Fable, the usual good/fast/cheap choice becomes something to push against. Rather than ranking a list of priorities, he suggests building all of it to let reality show the trade-off. He also says building is easier now, but generating value is still hard. ([16:54](https://youtu.be/9fubhllmsBU?t=1014))

## Techniques
- **Blind-spot pass** — Before starting an unfamiliar task (e.g. adding an auth provider), ask the model to read the relevant module, git diff or Slack context and list hidden gotchas and unknown unknowns, then use those to write a better prompt. *When:* At the start of work in an unfamiliar codebase or domain, before writing the spec.
- **Brainstorm via throwaway prototypes** — Ask for several very different versions (e.g. an HTML dashboard with four wildly different design decisions) and react to them, so tacit preferences surface that you could not describe in words. *When:* When you know the goal but cannot state the look, feel or design preference in advance.
- **Interview me before building** — Ask the model to interview you about the work, and say which kind of questions matter most (e.g. ones that would change the architecture). Newer models can ask dozens of questions, or put them in an HTML form. *When:* After you have a rough idea but suspect unspecified decisions remain.
- **Reference as the map** — Give the model an existing artifact in place of a written spec: a code sample in another language or system, or an HTML mockup for a React component. It reads the artifact and starts from it. *When:* When the desired behaviour is easier to show than to describe.
- **Implementation-note log for unknowns** — Tell the agent to write down each unknown it hits and the decision it made, so deviations from the plan are visible and can be checked. *When:* During long or autonomous agent runs where the user will review the result later.
- **Quiz the agent on its own work** — Before creating or merging a PR, ask the model to quiz you on what was done to confirm you understand the change well enough to represent it. *When:* Before merging agent-written code, to keep the human in the loop.
- **Shrink the system prompt for newer models** — Remove examples and 'do not' rules, and replace them with the reason behind the desired behaviour. Keep only the tools and instructions that the model needs. *When:* When upgrading to a newer model class, since older prompt patterns may constrain it.
- **Give the agent a tool rather than more context** — Provide a code-execution or Bash tool so the model can fetch, filter and compute over data, instead of relying on memory or pasting large amounts of text into the context. *When:* When the task needs exact enumeration, filtering or search over data the model may only partly recall.

## Numbers
- About 1,000 Pokemon exist, and only 2 names end in AW (Croconaw and Dreadnought); a chat model failed this but a coding agent solved it by scripting a filter ([4:13](https://youtu.be/9fubhllmsBU?t=253))
- Anthropic removed about 80% of the Claude Code system prompt when moving to the newer model class ([5:39](https://youtu.be/9fubhllmsBU?t=339))
- Opus 4.5 could run an interview of about 40 spec questions; Opus 4.8 and Fable can produce HTML reports with questions embedded ([7:05](https://youtu.be/9fubhllmsBU?t=425))
- A full deck was made in about four hours with Fable ([16:54](https://youtu.be/9fubhllmsBU?t=1014))
- Speaker ran a YC-backed startup of about 30 people and describes trade-offs forced by how hard code was to change ([14:02](https://youtu.be/9fubhllmsBU?t=842))

## Hot takes
- Models are grown, not designed, so the harness and prompts are a function of how well we understand the model.
- Capability is spiky: a coding agent can answer questions that a chat model with the same knowledge cannot.
- Newer models want fewer examples and fewer 'do not' rules; examples can constrain them more than they help.
- Trade-offs are not real; the way to find them is to attempt the full scope and let reality show the cost.
- Building is easier now, but generating value is still hard, and teams over-invest in process and setup.

## Tools mentioned
Claude Code, Bash tool, code execution tool, AskUserQuestion tool

## Relevance to our work
- **prosharness** (2/3): ProsHarness drives Claude Code with plans, critique and checkpoints. The talk covers plan-stage interviews, unknown-logging and quizzing the agent before a merge, which map to its plan and approval steps. → *Add an interview or blind-spot pass step before ProsHarness generates a plan, and have each run write an unknowns log that the approval phone flow can show.*
- **general** (2/3): Covers context engineering for coding agents: shrink system prompts, prefer reasons over constraints, and give agents tools to fetch context on demand. This is directly on the recurring context-engineering interest. → *Audit the CLAUDE.md or AGENTS.md in the working repos: remove 'do not' rules and examples that could be replaced by one line of reasoning, then compare agent behaviour on a fixed task set.*
