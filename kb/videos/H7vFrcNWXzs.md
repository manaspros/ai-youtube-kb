# Building ambitious software — Jonathan Kelley, Dioxus Labs & Cognition

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `H7vFrcNWXzs` · [watch](https://youtu.be/H7vFrcNWXzs) · **date:** 2026-09-18 · **length:** 19:14 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Jonathan Kelley · **orgs:** Dioxus Labs, Cognition
- **topics:** coding-agents, testing-verification, context-engineering · **tags:** rust, dioxus, claude-code, coding-agents, architecture, fuzzing, code-review, release-engineering, documentation, prompt-intent, open-source

> Dioxus Labs (now part of Cognition) on building an ambitious Rust framework with coding agents: fast on knowledge work and mundane upkeep, weak at tests, and architecture plus review now carry the load.

## Summary
Jonathan Kelley, co-creator of Dioxus, describes five years of building a cross-platform Rust app framework (Dioxus, the Blitz HTML/CSS renderer, and the SubSecond hot-reload engine) and how the team changed its workflow once coding agents became good at Rust. The team first generated lots of agent code that did not clear its merge bar, which he calls a "slop cannon" problem. They recovered by treating Rust's strict compiler as a guardrail the agents work against, using agents for knowledge-heavy work (platform plugins, CSS behavior, release checklists, backports, doc comments), and using them to build fuzzing harnesses. Agents still write shallow tests, so humans enumerate test conditions. Architecture and intent communication now take most of the team's time, and every PR is still read line by line. The closing point is that code is now cheap but quality is not, and reading code matters more than writing it. The talk is a practitioner account from a small team (three core engineers) and it reports its own limits honestly.

## Key ideas
- **Agent-written code piled up in drafts because it failed the team's merge bar, so 'more agent output' was not the win.** — After tens of thousands of lines of agent-written Rust, very little cleared the quality bar. He calls this becoming a 'slop cannon' and says the team did not yet know how to use these tools properly. ([5:37](https://youtu.be/H7vFrcNWXzs?t=337))
- **Rust's strictness, which the team once tried to reduce for humans, now works in the agents' favor.** — Developer-friendly error messages and ergonomics matter less to agents. The compiler's bar checker and the language's difficulty catch agent mistakes, so the learning curve he fought to reduce is now a feature. ([7:00](https://youtu.be/H7vFrcNWXzs?t=420))
- **Define what 'ambitious' means for your project before choosing how much to delegate.** — For Dioxus the priorities are: the code works and can be fixed easily, the codebase stays maintainable because velocity sits on top of it, new features ship on a long roadmap, and patch releases never break APIs that businesses depend on. Speed trades off against that quality bar. ([8:19](https://youtu.be/H7vFrcNWXzs?t=499))
- **Agents are strongest on knowledge-heavy problems that no small team can hold in its head.** — Kotlin and Swift plugins deeply integrated into the build system took about two to three weeks, with the implementation done on day one and the rest spent on tests and real-device checks. Agents also recall how Chrome and Safari handle CSS and layout, so the team can choose the right fix over the hacky one. ([9:44](https://youtu.be/H7vFrcNWXzs?t=584))
- **Routine upkeep is a major agent win, and it keeps the release cadence high.** — Agents handle release checklists, backporting fixes to stable branches, and auditing doc comments and examples, which often drift out of date. Patch releases are now more frequent than ever, at a weekly or multiple-times-a-week pace. ([12:23](https://youtu.be/H7vFrcNWXzs?t=743))
- **Agents write shallow tests and need humans to decide what to test; they are better at building test harnesses.** — Agents tend to test trivial things such as a constructor. Humans still enumerate test conditions and write test APIs, and agents help brainstorm edge cases. Agents do well at building fuzzing harnesses that throw malformed and adversarial inputs at the software. ([13:43](https://youtu.be/H7vFrcNWXzs?t=823))
- **Architecture is now the bottleneck, and sloppy architecture gets amplified faster.** — Agents rarely hesitate to do large refactors and just ship, so bad structure compounds quickly. Most of the team's time now goes to architecture and how features will fit the future system. The code-writing share of time shrinks. ([16:15](https://youtu.be/H7vFrcNWXzs?t=975))
- **Human line-by-line review and intent communication still matter, especially for outside PRs.** — The team uses AI review to catch bugs early, but humans still read every line. Outside contributors often do not communicate the intent behind a change, and models depend heavily on the prompt, so prompt quality shapes the result. ([17:39](https://youtu.be/H7vFrcNWXzs?t=1059))

## Techniques
- **Let the compiler's strictness act as the agent's guardrail** — Keep strong types and a strict compiler in the stack so agent mistakes fail fast, and do not optimize the language for human ergonomics at the cost of checks. *When:* Choosing or keeping a language/toolchain that will be used heavily by coding agents.
- **Agents as a knowledge oracle for platform and spec behavior** — Ask the agent how a reference engine (Chrome, Safari) or a spec handles a CSS or layout case, or how a platform API works, instead of reading the source yourself, then pick the principled fix. *When:* Debugging obscure platform, rendering or spec-level behavior.
- **Delegate checklist-style maintenance to agents** — Give the agent the release checklist, backport steps, or a doc-comment audit (every public item has an example and matches its behavior) as a concrete task with clear done-criteria. *When:* Repetitive, well-specified upkeep work such as release verification, backports and docs.
- **Agent-built fuzzing harnesses** — Have the agent write harnesses that feed large volumes of malformed and adversarial inputs into the software under test. *When:* Hardening parsers or any entry point that receives untrusted input.
- **Human-enumerated test conditions with agent brainstorming** — Use the agent to propose edge cases for an area, then have a person choose the conditions and build the test APIs and runners. Do not accept agent-generated tests that only exercise trivial constructors. *When:* Writing tests for behavior that matters, where shallow coverage would give false confidence.
- **Architecture-first, then implementation, with full PR reading** — Settle the architecture and the intent for a change in text before the agent implements it, run AI review as a bug pre-filter, and keep a human reading every line of what ships. *When:* Running an agent-heavy workflow on a large open-source or long-lived codebase.

## Numbers
- Dioxus has nearly 37,000 GitHub stars and millions of downloads. ([2:39](https://youtu.be/H7vFrcNWXzs?t=159))
- Apps built with Dioxus have a cumulative estimated reach of over 200 million end users. ([2:39](https://youtu.be/H7vFrcNWXzs?t=159))
- Blitz apps are under 5 MB bundle size and use under 50 MB of RAM at runtime, compared with Electron apps. ([4:08](https://youtu.be/H7vFrcNWXzs?t=248))
- SubSecond recompiles changed code and patches the running app in about 100 milliseconds. ([4:08](https://youtu.be/H7vFrcNWXzs?t=248))
- Kotlin and Swift plugins took about two to three weeks with agents, with the implementation done on day one and the rest spent on testing. ([11:05](https://youtu.be/H7vFrcNWXzs?t=665))
- The core team is three engineers. ([12:23](https://youtu.be/H7vFrcNWXzs?t=743))
- The team shipped more patch releases in its most recent version than ever before, at a weekly or multiple-times-a-week cadence. ([13:43](https://youtu.be/H7vFrcNWXzs?t=823))

## Hot takes
- Code is now cheap, but quality is not.
- Rust's difficulty is now a feature for coding agents, because the compiler catches their mistakes.
- Reading code has always mattered more than writing it, and that matters more as the project grows.
- Agent-written tests tend to be sloppy and check trivial things, so humans must decide what to test.
- Most engineering time now goes to architecture and intent, not to writing code.

## Tools mentioned
Claude Code, Rust, Dioxus, Blitz, SubSecond, Firefox (CSS engine), Electron, React Native, Flutter, Kotlin, Swift, Zed, WebAssembly

## Relevance to our work
- **agentos** (1/3): Govrix Scout is a Rust proxy that handles untrusted prompts (PII and injection scanning). The talk's fuzzing-harness point applies to that input surface, though it is not a direct change to what we build. → *Ask a coding agent to write fuzz harnesses for Govrix Scout's request parser and its PII and prompt-injection scanner, using malformed and adversarial inputs, and log the crashes or misses it finds.*
- **prosharness** (1/3): ProsHarness wraps Claude Code with planning, checkpoints and review, and the talk's point that architecture and intent are the bottleneck fits its plan stage. The talk does not describe any harness mechanism. → *Consider having the ProsHarness plan stage require a short written intent and architecture note, reviewed before any implementation starts, and check whether it reduces the amount of agent code that gets rejected at review.*
- **general** (1/3): Practitioner account of agent-driven quality limits, including the 'slop cannon' failure and where agents fail on tests. Useful background for any agent-written code pipeline. → *Read the transcript's sections on tests and fuzzing (13:43 to 14:57) before designing verification for agent-written code.*
