# Guide: voice-multimodal

*Synthesized by Sonnet from 79 talks since 2026-05-18.*

Scope: voice agents, realtime speech, vision and video, computer use, browser agents, robotics and on-device models.

## State of the art

**Voice agents: the cascade still wins in production.**
- Teams ship streaming STT, then an LLM with tools, then streaming TTS. Speech-to-speech is not yet reliable enough (`P_RI1kCkRbo`, `a8EcVumh71E`, `MBHOH1NmDqc`, `hMlLw1LeIK8`).
- Latency is the main design constraint. Practitioners measure time to first audio, per stage, at P95 (`vblnYHzBgS4`, `hMlLw1LeIK8`, `xLUQOqjudtA`).
- Typical cloud stacks land at 750 ms to 1.3 s. Quoted targets run from under 550 ms (`vblnYHzBgS4`) to about 950 ms before a reply should start (`fnLBmfsI_Fg`).
- Turn-taking is treated as an audio problem. The current best pattern is VAD plus a learned end-of-turn model plus a silence timer as a safety net (`hMlLw1LeIK8`).
- Barge-in is classified, not always treated as a stop (`hMlLw1LeIK8`, `xLUQOqjudtA`).

**Small model plus harness.**
- A small, fast model does the talking. Code owns the state, planning and decisions (`fnLBmfsI_Fg`, `m24UKZomm7k`).
- Heavy work goes async to a bigger model (`65X0pQ6Lmbg`, `a8EcVumh71E`).
- Some teams route per turn by stakes, not cost (`xLUQOqjudtA`).
- Others keep a frontier model and hide latency with tricks: early generation on partial transcripts, background tool calls, and a TTS prefix cache (`MBHOH1NmDqc`).

**Voice without speech output.**
- Voice input with visual output is often better than voice-to-voice (`65X0pQ6Lmbg`).
- OpenAI frames three modes: speech-to-speech, speech-to-action, event-to-speech. Speech-to-action is under-explored (`OpY6MmZFeHo`).
- ElevenLabs argues voice needs a visual co-channel (`u-rJwPPU3QA`).

**Voice reliability and ops.**
- Real error rates are around 10 percent (`qStB9GbppMU`).
- Transcripts hide failures, so teams trace whole audio sessions and run audio-native evals (`42Bz0TUfeOQ`).
- Clinical voice teams use simulated users, calibrated judges and hazard-linked evidence (`McknwOzbmyg`, `AN65uc645mE`).

**Browser and computer-use agents.**
- The shared view is that the harness matters more than the model (`JnubYCYunk8`, `GqoNrUz8hEU`, `p7gaxmCUiIU`).
- Compact page views (accessibility tree, a few thousand tokens) beat the full DOM (`JnubYCYunk8`, `GqoNrUz8hEU`, `tyFPqtyOK5w`).
- Production systems record a successful run as code, verify each step, and heal it when it breaks (`tyFPqtyOK5w`, `5xi_S1f9sDU`).
- Verification is the bottleneck. LLM judges overstate success (`xLxhT2ZI7UM`), and static benchmarks can be gamed by replay (`CTLa_p6iOiY`).
- Websites are adding agent-facing tool surfaces, such as WebMCP (`ghJmWQCIHRM`, `LMbeDEQO6QM`).
- One camp expects pixel-level agents to cover the long tail (`Ki980nV0__0`).

**Vision, video and generation.**
- Google ships separate specialist media models, not one omni model, and uses a cheap LLM to write their prompts (`BcWFc3H7Khg`, `ns9f1fjLD7Y`, `GIRpQEfYf3U`).
- Real-time video comes from distillation and causal attention (`Xln-On3syJk`, `z1dqv74SpUs`, `gHs5ZiY80PM`).
- Video evals are moving to small distilled judges trained on pairwise data (`b_PmGocP4rc`).
- Video memory is moving to a context graph built once at ingest (`mOf-PP4mVjA`).

**On-device and robotics.**
- Small models (Gemma 4, MLX) now run on phones (`a2muGkT4WD4`, `_A367W_qvc8`, `hacEQHHhu2Q`).
- Robotics is a data and reliability problem (`Sjfz1TqxzEs`, `jFHteJjRl8A`).

