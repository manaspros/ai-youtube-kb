# The Death of the Code Review: What the Data Actually Says — Laurie Voss, Arize AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `_mi3alkqy4s` · [watch](https://youtu.be/_mi3alkqy4s) · **date:** 2026-10-04 · **length:** 24:41 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Laurie Voss · **orgs:** Arize AI, NPM Inc, OpenAI, Cursor, GitHub, Cognition, Anthropic, Bun, Stripe, CodeRabbit, Greptile, Graphite
- **topics:** pr-code-review, evals, testing-verification, observability · **tags:** code-review, human-in-the-loop, mergeability, review-harness, false-positives, agent-generated-code, security-review, prompt-injection, production-trajectories, benchmarks

> Laurie Voss (Arize AI) argues that agent code generation has outrun human review, so teams should stop reviewing PRs by hand and build an engineered review harness, with humans designing its definition of good.

## Summary
The speaker says code generation has become cheap while human review throughput has not, so review is now the bottleneck on shipping. He cites a Cisco study showing reviewers lose effectiveness past roughly 400 to 450 lines, and a Meter-style test where maintainers merged only about half of the PRs that passed SWE-bench. He describes FrontierBench, a mergeability benchmark where a top model drops from 88% on SWE-bench Pro to 29% on the hardest slice. Automated reviewers in production (GitHub Copilot, Cursor, CodeRabbit, Greptile, Graphite) rely on multi-pass filtering and on human acceptance as their success metric. Experiments that removed humans (OpenAI's Codex project, the Bun Zig-to-Rust port, Carlini's C compiler) left hidden costs or needed human-written harnesses, and Dexter Horthy publicly reversed his no-review position. His conclusion is that human checkpoints survive where correctness is hard to check or blast radius is large, so humans should move up to designing reviewers, rules and evals, with production trajectories as the last reviewer.

