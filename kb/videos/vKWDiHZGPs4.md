# I Stress-Tested Meta’s SAM 3D on Real Photos And The Results Were Shocking!

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `vKWDiHZGPs4` · [watch](https://youtu.be/vKWDiHZGPs4) · **date:** 2026-01-02 · **length:** 12:25 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** Andrus · **orgs:** Better Stack, Meta, RunPod, Expo, Hugging Face, Blender
- **topics:** voice-multimodal, inference-serving · **tags:** sam-2, sam-3d, segment-anything, 3d-reconstruction, gaussian-splatting, expo, runpod, mobile-app, remote-gpu, huggingface, glb, vision-models

> Better Stack tutorial that walks through Meta's SAM 2 and SAM 3D Objects models and builds an Expo mobile app that turns a photo into a 3D model, with the models hosted on a rented RunPod A40 GPU.

## Summary
The speaker explains Meta's Segment Anything family: SAM 2 uses clicks or boxes, later SAM versions accept text prompts, and SAM 3D reconstructs 3D shapes from a single 2D image plus a mask (SAM 3D Objects for everyday objects, SAM 3D Body for human shape and pose). He describes the pipeline as an image-and-mask encoder, a flow-based transformer that outputs 3D Gaussian primitives, Gaussian splatting rendering, and conversion of the resulting point cloud to a mesh. The build uses an Expo front end that calls an API running in a RunPod A40 container, with SAM 2 for one-click segmentation and SAM 3D Objects for reconstruction. Setup is a single script that takes about 15 minutes, mostly for SAM 3D dependencies, and requires a Hugging Face token with approved access to the gated model weights. In tests, SAM 3D filled in occluded parts of a dog and an old car well, took roughly a minute per object, and exported GLB files that were usable in Blender but low-detail up close. It failed on a squirrel photo (wrong proportions, Pokemon-like result) and did not reproduce text labels, and the speaker stresses that good segmentation is still needed. The speaker also notes that Meta's hosted playground segments more completely than SAM 2 does out of the box.

## Key ideas
- **SAM 3D reconstructs 3D geometry and texture from one 2D image plus an object mask, and can fill in parts of an object that are occluded.** — Pipeline described: image and mask go through a vision encoder, then a flow-based transformer produces 3D Gaussian primitives, which are rendered via Gaussian splatting and converted to a solid mesh. Two variants: SAM 3D Objects (everyday objects and scenes) and SAM 3D Body (human shape and pose). ([1:38](https://youtu.be/vKWDiHZGPs4?t=98))
- **The app architecture offloads all vision work to a remote GPU container behind a small API, with a thin mobile client.** — Expo handles photo capture, segmentation UI and 3D preview; a RunPod A40 pod hosts the models and exposes port 8000. The speaker chose an A40 to limit cost and notes an RTX 5090 would be faster. ([3:01](https://youtu.be/vKWDiHZGPs4?t=181))
- **SAM 2 and SAM 3 are used for different parts of the flow: SAM 2 for one-click segmentation, SAM 3D Objects for reconstruction.** — SAM 3 uses a draggable box for segmentation; the speaker prefers SAM 2's one-click flow and says the comparison is a chance to test both generations. ([4:05](https://youtu.be/vKWDiHZGPs4?t=245))
- **Out-of-the-box SAM 2 segmentation can be partial, so extra clicks are needed to mask the whole object before 3D generation.** — On a dog photo, one click segmented only the head. Meta's playground segmented the whole dog. The speaker says the demo behavior is not what the released model does by default; adding more points fixed it. ([7:48](https://youtu.be/vKWDiHZGPs4?t=468))
- **SAM 3D output is a GLB mesh plus a preview GIF, and quality is good but limited in fine detail.** — The app shows a rotating GIF rather than a 3D viewer; the API serves an assets listing for downloading GLB files. In Blender the models were usable for low-poly game assets but low-resolution up close. ([8:53](https://youtu.be/vKWDiHZGPs4?t=533))
- **SAM 3D fails when the input shows too little of the subject, and it does not reproduce text.** — A squirrel with only the head masked got added hands and feet with wrong proportions, looking more like a Pokemon. Labels and text on objects were not reproduced, though object shapes and proportions were mostly correct on household items. ([10:17](https://youtu.be/vKWDiHZGPs4?t=617))
- **The speaker's main takeaway is that segmentation quality is the bottleneck, not the 3D model.** — He calls the occlusion compensation powerful but says good segmentation is still necessary for good output. He also tested architecture (a CN Tower model) taken outdoors. ([10:17](https://youtu.be/vKWDiHZGPs4?t=617))

## Techniques
- **Provision a RunPod GPU pod for vision models** — Deploy an A40 pod with container disk raised to 100 GB (project is about 50 GB), expose port 8000 as the API port, SSH in with the copied command, and clone the API repo. Speaker notes that disk is cheap on RunPod and GPU time is the real cost. *When:* When you need a remote GPU for a self-hosted model demo or prototype and want to avoid buying hardware.
- **Hugging Face gated-model access setup** — Create a Hugging Face account and access token, request access to the SAM model repos (approval is usually quick), then run the Hugging Face CLI login in the pod and paste the token when prompted. *When:* Before the first run, whenever weights come from gated Hugging Face repos.
- **One-command setup script, then launch the API** — Run the single setup script from the API repo (about 15 minutes, mostly SAM 3D dependencies). Launch the server with uvicorn bound to host 0.0.0.0 and port 8000 (caption reads 'uvicorn api:app', so the module name is inferred). The first launch downloads SAM 2 weights from Hugging Face. *When:* To reproduce the stack from the repo. Expect a long install and a first-run download.
- **Point the Expo client at the pod** — Clone the front-end repo, run npm install, then run expo. In api.ts, set the SAM API base variable to the container URL from RunPod's connect button. *When:* To connect a local mobile client to the remote model API.
- **Iterative point-based segmentation before 3D generation** — Tap points on the object in the app; add more points until the whole object is masked (a single click on a dog's head only covered the head). Then trigger 3D generation (roughly a minute on an A40). *When:* For partially occluded objects or any subject where a single click under-segments.
- **Export and inspect generated assets** — Use the API's assets list endpoint to download generated files, including the GLB, and open the GLB in Blender to check detail. *When:* When the 3D output needs a 3D tool such as Blender, since the app has no built-in viewer.

## Numbers
- Project footprint is about 50 GB; container disk set to 100 GB on RunPod. ([4:05](https://youtu.be/vKWDiHZGPs4?t=245))
- Full setup takes about 15 minutes, mainly due to SAM 3D dependencies. ([5:21](https://youtu.be/vKWDiHZGPs4?t=321))
- A40 GPU used; RTX 5090 suggested as faster but the speaker did not want to pay for it. ([3:01](https://youtu.be/vKWDiHZGPs4?t=181))
- 3D generation takes roughly a minute on the A40. ([7:48](https://youtu.be/vKWDiHZGPs4?t=468))
- Video length is 12:25. ([0:00](https://youtu.be/vKWDiHZGPs4?t=0))

## Hot takes
- Meta's hosted playground segments objects more completely than SAM 2's out-of-box behavior, and the speaker says even Meta's own demos do not match what the released model does.
- SAM 3D's occlusion compensation is 'really, really powerful' on the dog and car, but it breaks on unusual subjects and text.
- The setup is heavy for a demo: a 50 GB project and roughly 15 minutes of installation.

## Tools mentioned
SAM 2, SAM 3, SAM 3D Objects, SAM 3D Body, Expo, RunPod (A40 GPU pod), RTX 5090 (mentioned as a faster alternative), Hugging Face CLI, uvicorn, npm, Blender, GLB file format, Gaussian splatting

## Relevance to our work
- **agentos** (1/3): InferCraft-style GPU serving: the video is a small example of hosting a vision model on a rented GPU behind a thin API. It is a demo pattern, not a serving-architecture reference. → *No change needed. Revisit only if vision or 3D generation enters AgentOS scope.*
