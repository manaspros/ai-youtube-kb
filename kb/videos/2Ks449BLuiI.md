# LBMs Are About to Change Everything in Robotics

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `2Ks449BLuiI` · [watch](https://youtu.be/2Ks449BLuiI) · **date:** 2025-11-02 · **length:** 4:51 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** Andrus · **orgs:** Better Stack, Figure AI, Toyota Research Institute
- **topics:** models-research, agent-architecture · **tags:** robotics, large-behavior-models, vision-language-action, helix, hierarchical-control, teleoperation-data, open-source-robotics, sim-environments

> Explainer on large behavior models (LBMs), robot-control models that map camera, joint and language inputs to actions, using Figure AI's Helix as the example. Thin on substance; mostly hype and analogy.

## Summary
Andrus from Better Stack introduces large behavior models (LBMs) as "LLMs for the real world": models that take camera feeds, joint angles and language prompts and output robot actions. He uses Figure AI's Helix as the main example, describing a single vision-language-action model that picks up objects it has not seen before, controls the upper body including fingers at 200 Hz on embedded GPUs, and runs one set of weights across several robots. He describes Helix's two-layer design, a slow layer that reasons over vision and language a few times per second and a fast reflex layer at 200 Hz. He cites Toyota Research Institute's finding that a few hundred hours of diverse data reduces fine-tuning needs, and says Helix used roughly 500 hours of teleoperated data. He ends by pointing to the open-source OK-Robot project and to simulators such as Isaac Gym and MuJoCo as entry points. The video gives no benchmarks, no source links for the figures, and no hands-on detail.

## Key ideas
- **LBMs are presented as LLMs for the physical world: they take camera feeds, joint angles and language and predict the next robot action instead of the next token.** — The aim is robots that adapt to new situations rather than following pre-programmed scripts. This is a framing, not a technical explanation of how the model is trained or structured. ([0:00](https://youtu.be/2Ks449BLuiI?t=0))
- **Helix is described as one model that combines vision, language and action, so a spoken command like 'pick up a mug' can be carried out on a mug the model has never seen.** — The speaker says it controls the whole upper body including fingers at 200 Hz, running on embedded GPUs on the robot. No success rates or comparison baselines are given. ([1:01](https://youtu.be/2Ks449BLuiI?t=61))
- **Helix's data is claimed to be small: roughly 500 hours of teleoperated demonstrations, which the speaker says is far less than people expect.** — This is used to argue that smaller teams and open-source groups could replicate similar models. The claim is not backed by evidence in the video. ([1:01](https://youtu.be/2Ks449BLuiI?t=61))
- **Helix uses a two-layer control design: a slow reasoning layer and a fast reflex layer.** — The slow layer processes vision and language at a few frames per second to handle high-level goals. The fast layer runs 200 times per second to drive the joints, so the robot can react immediately to its surroundings. ([2:04](https://youtu.be/2Ks449BLuiI?t=124))
- **One set of weights runs on several robots at once, so they share what they have learned.** — In the demos, two robots with the same model coordinate on tasks such as putting away groceries and passing objects between them, without extra training. The speaker calls this a fleet sharing skills. ([2:04](https://youtu.be/2Ks449BLuiI?t=124))
- **Toyota Research Institute is cited as finding that a few hundred hours of diverse data means robots need far less fine-tuning.** — This is the only data-scaling claim in the video, and it is given without a paper, figure or method. ([1:01](https://youtu.be/2Ks449BLuiI?t=61))
- **For hands-on work, the video points to the OK-Robot open-source framework for language-conditioned pick-and-place in homes, and to simulators such as Isaac Gym and MuJoCo.** — The speaker describes OK-Robot as a modular stack linking perception, planning and control using off-the-shelf models and affordable hardware. No setup steps or commands are shown. ([3:12](https://youtu.be/2Ks449BLuiI?t=192))

## Techniques
- **Two-rate hierarchical control (slow reasoner, fast reflex)** — Run a slow loop that handles vision and language at a few Hz to set high-level goals, and a separate fast loop at around 200 Hz that turns those goals into joint-level control. The fast loop keeps the robot reacting in real time while the slow loop does the reasoning. The speaker presents this as the core of Helix's design, and gives no implementation detail. *When:* When one model has to plan at a slower rate than a control loop must run, for example robot control or any system where a fast feedback loop must stay responsive while a slower model decides what to do.
- **One shared policy across several robots** — Load the same weights onto multiple robots and let them share what they learn. The speaker describes this as coordination without extra training, shown in grocery-putting-away and object-handover demos. No training or deployment details are given. *When:* When several agents or robots perform related tasks and you want to share skills across them rather than train each one separately.
- **Starting point for hands-on LBM work** — Begin with the OK-Robot open-source framework to see how perception, planning and control connect using off-the-shelf models. Then move to simulators such as Isaac Gym or MuJoCo before real hardware. The speaker gives no commands or versions. *When:* When you want to learn LBM-style robot control on affordable hardware or in simulation before attempting a real robot.

## Numbers
- Helix controls the upper body, including fingers, at 200 Hz, running on embedded GPUs. ([1:01](https://youtu.be/2Ks449BLuiI?t=61))
- Helix was trained on roughly 500 hours of teleoperated data. ([1:01](https://youtu.be/2Ks449BLuiI?t=61))
- Toyota Research Institute found that a few hundred hours of diverse training data means robots need far less fine-tuning. ([1:01](https://youtu.be/2Ks449BLuiI?t=61))
- The slow reasoning layer processes vision and language at a few frames per second; the fast reflex layer runs 200 times per second. ([2:04](https://youtu.be/2Ks449BLuiI?t=124))

## Hot takes
- The title says LBMs 'are about to change everything', but the video gives no benchmarks, success rates or comparisons to back that up.
- The claim that smaller and open-source teams could realistically replicate Helix is asserted, not shown.
- The comparison to 'GPT-3 and GPT-4' and to '2021 for LLMs' is an analogy presented as a trend, with no supporting evidence.
- The video cites Toyota Research Institute and the 500-hour figure without sources, so the data-efficiency argument cannot be checked from the video.

## Tools mentioned
Helix (Figure AI robot model), OK-Robot (open-source pick-and-place framework), Isaac Gym (simulator), MuJoCo (simulator; auto-caption reads 'Mujocko'), GPT-3 (mentioned as an analogy), GPT-4 (mentioned as an analogy)

## Relevance to our work
- **general** (1/3): Useful as background on robot foundation models and hierarchical control, but thin and not practitioner-level.
