# The Dark Arts of Skill Engineering — Paul Bakaus, Renaissance Geek (Impeccable)

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `SQMCtZX3trg` · [watch](https://youtu.be/SQMCtZX3trg) · **date:** 2026-09-27 · **length:** 1:04:53 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Paul Bakaus · **orgs:** Renaissance Geek, Anthropic, Cursor, Google
- **topics:** skills-self-improvement, coding-agents, context-engineering, evals · **tags:** skill-engineering, sub-agents, adversarial-critique, forced-divergence, hooks, cross-harness, per-model-overfitting, ablation-testing, design-linting, prompt-caching, live-browser, llm-as-judge

> Paul Bakaus (Impeccable) on building production agent skills as harness extensions: blind sub-agents, forced divergence, scripts, hooks and per-model builds, rather than prose alone.

## Summary
Paul Bakaus, author of the open-source Impeccable design skill, walks through what he learned by growing a single prompt-style skill into a multi-file, cross-harness skill system. His thesis is that a skill is an extension of the coding harness (like MCP), so it should use scripts, hooks, sub-agents and harness features, not just prose rules. He argues that prose rules only move the model to the next common output ("the median is the model's gravity"), so he uses seeded randomness and sub-agent ranking to force divergence. For review tasks he runs two blind sub-agents (a design-judge LLM and a deterministic detector) and merges their results, which avoids self-rating and anchoring. He covers routing between sub-skills, memory across sessions, scripts whose stdout instructs the model, pre/post-tool hooks, and a live-browser mode that uses no MCP. The second half lists harness and model differences (sub-agent permissions, ask-user tools, background-task wake-up, per-model overfitting) and how he handles them with per-harness builds, unskippable gates and ablation-tested rules. Evals are an LLM-driven harness over several models plus a design judge, with a caveat that taste is hard to evaluate automatically.

## Key ideas
- **Prose rules do not fix convergence** — Banning a common choice (for example a font) only moves the model to the next most common option. The speaker treats prompting as the starting level and harness engineering as the goal. ([3:45](https://youtu.be/SQMCtZX3trg?t=225))
- **Blind sub-agents beat self-review** — A model asked to grade its own work rates it very high. Two sub-agents that never see each other's output, one acting as a design judge and one running a deterministic linter with browser evidence, give a more balanced critique when the main thread merges them. ([8:09](https://youtu.be/SQMCtZX3trg?t=489))
- **Sub-agent permission differs by harness** — Claude Code can spawn sub-agents programmatically. Codex needs the user to ask for them, so the skill must tell the model to stop and ask, and to state that it is giving a degraded experience if it cannot spawn them. Otherwise Codex takes the easier path and skips them. ([13:31](https://youtu.be/SQMCtZX3trg?t=811))
- **Seed randomness to force divergence** — Three ways to escape the model's usual outputs: exclude its top-three picks, generate many ideas and have a fresh sub-agent rank them (the sub-agent has no session context), or seed creativity from a script that outputs a random starting point such as a color from a list of about 100. ([17:35](https://youtu.be/SQMCtZX3trg?t=1055))
- **Route between sub-skills by register** — A large skill acts like a mixture of experts. Based on the brief, it loads different rule files for brand work (attention-grabbing pages) and product UI work (native-feeling, system fonts), since one general file blurs the instructions. ([21:51](https://youtu.be/SQMCtZX3trg?t=1311))
- **Persist state in the skill folder to make runs compound** — Save each critique as a file in a project folder (git-ignored). Later sessions read the prior files to see progress and user preferences, and multi-session refactors can work one file at a time. ([23:20](https://youtu.be/SQMCtZX3trg?t=1400))
- **Scripts that print instructions are followed more reliably than prose** — A script run at skill start (context.mjs) gathers project files and, when something is missing, prints structured JSON with the exact next step. The model follows stdout instructions more than rules buried in the prompt. The cost is that dynamic output breaks prompt caching for that part. ([26:16](https://youtu.be/SQMCtZX3trg?t=1576))
- **Use hooks as passive guardrails, with pre-tool blocking for weaker models** — A design linter runs as hooks in Claude Code, Cursor, Codex and Copilot on every edit. Post-tool hooks report violations after a write, but weaker models ignore them, so pre-tool hooks block the write. Ignore rules are needed to handle false positives. ([28:00](https://youtu.be/SQMCtZX3trg?t=1680))
- **Live-browser mode with no MCP** — A small local server injects a script into the dev server. The user's clicks and comments are sent over server-sent events to a poller. The poller exits with a stdout message, which wakes the model to act on the selection, so the in-app browser and the chat thread work as one loop. ([34:00](https://youtu.be/SQMCtZX3trg?t=2040))

## Techniques
- **Blind adversarial critique** — Run two or more sub-agents that never see each other's output (for example a judge and a deterministic checker), then have the main thread synthesize one result. *When:* Code review, design critique, security audits, plan/RFC review, or ranking outputs, where self-grading anchors on the model's own work.
- **Anti-attractor divergence** — Inject randomness from user input or a script, exclude the model's top-N picks, or have a fresh sub-agent rank a large batch of generated ideas. *When:* Generating many distinct options (themes, shaders, palettes) where the model keeps returning the same few.
- **Register routing inside one skill** — Classify the request early and load different rule files per mode, instead of one long file with if/else branches. *When:* A skill covers several audiences or job types that need conflicting rules.
- **Cross-session skill memory** — Save each run's output to a git-ignored folder in the repo and have later runs read them as history and user preferences. *When:* Resumable, multi-session refactors or migrations, and skills that should learn a user's preferences.
- **Scripts that print next-step instructions** — Run a script inline at skill start and have it emit structured JSON or text saying exactly what to do next (for example, missing files, update prompts). *When:* Setup, onboarding, environment checks, or adaptive flows where the model must follow exact steps. Accept the loss of prompt caching for that part.
- **Pre-tool-use blocking hooks for weaker models** — Use pre-tool hooks that block a bad write, instead of post-tool hooks that only warn, and add per-file or per-rule ignore rules for false positives. *When:* Shipping enforcement to models that do not reliably act on post-write feedback.
- **Hook-driven feedback loop from a skill** — Ship hooks with the skill that validate each edit against the skill's rules, so the agent fixes violations without being asked. *When:* Design systems, lint-like style rules, or team conventions that should hold even when the agent forgets to call the skill.
- **Unskippable gates with logged results** — Split the procedure into numbered gates, require the model to log each one's pass result, and say that skipping one is not allowed. *When:* Long procedures where the model is known to skip or compress steps, such as GPT-family models with a Codex harness.
- **Per-harness and per-model builds** — Compile one skill source into several variants: substitute the harness's ask-user tool, add model-specific guard text, and install each variant to its own directory. *When:* Distributing a skill to several harnesses and models, where symlinks or a generic package installer will not work.
- **Ablation testing of rules** — Tag each rule with a unique ID, remove it, run evals across models, and check the result with a deterministic detector. Keep the rule only if the check changes. *When:* Large rule sets where you need to know which lines actually change behavior.
- **LLM-as-user with a judge panel** — Reproduce each target harness's tools and a simulated user that answers the skill's questions, then score the outputs with several judges across many niches and models. *When:* Regression testing a skill release across models and harnesses.
- **Inverted judges** — When a judge model shows a known bias (for example, rating crammed first viewports higher), invert its score for that criterion. *When:* Judges with a documented, consistent bias that is easier to flip than to fix.

## Numbers
- The first design skill was about 55 lines of named rules with no scripts; he later calls 250 lines of prose insufficient to change model defaults. ([3:45](https://youtu.be/SQMCtZX3trg?t=225))
- Pre-written color palettes used as a random seed: over 100 hand-picked primary colors. ([19:00](https://youtu.be/SQMCtZX3trg?t=1140))
- A shader library target of about 100 shaders, produced by generating ideas and having a sub-agent rank them. ([17:35](https://youtu.be/SQMCtZX3trg?t=1055))
- Eval matrix per release: about 20 niches, GPT-5.5, Opus and Sonnet, 5 to 10 runs per combination, plus comparison against the Anthropic front-end design skill. ([54:06](https://youtu.be/SQMCtZX3trg?t=3246))
- Codex design-review gate list has eight gates that must each be logged. ([47:07](https://youtu.be/SQMCtZX3trg?t=2827))
- Every rule in Impeccable is ablation-tested across models. ([44:42](https://youtu.be/SQMCtZX3trg?t=2682))

## Hot takes
- Prompting is the starter level, and the goal is harness engineering.
- Slop is a moving target: each ban just pushes the model to the next cluster (Claude beige replaced purple gradients).
- If a gate can be skipped, the model will skip it.
- Taste cannot be solved at the model level, and models are bad at judging it.
- Most distributed skills should be written by the people who use them, and skill authors should battle-test more before shipping.
- Symlinking one instruction file across harnesses is fine for a personal skill but not for shipping to many users.

## Tools mentioned
Claude Code, Codex, Cursor, GitHub Copilot, Gemini, Playwright, skills.sh, npx skills

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code and runs plan, Codex critique and debate steps, so the blind-sub-agent critique and the Codex sub-agent permission gotcha apply directly. Hooks and the background-task wake-up difference also bear on loops and schedules. → *Make the plan critique step run two blind sub-agents (a judge and a deterministic checker) that never see each other's output, then merge the results, and test it in both Claude Code and Codex, since Codex needs explicit permission to spawn sub-agents.*
- **general** (2/3): Matches recurring interests in context engineering, subagents and evals: per-model overfitting, unskippable gates, persisted run history and ablation tests for prompt rules. → *For any shipped skill, keep a per-model list of known overfits and tag each rule with an ID so it can be ablation-tested against the deterministic check.*
- **agentos** (1/3): SkillForge mines telemetry into governed skills and asks how to score skill-worthiness. The talk's ablation testing and per-run skill memory offer a loose way to test which skill rules matter. → *When drafting SkillForge's skill-worthiness scoring, try an ablation pass: tag each rule in a mined skill with an ID, remove it, rerun the eval, and keep the rule only if the deterministic check changes.*
