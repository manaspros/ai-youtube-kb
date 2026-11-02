# The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `li0SaBt9RDM` · [watch](https://youtu.be/li0SaBt9RDM) · **date:** 2026-06-18 · **length:** 17:05 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Priscila Andre de Oliveira · **orgs:** Sentry
- **topics:** claude-code, skills-self-improvement, coding-agents · **tags:** comprehension, codebase-onboarding, claude-code, session-analysis, skills, pr-review, sentry, agent-manager, sponsored

> Sentry engineer Priscila Andre de Oliveira on using AI mainly for codebase comprehension: she mined her own sessions, found 67% were comprehension and 2% generation, and built a reusable "Catch Me Up" skill.

## Summary
Priscila Andre de Oliveira, a senior engineer at Sentry, says she has only prompted, not coded, since December 2025. She describes Sentry's internal AI tools (Abacus, Warden, Junior) and a three-month "quality quarter" spent removing any types, TODOs and dead feature flags before AI work. Her main point is that in a large, fast-moving codebase the bottleneck is comprehension, not generation. She had Claude classify 116 of her sessions into six categories and found 67% were comprehension and 2% code generation. She turned her repeated comprehension prompts into a local "Catch Me Up" skill with six exploration modes, and used it to onboard onto an unfamiliar repo and to prepare for PR reviews. She proposes adding a research/comprehension stage before the usual plan and implement steps. The talk was sponsored by Sentry, which offered a trial at the end.

## Key ideas
- **Comprehension, not generation, is the biggest unlock for AI in a large codebase.** — She argues that in a big, moving codebase the scarce skill is understanding what exists, and that generating code is the smaller part of the work. She says she only prompts now and does not write code herself. ([14:15](https://youtu.be/li0SaBt9RDM?t=855))
- **Measure your own AI usage before optimising it.** — She had Claude analyse 116 of her sessions and sort them into six categories. The result, 67% comprehension and 2% generation, surprised her and changed how she thinks about her usage. ([9:46](https://youtu.be/li0SaBt9RDM?t=586))
- **Turn repeated prompts into a local skill.** — Her comprehension questions kept repeating, so she packaged them as a markdown skill, Catch Me Up, that is just a detailed prompt with clear goals. It runs on her machine and she could share it later. ([10:47](https://youtu.be/li0SaBt9RDM?t=647))
- **Structure comprehension questions into named exploration modes.** — The skill covers architecture, convention, feature trace, syntax, testing and history. She asks for visual output such as an org-chart-like structure and tables, because she is a visual person. ([10:47](https://youtu.be/li0SaBt9RDM?t=647))
- **Use AI for history and rationale, not only for code reading.** — During incidents she used to run git blame and search PRs by hand, and to wait a day for a colleague in another timezone to explain a product decision. Now a single prompt returns the regression point or the reasoning in seconds. ([8:30](https://youtu.be/li0SaBt9RDM?t=510))
- **Add a comprehension step between research and planning.** — She agrees with the research, plan, implement sequence but says the research step is missing a comprehension check. You need to understand what the agent found so you can steer it when it goes the wrong way. ([14:15](https://youtu.be/li0SaBt9RDM?t=855))
- **Reserve time to clean up the codebase so agents stay steerable.** — Sentry ran a three-month quality quarter that removed any types, stale TODOs and unused feature flags. She presents this as technical depth that makes the codebase easier for people and agents to understand. ([4:59](https://youtu.be/li0SaBt9RDM?t=299))

## Techniques
- **Session-log classification audit** — Have the model read your past agent sessions and sort them into intent categories such as comprehension, modification, process, review, generation and ordering. Count the shares to see where your AI time actually goes. *When:* When you suspect your AI use is mostly something other than what you think, or before deciding which skills to build.
- **Repeated prompt to personal skill** — When the same kind of prompt keeps coming back, write it into a markdown skill file with explicit goals and a fixed set of modes. Keep it local at first and share later if it works. *When:* When you notice you retype the same instruction across many sessions.
- **Onboarding via a 'new contributor' framing** — Start the session by saying you are a new contributor. Ask a specific question, such as whether a test layer intercepts or simulates a payload, and ask for a flow summary alongside the answer. *When:* When you enter an unfamiliar repository or need to check how a subsystem behaves before changing it.
- **Comprehension pass before PR review** — Before approving a colleague's PR, run the comprehension skill on the affected area to rebuild context. Do not approve on code you do not understand. *When:* When you have enough context to comment but not enough to approve a change.
- **Research, then comprehension check, then plan, then implement** — Add an explicit step after the agent's research where you check its understanding and redirect it if needed, before asking for a plan and then implementation. *When:* On large, complex codebases where the agent can misread the existing code and build on the wrong picture.
- **Codebase hygiene sprint for agent legibility** — Set aside a fixed period to remove any types, stale TODOs and dead feature flags, and to simplify code, so the codebase is easier to read for both humans and agents. *When:* When the codebase is large, changes daily and has accumulated cruft that makes it harder to reason about.

## Numbers
- 116 sessions analysed by Claude and sorted into six categories ([9:46](https://youtu.be/li0SaBt9RDM?t=586))
- 67% of her AI usage was comprehension ([9:46](https://youtu.be/li0SaBt9RDM?t=586))
- 2% of her AI usage was code generation ([9:46](https://youtu.be/li0SaBt9RDM?t=586))
- Cited study figure: about 70% of developer time goes on reading and navigating code (attributed by the speaker to existing studies, not verified here) ([7:28](https://youtu.be/li0SaBt9RDM?t=448))
- About 100 PRs merged per day into the Sentry codebase ([6:18](https://youtu.be/li0SaBt9RDM?t=378))
- Sentry has about 400 employees, 100K organisations on the platform, and 15+ years of code (founded 2010) ([2:51](https://youtu.be/li0SaBt9RDM?t=171))
- Quality quarter lasted three months ([4:59](https://youtu.be/li0SaBt9RDM?t=299))
- Sponsor offer: three months free trial of the business plan via QR code ([15:36](https://youtu.be/li0SaBt9RDM?t=936))

## Hot takes
- She has not written code since December 2025 and only prompts.
- 67% of AI usage should be comprehension and 2% generation, which she sees as the real value of AI in a large codebase.
- Do not ship code you do not understand, even when the project is vibe-coded.
- The industry research, plan, implement loop is missing a comprehension step.
- AI is the cheapest senior engineer you have, so ask the dumb questions.

## Tools mentioned
Claude Code, Claude Opus, Catch Me Up (personal skill), Warden (Sentry code review agent), Junior (Sentry Slack bot that turns threads into PRs), Abacus (Sentry internal AI usage tracker)

## Relevance to our work
- **prosharness** (2/3): Her research, comprehension check, plan, implement sequence maps directly onto ProsHarness's plan to critique to debate flow, and she offers a concrete extra gate before planning. → *Add a comprehension checkpoint between the research output and the plan step in ProsHarness, where the harness asks the agent to restate the relevant code and flags misreadings before planning, then measure whether this reduces critique rounds.*
- **agentos** (1/3): Mining her own session logs into intent categories parallels SkillForge's open question about mining telemetry into skill candidates, though she uses a one-off LLM classification, not a pipeline. → *Prototype a one-off classifier over Claude Code session logs that buckets sessions into comprehension, generation, review and process, and check whether the split is usable as a signal for SkillForge's skill-worthiness scoring.*
