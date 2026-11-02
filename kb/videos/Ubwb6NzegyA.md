# Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Ubwb6NzegyA` · [watch](https://youtu.be/Ubwb6NzegyA) · **date:** 2026-06-18 · **length:** 20:03 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Nicholas Kang, Michael Aaron · **orgs:** Google DeepMind, Kaggle
- **topics:** evals, testing-verification, models-research · **tags:** kaggle, game-arena, agent-exams, community-benchmarks, pvp-evals, bradley-terry, harness-variance, benchmark-saturation, eval-transparency, hackathons, openspiel

> Google DeepMind and Kaggle staff tour their open eval platforms (hackathons, agent exams, Game Arena, community benchmarks) and the problems they hit: saturation, cost, harness variance, and hidden configs.

## Summary
Nicholas Kang and Michael Aaron from Google DeepMind (Kaggle) argue that AI evals are scattered, go stale quickly, and are often not transparent or reproducible. They cite a case where a rival lab reran a published benchmark with API-side compaction and got much higher scores, which shows that configuration can change results. They present Kaggle's open efforts: hackathons for crowd-built benchmarks, one-line "agent exams" that score an agent against a leaderboard, Game Arena (PvP games with Bradley-Terry ratings), and a community benchmarks platform built from assertions and LLM judges. The Game Arena section covers how games are chosen and checked against random play, how the Kaggle simulation platform and an LLM proxy run the games, and why poker needed about 400,000 hands for significance. The closing section argues that the agent harness can move coding-benchmark scores as much as the model does, citing a third-party post they had not verified. The talk is mostly a product overview, with the cost, harness and config points as the useful parts.

