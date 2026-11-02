# From VLM/VLA's to Embodied Agents — Armen Aghajanyan, Perceptron AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ZZcE0HeO-Hc` · [watch](https://youtu.be/ZZcE0HeO-Hc) · **date:** 2026-09-27 · **length:** 20:42 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Armen Aghajanyan · **orgs:** Perceptron AI, Meta FAIR, Google DeepMind, Allen Institute for AI (AI2)
- **topics:** voice-multimodal, models-research, training-finetuning-rl · **tags:** embodied-ai, robotics, vlm, vla, world-models, mixture-of-experts, token-sparsity, video-understanding, teleop-data, scaling-laws, agentic-vision, orchestrator-policy

> Perceptron's CEO argues VLMs, VLAs and world models should merge into one "embodied foundation model," and shares sparsity, token-routing and data-mix findings with public benchmarks but few hard details.

## Summary
Armen Aghajanyan (transcribed as "Armin"), co-founder and CEO of Perceptron AI, argues the field should stop separating VLMs, VLAs and world models and build one embodied foundation model that perceives, reasons and acts. He names two core problems: video is extremely sparse (about 1M visual tokens per hour, with loss on roughly 0.2% of them) and context bloats fast with always-on cameras. His answer is a data-sparse mixture-of-experts with a learned router that skips low-value tokens, which he says makes the model focus on task-relevant regions without hard-coded priors. He reports that his model beats Gemini embodied reasoning and is about 15x cheaper, and that detection becomes an agentic code-and-zoom loop. On robotics, he claims a scaling trade where 10x more video pretraining can replace 10x less teleop data (about $100/hour), and that joint perception-control models are more robust to background changes than VLA fine-tunes. Most results are unpublished or reported as company claims, and the talk ends with a pitch for partner access and a planned open-source smaller model.

