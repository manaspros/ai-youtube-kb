# Guide: skills-self-improvement

*Synthesized by Sonnet from 77 talks since 2026-05-18.*

## State of the art

Skills are now the standard unit of agent know-how. A skill is a small folder with a short `SKILL.md`. Only its name and description sit in context. The body and reference files load on demand. Talks from May to October 2026 agree on this layout (`pFsfax19yOM`, `7jjudsEhBtM`, `LC3-P7v3yoI`).

Talks from May to October 2026 have moved on from "how to write a skill". They now cover three other problems.

- **Prove the skill works.** Practitioners run with/without-skill evals, trigger tests and CI gates on skill diffs (`0vphxNt4wyk`, `GmAQKINjv1E`, `vy7o1g2iHY8`).
- **Let the agent write and fix its own skills.** Traces and failed runs are distilled into skills. A human or an eval gate approves each change, usually through a PR (`u-o0sW9nwmk`, `TN3mj92oZ8I`, `9wZpvF3QleU`, `p7gaxmCUiIU`).
- **Govern the library.** Skills are treated as a supply chain. They get owners, versions, scans and a central registry, often served over MCP (`iKQ78wyJEXU`, `M05vON8i0aI`, `X6l4lpA0_NY`).

Self-improvement in practice means a loop with three parts. First, collect traces and feedback. Second, have an agent propose an edit to a skill, a prompt or a memory. Third, accept the edit only if a fixed eval improves and old tests do not regress (`2IxD9OB3XuQ`, `aHhB3sjGjkI`, `TeErpYBUIeM`, `x4e5O9zN0TE`). Most teams keep the human at the gate and the goal. They let the agent do the tedious middle.

Short, hand-written skills beat long generated ones. Gotcha lists beat doc summaries (`vy7o1g2iHY8`, `0vphxNt4wyk`).

## Consensus patterns

1. **Progressive disclosure is the base design.** Metadata always loads. The body loads when the description matches. Deep references load only on need. This works even on 270M to 4B on-device models (`BKWpYIWvAo4`, `-TiET_K-E_g`, `ynJyIKwjonM`, `LC3-P7v3yoI`).
2. **The description is a routing rule.** Write it from the user's side. Start with a directive. Add when-not-to-use cases (`pFsfax19yOM`, `0vphxNt4wyk`, `7jjudsEhBtM`, `GmAQKINjv1E`, `eBUyTS7SzV4`).
3. **Keep skills small and give constraints, not step lists.** Common caps are about 100 lines (`aeTb5BdmTTc`) to about 500 lines (`0vphxNt4wyk`). Move fixed procedures into scripts. Put must-not-miss rules inline, and detail in reference files (`JT3OzDKrucU`, `UNzCG3lw6O0`).
4. **Point to live docs. Do not copy them.** Models go stale on fast-moving SDKs. The skill should say where fresh docs are and how to search them (`JT3OzDKrucU`, `juoNbJiZUi0`, `vNCY9kXXyDQ`).
5. **Evaluate skills like code.** Run each task with and without the skill. Add trigger and negative cases. Prefer deterministic asserts first, and use an LLM judge only for what code cannot check. Repeat runs and use error budgets, because agents are non-deterministic (`0vphxNt4wyk`, `GmAQKINjv1E`, `bSG9wUYaHWU`, `JT3OzDKrucU`, `vNCY9kXXyDQ`).
6. **Every failure becomes a guidance update.** This covers corrections, PR comments, stop-hook questions and trace review. The fix goes into a skill or rules file, and a test case is added so it does not recur (`4_VQBbs2iQA`, `bSG9wUYaHWU`, `juoNbJiZUi0`, `YgEv7IQzGdM`, `6MudaeKdBSk`, `X6l4lpA0_NY`).
7. **Distill traces into skills, and learn from failures too.** The source can be successful runs, failed runs, recurring queries or accepted outputs (`u-o0sW9nwmk`, `9dYcwOkpCE8`, `eBUyTS7SzV4`, `Jx4ZFEAq6bY`, `XPj3mIKEtI4`, `jtzh-GBXBWc`).
8. **Gate every self-edit.** Common gates are a PR with human review, a held-out eval set the optimizer cannot touch, a regression suite, and a backtest against a baseline (`TN3mj92oZ8I`, `aHhB3sjGjkI`, `2IxD9OB3XuQ`, `TeErpYBUIeM`, `khVX_BUnEwU`, `x4e5O9zN0TE`).
9. **Enforce rules in code, not in prose.** Use state machines, hooks and hash receipts. Agents skip prompt rules and fake completion (`vy7o1g2iHY8`, `YXiLj4tJt5A`, `SQMCtZX3trg`, `6MudaeKdBSk`).
10. **Treat skills as a governed supply chain.** Scan for tokens, dangerous shell and injection. Give skills versions, owners and approvers. Publish through a registry or MCP front end (`iKQ78wyJEXU`, `cgimkNGNjvU`, `M05vON8i0aI`, `X6l4lpA0_NY`, `u-o0sW9nwmk`, `9wZpvF3QleU`).
11. **Domain experts write the skills.** Capture judgment by narrating real cases. Include ask-first questions and never-do limits (`gpmze-6ueGU`, `6MudaeKdBSk`, `eBUyTS7SzV4`).
12. **Cut the skill library by user job, not by data model.** Split a phase into its own skill when the agent under-does it (`7jjudsEhBtM`, `UNzCG3lw6O0`, `M05vON8i0aI`).

