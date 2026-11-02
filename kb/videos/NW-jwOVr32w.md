# The Design-Code Roundtrip That Isn't — Jonathan Gordon, ReWeaver AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `NW-jwOVr32w` · [watch](https://youtu.be/NW-jwOVr32w) · **date:** 2026-09-18 · **length:** 18:37 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Jonathan Gordon · **orgs:** ReWeaver AI, Microsoft, Figma, Anthropic, Cursor, Sketch
- **topics:** product-ux, vibe-coding-app-building, governance-compliance · **tags:** design-to-code, round-trip, drift, deterministic-guardrails, provenance, accessibility, design-system, figma, vibe-coding, product-pitch

> Jonathan Gordon (ReWeaver AI) argues a lossless design-code round trip is not yet solved and proposes deterministic guardrails plus provenance to control drift around LLM-generated UI code.

## Summary
Jonathan Gordon, founder of ReWeaver AI, defines a true design-code round trip as a lossless, bidirectional loop with provenance, and says prior handoffs failed because design and engineering goals diverged. He describes his own vibe-coding experience, including catching an unsafe innerHTML change mid-generation, which led him to read the code. He tested five tool setups for code-to-design-to-code round trips and found design changes survived but code changes and bindings were lost. His harness shows a design system built from code in Figma, plus a "show drift" report that scans code and design together across nine guardrail dimensions, including accessibility (e.g., a missing ARIA live region). His experiment ran 12 iterations of pure LLM generation, which started around 30% fidelity, and adding deterministic guardrails improved results, with the remaining ~10% needing human judgment. The talk is largely a product pitch for ReWeaver, so the evidence is anecdotal and no independent benchmark is shown.

## Key ideas
- **Define the goal as a lossless, bidirectional design-code loop with provenance** — A true round trip should keep fidelity in both directions and record where each line or element came from, so changes can be traced to their source. ([1:15](https://youtu.be/NW-jwOVr32w?t=75))
- **Past handoffs failed because outcomes diverged, not because of tooling alone** — Engineering optimized for technical constraints while design optimized for a future vision, so the loop was never closed. He thinks one LLM that understands design intent and writes code may close it at inference speed. ([2:45](https://youtu.be/NW-jwOVr32w?t=165))
- **Reading the generated code caught a real security problem** — While vibe coding he noticed an innerHTML change, a known injection risk, and stopped the agent. This led him to stop trusting unreviewed output. ([5:16](https://youtu.be/NW-jwOVr32w?t=316))
- **Five tool setups failed to close the loop in both directions** — Design edits survived the trip, but code edits did not, and bindings were lost. He thinks some tooling will be needed to surface drift. ([11:04](https://youtu.be/NW-jwOVr32w?t=664))
- **Drift is the long-term tech debt, and deterministic guardrails should wrap the AI** — Per-session drift shows up while coding, but drift over time piles up across the codebase. He argues for deterministic reconciliation around non-deterministic models, with a human accepting or refusing each fix. ([13:31](https://youtu.be/NW-jwOVr32w?t=811))
- **Pure LLM output starts around 30% fidelity; guardrails and fixes raise it** — In a 12-iteration test on a complex UI, LLM-only generation degraded slightly from about 30% fidelity. Adding deterministic checks and fixes improved it, and the remaining gap needs human judgment. ([12:05](https://youtu.be/NW-jwOVr32w?t=725))
- **Accessibility is a concrete, checkable guardrail for generated code** — LLM-generated code often lacks accessibility basics. An example is a missing ARIA live region that stops screen readers from announcing a change. The tool flags it and proposes a fix. ([9:37](https://youtu.be/NW-jwOVr32w?t=577))

## Techniques
- **Design-system extraction from code into the design canvas** — Prompt an LLM to pull styles and components from an existing app into a design file, and to build a design system that is also live in runtime code. Keep code and design in sync through shared tokens and components. *When:* When a product already has a codebase and a design system, and the goal is to keep design and code aligned.
- **Joint drift report across code and design** — Scan the code and the design together, then list issues across dimensions such as design quality, code quality, performance, tokens and accessibility. Each issue can be accepted and fixed, or refused. *When:* Before merging AI-generated UI changes, to catch mismatches between design intent and shipped code.
- **Deterministic guardrails around LLM generation** — Keep the LLM as the generator, but run rule-based checks on its output and apply fixes that a human approves. Track fidelity over iterations to see if quality drifts. *When:* When AI-written code must meet fixed standards such as design consistency or accessibility, and cost and control must stay with humans.
- **Fidelity metric per iteration (production drift ratio)** — Score each generation with a drift ratio, and use a lower score as the target. He ran a public challenge asking for a score below 0.30. *When:* To compare generation runs and track whether repeated AI edits degrade quality.
- **Undo and review loop for AI code edits** — Let the tool write fixes, but show code as it is written, and allow the user to cancel or undo before anything merges. *When:* When an agent edits code and the human needs to stay in control of each change.

## Numbers
- Pure LLM generation began at about 30% fidelity (true pixel-perfect) and degraded slightly over 12 iterations on a complex UI ([12:05](https://youtu.be/NW-jwOVr32w?t=725))
- Five different tool setups were tried for bidirectional round trips; design changes survived but code changes and bindings were lost ([11:04](https://youtu.be/NW-jwOVr32w?t=664))
- Public challenge threshold: a production drift ratio (PDR) below 0.30 earns a beta seat; beta planned for mid-July ([17:00](https://youtu.be/NW-jwOVr32w?t=1020))
- Nine top-level guardrail dimensions for software quality and production readiness ([15:57](https://youtu.be/NW-jwOVr32w?t=957))
- Speaker claims about 10% of quality needs human judgment and cannot be automated ([12:05](https://youtu.be/NW-jwOVr32w?t=725))

## Hot takes
- The design-code round trip is not solved yet; industry claims of a true round trip overstate what works.
- Drift over time is the new tech debt, and it will be more costly than drift in a single session.
- AI generation needs deterministic guardrails and human accept/refuse decisions, not more agent autonomy.
- Human judgment is required for the last ~10% of design fidelity and cannot be automated away.

## Tools mentioned
Figma, Sketch, Cursor, Claude Code, ReWeaver

## Relevance to our work
- **prosharness** (1/3): Deterministic checks on Claude Code output before approval echo ProsHarness's approval and gate flow, but the talk is about UI design fidelity, not long-run checkpoints or planning. → *Consider adding a deterministic rule-check step, such as lint or spec-match, between a Claude Code run and the phone approval, and log the pass rate per run.*
- **general** (1/3): Shows a pattern of deterministic checks around LLM generation with humans accepting or refusing fixes, which applies to any agent-written code. → *Read the talk's guardrail framing next to the existing ProsHarness approval flow to decide whether a rule-check pass belongs before merge.*
