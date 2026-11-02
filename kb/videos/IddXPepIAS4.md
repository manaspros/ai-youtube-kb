# Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `IddXPepIAS4` · [watch](https://youtu.be/IddXPepIAS4) · **date:** 2026-07-18 · **length:** 17:47 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Erik Hanchett · **orgs:** AWS, GitHub
- **topics:** context-engineering, coding-agents, testing-verification, mcp-and-tools · **tags:** spec-driven-development, kiro, spec-kit, requirements, design-doc, property-based-testing, steering-docs, agents-md, ears, human-in-the-loop, mcp, mvp-first

> Erik Hanchett (AWS) on spec-driven development: write requirements, design and task markdown before code, keep a human reviewer in the loop, and use property-based tests to check the result.

## Summary
The speaker argues that writing requirements, design and task markdown before any code gives LLM coding assistants the direction they need, since they act like eager AI interns. He stresses keeping agents.md or CLAUDE.md steering docs at a 'Goldilocks' level of detail and using on-demand skills during the spec process. The human stays accountable as the reviewer of every spec and every code change. The workflow has three phases: requirements in EARS format after clarifying questions, a higher-level design with diagrams, and an implementation task list. He recommends generating property-based tests from the requirements and design, then asking for the top four tasks as an MVP so it can be seen working first. MCP can pull tickets from Jira or Asana into spec creation. He says the method also works for legacy projects. Most of the talk is a walkthrough of AWS's Kiro IDE, with GitHub's spec-kit and a manual prompt sequence offered as alternatives.

## Key ideas
- **Spec before code: write requirements, design and task markdown first** — Specs and design docs are written as markdown before any code. The speaker says this suits LLM assistants because it supplies the context and direction they need. ([0:00](https://youtu.be/IddXPepIAS4?t=0))
- **Treat coding assistants like eager AI interns** — Given even a little latitude, assistants go off track. He compares them to an intern who drops everything for each offhand idea from a VP and must be taught to write requests down and check them. ([1:15](https://youtu.be/IddXPepIAS4?t=75))
- **Steering docs need a Goldilocks amount of context** — agents.md or CLAUDE.md should hold enough rules for the assistant to act correctly, but not so much that it drowns. Skills (on-demand instruction files triggered by keywords or slash commands) can carry the rest during design and task work. ([3:51](https://youtu.be/IddXPepIAS4?t=231))
- **The human stays the reviewer and is accountable** — Every design doc, requirements doc and code change needs human review. He says the person who ships is blamed, not the agent. AI review tools can help, but they do not replace the human. ([5:15](https://youtu.be/IddXPepIAS4?t=315))
- **Three-phase flow: EARS requirements, design, then tasks** — Requirements use EARS format after clarifying questions. The design doc is higher level and may include Mermaid diagrams. The task list comes last. He advises editing each doc by hand and checking for inconsistencies and hallucinations before moving on. Design-first is also valid. ([9:17](https://youtu.be/IddXPepIAS4?t=557))
- **Property-based tests as a check that tasks match the spec** — The flow generates property tests from the requirements and design. In his TypeScript demo these use FastCheck and run many generated inputs per property. He also asks for the top four tasks to be done as an MVP first, so a working result can be seen early. ([11:51](https://youtu.be/IddXPepIAS4?t=711))
- **MCP pulls product requirements into the spec process** — Tickets and requirement docs in tools like Jira or Asana can be fetched through MCP while specs are written. Steering files or the first prompt can say which MCP server to read. He calls MCP still maturing and worth watching for security. ([13:14](https://youtu.be/IddXPepIAS4?t=794))

## Techniques
- **Manual spec loop with any coding assistant** — Prompt for user requirements (or supply your own as a basis), review them, then ask for a design doc, review it, then ask for a task list tied to both documents. Do the implementation one task at a time. *When:* You do not have a spec tool, or you want to run the process on any assistant.
- **Clarifying questions before requirements** — Have the assistant ask Q&A questions before it writes requirements. Answers feed a quick plan mode that generates all the spec docs at once. *When:* The prompt is short and the assistant would otherwise guess at scope.
- **EARS-format requirements** — Write each requirement as a user story in EARS form (for example, 'When X, the system shall Y'), with a numbered intro and user stories. *When:* You need requirements precise enough to turn into tests or tasks.
- **Property tests generated from requirements and design** — Ask for property-based tests that express the requirements, then run them against the implementation. In his demo the tests check invariants such as the genre list being a sorted set of unique values over any data set. *When:* You want evidence that each task meets the spec, not only that example tests pass.
- **MVP-first task ordering** — After the task list is generated, ask the assistant to move the top four tasks to the front and deliver a working MVP before the rest. *When:* You want something runnable early and a chance to review direction before the full build.
- **Steering docs plus on-demand skills** — Keep agents.md or CLAUDE.md to rules and guidelines only. Put specialized procedures, such as design-doc or task steps, in skills that load on keywords or slash commands. *When:* The project has grown and one global context file is becoming too large or too thin.
- **Pull requirements from PM tools via MCP** — Connect a Jira or Asana MCP server. Name it in steering docs or in the first spec prompt so the assistant reads tickets before writing requirements. *When:* Product requirements already exist as tickets or docs.

## Numbers
- Kiro preview downloads reached tens of thousands, and the team had to add a gate in front of the preview (speaker's account) ([7:59](https://youtu.be/IddXPepIAS4?t=479))
- Property tests from the spec run dozens, if not hundreds, of times with different generated values per property ([14:45](https://youtu.be/IddXPepIAS4?t=885))
- Top four tasks are used as the first MVP slice before the rest of the task list is implemented ([11:51](https://youtu.be/IddXPepIAS4?t=711))

## Hot takes
- Human reviewers are accountable for spec-driven output; blame falls on the person, not the agent.
- Frontier models are improving but still not good enough to skip explicit context and design documents.
- MCP is still maturing, but is worth using to feed PM tickets into spec creation, despite security concerns.

## Tools mentioned
Kiro, spec-kit, MCP, FastCheck, Mermaid, EARS, Jira, Asana, agents.md, CLAUDE.md

## Relevance to our work
- **prosharness** (2/3): ProsHarness runs long Claude Code tasks with plan and critique steps; a requirements, design, task and MVP-first stage with a human review gate would fit before its task loop, and the property-test idea could sit in its verify step. → *Add a spec-doc stage (requirements, design, tasks) with a human review gate before the task loop, and try generating property tests from the requirements as a verify step.*
- **general** (2/3): Directly relevant to context engineering: the Goldilocks guidance for CLAUDE.md or agents.md and on-demand skills for procedures. → *Audit the CLAUDE.md files in use for too much or too little context, and move procedure-specific steps into on-demand skills.*
- **agentos** (1/3): Next-phase AgentOS is about correctness checks, and this talk's property-based test idea could apply there. Most of the talk is about dev workflow, not infra. → *Read the FastCheck property-test approach and consider using requirement-derived property tests as the correctness check for one AgentOS component.*
