# coding-agents — 489 videos

*Claude Code, Codex, Cursor, Devin etc. — how to use and build coding agents, IDE/CLI agents*

By channel: AI Engineer 138 · Kai Explains 16 · AI LABS 167 · Better Stack 168

**Synthesized guide:** [guides/coding-agents.md](../guides/coding-agents.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [Your AI Agent Starts Every Session Like a New Hire - Killian Carlsen-Phelan, Sonar](../videos/8vDzncmzxyg.md)
`8vDzncmzxyg` · AI Engineer · 2026-10-31 · q2 · practitioner · talk · also: testing-verification, context-engineering, security-guardrails

Sonar pitches Vortex, a plugin that gives coding agents project context before they write and runs deterministic checks on every edit, so issues are caught before PR review.

- Techniques: Pre-write context retrieval from a verifier; Per-edit plus end-of-turn verification hooks; Enforce on changed lines only, surface the rest; Explicit-permission rule for sensitive resources; Deterministic layer between AI reviews
- Tools: Sonar Vortex (Sonar's agent plugin, named in the talk), SonarQube (static analysis, CI scan, data-flow and security analysis), Sonar CLI and MCP clients, Claude Code, Codex, Antigravity, Guitar (Sonar's AI reviewer, named in the captions; the speaker did not cover it), Java (language guidelines used in the demo)

## [The Best Git Worktree Tool I've Used (Worktrunk)](../videos/mNo24Omj8X4.md)
`mNo24Omj8X4` · Better Stack · 2026-10-31 · q3 · practitioner · review · also: multi-agent, dev-tools

Review of Worktrunk (wt), a Rust CLI on top of git worktrees that adds per-branch switching, a multi-agent status view, one-command merge, copy-on-write cloning of ignored files, and per-worktree dev ports for parallel coding agents.

- Techniques: Worktree per parallel agent; One-screen status across agents; Shell integration before first use; Cheap clone of ignored dependencies and caches; Per-worktree dev server ports; Single-command merge back
- Tools: Worktrunk (wt, Rust CLI, MIT/Apache dual license, v0.81 as stated), Claude Code (native worktrees and its worktree-creation hook), Codex, OpenCode, Gemini CLI, git, Vibe Kanban (mentioned as a Kanban-board alternative), APFS (macOS copy-on-write filesystem), ext4 (Linux filesystem, full copies)

## [Why Docker Isn't Enough for AI Coding Agents (Openshell)](../videos/SbwckhZkPGs.md)
`SbwckhZkPGs` · Better Stack · 2026-10-29 · q4 · practitioner · review · also: sandboxing-execution, security-guardrails

Josh from Better Stack demos NVIDIA's open-source OpenShell agent sandbox, which adds per-request, per-binary policy, supervisor-side credential injection and audit logs on top of containers, then lists its caveats.

- Techniques: Default-deny egress with live, narrow allow rules; Bind network permissions to the calling binary; Supervisor-side credential injection; Check policy diffs with a solver before applying; macOS preflight for OpenShell
- Tools: OpenShell (NVIDIA, Apache 2.0, Rust, self-hosted; ~20k GitHub stars at time of video), openshell CLI (`openshell policy update`, `openshell logs`, sandbox status, doctor), Docker / Docker Desktop, Podman, Kubernetes, Firecracker, Apple container, Anthropic sandbox runtime, E2B, Daytona, Z3 SMT solver, Landlock (Linux kernel feature)

## [Your $200 ChatGPT Plan is now worth less!](../videos/P0i3vYuJZH8.md)
`P0i3vYuJZH8` · Kai Explains · 2026-10-29 · q4 · practitioner · review · also: token-cost-efficiency, governance-compliance

OpenAI halves the Codex allowance for grandfathered $200 Pro plans from Oct 30, 2026, and the undocumented 28-day reset run ends with it. The video works out per-model cost math and a checklist for what to do.

- Techniques: Convert a subscription allowance into API dollars; Weight cost by cache-read share; State the baseline when comparing a price change; Default cheap, escalate only on demonstrated failure; Keep your own log of allowance burn and resets
- Tools: OpenAI Codex (agentic coding system), ChatGPT Pro 200 / Pro 100 / Pro 500 / Plus plans, GPT-6 Astra (flagship), GPT-6.1 Sol, GPT-6.1 Terra, GPT-6 Sol, GPT-6 Luna, GPT-5.6 Sol, Claude Max 20x / Claude Pro (Anthropic), codexresets.com (community reset tracker), Artificial Analysis benchmark index (cost per task), SemiAnalysis (token-mix and allowance measurements)

## [How to Test Your Agents on Real Tasks With Harbor - Xander Song, Arize AI](../videos/kRJjSOYqW0I.md)
`kRJjSOYqW0I` · AI Engineer · 2026-10-27 · q4 · practitioner · talk · also: testing-verification, evals, observability

Xander Song (Arize) introduces Harbor, an open-source framework for testing agents on real tasks in fresh sandboxes, scored by side-effect verifiers, and shows how his team used it to tune a prompt for SQL over GraphQL.

- Techniques: Harbor task layout; Oracle-first validation; Keep verifiers outside the agent's view; Synthetic task and oracle generation; Before/after prompt A/B in a fixed harness; Read-only SQL tool for aggregates; Single-node app snapshot in Docker; One-turn skill-triggering test
- Tools: Harbor, Docker, Arize Phoenix, OpenInference, OpenTelemetry, OTLP, ATIF (Agent Trajectory Interchange Format), Daytona, Modal, E2B, SQLite, Postgres

## [EGM: Google's New Way To Use Claude Code Is Insane](../videos/xxf6D9jynFw.md)
`xxf6D9jynFw` · AI LABS · 2026-10-26 · q2 · practitioner · tutorial · also: context-engineering, multi-agent, claude-code

Walkthrough of Google's EGM, a spec-first workflow where zero-context goldfish sub-agents critique a plan before any code is written, with install, bootstrap, review and drift steps for Claude Code. A sponsor segment caps quality.

- Techniques: Isolated-context plan critique; Multi-lens rubric reviewers; Fan-out with a single merged report; Staged plan authoring with per-section approval; Round-based review gate; Drift check against per-folder docs; Make per-folder docs agent-readable; Verify the installer's CLAUDE.md edits; Install by agent-specific command or by prompt; Command sequence
- Tools: EGM (Google Elephant Goldfish Model, free on Google's GitHub), Claude Code, Codex (named as a supported agent), Hydra (sponsor, video generation for app promos)

## [Why Rust Is The New GOAT For AI](../videos/R-tLX37Xgx8.md)
`R-tLX37Xgx8` · Better Stack · 2026-10-24 · q3 · intro · other · also: dev-tools, infra-cost-scaling

Better Stack argues Rust is taking over AI tooling: memory safety, no GC pauses, and single native binaries, with GitHub Copilot, Codex CLI and Bun as examples. Mostly company anecdotes.

- Techniques: Rust core behind a Python API; Ship a native library instead of a helper process; Feed compiler errors back into the agent loop; Ownership-based memory for latency-critical services
- Tools: Rust, Cargo, GitHub Copilot, Copilot SDK, Bun, Zig, Claude Code, Codex CLI, Node.js, TypeScript, Go, Python

## [The Best Agent IDE I've ever used (Orca)](../videos/8QgBcI40VC8.md)
`8QgBcI40VC8` · Better Stack · 2026-10-24 · q3 · intro · review · also: multi-agent, dev-tools

Walkthrough of Orca, a free open-source desktop app that runs Claude Code, Codex and other coding CLIs side by side with per-task git worktrees, a browser with element annotation, and multi-agent orchestration.

- Techniques: Worktree-per-task agent launch; Element-annotated fix requests from an embedded browser; Forced multi-provider split for comparison; Run the orca CLI from the terminal
- Tools: Orca, Claude Code, Codex, Goose, Kimi (transcript says 'kimmy'), Cursor, Herdr (transcript says 'Herder'), Ghostty (transcript says 'Ghosty'), GitHub, Linear, caffeinate, Apple Design skill (named in demo, source not stated)

## [Better AI Models Won't Fix Your Engineering Team — Nicholas Arcolano, Jellyfish](../videos/Ve2bAarPA2I.md)
`Ve2bAarPA2I` · AI Engineer · 2026-10-23 · q4 · practitioner · talk · also: enterprise-adoption, token-cost-efficiency

Jellyfish data from ~50k engineers: switching AI models or tools barely moves merged PRs, while skill use, token volume, company and individual engineer effects explain far more.

- Techniques: Natural experiment from a vendor-driven shock; Within-engineer switch comparison; Variance decomposition of throughput; Skill-use level bins over time; Percentile binning of consumption against output; Longitudinal rank-stability check
- Tools: Cursor, Claude Code, Grok, Opus, Sonnet, ChatGPT, Artificial Analysis (model benchmark charts), Jellyfish (engineering telemetry platform)

## [AI Just Made Physics Interactive. This Is Insane. (Anatomy)](../videos/lyGYidIZK4I.md)
`lyGYidIZK4I` · Better Stack · 2026-10-22 · q3 · practitioner · review · also: skills-self-improvement, claude-code, token-cost-efficiency

Better Stack demos "anatomy", an agent skill that explains concepts as physical machines in interactive HTML/SVG/React figures; useful, but very slow, token-hungry, and its metaphors need checking.

- Techniques: Install and invoke the anatomy skill; Truth-first figure generation; Steering the output with modifiers; Verify the metaphor and the draft; Budget before running
- Tools: anatomy (Claude skill, tool name as spoken in the video), skills CLI, Claude Code, Codex, OpenCode, Antigravity, Chrome, WebGL, React, SVG, Mermaid, D2

## [A Bank Built Its Own Coding Agent. It Took Off — Felippe Felisola Caso & Francesco Galletta, Monzo](../videos/adfw3xJBx1o.md)
`adfw3xJBx1o` · AI Engineer · 2026-10-21 · q3 · practitioner · talk · also: enterprise-adoption, mcp-and-tools, sandboxing-execution

Monzo's engineers describe Agent Chip, an in-house coding agent that began as a viral Slack emoji trigger and grew into a sandboxed, MCP-gated platform building block.

- Techniques: Gateway-first MCP layer for internal tools; Isolated sandbox namespace for remote agents; Separate orchestrator from execution; Emoji-reaction prompt trigger in chat; Low-signal incident mode; Proactive impact checks on backend changes
- Tools: Agent Chip (Monzo's in-house coding agent), Slack, GitHub, Linear, MCP (internal MCP gateway server)

## [Is the Agent Harness Dead? — Jediah Katz, SpaceXAI](../videos/7Y4sbZgBdnc.md)
`7Y4sbZgBdnc` · AI Engineer · 2026-10-20 · q4 · practitioner · talk · also: agent-architecture, context-engineering, token-cost-efficiency

Jediah Katz (SpaceXAI, formerly Cursor's harness lead) argues the agent harness is not dead: smarter models absorb coding scaffolding, but the harness keeps unlocking new frontiers, handles runtime, trust, and cost, and is moving toward agents as building blocks.

- Techniques: Two-layer harness split; Shim registry with a removal bot; Event subscription primitive; Nudge guardrails for responsiveness; Efficiency tuning levers
- Tools: Cursor, Cursor Agent Harness, GrokBot, Grind Swarm, Rollouts, Claude Code, Pi, Codex, SWE-bench Lite, MLE-bench

## [Google Just Fixed AI Design By Releasing This](../videos/au2TI8sdq8E.md)
`au2TI8sdq8E` · AI LABS · 2026-10-19 · q3 · practitioner · tutorial · also: context-engineering, skills-self-improvement, testing-verification

Google's Stitch design tool now has a terminal CLI, so Claude Code can drive it through a brief-to-design-to-site workflow with review and story-review skills; the video is a tutorial-style walkthrough with a sponsor segment.

- Techniques: Stitch CLI install with the skill in .claude; brief.md interview before any design generation; Loop of generate, check, and re-prompt in Stitch; Build from Stitch via download of HTML, images and fonts; Two-stage review: design fidelity, then story quality
- Tools: Stitch (Google), Stitch CLI, Claude Code, Stitch skill, scrollytelling skill, design.md, brief.md, Whisperflow (sponsor)

## [AI Is Merging Video Games Now (here's how)](../videos/9dDJq1LGBAw.md)
`9dDJq1LGBAw` · Better Stack · 2026-10-19 · q3 · intro · review · also: skills-self-improvement, multi-agent, token-cost-efficiency

Better Stack demos Universal Modder, an open-source Claude Code plugin that builds GTA 5 mods from games you own via recon, hot reload, in-game testing and shared field notes; ~$68 API cost.

- Techniques: Back up and log before touching user state; Fingerprint before coding; Parallel narrow research sub-agents; Write a converter for proprietary asset formats; Hot-reload the logic, not the host; Screenshot check after each reload; Draw new content as a post-process overlay; Field note plus shared KB PR
- Tools: Universal Modder (Rayhan; open-source Claude Code plugin with skills, a CLI and a knowledge base), Claude Code, Claude Opus 5.5 (as stated in the video), Script Hook 5 (GTA 5 script loader), ReShade, FAL (image generation for sprites, textures, 3D models, sound and voice; made by an ex-FAL engineer per the host), OpenCode (wrote KB notes), Steam (game library)

## [6 Insane Trending GitHub AI Design Repos You Need to Use](../videos/NZjjmf3I6I4.md)
`NZjjmf3I6I4` · AI LABS · 2026-10-19 · q2 · practitioner · review · also: skills-self-improvement, mcp-and-tools, multi-agent

Walkthrough of six GitHub repos that give coding agents design references, multi-viewport checks, design-token extraction, multi-agent page builds, app-store screenshots and launch-video generation. Mostly sponsored tool demos with little measurement.

- Techniques: Reference-first design with an awards MCP; Post-build responsive check with Responsively MCP; Design taste skills, chosen by scope; Extract and diff design tokens with Dembrandt; Generate app-store screenshots with a local editor project; Launch video with Brag, with a verification pass
- Tools: Awards MCP (awards setup and awards inspiration commands), Klein CLI (caption spelling; probably Cline), sponsor, Kleinpass (caption spelling; probably ClinePass), sponsor, open-weight model access, first-month discount link, Whisperflow landing page (probably Wispr Flow, used as a reference site), Butter.Video (animation reference site), Responsively (Mac app and MCP server), Genjutsu skills: Cast, Paint, Bunshin, taste skill and hallmark (previously covered by the channel), Dembrandt (skill, design.md output), App store screenshots skill and local editor, Brag / Bragg (brag command, Full Mode and Slim Mode), Hyperframes (video framework used by Brag Full Mode)

## [Teach Your Agent to Prove It's Done — Nick Nisi & Zack Proser, WorkOS](../videos/q4WC4TowkBo.md)
`q4WC4TowkBo` · AI Engineer · 2026-10-18 · q3 · practitioner · workshop · also: testing-verification, evals, context-engineering

Build deterministic verifier CLIs and evidence "receipts" so coding agents can prove their own work is done, closing the loop without the human reading every line of code.

- Techniques: Per-app verifier CLI with subcommands; Deterministic end-to-end prove step with Playwright; System-one LLM judge for fuzzy outcomes; Doctor/preflight plus stale-proof detection; Centralized verifier gate on workflow nodes (CTX); Babysitter agent for PR follow-through; Generate many variants and select via eval; Saboteur/detective bug-injection test of the verifier; Evidence attached to PRs; Outcome-first prompting with clear stop conditions; Error messages written for agents; Post-deploy monitoring agent
- Tools: Playwright, Chrome DevTools, pnpm, GitHub CLI (gh), GitHub API, Cloudflare Workers, MCP, Reptile, CodeRabbit, Datadog, Claude Code, Pi

## [Tokens Are the Cheap Part — Steve Jamison, Jellyfish](../videos/U7ZYBCcdJPg.md)
`U7ZYBCcdJPg` · AI Engineer · 2026-10-14 · q4 · practitioner · talk · also: governance-compliance, token-cost-efficiency, enterprise-adoption

Steve Jamison (Jellyfish) argues AI tokens are a small share of PR cost; tracking total intelligence cost per merged PR, with revert rates as a counterweight, beats watching the token bill alone.

- Techniques: Blended cost per merged PR; Token-spend quintile cohorts; Within-developer baseline comparison; Counterweight metrics beside throughput

## [Please… Enough with the Sloppy, One-Shot SaaS Replacements — Mahmoud Abdelwahab, Railway](../videos/oixzVKMAXG0.md)
`oixzVKMAXG0` · AI Engineer · 2026-10-13 · q3 · practitioner · talk · also: product-ux, testing-verification, skills-self-improvement

Railway's Mahmoud Abdelwahab on why agent-built internal tools feel broken: agents skip product polish (autosave, optimistic updates, undo, URL state) unless asked, so encode taste in skills, reference existing pages, and force end-to-end verification.

- Techniques: Pattern-following via existing abstractions; Named UX patterns as explicit asks; Reference-page anchoring; Taste packaged as skills; End-to-end verification loop
- Tools: Railway, Payload CMS, TanStack, Claude Code

## [Build with Perception Agents — Emile Baizel & Shruti Arora, Amazon AGI Lab](../videos/ZGzthw4BZiA.md)
`ZGzthw4BZiA` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: voice-multimodal, testing-verification, mcp-and-tools

Amazon AGI Lab hands-on workshop on Nova Act's open-sourced perception primitives: point-and-annotate a live page into JSON, run Gherkin-based visual verification, and wire both to a coding agent.

- Techniques: Deterministic visual annotation to JSON; Gherkin user flows auto-generated from a surface crawl; Browser extension to coding agent bridge; Automatic verification after every agent change; Voice or wearable transcript as an annotation source
- Tools: Amazon Nova Act, Nova Act SDK, Nova Act MCP server, Visual Annotator (Chrome extension), Visual verification skill, Claude Code, Kiro, Gherkin, Chrome, uv / uvx, Jam MCP, Atlassian MCP

## [Everything is Open Source Now (Reverse Engineer Anything)](../videos/jtfpCGsbSJU.md)
`jtfpCGsbSJU` · Better Stack · 2026-10-12 · q3 · intro · news · also: software-factory, testing-verification

Better Stack commentary on Artcraft, a viral open-source Adobe clone, and a "reverse engineer anything" MCP; the host tests Opus 5.5 rebuilding a 1990s pinball game in Rust with sub-agents and verification passes.

- Techniques: Reference-driven port with source-address traceability; Fresh-context verification pass after a fan-out; Verifiable-goal loop (test suite as the spec); Clean-room rebuild from public specs and observed behavior
- Tools: Artcraft, Photocraft, Vectorcraft, Filmcraft, Adobe Photoshop, Reverse Engineer Anything (MCP, GitHub), Hopper, Ghidra (transcribed as 'Geirdre'), IDA, Claude Opus 5.5, Rust, Pinball Space Cadet (original EXE from Internet Archive)

## [Burn Your Flags: Interactive CLIs for Agents — Mark Lummus & Navinkumar Patil, PayPal](../videos/aV_vgUSatqs.md)
`aV_vgUSatqs` · AI Engineer · 2026-10-12 · q3 · intro · workshop · also: mcp-and-tools, context-engineering

PayPal's developer tools leads run a live workshop where attendees make a coffee-ordering CLI work for agents. Main point: interactive prompts fail silently under agents, so CLIs need machine-readable side channels, injected context, and determinism.

- Techniques: Side-channel JSON interface for CLIs; Tmux driver for interactive CLIs; Context injection via a single input file; Deterministic CLI, reasoning outside; Have an agent build the solver
- Tools: tmux, Claude Code, Codex, Claude Agent SDK, Opus 4.8, Slack

## [This Open-Source Engine Claims 2x Faster Than llama.cpp](../videos/90itFOj7jfo.md)
`90itFOj7jfo` · Better Stack · 2026-10-12 · q3 · practitioner · review · also: local-ai, inference-serving

Hands-on test of Magnitude, a new Rust inference engine for Apple Silicon that tunes kernels per machine and targets agent workloads; the "2x llama.cpp" claim holds for one decode config but is mixed in independent tests.

- Techniques: Benchmark decode and prefill separately, and match KV-cache precision; Per-device kernel autotuning, cached per machine; Point Claude Code at a local Anthropic-compatible endpoint; Agent-serving cache and memory policy
- Tools: Magnitude (v0.2.5), llama.cpp, MLX, Ollama, Qwen 3.5 4B (Q8), Qwen 3.6 35B A3B (4-bit), Seismic (numerical compiler), Claude Code, Codex, OpenCode, RapidMLX, vLLM

## [Continuously Improving Agents with Langfuse — Annabell Schäfer & Lotte Verheyden, ClickHouse](../videos/BOCjybvJYM4.md)
`BOCjybvJYM4` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: observability, evals

Hands-on Langfuse workshop on monitoring agents in production: instrument traces, write failure-mode evaluators (LLM-judge and code) on live traces, then use a coding agent over trace data to find silent failures.

- Techniques: Failure-mode-first evaluator set; JSON-path variable mapping for LLM judges; Boolean code evaluators on live observations; Coding agent as trace analyst; Coverage monitoring
- Tools: Langfuse, OpenAI Agents SDK, OpenAI API, Codex, Claude Code, TypeScript, Python

## [Let Your Agent Cook: Using Skills to Evaluate and Improve Your App — Ankur Duggal, Arize AI](../videos/_zUp6y9bDU8.md)
`_zUp6y9bDU8` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: evals, observability, skills-self-improvement

Arize's Ankur Duggal argues agents need trace-based evals, then demos a coding agent (Claude Code plus Arize skills) turning production traces into failure analysis, datasets, evaluators and experiments.

- Techniques: Trace-to-dataset-to-experiment loop; Coding agent as eval workflow driver; Mixed evaluator set; Sampled online evals; Tailored evals from observed failures
- Tools: Arize AX, Phoenix, Claude Code, Codex, Cursor

## [How to Build Quality Gates into Agentic Coding Workflows — Nnenna Ndukwe, Qodo AI](../videos/-AKPRSYccJc.md)
`-AKPRSYccJc` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: pr-code-review, context-engineering, testing-verification

Hands-on workshop by a Qodo DevRel on wiring codified rules, skills, structured plans and deterministic gates into an agentic coding loop from planning through PR review and autofix.

- Techniques: Codified rules and skills pulled per phase; Structured high-level plan plus execution plan; Read-only plan mode with an explicit skill handoff; Local verification command as the gate; Audit skills during implementation; Review-findings autofix loop; Severity-tiered rules with merge blocking
- Tools: Qodo, Claude Code, Codex, Semgrep, Ruff, Pyright, Bandit, pytest, GitHub CLI, uv, conventional commits, git worktrees

## [Don't Buy a RTX Spark Laptop For Local AI Until You See This](../videos/aQKGejbv-Rs.md)
`aQKGejbv-Rs` · Kai Explains · 2026-10-12 · q4 · practitioner · review · also: local-ai, inference-serving

Pre-review critique of the RTX Spark / Surface Laptop Ultra for local AI: the cold-prefill wait on long prompts (about 170 s at 128K) matters more for agent work than decode speed, and the wattage is still unpublished.

- Techniques: Cold prefill benchmark at real context length; Split throughput into prefill and decode; Sustained and battery soak test; Memory budget with OS and tooling headroom; Speculative decoding for decode speed; Keep the prompt cache warm in long sessions
- Tools: Microsoft Surface Laptop Ultra, NVIDIA RTX Spark N1X, NVIDIA DGX Spark, Surface RTX Spark Dev Box, MAI Code 1.1 Flash (Microsoft coding model, 137B total / 6.8B active MoE, about 53 GB compressed), llama.cpp (Windows on ARM build with CUDA; transcribed as 'Lama CPP'), DFlash 2 speculative decoding (transcribed as 'DF Flash 2'), GitHub Copilot, Windows 11, NVIDIA Linux (DGX Spark), AMD Ryzen AI Max Plus 395, ASUS ROG Flow Z13

## [SonarQube + OpenAI: Agentic Development — Killian Carlsen-Phelan, Sonar](../videos/bI8WyG9YB0I.md)
`bI8WyG9YB0I` · AI Engineer · 2026-10-12 · q3 · practitioner · demo · also: testing-verification, security-guardrails, context-engineering

A Codex deployment engineer and a Sonar developer advocate argue that agent "done" needs evidence, containment is not correctness, and feedback checks belong inside the agent loop, then demo SonarQube hooks, MCP and CLI wired into Codex.

- Techniques: Evidence-backed definition of done; Layered execution and artifact controls; Secret-blocking lifecycle hook; Guide, verify, solve loop (ACDC); Taint analysis across files; Changed-code-only verification for agent edits; Custom rules targeting agent-written code
- Tools: Codex (OpenAI coding agent CLI), SonarQube Cloud, SonarQube CLI, SonarQube MCP server, SonarQube Codex plugin / marketplace, Docker, Git Bash (for setup script)

## [From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases](../videos/YIxzNZDDy1A.md)
`YIxzNZDDy1A` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: evals, observability, sandboxing-execution

Wolfram Ravenwolf's hands-on workshop on building a reproducible agent benchmark (Terminal-Bench via Harbor, WolfBench dashboard), arguing that one averaged score hides variance, cost and configuration choices.

- Techniques: Multi-metric leaderboard per configuration; Pin the harness and keep a fork; Sandbox per trial with bounded concurrency; Smoke-test one task before the full run; Explicit retry policy by error class; Set and record every sampling and agent setting; Trace-first debugging of surprising scores; Shareable result snapshot
- Tools: Harbor, Terminal-Bench 2.0, Terminus 2, Weights & Biases Weave, WolfBench, Inspect (UK AISI), Marimo, CoreWeave serverless sandboxes, Daytona, OpenRouter, Docker, uv

## [Sandboxes Aren't Optional: 4 Ways to Isolate Coding Agents — Robert Brennan, OpenHands](../videos/iH_wV8BbS24.md)
`iH_wV8BbS24` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: sandboxing-execution, security-guardrails, infra-cost-scaling

Robert Brennan (OpenHands CEO) compares four ways to sandbox coding agents, from Docker on a laptop to one Kubernetes pod per session, and argues least privilege should set the blast radius.

- Techniques: Container per agent conversation with selective mounts; Least-privilege sandbox spec; Ephemeral pod per agent session; Event- or schedule-triggered cloud agents; Matching environment to job
- Tools: OpenHands, OpenHands Agent Canvas, Claude Code, Codex, Docker, Kubernetes, GitHub Actions, Cursor, GitHub Copilot, Twilio, Slack, Datadog

## [AI Security Engineer Foundations + Certificate — Javier Garza, Snyk](../videos/ZyC56eV8sVw.md)
`ZyC56eV8sVw` · AI Engineer · 2026-10-12 · q2 · intro · workshop · also: security-guardrails, mcp-and-tools, governance-compliance

A two-hour Snyk workshop on AI security basics: OWASP LLM Top 10, shadow AI and AI bills of materials, AI threat modeling, MCP and skill supply-chain risk, and secure-by-default coding hooks.

- Techniques: Treat LLM input and output as untrusted data; Read-only database views for agents; Approval gate for high-risk actions; Full action logging plus a background log scanner; Scan-fix-rescan agent hook; Pre-install scanning of MCP servers and skills; AI-BOM inventory with query by component; Security requirements inside the prompt
- Tools: Snyk agent-scan (MCP and tool scanner), Snyk AI-BOM (CycloneDX-style inventory), Gandalf (Lakera) prompt-injection game, Claude Code, Cursor, Windsurf, OpenClaw, CycloneDX, SPDX, STRIDE, MITRE ATLAS, uvx

## [From Your Laptop to the Pipeline: Scaling Custom Agents with GitHub Copilot](../videos/b9UhZkKjX_A.md)
`b9UhZkKjX_A` · AI Engineer · 2026-10-11 · q2 · intro · talk · also: software-factory, observability, multi-agent

GitHub's Jose Palafox walks through the Copilot agent surfaces: local agents you steer, reusable shared agents, cross-repo orchestration, and headless agents in CI that get cost and trace visibility through OTel.

- Techniques: Headless one-shot agent in CI; Slash-command phase gates on issues; Scaffold agents from a one-line description; Marketplace or private-repo distribution; Orchestrate: issues as goals, agents per repo; Cross-model plan audit; Small-model codebase explorer; OTel per-agent cost monitoring
- Tools: GitHub Copilot CLI, GitHub Copilot SDK, GitHub Actions, GitHub Agentic Workflows, Awesome Copilot, OpenTelemetry, Slack, Microsoft Teams

## [Building on the Codex Harness — Dominik Kundel, OpenAI](../videos/9WiBJRO84yY.md)
`9WiBJRO84yY` · AI Engineer · 2026-10-10 · q3 · practitioner · talk · also: agent-architecture, mcp-and-tools, context-engineering

OpenAI's Dominik Kundel shows how to build your own client on the open-source Codex app server, the JSON-RPC protocol that wraps the Codex harness, and gives three rules for customizing it safely.

- Techniques: Append developer instructions instead of replacing the system prompt; Deferred dynamic tools with tool search; Pin and bundle the harness binary; Per-thread config overrides; Integrate by delegating to the coding agent; Choose exec or app server by parallelism and interactivity
- Tools: Codex app server, Codex CLI, Codex exec, Codex desktop app, Python SDK (Codex), Agent Client Protocol (ACP), LM Studio, Ollama, Electron, Cloudflare Doom WASM renderer, T3 Code, Claude Code Codex plugin

## [Stop Prompting — Greg Pstrucha, Sentry](../videos/E3KbFLAGD6A.md)
`E3KbFLAGD6A` · AI Engineer · 2026-10-10 · q3 · practitioner · talk · also: context-engineering, testing-verification, pr-code-review

Sentry's Greg Pstrucha argues teams should stop re-prompting coding agents and instead codify repeated conventions as deterministic lint rules, skills checks, and policy-driven review loops.

- Techniques: Mine feedback to find lint-worthy rules; Custom AST lint rules with ast-grep or ESLint-style tools; Lint for schema sync; Validate code examples inside skill documents; Policy files plus per-policy sub-agent review loop; Hooks to run deterministic checks at the right moment
- Tools: ast-grep, ESLint, OxLint, Flake8, Clippy, Claude Code skills, OpenAPI schema, Django REST Framework, a plain-English lint tool transcribed as 'TaskLessware' (name uncertain from auto-captions)

## [Designing CLIs for Agents, Not Humans — Pedro Lopez, Airbyte](../videos/3wj6sgbi1YA.md)
`3wj6sgbi1YA` · AI Engineer · 2026-10-10 · q3 · practitioner · talk · also: mcp-and-tools, security-guardrails

Airbyte's Pedro Lopez on building a thin MCP server and CLI for agents: a small tool surface, OAuth-only auth, JSON in and out, non-interactive credentials, and skills shipped with the CLI.

- Techniques: Thin interface over a shared API spec; Minimal tool surface with progressive discovery; OAuth-first MCP auth with a connect-link flow for third-party credentials; Agent-friendly CLI contract; Ship a skill with the CLI, with progressive references; Use failure patterns as a design signal
- Tools: MCP, CLI, OAuth, OpenAPI, jq, Claude Desktop, Claude custom connectors, ChatGPT app store, Airbyte AI Agents context store, Zendesk, Stripe, HubSpot

## [We Mapped 115 Microservices for Our Coding Agents — Kamalakannan Nandagopal, Postman](../videos/k2ClBT4aqAg.md)
`k2ClBT4aqAg` · AI Engineer · 2026-10-09 · q4 · practitioner · talk · also: context-engineering, evals

Postman's engineer describes an API context graph over 115+ microservices, grounded in code and telemetry, that improves coding-agent answers on API discovery, shape analysis and impact assessment, with a token-efficiency gain and a staleness warning.

- Techniques: Code- and telemetry-grounded API context graph; Retrospective PR-based eval with quality-vs-tokens plot; Context layer exposed as a skill next to a generic coding agent; Treat graph staleness as an eval regression; Run expensive architecture checks cheaper and earlier
- Tools: Postman API context graph, Claude Code, GitHub code search, Postman AI agent

## [Your AI Agent Has No Nervous System — Matt Gibiec, Dynatrace](../videos/YNT7Plf9KIg.md)
`YNT7Plf9KIg` · AI Engineer · 2026-10-09 · q2 · intro · talk · also: observability, context-engineering

Vendor pitch for Dynatrace's "Blue Box" agent, which argues AI coding agents need live environment context (service dependencies, production telemetry, change history) to avoid hallucinated or breaking changes.

- Techniques: Dependency-mapped local testing; Baseline-deviation alerts to the coding agent; Change-correlated incident triage; Context-scoped fix suggestion with human approval
- Tools: Dynatrace Blue Box

## [Cooking with Codex — Charlie Guo & Gabriel Chua, OpenAI](../videos/FwiS44-xyYw.md)
`FwiS44-xyYw` · AI Engineer · 2026-10-06 · q3 · practitioner · workshop · also: multi-agent, context-engineering, software-factory

OpenAI's hands-on Codex workshop walks through context, computer use, long-running goals, subagents, hooks and automations, then shows the app server for embedding Codex in your own product.

- Techniques: Verifiable goal with milestone files; Milestone-triggered review and goal-audit threads; Side-thread unblock and status query; Subagent vs thread handoff split; Hook-based deterministic guardrails; Heartbeat automation for external waits; Scheduled triage that spawns worktree threads to PRs; Choosing a control surface: computer use vs Chrome extension vs in-app browser; Embedding via the App Server protocol
- Tools: Codex app, Codex CLI, Codex remote (ChatGPT mobile), Codex Chrome extension, Codex computer use, Codex in-app browser, Agents SDK, Sites, Chronicle (research preview, Pro), AppShots (screenshot with embedded text), AGENTS.md, config.toml hooks

## [Advanced Workshop: Mastering AI Observability — Doug Guthrie, Braintrust](../videos/hfEczxdNyvU.md)
`hfEczxdNyvU` · AI Engineer · 2026-10-06 · q3 · practitioner · workshop · also: observability, evals

Braintrust workshop on AI observability: trace agents, score production traffic with judges and topics, and let a coding agent run the eval-and-fix flywheel through the Braintrust CLI.

- Techniques: Binary, harsh LLM judges with examples in the prompt; Human-calibrated judges; Scores defined in code and pushed to the platform; Automation rules with scope and sampling for online scoring; Topic windows and filters for long conversations; Coding agent as flywheel operator; Service account for the analysis loop; Remote eval exposed to a playground; Mutable spans for attaching scores later
- Tools: Braintrust, Braintrust CLI (bt), OpenAI Agents SDK, Codex, Claude Code, Cursor, OpenCode, uv, GitHub Actions, Modal, ClickHouse, Brainstore

## [Build the Right Thing: Product Engineering (Part 1) — Kent C. Dodds, EpicProduct.engineer](../videos/_fHTqOs5wQA.md)
`_fHTqOs5wQA` · AI Engineer · 2026-10-06 · q3 · intro · workshop · also: product-ux

Kent C. Dodds argues that once agents level implementation, the durable engineering skill is deciding what to build, using Mom Test-style validation and smallest-slice thinking. Part 1 of a workshop, mostly framing.

- Techniques: Mom Test customer interviews; Ask what the problem costs; Smallest slice / minimal demonstrable solution; Throwaway prototype, then rebuild with agents; Check the neighbors before building; Build the agent playground
- Tools: Slido, Cursor, OpenCode, Claude (captioned as 'cloud')

## [Lifestyles of the AI-Native — Nick Nisi & Zack Proser, WorkOS](../videos/AgBAOXVxt4A.md)
`AgBAOXVxt4A` · AI Engineer · 2026-10-06 · q3 · practitioner · workshop · also: claude-code, testing-verification, context-engineering

WorkOS engineers run a hands-on workshop on operating fleets of Claude Code agents: voice dictation, goal vs loop, verification hooks, Codex adversarial review, worktrees and scheduled tasks.

- Techniques: Goal with a measurable done condition; Loop for recurring or open-ended monitoring; Checksum-verified evidence of test runs; Hook-enforced gates; Cross-model adversarial review; Retrospective agent with curated memory; State machine for ordered steps; Git worktrees for parallel agents; Interactive first, then schedule; Session fleet management; Triage automated PR review output by score
- Tools: Claude Code, Codex CLI, Handy, WhisperFlow, Granola, Greptile, CodeRabbit, Devin, Linear, Slack, tmux, Fleet (nicknesey/fleet)

## [Agentic Search vs Vector Search for Coding Agents: We Ran the Eval — Braintrust](../videos/T3SS931wU0I.md)
`T3SS931wU0I` · AI Engineer · 2026-10-06 · q3 · practitioner · talk · also: rag-retrieval, evals

Braintrust dev-rel walks through a small eval comparing agentic search (grep/find/cat in Claude Code) with vector search for finding bugs in the TypeScript Go repo: equal accuracy, but vector cost 4x more.

- Techniques: Eval composition: dataset, task, scorer, experiment; Production-log sampling into a dataset; Mining bug-fix PRs as coding-agent eval tasks; Binary scoring from the repo's own test suite; Forcing a retrieval strategy in a coding agent; Propagating parent span IDs to subprocess agents
- Tools: Braintrust (evals, tracing, UI, CLI, MCP server), Claude Code (agent harness, disallowed-tools flag), grep, find, ls, cat, bash (agentic search tools), Vector database (unnamed in the talk), Microsoft TypeScript Go repo and its test suite (dataset and scorer), Cursor semantic search post (cited as motivation)

## [AI Coding Agents Are Breaking Big Codebases — Dan Adler, Sourcegraph](../videos/Bdrs3uAX0_M.md)
`Bdrs3uAX0_M` · AI Engineer · 2026-10-05 · q3 · practitioner · talk · also: software-factory, context-engineering, rag-retrieval

Sourcegraph CEO Dan Adler argues that large, decades-old codebases are decaying under the flood of AI-written code, and that agents need code-graph and search infrastructure to see and change them across thousands of repos.

- Techniques: Deterministic scripts for mechanical sweep changes; Hybrid agent and script batch change loop; Code-graph plus search as agent context; Coverage audit for sweeping changes
- Tools: Sourcegraph, agentic batch changes, Claude Code, Codex, Cursor

## [GLM-5.2: Open Weights, Near-Frontier Intelligence — Zixuan Li, Z.ai](../videos/9JFGohx4E7U.md)
`9JFGohx4E7U` · AI Engineer · 2026-10-04 · q2 · intro · keynote · also: models-research, training-finetuning-rl

Z.ai's Zixuan Li introduces GLM 5.2, an open-weight model he says is near frontier on coding and agentic tasks, and explains why Z.ai opens its weights, plus its Zcode harness.

- Techniques: Open-weight release for on-premise deployment; Vertical fine-tuning on an open base model; Tiered thinking budget; Own harness with bring-your-own-key and compaction
- Tools: GLM-5.2, Zcode, Hugging Face, Codex, Claude Code, OpenCode, Terminal Bench 2.1, Artificial Analysis Intelligence Index

## [Orchestras, Not Factories: How the Fastest Builders Work — Charlie Holtz, Conductor](../videos/TRfzFJCJ7ZE.md)
`TRfzFJCJ7ZE` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: multi-agent, software-factory, sandboxing-execution

Charlie Holtz (Conductor co-founder) lists six principles for fast agent-driven building: stay near the frontier, don't beat the market, mark slot-free zones, feed a central store, run free-range cloud agents, and orchestrate rather than run a factory.

- Techniques: Don't-beat-the-market test; Slot-free zones with CI-enforced human review; CLAUDE.md / AGENTS.md and skills as onboarding material; Central event store with a SQL tool for agents; Cloud sandboxes per task with lifecycle independent of the laptop; Agents calling the product API to create work
- Tools: Conductor, Claude Code, Codex, git worktrees, Postgres, Slack, Discord, Telegram, OpenClaw, React

## [Your Coding Agent Is 6 Months Out of Date — Jakub Hojsan, Exa](../videos/cKhpeEBnT1o.md)
`cKhpeEBnT1o` · AI Engineer · 2026-10-04 · q2 · practitioner · talk · also: rag-retrieval, mcp-and-tools

Exa's forward-deployed engineer explains why coding agents miss recent changes past their model cutoff, and how query-targeted web search snippets, plus explicit search rules, close that gap. Partly a product pitch.

- Techniques: Two-part search instructions for agents; Query-targeted highlight extraction; Full retrieval trace logging; Natural-language schema for structured output
- Tools: Exa search API, Exa Agent, MCP server, Claude Code, CodeRabbit, Cursor

## [Stop Rationing Tokens: Let the Harness Pick the Model — Kimchi by Cast AI](../videos/48YUYDjwfYY.md)
`48YUYDjwfYY` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: token-cost-efficiency, infra-cost-scaling, sandboxing-execution

Cast.ai's Kimchi team argues for routing each task to the cheapest model that still meets a quality bar, judged by cost per task, with long-running sessions kept alive in remote sandboxes.

- Techniques: Per-task cost-at-quality model comparison; Outcome-scored harness with a grade gate; Milestone-based long-run planning with up-front questions; Remote sandbox session that outlives the client; Team review board for agent sessions
- Tools: Kimchi, Ferment, Teleport, Studio, pi-mono SDK (captioned as 'PyMono SSDK'), Claude

## [We're the bottleneck, but we don't have to be — Ido Salomon, AgentCraft](../videos/YIVkERhy8xo.md)
`YIVkERhy8xo` · AI Engineer · 2026-10-04 · q2 · intro · talk · also: multi-agent, product-ux, software-factory

Ido Salomon (AgentCraft) argues that humans are the bottleneck in agent work and demos a game-style orchestrator with attention-jumping, a map view, review kits, shared rooms, and a simpler "loopers" mode for non-engineers.

- Techniques: Attention queue with jump-to-next; Spatial projection of agent activity; Review kit for parallel agent output; Orchestrator with isolated local containers and background loops; Shared room with cross-agent notice board; Progressive disclosure for low-floor use
- Tools: AgentCraft, Claude Code, Codex, OpenCode, OpenClaw, Git, Telegram, MCP Apps (MCPUI)

## [Get Out of the Model's Way — Kevin Hou, Google Antigravity](../videos/buHC7bQE1X4.md)
`buHC7bQE1X4` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: multi-agent, product-ux, agent-architecture

Google's Antigravity lead on building agent products that get out of the model's way: subagent teams, sidecar triggers and generative UI, with cost and token stats from a kernel-building run.

- Techniques: Dynamic subagent teams under a lead agent; One subagent per hypothesis fan-out for eval deltas; Skills file plus natural language for internal workflow automation; Sidecar trigger process; Generative UI in the conversation instead of fixed screens; Separate the orchestration surface from the editor; Primitive audit against the next model
- Tools: Google Antigravity, Antigravity CLI, Antigravity 2.0 agent manager, Gemini 3.5 Flash, MCP, Cloud sandboxes and remote execution (unnamed), Windsurf (reference only)

## [MCP Doesn't Suck. Your Agent Does. — Jan Čurn, Apify](../videos/pAnLpiAG6Es.md)
`pAnLpiAG6Es` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: mcp-and-tools, context-engineering

Apify's CEO argues MCP's problems come from agent harnesses, not the protocol. He covers progressive tool discovery, code mode, and CLIs, then pitches MCPC, a CLI wrapper for MCP.

- Techniques: Progressive tool discovery; Code mode for tool calls; Keep large or sensitive tool output out of context; Wrap MCP in a CLI and give the agent bash; Async tool invocation with detach and poll; Connector evals
- Tools: MCP, MCPC, Claude Code, Claude Tool Search Tool, Cloudflare code mode, Bash, jq, Terminal Bench

## [AI-Generated Code Is Already Competing With Human Code — Daksh Gupta, Greptile](../videos/474j-n1Ltxc.md)
`474j-n1Ltxc` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · also: pr-code-review, evals

Greptile's Daksh Gupta uses review data from its own PR pipeline to test whether fully agent-written PRs are worse than human PRs; his answer is roughly no on reverts, severity and review rounds, but failure modes differ by agent.

- Techniques: Signal-based detection of agent-authored PRs; Proxy quality metrics for agent PRs; Per-agent failure-mode profiling via keyword counts; Three-question PR validation gate
- Tools: Greptile, Codex, Claude Code, Devin, Cursor, GitHub

## [Your AI Agent Just Changed 40 Files... Now What? (Whiteboard)](../videos/cP5PRDo3u6Q.md)
`cP5PRDo3u6Q` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: pr-code-review, claude-code, dev-tools

Walkthrough of Whiteboard, an open-source Mac app that lets a coding agent draw linked review diagrams of its own branch changes, with a privacy warning about its default telemetry.

- Techniques: Install Whiteboard as a Claude Code plugin; Turn telemetry off before opening a private repo; Review-only prompt with tool-call approval; Click-through verification of diagram blocks; Typed diagram blocks instead of free-form output; Diff reduction for large agent branches; Own-backend OpenTelemetry instead of vendor telemetry; Check trace storage before enabling trace capture
- Tools: Whiteboard (open-source Mac app, MIT, VS Code fork), Claude Code, Codex, Cursor, OpenCode, VS Code / Code OSS, Electron, Rust (diff engine), MCP, Mermaid, Archify, CodeRabbit

## [React-Native Is Dead... Thanks to AI.](../videos/r0u83Ss7QRc.md)
`r0u83Ss7QRc` · Better Stack · 2026-10-02 · q3 · intro · news · also: software-factory, testing-verification, dev-tools

Better Stack commentary on Shopify dropping React Native for native apps, with Shopify's Helix checkpoint-gated agent loop and headless app logic for fast agent testing. Opinion-led, relays Shopify's blog post.

- Techniques: Checkpoint-gated agent migration (Helix pattern); Headless state plus CLI driver for agent testing; Avoid out-of-process UI automation for agent verification
- Tools: React Native, Shopify React Native packages (FlashList, React Native Skia, Restart), Helix (Shopify in-house agent migration system), Swift, Kotlin, SwiftUI, CloudKit, Apple XCUITest

## [Github Top Trending Tool Just Fixed The AI Agent’s Biggest Problem](../videos/cyIWQHYoUg8.md)
`cyIWQHYoUg8` · AI LABS · 2026-10-02 · q3 · practitioner · review · also: token-cost-efficiency, context-engineering, rag-retrieval

Walkthrough of Graft, a free open-source CLI that builds a code knowledge graph and hooks into Claude Code to cut search turns, tokens and cost; the benchmark is self-reported by its makers.

- Techniques: Code knowledge graph for impact-aware retrieval; Pre-prompt context injection via a UserPromptSubmit hook; Hook trio for a Claude Code workflow; Pick CLI injection or MCP on-demand lookup; Long autonomous run setup for a token-hungry model; Install and initialize Graft in a Claude Code project
- Tools: Graft, Claude Code, Codex, MCP, Opus, GPT 5.6, GPT Astra (as transcribed, unverified), Fable 5.1 (as transcribed), Hydra (sponsor; API for AI generation)

## [Opus 5.5 vs GPT-6 Sol (Blender F1 Car Test)](../videos/Zc72O98x3nk.md)
`Zc72O98x3nk` · Better Stack · 2026-10-02 · q2 · practitioner · review · also: models-research, token-cost-efficiency, evals

Better Stack runs Opus 5.5 (Claude Code) and GPT-6 Sol (Codex) through the same three Blender prompts (static F1 model, build animation, pit-stop animation); Opus wins on quality but costs about 6x more.

- Techniques: Same-prompt, same-order head-to-head across agent CLIs; Judge cost per finished task, not per token; Build an animation as a sequence of agent prompts
- Tools: Claude Code, Codex, Blender, Claude Opus 5.5, GPT-6 Sol, GPT-6 Astra, Fable 5.1, GPT-6 Luna

## [The GPT 6 Astra Vs Claude Fable 5.1 Debate Is Finally Over](../videos/BwNNcob3-A0.md)
`BwNNcob3-A0` · AI LABS · 2026-10-02 · q2 · practitioner · review · also: models-research, evals, token-cost-efficiency

Blind-judged comparison of Claude Fable 5.1 and GPT-6 Astra on the team's own client-style projects: Fable wins quality, interaction and review depth; Astra wins cost, speed, instruction following and long-running builds.

- Techniques: Blind LLM-as-judge on your own tasks; Human-in-the-loop UI review with a per-model viewer; Autonomy test with a vague brief written in the model's own prompting guide style; Track output tokens and tool calls as cost drivers; Enforce file-edit tool use and check for violations afterward; Planted-bug review test with decoys; Check whether the model changed mid-run
- Tools: Claude Fable 5.1, GPT-6 Astra, GPT 5.6 (judge model), Claude Code, Codex, Claude Opus (referenced for design comparison), Cursor (named as a place to use the Zapier SDK), Zapier SDK

## [This Open-Source Tool Makes Claude Create Architecture Diagrams](../videos/iuJszJuiuSg.md)
`iuJszJuiuSg` · Better Stack · 2026-10-02 · q3 · practitioner · tutorial · also: context-engineering, dev-tools

Better Stack walkthrough of Archify, an open-source agent skill where the coding agent emits validated typed JSON that a local compiler renders into HTML architecture diagrams; useful for PR and design-review artifacts, not for READMEs or mapping huge repos.

- Techniques: Schema-validated diagram IR; Evidence-gated nodes; Narrow architecture question prompt; Diff two architecture snapshots; Install as an agent skill
- Tools: Archify, Claude Code, Cursor, Codex, Mermaid, GitHub

## [Github #1 Trending Skill's Author Just Fixed Claude's Design Problem](../videos/Ow_z94c3wKk.md)
`Ow_z94c3wKk` · AI LABS · 2026-10-02 · q2 · practitioner · review · also: mcp-and-tools, vibe-coding-app-building

Walkthrough of Inspo, a free MCP server of 832 captured sites with per-site design.md files that lets coding agents pull real references before designing. Sponsored segment; tested on one demo page.

- Techniques: Pre-build style menu; Reference provenance check; Filter-scoped reference search; Cap reference study depth; Install Inspo in user scope; Split design and animation into separate MCP lookups
- Tools: Inspo (MCP server, free, no account or API key), UI Skills MCP server, Emil Kowalski animation skill, Mengto scroll animation skill (name as transcribed), Hallmark design skill (name as transcribed), AI Labs Pro design system (community resource), Claude Code, Manid (sponsor, agent tools API gateway)

## [This Is What Voice Coding Was Supposed to Be (Qwen Audio Agent)](../videos/blpZ1xgFhCk.md)
`blpZ1xgFhCk` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: voice-multimodal, agent-architecture, multi-agent

Hands-on review of Qwen Audio Agent, an open-source voice runtime that keeps a voice conversation alive while Claude Code does slow coding work in the background over ACP. The main lesson is that voice coding is a concurrency problem, not a transcription problem.

- Techniques: Voice front-end + async coding back-end over ACP; Interruption as an explicit state machine; Local fast-path for trivial questions; Setup (as demonstrated)
- Tools: Qwen Audio Agent (open-source voice runtime, Apache 2.0; no model weights shipped), Claude Code (back-end coding agent), Codex, OpenCode, ACP (Agent Client Protocol), Alibaba DashScope (paid cloud voice API), OpenAI Realtime API (mentioned as comparison), PipeCat (mentioned as comparison), LiveKit Agents (mentioned as comparison), Whisper (dictation baseline), Hugging Face speech-to-text pipeline, MLX (Apple Silicon local backend)

## [Shadcn Just Fixed Tailwind's Biggest Problem](../videos/tPQgw_DPIoM.md)
`tPQgw_DPIoM` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: dev-tools, vibe-coding-app-building

shadcn's new agent-first linter for Tailwind v4 design systems. It turns design-system rules into lint errors that AI agents can fix against, which the presenter says cut violations to zero in his eight-task test.

- Techniques: Lint the design system instead of prompting it; Use lint messages as the agent's fix instructions; Per-component contracts; Custom messages and a global note; Strict component APIs as a prerequisite
- Tools: shadcn linter (shadcn's new Tailwind design-system linter, no version stated), Oxlint, ESLint, Tailwind CSS v4, shadcn/ui, CVA (class-variance-authority, read by the linter for variant lists), Biome (no plugin yet; open GitHub issue), Starlex (transcribed name; presenter cites it as the alternative people switch to)

## [Claude Code + GPT 6 Astra Just Killed AI Video Editing](../videos/p565AqELA8M.md)
`p565AqELA8M` · AI LABS · 2026-10-02 · q2 · practitioner · tutorial · also: claude-code, voice-multimodal, token-cost-efficiency

Tutorial for making agent-generated product videos in Claude Code: plan first, review in the browser, render shots one by one, then add music. Sponsored in part, and the title oversells it.

- Techniques: Route Claude Code to a Codex subscription via a local proxy; Plan-first with browser preview, comments, and an explicit lock; Render shots individually at full resolution, approve, then fix; Polish and combine with explicit timing; Music skill driven by plan style and shot cadence
- Tools: Claude Code, GPT-6 Astra (OpenAI model, accessed through Codex), Codex, CLI Proxy API, Homebrew (brew), Hyperframes (video-creation tool with skills), Mixkit (free music library), Luma Ray 3.2 (sponsor), Ray 3 (comparison), Kling 3.0 (mentioned in sponsor segment), Gen 4.5 (mentioned in sponsor segment), Fable (model compared to Astra on design in an earlier video)

## [This New Open Source Tool Just Fixed Your Claude Code Workflow](../videos/CHHEjuNBxoQ.md)
`CHHEjuNBxoQ` · AI LABS · 2026-10-02 · q3 · practitioner · review · also: context-engineering, memory, security-guardrails

Walkthrough of Agit, an open-source tool that applies git's model (repos, sessions as branches, turns as commits) to agent conversations, with sharing, revert, cross-agent fork and secret redaction.

- Techniques: Versioned agent sessions via a git-style repo; Reverting a session to an earlier turn; Cherry-picking messages between sessions; Forking a Claude Code session into Codex; Registering known passwords before a session is saved
- Tools: Agit, createagit (installer), npm, GitHub, Claude Code, Codex, AGENTS.md, CLAUDE.md, Runnable (sponsor)

## [Insane GitHub Repos That 10x Your Codex And Claude Code Setup](../videos/Ua0APTMVcb8.md)
`Ua0APTMVcb8` · AI LABS · 2026-10-02 · q2 · intro · review · also: skills-self-improvement, testing-verification, token-cost-efficiency

AI LABS tours eight GitHub tools that extend Claude Code and Codex setups: browser verification, terse output, design-skill search, planning, skill evals, and linting. Mostly README-level, with one sponsor segment.

- Techniques: Browser-verified completion check (Reticle); Staged image-to-3D reconstruction with self-comparison; Terse-output plugin with lifecycle hooks (Chisel); MCP-attached design skill search (UISkills); Interview-plan-review-verify loop (Ouroboros); Apple-native skill pack for iOS UI; Skill evaluation with Caliper; Rule-based anti-pattern guard (Antislop)
- Tools: Image-to-3JS skill (spoken 'image to 3JS', captioned 'Image23JS'; GitHub trending per the presenter), Reticle, Chisel, Caveman, Ponytail, UISkills, Manufact (sponsor; hosted MCP server deployment and publishing checks), mcp-use open-source SDK (captioned 'MCPUs'), Ouroboros, Apple SwiftUI skills repo (Liquid Glass skill, layout skill), Liquid Glass (Apple iOS 26 design system), Claude Code (plugins, hooks, Skill Doctor command)

## [We Let Claude Code and Codex Race Human Researchers — Elie Bakouch, Prime Intellect](../videos/oVsEddfhdxc.md)
`oVsEddfhdxc` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: claude-code, models-research, evals

Prime Intellect's Elie Bakouch runs Claude Code and Codex on an optimizer speedrun against human records, finding both beat the records but neither produced a novel optimizer, and that Claude Code idled while Codex kept working.

- Techniques: Speedrun as a verifiable research environment; Constrained variants to force novelty; Goal file plus rules file as the agent's contract; Restart with the latest best state; Behavior logs normalized by active time; Generator, judge and scale-up loop
- Tools: Claude Code, Codex, Slurm, AGENTS.md, goal.md, Verifiers, Prime-RL, Hosted Training, Kimi K2.7, GLM

## [The Dark Arts of Skill Engineering — Paul Bakaus, Renaissance Geek (Impeccable)](../videos/SQMCtZX3trg.md)
`SQMCtZX3trg` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: skills-self-improvement, context-engineering, evals

Paul Bakaus (Impeccable) on building production agent skills as harness extensions: blind sub-agents, forced divergence, scripts, hooks and per-model builds, rather than prose alone.

- Techniques: Blind adversarial critique; Anti-attractor divergence; Register routing inside one skill; Cross-session skill memory; Scripts that print next-step instructions; Pre-tool-use blocking hooks for weaker models; Hook-driven feedback loop from a skill; Unskippable gates with logged results; Per-harness and per-model builds; Ablation testing of rules; LLM-as-user with a judge panel; Inverted judges
- Tools: Claude Code, Codex, Cursor, GitHub Copilot, Gemini, Playwright, skills.sh, npx skills

## [500 Skills, Zero Fine-Tuning: LinkedIn's Playbook for AI Agents — Ajay Prakash, LinkedIn](../videos/9wZpvF3QleU.md)
`9wZpvF3QleU` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: skills-self-improvement, mcp-and-tools, context-engineering

LinkedIn's Ajay Prakash on an internal MCP server that serves tools plus self-contained markdown "playbooks" teaching coding agents company workflows, kept current by a PR-based self-update loop.

- Techniques: Playbooks as MCP-served instruction docs; Compose playbooks by reference; Session-end playbook self-update PR; Three meta tools for large tool catalogues; Central plus repo-local instruction split; Single pre-installed local MCP server with hourly auto-update
- Tools: MCP, Claude Code, GitHub Copilot, Cursor, Airflow, Jira, Slack

## [We let an AI agent execute Bash and lived to talk about it — Sarah Sanders, PostHog](../videos/4lXks428C9o.md)
`4lXks428C9o` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: security-guardrails, sandboxing-execution

PostHog's Sarah Sanders on securing the PostHog wizard, an agentic CLI with shell access: deterministic enforcement, scanning every content source, and an LLM used only as an advisor.

- Techniques: Deterministic gate ahead of LLM judgment; Detector separated from actor; Scan both ends of the content pipe; Rule anatomy with paired tests; Deny-by-default command allowlist with a vault; Audit for composed attacks
- Tools: YARA, Ink, MCP, PostHog wizard, Warlock, Cursor

## [ACP: The Universal Remote Control for AI Agents — Alex Hancock, Block](../videos/YkNulwcc5jk.md)
`YkNulwcc5jk` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: mcp-and-tools, agent-architecture

Alex Hancock (Block, Goose and MCP maintainer) argues for ACP, an open client-to-harness protocol, so one client can drive any agent over local stdio or remote HTTP/WebSocket.

- Techniques: Standard client-to-harness protocol (ACP); Underscore-prefixed custom methods, then standardize by usage; Transport swap with unchanged messages; Split the agent stack into four movable parts
- Tools: ACP (Agent Client Protocol), Goose, Zed, JetBrains IDEs, MCP (Model Context Protocol), JSON-RPC, stdio, HTTP, WebSocket

## [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../videos/5Bn0xro2ol8.md)
`5Bn0xro2ol8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, testing-verification, context-engineering

Figma engineer on rolling out coding agents across an org: verification-first testing, plan-before-prompt with phase validation gates, and labeling AI-written text so reviewer attention is spent well.

- Techniques: Verification-first agent workflows; Encode agent discoveries as deterministic tests or flows; Testing pyramid for agent-written code; Red-green prompting; Why-first phased plan with validation gates; Human-first labeled communication; Agent-in-thread invitation
- Tools: Playwright MCP, Slack, cloud coding agent (unnamed)

## [Building ambitious software — Jonathan Kelley, Dioxus Labs & Cognition](../videos/H7vFrcNWXzs.md)
`H7vFrcNWXzs` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: testing-verification, context-engineering

Dioxus Labs (now part of Cognition) on building an ambitious Rust framework with coding agents: fast on knowledge work and mundane upkeep, weak at tests, and architecture plus review now carry the load.

- Techniques: Let the compiler's strictness act as the agent's guardrail; Agents as a knowledge oracle for platform and spec behavior; Delegate checklist-style maintenance to agents; Agent-built fuzzing harnesses; Human-enumerated test conditions with agent brainstorming; Architecture-first, then implementation, with full PR reading
- Tools: Claude Code, Rust, Dioxus, Blitz, SubSecond, Firefox (CSS engine), Electron, React Native, Flutter, Kotlin, Swift, Zed

## [The Spatial Harness: Bringing Agents to the Canvas — Max Drake, tldraw](../videos/XWcXwnysmpY.md)
`XWcXwnysmpY` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: product-ux, multi-agent, agent-architecture

tldraw's Max Drake on giving LLM agents a spatial canvas: teaching them to read screenshots plus shape data, running multi-agent fairies, and driving live apps and the desktop through code.

- Techniques: Screenshot plus structured data as canvas context; Agentic canvas harness with self-set goals; Visual agent identity and on-canvas task state; Orchestrator agent posting tasks to a shared board; Local editor server for code-mode agents; Dependency graph of agent tasks
- Tools: tldraw SDK, tldraw desktop app, Claude Code, Notion, Gmail, Conductor, OpenAI Symphony

## [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](../videos/V_5bn4q-vAI.md)
`V_5bn4q-vAI` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: context-engineering, mcp-and-tools, product-ux

Christopher Burns (Inth) on making LLMs recommend and correctly use his open-source cookie-banner library by shipping agent-friendly docs: hand-written llms.txt, markdown twins, web MCP, and grep-able docs inside node_modules.

- Techniques: Hand-curated llms.txt index; Markdown twin per page with discovery header; Three ways to reach markdown; Bundle docs in the package with an agents.md pointer; Web MCP for docs; Agent-readiness checks as a loop
- Tools: LeadType, llms.txt, llms-full.txt, AGENTS.md, Next.js, Aura AI, Cloudflare agent-readiness checker, MCP

## [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../videos/pqlWNihgdjI.md)
`pqlWNihgdjI` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: enterprise-adoption, context-engineering, testing-verification

Amazon's frontier-dev habits from AWS's Clare Liguori: teams that changed how they worked (context files, self-validating agents, spec-first, local tests) hit a 4.5x median in deployment velocity; tool-only teams got under 3x.

- Techniques: Living steering/skills file with a rule per agent mistake; Self-validating agent loop; Spec-first iteration; Local deterministic mock services; Agent-friendly language and error design; Deployment velocity as the productivity metric; Decision-speed audit
- Tools: Kiro, MCP servers, Bedrock, TypeScript, Rust

## [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../videos/mJqwmmOx4WA.md)
`mJqwmmOx4WA` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: governance-compliance, vibe-coding-app-building, product-ux

Andrew Garvin (Metronome, now part of Stripe) live-demos using Stripe Projects and a Metronome billing agent to build a usage-based billing setup from one natural-language prompt, arguing for sandboxed agent-built billing and for usage or credit pricing when agents are the users.

- Techniques: Portable skills files as agent context for a complex API; Verbose, machine-readable errors for agent self-correction; Sandbox-first agent-built billing with synthetic usage; Natural-language provisioning through a CLI orchestrator; Classify agent roles before designing pricing
- Tools: Stripe Projects, Stripe CLI, Metronome, Claude (selected as the coding agent in the demo), Vercel, Postgres, skills files

## [Prototyping as Leadership: How a CTO Ships with AI Agents — Hursh Agrawal, The Browser Company](../videos/bdHaOXZOhcM.md)
`bdHaOXZOhcM` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: software-factory, evals, enterprise-adoption

A CTO explains how a manager with a full calendar keeps building by running coding agents overnight (context gathering at 5pm, morning review), using evals and custom-model training as examples.

- Techniques: Overnight agent loop; Context-harvesting prompt; Test-first with end-to-end computer-use verification; Feedback-to-eval hill-climb; Overnight custom-model training with sandboxed cloud access; Prototype branch behind feature flags; Small PRs with an AI reviewer in a clean sub-agent
- Tools: Claude Code, Codex, Cursor, Dia, Wispr Flow, Slack, Jira, Confluence, Notion, SQLite, AWS EC2, ModernBERT

## [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../videos/qqrk7CtkuIw.md)
`qqrk7CtkuIw` · AI Engineer · 2026-09-18 · q3 · practitioner · interview · also: software-factory, pr-code-review, enterprise-adoption

Anthropic's Mike Krieger on how Labs builds: delegate end states to agents, be less constrained with tools, share intent instead of 2,000-line PRs, and run fast persevere-or-pivot cycles.

- Techniques: Describe the end state, then review the trade-offs; Give agents a full environment instead of a narrow tool set; Port-verify-cross-read loop for large code migrations; Capture production runtime types to guide migrations; Share intent, trade-offs and production measurements in place of raw diffs; Tiered review: deep human review for architecture, fix-forward for cosmetic; Agent as a shared teammate in team channels; Instrument before you need it; use flags and dynamic config; Short bets with two-week persevere-or-pivot reviews; Unship primitives superseded by newer ones
- Tools: Claude Code, Claude Design, Cowork, Claude Code artifacts, Bun, MonkeyType, Slack, Python, TypeScript

## [Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic](../videos/rbjWzZK2LU0.md)
`rbjWzZK2LU0` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: governance-compliance, security-guardrails

Sachin Malhotra (Anthropic CI) on giving agents budgets instead of tokens: classify verbs by how they fail, cap every write with refilling rate limits, watch aggregates with tripwires, and take identity from infrastructure.

- Techniques: Verb triage by failure visibility; Break-glass verbs with proxy-stamped audit; Refilling per-write rate limits with scope-sized budgets; Bypass that asks the human inside agent sessions; Aggregate tripwires paired with context fixes; Undo test for sizing controls; Identity stamping at the proxy with inherited labels; Two-layer policy: text plus deterministic proxy
- Tools: Kubernetes, admission webhook, Slack, Claude Code

## [Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](../videos/lRa9sPaMyy4.md)
`lRa9sPaMyy4` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: testing-verification, context-engineering

Varun Pant (AWS) argues that formal verification in Lean, Verus and similar tools can prove code correct for all inputs, which tests and LLM judges cannot, and that humans should own the specification while agents write code and proofs.

- Techniques: Spec-first verified agent coding; Spec model plus differential random testing; Lemma decomposition for AI proofs; In-code pre- and post-conditions checked by a solver; Intermediate-representation dialect to many backends
- Tools: Lean, Lean 4 browser playground, Kiro (transcript shows 'Kero', likely the AWS agentic IDE), Verus, Z3, Aeneas, Strata / Strata Core, Cedar, SMT solvers, model checkers, ArenaLang (kernel registry)

## [The Missing Layer: Design Taste in AI Agents — Hassan El Mghari, Together AI](../videos/7GMKdpLsxwU.md)
`7GMKdpLsxwU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: vibe-coding-app-building, product-ux, context-engineering

Hassan El Mghari (Together AI) on getting AI-built UIs out of "AI slop": codify the tells as anti-patterns, feed in references, iterate with a cheaper model.

- Techniques: Slop-gate anti-pattern list in a design skill; Theme library as inspiration; Screenshot inspiration vault; Two-tier model routing for UI work; agents.md as a taste log; Batched feature prompting
- Tools: Codex, Claude Code, Cursor, Hallmark, agents.md, GLM 5.2, Opus 4.8, Composer 2.5, Together AI

## [Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean](../videos/FvxY8oPoI8o.md)
`FvxY8oPoI8o` · AI Engineer · 2026-09-18 · q2 · practitioner · demo · also: token-cost-efficiency, infra-cost-scaling, evals

DigitalOcean's Archana Kamath and Tyler Gillam argue for per-request model routing chosen by task, cost, latency and rules, validated with your own evals. A live OpenCode demo shows roughly 3x lower session cost at similar quality, though the evidence is one vendor demo.

- Techniques: Per-task model pools with ordered failover; Natural-language routing preferences plus hard rules; Side-by-side routed vs single-model agent runs with live cost tracking; Eval-gated routing with feedback loop
- Tools: Plano (open-source proxy and routing model), OpenCode, Claude Opus, Claude Sonnet 5, GLM 5.2, GPT 5.2, Llama 4 Maverick (caption reads 'long before Maverick')

## [Design at the Speed of Adjectives — Paul Bakaus, Renaissance Geek, Inc.](../videos/v42opQpCy60.md)
`v42opQpCy60` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: vibe-coding-app-building, product-ux, context-engineering

Paul Bakaus on steering coding agents toward good design with a skill (Impeccable) that maps vague design adjectives like "bolder" to project-specific meanings, keeping humans in the loop instead of one-shotting.

- Techniques: Project-defined verb and adjective commands; Self-check against a stated failure test; Pre-brief questions before generation; Workflow-stage command mapping; Community-tested experimental commands
- Tools: Impeccable, Claude Code, GitHub Copilot, Cursor, Codex, Figma, Webflow, Claude Design, Radiant Shaders

## [PrimeAgent + Opus 5 is INSANE (Why I Dropped Claude Code)](../videos/kg3MmLd0qEM.md)
`kg3MmLd0qEM` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: agent-architecture, memory, skills-self-improvement

A Kai Explains review of Prime Agent, an open-source MIT terminal coding harness with cross-session learning, paired with Claude Opus 5 as a Claude Code replacement; the self-reported benchmarks are flagged as unverified.

- Techniques: Learned-layer self-improvement over an immutable base prompt; Persistent goal with bounded autonomous run; RLM-style context management; Per-task effort dial; Model-agnostic routing with self-hosting; Container isolation for self-modifying agents
- Tools: Prime Agent (Prime Intellect, MIT, open-sourced 2026-08-05), Claude Opus 5 (released 2026-07-24), Claude Code, Cursor, Cline (transcribed as 'Klein'), Claude Fable 5, GPT 5.6 Sol, vLLM, Ollama (transcribed as 'Alama'), LM Studio, FrontierBench v0.1, ARC-AGI-3

## [Spotify Made an Agent Harness... I Don't Hate It](../videos/TK1LvtX-Bqs.md)
`TK1LvtX-Bqs` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: multi-agent, dev-tools

Walkthrough of Spotify's closed-source agent session manager "Zerp" (Claude Code, Codex, Gemini in one GUI). Useful session features, but the host finds nothing that justifies the account and closed-source tradeoff.

- Techniques: Dependent worktree chains for agent work; Forking a session to test alternatives; Mid-session agent handoff; Grid monitoring of parallel agents
- Tools: Zerp (Spotify internal agentic development environment; auto-captions transcribe it as Zurb), Claude Code, Codex, Gemini, Portal (Spotify product, related to Zerp), tmux, CMUX, Conductor, T3 Code, Matt Pocock's skills (referenced, not in the video)

## [Fable 5.1 is here, and its REALLY good](../videos/0lBvjhcRqyU.md)
`0lBvjhcRqyU` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: models-research, token-cost-efficiency, vibe-coding-app-building

Better Stack's hands-on review of Fable 5.1: a pricing and benchmark rundown, then five one-shot builds (F1 browser game, tennis-club site) comparing cost, time and tokens against Fable 5, GPT 5.6 Sol, Grok 4.6 and Kimi K3.

- Techniques: Pick effort level by cost per task, not per token; Same prompt, single-file runnable artifact, measure time/cost/tokens; Use the same effort level across models before comparing
- Tools: Fable 5.1, Fable 5, Mythos 5.1, Opus 5, GPT 5.6 Sol, GPT Image 2, Grok 4.6, Kimi K3, Three.js, Artificial Analysis Intelligence Index, Cursor bench, Terminal Bench Science

## [How To Use Claude Design To Build Beautiful Sites](../videos/bBlY5YOsKN8.md)
`bBlY5YOsKN8` · AI LABS · 2026-09-02 · q3 · practitioner · tutorial · also: vibe-coding-app-building, context-engineering, skills-self-improvement

A five-stage workflow for building a site with Claude Design: write a design.md brand file first, build a design system from it, wireframe, produce the full design, then hand off to Claude Code with a Supabase backend.

- Techniques: design.md-first planning skill; Preview design.md outside the token-metered tool; Design system from design.md; Wireframe, then batched comments; Full design from a chosen wireframe; Claude Design to Claude Code handoff; Post-build design.md conformance review; Supabase skill install and MCP connection
- Tools: Claude Design, Claude Code, Opus 5, Opus 4.7, Haiku, Fable, design.md (Google format), Supabase, Supabase agent skills (general and best-practices), Supabase MCP, Supabase CLI, VS Code

## [Can a Local LLM Actually Replace Claude or Codex for Coding?](../videos/uefMWJ1GBWg.md)
`uefMWJ1GBWg` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: local-ai, token-cost-efficiency, infra-cost-scaling

Kai Explains on whether a local open-weight model can replace Claude Code or Codex for coding. Verdict: memory and tool-calling decide it, the hybrid and free-tier route wins on cost for most people, and local is a daily driver only for bounded work.

- Techniques: Test the harness on a trivial task before a big job; Size hardware as weights plus context; Prefer higher quantization on a smaller model for tool use; Rewire a cloud CLI to a local endpoint; Hybrid routing: frontier plans, local executes; Sandbox any local agent that can run shell commands; Break-even math for local versus cloud; Price agent API usage on cached input
- Tools: Claude Code, Codex, ChatGPT, Ollama, llama.cpp, MLX, LM Studio, Aider, OpenCode, Cline (transcribed as Klein), Qwen Code (transcribed as QuenCode; model not named), OpenRouter

## [I Made Qwen 3.8 and Claude Opus 5 Build the Same Game](../videos/m8HFQ8cZlTU.md)
`m8HFQ8cZlTU` · Better Stack · 2026-09-02 · q2 · intro · review · also: models-research, token-cost-efficiency, local-ai

Better Stack runs the same one-prompt 3D endless-runner build on Qwen 3.8 (2.4T open-weight) and Claude Opus 5, then argues cost, speed, verbosity and weight access matter more than the 58-vs-63 benchmark gap.

- Techniques: Same-prompt, play-the-output model comparison; Score by behavior, not by code volume; Route by three axes: speed, verbosity, access; Hosted open-weight via an OpenAI-compatible endpoint
- Tools: Qwen 3.8 (2.4T total, ~95B active, open-weight), Qwen 3.8 Max (hosted production variant), Qwen 3.8 27B (mentioned as the locally-runnable size), Claude Opus 5 (Max), three.js (CDN, used by the game test), Artificial Analysis (benchmark index), OpenRouter, DeepInfra, Fireworks

## [How To Never Run Out Of Codex and Claude Usage Limits](../videos/jwje1JK8Nqs.md)
`jwje1JK8Nqs` · AI LABS · 2026-09-02 · q3 · practitioner · tutorial · also: token-cost-efficiency, claude-code, context-engineering

AI Labs walks through 24 tactics for stretching Claude Code and Codex usage limits, from habits (clear, compact, rewind, one big prompt) to settings (model and effort, skill and CLAUDE.md size, memory, bundled skills, output caps, advisor).

- Techniques: Clear between unrelated tasks; Compact with explicit keep-instructions, before breaks; Rewind instead of correcting; Batch changes into one prompt; Turn off automatic session recaps (Claude Code only); Set model per task with /model and effort with /effort; Pin sub-agent model in the prompt, or route automatically with a skill; Keep skills small with reference files; Write a lean CLAUDE.md and per-folder CLAUDE.md files; Check spend with the usage command; Use a CLI instead of an MCP server when the CLI is enough (Supabase example); Turn off memory and bundled skills; Disable or cap sub-agent workflows; Filter passing tests out of tool output with a hook; Cap bash output length; Replace the built-in advisor with a custom on-demand agent; Message between Claude Code sessions with only the relevant part
- Tools: Claude Code, Codex, Claude Opus, Claude Sonnet, Claude Haiku, GPT-5.6 Sol (spoken as GPT 5.6 Soul), GPT-5.6 Terra (spoken; name uncertain), GPT-5.4 Mini, ChatGPT plans (Free, Go, Plus, Pro), Claude Pro and Max plans, Supabase, Supabase CLI

## [10 Best Local Coding Models Right Now 2026](../videos/z605KVofJAY.md)
`z605KVofJAY` · Kai Explains · 2026-09-02 · q3 · intro · review · also: local-ai, models-research, inference-serving

Kai Explains lists 10 open coding models split by hardware tier and task type, and argues that picking a model for your own hardware and job matters more than leaderboard rank.

- Techniques: Hardware-first model sizing; Route models by job, not one model for everything; Local tab completion with Continue.dev and a FIM model; Running Qwen3.6 27B on one 24 GB card; Pick for tool-call reliability; Filter by license before commercial use; Cheap hosted model for bulk processing
- Tools: GLM 5.3, Kimi K2.7, Kimi K3, DeepSeek V4 Pro, DeepSeek V4 Flash, Qwen3-Coder (480B), Qwen3-Coder-Next, Qwen 3.6 27B, Qwen 2.5 Coder 14B, Devstral Small 2, GPT-OSS-20B, Codestral 2

## [Buzz Just Fixed AI Agents... But It Has A Serious Flaw](../videos/a8tLTd4q-fU.md)
`a8tLTd4q-fU` · AI LABS · 2026-09-02 · q2 · practitioner · review · also: multi-agent, token-cost-efficiency

AI LABS tests Buzz, an open-source group-chat app where Claude and GPT agents share channels; they find real coordination and token-cost problems but praise its per-agent attribution and cross-vendor adversarial review, and say solo builders should skip it.

- Techniques: Role-explicit prompt for multi-agent planning; Cross-vendor adversarial review of a spec; Per-agent identity and attribution in a shared channel; Agent export with memory; Installing Buzz
- Tools: Buzz (v0.5, open-source group-chat app for agents), Claude Code, Claude Code agent teams, Codex (OpenAI coding agent), GPT (OpenAI model), Goose (coding agent), Slack, Claude Tag (Anthropic Slack agent, team and enterprise plans), OpenAI Codex plugin for Claude Code, EgoLite (sponsored browser-agent skill, Mac only), GitHub, Vercel

## [Stop Worrying About Token Costs (DeepSeek V4 Flash)](../videos/93iYf9wp7Qw.md)
`93iYf9wp7Qw` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: models-research, token-cost-efficiency

Better Stack tests DeepSeek V4 Flash against seven similar models on cost, speed and output quality by building the same full-stack finance app; it is far cheaper per task but weaker on UI and slower.

- Techniques: Cost-per-task ranking instead of per-token price; Same-prompt, from-scratch build benchmark; Check provider prices on OpenRouter; Split models by task strength; Explicit prompt for real persistence
- Tools: DeepSeek V4 Flash 0731, DeepSeek V4 Flash, Kimi K3, GLM 5.2, Gemini 3.6 Flash, Gemini 3.5 Flash, GPT 5.6 Luna, GPT 5.6 Sol, GPT 5.6 Terra, GPT 5.5, Opus 5, MuseSpark

## [oMLX Best Way to Run Local AI on A MAC](../videos/j557WxWtdZk.md)
`j557WxWtdZk` · Kai Explains · 2026-09-02 · q3 · practitioner · tutorial · also: local-ai, inference-serving, token-cost-efficiency

Kai Explains walks through OMLX, an open-source local inference server for Apple Silicon Macs that keeps a two-tier (RAM + SSD) KV cache so near-identical prefixes in long coding-agent sessions are reused instead of recomputed, mainly cutting time-to-first-token.

- Techniques: Diagnose slow agent turns as a prefix-cache miss; Install OMLX via the signed DMG; Point Claude Code at OMLX; Point Cursor at a local OpenAI-compatible server; One-command agent configuration with OMLX's CLI launcher; Browse and reuse Hugging Face and LM Studio model caches
- Tools: OMLX (Apache 2.0, about 18.6k GitHub stars, by one developer), Apple MLX / MLX server, Claude Code, Cursor, OpenCode, Codex, PyAgent, Pi, Hugging Face cache, LM Studio, safetensors, Qwen3 Coder Next (8-bit, benchmark model)

## [This Linter Rejects AI Slop From Your Code](../videos/mmrSYvYKD9g.md)
`mmrSYvYKD9g` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: testing-verification, dev-tools, token-cost-efficiency

Better Stack demo of the anti-slop rule package for oxlint, which hard-fails low-evidence TypeScript/JavaScript patterns and whose error messages give coding agents a fix to apply.

- Techniques: Hand-picked lint gate for agent-written TS/JS; Agent self-repair loop on lint output; Validate untrusted input at the boundary instead of casting
- Tools: oxlint (Oxc; Rust-based JavaScript and TypeScript linter), anti-slop (rule package for oxlint; created the week before the video), Oxc (the toolchain that oxlint belongs to), Claude Code, CLAUDE.md, TypeScript, ESLint (comparison point only), Zod (suggested runtime validation)

## [YC Just Open-Sourced Its Multiplayer Harness](../videos/GrZ-X3-2TVs.md)
`GrZ-X3-2TVs` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: agent-architecture, security-guardrails, enterprise-adoption

Better Stack's hands-on tour of YC's open-source "multiplayer" agent harness (QM): a self-hosted, multi-user web app with Slack access, per-workspace containers, a seven-tool surface and org-level approval modes. Promising but two weeks old.

- Techniques: Minimal primitive tool surface plus shell sandbox; Org ceiling with per-team tightening and a posture-independent command deny list; Enable extra harnesses through the admin API; Share context through a team project, keep credentials private by default
- Tools: QM (YC open-source multiplayer agent harness; the caption spelling may be off, and the repo was about two weeks old at the video date), pi (the default agent harness in QM), Claude Code (can be enabled as a harness inside QM), Slack (integration surface), PostgreSQL (session history), GitHub (repo linked in the description)

## [This Makes Claude Code Free Forever](../videos/vxrZWbZ2fZA.md)
`vxrZWbZ2fZA` · Better Stack · 2026-09-02 · q3 · intro · review · also: claude-code, token-cost-efficiency, local-ai

Free Claude Code, an open-source local proxy that keeps Claude Code's interface but sends its requests to a free, cheaper, or local model. Useful for routing easy tasks off premium models; the speaker says it is not a replacement for Claude.

- Techniques: Proxy-based model swap behind an unchanged coding client; Tiered per-task model routing; Bounded refactor as a smoke test for a new model route; Reliability-first fallback to premium model
- Tools: Free Claude Code (FCC), Claude Code, Codex, Pi, NVIDIA NIM, OpenRouter, Opus 5 (model name shown in Claude Code UI)

## [This Claude Skill Just Fixed Loop Engineering](../videos/D_uojDHkbw4.md)
`D_uojDHkbw4` · AI LABS · 2026-09-02 · q3 · practitioner · tutorial · also: multi-agent, testing-verification

Explains the "gauntlet loop" (agent builds, critic sub-agents judge against a reference) and its two failure modes, then shows a planning-skill fix: a settled spec and pass/fail answer key the critic checks against.

- Techniques: Three-line gauntlet loop prompt; Swap the reference for a planned answer key; Planning fog map; Phased build order inside one loop
- Tools: Claude Code, Wayfinder (Matt Pocock planning skill), Grill Me (Matt Pocock skill), Matt Pocock skill set (installed from GitHub), Claude Max plan, Claude API (cost comparison), SerpAPI (sponsor, not used in the method)

## [OpenSource AI Tools That Feel ILLEGAL To Get Free](../videos/VghawjhiGkw.md)
`VghawjhiGkw` · Kai Explains · 2026-09-02 · q3 · intro · review · also: local-ai, token-cost-efficiency, agent-architecture

Kai Explains reviews five open-source AI tools (Goose, Jan, Money Printer Turbo, a DeepSeek harness) as subscription replacements, stressing that the software is free but inference, API keys and hardware still cost money.

- Techniques: Point an OpenAI-SDK client at a local endpoint; Run the DeepSeek harness as a local web app; Semantic-mismatch test for generated video; Read a README past the marketing lines
- Tools: Goose, Jan, Hugging Face, Llama, Gemma, Qwen (transcribed as 'Quen'), Money Printer Turbo, FFmpeg, Pexels, Pixabay, Coverr (transcribed as 'Caver'), Edge TTS

## [The Python YouTuber Who Never Missed an Upload in 7 Years | Better Stack Podcast Ep. 19](../videos/90t4HgAFqZU.md)
`90t4HgAFqZU` · Better Stack · 2026-09-02 · q2 · intro · interview · also: claude-code, models-research, dev-tools

Better Stack podcast with Florian of Neural9 on growing a 500k-subscriber Python channel, daily Claude Code use, the agentic-engineering vs vibe-coding line, and open-weight model claims. Mostly career anecdote, thin on technique.

- Techniques: Minimal, concise CLAUDE.md for Claude Code; Work on a second project while a long agent run finishes; Hand-written proof of concept, then agent implementation; Tiered review: line-by-line for backend, skim for frontend; Learn a new technology by building first; Continue a Claude Code session from a phone; Use uv for all Python package installs
- Tools: Claude Code, Claude Opus 4.8 (as named by speaker), Fable (model, as named by speaker), GLM 5.2 Max (model, as named by speaker), Kimi K3 (model, as named by speaker), LiteRT (Google, formerly TensorFlow Lite), LiteRT.js, TensorFlow, PyTorch, JAX, uv, pip

## [GitHub's #1 Trending Author's New Claude Skill Is Insane](../videos/c47uqR7XB_c.md)
`c47uqR7XB_c` · AI LABS · 2026-09-02 · q2 · practitioner · review · also: testing-verification, skills-self-improvement, multi-agent

AI LABS walks through "unlazy," an agent skill that makes coding agents prove each task is done via a gates ledger, tree decomposition and fresh-agent re-checks, plus their fix for its slow sequential runs.

- Techniques: Gates ledger with verifier command; Recursive tree decomposition with depth cap; Orchestrator re-verifies sub-agent claims; Parallel sub-agents with file ownership in plan.md; Explicit give-up instead of silent drop; Installing unlazy into a project
- Tools: unlazy (agent skill; name as spoken in the video), Claude Code, Codex, Ralph loop, Claude goal command, Opus, GPT 5.6, VS Code, Data for SEO (sponsor), model router skill (generic, unnamed)

## [DeepSeek Harness Just Changed AI Forever](../videos/DTu4yvmc0Fc.md)
`DTu4yvmc0Fc` · Better Stack · 2026-09-02 · q2 · intro · review · also: agent-architecture, observability

Short hands-on tour of an open-source, plugin-first coding harness built on the Cordis framework, covering swappable models, an append-only trajectory log, and adding plugins by prompt. Hype title, thin on setup.

- Techniques: Add a plugin by prompting inside the harness; Use an append-only trajectory log to audit a run; Swap the model provider through plugin config
- Tools: DeepSeek harness (open-source agent harness, desktop app and TUI), Cordis (plugin framework; name as auto-captioned), DeepSeek V4 Pro (model; named in the video), GLM 5.2 (model used as a comparison point), Claude Sonnet 4.5 (in sample provider config), OpenClaw (named as "open claw" in the video), OpenCode (compared for in-prompt customization), QM (a harness the channel covered earlier, name as spoken)

## [xAI are killing it (Grok 4.6, Image 2.0 and more...)](../videos/ILHJqmJdWso.md)
`ILHJqmJdWso` · Better Stack · 2026-09-02 · q3 · intro · review · also: models-research, voice-multimodal, token-cost-efficiency

Better Stack walkthrough of xAI's recent releases: Grok 4.6 benchmarks and cost, Grok Imagine image and video editing, Grok Build and Cursor, and a voice agent builder. Main takeaway: list price is not total cost.

- Techniques: Compare models by cost per completed task, not list price; Element-level re-prompting of a generated image; Multi-image virtual try-on with a template; Voice agent with tools and a phone number
- Tools: Grok 4.6, Grok 4.7, Grok Imagine, Grok Build, GrokBots, Grok voice agent builder, Cursor, Composer 2.5, Cursor auto router, Claude Code, Codex CLI, Claude Cowork

## [Github's Biggest Release In Years. Stacked PRs.](../videos/3Z1xcfF2xlY.md)
`3Z1xcfF2xlY` · Better Stack · 2026-09-02 · q3 · intro · tutorial · also: pr-code-review, dev-tools

Better Stack walks through GitHub's stacked PRs: splitting a large change into a chain of dependent PRs, managing the chain with the gh CLI, and merging the whole stack at once.

- Techniques: Stacked PR workflow with gh stack; Manual stacking without the CLI; Layer the stack by dependency
- Tools: GitHub (stacked pull requests, Merge stack, stack UI), GitHub CLI (gh), with gh stack init / add / submit subcommands, git

## [Want to Run Your Agents For Hours? Use These 12 Rules for Claude.md](../videos/D4uBfIe7SzA.md)
`D4uBfIe7SzA` · Better Stack · 2026-09-02 · q3 · practitioner · tutorial · also: context-engineering, claude-code, testing-verification

Warren from Better Stack walks through 12 rules for a CLAUDE.md file so agents can run longer without constant correction: a living failure log, TDD, clarifying questions, strict types, vetted packages, naming, testing, performance, error handling, and architecture notes.

- Techniques: Failure-log CLAUDE.md with an automated update skill; Size budget for CLAUDE.md, with nesting and skills; Tests as the definition of done; Clarify-before-assuming rule; Strict type rules in CLAUDE.md; Dependency vetting rule; Human-style end-to-end and screenshot verification; Endpoint latency budget and database-first queries; Fail-fast error convention referenced from CLAUDE.md; Architecture lookup table in CLAUDE.md
- Tools: Claude, CLAUDE.md, AGENTS.md, Codex, Claude memory, Chrome, iOS Simulator, Playwright, PostgreSQL, Rust, TypeScript, GitHub

## [This 600M Model Fixes What Whisper Leaves Behind](../videos/jp0PGmAwK3w.md)
`jp0PGmAwK3w` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: local-ai, data-engineering

Super Whisper's open 600M-parameter S1 Mini cleans raw speech-to-text output (fillers, self-corrections, spoken numbers, emails) locally via GGUF and Ollama. English only, early software.

- Techniques: Post-ASR cleanup layer; Local GGUF serving with Ollama; Keep the cleanup model narrow and use a general LLM for everything else; Fully local dictation pipeline
- Tools: S1 Mini (Super Whisper, open 600M model), S1 Voice (Super Whisper, cloud ASR, not covered), S1 Language (Super Whisper, cloud, not covered), Whisper, Whisper.cpp, Parakeet, MLX Whisper, Ollama, llama.cpp, LM Studio, Hugging Face, GGUF

## [DeepSWE: A Contamination-Resistant Coding Benchmark — James Shi, Datacurve](../videos/Yk87oUPVaxU.md)
`Yk87oUPVaxU` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, testing-verification, models-research

Datacurve's DeepSWE talk: a long-horizon coding benchmark with tasks written from scratch to resist PR-mined contamination, plus per-model behavior findings and verifier design lessons.

- Techniques: Original task authoring by domain experts; Behavior-based verifiers; Verifier isolation and history scrubbing; Terse objective-only prompts; Per-model failure-mode analysis; Harness-agnostic base-model comparison; Hybrid verification with LLM judges
- Tools: DeepSWE, SWE-Bench Pro, mini-SWE-agent

## [Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute](../videos/ZTA0GwpAUak.md)
`ZTA0GwpAUak` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: training-finetuning-rl, enterprise-adoption

Samuel Denton (Applied Compute) lays out a 2x2 of offline/online hints and traces for distilling production agents, with SWE-bench and hyperlink-format results showing online hints win on on-policy behavior.

- Techniques: Offline hint on offline production traces; Turn-budget nudge hint; One-step on-policy rollout from an offline trace; Online hint from each rollout; Judge-chosen hint placement with next-step distillation; Relevance-mass token selection (self-distillation)
- Tools: SWE-bench, Qwen 3.5 (thinking model)

## [How Codex Works — Dominik Kundel, OpenAI](../videos/shRR1e2HXMk.md)
`shRR1e2HXMk` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: agent-architecture, context-engineering, sandboxing-execution

OpenAI's Dominik Kundel walks through what happens when a message is sent to Codex: context assembly, sub-agents, computer use, sandboxing, auto-review, WebSocket transport, goal loops and compaction.

- Techniques: Deferred tool loading with tool search; Capping the skills list as a share of the context window; Sub-agent tool set: spawn, send input, wait, shutdown; Code-execution computer use with a persistent REPL; Auto-review sub-agent for escalated actions; Stateful WebSocket transport for agent loops; Goal loop with an explicit done tool; Server-side compaction item
- Tools: Codex, OpenAI Responses API, Codex app server, ripgrep, PowerShell, Node REPL, Chromium, Seatbelt (macOS sandbox), Bubblewrap (Linux sandbox), Cerebras (GPT-5.3 Codex Spark), Ollama, LM Studio

## [Security Track Intro — Randall Degges, Snyk](../videos/2xJoimgoqBg.md)
`2xJoimgoqBg` · AI Engineer · 2026-08-18 · q2 · intro · keynote · also: security-guardrails

Snyk's Randall Degges opens the World's Fair security track: AI-written code has security bugs, autonomous agents need containment, and model access limits are a barrier to shipping fearlessly.
- Tools: Fable (AI model, access reportedly pulled; name as spoken), OpenAI GPT 5.6 (new model, speaker says it is not available to many yet)

## [Through the AI Fog: The Architectural Decision Agentic Security Depends On — Manoj Nair, Snyk](../videos/1EZdpEhwmNc.md)
`1EZdpEhwmNc` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: security-guardrails, mcp-and-tools, evals

Snyk's CTO argues agent security needs deterministic checks alongside LLMs, with customer data on attacks, toxic skills and MCP servers, plus a live coding-agent demo.

- Techniques: Hybrid LLM plus deterministic security checks; Repeated-run recall measurement; Pre-install package health gate; Skill and MCP risk assessment before adoption; Per-model red-team suite; Breakability-aware automated remediation; Deterministic invocation through a skill or hook
- Tools: Claude Code, Cursor Cloud, Codex, Snyk Studio, Snyk Evo, Snyk package health check

## [Loop Engineering from First Principles — Kyle Mistele, HumanLayer](../videos/xIt_mTQp6mY.md)
`xIt_mTQp6mY` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: software-factory, agent-architecture

Kyle Mistele (HumanLayer) argues agent loops should be built as incremental control loops (sensor, controller, actuator) that keep humans reading the code, not blind "Ralph" loops that dump 40k-line PRs.

- Techniques: Sensor, controller, actuator loop for code migration; Deterministic baseline plus per-PR ratchet; Ast-grep as the sensor; Golden-pattern skill for the actuator; Scheduled CI workflow as the loop runner; Feedback file plus comment-triggered re-steering; Single-open-PR flow control
- Tools: Claude Code, ast-grep, GitHub Actions, Effect (TypeScript), React Doctor, OpenClaw, OpenCode

## [Agentic Development Security — Ezra Tanzer, Snyk](../videos/cgimkNGNjvU.md)
`cgimkNGNjvU` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails, claude-code, skills-self-improvement

Snyk on securing agent development in three pillars: the code agents generate, the skills and MCP servers they use, and the actions they take. Mainly a product showcase, with a useful hook-based scanning pattern.

- Techniques: Async post-write scan hook with deferred fix at stop; Steer vs ask policy actions in pre-tool hooks; Static scan of skills and MCP tool descriptions; Per-workspace guardrail profiles
- Tools: Snyk, Claude Code, Codex, Cursor, MCP, Python hooks, VS Code, Electron, ClawHub

## [Guide, Verify, Solve — Anirban Chatterjee, Sonar](../videos/03l29gJXpCE.md)
`03l29gJXpCE` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: testing-verification, pr-code-review, governance-compliance

Sonar's product marketer argues AI-written code needs zero-trust, multilayered verification inside agent loops and in CI/CD, framed as a Guide-Verify-Solve (ACDC) cycle, with vendor product pitches throughout.

- Techniques: In-loop verifier callback with fix-and-rerun; Task-scoped context retrieval for agents; Machine-enforced quality rulebook; Dual PR gate: LLM review plus deterministic scan; Cross-model or cross-method review; Graduated automation of review bots; Remediation agent for backlog debt; Per-task model choice from a quality profile
- Tools: SonarQube, Sonar Vortex, Guitar (AI code-review tool, name from captions), Cursor, Claude Code, Codex, Antigravity

## [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization - May Walter, Hud](../videos/JJGbw4ggaFs.md)
`JJGbw4ggaFs` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: software-factory, observability, context-engineering

May Walter (HUD) shows how HUD runs a weekly agentic workflow on GitHub Actions with Claude Code that mines production traces, scores performance fixes by ROI, verifies them at runtime, and sends a human-readable report to Slack.

- Techniques: Scheduled agentic investigation with runtime verification; Function-level production context map; Query language plus task skills; ROI and risk scoring with a human-readable gist; Vendor-neutral workflow layer; Targeted automatic checks for known performance smells
- Tools: Claude Code, GitHub Actions, MCP, ClickHouse, Slack

## [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../videos/Kz4QJmNrVXU.md)
`Kz4QJmNrVXU` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: context-engineering, multi-agent

Matt Dailey (Ref) argues that AI makes individual engineers faster but not teams, and proposes working in shared docs for decisions, with agents as stateless actions, so humans keep ownership of the product.

- Techniques: Doc as shared state, agents as stateless workers; Two-gear workflow: plan vs polish; Front-load decisions before code; Plan as a portal to the system; Idea exploration before build

## [Perception Agents — Antje Barth, Amazon AGI Lab](../videos/2JX6JYyQG4Y.md)
`2JX6JYyQG4Y` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: voice-multimodal, testing-verification

Amazon AGI Lab's Antje Barth argues computer-use agents need shared screen context and self-verification, then demos open-source annotation and design-spec checking tools for UI work.

- Techniques: Element pointing as agent input; Design-rules verification from a spec file; Meeting transcript to agent to verification pipeline; Perceive, plan, act, then re-check the screen
- Tools: Chrome extension (annotation tool), design rules markdown file (design.md), wearable transcription device, Amazon AGI Lab open-source perception agent harness (GitHub)

## [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../videos/aeTb5BdmTTc.md)
`aeTb5BdmTTc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: context-engineering, enterprise-adoption, skills-self-improvement

How a 10-person team got to shipping with coding agents: treat agent setup as a leadership job, share the best practices, invest in one high-value skill, and close the loop on slop.

- Techniques: Thin CLAUDE.md/AGENTS.md index; Skill as a folder with a short SKILL.md; Runbooks in code comments as discovery hooks; One end-to-end ship-it skill; Nightly code-gardener agent; Shared setup with an opt-out for experiments; First-prompt context audit
- Tools: Claude Code, CLAUDE.md, AGENTS.md, CI/CD, issue boards

## [AI Agents for Performance: Ship Faster, Pay Less — Rajat Shah, Netflix](../videos/CgsWxRUY5Eo.md)
`CgsWxRUY5Eo` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: infra-cost-scaling, pr-code-review, context-engineering

Netflix's playbook for using coding agents on production profiling data to find CPU hot spots, open reviewed fixes, and grow a shared pattern catalog, with a canary gate and an autonomy ladder.

- Techniques: Profile-to-PR agent pipeline; Central anti-pattern catalog in git; Cross-repo sweep for recurring patterns; Canary-gated review; Shift-left catalog injection; Scheduled fixed workflow before autonomy
- Tools: Continuous profilers (sampled call stacks with CPU time), Git and code search across repos, Canary deployment infrastructure, TorchFix (public PyTorch anti-pattern catalog), Spectator (metrics library, named as the source of the counter-object pattern)

## [Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](../videos/7vn4WpqNpck.md)
`7vn4WpqNpck` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, enterprise-adoption

Denys Linkov (Wisedocs) on whether a six-month monorepo refactor of a medical-claims ML pipeline was worth it when coding agents keep improving, and how to measure agent reliability.

- Techniques: Time-horizon reliability check before long runs; Agentic tool-evaluation pipeline; Monorepo consolidation for agent-driven work; Human PRs as a context-building step; Check hidden assumptions in dependencies; Layered refactor instead of a full rewrite
- Tools: Cursor, Temporal, Claude Sonnet 4.6, Claude Opus 4.8, o3, GPT-5.5, Confluence, Claude Code plan mode

## [Your Finance Agent's Bottleneck Is You — Ramana Siddanth Emani, Auditoria AI](../videos/z0sh8HyTrDo.md)
`z0sh8HyTrDo` · AI Engineer · 2026-08-18 · q2 · practitioner · talk · also: software-factory, multi-agent, governance-compliance

Auditoria AI speaker says human attention bottlenecks agent work: use parallel worktree subagents, skills, one-pane UX, goals and loops, and self-improving harnesses, keeping humans at intake and sign-off.

- Techniques: Worktree-per-task parallel subagents; Ticket-to-stage pipeline with two human gates; Encode organizational procedure as skills; Single-pane minimal UX for orchestration; Daily self-retrospective on the agent's own loop; Goals plus loops, monitored from a phone; Background dreaming for pattern compaction
- Tools: Claude Code, git worktrees, Kubernetes, Docker, Jira, GitHub, MCP

## [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../videos/il1c1a2FufU.md)
`il1c1a2FufU` · AI Engineer · 2026-08-18 · q4 · practitioner · workshop · also: context-engineering, skills-self-improvement, multi-agent

Jason Liu (OpenAI) shows how he runs Codex as a personal ops system: pinned long-lived threads, a git-tracked memory vault, heartbeats, and goal verifiers. Main takeaway: compaction makes long threads workable.

- Techniques: Long-lived pinned thread per workstream; Heartbeat / loop in the same thread; /goal with a verifier and file-backed goal; App shot plus accessibility tree; Git-tracked personal memory vault with agents.md routing; Monitor thread that spawns per-issue threads; Skill from one completed run, with self-edit permission; Annotate a localhost preview to steer the agent; Model and reasoning tiering
- Tools: Codex app, Codex CLI, Codex in-app browser, computer use, Chrome extension, Slack connector, Gmail connector, Google Drive connector, Notion, Linear, Obsidian, GitHub

## [Content Is Code - Matt Palmer, Conductor](../videos/yv6xovSsB1U.md)
`yv6xovSsB1U` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: product-ux, context-engineering

Matt Palmer (Conductor) argues code is becoming the medium for technical content, so docs, changelogs and product videos should be generated from a structured source of truth.

- Techniques: Generate product tour videos with React and Remotion; Derive changelogs and product updates from the diff; Keep design tokens separate from app code; Write internal docs and skills for agents
- Tools: React, TypeScript, Remotion, CSS, HTML, Claude

## [Multiplayer agentic engineering — Arjun Singh, Superconductor](../videos/OL7kfezynJM.md)
`OL7kfezynJM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: software-factory, sandboxing-execution

Arjun Singh (Superconductor) on making agent work multiplayer: one shared session across Slack, desktop, mobile and GitHub, cloud sandboxes, and benchmarking agents on your own codebase.

- Techniques: Cloud sandbox per project; Same session across interfaces; Artifacts as proof of work; Meeting bot as an idea-to-ticket intake; Acceptance-criteria fields in the ticket form; Network egress allowlist with grant prompts; Scoped credentials instead of ambient access; Codebase-specific agent benchmark; Switch defaults on evidence
- Tools: Claude Code, Codex, Cursor, Slack, GitHub, Linear, Sentry, Notion, Google Meet, Zoom, Microsoft Teams, GLM 5.2

## [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../videos/iQ5xldZ9StU.md)
`iQ5xldZ9StU` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: software-factory, security-guardrails, sandboxing-execution

GitHub Next demos Agentic Workflows (markdown playbooks compiled to Actions with deterministic guardrails) and ACE, a cloud multiplayer dev environment where humans and agents share chat and plans.

- Techniques: Markdown playbook compiled to CI workflow; Declarative guardrail front matter; Secret brokering outside the agent sandbox; Staged, logged writes; Swarm of role-specific workflows; Shared cloud session per branch with team chat as context; Shared markdown plan as contract; Automation triage by stack trace origin
- Tools: GitHub Copilot, GitHub Actions, Dependabot, Astro, Cloudflare, ACE (GitHub Next prototype)

## [This New Skill Finally Solves Thinking For AI Agents](../videos/m6IXL_YGqBQ.md)
`m6IXL_YGqBQ` · AI LABS · 2026-08-02 · q2 · intro · review · also: multi-agent, testing-verification, skills-self-improvement

AI LABS walks through a community "ADHD" skill that makes a coding agent ideate by fanning out isolated sub-agents, each seeded with a different frame, then scoring and merging the results; shown for test planning and pre-ship UX/churn review.

- Techniques: Frame-diversified tree-of-thought fan-out; Three-question gate before auto-invoking an expensive fan-out; Install an agent skill from a repo and fix the config folder for Claude Code; TDD test-strategy planning with PRD and tech spec linked in CLAUDE.md; Pre-launch UX and churn review by fan-out
- Tools: Claude Code, Codex, Cursor, CLAUDE.md, .agents folder (installer target), SKILL.md, Top View (sponsor; AI video skill), Kling, Sea Dance, Nano Banana

## [OmniRoute + Claude Code is INSANE (Why I Cancelled My Claude Code Subscription)](../videos/k26fT4athQs.md)
`k26fT4athQs` · Kai Explains · 2026-08-02 · q2 · intro · review · also: token-cost-efficiency, infra-cost-scaling

A host explains dropping a Claude Code subscription for OmniRoute, a self-run gateway that routes Claude Code to many providers with fallback, token compression and free tiers, and says when to keep a paid Opus key.

- Techniques: Local OpenAI-compatible gateway in front of a coding agent; Mid-request provider fallback; Tool-output compression before the model call; Per-task model routing with a paid escape hatch; Semantic cache for repeated questions
- Tools: OmniRoute (also captioned as OmniRoot; self-hosted LLM gateway, version not stated), Claude Code (agent CLI), Anthropic Claude Opus (paid model for hard tasks), RTK (token-compression pass), Caveman (token-compression pass), MCP (gateway ships about 94 built-in tools over Model Context Protocol)

## [Jack Dorsey's New App Is Coming for Slack and GitHub (buzz)](../videos/CHEMPZ87FLw.md)
`CHEMPZ87FLw` · Better Stack · 2026-08-02 · q3 · intro · review · also: multi-agent, security-guardrails, token-cost-efficiency

Hands-on walkthrough of Block's open-source Buzz, a Slack-like workspace for humans and AI agents built on Nostr with signed audit trails. Covers agent setup, a two-model coding contest, and a warning about runaway token use.

- Techniques: Bootstrap a Buzz community; Custom agent with persona, harness and model; Head-to-head model contest, then cross-model audit; Stop runaway multi-agent loops
- Tools: Buzz, Nostr protocol (the video says 'Noster'), Nostr relay (Block's hosted relay, in beta), BitChat (Bluetooth mesh app that adopted Nostr 2 as a fallback transport), Agent Client Protocol, Claude Code, OpenAI Codex, Goose (Block's agent framework), OpenRouter, Gemini 3.6 Flash (as named in the video), GLM 5.2 (as named in the video), GPT 5.6 Sol (as named in the video)

## [5 Open Source AI Tools That Feel ILLEGAL To Know About](../videos/-UxcljWN49I.md)
`-UxcljWN49I` · Kai Explains · 2026-08-02 · q2 · intro · review · also: agent-architecture, memory, voice-multimodal

Roundup of five open-source agent building blocks (Browser Use, Firecrawl, Mem0, OpenHands, Dify) mapped to read, act, remember, code and orchestrate roles. Mostly star counts and vendor stats, with no hands-on steps.

- Techniques: Read-decide-act browser agent loop; Scrape-to-markdown before retrieval; Two-phase memory: extract on write, retrieve on read; Sandboxed plan-write-test-iterate coding loop; Per-step tracing and worker queues for visual workflows
- Tools: Firecrawl (transcribed 'fire crawl'), Browser Use, Mem0 (transcribed 'Memzero'), OpenHands (transcribed 'open hands'), Dify (transcribed 'DeFi'), Devin (transcribed 'Devon'; Cognition AI, mentioned as a $500/month closed product), WebVoyager (benchmark, 586 tasks), SWE-bench (benchmark), Langflow (mentioned as Dify's origin comparison), OpenTelemetry (Dify export)

## [This is basically an X-ray for your codebase...](../videos/Y_7_rbtQXcs.md)
`Y_7_rbtQXcs` · Better Stack · 2026-08-02 · q3 · intro · review · also: observability, evals

Short Better Stack walkthrough of MindWalk v0.3, a 3D session replay for Claude Code and Codex runs, with an LLM judge that grades how the agent explored, stayed in scope and verified its work.

- Techniques: Color-coded session replay of file access; LLM-judge rubric over a whole agent session; Timeline event markers for multi-agent runs; Choose the review lens by change size
- Tools: MindWalk v0.3, Claude Code, Codex, Three.js, Graphify (named as a comparison, not evaluated)

## [Open Source Is Back. Goodbye Claude.](../videos/wOfm7x0i3sw.md)
`wOfm7x0i3sw` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: token-cost-efficiency, multi-agent, claude-code

Better Stack walkthrough of OpenCode, an open-source terminal coding agent with bring-your-own models and custom subagents, weighed against Claude Code; the cost verdict depends on whether you pay per API token or hold a subscription.

- Techniques: Pin a cheap model to a specialist subagent; Low-temperature review subagent; Same agent definition in one JSON file; Enable LSP for type-aware feedback; Generate AGENTS.md with /init; Plan then build
- Tools: OpenCode, Ghostty, models.dev, big pickle (free default model in OpenCode), GLM 5.2, DeepSeek 4, Claude Sonnet 4, Fable 5 (named as a comparison model), Claude Code, GitHub Copilot (comparison), Design Arena (benchmark), AGENTS.md

## [How To Use Codex To Build Insanely Beautiful Websites Using GPT 5.6 Sol](../videos/pHstb0JGGhE.md)
`pHstb0JGGhE` · AI LABS · 2026-08-02 · q3 · practitioner · tutorial · also: vibe-coding-app-building, context-engineering, skills-self-improvement

Seven-stage tutorial for building a non-generic landing page with the Codex app and GPT 5.6, using AGENTS.md, a design skill, a design.md brand file, generated images, and a deploy step. Main lesson: encode taste and brand in files, not in each prompt.

- Techniques: Scoped seed prompt; AGENTS.md via /init, plus a self-verify rule; Install a design skill and forbid the default one; Browser verification loop; design.md brand system; Plan-mode image generation into an assets folder; Screenshot-based layout cloning; Single-section component swap; Performance pass; Local commits as checkpoints; Deploy with the site skill
- Tools: Codex (in the ChatGPT app), GPT 5.6, GPT image model, Next.js, AGENTS.md, GPT Taste skill, OpenAI site skill, Anthropic front-end design skill, design.md (format introduced by Google through Stitch), Aura Build design.md library, 21.dev, Godly components

## [Qwen 3.6 + Ollama is INSANE: Better than Claude Code (FREE + Local + open Source)](../videos/qS5ZUEaKwNw.md)
`qS5ZUEaKwNw` · Kai Explains · 2026-08-02 · q3 · intro · review · also: local-ai, token-cost-efficiency

Kai runs Alibaba's open Qwen 3.6 locally through Ollama and Qwen Code against Claude Code on three same-prompt builds; local wins on privacy, cost and offline use, but loses on finish and wiring.

- Techniques: Point Qwen Code at a local Ollama model; Raise the Ollama context window before running an agent; Smoke-test the agent loop before real work; Compare agents on the same prompts, judged by behavior; Route by lane: local for private, offline or cheap work; cloud for complex repos
- Tools: Qwen 3.6 (Alibaba open-weights model; sizes from 2B to 122B per transcript), Qwen Code (Alibaba's open-source agentic coding harness), Ollama (local model server, default context 4,096), Claude Code (Anthropic, cloud comparison, $200/month Max plan), Qwen 3.5 (earlier model, mentioned), Three.js (used in the aquarium task)

## [Kimi K3 Is Fable Level... (they should be worried)](../videos/QfCpRTLSOB4.md)
`QfCpRTLSOB4` · Better Stack · 2026-08-02 · q3 · intro · review · also: models-research, token-cost-efficiency

Hands-on one-shot app tests of open-weight Kimi K3 against Fable 5, GPT 5.6 Sol and GLM 5.2: near-frontier output and per-task cost, but single runs and harness effects muddy the result.

- Techniques: One-shot app bake-off; Separate harness effects from model effects; Name the stack in the prompt when it matters; Rank models by cost per completed task; Disable unrequested auto-hosting
- Tools: Kimi K3, Kimi Code CLI, OpenRouter, Claude Code, Fable 5, GPT 5.6 Sol, GPT 5.6 Terra, GPT 5.6 Luna, GPT 5.5, Opus 4.8, Sonnet 5, K2.6

## [The Largest Supply Chain Attack Ever Just Infected Go](../videos/lNsSxWQDqaU.md)
`lNsSxWQDqaU` · Better Stack · 2026-08-02 · q3 · practitioner · news · also: security-guardrails, claude-code, dev-tools

Better Stack explains how the self-replicating npm worm (Shai-Hulud) jumped to a Go module, hiding hooks in Claude Code and VS Code config so code runs on folder open, and lists five hardening steps.

- Techniques: Audit agent and editor config before opening untrusted code; Turn off VS Code automatic tasks; Treat .claude/ and .vscode/ as executable code in review; Short-lived, least-privilege CI credentials via OIDC; Egress filtering on CI runners; Minimum release age for packages; Keep secrets out of plaintext on dev machines
- Tools: npm, Go modules, Claude Code (called 'clawed code' in the auto-captions), VS Code (tasks.json, folder-open tasks), Bun (runtime the payload uses to stage its code), Node.js (runs the setup script), TruffleHog (secret scanner the worm reuses), GitHub Actions (CI workflows named as the risk surface), Socket.dev (security firm that flagged the wave), CrowdStrike, Microsoft Defender, SentinelOne (endpoint products the malware checks for), OIDC (short-lived CI credentials), .npmrc (minimum release age setting)

## [OpenAI Sol Ultra Just BEAT Claude Fable](../videos/27QLmUQvL2A.md)
`27QLmUQvL2A` · Better Stack · 2026-08-02 · q2 · intro · news · also: models-research, multi-agent, evals

Better Stack on GPT-5.6 Sol and its Ultra sub-agent mode: 91.9% Terminal-Bench 2.1, METR caught heavy test-gaming, Sol costs about half of Claude Fable 5.

- Techniques: Tiered model routing by task weight; Discount benchmark leads when the independent evaluator disputes them; Watch unattended runs for test-gaming
- Tools: OpenAI Codex, GPT-5.6, GPT-5.5, Sol, Terra, Luna, Sol Ultra (Ultra mode), Terminal-Bench 2.1, Claude Mythos 5, Claude Fable 5, METR time-horizon evals, Cerebras chips

## [Postgres was rewritten in Rust… and somehow passed every test](../videos/WvfacC0FtbE.md)
`WvfacC0FtbE` · Better Stack · 2026-08-02 · q3 · intro · review · also: dev-tools

Better Stack reviews PG Rust, a from-scratch Rust reimplementation of Postgres that passes the official regression suite but is not production ready, with its headline performance claims unverified.

- Techniques: Use an upstream regression suite as the compatibility oracle; Smoke-test compatibility with unmodified clients; Check on-disk compatibility by booting an existing data directory; Triage performance claims by asking for the code or benchmark
- Tools: PG Rust (Postgres 18.3 compatible target), PostgreSQL, Docker, psql, Bun (mentioned as another Rust rewrite), CockroachDB, YugaByte, GitHub, Hacker News

## [Bun Moved To Rust... Zig's Creator Fired Back](../videos/0TSxrzBVEwQ.md)
`0TSxrzBVEwQ` · Better Stack · 2026-08-02 · q4 · practitioner · news · also: multi-agent, software-factory, testing-verification

Bun ported its ~1M-line codebase from Zig to Rust in 11 days using parallel Claude agents with an implementer, two adversarial reviewers and a fixer; the video also covers Zig creator Andrew Kelly's public criticism.

- Techniques: Adversarial review loop per unit of work; Porting spec plus lifetime table before code generation; Faithful port over idiomatic rewrite, all at once; Guardrails for parallel agents on one git repo; Sharding by git worktree; Error-driven crate-by-crate loop; Reviewer rule against justified workarounds; Test-file batch loops as the verification step
- Tools: Bun (1.3.14 final Zig release, 1.4 Rust), Zig, Rust, Claude / Claude Code, Fable 5 (pre-release model, as named in the video), cargo, git (worktrees), Next.js (dev-server hot reload test), JavaScriptCore, TigerBeetle (referenced by Kelly), Hacker News / GitHub (where the porting doc was noticed)

## [Grok Was Caught Uploading Your Entire Codebase](../videos/n6DIs13ilvU.md)
`n6DIs13ilvU` · Better Stack · 2026-08-02 · q3 · intro · news · also: security-guardrails, governance-compliance

Better Stack summarizes reports that Grok's coding CLI uploaded whole repos, git history and env vars to xAI, what xAI changed afterward, and why the /privacy toggle is not real local protection.

- Techniques: Audit a CLI's uploads with a MITM proxy; Grep CLI logs for upload sessions; Rotate secrets if an upload is confirmed; Harden the CLI config and verify the flags
- Tools: Grok CLI (Grok Build), xAI API / account settings, MITM proxy, Claude Code, Codex, Gemini CLI

## [7 Rules To Use GPT 5.6 Sol Better Than 90% Of People](../videos/STczJBYJf7w.md)
`STczJBYJf7w` · AI LABS · 2026-08-02 · q3 · practitioner · review · also: context-engineering, multi-agent, token-cost-efficiency

AI LABS' four-day hands-on comparison of GPT 5.6 Sol and Fable: Sol is better at finishing long autonomous work and screen-based review, Fable at deciding what to build, plus seven usage rules.

- Techniques: Git checkpoint before a long autonomous run; Codex app sandbox and approval configuration; Single-session delegation of multi-session work; Role-by-role journey review after the build; One-instruction-removal test for prompts and skills; Plan with one model, build with another
- Tools: GPT 5.6 Sol, GPT 5.6 Terra, GPT 5.6 Luna, Ultra (Sol multi-agent mode), Codex (app and CLI), ChatGPT app, Fable, Opus 4.8, Opus, Sonnet, Qwen 3.6, Cursor

## [Build Your Own Fully Private Local AI Stack (Chat, RAG, Coding Agent & Automation)](../videos/np8booSU7Og.md)
`np8booSU7Og` · Kai Explains · 2026-08-02 · q3 · practitioner · tutorial · also: local-ai, rag-retrieval, agent-architecture

Kai Explains walkthrough of a fully local AI stack: llama.cpp behind one OpenAI-compatible endpoint, with AnythingLLM for chat and RAG, Pi as a local coding agent, and n8n for email automation.

- Techniques: Single OpenAI-compatible endpoint as the integration bus; llama-server router preset mode, with LlamaSwap as fallback; Headless AnythingLLM in Docker, configured from the UI; Local RAG with AnythingLLM defaults; Pi as a local coding agent; n8n email triage with a local model; Always-on home lab hardening
- Tools: llama.cpp, llama-server, LlamaSwap, AnythingLLM, Open WebUI, LanceDB, Pi (coding agent, npm), OpenCode, n8n, Docker, Docker Compose, Portainer

## [This Skill Just Made Kimi K3 a 10X Better Designer](../videos/EwTOiqWWqEc.md)
`EwTOiqWWqEc` · AI LABS · 2026-08-02 · q2 · practitioner · review · also: claude-code, skills-self-improvement, vibe-coding-app-building

Walkthrough of running Kimi K3 inside Claude Code via a local proxy on a Kimi subscription, then using the Hallmark anti-slop design skill to push Kimi, Opus and Codex off their default visual styles.

- Techniques: Run a non-Claude model inside Claude Code via a local subscription proxy; Install Hallmark for the right agent; Invoke a skill manually with its slash command when the model is not Claude; Prompt Hallmark with the three pre-flight answers; Run the audit verb, then pick which findings to fix; Use the study verb, not a clone request; Manage context manually on long design sessions
- Tools: Kimi K3, Kimi Code, Claude Code, Codex, Codex app, CLIProxy API, Hallmark, Next.js, Opus 4.8, Sonnet 4.5, GPT 5.6, Fable 5

## [Best Local Agent Harness Right Now (My Top 3)](../videos/YgyyWDGeQWM.md)
`YgyyWDGeQWM` · Kai Explains · 2026-08-02 · q3 · intro · review · also: local-ai, agent-architecture, context-engineering

A survey of local/open coding-agent harnesses (OpenCode, Aider, Pi, plus OpenHands, Cline, Goose) arguing the harness now matters more than the model, with local-model pairing advice and a warning that the list goes stale fast.

- Techniques: Git-native atomic AI commits (Aider); Mid-session model downgrade for cost; Lazy-loaded skill blocks to keep the base prompt small (Pi); Custom subagents with per-agent model and permissions (OpenCode); Parallel agents on one GPU via vLLM; Local model sizing by memory footprint; Pre-standardization vetting checklist
- Tools: OpenCode (172k+ GitHub stars per speaker; 1.68M weekly npm installs as of June 2026), Aider, Pi (by Armin Ronacher), OpenClaw, OpenHands (spoken as 'Open hands'), Cline (spoken as 'Klein'), Goose, Roo Code (archived May 2026), Gemini CLI, Claude Code, Claude Opus 4.8, GPT-5.5

## [Opus 5 Beats Fable... at Half the Price?](../videos/56wK2ttgIsc.md)
`56wK2ttgIsc` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: models-research, token-cost-efficiency

Single-run tests of Claude Opus 5 against Fable 5, GPT 5.6 Sol and Kimi K3 on one-shot app builds plus benchmarks: Opus leads on UI and agentic scores, but its cost per run is close to Fable's.

- Techniques: Compare models on cost per completed task, not per-token price; Estimate a subscription-billed run's cost from usage data; One-shot app bake-off; Check whether the prompt or the model chose the stack
- Tools: Claude Opus 5, Claude Opus 4.8, Claude Fable 5, Claude Mythos 5, Claude Max, Claude Pro, Claude Code (usage tool), GPT 5.6 Sol, Kimi K3, ARC-AGI, FrontierBench, GDPVAL

## [Fleet Engineering Is Insane... The Next Evolution Of Vibe Coding](../videos/qxjII6x2yPY.md)
`qxjII6x2yPY` · AI LABS · 2026-08-02 · q2 · practitioner · tutorial · also: multi-agent, claude-code, sandboxing-execution

Walkthrough for running many Claude Code sessions in parallel: resume and handoff basics, file ownership, background dashboards, git worktrees, issue-driven orchestration, and Docker Sandbox isolation.

- Techniques: Session recovery with continue, resume, recap, export; File ownership by prompt; Plan-mode task decomposition; Handoff documents via the handoff skill; Background sessions and the agent dashboard; Git worktrees per session; Issue-driven background orchestration; Docker Sandbox for isolated execution with clone mode
- Tools: Claude Code, Claude Code plan mode, Claude Code background sessions, Claude Code agent dashboard, handoff skill, git worktrees, OpenAI Symphony, Codex, Linear, GitHub, Docker Sandbox (sbx), Docker micro-VM sandboxes

## [Grok 4.5 Was Trained on YOUR Cursor Sessions (What SpaceX Isn't Telling You)](../videos/hdWUv2V1jRg.md)
`hdWUv2V1jRg` · Kai Explains · 2026-08-02 · q3 · intro · news · also: security-guardrails, models-research, governance-compliance

Commentary arguing Grok 4.5 was partly trained on Cursor user sessions captured while privacy mode was off by default, and that behavioral coding data is now the valuable asset.

- Techniques: Audit training and privacy settings in each AI coding tool; Treat codebase-derived vendor benchmarks as possibly contaminated; Scan launch posts for buried data-use disclosures
- Tools: Cursor, Grok 4.5, CursorBench, SWE-Bench Pro (transcribed as "WE Bench Pro"), Terminal Bench 2.1, Fable (model, as named in transcript), Opus 4.8, Opus 4.7, GPT 5.5

## [Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI](../videos/ZpK5PWX2YRM.md)
`ZpK5PWX2YRM` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: pr-code-review, testing-verification, software-factory

Alex Volkov on the "Z/L continuum" for how much agent-written code engineers should read in 2026: route review effort by the proof a change needs, not by a blanket rule.

- Techniques: Risk-tiered review routing; Decompose into atomic PRs with agents; Separate writer, inspector and test author; Turn review findings into system rules; Ask the agent where the critical code is; Loops with verification and retry
- Tools: Claude Code, Codex, OpenClaw, Pi, Antigravity, Grok Code

## [A Song of Types and Agents - Roberto Stagi, Ratel](../videos/UlFB6efYN5Q.md)
`UlFB6efYN5Q` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: agent-architecture, dev-tools

Roberto Stagi argues TypeScript is overtaking Python for the agent and application layer, because coding agents default to it, npm is deep, and one Zod schema can type the whole stack; Python keeps training and serving.

- Techniques: Shared Zod schema across the full stack; Single-language monorepo for agent apps; Split by layer: Python for training and serving, TypeScript for the app and agent layer
- Tools: TypeScript, Python, Zod, npm, Vercel AI SDK, FastAPI, React, Claude Code, Cursor, Codex, Lovable

## [Claws Out: Securing and Building with OpenClaw - Nick Taylor, Pomerium](../videos/xg1zNlzw7Jk.md)
`xg1zNlzw7Jk` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: security-guardrails, mcp-and-tools

Nick Taylor (Pomerium) on hardening the OpenClaw control plane with trusted-proxy auth, then a live demo of building a UI-bearing MCP app for ChatGPT by editing its workspace from Discord on his phone.

- Techniques: Identity-aware proxy as the auth layer for an agent control plane; Live-edit an MCP app from chat; Widget-to-LLM calls via the MCP apps send-message function; Narrow write access for agent-driven PRs; Test the unauthenticated or fresh-install path
- Tools: OpenClaw, Pomerium, ChatGPT apps (MCP apps), MCP, React, Vite, Discord, Telegram, WhatsApp, Caddy, NGINX, GitHub CLI

## [Agents Building Agents - Alfonso Graziano, Nearform](../videos/aHhB3sjGjkI.md)
`aHhB3sjGjkI` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: evals, skills-self-improvement, observability

Alfonso Graziano (Nearform) shows coding agents improving other agents: an eval-driven loop lifts a toy agent from 18% to 83% and a production agent from 67% to 86%, and a trace-clustering loop turns live user feedback into fixes.

- Techniques: Golden dataset plus scorers as the agent test suite; Baseline report before the optimization loop; Branch-per-hypothesis improvement loop with rollback; Protected eval set in the optimizer instructions; Reading the agent's full traces, including thinking traces, for root cause; Trace clustering from live feedback; Packaging the analysis as a reusable skill; Failure mode to spec to golden-set entry
- Tools: Claude Code, Mastra, auto-agent (the speaker's own internal tool, not public)

## [remobi.app: Don't change your terminal workflow for mobile](../videos/5192csoTkVo.md)
`5192csoTkVo` · AI Engineer · 2026-07-18 · q2 · intro · demo · also: dev-tools, product-ux

Connor Adams demos Remobi, an open-source progressive web app that gives phone access to tmux sessions running Claude Code and other coding agents, reached over a private network such as Tailscale.

- Techniques: tmux as the agent session host; Private-network remote access to a dev box; Gesture-mapped terminal UI; Diff review in a side window; Skill-driven environment setup
- Tools: Remobi, tmux, Tailscale, Cloudflare Tunnels, ngrok, Claude Code, Happy, lazygit, critique, agent-browser, npm, Conductor

## [Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com](../videos/MpZzWMdmQCE.md)
`MpZzWMdmQCE` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: testing-verification, claude-code, agent-architecture

Talha Sheikh (Checkout.com) argues coding agents need deterministic, shareable verification hooks, not better instructions, and that the real engineering work is designing the verification harness.

- Techniques: Stop-hook deterministic verifier; Fail-and-retry feedback loop; Layered enforcement at multiple points; Language-agnostic check contract; Executor plus advisor loop; Cheap model plus strong harness
- Tools: Claude Code, Claude Code hooks (Stop hook), VectorV1 / Vector Harness, Haiku, Opus, Anthropic Glasswing / Project Mythos (named, not described)

## [500 people vibe-coded for 30 days. I was one of them. - Sanja Grbic, Automattic](../videos/UcYoMg-8-L8.md)
`UcYoMg-8-L8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: enterprise-adoption, vibe-coding-app-building, product-ux

Automattic's 30-day "Radical Speed Month" experiment, in which about 500 people in paired teams shipped roughly 794 projects, and how the speaker moved from designer to design engineer by prototyping in code before Figma.

- Techniques: Time-boxed paired ship sprint; Prototype-in-code before design tool; Shared file-based exploration log; Aggregating scattered sources into a status tracker; Engineer as enabler in mixed-skill pairs
- Tools: Claude Code, Figma, Storybook, GitHub, Nano Banana, Context MCP server, WordPress.com, Jetpack, WooCommerce

## [HTML is All You Need (for Agents to Make Graphics) - Amol Kapoor, Nori](../videos/JRTAtZ5iBkU.md)
`JRTAtZ5iBkU` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: product-ux, vibe-coding-app-building

Amol Kapoor (Nori) argues agents fail at graphics because of the medium, not the model, and that HTML is a better authoring format than canvas tools or SVG for slides, docs and video.

- Techniques: HTML as the agent's authoring format for visual artifacts; Pick the format the model is strongest in, separate from the delivery format; Ground the artifact in source data, not in the layout; Avoid screenshot-and-replace loops and canvas-driving tools for agents
- Tools: HTML, CSS, SVG, Figma MCP, PowerPoint CLI, PDF export, Nori Sessions

## [The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI](../videos/pMggiOb18tc.md)
`pMggiOb18tc` · AI Engineer · 2026-07-18 · q3 · intro · keynote · also: multi-agent, software-factory, agent-architecture

OpenAI's Codex team argues engineers move from watching agents to running manager-worker loops, with human attention as the scarce resource to spend on the outer loop.

- Techniques: Long-lived manager agent over worker agents; Trigger-driven manager wake-ups; Offload test runs to a separate machine; Server-side compaction for long tasks; Parallel attempts with a fast, strong model; Shared instruction file across agents; Chat-first UI with escalation to direct editing
- Tools: Codex, Codex app, Codex Cloud, Responses API, AGENTS.md, OpenClaw, OpenCode, Cerebras, VS Code extension, Xcode, JetBrains, Slack

## [ReviewDebt: a practical framework for scoring every pull request — Sachin Gupta, Ebay](../videos/TJPInBjhE4Q.md)
`TJPInBjhE4Q` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: pr-code-review, evals, governance-compliance

Sachin Gupta (eBay) argues coding agents create unmeasured review debt and offers a deterministic 0-100 PR review-burden score built from five signal families, plus a rollout plan.

- Techniques: Deterministic review-burden score; Backfill calibration; Non-blocking rollout ladder; Shape rules for agent PRs; Authorship detection as a weak amplifier
- Tools: GitHub, GitHub Copilot, Codex, Cursor

## [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON](../videos/4kYl2_mqmnQ.md)
`4kYl2_mqmnQ` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: multi-agent, claude-code, context-engineering

A KRAFTON engineer runs AI coding agents across three machines, organizes them as a hierarchy, keeps state in files, and lists the five failures and four open problems that followed.

- Techniques: Agent org hierarchy with scoped context; File-backed agent state with handoff folders; Clear-and-reload instead of compaction; Blocking review gateway with approval hook; Force delegation through a CLI harness; Git-based context sync with per-machine partitions; Single always-on control plane and chat router; Boot command that restores the fleet from state files
- Tools: Claude Code, tmux, tmux capture-pane, SSH, Git, Discord, MCP servers, Kubernetes, Linux, macOS

## [Field Guide to Fable — Thariq Shihipar, Anthropic](../videos/9fubhllmsBU.md)
`9fubhllmsBU` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: claude-code, context-engineering, models-research

Anthropic's Thariq Shihipar gives a practical field guide to working with the Fable model: unhobble Claude with tools, find your unknowns, stay in the loop, and be less reasonable about trade-offs.

- Techniques: Blind-spot pass; Brainstorm via throwaway prototypes; Interview me before building; Reference as the map; Implementation-note log for unknowns; Quiz the agent on its own work; Shrink the system prompt for newer models; Give the agent a tool rather than more context
- Tools: Claude Code, Bash tool, code execution tool, AskUserQuestion tool

## [Your agent is blindfolded — Johan Lajili, Poolside AI](../videos/iRcX54EO5g8.md)
`iRcX54EO5g8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: testing-verification, context-engineering

Johan Lajili (Poolside) argues agent trust comes from verification: give agents a CLI to drive and test the app, make them reproduce bugs before fixing, and make the codebase easy for AI to check.

- Techniques: Reproduce-first gate; App-driving CLI for non-web apps; Token-compressed UI snapshot; Let the agent discover its own UI problems; Periodic self-review of logs and repeated actions; Human-like exploratory testing by the agent
- Tools: Poolside internal app-testing CLI (unnamed), VS Code extension, G-Stack (mentioned as an existing tool for screenshots and snapshots)

## [Understanding is the new bottleneck — Geoffrey Litt, Notion](../videos/WkBPX-oDMnA.md)
`WkBPX-oDMnA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: testing-verification, product-ux, skills-self-improvement

Geoffrey Litt (Notion) argues humans must still understand agent-written code to stay creative participants, not only to verify it, and shows explainer docs, comprehension quizzes, agent-built micro-worlds and shared spaces for doing so.

- Techniques: Explainer doc per agent change (ExplainDiff-style skill); Comprehension quiz gate before sharing code; Intuition-first, literate ordering; Agent-built micro-world debugger; Step-through simulation for a migration; Shared threads and commentable docs with agents
- Tools: Claude Code, Claude, Cursor, Notion, Notion HTML blocks

## ["Software engineering is not about writing code" — Benoit Schillings, Google DeepMind VP of Research](../videos/1P1hJ36rxM0.md)
`1P1hJ36rxM0` · AI Engineer · 2026-07-18 · q3 · intro · review · also: evals, models-research

A Google DeepMind research VP argues code is now nearly free to write, so the bottlenecks move to specification, verification, architecture and open-ended evals, with self-play replacing scarce human code data.

- Techniques: Self-play with verifiable coding challenges; Open-ended scored eval instead of pass/fail; Shift the correctness burden to the language or type system; Decompose before generating; Generate correct code directly instead of detect-and-patch
- Tools: Gemini, Google DeepMind research stack (unnamed), AlphaZero (reference point), Python, Lean (proof assistant, referenced as inspiration), Mythos (model that found vulnerabilities, referenced in news), GitHub (as the source of public code), Pitchfork (internal ML-for-code project started at Google X in 2018)

## [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI](../videos/Rx8f05JI_WA.md)
`Rx8f05JI_WA` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: evals, testing-verification, security-guardrails

Rishi Desai presents SWE-Marathon, 20 project-scale coding tasks where the best agent solves only 26%, and argues that multi-channel, anti-cheat verification is the main bottleneck for long-horizon evals.

- Techniques: Multi-channel verification; Strace-based forbidden-subprocess detection; Hardening loop before publishing a benchmark; Standardize tasks into a Harbor-format environment; Trajectory work-pattern charts
- Tools: SWE-Marathon, Harbor, HumanEval, SWE-bench, Terminal-Bench, Claude Opus 4.8, Claude Code, GPT-5.5 (transcribed as 'gbd 5.5'), Codex, GLM 5.2, Gemini, strace

## [We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco](../videos/dRmWYHuIJxM.md)
`dRmWYHuIJxM` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: token-cost-efficiency, context-engineering, rag-retrieval

Rajkumar Sakthivel (Tesco) on cutting AI coding-tool token spend by sending less context: a local code index with hybrid search, slimmed results and a relevance threshold, reporting about 94% fewer input tokens on one small benchmark.

- Techniques: Code-aware chunking; Parallel hybrid retrieval; Result slimming; Call-graph expansion; Heuristic relevance gate instead of LLM self-grading; Shared local index across tools; Per-query savings accounting
- Tools: Claude Code, Cursor, GitHub Copilot, Codex, CCE (speaker's free open-source local code index; name as spoken)

## [From Writing Code to Designing Systems: How the Developer Role is Changing — Chris Noring, Microsoft](../videos/GdvKNwMcfd0.md)
`GdvKNwMcfd0` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: context-engineering, software-factory, multi-agent

Microsoft's Chris Noring on moving from writing code to running agents: start in the CLI, use AGENTS.md, skills and custom agents as guardrails, and delegate background work that comes back as draft PRs for human review.

- Techniques: Layered repo guardrails (AGENTS.md, skills, custom agents); Tools allowlist to constrain an agent; Delegate to a background cloud agent that returns a draft PR; Parallel terminals as a scaling model; Ask the agent to write its own skill or instructions
- Tools: GitHub Copilot CLI, Claude Code, Claude Desktop, VS Code, GitHub Copilot cloud agent, GitHub MCP server, Playwright MCP, AGENTS.md, SKILL.md skills, custom agents (.github/agents)

## [Respect The Process - Andrew Dumit, Watershed Technology Inc.](../videos/CLttOU7n6sI.md)
`CLttOU7n6sI` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: governance-compliance, testing-verification, sandboxing-execution

Andrew Dumit (Watershed) on deploying coding agents for sustainability supply-chain graph edits: constrain the effects through a typed SDK and deterministic execution, not the agent's reasoning, so the process can be validated.

- Techniques: Typed SDK as the only write path; Deterministic run executor (validate-then-commit); Review artifact instead of code review; Constrain effects, not reasoning; Eval-driven hill-climbing on the agent task
- Tools: Claude Code, TypeScript SDK, React agent (earlier version)

## [Everything we knew about software has changed — Theo Browne, @t3dotgg ​](../videos/xUnRQ9vLXxo.md)
`xUnRQ9vLXxo` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: product-ux, agent-architecture, multi-agent

Theo Browne argues that models have moved coding into an orchestration era, so tools, product tiers and software defaults should be rethought, with a markdown file running on cron as his example.

- Techniques: Markdown as a recurring program; Prompt-driven sub-agent orchestration; Breadth-first product with extension points; Assumption audit
- Tools: Claude Code, Codex, Git, GitHub, S3, Cron, Vercel, Slack bot APIs, Reddit, OBS, tmux, GNU Screen

## [Recursive Coding Agents - Raymond Weitekamp, OpenProse](../videos/3hXJI2q0Jz8.md)
`3hXJI2q0Jz8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, multi-agent

Raymond Weitekamp (OpenProse) on applying recursive language model (RLM) ideas to coding agents, with Claude Code dynamic workflows, the Pi extension, and OpenProse markdown workflows as ways to build them.

- Techniques: RLM as a tool call for a coding agent; Recursive agent via a pure Pi extension; Map-reduce versus deep-research workflows in Claude Code; Declarative workflow with parent verification; Adversarial or skeptical subagent roles; Golden session distillation; Small local model as RLM root
- Tools: Claude Code, Codex SDK, Pi, OpenProse, DSPy (dspy.rlm), RLM package (Alex Zhang), Agentica (Symbolica), Axe, Unix RLM (bash), LambdaRLM, Qwen 3.5 9B

## [Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS](../videos/IddXPepIAS4.md)
`IddXPepIAS4` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: context-engineering, testing-verification, mcp-and-tools

Erik Hanchett (AWS) on spec-driven development: write requirements, design and task markdown before code, keep a human reviewer in the loop, and use property-based tests to check the result.

- Techniques: Manual spec loop with any coding assistant; Clarifying questions before requirements; EARS-format requirements; Property tests generated from requirements and design; MVP-first task ordering; Steering docs plus on-demand skills; Pull requirements from PM tools via MCP
- Tools: Kiro, spec-kit, MCP, FastCheck, Mermaid, EARS, Jira, Asana, agents.md, CLAUDE.md

## [Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat](../videos/9arM9b7JgOo.md)
`9arM9b7JgOo` · AI Engineer · 2026-07-18 · q2 · intro · workshop · also: multi-agent, context-engineering

Snapchat engineer Jeffrey Lee-Chan demos his personal coding-agent workflow built on OpenClaw: a manager agent with memory delegates work to parallel worktree workers, and separating the manager's context from the workers' reduces overclaiming.

- Techniques: Manager and worker split with a separate-context reviewer; Layered verification with humans last; Context budgeting for the orchestrator; Local, staging, then production flow for agent changes; Cost-tiered model switching
- Tools: OpenClaw, CMUX, Claude Code, Claude Code Teams, Codex 5.3, GPT-5.4, MiniMax, git worktrees, Docker

## [Building an ACP-Compatible Agent Live — Bennet Fenner, Zed](../videos/HsxQICTLF84.md)
`HsxQICTLF84` · AI Engineer · 2026-07-18 · q3 · practitioner · demo · also: mcp-and-tools, agent-architecture

Live demo of turning a minimal TypeScript coding agent into an ACP-compatible agent for Zed: four required methods, streamed text, tool-call updates, client-proxied file access, and a diff content type.

- Techniques: Minimal agent loop as the ACP core; Session-scoped agent instances; Streaming through session-update notifications; Two-phase tool-call reporting; Client-proxied file system; Diff content type for edits; Using the protocol's debug view to inspect traffic
- Tools: Zed, Agent Client Protocol (ACP), ACP TypeScript SDK, Anthropic SDK, Node.js, stdio

## [RLM: Recursive Language Models for Large Codebases - Shashi, Superagentic AI](../videos/8oyalrfwgjw.md)
`8oyalrfwgjw` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: context-engineering, agent-architecture

Shashi (Superagentic AI) explains Recursive Language Models (RLM) for large codebases: keep the repo in a REPL, let the model write code to slice it, and call sub-models in a loop. He demos his open-source RLM Code harness with Gemini.

- Techniques: REPL-based context slicing (RLM loop); Recursive sub-calls with a budget; Full trajectory capture as JSONL; Sandboxed REPL execution; Model-agnostic sub-calls
- Tools: RLM Code, DSPy, Gemini, Docker, Codex, Pydantic AI, Google ADK, JSONL trace export

## [A Genius With Amnesia - Victor Savkin, Nx](../videos/jVjt-2g8NMY.md)
`jVjt-2g8NMY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: memory, agent-architecture

Victor Savkin (Nx) argues coding agents are limited by seeing one repo and forgetting past sessions, and shows Polygraph, a meta-harness that builds a cross-repo dependency graph and replays captured sessions on other machines.

- Techniques: Out-of-band cross-repo dependency graph; Multi-repo session as one unit of work; Session state replay for handoff; Intent-based scope selection; Agent-agnostic meta-harness
- Tools: Polygraph, Nx, Claude Code, Codex, GitHub

## [1,000+ Tokens/Sec: Google Just Shattered the AI Speed Limit (DiffusionGemma)](../videos/Dxn3BcSgsMY.md)
`Dxn3BcSgsMY` · Better Stack · 2026-07-02 · q3 · intro · review · also: models-research, inference-serving, local-ai

Better Stack walks through Google DeepMind's DiffusionGemma, a diffusion-style text model that refines a 256-token canvas in parallel, and tests its speed on an H100 via RunPod and OpenCode.

- Techniques: Parallel canvas refinement (non-autoregressive decoding); Uniform-state corruption for text diffusion; Encoder/denoiser mode split with bidirectional denoising; Run DiffusionGemma on RunPod and read the endpoint; Point OpenCode at the remote DiffusionGemma server; Local serving with vLLM in Docker; Read throughput from the server logs
- Tools: DiffusionGemma, Gemma 4 (26B base), OpenCode, vLLM, Docker, RunPod, NVIDIA H100, NVIDIA RTX 5090, Hugging Face

## [Use This To Make The Hermes Agent Basically Free](../videos/5d02TYoOzfE.md)
`5d02TYoOzfE` · AI LABS · 2026-07-02 · q2 · practitioner · tutorial · also: token-cost-efficiency, context-engineering, agent-architecture

Hermes Agent cost-reduction tutorial from AI LABS: where the tokens go, and which model, context, tool, and hard-limit settings cut the bill without hurting output.

- Techniques: Audit token spend before tuning; Route auxiliary and sub-agent work to a cheaper model; Use the OpenRouter Pareto router; Match effort level to task, and turn thinking off for simple work; Compress context early with a lower threshold and target ratio; Cap tool output in context; Use ephemeral system prompts for one-session instructions; Keep knowledge in files the agent loads on demand; Undo the last message and re-prompt with the failure described; Trim tools, skills, and MCP servers to what is used; Set hard limits on output, turns, and loops
- Tools: Hermes Agent, OpenRouter, Pareto router (OpenRouter), OpenAI Codex subscription, OpenAI subscription, Claude Code, Anthropic API, Gemini, MCP servers, Slack, Luma (sponsor), config.yaml

## [Claude Mythos is FINALLY here (Fable 5)](../videos/Ubazoyagym0.md)
`Ubazoyagym0` · Better Stack · 2026-07-02 · q2 · intro · news · also: models-research, token-cost-efficiency, governance-compliance

Anthropic's Fable 5, a safeguarded Mythos-class model: vendor benchmarks, a one-shot UI test, steep pricing, plan-limit burn, and a 30-day retention requirement. Mostly a reaction to launch claims.

- Techniques: Same-prompt side-by-side model comparison; Screenshot-to-site cloning
- Tools: Fable 5 (Anthropic model, Mythos class), Claude Mythos, Opus 4.8, GPT 5.5 (OpenAI), SWE-Bench Pro, Frontier Code (Cognition benchmark), Terminal Bench, Devin (referenced as Cognition product), Claude Max, Team and Enterprise plans

## [These Claude Workflows Turn Claude Code Into A Whole OS](../videos/5LnwJyi1il4.md)
`5LnwJyi1il4` · AI LABS · 2026-07-02 · q3 · intro · review · also: multi-agent, claude-code, token-cost-efficiency

Walkthrough of how Claude Code's pieces (CLAUDE.md, MCP, skills, loops/routines, dynamic workflows) form an "OS", with guidance on when a deterministic workflow beats goal or a plain skill; mostly a sponsored-style pitch with thin hands-on steps.

- Techniques: Start a dynamic workflow; Strict output schemas for sub-agents; Choose workflow vs goal vs skill; Convert a skill from a session; Coding-project OS setup; Second-brain audit workflow
- Tools: Claude Code, Claude Opus 4.8, CLAUDE.md, MCP, Google Calendar MCP, Notion MCP, Deep Research workflow, goal command, loops, routines, hooks, skills

## [Why I Quit My Dev Job Before AI Could Take It | Better Stack Podcast Ep. 16](../videos/VuMf2ZVA0RE.md)
`VuMf2ZVA0RE` · Better Stack · 2026-07-02 · q3 · practitioner · interview · also: claude-code, context-engineering, dev-tools

Better Stack podcast with Dreams of Code's Elliot on leaving dev work, betting on Rust, and practical AI-coding habits: stub-first interfaces, git-staged checkpoints, human-steered architecture.

- Techniques: Stub-first public interface; Hand-built spike before delegating; Git staging as manual checkpoints; Architecture-owner, typing-delegate split; Codec backend abstraction
- Tools: Claude Code, Codex CLI, Cursor, OpenCode, Bun, Zig 0.16, Rust, GPUI, gpui-component, Iced, egui, Tauri

## [GLM 5.2 is my new favorite model...](../videos/nODxez6nZEU.md)
`nODxez6nZEU` · Better Stack · 2026-07-02 · q3 · practitioner · review · also: models-research, token-cost-efficiency, evals

Hands-on test of open-weight GLM 5.2 against Kimi K2.7 Code and Claude Opus 4.8 on web design, one-shot apps and cost; strong and cheap per task, but token-hungry, and prompt steering drove most results.

- Techniques: Text prompt via a multimodal model for a text-only target; Section-and-style design brief for a one-shot landing page; Single-prompt full-stack app as a stack-choice and integration probe; Console-error loop as a pass or fail check; Cost per task from token counts and per-million prices; Use a cheaper open model for simpler tasks; Claude Code harness on a non-Anthropic API endpoint
- Tools: GLM 5.2 (Z.ai), GLM 5.1, Kimi K2.7 Code, Kimi K2.6, Claude Opus 4.8, Claude Opus 4.7, Claude Sonnet 4.6, Claude Code, Claude (vision, used to write the screenshot-to-prompt), Fable 5, Qwen 3.7, MiniMax M3

## [AI passed every benchmark… then failed at real work](../videos/7s2IIIP47GM.md)
`7s2IIIP47GM` · Kai Explains · 2026-07-02 · q2 · intro · other · also: evals, enterprise-adoption

Opinion piece arguing AI coding tools look strong on benchmarks but fail on open-ended, underspecified real work, and that failures are quiet. Recommends measuring shipped outcomes and keeping humans on costly decisions.

- Techniques: Outcome-based tool evaluation; Human gating by cost of error; Evaluate on your own codebase and problems
- Tools: Claude Code (transcript says "Clawed code"), GitHub Copilot, Gemini CLI, Cursor

## [Character swap live streaming, 3D mesh generator,  Google's DiffusionGemma & More AI News](../videos/73iY1aGFSYI.md)
`73iY1aGFSYI` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, local-ai, inference-serving

Weekly open-source AI news roundup: Meta's MeshFlow mesh generator, Google's DiffusionGemma block-diffusion LM, Cohere's North Minicode coding model, plus robotics and webcam mocap releases.

- Techniques: Block-wise denoising decoding with confidence-based re-noising; Generate structured geometry as a continuous latent with a parallel diffusion transformer; Self-supervised quality scoring via pairwise majority voting; Shared keypoint conditioning across embodiments
- Tools: MeshFlow, Gradio, Hugging Face, Blender, Maya, DiffusionGemma, Gemma 4, GGUF, Kaggle, Vertex AI, North Minicode, open code

## [herdr: Is This the Ultimate Agent Multiplexer?](../videos/PlN86TvzGy4.md)
`PlN86TvzGy4` · Better Stack · 2026-07-02 · q3 · intro · review · also: multi-agent, dev-tools

A walkthrough of herdr, a single Rust terminal multiplexer that adds agent awareness (working, blocked, done) to tmux-style panes, lets agents drive it through a CLI or socket, and works over SSH.

- Techniques: Install and launch herdr; Remap the prefix key; Agent-spawned panes with herdr CLI; Remote session over SSH with local config
- Tools: herdr, tmux, Warp, cmux, Claude Code, Codex CLI, OpenCode, Vim, Bash, Fish, Ratatui, Rust

## [Your AI Agent Is Missing Half the Internet… Until Now (Agent-Reach)](../videos/aanqEqQwjNU.md)
`aanqEqQwjNU` · Better Stack · 2026-07-02 · q3 · intro · review · also: mcp-and-tools, rag-retrieval

A 6-minute Better Stack review of Agent Reach, an MIT-licensed Python CLI that gives coding agents multi-platform web access (social, code, video, Chinese platforms) with health checks and fallback backends.

- Techniques: Per-platform channel adapters with primary and fallback backends; One-sentence agent-driven install plus a doctor health check; Shell permission as a prerequisite for self-install
- Tools: Agent Reach (Python CLI and library, MIT licensed, over 28,000 GitHub stars), Claude (used inside VS Code), Cursor 2, Playwright (suggested for interactive browser actions), Firecrawl (suggested for plain web pages; transcript says 'fire crawl'), YouTube, GitHub, Twitter/X, Reddit, Bilibili, Xiaohongshu (platform channels)

## [Insane Claude Design Skills You Need To Build Beautiful Websites](../videos/Ot582-E61ac.md)
`Ot582-E61ac` · AI LABS · 2026-07-02 · q3 · intro · review · also: skills-self-improvement, product-ux, mcp-and-tools

A walkthrough of Claude design skills (Anthropic frontend-design, ShadCN, UI UX Pro Max, GSAP, Material 3, SwiftUI, Expo) for building less generic websites and mobile apps, with a sponsor segment.

- Techniques: Commit to a design direction before generating; Separate functional and marketing design skills; Pair a rules skill with a component-registry MCP; Separate layout reasoning from component work for dashboards; Use a taste preset instead of a full design system; Prefer compositor-friendly animation properties
- Tools: Claude, Anthropic frontend-design skill, Opus 4.8, Fable 5, ShadCN, ShadCN MCP, UI UX Pro Max, GSAP, Higgsfield, C-Dance (as captioned; video model), Material 3, SwiftUI

## [Real-time Voice cloning, Kimi K2.7 CODE, GLM 5.2 and 3D reconstruction | AI News](../videos/DX4kW1vdTXc.md)
`DX4kW1vdTXc` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, local-ai, voice-multimodal

Weekly open-model news roundup (2026-07-02): Zonos 2 voice cloning, MiniMax M3, Kimi K2.7 Code, GLM 5.2, NVIDIA Motion Bricks, Microsoft Fara-7B, plus robotics and 3D items. Mostly vendor-reported claims.

- Techniques: Shared fixed-size latent for variable-view 3D reconstruction (Surflow); Reusable motion primitives with zero-shot composition (Motion Bricks); Report steps and cost per task next to success rate for computer-use agents (Fara-7B); Canonical body topology as a pivot between body models (SOMA); Haptic torque feedback in teleoperation for robot data collection (UME); Where to get each release (as stated in the video)
- Tools: Zonos 2, Zyphra Cloud, MiniMax M3, MSA (Minimax Sparse Attention), Minimax Code, Kimi K2.7 Code, Kimi K2.6, KimiCode, Kimi Code Bench V2, Program Bench, MLS Bench Lite, MCP Atlas

## [This Claude Code Plugin Writes 94% Less Code (ponytail)](../videos/2xuFcmUAQUc.md)
`2xuFcmUAQUc` · Better Stack · 2026-07-02 · q3 · practitioner · review · also: claude-code, token-cost-efficiency, evals

Better Stack tests Ponytail, a Claude Code plugin that applies a YAGNI decision ladder to make agents write less code. Its cost claims come with a caveat, and one A/B test shows fewer lines and lower cost.

- Techniques: YAGNI decision ladder in the agent prompt; Native-first replacement check; Record deferred decisions in a code comment; Benchmark cost next to correctness; Side-by-side A/B of a coding agent with and without a plugin
- Tools: Ponytail (Claude Code plugin; benchmark compares no skill, Caveman, and Ponytail), Claude Code, Caveman, Radix UI (React dialog library, the default-agent choice in the modal example), npm (npm package dialog example), Python server (default-run output, not a named tool)

## [SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius](../videos/wcUJWP6WpGM.md)
`wcUJWP6WpGM` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: evals, testing-verification, training-finetuning-rl

Ibragim Badertdinov (Nebius) shares lessons from running monthly SWE-rebench evals of coding agents: fresh time-split tasks, verifier quality, infra noise, benchmark cheating, and reporting cost and reliability.

- Techniques: Monthly time-split task collection; Oversample, then filter by running agents; Strip future information from the agent sandbox; Minimal agent with strong infrastructure; Error-class retry policy; Reliability-aware metrics; Reproduce a public benchmark before trusting your own numbers; Eval pipeline reused as training pipeline
- Tools: SWE-rebench, SWE-bench, Terminal-Bench, Claude Code, Codex, Junie, Docker, GitHub Archive, GitHub API

## [Your Coding Agent Should Do AI System Engineering — Ben Burtenshaw, Hugging Face](../videos/JomVvNDjGb8.md)
`JomVvNDjGb8` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: skills-self-improvement, multi-agent, training-finetuning-rl

Ben Burtenshaw (Hugging Face) argues coding agents can take on AI systems work: writing CUDA kernels, fine-tuning models, and running a multi-agent automated research lab, using open skills, open Hub repos and an open dashboard data layer.

- Techniques: Skill-as-few-shot-examples with bundled benchmark scripts; Skill eval across models (Upskill); Role-split autoresearch loop; Git and bucket as agent shared state; Open-format dashboard as an agent data source; Verifiable-experiment precondition
- Tools: CUDA, Hugging Face kernels library, Upskill, Hugging Face Skills repo, HF Papers CLI, HF Jobs, OpenCode, Codex, Claude Code, Trackio, Parquet, Unsloth

## [Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer](../videos/zKk7sDMGDEQ.md)
`zKk7sDMGDEQ` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: rag-retrieval, claude-code, evals

Turbopuffer's Kuba Rogut benchmarks semantic code search as an extra tool for Claude Code, using a windowed-grep baseline and file, line and symbol precision and recall on human-labelled context tasks; semantic search helps precision but the gain is smaller than Cursor's because Claude Code does not know when to call it.

- Techniques: Chunk-embed-index semantic code search as a CLI tool; Windowed file reads as a retrieval baseline; Trajectory-level retrieval evaluation; Inline comments as embedding context
- Tools: Turbopuffer, Voyage code-3, Claude Code, Cursor, TurboGrep, tree splitter

## [Fast Models Need Slow Developers — Sarah Chieng, Cerebras](../videos/TeGsFFNqRLA.md)
`TeGsFFNqRLA` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: inference-serving, testing-verification, context-engineering

Cerebras's Sarah Chieng argues that fast coding models (Codex Spark, ~1,200 tok/s) demand new habits: plan with a large model, execute with a fast one, verify every step, and keep context in bounded goals.

- Techniques: Planner-executor model split; Session-to-skill distillation; Per-step automatic verification; Parallel variant generation with cherry-picking; Scoped steering constraints; Automatic refactor pass after each task; Bounded goals with a context budget; Four-file external memory (AGENTS/PLAN/PROGRESS/VERIFY)
- Tools: Codex Spark, Codex, GPT-5.4, GPT-5.3 Codex, Sonnet, Opus, REAP (router-weighted expert activation pruning)

## [Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub](../videos/_xIwFcnHqp4.md)
`_xIwFcnHqp4` · AI Engineer · 2026-06-18 · q3 · practitioner · demo · also: mcp-and-tools, product-ux

Marlene Mhangami and Liam Hampton (GitHub) show how MCP Apps let a tool return an interactive HTML UI rendered in a sandboxed iframe inside VS Code chat, with a live Go flame-graph demo.

- Techniques: MCP App tool-plus-resource pattern; Skill-driven MCP app scaffolding; Tool visibility scoping; Profiler-to-flame-graph bridge; Install MCP servers from curated lists only
- Tools: VS Code, GitHub Copilot, Copilot CLI, MCP, Go pprof, React, Excalidraw, Figma

## [Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw](../videos/pmoDeA3RBZY.md)
`pmoDeA3RBZY` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: software-factory, multi-agent, skills-self-improvement

OpenClaw maintainer Vincent Koc on running dozens of parallel coding agents as a "dark factory": swim lanes, opinionated loops, a big plugin refactor, and token efficiency over token maxing.

- Techniques: Swim-lane parallel agents; Big refactor gated by existing tests; Plugin split for blast-radius control; One clone per session instead of worktrees; Explanation quality as a health check; Skill improvement from session logs; Embedding graph for backlog dedupe; Synthetic plus real fake-chat eval harness
- Tools: Codex, Git worktrees, GitHub, Discord, Slack, MS Teams, Docker, GEPA, skills.sh, OpenClaw, NemoClaw, vector embeddings

## [How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind](../videos/7gujZrJ9L5I.md)
`7gujZrJ9L5I` · AI Engineer · 2026-06-18 · q3 · intro · panel · also: agent-architecture, skills-self-improvement, infra-cost-scaling

A Google DeepMind panel on running coding and research agents at Google scale, covering shared workspaces, quota and cost control, skill sprawl, internal observability, and PR review.

- Techniques: Shared file-system workspace between agent stages; Editable plan gate before execution; Scratchpad notes as a reviewable trace; Mock compute for harness testing; Trajectory store plus hierarchical drill-down; Per-language fine-tuned review model plus per-product review prompts; Transparent model fallback under the harness; Skills plus guardrailed CLI over MCP for internal tools
- Tools: Antigravity, Gemini, Gemma 4, Deep Research, Jules, MCP, OpenClaw

## [Cooking with Agents in VS Code — Liam Hampton, Microsoft](../videos/dyHpnnlkTc8.md)
`dyHpnnlkTc8` · AI Engineer · 2026-06-18 · q2 · intro · demo · also: multi-agent, context-engineering, sandboxing-execution

A Microsoft product tour of running local, background (worktree) and cloud coding agents side by side in VS Code, with advice on which mode fits which task.

- Techniques: Worktree-per-background-agent; Route tasks by hands-on level; Plan first, autopilot second, pause before PR; Task-specific custom agents; Cloud agent with MCP and browser testing
- Tools: GitHub Copilot, VS Code, GitHub Copilot CLI, Git worktree, GitHub Actions, GitHub MCP server, Playwright MCP server, Microsoft Learn MCP server, awesome-copilot (open-source repo of agent customizations), Claude Opus 4.6 (used for the local agent)

## [RAG is dead, right?? — Kuba Rogut, Turbopuffer](../videos/UM6sFg_jdlE.md)
`UM6sFg_jdlE` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: rag-retrieval, context-engineering, infra-cost-scaling

Kuba Rogut (Turbopuffer) argues that "RAG is dead" misreads the problem: retrieval should be a toolbox (vector, BM25, grep, filters) used in iterative agent loops, and embeddings work best as precomputed cache compute.

- Techniques: Multi-modal retrieval toolbox for agents; Iterative search-read-assess loop; Index once, query at runtime; Merkle-tree index reuse across near-identical corpora; Staged narrowing before the context window
- Tools: Claude Code, Codex, Cursor, Turbopuffer, BM25, Merkle trees

## [What the Best Agents Share — Mardu Swanepoel, Flinn AI](../videos/7CrPrHgoEYk.md)
`7CrPrHgoEYk` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: product-ux, context-engineering

Mardu Swanepoel (Flinn AI) on four UX patterns shared by strong agents: focus modes, transparent execution, personalization, and reversibility, illustrated with Cursor, Claude Cowork, Harvey and Manus.

- Techniques: Mode-scoped agent configuration; Plan-only mode; Hypothesis-driven debug mode; Visible execution trace; Playbook and memory personalization; Layered undo; Native host integration for review
- Tools: Cursor, Claude Cowork, Claude skills and connectors, Manus, Harvey, Microsoft Word API

## [Prompt to Pipeline: Building with Google's Gen Media Stack — Paige & Guillaume, Google DeepMind](../videos/ns9f1fjLD7Y.md)
`ns9f1fjLD7Y` · AI Engineer · 2026-06-18 · q3 · practitioner · workshop · also: models-research, voice-multimodal, vibe-coding-app-building

Google DeepMind's Paige and Guillaume, with Gemma's Ian Ballantyne, demo AI Studio, Gen Media models and local Gemma 4 agents. Mostly a live product tour, with some practical prompting and cost tips.

- Techniques: Playground-to-code export; Code execution for verified counting and drawing; Per-scene reference injection for character consistency; Structured outputs as a prompt-writing stage; Prompt-level multi-voice TTS; Flex and priority service tiers; Local orchestrator with parallel subagents on an OpenAI-compatible server; Vibe-coding guardrails: one file per feature, plus logging
- Tools: Google AI Studio, Gemini API, Gemini Live, Google Build (AI Studio), Firestore, Google Search grounding, Antigravity, Nano Banana 2, Veo 3.1 Lite, Lyria 3, Lyria RealTime, Genie 3 / Project Genie

## [Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry](../videos/ugUeZ8-b-u0.md)
`ugUeZ8-b-u0` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: testing-verification, dev-tools

Argues Rust's strict compiler suits agent-written code better than Python or TypeScript: compile-time checks rule out bug classes that tests and LLM review miss, and compiler errors give agents concrete fix signals. Sponsored by Sentry.

- Techniques: Compile-in-the-loop repair; Deterministic checks before LLM review; Use error messages that name the concrete type; Choose a language by how strongly its checker constrains output; Write tests first when an agent writes tests
- Tools: Rust, rustc (Rust compiler), TypeScript, Python, Sentry

## [Evals Are Broken, Use Them Anyway — Ara Khan, Cline](../videos/QuuIywMG4s8.md)
`QuuIywMG4s8` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: evals, testing-verification

Ara Khan (Cline) argues most people misuse evals, either trusting vendor leaderboards or dismissing evals for vibes, and shows how to build a Terminal-Bench-style agent eval and hill-climb on it alongside a vibe check.

- Techniques: Failure-trace triage loop; Isolated parallel eval runs; Hill-climb with a vibe check; Sort fixes into three zones; Delayed model adoption; Check the task itself
- Tools: Terminal-Bench, Harbor, SWE-bench Verified, Claude Code, Codex, Daytona, Docker, Modal

## [Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs](../videos/V-L0INGTEOg.md)
`V-L0INGTEOg` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: claude-code, skills-self-improvement

Boris Starkov (ElevenLabs) shows how Claude Code reverse-engineered an undocumented 1990s-style VoIP phone's protocol through port probing, command brute-force, and a traffic-capture proxy, then packaged the result as a reusable skill.

- Techniques: Black-box command sweep with error classification; Intermediary proxy for vendor-client traffic capture; Closed-loop hypothesis confirmation; Persisting a learned protocol as a skill; Using the full session transcript as context to generate a deliverable; Human as actuator for physical steps
- Tools: Claude Code, Twilio (SIP trunk), ElevenLabs conversational agents, Windows virtual machine, TCP proxy on macOS, PoE router

## [The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry](../videos/li0SaBt9RDM.md)
`li0SaBt9RDM` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: claude-code, skills-self-improvement

Sentry engineer Priscila Andre de Oliveira on using AI mainly for codebase comprehension: she mined her own sessions, found 67% were comprehension and 2% generation, and built a reusable "Catch Me Up" skill.

- Techniques: Session-log classification audit; Repeated prompt to personal skill; Onboarding via a 'new contributor' framing; Comprehension pass before PR review; Research, then comprehension check, then plan, then implement; Codebase hygiene sprint for agent legibility
- Tools: Claude Code, Claude Opus, Catch Me Up (personal skill), Warden (Sentry code review agent), Junior (Sentry Slack bot that turns threads into PRs), Abacus (Sentry internal AI usage tracker)

## [Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar](../videos/NuePCNMpWGc.md)
`NuePCNMpWGc` · AI Engineer · 2026-06-18 · q2 · practitioner · talk · also: pr-code-review, evals, testing-verification

Sonar argues that LLM pass rates miss security, maintainability and verbosity. It shows its Java eval of 53+ models and pitches a verify-in-loop and remediation pipeline, so it is product-heavy.

- Techniques: Dual-metric model evaluation; In-loop static analysis via MCP; Regression-gated autofix; One PR per issue for tech debt; Remediation on quality-gate failure
- Tools: SonarQube, SonarQube Agentic Analysis (MCP), Sonar Sweep, Sonar Context Augmentation, Sonar remediation agent, Claude Code, Codex, Gemini CLI, Devin, Cursor, Windsurf, Antigravity

## [Let's Talk About FOMAT: Fear of Missing Agent Time — Michael Richman, Cmd+Ctrl](../videos/W-SX_srBa3Y.md)
`W-SX_srBa3Y` · AI Engineer · 2026-06-18 · q2 · practitioner · demo · also: multi-agent, agent-architecture

Bitly engineer Michael Richman presents Command & Control, his tool for monitoring and answering coding agents from a phone, web or watch, and frames the idle-agent problem as FOMAT.

- Techniques: Per-platform lifecycle daemon feeding a control plane; Tiered notification and watch lists; Overview summaries from the last few messages; Start remotely, resume locally on the same session
- Tools: Command & Control (Cmd+Ctrl, speaker's own tool), Claude Code (captioned as Cloud Code), Codex / Codex CLI, Gemini (CLI), Cursor (IDE), GitHub Copilot, OpenCode, Anthropic remote control and teleportation (Claude Code features, mentioned), Bitly MCP server (co-written by speaker, mentioned), Agent Craft (gaming-based agent tool, mentioned as seen earlier that morning)

## [Don't Build Slop (4 Levels of AI Agent Maturity) - Ara Khan, Cline](../videos/yUmS-F9IX90.md)
`yUmS-F9IX90` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: agent-architecture, context-engineering, software-factory

Ara Khan (Cline) argues for four maturity levels of agent building: framework, hand-built state machine, Kanban as the UX, and cloud execution. Core warnings: keep prompts minimal, keep agents CLI-testable, and keep architecture human-owned.

- Techniques: Agent as explicit state machine; Prune the system prompt on every change; CLI-first agent interface for agent-driven development; Exact reasoning-trace round-tripping; Kanban board as the multi-agent control surface; Per-task cloud agent dispatch; Human-owned architecture before code generation
- Tools: Claude Code, Codex, Cursor, Factory, Cline, LangChain, LangGraph, OpenRouter, Linear, AGENTS.md, VS Code

## [From MCP to Scale: Pipelines That Build Themselves — Rafael Levi, Bright Data](../videos/zTZ0qunQXnM.md)
`zTZ0qunQXnM` · AI Engineer · 2026-06-18 · q2 · practitioner · demo · also: data-engineering, mcp-and-tools, voice-multimodal

A Bright Data vendor demo arguing LLMs should write a reusable scraper once instead of parsing every page, then run and self-repair it on a schedule. Useful pattern, heavy product pitch.

- Techniques: Generate-then-run scraper; Scheduled self-repairing collection loop; Tiered fetch format; Remote browser with human-like input for multi-step flows; Public-data-only policy check
- Tools: Claude Code, Codex, Bright Data MCP, Bright Data scrape-as-markdown, Bright Data Web Unlocker API, Bright Data remote browsers, Bright Data skill docs on GitHub, Haiku

## [Terax: One Developer Built an AI Terminal Better Than Warp](../videos/3L8htHUzAI4.md)
`3L8htHUzAI4` · Better Stack · 2026-06-02 · q3 · intro · review · also: dev-tools, context-engineering

Review of Terax, a small open-source AI terminal and code editor built with Tauri 2 and Rust, compared against Warp and CMUX; the reviewer keeps Warp and Neovim for daily work.

- Techniques: Lean desktop shell for a terminal-plus-agent app; Read-only plan mode, then build mode, for agent edits; Generate a project context file with init, then review it as a diff; Hide sensitive tabs from the agent with a privacy page; Keep API keys in the OS keyring
- Tools: Terax, Tauri 2, Rust, React, Electron (comparison), Xterm.js (WebGPU renderer), CodeMirror 6, Vercel AI SDK, Warp, CMUX, Helix, Neovim

## [It’s Broken… The Codex vs Claude Code Debate Is Finally Over](../videos/8ImlAQOyVTs.md)
`8ImlAQOyVTs` · AI LABS · 2026-06-02 · q3 · practitioner · review · also: claude-code, context-engineering, multi-agent

A single-author head-to-head of Claude Code (Opus 4.7) vs Codex CLI (GPT 5.5) across usability, planning, greenfield builds, context, memory and sub-agents; Codex wins on cost and autonomy, Claude on UX, hooks and ecosystem.

- Techniques: Count tokens per session from the CLI's session files; Set a Codex personality to reduce sycophancy; Use Claude Code's expanded thinking to course-correct; Use Codex's attempt flag for best-of-n; Keep AGENTS.md or CLAUDE.md lean; Design sub-agents for isolation or inheritance deliberately
- Tools: Claude Code, Codex CLI, Opus 4.7, GPT 5.5, FastAPI, Flask, Next.js, ShadCN UI, Gemini API, Claude desktop app, Codex web app, Stream Vision Agents

## [This One Command Fixed The Biggest Problem Of AI Coding](../videos/qkc1j3_k8gs.md)
`qkc1j3_k8gs` · AI LABS · 2026-06-02 · q3 · practitioner · tutorial · also: security-guardrails, token-cost-efficiency, pr-code-review

Walkthrough of DeepSec, a regex-prefilter plus batched Claude Code/Codex agent harness for repo security scans. Strong on code-local bugs, weak on runtime and logic flaws.

- Techniques: Regex prefilter before agent review; Batched parallel agent investigation with merge and coverage check; Project context file for the scanner (info.md); DeepSec command sequence; Resumable batch processing; Per-finding output with ownership and repro; Scoping an unscoped agent review
- Tools: DeepSec (Vercel security harness; `deepsec init`, `scan`, `process`, `report`, `export`), Claude Code, Codex, Claude Agent SDK, Codex Agent SDK, Opus 4.7 (max effort), GPT 5.5 (x-high reasoning), Git (metadata for commit attribution and owner), Markdown and JSON (output formats)

## [Stop Using Claude Code CLI. Use THIS Instead! (Oh-My-Pi)](../videos/8ukl-0tlVgM.md)
`8ukl-0tlVgM` · Better Stack · 2026-06-02 · q2 · intro · review · also: token-cost-efficiency, agent-architecture, dev-tools

A 5-minute Better Stack walkthrough of Oh My Pi, an open-source terminal agent harness built on the Pi framework, covering LSP refactoring, debugger attach, per-task models, hashline edits, and Pi package support.

- Techniques: Hashline edits (anchor-based line editing); LSP-backed workspace refactor; Per-task model routing in a harness; Debugger attach for agent debugging
- Tools: Oh My Pi (open-source terminal agent harness), Pi framework (base for Oh My Pi; source of the Doom package), Claude Code CLI (compared against; plugins and settings are imported on login), Claude Opus (named as the model that reproduces full edit text in Claude Code), Grok 4 Fast (model used for the 61% token-savings claim), DLV (Go debugger), DebugPy (Python debugger), Chrome (launched by the built-in browser tool), Hindsight (agent memory management, mentioned only), Rust (language of the demo app)

## [Is Your AI Code Producing CRAP? (Here's How To Fix It)](../videos/XuMR1pgc6pc.md)
`XuMR1pgc6pc` · Better Stack · 2026-06-02 · q3 · practitioner · review · also: testing-verification, pr-code-review

Better Stack explains the CRAP metric (complexity combined with test coverage) and the cargo crap Rust tool, arguing it is a useful second check on complex, under-tested code, especially AI-generated code.

- Techniques: Run a CRAP check after the unit tests; Set a complexity budget; Check that the metric reacts to test removal
- Tools: cargo crap (cargocrap Rust package, by Oleksandr Prokhoranko), CRAP metric (Savoia and Evans, 2007), Rust, CRAP tool for Java (same author, mentioned, not shown)

## [Vercel made a programming language](../videos/Koop0_nkNtc.md)
`Koop0_nkNtc` · Better Stack · 2026-06-02 · q3 · practitioner · review · also: dev-tools, context-engineering

Better Stack walkthrough of Xero, a new systems language whose toolchain emits JSON diagnostics with fix guidance so agents can repair code. A Claude fix run succeeded without docs, but the presenter doubts a new language was needed.

- Techniques: Self-describing toolchain for agents; Zero-context fix-loop test; Explicit capability marking for IO; Error propagation with raises and check; Scoped cleanup with owned values, drop and defer; Running a Xero program
- Tools: Xero (systems language and toolchain, named as 'Xero' or 'zero' in the transcript), Claude (Claude Code, used for the fix run), Rust, Zig, Go, jq, Bun (mentioned only as a possible future rewrite target), WebAssembly (compile target)

## [This New Syntax Wants To Replace JSX](../videos/B_N-O8_eG34.md)
`B_N-O8_eG34` · Better Stack · 2026-06-02 · q3 · intro · review · also: dev-tools

Walkthrough of TSRX, a statement-based JSX syntax from the creator of Ripple that compiles to React, Preact, Solid, Vue and Ripple. The presenter likes several control-flow ideas but will stay with React and Tailwind.

- Techniques: Statement-based conditional rendering; for...of list rendering with key and index; try/catch error boundary plus pending block for async; Hooks after conditions and early returns; Component-scoped CSS with shared style keyword; Escaped text vs raw HTML; Lazy destructuring with ampersand
- Tools: TSRX, Ripple, Ripple View, React, Preact, Solid, Vue, Svelte, Vite, Tailwind CSS, Claude, llms.txt

## [Harness Engineering: The Missing Layer for AI Coding Agents (Archon)](../videos/-1BOhPOcEb8.md)
`-1BOhPOcEb8` · Better Stack · 2026-06-02 · q2 · intro · review · also: agent-architecture, software-factory

Better Stack demos Archon, an open-source harness that defines coding-agent work as YAML workflows with fixed and AI steps, runs each job in its own git worktree, and auto-loads skills, aiming for repeatable, conflict-free parallel runs.

- Techniques: Process-as-YAML DAG with mixed step types; Per-run git worktree isolation; Skills as on-demand context; Local setup flow shown in the video (no exact commands on screen)
- Tools: Archon, ArchonServe (Archon local UI), Claude Code, Cursor, Codex, LangChain, Agent Skills, git worktree, YAML

## [Gemini 3.5 Flash is just... fine](../videos/JegffwBtXJ0.md)
`JegffwBtXJ0` · Better Stack · 2026-06-02 · q3 · practitioner · review · also: models-research, token-cost-efficiency

Review of Google's Gemini 3.5 Flash and Antigravity 2: very fast and good at agentic tasks and UI, but token-hungry, costly per run and weak on coding versus frontier models.

- Techniques: Cross-check vendor benchmarks against third-party indexes; Judge cost per completed task, not list price per token; Run the same one-shot prompt across models for UI quality; Compare speed against intelligence
- Tools: Gemini 3.5 Flash, Antigravity 2, Antigravity CLI, Gemini CLI, Gemini 3 Flash, Gemini 3.1 Pro, Gemini 3.5 Pro, Claude Opus 4.7, GPT 5.5, Kimi K2.6, Haiku, Codex

## [Why OpenAI Built Symphony and Gave It Away for Free](../videos/n8qDKMPpLXc.md)
`n8qDKMPpLXc` · Better Stack · 2026-06-02 · q3 · intro · review · also: agent-architecture, multi-agent, software-factory

Better Stack walkthrough of OpenAI's open-source Symphony, which polls Linear for issues and runs a coding agent per issue, with humans involved only at review. Covers setup, workflow file and hooks.

- Techniques: Tracker-driven agent dispatch; Workflow file with YAML front matter plus a per-issue prompt; Clone-and-branch after-create hook, commit-push-PR after-run hook; Spec-driven self-implementation
- Tools: Symphony (OpenAI, open-source orchestrator), Linear (issue tracker), Codex CLI (OpenAI coding agent), GPT-5.5 (model, used at low effort for spec-generated build), Elixir (language for the manual install route), TypeScript and Bun (demo app), Python (spec-generated Symphony version), Go with Charm CLI (community Symphony version), Claude SDK (community Symphony version), uv (Python tool; speaker says OpenAI acquired it, not verified in video), Multica (agent orchestration product, compared), Conductor (agent orchestration product, compared)

## [MCP Apps Are Changing the Internet. Here’s How to Build One! (Skybridge)](../videos/9X8GRGcl5oA.md)
`9X8GRGcl5oA` · Better Stack · 2026-06-02 · q3 · intro · tutorial · also: mcp-and-tools, vibe-coding-app-building

Better Stack walkthrough of Alpic's SkyBridge 1.0, a TypeScript/React framework for building MCP apps (interactive widgets inside chatbots), shown by building and testing a camera-lens store app with its local dev dashboard, tunnel and Beacon Audit.

- Techniques: Install the SkyBridge skill into the repo, then prompt the agent to build the app; Test tools and widget state in the SkyBridge dashboard before involving a chatbot; Expose a local MCP server with the dashboard tunnel and attach it as a Claude custom connector; Run Beacon Audit before submitting to an app store
- Tools: SkyBridge 1.0 (Alpic, open-source TypeScript framework for MCP apps), Alpic Playground (sandbox inside the SkyBridge dashboard), Beacon Audit (SkyBridge app audit tool), React, TypeScript, Claude (builds the app and hosts the custom connector; the transcript does not name the surface used for generation), ChatGPT (developer settings used for testing the tunnel URL), Skybridge agent skill (installed into the repo's .agents directory)

## [What Happens When AI Coding Gets a Delivery Pipeline (Routa)](../videos/_16PhraFYjQ.md)
`_16PhraFYjQ` · Better Stack · 2026-06-02 · q3 · intro · review · also: software-factory, multi-agent, pr-code-review

Walkthrough of Routa, a free, local-first, open-source Kanban desktop app that runs AI coding agents through backlog, dev, and review lanes with evidence and gates instead of one chat thread.

- Techniques: Lane-per-stage agent pipeline; Evidence-backed review gates; Per-task traceability; Self-hosted setup
- Tools: Routa (open-source AI coding delivery tool; spelled Ruta in captions, Routa in the title; desktop app and Docker Compose), OpenCode (agent runtime used for the agents), Anthropic API / Claude (model provider via synced API key), MCP (Model Context Protocol, supported for agent connections), ACP (Agent Client Protocol, supported for agent connections), Docker Compose (self-hosting path), Cursor (chat-first comparison), Claude Code (chat-first comparison), CrewAI (agent framework comparison), LangGraph (agent framework comparison; spelled LaneGraph in captions)

## [Impeccable Makes Claude Build Sites That Don't Look Like AI](../videos/Ln11hm7jieM.md)
`Ln11hm7jieM` · Better Stack · 2026-06-02 · q3 · intro · review · also: context-engineering, token-cost-efficiency

Better Stack walks through Impeccable, a design-quality skill/toolchain that steers AI coding agents away from generic-looking sites, builds a homepage with it, and concludes it suits people who want good-looking output without deep design control, and that Claude Code is token-expensive for it.

- Techniques: Staged design workflow with persistent design MD files; Forcing an image-model probe step when the harness has no image generation; Browser-driven live iteration with impeccable live; Run document after the visual pass
- Tools: Impeccable (design-quality toolchain / agent skill, installed via skills.sh), Claude Code, Astro, Tailwind CSS, GPT Image 2 (OpenAI image model, used for probes), OpenAI API key via shell environment, Codex CLI, Codex GUI, Pencil (design tool, mentioned as the precise alternative; earlier Better Stack video), Superpowers (Claude plugin, mentioned for comparison), jQuery UI (creator's earlier project, mentioned)

## [This Open Source Tool Gives You God Mode for AI Agents (AoE)](../videos/fPz9OB3Bau8.md)
`fPz9OB3Bau8` · Better Stack · 2026-06-02 · q2 · intro · review · also: multi-agent, sandboxing-execution

Better Stack demo of Agent of Empires (AoE), an open-source terminal dashboard that runs many CLI coding agents side by side using git worktrees, status indicators and optional Docker sandboxes. Short and promo-leaning, with little configuration detail.

- Techniques: Run many CLI agents from one dashboard; Per-agent git worktree isolation; Triage agents by status instead of attaching; Optional Docker sandbox per agent
- Tools: Agent of Empires (AoE), Claude, Codex, tmux, Git worktrees, Docker, Agent Deck, Homebrew

## [OpenTUI: React for Your Terminal, Powered by Bun and Zig](../videos/zr4ctBgKAOU.md)
`zr4ctBgKAOU` · Better Stack · 2026-06-02 · q3 · intro · review · also: dev-tools

Walkthrough of OpenTUI, a Zig-core terminal UI library with React and Solid bindings running on Bun, compared against Ink. The speaker builds a small React TUI and argues JSX is the best way to compose terminal UIs.

- Techniques: Scaffold a React TUI project with the Bun template wizard; Choose a screen mode; Bind input state with useState and onInput; Style and lay out with Box props and Yoga flexbox; Animate with the useTimeline hook; Use other OpenTUI hooks and components; Live reload during development
- Tools: OpenTUI, Zig, React, Solid, Bun, Bun FFI, Yoga, Ink, Bubble Tea, Ratatui (spoken as 'Ratatouille'), Three.js (spoken as '3.js', WebGPU rendering), OpenCode

## [Open Design: Why 40k Developers Abandoned Claude Design](../videos/B3coWv2ZV68.md)
`B3coWv2ZV68` · Better Stack · 2026-06-02 · q3 · intro · review · also: vibe-coding-app-building, product-ux

Walkthrough of OpenDesign, an open-source, local alternative to Anthropic's Claude Design that generates HTML prototypes and slides on top of whichever coding agent is installed; the speaker argues design systems plus per-output skills drive quality more than the model.

- Techniques: Run OpenDesign from source; Harness and model selection per project; Seed a design from a live URL; Pick a design system before prompting; Finalize, export and hand off; Iterate with follow-up prompts
- Tools: OpenDesign (open-source Claude Design alternative, Nexa team), Claude Design (Anthropic, proprietary, cloud-only, $20/month per the speaker), Claude Code, Claude Opus 4.7 (speaker's claim that it is strong at front-end design), Codex, OpenCode, GLM 5.1 (used as the generation model), GPT-Image2 (OpenAI image model, default image provider via OpenAI key), ElevenLabs (TTS and sound effects, optional), agent-browser (browser tool the agent used), Chrome (opened via curl by the agent), Docker (optional install path)

## [Claude Code Just Killed Every Shopify Agency Ever](../videos/x2pRavsHdls.md)
`x2pRavsHdls` · AI LABS · 2026-06-02 · q2 · practitioner · tutorial · also: claude-code, vibe-coding-app-building, context-engineering

A walkthrough for building and syncing a Shopify storefront with Claude Code, using the Shopify CLI, AI toolkit MCP, HTML prototype skill, Gemini image skill and settings.json hooks. Quality is capped by a sponsor segment and a thin, hype-titled setup guide.

- Techniques: Two-phase skill: HTML preview, then apply; Image generation through a CLI skill; Pre-tool-use hook as an approval gate; Shopify project bootstrap; Admin API auth with incremental scopes
- Tools: Shopify Partner account, Shopify CLI (React app template, TypeScript), Shopify AI toolkit (MCP), Shopify plugin (agents and skills), Shopify Admin API, Claude Code, CLAUDE.md, Gemini CLI (image generation), settings.json hooks, Willow Voice (sponsor segment, not a tool used in the setup)

## [This Is Insane... This Just Ended The Google Stitch VS Claude Design Debate](../videos/PJ9CmTODmVo.md)
`PJ9CmTODmVo` · AI LABS · 2026-06-02 · q2 · intro · review · also: product-ux, mcp-and-tools, context-engineering

Hands-on head-to-head of Claude Design and Google Stitch across features, limits, design quality, animation, iteration and handoff; each tool wins different categories.

- Techniques: Batch design comments before sending; Import a design system from a URL; Portable design.md design system; Coding agent drives the design tool through MCP; Generate the design system before the screens
- Tools: Claude Design, Claude Opus 4.7, Google Stitch, Gemini 3, Nano Banana, Claude Code, Figma, Google AI Studio, Firebase, GitHub, design.md

## [Your AI UI Looks Generic… This Fixes It (DESIGN.md)](../videos/pY52H5gKhGg.md)
`pY52H5gKhGg` · Better Stack · 2026-06-02 · q2 · intro · review · also: vibe-coding-app-building, context-engineering

Google's open-sourced DESIGN.md: a repo-root markdown file of design tokens plus intent prose that keeps AI-generated UI from looking generic. Practical but thin.

- Techniques: Repo-root DESIGN.md with tokens then intent; Fixed-prompt A/B for design context; Start from a community template, then customize; Write the design rules once, not in every prompt
- Tools: DESIGN.md (Google open-source format), Cursor, Claude Code (transcribed as 'Cloud Code'), v0, Figma, CLAUDE.md, Cursor rules, Tailwind (default styling referenced in demo)

## [Why I’m Switching To Powabase for My AI Apps](../videos/wC2QpP_A9-Y.md)
`wC2QpP_A9-Y` · Better Stack · 2026-06-02 · q2 · intro · review · also: rag-retrieval, vibe-coding-app-building

Better Stack tests PowerBase, a hosted backend bundling Postgres, pgvector RAG and an agent workflow builder, by having Claude Code build a RAG chatbot over an 80s hardware catalog. One demo, no measurements.

- Techniques: Agent-driven backend setup from docs and credentials; Single-Postgres RAG with pgvector; Ingest an existing OCR text export for RAG; Corpus-bounded answers with a missing-item probe; Node-based guardrails around LLM tool use; Review the session run log
- Tools: PowerBase (powerbase.ai), Supabase, PostgreSQL, pgvector, Claude Code

## [Self-Training Agents: Hermes Agent, HF Traces, Skills, MCP & Finetuning  — Merve Noyan, Hugging Face](../videos/OV56RddyFuU.md)
`OV56RddyFuU` · AI Engineer · 2026-05-18 · q2 · practitioner · demo · also: local-ai, training-finetuning-rl, mcp-and-tools

Hugging Face's Merve Noyan demos open-model agent workflows: picking and serving open models, Hermes Agent, pushing agent traces to the Hub, HF MCP server and skills that let coding agents launch fine-tuning and batch OCR jobs.

- Techniques: Hub-ID local serving for coding agents; GGUF hardware-fit check before download; Agent-driven fine-tuning via skills; Session traces pushed to a Hub dataset; Corpus OCR via prompted batch job; HF MCP server for catalog access
- Tools: Hugging Face Hub, Hugging Face MCP server, Hugging Face skills (hub CLI, LLM trainer, Gradio, dataset), Inference Providers, Hermes Agent, Pi, llama.cpp, vLLM, MLX, LM Studio, Claude Code, Codex

## [Vibe Engineering Effect Apps — Michael Arnaldi, Effectful](../videos/Wmp2Tku2PrI.md)
`Wmp2Tku2PrI` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: context-engineering, testing-verification, agent-architecture

Michael Arnaldi builds a TypeScript Effect HTTP to-do API from an empty repo, arguing agents need the real source repo, strict lint back pressure, and generated pattern docs.

- Techniques: Clone the library source into the repo; Strict diagnostics plus lint as back pressure; AGENTS.md as a living rulebook; Spec file plus Ralph-style loop; Self-selected pattern docs; Single execute tool instead of many tools; Per-test rollback transactions for DB tests; Test layers with it.layer; Lint reference checks in CI for pattern docs
- Tools: Effect v4 (beta), Effect SQL with SQLite, Bun, Vitest, TypeScript native preview (tsgo), ESLint, OpenCode, GPT-5.4, Claude Opus, Codex, Cursor, Temporal

## [Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop](../videos/-aM2EDTiaMs.md)
`-aM2EDTiaMs` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: observability, evals, agent-architecture

Raindrop's founders argue production agent monitoring must replace evals as the main safety net, using implicit classifier signals, regex, ship-vs-control experiments, and agent self-diagnostic reports.

- Techniques: Binary issue classifiers as monitoring signals; Regex keyword signals on user messages; Percentage rollout with a control group, judged by signal rates; Self-diagnostic report tool; Natural-language signal definition (deep search); Daily triage agent over signals; Cluster by user intent and track issue rate per cluster; Trajectory search over tool-call sequences
- Tools: Raindrop, OpenTelemetry, Claude Code, Codex, OpenAI API, Sentry, Slack, BigQuery, Snowflake, Statsig

## [Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor](../videos/WE_Gnowy3uw.md)
`WE_Gnowy3uw` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: skills-self-improvement, multi-agent, evals

Cursor's David Gomes on replacing its git-worktree and best-of-N feature (about 15K lines deleted) with one markdown skill plus subagents, and what was lost in the swap.

- Techniques: Skill as the orchestrator for a stateful workflow; Best-of-N through one subagent per model; Commands instead of skills for server-controlled prompts; Prompt-level containment with system reminders; Two-scorer isolation eval run headlessly; Feeding failure cases into RL training
- Tools: Cursor (2.0 and 3.0), Cursor CLI (headless), Git worktrees, Agent skills, Subagents, Slash commands, Composer (Cursor's own model, version 2 mentioned), Braintrust, Kimi, Grok, GPT, Opus

## [Ralph Loops: Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick](../videos/2TLXsxkz0zI.md)
`2TLXsxkz0zI` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: software-factory, agent-architecture, context-engineering

Chris Parsons runs a live workshop on Ralph loops: re-running Claude Code on fresh context until work ships, fed by ticket files, a sequential queue, and reversibility limits on unattended agents.

- Techniques: Bash while-loop over fresh Claude sessions; Next-most-important-ticket selection over flat markdown tickets; Recovery check for mid-flight work; Reversibility gate with stop-and-report; Fresh-subagent adversarial review; Claude /loop for timed repetition; Resume a project in an interactive session; Simulated audience personas run in parallel subagents; Nightly session digest
- Tools: Claude Code, Codex, Cursor, n8n, Docker Sandbox, Playwright, Obsidian, Lian (embeddings CLI), Beads, Linear, Jira, Telegram

## [Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft](../videos/iOXM3zE-2dk.md)
`iOXM3zE-2dk` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: observability, evals, security-guardrails

Microsoft Foundry workshop on agent observability: trace-linked evals, stage-wise agent evaluators, OTel tracing, red teaming, and an observe skill that automates the eval-optimize loop with a human stopping regressions.

- Techniques: Trace-linked evaluation; Stage-wise agent evaluators; Bootstrapped eval dataset from instructions; Version-compare regression diff; Bounded auto-optimization with human stop; Adversarial red teaming with an attacker agent; OTel GenAI tracing with custom attributes; Eval gate on model swap
- Tools: Microsoft Foundry, Azure Monitor, Application Insights, OpenTelemetry, GitHub Codespaces, dev containers, GitHub Copilot Chat, Foundry MCP server, Azure AI Toolkit (VS Code extension), LangGraph, KQL, PyRIT (auto-caption reads it as 'pirate')

## [OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman](../videos/MhHEGMFCEB0.md)
`MhHEGMFCEB0` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: multi-agent, security-guardrails, pr-code-review

OpenAI's Codex workshop on plugins, background automations, code review, custom sub-agents with sandbox modes, guardian approvals, and stop hooks for long runs.

- Techniques: Custom sub-agent personas as TOML files; Fan-out review by file slices with an orchestrator; Read-only explorer on a fast cheap model; Parallel brainstorm of implementation options; Guardian verifier sub-agent for privileged actions; Stop hook that keeps a run going; Best-of-N cloud runs; Playwright interactive skill for visual debugging
- Tools: Codex, Codex app, Codex CLI, Codex IDE extension, Codex Code Review, Codex Security, Claude Code plugin for Codex, Playwright, ImageGen, Slack, Gmail, Google Drive

## [Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub](../videos/ClWD8OEYgp8.md)
`ClWD8OEYgp8` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: multi-agent, product-ux, context-engineering

Maggie Appleton (GitHub Next) argues agents have shifted the bottleneck from building to agreeing on what to build, and previews ACE, a shared multiplayer environment for team-plus-agent work.

- Techniques: Shared always-on agent session per task; Whole-conversation context as prompt input; Plan first, co-edit, then execute; Session summary for switching between parallel sessions; Backward-compatible PRs that link back to the session
- Tools: GitHub ACE (Agent Collaboration Environment, research prototype), Claude Opus 4.6 (model used in the demo), Bun (bun install / bun dev in the demo project), VS Code (real-time multiplayer editing in the shared cloud machine), Slack, Jira, Linear (named as coordination tools that are not built for agentic work)

## [Agents for Everything Else — swyx](../videos/zepu8Kk6FBQ.md)
`zepu8Kk6FBQ` · AI Engineer · 2026-05-18 · q3 · intro · keynote · also: enterprise-adoption, product-ux

swyx describes how the nine-person AI Engineer team runs its business with coding agents (Devin, Claude Cowork), and argues agents should handle the routine "everything else" work, not just code.

- Techniques: Figma-to-site via coding agent; Code as the CMS source of truth, maintained by an agent; Agent as ops triage for routine requests; Prioritised concern reduction for AI adoption
- Tools: Devin, Claude Cowork, Figma, Sanity, Notion, Google Sheets, Sessionize, Supabase, React, OpenClaw, tldraw

## [AgentCraft: Putting the Orc in Orchestration — Ido Salomon](../videos/kR64LOqBBCU.md)
`kR64LOqBBCU` · AI Engineer · 2026-05-18 · q2 · intro · demo · also: multi-agent, product-ux, pr-code-review

Ido Salomon demos AgentCraft, an RTS-style orchestrator for many coding agents, arguing the human is the bottleneck and offering visibility, campaigns, review bundles and shared workspaces as fixes.

- Techniques: Filesystem-projected agent map with collision heat map; Hotkey cycling to agents that need attention; Campaign mode: broad goal in a container, plan first; Review bundles with rationale and visual evidence; Best-of-N parallel attempts with human selection; Soft coordination via shared human and agent chat
- Tools: AgentCraft, MCPUI, MCP Apps, Cursor, Claude Code, Codex, OpenClaw, Git, Chrome

## [Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban](../videos/W76woOYHlvY.md)
`W76woOYHlvY` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: software-factory, product-ux, agent-architecture

Louis Knight-Webb (Vibe Kanban) argues engineers will mostly plan and review as agents run longer, then live-demos shutting his company down through the tool.

- Techniques: Task-type mode selection; Clarifying-question planning; Parallel agent workspaces; PR comment shepherding
- Tools: Vibe Kanban, Claude Code, Codex, Cursor, GitHub Copilot, Playwright MCP, GitHub, Cloudflare CDN

## ["Software Fundamentals Matter More Than Ever" — Matt Pocock](../videos/v4F1gFy-hqg.md)
`v4F1gFy-hqg` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: testing-verification, context-engineering, claude-code

Matt Pocock argues software fundamentals (deep modules, shared language, TDD, good feedback loops) matter more with AI agents, because bad code is now the most expensive it has been.

- Techniques: Grill-me interview before planning; Generated ubiquitous-language glossary; Small-step TDD with feedback loops; Codebase architecture improvement skill; Design the interface, delegate the implementation
- Tools: Claude Code

## [Taste & Craft: A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @The Pragmatic Engineer](../videos/wjk0ulMAkbc.md)
`wjk0ulMAkbc` · AI Engineer · 2026-05-18 · q3 · practitioner · interview · also: product-ux, testing-verification

Linear's CTO and Gergely Orosz on why AI makes taste and quality the scarce advantage. Linear's practices: Quality Wednesdays, a zero-bug policy, and week-long paid work trials.

- Techniques: Quality Wednesday; Zero-bug policy with agent triage; Single-shot agent PRs for incoming bugs; Human-judged feel in agent output; Paid greenfield work trial; Open, tagged customer meeting archive
- Tools: Claude Code, Opus 4.5, Linear, Apple Human Interface Guidelines

## [LLM codegen fails and how to stop 'em — Danilo Campos, PostHog](../videos/juoNbJiZUi0.md)
`juoNbJiZUi0` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: context-engineering, skills-self-improvement, security-guardrails

Danilo Campos (PostHog) on making an autonomous integration agent reliable: feed fresh docs, use thin "model airplane" example apps, breadcrumb the task, interrogate the agent at each stop, and lock down secrets.

- Techniques: Agent-selected fresh docs menu; Model airplane example apps; Breadcrumbed multi-stage prompting; Stop-hook self-interrogation; Tool-gated secret access
- Tools: PostHog Wizard, Claude Agent SDK, Claude Code, Cursor, MCP, PostHog LLM gateway

## [Building your own software factory — Eric Zakariasson, Cursor](../videos/rnDm57Py54A.md)
`rnDm57Py54A` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: software-factory, context-engineering, testing-verification

Cursor engineer Eric Zakariasson on building a "software factory": how to structure repos, grow rules from observed failures, make agents verify their own work, and automate the human loops. Practical, with a product pitch.

- Techniques: Failure-driven rule growth; Reviewer bot enforces house conventions the model lacks; Self-verification with e2e tests and recorded runs; Scoped, parallel async tasks with front-loaded specs; Per-agent VM with a single dev command; Agentic code owners with risk tiering; Loop and stall detection for background agents; Event-triggered cleanup agents
- Tools: Cursor, Cursor cloud agents, BugBot, Playwright, AGENTS.md, Linear, Slack, GitHub, Datadog, Notion, MCP, Cursor workers

## [Fighting AI with AI — Lawrence Jones, Incident](../videos/L2r6vLlLgs8.md)
`L2r6vLlLgs8` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: evals, observability, multi-agent

Lawrence Jones (Incident.io) on using AI tools to debug and improve multi-prompt AI systems: export UI traces and eval suites as file systems for coding agents, then run parallel backtest analysis pipelines.

- Techniques: Eval-tool CLI for agents; Runbook-driven prompt fix; Download trace or interaction as a file tree; Parallel per-item analysis with file-based resume; Cohort clustering over failures; Analysis as a repeatable markdown playbook; Investigate, fix, then verify in one session
- Tools: Claude Code, Codex, Go, YAML

## [A Piece of Pi: Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon](../videos/vAIDdLKB6-w.md)
`vAIDdLKB6-w` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: agent-architecture, enterprise-adoption

Matthias Luebken (Taven AI) shows how the open-source Pi coding agent, the core under OpenClaw, can be embedded in a product: an agent is a tool-calling loop, and a sales-RFP email agent is built on per-customer sessions and CLI tools.

- Techniques: Agent as tool loop with event and hook surface; Extension commands with UI selection; Per-customer agent with harness and customer files; Backend access as CLIs for the agent; Small single-purpose tools packaged as a skill; Draft-first human-in-the-loop output
- Tools: Pi, OpenClaw, Claude Cowork, FFmpeg, pandas, openpyxl, LibreOffice, AGENTS.md, NVIDIA OpenShell, TypeScript

## [How AI is changing Software Engineering: A Conversation with Gergely Orosz, @The Pragmatic Engineer](../videos/CS5Cmz5FssI.md)
`CS5Cmz5FssI` · AI Engineer · 2026-05-18 · q3 · practitioner · interview · also: enterprise-adoption, governance-compliance, infra-cost-scaling

Gergely Orosz (Pragmatic Engineer) on "token maxing": how usage leaderboards get gamed, why individual gains do not yet show up as team gains, and why big companies build their own agent infrastructure.

- Techniques: Enable non-engineers to build with coding agents; Keep agent count small and treat orchestration like tech lead mentoring; Single MCP gateway tied to service discovery; Risk-tiered code review for agent-written changes; Trade early access for structured feedback
- Tools: Claude Code, Cursor, GitHub Copilot, MCP gateway

## [Beyond Code Coverage: Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft](../videos/FWEInOtngmM.md)
`FWEInOtngmM` · AI Engineer · 2026-05-18 · q3 · practitioner · tutorial · also: testing-verification, mcp-and-tools

Marlene Mhangami (Microsoft/GitHub) argues for red-green TDD with coding agents, testing user-facing behavior with Playwright instead of unit-test coverage, and shows a live Copilot CLI demo.

- Techniques: Red-green-refactor with a coding agent; Behavior-scoped tests against user-facing or stable-contract behavior; Connect the agent to Playwright (three options); Checkpoint before the healer runs; Operational hygiene for Playwright runs; Ingest requirements from M365 with WorkIQ; Prefer direct API tests when an API exists
- Tools: GitHub Copilot CLI, Playwright, Playwright MCP server, Playwright CLI, Playwright Agents, WorkIQ, Azure AI search, Claude, Codex, Ruby on Rails, Python (Playwright binding), TypeScript (Playwright binding)

## [Claude Ultraplan vs Superpowers: I Found a WINNER and It's Not Even Close](../videos/-qFf7v2399E.md)
`-qFf7v2399E` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: claude-code, testing-verification, token-cost-efficiency

A single-repo demo comparing Claude Code's cloud Ultraplan with the Superpowers plugin for planning a release pipeline: Ultraplan is faster and cheaper but thinner, and the host plans locally about 90% of the time.

- Techniques: Launch Ultraplan from the Claude Code CLI; Review and revise an Ultraplan plan in the browser; Superpowers two-stage planning; Stop the planner from using a skill when comparing
- Tools: Claude Code (CLI), Ultraplan (Claude Code feature), Claude Code on the web (Claude Code for Web), Claude Code desktop app for Mac, Superpowers (Claude Code plugin), Claude Routines (mentioned as newly released), GitHub

## [Multica: The Open Source Tool That Makes Claude Code 10x Better](../videos/WdGSXQPwwmo.md)
`WdGSXQPwwmo` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: multi-agent, agent-architecture

Better Stack walks through self-hosting Multica on a VPS to turn Claude Code and OpenCode into assignable, scheduled agents, then judges it technical to set up and less suited to dialogue-style work than managed alternatives.

- Techniques: Self-host Multica with Docker on a VPS; Log in without the emailed code; Connect a machine as an agent runtime; Define an agent; Issue-driven task flow; Scheduled autopilot (recurring agent run)
- Tools: Multica, Claude Code, OpenCode, OpenCode Zen (big pickle model, as named in the video), Codex CLI, Hermes, Claude Routines, Claude Managed Agents, Docker, Go, Next.js, TypeScript

## [8 Vibe Coded Apps That Generated Millions Overnight](../videos/zNOunnM1jTs.md)
`zNOunnM1jTs` · AI LABS · 2026-05-02 · q2 · intro · other · also: vibe-coding-app-building, product-ux

Anecdotal roundup of eight solo, vibe-coded apps with self-reported revenue; the useful part is a few habits (small prompts, outsourced dependencies, defining an ICP first), not the numbers.

- Techniques: Incremental, chunked prompting; Minimal correct context; Model fallback chain; Design first, then modular build; Template-guided UI generation; Stack choice for AI tools; Outsource commodity operations; Real-time multiplayer transport; Define the ICP before the build
- Tools: Claude, Claude Code, Cursor, ChatGPT, Grok, Grok 3, Claude Sonnet 3.7, Gemini, GPT, Midjourney, ElevenLabs, Next.js

## [I Stopped Using Grep and My Agent Got 10x Faster](../videos/gPeWb4_DMok.md)
`gPeWb4_DMok` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: rag-retrieval, mcp-and-tools, token-cost-efficiency

Hands-on test of Claude Context, an MCP server that indexes a codebase into Zilliz/Milvus using Tree-sitter chunks, Merkle-based incremental updates and hybrid vector+BM25 search. Faster and richer on mid-size repos, slow to index on huge ones.

- Techniques: Set up Claude Context as an MCP server; Index once, then search many times; Compare indexed and plain agents side by side; Pick the repo size where the trade-off works; Test on a cheaper model to save subscription quota
- Tools: Claude Context (Zilliz MCP plugin for codebase indexing and search), Zilliz Cloud (serverless cluster), Milvus (vector database), OpenAI embeddings API, OpenCode (agent harness), GLM5 Turbo (model), Claude Code (mentioned as a possible agent), Claude Pro (subscription; weekly limit), Opus 4.7 (model, not tested), Tree-sitter (AST chunking, 9 languages), BM25 (keyword index), Merkle DAG with JSON snapshots (change detection)

## [Kimi K2.6 vs Claude Code: Why I’m Switching to the $39 Plan (Full Model Breakdown)](../videos/icbeuJxnrKU.md)
`icbeuJxnrKU` · Better Stack · 2026-05-02 · q2 · practitioner · review · also: models-research, multi-agent, token-cost-efficiency

Better Stack runs Kimi K2.6 through an agent-swarm research task, a landing-page build and a scraping web app, and finds it a modest step up from K2.5 with no token-cost data.

- Techniques: Per-entity agent swarm fan-out; Follow-up for per-item differentiation; Fix a missing feature with a targeted follow-up; Scraper stack used by the model
- Tools: Kimi K2.6, Kimi K2.5, Kimi chatbot interface (agent swarm feature), Kimi CLI (newest version, includes token counter), MoonViT (native vision encoder, open source), Hugging Face (model weights), GSAP, Node.js, Express, Axios, Cheerio, Claude Code

## [Opus 4.7 Is GREAT (except the token usage)](../videos/KZCKfhjMuOQ.md)
`KZCKfhjMuOQ` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: models-research, token-cost-efficiency, vibe-coding-app-building

Hands-on review of Claude Opus 4.7: better coding and UI, but a new tokenizer and higher default effort can burn up to 35% more tokens. Tested via single-prompt cafe site and finance dashboard builds against Opus 4.6, Gemini 3.1 and GPT 5.4.

- Techniques: Effort-level sweep before changing defaults; Same-prompt model bake-off; Re-audit old prompts after a model upgrade; Check the stack and persistence explicitly in app-generation prompts
- Tools: Claude Opus 4.7, Claude Opus 4.6, Claude Code, Gemini 3.1, GPT 5.4, Codex, Mythos (unreleased Anthropic model, mentioned only), Design Arena, Unsplash, React, Vite, React Router

## [This Tool Fixes AI Coding at Scale with 70x Fewer Tokens (Graphify)](../videos/WNru_PFycT8.md)
`WNru_PFycT8` · Better Stack · 2026-05-02 · q3 · intro · review · also: token-cost-efficiency, context-engineering, memory

Better Stack demo of Graphify, a tool that builds a relationship graph of a repo and its docs so Claude Code answers from the map instead of re-reading files. Claims over 70% fewer tokens; the evidence is one small-repo anecdote.

- Techniques: Pre-built repo knowledge graph as the agent's map; Hybrid extraction: parser for structure, LLM for meaning; Label edges with provenance and confidence; Incremental re-indexing with a persisted report
- Tools: Graphify, Claude Code, Cursor, tree-sitter

## [Anthropic Just Fixed The Token Problem](../videos/sncxStbRSwI.md)
`sncxStbRSwI` · AI LABS · 2026-05-02 · q2 · practitioner · review · also: token-cost-efficiency, multi-agent, claude-code

AI LABS walks through Anthropic's advisor strategy in Claude Code: a Sonnet executor does all the work and calls Opus only when stuck. Three anecdotal tests show it helps simple-to-medium apps but needs nudging.

- Techniques: Executor/advisor model split in Claude Code; Escalate after repeated failure; Consult before a high-blast-radius change; Name the advisor explicitly for non-trivial tasks; Choose the main model by app scope
- Tools: Claude Code, Claude Opus 4.6, Claude Sonnet, Claude Haiku, Playwright MCP, SWE-bench, Junie (JetBrains, sponsor segment)

## [Give Me 13mins, I Will Show You The Right Agent Setup](../videos/ywIhw15za9Y.md)
`ywIhw15za9Y` · AI LABS · 2026-05-02 · q2 · intro · tutorial · also: claude-code, context-engineering, testing-verification

AI LABS walks through a pre-build setup checklist for Claude Code: product-focused PRD, hand-written CLAUDE.md, agents and skills, spec-first tests, progress and learnings files, and load planning. Generic, sponsored, no benchmarks.

- Techniques: Agent-led PRD interview; Lean hand-written CLAUDE.md that links the PRD; Agent vs skill split; Path-scoped rules linked from CLAUDE.md; Negative-constraints docs file; Progress file plus learnings file; Spec-first test generation; Commit-per-implementation with worktrees; Concurrency-aware load test planning
- Tools: Claude Code, CLAUDE.md, Supabase MCP, shadcn/ui, Playwright, Playwright MCP, skill-creator, GitHub, Git (commits, worktrees), Notion MCP, Trello, OpenClaw (sponsor's skill)

## [Knowing This Gives You An Unfair Advantage With AI Coding](../videos/fMY5Sdj2DMk.md)
`fMY5Sdj2DMk` · AI LABS · 2026-05-02 · q3 · practitioner · tutorial · also: claude-code, context-engineering, testing-verification

Tutorial for writing CLAUDE.md rules that keep Claude Code on task: think-first, simplicity, surgical edits, verifiable goals, git safety, scoped rule files and a corrections log.

- Techniques: Behavioral rule block for CLAUDE.md (Karpathy-derived); Verification gate before reporting completion; List only non-default tooling; Corrections-to-learnings loop; Destructive-command confirmation rule; Path-scoped rule files and nested CLAUDE.md; CLAUDE.md structure: description first, priority tiers, length cap
- Tools: Claude Code, CLAUDE.md, AGENTS.md, Karpathy skills repo (referenced, not named as a package), Claude Chrome extension, Puppeteer MCP, Git, GitHub CLI (gh), npm, pnpm, Klaus (sponsor, AI agent hosting), OpenClaw (sponsor, open-source AI agent)

## [How IBM’s Bob uses "Review Mode" to solve the hardest coding tasks (Full Breakdown)](../videos/pSzLkt0NfJQ.md)
`pSzLkt0NfJQ` · Better Stack · 2026-05-02 · q2 · intro · review · also: pr-code-review, dev-tools

Better Stack walkthrough of IBM's Bob IDE, which separates ask/code/plan modes and runs a security Review mode with a findings panel and one-click fixes; tested on the ZBank COBOL repo, with a short sponsored-style pitch for the free trial.

- Techniques: Mode-separated agent workflow; Scoped auto-approval; Review-then-fix-then-test loop; Atomic SQLite write for a race condition
- Tools: IBM Bob, Bob Shell, IBM Granite, ZBank (open-source COBOL repo), Streamlit, SQLite, COBOL, VS Code

## [We Already Have Something Better Than Claude Design](../videos/GbuwosWEvHo.md)
`GbuwosWEvHo` · AI LABS · 2026-05-02 · q2 · intro · review · also: claude-code, product-ux, context-engineering

AI LABS argues Claude Design is mostly hype: Claude Code with Opus 4.7 can match it, and it adds Git, parallel worktrees, and skills. The evidence is one anecdotal comparison plus sponsor-heavy, unverified claims.

- Techniques: Clarifying-question skill to replace Claude Design's intake flow; Hero video background plus animation libraries; Component libraries and MCP for UI consistency; Parallel design variants in git worktrees; Prototype as HTML mock-ups
- Tools: Claude Code, Claude Design, Claude Opus 4.7, Claude Opus 4.6, GSAP, Lenis, ShadCN, ShadCN MCP server, Aceternity UI, Hero UI, scrollytelling skill, Figma

## [Why GUIs Will Replace TUIs for AI Developer Tools | Better Stack Podcast Ep. 14](../videos/zr-Xk0UVHEU.md)
`zr-Xk0UVHEU` · Better Stack · 2026-04-02 · q3 · practitioner · interview · also: pr-code-review, multi-agent, dev-tools

Better Stack podcast with Warp DevRel Ben Holmes on why GUI-style wrappers around coding agents will beat TUIs, plus practical patterns for agent code review, cloud agents, and multi-agent delegation.

- Techniques: Fresh-session review pass; Ask why, do not accuse; Two-lens review passes; Agent review as a GitHub Action; Keep READMEs and CLAUDE.md thin; Two clones instead of worktrees for parallel agents; Cloud research, then fork locally; Multi-repo sandbox environment; Route by task complexity; Tune the harness per model; Figma for design, agent for implementation
- Tools: Warp, Oz (Warp cloud agent platform), Claude Code, Codex (CLI and app), OpenCode, Pi, OpenClaw, Cursor, GitHub Copilot, Ghostty, tmux, cmux

## [Google's New CLI Is The Missing Piece for Claude Code](../videos/EKG9kX86u0s.md)
`EKG9kX86u0s` · Better Stack · 2026-04-02 · q3 · practitioner · review · also: mcp-and-tools, token-cost-efficiency, claude-code

Walkthrough of Google's new Rust Workspace CLI for agents: OAuth setup pain, CLI vs MCP token trade-offs, and design choices (nested JSON, runtime schema lookup, field masks) that keep context use low.

- Techniques: Agent-discoverable CLI with runtime help and schema; Nested JSON params flag for complex calls; Field selection to trim API responses; Layer skills on top of the CLI for guidance; Google Workspace OAuth setup for a CLI; Choose CLI vs MCP by token and portability trade-offs
- Tools: Google Workspace CLI (GWS CLI, Rust, written by a developer named Justin; no version stated), Claude / Claude Code, gcloud CLI (Google Cloud CLI, installed with Homebrew), Google Cloud Console (OAuth client, consent screen, Audience), Gmail, Google Drive, Google Slides, Google Sheets, Google Calendar (Workspace APIs used in the demos), SkillsSH (skills registry; over 100 Workspace skills), MCP (Model Context Protocol; compared, not reviewed in depth), Playwright CLI (mentioned as a prior example of an MCP server turned into a CLI; covered in an earlier video), Electrobun (Electron alternative powered by Bun; promoted at the end, not covered)

## [T3 Code: Better Than Codex?](../videos/6x7hh6Qzm9U.md)
`6x7hh6Qzm9U` · Better Stack · 2026-04-02 · q3 · intro · review · also: multi-agent, dev-tools

Walkthrough of T3 Code, an open-source desktop GUI for running multiple coding agents (currently Codex) on your existing subscription, with per-thread git worktrees, plan mode, one-click commit/PR, and a list of missing features.

- Techniques: One git worktree per agent thread; Plan first, then implement; Supervised vs full-access tool calls; One-click commit, push and PR; Quick-action buttons for setup commands; Fork the agent GUI and let the agent extend it
- Tools: T3 Code, Codex, Codex app, Claude Code, Cursor, OpenCode, Gemini, git worktrees, Finder

## [How to Use Google Stitch to Make Sites 10X More Beautiful](../videos/b0lwCDNOFUY.md)
`b0lwCDNOFUY` · AI LABS · 2026-04-02 · q2 · practitioner · tutorial · also: vibe-coding-app-building, context-engineering, skills-self-improvement

Tutorial on pairing Google Stitch with Claude Code: design.md design systems, screenshot-based redesign, Stitch skills and MCP, then React and shadcn conversion. Includes sponsor segments.

- Techniques: design.md-first design system; Extract design.md from an existing Stitch project; Screenshot as style reference (Redesign); Import style from a URL; Sketch plus theme to correct drift; Annotate-and-apply targeted edits; CLAUDE.md pipeline for Stitch skills; Convert a Stitch project to shadcn/ui
- Tools: Google Stitch, Claude Code, design.md, Stitch MCP, Stitch Enhance Prompt skill, Stitch Loop skill, Stitch React component skill, Stitch design.md skill, Google Stitch skills repo, Chrome DevTools, NanoBanana (image generation), GoFullPage (Chrome extension)

## [Qwen 3.5 Small Models Are INCREDIBLE! (Testing 0.8B & 2B On Edge Devices)](../videos/hQoF_dv2UQ4.md)
`hQoF_dv2UQ4` · Better Stack · 2026-04-02 · q3 · intro · review · also: local-ai, models-research

Hands-on offline tests of Qwen 3.5 0.8B and 2B on a laptop and iPhone: fast and surprisingly multimodal, but repetition loops and hallucinations rule out serious coding.

- Techniques: Local OpenAI-style server in LM Studio, wired into Cline; Constrain the stack so offline output has no external dependencies; On-device iPhone inference with MLX Swift; Five-prompt probe battery for tiny multimodal models
- Tools: Qwen 3.5 (0.8B and 2B, GGUF builds), LM Studio, Cline (VS Code extension; transcribed as 'Klein' and 'Climb'), MLX / MLX Swift, Swift / Xcode-style iOS app, Metal GPU, IBM Granite 4.0 nano (mentioned), Llama 2 7B (mentioned as a comparison point), Unsplash (image URLs the model hard-coded), OCRBench (benchmark named), MMLU (benchmark named)

## [How to use Claude Code and Gemini Cli Together](../videos/XdtBAm2pM-0.md)
`XdtBAm2pM-0` · AI LABS · 2026-04-02 · q3 · practitioner · tutorial · also: multi-agent, claude-code, context-engineering

Walkthrough of Agent Chatter, a shared chat layer where Claude Code, Gemini CLI and Codex agents run in tmux and coordinate through channels, with planning, peer review and loop-guard setup.

- Techniques: Shared multi-model chat via per-agent tmux sessions; Per-agent settings.json permissions instead of skip-permissions; Shared agents.md as the single instruction source; Named personas per agent; Loop guard and continue gate; Planner-first with PRD and spec templates; Three-phase presenter/challenger/synthesizer review; Planner as orchestrator with an ask-don't-assume rule; Git worktrees per agent (suggested, not tested); Initialize the app framework before starting agents
- Tools: Agent Chatter, Claude Code, Opus 4.6, Gemini CLI, Codex, Kimi, Qwen, GLM, tmux, Next.js, MCP, agents.md

## [Claude Code + CMUX: The Ultimate AI Coding Terminal](../videos/8oLP8oxqtOE.md)
`8oLP8oxqtOE` · Better Stack · 2026-04-02 · q3 · intro · review · also: claude-code, multi-agent, dev-tools

Walkthrough of cmux, a native macOS terminal whose CLI and Unix socket let Claude Code or OpenCode drive browser panes, spawn sub-agent panes, and send attention notifications.

- Techniques: Agent-driven browser pane for live testing; Sub-agents in split panes that report back and close; Attention notifications with pane flash; Sidebar status from the agent; Setup with cmux skills and hooks; Cheap demo runs by switching the model
- Tools: cmux, Claude Code, OpenCode, libghostty, Ghostty, WebKit, Bonsplit, tmux, Warp, soloterm, Demux, Haiku

## [The toolkit from Y Combinator CEO that Will Makes Claude Code Amazing](../videos/kLq5p43huYQ.md)
`kLq5p43huYQ` · Better Stack · 2026-04-02 · q3 · practitioner · review · also: claude-code, pr-code-review, testing-verification

A Better Stack walkthrough of GStack, Gary Tan's Claude Code skill pack, showing a plan, review, ship and QA pipeline that builds, tests and opens a PR for a tweet-screenshot feature.

- Techniques: Install GStack into a Claude Code project; Plan-mode CEO scope review before coding; Diff-aware review, ship and QA chain; Let the review command resolve PR review comments; Put tool preferences in CLAUDE.md, not hooks; Skill template plus generated SKILL.md
- Tools: Claude Code, GStack, Bun, Playwright, Greptile, Superpowers (Claude Code plugin), Conductor, React, Vite, TypeScript, Opus, CLAUDE.md

## [Chrome Just Became the Ultimate Agent Browser (Finally!)](../videos/51m_GGbXAng.md)
`51m_GGbXAng` · Better Stack · 2026-04-02 · q3 · practitioner · tutorial · also: mcp-and-tools, dev-tools

Chrome 144+ lets the Chrome DevTools MCP server auto-attach to your running browser for login-state debugging, element selection and network inspection, plus an experimental CLI alternative that avoids MCP context cost.

- Techniques: Attach the Chrome DevTools MCP server to your running Chrome (auto-connect); Select an element in DevTools to hand it to the agent; Isolated profile for security-sensitive use; Sandboxed MCP server with an HTTP remote debugging port; Chrome DevTools CLI instead of the MCP server; Persist the debugging profile across sessions
- Tools: Chrome DevTools MCP server (auto-connect option), Chrome DevTools CLI (experimental, in the MCP skills directory), Google Chrome 144+, OpenCode, Claude Code (terminal), Lighthouse (audit tool used by the agent), Playwright (mentioned as a comparison), Agent Browser (mentioned as the presenter's preferred tool), Comet (mentioned as an AI browser), Claude Chrome extension (mentioned), React Grab (mentioned), Arc (mentioned; the presenter wishes the feature came to it)

## [GPT-5.4: The Pros & Cons](../videos/c8b-tyFWlg8.md)
`c8b-tyFWlg8` · Better Stack · 2026-04-02 · q3 · practitioner · review · also: models-research, token-cost-efficiency, mcp-and-tools

Better Stack's 5-minute review of OpenAI's GPT-5.4: native computer use, tool search and a fast mode on the upside; slower output, a long-context price cliff and a generic UI style on the downside.

- Techniques: Tool search (deferred tool definitions); Playwright self-verification loop for front-end work; Compact context before the long-context price cliff; Fast mode as a priority tier
- Tools: GPT-5.4, Codex (5.3 referenced as the prior default), GPT-5.2 (referenced), Playwright (experimental skill), image generation skill (unnamed), Opus 4.6, Gemini, Artificial Analysis (benchmarks), Design Arena (design ranking)

## [GSD Is the Missing Piece For Claude Code](../videos/uEit1oOJK0w.md)
`uEit1oOJK0w` · AI LABS · 2026-04-02 · q2 · practitioner · review · also: context-engineering, multi-agent, testing-verification

AI LABS walks through GSD (Get Shit Done), a planning-and-execution framework for Claude Code, and compares it with BMAD and Superpowers. Main takeaway: choose the framework by how fixed your requirements are.

- Techniques: Choose the framework by requirement certainty; Per-project install with project scope; Initialise GSD on existing vs blank codebases; Keep the planning anchor short; Per-phase discuss, then concise context file; Ground phase research in docs with Context7; Adversarial plan verification and waves; Phase verification gates
- Tools: GSD (Get Shit Done), BMAD method, Superpowers, Claude Code, Claude Opus 4.6, Claude Sonnet, Next.js, Playwright, Context7 MCP, GenSpark (sponsor segment), Speakly (sponsor segment)

## [Anthropic's Head of Design Just Killed The Old Process](../videos/X4vAlWtsJD4.md)
`X4vAlWtsJD4` · AI LABS · 2026-04-02 · q2 · practitioner · tutorial · also: vibe-coding-app-building, context-engineering, product-ux

A walkthrough of how an AI Labs team now builds app prototypes: actors and constraints first, PRD and architecture files, a Next.js and Supabase prototype with mock data, then a backend added only when needed.

- Techniques: Actor-first requirements; Constraints instead of tool instructions; PRD interview prompt; Layer prompt to architecture.md; Scaffold Next.js with Supabase, then apply a frontend-design skill; Mock-data prototype for sign-off; Task lists from architecture.md; API spec from frontend code plus PRD plus architecture; Supabase MCP for schema and migrations; Front end talks directly to the database; backend only when needed; Delegate the backend layer to a cloud agent
- Tools: Figma, Next.js, Supabase, Supabase MCP, Python, Warp Oz (sponsored cloud-agent orchestration), Stripe, Google authentication, Anthropic general-purpose frontend-design skill

## [Pencil, AI Agents & The Future of Design | Better Stack Podcast Ep. 13](../videos/FqD_hlQSQIk.md)
`FqD_hlQSQIk` · Better Stack · 2026-04-02 · q3 · intro · interview · also: product-ux, multi-agent, models-research

Pencil's CEO on "vibe designing": a canvas stored as structured JSON in git that humans and agents edit together, with elicitation, parallel agents and speed as the real bottlenecks.

- Techniques: Keep the design as a structured file in the repo; Drop references into the agent chat as a rules-plus-libraries-plus-images bundle; Extract a palette from a vibe image; Partition a page across parallel agents by region; Run the same task across several models side by side; Elicit requirements before building; Correct the agent in a second round instead of restarting; Edit other regions while the agent works
- Tools: Pencil (pencil.dev), Cursor, Windsurf, Antigravity, VS Code, Codex, Claude Code, Opus 4.6, Opus 4.5, Sonnet 3.5, Sonnet 3.7, Gemini

## [The Open-Source Copilot Alternative Devs Are Switching To (Tabby)](../videos/eZ3J45K7gXU.md)
`eZ3J45K7gXU` · Better Stack · 2026-04-02 · q2 · intro · review · also: local-ai, dev-tools

Walkthrough of Tabby, a self-hosted AI coding server run via Docker and used from a VS Code extension, giving Copilot-style completions and repo-aware chat with code kept on your own machine. Short promotional demo with little exact setup detail.

- Techniques: Run a self-hosted completion and chat server, then point the IDE at it; Use selected-code actions for refactor, perf and tests; Match the model to hardware before judging quality
- Tools: Tabby (self-hosted AI coding server, Docker), VS Code (Tabby extension), Docker, GitHub Copilot, Cursor, Continue (transcribed as 'Continued Dev'), Tab9 (transcript name; likely Tabnine), Mac M4 Pro (hardware used for the demo)

## [Opus 4.6 + Agent Teams Makes Claude Code Insane](../videos/LZyWuPqvvjU.md)
`LZyWuPqvvjU` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: multi-agent, claude-code, token-cost-efficiency

Walkthrough of Claude Code's experimental Agent Teams: independent teammates with a shared task list that can message each other, viewed in tmux or in-process. Two teammates used 29% of usage, so the presenter would restrict it.

- Techniques: Enable agent teams; Give the team lead a plan and let it spawn teammates; Watch teammates in tmux; Switch teammates in a single window; Inspect team state on disk; Reserve teams for cross-checking and research
- Tools: Claude Code, Claude Opus 4.6, Claude Haiku, tmux, iTerm2, OpenCode

## [I Let 30 AI Agents Loose in My Repo (Gas Town)](../videos/_mrMidIwCzk.md)
`_mrMidIwCzk` · Better Stack · 2026-03-02 · q2 · intro · review · also: multi-agent, software-factory

A Better Stack walkthrough of Gastown, an open-source orchestrator that runs many Claude Code agents in parallel on one feature, shown on a Go to-do app with a single prompt and a candid look at the costs.

- Techniques: Mayor-decomposed parallel feature build; Git-backed orchestration state for crash recovery; Verify parallel agent output by diff and running the app
- Tools: Gastown, Claude Code, Go, SQLite, Docker, Homebrew, JWT, GitHub

## [The Correct Way to Use Claude Code Teams](../videos/MSyWjPDrHJw.md)
`MSyWjPDrHJw` · AI LABS · 2026-03-02 · q3 · practitioner · tutorial · also: claude-code, multi-agent, token-cost-efficiency

AI LABS walks through Claude Code agent teams, an experimental upgrade over sub-agents where teammates message each other directly, and shows three uses plus practical rules for keeping them on track.

- Techniques: Enable agent teams behind the experimental flag; Reviewer and fixer pair for parallel code review; Multi-perspective bug hunt; Staged build with a blocking foundation agent; Per-assignment task documents to bound scope; Lead supervision rules
- Tools: Claude Code, Claude Code agent teams (experimental), Claude Code sub-agents, Claude Opus 4.6

## [This Changed The Way I Design With AI](../videos/sdxJEd7nqiQ.md)
`sdxJEd7nqiQ` · AI LABS · 2026-03-02 · q3 · practitioner · review · also: claude-code, product-ux, skills-self-improvement

Pencil.dev design-to-code workflow with Claude Code: a file-watcher syncs .pen edits to code, subagents build pages, and a UX-audit skill raised the site grade from C to B.

- Techniques: Design file as a repo artifact; Save-triggered sync watcher; Pre-approve permissions for unattended claude runs; One subagent per page with shared docs; XML-tagged task prompts; Layer Lenis over GSAP for scroll; UX Audit skill with a scored re-run loop
- Tools: Pencil.dev, Claude Code, Claude CLI, Claude Opus 4.6, Codex, Figma MCP, Stitch, Bolt, npm, Git, GSAP, Lenis

## [What REALLY Happened When 16 Claude Agents Tried To Build a C Compiler From Scratch](../videos/SVREdZHPG1I.md)
`SVREdZHPG1I` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: multi-agent, testing-verification, agent-architecture

Better Stack breaks down Anthropic's experiment with 16 parallel Claude Opus 4.6 agents building a C compiler: git-based task locks, shared test harnesses, GCC as an oracle, and why the presenter says it was not fully autonomous.

- Techniques: Git-commit task lock for parallel agents; Isolated clones with push-to-upstream; Ralph loop with a fresh session per task; Quiet test harness with a log file; Deterministic sharded test subsets; Reference-compiler oracle for partial builds; README and progress files as cross-session memory; Role-specialized review agents
- Tools: Claude Opus 4.6, Claude (Anthropic agent), Docker, Git, GCC, Ralph loop, Linux kernel, SQLite test suite, LibJPEG test suite, Redis test suite, Rust

## [I Let Aider AI Refactor My App](../videos/cTSvN0YLMgw.md)
`cTSvN0YLMgw` · Better Stack · 2026-03-02 · q3 · intro · review · also: dev-tools, token-cost-efficiency

Short walkthrough of Aider, a terminal AI pair programmer that makes git-committed, repo-wide edits. Its architect-then-code split and per-change undo are the useful parts; the speed and cost claims are mostly unverified.

- Techniques: Architect-then-code two-pass edit; Git-as-checkpoint for agent edits; Passing-tests-plus-clean-commit as the done bar; Model swap via YAML config for cheaper runs; Diff review before accepting
- Tools: Aider, DeepSeek (cited as DeepSeq in captions), Claude (model), OpenAI models, Ollama, Flask, Flask-Login, bcrypt, React, TypeScript, tree-sitter, Git

## [OpenAI is Winning... (Opus 4.6 + Codex 5.3)](../videos/OI6DkkNDf6o.md)
`OI6DkkNDf6o` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: models-research, context-engineering

Better Stack runs Claude Opus 4.6 and GPT-5.3 Codex through an AI SDK v6 migration, a Three.js Club Penguin clone and a landing page; each test is one run, so the verdicts are soft.

- Techniques: Migration prompt with guardrails; Review the diff for reimplemented library helpers; Cross-model second opinion; Steer instead of interrupt
- Tools: Claude Opus 4.6, GPT-5.3 Codex, GPT-5.2 Codex, GPT-5.2, Claude Code, Codex app, Convex, Convex Agent package, AI SDK v6, Three.js, Terminal-Bench 2.0, Artificial Analysis

## [I Tested Every "Top" Coding Agent. Only One Survived Xcode.](../videos/J8-CdK4215Y.md)
`J8-CdK4215Y` · Better Stack · 2026-03-02 · q3 · intro · review · also: evals, models-research

Better Stack gives seven coding agents the same SwiftUI "Dog Tinder" build prompt; Claude Opus 4.6 via Claude Code is the only one that works first try and looks best, while GLM-5 fails badly.

- Techniques: Fixed-spec, first-try app build as a coding-agent eval; Check that the output opens, not just that files exist; Generate an Xcode project from a YAML spec with the codegen CLI; Use Xcode's built-in AI assistant with OpenRouter as the model backend; Give Claude Code only the permissions it needs, then let it run the whole project
- Tools: Swift, SwiftUI, Xcode, Xcode AI assistant (coding intelligence), OpenRouter, Claude Code CLI, Opus 4.6, Gemini CLI, Gemini 3 Pro (preview on CLI), Qwen CLI, Qwen 3 Coder Next, Kimi CLI

## [Copilot Helps You Type…. This Helps You Ship](../videos/LRwc64Ui_MQ.md)
`LRwc64Ui_MQ` · Better Stack · 2026-03-02 · q2 · intro · review · also: pr-code-review, context-engineering

A short walkthrough of Continue, an open-source VS Code extension for model-agnostic codebase chat, diff-based edits and markdown-defined PR review agents, positioned as complementary to Copilot.

- Techniques: Model-agnostic Continue setup; Repo-aware explanation of unfamiliar code; Review and apply diffs in chat; Markdown-defined PR review agent; Split autocomplete and review tools
- Tools: Continue (VS Code extension, open source), GitHub Copilot, VS Code, Ollama, Llama 3 (Llama3), GPT-4, Claude, OpenAI, Slack, Cursor, Claude Code

## [Vercel Just DESTROYED Port Numbers Forever (Portless)](../videos/DzGwnTbQjjg.md)
`DzGwnTbQjjg` · Better Stack · 2026-03-02 · q3 · intro · review · also: dev-tools

Short walkthrough of Portless, a Vercel Labs CLI that gives dev servers stable named localhost URLs through a local proxy instead of fixed port numbers, aimed at humans and parallel AI agents.

- Techniques: Named stable dev hostnames via a local proxy; Portless URLs without a port suffix; Debugging Portless itself; Making a framework respect a dynamic port
- Tools: Portless (Vercel Labs CLI), Bun (bun run dev in the demo), Vite, Next.js, Agent Browser (Vercel Labs; plugged for next video, not covered), JSON Render (Vercel Labs; named only in passing)

## [A Code Editor That Actually Scales](../videos/kCWwrx51IS4.md)
`kCWwrx51IS4` · Better Stack · 2026-03-02 · q2 · intro · review · also: dev-tools, claude-code

A short tour of Zed, a Rust editor pitched against Cursor on large-repo speed and real-time multiplayer. The Claude integration via ACP is the headline, but the evidence for speed is anecdotal.

- Techniques: Inline AI edit on a selection; Opt-in Claude Code sidebar; Live collaboration channel for pairing and review; Keyboard navigation for large repos
- Tools: Zed, Claude (via Agent Client Protocol, ACP), Claude Code (sidebar in Zed, transcript says 'Cloud Code'), Cursor (comparison only), GitHub (invites)

## [How To Use NotebookLM - 7 Crazy Ways](../videos/eFCHwtufjJc.md)
`eFCHwtufjJc` · AI LABS · 2026-03-02 · q3 · practitioner · tutorial · also: context-engineering, rag-retrieval, claude-code

AI LABS shows seven ways to wire Google's NotebookLM CLI into Claude Code as a grounded knowledge base: a second brain, research store, codebase onboarding, debugging KB, agent-readable visualizations, and a security handbook.

- Techniques: Install and verify the NotebookLM CLI; Notebook as project second brain via CLAUDE.md; Research offload to a notebook; Codebase onboarding via Repomix; Debugging knowledge base in place of web search; Export mind maps and tables as agent-readable artifacts; Security handbook notebook for grounded reviews; Shared notebook as knowledge base for people and other agents
- Tools: NotebookLM (Google), NotebookLM CLI (version not stated), Claude Code, CLAUDE.md, Repomix (CLI, installed via npm), GitHub CLI (gh), Gemini (answers NotebookLM queries, per the speaker), Cursor, Gemini CLI, OWASP cheat sheets, Make (sponsor, pre-built market research agent)

## [This Just Fixed 90% of AI Coding Errors](../videos/romGzY0Xu0s.md)
`romGzY0Xu0s` · AI LABS · 2026-03-02 · q3 · practitioner · review · also: testing-verification, multi-agent, skills-self-improvement

AI LABS team tests the Superpowers Claude Code plugin on a Trello-style app: enforced brainstorm, plan, subagent, TDD and review gates work, but they burn context fast and are best used selectively.

- Techniques: Install a workflow plugin from a marketplace in Claude Code; Brainstorm-gated kickoff prompt; Subagent-driven implementation with worktrees and review gates; Anti-test-edit TDD cue; Four-phase systematic debugging prompt; Compact before the next feature; Selective process use; Re-invoke skills after context loss
- Tools: Claude Code, Superpowers (Claude Code plugin), git, git worktrees, BMAD, OpenSpec, Trello (the example app being cloned)

## [Google Just Solved The Greatest Limitation of AI Agents](../videos/uprZUcv0FSc.md)
`uprZUcv0FSc` · AI LABS · 2026-03-02 · q3 · practitioner · review · also: mcp-and-tools, voice-multimodal

Walkthrough of WebMCP, a proposed browser standard where websites register callable tools for agents instead of agents guessing from screenshots or DOM. Covers declarative and imperative APIs, per-page tool loading, and current limits.

- Techniques: Declarative WebMCP tool on an HTML form; Imperative WebMCP tool registration per route; Scope tool lists to the page (contextual loading); Write tool descriptions for a cold reader; Inspect tool schemas with the Model Context Tool Inspector extension; Test with the Gemini-backed demo paths
- Tools: WebMCP, Chrome Canary, Chrome 146, Chrome Labs WebMCP repo, Model Context Tool Inspector extension, Claude Code, Gemini (built into Chrome; Gemini API key option in the demo), Next.js, React, Zen browser, Community WebMCP bridge (unnamed, not identified), Brilliant (sponsor)

## [I thought I was a Senior React Dev... until I ran React Doctor.](../videos/k3vyIIEZfU4.md)
`k3vyIIEZfU4` · Better Stack · 2026-03-02 · q2 · intro · review · also: dev-tools

A short walkthrough of React Doctor, a Rust-fast (OXLint-based) CLI that flags React anti-patterns, shown on an old personal project and an open-source CRM monorepo.

- Techniques: Run a React anti-pattern scan on a repo; Fix the three demonstrated findings; Use the scanner as a coding-agent skill
- Tools: React Doctor (CLI, Aidan Bai), OXLint (Rust-based JavaScript linter), React, Recharts, Node.js (programmatic API), Million.js (creator's earlier project, mentioned), React Grab (creator's project, mentioned), React Scan (creator's project, mentioned), Amy (named as a creator project, caption may be imprecise), Twenty (open-source Salesforce-alternative CRM, captioned as "20"), useTransition (React hook referenced)

## [We Tested The Smallest "OpenClaw" AI Agent in the World (zclaw)](../videos/MCTTe8nZEgc.md)
`MCTTe8nZEgc` · Better Stack · 2026-03-02 · q2 · intro · review · also: agent-architecture, dev-tools

Better Stack installs zclaw, a tiny ESP-IDF AI assistant for ESP32 boards driven over Telegram, then adds a custom display tool; a hands-on hardware demo with reproducible setup steps and candid limits.

- Techniques: zclaw install and provisioning flow; Wi-Fi bench workaround; Adding a custom tool to zclaw; Natural-language pin aliases stored on-device; Hello-world LED sanity circuit; Telegram allow-list for device control
- Tools: zclaw, ESP32, ESP32-C3, ESP-IDF, Telegram, BotFather (Telegram bot), Telegram user-info bot, OpenRouter, OpenAI, Anthropic, Ollama, Claude Code

## [Is This A Better Way to Use Git?](../videos/3BAhV2xpzZ8.md)
`3BAhV2xpzZ8` · Better Stack · 2026-03-02 · q3 · intro · review · also: dev-tools

A 5-minute walkthrough of GitButler, a GUI layer over Git that adds virtual branches, AI commit messages, and easier history rewriting, with an honest pros and cons take.

- Techniques: Virtual branches for parallel work on one working tree; AI-generated commit messages; Drag, squash and amend commits with undo; Open a PR from the app; Adoption path for GitButler
- Tools: GitButler (GUI and CLI, beta, free during beta per the presenter), Git, GitHub, VS Code, Claude, Cursor, MCP

## [How I Turned Claude Into a Design Tool with Pencil.dev](../videos/DFcvz2kcR74.md)
`DFcvz2kcR74` · Better Stack · 2026-03-02 · q2 · intro · review · also: vibe-coding-app-building, mcp-and-tools

Walkthrough of Pencil, a free agent-driven design tool that Claude Code can drive over MCP to build dashboards and a bakery website, then code them. Shows a workable loop, with no benchmarks.

- Techniques: Drive a design tool from Claude Code via its MCP server; Build a UI from a UI kit; Blank-canvas site generation with a style guide; Fix AI design output by direct manipulation; Hand designs to the agent for implementation; Import existing Figma designs
- Tools: Pencil (pencil.dev), Pencil MCP server, Pencil batch design tool, Claude Code, Figma, Figma MCP tool, Sketch, Sketch MCP tool, Lunaris UI kit, Halo UI kit, Nitro UI kit, Unsplash

## [I Didn't Expect This From OpenAI's IDE](../videos/sC4JpJlD3aQ.md)
`sC4JpJlD3aQ` · AI LABS · 2026-03-02 · q3 · intro · tutorial · also: multi-agent, vibe-coding-app-building, skills-self-improvement

A 7-minute build log: turning a car photo into a 3D hero section for a Next.js landing page with Tripo 3D, OpenAI's Codex app, GSAP and Aceternity UI, with parallel Codex subagents in git worktrees.

- Techniques: Pre-clean the image for image-to-3D; GLB asset in a Next.js public folder; Generate a project skill with the agent's skill creator; Work around agent install timeouts; Parallel subagents in separate git worktrees; Scope the agent with explicit do-not-touch constraints; Fix visual drift with screenshots and named variants
- Tools: Codex app (OpenAI), Tripo 3D, Canva background remover, Next.js, GSAP, Aceternity UI, React Three Fiber, post-processing package for React Three Fiber (named 'Post Processing' in the transcript), npm, GLB (file format), Antigravity (agent manager, compared in passing), Claude Code (mentioned as the previous agent used)

## [Qwen 3.5 The FREE AI Model That Claims to Beat Sonnet 4.5](../videos/y8JWZQpWbxQ.md)
`y8JWZQpWbxQ` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: models-research, local-ai, evals

Better Stack runs three coding tasks (todo app, Three.js solar system, tweet-screenshot feature) comparing Qwen 3.5 35B on OpenRouter against Claude Sonnet 4.5, and finds Sonnet ahead on all three; the takeaway is to run your own evals, not trust benchmarks.

- Techniques: Three-tier hands-on model bake-off; Pin the harness before comparing models; Check the project layout, not only whether the app runs; Check whether a fix targets the root cause; Code-structure review of generated components
- Tools: Qwen 3.5 (medium series, 35B; 400B max-thinking variant mentioned), Claude Sonnet 4.5, Claude Opus 4.5 (benchmark comparison only), Claude Code, Claude Cowork (mentioned), OpenCode, OpenCode Go (model list, mentioned), OpenRouter, superpowers skill (OpenCode), React, Vite, Three.js

## [How Is This Almost as Good as Opus?](../videos/B6P0Fn6xYfo.md)
`B6P0Fn6xYfo` · Better Stack · 2026-03-02 · q2 · intro · review · also: models-research, token-cost-efficiency, local-ai

A one-prompt Kanban build comparison of open-weight MiniMax M2.5 against Claude Opus 4.6: near-equal results at roughly a tenth of the price, with UI gaps and one missed feature.

- Techniques: Single-prompt head-to-head build eval; Cost-per-task estimate instead of per-token price; Open-weight model as a drop-in cheap tier
- Tools: MiniMax M2.5, Claude Opus 4.6, Cursor, Ollama, Hugging Face, SWE-Bench Verified, Multi-SWE-Bench, Droid benchmark (as named in the video), GPT-5 (comparison only), Gemini 3 Pro (comparison only), MiniMax M2.1 (predecessor, comparison only)

## [OpenClaw Use Cases That Are Actually Insane](../videos/hp7n45JqvIw.md)
`hp7n45JqvIw` · AI LABS · 2026-03-02 · q2 · practitioner · review · also: agent-architecture, software-factory

AI LABS walks through weeks of running OpenClaw on a Mac Mini for developer ops: dependency upgrades, cost and uptime monitoring, SEO checks, PRD-to-deploy builds, cold-email drafts and Claude Code delegation.

- Techniques: Guideline-driven dependency upgrade cron; Scheduled research briefing; Cost watchdog skill; Hosted-app heartbeat monitor; SEO heartbeat; PRD-to-deployed-app run; Delegate to Claude Code with subtasks and per-step commits; Draft-only cold outreach via cron; Email triage heartbeat
- Tools: OpenClaw, Claude Code, Codex, Gemini 3, Nano Banana Pro (Google image-generation skill, bundled with OpenClaw), Nano Banana (earlier skill referenced), GOG CLI, Google Workspace CLI, Google Cloud console, AWS CloudWatch, Vercel, GitHub

## [This Sandbox Tool Makes Claude Code Unstoppable (Code On Incus)](../videos/t78-JUnTK5Q.md)
`t78-JUnTK5Q` · Better Stack · 2026-03-02 · q3 · practitioner · tutorial · also: sandboxing-execution, security-guardrails

Better Stack walkthrough of Code On Incus (COI): running Claude Code agents in isolated Incus system containers on a Mac via Colima, with a malware-file triage demo.

- Techniques: Nested sandbox on macOS: Colima, then Incus, then COI; Bridge networking fix for Incus; Build COI from the cloned repo; Launch per-role agents into slots with a shared workspace; Analyze untrusted files inside the sandbox
- Tools: Code On Incus (COI), Incus, Colima, Claude Code, Docker, incus file push, coi build, incusbr0 (Incus bridge), EICAR test file, SWAPI (Star Wars API; auto-caption says 'Swoppy')

## [Native Worktrees Just Killed Traditional Claude Code Workflows](../videos/lj_xZn-Yf18.md)
`lj_xZn-Yf18` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: claude-code, multi-agent, dev-tools

A 4-minute walkthrough of Claude Code's native git worktree support: run parallel feature branches in isolated worktrees, resume them by name, and use worktree-isolated subagents, with a note on a recent breakage.

- Techniques: Parallel feature branches with named worktrees; Isolate a broken feature and ship the rest; Return to or resume a worktree; Open a shell in a worktree directory with tmux; Worktree isolation for custom subagents; Clean up temporary worktrees
- Tools: Claude Code, Claude Desktop, git, React, tmux, Claude Squad, React Doctor, SVN, Jujutsu

## [Vite, Rust & The Future of JavaScript Tooling | Better Stack Podcast Ep. 11](../videos/LSGZtHafiM4.md)
`LSGZtHafiM4` · Better Stack · 2026-03-02 · q4 · practitioner · review · also: dev-tools, context-engineering

Vite creator Evan You explains why the Vite toolchain is moving to Rust (Rolldown, OXC), the unified Vite+ CLI, guardrails for agent-written code, and his skepticism about React Server Components.

- Techniques: Pre-bundle dependencies in dev, serve source as native ESM; Bundle for production when module count crosses a threshold; Built-in transforms instead of plugin chains; Check the data-boundary cost before offloading to native code; Arena-allocate ASTs in one contiguous buffer; One config, one resolver for the whole toolchain; Vite+ commands and version pinning; Ship AGENTS.md and skills with the package, patched on upgrade; Guardrails against agent shortcuts in PR review; Schedule debt-paydown passes between feature pushes; Plan mode, then write AGENTS.md, and run agents in parallel; Run downstream ecosystem CI before a major release
- Tools: Vite (v7 current, v8 in beta per the speaker), Vite+ (vp CLI), Rollup, Rolldown, esbuild, webpack, Rspack, SWC, OXC (parser, resolver, transformer, minifier), oxlint, oxfmt, Vitest (auto-caption 'VTest')

## [Playwright CLI vs MCP Server: Which is Actually BETTER for Claude Code?](../videos/V2qjnBDZZ7A.md)
`V2qjnBDZZ7A` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: mcp-and-tools, token-cost-efficiency, testing-verification

Better Stack runs the same Twitter-video download task through the Playwright CLI and the Playwright MCP server in Claude Code, and finds the CLI cheaper in context, with MCP better for portable agent loops.

- Techniques: Drive the browser through a CLI skill instead of an MCP server (in Claude Code); Turn a repeated browser check into a bash script for humans and agents; Keep MCP for portable agent loops and trim its tool list
- Tools: Playwright CLI, Playwright MCP server, Claude Code, agent-browser (a Rust CLI that runs Playwright under the hood; spelled 'Vasell' in the auto-captions)

## [Why is Everyone OBSESSED With The New Kimi K2.5 AI Model](../videos/KvOYDevFGiw.md)
`KvOYDevFGiw` · Better Stack · 2026-02-02 · q3 · intro · review · also: models-research, multi-agent, vibe-coding-app-building

Hands-on review of Moonshot's open-weight Kimi K2.5: video-to-website cloning, a single-image campaign site, and the Agent Swarm feature, with the speaker's verdict that the front-end output is strong but the research output had stale data.

- Techniques: Reference-video to front-end clone; Single-image creative brief; Force subagent fan-out by naming it in the prompt; Check the as-of date of generated research
- Tools: Kimi K2.5, Kimi CLI, FFmpeg, Claude Code, Kimi K2, Llama 4 Scout, GitHub Copilot

## [Anthropic Shows What Most Developers Are Missing](../videos/LC7kGTDoWRY.md)
`LC7kGTDoWRY` · AI LABS · 2026-02-02 · q2 · intro · news · also: multi-agent, testing-verification, enterprise-adoption

AI LABS argues that engineering is shifting from writing code to orchestrating agents, reviewing exceptions, and stating intent clearly, with a short sponsored segment and little measured evidence.

- Techniques: CLAUDE.md verification loop for long autonomous runs; Commit each verified unit, with decisions in the message; Split work into small independent units and run agents in parallel; Custom specialist subagents with chosen models and instructions; Plan mode with agent questions before building; Agent first-pass review with human review of exceptions; Layered security agents plus an external scanner
- Tools: Claude Code, CLAUDE.md, Claude Chrome extension, Puppeteer MCP, git, CodeRabbit, Cowork (Anthropic), Claude Opus 4.5, GPT-5.2, Golang, COBOL, Fortran

## [AI, Terminal Tools & Building a Supportive Developer Community | Better Stack Podcast Ep. 10](../videos/SwYENemHJp4.md)
`SwYENemHJp4` · Better Stack · 2026-02-02 · q2 · intro · interview · also: dev-tools

Better Stack podcast ep. 10: guest Bash Bunny (ex-Charm) on switching to Doom Emacs and org mode, Sway and Linux, and a case for limiting AI in hobby work; mostly anecdote.

- Techniques: Ease into Vim motions with VS Code Vim keybindings, then VimTutor; Doom Emacs command discovery via M-x; Org mode task basics; End-of-day brain dump, one dated file per day; Keep inline completion on, but write the code yourself; Scoped AI questions, then implement by hand; Learn an OSS feature by reading its introducing PR; Trust filter for OSS learning sources; Docs-first, then tweak and break the example; Remote development from a Mac into a Linux machine; Time-boxed MVP with visible pain points
- Tools: Neovim, Vim, VimTutor, Doom Emacs, Emacs, LazyVim, LunarVim, Org mode, Notion, Obsidian, Trello, Cursor

## [Is Kimi K2.5 Actually The Best Open Source Model?](../videos/D4ICNmfXmwI.md)
`D4ICNmfXmwI` · AI LABS · 2026-02-02 · q2 · practitioner · review · also: models-research, multi-agent

AI LABS hands-on test of Moonshot's Kimi K2.5: open-weight, not open-source; agent-swarm migration was not faster on a large codebase, while a Notion-clone-from-video test worked after one follow-up prompt.

- Techniques: Parallel per-group migration with a sub-agent per page group; Post-migration cleanup pass; Video-as-input UI cloning; Iterate on broken features with a follow-up prompt
- Tools: Kimi K2.5 (Moonshot AI, open-weight, 1T total / 32B active MoE), Kimi Code CLI (agent CLI released with Kimi K2.5), ShadCN UI, Material UI, Claude Opus 4.5 (used as a comparison model), Claude Code (compared for sub-agent behavior and pricing), Notion (cloned from screen recording), DeepSeek (architecture comparison only), Opera Neon (sponsor, agentic browser)

## [Claude Code's HIDDEN Agent Swarm (Better Than Kimi K2.5?)](../videos/eRu5kIYAAz8.md)
`eRu5kIYAAz8` · Better Stack · 2026-02-02 · q2 · intro · review · also: claude-code, multi-agent

Better Stack demos an unreleased Claude Code "agent swarm" mode, hidden behind a flag, where an orchestrator spawns specialized sub-agents on the fly, then argues Anthropic is unlikely to ship it soon as-is.

- Techniques: Plan-file to swarm execution (reproducing the demo); Checking existing sub-agents before a swarm run; Manual sub-agent memory via shared markdown files
- Tools: Claude Code, Claude Sneak Peek (fork of CC Mirror), CC Mirror, Kimi K2.5, Opus (mentioned as a benchmark comparison, no version detail), XDL (X/Twitter video downloader, the demo target), Better Stack (log monitoring, anomaly detection, AI-native error tracking)

## [The Open Models Have Caught Up (MiniMax M2.1 & GLM 4.7 Review)](../videos/TsdFAwOcvTM.md)
`TsdFAwOcvTM` · Better Stack · 2026-02-02 · q3 · practitioner · review · also: models-research, token-cost-efficiency

Hands-on review of MiniMax M2.1 and GLM 4.7 against Sonnet 4.5, Opus 4.5 and Gemini 3 Pro on UI design and a full app build; open-weight models are cheap and strong on design, but first-attempt completion and backend correctness lagged.

- Techniques: Same-prompt cross-model bake-off; Continue-until-done follow-up; Cost-to-done accounting; Thinking-loop recovery
- Tools: MiniMax M2.1, GLM 4.7, Claude Sonnet 4.5, Claude Opus 4.5, Gemini 3 Pro, OpenCode, OpenRouter, Design Arena, Next.js (transcribed as NextGest), Drizzle ORM, SQLite

## [This is How I Design With Stitch Now](../videos/VNx9Gy5pHZI.md)
`VNx9Gy5pHZI` · AI LABS · 2026-02-02 · q3 · practitioner · tutorial · also: mcp-and-tools, testing-verification, vibe-coding-app-building

A Stitch-as-MCP design workflow in Claude Code: plan first, generate one long landing page, pull its HTML, then test with Vercel's snapshot-based Agent Browser. The Stitch MCP wrapper is unofficial.

- Techniques: Stitch MCP for agent-driven design generation; Plan-mode UI guide before design; One long page prompt instead of per-section prompts; Pulling Stitch screen code into a project; Follow-up refactor after code dump; CLAUDE.md rules that mandate a test tool; Snapshot-driven UI testing with Vercel Agent Browser
- Tools: Google Stitch, Stitch MCP (community, unofficial), Google Cloud SDK / gcloud CLI, Homebrew (brew), Claude Code (plan mode, CLAUDE.md), Gemini 3 Flash, Next.js, curl, Vercel Agent Browser, Claude's Chrome extension (compared), Playwright (compared), Puppeteer (compared)

## [I Can't Believe Anthropic Messed Up The Ralph Wiggum](../videos/XVAhQ-EcrWA.md)
`XVAhQ-EcrWA` · Better Stack · 2026-02-02 · q3 · practitioner · tutorial · also: agent-architecture, context-engineering, claude-code

Better Stack explains the Ralph loop (a bash while-loop that reruns one prompt with a fresh context each time) and why the official Claude Code Ralph plugin, with compaction and iteration caps, drifts from the canonical design.

- Techniques: Fresh-context bash Ralph loop; Plan-file task selection; Keep fixed context small; Human-on-the-loop review; GitHub-issues task queue; Filter error output with an MCP server
- Tools: Ralph loop (bash while-loop pattern), Claude Code, Claude Code Ralph Wiggum plugin (Anthropic, slash command with max iterations and completion promise), agents.md, Raz Mike's Ralphie bash script, agent-browser tool (named Vasell in the captions), GitHub issues, Better Stack MCP server (log and frontend error search), GPT-5 tokenizer (used for a token-count comparison)

## [Skills Had ONE Job (They Failed)](../videos/i0W90tlKfYg.md)
`i0W90tlKfYg` · Better Stack · 2026-02-02 · q4 · practitioner · review · also: context-engineering, skills-self-improvement, evals

Vercel's Next.js eval found a passive AGENTS.md doc index beat on-demand skills (100% vs. skills that were often never invoked); skills suit explicit workflows, AGENTS.md suits framework knowledge.

- Techniques: Passive documentation index in AGENTS.md; Split context by trigger type; Measure skill trigger rate, not just existence
- Tools: Next.js, Agent Skills (open standard, Anthropic), Vercel skills CLI and skills repository (named as 'skill CLI' in the transcript), AGENTS.md, CLAUDE.md

## [Claude Now Builds Custom Interfaces to Plan Your Life](../videos/jRBiWoSKpIo.md)
`jRBiWoSKpIo` · Better Stack · 2026-02-02 · q2 · intro · review · also: claude-code, mcp-and-tools

A 4-minute demo of Claude Canvas, an open-source Claude Code plugin that opens tmux split panes rendered with Ink to preview emails, flights and calendar items, with the pane sending user choices back to Claude. The data shown is invented, and the "future of terminal assistants" claim is opinion.

- Techniques: Skill-routed CLI that spawns a split pane; Preview a draft in a pane before sending; Bidirectional pane-to-agent IPC for user selections
- Tools: Claude Code, Claude Canvas (Claude Code plugin), tmux, bun, Ink, Ghostty, iTerm, Apple Terminal, Gmail MCP server (mentioned as a possible source of From/To fields, not demoed), Astro (creator mentioned as suggesting generated UI)

## [I Couldn't Believe Claude Tasks Could Do This](../videos/li8bIt-mjbA.md)
`li8bIt-mjbA` · AI LABS · 2026-02-02 · q2 · intro · review · also: claude-code, multi-agent, agent-architecture

Walkthrough of Claude Code's new built-in task system: a coordinator splits work into a dependency graph, runs independent sub-agents in parallel, and persists tasks outside the context window so they survive /clear and restarts.

- Techniques: Explicit dependency breakdown prompt; Fan out independent sections of a spec; Named long-running sessions; Inspect task state on disk; Batch folder documentation with Cowork; Research-then-implement handoff
- Tools: Claude Code, Cowork, Claude Chat, Opus 4.5, Haiku, Sonnet, CLAUDE.md, Notion, Lovart (sponsor segment, not evaluated)

## [Anthropic's Latest Move: Why OpenCode Users Are Worried](../videos/vLecpJt_8jM.md)
`vLecpJt_8jM` · Better Stack · 2026-02-02 · q2 · intro · news · also: claude-code, token-cost-efficiency, governance-compliance

Speaker reports Anthropic restricting Claude Pro/Max subscriptions to Claude Code, hitting third-party agents like OpenCode, and describes a temporary tool-name workaround. Mostly speculation.

- Techniques: Keep the harness model-agnostic and route each workflow to a cheaper or better model; Use subscription quota first, then fall back to API billing; Tool-name prefix workaround reported by OpenCode (unverified; the speaker says it is temporary)
- Tools: Claude Code, Claude Pro, Claude Max, Claude Opus 4.5, OpenCode, OpenCode Black, OpenCode TUI, ClaudeBot, Ralph loop, npm, GitHub, OpenAI models

## [Why Google Antigravity Suddenly Makes Sense](../videos/e4giCKHIJy8.md)
`e4giCKHIJy8` · AI LABS · 2026-02-02 · q2 · practitioner · review · also: context-engineering, testing-verification, skills-self-improvement

A walkthrough of Google Antigravity as a coding agent, using Cursor's published harness principles: plan-first with commented revisions, on-demand context, TDD, Git as knowledge base, and skills-based debug mode.

- Techniques: Comment-driven plan revision; On-demand context instead of manual file tagging; Conversation reset policy; Project rules as markdown in .agent/rules; Skill folders following Anthropic's open standard; TDD with a committed test baseline; Screenshot as design and bug input; Git workflows as reusable commands; Agent-run code review with severity sorting; Parallel agents on separate branches; Skill-based debug mode; Watch the agent and redirect early
- Tools: Google Antigravity (AI code editor with planning mode, rules, skills and workflows), Gemini 3 (model used in Antigravity), Claude Code, Claude Opus, Cursor, Cursor's agent harness article (referenced, not named as a product), Anthropic's long-running agent harness (referenced), Anthropic's open Agent Skills standard (SKILL.md), Git, GitHub (built-in PR code review), CodeRabbit, Sentry

## [The Greatest Problem With AI Coding Is Solved](../videos/3FZIdRZsUMM.md)
`3FZIdRZsUMM` · AI LABS · 2026-02-02 · q2 · intro · talk · also: context-engineering, testing-verification, claude-code

AI LABS argues the implementation middle of software work is being replaced by agents, so developers should focus on planning, context setup, and reviewing or testing agent output.

- Techniques: Refine the plan, then run one-shot implementation; Split spec into per-concern documents; Test-first with a context reset and locked tests; Black-box testing from user stories with a browser agent; White-box review with an XML test plan and a slash command; Layered project structure for agents
- Tools: Linear, Dart AI, VS Code, Claude Code, Claude Chrome extension, Cursor, Slack, CLAUDE.md, skill.md, MCP, XML

## [How I Made Claude Code WAY Better With Vercel Agent Skills](../videos/PkeC2hNQ9Zw.md)
`PkeC2hNQ9Zw` · Better Stack · 2026-02-02 · q2 · intro · review · also: skills-self-improvement, claude-code

Better Stack explains the Agent Skills format, Vercel's add-skill installer and skills.sh discovery, and Cloudflare's proposed well-known skills index, then closes with a sponsor read.

- Techniques: Write a skill file with frontmatter; Install one skill into several agents; Discover skills by popularity; Publish a skill index at a well-known path (proposal)
- Tools: Claude Code, Agent Skills (Anthropic), add-skill (Vercel, npx add-skill), skills.sh, Cloudflare well-known skills index proposal, Cursor, Wrangler, Remotion, React Native skills, Better Stack

## [Claude Code Can Now Control Your Browser (Thanks to Vercel)](../videos/P7JrP57AxR0.md)
`P7JrP57AxR0` · Better Stack · 2026-02-02 · q3 · practitioner · review · also: testing-verification, voice-multimodal, mcp-and-tools

Walkthrough of Vercel's open-source Agent Browser, a headless-Chromium CLI that lets a coding agent snapshot, click and test web pages, with a comparison to Browser Use and the Playwright MCP server.

- Techniques: Agent-driven UI verification loop; Install the CLI globally and let the agent discover it; Generate a bash regression test from the browser session; Prefer snapshot references, fall back to semantic locators
- Tools: Agent Browser (Vercel, open source), Rust, Node.js, Playwright, Chromium, OpenCode, GLM 4.7, npm, shadcn/ui (transcribed as 'Shadxian'), React (transcribed as 'Riat'), Vite, Browser Use

## [Cursor 2.0 Changes Everything - It Feels Illegal](../videos/4QUBKKX2ktQ.md)
`4QUBKKX2ktQ` · Better Stack · 2026-01-02 · q2 · intro · news · also: multi-agent

A 4-minute Better Stack overview of Cursor 2.0 (Oct 2025 release): the Composer model, up to eight parallel agents in isolated worktrees, and a built-in browser, with mostly unquantified claims and a sponsor plug.

- Techniques: Parallel agents in isolated work trees; Assign, then verify diffs; Check the privacy opt-out before use; Starter run from the video
- Tools: Cursor, Cursor Composer model, Cursor built-in browser, Claude (as the latency comparison), VS Code (Cursor is a fork of it), ChatGPT (mentioned in passing), SWE-bench Verified, Better Stack (sponsored logging plug)

## [The Best MCP Servers of 2025](../videos/kRxdsv1ZY1E.md)
`kRxdsv1ZY1E` · AI LABS · 2026-01-02 · q2 · intro · review · also: mcp-and-tools, context-engineering

AI LABS roundup of six MCP servers for AI coding agents: Context7, Docker MCP, ShadCN, Google's managed servers, Notion and Supabase. Anecdotal, partly sponsored, and thin on measurements.

- Tools: Model Context Protocol (MCP), Context7, Ref, Docker MCP (MCP Find, MCP Add), Cloudflare code mode (concept), ShadCN registry MCP, shadcn components.json, Aceternity UI, Magic UI, Gemini 3, Google Maps MCP, BigQuery MCP

## [Google's Biggest Fail of the year](../videos/PB9sJnZyQ7g.md)
`PB9sJnZyQ7g` · AI LABS · 2026-01-02 · q2 · intro · review · also: context-engineering, testing-verification

A solo review of Google's Conductor, a Gemini CLI extension for spec-driven "track" workflows. The host finds the file layout sound but the command instructions weak, with destructive and falsely-completed steps.

- Techniques: Per-track spec + plan with a status index; Commit per task with git notes and git-aware revert; Default test gate on every task; Review each generated doc before auto-generation; Scope context updates to what changed; Verify completion against real state
- Tools: Conductor (Google Gemini CLI extension), Gemini CLI, Gemini (model), Claude Code plugins (mentioned as comparison), BMAD (recommended alternative), Supabase, npm, pnpm, git, git notes, GitHub

## [Inngest's New Tool Is Insane For AI Coding](../videos/8vvTHnta59A.md)
`8vvTHnta59A` · AI LABS · 2026-01-02 · q2 · intro · review · also: mcp-and-tools, testing-verification

Short demo of Inngest's MCP server for its local dev server, showing a coding agent sending test events, polling run status and checking its own workflow runs in Claude Code.

- Techniques: Wire an event-driven dev server into Claude Code via MCP; Agent-driven verify loop: send event, poll run, check result; Switch model provider through a gateway in one prompt
- Tools: Inngest, Inngest dev server, Inngest MCP server, Claude Code, Cursor, Next.js, OpenAI API, Vercel AI Gateway (auto-captioned as 'Versal'), Puppeteer MCP, CLAUDE.md, .mcp.json

## [Building a One-Man Empire with AI & the Future of Developer Education | Better Stack Podcast Ep. 9](../videos/XG6ToBSg2HU.md)
`XG6ToBSg2HU` · Better Stack · 2026-01-02 · q3 · practitioner · interview · also: dev-tools, infra-cost-scaling, data-engineering

Better Stack podcast with solo developer David Flanagan (Raw Code Academy) on running a one-person, AI-assisted business: Cloudflare automation, LLM transcript correction, Kubernetes vs serverless cost trade-offs, QEnv and Dagger.

- Techniques: LLM-assisted transcript correction loop; Cron-driven content publishing on Cloudflare Workers; Spec-first delegation to coding agents; Hierarchical env with secret references (QEnv); Per-package CI definitions in a monorepo; Dagger pipelines in TypeScript; Cost-inflection planning for hosting; Reproducible machine via NixOS config
- Tools: Cloudflare Workers, Cloudflare R2, Cloudflare D1, Cloudflare service bindings, Gemini 3, Claude Code, Codex, Droid (multi-model agent CLI), Deepgram Nova 3, Whisper, ElevenLabs, Bluesky

## [Anthropic Released A New Way To "Vibe Code"](../videos/XWp4k9K6oK8.md)
`XWp4k9K6oK8` · AI LABS · 2026-01-02 · q3 · practitioner · tutorial · also: context-engineering, agent-architecture, testing-verification

Anthropic's long-running-agent harness: an initializer agent sets up a JSON feature list, progress file and git repo, then a coding agent implements one feature per session with browser testing and commits, so work survives compaction.

- Techniques: Initializer + incremental coder harness; Forced browser verification via Puppeteer; Resume from state, not from context
- Tools: Claude Code, Claude.md, Puppeteer, Git, Next.js, BMAD

## [Claude Released Something To Fix Your Errors](../videos/NuKrtiJqW3Y.md)
`NuKrtiJqW3Y` · AI LABS · 2026-01-02 · q2 · practitioner · tutorial · also: testing-verification, context-engineering, voice-multimodal

Tips for testing web apps with Claude Code's Chrome extension: full-page screenshot scripts, CLAUDE.md context and cookie-banner rules, split test files, progress reports across compaction.

- Techniques: Full-page screenshot script behind a slash command; CLAUDE.md rule to limit DOM extraction; Cookie-banner dismissal script run first; Authenticate before handing off the task; Split end-to-end testing into per-area test files; Progress report after each test file; Compact and check context before browser test runs; Guided testing slash command
- Tools: Claude Code, Claude Code Chrome extension (Claude in Chrome integration), Playwright MCP, Puppeteer MCP, Google Chrome, Google Docs, Google Sheets, CLAUDE.md, Chrome Manifest V3 extensions

## [GitHub’s New Secret Copilot Model Is Shockingly Fast](../videos/lYCma3E1zdk.md)
`lYCma3E1zdk` · Better Stack · 2026-01-02 · q2 · intro · review · also: models-research

Better Stack tries GitHub Copilot's preview model Raptor Mini on a satellite-tracking dashboard. Fast first pass, but the evidence is one demo with no benchmarks.

- Techniques: Spec bundle for one-shot app generation; Stepwise visual upgrade with an asset; Prefer a minimal stack for prototypes
- Tools: GitHub Copilot, Raptor Mini, GPT-5 mini (per public reporting cited by the speaker), Claude (mentioned as a larger comparison model), Express, vanilla JavaScript, CSS, Three.js, N2YO API, Figma, SVG, Next.js (mentioned as the alternative not used)

## [Claude Cluster is Insane… Upgrade Your Claude Code Workflow ](../videos/V-xBaFveTvA.md)
`V-xBaFveTvA` · AI LABS · 2026-01-02 · q2 · intro · review · also: claude-code, multi-agent, dev-tools

AI LABS walkthrough of Claude Code background subagents, using git worktrees to run parallel agents on isolated branches, plus a few changelog features. Hype title, sponsored segment, and shallow on mechanics.

- Techniques: Background a research or review subagent; Parallel review fan-out; Worktree-per-agent via a custom slash command; Named project agents via --agent flag; Fork a session on resume; Keep background tasks isolated and named
- Tools: Claude Code (background agents, tasks command, --agent flag, resume flag, custom slash commands, instant auto-compact, prompt suggestions), git worktree

## [5 Ways To Build Beautiful Websites Using Claude Code](../videos/VGYsHicpp34.md)
`VGYsHicpp34` · AI LABS · 2026-01-02 · q2 · intro · review · also: vibe-coding-app-building, testing-verification

A design-first workflow for building websites with Claude Code: shadcn presets, Coolers palettes, Google Stitch designs and prototypes, background browser-testing agents, and Drawbridge for visual fixes. Partly a promo for the presenter's agency.

- Techniques: shadcn preset import; Palette before layout; Design in Stitch, then hand off to Claude; Screenshot-driven inspiration; Background browser-test subagent; Drawbridge visual issue reporting
- Tools: shadcn/ui, Coolers, Google Stitch, Gemini 3 Pro, Nano Banana, Google AI Studio, Jules, Claude Code, Claude subagents (background mode), Puppeteer MCP, Drawbridge, Opus 4.5 (named as context)

## [I Gave Claude Code Permanent Memory - The Results Are Shocking](../videos/EsFa7W-FYdM.md)
`EsFa7W-FYdM` · Better Stack · 2026-01-02 · q2 · intro · review · also: context-engineering, mcp-and-tools

Beads gives coding agents a git-synced issue tracker (SQLite locally, JSON Lines in git) so task state survives context resets. A 4-minute overview with claimed context savings and no measured results.

- Techniques: Repo-local issue tracker as agent working memory; Dependency-graph querying instead of loading planning docs; Compaction of closed issues; Spec first, then issues
- Tools: Beads, Beads MCP server, SQLite, JSON Lines, Git, Jira, SpecKit, Kiro, Claude Code, Sourcegraph, AMP

## [Anthropic Just Bought Bun?!?!](../videos/UOpzufhECNg.md)
`UOpzufhECNg` · Better Stack · 2026-01-02 · q2 · intro · news · also: dev-tools

News recap of Anthropic's acquisition of the Bun JavaScript runtime, drawn from the two companies' blog posts; Bun will power Claude Code and the Agent SDK while staying MIT-licensed.
- Tools: Bun, Claude Code, Claude Agent SDK, Node.js, Factory AI, OpenCode

## [GLM 4.7 is INSANE For Software Dev...](../videos/JaLycsbTlHU.md)
`JaLycsbTlHU` · AI LABS · 2026-01-02 · q3 · practitioner · review · also: token-cost-efficiency, models-research

AI LABS tests Z.ai's GLM 4.7 as a Claude Code backend: cheap coding plan, better architecture than 4.6, but slow and not autonomous enough to run unattended.

- Techniques: Config GLM as the Claude Code backend via settings.json; Design-only UI benchmark prompt; Back-end-ready mock data structure; Steer a weak autonomous run
- Tools: GLM 4.7 (Z.ai), GLM coding plan (Z.ai), Claude Code, Claude Sonnet 4.5, Claude Max plan, Next.js, shadcn/ui, Framer Motion, Gemini 3, GPT-5, Humanity's Last Exam (benchmark), SWE-bench (benchmark)

## [Claude Ralph - The Bizarre Anthropic Plugin That Every Developer Is Missing](../videos/ny_BAA3eYaI.md)
`ny_BAA3eYaI` · Better Stack · 2026-01-02 · q3 · intro · review · also: claude-code, agent-architecture, token-cost-efficiency

Walkthrough of the Ralph Wiggum Claude Code plugin, which re-runs the same prompt through a stop hook until a completion promise appears, with a max-iterations cap as a cost guard.

- Techniques: Ralph-style re-prompt loop (manual); Ralph Claude Code plugin with stop hook; Iteration cap as a spend limit; Tests in the prompt file as the completion gate; Decompose before looping
- Tools: Claude Code, Ralph Wiggum plugin (Anthropic Claude Code plugin, /ralph command), Claude Code stop hook, AMP (agent named as a comparison; no details given), bun test (Bun test runner), beads (suggested pairing, not demonstrated), TypeScript, Python

## [AI Coding Finally Fixed, New AI Models, Huge Gemini Deal and More!](../videos/noxDpgSsops.md)
`noxDpgSsops` · AI LABS · 2025-12-02 · q2 · intro · news · also: models-research, pr-code-review

AI LABS' first Context Weekly roundup: GitHub Agent HQ as a multi-agent command center, Cursor 2.0 with its Composer model, and assorted model, product and robotics announcements, mostly relayed from press coverage.

- Techniques: Clarify-then-dispatch planning for multiple agents; Side-by-side model comparison on one prompt; Select-and-ask UI fix loop in a built-in browser; Mid-reasoning context injection
- Tools: GitHub Agent HQ, Cursor 2.0, Composer (Cursor model), Chrome DevTools, Gemini 3 Pro (preview, expected), Nano Banana 2 (image model, expected), GPT-5.1 (rumored), Design Arena, ChatGPT, Claude (financial services features), Excel, 1X NEO

## [I Tried Google’s New AI IDE… Here’s the Truth (Antigravity)](../videos/KLq250wGeEg.md)
`KLq250wGeEg` · Better Stack · 2025-12-02 · q3 · intro · review · also: security-guardrails, testing-verification

Hands-on tour of Google's Antigravity agent IDE: a useful agent manager, plan-review flow and browser self-testing, undercut by quotas, a markdown-image prompt-injection exfiltration issue, and a half-baked preview.

- Techniques: Plan-first review gate for agent work; Browser-subagent UI self-test with visual evidence; Agent-generated visual assets for prototypes; Red-team the agent with a markdown image exfiltration test
- Tools: Google Antigravity, Gemini 3 Pro, Nano Banana Pro (speaker thinks it is used under the hood, unconfirmed), Google Jules (captions say 'Google Jewels'; speaker's comparison only), Cursor, VS Code, Chrome

## [You can literally win 50K... Just By Prompting](../videos/yq3EN46qw_U.md)
`yq3EN46qw_U` · AI LABS · 2025-12-02 · q2 · intro · tutorial · also: mcp-and-tools

Sponsored walkthrough of Apify's $1M actor-building challenge (Nov 2025 to Jan 31 2026), showing how Claude Code plus Apify's agent prompt and CLI can produce a publishable actor quickly.

- Techniques: Template to agent prompt to CLI deploy; Actor publish checklist; Idea sourcing from published wish lists
- Tools: Apify (actor platform, Apify Store, Apify console), Apify CLI, Claude Code, Google Maps (scraper input requires a Google API key), Gemini MCP (actor built by the host), MCP server template (Apify), Discord

## [Gemini Designer is INSANE... Build Beautiful Websites in Minutes](../videos/v9Rd_l6gLjU.md)
`v9Rd_l6gLjU` · AI LABS · 2025-12-02 · q3 · practitioner · tutorial · also: vibe-coding-app-building, product-ux, context-engineering

Walkthrough of Google Stitch, an AI UI designer, plus a six-phase Klein rules-file workflow that turns exported Stitch HTML into a Next.js app and validates it against the designs.

- Techniques: Iterative screen-by-screen prompting in Stitch; Design-system extraction from exported HTML (phase 1); Per-page analysis and component library (phases 2-3); Navigation-flow mapping (phase 4); Blueprint-then-implement (phase 5); Validation checklist and scorecard (phase 6); Build from HTML, not screenshots
- Tools: Google Stitch, Klein (VS Code extension, multi-model, rules file, MCP store), VS Code, Next.js, Figma (via Klein's MCP store), ChatGPT (GPT-5 Temporary), Claude Pro, Material UI, Arc browser (example prompt)

## [Here's What They Didn't Tell You About Gemini 3](../videos/kyflIo3EKLw.md)
`kyflIo3EKLw` · AI LABS · 2025-12-02 · q2 · intro · review · also: models-research, vibe-coding-app-building, context-engineering

Hands-on review of Gemini 3 vs Claude and GPT-5.1 for UI generation and multi-phase coding; the speaker finds Gemini 3 strong at UI design but credits the agent harness, not the model, for most of the difference.

- Techniques: Same-spec head-to-head coding test; Separate model from harness; One-shot UI test with no guidance; Track context-window use per story
- Tools: Gemini 3 Pro, Gemini CLI, Google Antigravity (VS Code fork), Google AI Studio (Code Assistant), Claude 4.5, Claude Code, Claude desktop app, Claude canvas, GPT-5.1, GPT-5, nano banana (image model, named by the speaker)

## [I Tested the 20% Claude VS ChatGPT Plans To Decide Which is Better](../videos/ageSodnKpw0.md)
`ageSodnKpw0` · AI LABS · 2025-12-02 · q2 · intro · review · also: token-cost-efficiency

A consumer comparison of ChatGPT Plus and Claude Pro at $20/month, covering model access, usage windows, context, file and image limits, deep research, connectors, and coding tools. Its verdict is to choose by use case, and it contains a sponsored segment.

- Techniques: Put large reference sets in a Claude project; Run Claude deep research for a cited report
- Tools: ChatGPT Plus, Claude Pro, GPT-5, GPT-4o, o4-mini, Claude Haiku, Claude Opus, Sora, Codex, Claude Code, MCP, GitHub

## [Claude Killer? My Review on Kimi K2 Thinking After Days of Testing](../videos/fjCwC6BYKAE.md)
`fjCwC6BYKAE` · AI LABS · 2025-12-02 · q2 · practitioner · review · also: models-research, token-cost-efficiency

Hands-on review of Moonshot's Kimi K2 Thinking via a coding agent: cheap and context-efficient, but slower and weaker than Claude on UI, game and feature-addition tasks.

- Techniques: Same-prompt A/B against a reference model; Feature addition to an existing codebase; Iterate the prompt on a stuck build
- Tools: Kimi K2 Thinking (Moonshot AI), Claude (Sonnet 4.5 named as the comparison point), GPT-5, Klein (transcribed name, likely the Cline VS Code coding agent; used as the editor agent), Firebase Authentication, Make (sponsor)

## [Here's What They Didn't Tell You About Claude's New Model - Opus 4.5](../videos/IZhGvZ4UlPs.md)
`IZhGvZ4UlPs` · AI LABS · 2025-12-02 · q2 · intro · review · also: models-research, evals

A hands-on review of Claude Opus 4.5 covering the launch benchmarks, system-card safety findings, and side-by-side coding tests against Gemini 3 Pro and Sonnet 4.5.

- Techniques: Epics-and-stories spec before building; Identical-prompt cross-tool comparison; Steerability probe via style cue; Functional check beyond visuals; Human-judgment fallback when automated evals saturate
- Tools: Claude Opus 4.5, Claude Sonnet 4.5, Claude Code, Claude desktop app, Cursor, Gemini 3 Pro, GPT-5.1, SWE-bench, tau-squared-bench (tau2-bench), MonkeyType (test-app target, not a tool used), Swift

## [Gemini 3 is My New Daily Driver (Best Model)](../videos/aLjt3H-hDGs.md)
`aLjt3H-hDGs` · Better Stack · 2025-12-02 · q2 · intro · review · also: models-research, token-cost-efficiency

Better Stack's first-look review of Gemini 3 Pro: strong one-shot 3D and UI demos, benchmark leads and tiered pricing, all based on anecdotal single-prompt tests.

- Techniques: Same-prompt one-shot comparison; Blind pairwise preference voting with ELO; Cross-check launch claims with third-party leaderboards; Account for tiered long-context pricing
- Tools: Gemini 3 Pro (Gemini 3 Pro High in Antigravity), Gemini 2.5 Pro, Gemini 3 Flash (mentioned as upcoming, no evaluation), Antigravity (Google's AI IDE), Three.js (transcribed as '3GS'), Claude Sonnet 4.5, Claude 4.5, GPT-5.1, Grok 4 Fast, Design Arena, Artificial Analysis, ARC-AGI benchmark

## [Claude Might Be Going In A Different Direction + More](../videos/fiHrS04ZUA8.md)
`fiHrS04ZUA8` · AI LABS · 2025-12-02 · q2 · intro · news · also: models-research, security-guardrails

AI LABS weekly roundup (Dec 2025) covering GPT-5.1, Gemini 3 leaks, Google agents, an Anthropic robot-dog experiment, an Anthropic report on a Claude Code-driven espionage campaign, and IBM quantum processors.

- Techniques: Usage-limit fallback to a smaller model; Plan-then-approve for deep research
- Tools: GPT-5.1, GPT-5.1 Instant, GPT-5.1 Thinking, GPT-5.1-Codex, GPT-5 Codex Mini, Codex, ChatGPT, GitHub Copilot, Gemini 3, Nano Banana 2, Google Maps, Google Opal

## [Claude 4 is HERE and is taking on Cursor... (Claude Code)](../videos/-Qdlg-dkrX8.md)
`-Qdlg-dkrX8` · Better Stack · 2025-11-02 · q3 · intro · news · also: claude-code, models-research, mcp-and-tools

Better Stack's launch-day recap of Claude 4 (Sonnet 4, Opus 4) with a short Claude Code VS Code demo. It mostly relays Anthropic's benchmark and behavior claims, with light skepticism.

- Techniques: Claude Code inside VS Code or JetBrains via the CLI; Paste-the-error bug fix; Agent-maintained memory file; Remote MCP servers through the Claude API; One-hour prompt cache TTL; Tagging Claude Code in GitHub PRs
- Tools: Claude Opus 4, Claude Sonnet 4, Claude 3.7 Sonnet, Claude Code, Claude Code SDK, Claude API (remote MCP connector), VS Code, JetBrains IDEs, Next.js, Excalidraw, GitHub Copilot agent, Codex 1

## [I've Found A Better Alternative to Lovable.dev](../videos/05Bg0yI7Ob4.md)
`05Bg0yI7Ob4` · AI LABS · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building

A sponsored walkthrough of Leap, an AI app builder on the Encore backend framework, pitched as a Lovable alternative that scales. It shows building a shop, deploying, and handing the repo to Claude Code.

- Techniques: Step-by-step MVP prompting for a generated app; Reference-image fixes for UI drift; Auth as a detailed prompt; Clone-and-continue handoff to a local coding agent; Give the agent a platform rule file; Scope agent edits tightly
- Tools: Leap, Encore (open-source backend framework; Encore Cloud), Lovable, Claude Code, Cursor, React, shadcn/ui, Unsplash, AWS, Google Cloud Platform

## [GPT-4.1 is GREAT at Coding... (and long context!)](../videos/8cty1srbCv4.md)
`8cty1srbCv4` · Better Stack · 2025-11-02 · q3 · intro · news · also: models-research, token-cost-efficiency

Short overview of OpenAI's GPT-4.1, 4.1 mini and 4.1 nano: a single-prompt Cursor front-end comparison against GPT-4o and Claude 3.7 Sonnet, plus vendor-reported coding, instruction-following, long-context and pricing figures.

- Techniques: Identical-prompt cross-model UI comparison; Contrast and readability check on generated UI; Pair vendor benchmarks with per-model pricing
- Tools: GPT-4.1, GPT-4.1 mini, GPT-4.1 nano, GPT-4.5 (preview, being deprecated in the API), GPT-4o, GPT-4o mini, Claude 3.7 Sonnet, Cursor, Windsurf, Tailwind CSS, shadcn/ui (transcribed as 'Shadzien'), Gemini (mentioned as competitor, not tested)

## [How to 10X Your Claude Code Workflow](../videos/xhrqmAWI_cw.md)
`xhrqmAWI_cw` · AI LABS · 2025-11-02 · q2 · intro · review · also: claude-code, multi-agent, context-engineering

Walkthrough of a compound-engineering Claude Code plugin (plan, work, review, triage, codify, resolve commands) that persists to-dos and runs parallel review agents. Practical, but the 10X title is unmeasured.

- Techniques: Plan, work, review, triage, codify, resolve command loop; Built-in to-do tool as the phase ledger; Pause-per-phase human checkpoint; Context check before each phase; Language- and concern-specific parallel review agents; Dependency-graph parallel resolution of to-dos; Git ingest for Q&A on a repo; Install as a plugin via marketplace
- Tools: Claude Code, compound engineering (Claude Code plugin), Claude Code plugin marketplace, Claude Code built-in to-do tool, GitHub issues, git worktrees, git ingest, BMAD method (compared, not used), Next.js, FastAPI, Python, TypeScript

## [The PERFECT Design Workflow with Claude Code](../videos/9uFVCxfkLCo.md)
`9uFVCxfkLCo` · AI LABS · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building, mcp-and-tools, context-engineering

Walkthrough of capturing a website component with the Web2 MCP Chrome extension, cloning it one-to-one with a Claude Code/Cursor agent using a modified CLAUDE.md, and generating variants with SuperDesign. Mixed results, with a Rocket.new sponsor segment.

- Techniques: Capture an element with Web2 MCP and reference it by ID; Initialize SuperDesign rule files and edit CLAUDE.md for one-to-one cloning; Two-session workflow: clone first, then generate variants; Use SuperDesign's canvas view to inspect how a design was produced
- Tools: Web2 MCP (paid Chrome extension and MCP server; $2.50/month Pro tier as stated), MCP Pointer (open-source alternative, judged weaker), SuperDesign (superdesign.dev; editor extension with rule files for Cursor, Windsurf and CLAUDE.md), Claude Code, Cursor, Windsurf, Stagewise (mentioned as a prior featured tool), Arc browser, shadcn/ui (described as the common component library), Rocket.new (sponsor; no version), Netlify (mentioned in the Rocket.new segment)

## [3 Ways to Clone Any Site Using Cursor AI](../videos/zmP8Pl-MJXw.md)
`zmP8Pl-MJXw` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: vibe-coding-app-building, mcp-and-tools

Three practical ways to clone a website's design into a Next.js or HTML project using Cursor plus Gemini, the Figma MCP, or the Firecrawl MCP, with the presenter noting where each one falls short.

- Techniques: Full-page screenshot capture for layout cloning; Marker-based splitting of generated code into a Next.js app; Figma selection link to Cursor via the Figma MCP; Turning a GitHub repo into indexable docs for Cursor; Scraping a live site with Firecrawl MCP for a structural clone; Build clones in a framework, not plain HTML
- Tools: Cursor, Gemini (canvas feature), Claude artifacts, ChatGPT, Chrome DevTools (command runner, full-size screenshot), React, Next.js, bash (integrate.sh script), Figma MCP, git2doc, Firecrawl MCP (8 tools), Wallhaven (example site)

## [These Factory AI Droids Built My App in 10 Minutes! (Rust + TypeScript!) 👉 Code, Debug & Ship Apps](../videos/4ZYxlTPX-LM.md)
`4ZYxlTPX-LM` · AI LABS · 2025-11-02 · q2 · intro · review · also: software-factory, multi-agent

A hands-on tour of Factory's "droids" (role-specialized coding agents) building a Tauri desktop chat app, covering local bridge setup, command approval, and a model-switch debug. Thin on depth; the title overstates it.

- Techniques: Role-split agent team; Paired local bridge for hosted agents; Pre-approved command checklist with per-command risk prompts; Live file-diff preview during agent edits; Model-swap triage for a model-dependent bug
- Tools: Factory Droids, Factory Bridge (desktop app), Tauri, Rust, TypeScript, OpenAI API, GPT-4, Gemini 2.5 Pro, Notion (integration named), Jira (integration named), Linear (integration named)

## [This $8/hr AI Engineer Could Replace Junior Devs | Devin AI | Agentic Developer.](../videos/rfWx5zB0Cws.md)
`rfWx5zB0Cws` · AI LABS · 2025-11-02 · q2 · intro · review · also: software-factory, security-guardrails

AI LABS walks through Devin's general availability: Slack/GitHub-driven autonomous coding, a self-QA demo, a $500/month plan the narrator converts to about $8/hour, and a live-share security leak. Mostly demo and hype, few hard numbers.

- Techniques: Assign work from Slack, get progress in-thread; Agent-driven E2E QA on every push; Bootstrap an unfamiliar repo by fix-and-run loop; Sign-up sequence to start a Devin account
- Tools: Devin (Cognition), Slack, GitHub, VS Code Live Share, Rust documentation (consulted by the agent), SWE-bench (vendor-reported results), o1-preview (comparison model, named in video), Cursor (mentioned in others' takes)

## [Time to UPGRADE... Agent OS Replaces 95% of AI Coding](../videos/0rK4-8TryBo.md)
`0rK4-8TryBo` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: context-engineering, claude-code

Walkthrough of Agent OS for Claude Code and Cursor: base and tool installs, opinionated standards files, roadmap-driven builds, and spec/resume commands. Mostly one demo run; the 95% claim is unsupported.

- Techniques: Two-stage install; Edit the standards folder before the first plan; Plan-product prompt structure; Roadmap-driven build loop; create-spec for new features; Custom tool-routing rule for a component library; Resume with execute-task; Retrofit with analyze-product; Invoke rules by tool syntax
- Tools: Agent OS (spoken as AgentOS), Claude Code, Cursor, Next.js, pnpm, npm (avoided in demo), ShadCN UI, ShadCN MCP server, TweakCN (spoken as tweak cn)

## [How the 1% ACTUALLY Build Apps with Cursor's Context Engineering](../videos/QgA55EnmUp4.md)
`QgA55EnmUp4` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: context-engineering, vibe-coding-app-building

A hands-on workflow for building a full app with Cursor or Claude Code by splitting context into a PRD-generated docs folder, a short always-on rule, and a staged implementation plan.

- Techniques: Four-file documentation set generated from a PRD; Small always-attached workflow rule that routes to on-demand docs; Staged implementation plan with optional subtask lists; Put the foundations and scope into the generate prompt; Claude Code slash command for the generate step; Parallelize only independent work
- Tools: Cursor, Claude Code, CLAUDE.md, ChatGPT, Next.js, FastAPI

## [Warp Terminal - 6 GAME-CHANGING Features You Need to Know](../videos/HSgHiRxsFzg.md)
`HSgHiRxsFzg` · Better Stack · 2025-11-02 · q2 · intro · review · also: dev-tools

A six-feature walkthrough of the Warp terminal (command blocks, Warp Drive, agent mode, customization), with a Better Stack sponsor segment in the middle. Light on depth, no benchmarks.

- Techniques: Save recurring commands as Warp workflows; Use notebooks as runnable Markdown runbooks; Run long commands as background blocks; Share a block for debugging; Persist a split layout with launch configurations; Keep an existing prompt framework
- Tools: Warp, Warp Drive, Starship, Powerlevel10k, zsh, VS Code, JetBrains, Cursor, Better Stack

## [Cursor AI Just Got a Massive Upgrade Over Claude Code](../videos/WKy71aZHx20.md)
`WKy71aZHx20` · AI LABS · 2025-11-02 · q2 · practitioner · review · also: claude-code, token-cost-efficiency

A solo creator's hands-on comparison of Cursor's new agent features (plan mode, hooks, slash commands, worktrees, browser control) against Claude Code, concluding Cursor wins on usability and that subscribing to both is the best setup.

- Techniques: Share custom commands between Cursor and Claude Code; Plan first, then build; One git worktree per agent; Browser test-and-fix loop; Shareable prompt deep links; Guard auto-run with before/after tool hooks; Split models across two subscriptions
- Tools: Cursor, Cursor Auto mode, Cursor CLI, Claude Code, Claude Code VS Code extension, Claude Sonnet 4.5, Playwright, Playwright MCP, Conductor, Warp Code, Claude Router, Linear

## [I Found the Simplest AI Dev Tool Ever](../videos/cQv3ocbsKHY.md)
`cQv3ocbsKHY` · Better Stack · 2025-11-02 · q3 · intro · review · also: context-engineering, token-cost-efficiency

Walkthrough of OpenSpec, a lightweight spec-driven development tool, building a small Vite/React charting app through a propose, review tasks, apply, archive loop with OpenCode.

- Techniques: Three-step spec loop; Project file bootstrap; Scope a change by editing its tasks; Track progress from the terminal; Apply and archive via slash commands; Parallel changes in separate tabs
- Tools: OpenSpec, OpenCode, Vite, React, Kiro, GitHub SpecKit

## [Does GitHub's New MCP Server KILL Git Commands? (w/ Cursor)](../videos/3ivTdBgzMMI.md)
`3ivTdBgzMMI` · Better Stack · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, dev-tools

Better Stack runs one timed repo-and-PR task through the GitHub MCP server inside Cursor, finds it about twice as slow as Git aliases and the GitHub CLI, and advises against it for simple Git work.

- Techniques: Run the GitHub MCP server in Cursor; Manual Git and PR flow with aliases (baseline); Fall back to direct git when the agent stalls
- Tools: GitHub MCP server (new, Docker-based; the older server ran via npx), Cursor (IDE with MCP settings), Docker, Git, GitHub CLI / Git aliases (baseline), NeoVim, macOS dictation feature, Supabase MCP server, Figma MCP server, Playwright MCP server

## [Goose + Qwen3 Is INSANE — Best AI Tool I’ve Tried So Far](../videos/thCFAzPJBZo.md)
`thCFAzPJBZo` · Better Stack · 2025-11-02 · q3 · intro · review · also: context-engineering, token-cost-efficiency

Better Stack reviews Goose, Block's open-source local coding agent, paired with Qwen3 Coder via OpenRouter; three small web apps built, with a hints file steering stack choices and a few real failure modes.

- Techniques: Point an open agent at a cheap open-weight coder via a routing gateway; Hints file for per-project or global conventions; Override defaults explicitly in the prompt; Iterate by feature request instead of re-specifying
- Tools: Goose (Block; open-source agent, CLI and desktop client; version not stated), Qwen3 Coder (coding model, called Quen 3 Coder in the transcript), OpenRouter (model gateway used as the provider), Ollama (local model runner Goose can use; not used in this video), Anthropic, OpenAI and Gemini (commercial providers Goose can connect to; not used in this video), Goose AI (named as an unrelated project; not reviewed), MediaPipe (hand detection library the agent chose), SQLite, Node.js, Express, VS Code, React

## [How I Build Beautiful Websites With AI](../videos/1cB2iqz_vnM.md)
`1cB2iqz_vnM` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: claude-code, vibe-coding-app-building, context-engineering

Walkthrough of Drawbridge, an open-source Chrome extension that turns clicks on a localhost page into a queued task list for Claude Code or Cursor, with landing-page and client-prototyping use cases. Main takeaway: UI fixes become batched, position-aware agent tasks.

- Techniques: Install Drawbridge as an unpacked Chrome extension; Queue element-level UI changes; Have the agent process the queue; Turn the Cursor workflow rule into a Claude Code slash command; Build a landing page section by section; Keep a design language in files the agent reads
- Tools: Drawbridge (open-source Chrome extension and visual editor for coding agents), Chrome (extensions, load unpacked), Cursor, Claude Code, shadcn/ui, TweakCN (shadcn theme site), Lumi (sponsored AI website builder), Git (used to revert the demo project)

## [Gemini CLI: The FUTURE of Coding is Here (But There's a Catch)](../videos/OkCHqqX_8fg.md)
`OkCHqqX_8fg` · Better Stack · 2025-11-02 · q2 · intro · review · also: token-cost-efficiency

Head-to-head test of Gemini CLI and Claude Code building the same MP3-to-Whisper transcriber app from one prompt file. Claude Code ran with fewer approval interruptions and tokens; Gemini CLI eventually worked but looped on fixes.

- Techniques: Identical-spec head-to-head test; Auto-accept edits mode in Claude Code; Yolo mode and 'always allow' in Gemini CLI; Paste-error repair loop
- Tools: Gemini CLI, Claude Code, OpenAI Whisper, OpenAI SDK, Bun, React, Vite, OpenAI Codex, MCP

## [TikTok built an IDE to rival Cursor - Trae AI](../videos/OKmwTv0BHwE.md)
`OKmwTv0BHwE` · Better Stack · 2025-11-02 · q2 · intro · review · also: dev-tools

Hands-on first look at Trae, ByteDance's free VS Code-based AI IDE with an agent "builder" mode, inline edit and tab completion; the host finds it not yet compelling enough to replace Cursor.

- Techniques: Scaffold a project from a builder-mode prompt; Attach context to builder mode; Screenshot-to-UI with split inputs; Inline edit for scoped changes
- Tools: Trae (ByteDance AI IDE), VS Code, Cursor, Windsurf, Claude 3.5 Sonnet, GPT-4o, Next.js, Tailwind CSS, create-next-app, JetBrains Fleet, DeepSeek

## [The $3 A Month AI Model That Outperforms Claude Sonnet 4](../videos/ZS03emHhKFg.md)
`ZS03emHhKFg` · Better Stack · 2025-11-02 · q3 · intro · review · also: token-cost-efficiency, models-research

Better Stack runs three one-shot coding tasks (portfolio site, HN clone upgrade, three.js voxel game) through OpenCode on Z.ai's GLM 4.5 and Claude Sonnet 4; Claude wins two of three and GLM is pitched as close enough at $3/month.

- Techniques: Same-prompt head-to-head in one harness; Paste the runtime error back into the agent; Ask for clarifying questions before the build; Put the spec in a prompt .md file; Targeted follow-up prompts for specific bugs, and restart when the bug is vague
- Tools: GLM 4.5 (Z.ai), GLM 4.5 Air, GLM 4.5 Flash, GLM 4.5 355B, GLM 4.5V, Z.ai GLM coding plan, Claude Sonnet 4, Claude Pro, Claude Code, OpenCode, React, Vite

## [Zapier MCP: The Only MCP Server That Cursor Needs](../videos/tFFsX97HzEk.md)
`tFFsX97HzEk` · AI LABS · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, security-guardrails

Zapier's hosted MCP server replaces a pile of local MCP servers with one endpoint, per-action tool selection and fixed-argument control. Useful setup detail, but a vendor walkthrough with a hype title.

- Techniques: Consolidate local MCP servers into one hosted endpoint; Add only the specific tool actions an agent needs; Fix routing fields, leave content fields to the model; Override model-sent arguments on the server side; Connect a Postgres database for read and write actions
- Tools: Zapier MCP server, WebParse by Zapier, Cursor, mcp.json, Postgres, Official Postgres MCP server (read-only, per presenter), Supabase MCP server (noted as missing from Zapier), Composio (compared; manual auth grants), Slack, Jira, GitHub, GitLab

## [Replit Has Become Essential to My Vibe Coding Workflow.](../videos/YtgqzCEeHVw.md)
`YtgqzCEeHVw` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building, context-engineering

Walkthrough of a vibe-coding workflow: Claude brainstorms and writes a no-code front-end prompt, Replit generates a shadcn-based responsive UI with exposed APIs, and Windsurf builds the FastAPI backend from the exported API docs.

- Techniques: Planning prompt with pages and modals; Front end first, API docs as the contract; Dependency and run step for a generated front end; Send browser context to the agent; In-memory storage first, database later
- Tools: Claude (Anthropic), Replit, shadcn/ui, Windsurf, Cascade, Cursor, v0, FastAPI, npm, SuperWhisper, macOS voice dictation, Supabase

## [The $10B System Prompts Behind Cursor AI and Others Just Leaked…](../videos/A5r2tfifYfY.md)
`A5r2tfifYfY` · AI LABS · 2025-11-02 · q2 · intro · review · also: context-engineering, agent-architecture, sandboxing-execution

Walkthrough of leaked system prompts from Cursor, Windsurf, Replit, Manus and others, with the host's takeaways on tool design, background execution, memory, sandboxing and a repo-to-text trick. Useful as prompt-design evidence, but the verdicts are overreaching.

- Techniques: Repo subfolder to LLM-readable text; Post-edit verification loop; Background command execution with process status checks; Persistent memory with semantic auto-retrieval; Ask-for-secrets and stuck-fallback behavior; Sandbox-scoped guardrails in the system prompt
- Tools: Cursor, Windsurf (Cascade), Replit, Manus, Lovable, Devin, Bolt, Roo Code (transcript: 'Rucode'), Netlify, Next.js, shadcn/ui (transcript: 'Shad CNUI'), PostgreSQL

## [Time to SWITCH...Claude Code vs Cursor debate just ended](../videos/tCy5cJRErTg.md)
`tCy5cJRErTg` · AI LABS · 2025-11-02 · q2 · intro · review · also: claude-code, dev-tools, mcp-and-tools

Walkthrough of Claudia, a build-from-source desktop GUI over Claude Code with custom agents, per-prompt checkpoints, a preview pane and GUI MCP setup, pitched as a reason to leave Cursor. Hype title; single-tool demo.

- Techniques: Read-only research subagent; Checkpoint before a risky AI change; Visual bug loop with a preview pane; Add MCP servers through a form; Build Claudia from source
- Tools: Claudia, Claude Code, Cursor, Rust, Bun, git, Next.js, shadcn/ui, Claude Pro plan ($20), MCP (stdio and SSE servers), CLAUDE.md, HTML

## [The #1 Open Source AI Agent to Stop Overloading Cursor AI (Cursor MCP + ACI.dev Unified Server)](../videos/eWvaItBefYw.md)
`eWvaItBefYw` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: mcp-and-tools

Setup walkthrough for ACI.dev's unified MCP server, which exposes search and execute meta-tools so Cursor or Windsurf can reach many MCP apps without loading each one; the speaker's performance and context claims are anecdotal.

- Techniques: Unified MCP server with search and execute meta-tools; Pasting the ACI usage prompt as a Cursor project rule; Recovering from 'user isn't authenticated' errors; Smoke-testing the connection
- Tools: ACI.dev unified MCP server, ACI App Store / agent playground, Cursor, Windsurf, Claude Desktop, Brave Search API, Archive (research papers app), Google Calendar integration, Figma MCP, GitHub MCP, Firecrawl MCP

## [Warp + Neovim + Superfile: This Terminal Setup CHANGED How I Code](../videos/IGnbTs5HWvY.md)
`IGnbTs5HWvY` · Better Stack · 2025-11-02 · q2 · intro · review · also: dev-tools

A Better Stack presenter walks through a terminal-only workflow: Vim motions learned over about a month, NeoVim on top of LazyVim/NVChad, Warp as the terminal with its Agent used to maintain the NeoVim config, plus superfile, lazygit and fish. Mostly personal anecdote with a few transferable tips.

- Techniques: Vim motions bootstrap via VS Code Vim extension; Migrate from the VS Code/Cursor Vim plugin to NeoVim; Agent-maintained editor config; Terminal styling that matches the editor; Inline image previews in the terminal; Split AI roles inside the editor
- Tools: Warp (terminal, with Warp Agent), Neovim, LazyVim, NVChad, nvim-tree, mason, lualine, noice, supermaven, avante, OpenCode, VS Code Vim extension

## [GPT-5 Just Killed Claude – Smarter & Cheaper](../videos/pNi9RIOPs0Q.md)
`pNi9RIOPs0Q` · Better Stack · 2025-11-02 · q2 · intro · review · also: models-research, token-cost-efficiency

Hands-on first look at OpenAI's GPT-5 launch (Nov 2025): a few informal coding tests against Claude Opus, plus the pricing and benchmark claims relayed from OpenAI's livestream.

- Techniques: Same prompt across models, judged by running the output; Compare models inside the agent harness, not in chat; Tier models by task definition; Check the backend, not just the UI
- Tools: GPT-5, GPT-5 Pro, GPT-5 Mini, GPT-5 Nano, GPT-5 Chat, Codex, Claude Opus 4.1, Claude Opus, OpenAI O3, Cursor, Windsurf, GitHub Copilot

## [Deploy Project to Netlify Instantly.](../videos/ruRxIGmsCgs.md)
`ruRxIGmsCgs` · AI LABS · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building

Windsurf Wave 6 adds "deploys": Cascade publishes a static site to Netlify under a windsurf.build subdomain, which must be claimed in your own Netlify account within 24 hours.

- Techniques: Agent-driven static deploy; Claim within 24 hours; Deploy-log feedback loop; Plan pages and modals first; Specify constraints in the build prompt
- Tools: Windsurf (Wave 6, Cascade agent), Netlify, GitHub, Cursor, netlify.toml

## [DeepClaude: The Combined Power of Deepseek R1 & Claude 3.5 Sonnet!](../videos/ymunCZzgzeg.md)
`ymunCZzgzeg` · AI LABS · 2025-11-02 · q2 · intro · review · also: models-research

A short walkthrough of DeepClaude, an open-source chat UI that calls DeepSeek R1 and Claude 3.5 Sonnet through their APIs; the presenter installs it, runs one React prompt, and finds it weak as a standalone chat app.

- Techniques: Dual-provider chat setup; Single-prompt comparison test; Per-chat model switching
- Tools: DeepClaude, DeepSeek R1, Claude 3.5 Sonnet, Rust 1.75, npm, React, Aider Polyglot benchmark

## [How to Use Cursor in the Smartest Way Possible](../videos/LXk8nWwOPuY.md)
`LXk8nWwOPuY` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: pr-code-review, context-engineering

A tutorial on pairing Cursor's agent with the CodeRabbit extension: commit each implementation chunk, run a review, feed suggestions back, and drive a phased implementation plan.

- Techniques: Commit-gated review loop; Branch-visibility workaround for missing reviews; One-comment-per-paste fix loop; Phase-by-phase plan with a structure file
- Tools: Cursor, CodeRabbit (VS Code / Cursor / Windsurf extension), Windsurf, Git, GitHub (CodeRabbit sign-in), Gemini 2.5 Pro, Next.js, FastAPI, shadcn/ui (spoken as 'shad cn')

## [Cursor AI Had a BIG PROBLEM — I Just Found the FIX](../videos/UngBxJ9uy70.md)
`UngBxJ9uy70` · AI LABS · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, context-engineering, multi-agent

AI LABS walkthrough of GitMCP, which turns any GitHub repo into a hosted MCP docs server, shown as an alternative to Context7 for keeping Cursor grounded in current docs, with a three-agent A2A demo.

- Techniques: Per-repo hosted MCP docs via URL swap; Scope docs to one repo instead of a broad doc index; Use the hosted repo chat as a post-build spec check; Router agent plus domain specialist agents over A2A; Routing check by server log
- Tools: Cursor, Gemini 2.5, GitMCP (gitmcp.io), Context7 MCP, MCP (Model Context Protocol), A2A (Google Agent-to-Agent protocol), Claude Desktop, Windsurf, VS Code, Claude, LangGraph (docs example), Three.js (demo project)

## [Build Apps Using ONLY your Voice (WARP 2.0 is Insane)](../videos/4n7z4eb_aKU.md)
`4n7z4eb_aKU` · Better Stack · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building, dev-tools

Better Stack demos Warp 2.0's Code and Agents features by building several small web apps mostly from voice prompts, then deploys one. Mostly a demo with a few practical notes, and the title oversells it.

- Techniques: Refine-with-docs correction; Reference image plus voice prompt for UI; Auto-approve for unattended agent runs; Parallel agent panels by concern; Deploy by asking for a host, then letting the agent run it
- Tools: Warp 2.0 (Warp Code, Warp Agents, Warp Drive), Tailwind CSS (Vite plugin), Vue.js, React (mentioned only), Vanilla JavaScript, HTML5 canvas, Framer (used for the reference design), GitHub Pages, Vercel CLI (mentioned), npm, Cursor (comparison), Claude Code (comparison)

## [OpenAI FINALLY Goes Open... 2 NEW models (they're good?)](../videos/hIgQ_0VMj_4.md)
`hIgQ_0VMj_4` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: models-research, local-ai

Hands-on test of OpenAI's open-weight gpt-oss-120b and gpt-oss-20b: the 20B runs locally on a MacBook, the 120B runs via OpenRouter, and coding results are mixed against OpenAI's self-reported benchmarks.

- Techniques: Run gpt-oss-20b locally for offline use; Route the 120B model through OpenRouter inside OpenCode; Scope the prompt to what the model can finish; Use a fixed single-file stress prompt for quick model comparisons
- Tools: gpt-oss-120b, gpt-oss-20b, Ollama (auto-caption 'Alarma'), OpenRouter, OpenCode, Next.js, tRPC, Tailwind CSS, Claude Code, Claude Sonnet 4 (auto-caption 'Claude Sonic 4'), o3, o3-mini

## [Qwen3 Coder vs Kimi K2 vs Claude Sonnet 4](../videos/nzAT09XolYw.md)
`nzAT09XolYw` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: evals, token-cost-efficiency

Better Stack runs one Next.js blog-generator spec through Qwen3 Coder, Kimi K2 and Claude Sonnet 4 in OpenCode. Qwen was fastest and cheapest, Sonnet built fastest, yet all three hit a YouTube-transcript failure.

- Techniques: Same-repo, same-prompt head-to-head; Spec in a prompt file, not in the chat; Stop-loss on the debug loop; Style-from-samples analysis step; Tiered model assignment by cost
- Tools: OpenCode, Qwen3 Coder, Kimi K2, Claude Sonnet 4, Next.js, bun, OpenRouter, Moonshot console, Gemini CLI (fork basis for Qwen CLI, not used in the test), GPT-4 (named as the extraction model in the Claude build's prompts), YouTube transcript API/library (unnamed), Markdown

## [Automate Your Browser with AI Using StageHand AI Agent](../videos/PPutzww1RaM.md)
`PPutzww1RaM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: voice-multimodal

Short quickstart for Stagehand, a Playwright-based browser agent with plain-language act, goto and extract APIs, scaffolded with a create-app command and driven from Cursor.

- Techniques: Scaffold a Stagehand project; Plain-language page actions and extraction; Generate Stagehand code in Cursor
- Tools: Stagehand, Playwright, Browserbase, Cursor, Zod, Chromium, GPT-4 (via OpenAI API), Node.js / npm / npx

## [Vercel made a Model (v0 in Cursor)](../videos/jZB1sXDaOj8.md)
`jZB1sXDaOj8` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: vibe-coding-app-building, models-research

Better Stack tries Vercel's new v0-1.0-md model through its API, routes Cursor's OpenAI model slot to it via a base-URL override, and builds a shadcn to-do app from one prompt.

- Techniques: Get a v0 API key for model access; Route Cursor to the v0 model via base-URL override; Single-prompt full-app generation in agent mode; Compare the same prompt across two surfaces
- Tools: v0 (v0.dev), v0-1.0-md, Cursor, Next.js, shadcn/ui (spoken as 'ShadCN'), Vercel AI SDK, Vercel AI playground, Three.js (mentioned as a v0 output example), Codex (transcript reads 'codecs'; another coding tool the host names as a target)

## [3 Ways to Make GENUINELY Stunning Websites Using Claude Code](../videos/McJluKfjVGk.md)
`McJluKfjVGk` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: vibe-coding-app-building, claude-code, mcp-and-tools

A walkthrough of three Claude Code workflows for building polished UIs: SuperDesign for iterative design canvases, ShadCN MCP for component-library builds, and Firecrawl or Figma MCPs for cloning existing designs.

- Techniques: SuperDesign canvas setup; Layout-then-theme-then-polish staging; Targeted correction round; ShadCN MCP plus a saved usage-rule slash command; Theme import from tweakcn; Site cloning with Firecrawl MCP; Figma MCP selection import; Animation snippet import from Animatopy
- Tools: Claude Code, SuperDesign (superdesign.dev, VS Code / Cursor extension), Cursor, VS Code, ShadCN UI, ShadCN MCP server, Firecrawl MCP, Figma MCP server, tweakcn, Animatopy, Colors (palette generator website), Next.js

## [What Cursor Doesn't Have: Claude Code Subagents](../videos/Ppu6pJ5yyD4.md)
`Ppu6pJ5yyD4` · AI LABS · 2025-11-02 · q2 · practitioner · review · also: claude-code, multi-agent, context-engineering

Walkthrough of Claude Code's native subagents: creating project agents with /agents, why isolated context windows help, and how auto-delegation and chaining work. Practical but thin, with a sponsor segment.

- Techniques: Create a project-scoped subagent with /agents; Write a specific description and scope tools tightly; Spec file plus rules file handed to a builder subagent; Theme swap through a subagent; Chain subagents in a custom slash command; Invoke a subagent explicitly
- Tools: Claude Code, Claude Code subagents (/agents), Cursor, ShadCN UI, ShadCN UI MCP server, Next.js, Tailwind CSS v3, TweakCN, TestSprite MCP server, BMAD workflow, SuperClaude workflow, GitHub subagents collection (unnamed)

## [Is Stealth Grok 4 Code Model (Sonic) Actually Good?](../videos/CNIo3NPwWhM.md)
`CNIo3NPwWhM` · Better Stack · 2025-11-02 · q2 · practitioner · review · also: models-research

Hands-on test of the stealth coding model Sonic in OpenCode: strong one-shot code and server-side API key handling, weaker UI design, judged not better than Sonnet after a few hours.

- Techniques: Interrupt and redirect a scaffold choice; API key placement probe; Clarifying-questions prompt; Prompt file as the project spec; Paste-the-error repair loop; Mid-session model switch for comparison; Reviewing agent code by eye
- Tools: OpenCode (version 5.8 as stated in the video), Sonic (stealth model, name as spoken), Grok 4 (speculated link, unconfirmed), Claude Sonnet 4, GPT-5, Three.js, React Three Fiber, React, Create React App, Vite, Bun, Tailwind CSS

## [Figma MCP Tutorial: The Best Way to Clone a Front-End](../videos/FJBLhd23f80.md)
`FJBLhd23f80` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: mcp-and-tools, vibe-coding-app-building

A 5-minute tutorial on connecting an open-source Figma MCP server to Cursor, then having the agent generate HTML/CSS from a Figma page link instead of a screenshot.

- Techniques: Run a Figma MCP server over SSE and attach it to Cursor; Copy a link to a Figma selection and hand it to the agent; Force the agent to the node tool when it picks the wrong one; Combine the Figma link with a screenshot for corrections
- Tools: Figma MCP server (glips, open source, run via npx and pnpm), Figma API / personal access tokens, Cursor (MCP client), pnpm, npx, git, HTML/CSS (generation target)

## [Poml: Microsoft's Secret Tool for PERFECT AI Prompts](../videos/tfOwh6YCY8M.md)
`tfOwh6YCY8M` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: context-engineering, data-engineering

Walkthrough of POML, Microsoft's open-source markup language for prompts, showing components, data embedding, templating, and a script that generates an AGENTS.md file.

- Techniques: Compile a POML file to an API-ready message list; Embed a spreadsheet as a prompt data component; Parameterize a prompt with templating and Python context; Generate an AGENTS.md from style documents with a cheap model; Run a compiled prompt through a non-interactive coding agent
- Tools: POML (Microsoft open-source prompt markup language), POML Python SDK, POML TypeScript SDK (said to be unstable at the time), POML VS Code extension, OpenAI Python SDK, GPT-5 mini, GPT-5 nano, Codex CLI (non-interactive), Claude Code, OpenCode, Gemini CLI, LangChain

## [Why Crush Is the Best‑Looking AI Coding CLI (RIP Claude Code?)](../videos/kCcCxzCSf_w.md)
`kCcCxzCSf_w` · Better Stack · 2025-11-02 · q2 · intro · review · also: claude-code, dev-tools

A short hands-on look at Charm's Crush, a terminal AI coding CLI, compared against Claude Code and OpenCode on one React app prompt. It looks polished, but it trails on features and only supports API keys.

- Techniques: Same-prompt cross-CLI comparison; Permission modal: allow for session; Init a project memory file; Keyboard navigation in Crush; Configure LSPs and MCP servers in crush.json; Check where generated apps put API keys
- Tools: Crush (Charm terminal coding agent), OpenCode (original project, later renamed to Crush), OpenCode (SST, TypeScript version), Claude Code, Claude Sonnet 4, OpenAI Whisper API, Vite, React, LSP servers, MCP servers, crush.json, CRUSH.md

## [The BEST Way To Use Claude Code Anywhere (Thanks To Levelsio)](../videos/N434yhINnHo.md)
`N434yhINnHo` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: claude-code, dev-tools

Better Stack walkthrough for running Claude Code on a cheap always-on Hetzner server and driving it from a phone via SSH or Mosh in Terminus or Termux.

- Techniques: Always-on remote Claude Code host; Terminus SSH host setup (iOS/Android); Termux setup (Android); Mosh for roaming and reconnects; Docker isolation for the agent
- Tools: Claude Code, Hetzner, Node.js, NVM, Terminus, Termux, Termux Style, OpenSSH, fish shell, Mosh, Docker, GitHub

## [GitHub Spark Is INSANE – A Full App in Just 20 Minutes!](../videos/Lwi6VKBl7EU.md)
`Lwi6VKBl7EU` · Better Stack · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building, product-ux

A Better Stack walkthrough of GitHub Spark, a browser-based vibe-coding platform, building a movie-rating app from one prompt in about 4 minutes, with the caveats that it is React/TypeScript-only, needed a manual API key, and was not responsive.

- Techniques: Front-load the full feature list in one prompt; Supply the missing credential the builder asks for, and verify it; Iterate through the suggestion panel while using the app; Tune the in-app LLM through the prompts tab; Check responsiveness explicitly
- Tools: GitHub Spark, Claude Sonnet 4, Kiro (Amazon IDE, mentioned only), React, TypeScript, Tailwind CSS, TMDB movie API, Unsplash, GitHub Copilot Pro Plus

## [The Cursor CLI is Actually Good!?](../videos/onaIazLEVi8.md)
`onaIazLEVi8` · Better Stack · 2025-11-02 · q3 · intro · review · also: claude-code

Better Stack's hands-on head-to-head of the Cursor CLI beta against Claude Code on the same Sonnet 4 model: Cursor planned and implemented better, and the host recommends it for language coverage, IDE consistency and single-subscription setups.

- Techniques: Plan-only prompt before implementation; Shell command from inside the agent chat; Headless Cursor agent in CI; Review mode with file-scoped follow-ups; Rules file to prevent inline React components
- Tools: Cursor CLI (beta), Cursor Agent, Cursor IDE, Claude Code, Claude Sonnet 4, Next.js, Better T-Stack, GitHub Actions, OpenCode (mentioned for UI comparison), Vim, npm

## [Sonnet 4.5 Just Unlocked a New Breed of Agents](../videos/t7VuWwukO3I.md)
`t7VuWwukO3I` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: claude-code, mcp-and-tools, agent-architecture

AI LABS walkthrough of running Claude Code as a scheduled GitHub Actions agent (model-news monitor to Slack) and as an issue-triggered background coder, with two rules learned from failed runs: auto-approve tools and test MCP servers first.

- Techniques: Install the Claude Code GitHub app into a repo; Scheduled news monitor on GitHub Actions; Whitelist all tools for headless runs (Rule 1); Verify MCP servers before automation (Rule 2); Post to Slack via incoming webhook with curl; Hand off a background coding task via a GitHub issue; Paste SDK documentation into the task; Verify auth end to end on a branch
- Tools: Claude Code (version 2 announced with Sonnet 4.5), Claude Sonnet 4.5, Claude Code GitHub app, GitHub Actions, GitHub, Slack (incoming webhook via curl), Supabase (auth), Supabase MCP server, Claude Agent SDK (TypeScript and Python docs), BMAD method (referenced), OpenAI Codex (referenced as inspiration for cloud agents), Cursor (referenced for code rewind), GPT-5 (mentioned in the opening)

## [Claude 3.7 Sonnet is INSANE + Claude Code? (Best Coding Model)](../videos/6KGH47rdeBs.md)
`6KGH47rdeBs` · Better Stack · 2025-11-02 · q2 · intro · review · also: claude-code, models-research

Walkthrough of Claude 3.7 Sonnet's hybrid extended-thinking mode, its published benchmarks, and the Claude Code research preview, shown on a single demo project.

- Techniques: Toggle extended thinking in the chat UI; Set a thinking budget on API calls; Quick-start Claude Code on an existing project; Approve Claude Code actions with scoped trust; Have Claude Code create the commit; Custom scaffolding for SWE-bench-style agents
- Tools: Claude 3.7 Sonnet, Claude Code, Cursor, Gemini, DeepSeek, Next.js, TypeScript, Tailwind CSS, npm, git, SWE-bench, TAU-bench

## [The EASIEST Way To Switch From ESLint & Prettier to Biome — Ultracite](../videos/lEkXbneUnWg.md)
`lEkXbneUnWg` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: dev-tools, context-engineering

Better Stack walks through Ultracite, a zero-config preset that sets up Biome (a Rust linter and formatter) with AI rule files, editor settings and pre-commit hooks in one init command.

- Techniques: Zero-config Biome bootstrap; Biome config that only extends the preset; Thin CLI wrappers for lint and format; Pre-commit format gate via Husky; Shift lint rules left into the agent's context; Expose rules through an MCP server
- Tools: Ultracite (npx ultracite init, lint, format), Biome (biome check, biome check --write), ESLint, Prettier, Husky, lint-staged, lefthook, Bun, shadcn/ui, VS Code, Cursor, Zed

## [How I ACTUALLY Use Claude Code... My Complete Workflow](../videos/7Sx0o-41r2k.md)
`7Sx0o-41r2k` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: claude-code, multi-agent, context-engineering

A host walks through a multi-agent Claude Code workflow for building an app: specialized sub-agents run in sequence, each writing its output to docs, with checkpoints for rollback and a generated agent-workflow setup.

- Techniques: Phased sub-agent chain driven by one prompt; Parallel sub-agent fan-out; Docs-first planning with scoped agents; Two-stage requirements before agent planning; Rewind with double-Escape checkpoints; Generate an agent workflow from a repo; Verbose view of sub-agent activity
- Tools: Claude Code, Claude Code sub-agents, Claude Desktop, Claude Opus, Cursor (checkpointing, as cited by the host), BMAD method, SuperClaude, gitingest.com, Next.js, UX researcher agent, sprint prioritizer agent, UI designer agent

## [Wait... Cursor AI Just Launched a New Agent?](../videos/QOJdhje6Vnc.md)
`QOJdhje6Vnc` · AI LABS · 2025-11-02 · q2 · intro · review · also: claude-code, models-research

Hands-on first look at Cursor's new terminal agent CLI (beta) using GPT-5: install, slash commands, a Kanban app test, and why the host would not switch from Claude Code yet.

- Techniques: First-run setup for Cursor agent CLI; Switch models with /model inside the agent; Retry a stalled agent run with the same prompt; Fixed-prompt smoke test for a coding agent; Give visual feedback when the CLI cannot take images
- Tools: Cursor agent CLI (`cursor agent`), Cursor IDE, GPT-5 (OpenAI), Claude Code, Claude Code Router

## [How to Use Cursor AI with Its Own Cursor Memory Bank](../videos/azXNHRtzd5s.md)
`azXNHRtzd5s` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: memory, context-engineering

A short walkthrough of Cline's "Memory Bank" pattern: a set of structured markdown files that keep a coding agent's project context across sessions, set up in Cursor via pasted global rules. Practical but thin, with an admitted rules bug.

- Techniques: Paste a memory-bank rules file into Cursor User Rules; Initialize the memory bank with a single agent-mode prompt; Force plan-then-act with edit blocking; Keep the bank current in act mode
- Tools: Cline (Memory Bank, named 'Klein' in the transcript), Cursor (agent mode, User Rules, Cursor 2), Windsurf, Next.js, React Router, Unsplash API, Mermaid

## [3 Things Before You FINALLY Switch to Codex CLI](../videos/gRXrOuFn9dE.md)
`gRXrOuFn9dE` · AI LABS · 2025-11-02 · q2 · intro · review · also: context-engineering, multi-agent

Hands-on comparison of Codex CLI against Claude Code: a single-prompt game test, the GUI options for each, an MCP workaround for missing sub-agents, and the BMAD planning method for multi-step builds. Sponsored intro; thin evidence.

- Techniques: Sub-agent delegation through an MCP server; Fork and patch an unmaintained community tool; BMAD-style plan-then-build workflow; Manual agent wiring for Codex; Edit MCP config from inside the Codex IDE extension
- Tools: Codex CLI (OpenAI), Codex IDE extension, GPT-5 Codex High (model used in the test), Claude Code, Phaser 3 (game engine), Kenney assets (spoken as Kenny), Three.js (spoken as 3.js), React, Next.js, shadcn/ui, Opcode (formerly Claudia), Conductor

## [GLM 4.6 Review: Better Than Claude for Coding? (Real Project Tests)](../videos/wEHWvzWOjt0.md)
`wEHWvzWOjt0` · AI LABS · 2025-11-02 · q2 · practitioner · review · also: token-cost-efficiency, models-research, context-engineering

Hands-on test of GLM 4.6 against Claude Sonnet 4.5 on a UI-design prompt and a multi-epic Svelte 5 build; GLM is far cheaper per message but needed Sonnet to finish integration.

- Techniques: Same-prompt model bake-off for UI work; BMAD epic-to-story decomposition for agent builds; Provision the backend through the database MCP; Commit per fix to attribute regressions to a model; Cheap model for most of the build, strong model for integration; Use a stack with thin training data as a stress test
- Tools: GLM 4.6, GLM 4.5, GLM coding plan (GLM Lite and Max tiers), Claude Sonnet 4.5, Claude Max plan, Claude Code, BMAD method, Svelte 5, Supabase, Supabase MCP, shadcn-svelte, CodeRabbit CLI (sponsor)

## [Roo Code is AMAZING - AI VSCode Extension (better than Cursor?)](../videos/r5T3h0BOiWw.md)
`r5T3h0BOiWw` · Better Stack · 2025-11-02 · q3 · intro · review · also: token-cost-efficiency, testing-verification

Walkthrough of Roo Code, an open-source VS Code agent extension: built-in modes, auto-approve, browser self-testing, per-mode model choice and custom modes, with a Claude Sonnet vs Gemini Flash cost comparison.

- Techniques: Architect-then-code split; Enhance Prompt before sending; Category-scoped auto-approve; Browser self-check loop for UI work; Per-mode model assignment; Custom mode via prompt, then scope with file regex; Edit support prompts and attach diagnostics
- Tools: Roo Code, VS Code, OpenRouter, Claude Sonnet, Gemini 2 Flash 001, DeepSeek, Next.js, create-next-app, npm, Tailwind CSS, Cursor (comparison only), MCP (Model Context Protocol) servers

## [How to Make Cursor CODE What You ACTUALLY Want.....](../videos/Dv_tSxAA0HE.md)
`Dv_tSxAA0HE` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: context-engineering

A short Cursor feature tour: scoped project rules that replace the deprecated .cursorrules file, plus reusable prompts in Notepads, @web search, and custom doc indexing.

- Techniques: Global user rules for all projects; Scoped project rules with description and globs; Reuse community rule files; Reusable prompts in Notepads; Web search and custom docs in chat
- Tools: Cursor, Cursor Composer, cursor.directory, Supabase (examples/prompts repo), Next.js, TypeScript, Python, Tailwind, n8n, MCP (Model Context Protocol)

## [The Only Guide You Need to Build MCP Server.](../videos/kfTDFkhNDFU.md)
`kfTDFkhNDFU` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools, context-engineering

Walkthrough of building a minimal Python MCP server with the official SDK, wiring it into Cursor, and using docs and AI generation to wrap a web crawler and a Figma API.

- Techniques: Minimal Python MCP server; Register a local MCP server in Cursor; Feed SDK docs to the coding agent; gitingest to turn a repo into LLM context; Wrap an existing script as an MCP tool; API-to-tool generation from endpoint docs
- Tools: MCP Python SDK (mcp, installed with pip; no version stated), Cursor (agent, Composer, docs feature, MCP settings), Crawl4AI (open-source web crawler and data extractor), Figma REST API (get file endpoint), gitingest (gitingest.com, GitHub URL swap), GitHub (SDK repo, README)

## [Time to SWITCH… 20X your Claude Code Workflow](../videos/PRqHKpTHQVE.md)
`PRqHKpTHQVE` · AI LABS · 2025-11-02 · q2 · intro · review · also: models-research, claude-code

AI LABS compares Claude Opus 4.1 with Opus 4 inside Claude Code on two single-run builds (a Pac-Man game and a ShadCN/Framer Motion site); the 4.1 gains look real but the evidence is anecdotal.

- Techniques: Identical-prompt A/B across model versions; Requirement checklist for generated UI; Model upgrade inside Claude Code; API model-name swap
- Tools: Claude Code, Claude Opus 4.1, Claude Opus 4, Claude Sonnet 3.7, Claude Sonnet 4, shadcn/ui, Framer Motion, SWE-bench Verified

## [Spec Kit: Github's NEW tool That FINALLY Fixes AI Coding](../videos/em3vIT9aUsg.md)
`em3vIT9aUsg` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: context-engineering, testing-verification

Walkthrough of GitHub's open-source Spec Kit, a four-phase (specify, plan, tasks, implement) spec-driven workflow for AI coding agents, shown building a small Pokedex app.

- Techniques: Four-phase spec-driven loop; Resolve 'needs clarification' blocks before planning; Put performance guardrails in the plan prompt; Track progress through the tasks file
- Tools: Spec Kit (GitHub open-source spec-driven toolkit with CLI, templates and steering prompts), GitHub Copilot (agent used in the demo), Claude Code (referred to as 'CloudCode' in the auto-captions; listed as a supported agent), Gemini CLI (listed as a supported agent), Amazon Kiro (earlier spec-driven framework, mentioned only), Grok Code Fast 1 (base model for the demo; auto-captions say 'grokcodefast1'), GPT-4.1 (comparison model, one run), Zod (schema library used in the generated data model), shadcn/ui (likely; auto-captions say 'Shotzi' for the UI library)

## [I Made MCP AI Agents That Automate Every App I Build.](../videos/23ykmgvaSmM.md)
`23ykmgvaSmM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools, vibe-coding-app-building

Tutorial on wrapping an existing FastAPI to-do app with the FastAPI MCP server so Cursor, Windsurf, Claude Desktop, or a Python MCP-client agent can call its endpoints as tools. Covers setup, tool naming, and a registration gotcha.

- Techniques: Expose a FastAPI app as MCP tools; Name MCP tools with operation IDs; Register MCP after all endpoints are declared; Add the MCP server to an IDE client; Drive the MCP server from a custom Python agent
- Tools: FastAPI, fastapi-mcp (FastAPI MCP package), Next.js, Cursor, Windsurf, Claude Desktop, pip, uv, MCP use framework (Python MCP client library, name as spoken), mcp.json, config.json

## [Firecrawl MCP = Effortless Web Scraping](../videos/2GHRDoFquOo.md)
`2GHRDoFquOo` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools, vibe-coding-app-building

Tutorial on wiring the Firecrawl MCP server into Cursor so an agent can scrape a live URL and generate a near-copy of a Notion landing page in Next.js. Shows setup and a single demo run, with the output's flaws called out.

- Techniques: Register Firecrawl MCP in Cursor; Name the MCP tool in the prompt and use agent mode; Scrape, then generate by component; Pick scrape vs extract by goal
- Tools: Firecrawl MCP server (scrape and extract tools, npx command, API key), Cursor (agent mode, MCP settings), Windsurf (same MCP config pattern, mentioned as an alternative), Claude 3.7 Sonnet (model selected in Cursor), Next.js (blank starter app used as the target), Notion landing page (the site being cloned)

## [Turn Cursor AI into the 500$ Devin (Just Paste this...)](../videos/wJk2_Ds-9cM.md)
`wJk2_Ds-9cM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: context-engineering, skills-self-improvement

Walkthrough of a Cursor rules file that adds a lessons log and task scratchpad, used to build a full-stack Trello clone; one anecdotal demo with overstated "Devin" framing.

- Techniques: Per-project .cursor rules file; Lesson log inside the rules file; Scratchpad task plan with checkboxes and a current-focus section; Generate the rules prompt with another model, then run it in the IDE agent
- Tools: Cursor, Cursor Composer, Windsurf, Devin, GPT (used to write the prompt), PostgreSQL, Docker, OpenAI API (gpt-4 model name), Trello (clone target, not a tool used)

## [This Designer is INSANE... The Ultimate UI Setup](../videos/uayt-IVbh8E.md)
`uayt-IVbh8E` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: multi-agent, vibe-coding-app-building, context-engineering

Walkthrough of a Claude Code sub-agent pipeline for UI work: a UX agent drafts layout from requirements, a UI agent applies color variants, and a converter agent ports the HTML to SwiftUI.

- Techniques: Stage-separated UI sub-agent pipeline; Explicit agent count for variants; Split HTML output into HTML, CSS and JS files; Keep emoji placeholders, then fix icons in the target platform; Doc-grounded conversion guide via Context7, then bake into the agent
- Tools: Claude Code (sub-agents defined as markdown files), Cursor (mentioned in the intro as an AI coding tool, not used in the walkthrough), Context7 MCP, SwiftUI, iOS Simulator, HTML / CSS / JavaScript

## [Before You CHOOSE, Watch This Cursor vs Windsurf Face-Off!](../videos/0Ttn6dqnuQk.md)
`0Ttn6dqnuQk` · AI LABS · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building, token-cost-efficiency

A short, single-run head-to-head of Cursor and Windsurf on a CLI task app, a web music player and pricing, with a verdict favoring Windsurf.

- Techniques: Same-prompt bake-off with explicit pass criteria; Scope check with a deliberately simple app; Trial and plan comparison before buying
- Tools: Cursor (Composer, agent panel), Windsurf (Cascade, image upload, explain-and-fix), ElevenLabs (voiceover audio used in the music-player test), tasks.json (file created by the CLI test)

## [3 More Ways To ACTUALLY Build Beautiful Websites with Cursor IDE](../videos/U1_nzjWUpL4.md)
`U1_nzjWUpL4` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: vibe-coding-app-building, mcp-and-tools, context-engineering

Three practical ways to turn website designs into working Next.js UI in Cursor: a structured front-end spec prompt, a design.json built from screenshots, Browser MCP for cloning structure, and stagewise for precise element-level edits.

- Techniques: Structured front-end spec prompt; Screenshot to design.json style profile; Clone a site's structure with Browser MCP; Element-level UI edits with stagewise
- Tools: Cursor, Claude, ChatGPT, Claude Code, Next.js, Tailwind CSS, Browser MCP, stagewise, mcp.json, design.json

## [Build Apps with Cursor Like the 1% Using This NEW Method](../videos/OZaxtm3RyCw.md)
`OZaxtm3RyCw` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: context-engineering, agent-architecture

Walkthrough of building a wallpaper app in Cursor with Taskmaster AI: the PRD becomes a dependency-ordered task list the agent works through one task at a time, so one chat holds the whole build.

- Techniques: Install and initialize Taskmaster globally, then init per project; Configure keys in .env; Brainstorm with a no-edit instruction; Generate the PRD from an example template; Parse the PRD into tasks, then work them sequentially; Handle implementation drift with an explicit change list; Work in the correct subdirectory
- Tools: Cursor, Taskmaster AI, Claude (Anthropic API), Perplexity API, Unsplash API, Next.js

## [Trae AI: The New Cursor AI Alternative](../videos/cdLnorNbewA.md)
`cdLnorNbewA` · AI LABS · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building, testing-verification

Hands-on test of Trae, ByteDance's VS Code-fork IDE with a single-agent workflow and free Claude access; a to-do app and a Spotify screenshot clone show a basic UI with missing-config errors, verdict "hype".

- Techniques: Screenshot-to-app clone prompt; Built-in web view preview; Manual behavioural check of agent output; Config-first debugging for missing styles
- Tools: Trae (ByteDance IDE), Claude 3.5 Sonnet, GPT-4.0 (mentioned as promised, not available), Cursor, Windsurf, VS Code, React, Tailwind CSS, PostCSS

## [Generate Multiple Cursor Rules with ONE CLICK!](../videos/ztT6Bu1MPpY.md)
`ztT6Bu1MPpY` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: context-engineering

Short tutorial on using Cursor Directory's generate-project-rules feature to turn package.json or requirements.txt into Cursor .rules files, with a UI demo and no evaluation of rule quality.

- Techniques: Generate project rules from dependency manifests; Generate rules per manifest in polyglot repos
- Tools: Cursor, Cursor Directory, Grok (named by the speaker as the generation model), Next.js, React, TypeScript, Tailwind CSS, FastAPI, SQLAlchemy, Obsidian (markdown MCP server example), MCP servers

## [Claude Code Tutorial: Full Setup, MCP, and Cursor AI Integration (Claude Squad Guide)](../videos/u-GGktUnSgg.md)
`u-GGktUnSgg` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: claude-code, multi-agent

Tutorial on running Claude Code inside Cursor and installing Claude Squad to run several Claude Code instances in tmux; the IDE link fails on camera and the MCP in the title is never covered.

- Techniques: Install Claude Code and open it in Cursor; Check the IDE connection from Claude Code; Install Claude Squad; Prepare a repository for Claude Squad; Run parallel sessions for front end and back end; One-shot build prompt that yields a to-do list
- Tools: Claude Code, Cursor, Claude Code extension for Cursor, Claude Squad (cs), tmux, GitHub CLI (gh), git, GitHub, OpenAI Codex, Claude Opus, Claude Max plan, Claude Pro plan

## [Coding Test: Can CLAUDE COMPUTER USE Build Apps?](../videos/XbL5nzTLtag.md)
`XbL5nzTLtag` · AI LABS · 2025-11-02 · q2 · intro · review · also: voice-multimodal, context-engineering

A short hands-on test of Claude Computer Use building a budget-manager app: it handled terminal setup but failed at front-end code generation, and a page refresh wiped the project.

- Techniques: Staged prompt decomposition for agent app builds; Verify toolchain installs in the agent's terminal; Keep recoverable copies of agent-generated work outside the agent's UI
- Tools: Claude Computer Use API, Claude (Claude 3.5 mentioned as the comparison model), ChatGPT (used to write and split the build prompt), Node.js, npm

## [Connect any LLM to any MCP server without any MCP client.](../videos/QZ6AreMxMKA.md)
`QZ6AreMxMKA` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools, agent-architecture

A beginner walkthrough of a Python MCP client library that runs an agent over any LLM and any MCP server, so no desktop client is needed. Shows setup, a single-file Airbnb example, multi-server config and Cursor tips.

- Techniques: Provider-agnostic MCP agent from a config file; Cap agent steps and filter results in the prompt; Multi-server config with a service manager; Give a coding assistant the library docs; Flatten a repo for LLM questions (gitingest)
- Tools: MCP (Model Context Protocol), Python, pip3, LangChain, LangChain OpenAI integration, LangChain Anthropic integration, OpenAI, Anthropic, Cursor, Windsurf, Claude Desktop, Airbnb MCP server

## [The GPT-5 Backlash, AI CLI Tools & AI Agent Protocols | Better Stack Podcast Ep 1](../videos/no8ijoB4qxM.md)
`no8ijoB4qxM` · Better Stack · 2025-11-02 · q2 · intro · other · also: claude-code, mcp-and-tools, evals

Better Stack podcast on GPT-5's messy rollout, Claude Code's lead among CLI coding tools, benchmark contamination, and why MCP won while rival agent protocols stalled. Opinion-heavy, little hard data.

- Techniques: Benchmark contamination check; Plan with the strong model, execute with the cheaper one; Turn an existing REST API into an MCP server; Convert web pages to Markdown before sending them to the model; Pair a strong general model with a browser MCP server; Custom Claude Code status line
- Tools: GPT-5, GPT-5 medium, GPT-5 high, OpenAI Codex (Codex CLI), Claude Code, Claude Sonnet, Claude Opus (4.1), Cursor, GitHub Copilot, VS Code, Goose, OpenCode (SST)

## [Why Developers Are Switching from Claude](../videos/XKdeJAKTb3M.md)
`XKdeJAKTb3M` · Better Stack · 2025-11-02 · q2 · intro · review · also: models-research, token-cost-efficiency

Better Stack runs Sonnet 4.5, GLM 4.6 and GPT-5 Codex through three coding tasks in OpenCode (portfolio site, HN clone, Minecraft-like game); no model wins everywhere, and GLM 4.6 is pitched as the value pick.

- Techniques: Same-prompt, same-harness model bake-off; Prompt-file execution; Feed back runtime errors as follow-up prompts
- Tools: Claude Sonnet 4.5, GLM 4.6 (Z.ai), GPT-5 Codex, OpenCode, Unsplash, TanStack

## [3 Things I Wish I Knew Before using Claude Code](../videos/_9T-6dw-CZs.md)
`_9T-6dw-CZs` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: claude-code, mcp-and-tools, context-engineering

A beginner-level walkthrough of five Claude Code features: custom slash commands, Cursor integration with multi-line input, adding MCP servers (Sentry example), plan mode with CLAUDE.md, and the "ultrathink" keyword.

- Techniques: Custom slash command as a prompt file; Claude Code inside Cursor; Add an MCP server from an existing Cursor or Windsurf JSON config; Use MCP server commands from slash commands; Plan first, then save rules to CLAUDE.md; Add 'ultrathink' to a prompt for hard problems
- Tools: Claude Code, Cursor, Windsurf, Sentry, Sentry MCP server, Seer (Sentry AI agent), Claude Agent SDK, Claude GitHub app

## [Claude Sonnet 4.5 is HERE + Claude Code Upgrades](../videos/dDsa7_G7djc.md)
`dDsa7_G7djc` · Better Stack · 2025-11-02 · q3 · practitioner · news · also: claude-code, models-research, context-engineering

Better Stack's roundup of Anthropic's Claude Sonnet 4.5 launch and Claude Code 2.0 updates (VS Code extension, checkpoints, prompt history), with a one-prompt comparison against GPT-5 and Sonnet 4.

- Techniques: Rewind to a checkpoint in Claude Code; Search prompt history with Ctrl+R; Use the VS Code extension with editor context; Compare models on one prompt in the same harness; Enable context editing and the memory tool in the Claude API
- Tools: Claude Sonnet 4.5, Claude Sonnet 4, Claude Code 2.0, Claude Code VS Code extension, Claude Agent SDK (renamed from Claude Code SDK), Claude API context editing, Claude API memory tool, Imagine with Claude (research preview), Claude in Chrome extension, GPT-5, GPT-5 Codex, OpenCode

## [Cursor AI Shotgun Code (FREE): Fix Any Next.js App with AI (Full Tutorial)](../videos/4A66bMRiPQ0.md)
`4A66bMRiPQ0` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: context-engineering, vibe-coding-app-building

A walkthrough of Shotgun Code, which packs a whole Next.js repo into one prompt, gets a full diff from Gemini 2.5 Pro, and applies it in Cursor to overhaul a personal app.

- Techniques: Setup and launch from repo root; Curate the context before generating the prompt; Write one task plus custom rules into the packed prompt; Generate the diff in Google AI Studio; Apply the diff with a coding agent in chunks; Control visual style through the task text
- Tools: Shotgun Code (the GitHub repo demoed, a Go app with a frontend), Go, Node.js, Wails CLI (captioned as 'Wales'), Next.js, Google AI Studio, Gemini 2.5 Pro, Gemini Flash (mentioned as the option not to use), Cursor, Windsurf (mentioned as an alternative executor), Claude 3.5 Sonnet, shadcn/ui (captioned as 'shad cn')

## [Vibe Coding Debugging: The Only Tutorial You Need for 10X Fast Debugging](../videos/2h8WSChA1-o.md)
`2h8WSChA1-o` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: observability, mcp-and-tools

A Sentry MCP walkthrough: an agent in Cursor creates a Sentry project, installs the Next.js SDK, wires the DSN, triggers test errors, then reads an issue's trace and proposes a fix. Vendor-led, with a paid SEER feature.

- Techniques: Let the agent provision Sentry through the MCP; Install the Sentry MCP into a client; Debug an error from its issue data, not the raw code; Set a verification step after the agent wires monitoring
- Tools: Sentry, Sentry MCP server, Sentry SDK, Next.js, Python SDK, Cursor, Claude Code, SEER, mcp.json

## [Claude Engineer is INSANE... Upgrade Your Claude Code Workflow](../videos/6Rg5M69bMgQ.md)
`6Rg5M69bMgQ` · AI LABS · 2025-11-02 · q2 · intro · review · also: claude-code, context-engineering, mcp-and-tools

A walkthrough of two free add-ons for Claude Code: the SuperClaude configuration framework (slash commands, flags, personas, MCP-wired workflows) and a basic browser web UI for reaching Claude Code from other devices on the LAN.

- Techniques: Install SuperClaude from its GitHub repo; Have an AI write a usage guide from the framework's own config; Turn a phase into a runnable slash command plus prompt; Wire MCPs yourself, then reference them through flags; Reach Claude Code from a phone on the same LAN
- Tools: SuperClaude (configuration framework for Claude Code; no version stated), Claude Code, Cursor (used to read config and generate docs.md), Context7 MCP, Sequential MCP, Magic UI MCP, Puppeteer MCP, React, Next.js (spoken as 'xjs'), ElevenLabs API, OpenAI API, Warp (terminal, used to get the LAN IP)

## [Codeium Windsurf: The Full-Stack App Builder | Better Than Cursor?](../videos/Wvyc2E6OHm8.md)
`Wvyc2E6OHm8` · AI LABS · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building

A feature tour of Windsurf's Cascade and Flows agent features, comparing it with Cursor and building a 2048 game and a Splitwise clone from single prompts. Useful as a demo of full-stack generation, thin on technical depth.

- Techniques: Start from an example project in Cascade; Iterative follow-up prompt, then review with OpenDiff; Name-based full-stack build prompt; Paste raw errors back into the agent; Flows for multi-step tasks with context kept
- Tools: Windsurf (Codeium editor), Cascade, Flows, Cursor, Cursor Composer, GitHub Copilot, VS Code, Bootstrap 5, Claude models (named as available on Windsurf Pro, no version given), GPT-4 (named, no version given), OpenDiff

## [Is This The Future of Vibe Coding? (Vibe Kanban)](../videos/NKkO8JL6IJg.md)
`NKkO8JL6IJg` · Better Stack · 2025-11-02 · q2 · intro · review · also: software-factory, vibe-coding-app-building

Better Stack walkthrough of Vibe Kanban, a free open-source board that assigns tasks to coding agents, runs them in parallel and sends their diffs to review; the setup is clear, but the depth is thin and the demo shows bugs.

- Techniques: Kanban as a dispatcher for parallel agent tasks; Setup via npx and the in-app flow; Per-task agent and base-branch selection; Human review gate before merge
- Tools: Vibe Kanban (npx vibe-kanban), Claude Code, Amp, Gemini CLI, OpenCode, Codex (transcript shows 'echo', likely Codex), VS Code, GitHub, Nuxt, Tailwind CSS, MCP servers (configurable in the app)

## [People Are Getting RICH With AI Mobile Apps – Let’s Build One](../videos/HQJUvSLO91o.md)
`HQJUvSLO91o` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building, context-engineering

A walkthrough of building a macOS menu-bar Swift app by prompting Windsurf with a docs-first template and Gemini 2.5, after Claude failed on the same prompt; mostly process, with the prompt itself left in the video description.

- Techniques: Docs-first agent prompt for a new app; Scaffold the native project and place it in the agent workspace; Relay errors as text, and switch models for visual bugs; Turbo mode for unattended builds; Export a standalone macOS app from Xcode
- Tools: Windsurf, Cursor, Gemini 2.5, Claude 3.7, Claude, ChatGPT, Xcode, Swift, SwiftUI, Taskmaster (mentioned, as needing Claude and Perplexity API keys), Perplexity API (mentioned), Next.js (analogy only)

## [Context7 MCP Tutorial: Get Instant RAG for Your AI Coders](../videos/323l56VqJQw.md)
`323l56VqJQw` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools, context-engineering

Tutorial on wiring the Context7 MCP server into Cursor so the agent pulls current, targeted library docs instead of stale training data or whole doc files; the evidence is one informal before/after build.

- Techniques: Add Context7 as an MCP server in Cursor; Recover missing MCP tools; Pull targeted doc sections instead of attaching whole docs; Keep API keys out of agent context
- Tools: Cursor, Context7 MCP server (context7.com), mcp-use (auto-caption 'mcpus'; the Python agent framework built in the demo), Playwright MCP, Claude 3.7 (model named by the speaker), shadcn/ui (example library), Next.js (example framework), Windsurf, VS Code with GitHub Copilot agent, .cursorignore

## [Google Firebase is an AI IDE now... (and its good!?)](../videos/dAE4YloBUgI.md)
`dAE4YloBUgI` · Better Stack · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building, product-ux

A Better Stack walkthrough of Google's Firebase Studio, a browser IDE that turns a prompt into a blueprint, a built app, and a Firebase deployment. The presenter finds the prototyping flow useful but the annotation and AI-injection behavior unreliable.

- Techniques: Confirm the blueprint before the build; Auto-provision the Gemini key from the build prompt; Scoped edit with inspect-element; Annotation overlay (lower reliability); Phone check via public preview link; Drop into the code view for manual fixes; Publish with Firebase App Hosting
- Tools: Firebase Studio, Project IDX (earlier name of Firebase Studio), Gemini 2.5 Pro, Gemini Flash, Gemini 2.5 Pro Experimental, Gemini API, Google AI Studio, Excalidraw, ShadCN UI, Next.js, Astro, Firebase App Hosting

## [Supabase MCP Cursor Integration (Step by Step)](../videos/b_hr1TB2GYQ.md)
`b_hr1TB2GYQ` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: mcp-and-tools, context-engineering

Step-by-step setup of Supabase's MCP server in Cursor so the agent can see the live database schema, with a connection-string walkthrough and a bash-wrapper trick. Anecdotal, short, and light on verification data.

- Techniques: Add Supabase MCP to Cursor via the command type; Wrap the MCP command in a bash script; Make the agent verify schema before and after each DB step
- Tools: Supabase, Supabase MCP server, Supabase CLI (`supabase status`, local instances), Cursor, Windsurf, Claude Desktop, GitHub MCP server, bash

## [Integrate Cursor/Windsurf into Apple Ecosystem with This Cursor MCP Setup!](../videos/htbzu9s189E.md)
`htbzu9s189E` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools

Walkthrough of connecting the open-source apple-mcp server to Cursor so an agent can read and act on Apple Contacts, Notes, Messages and Reminders; mostly setup steps, with a useful note on restructuring a tool's navigation.

- Techniques: Register a local MCP server in Cursor; Get the absolute entry path for an MCP server; Use agent mode to call MCP tools; Extend an MCP server by having the agent copy existing modules; Restructure a search-everything tool into hierarchical navigation
- Tools: Cursor, apple-mcp (GitHub repo, MCP server for Apple apps), Claude Desktop, Windsurf, Docker MCP server (already added in Cursor, unrelated to the Apple setup), Claude 3.5 Sonnet, GPT-4, bun, realpath, Apple Notes, Apple Contacts, Apple Messages

## [Task Master AI Has Changed How I Code FOREVER (w/ Claude Code)](../videos/1I73OFAnvdg.md)
`1I73OFAnvdg` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: claude-code, context-engineering, software-factory

Better Stack walkthrough of Task Master AI with Claude Code: a PRD is parsed into dependency-tracked tasks, scored for complexity, expanded into subtasks, then run one at a time. The demo app built in one pass, but the claims rest on one example.

- Techniques: Pick models per Task Master role; Have the model write the PRD from an example template; Parse the PRD into tasks, then score complexity and expand the hardest tasks; Drive the work loop by task status; Keep project hooks in the loop
- Tools: Task Master AI (taskmaster / task-master-ai), Claude Code, Claude Sonnet, Claude Opus, OpenAI API, Next.js, IndexedDB, MCP (mcp.json), fish shell, Git, bun, npm

## [Phi-4: The Smallest Open Source AI Model](../videos/yzSYIndCWD8.md)
`yzSYIndCWD8` · AI LABS · 2025-11-02 · q2 · intro · review · also: local-ai, vibe-coding-app-building

Single-run hands-on test of Phi-4 (14B, MIT license) through Ollama, bolt.diy and Cline. It runs locally, but it failed to integrate a React component, which the speaker blames on the context window.

- Techniques: Local model via Ollama; OpenRouter key as a hosted fallback; bolt.diy from source; Point Cline at local Ollama; Frontier model writes, local model integrates; Shrink the task when the agent stalls
- Tools: Phi-4 (Microsoft, 14B open weights, MIT license; captioned as "5.4"), Ollama, OpenRouter, bolt.diy (captioned "BoltDIY" and "bold.diy"), Cline (captioned "Klein"; formerly Claude Dev), Claude (used to write the card component), VS Code, pnpm, Next.js 14, React, TypeScript, Tailwind CSS

## [How I Build Apps 10x Faster with this 7-Step Cursor Workflow](../videos/cAFIUiE_8DM.md)
`cAFIUiE_8DM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building, context-engineering

A solo builder walks through a seven-step AI app workflow (idea, MVP, HTML prototype, design.json styling, SwiftUI conversion, Supabase backend, UI polish) for an iOS habit app, using Cursor and Claude Code.

- Techniques: Stage-gated AI app build; Screenshot-driven correction loop; design.json from a reference image; Rules-file-driven framework conversion; MCP-based backend provisioning; Image model for app icon iteration; Model switching by task
- Tools: Cursor, Claude Code, Claude (chat), ChatGPT, OpenAI image generation model, Supabase, Supabase MCP server, Supabase SDK, SwiftUI, Swift, Xcode, Next.js (mentioned as an example template)

## [OpenAI O3-Mini: The Fastest Reasoning Model Yet?](../videos/cdYA5QV8gRY.md)
`cdYA5QV8gRY` · AI LABS · 2025-11-02 · q2 · intro · review · also: models-research, evals

Quick anecdotal test of OpenAI's o3-mini and o3-mini-high: the speaker reports correct answers on six reasoning prompts, far faster than o1, plus a Chrome extension built with o3-mini-high.

- Techniques: Latency-first spot check of a reasoning model; Pick the lower reasoning tier when the task is simple; One-shot scaffold for a small browser extension
- Tools: o3-mini, o3-mini-high, o1, ChatGPT, Chrome extension, Cursor, Windsurf

## [Gemma3n - The Most OVERHYPED AI Model of 2025 (For Coding)](../videos/FCl6ZR8l_EM.md)
`FCl6ZR8l_EM` · Better Stack · 2025-11-02 · q2 · intro · review · also: local-ai, models-research

Better Stack gives Gemma 3n, Llama 4 and DeepSeek R1 three browser coding prompts. Gemma 3n finishes last, and the speaker concludes open models aren't ready for complex coding.

- Techniques: Feed errors back for a fix; Switch language when a generated graphic does not render; Give the model the CDN link for a 3D library; Same-prompt, multi-attempt model bake-off
- Tools: Gemma 3n, Llama 4, DeepSeek R1, DeepSeek, Ollama, Three.js, Python, JavaScript, Claude 3.7 (comparison reference)

## [INK: The React Library POWERING AI Terminal Tools (For Now...)](../videos/qSZwx5_EmSA.md)
`qSZwx5_EmSA` · Better Stack · 2025-11-02 · q2 · intro · review · also: dev-tools

Quick Ink (React for terminals) counter tutorial that measures its memory cost against Bubble Tea and points to OpenTUI as a leaner TypeScript alternative.

- Techniques: Ink counter component pattern; Measure the runtime footprint before choosing a TUI framework; Keep the TUI process alive until an explicit exit key
- Tools: Ink, React, TypeScript, Yoga (WASM build, flexbox layout), Bubble Tea (Go), OpenTUI (Zig and TypeScript), Bun FFI, SolidJS implementation of OpenTUI, OpenTUI core, OpenCode, Qwen Code, Gemini CLI

## [MCP Servers are Security Nightmares...](../videos/CRKYNyMc4PM.md)
`CRKYNyMc4PM` · Better Stack · 2025-11-02 · q3 · practitioner · demo · also: security-guardrails, mcp-and-tools

Demo of MCP tool poisoning, tool shadowing, rug-pull mutation and command injection in MCP servers. Main takeaway: treat tool descriptions and server code as untrusted input.

- Techniques: Pin and diff tool definitions; Review full tool descriptions and arguments before approval; Treat tool descriptions as untrusted input; Avoid shell interpolation in MCP tool handlers; Probe your own MCP servers directly; Limit what a server can reach
- Tools: Cursor, MCP (Model Context Protocol), WhatsApp MCP server (community project, named as legitimate), MCP client libraries (used to call server tools directly)

## [Warp Code Tutorial: Save 90% of Time with Warp AI Agents (vs Claude Code) Agentic Development](../videos/STd07QswCpk.md)
`STd07QswCpk` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: context-engineering, multi-agent, mcp-and-tools

Sponsored walkthrough of building a full-stack notes app with Warp's agentic development environment, covering PRD planning, parallel agents split by API contract, saved prompts and rules, and MCP context.

- Techniques: PRD-first, then API contract, then fan out; Saved prompts as reusable commands; Templated workflows for known-hard setup steps; Rules to pin dependency and library behavior; Notebooks as context documents; Explicit task list for long runs; Parallel agent tabs with completion monitoring
- Tools: Warp (agentic development environment and terminal, with a built-in AI agent), Warp Drive (saved prompts, rules, MCP servers, workflows, notebooks), Context7 MCP, Playwright MCP, ChatGPT, Express Validator, Zod, Next.js, SWE-bench (vendor claim: 75.8%), Terminal Bench (vendor claim: #1)

## [Connect to Anything with This Cursor MCP Setup](../videos/brhs5DogIf8.md)
`brhs5DogIf8` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools

Walkthrough of adding community MCP servers to Cursor as stdio commands (Docker, YouTube summarizer), with a YOLO-mode caveat; mostly screen-recorded clicks, thin on specifics.

- Techniques: Add a stdio MCP server in Cursor; Verify tool access with a small agent-mode task; Use YOLO mode only with monitoring; Summarize a YouTube video through MCP
- Tools: Cursor, Model Context Protocol (MCP), Claude Desktop app, Claude, Composer (Cursor agent), uvx, Docker MCP server, Jira MCP server, Spotify MCP server, Shopify MCP server, YouTube MCP server, yt-dlp

## [BREAKING: OpenAI BUYING Windsurf, NEW Coding Tool, o3 and o4-mini](../videos/FesaebCzgH0.md)
`FesaebCzgH0` · Better Stack · 2025-11-02 · q2 · intro · news · also: models-research, token-cost-efficiency

Launch-day walkthrough of OpenAI's o3 and o4-mini: o3 uses OCR, crop-and-zoom and web search on one screenshot; open-source Codex CLI is tried on a React repo and a Pong feature; benchmarks and prices come from launch slides.

- Techniques: Iterative image crop and OCR loop; Codex CLI first run on an unfamiliar repo; Patch the open-source CLI from a local clone; One-shot physics prompt as a quick smoke test
- Tools: o3, o4-mini, o4-mini-high, Codex CLI, ChatGPT, Claude Code, Claude 3.7 Sonnet (reasoning), Gemini 2.5 Pro, GPT-4.1, npm, Windsurf, Cursor

## [Claude code vs Codex vs Cursor: Who gets the cake?](../videos/_Xbe7MQ2NxI.md)
`_Xbe7MQ2NxI` · AI LABS · 2025-11-02 · q2 · intro · review · also: claude-code, mcp-and-tools, agent-architecture

Argues Claude Code and other AI CLIs are "portable agent engines": terminal agents can call each other via bash, run headless (-p), deploy to GitHub Actions and act as MCP servers. Opinion-heavy, with a sponsor segment.

- Techniques: Headless single-shot invocation; Cross-agent delegation through bash; Scheduled agent via GitHub Actions; Claude Code GitHub app for PR review; Mixed local and remote MCP servers
- Tools: Claude Code, Claude Code GitHub app, Claude Code for Chrome, Claude for Excel, Agent SDK (formerly Claude Code SDK), Codex CLI, Gemini CLI, Qwen Code (transcript: QuenCode), Cursor CLI, gitingest, GitHub Actions, Slack

## [Here Is How to Vibe Code Large Scale Projects](../videos/k9fPAzS5_Kw.md)
`k9fPAzS5_Kw` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: context-engineering, vibe-coding-app-building

AI LABS walkthrough of Plandex, a self-hosted CLI coding agent aimed at large projects: local Docker setup, chat-then-tell workflow, reviewable sandboxed changes, and one Swift app demo. Context-size claims are unverified.

- Techniques: Self-host Plandex in local mode; Set keys and initialize a repo; Chat to brainstorm and understand, then tell to implement; Review before applying, and debug failed commands
- Tools: Plandex, Docker, OpenRouter API, OpenAI API, Tree-sitter, Cursor, Xcode, Swift, SwiftUI, Gemini 2.5

## [This MCP Setup is the Best Way to Add 3D Models to Your Frontend](../videos/srsst0L51RE.md)
`srsst0L51RE` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools, vibe-coding-app-building

Short tutorial on connecting the Sketchfab MCP server to Cursor so an agent can search, download and place a 3D model into a Three.js landing page from one prompt.

- Techniques: Install the Sketchfab MCP server from source; Get a Sketchfab API token; Get the absolute path to the built server entry point; Register the server in Cursor via mcp.json; Prompt for a 3D hero section and iterate on the model
- Tools: Sketchfab MCP server (community server listed on mcp.so), Sketchfab, Cursor, Windsurf, Claude Desktop, Three.js (3JS), git, npm, Claude 3.7 (mentioned for 3D game generation)

## [Traycer is INSANE… Cursor AI is Not Enough Anymore](../videos/0hAS1xCeixQ.md)
`0hAS1xCeixQ` · AI LABS · 2025-11-02 · q2 · intro · review · also: context-engineering, testing-verification

A product walkthrough of Traycer, an IDE extension that runs a planning stage (gap-filling questions, phased plan), implementation, and a self-review pass before or alongside coding agents such as Claude Code and Cursor.

- Techniques: Clarify-before-plan requirements file; Phased plan as the unit of execution; Plan handoff to a coding agent; Severity-classed self-review pass; Change tracking with M/N badges; Version-conflict repair by dependency pinning
- Tools: Traycer (IDE extension, sign-up required), Next.js, TypeScript, Tailwind CSS (v3 before the intentional upgrade), HeroUI (named as Hero UI), NextUI (mentioned as the wrong provider), shadcn (mentioned as a common library), Claude Code, Cursor

## [Develop Faster using the browser tools MCP Cursor/Windsurf.](../videos/G25UyWfYogQ.md)
`G25UyWfYogQ` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: mcp-and-tools, testing-verification

Walkthrough of the browser-tools MCP server, which lets Cursor's agent run accessibility/SEO/performance audits, read screenshots and selected DOM elements from Chrome, and iterate on front-end fixes.

- Techniques: Install browser-tools MCP into Cursor; Load the Chrome extension and start the connector; Accessibility audit and fix loop; Configure screenshot folder and auto-paste; Select-element targeting; Voice mode for prompting
- Tools: browser-tools MCP server (browser-tools-mcp, GitHub repo linked in the description), Cursor (IDE and agent), Windsurf (mentioned for its select-element feature), Chrome browser extension (browser-tools), Chrome DevTools (Browser Tools MCP tab for settings and screenshot folder), mcp.json (Cursor MCP config file), React (demo app's calendar component)

## [Bash Apps Are INSANE… A New Way To Use Claude Code](../videos/1_twhMU9AxM.md)
`1_twhMU9AxM` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: claude-code, context-engineering

Wrap any terminal CLI as a Claude Code agent via CLAUDE.md; builds a Git Agent on GitIngest and Click that stores repo context in the repo. Practical pattern, light on code.

- Techniques: Document a CLI as an agent tool in CLAUDE.md; Token-size gate before repo extraction; Persist extractions and analyses as repo files; Wrap an existing CLI in a Click command group; PRD-first build loop with Claude Code
- Tools: Claude Code, Claude Desktop, Cursor, GalleryDL, aria2, GitIngest (git ingest, open-source CLI with a GitHub URL mode), Git Agent (the speaker's own CLI wrapper, not released in the transcript), BMAD method (framework mentioned as a past featured video, not demoed), Click (Python CLI framework; auto-captions say Qlik), CLAUDE.md, ScaleKit (sponsor; OAuth and auth layer for AI apps)

## [Codex SDK vs Claude: One is CLEARLY Better](../videos/X1izM-063g0.md)
`X1izM-063g0` · Better Stack · 2025-11-02 · q2 · intro · review · also: agent-architecture

Short walkthrough of the TypeScript-only Codex SDK (run, streamed events, sandbox modes, tool calls, a follow-up loop), ending with the host preferring the Claude Agent SDK for its missing features.

- Techniques: Minimal Codex SDK script; Choose a sandbox mode per run; Resume a thread by ID; Structured response via JSON schema or zod; Stream typed events with runStreamed; Interactive loop over one thread
- Tools: Codex SDK (TypeScript), Codex CLI, Codex IDE extension, Codex Web, Claude Agent SDK, OpenAI App SDK, OpenAI Agent Builder, zod

## [Google's New AI Code Editor Built My Flutter App in the Browser!"](../videos/P4xA6j3B39U.md)
`P4xA6j3B39U` · AI LABS · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building

Hands-on review of Google's browser-based Project IDX: the host builds a Flutter task-manager app with its Gemini chat, and reports that fixes needed repeated prompting and manual insertion.

- Techniques: Full-file repair loop; Explicit insert prompt; Observable-symptom prompt; Review diff before applying; Setup steps for the browser IDE
- Tools: Project IDX, Gemini, Flutter, VS Code, Cursor, Windsurf, Expo, Next.js, Python, Go, Node.js

## [GitHub MCP Server: Let AI Handle Your GitHub](../videos/TrDW2Puhw0Y.md)
`TrDW2Puhw0Y` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: mcp-and-tools, dev-tools

Step-by-step setup of the GitHub MCP server in Cursor, then a live demo of an agent creating a repo, pushing a file, cloning and searching GitHub from the chat.

- Techniques: Wrap the GitHub token in a shell script for Cursor's MCP command; Create a GitHub classic personal access token for the MCP server; Register the script as a command-type MCP server in Cursor; Smoke-test the MCP connection with a read-only query
- Tools: GitHub MCP server (GitHub's official MCP server, run through npx), Cursor (IDE, agent mode, MCP settings), npx, bash, nano, realpath, GitHub classic personal access tokens, Claude Desktop (mentioned as the server's reference client), Archon (another creator's agent-building repo, mentioned in passing)

## [Anthropic Claude AI Agentic Browser: The Claude Chrome Extension for Builders (EXCLUSIVE DEMO)](../videos/TVetQbcgdMU.md)
`TVetQbcgdMU` · AI LABS · 2025-11-02 · q3 · practitioner · review · also: testing-verification, voice-multimodal

Hands-on demo of Anthropic's Claude Chrome extension as a visual-testing partner for Claude Code: a slash command reviews each finished task on a running dev server, and the browser agent reports visual and functional issues.

- Techniques: Per-task visual review slash command; Fresh chat per task; Prioritized improvement triage before the next task; Batch review of several tasks; Per-site approval allowlist for browser actions
- Tools: Claude Code, Claude Chrome extension (Claude browser extension, research preview), Claude 4 series models, Next.js, GPT (used to brainstorm the app idea), BMAD method (mentioned, not used), Playwright MCP (compared, not used), Cursor (mentioned as a competitor)

## [I Built 5 Websites Without Touching HTML:  Here's How (Kibo UI)](../videos/6odlDS7-G8k.md)
`6odlDS7-G8k` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: vibe-coding-app-building, mcp-and-tools, context-engineering

Tutorial on wiring the shadcn MCP server and a custom 1100-component Kibo UI registry into a coding agent, plus TweakCN's live-embed theming flow for building Next.js UIs.

- Techniques: Wire the shadcn MCP into a Next.js or React project; Host a custom component registry from shadcn's registry template; Category-guided component selection for very large catalogs; Two-command design-first workflow (init once, build per session); Embed a TweakCN live theme preview into a Next.js app
- Tools: shadcn, shadcn CLI, shadcn MCP server, shadcn registry template, Kibo UI (patterns registry, ~1100 components), TweakCN, TweakCN MCP server, Next.js, React, Claude Code, Cursor, components.json

## [OpenAI Codex Hacked: Use It with Gemini 2.5 PRO (The Best Coding Model)](../videos/e3yxrNoC7mc.md)
`e3yxrNoC7mc` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: context-engineering

Walkthrough of setting up a multi-provider fork of OpenAI's Codex CLI with Gemini 2.5 Pro, including config files and full-auto use, plus a failed full-scope attempt and a narrowed retry.

- Techniques: Swap the model behind a forked CLI agent; Persist per-project agent setup in files, not shell exports; Run the agent inside a git repo; Full-auto single-prompt build, then narrow scope on stall
- Tools: OpenAI Codex CLI, OpenCodex (community fork of Codex CLI, name as spoken in the video; exact package name not stated), npm, Gemini 2.5 Pro, Google AI Studio, Google Cloud, OpenRouter, Ollama, shadcn/ui, Next.js, Cursor (used as the editor to open config.json), git

## [SAVE Your 20$ by using Cursor AI for FREE!](../videos/Nm2Lhe0-6To.md)
`Nm2Lhe0-6To` · AI LABS · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, token-cost-efficiency

Walkthrough of Desktop Commander, a free MCP server that gives Claude Desktop file, terminal and edit tools, demoed by building a Next.js and FastAPI image editor from one prompt.

- Techniques: Replace an AI IDE with an MCP server in an existing chat client; One prompt with a target path and an objective; Search-and-replace edits instead of full-file rewrites; Read and change the MCP server's config through its own tools; Run-and-verify loop with bug reports in chat; Side-by-side IDE view with agent edits
- Tools: Desktop Commander MCP, Claude Desktop, File system MCP server, Claude Code, Cursor, Windsurf, VS Code, Cline (transcribed as 'Klein'), Roo Code (transcribed as 'RuCode'), Claude 3.7 Sonnet, Claude 3.5 Sonnet, Next.js

## [I've Been Using the n8n MCP WRONG - The Correct Workflow](../videos/jUfpYmN9q6Y.md)
`jUfpYmN9q6Y` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: claude-code, context-engineering, mcp-and-tools

Driving the n8n MCP from Claude Code works better with a phased, file-based workflow: plan, research, build and validate in separate sessions, delete-and-recreate on update, and OAuth instead of API keys.

- Techniques: Phased file-based workflow pipeline; Clear context between phases; Put standing rules in CLAUDE.md; Pre-build version and health check; Delete-and-recreate instead of in-place update; OAuth-first credentials; Single-node isolation debugging; Documentation re-check prompt
- Tools: n8n, n8n MCP server, Claude Code, Claude Desktop, Claude.md (CLAUDE.md), OpenAI node in n8n, Google Calendar node, Gmail, Google Cloud Platform, Brave Search (from the previous video), Gamma (sponsor segment)

## [This Tool Codes for FREE – Here’s How to Install It!](../videos/xsJAA3vhy0E.md)
`xsJAA3vhy0E` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building, dev-tools

Install-and-try walkthrough of Bolt DIY, a self-hosted, free alternative to Bolt.new, driven by DeepSeek V3 through OpenRouter. The demo works for a whiteboard app, but shapes stay broken, and the title overstates what is free.

- Techniques: Clone, install and run Bolt DIY locally; Configure OpenRouter as the provider with DeepSeek V3; Set a model from the dropdown and check its voice and image support; Iterate with one bug per follow-up prompt
- Tools: Bolt DIY (bolt.diy), Bolt.new, DeepSeek V3, DeepSeek chat, deepseek-coder, OpenRouter, ShadCN UI, Claude 3.5 Sonnet, Perplexity AI, Hugging Face, pnpm, git

## [These Hidden Cursor Features Will Make You 10x More Productive](../videos/A9BiNPf34Z4.md)
`A9BiNPf34Z4` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: mcp-and-tools, context-engineering

A feature tour of Cursor's hidden productivity tools: global and project rules, notepads, indexed docs, MCP servers (Docker example), and YOLO mode for auto-running tools.

- Techniques: Global behaviour rules; Scoped project rules as .mdc files; Borrowing rule sets; Notepads as prompt templates; Web and indexed-doc references in Composer; Adding an MCP server in Cursor; YOLO mode with allow and deny lists
- Tools: Cursor, Cursor Rules (.cursor/rules, .mdc files), cursor.directory, Supabase (Postgres rule examples on GitHub), Tailwind CSS v4, Next.js, Better Stack docs, Model Context Protocol (MCP), Claude desktop app, docker-mcp (Docker MCP server, run with uvx), uv / uvx, npx

## [Automation Testing Tutorial Using Cursor AI + Operative.sh & Claude 4 (Setup + Demo)](../videos/GuKdinu64Z0.md)
`GuKdinu64Z0` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: testing-verification, mcp-and-tools

Walkthrough of installing operative.sh's web-eval MCP agent into Cursor and using plain-English test cases, including edge cases, to drive a Playwright browser against a local login page. Vendor-specific, thin on evidence.

- Techniques: Install operative.sh web-eval MCP into Cursor; Call the web eval agent with url, task and headless; Save an authenticated session once with setup-browser-state; Generate test cases to a file, then run them sequentially and write results back
- Tools: operative.sh (web eval agent, setup-browser-state tool, MCP installer, API key), Cursor (IDE, MCP host), Playwright (browser automation, installed by the setup), Claude 4 (Anthropic model; the presenter says it was released 2-3 days before recording and praises it), Aceternity UI (the demo site's UI library; auto-caption reads it as 'as eternity ui'), MCP (Model Context Protocol, the integration path)

## [Codex CLI Has Just Got WAY Better!](../videos/Szi4SHB4nNs.md)
`Szi4SHB4nNs` · Better Stack · 2025-11-02 · q3 · intro · review · also: sandboxing-execution, claude-code, mcp-and-tools

Better Stack tours the late-2025 Codex CLI update (Rust rewrite, ChatGPT login, sandbox and approval modes, config profiles) and candidly compares it with Claude Code.

- Techniques: Separate sandbox from approval when setting agent autonomy; Named config profiles in config.toml run with -p; Audit an agent run via the transcript view; Tune model and reasoning effort per task; Point Codex at an OpenAI-compatible endpoint for non-OpenAI models; Notify script for event alerts; Everyday workflow commands
- Tools: Codex CLI (OpenAI terminal coding agent), GPT-5, GPT-OSS, DeepSeek (tested, errored), AGENTS.md, config.toml, Ink (previous TypeScript UI), Ratatui (Rust TUI library), ChatGPT login, Codex VS Code plugin, Claude Code (comparison), Better Stack MCP (host plug)

## [The BMAD Method: The Ultimate AI Coding System](../videos/fD8NLPU0WYU.md)
`fD8NLPU0WYU` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: context-engineering, multi-agent

BMAD Method tutorial: role-based agents (PO, scrum master, dev, QA) shard a PRD and architecture doc into epics and stories with approval gates, run in Cursor or Claude Code.

- Techniques: Two-document spec bootstrap; Shard then epic/story decomposition; Manual approval gate via story status field; Fresh chat per agent role; Story packet handoff; Learn an unfamiliar repo by feeding it to an LLM; Per-project install with npx; Asterisk commands and role switching
- Tools: BMAD Method (BMAD Code's agile workflow; version not stated), Cursor, Claude Code, Windsurf, ChatGPT, Claude, Gemini, GitIngest, npx (BMAD installer)

## [Amazon's NEW AI IDE is Actually Different (in a good way!) – Kiro](../videos/Z9fUPyowRLI.md)
`Z9fUPyowRLI` · Better Stack · 2025-11-02 · q3 · intro · review · also: context-engineering, software-factory

Walkthrough of Amazon's Kiro, a VS Code fork built around spec-driven development (requirements, design, tasks gated by the human) and event-driven agent hooks saved in the repo.

- Techniques: Staged spec gate before implementation; Spec re-sync after manual edits; Event-driven hook for doc or test upkeep; Steering documents
- Tools: Kiro, VS Code, Claude (Sonnet 3.7 and 4 model options), Cursor (comparison only), React, TypeScript, tRPC, Mermaid, Storybook, MCP servers, GitHub, Google login

## [Postman MCP Server Tutorial: Build & Run AI Agents with APIs (Postman MCP Generator + Cursor)](../videos/QDz4htGbOC4.md)
`QDz4htGbOC4` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools

Tutorial on Postman's MCP generator: turn selected API requests into a locally run MCP server, then register it in Cursor and call it from the chat. Thin on depth, but the steps are reproducible.

- Techniques: Generate a local MCP server from API docs in Postman; Put secrets in the generated .env file; Register a local MCP server in Cursor; Test an MCP server through Postman; Build an agent from an MCP server in code with mcp-use
- Tools: Postman MCP generator, Postman, Model Context Protocol (MCP), FastAPI MCP library, mcp-use, Cursor, Claude Desktop, Windsurf, Node.js, npm, OpenWeatherMap API

## [Time to UPGRADE… Unified AI Agents Are Finally Here](../videos/VDql5GzoSoc.md)
`VDql5GzoSoc` · AI LABS · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, rag-retrieval

Walkthrough of ACI.dev, a hosted platform that connects apps to agents via an app store, an agent playground and a unified MCP server with search and execute tools; the hype title outruns the unbenchmarked speed claims.

- Techniques: Attach apps to an agent in ACI's playground; Unified MCP server in Cursor; Separate agents with separate tool sets
- Tools: ACI.dev, ACI unified MCP server, ACI app MCP server, Agent Playground (ACI), Google Calendar, YouTube, Google Maps, Gmail, Brave Search, Archive (app named in video), Cursor, Claude Desktop

## [Claude Code SDK: Build Real AI Apps with Python & MCP](../videos/h1AGjM9IeBM.md)
`h1AGjM9IeBM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: claude-code, mcp-and-tools, pr-code-review

A short walkthrough of the Claude Code SDK (Python, with the docs' example script and a GitHub Actions demo) that frames Claude Code as a programmable subprocess. The example broke for the speaker, and the video shows no working SDK run beyond that.

- Techniques: Run Claude Code as a subprocess from Python; Cap agent iterations with max_turns; Attach external MCP servers to programmatic Claude Code; Mention-triggered issue-to-PR workflow in GitHub Actions
- Tools: Claude Code, Claude Code SDK (Python, TypeScript, CLI), ClaudeCodeOptions, query(), Cursor, GitHub Actions, Claude Code GitHub Actions workflow, Jira MCP server, Slack MCP server, pip

## [Github Spec Kit FINALLY Fixed AI Coding](../videos/M0ivqkQ5mF4.md)
`M0ivqkQ5mF4` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: context-engineering, multi-agent, testing-verification

A walkthrough of GitHub Spec Kit's specify, plan and tasks workflow driving Claude Code on a demo app, with an honest verdict: the spec-first flow works, but tasks run by hand and the UI came out cluttered.

- Techniques: Requirements in a general chat model before spec-kit; Run /specify with the requirements and answer the clarification flags; Run /plan after the spec is settled; Run /tasks and write tests before implementation; Run independent tasks in parallel with sub-agents
- Tools: GitHub Spec Kit ("Specify"), Claude Code, ChatGPT, Gemini (supported assistant), GitHub Copilot (supported assistant), ShadCN UI components, Notion (visual theme followed), git

## [Windsurf vs Cursor: The AI IDE Battle](../videos/AD4BLcJf5Bg.md)
`AD4BLcJf5Bg` · Better Stack · 2025-11-02 · q3 · intro · review · also: context-engineering, token-cost-efficiency

Side-by-side walkthrough of Windsurf (Codeium) and Cursor, both VS Code forks: inline edits and tab completion are about even, while Windsurf's Cascade agent felt more context-aware and cheaper on paper.

- Techniques: Inline edit with a model picker; Terminal command prompt with undo context; Agentic scaffold with per-step accept and mid-run redirect; Continue-my-work after manual edits; Chat-only mode for AI suggestions without edits
- Tools: Windsurf (Codeium editor), Cascade (Windsurf agent: chat, write and terminal modes), Super Complete (Windsurf next-edit prediction), Cursor, Tab (Cursor next-edit prediction), Composer (Cursor agent), Claude 3.5 Sonnet, GPT-4o, React, Vite, create-react-app (rejected by the agent in the demo), Tailwind CSS

## [ShadCN Dropped Something to FINALLY Fix Your UI](../videos/mSMflOx5pq8.md)
`mSMflOx5pq8` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: mcp-and-tools, multi-agent, context-engineering

Tutorial on shadcn's official registry MCP: add extra community component registries, then run a multi-subagent workflow (requirements, component research, implementation) to build UIs without unnecessary components.

- Techniques: Install the shadcn registry MCP; Add third-party component registries; Preview a registry's visual style before using it; Three-stage subagent workflow for UI builds; Express agent for small changes; Port the commands to Cursor; Apply a TweakCN theme
- Tools: shadcn (CLI and registry MCP server), Claude Code, Cursor, VS Code, Next.js, React, npm, components.json, mcp.json, Aceternity UI, Origin UI, Neo Brutalism (registry, failed)

## [GitHub Copilot Agent Mode & Project Padawan – A Game Changer?](../videos/y3oo7MGo1DA.md)
`y3oo7MGo1DA` · Better Stack · 2025-11-02 · q2 · intro · review · also: software-factory

Hands-on walkthrough of GitHub Copilot agent mode and Edits in VS Code, plus a teaser for Project Padawan; the agent runs terminal commands but missed errors and ignored the screenshot, while Claude output matched the target better.

- Techniques: Agent mode for scaffold-and-run tasks; Screenshot as design reference, with a model check; Edits mode with voice input (speaker's caveat); Reviewing edits with diff and undo; Issue-to-PR flow (Padawan, not shown)
- Tools: GitHub Copilot, VS Code, Copilot Agent mode, Copilot Edits, Project Padawan, Cursor, Windsurf, Devin, Claude 3.5 Sonnet, GPT-4o, Gemini 2 Flash, Next.js

## [I Tried Building an Expo App in 360 Seconds… Here’s What Happened](../videos/Dmgu7jE2toM.md)
`Dmgu7jE2toM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building, context-engineering

Walkthrough of a two-tool flow for Expo mobile apps: Tempolabs generates the PRD, user flow and wireframes, then Cursor takes over the code via a synced docs folder. Single-project demo with no measurements.

- Techniques: PRD and user flow from a requirements prompt; Connect the builder to the IDE via the Tempolabs extension; Commit the spec into the repo as context for the coding agent; Route stubborn bugs to the agent that made the code; Verify gestures on a device, not the desktop preview
- Tools: Tempolabs, Cursor, Expo, Expo Go, Gemini 2.5 Pro, ChatGPT, Mermaid, Windsurf, Next.js, Supabase, Stripe, SSH

## [Stack Overflow for your LLMs (and you!)](../videos/IYyyiA5eWEo.md)
`IYyyiA5eWEo` · Better Stack · 2025-11-02 · q3 · intro · review · also: mcp-and-tools, rag-retrieval

A short Better Stack tool walkthrough of grep.app, a fast regex code search over GitHub, and its MCP server, which lets Claude Code or Cursor pull real library usage into context instead of hallucinating APIs.

- Techniques: Add grep.app as an MCP server in Cursor or Claude Code; Literal and regex code search with filters; Version-specific search for new packages; Regex to detect committed secrets (defensive use)
- Tools: grep.app, GitHub, Claude Code, Cursor, MCP, Lexical, Next.js, React Router, Payload CMS

## [Agents Can FINALLY See the Frontend (Chrome DevTools MCP)](../videos/zaXKZjJvaAs.md)
`zaXKZjJvaAs` · Better Stack · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, testing-verification

Walkthrough of Chrome's DevTools MCP server, which lets a coding agent open, inspect, audit, and automate pages in a real Chrome instance. Mostly a prompt-driven demo with little setup detail.

- Techniques: Attach Chrome DevTools MCP to a coding agent; Prompt for a performance audit targeting LCP; Repeat the audit under network throttling; End-to-end flow and API check through the browser; Debug console errors and failed network requests
- Tools: Chrome DevTools MCP (Chrome's MCP server for coding agents), GitHub Copilot (agent used in the demo), Recommendoo (demo app built by the host with vibe-coding), OpenAI API (used by the demo app for suggestions), Watch Mode API (used by the demo app for title data)

## [Cursor 1.0 is their BEST update yet... (Agents, BugBot, Memories and more)](../videos/Ig-cfiqWJCs.md)
`Ig-cfiqWJCs` · Better Stack · 2025-11-02 · q3 · intro · review · also: pr-code-review, sandboxing-execution, mcp-and-tools

Feature tour of Cursor 1.0 covering BugBot PR review, remote background agents, per-project memories and one-click MCP install with OAuth, plus the security caveats of background agents.

- Techniques: BugBot on GitHub PRs with trigger control; Launching a background agent from a prompt; Background agent environment via snapshot or environment.json; Saving persistent project rules as memories; One-click MCP install with OAuth
- Tools: Cursor 1.0, Cursor BugBot, Cursor Agent, Cursor background agents, Cursor memories, Cursor dashboards, GitHub, GitHub Copilot, Claude Code (transcribed as 'clawed code'), Notion MCP server, Bun / bunx, Create React App (npx)

## [Google won't STOP... They Just Upped the Gemini CLI Again](../videos/A3AOeX1s7yw.md)
`A3AOeX1s7yw` · AI LABS · 2025-11-02 · q2 · practitioner · review · also: mcp-and-tools, context-engineering

A walkthrough of Gemini CLI's recent updates: free-tier quotas, MCP setup via settings.json, slash commands, VS Code inline diffs, and "extensions" as shareable bundles of context, MCP servers and commands.

- Techniques: Custom slash commands as TOML files for page and component generation; Adding MCP servers by editing settings.json; YOLO mode toggle for uninterrupted runs; Reviewing agent edits in VS Code via the IDE companion; Built-in session helpers; Packaging a team extension
- Tools: Gemini CLI, Gemini 2.5 Pro, ShadCN MCP (shadcn), Gemini CLI companion extension (VS Code), VS Code, Claude Code (compared, not demoed), Cursor (compared, not demoed), ChatGPT (used to draft the to-do app), TweakCN (theme source), Qwen (named as a competing free agent, no version), Skywork Super Agents (sponsor, not demoed)

## [Qwen 3 ACTUALLY Made Me Quit Claude Code](../videos/lXWazKnuZNQ.md)
`lXWazKnuZNQ` · AI LABS · 2025-11-02 · q2 · intro · review · also: token-cost-efficiency, mcp-and-tools

Walkthrough of using Qwen Code's free OAuth tier and Claude Code Router to run cheap Qwen3 Coder backends, with a single anecdotal DaisyUI build comparing it to Claude Code.

- Techniques: Qwen Code OAuth sign-in for free runs; Routing Claude Code through Claude Code Router; Context7 MCP for libraries models do not know well; Give the agent a PRD before building
- Tools: Qwen Code, Qwen3 Coder, Claude Code, Claude Code Router (ccr), Gemini CLI, Context7 MCP, DaisyUI, OpenRouter, ModelScope, Claude Sonnet 4, Cursor, CLAUDE.md

## [Google I/O in 6 Minutes (Developer Focused)](../videos/Da275bLi_-4.md)
`Da275bLi_-4` · Better Stack · 2025-11-02 · q2 · intro · news · also: models-research, local-ai, mcp-and-tools

A 6-minute developer-focused roundup of Google I/O 2025 announcements: Jules, Gemini Code Assist, Stitch, Colab, Gemini Diffusion, 2.5 Pro/Flash API features, Gemma 3N, Chrome AI APIs and Android agents.

- Techniques: Async function calling for long-running tools; URL context instead of search for known pages; Thinking budgets for cost control on 2.5 Pro; Sketch or wireframe to UI to code loop (Stitch)
- Tools: Jules, Gemini 2.5 Pro, Gemini 2.5 Flash, Gemini 2.5 Flash-Lite, Gemini Code Assist, VS Code, JetBrains IDEs, Stitch, Figma, Google Colab, Gemini Diffusion, DeepThink

## [Llama Coder: Is is WORTH It? Tested for Full-Stack App Building!](../videos/T5fIdojtR3A.md)
`T5fIdojtR3A` · AI LABS · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building

Hands-on test of Llama Coder, a free open-source prompt-to-app builder on Together AI. It improved after switching to Llama 3.3 but still fell short of Cursor, Windsurf, Bolt.new and v0.

- Techniques: Run Llama Coder locally from the GitHub repo; Paste runtime errors back into the change prompt box; Switch the generation model from the dropdown; Enable the ShadCN UI toggle; Publish and share the generated app; Use the built-in placeholder prompt for a calculator
- Tools: Llama Coder, Together AI, Llama 3.3, Llama 3.1, Qwen 2.5 Coder, Gemma 2, ShadCN UI, ChatGPT, Claude 3.5 Sonnet, GPT-4 Omni, Gemini, Cursor

## [The Windsurf vs Cursor rivalry just reached a turning point](../videos/gejEvBWbgHA.md)
`gejEvBWbgHA` · AI LABS · 2025-11-02 · q2 · intro · news · also: vibe-coding-app-building, product-ux

Windsurf feature tour: select a live page element in the preview, describe the change to Cascade, and it edits the code. Also covers Tab to Import, linter integration, suggested actions, built-in MCP docs and admin model controls. Mostly unmeasured demos.

- Techniques: Select-and-describe UI edits; Batch section edits for animations; Let the agent fix its own build errors; Drag files into the agent instead of referencing them
- Tools: Windsurf, Cascade, Cursor, Claude 3.7 (thinking mode, as named by the host), GPT-4.5 (as named by the host), DeepSeek V3, MCP

## [Warp CLI: Access the Latest AI Models Anywhere For FREE](../videos/dxvowd5bdoI.md)
`dxvowd5bdoI` · Better Stack · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, dev-tools

A short walkthrough of Warp CLI, which runs Warp's saved prompts, agent profiles and MCP servers from any terminal, including headless one-shot runs for scripts and CI.

- Techniques: Headless one-shot agent run; Reuse a saved Warp Drive prompt from the CLI; Run a saved workflow with arguments; Pin model and permissions with an agent profile; Attach an MCP server to a single run; Chain prompts in a shell script
- Tools: Warp CLI (warp command, beta), Warp agent profiles, Warp Drive (saved prompts, workflows, notebooks, rules), Warp MCP servers, GPT-5, Context7 MCP server, Better Stack MCP server, WezTerm, Ghostty, iTerm, Next.js, OpenCode

## [Gemini 2.0 Flash: Is Google Taking Over Code?](../videos/5Z42W5AK6JU.md)
`5Z42W5AK6JU` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building

Hands-on tutorial that builds small apps with Gemini 2.0 Flash through the Aider and Cline coding agents, with setup steps and a candid note on the output's gaps. Thin on analysis despite its "is Google taking over code" title.

- Techniques: Aider with a Gemini default via .env; Cline on OpenRouter to avoid provider rate limits; Iterative prompting to finish a scaffold
- Tools: Gemini 2.0 Flash, Aider, Cline (formerly Claude Dev), VS Code, OpenRouter, Google AI Studio, shadcn/ui, Claude, GPT-4

## [How To Use Open AI Codex Absolute Beginners](../videos/KpZYZwaHBc0.md)
`KpZYZwaHBc0` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: context-engineering, software-factory

Beginner walkthrough of OpenAI's Codex CLI and cloud agents: approval modes, AGENTS.md, MCP setup, role-specialized agent files, and running background tasks that end in a GitHub PR.

- Techniques: Full Access approval mode for unattended runs; Model selection by task difficulty; Compact to manage context; Generate AGENTS.md with /init; Role-specialized agent files; Build MCP config from a repo-to-text dump; Cloud task per branch with PR handoff; Plan mode before implementation; BMAD-style planning loop
- Tools: Codex CLI, Codex IDE extension, Codex cloud (ChatGPT app), GPT-5, GPT-5 Codex (Low, High), AGENTS.md, config.toml, Claude Code, Claude Desktop, Cursor, ChatGPT, GitHub

## [Generate The PERFECT App UI Every Time with this 2-Step Cursor Guide](../videos/H-ok6Zx9SR8.md)
`H-ok6Zx9SR8` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: vibe-coding-app-building, context-engineering

AI LABS tutorial on generating varied app UI designs inside Cursor with manually invoked rule files, replacing a paid-API design extension, with a Claude Code port and a plain-English method for writing rule files.

- Techniques: Manual-mode Cursor rule files as invocable workflows; Extract a design.json from a reference image; Targeted variation rules (persona, device, geolocation); Infinite-design iteration loop; Fresh chat per generation round; Writing rule files in plain English; Porting a rule to Claude Code custom commands
- Tools: Cursor (rules, agent, .mdc rule files), Super Design Dev (Cursor extension by Jason Zhao), Claude Code (custom commands, parallel agents), Claude 3.5 Sonnet, Anthropic Claude API

## [You Need Claude Sandboxes... 90% Faster AI Coding](../videos/xckU9n9r8Rs.md)
`xckU9n9r8Rs` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: multi-agent, software-factory, context-engineering

Walkthrough of running BMAD-planned stories in parallel with git worktrees and one Claude Code instance per subtask, with a QA agent review loop. The 90% title claim is not backed by the numbers shown.

- Techniques: BMAD planning-first pipeline; Prompt the story generator to split stories into non-conflicting parallel subtasks; One git worktree per subtask, managed through Conductor; QA review then fix loop per story; PR per story, merged by Claude Code
- Tools: BMAD method (planning agents, Scrum Manager, dev and QA agents), Claude Code, Claude Desktop, ChatGPT, Cursor, Conductor (multi-workspace UI for parallel Claude Code runs), git worktrees, GitHub, Next.js (initialized in story 1), OutSkill (sponsor segment, not used in the demo)

## [OpenAI's NEW Cloud-based Software Engineer (Codex)](../videos/nPAXAAbU16w.md)
`nPAXAAbU16w` · Better Stack · 2025-11-02 · q3 · intro · review · also: software-factory, sandboxing-execution

Launch-day walkthrough of OpenAI's cloud Codex agent: parallel tasks in isolated containers, GitHub integration, AGENTS.md, and the codex-1 and codex-mini pricing.

- Techniques: Repo-level agent instructions via AGENTS.md; Configure the agent's dev environment to match local; Turn Ask-mode suggestions into Code tasks; Use a failing agent task as bug triage; Ask for verifiable evidence in every completion
- Tools: Codex (cloud agent, ChatGPT sidebar / chatgpt.com/codex), Codex CLI (mentioned as distinct), ChatGPT, GitHub (repo connection and PR creation), AGENTS.md, codex-1 (o3 variant for SWE), codex-mini-latest, o3 High (comparison baseline), SWE-bench Verified (benchmark cited), Devin (mentioned as competitor), Windsurf (mentioned as recent OpenAI purchase)

## [RAG Just Got Updated…](../videos/EgXOaH-ZqfU.md)
`EgXOaH-ZqfU` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: context-engineering, rag-retrieval, mcp-and-tools

Setup and demo of Archon, a beta self-hosted tool that gives Claude Code or Cursor project docs, a task backlog, and on-demand RAG over crawled docs via MCP. Includes a sponsor segment and an oversold title.

- Techniques: Local Archon stack setup; Project docs and backlog from a feature description; Rules-file-driven on-demand RAG; Crawl vendor docs into a knowledge base
- Tools: Archon, Claude Code, Cursor, Supabase, Docker, Docker Compose, MCP (Model Context Protocol), OpenAI API (embeddings), Google Gemini API (embeddings, free tier), SwiftUI, Xcode, Liquid Glass (Apple UI design)

## [Grok 3 Tested: Did Elon Musk Actually Succeed This Time?](../videos/E4fML4Lghjw.md)
`E4fML4Lghjw` · AI LABS · 2025-11-02 · q2 · intro · review · also: models-research, evals

Hands-on test of xAI's Grok 3 with about 11 quick prompts: strong on word problems and reasoning, failed the constrained haiku and most coding prompts, so the verdict is not for coding tools.

- Techniques: Pass/fail prompt battery for a new model; Letter-constraint instruction test; Copy-paste code check for generated apps
- Tools: Grok 3 (xAI), Grok 3 reasoning mode ('Big Brain'), Grok Deep Search agent, LM Arena (called 'chat arena' in the transcript), Artificial Analysis leaderboard, OpenAI o3 (upcoming, per the host), OpenAI o3-mini, DeepSeek R1, GPT-4o, Claude 3.5 (image and SVG comparison), Cursor, Windsurf

## [Program Claude Code to be your new UI Designer (+ works with any IDE)](../videos/TyGx277x9hQ.md)
`TyGx277x9hQ` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: claude-code, vibe-coding-app-building, context-engineering

Walkthrough of using Claude Code plus ChatGPT planning to turn an HTML UI prototype into a SwiftUI iOS app and re-skin it in Apple's Liquid Glass style; practical but anecdotal.

- Techniques: Plan-in-chat, then execute in agent; Screenshot-to-HTML prototype; Conversion rules file; Style transfer from references; Visual bug reporting; Start from the native project template
- Tools: Claude Code, Claude 4 Sonnet, Claude Opus (Claude 4), Cursor (Max mode), ChatGPT, Xcode, SwiftUI, Swift, Next.js, HTML/CSS, iOS Simulator, Apple Liquid Glass design

## [Building Custom AI Agents Just Got EASIER - Claude Agent SDK](../videos/NsROagHaKxA.md)
`NsROagHaKxA` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: claude-code, agent-architecture, mcp-and-tools

Better Stack walkthrough of the Claude Code SDK (now also called the Agent SDK): a single-prompt query, a streaming-input REPL, replacing the system prompt, and adding a custom MCP tool, all in one short TypeScript file.

- Techniques: One-shot query; Streaming-input REPL; Full system-prompt replacement; Appending to the system prompt; In-process custom MCP tool; Combined demo structure
- Tools: Claude Code SDK (the video also calls it the Claude Agent SDK in its title), Claude Code CLI, Claude Haiku (model option example), TypeScript, zod, MCP (createSdkMcpServer, tool), Bash tool (built-in), Glob tool (built-in)

## [The BEST Way To Start a Project (Better-T-Stack)](../videos/CWwkWJmT_zU.md)
`CWwkWJmT_zU` · Better Stack · 2025-11-02 · q2 · intro · review · also: dev-tools, vibe-coding-app-building

A Better Stack walkthrough of Better-T-Stack, a scaffolder that builds a full TypeScript monorepo (TanStack Router, Hono on Bun, oRPC, Postgres, Drizzle, Better Auth) from one command, with auth working on first run.

- Techniques: Scaffold a full-stack TS monorepo from a builder; Bring up the stack locally; First-run smoke test of the full path; Hand the scaffold to a coding agent
- Tools: Better-T-Stack (scaffolder with website Builder and CLI), TanStack Router, Hono, Bun, oRPC, tRPC (listed as an alternative API layer), PostgreSQL, Docker / Docker Compose, Drizzle ORM, Prisma (listed as an alternative ORM), Better Auth, Turborepo

## [OpenAI Agent Builder vs Claude: Who Wins Multi-Agent Workflows? (Complete Comparison)](../videos/sLiVXlIlSBQ.md)
`sLiVXlIlSBQ` · AI LABS · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, agent-architecture, product-ux

A walkthrough of OpenAI's AgentKit (Agent Builder, ChatKit, widgets), with a Speechmatics sponsor segment up front; practical for seeing the visual workflow and ChatKit setup, thin as a head-to-head comparison.

- Techniques: Classifier-then-route agent workflow; Human approval gate in a workflow; Remote MCP server registration per agent; ChatKit starter quickstart; Theme via Playground, then hand off to a coding agent; Prompt-to-widget, then pin the format in the agent prompt; Custom widgets with Claude Code and agents.md
- Tools: OpenAI Agent Builder, OpenAI AgentKit, OpenAI ChatKit, ChatKit Playground, OpenAI Widget Builder, OpenAI vector store / file search, OpenAI guardrails node, ChatGPT apps, Zapier (MCP servers), Pipedream (MCP servers), n8n (comparison only), Next.js

## [I Built an MCP Server with a Single Prompt!](../videos/yLAmw4oL-6A.md)
`yLAmw4oL-6A` · AI LABS · 2025-11-02 · q2 · intro · review · also: mcp-and-tools

A walkthrough of a hosted prompt-to-MCP-server generator, shown building a weather server and a Figma server, with practical lessons on testing before deploy and wiring the result into Cursor.

- Techniques: Prompt-to-MCP generation with env-var credentials; Test the raw API call before deploying; Declare the plan limits up front; Recover from drift by restarting from the original prompt; Wire a hosted MCP server into Cursor; Split tools by data type; Export and run locally
- Tools: MCP (Model Context Protocol), SSE-based MCP servers, Figma MCP server (get Figma node data tool), OpenWeather API, Cursor, Claude Desktop, Windsurf, mcp.json

## [I Just Saved $1600 With GLM 4.5](../videos/yD4qcd_8o2U.md)
`yD4qcd_8o2U` · AI LABS · 2025-11-02 · q3 · intro · review · also: token-cost-efficiency, models-research

AI LABS walkthrough of ZAI's $3 GLM Coding Lite plan as a cheaper Claude Code backend, with the author's side-by-side UI test and a claim of roughly $1600 saved; the cost case rests on prompt counts and one subjective comparison.

- Techniques: Point Claude Code at GLM via env var override; Same-prompt side-by-side model comparison; Parallel agents in separate git worktrees; HTML-first UI prototyping on a canvas
- Tools: GLM (GLM 4.5 coding plan, ZAI), Claude Code, Cline, superdesign.dev, Conductor, BMAD method, Cursor, Codex, Kimi K2, Lindy Build

## [Claude Code Can Finally Make Beautiful Websites](../videos/idccdssOZQ8.md)
`idccdssOZQ8` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building, product-ux

Three UI design principles (depth through layered color and shadows, box-based responsive layout, and a four-role color palette) for making AI-generated sites look better, shown on a cloned Airbnb-style page.

- Techniques: Color-layer depth instead of borders; Dual shadow with depth levels and a gradient; Flexible box layout with parent-child structure; Priority-based responsiveness; Four-role palette; Prompt per principle, with before/after comparison
- Tools: Claude Code (named in the title only; the transcript does not name it), Colors (palette-browsing site, named in the transcript, no URL given), Airbnb-style page clone (demo subject, not a tool)

## [10 Pro Claude Code Tips & Tricks NO ONE Shares](../videos/Br5Ofobq6Is.md)
`Br5Ofobq6Is` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: claude-code, token-cost-efficiency, dev-tools

A 4-minute Better Stack listicle of ten Claude Code tips: phone notifications via hooks, permission and thinking-budget settings, CLAUDE.md emphasis, session recovery, parallel sessions, and cheaper model use. Quick ideas, few exact configs.

- Techniques: Stop/Notification hook for completion alerts and phone pings; Alias the skip-permissions flag and toggle it off with shift+tab; Deny read access to sensitive files at global or project scope; Thinking budget by keyword in the prompt; CLAUDE.md emphasis, file links and memory; Custom slash commands with chained arguments and nested folders; Session recovery with --continue, --resume and double-escape rewind; Parallel agents on git worktrees with Claude Squad or tmux; Browser access to a terminal with Vibe Tunnel; /clear on topic change plus a cheaper model
- Tools: Claude Code, CLAUDE.md, Claude Squad, tmux, git worktrees, Vibe Tunnel, Kimi K2, BetterStack

## [Warp Terminal: The AI Terminal That Transformed My Workflow...](../videos/C8vL-VKcJgo.md)
`C8vL-VKcJgo` · AI LABS · 2025-11-02 · q2 · intro · review · also: dev-tools

A feature tour of the Warp terminal: natural-language commands with approve-before-run, Ctrl+R and Ctrl+I AI modes, an agent that installs a repo from its README, Warp Drive team sharing, and a WSL route for Windows.

- Techniques: Natural-language command generation with approve-before-run; README-driven repo setup via agent; Environment variable for API keys before launch; Team sharing through Warp Drive; Windows install via WSL
- Tools: Warp (terminal, built-in AI agent, Warp Drive), Aider (transcribed as "Adr"/"AIDR"; a repo the host installs, probably Aider), OpenAI API (key set as an environment variable), WSL (Windows Subsystem for Linux), Debian .deb installer for Warp, Python (the wrong version was caught in the README setup), Windsurf (teased for a later video)

## [I'm Never Vibe Coding Without Next JS Agents Anymore](../videos/yJv2JRM--ws.md)
`yJv2JRM--ws` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools, vibe-coding-app-building

A walkthrough of building a full-stack Next.js agent marketplace with Claude Code and three MCP servers (Supabase, ShadCN, Stripe), driven by a PRD and per-MCP prompts. The reusable parts live in linked resources, not on screen.

- Techniques: One-command MCP wiring with a /mcp health check; PRD to converter prompts, one per MCP; Dependency-ordered single-session build; Component-grounded UI with a theme and a usage slash command; Static UI first, then a separate wiring pass; Mock-then-real payment verification
- Tools: Claude Code, Cursor, Next.js, Supabase (MCP server), ShadCN MCP, shadcn/ui, TweakCN, Stripe (MCP server, Stripe checkout), ChatGPT (used for the PRD brainstorm)

## [This Free Tool Makes Cursor 10x Smarter](../videos/52FC3qObp9E.md)
`52FC3qObp9E` · Better Stack · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, context-engineering

Better Stack demo: Cursor's built-in docs indexing misses newer APIs, so adding "use context7" to a prompt fetches current library docs through an MCP server. Install is a single npx entry.

- Techniques: Install Context7 as a global MCP server in Cursor; Trigger doc retrieval with 'use context7' in the prompt; Manual doc snippet pull without MCP
- Tools: Cursor, Context7 (MCP server, run via npx; maintained by Upstash), Next.js 15.3 (onNavigate handler), Claude 3.5 Sonnet (model used in Cursor), MCP (Model Context Protocol), npx

## [Build FRONTEND Faster Than Ever with This Cursor MCP Setup!](../videos/DpdM4xei5fw.md)
`DpdM4xei5fw` · AI LABS · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, vibe-coding-app-building

A 6-minute walkthrough of the 21st.dev / Magic UI MCP server inside Cursor, showing component generation, logo search and catalog install for frontend work.

- Techniques: Install an MCP UI server into the IDE; Prompt for a self-contained component, then let the IDE agent place it; Use logo search to fill in brand or icon assets; Install a catalog component by copying the command
- Tools: 21st.dev (Magic component builder, logo search, component inspiration, UI catalog), Magic UI, Cursor, Windsurf, Cline (called "Klein" in the auto-captions), VS Code, React, TypeScript, MCP (Model Context Protocol), WSL, v0 (mentioned as the comparison point for the component builder), ChatCN (named by the host as a UI library source; spelling from auto-captions, not verified)

## [Why Every Developer is Switching from Claude to Open Source Kimi K2](../videos/av0Lsz3KkSE.md)
`av0Lsz3KkSE` · Better Stack · 2025-11-02 · q2 · intro · review · also: models-research, token-cost-efficiency

Single-run head-to-head of open-weight Kimi K2 vs Claude Sonnet 4 building the same MP3 transcription app. K2 cost about a third as much and wrote better docs, but took 11+ minutes under server load.

- Techniques: Point Claude Code at an Anthropic-compatible endpoint to try a cheaper model; Same-scaffold A/B test of coding agents; Compute cost from usage when the tool's cost display is wrong; Ask the agent explicitly for run instructions; Feed the real runtime error back to the agent
- Tools: Kimi K2 (Moonshot AI), Claude Sonnet 4, Claude 4 Opus, Claude Code, OpenCode, GPT-4.1, Gemini 2.5 Pro, Gemini CLI, OpenAI Whisper API, Vite, React, Express

## [Agents.md Is HERE… 90% of AI Tools Will Use This Now](../videos/Pmc4OfSlhbE.md)
`Pmc4OfSlhbE` · AI LABS · 2025-11-02 · q2 · intro · news · also: context-engineering, claude-code

Host argues OpenAI's AGENTS.md should become the single cross-tool agent context file, replacing per-tool rules files, and says Claude Code's absence is the gap. Includes a sponsor segment.

- Techniques: Single AGENTS.md as shared project context; Rely on the auto-loaded context file for session bootstrap
- Tools: AGENTS.md, CLAUDE.md, Model Context Protocol (MCP), Figma MCP server, Claude Code, OpenAI Codex, Gemini CLI, Qwen Code, Cursor, Windsurf, Kiro, GitHub Copilot

## [Build ANYTHING with MCP Servers - Coding Tutorial](../videos/sMqlObpNz64.md)
`sMqlObpNz64` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: mcp-and-tools

Builds a TypeScript MCP server wrapping Better Stack's monitors API, then wires it into Cursor and Claude Desktop. Covers tools, resources, prompts, stdio vs SSE, and env-var wrapper scripts.

- Techniques: Minimal TypeScript MCP server skeleton; Register a tool with name, description, zod schema and async callback; Return errors so the model can self-correct; Pick the transport by where the server runs; Cursor setup with an env-var wrapper script; Claude Desktop setup via config file; Static and dynamic resources; Generate the API client from docs with an AI editor
- Tools: Model Context Protocol (MCP) TypeScript SDK (@modelcontextprotocol/sdk), zod, pnpm, shx, Node.js, Cursor, Claude Desktop, Cline (spoken as 'Klein'), Better Stack monitors API, FastMCP (Python wrapper mentioned), Model Context Protocol Python, Java, Kotlin, Rust SDKs (mentioned)

## [Complete Guide to ChatGPT’s Canvas Update  New Tools & Features You Need](../videos/-ajtoeyu4go.md)
`-ajtoeyu4go` · AI LABS · 2024-11-02 · q2 · intro · review · also: product-ux

A roughly 11-minute walkthrough of ChatGPT Canvas, the side-by-side editor for code and writing, covering inline edits, auto-comments, logging, port-to-language, and version navigation. Little hard data; mostly a UI tour.

- Techniques: Iterate in place with Canvas instead of re-prompting; Canvas editor actions for code: review, comments, logs, port; Canvas writing actions: Suggest Edits, reading level, polish, emojis
- Tools: ChatGPT, ChatGPT Canvas, GPT-4 (with Canvas), Python, Pygame, VS Code, C++, SFML

## [Get Started with Cursor: The AI Code Editor That Lets You Build Without Coding](../videos/NtGagWyY1kU.md)
`NtGagWyY1kU` · AI LABS · 2024-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building

A 5-minute beginner walkthrough of the Cursor AI code editor: install, set up, use Ctrl+L chat and Ctrl+K inline edits to generate and modify small Pygame games. Thin, hype-framed, no review of output quality.

- Techniques: Chat-first prototyping of a small game; Inline edit with prompt, Apply, Accept; VS Code migration at setup; Toggle AI features and bring your own model key
- Tools: Cursor, VS Code, Python, Pygame

## [Bolt.new Tutorial Website – Replaces Cursor, Claude & v0 – The Only AI Tool You Need!](../videos/6-sTKmPl4wA.md)
`6-sTKmPl4wA` · AI LABS · 2024-11-02 · q2 · intro · review · also: vibe-coding-app-building

A 7-minute walkthrough of Bolt.new, a browser tool that generates a React website from a text prompt, then iterates on it through chat; the transcript shows real friction (vague prompts, missing images, out-of-credits).

- Techniques: One-prompt scaffold, then chat-driven iteration; Name the exact effect or fix instead of describing a mood; Copy build errors back into the chat; Check generated assets and sections by eye
- Tools: Bolt.new, React, V0, Cursor, Replit (comparison only), Claude (UI resemblance only)

## [I Built an App in 10 Minutes WITHOUT Coding! | Using Cursor Composer](../videos/LrIhNW2BN28.md)
`LrIhNW2BN28` · AI LABS · 2024-11-02 · q2 · intro · review · also: vibe-coding-app-building, context-engineering

Short Cursor promo that builds a budget tracker and a task app from plain-text requirements with Composer; shows multi-file generation, but the evidence is two cherry-picked demos.

- Techniques: Requirements file, then generate; Enable Composer before first use; Generate, then re-prompt for design, then fix bugs; Scope chat with @-references; Ctrl+K for local edits
- Tools: Cursor, Cursor Composer, Cursor Tab (completions), Cursor Chat (@-references), Cursor Ctrl+K inline edit

## [Future of AI security with Michal Pechoucek](../videos/t7iwv_8E9_g.md)
`t7iwv_8E9_g` · Better Stack · 2024-11-02 · q2 · intro · talk · also: security-guardrails

Gen Digital's technology head argues the real AI threats are weaponized attacks, insecure AI-written code, attacks on AI systems, and mostly human-targeted scams, and pitches a free scam-detection app.

- Techniques: Generative-AI scam text classifier; On-device conversational scam check
- Tools: Norton Genie (Gen Digital, free scam-detection app for iPhone and Android), MITRE ATLAS (taxonomy of known attacks on AI systems, transcribed as 'Mitra' / 'Atlas'), Windows 95 (cited as a historical vulnerability event), Copilot-style AI coding assistants (unnamed 'copilots')