## Key ideas
- **Unify perception, reasoning and control in one embodied foundation model** — The speaker wants to drop the split between VLMs, VLAs, world models and semantic world models. A single model should take in many modalities and output text, grounding, actions and more. ([0:08](https://youtu.be/ZZcE0HeO-Hc?t=8))
- **Video supervision is extremely sparse** — One hour of video can be about 1M visual tokens, but the loss touches only about 0.2% of them. Synthetic labels and predicting every pixel both inject a poor training signal, either too sparse, too synthetic or too indiscriminate. ([3:43](https://youtu.be/ZZcE0HeO-Hc?t=223))
- **Learn which percepts matter instead of hard-coding them** — Hard-coded targets such as the gripper tip help, but the speaker wants the model to discover the useful future percepts automatically. He says they have a way to do this but will not describe it. ([4:36](https://youtu.be/ZZcE0HeO-Hc?t=276))
- **Learned token routing (data-sparse MoE) handles context bloat** — A router in each layer decides which tokens to process and which to skip. Visualizations show the model focusing on dense or task-relevant areas, such as a graph or the fruit when asked to segment fruit, with few hand-coded architectural priors. ([7:02](https://youtu.be/ZZcE0HeO-Hc?t=422))
- **Reframe classical CV tasks as agentic loops** — The model writes code, zooms into regions, tiles the image, changes contrast and proposes boxes to find hard-to-see objects. Detection becomes an iterative search rather than a single bounding-box output. ([9:25](https://youtu.be/ZZcE0HeO-Hc?t=565))
- **Split orchestrator and low-level control policy** — One pattern for robots is a reasoning orchestrator that breaks a task into subtasks, with a control policy running underneath. The speaker places this on a spectrum between a single end-to-end VLA and a full agentic system. ([11:18](https://youtu.be/ZZcE0HeO-Hc?t=678))
- **Trade teleop data for video pretraining** — Teleop data costs about $100 per hour, while video pretraining is far cheaper. The speaker claims 10x more video pretraining can replace 10x less teleop data in unified models, a gain he says pure VLA policies do not show as strongly. ([12:37](https://youtu.be/ZZcE0HeO-Hc?t=757))
- **Data distribution matters for spatial and temporal skills** — Internet crawls rarely label left/right or above/below relations, so models struggle with them unless the data is curated early. The speaker also mentions key-frame vs delta-frame management as a way to control context for robot video, though he says they moved past it. ([17:17](https://youtu.be/ZZcE0HeO-Hc?t=1037))
- **Joint perception and control improves robustness** — Fine-tuned VLA policies can fail when the table background changes. The speaker says joint perceptive and control modeling, plus online augmentations such as a faked camera outage or sunlight, makes the policy more robust, though he does not overclaim. ([18:44](https://youtu.be/ZZcE0HeO-Hc?t=1124))

## Techniques
- **Data-sparse MoE token routing** — Add a router in the model that decides, per layer, which tokens to process and which to skip. The model learns the routing with few hard-coded priors, and visualizations show it focusing on high-density or task-relevant regions. *When:* Long, dense inputs such as high-FPS video or always-on camera streams, where most tokens carry little signal.
- **Agentic detection with zoom, tiling and contrast** — Give the model code execution and image operations so it can tile, zoom, adjust contrast and propose boxes iteratively, instead of a one-shot detection output. *When:* Finding small or hard-to-see objects in images, where a single pass fails.
- **Orchestrator plus low-level control policy** — A reasoning model decomposes a robot task into subtasks and hands each one to a fast control policy, sitting between a pure end-to-end VLA and a full agent system. *When:* Multi-step physical tasks that mix perception, reading and control, such as reading a book title and then sorting it into a bin.
- **Self-verifying video annotation** — The model clips video segments, re-looks at them, checks whether captions are correct and corrects itself, all in one loop. *When:* Bulk annotation of robot or egocentric video, where cost per clip must stay low.
- **Online augmentation for robustness** — During training, simulate faults and lighting changes, such as an arm camera going dark or sunlight from one direction. *When:* Robot policies that must survive camera faults and lighting or background shifts.
- **Patch averaging for token compression** — Average patch-wise representations across a video or image to compress tokens, reported up to about 10x. The speaker calls this a hack and not a proper architectural fix. *When:* A quick baseline for reducing visual token count before a learned method is in place.

## Numbers
- One hour of video can produce about 1M visual tokens, and the loss covers about 0.2% of them ([3:43](https://youtu.be/ZZcE0HeO-Hc?t=223))
- Patch-wise averaging for token compression reaches up to about 10x ([5:46](https://youtu.be/ZZcE0HeO-Hc?t=346))
- Perceptron's model is said to be on the frontier of Gemini 3.1 Pro and better than Gemini Embodied Reasoning, at about 15x lower cost (company claim) ([9:25](https://youtu.be/ZZcE0HeO-Hc?t=565))
- The training data totals about one petabyte across text, images, video, trajectories and synthetic data ([9:25](https://youtu.be/ZZcE0HeO-Hc?t=565))
- Teleop data costs on the order of $100 per hour ([12:37](https://youtu.be/ZZcE0HeO-Hc?t=757))
- 10x less teleop data can be traded for 10x more video pretraining data in unified models (company claim) ([13:36](https://youtu.be/ZZcE0HeO-Hc?t=816))
- Context window of about 1M tokens for the models discussed ([15:59](https://youtu.be/ZZcE0HeO-Hc?t=959))

## Hot takes
- The VLM, VLA and world-model split should be dropped in favor of a single embodied foundation model.
- Predicting every pixel allocates attention poorly, because background pixels get the same weight as the gripper tip or contact points.
- Fine-tuned VLA policies are brittle: changing the table background can make them fail.
- Internet-scale data lacks spatial relations such as left and right, so data distribution has to be planned early.

## Tools mentioned
Gemini 3.1 Pro, Gemini Embodied Reasoning, Perceptron models (Mark 1)

## Relevance to our work
- **prosharness** (1/3): The orchestrator plus low-level policy split is an analogue of ProsHarness's plan-then-execute loop, but the talk gives no reusable harness detail. → *Optional read: skim the planner and executor split pattern only as a design analogy for ProsHarness plan and checkpoint steps. No code change suggested.*
- **general** (1/3): Context-management ideas (key frames vs delta frames, skipping low-value tokens) loosely connect to context-engineering work, but they are about video tokens, not text agent context. → *Note the learned skip-or-process router idea as a reference for context-engineering discussions, and do not act on it yet.*
