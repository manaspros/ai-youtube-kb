# Tribal Dungeons of Global Shipping: AI Agents at Global Scale — Dmitry Buykin, Maersk

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `dQ-_i1tZiws` · [watch](https://youtu.be/dQ-_i1tZiws) · **date:** 2026-09-18 · **length:** 12:02 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Dmitry Buykin · **orgs:** Maersk
- **topics:** enterprise-adoption, evals, agent-architecture, security-guardrails · **tags:** sop, tribal-knowledge, production-agents, write-gate, replay, heat-map, legacy-integration, logistics, corrections, harness

> Maersk's Dmitry Buykin on running 200+ production shipping agents by turning expert SOPs into executable agent procedures, with a feedback loop that turns each correction into a harness change.

## Summary
The speaker from Maersk describes production AI agents for global shipping operations, where each shipment is many parallel state machines and the long tail of exceptions is the costly part. The core problem is that expert knowledge lives in legacy SOPs written for humans (effectively screenshots and clicks), while an agent needs preconditions, decisions, identifiers, validation, recovery steps and evidence of success. Their system has three parts: an SOP corpus that acts as process memory, an execution runtime, and SME feedback capture. They report over 200 instances in production with latencies from a few minutes to about 10 minutes, limited by legacy systems and expert time. Quality came from more than 100,000 corrections over nine months, replayed against real examples with write rights disabled, and from mapping each failure to a specific preventive fix such as a classifier eval or a write gate. The speaker argues that the harness, not the agent loop, is the real system, and that production needs a cage while discovery needs freedom. They also say they avoid MCP because the systems behind it are bloated, and they tune function-calling tools instead.

## Key ideas
- **The hard part is turning tribal, operational knowledge into a form an agent can execute safely.** — Many processes exist only as expert know-how or screenshot-style SOPs. The speaker calls these 'tribal dungeons'. Agent-ready SOPs need preconditions, decisions, identifiers, validation, recovery paths and evidence of success. ([0:08](https://youtu.be/dQ-_i1tZiws?t=8))
- **Shipments are many parallel state machines, so the happy path is easy and the exception tail is the expensive part.** — Automation already covers the easy majority in many companies. When one step cannot complete, the process needs expert orchestration across several incomplete legacy systems. ([1:13](https://youtu.be/dQ-_i1tZiws?t=73))
- **Experts own the what, agents own the how, and exceptions become guardrails.** — Most of the effort is negotiation between experts and engineers to agree on the procedure. The system has three parts: an SOP corpus used as process memory, an execution runtime, and SME feedback capture. The loop around the agent is the system, not the agent loop itself. ([3:20](https://youtu.be/dQ-_i1tZiws?t=200))
- **The SOP corpus is the real asset, about 20 times larger than the runtime, and it has to vary by country.** — Each country's procedures differ, so the corpus grows in variants. The speaker says it represents the company's process memory. ([4:24](https://youtu.be/dQ-_i1tZiws?t=264))
- **A correction only counts once it becomes an executable change, and quality comes from replay, not a bigger model.** — Real past examples are replayed with production write rights disabled, and the team checks whether behavior improved. Expert review and engineering review use the same shared trace as evidence. ([5:30](https://youtu.be/dQ-_i1tZiws?t=330))
- **Each failure should map to a specific preventive fix, and prompts alone are not a guardrail.** — A wrong workflow becomes a classifier eval, a wrong write becomes a write gate, and a wrong assumption gets its own fix. Critical paths keep review and approval in the loop. Discovery needs agent freedom, and production needs a cage. ([8:11](https://youtu.be/dQ-_i1tZiws?t=491))
- **Heat maps of clustered traces set the priorities, and turning one red cell green takes about one to two months of team effort.** — Thousands of traces are grouped into tracked scenario cells so experts and engineers look at the same problems. The speaker says the team has logged over 100,000 corrections in nine months. ([6:42](https://youtu.be/dQ-_i1tZiws?t=402))
- **Successful step sequences should be folded back into composite tools that other agents can reuse.** — The aim is an adaptive system that learns from what works and rolls it into code. This is how a process extends from one country to hundreds of countries at once. ([9:21](https://youtu.be/dQ-_i1tZiws?t=561))

## Techniques
- **SOP-to-agent conversion** — Rewrite human SOPs (screenshots and click paths) into agent procedures with explicit preconditions, decision points, identifiers, validation calls, recovery steps and evidence of successful execution. *When:* When a legacy process is documented for people and an agent has to run it safely.
- **Three-part agent harness** — Keep an SOP corpus as process memory, an execution runtime that bounds what the agent can do, and an SME feedback capture path. Treat the refinement loop around the agent as the main system. *When:* When the agent loop is not the bottleneck and quality depends on feedback from domain experts.
- **Failure-to-fix mapping** — For each failed trace, classify the root cause and apply a matching fix: a classifier eval for a wrong workflow, a write gate for a wrong write, or a dedicated check for a wrong assumption. Prefer preventive controls over instructions to be careful. *When:* When production failures need repeatable, reviewable fixes instead of prompt edits.
- **Replay with writes disabled** — Replay real past cases through the agent with production write rights turned off, and measure whether behavior improved after a change. *When:* When you need regression evidence for a change without risking live systems.
- **Trace clustering into heat maps** — Group thousands of traces into scenario cells, color the cells by failure density, and assign work from the hottest cells. *When:* When experts and engineers need one shared, prioritized view of many failures.
- **Composite tools from repeated success** — Collect successful step sequences and merge them into larger reusable tools for other agents. *When:* When the same multi-step pattern recurs across countries or workflows.
- **Function-calling tools instead of MCP** — Distill backend responses and tune each tool through function calling, instead of exposing bloated systems through MCP. *When:* When backend systems return verbose data and the team needs tight control of tool quality.

## Numbers
- Over 200 agent instances running in production ([4:24](https://youtu.be/dQ-_i1tZiws?t=264))
- Latency runs from a few minutes up to about 10 minutes, bounded by legacy systems and expert time ([4:24](https://youtu.be/dQ-_i1tZiws?t=264))
- The SOP corpus is about 20 times larger than the runtime ([4:24](https://youtu.be/dQ-_i1tZiws?t=264))
- Over 100,000 corrections logged in the past nine months ([6:42](https://youtu.be/dQ-_i1tZiws?t=402))
- Turning one red heat-map cell into a fixed area takes about one to two months of whole-team effort ([6:42](https://youtu.be/dQ-_i1tZiws?t=402))
- Talk length about 12 minutes; the transcript covers the talk and a brief Q&A close ([0:08](https://youtu.be/dQ-_i1tZiws?t=8))

## Hot takes
- Vibe coding ends where the real work starts, and spec-driven development stops improving accuracy at this scale.
- Please be careful is not a guardrail; a preventive control that removes the unsafe path is.
- Accuracy was earned one small correction at a time, not designed up front.
- The best AI models are rented intelligence; the adaptive architecture around them is the asset.
- They do not use MCP because the systems behind it are bloated, so they tune function-calling tools instead.

## Tools mentioned
SME bench (internal triage tool that clusters failures), Function calling

## Relevance to our work
- **agentos** (2/3): SkillForge needs a success signal and governed skills. The talk uses expert corrections as that signal, and folds repeated successful step sequences into composite tools. → *For SkillForge, treat an expert-confirmed correction as the success label, and test replaying mined sequences with side-effecting tools disabled.*
- **prosharness** (2/3): ProsHarness wraps long Claude Code runs with checkpoint and resume. The talk's separation of discovery freedom from production caging, plus write gates, applies directly to the harness. → *Add a per-run write gate and a replay-with-writes-disabled check to ProsHarness checkpoint/resume runs, and log each failure with a fix-type label.*
- **general** (1/3): Rule that a correction is not done until it becomes an executable change or test, and that replay outcomes are the evidence. → *Adopt this rule in review notes: a fix counts only once it is a test, eval or code change that can be re-run.*
