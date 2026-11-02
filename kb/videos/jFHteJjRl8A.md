# Robotics Has Been Stuck for 70 Years — Deepak Pathak, Skild AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `jFHteJjRl8A` · [watch](https://youtu.be/jFHteJjRl8A) · **date:** 2026-09-27 · **length:** 28:18 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Deepak Pathak · **orgs:** Skild AI, NVIDIA, UC Berkeley, CMU, Google
- **topics:** voice-multimodal, training-finetuning-rl, models-research, data-engineering · **tags:** robotics, physical-ai, teleoperation, imitation-learning, sim-to-real, data-flywheel, end-to-end-policy, omnibodied-model, moravec-paradox, pretraining-post-training

> Deepak Pathak (Skild AI) argues robotics lacks internet-scale data, so the answer is one omnibodied brain pretrained on diverse data, post-trained on teleop, and improved by a deployment data flywheel.

## Summary
Pathak opens with a history of robotics demos (a 1960s MIT copy demo, teleoperation rigs from the 1950s, Berkeley table cleanup on one GPU) to argue the field has barely moved in decades, and that hardware-first thinking is the cause. He ties this to Moravec's paradox: perception and physical adaptation are hard, while fully observed tasks such as backflips are easy. The core claim is that robotics has no internet-scale data, and teleoperation at about one minute per example cannot reach LLM-scale token counts. His proposed recipe is to pretrain on scalable, diverse but noisy data (simulation, human video), post-train on small high-quality teleop data, and add deployment data that grows once robots are deployed. He argues for a single "omnibodied" end-to-end model across any robot, reading camera input and driving motors with only a PID inner loop, and shows transfer from human video with under one hour of robot data. Deployment results include a GPU assembly line at NVIDIA's Houston factory, package delivery, and fault recovery when a robot leg breaks. The talk is mostly a company overview, but it has concrete data-cost and transfer numbers.

