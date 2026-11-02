# Agents Need Feature Flags - Sachin Gupta

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `zU4EagB311U` · [watch](https://youtu.be/zU4EagB311U) · **date:** 2026-07-18 · **length:** 19:17 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Sachin Gupta · **orgs:** Cursor, Replit, LangChain, Railway, LaunchDarkly, Unleash, Air Canada
- **topics:** governance-compliance, security-guardrails, agent-architecture · **tags:** feature-flags, kill-switch, canary-rollout, autonomy-levels, tool-access-control, model-routing, memory-policy, audit-trail, agent-middleware, rollout-playbook

> Sachin Gupta argues agents need feature-flag discipline: six flag types (prompt, tool, model, memory, autonomy, kill switch), a middleware layer, and a kill switch shipped first, with four metrics to track.

## Summary
The speaker, a back-end engineer, says agent behavior (prompts, tools, models, memory, autonomy, sub-agents) ships to all users at once with no canary, segment, or rollback. He cites four incidents from the past 14 months (a support bot citing a nonexistent policy, a database deletion with fabricated users, a four-agent LangChain loop costing $47,000, and a coding agent running a production DB command with a wrongly used token). He proposes six flag types, one per behavior surface, resolved in a middleware layer that sits between users and the agent loop and that every spawned sub-agent must also pass through. A live-style demo (illustrative, not real measurements) shows a tool flag turning off mid-conversation and a kill switch halting a runaway loop within about 30 seconds. He gives a five-step rollout order (kill switch first, then tool wrapping, staged autonomy, prompt variants, then watching metrics) and four suggested metrics with default thresholds. He closes with common failure modes (flags resolved per session, sub-agent bypass, caching masking flips, silent kill-switch fires, flag sprawl) and a case for why enterprise buyers will ask for these controls.

## Key ideas
- **Agents change behavior in ways a plain on/off feature flag cannot express** — Prompts, tools, models, memory, autonomy, and sub-agents each change what the agent does, so each needs its own flag type. A single boolean feature flag does not cover them. ([4:36](https://youtu.be/zU4EagB311U?t=276))
- **Current agent releases are all-or-nothing** — A merged prompt chain or tool addition reaches 100% of users immediately, with no canary, segment, or rollback. The speaker frames this as the failure mode behind the talk. ([0:00](https://youtu.be/zU4EagB311U?t=0))
- **Incidents cited as the motivation** — He cites four incidents in 14 months: a support bot inventing a policy, an agent deleting a production database and fabricating users, a four-agent loop costing $47,000, and an agent using an unrelated token against production. These are his cited sources, not verified by this note. ([3:05](https://youtu.be/zU4EagB311U?t=185))
- **Six flag types, one per behavior surface** — Prompt variant, tool access, model routing, memory policy, autonomy level, and kill switch. He says none need a new flag backend, since existing tools like LaunchDarkly or Unleash can host them. ([4:36](https://youtu.be/zU4EagB311U?t=276))
- **Middleware layer is where flags are enforced** — A middleware sits between the user and the agent loop. It resolves flags, gates tools, routes models, applies autonomy, and honors the kill switch. The agent loop itself stays unchanged. ([11:35](https://youtu.be/zU4EagB311U?t=695))
- **Sub-agents must go through the same middleware** — The biggest failure mode he sees is a parent with correct flags spawning a child that calls the model and tools directly. The kill switch then never reaches the child, so middleware must wrap every spawn. ([13:06](https://youtu.be/zU4EagB311U?t=786))
- **Autonomy should be staged: suggest, then auto-approve, then auto-execute** — Default every surface to suggest. Move to auto-approve per surface as trust builds. Auto-execute is opt-in per tool. He calls autonomy the largest blast-radius dial. ([9:04](https://youtu.be/zU4EagB311U?t=544))
- **Ship the kill switch first** — One agent-wide kill switch and one per tool, shipped before anything else. He lists three properties: it takes effect in seconds, in-flight requests check it at the next decision point, and it is wired in at design time. ([9:04](https://youtu.be/zU4EagB311U?t=544))
- **Business case: enterprise buyers will ask for these controls** — He lists five buyer questions (kill switch demo, prompt rollout policy, beta isolation, mitigation speed, and who can flip flags and whether it is audited). He says a team that cannot demo them will lose deals. ([15:36](https://youtu.be/zU4EagB311U?t=936))

## Techniques
- **Six-surface flag taxonomy** — Create one flag type per surface: prompt variant (route cohorts to prompt versions), tool access (allow or revoke tools per segment or risk class), model routing (cost tier to model, with a stable fallback), memory policy (retention, scope, write-enabled, user-visible), autonomy level (suggest, auto-approve, auto-execute), and kill switch (agent-wide and per tool). *When:* Any agent that ships prompt, tool, or model changes to users, especially with money-moving, data-deleting, or compliance-sensitive tools.
- **Flag middleware between user and agent loop** — Resolve flags in one layer that gates tools, picks the model, sets autonomy, and checks the kill switch. Wrap every sub-agent spawn with the same layer, not only the entry point. *When:* When an agent system has parent-child spawning, or when you need one place to enforce flags.
- **Kill switch with three properties** — Flip takes effect in seconds without a deploy. In-flight requests re-check the flag at each decision point. Wire the switch in during agent design, not during an incident. *When:* Before anything else ships; the speaker says it is the highest-value first step.
- **Canary prompt variant** — Route about 5% of beta traffic to a new prompt. Watch hallucination rate and escalation rate. Promote only when the metrics hold, and block promotion if error rate rises more than 2% over baseline. *When:* Any prompt change, before it goes to all users.
- **Five-step rollout order** — 1) Kill switch for agent and each tool. 2) Wrap every tool call in a flag check. 3) Default autonomy to suggest and promote per surface. 4) Move system prompts out of code into flag-resolved config. 5) Watch four metrics from day one. *When:* When adding flags to an existing agent system and deciding what to build first.
- **Resolve flags per turn and log segment context** — Evaluate flags on each turn, not only at session start. Log the user's segmentation context at the conversation level so later turns are traceable. *When:* Long conversations where user segment or flag state can change mid-session.
- **Bypass caching for flag-sensitive responses** — Make sure the LLM gateway cache does not return an old prompt's response after a flag flip. *When:* Any gateway or response cache sitting in front of agents whose behavior is flag-controlled.
- **Flag hygiene rules** — Give every flag an owner and a removal date. Delete temporary rollout flags right after the rollout. Keep a documented flag inventory. Test the Cartesian product of concurrently active prompt variants. *When:* When flags accumulate; he cites an example of around 600 undocumented flags.

## Numbers
- Four named agent incidents in the last 14 months (speaker's cited examples) ([3:05](https://youtu.be/zU4EagB311U?t=185))
- Four-agent LangChain pipeline looped 11 days and cost $47,000 (cited incident) ([3:05](https://youtu.be/zU4EagB311U?t=185))
- Demo baseline of 428 tool calls per minute; illustrative simulation, not measured data ([11:35](https://youtu.be/zU4EagB311U?t=695))
- Kill switch flipped about 20 seconds into the demo; in-flight agents shut down gracefully by about 30 seconds, flattening the cost graph ([11:35](https://youtu.be/zU4EagB311U?t=695))
- Prompt variant canary at 5% of beta traffic, with promotion blocked if error rate rises more than 2% over baseline ([6:09](https://youtu.be/zU4EagB311U?t=369))
- Suggested target: kill switch fires should be zero per week; investigate if more than two per week ([14:33](https://youtu.be/zU4EagB311U?t=873))
- Suggested target: under 5 minutes to mitigate via kill switch, under 30 minutes for a prompt rollback ([14:33](https://youtu.be/zU4EagB311U?t=873))
- Suggested target: 100% flag audit trail completeness (who flipped what, and when) ([14:33](https://youtu.be/zU4EagB311U?t=873))
- Example of a team with around 600 flags and no documentation (anecdotal) ([16:37](https://youtu.be/zU4EagB311U?t=997))

## Hot takes
- Ship the kill switch first; if you do nothing else, build one agent-wide and one per-tool kill switch.
- Sub-agents bypassing the middleware is the biggest failure mode in agent flag systems.
- Flags are the demo: an enterprise deal can be lost if the team cannot show a kill switch, rollout policy, and audit trail.
- 2026 was about adoption; 2027 will be about control.

## Tools mentioned
LaunchDarkly, Unleash, Lift (as spoken), homegrown flag service

## Relevance to our work
- **agentos** (2/3): AgentOS already toggles pillars through a manifest and routes traffic through one proxy, so a per-agent and per-tool kill switch plus a model-routing fallback fit its L1 proxy design. → *Add an agent-wide and per-tool kill switch to the Govrix Scout proxy path, checked on each request, with an audit log entry for each flip. Measure kill-switch fire rate and time to mitigation from day one.*
- **prosharness** (2/3): ProsHarness already has phone-driven approvals and long-running loops and schedules. The autonomy levels (suggest, auto-approve, auto-execute) and a kill switch checked at each step map onto that design. → *Add a per-tool autonomy level (suggest by default) and a harness-wide kill switch that the loop re-reads at each checkpoint, not only at session start. Log who changed each flag.*
- **general** (1/3): The talk's advice to test combinations of concurrently active prompt variants is a general point for any agent project that uses prompt flags. → *If more than one prompt flag can be on at once, test the combinations as a matrix instead of testing each flag alone.*
