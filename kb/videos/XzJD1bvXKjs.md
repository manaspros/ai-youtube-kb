# How long can your skills be before your agent forgets what you told it? — Laurie Voss, Arize AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `XzJD1bvXKjs` · [watch](https://youtu.be/XzJD1bvXKjs) · **date:** 2026-09-18 · **length:** 22:26 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Laurie Voss · **orgs:** Arize AI, Chroma, IFScale paper authors
- **topics:** context-engineering, evals, skills-self-improvement, models-research · **tags:** skills files, instruction following, IFScale, instruction density, frontier model benchmarks, failure modes, silent partial failure, LLM-as-judge, prompt length, cost and latency

> Laurie Voss re-runs the 200-instruction IFScale benchmark on 2026 frontier models and finds the ceiling moved about 10x, to roughly 2,000 to 5,000 rules, but reliability and verification remain open problems.

## Summary
Laurie Voss (Arize AI) checks a widely repeated claim that agents forget instructions after about 200. The claim comes from the IFScale benchmark, where the model must include a list of named keywords in a generated business report. He replicates the 2025 result, then finds that current frontier models hold about 2,000 rules before accuracy drops, and the best reach about 5,000. The benchmark had to be scaled to a 10,000-word vocabulary before the new ceiling appeared. The four models he tested each fail in a different way: DeepSeek forgets quietly, Claude refuses on its safety classifier, Gemini spends its token budget on thinking, and GPT-5.5 stops halfway through the report. His practical advice is that long skill files are now viable, so the main cost is price and latency. The harder remaining problem is verifying that the model did what was asked, which he argues requires evals run on every output. He also cites newer work showing that rewording or reordering instructions can change results, and that reasoning over conflicting instructions is not guaranteed.

