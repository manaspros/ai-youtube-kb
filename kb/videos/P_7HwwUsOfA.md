# This AI Startup Is Making Powerful AI Models (Desert Ant Labs)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `P_7HwwUsOfA` · [watch](https://youtu.be/P_7HwwUsOfA) · **date:** 2026-10-02 · **length:** 15:53 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Andrus · **orgs:** Better Stack, Desert Ant Labs, Anthropic, Apple, Hugging Face
- **topics:** local-ai, voice-multimodal, security-guardrails · **tags:** on-device-ai, small-models, speech-recognition, pii-redaction, language-identification, vibe-coding, model-review

> Better Stack hands-on tour of 12 tiny on-device models from Desert Ant Labs (speech, redaction, language ID, emoji). Several are fast and useful, some are weak, and the vendor benchmarks are mostly unverified.

## Summary
Andrus from Better Stack profiles Desert Ant Labs, a European lab that builds small, single-task models meant to run offline on phones and laptops with no server, API key or per-token cost. The lab's pitch is a "cerebellum" layer: small on-device models handle constant background work while large cloud models do the reasoning. It has shipped 12 models, all open on Hugging Face with an SDK on GitHub and free use up to 100,000 monthly active devices per platform, and lists five more in beta. The presenter runs each model he can reach from a quick app (vibe-coded with Opus 5) or on an iPhone, using his own recordings, typed text and several languages. Results are mixed: Vaus transcribed a 7-minute clip in about 2 seconds, Tongue and Emo look usable, while Redact missed passwords and a Canadian SIN, Gist's tags are keyword-driven, and Ear is slow and wrong on Latvian. Several headline claims, such as Clips' 470x energy saving versus Sonnet and Align beating Apple's transcriber, were not tested. The closing view that single-task micro models are the sensible direction for on-device AI is opinion, and the video shows no architecture, code or measured accuracy.

