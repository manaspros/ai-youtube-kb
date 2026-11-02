# Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Kz4QJmNrVXU` · [watch](https://youtu.be/Kz4QJmNrVXU) · **date:** 2026-08-18 · **length:** 20:37 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Matt Dailey · **orgs:** Ref
- **topics:** context-engineering, multi-agent, coding-agents · **tags:** velocity-sickness, planning-vs-implementation, shared-plan-doc, stateless-agents, decision-log, idea-velocity, PR-review-shift-left, team-alignment, plan-mode, human-ownership

> Matt Dailey (Ref) argues that AI makes individual engineers faster but not teams, and proposes working in shared docs for decisions, with agents as stateless actions, so humans keep ownership of the product.

## Summary
The speaker names "velocity sickness": output rises sharply with AI, but impact does not follow. He lists four team-level symptoms: too many PRs to merge, moving in too many directions, "agent bankruptcy" (throwing away and rebuilding agent sessions each day), and critical decisions made silently by agents. He argues that the IDE and chat were built for implementation, while the new work is planning and decision-making, which needs a shared and durable artifact. His proposed fix is to make a doc the core unit of work: decisions are written there, agents are treated as stateless workers that start from the doc, and the team reviews the plan before code is written. He frames the shift as moving from code velocity to idea velocity. The talk ends with a pitch for Ref, the speaker's own product, which is a tool for the decision layer.

## Key ideas
- **Velocity sickness: individual AI speed-ups do not reach team impact** — The speaker defines it as stress from sudden output increases, which results in output without impact. Four symptoms: too many PRs, too many directions at once, agent bankruptcy, and agents making critical decisions. He says the symptoms get worse when the whole team has them. ([3:46](https://youtu.be/Kz4QJmNrVXU?t=226))
- **Agent bankruptcy comes from keeping state in the session** — When the agent's context lives only in a long chat, a new day means rebuilding it and paying for the same work twice. He says the fix is to keep state out of the session. ([2:17](https://youtu.be/Kz4QJmNrVXU?t=137))
- **Chat is built for implementation, not for decisions** — IDEs and chat were designed for heads-down building. Chats are isolated and ephemeral, so decisions made in them are not shared with the team and are lost. The new work needs a different tool built around docs. ([9:02](https://youtu.be/Kz4QJmNrVXU?t=542))
- **Separate the agent (action) from the doc (state)** — The durable doc holds the decisions and context. Agents are close to stateless and start from the doc, so new agents can pick up the same context and several can work in parallel. ([13:02](https://youtu.be/Kz4QJmNrVXU?t=782))
- **Shift from code velocity to idea velocity** — Planning without implementing is a good sign: ideas get explored, and only the worth-building ones get built. This helps avoid prototype gravity, where a team ships the first idea it built. ([15:01](https://youtu.be/Kz4QJmNrVXU?t=901))
- **Move review earlier, to decisions** — If the key decisions are aligned in the plan first, code review becomes simpler because the hard part, deciding what matters, is already done. Humans must own the decisions to keep ownership of the product. ([16:05](https://youtu.be/Kz4QJmNrVXU?t=965))
- **Durable decision log beats LLM summaries** — Pulling decisions out up front, agreeing on them, and storing them in a durable place avoids relying on a model to summarise the session later and maybe pick the wrong things. ([17:07](https://youtu.be/Kz4QJmNrVXU?t=1027))
- **Share plans with teammates before implementation** — Plans should be given to teammates as well as agents, because teammates hold context that is not written down and give useful feedback. He calls this unnatural for many engineers. ([19:37](https://youtu.be/Kz4QJmNrVXU?t=1177))

## Techniques
- **Doc as shared state, agents as stateless workers** — Keep decisions, context and plan in a doc. Start each agent from the doc, and have agents write results back to it. Resume work by reading the doc, not the old chat. *When:* Multi-session or multi-agent work, handoffs between people, and any project where a restart would otherwise lose context.
- **Two-gear workflow: plan vs polish** — Treat planning (exploring the idea, making decisions) and polish (checking the agent's output) as separate modes. Notice when a single session drifts from one into the other, and check whether the tool fits the current mode. *When:* Any time a session mixes exploration with implementation and the output starts to feel unfocused.
- **Front-load decisions before code** — Before an agent implements, list the key decisions and agree on them with the team in the plan. Review the plan first, so the code review only has to check the implementation. *When:* Large changes or several parallel agents where PR volume and direction drift are problems.
- **Plan as a portal to the system** — Ask the agent to pull out the parts of the system that matter for the current task, lay them out, and let the human arrange them in the way they want the system to grow. *When:* Working in an unfamiliar or complex codebase, or deciding where a system should go next.
- **Idea exploration before build** — Let the agent explore several ideas as plans without building them. Build only the ones that survive the exploration. *When:* Early product or feature discovery, when a prototype would otherwise lock the team into one direction.

## Numbers
- Anecdote: an engineer with 12 terminals open each running an agent, then having to restart the work the next morning ([2:17](https://youtu.be/Kz4QJmNrVXU?t=137))
- Anecdote: a newsletter writer using agents to produce about a book's worth of pages every week, which go largely unread ([5:11](https://youtu.be/Kz4QJmNrVXU?t=311))

## Hot takes
- Chat is the wrong default for decision-making work because it is isolated, ephemeral and skips the team.
- Agent bankruptcy is avoidable if the state lives in a doc and agents are treated as stateless.
- Planning without implementing is a healthy sign, not wasted effort.
- Letting an agent make critical decisions means giving up ownership of the code and product.

## Relevance to our work
- **prosharness** (2/3): The doc-as-state pattern matches ProsHarness checkpoint/resume: the doc acts as the checkpoint and fresh agent sessions rebuild from it. The plan-review and shared-plan ideas also map onto its plan, critique and debate steps. → *Make the ProsHarness checkpoint a human-readable plan doc that a fresh session reads first, and have a teammate review the plan before the implementation step runs.*
- **agentos** (1/3): The stateless-agent and durable decision-log ideas relate to SkillForge and EvolveCraft, but the talk gives no technical detail for building them. → *Consider storing SkillForge's decisions in a durable log that is separate from the agent session.*