## Consensus patterns

1. **Cascade first, speech-to-speech later.** Move only when the new stack has tools, observability and content quality equal to the cascade (`P_RI1kCkRbo`, `MBHOH1NmDqc`, `a8EcVumh71E`).
2. **Budget latency per stage and watch the tail.** Break it into endpointing, STT, LLM first token, TTS first byte and playback. Track P95, not P50 (`hMlLw1LeIK8`, `vblnYHzBgS4`, `xLUQOqjudtA`).
3. **Stream everything.** Start playback on the first audio chunk. Take partial STT while the user is still talking (`3jGAU2sbAyY`, `0jeZfjJMfmo`, `MBHOH1NmDqc`).
4. **Layered turn detection with a fallback.** Use VAD, then a learned end-of-turn model, then a timer (`hMlLw1LeIK8`). Tune the barge-in rule: Tolan accepted about 60 ms extra latency to halve the worst early aborts (`xLUQOqjudtA`).
5. **Filler and preambles hide tool latency.** Tool calls, not TTS, are now the main delay (`P_RI1kCkRbo`, `OpY6MmZFeHo`).
6. **Keep the model small and the harness strong.** The model proposes. Code validates and decides the next state (`m24UKZomm7k`, `fnLBmfsI_Fg`).
7. **Keep prompts prefix-stable** so provider caching works (`65X0pQ6Lmbg`, `xLUQOqjudtA`).
8. **Wrap, do not rebuild.** Add voice to an existing agent and reuse its tools, split into client-side and server-side tools (`DCZZ3AJKzuc`, `OpY6MmZFeHo`).
9. **Give ASR context.** Pass conversation and domain context into recognition, boost keywords per call phase, and re-score short answers with full context (`AN65uc645mE`, `vblnYHzBgS4`, `IDNfAZVKvPE`).
10. **Evaluate audio, not transcripts.** Use session traces, audio-native judges, scenario-varied regression runs, and production A/B tests (`42Bz0TUfeOQ`, `qStB9GbppMU`, `McknwOzbmyg`).
11. **Compress what the browser agent sees.** Use the accessibility tree plus an optional screenshot, and report page deltas after each action (`JnubYCYunk8`, `GqoNrUz8hEU`, `tyFPqtyOK5w`).
12. **Move deterministic steps out of the model.** Replay recorded runs as code. Keep a model fallback at the failing step (`5xi_S1f9sDU`, `tyFPqtyOK5w`, `GqoNrUz8hEU`).
13. **Define success as a checkable artifact.** Measure per transaction. Use pass^k, not pass@1 (`5xi_S1f9sDU`, `tyFPqtyOK5w`).
14. **Verify with rubrics and evidence.** Never trust an uncalibrated judge. Check agent claims against screenshots (`xLxhT2ZI7UM`, `McknwOzbmyg`).
15. **Skills as portable site knowledge.** A teacher agent writes learnings into a skill file that any agent can load (`p7gaxmCUiIU`, `GqoNrUz8hEU`).
16. **Prefer deterministic access over a browser.** Use APIs and search first, a browser last, and validate page content before the LLM sees it (`XsvUhpnHepE`, `zTZ0qunQXnM`, `26RtyAm9y_Q`).
17. **Use a cheap model to write prompts for expensive generative models,** with structured output between stages (`BcWFc3H7Khg`, `ns9f1fjLD7Y`).
18. **Distill for real time.** Collapse denoising steps and use causal attention (`gHs5ZiY80PM`, `Xln-On3syJk`, `z1dqv74SpUs`).

## Disagreements & open questions