## Key ideas
- **Desert Ant Labs' thesis: small specialized on-device models as a background layer under large cloud reasoning models** — Framed with a cerebellum analogy: fast, constant reflex work is offloaded locally so the big model is free to reason. The presenter treats this as the lab's philosophy, not a measured result. ([0:00](https://youtu.be/P_7HwwUsOfA?t=0))
- **Release footprint: 12 shipped models plus 5 beta models** — Shipped models cover audio, text and vision and are open on Hugging Face, with the SDK on GitHub and free use up to 100,000 monthly active devices per platform. Beta models named: speaker identification, structured JSON extraction from raw text, toxicity, nudity moderation, and vision tasks (Eye and Face). ([1:15](https://youtu.be/P_7HwwUsOfA?t=75))
- **Vaus speech recognition matched its speed claim in one test** — A 7-minute clip transcribed in about 2 seconds on an iPhone. The transcript was shown but accuracy was not scored. ([2:24](https://youtu.be/P_7HwwUsOfA?t=144))
- **Clear speech enhancement only partly cleaned an extreme noisy recording** — On a loud kitchen recording with a fan running, the presenter judged noise removal about 70% effective and said cleaner input would likely do better. ([3:03](https://youtu.be/P_7HwwUsOfA?t=183))
- **Clips and Clipper: highlight ranking is a black box with a large energy claim** — The model cuts long videos into ranked shorts via a desktop app. The presenter found the ranking weak for virality and noted there is no way to tune it. The 470x energy-versus-Sonnet claim was not tested. ([4:21](https://youtu.be/P_7HwwUsOfA?t=261))
- **Redact PII stripping misses obvious sensitive types but handles Latvian** — It redacts as you type across 27 languages. In the demo it did not catch a password or a Canadian SIN, but it did handle Latvian text. ([5:35](https://youtu.be/P_7HwwUsOfA?t=335))
- **Gist topic tagging is keyword-driven, not context-driven** — A space-travel article was tagged careers and productivity, and a science study was tagged arts and culture. The presenter said it is not production ready. ([9:47](https://youtu.be/P_7HwwUsOfA?t=587))
- **Tongue and Ear do language ID from text and audio with different tradeoffs** — Tongue (2 MB, tens of microseconds, 84 languages) got the test phrases right, including Latvian. Ear (99 languages, audio input) took about 10 s for English and 5 s for Latvian and French, and was wrong on Latvian. ([12:16](https://youtu.be/P_7HwwUsOfA?t=736))
- **Reported confidence tracked correctness in the Ear tests** — The wrong Latvian guess (Turkish) came with 29% confidence, while the correct French result came with 96%. The presenter did not draw a rule from this, but it is a usable signal. ([13:26](https://youtu.be/P_7HwwUsOfA?t=806))

## Techniques
- **Small specialist model as a background layer** — Split the pipeline: small on-device models handle narrow, high-frequency tasks (speech-to-text, filler removal, PII redaction, language ID, emoji suggestion), and a large cloud model handles reasoning. The lab frames this with a cerebellum analogy. *When:* High-volume, latency-sensitive or privacy-sensitive preprocessing where per-token cost or a server round trip is not acceptable.
- **Smoke-test a vendor micro-model on your own data inside a thin wrapper app** — The presenter wraps each model in a quick app (vibe-coded with Opus 5), runs it on an iPhone, and feeds it real recordings, typed text and several languages. He judges by output quality, timing and confidence values, not the vendor demo. *When:* Before committing to a small model. Check accuracy on your domain (noisy audio, your languages, your PII types), not on the marketing page demo.
- **Read the confidence score before trusting a language-ID result** — In the Ear test, the wrong answer came with 29% confidence and the correct answers with 96% and 100%. Use the reported confidence to decide whether to accept or fall back. *When:* Any classifier that returns a label with a score, such as language ID, when a wrong label is costly.

## Numbers
- 12 shipped models plus 5 in beta; free use up to 100,000 monthly active devices per platform ([1:15](https://youtu.be/P_7HwwUsOfA?t=75))
- Vaus claims 10 minutes of audio transcribed in about 2 seconds on-device; a 7-minute test clip took about 2 seconds ([2:24](https://youtu.be/P_7HwwUsOfA?t=144))
- Clips claims it clipped 100,000 30-minute videos using 470x less energy than Claude Sonnet for the same job (vendor claim, untested) ([4:21](https://youtu.be/P_7HwwUsOfA?t=261))
- Um claims under 20 ms to remove each filler and about 12 seconds for an hour of audio; in the demo it found 5 fillers in under a second ([7:02](https://youtu.be/P_7HwwUsOfA?t=422))
- Emo is about 5 MB on device and returns a suggestion in under 2 ms ([8:24](https://youtu.be/P_7HwwUsOfA?t=504))
- Gist claims 101 languages; it tagged 'full body workout' as health and fitness with 99% accuracy (presenter's figure) ([9:47](https://youtu.be/P_7HwwUsOfA?t=587))
- Tongue is about 2 MB, runs in tens of microseconds, and supports 84 languages ([12:16](https://youtu.be/P_7HwwUsOfA?t=736))
- Ear supports 99 languages; English was identified at 100% confidence in about 10 s, Latvian at 29% confidence (wrong) in 5 s, French at 96% in 5 s ([12:16](https://youtu.be/P_7HwwUsOfA?t=736))
- Clear's noise removal on an extreme kitchen recording was judged about 70% effective (presenter estimate) ([3:03](https://youtu.be/P_7HwwUsOfA?t=183))

## Hot takes
- The presenter calls the lab 'the coolest AI company out there' and praises its marketing pages, which is tone rather than evidence.
- Most numbers are vendor claims. Align (vs Apple's transcriber) and Clips' 470x energy claim were not tested, and no accuracy or WER metrics were computed for any model.
- The test inputs were ad hoc (a noisy kitchen recording, a 7-minute convention clip, typed sentences), so the results are anecdotes rather than a benchmark.
- The presenter says Gist is not production ready, Redact leaks passwords and national IDs, and Ear is too slow and unreliable for Latvian. These are the most useful negatives in the video.
- The closing claim that single-task micro models are the sensible future of on-device AI is opinion and is not supported by anything measured in the video.
- Relevance to us is thin: these are consumer-facing, on-device utilities, not server-side infrastructure for AgentOS, the gateway or ProsHarness. The only transferable idea is a small PII/redaction or classifier step.

## Tools mentioned
Desert Ant Labs (vendor, 12 shipped models plus 5 beta), Hugging Face (model hosting), GitHub (SDK), Vaus (on-device speech recognition, claims 10 min audio in ~2 s on iPhone), Clear (speech enhancement), Clips (highlight extraction from long recordings), Clipper (desktop app built on Clips), Title (short factual title and description from text), Redact (on-device PII stripping as you type, 27 languages), Um (filler-word removal), Emo (emoji suggestion, ~5 MB), Gist (topic and tag prediction from titles, claims 101 languages), Align (word-level timestamps from any transcriber), Shapes (hand-drawn strokes to vector shapes), Tongue (language ID from text, 84 languages, 2 MB), Ear (language ID from audio, 99 languages), Shemmer, Toxic, Moderator, Eye, Face (beta models, named), Opus 5 (used to vibe-code the test app), Claude Sonnet (comparison point for energy claim), Apple's transcriber (comparison point for Align)

## Relevance to our work
- **agentos** (1/3): Govrix Scout already has a PII/prompt-injection scan. Redact is an on-device PII redactor whose demo missed passwords and a national ID, which is a useful negative reference point. The cerebellum framing (small local models for background work, large model for reasoning) loosely matches the cheap-model pipeline interest. → *Compare a small on-device PII redactor against the Govrix Scout PII scanner on a labelled set that includes passwords and national IDs before adopting either.*
