# GTM Engineering: The Technical Bits — Everett Berry, Clay

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `UhCY231d0FQ` · [watch](https://youtu.be/UhCY231d0FQ) · **date:** 2026-09-18 · **length:** 19:04 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Everett Berry · **orgs:** Clay, Smartlead
- **topics:** data-engineering, agent-architecture, multi-agent · **tags:** gtm-engineering, waterfall-enrichment, orchestration, persistent-agents, cold-email, crm, data-quality, field-ownership, multi-domain-outreach

> Everett Berry (Clay) on the technical hard parts of GTM engineering: data waterfalling, graph-based orchestration, long-running per-account agents, and outbound execution limits.

## Summary
Everett Berry from Clay gives a short tour of the technical problems in GTM (go-to-market) engineering, framed as removing constraints so GTM teams can ship at roughly engineering cadence. He covers four areas: the data layer (a continuously updated model of accounts and contacts), orchestration across the 10 to 30 tools a GTM team uses, long-running agents that keep per-account state, and execution (outbound email and calls). The data section centres on waterfalling, which means querying several vendors in turn because no single provider has complete coverage, plus selective field updates to control cost. For orchestration, he argues for a graph of general-purpose nodes (agent, tool call, conditional, code, fan-out and fan-in) because separately syncing systems force waits and loops. For agents, he describes one persistent agent per account that sleeps until a trigger or heartbeat wakes it, and recommends keeping agent-written CRM fields separate from human and deterministic fields. The talk ends with cold-outreach realities: reply rates are very low, so he routes reply handling across multiple domains and suppresses sequences when another channel books a meeting. Q&A names the human-agent handoff as the hardest open problem. The talk is practitioner-level and light on code, but the patterns are concrete.

## Key ideas
- **GTM teams now ship changes at near engineering cadence (Clay pushes new data, automations and campaigns about every two weeks), and GTM engineering exists to remove what stopped them.** — The speaker says the role is one of the first that directly tracks AI model progress, because stronger models give GTM engineers more leverage. ([0:08](https://youtu.be/UhCY231d0FQ?t=8))
- **The data layer's goal is a live virtual copy of the market, and accounts change constantly, both on their own and because of GTM activity.** — Field updates on paid third-party data are expensive, so teams should refresh only selected fields, not everything. First-party and streaming signal data must be merged in too. ([2:28](https://youtu.be/UhCY231d0FQ?t=148))
- **Waterfalling: no single data vendor covers everything, so query several providers in sequence to fill gaps.** — His example: one phone-number provider covered only about half the target countries. Teams should run evals across providers to find which is most accurate per field. ([4:37](https://youtu.be/UhCY231d0FQ?t=277))
- **Systems sync on their own schedules, so a record created in one tool may not exist yet in another, which forces waits and polling loops.** — Different systems need different cadences: real-time single records, bulk daily runs, or monthly refreshes. Field-level change rates also differ (headcount changes often, HQ rarely). ([7:55](https://youtu.be/UhCY231d0FQ?t=475))
- **He recommends a graph-based orchestration layer built from general-purpose nodes: agent, tool call, conditional, code, and a MapReduce-style fan-out and fan-in.** — Triggers or schedules start the graph, it talks to several systems, merges the results, and pushes them to the interfaces reps use. He says this is the modern default whether you build or buy. ([8:55](https://youtu.be/UhCY231d0FQ?t=535))
- **For long deal cycles, use one persistent agent per account. It is dormant most of the time, wakes on a trigger or heartbeat, and reloads current context from the data and orchestration layers.** — After a loss, the agent waits a set time before re-engaging. Continual learning from outcomes is, in his words, still unsolved. ([10:38](https://youtu.be/UhCY231d0FQ?t=638))
- **Keep the fields agents write separate from fields written by deterministic systems or humans.** — Agent output has to be mapped carefully into structured CRM schemas, and the agent's writable fields should be explicit. ([11:48](https://youtu.be/UhCY231d0FQ?t=708))
- **Cold outreach reply rates are low and falling (about 0.5 to 1 percent), so execution errors cost a lot, and sending from one main domain risks reputation damage.** — Common fixes are several sending domains, routing replies from those domains back to the main inbox, and suppressing other sequences once a meeting is booked on another channel. ([13:54](https://youtu.be/UhCY231d0FQ?t=834))
- **The hardest open problem he named is coordinating human reps with agent actions, since a rep may not know what the agent did or may disagree with it.** — This came from Q&A. He also said GTM engineering covers inbound as well as outbound, because routing and qualification have the same orchestration problems. ([16:15](https://youtu.be/UhCY231d0FQ?t=975))

## Techniques
- **Waterfall enrichment** — Query several data providers in sequence for the same field, keep the first valid result, and fall through to the next provider when it is missing. Run evals per provider and field to choose the order. *When:* When no single vendor covers the fields you need, for example phone numbers across many countries.
- **Selective field refresh** — Define refresh rules per field based on how fast it changes and what it costs, so paid fields are updated only when needed. *When:* When third-party enrichment is expensive and fields change at very different rates.
- **Typed-node orchestration graph** — Build workflows from general-purpose nodes (agent, tool call, conditional, code, fan-out/fan-in). Use waits and loops to poll until downstream systems have synced before acting. *When:* When several SaaS systems sync independently and actions depend on records existing in another system first.
- **Persistent per-entity agent with wake-up triggers** — Keep one agent per account with stored state. Keep it dormant, wake it on events or a heartbeat, and have it load fresh context from the data layer on every wake. *When:* For multi-week workflows where state must persist and the agent acts only on events.
- **Field ownership split** — Give agent-written fields their own CRM properties, separate from deterministic-system and human-written fields. *When:* When agents write back into structured systems and you need to audit or reverse what the agent changed.
- **Timed re-engagement cooldown** — After a negative outcome such as a closed-lost deal, the agent waits a fixed period before it contacts the account again. *When:* To avoid spamming accounts that just said no.
- **Multi-domain sending with reply routing** — Send cold outreach from secondary domains to protect the main domain's reputation. Forward replies from those domains into the main reps' inboxes. *When:* For high-volume cold outbound where deliverability is at risk.
- **Cross-channel suppression** — When a meeting is booked on one channel (such as a call), automatically pause the other channels' sequences, such as email or lifecycle campaigns. *When:* In multi-channel outbound where duplicate or stale touches hurt the account relationship.

## Numbers
- Clay ships new data, automations and campaigns to GTM teams about every two weeks. ([0:08](https://youtu.be/UhCY231d0FQ?t=8))
- One phone-number provider covered only about half of the target countries, so waterfalling across providers was needed. ([4:37](https://youtu.be/UhCY231d0FQ?t=277))
- LinkedIn outreach is about 3 to 4 times more effective than cold email, and cold calling and cold email are roughly equal. ([13:54](https://youtu.be/UhCY231d0FQ?t=834))
- Cold email reply rates are about 0.5 to 1 percent, based on Smartlead data from about 20 million emails. With 100 sequenced contacts, perhaps one reply comes back. ([13:54](https://youtu.be/UhCY231d0FQ?t=834))

## Hot takes
- GTM engineering is one of the first roles that directly reflects progress in AI models, because each model gain gives GTM engineers more leverage.
- Cold email gets less effective every year, and this has been the trend for a long time.
- Waterfalling across data vendors is a required technique, not an optional one, because no single provider is complete.
- The hardest unsolved GTM problem is the human-agent interface, not the agent logic itself.

## Tools mentioned
Clay, Salesforce, Outreach, Slack, Smartlead, Forager

## Relevance to our work
- **prosharness** (2/3): The per-account agent that stays dormant, wakes on triggers or a heartbeat, and reloads context is close to ProsHarness's loops and schedules and checkpoint/resume model for long runs. → *Model each long-running ProsHarness run as a persistent state record that wakes on a schedule or event and reloads fresh context on each wake. Check that checkpoints store state, not transcripts.*
- **agentos** (1/3): The field-ownership split (agent-written fields kept apart from deterministic or human-written fields) applies to how AgentOS stores state and memory. → *Make each AgentOS memory or state record declare which writer owns each field (agent, system or human), and enforce it at the write path.*
- **general** (1/3): Waterfall enrichment with per-field evals across providers is a reusable data-quality pattern for entity and record work. → *Read the waterfalling section (4:37) and consider per-field eval results across providers as a method for ER data-quality checks.*