- **Cascade vs native speech-to-speech.** Google DeepMind argues one multimodal model gives better translation, interruption handling and proactive gating (`18Um2VjMM_g`, `xfPVBzDYjH4`, `Bc6Ojl2XS1w`). Others say it trades intelligence for naturalness and lacks tools and observability (`P_RI1kCkRbo`, `a8EcVumh71E`). A middle path is a small full-duplex front end that hands off to a text LLM (`a8EcVumh71E`).
- **Frontier vs small model for voice.** Microsoft and Plivo say small and fast (`fnLBmfsI_Fg`, `vblnYHzBgS4`). EliseAI keeps a frontier model and engineers around the latency (`MBHOH1NmDqc`). Tolan routes by stakes (`xLUQOqjudtA`).
- **Pixels vs structure for browser agents.** Yutori says pixels are the source of truth (`Ki980nV0__0`). Others say compressed DOM or accessibility structure, with a screenshot as a backup (`JnubYCYunk8`, `tyFPqtyOK5w`, `GqoNrUz8hEU`).
- **CLI vs MCP for browser control.** The speaker cites equal success and much lower cost for a CLI (`26RtyAm9y_Q`). WebMCP bets on sites exposing tools (`ghJmWQCIHRM`).
- **Do not run VLMs at runtime.** Hugging Face says use a VLM to label data and train a small detector (`dKcTBQzR7jI`). Others put VLMs directly in the agent loop (`2wgPHvW0mG8`, `jNE8No-wvok`).
- **Pretty pixels vs causal structure in world models** (`4Gqg0HVe-AY`, `KLDdXOw6jIc`).
- **Open questions.** Can end-of-turn and barge-in be solved without extra latency? How do you judge video and computer-use runs without gameable or overconfident judges (`CTLa_p6iOiY`, `xLxhT2ZI7UM`, `KLDdXOw6jIc`)? Does the cost of a skill or harness pay back once base models improve (`ns9f1fjLD7Y`)?
- **Vendor-heavy talks.** Many numbers are self-reported (`qStB9GbppMU`, `AN65uc645mE`, `ZZcE0HeO-Hc`). Treat them as claims.

## How thinking changed over time

- **2026-05-18.** Voice is pitched as the next interface. Gradium says tool-call latency now beats TTS latency as the bottleneck (`P_RI1kCkRbo`). TTS is described as LLM-style audio-token modeling (`3jGAU2sbAyY`). On-device Gemma 4 and MLX arrive (`a2muGkT4WD4`, `_gVFUEdhCyI`).
- **2026-06-18.** Focus shifts to the media stack and agent-readable web: Gemini audio and generation (`Bc6Ojl2XS1w`, `GIRpQEfYf3U`, `BcWFc3H7Khg`), diarization limits (`mFLlVpnGpds`), and WebMCP (`ghJmWQCIHRM`, `LMbeDEQO6QM`). Voice UX gets a visual co-channel and playback-aware barge-in proposals (`u-rJwPPU3QA`).
- **2026-07-18.** "Better eyes, not better models" for browser agents (`JnubYCYunk8`). Computer use goes to background, window-scoped drivers (`ZSQb5fzRFPw`). Voice-in, visuals-out appears (`65X0pQ6Lmbg`).
- **2026-08-18.** The cluster peak. Turn-taking levels, state-machine harnesses, and small models for voice (`hMlLw1LeIK8`, `m24UKZomm7k`, `fnLBmfsI_Fg`). Browser agents are framed as a harness problem (`GqoNrUz8hEU`). Benchmarks are attacked (`CTLa_p6iOiY`). RL for messy real UIs (`Cc0_nyxROBA`). Perception agents (`2JX6JYyQG4Y`).
- **2026-09-18.** Production voice maturity. Failure modes in week one (`vblnYHzBgS4`), 10 percent error rate (`qStB9GbppMU`), clinical safety (`AN65uc645mE`, `McknwOzbmyg`), and latency hacks (`MBHOH1NmDqc`). Act, confirm or stop is framed as a cost problem (`Zd5b40Jbp_k`). Real-time video avatars (`z1dqv74SpUs`).
- **2026-09-27.** Attention moves to physical AI: robot reliability, data flywheels, and world models (`Sjfz1TqxzEs`, `jFHteJjRl8A`, `4Gqg0HVe-AY`, `ZZcE0HeO-Hc`).
- **2026-10.** Verification and learning loops. Per-step accuracy math (`5xi_S1f9sDU`), rubric verifiers (`xLxhT2ZI7UM`), hill-climbing skills (`p7gaxmCUiIU`), replay with healing (`tyFPqtyOK5w`), and voice observability (`42Bz0TUfeOQ`).

