# The HIDDEN Reason GPT‑5 Feels Underwhelming

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `RuBXRjqqxZ8` · [watch](https://youtu.be/RuBXRjqqxZ8) · **date:** 2025-11-02 · **length:** 4:51 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed Better Stack presenter · **orgs:** Better Stack, OpenAI, Anthropic, Vals AI
- **topics:** evals, models-research · **tags:** swe-bench, swe-bench-verified, aider-polyglot, livecodebench, gpt-5, benchmarks, model-router, leaderboards, mini-swe-agent

> Walks through SWE-bench, Aider Polyglot and LiveCodeBench to show GPT-5's coding scores are not like-for-like, then speculates that its real-time model router explains why it feels underwhelming.

## Summary
The presenter responds to claims that GPT-5 is a big coding upgrade and that some developers find it underwhelming. He goes through three coding benchmarks: SWE-bench (and the human-verified SWE-bench Verified subset), Aider Polyglot, and LiveCodeBench. For each, he points out that the headline numbers come from different task subsets, attempt policies, thinking modes, or agent setups, so direct comparison is unfair. He leans on the official SWE-bench bash-only leaderboard, where a same-scaffold run ranks Claude 4 Opus first, GPT-5 second and Claude 4 Sonnet third. He notes that the Aider Polyglot leaderboard had not yet been updated for GPT-5, and that OpenAI's 88% figure is unverified. For the underwhelming experience, he offers his own opinion: GPT-5 is a mixture of models behind a real-time router, which may send simple prompts to a simpler model that answers without the extra actions a stronger coding model takes. He closes by saying up-to-date leaderboards for older benchmarks such as HumanEval are hard to find.

## Key ideas
- **Benchmark numbers are not comparable unless the task subset, attempt policy, thinking mode and agent scaffold match.** — The presenter contrasts GPT-5 at about 75% on a fixed 477-task SWE-bench Verified subset (one try, with thinking) against Opus 4.1 at 74.5% on the full set, and calls that comparison unfair for those reasons. ([0:00](https://youtu.be/RuBXRjqqxZ8?t=0))
- **SWE-bench is built from real GitHub issues, and Verified is a human-checked subset.** — Full SWE-bench has over 2,200 real issues from popular open-source Python repositories (the speaker's repository count is garbled in the captions). SWE-bench Verified keeps 500 human-verified tasks to remove unclear issues. ([0:00](https://youtu.be/RuBXRjqqxZ8?t=0))
- **Use the official same-scaffold bash-only leaderboard for a fair model ranking.** — Under the mini-SWE-agent scaffold, Claude 4 Opus scores 67.6%, GPT-5 (medium reasoning) 65%, and Claude 4 Sonnet 64.93%. On the bash-only full set of 2,294 tasks the order is Opus, then GPT-5, then Sonnet. ([1:23](https://youtu.be/RuBXRjqqxZ8?t=83))
- **Aider Polyglot is a hard multi-language test, and the OpenAI claim is not yet independently verified.** — It uses 225 of Exercism's hardest problems across six languages. o3 scores near 85%, Claude 4 Opus with thinking 72%, and OpenAI claims 88% for GPT-5 with thinking at a two-attempt pass rate. The leaderboard maintainer had not yet added GPT-5, so the presenter waits for verification. ([1:23](https://youtu.be/RuBXRjqqxZ8?t=83))
- **LiveCodeBench reduces training contamination by filtering problems by date against the model's training cutoff.** — It collects problems continuously from LeetCode, AtCoder and Codeforces. Version 6 has over 1,000 problems in easy, medium and hard tiers, and measures code generation, self-repair and test-output prediction separately. ([2:36](https://youtu.be/RuBXRjqqxZ8?t=156))
- **The underwhelming experience may come from GPT-5's router, not from the model itself (speaker's opinion).** — GPT-5 is a mixture of models with a real-time router that analyses each prompt and picks a model. A powerful coding model may over-deliver on a simple task by doing extra work, while the router sends the same simple prompt to a lighter model that just answers. The presenter says this is only his opinion. ([2:36](https://youtu.be/RuBXRjqqxZ8?t=156))
- **The router may also explain GPT-5's low price, and the router can be improved.** — The presenter links the cheaper pricing to routing simpler prompts to smaller models, and says OpenAI is still working on the router so answers are good for every prompt type. ([4:00](https://youtu.be/RuBXRjqqxZ8?t=240))
- **Up-to-date leaderboards for older benchmarks such as HumanEval and basic programming problems are hard to find.** — He mentions them briefly as other coding benchmarks and says a current leaderboard with the popular models is difficult to find, so he does not cover them. ([4:00](https://youtu.be/RuBXRjqqxZ8?t=240))

## Techniques
- **Same-scaffold model comparison** — Compare models on SWE-bench only from runs using the same agent scaffold (here mini-SWE-agent, bash-only) and the full task set. Do not compare a vendor's self-reported subset score with a leaderboard score from a different agent. *When:* Choosing a coding model for an agent or harness, or checking a vendor's benchmark claim.
- **Check the eval metadata before trusting a number** — Record the task count (for example 477 of 500 Verified, or 2,294 bash-only), the attempt policy (one try vs two attempts), whether thinking is on, the agent scaffold and the tools available. Only compare scores that share all of these. *When:* Reading any benchmark table, including your own internal evals.
- **Contamination-aware problem selection** — Filter the eval problems by publication date so they fall after the model's training cutoff, as LiveCodeBench does. Score the results separately for code generation, self-repair and test-output prediction. *When:* Building or choosing an eval for coding models where training-data leakage is a concern.
- **Probe routed systems with simple prompts** — When a provider uses a router that picks the underlying model per prompt, send simple and complex prompts and check whether simple ones get a bare answer and complex ones get more work. The presenter suggests this as a reason for the mismatch but did not measure it. *When:* Evaluating an auto-routing model against a fixed model you already rely on.

## Numbers
- SWE-bench full set has over 2,200 real GitHub issues ([0:00](https://youtu.be/RuBXRjqqxZ8?t=0))
- SWE-bench Verified has 500 human-verified tasks; GPT-5 (thinking, one try) scores almost 75% on a fixed 477-task subset ([0:00](https://youtu.be/RuBXRjqqxZ8?t=0))
- Claude Opus 4.1 scores 74.5% on the full set (speaker says this is not a fair comparison) ([0:00](https://youtu.be/RuBXRjqqxZ8?t=0))
- Official SWE leaderboard, mini-SWE-agent: Claude 4 Opus 67.6%, GPT-5 medium reasoning 65%, Claude 4 Sonnet 64.93% ([1:23](https://youtu.be/RuBXRjqqxZ8?t=83))
- Bash-only SWE-bench run covers the full 2,294 tasks ([1:23](https://youtu.be/RuBXRjqqxZ8?t=83))
- Aider Polyglot: 225 questions across six languages; o3 scores almost 85% ([1:23](https://youtu.be/RuBXRjqqxZ8?t=83))
- Claude 4 Opus with thinking scores 72% on Aider Polyglot, higher than without thinking ([1:23](https://youtu.be/RuBXRjqqxZ8?t=83))
- OpenAI claims GPT-5 with thinking scores 88% on Aider Polyglot at a two-attempt pass rate (unverified at time of video) ([1:23](https://youtu.be/RuBXRjqqxZ8?t=83))
- LiveCodeBench version 6 has over 1,000 coding problems, tiered easy, medium and hard ([2:36](https://youtu.be/RuBXRjqqxZ8?t=156))
- Vals AI ranks GPT-5 mini top for performance and speed, above GPT-5 and Claude 4 Opus (speaker's reading of that leaderboard) ([2:36](https://youtu.be/RuBXRjqqxZ8?t=156))

## Hot takes
- The router explanation for the underwhelming experience is the presenter's own opinion (he says so); no source is cited for it.
- The presenter calls OpenAI's 88% Aider Polyglot claim believable but says it should wait for independent verification.
- The title promises a hidden reason, but the substance is one speculative paragraph; the rest is leaderboard reading. Quality is capped at 2 for hype title and thin substance.
- The presenter cites Opus 4.1 at 74.5% and GPT-5 at about 75% in the same breath, then calls that comparison unfair. The headline benchmark numbers are presented as not comparable.
- Auto-caption errors were fixed (SWE-bench, Exercism, LiveCodeBench, Vals AI, o3/o4); the repository count in the SWE-bench description is garbled in the source and is not used.

## Tools mentioned
SWE-bench, SWE-bench Verified, mini-SWE-agent, Aider Polyglot, LiveCodeBench, GPT-5, GPT-5 mini, o3, o3 Pro, o4, Claude 4 Opus, Claude 4 Sonnet, Claude Opus 4.1, HumanEval, Vals AI leaderboard

## Relevance to our work
- **agentos** (1/3): AgentOS has strategy routing in its Govrix proxy and aims to prove claims with evals. The video is a warning about per-prompt routing and about benchmark comparability. → *Before comparing models for AgentOS routing or InferCraft, check the eval metadata (task subset, attempt policy, thinking, scaffold). For any router, test simple prompts against a fixed model to see whether it under-delivers.*
- **prosharness** (1/3): ProsHarness uses plan, critique and debate across models. Choosing which model fills each role is a benchmark question, and the video shows how misleading mixed-scaffold numbers can be. → *When choosing models for the plan, critique (Codex) or debate roles, compare on the same bash-only or same-scaffold subset, not vendor-reported numbers.*
