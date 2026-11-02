# First Steps Toward Automated AI Research — Richard Socher, CEO Recursive AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `pWXUkLP9uWM` · [watch](https://youtu.be/pWXUkLP9uWM) · **date:** 2026-08-18 · **length:** 20:24 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Richard Socher · **orgs:** Recursive (Recursive AI), U.com, AIX Ventures
- **topics:** models-research, agent-architecture, evals · **tags:** automated-research, recursive-self-improvement, eureka-machine, nanochat, nanogpt-speedrun, cuda-kernels, reward-hacking, agent-swarm, popper, web-search-for-llms

> Richard Socher (Recursive AI) argues for automating scientific research via a "Eureka machine" and shows small auto-research wins on NanoChat, NanoGPT speedrun and CUDA kernels, while separating these from true recursive self-improvement.

## Summary
Socher frames automated science as the next step after evolution and past technology waves, arguing that human researchers are spread too thin across niche fields. He proposes a "Eureka machine" built from four pillars (existing knowledge, measurement data, simulations, and physical labs) run by an agent swarm. He says the core loop is ideation, implementation and validation, and that AI can now do this because coding agents can work over longer horizons, which only became viable in the last six to eight months. He presents three small auto-research demos: a NanoChat training run that improved bits-per-byte from 0.93 to 0.91, a NanoGPT speedrun that cut more than two seconds off a 70-second time, and CUDA kernels that beat the NVIDIA leaderboard. He stresses that these are auto-research, not true recursive self-improvement, which would require a system that updates its entire stack, including training, harnesses and itself. The talk ends with a claim that intelligence has many dimensions, so there is still far to go. Much of the talk is vision and company promotion, and the method details are thin.

## Key ideas
- **Automate scientific discovery with a 'Eureka machine' because human researchers cannot keep up with the growing number of niche fields** — Socher argues exponential science output will stall from a lack of people per subfield. His answer is a machine built on four pillars: a knowledge base of prior work, measurement data, simulations for things not yet measured, and physical labs as the last check. An agent swarm connects them. ([7:59](https://youtu.be/pWXUkLP9uWM?t=479))
- **Replacing manual steps with learned systems has been the pattern in AI, so AI should now help build AI** — He compares NLP history: linguists' features, then learned features, then architecture engineering. Each time a hand-made step was replaced by a learned one, gains followed. He says recursive self-improvement is the next step, and it is possible now because AI can code over longer horizons. ([12:06](https://youtu.be/pWXUkLP9uWM?t=726))
- **Auto-research is not recursive self-improvement (RSI)** — He says true RSI means a system that knows its own weaknesses, has full access to its pre-training, RL, harnesses and everything else, and rewrites its whole stack for the next version. Asking an agent to improve a small training run is useful but is a weaker form. ([14:49](https://youtu.be/pWXUkLP9uWM?t=889))
- **The auto-research loop is ideation, implementation, then validation** — He says this loop holds across most scientific fields. In the demos, an agent proposes changes, implements them, and checks each change against a fixed benchmark metric. ([13:25](https://youtu.be/pWXUkLP9uWM?t=805))
- **Auto-research found real ideas on NanoChat, not just tuned hyperparameters** — On a five-minute training run, the system reached 0.91 bits-per-byte after a day or two, from 0.93 where the community had stalled. Its finds included hashed bigram and trigram embedding tables and learned gates mixed into the value paths. ([16:02](https://youtu.be/pWXUkLP9uWM?t=962))
- **Auto-research beat a year of human-plus-AI effort on NanoGPT speedrun and found CUDA kernels better than the NVIDIA leaderboard** — The speedrun cut more than two seconds from a 70-second benchmark. For CUDA kernels, the team had no kernel specialists, and after a couple of days the system beat the leaderboard by a clear margin in every category. The team checked with NVIDIA for reward hacks before accepting the results. ([17:25](https://youtu.be/pWXUkLP9uWM?t=1045))

## Techniques
- **Benchmark-gated auto-research loop** — Give an agent a training or kernel codebase and one fixed metric (bits-per-byte, wall-clock time, kernel latency). Have it propose ideas, implement them, run a short timed test, and keep only the changes that improve the metric. Repeat. *When:* Any task where a single number can score each attempt and a run is cheap enough to repeat many times.
- **Short fixed-budget runs as the test** — Use a small, fixed-time training run (for example five minutes) as the scoring function, so every idea is compared under the same budget. *When:* When you need many quick comparisons of ideas and cannot afford full-scale runs for each one.
- **Reward-hack audit before trusting results** — Before accepting an agent's improvement, have a domain owner (here, the hardware vendor) check that it is a real gain and not an exploit of the benchmark. *When:* Whenever the score comes from a public or shared benchmark or leaderboard that the agent can game.
- **Simulation as the verifier** — For things you cannot measure yet, build a simulator and verify candidate ideas in it. Keep physical experiments as the last step. *When:* Scientific or engineering domains where simulation is cheaper than real experiments, but where real checks remain necessary.

## Numbers
- NanoChat bits-per-byte improved from 0.93 (community best) to 0.91 after a day or two of auto-research on a five-minute training run ([16:02](https://youtu.be/pWXUkLP9uWM?t=962))
- NanoGPT speedrun: auto-research beat a year-plus of human and AI effort and cut more than two seconds off a 70-second benchmark ([16:02](https://youtu.be/pWXUkLP9uWM?t=962))
- CUDA kernel search found kernels better than the NVIDIA benchmark leaderboard, by a sizable margin in all categories, after a couple of days ([17:25](https://youtu.be/pWXUkLP9uWM?t=1045))
- Speaker says large MoE clusters costing billions of dollars often run at around 30% utilization ([17:25](https://youtu.be/pWXUkLP9uWM?t=1045))
- Long-horizon coding ability for agents only became usable in the last six to eight months ([12:06](https://youtu.be/pWXUkLP9uWM?t=726))
- Speaker estimates an AI shift on the scale of flight (Wright brothers to the Moon in one lifetime) in about 30 to 60 years ([5:23](https://youtu.be/pWXUkLP9uWM?t=323))

## Hot takes
- We should fire all the AI engineers and have them manage an AI that does AI research.
- Most current auto-research is not recursive self-improvement; true RSI rewrites the whole system, including its own harness and training.
- Science will stall because too few people work on each niche field, so automating discovery is the only way forward.
- Intelligence has many dimensions, and we are still astronomically far from the upper bounds on each.

## Tools mentioned
NanoChat, NanoGPT speedrun, NVIDIA CUDA kernels, U.com web search for LMs

## Relevance to our work
- **agentos** (1/3): The benchmark-gated loop could help tune InferCraft serving settings (KV-cache strategy, speculative decoding), but the talk gives no method for it and is mostly about vision. → *Prototype a small benchmark-gated loop that tries InferCraft settings on the single RTX 5090 and keeps only changes that beat a fixed latency or throughput target, with a manual check for reward hacks.*
- **prosharness** (1/3): The keep-only-if-metric-improves step fits ProsHarness's checkpoint and loop design, but the talk offers no harness-level details. → *Consider adding a metric-gated accept or reject step to ProsHarness's long-run loops, so a run keeps a change only when a fixed check improves.*
- **general** (1/3): Useful as a framing for autonomous experiment loops, and it makes the auto-research versus RSI distinction clearly. → *Read the talk's distinction between auto-research and RSI before writing any claim that an agent improves itself.*