## Key ideas
- **Robotics lacks internet-scale data, which is why the LLM scaling recipe does not transfer directly.** — Teleoperation takes about one minute per example. The speaker says matching GPT-3-scale token counts this way would take more than a century of the whole US population working on it. He calls teleop slow and expensive, and not a new idea. ([5:43](https://youtu.be/jFHteJjRl8A?t=343))
- **Judge data sources on three axes: scalability, diversity, and closeness to the robot's own joint angles.** — Simulation is very scalable and moderately close to the robot, but low in diversity. Human video is scalable and diverse but far from robot data. Teleop is close to the robot but hard to scale. No single source wins, and the sources' weaknesses complement each other. ([9:48](https://youtu.be/jFHteJjRl8A?t=588))
- **Pretrain on scalable, diverse, lower-quality data, then post-train on a small amount of high-quality teleop.** — He says this mirrors LLM training. Simulation and human video are used for pretraining, and teleop for post-training. A third bucket, deployment data, becomes the largest source once deployment is at scale. ([12:41](https://youtu.be/jFHteJjRl8A?t=761))
- **A deployment data flywheel feeds post-training and deployment data back into pretraining.** — The speaker argues one robot shape will never be deployed everywhere, so a single omnibodied model is needed to pool data across hardware. Deployment itself is named as the hardest part of the flywheel. ([13:48](https://youtu.be/jFHteJjRl8A?t=828))
- **A single end-to-end policy reads camera input and drives motors, with no state machine and only a PID loop at the bottom.** — The PID loop raises control from 100 to 500 Hz. He says vision is just another input, and the robot is trained on as little as under 10 hours of data for omelet making with unseen objects. Robustness comes from the pretrained base model. ([18:50](https://youtu.be/jFHteJjRl8A?t=1130))
- **Human video pretraining plus under one hour of robot data transfers to humanoids.** — The robot's own model generates imagined scenarios, which the speaker calls the robot's dream, to multiply learning from few examples. He says the work is moving from egocentric human video to third-person video, which would open up YouTube as a source. ([17:20](https://youtu.be/jFHteJjRl8A?t=1040))
- **Moravec's paradox explains why stair climbing is hard and backflips are easy.** — A backflip only requires knowing the robot's own body, which is fully observed and easy to simulate. Stairs require perceiving unknown geometry and adapting to disturbances, so they need vision and understanding. ([21:39](https://youtu.be/jFHteJjRl8A?t=1299))
- **Fault recovery and safety fall out of the omnibodied model.** — When a leg is disabled, the robot relearns to walk on two legs in about three trials. Adaptation takes from milliseconds to around 30 seconds, and the same brain runs on wheels when a wheel jams. ([25:42](https://youtu.be/jFHteJjRl8A?t=1542))

## Techniques
- **Pretrain on diverse, scalable data, post-train on small high-quality teleop** — Use simulation and human video for broad pretraining, then fine-tune on a small set of teleoperated demonstrations that match the target robot's joint-level data. *When:* When high-quality target-domain data is scarce but cheap, noisy data is plentiful.
- **Deployment data flywheel** — Log data from deployed robots and feed it back into pretraining, so each deployment improves the shared base model. *When:* When the system is already deployed and can gather data at scale.
- **End-to-end camera-to-motor policy with only a low-level PID loop** — Skip hand-built planning, mapping and state machines. Map camera input directly to motor commands, with a PID controller only to run the loop at 100-500 Hz. *When:* When a single learned policy must cover many tasks and the system must tolerate disturbances.
- **Learn from human video, then adapt with minimal robot data** — Pretrain on egocentric human video, then add under one hour of robot data to transfer to the robot embodiment. *When:* When robot data is expensive but human video is plentiful.
- **Cross-embodiment zero-shot transfer** — Train one model across many robot bodies and deploy it zero-shot to unseen humanoids and platforms. *When:* When you need one model to run on varied or changing hardware.

## Numbers
- Teleoperation takes about 1 minute per training example, which the speaker says makes LLM-scale data collection impractical. ([5:43](https://youtu.be/jFHteJjRl8A?t=343))
- GPT-3 training used roughly 30 trillion tokens. Current frontier models use hundreds of trillions. ([5:43](https://youtu.be/jFHteJjRl8A?t=343))
- The omelet-making robot costs about $4,000 in arms and has only a camera as sensor (no force sensing). ([18:50](https://youtu.be/jFHteJjRl8A?t=1130))
- Omelet-making robustness was learned from under 10 hours of robot data. ([20:12](https://youtu.be/jFHteJjRl8A?t=1212))
- Transfer to humanoids needed under one hour of robot data after pretraining on human video. ([17:20](https://youtu.be/jFHteJjRl8A?t=1040))
- Robot hands reportedly break within about 100 hours of use in the speaker's experience. ([17:20](https://youtu.be/jFHteJjRl8A?t=1040))
- A newer stair-climbing policy trains in about 30 minutes, versus much longer for the earlier version. ([23:07](https://youtu.be/jFHteJjRl8A?t=1387))
- After disabling a leg, the robot learns to walk on two legs in about three trials, with adaptation taking from milliseconds to around 30 seconds. ([25:42](https://youtu.be/jFHteJjRl8A?t=1542))

## Hot takes
- Robotics has been stuck for about 70 years because it has been treated as a hardware problem first.
- Humanoid claims about home robots by December are hype, and the real test is whether a humanoid can climb stairs.
- Hands are an excuse for the lack of progress. The bottleneck is the intelligence, not the hand.
- Moravec's paradox is the central lens: what humans find hard, such as perception and adaptation, is hard for robots, and what seems hard, such as backflips, is easy.

## Relevance to our work
- **agentos** (1/3): The pretrain / post-train / deployment-data split and the flywheel idea map loosely onto SkillForge's mining of agent telemetry into skills. → *Read how the speaker frames the flywheel (deployment data feeding pretraining) and compare it to SkillForge's planned telemetry-to-skill loop, to see whether raw telemetry should count as pretraining data and curated traces as post-training data.*
- **general** (1/3): The three-axis data check (scalability, diversity, closeness to target) is a reusable way to pick training or eval data sources. → *When choosing data for a cheap-model pipeline or an entity-resolution labeling set, score each candidate source on scale, diversity and closeness to the production distribution before mixing them.*
