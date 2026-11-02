# Why 99% Accurate Browser Agents Still Fail — Derek Meegan, Browserbase

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `5xi_S1f9sDU` · [watch](https://youtu.be/5xi_S1f9sDU) · **date:** 2026-10-04 · **length:** 16:49 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Derek Meegan · **orgs:** Browserbase
- **topics:** voice-multimodal, testing-verification, agent-architecture · **tags:** browser-agents, production, deterministic-tools, unit-economics, per-transaction-success, retries, skills-as-sop, computer-use

> Why 99%-accurate browser agents still fail in production, and how moving deterministic steps out of the model and verifying outcomes makes transactional browser workflows profitable.

## Summary
Derek Meegan (Browserbase) argues that a browser agent demo is easy but production runs are not, because cost accumulates per step while value is only realized when the whole transaction succeeds. He shows that a 99% per-step success rate over 100 steps gives only about 36% end-to-end. He proposes judging agents by profit (revenue minus cost) and ranking performance first, then cost, then maintainability. Success should be defined by a concrete artifact the run leaves behind, measured per transaction with retries allowed. He walks through a health-insurance portal example that starts as a bare agent and is refactored step by step: a single download tool, an OCR-based verify tool checked against the system of record, a serverless auth function outside the model, and a skill written as an agent SOP for the critical path. The talk is practitioner-level with some vendor framing.

## Key ideas
- **Cost accumulates with every step, but value is only realized when the whole task is done. Browser agents get no partial credit.** — Each step adds cost and risk. Value arrives only at the end of the trajectory, so the success of the full chain is what matters. ([4:19](https://youtu.be/5xi_S1f9sDU?t=259))
- **Compounding per-step failure makes long browser trajectories fragile.** — With a 99% success rate per step over 100 steps, end-to-end success is about 36%. The speaker says this is not a reason to avoid browser agents, because the math is not the whole story. ([5:20](https://youtu.be/5xi_S1f9sDU?t=320))
- **Judge agents by profit (revenue minus cost), in priority order: performance, then cost, then maintainability.** — Performance comes first because cost and maintainability become optimization problems once the agent reliably completes the task. The speaker says optimization problems can be solved with engineering. ([6:47](https://youtu.be/5xi_S1f9sDU?t=407))
- **Define success as a concrete artifact the run leaves behind, and measure per transaction, not per run.** — Examples are a confirmation email, an order ID, or a record that can be queried deterministically. Allowing retries, one agent at 50% per run reaches about 94% per transaction. The customer cares about the completed workflow, not the number of attempts. ([8:13](https://youtu.be/5xi_S1f9sDU?t=493))
- **Costs have a per-run part and a maintenance part, and maintenance is often the larger one.** — Per-run costs are mostly model cost now, but the speaker expects model cost to shrink as open models cut prices. Maintenance covers observability of what happened in the browser, developer time to fix breakage, and re-evaluation as sites and models change. ([9:40](https://youtu.be/5xi_S1f9sDU?t=580))
- **Move steps that do not need judgment out of the model and into deterministic code.** — The speaker's example refactor encapsulates the download in one tool, pulls the fixed login flow into a serverless function, and adds a verify tool. Each change reduces the steps the model must take, which lowers cost and raises performance. ([12:38](https://youtu.be/5xi_S1f9sDU?t=758))
- **Give the agent a deterministic verifier so it can check its own outcome.** — An OCR tool extracts entities from the downloaded document and compares them with the system of record. The agent then knows authoritatively whether its trajectory succeeded. ([13:35](https://youtu.be/5xi_S1f9sDU?t=815))
- **Write a skill as an agent SOP that narrows the critical path.** — Because the output is a probability distribution, naming the next step in a skill makes the model more likely to take it. The speaker says this removes ambiguity and keeps the agent on the critical path. ([15:00](https://youtu.be/5xi_S1f9sDU?t=900))

## Techniques
- **Three browser interaction strategies** — Textual representation (HTML plus accessibility tree hybrid), computer use (screenshot series), or de-harnessed execution (agent writes arbitrary JS or CDP code). Most production systems use the first, the second, or a combination. *When:* Choose the representation based on how much the task depends on visual layout versus semantic structure.
- **Transactional scope for browser agents** — Target workflows that complete one unit of work end to end, such as paying a bill, placing an order, or submitting a form, and treat the browser as the execution environment for ambiguity. *When:* At scale, when each run must produce a verifiable outcome and partial completion has no value.
- **Per-transaction success with bounded retries** — Measure success against the completed business artifact, not per attempt, and allow a fixed number of retries per transaction. *When:* When the customer cares about reliable completion and retry cost is small compared with the value of the outcome.
- **Artifact-based success check** — Define the artifact a successful run leaves behind and check it with deterministic code, for example by querying a system of record or comparing extracted entities. *When:* Any workflow where the agent might believe it succeeded when it did not.
- **Single-transaction tool encapsulation** — Wrap a multi-step browser operation, such as navigate, click through a download, and retrieve the file, into one tool call that the model invokes. *When:* When a sub-procedure is fixed and the model's choices inside it add cost and failure risk without adding value.
- **Deterministic auth outside the model** — Run login or other invariant authentication in a separate serverless function that hands an authenticated browser to the agent runtime. *When:* When the same login flow is reused across many business workflows on one site.
- **Skill as SOP for the critical path** — Write a skill document that lists the steps for the agent in order, like a human standard operating procedure, so the agent knows its next step. *When:* When the agent has a small area of real ambiguity and the rest of the workflow is known.

## Numbers
- Per-step success of 99% over 100 steps gives about 36% end-to-end success (speaker's example). ([5:20](https://youtu.be/5xi_S1f9sDU?t=320))
- A browser agent with 50% success per run reaches about 94% per transaction when up to four retries are allowed (speaker's figure). ([8:13](https://youtu.be/5xi_S1f9sDU?t=493))
- Model cost is currently the main per-run cost, and the speaker expects it to fall as open-source model pricing drops. ([9:40](https://youtu.be/5xi_S1f9sDU?t=580))

## Hot takes
- Performance comes first and cost and maintainability are optimization problems that engineering can solve once the agent reliably completes the task.
- Measure browser agents per transaction with retries allowed, because customers do not care how many retries it took.
- An agent is just another line item, and it should return more than it costs.

## Tools mentioned
Browserbase, Chrome DevTools Protocol (CDP), OCR, accessibility tree, serverless functions

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code runs with checkpoint/resume and verification steps. The talk's split between model-driven steps and deterministic tools, plus its verify-against-record pattern, applies directly to long agent runs. → *In ProsHarness checkpoint loops, route fixed sub-steps through deterministic tool calls and add a verifier that checks the produced artifact against ground truth, not the agent's own claim of success.*
- **agentos** (1/3): Crucible runs sandboxed code execution, and browser-driving tasks would fall under it. The talk's guidance on deterministic tools and artifact verification is relevant only if AgentOS handles browser workflows. → *If Crucible ever runs browser tasks, read the deterministic-tool-plus-verify pattern before designing its exec-gate checks.*
- **general** (1/3): The per-transaction success metric and the artifact-based success definition apply to any agent workflow, not only browsers. → *For each agent task we measure, define the artifact that proves success and report success per transaction after retries.*
