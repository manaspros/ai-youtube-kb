# Let Your Agent Cook: Using Skills to Evaluate and Improve Your App — Ankur Duggal, Arize AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `_zUp6y9bDU8` · [watch](https://youtu.be/_zUp6y9bDU8) · **date:** 2026-10-12 · **length:** 36:04 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Ankur Duggal · **orgs:** Arize AI
- **topics:** evals, observability, coding-agents, skills-self-improvement · **tags:** trace-driven evals, LLM-as-judge, agent debugging, experiments, failure triage, Arize, Phoenix, Claude Code skills, production monitoring

> Arize's Ankur Duggal argues agents need trace-based evals, then demos a coding agent (Claude Code plus Arize skills) turning production traces into failure analysis, datasets, evaluators and experiments.

## Summary
The speaker argues that teams shipping agents on vibes cannot find failures without traces, since agent control flow is decided at runtime and is invisible in the code. He lays out a manual improvement loop (find failures, sample them into a dataset, add guardrails or evaluators, run experiments, ship, repeat) and says a coding agent with CLI access to the trace platform, evals, annotations, APM and the codebase can run most of it. In a live demo, Claude Code analysed a financial advice agent that wrongly recommended a stock, and reported bad summaries, fabricated answers, redundant tool calls and silent tool failures. The agent then built a dataset and experiments for a cross-market stock bug, going from a 0% baseline to about 90% over three iterations. He stresses that evals should be tailored to your own agent, that judge models can differ from production models, and that evals keep working after model or query drift. The talk is a vendor demo (Arize AX and open-source Phoenix) with little hard data, and the speaker admits the demo agent was run with permissions skipped.