## Key ideas
- **Evals are scattered, decentralized, and go stale fast.** — Speaker says 10+ new benchmarks appear daily, and leaderboards in papers stop being maintained once the authors move on. Finding what matters means reading papers by hand. ([2:05](https://youtu.be/Ubwb6NzegyA?t=125))
- **Published eval numbers are often not reproducible because the configuration is hidden.** — Model settings and how the benchmark is orchestrated are rarely disclosed. An anecdote: a rival lab reran a Kaggle-published benchmark using API-side compaction and got much higher scores, while Kaggle ran all models without it. ([3:16](https://youtu.be/Ubwb6NzegyA?t=196))
- **Very few people build evals, so model capability is jagged.** — Speaker contrasts a small number of AI researchers with a much larger pool of engineers and data scientists. Anything not benchmarked cannot be hill-climbed, which leads to uneven model skill. He argues for open, community-built evals. ([3:16](https://youtu.be/Ubwb6NzegyA?t=196))
- **Domain experts hold benchmark data that labs will not build.** — A wastewater plant engineer in Turkey built a private benchmark from 20 years of experience about safety protocols. Speaker says this data would never be produced by labs because it is not economically productive for them. ([4:39](https://youtu.be/Ubwb6NzegyA?t=279))
- **Hackathons are used to crowdsource benchmark creation, but they need tooling and human judging.** — DeepMind is running a hackathon on five of the ten cognitive faculties from a recent paper. Challenges include giving participants compute and API access, writing up results, and judging creativity, which speaker says still needs human experts who may not agree. ([7:03](https://youtu.be/Ubwb6NzegyA?t=423))
- **Game Arena uses PvP games to avoid benchmark saturation.** — Models play each other, so there is always a winner and loser and the ELO-style rating never runs out of headroom. Games were picked to test different skills: Werewolf for deception, poker for randomness and risk, chess as a classic. ([12:19](https://youtu.be/Ubwb6NzegyA?t=739))
- **Poker needed about 400,000 hands for significance, so run cost is the main limit.** — Speaker says the statistics needed huge run counts. He asks for ways to reach significance with fewer games. Bradley-Terry pairwise scheduling is used to reduce the number of matches. ([14:37](https://youtu.be/Ubwb6NzegyA?t=877))
- **The agent harness can change coding-benchmark results more than the model does.** — Speaker cites a third-party post, which he has not checked, saying frontier models on SWE-Bench Pro land within a few points of each other, while the harness changed scores by about 22%. He says it is hard to know whether a test measures the harness or the model. ([18:22](https://youtu.be/Ubwb6NzegyA?t=1102))

## Techniques
- **PvP game benchmark with pairwise rating** — Choose games that test one capability each. Check that models can play at all, and that they beat random play. Tune prompts so they are fair. Run games through a shared LLM proxy on a simulation platform (OpenSpiel-based). Rate models with Bradley-Terry pairwise scheduling, and publish conversation logs as a dataset. *When:* When static benchmarks saturate and you need a rating that stays open to improvement over time.
- **Task-of-assertions plus LLM-judge benchmark structure** — Write each task as a set of deterministic assertions (for example, the output has the right text, or the file parses) plus LLM-judge checks. Group tasks into a benchmark, run it across a chosen model set, and compare results side by side. Example: an SVG-reproduction task. *When:* When you want a shareable, community-built eval that is closer to production eval style but open.
- **One-line agent exam** — Give the user a single prompt to paste into their agent. The agent runs the exam and a score is posted to a leaderboard. Tune difficulty so the exam is hard enough to give signal but short enough that agents finish. *When:* For a fast baseline of consumer or personal agents before they are deployed.
- **Lock down the harness and config when comparing models** — Run every model with identical settings. Do not allow model-side features such as API compaction to differ across runs. Report the harness and config alongside the score. *When:* Any time you publish or compare agent or model eval numbers.

## Numbers
- 10+ new AI benchmarks released per day (speaker's estimate) ([2:05](https://youtu.be/Ubwb6NzegyA?t=125))
- Kaggle community of 30+ million users ([0:56](https://youtu.be/Ubwb6NzegyA?t=56))
- Roughly 30,000 AI researchers versus about 30 million software engineers and data scientists (speaker's rough figure from a search) ([3:16](https://youtu.be/Ubwb6NzegyA?t=196))
- About 400,000 poker hands needed for statistical significance in Game Arena ([14:37](https://youtu.be/Ubwb6NzegyA?t=877))
- Over 500 agents evaluated on the agent exam within about a week of launch, without much promotion ([11:02](https://youtu.be/Ubwb6NzegyA?t=662))
- Harness choice changes SWE-Bench Pro scores by about 22%, per a third-party post the speaker has not verified ([18:22](https://youtu.be/Ubwb6NzegyA?t=1102))
- Six frontier models within a couple of percentage points of each other on SWE-Bench Pro, per the same third-party post (unverified) ([18:22](https://youtu.be/Ubwb6NzegyA?t=1102))
- Hackathon covers 5 of the 10 cognitive faculties from the DeepMind paper ([7:03](https://youtu.be/Ubwb6NzegyA?t=423))

## Hot takes
- Published model benchmark numbers may not reflect the model. Config choices such as API-side compaction can move scores a lot, as the rival-lab rerun showed.
- Agent benchmark results often measure the harness as much as the model, so comparisons between models need the harness held fixed.
- Saturation-proof ratings come from PvP games, since one model always has to win and lose.
- Consumer agents are being sent out without any testing, so a short standard exam should be a baseline before they run tasks like email or purchases.

## Tools mentioned
Kaggle Benchmarks, Kaggle Game Arena, OpenSpiel, Kaggle simulation platform, LLM model proxy (also available on Colab), Bradley-Terry pairwise rating, Moltbook (transcribed as Motebook), SWE-Bench Pro (cited)

## Relevance to our work
- **prosharness** (2/3): The talk's main warning is that harness choice can change agent results more than the model. ProsHarness wraps Claude Code, so any ProsHarness eval has to control for that wrapper. → *Run the same task set through bare Claude Code and through ProsHarness, and report the harness as a separate variable before claiming gains from checkpoints or plan-critique loops.*
- **agentos** (1/3): Speaker's point that config (for example, API compaction) and harness choices can shift eval numbers applies to any AgentOS eval claims, such as RAGAS or benchmark runs. → *When publishing AgentOS eval numbers, record the exact proxy and harness config and run every compared model under the same settings.*
- **agentos** (1/3): Pairwise Bradley-Terry scheduling is a way to rank models with fewer matches, which may help when comparing many routing or model options. → *Read the Kaggle Game Arena scheduling approach before adding a pairwise ranking step to AgentOS model-routing evals.*
- **general** (1/3): Haiku-based pipelines could use pairwise, Bradley-Terry-style ranking of outputs as a cheaper judging method than scoring each output alone. → *Try pairwise comparison with a cheap model on a small sample and check whether the ranking agrees with absolute scores.*
