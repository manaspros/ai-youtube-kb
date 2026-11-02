# This 600M Model Fixes What Whisper Leaves Behind

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `jp0PGmAwK3w` · [watch](https://youtu.be/jp0PGmAwK3w) · **date:** 2026-09-02 · **length:** 8:41 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Super Whisper, Better Stack, Hugging Face
- **topics:** local-ai, data-engineering, coding-agents · **tags:** speech-to-text, transcript-cleanup, ollama, gguf, whisper, on-device, small-models, dictation

> Super Whisper's open 600M-parameter S1 Mini cleans raw speech-to-text output (fillers, self-corrections, spoken numbers, emails) locally via GGUF and Ollama. English only, early software.

## Summary
The video presents S1 Mini, an open 600M-parameter model from Super Whisper that is meant to sit after any speech-to-text system and turn raw transcripts into clean written text. The speaker's pitch is a narrow job: remove fillers, resolve false starts and self-corrections, format numbers, dates and email addresses, and optionally set tone, without rewriting or expanding meaning. He runs a quantized GGUF (about 462 MB) on a Mac M4 Pro through Ollama, and shows a handful of hand-picked messy samples that come out cleaned with near-instant latency. He argues a general LLM can do this too but can take the text in too many directions, which is why a small constrained model is the point. He frames the pipeline as ASR, then S1 Mini, then the destination (editor, coding agent, Slack, email, tickets), and suggests a fully local dictation setup with Whisper.cpp plus S1 Mini. The limits he names are English-only support, a very recent release (August 19), and that S1 Voice and S1 Language are separate cloud models. The evidence is a demo of a few samples, with no accuracy or latency measurements.

## Key ideas
- **Transcription is largely solved; the remaining problem is cleaning the transcript.** — The speaker positions S1 Mini as a post-ASR layer: raw text in, clean text out, sitting after Whisper, Whisper.cpp, Parakeet or a custom ASR service. ([0:00](https://youtu.be/jp0PGmAwK3w?t=0))
- **S1 Mini is a narrow normalizer, not a general model.** — It removes fillers, resolves false starts and self-corrections, formats numbers, dates and emails, and can control tone. He stresses it leaves most meaning alone and should not be used for reasoning or summarization. ([0:56](https://youtu.be/jp0PGmAwK3w?t=56))
- **Small and local is the point: the GGUF is about 462 MB and runs through standard local tooling.** — He used a quantized GGUF from Hugging Face on a Mac M4 Pro, served through Ollama, and notes llama.cpp and LM Studio also work. ([0:56](https://youtu.be/jp0PGmAwK3w?t=56))
- **Demo: a deliberately messy sample (filler, mid-sentence correction, spoken email) comes out cleaned.** — Fillers disappear, the changed-mind correction is applied, and the spoken email address is formatted. He reports no perceptible lag, but shows only a few samples and no metrics. ([2:06](https://youtu.be/jp0PGmAwK3w?t=126))
- **Constrained output is the argument for a small model over a general LLM.** — A general LLM can rewrite, summarize or expand a transcript. A model with a smaller job avoids turning one sentence into a long email. ([4:42](https://youtu.be/jp0PGmAwK3w?t=282))
- **Clear separation of stages: Whisper turns audio into text, S1 Mini turns text into written-style text.** — He sketches a fully local dictation pipeline with Whisper.cpp for audio and S1 Mini for cleanup, with output going straight into an editor, and a coding-agent case where the correction is cleaned before the instruction reaches the agent. ([5:46](https://youtu.be/jp0PGmAwK3w?t=346))
- **Limits: English only, a very new model family, and S1 Voice and S1 Language are cloud products.** — The S1 family dropped on August 19. He advises treating it as early software and not confusing S1 Mini with the cloud speech models. ([6:56](https://youtu.be/jp0PGmAwK3w?t=416))

## Techniques
- **Post-ASR cleanup layer** — Run any local speech-to-text (Whisper.cpp, Parakeet, MLX Whisper, custom ASR) first, then pass the raw transcript through S1 Mini to remove fillers, apply self-corrections and normalize numbers, dates and emails before the text reaches its destination. *When:* Voice input that becomes text for coding agents, Slack messages, emails, support tickets or meeting notes, where the output should look typed rather than spoken.
- **Local GGUF serving with Ollama** — Download the quantized S1 Mini GGUF from Hugging Face, write a simple Ollama Modelfile pointing at the file, create the model, and serve it. The speaker says he used curl for the download and a Modelfile on the desktop, but does not show exact commands or the Modelfile contents on screen; the model page link is in the video description. The same GGUF works with llama.cpp or LM Studio. *When:* When you want cleanup with no cloud API call and no per-request cost, on a laptop or workstation.
- **Keep the cleanup model narrow and use a general LLM for everything else** — Use S1 Mini only for transcript normalization. Route reasoning, summarization or agent work to a general model, which the speaker says should be used for those tasks. *When:* When designing a voice pipeline where you want to limit what the model can change in the user's text.
- **Fully local dictation pipeline** — Capture audio, transcribe with Whisper.cpp, pass the text to S1 Mini, and write the cleaned text straight to the editor, so no audio or text leaves the machine. *When:* Privacy-sensitive dictation or any workflow where transcript data must stay on the device.

## Numbers
- S1 Mini has about 600 million parameters. ([0:00](https://youtu.be/jp0PGmAwK3w?t=0))
- Quantized GGUF is about 462 MB, the speaker's stated size of the download he ran on an M4 Pro Mac. ([0:56](https://youtu.be/jp0PGmAwK3w?t=56))
- Demo used a pre-recorded audio clip of about 10 seconds, transcribed with MLX Whisper, then cleaned. ([3:29](https://youtu.be/jp0PGmAwK3w?t=209))
- Cleanup is described as near-instant with no visible lag on the samples shown. No measured latency or accuracy is given. ([2:06](https://youtu.be/jp0PGmAwK3w?t=126))
- The S1 family was released on August 19 (the video is dated 2026-09-02). ([6:56](https://youtu.be/jp0PGmAwK3w?t=416))

## Hot takes
- A constrained 600M cleanup model is safer for this step than a general LLM because it cannot rewrite or summarize (speaker's opinion, not tested).
- Cloud API costs and privacy go away when cleanup runs locally, which matters at high volume (speaker's claim; no cost numbers shown).
- The evidence is a few hand-picked samples on one Mac. No accuracy, error-rate or multilingual results are given, and the speaker says it is English-only and early.

## Tools mentioned
S1 Mini (Super Whisper, open 600M model), S1 Voice (Super Whisper, cloud ASR, not covered), S1 Language (Super Whisper, cloud, not covered), Whisper, Whisper.cpp, Parakeet, MLX Whisper, Ollama, llama.cpp, LM Studio, Hugging Face, GGUF, GPT and Claude (named as general LLM alternatives)

## Relevance to our work
- **agentos** (1/3): AgentOS is an OpenAI-compatible local proxy for self-hosted agents; a small local cleanup model could sit in front of agent input, but this is a text normalization step, not an infra or gateway concern. → *Optional: if AgentOS ever takes voice input, test a local cleanup pass (served through Ollama or vLLM) before the request goes to the proxy.*
- **prosharness** (1/3): ProsHarness drives the Claude Code CLI and has phone-driven approvals; the speaker explicitly names cleaning dictated instructions before they reach a coding agent. → *If ProsHarness accepts spoken or phone-dictated instructions, try a local post-transcription cleanup step before the instruction is sent to the Claude Code CLI.*