## Key ideas
- **Evals have to sit on traces, because agent behaviour is decided at runtime.** — Unlike deterministic code paths that APM can follow, an agent's tool choice and steps only show up in traces. Without them you cannot tell where it broke, so vibe-checking input and output does not scale to production. ([1:18](https://youtu.be/_zUp6y9bDU8?t=78))
- **The improvement loop starts from production failures and ends with experiments.** — Take the failing traces, sample them into a dataset, decide whether the fix belongs in the prompt, a guardrail or the tool, add an evaluator to check that the fix works, run an experiment, then ship and repeat. Done by hand it takes hours or days. ([4:08](https://youtu.be/_zUp6y9bDU8?t=248))
- **Compress the loop by giving a coding agent CLI and skills access to every data source.** — The coding agent gets traces, evals, human annotations, APM data and the codebase, plus skills for datasets, evaluators and experiments. It can then find failing spans, diagnose them and propose code changes, not just edit prompts. ([6:58](https://youtu.be/_zUp6y9bDU8?t=418))
- **The demo agent's failures came from a mix of evals and the agent's own analysis.** — Claude reported about 44% of interactions producing bad summaries, fabricated answers, high rates of redundant tool calls, silent tool failures, and hallucination when a tool failed instead of disclosing it. It also flagged a numeric groundedness problem. ([16:39](https://youtu.be/_zUp6y9bDU8?t=999))
- **Fixes should be tested against the spans that failed, and iteration is expected.** — For a cross-market stock question, the baseline built from production traces scored 0%. A quick country-name normalisation did not help because the tool was outdated. A third iteration after the tool update reached about 90%. ([20:22](https://youtu.be/_zUp6y9bDU8?t=1222))
- **Pair code-based and LLM-as-judge evaluators, and let the judge use a different model.** — A code-based evaluator failed to set up in the demo, so an LLM judge was built instead. The speaker says the judge can be a stronger or different model from the one in production, since the agent is only as good as its evals. ([23:04](https://youtu.be/_zUp6y9bDU8?t=1384))
- **Generic out-of-box evals and public benchmarks tell you little about your own agent.** — Templates such as bad summary or healthy agent catch broad issues. Choosing the right eval model for your use case means running your own analysis, because benchmarks may not reflect your agent or domain. ([33:30](https://youtu.be/_zUp6y9bDU8?t=2010))
- **Evals are for monitoring drift after the fix, not just for finding bugs once.** — A skill that fixes summaries can degrade later through model regressions or changing user query patterns, so evals keep watching the same failure modes. ([26:58](https://youtu.be/_zUp6y9bDU8?t=1618))
- **Coding agents tend to fixate on minor issues such as lint, so grounding them in trace evidence matters.** — The speaker says that when the agent sees the actual wrong tool call in the trace, it works on the real failure rather than cosmetic code problems. ([28:12](https://youtu.be/_zUp6y9bDU8?t=1692))

## Techniques
- **Trace-to-dataset-to-experiment loop** — Pull the failing production spans into a dataset, record a baseline run (expect it to fail), make a candidate fix, rerun the experiment against those spans, and check the pass rate before shipping. *When:* After a production failure, to turn a bug into a regression test before changing the agent.
- **Coding agent as eval workflow driver** — Install the platform CLI and skills, create a profile that points at the trace store, then ask the coding agent to pull spans, analyse failures, draft evaluators and set up experiments. The skills call the CLI or API for datasets, evaluators and experiments. *When:* When traces already live in an observability platform and you want an agent to propose the evals and fixes.
- **Mixed evaluator set** — Use deterministic code checks for things like tool-call correctness, redundancy or empty responses. Use LLM-as-judge for semantic checks such as summary quality and numeric grounding, with a prompt that reads the full agent context. *When:* When a failure mode is partly mechanical and partly semantic, and one evaluator type is not enough.
- **Sampled online evals** — Run evaluators on a sample of traces and on a focused subset of calls, not on every call, and track evaluator token cost from the trace history. *When:* When continuous monitoring would be too expensive at full traffic.
- **Tailored evals from observed failures** — Let the agent read real traces and annotations, then write evaluators for the failure modes it finds, rather than starting from a generic eval template. *When:* When the agent is domain-specific and out-of-the-box evals give generic scores.

## Numbers
- About 44% of agent interactions in the demo produced a bad summary, per the coding agent's analysis of existing evals. ([16:39](https://youtu.be/_zUp6y9bDU8?t=999))
- Cross-market stock question: baseline pass rate 0%, third iteration about 90% success. ([20:22](https://youtu.be/_zUp6y9bDU8?t=1222))
- Automated trace-analysis and fix run took about 14 minutes. ([32:00](https://youtu.be/_zUp6y9bDU8?t=1920))
- Speaker's audience poll: many attendees ship on vibes; fewer have evals; few have full eval coverage. ([0:12](https://youtu.be/_zUp6y9bDU8?t=12))

## Hot takes
- Shipping agents on vibes is not shippable, because you cannot see where production breaks without evals on top of traces.
- Out-of-the-box evals give out-of-the-box results; custom evals are needed for agents built for one use case.
- Benchmarks are not the right way to choose an eval model; you have to test which LLM judges your own agent well.
- Coding agents will fix a bad agent faster than a human, but a human still has to check the fix did not just change lint.

## Tools mentioned
Arize AX, Phoenix, Claude Code, Codex, Cursor

## Relevance to our work
- **agentos** (2/3): AgentOS has an observability layer and SkillForge, which mines agent telemetry into skills. The trace-to-dataset-to-experiment loop and the evaluator design map straight onto that path. → *Build a failing-span dataset from AgentOS's own traces, run candidate fixes against it, and compare Phoenix (open-source Arize) as a trace backend before writing one.*
- **prosharness** (2/3): ProsHarness wraps Claude Code and already does checkpoint/resume and critique. A skill that pulls a failed run's trace and eval results into a regression set before resuming would fit the harness. → *Prototype a ProsHarness skill that turns a failed run's trace into a regression case and reruns the fix against it before the run resumes.*
