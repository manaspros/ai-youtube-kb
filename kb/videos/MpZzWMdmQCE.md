# Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `MpZzWMdmQCE` · [watch](https://youtu.be/MpZzWMdmQCE) · **date:** 2026-07-18 · **length:** 10:08 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Talha Sheikh · **orgs:** Checkout.com, Anthropic, OpenAI, Kudo (likely Qodo, auto-caption), WorkOS, Facebook
- **topics:** testing-verification, claude-code, coding-agents, agent-architecture · **tags:** verification, stop-hook, deterministic-checks, retry-loop, claude-code, harness-engineering, guardrails, llm-as-judge, trust, cost-reduction, executor-advisor

> Talha Sheikh (Checkout.com) argues coding agents need deterministic, shareable verification hooks, not better instructions, and that the real engineering work is designing the verification harness.

## Summary
The speaker describes repeatedly catching Claude Code runs that reported "task completed" while the output still failed, so he was acting as the enforcement layer. He built VectorV1 (also called Vector Harness), a tool that uses a Claude Code Stop hook to run a config-defined set of tests when a session ends, and feeds failures back to the agent with a retry instruction until everything passes. He frames the goal as trust: whether the agent actually did what was wanted, not whether it is capable of doing the task. He argues that more capable models and better specs, MCP servers or subagents do not replace verification. Guardrails could let cheaper models like Haiku or open-source models reach the needed output, shifting cost from the frontier model to the harness. Because every team builds bespoke enforcement, he proposes a language-agnostic contract: a task goes in, developer-defined checks run at several levels (in-conversation, before commit, between agents, async jobs, and optionally LLM-as-judge). He notes that Anthropic (executor-advisor pattern), OpenAI (harness engineering), PR review vendors and WorkOS are converging on the same idea. His conclusion is that verification design, not code output, is now where the value lies, so one should work on the harness rather than the code.

