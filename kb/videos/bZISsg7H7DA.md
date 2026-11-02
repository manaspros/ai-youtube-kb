# Your Agents Need a Save Button - Hamza Tahir, ZenML

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `bZISsg7H7DA` · [watch](https://youtu.be/bZISsg7H7DA) · **date:** 2026-07-18 · **length:** 17:07 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Hamza Tahir · **orgs:** ZenML, DoorDash, Braintrust
- **topics:** agent-architecture, observability, evals · **tags:** checkpointing, replay, counterfactual-evals, durable-execution, trace-analysis, cohort-analysis, model-swap, kitaru, zenml

> Hamza Tahir (ZenML) argues agents need checkpointed runtime state so production runs can be replayed with what-if changes (model swap, mocked tool), compared across cohorts, and shipped only after cohort-level diffs.

## Summary
Tahir says agent traces are disconnected from the runtime, since they record tool calls and I/O but not variables, filesystem state, code, or environment. He proposes a "save button" for agents: checkpoint state at each step so a run can be replayed from any point. Replays let you ask what-if questions such as swapping in a cheaper model or mocking a tool, while holding everything else constant. He presents Kitaru, a ZenML tool that sits below the agent harness, snapshots code, artifacts and environment between tool calls, skips unchanged checkpoints on replay, and gives side-by-side diffs of runs. He argues for a checkpoint, replay, diff, decide loop run over cohorts of real production runs (expensive, slow or risky ones) rather than single replays. In his demo, a cohort analysis by an agent via an MCP server concluded not to ship the cheaper model, even though one replay looked fine. He warns that naive model swaps often look cheaper on paper but hurt task outcomes, and cites a Braintrust study and a tau-bench consistency point to argue that one replay is an anecdote. Claims about DoorDash's simulation results come from the speaker's citation of their blog post and are not verified here.

## Key ideas
- **Traces are not enough for agents** — A trace records tool calls and their inputs/outputs, but it is detached from the runtime: variables, in-flight filesystem, code and decisions are lost. The speaker says the missing piece is a clear link between observability spans and the actual execution. ([0:00](https://youtu.be/bZISsg7H7DA?t=0))
- **A save button makes agent runs replayable** — Persistent checkpoints of agent state let you go back in history and ask what-if questions (swap the model, mock a tool, degrade a tool on purpose). These questions are impossible without captured state. ([1:00](https://youtu.be/bZISsg7H7DA?t=60))
- **Production already contains the data needed for improvement** — If the runtime checkpoints state, production traces plus checkpoints allow replay-based evaluation on real runs. The speaker frames this as closing the loop: checkpoint, replay, diff, decide. ([2:30](https://youtu.be/bZISsg7H7DA?t=150))
- **Checkpoints snapshot code, artifacts and environment, not just tool I/O** — In the Kitaru demo, clicking a checkpoint shows the configuration, code, artifacts in and out, and the environment (Docker image or sandbox). Replay starts from a chosen checkpoint and skips earlier ones because their state is already stored. ([5:19](https://youtu.be/bZISsg7H7DA?t=319))
- **Replay from a point, change one thing, hold the rest constant** — Changing the model at one checkpoint re-runs only the later steps. Mocking a tool with a code function gives a controlled counterfactual. A side-by-side diff of baseline and forks shows where the runs diverge and what decisions changed. ([6:47](https://youtu.be/bZISsg7H7DA?t=407))
- **Use cohorts, not single replays** — Replaying across many runs (sorted by cost, length or risk) gives a distribution. The speaker says a single replay is an anecdote and that a cheap-model swap often looks good on one dimension while failing on outcomes. ([11:14](https://youtu.be/bZISsg7H7DA?t=674))
- **Naive model swaps can be a false economy** — A cheaper model can look better on cost and latency alone while the support bot stops resolving requests. Cite a Braintrust study for this. The decision should weigh cost against value created. ([14:07](https://youtu.be/bZISsg7H7DA?t=847))
- **Playbook: real runs, cohorts, human at the end** — Start from real checkpointed production runs, build cohorts that matter, replay at scale, diff, and only then route, hold or ship. Automate the loop where possible, with a human approving the final ship decision. ([15:35](https://youtu.be/bZISsg7H7DA?t=935))

## Techniques
- **Per-step checkpointing of agent state** — Snapshot code version, config, input/output artifacts and execution environment (container or sandbox) at each tool call or LLM step, not just telemetry spans. *When:* When you need to explain or re-run why an agent made a decision, or to replay a run later.
- **Counterfactual replay from a checkpoint** — Pick a checkpoint, change one variable (model, a tool's return value via a mock function, or a policy), and re-run only the steps after it while earlier checkpoints are reused. *When:* To test a cheaper model or a changed tool before shipping, without re-running the whole workflow.
- **Side-by-side run diffing** — Compare the original run and each fork: shared prefix, first divergent tool call, latency, token cost, and final artifact or decision. *When:* To see exactly where a change altered behaviour and whether the outcome is acceptable.
- **Cohort replay with agent-driven analysis** — Select a set of production runs by cost, duration or risk, replay the same change across all of them, export a JSON report, and have an LLM agent (via an MCP server or skill) flag regressions and summarise patterns. *When:* When single-run results are noisy and you need a population-level go/no-go decision.
- **Replay-based ship gate** — Require cohort-level evidence on quality and cost before routing traffic to a changed model or tool; default verdict is hold. *When:* Before switching models or tools in production, where a cheap swap could silently hurt task success.

## Numbers
- DoorDash (speaker cites its 1 June blog post): simulated replays of customer bots cut analysis from hours to about 5 minutes across hundreds of simulations, with 90% fewer hallucinations and results within 2 points of production. Speaker-reported, not verified. ([3:53](https://youtu.be/bZISsg7H7DA?t=233))
- Tau-bench point cited by speaker: a model that passes 60% of the time is only self-consistent about a quarter of the time, so one replay is not reliable evidence. ([14:07](https://youtu.be/bZISsg7H7DA?t=847))
- Demo: one replay with GPT-5 Nano looked cheaper and reached the same outcome, but the cohort verdict was don't ship. No cost or token figures were stated numerically; cheaper was described qualitatively. ([12:40](https://youtu.be/bZISsg7H7DA?t=760))

## Hot takes
- A naive model swap usually does not work; judging it on cost alone is a false economy.
- One replay is an anecdote; ship decisions need cohort-level analysis.
- Agent traces alone are a read-only record; without runtime state you cannot ask what would have happened.

## Tools mentioned
Kitaru, OpenTelemetry, GPT-5 Nano

## Relevance to our work
- **agentos** (2/3): AgentOS L4 covers observability and L2D mines telemetry into skills, but there is no per-step checkpoint of code, artifacts and environment for replay. Crucible's sandboxing is a possible snapshot target. The cohort-replay idea fits the telemetry-to-skills pipeline. → *Scope a spike: record per-tool-call checkpoints (config, artifacts, sandbox ref) for one AgentOS agent, then replay one run with a swapped model and diff the outputs before adding cohort replay.*
- **prosharness** (2/3): ProsHarness already has checkpoint/resume for long Claude Code runs. Replay of a checkpoint with one variable changed (model or mocked tool), plus side-by-side diff, is the piece it does not have. → *Compare the ProsHarness checkpoint format against the per-step snapshot described here, and add a replay-from-step command that accepts a model override and a mocked tool result.*
