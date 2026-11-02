# Build an AI Video Generator Like Sora (with ComfyUI)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `DxvC2B0eVkc` · [watch](https://youtu.be/DxvC2B0eVkc) · **date:** 2025-11-02 · **length:** 10:58 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** Andrus · **orgs:** Better Stack, DigitalOcean
- **topics:** local-ai, voice-multimodal, dev-tools · **tags:** comfyui, video-generation, wan, omnigen2, gpu-cloud, digitalocean, ssh-tunnel, viewcomfy, text-to-image-to-video, comfy-cli

> Step-by-step tutorial for running ComfyUI on a rented DigitalOcean GPU droplet, chaining an OmniGen2 text-to-image workflow into a WAN video workflow, and serving the export through ViewComfy over SSH tunnels.

## Summary
Better Stack's Andrus walks through building a text-to-video generator on ComfyUI, because his M2 MacBook has no CUDA. He rents the cheapest DigitalOcean GPU Droplet (RTX 4000 Ada), installs ComfyUI with comfy-cli, and reaches the web UI on port 8188 through an SSH tunnel. He loads the sample WAN video workflow, downloads its models into the folder paths the UI reports, and finds that text-to-video alone gives poor cartoon output. Feeding in a source image from an OmniGen2 text-to-image workflow works better, but the combined graph fails until both text encoders share one prompt string node. He exports the workflow as API JSON and runs it in ViewComfy, a Next.js playground on port 3000. The result is a working but low-fidelity pipeline on a low-end GPU, and he notes that more steps and a bigger server would improve it.

