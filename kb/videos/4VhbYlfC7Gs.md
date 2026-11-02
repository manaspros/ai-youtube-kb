# Malleable Evals: Why Are We Evaluating Adaptive Systems with Static Tests? — Vincent Koc, OpenClaw

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `4VhbYlfC7Gs` · [watch](https://youtu.be/4VhbYlfC7Gs) · **date:** 2026-05-18 · **length:** 15:05 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Vincent Koc · **orgs:** Comet, OpenClaw
- **topics:** evals, agent-architecture, observability · **tags:** malleable evals, intent engineering, eval calcification, always-on evals, trace-based eval curation, telemetry in the loop, autoresearch, static benchmarks, agent harness

> Vincent Koc (Comet, OpenClaw) argues static, hand-written evals don't fit adaptive agents; he proposes intent-based, always-on evals self-curated from traces, with the eval suite treated as living code.

## Summary
Koc opens by saying "evals are dead" is a joke with some truth: agentic systems change over time, but benchmarks stay static. He contrasts software engineering practice (unit tests, regression suites, CI/CD, chaos engineering, observability) with AI evaluation, which he says relies on handcrafted offline test sets. He argues agents now adapt (he cites OpenClaw, where the harness changes itself), so tests must adapt too. His proposal is intent-based outcome evals: define the end state rather than a fixed dataset, self-curate suites from production traces, run evals as an always-on service, and feed telemetry back into the harness so it can self-correct. He calls the drift problem "eval calcification" and says the unpredictable tail of usage is what hurts businesses. He closes by saying evals should be treated as software or a living agent, not a point-in-time dataset. The talk is conceptual: he says the Comet implementation is unfinished and avoided a sales pitch, and no benchmarks or results are shown.

## Key ideas
- **Static, handcrafted benchmarks cannot keep up with adaptive agents; teams have offline evals but no chaos-style layer that probes how the system breaks.** — He says offline evals cycle through handcrafted test sets before deploy, and that teams end up with large benchmark sets that still do not explain production failures. ([2:32](https://youtu.be/4VhbYlfC7Gs?t=152))
- **Harnesses now change themselves, so evals have to change with them.** — He cites OpenClaw, where the harness shifts as skills are added, and an adaptive-testing paper that selects tests more sparingly. Benchmarks should track the application. ([3:49](https://youtu.be/4VhbYlfC7Gs?t=229))
- **Prompt, context and tool-calling eras each made evals more tractable, but intentful agents make them harder.** — Decomposing agents into tools made evals steerable. Agents that adapt to each user mean one user's experience differs from another's, which widens the eval problem. ([6:32](https://youtu.be/4VhbYlfC7Gs?t=392))
- **Replace the dataset-as-starting-point with an end state the system optimizes toward (intent engineering).** — Evals become the defined end state; rubrics can express ambiguity and personality, and the agent does the work. He compares this to Karpathy's autoresearch: set a goal and a reward signal and let the loop tune itself. ([12:07](https://youtu.be/4VhbYlfC7Gs?t=727))
- **Self-curate eval suites from production traces and run evals always-on.** — Most traffic is repetitive, but the customer mix shifts. Watching traces for drift and having agents regenerate suites makes evaluation a continuous loop, not a one-time benchmark run. ([10:41](https://youtu.be/4VhbYlfC7Gs?t=641))
- **Telemetry in the loop: let the harness read errors, cost and conditions so it can self-correct.** — He describes a paper he wrote on this. The harness watches what is breaking and what it costs, so it can fix or continue from errors instead of predicting failures in advance. ([10:41](https://youtu.be/4VhbYlfC7Gs?t=641))
- **The unpredictable tail (about 20% by his estimate) is what breaks a business; keep the common 80% static and monitor the rest.** — Odd questions and unusual usage are the failure source. He recommends agents that maintain and watch that tail, then adapt the evals to it. ([13:31](https://youtu.be/4VhbYlfC7Gs?t=811))

## Techniques
- **Intent-defined end-state evals** — Write evals as the desired end state plus a reward or rubric (for ambiguity, tone, personality) rather than fixed input/expected-output pairs. Let an optimization loop search toward that target. *When:* Agent behavior is ambiguous or personalized, so exact-match expected outputs do not apply.
- **Trace-driven suite self-curation** — Trace production agent runs, cluster recurring patterns, detect distribution shifts, and have an agent turn new or drifting traces into eval cases. *When:* The user population or usage changes over time and handcrafted datasets go stale.
- **Always-on eval service** — Run evals continuously against live traces, not only as a pre-deploy offline pass, and alert when behavior changes. *When:* You need to catch drift in production instead of after an incident.
- **Telemetry-aware harness** — Expose error, cost and failure telemetry to the agent harness, with explicit conditions it can act on to retry, correct or stop. *When:* You want the agent to self-correct from runtime signals, not just log them for humans.
- **Split static and dynamic evals** — Hold the common, well-understood behavior in a static, intent-defined suite, and put continuous monitoring and adaptive tests on the long tail. *When:* Planning eval coverage for a system with a long tail of unusual usage.

## Numbers
- Speaker's rough heuristic: about 80% of agent behavior is predictable and about 20% changes and drives failures. This is an estimate, not a measured result. ([13:31](https://youtu.be/4VhbYlfC7Gs?t=811))

## Hot takes
- Evals are not dead, but static benchmarks and handcrafted offline datasets are inadequate for adaptive agents.
- Evals should be treated as living software that agents maintain; the defined end state matters more than the starting dataset.
- Frames drift in the tail of usage ('eval calcification') as the core failure mode.
- The talk is conceptual: the speaker says the Comet implementation is unfinished and avoided a sales pitch; no benchmarks or results are shown.

## Tools mentioned
Comet, OpenClaw, Claude, Codex, MCP, Karpathy autoresearch

## Relevance to our work
- **agentos** (2/3): AgentOS has RAGAS evals and a gateway that sees all traffic; trace-driven eval curation and always-on evaluation map onto its eval and observability pillars. → *Prototype a trace-to-eval-suite job: sample gateway traces from the audit log, cluster them, and propose new RAGAS test cases when the input distribution shifts.*
- **prosharness** (2/3): Telemetry-in-the-loop, where the harness reads errors and cost to self-correct, fits ProsHarness's checkpoint, resume and loop design. → *Add a per-step telemetry record (errors, cost) to ProsHarness runs and test whether a retry or stop rule based on it improves long-run outcomes.*
