# Hiring Employable Agents + Startup Battlefield Finals — Howie Liu, HyperAgent

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `EEt3ZSG4a1s` · [watch](https://youtu.be/EEt3ZSG4a1s) · **date:** 2026-10-12 · **length:** 47:37 · **format:** other · **quality:** 2/5 · **depth:** intro
- **speakers:** Howie Liu, Spiro Nanakos, Nick Nanakos, Max Winnebom, Weston Bel Geddes, Theo (judge), Joshua (judge) · **orgs:** HyperAgent, Airtable, Kamad, Common.io, Built by Foundry, AIE, OpenClaw, Anthropic, Textio
- **topics:** agent-architecture, multi-agent, product-ux, enterprise-adoption · **tags:** always-on agents, heartbeat, human-in-the-loop, agent orchestration, control plane, real-time learning, startup competition, multiplayer markdown, vertical agents, creator economy

> Howie Liu (HyperAgent) argues agents are moving toward always-on "claws" that humans unblock and orchestrate, then the video covers the Startup Battlefield finals (Kamad, Common.io, Foundry).

## Summary
Howie Liu, CEO of Airtable and HyperAgent, opens with a product-form-factor view: completions, chatbots, agents that loop on tool calls, and "claws" that wake on a heartbeat and keep working on long goals. He gives a landscaping-business example where a triager agent hands off to a surveyor agent running in a sandbox VM, and a human approves the binding quote before it goes to the client. He argues agents should learn from user corrections in real time through memory and skill updates instead of waiting for fine-tuning, and that the human job becomes orchestrating a fleet through a control-plane view of status, blockers and handoffs. The second half is the Startup Battlefield finals, a $100K prize contest sponsored by HyperAgent. The three finalists pitched Kamad (agentic commodity trade with a state-machine gate protocol), Common.io (a multiplayer markdown editor for people and agents), and Built by Foundry (agent teams that build products for creators). Most of this half is pitch content with founder claims and few verifiable numbers, so the reusable signal is mainly in Howie's first section.

## Key ideas
- **An agent is a model that recurses on itself with an open set of tools and decisions, which is distinct from a fixed workflow.** — Howie uses the Anthropic definition. The next step is the 'claw': an agent that runs for hours and wakes on a heartbeat, so each wake-up triggers many tool-call turns. ([2:31](https://youtu.be/EEt3ZSG4a1s?t=151))
- **Long-running agents are made by re-invoking the loop on a heartbeat, not by making one turn longer.** — When the loop stops, a heartbeat restarts it, so the agent keeps moving toward its goal and works out how to unblock itself where older agents got stuck. ([3:29](https://youtu.be/EEt3ZSG4a1s?t=209))
- **Agents can be split into scoped roles that hand off work, such as a triager that qualifies a lead and a surveyor that builds the proposal.** — Each agent works in its own context window and tool scope. The surveyor uses a sandbox VM and FFmpeg to pull frames from a customer video. ([9:05](https://youtu.be/EEt3ZSG4a1s?t=545))
- **Humans should stay as the gate for high-impact or binding actions, the way a manager approves a team's work.** — Agents do the research and drafting, then wait for approval before sending a binding quote or agreeing to work. Howie ties this to Sarah Guo's point that humans still own decisions and policy. ([11:24](https://youtu.be/EEt3ZSG4a1s?t=684))
- **Agents should learn from each interaction through memory and skill updates instead of waiting for a fine-tuning run.** — A user can say in Slack or email to remember a correction next time. Howie treats this sticky, evolving context layer as a core property of useful agents. ([12:24](https://youtu.be/EEt3ZSG4a1s?t=744))
- **As the human role changes, the interface needs an orchestration control plane that shows what every agent is doing, what is blocked, and who hands off to whom.** — The human zooms out to supervise the fleet rather than micro-managing each task. Howie says a good fleet keeps working overnight, and an idle fleet is a lost opportunity. ([14:38](https://youtu.be/EEt3ZSG4a1s?t=878))
- **Kamad's gate design: agents advance only after every deny condition clears, so the workflow cannot move until the evidence is real.** — Kamad describes its CFC state machine as governing verification, execution and settlement agents. It emits a settlement signal and never touches funds. This is a founder claim, not something shown in detail. ([23:57](https://youtu.be/EEt3ZSG4a1s?t=1437))
- **Common.io argues productivity tools built for people cannot host agents, so agents need a document product designed for both.** — Their pitch is that Google Docs-style tools only expose MCP for send and read, not for real-time collaboration. Agents and people should appear in the same document and notify each other. ([34:02](https://youtu.be/EEt3ZSG4a1s?t=2042))

## Techniques
- **Heartbeat re-invocation for always-on agents** — After an agent loop stops, restart it on a timer or heartbeat with the goal and current state, so it keeps working until it finishes or is blocked. *When:* Long-running or open-ended goals where a single run would end too early, such as overnight monitoring or multi-hour research.
- **Human approval gate on high-impact actions** — Let agents research, draft and prepare the output, then pause before any binding or customer-facing step until a human approves. Surface the pending item in the human's usual channel. *When:* Actions that are costly or irreversible, such as sending a quote, committing to work, or moving money.
- **Correction-to-memory loop** — When a user corrects the agent in chat, store it as a memory or skill update that the next run reads. No retraining is involved. *When:* Repeated workflows where the same preferences or cost levers keep being explained by hand.
- **Specialist triage and handoff pipeline** — Route an incoming request to a triage agent that checks scope and quality, then hand off to specialist agents with narrower tools and context. *When:* Inbound requests that need different skills at different stages.
- **Deny-condition state machine for agent actions** — Define a state machine where each transition needs explicit checks to pass. Agents cannot advance until all checks clear, and the machine emits a signal for a separate system to act on. *When:* High-stakes multi-party workflows where a wrong step costs money, such as KYC, sanctions or document checks.
- **Sandbox VM per agent thread** — Give each agent thread its own VM where it can write code, manipulate files and run tools like FFmpeg to extract frames from video. *When:* Agents that must analyze media or run code as part of a deliverable.

## Numbers
- Startup competition: 500 founders pre-selected to 20, then 3 finalists. ([16:44](https://youtu.be/EEt3ZSG4a1s?t=1004))
- Prize pool of $100K: $50K winner, $30K runner-up, $20K second runner-up. ([19:56](https://youtu.be/EEt3ZSG4a1s?t=1196))
- Viewers get $1,000 of inference credit on hyperagent.com/AIE. ([16:44](https://youtu.be/EEt3ZSG4a1s?t=1004))
- Kamad says about $17 trillion in physical commodities moves each year. ([23:57](https://youtu.be/EEt3ZSG4a1s?t=1437))
- Kamad says a single trade can be about $200M, and some refinery partners transact $9-12B a month. They estimate about 100 customers would make a billion-dollar company. ([26:10](https://youtu.be/EEt3ZSG4a1s?t=1570))
- Built by Foundry says over half a million people use products its agents built. ([37:00](https://youtu.be/EEt3ZSG4a1s?t=2220))
- A creator going from 4 sponsors to 80 found more conversion, even though most sponsors are irrelevant to any single viewer. ([39:42](https://youtu.be/EEt3ZSG4a1s?t=2382))
- Foundry says no creator has ever left the company, since their products are profitable. ([42:09](https://youtu.be/EEt3ZSG4a1s?t=2529))

## Hot takes
- Nothing is defensible except being the most creative in your category, so ship fast and win on distribution.
- Going to sleep without agents running overnight feels like a loss, since the team is idle without someone unblocking them.
- Writing software today is terrible for agents, and Google Docs-style tools only expose MCP for send and read, not real-time co-editing.
- Creator-led products with cold-start distribution are a strong business model.
- Judge Theo says the creator pivot is weaker in a tech niche because the market is crowded, and Foundry's counter was that homesteading or gardening creators pay more easily.

## Tools mentioned
HyperAgent, OpenClaw, Claude Code (workflows, fan-out to parallel agents), FFmpeg, Slack, email, Gmail, Stripe, Salesforce, WhatsApp, Google Docs, GitHub, MCP

## Relevance to our work
- **agentos** (2/3): The heartbeat re-invocation pattern, the human gate on high-impact actions, and the correction-to-memory loop map onto the L2D self-improvement and MemoryMesh write paths. → *Prototype a correction-to-memory loop: a user correction in a run becomes a MemoryMesh entry read by the next run, and measure whether the next run's output changes on a fixed test case.*
- **prosharness** (2/3): ProsHarness already has checkpoint/resume, schedules and phone-driven approvals. The heartbeat and human-gate patterns extend those directly. → *Use the phone approval step as the explicit human gate before any customer-facing or irreversible step in a long run, and drive resumes from the existing schedules on a heartbeat-like interval.*
- **general** (1/3): The idea that a human should gate binding actions while agents prepare them is a general pattern for multi-agent pipelines. → *Add an explicit approval step, with a named approver and a log entry, to any multi-agent pipeline that sends output outside the team.*
