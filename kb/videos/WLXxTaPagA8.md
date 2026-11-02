# Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD - Sumaiya Shrabony

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `WLXxTaPagA8` · [watch](https://youtu.be/WLXxTaPagA8) · **date:** 2026-07-18 · **length:** 10:51 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Sumaiya Shrabony · **orgs:** ?
- **topics:** testing-verification, evals, observability, multi-agent · **tags:** ci-cd for agents, blocking gates, handoffs, voice contract, deduplication, audit trail, solo builders, content pipeline, Claude Code

> Solo agent builders keep rebuilding CI/CD-style controls (regression tests, alerts, contracts, staging, audit trails) one failure at a time; the talk argues for blocking gates at the most expensive handoff.

## Summary
Sumaiya Shrabony describes her content-generation agent system (scheduler, research, content plan, production skill, verifier, reviewer, output folder) and the controls she rebuilt after failures. The dangerous failure, she argues, is a polished artifact that looks ready but would fail the team's gates: generic AI-marketing voice, an unsupported statistic with an empty verification log, or a near-duplicate hook. Her demo shows a guarded mode that blocks these cases before the ready folder, while a naive mode lets them through. She names five controls she reinvented: regression testing, failure alerting, boundary contract testing, staging checkpoints, and audit logging that records which gate failed and why. Her advice is to map every handoff, pick the one where bad data costs the most, and make that gate block rather than warn. The talk has no benchmarks; its value is the gate taxonomy.

## Key ideas
- **Solo agent builders end up rebuilding CI/CD controls badly, one failure at a time.** — The sequence is regression testing after a prompt or skill change, alerts after a silent cron failure, boundary validation after a schema change, staging checkpoints before the ready folder, and audit logs when no one can find the bad prompt or handoff. ([0:00](https://youtu.be/WLXxTaPagA8?t=0))
- **Every handoff between agent steps is a place where the system can lie.** — Her content system has seven handoffs (scheduler to command, research to content plan, plan to production skill, production to verifier, verifier to reviewer, reviewer to output). Nobody checks them when one person builds alone. ([1:19](https://youtu.be/WLXxTaPagA8?t=79))
- **The dangerous failure is a polished artifact that passes at a glance, not an obviously bad output.** — Artifacts with the right sections and a ready status can still break voice, verification, or duplication rules. She compares shipping them to shipping code that was never tested. ([2:48](https://youtu.be/WLXxTaPagA8?t=168))
- **Voice drift is caught by a voice contract at a blocking gate.** — A generic LinkedIn-style paragraph has all required sections, so a shape check alone passes it. Guarded mode blocks it at the voice contract; the gate does not rewrite the content. ([5:41](https://youtu.be/WLXxTaPagA8?t=341))
- **Claims need a verification trail before they can ship.** — A specific statistic (37%) appeared with an empty verification log. She treats a confident claim with no source as an unverified assertion, and says trusting the model is not a verifier. ([7:01](https://youtu.be/WLXxTaPagA8?t=421))
- **Near-duplicate hooks are the most realistic failure for solo builders, and need a dedup check against history.** — The new piece is technically coherent but reuses an opening angle already in the vault history. Guarded mode blocks it at the deduplication check. ([7:01](https://youtu.be/WLXxTaPagA8?t=421))
- **Each gate should write an audit record naming the gate, the contract, and the reason.** — When a scheduled run fails at 2 am, the final artifact alone is not enough. You need to know which gate failed and which contract was violated, without rerunning the whole pipeline. ([8:00](https://youtu.be/WLXxTaPagA8?t=480))
- **Map the handoffs, then put the first gate on the most expensive one, and make it block.** — Pick the handoff where bad data costs the most (a public wrong claim, a broken schema that cascades, a duplicate that erodes trust). A gate that only warns is a suggestion, not a gate. ([9:23](https://youtu.be/WLXxTaPagA8?t=563))

## Techniques
- **Boring blocking gates before save** — Add checks that stop the artifact from moving forward: a pre-save output contract (required shape), a voice or domain contract, a verification contract (claims traced to a source), a dedup check against history, and an audit record per gate. *When:* Any agent pipeline whose outputs are published or passed to other steps, especially when run unattended.
- **Guarded vs naive mode demo** — Run the same pipeline with the gate off and on, and show that the naive run produces a ready-looking artifact that the guarded run blocks. *When:* To show that demos on the happy path hide failures.
- **Handoff mapping** — List every arrow from input to final output, then choose the most expensive one (by cost of bad data, not complexity) for the first gate. *When:* Before adding a new agent or gate to a multi-step system.
- **Per-gate audit record** — Record which gate ran, which contract it checked, the verdict, and why, so a failed run can be reconstructed without rerunning it. *When:* Scheduled or background agent runs where failures happen off-hours.
- **Voice and domain contracts as explicit rules** — Write the rules the output must follow as a checkable contract, then test outputs against it rather than relying on the prompt alone. *When:* Content or domain-specific outputs where generic model wording is a known failure.

## Numbers
- Seven handoffs in her content system, and 12 content pieces produced per run. ([1:19](https://youtu.be/WLXxTaPagA8?t=79))
- A 37% rework-reduction figure appears in her demo artifact as an unverified example claim. It is illustrative, not evidence. ([5:41](https://youtu.be/WLXxTaPagA8?t=341))

## Hot takes
- A gate that only warns is not a gate, it is a suggestion.
- The most dangerous agent failure is a polished artifact that looks ready, not an obviously bad output.
- Solo agent builders reinvent regression testing, alerting, contract testing, staging, and audit logs without noticing.

## Tools mentioned
Claude Code

## Relevance to our work
- **agentos** (2/3): AgentOS already has an audit log and a PII/prompt-injection scan, but the talk's per-gate record (which gate, which contract, why) and blocking-by-default gates are a different design from warn-only scanning. → *Make each AgentOS guardrail check emit a structured verdict record (gate id, contract, pass/block, reason) and test that a block stops the request, not just logs a warning.*
- **prosharness** (2/3): ProsHarness checkpoints long Claude Code runs and runs plan, critique, and debate stages. A blocking verification gate between stages, with an audit record, fits that design. → *Add a blocking gate before a checkpoint is marked done that requires a verification record for any claim in the plan, and log which contract failed when it blocks.*
