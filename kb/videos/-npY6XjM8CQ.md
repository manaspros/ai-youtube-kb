# When Will The Benchmaxxing Plague End? — Nick Heiner, Surge AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `-npY6XjM8CQ` · [watch](https://youtu.be/-npY6XjM8CQ) · **date:** 2026-08-18 · **length:** 17:25 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Nick Heiner · **orgs:** Surge AI
- **topics:** evals, models-research · **tags:** benchmarks, benchmaxxing, contamination, reward-hacking, verifiers, lm-arena, human-eval, holdout-sets, llm-as-judge, swe-bench, ifeval

> Nick Heiner (Surge AI) on why benchmarks drift from real value (cost, contamination, reward hacking, bad verifiers, leaderboard gaming) and how to build better ones.

## Summary
Heiner argues that benchmarks often diverge from real-world value because of incentives and poor methodology, and that the industry's reliance on popular but weak benchmarks (LM Arena, SWE-bench Verified, IFEval, Apex, Automation Bench) feeds a popularity loop. He lists anti-patterns: high build cost that pushes teams toward cheap or AI-assisted task creation, contamination through memorized public Q&A, reward hacking by lazy optimizers, and verifiers that reject valid answers (hard-coded string matches, contradictory or impossible prompts, Unicode look-alike tricks). He describes benchmaxxing from the lab side, including hill-climbing while human eval stays flat, crowd voting on LM Arena via watermarks, and undisclosed testing of many models. His recipe for a good benchmark is expert humans with product sense, real input data, working tools, two-way alignment between prompts and verifiers, thorough QC, and a private holdout set. He also says saturation can hide broken tasks, which adds noise to rankings, and presents Surge's Hemingway-Bench, which uses blind comparisons by professional writers instead of an LLM judge. The talk is partly a hiring pitch, but it has concrete, checkable failure cases.

