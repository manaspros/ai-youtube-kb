# Take Back Your PRIVACY and Run DeepSeek on EC2 in 5 Minutes!

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `DCWtyd9AW4w` · [watch](https://youtu.be/DCWtyd9AW4w) · **date:** 2025-11-02 · **length:** 5:47 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** AWS, DeepSeek, Ollama, Better Stack
- **topics:** local-ai, infra-cost-scaling, dev-tools · **tags:** deepseek, ollama, open-webui, ec2, docker, nginx, self-hosted-llm, q4_k_m, privacy, amazon-linux

> Step-by-step tutorial for running distilled DeepSeek (Qwen-based) models on a CPU-only AWS EC2 instance using Ollama, Open WebUI in Docker, and an Nginx reverse proxy, framed around keeping prompts private.

## Summary
The video walks through a private self-hosted setup for DeepSeek-family models on AWS EC2. The host launches an Amazon Linux instance (a non-GPU r5.xlarge, since the G4DN type was blocked for his account) with a 20 GB disk and HTTP/HTTPS ports open. He installs Docker, runs Ollama in a container with a volume and port 11434 published, and pulls two distilled Qwen-based DeepSeek models (1.5B and 7B) quantized to Q4_K_M. Open WebUI runs in a second container with port 8080 mapped to 3000, and Nginx forwards port 80 to localhost:3000. The result is a web login page reachable from the browser, where the user signs up and queries the models. The host acknowledges the setup is slow without a GPU and that a larger model on a GPU instance would work better. No benchmarks or latency figures are given; the value is the deployment sequence and the privacy motivation.

## Key ideas
- **Self-hosting is pitched as the fix for privacy worries about hosted DeepSeek web UIs.** — The motivation is that people avoid the vendor's web UI over data concerns, so the host runs the model on infrastructure the user controls. The claim is about where prompts go, not about model quality. ([0:00](https://youtu.be/DCWtyd9AW4w?t=0))
- **The host uses a CPU-only instance on purpose, because the GPU instance type was blocked on his account.** — He tried G4DN, got an AWS error, and fell back to an r5.xlarge with no GPU. He calls the result slow but acceptable for a tutorial. ([0:00](https://youtu.be/DCWtyd9AW4w?t=0))
- **Ollama runs in Docker as the model server, with its models kept in a named volume.** — The container is started detached, with a volume for model storage, port 11434 published, and the image pulled from Ollama. A curl to the port should return that Ollama is running. ([1:00](https://youtu.be/DCWtyd9AW4w?t=60))
- **The models are quantized Q4_K_M, presented as a middle ground between FP16 and Q8_0.** — He says FP16 gives the best results but uses the most resources, Q8_0 uses much less with worse results, and Q4_K_M sits between them. This is his explanation, not a measured comparison. ([2:23](https://youtu.be/DCWtyd9AW4w?t=143))
- **Open WebUI runs as a second container and is the chat front end for the Ollama models.** — Container port 8080 is mapped to host port 3000, with a host-gateway entry and a volume, and the container is named open-webui in the video (he says olama webui). ([3:45](https://youtu.be/DCWtyd9AW4w?t=225))
- **Nginx is used instead of Caddy as a reverse proxy because Caddy needs extra steps on Amazon Linux.** — Nginx forwards port 80 to localhost:3000. The config is checked before enabling and starting the service. He prefers Caddy but chose the simpler path for this video. ([3:45](https://youtu.be/DCWtyd9AW4w?t=225))
- **Browser access over the instance's public address requires switching the URL scheme from https to http.** — The site fails on https, so the host switches the address to http to reach the login page. He does not explain this in detail, and it means the traffic is unencrypted. ([5:06](https://youtu.be/DCWtyd9AW4w?t=306))
- **The host is open that this setup is a starting point and a larger model on a GPU instance would do better.** — He says the 1.5B and 7B distills on CPU are a baseline, and the same steps would work with a bigger model and a GPU instance. No throughput or latency numbers are shown. ([5:06](https://youtu.be/DCWtyd9AW4w?t=306))

## Techniques
- **Run Ollama in Docker with a persistent volume and a published port** — Start the ollama/ollama image detached (-d), mount a named volume for model storage, publish port 11434, and name the container ollama. Verify with docker ps and curl localhost:11434, which should respond that Ollama is running. Pull models with docker exec into the container. *When:* Self-hosting open-weight models on a Linux VM where you want the model server isolated and its models to survive container restarts.
- **Open WebUI as a front end for a Docker-hosted Ollama** — Run the Open WebUI image detached, publish container port 8080 to host port 3000, add a host-gateway mapping so the container can reach the host's Ollama port, mount a volume, and name the container open-webui. Then create a user account on first load. *When:* When you want a chat interface and multi-user login in front of local models without writing a client.
- **Nginx reverse proxy from port 80 to a local app port** — Install nginx, add a server block inside the include section of the config that proxies location / to localhost:3000, check with nginx -t, then enable and start the service. Open port 80 in the instance's security group. *When:* Exposing a container's web UI on the default HTTP port of a public VM. The video skips TLS, so add certificates before using it with real data.
- **Pick a quantization level by tradeoff** — The host's rule of thumb: FP16 for best quality at highest memory cost, Q8_0 for lower memory with some quality loss, Q4_K_M as the middle option. Choose the tag when pulling the Ollama model. *When:* Fitting a model into limited RAM or VRAM when you accept some quality loss.

## Numbers
- Instance is an r5.xlarge (written as R5XL) with no GPU, chosen after the G4DN type was refused. ([0:00](https://youtu.be/DCWtyd9AW4w?t=0))
- Root volume set to 20 GB. ([0:57](https://youtu.be/DCWtyd9AW4w?t=57))
- Ollama published on port 11434; Open WebUI maps container 8080 to host 3000; Nginx forwards 80 to 3000. ([2:23](https://youtu.be/DCWtyd9AW4w?t=143))
- Two models installed: the 1.5B and 7B distilled variants, both at Q4_K_M quantization. No tokens/sec or latency measured. ([2:23](https://youtu.be/DCWtyd9AW4w?t=143))

## Hot takes
- The privacy framing is only partly addressed: the setup uses plain HTTP after an https-to-http switch, so traffic is unencrypted. The video does not mention this as a risk.
- Calling a CPU-only r5.xlarge workable for a DeepSeek model is a weak claim; the host admits it is slow and gives no measurements.
- The video is a basic deployment walkthrough with no benchmarks, cost figures, or security hardening. It is useful as a reproducible sequence and not much beyond that.

## Tools mentioned
AWS EC2, Amazon Linux, Docker, Ollama, Open WebUI, Nginx, Caddy (mentioned, not used), DeepSeek (distilled models, Qwen-based per the speaker), Qwen (distilled base for the 1.5B and 7B models), vim / nano

## Relevance to our work
- **agentos** (1/3): AgentOS's InferCraft runs vLLM and Ray Serve on one RTX 5090. This video covers a CPU-only Ollama baseline on EC2 with no serving-level detail, so it is a weak comparison point for the self-hosted inference story. → *Read only if we want a minimal Ollama baseline for comparing against vLLM throughput and latency in InferCraft benchmarks.*
