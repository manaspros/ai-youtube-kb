# Google's New AI Architecture Changes Everything (Gemma 4 12B)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `WLtCHXdHTF0` · [watch](https://youtu.be/WLtCHXdHTF0) · **date:** 2026-07-02 · **length:** 11:02 · **format:** review · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Andrus · **orgs:** Better Stack, Google DeepMind
- **topics:** models-research, local-ai, voice-multimodal · **tags:** gemma-4, gemma-4-12b, multimodal, encoder-free, linear-projection, local-inference, apple-silicon, omlx, quantization, multi-token-prediction

> Better Stack explains Google's encoder-free Gemma 4 12B, which replaces vision and speech encoders with linear projections, then runs an offline image test on a 24GB M2 Mac. The architecture detail is useful, but the claims are unbenchmarked.

## Summary
The host presents Google DeepMind's Gemma 4 12B as a multimodal model with no separate vision or speech encoder. Standard pipelines run a vision encoder (he cites a 550M-parameter example) and a speech encoder before the LLM, which costs VRAM and time. In Gemma 4 12B, image patches (48x48) and 40 ms audio frames (640 floats from 16 kHz audio) each go through one linear projection into the LLM's input space, and he describes this as about 35M parameters. He argues the backbone already has enough depth to do the visual reasoning. He cites closeness to the 26B sibling, fit on a laptop with 16GB+ VRAM, and bundled multi-token prediction drafters, but shows no benchmark numbers. The hands-on part runs an 8-bit quantized build in OMLX on an M2 MacBook Pro with 24GB, offline, on two images; Google's AI Edge Gallery app failed on image input. The speed impressions are subjective, with no tokens/s or latency figures.