## Disagreements & open questions

- **Generated skills: help or hurt?** SkillsBench says human-written skills do best and AI-generated ones can lower scores (`0vphxNt4wyk`). A WorkOS team found 10k generated lines made evals worse, and 553 hand-written gotcha lines did better (`vy7o1g2iHY8`). Yet Runlayer, Neo4j and Vercel auto-distill skills (`u-o0sW9nwmk`, `XPj3mIKEtI4`, `9dYcwOkpCE8`). Runlayer and Vercel offer single-anecdote results, and Neo4j gives no numbers. Likely resolution: distillation is fine if an eval gate and a human review sit behind it.
- **Skill vs MCP.** Several talks say they are complements. Skills hold procedure and MCP holds execution (`LC3-P7v3yoI`, `GmAQKINjv1E`, `JT3OzDKrucU`). Others use MCP as the distribution layer for skills (`u-o0sW9nwmk`, `9wZpvF3QleU`, `M05vON8i0aI`). One claims MCP degrades past about 30 to 40 tools (`9wZpvF3QleU`, no data shown).
- **How many skills before routing breaks?** One speaker says a flat list breaks past about 10 skills (`7jjudsEhBtM`). Others route larger skill sets with resolver tables or vector retrieval (`eBUyTS7SzV4`, `xs-ob87TTzg`).
- **Model-invoked vs user-invoked.** Model invocation adds a description to every request and is unpredictable (`UNzCG3lw6O0`). Explicit invocation is the reliable way to load a skill (`GmAQKINjv1E`).
- **What is the success signal?** Binary outcomes work (booked or not, tests pass). Fuzzy quality is harder. Proxies include golden examples, harness-as-judge and human-calibrated judges (`p7gaxmCUiIU`, `7taOQBfjDyE`, `fnuNVFgLjHA`).
- **Where should learning live?** Options are weights, harness or memory. The advice is to use the cheapest, smallest durable layer first (`2IxD9OB3XuQ`, `OA-Mc60Rboo`, `zL1kLftVTlo`).
- **Verified gains are thin.** Many reported numbers are single anecdotes, vendor claims or one-off runs (`u-o0sW9nwmk`, `ZccJsdOE54M`, `2IxD9OB3XuQ`).
- **Instruction capacity.** The ceiling moved about 10x to roughly 2,000 to 5,000 rules. Verification of rule-following is now the hard part (`XzJD1bvXKjs`).

## How thinking changed over time