## Numbers worth remembering

- Human turn switch is about 200 ms. About 800 ms feels off. About 1.5 s makes users hang up (`hMlLw1LeIK8`).
- Target time to first audio is under about 550 ms. Most deployments sit at 750 ms to 1.2 s. Frontier model P50 first token is about 450 to 500 ms, with P90 and P95 above 1.2 s (`vblnYHzBgS4`).
- Haiku 4.5 with a state machine answered in about 900 ms. Opus 4.7 with reasoning took a couple of seconds (`fnLBmfsI_Fg`).
- Tool calls via routers take 500 ms to 4 s (`P_RI1kCkRbo`).
- Tolan's turn target is about 2 s round trip. Drift from 2 s to 2.5 s hurt most metrics. Smart turn-taking cost about 60 ms and halved the worst early aborts (`xLUQOqjudtA`).
- Voice-out needs about 200 ms. Instant feels like about 100 ms. The train-of-thought limit is about 1000 ms (`65X0pQ6Lmbg`).
- Real-world voice error rate is about 10 percent across about 10,000 monitored agents (vendor figure) (`qStB9GbppMU`).
- 2.4 s of dead air was found in one traced call (`42Bz0TUfeOQ`).
- A 99 percent per-step agent over 100 steps gives about 36 percent end to end. A 50 percent agent with up to four retries reaches about 94 percent per transaction (`5xi_S1f9sDU`).
- A 7B web agent scored 74 percent under a common judge and 38 percent under the rubric verifier. Verifier-to-human kappa was 0.58 (`xLxhT2ZI7UM`).
- A blind replay script under 1 MB can match frontier models on OSWorld-style benchmarks (`CTLa_p6iOiY`).
- A compact page view cuts about 20,000 DOM tokens to a few thousand. A screenshot is about 1,100 tokens (`JnubYCYunk8`).
- Cua Driver raised pass rate from about 62 to about 80 percent with 34 percent fewer tokens (`ZSQb5fzRFPw`).
- CLI and MCP both reach about 83 percent task success. The CLI took 7 turns against 71 round trips (`26RtyAm9y_Q`).
- A skill-hill-climbing loop cut a task from $12 to $3, and another from $6.22 to $0.51 (`p7gaxmCUiIU`).
- Sending 10 pages with only 3 valid wastes about 70 percent of tokens (`XsvUhpnHepE`).
- Audio input costs about 1,920 tokens per minute. Video at 1 fps was about 30,900 tokens for 5 minutes (`GIRpQEfYf3U`, `ns9f1fjLD7Y`).
- Cached input tokens are about 90 percent cheaper (`cVzf49yg0D8`).
- Step distillation cuts about 50 denoising steps to 4 or 8 (`gHs5ZiY80PM`). One real-time video model went from about 30 steps to 1 (`z1dqv74SpUs`).
- A Gemma E2B model needs about 2 GB RAM (about 841 MB weights). Gemma 4 at 4-bit ran about 40 tok/s on an iPhone (`hacEQHHhu2Q`, `a2muGkT4WD4`).
- A pipeline of VLM labeling, judging and detector training costs about $3 to 4 per run (`dKcTBQzR7jI`).
- Act-confirm-stop cost tuning: always-act scored 2.1 cost per turn, a guessed threshold 1.9 (`Zd5b40Jbp_k`).
- Support agent resolution went from 10 to 80 percent for about $700 per month (`pyvRID_CZZU`).

## From creator channels (Kai Explains, AI LABS, Better Stack)

Source: creator videos, mostly Better Stack hands-on tests and Kai Explains news roundups. Most numbers are vendor claims or one-run impressions. Claims marked "single video" rest on one creator.

### Practical playbook

