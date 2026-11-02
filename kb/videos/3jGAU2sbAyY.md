# Why TTS Models Now Look Like LLMs — Samuel Humeau, Mistral

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `3jGAU2sbAyY` · [watch](https://youtu.be/3jGAU2sbAyY) · **date:** 2026-05-18 · **length:** 22:26 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Samuel Humeau · **orgs:** Mistral AI, Facebook (FAIR)
- **topics:** voice-multimodal, models-research, inference-serving · **tags:** text-to-speech, audio codec, audio tokens, autoregressive decoding, flow matching, voice cloning, streaming latency, voice agents, Mistral, open source model

> Mistral's Samuel Humeau explains why modern text-to-speech uses autoregressive audio-token LLM-style backbones, frame-level codecs and streamed output for voice agents.

## Summary
Samuel Humeau of Mistral AI argues that text-to-speech is mainly used now as the output layer of voice chat agents, where latency matters most. He shows a demo where audio starts playing from the first packets while the full clip is still being computed, which lowers perceived latency. He then walks through the common architecture: a codec turns about 80 ms audio frames into discrete tokens, and an autoregressive backbone predicts those tokens, with a small inner model handling the tokens within each frame. He explains why audio needs far more tokens than text and how codecs are trained with reconstruction, adversarial, and text-aware losses. He describes the conditioning split between models that receive all text up front and models that take streamed text, and says Mistral's open model is in the first group, with about 70 ms from text input to first playable audio on one GPU. He presents streaming text input as an open research question, with interleaved and dual-stream designs both still in play. Voice cloning from a few seconds of reference audio is shown, but the encoder for cloning is kept proprietary.

## Key ideas
- **For TTS, the main production use is as the output stage of a voice chat agent, so latency is the key metric.** — Pipeline is speech-to-text, then a text LLM, then TTS. Speech-to-text can run in real time so the transcript is ready at end of turn, and the TTS side should start speaking on the first audio packets rather than waiting for the full clip. ([2:05](https://youtu.be/3jGAU2sbAyY?t=125))
- **Perceived latency depends on time to first audio packet, not time to full audio.** — In the demo, playback begins on the first packet while the full computation still takes a few seconds. The speaker also says the ideal is streaming text in and speech out, starting speech from the first LLM token. ([3:28](https://youtu.be/3jGAU2sbAyY?t=208))
- **Most labs have converged on an LLM-style design: an autoregressive backbone over audio tokens, with a codec that maps short audio frames to and from tokens.** — Audio is generated as patches, one frame at a time, not sample by sample. An encoder compresses each frame (about 80 ms) into tokens, and a decoder reverses this. Generating the whole clip at once was an earlier approach, but streaming the start first is more useful. ([8:18](https://youtu.be/3jGAU2sbAyY?t=498))
- **Audio needs far more tokens than text, so the codec must compress hard while keeping voice identity.** — Text carries only a few bits per second, whereas a standard MP3 is about 200 kbps. The codec is trained by reconstruction through a bottleneck, with reconstruction and adversarial losses. Some tokens are also trained to carry the transcript so text can be read back from them. ([9:38](https://youtu.be/3jGAU2sbAyY?t=578))
- **Two-level decoding keeps the big model's step count down: the large backbone runs once per frame and a smaller inner transformer produces that frame's tokens.** — Each frame in the speaker's model maps to 37 tokens, about 500 tokens per second overall. The released model departs from this pattern: it generates all 37 tokens of a frame at once with a flow-matching (diffusion-like) head. ([12:30](https://youtu.be/3jGAU2sbAyY?t=750))
- **Conditioning splits into two families: models that get all the text up front, and models that take text as a stream while audio is being produced.** — The released model is in the first family. It gets a few seconds of reference audio plus the full text, and it reaches about 70 ms from text input to first playable audio on a single GPU, excluding network time. Streaming text input is still unsolved, with interleaved and dual-stream designs both under study. ([15:25](https://youtu.be/3jGAU2sbAyY?t=925))
- **Speech as the universal agent interface can go a long way, because agents can keep their own text output and only add speech on top.** — The speaker's argument is that the central LLM can stay text-to-text and simply stream its tokens to a TTS layer. This keeps the same interface for any agent. ([20:02](https://youtu.be/3jGAU2sbAyY?t=1202))

## Techniques
- **Stream the first audio chunks** — Start playback on the first frames of audio while the rest is still generating. Measure latency as time to first packet. *When:* Any voice agent where the answer is long or where perceived responsiveness matters more than total time.
- **Two-level frame decoding** — Run the large autoregressive backbone once per audio frame, and a small inner transformer that predicts all tokens inside that frame. *When:* Audio token sequences would otherwise be too long for the backbone, with thousands of backbone steps per clip.
- **Codec with a bottleneck and text-aware token losses** — Train an audio codec by reconstruction through a bottleneck, using reconstruction and adversarial losses, and force some tokens to carry text so the transcript is recoverable. *When:* Building or choosing an audio tokenizer that must keep voice and acoustic detail but still needs few tokens per second.
- **Flow-matching token head per frame** — Generate all tokens of one audio frame in one step with a flow-matching (diffusion-like) model, not one token at a time. *When:* Per-frame token count is high (37 here) and sequential token generation is the bottleneck.
- **Full-context conditioning with a short voice prompt** — Give the model a few seconds of reference audio and the full text before generating audio. *When:* The text is known in advance, as with the released model, and cloning or a consistent voice is needed.
- **Fast small LLM for the text, TTS for the audio** — In the demo, a small fast LLM produced the answer text in one go, and TTS then voiced it with streaming. *When:* A voice agent that needs a quick first reply and can accept a lighter text model.

## Numbers
- Mistral's first open-source TTS model, released the week before the talk; the speaker calls it an extremely strong model. ([0:00](https://youtu.be/3jGAU2sbAyY?t=0))
- Audio is measured as pressure samples several thousand times per second; a standard quality MP3 is about 200 kbps. ([8:18](https://youtu.be/3jGAU2sbAyY?t=498))
- Real-time speech-to-text in the demo carried only about 15 bits per second of information. ([11:04](https://youtu.be/3jGAU2sbAyY?t=664))
- Frames are 80 ms, roughly 12 frames per second; each frame is 37 tokens, about 500 tokens per second in total. ([11:04](https://youtu.be/3jGAU2sbAyY?t=664))
- The backbone of the released system is about 4 billion parameters. ([12:30](https://youtu.be/3jGAU2sbAyY?t=750))
- About 70 ms from text input to first playable audio on a single GPU, excluding network. ([15:25](https://youtu.be/3jGAU2sbAyY?t=925))
- Voice cloning needs only a few seconds of reference audio. ([6:03](https://youtu.be/3jGAU2sbAyY?t=363))

## Hot takes
- Speech as the interface may go very far, since a central text LLM can stay as it is and only be wrapped in speech.
- Voice identity will become as common a brand asset as a website's look, once voice cloning is easy.
- Streaming text input to TTS is still an open architecture question; the speaker does not know which design will win.
