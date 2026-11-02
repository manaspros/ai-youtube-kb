# How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `5Bn0xro2ol8` · [watch](https://youtu.be/5Bn0xro2ol8) · **date:** 2026-09-18 · **length:** 17:43 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Eyal Blum · **orgs:** Figma
- **topics:** enterprise-adoption, testing-verification, coding-agents, context-engineering · **tags:** adoption, verification, testing pyramid, tdd, planning, phased plans, subagents, pr descriptions, attention, slack, playwright mcp, culture, figma

> Figma engineer on rolling out coding agents across an org: verification-first testing, plan-before-prompt with phase validation gates, and labeling AI-written text so reviewer attention is spent well.

## Summary
Eyal Blum (Figma) describes how Figma's engineering org is adopting coding agents without lowering code quality. He frames adoption as three acts (quick wins, failure on bigger problems, then building real skill) and says teams are at uneven stages. He names side effects: engineers losing craft satisfaction, the most senior engineer becoming a bottleneck, and documents and messages growing much longer. His main lesson is to move verification from humans to deterministic checks and agents, so that humans review only functionality. He also recommends writing detailed plans with a why section and independently verifiable phases before handing work to agents, and he marks AI-written text explicitly in PRs and messages. Adoption tactics include letting skeptics own the AI-safety roadmap and letting people tag an agent in a Slack thread. The talk is anecdotal and self-described as unfinished, with a single 5x speedup example.

