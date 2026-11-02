# AI in GTM at Notion — Flora Liu

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `L4I7WgiEquo` · [watch](https://youtu.be/L4I7WgiEquo) · **date:** 2026-09-18 · **length:** 21:15 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Flora Liu · **orgs:** Notion
- **topics:** enterprise-adoption, multi-agent, agent-architecture, data-engineering · **tags:** gtm-engineering, signals, durable-workflows, temporal, human-in-the-loop, context-layer, decision-logs, entity-resolution, snowflake, dynamodb, subagents, build-vs-buy

> Notion's GTM engineer explains a know/decide/act/learn system that unifies sales and self-serve signals, with humans and agents working in one shared context layer on durable workflows.

## Summary
Flora Liu, an engineer on Notion's GTM engineering team, describes replacing a fragmented sales and marketing tool stack with one decisioning system. The team's architecture has four layers: know (a trusted per-customer context), decide (pick the next best step), act (emit a lifecycle email, in-app nudge, or rep task), and learn (feed outcomes back into decisions). Humans and agents operate on the same substrate, with agents doing the repetitive gathering and drafting and humans approving anything customer-facing. The team owns the context layer and rents orchestration, email, and enrichment, using Snowflake for modeled entities, DynamoDB for fast profile reads, and Temporal for durable per-signal workflows. Reported results are early: a 63% higher next-step rate for users who got context-aware recommendations, and more qualified opportunities for enterprise reps over 13 weeks, with no baseline given. The talk is a practitioner case study with few hard numbers and some company-promotional framing.

## Key ideas
- **Four-question loop as the architecture** — Every GTM workflow reduces to: what do we know about the customer, what should happen next, how do we execute safely, and did it work. These map to know, decide, act, learn, with learn feeding back into decide. ([5:21](https://youtu.be/L4I7WgiEquo?t=321))
- **Humans and agents share one loop and one substrate** — Agents do repetitive work at scale (gathering context, researching, drafting). Humans supply judgment, approve recommendations, and own the relationship. The agent is treated as another operator inside the same system, not a layer on top. Context is kept readable to both. ([6:25](https://youtu.be/L4I7WgiEquo?t=385))
- **No direct agent-to-customer contact; untrusted form input** — For sales-assist workflows, humans stay in the loop by default and approve agent actions. Inbound contact-sales form data is treated as untrusted input so trust boundaries hold when an agent is in the middle. ([6:25](https://youtu.be/L4I7WgiEquo?t=385))
- **Build the context layer, rent everything else** — The team builds its own customer context model because that is where its edge is and it must be debuggable. It rents orchestration (Temporal), email, and enrichment (Clay). The choice is made per layer, not as a blanket build-or-buy rule. ([7:47](https://youtu.be/L4I7WgiEquo?t=467))
- **Signal as the unit of action** — A signal is one customer event important enough to change the next step, either user-driven (hit AI limit, contacted sales) or external (funding, hiring, tech-stack change). External signals make the system proactive. A signal service decides whether an action exists, who owns it, and emits a task for a human or agent. ([12:05](https://youtu.be/L4I7WgiEquo?t=725))
- **Each signal runs as a durable workflow** — Every signal becomes a Temporal workflow covering enrichment, web search, and drafting. Retries, dedupe, and resume-from-failure are handled by the engine, so one malformed transcript cannot fail the whole batch. Every LLM step is traced for evaluation. ([13:25](https://youtu.be/L4I7WgiEquo?t=805))
- **Decision logs tie outcomes to the decision that caused them** — Every action is logged as a decision, and outcomes thread back to it. Engagement and lifecycle-message history feed the decision layer, so it can continue, advance, or pivot a thread. The speaker frames this as the self-improvement loop. ([14:48](https://youtu.be/L4I7WgiEquo?t=888))
- **Shadow the best human first, and start with the most legible workflow** — The team shadowed top reps to find the most repetitive part of their job and encoded that. The speaker's warning: encoding a mediocre process yields a mediocre agent. The aim is to raise the floor so new reps can learn from strong reps' patterns. ([15:47](https://youtu.be/L4I7WgiEquo?t=947))

## Techniques
- **Four-layer know/decide/act/learn loop** — Build a trusted per-entity context layer, a decision step that picks one next action, an action step that emits concrete tasks or messages, and a feedback step that links outcomes to the decision logs. *When:* When automations across several tools keep acting on stale or conflicting data and you need a closed loop, not one-shot automations.
- **Denormalized key-addressable profile plus keyed unstructured artifacts** — Compute versioned, modeled entities (accounts, contacts, eligibility, facts) in the warehouse with owner and timestamp per row. Publish a join-free profile per ID to a key-value store for millisecond reads. Store agent-generated notes and summaries under the same IDs so one lookup returns structured and unstructured context. *When:* When agents need low-latency, join-free reads of entity state and must combine structured data with notes.
- **Durable workflow per event with engine-managed retries** — Run each trigger as a workflow on a durable engine. Write only the sequential business logic and let the engine handle retries, dedupe, and resume after failure, isolating each item so one bad input cannot fail the batch. *When:* When each event fans out to several flaky network calls such as LLM, enrichment, or search APIs, and batches must survive single-item failures.
- **Parallel research subagents with score-and-select review loop** — Fan out concurrent research sub-agents, generate several candidate drafts, score them, then have a review agent pick the best and revise it. Repeat the revise step if needed. *When:* For outbound drafting where quality varies and a cheap scored best-of-N with a reviewer beats a single draft.
- **Single eligibility and routing classifier** — Move segmentation and signal definitions out of individual tools into one shared place that every system reads. One classifier decides what the customer should receive, which prevents double sends. *When:* When several tools each apply their own eligibility rules and produce duplicate or contradictory messages.
- **Human approval gate by default, untrusted inbound input** — Agents draft and gather; a human approves before anything reaches a customer. Treat form submissions and other inbound text as untrusted before they enter agent context. *When:* For any customer-facing action with agents in the loop, where a wrong message damages trust.
- **Trace every LLM step and log decisions with outcome links** — Trace each LLM call so quality can be evaluated later. Record each automated action as a decision entry and join downstream outcomes back to it for offline improvement. *When:* When you need to measure whether agent decisions improve over time, not only whether they ran.

## Numbers
- Users who received context-aware lifecycle recommendations were 63% more likely to take the next step (no baseline or sample size given) ([18:32](https://youtu.be/L4I7WgiEquo?t=1112))
- Enterprise reps show increased qualified opportunities over the last 13 weeks (no figure given) ([18:32](https://youtu.be/L4I7WgiEquo?t=1112))
- Each cold outbound signal produces three email drafts that are scored, and the best is revised by a review agent ([12:05](https://youtu.be/L4I7WgiEquo?t=725))
- Snowflake ingests all GTM vendors with daily transforms, some real-time; DynamoDB serves profiles in milliseconds with no joins ([9:13](https://youtu.be/L4I7WgiEquo?t=553))

## Hot takes
- If you encode a mediocre process, you get a mediocre agent, so shadow your best human first.
- Be headless by default and design for agents as operators, not just copilots.
- Build versus buy is a per-layer decision: own the context layer, rent orchestration, email, and CRM.
- Customer-facing agent actions should stay behind human approval, especially where inbound data is untrusted.

## Tools mentioned
Notion, Snowflake, DynamoDB, Temporal, Clay, Gong, Salesforce, Outreach, Nooks, ZoomInfo, Snowflake (product usage), Notion custom agents, MCP

## Relevance to our work
- **general** (2/3): Strong, directly applicable pattern for the recurring interests: a plain-markdown context layer that both humans and agents can navigate, with an approval gate and entity-level provenance. → *Read the talk's context-layer section and design a CLAUDE.md-style context hierarchy that is readable to both humans and agents, with source and timestamp per fact.*
- **agentos** (1/3): The decision-log plus outcome-linking loop maps onto the open question of what success signal SkillForge should use, but the talk gives no method for scoring skill-worthiness. → *Record each agent action as a decision entry with an ID, and join later outcomes back to it as one candidate success signal for SkillForge.*
- **prosharness** (1/3): Per-step durable execution with retries and resume-from-failure is close to ProsHarness checkpoint/resume, and the approval gate matches its phone-driven approvals. → *Compare ProsHarness checkpoints against per-step retry and dedupe semantics, and check that one malformed step cannot stall a whole batch.*
