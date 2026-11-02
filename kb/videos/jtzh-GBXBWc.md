# The Factory That Dreams: 39 AI Agents, No Framework - Rushabh Doshi, Machinecraft

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `jtzh-GBXBWc` · [watch](https://youtu.be/jtzh-GBXBWc) · **date:** 2026-07-18 · **length:** 9:58 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Rushabh Doshi · **orgs:** Machinecraft, Cursor
- **topics:** multi-agent, memory, skills-self-improvement, enterprise-adoption · **tags:** company-brain, knowledge-graph, vector-store, salience-gate, dream-cycle, soul-file, specialist-agents, go-to-market, BrainOS, no-fine-tuning, human-in-the-loop-drafts

> A 100-person Indian thermoforming-machine maker built a 36-agent go-to-market "brain" with layered memory and a nightly dream cycle, with no training and no framework. The talk is a company story with some architecture and cost claims.

## Summary
Rushabh Doshi of Machinecraft, a 100-person factory in India, describes building an AI system that runs the company's go-to-market. The motivation was that company knowledge lived in three generations of people, and staff turnover kept losing it. The team ingested years of quotes, drawings, emails and payment records, chunked them, and stored them as vectors plus a relationship graph, using off-the-shelf models and no fine-tuning. The system is split into about 36 single-purpose agents (the title says 39), with an orchestrator that pulls in specialists who debate before giving one answer. Memory is layered, with a salience gate, and human corrections are treated as permanent and win conflicts. A nightly "dream cycle" replays the day, finds contradictions, prunes stale items, turns work into reusable skills, and writes a morning report. The speaker says a written rules file (the "soul file") acts as guardrails, and claims the build cost about 30k against a 230k agency quote, running at roughly a couple of thousand dollars a month. The talk ends by pitching BrainOS, a forkable version of the architecture. The speaker gives no evals, error rates or measured results, so the claims are unverified.

## Key ideas
- **Company knowledge, not machines, is the real asset, and it had been held by three generations of people. Staff turnover was the risk the company wanted to fix.** — The speaker framed the goal as a system that remembers what customers were quoted, why a machine was customised, and so on. Turnover was losing that knowledge each time someone left. ([0:00](https://youtu.be/jtzh-GBXBWc?t=0))
- **No training was needed. Historical documents were chunked, passed through off-the-shelf models to extract facts, and stored as vectors plus a relationship graph.** — The corpus was private company history (quotes, drawings, payment schedules, emails). The speaker presents retrieval-and-extraction as the whole approach, with no GPUs or fine-tuning. ([2:31](https://youtu.be/jtzh-GBXBWc?t=151))
- **Many narrow agents beat one large prompt. Each agent has one job, and an orchestrator convenes specialists who argue and return a single answer.** — Roles named in the talk include an orchestrator (Athena), a sales agent, a pricing agent, a machine-spec agent, a fact-checker, and a corrections guard. The speaker says one prompt doing everything performs badly. ([3:58](https://youtu.be/jtzh-GBXBWc?t=238))
- **Human corrections are stored permanently and override other sources. The corrections agent is what keeps a fixed fact fixed.** — On conflicts, the speaker says corrections win. The stated rule is that once a human fixes something, it stays fixed. ([6:26](https://youtu.be/jtzh-GBXBWc?t=386))
- **Memory is built in layers with a gate, so the store does not fill with junk.** — Layers named: working memory for the last few minutes, pinned facts about people, episodes (whole conversations as short stories), and relationship warmth that grows over time. A salience gate decides what is worth keeping. ([6:26](https://youtu.be/jtzh-GBXBWc?t=386))
- **A nightly consolidation job is the main improvement loop. It replays the day, promotes useful items, flags contradictions, forgets stale ones, and distils skills, then writes a morning report for a human to read.** — The speaker says the system gets smarter overnight. The dream report lists what was consolidated, what was dropped, and what was learned. No measured effect on quality is given. ([7:26](https://youtu.be/jtzh-GBXBWc?t=446))
- **Behavioural rules are written as a single guardrail file taken from the company's family principles. The speaker says these rules are engineering constraints.** — Examples given: cross-check before speaking, never state things absolutely, cite the document and date, stay in your own lane, and report uncomfortable truths. Each rule is meant to be enforced in production. ([7:26](https://youtu.be/jtzh-GBXBWc?t=446))
- **Agents draft, humans send. Every outbound action is shown to a person before it goes out.** — The speaker calls this the golden rule. It covers outbound emails, quotes, and replies, with human approval before anything is sent. ([5:27](https://youtu.be/jtzh-GBXBWc?t=327))

## Techniques
- **One-job specialist agents with an orchestrator and debate** — Split the work into narrow agents (sales, pricing, specs, fact-check, corrections). An orchestrator pulls in the relevant specialists, they argue, and one answer comes out. *When:* When a single prompt is failing across many unrelated sub-tasks, and you need a checked answer rather than a fast one.
- **Layered agent memory with a salience gate and correction precedence** — Keep working memory for recent turns, pinned facts, episodic summaries, and per-contact relationship state. Gate writes so only salient items are stored. Let human corrections override conflicting stored facts. *When:* Long-lived assistants that talk to the same people across sessions and must not drift or re-learn corrections.
- **Nightly consolidation (dream cycle) job** — On a schedule, replay the day's activity, promote useful facts, detect contradictions, prune stale entries, convert repeated work into reusable skills, and write a report for a human to review in the morning. *When:* Agents that run daily and need continuity and skill growth without someone supervising each task.
- **Rules file as production guardrails** — Write a short set of behavioural rules (cross-check sources, avoid absolute claims, cite source and date) and load it into every agent as a constraint. *When:* Agents that make factual claims from several internal sources and must show where each claim came from.
- **Chunk-and-extract over a private corpus with no training** — Chunk historical documents, extract facts using off-the-shelf models, and store results as vectors plus a relationship graph, with a CRM alongside. *When:* A company with a large private document history and no ML team or training budget.
- **Draft-only outbound with human send** — Agents create drafts, quotes and replies, and a person approves before anything leaves the system. *When:* Any agent that writes to customers or external parties.

## Numbers
- Company runs on about 36 agents. The title says 39, and the body says 36. ([0:00](https://youtu.be/jtzh-GBXBWc?t=0))
- Roughly 100 people and no data science team or ML budget. ([0:00](https://youtu.be/jtzh-GBXBWc?t=0))
- Hundreds of gigabytes of private history (quotes, drawings, payment schedules, emails) were ingested. ([2:31](https://youtu.be/jtzh-GBXBWc?t=151))
- One machine type serves seven different end markets. ([1:32](https://youtu.be/jtzh-GBXBWc?t=92))
- Nine daily go-to-market jobs run through the system. ([3:58](https://youtu.be/jtzh-GBXBWc?t=238))
- Three model providers are used, each chosen for a specific job. ([5:27](https://youtu.be/jtzh-GBXBWc?t=327))
- 213 tools exposed over a single protocol. ([6:26](https://youtu.be/jtzh-GBXBWc?t=386))
- Speaker says an agency quoted 230k to build it, and it was built for around 30k. ([8:52](https://youtu.be/jtzh-GBXBWc?t=532))
- Speaker says it runs on a couple of thousand dollars a month, and that no training bill was incurred. ([8:52](https://youtu.be/jtzh-GBXBWc?t=532))

## Hot takes
- The expensive part of company AI is not compute, but teaching the company to remember itself.
- Biology and ancient philosophy are usable engineering blueprints for agent memory and guardrails.
- A company's brain can be forked from a blank template, and each company should fill it with its own data.

## Tools mentioned
Cursor, vector database, graph database, CRM, Google Workspace integrations, document ingestion tooling, monitoring tooling

## Relevance to our work
- **agentos** (2/3): Layered memory with a salience gate, correction precedence, and a nightly consolidation loop that turns daily work into skills. This overlaps MemoryMesh and SkillForge, but the talk offers no measured results. → *Read the dream-cycle design (replay, contradiction check, pruning, skill distillation, morning report) as prior art for SkillForge's skill-worthiness scoring. Do not copy its quality claims without measurement.*
- **prosharness** (1/3): A scheduled nightly job with a morning report and an overnight skill-promotion step is similar to ProsHarness loops and schedules. The specialist debate is also a loose match for plan, critique and debate. → *Consider a scheduled consolidation pass in ProsHarness that writes a morning report of skill and memory changes for review.*
