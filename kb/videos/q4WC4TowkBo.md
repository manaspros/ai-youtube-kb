# Teach Your Agent to Prove It's Done — Nick Nisi & Zack Proser, WorkOS

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `q4WC4TowkBo` · [watch](https://youtu.be/q4WC4TowkBo) · **date:** 2026-10-18 · **length:** 1:01:04 · **format:** workshop · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Nick Nisi, Zack Proser · **orgs:** WorkOS, Cloudflare, Amp, Bun, Datadog
- **topics:** testing-verification, evals, coding-agents, context-engineering · **tags:** verification-loop, agent-self-verification, receipts, llm-as-judge, playwright, agents-md, deterministic-checks, eval-baseline

> Build deterministic verifier CLIs and evidence "receipts" so coding agents can prove their own work is done, closing the loop without the human reading every line of code.

## Summary
Nick Nisi and Zack Proser (WorkOS) run a hands-on workshop on making coding agents verify their own output instead of self-reporting success. They open with a failure mode: an agent says a form saved and the UI looks right, but nothing persisted, so the check was only on the UI half. Their core argument is that status should come from records and evidence, not model prose, and that a verifier the agent can run is the foundation for trusting agents at scale. The practical pattern is a per-app CLI (a "snack" demo tool) with subcommands for health checks, driving the UI, inspecting state, deterministic prove steps, and a judge step using a fast model for fuzzy outcomes. Failing output is fed back to the agent so it self-corrects in a loop, and passing runs leave screenshots, recordings, or test results as evidence attached to PRs. They also describe a bug-injection "saboteur vs detective" exercise to test whether the verifier itself catches bugs, and they argue that accumulated receipts become a dataset for future evals and self-improvement. Caveat: much of the session promotes WorkOS-adjacent tools and their own experiments (CTX, Ryker), and the evidence is anecdotal.

## Key ideas
- **Verification is the foundational constraint for trusting agents** — Quoting a community post: if an agent can't verify its own work, nothing else matters. The speakers argue reliability and verification matter more than raw generation as models improve. ([7:44](https://youtu.be/q4WC4TowkBo?t=464))
- **Status must come from records, not model prose** — Agents will say a task passed when a persistence or state check would fail. Fix this by making the agent prove completion through a check whose output is recorded, not through its own summary. ([11:36](https://youtu.be/q4WC4TowkBo?t=696))
- **Pin verification to a single deterministic command** — Prose instructions like 'verify in a browser' are vague and vary across agents. A script that runs bash/Playwright steps gives uniform, repeatable checks, and its output can be fed back into the agent for targeted repair. ([18:45](https://youtu.be/q4WC4TowkBo?t=1125))
- **Failures should drive future work through a self-correcting loop** — When a verifier fails, the agent reads the failure, fixes the code, and reruns, so it does not hand a broken PR back to the human. Multiplied across many lanes, this removes the need for turn-by-turn nudging. ([32:00](https://youtu.be/q4WC4TowkBo?t=1920))
- **A screenshot is not proof; the agent must run the full flow** — A screenshot can show a state reached via an impossible UI path. Verification should run start to finish through the real flow and check persistence, not just the visible result. ([31:26](https://youtu.be/q4WC4TowkBo?t=1886))
- **Split proof into deterministic checks plus a fast LLM judge for fuzzy outcomes** — Exact text matching breaks on copy changes like 'waitlisted' vs 'you're in'. A small fast model can judge whether the outcome is semantically right, while hard contracts stay deterministic. ([40:10](https://youtu.be/q4WC4TowkBo?t=2410))
- **Verifiers and receipts as a reusable, compounding asset** — Every run's receipts (flows, errors, timings, screenshots) can be fed to LLMs or aggregated overnight. The speakers argue a clean history of such runs becomes an advantage for future evals and self-evolving harnesses. ([37:59](https://youtu.be/q4WC4TowkBo?t=2279))
- **Each missed case becomes a new check in the eval baseline** — Use the saboteur/detective exercise: inject a random bug and see whether the verifier finds it. Every miss is a new line in the verification map, and verifiers themselves need tests. ([45:47](https://youtu.be/q4WC4TowkBo?t=2747))
- **Enforce verification through repo instructions and CI, not skills alone** — Put the verify command in AGENTS.md, and wire it into CI, git hooks, or agent hooks. A questioner argued skills depend on the model choosing to follow them; the speakers agreed on instructions plus enforcement as the easiest route to team-wide adoption. ([54:39](https://youtu.be/q4WC4TowkBo?t=3279))

## Techniques
- **Per-app verifier CLI with subcommands** — Build a script (e.g., pnpm snack) exposing doctor (env/session/build health), drive (join, reload, reset), inspect (snapshot, storage, console, network, screenshot), prove (deterministic assertions), and judge (LLM). Agents call it as a tool and get structured output. *When:* Any web app without a bespoke verifier; the speakers call this the highest-leverage first step for an unpaved codebase.
- **Deterministic end-to-end prove step with Playwright** — Assert the pre-state is empty, fill the input, click the button, assert the status element contains the expected text, then reload and assert persistence. Mirrors a standard E2E test. *When:* Regression proof for a feature; reusable as a regression test on later changes.
- **System-one LLM judge for fuzzy outcomes** — Pass the page state or screenshot to a fast small model with a rubric, not an exact string match, so the check tolerates wording changes. *When:* UI copy or output is free-form and exact matching causes false failures; keep hard contracts deterministic.
- **Doctor/preflight plus stale-proof detection** — Run environment checks first. Tie each proof to the current code state so an old receipt cannot pass for a new change. *When:* Before trusting any verifier result, especially after code has changed between runs.
- **Centralized verifier gate on workflow nodes (CTX)** — The agent reports completion to a service over MCP; the service runs a known verifier (e.g., GitHub API checks that a PR exists and merge checks pass) and marks the node satisfied only if it passes, otherwise returns the remaining failures. *When:* Multi-step workflows where agent claims need independent verification and reusable verifiers across an org.
- **Babysitter agent for PR follow-through** — A separate agent takes the PR after the human hands off the idea, fixes failing tests and review comments, reruns verification, and alerts the human only when needed. *When:* Reducing the human's time on the final 10% of shipping work across many PRs.
- **Generate many variants and select via eval** — With a reliable eval, spawn many implementations of the same feature and keep the one that passes the most checks. *When:* When tokens are cheap relative to human review time and the eval is trustworthy.
- **Saboteur/detective bug-injection test of the verifier** — Inject a random bug (e.g., a wrong port or a broken persistence path) and check whether the verifier names it with evidence. Track false negatives and false positives as they appear. *When:* To validate that a verifier actually catches regressions before depending on it.
- **Evidence attached to PRs** — Post screenshots, recorded walkthroughs of the user flow, and test results on the PR (the speakers mention the GitHub CLI for this) so a human can review the outcome without reading the code. *When:* When reviewing agent-written PRs and the outcome matters more than the diff.
- **Outcome-first prompting with clear stop conditions** — Specify the destination and the command that proves it (e.g., 'you're done when this command returns X') rather than step-by-step paths, letting the agent find its own route. *When:* With current frontier models; the speakers say they only recently became good enough at this.
- **Error messages written for agents** — Make failure output explicit about what failed and the state that led to it, so the agent can self-repair from the message alone. *When:* Any codebase where agents will run and debug the code themselves.
- **Post-deploy monitoring agent** — After a mostly agent-implemented rollout, a separate agent watches metrics (e.g., Datadog) and feature flags and can recommend or trigger a revert. *When:* Production rollouts of agent-written changes; described as an emerging pattern, not a proven one.

## Numbers
- An agent deleted a production database in 9 seconds (incident referenced as motivation) ([0:34](https://youtu.be/q4WC4TowkBo?t=34))
- Team member reportedly ships ~900 PRs a month with no incidents (anecdotal) ([10:30](https://youtu.be/q4WC4TowkBo?t=630))
- Speakers run 18–30 terminal tabs on an average day; one says 10–15 agents is normal for him ([12:43](https://youtu.be/q4WC4TowkBo?t=763))
- Some folks reportedly achieve thousands of PRs a month with verification-first loops (anecdotal, unverified) ([19:51](https://youtu.be/q4WC4TowkBo?t=1191))
- Reptile code-review score of 5/5 plus passing CI gives high confidence against production breakage (speaker's experience) ([58:33](https://youtu.be/q4WC4TowkBo?t=3513))
- Speaker runs three agents in parallel at the conference; normally 10–15 ([56:54](https://youtu.be/q4WC4TowkBo?t=3414))
- Model provider offers about $5 free credit on signup (workshop note) ([44:41](https://youtu.be/q4WC4TowkBo?t=2681))

## Hot takes
- If your web app has no custom verifier CLI, building one is the highest-leverage thing to do before anything else.
- Source code matters less than the verification. If verifiers are strong, you can rewrite the app (the Bun-to-Rust example) and prove the rewrite works.
- A successful screenshot is not proof; agents can reach a visible state through paths the real UI does not allow.
- Skills alone are unreliable for enforcement; put verification in AGENTS.md and enforce it in CI or hooks.
- Error messages are now more important than ever because the agent is the one reading them.
- There is no universal verifier. Each team's evals will differ widely, so you have to build them for your app.

## Tools mentioned
Playwright, Chrome DevTools, pnpm, GitHub CLI (gh), GitHub API, Cloudflare Workers, MCP, Reptile, CodeRabbit, Datadog, Claude Code, Pi, ChatGPT, AGENTS.md, CTX (speakers' own tool), Ryker (speakers' own tool), Snack (workshop demo tool)

## Relevance to our work
- **prosharness** (3/3): The talk's centralized verifier gate (node satisfied only when an external check passes, with failures fed back) maps directly onto ProsHarness's plan/checkpoint flow and would change how nodes are marked done. → *Add a verifier gate per plan node: a node moves to satisfied only when a deterministic verify command exits 0, and on failure feed the failing-check output back into the Claude Code run instead of accepting the agent's self-report.*
- **agentos** (2/3): The talk's receipts-as-dataset idea addresses SkillForge's open question about the success signal for mining telemetry into skills. → *Define a run receipt schema (verifier pass/fail, evidence path, failing checks) and use verifier outcome as the success label for SkillForge's skill-worthiness scoring.*
- **general** (2/3): Putting one verify command in AGENTS.md and writing failure messages for agent self-repair is cheap and applies to any repo the team touches. → *For each active repo, add a single verify command to AGENTS.md/CLAUDE.md, require the agent to run it before declaring done, and make failure output state what failed and why.*
