# Why AI Didn't Actually Make You Ship Faster — Gabriel Spencer-Harper, Meticulous

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `HLTa7Vcs4X0` · [watch](https://youtu.be/HLTa7Vcs4X0) · **date:** 2026-10-04 · **length:** 11:15 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** Gabriel Spencer-Harper · **orgs:** Meticulous, Discord, Wiz, Dropbox, Notion, ElevenLabs, LaunchDarkly
- **topics:** testing-verification, pr-code-review · **tags:** visual-regression, record-replay, e2e-testing, flaky-tests, code-coverage, pr-review, browser-determinism, network-mocking

> A short vendor demo arguing that review and verification, not code writing, are now the bottleneck, and that screenshot-based record-and-replay of front-end flows can give near-exhaustive verification.

## Summary
Gabriel Spencer-Harper, CEO of Meticulous, argues that AI makes code generation faster than humans can review it, so verification becomes the constraint. He says assertion-based tests cannot cover the space of possible regressions, and that most teams would not merge an AI-generated PR without a long manual check. Meticulous records real user flows on non-production environments with one line of JavaScript, then replays a coverage-selected subset on each PR and screenshots every step before and after the change. The output is a set of visual diffs posted as a PR comment for a human or agent to judge, not a pass/fail verdict. The speaker claims the approach is near-deterministic because the browser's scheduling is patched and all network calls are mocked, which removes flakiness and lets tests run in parallel. The talk is mostly a product pitch with customer names and no benchmark data, so the technical ideas are more useful than the numbers.

## Key ideas
- **Verification is now the bottleneck, not code writing** — AI writes code faster than humans can review it. The speaker's claim is that only exhaustive verification lets teams ship at the speed agents write code. Without it, someone spends time verifying by hand. ([0:08](https://youtu.be/HLTa7Vcs4X0?t=8))
- **Assertion tests cannot cover the regression space** — Encoding correct behavior up front in assertions cannot cover every flag, role, permission, config and edge case. The speaker's test: if an AI wrote this PR, would you merge it? He says most organizations would say no. ([1:37](https://youtu.be/HLTa7Vcs4X0?t=97))
- **Review diffs of behavior instead of writing assertions** — The tool does not decide whether a change is a bug. It shows before/after screenshot diffs of what would change if the PR merged, and a human or agent judges whether each diff is expected. ([6:03](https://youtu.be/HLTa7Vcs4X0?t=363))
- **Mock all network I/O at record time and stub it at replay** — Recorded network requests and responses are stubbed in at replay. The speaker says this makes each test idempotent (repeatable 1,000 times with the same result) and isolated, so tests can run in parallel and finish in minutes. ([7:36](https://youtu.be/HLTa7Vcs4X0?t=456))
- **Patch the browser to remove nondeterminism** — Browsers were not designed for determinism. Sources of randomness include CPU clock speed affecting animations and interleaving of setTimeout and setInterval. The speaker says the browser scheduling layer was modified to make it near-deterministic, which he credits for far fewer flakes than Cypress or Playwright. This is his claim, with no numbers given. ([7:36](https://youtu.be/HLTa7Vcs4X0?t=456))
- **Pick a replay subset by line coverage, and screenshot every step** — Each recorded flow is replayed once on the main branch to record which lines it executes. The tool then selects a subset of flows that maximizes code coverage. Because it screenshots at every moment, the speaker argues code covered is roughly the same as code tested, since a single pixel diff anywhere in a 412-step flow gets flagged. ([8:51](https://youtu.be/HLTa7Vcs4X0?t=531))
- **Screenshot-per-step only works if flakiness is solved at the root** — Screenshotting at every possible moment produces tens to hundreds of millions of images. The speaker says that without root-level determinism, this would drown in noise, which is why the browser was modified. ([10:12](https://youtu.be/HLTa7Vcs4X0?t=612))

## Techniques
- **One-line record of real user flows in non-prod** — Inject a single script into localhost, QA, dev and staging that records real user interactions as workflows. Replay them later on PRs without writing test scripts. *When:* A front-end codebase where writing and maintaining E2E test scripts is a large share of engineering time.
- **Per-step screenshot diff of base vs PR** — Replay each selected workflow on the base commit and on the PR branch. Screenshot after every event, diff the two sequences, and post the diffs as a PR comment with before/after views. *When:* Reviewing AI-generated UI changes, where the question is what the change did to the app, not whether a specific assertion holds.
- **Record-time network mocking with replay-time stubs** — Capture all network requests and responses during recording. At replay, serve them from the recording. This makes each test deterministic and isolated. *When:* You need parallel, repeatable UI tests without a live backend, or tests that flake because of backend state.
- **Coverage-maximizing test subset selection** — Run each recorded workflow once on main and log the lines it executes. Build a workflow-to-lines index, then choose a subset of workflows that covers the most code. Run that subset on each PR. *When:* The full set of recorded flows is too large to run on every PR, and you want the subset to still exercise most of the code.

## Numbers
- Verification and test maintenance cost engineering orgs double-digit percentages of their time (manual validation, review, debugging flakes, updating tests), per the speaker ([3:04](https://youtu.be/HLTa7Vcs4X0?t=184))
- Meticulous posts its PR comment typically within a few minutes ([4:37](https://youtu.be/HLTa7Vcs4X0?t=277))
- Tests run in parallel and finish in a few minutes because each test is isolated ([7:36](https://youtu.be/HLTa7Vcs4X0?t=456))
- Claims 'orders of magnitude less flakes' than Cypress or Playwright, with no data shown ([7:36](https://youtu.be/HLTa7Vcs4X0?t=456))
- Example flow of 412 steps where a single pixel diff is flagged ([8:51](https://youtu.be/HLTa7Vcs4X0?t=531))
- Full screenshot-per-moment capture produces on the order of tens to hundreds of millions of screenshots ([10:12](https://youtu.be/HLTa7Vcs4X0?t=612))
- Named deployments: Discord, Wiz, Dropbox, Notion, ElevenLabs, LaunchDarkly, plus many others, per the speaker ([0:08](https://youtu.be/HLTa7Vcs4X0?t=8))

## Hot takes
- Code coverage is a terrible metric for every tool in the world except this one, because a Cypress or Playwright test can cover 100% of the code with a single assertion.
- If you cannot merge AI-generated PRs without a long manual check, verification is the real bottleneck, not code generation.
- Exhaustive verification changes how you program: you can bump all dependencies, make sweeping refactors, and accept any AI-generated change with confidence.

## Tools mentioned
Meticulous, Cypress, Playwright

## Relevance to our work
- **prosharness** (1/3): ProsHarness runs long Claude Code agent jobs and needs a way to show an agent's work is done. The talk's before/after diff idea applies only if a run changes a UI. → *When a ProsHarness run changes front-end code, add a before/after screenshot diff of the affected flows as an evidence artifact for the run's done-check.*
- **general** (1/3): Useful framing that verification, not generation, limits agent-driven shipping, plus the coverage-based subset idea. The product claims are unverified. → *Read the coverage-maximizing workflow-subset selection idea as a possible way to choose a minimal eval or test subset for agent-written code.*
