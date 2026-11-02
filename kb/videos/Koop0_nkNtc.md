# Vercel made a programming language

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Koop0_nkNtc` · [watch](https://youtu.be/Koop0_nkNtc) · **date:** 2026-06-02 · **length:** 8:08 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Better Stack presenter (unnamed) · **orgs:** Vercel (named in the title and as 'Vassell' in the transcript), Better Stack
- **topics:** dev-tools, coding-agents, context-engineering · **tags:** programming-language, structured-diagnostics, json-output, agent-friendly-toolchain, self-documenting-cli, xero, claude-code, rust-comparison, compile-time-capabilities

> Better Stack walkthrough of Xero, a new systems language whose toolchain emits JSON diagnostics with fix guidance so agents can repair code. A Claude fix run succeeded without docs, but the presenter doubts a new language was needed.

## Summary
The presenter walks through Xero (transcribed as "Zero" in places), a systems language pitched as built for humans and AI agents to write small native programs together. He covers hello-world, a classifier demo with enums, shapes, match, spans, owned values, drop and defer, and the explicit "world" capability for IO. The main claim is that every toolchain command can emit JSON, including diagnostics with severity, location, expected and actual values, help text, a safety/human-review flag, and a repair policy. A zero-context Claude run fixed three planted errors in about 31 seconds by calling the language's fix command until it returned okay. The presenter then argues that structured compiler errors already exist in mature languages like Rust, that LLMs already handle those well, and that a new language has no training data to lean on. His verdict is that it is a neat experiment that shows a language can carry its own agent-facing docs, but he doubts it is needed and would not use it over Rust, Zig or Go. The video has no sponsor segment and is a single-creator tool review.

## Key ideas
- **Xero is pitched as a systems language (Rust/Zig-like) whose whole toolchain is designed around structured data so AI agents can work with it** — The premise is that current languages are built for humans reading wall-of-text errors and warnings, while agents do better with JSON. The presenter notes the website copy reads as AI-written and that he is skeptical. ([0:00](https://youtu.be/Koop0_nkNtc?t=0))
- **Explicit effects: a 'world' capability marks IO and is checked at compile time against the build target** — A function with the world capability signals IO side effects; one without is IO-free. If code uses file-system access and the target is WebAssembly, the compiler errors out instead of failing at runtime. ([1:06](https://youtu.be/Koop0_nkNtc?t=66))
- **Error handling uses a 'raises' marker on functions and a 'check' keyword to propagate errors** — Presented as similar to Rust's ? operator but as a keyword. ([2:09](https://youtu.be/Koop0_nkNtc?t=129))
- **Every command has a JSON mode, and diagnostics are structured for an LLM** — Diagnostic fields include severity, code, message, location, expected and actual values, help text, a safety field that requires human review, and repair information. The presenter notes it is designed to give the LLM enough context to fix the code itself. ([4:15](https://youtu.be/Koop0_nkNtc?t=255))
- **A dedicated fix command returns repair guidance, including the fix for each error code** — The zero fix command, run in plan mode with JSON output, returns fields such as safety level, mode, whether an edit applies, a repair policy, the diagnostic list, and the documented fix for each error code. ([4:15](https://youtu.be/Koop0_nkNtc?t=255))
- **Zero-context Claude fixed a broken Xero file by calling the toolchain, with no docs or web search** — In an empty directory with no Xero information, Claude was given the diagnostics command and asked to fix the file. After about 31 seconds all three planted errors were fixed, and the run ended when fix returned okay true. ([5:17](https://youtu.be/Koop0_nkNtc?t=317))
- **Structured errors are not new, and LLMs already handle mainstream languages well** — The presenter says Rust can emit JSON errors and that a Claude fix would probably work on Rust even without structured output. Because Xero is not in training data, he thinks the demo is still impressive but questions whether a new language was needed. ([6:26](https://youtu.be/Koop0_nkNtc?t=386))
- **Verdict: a neat experiment, not something to build complex apps on** — He sees it as evidence that a language can ship its own LLM-facing context without training data, but says he would still reach for Rust, Zig or Go. ([7:18](https://youtu.be/Koop0_nkNtc?t=438))

## Techniques
- **Self-describing toolchain for agents** — Give every toolchain command a JSON mode. Include in each diagnostic a severity, code, message, location, expected and actual values, help text, a safety/human-review flag, and repair info. Add a fix subcommand that returns per-error fix guidance. The agent runs fix, applies the edit, and repeats until it returns okay true. *When:* When agents will write or repair code in a language or API they have no training data or docs for, and you can change the toolchain.
- **Zero-context fix-loop test** — Copy the broken file into a new empty directory with no docs or skills. Tell Claude to fix it and give it only the diagnostics command. Check whether it converges to okay true without web search. *When:* To check whether a CLI or language gives agents enough information to self-correct without reading documentation.
- **Explicit capability marking for IO** — Mark functions that perform IO with a world capability parameter. Functions without it are treated as side-effect free. The compiler rejects IO calls when the build target does not support them. *When:* When you want side-effect boundaries and target incompatibilities to be caught at compile time rather than at runtime.
- **Error propagation with raises and check** — Mark fallible functions with raises and propagate errors with the check keyword, similar to Rust's ? operator. *When:* When you want Rust-style error propagation expressed as keywords.
- **Scoped cleanup with owned values, drop and defer** — Use an owned type and define a drop function on the type for cleanup, or use defer to run a function when the enclosing scope ends. *When:* For deterministic resource cleanup without a garbage collector.
- **Running a Xero program** — Run `xero run <file>` on a source file with the Xero extension (the presenter shows hello.0). The presenter does not show the JSON flag name for the check or fix commands. *When:* Basic usage. Flag names are not stated in the transcript; check the Xero docs for them.

## Numbers
- Claude fixed three deliberately introduced errors in a Xero file in about 31 seconds, starting with zero Xero context and no web search. ([5:17](https://youtu.be/Koop0_nkNtc?t=317))
- The fix run ended when the fix command returned okay true, which confirmed no errors were left. ([5:17](https://youtu.be/Koop0_nkNtc?t=317))
- The video is about 8 minutes long (8:08) and gives no benchmarks, binary sizes or latency figures. The only size claim is that output 'compiles down to a nice size', which is not quantified. ([3:13](https://youtu.be/Koop0_nkNtc?t=193))

## Hot takes
- Structured JSON compiler errors are not new (for example, Rust can already emit them), so a whole language built around the idea is not clearly necessary.
- A language with no training data can still be debugged by an LLM if the toolchain carries the context, so self-documenting toolchains may matter more than the language.
- The branding and website copy read as AI-written, and the marketing overstates what a new language adds.

## Tools mentioned
Xero (systems language and toolchain, named as 'Xero' or 'zero' in the transcript), Claude (Claude Code, used for the fix run), Rust, Zig, Go, jq, Bun (mentioned only as a possible future rewrite target), WebAssembly (compile target)

## Relevance to our work
- **agentos** (1/3): Shows a pattern for agent-facing CLI output: structured diagnostics with an ok flag and per-error fix guidance. Relevant to tooling in Crucible or other AgentOS components that agents call. → *Where AgentOS tooling reports failures to an agent, add a JSON mode with severity, code, location, expected/actual values, and a fix field, and test it with a zero-context agent run in an empty directory.*
- **prosharness** (1/3): ProsHarness wraps Claude Code, so the self-correcting fix loop (run a fix command, read structured output, repeat until ok) matches how the harness should expose check results to the agent. → *Make ProsHarness check and validation commands emit JSON with an ok flag and per-issue fix hints, then test that a fresh Claude Code session converges using only that output.*
