# This 2B Model Cloned My Voice Locally (VoxCPM)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `O4TMwZlUJvQ` · [watch](https://youtu.be/O4TMwZlUJvQ) · **date:** 2026-09-02 · **length:** 10:14 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Josh (Better Stack host) · **orgs:** Better Stack, OpenBMB, ElevenLabs, Hugging Face
- **topics:** voice-multimodal, local-ai, inference-serving · **tags:** tts, voice-cloning, voice-design, voxcpm2, self-hosting, openai-compatible-api, vllm, apache-2.0, multilingual, macos, nvidia-vram

> Tutorial on running OpenBMB's 2B VoxCPM2 TTS locally for speech generation, voice design from text, and voice cloning, with a clear list of where it falls short versus hosted APIs.

## Summary
The host (Josh, Better Stack) installs VoxCPM2 from OpenBMB, a roughly 2B-parameter text-to-speech model that does plain TTS, text-described voice design, and cloning from a short reference clip, all from one checkpoint. He runs a local Python script on a Mac M4 Pro, then shows how the same model can sit behind an OpenAI-shaped /v1/audio/speech endpoint on a GPU host so an existing app only changes its base URL. He demos voice design from a one-line persona, an 8-second voice clone, and multilingual output (Arabic weaker, French better). The video's real value is the trade-off section: VRAM needs for KV cache and concurrency, uneven quality across prompts and languages, and a suggested test-in-the-Hugging-Face-demo-first workflow. Most of the claims are based on a few listening samples rather than benchmarks, so treat the quality statements as anecdotal.

