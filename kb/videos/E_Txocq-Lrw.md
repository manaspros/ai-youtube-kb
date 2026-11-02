# While my guitar gently speaks — Todd Fisher, Philo Ventures

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `E_Txocq-Lrw` · [watch](https://youtu.be/E_Txocq-Lrw) · **date:** 2026-09-18 · **length:** 18:35 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** Todd Fisher · **orgs:** Philo Ventures
- **topics:** voice-multimodal, vibe-coding-app-building, product-ux · **tags:** side-project, guitar, audio-dsp, pitch-detection, vocoder, text-to-speech, speech-to-text, whisper, local-llm, word-segmentation, vocalset, logic-pro, live-demo

> A guitar that speaks and sings: pitch detection, word slicing, vocoder synthesis and a local Whisper-to-LLM loop. Mainly a call to build passion projects with AI.

## Summary
Todd Fisher, a guitarist and engineer, walks through a personal project to make his guitar speak and then sing, starting from a Halloween app that paints letters on his garage door from his playing. He first routes text-to-speech audio through a Logic Pro plugin, then tries to slice speech into words using energy-gap and sonority-peak methods, which fail on unbroken speech and end up needing manual edits. He detects the pitch of each played note with the YIN algorithm, builds a synthesized sawtooth tone, and pushes it through a vocoder so the AI voice sits on the note. He adds a conversational loop (Whisper speech-to-text, a local LLM, then speech on the guitar), which he calls choppy but working. For singing, he pitch-shifts pre-recorded singer samples from VocalSet with the WORLD tool and maps each fret to a sample, since this is too slow to run live. The talk is mostly a demo and a pitch to build passion projects, with no benchmarks or hard data.

## Key ideas
- **Motivation: AI makes it easier to build the side projects engineers have on a list, so go build one** — The speaker frames the talk as a push for people to start passion projects now, saying AI has lowered the time cost and that caveats exist but the general point holds. ([0:12](https://youtu.be/E_Txocq-Lrw?t=12))
- **Word slicing from continuous speech is hard** — Energy-gap segmentation (cut at silence) fails when words run together. Adding a sonority-peak syllabifier (vowels mark syllables) helped partly, and the speaker settled on manual editing of segments. ([8:14](https://youtu.be/E_Txocq-Lrw?t=494))
- **Pitch detection turns a played note into a synthesized tone** — The YIN algorithm finds the fundamental frequency of a guitar note. The system then generates a synthesized sawtooth at that pitch, shaped with ADSR envelope controls, and passes it through a vocoder so the voice takes the note. ([9:41](https://youtu.be/E_Txocq-Lrw?t=581))
- **Live conversation works but is choppy** — Speech goes to Whisper, then to any local LLM, then to speech played through the guitar pipeline. The speaker says the output is choppy but workable, and he mixes the synthesized note with the voice to balance clarity. ([13:33](https://youtu.be/E_Txocq-Lrw?t=813))
- **Singing needs pre-baked samples because the DSP is too heavy to run live** — He pitch-shifts VocalSet singer recordings with the WORLD tool, then maps each fret to one pre-rendered sample. He started with sung vowels (five samples) because the full process takes a long time. ([15:10](https://youtu.be/E_Txocq-Lrw?t=910))
- **Earlier version was a Halloween project that paints letters from notes** — The first build used microphone pitch detection to light up Stranger Things-style letters on a garage door, with custom messages. It was the seed for the later audio work. ([4:23](https://youtu.be/E_Txocq-Lrw?t=263))

## Techniques
- **Energy-gap plus sonority-peak word segmentation** — Cut audio where energy dips toward silence, and use vowel-based sonority peaks to find syllable nuclei. Combine the two signals and expect to fall back to manual edits on connected speech. *When:* Slicing a recorded TTS or speech clip into per-word units to trigger on instrument input.
- **YIN pitch detection to synthesized tone to vocoder** — Detect the fundamental frequency of the played note with YIN, generate a sawtooth synth tone at that pitch with ADSR shaping, then run the voice through a vocoder (talk-box style) so the voice follows the note. *When:* Mapping a live instrument's pitch onto a voice or sound in real time.
- **Pre-bake heavy DSP, then map to controls** — Pitch-shift sample libraries offline with WORLD, then assign each fret or note to one prepared sample so playback stays instant. *When:* A DSP step is too slow for live use but the input space (notes or frets) is small and known.
- **Local voice loop: STT, then local LLM, then TTS** — Transcribe the mic with Whisper, send the text to a local model, then play the reply through the instrument chain. *When:* Building a private, offline conversational voice agent on a laptop.
- **Plugin packaging inside a DAW** — Build the effect as an audio plugin with the JUCE framework and load it into Logic Pro as a normal plugin in the effect chain. *When:* Shipping audio processing that musicians can drop into an existing production setup.

## Numbers
- Has played guitar for trick-or-treaters on Halloween for roughly 10+ years ([2:58](https://youtu.be/E_Txocq-Lrw?t=178))
- Vowel-only singing pass uses five samples, one per vowel, before full singing is done ([16:23](https://youtu.be/E_Txocq-Lrw?t=983))
- A sustained Stranger Things-style scene on Broadway lasted about one minute (audience reference, not a project metric) ([1:36](https://youtu.be/E_Txocq-Lrw?t=96))

## Hot takes
- Maybe you don't need physical effects pedals anymore, since software now covers all the effects
- Time is typically no longer the big time sink for side projects because of AI

## Tools mentioned
JUCE, Logic Pro, Piper TTS, Whisper, YIN pitch algorithm, WORLD vocoder/pitch-shift, VocalSet, Apple built-in TTS
