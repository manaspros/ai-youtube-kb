# Recursive Coding Agents - Raymond Weitekamp, OpenProse

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `3hXJI2q0Jz8` · [watch](https://youtu.be/3hXJI2q0Jz8) · **date:** 2026-07-18 · **length:** 23:48 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Raymond Weitekamp · **orgs:** OpenProse, MIT, Anthropic, Symbolica, ARC Prize
- **topics:** agent-architecture, coding-agents, multi-agent · **tags:** recursive-language-models, rlm, openprose, pi, claude-code, dynamic-workflows, subagents, orchestration, test-time-compute, arc-agi-3, long-cot, golden-session, declarative-workflows

> Raymond Weitekamp (OpenProse) on applying recursive language model (RLM) ideas to coding agents, with Claude Code dynamic workflows, the Pi extension, and OpenProse markdown workflows as ways to build them.

## Summary
The speaker argues the bottleneck for useful agents is reliability, not intelligence, and that the missing layer is how to specify, manage, reuse and verify agent work. An RLM treats the prompt as a variable in a code REPL, explores it symbolically, and delegates pieces to sub-LMs instead of loading everything into context. He gives a rubric for what counts as an RLM: an executable environment, an externalized prompt, code that calls the model, the model choosing the decomposition, and state that stays symbolic. Hard-coded map-reduce pipelines fail the last test because the model does not choose the decomposition. He says coding agents can be RLMs but are not automatically so, and shows three routes: wrapping an RLM package as a tool, a Pi extension where Pi calls Pi to a set depth, and Claude Code dynamic workflows. He then presents OpenProse, a markdown "language" that a coding agent compiles, which declares subagents, has the parent verify their output, and wires in skills and tools as explicit dependencies. He ends with capturing a successful ("golden") session as a reusable workflow. Much of the talk is a tour of the speaker's own projects and a promotion of OpenProse, and most benchmark claims are his own reports without detail.

## Key ideas
- **The bottleneck is reliability, not raw intelligence** — The speaker says models know enough but cannot reliably deliver outcomes, so users cannot trust them. He gives an anecdote where an agent emptied his crypto wallet. ([0:00](https://youtu.be/3hXJI2q0Jz8?t=0))
- **Today's agents are mismanaged geniuses** — The missing layer is how to specify, manage, reuse and verify agent work. He argues the next step is behavioral and orchestration-level, not more raw intelligence. ([1:29](https://youtu.be/3hXJI2q0Jz8?t=89))
- **In an RLM the prompt is a variable, not the input** — The full prompt (possibly many files) lives in a REPL. The model pokes at it symbolically and hands pieces to sub-LMs, rather than reading it all into its context window. ([2:29](https://youtu.be/3hXJI2q0Jz8?t=149))
- **A rubric decides what counts as an RLM** — Required: an executable environment, an externalized prompt, code that calls the model, the model choosing how to decompose the problem, and state that stays symbolic. Plain LLMs, RAG and hard-coded map-reduce (such as LambdaRLM) come close but miss the model-driven decomposition. ([9:07](https://youtu.be/3hXJI2q0Jz8?t=547))
- **Coding agents can be RLMs but are not automatically RLMs** — Swapping agents and subagents for LMs and sub-LMs gives the same structure. The speaker's first experiment was just wrapping the RLM package as a CLI tool a coding agent can call, for example to sift a 100M-token corpus. ([10:31](https://youtu.be/3hXJI2q0Jz8?t=631))
- **Pi can be made fully recursive with a pure extension** — Pi, a minimal extensible coding agent, originally needed a fork. After Pi's extension system changed, the speaker built a pure extension where pi calls pi to any depth, plus a wrapper called ypi. ([12:01](https://youtu.be/3hXJI2q0Jz8?t=721))
- **Claude Code dynamic workflows make it recursive** — The speaker wrote two workflows: a hard-coded map-reduce (explicitly not an RLM) and a deep-research pass over a file system (picking a handle, assigning it to an agent, bringing back findings), which he argues is RLM-like. ([16:15](https://youtu.be/3hXJI2q0Jz8?t=975))
- **OpenProse: a markdown spec compiled by the coding agent** — A .pros.md file is logical English, and any agent with a filesystem and subagents can run it as an RLM. It declares subagent work, makes the parent session verify subagent output, and lists skills and tools as explicit dependencies per subagent. ([17:41](https://youtu.be/3hXJI2q0Jz8?t=1061))
- **Capture a golden session as a reusable workflow** — An agent deconstructs a successful session from Claude Code, Codex or Pi into a reusable OpenProse workflow, aiming to reproduce good performance reliably. ([20:34](https://youtu.be/3hXJI2q0Jz8?t=1234))

## Techniques
- **RLM as a tool call for a coding agent** — Wrap an RLM package as a CLI, so the coding agent can invoke it as a tool when a task needs symbolic exploration of a large corpus. *When:* The input (e.g., a corpus of about 100M tokens) is far too large to read into the agent's context.
- **Recursive agent via a pure Pi extension** — Write a Pi extension that lets the agent spawn the same agent as a tool call, with a configurable recursion depth. The speaker's earlier version required a fork. *When:* You want a self-calling coding agent without forking the harness.
- **Map-reduce versus deep-research workflows in Claude Code** — Define a workflow that assigns each part of a directory to a subagent, then merges findings. The deep-research variant lets each subagent go further into its own part recursively. *When:* Large refactors, scale migrations, or analysis across many files where parallel work and a final merge pay off.
- **Declarative workflow with parent verification** — Write a markdown spec that names subagents, their skills and CLI tools as explicit dependencies, and a parent step that checks each subagent's output before accepting it. *When:* Multi-step work where each step needs specific tools or skills and the output must be checked before use.
- **Adversarial or skeptical subagent roles** — Run red-team or skeptical agents in parallel to try to break or challenge the work, with results checked in the parent session. *When:* Audits, bug sweeps, or hardening agent-written changes.
- **Golden session distillation** — Have an agent deconstruct a successful session into a reusable workflow file and rerun it to get the same good outcome again. *When:* A run went well and you want to repeat it reliably instead of relying on luck.
- **Small local model as RLM root** — Run a small model (the speaker used Qwen 3.5 9B) with a code REPL and recursive sub-calls, instead of a single large model reasoning in one pass. *When:* Long multi-step reasoning tasks where the chain of thought must be held over many steps and a small local model is wanted.

## Numbers
- RLMs process information many orders of magnitude larger than their context window (OOLONG), tens of millions of tokens. ([4:52](https://youtu.be/3hXJI2q0Jz8?t=292))
- Speaker's own claim: the default RLM harness works as a top-10 memory system with no modification, and better with small changes. ([4:52](https://youtu.be/3hXJI2q0Jz8?t=292))
- On Long COT, Qwen 3.5 9B run as an RLM beats Opus and GPT 5.4 used as plain LLMs on long reasoning tasks. No scores given in the talk. ([6:18](https://youtu.be/3hXJI2q0Jz8?t=378))
- ARC-AGI-3: frontier model top scores were around 2-3%. Symbolica's agentica RLM harness reached a score in the 30s percent within hours of release (speaker's report). ([6:18](https://youtu.be/3hXJI2q0Jz8?t=378))
- Example scale: sifting a corpus of about 100M tokens through an RLM tool call. ([10:31](https://youtu.be/3hXJI2q0Jz8?t=631))

## Hot takes
- RLMs are the new reasoning models, and the next paradigm of test-time compute, because code execution is a form of reasoning.
- Coding agents can be RLMs, but being an agent does not make a system an RLM; the model must choose the decomposition and state must stay symbolic.
- The next gain comes from orchestration and behavior, not raw intelligence.
- Benchmark leaderboards that ban tool-using harnesses should have separate open harness boards; the speaker does not care whether reasoning happens in latent space, reasoning tokens or code.
- Claude Code became RLM-capable once dynamic workflows shipped, though it was not at launch.

## Tools mentioned
Claude Code, Codex SDK, Pi, OpenProse, DSPy (dspy.rlm), RLM package (Alex Zhang), Agentica (Symbolica), Axe, Unix RLM (bash), LambdaRLM, Qwen 3.5 9B

## Relevance to our work
- **agentos** (2/3): The talk's ideas on capturing a successful session as a reusable workflow, and on RLM-style memory over a default harness, bear on the SkillForge open question about skill-worthiness and on MemoryMesh retrieval. The evidence is the speaker's own claims, not measured results. → *Build a small SkillForge experiment: take one successful agent session from telemetry, have an agent distill it into a replayable workflow file, then rerun it and measure whether the success signal holds.*
- **prosharness** (2/3): ProsHarness runs plan, critique and debate loops around Claude Code. OpenProse's declarative subagent specs, parent verification step and explicit skill and tool dependencies map closely onto that loop. → *Express one ProsHarness plan-critique-debate loop as a declarative markdown workflow that names each subagent, its skills and tools, and a parent verify step, then compare it with the current code path on reliability and checkpoint behavior.*
- **general** (2/3): Recurring interests in subagents, multi-agent orchestration and context engineering. The talk gives a concrete test for what separates an RLM from a coding agent with subagents. → *Read the recursivecodingagents.com companion repo and the RLM paper, and apply the five-part rubric to one of our own multi-agent workflows to see which parts are missing.*
