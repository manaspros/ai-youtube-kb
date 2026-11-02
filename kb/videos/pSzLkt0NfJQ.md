# How IBM’s Bob uses "Review Mode" to solve the hardest coding tasks (Full Breakdown)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `pSzLkt0NfJQ` · [watch](https://youtu.be/pSzLkt0NfJQ) · **date:** 2026-05-02 · **length:** 8:06 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Andrus · **orgs:** IBM, Better Stack
- **topics:** coding-agents, pr-code-review, dev-tools · **tags:** ibm-bob, review-mode, cobol, legacy-modernization, security-scan, auto-fix, ide, granite, modes, auto-approval, streamlit, sqlite

> Better Stack walkthrough of IBM's Bob IDE, which separates ask/code/plan modes and runs a security Review mode with a findings panel and one-click fixes; tested on the ZBank COBOL repo, with a short sponsored-style pitch for the free trial.

## Summary
Better Stack tests IBM's Bob, a Granite-powered IDE pitched as architectural governance rather than vibe coding. The host opens Bob's mode picker (ask, code, plan, custom modes) and shows a /review command that scans for hard-coded secrets, injection risks and OWASP issues, surfacing findings in a triage panel. He asks Bob to modernize the ZBank COBOL repo into a Streamlit Python app, which takes about three minutes and runs functionally, though the UI shows weak design judgment. Each finding has a light-bulb auto-fix that also offers a unit test; the race-condition fix was a one-line SQLite BEGIN IMMEDIATE change. Reviewing the original COBOL found eight issues, but Bob added no tests because there is no COBOL test tooling in the repo. The host closes by preferring IDEs to CLIs for visibility, and mentions a free trial with 40 Bob coins, where the run cost about four coins (roughly 50 cents per coin). The evidence is one demo on one repo, with no benchmarks.

## Key ideas
- **Bob separates planning from execution with explicit modes (ask, code, plan, custom) rather than one chat window.** — The host frames Bob as built for architectural governance, contrasting it with vibe coding, and points to the mode picker at the bottom of the chat. ([1:11](https://youtu.be/pSzLkt0NfJQ?t=71))
- **A slash review command runs a security audit in the IDE and gives a findings panel for triage.** — Built-in guardrails look for hard-coded secrets, injection risks and weak OWASP practices. A CLI version, Bob Shell, is also available. ([1:11](https://youtu.be/pSzLkt0NfJQ?t=71))
- **Auto-approval can be scoped to a sandbox rather than clicked through.** — Before the agent acts, a modal lets you pick which actions it may take without asking. The host allowed read and write on the repo only. He admits most people just hit approve. ([3:24](https://youtu.be/pSzLkt0NfJQ?t=204))
- **Each review finding can be auto-fixed, and the fix can be followed by a generated unit test.** — The light-bulb button fixes an issue, then Bob asks whether to add a test for it and runs the test. A diff view shows the changes. ([4:46](https://youtu.be/pSzLkt0NfJQ?t=286))
- **The COBOL review found eight issues, but the fix flow produced no tests.** — Bob did not add tests because the legacy mainframe repo has no test framework in it. The host reads this as a sign that the stack was tested manually. ([5:45](https://youtu.be/pSzLkt0NfJQ?t=345))
- **The host prefers IDE panels for approvals and findings over CLI agents, because he cannot see what a CLI agent is doing.** — This is a stated personal preference, not a measured result. ([6:47](https://youtu.be/pSzLkt0NfJQ?t=407))

## Techniques
- **Mode-separated agent workflow** — Use ask mode for questions, code mode for implementation and plan mode for planning. Define custom modes for other phases. The mode picker is at the bottom of the chat panel. *When:* When you want planning, coding and review kept as separate phases with different permissions.
- **Scoped auto-approval** — Use the auto-approval modal before the agent starts to pick exactly which actions it may take unattended, such as read and write limited to the repo. *When:* When you would otherwise approve everything and need a defined sandbox for an autonomous run.
- **Review-then-fix-then-test loop** — Run the slash review command for a security audit. Open a finding, click the light-bulb auto-fix, review the diff, then accept the offer to add a unit test that confirms the fix. *When:* For triaging security and bug findings in a legacy or unfamiliar codebase where you want each fix verified by a test.
- **Atomic SQLite write for a race condition** — The reported fix for a race condition was to change the SQLite transaction to BEGIN IMMEDIATE so that the write lock is taken up front. *When:* When a read-then-write sequence on SQLite can race between concurrent writers.

## Numbers
- Modernizing the ZBank COBOL repo into a Streamlit Python app took about 3 minutes. ([3:24](https://youtu.be/pSzLkt0NfJQ?t=204))
- The review on the original COBOL code reported eight issues. ([5:45](https://youtu.be/pSzLkt0NfJQ?t=345))
- The free trial includes 40 Bob coins. The test run cost about 4 coins, and 1 coin is about 50 cents USD. ([6:47](https://youtu.be/pSzLkt0NfJQ?t=407))

## Hot takes
- Bob is built for architectural governance rather than vibe coding.
- IDE panels for approvals and findings give a more structured view than CLI agents, which the host says he cannot follow.
- Most people just hit auto-approval all the time, so scoped sandboxes are rarely used in practice.

## Tools mentioned
IBM Bob, Bob Shell, IBM Granite, ZBank (open-source COBOL repo), Streamlit, SQLite, COBOL, VS Code

## Relevance to our work
- **prosharness** (1/3): Scoped auto-approval and the findings-triage loop are close to ProsHarness's approval and review ideas, though the video shows them only in an IDE. → *Compare Bob's scoped auto-approval modal with ProsHarness's phone-driven approvals to see if a per-action permission scope is worth adding.*
