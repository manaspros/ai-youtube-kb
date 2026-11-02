# Tell the Robot What You Want — Sandhya Subramani, AWS

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `S6aSoQ6_u5A` · [watch](https://youtu.be/S6aSoQ6_u5A) · **date:** 2026-09-18 · **length:** 17:23 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** Sandhya Subramani · **orgs:** AWS
- **topics:** multi-agent, agent-architecture, voice-multimodal · **tags:** robotics, embodied-agents, strands, agentcore, vla, telegram, edge-cloud, tool-calling, claude-opus, raspberry-pi, teleoperation-data

> Live demo of a rover robot driven by an LLM agent built on the Strands harness, with a four-layer agent-to-hardware stack and a pitch that VLA policies may eventually make per-task robot training unnecessary.

## Summary
Sandhya Subramani (AWS) demos "Scout," a rover whose behavior is driven by natural-language instructions rather than only pre-trained policies. The rover runs on a Raspberry Pi in New York over a 4G SIM connection, and an LLM agent (Claude Opus 4.8 via the Strands agent SDK) decides which robot tool or policy to call. The talk describes a four-layer stack: the agent layer, a policy provider, a back end (simulation or real hardware), and the robot itself. It also describes a hybrid setup where policy training runs in the cloud on AgentCore while runtime calls execute on the edge. Scout runs three Strands agents in parallel (a constant "thinker" loop, a chat channel via Telegram and a web app, and a voice agent that was disabled for the demo). Most of the 17-minute talk is live demo, with little benchmark data. The speaker presents the approach as a stepping stone toward large VLA models that need no per-task fine-tuning.

## Key ideas
- **Treat a robot's preset actions as tools for an LLM agent** — The agent decides which robot policy to call from natural-language input. The speaker's framing is that a hardware tool works like a software tool, so the same agent loop applies. ([3:33](https://youtu.be/S6aSoQ6_u5A?t=213))
- **Setup is short: a robot is passed to an agent as a tool** — The speaker says the Strands example takes about five lines of code: import the agent, pass the robot as a tool, and give it an instruction such as 'pick up the red cube'. This assumes the robot already has that capability. ([4:29](https://youtu.be/S6aSoQ6_u5A?t=269))
- **Split one robot into several concurrent agents** — Scout runs a thinker agent that continuously assesses the environment, a communication agent for Telegram and web chat, and a voice agent. All three share the same robot tool. The voice agent was turned off because it kept responding to the speaker. ([5:39](https://youtu.be/S6aSoQ6_u5A?t=339))
- **Four-layer architecture from instruction to motion** — The top layer is the agent, which routes instructions and feeds observations back up. Below it sits a policy provider, then a back end (simulation or real hardware chip) where the policy runs, and finally the physical robot. The speaker stresses that the flow is bidirectional. ([6:46](https://youtu.be/S6aSoQ6_u5A?t=406))
- **Hybrid edge and cloud split** — Policy and VLA training happen in the cloud on AgentCore, which collects data and generates simulation data. Runtime policy calls happen on the edge for speed. Strands decides which side to call. ([9:07](https://youtu.be/S6aSoQ6_u5A?t=547))
- **Manual driving generates training episodes** — The speaker uses the same rig to steer the robot by hand. Each run becomes a training episode, and the logs of how it reasons about questions help improve the policy. ([12:50](https://youtu.be/S6aSoQ6_u5A?t=770))
- **Speaker's long-run view: VLA models could replace per-task training** — The speaker expects VLA models could eventually be as large and general as LLMs, so robots would need no fine-tuning on top of them. The current setup is presented as a stepping stone toward that. ([10:19](https://youtu.be/S6aSoQ6_u5A?t=619))

## Techniques
- **Robot as an agent tool** — Wrap each preset robot function or learned policy as a tool the agent can call. Describe each tool's purpose in the system prompt so the agent picks the right one from natural-language input. *When:* A robot already has preset skills or trained policies, and you want language-driven task selection without writing a new controller.
- **Concurrent specialized agents on one tool surface** — Run separate agent loops for background perception and reasoning, for chat or messaging, and for voice. All of them call the same robot tool. *When:* A long-running embodied or monitoring agent needs to keep assessing the environment while it also takes interactive requests.
- **Edge/cloud policy split** — Run training and data collection in the cloud and deploy policies to the device for low-latency execution. Let the agent choose which side handles each call. *When:* Control loops need fast local response, but training needs large-scale cloud compute.
- **Teleop for dataset creation** — Drive the robot manually through the same agent stack to record episodes, then use the recorded reasoning and actions to improve the policy. *When:* You need task-specific demonstration data for a robot that has no dataset yet.
- **Messaging-app control over cellular** — Attach a Telegram bot and a web app to the agent so the operator can send natural-language commands from anywhere. The robot connects over a 4G SIM. *When:* The operator is remote and needs to issue or check commands for a device that is on a mobile network.

## Numbers
- Latency: the agent takes about a second or two to respond to a spoken command over 4G, per the speaker's description of the demo. No measured figure is given. ([1:04](https://youtu.be/S6aSoQ6_u5A?t=64))
- Five lines of code to start: a Strands agent with the robot passed as a tool. ([4:29](https://youtu.be/S6aSoQ6_u5A?t=269))
- Three concurrent Strands agents on one robot (thinker, communication, voice). The voice agent was disabled during the demo. ([5:39](https://youtu.be/S6aSoQ6_u5A?t=339))
- The open-source framework supports more than 40 robots across eight categories. ([6:46](https://youtu.be/S6aSoQ6_u5A?t=406))
- Four architecture layers: agent, policy provider, back end (simulation or hardware), and robot. ([6:46](https://youtu.be/S6aSoQ6_u5A?t=406))
- Brain model: Claude Opus 4.8 via Strands; voice output from OpenAI Realtime. ([14:08](https://youtu.be/S6aSoQ6_u5A?t=848))

## Hot takes
- VLA models could become as large and general as LLMs, so per-task robot training would no longer be needed. The speaker calls the current approach a 'stepping stone' to that.
- Language-driven agents on top of robot policies are a new generation of robot, separate from traditional pre-programmed robot training.

## Tools mentioned
Strands Agents (agent SDK), Amazon Bedrock AgentCore, Claude Opus 4.8, OpenAI Realtime (voice), Telegram, Raspberry Pi, VLA models, 4G SIM

## Relevance to our work
- **agentos** (1/3): Parallel specialized agents (background thinker, chat channel, voice) sharing one tool layer is a pattern AgentOS's multi-agent work could borrow. The talk gives no measurements, so the fit is weak. → *Read the Strands multi-agent docs to see how the talk's thinker and chat agents share one tool surface, and compare with the AgentOS subagent design.*
- **prosharness** (1/3): ProsHarness has phone-driven approvals. The talk runs a long-lived agent that accepts commands from Telegram while the operator is away. → *Consider whether ProsHarness' phone approval flow should accept commands over a messaging channel, as this demo does with Telegram, instead of only approving requests.*
- **general** (1/3): The talk's architecture sketch (agent to policy to back end to hardware) is a clear way to describe agent-to-actuator systems. The rest is demo.