## Key ideas
- **Three-act adoption curve** — Teams first get quick wins on simple tasks, then trust breaks when they apply the same habits to bigger problems, and only then do they build real skill (guardrails, prompting, context). Adoption is uneven across teams and they must work together. ([0:12](https://youtu.be/5Bn0xro2ol8?t=12))
- **Hidden costs of adoption** — Engineers lose craft satisfaction when reduced to prompt-and-wait cycles. The best engineer, who holds the pitfalls in their head, becomes the bottleneck and is slowest to adapt. Docs and messages became 3-4x longer and email volume 2-3x. ([4:07](https://youtu.be/5Bn0xro2ol8?t=247))
- **Invest in verification above all else** — The highest-value work is moving any step that a human does today into something the agent can verify itself. Example: Playwright MCP let the agent explore the running app instead of humans clicking through it. ([5:26](https://youtu.be/5Bn0xro2ol8?t=326))
- **Encode what works into deterministic flows** — When an agent discovers a useful procedure, turn it into a deterministic, repeatable flow or test. This saves tokens and time and keeps LLM reasoning for steps that really need it. ([5:26](https://youtu.be/5Bn0xro2ol8?t=326))
- **Testing pyramid with agents on top of deterministic checks** — Push as much as possible down to linters, compilers and unit tests. Encode architecture standards so agent review applies them. Only the top layer, functional behavior, needs a human. ([6:47](https://youtu.be/5Bn0xro2ol8?t=407))
- **Red-green TDD prompting** — Asking the agent to write code test-first gives better results than writing tests afterwards, because tests written after tend to fit the code rather than check the requirement. ([7:20](https://youtu.be/5Bn0xro2ol8?t=440))
- **Planning over prompting, with phased validation gates** — Spend days on a detailed plan, get it reviewed, then hand it to an agent. Start the plan with the why as an executive summary to prevent drift. Split it into parts that can each be verified on their own with an explicit gate, so no stage is built on unchecked assumptions. ([8:07](https://youtu.be/5Bn0xro2ol8?t=487))
- **Right-size phases by review effort** — A phase is the right size when its PR can be reviewed in one sitting. If it would take a coffee break to read, split it. Each phase should carry enough detail that a subagent can run it independently. ([9:05](https://youtu.be/5Bn0xro2ol8?t=545))
- **Mark AI-written versus human-written text** — Each PR and message starts with a short human-written summary, followed by AI-generated text that the reader should scan with more suspicion. This signals how much attention each part deserves. A senior skeptic was upset by unlabeled AI output, which taught the speaker to state intent and say what is AI. ([12:58](https://youtu.be/5Bn0xro2ol8?t=778))
- **Skeptics own the AI-safety roadmap, and agents join the thread** — The engineers most burdened by failures know where verification is missing, so put them in charge of the improvement roadmap. Let people tag an agent in a Slack thread to close a loop, which lowers the bar for trying it. ([11:30](https://youtu.be/5Bn0xro2ol8?t=690))

## Techniques
- **Verification-first agent workflows** — Give the agent tools that let it check its own work, such as a browser MCP to explore the running app. Convert each human check into an automated or agent-run check. *When:* Any codebase where humans currently verify behavior by hand, before scaling agent use.
- **Encode agent discoveries as deterministic tests or flows** — After an agent finds a working procedure, write it as a fixed test or script so later runs need no LLM reasoning for that step. *When:* A known, repeatable procedure has been reached by trial and error with an agent.
- **Testing pyramid for agent-written code** — Base layer: linters, compiler, unit tests. Middle: agent review against encoded architecture standards. Top: human review of functionality only. *When:* Reviewing agent-written PRs at volume, so human attention goes to behavior.
- **Red-green prompting** — Instruct the agent to write the failing test first, then the code to pass it, rather than writing tests after the implementation. *When:* Agent-written features where tests must check the requirement, not the code.
- **Why-first phased plan with validation gates** — Put a short executive summary of the why at the top. Break the work into phases, each with its own verification criteria and detail sufficient for a subagent. Review and approve the plan before any implementation. *When:* Long or multi-PR changes where drift between stages is a risk.
- **Human-first labeled communication** — Start each PR description or message with a short handwritten summary, then mark the AI-generated part and tell readers what to skim or override. *When:* Team norms for PRs, Slack and email when AI drafts most of the text.
- **Agent-in-thread invitation** — Tag an agent in an existing Slack thread to complete a task for a colleague who is not yet using AI, so they see the result without needing to adopt a new tool. *When:* Low-pressure adoption with colleagues who are skeptical.

## Numbers
- Docs, Slack messages and emails became 3-4x longer, and there are 2-3x as many emails, with the same effective output ([4:07](https://youtu.be/5Bn0xro2ol8?t=247))
- Plan for one large change took about a week to write, plus about a week of alignment with three other teams, then an overnight agent run produced about six weeks of coding work in one week (speaker's claimed 5x speedup) ([10:31](https://youtu.be/5Bn0xro2ol8?t=631))
- The resulting plan was about 20 PRs, most roughly 10 to 100 lines ([10:31](https://youtu.be/5Bn0xro2ol8?t=631))
- A brainstorm with a group of engineers to build the AI-safety roadmap took under an hour ([11:30](https://youtu.be/5Bn0xro2ol8?t=690))
- Speaker has worked in the Valley for about 15 years, and calls this the biggest culture and technology change of that time ([16:32](https://youtu.be/5Bn0xro2ol8?t=992))

## Hot takes
- Investing in verification is probably the highest-value work a codebase can get, for agent adoption.
- Tests written after the code tend to fit the code rather than check the requirement, so write them first.
- The most burdened senior engineers should set the AI-safety roadmap rather than be asked to adopt AI.
- Human review should be left to functionality, with linting, compiler, unit tests and agent review covering everything below.

## Tools mentioned
Playwright MCP, Slack, cloud coding agent (unnamed)

## Relevance to our work
- **prosharness** (2/3): Plan-first phases with validation gates and subagent-sized steps map onto ProsHarness' plan -> critique -> debate loop and its checkpoint/resume runs. → *Add a plan lint step before critique in ProsHarness: require a why summary at the top, a verification gate per phase, and split any phase too big to review in one sitting.*
- **general** (1/3): Useful as adoption and verification guidance for any agent-driven team, though it is anecdotal and mostly qualitative. → *Read the talk's testing-pyramid and red-green prompting points before deciding how to structure agent review gates in the agent-registry work.*
