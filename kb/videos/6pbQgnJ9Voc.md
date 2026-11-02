# Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `6pbQgnJ9Voc` · [watch](https://youtu.be/6pbQgnJ9Voc) · **date:** 2026-09-18 · **length:** 18:49 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Jeffrey Wang · **orgs:** Exa, Cursor, Cognition, Salesforce, Palantir
- **topics:** enterprise-adoption, product-ux, mcp-and-tools, security-guardrails · **tags:** go-to-market, agent-first, api-first, personal-clone-agent, ICP, semantic-web-search, forward-deployed-engineering, caller-scoped-permissions, salesforce-mcp, internal-agents

> Exa's co-founder argues go-to-market is an AI engineering data problem and shows the internal agents, ICP dashboard, and JeffBot clone that run his GTM team.

## Summary
Jeffrey Wang, co-founder of Exa (a web search engine built for agents), argues that go-to-market is a data problem that engineers can solve with AI tooling, and that product and GTM both have to be right. He describes Exa's internal stack: an ICP dashboard that classifies every company in its addressable market using Exa's own semantic search, RequestLens alerts on customer signals, a dozen shared Slack agents with broad internal data access, and JeffBot, a clone of himself built from his emails and past decisions. His agent-first principles are: be API-first, keep both chat and crystallized UIs, and treat any SaaS as arbitrarily customizable rather than choosing between buying and building. The GTM team uses Salesforce through its MCP server. Permissions depend on the caller: he can read and write through JeffBot, while other callers get draft-only output and a narrower tool set. The Q&A covers how the forward-deployed engineering role emerged and how the GTM team's skills are split.

