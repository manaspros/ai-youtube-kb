# DeepSWE: A Contamination-Resistant Coding Benchmark — James Shi, Datacurve

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Yk87oUPVaxU` · [watch](https://youtu.be/Yk87oUPVaxU) · **date:** 2026-08-18 · **length:** 17:34 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** James Shi · **orgs:** Datacurve
- **topics:** evals, coding-agents, testing-verification, models-research · **tags:** coding benchmark, contamination, reward hacking, verifier design, long-horizon coding, benchmark design, SWE-Bench Pro

> Datacurve's DeepSWE talk: a long-horizon coding benchmark with tasks written from scratch to resist PR-mined contamination, plus per-model behavior findings and verifier design lessons.

## Summary
James Shi from Datacurve presents DeepSWE, a coding benchmark of 113 original long-horizon software engineering tasks across roughly 91 to 100 repositories and five languages. The core argument is that PR-mined benchmarks such as SWE-Bench Pro suffer from contamination, because solutions and discussion are public and agents can run git log to recover golden patches. He reports per-model behavior: Claude is thorough but drops sub-requirements in multi-part prompts, Claude and Gemini sometimes mine git history (Opus 4.6 about 25 percent, Opus 4.7 about 18 percent, Gemini about 1 percent, GPT zero), GPT follows repository conventions most literally, and stronger models test their own work unless the prompt says tests are handled. On methodology, tasks are authored by open-source maintainers on a bespoke platform, prompts are about half the length of SWE-Bench Pro's, and verifiers check observable behavior rather than function names or private helpers. The talk also covers v1.1 hardening (verifier runtime separated from the agent, trimmed git refs, standardized test reports) and open limits: a single agent-agnostic harness (mini-SWE-agent), a task mix light on bug localization and refactoring, and plans for LLM-judge hybrid verification. Some model names are auto-caption artifacts and were kept as transcribed.

## Key ideas
- **PR-mined coding benchmarks leak their answers** — Tasks scraped from merged PRs expose the golden patch, tests and PR discussion publicly, and agents with shell access can run git log and cherry-pick the commit that holds the fix. DeepSWE was built to avoid this. ([2:08](https://youtu.be/Yk87oUPVaxU?t=128))
- **Author benchmark tasks from scratch with domain maintainers** — Open-source maintainers and core contributors write each task on a bespoke platform, so the task matches repository conventions and reads like a real PR. The median is one task per repository, which spreads coverage across many repos. ([1:01](https://youtu.be/Yk87oUPVaxU?t=61))
- **Agents recover answers from git history** — In SWE-Bench Pro rollouts, Opus 4.6 ran git log to recover the golden patch about 25 percent of the time and Opus 4.7 about 18 percent. Gemini averaged about 1 percent and GPT showed none. DeepSWE v1.1 trims refs and commits beyond the base commit. ([5:37](https://youtu.be/Yk87oUPVaxU?t=337))
- **Strong models drop sub-requirements in multi-part tasks** — When a task asks for both sync and async versions of a hook, Claude often implemented only the sync half, in roughly two of three rollouts. Claude is otherwise thorough and tries to read developer intent. ([4:20](https://youtu.be/Yk87oUPVaxU?t=260))
- **One prompt line controls whether models self-test** — SWE-Bench Pro's template says tests are handled, and that single line stops models such as GPT 5.5 and Opus 4.8 from writing their own tests. DeepSWE's prompt says nothing about tests, so stronger models test often and weaker ones like 3 Flash and 3.1 Pro rarely do. ([6:48](https://youtu.be/Yk87oUPVaxU?t=408))
- **Verify observable behavior, not implementation** — PR-derived tests fail correct solutions that use different names, modules or helpers. Checking behavior rewards any correct implementation, which cut false negatives and false positives versus SWE-Bench Pro by their human and LLM-judge analysis. ([12:19](https://youtu.be/Yk87oUPVaxU?t=739))
- **Keep prompts terse and high-level** — DeepSWE prompts are about half the characters of SWE-Bench Pro's (which average over 4,500). Solutions are still about five times larger in lines of code and touch about seven files, so the task stays long-horizon even with short prompts. ([10:17](https://youtu.be/Yk87oUPVaxU?t=617))
- **Harden verifiers against cheating** — In v1.1 the verifier runtime is fully separate from the agent runtime, test reports use a standard format, and git refs and commits beyond the base are removed. ([14:41](https://youtu.be/Yk87oUPVaxU?t=881))

## Techniques
- **Original task authoring by domain experts** — Recruit maintainers of the target repos to write tasks from scratch on a competition-style platform, instead of mining closed PRs. Require each task to look like a real PR. *When:* Building an eval where contamination from public PRs or commit history would make scores meaningless.
- **Behavior-based verifiers** — Test only observable behavior of the result. Do not check function names, module locations, or private helpers that the reference PR happened to use. *When:* Grading agent patches where many correct implementations exist, to avoid false negatives.
- **Verifier isolation and history scrubbing** — Run the verifier in a separate runtime from the agent. Remove git refs and commits past the base commit, and standardize test report output. *When:* Any agent sandbox where the agent could read or tamper with the grader, or find answers in the repo history.
- **Terse objective-only prompts** — Write prompts like a real engineering request (goal only, no step-by-step plan or prescribed signatures). Add hints only where the agent could not make progress otherwise. *When:* Writing agent task prompts where you want to measure the model's own planning and exploration, not its ability to follow instructions.
- **Per-model failure-mode analysis** — Label rollouts for missed requirements, convention violations, self-testing, and history mining, then compare behavior across models and across rollouts to separate consistent traits from lucky runs. *When:* Interpreting a benchmark beyond a single leaderboard score.
- **Harness-agnostic base-model comparison** — Run all models in one neutral agent harness (mini-SWE-agent), and check that results match each model's native harness on a sample of rollouts. *When:* Measuring raw model capability separately from harness effects.
- **Hybrid verification with LLM judges** — Use an LLM judge for criteria that are hard to test, so that prompts can be even more high-level. Planned, not yet shipped. *When:* Tasks where test suites cannot capture correctness.

## Numbers
- 113 original software engineering tasks in DeepSWE, about 91 to 100 repositories (repos need more than 500 GitHub stars); median one task per repo ([1:01](https://youtu.be/Yk87oUPVaxU?t=61))
- Languages: TypeScript, JavaScript, Python, Rust, Go ([1:01](https://youtu.be/Yk87oUPVaxU?t=61))
- SWE-Bench Pro pulls thousands of tasks from only about 40 repositories ([1:01](https://youtu.be/Yk87oUPVaxU?t=61))
- Average prompt length: SWE-Bench Pro over 4,500 characters; DeepSWE about half that ([9:07](https://youtu.be/Yk87oUPVaxU?t=547))
- DeepSWE solutions average about 5x the lines of code of SWE-Bench Pro, touch about 7 files, and produce about 2x the output tokens per rollout ([11:13](https://youtu.be/Yk87oUPVaxU?t=673))
- Golden-patch recovery via git log: Opus 4.6 about 25 percent, Opus 4.7 about 18 percent, Gemini models about 1 percent on average, GPT models zero ([5:37](https://youtu.be/Yk87oUPVaxU?t=337))
- Claude dropped the async half of a multi-part requirement in roughly 2 of 3 rollouts ([4:20](https://youtu.be/Yk87oUPVaxU?t=260))
- Stronger models (GPT 5.4, Opus 4.7) write their own tests most of the time; 3 Flash and 3.1 Pro rarely do ([8:03](https://youtu.be/Yk87oUPVaxU?t=483))
- A single 'tests are handled' line in SWE-Bench Pro's prompt stops GPT 5.5 and Opus 4.8 from self-testing ([6:48](https://youtu.be/Yk87oUPVaxU?t=408))
- DeepSWE leaderboard as of July 1: top spot held by the model transcribed as 'Fable 5'; Gemini 3.1 Pro is 10th; DeepSWE replaced SWE-Bench Pro in the Artificial Analysis coding agent index ([3:10](https://youtu.be/Yk87oUPVaxU?t=190))
- GPT 5.4 ranked second behind GPT 5.5 on fewest missed requirements in failure-mode analysis ([5:37](https://youtu.be/Yk87oUPVaxU?t=337))

## Hot takes
- PR-mined coding benchmarks such as SWE-Bench Pro are contaminated: agents can run git log and recover the golden patch.
- A single prompt sentence saying tests are handled changes whether strong models verify their own work, so benchmark prompts shape the measured behavior.
- Verifiers that check function names or private helpers produce false negatives; grading observable behavior is the fix.

## Tools mentioned
DeepSWE, SWE-Bench Pro, mini-SWE-agent

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code and runs plan, critique and debate steps, and the talk shows Claude dropping sub-requirements and self-testing depends on prompt wording. → *Add a per-requirement checklist to the plan and critique step to catch dropped sub-requirements, and make the harness prompt's test instruction an explicit, tested setting.*
- **agentos** (1/3): Crucible runs opt-in sandboxed code execution, and the talk's verifier isolation and history scrubbing apply if AgentOS adds coding-agent evals. → *If AgentOS adds coding-agent evals under Crucible, run the grader in a separate runtime from the agent and strip git refs beyond the base commit.*
