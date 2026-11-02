# OpenClaw in Your Hand: Building a Physical AI Terminal - Lech Kalinowski, Callstack

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `akk6KRlcwW4` · [watch](https://youtu.be/akk6KRlcwW4) · **date:** 2026-07-18 · **length:** 24:36 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Lech Kalinowski · **orgs:** Callstack
- **topics:** local-ai, inference-serving, product-ux · **tags:** openclaw, esp32, dgx-spark, physical-ai, hardware, e-paper, oled, rpg, thin-client, openai-compatible-proxy, gpt-oss-120b, embedded

> Callstack engineer Lech Kalinowski builds a handheld text-terminal for OpenClaw and local LLMs on an ESP32, with a thin-client design backed by a 120B model on a DGX Spark. Mostly a hardware showcase with useful field notes.

## Summary
The speaker, Lech Kalinowski of Callstack, describes a handheld AI terminal built over about three months. It pairs a small OLED screen (live typing) with an e-paper screen (slow, stable display of the final output), driven by an ESP32 dual-core microcontroller. The device is a thin client: a backend on a DGX Spark runs the agent work through OpenClaw and serves an open-source 120B model. Because the MCU has little memory, rendering uses pre-allocated one-bit images with no markdown engine and no malloc. The talk spends a lot of time on hardware problems (I2C pull-ups, a silent GPIO failure, a regulator that damaged the display, and a noisy cheap encoder). The most unusual feature is an RPG mode, where the LLM generates NPCs, worlds and maps that are converted to one-bit assets. The speaker closes with three takeaways and a demo video. Most of the content is a project showcase, with little new detail on LLM serving.

## Key ideas
- **Motivation: a remote controller for an OpenClaw instance on a DGX Spark, with a dual-display design** — The speaker wanted a physical device to talk to an LLM. An OLED gives fast typing and an e-paper screen gives a readable, energy-efficient final view. Together they make a low-power terminal. ([1:41](https://youtu.be/akk6KRlcwW4?t=101))
- **The device is a thin client; the heavy work runs on a backend** — Firmware on the ESP32 handles input and display. A separate backend on the DGX Spark handles the agent work with OpenClaw and the LLM. The MCU does not run models. ([4:52](https://youtu.be/akk6KRlcwW4?t=292))
- **On a microcontroller, render from pre-allocated one-bit images** — Pages live in fixed buffers in memory. There is no markdown engine and no malloc on the MCU side. The speaker says this is needed because of the memory limits. ([6:25](https://youtu.be/akk6KRlcwW4?t=385))
- **Serve an open 120B model behind an OpenAI-style proxy** — The speaker ran a 120B open-source model on NVIDIA's serving stack and exposed an OpenAI-style API. Other open models did not match the OpenAI API closely enough, so the proxy was needed to make them work. ([8:56](https://youtu.be/akk6KRlcwW4?t=536))
- **Power and hardware issues dominated the build** — Silent I2C failure without external pull-ups, a GPIO 13 failure that needed a port move, and a regulator that damaged the display (replacement parts took weeks). Cheap encoders added rotational noise that needed pull-ups and capacitors. ([10:29](https://youtu.be/akk6KRlcwW4?t=629))
- **RPG mode uses the LLM for world-building** — The LLM generates NPCs, worlds, maps and skills. The images are converted to one-bit matrices so the MCU can display them. The speaker built four worlds and a mood system. ([13:22](https://youtu.be/akk6KRlcwW4?t=802))
- **Design for fallbacks so the device stays usable** — If the OLED fails, the e-paper still works. If the keyboard fails, the encoder works. If Wi-Fi drops, the local shell still runs. ([14:52](https://youtu.be/akk6KRlcwW4?t=892))
- **Takeaways: match displays to the job, LLMs are too heavy for tiny MCUs, and context matters more than numbers** — The speaker says no current model runs on very small MCUs, so LLM work must go to a backend. The speaker also says narrative and context matter most for LLM products. ([17:22](https://youtu.be/akk6KRlcwW4?t=1042))

## Techniques
- **Thin-client MCU with a heavy backend** — Keep firmware to input and display only. Put agent orchestration and model calls on a server, and expose it to the device over the network. *When:* When the device has very little RAM or compute and must still feel interactive.
- **Pre-allocated one-bit page buffers** — Store each screen as a fixed one-bit bitmap in memory. Avoid runtime allocation and any markup or layout engine on the MCU. *When:* For text or image output on a small MCU with a monochrome display.
- **Dual-display split by job** — Use a fast OLED for live input and an e-paper panel for a stable, low-power final view that updates only on commit. *When:* When you need fast text entry and a readable, energy-efficient output on the same device.
- **OpenAI-style proxy in front of open models** — Serve an open model with a fast inference engine and wrap it in an OpenAI-compatible endpoint, so clients written for the OpenAI API can use it. *When:* When existing agent tooling expects the OpenAI API and the open model's native API does not match it.
- **Graceful degradation across hardware parts** — Give each input and output a fallback path, so the device keeps working if one part fails. *When:* For hardware prototypes where parts are fragile or unreliable.

## Numbers
- About 130 commits over roughly three months of work ([15:48](https://youtu.be/akk6KRlcwW4?t=948))
- Two displays, four modes, four RPG worlds, and 16 character classes ([15:48](https://youtu.be/akk6KRlcwW4?t=948))
- Powered by a single lithium-polymer cell ([15:48](https://youtu.be/akk6KRlcwW4?t=948))
- Backend serves an open-source 120 billion parameter model ([8:56](https://youtu.be/akk6KRlcwW4?t=536))
- MCU is an ESP32 dual-core microcontroller ([7:56](https://youtu.be/akk6KRlcwW4?t=476))
- A GPIO 13 silent failure and an I2C issue without external pull-ups ([10:29](https://youtu.be/akk6KRlcwW4?t=629))

## Hot takes
- Match displays to the job. There are plenty on the market.
- LLMs are still too heavy for tiny MCUs, so the model has to run on a backend.
- Context and narrative matter more than numbers in LLM products.

## Tools mentioned
OpenClaw, ESP32, NVIDIA DGX Spark, NVIDIA serving stack (auto-caption: 'Tensor Earth'), OLED display, e-paper display

## Relevance to our work
- **agentos** (1/3): The speaker found that not all open models match the OpenAI API, so the serving side needed an OpenAI-style proxy. This touches AgentOS's proxy and InferCraft serving, but only lightly. → *Check that InferCraft's OpenAI-compatible endpoint works with open models that do not fully match the OpenAI API, and test it with a non-OpenAI-style model.*
