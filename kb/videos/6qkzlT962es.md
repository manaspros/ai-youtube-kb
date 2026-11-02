# Generation Is Cheap, Review Is Expensive: How to Stop Shipping AI Slop — Gabriel Martinez, G2i

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `6qkzlT962es` · [watch](https://youtu.be/6qkzlT962es) · **date:** 2026-10-10 · **length:** 17:18 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Gabriel Martinez (Gabo) · **orgs:** G2i
- **topics:** pr-code-review, context-engineering, software-factory, product-ux · **tags:** AI slop, code review bottleneck, generation vs evaluation, conventions over configuration, Rails, declarative architecture, diagrams as review surface, small PRs, accountability metrics, incentives, ORC, orchestration with judgment

> Gabo (G2i) argues AI slop comes from generation outrunning judgment. His fixes are conventions, small reviewable chunks, visible accountability, and ORC, an orchestration workflow built around review.

## Summary
Gabriel Martinez, an engineering manager at G2i, defines slop as output that looks finished before the thinking behind it is finished. He says the cost of generating code has fallen while the cost of understanding it has not, so teams must still understand the main flows, boundaries, and data model. He traces the pressure to ship faster to stakeholder demos, incentives that reward merge throughput, and AI-inflated documents and PRs that move the ambiguity onto reviewers. His remedies are conventions that leave one obvious way to do things, declarative layers with diagrams as the human review surface, small reviewable chunks, and visible accountability metrics. He ends by introducing ORC, which bakes planning, context management, adversarial checks, and review into the agent workflow. The talk is opinion-driven, with few hard numbers and no ORC internals or results.

## Key ideas
- **Slop is not AI-generated code. It is output that looks finished before the thinking is finished, where ambiguity was settled by guesses and ownership was never taken.** — The real danger is that the engineer never notices a choice existed, so the unknown unknowns stay hidden. Software is a record of choices, and unseen choices cannot be owned. ([0:08](https://youtu.be/6qkzlT962es?t=8))
- **The cost of creating code is falling, but the cost of understanding a program is not.** — Nobody must read every line, but the main flows, boundaries, data model, and product behaviour must be understood. Any line of code is a liability, and an agent does not rescue a messy system. It builds the ball of mud bigger and faster. ([2:17](https://youtu.be/6qkzlT962es?t=137))
- **Incentives drive slop. When merge speed is rewarded, engineers merge code they have not understood or tested.** — He describes performance anxiety from watching peers merge quickly. Rewards should centre on well-factored design, clear test and eval harnesses, and value produced, not PR count or token burn. ([7:31](https://youtu.be/6qkzlT962es?t=451))
- **Generation is cheap, evaluation is expensive. Output that exceeds what humans can review is a bottleneck, not a speed-up.** — A vague brief turns into a huge PR, or a 10-bullet scope turns into a 20-page document. The ambiguity the author should have resolved moves to the reviewer. ([9:00](https://youtu.be/6qkzlT962es?t=540))
- **Use a compressed review surface. Diagrams of service boundaries, data flows, state transitions, and failure modes let humans review the main workflow, with details pushed to the leaves.** — He favours declarative code and architecture patterns that create layers humans can reason about, so reviewers can check intent rather than reverse-engineer thousands of generated lines. ([11:55](https://youtu.be/6qkzlT962es?t=715))
- **Conventions cut cognitive overhead for humans and agents. A single canonical way to do each thing is better for agentic development than many competing styles.** — He uses Rails as the example, where convention over configuration removes repeated decisions. Agents are confused by dozens of approaches, and the reviewer has to infer intent from every new style. ([13:19](https://youtu.be/6qkzlT962es?t=799))
- **ORC packages the human discipline of planning, context management, option weighing, adversarial checks, and review into an agent workflow, with the human still responsible.** — He says ORC is not a box that removes correctness as a human duty. It is a system to preserve that duty while agents do more of the work, and the goal is code that stays coherent, tested, maintainable, and owned. ([14:44](https://youtu.be/6qkzlT962es?t=884))

## Techniques
- **Single canonical pattern per concept** — Document one blessed way to structure each concept (routing, data access, module shape) in conventions files so agents do not choose among competing styles. Pick a framework or house style that minimises decision surface. *When:* Before letting agents generate code in a mature or multi-contributor codebase where reviewers must infer intent.
- **Diagram-first review surface** — Have the agent or engineer produce diagrams of service boundaries, data flows, state transitions and failure modes for each change. Reviewers approve the main flow and inspect implementation only at the leaves. *When:* When generated changes are too large to read line by line, and reviewers need to see the shape of the change first.
- **Small reviewable chunks with explicit ownership** — Break a feature into pieces small enough to hold in one head. Define done for each chunk and attach a visible accountability metric to each unit of work product. *When:* When agents produce multi-thousand-line PRs or long documents that nobody can fully review.
- **Built-in adversarial and planning gates before merge** — Route agent output through planning, context curation, option weighing and adversarial checks before code enters the main branch, as ORC does. The human keeps the merge decision. *When:* When you run autonomous or background coding agents that could push code faster than the team can judge it.

## Numbers
- A prototype with a clickable UI can be vibe-coded in about an hour, which shifts stakeholder expectations of how fast software can be built. ([5:09](https://youtu.be/6qkzlT962es?t=309))
- SQLite's maintainer says a PR is not free: it means maintaining, documenting and testing the code for the next 25 years (quoted by the speaker). ([6:03](https://youtu.be/6qkzlT962es?t=363))
- A 10-bullet scope request came back as a 20-page document, and a single screen had 12 escape hatches. ([9:00](https://youtu.be/6qkzlT962es?t=540))
- A multi-thousand-line PR cannot be fully understood by one human reviewer (speaker's assertion, no measurement). ([7:31](https://youtu.be/6qkzlT962es?t=451))
- The speaker had a four-year gap between two stints using Rails, and the patterns were unchanged when he returned. ([13:19](https://youtu.be/6qkzlT962es?t=799))

## Hot takes
- Slop is not about AI as a tool. It is about the absence of judgment.
- The Ralph loop is just a while loop, dressed up as an agentic breakthrough.
- Lines of code are a garbage productivity metric, and so are tokens burned.
- Environments with one correct way of doing things are better for agentic development than ecosystems with many competing approaches.
- The best code is no code at all.

## Tools mentioned
ORC (G2i's orchestration system, described only at a high level), Ruby on Rails (convention-over-configuration example), SQLite (quoted maintainer comment on PR maintenance cost)

## Relevance to our work
- **prosharness** (2/3): ProsHarness already runs plan, critique and debate steps. The talk's review-surface, small-chunk and definition-of-done ideas map onto its checkpoint and approval loop. → *Add a size cap per generated change and a human-readable main-flow summary to the ProsHarness approval step, then measure how many approvals are rubber-stamped.*
- **general** (2/3): Relevant to the recurring interests in context engineering and coding-agent workflows. It frames convention files as a way to reduce agent confusion. → *Audit the CLAUDE.md or AGENTS.md conventions in the active repos to ensure there is one canonical pattern per concept, and note which concepts still have two competing styles.*
