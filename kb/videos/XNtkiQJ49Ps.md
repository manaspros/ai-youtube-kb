# Agents need more than a chat - Jacob Lauritzen, CTO Legora

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `XNtkiQJ49Ps` · [watch](https://youtu.be/XNtkiQJ49Ps) · **date:** 2026-05-18 · **length:** 14:21 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Jacob Lauritzen · **orgs:** Legora
- **topics:** product-ux, agent-architecture, evals, skills-self-improvement · **tags:** vertical-ai, legal, verifiers-rule, trust-and-control, human-in-the-loop, decision-log, skills, elicitation, guardrails, tabular-review, collaborative-artifacts, chat-vs-artifacts, long-running-agents, compaction

> Legora's CTO argues that vertical agents need more than chat: make work verifiable, let humans steer through skills and decision logs, and use persistent artifacts as the collaboration surface.

## Summary
Jacob Lauritzen, speaking for Legora (a collaborative AI workspace for law firms), argues that the bottleneck in agent work has moved from doing the work to planning and reviewing it. He frames trust with the verifier's rule: tasks that are easy to verify get solved by agent loops, and verifiability differs by legal task (checking definitions is easy, contract strategy is not). He proposes raising trust by making tasks more verifiable (golden-contract comparisons, linting-style checks), decomposing work so humans keep the judgment calls, and limiting what agents can touch. For control, he prefers encoding judgment into skills at each node of the work tree over up-front planning, with agents deciding and writing to a decision log when unsure. Finally he says chat is a low-bandwidth interface and that agents should collaborate in persistent, high-bandwidth artifacts such as clause-scoped documents and tabular reviews. The talk is a product-flavored practitioner talk with few hard numbers.

## Key ideas
- **The bottleneck has shifted from doing work to planning and reviewing it.** — Producing work is now cheap, so the expensive parts are gathering requirements and specs and reviewing large agent outputs. Self-review by agents is tried, but he is not sure it works. ([2:09](https://youtu.be/XNtkiQJ49Ps?t=129))
- **Apply the verifier's rule to agents: easy-to-verify tasks get solved by running an agent in a loop.** — If a task can be checked, the agent can loop on feedback until it passes. Verifiability varies inside one domain: checking contract definitions is easy, while writing a contract is hard to verify (only a court really tests it) and litigation strategy has no objective answer. ([3:09](https://youtu.be/XNtkiQJ49Ps?t=189))
- **Trust rises when you make a task more verifiable, using proxies where true verification is impossible.** — For contracts, compare a new draft against known-good 'golden' precedent contracts as a stand-in test. Giving a coding agent browser access and TDD makes a feature task checkable. ([6:13](https://youtu.be/XNtkiQJ49Ps?t=373))
- **Decompose tasks so humans keep the judgment calls and agents take the checkable pieces.** — Humans keep the risk profile, precedent choice and negotiation stance. Agents handle formatting to house style and linting-like checks, such as whether every defined term is used and every used term is defined. ([6:13](https://youtu.be/XNtkiQJ49Ps?t=373))
- **Guardrails are an allowlist of what the agent may touch, and they buy trust.** — Examples given: only edit these three files, only read from this directory, only search these websites. Claude Code's permission prompts are cited as the low-trust extreme. ([6:13](https://youtu.be/XNtkiQJ49Ps?t=373))
- **Control comes from how the work is structured: a DAG of nodes with judgment encoded at each node, not planning up front or judgment at the root.** — Judging only at the root of a long agent tree gives low control, and up-front planning cannot anticipate special cases. Skills put human judgment into the nodes where work happens, so a special-case rule (for example an EU termination law) is applied when that node runs. ([7:38](https://youtu.be/XNtkiQJ49Ps?t=458))
- **When the agent is unsure, it should decide, log the decision, and keep going; the human reviews the log and reverses choices.** — This combines elicitation with a decision log so runs are not blocked by a stream of questions. Asking 50 questions in a chat is not workable because the human lacks the context to answer. ([10:00](https://youtu.be/XNtkiQJ49Ps?t=600))
- **Chat is too low-bandwidth for complex agent work, so collaboration should happen in persistent, domain-specific artifacts.** — Examples are a document where you can highlight clause three and only that clause changes, comments, tagging agents and collaborators, and handing sections to specialist agents. Tabular review lets the agent flag only the items it wants a human to judge. He says the industry is converging on this UI pattern. ([11:04](https://youtu.be/XNtkiQJ49Ps?t=664))

## Techniques
- **Proxy verification with golden examples** — Keep a set of previously approved outputs (for example contracts) and score new outputs by similarity to them, so the agent has a checkable signal where no ground truth exists. *When:* The true quality test is slow or external (court, customer outcome), but past accepted artifacts are available.
- **Task decomposition by verifiability** — Split one fuzzy task into subtasks. Leave judgment calls to the human and hand the agent formatting, lint-like rules and consistency checks that can be verified mechanically. *When:* A large deliverable mixes easy-to-check mechanical parts with hard judgment parts.
- **Allowlist guardrails for agent actions** — Scope the agent to named files, directories and websites rather than letting it act freely, which lowers review burden. *When:* You want to increase trust in a long-running agent without reviewing every trace.
- **Skills as judgment encoded at work nodes** — Write skills that encode a firm's rules (for example a clause-specific review method, or a jurisdiction's special law) so they fire when the relevant node of the work tree runs, including progressive discovery. *When:* Expert judgment must apply consistently across many subtasks, and up-front planning cannot foresee every case.
- **Elicit-or-decide with a decision log** — When the agent meets something it cannot handle from skills, it asks the human only where needed. Otherwise it makes a decision, records it in a log, and continues. The human later reviews and reverses decisions. *When:* Long runs should not block on humans, but a human must be able to audit and undo choices afterwards.
- **Persistent, scoped artifacts as the collaboration surface** — Use a document or a tabular review as the shared object. Support scoped edits (change only the highlighted clause), comments, @-tagging of agents or people, and handing sections to specialist agents. *When:* The work is a tree with many decisions and reviewers need to see state and steer locally rather than through one linear chat.

## Numbers
- Legora has more than 1,000 customers across more than 50 markets (self-described, fast growth). ([1:08](https://youtu.be/XNtkiQJ49Ps?t=68))
- Illustrative pain point: a long-running contract agent can take about 30 minutes before returning a draft, then gets clause-level errors that a re-run may reintroduce (no benchmark). ([0:00](https://youtu.be/XNtkiQJ49Ps?t=0))
- Tabular review and a new collaborative UI shipped within the last two weeks (relative to the talk, no metric). ([12:30](https://youtu.be/XNtkiQJ49Ps?t=750))

## Hot takes
- Planning as a steering mechanism is inefficient and will not survive; skills and elicitation replace it.
- Chat should not be the main mode of collaboration with complex agents.
- Agents should not be constrained to human language; interfaces such as org charts they can read and edit would be better.
- Asking agents to review their own work with no humans involved is worth trying but unproven.
- Most verticals sit at different points on the verifiability spectrum, so trust tactics must be domain-specific.

## Tools mentioned
Claude Code

## Relevance to our work
- **prosharness** (2/3): ProsHarness runs long Claude Code jobs with checkpoints and phone approvals. The talk's decision-log instead of blocking, skill-encoded judgment, and up-front planning critique are directly relevant. → *Add an 'decide, log, continue' mode to ProsHarness checkpoint runs, where the agent records its chosen default and the phone approval flow reviews and reverts it later.*
- **general** (2/3): A clear framework for where to put human review (verifiability, control, artifact-based review) applies to any agent team. → *Read the verifier's-rule and control-vs-trust slides, then label each recurring agent task as verifiable or not before deciding how much human review it gets.*
- **agentos** (1/3): Decision-log plus elicitation is a governance pattern for long agent runs, and the talk offers no implementation detail that changes AgentOS's stack. → *Read the talk's decision-log idea and consider a logged-defaults mode for long AgentOS runs; no build change yet.*
