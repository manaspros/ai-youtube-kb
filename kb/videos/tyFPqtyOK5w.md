# The Autonomous Computer: Infrastructure for Computer Use Agents — Ang Li, Simular

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `tyFPqtyOK5w` · [watch](https://youtu.be/tyFPqtyOK5w) · **date:** 2026-10-12 · **length:** 1:12:59 · **format:** workshop · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Ang Li · **orgs:** Simular, DeepMind, Microsoft, OpenAI, Anthropic
- **topics:** voice-multimodal, agent-architecture, evals, sandboxing-execution · **tags:** computer-use, neurosymbolic, OSWorld, pass-k, replay, accessibility-tree, guardrails, cloud-desktop, stateful-programming

> Ang Li (Simular) on computer-use agents: why reliability needs a neurosymbolic loop, where the agent writes code that is replayed, and why pass^k matters more than pass@1.

## Summary
Ang Li, CEO of Simular, runs a workshop on computer-use agents that operate a full desktop through screenshots or the accessibility tree. He traces the company's harness generations (Agent S, S2, S3), which went from accessibility-tree grounding to vision-only manager/worker setups to test-time scaling with multiple agents. He argues the next problem is reliability, not raw success: a pass^k metric (every one of k runs must succeed) shows the best agents losing about 10 points on repeat runs, and a clarification-question prompt helps. His main proposal is neurosymbolic: a VLM agent does the task once while writing code, the code is replayed on later runs, and the agent takes over again when a verification step fails. He also presents cloud-hosted desktops and an API as the scaling path, and he pitches his own closed-beta product and an open-source scripting language. Most figures are his own internal or qualitative claims rather than independent results.

## Key ideas
- **Measure pass^k, not pass@1, for production agents.** — Customers wanted agents that run the same workflow every day without babysitting. He proposes pass^k (the task must succeed in all k runs). The best OSWorld agents degrade noticeably at k=3, and degrade more when the environment or query is perturbed. ([17:36](https://youtu.be/tyFPqtyOK5w?t=1056))
- **A clarification-question instruction improves reliability.** — Prompt the agent to ask about ambiguous parts of the task while keeping questions to a minimum. In the paper he cites, reliability improves for all tested agents, with the largest gain for Agent S with GPT-5. ([20:24](https://youtu.be/tyFPqtyOK5w?t=1224))
- **Neural plus symbolic is the core design principle.** — The neural part is a VLM that handles open-ended screens. The symbolic part is code, which is deterministic. He frames the goal as a Pareto front between adaptivity and reliability, and says no single approach wins on every axis. ([8:16](https://youtu.be/tyFPqtyOK5w?t=496))
- **Screen signals: screenshot vs accessibility tree.** — The accessibility tree is OS-level text (a different format on Mac and Windows) that renders the UI. Text allows exact matching, which code replay needs. Screenshots cover what the tree omits. Developers can hide elements from the tree on purpose. ([9:43](https://youtu.be/tyFPqtyOK5w?t=583))
- **Replay a successful run as code, and heal it when it breaks.** — The VLM agent runs the task while writing code for each step. Next time, the code runs first. If the environment changed and a step fails, a coding-agent healing loop repairs the script, falling back to the live agent when needed. ([30:27](https://youtu.be/tyFPqtyOK5w?t=1827))
- **Verification after each step makes replay safe.** — Each replayed step is checked. A failure stops the run, and the agent switches back to VLM mode from that point. The agent also chooses per step between a screenshot and an accessibility snapshot. ([40:54](https://youtu.be/tyFPqtyOK5w?t=2454))
- **Stateful programming versus stateless programming.** — He describes conventional scripts as stateless: they run without reading the environment. A neurosymbolic agent reads the state after each line and the state changes, which he argues will shape future programming. ([52:35](https://youtu.be/tyFPqtyOK5w?t=3155))
- **Accuracy comes from verification loops and code-first guardrails.** — For data entry, reverse the filled form and ask the model whether it makes sense; the model catches errors more often because checking is easier than acting. Guardrails use rules first, then the agent, then a human. An irreversible-action gate asks for approval, and VM images can whitelist OS-level actions. ([58:21](https://youtu.be/tyFPqtyOK5w?t=3501))
- **Cloud desktops are the scaling path.** — A local agent takes over the user's only foreground computer. Once the agent works, users want more machines, so Simular hosts cloud Windows desktops (macOS, Linux and Android are planned), with a CLI and API. ([43:49](https://youtu.be/tyFPqtyOK5w?t=2629))

## Techniques
- **Neurosymbolic replay with healing** — Let a VLM agent solve the task once while emitting code for each step. Store the code for successful runs. On later runs, execute the code first, verify each step, and on failure either repair the code with a coding agent or hand control back to the VLM at the failing step. *When:* Repeated workflows on apps that are mostly stable, where token cost and determinism matter, such as form filling or data pulls.
- **Accessibility-tree grounding with IDs** — Linearize the accessibility tree into a text list with element IDs and ask the model which ID to act on. Text output allows exact matching, unlike screenshot coordinates. *When:* Desktop or web apps that expose a usable accessibility tree, and when deterministic replay is needed.
- **Per-step observation choice** — Let the agent pick between a screenshot and an accessibility snapshot for each step. For summarizing or extraction, it used the snapshot. *When:* Mixed tasks where some steps need visual layout and others need the text of the page.
- **Clarification-first prompt** — Instruct the agent to ask for clarification on ambiguous parts of a task while keeping questions to the minimum needed to preserve the task's intent. *When:* Tasks where the instruction is underspecified and the agent should not guess at high cost.
- **Reverse-check verification of entries** — After filling a form, give the model the filled form and ask whether the values make sense. If something is wrong, rerun the task. *When:* Data entry where accuracy must be near 100%, and a second model call for checking is affordable.
- **Rules-first guardrail chain** — Route each action through deterministic rules first. Unmatched cases go to the agent and then to a human. Irreversible actions trigger an approval gate. Enforce OS-level whitelists in a custom VM image. *When:* Agents that can take actions with real money or data at stake.
- **Exploration swarm for changing UIs** — When a UI changes, run many cheap exploration agents to re-map trajectories. Use the map to rebuild the replay scripts. *When:* Legacy or frequently changing software where exploration has no real cost. Not suitable where each exploratory action is expensive, such as banking.
- **Test-time scaling by agent count** — Run several agents on the same task and compare success rates at a fixed budget (workers times steps). *When:* Benchmarks or tasks where extra compute can buy reliability and you need a fair cost comparison.
- **Save-to-skill with parameters** — Save the code from a successful session as a skill. On a later run with different inputs (for example, another day), replay it with changed parameters and fall back when a hiccup appears. *When:* Recurring lookups where only a few inputs change between runs.

## Numbers
- Agent S (late 2024) reached 20% success on OSWorld, state of the art at the time. The early-2024 benchmark was about 5%. ([11:04](https://youtu.be/tyFPqtyOK5w?t=664))
- Agent S3 (late 2025) surpassed the human baseline on OSWorld in December. OSWorld 2 was released recently, and the best model scores about 20% on it. ([13:46](https://youtu.be/tyFPqtyOK5w?t=826))
- With a fixed budget of workers times steps, 10 agents scale better in success rate than fewer agents (speaker's chart). ([13:46](https://youtu.be/tyFPqtyOK5w?t=826))
- Under pass^3, the best OSWorld agents lose almost 10 points of success, and perturbed environments make it worse. ([19:02](https://youtu.be/tyFPqtyOK5w?t=1142))
- On the second run of a replayed workflow, he estimates maybe 50% of the effort is done by code with no LLM calls (his estimate, not a measured result). ([40:54](https://youtu.be/tyFPqtyOK5w?t=2454))
- A $500 unlimited task plan was tested with users. He suggests usage-based pricing may not last. ([42:24](https://youtu.be/tyFPqtyOK5w?t=2544))
- He personally runs about 20 cloud machines in the background. ([45:07](https://youtu.be/tyFPqtyOK5w?t=2707))
- About 80% of applications live in legacy systems (his estimate). ([1:09:58](https://youtu.be/tyFPqtyOK5w?t=4198))
- He says training a computer-use model would need exponentially more money than current labs spend, because screen data is 2D and text is 1D. He jokes it would take a couple trillion dollars. ([1:11:05](https://youtu.be/tyFPqtyOK5w?t=4265))

## Hot takes
- Computer-use agents should become neurosymbolic: the agent explores once, code replays deterministically, and the agent is used only to heal.
- Production customers need pass^k, not pass@1, and most benchmarks do not measure it.
- Per-task token spend should trend toward zero once a workflow has been learned, and per-use pricing will not last.
- There is no silver bullet across accessibility tree, DOM and screenshots, so robust systems need several modalities, like a self-driving car with radar plus camera.
- Legacy software is the largest near-term market for computer-use agents, because most apps run on systems without APIs.

## Tools mentioned
Simular Agent S / S2 / S3 harnesses, Simuland (open-source scripting language), Claude Code, OSWorld, OSWorld 2, Playwright, Windows 365 for agents (Microsoft), Simular cloud desktop API and CLI, GPT-4V, GPT-5, GLM 5.2

## Relevance to our work
- **agentos** (2/3): SkillForge (L2D) mines agent telemetry into governed skills, and this talk shows a concrete replay-first pattern with an LLM fallback. Crucible's exec-gate guardrails map to the rules-first approval chain. → *Prototype a replay tier in SkillForge: store the code from each successful agent trajectory, replay it first, verify each step, and fall back to the LLM on failure. Log tokens saved per run.*
- **prosharness** (2/3): ProsHarness checkpoints long agent runs. The talk's per-step verification and handback-on-failure pattern is a natural fit for checkpoint/resume. The clarification-question prompt could also feed its plan stage. → *Use checkpoint boundaries as fallbacks: verify each step's outcome, and on failure resume the live agent from the last checkpoint instead of restarting the whole run.*
- **general** (2/3): Recurring evals interest. The talk gives a concrete repeat-run reliability metric (pass^k) and shows it can reveal degradation that pass@1 hides. → *Report pass^k (all k runs succeed, k=3 to start) next to pass@1 in our agent evals, and track the gap as a reliability signal.*