## Key ideas
- **Benchmarks become a popularity feedback loop** — Because everyone needs a way to pick models but few can judge whether a benchmark is good, people judge by popularity. That shifts the conversation toward incumbency and marketing rather than real-world value. ([2:17](https://youtu.be/-npY6XjM8CQ?t=137))
- **Building a good benchmark is expensive, so teams cut corners** — Speaker's estimate: 1,000 coding tasks at 60 hours each with $500k/yr engineers is about $15M, and roughly a third of tasks go stale each year as models improve. Workarounds like AI-written tasks or cheap labor produce weak results. Quality needs paid expert humans. ([3:20](https://youtu.be/-npY6XjM8CQ?t=200))
- **Contamination is the default unless you work hard against it** — Public questions and answers get memorized. Given the first part of an SWE-bench Verified prompt, a model reproduced the rest verbatim, and the speaker's team found memorization above the rest of the source repos. The model card did not disclose this. ([4:49](https://youtu.be/-npY6XjM8CQ?t=289))
- **Design verifiers against a maximally lazy optimizer** — Reward hacking is meeting the letter but not the spirit of a task. Gradient descent follows the path of least resistance, so verifiers must hold up against that pressure. ([5:48](https://youtu.be/-npY6XjM8CQ?t=348))
- **Verifiers that reject valid answers make benchmarks useless** — Hard-coded string matches fail when many formats are acceptable, such as phone numbers. In Automation Bench, Haiku and Fable both score 20%, but for different reasons (one makes mistakes, the other picks a different valid format), so the task does not separate them. IFEval has contradictory or unsolvable prompts and a weak sentence splitter, and a response could pass by using a Cyrillic I instead of an ASCII I. ([7:18](https://youtu.be/-npY6XjM8CQ?t=438))
- **Hill-climbing can diverge from human preference, and arenas can be gamed** — A benchmark can keep rising while human eval stays flat or falls. Leaderboards with little voter filtering can be manipulated with watermarks that tell a crowd which anonymized model to vote for. Undisclosed testing of many variants (the talk cites Meta testing 27 models) distorts results. ([11:20](https://youtu.be/-npY6XjM8CQ?t=680))
- **Benchmark quality needs experts, real data, working tools, two-way verifier alignment, and a holdout** — Experts with product sense decide the task types and success criteria. Input data should come from the real world. Every prompt requirement needs a verifier, and every verifier check needs a prompt requirement. Keep a private holdout set. Saturation at about 80% can mean 20% of tasks are broken, and those broken tasks bias the ranking. ([13:56](https://youtu.be/-npY6XjM8CQ?t=836))
- **Subjective quality needs blind expert comparisons, not mechanical metrics or an LLM judge** — For writing, Surge built Hemingway-Bench with thousands of professional writers doing blind pairwise model comparisons. The speaker argues LLM judges lack good taste, so they cannot expand the frontier from within it. ([14:55](https://youtu.be/-npY6XjM8CQ?t=895))

## Techniques
- **Two-way verifier-prompt alignment audit** — Check that every requirement in the prompt is covered by a verifier, and that every verifier check corresponds to something the prompt asks for. Fix either gap before trusting scores. *When:* Whenever you write or review an eval task, especially tool-call or instruction-following tasks.
- **Accept all valid answer formats in verifiers** — Normalize or allow multiple equivalent forms (phone formats, date formats) instead of one hard-coded string match. Otherwise correct models get penalized. *When:* When graders compare strings for entities that have many valid surface forms.
- **Adversarial check of graders against lazy solutions** — Probe a grader with cheap exploits, such as look-alike Unicode characters or outputs that satisfy a count check without doing the task, and confirm they fail. *When:* Before using any automated grader, and especially any grader used as a training reward.
- **Contamination probe by prefix completion** — Give the model the first part of a benchmark item and check whether it reproduces the hidden remainder, including the reference answer, verbatim. Compare against matched non-benchmark text from the same source. *When:* Before trusting public benchmark scores, or when building a benchmark from public repos or Q&A.
- **Private holdout plus disclosure of test conditions** — Keep a private test split that is never published. Report the number of variants tested and the eval conditions. *When:* When you publish or rely on leaderboard-style results.
- **Watch for benchmark-vs-human-eval divergence** — Track a benchmark alongside a human rating set. A flat or falling human score while the benchmark rises is a sign of overfitting. *When:* During iterative model or prompt tuning against a proxy metric.
- **Blind pairwise expert comparison for subjective quality** — Have domain experts compare anonymized outputs side by side and build a leaderboard from the results. Use it where mechanical metrics and LLM judges are not trusted. *When:* For writing, taste, or other quality dimensions that do not reduce to a string or a rubric.
- **Saturation check for broken tasks** — When a benchmark plateaus, audit the failing tasks for broken verifiers or impossible prompts before concluding the model is at its limit. *When:* When a benchmark score stops moving, or near a high ceiling.

## Numbers
- Benchmark build cost: 1,000 tasks x 60 hours each at $500k/yr per engineer is about $15M ([3:20](https://youtu.be/-npY6XjM8CQ?t=200))
- Yearly replacement cost is about $5M, assuming a third of tasks become obsolete each year ([3:20](https://youtu.be/-npY6XjM8CQ?t=200))
- Automation Bench: Haiku and Fable both score 20%; Fable is said to be correct 80% of the time but picks a different valid format from the grader ([7:18](https://youtu.be/-npY6XjM8CQ?t=438))
- Meta tested 27 models without disclosing it, which the speaker says distorted LM Arena results ([12:52](https://youtu.be/-npY6XjM8CQ?t=772))
- Saturation near 80% can hide roughly 20% of tasks being broken ([14:55](https://youtu.be/-npY6XjM8CQ?t=895))

## Hot takes
- LM Arena may be doing more harm than good and should consider that question seriously
- Contamination is the default outcome for public benchmarks unless the builder works very hard against it
- LLM-as-a-judge does not work for writing quality because LLMs lack good taste
- Labs are not in the habit of disclosing benchmark contamination in model cards
- Most current benchmarks are not built with product sense, so they measure the wrong things

## Tools mentioned
LM Arena, SWE-bench Verified, IFEval, Apex, Automation Bench, Hemingway-Bench

## Relevance to our work
- **general** (2/3): The verifier-alignment audit, contamination probe, and holdout discipline apply to any model choice or agent evaluation the team runs. → *Before choosing a model from a public leaderboard, run the candidate models on a small private task set with two-way verifier checks and a holdout.*
- **agentos** (1/3): AgentOS plans evals (RAGAS, load tests) and an agent stack. The talk's verifier and contamination lessons apply to those evals, but nothing is specific to its architecture. → *When writing AgentOS eval cases, check each grader for hard-coded string matches and run a prefix-completion contamination probe on any public-derived test set.*
- **prosharness** (1/3): ProsHarness runs checks around Claude Code, so the verifier-alignment and adversarial-grader points could apply to its completion checks. → *Audit ProsHarness completion and checkpoint verifiers for strict string matching and for any path a lazy agent could use to pass without doing the work.*
