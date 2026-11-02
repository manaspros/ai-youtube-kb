# Generative Video at the Speed of Light — Keegan McCallum, uRun

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Xln-On3syJk` · [watch](https://youtu.be/Xln-On3syJk) · **date:** 2026-09-18 · **length:** 8:43 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Keegan McCallum · **orgs:** uRun
- **topics:** voice-multimodal, inference-serving, infra-cost-scaling · **tags:** generative-video, real-time-inference, long-horizon-generation, distillation, webrtc, streaming-pipelines, world-models, video-to-video, avatars, react-component, mcp, cost-efficiency

> Keegan McCallum (uRun) argues generative video is improving on efficiency and long-horizon generation as well as quality, and describes the infra needed for real-time interactive video apps.

## Summary
The speaker, founder of uRun (an inference provider for interactive media), says generative video is usually judged only on quality, but efficiency and long continuous generation are improving fast too. He demos Helios, a distilled version of Wan 2.1 14B that uRun serves, which runs in real time at roughly last year's frontier quality for about 1/100th of the cost. He cites at least 40 real-time or long-horizon video models released this year and frames the cost as about $10 for roughly 3 hours of continuous video. He lists use cases such as webcam "magic mirror" try-ons, accessibility for visual thinkers, and steering shots in real time instead of paying about $10 per minute on a prompt-and-keyframe slot machine. On the build side, he says real-time video apps need GPUs spread globally, WebRTC/ICE/TURN, and multi-model streaming pipelines synced to user controls every frame. uRun's answer is a React component plus an async Python runtime, with a CLI and MCP server so agents can build on it. The talk is part technical overview and part hiring and product pitch.

## Key ideas
- **Video progress has two axes, not one: quality and efficiency/long-horizon generation. Efficiency is the axis the speaker says is moving fastest.** — He says the field talks mostly about quality, with a historical progression from the 2023 spaghetti clip through Sora and Sora 2 to Seedance this year. He argues the efficiency axis is being missed. ([0:12](https://youtu.be/Xln-On3syJk?t=12))
- **Helios is a distilled Wan 2.1 14B that gives near-frontier-of-last-year quality in real time, with continuous long generations.** — Shown side by side with a clip that took minutes to generate, the real-time one is comparable or slightly weaker on motion per the speaker's own comparison. The speaker says the real-time clip costs about 1/100th as much. ([1:21](https://youtu.be/Xln-On3syJk?t=81))
- **Many techniques are spreading across model types, not one model: world models with fine camera control, avatar models, and real-time video-to-video transforms.** — He counts at least 40 models with real-time and long-horizon capability released this year. He frames it as a general pattern, not a single model release. ([2:28](https://youtu.be/Xln-On3syJk?t=148))
- **Real-time control changes the cost model from slot machine to steering.** — The current workflow is a prompt plus keyframes at about $10 per minute of output, with little control during generation. Real-time models can be steered in under a second while they generate, so users get the shot they want without re-rolling. ([4:35](https://youtu.be/Xln-On3syJk?t=275))
- **Real-time video apps need infrastructure that most model-serving stacks don't cover: global GPU placement, WebRTC with ICE/TURN, and per-frame sync with user controls.** — Interactive use means choosing which GPU serves which user region, streaming over WebRTC, and wiring several models into continuous pipelines. Controls must line up with each frame to keep the stream smooth. ([6:03](https://youtu.be/Xln-On3syJk?t=363))
- **Expose interactive video as a frontend component plus an async runtime, and make it agent-accessible through a CLI and MCP server.** — The proposal is a React component for apps and a programmable Python runtime for async multi-model pipelines. The speaker argues that in 2026 apps need software factories and agent-facing interfaces, not only platforms. ([7:29](https://youtu.be/Xln-On3syJk?t=449))

## Techniques
- **Distill a large video model for real-time serving** — Use a distilled small variant (Helios from Wan 2.1 14B) to trade a little motion quality for real-time frame rates and much lower cost per second of video. *When:* When interactive latency or per-second cost matters more than peak fidelity.
- **Real-time steering instead of prompt-and-reroll** — Let users change prompts, camera, or viewport while the model is still generating, rather than generating full clips from one prompt and keyframes. *When:* For creative or interactive tools where iteration cost dominates, such as content creation or agent output monitoring.
- **Multi-model streaming pipeline with per-frame control sync** — Chain several models (for example avatar plus video-to-video) in an async pipeline, and tie user control inputs to each generated frame. *When:* For live interactive media apps such as magic mirrors, avatars, or agent visualization.
- **Wrap real-time video as a React component plus Python runtime** — Expose the streaming model as a drop-in component on the front end, and keep pipeline logic in an async Python runtime on the back end. *When:* When product teams need to add live generated video to an existing web app without building the streaming stack.
- **Agent-facing access via CLI and MCP server** — Give agents a CLI or MCP server so they can build and run these video apps themselves. *When:* When the goal is to let coding agents create real-time media applications.

## Numbers
- Real-time Helios clip generated at about 1/100th of the cost of the minutes-long comparison clip ([1:21](https://youtu.be/Xln-On3syJk?t=81))
- At least 40 models with real-time or long-horizon capabilities released this year ([2:28](https://youtu.be/Xln-On3syJk?t=148))
- Helios released in March ([2:28](https://youtu.be/Xln-On3syJk?t=148))
- About $10 buys about 3 hours of continuous generated video with most of these models; $50 buys about 15 hours ([2:28](https://youtu.be/Xln-On3syJk?t=148))
- Prompt-and-keyframe workflow costs about $10 per minute of output ([4:35](https://youtu.be/Xln-On3syJk?t=275))
- Real-time models can be steered in under a second while generating ([4:35](https://youtu.be/Xln-On3syJk?t=275))

## Hot takes
- In 2026 we don't just need platforms; we need software factories and ways for agents to interact with these.
- Video generation is moving from slot-machine prompting to real-time steering, and efficiency is improving as fast as quality.
- Most of the field discusses video quality, while efficiency and long-horizon generation are the underrated axes.

## Tools mentioned
Helios, Wan 2.1 14B, WebRTC, ICE, TURN, React, Python async runtime, MCP, CLI, Sora, Sora 2, Seedance, Gemini Omni, LemonSlice, Claude Code

## Relevance to our work
- **agentos** (1/3): InferCraft serves models on one GPU with latency-sensitive scheduling; this talk is a reference for per-frame streaming latency and real-time multi-model pipelines, but it is a video-specific case. → *Skim how real-time streaming pipelines are built (WebRTC plus per-frame sync) if InferCraft ever needs a latency budget for streamed outputs; no change to build now.*
