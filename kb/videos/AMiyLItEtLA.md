# fighting slop with slop — Vaibhav Gupta, Boundary

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `AMiyLItEtLA` · [watch](https://youtu.be/AMiyLItEtLA) · **date:** 2026-08-18 · **length:** 21:32 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Vaibhav Gupta · **orgs:** Boundary, BAML
- **topics:** software-factory, context-engineering, testing-verification, dev-tools · **tags:** slop, architecture-invariants, dependency-graph, transcript-analysis, design-docs, BAML, language-design, cli-tools, error-handling, ab-testing

> Vaibhav Gupta of Boundary argues that teams without code review can keep AI-written code stable by building internal tools that enforce invariants, mine agent transcripts, and rethink the language and tooling layers underneath.

## Summary
The speaker says his team (Boundary) skips code review, lets engineers work in parallel, and does not standardize AI tools, while building BAML, a language where behavior must be exactly the same every time. His core claim is that "slop" is any code nobody reads, so the answer is to fight slop with more agent-run tooling rather than manual review. The team keeps a tiny architecture.md that holds only invariants expected to last months, requires reading for design docs (code may be slop, writing may not), and uses a dependency-graph tool with CLI guards in CI to catch leaky packages. They run agents on BAML tasks, collect full transcripts, have agents flag wasteful tool-call patterns, have humans triage the findings, and A/B test language features or skills by tool calls, errors and correctness. The second half is an opinionated critique of TypeScript and JavaScript, with proposals for function-level CLIs, type-inferred error handling and a BAML bridge callable from existing languages. The talk is strongest as a set of internal-tool patterns and weakest where it is provocative and light on data.

## Key ideas
- **Slop is any code nobody reads, so the fix is agent-run tooling that checks code instead of humans reading it.** — The speaker's team has no code review. He frames the job as fighting slop with slop: build internal tools that agents and humans use to inspect outputs. ([1:11](https://youtu.be/AMiyLItEtLA?t=71))
- **Keep a tiny architecture file that holds only invariants that will not change for months.** — Engineers can use any AI tool they like, so the team shares one short architecture.md (compiler layers in their case) that every model can read, and nothing volatile goes in it. ([1:11](https://youtu.be/AMiyLItEtLA?t=71))
- **Make the rule about reading, not about writing.** — Code can be slop but design docs cannot. Versioned design docs with commenting and Slack notifications were not enough. The team's real fix was a rule that anyone who ships a design doc must have people read it, which raised quality. ([2:39](https://youtu.be/AMiyLItEtLA?t=159))
- **Turn architecture rules into CLI checks that run in CI.** — A dependency-graph visualizer plus CLI tools that guarantee certain invariants cannot break. When an agent adds a leaky package or dependency, CI or the git history shows where it broke. The speaker says the architecture has not changed in three or four months. ([4:04](https://youtu.be/AMiyLItEtLA?t=244))
- **Use agents to inspect full run transcripts, then turn findings into fixes and A/B tests.** — Agents build BAML programs from scratch, and their full transcripts are reviewed for errors and for wasteful patterns such as three tool calls where one would do. Humans triage which findings are real, agents fix them, and features or skills are compared by tool calls, error rate and correct outcome. ([5:31](https://youtu.be/AMiyLItEtLA?t=331))
- **Make the compiler carry error types so handling is checked exhaustively.** — In his BAML demo, a divide function's division-by-zero error is inferred and propagated up to calling functions automatically. The compiler can then prove whether a caller handles it. Nobody writes the error types by hand. ([14:45](https://youtu.be/AMiyLItEtLA?t=885))
- **Expose each function as a CLI command and make navigation tools describe code in one call.** — A describe-style query returns docstrings, source and usages together. Each function can also run standalone as a CLI binary, so agents can run code without grepping through its behavior. ([12:16](https://youtu.be/AMiyLItEtLA?t=736))
- **Build the new language as a bridge so existing codebases can call it.** — Every BAML function is callable from Python, TypeScript, Rust, Go and others with full types, so teams do not need a rewrite. The speaker says they also pass lambdas, generics and closures across the boundary. ([17:56](https://youtu.be/AMiyLItEtLA?t=1076))
- **Process has to change for agent speed, and early CI/CD-style investment pays back.** — He compares it to teams that added CI/CD: it slowed them down for about three months, then they moved faster. He says one engineer recently built a partial C compiler in BAML in a day. ([19:27](https://youtu.be/AMiyLItEtLA?t=1167))

## Techniques
- **Invariant-only architecture file** — Keep one short architecture file (for example compiler layers) with only facts that will not change for months. Point every agent tool at it so teams can use different tools without drifting. *When:* Many engineers use different AI coding tools and you need shared standards without enforcing a tool choice.
- **CLI guard checks for architecture invariants** — Build a dependency-graph view with semantic package boundaries and CLI checks that fail when a change breaks an invariant. Run them in CI or on commits so the break is traceable in git history. *When:* Agents add packages or dependencies faster than people can review them and you want architecture to stay stable.
- **Required reading as the gate for design docs** — Allow AI-written code to be unread, but require at least one other person to read any design doc before it is shipped. Notify a channel when docs change. *When:* A team is producing too many AI-written specs and needs a quality filter that does not depend on writing style.
- **Transcript triage loop** — Run agents on realistic tasks, save full transcripts, have agents flag excess tool calls and errors, have humans label findings as real or not, then have agents propose and test fixes. *When:* You want to improve tools, prompts or skills from observed behavior instead of guesses.
- **A/B test skills or features by agent outcomes** — Compare variants by tool-call count, error count and whether the output is correct, and choose the winner from those numbers. *When:* You need a success signal for which skill or tool variant is worth keeping.
- **Per-function CLI and describe tool** — Expose each function as a standalone CLI command, and give agents one call that returns docs, source and usages for a symbol. *When:* Agents need to learn code or library behavior fast and cheaply without many search calls.

## Numbers
- Team has been building BAML for about three years (no code review during that time). ([0:08](https://youtu.be/AMiyLItEtLA?t=8))
- Author personally shipped about 10 design docs a day while suffering from AI-driven over-production; the team then had to enforce a reading rule. ([2:39](https://youtu.be/AMiyLItEtLA?t=159))
- Architecture has not changed in the last three or four months under the CLI invariant checks. ([4:04](https://youtu.be/AMiyLItEtLA?t=244))
- Interop idea for calling BAML from other languages was started about two years ago. ([17:56](https://youtu.be/AMiyLItEtLA?t=1076))
- A CI/CD adoption slowed a team down for about three months before it sped them up. ([19:27](https://youtu.be/AMiyLItEtLA?t=1167))
- One engineer built a partial C compiler purely in BAML in one day (anecdote, no benchmark). ([19:27](https://youtu.be/AMiyLItEtLA?t=1167))

## Hot takes
- Code reviews are not necessary if a team builds enough internal tooling to enforce invariants.
- TypeScript's core design favors human productivity over correctness, so agent-first tooling needs a different foundation.
- The team needs a new Git, a new database and a new programming language.

## Tools mentioned
BAML, Claude, Codex, TypeScript, Python, Rust, Go, Ruby, Java, WASM, ripgrep, Notion, GitHub, Slack, VS Code, Effect, CoffeeScript

## Relevance to our work
- **agentos** (2/3): The A/B comparison of skills by tool calls, errors and outcomes is a concrete candidate for SkillForge's open success signal and skill-worthiness question. → *Score candidate skills in a small A/B run by tool-call count, error count and output correctness, and check whether those three signals separate good skills from bad ones.*
- **prosharness** (2/3): Architecture invariants, CLI checks and transcript triage map onto ProsHarness checkpoints, critique passes and loops. → *Add a transcript-triage step to ProsHarness run reports that counts tool calls and errors per task, then compare runs on those numbers.*
- **general** (2/3): Strong practitioner pattern for context engineering: keep the shared architecture file to stable invariants only, and enforce them with checks rather than prose. → *Trim CLAUDE.md or architecture notes to facts that will not change for months, and move volatile details elsewhere.*
