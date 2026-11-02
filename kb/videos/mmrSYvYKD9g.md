# This Linter Rejects AI Slop From Your Code

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `mmrSYvYKD9g` · [watch](https://youtu.be/mmrSYvYKD9g) · **date:** 2026-09-02 · **length:** 4:41 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Better Stack host (unnamed in transcript) · **orgs:** Better Stack, Oxc
- **topics:** coding-agents, testing-verification, dev-tools, token-cost-efficiency · **tags:** oxlint, anti-slop, linting, typescript, type-assertions, zod, claude-code, claude-md, agent-code-quality, hard-fail-gates

> Better Stack demo of the anti-slop rule package for oxlint, which hard-fails low-evidence TypeScript/JavaScript patterns and whose error messages give coding agents a fix to apply.

## Summary
The speaker argues that CLAUDE.md rules are easy for agents to ignore, while lint rules are a deterministic hard fail that is also cheaper in tokens. The tool is the anti-slop rule package for oxlint, a Rust-based JS/TS linter from Oxc. The point is to hand-pick the rules that match your team's standards, not to enable all of them. A demo file with double type assertions (unknown, then a User type) and a function returning unknown shows descriptive errors that name the problem and the fix, such as validating at the boundary with Zod or returning a named domain type. Claude Code is asked to "fix all issues in api client"; it runs the lint script after each edit and repairs until clean, taking a few minutes. The speaker says lint errors are not bugs in themselves but catch the lost type evidence that later causes bugs, such as an API date that is really a string. The package was created the week before, and the speaker claims oxlint is 50 to 100 times faster than ESLint without showing a benchmark. The video is short, has no sponsor segment, and ends with a subscribe request.

## Key ideas
- **Lint rules beat CLAUDE.md rules for keeping slop out: agents can ignore or work around prose rules, while a lint failure is deterministic and cheaper in tokens.** — The speaker says no amount of CLAUDE.md tweaking reliably stops slop, and that linting is a hard fail on the patterns you want out. ([0:00](https://youtu.be/mmrSYvYKD9g?t=0))
- **anti-slop is a set of oxlint rules that reject low-evidence TypeScript and JavaScript patterns, and you should hand-pick the subset that matches your team's standards.** — The package has many rules, including chain type assertions, unknown parameters and unknown returns. The speaker says the point is not to enable all of them. ([0:00](https://youtu.be/mmrSYvYKD9g?t=0))
- **Lint error messages explain why and how to fix, which makes them useful feedback for an agent in a way raw TypeScript errors are not.** — Example messages: an assertion chain discards type evidence (fix: keep the original precise type or validate untrusted input at the boundary, e.g. with Zod); a function exposes unknown to its caller (fix: validate at the boundary and return a named domain type). ([1:00](https://youtu.be/mmrSYvYKD9g?t=60))
- **Run the agent in a generate, lint, repair loop: the lint script in package.json runs oxlint on the source, and Claude fixes its own errors.** — The demo prompt was 'fix all issues in api client'. Claude ran for a few minutes and cleared all flagged issues, with almost all rules enabled in the lint config. ([2:10](https://youtu.be/mmrSYvYKD9g?t=130))
- **Lint findings are not bugs, but they catch the lost type evidence that becomes bugs.** — Casting an API response to an Account type where created is a Date compiles, yet JSON returns a string. Because the cast discarded the evidence, TypeScript cannot warn, and the first date operation fails. ([3:09](https://youtu.be/mmrSYvYKD9g?t=189))
- **The package is new and built on oxlint, which the speaker presents as much faster than ESLint.** — The speaker says the package was created last week, that he has used it for months, and that some users reported more slop errors than they expected. ([3:09](https://youtu.be/mmrSYvYKD9g?t=189))

## Techniques
- **Hand-picked lint gate for agent-written TS/JS** — Install the anti-slop rules for oxlint, add a lint script to package.json that runs oxlint on the source directory, enable only the rules that match team standards (the speaker's demo config enables almost all), and make lint a required pass before an agent's change is accepted. *When:* A TypeScript or JavaScript repo where agents write code and CLAUDE.md rules are being ignored.
- **Agent self-repair loop on lint output** — Prompt the agent to fix all issues in a module (the demo used 'fix all issues in api client'). The agent writes code, runs the lint script, reads the rule messages, and repairs until the linter exits clean. *When:* Cleaning up or generating a module where the lint messages state the fix precisely enough for the agent to act without extra prompting.
- **Validate untrusted input at the boundary instead of casting** — Replace chained casts such as as unknown as User on JSON responses with a runtime schema (the speaker names Zod) at the API boundary. Return a named domain type from the function rather than unknown. *When:* Any code that receives JSON from an API and would otherwise use type assertions to make the compiler accept it.

## Numbers
- Speaker says oxlint is benchmarked at 50 to 100 times faster than ESLint. The speaker shows no benchmark, so treat it as an unverified claim. ([3:09](https://youtu.be/mmrSYvYKD9g?t=189))
- Claude completed the 'fix all issues in api client' task in a few minutes (roughly 2-3 minutes). ([2:10](https://youtu.be/mmrSYvYKD9g?t=130))
- The anti-slop package was created about one week before the video. The speaker has used it on his projects for a few months, which is inconsistent with the package's age and is probably a slip in the transcript. ([3:09](https://youtu.be/mmrSYvYKD9g?t=189))
- Video length is 4:41. ([0:00](https://youtu.be/mmrSYvYKD9g?t=0))

## Hot takes
- Lint rules are a deterministic gate on agent output and beat CLAUDE.md prose rules, which agents ignore.
- Linters are not new, but their explanatory messages are now useful input for coding agents.
- Do not enable every rule in an anti-slop-style package; choose the subset your team agrees on.
- Unverified: oxlint is 50 to 100 times faster than ESLint (no benchmark shown).

## Tools mentioned
oxlint (Oxc; Rust-based JavaScript and TypeScript linter), anti-slop (rule package for oxlint; created the week before the video), Oxc (the toolchain that oxlint belongs to), Claude Code, CLAUDE.md, TypeScript, ESLint (comparison point only), Zod (suggested runtime validation)

## Relevance to our work
- **prosharness** (2/3): ProsHarness runs Claude Code in loops and checkpoints. A deterministic lint step after each agent edit, with rule messages fed back, fits that loop better than CLAUDE.md rules. → *Add a lint step to the ProsHarness edit-and-repair loop for TS or JS targets, with the rule messages passed back to the agent, and measure how many fix iterations it saves.*
