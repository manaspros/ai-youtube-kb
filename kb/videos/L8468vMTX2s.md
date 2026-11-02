# Goodbye AI Cloud Bills... Exo Runs AI on Your Own Devices

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `L8468vMTX2s` · [watch](https://youtu.be/L8468vMTX2s) · **date:** 2026-01-02 · **length:** 4:10 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed Better Stack host · **orgs:** Better Stack, ExoLabs, Apple
- **topics:** local-ai, inference-serving, infra-cost-scaling · **tags:** exo, local-inference, mlx, apple-silicon, model-sharding, tensor-parallelism, pipeline-parallelism, rdma, thunderbolt-5, heterogeneous-cluster, openai-compatible-api, self-hosting

> Short Better Stack overview of EXO, an open-source tool that auto-discovers devices on a LAN and shards one model across them; the demo runs on a single Mac, so the multi-device claims are unverified.

## Summary
The host introduces EXO as an open-source tool that builds a peer-to-peer AI cluster from devices the user already owns, such as MacBooks and Raspberry Pis, to cut cloud inference costs and keep data local. EXO autodiscovers machines on the local network, measures bandwidth, latency and available memory, and splits a model across devices using tensor and pipeline parallelism. Mixed hardware is described as workable: macOS GPUs run through Apple's MLX, while Linux nodes fall back to CPU. The live demo runs on a single M4 Pro, launching EXO with no config and sending one prompt to an OpenAI-style endpoint, so it does not show a distributed run. The host also covers Thunderbolt 5 RDMA between supported Macs and cites secondhand community benchmarks for large models. The video is light on reproducible steps and leans on hype, so treat the numbers as leads to verify rather than facts.

## Key ideas
- **EXO is pitched as a peer-to-peer AI cluster built from everyday devices, aimed at cutting cloud inference bills and keeping data on local hardware.** — The motivation is cost, control of data, and room to experiment. Framed as pooling existing machines (MacBooks, Raspberry Pis) rather than buying cloud GPUs. ([0:00](https://youtu.be/L8468vMTX2s?t=0))
- **Devices are discovered automatically on the LAN, with no manual networking or IP configuration.** — The demo claims no config files or IP addresses are needed; the first run is slow while setup completes. ([0:00](https://youtu.be/L8468vMTX2s?t=0))
- **EXO measures each node's bandwidth, latency and free memory, then decides how to split the model across nodes using tensor and pipeline parallelism.** — The claim is that this gives faster inference and pooled memory, which is how very large models such as DeepSeek V3 could run locally. The video does not show the placement logic. ([0:53](https://youtu.be/L8468vMTX2s?t=53))
- **Mixed hardware is supported, with uneven capability per platform: macOS GPUs via Apple's MLX, Linux nodes on CPU only.** — The example is a MacBook Pro M4 Pro paired with a Raspberry Pi running on CPU. The host says the goal is pooling resources, not peak performance. ([0:53](https://youtu.be/L8468vMTX2s?t=53))
- **The live demo runs on one Mac only, so it does not show distributed inference.** — The host launches EXO, sends one prompt to an OpenAI-style endpoint and says the point is that it works, not speed. Additional machines would appear automatically, but none were added on camera. ([2:02](https://youtu.be/L8468vMTX2s?t=122))
- **On supported Apple hardware, EXO uses RDMA over Thunderbolt 5 for GPU-to-GPU transfers that skip the CPU, which lowers latency and makes linked Macs act more like one system.** — Described briefly, with no setup steps or measurements shown. ([2:02](https://youtu.be/L8468vMTX2s?t=122))
- **Wired links are said to scale better than Wi-Fi, and power draw rises with more machines but stays small next to cloud GPUs.** — This is a qualitative claim from the host with no measurements shown in the video. ([3:10](https://youtu.be/L8468vMTX2s?t=190))
- **The host's verdict: running serious models locally is practical only if you already own several Macs, and the setup is not perfect.** — Stated caveat: most viewers do not have a cluster of MacBooks, so the value depends on existing hardware. ([3:10](https://youtu.be/L8468vMTX2s?t=190))

## Techniques
- **Zero-config LAN cluster for local inference** — Install and launch EXO on each machine on the same local network. Let it autodiscover peers (the first run is slow), then send requests to the local OpenAI-style endpoint. The video shows only the launch and one prompt; no exact install commands, ports, flags or config keys are shown, so check the EXO repo before reproducing. *When:* You have spare Macs or mixed boxes on one LAN and want one shared local model without hand-written networking or IP config.
- **Shard the model by measured node capacity** — EXO measures bandwidth, latency and free memory on each node, then splits the model across nodes using tensor and pipeline parallelism. The video does not explain how the split is chosen. *When:* A model is too large for one machine's memory, and the nodes differ in capability (for example, Macs plus a Pi).
- **Thunderbolt 5 RDMA between Macs** — On supported Apple hardware, connect the machines with Thunderbolt 5 so EXO can use RDMA for GPU-to-GPU transfers. The host says wired links beat Wi-Fi for cluster performance, but shows no setup or measurements. *When:* Several Apple Silicon machines need low-latency cross-machine inference, and Wi-Fi is the bottleneck.

## Numbers
- Four M3 Ultra Mac Studios running Qwen3 235B at about 32 tokens/s, from a community benchmark the host attributes to 'Jeff Grealing's papers' (auto-caption, name unverified). ([3:10](https://youtu.be/L8468vMTX2s?t=190))
- ExoLabs reportedly ran DeepSeek V3 671B on eight M4 Mac minis. The memory figure is garbled in captions ('five 12GB pulled memory'), likely 512 GB pooled memory, so verify against the source before quoting. ([3:10](https://youtu.be/L8468vMTX2s?t=190))
- Wired (Thunderbolt) clusters scale better than Wi-Fi. No measurement given. ([3:10](https://youtu.be/L8468vMTX2s?t=190))
- Demo is a single M4 Pro, so the video contains no multi-device throughput or latency measurements of its own. ([2:02](https://youtu.be/L8468vMTX2s?t=122))

## Hot takes
- The 'Goodbye AI Cloud Bills' framing is hype. The only live demo runs on one Mac, so the multi-device sharding and cluster claims are not shown.
- The host admits the demo's point is that 'it works', not speed, and the throughput figures are secondhand from community papers.
- Mixed hardware is presented as performing acceptably, but the only mixed example is a Pi on CPU. No numbers support that.
- Practical value is limited to people who already own several Apple Silicon machines, as the host concedes.

## Tools mentioned
EXO (open-source peer-to-peer inference cluster, ExoLabs), Apple MLX, OpenAI-style chat endpoint (served by EXO), Thunderbolt 5 RDMA, DeepSeek V3 671B (cited community run), Qwen3 235B (cited community run), MacBook Pro M4 Pro (demo machine), Mac Studio M3 Ultra (cited benchmark), Mac mini M4 (cited ExoLabs run), Raspberry Pi (CPU node)

## Relevance to our work
- **agentos** (1/3): InferCraft plans vLLM plus Ray Serve on one RTX 5090. EXO is a different approach to pooling heterogeneous devices, with its own sharding policy. Relevant only as a reference for multi-node placement. → *Skim EXO's sharding and placement code (tensor/pipeline split based on measured bandwidth, latency and memory) as a reference for any future multi-node InferCraft design. Do not adopt it now.*
