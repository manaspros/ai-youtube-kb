# Why Software Factories Fail

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Ib5GBkD555M` · [watch](https://youtu.be/Ib5GBkD555M) · **date:** 2026-08-18 · **length:** 19:18 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Dex · **orgs:** HumanLayer, StrongDM, Cloudflare, Cognition, Abundant AI, DataCurve, OpenAI, Pharos AI (as captioned)
- **topics:** software-factory, pr-code-review, evals, context-engineering · **tags:** software-factory, lights-off, harness-engineering, maintainability, rl-rewards, swe-bench, planning, vertical-slices, program-design, pr-review, judge-models

> Dex (HumanLayer) argues that agent "lights-off" software factories fail because coding models are trained on tests passing, not maintainable code, so teams must restore code review and plan up front.

## Summary
The speaker says the prevailing story (spend more tokens, add loops, skip reading code) is breaking down: outages, bloated PR reviews, and rising bugs per developer. He argues this is a model training problem, not only a harness problem, because RL rewards only check that tests pass and cannot penalize poor design. He describes his own team's July 2025 "lights-off" experiment, where agents stalled after roughly three to six months of unreviewed output. His remedy is to put review back and do staged planning (product review, architecture, program design, vertical slices) so reviews are short and every line can still be read. He also reviews newer long-horizon coding benchmarks and says LLM judges can raise the quality floor but are limited by what the model already knows. The talk ends with a pitch for HumanLayer, so treat the closing as promotion.

## Key ideas
- **The harness is not enough; maintainability is a model training gap** — The speaker argues that more loops, more tokens and adversarial review bots cannot fix a problem rooted in how coding models are trained. He says the verification signal does not reward code quality. ([2:52](https://youtu.be/Ib5GBkD555M?t=172))
- **Symptoms of agent-heavy teams** — He cites a vendor report (captioned as Pharos AI) that PR review quality fell, comments grew longer and more numerous, many PRs merged with no review, and incidents and bugs per developer rose. He says this is not just a user-skill problem. ([1:30](https://youtu.be/Ib5GBkD555M?t=90))
- **Agents build fast, but review remains the bottleneck** — Replacing 'someone builds the thing' with an agent cuts build time to minutes or hours. Human review and testing still take hours or days, so adding agentic review helps but does not remove the bottleneck. ([4:07](https://youtu.be/Ib5GBkD555M?t=247))
- **Lights-off factories hit a wall after a few months** — His team tried skipping code reading in July 2025. Agents struggled after roughly three to six months, and the team had to dig through code it had stopped reading to find what was broken. ([8:08](https://youtu.be/Ib5GBkD555M?t=488))
- **RL rewards tests passing, so bad design goes unpunished** — He walks through SWE-bench-style training: a hidden test patch and golden patch decide a binary reward. Nothing penalizes try/catch clutter, needless casts, or poor architecture, and the cost of bad architecture shows up only months later, which makes the reward signal hard to propagate. ([10:50](https://youtu.be/Ib5GBkD555M?t=650))
- **Newer long-horizon benchmarks help, but judges have limits** — He lists SWE-Marathon (about 400-hour tasks), DeepSWE, and Frontier Code (multi-PR tasks, penalizing tests that do not fail on the pre-patch code, plus a judge for quality rules). He says judges raise the floor, but a model that already knew good code would have written it. ([13:39](https://youtu.be/Ib5GBkD555M?t=819))
- **Plan up front so the review is cheap enough to read every line** — Use a staged plan: product review, system architecture (component contracts, data models, constraints), program design (types, signatures, call stacks, call graphs), then vertical slices with checks along the way. Small tasks still go straight to the agent. ([15:02](https://youtu.be/Ib5GBkD555M?t=902))
- **Too many PRs means too many bad PRs** — Thirty minutes of pre-planning and alignment can save hours of review. A good PR should be a joy to review because it matches what was agreed. Even 20% rework is a heavy burden on reviewer and author. ([16:24](https://youtu.be/Ib5GBkD555M?t=984))

## Techniques
- **Staged plan before agent implementation** — Write a product review (problem, desired behavior, mock-ups), then system architecture (component contracts, data models, constraints), then program design (types, method signatures, call stacks; call graphs as a planning aid), then vertical slices with an implementation order and checks between phases. Use AI to gather the information, then have humans align on the plan. *When:* Non-trivial features in large or brownfield codebases, especially cross-repo work. Skip for small changes that can go straight to an agent.
- **Review the plan so the PR review is short** — Align on the design before coding so the PR matches what was agreed. Review the PR against the plan, not from scratch. *When:* When PR volume or review time is growing and the PRs feel like slop to read.
- **Check for test gaming with pre-patch runs and a quality judge** — Penalize tests that also pass on the unpatched code, and use a judge model that checks code-quality rules. He presents this as what newer benchmarks like Frontier Code do, and as a way to raise the floor. *When:* When building agent eval or training signals and you want to catch tests that do not really check the change, or code that passes tests but is poorly designed.
- **Diagnose RL-style reward gaps** — Ask what the reward measures. If it is only binary test pass/fail on hidden tests, expect agents to comment out tests, add defensive clutter, or hack types, and not to care about design. *When:* When judging why an agent or model keeps producing code that passes tests but is hard to maintain.

## Numbers
- Claude Code revenue reportedly grew from about $4B to about $9B in under a year (speaker's recollection, 'I think') ([13:39 area (about 13:00)](https://youtu.be/Ib5GBkD555M?t=0))
- Companies claim agents write about 75% of their code (hearsay the speaker repeats, not verified) ([5:26](https://youtu.be/Ib5GBkD555M?t=326))
- Promised '10 to 100x faster' output with agents is the hype claim he disputes ([0:08](https://youtu.be/Ib5GBkD555M?t=8))
- Agents begin to struggle after about 3 to 6 months of unreviewed or lights-off output; team's own experiment ran from July 2025 ([8:08](https://youtu.be/Ib5GBkD555M?t=488))
- SWE-bench Multilingual tasks take about 15 minutes each, with binary 0/1 reward ([10:50](https://youtu.be/Ib5GBkD555M?t=650))
- SWE-Marathon tasks are about 400 hours long (e.g., clone all of Microsoft Excel) ([13:39](https://youtu.be/Ib5GBkD555M?t=819))
- Even 20% rework per PR is called generous for AI-generated slop; 30 minutes of pre-planning is said to save hours of review ([16:24](https://youtu.be/Ib5GBkD555M?t=984))
- HumanLayer is said to be free for small teams ([17:48](https://youtu.be/Ib5GBkD555M?t=1068))

## Hot takes
- The harness is not enough: the maintainability gap is a model training problem, not a prompt or loop problem.
- Lights-off software factories (never reading the code) fail after a few months on real codebases.
- If you are drowning in PRs, you have too many bad PRs.
- Tests-passing is the only reward most coding-model training uses, so design quality is never trained for.
- LLM judges can raise the quality floor, but they cannot exceed what the model already knows about good code.

## Tools mentioned
Claude Code, Codex, SWE-bench Multilingual, SWE-Marathon, DeepSWE, Frontier Code, Linear, Jira, HumanLayer

## Relevance to our work
- **prosharness** (2/3): ProsHarness already runs plan -> critique -> debate. The talk's staged plan (product review, architecture, program design, vertical slices) suggests more structure in the plan stage and per-slice checks. → *Add a program-design artifact (types, signatures, call graph) and a vertical-slice order with checkpoints to the ProsHarness plan output, and check it before the implementation loop starts.*
- **agentos** (1/3): The talk proposes a maintainability check: penalize tests that also pass on pre-patch code and add a quality-rule judge. This fits AgentOS evals, but the talk gives no measurements. → *Consider a small eval gate for agent PRs: check that new tests fail on the pre-patch code, and run a quality-rule judge on the diff. Measure whether it catches the design issues the talk describes.*
- **general** (1/3): Plan-stage artifacts such as component contracts and program design can serve as explicit context documents for coding agents, which fits the context-engineering interest. → *Treat plan artifacts (product review, component contracts, call graph) as first-class context files for agent runs, and compare outcomes with and without them.*