1. **Run a barge-in test before anything else.** Start a long agent answer, interrupt mid-sentence, then check three things: it stops, the next turn works, and the reply still fits the question. Repeat across presets (`ES3HhoYCtIc`).
2. **Model barge-in as a state machine.** Detect user speech, mark the interruption, emit an interrupt signal, cancel in-flight audio and transcript, then start the new turn. If barge-in is one event, stale speech keeps playing (`blpZ1xgFhCk`). Single video.
3. **Split a fast voice layer from a slow worker.** The voice agent answers status, cancel and trivial questions itself. Real coding or tool work becomes an async task, and the result goes back into the live conversation when it finishes (`blpZ1xgFhCk`). Single video, no latency numbers.
4. **Test TTS on app-shaped strings, not demo prose.** Build one fixed set: currency with cents, a due date, a phone number, a clock time, and a short invoice sentence. Run the same set on every candidate model. The local model in the Supertonic test failed on its invoice and date sentences, and the VoxCPM2 host also found uneven quality by prompt (`pbsTTxKTuts`, `O4TMwZlUJvQ`).
5. **Prototype the voice in a hosted demo before renting a GPU.** Paste the production sentences into the model's hosted demo. Self-host only if the voice passes there. This separates voice quality from deployment work (`O4TMwZlUJvQ`).
6. **Point an existing OpenAI speech client at a local server.** Run the local server and change only the base URL, plus a parameter or two. Supertonic ships an OpenAI-compatible `/v1/audio/speech` route (`pbsTTxKTuts`). VoxCPM2 exposes the same route through vLLM on a GPU host (`O4TMwZlUJvQ`). Neither video spoke the exact commands, so take them from the repo README.
7. **Clone from a clean 8 to 10 second reference, with its transcript.** The VoxCPM2 host found the transcript improved delivery, not just timbre (`O4TMwZlUJvQ`). Voicebox also asks for a transcript in the voice profile (`RL_PDX_BVxw`). Clone only voices you have permission to use.
8. **Confirm the GPU is actually used.** Watch Activity Monitor during generation. On one Apple Silicon build, a pinned CPU with an idle GPU meant the code had fallen back to CPU. Setting Torch to 8 threads helped, but speed stayed below real time (`9YzLI8-uF4s`). Single video.
9. **Read the weights license separately from the code license.** Breeze TTS 2 weights are non-commercial research use, which blocks most product use (`kJppefEh2ZA`). KittenTTS 2 weights are revocable and revenue-gated, unlike the Apache-2.0 original (`9YzLI8-uF4s`). Check whether a hosted API grants commercial rights to the weights or outputs.
10. **Give browser agents a snapshot, not pixels.** Take an accessibility snapshot with element references, act on the refs, and fall back to ARIA role, label or visible text when refs are unstable (`P7JrP57AxR0`). A numbered menu of interactive elements makes the same point (`OprnDByYVLQ`). If the agent must read its own screenshots, pick a multimodal model. The Agent Browser demo used a text-only model and the presenter said he would not repeat that (`P7JrP57AxR0`).
11. **Let the agent discover the CLI, then keep its checks.** Install the CLI globally, point the agent at the dev server port, and have it run the help command first. Ask it to save the session's steps as a bash regression test (`P7JrP57AxR0`).
12. **Gate and cap logged-in browser runs.** Use a throwaway account or a VM. Start with read-only tasks. Require a human to confirm purchases, sends and deletes, and cap steps per task (`OprnDByYVLQ`). Single video; the threat claims are not measured.
13. **Smoke-test dictation with a term-heavy passage.** Dictate the same passage into each tool, then score punctuation, sentence splits, and product, model and acronym names. The creator ran one pass per tool, so treat it as a smoke test (`ZRsDQp9CrXc`).

### Tools creators recommend

Tried in hands-on tests, with the caveats the creators gave.

