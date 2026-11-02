# Scaling up Continual Learning — Ronak Malde, Trajectory

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `zL1kLftVTlo` · [watch](https://youtu.be/zL1kLftVTlo) · **date:** 2026-08-18 · **length:** 23:03 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Ronak Malde · **orgs:** Trajectory, Windsurf, Google DeepMind, Harvey, Dekagon, Rogo
- **topics:** training-finetuning-rl, agent-architecture, skills-self-improvement · **tags:** continual-learning, on-policy-distillation, self-distillation, OPSD, GRPO, hint-leakage, long-horizon-tool-calling, token-efficiency, production-traces

> Ronak Malde (Trajectory) on scaling continual learning: on-policy self-distillation with privileged hints as a step past GRPO, plus fixes for long tool-calling runs (step-level weighting, hint-leakage control).

## Summary
The speaker argues that benchmark-driven RL is getting slower and more expensive, while production traffic already produces failure data worth training on. He walks through the trade-offs of SFT, DPO/RLHF and GRPO across four criteria: task distribution, on-policy sampling, parallelism and reward granularity. His proposed method, on-policy self-distillation (OPSD), samples one rollout from the student, gives the same model a hint in its prompt as a teacher, and fits the student's per-token distribution to that teacher. He reports this works on short tasks, including better LiveCodeBench results than GRPO, but breaks down at around 120B parameters with 50 to 100 tool calls, where hedging words ("wait", "maybe") take over and run-to-run variance rises. His fixes are per-step KL weighting for long trajectories, an LLM filter or residual (partial-hint) guidance to prevent hint leakage, and a reported 120B result on Mercor APEX-Agents. The talk closes with a pitch for Trajectory's platform and a Q&A admitting the field is still in "pseudo-continual learning" with batch updates.

## Key ideas
- **Benchmark-driven RL is getting slower and more expensive** — Benchmarks saturate within months, and some take 4, 6, 24 hours or several days to build. The speaker argues they are also not tied to real-world use, while production inference already generates failure data that could be trained on. ([0:08](https://youtu.be/zL1kLftVTlo?t=8))
- **Four criteria explain the progression from SFT to GRPO** — The criteria are task distribution (online vs fixed), on-policy sampling, parallelism (how many rollouts and environment copies are needed), and reward granularity (per-token vs sequence). Each method trades some of these off. GRPO gives on-policy learning but needs heavy parallel environment infrastructure and a sequence-level reward. ([2:43](https://youtu.be/zL1kLftVTlo?t=163))
- **On-policy self-distillation uses the model as its own teacher through a hint** — The student rolls out on its own task. The same model, given privileged information (a hint, or a golden solution) in its prompt, acts as the teacher. The student's per-token log-probs are fitted to the teacher's. This needs one rollout per example, not a group. ([7:49](https://youtu.be/zL1kLftVTlo?t=469))
- **Match the full vocabulary distribution, not only the sampled token** — The speaker says the update touches the whole distribution over roughly a 65K-token vocabulary at each step, which shifts whole distributions rather than sharpening the sampled choice as RL does. He reports that GRPO plateaus near Sonnet-level on LiveCodeBench while this approach reaches further. ([10:23](https://youtu.be/zL1kLftVTlo?t=623))
- **Long tool-calling runs expose failure modes that short tasks hide** — At around 120B parameters with 50 to 100 tool calls, eval accuracy and run-to-run variance get high and tool-call format errors appear. The teacher keeps correcting the drifting student, which leads to a local optimum full of hedging words, with the student stuck between two divergent distributions. ([13:08](https://youtu.be/zL1kLftVTlo?t=788))
- **Weight each step by how far the student has drifted from the teacher** — Per-step KL between student and teacher is used as a token weight instead of a KL penalty. Steps that diverge heavily are down-weighted, while steps that get back on track regain weight later in the trajectory. ([14:35](https://youtu.be/zL1kLftVTlo?t=875))
- **Hint leakage is the OPSD version of reward hacking** — The student can learn to act as if it knows the hidden answer (the speaker's example: it reasons its way to the zeros in a last-three-digits problem). Two mitigations are named: an LLM that rewrites the hint into something the student could plausibly have known, and residual guidance that mixes the partial-hint and full-hint teacher log-probs to control how far the update moves. ([15:57](https://youtu.be/zL1kLftVTlo?t=957))
- **Q&A: the field is still in pseudo-continual learning** — Current systems do offline batch updates and re-upload the model. Merging the rollouts from many users is partly an infrastructure problem. The speaker calls the joint updating of model and harness, which he says is underexplored, one of the most exciting open questions. ([21:28](https://youtu.be/zL1kLftVTlo?t=1288))

## Techniques
- **On-policy self-distillation (OPSD)** — Sample one rollout from the student on its own task prompt. Re-score the same rollout with the same model given a privileged hint in the prompt (the teacher). Train the student to match the teacher's per-token distribution over the full vocabulary. *When:* When no stronger teacher model exists and you want on-policy, single-rollout, per-token training on a fixed or online task distribution.
- **Step-level divergence weighting for long trajectories** — Compute the KL between student (no hint) and teacher (with hint) at each step of a tool-calling trajectory. Use that KL as the token weight for the step, not as a penalty. Steps that diverge are down-weighted and steps that re-align count again. *When:* When OPSD works on short tasks but degrades on long multi-tool-call runs (around 50 or more calls).
- **Residual guidance via linear combination of hint strengths** — Get teacher log-probs from a partial hint (about half the hint) and from the full hint. Take a linear combination of the two so the target sits between them, which limits how far the student moves out of its own distribution. *When:* When the full hint is far out of distribution for the student and a full-hint update shifts the model into unknown territory.
- **LLM-filtered hints to prevent leakage** — Have an LLM turn a hint built from logs or the solution into a form the student could plausibly have known. The speaker's example: an expired SSO token found in the logs becomes a reasonable diagnostic clue, not the answer. *When:* When hints contain information the student could not know at inference time, and you need to avoid shortcut reasoning.
- **Inspect rollouts for hint leakage** — Read rollouts for signs that the student refers to the hidden answer or skips steps it could not know, as in the speaker's last-three-digits example. *When:* Whenever you design hints for OPSD, before relying on the training signal.

## Numbers
- Some benchmark tasks take 4 hours, 6 hours, 24 hours or several days to scale up ([0:08](https://youtu.be/zL1kLftVTlo?t=8))
- Labs are spending hundreds of trillions of tokens per day on inference (speaker's figure) ([1:18](https://youtu.be/zL1kLftVTlo?t=78))
- GRPO uses a group of about 8 parallel rollouts per example, which OPSD avoids ([9:08](https://youtu.be/zL1kLftVTlo?t=548))
- Vocabulary of about 65K tokens that OPSD optimizes over at each token ([10:23](https://youtu.be/zL1kLftVTlo?t=623))
- GRPO saturates around Sonnet-level performance on LiveCodeBench (speaker's observation) ([10:23](https://youtu.be/zL1kLftVTlo?t=623))
- Scaled tests ran on 120B, 500B and 1 trillion parameter models ([11:43](https://youtu.be/zL1kLftVTlo?t=703))
- Breakdown appears around 120B parameters with 50 to 100 tool calls, with high eval variance and tool-call format errors ([11:43](https://youtu.be/zL1kLftVTlo?t=703))
- A 120B model reportedly reaches results on Mercor APEX-Agents, a task that needs 100+ tool calls (no score given in talk) ([18:40](https://youtu.be/zL1kLftVTlo?t=1120))

## Hot takes
- Benchmark-based RL scaling is becoming too slow and expensive, and production traces are the better training signal.
- On-policy self-distillation with a hint can surpass RL on some long-horizon agentic tasks (speaker's claim, no numbers in talk).
- Continual learning for agents needs the model and the harness updated together, and this joint update is underexplored.
- Per-token dense reward is more useful than one scalar reward per rollout for messy real-world data.

## Tools mentioned
GRPO, OPSD, OpenClaw RL, LiveCodeBench, Mercor APEX-Agents

## Relevance to our work
- **agentos** (1/3): The SkillForge / EvolveCraft goal of turning agent telemetry into learning signal overlaps with using production traces as per-token training data, though the talk is about model weights, not skills. → *Read the OPSD and step-level divergence ideas as a possible signal design for EvolveCraft, and check hint leakage before any use on real traffic.*
- **prosharness** (1/3): The speaker's point that run-to-run variance at 100+ tool calls can dominate results matters for any long-run harness that is checkpointed and resumed. → *When ProsHarness evaluates long runs, record variance across reruns of the same plan, not a single pass.*
