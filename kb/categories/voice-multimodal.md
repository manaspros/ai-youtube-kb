# voice-multimodal — 153 videos

*voice agents, realtime, vision, video, computer use, browser agents*

By channel: AI Engineer 81 · Kai Explains 15 · AI LABS 17 · Better Stack 40

**Synthesized guide:** [guides/voice-multimodal.md](../guides/voice-multimodal.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [Voice AI Where One Wrong Question Breaks the Rules - Shiv Indap, Upstart & Brooke Hopkins, Coval](../videos/3osCbSufv8g.md)
`3osCbSufv8g` · AI Engineer · 2026-10-31 · q4 · practitioner · talk · also: evals, governance-compliance, observability

Coval and Upstart walk through a regulated voice-agent (lending verification calls) eval loop: human review, judge calibration, failure routing, and simulation before release.

- Techniques: Judge-human calibration loop; Structured human review queues; Clustering and anomaly detection for unknown failure modes; Failure-to-owner routing; Voice simulation before release; Feature-flagged agent changes with named approvers
- Tools: Coval (voice-agent evaluation and simulation platform), Google Sheets (initial manual review tracking), LLM-as-judge, RL pipelines and fine-tuned LLMs (mentioned as options for self-healing, not shown)

## [I Hid a Raspberry Pi in a Pumpkin to Fix Smart Speakers](../videos/t9Jro9BAIMw.md)
`t9Jro9BAIMw` · Better Stack · 2026-10-30 · q3 · intro · tutorial · also: local-ai, dev-tools

Better Stack builds a Raspberry Pi voice assistant inside a pumpkin: local wake word and speech-to-text, a fast remote LLM for replies, and remote TTS. Practical on latency and soldering, light on reproducible detail.

- Techniques: Wake word -> local STT -> remote fast LLM -> TTS voice loop; Pick the LLM on measured reply speed first, then check quality; Keep TTS remote when local voice quality or speed falls short; Solder to a separate hat, then mate it to the Pi header; Check clearance between solder joints and the cooler before power-up; Insulate the pumpkin's internals with cling film
- Tools: Raspberry Pi, Perma-Proto hat (Adafruit board, as named in captions), sherpa-onnx, Parakeet (speech-to-text model), Python, DeepSeek Flash, Gemini Flash, Haiku, ElevenLabs Flash, multimeter, active cooler (Raspberry Pi)

## [How to Build Voice Agents That Don't Fall Apart When You Interrupt - Jesse Hall, LiveKit](../videos/OmyqelTwpOo.md)
`OmyqelTwpOo` · AI Engineer · 2026-10-26 · q4 · practitioner · talk · also: evals, inference-serving

LiveKit's Jesse Hall argues voice agents must be evaluated as whole conversations: measure time-to-first-audio and time-to-first-sentence, use non-blocking tool calls, use audio-aware turn detection, and benchmark full stacks with simulated callers.

- Techniques: Time-to-first-audio and time-to-first-sentence instrumentation; Non-blocking (async) tool calls in a voice agent; Audio-aware turn detection; Full-stack scenario simulation with identical replay; Regression scenarios from production failures; Financial voice-agent guardrail checklist
- Tools: LiveKit (open-source real-time agent framework and infrastructure), LiveKit turn detector (audio + transcript end-of-turn model), LiveKit inference (model serving tuned for voice; speaker says it is model agnostic), Gemma 4 31B (auto-caption reads 'Gemma 431B'; top LLM on the hotel agent benchmark), ChatGPT advanced voice mode (cited as using LiveKit)

## [How to Build Financial Agents That Work Across the Web - Jay Sahnan & Arik Bird, Browserbase](../videos/DZ24Xbm9Joc.md)
`DZ24Xbm9Joc` · AI Engineer · 2026-10-25 · q2 · practitioner · review · also: sandboxing-execution, data-engineering, enterprise-adoption

Browserbase engineers pitch hosted, forked "verified" Chromium plus the open-source Stagehand SDK for running browser agents at scale on finance portals, with Ramp, Bill and Stripe as case studies.

- Techniques: Accessibility-tree page compaction before the LLM call; Hybrid deterministic plus natural-language browser control; Observe, act, extract as three separate primitives; Schema-first extraction with Zod; Single code path fanned out across many sites; Keep browser processes alive between tasks; Run the agent-side browser controller next to the browser; Copy-prompt onboarding for coding agents
- Tools: Browserbase (hosted browser infrastructure), Stagehand (open-source browser-control SDK built on Playwright), Playwright, Selenium, BeautifulSoup, Chromium (forked; Browserbase's verified build), Chrome, Zod, ngrok (used to share the demo), EC2 (named as the data-center example)

## [These 2 Tiny AI Models Run on Your Phone, Not the Cloud](../videos/7oWM2UEH2mg.md)
`7oWM2UEH2mg` · Better Stack · 2026-10-25 · q3 · practitioner · review · also: local-ai

Better Stack tests two beta on-device models from Desert Ant Labs: WHO (speaker diarization) and I (photo tagging, duplicates, aesthetic score). Fast local demos, but benchmarks are vendor-sourced and the license has a monthly check.

- Techniques: Diarize then merge with ASR by timestamp; Two-threshold tagging policy; Browser-side batch triage with WebGPU fallback; One-call multi-signal triage for photo cleanup
- Tools: Desert Ant Labs SDK 4.0 (beta), WHO (speaker diarization model, Desert Ant Labs), I (image classification and tagging model, Desert Ant Labs), PyAnnote (open-source diarization library, comparison baseline), Apple built-in speech transcriber (macOS), LiteRT.js (Google's web runtime for models), WebGPU, WebAssembly, Chrome, Node, Apple Neural Engine, Who Said What Where (the presenter's Mac app; GitHub link in the description)

## [This Looks Like Spy Software... It's Just Public Data](../videos/PQN76wcEt10.md)
`PQN76wcEt10` · Better Stack · 2026-10-23 · q3 · intro · review · also: mcp-and-tools, dev-tools, data-engineering

Walkthrough of God's Eye View, an open-source local globe that fuses public live feeds (planes, ships, satellites, cameras, quakes), with its feed-smoothing design and honest data caveats.

- Techniques: Run God's Eye View locally; Render the last update one step behind and interpolate; Dead reckoning for dropped feeds; Ration a free API quota with a budget; Hard spend cap for a realtime voice API; Unlock 3D tiles through an external key
- Tools: God's Eye View (open-source globe project, about 55,000 GitHub stars), Cesium JS, Vite, Node.js (24.14 or newer required; 25 unsupported), npm, SGP4 orbit model, ADS-B, AIS, OpenSky Network, MCP (Model Context Protocol) server, Claude, Codex

## [The AI Content System Behind 200M Views — Sarah Chieng, Cerebras & Cova Lee, OpenAI](../videos/CFbnVpSsDFQ.md)
`CFbnVpSsDFQ` · AI Engineer · 2026-10-22 · q3 · practitioner · workshop · also: context-engineering, skills-self-improvement, product-ux

Two creators (Cerebras and OpenAI DevEx) walk through a six-stage AI content pipeline: swipe-file ideation, voice-captured scripts, shot lists, agent-driven editing, captioning, scheduling and a periodic process-review skill.

- Techniques: Swipe-file reference library for agents; Build a voice skill from your own past content; Voice-first script interview; Outlier analysis against channel baseline; Two-pass shot list from a script; Organize footage before editing; Agent-driven editing via API or desktop control; Brand design system generated from your own videos; Background and visual enhancement with image generation; Fix mistakes with short inserts; Repurposing into short-form cut-downs; Scheduling with human approval; Remove AI tells from captions and prose; Weekly process-review skill
- Tools: ChatGPT, Codex (CLI, computer use; transcribed as 'Astra/Astro'), GPT-5.6 Sol Ultrafast (as named in the talk; runs on Cerebras at ~750 tokens/sec), Cerebras, Wispr Flow (transcribed as 'whisper flow'), Figma (MCP and plugins), Notion, Obsidian, HyperFrames (HeyGen), HeyGen (avatars), CapCut, Adobe Premiere

## [Speech Recognition Without the Internet Now Fits on a $10 Chip (Whistle)](../videos/bavO_V80ohM.md)
`bavO_V80ohM` · Better Stack · 2026-10-19 · q3 · practitioner · tutorial · also: local-ai, inference-serving

Andres from Better Stack runs Cactus's 16.9 MB Whistle speech-to-text model fully offline on a $10 ESP32-S3, trimming decoder layers and quantizing math to fit and speed it up.

- Techniques: Decoder layer trimming for flash-constrained devices; Keyword biasing on a constrained command vocabulary; Confidence-gated retry in another language; Use short phrases, not single words, as voice commands; Microcontroller inference speedups; Push-to-talk with local feedback
- Tools: Whistle (Cactus Compute speech-to-text model, Apache 2.0, on Hugging Face), Needle / Needle 2 / Needle 3 (Cactus models, referenced from earlier videos), Cactus Compute inference engine, ESP32-S3 microcontroller (16 MB flash, 8 MB RAM, 240 MHz), INMP441 digital MEMS microphone, OpenAI WhisperBase (comparison model, 145 MB), LibriSpeech (benchmark test set), A terminal UI app that shows transcript, LED state and per-step timing (unnamed)

## [This 164MB Speech Model Might Replace Whisper...](../videos/eskgvQYchd0.md)
`eskgvQYchd0` · Better Stack · 2026-10-19 · q4 · practitioner · review · also: local-ai, models-research

Review of "Phonon 2," a 164 MB local speech-to-text model from Fermion Research. It is fast and includes an OpenAI-compatible server, but the speed and accuracy claims rest mostly on the vendor's own benchmarks.

- Techniques: Local transcription setup; Live captions and hot words; Drop-in OpenAI-compatible speech server; Checking speed claims for the runtime, not just the model
- Tools: Phonon 2 (Fermion Research speech model), phonon CLI (transcribe, listen, serve), NVIDIA Parakeet (original 2.5 GB model), Parakeet Redux (178 MB, 1.58-bit weights, Moondream), Whisper Large V3 Turbo, whisper.cpp (Metal), MLX, Core ML, Fluid Audio (third-party Core ML port), OpenASR leaderboard, Python 3.10+, Fermion's Mac dictation app (named Detta in captions)

## [Every Building Is a Balance Sheet: Spatial Memory for Real-World Assets — Jordi Spranger, Spranic](../videos/Fe4aSMXsOZ4.md)
`Fe4aSMXsOZ4` · AI Engineer · 2026-10-14 · q2 · intro · talk · also: data-engineering, product-ux

Jordi Spranger (Spranic, with Neo4j) pitches walk-through 3D scans stored as a time-aligned graph, so real buildings become queryable, change-tracked data for insurance and lending.

- Techniques: Repeat-capture alignment and diffing; Graph as the world model; Provenance on every observation; Natural-language query over a graph map
- Tools: Neo4j, off-the-shelf 3D scanning sensor

## [Build with Perception Agents — Emile Baizel & Shruti Arora, Amazon AGI Lab](../videos/ZGzthw4BZiA.md)
`ZGzthw4BZiA` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: testing-verification, coding-agents, mcp-and-tools

Amazon AGI Lab hands-on workshop on Nova Act's open-sourced perception primitives: point-and-annotate a live page into JSON, run Gherkin-based visual verification, and wire both to a coding agent.

- Techniques: Deterministic visual annotation to JSON; Gherkin user flows auto-generated from a surface crawl; Browser extension to coding agent bridge; Automatic verification after every agent change; Voice or wearable transcript as an annotation source
- Tools: Amazon Nova Act, Nova Act SDK, Nova Act MCP server, Visual Annotator (Chrome extension), Visual verification skill, Claude Code, Kiro, Gherkin, Chrome, uv / uvx, Jam MCP, Atlassian MCP

## [Hill-Climbing Skills: Improve Agents Without Changing the Model — Shubhankar Srivastava, Browserbase](../videos/p7gaxmCUiIU.md)
`p7gaxmCUiIU` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: skills-self-improvement, evals, agent-architecture

Browserbase's Shubhankar Srivastava shows an auto-research loop in which a doer agent and a teacher agent iterate on a strategy file until browser-agent tasks converge into reusable skill.md files that cut cost and latency.

- Techniques: Teacher-doer auto-research loop with strategy file; Converged output as a skill.md artifact; Binary success verifier with minimal guardrails; Scheduled sample runs and failure-triggered healing; Three-layer security for learned skills; Objective choice in the teacher's criteria
- Tools: Claude Agent SDK, Claude Code, Codex, Opus 4.8, Sonnet, Browserbase browse CLI, Browserbase SDK, Stagehand, Browse.sh, WebMCP, Karpathy auto-research, OpenClaw

## [The Autonomous Computer: Infrastructure for Computer Use Agents — Ang Li, Simular](../videos/tyFPqtyOK5w.md)
`tyFPqtyOK5w` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: agent-architecture, evals, sandboxing-execution

Ang Li (Simular) on computer-use agents: why reliability needs a neurosymbolic loop, where the agent writes code that is replayed, and why pass^k matters more than pass@1.

- Techniques: Neurosymbolic replay with healing; Accessibility-tree grounding with IDs; Per-step observation choice; Clarification-first prompt; Reverse-check verification of entries; Rules-first guardrail chain; Exploration swarm for changing UIs; Test-time scaling by agent count; Save-to-skill with parameters
- Tools: Simular Agent S / S2 / S3 harnesses, Simuland (open-source scripting language), Claude Code, OSWorld, OSWorld 2, Playwright, Windows 365 for agents (Microsoft), Simular cloud desktop API and CLI, GPT-4V, GPT-5, GLM 5.2

## [I Turned My Wi-Fi Into a Surveillance System](../videos/9Tihk9_jUyo.md)
`9Tihk9_jUyo` · Better Stack · 2026-10-12 · q3 · practitioner · review · also: models-research, security-guardrails

Walkthrough of Wi-Fi sensing (RuView): the speaker critiques its headline accuracy, rebuilds a cheap ESP32-S3 setup, and trains a Wi-Fi-only pose model from camera labels.

- Techniques: Camera-supervised CSI training (teacher-student); Held-out environment evaluation for sensing models; Node-to-node links to multiply sensing lines; Edge-only label export for privacy; Visual node identification during setup
- Tools: RuView (open-source Wi-Fi sensing firmware and pose model; includes a fall detection feature), ESP32-S3 boards (about $10 each, three used), MediaPipe (Google, pose detection running in the browser), MacBook (ran the RuView pose model), MMFI public dataset (40 people, four rooms, camera plus Wi-Fi), 802.11bf (Wi-Fi sensing standard, mentioned as published last year)

## [The Tiny TTS Everyone Loved Isn't Tiny Anymore (KittenTTS 2)](../videos/9YzLI8-uF4s.md)
`9YzLI8-uF4s` · Better Stack · 2026-10-12 · q3 · practitioner · review · also: local-ai, governance-compliance

Hands-on review of KittenTTS 2: it has grown to 1.7B parameters, runs slower than real time on a Mac CPU, and ships source-available weights under a revocable, revenue-gated license, unlike the tiny Apache-2.0 original.

- Techniques: Clone a voice from a short reference clip; Check that the GPU is actually used; Turn off text normalization for non-English text; License gate before shipping model weights
- Tools: KittenTTS 2 (Kitten TTS v2), Kitten TTS (original, Apache 2.0), S3 Gen vocoder (Resemble AI, Chatterbox Turbo), Whisper (reference-clip transcription), PyTorch (torch), transformers, diffusers, Activity Monitor, ElevenLabs, VoxCPM2, libtorch (C++ port), Hugging Face

## [Can Your Agent Hear You Now? Building Live Voice Agents with Gemini — Thor Schaeff](../videos/xfPVBzDYjH4.md)
`xfPVBzDYjH4` · AI Engineer · 2026-10-12 · q2 · intro · demo · also: models-research, mcp-and-tools

A Google DeepMind developer-experience lead demos the Gemini Live API for real-time voice and vision agents, covering native-audio sessions, tool calls, live translation and stateful image generation. Mostly a product showcase with a few useful architecture points.

- Techniques: Stateful WebSocket session for real-time multimodal agents; Tool call from a live voice agent to a slow generator; Chaining generations with the previous interaction ID; Native audio vs cascaded voice pipeline
- Tools: Gemini Live API, Gemini 3.1 Flash Live, Gemini 3.5 Live Translate, Gemini TTS, Nano Banana Lite, Omni Flash, Lyria 3, Gemini Interactions API, Google AI Studio, LiveKit, Pipecat

## [Latency Is a Budget. Humanlike Is the Goal. — Jesse Hall, LiveKit](../videos/j4AmIK6OvHc.md)
`j4AmIK6OvHc` · AI Engineer · 2026-10-11 · q3 · practitioner · talk · also: evals, agent-architecture

LiveKit's Jesse Hall argues voice-agent latency is a budget to spend on human-like behavior, not raw speed, and shares audio-based turn detection, perceived-latency metrics, async tool handling and an outcome-scored simulated-caller benchmark.

- Techniques: Perceived-latency metric; Async tool with early turn release; Audio-based end-of-turn detection; Speculative LLM on provisional transcript, TTS on first sentence; Outcome-scored simulated-user benchmark; Stack-level model selection; Checklist for voice agents
- Tools: LiveKit (open-source real-time agent framework and infrastructure), LiveKit Inference (hosted model inference), LiveKit turn detector (audio-based end-of-turn model), Gemma 4 31B (tuned for voice on LiveKit Inference; auto-captions render it as 'Gemini 4 31B' at one point), ChatGPT advanced voice mode (cited as an example of a LiveKit-powered product), LiveKit voice eval harness and hotel-booking benchmark (open source)

## [How MiniMax M3 Was Built: Sparse Attention and Native Multimodality — Olive Song](../videos/htod7Nv1cBc.md)
`htod7Nv1cBc` · AI Engineer · 2026-10-11 · q4 · practitioner · talk · also: models-research, inference-serving

MiniMax's Olive Song explains how M3 adapts DeepSeek-style sparse attention to GQA with per-KV-head block selection, and why it was trained on vision and text from step zero.

- Techniques: Index-branch sparse attention; Per-KV-head selection under GQA; Block-level retrieval instead of token-level top-k; Native multimodal pretraining from step zero; Attention-map check for modality fusion; 3D attention in the ViT with a frame cap
- Tools: MiniMax M3, MSA (MiniMax Sparse Attention), DeepSeek DSA

## [The Transcript Looked Fine. The Call Wasn't. — Debugging Voice Agents, Arize](../videos/42Bz0TUfeOQ.md)
`42Bz0TUfeOQ` · AI Engineer · 2026-10-06 · q2 · practitioner · talk · also: observability, evals

Arize PM Fuad Ali on why voice agent failures are invisible in transcripts, and how to trace audio sessions, run audio-native evals, and close an observe-evaluate-improve loop. Partly a product pitch, with real open-source instrumentation content.

- Techniques: Session-stitched voice trace view; Provider-agnostic semantic conventions for LLM traffic; Audio-native evals for tone, latency and interruptions; Online evals on spans with monitors that trigger investigation; Replay failed traces against a patched endpoint to verify a fix
- Tools: Arize, OpenInference, OpenTelemetry, Grafana, WebSocket realtime API, GPT Realtime, Gemini Live, LiveKit

## [Your LLM Judge Is a Confident Liar: Building Better Verifiers — Browserbase](../videos/xLxhT2ZI7UM.md)
`xLxhT2ZI7UM` · AI Engineer · 2026-10-06 · q4 · practitioner · talk · also: evals, testing-verification, training-finetuning-rl

Browserbase and Microsoft researchers on why LLM judges confidently mis-grade web agents, and their rubric-and-evidence "universal verifier" that agrees with humans far better, plus its use for filtering training data.

- Techniques: Rubric-first LLM verification; Per-criterion top-K screenshot evidence; Dual verdict: partial-credit score plus boolean outcome; Controllable vs uncontrollable failure schema; Error isolation across dependent criteria; Human-agreement validation with held-out labels; Verifier as data filter for SFT; Auto-research loop to build a verifier, primed with human findings
- Tools: WebVoyager, Online Mind2Web (captioned as 'Online Minor Web'), OSWorld, GPT-4o, Opus 4.6, Cohen's kappa, Browserbase, Microsoft open-source web-agent framework (captioned 'StateGen')

## [This Speech Model Went From 1.2GB to 178MB (Parakeet Redux)](../videos/sr550syhwL0.md)
`sr550syhwL0` · Better Stack · 2026-10-05 · q3 · practitioner · review · also: local-ai, models-research

Moondream's Parakeet Redux compresses NVIDIA's Parakeet speech model from 1.2GB to 178MB using ternary weights, with near-equal English accuracy. The inference engine is closed, and noisy audio degrades more.

- Techniques: Quantized local speech-to-text on CPU; Word-level timestamps for subtitles; Transcribe a slice of a long recording; Live microphone streaming with replace-not-append handling; Language-agnostic input; Benchmark on your own hardware before trusting speed claims; Keep the original Parakeet for noisy audio
- Tools: Parakeet Redux (Moondream), NVIDIA Parakeet 0.6B v3, Parakeet.cpp, Whisper large-v3-turbo, whisper.cpp, PyTorch, Photon (Moondream inference engine, not open source), Kestrel kernels (proprietary license), Deepgram Nova 3, OpenAI mini-transcribe, Parakeet variant the speaker calls 'parakeet mix' (Apache-licensed; exact name unclear in captions)

## [We Built an AI Support Agent That Resolves 80% of Tickets — AssemblyAI](../videos/pyvRID_CZZU.md)
`pyvRID_CZZU` · AI Engineer · 2026-10-05 · q3 · practitioner · talk · also: agent-architecture, context-engineering, enterprise-adoption

AssemblyAI's FDE team built "Joey," a Claude Agent SDK support agent over local markdown docs, lifting end-to-end ticket resolution from 10% to 80% for about $700/month; the talk also argues for dogfooding your own product.

- Techniques: Docs-as-markdown synced into the agent's workspace; Two-stage retrieval: embeddings first, then agentic file search; Guardrail CLAUDE.md as the behavior-tuning loop; Escalation reason taxonomy as a product backlog; PaaS deploy from a Dockerfile for fast fix cycles; Monitoring through the existing support tool
- Tools: Claude Agent SDK, Claude Code, CLAUDE.md, Railway, Docker, Pylon, Voyage AI embeddings, AssemblyAI voice agent API, Slack, WebSocket

## [Why 99% Accurate Browser Agents Still Fail — Derek Meegan, Browserbase](../videos/5xi_S1f9sDU.md)
`5xi_S1f9sDU` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: testing-verification, agent-architecture

Why 99%-accurate browser agents still fail in production, and how moving deterministic steps out of the model and verifying outcomes makes transactional browser workflows profitable.

- Techniques: Three browser interaction strategies; Transactional scope for browser agents; Per-transaction success with bounded retries; Artifact-based success check; Single-transaction tool encapsulation; Deterministic auth outside the model; Skill as SOP for the critical path
- Tools: Browserbase, Chrome DevTools Protocol (CDP), OCR, accessibility tree, serverless functions

## [This AI Startup Is Making Powerful AI Models (Desert Ant Labs)](../videos/P_7HwwUsOfA.md)
`P_7HwwUsOfA` · Better Stack · 2026-10-02 · q3 · intro · review · also: local-ai, security-guardrails

Better Stack hands-on tour of 12 tiny on-device models from Desert Ant Labs (speech, redaction, language ID, emoji). Several are fast and useful, some are weak, and the vendor benchmarks are mostly unverified.

- Techniques: Small specialist model as a background layer; Smoke-test a vendor micro-model on your own data inside a thin wrapper app; Read the confidence score before trusting a language-ID result
- Tools: Desert Ant Labs (vendor, 12 shipped models plus 5 beta), Hugging Face (model hosting), GitHub (SDK), Vaus (on-device speech recognition, claims 10 min audio in ~2 s on iPhone), Clear (speech enhancement), Clips (highlight extraction from long recordings), Clipper (desktop app built on Clips), Title (short factual title and description from text), Redact (on-device PII stripping as you type, 27 languages), Um (filler-word removal), Emo (emoji suggestion, ~5 MB), Gist (topic and tag prediction from titles, claims 101 languages)

## [This Open-Weights TTS Beat ElevenLabs... Then I Read the License](../videos/kJppefEh2ZA.md)
`kJppefEh2ZA` · Better Stack · 2026-10-02 · q4 · practitioner · review · also: evals, local-ai

Josh from Better Stack tests Breeze TTS 2, an open-weights voice model that tops a benchmark, then shows why its non-commercial weights license blocks most real use.

- Techniques: Local voice-design install on macOS; Lower CFG scale to make voice descriptions stick; Inline vocal-event markup; License check before adopting open weights; Read leaderboards for vote count and prompt control
- Tools: Breeze TTS 2 (Breeze Blue), MLX audio (mlx-audio, pip install), Qwen 3, Qwen3-TTS, T5Gemma 2, Mimi audio codec, ElevenLabs Conversational, Cartesia Sonic 3.6, Artificial Analysis speech arena, Kokoro, Chatterbox, VoxCPM2

## [This Is What Voice Coding Was Supposed to Be (Qwen Audio Agent)](../videos/blpZ1xgFhCk.md)
`blpZ1xgFhCk` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: agent-architecture, coding-agents, multi-agent

Hands-on review of Qwen Audio Agent, an open-source voice runtime that keeps a voice conversation alive while Claude Code does slow coding work in the background over ACP. The main lesson is that voice coding is a concurrency problem, not a transcription problem.

- Techniques: Voice front-end + async coding back-end over ACP; Interruption as an explicit state machine; Local fast-path for trivial questions; Setup (as demonstrated)
- Tools: Qwen Audio Agent (open-source voice runtime, Apache 2.0; no model weights shipped), Claude Code (back-end coding agent), Codex, OpenCode, ACP (Agent Client Protocol), Alibaba DashScope (paid cloud voice API), OpenAI Realtime API (mentioned as comparison), PipeCat (mentioned as comparison), LiveKit Agents (mentioned as comparison), Whisper (dictation baseline), Hugging Face speech-to-text pipeline, MLX (Apple Silicon local backend)

## [Grok Bot Use Cases That Are Actually Insane](../videos/90pwPVrydHg.md)
`90pwPVrydHg` · AI LABS · 2026-10-02 · q2 · intro · review · also: multi-agent, testing-verification, product-ux

Walkthrough of GrokBot's eight use cases: a hosted, always-on bot group sharing one logged-in browser, used for app testing, support triage, monitoring and AI-search checks. Light on setup detail; sponsor and paid-tier plugs.

- Techniques: Role-bot test fan-out with a lead bot; Backend-verified UI failure triage; Agent-triggered test round; Support email to draft reply and PR; Fresh-account onboarding audit; Unbranded AI-search visibility check; Scheduled morning monitoring routine; Coordinator bot over functional bots
- Tools: GrokBot, Grok, SuperGrok, Cursor, Hermes, Claude Code, Codex, Supabase, Stripe, Gmail, Sentry, GitHub

## [Claude Code + GPT 6 Astra Just Killed AI Video Editing](../videos/p565AqELA8M.md)
`p565AqELA8M` · AI LABS · 2026-10-02 · q2 · practitioner · tutorial · also: claude-code, coding-agents, token-cost-efficiency

Tutorial for making agent-generated product videos in Claude Code: plan first, review in the browser, render shots one by one, then add music. Sponsored in part, and the title oversells it.

- Techniques: Route Claude Code to a Codex subscription via a local proxy; Plan-first with browser preview, comments, and an explicit lock; Render shots individually at full resolution, approve, then fix; Polish and combine with explicit timing; Music skill driven by plan style and shot cadence
- Tools: Claude Code, GPT-6 Astra (OpenAI model, accessed through Codex), Codex, CLI Proxy API, Homebrew (brew), Hyperframes (video-creation tool with skills), Mixkit (free music library), Luma Ray 3.2 (sponsor), Ray 3 (comparison), Kling 3.0 (mentioned in sponsor segment), Gen 4.5 (mentioned in sponsor segment), Fable (model compared to Astra on design in an earlier video)

## [Modality Misalignment and Originality Attribution in Short-Form Video — Aditya Gautam, Meta](../videos/jNE8No-wvok.md)
`jNE8No-wvok` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: multi-agent, evals, training-finetuning-rl

Meta's Aditya Gautam on using a multi-agent system of small domain-tuned VLMs to find intra-video policy anomalies and duplicate content in short-form video, with a production judge-and-human feedback loop.

- Techniques: Orchestrator plus specialist agents for video review; Change-based frame compression; Per-signal index routing; Domain pre-training plus schema-constrained instruction tuning; Judge-plus-human-queue production loop; Distillation plus quantization sweep; Node-level evaluation suite; Pre-inference gating with cache and metadata
- Tools: CLIP, MCP, Ray, DPO, JSON schema, vector database, graph database, inverted index

## [World Models Need Causality, Not Pretty Pixels — Christopher Manning, Moonlake AI](../videos/4Gqg0HVe-AY.md)
`4Gqg0HVe-AY` · AI Engineer · 2026-09-27 · q3 · intro · talk · also: models-research, training-finetuning-rl

Christopher Manning of Moonlake AI argues that world models for physical AI need abstracted, causal, editable representations rather than beautiful pixels, and proposes code-based neurosymbolic simulators that can be verified and used for sim-to-real transfer.

- Techniques: Action-conditioned semantic world model; Code as the controllable scene representation; Render-compare-revise loop; Retrieval to fill unobserved state; Task-driven fidelity budgeting; Neural sim-to-real gap reduction
- Tools: Genie 3, Marble, JEPA, Claude, physics engines, diffusion models, RAG over web search

## [The Best Models Still Reason Like Toddlers — Andrew Dai, Elorian](../videos/A_I8mw8yfns.md)
`A_I8mw8yfns` · AI Engineer · 2026-09-27 · q2 · intro · talk · also: models-research, evals

Elorium's CEO argues frontier models (Claude, ChatGPT, Gemini) pattern-match instead of reasoning over images and video, and proposes visual chain-of-thought trained on synthetic data as the fix.

- Techniques: Keep visual sub-tasks simple; One-second test for task difficulty; Visual chain of thought; Synthetic data flywheel for a hard modality; Programmatic or simulator validation of outputs
- Tools: Google Lens, SAM3, YOLO, Mask R-CNN, Siemens simulators, ByteDance Seedance (rendered as C-Dance in transcript)

## [Skill issue: stop deploying vision language models, use them with Skills — Merve Noyan, Hugging Face](../videos/dKcTBQzR7jI.md)
`dKcTBQzR7jI` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: data-engineering, training-finetuning-rl, evals

Merve Noyan (Hugging Face) argues against running VLMs for real-time vision and shows a pipeline where VLMs label and judge data to train small Apache-2.0 detectors such as RF-DETR, plus a toolkit of models exposed as agent tools.

- Techniques: VLM as offline labeler, small detector at runtime; Overlay-and-ask judging; Ensemble of small judges with any-yes merge; License-first model selection; Agent with domain rules and human checkpoints; Models exposed as agent tools
- Tools: RF-DETR, Gemma 4 E4B, LFM2.5-VL, Qwen VLM (auto-caption reads 'Q1 3.5', ~3.5B), Falcon Perception, Moondream 3, MM Grounding DINO, SAM 3.1, Supervision (Roboflow), Hugging Face Jobs, Hugging Face Inference Providers, Hugging Face buckets

## [From VLM/VLA's to Embodied Agents — Armen Aghajanyan, Perceptron AI](../videos/ZZcE0HeO-Hc.md)
`ZZcE0HeO-Hc` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: models-research, training-finetuning-rl

Perceptron's CEO argues VLMs, VLAs and world models should merge into one "embodied foundation model," and shares sparsity, token-routing and data-mix findings with public benchmarks but few hard details.

- Techniques: Data-sparse MoE token routing; Agentic detection with zoom, tiling and contrast; Orchestrator plus low-level control policy; Self-verifying video annotation; Online augmentation for robustness; Patch averaging for token compression
- Tools: Gemini 3.1 Pro, Gemini Embodied Reasoning, Perceptron models (Mark 1)

## [Robotics Has Been Stuck for 70 Years — Deepak Pathak, Skild AI](../videos/jFHteJjRl8A.md)
`jFHteJjRl8A` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: training-finetuning-rl, models-research, data-engineering

Deepak Pathak (Skild AI) argues robotics lacks internet-scale data, so the answer is one omnibodied brain pretrained on diverse data, post-trained on teleop, and improved by a deployment data flywheel.

- Techniques: Pretrain on diverse, scalable data, post-train on small high-quality teleop; Deployment data flywheel; End-to-end camera-to-motor policy with only a low-level PID loop; Learn from human video, then adapt with minimal robot data; Cross-embodiment zero-shot transfer

## [One Operator, Many Drones: Inside Skydio's Autonomy Stack — Suchet Bargoti, Skydio](../videos/2wgPHvW0mG8.md)
`2wgPHvW0mG8` · AI Engineer · 2026-09-27 · q3 · intro · talk · also: multi-agent, agent-architecture, infra-cost-scaling

Skydio's Suchet Bargoti on running fleets of docked drones as agent-commanded infrastructure: tool-based VLM control, edge/cloud latency tiers, a shared map that the fleet updates, and a learning flywheel.

- Techniques: Tool-exposed primitives for a VLM agent; Latency-tiered edge and cloud split; Fleet-shared map with sync-back; Bandwidth-aware video encoding for cloud agents; Hybrid end-to-end versus hand-engineered decomposition; Log, sanitize, retrain, redeploy loop
- Tools: Vision-language model (VLM), Reinforcement learning, Drone APIs exposed as agent tools, Cloud GPUs and inference engines, Map merging and sync service

## [Robot Demos Are Easy. Reliability Is Hard — Jason Ma, Dyna Robotics](../videos/Sjfz1TqxzEs.md)
`Sjfz1TqxzEs` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: training-finetuning-rl, evals

Dyna Robotics co-founder on making generalist robot manipulation policies reliable enough for commercial use, via reward-model progress scoring and a targeted active-learning loop.

- Techniques: Reward model as progress scorer for background supervision; Failure-driven active learning loop; Pre-train, post-train, then active learn; Grade-based success criteria tied to customer acceptance; Two-level architecture

## [I Gave an AI a Body — Cyrus Clarke, MIT Media Lab](../videos/jgWY66RaSrQ.md)
`jgWY66RaSrQ` · AI Engineer · 2026-09-27 · q3 · intro · talk · also: product-ux, agent-architecture

MIT Media Lab researcher Cyrus Clarke gives an OpenClaw agent a 900-pin shape display and has it build its own gesture vocabulary, arguing for non-humanoid, aesthetics-led physical AI.

- Techniques: Closed-loop gesture generation with gates and scoring; Pre-authored action repertoire to cut latency; Neutral embodiment with no affordances; Open-ended exploration prompt with machine access
- Tools: OpenClaw, openFrameworks, Numalab (speaker's own system), Shape display (physical pixel grid, 900 pins)

## [From Scratch to SOTA: Training a 3B State-Space Vision Model — Krishna Prasad Srinivasan, Sarvam](../videos/T72nqdC92PM.md)
`T72nqdC92PM` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: data-engineering, training-finetuning-rl, models-research

Sarvam's Krishna Prasad Srinivasan on training Servam Vision, a 3B state-space document-OCR model built from scratch for English and 22 Indian languages, using block-level OCR, a four-stage curriculum and RL with machine-checkable rewards.

- Techniques: Block-level OCR with layout and reading-order modules; Four-stage training curriculum for a domain VLM; RLVR with unit-test rewards; Real complex documents as RL reward sources, synthetic documents for SFT; Human-in-the-loop workbench with confidence scores and block grounding
- Tools: Servam Vision, Akshar (agentic document workbench), OlmOCR-Bench, OmniDocBench, Qwen, Gemma

## [Physical AI's Next Bottleneck Is Finding the Right Video — Rafael Levi, Bright Data](../videos/I_VEh7XSwyc.md)
`I_VEh7XSwyc` · AI Engineer · 2026-09-27 · q2 · intro · talk · also: data-engineering

Rafael Levi (Bright Data) argues physical-AI training is limited by usable action data, not models, and pitches searching indexed public video by action before collecting it.

- Techniques: Action-based clip retrieval before collection; Frame-to-frame motion estimation from plain video; Descriptive queries for retrieval
- Tools: Bright Data video indexing API

## [The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](../videos/XsvUhpnHepE.md)
`XsvUhpnHepE` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: mcp-and-tools, infra-cost-scaling, token-cost-efficiency

Oxylabs' Giedrius Šteimantas argues web-using agents need a scraping infrastructure layer: use browsers only when required, validate content before it reaches the LLM, and fix the failing discovery and purchase stages of a shopping agent.

- Techniques: Validate page content before the LLM sees it; Search API for discovery, not a browser; Tiered web access: API first, browser last; Markdown and geolocated output from the scraper; Drop-in managed browser for Playwright MCP
- Tools: Playwright MCP, Oxylabs Fast Search API, Oxylabs Web Scraper API, Oxylabs Headless Browser

## [SOTA Generative Media Panel — Dumitru Erhan, Shane Gu & Nicole Brichtova, Google DeepMind](../videos/KLDdXOw6jIc.md)
`KLDdXOw6jIc` · AI Engineer · 2026-09-18 · q3 · practitioner · panel · also: models-research, evals

Google DeepMind panel on generative media (Veo, Gemini Omni, Nano Banana): why language is a lossy conditioning channel, why human preference evals mislead, and why real-task data and FDE feedback matter.

- Techniques: Side-by-side human preference eval for close model comparisons; Deterministic checks for rendered text; Early-access programs before broad release; Amortizing human labels into a learned evaluator; Joint generation of coupled modalities in one model
- Tools: Veo 3, Gemini Omni, Nano Banana, Nano Banana Pro, Nano Banana 2 Lite, Manim, FFmpeg, Stable Diffusion, OCR

## [Realtime Voice Agents with Frontier Intelligence — Bohan Li, EliseAI](../videos/MBHOH1NmDqc.md)
`MBHOH1NmDqc` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: agent-architecture, inference-serving

EliseAI's Bo Li explains a cascaded voice-agent harness (streaming transcription, background tool calls, prefix-cached TTS) that keeps frontier-model intelligence at real-time speed.

- Techniques: Streaming speculative transcription (two-tier ASR); Early generation with background tool calls and cancellation; Word-sequence prefix cache for TTS; Playback deduplication after speculative TTS
- Tools: Flux (fast streaming transcriber), Scribe V2 (accurate batch transcriber), Cartesia (TTS with WebSocket support)

## [Tolan: Voice-First AI Companion — Paula Dozsa, Tolan](../videos/xLUQOqjudtA.md)
`xLUQOqjudtA` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: memory, context-engineering, software-factory

Tolan's engineers explain how a voice-first AI companion needs sub-two-second turns, stakes-based model routing, retrieval-style memory, and per-turn context rebuilding, plus how they use Claude agent fleets to ship iOS code.

- Techniques: Smart turn-taking from speech patterns; Per-stage latency instrumentation; Stakes-based model tiering with a cheap per-turn router; Retrieval-based memory with nightly consolidation; Stable-versus-volatile memory blocks; Character identity held separately from tone; Multi-judge eval loop for persona changes; Agent fleet with reviewer and PR-shepherd roles
- Tools: Claude, GPT-5.1, OpenAI Responses API, MCP, Linear, Sentry, Datadog, App Store

## [Your Voice Agent is Just a Walkie Talkie — Neil Zeghidour, Gradium](../videos/a8EcVumh71E.md)
`a8EcVumh71E` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: agent-architecture, models-research

Gradium's CEO traces voice agents from Siri to speech-to-speech models, explains why full-duplex needs multi-stream audio, and argues for a small full-duplex front end delegating to a background text LLM.

- Techniques: Audio tokenizer (neural codec) before the LLM; Multi-stream full-duplex modeling; Split front-end / background-LLM voice architecture (MoshiRAG)
- Tools: Moshi, Hibiki, GPT Realtime, OpenAI advanced voice mode, Siri, Claude Sonnet 5

## [Generative Video at the Speed of Light — Keegan McCallum, uRun](../videos/Xln-On3syJk.md)
`Xln-On3syJk` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: inference-serving, infra-cost-scaling

Keegan McCallum (uRun) argues generative video is improving on efficiency and long-horizon generation as well as quality, and describes the infra needed for real-time interactive video apps.

- Techniques: Distill a large video model for real-time serving; Real-time steering instead of prompt-and-reroll; Multi-model streaming pipeline with per-frame control sync; Wrap real-time video as a React component plus Python runtime; Agent-facing access via CLI and MCP server
- Tools: Helios, Wan 2.1 14B, WebRTC, ICE, TURN, React, Python async runtime, MCP, CLI, Sora, Sora 2, Seedance

## [Act, Confirm, or Stop? Smarter behavior for AI assistants, wearables & robots — Amit Desai, Roku](../videos/Zd5b40Jbp_k.md)
`Zd5b40Jbp_k` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: product-ux, evals

Voice assistant satisfaction can rise without better accuracy: gate act/confirm/stop on calibrated confidence and pick thresholds by minimizing a user-cost function ("ouch").

- Techniques: Outcome user-cost minimization for act/confirm/stop; Two-threshold three-band policy with grid search; Sensitivity check on unit costs
- Tools: Interactive threshold-sweep graph built with a coding assistant (no specific library named)

## [Voice Agents Can Just Do Things — Charlie Guo, OpenAI](../videos/OpY6MmZFeHo.md)
`OpY6MmZFeHo` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: mcp-and-tools, product-ux

Charlie Guo (OpenAI) argues voice agents need not always talk back and lays out three voice modes (speech-to-speech, speech-to-action, event-to-speech), with GPT Realtime 2 as the example stack.

- Techniques: Three-mode voice design; Expose app verbs as tools; Escalating attention ladder; Preamble prompting; Native audio streaming; Role-first voice design checklist
- Tools: GPT Realtime 2, OpenAI Realtime API, Codex, ChatGPT advanced voice mode, CarPlay, Google Maps, Spotify

## ["My name is... my name is...": A Linguistic Map for Voice Agents — Midam Kim, ServiceNow](../videos/IDNfAZVKvPE.md)
`IDNfAZVKvPE` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: evals, product-ux

Midam Kim (ServiceNow) uses a linguistics framework to explain why voice agents fail and proposes diagnosing them by listen/speak channels, timing, and the user's mental model.

- Techniques: Linguistic diagnostic grid for voice agents; Interactive clarification on recognition errors; Locale-aware pre-processing for TTS and vocabulary; Turn-taking and barge-in control; Dynamic per-call context retention; EvaBench for diagnosing voice agents
- Tools: EvaBench

## [Tell the Robot What You Want — Sandhya Subramani, AWS](../videos/S6aSoQ6_u5A.md)
`S6aSoQ6_u5A` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: multi-agent, agent-architecture

Live demo of a rover robot driven by an LLM agent built on the Strands harness, with a four-layer agent-to-hardware stack and a pitch that VLA policies may eventually make per-task robot training unnecessary.

- Techniques: Robot as an agent tool; Concurrent specialized agents on one tool surface; Edge/cloud policy split; Teleop for dataset creation; Messaging-app control over cellular
- Tools: Strands Agents (agent SDK), Amazon Bedrock AgentCore, Claude Opus 4.8, OpenAI Realtime (voice), Telegram, Raspberry Pi, VLA models, 4G SIM

## [Speech-to-Speech Model Research at Google DeepMind — Valeria Wu Fon & Tom Ouyang, Google DeepMind](../videos/18Um2VjMM_g.md)
`18Um2VjMM_g` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: models-research, product-ux

Google DeepMind's Gemini speech-to-speech team explains why one natively multimodal, promptable model beats cascaded ASR+LLM+TTS for voice agents, with live translation, Search Live and Live API demos.

- Techniques: Native multimodal pretraining for audio tasks; Streaming translation as a prompt; Proactive audio gating; Managing the latency vs intelligence knob; One promptable model for many modes
- Tools: Gemini Live, Search Live, Gemini Live API, Google Meet speech translation

## [Building an Agentic Video Editor for Mass Consumer — Ekaterina Deyneka, Reelful](../videos/pPj_tjlvYjA.md)
`pPj_tjlvYjA` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: sandboxing-execution, product-ux, testing-verification

Reelful's founder shows how an agentic video editor turns real footage into a clip: media understanding, a user-approved plan, a sandboxed agent with skills, Remotion rendering, and a verification loop.

- Techniques: Sandbox per approved job; Plan approval gate; Skills as encoded craft; Code-defined render target; Verification-then-reiterate loop; Directional templates plus manual editor fallback
- Tools: Remotion, React

## [5 Voice Agent Failure Modes You'll Hit in Week One — Venky B, Plivo](../videos/vblnYHzBgS4.md)
`vblnYHzBgS4` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: inference-serving, data-engineering, evals

Venky B of Plivo lists five voice-agent failure modes seen in production (latency, transcription, data collection, TTS output, barge-in) and the fixes his team uses. Main takeaway: treat voice as a structured pipeline problem, not a prompt problem.

- Techniques: Per-stage latency budget with time-to-first-audio as the metric; Self-hosted small or MoE open model for the conversational LLM; Dynamic keyword boosting per call phase; LLM post-processing of STT output with domain context; Typed field schema with validation and confirmation for data collection; Field-level unit-test evals for voice agents; Normalization layer between LLM and TTS; Pronunciation smoke tests with known hard names
- Tools: LiveKit, Pipecat, Pydantic, Zod, Qwen 3.5, Gemma 4, Cerebras, Groq

## [While my guitar gently speaks — Todd Fisher, Philo Ventures](../videos/E_Txocq-Lrw.md)
`E_Txocq-Lrw` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: vibe-coding-app-building, product-ux

A guitar that speaks and sings: pitch detection, word slicing, vocoder synthesis and a local Whisper-to-LLM loop. Mainly a call to build passion projects with AI.

- Techniques: Energy-gap plus sonority-peak word segmentation; YIN pitch detection to synthesized tone to vocoder; Pre-bake heavy DSP, then map to controls; Local voice loop: STT, then local LLM, then TTS; Plugin packaging inside a DAW
- Tools: JUCE, Logic Pro, Piper TTS, Whisper, YIN pitch algorithm, WORLD vocoder/pitch-shift, VocalSet, Apple built-in TTS

## [The Next Medium: Why Real-Time Interactive Video Changes Everything — Ahmed Ahres, Reactor](../videos/5dCAmSDOAjI.md)
`5dCAmSDOAjI` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: inference-serving, product-ux, infra-cost-scaling

Ahmed Ahres (Reactor) argues real-time interactive video and world models will change how content is made and consumed, then describes the infra gaps: streaming, session memory, and sub-100 ms global latency. Mostly a company pitch.

- Techniques: Stream frames over a live session instead of returning a file; Regional GPU routing for a latency budget; Session memory to keep generated worlds consistent; Multi-GPU serving plus quantization for cost and speed; Human-in-the-loop evaluation for real-time output
- Tools: Reactor API (real-time world model platform, roughly 10 lines to integrate per the speaker), Helios (ByteDance, interactive video model), LingBot (Alibaba, world model), LongLive 2 (NVIDIA, multi-shot film model), StreamDiffusion (NVIDIA, video-to-video; transcript reads 'SoundCloud Streaming', likely a caption error), Veo, Sora, Genie 3 (mentioned as comparisons)

## [200 Million Patient Interactions Later — Vivek Muppalla, Hippocratic AI](../videos/AN65uc645mE.md)
`AN65uc645mE` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: inference-serving, evals, multi-agent

Hippocratic AI's engineering lead explains how their clinical voice agent (200M+ patient conversations) hits safety, latency and accuracy at once: a vertically built stack, 31 parallel specialist models, context-fed ASR, and lossless inference tricks.

- Techniques: Parallel specialist models with self-gating; Context-conditioned ASR; Second-pass rescoring for ambiguous short utterances; Async and offline verifiers for tool calls; Human plus synthetic eval mix with sample-size planning; Severity-graded harm rubric; Lossless inference stack
- Tools: Whisper (large-turbo, fine-tuned), speculative decoding, 4-bit quantization, KV cache

## [Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia](../videos/McknwOzbmyg.md)
`McknwOzbmyg` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: evals, testing-verification, product-ux

Jared Joselowitz (Ufonia) on shipping a clinical voice agent to patients without A/B tests or rollback, using simulated patients, a calibrated LLM judge, and prompt optimization gated by hazard-linked evidence.

- Techniques: Hazard-first safety case; Scenario-conditioned simulated user; Calibrated LLM judge; Reflective prompt optimization (GEPA) with a cost-weighted metric; Synthetic edge-case generation; Staged gated rollout with evidence-based autonomy; Pin prompt versions and keep full traces
- Tools: Matrix (internal simulation framework), PatBot (internal LLM patient), BevJudge (internal LLM judge), GEPA (genetic-Pareto prompt optimizer), DSPy (mentioned as the origin of GEPA), Gemini 2.5 Pro (judge model at the time of the paper)

## [Voice agents with Realtime Video — Sidney Primas, LemonSlice](../videos/z1dqv74SpUs.md)
`z1dqv74SpUs` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: inference-serving, agent-architecture

Lemon Slice's CTO explains how they build real-time, photorealistic video avatars from a causal video model, covering past-only attention, one-step denoising, long error-free runs, and a GPU/CPU harness that keeps streams stutter-free.

- Techniques: Causal (past-only) attention mask for streaming video; Collapse denoising steps for real-time output; Expressive audio encoders over default ones; Real-time model harness (GPU/CPU orchestration); Two-layer EQ/IQ split

## [1 Trillion Phone Calls/yr, 10% Error rate: The Crisis in Voice AI — Sumanyu Sharma, Hamming AI](../videos/qStB9GbppMU.md)
`qStB9GbppMU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: evals, observability, security-guardrails

Hamming AI's CEO argues voice agent errors (about 10% in practice) are the top deployment blocker, and offers a loop to find, prioritise, test and red-team failures across many calls.

- Techniques: Frequency and severity triage matrix; Scenario-variation regression testing; Production A/B testing for voice fixes; Cross-conversation pattern analysis; Continuous adversarial red-teaming

## [This 2B Model Cloned My Voice Locally (VoxCPM)](../videos/O4TMwZlUJvQ.md)
`O4TMwZlUJvQ` · Better Stack · 2026-09-02 · q3 · practitioner · tutorial · also: local-ai, inference-serving

Tutorial on running OpenBMB's 2B VoxCPM2 TTS locally for speech generation, voice design from text, and voice cloning, with a clear list of where it falls short versus hosted APIs.

- Techniques: Prototype the voice in a hosted demo before any infra work; Local install and minimal generation script; Turn the model into a service behind the OpenAI speech API; Voice design from a persona description; Voice cloning from a short reference, with transcript; Set the output language explicitly for multilingual speech
- Tools: VoxCPM / VoxCPM2 (OpenBMB, Apache 2.0, ~2B params), PyTorch, torchaudio, Python, vLLM, Hugging Face (demo and checkpoint), macOS afplay, ComfyUI, GGUF, MLX (community paths mentioned), Chatterbox (TTS comparison), Qwen3-TTS (TTS comparison), ElevenLabs (hosted TTS comparison)

## [Someone Built Ollama for Audio… and It Runs Locally](../videos/CvZuuKkT3Sw.md)
`CvZuuKkT3Sw` · Better Stack · 2026-09-02 · q3 · intro · review · also: local-ai, inference-serving

Walkthrough of Audio CPP, a month-old GGML single-binary runtime for about 30 local audio model families (TTS, STT, voice cloning, music); early and crash-prone, with speed claims measured only on NVIDIA.

- Techniques: Single-binary local audio runtime; OpenAI-compatible local audio server; Voice cloning from a short reference clip; Validate speed on your own hardware
- Tools: Audio CPP, GGML, llama.cpp, whisper.cpp, Ollama, Kokoro, Piper, FFmpeg, PyTorch, MLX, CUDA, Vulkan

## [xAI are killing it (Grok 4.6, Image 2.0 and more...)](../videos/ILHJqmJdWso.md)
`ILHJqmJdWso` · Better Stack · 2026-09-02 · q3 · intro · review · also: models-research, coding-agents, token-cost-efficiency

Better Stack walkthrough of xAI's recent releases: Grok 4.6 benchmarks and cost, Grok Imagine image and video editing, Grok Build and Cursor, and a voice agent builder. Main takeaway: list price is not total cost.

- Techniques: Compare models by cost per completed task, not list price; Element-level re-prompting of a generated image; Multi-image virtual try-on with a template; Voice agent with tools and a phone number
- Tools: Grok 4.6, Grok 4.7, Grok Imagine, Grok Build, GrokBots, Grok voice agent builder, Cursor, Composer 2.5, Cursor auto router, Claude Code, Codex CLI, Claude Cowork

## [Bringing agents onto the world wide web — Paul Klein IV, Browserbase](../videos/GqoNrUz8hEU.md)
`GqoNrUz8hEU` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, security-guardrails, mcp-and-tools

Paul Klein (Browserbase) argues reliable browser agents are a harness, tooling and infrastructure problem rather than a model problem, and lays out a multimodal, harness-engineered, consistently hosted approach.

- Techniques: Hybrid code-plus-browser execution; Per-site skill packs loaded before visiting; Compressed page representation; Pinned, consistent browser environment; Sites expose WebMCP tool calls and agent-first auth; Observability-to-self-improvement loop
- Tools: Browserbase, Browse.sh, WebMCP, Playwright CLI, Claude Code, Operator, Cursor, Factory, OpenClaw, WorkOS AuthMD, web bot auth, auto-browse

## [Don't Let the LLM Drive - Ornella Bahidika & Joel Allou, Microsoft](../videos/m24UKZomm7k.md)
`m24UKZomm7k` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, context-engineering

Microsoft's ACE live voice tutor: run a lesson as a state machine where the model only proposes narrow outputs and a harness validates them and decides the next step.

- Techniques: Lesson-as-state-machine harness; Per-step narrow prompts; Model proposes, harness decides; Right-size the model to the harness; Reliability coin-flip test
- Tools: Claude Opus 4.7, Claude Haiku 4.5

## [From RL to IRL — Gaurav Mishra, Amazon AGI Lab](../videos/Cc0_nyxROBA.md)
`Cc0_nyxROBA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: training-finetuning-rl, agent-architecture, security-guardrails

Gaurav Mishra (Amazon AGI Lab) on why RL-trained computer-use agents break on real login screens, ads, and expired sessions, and how to adapt training and the harness to real-world messiness.

- Techniques: Simulated messy environments for agent RL; Recovery as a native model action; Process reward model over the trajectory; Action risk classifier in the harness; Harness-level credential and loop guardrails; Checkpoint, rollback, and audit trail; Forced human handoff; Adversarial tasks in mainstream training; Design-partner failure loop
- Tools: Playwright, WebMCP, MCP, web search APIs, PPO, GRPO

## [Computer-use models will agentify the web, not APIs — Dhruv Batra, Yutori](../videos/Ki980nV0__0.md)
`Ki980nV0__0` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, infra-cost-scaling

Dhruv Batra (Yutori) argues the long-tail web will be driven by pixel-based computer-use agents rather than new APIs, and shows his Navigator model's accuracy and cost per task.

- Techniques: Screenshot-in, action-out computer-use loop; Code-on-demand as a browser action; Pixel-based success check; Parallel sandboxed-browser fan-out; Read the async data call, not the initial HTML; Cost-per-task as the headline metric
- Tools: Navigator (Yutori computer-use model), OnlineMind2Web benchmark, Chrome extension for browser actions, MCP servers and web MCP, Opus 4.7 and GPT 5.5 (comparison models), Cloud sandbox browsers

## [Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs](../videos/mOf-PP4mVjA.md)
`mOf-PP4mVjA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: memory, rag-retrieval, agent-architecture

TwelveLabs' James Le argues video needs a persistent memory layer (a context graph over moments, entities and relationships) rather than frame sampling, search or long context, and demos a video agent called Jockey.

- Techniques: Context graph over video moments; Ingest once, reason many times; Timestamp-grounded outputs; Intent-configurable extraction; Video worker harness; Evaluate retrieval, synthesis and budget separately
- Tools: TwelveLabs Marengo (multimodal embeddings for spatial-temporal spans), TwelveLabs Pegasus (video-aware language model used as the reasoning layer), Jockey (TwelveLabs video agent product used for the demos)

## [The New Primitives: Building AI Native Software — Kwindla Kramer, Daily](../videos/LZuWZRze3MU.md)
`LZuWZRze3MU` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: product-ux, multi-agent, agent-architecture

Kwindla Kramer (Daily, PipeCat) argues agents are a stage on the way to AI-native software, using 80 years of computing history and demos of a real-time Knowledge Navigator and a multiplayer LLM game.

- Techniques: Asynchronous non-blocking context compression for sub-agents; Long-running sub-agents that share context; Progressive skills loading; Dynamic UI generation driven by the agent; Real-time voice plus LLM orchestration with a pipeline framework
- Tools: PipeCat, Gradient Bang, Daily, Tavus

## [HTML Is All Agents Need — James Russo, HeyGen](../videos/Cz4v1WHVyZc.md)
`Cz4v1WHVyZc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: context-engineering, skills-self-improvement, product-ux

HeyGen's Hyperframes turns agent-written HTML into deterministic MP4 video by freezing the browser clock and seeking frame by frame; the thinnest HTML wrapper beat heavier DSLs.

- Techniques: Thin HTML as the agent output format; Deterministic frame-by-frame browser rendering; Single render path for preview and output; Taste-focused skills instead of syntax skills; Small model as a format canary; Storyboard, iterate, then human last-mile edit; Website-to-asset single-shot skill
- Tools: Hyperframes, HTML/CSS/JS, Three.js, WebGL, WebGPU, Lottie, Rive, Remotion (transcribed as "Promotion"), After Effects, Premiere Pro, Gemini 3 Flash, Claude Code

## [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans — Corey Gallon, Rexmore](../videos/26RtyAm9y_Q.md)
`26RtyAm9y_Q` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: mcp-and-tools, agent-architecture, security-guardrails

Corey Gallon on driving websites with agents via a shell CLI over the Chrome DevTools Protocol, climbing from synthetic clicks to trusted input to human-like motion, and beating Cloudflare Turnstile, MT Capture, Lemin and reCAPTCHA v2.

- Techniques: CLI over MCP for repeatable browser tasks; Cross-channel verification after each action; Lowest-rung escalation; Coordinate-based trusted click through closed shadow roots and cross-origin iframes; Solver plus operator split; Explore, then codify
- Tools: Chrome DevTools Protocol (CDP), Chrome Agent (speaker's Python CLI), Cloudflare Turnstile, MT Capture, Lemin (auto-captioned as 'lemon'), reCAPTCHA v2, Outlook web client

## [Designing Voice Agents for Real Conversations - Chintan Agrawal & Daniel Wirjo, AWS](../videos/hMlLw1LeIK8.md)
`hMlLw1LeIK8` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: infra-cost-scaling

AWS solutions architects walk through turn-taking in voice agents: three levels from Silero VAD silence timers to Smart Turn, plus latency budgets and production issues. Includes live Pipecat demos.

- Techniques: Hybrid VAD + learned end-of-turn model with timer fallback; Interruption classification at barge-in; Per-stage latency budget with P50 and P95 tracking; Co-location to remove network hops; Session pruning or reset for long voice sessions; Config-only swap between turn-detection strategies for A/B tests
- Tools: Pipecat, Silero VAD, Smart Turn v3, Cartesia (STT and Sonic TTS), Deepgram Nova 3, Claude Haiku, GPT-4.1, Nemotron 3 Ultra

## [Your Voice Agent Doesn't Need a Frontier Model - Joel Allou & Ornella Bahidika, Microsoft](../videos/fnLBmfsI_Fg.md)
`fnLBmfsI_Fg` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: agent-architecture, infra-cost-scaling

Microsoft's ACE live voice tutor uses a small model (Haiku 4.5) for speech only, moving reasoning, lesson state and planning into a code state machine to hit about 900ms response time.

- Techniques: Externalised state machine for a small speaking model; Per-turn summary handoff; Strict rules to keep small models on track; Model selection by latency budget
- Tools: Claude Opus 4.7, Claude Haiku 4.5

## [Perception Agents — Antje Barth, Amazon AGI Lab](../videos/2JX6JYyQG4Y.md)
`2JX6JYyQG4Y` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: testing-verification, coding-agents

Amazon AGI Lab's Antje Barth argues computer-use agents need shared screen context and self-verification, then demos open-source annotation and design-spec checking tools for UI work.

- Techniques: Element pointing as agent input; Design-rules verification from a spec file; Meeting transcript to agent to verification pipeline; Perceive, plan, act, then re-check the screen
- Tools: Chrome extension (annotation tool), design rules markdown file (design.md), wearable transcription device, Amazon AGI Lab open-source perception agent harness (GitHub)

## [Evaling Video Slop — Maor Bril, Character.ai](../videos/b_PmGocP4rc.md)
`b_PmGocP4rc` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, testing-verification, agent-architecture

Maor Bril (Character.ai) on evaluating AI video: frame-level metrics miss story, physics and pacing, so he distilled a judge committee into a small fast VLM trained on pairwise comparisons and run inside the generation loop.

- Techniques: Pairwise A-vs-B judge training; Manufactured negatives; Matched-encoding real-vs-AI pairing with identical annotation; Expert-committee distillation into a small VLM; Eval inside the generation loop; Calibration sessions with randomized annotation; Agent with validation tools
- Tools: Qwen (small VLM, post-trained), Dolby Atmos (audio quality), CLIP-style frame metrics, frame-drift metrics, Kling, Seedance, Veo, Sora, OpenTelemetry (requested, planned for harness)

## [Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](../videos/CTLa_p6iOiY.md)
`CTLa_p6iOiY` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, testing-verification

Pierluca D'Oro (Programma Labs) shows that static computer-use benchmarks can be gamed by replaying recorded successful traces, and argues for varied environments plus hierarchical confidence intervals.

- Techniques: Replay-agent baseline check; PRISM environment design checklist; Template plus verifier config compiler; Hierarchical confidence intervals; Interval-gated model decisions

## [5 Open Source AI Tools That Feel ILLEGAL To Know About](../videos/-UxcljWN49I.md)
`-UxcljWN49I` · Kai Explains · 2026-08-02 · q2 · intro · review · also: agent-architecture, memory, coding-agents

Roundup of five open-source agent building blocks (Browser Use, Firecrawl, Mem0, OpenHands, Dify) mapped to read, act, remember, code and orchestrate roles. Mostly star counts and vendor stats, with no hands-on steps.

- Techniques: Read-decide-act browser agent loop; Scrape-to-markdown before retrieval; Two-phase memory: extract on write, retrieve on read; Sandboxed plan-write-test-iterate coding loop; Per-step tracing and worker queues for visual workflows
- Tools: Firecrawl (transcribed 'fire crawl'), Browser Use, Mem0 (transcribed 'Memzero'), OpenHands (transcribed 'open hands'), Dify (transcribed 'DeFi'), Devin (transcribed 'Devon'; Cognition AI, mentioned as a $500/month closed product), WebVoyager (benchmark, 586 tasks), SWE-bench (benchmark), Langflow (mentioned as Dify's origin comparison), OpenTelemetry (Dify export)

## [Gemini 3.6 Flash, 3.5 Flash-Lite, & 3.5 Flash Cyber, Fugu Cyber, Qwen Audio, Audex & More AI News](../videos/pJcCPsa5IbY.md)
`pJcCPsa5IbY` · Kai Explains · 2026-08-02 · q3 · intro · news · also: models-research, local-ai, security-guardrails

Weekly AI news (Aug 2026): Gemini 3.6 Flash and 3.5 Flash-Lite, Poolside's open 118B Laguna S2.1 with published trajectories, Microsoft's 4B MageFlow, plus audio, cyber and humanoid launches. Mostly vendor claims; Poolside's transparency stands out.

- Techniques: Wrap a frozen policy in a planner with memory (Harness VLA); Publish every trial's trajectory for benchmark claims (Poolside); Thinking on/off ablation on the same benchmark; Agent optimizes its own harness in an automated research loop; Fit check before running an image model locally
- Tools: Gemini 3.6 Flash, Gemini 3.5 Flash-Lite, Gemini 3.5 Flash Cyber, Gemini 3.5 Pro (partner testing), Gemini 4 (pre-training), Google AI Studio, Gemini API, Gemini app, Laguna S2.1 (Poolside, 118B total / 8B active MoE), Hugging Face, OpenMDW 1.1 license, GGUF

## [Grok 4.5 beats Claude and GPT, Seedream 5.0, Reve 2.1,Muse image and Video by Meta | AI News](../videos/FUCNOKb33qs.md)
`FUCNOKb33qs` · Kai Explains · 2026-08-02 · q3 · intro · news · also: models-research, token-cost-efficiency, local-ai

Weekly AI news roundup (Aug 2026) covering Meta Muse Image, Grok 4.5, LingBot VLA 2.0, NVIDIA AudX 2B, MOSS Transcribe Diarize, WanStreamer 0.2, Seedream 5.0 Pro, Reve 2.1 and Alaya World, mostly with vendor-reported numbers.

- Techniques: Dual-memory consistency for interactive world models; Thinker/performer pipeline split for latency-neutral resolution upgrades; Layout-first image generation for targeted edits; Single-pass joint ASR and diarization; Unified multi-task audio model that preserves text ability; Test-time compute scaling with tool calls and self-refinement
- Tools: Muse Image, Muse Video, Meta AI, Instagram, WhatsApp, Grok 4.5, Grok Build, Cursor, XAI API, Opus 4.8, Fable Max (as transcribed), GPT 5.5 (as transcribed 'Xi')

## [This component library is mind-blowing (Canvas UI)](../videos/JZf_m_BVDaQ.md)
`JZf_m_BVDaQ` · Better Stack · 2026-08-02 · q3 · intro · review · also: vibe-coding-app-building, dev-tools

Better Stack walkthrough of Canvas UI, an open-source, shadcn-installable library of 33 WebGL and HTML-in-Canvas effects, plus using those effects on code-generated video through HyperFrames.

- Techniques: Install a Canvas UI component with the shadcn CLI; Progressive enhancement for HTML-in-Canvas effects; Test HTML-in-Canvas in Chrome with the feature flag; Apply shader-style effects to generated video with an agent; Match effects to the UX intent
- Tools: Canvas UI, shadcn (CLI), Three.js, HTML-in-Canvas (WICG proposal, browser API), drawElementImage, TextElementImage2D (WebGL), CopyElementImageToTexture (WebGPU), Chrome (feature flag), Firefox, Claude, HyperFrames, Remotion

## [Inkling: This Open-Weight Model Wants To Be Fine Tuned](../videos/YAcIUCjsRnU.md)
`YAcIUCjsRnU` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: models-research, training-finetuning-rl

Better Stack walks through Thinking Machines' open-weight "Inkling" model: a MoE that takes raw audio and image patches, positioned as a base for fine-tuning on Tinker rather than a general frontier model.

- Techniques: Decide fine-tune vs retrieval by failure type; Distill a narrow task from a general model into a small fine-tuned model; Let the model generate its own fine-tuning dataset via Tinker; Feed raw audio directly to the model for tasks needing prosody or delivery; Tune reasoning depth with the thinking-effort slider
- Tools: Inkling (Thinking Machines open-weight MoE model), Tinker (fine-tuning platform), LoRA, Hugging Face, GLM 5.2, GPT-OSS, GPT-4.0, Kimi K3, Qwen, DeepSeek, NVIDIA Nemotron

## [Bonsai runs on iPhone, Claude Browser ,Muse Spark, ARDY by Nvidia, 1X Robot Hand & More AI News](../videos/4TlbzLB3IgE.md)
`4TlbzLB3IgE` · Kai Explains · 2026-08-02 · q3 · intro · news · also: models-research, local-ai, claude-code

Weekly roundup (Aug 2026): Meta Muse Spark 1.1, a built-in browser in Claude Code, Bonsai 27B running in 1-bit on a phone, several open vision and edge models, NVIDIA's ARTI motion model, and 1X NEO's tendon-driven hands.

- Techniques: Open the Claude Code built-in browser; Expect a domain prompt and per-write classifier on external browsing; Run Bonsai 27B locally on Apple or NVIDIA hardware; Interleaved token stream plus silence token for live video; Output format as the task selector for a unified vision model; Mid-generation constraints with a look-ahead window for motion
- Tools: Muse Spark 1.1 (Meta Superintelligence Labs), Meta Model API (public preview), Meta AI app (thinking mode on meta.ai), Claude Code (desktop Code tab built-in browser), Claude Desktop, Bonsai 27B (PrismML), MLX, CUDA, Hugging Face, GitHub, MoSVL Realtime (name as captioned; 11B), X-RopeE positional encoding (as captioned)

## [Browser Use + Claude Code Is INSANE (Free + Open Source + Real Browser)](../videos/OprnDByYVLQ.md)
`OprnDByYVLQ` · Kai Explains · 2026-08-02 · q3 · intro · review · also: security-guardrails, token-cost-efficiency

Browser Use plus Claude Code: the browser part is old, the new part is a model choosing actions from a numbered text menu of page elements. The menu makes it useful, and the same open page makes prompt injection a real risk when the browser is logged in.

- Techniques: Numbered interactive-element menu for browser agents; Untrusted-page threat model for browser agents; Staged rollout for browser agents: read-only first; Human gate on destructive browser actions and a step cap
- Tools: Browser Use, Claude Code, Claude, Anthropic computer use, Selenium, Playwright, Puppeteer, Google Flights, Cloudflare (bot check)

## [I Haven't Typed in a Week (Thanks to This App)](../videos/ZRsDQp9CrXc.md)
`ZRsDQp9CrXc` · Better Stack · 2026-08-02 · q3 · intro · review · also: local-ai, dev-tools

Better Stack host tours Handy, an open-source, MIT-licensed, fully offline dictation app with user-chosen models, and compares its output against Google Docs voice typing and Wispr Flow on one passage.

- Techniques: Handy push-to-talk or toggle dictation setup; Choosing a model by speed/accuracy trade-off; Adding a custom fine-tuned Whisper model; Side-by-side dictation accuracy check
- Tools: Handy (open-source offline dictation app, MIT, built by CJ Pace), Tauri (transcribed as "talk"; the Rust-plus-web-UI shell is implied by the description), React, TypeScript, Transcribe CPP (runtime for Whisper-family GGML/GGUF models), transcribe-rs (runs Parakeet), Parakeet Unified 0.6B (CPU-only speech model), Whisper (GGML models, including custom fine-tunes), Silero VAD (transcribed as "Cilero VAD"), cpal (cross-platform audio input), rdev (global keyboard shortcuts), rubato (real-time resampling)

## [Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua](../videos/ZSQb5fzRFPw.md)
`ZSQb5fzRFPw` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: sandboxing-execution, evals, infra-cost-scaling

Cua's team presents "Computer-Use 2.0": a background computer-use driver (Cua Driver), a multi-platform benchmark (CuaBench, including a KiCad electrical-engineering set), and warm sandbox pools (CuaFleet) that cut idle GPU time in RL training.

- Techniques: Two-tier background action with fallback; Window-scoped observation; Single-file cross-platform task definition; Adversarial pre-validation of evals; Trajectory forking for world-model probes; Demand-autoscaled warm pool for sandboxes
- Tools: Cua Driver, CuaBench, CuaFleet, Codex computer-use model, TerminalBench, Harbor, Android activity framework, Hermes harness, KiCad

## [The Prompt Is Still a Punch Card - Ted Johnson, JoinIn AI](../videos/hVJOnuhFmTA.md)
`hVJOnuhFmTA` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: product-ux, context-engineering

Ted Johnson (JoinIn AI) argues that prompting is a batch-style punch-card protocol that leaves users doing the work, and that AI interfaces should become turn-taking, conversation-like, and aware of who is being addressed.

- Techniques: Classify each utterance, then act only at a floor-free moment; Full-duplex turn-taking with yield and resume; Ask what burden the human still carries; Voice-driven record edits in a meeting
- Tools: NVIDIA Personaplex, OpenAI GPT Realtime 2

## [Voice In, Visuals Out: The Agony and the Ecstasy - Allen Pike, Forestwalk Labs](../videos/65X0pQ6Lmbg.md)
`65X0pQ6Lmbg` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: infra-cost-scaling, product-ux

Allen Pike (Forestwalk Labs) on why voice input with visual output beats voice-to-voice for AI now, and the latency tactics (fast small model, eager short inference turns, stable prompt prefixes) that make it feel responsive.

- Techniques: Two-tier model split (fast responder plus async thinker); Eager short-interval inference; Prefix-stable context layout for caching; Visual response envelope
- Tools: Linear, Slack, GPT-5 Mini, Haiku

## [Browser Agents Don't Need Better Models. They Need Better Eyes. - Kushan Raj, Sarvam AI](../videos/JnubYCYunk8.md)
`JnubYCYunk8` · AI Engineer · 2026-07-18 · q2 · intro · demo · also: context-engineering, token-cost-efficiency

Kushan Raj (Sarvam AI) argues browser agents fail because of their infrastructure, not model quality, and shows a compact page representation plus change feedback that makes a cheap model faster and more reliable.

- Techniques: Compact page representation for agents; Delta feedback to the agent; Invest in the environment instead of the model; Expose a browser task as an API
- Tools: browser agent harness (speaker's own, to be open sourced), Claude (used as the baseline in demos)

## [Google's New AI Architecture Changes Everything (Gemma 4 12B)](../videos/WLtCHXdHTF0.md)
`WLtCHXdHTF0` · Better Stack · 2026-07-02 · q2 · practitioner · review · also: models-research, local-ai

Better Stack explains Google's encoder-free Gemma 4 12B, which replaces vision and speech encoders with linear projections, then runs an offline image test on a 24GB M2 Mac. The architecture detail is useful, but the claims are unbenchmarked.

- Techniques: Patch-and-project image input for an encoder-free multimodal LLM; Audio frames projected as tokens; Offline real-time image sanity check for a local model; Native multi-token prediction drafters
- Tools: Gemma 4 12B, Gemma 4 26B (sibling model, comparison only), OMLX (local inference framework for Apple Silicon), Google AI Edge Gallery (mobile app, buggy on image input in the host's test), M2 MacBook Pro (24GB, host's test machine)

## [Ideogram 4.0 image model, ByteDance Ditches Nvidia GPU, Google's 16GB Multimodal Beast AI News](../videos/12_TXXeI4uE.md)
`12_TXXeI4uE` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, local-ai, training-finetuning-rl

Roundup of late-June/early-July 2026 open-model releases: Ideogram 4.0 (open-weight, describe-to-structure training), Reve 2.0, Joy AI Echo long-video generation, Gemma 4 12B unified multimodal model, Magenta RealTime 2, ByteDance CUDA Agent, LFM 2.5 VL 450M, Molmo 2, MDA depth, Nemotron ASR, NVIDIA Artifixer.

- Techniques: Describe-to-structure-to-recreate training; Mixture-density depth output; Agentic kernel optimization loop; Unified decoder-only multimodal input without encoders
- Tools: Ideogram 4.0, Reve 2.0, Joy AI Echo, Gemma 4 (12B), Magenta RealTime 2 (MRT2), CUDA Agent, CUDA Agent Ops 6K, torch.compile, KernelBench, LFM 2.5 VL 450M, Molmo 2, MDA (Modeling Depth Ambiguity)

## [Microsoft MAI Models, Live AI Characters, 3D from One Image & More AI News](../videos/WVC03w3AG6k.md)
`WVC03w3AG6k` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, local-ai

Kai Explains weekly AI news: Microsoft's seven-model MAI family from Build 2026, StreamChar live audio-video characters, Pager 360-panorama geometry, and JetBrains' open Mellum 2 coding model.

- Techniques: Reproject non-native inputs into the distribution a model was trained on (Pager); Split a streaming avatar into an LLM planner and a joint audio-video diffusion generator (StreamChar); Try Mellum 2 Thinking as a low-active-parameter coding model
- Tools: MAI-Thinking-1 (captioned MyThinkingOne), MAI Image 2.5, MAI Transcribe 1.5, MAI Voice 2, MAI Voice 1, MAI Code 1 Flash, GitHub Copilot, VS Code, Azure AI Foundry, Arena text-to-image leaderboard, StreamChar, Pager

## [Midjourney full body scanner, VibeThinker, Qwen-Robots, Happy Oyster & More | AI News](../videos/aGseXhwqiLg.md)
`aGseXhwqiLg` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, agent-architecture, local-ai

Weekly AI news roundup (2026-07-02): a 3B reasoning model with contested benchmarks, Midjourney's ultrasonic full-body scanner, Qwen robot models, world models, TTS, a multi-agent deep research system, and a camera-control model.

- Techniques: Orchestrator, parallel sub-agents, and a global verifier; Progressive training for interactive world models; World memory via retrieval of prior generations; Camera grid as a control signal; Two decoders for trajectory prediction; Unified state-action space for cross-embodiment control; Inline control tokens in TTS input
- Tools: VibeThinker (Weibo AI, 3B reasoning model, MIT license), Midjourney Medical (ultrasonic CT body scanner, unreleased), Qwen Robot Nav, Qwen Robot Manip, Qwen Robot World (Alibaba; Nav built on Qwen3-VL), DreamX World (5B interactive world model), Higgs Audio V3 (Boson AI TTS, research license), Molmo Motion and PointMotionBench (Allen AI), Apodex One (deep research agent, up to 150 sub-agents), Happy Oyster (Alibaba hosted world engine; formerly Happy Horse 1.0), OmniDirector (Kling team camera-control model), Hugging Face (weights), GitHub (code), arXiv (papers)

## [Krea 2 image model, Sakana Fugu beats Fable 5, Seedance 2.5, Seed 2.1 & More AI News](../videos/q8NQD1IZnFk.md)
`q8NQD1IZnFk` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, multi-agent, skills-self-improvement

Weekly AI news roundup (July 2026): Seedance 2.5 preview, Sakana Fugu model routing, Ling/Ring 2.6 open trillion-parameter MoEs, Krea 2 open weights, NVIDIA BioNeMo skills. Nearly all numbers are vendor-reported.

- Techniques: Documented skill specs for domain tools (BioNeMo skills); Single-endpoint learned model assembly (Sakana Fugu); Sparse 3D box blocking for object motion (Loose Control Video); Bidirectional generation for seamless loops (Unitemp); Reasoning effort toggle per task (Ring 2.6); Pick the Krea 2 checkpoint by use (RAW vs Turbo)
- Tools: Seedance 2.5 (transcribed as CDance 2.5), Seedance 2.0, Veo 3.1, Kling 3.0, Sakana Fugu, Trinity (ICLR 2026), Conductor (ICLR 2026), Ling 2.6, Ring 2.6, ICEPOP (async RL method), Gemini 3.1 Pro, Claude Opus 4.7

## [Humanoid GPT, GitHub for Robotics, Sana Real-Time AI Video Editing and D4rt 4D Scene Model AI News](../videos/EenYAIfx2ME.md)
`EenYAIfx2ME` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, local-ai, evals

Weekly AI news roundup (2026-07-02) covering NVIDIA SANA streaming, Holo 3.1, Dots.TTS, D4RT, Tanker, MAMA, QJudger, VibeVoice and Humanoid GPT; nearly all claims are repeated from project pages, not tested.

- Techniques: Hybrid softmax/linear attention diffusion transformer for streaming video; Cycle reverse regularization for temporal consistency; Codebook-free autoregressive TTS with a flow-matching head; Ultra-low frame-rate continuous speech tokenizers for long-form dialogue; Multi-dimension structured LLM-as-judge with human-agreement validation; Contact-aware optimization for close multi-person pose; DAgger distillation from motion experts into a GPT-style controller; Compare quantized formats on your own hardware before choosing one
- Tools: SANA streaming, SANA video, SANA (NVIDIA), Holo 3.1, HoloTab harness, Android World benchmark, DGX Spark, NVIDIA RTX 5090, NVFP4, FP8, GGUF Q4, BF16

## [TEN Framework: Voice AI That Can Actually Be Interrupted](../videos/ES3HhoYCtIc.md)
`ES3HhoYCtIc` · Better Stack · 2026-07-02 · q3 · intro · review · also: agent-architecture

Better Stack hands-on test of TEN Framework, an open-source runtime for real-time voice agents built as graphs of extensions, focused on whether interruptions (barge-in) work.

- Techniques: Graph-of-extensions voice agent; Barge-in test for voice agents; Local TEN bring-up with Docker Compose; Graph-based debugging in TEN Manager
- Tools: TEN Framework (open-source real-time voice agent runtime, version not stated), TEN Manager (visual graph designer), Agora (real-time audio / RTC), Deepgram (speech recognition and TTS preset), OpenAI (LLM in the demo), ElevenLabs (TTS), XAI (alternative preset), Docker Compose, LiveKit Agents (alternative, named by presenter), Pipecat (alternative, named by presenter), Python, C++, Go, Rust, TypeScript (extension languages), SIP telephony, ESP32 hardware, speaker diarization (example configs named)

## [Claude Fable 5, Grok imagine 1.5, Gemini Live Translate, HumanEgo Robot, Mirage World Model AI News](../videos/ibGW_YqQmLg.md)
`ibGW_YqQmLg` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, inference-serving, training-finetuning-rl

Kai Explains weekly AI news roundup (2026-07-02): Claude Fable 5 and Mythos 5, Grok Imagine 1.5, N2 Pro, Quasar, LeVar, vLLM-Omni, HumanEgo, SCAIL 2, Gemini 3.5 Live Translate, Mirage. Mostly vendor and paper claims relayed without testing.

- Techniques: Adaptive thinking gate; Sensitive-category model routing; Persistent file-based memory for long agent runs; Latent-space scene memory (Mirage); Interaction-centric tokens for cross-embodiment policies (HumanEgo); Skeleton-free motion transfer (SCAIL 2); Geometry from a 4D reconstruction model as a video-diffusion condition (LeVar)
- Tools: Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, Claude Opus 4.7, Claude Mythos Preview, Project Glasswing, Grok Imagine 1.5, xAI API, N2 Pro (SII), N2 Mini, Qwen 3.5, OpenRouter

## [OpenAI GPT 5.6 launch, Realtime Video avatar, HappyHorse 1.1, Nvidia & More AI News](../videos/odlkEMloedA.md)
`odlkEMloedA` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, local-ai, training-finetuning-rl

Weekly AI news roundup: GPT-5.6 Sol/Terra/Luna and its gated release, Happy Horse 1.1 video, Ornith 1.0 open coding models, WanStreamer, NVIDIA's video inference engine, Fine VLA and SURF. Mostly vendor-reported claims.

- Techniques: Self-scaffolding RL training (Ornith 1.0); Tiered model family routing; Automatic per-model acceleration stack selection; Single-transformer streaming for conversational avatars; Fine-grained instruction relabeling for robot data
- Tools: GPT-5.6 (Sol, Terra, Luna), OpenAI Preparedness Framework, Terminal Bench 2.1, GeneBench V1, ExploitBench, ExploitGym, Happy Horse 1.1, Happy Horse 1.0, Arena AI Video Arena, Ornith 1.0 (9B dense, 31B dense, 35B MoE, 397B MoE), Claude Opus 4.7, MiniMax M3

## [I Tried the Open Source ElevenLabs Alternative (Voicebox)](../videos/RL_PDX_BVxw.md)
`RL_PDX_BVxw` · Better Stack · 2026-07-02 · q3 · intro · review · also: local-ai, mcp-and-tools

Better Stack walkthrough of Voicebox, a free open-source local voice studio for cloning, TTS, system-wide dictation and agent speech. Works well on Apple Silicon, but the tool is early and the agent integration was not tested.

- Techniques: Desktop install instead of Docker; Clone a voice from a short sample; System-wide dictation via global hotkey; Restart to clear app-level glitches; Pick the model for emotion control
- Tools: Voicebox, ElevenLabs, Ollama, Docker, Piper, Whisper, Claude Code, Cursor, Chatterbox TTS Turbo, MCP

## [Real-time Voice cloning, Kimi K2.7 CODE, GLM 5.2 and 3D reconstruction | AI News](../videos/DX4kW1vdTXc.md)
`DX4kW1vdTXc` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, local-ai, coding-agents

Weekly open-model news roundup (2026-07-02): Zonos 2 voice cloning, MiniMax M3, Kimi K2.7 Code, GLM 5.2, NVIDIA Motion Bricks, Microsoft Fara-7B, plus robotics and 3D items. Mostly vendor-reported claims.

- Techniques: Shared fixed-size latent for variable-view 3D reconstruction (Surflow); Reusable motion primitives with zero-shot composition (Motion Bricks); Report steps and cost per task next to success rate for computer-use agents (Fara-7B); Canonical body topology as a pivot between body models (SOMA); Haptic torque feedback in teleoperation for robot data collection (UME); Where to get each release (as stated in the video)
- Tools: Zonos 2, Zyphra Cloud, MiniMax M3, MSA (Minimax Sparse Attention), Minimax Code, Kimi K2.7 Code, Kimi K2.6, KimiCode, Kimi Code Bench V2, Program Bench, MLS Bench Lite, MCP Atlas

## [Genesis Eno, Unitree H2 Plus, Atlas In Factory, Figure AI 1 Robot/Hour, Humanoid-GPT & More AI News](../videos/laFa8sZ5CFU.md)
`laFa8sZ5CFU` · Kai Explains · 2026-07-02 · q2 · intro · news · also: models-research, enterprise-adoption

Weekly robotics news roundup from Kai Explains: Genesis AI's Eno robot, Unitree H2 Plus, XPeng, Figure's production scale-up, Boston Dynamics Atlas at Hyundai, and HumanoidGPT and Deep Robotics DR02 demos.

- Techniques: Multi-expert RL distillation into one motion-tracking policy (HumanoidGPT); Lightweight fine-tuning for out-of-distribution motions; VR teleoperation demonstrations as training data (Atlas); Fleet telemetry feeding model training (Figure Helix); End-of-line functional test gating with burn-in (Figure BotQ); Visible intent display for robots working near people (Eno cognitive interface)
- Tools: Genesis AI Eno, Gene (Genesis AI model), Unitree H2 Plus, NVIDIA Jetson Thor, NVIDIA Blackwell GPU, Sharpa Wave tactile hands, NVIDIA Isaac GR00T (transcribed 'Isaac Groot'), NVIDIA Isaac Sim, NVIDIA Isaac Lab, NVIDIA Isaac ROS (transcribed 'Isaac Ross'), XPeng iron humanoid, Figure 03

## [Introducing WebMCP: Agents in the Browser — RL Nabors](../videos/LMbeDEQO6QM.md)
`LMbeDEQO6QM` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: mcp-and-tools, product-ux

A practical tour of MCP over HTTP, MCP Apps for in-chat UI with CSP and sandbox gotchas, and WebMCP, which lets agents call tools exposed by a web page's own JavaScript.

- Techniques: Single server, multiple client surfaces; Remote connector onboarding over HTTP; App-only tool visibility for UI navigation; Bundle MCP App into one file with explicit CSP; WebMCP imperative registration with feature detection; Declarative WebMCP on existing forms
- Tools: MCP, MCP Apps, WebMCP, navigator.modelContext.registerTool, Vite single-file plugin, Web Speech API, MCP Inspector-style debugging extension

## [Reachy Mini: the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face](../videos/0jeZfjJMfmo.md)
`0jeZfjJMfmo` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: inference-serving, infra-cost-scaling

Hugging Face's Andres Marafioti on the open-source $300-450 Reachy Mini robot, its voice pipeline, and how a streaming TTS model was made fast enough for real-time voice agents.

- Techniques: Stream TTS audio instead of generating full utterances; Static KV cache plus graph capture for autoregressive audio models; Partial STT every 150 ms; Separate scaling of LLM inference from stateful conversation nodes; Measure the whole latency path, not just the model; Codex-driven hardware app development
- Tools: Reachy Mini, Raspberry Pi, Codex, Parakeet, Qwen3-TTS, Qwen 3.5 27B, Kokoro, Voxtral, Hugging Face Inference Endpoints, speech-to-speech pipeline, GPT Realtime

## [The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google](../videos/ghJmWQCIHRM.md)
`ghJmWQCIHRM` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: mcp-and-tools, product-ux

Google Chrome DevRel on WebMCP, a proposed browser standard that lets a website expose its actions as structured tools for in-browser AI agents, with declarative and imperative APIs and an early-preview setup guide.

- Techniques: Declarative tool exposure from HTML forms; Imperative registerTool for multi-step UI; Mirror tool calls in the visible UI; Hybrid browse-then-delegate flow; Test tools with an inspector and evals CLI
- Tools: WebMCP, Chrome Canary, Model Context Tool Inspector (Chrome extension), Gemini, Chrome DevTools-style flag (WebMCP testing flag), WebMCP evals CLI

## [Beyond Transcription: Building Voice AI That Understands Conversations — Hervé Bredin, pyannoteAI](../videos/mFLlVpnGpds.md)
`mFLlVpnGpds` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: evals, data-engineering

Pyannote's Hervé Bredin explains why speaker diarization is still unsolved and why merging it with STT word timestamps is hard, with a live DER demo.

- Techniques: DER error breakdown; Benchmark in your own acoustic condition; Exclusive diarization in overlaps; Timestamp-based word-to-speaker alignment; Model-agnostic reconciliation layer
- Tools: pyannote (open-source diarization toolkit), pyannote metrics (DER evaluation), OpenAI Whisper, NVIDIA Parakeet, Hugging Face model hub, pyannoteAI cloud API

## [Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind](../videos/BcWFc3H7Khg.md)
`BcWFc3H7Khg` · AI Engineer · 2026-06-18 · q3 · practitioner · workshop · also: models-research, context-engineering

Live workshop from Google DeepMind's Guillaume Vernade building an illustrated children's book with Gemini, Nano Banana, Veo, Lyria and TTS, plus API tips on retries, service tiers and stateful chats.

- Techniques: Retry wrapper around the media client; Service tier choice per request; Iterate cheap, then upscale; Structured output as a scene manifest; Style and composition system instructions; Streamed Lyria output; Lyria RealTime as a live, steerable stream
- Tools: Gemini API, Vertex AI, Google AI Studio, Google GenAI SDK, Google Colab, Nano Banana 2, Veo 3.1 and Veo 3.1 Lite, Lyria 3 clip and full-song models, Lyria RealTime, Gemini TTS, Interactions API, Gutenberg (source book)

## [Prompt to Pipeline: Building with Google's Gen Media Stack — Paige & Guillaume, Google DeepMind](../videos/ns9f1fjLD7Y.md)
`ns9f1fjLD7Y` · AI Engineer · 2026-06-18 · q3 · practitioner · workshop · also: models-research, vibe-coding-app-building, coding-agents

Google DeepMind's Paige and Guillaume, with Gemma's Ian Ballantyne, demo AI Studio, Gen Media models and local Gemma 4 agents. Mostly a live product tour, with some practical prompting and cost tips.

- Techniques: Playground-to-code export; Code execution for verified counting and drawing; Per-scene reference injection for character consistency; Structured outputs as a prompt-writing stage; Prompt-level multi-voice TTS; Flex and priority service tiers; Local orchestrator with parallel subagents on an OpenAI-compatible server; Vibe-coding guardrails: one file per feature, plus logging
- Tools: Google AI Studio, Gemini API, Gemini Live, Google Build (AI Studio), Firestore, Google Search grounding, Antigravity, Nano Banana 2, Veo 3.1 Lite, Lyria 3, Lyria RealTime, Genie 3 / Project Genie

## [From Transcription to Live Music: Gemini's Audio Stack — Thor Schaeff, Google DeepMind](../videos/Bc6Ojl2XS1w.md)
`Bc6Ojl2XS1w` · AI Engineer · 2026-06-18 · q2 · intro · demo · also: data-engineering, models-research

Google DeepMind's Thor Schaeff tours Gemini's audio stack: one-call structured audio extraction, director's-note TTS, a native speech-to-speech Live model, and a live tool call to Lyria music generation.

- Techniques: Single-call structured audio extraction; Director's-note TTS prompting; Realtime model with a generation tool; System-instruction persona on a live audio model; Install vendor API skills into coding agents
- Tools: Gemini API, Google AI Studio, Gemini 3 Flash Preview, Gemini 3.1 Flash Live, Gemini Live API (WebSocket), Lyria 3 / Lyria 3 Pro, Gemma 4, Veo 3.1 Lite, Gemini coding-agent skills

## [Engineering voice agents: Latency, quality, and scale — Rishabh Bhargava, Together AI](../videos/N7b1PJc7SFc.md)
`N7b1PJc7SFc` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: infra-cost-scaling, evals, agent-architecture

Together AI's voice AI lead on the cascading STT→LLM→TTS pipeline: per-stage latency budgets, streaming STT, co-locating models to cut network hops, and why speech-to-speech is not yet production-ready.

- Techniques: Cascading voice pipeline with streamed hand-offs; Per-stage latency budget; Streaming STT with lookahead-limited encoders; Co-locate models with the orchestrator; Asymmetric autoscaling for stateful voice; Pre- and post-LLM guardrail and routing stages; Thinker-talker delegation; Tiered tool-call evals; Full-duplex conversation evals
- Tools: Together AI (hosted inference, the speaker's company), Pipecat (agent orchestrator, named as an example), LiveKit (agent orchestrator, named as an example), Whisper (OpenAI speech-to-text, cited as the batch model), NVIDIA streaming speech encoder (named only as a recent NVIDIA model), NVIDIA VoiceChat (speech-to-speech model), OpenAI realtime API (speech-to-speech), ChatGPT advanced voice mode, Claude Code and Cursor (cited as voice-interaction examples)

## [Any-to-Any: Building Native Multimodal Agents - Patrick Löber, Google DeepMind](../videos/GIRpQEfYf3U.md)
`GIRpQEfYf3U` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: agent-architecture, mcp-and-tools

Google DeepMind's Patrick Löber walks through building a NotebookLM-style agent: Gemini reasons, calls native image and speech generators via function calling, and uses multimodal input and a live audio model.

- Techniques: Agentic generation loop with function-declared generators; Single-call multimodal synthesis; Timestamp-windowed media analysis; Context caching for repeated queries; Scaffold with a Gemini API skill; Audio-to-audio live session for voice
- Tools: Google Gen AI SDK, Gemini API, Google AI Studio, Gemini 3 Flash, Gemini 3.5 Flash Image preview (Nano Banana 2), Gemini 2.5 text-to-speech, Gemini 3.1 Flash Live, File API, Gemma 4, Gemini API skill

## [You Might Not Need 50 Diffusion Steps — Ziv Ilan, Nvidia](../videos/gHs5ZiY80PM.md)
`gHs5ZiY80PM` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: inference-serving, training-finetuning-rl

NVIDIA's Ziv Ilan on making diffusion image and video models fast enough for real use: quantization, step caching and step distillation, stacked incrementally, with distillation as the biggest win.

- Techniques: Post-training quantization with dynamic ranges for diffusion; Step caching (TeaCache-style and chunk-based); Trajectory vs distribution step distillation; Incremental optimization ladder
- Tools: TensorRT-LLM Visual Gen, FastGen, vLLM-Omni, SGLang Diffusion, TeaCache, Blackwell GPUs (B200), Hugging Face checkpoints

## [How to talk to statues — Joe Reeve, ElevenLabs](../videos/u-rJwPPU3QA.md)
`u-rJwPPU3QA` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: product-ux, vibe-coding-app-building

ElevenLabs growth lead on the viral "Statue" app, built in two hours, and on voice-agent UX. Main points: glue code and storytelling matter most, and voice agents need visual co-presence and interruptible, editable transcripts.

- Techniques: Research-to-persona-to-agent chain; Thin glue layer on managed APIs; Playback-position transcript truncation for barge-in; Visual side panel for voice conversations; Hook-first short video with late music
- Tools: ElevenLabs Agents, ElevenLabs Voice Design API, ElevenLabs music generation, OpenAI deep research, Cursor, Supabase, Facebook Instant Games API (deprecated), CapCut, Claude app voice UI, OpenClaw

## [From MCP to Scale: Pipelines That Build Themselves — Rafael Levi, Bright Data](../videos/zTZ0qunQXnM.md)
`zTZ0qunQXnM` · AI Engineer · 2026-06-18 · q2 · practitioner · demo · also: data-engineering, coding-agents, mcp-and-tools

A Bright Data vendor demo arguing LLMs should write a reusable scraper once instead of parsing every page, then run and self-repair it on a schedule. Useful pattern, heavy product pitch.

- Techniques: Generate-then-run scraper; Scheduled self-repairing collection loop; Tiered fetch format; Remote browser with human-like input for multi-step flows; Public-data-only policy check
- Tools: Claude Code, Codex, Bright Data MCP, Bright Data scrape-as-markdown, Bright Data Web Unlocker API, Bright Data remote browsers, Bright Data skill docs on GitHub, Haiku

## [AI avatar beats HeyGen, 1-min 720p video, video timestamps AI, lip sync model: AI NEWS](../videos/MYzITZG4c4M.md)
`MYzITZG4c4M` · Kai Explains · 2026-06-02 · q3 · intro · news · also: models-research, local-ai, inference-serving

Kai Explains weekly AI news (June 2, 2026): a roundup of new open-weight releases across robotics sim, small translation and video models, avatars, humanoids, TTS and segmentation.

- Techniques: Simulation as an evaluation signal; Prompt-level control of a small translation model; Ternary (1.58-bit) weights for memory savings; Rolling multi-segment inference for identity-stable long video; Few-step distillation (DMD) for video diffusion
- Tools: Genesis World 1.0, Nix (renderer), Quadrants (Python-to-GPU compiler), IsaacSim, MuJoCo, HiMT2 (Tencent translation models, captioned as 'HiMT2'), BitCPM-CANN, MiniCPM4, Huawei Ascend 910B / NPU, Marlin 2B, LongCat Video Avatar 1.5, Whisper Large V3

## [Developers Finally Got an Open-Source Voice AI Platform (Dograh)](../videos/xD9JEvfCH9k.md)
`xD9JEvfCH9k` · Better Stack · 2026-06-02 · q3 · intro · review · also: observability, infra-cost-scaling

Short hands-on look at Dograh, a self-hostable open-source voice agent platform with a visual workflow builder, per-call traces and recordings, as an alternative to hosted tools like Vapi.

- Techniques: Local spin-up of a self-hosted voice agent stack; Lead-qualification voice flow as a node graph; Per-call debugging via transcript, trace and recording; Swap providers at the runtime layer
- Tools: Dograh, Docker Compose, Git, Vapi, Bland, Retell, Pipecat, Vocode, LiveKit

## [Developers Might Finally Have a Local TTS Model That Doesn’t Suck](../videos/pbsTTxKTuts.md)
`pbsTTxKTuts` · Better Stack · 2026-06-02 · q3 · intro · review · also: local-ai

Hands-on test of Supertonic 3, a 99M-parameter local TTS model: fast and easy to deploy, but it mangles prices, dates and expression tags, so test your own app text first.

- Techniques: Stress-test TTS with production-shaped strings; Side-by-side demo harness for a TTS model; Point an OpenAI-style speech client at a local server
- Tools: Supertonic / Supertonic 3 (Supertone, on-device TTS, 99M parameters, 31 languages), supertonic (pip package: Python SDK, CLI, local HTTP server), ONNX Runtime (CPU inference), Python, OpenAI audio speech API (compatible local endpoint; cloud comparison), ElevenLabs ("11 Labs" in the transcript; cloud comparison), Java, C++, C# and browser example clients

## [Why MLX — Prince Canuma, Neywa Labs](../videos/zTLJNHj0DeQ.md)
`zTLJNHj0DeQ` · AI Engineer · 2026-05-18 · q3 · intro · talk · also: local-ai, inference-serving

Prince Canuma argues for running agents, voice, and vision models fully on Apple Silicon with MLX to cut cloud subscription costs and work offline. Demos are mixed, and the talk ends with a TurboQuant KV-cache claim.

- Techniques: Modular speech pipeline; Chained short-clip video generation; Grounded visual reasoning on video; Storage-backed model loading on phones; TurboQuant-style KV-cache quantization; Live GPU monitoring during inference
- Tools: MLX, MLX-VLM, MLX-Audio, Marvis TTS, RF-DETR, Gemma 4, Qwen3-Omni, Core ML, Gradio, MacTop, Reachy Mini, LM Studio

## [Voice AI: when is the "Her" moment? — Neil Zeghidour, CEO, Gradium AI](../videos/P_RI1kCkRbo.md)
`P_RI1kCkRbo` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: infra-cost-scaling, models-research

Gradium's CEO argues voice AI is not yet at the "Her" moment: cascaded pipelines hit latency limits, full-duplex speech models lack reliability and tools, and TTS cost dominates. He pitches on-device TTS as the fix.

- Techniques: Filler speech while a tool call runs; Stress-test full-duplex and interruption behaviour; On-device TTS for cost and privacy; Keep the cascade as the default for reliable agents
- Tools: Moshi, Gradium Phonon, NVIDIA PersonaPlex, Kokoro, ElevenLabs, OpenRouter

## [Why TTS Models Now Look Like LLMs — Samuel Humeau, Mistral](../videos/3jGAU2sbAyY.md)
`3jGAU2sbAyY` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: models-research, inference-serving

Mistral's Samuel Humeau explains why modern text-to-speech uses autoregressive audio-token LLM-style backbones, frame-level codecs and streamed output for voice agents.

- Techniques: Stream the first audio chunks; Two-level frame decoding; Codec with a bottleneck and text-aware token losses; Flow-matching token head per frame; Full-context conditioning with a short voice prompt; Fast small LLM for the text, TTS for the audio

## [FLUX, Open Research, and the Future of Visual AI — Stephen Batifol, Black Forest Labs](../videos/x8Yb4RidLgM.md)
`x8Yb4RidLgM` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: models-research, inference-serving

Black Forest Labs' developer relations engineer walks through FLUX model history, a new self-supervised training method (Self-Flow) that drops external encoders, and sub-second Klein editing.

- Techniques: Dual-noise self-supervised representation learning (Self-Flow); External-encoder representation alignment; Multi-reference conditioning for consistency; Chaining edited frames as video keyframes
- Tools: FLUX.1, FLUX Context, FLUX.2, FLUX.2 Klein, Self-Flow, DINOv2, DINOv3, Qwen

## [Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind](../videos/cVzf49yg0D8.md)
`cVzf49yg0D8` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: agent-architecture, mcp-and-tools, context-engineering

Google DeepMind hands-on workshop on building agents with the Gemini Interactions API (server-side state, background runs, skills) and the Live API (native-audio voice agents), with live demos that partly failed.

- Techniques: Chained interactions via previous ID; Async background runs with polling or webhooks; Skill that links to live docs; Tool loop with recursion; Server-to-server Live proxy; Ephemeral token for direct browser connection; Context window compression for long Live sessions; Voice persona through system instructions; Send a single image and then audio
- Tools: Gemini Interactions API, Gemini Live API, Google AI Studio, Gemini 3 Flash / 3.1 Flash Live, Lyria 3, Nano Banana, Google Search grounding, uv, FastAPI, Context7, skills.sh, Antigravity

## [Give Your Chat Agent a Voice — Luke Harries, Head of Growth, ElevenLabs](../videos/DCZZ3AJKzuc.md)
`DCZZ3AJKzuc` · AI Engineer · 2026-05-18 · q2 · intro · demo · also: agent-architecture, mcp-and-tools

ElevenLabs' Luke Harries argues chat agents should add voice, and previews VoiceEngine, a wrapper that adds STT, TTS and turn-taking to an existing chat agent without a rebuild.

- Techniques: Voice wrapper around an existing agent; Client-side vs server-side tools for voice; Prompt a coding agent with a conversion skill
- Tools: ElevenLabs VoiceEngine, ElevenLabs Scribe (speech-to-text), ElevenLabs V3 (text-to-speech), ShadCN / Vercel-style UI components

## [Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind](../videos/xOP1PM8fwnk.md)
`xOP1PM8fwnk` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: models-research, inference-serving, training-finetuning-rl

Google DeepMind's Sander Dieleman walks through training image and video diffusion models at scale: learned latents, how denoising works, guidance, step-count distillation, and control signals added in post-training.

- Techniques: Two-stage latent diffusion with a learned autoencoder; Guidance by amplifying the conditional-minus-unconditional difference; Deterministic sampling as a distillation teacher; Consistency distillation restricted to sampling intervals; Injecting conditioning via extra tokens or broadcast; Data-parallel first, then model-parallel sharding with JAX pjit
- Tools: JAX, pjit, TPU, Stable Diffusion, GLIDE, EQVAE, Veo, Genie

## [This Tiny 82M Model Just Beat Most TTS APIs (Runs Locally)](../videos/bdf6BxyxCnQ.md)
`bdf6BxyxCnQ` · Better Stack · 2026-05-02 · q3 · intro · review · also: local-ai, infra-cost-scaling

Better Stack tries Kokoro 82M, a small open TTS model, on a Mac M4 Pro and weighs its speed, privacy and cost against its missing voice cloning and emotion control.

- Techniques: Run a small local TTS model as a drop-in for cloud TTS; Pick a small TTS model when time-to-first-audio matters; Evaluate TTS by listening to your own text per language and voice
- Tools: Kokoro 82M (TTS model, Apache 2.0), StyleTTS2 (architecture the model is based on), Misaki (text processing library named by the host), XTTS, CosyVoice, F5-TTS, ElevenLabs (cloud TTS), OpenAI TTS (cloud TTS), Python, pip, conda, Mac M4 Pro (test hardware)

## [Netflix's New AI Can Now Remove Actors From Scenes (VOID Model Breakdown)](../videos/1yj46x45-QI.md)
`1yj46x45-QI` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: models-research, dev-tools

Walkthrough of Netflix's open-source VOID model, which removes an object from video and also rewrites the physical consequences of its removal, plus a self-built web UI and the setup gotchas the speaker hit.

- Techniques: Two-stage video object removal with an intermediate mask; Counterfactual training data from paired simulations; Running VOID on RunPod (speaker's setup); Web UI workflow, tab by tab; Prompting for the counterfactual background; Segment every part of the target
- Tools: VOID (Video Object and Interaction Deletion, Netflix open source), SAM2 (Segment Anything Model 2), SAM3 (gated; required for the inference command, per the speaker), Gemini API (pose estimation for quad mask generation), Video diffusion model (unnamed in transcript), Vision-language model (unnamed in transcript), Flow Warp Noise (second-pass shape stabilization), Kubric/'Kubrick' physics simulator (likely; caption), RunPod (H100 GPU pods), Hugging Face (model downloads), Gradio (VOID's official demo), run.sh (speaker's repo install script)

## [Lightpanda: The 64MB Browser That is 60x FASTER than Chrome](../videos/yFWYK3wN88w.md)
`yFWYK3wN88w` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: mcp-and-tools

Better Stack tests Lightpanda, a Zig-built headless browser that speaks CDP, against headless Chrome in a Claude SDK web-fetch agent: far less memory and faster at scale, but it fails on the Airbnb single-page app.

- Techniques: Lightpanda as a CDP fetch backend; Custom WebFetch tool in a Claude SDK agent loop; Fair headless-browser benchmark; Route by page type (implied by the verdict)
- Tools: Lightpanda, Chrome (headless), Puppeteer, Playwright, Claude SDK, Chrome DevTools Protocol, OpenClaw, Vercel agent browser, Chrome MCP server (referenced as a related video)

## [Stop Assuming Your AI Agent Can Read the Web (Test It!)](../videos/OlNZCtk100Q.md)
`OlNZCtk100Q` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: evals, testing-verification

Walkthrough of the Agent Reading Test, a canary-token benchmark that checks whether an AI agent's web fetch pipeline actually reads a full page, with a 13/20 Kimi 2.5 example.

- Techniques: Canary-token reading audit; Verify agent-reported coverage against the answer key; Checklist of web-fetch failure modes
- Tools: Agent Reading Test (agentreadingtest.com), Claude Code, Kimi 2.5

## [The FASTEST Vision Model for Your Laptop (Liquid AI LFM 2.5)](../videos/ZeMuQh9j3dE.md)
`ZeMuQh9j3dE` · Better Stack · 2026-04-02 · q2 · intro · review · also: local-ai, models-research

Better Stack demos Liquid AI's LFM vision-language model running in the browser via WebGPU and ONNX Runtime; real-time webcam captioning works offline once cached, but no benchmarks are measured.

- Techniques: Run a vision-language model in the browser; Native resolution with tiling for large images; Offline verification by disabling the network
- Tools: Liquid AI LFM (Liquid Foundation Model), vision-language variant, 1.6B parameters (title says LFM 2.5), WebGPU (browser GPU API), ONNX Runtime (transcribed as 'onyx runtime', running in the browser), Hugging Face Spaces (demo host)

## [Qwen TTS Just Changed Open-Source Voice](../videos/Lw7mrsG58KY.md)
`Lw7mrsG58KY` · Better Stack · 2026-03-02 · q2 · intro · review · also: local-ai

Hands-on test of Qwen3 TTS, an Apache 2.0 open-source voice model that is steered by plain-language emotion and persona instructions and runs fully local; compares it with ElevenLabs, Chatterbox and Vibe Voice.

- Techniques: Voice cloning in the Qwen3 TTS web UI; Emotion and delivery via the instruct box; Persona voice design; Local setup
- Tools: Qwen3 TTS (Alibaba open-source TTS; 1.7B variant and a lighter model, size not stated), Chatterbox (open-source TTS with emotion slider), Vibe Voice (Microsoft, voice cloning), ElevenLabs (commercial TTS)

## [An Open-Source Audio Model From Microsoft That Does Too Much…](../videos/AyHSSslWeHE.md)
`AyHSSslWeHE` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: local-ai, models-research

Hands-on review of Microsoft's open-source VibeVoice speech stack: strong on long-form multi-speaker audio and offline use, weaker on emotion, languages and polish; worth it for local devs, not production.

- Techniques: Long-form multi-speaker generation in one pass; Voice cloning via the Gradio UI; Using structured ASR output (diarization plus timestamps); Incremental streaming for voice agents
- Tools: VibeVoice (Microsoft), Gradio, Hugging Face (demo and model hosting), Chatterbox, ElevenLabs, Whisper, CosyVoice (called Cozy Voice in transcript), Qwen TTS models, macOS Voice Memos

## [Google Just Solved The Greatest Limitation of AI Agents](../videos/uprZUcv0FSc.md)
`uprZUcv0FSc` · AI LABS · 2026-03-02 · q3 · practitioner · review · also: mcp-and-tools, coding-agents

Walkthrough of WebMCP, a proposed browser standard where websites register callable tools for agents instead of agents guessing from screenshots or DOM. Covers declarative and imperative APIs, per-page tool loading, and current limits.

- Techniques: Declarative WebMCP tool on an HTML form; Imperative WebMCP tool registration per route; Scope tool lists to the page (contextual loading); Write tool descriptions for a cold reader; Inspect tool schemas with the Model Context Tool Inspector extension; Test with the Gemini-backed demo paths
- Tools: WebMCP, Chrome Canary, Chrome 146, Chrome Labs WebMCP repo, Model Context Tool Inspector extension, Claude Code, Gemini (built into Chrome; Gemini API key option in the demo), Next.js, React, Zen browser, Community WebMCP bridge (unnamed, not identified), Brilliant (sponsor)

## [I Didn’t Expect Open-Source Speech AI to Do This](../videos/7jJEK95o7T8.md)
`7jJEK95o7T8` · Better Stack · 2026-02-02 · q2 · intro · review · also: —

Short hands-on demo of SpeechBrain, an open-source PyTorch speech toolkit: noise enhancement and speaker verification work well in the demos, while live ASR did not.

- Techniques: Pre-trained noise enhancement on a noisy recording; Enroll-then-verify speaker check; Gradio front end for quick speech demos
- Tools: SpeechBrain, PyTorch, Hugging Face, Gradio, VoxCeleb (dataset the speaker model was pre-trained on), macOS (test machine)

## [NVIDIA’s New Voice AI is Absolutely WILD! (PersonaPlex)](../videos/n_m0fqp8xwQ.md)
`n_m0fqp8xwQ` · Better Stack · 2026-02-02 · q3 · intro · review · also: models-research, inference-serving

Hands-on look at NVIDIA's open PersonaPlex full-duplex voice model: deploy on a rented RunPod A40, run the Moshi server, and test role prompts, which work for scripted flows but drift under confusing input.

- Techniques: Deploy PersonaPlex on a rented GPU pod; Role prompt presets and custom persona prompts in the web UI; Stress-test a voice model with adversarial and off-script user turns
- Tools: PersonaPlex (NVIDIA open voice model, full-duplex), Moshi (Kyutai speech-to-speech architecture and server), Mimi (neural audio codec), Opus (audio codec, installed on the server), RunPod (GPU container hosting, A40 used), PyTorch Ubuntu template (RunPod), Hugging Face (model download, token required), ChatGPT voice mode (comparison only)

## [Claude Code Can Now Control Your Browser (Thanks to Vercel)](../videos/P7JrP57AxR0.md)
`P7JrP57AxR0` · Better Stack · 2026-02-02 · q3 · practitioner · review · also: testing-verification, coding-agents, mcp-and-tools

Walkthrough of Vercel's open-source Agent Browser, a headless-Chromium CLI that lets a coding agent snapshot, click and test web pages, with a comparison to Browser Use and the Playwright MCP server.

- Techniques: Agent-driven UI verification loop; Install the CLI globally and let the agent discover it; Generate a bash regression test from the browser session; Prefer snapshot references, fall back to semantic locators
- Tools: Agent Browser (Vercel, open source), Rust, Node.js, Playwright, Chromium, OpenCode, GLM 4.7, npm, shadcn/ui (transcribed as 'Shadxian'), React (transcribed as 'Riat'), Vite, Browser Use

## [I Wasn't Ready For What This Does](../videos/XP6TJRbOdGo.md)
`XP6TJRbOdGo` · AI LABS · 2026-02-02 · q2 · intro · tutorial · also: vibe-coding-app-building, context-engineering

A step-by-step landing-page workflow: Google Whisk keyframes, Google Flow frame-to-video, MP4-to-animated-WebP for a scroll-mapped hero, then Claude adds HeroUI, Motion.dev and 21st.dev components in Next.js.

- Techniques: Two-keyframe hero animation; MP4 to animated WebP for scroll mapping; XML-sectioned prompt for an AI coding agent; Install individual UI components instead of the whole library; Copy-paste component prompts from 21st.dev
- Tools: Google Whisk, Nano Banana (image generation, via Whisk), Gemini 3 (prompt expansion layer in Whisk; planning in Flow), Google MixBoard, Google Flow, VO 3.1 (video model; 20 credits per video), Claude (coding agent), Next.js, Tailwind CSS, HeroUI (library, formerly Hero UI), framer-motion, Motion.dev (motion library)

## [I Stress-Tested Meta’s SAM 3D on Real Photos And The Results Were Shocking!](../videos/vKWDiHZGPs4.md)
`vKWDiHZGPs4` · Better Stack · 2026-01-02 · q3 · intro · tutorial · also: inference-serving

Better Stack tutorial that walks through Meta's SAM 2 and SAM 3D Objects models and builds an Expo mobile app that turns a photo into a 3D model, with the models hosted on a rented RunPod A40 GPU.

- Techniques: Provision a RunPod GPU pod for vision models; Hugging Face gated-model access setup; One-command setup script, then launch the API; Point the Expo client at the pod; Iterative point-based segmentation before 3D generation; Export and inspect generated assets
- Tools: SAM 2, SAM 3, SAM 3D Objects, SAM 3D Body, Expo, RunPod (A40 GPU pod), RTX 5090 (mentioned as a faster alternative), Hugging Face CLI, uvicorn, npm, Blender, GLB file format

## [Claude Released Something To Fix Your Errors](../videos/NuKrtiJqW3Y.md)
`NuKrtiJqW3Y` · AI LABS · 2026-01-02 · q2 · practitioner · tutorial · also: testing-verification, coding-agents, context-engineering

Tips for testing web apps with Claude Code's Chrome extension: full-page screenshot scripts, CLAUDE.md context and cookie-banner rules, split test files, progress reports across compaction.

- Techniques: Full-page screenshot script behind a slash command; CLAUDE.md rule to limit DOM extraction; Cookie-banner dismissal script run first; Authenticate before handing off the task; Split end-to-end testing into per-area test files; Progress report after each test file; Compact and check context before browser test runs; Guided testing slash command
- Tools: Claude Code, Claude Code Chrome extension (Claude in Chrome integration), Playwright MCP, Puppeteer MCP, Google Chrome, Google Docs, Google Sheets, CLAUDE.md, Chrome Manifest V3 extensions

## [An Open-Source Alternative to ElevenLabs](../videos/chH2tlh_Vvk.md)
`chH2tlh_Vvk` · Better Stack · 2026-01-02 · q3 · intro · review · also: local-ai

Quick hands-on look at Resemble AI's open-source, MIT-licensed Chatterbox Turbo TTS: runs locally, fast enough for agents, with honest drawbacks around overacting and tail artifacts.

- Techniques: Local offline TTS setup; Zero-shot voice cloning from short reference audio; Tune expressiveness with exaggeration, CFG weight and inline tags; Post-process generations to remove tail artifacts; Benchmark on your own hardware before committing
- Tools: Chatterbox Turbo, Chatterbox Multilingual, Chatterbox (original), Python, Torch, conda, Gradio, Hugging Face, MLX audio, Spark TTS, ElevenLabs, Perth watermarking

## [10 Crazy Ways To Use Nano Banana Pro](../videos/OWdlgdQSR60.md)
`OWdlgdQSR60` · AI LABS · 2026-01-02 · q2 · intro · review · also: models-research

A 5-minute AI LABS walkthrough of ten prompting and editing tips for Google's Nano Banana Pro image model, with a Make.com sponsor segment and a brief SynthID note.

- Techniques: Iterative single-feature edits; Context word for style; Infographic prompt pattern; Entity locking with reference images; Search grounding before generation; Narrative storyboard prompt; Sketch or wireframe as input; Resolution and texture in the prompt
- Tools: Nano Banana Pro (Google image model), Gemini (watermark, plans), Google Search (grounding), SynthID (invisible watermark), Make.com (sponsor)

## [The WhatsApp Trick That’s Running My Business for Me](../videos/BjqR3Ddb71k.md)
`BjqR3Ddb71k` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools

A 6-minute setup tutorial for a local WhatsApp MCP server plus the ElevenLabs MCP in Claude Desktop, so an agent can read WhatsApp chats and reply with a synthesized voice note.

- Techniques: Local WhatsApp MCP setup in Claude Desktop; Adding the ElevenLabs MCP with one env var; Prompt the agent with an explicit contact name; Windows build fix for the WhatsApp bridge
- Tools: Claude Desktop, WhatsApp MCP server (Go bridge + MCP), ElevenLabs MCP, ElevenLabs voice cloning, uv / uvx, Go, Cursor, Windsurf, Blender MCP, Swift (planned app), MCP

## [Get Started with Claude’s Computer Use API – Full Setup & Demo](../videos/XSXaGvCRJ3c.md)
`XSXaGvCRJ3c` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: sandboxing-execution, token-cost-efficiency

A 4-minute walkthrough of Anthropic's Computer Use API beta: run the setup container locally with Docker and your API key, then watch Claude operate a sandboxed virtual Linux desktop from a chat prompt.

- Techniques: Run computer use inside a disposable container; Give a multi-step browsing prompt and watch the screenshot loop
- Tools: Claude Computer Use API (Anthropic, beta), Claude API key (Anthropic), Docker, WSL2, Ubuntu, Bolt.new (named only as the video the agent found on the channel, not used as a tool)

## [Automate Your Browser with AI Using StageHand AI Agent](../videos/PPutzww1RaM.md)
`PPutzww1RaM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents

Short quickstart for Stagehand, a Playwright-based browser agent with plain-language act, goto and extract APIs, scaffolded with a create-app command and driven from Cursor.

- Techniques: Scaffold a Stagehand project; Plain-language page actions and extraction; Generate Stagehand code in Cursor
- Tools: Stagehand, Playwright, Browserbase, Cursor, Zod, Chromium, GPT-4 (via OpenAI API), Node.js / npm / npx

## [Janus Pro-7B: DeepSeek's New Model](../videos/m7M_EWV_GOg.md)
`m7M_EWV_GOg` · AI LABS · 2025-11-02 · q2 · intro · demo · also: models-research

A short hands-on demo of DeepSeek's Janus Pro 7B multimodal model on a Hugging Face Space, covering formula-to-LaTeX, image and code understanding, and text-to-image, with the speaker's training and limitation claims.

- Techniques: Quick multimodal capability probe; Round-trip check for OCR-to-markup output
- Tools: Janus Pro 7B (DeepSeek, multimodal), Janus Pro 1.3B / 1.5B (mentioned, sizes inconsistent in transcript), Hugging Face Spaces, DALL-E 3 (comparison only), Python (screenshot content), Online LaTeX viewer (unnamed)

## [Build an AI Video Generator Like Sora (with ComfyUI)](../videos/DxvC2B0eVkc.md)
`DxvC2B0eVkc` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: local-ai, dev-tools

Step-by-step tutorial for running ComfyUI on a rented DigitalOcean GPU droplet, chaining an OmniGen2 text-to-image workflow into a WAN video workflow, and serving the export through ViewComfy over SSH tunnels.

- Techniques: Remote GPU with SSH-tunneled ComfyUI; Downloading models into the path the workflow expects; Chain text-to-image into image-to-video; Shared prompt node across two text encoders; Export ComfyUI workflow as API JSON and run it in ViewComfy; Cost control for rented GPU droplets
- Tools: ComfyUI, comfy-cli, DigitalOcean GPU Droplets, NVIDIA RTX 4000 Ada, WAN video generation model (speaker says 2.25B parameters, auto-caption), OmniGen2, ViewComfy, Next.js, pip3, SSH

## [Coding Test: Can CLAUDE COMPUTER USE Build Apps?](../videos/XbL5nzTLtag.md)
`XbL5nzTLtag` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, context-engineering

A short hands-on test of Claude Computer Use building a budget-manager app: it handled terminal setup but failed at front-end code generation, and a page refresh wiped the project.

- Techniques: Staged prompt decomposition for agent app builds; Verify toolchain installs in the agent's terminal; Keep recoverable copies of agent-generated work outside the agent's UI
- Tools: Claude Computer Use API, Claude (Claude 3.5 mentioned as the comparison model), ChatGPT (used to write and split the build prompt), Node.js, npm

## [Google Just Released the ULTIMATE AI SDK (And It's Good)](../videos/Ksac1CuaBvQ.md)
`Ksac1CuaBvQ` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: dev-tools

A short Better Stack walkthrough of Google's new Gen AI JavaScript SDK for Gemini: one client for text, image and video analysis and generation, plus the speaker's complaints about API design, model access and cost.

- Techniques: Single client, method per modality; Poll-then-download for video generation; Express plus Multer upload endpoint; OpenAI SDK pointed at Gemini for text
- Tools: Google Gen AI SDK for JavaScript (Gemini API), Gemini, Veo 3 (said as VO3; the transcript caption is unclear), Express, Multer, Vertex AI, OpenAI SDK, Replicate, Google Search grounding

## [AI vs GeoGuessr Pro](../videos/3kPq2LlZh_U.md)
`3kPq2LlZh_U` · Better Stack · 2025-11-02 · q2 · intro · demo · also: models-research

Better Stack pits OpenAI's o3 (screenshot only, no web search) against GeoGuessr pro ZigZag over five rounds; o3 wins 22,197 to 21,379 on the video's totals.

- Techniques: Blind visual-geolocation eval with a human expert as baseline; Reading the reasoning trace for the cues a model used
- Tools: ChatGPT, OpenAI o3, GeoGuessr, Google Street View

## [Can AI Agents Finally Automate the Web? (BrowserOS Review)](../videos/rIZ8OBHL7Zo.md)
`rIZ8OBHL7Zo` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: local-ai, dev-tools

Better Stack reviews BrowserOS, an open-source Chromium-based agentic browser; the built-in agent works on Gemini, but local Ollama models mostly failed the Amazon cart task.

- Techniques: Run BrowserOS's agent on a local Ollama model; Evaluate candidate models on a browser-agent task before relying on them; Customize an agent's instructions by rebuilding from source
- Tools: BrowserOS, Chromium, Chrome, Perplexity Comet, Opera Neon, Fellow AI, OpenAI Operator, Brave, Arc, Dia, Ollama, Gemini 2.5

## [Anthropic Claude AI Agentic Browser: The Claude Chrome Extension for Builders (EXCLUSIVE DEMO)](../videos/TVetQbcgdMU.md)
`TVetQbcgdMU` · AI LABS · 2025-11-02 · q3 · practitioner · review · also: coding-agents, testing-verification

Hands-on demo of Anthropic's Claude Chrome extension as a visual-testing partner for Claude Code: a slash command reviews each finished task on a running dev server, and the browser agent reports visual and functional issues.

- Techniques: Per-task visual review slash command; Fresh chat per task; Prioritized improvement triage before the next task; Batch review of several tasks; Per-site approval allowlist for browser actions
- Tools: Claude Code, Claude Chrome extension (Claude browser extension, research preview), Claude 4 series models, Next.js, GPT (used to brainstorm the app idea), BMAD method (mentioned, not used), Playwright MCP (compared, not used), Cursor (mentioned as a competitor)

## [Sora 2 Cameos & Jailbreaks & Claude Agent SDK | Better Stack Podcast Ep. 5](../videos/YjdMscni2CI.md)
`YjdMscni2CI` · Better Stack · 2025-11-02 · q2 · intro · panel · also: claude-code, agent-architecture, context-engineering

Better Stack podcast: hosts riff on Sora 2's cameo feature, memorized training data and weak guardrails, then on the Claude Agent SDK for custom agents with their own prompts, tools and hooks. Mostly opinion.

- Techniques: Custom agent on the Claude Agent SDK with an owned system prompt; Local functions as agent tools in place of MCP tools; Hook-based output enforcement with automatic redo; Coaching agent that withholds answers
- Tools: Sora 2, VO3, Claude Agent SDK, Claude Code, Claude Code hooks, MCP, Claude Sonnet 4.5, Claude Opus, GPT-5, GPT-5 Codex, Codex, Grok 4

## [This Voice AI Creates Full Podcasts in Minutes! (Microsoft's VibeVoice)](../videos/uCOu4HZpPdQ.md)
`uCOu4HZpPdQ` · Better Stack · 2025-11-02 · q3 · intro · review · also: models-research

Hands-on review of Microsoft's open-source VibeVoice TTS: long multi-speaker audio from an LLM plus diffusion head, a RunPod setup to generate movie-trivia podcasts, and a skeptical verdict on its uncontrolled expressive output.

- Techniques: Script-then-speech podcast pipeline; Steering expressive output through the script prompt; Reproducing the demo on RunPod; Model design choices for long audio
- Tools: VibeVoice (Microsoft open-source TTS; 1.5B model and a larger model; version not stated), OpenAI API (speaker script generation), TMDB API (movie metadata), Wikipedia (trivia source), RunPod (A40 GPU hosting), uv (Python env and runner), Encodec (comparison baseline only), NotebookLM (comparison point only)

## [You Won’t Believe What Google Gemini 2.0 Can Do Now!  - #gemini2flash #aistudio](../videos/teEp3I83k-w.md)
`teEp3I83k-w` · AI LABS · 2025-11-02 · q2 · intro · review · also: models-research, sandboxing-execution

Walkthrough of Gemini 2.0 Flash's real-time webcam and screen-share mode in Google AI Studio, with a list of claimed benchmark scores and quick tests of its tools. Mostly a demo with light substance.

- Techniques: Live screen and webcam Q&A for unfamiliar software; Show token counts and temperature in AI Studio; Small smoke-test battery for a new model; Re-prompt once when grounding returns no sources; Get API access from AI Studio or OpenRouter
- Tools: Gemini 2.0 Flash, Gemini 1.5 Flash, Gemini 1.5 Pro, Google AI Studio, Gemini Multimodal Live API (Stream Real-Time), Google Search grounding, Gemini code execution, Microsoft Word, Adobe Premiere Pro, OpenRouter

## [How I Built a ChatGPT Powered Voice Agent with MCP + LiveKit](../videos/jRk63S3v-UQ.md)
`jRk63S3v-UQ` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: mcp-and-tools

Tutorial on building a voice agent with a LiveKit + Cartesia + OpenAI base, then wiring a local WhatsApp MCP server into it so speech can trigger tool calls.

- Techniques: Clone, install with uv, and run the voice agent locally; Change the LLM and the system prompt in the main agent file; Wire an MCP server into the voice agent through the MCP-use library
- Tools: LiveKit (voice agent transport and dashboard), OpenAI GPT-4o mini (LLM; transcribed as GPT-40 mini), OpenAI Whisper (speech-to-text), Cartesia Sonic preview (TTS), MCP-use library (MCP tool-use agent), WhatsApp MCP server (local), Brave Search MCP, Airbnb MCP (mentioned as a possible example), uv (Python package manager), Cursor (editor), git

## [Suno AI Tutorial - Make a Song Like Your Favorite Artists with Suno AI](../videos/tfntgZYlGko.md)
`tfntgZYlGko` · AI LABS · 2024-11-02 · q2 · intro · tutorial · also: —

A five-minute walkthrough of making songs in Suno AI (custom lyrics, style, vocal or instrumental tracks) plus its free-tier limits; a basic consumer tutorial with no engineering content.

- Techniques: Suno custom-mode song generation; Instrumental track generation; Steering with the style and genre list
- Tools: Suno AI (web app, Create tab, Custom Mode, instrumental toggle), ChatGPT (optional lyric generation)

## [AI Images Are Getting Shockingly Real - FLUX 1.1 PRO](../videos/sFZR6EG4WxU.md)
`sFZR6EG4WxU` · AI LABS · 2024-11-02 · q2 · intro · tutorial · also: product-ux

Short tutorial on generating photoreal images with Flux 1.1 through Together AI, using a prompt-template trick; anecdotal, hype-driven, and untested.

- Techniques: Flux 1.1 generation on Together AI (UI steps); Photo-style prompt template (speaker's 'secret trick'); Type-word plus file-type prompt
- Tools: Flux 1.1 (Flux 1.1 Pro per the title; the transcript says Flux 1.1), Together AI (website, Google sign-in)

## [The MIND-BLOWING Way to Create Videos with Kling AI!](../videos/r4eCgDR3_MU.md)
`r4eCgDR3_MU` · AI LABS · 2024-11-02 · q2 · intro · review · also: —

A short walkthrough of the Kling AI web app for generating AI videos and images from text prompts, with its free daily credits and settings. Thin on substance and not relevant to our projects.

- Techniques: Generate a text-to-video clip in Kling's web app; Generate images with reference and count settings
- Tools: Kling AI (web app: AI Video, AI Image, AI Video Editor which is marked coming soon)