- **2026-05-18.** The focus is on writing good skills. Talks cover progressive disclosure, description-as-router, live docs, and with/without evals (`pFsfax19yOM`, `JT3OzDKrucU`, `GmAQKINjv1E`, `bSG9wUYaHWU`). Early signs of the loop appear: demand-driven context from agent failure, and a guidance flywheel (`_QAVExf_1uw`, `4_VQBbs2iQA`).
- **2026-06-18.** The mood is skeptical about quantity. "I deleted 95% of my skills" (`vy7o1g2iHY8`). Teams add session-log mining and stuck-session loops (`so9l_MwS2yg`, `KA5kPbdkK2E`). Langfuse shares trace-driven skill tuning (`vNCY9kXXyDQ`).
- **2026-07-18.** Evals become the rule: "Don't ship skills without evals" (`0vphxNt4wyk`). Self-improvement turns formal, with golden datasets and a protected eval set (`aHhB3sjGjkI`) and a three-gate verification (`2IxD9OB3XuQ`). Memory begins to consolidate into skills (`Jx4ZFEAq6bY`, `jtzh-GBXBWc`).
- **2026-08-18.** Governance arrives. Skills are seen as the new SDKs and as a supply-chain risk (`LC3-P7v3yoI`, `iKQ78wyJEXU`). Active Graph shows gated self-modification (`khVX_BUnEwU`). Continual learning is framed as compression of experience (`I6aiEf3aEFQ`).
- **2026-09-18 to 09-27.** Registries and org-scale playbooks appear (`9wZpvF3QleU`, `M05vON8i0aI`). Optimization methods get formal: GEPA's reflective search, a frozen-harness ratchet, and production-trace flywheels (`OA-Mc60Rboo`, `x4e5O9zN0TE`, `XyV6bSMyq-I`).
- **2026-10.** Outer-loop agents edit skills behind a PR gate (`TN3mj92oZ8I`, `tUPPVhBBcoM`, `X6l4lpA0_NY`). Teacher-doer loops converge on a portable `skill.md` (`p7gaxmCUiIU`). Trace-to-skill distillation reports its first big numbers (`u-o0sW9nwmk`). Platforms ship "dreaming" passes over past sessions, with the advice to gate them with your own evals (`qJtcEDc_WJU`).

## Numbers worth remembering