## Key ideas
- **Gemma 4 12B is presented as encoder-free: no separate vision or speech encoder network sits in front of the LLM.** — Standard multimodal stacks tape separate encoders onto the LLM, which the host says hogs VRAM and slows inference. Google's design is presented as removing that middleman. ([0:00](https://youtu.be/WLtCHXdHTF0?t=0))
- **The standard pipeline is the problem being solved: a vision encoder and a speech encoder each translate raw input before the LLM sees it.** — He says running these alongside the LLM means three networks at once on a laptop, which costs memory and speed. ([1:06](https://youtu.be/WLtCHXdHTF0?t=66))
- **Image input becomes patches plus one linear projection.** — The image is cut into 48x48 patches, each flattened to 2304 values and multiplied by a single projection matrix into the LLM's token width. He says the projection is about 35M parameters, against a 550M-parameter vision encoder in a standard model. ([2:15](https://youtu.be/WLtCHXdHTF0?t=135))
- **The projection only reformats data; the backbone does the visual reasoning.** — He argues the language backbone already has enough layers for visual reasoning, so the encoder's attention layers are redundant. He presents this as an interpretation, not a measured result. ([3:20](https://youtu.be/WLtCHXdHTF0?t=200))
- **Audio is handled the same way: 40 ms frames of 16 kHz audio are projected into the LLM's input space.** — Each frame holds 640 floats. The backbone treats the audio stream like text tokens, which he says lets it handle transcription, translation and formatting in one forward pass. ([4:23](https://youtu.be/WLtCHXdHTF0?t=263))
- **Performance claims: near the 26B sibling's benchmarks, and it fits on a laptop with 16GB+ VRAM.** — Multi-token prediction drafters ship with the model for faster local decoding without compressing the weights. No benchmark scores or charts appear in the video. ([5:43](https://youtu.be/WLtCHXdHTF0?t=343))
- **A hands-on test on an M2 MacBook Pro shows image reasoning is fast, but the official app is unreliable.** — He used an 8-bit quantized build in OMLX, offline, with two images. Google AI Edge Gallery failed on image input for him, so he ran the test in OMLX. He calls it the best local image model he has tried, based on one run. ([8:07](https://youtu.be/WLtCHXdHTF0?t=487))

## Techniques
- **Patch-and-project image input for an encoder-free multimodal LLM** — Cut the image into fixed patches (48x48 in this model), flatten each patch to a vector (2304 values for the single-channel case he describes), and apply one learned linear projection to the LLM hidden size. The projected patches enter the transformer as a token-like sequence. No attention layers run before the backbone. *When:* Understanding the VRAM footprint and design trade-off of encoder-free multimodal models before choosing one for local serving.
- **Audio frames projected as tokens** — Slice a 16 kHz waveform into 40 ms frames (640 samples each), run each frame through one projection layer into the LLM's input dimension, and feed the sequence to the backbone alongside text tokens. *When:* Evaluating whether a single backbone can replace a separate speech encoder for live transcription or translation.
- **Offline real-time image sanity check for a local model** — In OMLX on Apple Silicon, load the 8-bit quantized model, turn off Wi-Fi to confirm offline operation, open the chat view, attach an image, and ask 'what do you see in this image'. Time the response unedited. Repeat with a second image of a different type (a blurry TV still). *When:* A quick first check that a local vision model answers in real time before deeper evals. Two images are not a benchmark.
- **Native multi-token prediction drafters** — The release ships drafter components that predict several tokens per step, which the host says speeds local inference without quantizing the model. No config, flags or runtime setup were shown. *When:* When local decode speed matters and you want to avoid lossy compression. Verify the runtime support first.

## Numbers
- Gemma 4 12B has 12 billion parameters. ([0:00](https://youtu.be/WLtCHXdHTF0?t=0))
- A standard vision encoder example has about 550M parameters; the Gemma projection is about 35M. ([2:15](https://youtu.be/WLtCHXdHTF0?t=135))
- Image patches are 48x48 pixels, flattened to 2304 values each. ([2:15](https://youtu.be/WLtCHXdHTF0?t=135))
- Audio is 16 kHz, sliced into 40 ms frames of 640 floats each. ([4:23](https://youtu.be/WLtCHXdHTF0?t=263))
- Fits on a standard laptop with 16GB VRAM or more. The host's test machine has 24GB. ([5:43](https://youtu.be/WLtCHXdHTF0?t=343))
- Claims closeness to the 26B model's benchmarks. No scores are shown. ([5:43](https://youtu.be/WLtCHXdHTF0?t=343))
- Image response speed was judged 'insane' and real-time on an unedited screen recording. No tokens/s or latency figures are given. ([8:07](https://youtu.be/WLtCHXdHTF0?t=487))

## Hot takes
- The 'encoder-free' and 'game changer' framing rests on the host's reading of a Google release. No paper, model card or benchmark table is shown, so performance claims are unverified.
- The numbers do not fully agree: a 48x48 patch flattened to 2304 values implies one channel, whereas RGB would give 6912 values. Check the model card before reusing the figure.
- The 'zero thinking' framing oversimplifies. The projection is still learned and still maps every patch, and the claim that the backbone does all visual reasoning is an interpretation.
- The speed verdict rests on one subjective run per image, with no prompt length, tokens/s, memory use or comparison to other local vision models.
- The title ('changes everything') and the repeated 'game changer' language are hype with thin measured evidence. Quality is capped at 2 for that reason, though the architecture walkthrough is concrete.

## Tools mentioned
Gemma 4 12B, Gemma 4 26B (sibling model, comparison only), OMLX (local inference framework for Apple Silicon), Google AI Edge Gallery (mobile app, buggy on image input in the host's test), M2 MacBook Pro (24GB, host's test machine)

## Relevance to our work
- **agentos** (1/3): InferCraft serves models on one RTX 5090. An encoder-free 12B multimodal model is a possible local candidate, but the claims are unverified and the video has no benchmarks. → *Check the Gemma 4 12B model card for the encoder-free design and its multi-token drafter support, then benchmark its image path on the InferCraft vLLM stack against the current local vision model.*
- **general** (1/3): Shows the direction of smaller local multimodal models, but no measured results. → *Verify the encoder-free claim against Google's own Gemma 4 release notes before citing it in the knowledge base.*
