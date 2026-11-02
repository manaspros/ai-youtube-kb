# Anthropic Just Fixed The Token Problem

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `sncxStbRSwI` · [watch](https://youtu.be/sncxStbRSwI) · **date:** 2026-05-02 · **length:** 10:16 · **format:** review · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Unnamed AI LABS host · **orgs:** Anthropic, AI LABS, JetBrains
- **topics:** coding-agents, token-cost-efficiency, multi-agent, claude-code · **tags:** advisor-strategy, executor-advisor, model-routing, sonnet, opus, token-limits, subagents, playwright-mcp, escalation

> AI LABS walks through Anthropic's advisor strategy in Claude Code: a Sonnet executor does all the work and calls Opus only when stuck. Three anecdotal tests show it helps simple-to-medium apps but needs nudging.

## Summary
The video presents Anthropic's advisor strategy as a way to cut token and rate-limit burn. A Sonnet executor runs the agent loop, including tool calls, code edits and user-facing output, while an Opus advisor is consulted only when the executor needs help and never writes code. The creator sets Sonnet as the main model and Opus 4.6 as the advisor inside Claude Code. In a real-time sync bug that Sonnet had failed to fix repeatedly, the executor invoked the advisor, which pinpointed the broken sync logic, and the fix held across devices. A large UI library migration took about 31 minutes, which the creator attributes to Sonnet working sequentially where Opus would parallelize. On a new feature, the executor skipped the advisor until prompted, and the advisor's diagnosis (wrong component choice) fixed the bleed-over and streaming issues. The creator's conclusion is that the pattern suits simple-to-medium apps under tight limits, while complex, dependency-heavy projects are better served by running Opus as the main agent.

## Key ideas
- **Advisor strategy splits roles: a Sonnet executor owns all tool calls, code changes and user output, and an Opus advisor is consulted only when the executor gets stuck.** — The advisor reads the conversation and gives guidance but never writes code or makes changes. The cost pitch is that Opus is invoked only where it matters, not on every iteration. ([0:00](https://youtu.be/sncxStbRSwI?t=0))
- **Creator cites an Anthropic experiment where the executor-plus-advisor combination beat Sonnet alone on SWE-bench at lower cost than running Opus as the main agent.** — The video gives no scores or cost figures for this claim, so treat it as unverified in this talk. ([1:22](https://youtu.be/sncxStbRSwI?t=82))
- **Real-time sync bug test: Sonnet alone failed repeatedly; after the executor invoked the advisor, the advice located the broken sync logic and the fix worked across devices.** — The executor applied the advisor's exact changes without back-and-forth. The creator says Sonnet alone would have needed more prompting rounds, and Opus alone would have burned more tokens. ([2:45](https://youtu.be/sncxStbRSwI?t=165))
- **Large UI library migration took about 31 minutes; the advisor flagged dependency version conflicts that had to be resolved before any UI work.** — Sonnet worked sequentially and checked the UI through Playwright MCP between steps. The creator says Opus would have been faster because it parallelizes independent work, so the strategy is weaker for large multi-part changes. ([5:18](https://youtu.be/sncxStbRSwI?t=318))
- **On a new feature the executor did not consult the advisor at all and treated it as routine work, so the user had to prompt it to use the advisor.** — The executor misjudged task complexity. After the prompt, the advisor identified the wrong component choice as the root cause of both the bleed-over and the missing live streaming. ([6:45](https://youtu.be/sncxStbRSwI?t=405))
- **Ceiling: the strategy suits simple-to-medium apps, while complex apps with many connected dependencies or failure points are better run on Opus directly.** — Even when Sonnet follows advice, it can pick the wrong implementation path because it lacks the depth to weigh approaches, and the back-and-forth can cost more time than starting on Opus. ([9:21](https://youtu.be/sncxStbRSwI?t=561))

## Techniques
- **Executor/advisor model split in Claude Code** — Set the main model to Sonnet and enable the advisor with Opus 4.6 via the advisor command in Claude Code. The video does not show the exact command syntax. The executor handles all tool calls and edits; the advisor only reads the conversation and returns guidance. *When:* Routine implementation work with occasional hard decisions, under tight token or rate limits.
- **Escalate after repeated failure** — When the executor has failed the same bug several times, prompt it to invoke the advisor instead of retrying alone. The advisor reviews the conversation so far and returns exact change instructions. *When:* Stuck debugging, such as sync or state-consistency bugs that persist across attempts.
- **Consult before a high-blast-radius change** — Have the executor inspect the current state first (the creator used the Playwright MCP to view the UI), then consult the advisor on the approach before editing. The advisor caught a dependency version conflict this way. *When:* Major refactors, library swaps or UI redesigns that could break the app if handled wrongly.
- **Name the advisor explicitly for non-trivial tasks** — Do not rely on the executor to judge complexity; in the prompt, tell it to use the advisor for the feature or fix. The creator needed to re-prompt in the new-feature test and says nudging is often required. *When:* New features or multi-file changes where the executor might treat the task as small.
- **Choose the main model by app scope** — Use the Sonnet-plus-advisor setup for simple-to-medium apps. For complex apps with many connected dependencies, or for large changes that can run in parallel, run Opus directly as the main agent. *When:* Deciding up front whether the advisor setup will save time or add back-and-forth.

## Numbers
- Rate limits were lowered, so the 5-hour window fills faster at peak hours (creator's claim, no figures given). ([0:00](https://youtu.be/sncxStbRSwI?t=0))
- Advisor plus Sonnet reportedly outperformed Sonnet alone on SWE-bench, and cost less than running Opus as the main agent (no figures shown). ([1:22](https://youtu.be/sncxStbRSwI?t=82))
- UI library migration with multiple changes in one go took about 31 minutes. ([5:18](https://youtu.be/sncxStbRSwI?t=318))

## Hot takes
- The advisor helps close the gap, but the executor misjudges when to escalate, so the user often has to nudge it to follow the intended workflow.
- The SWE-bench and cost claims are not backed by figures in the video; the evidence is three anecdotal tests on one creator's apps with no controlled comparison.
- The creator says Opus alone would have been faster on the large UI migration, which undercuts the cost-saving pitch for big parallelizable work.
- The video is a sponsored-segment case: a JetBrains Junie sponsor read at about 4:13. Under the quality rules this caps quality at 2 even though the rest of the video carries practitioner tests.
- The title frames this as a fix for the token problem, but the content is a mixed-results walkthrough with an explicit ceiling.

## Tools mentioned
Claude Code, Claude Opus 4.6, Claude Sonnet, Claude Haiku, Playwright MCP, SWE-bench, Junie (JetBrains, sponsor segment)

## Relevance to our work
- **agentos** (2/3): The executor/advisor split is a cheap-model-by-default routing pattern, which fits AgentOS strategy routing in the Govrix Scout proxy. → *Prototype an escalation route in strategy routing: send traffic to a cheap executor model by default, and send only the failing turn to a stronger advisor model that returns guidance and never edits. Benchmark it against the cheap model alone on the same task set.*
- **prosharness** (2/3): ProsHarness wraps Claude Code, and the video shows that the executor does not reliably escalate on its own, so escalation should be a harness rule rather than a prompt habit. → *Add a harness rule that forces a stronger-model advisor turn after N failed attempts at the same bug or step. The advisor call should be diagnosis-only, with no edit tools, and the harness should record the advice in the checkpoint.*
