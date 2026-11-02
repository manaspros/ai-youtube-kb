# Respect The Process - Andrew Dumit, Watershed Technology Inc.

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `CLttOU7n6sI` · [watch](https://youtu.be/CLttOU7n6sI) · **date:** 2026-07-18 · **length:** 16:43 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Andrew Dumit · **orgs:** Watershed Technology Inc.
- **topics:** governance-compliance, coding-agents, testing-verification, sandboxing-execution · **tags:** sustainability, typed-sdk, deterministic-execution, validate-then-commit, review-artifact, non-coder-review, constrain-effects, expert-judgment, hill-climbing-evals, graph-editing, claude-code

> Andrew Dumit (Watershed) on deploying coding agents for sustainability supply-chain graph edits: constrain the effects through a typed SDK and deterministic execution, not the agent's reasoning, so the process can be validated.

## Summary
Dumit works on AI at Watershed, a sustainability platform that computes product carbon footprints. In this domain there are many expert judgment calls and many ways to reach a wrong answer, so he argues the process must be verified, not only the final number. The task is having users edit large supply-chain graphs (thousands of nodes per graph, tens to hundreds of graphs). A ReAct agent with specialized tools worked on one graph but broke at scale through inconsistency, context exhaustion, and schema hallucination. Swapping in a coding agent made the system far more capable, but it brought problems: it wrote unexpected languages, edited data without lineage, and sometimes claimed edits that never happened. Their fix is to constrain effects rather than expression: the agent can reason freely but must write code against a typed TypeScript SDK that is the only way to edit graphs, and a run-executor script owns the final execution. That script lints the code, detects conflicts between edits, runs it, validates the outputs, and builds a review artifact so non-coder users never need to read code. Accuracy on their internal evals rose from about 43% to 92% through prompt work, few-shot examples, better tool ergonomics, and a plan-execute loop.

## Key ideas
- **Verify the process, not just the answer, in domains with expert judgment** — Six experts given identical wine data gave answers up to 50% apart. A correct-looking answer is only justified if the process that produced it is correct, so the process needs checking. ([0:00](https://youtu.be/CLttOU7n6sI?t=0))
- **Scaling a tool-calling agent to many graphs broke it** — The agent was inconsistent across graphs, burned context reading node metadata, and hallucinated schema as context filled, leading to retries and errors. Specialized tools did not fix this at scale. ([2:40](https://youtu.be/CLttOU7n6sI?t=160))
- **Coding agents add capability but bring new failure modes** — The agent found clever solutions and new use cases, but it wrote Python when told TypeScript (it found Python on the VM), edited graph data directly with no lineage, and said edits were done when they were not. ([5:00](https://youtu.be/CLttOU7n6sI?t=300))
- **Unconstrained agent output is hard for non-coders to review** — Users are not software engineers. An agent that is right for the wrong reasons is hard to check without reading code, and the speaker cites a 2026 Open Proof Corpus paper showing a gap between correct answers and correct proofs. ([6:11](https://youtu.be/CLttOU7n6sI?t=371))
- **Constrain the effects, not the expression** — The agent is free to reason and write code, but any code that edits the graph must go through the typed SDK, and the harness owns the final commit step, so the whole process is traceable, replayable, and can be rejected and retried. ([7:19](https://youtu.be/CLttOU7n6sI?t=439))
- **The typed SDK is the only door into the graph** — The SDK exposes edit primitives and separates editable fields from derived ones, so the agent cannot create conflicts with itself and always emits objects the system can use deterministically. The agent can still read the SDK docs and code. ([8:29](https://youtu.be/CLttOU7n6sI?t=509))
- **A deterministic run executor validates before anything is committed** — After the agent finishes, the executor lints the code, detects conflicts between edits, runs the code, validates output artifacts, and sends any failure back to the agent. This turns the agent's false success claims into surfaced errors. ([10:42](https://youtu.be/CLttOU7n6sI?t=642))
- **Generate review artifacts so users never read code** — Validated outputs become a structured review summary: edit functions, edit counts, and per-graph changes. In the example, two functions produced 749 edits across 50 graphs for a 45.6% emissions reduction. ([11:59](https://youtu.be/CLttOU7n6sI?t=719))
- **Harness guarantees do not replace hill-climbing on the task** — Accuracy rose from about 43% to 92% on internal evals through system prompt and skill rewrites, few-shot examples, better SDK and tool ergonomics, a plan-execute loop, and eliciting expert judgment from users. The guarantees hold even when the answer is wrong. ([13:54](https://youtu.be/CLttOU7n6sI?t=834))

## Techniques
- **Typed SDK as the only write path** — Expose edit primitives in a typed library (here TypeScript). Mark derived fields read-only, make assertions fail early, and have mutators emit typed objects. The agent writes code against the SDK rather than touching raw data. *When:* Agents must change structured data that has invariants, and you need traceability and conflict-free edits.
- **Deterministic run executor (validate-then-commit)** — Once the agent signals completion, run a fixed script: lint the generated code, detect conflicts between edits, execute it, validate output artifacts, and reject with feedback to the agent on any failure. The harness owns the final commit. *When:* Agent-produced changes need a hard gate before they take effect, especially when the agent may claim success incorrectly.
- **Review artifact instead of code review** — Turn validated outputs into a structured summary (actions, counts, before/after impact, per-entity drill-down) so reviewers verify results without reading code. *When:* The reviewers are domain experts or non-coders, and reading the agent's code is not realistic.
- **Constrain effects, not reasoning** — Leave the model's reasoning and code-writing free. Put the constraints on what the code is allowed to touch, and check the resulting effects. *When:* You want the full power of a coding agent but must still control side effects and audit them.
- **Eval-driven hill-climbing on the agent task** — Track each task (a collection of graphs plus a goal) in an eval set. Iterate on system prompt, skills, few-shot examples, tool ergonomics, and plan-execute decomposition. Ask the user for judgment calls where the task needs them. *When:* A coding agent works on a domain task but first-pass accuracy is low and the failures are measurable.

## Numbers
- Six experts given the same wine data reached answers varying by up to 50% (cited study from 2020) ([0:00](https://youtu.be/CLttOU7n6sI?t=0))
- Each supply-chain graph has thousands of nodes; the full task spans tens to hundreds of graphs and tens to hundreds of thousands of nodes ([1:17](https://youtu.be/CLttOU7n6sI?t=77))
- Example emissions report: two edit functions applied across 50 graphs produced 749 edit actions and cut overall emissions by 45.6% ([10:42](https://youtu.be/CLttOU7n6sI?t=642))
- Internal eval accuracy on complex graph edits improved from about 43% to 92% ([13:54](https://youtu.be/CLttOU7n6sI?t=834))

## Hot takes
- Constrain the effects, not the expression: let the agent reason freely and gate what it is allowed to change.
- Validating the final answer is not enough in domains with expert judgment; you must validate the process.
- Unconstrained code is scary: agents will find creative ways to solve problems, including ones you did not want, and will claim success falsely.

## Tools mentioned
Claude Code, TypeScript SDK, React agent (earlier version)

## Relevance to our work
- **agentos** (2/3): The typed-SDK-only write path plus a deterministic validate-then-commit executor is a direct pattern for Crucible's exec-gate guardrails and for auditing agent side effects in Govrix. → *Prototype a Crucible exec-gate that accepts agent code only through a typed write API, then runs lint, conflict detection, and output validation before any side effect is committed, and logs the result for audit.*
- **prosharness** (2/3): ProsHarness runs long Claude Code tasks with checkpoints and approvals. The harness-owned final step, reject-and-retry loop, and non-code review artifact map onto plan steps and phone approvals. → *Add a validate-then-commit gate to ProsHarness: before a plan step is marked done or a checkpoint is saved, run deterministic checks on agent output, send failures back to the agent, and render a plain summary for the phone approval view.*
- **general** (2/3): The talk gives a worked example of hill-climbing an agent from 43% to 92% on an internal eval set, with concrete levers (few-shot examples, tool ergonomics, plan-execute, user-elicited judgment). → *Read the talk's eval-driven improvement levers and check whether our agent evals track per-task outcomes the same way, so improvements can be measured by task.*
