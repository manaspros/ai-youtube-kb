# Figure 03 and the Future of Robotics

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `NL2zbYhC5Z4` · [watch](https://youtu.be/NL2zbYhC5Z4) · **date:** 2025-11-02 · **length:** 8:21 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** Andrus · **orgs:** Figure, Better Stack, NVIDIA, Boston Dynamics
- **topics:** models-research, training-finetuning-rl, agent-architecture · **tags:** robotics, humanoid, figure-03, helix, sim-to-real, real-time-control, sensor-latency, thermal-design, isaac-lab

> Better Stack's overview of Figure 03's claimed actuators, balance control, sensing, cooling and Helix model, plus speculative stack guesses from GitHub repo names; few reproducible details.

## Summary
The host walks through what Figure says makes its Figure 03 humanoid work: electric actuators with quasi-direct-drive gearboxes instead of hydraulics, a hybrid physics-plus-ML balance stack, stereo cameras with lower latency, palm cameras and fingertip force sensing, and an active-cooling, 2.3 kWh battery design with inductive foot charging. It credits a large behavior model called Helix for execution and describes idle robots offloading data for centralized training. The second half is inference from public GitHub repo names (an Isaac Lab fork, real-time motor repos, LightGlue ONNX, nvblox), which the host admits Figure has not open-sourced. The closing argument is that simulators such as Isaac Lab, Isaac Sim, MuJoCo and Brax let developers train robots without hardware. Almost every hardware figure is Figure's own claim, repeated without independent measurement, and the video gives no code, configs or reproducible steps.

## Key ideas
- **Figure moved from hydraulics to electric actuators, with quasi-direct-drive low-ratio gearboxes that cut friction and speed up control feedback.** — Hydraulics are described as powerful but messy and inefficient (Big Dog cited as the example). Electric actuators are claimed to be lighter, quieter and more responsive, with double the torque density. ([1:03](https://youtu.be/NL2zbYhC5Z4?t=63))
- **Humanoid balance is now a hybrid of physics and machine learning.** — A hierarchical inverse-dynamics solver runs hundreds of times per second to keep the center of mass inside the support polygon under the feet. Older systems used fixed if-this-then-that routines. The video notes the walk in the demo is very slow. ([1:56](https://youtu.be/NL2zbYhC5Z4?t=116))
- **Perception latency is treated as the main performance limit.** — Figure 3 is claimed to have stereo cameras with 60% wider field of view, twice the frame rate and one quarter of the latency of earlier single-camera designs. The host argues that even 100 ms of sensor delay visibly slows performance. ([1:56](https://youtu.be/NL2zbYhC5Z4?t=116))
- **Touch sensing is part of manipulation, not an add-on.** — Palm cameras and fingertip sensors are claimed to detect forces as light as 3 grams, enough to feel a paperclip begin to slip. Vision and touch together are presented as the basis for precise manipulation. ([3:12](https://youtu.be/NL2zbYhC5Z4?t=192))
- **Heat and power are design constraints the video calls underrated.** — Actuators, GPUs and batteries in a sealed shell create a large thermal load. The claimed fixes are active cooling channels in the die-cast frame, forced air moved through internal ducts, a 2.3 kWh pack lasting up to 5 hours, and 2 kW inductive charging through the feet. ([3:12](https://youtu.be/NL2zbYhC5Z4?t=192))
- **Execution runs on a proprietary large behavior model called Helix, and robots improve collectively.** — When off duty, robots offload data to a data center over 10 GB/s millimeter-wave links for centralized training, so the fleet's behavior can improve with each iteration. The video does not say how this training works. ([4:20](https://youtu.be/NL2zbYhC5Z4?t=260))
- **The stack architecture is inferred from public repo names, not from disclosed code.** — A fork of NVIDIA Isaac Lab suggests simulation-based policy training. Repos named like real-time motor control suggest a layered design, with hard real-time C++ joint loops below planning. LightGlue ONNX points to visual feature matching, and nvblox to dense 3D voxel mapping. The host calls these breadcrumbs and says Figure has not open-sourced its control stack. ([5:09](https://youtu.be/NL2zbYhC5Z4?t=309))
- **Developers can reproduce the training side with open simulators, not the robot.** — The closing argument names Isaac Lab, Isaac Sim, MuJoCo and Brax for simulation and RL training, plus nvblox and LightGlue ONNX for mapping and feature tracking on a local GPU. The video offers no setup steps. ([6:24](https://youtu.be/NL2zbYhC5Z4?t=384))

## Techniques
- **Physics-first balance with a learned layer** — Continuously solve joint motions (the speaker names hierarchical inverse dynamics, run hundreds of times per second) so the center of mass stays inside the support polygon formed by the feet. Put the ML layer on top of this physics controller. This is the speaker's description of Figure's approach, not verified. *When:* Bipedal or humanoid locomotion, especially on uneven terrain where fixed routines fail.
- **Layered real-time control stack** — Keep a hard real-time joint-control loop (speaker infers C++) isolated below planning and coordination layers, so actuators stay stable while higher-level logic runs slower. The layering is inferred from repo names. *When:* Robots or any closed-loop physical system where control jitter must not depend on planner latency.
- **Sim-to-real RL with massively parallel environments** — Spin up thousands of parallel simulated robots, randomize their environments, train control policies with reinforcement learning, then transfer them to hardware. The video names Isaac Lab for this and says Figure appears to use it, based on a fork. *When:* Teaching locomotion or manipulation when real-world trial and error would damage hardware.
- **Latency budgeting as a first-class metric** — Measure and reduce sensor-to-action delay directly (camera frame rate, latency, field of view) rather than optimizing model accuracy alone. The speaker treats latency as the primary performance limit. *When:* Any closed-loop perception-and-control system where delay compounds, such as robots or real-time agents.
- **Thermal co-design with structure** — Route cooling channels through the structural die-cast frame and move air through internal ducts, so heat removal and mechanical design happen together. The speaker describes Figure's design this way. *When:* Dense compute, batteries and actuators packed into a tight enclosure.
- **Fleet-wide offload for centralized training** — Robots that are off duty upload their data to a data center over a high-bandwidth link (the video cites 10 GB/s millimeter-wave) for centralized training, so one training run improves every robot. *When:* Deployed robot fleets with idle time and high-bandwidth connectivity.

## Numbers
- Stereo cameras with 60% wider field of view, 2x frame rate, and one quarter of the latency (Figure's claim). ([1:56](https://youtu.be/NL2zbYhC5Z4?t=116))
- Hierarchical inverse-dynamics balance solver runs hundreds of times per second. ([1:56](https://youtu.be/NL2zbYhC5Z4?t=116))
- Fingertip and palm sensing detects forces as light as 3 grams. ([3:12](https://youtu.be/NL2zbYhC5Z4?t=192))
- 2.3 kWh battery pack sustaining activity for up to 5 hours. ([3:12](https://youtu.be/NL2zbYhC5Z4?t=192))
- 2 kW inductive charging through the feet. ([3:12](https://youtu.be/NL2zbYhC5Z4?t=192))
- Off-duty data offload over 10 GB/s millimeter-wave links. ([4:20](https://youtu.be/NL2zbYhC5Z4?t=260))
- Example: sensors 100 ms late noticeably lag performance (illustrative, not measured). ([2:50](https://youtu.be/NL2zbYhC5Z4?t=170))

## Hot takes
- Quality is capped at 2: a 'future of robotics' title over a single product demo, and the body is mostly inferred and speculative.
- The stack architecture (Isaac Lab fork, layered C++ control, nvblox mapping) is inferred from GitHub repo names. The video itself says Figure has not open-sourced its control stack.
- Nearly all hardware numbers (latency, battery, cooling, 3 g touch sensitivity) are Figure's own claims repeated without independent verification.
- The host notes the demo walks very slowly, which undercuts the 'almost flawless' framing given at the start.
- The closing claim that anyone can train their own robotic agent overstates what open simulators provide. No setup, hardware path or steps are shown.

## Tools mentioned
Figure 03, Helix (Figure's large behavior model), NVIDIA Isaac Lab, NVIDIA Isaac Sim, MuJoCo, Brax, nvblox (transcribed as NV Blocks), LightGlue ONNX
