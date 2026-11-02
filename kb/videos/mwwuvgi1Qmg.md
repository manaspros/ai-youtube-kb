# Why Apple's New AI Model is TOO GOOD to Be True

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `mwwuvgi1Qmg` · [watch](https://youtu.be/mwwuvgi1Qmg) · **date:** 2026-01-02 · **length:** 6:26 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Unnamed Better Stack host · **orgs:** Apple, DigitalOcean, Hugging Face, Better Stack
- **topics:** models-research, inference-serving · **tags:** image-generation, video-generation, normalizing-flow, autoregressive, diffusion-alternative, apple, open-source, jacobi-iteration, h200, research-release

> Better Stack walkthrough of Apple's open-source STARFlow image/video model (autoregressive normalizing flow), with a single-H200 test run; the image checkpoint works, but there is no video checkpoint and no on-device path.

## Summary
The host introduces STARFlow (Scalable Auto-regressive Flow), Apple's open-source image and video generation repo, released with code last month after being announced in June. The model is a hybrid: autoregressive prediction applied to normalizing-flow layers, which map Gaussian noise to an image in one forward pass rather than many diffusion denoising steps. The host claims parallel Jacobi iterations make it up to 15x faster, especially for video, and that invertibility allows editing part of an image while keeping the rest fixed. He rents a DigitalOcean GPU droplet with one H200, installs from the repo, downloads the Hugging Face checkpoint, and generates cat, chicken and polar-bear images. Outputs are 256x256 with visible artifacts, and only the image checkpoint is public, so video could not be tested. He concludes it needs Python, PyTorch and a GPU, is not optimized for Apple Silicon or Metal, and is a research release rather than an iPhone feature. The speed and editing claims are reported from Apple's materials, not measured by the host.

## Key ideas
- **STARFlow is a hybrid: autoregressive prediction runs over normalizing-flow layers, not over pixels or tokens directly.** — The host frames it as two models in one repo, one for image and one for video. Flow layers are invertible functions that turn a simple Gaussian distribution into an image. Because they are invertible, the process can run in both directions. ([0:00](https://youtu.be/mwwuvgi1Qmg?t=0))
- **Flow models generate in a single forward pass, while diffusion needs many denoising steps.** — Diffusion removes noise over tens or thousands of passes. A normalizing flow reaches the image through stacked flow layers in one pass, which the host presents as the main efficiency argument. ([1:23](https://youtu.be/mwwuvgi1Qmg?t=83))
- **The autoregressive cost is the bottleneck, and parallel Jacobi iterations are the fix.** — Autoregressive cost inside each flow layer grows quadratically with the number of patches. STARFlow solves the autoregressive equations simultaneously with parallel Jacobi iterations, which the host reports as up to 15x faster, mainly for video. ([2:34](https://youtu.be/mwwuvgi1Qmg?t=154))
- **Invertibility allows exact round-trips and local edits.** — The host says an image can be taken back to its noise state and regenerated to the same result. Changing one small region while keeping everything else identical is presented as possible, and he demos edits such as orange-to-lemon and vase recoloring from the project site, not from his own runs. ([2:34](https://youtu.be/mwwuvgi1Qmg?t=154))
- **The shipped image checkpoint is low resolution and produces artifacts.** — The checkpoint generates 256x256 images. The repo's default batch size is 8, so one run yields eight images. The cat has a sinking head and doubled piano keys, and the chicken-on-custard output is blurry. Polar bear outputs look plausible in several styles, with a few artifacts. ([3:40](https://youtu.be/mwwuvgi1Qmg?t=220))
- **It is a research release, not an on-device model.** — Inference requires Python, PyTorch and GPU resources, with no Apple Silicon or Metal optimization. Only one image checkpoint is public, and the documented higher-resolution and video checkpoints are not released, so the host cannot test video. ([5:03](https://youtu.be/mwwuvgi1Qmg?t=303))

## Techniques
- **Reproduce STARFlow image generation on a rented GPU** — Clone Apple's STARFlow repo from GitHub. Download the image checkpoint from Hugging Face. Follow the repo's install steps on a single-GPU machine (the host used a DigitalOcean GPU droplet with one H200). Run the repo's sample generation command with a text prompt. Set the batch-size option (default 8) to 1 for a single image. The exact command, flag names and config file are not shown in the transcript, so check the repo README. *When:* When you want to evaluate the open-weight STARFlow image checkpoint without local hardware. Expect 256x256 output.
- **Check the claimed speedup against your own timing** — The host did not measure the 15x speedup. To verify it, time image or video generation with and without the parallel Jacobi path on identical prompts, seeds and hardware, then compare wall-clock time and output quality. Video needs a checkpoint that is not public. *When:* Before relying on the 15x claim for capacity planning or latency budgets. Image checkpoint only for now.
- **Edit by inverting the flow and changing part of the latent** — Per the speaker's account of the method: run the flow in reverse to get the noise latent for an existing image or video, change only the region to edit, then run forward again. Because the mapping is invertible, unedited regions should come back unchanged. The host did not run this himself. *When:* When you need local, prompt-driven edits that preserve the rest of the frame. Treat as a claim to verify, not a tested procedure.

## Numbers
- Apple has about 375 public GitHub repos, roughly 200 of them ML-related (fun fact, not verified by the host). ([0:00](https://youtu.be/mwwuvgi1Qmg?t=0))
- STARFlow was announced in June, and its code was uploaded the following month. ([0:00](https://youtu.be/mwwuvgi1Qmg?t=0))
- Diffusion may need tens or thousands of denoising passes, while the flow path runs in one forward pass. ([1:23](https://youtu.be/mwwuvgi1Qmg?t=83))
- Parallel Jacobi iterations are reported as up to 15x faster, especially for video (Apple's claim, not measured). ([2:34](https://youtu.be/mwwuvgi1Qmg?t=154))
- Test hardware: one H200 GPU droplet on DigitalOcean. ([2:34](https://youtu.be/mwwuvgi1Qmg?t=154))
- Default batch size is 8, so one run yields 8 images. Checkpoint output resolution is 256x256. ([3:40](https://youtu.be/mwwuvgi1Qmg?t=220))
- Only one image checkpoint is public; no video checkpoint was released, so no video was generated. ([5:03](https://youtu.be/mwwuvgi1Qmg?t=303))

## Hot takes
- Title hype ("TOO GOOD to Be True") is not borne out by the host's own test: low-res outputs, artifacts, no video checkpoint, and no on-device path.
- The 15x speedup and the editing claims come from Apple's materials. The host did not benchmark them, and the editing demos were shown from the project site.
- Speculation that Apple is 'turning into an AI company' is an aside, not supported by evidence in the video.
- Run-and-judge image quality is subjective; the host's comparison to Nano Banana Pro and Midjourney is not backed by any side-by-side test.

## Tools mentioned
STARFlow (Apple open-source repo), PyTorch, Hugging Face (checkpoint hosting), DigitalOcean GPU droplet, NVIDIA H200, Python, Nano Banana Pro (comparison), Midjourney (comparison)

## Relevance to our work
- **agentos** (1/3): Parallel Jacobi iteration over autoregressive layers is a generation-speed technique similar in spirit to speculative decoding, which AgentOS InferCraft already targets (EAGLE-3). It is a single 6-minute image/video demo, not a serving-side result for LLMs. → *Optional: skim the Jacobi/parallel-decoding literature alongside InferCraft's EAGLE-3 work to see whether parallel fixed-point decoding applies to LLM inference.*
