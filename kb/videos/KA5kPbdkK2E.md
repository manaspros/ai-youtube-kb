# How Lovable self-improves every hour — Benjamin Verbeek, Lovable

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `KA5kPbdkK2E` · [watch](https://youtu.be/KA5kPbdkK2E) · **date:** 2026-06-18 · **length:** 19:05 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Benjamin Verbeek · **orgs:** Lovable
- **topics:** skills-self-improvement, evals, observability, vibe-coding-app-building · **tags:** continuous-learning, knowledge-base, stuck-detection, llm-judge, holdout-eval, agent-feedback, vent-tool, vibe-coding, incident-detection, auto-pr

> Benjamin Verbeek (Lovable) on two continuous-learning loops: a self-updating "Stack Overflow" of fixes for stuck users, and an agent "vent" tool that reports platform friction to engineers.

## Summary
Lovable, a vibe-coding platform, wants a mistake to happen once and never again. The speaker splits "stuck" users into three groups: stuck but solvable with better prompting, blocked by a missing or buggy feature that is easy to fix, and blocked by hard problems that need weeks of work. An LLM judge scans sessions for repeated requests, complaints and abandonment, and the team focuses on sessions that go from stuck to unstuck without the user quitting. Each such fix is clustered, generalised, checked by an agent that runs a quick eval, and stored in a knowledge bank. A lightweight model injects the matching entry at the start of a new query. A small random sample gets blank injections so the team can compare outcomes against sessions that could have received the fix, then prune stale entries when models or features change. The second loop gives the agent a vent tool that sends feedback to Slack when tooling, docs or platform behaviour blocks it; the trigger prompt is tuned for high signal. An agent now dedupes these reports, investigates them and opens PRs that engineers review and merge. Vent volume spikes also turned out to be a useful incident detector.

## Key ideas
- **Define 'stuck' from behaviour, then split it into three classes** — Stuck means asking for the same thing again, complaining, or giving up. Stuck users fall into: (a) solvable with better prompting, (b) not supported but easy to add or a bug, (c) hard, needing weeks of AI-assisted engineering. Classes (a) and (b) should be fixed fast. ([5:38](https://youtu.be/KA5kPbdkK2E?t=338))
- **Mine the moment a user goes from stuck to unstuck** — An LLM judge flags sessions. The high-signal sample is the transition from stuck to not stuck, excluding cases where the user simply gave up. That gives a real problem plus a working fix. ([7:43](https://youtu.be/KA5kPbdkK2E?t=463))
- **A Stack Overflow for the agent, kept fresh by eval** — Fixes are clustered so entries generalise and do not overfit to one prompt. An agent reviewer generates and runs a quick eval (a human only when uncertain). A lightweight model injects matching entries into the main agent at query start. ([8:46](https://youtu.be/KA5kPbdkK2E?t=526))
- **Measure injection with blank holdouts and prune hard** — On a small sample the system injects nothing even when it could. Injected and could-have-been-injected projects are compared on overall success, and entries are shown more or less accordingly. Entries go stale with each new model or feature, so content is rebalanced and removed often. ([9:51](https://youtu.be/KA5kPbdkK2E?t=591))
- **Give the agent an outlet, tuned for low noise** — A vent tool lets the agent report when tooling, docs or platform behaviour materially slows it. The prompt is tuned to fire only on real frustration, because forcing an answer every turn produces noise and overfitting. Reports go to Slack. ([13:17](https://youtu.be/KA5kPbdkK2E?t=797))
- **The agent sees friction that users cannot diagnose** — Users rarely know why they are stuck, but the agent has been working the problem for several turns. Its reports exposed a copy tool that failed on file names with spaces. The first fix missed non-breaking spaces from WhatsApp and Mac screenshots, so reports kept coming until the fix was done properly. ([14:45](https://youtu.be/KA5kPbdkK2E?t=885))
- **Vent volume doubles as an incident signal, and a bot triages it** — Spikes in vent events lined up with platform incidents, such as broken sandboxes. An agent now dedupes reports, investigates them and opens PRs. Engineers review and merge, and review requests come to the phone. ([17:16](https://youtu.be/KA5kPbdkK2E?t=1036))

## Techniques
- **Stuck-session detection with an LLM judge** — Run a judge over conversation logs to flag repeated requests, complaints and abandonment. Track the isStuck flag over time and keep sessions that transition stuck to not-stuck without abandonment. *When:* You have many agent sessions and want to find fix candidates without reading them by hand.
- **Clustered, generalised fix knowledge bank** — Cluster similar failures, write a generalised fix instead of a per-prompt rule, verify it with an agent-run quick eval, store it, and inject the match into the main agent at query start with a cheap model. *When:* The same class of agent failure recurs across users and the fix can be stated generally.
- **Blank-injection holdout** — Randomly skip injection for a small sample of cases where it would apply. Compare outcomes (for example, project completion) between injected and held-out groups, then show each entry more or less based on the result. *When:* You need causal-ish evidence that injected context helps, and want to catch stale context.
- **Tuned agent vent tool** — Give the agent a tool with a trigger prompt listing concrete friction classes (missing tools, unclear schemas, conflicting docs, environment failures, repeated failed attempts). Tune it until the signal is high, and route the output to a team channel. *When:* The agent runs in a product you own and has more context than the user about why a task failed.
- **Agent triage of agent feedback** — A monitoring agent dedupes reports, investigates them and opens a PR. A human reviews and merges. *When:* The volume of reports is too high for manual triage but fixes still need human review.
- **Feedback volume as an incident detector** — Chart the count of agent-originated complaints over time and treat spikes as a signal of a platform problem. *When:* You want an early warning that complements your normal monitoring.

## Numbers
- Over 200,000 projects created per day on Lovable, a significant share of all new websites built there ([3:03](https://youtu.be/KA5kPbdkK2E?t=183))
- User base grew from a few thousand users when the speaker joined about a year earlier ([3:03](https://youtu.be/KA5kPbdkK2E?t=183))
- After the copy-tool vent went live, the team got about 20 complaints about the same file-name bug in the first hour ([14:45](https://youtu.be/KA5kPbdkK2E?t=885))
- Internal model rankings: top-ranked models all use the Stack Overflow knowledge bank, which gives a significant boost in internal ratings (no figures given) ([10:48](https://youtu.be/KA5kPbdkK2E?t=648))
- Early data: messages with fixed intent or users being stuck are dropping significantly, and more projects reach deploy, a key completion metric (no figures given) ([10:48](https://youtu.be/KA5kPbdkK2E?t=648))

## Hot takes
- A non-technical user who hits one technical block usually leaves, so removing stuck points matters more than raw model capability.
- Let the agent complain to its creators. Its view of the failure is often better than the user's, and it is cheaper than an external reviewer on every turn.
- Stale fix knowledge becomes context rot. Prune it aggressively whenever the model or the product changes.
- Overfitting to noise is the main risk with any LLM-judge or feedback loop; tune the trigger for signal, not coverage.

## Tools mentioned
Slack, Framer Motion

## Relevance to our work
- **agentos** (2/3): SkillForge needs a success signal and skill-worthiness scoring; the injected-vs-blank-holdout comparison on project completion is a concrete way to score a skill's effect. → *Prototype a holdout for SkillForge: skip injecting a mined skill on a small sample of matching sessions and compare task completion, to use as the success signal for skill-worthiness.*
- **general** (2/3): The stuck-to-unstuck transition plus a blank-holdout check is a reusable method for mining fixes from agent sessions into CLAUDE.md or skills, and for testing whether they help. → *Label stuck-to-unstuck transitions in local Claude Code session logs with a cheap LLM judge, then A/B a candidate CLAUDE.md rule on a held-out subset of similar tasks.*
- **prosharness** (1/3): A tuned agent-initiated feedback tool fits ProsHarness's phone approvals and loop structure, though it is not core to the current milestone. → *Consider a strict-trigger 'report friction' tool for the Claude Code harness, routed to the existing phone notification channel.*