- Voicebox: local cloning, TTS and Whisper dictation, with an MCP server and local REST API. Desktop install beat Docker on setup (`RL_PDX_BVxw`).
- Qwen Audio Agent: voice front end over ACP that hands coding work to Claude Code. Runtime is Apache 2.0, but the best voice path is a paid cloud API (`blpZ1xgFhCk`).
- TEN Framework with TEN Manager: graph-of-extensions voice runtime. Click any node to inspect data flow. Heavy for simple agents (`ES3HhoYCtIc`).
- VoxCPM2: about 2B TTS for speech, voice design and cloning. OpenAI-shaped server via vLLM. The creator said about 8 GB VRAM only covers running it (`O4TMwZlUJvQ`).
- Supertonic 3: 99M CPU TTS with a local OpenAI-compatible server. Good for local agents. Weak on numbers, and expression tags are paywalled (`pbsTTxKTuts`).
- Agent Browser (Vercel): Chromium-only CLI with accessibility refs. Simple to install, with no built-in agent loop (`P7JrP57AxR0`).
- Browser Use: a model picks actions from a numbered element menu. Metered tokens, and each step rereads the page (`OprnDByYVLQ`).
- Dograh: self-hosted voice agent platform with per-call transcript, trace and recording. Started with `docker compose up` (`xD9JEvfCH9k`).
- Handy: offline, MIT-licensed dictation with Silero VAD. Lets you choose the model by speed and accuracy (`ZRsDQp9CrXc`).
- Phonon 2: 164 MB local STT with a `phonon serve` OpenAI-compatible endpoint. Speed and accuracy claims are mostly vendor benchmarks (`eskgvQYchd0`).

### Where creators agree or clash with the conference talks

Agree:
- Barge-in and turn-taking decide perceived quality. The creators' tests match the turn-taking guidance above.
- A small, fast model should take the simple voice turns, with a stronger worker behind it. Qwen Audio Agent routes trivial questions away from the expensive agent (`blpZ1xgFhCk`).
- Browser agents should read a compact structure, not pixels (`P7JrP57AxR0`, `OprnDByYVLQ`). This matches the browser consensus above.
- Keyword and phrase biasing helps speech recognition. Creators found short phrases beat single words (`bavO_V80ohM`) and that hot words let you list names and terms for recognition (`eskgvQYchd0`). That creator did not report a before-and-after result.

Clash:
- **Latency measurement.** The conference talks give per-stage P95 budgets. The creators mostly report no latency numbers (`blpZ1xgFhCk`, `ES3HhoYCtIc`, `pbsTTxKTuts`). Their verdicts rest on single runs.
- **Frontier cascade vs local models.** The conference view is that a frontier cascade still wins in production. The local-first creators argue for small models on privacy and cost. Both sides say quality on hard text is the gate. The Voicebox host says ElevenLabs still wins on quality (`RL_PDX_BVxw`). The VoxCPM2 host's "80 percent replaceable" figure is his estimate, not a measurement (`O4TMwZlUJvQ`).
- **Is transcription solved?** One creator says yes (`blpZ1xgFhCk`). The conference treats ASR context and re-scoring as open work. The creators' own tests on technical terms show errors remain: Handy got most of the terms, not all (`ZRsDQp9CrXc`).
- **Safety in browser agents.** The conference focus is verification and judge calibration. Creators put prompt injection through a logged-in browser first (`OprnDByYVLQ`). Single video, not measured, and not covered in the conference sections above.

### Watch first

- `ES3HhoYCtIc`: the barge-in test as the first check on any voice stack, plus node-level debugging.
- `blpZ1xgFhCk`: the concurrency framing and the interruption state machine. Single video, no latency data.
- `O4TMwZlUJvQ`: the best trade-off section on self-hosting TTS.
- `pbsTTxKTuts`: the production-string test and where local TTS breaks.
- `OprnDByYVLQ`: a threat model for logged-in browser agents. Read it with the caveat that its claims are unmeasured.

## Watch first

- `hMlLw1LeIK8`: the clearest turn-taking and latency-budget walkthrough, with Pipecat demos.
- `vblnYHzBgS4`: five week-one failure modes with concrete targets and fixes.
- `MBHOH1NmDqc`: practical tricks to keep a frontier model fast (speculative ASR, background tools, TTS prefix cache).
- `fnLBmfsI_Fg` with `m24UKZomm7k`: small model plus state-machine harness. Short and directly reusable.
- `5xi_S1f9sDU`: the economics and step math of browser agents, with a refactor path.
- `xLxhT2ZI7UM`: why LLM judges lie, and a rubric-and-evidence verifier.
- `tyFPqtyOK5w`: neurosymbolic replay with healing and pass^k.
- `42Bz0TUfeOQ`: voice observability and audio-native evals (partly a pitch, but the instrumentation ideas transfer).

