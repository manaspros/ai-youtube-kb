# skills-self-improvement — 131 videos

*agent skills, skill libraries, self-improving / learning agents, procedural memory*

By channel: AI Engineer 79 · Kai Explains 4 · AI LABS 38 · Better Stack 10

**Synthesized guide:** [guides/skills-self-improvement.md](../guides/skills-self-improvement.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [This Is Microsoft's New Tool Finally Fixed Claude's Usage Limits](../videos/1kQ_1_QL5Es.md)
`1kQ_1_QL5Es` · AI LABS · 2026-10-29 · q2 · practitioner · review · also: token-cost-efficiency, claude-code, context-engineering

Walkthrough of Microsoft's Token Economizer, a Claude Code plugin that learns per-project token waste (repeated mistakes, unused tools, stuck loops) and cuts it; reports 21-31% savings and a cold-start caveat.

- Techniques: Install the plugin for your agent; Enable micro skills only for your own projects; Per-project repeated-failure facts; Prune unused tools per project, then restore on demand; Measure the tool-definition overhead; Two-step stuck escalation; Seed a new tool from existing session history; Three-hook layout for an agent harness
- Tools: Token Economizer (Microsoft; Claude Code and Codex plugin, install from GitHub repo, version not stated), Claude Code, Codex (OpenAI), GitHub Copilot, Sonnet 5, Opus 4.8, Graft (map-based token saver, mentioned as a comparison, not shown in use), Data Impulse (sponsor; residential proxy network)

## [Exploits Now Beat Patches: Open Source Security in the AI Era - Patrick Smyth, Chainguard](../videos/xZX3pmaB8Hk.md)
`xZX3pmaB8Hk` · AI Engineer · 2026-10-28 · q3 · practitioner · review · also: security-guardrails, dev-tools

Chainguard's Patrick Smyth argues frontier AI has made exploits beat patches: cooldowns, signed artifacts, tiered SLAs, minimal rebuilt images and vetted agent skills, wrapped in a vendor pitch.

- Techniques: Package cooldown period; Sign and verify every artifact; Build dependencies from clean source; Severity-tiered remediation SLA; Minimal, frequently rebuilt base images; Treat CI/CD as an attack surface; Vet agent skills before use; Hardware-backed developer identity
- Tools: Chainguard (vendor), Wolfi (Chainguard's rolling Linux distro), Chainguard Libraries (build-from-source packages), Chainguard Actions (hardened CI/CD actions), Chainguard agent skills (hardened third-party skills), Sigstore, SLSA (captioned 'Salsa'), Mandiant mTrends report (captioned 'Mandia'), Trivy (scanner, captioned 'Trivi', attacked in the supply chain incident), Grype (captioned 'Gripe', scanner named as an example), LiteLLM (captioned 'LightedLM', described as an agent router), Axios (npm package, compromised)

## [Agents That Self Improve While You Sleep - Fuad Ali, Arize AI](../videos/UGuNt2_Oz8s.md)
`UGuNt2_Oz8s` · AI Engineer · 2026-10-27 · q3 · practitioner · workshop · also: evals, observability, pr-code-review

A vendor-led workshop on closing an agent self-improvement loop: scheduled trace review, failure datasets, evals, replay experiments, and human checkpoints at the high-leverage points.

- Techniques: Trace-to-fixture pipeline; Trajectory-level LLM-judge eval; Cheap-first evaluator stack; Replay-based fix validation; Confidence-threshold human routing; Session-level eval signals; Stop criteria for eval depth
- Tools: Arize AX (tracing and evals platform), AX CLI, Arize Signal (always-on trace-review agent), Arize Alex (in-house agent), Phoenix (mentioned, not demonstrated), Arize managed sandboxes, GitHub, Codex, Cursor, Claude Code, OpenCode, Modal

## [Google's Harness² Is This the End of Harness Engineering?](../videos/yCgfyQmqhPM.md)
`yCgfyQmqhPM` · Kai Explains · 2026-10-24 · q4 · practitioner · review · also: context-engineering, evals, token-cost-efficiency

Critical read of Google's Harness² paper, where a second model rewrites an agent's harness files through a Propose/Probe/Compose loop. Headline gains are measured against an empty harness with a frontier editor, and token cost runs 8x to 40x a plain run.

- Techniques: Propose, Probe, Compose harness editing; A/B probe before keeping any harness edit; Trigger line on every skill; Place guidance by cost: skill, then script, then sub-agent, then plugin, then always-on text; Reopen-and-verify rule before declaring done; Exact output path and filename rule; Forbid plain-text tool calls; Restrict network before running a self-improvement loop; Put a cap on multi-run loops
- Tools: Harness Square (Google Cloud AI Research paper, Oct 2026), GLM-5 (Z.ai), Gemini 3.5 Flash, Claude Opus 4.8 (editor and judge in the paper), Claude Code, OpenCode, CodeBuddy, Codex (OpenAI Codex agent), MetaHarness (Hugging Face legal tool), WorkBuddy (benchmark), Jobbench (benchmark), Harvey legal agent benchmark

## [AI Just Made Physics Interactive. This Is Insane. (Anatomy)](../videos/lyGYidIZK4I.md)
`lyGYidIZK4I` · Better Stack · 2026-10-22 · q3 · practitioner · review · also: coding-agents, claude-code, token-cost-efficiency

Better Stack demos "anatomy", an agent skill that explains concepts as physical machines in interactive HTML/SVG/React figures; useful, but very slow, token-hungry, and its metaphors need checking.

- Techniques: Install and invoke the anatomy skill; Truth-first figure generation; Steering the output with modifiers; Verify the metaphor and the draft; Budget before running
- Tools: anatomy (Claude skill, tool name as spoken in the video), skills CLI, Claude Code, Codex, OpenCode, Antigravity, Chrome, WebGL, React, SVG, Mermaid, D2

## [The AI Content System Behind 200M Views — Sarah Chieng, Cerebras & Cova Lee, OpenAI](../videos/CFbnVpSsDFQ.md)
`CFbnVpSsDFQ` · AI Engineer · 2026-10-22 · q3 · practitioner · workshop · also: context-engineering, voice-multimodal, product-ux

Two creators (Cerebras and OpenAI DevEx) walk through a six-stage AI content pipeline: swipe-file ideation, voice-captured scripts, shot lists, agent-driven editing, captioning, scheduling and a periodic process-review skill.

- Techniques: Swipe-file reference library for agents; Build a voice skill from your own past content; Voice-first script interview; Outlier analysis against channel baseline; Two-pass shot list from a script; Organize footage before editing; Agent-driven editing via API or desktop control; Brand design system generated from your own videos; Background and visual enhancement with image generation; Fix mistakes with short inserts; Repurposing into short-form cut-downs; Scheduling with human approval; Remove AI tells from captions and prose; Weekly process-review skill
- Tools: ChatGPT, Codex (CLI, computer use; transcribed as 'Astra/Astro'), GPT-5.6 Sol Ultrafast (as named in the talk; runs on Cerebras at ~750 tokens/sec), Cerebras, Wispr Flow (transcribed as 'whisper flow'), Figma (MCP and plugins), Notion, Obsidian, HyperFrames (HeyGen), HeyGen (avatars), CapCut, Adobe Premiere

## [GitHub's #1 Trending Skill Is Insane (5 Use Cases)](../videos/rw0fqnrZgNM.md)
`rw0fqnrZgNM` · AI LABS · 2026-10-19 · q2 · practitioner · review · also: claude-code, testing-verification, security-guardrails

Walkthrough of the Reverse Engineer Anything (REA) MCP skill for Claude Code: feature cloning, black-box QA, competitor teardown, security sweep. Takeaway: tag findings by evidence, not guesses.

- Techniques: Behavior spec before implementation; Evidence-tagged findings; Black-box feature QA; Check the site against your written rules and promises; Competitor teardown; Pre-publish security and performance sweep
- Tools: Claude Code, Codex, Reverse Engineer Anything (REA) MCP server and skill, Hopper (binary analysis, optional), Firecrawl MCP server (sponsor), Notion MCP, Obsidian, Notion, OpenAI API, Stripe, GitHub

## [Google Just Fixed AI Design By Releasing This](../videos/au2TI8sdq8E.md)
`au2TI8sdq8E` · AI LABS · 2026-10-19 · q3 · practitioner · tutorial · also: coding-agents, context-engineering, testing-verification

Google's Stitch design tool now has a terminal CLI, so Claude Code can drive it through a brief-to-design-to-site workflow with review and story-review skills; the video is a tutorial-style walkthrough with a sponsor segment.

- Techniques: Stitch CLI install with the skill in .claude; brief.md interview before any design generation; Loop of generate, check, and re-prompt in Stitch; Build from Stitch via download of HTML, images and fonts; Two-stage review: design fidelity, then story quality
- Tools: Stitch (Google), Stitch CLI, Claude Code, Stitch skill, scrollytelling skill, design.md, brief.md, Whisperflow (sponsor)

## [AI Is Merging Video Games Now (here's how)](../videos/9dDJq1LGBAw.md)
`9dDJq1LGBAw` · Better Stack · 2026-10-19 · q3 · intro · review · also: coding-agents, multi-agent, token-cost-efficiency

Better Stack demos Universal Modder, an open-source Claude Code plugin that builds GTA 5 mods from games you own via recon, hot reload, in-game testing and shared field notes; ~$68 API cost.

- Techniques: Back up and log before touching user state; Fingerprint before coding; Parallel narrow research sub-agents; Write a converter for proprietary asset formats; Hot-reload the logic, not the host; Screenshot check after each reload; Draw new content as a post-process overlay; Field note plus shared KB PR
- Tools: Universal Modder (Rayhan; open-source Claude Code plugin with skills, a CLI and a knowledge base), Claude Code, Claude Opus 5.5 (as stated in the video), Script Hook 5 (GTA 5 script loader), ReShade, FAL (image generation for sprites, textures, 3D models, sound and voice; made by an ex-FAL engineer per the host), OpenCode (wrote KB notes), Steam (game library)

## [6 Insane Trending GitHub AI Design Repos You Need to Use](../videos/NZjjmf3I6I4.md)
`NZjjmf3I6I4` · AI LABS · 2026-10-19 · q2 · practitioner · review · also: coding-agents, mcp-and-tools, multi-agent

Walkthrough of six GitHub repos that give coding agents design references, multi-viewport checks, design-token extraction, multi-agent page builds, app-store screenshots and launch-video generation. Mostly sponsored tool demos with little measurement.

- Techniques: Reference-first design with an awards MCP; Post-build responsive check with Responsively MCP; Design taste skills, chosen by scope; Extract and diff design tokens with Dembrandt; Generate app-store screenshots with a local editor project; Launch video with Brag, with a verification pass
- Tools: Awards MCP (awards setup and awards inspiration commands), Klein CLI (caption spelling; probably Cline), sponsor, Kleinpass (caption spelling; probably ClinePass), sponsor, open-weight model access, first-month discount link, Whisperflow landing page (probably Wispr Flow, used as a reference site), Butter.Video (animation reference site), Responsively (Mac app and MCP server), Genjutsu skills: Cast, Paint, Bunshin, taste skill and hallmark (previously covered by the channel), Dembrandt (skill, design.md output), App store screenshots skill and local editor, Brag / Bragg (brag command, Full Mode and Slim Mode), Hyperframes (video framework used by Brag Full Mode)

## [The Cost of Accessibility in AI — Jemima Abu, CAIS](../videos/ZccJsdOE54M.md)
`ZccJsdOE54M` · AI Engineer · 2026-10-15 · q3 · intro · talk · also: context-engineering, product-ux, testing-verification

Jemima Abu (CAIS) argues accessibility is cheaper when built in from the start with AI agents, backed by a one-off experiment (58% lower cost, one-third the time) using a custom accessibility skill.

- Techniques: Accessibility skill for coding agents; Pre-run self-audit against a checklist; Audit the codebase before introducing an agent; Reusable component library as an accessibility lever
- Tools: Figma, Chrome Modern Web Guidance skill, WebAIM (cited study)

## [Please… Enough with the Sloppy, One-Shot SaaS Replacements — Mahmoud Abdelwahab, Railway](../videos/oixzVKMAXG0.md)
`oixzVKMAXG0` · AI Engineer · 2026-10-13 · q3 · practitioner · talk · also: product-ux, coding-agents, testing-verification

Railway's Mahmoud Abdelwahab on why agent-built internal tools feel broken: agents skip product polish (autosave, optimistic updates, undo, URL state) unless asked, so encode taste in skills, reference existing pages, and force end-to-end verification.

- Techniques: Pattern-following via existing abstractions; Named UX patterns as explicit asks; Reference-page anchoring; Taste packaged as skills; End-to-end verification loop
- Tools: Railway, Payload CMS, TanStack, Claude Code

## [We Let Our Financial Planners Write the Agents — Matthew Ragone, Range](../videos/gpmze-6ueGU.md)
`gpmze-6ueGU` · AI Engineer · 2026-10-13 · q3 · practitioner · talk · also: enterprise-adoption, context-engineering, product-ux

A financial planner at Range explains how non-engineers wrote Claude skills that drafts client work, using a five-step method: pick, teach, pack, test, ship.

- Techniques: Five-step skill build method; Narrated walkthrough as skill source; Ask-first and never-do sections in a skill; Background drafting while the expert is busy; Owner plus non-author reviewer for shared skills
- Tools: Claude

## [Hill-Climbing Skills: Improve Agents Without Changing the Model — Shubhankar Srivastava, Browserbase](../videos/p7gaxmCUiIU.md)
`p7gaxmCUiIU` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: evals, agent-architecture, voice-multimodal

Browserbase's Shubhankar Srivastava shows an auto-research loop in which a doer agent and a teacher agent iterate on a strategy file until browser-agent tasks converge into reusable skill.md files that cut cost and latency.

- Techniques: Teacher-doer auto-research loop with strategy file; Converged output as a skill.md artifact; Binary success verifier with minimal guardrails; Scheduled sample runs and failure-triggered healing; Three-layer security for learned skills; Objective choice in the teacher's criteria
- Tools: Claude Agent SDK, Claude Code, Codex, Opus 4.8, Sonnet, Browserbase browse CLI, Browserbase SDK, Stagehand, Browse.sh, WebMCP, Karpathy auto-research, OpenClaw

## [Building Self-Learning Loops for Your Agent — Fuad Ali, Arize AI](../videos/fnuNVFgLjHA.md)
`fnuNVFgLjHA` · AI Engineer · 2026-10-12 · q2 · intro · workshop · also: observability, evals, software-factory

Arize workshop on closing an agent's detect, investigate, fix, verify loop using an always-on trace-analysis agent, coding-agent skills, harness-as-judge scoring and replay experiments; mostly a product walkthrough.

- Techniques: Continuous failure clustering over production traces; Join trace evidence with the code path; Plain-language harness-as-judge rubric with tool access; Failure-dataset replay with agent experiments; Alert-triggered agent investigation; Agent skills for trace analysis from the coding agent
- Tools: Arize Signal, Arize skills, Arize agent experiments, Claude Code, OpenAI Agents SDK, FastAPI, Datadog, GitHub, Cursor, Codex

## [Agent Speedrun — Elizabeth Fuentes Leone & Sandhya Subramani, AWS](../videos/YXiLj4tJt5A.md)
`YXiLj4tJt5A` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: agent-architecture, security-guardrails, mcp-and-tools

Hands-on AWS workshop: build a Strands customer-service agent with hooks (rate limit, deterministic blocks), lazy-loaded skills, steering guardrails, then deploy to AgentCore Runtime.

- Techniques: Per-request tool-call rate limiter via hooks; Deterministic input filter hook; Skills as on-demand markdown procedures; Steering handler (rule or LLM buddy); Externalised steering rules; Message-history inspection
- Tools: Strands Agents, Amazon Bedrock AgentCore (Runtime, Memory, Gateway, Observability), Amazon Bedrock, Amazon CloudWatch, AWS CDK / CloudFormation, AWS OpenTelemetry Distro, boto3, agent-control (open-source steering rules library), MCP, A2A, Jupyter / Workshop Studio

## [Let Your Agent Cook: Using Skills to Evaluate and Improve Your App — Ankur Duggal, Arize AI](../videos/_zUp6y9bDU8.md)
`_zUp6y9bDU8` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: evals, observability, coding-agents

Arize's Ankur Duggal argues agents need trace-based evals, then demos a coding agent (Claude Code plus Arize skills) turning production traces into failure analysis, datasets, evaluators and experiments.

- Techniques: Trace-to-dataset-to-experiment loop; Coding agent as eval workflow driver; Mixed evaluator set; Sampled online evals; Tailored evals from observed failures
- Tools: Arize AX, Phoenix, Claude Code, Codex, Cursor

## [Scheduled Agents, Dreaming and Q&A: Claude Managed Agents (Part 3 of 4) — Anthropic](../videos/qJtcEDc_WJU.md)
`qJtcEDc_WJU` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: agent-architecture, multi-agent, memory

Anthropic's live demo and Q&A on Claude Managed Agents covers multi-session orchestration, scheduled deployments, outcome rubrics, and "dreaming," a memory-store self-improvement pass that the speaker says still needs your own evals.

- Techniques: Fan-out one session per entity via a dispatch tool; Scheduled deployment of a standing agent; Outcome rubric with a max-iteration cap; Offline dreaming pass over past transcripts; Workspace-per-tenant isolation instead of BYOK; Memory store as a separate attachable resource
- Tools: Claude Managed Agents, Claude Console, Claude Code, Anthropic SDK / API, AWS Bedrock, GitHub, OpenTelemetry, Jira (Atlassian integration), Notion (external agents)

## [Turning Agent Memory Into Skills That Work — Will Lyon, Neo4j](../videos/XPj3mIKEtI4.md)
`XPj3mIKEtI4` · AI Engineer · 2026-10-09 · q3 · practitioner · talk · also: memory, data-engineering

Neo4j PM Will Lyon argues agent memory should be a typed, traceable context graph, and shows how to distill that graph into governed, step-by-step agent skills rather than static markdown.

- Techniques: Typed context graph as agent memory; Decision traces as reasoning memory; Scope-first skill distillation; Coverage and coherence checks on generated skills; Staleness-aware skill registry; Typed step schema for skills (APE)
- Tools: Neo4j Agent Memory Service (NAMs), Neo4j graph database, Agent Skills open standard (agentskills.io), APE skill protocol, MCP tools, SkillsBench

## [How a Remote Company Builds AI Fluency — Em Shreve, Automattic](../videos/3XI90A3ENSg.md)
`3XI90A3ENSg` · AI Engineer · 2026-10-09 · q3 · intro · talk · also: enterprise-adoption, mcp-and-tools

Automattic's two-week, in-person AI enablement cohorts (50% facilitated workshops, 50% real project work) and how they scale learning through alumni champions, meetups and a shared MCP and skills hub.

- Techniques: Two-week immersive cohort with a 50/50 split; Living curriculum; Internal MCP server as a shared hub; Tool-agnostic shared skills directory; Champions, regional meetups and ride-alongs; Staged post-program surveys
- Tools: Claude Code, Codex, open code, MCP, Zendesk, WooCommerce, WordPress AI

## [From 36% to 100%: How Self-Improving Agents Write Their Own Skills — Rafal Wilinski, Runlayer](../videos/u-o0sW9nwmk.md)
`u-o0sW9nwmk` · AI Engineer · 2026-10-08 · q3 · practitioner · talk · also: mcp-and-tools, security-guardrails

Rafal Wilinski (Runlayer) argues agents should distill successful and failed runs into skills, serve them via MCP as a governed company-wide library, and reports a 36% to 100% success jump after one distilled skill.

- Techniques: Trace-to-skill distillation; Learn from failures too; Checks before publishing a skill; Remote MCP skill registry with tool-based access; Group similar runs before distilling
- Tools: MCP, Claude Sonnet 4.6, Voyager, Chromium, AWS Lambda, npx skills

## [The Self-Improving OSS Agent Stack — Marc Klingen, Langfuse](../videos/TeErpYBUIeM.md)
`TeErpYBUIeM` · AI Engineer · 2026-10-07 · q3 · intro · talk · also: evals, observability

Langfuse co-founder on moving agent improvement from manual trace review to an AI-driven loop, where agents propose fixes and dataset/evaluator updates while humans set goals and gate changes, with a changelog-writer case study.

- Techniques: Online plus offline eval loop; Agent-proposed fix with human gate; PR review decisions as eval signal; Backtest candidate against baseline; Agent-maintained evaluators from error patterns; Scheduled batch loop over labeled production data
- Tools: Langfuse, Langfuse agent skills, GitHub pull requests, coding agent, Langfuse prompt management, Langfuse annotation queues

## [Harness Engineering: How to Build a Software Factory — Dru Knox, Tessl](../videos/X6l4lpA0_NY.md)
`X6l4lpA0_NY` · AI Engineer · 2026-10-07 · q3 · practitioner · talk · also: software-factory, agent-architecture

Drew Knox of Tessl on building a "software factory" through harness engineering: three loops (inner, outer, meta), a three-layer setup order, and how Tessl's skills registry and automation support it.

- Techniques: Three-tier loop design for agent quality; Issue-to-PR control plane for agents; Governed skills registry; Mistake-to-skill feedback; Repeated task to scheduled skill; Human-intervention metrics as the factory KPI
- Tools: Tessl, Tessl Agent, tessl launch, Linear, GitHub, GitHub Actions, Codex, Claude Code, Gemini

## [He Finally 10x Claude Code With This Method](../videos/qLfSDQ5NGh0.md)
`qLfSDQ5NGh0` · AI LABS · 2026-10-05 · q3 · practitioner · tutorial · also: claude-code, testing-verification, multi-agent

Walkthrough of a Karpathy-style loop for Claude Code: frozen checks, fresh builder subagents, and an outer loop that rewrites instructions from failure logs. The "10x" claim is not measured.

- Techniques: Loop-fit test before building a loop; Project-context skill as app memory; Write, review, approve, lock, and commit checks; Fresh feature-builder subagent per feature, with a results file; Karpathy-style keep-or-undo loop with program.md; Outer auto loop that rewrites instructions from failures; Wire-up and sweep instructions
- Tools: Claude Code, Karpathy autoresearch (Auto Research), Upstash Box (sponsor; per-agent cloud sandbox), Approve Checks (custom script), program.md, features.md (feature tracking file), results file (custom per-round log), Project Context skill (custom), build skill (custom), write checks skill (custom), auto loop skill (custom), feature builder agent (custom subagent)

## [Scale the Judgment, Not the Model — Andrew Orobator, Reddit](../videos/6MudaeKdBSk.md)
`6MudaeKdBSk` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · also: testing-verification, software-factory, context-engineering

Reddit's Andrew Orobator on scaling agent judgment rather than model size: encode institutional judgment as skills, work logs, personas and hard gates, verified by recordings, so coding agents can ship with less human review.

- Techniques: Skills as encoded review judgment; Work log plus commit-hook enforcement; Persona prompting for perspective; Recording-based agent QA; Rules-first funnel for LLM cleanup; OS-level gate with operator-only bypass; Three operating modes; Scheduled skill drift audit
- Tools: Codex, git pre-commit and commit hooks, CI, lint, screenshot-based model review

## [No, That's Not a Software Factory — Ryan Cooke, WorkOS](../videos/HvboD89DyQ8.md)
`HvboD89DyQ8` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: software-factory, mcp-and-tools, context-engineering

Ryan Cooke (WorkOS) on why a sandbox plus coding agent is not a software factory. Build around outcome metrics, webhook-driven product workflows, and an internal MCP gateway.

- Techniques: Outcome-based factory metrics; Webhook-driven ticket pipeline; Agent plan refresh after each step; Agent-drafted PRD with human approval gate; Context-rich MCP gateway; Session mining for skill gaps
- Tools: Linear, Slack, GitHub, Notion, Snowflake, Cloudflare sandboxes, Claude Code, Devin, OpenCode, MCP

## [Building Self-Improving Agent Software Factories — Suraj Gupta, Warp](../videos/TN3mj92oZ8I.md)
`TN3mj92oZ8I` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: software-factory, memory, token-cost-efficiency

Warp's Suraj Gupta on making agent software factories self-improve through outer-loop skill edits gated by PR review, agent-scoped versioned memory, and rule-based model routing for cost.

- Techniques: Outer-loop skill improvement with PR gate; Agent-scoped fact memory with provenance; Rule-based model routing by task class; Best-of-k model sampling to learn routing
- Tools: Warp, Oz (Warp cloud agent platform), Sentry, GitHub, Codex, Claude Code, Opus, Haiku, GLM, Qwen

## [Software Engineering Is Becoming Factory Engineering — Zach Lloyd, Warp](../videos/tUPPVhBBcoM.md)
`tUPPVhBBcoM` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: software-factory, pr-code-review, observability

Warp's founder argues software engineering is becoming factory engineering: agent loops run from triage to spec to implementation to monitoring, with humans gating stuck points and observer agents improving the skills.

- Techniques: Software factory loop with human gates; Triage routing by ambiguity; Product spec plus tech spec; Observer agent skill loop; Verification by running the product
- Tools: Warp, Claude Code, CI/CD, GitHub, Computer use

## [Insane GitHub Repos That 10x Your Codex And Claude Code Setup](../videos/Ua0APTMVcb8.md)
`Ua0APTMVcb8` · AI LABS · 2026-10-02 · q2 · intro · review · also: coding-agents, testing-verification, token-cost-efficiency

AI LABS tours eight GitHub tools that extend Claude Code and Codex setups: browser verification, terse output, design-skill search, planning, skill evals, and linting. Mostly README-level, with one sponsor segment.

- Techniques: Browser-verified completion check (Reticle); Staged image-to-3D reconstruction with self-comparison; Terse-output plugin with lifecycle hooks (Chisel); MCP-attached design skill search (UISkills); Interview-plan-review-verify loop (Ouroboros); Apple-native skill pack for iOS UI; Skill evaluation with Caliper; Rule-based anti-pattern guard (Antislop)
- Tools: Image-to-3JS skill (spoken 'image to 3JS', captioned 'Image23JS'; GitHub trending per the presenter), Reticle, Chisel, Caveman, Ponytail, UISkills, Manufact (sponsor; hosted MCP server deployment and publishing checks), mcp-use open-source SDK (captioned 'MCPUs'), Ouroboros, Apple SwiftUI skills repo (Liquid Glass skill, layout skill), Liquid Glass (Apple iOS 26 design system), Claude Code (plugins, hooks, Skill Doctor command)

## [Long-Horizon Agents Need Experiments, Not Just Prompts — Erina Karati](../videos/x4e5O9zN0TE.md)
`x4e5O9zN0TE` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: evals, memory, multi-agent

Long-running, stateful agents need controlled scenario suites, balanced scorecards and a ratchet loop, not just prompt tweaks; the speaker's case study is a game-village multi-agent system tuned by an outer auto-research loop.

- Techniques: Controlled scenario suite with ground truth; Balanced behavioral scorecard with guardrails; Frozen-harness ratchet loop; Structured run-trace logging; Importance-scored memory with a threshold cache; Provenance and confidence tags on memories; Separate episodic memory from current belief
- Tools: Project Paradox (in-house framework), RAG-backed per-agent memory, auto-research loop (Karpathy-inspired)

## [Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA](../videos/OA-Mc60Rboo.md)
`OA-Mc60Rboo` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: evals, context-engineering, training-finetuning-rl

GEPA's Lakshya Agrawal explains reflective, text-space optimization: LLMs read full rollout traces and rewrite prompts, skills or harness code, with a Pareto pool, beating GRPO on sample efficiency.

- Techniques: Reflective prompt / artifact optimization loop; Pareto candidate pool selection; Actionable side information from the evaluator; Three optimization modes in one API; Optimize the agent file itself; Repo skill learning from trajectories; Judge-then-agent data flywheel
- Tools: GEPA (open-source, includes the optimize_anything API and a skill-learning feature), GRPO (used as the RL baseline), Claude Opus, Claude Sonnet 4.5, GPT-5 mini, GPT-4.1, GPT-4.1 nano, Gemini Flash, mini-SWE-agent, Claude Code, Codex, LLM-as-judge

## [The Loop Is the Product — Roland Gavrilescu, Introspection](../videos/7taOQBfjDyE.md)
`7taOQBfjDyE` · AI Engineer · 2026-09-27 · q2 · intro · talk · also: evals, agent-architecture, product-ux

Introspection's Roland Gavrilescu argues self-improving agent loops should distill a team's taste into versioned recipes of evals, judges and skills, validated in production and measured as value per watt.

- Techniques: Trace pattern clustering to find signals; Agent-drafted judges with human calibration; Recipe diffs as reviewable candidates; Production A/B or bandit promotion; Per-model harness profiles
- Tools: Py.Recipes, Harbor, OpenClaw (originally CloudBot), Claude Code, Codex, Cursor, Cognition

## [The Dark Arts of Skill Engineering — Paul Bakaus, Renaissance Geek (Impeccable)](../videos/SQMCtZX3trg.md)
`SQMCtZX3trg` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: coding-agents, context-engineering, evals

Paul Bakaus (Impeccable) on building production agent skills as harness extensions: blind sub-agents, forced divergence, scripts, hooks and per-model builds, rather than prose alone.

- Techniques: Blind adversarial critique; Anti-attractor divergence; Register routing inside one skill; Cross-session skill memory; Scripts that print next-step instructions; Pre-tool-use blocking hooks for weaker models; Hook-driven feedback loop from a skill; Unskippable gates with logged results; Per-harness and per-model builds; Ablation testing of rules; LLM-as-user with a judge panel; Inverted judges
- Tools: Claude Code, Codex, Cursor, GitHub Copilot, Gemini, Playwright, skills.sh, npx skills

## [How We Built an Agent That Improves Itself — Zubin Aysola, Weights & Biases](../videos/XyV6bSMyq-I.md)
`XyV6bSMyq-I` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: evals, observability, agent-architecture

Weights & Biases walks through how its ARIA agent evaluates and improves itself: production traces become offline regression tasks, and the agent runs its own hill-climbing loop.

- Techniques: Eval flywheel from production traces; Byte-identical prod and research agent with a sync job; YAML-defined config variants; Three task simulation modes; Dual scoring: pass/fail plus pairwise relative scoring; Unconstrained sandbox for agent research loops
- Tools: Weights & Biases Weave, W&B Reports, ARIA agent, Claude Code, YAML task and config specs

## [Total Recall: Agent Memory and Harness Engineering — Ignacio Martinez, Oracle](../videos/xs-ob87TTzg.md)
`xs-ob87TTzg` · AI Engineer · 2026-09-20 · q3 · practitioner · workshop · also: memory, agent-architecture, context-engineering

Oracle workshop on agent harness design: a 30-minute framework for agent memory (files vs databases, memory types, context rot, skill promotion), then a hands-on notebook build, with heavy Oracle product promotion.

- Techniques: Hybrid storage split; Per-agent git worktrees for file edits; Context card; Toolbox / skillbox index with vector retrieval; LLM-enhanced tool descriptions; Patience (hysteresis) budget for agent loops; Skill promotion by distillation; Difficulty-based model routing
- Tools: Oracle Database (converged: JSON, relational, spatial, graph, vector), Oracle DBFS, Oracle Agent Memory Package (OAMP), LangChain Oracle DB integration, OCI Generative AI service, GitHub Codespaces, Grok 4.1 Fast Reasoning, HNSW vector indexes, git worktrees, Python 3.12 notebook

## [How We Solved Agent Building — Andrew Qu, Vercel](../videos/9dYcwOkpCE8.md)
`9dYcwOkpCE8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: agent-architecture, context-engineering, multi-agent

Vercel's chief of software traces an internal data-science agent from a mega-prompt, to a multi-agent chain, to one file-system agent with distilled skills, then introduces the Eve agent framework.

- Techniques: Decompose-then-collapse; File-system agent with minimal tools; Query-to-skill distillation job; Convention-based agent folders; Built-in run observability
- Tools: Vercel AI SDK, Eve, Vercel Workflows, Vercel Sandbox, Vercel Connect, bash-tool (npm), SkillsSH, Claude Code, Claude Opus 4.5, Snowflake, Next.js, Postgres

## [500 Skills, Zero Fine-Tuning: LinkedIn's Playbook for AI Agents — Ajay Prakash, LinkedIn](../videos/9wZpvF3QleU.md)
`9wZpvF3QleU` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: mcp-and-tools, context-engineering, coding-agents

LinkedIn's Ajay Prakash on an internal MCP server that serves tools plus self-contained markdown "playbooks" teaching coding agents company workflows, kept current by a PR-based self-update loop.

- Techniques: Playbooks as MCP-served instruction docs; Compose playbooks by reference; Session-end playbook self-update PR; Three meta tools for large tool catalogues; Central plus repo-local instruction split; Single pre-installed local MCP server with hourly auto-update
- Tools: MCP, Claude Code, GitHub Copilot, Cursor, Airflow, Jira, Slack

## [Agents Without Code: Skills, YAML, and Filesystems Replaced Python — Philipp Schmid, Google DeepMind](../videos/fjF8EKnxKCU.md)
`fjF8EKnxKCU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: agent-architecture, sandboxing-execution, security-guardrails

Philipp Schmid (Google DeepMind) rebuilds one GitHub PR-review agent three ways, moving from a hand-written Python loop to a hosted sandboxed harness driven by markdown files, and argues to delete orchestration code as models improve.

- Techniques: Agents-as-files layout; Bootstrap script for CLI dependencies; Credential injection through a network proxy; Single-call agent turn with server-side loop; Named custom agent; File-based memory and handoffs; Build-to-delete audit
- Tools: Gemini API, Interactions API, Antigravity (agent harness), Google Agent Development Kit (ADK), GitHub CLI (gh), Google Search tool (Gemini API), Google Cloud Storage (GCS) bucket, GitHub repositories as sandbox sources, AI Studio, LangChain Open Deep Research (case reference), Cursor (case reference, speaker says 'Curso'), Manus (case reference, speaker says 'Manos')

## [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../videos/Qw_tC68KKes.md)
`Qw_tC68KKes` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, multi-agent, context-engineering

Cloudflare's Justin Joyce on scaling go-to-market analysis with curated skill files, a three-agent report pipeline and a self-service agent workspace; a practitioner account with few hard metrics.

- Techniques: Role-specific skill files with embedded question catalogue; Pre-shaped analytical data for agents; Draft, verify, then tone multi-agent report pipeline; Push generated narratives instead of dashboards; Reviewed central skill catalogue; Per-user persistent agent workspace
- Tools: Cloudflare Workers, Cloudflare Durable Objects, MCP, AI Gateway, Salesforce, Gemini (mentioned as a phone analogy)

## [The Era of Compound Engineering — Kieran Klaassen, Every/Cora](../videos/_ehJyfHg1Vk.md)
`_ehJyfHg1Vk` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: claude-code, software-factory, context-engineering

Kieran Klaassen (Every/Cora) on compound engineering: extract your judgment and repeated corrections into repo knowledge so each feature makes the next one easier, with a demo of his open-source plugin's commands.

- Techniques: Compound engineering loop; Ideation against strategy docs; Doc review for sharp questions; Brainstorm with minimal questions; Unattended end-to-end run (/lfg); PR polish with explanation; Extract a design rule from a review fix
- Tools: Claude Code, Codex, Cursor, Claude Cowork, Linear, GitHub, Slack, Intercom, Rails, React, MCP

## [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../videos/M05vON8i0aI.md)
`M05vON8i0aI` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, governance-compliance, context-engineering

Imad Touil (QuantumBlack) argues org know-how should live in governed agent skills: a central registry with owners, versions, access control and evals. Ungoverned skills bring duplication, quality decay, security risk and wasted tokens.

- Techniques: Skill catalog with metadata and an MCP search front end; Microservice-style skill design; Progressive disclosure of skills; Runtime composition of regulatory skills into a review workflow; Static skill tests before any evaluation; Individual-to-team-to-platform promotion path
- Tools: Claude Code, Cursor, MCP, Backstage (IDP), GitHub

## [How long can your skills be before your agent forgets what you told it? — Laurie Voss, Arize AI](../videos/XzJD1bvXKjs.md)
`XzJD1bvXKjs` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: context-engineering, evals, models-research

Laurie Voss re-runs the 200-instruction IFScale benchmark on 2026 frontier models and finds the ceiling moved about 10x, to roughly 2,000 to 5,000 rules, but reliability and verification remain open problems.

- Techniques: Instruction density probe; Model-specific failure profiling; Pre-screening test vocabulary for safety filters; Per-output eval of long rule sets; Robustness check by rewording and reordering
- Tools: IFScale benchmark, Arize AI (speaker's employer; no product detail given), Chroma context rot study, Firebench, CCRbench, Guidebench (names as captioned; may be misspelled)

## [Don’t be data poor — Anuj Iravane, Anterior](../videos/XAsb7MIAzm8.md)
`XAsb7MIAzm8` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: data-engineering, evals

Anuj Iravane (Anterior) explains how to generate synthetic medical records when real PHI cannot be kept, by sampling labels and policy reasoning traces first and generating documents backward.

- Techniques: Reverse-generation from sampled labels; Coarse-to-fine layered generation; Round-trip label verification; Cross-document consistency eval in a refinement loop; Skill files as the domain-expert interface
- Tools: internal agent harness (unnamed)

## [PrimeAgent + Opus 5 is INSANE (Why I Dropped Claude Code)](../videos/kg3MmLd0qEM.md)
`kg3MmLd0qEM` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: coding-agents, agent-architecture, memory

A Kai Explains review of Prime Agent, an open-source MIT terminal coding harness with cross-session learning, paired with Claude Opus 5 as a Claude Code replacement; the self-reported benchmarks are flagged as unverified.

- Techniques: Learned-layer self-improvement over an immutable base prompt; Persistent goal with bounded autonomous run; RLM-style context management; Per-task effort dial; Model-agnostic routing with self-hosting; Container isolation for self-modifying agents
- Tools: Prime Agent (Prime Intellect, MIT, open-sourced 2026-08-05), Claude Opus 5 (released 2026-07-24), Claude Code, Cursor, Cline (transcribed as 'Klein'), Claude Fable 5, GPT 5.6 Sol, vLLM, Ollama (transcribed as 'Alama'), LM Studio, FrontierBench v0.1, ARC-AGI-3

## [Insane Claude Design Skills You Need To Actually Build Beautiful Sites](../videos/Ysr7oNDajJI.md)
`Ysr7oNDajJI` · AI LABS · 2026-09-02 · q2 · intro · review · also: product-ux, claude-code

AI LABS walks through design-focused agent skill packs (Emil Kowalski, Conard Lee, Elia Design, Meng To, Jakub Krehel, Tastemaker, perception laws) for Claude Design and says they steer models away from generic layouts. Mostly an overview; little measured evidence.

- Techniques: Install and invoke a design skill in Claude Design; Layer skills by stage; Score-and-iterate loop; Regression-aware review via GitHub; Script-based reference extraction; Landing-page as one-action structure; Install only the skills that fit your workflow
- Tools: Claude Design, Claude Code, Codex, GitHub, Emil Kowalski design skills (design-engineering skill, Animate, Apple Design, animation vocabulary), Conard Lee garden skills (web design engineer skill), Elia Design landing-page skill, Meng To skills (video-to-prompt, awards-quality sites), Jakub Krehel skills (review, better layout), Tastemaker, screen critique skill, perception laws skill

## [This Claude Code Skill make Building 10x Faster](../videos/b9k-AE4v5yI.md)
`b9k-AE4v5yI` · AI LABS · 2026-09-02 · q2 · practitioner · review · also: claude-code, multi-agent

AI LABS walks through two Claude Code/Codex skills: one checks existing products and open-source projects before building, and one searches academic papers when nothing is shipped yet. Also covers a publish-once skill distribution setup. Partly a promo.

- Techniques: Clarify-then-search gate with logged assumptions; New-idea vs existing-project branch; Applicability-vs-scale notes for each prior-art project; Three-stage cost check; Install a skill from a GitHub link; Paper-per-sub-agent research fan-out; Publish-once, auto-pull skill distribution; Cheap-first, escalate-on-novelty cascade
- Tools: Claude Code, Codex, GitHub, Advise Project Approach (skill), NeuroArchive (skill), Head Start (skill), skills CLI, Claude Code plugins, Archive (preprint platform), Stream (chat API), Sendbird (chat API), Lovable (sponsor)

## [How To Use Claude Design To Build Beautiful Sites](../videos/bBlY5YOsKN8.md)
`bBlY5YOsKN8` · AI LABS · 2026-09-02 · q3 · practitioner · tutorial · also: vibe-coding-app-building, coding-agents, context-engineering

A five-stage workflow for building a site with Claude Design: write a design.md brand file first, build a design system from it, wireframe, produce the full design, then hand off to Claude Code with a Supabase backend.

- Techniques: design.md-first planning skill; Preview design.md outside the token-metered tool; Design system from design.md; Wireframe, then batched comments; Full design from a chosen wireframe; Claude Design to Claude Code handoff; Post-build design.md conformance review; Supabase skill install and MCP connection
- Tools: Claude Design, Claude Code, Opus 5, Opus 4.7, Haiku, Fable, design.md (Google format), Supabase, Supabase agent skills (general and best-practices), Supabase MCP, Supabase CLI, VS Code

## [Hermes Agent Skills That Make It 10x More Powerful](../videos/WJgxX0Eib6k.md)
`WJgxX0Eib6k` · AI LABS · 2026-09-02 · q2 · intro · review · also: context-engineering, token-cost-efficiency, multi-agent

Walkthrough of third-party skills for the Hermes agent (planning-with-files hook, Delegate Setup, RTK, Mantis security reviews, Agent Reach, Skill Retriever), most of which work with any coding agent; thin on exact commands and partly sponsored.

- Techniques: File-backed plan injected by a hook; Orchestrate several installed coding agents from one agent; Route shell commands through RTK via a skill; Scheduled security review with alerts; Retrieval-filtered skill list
- Tools: Hermes Agent, Claude Code, Codex, Cursor, planning-with-files, Delegate Setup, RTK, Mantis (Google), Agent Reach, Skill Retriever, Plural Workbench, Opus

## [These New Claude Skills Are Actually Insane](../videos/jyLKRN36-Dc.md)
`jyLKRN36-Dc` · AI LABS · 2026-09-02 · q3 · practitioner · review · also: claude-code, context-engineering, product-ux

AI LABS walks through six new agent skills: a self-improving skill-learning log, a four-rule coding baseline, a logged-in website CLI (OpenCLI), a variant-picker for UI, and two product-business skill sets for onboarding, paywalls, churn and validation.

- Techniques: Per-project learning log for skills; Parent-folder CLAUDE.md for base coding rules; Onboarding and paywall pattern; Cancellation save flow; Logged-in site commands via OpenCLI; Variant exploration for one UI section; Demand validation before building
- Tools: Claude Code, CLAUDE.md, Agent skills, log.md (task-observer output file), OpenCLI, Chrome extension (OpenCLI), Variate skill, Hallmark design skill (mentioned, not shown), Next.js, Supabase, Corey's 48-skill marketing collection, SVG (brand logo format)

## [GitHub's #1 Trending Author's New Claude Skill Is Insane](../videos/c47uqR7XB_c.md)
`c47uqR7XB_c` · AI LABS · 2026-09-02 · q2 · practitioner · review · also: testing-verification, multi-agent, coding-agents

AI LABS walks through "unlazy," an agent skill that makes coding agents prove each task is done via a gates ledger, tree decomposition and fresh-agent re-checks, plus their fix for its slow sequential runs.

- Techniques: Gates ledger with verifier command; Recursive tree decomposition with depth cap; Orchestrator re-verifies sub-agent claims; Parallel sub-agents with file ownership in plan.md; Explicit give-up instead of silent drop; Installing unlazy into a project
- Tools: unlazy (agent skill; name as spoken in the video), Claude Code, Codex, Ralph loop, Claude goal command, Opus, GPT 5.6, VS Code, Data for SEO (sponsor), model router skill (generic, unnamed)

## [We Vetted 2000 AI Skills Before They Reached Developers — Lucas Palma, Nubank](../videos/iKQ78wyJEXU.md)
`iKQ78wyJEXU` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails, pr-code-review, governance-compliance

Nubank's product security team built SkillVector, a CI scanner that vets internal AI skills (hybrid regex plus LLM) before they reach an internal marketplace, and reports 2,000+ skills scanned.

- Techniques: Three-point skill scanning; Hybrid deterministic plus LLM review; Findings as PR comments plus SARIF; Historical back-scan; Verify approval gates, not model confirmations
- Tools: SkillVector (spoken as 'SkillVetor' in the transcript), SARIF, Regex-based determinstic scanners, LLM reviewer, Internal skills marketplace

## [Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital](../videos/khVX_BUnEwU.md)
`khVX_BUnEwU` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, memory, multi-agent

Yohei Nakajima presents Active Graph, an experimental event-sourced graph runtime where an immutable typed log is the agent's ground truth and small behaviors coordinate through shared state; main takeaway is that log-centric design gives replay, forks, resume and gated self-modification for free.

- Techniques: Log-as-memory retrieval; Graph-subscription behaviors and graph-query views; Failure-type-scoped, gated self-edits; Acceptance test by simulated win rate with a confidence bound; Debug by querying the event log, not session logs; Pack-based composition of agents
- Tools: Active Graph, BabyAGI, LongMemEval, Replit, Claude Code, LangSmith (mentioned as a comparison), Kaggle Pokemon trading card game competition

## [Scaling up Continual Learning — Ronak Malde, Trajectory](../videos/zL1kLftVTlo.md)
`zL1kLftVTlo` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: training-finetuning-rl, agent-architecture

Ronak Malde (Trajectory) on scaling continual learning: on-policy self-distillation with privileged hints as a step past GRPO, plus fixes for long tool-calling runs (step-level weighting, hint-leakage control).

- Techniques: On-policy self-distillation (OPSD); Step-level divergence weighting for long trajectories; Residual guidance via linear combination of hint strengths; LLM-filtered hints to prevent leakage; Inspect rollouts for hint leakage
- Tools: GRPO, OPSD, OpenClaw RL, LiveCodeBench, Mercor APEX-Agents

## [HTML Is All Agents Need — James Russo, HeyGen](../videos/Cz4v1WHVyZc.md)
`Cz4v1WHVyZc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: voice-multimodal, context-engineering, product-ux

HeyGen's Hyperframes turns agent-written HTML into deterministic MP4 video by freezing the browser clock and seeking frame by frame; the thinnest HTML wrapper beat heavier DSLs.

- Techniques: Thin HTML as the agent output format; Deterministic frame-by-frame browser rendering; Single render path for preview and output; Taste-focused skills instead of syntax skills; Small model as a format canary; Storyboard, iterate, then human last-mile edit; Website-to-asset single-shot skill
- Tools: Hyperframes, HTML/CSS/JS, Three.js, WebGL, WebGPU, Lottie, Rive, Remotion (transcribed as "Promotion"), After Effects, Premiere Pro, Gemini 3 Flash, Claude Code

## [Agentic Development Security — Ezra Tanzer, Snyk](../videos/cgimkNGNjvU.md)
`cgimkNGNjvU` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails, claude-code, coding-agents

Snyk on securing agent development in three pillars: the code agents generate, the skills and MCP servers they use, and the actions they take. Mainly a product showcase, with a useful hook-based scanning pattern.

- Techniques: Async post-write scan hook with deferred fix at stop; Steer vs ask policy actions in pre-tool hooks; Static scan of skills and MCP tool descriptions; Per-workspace guardrail profiles
- Tools: Snyk, Claude Code, Codex, Cursor, MCP, Python hooks, VS Code, Electron, ClawHub

## [How to Kill the Code Review — Ankit Jain, Aviator](../videos/YgEv7IQzGdM.md)
`YgEv7IQzGdM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: pr-code-review, testing-verification, context-engineering

Ankit Jain (Aviator) argues code review's real job is alignment, not bug-catching, and proposes reviewing agent session intent, test-plan evidence and a codified "AI slop registry" instead of diffs.

- Techniques: AI slop registry; Capture session decisions as acceptance criteria; Test plan from criteria plus registry invariants, run against a preview; Agent-driven UI evidence with DB snapshots; Review the plan and evidence, not the diff
- Tools: GitHub, Aviator Verify

## [LLM Knowledge Bases: a practical guide — Ben Holmes, Warp](../videos/I3bpdgFJCUY.md)
`I3bpdgFJCUY` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: memory, context-engineering, agent-architecture

Ben Holmes (Warp) shows a markdown-first personal knowledge base: voice-dictate raw notes, have an agent enrich and link them, generate wikis, run it on a cloud schedule, and build graph views with HTML.

- Techniques: Enrich-note skill with a processed-timestamp marker; Controlled tag vocabulary with a no-invention rule; Backlinks via key-term search over a file tree; Raw folder to wiki generation; Sync-in, run, sync-out cloud schedule
- Tools: Obsidian, Obsidian Headless CLI, Warp, oz.dev, Hubble, Claude, Codex app, Exa, Tailwind CSS, Whisper Flow, Handy, GLM 5.2

## [Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition](../videos/I6aiEf3aEFQ.md)
`I6aiEf3aEFQ` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: memory, agent-architecture

Yu Su (Ohio State, CEO of NeoCognition) argues intelligence and expertise are different axes and that continual learning, not bigger models, is what turns agents into domain experts.

- Techniques: Adaptive compression loop for agent memory; Rules stored with preconditions and exceptions; Select context by expertise instead of parallel brute force; Measure expertise per environment

## [Skills are new features: Building Skill-Centric Harness — Yogendra Miraje, FactSet](../videos/7jjudsEhBtM.md)
`7jjudsEhBtM` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: agent-architecture, context-engineering, governance-compliance

FactSet's principal AI engineer argues skills are the new product features and engineers should ship harnesses, then covers a minimal skill harness, routing via descriptions, eval-gated skills, and skill-library governance.

- Techniques: Minimal skill registry and loop; Write descriptions as routing signals; Cut skills by user intent; Front-load critical instructions and re-run evals on model upgrades; Shortlist skills before they hit the system prompt; Governance as a skill PR pipeline
- Tools: Anthropic Agent Skills (SKILL.md format), Claude Code, Codex, bash or code sandbox for skill scripts

## [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../videos/aeTb5BdmTTc.md)
`aeTb5BdmTTc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: context-engineering, enterprise-adoption, coding-agents

How a 10-person team got to shipping with coding agents: treat agent setup as a leadership job, share the best practices, invest in one high-value skill, and close the loop on slop.

- Techniques: Thin CLAUDE.md/AGENTS.md index; Skill as a folder with a short SKILL.md; Runbooks in code comments as discovery hooks; One end-to-end ship-it skill; Nightly code-gardener agent; Shared setup with an opt-out for experiments; First-prompt context audit
- Tools: Claude Code, CLAUDE.md, AGENTS.md, CI/CD, issue boards

## [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../videos/il1c1a2FufU.md)
`il1c1a2FufU` · AI Engineer · 2026-08-18 · q4 · practitioner · workshop · also: coding-agents, context-engineering, multi-agent

Jason Liu (OpenAI) shows how he runs Codex as a personal ops system: pinned long-lived threads, a git-tracked memory vault, heartbeats, and goal verifiers. Main takeaway: compaction makes long threads workable.

- Techniques: Long-lived pinned thread per workstream; Heartbeat / loop in the same thread; /goal with a verifier and file-backed goal; App shot plus accessibility tree; Git-tracked personal memory vault with agents.md routing; Monitor thread that spawns per-issue threads; Skill from one completed run, with self-edit permission; Annotate a localhost preview to steer the agent; Model and reasoning tiering
- Tools: Codex app, Codex CLI, Codex in-app browser, computer use, Chrome extension, Slack connector, Gmail connector, Google Drive connector, Notion, Linear, Obsidian, GitHub

## [Every Harness Will Become A Claw — Sam Bhagwat, Mastra](../videos/8qWIPUia2O8.md)
`8qWIPUia2O8` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: agent-architecture, sandboxing-execution, product-ux

Sam Bhagwat (Mastra) argues agent harnesses will keep expanding into always-on "claws" with durability, initiative and learning, then shake out to a few winners. Mostly conceptual, with little hard data.

- Techniques: Durable turn streaming with resume; Queue, steer and interrupt on running threads; Session-scoped tool approval; Heartbeat wake-ups; Trace-driven continual learning; Cloud sandbox per parallel subagent
- Tools: Mastra, Claude Code, Codex, OpenClaw, Hermes Agent, Slack, Telegram, WhatsApp, GitHub

## [Skills are the New SDKs - Elvin Aghammadzada, DataRobot](../videos/LC3-P7v3yoI.md)
`LC3-P7v3yoI` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: context-engineering, mcp-and-tools

Elvin Aghammadzada (DataRobot) argues agent skills are a progressive-disclosure context tool that complements MCP, and that skills are software needing versioning, evals and security review.

- Techniques: Progressive disclosure via a skill index; Context budget ceiling; Skill as a wrapper around an MCP server; Split by role: skill for reasoning, MCP for execution; Treat skills as versioned, tested software
- Tools: Claude Code, Codex, Copilot, Gemini CLI, OpenClaw, ClawHub, MCP

## [This New Skill Finally Solves Thinking For AI Agents](../videos/m6IXL_YGqBQ.md)
`m6IXL_YGqBQ` · AI LABS · 2026-08-02 · q2 · intro · review · also: multi-agent, coding-agents, testing-verification

AI LABS walks through a community "ADHD" skill that makes a coding agent ideate by fanning out isolated sub-agents, each seeded with a different frame, then scoring and merging the results; shown for test planning and pre-ship UX/churn review.

- Techniques: Frame-diversified tree-of-thought fan-out; Three-question gate before auto-invoking an expensive fan-out; Install an agent skill from a repo and fix the config folder for Claude Code; TDD test-strategy planning with PRD and tech spec linked in CLAUDE.md; Pre-launch UX and churn review by fan-out
- Tools: Claude Code, Codex, Cursor, CLAUDE.md, .agents folder (installer target), SKILL.md, Top View (sponsor; AI video skill), Kling, Sea Dance, Nano Banana

## [Alibaba Just Cut AI Agent Costs by 99% — Here's How](../videos/eCZwexfka6E.md)
`eCZwexfka6E` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: mcp-and-tools, token-cost-efficiency, agent-architecture

Alibaba's SkillWeaver paper cuts agent tool-routing tokens from 884k to 1,160 per query by decomposing, retrieving and composing tools, but the benchmark is self-run and execution was mocked.

- Techniques: Decompose-Retrieve-Compose tool routing; Skill-aware decomposition (SAD) feedback loop; Right-size decomposition granularity
- Tools: SkillWeaver (Alibaba research paper, pipeline name), CompSkillBench (Alibaba benchmark: 300 multi-step queries, 2,209 MCP-derived tools, 24 categories), Qwen2.5-7B-Instruct, Qwen Max, MCP (Model Context Protocol) ecosystem, as the tool source, LangChain, LlamaIndex (spelled 'Lama index' in the transcript), GPT 5.5 (mentioned as a model the market is racing to wire in), Opus (mentioned as a model the market is racing to wire in)

## [Anthropic Just Fixed Graph Engineering's Greatest Flaw](../videos/H7t3uUp3HVw.md)
`H7t3uUp3HVw` · AI LABS · 2026-08-02 · q2 · intro · tutorial · also: testing-verification, multi-agent, claude-code

Graph engineering fans agent work across parallel nodes but hides failures; the video's fix is layered verification skills built with Skill Creator, plus a fresh-context Opus second opinion.

- Techniques: Install Skill Creator as a plugin; Standalone deep-review skill; Embedded verification skill that runs after each feature; Embedded rule-gate skill; Second-opinion skill via claude -p; Headless browser for visual verification; One skill per review angle, chained by an orchestrator skill; Write build, test and lint commands into CLAUDE.md; Pin the judging node to a stronger model
- Tools: Claude Code, Claude Opus, Claude Haiku, Codex, Skill Creator plugin, verify skill, code review skill, simplify skill, design skill, design.md, second opinion skill, CLAUDE.md

## [How To Use Codex To Build Insanely Beautiful Websites Using GPT 5.6 Sol](../videos/pHstb0JGGhE.md)
`pHstb0JGGhE` · AI LABS · 2026-08-02 · q3 · practitioner · tutorial · also: coding-agents, vibe-coding-app-building, context-engineering

Seven-stage tutorial for building a non-generic landing page with the Codex app and GPT 5.6, using AGENTS.md, a design skill, a design.md brand file, generated images, and a deploy step. Main lesson: encode taste and brand in files, not in each prompt.

- Techniques: Scoped seed prompt; AGENTS.md via /init, plus a self-verify rule; Install a design skill and forbid the default one; Browser verification loop; design.md brand system; Plan-mode image generation into an assets folder; Screenshot-based layout cloning; Single-section component swap; Performance pass; Local commits as checkpoints; Deploy with the site skill
- Tools: Codex (in the ChatGPT app), GPT 5.6, GPT image model, Next.js, AGENTS.md, GPT Taste skill, OpenAI site skill, Anthropic front-end design skill, design.md (format introduced by Google through Stitch), Aura Build design.md library, 21.dev, Godly components

## [Facebook's Release Just Gave Claude Code A New Design System](../videos/-HEdqzzYKco.md)
`-HEdqzzYKco` · AI LABS · 2026-08-02 · q2 · practitioner · review · also: claude-code, context-engineering, vibe-coding-app-building

Walkthrough of Meta's open-source React/StyleX component library (transcribed as "Asterix"), built to be read by coding agents via a CLI, plus a sponsor read and a plug for the presenter's skills.

- Techniques: Install the design system with the package manager; Run the init command to write agent instructions; Prompt for a whole site and let the agent pull from the CLI; Generate a manifest of CLI commands and flags for grounding; Screenshot and fix loop in headless Chrome; Chain a generic anti-slop review skill after the build
- Tools: Asterix (Meta's design system, transcript name; likely a caption misspelling), React, StyleX, shadcn/ui (transcribed as ShadCN), Next.js (App Router and Pages Router), npm, Claude Code, CLAUDE.md, AGENTS.md, globals.css, headless Chrome, AI Slop Detector skill (presenter's AI Labs design system)

## [This Skill Just Made Kimi K3 a 10X Better Designer](../videos/EwTOiqWWqEc.md)
`EwTOiqWWqEc` · AI LABS · 2026-08-02 · q2 · practitioner · review · also: claude-code, vibe-coding-app-building, coding-agents

Walkthrough of running Kimi K3 inside Claude Code via a local proxy on a Kimi subscription, then using the Hallmark anti-slop design skill to push Kimi, Opus and Codex off their default visual styles.

- Techniques: Run a non-Claude model inside Claude Code via a local subscription proxy; Install Hallmark for the right agent; Invoke a skill manually with its slash command when the model is not Claude; Prompt Hallmark with the three pre-flight answers; Run the audit verb, then pick which findings to fix; Use the study verb, not a clone request; Manage context manually on long design sessions
- Tools: Kimi K3, Kimi Code, Claude Code, Codex, Codex app, CLIProxy API, Hallmark, Next.js, Opus 4.8, Sonnet 4.5, GPT 5.6, Fable 5

## [On AI and Knowledge — Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft](../videos/RGSFUqzqErE.md)
`RGSFUqzqErE` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: rag-retrieval, evals, context-engineering

Microsoft's Pablo Castro splits agent knowledge into intrinsic, extrinsic and learned, and demos Foundry knowledge bases and an Agent Optimizer that tunes agent config from traces.

- Techniques: Three-way knowledge split for agent design; Hybrid retrieval over combined methods; Layered retrieval API; Agentic retrieval with a satisfaction check; Knowledge base as MCP server; Eval generated from traces, then hill-climb the agent config
- Tools: Microsoft Foundry, Foundry IQ, Azure AI Search, Work IQ, Fabric IQ, WebIQ, Agent Optimizer, Foundry Toolkit for VS Code, GitHub Copilot, MCP

## [Agents Building Agents - Alfonso Graziano, Nearform](../videos/aHhB3sjGjkI.md)
`aHhB3sjGjkI` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: evals, observability, coding-agents

Alfonso Graziano (Nearform) shows coding agents improving other agents: an eval-driven loop lifts a toy agent from 18% to 83% and a production agent from 67% to 86%, and a trace-clustering loop turns live user feedback into fixes.

- Techniques: Golden dataset plus scorers as the agent test suite; Baseline report before the optimization loop; Branch-per-hypothesis improvement loop with rollback; Protected eval set in the optimizer instructions; Reading the agent's full traces, including thinking traces, for root cause; Trace clustering from live feedback; Packaging the analysis as a reusable skill; Failure mode to spec to golden-set entry
- Tools: Claude Code, Mastra, auto-agent (the speaker's own internal tool, not public)

## [Building Great Agent Skills: The Missing Manual](../videos/UNzCG3lw6O0.md)
`UNzCG3lw6O0` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: context-engineering, claude-code

Matt Pocock's prerecorded talk gives a four-part checklist (trigger, structure, steering, pruning) for judging and writing agent skills, to escape "skill hell".

- Techniques: Choose user-invoked vs model-invoked per skill; Steps plus reference split with external context pointers; Leading words; Split phases into separate skills to force legwork; Deletion test and sediment audit
- Tools: SKILL.md agent skills, superpowers (comparison skill set), Matt Pocock skills repo (writing-great-skills skill)

## [Every company should have a Brain — Garry Tan, Y Combinator](../videos/eBUyTS7SzV4.md)
`eBUyTS7SzV4` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: context-engineering, memory, enterprise-adoption

Y Combinator's Garry Tan argues that AI productivity comes from how work is wired (skills as employees, routing tables, company memory with hygiene), not the model, and pitches an open-source "company brain" called GBrain.

- Techniques: Skill file as a single-job employee; Resolver table for routing context; Trigger evals on routing; Skillify at task end; Split latent and deterministic compute; Curated company brain; Select a small working set per task
- Tools: Claude Code, Codex, OpenClaw, Hermes agent, GBrain, Postgres, TypeScript, Markdown skill files

## [Chat and citations won't save your vertical AI - Atul Ramachandran, Filed Inc](../videos/RGiXcVxSD3s.md)
`RGiXcVxSD3s` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: product-ux, agent-architecture, observability

Vertical AI talk by the Filed CTO arguing chat and citations are not enough; products should be built for delegating long-running work to agents, with skills, traces, pause-and-intervene and plan approval.

- Techniques: Delegation-first task selection; Implicit skill capture from usage; Per-value trace-back for trust; Pause-and-tag intervention; Plan approval gate for irreversible actions
- Tools: Wispr Flow

## [Don't Ship Skills Without Evals — Philipp Schmid, Google DeepMind](../videos/0vphxNt4wyk.md)
`0vphxNt4wyk` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: evals, context-engineering

Philipp Schmid (Google DeepMind) argues skills need evals like code does, and gives a lean eval-harness recipe: trigger tests, regex asserts, repeated trials, and with/without-skill ablations to decide when to retire a skill.

- Techniques: Trigger and negative-case eval set; JSON cases plus regex asserts; LLM-as-judge for trace-level checks; CI gate on skill diffs; With/without-skill ablation; Isolated, repeated trials; Lean skill plus reference files; Goal-and-constraint skills, scripts for fixed workflows
- Tools: Gemini CLI, Gemini API, Gemini Interactions API, SkillsBench, Claude Code, Codex, Cursor, Antigravity, Python, regex, LLM-as-judge

## [Understanding is the new bottleneck — Geoffrey Litt, Notion](../videos/WkBPX-oDMnA.md)
`WkBPX-oDMnA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: coding-agents, testing-verification, product-ux

Geoffrey Litt (Notion) argues humans must still understand agent-written code to stay creative participants, not only to verify it, and shows explainer docs, comprehension quizzes, agent-built micro-worlds and shared spaces for doing so.

- Techniques: Explainer doc per agent change (ExplainDiff-style skill); Comprehension quiz gate before sharing code; Intuition-first, literate ordering; Agent-built micro-world debugger; Step-through simulation for a migration; Shared threads and commentable docs with agents
- Tools: Claude Code, Claude, Cursor, Notion, Notion HTML blocks

## [Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI](../videos/2IxD9OB3XuQ.md)
`2IxD9OB3XuQ` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: evals, memory, context-engineering

Soheil Feizi (RELAI) argues agents should learn from production failures only through verifiable updates: turn logs into replayable test environments, route fixes to model, harness or memory, and gate each change with regression tests. Second half is a product demo.

- Techniques: Log-to-replayable-environment lift; Instruction-first environment bootstrap; Three-gate fix verification; Layer routing by smallest durable change; Regression-aware optimization; Regression trap in benchmark design; Reviewable change proposal as output
- Tools: RELAI Rely (rely optimize CLI), GEPA, Letta, mem0, LoRA, DPO, GRPO, RLVR, SFT

## [WTF Is the Context Layer? The Missing Infrastructure for Production Agents — Prukalpa Sankar](../videos/8G_1-3IO4ZQ.md)
`8G_1-3IO4ZQ` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: context-engineering, memory, enterprise-adoption

Atlan's founder argues production agents fail on missing business context, not model intelligence, and proposes a shared, versioned "context layer" (a company brain) that agents draw from.

- Techniques: Jobs-to-be-done scaling factor for agent selection; Shared context layer as a company brain; Context lifecycle management like software; Trace-driven maintainer loop; Reverse-construct the data stack to bootstrap context
- Tools: Claude Code, Codex, Claude Cowork, Google ADK, Glean, Relevance AI, MCP, Qualified, Artisan

## [User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch](../videos/Jx4ZFEAq6bY.md)
`Jx4ZFEAq6bY` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: memory, rag-retrieval, evals

StarlightSearch's CEO argues agent memory should learn from outcomes: utility-weighted retrieval, reasoning-style memories, and consolidation into skills. Product-pitchy, with self-reported benchmarks.

- Techniques: Utility-weighted memory retrieval; Human failure report as a memory write; Memory as procedure, not fact; Consolidate memories into skills; Runtime learning vs compile-time optimization
- Tools: Reflect (StarlightSearch's memory system), Mem0 (transcribed as 'memzero'), DSPy, ReAct, Pinecone (cited in a post, not used)

## [The Factory That Dreams: 39 AI Agents, No Framework - Rushabh Doshi, Machinecraft](../videos/jtzh-GBXBWc.md)
`jtzh-GBXBWc` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: multi-agent, memory, enterprise-adoption

A 100-person Indian thermoforming-machine maker built a 36-agent go-to-market "brain" with layered memory and a nightly dream cycle, with no training and no framework. The talk is a company story with some architecture and cost claims.

- Techniques: One-job specialist agents with an orchestrator and debate; Layered agent memory with a salience gate and correction precedence; Nightly consolidation (dream cycle) job; Rules file as production guardrails; Chunk-and-extract over a private corpus with no training; Draft-only outbound with human send
- Tools: Cursor, vector database, graph database, CRM, Google Workspace integrations, document ingestion tooling, monitoring tooling

## [4 Ways to Actually Build Stunning Websites with Claude Code](../videos/HqD5a2Cae60.md)
`HqD5a2Cae60` · AI LABS · 2026-07-02 · q3 · practitioner · tutorial · also: vibe-coding-app-building, claude-code, context-engineering

AI LABS walks through four ways to get better websites and UIs from Claude Code: refresh design skills from model prompting guides, use design.md files, plan functional UIs as HTML mockups, and clone existing UIs. Mostly anecdotal, with a sponsor segment.

- Techniques: Refresh a design skill from the model's prompting guide; Mine older prompting guides for dropped fixes; Set effort by task type; Conditionally load a sub-skill from a rule; Apply design.md after generation for marketing pages; Functional UI pipeline: plan, mockups, gallery, port; Consistent variants via a shared design.md; CLAUDE.md as product context and verify contract; Verify with a sub-agent against design.md; Clone a marketing site with a capture CLI and sitemap; Clone an auth-gated app from screenshots
- Tools: Claude Code, Claude, Fable 5, Opus 4.8, Anthropic front-end design skill, design.md, GetDesign.md, GSAP, Single File CLI (as named in the video), sitemap.xml, HTML, CLAUDE.md

## [PAI: The Life OS for AI-Powered Development](../videos/JukZ7WWtOSg.md)
`JukZ7WWtOSg` · Better Stack · 2026-07-02 · q3 · intro · review · also: claude-code, memory, context-engineering

Better Stack reviews PAI (Personal AI Infrastructure), a memory-and-skills operating layer on Claude Code. Its value is cross-session continuity; it needs terminal comfort and ongoing upkeep.

- Techniques: Persistent project memory loaded every session; Planning prompt that requires risks, assumptions and verification; One custom skill per role or review type; Fixed action order through a multi-step process
- Tools: Claude Code, PAI (Personal AI Infrastructure), Pulse (PAI local dashboard), Telos (PAI goals/ideal-state file, as named in the video), Fabric (named as a prior project of the PAI creator), SecLists (spelled 'SecList' in captions; named as a prior project of the PAI creator), LangChain (compared against), CrewAI (compared against), Next.js (example skill domain)

## [They Finally Fixed Claude Code's Biggest Problem](../videos/KiTmBtyaeXg.md)
`KiTmBtyaeXg` · AI LABS · 2026-07-02 · q2 · practitioner · review · also: security-guardrails, claude-code

A walkthrough of NVIDIA's Skill Specter, a scanner for agent skills, plus a Claude Code wrapper that adds an LLM-based second scan through headless mode and a discover-scan-fix loop around skills.sh.

- Techniques: Two-tier skill scan before install; Use Claude headless mode as the LLM judge; Discover, scan, show, fix, rescan loop in SKILL.md; Check tool-name identity at the code-point level; Compare declared behavior with code behavior; Check dependencies against a live bad-package list
- Tools: Skill Specter (NVIDIA scanner, named by the host; version not stated), Claude Code, Claude headless mode (claude -p), skills.sh (skill registry with CLI search), OpenAI API (the AI check's default backend, per the host), Codex (mentioned only in the sponsor segment), Nimblist (sponsor; open-source visual workspace for Claude Code and Codex sessions, with a Kanban board, red/green diffs, auto-generated commit messages, and a mobile app)

## [Hermes Agent under Claude Code Is Insane](../videos/Sb96po6S67k.md)
`Sb96po6S67k` · AI LABS · 2026-07-02 · q2 · practitioner · tutorial · also: claude-code, mcp-and-tools, memory

Setup-and-use walkthrough for running the Hermes agent alongside Claude Code: Hermes adds persistent memory and self-evolving skills, and can run as an MCP server, cron-driven monitor, or Claude Code launcher.

- Techniques: Install Hermes and run the manual setup; Onboard Hermes with your context; Expose Hermes to Claude Code as an MCP server; Cron-driven living PRD skill from a Slack channel; Delegate feature work to Claude Code from a Hermes channel; Health-check skill loop for a deployed app
- Tools: Hermes Agent (Nous Research), OpenClaw, Claude Code, Claude Code subscription / non-interactive mode, Anthropic Agent SDK credit (policy claim), hermes setup command, hermes mcp serve command, .mcp.json, user.md and memory.md (Hermes memory files), soul file (Hermes agent personality/instructions), Hermes Skill Hub, Hermes bundled Claude Code skill

## [Finally, a Programmable AI Agent Framework That Works](../videos/n5cYS6KuyK8.md)
`n5cYS6KuyK8` · Better Stack · 2026-07-02 · q3 · practitioner · review · also: agent-architecture, sandboxing-execution, token-cost-efficiency

Walkthrough of Flue, an open-source TypeScript agent-harness framework from the Astro team, showing agents, workflows, HTTP triggers and an in-memory sandbox tier that avoids booting containers.

- Techniques: Single-file agent definition; Skill-backed workflow; Local execution for skills that need files; Safer custom tool instead of local mode; HTTP-triggered workflows; Tiered sandboxes
- Tools: Flue (Flue runtime, Flue CLI, flue.config.ts, server.mjs), Pi (minimal agent harness), OpenClaw (mentioned as built on Pi), Astro, Bun, Vite, Hono, Node.js, Cloudflare Workers and Durable Objects, Cloudflare sandboxes, Vercel Just Bash, Daytona

## [Krea 2 image model, Sakana Fugu beats Fable 5, Seedance 2.5, Seed 2.1 & More AI News](../videos/q8NQD1IZnFk.md)
`q8NQD1IZnFk` · Kai Explains · 2026-07-02 · q3 · intro · news · also: models-research, multi-agent, voice-multimodal

Weekly AI news roundup (July 2026): Seedance 2.5 preview, Sakana Fugu model routing, Ling/Ring 2.6 open trillion-parameter MoEs, Krea 2 open weights, NVIDIA BioNeMo skills. Nearly all numbers are vendor-reported.

- Techniques: Documented skill specs for domain tools (BioNeMo skills); Single-endpoint learned model assembly (Sakana Fugu); Sparse 3D box blocking for object motion (Loose Control Video); Bidirectional generation for seamless loops (Unitemp); Reasoning effort toggle per task (Ring 2.6); Pick the Krea 2 checkpoint by use (RAW vs Turbo)
- Tools: Seedance 2.5 (transcribed as CDance 2.5), Seedance 2.0, Veo 3.1, Kling 3.0, Sakana Fugu, Trinity (ICLR 2026), Conductor (ICLR 2026), Ling 2.6, Ring 2.6, ICEPOP (async RL method), Gemini 3.1 Pro, Claude Opus 4.7

## [Insane Claude Design Skills You Need To Build Beautiful Websites](../videos/Ot582-E61ac.md)
`Ot582-E61ac` · AI LABS · 2026-07-02 · q3 · intro · review · also: product-ux, coding-agents, mcp-and-tools

A walkthrough of Claude design skills (Anthropic frontend-design, ShadCN, UI UX Pro Max, GSAP, Material 3, SwiftUI, Expo) for building less generic websites and mobile apps, with a sponsor segment.

- Techniques: Commit to a design direction before generating; Separate functional and marketing design skills; Pair a rules skill with a component-registry MCP; Separate layout reasoning from component work for dashboards; Use a taste preset instead of a full design system; Prefer compositor-friendly animation properties
- Tools: Claude, Anthropic frontend-design skill, Opus 4.8, Fable 5, ShadCN, ShadCN MCP, UI UX Pro Max, GSAP, Higgsfield, C-Dance (as captioned; video model), Material 3, SwiftUI

## [Loop Engineering Totally 10x Hermes agents](../videos/AQRDjI5owZI.md)
`AQRDjI5owZI` · AI LABS · 2026-07-02 · q2 · practitioner · tutorial · also: agent-architecture, claude-code, multi-agent

Explains "loop engineering": replacing hand-written prompts with self-driving agent loops, split into deterministic loops (tests as the goal) and non-deterministic loops (UI judged by a skill plus a second verifier model), run on the Hermes agent and Claude Code.

- Techniques: Five-step loop; Deterministic loop with tests as the goal; Adversarial builder/verifier loop for judgment tasks; Explicit verification gates and termination; External state files
- Tools: Hermes agent (always-on agent, self-evolving skills), Claude Code (non-interactive and interactive modes), Claude Code hooks, Ralph loop, Claude goal command, Goal Buddy 2, OpenClaw, GitHub CLI (gh), GPT models (named as verifier, no version given), Claude Opus 4.5 (mentioned), Fable 5 (mentioned, no detail)

## [6 Insane Hermes Agent Use Cases That You Need Right Now](../videos/qMEm1bgxnUM.md)
`qMEm1bgxnUM` · AI LABS · 2026-07-02 · q2 · intro · review · also: token-cost-efficiency, agent-architecture, memory

Walkthrough of six Hermes Agent use cases: cron jobs gated by a wake flag or a no-agent flag, a Slack team second brain, Gmail lead webhooks, PRD-as-skill competitor tracking, and human-reviewed social posting.

- Techniques: Pre-LLM gating with a wake-agent flag; No-agent cron jobs for deterministic checks; Ask the agent to build the automation from a prompt; Draft-then-publish content skill with human review; PRD as a skill plus scheduled research; Gmail lead-triage webhook; Profiles for isolated personas
- Tools: Hermes Agent (desktop app and TUI), OpenClaw, Claude Code (transcribed as "clawed code"), cron, Slack, Stripe, Stripe MCP, AWS, Gemini API, Google Play API, Gmail, Google Cloud

## [Skill issue: Lessons from skilling up coding agents to use Langfuse - Marc Klingen, Clickhouse](../videos/vNCY9kXXyDQ.md)
`vNCY9kXXyDQ` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: observability, evals, claude-code

Langfuse's founder explains how they built an installable skill that teaches coding agents to add Langfuse tracing and evals, and what they learned about docs, eval checks and auto-tuning skills.

- Techniques: Skill with progressive disclosure; Agent-facing docs surface; Wrap the API as a CLI and advertise --help; Natural-language checks for skill evals; Auto-research loop on a skill with human review; Timestamped skill copies for staleness
- Tools: Claude Code, Langfuse, OpenAI SDK

## [Your Coding Agent Should Do AI System Engineering — Ben Burtenshaw, Hugging Face](../videos/JomVvNDjGb8.md)
`JomVvNDjGb8` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: coding-agents, multi-agent, training-finetuning-rl

Ben Burtenshaw (Hugging Face) argues coding agents can take on AI systems work: writing CUDA kernels, fine-tuning models, and running a multi-agent automated research lab, using open skills, open Hub repos and an open dashboard data layer.

- Techniques: Skill-as-few-shot-examples with bundled benchmark scripts; Skill eval across models (Upskill); Role-split autoresearch loop; Git and bucket as agent shared state; Open-format dashboard as an agent data source; Verifiable-experiment precondition
- Tools: CUDA, Hugging Face kernels library, Upskill, Hugging Face Skills repo, HF Papers CLI, HF Jobs, OpenCode, Codex, Claude Code, Trackio, Parquet, Unsloth

## [Your Attention Is the Bottleneck, Not Your Agents — Zack Proser, WorkOS](../videos/so9l_MwS2yg.md)
`so9l_MwS2yg` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: claude-code, software-factory, testing-verification

Zack Proser (WorkOS) argues human attention, not agent capacity, is the bottleneck, and shares remote Claude Code from a phone, verification gates, and session-log mining to protect focus.

- Techniques: Three-tier verification ladder for agent output; Closed-loop ticket fixing with explicit done criteria; Remote-controlled session from a phone; Scheduled session-log retrospective; Ticket-tagged overnight agent loop; Parallel large features with worktrees and agent teams; Voice-first brainstorm, then written artifact
- Tools: Claude Code, Claude Opus 4.6, Slack MCP, Linear MCP, GitHub Mobile, Cursor, Codex, Vercel bot, OpenClaw, Twilio, ChatGPT advanced voice mode, git worktrees

## [Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw](../videos/pmoDeA3RBZY.md)
`pmoDeA3RBZY` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: software-factory, multi-agent, coding-agents

OpenClaw maintainer Vincent Koc on running dozens of parallel coding agents as a "dark factory": swim lanes, opinionated loops, a big plugin refactor, and token efficiency over token maxing.

- Techniques: Swim-lane parallel agents; Big refactor gated by existing tests; Plugin split for blast-radius control; One clone per session instead of worktrees; Explanation quality as a health check; Skill improvement from session logs; Embedding graph for backlog dedupe; Synthetic plus real fake-chat eval harness
- Tools: Codex, Git worktrees, GitHub, Discord, Slack, MS Teams, Docker, GEPA, skills.sh, OpenClaw, NemoClaw, vector embeddings

## [How Lovable self-improves every hour — Benjamin Verbeek, Lovable](../videos/KA5kPbdkK2E.md)
`KA5kPbdkK2E` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: evals, observability, vibe-coding-app-building

Benjamin Verbeek (Lovable) on two continuous-learning loops: a self-updating "Stack Overflow" of fixes for stuck users, and an agent "vent" tool that reports platform friction to engineers.

- Techniques: Stuck-session detection with an LLM judge; Clustered, generalised fix knowledge bank; Blank-injection holdout; Tuned agent vent tool; Agent triage of agent feedback; Feedback volume as an incident detector
- Tools: Slack, Framer Motion

## [How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind](../videos/7gujZrJ9L5I.md)
`7gujZrJ9L5I` · AI Engineer · 2026-06-18 · q3 · intro · panel · also: agent-architecture, coding-agents, infra-cost-scaling

A Google DeepMind panel on running coding and research agents at Google scale, covering shared workspaces, quota and cost control, skill sprawl, internal observability, and PR review.

- Techniques: Shared file-system workspace between agent stages; Editable plan gate before execution; Scratchpad notes as a reviewable trace; Mock compute for harness testing; Trajectory store plus hierarchical drill-down; Per-language fine-tuned review model plus per-product review prompts; Transparent model fallback under the harness; Skills plus guardrailed CLI over MCP for internal tools
- Tools: Antigravity, Gemini, Gemma 4, Deep Research, Jules, MCP, OpenClaw

## [From 46% to 90%: Fine-Tuning Tiny LLMs for On-Device Agents — Cormac Brick, Google](../videos/-TiET_K-E_g.md)
`-TiET_K-E_g` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: training-finetuning-rl, local-ai, inference-serving

Google's Cormac Brick on on-device agents: a prompt-based skill harness on Gemma 4, and fine-tuning FunctionGemma on synthetic data to lift function-calling success from about 46% to 90%+ on most functions.

- Techniques: Progressive skill disclosure; In-app JavaScript rendering from a skill; Coding agent writes the skills; Synthetic-data fine-tune for fixed function calling; Export and deploy pipeline for small models; Chained tiny models for a pipeline
- Tools: LiteRT-LM, LiteRT, MediaPipe, Gemma 4, FunctionGemma, Gemma 3, Gemini Nano, Android AICore, Gemini CLI, Gemini Flash, litert-torch, transformers

## [Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs](../videos/V-L0INGTEOg.md)
`V-L0INGTEOg` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: claude-code, coding-agents

Boris Starkov (ElevenLabs) shows how Claude Code reverse-engineered an undocumented 1990s-style VoIP phone's protocol through port probing, command brute-force, and a traffic-capture proxy, then packaged the result as a reusable skill.

- Techniques: Black-box command sweep with error classification; Intermediary proxy for vendor-client traffic capture; Closed-loop hypothesis confirmation; Persisting a learned protocol as a skill; Using the full session transcript as context to generate a deliverable; Human as actuator for physical steps
- Tools: Claude Code, Twilio (SIP trunk), ElevenLabs conversational agents, Windows virtual machine, TCP proxy on macOS, PoE router

## [The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry](../videos/li0SaBt9RDM.md)
`li0SaBt9RDM` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: claude-code, coding-agents

Sentry engineer Priscila Andre de Oliveira on using AI mainly for codebase comprehension: she mined her own sessions, found 67% were comprehension and 2% generation, and built a reusable "Catch Me Up" skill.

- Techniques: Session-log classification audit; Repeated prompt to personal skill; Onboarding via a 'new contributor' framing; Comprehension pass before PR review; Research, then comprehension check, then plan, then implement; Codebase hygiene sprint for agent legibility
- Tools: Claude Code, Claude Opus, Catch Me Up (personal skill), Warden (Sentry code review agent), Junior (Sentry Slack bot that turns threads into PRs), Abacus (Sentry internal AI usage tracker)

## [How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS](../videos/vy7o1g2iHY8.md)
`vy7o1g2iHY8` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: testing-verification, agent-architecture, evals

WorkOS DX engineer on replacing 10k lines of generated agent skills with 553 lines of gotchas, enforcing gates in a state machine, and making agents prove their work with hashes and videos.

- Techniques: Enforced state-machine gates for agent pipelines; Hash-verified test receipts; Gotchas-only skills validated by paired evals; Visual before-and-after proof on PRs; Retrospective agent over run transcripts; Conditional rules instead of doc summaries
- Tools: Pi, Claude Code, Codex, Playwright CLI, TypeScript, SHA-256, WorkOS CLI, AuthKit, TanStack Start, Next.js, GitHub, Linear

## [How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom](../videos/4_VQBbs2iQA.md)
`4_VQBbs2iQA` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: claude-code, enterprise-adoption, pr-code-review

Intercom's platform lead explains how they set a goal to double engineering throughput by standardizing on Claude Code, backed by skills, hooks, calibrated auto-approval and telemetry.

- Techniques: Single-platform standardization with internal plugin distribution; Guidance flywheel; Problem-first prompting; Backtested skill authoring; Calibrated automatic approval; Agent telemetry and transcript mining
- Tools: Claude Code, GitHub Copilot, Cursor, Augment, Honeycomb, S3, DX, Ruby on Rails, React, GitHub

## [Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser](../videos/pFsfax19yOM.md)
`pFsfax19yOM` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: claude-code, evals, context-engineering

Hands-on WorkOS workshop on writing Claude skills: description-based routing, constraints over prose, progressive disclosure, confidence gates, with-and-without-skill evals, and sharing skills.

- Techniques: Description-as-router; Constraints over prescription; Bang-backtick command injection; Progressive disclosure via reference map; Subagent for verbose checks; Confidence-gated clarification; With-and-without-skill eval; Transcript-driven skill refinement; Looped connector poll
- Tools: Claude Code, Codex, Cursor, Pi, OpenClaw, Claude Desktop, Claude Agent SDK, WorkOS CLI, Obsidian, Linear, Slack connector, Remotion

## [Combine Skills and MCP to Close the Context Gap — Pedro Rodrigues, Supabase](../videos/JT3OzDKrucU.md)
`JT3OzDKrucU` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: mcp-and-tools, evals, context-engineering

Pedro Rodrigues (Supabase) on writing a product skill for agents, using a three-condition eval to show skills plus MCP beat MCP alone. Main lesson: agents need guidance, not more context.

- Techniques: Three-condition skill eval; Inline must-not-miss rules; Skill as pointer to live docs; Dev-first schema workflow with a deferred migration; Start minimal and iterate
- Tools: Supabase, Supabase advisor, Braintrust, Claude Code, Codex, Vercel skills package, MCP, SSH, Postgres

## [Agentic Search for Context Engineering — Leonie Monigatti, Elastic](../videos/ynJyIKwjonM.md)
`ynJyIKwjonM` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: rag-retrieval, context-engineering, mcp-and-tools

Leonie Monigatti (Elastic) argues context engineering is mostly agentic search, then walks through live demos of semantic search, ES|QL query tools, skill loading, and grep-style shell search, and when to use each.

- Techniques: Layered tool descriptions; Errors returned to the agent; Progressive disclosure for skills; Outsource aggregation to the search engine; Shell tool with semantic grep; Hybrid shell plus database verification; Log tool calls to find where specialization is needed; Use the file store as memory and offload old results
- Tools: LangChain, Elasticsearch, ES|QL, Jina embeddings v5, Jina grep (captioned as Gina grep), OpenAI GPT-5.4 nano and mini, shell / bash tool, Claude Code, OpenClaw (captioned as OpenCloud, exec tool)

## [Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor](../videos/WE_Gnowy3uw.md)
`WE_Gnowy3uw` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: coding-agents, multi-agent, evals

Cursor's David Gomes on replacing its git-worktree and best-of-N feature (about 15K lines deleted) with one markdown skill plus subagents, and what was lost in the swap.

- Techniques: Skill as the orchestrator for a stateful workflow; Best-of-N through one subagent per model; Commands instead of skills for server-controlled prompts; Prompt-level containment with system reminders; Two-scorer isolation eval run headlessly; Feeding failure cases into RL training
- Tools: Cursor (2.0 and 3.0), Cursor CLI (headless), Git worktrees, Agent skills, Subagents, Slash commands, Composer (Cursor's own model, version 2 mentioned), Braintrust, Kimi, Grok, GPT, Opus

## [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../videos/_QAVExf_1uw.md)
`_QAVExf_1uw` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: context-engineering, rag-retrieval, enterprise-adoption

A staff engineer at IKEA argues enterprise agents fail on undocumented institutional knowledge, and proposes a pull-based loop where agents surface knowledge gaps and curate context blocks before retrieval.

- Techniques: Pull-based knowledge capture from failed agent runs; Failing-tasks-as-tests for knowledge bases; Historical-incident replay as a probe source; Three-step gap scanner: probe generation, probe run, gap analysis; Freshness labels, flagged for human decision; Git-backed curated context blocks with a metamodel; 80/20 context cache with links to the monolith; Full-context before graph RAG, for small domains; Claude Code skills, rules, agents and hooks as the implementation
- Tools: Claude Code, GitHub Copilot, Confluence, Jira, Slack, GitHub, MCP, RAG, GraphRAG, Replit, Kanban board

## [Agents need more than a chat - Jacob Lauritzen, CTO Legora](../videos/XNtkiQJ49Ps.md)
`XNtkiQJ49Ps` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: product-ux, agent-architecture, evals

Legora's CTO argues that vertical agents need more than chat: make work verifiable, let humans steer through skills and decision logs, and use persistent artifacts as the collaboration surface.

- Techniques: Proxy verification with golden examples; Task decomposition by verifiability; Allowlist guardrails for agent actions; Skills as judgment encoded at work nodes; Elicit-or-decide with a decision log; Persistent, scoped artifacts as the collaboration surface
- Tools: Claude Code

## [Context Is the New Code — Patrick Debois, Tessl](../videos/bSG9wUYaHWU.md)
`bSG9wUYaHWU` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: context-engineering, evals, security-guardrails

Patrick Debois argues that agent context (instructions, skills, specs) needs its own lifecycle like code: generate, test with evals, distribute as packages, observe logs, then adapt.

- Techniques: Layered context tests (lint, judge, end-to-end); Repeated runs with error budgets; Commit-scoped context A/B scenarios; Turning feedback into context fixes; Context filter before loading; Packaging context with provenance and scanning; Parallel generation as a spec-quality check
- Tools: Claude Code, AGENTS.md, CLAUDE.md, SKILL.md, MCP, Tessl, GitHub, GitLab, Slack, Snyk, Gemini, GitHub Copilot

## [LLM codegen fails and how to stop 'em — Danilo Campos, PostHog](../videos/juoNbJiZUi0.md)
`juoNbJiZUi0` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: coding-agents, context-engineering, security-guardrails

Danilo Campos (PostHog) on making an autonomous integration agent reliable: feed fresh docs, use thin "model airplane" example apps, breadcrumb the task, interrogate the agent at each stop, and lock down secrets.

- Techniques: Agent-selected fresh docs menu; Model airplane example apps; Breadcrumbed multi-stage prompting; Stop-hook self-interrogation; Tool-gated secret access
- Tools: PostHog Wizard, Claude Agent SDK, Claude Code, Cursor, MCP, PostHog LLM gateway

## [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google](../videos/BKWpYIWvAo4.md)
`BKWpYIWvAo4` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: local-ai, inference-serving, training-finetuning-rl

Google AI Edge on running small Gemma models on-device via LiteRT-LM, the on-device agent-skills pattern (progressive disclosure, constrained tool calls), and fine-tuning tiny models with synthetic data.

- Techniques: Progressive disclosure for skills; Three-primitive orchestrator; Constrained decoding scoped to tool calls; Synthetic data then fine-tune then quantize; Modular pipeline of small models; LoRA hot-swap on one base model; Skill testing loop with a coding agent and a device; Build-once, deploy-everywhere model file with AOT for NPU
- Tools: LiteRT-LM, LiteRT (formerly TensorFlow Lite), LiteRT-Torch, Google AI Edge Gallery, MediaPipe, Gemma 4 (E2B, E4B), Function Gemma (270M), Gemma 3 270M, EmbeddingGemma (300M), FastVLM (500M, Apple), Qwen 0.6B, Gemini CLI

## [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase — Pedro Rodrigues, Supabase](../videos/GmAQKINjv1E.md)
`GmAQKINjv1E` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: evals, claude-code, context-engineering

Pedro Rodrigues (Supabase) walks through writing agent skills, testing their triggering, and running with/without-skill evals, using a Postgres RLS view bug as the running example.

- Techniques: Progressive-disclosure skill layout; Trigger-accuracy testing via headless CLI; With/without skill eval comparison; Deterministic state assertions before LLM judging; MCP tool plus skill split for data access; security_invoker for Postgres views over RLS tables; Skill install via npm skills package with symlinks
- Tools: Claude Code, Supabase MCP server, Supabase CLI via npx, Postgres, Next.js, Braintrust, Langfuse, Vercel skills npm package, Python (DB reset and eval scripts), VS Code

## [Hermes: The Self-Improving Agent That Gets Smarter Every Day](../videos/HdxtLpL9CC8.md)
`HdxtLpL9CC8` · Better Stack · 2026-05-02 · q3 · intro · review · also: memory, context-engineering, token-cost-efficiency

Hands-on test of Hermes, an open-source self-improving agent from Nous Research: it stores memory and writes skills from use, and the video shows how it manages context. A single-user demo, so the evidence is anecdotal.

- Techniques: Bounded memory preload plus full-text session archive; Early, selective context compression; Periodic persistence nudge; Style-learning loop that ends in a skill; Mid-session model switch for cost
- Tools: Hermes (open-source self-improving agent, Nous Research), OpenRouter (model provider; Gemma 4 selected), Gemma 4 (default model in the demo), GLM (cheaper model used mid-session; transcribed as 'glm5 turbo'), OpenClaw (compared agent, more channels and sandboxing), NanoClaw (compared agent, built on the Claude Agent SDK), Claude Agent SDK, Claude Code (compaction threshold comparison), SuperMemory (optional external memory processor), Mem0 (optional external memory processor; transcribed as 'Memzero'), OpenViking (optional external memory processor), SQLite with FTS5 (session store and search)

## [I Tried Every Skill. These Best Claude Skills Are Bizarre](../videos/qQ5uObNKBOU.md)
`qQ5uObNKBOU` · AI LABS · 2026-05-02 · q2 · intro · review · also: claude-code, testing-verification, token-cost-efficiency

Walkthrough of nine community Claude Code skills (notifications, adversarial app QA, output compression, git audit, premortem, mutation testing, plan stress-testing, Reddit research, UI color guidance). Mostly README-level tours, with a mid-video sponsor segment.

- Techniques: Per-event voice notifications for parallel Claude sessions; Adversarial browser QA sweep; Terse-output mode to cut response tokens; Git-history audit with a skill; Premortem pass before go-live; Mutation testing for test-suite strength; Stress-test a plan with selectable challenge modes; Fallback chain for scraping Reddit; Grounded design-reference skill for UI
- Tools: P on Ping (skill, transcript name), Claude Code, agent-browser (CLI), Dogfood skill, Caveman plugin, Git, Git Time Travel skill, Premortem skill, Mutation testing skill, The Fool skill, Gemini CLI, tmux

## [This Claude Skill Cuts Your Token Costs In HALF](../videos/RuH3uiJy84A.md)
`RuH3uiJy84A` · Better Stack · 2026-05-02 · q2 · practitioner · review · also: token-cost-efficiency, claude-code, context-engineering

Better Stack tests Caveman, a Claude Code skill that makes answers terse to cut output tokens. Output savings are real (45%), but the skill's own input overhead erases them on single prompts.

- Techniques: Terse-output skill file; Three-arm token A/B; Count the instruction file as input cost; Compressed instruction files; Terse commit and review outputs
- Tools: Claude Code (captions say 'claw code'), Codex (named as compatible), Caveman skill, Next.js (demo app), Better Stack RUM (demo app context), skills package installer (name garbled in captions as 'Vasell'), prompt caching (provider feature referenced by the presenter)

## [The Claude Code Skill Boris Cherny Runs on Every Project](../videos/AhXfI1rSUPc.md)
`AhXfI1rSUPc` · AI LABS · 2026-05-02 · q2 · practitioner · review · also: claude-code, multi-agent, testing-verification

A walkthrough of skills, plugins and slash commands the Claude Code team reportedly uses, including batch worktree fan-out, a verify skill and an end-of-session tech debt skill. Several are internal and unverified, and a sponsor segment is included.

- Techniques: Batch fan-out with worktrees; Project-specific verify skill; Skillify-style session capture; End-of-session tech-debt pass; Inner-loop slash commands; Issue dedupe with a confidence threshold; Security scan, then fix
- Tools: Claude Code, Claude Code batch command, git worktrees, frontend-design plugin, Code Simplifier plugin, Simplify (built-in), Claude Code security scan (built-in), commit command plugin, Remotion skill, skill creator skill, Skillify (internal), verify skill (internal)

## [How to Use Google Stitch to Make Sites 10X More Beautiful](../videos/b0lwCDNOFUY.md)
`b0lwCDNOFUY` · AI LABS · 2026-04-02 · q2 · practitioner · tutorial · also: vibe-coding-app-building, coding-agents, context-engineering

Tutorial on pairing Google Stitch with Claude Code: design.md design systems, screenshot-based redesign, Stitch skills and MCP, then React and shadcn conversion. Includes sponsor segments.

- Techniques: design.md-first design system; Extract design.md from an existing Stitch project; Screenshot as style reference (Redesign); Import style from a URL; Sketch plus theme to correct drift; Annotate-and-apply targeted edits; CLAUDE.md pipeline for Stitch skills; Convert a Stitch project to shadcn/ui
- Tools: Google Stitch, Claude Code, design.md, Stitch MCP, Stitch Enhance Prompt skill, Stitch Loop skill, Stitch React component skill, Stitch design.md skill, Google Stitch skills repo, Chrome DevTools, NanoBanana (image generation), GoFullPage (Chrome extension)

## [OpenClaw Agents Just Got Better With This](../videos/JC53AcoFh-Q.md)
`JC53AcoFh-Q` · AI LABS · 2026-04-02 · q2 · intro · review · also: security-guardrails, multi-agent, memory

A tool roundup for hardening and extending OpenClaw agents: a security skill suite, a deterministic multi-agent workflow runner, a hybrid memory plugin, a network-API browser skill, Cloudflare hosting, a dashboard, and a curated skill list.

- Techniques: Installing a skill from git when the registry is rate-limited; Self-verifying skills: checksum check with re-download on mismatch; Scheduled security heartbeat over installed skills; Deterministic multi-agent workflow with verifier and fresh contexts; Re-ranked hybrid memory as an agent memory plugin; Replaying site APIs with cookies instead of driving a browser visually; Filtering a large skill registry before installing
- Tools: OpenClaw, ClawSec, Prompt Security, Heartbeat skill, Soul Guardian, OpenClaw Watchdog, Antfarm, Ralph Loop (creator's earlier project, per speaker), AI Dev Task (creator's earlier project, per speaker), ClawHub (skill registry), Awesome OpenClaw Skills (curated list), MemoryLanceDB Pro

## [This Changed The Way I Design With AI](../videos/sdxJEd7nqiQ.md)
`sdxJEd7nqiQ` · AI LABS · 2026-03-02 · q3 · practitioner · review · also: claude-code, coding-agents, product-ux

Pencil.dev design-to-code workflow with Claude Code: a file-watcher syncs .pen edits to code, subagents build pages, and a UX-audit skill raised the site grade from C to B.

- Techniques: Design file as a repo artifact; Save-triggered sync watcher; Pre-approve permissions for unattended claude runs; One subagent per page with shared docs; XML-tagged task prompts; Layer Lenis over GSAP for scroll; UX Audit skill with a scored re-run loop
- Tools: Pencil.dev, Claude Code, Claude CLI, Claude Opus 4.6, Codex, Figma MCP, Stitch, Bolt, npm, Git, GSAP, Lenis

## [Anthropic Released Another Official Process](../videos/aEqKWI-0N0c.md)
`aEqKWI-0N0c` · AI LABS · 2026-03-02 · q2 · practitioner · tutorial · also: context-engineering, claude-code, testing-verification

A team rebuilds a Nano Banana image skill for Claude Code, then shows the skill-design fixes that mattered: trigger-rich descriptions, progressive disclosure, scripts, validation gates and error tables.

- Techniques: Trigger-rich skill descriptions with negative triggers; Three-level progressive disclosure layout; Move constraints out of prompts into post-processing; CLI scripts with modes and a preview mode; Two-stage validation gates with regenerate-on-fail; Error table with error, cause, and fix; Split domain knowledge into reference packets; Iterate against real outputs and refresh the skill-creator
- Tools: Claude Code, Google Antigravity, Nano Banana Pro, skill-creator (Claude Code official skill), Next.js, Cream (sponsor, merchant of record), Cursor, Windsurf

## [This Is The Only Claude Code Plugin You'll EVER Need (Superpowers)](../videos/lq3rzXP4_vs.md)
`lq3rzXP4_vs` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: claude-code, multi-agent, testing-verification

Walkthrough of Superpowers, a Claude Code skills plugin that forces brainstorm, planning, sub-agent TDD and per-step commits. It beat plain plan mode in one demo, but the agent skipped TDD once.

- Techniques: Brainstorm into a design doc before code; Split the design into sub-agent-sized tasks; Pick the execution mode deliberately; Per-task red-green loop with a git commit per step; Plan doc, clear context, then execute (presenter's own workflow, not part of Superpowers)
- Tools: Superpowers (agentic skills framework / Claude Code plugin; 14 skills per the presenter), Claude Code, Opus 4.6 (Anthropic model, used for both builds), React, Vite, Hono (server framework), CSS-in-JS styling library (unnamed in the video), Tailwind CSS (suggested by the presenter in hindsight, not used), XDL (CLI that downloads videos from Twitter; the demo app wraps it), git, Beads (planning tool, comparison only), spec-kit (spec-driven development, comparison only)

## [This Just Fixed 90% of AI Coding Errors](../videos/romGzY0Xu0s.md)
`romGzY0Xu0s` · AI LABS · 2026-03-02 · q3 · practitioner · review · also: coding-agents, testing-verification, multi-agent

AI LABS team tests the Superpowers Claude Code plugin on a Trello-style app: enforced brainstorm, plan, subagent, TDD and review gates work, but they burn context fast and are best used selectively.

- Techniques: Install a workflow plugin from a marketplace in Claude Code; Brainstorm-gated kickoff prompt; Subagent-driven implementation with worktrees and review gates; Anti-test-edit TDD cue; Four-phase systematic debugging prompt; Compact before the next feature; Selective process use; Re-invoke skills after context loss
- Tools: Claude Code, Superpowers (Claude Code plugin), git, git worktrees, BMAD, OpenSpec, Trello (the example app being cloned)

## [You Need To Know This Before Installing OpenClaw](../videos/M3P0hQMQtq0.md)
`M3P0hQMQtq0` · AI LABS · 2026-03-02 · q3 · practitioner · review · also: security-guardrails, token-cost-efficiency, sandboxing-execution

AI LABS tests the self-hosted agent OpenClaw and finds it costly (token-heavy context, heartbeats), slow as context grows, and risky (plain-text credentials, malicious community skills, prompt injection); it closes with mitigation advice.

- Techniques: Hard budget and alerts on the model API key; Reduce idle token burn; Vet community skills before install; Sandbox the agent; Least-privilege channel tokens; Prefer providers with built-in guardrails, with caution
- Tools: OpenClaw, Claude (former Claudebot name), OpenAI API, Anthropic models, OpenRouter, Ollama, Docker, Cisco open-source skill scanner, Discord, WhatsApp

## [I Didn't Expect This From OpenAI's IDE](../videos/sC4JpJlD3aQ.md)
`sC4JpJlD3aQ` · AI LABS · 2026-03-02 · q3 · intro · tutorial · also: coding-agents, multi-agent, vibe-coding-app-building

A 7-minute build log: turning a car photo into a 3D hero section for a Next.js landing page with Tripo 3D, OpenAI's Codex app, GSAP and Aceternity UI, with parallel Codex subagents in git worktrees.

- Techniques: Pre-clean the image for image-to-3D; GLB asset in a Next.js public folder; Generate a project skill with the agent's skill creator; Work around agent install timeouts; Parallel subagents in separate git worktrees; Scope the agent with explicit do-not-touch constraints; Fix visual drift with screenshots and named variants
- Tools: Codex app (OpenAI), Tripo 3D, Canva background remover, Next.js, GSAP, Aceternity UI, React Three Fiber, post-processing package for React Three Fiber (named 'Post Processing' in the transcript), npm, GLB (file format), Antigravity (agent manager, compared in passing), Claude Code (mentioned as the previous agent used)

## [The Last Claude Code Tutorial You'll Ever Need](../videos/EHDzlot7LKU.md)
`EHDzlot7LKU` · AI LABS · 2026-02-02 · q3 · intro · tutorial · also: context-engineering, claude-code, multi-agent

Principles for building your own agent workflow in Claude Code: progressive disclosure, external note files, context-budget hygiene, subagents, git and slash commands.

- Techniques: Progressive disclosure via skills; External note files for long tasks; Manual context hygiene; Delegating research to subagents; Format selection for context files; Git as memory and parallelism; Slash commands for repeated procedures
- Tools: Claude Code, Claude (Anthropic models, 200k context), Gemini (1M context), Sonnet 4.5, BMAD, SpecKit, agent.md / AGENTS.md, CLAUDE.md, Jira MCP, Figma MCP, Git, git worktrees

## [Skills Had ONE Job (They Failed)](../videos/i0W90tlKfYg.md)
`i0W90tlKfYg` · Better Stack · 2026-02-02 · q4 · practitioner · review · also: context-engineering, evals, coding-agents

Vercel's Next.js eval found a passive AGENTS.md doc index beat on-demand skills (100% vs. skills that were often never invoked); skills suit explicit workflows, AGENTS.md suits framework knowledge.

- Techniques: Passive documentation index in AGENTS.md; Split context by trigger type; Measure skill trigger rate, not just existence
- Tools: Next.js, Agent Skills (open standard, Anthropic), Vercel skills CLI and skills repository (named as 'skill CLI' in the transcript), AGENTS.md, CLAUDE.md

## [Moltbook is WILD... (AI Only Reddit)](../videos/EGD1LCuoTuo.md)
`EGD1LCuoTuo` · Better Stack · 2026-02-02 · q2 · intro · review · also: security-guardrails, agent-architecture

A walkthrough of Moltbook, a Reddit-style site where only AI agents post, powered by OpenClaw; it mostly shows how steerable and security-risky the setup is.

- Techniques: Human-steered post test for agent autonomy; Markdown skill plus heartbeat as an always-on agent loop
- Tools: Moltbook, OpenClaw (the video says it was formerly called MaltBot/Moltbot and ClaudeBot), Reddit (used as the comparison), Claude Opus 4.5 (shown as the model behind one post)

## [Why Google Antigravity Suddenly Makes Sense](../videos/e4giCKHIJy8.md)
`e4giCKHIJy8` · AI LABS · 2026-02-02 · q2 · practitioner · review · also: coding-agents, context-engineering, testing-verification

A walkthrough of Google Antigravity as a coding agent, using Cursor's published harness principles: plan-first with commented revisions, on-demand context, TDD, Git as knowledge base, and skills-based debug mode.

- Techniques: Comment-driven plan revision; On-demand context instead of manual file tagging; Conversation reset policy; Project rules as markdown in .agent/rules; Skill folders following Anthropic's open standard; TDD with a committed test baseline; Screenshot as design and bug input; Git workflows as reusable commands; Agent-run code review with severity sorting; Parallel agents on separate branches; Skill-based debug mode; Watch the agent and redirect early
- Tools: Google Antigravity (AI code editor with planning mode, rules, skills and workflows), Gemini 3 (model used in Antigravity), Claude Code, Claude Opus, Cursor, Cursor's agent harness article (referenced, not named as a product), Anthropic's long-running agent harness (referenced), Anthropic's open Agent Skills standard (SKILL.md), Git, GitHub (built-in PR code review), CodeRabbit, Sentry

## [How I Made Claude Code WAY Better With Vercel Agent Skills](../videos/PkeC2hNQ9Zw.md)
`PkeC2hNQ9Zw` · Better Stack · 2026-02-02 · q2 · intro · review · also: coding-agents, claude-code

Better Stack explains the Agent Skills format, Vercel's add-skill installer and skills.sh discovery, and Cloudflare's proposed well-known skills index, then closes with a sponsor read.

- Techniques: Write a skill file with frontmatter; Install one skill into several agents; Discover skills by popularity; Publish a skill index at a well-known path (proposal)
- Tools: Claude Code, Agent Skills (Anthropic), add-skill (Vercel, npx add-skill), skills.sh, Cloudflare well-known skills index proposal, Cursor, Wrangler, Remotion, React Native skills, Better Stack

## [Claude Just Introduced a New Way To Fix Your UI](../videos/eLDq5TfIHys.md)
`eLDq5TfIHys` · AI LABS · 2025-12-02 · q2 · practitioner · review · also: claude-code, context-engineering, vibe-coding-app-building

AI LABS tests Anthropic's front-end design skill guidance in Claude Code: typography and theme prompts, a 400k-token mega-prompt, and skills that often fail to auto-load.

- Techniques: Turn a design prompt into a project skill; Force-invoke the skill by name; Describe design as implementation, not taste; Name the fonts explicitly; Stage the design prompt per dimension, then combine; Artifacts builder skill for componentized output
- Tools: Claude Code, Claude skills, Claude desktop app, Google Fonts, React, shadcn-style UI (as generated by Claude), Zen Browser, Arc Browser, Anthropic front-end design cookbook, Claude Code front-end design plugin

## [I Was Using Claude Skills Wrong... The Ultimate System](../videos/fHGMA8hLNt8.md)
`fHGMA8hLNt8` · AI LABS · 2025-12-02 · q2 · intro · review · also: claude-code, context-engineering

A list of about 21 to 22 use cases for Claude Skills, from coding tasks like tests and CI/CD to business, personal and content workflows. Mostly unmeasured ideas, with a sponsor segment.

- Techniques: Skill folder with references, assets and scripts; Test-and-report skill; Clarify then generate; Template-driven document generation; Stateful skill with a maintained data file; Saved personal profile for planners
- Tools: Claude Code, Claude Desktop app, Claude Skills, Docker, GitHub Actions, npm package (unnamed), Appify (sponsor)

## [How Claude Solved AI's Biggest Problem](../videos/Z9glbip8pZc.md)
`Z9glbip8pZc` · AI LABS · 2025-11-02 · q3 · intro · review · also: claude-code, mcp-and-tools, context-engineering

Walkthrough of Claude Skills: SKILL.md folders loaded on demand, how they differ from MCP, building one with skill-creator, and HTML visualization widgets. Mostly demo, with one sponsor segment.

- Techniques: Skill folder layout; Keep the description one line; push detail into referenced files; Install shared skills into Claude Code; Bootstrap a skill with skill-creator; Visualization widget skill
- Tools: Claude Skills, Claude Desktop app, Claude Code, skill-creator skill (Anthropic skills repo), MCP builder skill, MCP, Figma MCP server, Figma API, PDF Extractor skill, Algorithm art skill, Canvas design skill, Word, PDF, Excel and PowerPoint document skills

## [Turn Cursor AI into the 500$ Devin (Just Paste this...)](../videos/wJk2_Ds-9cM.md)
`wJk2_Ds-9cM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, context-engineering

Walkthrough of a Cursor rules file that adds a lessons log and task scratchpad, used to build a full-stack Trello clone; one anecdotal demo with overstated "Devin" framing.

- Techniques: Per-project .cursor rules file; Lesson log inside the rules file; Scratchpad task plan with checkboxes and a current-focus section; Generate the rules prompt with another model, then run it in the IDE agent
- Tools: Cursor, Cursor Composer, Windsurf, Devin, GPT (used to write the prompt), PostgreSQL, Docker, OpenAI API (gpt-4 model name), Trello (clone target, not a tool used)

