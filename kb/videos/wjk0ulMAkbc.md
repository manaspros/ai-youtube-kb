# Taste & Craft: A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @The Pragmatic Engineer

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `wjk0ulMAkbc` · [watch](https://youtu.be/wjk0ulMAkbc) · **date:** 2026-05-18 · **length:** 29:17 · **format:** interview · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Tuomas Artman, Gergely Orosz · **orgs:** Linear, Uber, Lyft, Anthropic, The Pragmatic Engineer
- **topics:** product-ux, testing-verification, coding-agents · **tags:** taste, quality, zero-bug-policy, quality-wednesdays, product-engineer, feature-requests, agent-generated-bug-fixes, hiring, customer-feedback, claude-code, linear

> Linear's CTO and Gergely Orosz on why AI makes taste and quality the scarce advantage. Linear's practices: Quality Wednesdays, a zero-bug policy, and week-long paid work trials.

## Summary
Tuomas Artman (CTO of Linear) talks with Gergely Orosz (The Pragmatic Engineer) about shipping features faster because of AI agents. Artman argues that cheap shipping tempts teams into building software that is confusing and poor in quality, and that quality is the advantage when many competitors can copy features. He describes how Linear turns feature requests into root-cause problems before design and build, and how about 10% of incoming bugs already get an agent-written PR that lands without an engineer. The core quality practices are Quality Wednesdays, where every engineer shows one self-found quality fix each week, and a zero-bug policy with automatic assignment and a seven-day fix target. He says agents lack taste and a sense of time, so humans still have to judge animations and feel. He also covers Linear's hiring (a paid week-long greenfield work trial), its open, recorded customer meetings, and his view that engineers will need to act more like product people.

## Key ideas
- **Easy agent shipping can be a trap** — When features can be built in minutes, teams may ship too much without thinking. Software then becomes confusing. Before AI, slow engineering forced upfront thinking about what to build; that friction is now gone. ([1:08](https://youtu.be/wjk0ulMAkbc?t=68))
- **Quality is the moat when everyone can ship** — If a small team or one person can copy your features with AI, the advantage is tasteful, high-quality software. The speaker compares this to the hyper-growth race at Uber. ([2:27](https://youtu.be/wjk0ulMAkbc?t=147))
- **Turn feature requests into root causes** — Linear rarely ships requests as written. It collects customer feedback, groups requests, finds the root problem, and then designs a solution. AI can summarise and group requests, but humans still need time to decide what is right. ([5:01](https://youtu.be/wjk0ulMAkbc?t=301))
- **Quality decline is gradual and hard to measure** — Metrics such as revenue pushed Uber to ship features fast, and quality was hard to measure, so it slipped. The speaker argues users will gradually move to a better-quality competitor, and no A/B test will show the loss in time. ([7:22](https://youtu.be/wjk0ulMAkbc?t=442))
- **Quality Wednesdays make small fixes a habit** — A weekly meeting where each engineer shows one quality fix they found themselves. Started after an offsite where an hour on one small menu revealed about 35 problems. Engineers then watch for small defects even while building unrelated features, which cuts regressions. ([11:32](https://youtu.be/wjk0ulMAkbc?t=692))
- **Zero-bug policy with fixed-cost reasoning** — The rate of bug creation is roughly constant, so fixing bugs later costs the same as fixing them now. Linear stopped feature work for about three weeks to reach zero bugs. Now each bug is assigned automatically and fixed within seven days, usually in two to three hours. Some very rare bugs can be declined. ([16:46](https://youtu.be/wjk0ulMAkbc?t=1006))
- **Agents lack taste and a sense of time** — Agents work from screenshots or the DOM, so they do not feel delay or animation quality. A design engineer had agents build animations, then improved them by hand, and the human version felt more natural. The speaker expects this gap to close only slowly. ([19:37](https://youtu.be/wjk0ulMAkbc?t=1177))
- **Hiring and customer exposure as quality systems** — Linear uses a paid week-long greenfield work trial for each hire, which has produced few misses. Customer Slack channels are open to all staff, and customer meetings are recorded and tagged for anyone to search. ([22:54](https://youtu.be/wjk0ulMAkbc?t=1374))
- **Engineers will act more like product people** — The speaker expects engineers to talk to customers, understand what a good feature is, and build it. His advice: build something for yourself, ship it, and study Apple's Human Interface Guidelines. ([26:53](https://youtu.be/wjk0ulMAkbc?t=1613))

## Techniques
- **Quality Wednesday** — A 30-minute weekly all-hands. Each engineer shows one quality fix they found themselves, not one assigned to them. Bug fixes do not count. The fixes range from one-pixel changes to backend efficiency work. *When:* A team whose quality is slipping as it ships more. It works best as a standing habit, not a one-off cleanup.
- **Zero-bug policy with agent triage** — Each reported bug is assigned automatically to the person who last worked in the area, using agents. It becomes the top priority. A team can decline very rare bugs. Before the policy starts, stop feature work until the backlog reaches zero, then hold to a short fix window. *When:* When bugs pile up in a backlog and the team can accept a short pause in feature work to clear it.
- **Single-shot agent PRs for incoming bugs** — When a bug arrives, one agent run opens a PR that fixes it. For about 10% of bugs at Linear, this PR lands without an engineer doing anything. *When:* For simple, well-scoped bugs. The speaker expects the share to grow but does not expect it to reach 100% soon.
- **Human-judged feel in agent output** — Let agents produce the first version, such as an animation, then have a designer tune the timing and easing by hand. Compare the two side by side to see what the agent missed. *When:* For UI motion, timing, and other properties that a test cannot check.
- **Paid greenfield work trial** — Hire candidates for a full paid week in which they build a greenfield project or feature from start to finish. Sometimes the work ships. *When:* When you want to see whether someone can own a product from start to finish, beyond what interviews show.
- **Open, tagged customer meeting archive** — Record customer meetings, tag the notable points, and make the archive searchable by everyone so that engineers see customer pain directly. *When:* When the team needs direct exposure to customer problems and not just a PM's summary.

## Numbers
- About 10% of Linear bugs are fixed automatically by a single-shot AI instance that opens a PR and lands it without an engineer ([5:01](https://youtu.be/wjk0ulMAkbc?t=301))
- Uber used five golden metrics, with revenue the one everyone watched ([7:22](https://youtu.be/wjk0ulMAkbc?t=442))
- Quality Wednesdays: about 25 engineers, each showing one fix in a 30-minute call, with each fix taking under two minutes to show ([11:32](https://youtu.be/wjk0ulMAkbc?t=692))
- Hover fade-out is 150 ms, an example of the small details the team checks ([12:48](https://youtu.be/wjk0ulMAkbc?t=768))
- One small view-options menu had about 35 quality problems found in an hour ([14:06](https://youtu.be/wjk0ulMAkbc?t=846))
- About 2,500 to 3,000 small quality details fixed to date (speaker's estimate) ([14:06](https://youtu.be/wjk0ulMAkbc?t=846))
- Zero-bug push took about three weeks of paused feature work; after that, bugs are fixed within 7 days, usually in 2 to 3 hours ([18:13](https://youtu.be/wjk0ulMAkbc?t=1093))

## Hot takes
- Shipping features without much thought is a bad idea, and AI makes this worse
- Every company should have a zero-bug policy
- Quality is hard to measure, so companies drop it until competitors overtake them
- AI agents have no taste and cannot tell whether an interaction feels slow or unnatural
- Everyone will become a product engineer
- Apple's Human Interface Guidelines are the best book for good UX

## Tools mentioned
Claude Code, Opus 4.5, Linear, Apple Human Interface Guidelines

## Relevance to our work
- **agentos** (1/3): The speaker's point that agents lack taste and feel applies to any agent-built UI or CLI surface. The bug and quality-review habits could also help an AgentOS dashboard, but the talk gives no technical method. → *Keep a short weekly list of rough edges in the AgentOS CLI and dashboard, and have one person fix one item each week.*
- **prosharness** (1/3): Agent-written PRs that land without a human for simple bugs are relevant to ProsHarness loops, but the talk gives no method for safe landing or checks. → *Read the Linear bug-to-PR setup and compare it with the ProsHarness plan-critique-debate loop before adding any auto-land step.*
- **general** (1/3): The talk is about quality and taste for agent-written software. It fits the recurring interest in coding-agent workflows but gives no new technique for evals or context. → *Use the Quality Wednesday format as a model for a review step on agent-written code, with a fixed time box.*
