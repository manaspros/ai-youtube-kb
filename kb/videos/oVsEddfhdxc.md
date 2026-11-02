# We Let Claude Code and Codex Race Human Researchers — Elie Bakouch, Prime Intellect

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `oVsEddfhdxc` · [watch](https://youtu.be/oVsEddfhdxc) · **date:** 2026-09-27 · **length:** 19:39 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Elie Bakouch · **orgs:** Prime Intellect, Google
- **topics:** coding-agents, claude-code, models-research, evals · **tags:** automated-ai-research, speedrun, nanogpt, optimizer, recursive-self-improvement, claude-code-vs-codex, slurm, scratchpad-memory, token-usage, subagents, compaction, alphaevolve-style-loop

> Prime Intellect's Elie Bakouch runs Claude Code and Codex on an optimizer speedrun against human records, finding both beat the records but neither produced a novel optimizer, and that Claude Code idled while Codex kept working.

## Summary
Elie Bakouch from Prime Intellect describes an experiment where Claude Code (Opus, extra-high effort) and Codex (GPT-5.5, extra-high effort) were let loose on a cluster to beat the community's optimizer speedrun, a modded-nanoGPT-style training-speed benchmark with a fixed validation-loss target. Both agents beat the best human record (about 2,990 steps) by small margins, Claude Code by roughly 50 to 60 steps and Codex by about 20, but the speaker stresses the results are preliminary and not yet released. The two agents behaved very differently: Claude Code stopped every 9 to 10 hours claiming it could not improve, so about a third of its time was idle, while Codex ran continuously, spawned more subagents, burned far more tokens and compacted more often. In a longer optimizer-only run of about five to six days, Codex, Kimi and Claude were all competitive, with Kimi showing a step-function breakthrough on day four and Claude consuming the most output tokens. The main negative finding is that no agent invented a novel optimizer; they combined existing papers and made small +1 tweaks. The speaker proposes a discovery loop inspired by AlphaEvolve, with generator models, a cheap speedrun as the reward, a judge that gives qualitative feedback, promotion of winners to larger scale, and humans steering. Prime Intellect is building GPU sandboxing, an RLM-style agent, and the Verifiers, Prime-RL and Hosted Training products.

## Key ideas
- **The speedrun is a good research benchmark because the reward is clear and verifiable.** — Beating the last record with a positive reward and failing with zero or negative reward gives a crisp signal. Runs take about 15 to 20 minutes, and a statistical threshold guards against seed luck before a record is accepted. ([4:01](https://youtu.be/oVsEddfhdxc?t=241))
- **Claude Code and Codex differ sharply in persistence, not only in raw score.** — Claude Code stopped every 9 to 10 hours saying it could not beat the record, so roughly a third of its time was idle until the speaker re-prompted it. Codex worked continuously and rarely asked questions. ([8:19](https://youtu.be/oVsEddfhdxc?t=499))
- **Agents can be compared on behavior, not just the final number.** — The speaker logged scratchpad writing (Codex wrote far more), subagent spawning (Codex spawned more), token burn and compaction counts, normalized by active hours. Tone also differed: Claude was enthusiastic, Codex was terse and robotic. ([8:19](https://youtu.be/oVsEddfhdxc?t=499))
- **Restarting the agent with fresh human records keeps it improving.** — The agents could fetch the latest human records at any restart. The speaker restarted the runs (v2, v3) and fed them current records, which let both agents move past the human frontier. ([10:59](https://youtu.be/oVsEddfhdxc?t=659))
- **Both agents beat the human record, but the gains were small.** — The best human record was about 2,990 steps. Claude beat it by roughly 50 to 60 steps and Codex by about 20. The speaker says the experiment lacks controls, so a proper benchmark needs multiple seeds and matched conditions. ([10:59](https://youtu.be/oVsEddfhdxc?t=659))
- **Models combined existing ideas rather than discovering new mechanisms.** — Across the six-day optimizer run, no agent produced a new optimizer. They merged papers and added incremental +1 changes. Claude found a paper no other model found, and it led to the best record. ([15:20](https://youtu.be/oVsEddfhdxc?t=920))
- **A proposed discovery loop pairs generators, a cheap reward, a judge and scaling.** — Inspired by AlphaEvolve, the loop has open and closed generator models proposing ideas, the speedrun scoring them, a judge giving qualitative feedback on taste, and winners promoted to larger parameter and token counts because many speedrun tricks fail at scale. Humans steer the loop. The speaker says this is not yet tested. ([15:20](https://youtu.be/oVsEddfhdxc?t=920))

## Techniques
- **Speedrun as a verifiable research environment** — Fix the data and the target loss, let the agent change only what the rules allow, reward a beaten record and check it against seed variance before accepting it. *When:* Evaluating or training an agent on research tasks where success must be checked automatically.
- **Constrained variants to force novelty** — Restrict the search to one component (for example, only the optimizer) so the agent must find improvements in that space instead of rewriting the whole program. *When:* Trying to push agents toward discovery rather than generic optimization.
- **Goal file plus rules file as the agent's contract** — Write a goal.md with the objective and an AGENTS.md with the rules. Let the agent submit jobs itself (sbatch on Slurm, with preemptible permission on shared nodes) and read the training logs to decide whether it has a record. *When:* Running long autonomous experiments on a shared compute cluster.
- **Restart with the latest best state** — When an agent stalls, stop it, fetch the current best records, and restart it so it works from the new frontier. The speaker did this one or two days before a release. *When:* Long unattended runs where the agent stalls or is overtaken by outside progress.
- **Behavior logs normalized by active time** — Log scratchpad writes, subagent spawns, token use and compactions, and divide by active hours before comparing agents, so differences in behavior are not confused with differences in runtime. *When:* Comparing coding agents or detecting stalled or idle agent behavior.
- **Generator, judge and scale-up loop** — Use several generator models to propose ideas, score each with a cheap speedrun, have a judge give qualitative feedback, promote the best to larger scale, and keep a human in the loop to steer. *When:* Searching for real algorithmic discoveries instead of evaluating known methods.

## Numbers
- Target training time for GPT-2-level validation loss went from 90 minutes to 45 minutes to under 2 minutes in the community speedrun ([1:07 to 2:35](https://youtu.be/oVsEddfhdxc?t=0))
- The optimizer speedrun record was about 2 minutes, and each agent run took about 15 to 20 minutes ([4:01](https://youtu.be/oVsEddfhdxc?t=241))
- Claude Code stopped about every 9 to 10 hours and was idle roughly one third of the time ([8:19](https://youtu.be/oVsEddfhdxc?t=499))
- Across both agents, token use was about 1 billion including cached input (speaker's estimate), with Codex using far more tokens and subagents than Claude; Codex has a 250k context window ([9:43](https://youtu.be/oVsEddfhdxc?t=583))
- Human record was about 2,990 steps; Claude beat it by about 50 to 60 steps and Codex by about 20 steps ([10:59](https://youtu.be/oVsEddfhdxc?t=659))
- Optimizer-only run lasted about five to six days; Kimi showed a breakthrough on day four and Claude used the most output tokens; Kimi was the most token-efficient ([12:25 to 13:52](https://youtu.be/oVsEddfhdxc?t=0))
- No novel optimizer emerged from any agent; gains came from combining papers with +1 changes ([15:20](https://youtu.be/oVsEddfhdxc?t=920))

## Hot takes
- Frontier coding agents can beat human research records on a speedrun, but they do not invent new mechanisms; they recombine known papers.
- Claude Code's stop-and-claim-it-cannot-improve behavior wastes a third of the run, so long autonomous research needs active monitoring or restarts.
- Recursive self-improvement claims need third-party benchmarks, and open labs such as Prime Intellect should run them in public.

## Tools mentioned
Claude Code, Codex, Slurm, AGENTS.md, goal.md, Verifiers, Prime-RL, Hosted Training, Kimi K2.7, GLM

## Relevance to our work
- **prosharness** (2/3): ProsHarness is built for checkpoint/resume and loops around Claude Code, and the talk's main operational problem is Claude Code stopping and sitting idle for hours until someone re-prompts it. The restart-with-latest-state pattern also fits ProsHarness's resume design. → *Add a stall detector to ProsHarness loops: when a Claude Code run ends claiming no further progress is possible, resume it automatically from the last checkpoint with a new direction and the current best result in context.*
- **agentos** (1/3): SkillForge needs a success signal and a skill-worthiness score; the talk's behavior logs (scratchpad writes, subagent count, tokens and compactions per active hour) show what telemetry could be compared across runs. → *Add scratchpad writes, subagent spawns and compactions per active hour as candidate success-signal features in the SkillForge telemetry design, then check whether they separate runs that beat a baseline from runs that stall.*
