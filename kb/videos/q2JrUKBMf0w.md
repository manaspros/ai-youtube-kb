# The Future of Evals: From LLM as a Judge to Agent as a Judge — Aparna Dhinakaran, Arize AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `q2JrUKBMf0w` · [watch](https://youtu.be/q2JrUKBMf0w) · **date:** 2026-08-18 · **length:** 6:06 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Aparna Dhinakaran · **orgs:** Arize AI, Anthropic, OpenAI, Uber, Snorkel
- **topics:** evals, observability, agent-architecture · **tags:** agent-as-judge, llm-as-judge, trace-analysis, online-evals, failure-modes, stuck-loops, vendor-pitch, arize-signal

> Arize's founder argues that evals must add a third layer, agent-as-a-judge, that reads production traces, finds failure patterns, and can open fix PRs. It is a short vendor pitch with little method detail.

## Summary
Aparna Dhinakaran of Arize AI argues that eval practice has to change as agents change. Early evals scored single prompt answers, but agents now use tool calls, reasoning, deep research and long-horizon sub-agents, so their failures are different. She says Arize's own agent, Alex, forgot context, did not know when a task was finished, and got stuck in loops, which fixed-rubric LLM-as-a-judge evals did not catch. She describes three eval types: deterministic checks, LLM-as-a-judge with a fixed rubric, and agent-as-a-judge with adaptive analysis. Her claim is that most teams do the first two and should add the third. She says Arize's agent, Signal, reads traces, finds patterns such as the same tool being called repeatedly, and can open a PR with a fix. The talk gives no methodology, benchmarks or failure-rate data, and most of it promotes the product.

## Key ideas
- **Agent failures changed as agents changed** — Evals built for single prompt answers miss failures from tool calls, reasoning, deep research and long-horizon sub-agent loops. The failures are more complex and less predictable. ([1:37](https://youtu.be/q2JrUKBMf0w?t=97))
- **Fixed-rubric LLM-as-a-judge missed the failures Alex had** — Alex forgot context, did not know when a task was done, and looped. Classic LLM-as-a-judge evals were not enough, because each run follows a different trajectory and a fixed rubric cannot describe it. ([2:37](https://youtu.be/q2JrUKBMf0w?t=157))
- **Three eval layers instead of two** — Deterministic checks, LLM-as-a-judge with fixed rubrics, and agent-as-a-judge with adaptive analysis. The speaker says most teams use the first two and should add the third. ([3:35](https://youtu.be/q2JrUKBMf0w?t=215))
- **Evaluate production traces, not only offline test sets** — The speaker says the useful data comes from evals run on live production traces, which show what works and what fails. That data then feeds continual-learning loops. Offline and online evals each have a place. ([0:12](https://youtu.be/q2JrUKBMf0w?t=12))
- **An agent judge can find subtle loop failures and propose fixes** — Signal found an inefficient trajectory in which the same tool was called many times in a row. Because it has this analysis, it can open a PR with a fix. ([4:53](https://youtu.be/q2JrUKBMf0w?t=293))

## Techniques
- **Agent-as-a-judge over traces** — Run a long-lived agent over logged traces to discover failure patterns that a fixed rubric cannot express, then have it summarise them or propose a code fix as a PR. *When:* When agent trajectories vary a lot between runs and fixed-rubric judges miss failures such as loops, wasted tool calls or lost context.
- **Three-layer eval stack** — Combine deterministic checks, LLM-as-a-judge rubric scoring, and an adaptive agent judge. Each layer catches a different kind of failure. *When:* When a team already runs basic evals and needs to catch failures that only appear across a whole trajectory.
- **Trace-driven online evals** — Attach evaluators to traces from the live agent and treat the scores as signal for what to fix, not only as a pre-release gate. *When:* When the agent runs in production and failures show up only with real user traffic.
- **Repeated-tool-call loop detection** — Look for the same tool called many times in one trajectory as a cheap signal of inefficiency or getting stuck. The speaker gives this as an example of what the agent judge found. *When:* For long-horizon agents that sometimes cycle without making progress.

## Numbers
- Arize runs over 100 million evals per month ([0:12](https://youtu.be/q2JrUKBMf0w?t=12))
- The average team runs about 12 different eval jobs, and the top teams run over 3,800 evaluators ([0:12](https://youtu.be/q2JrUKBMf0w?t=12))

## Hot takes
- Most teams doing agent evals today only use deterministic checks and LLM-as-a-judge, and the third layer, agent-as-a-judge, is the future of evals.
- Classic LLM-as-a-judge evals are not enough for agents whose trajectories differ on every run.

## Tools mentioned
Arize Signal, Agent as a Judge (Arize)

## Relevance to our work
- **agentos** (1/3): AgentOS has RAGAS evals and OTel observability. The talk suggests trace-level judging for loops and wasted tool calls, but gives no method. → *Add a loop/repeated-tool-call check over AgentOS run traces and compare it with the RAGAS scores, to see whether trace-level signals catch failures that RAGAS misses.*
- **prosharness** (1/3): ProsHarness runs long Claude Code sessions and checkpoints them. The talk's stuck-loop case matches that workload, but the talk offers no concrete design. → *Read the Arize Signal/agent-as-judge write-up or docs, if one exists, to see how a judge reads run traces and whether that pattern could flag stuck runs for checkpoint or resume decisions.*
