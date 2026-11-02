# Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ugUeZ8-b-u0` · [watch](https://youtu.be/ugUeZ8-b-u0) · **date:** 2026-06-18 · **length:** 16:25 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Daniel Szoke · **orgs:** Sentry
- **topics:** coding-agents, testing-verification, dev-tools · **tags:** rust, vibe-coding, type-systems, compiler-feedback, deterministic-guardrails, typescript, python, sentry, sponsored

> Argues Rust's strict compiler suits agent-written code better than Python or TypeScript: compile-time checks rule out bug classes that tests and LLM review miss, and compiler errors give agents concrete fix signals. Sponsored by Sentry.

## Summary
Daniel Szoke, Rust SDK maintainer at Sentry, argues that Rust is a strong language for vibe coding, despite being hard for LLMs to write on the first try. He notes that the usual vibe-coding languages (Python, JavaScript, TypeScript) are popular because models write them easily and they run quickly. He argues the ease of generation is overrated, since the same flexibility makes mistakes easy to make. He says LLMs are fallible by design, that tests only prove incorrectness when they fail, and that agent-written tests and review agents can share the same errors. His answer is a deterministic guardrail: Rust's compiler enforces type, memory and concurrency rules before the code runs. He illustrates this with a 100-thread shared counter that compiles in Rust only when the data is made thread-safe, and shows how the compiler error names the exact offending type so an agent can fix it. He admits Rust is harder for models to get right first time, but argues that an agent in a compile-and-fix loop handles this well. The talk is sponsored, and it cites no benchmarks of its own.

## Key ideas
- **Default vibe-coding languages are Python and JS/TS** — The conventional wisdom picks Python and JavaScript/TypeScript because models write them easily and they are quick to scaffold and run. The speaker says TypeScript has likely become the top choice for agentic coding, and cites a GitHub article claiming AI pushed TypeScript to the top of GitHub by contributor count. ([1:03](https://youtu.be/ugUeZ8-b-u0?t=63))
- **Ease of generation is overrated** — The speaker argues that a language being easy for a model to write is not automatically good. The dynamic flexibility that makes generation easy also makes it easy to make mistakes, some of them obvious. Typing helps, but TypeScript and typed Python give limited safety, and an 'any' type can undo it. ([3:28](https://youtu.be/ugUeZ8-b-u0?t=208))
- **Tests and LLM review are not enough on their own** — LLms are fallible by design. Tests can only prove incorrectness when they fail, and it is impractical to test every input. Tests written after the implementation often check implementation details rather than behaviour. If agents write the tests or the reviews, they can make the same kinds of mistake. ([4:26](https://youtu.be/ugUeZ8-b-u0?t=266))
- **Use deterministic guardrails (Murphy's Law framing)** — Speaker argues that anything that can fail eventually will. Human review, agent review and tests all help, but without an absolute deterministic check you will see failures. The speaker wants checks that do not depend on judgement. ([8:00](https://youtu.be/ugUeZ8-b-u0?t=480))
- **A compiling Rust program rules out whole bug classes** — Rust is a compiled language that aims for C/C++ speed with memory and type safety. The compiler enforces type safety, null safety (an Option type must be checked before use) and fearless concurrency. The speaker's point is that if the code compiles, a lot of bug types are ruled out. ([9:09](https://youtu.be/ugUeZ8-b-u0?t=549))
- **Data race as a compile error, not a runtime surprise** — A counter shared by 100 threads should end at 100. In TypeScript a race like this might compile and run, and only show a wrong value now and then, which is hard to debug. In Rust the non-thread-safe shared type does not compile. ([11:47](https://youtu.be/ugUeZ8-b-u0?t=707))
- **Compiler messages give agents a concrete fix target** — The error says the future cannot be sent between threads safely, and deeper in the message it names the exact type (Rc<RefCell<i32>>) that is not Send. An agent that reads this can swap in a thread-safe type. The speaker argues agents suit this compile-check-fix loop. ([13:08](https://youtu.be/ugUeZ8-b-u0?t=788))
- **Accept a harder first attempt for a stronger loop** — Rust is harder for LLMs to get right first time because there are more rules. The speaker argues this is a good trade-off: an agent in a loop can compile, read failures and fix them, and each compile error is a bug kept out of production. He claims compiling is faster than an agent review, which he does not measure. ([14:35](https://youtu.be/ugUeZ8-b-u0?t=875))

## Techniques
- **Compile-in-the-loop repair** — Let the agent write code, run the compiler, read the diagnostics and fix errors, repeating until the build passes. Keep the diagnostics rich so the agent can act on them. *When:* Use with statically checked languages whose compiler messages are specific, especially when agents write code autonomously.
- **Deterministic checks before LLM review** — Order the checks so deterministic tools (compiler, type checker, tests) run first and the LLM review comes after. Treat the review as a second layer, not the main safety net. *When:* Use for code where memory, concurrency or type bugs are costly and where agent review or tests might miss them.
- **Use error messages that name the concrete type** — Read past the top-line error to the detailed explanation, which names the exact type or trait causing the problem, and ask the agent to fix that specific item. *When:* Use when an agent is stuck on a type or thread-safety error and needs a specific fix rather than a general one.
- **Choose a language by how strongly its checker constrains output** — When picking a language for agent-written production code, weigh how many bug classes the checker rules out against how easy the language is to generate, rather than generation ease alone. *When:* Use when deciding the stack for a new agent-written service or tool, especially one with concurrency or memory-safety risk.
- **Write tests first when an agent writes tests** — Prompt the agent to write the tests before the implementation, so tests check behaviour rather than code that already exists. The speaker notes that tests written afterwards often test implementation details. *When:* Use whenever an agent both writes the code and the tests for it.

## Numbers
- Cited GitHub article: AI pushed TypeScript to the top language on GitHub by contributor count (late 2025 article, cited as a claim, not verified by the speaker). ([1:03](https://youtu.be/ugUeZ8-b-u0?t=63))
- Shared-counter example: 100 threads each add 1 to a counter, so the expected result is 100. The unsafe version in a dynamic language could give other values only occasionally. The talk gives no benchmark, cost or latency data. ([11:47](https://youtu.be/ugUeZ8-b-u0?t=707))

## Hot takes
- The ease of an LLM writing a language is overstated, and in some cases it is a bad thing.
- Tests can only prove incorrectness when they fail, so they cannot give the proof a strict compiler gives.
- Rust is harder for LLMs to get right first time, and that is a good trade-off.
- Compiling is faster than having an AI agent review your code, and it catches things the review might miss.

## Tools mentioned
Rust, rustc (Rust compiler), TypeScript, Python, Sentry

## Relevance to our work
- **agentos** (1/3): AgentOS L1 (Govrix Scout) is a Rust proxy, so the compile-in-the-loop idea applies when agents write Rust for it. The talk gives no evidence beyond the argument. → *When agents write Rust for the Govrix Scout proxy, make cargo check and clippy an agent loop step with diagnostics fed back, and measure how many first-try failures it catches.*
- **prosharness** (1/3): ProsHarness uses plan, critique and debate. The talk's point is that LLM review should sit on top of deterministic checks, not replace them. → *Add a deterministic gate (build, tests, type check) before the Codex critique step in the ProsHarness plan loop, and check whether it catches failures the LLM critique misses.*
- **general** (1/3): Recurring interest in evals and agent verification. The talk argues that tests and LLM review share the same blind spots, which matters for any eval design. → *When designing an agent eval, include at least one deterministic check that does not use an LLM judge, and compare its results with the judge's.*
