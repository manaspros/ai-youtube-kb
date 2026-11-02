# Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `aeTb5BdmTTc` · [watch](https://youtu.be/aeTb5BdmTTc) · **date:** 2026-08-18 · **length:** 16:57 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Aditya Khandelwal · **orgs:** Amazon AGI Lab
- **topics:** context-engineering, enterprise-adoption, coding-agents, skills-self-improvement · **tags:** team adoption, CLAUDE.md, AGENTS.md, progressive disclosure, skills, ship-it skill, code gardener, harness engineering, merge hell, shared setup, PR automation, agentic code review

> How a 10-person team got to shipping with coding agents: treat agent setup as a leadership job, share the best practices, invest in one high-value skill, and close the loop on slop.

## Summary
Aditya Khandelwal, from Amazon AGI Lab, describes leading a team of 10 that moved from individual agent setups to a shared, team-wide codebase setup for coding agents. He argues the adoption problem is organizational: fear, low confidence and mandated token use all get in the way, and making engineers effective with agents is a leadership responsibility. His playbook is to find the best engineers' practices and share them, build one high-value "ship it" skill that takes finished code to a reviewable PR, and wire issues, CI and agentic review into the repo with a nightly "code gardener" agent. He lists the problems he hit, including hundreds of agent-created issues in a few weeks, merge conflicts and throwaway experiments that leak into standards. For context, he recommends a thin CLAUDE.md/AGENTS.md index, skills kept under about 100 lines with the rest in linked files, and runbooks placed in code comments so agents find them through grep. He checks progress by watching what an agent does on its first prompt and how many tokens it uses before doing any work. The talk is practitioner-level and mostly qualitative, with few hard benchmarks.

