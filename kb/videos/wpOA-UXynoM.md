# How Forward Deployed Engineering is done at Factory — Eno Reyes

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `wpOA-UXynoM` · [watch](https://youtu.be/wpOA-UXynoM) · **date:** 2026-08-18 · **length:** 21:21 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Eno Reyes · **orgs:** Factory, Palantir, Hugging Face, Microsoft, Anthropic, OpenAI, Google DeepMind, Cursor, Ramp, Decagon
- **topics:** software-factory, enterprise-adoption, testing-verification, product-ux · **tags:** forward-deployed-engineering, software-factory, agent-readiness, verification-loops, missions, droid, autonomy, model-independence, air-gap, signal-to-deploy

> Eno Reyes (Factory CTO) on forward-deployed engineering as the way to build software factories. The bottleneck is agent readiness, meaning deterministic validators in the codebase, not model capability.

## Summary
Eno Reyes, co-founder and CTO of Factory, explains how Factory runs forward-deployed engineering (FDE). He says Factory avoids consulting-style professional services and uses deployed engineers as the tip of the spear, feeding what they learn at the largest customers back into the product. The goal is a software factory where signals (bugs, customer talks, executive decisions) flow through planning, changes, validation and deploy with no human interruption in the flow, though humans still design and manage the system. He argues the real constraint is agent readiness: how many deterministic validation loops (linters, type checkers, security scans, end-to-end tests) a codebase has. Factory's Missions harness runs long tasks on problems that can be verified, and he gives migrations of 30 to 50 million line codebases as examples. He also describes the sell: an ROI story, a teach-the-model step for customers without an autonomy maturity model, and a model-independent, self-hostable harness that the customer owns the traces for. He closes with the Epcot analogy for building an exemplar that is advanced but not so far ahead that orgs dismiss it, and with hiring pitches for the role.

## Key ideas
- **FDE should not be professional services** — Factory declines consulting-style migrations for customers. Speaker says that work earns revenue but does not scale, and does not make the product better. Deployed engineers should instead send what they learn from big customers back into the product. ([3:20](https://youtu.be/wpOA-UXynoM?t=200))
- **Software factory as a signal-to-deploy loop** — Every org has an implicit loop: signals (customer talks, bug reports, chat, exec decisions) get triaged into plans, turned into changes, validated (review, QA, security, linters, type checkers), shipped, and monitored, which produces new signals. Speaker says most orgs instrument this loop poorly. The aim is an uninterrupted flow from signal to deploy, with humans still designing it. ([4:40](https://youtu.be/wpOA-UXynoM?t=280))
- **Agent readiness is the count of deterministic validation loops** — A codebase is agent-ready in proportion to how many pass/fail checks it has (linters, type checkers, security scans, end-to-end tests). More checks let agents run longer on harder tasks without a human. Speaker says that without this, the most capable models will not show their results. ([11:53](https://youtu.be/wpOA-UXynoM?t=713))
- **Long-running harness output is bounded by validatability** — Factory's Missions product is a long-running harness for hard knowledge work with checkable outcomes. Speaker says output quality tracks how well the work can be validated, so better validators allow more autonomy. He frames tasks as the set of verifiers that must pass. ([12:53](https://youtu.be/wpOA-UXynoM?t=773))
- **Split low-hanging fixes from workflow changes** — About 30 to 40% of readiness gaps can be fixed with one command to the agent. The remaining ~60% need workflow changes, because human developers find strict automated checks nitpicky. Validation must be added without breaking developers' flow. ([12:53](https://youtu.be/wpOA-UXynoM?t=773))
- **Verification signals work like dense reward** — Speaker links this to post-training: models need dense reward on long goal-directed tasks, and verification systems provide it. So the work that matters is preparing the environment for verification, more than solving the problem itself. ([13:56](https://youtu.be/wpOA-UXynoM?t=836))
- **Exemplar must be advanced but not a theme park** — Speaker compares Factory's reference codebase to Disney's EPCOT. A working example of the future can spread to other teams, but one that is too advanced makes an org think it cannot apply it to its own pace of work. Balance is needed. ([16:17](https://youtu.be/wpOA-UXynoM?t=977))
- **Hard unverifiable problems stay human** — Factory's own codebase is about 15 to 20% autonomy by its measure, and some customer codebases go further. Terminal UI flicker is hard to validate, so the team has not closed that loop yet. Speaker says visual judgment is still a human advantage. ([17:23](https://youtu.be/wpOA-UXynoM?t=1043))

## Techniques
- **Audit validation loops before deploying agents** — Count and inventory deterministic checks (lint, types, security scans, e2e tests) per repo. Add missing checks before asking agents to work autonomously. Use the count as the readiness measure. *When:* Before rolling coding agents into a codebase, especially a large one with poor test coverage.
- **Bounded long-running harness with an explicit definition of done** — The human writes the bounded task and what counts as solved, then the harness runs inference until the verifiers pass, with little intervention in between. Only the planning step is human. *When:* For tasks where completion can be checked automatically, such as migrations or other verifiable jobs.
- **Map the signal-to-deploy stages per org** — Trace how work flows from signal through planning, change, review, QA, security, and deploy, then note where feedback is missing or unautomated. Use the map to choose where agents are placed. *When:* When scoping an agent rollout across an enterprise and deciding which stage to automate first.
- **Land-and-expand with a reference implementation** — Build a working example in a few places with a customer, hand over the transformation model, and let the customer's team copy it to other parts of the org. *When:* When selling an autonomy change into a large org that resists big-bang change.
- **Split automation into one-click fixes and workflow changes** — Ship one-command fixes for the mechanical share of findings. Route the rest through workflow changes that do not stall developers. *When:* When turning a scan of agent-readiness gaps into a remediation plan.
- **Model-independent harness with owned traces and self-hosted deployment** — Keep the harness free of a single model vendor, keep all traces in the customer's environment, and allow air-gapped deployment with central governance. *When:* In regulated or high-security settings (finance, healthcare, government) where data ownership and vendor independence matter.

## Numbers
- Speaker says each code change that gets AI code review, AI QA and AI security analysis is 'maybe 87%' less likely to hit a bug (speaker's own rough figure, no source given) ([8:09](https://youtu.be/wpOA-UXynoM?t=489))
- Customer scale cited: an org of 45,000 people, possibly hundreds of thousands of engineers and tens of thousands of codebases ([8:09](https://youtu.be/wpOA-UXynoM?t=489))
- About 30 to 40% of low-hanging readiness fixes can be done by Droid with a single instruction; the other ~60% need workflow changes ([12:53](https://youtu.be/wpOA-UXynoM?t=773))
- Autonomous migrations of 30, 40, 50+ million line codebases cited as achieved ([13:56](https://youtu.be/wpOA-UXynoM?t=836))
- Factory's own codebase is roughly 15 to 20% 'autonomy' by its measure, and its autonomy ratio is in the upper 80s (speaker's words; the ratio is defined as human actions to AI actions before interruption) ([17:23](https://youtu.be/wpOA-UXynoM?t=1043))
- LegalDroid, Factory's legal workflow, is said to be maintained 100% autonomously ([18:40](https://youtu.be/wpOA-UXynoM?t=1120))

## Hot takes
- Forward-deployed engineering should not be consulting or professional services; it should feed the product.
- Model capability is not the bottleneck; agent readiness (deterministic verification in the codebase) is.
- 'Built, not bought': a software factory has to be assembled by the customer, not installed.
- Vendor-locked agent platforms are a risk because you lose model independence and ownership of traces and data.
- Engineers move from writing code to maintaining and managing the system that writes code; DevX people and PMs are best placed to make that shift.

## Tools mentioned
Factory Droid, Missions, LegalDroid, linters, type checkers, security scanners, end-to-end test suites

## Relevance to our work
- **prosharness** (2/3): ProsHarness runs long agent loops with checkpoint/resume. Missions-style validation (task defined by verifiers, outcome checked automatically) maps onto ProsHarness's checkpoint barrier. The readiness-count idea is a concrete check. → *Add a validator list to each ProsHarness run spec (tests, lint, typecheck). Only mark a checkpoint done when they pass, and flag steps with no automated check as unverified.*
- **agentos** (1/3): Speaker's argument that a customer must own traces and stay model-independent supports AgentOS's proxy and audit-log design, but the talk adds no new mechanism. → *Cite the owned-traces and model-independent-harness argument in AgentOS design notes as rationale for the L1 audit log. No code change needed.*