## Implications for our projects

**AgentOS (Govrix Scout, MemoryMesh, InferCraft, SkillForge)**
- *Proxy and budgets.* Add per-stage latency tracking with P95 for any voice or realtime route. Track time to first audio, not just tokens (`hMlLw1LeIK8`, `vblnYHzBgS4`).
- *Scheduler.* The 4-class priority scheduler fits voice: give interactive voice turns the top class with preemption, and send batch media to a flex class (`BcWFc3H7Khg`).
- *Routing.* Strategy routing can copy Tolan's cheap per-turn router that picks a model by stakes (`xLUQOqjudtA`). Also test the fast-responder plus async-thinker split (`65X0pQ6Lmbg`, `a8EcVumh71E`).
- *InferCraft.* Keep prompt prefixes stable and measure cache hit rate (`65X0pQ6Lmbg`). Static KV cache plus graph capture is relevant for audio decoders on the 5090 (`0jeZfjJMfmo`). Diffusion has no KV cache, so caching works at the step level (`gHs5ZiY80PM`).
- *MemoryMesh.* Use retrieval-style memory with nightly consolidation and conflict resolution (`xLUQOqjudtA`). Add provenance and time-grounded evidence for video or spatial memory (`mOf-PP4mVjA`, `Fe4aSMXsOZ4`).
- *SkillForge.* The teacher-doer loop that writes a skill file, with a binary success check, is a ready answer to the "success signal" question (`p7gaxmCUiIU`). Replay-as-code with healing is a candidate skill-worthiness test (`tyFPqtyOK5w`).
- *Crucible and exec-gate.* An action-risk classifier (authorization, reversibility, visibility, impact) fits the exec gate (`Cc0_nyxROBA`). Model proposes, harness decides (`m24UKZomm7k`).
- *Benchmarks.* The thesis of proving it with benchmarks matches the replay-baseline check and hierarchical confidence intervals (`CTLa_p6iOiY`).
- *Observability.* Map realtime events to one OTel-compatible schema, with a session ID on every span (`42Bz0TUfeOQ`).

- *Registry.* Catalogue per-site skill packs and WebMCP-style tool surfaces next to MCP servers (`GqoNrUz8hEU`, `ghJmWQCIHRM`, `LMbeDEQO6QM`). Note that clients rarely expose MCP resources (`LMbeDEQO6QM`).

**ProsHarness**
- *Checkpoint and resume.* Deterministic steps outside the model, with artifact-based success checks and bounded retries, map to resumable long runs (`5xi_S1f9sDU`, `tyFPqtyOK5w`).
- *Plan, critique, debate.* Use the plan-approval gate before costly execution (`pPj_tjlvYjA`). Use rubric-first verification for the critique step (`xLxhT2ZI7UM`).
- *Loops and schedules.* Scheduled sample runs with failure-triggered healing and a human-reviewed PR fit the schedule feature (`p7gaxmCUiIU`, `zTZ0qunQXnM`).
- *Phone approvals.* Act, confirm or stop thresholds, tuned by a cost function, can gate which actions need a phone approval (`Zd5b40Jbp_k`). The escalating attention ladder suits notifications (`OpY6MmZFeHo`).
- *Guardrail file.* Grow a single rules file from observed failures (`pyvRID_CZZU`).

**Recurring interests**
- *Cheap-model (Haiku) pipelines.* The small-model-plus-harness result is direct evidence (`fnLBmfsI_Fg`, `m24UKZomm7k`). Cheap models also write prompts for costly models (`BcWFc3H7Khg`). A small browsing model can be enough (`zTZ0qunQXnM`).
- *Entity resolution and data quality.* Context-conditioned ASR and re-scoring of short answers against a closed candidate list parallel candidate-constrained matching (`AN65uc645mE`, `IDNfAZVKvPE`). Ensembles of small judges with any-yes merge are a pattern for noisy labels (`dKcTBQzR7jI`).
- *Evals.* Calibrate every LLM judge against expert labels before trusting it (`xLxhT2ZI7UM`, `McknwOzbmyg`). Try to break each eval environment first (`ZSQb5fzRFPw`).