## Key ideas
- **Agents say 'done' but the output often fails when run; the human ends up as the enforcer.** — Multi-agent Claude Code runs show all sub-tasks completed, yet a small thing is still missing. The speaker had to keep prompting fixes, so he was the one checking the output. ([0:00](https://youtu.be/MpZzWMdmQCE?t=0))
- **Run deterministic checks automatically when the agent session ends, using a Claude Code hook.** — VectorV1 is driven by a config file listing the tests to check. A Stop hook calls it at session end. Failing tests are reported back to the agent, which is told to try again until all pass. ([1:58](https://youtu.be/MpZzWMdmQCE?t=118))
- **The problem is trust, not capability.** — The question is whether you can trust the agent to finish the task the way you want, not whether it can do the task at all. Instructions and specs are not the same as verification. ([1:58](https://youtu.be/MpZzWMdmQCE?t=118))
- **Better models and richer context do not remove the need for verification.** — Capability gains do not automatically mean reliability gains. Specs, MCP servers, subagents and context all help, but none of them checks the result. ([3:29](https://youtu.be/MpZzWMdmQCE?t=209))
- **Strong guardrails can make cheaper models viable, moving cost from the model to the harness.** — With good checks, a smaller model such as Haiku or an open-source model may reach the target output. Investing in the harness rather than always using a frontier model could cut cost sharply. This is argued, not measured. ([4:32](https://youtu.be/MpZzWMdmQCE?t=272))
- **Bespoke enforcement cannot be shared, so the pattern needs to be a language-agnostic contract.** — Each team enforces different rules, so private tools do not transfer. The proposed contract is: given a task, developers define the checks in the middle. Checks should run at conversation end, before commit, between agents in a workflow, on async agents, and optionally as non-deterministic LLM-as-judge. ([5:51](https://youtu.be/MpZzWMdmQCE?t=351))
- **The same convergence is visible across vendors: verification loops, not better instructions.** — He points to Anthropic's executor-advisor pattern, OpenAI's harness engineering, PR review vendors that run comprehensive reviews, and WorkOS's 'enforce, don't instruct' idea. ([7:13](https://youtu.be/MpZzWMdmQCE?t=433))
- **The bottleneck is verification, so slowing down is the right call.** — Agents can produce code faster than teams can verify it. The value has moved from the code itself to the verification system that a team designs. His summary: 'work on the harness and not on the code'. ([7:13](https://youtu.be/MpZzWMdmQCE?t=433))

## Techniques
- **Stop-hook deterministic verifier** — Register a Claude Code Stop hook that runs a checker script on session end. The checker reads a config listing the tests or checks for this task and returns pass/fail per check. *When:* Any agent task with a clear, checkable definition of done, especially when the agent's own 'done' claim is not trusted.
- **Fail-and-retry feedback loop** — When a check fails, send the specific failure output back to the agent and tell it to try again. Repeat until all checks pass. The speaker's example shows first test failing, retry, then all passing. *When:* Fix-verify cycles where the agent can self-correct from concrete test output.
- **Layered enforcement at multiple points** — Place checks at several levels: inside the conversation, before commit, at handoffs between agents in a multi-agent workflow, and on async agent results. Add an optional non-deterministic LLM-as-judge layer on top of the deterministic ones. *When:* Multi-agent or background-agent systems where one unchecked step can propagate errors downstream.
- **Language-agnostic check contract** — Define a shared contract: input is a task, output is pass/fail with evidence. The contents of the checks are supplied by each team, and any runner that can execute them deterministically can implement the contract. *When:* Several teams or repos need the same enforcement pattern without sharing one codebase.
- **Executor plus advisor loop** — One agent does the work. A separate advisor agent reviews the output and feeds comments back in a loop. The speaker cites Anthropic's executor-advisor pattern as an example. *When:* When a second opinion from a different agent is cheaper or more reliable than a single agent verifying itself.
- **Cheap model plus strong harness** — Use a smaller or open model for the work, and rely on deterministic guardrails and retries to reach the required output. Put effort into the harness rather than the model. *When:* Cost-sensitive pipelines where each task has a checkable output.

## Numbers
- No benchmark, latency, cost, or adoption figures are given. The cost reduction from cheaper models with guardrails is argued qualitatively only. ([4:32](https://youtu.be/MpZzWMdmQCE?t=272))
- Retry example: a test first fails, the agent is told to retry, then all tests pass. ([1:58](https://youtu.be/MpZzWMdmQCE?t=118))
- Talk runs 10:08 long, with about 40 seconds of Q&A time mentioned. ([8:29](https://youtu.be/MpZzWMdmQCE?t=509))

## Hot takes
- Better models do not equal more reliable models, and instructions are not verification.
- Be the one who designs the verification system; the value has moved from writing code to verifying it.
- If a stronger model means fewer checks, the frontier model becomes the most expensive choice; invest in the harness and use cheaper models.
- Developers should slow down, because verification is the real bottleneck, not code generation.
- The speaker's own tool may be obsolete if agent makers ship built-in verification, but the verification pattern still holds.

## Tools mentioned
Claude Code, Claude Code hooks (Stop hook), VectorV1 / Vector Harness, Haiku, Opus, Anthropic Glasswing / Project Mythos (named, not described)

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code and already has checkpoint/resume and plan->critique loops. A deterministic Stop-hook check with a retry loop fits the same harness and could gate when a checkpoint counts as done. → *Prototype a config-driven, deterministic check run from a Claude Code Stop hook in ProsHarness. Feed failures back into the same session until pass, then mark the checkpoint complete.*
- **agentos** (1/3): The talk's layered-check contract is related to exec-gate guardrails in Crucible and the post-run check idea in SkillForge, but the talk has no implementation detail for those components. → *Compare the layered check contract with Crucible's exec-gate design and decide whether post-run deterministic checks belong there.*
- **general** (1/3): Applies to any Claude Code workflow: a checkable definition of done plus a Stop hook is a small, portable pattern. The speaker's tool itself is a pitch, and his own examples are thin. → *Add a Stop hook to one Claude Code repo that runs a test suite and blocks the session from ending until it passes. Measure how often it catches a false 'done'.*