## Key ideas
- **The 200-instruction ceiling is a real published result, but it is about a year old and no longer holds.** — The figure comes from the IFScale benchmark (2025 paper). The speaker says it was stated as an aside and that the 2025 figure was not updated. He treats it as the starting point for re-testing. ([0:08](https://youtu.be/XzJD1bvXKjs?t=8))
- **IFScale measures instruction density with a simple keyword test.** — The model writes a business report that must include N named words exactly. Two numbers matter: N (density) and the fraction of words used (accuracy). He argues that keywords are a proxy for real named constraints such as a required section or a banned phrase, so the result is a ceiling for real instructions. ([3:10](https://youtu.be/XzJD1bvXKjs?t=190))
- **Frontier models moved the ceiling by roughly 10x in about a year, so the benchmark had to be scaled up.** — The original 500-word vocabulary was saturated: the models scored 100%. He doubled the vocabulary step by step to 10,000. Curves now bend near 2,000 rules, and the best model holds up to about 5,000. Replication of the original paper's curves matched within noise. ([6:40](https://youtu.be/XzJD1bvXKjs?t=400))
- **Models now fail in four distinct ways, so a silent failure needs model-specific detection.** — DeepSeek V4 Pro forgets rules silently, starting near 750 and dropping nearly half by 2,000. Claude Opus 4.7 refuses at the API level because its safety classifier is triggered by random word combinations. Gemini 3.1 Pro stays accurate to 5,000 but can spend its whole budget on thinking and return little output. GPT-5.5 is about 99% accurate to 5,000 and then writes part of the report before stopping and saying the task is pointless. ([8:54](https://youtu.be/XzJD1bvXKjs?t=534))
- **The new hard problem is verification, not fitting instructions into the prompt.** — In his conclusion, the compression problem (fitting rules into the context) is solved. Whether the model actually did what was asked is now the open question. He argues it can only be answered by checking each output, which is an eval. A polished partial answer is more dangerous than a loud refusal because it looks finished. ([20:25](https://youtu.be/XzJD1bvXKjs?t=1225))
- **Capacity to track instructions does not mean the model reasons well over them.** — He cites a Chroma study across 18 models in which accuracy on long inputs fell 30 to 50 percent well before the context window was full. Another 46-model paper found that rewording or reordering the same instructions can change results a lot. Conflicting rules are not reliably resolved. ([16:52](https://youtu.be/XzJD1bvXKjs?t=1012))

## Techniques
- **Instruction density probe** — Give the target model a generated task that must include N named keywords (or rules) exactly. Count hits at increasing N on a log scale and find the knee where accuracy falls. Scale the vocabulary up if the model scores 100% at the top of the range. *When:* Before deciding how long a skill file or system prompt can be for a specific model, and again every few months as models change.
- **Model-specific failure profiling** — Classify each failed run as silent forgetting, API refusal, output consumed by thinking tokens, or a partial answer that stops midway. Check each failure type separately, because the output looks different for each. *When:* When choosing a model for long-instruction workflows, or when a long prompt fails without an error.
- **Pre-screening test vocabulary for safety filters** — Run random benchmark words through a separate safety filter and remove any that trigger refusals. This keeps the test measuring instruction following instead of safety classification. *When:* When building synthetic instruction-following tests with random or unusual vocabulary and seeing refusals that are not about the task.
- **Per-output eval of long rule sets** — After each run, check the output against each named rule with an LLM judge or a deterministic check, and flag any rule that was dropped. Do not rely on the output reading as complete. *When:* In production with long skill files or style guides, where partial compliance is hard to spot by reading.
- **Robustness check by rewording and reordering** — Run the same instruction set with different phrasing and different order, and compare results. Treat large differences as a reliability problem even when the model passes the base test. *When:* Before trusting a long prompt whose instructions may interact or conflict.

## Numbers
- Original IFScale result: frontier models began to fall off around 200 to 300 rules (2025). ([0:08](https://youtu.be/XzJD1bvXKjs?t=8))
- Only 3 of the original 10 models were still available by API when re-tested; one was retired within a couple of weeks of publication. ([4:21](https://youtu.be/XzJD1bvXKjs?t=261))
- Replicated original curves matched the paper within noise; by 500 rules, models lost 30 to 50 percent of the instructions. ([5:22](https://youtu.be/XzJD1bvXKjs?t=322))
- Vocabulary scaled from 500 to 1,000, 2,000, 5,000, and 10,000 words before the new ceiling appeared. ([6:40](https://youtu.be/XzJD1bvXKjs?t=400))
- New frontier ceiling is about 2,000 rules for most models and up to about 5,000 for the best, roughly 10x in 12 months. ([7:48](https://youtu.be/XzJD1bvXKjs?t=468))
- DeepSeek V4 Pro starts forgetting around 750 rules and drops nearly half by 2,000. ([8:54](https://youtu.be/XzJD1bvXKjs?t=534))
- GPT-5.5 reaches about 99% accuracy up to 5,000 rules before it stops partway through the report. ([12:22](https://youtu.be/XzJD1bvXKjs?t=742))
- Model walls range from about 750 to 9,000+ rules depending on the model. ([15:30](https://youtu.be/XzJD1bvXKjs?t=930))
- Chroma study across 18 models: accuracy on long inputs fell 30 to 50 percent before the context window limit. ([16:52](https://youtu.be/XzJD1bvXKjs?t=1012))
- Whole study cost $209 for about 2,300 calls across seven models. ([17:58](https://youtu.be/XzJD1bvXKjs?t=1078))

## Hot takes
- The old advice to keep skill files under 200 instructions and shard them across subagents is now outdated; long single files are viable.
- Partial, polished answers that quietly stop midway are more dangerous than loud refusals, so every long-prompt output needs checking.
- Within a year the question moved from can the model do this to is it worth the cost and latency.

## Tools mentioned
IFScale benchmark, Arize AI (speaker's employer; no product detail given), Chroma context rot study, Firebench, CCRbench, Guidebench (names as captioned; may be misspelled)

## Relevance to our work
- **prosharness** (2/3): ProsHarness runs Claude Code with skill and instruction files. Silent partial compliance on long skills would make checkpoint or plan results look complete when they are not. → *Add a rule-by-rule compliance check to ProsHarness runs that use long CLAUDE.md or skill files, and flag any dropped rule in the checkpoint record.*
- **general** (2/3): Context engineering is a recurring interest. The talk gives a method for measuring how many instructions a specific model can hold, and a warning about silent failures. → *Run a small density probe on the model used for Haiku pipelines before writing very long prompts, and re-run it when the model changes.*
- **agentos** (1/3): SkillForge mines telemetry into reusable skills, and a skill's rules can be silently partially followed. A density probe is cheap to add to the skill-worthiness or verification step. → *In SkillForge, before publishing a mined skill, run each of its named rules through a per-output check and record the rule-drop rate on the target model.*
