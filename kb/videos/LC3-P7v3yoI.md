# Skills are the New SDKs - Elvin Aghammadzada, DataRobot

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `LC3-P7v3yoI` · [watch](https://youtu.be/LC3-P7v3yoI) · **date:** 2026-08-18 · **length:** 26:40 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Elvin Aghammadzada · **orgs:** DataRobot
- **topics:** skills-self-improvement, context-engineering, mcp-and-tools · **tags:** agent skills, progressive disclosure, context rot, smart zone, skills vs MCP, tool definitions token cost, skill security, skill versioning, OpenClaw, Claude Code, Codex, DataRobot

> Elvin Aghammadzada (DataRobot) argues agent skills are a progressive-disclosure context tool that complements MCP, and that skills are software needing versioning, evals and security review.

## Summary
The talk starts from the claim that frontier models' advertised huge context windows are misleading, since more context adds more places for the model to be misled, and quality drops well before the window is full. The speaker says the model's behavior degrades past roughly 40% context use, which he calls the "smart zone" versus the "dumb zone," so a long list of MCP servers and instructions can push an agent into the weak zone before the user has typed anything. He proposes skills as a fix: only a short metadata index is loaded up front, and the full skill body is loaded only when the model decides it needs it. He frames skills as a competitive "fluency" advantage (reducing friction between intent and outcome) rather than the "friction" lock-in of the SaaS era. On skills versus MCP, he says they complement each other: MCP handles authentication, isolation and heavy remote compute, while skills handle reasoning and procedure, and a skill can even wrap an MCP server. He closes with risks (LLM-written skills may hurt performance, prompt injection, no isolation, weak marketplace verification) and advice to treat skills as software that is versioned, evaluated and tested.

## Key ideas
- **Bigger context windows do not mean better answers** — The speaker says long context adds more chances for the model to be misled or poisoned. He cites a 'Context Rot' paper as showing degradation after about 25% of the window is used (his example: 256K of a 1M window). Quality slides in long chats, so tool-heavy agents can get worse over a session. ([1:01](https://youtu.be/LC3-P7v3yoI?t=61))
- **Friction moats are giving way to fluency moats** — In the SaaS era, lock-in came from switching cost and integrations. The speaker says AI can now rewrite large codebases quickly, so switching is cheaper. He argues the new moat is fluency: a platform gets better for the user with each skill, so value compounds with use. ([3:55](https://youtu.be/LC3-P7v3yoI?t=235))
- **Keep the pre-chat context small (the 40% smart zone)** — He says models perform well up to about 40% of context use and degrade past that. Stacking system prompts, CLAUDE.md, built-in tools and many MCP servers can fill that budget before the first user message, so the agent starts in the weak zone. ([10:13](https://youtu.be/LC3-P7v3yoI?t=613))
- **Load context progressively, not all at once** — A typical agent context holds instructions, external data (uploads and RAG), execution history, cross-session memory and output format rules. Instead of hard-coding all of it, the agent loads each piece only when it is needed. ([11:39](https://youtu.be/LC3-P7v3yoI?t=699))
- **Skills work like a database index, with three levels of loading** — Level 1 is the front-matter metadata, under about 100 tokens, always in the system prompt. Level 2 is the markdown body, under about 5k tokens, loaded only when the model activates the skill. Level 3 is scripts, which can run so that only their output goes back into context. ([20:46](https://youtu.be/LC3-P7v3yoI?t=1246))
- **Skills and MCP solve different problems and can be combined** — MCP defines what actions and capabilities an agent has and runs in its own process, which gives isolation and access to protected data or big compute. Skills change how the agent thinks about a problem. A skill can point to an MCP server, dump its tool list, or call remote tools, so the two complement each other. ([15:36](https://youtu.be/LC3-P7v3yoI?t=936))
- **Skills carry real risks and need software discipline** — He says research found LLM-generated skills can hurt performance by adding tokens and reasoning time. Skills also raise prompt-injection risk, run on the user's own machine with no isolation, and marketplaces lack verification. His advice is to version, evaluate and test skills like any other software. ([24:33](https://youtu.be/LC3-P7v3yoI?t=1473))

## Techniques
- **Progressive disclosure via a skill index** — Keep a tiny metadata block (name and description, under about 100 tokens) always loaded. Load the full skill body only when the model decides it applies. Load scripts on demand and return only their output. *When:* When many tools, docs or instructions would otherwise fill the context before the first user turn.
- **Context budget ceiling** — Measure how much of the window the static setup uses before any chat (system prompt, CLAUDE.md, tool definitions). Keep it well under about 40%, and cut or defer tools that are not always needed. *When:* When agents get dumber early in a session or start with a crowded context.
- **Skill as a wrapper around an MCP server** — Have the skill's markdown name the MCP server to use, or list its tools in the skill, so the agent can call remote tools when needed while the skill holds the procedure. *When:* When the procedure is easy to describe in text but the heavy or protected capability must run remotely.
- **Split by role: skill for reasoning, MCP for execution** — Put the know-how and procedure in a skill. Put authentication, isolated processes, large data and GPU work in an MCP server. *When:* When choosing between a skill and an MCP tool for a new capability.
- **Treat skills as versioned, tested software** — Version skill files, write evals that check the agent's output with and without the skill, and test them before rollout. *When:* When skills are shared across a team or ship to customers.

## Numbers
- Context Rot paper: performance degrades after about 25% of the context window is used (speaker's example: 256K of 1M) ([1:01](https://youtu.be/LC3-P7v3yoI?t=61))
- Traffic to documentation sites from coding agents went from about 10% to 50%, year over year ([2:26](https://youtu.be/LC3-P7v3yoI?t=146))
- Model 'smart zone' is roughly the first 40% of context; beyond it, responses get much worse (speaker's experience, not a measured study) ([10:13](https://youtu.be/LC3-P7v3yoI?t=613))
- 15 MCP servers can consume over 100,000 tokens per session in tool definitions alone, before the conversation starts (speaker estimate, hedged 'I'm pretty sure') ([16:38](https://youtu.be/LC3-P7v3yoI?t=998))
- Skill front-matter metadata is under about 100 tokens; the body is under about 5k tokens, loaded on activation; the speaker says this is at least about 10x smaller than the equivalent MCP load ([16:38](https://youtu.be/LC3-P7v3yoI?t=998))
- 26+ platforms support the skills format (for example Claude Code, Codex, Copilot, Gemini CLI); hundreds of thousands of skills exist ([21:44](https://youtu.be/LC3-P7v3yoI?t=1304))
- Speaker's open-source skills repo had about 85,000 skills in use (speaker's figure) ([19:25](https://youtu.be/LC3-P7v3yoI?t=1165))
- Illustrative only: semantic search over 400 TB of documents, or 75 GPUs, is the kind of workload that still needs a hosted MCP server ([19:25](https://youtu.be/LC3-P7v3yoI?t=1165))

## Hot takes
- Skills and MCP are not competitors; skills are the way to use an MCP server with progressive disclosure
- Long context does not mean better results, and the 'infinite context' promise is misleading
- Skills create a fluency moat that compounds with use, replacing the SaaS-era friction moat
- A good base model with only a handful of tools plus a skills folder can replace many MCP servers
- LLM-generated skills can hurt performance, so humans should still write them

## Tools mentioned
Claude Code, Codex, Copilot, Gemini CLI, OpenClaw, ClawHub, MCP

## Relevance to our work
- **agentos** (2/3): SkillForge (L2D) mines agent telemetry into governed reusable skills; the talk's versioning, eval and isolation points map to that pillar's open questions on skill-worthiness and safety. → *Add a skill-level eval gate (run with vs without the skill, compare output and token use) to the SkillForge design, and store skill versions with their eval results.*
- **prosharness** (2/3): ProsHarness wraps Claude Code and handles skill ranking and long runs; the talk's three-level skill loading and 40% context ceiling directly apply to how the harness loads instructions and skills. → *Measure the static context size of a ProsHarness run before the first user turn; if it is above about 40% of the window, move skill bodies behind progressive loading.*
- **agentos** (1/3): Speaker's 'skills need isolation' point concerns Crucible-style sandboxing of skill scripts, but the talk gives no concrete sandbox design. → *Read the isolation section of the talk notes when planning how SkillForge scripts run inside Crucible.*
- **prosharness** (1/3): Speaker's point that skill scripts return only their output is a context-saving pattern relevant to checkpoint and resume runs. → *Consider having long-run harness steps print short summaries instead of full transcripts into the agent context.*
- **general** (1/3): Speaker's measure of tool-definition token cost (100k for 15 MCP servers, his estimate) is a useful sanity check for any multi-MCP agent setup. → *Count the tool-definition tokens of our current MCP setup once, to check whether it is near the 40% zone.*
