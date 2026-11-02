# Grok Imagine Video 1.5, Qwen-VLA, NVIDIA Cosmos3-Nano, MiniMax M3, Bernini AI, Stax & More AI News

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `kQh9Hhr_eK0` · [watch](https://youtu.be/kQh9Hhr_eK0) · **date:** 2026-07-02 · **length:** 17:48 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** Kai (host, Kai Explains) · **orgs:** xAI, MiniMax, NVIDIA, Alibaba (Qwen team), ByteDance, Vast AI, Kai Explains (channel), Paddle (PaddlePaddle), pyannote, OpenMOS, Google Labs, Google, OpenAI, Anthropic
- **topics:** models-research, token-cost-efficiency, evals, local-ai · **tags:** news-roundup, open-weights, long-context, sparse-attention, robotics, vla, video-generation, 3d-gaussian-splatting, ocr, speaker-diarization, tts, eval-toolkit, pricing

> Weekly AI news roundup (Jul 2026): Grok Imagine Video 1.5, MiniMax M3 open-weight 1M-context model, NVIDIA Cosmos 3 Nano, Qwen VLA, ByteDance Bernini, plus OCR, diarization, TTS and Google Stacks eval toolkit.

## Summary
A Kai Explains weekly news roundup covering a batch of releases from the week of 2026-07-02. The most substantive items for engineers are MiniMax M3 (open weights, 1M context via a sparse attention scheme, with long autonomous-run demos and API pricing) and NVIDIA Cosmos 3 Nano (omnimodal mixture-of-transformers for video and robot action). Qwen VLA reports strong Libero and RoboTwin scores under Apache 2. Grok Imagine Video 1.5 claims the top image-to-video arena spot, with per-second pricing. Other items are brief: ByteDance Bernini (plan-then-render unified video edit/generate), TripoSplat (single image to 3D Gaussians), a 30B-A3B vision model, PaddleOCR 1.6, pyannote speaker diarization 3.1, MOSS TTS 1.5, and Google Labs' Stacks eval toolkit. Most items are presented as release announcements with benchmark claims the speaker does not verify. The content is a fast news pass, so each item gets one or two lines of detail, and the more useful ones are the MiniMax and Stacks items.

## Key ideas
- **MiniMax M3 is pitched as the first open-weight model combining frontier coding, a 1M-token context and native multimodality** — Speaker cites SWE-Bench Pro (59%, ahead of GPT 5.5) and BrowseComp (83.5, said to edge past Claude Opus 4.7). Weights are to be published shortly. Vendor claims, not independently checked. ([3:31](https://youtu.be/kQh9Hhr_eK0?t=211))
- **M3's long context rests on MiniMax Sparse Attention (MSA), claimed to cut per-token compute at long context to about 1/20th of full attention** — Speaker presents MSA as the mechanism that makes the 1M window practical, not just a spec. ([3:31](https://youtu.be/kQh9Hhr_eK0?t=211))
- **MiniMax's long-horizon demos are hour-scale autonomous runs, not short benchmarks** — One run had M3 reproduce an ICLR 2025 award paper over 12 hours (18 commits, 23 figures). Another optimized a Hopper GPU kernel over 24 hours, raising utilization from 7.6%, with no reference solution. ([4:40](https://youtu.be/kQh9Hhr_eK0?t=280))
- **NVIDIA Cosmos 3 Nano is a 16B omnimodal model that outputs video, audio and robot action trajectories from one prompt** — Uses a mixture-of-transformers design: an autoregressive transformer for discrete outputs such as text, and a diffusion transformer for continuous video, image and audio. Commercial and non-commercial use is allowed. ([6:00](https://youtu.be/kQh9Hhr_eK0?t=360))
- **Qwen VLA is an open Apache 2.0 vision-language-action model that claims strong zero-shot transfer across robot bodies** — Reports 97.9% on Libero, 87.2% on RoboTwin Hard, 76.9% out-of-distribution on real Aloha, and 26.6% zero-shot on domino manipulation. ([8:15](https://youtu.be/kQh9Hhr_eK0?t=495))
- **ByteDance Bernini uses a plan-then-render design for unified video generation and editing** — An MLLM acts as a semantic planner over the inputs and predicts the output; a DiT renderer then generates the video. One model handles V2V editing, reference-guided editing, content insertion and reference-to-video with up to five images. ([9:28](https://youtu.be/kQh9Hhr_eK0?t=568))
- **Grok Imagine Video 1.5 Preview tops the image-to-video arena and generates synchronized audio in one pass** — Scores 1473 ELO at 720p, a 52-point jump over the previous Grok Imagine version. Clips run 6 to 15 seconds. API pricing is $0.14 per second at 720p and $0.08 per second at 480p, against roughly $12 per minute for Google Veo 3.1 with audio. ([2:19](https://youtu.be/kQh9Hhr_eK0?t=139))
- **Google Labs' Stacks is a free eval toolkit that moves teams from vibe checks to custom datasets and evaluators** — Three stages: Experiment (compare models or prompts), Evaluate (managed dataset tests with custom evaluators), and Analyze (aggregated dashboards to decide when to ship). ([15:31](https://youtu.be/kQh9Hhr_eK0?t=931))

## Techniques
- **Plan-then-render for unified video generation/editing** — Use an MLLM as a semantic planner that reasons over the inputs and predicts the output, then a DiT renderer generates the video from that plan (Bernini's design, as described). *When:* When one model must handle several edit or generate modes and a single-shot prompt-to-video pass is too coarse.
- **Custom eval datasets with custom evaluators (Google Stacks workflow)** — Build a dataset of real product use cases, define evaluators or metrics that matter for the product, then run Experiment -> Evaluate -> Analyze as prompts, models or chains change. *When:* When you are replacing vibe checks or generic leaderboard scores with product-specific measurement before shipping.
- **Tiered upgrade path for diarization** — Start with the open-source pyannote speaker-diarization 3.1, move to Community-1 for better accuracy, then the hosted Premium model for production (the speaker's suggested path). *When:* When you need speaker-attributed transcripts and want to set a cost and accuracy ladder.

## Numbers
- MiniMax M3 SWE-Bench Pro: 59%, stated as ahead of GPT 5.5 (vendor claim) ([3:31](https://youtu.be/kQh9Hhr_eK0?t=211))
- MiniMax M3 BrowseComp: 83.5, stated as edging past Claude Opus 4.7 ([3:31](https://youtu.be/kQh9Hhr_eK0?t=211))
- MSA claimed to cut long-context per-token compute to about 1/20th of full attention ([3:31](https://youtu.be/kQh9Hhr_eK0?t=211))
- MiniMax M3 API pricing: $0.30 per 1M input tokens, $1.20 per 1M output tokens (speaker says >15x cheaper on input than Claude Opus 4.7 at $5 input / $25 output) ([4:40](https://youtu.be/kQh9Hhr_eK0?t=280))
- M3 long-horizon runs: 12 hours, 18 commits, 23 experimental figures; GPU kernel utilization 7.6% over 24 hours ([4:40](https://youtu.be/kQh9Hhr_eK0?t=280))
- Grok Imagine Video 1.5 Preview: 1473 ELO on image-to-video arena at 720p, +52 over previous Grok Imagine ([1:10](https://youtu.be/kQh9Hhr_eK0?t=70))
- Grok Imagine Video 1.5 pricing: $0.14/s at 720p ($1.40 for 10s), $0.08/s at 480p ([2:19](https://youtu.be/kQh9Hhr_eK0?t=139))
- Google Veo 3.1 cited at roughly $12 per minute with audio ([2:19](https://youtu.be/kQh9Hhr_eK0?t=139))
- Qwen VLA: Libero 97.9%, RoboTwin Hard 87.2%, real Aloha OOD 76.9%, zero-shot domino 26.6% ([8:15](https://youtu.be/kQh9Hhr_eK0?t=495))
- Cosmos 3 Nano: 16B parameters ([6:00](https://youtu.be/kQh9Hhr_eK0?t=360))
- Pyannote diarization 3.1: AMI DER 18.8%, VoxConverse 11.2%; Community-1: AliMeeting 24.5% to 20.3%, AMI-IHM 18.8% to 17.0% ([13:00](https://youtu.be/kQh9Hhr_eK0?t=780))
- Quai KeyVL2: 30B total, 3B active parameters per token ([10:45](https://youtu.be/kQh9Hhr_eK0?t=645))
- Pyannote usage: 140,000 registered developers, 45 million monthly Hugging Face downloads ([14:13](https://youtu.be/kQh9Hhr_eK0?t=853))

## Hot takes
- Speaker calls every item in the video useful, which is a sales-style framing; the segments are mostly release announcements that repeat vendor claims.
- Benchmark numbers (SWE-Bench Pro, BrowseComp, Libero, Grok ELO, MSA 1/20 compute) are presented as-is with no independent verification.
- The MiniMax long-horizon demos (12-hour paper replication, 24-hour kernel optimization) are the most substantive evidence in the video, but they are still vendor-run single examples.

## Tools mentioned
MiniMax M3, MiniMax Sparse Attention (MSA), NVIDIA Cosmos 3 Nano, Cosmos 3 Super, Qwen VLA, Grok Imagine Video 1.5 Preview, ByteDance Bernini, TripoSplat, Quai KeyVL2 (30B sparse MoE, 3B active), PaddleOCR 1.6 (ERNIE 4.5 backbone), pyannote Speaker Diarization 3.1, pyannote Community-1, MOSS TTS 1.5 (OpenMOS), Google Labs Stacks, Whisper, Hugging Face, GitHub, Libero, RoboTwin Hard, AMI, VoxConverse, OmniDocBench v1.6, SWE-Bench Pro, BrowseComp

## Relevance to our work
- **agentos** (1/3): MiniMax M3's 1M-context claim and cheap pricing are relevant to the InferCraft and cheap-model routing ideas, but the story is a vendor release and doesn't change the stack. → *Check the MiniMax M3 model card and MSA technical report when weights ship, and benchmark long-context retrieval against our vLLM setup before any routing change.*
- **prosharness** (1/3): Long autonomous runs (12h and 24h) are a data point for checkpoint/resume design, though they come from a vendor demo. → *Note the 12-hour and 24-hour autonomous-run figures as a stress-test target for ProsHarness checkpoint/resume.*
