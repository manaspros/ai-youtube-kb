# vibe-coding-app-building — 137 videos

*building apps and sites with AI (Lovable, v0, Bolt, Cursor), no-code, UI/design generation, shipping side projects*

By channel: AI Engineer 19 · AI LABS 76 · Better Stack 42

**Synthesized guide:** [guides/vibe-coding-app-building.md](../guides/vibe-coding-app-building.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [This Open-Source Tool Generates UI Like Magic](../videos/AhVHtwh5k3E.md)
`AhVHtwh5k3E` · Better Stack · 2026-10-23 · q3 · intro · review · also: product-ux

Better Stack demos OpenUI, a spec and streamable language for generative UI, and argues it beats JSON-based UI rendering on tokens and latency. Mostly a demo with unbenchmarked claims.

- Techniques: Line-streamed generative UI DSL; Component allowlist as the UI boundary; On-demand app generation from a title; Pick model by output quality, not raw speed
- Tools: OpenUI, OpenUI Lang, OpenUI Dev React lang package, Gemini 3.8 Flash (as spoken), Cerebras, Qwen 3.8 (as spoken, likely Qwen 3), Vercel JSON Render (auto-caption reads 'Versa'), Google A2UI, ChatGPT intelligent UI (OpenAI), React, Svelte, shadcn/ui

## [AI Security Engineer Foundations + Certificate — Micah Silverman, Snyk](../videos/p-2MT8KYZqU.md)
`p-2MT8KYZqU` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: security-guardrails, mcp-and-tools, governance-compliance

Two-hour Snyk workshop on AI security foundations: OWASP LLM Top 10 risks, shadow AI and AI bills of materials, AI threat modeling, MCP tool poisoning, vibe-coding failures, and a live CTF chatbot exercise.

- Techniques: Layered prompt-injection defense; Keep secrets out of prompts and enforce access outside the model; Scope chatbot data to what may be disclosed; AI threat modeling workflow; Adversarial review of an architecture; AI BOM as a CI gate; Audit MCP configs and servers before enabling; Secure-by-design playbook for agentic coding; Probe a chatbot in a CTF-style sandbox; Offer an approved alternative when restricting a tool
- Tools: Snyk Evo, Snyk Agent Scan, Snyk Code, Snyk (SCA/SAST), OWASP Top 10 for LLM Applications, STRIDE, DREAD, SBOM (SPDX, CycloneDX), CycloneDX (AI/ML BOM support), Model Context Protocol (MCP), Figma Framelink MCP server, OpenClaw

## [Let Anyone at Your Company Ship Internal Apps with AI — Garrett Galow, WorkOS](../videos/HTzgC3FoYsI.md)
`HTzgC3FoYsI` · AI Engineer · 2026-10-09 · q3 · practitioner · talk · also: enterprise-adoption, governance-compliance

WorkOS's Garrett Galow on a CLI, a Cloudflare-based platform and SSO-by-default that let non-engineers build and ship internal apps; 37% of about 60 apps had no engineer commits.

- Techniques: Pre-flight local setup CLI with template scaffolding; SSO gate on every deployed app by default; Platform abstraction over deploy target; Pair non-engineer driver with engineer consultant in timed hackathons; Push-to-register catalog with shared skills
- Tools: Claude Code, Codex, Lovable, Cloudflare Workers, Cloudflare D1, Cloudflare KV, Doppler, Okta, GitHub, Webflow, Slack, Node.js

## [Lovable Rewrote Vite in Rust... (kind of)](../videos/msSZ4CL_sNg.md)
`msSZ4CL_sNg` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: dev-tools, infra-cost-scaling

Better Stack tests Lovable's claim that OJ, a Rust rewrite of Vite's dev server, is 4x lighter and 2x faster to start, finds small gains on a small app and larger gains on a 5000-component app, and summarizes Evan You's critique.

- Techniques: Benchmark a dev server by time-to-deepest-component plus process-tree memory; Check fast refresh state preservation with a counter component; Coalesce agent write bursts into one hot update
- Tools: OJ (Orange Juice, Lovable's Rust dev server), Vite (8.1 per the transcript; Bundle Dev Mode is experimental), Rolldown (VoidZero), Oxc (VoidZero), Rust, React, TanStack Start, Tailwind CSS, esbuild (mentioned, not used), Vite Plugin Checker, Google Chrome (benchmark harness)

## [Why Smart Developers Use Kimi For Design](../videos/zx9xhp7wB9M.md)
`zx9xhp7wB9M` · Better Stack · 2026-10-02 · q2 · intro · review · also: models-research

Better Stack runs one informal side-by-side test of Kimi, Claude and an OpenAI model (Astra) across five design and game tasks, finds each model wins different rounds, and spends $6 on Kimi.

- Techniques: Same-brief, side-by-side model bake-off; Per-task model routing; Round scoring with a tie rule; Visual checks for generated 3D and animation output; Plan for iterative refinement on generic UI
- Tools: Kimi (Kimi K3 mentioned as a separate follow-up video), Claude, Astra (OpenAI model, as named in the transcript), Fable, Design Arena (leaderboard the speaker cites), Postgres (the product in the landing-page demo), npm (install block shown on the landing page)

## [Github #1 Trending Skill's Author Just Fixed Claude's Design Problem](../videos/Ow_z94c3wKk.md)
`Ow_z94c3wKk` · AI LABS · 2026-10-02 · q2 · practitioner · review · also: mcp-and-tools, coding-agents

Walkthrough of Inspo, a free MCP server of 832 captured sites with per-site design.md files that lets coding agents pull real references before designing. Sponsored segment; tested on one demo page.

- Techniques: Pre-build style menu; Reference provenance check; Filter-scoped reference search; Cap reference study depth; Install Inspo in user scope; Split design and animation into separate MCP lookups
- Tools: Inspo (MCP server, free, no account or API key), UI Skills MCP server, Emil Kowalski animation skill, Mengto scroll animation skill (name as transcribed), Hallmark design skill (name as transcribed), AI Labs Pro design system (community resource), Claude Code, Manid (sponsor, agent tools API gateway)

## [Shadcn Just Fixed Tailwind's Biggest Problem](../videos/tPQgw_DPIoM.md)
`tPQgw_DPIoM` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: coding-agents, dev-tools

shadcn's new agent-first linter for Tailwind v4 design systems. It turns design-system rules into lint errors that AI agents can fix against, which the presenter says cut violations to zero in his eight-task test.

- Techniques: Lint the design system instead of prompting it; Use lint messages as the agent's fix instructions; Per-component contracts; Custom messages and a global note; Strict component APIs as a prerequisite
- Tools: shadcn linter (shadcn's new Tailwind design-system linter, no version stated), Oxlint, ESLint, Tailwind CSS v4, shadcn/ui, CVA (class-variance-authority, read by the linter for variant lists), Biome (no plugin yet; open GitHub issue), Starlex (transcribed name; presenter cites it as the alternative people switch to)

## [How To Use Claude Code To Build Amazing Sites With Opus 5.5](../videos/DP7mgLUKN_U.md)
`DP7mgLUKN_U` · AI LABS · 2026-10-02 · q3 · intro · tutorial · also: claude-code, pr-code-review, context-engineering

Six-stage tutorial for building non-generic websites with Claude Code: plan mode, CLAUDE.md business context, a design-rules skill, design.md, git/GitHub/Vercel deployment, branch + PR review, and a 3D scroll skill.

- Techniques: Plan mode before building; Enrich CLAUDE.md with business context; Install and apply a design-rules skill to an existing project; Lock visual style with design.md; Commit checkpoints and set up GitHub via the CLI; Deploy from GitHub to Vercel; Feature branch, PR, and automated review loop; Scroll-driven 3D site via ScrollWorld skill
- Tools: Claude Code, Opus 5.5, Sonnet, Fable, Warp, VS Code, Next.js, Vercel, Vercel CLI, GitHub, GitHub CLI (gh), CodeRabbit

## [The Design-Code Roundtrip That Isn't — Jonathan Gordon, ReWeaver AI](../videos/NW-jwOVr32w.md)
`NW-jwOVr32w` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: product-ux, governance-compliance

Jonathan Gordon (ReWeaver AI) argues a lossless design-code round trip is not yet solved and proposes deterministic guardrails plus provenance to control drift around LLM-generated UI code.

- Techniques: Design-system extraction from code into the design canvas; Joint drift report across code and design; Deterministic guardrails around LLM generation; Fidelity metric per iteration (production drift ratio); Undo and review loop for AI code edits
- Tools: Figma, Sketch, Cursor, Claude Code, ReWeaver

## [Generative UI... in Python? — Jeremiah Lowin, Prefect](../videos/Krzs8GeiWTc.md)
`Krzs8GeiWTc` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: mcp-and-tools, product-ux

Jeremiah Lowin (Prefect) on Prefab, a Python DSL for composing MCP App UIs; the talk argues scoping UIs to pre-built components makes Python-only front ends viable and that streaming compact Python beats streaming JSON.

- Techniques: Return a UI component from a tool; Reactive bindings for client-side interactivity; App class with app.ui and app.tools; Agent-bypass upload via MCP app; Stream generative UI as code
- Tools: Prefab, FastMCP, MCP Apps, React, shadcn/ui, Goose

## [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../videos/mJqwmmOx4WA.md)
`mJqwmmOx4WA` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: governance-compliance, coding-agents, product-ux

Andrew Garvin (Metronome, now part of Stripe) live-demos using Stripe Projects and a Metronome billing agent to build a usage-based billing setup from one natural-language prompt, arguing for sandboxed agent-built billing and for usage or credit pricing when agents are the users.

- Techniques: Portable skills files as agent context for a complex API; Verbose, machine-readable errors for agent self-correction; Sandbox-first agent-built billing with synthetic usage; Natural-language provisioning through a CLI orchestrator; Classify agent roles before designing pricing
- Tools: Stripe Projects, Stripe CLI, Metronome, Claude (selected as the coding agent in the demo), Vercel, Postgres, skills files

## [The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu](../videos/VBCDhRrvlYo.md)
`VBCDhRrvlYo` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: agent-architecture, product-ux, context-engineering

Arturo Nunez (ex-Unity, MongoDB) pitches Nereu, a tag-driven, describe-it-to-build game engine where an AI assistant (Bibi) edits scenes via an Asset Tag System, so creators never touch engine vocabulary or code.

- Techniques: Entity tags as an intent layer over ECS; LLM-as-editor with a tool-only interface; Level-of-detail context assembly; Vision-model asset captioning; Domain expert in the loop while building with a coding agent
- Tools: Claude Code, Unity, Unreal, vision model

## [While my guitar gently speaks — Todd Fisher, Philo Ventures](../videos/E_Txocq-Lrw.md)
`E_Txocq-Lrw` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: voice-multimodal, product-ux

A guitar that speaks and sings: pitch detection, word slicing, vocoder synthesis and a local Whisper-to-LLM loop. Mainly a call to build passion projects with AI.

- Techniques: Energy-gap plus sonority-peak word segmentation; YIN pitch detection to synthesized tone to vocoder; Pre-bake heavy DSP, then map to controls; Local voice loop: STT, then local LLM, then TTS; Plugin packaging inside a DAW
- Tools: JUCE, Logic Pro, Piper TTS, Whisper, YIN pitch algorithm, WORLD vocoder/pitch-shift, VocalSet, Apple built-in TTS

## [The Missing Layer: Design Taste in AI Agents — Hassan El Mghari, Together AI](../videos/7GMKdpLsxwU.md)
`7GMKdpLsxwU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: product-ux, context-engineering, coding-agents

Hassan El Mghari (Together AI) on getting AI-built UIs out of "AI slop": codify the tells as anti-patterns, feed in references, iterate with a cheaper model.

- Techniques: Slop-gate anti-pattern list in a design skill; Theme library as inspiration; Screenshot inspiration vault; Two-tier model routing for UI work; agents.md as a taste log; Batched feature prompting
- Tools: Codex, Claude Code, Cursor, Hallmark, agents.md, GLM 5.2, Opus 4.8, Composer 2.5, Together AI

## [Training Taste — Thais Castello Branco, Taste Labs](../videos/sDMGWK4wZ_w.md)
`sDMGWK4wZ_w` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: evals, product-ux, context-engineering

Thais Castello Branco (Taste Labs) on measuring and fighting "AI slop" in design: decompose subjective quality into checkable parts, build feature classifiers that flag slop, and turn a brand into structured context the agent both follows and is graded against.

- Techniques: Decompose subjective quality into probes; Split objective checks from aesthetic judgment; Rule-aware intentional divergence; Brand spec as both generation context and rubric; Retrieve pre-built brand systems
- Tools: Claude Design, Wayback Machine-style web crawl

## [Design at the Speed of Adjectives — Paul Bakaus, Renaissance Geek, Inc.](../videos/v42opQpCy60.md)
`v42opQpCy60` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: product-ux, coding-agents, context-engineering

Paul Bakaus on steering coding agents toward good design with a skill (Impeccable) that maps vague design adjectives like "bolder" to project-specific meanings, keeping humans in the loop instead of one-shotting.

- Techniques: Project-defined verb and adjective commands; Self-check against a stated failure test; Pre-brief questions before generation; Workflow-stage command mapping; Community-tested experimental commands
- Tools: Impeccable, Claude Code, GitHub Copilot, Cursor, Codex, Figma, Webflow, Claude Design, Radiant Shaders

## [Fable 5.1 is here, and its REALLY good](../videos/0lBvjhcRqyU.md)
`0lBvjhcRqyU` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: models-research, token-cost-efficiency, coding-agents

Better Stack's hands-on review of Fable 5.1: a pricing and benchmark rundown, then five one-shot builds (F1 browser game, tennis-club site) comparing cost, time and tokens against Fable 5, GPT 5.6 Sol, Grok 4.6 and Kimi K3.

- Techniques: Pick effort level by cost per task, not per token; Same prompt, single-file runnable artifact, measure time/cost/tokens; Use the same effort level across models before comparing
- Tools: Fable 5.1, Fable 5, Mythos 5.1, Opus 5, GPT 5.6 Sol, GPT Image 2, Grok 4.6, Kimi K3, Three.js, Artificial Analysis Intelligence Index, Cursor bench, Terminal Bench Science

## [How To Use Claude Design To Build Beautiful Sites](../videos/bBlY5YOsKN8.md)
`bBlY5YOsKN8` · AI LABS · 2026-09-02 · q3 · practitioner · tutorial · also: coding-agents, context-engineering, skills-self-improvement

A five-stage workflow for building a site with Claude Design: write a design.md brand file first, build a design system from it, wireframe, produce the full design, then hand off to Claude Code with a Supabase backend.

- Techniques: design.md-first planning skill; Preview design.md outside the token-metered tool; Design system from design.md; Wireframe, then batched comments; Full design from a chosen wireframe; Claude Design to Claude Code handoff; Post-build design.md conformance review; Supabase skill install and MCP connection
- Tools: Claude Design, Claude Code, Opus 5, Opus 4.7, Haiku, Fable, design.md (Google format), Supabase, Supabase agent skills (general and best-practices), Supabase MCP, Supabase CLI, VS Code

## [Ox Alpha – Use This While It's FREE (Stealth Model)](../videos/hKEdP8nz_w0.md)
`hKEdP8nz_w0` · Better Stack · 2026-09-02 · q2 · practitioner · review · also: models-research, token-cost-efficiency

Better Stack runs one full-stack app prompt through a free stealth model, OxAlpha, and rival models, then argues from code fingerprints that it is likely based on GLM 5.3.

- Techniques: Same-prompt full-stack bake-off; Stack fingerprinting for model attribution; Community fingerprint cross-checks; Rerun the full benchmark before trusting a launch claim; Check retention terms before using free endpoints
- Tools: OxAlpha (stealth model, as named in the video), OpenRouter, OpenCode, Kilo (captioned as 'Klein'), Next.js, Drizzle ORM, better-sqlite3 (captioned as 'Better SQLite'), Express, Node SQLite, React, Claude (used to compare codebases), DeepSeek V4 Pro

## [Gadgets: Personal app vibe coding that is actually safe — Kenton Varda, Cloudflare](../videos/RmS5s6Wbin4.md)
`RmS5s6Wbin4` · AI Engineer · 2026-08-18 · q3 · practitioner · demo · also: sandboxing-execution, security-guardrails, product-ux

Kenton Varda (Cloudflare) argues personal AI codegen needs new infrastructure, and demos "Gadgets": per-user apps with platform-enforced sharing and sandboxed generated code, run on open-source workerd.

- Techniques: Platform-enforced sharing via single-purpose instances; Sandboxed generated UI with postMessage-only RPC; Give the agent the app source and a brief, let it add primitives; Export code-only templates (blueprints); Run the production runtime locally
- Tools: Cloudflare Workers, Durable Objects, Dynamic Workers, workerd, Claude, Cap'n Web RPC

## [This component library is mind-blowing (Canvas UI)](../videos/JZf_m_BVDaQ.md)
`JZf_m_BVDaQ` · Better Stack · 2026-08-02 · q3 · intro · review · also: dev-tools, voice-multimodal

Better Stack walkthrough of Canvas UI, an open-source, shadcn-installable library of 33 WebGL and HTML-in-Canvas effects, plus using those effects on code-generated video through HyperFrames.

- Techniques: Install a Canvas UI component with the shadcn CLI; Progressive enhancement for HTML-in-Canvas effects; Test HTML-in-Canvas in Chrome with the feature flag; Apply shader-style effects to generated video with an agent; Match effects to the UX intent
- Tools: Canvas UI, shadcn (CLI), Three.js, HTML-in-Canvas (WICG proposal, browser API), drawElementImage, TextElementImage2D (WebGL), CopyElementImageToTexture (WebGPU), Chrome (feature flag), Firefox, Claude, HyperFrames, Remotion

## [How To Use Codex To Build Insanely Beautiful Websites Using GPT 5.6 Sol](../videos/pHstb0JGGhE.md)
`pHstb0JGGhE` · AI LABS · 2026-08-02 · q3 · practitioner · tutorial · also: coding-agents, context-engineering, skills-self-improvement

Seven-stage tutorial for building a non-generic landing page with the Codex app and GPT 5.6, using AGENTS.md, a design skill, a design.md brand file, generated images, and a deploy step. Main lesson: encode taste and brand in files, not in each prompt.

- Techniques: Scoped seed prompt; AGENTS.md via /init, plus a self-verify rule; Install a design skill and forbid the default one; Browser verification loop; design.md brand system; Plan-mode image generation into an assets folder; Screenshot-based layout cloning; Single-section component swap; Performance pass; Local commits as checkpoints; Deploy with the site skill
- Tools: Codex (in the ChatGPT app), GPT 5.6, GPT image model, Next.js, AGENTS.md, GPT Taste skill, OpenAI site skill, Anthropic front-end design skill, design.md (format introduced by Google through Stitch), Aura Build design.md library, 21.dev, Godly components

## [Meta Just Open Sourced 8 Years of Ul Components (Astryx)](../videos/4GaR7k9VMp4.md)
`4GaR7k9VMp4` · Better Stack · 2026-08-02 · q2 · intro · review · also: dev-tools, context-engineering

Walkthrough of Meta's open-source Astryx React component library (built on StyleX): theming via tokens, component-level overrides, Tailwind bridge, and an AI-oriented CLI.

- Techniques: Theme from one brand color plus scale settings; Override a token per light/dark mode; Component-scoped override by variant; Custom component variant; One-off style override with xstyle; Tailwind bridge; Feed component docs to agents with the Astryx CLI
- Tools: Astryx (Meta component library; transcribed as 'Asterix'), StyleX (styling library Astryx is built on; transcribed as 'Starlex'), React, shadcn/ui (transcribed as 'ShadCN'), Tailwind CSS, Material UI, Panda CSS (transcribed as 'panda'), Next.js, Inter (transcribed as 'into'), AGENTS.md, TypeScript

## [Facebook's Release Just Gave Claude Code A New Design System](../videos/-HEdqzzYKco.md)
`-HEdqzzYKco` · AI LABS · 2026-08-02 · q2 · practitioner · review · also: claude-code, context-engineering, skills-self-improvement

Walkthrough of Meta's open-source React/StyleX component library (transcribed as "Asterix"), built to be read by coding agents via a CLI, plus a sponsor read and a plug for the presenter's skills.

- Techniques: Install the design system with the package manager; Run the init command to write agent instructions; Prompt for a whole site and let the agent pull from the CLI; Generate a manifest of CLI commands and flags for grounding; Screenshot and fix loop in headless Chrome; Chain a generic anti-slop review skill after the build
- Tools: Asterix (Meta's design system, transcript name; likely a caption misspelling), React, StyleX, shadcn/ui (transcribed as ShadCN), Next.js (App Router and Pages Router), npm, Claude Code, CLAUDE.md, AGENTS.md, globals.css, headless Chrome, AI Slop Detector skill (presenter's AI Labs design system)

## [This Skill Just Made Kimi K3 a 10X Better Designer](../videos/EwTOiqWWqEc.md)
`EwTOiqWWqEc` · AI LABS · 2026-08-02 · q2 · practitioner · review · also: claude-code, skills-self-improvement, coding-agents

Walkthrough of running Kimi K3 inside Claude Code via a local proxy on a Kimi subscription, then using the Hallmark anti-slop design skill to push Kimi, Opus and Codex off their default visual styles.

- Techniques: Run a non-Claude model inside Claude Code via a local subscription proxy; Install Hallmark for the right agent; Invoke a skill manually with its slash command when the model is not Claude; Prompt Hallmark with the three pre-flight answers; Run the audit verb, then pick which findings to fix; Use the study verb, not a clone request; Manage context manually on long design sessions
- Tools: Kimi K3, Kimi Code, Claude Code, Codex, Codex app, CLIProxy API, Hallmark, Next.js, Opus 4.8, Sonnet 4.5, GPT 5.6, Fable 5

## [500 people vibe-coded for 30 days. I was one of them. - Sanja Grbic, Automattic](../videos/UcYoMg-8-L8.md)
`UcYoMg-8-L8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: enterprise-adoption, product-ux, coding-agents

Automattic's 30-day "Radical Speed Month" experiment, in which about 500 people in paired teams shipped roughly 794 projects, and how the speaker moved from designer to design engineer by prototyping in code before Figma.

- Techniques: Time-boxed paired ship sprint; Prototype-in-code before design tool; Shared file-based exploration log; Aggregating scattered sources into a status tracker; Engineer as enabler in mixed-skill pairs
- Tools: Claude Code, Figma, Storybook, GitHub, Nano Banana, Context MCP server, WordPress.com, Jetpack, WooCommerce

## [HTML is All You Need (for Agents to Make Graphics) - Amol Kapoor, Nori](../videos/JRTAtZ5iBkU.md)
`JRTAtZ5iBkU` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: product-ux, coding-agents

Amol Kapoor (Nori) argues agents fail at graphics because of the medium, not the model, and that HTML is a better authoring format than canvas tools or SVG for slides, docs and video.

- Techniques: HTML as the agent's authoring format for visual artifacts; Pick the format the model is strongest in, separate from the delivery format; Ground the artifact in source data, not in the layout; Avoid screenshot-and-replace loops and canvas-driving tools for agents
- Tools: HTML, CSS, SVG, Figma MCP, PowerPoint CLI, PDF export, Nori Sessions

## [Imagination Engineering: "Live in the future and then build what's missing."](../videos/Z2Erdirpudo.md)
`Z2Erdirpudo` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: product-ux, context-engineering

A YC design lead shows "software on demand" built from a week of public stream-of-consciousness Slack posts, plus a one-morning personal tool, and argues idea generation is the new bottleneck.

- Techniques: Public thought log as agent input; Distil a voice file from public writing; Self-updating design language; Agent-readable glossary markdown; Checklist-driven completeness; Timeboxing with a timer
- Tools: Claude / Claude Code, Opus 4.8, Fable 5, Conductor, Slack, Paper (design tool), ChatGPT (used to make the header image)

## [Think You Can Build a Game with AI? Think Again! - Danielle An & David Hoe, Meta](../videos/grdoOC1BT1s.md)
`grdoOC1BT1s` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: product-ux, multi-agent

Two Meta game-creation leads argue that AI prompting makes basic games easy, so taste, art cohesion, playtesting and runtime-LLM NPCs decide quality, with undeterminism as the open engineering problem.

- Techniques: Key-art anchoring for image generation; Personality-driven LLM NPCs in a shared game loop; Parallel AI-assisted production with frequent playtests; Runtime LLM game master for per-player adjustment
- Tools: Gemini, Nano Banana, Meshy, Manus, Labubu (demo subject)

## [4 Ways to Actually Build Stunning Websites with Claude Code](../videos/HqD5a2Cae60.md)
`HqD5a2Cae60` · AI LABS · 2026-07-02 · q3 · practitioner · tutorial · also: claude-code, skills-self-improvement, context-engineering

AI LABS walks through four ways to get better websites and UIs from Claude Code: refresh design skills from model prompting guides, use design.md files, plan functional UIs as HTML mockups, and clone existing UIs. Mostly anecdotal, with a sponsor segment.

- Techniques: Refresh a design skill from the model's prompting guide; Mine older prompting guides for dropped fixes; Set effort by task type; Conditionally load a sub-skill from a rule; Apply design.md after generation for marketing pages; Functional UI pipeline: plan, mockups, gallery, port; Consistent variants via a shared design.md; CLAUDE.md as product context and verify contract; Verify with a sub-agent against design.md; Clone a marketing site with a capture CLI and sitemap; Clone an auth-gated app from screenshots
- Tools: Claude Code, Claude, Fable 5, Opus 4.8, Anthropic front-end design skill, design.md, GetDesign.md, GSAP, Single File CLI (as named in the video), sitemap.xml, HTML, CLAUDE.md

## [3,000+ Tokens Per Second? Let's Stress Test Xiaomi's New Model: MiMo V2.5 Pro UltraSpeed](../videos/HfRVXadseCo.md)
`HfRVXadseCo` · Better Stack · 2026-07-02 · q3 · intro · review · also: inference-serving, models-research

Better Stack stress-tests Xiaomi's MiMo V2.5 Pro UltraSpeed, claimed at 1000+ tok/s on a 1T MoE from one 8-GPU server; peaks near 3451 tok/s, with broken or frozen app outputs.

- Techniques: Precision exceptions with quantization-aware training for large MoE weights; Block-parallel drafting for speculative decoding (DFlash); Persistent kernel with warp specialization; Fixed-prompt generation speed and output sweep
- Tools: MiMo V2.5 Pro UltraSpeed (Xiaomi model; the speaker says 'Ultra Speed'), TileRT (systems partner, persistent-kernel engine), MXFP4 (4-bit weight format), QAT (quantization-aware training), DFlash (block-parallel speculative drafting), Three.js (used for the Subway Surfers clone), LeetCode (source of the hard algorithm test), GPT 5.5 (comparison only), Claude 4 Opus (comparison only), Diffusion Gemma (earlier Better Stack video referenced, not used)

## [How Lovable self-improves every hour — Benjamin Verbeek, Lovable](../videos/KA5kPbdkK2E.md)
`KA5kPbdkK2E` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: skills-self-improvement, evals, observability

Benjamin Verbeek (Lovable) on two continuous-learning loops: a self-updating "Stack Overflow" of fixes for stuck users, and an agent "vent" tool that reports platform friction to engineers.

- Techniques: Stuck-session detection with an LLM judge; Clustered, generalised fix knowledge bank; Blank-injection holdout; Tuned agent vent tool; Agent triage of agent feedback; Feedback volume as an incident detector
- Tools: Slack, Framer Motion

## [Prompt to Pipeline: Building with Google's Gen Media Stack — Paige & Guillaume, Google DeepMind](../videos/ns9f1fjLD7Y.md)
`ns9f1fjLD7Y` · AI Engineer · 2026-06-18 · q3 · practitioner · workshop · also: models-research, voice-multimodal, coding-agents

Google DeepMind's Paige and Guillaume, with Gemma's Ian Ballantyne, demo AI Studio, Gen Media models and local Gemma 4 agents. Mostly a live product tour, with some practical prompting and cost tips.

- Techniques: Playground-to-code export; Code execution for verified counting and drawing; Per-scene reference injection for character consistency; Structured outputs as a prompt-writing stage; Prompt-level multi-voice TTS; Flex and priority service tiers; Local orchestrator with parallel subagents on an OpenAI-compatible server; Vibe-coding guardrails: one file per feature, plus logging
- Tools: Google AI Studio, Gemini API, Gemini Live, Google Build (AI Studio), Firestore, Google Search grounding, Antigravity, Nano Banana 2, Veo 3.1 Lite, Lyria 3, Lyria RealTime, Genie 3 / Project Genie

## [How to talk to statues — Joe Reeve, ElevenLabs](../videos/u-rJwPPU3QA.md)
`u-rJwPPU3QA` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: voice-multimodal, product-ux

ElevenLabs growth lead on the viral "Statue" app, built in two hours, and on voice-agent UX. Main points: glue code and storytelling matter most, and voice agents need visual co-presence and interruptible, editable transcripts.

- Techniques: Research-to-persona-to-agent chain; Thin glue layer on managed APIs; Playback-position transcript truncation for barge-in; Visual side panel for voice conversations; Hook-first short video with late music
- Tools: ElevenLabs Agents, ElevenLabs Voice Design API, ElevenLabs music generation, OpenAI deep research, Cursor, Supabase, Facebook Instant Games API (deprecated), CapCut, Claude app voice UI, OpenClaw

## [I Didn't Know You Could Use Claude Code Like This](../videos/KQDVDtklf34.md)
`KQDVDtklf34` · AI LABS · 2026-06-02 · q2 · intro · tutorial · also: claude-code, context-engineering

Shows non-coding uses of Claude Code (second brain in Obsidian, Remotion video, grounded research pipeline, Canvas design skill, Claude Video watch skill, NotebookLM/Notion ops, role-based finance/teacher/legal setups) mostly as sponsored, shallow tutorials.

- Techniques: CLAUDE.md priority-tiered instructions for a non-code knowledge base; Remotion skill install and plan-first video generation; Step-file research pipeline with verification and cited output; Claude Video skill setup for watching videos; Canvas design skill workflow for posters and infographics; Local Claude Code over NotebookLM CLI and Notion MCP for content systems
- Tools: Claude Code, Claude.md, Obsidian, Remotion, Remotion skill, Anthropic Canvas design skill, Claude Video (watch skill), Groq, SERP API, Google Gemini, NotebookLM CLI, Notion MCP

## [MCP Apps Are Changing the Internet. Here’s How to Build One! (Skybridge)](../videos/9X8GRGcl5oA.md)
`9X8GRGcl5oA` · Better Stack · 2026-06-02 · q3 · intro · tutorial · also: mcp-and-tools, coding-agents

Better Stack walkthrough of Alpic's SkyBridge 1.0, a TypeScript/React framework for building MCP apps (interactive widgets inside chatbots), shown by building and testing a camera-lens store app with its local dev dashboard, tunnel and Beacon Audit.

- Techniques: Install the SkyBridge skill into the repo, then prompt the agent to build the app; Test tools and widget state in the SkyBridge dashboard before involving a chatbot; Expose a local MCP server with the dashboard tunnel and attach it as a Claude custom connector; Run Beacon Audit before submitting to an app store
- Tools: SkyBridge 1.0 (Alpic, open-source TypeScript framework for MCP apps), Alpic Playground (sandbox inside the SkyBridge dashboard), Beacon Audit (SkyBridge app audit tool), React, TypeScript, Claude (builds the app and hosts the custom connector; the transcript does not name the surface used for generation), ChatGPT (developer settings used for testing the tunnel URL), Skybridge agent skill (installed into the repo's .agents directory)

## [3 Design Levels For a Free Claude Code Boost (People Stop At Level 1)](../videos/5lycYTOYbPM.md)
`5lycYTOYbPM` · AI LABS · 2026-06-02 · q3 · practitioner · tutorial · also: claude-code, context-engineering, testing-verification

Three levels of getting non-generic UI from Claude Code: a structured single-page design prompt, a CLAUDE.md plus design.md system for cross-page consistency, and design tests written before the code, including visual TDD with Visly.

- Techniques: Structured single-page design prompt; CLAUDE.md for project context, design.md for the visual system; Lint design.md against Google's open template; Install an external design-principles audit skill per project; Derive design tests from design.md before writing UI code; Visly local visual TDD loop
- Tools: Claude Code, Claude Opus 4.7 (model named in the video), CLAUDE.md, design.md, OKLCH, Google design.md template (open-sourced), Versalab design-audit skill, Playwright, Visly CLI (transcribed as 'Visly Test' and 'Visley'), Zilliz Cloud (sponsor), Inter (named as banned font), Geist (named as banned font)

## [Open Design: Why 40k Developers Abandoned Claude Design](../videos/B3coWv2ZV68.md)
`B3coWv2ZV68` · Better Stack · 2026-06-02 · q3 · intro · review · also: coding-agents, product-ux

Walkthrough of OpenDesign, an open-source, local alternative to Anthropic's Claude Design that generates HTML prototypes and slides on top of whichever coding agent is installed; the speaker argues design systems plus per-output skills drive quality more than the model.

- Techniques: Run OpenDesign from source; Harness and model selection per project; Seed a design from a live URL; Pick a design system before prompting; Finalize, export and hand off; Iterate with follow-up prompts
- Tools: OpenDesign (open-source Claude Design alternative, Nexa team), Claude Design (Anthropic, proprietary, cloud-only, $20/month per the speaker), Claude Code, Claude Opus 4.7 (speaker's claim that it is strong at front-end design), Codex, OpenCode, GLM 5.1 (used as the generation model), GPT-Image2 (OpenAI image model, default image provider via OpenAI key), ElevenLabs (TTS and sound effects, optional), agent-browser (browser tool the agent used), Chrome (opened via curl by the agent), Docker (optional install path)

## [Claude Code Just Killed Every Shopify Agency Ever](../videos/x2pRavsHdls.md)
`x2pRavsHdls` · AI LABS · 2026-06-02 · q2 · practitioner · tutorial · also: coding-agents, claude-code, context-engineering

A walkthrough for building and syncing a Shopify storefront with Claude Code, using the Shopify CLI, AI toolkit MCP, HTML prototype skill, Gemini image skill and settings.json hooks. Quality is capped by a sponsor segment and a thin, hype-titled setup guide.

- Techniques: Two-phase skill: HTML preview, then apply; Image generation through a CLI skill; Pre-tool-use hook as an approval gate; Shopify project bootstrap; Admin API auth with incremental scopes
- Tools: Shopify Partner account, Shopify CLI (React app template, TypeScript), Shopify AI toolkit (MCP), Shopify plugin (agents and skills), Shopify Admin API, Claude Code, CLAUDE.md, Gemini CLI (image generation), settings.json hooks, Willow Voice (sponsor segment, not a tool used in the setup)

## [Your AI UI Looks Generic… This Fixes It (DESIGN.md)](../videos/pY52H5gKhGg.md)
`pY52H5gKhGg` · Better Stack · 2026-06-02 · q2 · intro · review · also: context-engineering, coding-agents

Google's open-sourced DESIGN.md: a repo-root markdown file of design tokens plus intent prose that keeps AI-generated UI from looking generic. Practical but thin.

- Techniques: Repo-root DESIGN.md with tokens then intent; Fixed-prompt A/B for design context; Start from a community template, then customize; Write the design rules once, not in every prompt
- Tools: DESIGN.md (Google open-source format), Cursor, Claude Code (transcribed as 'Cloud Code'), v0, Figma, CLAUDE.md, Cursor rules, Tailwind (default styling referenced in demo)

## [Why I’m Switching To Powabase for My AI Apps](../videos/wC2QpP_A9-Y.md)
`wC2QpP_A9-Y` · Better Stack · 2026-06-02 · q2 · intro · review · also: rag-retrieval, coding-agents

Better Stack tests PowerBase, a hosted backend bundling Postgres, pgvector RAG and an agent workflow builder, by having Claude Code build a RAG chatbot over an 80s hardware catalog. One demo, no measurements.

- Techniques: Agent-driven backend setup from docs and credentials; Single-Postgres RAG with pgvector; Ingest an existing OCR text export for RAG; Corpus-bounded answers with a missing-item probe; Node-based guardrails around LLM tool use; Review the session run log
- Tools: PowerBase (powerbase.ai), Supabase, PostgreSQL, pgvector, Claude Code

## [Vercel Just Killed Electron With Zig](../videos/GXNjnu7UqFs.md)
`GXNjnu7UqFs` · Better Stack · 2026-06-02 · q2 · intro · review · also: dev-tools

Walkthrough of zero-native, a thin Zig shell that hosts a system WebView for small desktop apps, covering setup, dev loop, 2.9 MB packaging, Electrobun comparison and limits.

- Techniques: Scaffold a zero-native app; Dev loop and packaging; Add zero-native to an existing JS project; Configure the app via app.zon; Call native or C code from the frontend
- Tools: zero-native (CLI and build via zig build), Zig, mise, Homebrew, Vite, React, Svelte, Vue, Next.js, Electron, Electrobun, Bun

## [Build & deploy AI-powered apps — Paige Bailey, Google DeepMind](../videos/G_bHFmEAarM.md)
`G_bHFmEAarM` · AI Engineer · 2026-05-18 · q2 · intro · demo · also: models-research, product-ux

Paige Bailey (Google DeepMind) gives a demo-heavy tour of Gemini models, AI Studio tools (grounding, URL context, code execution), Build for prompt-to-app, Genie 3, Veo 3.1 Lite, Gemma 4 and Gemini Live.

- Techniques: Clip video by time and frame rate; Let code execution do the exact work; URL context as lightweight grounding; Per-task thinking level; Prompt expansion before generation; Plan with a big model, act with a local model; Compare mode for model choice; Export UI experiments to code; System instructions for voice output style
- Tools: Google AI Studio, Gemini API, Gemini Live, Gemini 3.1 Pro, Gemini 3.1 Flash, Gemini 3.1 Flash-Lite, Google Search grounding, URL context, code execution, Build (AI Studio app builder), Firebase / Firestore, Cloud Run

## [HTML In Canvas Is Wild And I Love It](../videos/1zfRSiZBLyQ.md)
`1zfRSiZBLyQ` · Better Stack · 2026-05-02 · q3 · intro · tutorial · also: dev-tools

Better Stack demo of HTML in Canvas, an experimental proposal that lets live DOM elements render into WebGL or 2D canvases, with the basic setup steps and its drawbacks.

- Techniques: Render live DOM into a WebGL scene as a texture; 2D canvas: draw a DOM element directly; Custom input with a DOM element behind a canvas skin
- Tools: HTML in Canvas (browser proposal), Chrome Canary (experiment behind a flag), three.js, WebGL, WebGPU, Canvas 2D context drawElementImage, requestAnimationFrame

## [8 Vibe Coded Apps That Generated Millions Overnight](../videos/zNOunnM1jTs.md)
`zNOunnM1jTs` · AI LABS · 2026-05-02 · q2 · intro · other · also: product-ux, coding-agents

Anecdotal roundup of eight solo, vibe-coded apps with self-reported revenue; the useful part is a few habits (small prompts, outsourced dependencies, defining an ICP first), not the numbers.

- Techniques: Incremental, chunked prompting; Minimal correct context; Model fallback chain; Design first, then modular build; Template-guided UI generation; Stack choice for AI tools; Outsource commodity operations; Real-time multiplayer transport; Define the ICP before the build
- Tools: Claude, Claude Code, Cursor, ChatGPT, Grok, Grok 3, Claude Sonnet 3.7, Gemini, GPT, Midjourney, ElevenLabs, Next.js

## [Opus 4.7 Is GREAT (except the token usage)](../videos/KZCKfhjMuOQ.md)
`KZCKfhjMuOQ` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: models-research, token-cost-efficiency, coding-agents

Hands-on review of Claude Opus 4.7: better coding and UI, but a new tokenizer and higher default effort can burn up to 35% more tokens. Tested via single-prompt cafe site and finance dashboard builds against Opus 4.6, Gemini 3.1 and GPT 5.4.

- Techniques: Effort-level sweep before changing defaults; Same-prompt model bake-off; Re-audit old prompts after a model upgrade; Check the stack and persistence explicitly in app-generation prompts
- Tools: Claude Opus 4.7, Claude Opus 4.6, Claude Code, Gemini 3.1, GPT 5.4, Codex, Mythos (unreleased Anthropic model, mentioned only), Design Arena, Unsplash, React, Vite, React Router

## [This Open-Source Tool Might Fix Design Handoff Forever (PenPot)](../videos/9AGrepjrbqY.md)
`9AGrepjrbqY` · Better Stack · 2026-05-02 · q2 · intro · review · also: dev-tools

Better Stack walkthrough of Penpot, an open-source browser design tool whose output is real SVG/CSS, pitched as a Figma alternative that reduces design-to-code handoff; self-hosting via Docker is shown.

- Techniques: Self-host Penpot with Docker Compose; Design in flex layout so the inspect CSS maps to code; Use inspect mode for handoff instead of a dev-mode plugin
- Tools: Penpot, Figma, Sketch, Docker, Docker Compose, SVG, CSS, Flexbox, CSS Grid, HTML

## [How to Use Google Stitch to Make Sites 10X More Beautiful](../videos/b0lwCDNOFUY.md)
`b0lwCDNOFUY` · AI LABS · 2026-04-02 · q2 · practitioner · tutorial · also: coding-agents, context-engineering, skills-self-improvement

Tutorial on pairing Google Stitch with Claude Code: design.md design systems, screenshot-based redesign, Stitch skills and MCP, then React and shadcn conversion. Includes sponsor segments.

- Techniques: design.md-first design system; Extract design.md from an existing Stitch project; Screenshot as style reference (Redesign); Import style from a URL; Sketch plus theme to correct drift; Annotate-and-apply targeted edits; CLAUDE.md pipeline for Stitch skills; Convert a Stitch project to shadcn/ui
- Tools: Google Stitch, Claude Code, design.md, Stitch MCP, Stitch Enhance Prompt skill, Stitch Loop skill, Stitch React component skill, Stitch design.md skill, Google Stitch skills repo, Chrome DevTools, NanoBanana (image generation), GoFullPage (Chrome extension)

## [Anthropic's Head of Design Just Killed The Old Process](../videos/X4vAlWtsJD4.md)
`X4vAlWtsJD4` · AI LABS · 2026-04-02 · q2 · practitioner · tutorial · also: context-engineering, product-ux, coding-agents

A walkthrough of how an AI Labs team now builds app prototypes: actors and constraints first, PRD and architecture files, a Next.js and Supabase prototype with mock data, then a backend added only when needed.

- Techniques: Actor-first requirements; Constraints instead of tool instructions; PRD interview prompt; Layer prompt to architecture.md; Scaffold Next.js with Supabase, then apply a frontend-design skill; Mock-data prototype for sign-off; Task lists from architecture.md; API spec from frontend code plus PRD plus architecture; Supabase MCP for schema and migrations; Front end talks directly to the database; backend only when needed; Delegate the backend layer to a cloud agent
- Tools: Figma, Next.js, Supabase, Supabase MCP, Python, Warp Oz (sponsored cloud-agent orchestration), Stripe, Google authentication, Anthropic general-purpose frontend-design skill

## [This Open-Source Tool Replaces Bubble and Retool (Appsmith)](../videos/8O7AjZIAkpk.md)
`8O7AjZIAkpk` · Better Stack · 2026-04-02 · q2 · intro · review · also: dev-tools

Short Better Stack walkthrough of Appsmith, a self-hostable open-source low-code tool for internal dashboards, showing a Postgres employee search and CRUD-style table in about two minutes, with an honest list of limits and a Retool comparison.

- Techniques: Bind a Postgres table to a low-code table widget; Search query driven by an input widget; Keep logic in JS and source in Git; Server-side pagination for large tables
- Tools: Appsmith, PostgreSQL, React, Docker, Kubernetes, Git, Retool, Bubble, Webflow, ToolJet

## [How I Turned Claude Into a Design Tool with Pencil.dev](../videos/DFcvz2kcR74.md)
`DFcvz2kcR74` · Better Stack · 2026-03-02 · q2 · intro · review · also: coding-agents, mcp-and-tools

Walkthrough of Pencil, a free agent-driven design tool that Claude Code can drive over MCP to build dashboards and a bakery website, then code them. Shows a workable loop, with no benchmarks.

- Techniques: Drive a design tool from Claude Code via its MCP server; Build a UI from a UI kit; Blank-canvas site generation with a style guide; Fix AI design output by direct manipulation; Hand designs to the agent for implementation; Import existing Figma designs
- Tools: Pencil (pencil.dev), Pencil MCP server, Pencil batch design tool, Claude Code, Figma, Figma MCP tool, Sketch, Sketch MCP tool, Lunaris UI kit, Halo UI kit, Nitro UI kit, Unsplash

## [I Didn't Expect This From OpenAI's IDE](../videos/sC4JpJlD3aQ.md)
`sC4JpJlD3aQ` · AI LABS · 2026-03-02 · q3 · intro · tutorial · also: coding-agents, multi-agent, skills-self-improvement

A 7-minute build log: turning a car photo into a 3D hero section for a Next.js landing page with Tripo 3D, OpenAI's Codex app, GSAP and Aceternity UI, with parallel Codex subagents in git worktrees.

- Techniques: Pre-clean the image for image-to-3D; GLB asset in a Next.js public folder; Generate a project skill with the agent's skill creator; Work around agent install timeouts; Parallel subagents in separate git worktrees; Scope the agent with explicit do-not-touch constraints; Fix visual drift with screenshots and named variants
- Tools: Codex app (OpenAI), Tripo 3D, Canva background remover, Next.js, GSAP, Aceternity UI, React Three Fiber, post-processing package for React Three Fiber (named 'Post Processing' in the transcript), npm, GLB (file format), Antigravity (agent manager, compared in passing), Claude Code (mentioned as the previous agent used)

## [Why is Everyone OBSESSED With The New Kimi K2.5 AI Model](../videos/KvOYDevFGiw.md)
`KvOYDevFGiw` · Better Stack · 2026-02-02 · q3 · intro · review · also: models-research, multi-agent, coding-agents

Hands-on review of Moonshot's open-weight Kimi K2.5: video-to-website cloning, a single-image campaign site, and the Agent Swarm feature, with the speaker's verdict that the front-end output is strong but the research output had stale data.

- Techniques: Reference-video to front-end clone; Single-image creative brief; Force subagent fan-out by naming it in the prompt; Check the as-of date of generated research
- Tools: Kimi K2.5, Kimi CLI, FFmpeg, Claude Code, Kimi K2, Llama 4 Scout, GitHub Copilot

## [Astro is Joining Cloudflare (Here's Why)](../videos/vpbNP4loCiE.md)
`vpbNP4loCiE` · Better Stack · 2026-02-02 · q2 · intro · news · also: dev-tools

Astro, the MIT-licensed framework for content-driven sites, is joining Cloudflare. The team says it stays open source, multi-host and governed the same way, and the host sees the move as a funding fix for Astro.

- Techniques: Server-rendered static HTML with islands
- Tools: Astro (6 in beta), Cloudflare (Workers), Next.js, Nuxt, Svelte, Angular, Blazor, React, Vue, Solid, Hono, TanStack

## [Tailwind is Dying... (this is bad!)](../videos/YIRugFtqBsM.md)
`YIRugFtqBsM` · Better Stack · 2026-02-02 · q2 · intro · news · also: dev-tools, product-ux

A Better Stack commentary on a Tailwind CSS maintainer's refusal to review an LLMs.txt PR, arguing AI is eroding docs traffic and the paid products that fund open source.

- Techniques: Publish an LLM-optimized docs endpoint (LLMs.txt); Tie docs funnel to paid products, and track docs traffic against usage
- Tools: Tailwind CSS, Tailwind Plus, Tailwind v4, LLMs.txt, npm, ShadCN, Laravel, Sidekiq, Elastic, Redis, Anthropic, OpenAI

## [This is How I Design With Stitch Now](../videos/VNx9Gy5pHZI.md)
`VNx9Gy5pHZI` · AI LABS · 2026-02-02 · q3 · practitioner · tutorial · also: coding-agents, mcp-and-tools, testing-verification

A Stitch-as-MCP design workflow in Claude Code: plan first, generate one long landing page, pull its HTML, then test with Vercel's snapshot-based Agent Browser. The Stitch MCP wrapper is unofficial.

- Techniques: Stitch MCP for agent-driven design generation; Plan-mode UI guide before design; One long page prompt instead of per-section prompts; Pulling Stitch screen code into a project; Follow-up refactor after code dump; CLAUDE.md rules that mandate a test tool; Snapshot-driven UI testing with Vercel Agent Browser
- Tools: Google Stitch, Stitch MCP (community, unofficial), Google Cloud SDK / gcloud CLI, Homebrew (brew), Claude Code (plan mode, CLAUDE.md), Gemini 3 Flash, Next.js, curl, Vercel Agent Browser, Claude's Chrome extension (compared), Playwright (compared), Puppeteer (compared)

## [Could This Framework Replace Flask, Django, and FastAPI? (Reflex)](../videos/9QmH6DDyLCQ.md)
`9QmH6DDyLCQ` · Better Stack · 2026-02-02 · q3 · intro · tutorial · also: dev-tools

Better Stack walkthrough of Reflex, a pure-Python full-stack web framework; builds a counter, list, conditional and async fetch app, then concludes it is a React wrapper and not worth it over React for the frontend.

- Techniques: Reflex project bootstrap; State class with event handlers; Render lists with rx.foreach; Conditional rendering with rx.cond; Async handler with intermediate yield; Load data on page load; Inspect the compiled output
- Tools: Reflex, Reflex Build, Python, pip, httpx, asyncio, React, Vite, Tailwind CSS, React Router, Random Useless Facts API, Databricks

## [Radix is a problem...](../videos/TLUWRThKijg.md)
`TLUWRThKijg` · Better Stack · 2026-02-02 · q3 · practitioner · review · also: dev-tools

Better Stack argues against Radix UI in favor of Base UI, a headless React component library from the original Radix/Floating UI/MUI creators, comparing render props, data-driven collections, multi-select, and function-based styling.

- Techniques: Migrate asChild to the render prop; Function-as-render-prop for state-aware rendering; Function className with variant libraries; Data-driven collections via the root; Enable multi-select on Select
- Tools: Radix UI, Base UI, React Aria, shadcn/ui, Tailwind CSS, tailwind-variants, CSS Modules, React Hook Form, TanStack Form, Material UI, Floating UI, React

## [I Wasn't Ready For What This Does](../videos/XP6TJRbOdGo.md)
`XP6TJRbOdGo` · AI LABS · 2026-02-02 · q2 · intro · tutorial · also: voice-multimodal, context-engineering

A step-by-step landing-page workflow: Google Whisk keyframes, Google Flow frame-to-video, MP4-to-animated-WebP for a scroll-mapped hero, then Claude adds HeroUI, Motion.dev and 21st.dev components in Next.js.

- Techniques: Two-keyframe hero animation; MP4 to animated WebP for scroll mapping; XML-sectioned prompt for an AI coding agent; Install individual UI components instead of the whole library; Copy-paste component prompts from 21st.dev
- Tools: Google Whisk, Nano Banana (image generation, via Whisk), Gemini 3 (prompt expansion layer in Whisk; planning in Flow), Google MixBoard, Google Flow, VO 3.1 (video model; 20 credits per video), Claude (coding agent), Next.js, Tailwind CSS, HeroUI (library, formerly Hero UI), framer-motion, Motion.dev (motion library)

## [Shadcn is now PERFECT for Vibe Coding (v2 changes)](../videos/sIvYbCZzAts.md)
`sIvYbCZzAts` · Better Stack · 2026-01-02 · q2 · intro · review · also: dev-tools

Walkthrough of shadcn v2: a new visual customizer, Base UI as the component core instead of Radix, and a one-prompt comparison showing that AI-built UI looks better when constrained to shadcn components.

- Techniques: Customizer-first scaffold for vibe-coded UI; Constrain AI generation to a component library; Use the shuffle button and open the customizer in a second tab; Migrate v1 to v2 by copying components (unverified)
- Tools: shadcn/ui (v2), Base UI, Radix UI, Tailwind CSS, TanStack Start, bun, components.json, Tabler Icons, Lucide, Hugeicons, Phosphor, JetBrains Mono

## [The Greatest Design System I've Ever Used](../videos/61Z2jLH4yGU.md)
`61Z2jLH4yGU` · AI LABS · 2026-01-02 · q2 · intro · review · also: mcp-and-tools, product-ux

A short AI-design tool roundup: Design OS for guided planning, image generators, competitor-screenshot style extraction, Figma-to-Lottie animation and an HTML-to-Figma MCP, with a sponsored agency pitch at the end.

- Techniques: Design OS planning loop before building; Competitor style extraction into Claude Code; Figma animation to Lottie to Claude Code; HTML to Figma via MCP
- Tools: Design OS (Builder Methods), Claude Code, Claude, Cursor, GitHub Copilot, Viscom, Google Mixboard, Nano Banana, Go Full Page (browser extension), Figma, Magic Animator (Figma plugin), Lottie (Figma plugin)

## [5 Ways To Build Beautiful Websites Using Claude Code](../videos/VGYsHicpp34.md)
`VGYsHicpp34` · AI LABS · 2026-01-02 · q2 · intro · review · also: coding-agents, testing-verification

A design-first workflow for building websites with Claude Code: shadcn presets, Coolers palettes, Google Stitch designs and prototypes, background browser-testing agents, and Drawbridge for visual fixes. Partly a promo for the presenter's agency.

- Techniques: shadcn preset import; Palette before layout; Design in Stitch, then hand off to Claude; Screenshot-driven inspiration; Background browser-test subagent; Drawbridge visual issue reporting
- Tools: shadcn/ui, Coolers, Google Stitch, Gemini 3 Pro, Nano Banana, Google AI Studio, Jules, Claude Code, Claude subagents (background mode), Puppeteer MCP, Drawbridge, Opus 4.5 (named as context)

## [Cloudflare Just Destroyed v0, Lovable, and Replit in One Move](../videos/pDnpIkbJwN4.md)
`pDnpIkbJwN4` · Better Stack · 2026-01-02 · q2 · intro · review · also: sandboxing-execution, software-factory

Better Stack walkthrough of Cloudflare's open-source Vibe SDK: a self-hostable, MIT-licensed prompt-to-app platform that generates, previews and deploys full-stack apps on Cloudflare's edge. Mostly a demo and deploy checklist, with thin evidence behind the comparison claims.

- Techniques: Self-host Vibe SDK on Cloudflare via the Deploy button; Blueprint-first, phased app generation; Iterate by describing the bug in chat; Route all model calls through an AI gateway with caching
- Tools: Cloudflare Vibe SDK (open-source, MIT, self-hostable), Cloudflare Workers, Cloudflare Workers for Platforms, Cloudflare AI Gateway, Cloudflare sandbox containers, Google Gemini API (default model key), Bun (package install), GitHub (clone, export target), Replit (comparison), Cursor (comparison), Vercel (comparison), v0 (comparison)

## [Gemini Designer is INSANE... Build Beautiful Websites in Minutes](../videos/v9Rd_l6gLjU.md)
`v9Rd_l6gLjU` · AI LABS · 2025-12-02 · q3 · practitioner · tutorial · also: product-ux, coding-agents, context-engineering

Walkthrough of Google Stitch, an AI UI designer, plus a six-phase Klein rules-file workflow that turns exported Stitch HTML into a Next.js app and validates it against the designs.

- Techniques: Iterative screen-by-screen prompting in Stitch; Design-system extraction from exported HTML (phase 1); Per-page analysis and component library (phases 2-3); Navigation-flow mapping (phase 4); Blueprint-then-implement (phase 5); Validation checklist and scorecard (phase 6); Build from HTML, not screenshots
- Tools: Google Stitch, Klein (VS Code extension, multi-model, rules file, MCP store), VS Code, Next.js, Figma (via Klein's MCP store), ChatGPT (GPT-5 Temporary), Claude Pro, Material UI, Arc browser (example prompt)

## [Here's What They Didn't Tell You About Gemini 3](../videos/kyflIo3EKLw.md)
`kyflIo3EKLw` · AI LABS · 2025-12-02 · q2 · intro · review · also: models-research, coding-agents, context-engineering

Hands-on review of Gemini 3 vs Claude and GPT-5.1 for UI generation and multi-phase coding; the speaker finds Gemini 3 strong at UI design but credits the agent harness, not the model, for most of the difference.

- Techniques: Same-spec head-to-head coding test; Separate model from harness; One-shot UI test with no guidance; Track context-window use per story
- Tools: Gemini 3 Pro, Gemini CLI, Google Antigravity (VS Code fork), Google AI Studio (Code Assistant), Claude 4.5, Claude Code, Claude desktop app, Claude canvas, GPT-5.1, GPT-5, nano banana (image model, named by the speaker)

## [Claude Just Introduced a New Way To Fix Your UI](../videos/eLDq5TfIHys.md)
`eLDq5TfIHys` · AI LABS · 2025-12-02 · q2 · practitioner · review · also: skills-self-improvement, claude-code, context-engineering

AI LABS tests Anthropic's front-end design skill guidance in Claude Code: typography and theme prompts, a 400k-token mega-prompt, and skills that often fail to auto-load.

- Techniques: Turn a design prompt into a project skill; Force-invoke the skill by name; Describe design as implementation, not taste; Name the fonts explicitly; Stage the design prompt per dimension, then combine; Artifacts builder skill for componentized output
- Tools: Claude Code, Claude skills, Claude desktop app, Google Fonts, React, shadcn-style UI (as generated by Claude), Zen Browser, Arc Browser, Anthropic front-end design cookbook, Claude Code front-end design plugin

## [I've Found A Better Alternative to Lovable.dev](../videos/05Bg0yI7Ob4.md)
`05Bg0yI7Ob4` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents

A sponsored walkthrough of Leap, an AI app builder on the Encore backend framework, pitched as a Lovable alternative that scales. It shows building a shop, deploying, and handing the repo to Claude Code.

- Techniques: Step-by-step MVP prompting for a generated app; Reference-image fixes for UI drift; Auth as a detailed prompt; Clone-and-continue handoff to a local coding agent; Give the agent a platform rule file; Scope agent edits tightly
- Tools: Leap, Encore (open-source backend framework; Encore Cloud), Lovable, Claude Code, Cursor, React, shadcn/ui, Unsplash, AWS, Google Cloud Platform

## [The PERFECT Design Workflow with Claude Code](../videos/9uFVCxfkLCo.md)
`9uFVCxfkLCo` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, mcp-and-tools, context-engineering

Walkthrough of capturing a website component with the Web2 MCP Chrome extension, cloning it one-to-one with a Claude Code/Cursor agent using a modified CLAUDE.md, and generating variants with SuperDesign. Mixed results, with a Rocket.new sponsor segment.

- Techniques: Capture an element with Web2 MCP and reference it by ID; Initialize SuperDesign rule files and edit CLAUDE.md for one-to-one cloning; Two-session workflow: clone first, then generate variants; Use SuperDesign's canvas view to inspect how a design was produced
- Tools: Web2 MCP (paid Chrome extension and MCP server; $2.50/month Pro tier as stated), MCP Pointer (open-source alternative, judged weaker), SuperDesign (superdesign.dev; editor extension with rule files for Cursor, Windsurf and CLAUDE.md), Claude Code, Cursor, Windsurf, Stagewise (mentioned as a prior featured tool), Arc browser, shadcn/ui (described as the common component library), Rocket.new (sponsor; no version), Netlify (mentioned in the Rocket.new segment)

## [3 Ways to Clone Any Site Using Cursor AI](../videos/zmP8Pl-MJXw.md)
`zmP8Pl-MJXw` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: mcp-and-tools, coding-agents

Three practical ways to clone a website's design into a Next.js or HTML project using Cursor plus Gemini, the Figma MCP, or the Firecrawl MCP, with the presenter noting where each one falls short.

- Techniques: Full-page screenshot capture for layout cloning; Marker-based splitting of generated code into a Next.js app; Figma selection link to Cursor via the Figma MCP; Turning a GitHub repo into indexable docs for Cursor; Scraping a live site with Firecrawl MCP for a structural clone; Build clones in a framework, not plain HTML
- Tools: Cursor, Gemini (canvas feature), Claude artifacts, ChatGPT, Chrome DevTools (command runner, full-size screenshot), React, Next.js, bash (integrate.sh script), Figma MCP, git2doc, Firecrawl MCP (8 tools), Wallhaven (example site)

## [I Found the BEST UI Library](../videos/aQB0B3a1fh8.md)
`aQB0B3a1fh8` · Better Stack · 2025-11-02 · q2 · intro · review · also: dev-tools

A 5-minute tour of 21st.dev, a catalog of shadcn-style React component collections, showing how to install a component with the shadcn CLI or paste a copy-prompt into an AI editor to adapt it.

- Techniques: Install a registry component with the shadcn CLI; Install by copying the code manually; Use the copy-prompt button for an AI editor; Iterate on the pasted component with small prompts
- Tools: 21st.dev, shadcn/ui and the shadcn CLI, shadcn registry, Aceternity UI, Origin UI, Magic UI, Next.js, Tailwind CSS, v0, Lovable, Bolt.new

## [Shadcn's AI Elements are AWESOME (easiest way to build a chat app)](../videos/dS7hyPNvIb8.md)
`dS7hyPNvIb8` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: dev-tools, product-ux

A quick tour of Vercel's AI Elements, shadcn-style chat components built for the AI SDK, and a claimed five-minute build of a chat app with web search and markdown rendering.

- Techniques: Install AI Elements into an existing shadcn project; Chat screen composition; Per-request web-search switch
- Tools: AI Elements (Vercel), AI SDK (Vercel), shadcn/ui, shadcn CLI, Tailwind CSS, react-markdown, react-syntax-highlighter, Prism, Perplexity (model with built-in web search), GPT-5, Claude (model, transcribed as 'ClaudeForce'), ChatGPT (named as a clone example)

## [How the 1% ACTUALLY Build Apps with Cursor's Context Engineering](../videos/QgA55EnmUp4.md)
`QgA55EnmUp4` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: context-engineering, coding-agents

A hands-on workflow for building a full app with Cursor or Claude Code by splitting context into a PRD-generated docs folder, a short always-on rule, and a staged implementation plan.

- Techniques: Four-file documentation set generated from a PRD; Small always-attached workflow rule that routes to on-demand docs; Staged implementation plan with optional subtask lists; Put the foundations and scope into the generate prompt; Claude Code slash command for the generate step; Parallelize only independent work
- Tools: Cursor, Claude Code, CLAUDE.md, ChatGPT, Next.js, FastAPI

## [How I Build Beautiful Websites With AI](../videos/1cB2iqz_vnM.md)
`1cB2iqz_vnM` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: claude-code, coding-agents, context-engineering

Walkthrough of Drawbridge, an open-source Chrome extension that turns clicks on a localhost page into a queued task list for Claude Code or Cursor, with landing-page and client-prototyping use cases. Main takeaway: UI fixes become batched, position-aware agent tasks.

- Techniques: Install Drawbridge as an unpacked Chrome extension; Queue element-level UI changes; Have the agent process the queue; Turn the Cursor workflow rule into a Claude Code slash command; Build a landing page section by section; Keep a design language in files the agent reads
- Tools: Drawbridge (open-source Chrome extension and visual editor for coding agents), Chrome (extensions, load unpacked), Cursor, Claude Code, shadcn/ui, TweakCN (shadcn theme site), Lumi (sponsored AI website builder), Git (used to revert the demo project)

## [Replit Has Become Essential to My Vibe Coding Workflow.](../videos/YtgqzCEeHVw.md)
`YtgqzCEeHVw` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, context-engineering

Walkthrough of a vibe-coding workflow: Claude brainstorms and writes a no-code front-end prompt, Replit generates a shadcn-based responsive UI with exposed APIs, and Windsurf builds the FastAPI backend from the exported API docs.

- Techniques: Planning prompt with pages and modals; Front end first, API docs as the contract; Dependency and run step for a generated front end; Send browser context to the agent; In-memory storage first, database later
- Tools: Claude (Anthropic), Replit, shadcn/ui, Windsurf, Cascade, Cursor, v0, FastAPI, npm, SuperWhisper, macOS voice dictation, Supabase

## [Tempo Labs Tutorial: The Ultimate Vibe Coding Package](../videos/k6uBbUZ9MZg.md)
`k6uBbUZ9MZg` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: product-ux

Tutorial walkthrough of Tempo Labs, an AI app builder that wires Next.js, Supabase auth/database and Stripe payments before generating a gradient-wallpaper SaaS from a PRD-first prompt. Mostly a promotional demo with few verified claims.

- Techniques: Pre-wire integrations before the first build prompt; Supabase connection via Tempo; Stripe test-mode wiring; Adding plans through the Stripe product catalog; PRD-first build prompt with a subtask loop; Fix client-side rendering by prompting
- Tools: Tempo Labs (Tempo), Next.js, Supabase, Supabase edge functions, Supabase MCP, Stripe, Stripe webhooks, Mermaid, Cursor, Windsurf, Aceternity UI, Expo

## [Deploy Project to Netlify Instantly.](../videos/ruRxIGmsCgs.md)
`ruRxIGmsCgs` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents

Windsurf Wave 6 adds "deploys": Cascade publishes a static site to Netlify under a windsurf.build subdomain, which must be claimed in your own Netlify account within 24 hours.

- Techniques: Agent-driven static deploy; Claim within 24 hours; Deploy-log feedback loop; Plan pages and modals first; Specify constraints in the build prompt
- Tools: Windsurf (Wave 6, Cascade agent), Netlify, GitHub, Cursor, netlify.toml

## [Build Apps Using ONLY your Voice (WARP 2.0 is Insane)](../videos/4n7z4eb_aKU.md)
`4n7z4eb_aKU` · Better Stack · 2025-11-02 · q2 · intro · review · also: coding-agents, dev-tools

Better Stack demos Warp 2.0's Code and Agents features by building several small web apps mostly from voice prompts, then deploys one. Mostly a demo with a few practical notes, and the title oversells it.

- Techniques: Refine-with-docs correction; Reference image plus voice prompt for UI; Auto-approve for unattended agent runs; Parallel agent panels by concern; Deploy by asking for a host, then letting the agent run it
- Tools: Warp 2.0 (Warp Code, Warp Agents, Warp Drive), Tailwind CSS (Vite plugin), Vue.js, React (mentioned only), Vanilla JavaScript, HTML5 canvas, Framer (used for the reference design), GitHub Pages, Vercel CLI (mentioned), npm, Cursor (comparison), Claude Code (comparison)

## [ChatGPT Apps vs n8n vs AgentKit: The Future of AI Automation](../videos/lcqlgif2hFA.md)
`lcqlgif2hFA` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: mcp-and-tools, product-ux

Walkthrough of building a ChatGPT app as a self-hosted MCP server (Express, Google Places API) exposed through ngrok and registered in ChatGPT developer mode. Title promises an n8n/AgentKit comparison that never appears.

- Techniques: Prompt-driven MCP server scaffold for a ChatGPT app; Reuse an existing MCP server as a ChatGPT app; Expose localhost with ngrok for ChatGPT; Register the MCP endpoint in ChatGPT developer mode; Widget output over plain text, polished with ShadCN
- Tools: ChatGPT apps (OpenAI), OpenAI apps SDK, MCP (Model Context Protocol) SDK, Express, Google Places API, ngrok, ShadCN, Cursor, Codex, Claude Code, Make.com (sponsor), n8n (named in title only)

## [AI Tool Converts Your Sketch into Code Instantly!](../videos/p5hEVQIisgc.md)
`p5hEVQIisgc` · AI LABS · 2025-11-02 · q2 · intro · review · also: product-ux, inference-serving

Demo and local-install walkthrough of Groq App Gen, an open-source web app that generates and iterates on small web apps from a sketch plus text prompts on Groq inference; speed is asserted, not measured.

- Techniques: Local install of Groq App Gen; Sketch then prompt; One change per prompt, verify each; Generate the edit list with a second LLM
- Tools: Groq App Gen (open-source web app, GitHub repo), Groq API / Groq inference, Llama 3.3 70B (spoken as 'Lama 3.37 70 billion' in captions), Next.js, TypeScript, npm, Python, VS Code, Windsurf, Cursor, ChatGPT

## [Shadcn Isn’t Just a Library Anymore… Here’s How to 10x Your UI](../videos/V8rGgwQ-VJ0.md)
`V8rGgwQ-VJ0` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: mcp-and-tools, context-engineering

Shows how a shadcn/ui MCP server (component demos and blocks) plus Cursor rule files and a plan-first workflow produces better React UI, then how TweakCN restyles the result.

- Techniques: Fetch-before-build loop with the shadcn MCP; Rule file that forces the MCP lookup order; Plan first, with components named and no code; Theme with TweakCN after the structure is done
- Tools: shadcn/ui, shadcn UI MCP server (GitHub repo), Cursor, Claude (chat, used for the initial plan), Claude desktop MCP configuration, Windsurf, Claude Code, TweakCN, GitHub personal access token

## [Vercel made a Model (v0 in Cursor)](../videos/jZB1sXDaOj8.md)
`jZB1sXDaOj8` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: coding-agents, models-research

Better Stack tries Vercel's new v0-1.0-md model through its API, routes Cursor's OpenAI model slot to it via a base-URL override, and builds a shadcn to-do app from one prompt.

- Techniques: Get a v0 API key for model access; Route Cursor to the v0 model via base-URL override; Single-prompt full-app generation in agent mode; Compare the same prompt across two surfaces
- Tools: v0 (v0.dev), v0-1.0-md, Cursor, Next.js, shadcn/ui (spoken as 'ShadCN'), Vercel AI SDK, Vercel AI playground, Three.js (mentioned as a v0 output example), Codex (transcript reads 'codecs'; another coding tool the host names as a target)

## [3 Ways to Make GENUINELY Stunning Websites Using Claude Code](../videos/McJluKfjVGk.md)
`McJluKfjVGk` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: claude-code, mcp-and-tools, coding-agents

A walkthrough of three Claude Code workflows for building polished UIs: SuperDesign for iterative design canvases, ShadCN MCP for component-library builds, and Firecrawl or Figma MCPs for cloning existing designs.

- Techniques: SuperDesign canvas setup; Layout-then-theme-then-polish staging; Targeted correction round; ShadCN MCP plus a saved usage-rule slash command; Theme import from tweakcn; Site cloning with Firecrawl MCP; Figma MCP selection import; Animation snippet import from Animatopy
- Tools: Claude Code, SuperDesign (superdesign.dev, VS Code / Cursor extension), Cursor, VS Code, ShadCN UI, ShadCN MCP server, Firecrawl MCP, Figma MCP server, tweakcn, Animatopy, Colors (palette generator website), Next.js

## [Figma MCP Tutorial: The Best Way to Clone a Front-End](../videos/FJBLhd23f80.md)
`FJBLhd23f80` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: mcp-and-tools, coding-agents

A 5-minute tutorial on connecting an open-source Figma MCP server to Cursor, then having the agent generate HTML/CSS from a Figma page link instead of a screenshot.

- Techniques: Run a Figma MCP server over SSE and attach it to Cursor; Copy a link to a Figma selection and hand it to the agent; Force the agent to the node tool when it picks the wrong one; Combine the Figma link with a screenshot for corrections
- Tools: Figma MCP server (glips, open source, run via npx and pnpm), Figma API / personal access tokens, Cursor (MCP client), pnpm, npx, git, HTML/CSS (generation target)

## [GitHub Spark Is INSANE – A Full App in Just 20 Minutes!](../videos/Lwi6VKBl7EU.md)
`Lwi6VKBl7EU` · Better Stack · 2025-11-02 · q2 · intro · review · also: coding-agents, product-ux

A Better Stack walkthrough of GitHub Spark, a browser-based vibe-coding platform, building a movie-rating app from one prompt in about 4 minutes, with the caveats that it is React/TypeScript-only, needed a manual API key, and was not responsive.

- Techniques: Front-load the full feature list in one prompt; Supply the missing credential the builder asks for, and verify it; Iterate through the suggestion panel while using the app; Tune the in-app LLM through the prompts tab; Check responsiveness explicitly
- Tools: GitHub Spark, Claude Sonnet 4, Kiro (Amazon IDE, mentioned only), React, TypeScript, Tailwind CSS, TMDB movie API, Unsplash, GitHub Copilot Pro Plus

## [Add Social Logins to Next.js in 5 Minutes (Supabase UI)](../videos/jg6XAc-hhc8.md)
`jg6XAc-hhc8` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: dev-tools

Better Stack walkthrough of adding GitHub social login to a Next.js app using Supabase UI, shadcn's CLI, and a registry-installed component; mostly UI clicking through Supabase and GitHub settings.

- Techniques: Install a Supabase UI auth component via shadcn registry; Wire GitHub OAuth into Supabase Auth; Env vars from the Supabase connect dialog
- Tools: Next.js, shadcn/ui (shadcn CLI, `npx shadcn@latest`), Supabase, Supabase UI, GitHub OAuth, VS Code, Vercel (mentioned only as the look to imitate)

## [This App Works WITHOUT Internet?! (Jack Dorsey’s BitChat)](../videos/hdRn3DQ_C_Y.md)
`hdRn3DQ_C_Y` · Better Stack · 2025-11-02 · q2 · intro · review · also: security-guardrails

Quick hands-on look at Jack Dorsey's open-source BitChat, a Bluetooth mesh messenger with no internet or servers. The reviewer finds the iOS build buggy, and the app is a weekend vibe-coded project that drew security criticism.

- Techniques: Cross-platform two-device messaging test; Check the repo's security status before trusting an app
- Tools: BitChat, Bluetooth Low Energy (BLE), NoiseXX handshake, Goose, AirTags, iOS, Android

## [3 Simple Ways To EARN Money With Claude Code Apps](../videos/Y2oK0nubq9A.md)
`Y2oK0nubq9A` · AI LABS · 2025-11-02 · q2 · intro · review · also: product-ux, claude-code

Walkthrough of consumer-app paywall patterns (instant-value previews, habit hooks, usage caps, tier ladders) plus a Claude Code design-command workflow for cloning paywall screens. Middle segment is sponsored.

- Techniques: Progress-gated free tier for education apps; Anchored yearly pricing; Progress hook with time or feature gating; Usage cap at point of need; Three-tier ladder with a highlighted middle; Slash-command design pass for prototypes; Screenshot-to-clone reference
- Tools: Claude Code, Cursor, VS Code, SuperDesign, design.md (prompt file), Flowbite, Paywall Screens, Make, HabitKit, Sleep Cycle, Babbel, CapCut

## [I Made MCP AI Agents That Automate Every App I Build.](../videos/23ykmgvaSmM.md)
`23ykmgvaSmM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools, coding-agents

Tutorial on wrapping an existing FastAPI to-do app with the FastAPI MCP server so Cursor, Windsurf, Claude Desktop, or a Python MCP-client agent can call its endpoints as tools. Covers setup, tool naming, and a registration gotcha.

- Techniques: Expose a FastAPI app as MCP tools; Name MCP tools with operation IDs; Register MCP after all endpoints are declared; Add the MCP server to an IDE client; Drive the MCP server from a custom Python agent
- Tools: FastAPI, fastapi-mcp (FastAPI MCP package), Next.js, Cursor, Windsurf, Claude Desktop, pip, uv, MCP use framework (Python MCP client library, name as spoken), mcp.json, config.json

## [Firecrawl MCP = Effortless Web Scraping](../videos/2GHRDoFquOo.md)
`2GHRDoFquOo` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools, coding-agents

Tutorial on wiring the Firecrawl MCP server into Cursor so an agent can scrape a live URL and generate a near-copy of a Notion landing page in Next.js. Shows setup and a single demo run, with the output's flaws called out.

- Techniques: Register Firecrawl MCP in Cursor; Name the MCP tool in the prompt and use agent mode; Scrape, then generate by component; Pick scrape vs extract by goal
- Tools: Firecrawl MCP server (scrape and extract tools, npx command, API key), Cursor (agent mode, MCP settings), Windsurf (same MCP config pattern, mentioned as an alternative), Claude 3.7 Sonnet (model selected in Cursor), Next.js (blank starter app used as the target), Notion landing page (the site being cloned)

## [This Designer is INSANE... The Ultimate UI Setup](../videos/uayt-IVbh8E.md)
`uayt-IVbh8E` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, multi-agent, context-engineering

Walkthrough of a Claude Code sub-agent pipeline for UI work: a UX agent drafts layout from requirements, a UI agent applies color variants, and a converter agent ports the HTML to SwiftUI.

- Techniques: Stage-separated UI sub-agent pipeline; Explicit agent count for variants; Split HTML output into HTML, CSS and JS files; Keep emoji placeholders, then fix icons in the target platform; Doc-grounded conversion guide via Context7, then bake into the agent
- Tools: Claude Code (sub-agents defined as markdown files), Cursor (mentioned in the intro as an AI coding tool, not used in the walkthrough), Context7 MCP, SwiftUI, iOS Simulator, HTML / CSS / JavaScript

## [Before You CHOOSE, Watch This Cursor vs Windsurf Face-Off!](../videos/0Ttn6dqnuQk.md)
`0Ttn6dqnuQk` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, token-cost-efficiency

A short, single-run head-to-head of Cursor and Windsurf on a CLI task app, a web music player and pricing, with a verdict favoring Windsurf.

- Techniques: Same-prompt bake-off with explicit pass criteria; Scope check with a deliberately simple app; Trial and plan comparison before buying
- Tools: Cursor (Composer, agent panel), Windsurf (Cascade, image upload, explain-and-fix), ElevenLabs (voiceover audio used in the music-player test), tasks.json (file created by the CLI test)

## [3 More Ways To ACTUALLY Build Beautiful Websites with Cursor IDE](../videos/U1_nzjWUpL4.md)
`U1_nzjWUpL4` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: coding-agents, mcp-and-tools, context-engineering

Three practical ways to turn website designs into working Next.js UI in Cursor: a structured front-end spec prompt, a design.json built from screenshots, Browser MCP for cloning structure, and stagewise for precise element-level edits.

- Techniques: Structured front-end spec prompt; Screenshot to design.json style profile; Clone a site's structure with Browser MCP; Element-level UI edits with stagewise
- Tools: Cursor, Claude, ChatGPT, Claude Code, Next.js, Tailwind CSS, Browser MCP, stagewise, mcp.json, design.json

## [Trae AI: The New Cursor AI Alternative](../videos/cdLnorNbewA.md)
`cdLnorNbewA` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, testing-verification

Hands-on test of Trae, ByteDance's VS Code-fork IDE with a single-agent workflow and free Claude access; a to-do app and a Spotify screenshot clone show a basic UI with missing-config errors, verdict "hype".

- Techniques: Screenshot-to-app clone prompt; Built-in web view preview; Manual behavioural check of agent output; Config-first debugging for missing styles
- Tools: Trae (ByteDance IDE), Claude 3.5 Sonnet, GPT-4.0 (mentioned as promised, not available), Cursor, Windsurf, VS Code, React, Tailwind CSS, PostCSS

## [Replits NEW AI Agents Are INSANE](../videos/v1jLYiW0AWc.md)
`v1jLYiW0AWc` · AI LABS · 2025-11-02 · q3 · intro · review · also: product-ux, mcp-and-tools

Hands-on beta test of Replit Agent 3's Agents and Automations builder: guided setup via Slack, Telegram or scheduled triggers, OAuth connectors, and automatic app testing, with real gaps in memory, integrations and Slack deployment.

- Techniques: Least-privilege Notion OAuth; Test memory after deployment; Ask the agent to explain a missing action; Telegram publishing setup; Verify side effects end to end
- Tools: Replit Agent 3, Replit Agents and Automations, Replit app testing, Replit Stripe integration, OpenAI API, Notion (connector), Outlook (connector), OneDrive (connector), Spotify (connector), Linear (connector), Slack (connector and deployment target), Telegram (deployment target)

## [Build Your Own Shadcn/ui](../videos/_JqUWzI0AXA.md)
`_JqUWzI0AXA` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: dev-tools

Better Stack walkthrough of publishing your own components and blocks as a shadcn registry: registry.json, npx shadcn build, hosted JSON installed by URL, plus v0 and theme hooks.

- Techniques: Registry folder layout; registry.json item entries; Build to hostable JSON; Install into another project; Compose a block from registry dependencies; Open a registry item in v0; Distribute a theme through the registry
- Tools: shadcn/ui CLI (npx shadcn build, npx shadcn add), Next.js, React Aria Components, v0 (v0.dev), TweakCN, Cursor (mentioned as writing the remaining primitives from the first one), Supabase UI (transcript says 'Superbase UI'; mentioned as a shadcn-style collection), GitHub (mentioned as a possible host for the JSON)

## [I Found a Tool That Breaks MCP (In a Good Way)](../videos/6R7CoIKKkDE.md)
`6R7CoIKKkDE` · AI LABS · 2025-11-02 · q2 · intro · review · also: mcp-and-tools

Tempo Labs' MCP app store packages third-party APIs as MCP servers with docs built in; the host builds an ElevenLabs quotes app by installing integrations and prompting. Promotional, single happy-path demo.

- Techniques: Connect the backend before the integrations; Install an integration from the MCP app store; PRD and user flow as the build spec; Describe the full behavior in one feature prompt; Add error logging before debugging a broken integration
- Tools: Tempo (Tempo Labs app builder, with its MCP app store), Model Context Protocol (MCP), Supabase, Firecrawl, ElevenLabs (Eleven Labs API), Google Gemini, OpenAI, Anthropic (auto-caption reads 'Tropic'), Next.js (starter template kit), shadcn/ui (auto-caption reads 'Shadzian'), Mermaid, React

## [Cursor AI Shotgun Code (FREE): Fix Any Next.js App with AI (Full Tutorial)](../videos/4A66bMRiPQ0.md)
`4A66bMRiPQ0` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: context-engineering, coding-agents

A walkthrough of Shotgun Code, which packs a whole Next.js repo into one prompt, gets a full diff from Gemini 2.5 Pro, and applies it in Cursor to overhaul a personal app.

- Techniques: Setup and launch from repo root; Curate the context before generating the prompt; Write one task plus custom rules into the packed prompt; Generate the diff in Google AI Studio; Apply the diff with a coding agent in chunks; Control visual style through the task text
- Tools: Shotgun Code (the GitHub repo demoed, a Go app with a frontend), Go, Node.js, Wails CLI (captioned as 'Wales'), Next.js, Google AI Studio, Gemini 2.5 Pro, Gemini Flash (mentioned as the option not to use), Cursor, Windsurf (mentioned as an alternative executor), Claude 3.5 Sonnet, shadcn/ui (captioned as 'shad cn')

## [Codeium Windsurf: The Full-Stack App Builder | Better Than Cursor?](../videos/Wvyc2E6OHm8.md)
`Wvyc2E6OHm8` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents

A feature tour of Windsurf's Cascade and Flows agent features, comparing it with Cursor and building a 2048 game and a Splitwise clone from single prompts. Useful as a demo of full-stack generation, thin on technical depth.

- Techniques: Start from an example project in Cascade; Iterative follow-up prompt, then review with OpenDiff; Name-based full-stack build prompt; Paste raw errors back into the agent; Flows for multi-step tasks with context kept
- Tools: Windsurf (Codeium editor), Cascade, Flows, Cursor, Cursor Composer, GitHub Copilot, VS Code, Bootstrap 5, Claude models (named as available on Windsurf Pro, no version given), GPT-4 (named, no version given), OpenDiff

## [Is This The Future of Vibe Coding? (Vibe Kanban)](../videos/NKkO8JL6IJg.md)
`NKkO8JL6IJg` · Better Stack · 2025-11-02 · q2 · intro · review · also: software-factory, coding-agents

Better Stack walkthrough of Vibe Kanban, a free open-source board that assigns tasks to coding agents, runs them in parallel and sends their diffs to review; the setup is clear, but the depth is thin and the demo shows bugs.

- Techniques: Kanban as a dispatcher for parallel agent tasks; Setup via npx and the in-app flow; Per-task agent and base-branch selection; Human review gate before merge
- Tools: Vibe Kanban (npx vibe-kanban), Claude Code, Amp, Gemini CLI, OpenCode, Codex (transcript shows 'echo', likely Codex), VS Code, GitHub, Nuxt, Tailwind CSS, MCP servers (configurable in the app)

## [People Are Getting RICH With AI Mobile Apps – Let’s Build One](../videos/HQJUvSLO91o.md)
`HQJUvSLO91o` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, context-engineering

A walkthrough of building a macOS menu-bar Swift app by prompting Windsurf with a docs-first template and Gemini 2.5, after Claude failed on the same prompt; mostly process, with the prompt itself left in the video description.

- Techniques: Docs-first agent prompt for a new app; Scaffold the native project and place it in the agent workspace; Relay errors as text, and switch models for visual bugs; Turbo mode for unattended builds; Export a standalone macOS app from Xcode
- Tools: Windsurf, Cursor, Gemini 2.5, Claude 3.7, Claude, ChatGPT, Xcode, Swift, SwiftUI, Taskmaster (mentioned, as needing Claude and Perplexity API keys), Perplexity API (mentioned), Next.js (analogy only)

## [Google Firebase is an AI IDE now... (and its good!?)](../videos/dAE4YloBUgI.md)
`dAE4YloBUgI` · Better Stack · 2025-11-02 · q2 · intro · review · also: coding-agents, product-ux

A Better Stack walkthrough of Google's Firebase Studio, a browser IDE that turns a prompt into a blueprint, a built app, and a Firebase deployment. The presenter finds the prototyping flow useful but the annotation and AI-injection behavior unreliable.

- Techniques: Confirm the blueprint before the build; Auto-provision the Gemini key from the build prompt; Scoped edit with inspect-element; Annotation overlay (lower reliability); Phone check via public preview link; Drop into the code view for manual fixes; Publish with Firebase App Hosting
- Tools: Firebase Studio, Project IDX (earlier name of Firebase Studio), Gemini 2.5 Pro, Gemini Flash, Gemini 2.5 Pro Experimental, Gemini API, Google AI Studio, Excalidraw, ShadCN UI, Next.js, Astro, Firebase App Hosting

## [Phi-4: The Smallest Open Source AI Model](../videos/yzSYIndCWD8.md)
`yzSYIndCWD8` · AI LABS · 2025-11-02 · q2 · intro · review · also: local-ai, coding-agents

Single-run hands-on test of Phi-4 (14B, MIT license) through Ollama, bolt.diy and Cline. It runs locally, but it failed to integrate a React component, which the speaker blames on the context window.

- Techniques: Local model via Ollama; OpenRouter key as a hosted fallback; bolt.diy from source; Point Cline at local Ollama; Frontier model writes, local model integrates; Shrink the task when the agent stalls
- Tools: Phi-4 (Microsoft, 14B open weights, MIT license; captioned as "5.4"), Ollama, OpenRouter, bolt.diy (captioned "BoltDIY" and "bold.diy"), Cline (captioned "Klein"; formerly Claude Dev), Claude (used to write the card component), VS Code, pnpm, Next.js 14, React, TypeScript, Tailwind CSS

## [How I Build Apps 10x Faster with this 7-Step Cursor Workflow](../videos/cAFIUiE_8DM.md)
`cAFIUiE_8DM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, context-engineering

A solo builder walks through a seven-step AI app workflow (idea, MVP, HTML prototype, design.json styling, SwiftUI conversion, Supabase backend, UI polish) for an iOS habit app, using Cursor and Claude Code.

- Techniques: Stage-gated AI app build; Screenshot-driven correction loop; design.json from a reference image; Rules-file-driven framework conversion; MCP-based backend provisioning; Image model for app icon iteration; Model switching by task
- Tools: Cursor, Claude Code, Claude (chat), ChatGPT, OpenAI image generation model, Supabase, Supabase MCP server, Supabase SDK, SwiftUI, Swift, Xcode, Next.js (mentioned as an example template)

## [This n8n mcp is INSANE... Let AI Create your Entire Automation](../videos/xf2i6Acs1mI.md)
`xf2i6Acs1mI` · AI LABS · 2025-11-02 · q2 · intro · review · also: mcp-and-tools

A walkthrough of an n8n MCP server that lets Claude or Cursor research n8n nodes, build a workflow JSON, validate it and push it into an n8n workspace, shown with a deep-search agent demo and setup steps.

- Techniques: Register the n8n MCP in Claude Desktop; Register the n8n MCP in Cursor; Enforce tool-call order with a rulebook; Full management mode: API key and URL; Deep-search agent pattern in n8n
- Tools: n8n, n8n MCP server, Claude (Desktop, Projects, Artifacts), Claude Code, Cursor, Docker, npx, OpenAI API, SERP API, DuckDuckGo search node, Wikipedia search node, Reddit search node

## [Here Is How to Vibe Code Large Scale Projects](../videos/k9fPAzS5_Kw.md)
`k9fPAzS5_Kw` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: coding-agents, context-engineering

AI LABS walkthrough of Plandex, a self-hosted CLI coding agent aimed at large projects: local Docker setup, chat-then-tell workflow, reviewable sandboxed changes, and one Swift app demo. Context-size claims are unverified.

- Techniques: Self-host Plandex in local mode; Set keys and initialize a repo; Chat to brainstorm and understand, then tell to implement; Review before applying, and debug failed commands
- Tools: Plandex, Docker, OpenRouter API, OpenAI API, Tree-sitter, Cursor, Xcode, Swift, SwiftUI, Gemini 2.5

## [This MCP Setup is the Best Way to Add 3D Models to Your Frontend](../videos/srsst0L51RE.md)
`srsst0L51RE` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools, coding-agents

Short tutorial on connecting the Sketchfab MCP server to Cursor so an agent can search, download and place a 3D model into a Three.js landing page from one prompt.

- Techniques: Install the Sketchfab MCP server from source; Get a Sketchfab API token; Get the absolute path to the built server entry point; Register the server in Cursor via mcp.json; Prompt for a 3D hero section and iterate on the model
- Tools: Sketchfab MCP server (community server listed on mcp.so), Sketchfab, Cursor, Windsurf, Claude Desktop, Three.js (3JS), git, npm, Claude 3.7 (mentioned for 3D game generation)

## [Bun is now the ULTIMATE Frontend Toolchain? (Replace Vite)](../videos/IDHHDnWjhAc.md)
`IDHHDnWjhAc` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: dev-tools

Walkthrough of Bun 1.2.3's front-end toolchain: a template picker (bun init), a built-in router in Bun.serve, module-based hot reload, auto-installed deps, and bun create from a single file. Presented as a Vite replacement, but only the dev server is shown.

- Techniques: Scaffold a React + Tailwind + shadcn/ui app interactively; Routes in Bun.serve with dynamic params; Turn a single LLM-generated component file into a project; Find and install missing imports across source files
- Tools: Bun (1.2.3 cited), React, Tailwind CSS, shadcn/ui, Vite (named as the tool being replaced), Next.js (named as an alternative the presenter is moving away from), Svelte (plugin said to be coming), Vue (plugin said to be coming), Cursor (used to write components), framer-motion (installed by the analysis step), Anthropic (chat link import idea)

## [This AI Code Builder ACTUALLY Works (backend too!)](../videos/4ASZpNNG0f4.md)
`4ASZpNNG0f4` · Better Stack · 2025-11-02 · q2 · intro · review · also: dev-tools

Hands-on test of AI app builders on one backend-heavy prompt; Convex's Chef produced working auth, storage and database from a single prompt, while Firebase Studio, Bolt.new (with Supabase) and v0 failed or stalled.

- Techniques: One long, feature-complete prompt, then test each feature end to end; Bring your own model key to avoid builder token markup
- Tools: Chef by Convex, Convex (backend, dashboard, file storage, auth, durable functions), Bolt.new, Firebase Studio (preview), v0, Supabase, Anthropic API (BYOK)

## [Google's New AI Code Editor Built My Flutter App in the Browser!"](../videos/P4xA6j3B39U.md)
`P4xA6j3B39U` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents

Hands-on review of Google's browser-based Project IDX: the host builds a Flutter task-manager app with its Gemini chat, and reports that fixes needed repeated prompting and manual insertion.

- Techniques: Full-file repair loop; Explicit insert prompt; Observable-symptom prompt; Review diff before applying; Setup steps for the browser IDE
- Tools: Project IDX, Gemini, Flutter, VS Code, Cursor, Windsurf, Expo, Next.js, Python, Go, Node.js

## [Why Isn't Anyone Talking About This Vibe Coding Tool?](../videos/BXBwikXMb6Q.md)
`BXBwikXMb6Q` · AI LABS · 2025-11-02 · q2 · intro · review · also: dev-tools

A walkthrough of Convex's Chef, a prompt-to-full-stack-app builder, using it to make a Splitwise clone and a tool-rental app; the main takeaways are that prompt detail up front matters and that text-only prompting is a real limitation.

- Techniques: Front-load a comprehensive prompt; Bring your own API key when quota runs out, then re-prompt; Start from a preset and adjust the prompt; Verify by walking through the core flows; Export and run locally
- Tools: Chef (Convex's AI app builder), Convex, Lovable, Supabase, Bolt.new, v0 (Vercel), ChatGPT, Anthropic API (Claude), React, TypeScript

## [I Built 5 Websites Without Touching HTML:  Here's How (Kibo UI)](../videos/6odlDS7-G8k.md)
`6odlDS7-G8k` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: mcp-and-tools, coding-agents, context-engineering

Tutorial on wiring the shadcn MCP server and a custom 1100-component Kibo UI registry into a coding agent, plus TweakCN's live-embed theming flow for building Next.js UIs.

- Techniques: Wire the shadcn MCP into a Next.js or React project; Host a custom component registry from shadcn's registry template; Category-guided component selection for very large catalogs; Two-command design-first workflow (init once, build per session); Embed a TweakCN live theme preview into a Next.js app
- Tools: shadcn, shadcn CLI, shadcn MCP server, shadcn registry template, Kibo UI (patterns registry, ~1100 components), TweakCN, TweakCN MCP server, Next.js, React, Claude Code, Cursor, components.json

## [This Tool Codes for FREE – Here’s How to Install It!](../videos/xsJAA3vhy0E.md)
`xsJAA3vhy0E` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, dev-tools

Install-and-try walkthrough of Bolt DIY, a self-hosted, free alternative to Bolt.new, driven by DeepSeek V3 through OpenRouter. The demo works for a whiteboard app, but shapes stay broken, and the title overstates what is free.

- Techniques: Clone, install and run Bolt DIY locally; Configure OpenRouter as the provider with DeepSeek V3; Set a model from the dropdown and check its voice and image support; Iterate with one bug per follow-up prompt
- Tools: Bolt DIY (bolt.diy), Bolt.new, DeepSeek V3, DeepSeek chat, deepseek-coder, OpenRouter, ShadCN UI, Claude 3.5 Sonnet, Perplexity AI, Hugging Face, pnpm, git

## [How to Use Figma AI To Make Sites 10X More Beautiful](../videos/_-FEgdQ_L4I.md)
`_-FEgdQ_L4I` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: mcp-and-tools, context-engineering

A walkthrough of a prompt-chained Figma Make workflow for planning and generating a React app, then converting it with a coding agent and feeding Figma designs to agents through the Dev Mode MCP server.

- Techniques: Plan-first prompt chain for Figma Make; Universal full-stack conversion prompt; Figma Dev Mode MCP setup; Implementation-rules configuration file; Screen triage before implementation; Add shadcn MCP for component context
- Tools: Figma Make, Figma desktop app (Dev Mode), Figma Dev Mode MCP server (local and remote variants), ChatGPT (web interface, for planning and prompt outputs), Warp (Warp Code agent, referred to as Warpcode in captions), Supabase, React, Next.js, GitHub, shadcn MCP server, shadcn/ui, Aceternity UI

## [I Tried Building an Expo App in 360 Seconds… Here’s What Happened](../videos/Dmgu7jE2toM.md)
`Dmgu7jE2toM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, context-engineering

Walkthrough of a two-tool flow for Expo mobile apps: Tempolabs generates the PRD, user flow and wireframes, then Cursor takes over the code via a synced docs folder. Single-project demo with no measurements.

- Techniques: PRD and user flow from a requirements prompt; Connect the builder to the IDE via the Tempolabs extension; Commit the spec into the repo as context for the coding agent; Route stubborn bugs to the agent that made the code; Verify gestures on a device, not the desktop preview
- Tools: Tempolabs, Cursor, Expo, Expo Go, Gemini 2.5 Pro, ChatGPT, Mermaid, Windsurf, Next.js, Supabase, Stripe, SSH

## [Llama Coder: Is is WORTH It? Tested for Full-Stack App Building!](../videos/T5fIdojtR3A.md)
`T5fIdojtR3A` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents

Hands-on test of Llama Coder, a free open-source prompt-to-app builder on Together AI. It improved after switching to Llama 3.3 but still fell short of Cursor, Windsurf, Bolt.new and v0.

- Techniques: Run Llama Coder locally from the GitHub repo; Paste runtime errors back into the change prompt box; Switch the generation model from the dropdown; Enable the ShadCN UI toggle; Publish and share the generated app; Use the built-in placeholder prompt for a calculator
- Tools: Llama Coder, Together AI, Llama 3.3, Llama 3.1, Qwen 2.5 Coder, Gemma 2, ShadCN UI, ChatGPT, Claude 3.5 Sonnet, GPT-4 Omni, Gemini, Cursor

## [The Windsurf vs Cursor rivalry just reached a turning point](../videos/gejEvBWbgHA.md)
`gejEvBWbgHA` · AI LABS · 2025-11-02 · q2 · intro · news · also: coding-agents, product-ux

Windsurf feature tour: select a live page element in the preview, describe the change to Cascade, and it edits the code. Also covers Tab to Import, linter integration, suggested actions, built-in MCP docs and admin model controls. Mostly unmeasured demos.

- Techniques: Select-and-describe UI edits; Batch section edits for animations; Let the agent fix its own build errors; Drag files into the agent instead of referencing them
- Tools: Windsurf, Cascade, Cursor, Claude 3.7 (thinking mode, as named by the host), GPT-4.5 (as named by the host), DeepSeek V3, MCP

## [Gemini 2.0 Flash: Is Google Taking Over Code?](../videos/5Z42W5AK6JU.md)
`5Z42W5AK6JU` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents

Hands-on tutorial that builds small apps with Gemini 2.0 Flash through the Aider and Cline coding agents, with setup steps and a candid note on the output's gaps. Thin on analysis despite its "is Google taking over code" title.

- Techniques: Aider with a Gemini default via .env; Cline on OpenRouter to avoid provider rate limits; Iterative prompting to finish a scaffold
- Tools: Gemini 2.0 Flash, Aider, Cline (formerly Claude Dev), VS Code, OpenRouter, Google AI Studio, shadcn/ui, Claude, GPT-4

## [We Tested Google’s New AI Coding Tool Opal (Honest Review)](../videos/Uz3p1dovTeo.md)
`Uz3p1dovTeo` · Better Stack · 2025-11-02 · q2 · intro · review · also: product-ux

Hands-on review of Google's Opal, a node-based no-code tool for building AI "mini apps" from text prompts. The reviewer finds weak output control, broken image embedding, and no real sharing or embedding path.

- Techniques: Precise API-naming node prompt; Separating a broken image from a bad URL; Re-running to measure variance
- Tools: Google Opal, Gemini, Imagen 4 (heard as Imogen4 in captions), Google Maps API, Google Maps Static API, Google Search, Claude Code (heard as Cloud Code in captions), Kiro, Spark

## [Bun 1.2 is a HUGE update (its a bundler now!)](../videos/rtj-zd93Vfs.md)
`rtj-zd93Vfs` · Better Stack · 2025-11-02 · q3 · intro · news · also: dev-tools

Walkthrough of Bun 1.2's release notes: HTML-import bundling, built-in Postgres and S3 clients, a text lockfile, Node compatibility gains, a richer test runner, and cross-compiled executables. Mostly vendor-reported numbers.

- Techniques: Serve a bundled frontend straight from Bun.serve via an HTML import; Presigned S3 URLs so the server never relays file bytes; Put dependency pins and reasons in package.json comments; Review dependency changes as text diffs; Patch a broken dependency locally and commit the .patch file; Wire CI test reporting through JUnit or LCOV output; Cross-compile a standalone executable and enable bytecode caching
- Tools: Bun 1.2, Bun.serve, Bun SQL (Postgres client), postgres.js, Bun S3 client, AWS SDK for JavaScript, Bun test, bun outdated, bun publish, Tailwind CSS, Bun Tailwind plugin, Express

## [Generate The PERFECT App UI Every Time with this 2-Step Cursor Guide](../videos/H-ok6Zx9SR8.md)
`H-ok6Zx9SR8` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: coding-agents, context-engineering

AI LABS tutorial on generating varied app UI designs inside Cursor with manually invoked rule files, replacing a paid-API design extension, with a Claude Code port and a plain-English method for writing rule files.

- Techniques: Manual-mode Cursor rule files as invocable workflows; Extract a design.json from a reference image; Targeted variation rules (persona, device, geolocation); Infinite-design iteration loop; Fresh chat per generation round; Writing rule files in plain English; Porting a rule to Claude Code custom commands
- Tools: Cursor (rules, agent, .mdc rule files), Super Design Dev (Cursor extension by Jason Zhao), Claude Code (custom commands, parallel agents), Claude 3.5 Sonnet, Anthropic Claude API

## [AI Coding with Cursor & Claude: Build Apps That People Keep Using in 5 Simple Steps](../videos/i_31WoayEIo.md)
`i_31WoayEIo` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: context-engineering, product-ux, mcp-and-tools

Tutorial on building a photo-cleaner iOS app with Cursor and Claude: user journey saved in a markdown file, HTML prototype, palette, fonts, icon, Swift port and animations guided by Context7 docs.

- Techniques: Persistent context files in the repo; Specify the user journey first, then build an HTML prototype; Palette-from-elements prompt sequence; Google Fonts embed into the HTML prototype; App icon via ChatGPT image model with palette constraint; Context7 MCP for framework docs; Fresh chat per task plus Cursor to-do list; Two-stage animation pipeline; Screenshot-driven bug fixing
- Tools: Cursor, Windsurf, Lovable, bolt.new, Claude Code, Gemini CLI, Claude, ChatGPT, ChatGPT image model (called ChatGPT 4 image model in the video), Context7 MCP, Google Fonts, HTML

## [Program Claude Code to be your new UI Designer (+ works with any IDE)](../videos/TyGx277x9hQ.md)
`TyGx277x9hQ` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: claude-code, coding-agents, context-engineering

Walkthrough of using Claude Code plus ChatGPT planning to turn an HTML UI prototype into a SwiftUI iOS app and re-skin it in Apple's Liquid Glass style; practical but anecdotal.

- Techniques: Plan-in-chat, then execute in agent; Screenshot-to-HTML prototype; Conversion rules file; Style transfer from references; Visual bug reporting; Start from the native project template
- Tools: Claude Code, Claude 4 Sonnet, Claude Opus (Claude 4), Cursor (Max mode), ChatGPT, Xcode, SwiftUI, Swift, Next.js, HTML/CSS, iOS Simulator, Apple Liquid Glass design

## [Expo, AI, and the Future of Mobile Development with Beto | Better Stack Podcast Ep. 6](../videos/kIU7rdHz2XE.md)
`kIU7rdHz2XE` · Better Stack · 2025-11-02 · q3 · practitioner · interview · also: dev-tools

Expo developer advocate Beto on React Native in 2025: safe OTA updates with EAS Update, prebuild instead of eject, store submission, and the Flutter-vs-RN debate. Vendor-side anecdotes, little AI content.

- Techniques: Ship JS-only fixes with EAS Update and expo-updates; Check native compatibility before each OTA bundle; Prebuild instead of ejecting; Iterate in Expo Go, then switch to a dev build; First store submission with Expo Launch; Add widgets, Live Activities and Apple Watch targets with Apple Targets; Generate app icons from one source image with SnapAI
- Tools: Expo, Expo Launch, Expo Go, EAS Update, expo-updates, Expo UI, Expo Router, Expo API routes, Expo modules (native module API), React Native, React Native Skia (Shopify), React Native macOS and Windows (Microsoft)

## [The BEST Way To Start a Project (Better-T-Stack)](../videos/CWwkWJmT_zU.md)
`CWwkWJmT_zU` · Better Stack · 2025-11-02 · q2 · intro · review · also: dev-tools, coding-agents

A Better Stack walkthrough of Better-T-Stack, a scaffolder that builds a full TypeScript monorepo (TanStack Router, Hono on Bun, oRPC, Postgres, Drizzle, Better Auth) from one command, with auth working on first run.

- Techniques: Scaffold a full-stack TS monorepo from a builder; Bring up the stack locally; First-run smoke test of the full path; Hand the scaffold to a coding agent
- Tools: Better-T-Stack (scaffolder with website Builder and CLI), TanStack Router, Hono, Bun, oRPC, tRPC (listed as an alternative API layer), PostgreSQL, Docker / Docker Compose, Drizzle ORM, Prisma (listed as an alternative ORM), Better Auth, Turborepo

## [3 Ways to Build ACTUALLY Beautiful Websites Using Cursor AI](../videos/djDZHAi75dk.md)
`djDZHAi75dk` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: product-ux

Three Cursor workflows for less generic AI-built sites: clone a reference design via an extracted design JSON, theme shadcn/ui with TweakCN, and drop in React Bits components, plus font and layout prompting tips.

- Techniques: Reference design to JSON design system, then build from it; TweakCN theme to shadcn/ui project; Drop a copied component into a named section; Font via embed code; Spec the layout explicitly and keep it in a file; Animation restraint
- Tools: Cursor, Claude, ChatGPT, TweakCN, shadcn/ui, React Bits, Aceternity UI, Google Fonts, Next.js, framer-motion, React, HTML

## [Claude Code Can Finally Make Beautiful Websites](../videos/idccdssOZQ8.md)
`idccdssOZQ8` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: product-ux, coding-agents

Three UI design principles (depth through layered color and shadows, box-based responsive layout, and a four-role color palette) for making AI-generated sites look better, shown on a cloned Airbnb-style page.

- Techniques: Color-layer depth instead of borders; Dual shadow with depth levels and a gradient; Flexible box layout with parent-child structure; Priority-based responsiveness; Four-role palette; Prompt per principle, with before/after comparison
- Tools: Claude Code (named in the title only; the transcript does not name it), Colors (palette-browsing site, named in the transcript, no URL given), Airbnb-style page clone (demo subject, not a tool)

## [Clone Any Website INSTANTLY! New V0 Updates You Need to See.](../videos/gNgxnECvLWM.md)
`gNgxnECvLWM` · AI LABS · 2025-11-02 · q2 · intro · review · also: testing-verification

Walkthrough of v0's new URL-to-clone, built-in console logs, version rollback and click-to-edit features, shown on one Notion homepage clone; thin substance behind a hype title.

- Techniques: Clone a page from its URL; Log-driven debugging loop; Roll back and rebase on a known-good version; Scoped edits by element selection
- Tools: v0

## [I'm Never Vibe Coding Without Next JS Agents Anymore](../videos/yJv2JRM--ws.md)
`yJv2JRM--ws` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools, coding-agents

A walkthrough of building a full-stack Next.js agent marketplace with Claude Code and three MCP servers (Supabase, ShadCN, Stripe), driven by a PRD and per-MCP prompts. The reusable parts live in linked resources, not on screen.

- Techniques: One-command MCP wiring with a /mcp health check; PRD to converter prompts, one per MCP; Dependency-ordered single-session build; Component-grounded UI with a theme and a usage slash command; Static UI first, then a separate wiring pass; Mock-then-real payment verification
- Tools: Claude Code, Cursor, Next.js, Supabase (MCP server), ShadCN MCP, shadcn/ui, TweakCN, Stripe (MCP server, Stripe checkout), ChatGPT (used for the PRD brainstorm)

## [Build FRONTEND Faster Than Ever with This Cursor MCP Setup!](../videos/DpdM4xei5fw.md)
`DpdM4xei5fw` · AI LABS · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, coding-agents

A 6-minute walkthrough of the 21st.dev / Magic UI MCP server inside Cursor, showing component generation, logo search and catalog install for frontend work.

- Techniques: Install an MCP UI server into the IDE; Prompt for a self-contained component, then let the IDE agent place it; Use logo search to fill in brand or icon assets; Install a catalog component by copying the command
- Tools: 21st.dev (Magic component builder, logo search, component inspiration, UI catalog), Magic UI, Cursor, Windsurf, Cline (called "Klein" in the auto-captions), VS Code, React, TypeScript, MCP (Model Context Protocol), WSL, v0 (mentioned as the comparison point for the component builder), ChatCN (named by the host as a UI library source; spelling from auto-captions, not verified)

## [Build Sites That Sell 99% of Products with Claude AI](../videos/VtmBevBcDzI.md)
`VtmBevBcDzI` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: claude-code, context-engineering

A landing-page design walkthrough: reverse-engineer a strong v0 site, then steer Claude Code with named libraries (paper shaders, Framer Motion), Google Fonts, layout screenshots and SVG code. Mostly a practical tip list with a sponsor segment.

- Techniques: Reference-site reverse engineering; Named-library prompt with a focused context; Framer Motion for animations; Two-step gooey morph; One-word font accent; Layout from a gallery screenshot; SVG logos and icons as code
- Tools: Claude Code, v0, Cursor (mentioned as a tool to use, no steps shown), Paper Shaders (library for animated website backgrounds), Framer Motion (React version named), GitIngest ("Git Ingest", converts a repo to AI-readable text), Google Fonts, Landbook (layout and design gallery), ChatLLM by Abacus (sponsor)

## [6 INSANE Repos I Wish I Knew Before...](../videos/tmj4_HhX7jI.md)
`tmj4_HhX7jI` · AI LABS · 2025-11-02 · q2 · intro · review · also: claude-code, mcp-and-tools, context-engineering

Six-repo roundup for Claude Code and MCP: awesome-claude-code, BMAD agile agents, UI component libraries, GitMCP, FastAPI-MCP and mcp-use. Mostly quick pitches plus a mid-video sponsor segment.

- Techniques: Repo to remote MCP server via GitMCP; Expose FastAPI endpoints as MCP tools (fastapi_mcp); Use an MCP server from code with mcp-use; Repo dump into markdown as Claude Code context; BMAD staged agile agents; Pick UI components with the agent; Parallel Claude Code sessions and usage monitoring
- Tools: Claude Code, Claude Desktop, Claude Squad, Claude Code usage monitor, awesome-claude-code, BMAD method, Cursor, shadcn/ui (ShadCN), awesome-ui-component-library, Ant Design, Recharts, Next.js

## [The 1 Click Solution to PRESENTATION PERFECTION No One Tells You!](../videos/de71tQ3k5xA.md)
`de71tQ3k5xA` · AI LABS · 2024-11-02 · q2 · intro · tutorial · also: product-ux

Step-by-step walkthrough of generating a slide deck from pasted notes in Gamma AI, covering input methods, generation settings, and editing images and layout.

- Techniques: Generate a deck from pasted notes in Gamma; Replace a generated image; Reorganize a card's information layout; Keep AI-generation cost in check
- Tools: Gamma AI (gamma.app web app), Flux (image model used by Gamma for AI image generation, default option), Google account sign-in, PowerPoint (mentioned only as the familiar format being replaced)

## [Get Started with Cursor: The AI Code Editor That Lets You Build Without Coding](../videos/NtGagWyY1kU.md)
`NtGagWyY1kU` · AI LABS · 2024-11-02 · q2 · intro · tutorial · also: coding-agents

A 5-minute beginner walkthrough of the Cursor AI code editor: install, set up, use Ctrl+L chat and Ctrl+K inline edits to generate and modify small Pygame games. Thin, hype-framed, no review of output quality.

- Techniques: Chat-first prototyping of a small game; Inline edit with prompt, Apply, Accept; VS Code migration at setup; Toggle AI features and bring your own model key
- Tools: Cursor, VS Code, Python, Pygame

## [Discover the SECRET tool that unlocks UNLIMITED generations with the Flux model!](../videos/DiMliAtLc2M.md)
`DiMliAtLc2M` · AI LABS · 2024-11-02 · q2 · intro · review · also: —

Walkthrough of PicLumen, a web image generator that offers Flux and other models, covering reference images, inpainting and Hugging Face prompt building; the "unlimited" title is contradicted by the speaker's own caveat.

- Techniques: Character-consistent generation from one reference image; Style-consistent generation; Region inpainting; Building a Flux prompt with the Hugging Face prompt generator
- Tools: PicLumen (web image generator; the transcript spells it Pick Lumen / PIC Lumen), Flux (image model, lower-tier version on PicLumen), PicLumen line art model, PicLumen anime model, Hugging Face prompt generator for Flux

## [Bolt.new Tutorial Website – Replaces Cursor, Claude & v0 – The Only AI Tool You Need!](../videos/6-sTKmPl4wA.md)
`6-sTKmPl4wA` · AI LABS · 2024-11-02 · q2 · intro · review · also: coding-agents

A 7-minute walkthrough of Bolt.new, a browser tool that generates a React website from a text prompt, then iterates on it through chat; the transcript shows real friction (vague prompts, missing images, out-of-credits).

- Techniques: One-prompt scaffold, then chat-driven iteration; Name the exact effect or fix instead of describing a mood; Copy build errors back into the chat; Check generated assets and sections by eye
- Tools: Bolt.new, React, V0, Cursor, Replit (comparison only), Claude (UI resemblance only)

## [I Built an App in 10 Minutes WITHOUT Coding! | Using Cursor Composer](../videos/LrIhNW2BN28.md)
`LrIhNW2BN28` · AI LABS · 2024-11-02 · q2 · intro · review · also: coding-agents, context-engineering

Short Cursor promo that builds a budget tracker and a task app from plain-text requirements with Composer; shows multi-file generation, but the evidence is two cherry-picked demos.

- Techniques: Requirements file, then generate; Enable Composer before first use; Generate, then re-prompt for design, then fix bugs; Scope chat with @-references; Ctrl+K for local edits
- Tools: Cursor, Cursor Composer, Cursor Tab (completions), Cursor Chat (@-references), Cursor Ctrl+K inline edit

## [Fragments by E2B: The FREE AI Tool Surpassing Bolt.new & v0.dev?](../videos/Au5ixSJ4C3w.md)
`Au5ixSJ4C3w` · AI LABS · 2024-11-02 · q2 · intro · review · also: —

A short walkthrough of Fragments by E2B, an open-source Claude Artifacts-style tool that turns prompts or screenshots into live-previewed UI, with a free-tier and local-run note.

- Techniques: Iterative prompt-to-UI with targeted fix prompts; Screenshot-to-clone prompt; Persona-first generation; Local run from the open-source repo
- Tools: Fragments (by E2B), E2B, Claude Artifacts, Claude, Gemini (website used as the clone target), Google sign-in, Bolt.new (named in the title and intro only), v0.dev (named in the title only)

