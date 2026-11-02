# Why building eval platforms is hard — Phil Hetzel, Braintrust

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `_fQ7Z_Wfouk` · [watch](https://youtu.be/_fQ7Z_Wfouk) · **date:** 2026-05-18 · **length:** 25:39 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Phil Hetzel · **orgs:** Braintrust
- **topics:** evals, observability, data-engineering · **tags:** eval-platform, tracing, flywheel, online-evals, failure-modes, scoring-functions, unknown-unknowns, topic-modeling, headless-evals, full-text-search, large-spans, rbac, data-masking, ai-gateway-tracing, playground

> Braintrust's Phil Hetzel on why eval platforms are a systems problem: the maturity path from spreadsheets to tracing plus online evals, and why agent traces break ordinary data stacks.

## Summary
Phil Hetzel, solutions engineering lead at Braintrust, argues that agent evals and agent observability are the same systems problem, and that building the UI is the easy part. He walks through four maturity stages: a spreadsheet with a for loop, a bespoke UI on a real database, a playground for non-technical users to tweak agent configs, and finally tracing plus online scoring on production traffic. The core loop is to pull production traces back into offline evals, fix the agent, and repeat. Agent traces are very large, semi-structured and high-velocity, with spans seen at 10 to 20 MB against a typical few KB, so they need both low-latency ingestion and aggregate or full-text analytics. He says the common stitched-together setup (open-source warehouse, a custom query language, DuckDB in the browser) stopped working at scale. He also notes growing demand for headless evals driven by coding agents over SQL, topic modeling to find unknown unknowns, and platform concerns like RBAC, data masking and automatic tracing through a gateway. The talk is conceptual and he says he was asked not to make it a sales pitch.

## Key ideas
- **Evals and observability are one systems problem** — Pre-production evals and production observability use the same underlying data problem. Production traces feed offline evals, offline fixes go back to production, and this loop should run for the agent's whole life. ([14:21](https://youtu.be/_fQ7Z_Wfouk?t=861))
- **Maturity path: spreadsheet, then bespoke UI, then playground, then tracing** — Teams start with a spreadsheet and a for loop over input examples, which is documenting rather than experimenting. Next come a bespoke UI and a real database, then a playground where non-technical users can change agent parameters such as the system prompt and compare runs, then tracing and logging with online scoring. ([7:58](https://youtu.be/_fQ7Z_Wfouk?t=478))
- **Good scoring comes from failure modes found in production traces** — The best way to write evals is to list how the agent can fail and write scoring functions for each failure mode. Production trace data is the best source for finding those failure modes. ([13:11](https://youtu.be/_fQ7Z_Wfouk?t=791))
- **Agent traces are a different data shape from normal app traces** — They are semi-structured or unstructured, text-heavy, very large and high-velocity. Spans run 10 to 20 MB against a typical few KB, so putting a large trace in a single Postgres row causes performance trouble. ([16:55](https://youtu.be/_fQ7Z_Wfouk?t=1015))
- **A stitched stack fails on text-heavy analytics** — The earlier design used a low-latency ingest store, a separate analytics warehouse, a custom query language and DuckDB in the browser. It broke down for full-text search across big unstructured traces, which the speaker says the usual tools are not built for. ([18:15](https://youtu.be/_fQ7Z_Wfouk?t=1095))
- **Headless use: coding agents query the eval data** — Many users don't want the UI at all. They want Codex or Claude Code to pull aggregate eval data with plain SQL and improve the agent, so the data backend must support ad-hoc SQL. ([20:56](https://youtu.be/_fQ7Z_Wfouk?t=1256))
- **Find unknown unknowns with topic modeling and build for agents too** — Rather than making engineers read traces one by one, cluster traces by topic to show how users actually use the agent. Also design the platform for agent consumers, and add auto-tracing through an AI proxy or gateway so tracing is not optional. ([22:18](https://youtu.be/_fQ7Z_Wfouk?t=1338))

## Techniques
- **Spreadsheet plus for-loop eval starter** — Keep a list of input examples, loop the agent over them, and record outputs and scores in a sheet so each change to the agent can be compared. *When:* Day one, before any platform exists. Expect it to become documenting rather than experimenting as it grows.
- **Playground for non-technical experimentation** — Expose selected agent parameters (for example the system prompt) in a UI, run two configurations through the same evals, and compare the bubbled-up scores. The agent can run outside the eval platform. *When:* When domain experts and non-engineers need to iterate on agent behaviour.
- **Failure-mode-driven scoring functions** — Mine production traces for how the agent actually fails, turn each failure mode into a scoring function, then run those scorers offline. *When:* Once real production traces exist and eval coverage is ad hoc.
- **Online evals on the trace stream** — Point the same scoring functions at live observability traffic and alert on score changes. *When:* When tracing is in place and you want continuous quality monitoring.
- **Production-to-offline loop** — Pull real production examples back into an offline dataset, evaluate the candidate fix against them, ship, and repeat. *When:* As the standing improvement cycle for any production agent.
- **Topic modeling over traces** — Cluster traces by topic to show the main usage patterns and where engineering time should go. *When:* When trace volume is too large for people to review one at a time.
- **Automatic tracing through an AI proxy or gateway** — Route LLM calls through a gateway that attaches tracing centrally, so no caller can skip it. Governance policy can also be applied there. *When:* When tracing must be complete and enforced across many teams or agents.

## Numbers
- Typical trace span is a couple of KB; the speaker has seen spans of 10 to 20 MB ([19:34](https://youtu.be/_fQ7Z_Wfouk?t=1174))
- Customer ran an offline eval roughly every hour over piped production traffic, which led Braintrust to add production tracing (company started as evals-only about 3 years earlier) ([14:21](https://youtu.be/_fQ7Z_Wfouk?t=861))
- Illustrative only: a 1 GB trace stored as one Postgres row is given as an example of a performance problem, not a measured result ([16:55](https://youtu.be/_fQ7Z_Wfouk?t=1015))

## Hot takes
- Vibe-coding the eval UI is easy; the data layer for traces is the hard part.
- A spreadsheet of eval results is documentation, not experimentation.
- Evals are a systems problem, not a UI problem.
- Headless eval access for coding agents may matter more than the dashboard.

## Tools mentioned
Braintrust, Postgres, Neon, DuckDB, Google Sheets

## Relevance to our work
- **agentos** (2/3): AgentOS already plans trace-based observability and ClickHouse or DuckDB analytics. The talk's point that large, text-heavy spans break simple stores applies directly to the L3 storage plan. → *Benchmark the trace path with spans of 10 MB or more and full-text search over them before choosing the L3 analytics store.*
- **prosharness** (1/3): Checkpointed Claude Code runs produce per-step records. Storing them so that a headless SQL query can grade them is a light version of the talk's headless-eval idea. → *Consider logging each ProsHarness checkpoint step to a queryable table so runs can be scored later.*
- **general** (1/3): Recurring interest in evals for agents. The production-trace to offline-eval loop and failure-mode scorers are a usable spec for that work. → *Read Braintrust's blog on the topic-modeling and unknown-unknowns approach referred to in the talk, if the link can be found.*
