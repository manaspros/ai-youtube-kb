# Does Code Quality Still Matter? It Depends on This — Max Kanat-Alexander, Capital One

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `bU5gDVyu_28` · [watch](https://youtu.be/bU5gDVyu_28) · **date:** 2026-10-22 · **length:** 16:23 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Max Kanat-Alexander · **orgs:** Capital One
- **topics:** software-factory, context-engineering, testing-verification · **tags:** code quality, durable vs disposable software, rigor cost, standardization, in-workflow tooling, linting, test infrastructure, disposable software, maintainability, AI-generated code

> Max Kanat-Alexander (Capital One) argues code quality only matters for durable software: it's worth rigor when consequences, replacement cost, dependencies and maintenance are high, and rigor is cheaper when you standardize and automate it.

## Summary
The talk frames all software success around two things: understanding what the system actually does, and being able to modify it safely. Code quality practices exist to serve those two, and the real risk is that understanding decays non-linearly over time. The speaker splits software into durable (long-lived, high consequence, high maintenance) and disposable (cheap to replace, few dependents, little maintenance), and argues that AI-generated disposable software is about to become far more common. Rigor should scale with where a system sits on that spectrum, and the speaker says that for disposable software code quality does not matter while for durable software it does. The practical message is to reduce the cost of rigor itself: standardize tooling and frameworks, make checks in-workflow (fast, reliable, automatic), provide fakes and fast deterministic tests, and enforce strict linting early. He also suggests making systems more disposable through isolated environments, enforced independence and redundancy with a clunky durable backup. The talk is a conceptual framework with no benchmarks or case data, so the evidence is a single practitioner's opinion.

## Key ideas
- **All software success reduces to two understandings: what the system actually does, and how to modify it correctly and safely.** — Debuggers, observability, evals and tests all exist to improve understanding or the ability to act on it. Code quality practices serve those two factors and nothing else. ([1:02](https://youtu.be/bU5gDVyu_28?t=62))
- **Structure is what really matters in code, and understanding decays non-linearly.** — Components with recognizable identity are understandable; a large unstructured pile of instructions is not. Difficulty of understanding compounds over time, and every postmortem he cites reduces to poor understanding or a system made harder to understand. ([3:57](https://youtu.be/bU5gDVyu_28?t=237))
- **Software sits on a durable-to-disposable spectrum, and rigor should match the position.** — Four factors decide it: consequences of failure, cost of replacement, dependencies, and cost of maintenance. Low on all four means disposable; high on all four means durable. He advises erring toward treating software as durable. ([9:04](https://youtu.be/bU5gDVyu_28?t=544))
- **AI makes disposable software far more common, and you can make software more disposable deliberately.** — Suggested levers: isolated environments with no customer or PII data, no inbound calls from other production systems, and an old clunky durable backup so that vibe-coded replacements can fail safely. Limit scope to a single use. ([10:03](https://youtu.be/bU5gDVyu_28?t=603))
- **Durable software will not go away, and the goal is to make rigor cheaper, not to skip it.** — He expects the absolute amount of durable software to grow. The cheaper rigor is, the easier it is to be wrong about where a system sits on the spectrum and to change your mind later. ([11:26](https://youtu.be/bU5gDVyu_28?t=686))
- **Standardization reduces the cost of rigor by eliminating possibilities.** — Fewer languages, frameworks, linters and RPC protocols means fewer tools and practices to maintain. Agents can set up tooling, but only if you ask for it every time. ([12:48](https://youtu.be/bU5gDVyu_28?t=768))
- **In-workflow tooling must be free, fast, reliable and low in false positives so people do not have to choose to run it.** — Tools that run automatically are the ones that get used. Test infrastructure should make every test fast and deterministic without requiring expert testing knowledge. ([14:07](https://youtu.be/bU5gDVyu_28?t=847))
- **Maximum strictness up front is cheaper than turning on lints later.** — Set lint rules to maximum from the start so the codebase never accumulates a large backlog. A linter with a low false-positive rate and no catastrophic consequences is acceptable even when it is occasionally wrong. ([15:00](https://youtu.be/bU5gDVyu_28?t=900))

## Techniques
- **Place software on a durable-to-disposable spectrum** — Score the system on four factors: consequences of failure, cost of replacement, number of dependencies, and cost of maintenance. Apply engineering rigor in proportion, erring toward durable when unsure. *When:* Before deciding how much testing, review, and structure a new piece of software needs, especially for AI-generated tools.
- **Make software more disposable on purpose** — Deploy to isolated environments with no customer or PII data, block inbound calls from other production systems, keep an old durable backup system as a fallback, and limit scope to one user or one task. *When:* When letting users or agents vibe-code replacements for internal tools, so failures do not reach durable systems.
- **Standardize to reduce the cost of rigor** — Restrict the set of languages, frameworks, RPC protocols and linters in use so that each check and practice only has to be built once. *When:* When a codebase or organization is adding tooling that agents or engineers must otherwise set up each time.
- **Build in-workflow tooling** — Wire checks so they run automatically in the normal workflow, are fast and reliable, and have few false positives, so nobody has to remember to run them. *When:* When rigor depends on people remembering to run tools, which is the failure mode he wants to avoid.
- **Provide in-memory fakes for services** — Have each service owner ship an in-memory fake, so tests run fast and deterministically. He notes that coding agents can now write these fakes, but someone still has to choose to make them available to everyone. *When:* When building test infrastructure for a system with many service dependencies.
- **Turn lint rules to maximum from the start** — Enable the strictest lint configuration on day one for the whole codebase, rather than enabling it later across a large existing codebase. *When:* At the start of a new codebase, or when the team can accept a one-time cost to avoid a large future backlog.

## Numbers
- Speaker says disposable software will become 'about 100,000 times more common than any other form of software'. This is a rhetorical estimate, not measured data. ([6:41](https://youtu.be/bU5gDVyu_28?t=401))
- Speaker's time budget was about 5 minutes left at 12:48 after a 16:23 talk. No other quantitative data is presented. ([12:48](https://youtu.be/bU5gDVyu_28?t=768))

## Hot takes
- Code quality does not matter for disposable software and does matter for durable software.
- Turning lint rules to maximum up front is cheaper than enabling them later.
- Future models may or may not remove the complexity problem, and he declines to bet on it.
- Coding agents can write in-memory fakes now, so a long-standing test-owner wish is achievable.
- Most software engineers spend most of their time maintaining durable systems, and that will continue.

## Tools mentioned
Chromium (example codebase), Linux (example Hello World)

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code runs. Standardized in-workflow checks, a fast deterministic test setup, and maximum lint strictness apply directly to agent-written code the harness produces. → *Make the harness's post-run checks (lint, tests, fakes) run automatically in the loop with a low false-positive rate, rather than relying on the agent to choose them.*
- **agentos** (1/3): The durable-versus-disposable framing applies to agent-generated tools, which AgentOS governs. The talk gives no concrete mechanism for AgentOS. → *Consider tagging AgentOS-generated or user-generated agent tools with a durable/disposable tier that sets which governance and eval gates apply.*