- Almost no public skills have evals. SkillsBench indexed about 50,000 GitHub skills. Skills lift results about 15% on average. Human-written skills do best (`0vphxNt4wyk`).
- A cap of about 500 lines for `SKILL.md` (`0vphxNt4wyk`). A cap of about 100 lines (`aeTb5BdmTTc`). A useful skill can be about 30 lines (`pFsfax19yOM`).
- 10k generated skill lines gave 68-minute evals. 553 gotcha lines ran in six minutes. One skill cut a task from 97% to 77% success when loaded (`vy7o1g2iHY8`).
- A distilled skill lifted one task from 36% to 100% success. This is a single anecdote (`u-o0sW9nwmk`).
- Auto-agent loop took a toy agent from 18% to 83% in about 10 iterations. A hand-tuned production agent gained 10% (`aHhB3sjGjkI`).
- Teacher-doer loop cut a browser task from $12 to $3. An OpenTable task fell from $6.22 to $0.51 and from 189 s to 27 s (`p7gaxmCUiIU`).
- One reflection round on 3 examples gave about 2x the gain of GRPO, which used 25,000 rollouts (speaker's claim, `OA-Mc60Rboo`).
- Trace analysis moved a stock question from 0% to about 90% in three iterations. A run took about 14 minutes (`_zUp6y9bDU8`).
- A fine-tune lifted function calling from about 46% to 90%+. Fine-tuning gave 20 to 40 points on small models (`-TiET_K-E_g`, `BKWpYIWvAo4`).
- Utility-weighted memory with skills: 66% baseline, 76% with memory, 80% with skills on a policy benchmark. Self-reported (`Jx4ZFEAq6bY`).
- Skill scanning found 1,500+ risks in 2,000+ skills. About 1,000 were likely fixed soon after (`iKQ78wyJEXU`).
- Flag-cleanup agent: 7 of 7 PRs passed CI, at about $1.26 per PR (`6MudaeKdBSk`).
- Self-modification on LongMemEval: 4 to 5 patches accepted over 8 to 13 loops. The gain was modest but significant (`khVX_BUnEwU`).
- A flat skill list in the prompt should be shortlisted past about 10 skills (`7jjudsEhBtM`). Keep static context under about 40% of the window (`LC3-P7v3yoI`).
- Instruction ceiling: the 2025 curves fell off around 200 to 300 rules, and the ceiling is now about 2,000 to 5,000. In a replication, models lost 30 to 50% of instructions by 500 rules (`XzJD1bvXKjs`).
- Loading one SKILL.md cost about 1.3k tokens, much less than the equivalent MCP tool set (`GmAQKINjv1E`).
- PostHog's integration wizard reaches about 15,000 users a month and cut two hours of integration to about eight minutes (`juoNbJiZUi0`).
- Range ran 24 skills after six months. Each was tested with 5 to 10 real runs before sharing (`gpmze-6ueGU`).

## From creator channels (Kai Explains, AI LABS, Better Stack)

Source: 52 creator videos from 2025-11 to 2026-10. Most are single-demo reviews or tutorials. Several have sponsor segments (for example `c47uqR7XB_c` and `qLfSDQ5NGh0`). Few report measured results. Where a number is measured, the note says so.

### Practical playbook

1. **Keep framework facts in CLAUDE.md or AGENTS.md, not in a skill.** Write a short index of version-matched doc file paths. Add a line that says to prefer retrieval over pre-training for that framework. The result is a Vercel test reported secondhand, with no task count or variance (`i0W90tlKfYg`).
2. **Name the skill in the prompt for workflows you run on purpose.** Upgrades and migrations are the example. Explicit "use the skill" wording raised the trigger rate to 95%, but the results were fragile. Wording that forced the skill made the agent skip project context. Naming both the skill and the project context worked better (`i0W90tlKfYg`).
3. **Write each skill description as a trigger line.** Say when to load the skill and when not to. Audit the library for skills with no trigger. The Harness² editor prompt calls a missing trigger the most-violated rule (`yCgfyQmqhPM`, `EHDzlot7LKU`).
4. **Put each rule in the cheapest layer that works.** The order is skill, then script, then sub-agent, then plugin, then always-on text. Keep always-on text short, since every word is paid on every run (`yCgfyQmqhPM`).
5. **A/B every instruction change before you keep it.** Run the same task with and without the change to CLAUDE.md, a skill or a rule. Keep the change only if behavior improves (`yCgfyQmqhPM`).
6. **Add two plumbing rules to agent instructions.** First, reopen the written file and trace each figure to its source before finishing. Second, save output to the exact filename the grader reads. The host says one rule of this kind drives much of the paper's gain. This is a paper result as the host reports it (`yCgfyQmqhPM`).
7. **Make "done" a command result.** Before work starts, write a gates file. Each gate has a checkbox, a verification command, the expected output words, and an evidence line that starts as "pending." A checker ticks the box only when the expected words appear. A ticked box that still says "pending" counts as unmet. One demo, no success rate (`c47uqR7XB_c`).
8. **Re-run sub-agent checks yourself.** Give each sub-agent only its plan and its own gates file. When it reports done, the orchestrator runs that task's gate commands before it moves on. Gates that cannot pass are named, with a reason, in the final report (`c47uqR7XB_c`).
9. **Plan file ownership before parallel work.** Write plan.md, listing each task and the files it owns. Build the shared foundation first, then run independent tasks at once. The host says this moved a run from a login page after 3 to 4 hours to a working app in about 2 hours with 10 agents. That is one anecdote (`c47uqR7XB_c`).
10. **Run the loop-fit test before you build any loop.** Check four things. The task recurs. The token budget covers failed rounds. Code can score the result. The agent can run the app and see failures. If any check fails, use one prompt instead (`qLfSDQ5NGh0`).
11. **Freeze the checks before the loop starts.** Write the checks first and review them in plain words. Move them into a locked folder. Block edits to that folder with a Claude Code settings deny rule. The video does not show the settings key. Commit the checks (`qLfSDQ5NGh0`).
12. **Build each feature in a fresh sub-agent and log every round.** A build skill hands each feature to a new feature-builder agent. Each round writes a results file. The file records what was kept or undone, what was tried, and which checks still fail (`qLfSDQ5NGh0`).
13. **Let an outer loop edit only the how-to-work section of program.md.** It reads the results file, finds failures that repeat, and rewrites that section. It never edits the checks. Run one feature at a time with a review after each (`qLfSDQ5NGh0`).
14. **Cap every multi-run loop, and cut its network access.** Set per-task run and spend limits before you start. The paper's minimum setting uses about 8x the tokens of a plain run, and its maximum about 40x. Its repo has no built-in cap. In one run, an agent downloaded its own grading rubric, so firewall the benchmark hosts first (`yCgfyQmqhPM`).
15. **Count the instruction file as input cost.** Test three arms: baseline, a plain "be concise" instruction, and a terse-output skill. Use multi-turn sessions with prompt caching. In one test, output fell 45%. A single small prompt still cost about 10% more with the skill. Over multi-turn sessions with caching, the presenter's total cost fell about 39% (`RuH3uiJy84A`).
16. **Retrieve tools per subtask instead of dumping the whole catalog.** Decompose the task. Embed each subtask and keep the top-k tools. Have a planner order the chosen tools as a DAG. The paper's claim is about 884k tokens down to about 1,160 per query. It is a self-run benchmark with mock executors (`eCZwexfka6E`).

### Tools creators recommend

- Skill Creator (Anthropic) — generates a skill folder with SKILL.md and scripts from a plain request; install it as a plugin at user or project scope — `Z9glbip8pZc`, `H7t3uUp3HVw`
- Superpowers plugin — brainstorm, then plan, then per-task TDD sub-agents with a commit per step; AI LABS notes the gates use a lot of context — `lq3rzXP4_vs`, `romGzY0Xu0s`
- Caveman — terse-output skill for Claude Code and Codex; the only measured test is the Better Stack one — `RuH3uiJy84A`, `qQ5uObNKBOU`
- Hermes Agent — self-improving agent with a capped memory file, a searchable session archive, and an MCP mode (`hermes mcp serve`) so other agents can call it — `HdxtLpL9CC8`, `Sb96po6S67k`
- planning-with-files — three files (taskplan.md, findings.md, progress.md) that a hook injects on every turn — `WJgxX0Eib6k`
- RTK skill — routes shell commands through rtk so only useful output enters context; test runs show only failures by default — `WJgxX0Eib6k`
- unlazy — gates ledger plus re-verification of sub-agent work; one demo run, no success rate — `c47uqR7XB_c`
- Task-observer skill — logs lessons per skill to log.md outside the project, for review before they are applied — `jyLKRN36-Dc`
- Harness Square (Google research, not a product) — an editor loop that rewrites harness files; the repo is a research release — `yCgfyQmqhPM`
- Cisco open-source skill scanner — scans third-party skills before install; NVIDIA's Skill Specter adds an LLM pass after the pattern scan — `M3P0hQMQtq0`, `KiTmBtyaeXg`
- Token Economizer (Microsoft) — learns per-project repeated failures and prunes unused tools; Microsoft's own cost figures are 23.6% and 30.9% lower on two Claude models — `1kQ_1_QL5Es`
- Reverse Engineer Anything — MCP server plus skill; tags each finding as seen, guessed or unknown — `rw0fqnrZgNM`
- Anatomy — skill that explains a concept as an interactive physical machine; a figure can take 30 to 90 minutes — `lyGYidIZK4I`
- Auto-skill from a session (Skillify, Boris Cherny's skill set) — turns a refined workflow into a SKILL.md draft; the host's reverse-engineered account of an internal command, unverified — `AhXfI1rSUPc`

### Where creators agree or clash with the conference talks

- **Agree: progressive disclosure and trigger-based loading.** Creators repeat the consensus that the description routes and the body loads on demand (`EHDzlot7LKU`, `Z9glbip8pZc`, `yCgfyQmqhPM`).
- **Agree: skills are not reliably invoked.** Vercel's test found the skill unused in 56% of runs. That fits the conference view that model-invoked loading is unpredictable. It is one secondhand eval (`i0W90tlKfYg`).
- **Agree: test with and without the skill, and gate self-edits.** Creators run with/without tests (`RuH3uiJy84A`, `yCgfyQmqhPM`) and command-checked gates (`c47uqR7XB_c`). Their tests are small, with about 10 prompts or one demo. Use them as checklists, not as numbers.
- **Clash: generated skills.** SkillsBench, cited by the conference talks, finds that human-written skills do best and that generated ones can lower scores (`0vphxNt4wyk`). Creators push generation: Skill Creator (`Z9glbip8pZc`), Hermes writing skills from use (`HdxtLpL9CC8`), and session-to-skill capture (`AhXfI1rSUPc`). Their evidence is single demos. Keep any generated skill behind a trigger test and a human review.
- **Clash between creators: always-on index or skills.** Vercel's result favors a passive index in CLAUDE.md for framework knowledge (`i0W90tlKfYg`). Harness² says always-on text is the most expensive layer and should move into triggered skills (`yCgfyQmqhPM`). One split works for both: facts always loaded, procedures loaded on trigger. The guide's progressive-disclosure consensus leans toward the Harness² side. This is still open.
- **Gap: per-turn cost.** Creators count the instruction file as a per-turn input cost (`RuH3uiJy84A`). The conference notes rarely do. Add that check to any skill rollout.

### Watch first

- `yCgfyQmqhPM` — Harness² critical read: the probe step, the 8x to 40x token cost, and why the headline gain is measured against an empty harness. Kai Explains, 4/5.
- `i0W90tlKfYg` — passive index versus skills, with trigger-rate numbers. Short. The evidence is secondhand, so verify before you adopt it.
- `RuH3uiJy84A` — three-arm cost test that counts input tokens. Shows where terse-output savings disappear.
- `qLfSDQ5NGh0` — loop-fit test, frozen checks, and an outer loop that rewrites program.md. Good for loop design. The 10x claim is not measured.
- `c47uqR7XB_c` — gates ledger with command-backed evidence. Sponsor segment and single demo; use the gate pattern, not the speed claim.
- `eCZwexfka6E` — decompose-retrieve-compose routing for large MCP catalogs. Benchmark is self-run and execution was mocked.

## Watch first

- `0vphxNt4wyk` — the lean skill-eval recipe: trigger tests, regex asserts, CI gate, capability vs preference skills.
- `vy7o1g2iHY8` — the best argument for short gotcha skills, code-enforced gates and paired evals, with numbers.
- `u-o0sW9nwmk` — trace-to-skill distillation, learning from failures, and an MCP-served governed library.
- `p7gaxmCUiIU` — a teacher-doer loop that converges into a portable `skill.md`, with cost and latency results.
- `2IxD9OB3XuQ` — a clear three-gate rule for safe continual learning: executable test, measured delta, regression suite.
- `aHhB3sjGjkI` — an eval-driven optimizer loop with a protected eval set and branch-per-hypothesis rollback.
- `TN3mj92oZ8I` — outer-loop agent edits a skill and opens a PR; agent-scoped memory with provenance.
- `iKQ78wyJEXU` — how to vet skills as a supply chain with hybrid regex and LLM scanning.

## Implications for our projects

**AgentOS SkillForge and EvolveCraft**
- The open question is the success signal. Start with binary, checkable outcomes such as tests passing or an exec-gate pass. Fuzzy quality needs calibrated judges (`p7gaxmCUiIU`, `7taOQBfjDyE`).
- Skill-worthiness scoring: cluster recurring queries by shape and distil only clusters that repeat (`9dYcwOkpCE8`). Use a memory-count threshold to consolidate memories into a skill (`Jx4ZFEAq6bY`).
- Mine both successes and failures from Govrix Scout traces (`u-o0sW9nwmk`). Cluster stuck sessions with a judge (`KA5kPbdkK2E`).
- Every distilled skill must pass three gates before publishing: an executable test, a measured delta, and a regression suite (`2IxD9OB3XuQ`). Also scan for injection and PII, which Scout already does (`u-o0sW9nwmk`, `iKQ78wyJEXU`).
- Use blank-injection holdouts to measure whether a skill helps, and prune hard (`KA5kPbdkK2E`).
- Use a frozen harness with a small editable policy surface, and keep only improvements (`x4e5O9zN0TE`). Copy the GEPA pattern of a Pareto pool plus rich evaluator feedback (`OA-Mc60Rboo`).
- Keep the optimizer away from the eval set (`aHhB3sjGjkI`).
- Lifecycle: version, owner, dependency list and approver per skill (`8G_1-3IO4ZQ`, `M05vON8i0aI`). Retire capability skills when the base model catches up (`0vphxNt4wyk`).

**AgentOS MemoryMesh**
- Store memories as conditional procedures. Weight retrieval by past usefulness. Let human corrections override older facts (`Jx4ZFEAq6bY`, `jtzh-GBXBWc`).
- Run a nightly consolidation pass that promotes, flags contradictions, prunes, and emits skills. Gate it with your own evals (`jtzh-GBXBWc`, `qJtcEDc_WJU`).
- Add decision traces as a memory type (`XPj3mIKEtI4`). Keep memory edits reviewable and deletable with provenance (`TN3mj92oZ8I`).

**AgentOS Crucible and Scout**
- Prefer hooks and gates that run as code. Rate-limit tool calls, block sensitive input before the model, and steer or ask before risky actions (`YXiLj4tJt5A`, `cgimkNGNjvU`).
- Hash receipts for test runs fit the exec-gate idea (`vy7o1g2iHY8`).

- Registry entries for skills should carry owner, version, dependencies, access rules and eval status. Search through an MCP front end (`M05vON8i0aI`, `X6l4lpA0_NY`, `u-o0sW9nwmk`).
- Scan at three points: authoring, CI and the registered artifact. Post findings as PR comments and emit SARIF. Back-scan old entries (`iKQ78wyJEXU`).
- Use the meta-tool trio search, get schema, execute, to keep large catalogues usable (`9wZpvF3QleU`).

- The same traces drive evals: log production and offline runs in one format, then turn misses into tasks (`XyV6bSMyq-I`). Failure clustering over traces is a product pattern (`fnuNVFgLjHA`, `_zUp6y9bDU8`).
- Replay failing traces to check a fix. Do not trust the agent's own claim (`fnuNVFgLjHA`).

**ProsHarness**
- Already-matching ideas: plan, critique, debate and checkpoints. Add enforced state-machine gates and hash receipts (`vy7o1g2iHY8`).
- Skill ranking could use paired with/without evals and trigger tests run through the headless CLI (`GmAQKINjv1E`, `0vphxNt4wyk`).
- Add a retro step that reads session logs and writes per-topic memory (`vy7o1g2iHY8`, `so9l_MwS2yg`). Schedule a stop-hook "what would have helped" question (`juoNbJiZUi0`).
- Outer-loop skill edits through a PR gate suit the phone-approval flow (`TN3mj92oZ8I`, `p7gaxmCUiIU`).
- Use blind sub-agent critique and a work log enforced by a commit hook (`SQMCtZX3trg`, `6MudaeKdBSk`).

**Cheap-model pipelines and entity resolution**
- Skills can be small and run on small models via load-skill plus constrained tool calls (`BKWpYIWvAo4`). Compare cheaper models on the same skill eval (`JomVvNDjGb8`).
- Natural-language checks judged over file and trace state keep evals cheap (`vNCY9kXXyDQ`). Regex asserts can be rerun on every new model (`0vphxNt4wyk`).
- The ER rule work fits the gotcha-list style: record each failure as a conditional rule, test it with no-harm checks, and keep it only if the pass rate rises (`vy7o1g2iHY8`, `x4e5O9zN0TE`).
