# How to Kill the Code Review — Ankit Jain, Aviator

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `YgEv7IQzGdM` · [watch](https://youtu.be/YgEv7IQzGdM) · **date:** 2026-08-18 · **length:** 16:26 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Ankit Jain · **orgs:** Aviator
- **topics:** pr-code-review, testing-verification, context-engineering, skills-self-improvement · **tags:** code-review, alignment, spec-driven-development, acceptance-criteria, test-plan, ai-slop-registry, verification, preview-environments, human-in-the-loop, bdd, product-pitch

> Ankit Jain (Aviator) argues code review's real job is alignment, not bug-catching, and proposes reviewing agent session intent, test-plan evidence and a codified "AI slop registry" instead of diffs.

## Summary
Ankit Jain, co-founder of Aviator, says code volume now outruns human line-by-line review, and that over 30% of changes already merge without any review. He argues review's core value is alignment: knowledge sharing, mentorship and architectural feedback, which line-level review does not capture well. He says spec-driven development falls short because specs are written before unknowns surface and are never updated, and because the real decisions live in the agent prompts, which are thrown away once the PR is made. His proposed loop turns session decisions into acceptance criteria, combines them with a registry of recurring review rules into a test plan, and verifies it against a running preview, with agents collecting screenshots and database snapshots as evidence. Humans then review the intent, criteria and evidence rather than the diff. The talk is partly a product pitch for Aviator's unreleased Verify tool, and it gives no measured results for the approach itself.

## Key ideas
- **Code review is volume-bound and already failing** — Code churn and PR volume have grown faster than reviewers can keep up. Median review time has risen, and the speaker says teams spend about 4x as long waiting on reviews. Over 30% of changes merge with no review at all. ([1:03](https://youtu.be/YgEv7IQzGdM?t=63))
- **When AI reviews and nobody reads, the setup is wrong** — If AI agents write the code and also review it, the human ends up skimming. The speaker says the human has to be given a role that adds value, not a rubber-stamp one. ([2:34](https://youtu.be/YgEv7IQzGdM?t=154))
- **Review is mainly about alignment, not bugs** — Beyond catching bugs and enforcing conventions, review does knowledge sharing, mentorship, architecture feedback and onboarding. The speaker says alignment is the most important part and must survive when review moves to tooling. ([3:34](https://youtu.be/YgEv7IQzGdM?t=214))
- **Spec-driven development is waterfall without a feedback loop** — A spec is written up front and the agent is expected to implement it deterministically. But unclear points come up during coding, the spec is never updated, and LLMs are not deterministic, so the spec alone does not carry the work. ([4:59](https://youtu.be/YgEv7IQzGdM?t=299))
- **Intent lives in the prompts, and today they are discarded** — The real decisions happen in back-and-forth with the agent, not in the Jira ticket or the PRD. Teams create a PR and throw the prompts away. The speaker argues they should be kept as the record of intent. ([5:50](https://youtu.be/YgEv7IQzGdM?t=350))
- **Recurring review comments should become codified rules** — The speaker calls this an AI slop registry: each repeated review comment is captured as a rule, so it is no longer re-raised by hand. He says the registry gets better as humans keep adding to it, though he does not show how. ([6:28](https://youtu.be/YgEv7IQzGdM?t=388))
- **Session to acceptance criteria to test plan to preview** — The user's answers and decisions in the agent session become acceptance criteria. Those are combined with the registry's invariants into a test plan, which runs against a spun-up preview. Reviewers look at evidence that the intent was met, not at the code. ([7:52](https://youtu.be/YgEv7IQzGdM?t=472))
- **Build the test plan from the session, not from the code** — If the same agent writes the code and the tests from the code, the tests will miss its own mistakes. Taking criteria from the session keeps the test plan independent of the implementation. ([13:18](https://youtu.be/YgEv7IQzGdM?t=798))
- **Deterministic checks first, LLM as fallback** — Verification should be deterministic where possible. Where it is not, an agent can drive the app, fill in a form for example, and capture screenshots and database snapshots as evidence for a human reviewer. ([11:50](https://youtu.be/YgEv7IQzGdM?t=710))

## Techniques
- **AI slop registry** — Go through the last ~1,000 review comments, pick the ones that repeat, and encode each as a named rule or check the agent or a review bot runs before a human sees the PR. Add to it each time a new recurring comment appears. *When:* A team reviews many agent-written PRs and keeps leaving the same comments. Use it when review burden is high and the same feedback recurs.
- **Capture session decisions as acceptance criteria** — Keep the agent session as the source of truth. Pull out the clarifying questions and the user's decisions from the conversation and turn them into acceptance criteria, optionally with an LLM's help. *When:* Any agent-built feature where the user made design choices during the session that the original spec or ticket does not record.
- **Test plan from criteria plus registry invariants, run against a preview** — Combine the acceptance criteria with the registry's invariants into a test plan. Spin up a preview of the change and run the plan end to end. Store the results as evidence for review. *When:* Changes that need end-to-end behavior checks, not only unit tests, and where a preview environment is available.
- **Agent-driven UI evidence with DB snapshots** — An agent browses the running app, performs the flow (e.g. a new payment form), and takes screenshots. Pair these with before and after database snapshots, then check the criteria against both. *When:* UI or data-changing features where a reviewer needs more than the diff to trust the behavior.
- **Review the plan and evidence, not the diff** — Reviewers approve the acceptance criteria, test plan and captured evidence, and discuss architecture such as data models and service interactions, rather than reading the code line by line. *When:* Teams that have adopted agent-written code at volume and need review to stay useful.

## Numbers
- Code churn of 861%, stated as the reason review is falling behind (no source given) ([1:03](https://youtu.be/YgEv7IQzGdM?t=63))
- Over 30% of changes are merged with no review at all ([1:03](https://youtu.be/YgEv7IQzGdM?t=63))
- Teams spend about 4x as long waiting for reviews as before ([1:03](https://youtu.be/YgEv7IQzGdM?t=63))
- Code review has been around for about 15 to 20 years; Google formalized it internally in 2006 (the speaker names it as Mondrian) ([2:34](https://youtu.be/YgEv7IQzGdM?t=154))

## Hot takes
- Reviewing agent-written code line by line is the wrong review surface; review intent, criteria and evidence instead.
- Spec-driven development is waterfall with no feedback loop and falls short for day-to-day work.
- The prompts and session are the real record of decisions, and throwing them away after a PR is a mistake.
- If the same agent writes the code and the tests, the tests will not catch its mistakes.
- When AI reviews and nobody reads, the setup is misconfigured.

## Tools mentioned
GitHub, Aviator Verify

## Relevance to our work
- **prosharness** (2/3): ProsHarness has a plan, critique and debate stage. Carrying the user's clarifying decisions from the Claude Code session into acceptance criteria, then checking the finished run against them, would fill a gap the talk describes. → *In the ProsHarness plan stage, persist the user's clarifying Q&A as acceptance criteria and check each checkpoint's result against them before marking it done.*
- **agentos** (1/3): SkillForge mines agent telemetry into governed skills; the registry-of-recurring-review-rules idea is a close cousin of that, but this talk has no measured results. → *Note the registry idea as a possible input source for SkillForge's skill-worthiness scoring, using recurring review comments as the signal.*
