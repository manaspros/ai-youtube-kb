# AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `bMjlRrWjdT0` · [watch](https://youtu.be/bMjlRrWjdT0) · **date:** 2026-09-18 · **length:** 16:11 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Nachiket Paranjape, Swaroop Chitlur Haridas · **orgs:** DoorDash
- **topics:** evals, enterprise-adoption, product-ux, observability · **tags:** evals, llm-as-judge, annotation, cross-functional, self-serve-ui, api-first, golden-dataset, tracing, prompt-optimization, cost-reduction, agent-gateway, llm-gateway

> DoorDash GenAI platform team on building a cross-functional AI evals platform: UI-first, then API-first, then workflow-first, so non-engineers can run annotation and judge calibration themselves.

## Summary
DoorDash's GNI platform team describes its evals journey. The platform balances accuracy, latency and cost for product teams through shared gateways (LLM, agent) and an evals pillar. They found that evals is a cross-functional effort: strategy/ops set quality bars, PMs write rubrics, operators annotate, and engineers provide APIs and judges. Their platform moved from UIs to API-first to workflow-first, where domain experts can vibe-code their own annotation UIs on stable APIs. A continuous loop runs trace, sample, annotate, golden dataset, calibrate judges, monitor, repeat. Judge prompts are calibrated with a self-serve UI that uses the DSPy-style prompt optimizer (transcribed as "JEPA"), and the team reports lower per-annotation cost and faster iteration. The talk is practitioner-level with few hard numbers.

## Key ideas
- **Evals is a cross-functional team sport, not only an engineering harness.** — Strategy and ops set the quality bar, product people turn requirements into rubrics and workflows, operators annotate, and engineering provides APIs, telemetry, datasets and judges. ([4:11](https://youtu.be/bMjlRrWjdT0?t=251))
- **The platform went UI-first, then API-first, then workflow-first.** — UIs first let non-engineers contribute. APIs let engineers build without waiting on the central team. Coding agents now let ops and PMs run operations through workflows. ([2:54](https://youtu.be/bMjlRrWjdT0?t=174))
- **A continuous eval loop: trace, sample, annotate, golden set, calibrate, monitor, repeat.** — Sample traces down to a small set a human can review, annotate with domain expertise, build golden datasets to calibrate against, then monitor over time and loop again. ([5:08](https://youtu.be/bMjlRrWjdT0?t=308))
- **Stable APIs underlie every surface, and all scores are datasets.** — Two surfaces exist: a telemetry layer (traces, scores, observations, reachable via MCP, SDK or API) and a workflow layer for annotation tasks, golden-set review and judge creation and calibration. Both sit on one API plane owned by the platform team. ([6:24](https://youtu.be/bMjlRrWjdT0?t=384))
- **Ops staff vibe-coded their own annotation UIs on top of the APIs.** — Because the platform was API-first, ops teams with coding agents (Codex, Claude Code) built their own annotation UIs. Image annotation and manual testing use cases shared the same underlying patterns. ([9:42](https://youtu.be/bMjlRrWjdT0?t=582))
- **Judge prompts are calibrated in a self-serve UI, with before/after visibility.** — Start from a simple judge prompt, get baseline scores on traces, run a prompt-optimization loop, then promote the result. The UI shows the original and calibrated prompts side by side so partners can trust the change. Any model can be used, including Gemini, Claude or OpenAI. ([10:50](https://youtu.be/bMjlRrWjdT0?t=650))
- **Ownership of the judge prompt varies by team, and the platform supports all of them.** — Depending on the team, the prompt may be owned by strategy/ops, a PM or engineering. The tool is built to let each team choose. ([12:07](https://youtu.be/bMjlRrWjdT0?t=727))
- **Self-serve annotation cut per-annotation spend and sped up iteration.** — Thousands of rows need annotation each week. Moving this in-house with self-serve tooling reduced annotation cost and raised iteration speed. ([13:31](https://youtu.be/bMjlRrWjdT0?t=811))

## Techniques
- **Continuous eval loop** — Trace sessions, sample a small set, annotate with domain experts, promote reviewed items to golden datasets, calibrate judges against them, monitor, and repeat. *When:* Shipping LLM or agent features where quality depends on domain knowledge that engineers lack.
- **API-first eval platform with vibe-coded UIs** — Expose stable APIs for traces, scores, datasets and judges, then let domain staff generate their own annotation UIs with coding agents on top of them. *When:* Many teams need different annotation workflows and a platform team cannot build a UI for each.
- **Self-serve judge calibration with prompt optimization** — Start with a simple judge prompt, compute baseline scores on traces, run an automatic prompt-optimization loop (DSPy-style, transcribed as JEPA) against golden labels, then show the original and optimized prompts side by side for review. *When:* Non-engineers own judge prompts and need to iterate without filing engineering tickets.
- **Platform-level model choice for judges** — Let each team pick any model (Gemini, Claude or OpenAI) for the calibration loop. *When:* Judge models should be chosen per use case, not fixed by the platform.

## Numbers
- Thousands of rows annotated per week; per-annotation spend fell after moving to self-serve annotation (no figure given). ([13:31](https://youtu.be/bMjlRrWjdT0?t=811))
- Platform balances three forces: accuracy, latency and cost. ([0:13](https://youtu.be/bMjlRrWjdT0?t=13))

## Hot takes
- Evals should be treated as a cross-functional team sport, not an engineering-only harness.
- Domain experts can build their own annotation UIs with coding agents if the platform is API-first.

## Tools mentioned
Claude Code, Codex, DSPy-style prompt optimizer (transcribed as JEPA), MCP, LLM gateway, agent gateway

## Relevance to our work
- **general** (2/3): Shows a concrete org pattern for evals: UI-first, then API-first, then workflow-first, with domain experts in the loop. → *Apply the sample-annotate-calibrate loop to any LLM-judge metric before trusting it, and record the golden set.*
- **agentos** (1/3): AgentOS has no eval-platform or annotation layer; the closest fit is its RAGAS evals under MemoryMesh, which this talk does not address directly. → *Consider a judge-calibration path for RAGAS scores that lets a non-engineer adjust judge prompts against golden labels.*
- **prosharness** (1/3): ProsHarness runs long Claude Code loops, and the talk's trace-sample-annotate loop could check run quality, but this is a weak fit. → *Consider sampling ProsHarness run traces into a short review queue for judge calibration.*
