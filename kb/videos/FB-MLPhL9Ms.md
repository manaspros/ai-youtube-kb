# The maturity phases of running evals — Phil Hetzel, Braintrust

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `FB-MLPhL9Ms` · [watch](https://youtu.be/FB-MLPhL9Ms) · **date:** 2026-06-18 · **length:** 18:34 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Phil Hetzel · **orgs:** Braintrust, KPMG, Slalom Consulting
- **topics:** evals, observability, testing-verification · **tags:** eval-maturity, llm-as-judge, human-annotation, failure-modes, production-traces, flywheel, trace-evals, state-replay, vibe-checks

> Phil Hetzel (Braintrust) lays out four maturity stages of agent evals, from documented vibe checks to replaying tool-using agents offline with captured system state.

## Summary
Phil Hetzel, solutions engineering lead at Braintrust, gives an 18-minute talk on how teams mature in running evals for agents. He argues evals are not unit tests: start from high-level failure modes, accept directional results from non-deterministic judges, and avoid trying to enumerate every failure. The four stages are vibe checks with documented human annotation, scaling human judgment into LLM-as-judge scorers, evaluating whole traces once agents call external tools, and advanced replay that restores external system state. The core loop is a production flywheel: capture traces, triage failures by hand or with tooling, then replay them offline through evals. For tool-using agents, he suggests embedding system state inside large traces, using mocked APIs, and running time-versioned queries such as vector DB as-of-time lookups. He presents the stages as a continuum rather than fixed steps, and says the last two techniques are still emerging. The talk is conceptual, with little product detail and no benchmarks.

## Key ideas
- **Evals are not unit tests** — Start from the high-level failure modes of the agent, as a subject matter expert would describe them. Exhaustive enumeration of everything that could go wrong is infinite and blocks shipping. ([3:47](https://youtu.be/FB-MLPhL9Ms?t=227))
- **Directional eval results are acceptable** — Eval results need not be perfect, especially with non-deterministic LLM judges. A consistent upward trend is what matters. An eval is three parts: the task under test, a dataset of inputs, and scoring functions. ([5:07](https://youtu.be/FB-MLPhL9Ms?t=307))
- **Vibe checks are a fine start if documented** — Run about 10 example inputs and have a human (ideally a subject matter expert) give a thumbs up or down plus a written justification. The justification captures domain knowledge that can later be scaled. ([6:28](https://youtu.be/FB-MLPhL9Ms?t=388))
- **Derive failure modes from the justifications** — Feed thumbs-down justifications into a coding agent to cluster them into the agent's actual failure modes. This makes the failures explicit enough to score automatically. ([9:31](https://youtu.be/FB-MLPhL9Ms?t=571))
- **LLM judges need their own validation, and code can judge too** — Do not trust an LLM judge just because it is an LLM; check its agreement with humans. Objective failures such as too many tool calls or tokens can be scored with plain code instead. ([10:31](https://youtu.be/FB-MLPhL9Ms?t=631))
- **Production traces feed back into the eval set (the flywheel)** — Capture production traces, understand what went wrong (by human or tooling), bring those examples offline, rerun them through evals, and use the results to decide what to improve. Evals are framed as re-running production, not as tests. ([11:44](https://youtu.be/FB-MLPhL9Ms?t=704))
- **Agents with tools need whole-trace evals** — Once an agent calls external systems, scoring the final output is not enough. Context-gathering tools and CRUD tools both affect quality, so you must inspect each step and target individual tool or MCP calls. ([13:10](https://youtu.be/FB-MLPhL9Ms?t=790))
- **Replaying CRUD tools offline is the hard part** — Replaying needs the external system state from the time of the original run, and writes must not touch production data. Mock-level APIs can approximate this, but he says the problem is not fully solved. ([14:36](https://youtu.be/FB-MLPhL9Ms?t=876))
- **Store state inside arbitrarily large traces and query as of a point in time** — Because agent traces can be very large, system state can be packed into the trace and injected into the eval task. Where systems support it, timestamp or version queries (for example, a vector DB queried as of the original run) recreate the old state. ([15:50](https://youtu.be/FB-MLPhL9Ms?t=950))

## Techniques
- **Documented human annotation (thumbs plus justification)** — For each trace, a human gives a binary verdict and a written reason. Build the annotation view to match how users expect agent traces to look, rather than using a generic annotation UI. *When:* Very early, before any automation, when you have no labels and a few dozen inputs.
- **Failure-mode extraction from justifications** — Pass the thumbs-down justifications to a coding agent (Cursor, Claude Code, or Codex) and cluster them into named failure modes. Use those modes as the basis for scoring rules. *When:* After you have enough annotated failures and need to scale judgment beyond a few experts.
- **LLM-as-judge with binary outputs and human-aligned ground truth** — Use an LLM judge scorer with discrete (yes/no) outputs so a ground-truth dataset is easy to build. Check the judge against human labels before trusting it. *When:* When human review is the bottleneck and failures can be stated as clear criteria.
- **Deterministic code scorers for objective failures** — Write code checks for measurable failures, such as tool-call count or token budget, and fail the eval directly. *When:* When a failure can be measured without judgment, which is cheaper and more reliable than an LLM judge.
- **Production trace flywheel** — Capture production or UAT traces into the eval dataset, triage them, and replay them through offline evals to guide changes. *When:* Once the agent is live or near launch, to keep evals tied to real usage.
- **Whole-trace evaluation with per-step targeting** — Capture full traces with every tool and MCP call. Set evals on individual steps as well as on the final output. *When:* When the agent calls external tools or systems and final-output checks miss errors.
- **Embedding system state in traces and time-versioned queries** — Store the external state the agent saw inside the trace and inject it on replay. Use mock APIs for writes. Where supported, query stores such as vector DBs as of the original timestamp. *When:* When an eval must replay tool-using tasks offline without touching production data.

## Numbers
- Talk length of 18 minutes (18:34 recording) with about 2 minutes reserved for questions. ([0:00](https://youtu.be/FB-MLPhL9Ms?t=0))
- Starting point suggested: about 10 example inputs run through the agent for vibe checking before annotation. ([6:28](https://youtu.be/FB-MLPhL9Ms?t=388))
- Speaker has 12 years of consulting and systems implementation experience (4 at KPMG, 8 at Slalom), and about 1 year at Braintrust at recording time. ([1:00](https://youtu.be/FB-MLPhL9Ms?t=60))
- Four maturity stages: just getting started, measuring to manage, accounting for complexity, advanced eval techniques. He describes them as a continuum rather than discrete steps. ([6:28](https://youtu.be/FB-MLPhL9Ms?t=388))

## Hot takes
- Evals are not unit tests, and trying to enumerate every failure is infinite and blocks shipping.
- Vibe checking is fine as a start, as long as it is documented with justifications.
- Generic annotation tools are a mistake. Build annotation views specific to each user's traces.
- An LLM judge is not more trustworthy just because it is an LLM. Judges need their own evals.
- Agent traces can be arbitrarily large, so system state can be packed into the trace to replay offline.

## Tools mentioned
Braintrust, Cursor, Claude Code, Codex

## Relevance to our work
- **agentos** (2/3): AgentOS already plans RAGAS evals and L4 observability. The talk's trace-capture and replay ideas map to evaluating Crucible and MemoryMesh tool calls offline. → *Add per-step tool-call capture in the proxy traces, and record external-state snapshots so that a stored task can be replayed in an eval without touching live systems.*
- **prosharness** (1/3): ProsHarness runs plan, critique, and debate loops. Human thumbs plus justification on plan critiques could give the labels needed to derive failure modes. → *Log a verdict and a one-line reason for each plan critique, then cluster the reasons to find the recurring plan failures.*
- **general** (1/3): Entity resolution and data-quality work benefits from the same pattern: deterministic checks first, LLM judge only where needed, with the judge calibrated against human labels. → *For entity-resolution eval sets, store a reason with each match label, and calibrate any LLM judge against those labels before using it to score rules.*
