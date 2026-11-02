# Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents — Vasant Kearney, Onlay

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `UyyOoJmuATU` · [watch](https://youtu.be/UyyOoJmuATU) · **date:** 2026-09-18 · **length:** 20:25 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Vasant Kearney · **orgs:** Onlay
- **topics:** agent-architecture, governance-compliance, evals, enterprise-adoption · **tags:** healthcare, X12, claims, insurance, agent harness, guardrails, memory, multimodal, model swap, cost, EHR, FHIR, small models

> Vasant Kearney (Onlay) argues healthcare agents should run on X12 insurance transactions as a public, strict contract that guardrails can reject, with tiered memory and skeptical use of models.

## Summary
The speaker frames the goal of healthcare agent work as lowering the cost of insurance interactions and improving the patient experience, and says every technical choice should tie back to one of those. He describes the agentic execution layer as the model taking actions (database queries, code, insurance calls, web portals, EHR writes), with memory kept in a database rather than local files for separation. He argues that a new, better model cannot simply be swapped in, because the whole system has to be re-evaluated. He proposes X12 transactions (eligibility 270, attachments 275, acknowledgement 999, payment 835) as the harness: a shared structure that makes LLM output checkable and rejectable, and that engineers can look up instead of inventing schemas. Because insurers' systems can disagree or be wrong together, he treats the internal X12 record as correct only until downstream evidence contradicts it. He recommends balancing free agent reasoning with hard-coded steps, adding persistent memory at partner, organization and user levels while guarding against bias and letting users break out, and using small models cost-effectively for routine high-volume work.

## Key ideas
- **Ground every agent decision in the business goal** — The speaker says healthcare agent work should serve one of two aims: lower the cost of insurance interactions or improve the patient experience. Technical excitement alone is not enough. ([1:10](https://youtu.be/UyyOoJmuATU?t=70))
- **Use X12 transactions as the harness contract** — Insurance steps map to public X12 transactions (eligibility 270, attachments 275, acknowledgement 999, payment 835). A strict, shared format gives the model a narrow output space and a clear reason to reject bad output. ([9:04](https://youtu.be/UyyOoJmuATU?t=544))
- **Multi-step errors compound** — A claim can take around 50 steps. Each step can introduce an error that propagates, so strict checks that reject a wrong step matter more than a single good answer. ([9:04](https://youtu.be/UyyOoJmuATU?t=544))
- **Upstream image reduction can lose downstream context** — Reducing an image to findings for cost reasons can drop details that a later procedure or model needs. Multimodal context should be kept where it matters. ([5:13](https://youtu.be/UyyOoJmuATU?t=313))
- **A better model is not a drop-in replacement** — A model that scores higher on general evals may still fail on the specific workflows the system depends on. The speaker says to re-check the whole system with evals before switching models. ([7:58](https://youtu.be/UyyOoJmuATU?t=478))
- **Persistent memory adds bias** — Tiered memory (partner, organization, user) helps interpret short requests, but it can steer users into repeating yesterday's task. Users must be able to break out of remembered patterns. ([11:53](https://youtu.be/UyyOoJmuATU?t=713))
- **No ground truth across insurer systems** — Phone, browser and X12 layers can all confirm a wrong fact, as in a denial for a coverage gap. Treat the internal record as correct only until downstream evidence proves otherwise. ([16:07](https://youtu.be/UyyOoJmuATU?t=967))
- **Be AI-skeptical and match model size to the task** — Use LLMs and small models conservatively, since they can fail and designers can set them up to fail. Do not run an over-powered, expensive model on a routine task that runs about 1,000 times a day. ([18:43](https://youtu.be/UyyOoJmuATU?t=1123))

## Techniques
- **Standard-format tool contract** — Map each agent action to a public standard transaction (here X12) and validate model output against it, so invalid output can be rejected before it propagates. *When:* Regulated or integration-heavy domains where a public schema already exists, and where you want engineers to read a known spec rather than an agent-invented one.
- **Strict guardrail rejection per step** — Add checks at each step of a long agent chain that can reject an output, so errors stop early instead of compounding over about 50 steps. *When:* Long multi-step workflows where one bad intermediate result would corrupt later steps or incur costly actions.
- **Separated, tiered memory** — Store memory in a database, split into partner, organization and user scopes, instead of local files. Keep the user able to opt out or reset memory so it does not steer repeated behavior. *When:* Multi-tenant or enterprise settings where memory must be auditable, separated by tenant, and easy to reset.
- **Full-system regression evals before model swaps** — Re-run the complete workflow evals and validation whenever a model changes, not only public benchmarks. *When:* Before upgrading the model behind a production agent that depends on its exact behavior.
- **Hybrid hard-coded and agentic execution** — Hard-code routine, high-volume steps and leave open-ended reasoning to the agent, so the system does not become unmanageable or too costly. *When:* Routine workflows that run many times a day and need predictable cost and latency.
- **Write-action audit logging** — Keep at least user logs for any action with write implications, such as system transactions, calls, or portal changes. *When:* Agents that can change records in external systems.

## Numbers
- Example claim reasoning chain of about 50 steps, each a possible error point ([9:04](https://youtu.be/UyyOoJmuATU?t=544))
- Routine task example that runs about 1,000 times a day, used to argue against over-powered models ([19:44](https://youtu.be/UyyOoJmuATU?t=1184))

## Hot takes
- Be AI-pilled about capability but AI-skeptical about reliability; models can be set up to fail by their designers.
- Public standards such as X12 beat agent-invented schemas because a new engineer can look them up.
- Upstream image summarization for cost can silently drop context that downstream procedures need.
- Persistent memory across days is a bias risk, not only a convenience.

## Tools mentioned
X12, FHIR, EHR, Claude Code, Codex, OpenClaw, Hermes Agent

## Relevance to our work
- **agentos** (2/3): Its tiered cross-session memory (L2A MemoryMesh) matches the talk's partner/org/user memory tiers and its bias warning, which the talk says users must be able to escape. → *Add a user-facing reset or opt-out path and a bias test (repeat-task steering) to MemoryMesh tiered memory before adding more cross-session recall.*
- **prosharness** (2/3): The talk's broad 'harness' definition (memory, tools, checks, permissions, handoffs, evals) and per-step rejection overlap with ProsHarness's checkpoint and plan-critique loops. → *Add a per-step schema or rule check that can reject a Claude Code step output, and run a fixed regression eval before changing the underlying model.*