## Key ideas
- **Visual generative models need a GPU, so the speaker rents a remote GPU Droplet instead of running on a Mac with no CUDA support.** — Cheapest DigitalOcean GPU Droplet with an NVIDIA RTX 4000 Ada. The speaker warns that the droplet keeps billing when powered off. ([0:59](https://youtu.be/DxvC2B0eVkc?t=59))
- **Use snapshot, destroy and recreate to avoid paying for an idle GPU droplet.** — Save a snapshot, destroy the instance after use, and recreate it from the snapshot the next time it is needed. ([0:59](https://youtu.be/DxvC2B0eVkc?t=59))
- **Keep ComfyUI on the server and reach it through an SSH tunnel rather than exposing it publicly.** — ComfyUI listens on localhost:8188 on the server. The tunnel must be created while the server is running on that port, so the speaker stops ComfyUI, opens the tunnel, then restarts it in the background. ([2:07](https://youtu.be/DxvC2B0eVkc?t=127))
- **Model files must go into the exact folder paths the workflow expects, and the workflow's missing-model warning is the checklist.** — The WAN sample workflow flags missing models. Each model's folder path (for example diffusion models, then a VAE path) is copied into the comfy CLI download prompt. The warning clears after each download. ([3:15](https://youtu.be/DxvC2B0eVkc?t=195))
- **Text-to-video alone gave poor cartoon results, so the speaker chained text-to-image into image-to-video.** — The realistic video model did not handle cartoon prompts well without a source image. The OmniGen2 text-to-image template produced good source frames, which were then fed to the video workflow. ([5:20](https://youtu.be/DxvC2B0eVkc?t=320))
- **Combining two workflows broke because each has its own text encoder, so outputs cannot be shared directly.** — Reusing one prompt output in both branches caused a matrix multiplication error in the video sampler. A common positive and negative string node, bound to each prompt input, fixed it while each encoder still processed its prompt separately. ([6:30](https://youtu.be/DxvC2B0eVkc?t=390))
- **A ComfyUI workflow can be exported as API JSON and served from a custom app without rebuilding the graph.** — The speaker imports the exported JSON into ViewComfy, a Next.js app that acts as a playground for ComfyUI workflows. Repeated runs stack their outputs in the UI. ([7:30](https://youtu.be/DxvC2B0eVkc?t=450))
- **Output quality is limited by the cheap GPU, and the speaker sets expectations accordingly.** — The combined image-plus-video run took about two minutes on the low-end droplet and produced a janky video. He says more sampling steps and a stronger server would improve results. ([7:30](https://youtu.be/DxvC2B0eVkc?t=450))

## Techniques
- **Remote GPU with SSH-tunneled ComfyUI** — Install pip3 on the GPU droplet, then pip install comfy-cli. Run `comfy install`, then `comfy launch`; ComfyUI serves on localhost:8188. Stop the server, create an SSH tunnel from the laptop to port 8188 (the exact tunnel command is shown on screen and not spoken), then restart ComfyUI in the background and open localhost:8188 in the local browser. Keep the server running while the tunnel is open. *When:* Running a GPU-heavy generative UI from a machine without CUDA, without exposing the UI to the public internet.
- **Downloading models into the path the workflow expects** — Open the template, note the folder path of each model (for example the diffusion models folder, and the VAE folder), and click Copy URL on the model. On the server run the comfy CLI download command with that URL. It prompts for a folder path (type the memorized path), then a base model name (can be left blank), and keeps the file name. Refresh the UI and confirm the missing-model warning is gone. *When:* Setting up a fresh ComfyUI server from a sample or template workflow.
- **Chain text-to-image into image-to-video** — Run an OmniGen2 text-to-image template to produce a source frame. Select the image-output node and connect it to the image input of the video workflow in place of the original image input. Copy the nodes from the image workflow into the video workflow. *When:* Stylized or cartoon video where a text-only video model gives weak results. Use a source image to anchor style.
- **Shared prompt node across two text encoders** — Do not reuse one prompt conditioning output in both branches; each model has its own text encoder. Create one common positive and one common negative string node, then bind each text input of the two prompt nodes to the matching string node. Each encoder still encodes its own prompt, and one edit updates both branches. *When:* Merging workflows whose models use different text encoders, to avoid tensor shape errors such as the matrix multiplication failure the speaker hit.
- **Export ComfyUI workflow as API JSON and run it in ViewComfy** — Export the finished workflow in ComfyUI's API format and download the JSON. Clone the ViewComfy repo onto the server, install its dependencies, and run the Next.js app on port 3000. Open a second SSH tunnel to port 3000, import the saved workflow JSON in the app, give it a name and save, then run it from the playground. *When:* Wrapping a ComfyUI graph in a simple web front end without writing a custom API client.
- **Cost control for rented GPU droplets** — Droplets bill while powered off, so snapshot the droplet when done, destroy the instance, and recreate it from the snapshot next session. *When:* Any occasional GPU workload on a cloud provider that charges for stopped instances.

## Numbers
- Cheapest DigitalOcean GPU Droplet used, with an NVIDIA RTX 4000 Ada. Price not stated. ([0:59](https://youtu.be/DxvC2B0eVkc?t=59))
- Default WAN sample workflow takes about seven minutes to run on the droplet. ([4:07](https://youtu.be/DxvC2B0eVkc?t=247))
- A smaller-resolution cartoon prompt run took about one minute, with poor results. ([5:20](https://youtu.be/DxvC2B0eVkc?t=320))
- Combined OmniGen2 image plus WAN video run took about two minutes on the low-end droplet. ([7:30](https://youtu.be/DxvC2B0eVkc?t=450))
- ComfyUI web UI is on port 8188; ViewComfy app is on port 3000. ([2:07](https://youtu.be/DxvC2B0eVkc?t=127))

## Hot takes
- Text-to-video models are good at realistic footage but weak at cartoon style without a source image.
- Cloud GPU droplets keep charging while powered off, so snapshot and destroy between sessions.
- The speaker calls the output janky and says the stack needs more steps and a bigger server to look good.
- Sora and Veo are said to have far more GPUs; the video frames it as a hobbyist setup, not a competitor.

## Tools mentioned
ComfyUI, comfy-cli, DigitalOcean GPU Droplets, NVIDIA RTX 4000 Ada, WAN video generation model (speaker says 2.25B parameters, auto-caption), OmniGen2, ViewComfy, Next.js, pip3, SSH

## Relevance to our work
- **agentos** (1/3): Shows ComfyUI media generation on a rented GPU, which is outside AgentOS's LLM serving path (InferCraft on a local RTX 5090). Only the cost and tunnel patterns could transfer. → *If InferCraft ever needs burst GPU capacity, reuse the snapshot-destroy-recreate pattern and keep GPU services bound to localhost behind SSH tunnels.*