## Key ideas
- **Go-to-market is a data problem, so treat it as an engineering problem** — GTM covers researching targets, finding the right people at companies, and building POCs. The speaker says the shared thread is data: a live model of your world (internal customer and usage data plus external company, people and news data) that agents can act on. ([3:44](https://youtu.be/6pbQgnJ9Voc?t=224))
- **Product and GTM both have to be right; engineers default to building** — He says a company needs a good product and distribution. Engineers tend to build first and market later, and Exa was weak at marketing and sales early on. ([1:00](https://youtu.be/6pbQgnJ9Voc?t=60))
- **Semantic web search as a classification engine for the market** — Exa crawls the web and trains embeddings on it, so it can filter and slice the world semantically. The team uses this to classify every company in its TAM into segments (for example model providers and AI coding platforms) and to generate a list of potential ICPs with estimated spend. ([5:14](https://youtu.be/6pbQgnJ9Voc?t=314))
- **Customer-signal alerts (RequestLens) so the team can act on events** — Sign-ups, large search volume, drop-offs in usage, and key accounts showing up all trigger alerts that the team can act on. ([6:16](https://youtu.be/6pbQgnJ9Voc?t=376))
- **Shared internal agents with broad data access, used across GTM** — About a dozen agents live in Slack with access to a lot of internal data. Account executives use them to dig into accounts and build demos, and GTM agent spend is very high. ([7:50](https://youtu.be/6pbQgnJ9Voc?t=470))
- **JeffBot: a personal clone built from past artifacts and calibrated with evals** — He analyzed about 760 of his emails to capture his writing voice and turned hundreds of past decisions into a decision framework and evals. He calibrated the agent against those evals, then gave it read and write access to his own data. Others use it to draft Slack messages and emails. ([8:51](https://youtu.be/6pbQgnJ9Voc?t=531))
- **Agent-first means API-first; keep both chat and stable UIs** — Agents need programmatic access to internal and external data, whether through MCP, a CLI, or an API. He argues against chat-only design: dynamic UIs are useful, but a stable, consistent UI for recurring use cases helps people learn a tool over time. ([10:19](https://youtu.be/6pbQgnJ9Voc?t=619))
- **The build-vs-buy choice is a false dichotomy; aim for arbitrary customizability** — A system you build yourself is customizable because you can vibe-code changes. A bought SaaS also works if it can be made to act on your behalf and be customized. He uses Salesforce as a good database exposed through MCP, so agents can use it. ([11:42](https://youtu.be/6pbQgnJ9Voc?t=702))
- **Permissions depend on the caller, not only on the agent** — When he calls JeffBot, it can read and write across systems. When others call it, it can only draft messages and has no access to some MCPs and tools. He says the guardrails are deliberately defined, though not described in detail. ([15:43](https://youtu.be/6pbQgnJ9Voc?t=943))
- **The forward-deployed engineer role merged two jobs into one** — Technical staff who support revenue can now build tooling that makes their own work and the account executives' work easier. He says this used to be split between solutions engineers and AEs. The team is about 115 people, and the speaker reports eight or nine FTEs for the FDE group, which he says probably will not scale to everyone doing everything. ([17:05](https://youtu.be/6pbQgnJ9Voc?t=1025))

## Techniques
- **Decision-log to eval calibration for a personal proxy agent** — Mine past decisions from chat and email history (Slack, email). Extract them as eval cases, then tune the agent's decision framework and voice until it matches those past decisions. Also profile writing style, for example average words per email and sign-off habits. *When:* Building an agent that drafts or decides in one person's place and needs to match their judgment.
- **Caller-scoped agent permissions** — Give the owner full read and write access to the agent's tools. Give other callers a narrower tool set, with draft-only output that a human sends. *When:* A shared internal agent runs with one person's credentials and many people can call it.
- **Semantic web search as a segmentation pipeline** — Use embedding-based web search to classify every company in a market into categories, then enrich each company with metadata and an estimated-spend figure. *When:* Building an ideal-customer-profile list or a market map that has to cover a large number of companies.
- **API/MCP-first, then customize the SaaS** — Expose each internal and external system as an API or MCP server. Keep SaaS tools such as Salesforce as the data layer and customize them so agents can use them, instead of building a replacement CRM. *When:* Deciding whether to build or buy internal tooling, and designing interfaces for agents.
- **Signal-triggered alerts on customer events** — Watch for product events such as sign-ups, search-volume spikes, usage drop-offs, and key accounts appearing. Route each one to the team for action. *When:* Running sales or success workflows where timing matters.

## Numbers
- Exa launched in mid-2023 (post-GPT-4 era). ([3:44](https://youtu.be/6pbQgnJ9Voc?t=224))
- Over 60 million companies and over a billion LinkedIn users in the external data universe. ([3:44](https://youtu.be/6pbQgnJ9Voc?t=224))
- JeffBot analysis covered about 760 of the speaker's emails; he reports an average of 18 words per email. ([8:51](https://youtu.be/6pbQgnJ9Voc?t=531))
- The GTM org is about 115 people; the speaker mentions eight or nine FTEs for the FDE group. ([18:04](https://youtu.be/6pbQgnJ9Voc?t=1084))
- Customers named include Cursor and Cognition. ([0:08](https://youtu.be/6pbQgnJ9Voc?t=8))

## Hot takes
- Go-to-market is a data problem, so engineers should treat it as an AI engineering problem.
- Being agent-first means being API-first.
- Build vs buy is a false dichotomy; infinite customizability is the highest-order bit.
- Not everything should be a chatbot; stable UIs for recurring use cases still matter.

## Tools mentioned
Exa, Opus 4.5, Slack, Salesforce MCP

## Relevance to our work
- **agentos** (2/3): The caller-scoped permission model (owner gets read and write, others get draft-only and a narrower tool set) maps onto AgentOS's policy and budget pillars, which decide what each caller may do. → *Add a per-caller tool and capability scope to the Govrix proxy manifest, with owner and non-owner profiles, and test that non-owner calls cannot reach write tools.*
- **prosharness** (1/3): The decision-log-to-eval idea could calibrate the Codex critic in plan, critique and debate, but the talk is about personal drafting agents, not coding harnesses. → *Read ProsHarness approval history and turn past approve/reject decisions into a small eval set to calibrate the critic stage.*
- **general** (1/3): The talk shows a practical method for building a personal clone agent from past artifacts and evals, which fits the cheap-model pipeline interest. → *Read the JeffBot section as a reference for building a decision-framework eval from past decisions with a Haiku-class model.*