## Key ideas
- **Making engineers effective with agents is a leadership and company job, not an individual contributor's side project.** — Engineers who ship 10 PRs a day look like outliers next to those shipping 1-2, and the slower ones end up with the review burden. Changing how a codebase is organized needs team buy-in, which an IC cannot force. ([5:39](https://youtu.be/aeTb5BdmTTc?t=339))
- **Adoption is an emotional problem as well as a tooling one: fear and confidence drive usage more than the tool does.** — He maps engineers on a fear axis and a confidence axis. Mandates and token-maxing pushed usage up while confidence fell, after slop shipped and incidents followed. The fix is to build trust in the shared setup. ([8:28](https://youtu.be/aeTb5BdmTTc?t=508))
- **Principles for an agent-ready codebase: progressive disclosure, close the loop, and iterate continuously.** — The agent should be able to find the right context at the right time without being told where to look. Slop will get in, so detection and self-healing have to be part of the pipeline. Setup decays as models change, so the work is ongoing. ([7:05](https://youtu.be/aeTb5BdmTTc?t=425))
- **Spread the practices of your best engineers instead of letting each person keep a personal setup.** — Find the ICs who make the codebase work well for them, then turn their practices into a shared setup. Engineers find it hard to admit their own setup is imperfect, so this takes deliberate effort. ([9:29](https://youtu.be/aeTb5BdmTTc?t=569))
- **Invest in one high-value skill that takes code from done to a reviewable PR.** — Their ship-it skill handles the PR description, review comments, CI failures and merge steps. It often ran for over an hour, which worried people until they saw it work, after which they trusted it and stopped babysitting. ([9:29](https://youtu.be/aeTb5BdmTTc?t=569))
- **Wire issues, CI and agentic review into the repo, and add a nightly code-gardener agent that checks organization.** — What counts as correct organization depends on the codebase. The skeptics only buy in once they can edit and experiment with the shared setup themselves. ([10:28](https://youtu.be/aeTb5BdmTTc?t=628))
- **Scale problems from a shared agent setup: issue floods, duplicate agent behavior, and merge pain.** — They grew to 400-500 issues in a couple of weeks because many agents were creating issues without being wired correctly. Experiments should opt out of the usual standards and be treated as prototypes. Expect merge hell. ([11:59](https://youtu.be/aeTb5BdmTTc?t=719))
- **Use an agent's failures as feedback to improve the shared skill rather than falling back to babysitting.** — Ask how to make the setup smarter, not whether the model is dumb. A model that seems to get worse usually means the codebase setup needs revisiting, since the model itself did not change. ([11:59](https://youtu.be/aeTb5BdmTTc?t=719))
- **Check the first prompt to see whether the setup works: is the agent grepping or going straight to the right place, and how much context does it burn before starting?** — Keep the top-level CLAUDE.md/AGENTS.md as a thin index. A startup context near the usual baseline is healthy, while 40-50K before any work signals a problem. Silent context burn and auto-compaction on simple tasks point to the same setup issue. ([15:40](https://youtu.be/aeTb5BdmTTc?t=940))

## Techniques
- **Thin CLAUDE.md/AGENTS.md index** — Keep the always-loaded top-level file short and make it a map to the detailed files, not one large document. The agent reads the index first and then opens only what it needs. *When:* When the root instruction file is growing and every session starts with a large context footprint.
- **Skill as a folder with a short SKILL.md** — Cap SKILL.md at about 100 lines and move the detail into files in the same folder that the skill links to. *When:* When writing team skills that must load cheaply and still carry depth.
- **Runbooks in code comments as discovery hooks** — Put the documentation for a module in comments inside the code. When the agent greps into the code, it reads the comment and follows it to the relevant doc. *When:* When agents keep missing docs that sit outside the code path they are editing.
- **One end-to-end ship-it skill** — Build a single skill that covers the path from finished code to a reviewable PR: opening the PR, writing the description, handling review comments and CI failures, and merging. *When:* When engineers do not trust agents to carry work through to a PR and keep babysitting them.
- **Nightly code-gardener agent** — Schedule an agent to run every night, check the codebase for things that are out of place according to your own definition of order, and file or fix them. *When:* When slop accumulates and organization drifts faster than people can clean it up.
- **Shared setup with an opt-out for experiments** — Keep one team-owned setup and let prototype code opt out of the usual standards explicitly, so experiments are not held to shipping rules. *When:* When exploratory work is blocked by standards meant for production code, or when prototypes leak into main.
- **First-prompt context audit** — Give the agent a first prompt and watch whether it greps or heads straight to the right file. Record the context used before any real work starts. *When:* When checking whether a repo setup actually makes the agent efficient.

## Numbers
- Team size led by the speaker: 10 people. ([0:12](https://youtu.be/aeTb5BdmTTc?t=12))
- Model release cadence is roughly every 1.5 to 2 months. ([4:37](https://youtu.be/aeTb5BdmTTc?t=277))
- Heavy sessions can use around 500K tokens of context, and auto-compact can trigger at 750K to 1M, even on a simple task. ([4:37](https://youtu.be/aeTb5BdmTTc?t=277))
- Productivity gap: about 10 PRs a day for top engineers versus 1 to 2 for others. ([5:39](https://youtu.be/aeTb5BdmTTc?t=339))
- The ship-it skill often ran for over an hour. ([9:29](https://youtu.be/aeTb5BdmTTc?t=569))
- The repo grew to 400-500 issues within a couple of weeks. ([11:59](https://youtu.be/aeTb5BdmTTc?t=719))
- Skill SKILL.md hard limit of about 100 lines. ([14:32](https://youtu.be/aeTb5BdmTTc?t=872))
- Startup context: a baseline of about 20K tokens is normal (auto-caption reads it as '2025 tokens', so the exact number is uncertain). Reaching 40K to 50K before any real work is a warning sign. ([15:40](https://youtu.be/aeTb5BdmTTc?t=940))

## Hot takes
- If your team is babysitting agents, the setup is wrong, not the agent.
- When a model suddenly seems dumber, the codebase setup needs work. The model did not change, so ask how to make the setup smarter.
- Agents that take a long time are a good sign, since engineers can go do other work while they run.
- Getting a codebase ready for agents is a leadership job, not an individual contributor's job.
- Mandating token use without building trust in a shared setup makes the slop problem worse.

## Tools mentioned
Claude Code, CLAUDE.md, AGENTS.md, CI/CD, issue boards

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code and already has loops and schedules. The talk's first-prompt context audit and nightly gardener-style scheduled loop apply directly to that harness. → *Log the startup context size (tokens used before the first real action) for each ProsHarness run and alert when it passes about 40K.*
- **agentos** (1/3): SkillForge aims to turn agent telemetry into reusable skills. The talk's point that agent failures should feed back into the shared skill is a related loop, though the talk is not about telemetry. → *When designing SkillForge's skill-worthiness step, treat failed or babysat agent runs as input that revises the skill, and keep skills to a short index plus linked files.*
