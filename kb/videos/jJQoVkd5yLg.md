# Why We Deleted Our MCP Server and Rebuilt It — Abhi Arya, Reducto

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `jJQoVkd5yLg` · [watch](https://youtu.be/jJQoVkd5yLg) · **date:** 2026-10-09 · **length:** 16:40 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Abhi Arya · **orgs:** Reducto, Harvey, Scale AI, Circleback
- **topics:** mcp-and-tools, product-ux, observability · **tags:** agent-first-software, mcp-server-design, workflow-shaped-tools, uncertainty-legibility, clarifying-questions, human-in-the-loop, self-improving-loop, session-instrumentation, document-extraction, claude-code

> Reducto deleted its one-tool-per-endpoint MCP server after a team rollout showed agents were confidently wrong; the rebuild uses fewer workflow-shaped tools, legible uncertainty, and session logs that feed back into guidance.

## Summary
Abhi Arya, product at Reducto (an agentic document platform), argues that "agent-first" is an architecture question: who pays when the agent is wrong. His team wrapped every API endpoint as an MCP tool in one file. It looked good in a curated demo but broke when the whole team used it, because agents built full workflows confidently and nobody could see or check what they did. The fix was to delete that file in one commit and replace it with fewer tools that encode the real workflow, plus a snapshot tool that returns live pipeline state and error codes. The team also made uncertainty visible: extraction outputs carry confidence and bounding boxes, the agent is scored down for unstated assumptions, and it is rewarded for asking clarifying questions. Every MCP session and exported Claude Code session is logged, and overrides, low-confidence points and questions feed back into the guidance, so the system improves per org. Adoption came from exposing the tools rather than mandating them, and sales used them before customer calls. The talk gives no benchmark numbers for the rebuild, and it closes with the Reducto hiring plug.

## Key ideas
- **Agent-first is an architecture problem, not a model problem** — Speaker frames three buckets: auto mode (optimise autonomy, the vendor pays when the agent is wrong), user-first (human UI with a weak chatbot bolted on), and agent experience in service of the user (scoped capabilities, human can verify). The useful question is who pays for the agent being wrong. ([1:35](https://youtu.be/jJQoVkd5yLg?t=95))
- **A thin one-tool-per-endpoint MCP wrapper works in a demo and breaks in team use** — The curated Slack demo looked fine. Once the whole team had it, agents built whole pipelines end to end, confidently reported success, and neither user nor agent could explain what the workflow did. There was no point where a human could check it. ([4:16](https://youtu.be/jJQoVkd5yLg?t=256))
- **Replace API wrappers with fewer tools that carry the workflow's structure** — The team deleted the whole MCP file in one commit. New tools encode known paths, for example a single classify-to-extract tool that chains automatically. After each step the agent gets guidance on the valid next step, so the prompt no longer has to carry that logic. ([5:37](https://youtu.be/jJQoVkd5yLg?t=337))
- **Give a stateless agent a snapshot tool that returns live state and specific error codes** — One call returns the state of the whole pipeline and its errors with specific codes. The agent refers to what exists instead of guessing variable names or hallucinating state. Moving context out of the prompt and into structure stopped the guessing. ([8:23](https://youtu.be/jJQoVkd5yLg?t=503))
- **Make uncertainty visible, both in outputs and in the agent's own questions** — Extract outputs confidence scores and bounding boxes, and these are fed back to the model to tune the extraction schema over time. The agent should also surface ambiguity, for example two readings of a field, and ask the user rather than guess or stall. ([9:15](https://youtu.be/jJQoVkd5yLg?t=555))
- **Evals should penalise shaky assumptions and reward asking** — Evals fail the agent for building on unstated assumptions. Prompt guidance points it to the ask-user-question tools that Claude Code and other harnesses provide. The agent also explains what it built and why, so the human can review it. ([10:24](https://youtu.be/jJQoVkd5yLg?t=624))
- **Log every session and mine the logs to improve guidance** — Every MCP session is logged. Staff export their Claude Code sessions. The team looks for human overrides, low model confidence and clarifying questions, and that feeds into the long-term guidance. The speaker describes this as a self-improving loop per org or user, with no hand rewriting. ([13:11](https://youtu.be/jJQoVkd5yLg?t=791))
- **Adoption came from exposing the tools, not mandating them** — Staff were not told to build pipelines with the agent. Once it was offered as enterprise tools, the sales team wired it into pre-call research, and a colleague vouching for a working demo helped it reach high-value customers. ([14:31](https://youtu.be/jJQoVkd5yLg?t=871))
- **The question that matters is who finds out a wrong answer, and how fast** — The speaker's final reframe is that, since models keep getting cheaper and more capable, the differentiator is the harness that surfaces confident errors to a human quickly. Connecting an agent to everything is now easy. ([15:59](https://youtu.be/jJQoVkd5yLg?t=959))

## Techniques
- **Workflow-shaped MCP tools instead of endpoint wrappers** — Delete the one-tool-per-endpoint layer. Build fewer tools that encode the known valid paths and chain steps automatically, with validators and patterns built in. *When:* Agents build multi-step pipelines that a team reuses and that are hard to check when assembled freely.
- **Per-step next-action guidance in tool responses** — Each tool response tells the agent what the valid next step is, so the correct route is also the simplest route. *When:* Stateless agents running a fixed multi-step process where a prompt alone leaves the order to chance.
- **Snapshot / live-state tool with specific error codes** — Expose one read-only call that returns the full pipeline state and every error with a stable code, so the agent refers to real names and states. *When:* A stateless agent must reason over a long, evolving workflow and tends to hallucinate variable names or status.
- **Confidence and provenance in tool outputs fed back to the model** — Return confidence scores and grounding (for example bounding boxes) with extracted values. Use the failure signals to refine the schema or prompt. *When:* Extraction or classification outputs can be wrong quietly across large batches.
- **Evals that score clarifying questions as correct behaviour** — Add eval cases with ambiguous inputs. Fail the agent for building on unstated assumptions, and reward it when it uses the ask-user tool. *When:* Users give half-specified requests, and silent guessing causes downstream failures.
- **Session logging, then mining for override and low-confidence signals** — Log every MCP session and export coding-agent sessions. Mark human overrides, low-confidence moments and clarifying questions, then feed them back into the agent's standing guidance. *When:* You want guidance to improve from real usage across an org without manual rewrites.
- **Require an explanation of what was built and why** — Have the tool output a readable account of each generated artifact so the human can review it before relying on it. *When:* A human is accountable downstream for work an agent generated.

## Numbers
- Reducto has processed over 3 billion documents in the last three years, with customers including Harvey and Scale AI. ([0:12](https://youtu.be/jJQoVkd5yLg?t=12))
- Speaker's rough claim: a frontier model on a clean document gets about 60% of the way, and production (scans, rotation, messy layouts) is the hard part. Not a measured benchmark. ([0:12](https://youtu.be/jJQoVkd5yLg?t=12))

## Hot takes
- Agent-first is an architecture problem, not a model problem.
- Fewer tools that carry workflow structure beat one tool per API endpoint.
- Evals should fail an agent for building on unstated assumptions and reward it for asking.
- The real test of an agent is who finds out when it is confidently wrong, and how fast.
- Connecting an agent to everything is now easy, so the harness and legibility are what differentiate.

## Tools mentioned
Claude Code, MCP, Slack, Notion, Circleback

## Relevance to our work
- **agentos** (2/3): SkillForge's open question is what success signal to use. The talk uses human overrides, low-confidence moments and clarifying questions from logged sessions as the improvement signal, which is a concrete candidate. → *Log overrides, low-confidence events and clarifying-question turns per session, and test them as candidate success signals in SkillForge's skill-worthiness scoring.*
- **prosharness** (2/3): ProsHarness already has plan, critique and approval steps. The talk's ask-instead-of-guess eval and the surfaced-uncertainty pattern fit the plan stage directly. → *Add an ask-user step to the plan stage, and have the Codex plan critique count unstated assumptions as a failure, then check on a few real plans whether it catches them.*
