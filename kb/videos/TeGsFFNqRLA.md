# Fast Models Need Slow Developers — Sarah Chieng, Cerebras

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `TeGsFFNqRLA` · [watch](https://youtu.be/TeGsFFNqRLA) · **date:** 2026-06-18 · **length:** 18:02 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Sarah Chieng · **orgs:** Cerebras, OpenAI, AWS, NVIDIA, Groq, Together, Base10, Modal, Fireworks
- **topics:** coding-agents, inference-serving, testing-verification, context-engineering · **tags:** fast-inference, codex-spark, wafer-scale, prefill-decode, memory-wall, planner-executor, cherry-picking, context-compaction, external-memory, verification, steering-constraints

> Cerebras's Sarah Chieng argues that fast coding models (Codex Spark, ~1,200 tok/s) demand new habits: plan with a large model, execute with a fast one, verify every step, and keep context in bounded goals.

## Summary
The speaker says that coding agents have become 20x faster (Codex Spark at about 1,200 tokens/s versus roughly 40-60 for Sonnet or Opus), but developer habits built for slow models, such as huge prompts, huge commits and many parallel agents, will only produce bad code faster. She explains the inference stack briefly: the memory wall, the split between compute-bound prefill and memory-bound decode, mixture-of-experts, and KV-cache reuse. The practical playbook covers four areas: pairing a large planning model with a fast executor model and turning successful sessions into skills; making verification (tests, lint, hooks, diff review, browser QA) run on every step because it is now nearly free; generating many variants and picking the best one; and treating the agent as a real-time pair programmer with constraints such as no file deletion and a max diff size. Context management matters more at speed, because a context that once filled in 10 minutes now fills in about 30 seconds, so she recommends bounded tasks and a four-file external memory (AGENTS, PLAN, PROGRESS, VERIFY). The talk is partly vendor pitch, but most of the content is workflow advice that does not depend on the hardware.

## Key ideas
- **Fast models turn bad habits into bad code at scale.** — Massive one-shot prompts, huge commits and many agents running at once were tolerable at 50 tok/s. At 1,200 tok/s the same habits produce technical debt 20x faster, and nobody is verifying the output. ([1:07](https://youtu.be/TeGsFFNqRLA?t=67))
- **Split work between a big planner model and a fast executor model.** — Use a larger model for planning and long-horizon steps, then hand the checklist to a fast model running as sub-agents to execute each step. ([8:51](https://youtu.be/TeGsFFNqRLA?t=531))
- **Successful sessions can be captured as skills and replayed cheaply.** — Have the large model do the hard task once, distil the working trajectory into a skill so it becomes a verifiable, repeatable workflow, then let the fast agent rerun it in the background. ([8:51](https://youtu.be/TeGsFFNqRLA?t=531))
- **At high speed, verification costs almost nothing, so run it on every step.** — Test suites, linting, pre-commit hooks, diff reviews and browser QA can run after each step, not only before pushing. ([10:18](https://youtu.be/TeGsFFNqRLA?t=618))
- **Generate many variants and cherry-pick to induce taste.** — Models lack taste on their own. Generating 15 or 75 variants quickly and choosing the best one is a way to add taste, useful for UI, architecture or research directions. ([10:18](https://youtu.be/TeGsFFNqRLA?t=618))
- **Be the pilot in real-time collaboration, not a spectator.** — Keep two or three sessions open and steer them. Set constraints such as no file deletion, a max diff size, read-only scope, or only change this file. Redo work that is wrong. ([11:37](https://youtu.be/TeGsFFNqRLA?t=697))
- **Context fills about 20x faster, so keep tasks bounded and state external.** — Avoid running context at 80-100% because compaction loses information. Break large tasks into small goals and keep state in files that a fresh session can read to resume. ([14:20](https://youtu.be/TeGsFFNqRLA?t=860))
- **Four-file external memory for resumable sessions.** — AGENTS.md defines the sub-agents, PLAN.md holds the step-by-step checklist, PROGRESS.md records what is done, and VERIFY.md is the check run at each step. A new session reads PROGRESS.md and continues from there. ([15:48](https://youtu.be/TeGsFFNqRLA?t=948))

## Techniques
- **Planner-executor model split** — A larger model (e.g. GPT-5.4 or GPT-5.3 Codex) writes the plan and checklist; a fast model (Codex Spark) executes the steps one by one, spawned as sub-agents. *When:* Long multi-step tasks where planning needs more intelligence and execution needs speed.
- **Session-to-skill distillation** — After a hard task succeeds on a larger model, capture the trajectory as a skill with verification steps, then rerun it with a fast agent in the background. *When:* Repeatable workflows that you want cheap, consistent reruns of.
- **Per-step automatic verification** — After each checklist item, run tests, lint, pre-commit hooks, diff review and browser QA automatically, instead of batching checks at the end. *When:* When inference is fast enough that checks no longer slow the loop.
- **Parallel variant generation with cherry-picking** — Ask for many versions of the same output (e.g. 15 per sub-agent, across 5 sub-agents), then pick the best one. *When:* Design, UI, research directions or architecture options where variety matters more than a single answer.
- **Scoped steering constraints** — Explicitly ban file deletion, cap diff size, restrict the agent to read/write on named files, and give steering directions like 'only change this, don't touch types yet'. *When:* When you need to keep an agent's output reviewable and stop it from over-editing.
- **Automatic refactor pass after each task** — Add a step after each completed task that removes unused imports, trims unnecessary lines and enforces a consistent function structure. *When:* Running agents at high speed, where cleanup can be built into the workflow instead of done before commit.
- **Bounded goals with a context budget** — Split large tasks into smaller goals and keep context usage well below 80%, so compaction does not drop information. *When:* Any long agent session, more urgent with fast inference because context fills faster.
- **Four-file external memory (AGENTS/PLAN/PROGRESS/VERIFY)** — Store sub-agent definitions, the plan, progress state and per-step verification criteria in markdown files. Each new session starts by reading PROGRESS and resumes at the next task. *When:* Long-running work that must survive session resets or compaction.

## Numbers
- Codex Spark generates code at about 1,200 tokens/s; Sonnet and Opus families about 40-60 tokens/s, so roughly 20x faster. ([0:00](https://youtu.be/TeGsFFNqRLA?t=0))
- Popular model families (Gemini, Claude, GPT, Sonnet) stayed within about 50-150 tokens/s over the past two years. ([2:29](https://youtu.be/TeGsFFNqRLA?t=149))
- Hardware and memory movement account for 50-80% of inference latency (speaker's figure). ([2:29](https://youtu.be/TeGsFFNqRLA?t=149))
- Speaker says NVIDIA bought Groq (transcribed 'Grok') for $20 billion a few months earlier. This is a claim she made and was not checked. ([3:55](https://youtu.be/TeGsFFNqRLA?t=235))
- Context that used to take about 10 minutes to fill now fills in about 30 seconds at 20x speed. ([14:20](https://youtu.be/TeGsFFNqRLA?t=860))
- Cherry-picking example: 15 versions per agent, with 5 sub-agents, gives 75 candidates to choose from. ([10:18](https://youtu.be/TeGsFFNqRLA?t=618))

## Hot takes
- Fast models make bad habits dangerous: without changes, 1,200 tok/s just produces bad code 20x faster.
- Models have no taste, but generating many variants and picking one is a practical way to add it.
- The developer should be the one making decisions in the front seat, not the agent.
- Faster models are not the main point; developer experience is what improves.

## Tools mentioned
Codex Spark, Codex, GPT-5.4, GPT-5.3 Codex, Sonnet, Opus, REAP (router-weighted expert activation pruning)

## Relevance to our work
- **agentos** (2/3): The talk's skill-capture idea (successful large-model session becomes a verified skill that a cheap model replays) matches SkillForge's open question about skill-worthiness and success signals. It gives no measured data, though. → *Use the 'successful session distilled to skill, then replayed by a cheap model' pattern as a test case for SkillForge's skill-worthiness scoring.*
- **prosharness** (2/3): The four-file memory (PLAN/PROGRESS/VERIFY, plus AGENTS for sub-agents) is a simple version of checkpoint/resume for long runs. The planner-executor split also parallels ProsHarness's plan, critique and debate loop. → *Compare ProsHarness checkpoint/resume state files against the PLAN.md/PROGRESS.md/VERIFY.md scheme and add a per-step verify file if it is missing.*
- **general** (2/3): Concrete guidance for Claude Code sessions: keep context well below 80%, bound tasks, use scoped steering constraints (no deletes, max diff size), and run verification on every step. → *Add to CLAUDE.md or the working style: keep Claude Code tasks small, state a diff-size limit and a no-delete rule for long runs, and run tests after each step.*
