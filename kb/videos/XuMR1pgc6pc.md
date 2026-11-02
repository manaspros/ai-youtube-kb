# Is Your AI Code Producing CRAP? (Here's How To Fix It)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `XuMR1pgc6pc` · [watch](https://youtu.be/XuMR1pgc6pc) · **date:** 2026-06-02 · **length:** 6:44 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Andres (Better Stack host) · **orgs:** Better Stack
- **topics:** testing-verification, coding-agents, pr-code-review · **tags:** crap-metric, cargo-crap, cyclomatic-complexity, code-coverage, rust, code-quality, ai-generated-code, technical-debt, refactoring-risk

> Better Stack explains the CRAP metric (complexity combined with test coverage) and the cargo crap Rust tool, arguing it is a useful second check on complex, under-tested code, especially AI-generated code.

## Summary
The host introduces CRAP (Change Risk Anti-Patterns index), a metric from Alberto Savoia and Bob Evans in 2007 that flags functions that are both complex and poorly tested. It was revived by a Rust package, cargo crap, from Oleksandr Prokhoranko, who also wrote a blog post arguing it matters more now that AI agents write much of the code. The video explains cyclomatic complexity as the count of independent paths through a function, with each if, match, loop or catch adding a branch. In a demo, a function with complexity around 15 scored 13 under cargo crap with its tests in place, and commenting out the tests pushed the score past 100. The formula penalizes low coverage heavily: with full coverage the score equals complexity, while complexity 10 with zero coverage gives 110. The host suggests running the check after unit tests as a heat map for refactor risk, and notes AI agents tend to produce complex code that handles edge cases but has weak integration tests. The video is short and mostly explanatory, with a light, unmeasured claim about AI-generated code.

## Key ideas
- **CRAP (Change Risk Anti-Patterns index) finds functions that are highly complex but poorly tested, a metric first proposed in 2007 and revived by the cargo crap Rust package.** — The speaker credits Savoia and Evans for the metric and Oleksandr Prokhoranko for the Rust tool and a blog post that brought it back as AI writes more code. ([0:00](https://youtu.be/XuMR1pgc6pc?t=0))
- **Cyclomatic complexity is the number of independent execution paths in a function; every if, match, while or catch adds a fork.** — The example function has nested matches, loops and error handling, with complexity around 15, which the speaker calls hard for a human to map fully. ([0:58](https://youtu.be/XuMR1pgc6pc?t=58))
- **With full unit-test coverage, the CRAP score stays near the complexity value, so well-tested complex code is treated as safe.** — cargo crap reported 13 for a function the speaker estimated at 15; he guesses the tool skipped the error-handling path. Removing the tests sent the score past 100. ([1:57](https://youtu.be/XuMR1pgc6pc?t=117))
- **The formula penalizes complexity multiplied by lack of coverage, so the score is driven by untested complexity.** — Per the speaker, the formula combines cyclomatic complexity with coverage as a fraction. At 100% coverage the score equals complexity; complexity 10 with zero coverage gives 110. The default threshold is 30, and a team can set a stricter one such as 5. ([3:18](https://youtu.be/XuMR1pgc6pc?t=198))
- **AI agents write syntactically correct, complex code that handles edge cases but usually lack integration tests unless forced, so CRAP is meant as a second check after unit tests.** — The speaker says the score works as a heat map of technical debt, pointing to code most likely to break in a refactor. He also mentions agents duplicating functions across files and the value for onboarding. ([4:05](https://youtu.be/XuMR1pgc6pc?t=245))
- **The same author wrote a CRAP tool for Java, and the speaker encourages porting the idea to other languages.** — He says he was unaware of the metric until reading the blog post, and presents a port as a possible side project. ([5:25](https://youtu.be/XuMR1pgc6pc?t=325))

## Techniques
- **Run a CRAP check after the unit tests** — Run the test suite with coverage collection first, then run cargo crap (the cargocrap Rust package) so each function gets a score from its cyclomatic complexity and test coverage. Review the highest-scoring functions as refactor or test-writing candidates. The speaker's example shows the scores are 13 with tests and above 100 with tests commented out. *When:* On a Rust codebase after an agent or a developer makes large changes, as a second gate after unit tests pass.
- **Set a complexity budget** — Pick a per-function cutoff (the speaker suggests 5 as a strict example; the tool's default is 30) and flag any function above it, with a CRAP threshold on top if the tool supports one. Treat flagged functions as the first places to add tests or split logic. *When:* When you want a team rule for agent-written code, such as no function above a set complexity without high coverage.
- **Check that the metric reacts to test removal** — Comment out the tests for one function and re-run the CRAP tool to confirm the score jumps. The speaker uses this to show the score tracks coverage, not only complexity. *When:* When adopting the metric, to confirm the coverage data is wired in correctly before trusting the thresholds.

## Numbers
- The CRAP metric dates to 2007 (Savoia and Evans). ([0:00](https://youtu.be/XuMR1pgc6pc?t=0))
- Example function has cyclomatic complexity around 15. ([0:58](https://youtu.be/XuMR1pgc6pc?t=58))
- cargo crap reports 13 for that function with tests in place (speaker's guess for the gap: the error-handling path is not counted). ([1:57](https://youtu.be/XuMR1pgc6pc?t=117))
- With tests commented out, the cargo crap score goes above 100. ([1:57](https://youtu.be/XuMR1pgc6pc?t=117))
- Worked example: complexity 10 with 0% coverage gives a CRAP score of 110; at 100% coverage the score equals complexity. ([3:18](https://youtu.be/XuMR1pgc6pc?t=198))
- cargo crap default complexity threshold is 30; the speaker suggests 5 as a strict example. ([3:18](https://youtu.be/XuMR1pgc6pc?t=198))

## Hot takes
- The framing that AI code is 'producing CRAP' rests on an anecdote and the author's blog post; no data on AI-written code is shown.
- The 15-vs-13 gap is explained by a guess (error handling not counted) that is not verified on screen.
- The formula is described verbally with the cubic exponent; the exact expression is not written out in the transcript, and the 110 example is the only check on it.
- The metric is old and the revival rests on one Rust tool; the video itself says it is not new.
- Clickbait title with substantive but short explanatory content; no sponsor segment.

## Tools mentioned
cargo crap (cargocrap Rust package, by Oleksandr Prokhoranko), CRAP metric (Savoia and Evans, 2007), Rust, CRAP tool for Java (same author, mentioned, not shown)

## Relevance to our work
- **agentos** (2/3): Govrix Scout and other AgentOS components are Rust, and the metric targets complex, under-tested functions in agent-written code, which fits our verification and quality-gate work. → *Run cargo crap after cargo test on the Rust proxy crate (Govrix Scout) and save the top-scoring functions as a baseline before changing any code.*
- **prosharness** (1/3): ProsHarness runs long Claude Code jobs and could use a complexity-vs-coverage check as one more verification gate on agent-written code. → *Consider adding a CRAP-style check (complexity against coverage) as an optional verification gate before a ProsHarness run is marked done, if the target project is Rust.*