## Key ideas
- **VoxCPM2 is a single checkpoint that covers three jobs usually split across tools: plain speech generation, voice creation from a text description, and cloning from a reference recording.** — The model is about 2B parameters and works on continuous audio representations instead of discrete speech codec tokens, which the speaker credits for keeping breathing, pacing and emotional shifts. ([0:00](https://youtu.be/O4TMwZlUJvQ?t=0))
- **The case for self-hosting TTS is about three costs of hosted APIs: latency you do not control, a bill that scales with usage, and text or reference audio leaving your network.** — He frames the question as whether the model can remove a hosted dependency without making the stack worse, not whether it sounds cool. ([1:03](https://youtu.be/O4TMwZlUJvQ?t=63))
- **Hardware needs are a real constraint. The Nvidia path is about 8GB VRAM, but that only covers getting it running, not production load.** — He ran the demo on a Mac M4 Pro. He suggests testing your own sentences in the Hugging Face demo before provisioning any infrastructure. ([2:00](https://youtu.be/O4TMwZlUJvQ?t=120))
- **The local script proves the basics: text goes in and a 48 kHz WAV comes out, with no speaker ID or language parameter needed for the basic case.** — He plays the output with macOS afplay. ([4:08](https://youtu.be/O4TMwZlUJvQ?t=248))
- **Serving the model behind an OpenAI-shaped /v1/audio/speech endpoint lets an existing OpenAI TTS client switch with a base URL change and maybe a few parameters.** — He says the serving path uses vLLM and a GPU host. He did not run the server on his laptop. ([4:54](https://youtu.be/O4TMwZlUJvQ?t=294))
- **Voice design from text removes the need to record a reference voice first. The persona is configuration, so a bad persona can be swapped in seconds.** — His example persona was 'hyped American on caffeine'. He says the emotional range is noticeably better than Chatterbox, which he had trouble with. ([6:17](https://youtu.be/O4TMwZlUJvQ?t=377))
- **Cloning works from about 8 seconds of reference audio. Adding a transcript of the reference clip improves the delivery, not just the timbre.** — The model applies the cloned voice to new text rather than replaying the reference. He says the transcript gives it information about the performance. ([6:17](https://youtu.be/O4TMwZlUJvQ?t=377))
- **Quality is uneven across prompts and languages. The model covers about 30 languages, including several Chinese dialects, but Arabic was weaker than French in his test.** — Output language is set explicitly; the model does not translate the input text. ([7:20](https://youtu.be/O4TMwZlUJvQ?t=440))
- **The honest comparison is not 'beats ElevenLabs on every sentence' but whether it can replace the hosted API for most generated speech while a small hosted fallback is kept.** — He estimates roughly 80% of generation as the replaceable share. This is his estimate, not a measured figure. ([9:20](https://youtu.be/O4TMwZlUJvQ?t=560))

## Techniques
- **Prototype the voice in a hosted demo before any infra work** — Paste the exact production sentences into the Hugging Face demo for VoxCPM2. Only self-host if the voice passes there. This tests output quality separately from deployment. *When:* Evaluating any TTS or voice model before committing to GPU hosting.
- **Local install and minimal generation script** — Create a virtualenv on a recent Python. pip install torch and torchaudio (a reasonably recent PyTorch build), then pip install voxcpm. The checkpoint is OpenBMB/VoxCPM2. The script imports voxcpm, builds the model, sets the input text, and calls the generate method. The output is a 48 kHz WAV. Play it with afplay on macOS. The exact generate arguments were on screen and not spoken, so check the repo README before copying them. *When:* First local check on a dev machine with a few GB free disk and a GPU or Apple Silicon.
- **Turn the model into a service behind the OpenAI speech API** — On a Linux or Nvidia GPU host with enough VRAM, run the VoxCPM2 server command from the repo. The server exposes an OpenAI-compatible /v1/audio/speech route. Point the existing client's base URL at it and adjust a couple of parameters. The vLLM path is what he says makes this look like a normal service. The exact server command is shown on screen, not spoken, so check the repo. *When:* An app already calls the OpenAI TTS API and you want to move that traffic to a self-hosted model.
- **Voice design from a persona description** — Put a short natural-language description of the speaker (his example: 'hyped American on caffeine') ahead of the text to be spoken, then generate. The description is the voice config. No reference audio is needed. The exact prompt syntax is not spelled out in the transcript. *When:* Prototyping personas or agent voices when you have no recorded speaker.
- **Voice cloning from a short reference, with transcript** — Use about 8 seconds of clean reference audio of the target speaker. Generate new text in that voice. For better delivery, also provide the exact transcript of the reference clip. Only clone voices you have permission to use. *When:* A cloned voice is needed and the reference clip is clean, with a known transcript.
- **Set the output language explicitly for multilingual speech** — Pass the target language as an output parameter. The model does not translate, so translate the text first, then generate it in the target language. Expect uneven quality by language. Test each target language with your own sentences. *When:* Generating speech in several languages from one model.

## Numbers
- Model size is about 2 billion parameters ([0:00](https://youtu.be/O4TMwZlUJvQ?t=0))
- Output sample rate is 48 kHz ([4:08](https://youtu.be/O4TMwZlUJvQ?t=248))
- Nvidia path needs about 8 GB VRAM to run; the speaker says a 24 GB card gives much more room for KV cache and concurrency ([2:00](https://youtu.be/O4TMwZlUJvQ?t=120))
- Voice clone reference clip is about 8 seconds ([6:17](https://youtu.be/O4TMwZlUJvQ?t=377))
- Supports about 30 languages, including multiple Chinese dialects ([7:20](https://youtu.be/O4TMwZlUJvQ?t=440))
- License is Apache 2.0 ([8:17](https://youtu.be/O4TMwZlUJvQ?t=497))
- Speaker's replaceable share of hosted TTS generation is about 80%. This is his estimate with no measured data. ([9:20](https://youtu.be/O4TMwZlUJvQ?t=560))

## Hot takes
- The speaker says the emotional range is 'insanely good' compared with Chatterbox. This is a subjective judgment from a few samples, not a benchmark.
- Framing the model as able to 'crush 11 Labs' is hype in the cold open. The body of the video concedes that quality depends on language, reference audio and prompt, and that hosted APIs are still better in many cases.
- The '80% replaceable' estimate and the 8 GB-is-not-production point are the most useful claims, but they are unmeasured.
- Quality is roughly 3 rather than higher because it is a solid, honest walkthrough with a useful trade-off section, but it has no benchmarks, no exact API code, and no latency or throughput numbers.

## Tools mentioned
VoxCPM / VoxCPM2 (OpenBMB, Apache 2.0, ~2B params), PyTorch, torchaudio, Python, vLLM, Hugging Face (demo and checkpoint), macOS afplay, ComfyUI, GGUF, MLX (community paths mentioned), Chatterbox (TTS comparison), Qwen3-TTS (TTS comparison), ElevenLabs (hosted TTS comparison)

## Relevance to our work
- **agentos** (1/3): InferCraft (vLLM plus Ray Serve) could serve a speech model, and the OpenAI-shaped speech endpoint fits the proxy pattern. AgentOS has no voice pillar, so the fit is weak. → *Low priority: if AgentOS ever needs a self-hosted audio modality, check whether VoxCPM2 runs under the vLLM setup in InferCraft and how it fits on the RTX 5090.*
