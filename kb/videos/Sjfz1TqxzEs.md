# Robot Demos Are Easy. Reliability Is Hard — Jason Ma, Dyna Robotics

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Sjfz1TqxzEs` · [watch](https://youtu.be/Sjfz1TqxzEs) · **date:** 2026-09-27 · **length:** 26:42 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Jason Ma · **orgs:** Dyna Robotics
- **topics:** training-finetuning-rl, evals, voice-multimodal · **tags:** robotics, foundation-models, reward-model, active-learning, reliability, vla, deployment-data, error-recovery, commercial-deployment

> Dyna Robotics co-founder on making generalist robot manipulation policies reliable enough for commercial use, via reward-model progress scoring and a targeted active-learning loop.

## Summary
Jason Ma, co-founder of Dyna Robotics, argues that robot demos are easy but reliability is the hard part. He says generalist manipulation models typically hit 80-90% success in deployment, which he frames as too low for commercial work. His team's pipeline mixes off-robot human video, public datasets, on-robot data and deployment data, under a high-level reasoning model plus a low-level action model. The main technique is a reward model that scores task progress from video; dips in the score flag mistakes, so failures can be caught in the background and used for targeted data collection and retraining. On a napkin-folding task he reports 99.4% success over a 24-hour run, and he claims the general pre-training backbone helps the model recover from errors on new tasks. He also describes deploying at restaurants and a laundromat, and a conference run at a new site with no site-specific data. Caveat: his "10 in a row under 0.1%" figure does not match simple independent-trial math (0.8^10 is about 11%, 0.9^10 about 35%), so treat that stat as rhetorical. The talk is a company pitch with a Q&A; technical depth is moderate and no code or public eval setup is shown.

## Key ideas
- **Company flywheel: in-house R&D sets which tasks to commercialize, and deployments feed back data and show model weaknesses.** — Dyna says live deployments give high-quality data and reveal what models and hardware still fail at, which sharpens research priorities. ([1:19](https://youtu.be/Sjfz1TqxzEs?t=79))
- **Training data comes in three layers: off-robot human video and public data, on-robot diverse tasks, and deployment data.** — Off-robot data is cheap but not enough for precise actions. On-robot data adds precision. Deployment data closes the gap between lab and customer environments. The team reports over 200,000 hours in its training pipeline. ([2:44](https://youtu.be/Sjfz1TqxzEs?t=164))
- **Reliability, not peak success, is the bottleneck for commercial use.** — He says generalist models are around 80-90% successful in deployment. He argues a specialist pipeline does not scale to new tasks, so the goal is a general model that is also reliable. ([6:11](https://youtu.be/Sjfz1TqxzEs?t=371))
- **Good pre-training makes post-training cheap: under one hour of task data gives dexterous, repeatable behavior.** — Some demoed tasks were not in the pre-training data at all, yet fine-tuning on less than an hour of task data produced repeated success. ([4:54](https://youtu.be/Sjfz1TqxzEs?t=294))
- **A reward model that scores progress from video turns failures into a visible signal.** — Progress estimates rise steadily while the robot succeeds. They show non-monotonic dips when it makes a mistake, which lets operators detect failures without watching every run. ([11:52](https://youtu.be/Sjfz1TqxzEs?t=712))
- **Closed loop: the reward model catches failures, then targeted data collection and recovery data drive re-fine-tuning, repeated over several cycles.** — He calls this scalable supervision and active learning. Each cycle targets the failure modes the model is currently weak at, which is more efficient than manual oversight once the model is around 90%. ([13:06](https://youtu.be/Sjfz1TqxzEs?t=786))
- **Success criteria must be defined in terms a customer would accept.** — For napkin folding, a 'grade 5' fold is acceptable to the restaurant and a 'grade 3' is not. The two differ by about one inch in where the second fold seam sits. ([10:39](https://youtu.be/Sjfz1TqxzEs?t=639))
- **Recovery behavior generalizes across tasks because the pre-trained backbone has seen many error-recovery examples.** — Late Q&A remark: the model's recovery moves on napkins were largely interpolated from recovery behavior learned on other tasks. Training on a single task from the start was worse, he says. ([24:47](https://youtu.be/Sjfz1TqxzEs?t=1487))

## Techniques
- **Reward model as progress scorer for background supervision** — Train a model that reads robot video and outputs a 0-to-1 task-progress score. Run it during autonomous rollouts. Treat non-monotonic dips as a mistake signal and route those episodes to operators. *When:* Long-horizon tasks where failures are rare and manual watching is expensive, and the model is already reliable enough that most runs succeed.
- **Failure-driven active learning loop** — Use the reward-model alerts to find the failure modes the policy struggles with. Collect targeted data and error-recovery demonstrations for those modes, fine-tune, then repeat for several cycles. *When:* After the first fine-tune plateaus around 80-90% success and new failure modes keep showing up in deployment.
- **Pre-train, post-train, then active learn** — Pre-train a generalist on mixed off-robot, on-robot and deployment data. Post-train on small amounts of task data. Add an active-learning loop on top of that. *When:* Adapting one foundation model to many commercial tasks instead of training a separate specialist per task.
- **Grade-based success criteria tied to customer acceptance** — Define a graded quality scale using the customer's own acceptance threshold, and measure against that threshold rather than binary task completion. *When:* Physical or quality-sensitive tasks where a 'done' that the customer would reject still counts as failure.
- **Two-level architecture** — A high-level reasoning model handles semantics and planning. A low-level world-action model produces fine-grained, high-frequency motor actions and recovers from physical mistakes. *When:* Robot policies that need both semantic understanding and precise, fast control.

## Numbers
- Company founded Sept 2024; Series A; about $120M raised. ([0:12](https://youtu.be/Sjfz1TqxzEs?t=12))
- More than five deployment sites in use. ([1:19](https://youtu.be/Sjfz1TqxzEs?t=79))
- More than 200,000 hours of data in the training pipeline. ([3:50](https://youtu.be/Sjfz1TqxzEs?t=230))
- Typical generalist model success in deployment is about 80-90%. The speaker says 10 consecutive successes would then be under 0.1%, but independent-trial math gives about 11% at 80% and about 35% at 90%, so this figure looks overstated. ([6:11](https://youtu.be/Sjfz1TqxzEs?t=371))
- Post-training on less than one hour of task-specific data gives repeatable dexterous behavior. ([4:54](https://youtu.be/Sjfz1TqxzEs?t=294))
- Napkin-folding policy reached 99.4% success over a 24-hour run. The time-lapse is sped up about 1000x. ([8:21](https://youtu.be/Sjfz1TqxzEs?t=501))
- Four distinct 24-hour trials were shown. ([9:38](https://youtu.be/Sjfz1TqxzEs?t=578))
- Pre-training plus post-training alone reached about 80% on napkin folding before the reward-model loop. ([10:39](https://youtu.be/Sjfz1TqxzEs?t=639))
- Grade 5 vs grade 3 fold quality differs by about one inch in second-seam position. ([10:39](https://youtu.be/Sjfz1TqxzEs?t=639))
- Towel-folding demo ran for three days straight at Coral 2025 at a site the model had never seen, with no site-specific data. ([16:52](https://youtu.be/Sjfz1TqxzEs?t=1012))

## Hot takes
- Demo success rates mislead: a model at 80-90% per try fails most long repeated runs, so reliability has to be measured as a run-level number.
- A progress or reward signal that dips on mistakes can find failures faster than waiting for outright failure or manual review.
- For a new task, a general pre-trained backbone beats training from scratch on that one task, partly because it has seen recovery behavior from other tasks.

## Relevance to our work
- **agentos** (1/3): The reward-model idea of scoring progress over a long run and flagging non-monotonic dips maps loosely onto watching long agent traces for drift. This is an analogy, not a method from the talk. → *Look at whether a per-step progress score over agent traces (for example, tool-call sequences vs. a goal checklist) could feed AgentOS observability as an early failure signal.*
- **prosharness** (1/3): The failure-driven loop (detect failure, collect targeted recovery data, retrain) resembles resume and review loops on long Claude Code runs, but the talk is about robot policies, not coding agents. → *Consider logging the step where a long ProsHarness run first goes off-track and using those cases as targeted checkpoints or review prompts.*
- **general** (1/3): The talk shows the gap between demo and repeatable reliability over many runs. Evaluating agents on repeated-trial success rather than single-run success is a transferable point. → *When evaluating agent pipelines, report pass rates over repeated runs (for example pass^k) rather than one-shot success.*
