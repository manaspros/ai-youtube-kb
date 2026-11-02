# Build the AI GTM Agent That Knows the Buyer - Dr. Sajjan Kanukolanu, Position2 (Position Squared)

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ltv-L5oMPIs` · [watch](https://youtu.be/ltv-L5oMPIs) · **date:** 2026-08-18 · **length:** 26:27 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Dr. Sajjan Kanukolanu · **orgs:** Position Squared
- **topics:** enterprise-adoption, multi-agent, data-engineering · **tags:** gtm, sales-agents, buyer-intent, context-graph, identity-resolution, icp, alert-fatigue, human-in-the-loop, crm, hubspot, linkedin, slack

> Position Squared's three-layer, multi-agent GTM system (anonymous visitor ID, knowledge-base-gated ICP and CRM matching, rep actions). Lessons: ICP drift, alert fatigue, weak identity accuracy, and approval friction.

## Summary
Dr. Sajjan Kanukolanu of Position Squared argues that bolting AI onto an old GTM stack will not scale, and that signals, integration and architecture must be solved together. He describes three layers: signals (CRM, enrichment, LinkedIn activity), buyer intelligence (a knowledge base, ICP scoring, a context graph and routing), and action (personalized chat, rep alerts, CRM updates, sequence triggers). The running system is a chain of agents: multi-source visitor identification, then enrichment, an ICP filter against the knowledge base, a CRM match agent for warm or hot status, and an action agent that sends Slack alerts with draft emails, emails or LinkedIn outreach. He demos an internal dashboard of de-anonymized visitors and LinkedIn engagement. He lists four failure modes (ICP drift, alert fatigue, poor identity resolution, and human approval bottlenecks) and closes with four takeaways about identity, separating fit from intent, auditable policy, and a feedback flywheel. Most figures are from his own deployment, and the talk contains little concrete method detail.

## Key ideas
- **Bolting AI onto an existing GTM stack blocks scale** — Three problems must be solved together: AI that knows the buyer (role, history, intent), integration of intent signals and CRM context, and an architecture with AI at its core. Solving only the first two still fails. ([1:01](https://youtu.be/ltv-L5oMPIs?t=61))
- **Buyers arrive late-stage, so generic chat loses them** — Per his stats, the buyer has mostly decided before contact. A chat that opens with 'How can I help you?' sends the buyer backwards, and buyers leave. The system should already know who the visitor is. ([4:09](https://youtu.be/ltv-L5oMPIs?t=249))
- **Three-layer architecture: signals, buyer intelligence, action** — Signals cover CRM, enrichment of anonymous visitors, and social signals. Intelligence is a knowledge base of ICPs, personas and playbooks, plus scoring, a context builder and routing logic. Action covers personalized chat, rep alerts, CRM updates and sequence triggers. ([5:41](https://youtu.be/ltv-L5oMPIs?t=341))
- **Context graph per person, linked to account and deal** — Each person's signals link to their account, and accounts roll up to a buying committee. Deal-level data shows whether sales or marketing already touched the account. He says this graph is what lets you rank which accounts to prioritize. ([11:19](https://youtu.be/ltv-L5oMPIs?t=679))
- **Staged agent chain with knowledge-base gating** — Identification runs several tools and dedupes their output, then enrichment runs. An ICP filter agent checks the knowledge base and drops wrong industry, geo, size or persona. A match agent checks CRM for warm or hot status. An action agent decides alerts, emails or LinkedIn outreach, at the account or buying-committee level. ([13:26](https://youtu.be/ltv-L5oMPIs?t=806))
- **ICP drift needs quarterly retraining from closed won and lost deals** — Ideal customer criteria change, for example when a $50M to $100M ARR firm in a new vertical closes. Without refreshing the knowledge base each quarter, agents keep pointing at the wrong accounts. ([21:10](https://youtu.be/ltv-L5oMPIs?t=1270))
- **Alert fatigue and identity accuracy limit the system** — If every contact is flagged hot, reps stop trusting the system. He says vendor identity tools are roughly 70% accurate at company level and 15 to 20% at individual level, so plan outreach around those numbers and keep testing vendors. ([22:44](https://youtu.be/ltv-L5oMPIs?t=1364))
- **Approval friction decides whether reps keep using it** — Drafts should need only a minor edit and one click to send. If editing an AI draft takes longer than about 30 seconds, reps go back to writing emails themselves and the initiative dies. ([22:44](https://youtu.be/ltv-L5oMPIs?t=1364))
- **Auditable policy engine and a compounding feedback loop** — GTM staff, not only developers, need to see which agent or step broke and fix it. Sends, replies and closed deals should flow back into the knowledge base so the system improves over time. ([24:20](https://youtu.be/ltv-L5oMPIs?t=1460))

## Techniques
- **Dedupe-then-enrich identification** — Run several visitor identification tools in parallel, consolidate their results and dedupe them, then pass the result to enrichment. Swap vendors without changing the architecture. *When:* Anonymous web traffic where no single identity vendor catches every visitor.
- **Knowledge-base-gated ICP filter agent** — Compare each enriched contact against codified ICP criteria (industry, geo, size, persona). Delete non-fits and move the rest into a clean qualified table before any downstream agent runs. *When:* Before spending LLM or outreach budget on contacts that do not fit the target profile.
- **Per-person context graph with account and deal rollup** — Store all touchpoints in one record per person. Link people to accounts, roll up the buying committee per account, and attach deal-level sales and marketing touches. *When:* When you need to prioritize accounts and see who in a buying committee has already been contacted.
- **Separate fit score from intent score** — Score ICP fit and buying intent independently, then route on both. Do not merge them into one number. *When:* When routing messages, because a combined score sends the wrong message to the wrong person.
- **Personalized returning-visitor chat** — On landing, identify the visitor, greet them by name, and point to their earlier conversation or to content matched to their intent signals. Do not open with a generic question. *When:* When a site chat is meant to move a late-stage buyer forward.
- **Quarterly ICP refresh from closed outcomes** — Each quarter, retrain or update the knowledge base and agent criteria using closed-won and closed-lost opportunities. *When:* When the target customer profile is changing, to stop agents from using stale criteria.
- **Alert budget tuned to rep capacity** — Limit which accounts and contacts trigger a rep alert so the rep only sees high-value signals. Too many alerts lose the rep, too few miss revenue. *When:* When pushing alerts to sales reps in Slack or another channel.
- **Auditable, adjustable policy engine** — Log which agent or pipeline step produced or dropped each record, and let a GTM team member change the rules without a developer. *When:* When multi-agent pipelines break often and non-engineers own the output.
- **One-click draft approval with a 30-second budget** — Make AI drafts close enough to final that a rep can send with one click. Measure edit time; if it passes about 30 seconds, rework the draft quality. *When:* When a human must approve AI-written outreach and adoption is at risk.

## Numbers
- Position Squared has launched 75+ AI agents for clients and runs 18+ vertical knowledge bases, with 800+ agent runs per month (month-to-date June 2026, per the speaker). ([0:00](https://youtu.be/ltv-L5oMPIs?t=0))
- 94% of buyers use Gen AI as a primary research tool (Forrester 2026, cited by the speaker). ([3:09](https://youtu.be/ltv-L5oMPIs?t=189))
- 67% of B2B buyers prefer a rep-free experience during the decision. ([4:09](https://youtu.be/ltv-L5oMPIs?t=249))
- 80% of deals go to vendors already on the buyer's pre-contact list (speaker's figure). ([4:09](https://youtu.be/ltv-L5oMPIs?t=249))
- Only 17% of total buying time is spent talking with potential vendors. ([4:09](https://youtu.be/ltv-L5oMPIs?t=249))
- In his internal dashboard, the system identified about 3,000 visitors from about 280 accounts; IT is a top visiting vertical. The time window is not stated. ([17:49](https://youtu.be/ltv-L5oMPIs?t=1069))
- Over a few recent days, about 100 people visited the site via LinkedIn, from 73 companies, engaging with 8 recent posts. ([17:49](https://youtu.be/ltv-L5oMPIs?t=1069))
- Visitor identification tools are about 70%+ accurate at company level and only about 15% to 20% accurate at individual level. ([22:44](https://youtu.be/ltv-L5oMPIs?t=1364))
- Reps abandon AI drafts when editing takes longer than about 30 seconds. ([22:44](https://youtu.be/ltv-L5oMPIs?t=1364))

## Hot takes
- Bolting AI onto an existing GTM stack is itself a hindrance to scale.
- A generic 'How can I help you?' chat opener moves late-stage buyers backwards and makes them leave.
- Person-level identity from visitor-ID tools is so weak (15 to 20%) that it is a structural limit, not a tuning problem.
- If editing an AI-written email takes more than about 30 seconds, the initiative is dead.

## Tools mentioned
HubSpot, Slack, LinkedIn

## Relevance to our work
- **agentos** (1/3): Stage-by-stage audit of a multi-agent pipeline (which agent dropped or changed a record) maps loosely to AgentOS's audit and governance pillars. The GTM domain is unrelated. → *Consider a per-stage audit view for multi-agent runs, showing which step dropped or changed each record, if the Merkle audit log lacks step-level detail.*
- **prosharness** (1/3): Multi-stage agent chains that need a human to find and fix a broken stage fit ProsHarness's checkpoint and approval themes, but the talk gives no concrete harness mechanics. → *Consider letting a single failing stage of a ProsHarness multi-stage run be re-run from its checkpoint, without restarting the whole run.*
- **general** (1/3): Entity resolution appears only as vendor identity matching at about 70% company and 15-20% person accuracy, and as dedupe before match. No matching method is described. → *Use the reported company versus person accuracy gap as a reminder to report per-entity-type match metrics in ER evaluations.*
