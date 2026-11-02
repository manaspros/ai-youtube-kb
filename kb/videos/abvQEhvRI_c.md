# Context Graphs for Explainable, Decision-Aware AI Agents — Andreas Kollegger & Zaid Zaim, Neo4j

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `abvQEhvRI_c` · [watch](https://youtu.be/abvQEhvRI_c) · **date:** 2026-06-18 · **length:** 16:39 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Andreas Kollegger, Zaid Zaim · **orgs:** Neo4j
- **topics:** memory, agent-architecture, context-engineering, rag-retrieval · **tags:** context graphs, decision-making agents, knowledge graph, agent memory, policy and rules, escalation to human, decision audit trail, GraphRAG, Text2Cypher, multi-agent decomposition

> Neo4j speakers argue agents need context graphs that store policies and rules as well as facts, so they can make and record decisions. They give a decision framework: frame, check global rules, assess risk, propose, then act, defer or escalate.

## Summary
Two Neo4j speakers (Andreas Kollegger and Zaid Zaim) present context graphs as the next step after knowledge graphs and context engineering: the graph holds the rules and policies behind an agent's choices, not only the facts. They describe a memory layout with short-term conversation state and long-term data about organizations, people and reasoning. The core claim is that autonomous agents hit situations with no instructions, and prompt tweaks do not solve this at scale. Their proposed workflow frames the problem (causal history, objective, environment), checks past decisions and hard and soft rules, and runs a risk and value analysis. One agent proposes options with pros and cons, a separate step checks authority, and the agent then acts, defers or escalates to a human. Every decision, with the reasoning and alternatives considered, is saved to the graph as precedent. The speakers say the framework is generic but the steps are very domain specific, and they give no measured results. The talk ends with a pitch for Neo4j courses and booth visits.

## Key ideas
- **Context graphs add rules and policies to knowledge** — Knowledge graphs give agents facts. The speakers argue agents also need the why, meaning the policies and rules behind an action, so they can drive decisions and not just answer questions. ([3:32](https://youtu.be/abvQEhvRI_c?t=212))
- **Memory is split into short-term and long-term layers** — Short-term memory holds conversation history and state. Long-term memory holds a generalized graph of organizations and people, plus the reasoning that says why an agent should act under given policies. ([5:00](https://youtu.be/abvQEhvRI_c?t=300))
- **Decision-making is the gap that prompt engineering does not close** — Autonomous agents hit moments with no instructions (their example is an agent with a credit card reordering a drink). Patching prompts one case at a time does not scale, and the problem grows as agents multiply. ([7:24](https://youtu.be/abvQEhvRI_c?t=444))
- **Frame the decision with causal history, objective and environment** — The first step asks how the agent got here, what objective it is pursuing, and what environment it operates in. A purchase and a medical choice call for very different handling, so the agent must be told this context. ([8:48](https://youtu.be/abvQEhvRI_c?t=528))
- **Check the global context: past decisions and hard and soft rules** — The agent compares the current case with earlier decisions for consistency, then applies formal and informal business rules. It should balance precedent against rules that may have changed since. ([10:11](https://youtu.be/abvQEhvRI_c?t=611))
- **Risk checks: reference class, reversibility, cost of error, explicit value** — Before acting, the agent works out which reference group the case belongs to (the 99% versus the 1% example), whether the decision can be undone, what a wrong call costs, and what is being maximized or minimized. The speakers say risk analysis is where most agent effort belongs. ([11:10](https://youtu.be/abvQEhvRI_c?t=670))
- **Separate the proposing agent from the deciding agent** — One agent only lists alternatives with pros and cons. A second agent checks whether it has authority. It then acts, defers, or escalates to a more privileged agent or a human. ([13:39](https://youtu.be/abvQEhvRI_c?t=819))
- **Save the full reasoning as precedent for later agents** — The graph records what was considered and what was not, the decision, and the actions taken. Future agents can use this trail as precedent and for accountability. ([15:07](https://youtu.be/abvQEhvRI_c?t=907))

## Techniques
- **Propose, then decide, as two agents** — Split the decision into a proposer agent that returns options with pros and cons, and a decider agent that checks authority and then acts, defers or escalates. Keep the proposer from making the final choice. *When:* When an agent acts on real resources (money, orders, access) and needs an approval or escalation path.
- **Pre-decision risk screen** — Before acting, classify the case: which reference class it belongs to, whether the action is reversible, what a wrong decision costs, and what value is being maximized or minimized. Make these fields explicit instead of leaving them to the model's general knowledge. *When:* For any agent decision where the particulars matter and a generic policy could be wrong for the case.
- **Decision log as a graph of precedent** — Store the framing, the alternatives considered and rejected, the rules applied, the decision (act, defer or escalate), and the resulting actions as linked nodes. Future agents query this trail before deciding. *When:* When agents repeat similar decisions and you need accountability, consistency and audit.
- **Tiered memory in one graph** — Keep conversation state as short-term nodes, and organizations, people and policy rules as long-term nodes in the same graph. Agents query the graph for the decision context, and fall back to Text2Cypher to turn natural-language questions into graph queries. *When:* When an agent needs both recent conversation state and stable organizational rules to answer or act.
- **Framework as a skill or graph workflow** — Implement the decision steps as a workflow in an agent framework (the speakers name LangGraph and ADK), or as a set of skills. Adapt each step to the domain, because the generic steps are hard to reuse as-is. *When:* When you want to add structured decision-making to an existing agent without a full redesign.

## Hot takes
- Prompt engineering alone will not make autonomous agents make good decisions; decision logic has to be made explicit.
- An agent should propose options and not make the final choice, and a separate step should decide whether it has authority to act at all.
- Each decision (including deferrals) should be recorded with its reasoning and rejected alternatives so later agents can use it as precedent.

## Tools mentioned
Neo4j, Text2Cypher, LangGraph, ADK

## Relevance to our work
- **agentos** (2/3): The talk's memory tiers and decision-audit trail map onto MemoryMesh's tiered memory, provenance and conflict resolution. The speakers' graph-based approach is close to AgentOS's Neo4j storage layer. → *Prototype a decision-log schema for MemoryMesh that records the proposal, rejected alternatives, authority check, and final act/defer/escalate outcome as provenance nodes linked to the facts used.*
- **prosharness** (2/3): ProsHarness already runs plan, critique and debate steps and phone-driven approvals. The talk's separate propose and authorize steps and its act, defer or escalate outcomes map onto those approval gates. → *Model ProsHarness approval gates with three outcomes (act, defer, escalate) and store the reasoning and rejected options for each gate in the checkpoint record.*