## Key ideas
- **Code generation sped up far more than shipping.** — Cited study of 100k+ GitHub developers: agent users wrote about 741% more code but shipped only about 30% more software. The speaker treats review as the choke point. ([1:05](https://youtu.be/_mi3alkqy4s?t=65))
- **Human review has a hard capacity limit.** — Cisco study (2,500 reviews, 3.2M lines, 10 months): defect-finding drops past about 400 lines in one sitting and falls off past about 450 lines per hour. By his math a 10,000-line agent PR needs 3 to 4 working days of real review. ([3:47](https://youtu.be/_mi3alkqy4s?t=227))
- **Passing the tests is a weak proxy for mergeability.** — In a Meter-run test, open-source maintainers judged PRs that had already passed the SWE-bench grader. Only about half were mergeable. Failures were code quality and quiet breakage outside the test suite. ([6:25](https://youtu.be/_mi3alkqy4s?t=385))
- **A machine-checkable mergeability rubric exists in early form.** — FrontierBench (Cognition): 150 tasks from 20+ maintainers' repos, each over 40 expert hours, graded on correctness, regression, safety, scope, test quality and maintainability. The best model scores 88% on SWE-bench Pro but 29% on the hardest slice. GPT-5.5 scores under 6%. ([7:53](https://youtu.be/_mi3alkqy4s?t=473))
- **Whoever sets the review standard shapes the next models.** — Verifiers (compilers, tests) became training signals. A reliable mergeability benchmark would also become one, so the definition of good is a training decision. ([9:18](https://youtu.be/_mi3alkqy4s?t=558))
- **Automated reviewers need false-positive filtering and a suspicious default.** — Cursor's first reviewer ran 8 passes per diff and shuffled reviewer order, keeping findings that held up. A Peking University team found multi-pass agreement raised review quality by up to 44%. Cursor also had to tell the model not to trust code by default. ([11:43](https://youtu.be/_mi3alkqy4s?t=703))
- **Review fuses with repair, and the success metric is human acceptance.** — Cursor's reviewer spawns a fix agent and returns a diff, which adds a human approval step. Most vendors measure success as whether a human accepts the suggestion, which the speaker says is a preview of models optimizing for human approval. ([13:10](https://youtu.be/_mi3alkqy4s?t=790))
- **Skipping human review has hidden costs.** — Bun's agent-driven Zig-to-Rust port passed 99.8% of its tests but had 13,044 unsafe blocks versus about 74 in a comparable human-written codebase. OpenAI's no-manual-code project moved review into agent-to-agent loops and still needed humans to write the harness. ([16:43](https://youtu.be/_mi3alkqy4s?t=1003))
- **Human checkpoints survive in predictable places, and reviewers themselves need review.** — Humans stay where correctness is not cheaply checkable and where blast radius is large, moving up to designing the reviewer and the definition of good. Automated reviewers can be fooled: the speaker cites a study where a vulnerable diff with an innocent commit message fooled an agent reviewer 88% of the time versus 35% for humans. ([19:26](https://youtu.be/_mi3alkqy4s?t=1166))
- **Production trajectories become the last reviewer.** — Once pre-merge review is automated, step-by-step traces of what the shipped system actually did become the remaining check. The speaker frames this as the job of production monitoring, without pitching a product. ([22:00](https://youtu.be/_mi3alkqy4s?t=1320))

## Techniques
- **Multi-pass review with consensus filtering** — Run several independent review passes over the same diff, shuffle reviewer order, and keep only findings that recur across passes. Cursor and a Peking University study both report better precision this way. *When:* When automated review produces false positives that make developers ignore it.
- **Default-suspicious reviewer prompt** — Instruct the reviewing model explicitly not to trust code by default and to assume something is wrong. Cursor found the model otherwise tended to approve plausible code. *When:* When the LLM reviewer approves code too readily.
- **Tool-using reviewer over the whole repo** — Let the reviewer read the diff, call tools, and decide where to dig, rather than only reading the diff. Greptile builds a repo graph so it can see how a change lands in distant code. *When:* When changes break code outside the diff and single-pass diff review misses them.
- **Runtime verification by the agent itself** — Make the app bootable at every change so the agent can run it, inspect the UI, and check that a bug is fixed. OpenAI exposed the whole logging stack to the agent for this. *When:* When the diff alone cannot show whether a bug is fixed or behaviour is right.
- **Machine-checkable mergeability rubric** — Turn the maintainer's review questions (correctness, regression, safety, scope, test quality, maintainability) into graded checks, as FrontierBench does. *When:* When you need to measure whether agent PRs would actually be merged, not just whether tests pass.
- **Codify the definition of good as a harness** — Write down company context, domain rules and acceptance criteria as the review harness, then scale agents against it. Humans maintain the rules and evals rather than reading each diff. *When:* When review volume exceeds what humans can read line by line.

## Numbers
- Agent users wrote about 741% more code but shipped only about 30% more software (study of 100k+ GitHub developers, cited as three economists). ([1:05](https://youtu.be/_mi3alkqy4s?t=65))
- Cisco study: reviewers stop finding defects effectively past about 400 lines in one sitting and fall off past about 450 lines per hour (2,500 reviews, 3.2M lines, 10 months). A 10,000-line PR means 3 to 4 working days of review. ([3:47](https://youtu.be/_mi3alkqy4s?t=227))
- Stripe reported migrating a 50M-line Ruby codebase in a single day, estimated at over two months for a team (from Anthropic launch materials, as cited by the speaker). ([2:26](https://youtu.be/_mi3alkqy4s?t=146))
- Maintainers judged SWE-bench-passing PRs mergeable only about half the time. ([6:25](https://youtu.be/_mi3alkqy4s?t=385))
- FrontierBench: top model 88% on SWE-bench Pro vs 29% on the hardest FrontierBench slice; GPT-5.5 under 6%. 150 tasks, 20+ maintainers, 40+ expert hours each. ([7:53](https://youtu.be/_mi3alkqy4s?t=473))
- GitHub Copilot reviewer: 60M reviews, more than 1 in 5 code reviews on GitHub. ([10:28](https://youtu.be/_mi3alkqy4s?t=628))
- Multi-pass review agreement raised review quality by up to 44% (Peking University team). ([11:43](https://youtu.be/_mi3alkqy4s?t=703))
- Cursor's resolution rate (human acceptance of reviewer output) rose from 52% to over 70%. ([14:27](https://youtu.be/_mi3alkqy4s?t=867))
- Carlini: 16 agents built a C compiler in Rust that compiled the Linux kernel over about 2,000 sessions with no human approving code as written. ([14:27](https://youtu.be/_mi3alkqy4s?t=867))
- Bun Zig-to-Rust port: about 1M lines in 6 days, 99.8% of the test suite passing, 13,044 unsafe blocks vs about 74 in a comparable human-written codebase. ([16:43](https://youtu.be/_mi3alkqy4s?t=1003))
- OpenAI no-manual-code project: about 1M lines, about 1,500 merged PRs in five months, three engineers. ([5:08](https://youtu.be/_mi3alkqy4s?t=308))
- Vulnerable code with an innocent commit message fooled an autonomous review agent in 88% of attempts vs 35% for a human reviewer. ([20:44](https://youtu.be/_mi3alkqy4s?t=1244))
- CodeRabbit has reviewed over 13 million pull requests. ([13:10](https://youtu.be/_mi3alkqy4s?t=790))

## Hot takes
- Stop reviewing PRs line by line; it is the wrong level of abstraction for 2026.
- Whoever writes today's review standard is writing next year's default model behaviour.
- Review did not disappear at OpenAI; it was rebuilt as a system that humans had to build.
- Automated reviewers are easier to fool than humans, so removing humans can remove the hardest-to-fool check.
- Passing tests is a weak proxy for mergeability; the strongest models are nowhere near passing human review reliably.

## Tools mentioned
GitHub Copilot code review, Cursor reviewer, CodeRabbit, Greptile, Graphite, Codex, Anthropic automated security review action, SWE-bench, SWE-bench Pro, FrontierBench

## Relevance to our work
- **prosharness** (2/3): ProsHarness already runs plan, critique and debate loops; the talk's multi-pass consensus filtering and default-suspicious prompt bear directly on critique quality and false positives. → *Trial a critique step that runs 3 independent passes and keeps only findings raised in at least two, with a prompt that tells the critic not to assume the plan is correct by default.*
- **agentos** (1/3): Speaker's point that production trajectories become the last reviewer fits the L4 observability work, but the talk is about PR review, not AgentOS's core pillars. → *Read the trajectory-as-reviewer idea once and consider whether L4 OTel traces could record step-by-step agent actions for post-merge checks on agent-written code.*
