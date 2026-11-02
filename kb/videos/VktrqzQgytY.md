# CI/CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `VktrqzQgytY` · [watch](https://youtu.be/VktrqzQgytY) · **date:** 2026-05-18 · **length:** 18:37 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Madison Faulkner, Hugo Santos · **orgs:** NEA, Namespace, GitHub, Fal, Zed, Ramp, HashiCorp, Google, Meta
- **topics:** software-factory, pr-code-review, sandboxing-execution, multi-agent · **tags:** CI/CD, continuous compute, merge queue, serializability, spec-driven development, agent harness, external validation, stateful environments, GitHub Actions, pre-merge

> Talk arguing CI/CD was built for human-paced PRs and breaks under agent volume; proposes spec-driven agent loops with in-loop validation, a pre-merge queue, and stateful compute.

## Summary
The speakers argue that CI/CD assumes a few human PRs per week, and that agent-scale output (many short-lived branches across many repos) makes merging and validation the bottleneck. They say human latency used to hide slow builds, but once code generation gets cheap, validation has to move inside the agent's loop. Their proposed architecture drops PRs as the unit of work: a spec states intent, an agent harness works from a known commit, runs build and tests internally, and gets feedback from other review agents (security, API conformance). Parallel changes go into a pre-merge queue that reconciles them for serializable commits, and humans approve intent plus evidence rather than diffs. They also expect agents to explore several candidate commits at once and to keep environments stateful to avoid cold starts. The talk is a vision pitch from a speaker at Namespace, so most claims are unquantified and the only hard number is a 4x increase in PR volume on their own team.

## Key ideas
- **CI/CD was built for human pace; agent volume breaks it** — Humans submit one or two diffs a week and wait on review. Agents create many PRs across many repos, and thousands of short-lived branches pull the same codebase in different directions, so merging them becomes nearly impossible. ([2:33](https://youtu.be/VktrqzQgytY?t=153))
- **Human latency used to hide slow machines** — Validation and merges were slow, but the delay was swallowed by the time humans took to write and review code. Cheap generation removes that cover, so validation has to run continuously inside the loop. ([6:30](https://youtu.be/VktrqzQgytY?t=390))
- **Merging behaves like a database commit problem** — Every change must go into a single ledger under a lock. With humans the lock is held a long time; with machines it is short, but the volume of changes makes serialization the core issue. ([8:42](https://youtu.be/VktrqzQgytY?t=522))
- **Replace PRs with intent plus a spec-driven agent loop** — A spec records the goal (in a ticket, Slack, etc.). A harness such as Claude Code, Amp, Cursor or Factory checks out a known commit, builds and tests internally, and iterates until the plan is met. The PR is no longer the unit of work. ([10:02](https://youtu.be/VktrqzQgytY?t=602))
- **Validation splits into internal and external** — Internal validation (build and test) must be fast, because a 15 to 45 minute test run stalls the whole loop. External validation is done by other LLM agents, such as a security reviewer or an API conformance checker, whose feedback feeds back into the main harness. ([12:22](https://youtu.be/VktrqzQgytY?t=742))
- **Pre-merge queue with human approval on intent and results** — Finished changes wait in a pre-merge queue that reconciles parallel work into a serializable order. Humans approve the intent and its evidence (a demo video, a security report), and possibly across several commits or agents grouped together, rather than reading the code. ([13:48](https://youtu.be/VktrqzQgytY?t=828))
- **Explore multiple candidate commits in parallel** — Agents may plan from different points in history instead of the current tip, because the tip keeps moving. This multiplies compute use, so the inner loop has to be very fast. ([15:09](https://youtu.be/VktrqzQgytY?t=909))
- **Keep state and avoid cold starts; invariants become continuous** — Memory and environment state make the loop fast, so agents should not start from scratch. Checkout invariants (a known commit, no unvetted code) still matter for compliance but are enforced on every iteration. Coordination and governance move into the harness. ([16:06](https://youtu.be/VktrqzQgytY?t=966))

## Techniques
- **Spec-first agent loop with a known-commit start** — Write intent down as a spec, then have the agent harness check out a well-known commit, implement the plan, and run build and tests before reporting back. *When:* When agents generate many changes and each change must start from a verified base.
- **External review agents inside the loop** — Run specialised LLM reviewers (security, API conformance) on each candidate change, and feed their findings back to the main agent before any human sees the result. *When:* When human review cannot keep up with agent-written PR volume.
- **Pre-merge queue for serializable commits** — Hold finished changes in a queue that reconciles parallel edits to the same code and commits them in a single back-to-back order, grouping related changes semantically. *When:* When many agents change the same repository in parallel and merge conflicts become frequent.
- **Approve intent and evidence, not diffs** — Give the human reviewer the original intent plus the outputs (demo video, security scan result) that cover one or more commits, and let them approve that bundle. *When:* When reviewing code line by line no longer scales.
- **Stateful, incremental execution environments** — Keep warm environments and cached state, reuse previous work, and avoid rebuilding from scratch on each agent iteration. Their routing layer also adds ingress shaping, rate limiting, retries and agent identity. *When:* When validation latency is the bottleneck inside the agent loop.

## Numbers
- Team PR volume is about 4x what it was before agents (the speaker calls these PRs, which is ambiguous) ([15:09](https://youtu.be/VktrqzQgytY?t=909))
- A human developer submits about one or two diffs a week (the baseline the speaker uses) ([2:33](https://youtu.be/VktrqzQgytY?t=153))
- Example of too-slow internal validation: test runs of 15 or 45 minutes, given as illustrative figures ([12:22](https://youtu.be/VktrqzQgytY?t=742))
- A GitHub commit and line-change chart shows a sharp spike, but the speaker gives no numbers ([3:46](https://youtu.be/VktrqzQgytY?t=226))

## Hot takes
- CI/CD is dead for agent-scale software.
- The PR is the wrong unit of work once agents are doing most of the coding.
- Humans should approve intent and evidence, not code.
- Merging at agent scale is a high-performance database serialization problem.
- Stateful compute is the next infrastructure category, more than CI/CD.

## Tools mentioned
GitHub Actions, Claude Code, Amp, Cursor, Factory, GitHub Copilot, Namespace

## Relevance to our work
- **prosharness** (2/3): The talk's inner loop (spec, harness, internal and external validation, stateful resume) closely matches ProsHarness's checkpointed Claude Code harness with critique passes. → *Add an external-reviewer stage (security or API conformance agent) that runs on each checkpoint before a phone approval, and show intent plus evidence in the approval rather than the raw diff.*
- **agentos** (1/3): Crucible's sandboxed code execution would benefit from warm, stateful environments if validation runs repeatedly, but the talk gives no benchmarks. → *In Crucible, measure cold-start versus warm-sandbox latency for repeated test runs before deciding whether to keep sandboxes warm.*
