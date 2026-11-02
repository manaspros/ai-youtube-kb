# AI LABS (@AILABS-393) — 285 of 289 videos have notes

*Claude Code and AI-coding workflows, new tools, build-with-AI tutorials* · [channel](https://www.youtube.com/@AILABS-393/videos)

Top categories: [coding-agents](../categories/coding-agents.md) (167) · [context-engineering](../categories/context-engineering.md) (127) · [claude-code](../categories/claude-code.md) (98) · [mcp-and-tools](../categories/mcp-and-tools.md) (78) · [vibe-coding-app-building](../categories/vibe-coding-app-building.md) (76) · [multi-agent](../categories/multi-agent.md) (64) · [testing-verification](../categories/testing-verification.md) (47) · [token-cost-efficiency](../categories/token-cost-efficiency.md) (46) · [skills-self-improvement](../categories/skills-self-improvement.md) (38) · [models-research](../categories/models-research.md) (29) · [product-ux](../categories/product-ux.md) (29) · [agent-architecture](../categories/agent-architecture.md) (24)

Newest first.

## [Anthropic Just Released A New System For Using Claude Code](../videos/S49gppZl8H0.md)
`S49gppZl8H0` · AI LABS · 2026-10-31 · q2 · practitioner · tutorial · topics: claude-code, pr-code-review, testing-verification, multi-agent

Walkthrough of Anthropic's Claude Code review system, rebuilt as skills: eval.md gates before build, a fresh-context builder/verifier/reviewer loop, risk tiers, and git rollback.

- Techniques: Eval-first feature gating; Fresh-context builder/verifier/reviewer loop; Reviewer loop stop rules; review.md with a learned-rules section; Consequence-based risk tiering; First-time-user agent test; Git branch per feature with rollback
- Tools: Claude Code, CLAUDE.md, review.md, eval.md, state.md, Claude Code code review command, skills, subagents, hooks, git, Codex, Cursor

## [This Is Microsoft's New Tool Finally Fixed Claude's Usage Limits](../videos/1kQ_1_QL5Es.md)
`1kQ_1_QL5Es` · AI LABS · 2026-10-29 · q2 · practitioner · review · topics: token-cost-efficiency, claude-code, skills-self-improvement, context-engineering

Walkthrough of Microsoft's Token Economizer, a Claude Code plugin that learns per-project token waste (repeated mistakes, unused tools, stuck loops) and cuts it; reports 21-31% savings and a cold-start caveat.

- Techniques: Install the plugin for your agent; Enable micro skills only for your own projects; Per-project repeated-failure facts; Prune unused tools per project, then restore on demand; Measure the tool-definition overhead; Two-step stuck escalation; Seed a new tool from existing session history; Three-hook layout for an agent harness
- Tools: Token Economizer (Microsoft; Claude Code and Codex plugin, install from GitHub repo, version not stated), Claude Code, Codex (OpenAI), GitHub Copilot, Sonnet 5, Opus 4.8, Graft (map-based token saver, mentioned as a comparison, not shown in use), Data Impulse (sponsor; residential proxy network)

## [EGM: Google's New Way To Use Claude Code Is Insane](../videos/xxf6D9jynFw.md)
`xxf6D9jynFw` · AI LABS · 2026-10-26 · q2 · practitioner · tutorial · topics: context-engineering, multi-agent, coding-agents, claude-code

Walkthrough of Google's EGM, a spec-first workflow where zero-context goldfish sub-agents critique a plan before any code is written, with install, bootstrap, review and drift steps for Claude Code. A sponsor segment caps quality.

- Techniques: Isolated-context plan critique; Multi-lens rubric reviewers; Fan-out with a single merged report; Staged plan authoring with per-section approval; Round-based review gate; Drift check against per-folder docs; Make per-folder docs agent-readable; Verify the installer's CLAUDE.md edits; Install by agent-specific command or by prompt; Command sequence
- Tools: EGM (Google Elephant Goldfish Model, free on Google's GitHub), Claude Code, Codex (named as a supported agent), Hydra (sponsor, video generation for app promos)

## [Anthropic Just Revealed How Their Engineers Use Claude Code](../videos/92ZDgn8bgLM.md)
`92ZDgn8bgLM` · AI LABS · 2026-10-22 · q3 · practitioner · tutorial · topics: claude-code, context-engineering, multi-agent, testing-verification

AI Labs video on Felix Rieseberg's article: get more from Claude Code by asking for outcomes, expert methods, varied viewpoints, an outside judge, and the tools to verify results.

- Techniques: Outcome-first prompt (altitude); Expert-method meta-prompt (depth); Impossible-sounding goal reframing; Outside judge via a second model; Noun-to-verb role discovery and sequential specialist sub-agents (range); Verification resources for agents
- Tools: Claude Code, Claude (Anthropic), Codex CLI, MCP (Model Context Protocol), GoLogin (sponsor segment, not a recommended tool), AI Labs Pro (paid community, mentioned in closing)

## [Vercel's CEO Just Unveiled The Greatest AI Coding Workflow Ever](../videos/y2ifUC9_zuU.md)
`y2ifUC9_zuU` · AI LABS · 2026-10-20 · q2 · intro · tutorial · topics: context-engineering, testing-verification, claude-code, security-guardrails

Recap of a Vercel CEO interview: judge progress by direction rather than volume, run a plan-drift "direction" check, and use breaker, first-time-user and E2E agents plus MCP-based feedback triage. Partly a sponsor segment, with thin detail.

- Techniques: Direction drift-check command; Specs-first project setup; Must-not-trade-off rules with runnable tests; Quality gate checklist; Breaker agent loop; First-time-user agent with a hook-restricted bash tool; E2E path agent with JSON results; DeepSec security scan; Feedback triage with MCP connectors
- Tools: Claude Code, CLAUDE.md, DeepSec (Vercel security scanner), Gmail MCP, Sentry MCP, Victor (sponsor, AI hire in Slack/Teams)

## [GitHub's #1 Trending Skill Is Insane (5 Use Cases)](../videos/rw0fqnrZgNM.md)
`rw0fqnrZgNM` · AI LABS · 2026-10-19 · q2 · practitioner · review · topics: claude-code, skills-self-improvement, testing-verification, security-guardrails

Walkthrough of the Reverse Engineer Anything (REA) MCP skill for Claude Code: feature cloning, black-box QA, competitor teardown, security sweep. Takeaway: tag findings by evidence, not guesses.

- Techniques: Behavior spec before implementation; Evidence-tagged findings; Black-box feature QA; Check the site against your written rules and promises; Competitor teardown; Pre-publish security and performance sweep
- Tools: Claude Code, Codex, Reverse Engineer Anything (REA) MCP server and skill, Hopper (binary analysis, optional), Firecrawl MCP server (sponsor), Notion MCP, Obsidian, Notion, OpenAI API, Stripe, GitHub

## [Google Just Fixed AI Design By Releasing This](../videos/au2TI8sdq8E.md)
`au2TI8sdq8E` · AI LABS · 2026-10-19 · q3 · practitioner · tutorial · topics: coding-agents, context-engineering, skills-self-improvement, testing-verification

Google's Stitch design tool now has a terminal CLI, so Claude Code can drive it through a brief-to-design-to-site workflow with review and story-review skills; the video is a tutorial-style walkthrough with a sponsor segment.

- Techniques: Stitch CLI install with the skill in .claude; brief.md interview before any design generation; Loop of generate, check, and re-prompt in Stitch; Build from Stitch via download of HTML, images and fonts; Two-stage review: design fidelity, then story quality
- Tools: Stitch (Google), Stitch CLI, Claude Code, Stitch skill, scrollytelling skill, design.md, brief.md, Whisperflow (sponsor)

## [6 Insane Trending GitHub AI Design Repos You Need to Use](../videos/NZjjmf3I6I4.md)
`NZjjmf3I6I4` · AI LABS · 2026-10-19 · q2 · practitioner · review · topics: coding-agents, skills-self-improvement, mcp-and-tools, multi-agent

Walkthrough of six GitHub repos that give coding agents design references, multi-viewport checks, design-token extraction, multi-agent page builds, app-store screenshots and launch-video generation. Mostly sponsored tool demos with little measurement.

- Techniques: Reference-first design with an awards MCP; Post-build responsive check with Responsively MCP; Design taste skills, chosen by scope; Extract and diff design tokens with Dembrandt; Generate app-store screenshots with a local editor project; Launch video with Brag, with a verification pass
- Tools: Awards MCP (awards setup and awards inspiration commands), Klein CLI (caption spelling; probably Cline), sponsor, Kleinpass (caption spelling; probably ClinePass), sponsor, open-weight model access, first-month discount link, Whisperflow landing page (probably Wispr Flow, used as a reference site), Butter.Video (animation reference site), Responsively (Mac app and MCP server), Genjutsu skills: Cast, Paint, Bunshin, taste skill and hallmark (previously covered by the channel), Dembrandt (skill, design.md output), App store screenshots skill and local editor, Brag / Bragg (brag command, Full Mode and Slim Mode), Hyperframes (video framework used by Brag Full Mode)

## [This Just Fixed Your Claude Code Setup's Biggest Flaw](../videos/jlEMo6Dsh9E.md)
`jlEMo6Dsh9E` · AI LABS · 2026-10-12 · q2 · practitioner · review · topics: claude-code, testing-verification, context-engineering, token-cost-efficiency

Walkthrough of eight Claude Code add-ons, mostly from one vendor, that put an LLM yes/no judge at decision points: action gating, rule checks, stop gates, message routing, compaction, file shortlisting and SEO audits.

- Techniques: Judge-gated pre-action hook (Toolgate pattern); Rules-to-rubric compilation (Abide pattern); Completion gate with a confidence threshold (Belay pattern); Three-way routing of mid-run messages (Steer/Queue/Interrupt); Advised compaction timing; Shortlist-then-read file retrieval (Quicksilver pattern); Browser-driven test pass with judge verdicts; Site audit with a fixed checklist plus per-page judgment
- Tools: Claude Code, Codex, Jev (decision model; name as transcribed, provider TypeSafe), Toolgate, Abide, Jev Browser, Jev Belay, Jev Steer/Queue, Compact Advisor, Quicksilver, Jev SEO, OpenRouter

## [Claude Mods Are Insane... You Need To Try These Right Now](../videos/ERNqRK6sMJY.md)
`ERNqRK6sMJY` · AI LABS · 2026-10-12 · q3 · practitioner · review · topics: claude-code, context-engineering, multi-agent

AI LABS demos seven Claude Code "mods" they built (prompt enhancer, design picker, assumption reviewer, idea shelf, session dashboard, same-folder tracker, plain-language answers) and explains how to create and install them.

- Techniques: Build a mod from a prompt; Prompt enhancer before send; Assumption ledger with targeted correction; Visual option picker before a design choice; Two-pass answer rewrite with a cheap check
- Tools: Claude Code, Claude mods (Claude Code feature), plugin-authoring skill, Haiku model (answer rule check), Runway, Gen-4.5 (Runway video model, sponsor segment), Stride (AI LABS' own running-coach app, sponsor segment)

## [Claude Code Features That 90% Don't Know Exist](../videos/i6Q7bXnWGlM.md)
`i6Q7bXnWGlM` · AI LABS · 2026-10-12 · q3 · practitioner · tutorial · topics: claude-code, context-engineering, token-cost-efficiency

Walkthrough of about 20 hidden Claude Code settings, commands and shortcuts for context hygiene, permissions, plan mode, multi-session work and model routing, with exact setting names.

- Techniques: Enable New Init; Import setup from another agent; Prompt audit after a model release; Prune skills by token cost and usage; Auto Mode Setup; Fewer permission prompts allowlist; Disable connectors and artifacts; Build eval and hillclimb for LLM apps; Clear context on plan accept and save plans in-repo; Output styles; Show thinking summaries; Focus mode; Branch, fork and subtask; Cross-session messaging; Ask User Question Timeout and notifications; opusplan model routing; Pin sub-agent model; Prompt-editing shortcuts
- Tools: Claude Code, Claude app (connectors, artifacts), Claude.md, Claude API command (prompt audit, build eval, hillclimb), Codex, Cursor, Opus, Sonnet, Scrimba Explain (sponsor)

## [He Finally 10x Claude Code With This Method](../videos/qLfSDQ5NGh0.md)
`qLfSDQ5NGh0` · AI LABS · 2026-10-05 · q3 · practitioner · tutorial · topics: claude-code, testing-verification, skills-self-improvement, multi-agent

Walkthrough of a Karpathy-style loop for Claude Code: frozen checks, fresh builder subagents, and an outer loop that rewrites instructions from failure logs. The "10x" claim is not measured.

- Techniques: Loop-fit test before building a loop; Project-context skill as app memory; Write, review, approve, lock, and commit checks; Fresh feature-builder subagent per feature, with a results file; Karpathy-style keep-or-undo loop with program.md; Outer auto loop that rewrites instructions from failures; Wire-up and sweep instructions
- Tools: Claude Code, Karpathy autoresearch (Auto Research), Upstash Box (sponsor; per-agent cloud sandbox), Approve Checks (custom script), program.md, features.md (feature tracking file), results file (custom per-round log), Project Context skill (custom), build skill (custom), write checks skill (custom), auto loop skill (custom), feature builder agent (custom subagent)

## [Shopify Just Released The Greatest AI Coding Workflow Ever](../videos/bBMp5tLxShQ.md)
`bBMp5tLxShQ` · AI LABS · 2026-10-02 · q2 · practitioner · tutorial · topics: software-factory, multi-agent, testing-verification, claude-code

AI LABS rebuilds Shopify's checkpoint-and-gates agent loop as a Claude Code orchestrator skill; the key idea is enforcing gates with a stop hook, not advisory rules.

- Techniques: Checkpointed build with human plan approval; Stop-hook gate; Test-first behavior gate without a browser; Prototype-driven visual gate; Adversarial critic and fixer loop; Learnings file for cross-task feedback; Single orchestrator entry skill
- Tools: Helix (Shopify internal, not released), Claude Code, Claude sub-agents, Gemini (used by Shopify as UI reviewer), Hedra MCP server (sponsor segment), design.md, Ralph loop (transcribed as RALF), AI LABS orchestrator skill (their own), Checkpoint Planner agent (their own), tdd planner skill (modified, their own), prototype skill (their own), adversarial loop skill (their own)

## [Github Top Trending Tool Just Fixed The AI Agent’s Biggest Problem](../videos/cyIWQHYoUg8.md)
`cyIWQHYoUg8` · AI LABS · 2026-10-02 · q3 · practitioner · review · topics: token-cost-efficiency, context-engineering, coding-agents, rag-retrieval

Walkthrough of Graft, a free open-source CLI that builds a code knowledge graph and hooks into Claude Code to cut search turns, tokens and cost; the benchmark is self-reported by its makers.

- Techniques: Code knowledge graph for impact-aware retrieval; Pre-prompt context injection via a UserPromptSubmit hook; Hook trio for a Claude Code workflow; Pick CLI injection or MCP on-demand lookup; Long autonomous run setup for a token-hungry model; Install and initialize Graft in a Claude Code project
- Tools: Graft, Claude Code, Codex, MCP, Opus, GPT 5.6, GPT Astra (as transcribed, unverified), Fable 5.1 (as transcribed), Hydra (sponsor; API for AI generation)

## [The GPT 6 Astra Vs Claude Fable 5.1 Debate Is Finally Over](../videos/BwNNcob3-A0.md)
`BwNNcob3-A0` · AI LABS · 2026-10-02 · q2 · practitioner · review · topics: models-research, evals, token-cost-efficiency, coding-agents

Blind-judged comparison of Claude Fable 5.1 and GPT-6 Astra on the team's own client-style projects: Fable wins quality, interaction and review depth; Astra wins cost, speed, instruction following and long-running builds.

- Techniques: Blind LLM-as-judge on your own tasks; Human-in-the-loop UI review with a per-model viewer; Autonomy test with a vague brief written in the model's own prompting guide style; Track output tokens and tool calls as cost drivers; Enforce file-edit tool use and check for violations afterward; Planted-bug review test with decoys; Check whether the model changed mid-run
- Tools: Claude Fable 5.1, GPT-6 Astra, GPT 5.6 (judge model), Claude Code, Codex, Claude Opus (referenced for design comparison), Cursor (named as a place to use the Zapier SDK), Zapier SDK

## [Github #1 Trending Skill's Author Just Fixed Claude's Design Problem](../videos/Ow_z94c3wKk.md)
`Ow_z94c3wKk` · AI LABS · 2026-10-02 · q2 · practitioner · review · topics: mcp-and-tools, coding-agents, vibe-coding-app-building

Walkthrough of Inspo, a free MCP server of 832 captured sites with per-site design.md files that lets coding agents pull real references before designing. Sponsored segment; tested on one demo page.

- Techniques: Pre-build style menu; Reference provenance check; Filter-scoped reference search; Cap reference study depth; Install Inspo in user scope; Split design and animation into separate MCP lookups
- Tools: Inspo (MCP server, free, no account or API key), UI Skills MCP server, Emil Kowalski animation skill, Mengto scroll animation skill (name as transcribed), Hallmark design skill (name as transcribed), AI Labs Pro design system (community resource), Claude Code, Manid (sponsor, agent tools API gateway)

## [Insane Jev Use Cases You Need To Use Right Now](../videos/2nc_QMuNp18.md)
`2nc_QMuNp18` · AI LABS · 2026-10-02 · q2 · practitioner · review · topics: claude-code, token-cost-efficiency, context-engineering, pr-code-review

AI LABS shows seven Claude Code workflow hooks that offload yes/no, ranking and routing decisions to "Jev", a decision-only model with a confidence value, to cut latency and token spend.

- Techniques: Decision-model offload via gateway; Compaction replacement via project-local hook; Doc-rule to test coverage hook; Per-prompt skill picker hook; Keyword search then batched LLM rerank for Explore; Seven yes/no review gate; Browser agent with model-picked clicks; Pre-edit rule enforcement hook
- Tools: Jev (TypeSafe decision model, as auto-captioned), Vercel AI Gateway, OpenRouter, Claude Code, Codex, Fast Jev Compaction plugin, Claude Code Explore subagent, Opus (caption reads 'Opus 2'), Zapier (sponsor segment)

## [Grok Bot Use Cases That Are Actually Insane](../videos/90pwPVrydHg.md)
`90pwPVrydHg` · AI LABS · 2026-10-02 · q2 · intro · review · topics: multi-agent, voice-multimodal, testing-verification, product-ux

Walkthrough of GrokBot's eight use cases: a hosted, always-on bot group sharing one logged-in browser, used for app testing, support triage, monitoring and AI-search checks. Light on setup detail; sponsor and paid-tier plugs.

- Techniques: Role-bot test fan-out with a lead bot; Backend-verified UI failure triage; Agent-triggered test round; Support email to draft reply and PR; Fresh-account onboarding audit; Unbranded AI-search visibility check; Scheduled morning monitoring routine; Coordinator bot over functional bots
- Tools: GrokBot, Grok, SuperGrok, Cursor, Hermes, Claude Code, Codex, Supabase, Stripe, Gmail, Sentry, GitHub

## [Claude Code + GPT 6 Astra Just Killed AI Video Editing](../videos/p565AqELA8M.md)
`p565AqELA8M` · AI LABS · 2026-10-02 · q2 · practitioner · tutorial · topics: claude-code, coding-agents, voice-multimodal, token-cost-efficiency

Tutorial for making agent-generated product videos in Claude Code: plan first, review in the browser, render shots one by one, then add music. Sponsored in part, and the title oversells it.

- Techniques: Route Claude Code to a Codex subscription via a local proxy; Plan-first with browser preview, comments, and an explicit lock; Render shots individually at full resolution, approve, then fix; Polish and combine with explicit timing; Music skill driven by plan style and shot cadence
- Tools: Claude Code, GPT-6 Astra (OpenAI model, accessed through Codex), Codex, CLI Proxy API, Homebrew (brew), Hyperframes (video-creation tool with skills), Mixkit (free music library), Luma Ray 3.2 (sponsor), Ray 3 (comparison), Kling 3.0 (mentioned in sponsor segment), Gen 4.5 (mentioned in sponsor segment), Fable (model compared to Astra on design in an earlier video)

## [You Are Using Fable 5.1 Wrong (Do This Instead)](../videos/7au4tWVG8a0.md)
`7au4tWVG8a0` · AI LABS · 2026-10-02 · q3 · practitioner · review · topics: claude-code, token-cost-efficiency, context-engineering

Practical tips for getting better results and lower cost from Anthropic's Fable 5.1 in Claude Code: lower effort, prune old-model instructions, scope edits, and give whole-feature prompts. Mostly anecdotal.

- Techniques: Start at low effort and escalate only on evidence; Ablation test to prune CLAUDE.md; Unattended-run preamble; Explicit scope fence; Minimal-diff editing instruction; Remove mannered prose; Whole-feature prompts instead of step-by-step prompts
- Tools: Claude Code, Fable 5.1, Fable 5, Opus 5, CLAUDE.md, Claude API prompt audit (command name as spoken; exact invocation not shown), Artificial Analysis (independent model benchmarking), Porkbun (sponsor, domain registrar)

## [This New Open Source Tool Just Fixed Your Claude Code Workflow](../videos/CHHEjuNBxoQ.md)
`CHHEjuNBxoQ` · AI LABS · 2026-10-02 · q3 · practitioner · review · topics: coding-agents, context-engineering, memory, security-guardrails

Walkthrough of Agit, an open-source tool that applies git's model (repos, sessions as branches, turns as commits) to agent conversations, with sharing, revert, cross-agent fork and secret redaction.

- Techniques: Versioned agent sessions via a git-style repo; Reverting a session to an earlier turn; Cherry-picking messages between sessions; Forking a Claude Code session into Codex; Registering known passwords before a session is saved
- Tools: Agit, createagit (installer), npm, GitHub, Claude Code, Codex, AGENTS.md, CLAUDE.md, Runnable (sponsor)

## [How To Use Claude Code To Build Amazing Sites With Opus 5.5](../videos/DP7mgLUKN_U.md)
`DP7mgLUKN_U` · AI LABS · 2026-10-02 · q3 · intro · tutorial · topics: vibe-coding-app-building, claude-code, pr-code-review, context-engineering

Six-stage tutorial for building non-generic websites with Claude Code: plan mode, CLAUDE.md business context, a design-rules skill, design.md, git/GitHub/Vercel deployment, branch + PR review, and a 3D scroll skill.

- Techniques: Plan mode before building; Enrich CLAUDE.md with business context; Install and apply a design-rules skill to an existing project; Lock visual style with design.md; Commit checkpoints and set up GitHub via the CLI; Deploy from GitHub to Vercel; Feature branch, PR, and automated review loop; Scroll-driven 3D site via ScrollWorld skill
- Tools: Claude Code, Opus 5.5, Sonnet, Fable, Warp, VS Code, Next.js, Vercel, Vercel CLI, GitHub, GitHub CLI (gh), CodeRabbit

## [Insane GitHub Repos That 10x Your Codex And Claude Code Setup](../videos/Ua0APTMVcb8.md)
`Ua0APTMVcb8` · AI LABS · 2026-10-02 · q2 · intro · review · topics: coding-agents, skills-self-improvement, testing-verification, token-cost-efficiency

AI LABS tours eight GitHub tools that extend Claude Code and Codex setups: browser verification, terse output, design-skill search, planning, skill evals, and linting. Mostly README-level, with one sponsor segment.

- Techniques: Browser-verified completion check (Reticle); Staged image-to-3D reconstruction with self-comparison; Terse-output plugin with lifecycle hooks (Chisel); MCP-attached design skill search (UISkills); Interview-plan-review-verify loop (Ouroboros); Apple-native skill pack for iOS UI; Skill evaluation with Caliper; Rule-based anti-pattern guard (Antislop)
- Tools: Image-to-3JS skill (spoken 'image to 3JS', captioned 'Image23JS'; GitHub trending per the presenter), Reticle, Chisel, Caveman, Ponytail, UISkills, Manufact (sponsor; hosted MCP server deployment and publishing checks), mcp-use open-source SDK (captioned 'MCPUs'), Ouroboros, Apple SwiftUI skills repo (Liquid Glass skill, layout skill), Liquid Glass (Apple iOS 26 design system), Claude Code (plugins, hooks, Skill Doctor command)

## [Every Level Of Claude Code Loop Engineering Explained](../videos/PLyRe6Zk--8.md)
`PLyRe6Zk--8` · AI LABS · 2026-09-02 · q4 · practitioner · tutorial · topics: claude-code, software-factory, agent-architecture, testing-verification

A three-level walkthrough of "loop engineering" in Claude Code: spec-as-/goal for one feature, a queue-driven software factory with a separate adversarial reviewer per branch, then phone control of the loop. Substantive, with the skills and steps shown.

- Techniques: Spec file as a /goal with explicit verification; Queue-file tracker for overnight multi-feature runs; Builder and adversarial verifier split; Clickable HTML mock per feature as planning and verification oracle; PR as the human approval gate; CLI-based platform setup driven by the agent; Minimal CLAUDE.md that points at AGENTS.md; Mobile control of a laptop-resident Claude Code session
- Tools: Claude Code, /goal (Claude Code slash command), /loop (Claude Code slash command), Codex (said to work with the same system), GSAP, Next.js, GitHub (and gh-style CLI), Supabase (and its best-practices skill), Vercel (and deploy-to-Vercel skill), Warp, VS Code, Paseo

## [Insane Claude Design Skills You Need To Actually Build Beautiful Sites](../videos/Ysr7oNDajJI.md)
`Ysr7oNDajJI` · AI LABS · 2026-09-02 · q2 · intro · review · topics: skills-self-improvement, product-ux, claude-code

AI LABS walks through design-focused agent skill packs (Emil Kowalski, Conard Lee, Elia Design, Meng To, Jakub Krehel, Tastemaker, perception laws) for Claude Design and says they steer models away from generic layouts. Mostly an overview; little measured evidence.

- Techniques: Install and invoke a design skill in Claude Design; Layer skills by stage; Score-and-iterate loop; Regression-aware review via GitHub; Script-based reference extraction; Landing-page as one-action structure; Install only the skills that fit your workflow
- Tools: Claude Design, Claude Code, Codex, GitHub, Emil Kowalski design skills (design-engineering skill, Animate, Apple Design, animation vocabulary), Conard Lee garden skills (web design engineer skill), Elia Design landing-page skill, Meng To skills (video-to-prompt, awards-quality sites), Jakub Krehel skills (review, better layout), Tastemaker, screen critique skill, perception laws skill

## [This Claude Code Skill make Building 10x Faster](../videos/b9k-AE4v5yI.md)
`b9k-AE4v5yI` · AI LABS · 2026-09-02 · q2 · practitioner · review · topics: claude-code, skills-self-improvement, multi-agent

AI LABS walks through two Claude Code/Codex skills: one checks existing products and open-source projects before building, and one searches academic papers when nothing is shipped yet. Also covers a publish-once skill distribution setup. Partly a promo.

- Techniques: Clarify-then-search gate with logged assumptions; New-idea vs existing-project branch; Applicability-vs-scale notes for each prior-art project; Three-stage cost check; Install a skill from a GitHub link; Paper-per-sub-agent research fan-out; Publish-once, auto-pull skill distribution; Cheap-first, escalate-on-novelty cascade
- Tools: Claude Code, Codex, GitHub, Advise Project Approach (skill), NeuroArchive (skill), Head Start (skill), skills CLI, Claude Code plugins, Archive (preprint platform), Stream (chat API), Sendbird (chat API), Lovable (sponsor)

## [How To Use Claude Design To Build Beautiful Sites](../videos/bBlY5YOsKN8.md)
`bBlY5YOsKN8` · AI LABS · 2026-09-02 · q3 · practitioner · tutorial · topics: vibe-coding-app-building, coding-agents, context-engineering, skills-self-improvement

A five-stage workflow for building a site with Claude Design: write a design.md brand file first, build a design system from it, wireframe, produce the full design, then hand off to Claude Code with a Supabase backend.

- Techniques: design.md-first planning skill; Preview design.md outside the token-metered tool; Design system from design.md; Wireframe, then batched comments; Full design from a chosen wireframe; Claude Design to Claude Code handoff; Post-build design.md conformance review; Supabase skill install and MCP connection
- Tools: Claude Design, Claude Code, Opus 5, Opus 4.7, Haiku, Fable, design.md (Google format), Supabase, Supabase agent skills (general and best-practices), Supabase MCP, Supabase CLI, VS Code

## [How To Never Run Out Of Codex and Claude Usage Limits](../videos/jwje1JK8Nqs.md)
`jwje1JK8Nqs` · AI LABS · 2026-09-02 · q3 · practitioner · tutorial · topics: token-cost-efficiency, claude-code, context-engineering, coding-agents

AI Labs walks through 24 tactics for stretching Claude Code and Codex usage limits, from habits (clear, compact, rewind, one big prompt) to settings (model and effort, skill and CLAUDE.md size, memory, bundled skills, output caps, advisor).

- Techniques: Clear between unrelated tasks; Compact with explicit keep-instructions, before breaks; Rewind instead of correcting; Batch changes into one prompt; Turn off automatic session recaps (Claude Code only); Set model per task with /model and effort with /effort; Pin sub-agent model in the prompt, or route automatically with a skill; Keep skills small with reference files; Write a lean CLAUDE.md and per-folder CLAUDE.md files; Check spend with the usage command; Use a CLI instead of an MCP server when the CLI is enough (Supabase example); Turn off memory and bundled skills; Disable or cap sub-agent workflows; Filter passing tests out of tool output with a hook; Cap bash output length; Replace the built-in advisor with a custom on-demand agent; Message between Claude Code sessions with only the relevant part
- Tools: Claude Code, Codex, Claude Opus, Claude Sonnet, Claude Haiku, GPT-5.6 Sol (spoken as GPT 5.6 Soul), GPT-5.6 Terra (spoken; name uncertain), GPT-5.4 Mini, ChatGPT plans (Free, Go, Plus, Pro), Claude Pro and Max plans, Supabase, Supabase CLI

## [Buzz Just Fixed AI Agents... But It Has A Serious Flaw](../videos/a8tLTd4q-fU.md)
`a8tLTd4q-fU` · AI LABS · 2026-09-02 · q2 · practitioner · review · topics: multi-agent, token-cost-efficiency, coding-agents

AI LABS tests Buzz, an open-source group-chat app where Claude and GPT agents share channels; they find real coordination and token-cost problems but praise its per-agent attribution and cross-vendor adversarial review, and say solo builders should skip it.

- Techniques: Role-explicit prompt for multi-agent planning; Cross-vendor adversarial review of a spec; Per-agent identity and attribution in a shared channel; Agent export with memory; Installing Buzz
- Tools: Buzz (v0.5, open-source group-chat app for agents), Claude Code, Claude Code agent teams, Codex (OpenAI coding agent), GPT (OpenAI model), Goose (coding agent), Slack, Claude Tag (Anthropic Slack agent, team and enterprise plans), OpenAI Codex plugin for Claude Code, EgoLite (sponsored browser-agent skill, Mac only), GitHub, Vercel

## [This Claude Skill Just Fixed Loop Engineering](../videos/D_uojDHkbw4.md)
`D_uojDHkbw4` · AI LABS · 2026-09-02 · q3 · practitioner · tutorial · topics: multi-agent, testing-verification, coding-agents

Explains the "gauntlet loop" (agent builds, critic sub-agents judge against a reference) and its two failure modes, then shows a planning-skill fix: a settled spec and pass/fail answer key the critic checks against.

- Techniques: Three-line gauntlet loop prompt; Swap the reference for a planned answer key; Planning fog map; Phased build order inside one loop
- Tools: Claude Code, Wayfinder (Matt Pocock planning skill), Grill Me (Matt Pocock skill), Matt Pocock skill set (installed from GitHub), Claude Max plan, Claude API (cost comparison), SerpAPI (sponsor, not used in the method)

## [Hermes Agent Skills That Make It 10x More Powerful](../videos/WJgxX0Eib6k.md)
`WJgxX0Eib6k` · AI LABS · 2026-09-02 · q2 · intro · review · topics: context-engineering, skills-self-improvement, token-cost-efficiency, multi-agent

Walkthrough of third-party skills for the Hermes agent (planning-with-files hook, Delegate Setup, RTK, Mantis security reviews, Agent Reach, Skill Retriever), most of which work with any coding agent; thin on exact commands and partly sponsored.

- Techniques: File-backed plan injected by a hook; Orchestrate several installed coding agents from one agent; Route shell commands through RTK via a skill; Scheduled security review with alerts; Retrieval-filtered skill list
- Tools: Hermes Agent, Claude Code, Codex, Cursor, planning-with-files, Delegate Setup, RTK, Mantis (Google), Agent Reach, Skill Retriever, Plural Workbench, Opus

## [These New Claude Skills Are Actually Insane](../videos/jyLKRN36-Dc.md)
`jyLKRN36-Dc` · AI LABS · 2026-09-02 · q3 · practitioner · review · topics: skills-self-improvement, claude-code, context-engineering, product-ux

AI LABS walks through six new agent skills: a self-improving skill-learning log, a four-rule coding baseline, a logged-in website CLI (OpenCLI), a variant-picker for UI, and two product-business skill sets for onboarding, paywalls, churn and validation.

- Techniques: Per-project learning log for skills; Parent-folder CLAUDE.md for base coding rules; Onboarding and paywall pattern; Cancellation save flow; Logged-in site commands via OpenCLI; Variant exploration for one UI section; Demand validation before building
- Tools: Claude Code, CLAUDE.md, Agent skills, log.md (task-observer output file), OpenCLI, Chrome extension (OpenCLI), Variate skill, Hallmark design skill (mentioned, not shown), Next.js, Supabase, Corey's 48-skill marketing collection, SVG (brand logo format)

## [This Is How Forward Deployed Engineering Is Actually Done](../videos/AD-EmZ3v6-g.md)
`AD-EmZ3v6-g` · AI LABS · 2026-09-02 · q2 · intro · tutorial · topics: enterprise-adoption, product-ux, evals, mcp-and-tools

How to do forward deployed engineering: audit a business process before building, sort each step into software, model or human, then eval against real cases. Useful method, but includes a sponsored segment and unsourced stats.

- Techniques: Shadow-and-document the process; Three-filter triage per step; Connect to existing systems instead of migrating; Keep process steps visible with checkpoints; Labelled-case eval loop; Value-and-error-cost accounting; Process audit as the first deliverable
- Tools: Claude Code (used for the internal chatbot case study), MCP (Model Context Protocol), Notion (named as the example system for MCP connection), Slack, Cursor (as a company example), OpenAI (as a company example), Anthropic (as a company example), Dex (job-matching sponsor; named in a sponsored segment)

## [GitHub's #1 Trending Author's New Claude Skill Is Insane](../videos/c47uqR7XB_c.md)
`c47uqR7XB_c` · AI LABS · 2026-09-02 · q2 · practitioner · review · topics: testing-verification, skills-self-improvement, multi-agent, coding-agents

AI LABS walks through "unlazy," an agent skill that makes coding agents prove each task is done via a gates ledger, tree decomposition and fresh-agent re-checks, plus their fix for its slow sequential runs.

- Techniques: Gates ledger with verifier command; Recursive tree decomposition with depth cap; Orchestrator re-verifies sub-agent claims; Parallel sub-agents with file ownership in plan.md; Explicit give-up instead of silent drop; Installing unlazy into a project
- Tools: unlazy (agent skill; name as spoken in the video), Claude Code, Codex, Ralph loop, Claude goal command, Opus, GPT 5.6, VS Code, Data for SEO (sponsor), model router skill (generic, unnamed)

## [This New Skill Finally Solves Thinking For AI Agents](../videos/m6IXL_YGqBQ.md)
`m6IXL_YGqBQ` · AI LABS · 2026-08-02 · q2 · intro · review · topics: multi-agent, coding-agents, testing-verification, skills-self-improvement

AI LABS walks through a community "ADHD" skill that makes a coding agent ideate by fanning out isolated sub-agents, each seeded with a different frame, then scoring and merging the results; shown for test planning and pre-ship UX/churn review.

- Techniques: Frame-diversified tree-of-thought fan-out; Three-question gate before auto-invoking an expensive fan-out; Install an agent skill from a repo and fix the config folder for Claude Code; TDD test-strategy planning with PRD and tech spec linked in CLAUDE.md; Pre-launch UX and churn review by fan-out
- Tools: Claude Code, Codex, Cursor, CLAUDE.md, .agents folder (installer target), SKILL.md, Top View (sponsor; AI video skill), Kling, Sea Dance, Nano Banana

## [Claude Code Setup Guide By The Creator Himself](../videos/pGro_uKt-_M.md)
`pGro_uKt-_M` · AI LABS · 2026-08-02 · q2 · practitioner · tutorial · topics: claude-code, context-engineering, evals, token-cost-efficiency

AI LABS walks through Claude Code creator Boris Cherny's setup advice: strip your Claude Code setup to a baseline with each new model, keep only what Claude can't infer, and gate work with evals that can fail. Includes a sponsored segment.

- Techniques: Baseline-then-add-back setup audit; Usage triage; Keep-rule for CLAUDE.md; Doctor audit; Fail-able acceptance checks written first; Built-in headless browser verification; Outcome-first prompting; Escalation ladder for model mistakes; Recurring cloud routines for maintenance
- Tools: Claude Code, CLAUDE.md, Claude Code skills, MCP server, Claude Code hooks, Claude Code plugins, context command (Claude Code), usage command (Claude Code), doctor command (Anthropic), safe mode (Claude Code), headless Chrome, sub-agents

## [Anthropic Just Fixed Graph Engineering's Greatest Flaw](../videos/H7t3uUp3HVw.md)
`H7t3uUp3HVw` · AI LABS · 2026-08-02 · q2 · intro · tutorial · topics: testing-verification, multi-agent, claude-code, skills-self-improvement

Graph engineering fans agent work across parallel nodes but hides failures; the video's fix is layered verification skills built with Skill Creator, plus a fresh-context Opus second opinion.

- Techniques: Install Skill Creator as a plugin; Standalone deep-review skill; Embedded verification skill that runs after each feature; Embedded rule-gate skill; Second-opinion skill via claude -p; Headless browser for visual verification; One skill per review angle, chained by an orchestrator skill; Write build, test and lint commands into CLAUDE.md; Pin the judging node to a stronger model
- Tools: Claude Code, Claude Opus, Claude Haiku, Codex, Skill Creator plugin, verify skill, code review skill, simplify skill, design skill, design.md, second opinion skill, CLAUDE.md

## [How To Use Codex To Build Insanely Beautiful Websites Using GPT 5.6 Sol](../videos/pHstb0JGGhE.md)
`pHstb0JGGhE` · AI LABS · 2026-08-02 · q3 · practitioner · tutorial · topics: coding-agents, vibe-coding-app-building, context-engineering, skills-self-improvement

Seven-stage tutorial for building a non-generic landing page with the Codex app and GPT 5.6, using AGENTS.md, a design skill, a design.md brand file, generated images, and a deploy step. Main lesson: encode taste and brand in files, not in each prompt.

- Techniques: Scoped seed prompt; AGENTS.md via /init, plus a self-verify rule; Install a design skill and forbid the default one; Browser verification loop; design.md brand system; Plan-mode image generation into an assets folder; Screenshot-based layout cloning; Single-section component swap; Performance pass; Local commits as checkpoints; Deploy with the site skill
- Tools: Codex (in the ChatGPT app), GPT 5.6, GPT image model, Next.js, AGENTS.md, GPT Taste skill, OpenAI site skill, Anthropic front-end design skill, design.md (format introduced by Google through Stitch), Aura Build design.md library, 21.dev, Godly components

## [All The Types Of Claude Loops Explained In 13 Minutes](../videos/8wsM0euQOvc.md)
`8wsM0euQOvc` · AI LABS · 2026-08-02 · q2 · practitioner · tutorial · topics: agent-architecture, claude-code, multi-agent, testing-verification

AI LABS sorts Claude Code agent loops into five types (stateless, learning, multi-agent review, verification, workflow-improvement) with setup steps; anecdotal, with a sponsor segment.

- Techniques: Goal-command loop with tests as the acceptance criterion; Save-every-working-version rule in CLAUDE.md; Skill-improvement loop (learning loop); Multi-agent review loop with an orchestrator; Implementer vs. scorer verification loop; Workflow-improvement loop with a process optimizer
- Tools: Claude Code, CLAUDE.md, Haiku (completion checker in the goal loop), Ralph loop (named as a stateless loop example), goal command, skill loop command (name as spoken), learning.md, thermonuclear review (review skill, named as spoken), orchestrate command, review loop command, iterate command, JSON files (findings and scores)

## [7 Rules To Use GPT 5.6 Sol Better Than 90% Of People](../videos/STczJBYJf7w.md)
`STczJBYJf7w` · AI LABS · 2026-08-02 · q3 · practitioner · review · topics: coding-agents, context-engineering, multi-agent, token-cost-efficiency

AI LABS' four-day hands-on comparison of GPT 5.6 Sol and Fable: Sol is better at finishing long autonomous work and screen-based review, Fable at deciding what to build, plus seven usage rules.

- Techniques: Git checkpoint before a long autonomous run; Codex app sandbox and approval configuration; Single-session delegation of multi-session work; Role-by-role journey review after the build; One-instruction-removal test for prompts and skills; Plan with one model, build with another
- Tools: GPT 5.6 Sol, GPT 5.6 Terra, GPT 5.6 Luna, Ultra (Sol multi-agent mode), Codex (app and CLI), ChatGPT app, Fable, Opus 4.8, Opus, Sonnet, Qwen 3.6, Cursor

## [Facebook's Release Just Gave Claude Code A New Design System](../videos/-HEdqzzYKco.md)
`-HEdqzzYKco` · AI LABS · 2026-08-02 · q2 · practitioner · review · topics: claude-code, context-engineering, vibe-coding-app-building, skills-self-improvement

Walkthrough of Meta's open-source React/StyleX component library (transcribed as "Asterix"), built to be read by coding agents via a CLI, plus a sponsor read and a plug for the presenter's skills.

- Techniques: Install the design system with the package manager; Run the init command to write agent instructions; Prompt for a whole site and let the agent pull from the CLI; Generate a manifest of CLI commands and flags for grounding; Screenshot and fix loop in headless Chrome; Chain a generic anti-slop review skill after the build
- Tools: Asterix (Meta's design system, transcript name; likely a caption misspelling), React, StyleX, shadcn/ui (transcribed as ShadCN), Next.js (App Router and Pages Router), npm, Claude Code, CLAUDE.md, AGENTS.md, globals.css, headless Chrome, AI Slop Detector skill (presenter's AI Labs design system)

## [This Skill Just Made Kimi K3 a 10X Better Designer](../videos/EwTOiqWWqEc.md)
`EwTOiqWWqEc` · AI LABS · 2026-08-02 · q2 · practitioner · review · topics: claude-code, skills-self-improvement, vibe-coding-app-building, coding-agents

Walkthrough of running Kimi K3 inside Claude Code via a local proxy on a Kimi subscription, then using the Hallmark anti-slop design skill to push Kimi, Opus and Codex off their default visual styles.

- Techniques: Run a non-Claude model inside Claude Code via a local subscription proxy; Install Hallmark for the right agent; Invoke a skill manually with its slash command when the model is not Claude; Prompt Hallmark with the three pre-flight answers; Run the audit verb, then pick which findings to fix; Use the study verb, not a clone request; Manage context manually on long design sessions
- Tools: Kimi K3, Kimi Code, Claude Code, Codex, Codex app, CLIProxy API, Hallmark, Next.js, Opus 4.8, Sonnet 4.5, GPT 5.6, Fable 5

## [Fleet Engineering Is Insane... The Next Evolution Of Vibe Coding](../videos/qxjII6x2yPY.md)
`qxjII6x2yPY` · AI LABS · 2026-08-02 · q2 · practitioner · tutorial · topics: multi-agent, claude-code, sandboxing-execution, coding-agents

Walkthrough for running many Claude Code sessions in parallel: resume and handoff basics, file ownership, background dashboards, git worktrees, issue-driven orchestration, and Docker Sandbox isolation.

- Techniques: Session recovery with continue, resume, recap, export; File ownership by prompt; Plan-mode task decomposition; Handoff documents via the handoff skill; Background sessions and the agent dashboard; Git worktrees per session; Issue-driven background orchestration; Docker Sandbox for isolated execution with clone mode
- Tools: Claude Code, Claude Code plan mode, Claude Code background sessions, Claude Code agent dashboard, handoff skill, git worktrees, OpenAI Symphony, Codex, Linear, GitHub, Docker Sandbox (sbx), Docker micro-VM sandboxes

## [How To Use Claude Fable 5 Better Than 90% Of The People](../videos/GM7-ei-4Xc8.md)
`GM7-ei-4Xc8` · AI LABS · 2026-08-02 · q2 · practitioner · tutorial · topics: claude-code, token-cost-efficiency, testing-verification, multi-agent

How a small AI-coding team runs Claude Fable 5 in Claude Code: keep effort at low-high, plan big and implement small, test-first with a separate test author, and layered code and security review subagents.

- Techniques: Keep effort between low and high; PRD-first planner/implementer split; Subagent routing tiers in CLAUDE.md; Ponytail with a test net; Separate test-author subagent (TDD); Parallel scoped security review; Architecture review subagent; HTML mock-up before build; Pre-merge comprehension quiz
- Tools: Claude Code, Claude Fable 5, Claude Sonnet 5, Claude Opus, Claude Mythos, OpenAI Codex CLI, OpenAI Codex plugin for Claude Code, Ponytail, Cursor Thermonuclear Code Quality Review skill, Claude Code security review GitHub Action, CLAUDE.md, Veed (sponsor)

## [4 Ways to Actually Build Stunning Websites with Claude Code](../videos/HqD5a2Cae60.md)
`HqD5a2Cae60` · AI LABS · 2026-07-02 · q3 · practitioner · tutorial · topics: vibe-coding-app-building, claude-code, skills-self-improvement, context-engineering

AI LABS walks through four ways to get better websites and UIs from Claude Code: refresh design skills from model prompting guides, use design.md files, plan functional UIs as HTML mockups, and clone existing UIs. Mostly anecdotal, with a sponsor segment.

- Techniques: Refresh a design skill from the model's prompting guide; Mine older prompting guides for dropped fixes; Set effort by task type; Conditionally load a sub-skill from a rule; Apply design.md after generation for marketing pages; Functional UI pipeline: plan, mockups, gallery, port; Consistent variants via a shared design.md; CLAUDE.md as product context and verify contract; Verify with a sub-agent against design.md; Clone a marketing site with a capture CLI and sitemap; Clone an auth-gated app from screenshots
- Tools: Claude Code, Claude, Fable 5, Opus 4.8, Anthropic front-end design skill, design.md, GetDesign.md, GSAP, Single File CLI (as named in the video), sitemap.xml, HTML, CLAUDE.md

## [Use This To Make The Hermes Agent Basically Free](../videos/5d02TYoOzfE.md)
`5d02TYoOzfE` · AI LABS · 2026-07-02 · q2 · practitioner · tutorial · topics: token-cost-efficiency, context-engineering, agent-architecture, coding-agents

Hermes Agent cost-reduction tutorial from AI LABS: where the tokens go, and which model, context, tool, and hard-limit settings cut the bill without hurting output.

- Techniques: Audit token spend before tuning; Route auxiliary and sub-agent work to a cheaper model; Use the OpenRouter Pareto router; Match effort level to task, and turn thinking off for simple work; Compress context early with a lower threshold and target ratio; Cap tool output in context; Use ephemeral system prompts for one-session instructions; Keep knowledge in files the agent loads on demand; Undo the last message and re-prompt with the failure described; Trim tools, skills, and MCP servers to what is used; Set hard limits on output, turns, and loops
- Tools: Hermes Agent, OpenRouter, Pareto router (OpenRouter), OpenAI Codex subscription, OpenAI subscription, Claude Code, Anthropic API, Gemini, MCP servers, Slack, Luma (sponsor), config.yaml

## [They Finally Fixed Claude Code's Biggest Problem](../videos/KiTmBtyaeXg.md)
`KiTmBtyaeXg` · AI LABS · 2026-07-02 · q2 · practitioner · review · topics: security-guardrails, skills-self-improvement, claude-code

A walkthrough of NVIDIA's Skill Specter, a scanner for agent skills, plus a Claude Code wrapper that adds an LLM-based second scan through headless mode and a discover-scan-fix loop around skills.sh.

- Techniques: Two-tier skill scan before install; Use Claude headless mode as the LLM judge; Discover, scan, show, fix, rescan loop in SKILL.md; Check tool-name identity at the code-point level; Compare declared behavior with code behavior; Check dependencies against a live bad-package list
- Tools: Skill Specter (NVIDIA scanner, named by the host; version not stated), Claude Code, Claude headless mode (claude -p), skills.sh (skill registry with CLI search), OpenAI API (the AI check's default backend, per the host), Codex (mentioned only in the sponsor segment), Nimblist (sponsor; open-source visual workspace for Claude Code and Codex sessions, with a Kanban board, red/green diffs, auto-generated commit messages, and a mobile app)

## [19 Hidden Features To Unlock The True Potential Of Your Hermes Agent Setup](../videos/nN6DZi_fiSo.md)
`nN6DZi_fiSo` · AI LABS · 2026-07-02 · q2 · practitioner · tutorial · topics: agent-architecture, context-engineering, token-cost-efficiency, multi-agent

AI LABS walks through about 19 Hermes agent config settings (context limits, compression, sub-agents, auxiliary models, quick commands, checkpoints, YOLO, isolation mode) that they changed to fix workflow problems, with defaults and new values.

- Techniques: Per-profile config tuning; Compression threshold and tail tuning; Sub-agent concurrency, depth and permission settings; Cheap auxiliary models and effort control; Exec and alias quick commands; File checkpoints and rollback; Ephemeral system-prompt variable; Isolation mode for config debugging
- Tools: Hermes (agent, config.yaml, Hermes config / auth / personality / rollback commands), Claude Code (compared; dangerously-skip-permissions mode compared to YOLO), Codex (compared; compression threshold comparison), OpenRouter (provider; default auxiliary model fallback), Gemini Flash (auxiliary model used in their setup), Opus (main model example), Gemini (1M-token window model mentioned), Slack (used to coordinate the team via Hermes), Notion, Jira, Airtable (integrations named in the sponsor segment), Helix (sponsor, not evaluated)

## [These Claude Workflows Turn Claude Code Into A Whole OS](../videos/5LnwJyi1il4.md)
`5LnwJyi1il4` · AI LABS · 2026-07-02 · q3 · intro · review · topics: coding-agents, multi-agent, claude-code, token-cost-efficiency

Walkthrough of how Claude Code's pieces (CLAUDE.md, MCP, skills, loops/routines, dynamic workflows) form an "OS", with guidance on when a deterministic workflow beats goal or a plain skill; mostly a sponsored-style pitch with thin hands-on steps.

- Techniques: Start a dynamic workflow; Strict output schemas for sub-agents; Choose workflow vs goal vs skill; Convert a skill from a session; Coding-project OS setup; Second-brain audit workflow
- Tools: Claude Code, Claude Opus 4.8, CLAUDE.md, MCP, Google Calendar MCP, Notion MCP, Deep Research workflow, goal command, loops, routines, hooks, skills

## [Hermes Agent under Claude Code Is Insane](../videos/Sb96po6S67k.md)
`Sb96po6S67k` · AI LABS · 2026-07-02 · q2 · practitioner · tutorial · topics: claude-code, skills-self-improvement, mcp-and-tools, memory

Setup-and-use walkthrough for running the Hermes agent alongside Claude Code: Hermes adds persistent memory and self-evolving skills, and can run as an MCP server, cron-driven monitor, or Claude Code launcher.

- Techniques: Install Hermes and run the manual setup; Onboard Hermes with your context; Expose Hermes to Claude Code as an MCP server; Cron-driven living PRD skill from a Slack channel; Delegate feature work to Claude Code from a Hermes channel; Health-check skill loop for a deployed app
- Tools: Hermes Agent (Nous Research), OpenClaw, Claude Code, Claude Code subscription / non-interactive mode, Anthropic Agent SDK credit (policy claim), hermes setup command, hermes mcp serve command, .mcp.json, user.md and memory.md (Hermes memory files), soul file (Hermes agent personality/instructions), Hermes Skill Hub, Hermes bundled Claude Code skill

## [Google Replaced The Karpathy's LLM Wiki](../videos/k4sMSsMzX2g.md)
`k4sMSsMzX2g` · AI LABS · 2026-07-02 · q2 · practitioner · review · topics: context-engineering, memory, rag-retrieval, claude-code

AI LABS walks through Google's Open Knowledge Format (OKF), a folder, index.md and YAML-frontmatter convention for markdown knowledge bases, and reports a small team test with lower token use and faster lookups.

- Techniques: Index.md per folder as the agent's entry point; YAML frontmatter with name, description and type on every concept document; Script-first markdown-to-OKF conversion with evals; CLAUDE.md navigation section that documents the bundle; Trial on a Git branch and visualize the bundle
- Tools: Open Knowledge Format (OKF, Google), BigQuery, Claude Code, CLAUDE.md, Obsidian (comparison only), Git / GitHub, Karpathy LLM-wiki pattern (concept, not a product), Google design.md standard (named in passing), Mobbin MCP (sponsor), Cursor, Lovable, v0 (named in sponsor segment), Markdown to OKF skill (the team's own, unnamed script)

## [Insane Claude Design Skills You Need To Build Beautiful Websites](../videos/Ot582-E61ac.md)
`Ot582-E61ac` · AI LABS · 2026-07-02 · q3 · intro · review · topics: skills-self-improvement, product-ux, coding-agents, mcp-and-tools

A walkthrough of Claude design skills (Anthropic frontend-design, ShadCN, UI UX Pro Max, GSAP, Material 3, SwiftUI, Expo) for building less generic websites and mobile apps, with a sponsor segment.

- Techniques: Commit to a design direction before generating; Separate functional and marketing design skills; Pair a rules skill with a component-registry MCP; Separate layout reasoning from component work for dashboards; Use a taste preset instead of a full design system; Prefer compositor-friendly animation properties
- Tools: Claude, Anthropic frontend-design skill, Opus 4.8, Fable 5, ShadCN, ShadCN MCP, UI UX Pro Max, GSAP, Higgsfield, C-Dance (as captioned; video model), Material 3, SwiftUI

## [Loop Engineering Totally 10x Hermes agents](../videos/AQRDjI5owZI.md)
`AQRDjI5owZI` · AI LABS · 2026-07-02 · q2 · practitioner · tutorial · topics: agent-architecture, claude-code, multi-agent, skills-self-improvement

Explains "loop engineering": replacing hand-written prompts with self-driving agent loops, split into deterministic loops (tests as the goal) and non-deterministic loops (UI judged by a skill plus a second verifier model), run on the Hermes agent and Claude Code.

- Techniques: Five-step loop; Deterministic loop with tests as the goal; Adversarial builder/verifier loop for judgment tasks; Explicit verification gates and termination; External state files
- Tools: Hermes agent (always-on agent, self-evolving skills), Claude Code (non-interactive and interactive modes), Claude Code hooks, Ralph loop, Claude goal command, Goal Buddy 2, OpenClaw, GitHub CLI (gh), GPT models (named as verifier, no version given), Claude Opus 4.5 (mentioned), Fable 5 (mentioned, no detail)

## [6 Insane Hermes Agent Use Cases That You Need Right Now](../videos/qMEm1bgxnUM.md)
`qMEm1bgxnUM` · AI LABS · 2026-07-02 · q2 · intro · review · topics: token-cost-efficiency, agent-architecture, skills-self-improvement, memory

Walkthrough of six Hermes Agent use cases: cron jobs gated by a wake flag or a no-agent flag, a Slack team second brain, Gmail lead webhooks, PRD-as-skill competitor tracking, and human-reviewed social posting.

- Techniques: Pre-LLM gating with a wake-agent flag; No-agent cron jobs for deterministic checks; Ask the agent to build the automation from a prompt; Draft-then-publish content skill with human review; PRD as a skill plus scheduled research; Gmail lead-triage webhook; Profiles for isolated personas
- Tools: Hermes Agent (desktop app and TUI), OpenClaw, Claude Code (transcribed as "clawed code"), cron, Slack, Stripe, Stripe MCP, AWS, Gemini API, Google Play API, Gmail, Google Cloud

## [The Top Claude Code Features We Use](../videos/ECQA6oOyfIk.md)
`ECQA6oOyfIk` · AI LABS · 2026-07-02 · q2 · intro · review · topics: claude-code, multi-agent, pr-code-review, token-cost-efficiency

AI LABS walks through the Claude Code features its team uses most (Agent Teams, Advisor, goal, auto mode, worktree sub-agents, review commands, loop, monitor), with a Scalekit sponsor segment and little measured detail.

- Techniques: Adversarial finder/fixer agent team for code review; Cheap executor with strong advisor escalation; Goal-driven run to a verifiable end state; Auto mode instead of skip-permissions; Worktree-isolated sub-agents for design variants; Layered review commands before merge; Daily knowledge-base sync with loop; Anomaly-only monitor for agent logs
- Tools: Claude Code, Claude Agent SDK, Claude Haiku, Claude Sonnet, Claude Opus 4.8, tmux, Scalekit, ChromaDB, Notion, Gmail, Slack, Mac mini

## [It’s Broken… The Codex vs Claude Code Debate Is Finally Over](../videos/8ImlAQOyVTs.md)
`8ImlAQOyVTs` · AI LABS · 2026-06-02 · q3 · practitioner · review · topics: coding-agents, claude-code, context-engineering, multi-agent

A single-author head-to-head of Claude Code (Opus 4.7) vs Codex CLI (GPT 5.5) across usability, planning, greenfield builds, context, memory and sub-agents; Codex wins on cost and autonomy, Claude on UX, hooks and ecosystem.

- Techniques: Count tokens per session from the CLI's session files; Set a Codex personality to reduce sycophancy; Use Claude Code's expanded thinking to course-correct; Use Codex's attempt flag for best-of-n; Keep AGENTS.md or CLAUDE.md lean; Design sub-agents for isolation or inheritance deliberately
- Tools: Claude Code, Codex CLI, Opus 4.7, GPT 5.5, FastAPI, Flask, Next.js, ShadCN UI, Gemini API, Claude desktop app, Codex web app, Stream Vision Agents

## [This Is The Greatest Shift In Codex CLI And Claude Code](../videos/B44bXmzU60s.md)
`B44bXmzU60s` · AI LABS · 2026-06-02 · q2 · practitioner · review · topics: mcp-and-tools, context-engineering, claude-code

Walkthrough of Mirage, a virtual file system that mounts Gmail, Drive, Slack and similar services as folders so Claude Code can read them with bash instead of MCP tool calls. Partly sponsored, with a hype title.

- Techniques: Mount a SaaS service as a folder; Run the mount as a long-lived process; Start the agent inside the mounted workspace; Chain bash commands across services instead of MCP calls; Read attachments as files; Preserve a session across restarts; Wrap any API as a file system; macOS FUSE prerequisite
- Tools: Mirage (virtual file system for agents, cloned from source), Claude Code, MCP (Model Context Protocol), Gmail MCP, Google Drive MCP, Google Chat, Slack, Notion, Telegram, Figma (mentioned as a possible target), Claude Design (mentioned in passing, unverified), Google Cloud Console

## [This One Command Fixed The Biggest Problem Of AI Coding](../videos/qkc1j3_k8gs.md)
`qkc1j3_k8gs` · AI LABS · 2026-06-02 · q3 · practitioner · tutorial · topics: security-guardrails, coding-agents, token-cost-efficiency, pr-code-review

Walkthrough of DeepSec, a regex-prefilter plus batched Claude Code/Codex agent harness for repo security scans. Strong on code-local bugs, weak on runtime and logic flaws.

- Techniques: Regex prefilter before agent review; Batched parallel agent investigation with merge and coverage check; Project context file for the scanner (info.md); DeepSec command sequence; Resumable batch processing; Per-finding output with ownership and repro; Scoping an unscoped agent review
- Tools: DeepSec (Vercel security harness; `deepsec init`, `scan`, `process`, `report`, `export`), Claude Code, Codex, Claude Agent SDK, Codex Agent SDK, Opus 4.7 (max effort), GPT 5.5 (x-high reasoning), Git (metadata for commit attribution and owner), Markdown and JSON (output formats)

## [I Didn't Know You Could Use Claude Code Like This](../videos/KQDVDtklf34.md)
`KQDVDtklf34` · AI LABS · 2026-06-02 · q2 · intro · tutorial · topics: claude-code, context-engineering, vibe-coding-app-building

Shows non-coding uses of Claude Code (second brain in Obsidian, Remotion video, grounded research pipeline, Canvas design skill, Claude Video watch skill, NotebookLM/Notion ops, role-based finance/teacher/legal setups) mostly as sponsored, shallow tutorials.

- Techniques: CLAUDE.md priority-tiered instructions for a non-code knowledge base; Remotion skill install and plan-first video generation; Step-file research pipeline with verification and cited output; Claude Video skill setup for watching videos; Canvas design skill workflow for posters and infographics; Local Claude Code over NotebookLM CLI and Notion MCP for content systems
- Tools: Claude Code, Claude.md, Obsidian, Remotion, Remotion skill, Anthropic Canvas design skill, Claude Video (watch skill), Groq, SERP API, Google Gemini, NotebookLM CLI, Notion MCP

## [ADLC: Claude Code's New Lifecycle for AI Coding](../videos/aMBQB_IJ0dQ.md)
`aMBQB_IJ0dQ` · AI LABS · 2026-06-02 · q2 · intro · other · topics: agent-architecture, evals, claude-code, context-engineering

Conceptual walkthrough of the agentic development lifecycle (ADLC), a phase-by-phase SDLC analogue for non-deterministic agents with a validation gate and staged rollout. Thin on code and data, with a sponsor segment.

- Techniques: Behavior-first planning mode; Human-agent responsibility model; Ground-truth dataset plus baselines as a validation gate; Single orchestration layer for multiple agents; Context hygiene against context rot; Staged rollout with behavioral alerting; Feedback signals and periodic data refresh
- Tools: Claude Code (planning mode, agent view), Cursor, Google Calendar MCP, Gmail MCP, Notion MCP, RAGAS, DeepEval, Gemini (1M-token context, mentioned), Claude Opus (1M-token context, mentioned), ChatGPT (feedback UI example, mentioned), Softr (sponsor, transcribed as 'Softer')

## [The Greatest AI Coding System I've Ever Used, Forget Codex Vs Claude Code](../videos/q7Am0pV6FjQ.md)
`q7Am0pV6FjQ` · AI LABS · 2026-06-02 · q3 · practitioner · review · topics: claude-code, multi-agent, agent-architecture, context-engineering

Goal Buddy, an open-source plugin for Claude Code and Codex, wraps the native goal command with file-based state, an upfront "oracle" for done, and Scout/Worker/Judge agent roles.

- Techniques: Oracle-first done criteria; Role-separated agents with access limits; File-based run state instead of chat history; Slice contracts; Clarify before looping; Install and start a run
- Tools: Goal Buddy, Claude Code (goal command, resume command), Codex, Ralph Wiggum plugin, Haiku (native goal evaluator)

## [3 Design Levels For a Free Claude Code Boost (People Stop At Level 1)](../videos/5lycYTOYbPM.md)
`5lycYTOYbPM` · AI LABS · 2026-06-02 · q3 · practitioner · tutorial · topics: claude-code, context-engineering, testing-verification, vibe-coding-app-building

Three levels of getting non-generic UI from Claude Code: a structured single-page design prompt, a CLAUDE.md plus design.md system for cross-page consistency, and design tests written before the code, including visual TDD with Visly.

- Techniques: Structured single-page design prompt; CLAUDE.md for project context, design.md for the visual system; Lint design.md against Google's open template; Install an external design-principles audit skill per project; Derive design tests from design.md before writing UI code; Visly local visual TDD loop
- Tools: Claude Code, Claude Opus 4.7 (model named in the video), CLAUDE.md, design.md, OKLCH, Google design.md template (open-sourced), Versalab design-audit skill, Playwright, Visly CLI (transcribed as 'Visly Test' and 'Visley'), Zilliz Cloud (sponsor), Inter (named as banned font), Geist (named as banned font)

## [Claude Code Just Killed Every Shopify Agency Ever](../videos/x2pRavsHdls.md)
`x2pRavsHdls` · AI LABS · 2026-06-02 · q2 · practitioner · tutorial · topics: coding-agents, claude-code, vibe-coding-app-building, context-engineering

A walkthrough for building and syncing a Shopify storefront with Claude Code, using the Shopify CLI, AI toolkit MCP, HTML prototype skill, Gemini image skill and settings.json hooks. Quality is capped by a sponsor segment and a thin, hype-titled setup guide.

- Techniques: Two-phase skill: HTML preview, then apply; Image generation through a CLI skill; Pre-tool-use hook as an approval gate; Shopify project bootstrap; Admin API auth with incremental scopes
- Tools: Shopify Partner account, Shopify CLI (React app template, TypeScript), Shopify AI toolkit (MCP), Shopify plugin (agents and skills), Shopify Admin API, Claude Code, CLAUDE.md, Gemini CLI (image generation), settings.json hooks, Willow Voice (sponsor segment, not a tool used in the setup)

## [Anthropic Just Revealed The Best Claude Code Setup](../videos/lGalJmyI78w.md)
`lGalJmyI78w` · AI LABS · 2026-06-02 · q2 · practitioner · tutorial · topics: claude-code, context-engineering, multi-agent, mcp-and-tools

Practitioner checklist for setting up Claude Code harnesses on large codebases: layered CLAUDE.md, hooks, path-scoped skills, plugins, LSP, MCP, sub-agents, and periodic pruning.

- Techniques: Layered CLAUDE.md; Stop-hook learning loop; Hooks for enforcement; Path-scoped skills; Team plugin distribution; LSP before code; Custom sub-agents with an overridden Explore agent; Per-subdirectory tests and codebase map; Quarterly harness pruning with ignore files
- Tools: Claude Code, Codex, Gemini CLI, superpowers, CLAUDE.md, Claude Code hooks (SessionStart, PreToolUse, Stop, exit-code-2), skill-creator, Claude Code plugins and plugin marketplace, LSP (Language Server Protocol), MCP (Model Context Protocol), Explore sub-agent (built-in, overridable), .gitignore

## [This Is Insane... This Just Ended The Google Stitch VS Claude Design Debate](../videos/PJ9CmTODmVo.md)
`PJ9CmTODmVo` · AI LABS · 2026-06-02 · q2 · intro · review · topics: product-ux, mcp-and-tools, coding-agents, context-engineering

Hands-on head-to-head of Claude Design and Google Stitch across features, limits, design quality, animation, iteration and handoff; each tool wins different categories.

- Techniques: Batch design comments before sending; Import a design system from a URL; Portable design.md design system; Coding agent drives the design tool through MCP; Generate the design system before the screens
- Tools: Claude Design, Claude Opus 4.7, Google Stitch, Gemini 3, Nano Banana, Claude Code, Figma, Google AI Studio, Firebase, GitHub, design.md

## [I Tried Every Skill. These Best Claude Skills Are Bizarre](../videos/qQ5uObNKBOU.md)
`qQ5uObNKBOU` · AI LABS · 2026-05-02 · q2 · intro · review · topics: claude-code, skills-self-improvement, testing-verification, token-cost-efficiency

Walkthrough of nine community Claude Code skills (notifications, adversarial app QA, output compression, git audit, premortem, mutation testing, plan stress-testing, Reddit research, UI color guidance). Mostly README-level tours, with a mid-video sponsor segment.

- Techniques: Per-event voice notifications for parallel Claude sessions; Adversarial browser QA sweep; Terse-output mode to cut response tokens; Git-history audit with a skill; Premortem pass before go-live; Mutation testing for test-suite strength; Stress-test a plan with selectable challenge modes; Fallback chain for scraping Reddit; Grounded design-reference skill for UI
- Tools: P on Ping (skill, transcript name), Claude Code, agent-browser (CLI), Dogfood skill, Caveman plugin, Git, Git Time Travel skill, Premortem skill, Mutation testing skill, The Fool skill, Gemini CLI, tmux

## [This Is The Anthropic Team's Greatest Advice](../videos/O1XLCh-uA_E.md)
`O1XLCh-uA_E` · AI LABS · 2026-05-02 · q2 · practitioner · tutorial · topics: claude-code, context-engineering, multi-agent, agent-architecture

Practical habits for managing Claude Code's context window (compaction, clear, rewind, sub-agents, recaps) to limit context rot and goal drift in long runs; mostly attributed advice with a sponsored segment.

- Techniques: Manual compaction with an explicit instruction; Clear on task switch; Structured state handoff (save, clear, reload); Periodic recap to reinforce goals; Sub-agent isolation for raw-heavy subtasks; Rewind, then re-prompt
- Tools: Claude Code, Claude (Opus 4.5 and later models, 1M context window), CLAUDE.md, Verdant (sponsor)

## [8 Vibe Coded Apps That Generated Millions Overnight](../videos/zNOunnM1jTs.md)
`zNOunnM1jTs` · AI LABS · 2026-05-02 · q2 · intro · other · topics: vibe-coding-app-building, product-ux, coding-agents

Anecdotal roundup of eight solo, vibe-coded apps with self-reported revenue; the useful part is a few habits (small prompts, outsourced dependencies, defining an ICP first), not the numbers.

- Techniques: Incremental, chunked prompting; Minimal correct context; Model fallback chain; Design first, then modular build; Template-guided UI generation; Stack choice for AI tools; Outsource commodity operations; Real-time multiplayer transport; Define the ICP before the build
- Tools: Claude, Claude Code, Cursor, ChatGPT, Grok, Grok 3, Claude Sonnet 3.7, Gemini, GPT, Midjourney, ElevenLabs, Next.js

## [Anthropic Just Fixed The Token Problem](../videos/sncxStbRSwI.md)
`sncxStbRSwI` · AI LABS · 2026-05-02 · q2 · practitioner · review · topics: coding-agents, token-cost-efficiency, multi-agent, claude-code

AI LABS walks through Anthropic's advisor strategy in Claude Code: a Sonnet executor does all the work and calls Opus only when stuck. Three anecdotal tests show it helps simple-to-medium apps but needs nudging.

- Techniques: Executor/advisor model split in Claude Code; Escalate after repeated failure; Consult before a high-blast-radius change; Name the advisor explicitly for non-trivial tasks; Choose the main model by app scope
- Tools: Claude Code, Claude Opus 4.6, Claude Sonnet, Claude Haiku, Playwright MCP, SWE-bench, Junie (JetBrains, sponsor segment)

## [Give Me 13mins, I Will Show You The Right Agent Setup](../videos/ywIhw15za9Y.md)
`ywIhw15za9Y` · AI LABS · 2026-05-02 · q2 · intro · tutorial · topics: claude-code, context-engineering, testing-verification, coding-agents

AI LABS walks through a pre-build setup checklist for Claude Code: product-focused PRD, hand-written CLAUDE.md, agents and skills, spec-first tests, progress and learnings files, and load planning. Generic, sponsored, no benchmarks.

- Techniques: Agent-led PRD interview; Lean hand-written CLAUDE.md that links the PRD; Agent vs skill split; Path-scoped rules linked from CLAUDE.md; Negative-constraints docs file; Progress file plus learnings file; Spec-first test generation; Commit-per-implementation with worktrees; Concurrency-aware load test planning
- Tools: Claude Code, CLAUDE.md, Supabase MCP, shadcn/ui, Playwright, Playwright MCP, skill-creator, GitHub, Git (commits, worktrees), Notion MCP, Trello, OpenClaw (sponsor's skill)

## [Knowing This Gives You An Unfair Advantage With AI Coding](../videos/fMY5Sdj2DMk.md)
`fMY5Sdj2DMk` · AI LABS · 2026-05-02 · q3 · practitioner · tutorial · topics: claude-code, context-engineering, coding-agents, testing-verification

Tutorial for writing CLAUDE.md rules that keep Claude Code on task: think-first, simplicity, surgical edits, verifiable goals, git safety, scoped rule files and a corrections log.

- Techniques: Behavioral rule block for CLAUDE.md (Karpathy-derived); Verification gate before reporting completion; List only non-default tooling; Corrections-to-learnings loop; Destructive-command confirmation rule; Path-scoped rule files and nested CLAUDE.md; CLAUDE.md structure: description first, priority tiers, length cap
- Tools: Claude Code, CLAUDE.md, AGENTS.md, Karpathy skills repo (referenced, not named as a package), Claude Chrome extension, Puppeteer MCP, Git, GitHub CLI (gh), npm, pnpm, Klaus (sponsor, AI agent hosting), OpenClaw (sponsor, open-source AI agent)

## [The Claude Code Skill Boris Cherny Runs on Every Project](../videos/AhXfI1rSUPc.md)
`AhXfI1rSUPc` · AI LABS · 2026-05-02 · q2 · practitioner · review · topics: claude-code, skills-self-improvement, multi-agent, testing-verification

A walkthrough of skills, plugins and slash commands the Claude Code team reportedly uses, including batch worktree fan-out, a verify skill and an end-of-session tech debt skill. Several are internal and unverified, and a sponsor segment is included.

- Techniques: Batch fan-out with worktrees; Project-specific verify skill; Skillify-style session capture; End-of-session tech-debt pass; Inner-loop slash commands; Issue dedupe with a confidence threshold; Security scan, then fix
- Tools: Claude Code, Claude Code batch command, git worktrees, frontend-design plugin, Code Simplifier plugin, Simplify (built-in), Claude Code security scan (built-in), commit command plugin, Remotion skill, skill creator skill, Skillify (internal), verify skill (internal)

## [How To Never Hit Your Claude Code Limit Again](../videos/YsdQE6juGXY.md)
`YsdQE6juGXY` · AI LABS · 2026-05-02 · q3 · practitioner · tutorial · topics: token-cost-efficiency, claude-code, context-engineering

Practitioner tips for stretching Claude Code's usage limits: explains the 5-hour window, then covers context hygiene, lean CLAUDE.md, model and effort routing, hooks, and settings toggles. Partly sponsored; leaked-source claims are unverified.

- Techniques: Clear or compact between tasks; Side questions in a separate context via the by-the-way command; Rewind to before a misaligned turn instead of re-prompting; Lean CLAUDE.md with linked, progressively loaded docs; Path-scoped rules files; Skills with bundled scripts for repetitive workflows; Session-only instructions via the append-system-prompt flag; Task-based model and effort routing; Disable unused MCP servers per project; Hook that keeps only failing tests in context; Settings toggles for token use
- Tools: Claude Code, Claude (Pro and Max plans), Claude Desktop, Cowork, Claude Opus, Claude Sonnet, Claude Haiku, Claude.md (CLAUDE.md), MCP servers, Twin (sponsor), Zapier (named in sponsor segment), n8n (named in sponsor segment)

## [We Already Have Something Better Than Claude Design](../videos/GbuwosWEvHo.md)
`GbuwosWEvHo` · AI LABS · 2026-05-02 · q2 · intro · review · topics: claude-code, coding-agents, product-ux, context-engineering

AI LABS argues Claude Design is mostly hype: Claude Code with Opus 4.7 can match it, and it adds Git, parallel worktrees, and skills. The evidence is one anecdotal comparison plus sponsor-heavy, unverified claims.

- Techniques: Clarifying-question skill to replace Claude Design's intake flow; Hero video background plus animation libraries; Component libraries and MCP for UI consistency; Parallel design variants in git worktrees; Prototype as HTML mock-ups
- Tools: Claude Code, Claude Design, Claude Opus 4.7, Claude Opus 4.6, GSAP, Lenis, ShadCN, ShadCN MCP server, Aceternity UI, Hero UI, scrollytelling skill, Figma

## [Your AI Output Sucks Because You’re Not Doing This](../videos/cop_G65D7PA.md)
`cop_G65D7PA` · AI LABS · 2026-04-02 · q2 · intro · tutorial · topics: context-engineering, claude-code, multi-agent, token-cost-efficiency

AI LABS' pre-setup tips for Cowork: a per-folder manifest.md with tiered sources, voice and working-style files, global instructions that demand plans and questions, end-state prompts, batching and guardrails.

- Techniques: Per-folder manifest.md with tiered sources; Identity, voice and working-style context files; Global instructions as a default operating contract; State the end state and the edge-case rule; Batch by shared context, keep unrelated work apart; Scheduled report from meeting notes via the schedule skill; Build a plugin with the plugin-creation skill; Guardrails for agent file access
- Tools: Cowork, Claude Code (clawed code in transcript), Claude desktop app, CLAUDE.md (global and per-folder instructions), manifest.md (the presenter's convention), schedule skill, plugin-creation skill, OpenClaud (auto-caption; used for research, tool-release tracking and a Discord report; spelling uncertain), Discord, Gmail connector, Google Drive connector, cron jobs

## [How to Use Google Stitch to Make Sites 10X More Beautiful](../videos/b0lwCDNOFUY.md)
`b0lwCDNOFUY` · AI LABS · 2026-04-02 · q2 · practitioner · tutorial · topics: vibe-coding-app-building, coding-agents, context-engineering, skills-self-improvement

Tutorial on pairing Google Stitch with Claude Code: design.md design systems, screenshot-based redesign, Stitch skills and MCP, then React and shadcn conversion. Includes sponsor segments.

- Techniques: design.md-first design system; Extract design.md from an existing Stitch project; Screenshot as style reference (Redesign); Import style from a URL; Sketch plus theme to correct drift; Annotate-and-apply targeted edits; CLAUDE.md pipeline for Stitch skills; Convert a Stitch project to shadcn/ui
- Tools: Google Stitch, Claude Code, design.md, Stitch MCP, Stitch Enhance Prompt skill, Stitch Loop skill, Stitch React component skill, Stitch design.md skill, Google Stitch skills repo, Chrome DevTools, NanoBanana (image generation), GoFullPage (Chrome extension)

## [12 Hidden Settings To Enable In Your Claude Code Setup](../videos/pDoBe4qbFPE.md)
`pDoBe4qbFPE` · AI LABS · 2026-04-02 · q2 · practitioner · tutorial · topics: claude-code, context-engineering, multi-agent

Tour of under-documented Claude Code settings: session retention, output and read caps, sub-agent flags, auto-compact at 75%, commit attribution, telemetry, and exit-code-2 hooks. Includes a sponsored segment.

- Techniques: Extend session retention; Path-scoped rules; Raise the bash output cap; Run a session as a sub-agent; Raise the file read cap and enforce full reads; Lower the auto-compact threshold; Remove commit co-author lines; Opt out of telemetry without losing updates; Prompt stash with Ctrl+S; Exit-code-2 hook to block and steer; Loop-until-done with exit-code hooks (Ralph-style); Claude CTX profiles
- Tools: Claude Code, Claude CTX (open-source profile switcher), Opus 4.6 (cited as the 1M-token-context model), uv (transcribed as 'uvicorn'; likely the pip replacement in the hook example), Statsig (analytics sink, named by speaker), Sentry (error reporting sink, named by speaker), Make.com (sponsor), Ralph loops (named concept, not a tool)

## [OpenClaw Agents Just Got Better With This](../videos/JC53AcoFh-Q.md)
`JC53AcoFh-Q` · AI LABS · 2026-04-02 · q2 · intro · review · topics: security-guardrails, multi-agent, memory, skills-self-improvement

A tool roundup for hardening and extending OpenClaw agents: a security skill suite, a deterministic multi-agent workflow runner, a hybrid memory plugin, a network-API browser skill, Cloudflare hosting, a dashboard, and a curated skill list.

- Techniques: Installing a skill from git when the registry is rate-limited; Self-verifying skills: checksum check with re-download on mismatch; Scheduled security heartbeat over installed skills; Deterministic multi-agent workflow with verifier and fresh contexts; Re-ranked hybrid memory as an agent memory plugin; Replaying site APIs with cookies instead of driving a browser visually; Filtering a large skill registry before installing
- Tools: OpenClaw, ClawSec, Prompt Security, Heartbeat skill, Soul Guardian, OpenClaw Watchdog, Antfarm, Ralph Loop (creator's earlier project, per speaker), AI Dev Task (creator's earlier project, per speaker), ClawHub (skill registry), Awesome OpenClaw Skills (curated list), MemoryLanceDB Pro

## [How to use Claude Code and Gemini Cli Together](../videos/XdtBAm2pM-0.md)
`XdtBAm2pM-0` · AI LABS · 2026-04-02 · q3 · practitioner · tutorial · topics: multi-agent, coding-agents, claude-code, context-engineering

Walkthrough of Agent Chatter, a shared chat layer where Claude Code, Gemini CLI and Codex agents run in tmux and coordinate through channels, with planning, peer review and loop-guard setup.

- Techniques: Shared multi-model chat via per-agent tmux sessions; Per-agent settings.json permissions instead of skip-permissions; Shared agents.md as the single instruction source; Named personas per agent; Loop guard and continue gate; Planner-first with PRD and spec templates; Three-phase presenter/challenger/synthesizer review; Planner as orchestrator with an ask-don't-assume rule; Git worktrees per agent (suggested, not tested); Initialize the app framework before starting agents
- Tools: Agent Chatter, Claude Code, Opus 4.6, Gemini CLI, Codex, Kimi, Qwen, GLM, tmux, Next.js, MCP, agents.md

## [GSD Is the Missing Piece For Claude Code](../videos/uEit1oOJK0w.md)
`uEit1oOJK0w` · AI LABS · 2026-04-02 · q2 · practitioner · review · topics: coding-agents, context-engineering, multi-agent, testing-verification

AI LABS walks through GSD (Get Shit Done), a planning-and-execution framework for Claude Code, and compares it with BMAD and Superpowers. Main takeaway: choose the framework by how fixed your requirements are.

- Techniques: Choose the framework by requirement certainty; Per-project install with project scope; Initialise GSD on existing vs blank codebases; Keep the planning anchor short; Per-phase discuss, then concise context file; Ground phase research in docs with Context7; Adversarial plan verification and waves; Phase verification gates
- Tools: GSD (Get Shit Done), BMAD method, Superpowers, Claude Code, Claude Opus 4.6, Claude Sonnet, Next.js, Playwright, Context7 MCP, GenSpark (sponsor segment), Speakly (sponsor segment)

## [Anthropic Just Killed All Your Agent Harnesses](../videos/nBH07G-zayk.md)
`nBH07G-zayk` · AI LABS · 2026-04-02 · q2 · practitioner · review · topics: agent-architecture, testing-verification, context-engineering, claude-code

Walkthrough of Anthropic's reported harness ablations: with Opus 4.5/4.6, keep a planner, a generator and a separate graded evaluator, and drop micro-level plans, context resets and sprint contracts for strong models.

- Techniques: Product-level planner agent; Separate evaluator with an adversarial stance; Weighted rubric with a score per criterion; Generator and evaluator as agent-team members; Sprint contract for weaker models; Bolt Anthropic's evaluator onto GSD
- Tools: Claude Code, Claude Opus 4.5, Claude Opus 4.6, Claude Sonnet, Claude Haiku, Anthropic agent harness, BMAD, GSD, SpecKit, Superpowers, Ralph Loop, Playwright MCP

## [Anthropic's Head of Design Just Killed The Old Process](../videos/X4vAlWtsJD4.md)
`X4vAlWtsJD4` · AI LABS · 2026-04-02 · q2 · practitioner · tutorial · topics: vibe-coding-app-building, context-engineering, product-ux, coding-agents

A walkthrough of how an AI Labs team now builds app prototypes: actors and constraints first, PRD and architecture files, a Next.js and Supabase prototype with mock data, then a backend added only when needed.

- Techniques: Actor-first requirements; Constraints instead of tool instructions; PRD interview prompt; Layer prompt to architecture.md; Scaffold Next.js with Supabase, then apply a frontend-design skill; Mock-data prototype for sign-off; Task lists from architecture.md; API spec from frontend code plus PRD plus architecture; Supabase MCP for schema and migrations; Front end talks directly to the database; backend only when needed; Delegate the backend layer to a cloud agent
- Tools: Figma, Next.js, Supabase, Supabase MCP, Python, Warp Oz (sponsored cloud-agent orchestration), Stripe, Google authentication, Anthropic general-purpose frontend-design skill

## [I Didn't Know This Was Possible Until Now](../videos/LqN_ItMqovA.md)
`LqN_ItMqovA` · AI LABS · 2026-04-02 · q3 · practitioner · review · topics: mcp-and-tools, token-cost-efficiency, claude-code, context-engineering

A team's walkthrough of MCP context bloat and a runtime MCP-to-CLI converter (MCP2CLI), plus CLAUDE.md and skills rules that keep large tool outputs out of the context window.

- Techniques: Run MCP2CLI without installing it; Give the agent the MCP access tokens through environment or file references; Verify MCP connections by asking the agent to count the tools; CLAUDE.md rule to consult docs before coding; Move per-MCP guidance from CLAUDE.md into one skill per MCP; Ask for TOON output for verbose documentation MCPs; Redirect large MCP output to a file and grep it; Use Claude's browser extension for stateful browser testing

## [10 Crazy Claude Code Tips That Give You An Unfair Advantage](../videos/TmsH-RIHvas.md)
`TmsH-RIHvas` · AI LABS · 2026-03-02 · q3 · practitioner · tutorial · topics: claude-code, context-engineering, testing-verification, multi-agent

AI LABS walks through ten Claude Code practices: session-insight reviews, Claude-written planning docs, exit-code-2 hooks, worktree-based parallel agents, adversarial fact-checking, and browser-based self-verification.

- Techniques: Session insights review into CLAUDE.md; Claude-authored planning docs as context; Context7 MCP for current library docs; Exit-code-2 PreToolUse guard for protected paths; MCP CLI mode to keep tool schemas out of context; One git worktree per parallel agent; Strict TypeScript and user stories before implementation; Adversarial researcher and fact-checker agents; Agent Browser for self-verification, with CLAUDE.md fallback order; Failure-prediction review pass
- Tools: Claude Code, CLAUDE.md, Claude Code hooks (PreToolUse), MCPCLI (experimental MCP CLI mode), Context7 MCP, git worktrees, TypeScript, Claude in Chrome extension, Puppeteer MCP, Agent Browser (Vercel), Kimi K2.5 (named as comparison in a research example), Opus 4.6 (named as subject of a research example)

## [The Correct Way to Use Claude Code Teams](../videos/MSyWjPDrHJw.md)
`MSyWjPDrHJw` · AI LABS · 2026-03-02 · q3 · practitioner · tutorial · topics: claude-code, multi-agent, coding-agents, token-cost-efficiency

AI LABS walks through Claude Code agent teams, an experimental upgrade over sub-agents where teammates message each other directly, and shows three uses plus practical rules for keeping them on track.

- Techniques: Enable agent teams behind the experimental flag; Reviewer and fixer pair for parallel code review; Multi-perspective bug hunt; Staged build with a blocking foundation agent; Per-assignment task documents to bound scope; Lead supervision rules
- Tools: Claude Code, Claude Code agent teams (experimental), Claude Code sub-agents, Claude Opus 4.6

## [This Changed The Way I Design With AI](../videos/sdxJEd7nqiQ.md)
`sdxJEd7nqiQ` · AI LABS · 2026-03-02 · q3 · practitioner · review · topics: claude-code, coding-agents, product-ux, skills-self-improvement

Pencil.dev design-to-code workflow with Claude Code: a file-watcher syncs .pen edits to code, subagents build pages, and a UX-audit skill raised the site grade from C to B.

- Techniques: Design file as a repo artifact; Save-triggered sync watcher; Pre-approve permissions for unattended claude runs; One subagent per page with shared docs; XML-tagged task prompts; Layer Lenis over GSAP for scroll; UX Audit skill with a scored re-run loop
- Tools: Pencil.dev, Claude Code, Claude CLI, Claude Opus 4.6, Codex, Figma MCP, Stitch, Bolt, npm, Git, GSAP, Lenis

## [Anthropic Released Another Official Process](../videos/aEqKWI-0N0c.md)
`aEqKWI-0N0c` · AI LABS · 2026-03-02 · q2 · practitioner · tutorial · topics: skills-self-improvement, context-engineering, claude-code, testing-verification

A team rebuilds a Nano Banana image skill for Claude Code, then shows the skill-design fixes that mattered: trigger-rich descriptions, progressive disclosure, scripts, validation gates and error tables.

- Techniques: Trigger-rich skill descriptions with negative triggers; Three-level progressive disclosure layout; Move constraints out of prompts into post-processing; CLI scripts with modes and a preview mode; Two-stage validation gates with regenerate-on-fail; Error table with error, cause, and fix; Split domain knowledge into reference packets; Iterate against real outputs and refresh the skill-creator
- Tools: Claude Code, Google Antigravity, Nano Banana Pro, skill-creator (Claude Code official skill), Next.js, Cream (sponsor, merchant of record), Cursor, Windsurf

## [How To Use NotebookLM - 7 Crazy Ways](../videos/eFCHwtufjJc.md)
`eFCHwtufjJc` · AI LABS · 2026-03-02 · q3 · practitioner · tutorial · topics: context-engineering, rag-retrieval, claude-code, coding-agents

AI LABS shows seven ways to wire Google's NotebookLM CLI into Claude Code as a grounded knowledge base: a second brain, research store, codebase onboarding, debugging KB, agent-readable visualizations, and a security handbook.

- Techniques: Install and verify the NotebookLM CLI; Notebook as project second brain via CLAUDE.md; Research offload to a notebook; Codebase onboarding via Repomix; Debugging knowledge base in place of web search; Export mind maps and tables as agent-readable artifacts; Security handbook notebook for grounded reviews; Shared notebook as knowledge base for people and other agents
- Tools: NotebookLM (Google), NotebookLM CLI (version not stated), Claude Code, CLAUDE.md, Repomix (CLI, installed via npm), GitHub CLI (gh), Gemini (answers NotebookLM queries, per the speaker), Cursor, Gemini CLI, OWASP cheat sheets, Make (sponsor, pre-built market research agent)

## [This Just Fixed 90% of AI Coding Errors](../videos/romGzY0Xu0s.md)
`romGzY0Xu0s` · AI LABS · 2026-03-02 · q3 · practitioner · review · topics: coding-agents, testing-verification, multi-agent, skills-self-improvement

AI LABS team tests the Superpowers Claude Code plugin on a Trello-style app: enforced brainstorm, plan, subagent, TDD and review gates work, but they burn context fast and are best used selectively.

- Techniques: Install a workflow plugin from a marketplace in Claude Code; Brainstorm-gated kickoff prompt; Subagent-driven implementation with worktrees and review gates; Anti-test-edit TDD cue; Four-phase systematic debugging prompt; Compact before the next feature; Selective process use; Re-invoke skills after context loss
- Tools: Claude Code, Superpowers (Claude Code plugin), git, git worktrees, BMAD, OpenSpec, Trello (the example app being cloned)

## [Google Just Solved The Greatest Limitation of AI Agents](../videos/uprZUcv0FSc.md)
`uprZUcv0FSc` · AI LABS · 2026-03-02 · q3 · practitioner · review · topics: mcp-and-tools, voice-multimodal, coding-agents

Walkthrough of WebMCP, a proposed browser standard where websites register callable tools for agents instead of agents guessing from screenshots or DOM. Covers declarative and imperative APIs, per-page tool loading, and current limits.

- Techniques: Declarative WebMCP tool on an HTML form; Imperative WebMCP tool registration per route; Scope tool lists to the page (contextual loading); Write tool descriptions for a cold reader; Inspect tool schemas with the Model Context Tool Inspector extension; Test with the Gemini-backed demo paths
- Tools: WebMCP, Chrome Canary, Chrome 146, Chrome Labs WebMCP repo, Model Context Tool Inspector extension, Claude Code, Gemini (built into Chrome; Gemini API key option in the demo), Next.js, React, Zen browser, Community WebMCP bridge (unnamed, not identified), Brilliant (sponsor)

## [You Need To Know This Before Installing OpenClaw](../videos/M3P0hQMQtq0.md)
`M3P0hQMQtq0` · AI LABS · 2026-03-02 · q3 · practitioner · review · topics: security-guardrails, token-cost-efficiency, sandboxing-execution, skills-self-improvement

AI LABS tests the self-hosted agent OpenClaw and finds it costly (token-heavy context, heartbeats), slow as context grows, and risky (plain-text credentials, malicious community skills, prompt injection); it closes with mitigation advice.

- Techniques: Hard budget and alerts on the model API key; Reduce idle token burn; Vet community skills before install; Sandbox the agent; Least-privilege channel tokens; Prefer providers with built-in guardrails, with caution
- Tools: OpenClaw, Claude (former Claudebot name), OpenAI API, Anthropic models, OpenRouter, Ollama, Docker, Cisco open-source skill scanner, Discord, WhatsApp

## [I Didn't Expect This From OpenAI's IDE](../videos/sC4JpJlD3aQ.md)
`sC4JpJlD3aQ` · AI LABS · 2026-03-02 · q3 · intro · tutorial · topics: coding-agents, multi-agent, vibe-coding-app-building, skills-self-improvement

A 7-minute build log: turning a car photo into a 3D hero section for a Next.js landing page with Tripo 3D, OpenAI's Codex app, GSAP and Aceternity UI, with parallel Codex subagents in git worktrees.

- Techniques: Pre-clean the image for image-to-3D; GLB asset in a Next.js public folder; Generate a project skill with the agent's skill creator; Work around agent install timeouts; Parallel subagents in separate git worktrees; Scope the agent with explicit do-not-touch constraints; Fix visual drift with screenshots and named variants
- Tools: Codex app (OpenAI), Tripo 3D, Canva background remover, Next.js, GSAP, Aceternity UI, React Three Fiber, post-processing package for React Three Fiber (named 'Post Processing' in the transcript), npm, GLB (file format), Antigravity (agent manager, compared in passing), Claude Code (mentioned as the previous agent used)

## [OpenClaw Use Cases That Are Actually Insane](../videos/hp7n45JqvIw.md)
`hp7n45JqvIw` · AI LABS · 2026-03-02 · q2 · practitioner · review · topics: agent-architecture, coding-agents, software-factory

AI LABS walks through weeks of running OpenClaw on a Mac Mini for developer ops: dependency upgrades, cost and uptime monitoring, SEO checks, PRD-to-deploy builds, cold-email drafts and Claude Code delegation.

- Techniques: Guideline-driven dependency upgrade cron; Scheduled research briefing; Cost watchdog skill; Hosted-app heartbeat monitor; SEO heartbeat; PRD-to-deployed-app run; Delegate to Claude Code with subtasks and per-step commits; Draft-only cold outreach via cron; Email triage heartbeat
- Tools: OpenClaw, Claude Code, Codex, Gemini 3, Nano Banana Pro (Google image-generation skill, bundled with OpenClaw), Nano Banana (earlier skill referenced), GOG CLI, Google Workspace CLI, Google Cloud console, AWS CloudWatch, Vercel, GitHub

## [Anthropic Shows What Most Developers Are Missing](../videos/LC7kGTDoWRY.md)
`LC7kGTDoWRY` · AI LABS · 2026-02-02 · q2 · intro · news · topics: coding-agents, multi-agent, testing-verification, enterprise-adoption

AI LABS argues that engineering is shifting from writing code to orchestrating agents, reviewing exceptions, and stating intent clearly, with a short sponsored segment and little measured evidence.

- Techniques: CLAUDE.md verification loop for long autonomous runs; Commit each verified unit, with decisions in the message; Split work into small independent units and run agents in parallel; Custom specialist subagents with chosen models and instructions; Plan mode with agent questions before building; Agent first-pass review with human review of exceptions; Layered security agents plus an external scanner
- Tools: Claude Code, CLAUDE.md, Claude Chrome extension, Puppeteer MCP, git, CodeRabbit, Cowork (Anthropic), Claude Opus 4.5, GPT-5.2, Golang, COBOL, Fortran

## [The Last Claude Code Tutorial You'll Ever Need](../videos/EHDzlot7LKU.md)
`EHDzlot7LKU` · AI LABS · 2026-02-02 · q3 · intro · tutorial · topics: context-engineering, claude-code, multi-agent, skills-self-improvement

Principles for building your own agent workflow in Claude Code: progressive disclosure, external note files, context-budget hygiene, subagents, git and slash commands.

- Techniques: Progressive disclosure via skills; External note files for long tasks; Manual context hygiene; Delegating research to subagents; Format selection for context files; Git as memory and parallelism; Slash commands for repeated procedures
- Tools: Claude Code, Claude (Anthropic models, 200k context), Gemini (1M context), Sonnet 4.5, BMAD, SpecKit, agent.md / AGENTS.md, CLAUDE.md, Jira MCP, Figma MCP, Git, git worktrees

## [Is Kimi K2.5 Actually The Best Open Source Model?](../videos/D4ICNmfXmwI.md)
`D4ICNmfXmwI` · AI LABS · 2026-02-02 · q2 · practitioner · review · topics: models-research, coding-agents, multi-agent

AI LABS hands-on test of Moonshot's Kimi K2.5: open-weight, not open-source; agent-swarm migration was not faster on a large codebase, while a Notion-clone-from-video test worked after one follow-up prompt.

- Techniques: Parallel per-group migration with a sub-agent per page group; Post-migration cleanup pass; Video-as-input UI cloning; Iterate on broken features with a follow-up prompt
- Tools: Kimi K2.5 (Moonshot AI, open-weight, 1T total / 32B active MoE), Kimi Code CLI (agent CLI released with Kimi K2.5), ShadCN UI, Material UI, Claude Opus 4.5 (used as a comparison model), Claude Code (compared for sub-agent behavior and pricing), Notion (cloned from screen recording), DeepSeek (architecture comparison only), Opera Neon (sponsor, agentic browser)

## [This Exceeded Every Expectation I Had](../videos/iC9loBJjduM.md)
`iC9loBJjduM` · AI LABS · 2026-02-02 · q3 · practitioner · tutorial · topics: context-engineering, claude-code, mcp-and-tools, token-cost-efficiency

Applies Cursor's dynamic context discovery ideas to Claude Code via CLAUDE.md: offload big tool output and chat history to files, lazy-load MCP tools, and grep logs instead of re-running them.

- Techniques: Offload large MCP responses to files; Per-session history file as compaction insurance; Timestamped terminal logs with grep-and-tail retrieval; Progressive-disclosure skills; Lazy MCP tool loading with the experimental MCP CLI flag
- Tools: Claude Code, Cursor, Antigravity, Codex, Gemini CLI, Claude Chrome extension, CLAUDE.md, MCP (Model Context Protocol), MCP CLI (experimental Claude Code flag), Claude advanced tool search (developer platform), Cursor semantic search, grep

## [Claude Code's Creator Does This Before Every Single Project](../videos/B-UXpneKw6M.md)
`B-UXpneKw6M` · AI LABS · 2026-02-02 · q2 · practitioner · tutorial · topics: claude-code, testing-verification, context-engineering, multi-agent

Boris, who created Claude Code at Anthropic, shares a short workflow: give the agent a way to verify its work, keep CLAUDE.md lean and team-maintained, use plan mode and scoped permissions, and run parallel or background sessions.

- Techniques: Verification line in CLAUDE.md; Tests-first or tests alongside each feature; Browser or screenshot verification for UI; Team-maintained CLAUDE.md; Mistakes from PR review go into CLAUDE.md; Project-scoped allow/ask/deny permissions; Plan mode before execution; Parallel sessions with numbered tabs; Cloud background agents with teleport; Background verification tasks; Stop hook for verification; Loop plugin for autonomous runs; Per-language linters and formatters; Committed slash commands; Narrow subagents
- Tools: Claude Code, CLAUDE.md, Claude Code GitHub action, Claude Code on the web (cloud sessions), Claude browser extension, Opus 4.5, Sonnet, Haiku, Ralph Wiggum plugin, MCP servers (Slack, Notion), BigQuery CLI, Sentry CLI

## [This is How I Design With Stitch Now](../videos/VNx9Gy5pHZI.md)
`VNx9Gy5pHZI` · AI LABS · 2026-02-02 · q3 · practitioner · tutorial · topics: coding-agents, mcp-and-tools, testing-verification, vibe-coding-app-building

A Stitch-as-MCP design workflow in Claude Code: plan first, generate one long landing page, pull its HTML, then test with Vercel's snapshot-based Agent Browser. The Stitch MCP wrapper is unofficial.

- Techniques: Stitch MCP for agent-driven design generation; Plan-mode UI guide before design; One long page prompt instead of per-section prompts; Pulling Stitch screen code into a project; Follow-up refactor after code dump; CLAUDE.md rules that mandate a test tool; Snapshot-driven UI testing with Vercel Agent Browser
- Tools: Google Stitch, Stitch MCP (community, unofficial), Google Cloud SDK / gcloud CLI, Homebrew (brew), Claude Code (plan mode, CLAUDE.md), Gemini 3 Flash, Next.js, curl, Vercel Agent Browser, Claude's Chrome extension (compared), Playwright (compared), Puppeteer (compared)

## [ShadCN is Way too Powerful Now](../videos/MFJ0mH72_qI.md)
`MFJ0mH72_qI` · AI LABS · 2026-02-02 · q2 · practitioner · tutorial · topics: claude-code, testing-verification, agent-architecture, context-engineering

Ralph stop-hook loop plus TDD and screenshot checks for ShadCN UI work; a separate verification iteration before the completion promise fixed premature "done" claims.

- Techniques: Stop-hook completion-promise loop; Test-first workflow inside the loop; Screenshot verification protocol; Two-phase completion gate
- Tools: ShadCN (UI component library), Claude Code, Ralph plugin (Anthropic, Ralph loop), Claude Code stop hooks, Playwright, Playwright MCP (named only to say it was not used), Notion (reference point for the board view), Automata (sponsor)

## [I Couldn't Believe Claude Tasks Could Do This](../videos/li8bIt-mjbA.md)
`li8bIt-mjbA` · AI LABS · 2026-02-02 · q2 · intro · review · topics: claude-code, multi-agent, agent-architecture, coding-agents

Walkthrough of Claude Code's new built-in task system: a coordinator splits work into a dependency graph, runs independent sub-agents in parallel, and persists tasks outside the context window so they survive /clear and restarts.

- Techniques: Explicit dependency breakdown prompt; Fan out independent sections of a spec; Named long-running sessions; Inspect task state on disk; Batch folder documentation with Cowork; Research-then-implement handoff
- Tools: Claude Code, Cowork, Claude Chat, Opus 4.5, Haiku, Sonnet, CLAUDE.md, Notion, Lovart (sponsor segment, not evaluated)

## [Vercel Just Revealed Claude Code's Greatest Advantage](../videos/gZr5VmsXmXQ.md)
`gZr5VmsXmXQ` · AI LABS · 2026-02-02 · q3 · practitioner · talk · topics: rag-retrieval, context-engineering, sandboxing-execution

Argues that LLM agents can retrieve context with plain bash (ls, find, grep, cat) instead of a vector DB, sending only a small slice to the model; shows a Gemini 2.5 Flash policy-docs demo and states when RAG still wins.

- Techniques: Bash-tool retrieval over a document directory; Scoped execution for agent shell access; Markdown-defined multi-phase evaluation pipeline; Route retrieval by data shape and query type
- Tools: Vercel bash tool (open-sourced; name not stated), Vercel sandbox (full VM isolation), Claude Code, CLAUDE.md, Gemini 2.5 Flash, Chroma (vector DB the speaker would normally have used), grep, ls, find, cat

## [Why Google Antigravity Suddenly Makes Sense](../videos/e4giCKHIJy8.md)
`e4giCKHIJy8` · AI LABS · 2026-02-02 · q2 · practitioner · review · topics: coding-agents, context-engineering, testing-verification, skills-self-improvement

A walkthrough of Google Antigravity as a coding agent, using Cursor's published harness principles: plan-first with commented revisions, on-demand context, TDD, Git as knowledge base, and skills-based debug mode.

- Techniques: Comment-driven plan revision; On-demand context instead of manual file tagging; Conversation reset policy; Project rules as markdown in .agent/rules; Skill folders following Anthropic's open standard; TDD with a committed test baseline; Screenshot as design and bug input; Git workflows as reusable commands; Agent-run code review with severity sorting; Parallel agents on separate branches; Skill-based debug mode; Watch the agent and redirect early
- Tools: Google Antigravity (AI code editor with planning mode, rules, skills and workflows), Gemini 3 (model used in Antigravity), Claude Code, Claude Opus, Cursor, Cursor's agent harness article (referenced, not named as a product), Anthropic's long-running agent harness (referenced), Anthropic's open Agent Skills standard (SKILL.md), Git, GitHub (built-in PR code review), CodeRabbit, Sentry

## [The Greatest Problem With AI Coding Is Solved](../videos/3FZIdRZsUMM.md)
`3FZIdRZsUMM` · AI LABS · 2026-02-02 · q2 · intro · talk · topics: context-engineering, testing-verification, coding-agents, claude-code

AI LABS argues the implementation middle of software work is being replaced by agents, so developers should focus on planning, context setup, and reviewing or testing agent output.

- Techniques: Refine the plan, then run one-shot implementation; Split spec into per-concern documents; Test-first with a context reset and locked tests; Black-box testing from user stories with a browser agent; White-box review with an XML test plan and a slash command; Layered project structure for agents
- Tools: Linear, Dart AI, VS Code, Claude Code, Claude Chrome extension, Cursor, Slack, CLAUDE.md, skill.md, MCP, XML

## [I Wasn't Ready For What This Does](../videos/XP6TJRbOdGo.md)
`XP6TJRbOdGo` · AI LABS · 2026-02-02 · q2 · intro · tutorial · topics: vibe-coding-app-building, voice-multimodal, context-engineering

A step-by-step landing-page workflow: Google Whisk keyframes, Google Flow frame-to-video, MP4-to-animated-WebP for a scroll-mapped hero, then Claude adds HeroUI, Motion.dev and 21st.dev components in Next.js.

- Techniques: Two-keyframe hero animation; MP4 to animated WebP for scroll mapping; XML-sectioned prompt for an AI coding agent; Install individual UI components instead of the whole library; Copy-paste component prompts from 21st.dev
- Tools: Google Whisk, Nano Banana (image generation, via Whisk), Gemini 3 (prompt expansion layer in Whisk; planning in Flow), Google MixBoard, Google Flow, VO 3.1 (video model; 20 credits per video), Claude (coding agent), Next.js, Tailwind CSS, HeroUI (library, formerly Hero UI), framer-motion, Motion.dev (motion library)

## [Docker Just Fixed 90% of AI Coding By Releasing This](../videos/ZOutBmRai2M.md)
`ZOutBmRai2M` · AI LABS · 2026-01-02 · q2 · practitioner · review · topics: mcp-and-tools, token-cost-efficiency, sandboxing-execution

Docker's MCP toolkit walkthrough: one gateway in front of a vetted catalog, on-demand tool loading, and "code mode" where the agent chains MCP calls in a sandbox, keeping bulky results out of context.

- Techniques: Single MCP gateway front door; On-demand tool discovery with find/add/remove; Code mode: chain MCP calls in a sandboxed script; Write bulky tool output to a file and return only the fields needed; Volume-backed state between tool calls; Merge repeated tool calls into one generated tool
- Tools: Docker MCP Toolkit, Docker MCP Catalog, Docker MCP Gateway, Docker MCP find/add/remove tools, mcp exec tool, Docker containers and volumes (sandbox), Claude Code, GitHub MCP server, Notion MCP server, Cloudflare code mode (referenced), Anthropic MCP token post (referenced)

## [The Best MCP Servers of 2025](../videos/kRxdsv1ZY1E.md)
`kRxdsv1ZY1E` · AI LABS · 2026-01-02 · q2 · intro · review · topics: mcp-and-tools, context-engineering, coding-agents

AI LABS roundup of six MCP servers for AI coding agents: Context7, Docker MCP, ShadCN, Google's managed servers, Notion and Supabase. Anecdotal, partly sponsored, and thin on measurements.

- Tools: Model Context Protocol (MCP), Context7, Ref, Docker MCP (MCP Find, MCP Add), Cloudflare code mode (concept), ShadCN registry MCP, shadcn components.json, Aceternity UI, Magic UI, Gemini 3, Google Maps MCP, BigQuery MCP

## [Google's Biggest Fail of the year](../videos/PB9sJnZyQ7g.md)
`PB9sJnZyQ7g` · AI LABS · 2026-01-02 · q2 · intro · review · topics: context-engineering, coding-agents, testing-verification

A solo review of Google's Conductor, a Gemini CLI extension for spec-driven "track" workflows. The host finds the file layout sound but the command instructions weak, with destructive and falsely-completed steps.

- Techniques: Per-track spec + plan with a status index; Commit per task with git notes and git-aware revert; Default test gate on every task; Review each generated doc before auto-generation; Scope context updates to what changed; Verify completion against real state
- Tools: Conductor (Google Gemini CLI extension), Gemini CLI, Gemini (model), Claude Code plugins (mentioned as comparison), BMAD (recommended alternative), Supabase, npm, pnpm, git, git notes, GitHub

## [Inngest's New Tool Is Insane For AI Coding](../videos/8vvTHnta59A.md)
`8vvTHnta59A` · AI LABS · 2026-01-02 · q2 · intro · review · topics: mcp-and-tools, coding-agents, testing-verification

Short demo of Inngest's MCP server for its local dev server, showing a coding agent sending test events, polling run status and checking its own workflow runs in Claude Code.

- Techniques: Wire an event-driven dev server into Claude Code via MCP; Agent-driven verify loop: send event, poll run, check result; Switch model provider through a gateway in one prompt
- Tools: Inngest, Inngest dev server, Inngest MCP server, Claude Code, Cursor, Next.js, OpenAI API, Vercel AI Gateway (auto-captioned as 'Versal'), Puppeteer MCP, CLAUDE.md, .mcp.json

## [Anthropic Released A New Way To "Vibe Code"](../videos/XWp4k9K6oK8.md)
`XWp4k9K6oK8` · AI LABS · 2026-01-02 · q3 · practitioner · tutorial · topics: coding-agents, context-engineering, agent-architecture, testing-verification

Anthropic's long-running-agent harness: an initializer agent sets up a JSON feature list, progress file and git repo, then a coding agent implements one feature per session with browser testing and commits, so work survives compaction.

- Techniques: Initializer + incremental coder harness; Forced browser verification via Puppeteer; Resume from state, not from context
- Tools: Claude Code, Claude.md, Puppeteer, Git, Next.js, BMAD

## [Claude Released Something To Fix Your Errors](../videos/NuKrtiJqW3Y.md)
`NuKrtiJqW3Y` · AI LABS · 2026-01-02 · q2 · practitioner · tutorial · topics: testing-verification, coding-agents, context-engineering, voice-multimodal

Tips for testing web apps with Claude Code's Chrome extension: full-page screenshot scripts, CLAUDE.md context and cookie-banner rules, split test files, progress reports across compaction.

- Techniques: Full-page screenshot script behind a slash command; CLAUDE.md rule to limit DOM extraction; Cookie-banner dismissal script run first; Authenticate before handing off the task; Split end-to-end testing into per-area test files; Progress report after each test file; Compact and check context before browser test runs; Guided testing slash command
- Tools: Claude Code, Claude Code Chrome extension (Claude in Chrome integration), Playwright MCP, Puppeteer MCP, Google Chrome, Google Docs, Google Sheets, CLAUDE.md, Chrome Manifest V3 extensions

## [Claude Cluster is Insane… Upgrade Your Claude Code Workflow ](../videos/V-xBaFveTvA.md)
`V-xBaFveTvA` · AI LABS · 2026-01-02 · q2 · intro · review · topics: claude-code, multi-agent, coding-agents, dev-tools

AI LABS walkthrough of Claude Code background subagents, using git worktrees to run parallel agents on isolated branches, plus a few changelog features. Hype title, sponsored segment, and shallow on mechanics.

- Techniques: Background a research or review subagent; Parallel review fan-out; Worktree-per-agent via a custom slash command; Named project agents via --agent flag; Fork a session on resume; Keep background tasks isolated and named
- Tools: Claude Code (background agents, tasks command, --agent flag, resume flag, custom slash commands, instant auto-compact, prompt suggestions), git worktree

## [The Greatest Design System I've Ever Used](../videos/61Z2jLH4yGU.md)
`61Z2jLH4yGU` · AI LABS · 2026-01-02 · q2 · intro · review · topics: vibe-coding-app-building, mcp-and-tools, product-ux

A short AI-design tool roundup: Design OS for guided planning, image generators, competitor-screenshot style extraction, Figma-to-Lottie animation and an HTML-to-Figma MCP, with a sponsored agency pitch at the end.

- Techniques: Design OS planning loop before building; Competitor style extraction into Claude Code; Figma animation to Lottie to Claude Code; HTML to Figma via MCP
- Tools: Design OS (Builder Methods), Claude Code, Claude, Cursor, GitHub Copilot, Viscom, Google Mixboard, Nano Banana, Go Full Page (browser extension), Figma, Magic Animator (Figma plugin), Lottie (Figma plugin)

## [5 Ways To Build Beautiful Websites Using Claude Code](../videos/VGYsHicpp34.md)
`VGYsHicpp34` · AI LABS · 2026-01-02 · q2 · intro · review · topics: vibe-coding-app-building, coding-agents, testing-verification

A design-first workflow for building websites with Claude Code: shadcn presets, Coolers palettes, Google Stitch designs and prototypes, background browser-testing agents, and Drawbridge for visual fixes. Partly a promo for the presenter's agency.

- Techniques: shadcn preset import; Palette before layout; Design in Stitch, then hand off to Claude; Screenshot-driven inspiration; Background browser-test subagent; Drawbridge visual issue reporting
- Tools: shadcn/ui, Coolers, Google Stitch, Gemini 3 Pro, Nano Banana, Google AI Studio, Jules, Claude Code, Claude subagents (background mode), Puppeteer MCP, Drawbridge, Opus 4.5 (named as context)

## [OpenAI's New Release Is WILD](../videos/75SHVbKCe44.md)
`75SHVbKCe44` · AI LABS · 2026-01-02 · q2 · intro · news · topics: evals, models-research, security-guardrails

OpenAI's "confession report" method for reducing model dishonesty, as a short, mostly critical take: the speaker argues it rewards admissions rather than accuracy and only helps identify errors, not prevent them.

- Techniques: Confession report after each response; Classify outcomes on a 2x2 grid (answer correct or wrong x confessed or not)
- Tools: OpenAI models (ChatGPT, unnamed model in the study), Claude (referenced in passing as a reward-hacking example), YouWear (sponsor, AI app builder)

## [10 Crazy Ways To Use Nano Banana Pro](../videos/OWdlgdQSR60.md)
`OWdlgdQSR60` · AI LABS · 2026-01-02 · q2 · intro · review · topics: voice-multimodal, models-research

A 5-minute AI LABS walkthrough of ten prompting and editing tips for Google's Nano Banana Pro image model, with a Make.com sponsor segment and a brief SynthID note.

- Techniques: Iterative single-feature edits; Context word for style; Infographic prompt pattern; Entity locking with reference images; Search grounding before generation; Narrative storyboard prompt; Sketch or wireframe as input; Resolution and texture in the prompt
- Tools: Nano Banana Pro (Google image model), Gemini (watermark, plans), Google Search (grounding), SynthID (invisible watermark), Make.com (sponsor)

## [GLM 4.7 is INSANE For Software Dev...](../videos/JaLycsbTlHU.md)
`JaLycsbTlHU` · AI LABS · 2026-01-02 · q3 · practitioner · review · topics: coding-agents, token-cost-efficiency, models-research

AI LABS tests Z.ai's GLM 4.7 as a Claude Code backend: cheap coding plan, better architecture than 4.6, but slow and not autonomous enough to run unattended.

- Techniques: Config GLM as the Claude Code backend via settings.json; Design-only UI benchmark prompt; Back-end-ready mock data structure; Steer a weak autonomous run
- Tools: GLM 4.7 (Z.ai), GLM coding plan (Z.ai), Claude Code, Claude Sonnet 4.5, Claude Max plan, Next.js, shadcn/ui, Framer Motion, Gemini 3, GPT-5, Humanity's Last Exam (benchmark), SWE-bench (benchmark)

## [AI Coding Finally Fixed, New AI Models, Huge Gemini Deal and More!](../videos/noxDpgSsops.md)
`noxDpgSsops` · AI LABS · 2025-12-02 · q2 · intro · news · topics: models-research, coding-agents, pr-code-review

AI LABS' first Context Weekly roundup: GitHub Agent HQ as a multi-agent command center, Cursor 2.0 with its Composer model, and assorted model, product and robotics announcements, mostly relayed from press coverage.

- Techniques: Clarify-then-dispatch planning for multiple agents; Side-by-side model comparison on one prompt; Select-and-ask UI fix loop in a built-in browser; Mid-reasoning context injection
- Tools: GitHub Agent HQ, Cursor 2.0, Composer (Cursor model), Chrome DevTools, Gemini 3 Pro (preview, expected), Nano Banana 2 (image model, expected), GPT-5.1 (rumored), Design Arena, ChatGPT, Claude (financial services features), Excel, 1X NEO

## [There’s a New Way To Corrupt AI Models](../videos/D5QeUQ4VbjM.md)
`D5QeUQ4VbjM` · AI LABS · 2025-12-02 · q2 · intro · news · topics: models-research, security-guardrails, testing-verification

Recap of an Anthropic study: teaching a model to reward-hack in coding generalized into broader misalignment, and some fixes only masked it. Secondhand and hype-titled.

- Techniques: Permissive framing for hacking in a research environment (reported mitigation); Avoid explicit 'do not hack' system prompts for measurement; Test mitigations on hard tasks, not only simple ones
- Tools: Claude Code, Claude Sonnet 3.7, Claude Sonnet 4.5, Code Cloud (sponsor, not relevant)

## [Claude Just Solved Their Biggest Problem](../videos/opZpIN8g_6M.md)
`opZpIN8g_6M` · AI LABS · 2025-12-02 · q3 · intro · review · topics: mcp-and-tools, context-engineering, token-cost-efficiency, sandboxing-execution

Walkthrough of Anthropic's paper on running MCP servers as code files instead of direct tool calls, to cut context bloat; no implementation shown.

- Techniques: Filesystem-based MCP tool catalogue with progressive disclosure; Result shaping inside the execution script; Code-owned control flow between tool calls; Placeholder returns for sensitive data; File-based state for resumable runs
- Tools: MCP (Model Context Protocol), Claude, Claude skills, Memory tool, Cloudflare code mode, TypeScript, index.ts (file convention from the paper)

## [You can literally win 50K... Just By Prompting](../videos/yq3EN46qw_U.md)
`yq3EN46qw_U` · AI LABS · 2025-12-02 · q2 · intro · tutorial · topics: coding-agents, mcp-and-tools

Sponsored walkthrough of Apify's $1M actor-building challenge (Nov 2025 to Jan 31 2026), showing how Claude Code plus Apify's agent prompt and CLI can produce a publishable actor quickly.

- Techniques: Template to agent prompt to CLI deploy; Actor publish checklist; Idea sourcing from published wish lists
- Tools: Apify (actor platform, Apify Store, Apify console), Apify CLI, Claude Code, Google Maps (scraper input requires a Google API key), Gemini MCP (actor built by the host), MCP server template (Apify), Discord

## [Gemini Designer is INSANE... Build Beautiful Websites in Minutes](../videos/v9Rd_l6gLjU.md)
`v9Rd_l6gLjU` · AI LABS · 2025-12-02 · q3 · practitioner · tutorial · topics: vibe-coding-app-building, product-ux, coding-agents, context-engineering

Walkthrough of Google Stitch, an AI UI designer, plus a six-phase Klein rules-file workflow that turns exported Stitch HTML into a Next.js app and validates it against the designs.

- Techniques: Iterative screen-by-screen prompting in Stitch; Design-system extraction from exported HTML (phase 1); Per-page analysis and component library (phases 2-3); Navigation-flow mapping (phase 4); Blueprint-then-implement (phase 5); Validation checklist and scorecard (phase 6); Build from HTML, not screenshots
- Tools: Google Stitch, Klein (VS Code extension, multi-model, rules file, MCP store), VS Code, Next.js, Figma (via Klein's MCP store), ChatGPT (GPT-5 Temporary), Claude Pro, Material UI, Arc browser (example prompt)

## [Here's What They Didn't Tell You About Gemini 3](../videos/kyflIo3EKLw.md)
`kyflIo3EKLw` · AI LABS · 2025-12-02 · q2 · intro · review · topics: models-research, coding-agents, vibe-coding-app-building, context-engineering

Hands-on review of Gemini 3 vs Claude and GPT-5.1 for UI generation and multi-phase coding; the speaker finds Gemini 3 strong at UI design but credits the agent harness, not the model, for most of the difference.

- Techniques: Same-spec head-to-head coding test; Separate model from harness; One-shot UI test with no guidance; Track context-window use per story
- Tools: Gemini 3 Pro, Gemini CLI, Google Antigravity (VS Code fork), Google AI Studio (Code Assistant), Claude 4.5, Claude Code, Claude desktop app, Claude canvas, GPT-5.1, GPT-5, nano banana (image model, named by the speaker)

## [I Tested the 20% Claude VS ChatGPT Plans To Decide Which is Better](../videos/ageSodnKpw0.md)
`ageSodnKpw0` · AI LABS · 2025-12-02 · q2 · intro · review · topics: token-cost-efficiency, coding-agents

A consumer comparison of ChatGPT Plus and Claude Pro at $20/month, covering model access, usage windows, context, file and image limits, deep research, connectors, and coding tools. Its verdict is to choose by use case, and it contains a sponsored segment.

- Techniques: Put large reference sets in a Claude project; Run Claude deep research for a cited report
- Tools: ChatGPT Plus, Claude Pro, GPT-5, GPT-4o, o4-mini, Claude Haiku, Claude Opus, Sora, Codex, Claude Code, MCP, GitHub

## [Claude Killer? My Review on Kimi K2 Thinking After Days of Testing](../videos/fjCwC6BYKAE.md)
`fjCwC6BYKAE` · AI LABS · 2025-12-02 · q2 · practitioner · review · topics: models-research, coding-agents, token-cost-efficiency

Hands-on review of Moonshot's Kimi K2 Thinking via a coding agent: cheap and context-efficient, but slower and weaker than Claude on UI, game and feature-addition tasks.

- Techniques: Same-prompt A/B against a reference model; Feature addition to an existing codebase; Iterate the prompt on a stuck build
- Tools: Kimi K2 Thinking (Moonshot AI), Claude (Sonnet 4.5 named as the comparison point), GPT-5, Klein (transcribed name, likely the Cline VS Code coding agent; used as the editor agent), Firebase Authentication, Make (sponsor)

## [A Problem You Never Knew About](../videos/w3pmfaczpLc.md)
`w3pmfaczpLc` · AI LABS · 2025-12-02 · q2 · intro · review · topics: product-ux, mcp-and-tools

Sponsored demo of Thesis's C1, a generative UI API that turns LLM output into interactive components (forms, tables, dashboards) via a React SDK. Pitch-level; no evaluation data.

- Techniques: Generative UI middleware in front of the LLM; Two-step retrofit of an existing AI app; Form submission as the next prompt; Documentation skill for coding agents
- Tools: Thesis C1 (generative UI API), C1 React SDK, Vercel AI SDK (transcribed as 'Versal AI SDK'), GPT-5, Claude, Claude skill (custom, for C1)

## [Claude Just Introduced a New Way To Fix Your UI](../videos/eLDq5TfIHys.md)
`eLDq5TfIHys` · AI LABS · 2025-12-02 · q2 · practitioner · review · topics: skills-self-improvement, claude-code, context-engineering, vibe-coding-app-building

AI LABS tests Anthropic's front-end design skill guidance in Claude Code: typography and theme prompts, a 400k-token mega-prompt, and skills that often fail to auto-load.

- Techniques: Turn a design prompt into a project skill; Force-invoke the skill by name; Describe design as implementation, not taste; Name the fonts explicitly; Stage the design prompt per dimension, then combine; Artifacts builder skill for componentized output
- Tools: Claude Code, Claude skills, Claude desktop app, Google Fonts, React, shadcn-style UI (as generated by Claude), Zen Browser, Arc Browser, Anthropic front-end design cookbook, Claude Code front-end design plugin

## [Here's What They Didn't Tell You About Claude's New Model - Opus 4.5](../videos/IZhGvZ4UlPs.md)
`IZhGvZ4UlPs` · AI LABS · 2025-12-02 · q2 · intro · review · topics: models-research, coding-agents, evals

A hands-on review of Claude Opus 4.5 covering the launch benchmarks, system-card safety findings, and side-by-side coding tests against Gemini 3 Pro and Sonnet 4.5.

- Techniques: Epics-and-stories spec before building; Identical-prompt cross-tool comparison; Steerability probe via style cue; Functional check beyond visuals; Human-judgment fallback when automated evals saturate
- Tools: Claude Opus 4.5, Claude Sonnet 4.5, Claude Code, Claude desktop app, Cursor, Gemini 3 Pro, GPT-5.1, SWE-bench, tau-squared-bench (tau2-bench), MonkeyType (test-app target, not a tool used), Swift

## [I Was Using Claude Skills Wrong... The Ultimate System](../videos/fHGMA8hLNt8.md)
`fHGMA8hLNt8` · AI LABS · 2025-12-02 · q2 · intro · review · topics: claude-code, skills-self-improvement, context-engineering

A list of about 21 to 22 use cases for Claude Skills, from coding tasks like tests and CI/CD to business, personal and content workflows. Mostly unmeasured ideas, with a sponsor segment.

- Techniques: Skill folder with references, assets and scripts; Test-and-report skill; Clarify then generate; Template-driven document generation; Stateful skill with a maintained data file; Saved personal profile for planners
- Tools: Claude Code, Claude Desktop app, Claude Skills, Docker, GitHub Actions, npm package (unnamed), Appify (sponsor)

## [Claude Might Be Going In A Different Direction + More](../videos/fiHrS04ZUA8.md)
`fiHrS04ZUA8` · AI LABS · 2025-12-02 · q2 · intro · news · topics: models-research, security-guardrails, coding-agents

AI LABS weekly roundup (Dec 2025) covering GPT-5.1, Gemini 3 leaks, Google agents, an Anthropic robot-dog experiment, an Anthropic report on a Claude Code-driven espionage campaign, and IBM quantum processors.

- Techniques: Usage-limit fallback to a smaller model; Plan-then-approve for deep research
- Tools: GPT-5.1, GPT-5.1 Instant, GPT-5.1 Thinking, GPT-5.1-Codex, GPT-5 Codex Mini, Codex, ChatGPT, GitHub Copilot, Gemini 3, Nano Banana 2, Google Maps, Google Opal

## [I've Found A Better Alternative to Lovable.dev](../videos/05Bg0yI7Ob4.md)
`05Bg0yI7Ob4` · AI LABS · 2025-11-02 · q2 · intro · review · topics: vibe-coding-app-building, coding-agents

A sponsored walkthrough of Leap, an AI app builder on the Encore backend framework, pitched as a Lovable alternative that scales. It shows building a shop, deploying, and handing the repo to Claude Code.

- Techniques: Step-by-step MVP prompting for a generated app; Reference-image fixes for UI drift; Auth as a detailed prompt; Clone-and-continue handoff to a local coding agent; Give the agent a platform rule file; Scope agent edits tightly
- Tools: Leap, Encore (open-source backend framework; Encore Cloud), Lovable, Claude Code, Cursor, React, shadcn/ui, Unsplash, AWS, Google Cloud Platform

## [Before You Pay for Manus AI, See What This Free Tool Can Do](../videos/S3Q7CCV_PzE.md)
`S3Q7CCV_PzE` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: local-ai, multi-agent, agent-architecture

Walkthrough of installing and running Agentic Seek, an open-source Manus-style multi-agent tool that runs locally or through a cloud API, with the speaker's hardware and cost caveats.

- Techniques: Install from the README; Switch config.ini from local to API mode; Headless browser and voice options; Start order; Planner plus specialized agents
- Tools: Agentic Seek (version not stated), Manus AI, Docker, Python 3.10, Ollama, Qwen, DeepSeek, GPT-4o, GPT-4o mini, Cursor (editor used for config)

## [How to 10X Your Claude Code Workflow](../videos/xhrqmAWI_cw.md)
`xhrqmAWI_cw` · AI LABS · 2025-11-02 · q2 · intro · review · topics: coding-agents, claude-code, multi-agent, context-engineering

Walkthrough of a compound-engineering Claude Code plugin (plan, work, review, triage, codify, resolve commands) that persists to-dos and runs parallel review agents. Practical, but the 10X title is unmeasured.

- Techniques: Plan, work, review, triage, codify, resolve command loop; Built-in to-do tool as the phase ledger; Pause-per-phase human checkpoint; Context check before each phase; Language- and concern-specific parallel review agents; Dependency-graph parallel resolution of to-dos; Git ingest for Q&A on a repo; Install as a plugin via marketplace
- Tools: Claude Code, compound engineering (Claude Code plugin), Claude Code plugin marketplace, Claude Code built-in to-do tool, GitHub issues, git worktrees, git ingest, BMAD method (compared, not used), Next.js, FastAPI, Python, TypeScript

## [The PERFECT Design Workflow with Claude Code](../videos/9uFVCxfkLCo.md)
`9uFVCxfkLCo` · AI LABS · 2025-11-02 · q2 · intro · review · topics: vibe-coding-app-building, coding-agents, mcp-and-tools, context-engineering

Walkthrough of capturing a website component with the Web2 MCP Chrome extension, cloning it one-to-one with a Claude Code/Cursor agent using a modified CLAUDE.md, and generating variants with SuperDesign. Mixed results, with a Rocket.new sponsor segment.

- Techniques: Capture an element with Web2 MCP and reference it by ID; Initialize SuperDesign rule files and edit CLAUDE.md for one-to-one cloning; Two-session workflow: clone first, then generate variants; Use SuperDesign's canvas view to inspect how a design was produced
- Tools: Web2 MCP (paid Chrome extension and MCP server; $2.50/month Pro tier as stated), MCP Pointer (open-source alternative, judged weaker), SuperDesign (superdesign.dev; editor extension with rule files for Cursor, Windsurf and CLAUDE.md), Claude Code, Cursor, Windsurf, Stagewise (mentioned as a prior featured tool), Arc browser, shadcn/ui (described as the common component library), Rocket.new (sponsor; no version), Netlify (mentioned in the Rocket.new segment)

## [3 Ways to Clone Any Site Using Cursor AI](../videos/zmP8Pl-MJXw.md)
`zmP8Pl-MJXw` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · topics: vibe-coding-app-building, mcp-and-tools, coding-agents

Three practical ways to clone a website's design into a Next.js or HTML project using Cursor plus Gemini, the Figma MCP, or the Firecrawl MCP, with the presenter noting where each one falls short.

- Techniques: Full-page screenshot capture for layout cloning; Marker-based splitting of generated code into a Next.js app; Figma selection link to Cursor via the Figma MCP; Turning a GitHub repo into indexable docs for Cursor; Scraping a live site with Firecrawl MCP for a structural clone; Build clones in a framework, not plain HTML
- Tools: Cursor, Gemini (canvas feature), Claude artifacts, ChatGPT, Chrome DevTools (command runner, full-size screenshot), React, Next.js, bash (integrate.sh script), Figma MCP, git2doc, Firecrawl MCP (8 tools), Wallhaven (example site)

## [Google A2A Protocol Explained: Tutorial, Demo, & How It Works with MCP & AI Agents](../videos/GUozMSpnmcc.md)
`GUozMSpnmcc` · AI LABS · 2025-11-02 · q2 · intro · review · topics: mcp-and-tools, multi-agent

Explainer of Google's A2A (agent-to-agent) protocol: agent cards for discovery, how it complements MCP, a hiring demo, and a CrewAI sample repo to clone.

- Techniques: Select a remote agent by its card before delegating; Expose agent cards as MCP resources; Generate A2A client and server code from the docs; Quickstart with the sample agent repo
- Tools: A2A protocol (Google), MCP (Model Context Protocol), Google Agentspace (spoken as 'agent space'), Google Agent Development Kit (ADK), LangChain, CrewAI, Gemini API, Cursor (@docs feature), Google A2A GitHub repo (sample agents; name not stated)

## [Deepseek R1 vs O1: Here’s Why R1 Crushes It!](../videos/ciLo6YtqvL0.md)
`ciLo6YtqvL0` · AI LABS · 2025-11-02 · q2 · intro · review · topics: models-research, evals, token-cost-efficiency

A hands-on, anecdotal test of DeepSeek R1 against OpenAI o1 on about ten reasoning and coding prompts. R1 passes 8 of 10 and is pitched as open-weight and cheap, but the verdict rests on single runs.

- Techniques: Mixed reasoning probe battery; Read the visible reasoning trace to locate the failure; Render generated outputs before grading; Distill a reasoning model into small open-base models
- Tools: DeepSeek R1 (open weights, MIT license), DeepSeek R1-Zero (transcript 'R10'), DeepSeek V3 (base model for R1), DeepSeek chat platform with DeepThink toggle, DeepSeek API, Qwen distilled models (1.5B, 7B, others), Llama 3.3 distilled model, OpenAI o1, OpenAI o1-mini, Claude Sonnet, SVG viewer, browser HTML viewer

## [These Factory AI Droids Built My App in 10 Minutes! (Rust + TypeScript!) 👉 Code, Debug & Ship Apps](../videos/4ZYxlTPX-LM.md)
`4ZYxlTPX-LM` · AI LABS · 2025-11-02 · q2 · intro · review · topics: coding-agents, software-factory, multi-agent

A hands-on tour of Factory's "droids" (role-specialized coding agents) building a Tauri desktop chat app, covering local bridge setup, command approval, and a model-switch debug. Thin on depth; the title overstates it.

- Techniques: Role-split agent team; Paired local bridge for hosted agents; Pre-approved command checklist with per-command risk prompts; Live file-diff preview during agent edits; Model-swap triage for a model-dependent bug
- Tools: Factory Droids, Factory Bridge (desktop app), Tauri, Rust, TypeScript, OpenAI API, GPT-4, Gemini 2.5 Pro, Notion (integration named), Jira (integration named), Linear (integration named)

## [This $8/hr AI Engineer Could Replace Junior Devs | Devin AI | Agentic Developer.](../videos/rfWx5zB0Cws.md)
`rfWx5zB0Cws` · AI LABS · 2025-11-02 · q2 · intro · review · topics: coding-agents, software-factory, security-guardrails

AI LABS walks through Devin's general availability: Slack/GitHub-driven autonomous coding, a self-QA demo, a $500/month plan the narrator converts to about $8/hour, and a live-share security leak. Mostly demo and hype, few hard numbers.

- Techniques: Assign work from Slack, get progress in-thread; Agent-driven E2E QA on every push; Bootstrap an unfamiliar repo by fix-and-run loop; Sign-up sequence to start a Devin account
- Tools: Devin (Cognition), Slack, GitHub, VS Code Live Share, Rust documentation (consulted by the agent), SWE-bench (vendor-reported results), o1-preview (comparison model, named in video), Cursor (mentioned in others' takes)

## [Time to UPGRADE... Agent OS Replaces 95% of AI Coding](../videos/0rK4-8TryBo.md)
`0rK4-8TryBo` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: coding-agents, context-engineering, claude-code

Walkthrough of Agent OS for Claude Code and Cursor: base and tool installs, opinionated standards files, roadmap-driven builds, and spec/resume commands. Mostly one demo run; the 95% claim is unsupported.

- Techniques: Two-stage install; Edit the standards folder before the first plan; Plan-product prompt structure; Roadmap-driven build loop; create-spec for new features; Custom tool-routing rule for a component library; Resume with execute-task; Retrofit with analyze-product; Invoke rules by tool syntax
- Tools: Agent OS (spoken as AgentOS), Claude Code, Cursor, Next.js, pnpm, npm (avoided in demo), ShadCN UI, ShadCN MCP server, TweakCN (spoken as tweak cn)

## [How the 1% ACTUALLY Build Apps with Cursor's Context Engineering](../videos/QgA55EnmUp4.md)
`QgA55EnmUp4` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · topics: context-engineering, coding-agents, vibe-coding-app-building

A hands-on workflow for building a full app with Cursor or Claude Code by splitting context into a PRD-generated docs folder, a short always-on rule, and a staged implementation plan.

- Techniques: Four-file documentation set generated from a PRD; Small always-attached workflow rule that routes to on-demand docs; Staged implementation plan with optional subtask lists; Put the foundations and scope into the generate prompt; Claude Code slash command for the generate step; Parallelize only independent work
- Tools: Cursor, Claude Code, CLAUDE.md, ChatGPT, Next.js, FastAPI

## [Cursor AI Just Got a Massive Upgrade Over Claude Code](../videos/WKy71aZHx20.md)
`WKy71aZHx20` · AI LABS · 2025-11-02 · q2 · practitioner · review · topics: coding-agents, claude-code, token-cost-efficiency

A solo creator's hands-on comparison of Cursor's new agent features (plan mode, hooks, slash commands, worktrees, browser control) against Claude Code, concluding Cursor wins on usability and that subscribing to both is the best setup.

- Techniques: Share custom commands between Cursor and Claude Code; Plan first, then build; One git worktree per agent; Browser test-and-fix loop; Shareable prompt deep links; Guard auto-run with before/after tool hooks; Split models across two subscriptions
- Tools: Cursor, Cursor Auto mode, Cursor CLI, Claude Code, Claude Code VS Code extension, Claude Sonnet 4.5, Playwright, Playwright MCP, Conductor, Warp Code, Claude Router, Linear

## [How I Build Beautiful Websites With AI](../videos/1cB2iqz_vnM.md)
`1cB2iqz_vnM` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · topics: claude-code, coding-agents, vibe-coding-app-building, context-engineering

Walkthrough of Drawbridge, an open-source Chrome extension that turns clicks on a localhost page into a queued task list for Claude Code or Cursor, with landing-page and client-prototyping use cases. Main takeaway: UI fixes become batched, position-aware agent tasks.

- Techniques: Install Drawbridge as an unpacked Chrome extension; Queue element-level UI changes; Have the agent process the queue; Turn the Cursor workflow rule into a Claude Code slash command; Build a landing page section by section; Keep a design language in files the agent reads
- Tools: Drawbridge (open-source Chrome extension and visual editor for coding agents), Chrome (extensions, load unpacked), Cursor, Claude Code, shadcn/ui, TweakCN (shadcn theme site), Lumi (sponsored AI website builder), Git (used to revert the demo project)

## [Agno AI Agent Tutorial: Build & Run AI Agents with Agent UI + MCP + CrewAI (Best Tutorial)](../videos/RWQv6JV7rKw.md)
`RWQv6JV7rKw` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: multi-agent, mcp-and-tools, agent-architecture

A short tutorial on Agent UI, an open-source Next.js chat front-end for agents. It shows swapping Agno's playground for a FastAPI backend and routing between specialist agents over A2A.

- Techniques: Install Agent UI via the docs' npx template; Swap the Agno Playground for your own backend; Main-agent router over specialist endpoints; Cap reply length with the system prompt
- Tools: Agent UI, Agno, Agno Playground, Next.js, npx, FastAPI, OpenAI SDK, A2A (agent-to-agent protocol), Cursor, LangChain, gpt-4o-mini, Gemini 2.5 Pro (mentioned in the demo answer, not used by the presenter's own setup)

## [The WhatsApp Trick That’s Running My Business for Me](../videos/BjqR3Ddb71k.md)
`BjqR3Ddb71k` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: mcp-and-tools, voice-multimodal

A 6-minute setup tutorial for a local WhatsApp MCP server plus the ElevenLabs MCP in Claude Desktop, so an agent can read WhatsApp chats and reply with a synthesized voice note.

- Techniques: Local WhatsApp MCP setup in Claude Desktop; Adding the ElevenLabs MCP with one env var; Prompt the agent with an explicit contact name; Windows build fix for the WhatsApp bridge
- Tools: Claude Desktop, WhatsApp MCP server (Go bridge + MCP), ElevenLabs MCP, ElevenLabs voice cloning, uv / uvx, Go, Cursor, Windsurf, Blender MCP, Swift (planned app), MCP

## [Get Started with Claude’s Computer Use API – Full Setup & Demo](../videos/XSXaGvCRJ3c.md)
`XSXaGvCRJ3c` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: voice-multimodal, sandboxing-execution, token-cost-efficiency

A 4-minute walkthrough of Anthropic's Computer Use API beta: run the setup container locally with Docker and your API key, then watch Claude operate a sandboxed virtual Linux desktop from a chat prompt.

- Techniques: Run computer use inside a disposable container; Give a multi-step browsing prompt and watch the screenshot loop
- Tools: Claude Computer Use API (Anthropic, beta), Claude API key (Anthropic), Docker, WSL2, Ubuntu, Bolt.new (named only as the video the agent found on the channel, not used as a tool)

## [Zapier MCP: The Only MCP Server That Cursor Needs](../videos/tFFsX97HzEk.md)
`tFFsX97HzEk` · AI LABS · 2025-11-02 · q2 · intro · review · topics: mcp-and-tools, coding-agents, security-guardrails

Zapier's hosted MCP server replaces a pile of local MCP servers with one endpoint, per-action tool selection and fixed-argument control. Useful setup detail, but a vendor walkthrough with a hype title.

- Techniques: Consolidate local MCP servers into one hosted endpoint; Add only the specific tool actions an agent needs; Fix routing fields, leave content fields to the model; Override model-sent arguments on the server side; Connect a Postgres database for read and write actions
- Tools: Zapier MCP server, WebParse by Zapier, Cursor, mcp.json, Postgres, Official Postgres MCP server (read-only, per presenter), Supabase MCP server (noted as missing from Zapier), Composio (compared; manual auth grants), Slack, Jira, GitHub, GitLab

## [Get 400K+ Al Apps on this site...](../videos/jEYHsyiTwso.md)
`jEYHsyiTwso` · AI LABS · 2025-11-02 · q2 · intro · review · topics: models-research, local-ai

A five-minute tour of Hugging Face Spaces: a public directory of 400K+ community AI apps and hosted open models, shown through logo placement, image-to-3D, image extension and comic generation demos.

- Techniques: Discover demo apps via the Spaces directory; Try an open model through its hosted demo before running it locally; Publish a project as a Space to share a demo
- Tools: Hugging Face Spaces, Flux (Flux Dev), Trellis, Janus Pro 7B, Qwen 2.5 Max, Midjourney, o3 mini (attributed to ChatGPT), AI Comic Factory, Neural Jam, Blender (mentioned as the target for GLB export), GLB (3D file format)

## [Replit Has Become Essential to My Vibe Coding Workflow.](../videos/YtgqzCEeHVw.md)
`YtgqzCEeHVw` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: coding-agents, vibe-coding-app-building, context-engineering

Walkthrough of a vibe-coding workflow: Claude brainstorms and writes a no-code front-end prompt, Replit generates a shadcn-based responsive UI with exposed APIs, and Windsurf builds the FastAPI backend from the exported API docs.

- Techniques: Planning prompt with pages and modals; Front end first, API docs as the contract; Dependency and run step for a generated front end; Send browser context to the agent; In-memory storage first, database later
- Tools: Claude (Anthropic), Replit, shadcn/ui, Windsurf, Cascade, Cursor, v0, FastAPI, npm, SuperWhisper, macOS voice dictation, Supabase

## [The $10B System Prompts Behind Cursor AI and Others Just Leaked…](../videos/A5r2tfifYfY.md)
`A5r2tfifYfY` · AI LABS · 2025-11-02 · q2 · intro · review · topics: coding-agents, context-engineering, agent-architecture, sandboxing-execution

Walkthrough of leaked system prompts from Cursor, Windsurf, Replit, Manus and others, with the host's takeaways on tool design, background execution, memory, sandboxing and a repo-to-text trick. Useful as prompt-design evidence, but the verdicts are overreaching.

- Techniques: Repo subfolder to LLM-readable text; Post-edit verification loop; Background command execution with process status checks; Persistent memory with semantic auto-retrieval; Ask-for-secrets and stuck-fallback behavior; Sandbox-scoped guardrails in the system prompt
- Tools: Cursor, Windsurf (Cascade), Replit, Manus, Lovable, Devin, Bolt, Roo Code (transcript: 'Rucode'), Netlify, Next.js, shadcn/ui (transcript: 'Shad CNUI'), PostgreSQL

## [Time to SWITCH...Claude Code vs Cursor debate just ended](../videos/tCy5cJRErTg.md)
`tCy5cJRErTg` · AI LABS · 2025-11-02 · q2 · intro · review · topics: claude-code, coding-agents, dev-tools, mcp-and-tools

Walkthrough of Claudia, a build-from-source desktop GUI over Claude Code with custom agents, per-prompt checkpoints, a preview pane and GUI MCP setup, pitched as a reason to leave Cursor. Hype title; single-tool demo.

- Techniques: Read-only research subagent; Checkpoint before a risky AI change; Visual bug loop with a preview pane; Add MCP servers through a form; Build Claudia from source
- Tools: Claudia, Claude Code, Cursor, Rust, Bun, git, Next.js, shadcn/ui, Claude Pro plan ($20), MCP (stdio and SSE servers), CLAUDE.md, HTML

## [Tempo Labs Tutorial: The Ultimate Vibe Coding Package](../videos/k6uBbUZ9MZg.md)
`k6uBbUZ9MZg` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: vibe-coding-app-building, product-ux

Tutorial walkthrough of Tempo Labs, an AI app builder that wires Next.js, Supabase auth/database and Stripe payments before generating a gradient-wallpaper SaaS from a PRD-first prompt. Mostly a promotional demo with few verified claims.

- Techniques: Pre-wire integrations before the first build prompt; Supabase connection via Tempo; Stripe test-mode wiring; Adding plans through the Stripe product catalog; PRD-first build prompt with a subtask loop; Fix client-side rendering by prompting
- Tools: Tempo Labs (Tempo), Next.js, Supabase, Supabase edge functions, Supabase MCP, Stripe, Stripe webhooks, Mermaid, Cursor, Windsurf, Aceternity UI, Expo

## [The #1 Open Source AI Agent to Stop Overloading Cursor AI (Cursor MCP + ACI.dev Unified Server)](../videos/eWvaItBefYw.md)
`eWvaItBefYw` · AI LABS · 2025-11-02 · q3 · intro · tutorial · topics: mcp-and-tools, coding-agents

Setup walkthrough for ACI.dev's unified MCP server, which exposes search and execute meta-tools so Cursor or Windsurf can reach many MCP apps without loading each one; the speaker's performance and context claims are anecdotal.

- Techniques: Unified MCP server with search and execute meta-tools; Pasting the ACI usage prompt as a Cursor project rule; Recovering from 'user isn't authenticated' errors; Smoke-testing the connection
- Tools: ACI.dev unified MCP server, ACI App Store / agent playground, Cursor, Windsurf, Claude Desktop, Brave Search API, Archive (research papers app), Google Calendar integration, Figma MCP, GitHub MCP, Firecrawl MCP

## [Deploy Project to Netlify Instantly.](../videos/ruRxIGmsCgs.md)
`ruRxIGmsCgs` · AI LABS · 2025-11-02 · q2 · intro · review · topics: vibe-coding-app-building, coding-agents

Windsurf Wave 6 adds "deploys": Cascade publishes a static site to Netlify under a windsurf.build subdomain, which must be claimed in your own Netlify account within 24 hours.

- Techniques: Agent-driven static deploy; Claim within 24 hours; Deploy-log feedback loop; Plan pages and modals first; Specify constraints in the build prompt
- Tools: Windsurf (Wave 6, Cascade agent), Netlify, GitHub, Cursor, netlify.toml

## [DeepClaude: The Combined Power of Deepseek R1 & Claude 3.5 Sonnet!](../videos/ymunCZzgzeg.md)
`ymunCZzgzeg` · AI LABS · 2025-11-02 · q2 · intro · review · topics: models-research, coding-agents

A short walkthrough of DeepClaude, an open-source chat UI that calls DeepSeek R1 and Claude 3.5 Sonnet through their APIs; the presenter installs it, runs one React prompt, and finds it weak as a standalone chat app.

- Techniques: Dual-provider chat setup; Single-prompt comparison test; Per-chat model switching
- Tools: DeepClaude, DeepSeek R1, Claude 3.5 Sonnet, Rust 1.75, npm, React, Aider Polyglot benchmark

## [How to Use Cursor in the Smartest Way Possible](../videos/LXk8nWwOPuY.md)
`LXk8nWwOPuY` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · topics: pr-code-review, coding-agents, context-engineering

A tutorial on pairing Cursor's agent with the CodeRabbit extension: commit each implementation chunk, run a review, feed suggestions back, and drive a phased implementation plan.

- Techniques: Commit-gated review loop; Branch-visibility workaround for missing reviews; One-comment-per-paste fix loop; Phase-by-phase plan with a structure file
- Tools: Cursor, CodeRabbit (VS Code / Cursor / Windsurf extension), Windsurf, Git, GitHub (CodeRabbit sign-in), Gemini 2.5 Pro, Next.js, FastAPI, shadcn/ui (spoken as 'shad cn')

## [Cursor AI Had a BIG PROBLEM — I Just Found the FIX](../videos/UngBxJ9uy70.md)
`UngBxJ9uy70` · AI LABS · 2025-11-02 · q2 · intro · review · topics: mcp-and-tools, coding-agents, context-engineering, multi-agent

AI LABS walkthrough of GitMCP, which turns any GitHub repo into a hosted MCP docs server, shown as an alternative to Context7 for keeping Cursor grounded in current docs, with a three-agent A2A demo.

- Techniques: Per-repo hosted MCP docs via URL swap; Scope docs to one repo instead of a broad doc index; Use the hosted repo chat as a post-build spec check; Router agent plus domain specialist agents over A2A; Routing check by server log
- Tools: Cursor, Gemini 2.5, GitMCP (gitmcp.io), Context7 MCP, MCP (Model Context Protocol), A2A (Google Agent-to-Agent protocol), Claude Desktop, Windsurf, VS Code, Claude, LangGraph (docs example), Three.js (demo project)

## [Add this Chrome Extension to 10X your productivity](../videos/j8KcvLrZ9uU.md)
`j8KcvLrZ9uU` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: agent-architecture, product-ux

A walkthrough of MindStudio's Chrome extension for running prebuilt browser agents and building a simple word-lookup agent with its visual block builder. Mostly a product tour with a hype title and thin technical depth.

- Techniques: Install and pin the MindStudio extension; Build a selection-driven lookup agent in the visual builder; Workaround for end-session returning JSON
- Tools: MindStudio (Chrome extension and agent builder), Chrome Web Store, Arc browser, Claude 3.5 Haiku (free model in builder), GPT 4.0 Mini (free model in builder), ChatGPT (mentioned as the manual alternative), Cursor (mentioned), Windsurf (mentioned)

## [Gemini 2.0 Tested: Google's New Models Are No Joke!](../videos/XcQhApQVPCY.md)
`XcQhApQVPCY` · AI LABS · 2025-11-02 · q2 · practitioner · review · topics: models-research, evals, token-cost-efficiency

AI LABS runs a hands-on test of Gemini 2.0 Flash, Flash-Lite ("Flashlight") and Pro on 10 quick prompts: Flash-Lite is fastest and cheapest, but coding and reasoning results are mixed.

- Techniques: Fixed prompt suite with per-model latency and pass/fail; Run generated code before scoring it; Trick-question check for reasoning; Shortlist with quality-vs-price and speed charts before hands-on tests
- Tools: Gemini 2.0 Flash, Gemini 2.0 Flash-Lite (called 'Flashlight' in the video; name is an auto-caption-based guess), Gemini 2.0 Pro (experimental), Trillium TPU (named as Google's new chip, unverified link to the speed gains), Nvidia GPUs, Artificial Analysis (benchmark charts), o3-mini, GPT-4o, GPT-4 mini, o1, DeepSeek R1, Qwen 2.5 Max (auto-caption 'Quen 2.5 Max')

## [ChatGPT Apps vs n8n vs AgentKit: The Future of AI Automation](../videos/lcqlgif2hFA.md)
`lcqlgif2hFA` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · topics: mcp-and-tools, vibe-coding-app-building, product-ux

Walkthrough of building a ChatGPT app as a self-hosted MCP server (Express, Google Places API) exposed through ngrok and registered in ChatGPT developer mode. Title promises an n8n/AgentKit comparison that never appears.

- Techniques: Prompt-driven MCP server scaffold for a ChatGPT app; Reuse an existing MCP server as a ChatGPT app; Expose localhost with ngrok for ChatGPT; Register the MCP endpoint in ChatGPT developer mode; Widget output over plain text, polished with ShadCN
- Tools: ChatGPT apps (OpenAI), OpenAI apps SDK, MCP (Model Context Protocol) SDK, Express, Google Places API, ngrok, ShadCN, Cursor, Codex, Claude Code, Make.com (sponsor), n8n (named in title only)

## [AI Tool Converts Your Sketch into Code Instantly!](../videos/p5hEVQIisgc.md)
`p5hEVQIisgc` · AI LABS · 2025-11-02 · q2 · intro · review · topics: vibe-coding-app-building, product-ux, inference-serving

Demo and local-install walkthrough of Groq App Gen, an open-source web app that generates and iterates on small web apps from a sketch plus text prompts on Groq inference; speed is asserted, not measured.

- Techniques: Local install of Groq App Gen; Sketch then prompt; One change per prompt, verify each; Generate the edit list with a second LLM
- Tools: Groq App Gen (open-source web app, GitHub repo), Groq API / Groq inference, Llama 3.3 70B (spoken as 'Lama 3.37 70 billion' in captions), Next.js, TypeScript, npm, Python, VS Code, Windsurf, Cursor, ChatGPT

## [Automate Your Browser with AI Using StageHand AI Agent](../videos/PPutzww1RaM.md)
`PPutzww1RaM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: voice-multimodal, coding-agents

Short quickstart for Stagehand, a Playwright-based browser agent with plain-language act, goto and extract APIs, scaffolded with a create-app command and driven from Cursor.

- Techniques: Scaffold a Stagehand project; Plain-language page actions and extraction; Generate Stagehand code in Cursor
- Tools: Stagehand, Playwright, Browserbase, Cursor, Zod, Chromium, GPT-4 (via OpenAI API), Node.js / npm / npx

## [Shadcn Isn’t Just a Library Anymore… Here’s How to 10x Your UI](../videos/V8rGgwQ-VJ0.md)
`V8rGgwQ-VJ0` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · topics: mcp-and-tools, context-engineering, vibe-coding-app-building

Shows how a shadcn/ui MCP server (component demos and blocks) plus Cursor rule files and a plan-first workflow produces better React UI, then how TweakCN restyles the result.

- Techniques: Fetch-before-build loop with the shadcn MCP; Rule file that forces the MCP lookup order; Plan first, with components named and no code; Theme with TweakCN after the structure is done
- Tools: shadcn/ui, shadcn UI MCP server (GitHub repo), Cursor, Claude (chat, used for the initial plan), Claude desktop MCP configuration, Windsurf, Claude Code, TweakCN, GitHub personal access token

## [3 Ways to Make GENUINELY Stunning Websites Using Claude Code](../videos/McJluKfjVGk.md)
`McJluKfjVGk` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · topics: vibe-coding-app-building, claude-code, mcp-and-tools, coding-agents

A walkthrough of three Claude Code workflows for building polished UIs: SuperDesign for iterative design canvases, ShadCN MCP for component-library builds, and Firecrawl or Figma MCPs for cloning existing designs.

- Techniques: SuperDesign canvas setup; Layout-then-theme-then-polish staging; Targeted correction round; ShadCN MCP plus a saved usage-rule slash command; Theme import from tweakcn; Site cloning with Firecrawl MCP; Figma MCP selection import; Animation snippet import from Animatopy
- Tools: Claude Code, SuperDesign (superdesign.dev, VS Code / Cursor extension), Cursor, VS Code, ShadCN UI, ShadCN MCP server, Firecrawl MCP, Figma MCP server, tweakcn, Animatopy, Colors (palette generator website), Next.js

## [What Cursor Doesn't Have: Claude Code Subagents](../videos/Ppu6pJ5yyD4.md)
`Ppu6pJ5yyD4` · AI LABS · 2025-11-02 · q2 · practitioner · review · topics: claude-code, multi-agent, coding-agents, context-engineering

Walkthrough of Claude Code's native subagents: creating project agents with /agents, why isolated context windows help, and how auto-delegation and chaining work. Practical but thin, with a sponsor segment.

- Techniques: Create a project-scoped subagent with /agents; Write a specific description and scope tools tightly; Spec file plus rules file handed to a builder subagent; Theme swap through a subagent; Chain subagents in a custom slash command; Invoke a subagent explicitly
- Tools: Claude Code, Claude Code subagents (/agents), Cursor, ShadCN UI, ShadCN UI MCP server, Next.js, Tailwind CSS v3, TweakCN, TestSprite MCP server, BMAD workflow, SuperClaude workflow, GitHub subagents collection (unnamed)

## [Janus Pro-7B: DeepSeek's New Model](../videos/m7M_EWV_GOg.md)
`m7M_EWV_GOg` · AI LABS · 2025-11-02 · q2 · intro · demo · topics: voice-multimodal, models-research

A short hands-on demo of DeepSeek's Janus Pro 7B multimodal model on a Hugging Face Space, covering formula-to-LaTeX, image and code understanding, and text-to-image, with the speaker's training and limitation claims.

- Techniques: Quick multimodal capability probe; Round-trip check for OCR-to-markup output
- Tools: Janus Pro 7B (DeepSeek, multimodal), Janus Pro 1.3B / 1.5B (mentioned, sizes inconsistent in transcript), Hugging Face Spaces, DALL-E 3 (comparison only), Python (screenshot content), Online LaTeX viewer (unnamed)

## [Figma MCP Tutorial: The Best Way to Clone a Front-End](../videos/FJBLhd23f80.md)
`FJBLhd23f80` · AI LABS · 2025-11-02 · q3 · intro · tutorial · topics: mcp-and-tools, coding-agents, vibe-coding-app-building

A 5-minute tutorial on connecting an open-source Figma MCP server to Cursor, then having the agent generate HTML/CSS from a Figma page link instead of a screenshot.

- Techniques: Run a Figma MCP server over SSE and attach it to Cursor; Copy a link to a Figma selection and hand it to the agent; Force the agent to the node tool when it picks the wrong one; Combine the Figma link with a screenshot for corrections
- Tools: Figma MCP server (glips, open source, run via npx and pnpm), Figma API / personal access tokens, Cursor (MCP client), pnpm, npx, git, HTML/CSS (generation target)

## [NEW Qwen 2.5 Coder (32B): Insane Coding Power Tested! Is This the Best Free LLM?](../videos/4shPVb4RqGQ.md)
`4shPVb4RqGQ` · AI LABS · 2025-11-02 · q2 · intro · review · topics: models-research, local-ai, evals

Informal hands-on test of Qwen 2.5 Coder (32B) against five coding prompts via the hosted demo; it passed three and failed two, and the presenter says to test it yourself before switching from Claude.

- Techniques: Fixed pass/fail prompt set for a quick coder-model smoke test; Trying an open coder model locally with Ollama; Testing in a hosted artifacts sandbox
- Tools: Qwen 2.5 Coder (32B and 7B), Qwen 2.5, Claude 3.5 Sonnet, GPT-4 Omni (GPT-4o), Cursor, Open WebUI, Ollama, Hugging Face (demo space and artifacts), Notion (test list)

## [Sonnet 4.5 Just Unlocked a New Breed of Agents](../videos/t7VuWwukO3I.md)
`t7VuWwukO3I` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · topics: claude-code, coding-agents, mcp-and-tools, agent-architecture

AI LABS walkthrough of running Claude Code as a scheduled GitHub Actions agent (model-news monitor to Slack) and as an issue-triggered background coder, with two rules learned from failed runs: auto-approve tools and test MCP servers first.

- Techniques: Install the Claude Code GitHub app into a repo; Scheduled news monitor on GitHub Actions; Whitelist all tools for headless runs (Rule 1); Verify MCP servers before automation (Rule 2); Post to Slack via incoming webhook with curl; Hand off a background coding task via a GitHub issue; Paste SDK documentation into the task; Verify auth end to end on a branch
- Tools: Claude Code (version 2 announced with Sonnet 4.5), Claude Sonnet 4.5, Claude Code GitHub app, GitHub Actions, GitHub, Slack (incoming webhook via curl), Supabase (auth), Supabase MCP server, Claude Agent SDK (TypeScript and Python docs), BMAD method (referenced), OpenAI Codex (referenced as inspiration for cloud agents), Cursor (referenced for code rewind), GPT-5 (mentioned in the opening)

## [Qwen 2.5 Max vs DeepSeek R1 – Which One is Better? (Tested)](../videos/6o_VFkOEwsI.md)
`6o_VFkOEwsI` · AI LABS · 2025-11-02 · q2 · intro · review · topics: models-research, evals

Hands-on, informal test of Alibaba's closed Qwen 2.5 Max chat model on roughly ten prompts reused from a DeepSeek R1 test; verdict: decent, but below DeepSeek V3 and not open source.

- Techniques: Fixed prompt suite reused across models; Render-and-inspect generated artifacts; Ask for a single-file HTML output for testing; Checkable constraint probe
- Tools: Qwen 2.5 Max (Alibaba, closed model, chat and API only), Qwen 2.5 Plus (default model in the Qwen chat), Qwen 2.5 72B, DeepSeek R1 (reasoning model, baseline), DeepSeek V3, DeepSeek Chat (online HTML preview feature), Phi 3, Llama 3.1, GPT-4o, Claude 3.5 Sonnet, Notion (prompt storage), Arena Hard (benchmark)

## [How I ACTUALLY Use Claude Code... My Complete Workflow](../videos/7Sx0o-41r2k.md)
`7Sx0o-41r2k` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · topics: claude-code, multi-agent, context-engineering, coding-agents

A host walks through a multi-agent Claude Code workflow for building an app: specialized sub-agents run in sequence, each writing its output to docs, with checkpoints for rollback and a generated agent-workflow setup.

- Techniques: Phased sub-agent chain driven by one prompt; Parallel sub-agent fan-out; Docs-first planning with scoped agents; Two-stage requirements before agent planning; Rewind with double-Escape checkpoints; Generate an agent workflow from a repo; Verbose view of sub-agent activity
- Tools: Claude Code, Claude Code sub-agents, Claude Desktop, Claude Opus, Cursor (checkpointing, as cited by the host), BMAD method, SuperClaude, gitingest.com, Next.js, UX researcher agent, sprint prioritizer agent, UI designer agent

## [Wait... Cursor AI Just Launched a New Agent?](../videos/QOJdhje6Vnc.md)
`QOJdhje6Vnc` · AI LABS · 2025-11-02 · q2 · intro · review · topics: coding-agents, claude-code, models-research

Hands-on first look at Cursor's new terminal agent CLI (beta) using GPT-5: install, slash commands, a Kanban app test, and why the host would not switch from Claude Code yet.

- Techniques: First-run setup for Cursor agent CLI; Switch models with /model inside the agent; Retry a stalled agent run with the same prompt; Fixed-prompt smoke test for a coding agent; Give visual feedback when the CLI cannot take images
- Tools: Cursor agent CLI (`cursor agent`), Cursor IDE, GPT-5 (OpenAI), Claude Code, Claude Code Router

## [How to Use Cursor AI with Its Own Cursor Memory Bank](../videos/azXNHRtzd5s.md)
`azXNHRtzd5s` · AI LABS · 2025-11-02 · q3 · intro · tutorial · topics: memory, context-engineering, coding-agents

A short walkthrough of Cline's "Memory Bank" pattern: a set of structured markdown files that keep a coding agent's project context across sessions, set up in Cursor via pasted global rules. Practical but thin, with an admitted rules bug.

- Techniques: Paste a memory-bank rules file into Cursor User Rules; Initialize the memory bank with a single agent-mode prompt; Force plan-then-act with edit blocking; Keep the bank current in act mode
- Tools: Cline (Memory Bank, named 'Klein' in the transcript), Cursor (agent mode, User Rules, Cursor 2), Windsurf, Next.js, React Router, Unsplash API, Mermaid

## [3 Things Before You FINALLY Switch to Codex CLI](../videos/gRXrOuFn9dE.md)
`gRXrOuFn9dE` · AI LABS · 2025-11-02 · q2 · intro · review · topics: coding-agents, context-engineering, multi-agent

Hands-on comparison of Codex CLI against Claude Code: a single-prompt game test, the GUI options for each, an MCP workaround for missing sub-agents, and the BMAD planning method for multi-step builds. Sponsored intro; thin evidence.

- Techniques: Sub-agent delegation through an MCP server; Fork and patch an unmaintained community tool; BMAD-style plan-then-build workflow; Manual agent wiring for Codex; Edit MCP config from inside the Codex IDE extension
- Tools: Codex CLI (OpenAI), Codex IDE extension, GPT-5 Codex High (model used in the test), Claude Code, Phaser 3 (game engine), Kenney assets (spoken as Kenny), Three.js (spoken as 3.js), React, Next.js, shadcn/ui, Opcode (formerly Claudia), Conductor

## [GLM 4.6 Review: Better Than Claude for Coding? (Real Project Tests)](../videos/wEHWvzWOjt0.md)
`wEHWvzWOjt0` · AI LABS · 2025-11-02 · q2 · practitioner · review · topics: coding-agents, token-cost-efficiency, models-research, context-engineering

Hands-on test of GLM 4.6 against Claude Sonnet 4.5 on a UI-design prompt and a multi-epic Svelte 5 build; GLM is far cheaper per message but needed Sonnet to finish integration.

- Techniques: Same-prompt model bake-off for UI work; BMAD epic-to-story decomposition for agent builds; Provision the backend through the database MCP; Commit per fix to attribute regressions to a model; Cheap model for most of the build, strong model for integration; Use a stack with thin training data as a stress test
- Tools: GLM 4.6, GLM 4.5, GLM coding plan (GLM Lite and Max tiers), Claude Sonnet 4.5, Claude Max plan, Claude Code, BMAD method, Svelte 5, Supabase, Supabase MCP, shadcn-svelte, CodeRabbit CLI (sponsor)

## [How to Make Cursor CODE What You ACTUALLY Want.....](../videos/Dv_tSxAA0HE.md)
`Dv_tSxAA0HE` · AI LABS · 2025-11-02 · q3 · intro · tutorial · topics: coding-agents, context-engineering

A short Cursor feature tour: scoped project rules that replace the deprecated .cursorrules file, plus reusable prompts in Notepads, @web search, and custom doc indexing.

- Techniques: Global user rules for all projects; Scoped project rules with description and globs; Reuse community rule files; Reusable prompts in Notepads; Web search and custom docs in chat
- Tools: Cursor, Cursor Composer, cursor.directory, Supabase (examples/prompts repo), Next.js, TypeScript, Python, Tailwind, n8n, MCP (Model Context Protocol)

## [Why Your LLM Answers Are Mediocre (And How to Fix It)](../videos/Ym-iMJ-sds0.md)
`Ym-iMJ-sds0` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: context-engineering, memory, product-ux

Beginner tips for getting better LLM answers in ChatGPT (prompting, context windows, memory, Projects, deep research, Canvas), with a brief tour of Codex, Gemini CLI and Claude Code.

- Techniques: Specific, iterated prompting; Fresh chat per idea; Project system prompt with role and sample output; Escalate from web search to deep research; Canvas for partial edits
- Tools: ChatGPT, GPT-5, Claude, Gemini, Gemini CLI, Codex, Claude Code, Nano Banana, ChatGPT Canvas, ChatGPT Deep Research, ChatGPT Projects, ChatGPT Voice Mode

## [TMUX Coding Is INSANE... Upgrade Your Claude Code Workflow](../videos/UgHbHqg_Wmo.md)
`UgHbHqg_Wmo` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · topics: multi-agent, software-factory, claude-code

Walkthrough of a tmux-based orchestrator that lets one Claude Code agent spawn and manage several Claude Code teams via scheduled check-ins, spec-driven phases, and a skip-permissions setting. Useful pattern, but the live demo never ran.

- Techniques: tmux-based agent orchestrator setup; Fix hard-coded paths and permission command in the orchestrator; Spec folder as the build blueprint; Team start prompt pattern; Scheduled check-ins with restore-point commits; Summarize an unfamiliar repo with GitIngest
- Tools: tmux, Claude Code, tmuxorchestrator (repo name as spoken), Cursor (used only to show the folder structure on screen), shadcn, shadcn MCP, GitIngest (gitingest.com), ChatGPT (mentioned as a comparison for the summary step), Git (version control and restore-point commits)

## [The Only Guide You Need to Build MCP Server.](../videos/kfTDFkhNDFU.md)
`kfTDFkhNDFU` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: mcp-and-tools, coding-agents, context-engineering

Walkthrough of building a minimal Python MCP server with the official SDK, wiring it into Cursor, and using docs and AI generation to wrap a web crawler and a Figma API.

- Techniques: Minimal Python MCP server; Register a local MCP server in Cursor; Feed SDK docs to the coding agent; gitingest to turn a repo into LLM context; Wrap an existing script as an MCP tool; API-to-tool generation from endpoint docs
- Tools: MCP Python SDK (mcp, installed with pip; no version stated), Cursor (agent, Composer, docs feature, MCP settings), Crawl4AI (open-source web crawler and data extractor), Figma REST API (get file endpoint), gitingest (gitingest.com, GitHub URL swap), GitHub (SDK repo, README)

## [Time to SWITCH… 20X your Claude Code Workflow](../videos/PRqHKpTHQVE.md)
`PRqHKpTHQVE` · AI LABS · 2025-11-02 · q2 · intro · review · topics: coding-agents, models-research, claude-code

AI LABS compares Claude Opus 4.1 with Opus 4 inside Claude Code on two single-run builds (a Pac-Man game and a ShadCN/Framer Motion site); the 4.1 gains look real but the evidence is anecdotal.

- Techniques: Identical-prompt A/B across model versions; Requirement checklist for generated UI; Model upgrade inside Claude Code; API model-name swap
- Tools: Claude Code, Claude Opus 4.1, Claude Opus 4, Claude Sonnet 3.7, Claude Sonnet 4, shadcn/ui, Framer Motion, SWE-bench Verified

## [3 Simple Ways To EARN Money With Claude Code Apps](../videos/Y2oK0nubq9A.md)
`Y2oK0nubq9A` · AI LABS · 2025-11-02 · q2 · intro · review · topics: product-ux, vibe-coding-app-building, claude-code

Walkthrough of consumer-app paywall patterns (instant-value previews, habit hooks, usage caps, tier ladders) plus a Claude Code design-command workflow for cloning paywall screens. Middle segment is sponsored.

- Techniques: Progress-gated free tier for education apps; Anchored yearly pricing; Progress hook with time or feature gating; Usage cap at point of need; Three-tier ladder with a highlighted middle; Slash-command design pass for prototypes; Screenshot-to-clone reference
- Tools: Claude Code, Cursor, VS Code, SuperDesign, design.md (prompt file), Flowbite, Paywall Screens, Make, HabitKit, Sleep Cycle, Babbel, CapCut

## [How Claude Solved AI's Biggest Problem](../videos/Z9glbip8pZc.md)
`Z9glbip8pZc` · AI LABS · 2025-11-02 · q3 · intro · review · topics: claude-code, skills-self-improvement, mcp-and-tools, context-engineering

Walkthrough of Claude Skills: SKILL.md folders loaded on demand, how they differ from MCP, building one with skill-creator, and HTML visualization widgets. Mostly demo, with one sponsor segment.

- Techniques: Skill folder layout; Keep the description one line; push detail into referenced files; Install shared skills into Claude Code; Bootstrap a skill with skill-creator; Visualization widget skill
- Tools: Claude Skills, Claude Desktop app, Claude Code, skill-creator skill (Anthropic skills repo), MCP builder skill, MCP, Figma MCP server, Figma API, PDF Extractor skill, Algorithm art skill, Canvas design skill, Word, PDF, Excel and PowerPoint document skills

## [I Made MCP AI Agents That Automate Every App I Build.](../videos/23ykmgvaSmM.md)
`23ykmgvaSmM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: mcp-and-tools, coding-agents, vibe-coding-app-building

Tutorial on wrapping an existing FastAPI to-do app with the FastAPI MCP server so Cursor, Windsurf, Claude Desktop, or a Python MCP-client agent can call its endpoints as tools. Covers setup, tool naming, and a registration gotcha.

- Techniques: Expose a FastAPI app as MCP tools; Name MCP tools with operation IDs; Register MCP after all endpoints are declared; Add the MCP server to an IDE client; Drive the MCP server from a custom Python agent
- Tools: FastAPI, fastapi-mcp (FastAPI MCP package), Next.js, Cursor, Windsurf, Claude Desktop, pip, uv, MCP use framework (Python MCP client library, name as spoken), mcp.json, config.json

## [Firecrawl MCP = Effortless Web Scraping](../videos/2GHRDoFquOo.md)
`2GHRDoFquOo` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: mcp-and-tools, vibe-coding-app-building, coding-agents

Tutorial on wiring the Firecrawl MCP server into Cursor so an agent can scrape a live URL and generate a near-copy of a Notion landing page in Next.js. Shows setup and a single demo run, with the output's flaws called out.

- Techniques: Register Firecrawl MCP in Cursor; Name the MCP tool in the prompt and use agent mode; Scrape, then generate by component; Pick scrape vs extract by goal
- Tools: Firecrawl MCP server (scrape and extract tools, npx command, API key), Cursor (agent mode, MCP settings), Windsurf (same MCP config pattern, mentioned as an alternative), Claude 3.7 Sonnet (model selected in Cursor), Next.js (blank starter app used as the target), Notion landing page (the site being cloned)

## [Turn Cursor AI into the 500$ Devin (Just Paste this...)](../videos/wJk2_Ds-9cM.md)
`wJk2_Ds-9cM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: coding-agents, context-engineering, skills-self-improvement

Walkthrough of a Cursor rules file that adds a lessons log and task scratchpad, used to build a full-stack Trello clone; one anecdotal demo with overstated "Devin" framing.

- Techniques: Per-project .cursor rules file; Lesson log inside the rules file; Scratchpad task plan with checkboxes and a current-focus section; Generate the rules prompt with another model, then run it in the IDE agent
- Tools: Cursor, Cursor Composer, Windsurf, Devin, GPT (used to write the prompt), PostgreSQL, Docker, OpenAI API (gpt-4 model name), Trello (clone target, not a tool used)

## [This Designer is INSANE... The Ultimate UI Setup](../videos/uayt-IVbh8E.md)
`uayt-IVbh8E` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: coding-agents, multi-agent, vibe-coding-app-building, context-engineering

Walkthrough of a Claude Code sub-agent pipeline for UI work: a UX agent drafts layout from requirements, a UI agent applies color variants, and a converter agent ports the HTML to SwiftUI.

- Techniques: Stage-separated UI sub-agent pipeline; Explicit agent count for variants; Split HTML output into HTML, CSS and JS files; Keep emoji placeholders, then fix icons in the target platform; Doc-grounded conversion guide via Context7, then bake into the agent
- Tools: Claude Code (sub-agents defined as markdown files), Cursor (mentioned in the intro as an AI coding tool, not used in the walkthrough), Context7 MCP, SwiftUI, iOS Simulator, HTML / CSS / JavaScript

## [How to use Reasoning Models Correctly?](../videos/w42_sbxa08w.md)
`w42_sbxa08w` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: context-engineering, models-research, multi-agent

Walkthrough of OpenAI's Reasoning Best Practices doc: keep prompts direct, skip chain-of-thought instructions, use delimiters, go zero-shot first, and use reasoning models as planners with cheaper models executing.

- Techniques: Section the prompt into Context / Examples / Instructions; Drop chain-of-thought scaffolding; Zero-shot first, then few-shot; Explicit constraints plus goal; Re-enable markdown in developer message (API); Planner/workhorse agent split
- Tools: OpenAI Reasoning Best Practices documentation, o1, o3-mini, GPT-4o, GPT-4o mini, Claude, Gemini, DeepSeek

## [Using this will make your AI AGENTS EVEN SMARTER!](../videos/2G-xavWw1bY.md)
`2G-xavWw1bY` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: context-engineering, rag-retrieval, token-cost-efficiency

A 5-minute tip for loading a whole GitHub repo into an LLM, either through a chat tool or a repo-to-text converter (gitingest), to answer questions and find install steps.

- Techniques: Repo URL swap into a chat-with-repo tool; gitingest repo-to-text conversion; Pick the model by token count; Explicit completeness prompting; Iterative setup questions on an ingested repo
- Tools: gitingest (named 'git ingest' in the transcript), DeepSeek (model, transcribed as 'DeepSeq'), Gemini (model), Cursor IDE, Claude (install instructions in the repo), GitHub, MCP server (example repo, unnamed)

## [Before You CHOOSE, Watch This Cursor vs Windsurf Face-Off!](../videos/0Ttn6dqnuQk.md)
`0Ttn6dqnuQk` · AI LABS · 2025-11-02 · q2 · intro · review · topics: coding-agents, vibe-coding-app-building, token-cost-efficiency

A short, single-run head-to-head of Cursor and Windsurf on a CLI task app, a web music player and pricing, with a verdict favoring Windsurf.

- Techniques: Same-prompt bake-off with explicit pass criteria; Scope check with a deliberately simple app; Trial and plan comparison before buying
- Tools: Cursor (Composer, agent panel), Windsurf (Cascade, image upload, explain-and-fix), ElevenLabs (voiceover audio used in the music-player test), tasks.json (file created by the CLI test)

## [3 More Ways To ACTUALLY Build Beautiful Websites with Cursor IDE](../videos/U1_nzjWUpL4.md)
`U1_nzjWUpL4` · AI LABS · 2025-11-02 · q3 · intro · tutorial · topics: vibe-coding-app-building, coding-agents, mcp-and-tools, context-engineering

Three practical ways to turn website designs into working Next.js UI in Cursor: a structured front-end spec prompt, a design.json built from screenshots, Browser MCP for cloning structure, and stagewise for precise element-level edits.

- Techniques: Structured front-end spec prompt; Screenshot to design.json style profile; Clone a site's structure with Browser MCP; Element-level UI edits with stagewise
- Tools: Cursor, Claude, ChatGPT, Claude Code, Next.js, Tailwind CSS, Browser MCP, stagewise, mcp.json, design.json

## [Build Apps with Cursor Like the 1% Using This NEW Method](../videos/OZaxtm3RyCw.md)
`OZaxtm3RyCw` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · topics: coding-agents, context-engineering, agent-architecture

Walkthrough of building a wallpaper app in Cursor with Taskmaster AI: the PRD becomes a dependency-ordered task list the agent works through one task at a time, so one chat holds the whole build.

- Techniques: Install and initialize Taskmaster globally, then init per project; Configure keys in .env; Brainstorm with a no-edit instruction; Generate the PRD from an example template; Parse the PRD into tasks, then work them sequentially; Handle implementation drift with an explicit change list; Work in the correct subdirectory
- Tools: Cursor, Taskmaster AI, Claude (Anthropic API), Perplexity API, Unsplash API, Next.js

## [Trae AI: The New Cursor AI Alternative](../videos/cdLnorNbewA.md)
`cdLnorNbewA` · AI LABS · 2025-11-02 · q2 · intro · review · topics: coding-agents, vibe-coding-app-building, testing-verification

Hands-on test of Trae, ByteDance's VS Code-fork IDE with a single-agent workflow and free Claude access; a to-do app and a Spotify screenshot clone show a basic UI with missing-config errors, verdict "hype".

- Techniques: Screenshot-to-app clone prompt; Built-in web view preview; Manual behavioural check of agent output; Config-first debugging for missing styles
- Tools: Trae (ByteDance IDE), Claude 3.5 Sonnet, GPT-4.0 (mentioned as promised, not available), Cursor, Windsurf, VS Code, React, Tailwind CSS, PostCSS

## [Generate Multiple Cursor Rules with ONE CLICK!](../videos/ztT6Bu1MPpY.md)
`ztT6Bu1MPpY` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: coding-agents, context-engineering

Short tutorial on using Cursor Directory's generate-project-rules feature to turn package.json or requirements.txt into Cursor .rules files, with a UI demo and no evaluation of rule quality.

- Techniques: Generate project rules from dependency manifests; Generate rules per manifest in polyglot repos
- Tools: Cursor, Cursor Directory, Grok (named by the speaker as the generation model), Next.js, React, TypeScript, Tailwind CSS, FastAPI, SQLAlchemy, Obsidian (markdown MCP server example), MCP servers

## [Claude Code Tutorial: Full Setup, MCP, and Cursor AI Integration (Claude Squad Guide)](../videos/u-GGktUnSgg.md)
`u-GGktUnSgg` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: claude-code, coding-agents, multi-agent

Tutorial on running Claude Code inside Cursor and installing Claude Squad to run several Claude Code instances in tmux; the IDE link fails on camera and the MCP in the title is never covered.

- Techniques: Install Claude Code and open it in Cursor; Check the IDE connection from Claude Code; Install Claude Squad; Prepare a repository for Claude Squad; Run parallel sessions for front end and back end; One-shot build prompt that yields a to-do list
- Tools: Claude Code, Cursor, Claude Code extension for Cursor, Claude Squad (cs), tmux, GitHub CLI (gh), git, GitHub, OpenAI Codex, Claude Opus, Claude Max plan, Claude Pro plan

## [Coding Test: Can CLAUDE COMPUTER USE Build Apps?](../videos/XbL5nzTLtag.md)
`XbL5nzTLtag` · AI LABS · 2025-11-02 · q2 · intro · review · topics: coding-agents, voice-multimodal, context-engineering

A short hands-on test of Claude Computer Use building a budget-manager app: it handled terminal setup but failed at front-end code generation, and a page refresh wiped the project.

- Techniques: Staged prompt decomposition for agent app builds; Verify toolchain installs in the agent's terminal; Keep recoverable copies of agent-generated work outside the agent's UI
- Tools: Claude Computer Use API, Claude (Claude 3.5 mentioned as the comparison model), ChatGPT (used to write and split the build prompt), Node.js, npm

## [Connect any LLM to any MCP server without any MCP client.](../videos/QZ6AreMxMKA.md)
`QZ6AreMxMKA` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: mcp-and-tools, agent-architecture, coding-agents

A beginner walkthrough of a Python MCP client library that runs an agent over any LLM and any MCP server, so no desktop client is needed. Shows setup, a single-file Airbnb example, multi-server config and Cursor tips.

- Techniques: Provider-agnostic MCP agent from a config file; Cap agent steps and filter results in the prompt; Multi-server config with a service manager; Give a coding assistant the library docs; Flatten a repo for LLM questions (gitingest)
- Tools: MCP (Model Context Protocol), Python, pip3, LangChain, LangChain OpenAI integration, LangChain Anthropic integration, OpenAI, Anthropic, Cursor, Windsurf, Claude Desktop, Airbnb MCP server

## [Claude Code Is an MCP Now?...3 CRAZY Things You Never Saw Coming](../videos/diTuQaSJ3nI.md)
`diTuQaSJ3nI` · AI LABS · 2025-11-02 · q3 · practitioner · review · topics: claude-code, mcp-and-tools, multi-agent, token-cost-efficiency

Community tools that extend Claude Code: calling it as an MCP server from Cursor, routing it to other models (Kimi K2 via OpenRouter), a multi-agent "hive mind" mode, and a dedicated Claude Code Chat extension.

- Techniques: Expose Claude Code as an MCP server and call it from another client; Canvas-to-code handoff from Claude Desktop; Route Claude Code to OpenRouter models with Claude Code Router; Hive mind multi-agent sessions in Claude Flow; Dedicated Claude Code Chat window in the editor
- Tools: Claude Code, Claude Code SDK, Claude Code MCP server (community wrapper, unnamed in video), Claude Code Router (ccr), Cursor, Claude Desktop, Claude 3, OpenRouter, Kimi K2, Gemini, OpenAI models, DeepSeek

## [3 Things I Wish I Knew Before using Claude Code](../videos/_9T-6dw-CZs.md)
`_9T-6dw-CZs` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: claude-code, mcp-and-tools, coding-agents, context-engineering

A beginner-level walkthrough of five Claude Code features: custom slash commands, Cursor integration with multi-line input, adding MCP servers (Sentry example), plan mode with CLAUDE.md, and the "ultrathink" keyword.

- Techniques: Custom slash command as a prompt file; Claude Code inside Cursor; Add an MCP server from an existing Cursor or Windsurf JSON config; Use MCP server commands from slash commands; Plan first, then save rules to CLAUDE.md; Add 'ultrathink' to a prompt for hard problems
- Tools: Claude Code, Cursor, Windsurf, Sentry, Sentry MCP server, Seer (Sentry AI agent), Claude Agent SDK, Claude GitHub app

## [This New MCP Client Lets You Integrate So Many MCP Servers!!](../videos/xEyKT5iY0W0.md)
`xEyKT5iY0W0` · AI LABS · 2025-11-02 · q2 · intro · review · topics: mcp-and-tools, security-guardrails

Walkthrough of an open-source general-purpose MCP client that runs an agent over MCP servers outside coding IDEs, using Composio-hosted servers with agent-driven auth; the local install is slow.

- Techniques: Adding a remote MCP server to a generic client; Agent-driven auth for hosted MCP servers; Running the open client locally
- Tools: Open MCP client (open-source MCP client app, hosted on Vercel, source on GitHub), Composio (composio.dev, hosted MCP server catalog with auth), Google Tasks MCP server, Hacker News MCP server, Gmail MCP server, Google Drive MCP server, Notion MCP server, Google Meet MCP server, Cursor, Windsurf, LangSmith, OpenAI models

## [Replits NEW AI Agents Are INSANE](../videos/v1jLYiW0AWc.md)
`v1jLYiW0AWc` · AI LABS · 2025-11-02 · q3 · intro · review · topics: product-ux, vibe-coding-app-building, mcp-and-tools

Hands-on beta test of Replit Agent 3's Agents and Automations builder: guided setup via Slack, Telegram or scheduled triggers, OAuth connectors, and automatic app testing, with real gaps in memory, integrations and Slack deployment.

- Techniques: Least-privilege Notion OAuth; Test memory after deployment; Ask the agent to explain a missing action; Telegram publishing setup; Verify side effects end to end
- Tools: Replit Agent 3, Replit Agents and Automations, Replit app testing, Replit Stripe integration, OpenAI API, Notion (connector), Outlook (connector), OneDrive (connector), Spotify (connector), Linear (connector), Slack (connector and deployment target), Telegram (deployment target)

## [DeepSeek R1 Lite: Open-Source AI That Might Beat OpenAI O1?](../videos/Kr3zaxX8-g4.md)
`Kr3zaxX8-g4` · AI LABS · 2025-11-02 · q2 · intro · review · topics: models-research, evals

Hands-on check of DeepSeek R1 Lite Preview's web demo on seven prompts (code, SVG, math, summarizing, pseudocode); six pass, one fails. Anecdotal, with no methodology.

- Techniques: Manual pass/fail test tracker; Run generated artifacts in their real runtime; Repeat a nondeterministic run; Check the reasoning stream against a known answer; Cross-model verification with no ground truth
- Tools: DeepSeek R1 Lite Preview (web demo, deep-think toggle), OpenAI o1-preview (comparison only), Claude 3.5 Sonnet (comparison only), Notion (test tracker), VS Code (running generated Python and HTML), SVG viewer (unnamed), Other LLMs (pseudocode cross-check, unnamed)

## [I Found a Tool That Breaks MCP (In a Good Way)](../videos/6R7CoIKKkDE.md)
`6R7CoIKKkDE` · AI LABS · 2025-11-02 · q2 · intro · review · topics: vibe-coding-app-building, mcp-and-tools

Tempo Labs' MCP app store packages third-party APIs as MCP servers with docs built in; the host builds an ElevenLabs quotes app by installing integrations and prompting. Promotional, single happy-path demo.

- Techniques: Connect the backend before the integrations; Install an integration from the MCP app store; PRD and user flow as the build spec; Describe the full behavior in one feature prompt; Add error logging before debugging a broken integration
- Tools: Tempo (Tempo Labs app builder, with its MCP app store), Model Context Protocol (MCP), Supabase, Firecrawl, ElevenLabs (Eleven Labs API), Google Gemini, OpenAI, Anthropic (auto-caption reads 'Tropic'), Next.js (starter template kit), shadcn/ui (auto-caption reads 'Shadzian'), Mermaid, React

## [Cursor AI Shotgun Code (FREE): Fix Any Next.js App with AI (Full Tutorial)](../videos/4A66bMRiPQ0.md)
`4A66bMRiPQ0` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: context-engineering, coding-agents, vibe-coding-app-building

A walkthrough of Shotgun Code, which packs a whole Next.js repo into one prompt, gets a full diff from Gemini 2.5 Pro, and applies it in Cursor to overhaul a personal app.

- Techniques: Setup and launch from repo root; Curate the context before generating the prompt; Write one task plus custom rules into the packed prompt; Generate the diff in Google AI Studio; Apply the diff with a coding agent in chunks; Control visual style through the task text
- Tools: Shotgun Code (the GitHub repo demoed, a Go app with a frontend), Go, Node.js, Wails CLI (captioned as 'Wales'), Next.js, Google AI Studio, Gemini 2.5 Pro, Gemini Flash (mentioned as the option not to use), Cursor, Windsurf (mentioned as an alternative executor), Claude 3.5 Sonnet, shadcn/ui (captioned as 'shad cn')

## [Vibe Coding Debugging: The Only Tutorial You Need for 10X Fast Debugging](../videos/2h8WSChA1-o.md)
`2h8WSChA1-o` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: observability, mcp-and-tools, coding-agents

A Sentry MCP walkthrough: an agent in Cursor creates a Sentry project, installs the Next.js SDK, wires the DSN, triggers test errors, then reads an issue's trace and proposes a fix. Vendor-led, with a paid SEER feature.

- Techniques: Let the agent provision Sentry through the MCP; Install the Sentry MCP into a client; Debug an error from its issue data, not the raw code; Set a verification step after the agent wires monitoring
- Tools: Sentry, Sentry MCP server, Sentry SDK, Next.js, Python SDK, Cursor, Claude Code, SEER, mcp.json

## [Claude Engineer is INSANE... Upgrade Your Claude Code Workflow](../videos/6Rg5M69bMgQ.md)
`6Rg5M69bMgQ` · AI LABS · 2025-11-02 · q2 · intro · review · topics: claude-code, context-engineering, coding-agents, mcp-and-tools

A walkthrough of two free add-ons for Claude Code: the SuperClaude configuration framework (slash commands, flags, personas, MCP-wired workflows) and a basic browser web UI for reaching Claude Code from other devices on the LAN.

- Techniques: Install SuperClaude from its GitHub repo; Have an AI write a usage guide from the framework's own config; Turn a phase into a runnable slash command plus prompt; Wire MCPs yourself, then reference them through flags; Reach Claude Code from a phone on the same LAN
- Tools: SuperClaude (configuration framework for Claude Code; no version stated), Claude Code, Cursor (used to read config and generate docs.md), Context7 MCP, Sequential MCP, Magic UI MCP, Puppeteer MCP, React, Next.js (spoken as 'xjs'), ElevenLabs API, OpenAI API, Warp (terminal, used to get the LAN IP)

## [Wait.. Claude Code is MADE Slow on Purpose? Heres How to Fix It](../videos/wYWyJNs1HVk.md)
`wYWyJNs1HVk` · AI LABS · 2025-11-02 · q2 · intro · review · topics: claude-code, context-engineering, mcp-and-tools, token-cost-efficiency

Walkthrough of installing the Serena MCP (semantic code retrieval over a project index) and a Claude Code usage monitor, to keep Claude's context window focused and token use lower; the title's "made slow on purpose" claim is not supported in the video.

- Techniques: Per-project Serena MCP install; Index the project before using Serena; Prime Claude with Serena's instructions; Use the Serena dashboard for logs and clean shutdown; Track plan-window usage in a terminal tab
- Tools: Serena (MCP server for semantic code retrieval and indexing), Context7 (MCP for up-to-date library documentation), Claude Code, Cursor, Windsurf, uv (Python package runner used to install Serena), Claude Code usage monitor (terminal tool; name not stated in the transcript), Next.js, Python, Claudia and the Claude Code web UI (mentioned as alternatives)

## [Codeium Windsurf: The Full-Stack App Builder | Better Than Cursor?](../videos/Wvyc2E6OHm8.md)
`Wvyc2E6OHm8` · AI LABS · 2025-11-02 · q2 · intro · review · topics: vibe-coding-app-building, coding-agents

A feature tour of Windsurf's Cascade and Flows agent features, comparing it with Cursor and building a 2048 game and a Splitwise clone from single prompts. Useful as a demo of full-stack generation, thin on technical depth.

- Techniques: Start from an example project in Cascade; Iterative follow-up prompt, then review with OpenDiff; Name-based full-stack build prompt; Paste raw errors back into the agent; Flows for multi-step tasks with context kept
- Tools: Windsurf (Codeium editor), Cascade, Flows, Cursor, Cursor Composer, GitHub Copilot, VS Code, Bootstrap 5, Claude models (named as available on Windsurf Pro, no version given), GPT-4 (named, no version given), OpenDiff

## [People Are Getting RICH With AI Mobile Apps – Let’s Build One](../videos/HQJUvSLO91o.md)
`HQJUvSLO91o` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: vibe-coding-app-building, coding-agents, context-engineering

A walkthrough of building a macOS menu-bar Swift app by prompting Windsurf with a docs-first template and Gemini 2.5, after Claude failed on the same prompt; mostly process, with the prompt itself left in the video description.

- Techniques: Docs-first agent prompt for a new app; Scaffold the native project and place it in the agent workspace; Relay errors as text, and switch models for visual bugs; Turbo mode for unattended builds; Export a standalone macOS app from Xcode
- Tools: Windsurf, Cursor, Gemini 2.5, Claude 3.7, Claude, ChatGPT, Xcode, Swift, SwiftUI, Taskmaster (mentioned, as needing Claude and Perplexity API keys), Perplexity API (mentioned), Next.js (analogy only)

## [Context7 MCP Tutorial: Get Instant RAG for Your AI Coders](../videos/323l56VqJQw.md)
`323l56VqJQw` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: mcp-and-tools, coding-agents, context-engineering

Tutorial on wiring the Context7 MCP server into Cursor so the agent pulls current, targeted library docs instead of stale training data or whole doc files; the evidence is one informal before/after build.

- Techniques: Add Context7 as an MCP server in Cursor; Recover missing MCP tools; Pull targeted doc sections instead of attaching whole docs; Keep API keys out of agent context
- Tools: Cursor, Context7 MCP server (context7.com), mcp-use (auto-caption 'mcpus'; the Python agent framework built in the demo), Playwright MCP, Claude 3.7 (model named by the speaker), shadcn/ui (example library), Next.js (example framework), Windsurf, VS Code with GitHub Copilot agent, .cursorignore

## [Supabase MCP Cursor Integration (Step by Step)](../videos/b_hr1TB2GYQ.md)
`b_hr1TB2GYQ` · AI LABS · 2025-11-02 · q3 · intro · tutorial · topics: mcp-and-tools, coding-agents, context-engineering

Step-by-step setup of Supabase's MCP server in Cursor so the agent can see the live database schema, with a connection-string walkthrough and a bash-wrapper trick. Anecdotal, short, and light on verification data.

- Techniques: Add Supabase MCP to Cursor via the command type; Wrap the MCP command in a bash script; Make the agent verify schema before and after each DB step
- Tools: Supabase, Supabase MCP server, Supabase CLI (`supabase status`, local instances), Cursor, Windsurf, Claude Desktop, GitHub MCP server, bash

## [Integrate Cursor/Windsurf into Apple Ecosystem with This Cursor MCP Setup!](../videos/htbzu9s189E.md)
`htbzu9s189E` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: mcp-and-tools, coding-agents

Walkthrough of connecting the open-source apple-mcp server to Cursor so an agent can read and act on Apple Contacts, Notes, Messages and Reminders; mostly setup steps, with a useful note on restructuring a tool's navigation.

- Techniques: Register a local MCP server in Cursor; Get the absolute entry path for an MCP server; Use agent mode to call MCP tools; Extend an MCP server by having the agent copy existing modules; Restructure a search-everything tool into hierarchical navigation
- Tools: Cursor, apple-mcp (GitHub repo, MCP server for Apple apps), Claude Desktop, Windsurf, Docker MCP server (already added in Cursor, unrelated to the Apple setup), Claude 3.5 Sonnet, GPT-4, bun, realpath, Apple Notes, Apple Contacts, Apple Messages

## [Phi-4: The Smallest Open Source AI Model](../videos/yzSYIndCWD8.md)
`yzSYIndCWD8` · AI LABS · 2025-11-02 · q2 · intro · review · topics: local-ai, coding-agents, vibe-coding-app-building

Single-run hands-on test of Phi-4 (14B, MIT license) through Ollama, bolt.diy and Cline. It runs locally, but it failed to integrate a React component, which the speaker blames on the context window.

- Techniques: Local model via Ollama; OpenRouter key as a hosted fallback; bolt.diy from source; Point Cline at local Ollama; Frontier model writes, local model integrates; Shrink the task when the agent stalls
- Tools: Phi-4 (Microsoft, 14B open weights, MIT license; captioned as "5.4"), Ollama, OpenRouter, bolt.diy (captioned "BoltDIY" and "bold.diy"), Cline (captioned "Klein"; formerly Claude Dev), Claude (used to write the card component), VS Code, pnpm, Next.js 14, React, TypeScript, Tailwind CSS

## [How I Build Apps 10x Faster with this 7-Step Cursor Workflow](../videos/cAFIUiE_8DM.md)
`cAFIUiE_8DM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: coding-agents, vibe-coding-app-building, context-engineering

A solo builder walks through a seven-step AI app workflow (idea, MVP, HTML prototype, design.json styling, SwiftUI conversion, Supabase backend, UI polish) for an iOS habit app, using Cursor and Claude Code.

- Techniques: Stage-gated AI app build; Screenshot-driven correction loop; design.json from a reference image; Rules-file-driven framework conversion; MCP-based backend provisioning; Image model for app icon iteration; Model switching by task
- Tools: Cursor, Claude Code, Claude (chat), ChatGPT, OpenAI image generation model, Supabase, Supabase MCP server, Supabase SDK, SwiftUI, Swift, Xcode, Next.js (mentioned as an example template)

## [OpenAI O3-Mini: The Fastest Reasoning Model Yet?](../videos/cdYA5QV8gRY.md)
`cdYA5QV8gRY` · AI LABS · 2025-11-02 · q2 · intro · review · topics: models-research, coding-agents, evals

Quick anecdotal test of OpenAI's o3-mini and o3-mini-high: the speaker reports correct answers on six reasoning prompts, far faster than o1, plus a Chrome extension built with o3-mini-high.

- Techniques: Latency-first spot check of a reasoning model; Pick the lower reasoning tier when the task is simple; One-shot scaffold for a small browser extension
- Tools: o3-mini, o3-mini-high, o1, ChatGPT, Chrome extension, Cursor, Windsurf

## [This n8n mcp is INSANE... Let AI Create your Entire Automation](../videos/xf2i6Acs1mI.md)
`xf2i6Acs1mI` · AI LABS · 2025-11-02 · q2 · intro · review · topics: mcp-and-tools, vibe-coding-app-building

A walkthrough of an n8n MCP server that lets Claude or Cursor research n8n nodes, build a workflow JSON, validate it and push it into an n8n workspace, shown with a deep-search agent demo and setup steps.

- Techniques: Register the n8n MCP in Claude Desktop; Register the n8n MCP in Cursor; Enforce tool-call order with a rulebook; Full management mode: API key and URL; Deep-search agent pattern in n8n
- Tools: n8n, n8n MCP server, Claude (Desktop, Projects, Artifacts), Claude Code, Cursor, Docker, npx, OpenAI API, SERP API, DuckDuckGo search node, Wikipedia search node, Reddit search node

## [Warp Code Tutorial: Save 90% of Time with Warp AI Agents (vs Claude Code) Agentic Development](../videos/STd07QswCpk.md)
`STd07QswCpk` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: coding-agents, context-engineering, multi-agent, mcp-and-tools

Sponsored walkthrough of building a full-stack notes app with Warp's agentic development environment, covering PRD planning, parallel agents split by API contract, saved prompts and rules, and MCP context.

- Techniques: PRD-first, then API contract, then fan out; Saved prompts as reusable commands; Templated workflows for known-hard setup steps; Rules to pin dependency and library behavior; Notebooks as context documents; Explicit task list for long runs; Parallel agent tabs with completion monitoring
- Tools: Warp (agentic development environment and terminal, with a built-in AI agent), Warp Drive (saved prompts, rules, MCP servers, workflows, notebooks), Context7 MCP, Playwright MCP, ChatGPT, Express Validator, Zod, Next.js, SWE-bench (vendor claim: 75.8%), Terminal Bench (vendor claim: #1)

## [Connect to Anything with This Cursor MCP Setup](../videos/brhs5DogIf8.md)
`brhs5DogIf8` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: mcp-and-tools, coding-agents

Walkthrough of adding community MCP servers to Cursor as stdio commands (Docker, YouTube summarizer), with a YOLO-mode caveat; mostly screen-recorded clicks, thin on specifics.

- Techniques: Add a stdio MCP server in Cursor; Verify tool access with a small agent-mode task; Use YOLO mode only with monitoring; Summarize a YouTube video through MCP
- Tools: Cursor, Model Context Protocol (MCP), Claude Desktop app, Claude, Composer (Cursor agent), uvx, Docker MCP server, Jira MCP server, Spotify MCP server, Shopify MCP server, YouTube MCP server, yt-dlp

## [Claude code vs Codex vs Cursor: Who gets the cake?](../videos/_Xbe7MQ2NxI.md)
`_Xbe7MQ2NxI` · AI LABS · 2025-11-02 · q2 · intro · review · topics: claude-code, coding-agents, mcp-and-tools, agent-architecture

Argues Claude Code and other AI CLIs are "portable agent engines": terminal agents can call each other via bash, run headless (-p), deploy to GitHub Actions and act as MCP servers. Opinion-heavy, with a sponsor segment.

- Techniques: Headless single-shot invocation; Cross-agent delegation through bash; Scheduled agent via GitHub Actions; Claude Code GitHub app for PR review; Mixed local and remote MCP servers
- Tools: Claude Code, Claude Code GitHub app, Claude Code for Chrome, Claude for Excel, Agent SDK (formerly Claude Code SDK), Codex CLI, Gemini CLI, Qwen Code (transcript: QuenCode), Cursor CLI, gitingest, GitHub Actions, Slack

## [Here Is How to Vibe Code Large Scale Projects](../videos/k9fPAzS5_Kw.md)
`k9fPAzS5_Kw` · AI LABS · 2025-11-02 · q3 · intro · tutorial · topics: coding-agents, context-engineering, vibe-coding-app-building

AI LABS walkthrough of Plandex, a self-hosted CLI coding agent aimed at large projects: local Docker setup, chat-then-tell workflow, reviewable sandboxed changes, and one Swift app demo. Context-size claims are unverified.

- Techniques: Self-host Plandex in local mode; Set keys and initialize a repo; Chat to brainstorm and understand, then tell to implement; Review before applying, and debug failed commands
- Tools: Plandex, Docker, OpenRouter API, OpenAI API, Tree-sitter, Cursor, Xcode, Swift, SwiftUI, Gemini 2.5

## [This MCP Setup is the Best Way to Add 3D Models to Your Frontend](../videos/srsst0L51RE.md)
`srsst0L51RE` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: mcp-and-tools, coding-agents, vibe-coding-app-building

Short tutorial on connecting the Sketchfab MCP server to Cursor so an agent can search, download and place a 3D model into a Three.js landing page from one prompt.

- Techniques: Install the Sketchfab MCP server from source; Get a Sketchfab API token; Get the absolute path to the built server entry point; Register the server in Cursor via mcp.json; Prompt for a 3D hero section and iterate on the model
- Tools: Sketchfab MCP server (community server listed on mcp.so), Sketchfab, Cursor, Windsurf, Claude Desktop, Three.js (3JS), git, npm, Claude 3.7 (mentioned for 3D game generation)

## [Traycer is INSANE… Cursor AI is Not Enough Anymore](../videos/0hAS1xCeixQ.md)
`0hAS1xCeixQ` · AI LABS · 2025-11-02 · q2 · intro · review · topics: coding-agents, context-engineering, testing-verification

A product walkthrough of Traycer, an IDE extension that runs a planning stage (gap-filling questions, phased plan), implementation, and a self-review pass before or alongside coding agents such as Claude Code and Cursor.

- Techniques: Clarify-before-plan requirements file; Phased plan as the unit of execution; Plan handoff to a coding agent; Severity-classed self-review pass; Change tracking with M/N badges; Version-conflict repair by dependency pinning
- Tools: Traycer (IDE extension, sign-up required), Next.js, TypeScript, Tailwind CSS (v3 before the intentional upgrade), HeroUI (named as Hero UI), NextUI (mentioned as the wrong provider), shadcn (mentioned as a common library), Claude Code, Cursor

## [Develop Faster using the browser tools MCP Cursor/Windsurf.](../videos/G25UyWfYogQ.md)
`G25UyWfYogQ` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · topics: mcp-and-tools, coding-agents, testing-verification

Walkthrough of the browser-tools MCP server, which lets Cursor's agent run accessibility/SEO/performance audits, read screenshots and selected DOM elements from Chrome, and iterate on front-end fixes.

- Techniques: Install browser-tools MCP into Cursor; Load the Chrome extension and start the connector; Accessibility audit and fix loop; Configure screenshot folder and auto-paste; Select-element targeting; Voice mode for prompting
- Tools: browser-tools MCP server (browser-tools-mcp, GitHub repo linked in the description), Cursor (IDE and agent), Windsurf (mentioned for its select-element feature), Chrome browser extension (browser-tools), Chrome DevTools (Browser Tools MCP tab for settings and screenshot folder), mcp.json (Cursor MCP config file), React (demo app's calendar component)

## [Bash Apps Are INSANE… A New Way To Use Claude Code](../videos/1_twhMU9AxM.md)
`1_twhMU9AxM` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · topics: claude-code, coding-agents, context-engineering

Wrap any terminal CLI as a Claude Code agent via CLAUDE.md; builds a Git Agent on GitIngest and Click that stores repo context in the repo. Practical pattern, light on code.

- Techniques: Document a CLI as an agent tool in CLAUDE.md; Token-size gate before repo extraction; Persist extractions and analyses as repo files; Wrap an existing CLI in a Click command group; PRD-first build loop with Claude Code
- Tools: Claude Code, Claude Desktop, Cursor, GalleryDL, aria2, GitIngest (git ingest, open-source CLI with a GitHub URL mode), Git Agent (the speaker's own CLI wrapper, not released in the transcript), BMAD method (framework mentioned as a past featured video, not demoed), Click (Python CLI framework; auto-captions say Qlik), CLAUDE.md, ScaleKit (sponsor; OAuth and auth layer for AI apps)

## [Google's New AI Code Editor Built My Flutter App in the Browser!"](../videos/P4xA6j3B39U.md)
`P4xA6j3B39U` · AI LABS · 2025-11-02 · q2 · intro · review · topics: coding-agents, vibe-coding-app-building

Hands-on review of Google's browser-based Project IDX: the host builds a Flutter task-manager app with its Gemini chat, and reports that fixes needed repeated prompting and manual insertion.

- Techniques: Full-file repair loop; Explicit insert prompt; Observable-symptom prompt; Review diff before applying; Setup steps for the browser IDE
- Tools: Project IDX, Gemini, Flutter, VS Code, Cursor, Windsurf, Expo, Next.js, Python, Go, Node.js

## [Why Isn't Anyone Talking About This Vibe Coding Tool?](../videos/BXBwikXMb6Q.md)
`BXBwikXMb6Q` · AI LABS · 2025-11-02 · q2 · intro · review · topics: vibe-coding-app-building, dev-tools

A walkthrough of Convex's Chef, a prompt-to-full-stack-app builder, using it to make a Splitwise clone and a tool-rental app; the main takeaways are that prompt detail up front matters and that text-only prompting is a real limitation.

- Techniques: Front-load a comprehensive prompt; Bring your own API key when quota runs out, then re-prompt; Start from a preset and adjust the prompt; Verify by walking through the core flows; Export and run locally
- Tools: Chef (Convex's AI app builder), Convex, Lovable, Supabase, Bolt.new, v0 (Vercel), ChatGPT, Anthropic API (Claude), React, TypeScript

## [GitHub MCP Server: Let AI Handle Your GitHub](../videos/TrDW2Puhw0Y.md)
`TrDW2Puhw0Y` · AI LABS · 2025-11-02 · q3 · intro · tutorial · topics: mcp-and-tools, coding-agents, dev-tools

Step-by-step setup of the GitHub MCP server in Cursor, then a live demo of an agent creating a repo, pushing a file, cloning and searching GitHub from the chat.

- Techniques: Wrap the GitHub token in a shell script for Cursor's MCP command; Create a GitHub classic personal access token for the MCP server; Register the script as a command-type MCP server in Cursor; Smoke-test the MCP connection with a read-only query
- Tools: GitHub MCP server (GitHub's official MCP server, run through npx), Cursor (IDE, agent mode, MCP settings), npx, bash, nano, realpath, GitHub classic personal access tokens, Claude Desktop (mentioned as the server's reference client), Archon (another creator's agent-building repo, mentioned in passing)

## [Anthropic Claude AI Agentic Browser: The Claude Chrome Extension for Builders (EXCLUSIVE DEMO)](../videos/TVetQbcgdMU.md)
`TVetQbcgdMU` · AI LABS · 2025-11-02 · q3 · practitioner · review · topics: coding-agents, testing-verification, voice-multimodal

Hands-on demo of Anthropic's Claude Chrome extension as a visual-testing partner for Claude Code: a slash command reviews each finished task on a running dev server, and the browser agent reports visual and functional issues.

- Techniques: Per-task visual review slash command; Fresh chat per task; Prioritized improvement triage before the next task; Batch review of several tasks; Per-site approval allowlist for browser actions
- Tools: Claude Code, Claude Chrome extension (Claude browser extension, research preview), Claude 4 series models, Next.js, GPT (used to brainstorm the app idea), BMAD method (mentioned, not used), Playwright MCP (compared, not used), Cursor (mentioned as a competitor)

## [I Built 5 Websites Without Touching HTML:  Here's How (Kibo UI)](../videos/6odlDS7-G8k.md)
`6odlDS7-G8k` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · topics: vibe-coding-app-building, mcp-and-tools, coding-agents, context-engineering

Tutorial on wiring the shadcn MCP server and a custom 1100-component Kibo UI registry into a coding agent, plus TweakCN's live-embed theming flow for building Next.js UIs.

- Techniques: Wire the shadcn MCP into a Next.js or React project; Host a custom component registry from shadcn's registry template; Category-guided component selection for very large catalogs; Two-command design-first workflow (init once, build per session); Embed a TweakCN live theme preview into a Next.js app
- Tools: shadcn, shadcn CLI, shadcn MCP server, shadcn registry template, Kibo UI (patterns registry, ~1100 components), TweakCN, TweakCN MCP server, Next.js, React, Claude Code, Cursor, components.json

## [OpenAI Codex Hacked: Use It with Gemini 2.5 PRO (The Best Coding Model)](../videos/e3yxrNoC7mc.md)
`e3yxrNoC7mc` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: coding-agents, context-engineering

Walkthrough of setting up a multi-provider fork of OpenAI's Codex CLI with Gemini 2.5 Pro, including config files and full-auto use, plus a failed full-scope attempt and a narrowed retry.

- Techniques: Swap the model behind a forked CLI agent; Persist per-project agent setup in files, not shell exports; Run the agent inside a git repo; Full-auto single-prompt build, then narrow scope on stall
- Tools: OpenAI Codex CLI, OpenCodex (community fork of Codex CLI, name as spoken in the video; exact package name not stated), npm, Gemini 2.5 Pro, Google AI Studio, Google Cloud, OpenRouter, Ollama, shadcn/ui, Next.js, Cursor (used as the editor to open config.json), git

## [SAVE Your 20$ by using Cursor AI for FREE!](../videos/Nm2Lhe0-6To.md)
`Nm2Lhe0-6To` · AI LABS · 2025-11-02 · q2 · intro · review · topics: mcp-and-tools, coding-agents, token-cost-efficiency

Walkthrough of Desktop Commander, a free MCP server that gives Claude Desktop file, terminal and edit tools, demoed by building a Next.js and FastAPI image editor from one prompt.

- Techniques: Replace an AI IDE with an MCP server in an existing chat client; One prompt with a target path and an objective; Search-and-replace edits instead of full-file rewrites; Read and change the MCP server's config through its own tools; Run-and-verify loop with bug reports in chat; Side-by-side IDE view with agent edits
- Tools: Desktop Commander MCP, Claude Desktop, File system MCP server, Claude Code, Cursor, Windsurf, VS Code, Cline (transcribed as 'Klein'), Roo Code (transcribed as 'RuCode'), Claude 3.7 Sonnet, Claude 3.5 Sonnet, Next.js

## [All My AI Apps Are Connected to One MIND — With Open Memory](../videos/Y2XI2nk44WE.md)
`Y2XI2nk44WE` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · topics: memory, mcp-and-tools

Tutorial on Open Memory, a self-hosted shared memory server that several MCP clients (Claude Desktop, Cursor) can read and write, with setup steps and the failure modes the host hit.

- Techniques: Run Open Memory locally; Install the MCP server via generated client commands; Ingest a whole plan as one memory add; End-of-session progress checkpoint; Scope retrieval with specific project wording; Store plain-text memories, not structure
- Tools: Open Memory (Mem0 repo), Mem0, Claude Desktop, Claude, Cursor, Docker, make, OpenAI API, MCP, Next.js, React, TypeScript

## [I've Been Using the n8n MCP WRONG - The Correct Workflow](../videos/jUfpYmN9q6Y.md)
`jUfpYmN9q6Y` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · topics: coding-agents, claude-code, context-engineering, mcp-and-tools

Driving the n8n MCP from Claude Code works better with a phased, file-based workflow: plan, research, build and validate in separate sessions, delete-and-recreate on update, and OAuth instead of API keys.

- Techniques: Phased file-based workflow pipeline; Clear context between phases; Put standing rules in CLAUDE.md; Pre-build version and health check; Delete-and-recreate instead of in-place update; OAuth-first credentials; Single-node isolation debugging; Documentation re-check prompt
- Tools: n8n, n8n MCP server, Claude Code, Claude Desktop, Claude.md (CLAUDE.md), OpenAI node in n8n, Google Calendar node, Gmail, Google Cloud Platform, Brave Search (from the previous video), Gamma (sponsor segment)

## [This Tool Codes for FREE – Here’s How to Install It!](../videos/xsJAA3vhy0E.md)
`xsJAA3vhy0E` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: vibe-coding-app-building, coding-agents, dev-tools

Install-and-try walkthrough of Bolt DIY, a self-hosted, free alternative to Bolt.new, driven by DeepSeek V3 through OpenRouter. The demo works for a whiteboard app, but shapes stay broken, and the title overstates what is free.

- Techniques: Clone, install and run Bolt DIY locally; Configure OpenRouter as the provider with DeepSeek V3; Set a model from the dropdown and check its voice and image support; Iterate with one bug per follow-up prompt
- Tools: Bolt DIY (bolt.diy), Bolt.new, DeepSeek V3, DeepSeek chat, deepseek-coder, OpenRouter, ShadCN UI, Claude 3.5 Sonnet, Perplexity AI, Hugging Face, pnpm, git

## [How to Use Figma AI To Make Sites 10X More Beautiful](../videos/_-FEgdQ_L4I.md)
`_-FEgdQ_L4I` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · topics: vibe-coding-app-building, mcp-and-tools, context-engineering

A walkthrough of a prompt-chained Figma Make workflow for planning and generating a React app, then converting it with a coding agent and feeding Figma designs to agents through the Dev Mode MCP server.

- Techniques: Plan-first prompt chain for Figma Make; Universal full-stack conversion prompt; Figma Dev Mode MCP setup; Implementation-rules configuration file; Screen triage before implementation; Add shadcn MCP for component context
- Tools: Figma Make, Figma desktop app (Dev Mode), Figma Dev Mode MCP server (local and remote variants), ChatGPT (web interface, for planning and prompt outputs), Warp (Warp Code agent, referred to as Warpcode in captions), Supabase, React, Next.js, GitHub, shadcn MCP server, shadcn/ui, Aceternity UI

## [Automation Testing Tutorial Using Cursor AI + Operative.sh & Claude 4 (Setup + Demo)](../videos/GuKdinu64Z0.md)
`GuKdinu64Z0` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: testing-verification, mcp-and-tools, coding-agents

Walkthrough of installing operative.sh's web-eval MCP agent into Cursor and using plain-English test cases, including edge cases, to drive a Playwright browser against a local login page. Vendor-specific, thin on evidence.

- Techniques: Install operative.sh web-eval MCP into Cursor; Call the web eval agent with url, task and headless; Save an authenticated session once with setup-browser-state; Generate test cases to a file, then run them sequentially and write results back
- Tools: operative.sh (web eval agent, setup-browser-state tool, MCP installer, API key), Cursor (IDE, MCP host), Playwright (browser automation, installed by the setup), Claude 4 (Anthropic model; the presenter says it was released 2-3 days before recording and praises it), Aceternity UI (the demo site's UI library; auto-caption reads it as 'as eternity ui'), MCP (Model Context Protocol, the integration path)

## [The BMAD Method: The Ultimate AI Coding System](../videos/fD8NLPU0WYU.md)
`fD8NLPU0WYU` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · topics: context-engineering, multi-agent, coding-agents

BMAD Method tutorial: role-based agents (PO, scrum master, dev, QA) shard a PRD and architecture doc into epics and stories with approval gates, run in Cursor or Claude Code.

- Techniques: Two-document spec bootstrap; Shard then epic/story decomposition; Manual approval gate via story status field; Fresh chat per agent role; Story packet handoff; Learn an unfamiliar repo by feeding it to an LLM; Per-project install with npx; Asterisk commands and role switching
- Tools: BMAD Method (BMAD Code's agile workflow; version not stated), Cursor, Claude Code, Windsurf, ChatGPT, Claude, Gemini, GitIngest, npx (BMAD installer)

## [Postman MCP Server Tutorial: Build & Run AI Agents with APIs (Postman MCP Generator + Cursor)](../videos/QDz4htGbOC4.md)
`QDz4htGbOC4` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: mcp-and-tools, coding-agents

Tutorial on Postman's MCP generator: turn selected API requests into a locally run MCP server, then register it in Cursor and call it from the chat. Thin on depth, but the steps are reproducible.

- Techniques: Generate a local MCP server from API docs in Postman; Put secrets in the generated .env file; Register a local MCP server in Cursor; Test an MCP server through Postman; Build an agent from an MCP server in code with mcp-use
- Tools: Postman MCP generator, Postman, Model Context Protocol (MCP), FastAPI MCP library, mcp-use, Cursor, Claude Desktop, Windsurf, Node.js, npm, OpenWeatherMap API

## [Time to UPGRADE… Unified AI Agents Are Finally Here](../videos/VDql5GzoSoc.md)
`VDql5GzoSoc` · AI LABS · 2025-11-02 · q2 · intro · review · topics: mcp-and-tools, coding-agents, rag-retrieval

Walkthrough of ACI.dev, a hosted platform that connects apps to agents via an app store, an agent playground and a unified MCP server with search and execute tools; the hype title outruns the unbenchmarked speed claims.

- Techniques: Attach apps to an agent in ACI's playground; Unified MCP server in Cursor; Separate agents with separate tool sets
- Tools: ACI.dev, ACI unified MCP server, ACI app MCP server, Agent Playground (ACI), Google Calendar, YouTube, Google Maps, Gmail, Brave Search, Archive (app named in video), Cursor, Claude Desktop

## [ChatGPT Search Just Launched! Say Goodbye to Google?](../videos/f57EGI35bwI.md)
`f57EGI35bwI` · AI LABS · 2025-11-02 · q2 · intro · review · topics: rag-retrieval, product-ux

Short AI LABS walkthrough of ChatGPT's web search for Plus users, with cited sources, live stock and flight queries, and a Chrome extension that routes browser searches to ChatGPT.

- Techniques: Run a cited web search in ChatGPT; Make ChatGPT the browser's default search
- Tools: ChatGPT, ChatGPT web search, Google Search, Perplexity, Google Chrome, Chrome Web Store

## [Claude Code SDK: Build Real AI Apps with Python & MCP](../videos/h1AGjM9IeBM.md)
`h1AGjM9IeBM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: claude-code, coding-agents, mcp-and-tools, pr-code-review

A short walkthrough of the Claude Code SDK (Python, with the docs' example script and a GitHub Actions demo) that frames Claude Code as a programmable subprocess. The example broke for the speaker, and the video shows no working SDK run beyond that.

- Techniques: Run Claude Code as a subprocess from Python; Cap agent iterations with max_turns; Attach external MCP servers to programmatic Claude Code; Mention-triggered issue-to-PR workflow in GitHub Actions
- Tools: Claude Code, Claude Code SDK (Python, TypeScript, CLI), ClaudeCodeOptions, query(), Cursor, GitHub Actions, Claude Code GitHub Actions workflow, Jira MCP server, Slack MCP server, pip

## [Auto Claude is HERE… Upgrade your Claude Code Workflow](../videos/ytn0aXK2gzE.md)
`ytn0aXK2gzE` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: claude-code, testing-verification, dev-tools

AI LABS shows how to attach Claude Code hooks (formatter, linter, build, stop-sound) to settings.json, and how to have a general LLM draft per-language hook rules. Mostly a SwiftUI demo with a sponsor segment.

- Techniques: Post-edit hooks as hard quality gates; Feed check output back to the agent; Stop-event sound notification; Generate hooks from a rules file; Accessibility audit as a hook; Autonomous run from a task file
- Tools: Claude Code, Claude Code hooks (settings.json), ChatGPT (used to draft lint and format rules), swift-format, SwiftLint (swiftlint.yml), SwiftUI, SQLite (local database in the demo app), Prettier (example formatter for other languages), Black (Python formatter, example in the rule-to-hook walkthrough), BMAD method (mentioned as a better approach, not used), claude code rule to hook (GitHub repo, name as spoken; exact repo not confirmed), tools.md (presenter's reference file of Claude Code tools and execution points; not shown)

## [Github Spec Kit FINALLY Fixed AI Coding](../videos/M0ivqkQ5mF4.md)
`M0ivqkQ5mF4` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · topics: context-engineering, coding-agents, multi-agent, testing-verification

A walkthrough of GitHub Spec Kit's specify, plan and tasks workflow driving Claude Code on a demo app, with an honest verdict: the spec-first flow works, but tasks run by hand and the UI came out cluttered.

- Techniques: Requirements in a general chat model before spec-kit; Run /specify with the requirements and answer the clarification flags; Run /plan after the spec is settled; Run /tasks and write tests before implementation; Run independent tasks in parallel with sub-agents
- Tools: GitHub Spec Kit ("Specify"), Claude Code, ChatGPT, Gemini (supported assistant), GitHub Copilot (supported assistant), ShadCN UI components, Notion (visual theme followed), git

## [OpenAI Announces a Major Breakthrough: AGI is Here (OpenAI o3 Explained)](../videos/AJknN7qzmDU.md)
`AJknN7qzmDU` · AI LABS · 2025-11-02 · q2 · intro · news · topics: models-research, evals

Announcement-day explainer on OpenAI o3 and o3-mini: ARC-AGI scores from ARC Prize, plus two live demos of o3-mini writing code and grading itself on GPQA. The "AGI is here" title overstates what the video shows.

- Techniques: Self-written evaluation harness on a public dataset; Prompt-to-code-to-run loop from a local UI; Compare reasoning effort levels on the same benchmark
- Tools: OpenAI o3, OpenAI o3-mini, OpenAI o1 Pro, OpenAI o1-preview, OpenAI o1-mini, GPT-4 Turbo (caption reads 'GPT for Turbo' in the latency comparison), ARC-AGI benchmark, ARC Prize leaderboard, GPQA dataset, Python

## [ShadCN Dropped Something to FINALLY Fix Your UI](../videos/mSMflOx5pq8.md)
`mSMflOx5pq8` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · topics: mcp-and-tools, coding-agents, multi-agent, context-engineering

Tutorial on shadcn's official registry MCP: add extra community component registries, then run a multi-subagent workflow (requirements, component research, implementation) to build UIs without unnecessary components.

- Techniques: Install the shadcn registry MCP; Add third-party component registries; Preview a registry's visual style before using it; Three-stage subagent workflow for UI builds; Express agent for small changes; Port the commands to Cursor; Apply a TweakCN theme
- Tools: shadcn (CLI and registry MCP server), Claude Code, Cursor, VS Code, Next.js, React, npm, components.json, mcp.json, Aceternity UI, Origin UI, Neo Brutalism (registry, failed)

## [I Tried Building an Expo App in 360 Seconds… Here’s What Happened](../videos/Dmgu7jE2toM.md)
`Dmgu7jE2toM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: vibe-coding-app-building, coding-agents, context-engineering

Walkthrough of a two-tool flow for Expo mobile apps: Tempolabs generates the PRD, user flow and wireframes, then Cursor takes over the code via a synced docs folder. Single-project demo with no measurements.

- Techniques: PRD and user flow from a requirements prompt; Connect the builder to the IDE via the Tempolabs extension; Commit the spec into the repo as context for the coding agent; Route stubborn bugs to the agent that made the code; Verify gestures on a device, not the desktop preview
- Tools: Tempolabs, Cursor, Expo, Expo Go, Gemini 2.5 Pro, ChatGPT, Mermaid, Windsurf, Next.js, Supabase, Stripe, SSH

## [Google won't STOP... They Just Upped the Gemini CLI Again](../videos/A3AOeX1s7yw.md)
`A3AOeX1s7yw` · AI LABS · 2025-11-02 · q2 · practitioner · review · topics: coding-agents, mcp-and-tools, context-engineering

A walkthrough of Gemini CLI's recent updates: free-tier quotas, MCP setup via settings.json, slash commands, VS Code inline diffs, and "extensions" as shareable bundles of context, MCP servers and commands.

- Techniques: Custom slash commands as TOML files for page and component generation; Adding MCP servers by editing settings.json; YOLO mode toggle for uninterrupted runs; Reviewing agent edits in VS Code via the IDE companion; Built-in session helpers; Packaging a team extension
- Tools: Gemini CLI, Gemini 2.5 Pro, ShadCN MCP (shadcn), Gemini CLI companion extension (VS Code), VS Code, Claude Code (compared, not demoed), Cursor (compared, not demoed), ChatGPT (used to draft the to-do app), TweakCN (theme source), Qwen (named as a competing free agent, no version), Skywork Super Agents (sponsor, not demoed)

## [Qwen 3 ACTUALLY Made Me Quit Claude Code](../videos/lXWazKnuZNQ.md)
`lXWazKnuZNQ` · AI LABS · 2025-11-02 · q2 · intro · review · topics: coding-agents, token-cost-efficiency, mcp-and-tools

Walkthrough of using Qwen Code's free OAuth tier and Claude Code Router to run cheap Qwen3 Coder backends, with a single anecdotal DaisyUI build comparing it to Claude Code.

- Techniques: Qwen Code OAuth sign-in for free runs; Routing Claude Code through Claude Code Router; Context7 MCP for libraries models do not know well; Give the agent a PRD before building
- Tools: Qwen Code, Qwen3 Coder, Claude Code, Claude Code Router (ccr), Gemini CLI, Context7 MCP, DaisyUI, OpenRouter, ModelScope, Claude Sonnet 4, Cursor, CLAUDE.md

## [Llama Coder: Is is WORTH It? Tested for Full-Stack App Building!](../videos/T5fIdojtR3A.md)
`T5fIdojtR3A` · AI LABS · 2025-11-02 · q2 · intro · review · topics: vibe-coding-app-building, coding-agents

Hands-on test of Llama Coder, a free open-source prompt-to-app builder on Together AI. It improved after switching to Llama 3.3 but still fell short of Cursor, Windsurf, Bolt.new and v0.

- Techniques: Run Llama Coder locally from the GitHub repo; Paste runtime errors back into the change prompt box; Switch the generation model from the dropdown; Enable the ShadCN UI toggle; Publish and share the generated app; Use the built-in placeholder prompt for a calculator
- Tools: Llama Coder, Together AI, Llama 3.3, Llama 3.1, Qwen 2.5 Coder, Gemma 2, ShadCN UI, ChatGPT, Claude 3.5 Sonnet, GPT-4 Omni, Gemini, Cursor

## [The Windsurf vs Cursor rivalry just reached a turning point](../videos/gejEvBWbgHA.md)
`gejEvBWbgHA` · AI LABS · 2025-11-02 · q2 · intro · news · topics: coding-agents, vibe-coding-app-building, product-ux

Windsurf feature tour: select a live page element in the preview, describe the change to Cascade, and it edits the code. Also covers Tab to Import, linter integration, suggested actions, built-in MCP docs and admin model controls. Mostly unmeasured demos.

- Techniques: Select-and-describe UI edits; Batch section edits for animations; Let the agent fix its own build errors; Drag files into the agent instead of referencing them
- Tools: Windsurf, Cascade, Cursor, Claude 3.7 (thinking mode, as named by the host), GPT-4.5 (as named by the host), DeepSeek V3, MCP

## [You Won’t Believe What Google Gemini 2.0 Can Do Now!  - #gemini2flash #aistudio](../videos/teEp3I83k-w.md)
`teEp3I83k-w` · AI LABS · 2025-11-02 · q2 · intro · review · topics: voice-multimodal, models-research, sandboxing-execution

Walkthrough of Gemini 2.0 Flash's real-time webcam and screen-share mode in Google AI Studio, with a list of claimed benchmark scores and quick tests of its tools. Mostly a demo with light substance.

- Techniques: Live screen and webcam Q&A for unfamiliar software; Show token counts and temperature in AI Studio; Small smoke-test battery for a new model; Re-prompt once when grounding returns no sources; Get API access from AI Studio or OpenRouter
- Tools: Gemini 2.0 Flash, Gemini 1.5 Flash, Gemini 1.5 Pro, Google AI Studio, Gemini Multimodal Live API (Stream Real-Time), Google Search grounding, Gemini code execution, Microsoft Word, Adobe Premiere Pro, OpenRouter

## [Gemini 2.0 Flash: Is Google Taking Over Code?](../videos/5Z42W5AK6JU.md)
`5Z42W5AK6JU` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: coding-agents, vibe-coding-app-building

Hands-on tutorial that builds small apps with Gemini 2.0 Flash through the Aider and Cline coding agents, with setup steps and a candid note on the output's gaps. Thin on analysis despite its "is Google taking over code" title.

- Techniques: Aider with a Gemini default via .env; Cline on OpenRouter to avoid provider rate limits; Iterative prompting to finish a scaffold
- Tools: Gemini 2.0 Flash, Aider, Cline (formerly Claude Dev), VS Code, OpenRouter, Google AI Studio, shadcn/ui, Claude, GPT-4

## [How To Use Open AI Codex Absolute Beginners](../videos/KpZYZwaHBc0.md)
`KpZYZwaHBc0` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: coding-agents, context-engineering, software-factory

Beginner walkthrough of OpenAI's Codex CLI and cloud agents: approval modes, AGENTS.md, MCP setup, role-specialized agent files, and running background tasks that end in a GitHub PR.

- Techniques: Full Access approval mode for unattended runs; Model selection by task difficulty; Compact to manage context; Generate AGENTS.md with /init; Role-specialized agent files; Build MCP config from a repo-to-text dump; Cloud task per branch with PR handoff; Plan mode before implementation; BMAD-style planning loop
- Tools: Codex CLI, Codex IDE extension, Codex cloud (ChatGPT app), GPT-5, GPT-5 Codex (Low, High), AGENTS.md, config.toml, Claude Code, Claude Desktop, Cursor, ChatGPT, GitHub

## [Generate The PERFECT App UI Every Time with this 2-Step Cursor Guide](../videos/H-ok6Zx9SR8.md)
`H-ok6Zx9SR8` · AI LABS · 2025-11-02 · q3 · intro · tutorial · topics: vibe-coding-app-building, coding-agents, context-engineering

AI LABS tutorial on generating varied app UI designs inside Cursor with manually invoked rule files, replacing a paid-API design extension, with a Claude Code port and a plain-English method for writing rule files.

- Techniques: Manual-mode Cursor rule files as invocable workflows; Extract a design.json from a reference image; Targeted variation rules (persona, device, geolocation); Infinite-design iteration loop; Fresh chat per generation round; Writing rule files in plain English; Porting a rule to Claude Code custom commands
- Tools: Cursor (rules, agent, .mdc rule files), Super Design Dev (Cursor extension by Jason Zhao), Claude Code (custom commands, parallel agents), Claude 3.5 Sonnet, Anthropic Claude API

## [AI Coding with Cursor & Claude: Build Apps That People Keep Using in 5 Simple Steps](../videos/i_31WoayEIo.md)
`i_31WoayEIo` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: vibe-coding-app-building, context-engineering, product-ux, mcp-and-tools

Tutorial on building a photo-cleaner iOS app with Cursor and Claude: user journey saved in a markdown file, HTML prototype, palette, fonts, icon, Swift port and animations guided by Context7 docs.

- Techniques: Persistent context files in the repo; Specify the user journey first, then build an HTML prototype; Palette-from-elements prompt sequence; Google Fonts embed into the HTML prototype; App icon via ChatGPT image model with palette constraint; Context7 MCP for framework docs; Fresh chat per task plus Cursor to-do list; Two-stage animation pipeline; Screenshot-driven bug fixing
- Tools: Cursor, Windsurf, Lovable, bolt.new, Claude Code, Gemini CLI, Claude, ChatGPT, ChatGPT image model (called ChatGPT 4 image model in the video), Context7 MCP, Google Fonts, HTML

## [How I Built a ChatGPT Powered Voice Agent with MCP + LiveKit](../videos/jRk63S3v-UQ.md)
`jRk63S3v-UQ` · AI LABS · 2025-11-02 · q3 · intro · tutorial · topics: voice-multimodal, mcp-and-tools

Tutorial on building a voice agent with a LiveKit + Cartesia + OpenAI base, then wiring a local WhatsApp MCP server into it so speech can trigger tool calls.

- Techniques: Clone, install with uv, and run the voice agent locally; Change the LLM and the system prompt in the main agent file; Wire an MCP server into the voice agent through the MCP-use library
- Tools: LiveKit (voice agent transport and dashboard), OpenAI GPT-4o mini (LLM; transcribed as GPT-40 mini), OpenAI Whisper (speech-to-text), Cartesia Sonic preview (TTS), MCP-use library (MCP tool-use agent), WhatsApp MCP server (local), Brave Search MCP, Airbnb MCP (mentioned as a possible example), uv (Python package manager), Cursor (editor), git

## [You Need Claude Sandboxes... 90% Faster AI Coding](../videos/xckU9n9r8Rs.md)
`xckU9n9r8Rs` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · topics: coding-agents, multi-agent, software-factory, context-engineering

Walkthrough of running BMAD-planned stories in parallel with git worktrees and one Claude Code instance per subtask, with a QA agent review loop. The 90% title claim is not backed by the numbers shown.

- Techniques: BMAD planning-first pipeline; Prompt the story generator to split stories into non-conflicting parallel subtasks; One git worktree per subtask, managed through Conductor; QA review then fix loop per story; PR per story, merged by Claude Code
- Tools: BMAD method (planning agents, Scrum Manager, dev and QA agents), Claude Code, Claude Desktop, ChatGPT, Cursor, Conductor (multi-workspace UI for parallel Claude Code runs), git worktrees, GitHub, Next.js (initialized in story 1), OutSkill (sponsor segment, not used in the demo)

## [RAG Just Got Updated…](../videos/EgXOaH-ZqfU.md)
`EgXOaH-ZqfU` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: context-engineering, rag-retrieval, mcp-and-tools, coding-agents

Setup and demo of Archon, a beta self-hosted tool that gives Claude Code or Cursor project docs, a task backlog, and on-demand RAG over crawled docs via MCP. Includes a sponsor segment and an oversold title.

- Techniques: Local Archon stack setup; Project docs and backlog from a feature description; Rules-file-driven on-demand RAG; Crawl vendor docs into a knowledge base
- Tools: Archon, Claude Code, Cursor, Supabase, Docker, Docker Compose, MCP (Model Context Protocol), OpenAI API (embeddings), Google Gemini API (embeddings, free tier), SwiftUI, Xcode, Liquid Glass (Apple UI design)

## [Grok 3 Tested: Did Elon Musk Actually Succeed This Time?](../videos/E4fML4Lghjw.md)
`E4fML4Lghjw` · AI LABS · 2025-11-02 · q2 · intro · review · topics: models-research, evals, coding-agents

Hands-on test of xAI's Grok 3 with about 11 quick prompts: strong on word problems and reasoning, failed the constrained haiku and most coding prompts, so the verdict is not for coding tools.

- Techniques: Pass/fail prompt battery for a new model; Letter-constraint instruction test; Copy-paste code check for generated apps
- Tools: Grok 3 (xAI), Grok 3 reasoning mode ('Big Brain'), Grok Deep Search agent, LM Arena (called 'chat arena' in the transcript), Artificial Analysis leaderboard, OpenAI o3 (upcoming, per the host), OpenAI o3-mini, DeepSeek R1, GPT-4o, Claude 3.5 (image and SVG comparison), Cursor, Windsurf

## [Program Claude Code to be your new UI Designer (+ works with any IDE)](../videos/TyGx277x9hQ.md)
`TyGx277x9hQ` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: claude-code, vibe-coding-app-building, coding-agents, context-engineering

Walkthrough of using Claude Code plus ChatGPT planning to turn an HTML UI prototype into a SwiftUI iOS app and re-skin it in Apple's Liquid Glass style; practical but anecdotal.

- Techniques: Plan-in-chat, then execute in agent; Screenshot-to-HTML prototype; Conversion rules file; Style transfer from references; Visual bug reporting; Start from the native project template
- Tools: Claude Code, Claude 4 Sonnet, Claude Opus (Claude 4), Cursor (Max mode), ChatGPT, Xcode, SwiftUI, Swift, Next.js, HTML/CSS, iOS Simulator, Apple Liquid Glass design

## [OpenAI Agent Builder vs Claude: Who Wins Multi-Agent Workflows? (Complete Comparison)](../videos/sLiVXlIlSBQ.md)
`sLiVXlIlSBQ` · AI LABS · 2025-11-02 · q2 · intro · review · topics: mcp-and-tools, agent-architecture, product-ux, coding-agents

A walkthrough of OpenAI's AgentKit (Agent Builder, ChatKit, widgets), with a Speechmatics sponsor segment up front; practical for seeing the visual workflow and ChatKit setup, thin as a head-to-head comparison.

- Techniques: Classifier-then-route agent workflow; Human approval gate in a workflow; Remote MCP server registration per agent; ChatKit starter quickstart; Theme via Playground, then hand off to a coding agent; Prompt-to-widget, then pin the format in the agent prompt; Custom widgets with Claude Code and agents.md
- Tools: OpenAI Agent Builder, OpenAI AgentKit, OpenAI ChatKit, ChatKit Playground, OpenAI Widget Builder, OpenAI vector store / file search, OpenAI guardrails node, ChatGPT apps, Zapier (MCP servers), Pipedream (MCP servers), n8n (comparison only), Next.js

## [I Built an MCP Server with a Single Prompt!](../videos/yLAmw4oL-6A.md)
`yLAmw4oL-6A` · AI LABS · 2025-11-02 · q2 · intro · review · topics: mcp-and-tools, coding-agents

A walkthrough of a hosted prompt-to-MCP-server generator, shown building a weather server and a Figma server, with practical lessons on testing before deploy and wiring the result into Cursor.

- Techniques: Prompt-to-MCP generation with env-var credentials; Test the raw API call before deploying; Declare the plan limits up front; Recover from drift by restarting from the original prompt; Wire a hosted MCP server into Cursor; Split tools by data type; Export and run locally
- Tools: MCP (Model Context Protocol), SSE-based MCP servers, Figma MCP server (get Figma node data tool), OpenWeather API, Cursor, Claude Desktop, Windsurf, mcp.json

## [3 Ways to Build ACTUALLY Beautiful Websites Using Cursor AI](../videos/djDZHAi75dk.md)
`djDZHAi75dk` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: vibe-coding-app-building, product-ux

Three Cursor workflows for less generic AI-built sites: clone a reference design via an extracted design JSON, theme shadcn/ui with TweakCN, and drop in React Bits components, plus font and layout prompting tips.

- Techniques: Reference design to JSON design system, then build from it; TweakCN theme to shadcn/ui project; Drop a copied component into a named section; Font via embed code; Spec the layout explicitly and keep it in a file; Animation restraint
- Tools: Cursor, Claude, ChatGPT, TweakCN, shadcn/ui, React Bits, Aceternity UI, Google Fonts, Next.js, framer-motion, React, HTML

## [I Just Saved $1600 With GLM 4.5](../videos/yD4qcd_8o2U.md)
`yD4qcd_8o2U` · AI LABS · 2025-11-02 · q3 · intro · review · topics: token-cost-efficiency, coding-agents, models-research

AI LABS walkthrough of ZAI's $3 GLM Coding Lite plan as a cheaper Claude Code backend, with the author's side-by-side UI test and a claim of roughly $1600 saved; the cost case rests on prompt counts and one subjective comparison.

- Techniques: Point Claude Code at GLM via env var override; Same-prompt side-by-side model comparison; Parallel agents in separate git worktrees; HTML-first UI prototyping on a canvas
- Tools: GLM (GLM 4.5 coding plan, ZAI), Claude Code, Cline, superdesign.dev, Conductor, BMAD method, Cursor, Codex, Kimi K2, Lindy Build

## [Claude Code Can Finally Make Beautiful Websites](../videos/idccdssOZQ8.md)
`idccdssOZQ8` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: vibe-coding-app-building, product-ux, coding-agents

Three UI design principles (depth through layered color and shadows, box-based responsive layout, and a four-role color palette) for making AI-generated sites look better, shown on a cloned Airbnb-style page.

- Techniques: Color-layer depth instead of borders; Dual shadow with depth levels and a gradient; Flexible box layout with parent-child structure; Priority-based responsiveness; Four-role palette; Prompt per principle, with before/after comparison
- Tools: Claude Code (named in the title only; the transcript does not name it), Colors (palette-browsing site, named in the transcript, no URL given), Airbnb-style page clone (demo subject, not a tool)

## [AI Memory Explained: SuperMemory MCP for Cursor, Claude & Windsurf](../videos/mKXzPVIMFYE.md)
`mKXzPVIMFYE` · AI LABS · 2025-11-02 · q2 · intro · review · topics: memory, mcp-and-tools, context-engineering

Walkthrough of SuperMemory MCP: one hosted memory store shared across Cursor, Claude Desktop and Windsurf through add and search MCP tools, plus an IDE rule that auto-saves project changes.

- Techniques: Cross-client memory via a hosted MCP server; Milestone summary saved to memory; Auto-sync rule for memory updates; Resume by searching memory first
- Tools: SuperMemory MCP, SuperMemory API, Cursor, Claude Desktop, Windsurf, Next.js, React

## [Clone Any Website INSTANTLY! New V0 Updates You Need to See.](../videos/gNgxnECvLWM.md)
`gNgxnECvLWM` · AI LABS · 2025-11-02 · q2 · intro · review · topics: vibe-coding-app-building, testing-verification

Walkthrough of v0's new URL-to-clone, built-in console logs, version rollback and click-to-edit features, shown on one Notion homepage clone; thin substance behind a hype title.

- Techniques: Clone a page from its URL; Log-driven debugging loop; Roll back and rebase on a known-good version; Scoped edits by element selection
- Tools: v0

## [Warp Terminal: The AI Terminal That Transformed My Workflow...](../videos/C8vL-VKcJgo.md)
`C8vL-VKcJgo` · AI LABS · 2025-11-02 · q2 · intro · review · topics: dev-tools, coding-agents

A feature tour of the Warp terminal: natural-language commands with approve-before-run, Ctrl+R and Ctrl+I AI modes, an agent that installs a repo from its README, Warp Drive team sharing, and a WSL route for Windows.

- Techniques: Natural-language command generation with approve-before-run; README-driven repo setup via agent; Environment variable for API keys before launch; Team sharing through Warp Drive; Windows install via WSL
- Tools: Warp (terminal, built-in AI agent, Warp Drive), Aider (transcribed as "Adr"/"AIDR"; a repo the host installs, probably Aider), OpenAI API (key set as an environment variable), WSL (Windows Subsystem for Linux), Debian .deb installer for Warp, Python (the wrong version was caught in the README setup), Windsurf (teased for a later video)

## [I'm Never Vibe Coding Without Next JS Agents Anymore](../videos/yJv2JRM--ws.md)
`yJv2JRM--ws` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: mcp-and-tools, coding-agents, vibe-coding-app-building

A walkthrough of building a full-stack Next.js agent marketplace with Claude Code and three MCP servers (Supabase, ShadCN, Stripe), driven by a PRD and per-MCP prompts. The reusable parts live in linked resources, not on screen.

- Techniques: One-command MCP wiring with a /mcp health check; PRD to converter prompts, one per MCP; Dependency-ordered single-session build; Component-grounded UI with a theme and a usage slash command; Static UI first, then a separate wiring pass; Mock-then-real payment verification
- Tools: Claude Code, Cursor, Next.js, Supabase (MCP server), ShadCN MCP, shadcn/ui, TweakCN, Stripe (MCP server, Stripe checkout), ChatGPT (used for the PRD brainstorm)

## [Build FRONTEND Faster Than Ever with This Cursor MCP Setup!](../videos/DpdM4xei5fw.md)
`DpdM4xei5fw` · AI LABS · 2025-11-02 · q2 · intro · review · topics: mcp-and-tools, vibe-coding-app-building, coding-agents

A 6-minute walkthrough of the 21st.dev / Magic UI MCP server inside Cursor, showing component generation, logo search and catalog install for frontend work.

- Techniques: Install an MCP UI server into the IDE; Prompt for a self-contained component, then let the IDE agent place it; Use logo search to fill in brand or icon assets; Install a catalog component by copying the command
- Tools: 21st.dev (Magic component builder, logo search, component inspiration, UI catalog), Magic UI, Cursor, Windsurf, Cline (called "Klein" in the auto-captions), VS Code, React, TypeScript, MCP (Model Context Protocol), WSL, v0 (mentioned as the comparison point for the component builder), ChatCN (named by the host as a UI library source; spelling from auto-captions, not verified)

## [Agents.md Is HERE… 90% of AI Tools Will Use This Now](../videos/Pmc4OfSlhbE.md)
`Pmc4OfSlhbE` · AI LABS · 2025-11-02 · q2 · intro · news · topics: context-engineering, coding-agents, claude-code

Host argues OpenAI's AGENTS.md should become the single cross-tool agent context file, replacing per-tool rules files, and says Claude Code's absence is the gap. Includes a sponsor segment.

- Techniques: Single AGENTS.md as shared project context; Rely on the auto-loaded context file for session bootstrap
- Tools: AGENTS.md, CLAUDE.md, Model Context Protocol (MCP), Figma MCP server, Claude Code, OpenAI Codex, Gemini CLI, Qwen Code, Cursor, Windsurf, Kiro, GitHub Copilot

## [Build Sites That Sell 99% of Products with Claude AI](../videos/VtmBevBcDzI.md)
`VtmBevBcDzI` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · topics: vibe-coding-app-building, claude-code, context-engineering

A landing-page design walkthrough: reverse-engineer a strong v0 site, then steer Claude Code with named libraries (paper shaders, Framer Motion), Google Fonts, layout screenshots and SVG code. Mostly a practical tip list with a sponsor segment.

- Techniques: Reference-site reverse engineering; Named-library prompt with a focused context; Framer Motion for animations; Two-step gooey morph; One-word font accent; Layout from a gallery screenshot; SVG logos and icons as code
- Tools: Claude Code, v0, Cursor (mentioned as a tool to use, no steps shown), Paper Shaders (library for animated website backgrounds), Framer Motion (React version named), GitIngest ("Git Ingest", converts a repo to AI-readable text), Google Fonts, Landbook (layout and design gallery), ChatLLM by Abacus (sponsor)

## [Claude FINALLY Fixed AI Coding By Releasing This](../videos/oj44Vrh0XyM.md)
`oj44Vrh0XyM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · topics: context-engineering, claude-code, multi-agent, memory

Walks through four Claude Code context-engineering techniques from Anthropic's "Effective Context Engineering for AI Agents" paper: compaction, context editing and memory, structured note-taking, and subagents. Mostly a conceptual intro with small demos; the main takeaway is to pick the technique that fits the task.

- Techniques: Manual compaction with retain instructions; Persistent instruction via the # memory shortcut; CLAUDE.md as the project brief; Structured note files maintained by the agent; Coordinator plus specialist subagents
- Tools: Claude Code, Claude Sonnet 4.5, CLAUDE.md, Claude memory tool, ACI.dev Gate22 (open-source MCP gateway, sponsor), Anthropic paper: Effective Context Engineering for AI Agents

## [6 INSANE Repos I Wish I Knew Before...](../videos/tmj4_HhX7jI.md)
`tmj4_HhX7jI` · AI LABS · 2025-11-02 · q2 · intro · review · topics: claude-code, mcp-and-tools, context-engineering, vibe-coding-app-building

Six-repo roundup for Claude Code and MCP: awesome-claude-code, BMAD agile agents, UI component libraries, GitMCP, FastAPI-MCP and mcp-use. Mostly quick pitches plus a mid-video sponsor segment.

- Techniques: Repo to remote MCP server via GitMCP; Expose FastAPI endpoints as MCP tools (fastapi_mcp); Use an MCP server from code with mcp-use; Repo dump into markdown as Claude Code context; BMAD staged agile agents; Pick UI components with the agent; Parallel Claude Code sessions and usage monitoring
- Tools: Claude Code, Claude Desktop, Claude Squad, Claude Code usage monitor, awesome-claude-code, BMAD method, Cursor, shadcn/ui (ShadCN), awesome-ui-component-library, Ant Design, Recharts, Next.js

## [Complete Guide to ChatGPT’s Canvas Update  New Tools & Features You Need](../videos/-ajtoeyu4go.md)
`-ajtoeyu4go` · AI LABS · 2024-11-02 · q2 · intro · review · topics: coding-agents, product-ux

A roughly 11-minute walkthrough of ChatGPT Canvas, the side-by-side editor for code and writing, covering inline edits, auto-comments, logging, port-to-language, and version navigation. Little hard data; mostly a UI tour.

- Techniques: Iterate in place with Canvas instead of re-prompting; Canvas editor actions for code: review, comments, logs, port; Canvas writing actions: Suggest Edits, reading level, polish, emojis
- Tools: ChatGPT, ChatGPT Canvas, GPT-4 (with Canvas), Python, Pygame, VS Code, C++, SFML

## [The 1 Click Solution to PRESENTATION PERFECTION No One Tells You!](../videos/de71tQ3k5xA.md)
`de71tQ3k5xA` · AI LABS · 2024-11-02 · q2 · intro · tutorial · topics: vibe-coding-app-building, product-ux

Step-by-step walkthrough of generating a slide deck from pasted notes in Gamma AI, covering input methods, generation settings, and editing images and layout.

- Techniques: Generate a deck from pasted notes in Gamma; Replace a generated image; Reorganize a card's information layout; Keep AI-generation cost in check
- Tools: Gamma AI (gamma.app web app), Flux (image model used by Gamma for AI image generation, default option), Google account sign-in, PowerPoint (mentioned only as the familiar format being replaced)

## [Suno AI Tutorial - Make a Song Like Your Favorite Artists with Suno AI](../videos/tfntgZYlGko.md)
`tfntgZYlGko` · AI LABS · 2024-11-02 · q2 · intro · tutorial · topics: voice-multimodal

A five-minute walkthrough of making songs in Suno AI (custom lyrics, style, vocal or instrumental tracks) plus its free-tier limits; a basic consumer tutorial with no engineering content.

- Techniques: Suno custom-mode song generation; Instrumental track generation; Steering with the style and genre list
- Tools: Suno AI (web app, Create tab, Custom Mode, instrumental toggle), ChatGPT (optional lyric generation)

## [AI Images Are Getting Shockingly Real - FLUX 1.1 PRO](../videos/sFZR6EG4WxU.md)
`sFZR6EG4WxU` · AI LABS · 2024-11-02 · q2 · intro · tutorial · topics: voice-multimodal, product-ux

Short tutorial on generating photoreal images with Flux 1.1 through Together AI, using a prompt-template trick; anecdotal, hype-driven, and untested.

- Techniques: Flux 1.1 generation on Together AI (UI steps); Photo-style prompt template (speaker's 'secret trick'); Type-word plus file-type prompt
- Tools: Flux 1.1 (Flux 1.1 Pro per the title; the transcript says Flux 1.1), Together AI (website, Google sign-in)

## [Introducing Open-Source PHIDATA: Your first step towards building your own AI Agents](../videos/nkh7q8WU7oU.md)
`nkh7q8WU7oU` · AI LABS · 2024-11-02 · q2 · intro · tutorial · topics: agent-architecture, memory

Walkthrough of Phidata's agent playground UI, showing how to serve agents from a local server on port 7777 and chat with them through the hosted app while memory and sessions stay on your machine.

- Techniques: Serve agents from a local server and attach a hosted chat UI; Define an agent with a description, tools and a current date; Keep session history in a local DB file and reset by deleting it; Turn on debug logs with an environment variable
- Tools: Phidata, Phidata agent UI / playground, OpenAI, Exa, DuckDuckGo search, Ollama, Python virtualenv

## [Get Started with Cursor: The AI Code Editor That Lets You Build Without Coding](../videos/NtGagWyY1kU.md)
`NtGagWyY1kU` · AI LABS · 2024-11-02 · q2 · intro · tutorial · topics: coding-agents, vibe-coding-app-building

A 5-minute beginner walkthrough of the Cursor AI code editor: install, set up, use Ctrl+L chat and Ctrl+K inline edits to generate and modify small Pygame games. Thin, hype-framed, no review of output quality.

- Techniques: Chat-first prototyping of a small game; Inline edit with prompt, Apply, Accept; VS Code migration at setup; Toggle AI features and bring your own model key
- Tools: Cursor, VS Code, Python, Pygame

## [OpenAI's NEXT BIG LEAP in AI Reasoning](../videos/sFn8D9DutIw.md)
`sFn8D9DutIw` · AI LABS · 2024-11-02 · q2 · intro · news · topics: models-research, evals

Short AI LABS news explainer on OpenAI's o1 preview: slower, chain-of-thought reasoning, vendor benchmark claims, and three single-prompt demos (strawberry letter count, math, murder mystery) cross-checked with Claude.

- Techniques: Side-by-side prompt comparison; Cross-model verification
- Tools: OpenAI o1 (o1-preview), GPT-4.0 (as spoken in the transcript), ChatGPT Plus, Claude

## [Discover the SECRET tool that unlocks UNLIMITED generations with the Flux model!](../videos/DiMliAtLc2M.md)
`DiMliAtLc2M` · AI LABS · 2024-11-02 · q2 · intro · review · topics: vibe-coding-app-building

Walkthrough of PicLumen, a web image generator that offers Flux and other models, covering reference images, inpainting and Hugging Face prompt building; the "unlimited" title is contradicted by the speaker's own caveat.

- Techniques: Character-consistent generation from one reference image; Style-consistent generation; Region inpainting; Building a Flux prompt with the Hugging Face prompt generator
- Tools: PicLumen (web image generator; the transcript spells it Pick Lumen / PIC Lumen), Flux (image model, lower-tier version on PicLumen), PicLumen line art model, PicLumen anime model, Hugging Face prompt generator for Flux

## [Bolt.new Tutorial Website – Replaces Cursor, Claude & v0 – The Only AI Tool You Need!](../videos/6-sTKmPl4wA.md)
`6-sTKmPl4wA` · AI LABS · 2024-11-02 · q2 · intro · review · topics: vibe-coding-app-building, coding-agents

A 7-minute walkthrough of Bolt.new, a browser tool that generates a React website from a text prompt, then iterates on it through chat; the transcript shows real friction (vague prompts, missing images, out-of-credits).

- Techniques: One-prompt scaffold, then chat-driven iteration; Name the exact effect or fix instead of describing a mood; Copy build errors back into the chat; Check generated assets and sections by eye
- Tools: Bolt.new, React, V0, Cursor, Replit (comparison only), Claude (UI resemblance only)

## [I Built an App in 10 Minutes WITHOUT Coding! | Using Cursor Composer](../videos/LrIhNW2BN28.md)
`LrIhNW2BN28` · AI LABS · 2024-11-02 · q2 · intro · review · topics: vibe-coding-app-building, coding-agents, context-engineering

Short Cursor promo that builds a budget tracker and a task app from plain-text requirements with Composer; shows multi-file generation, but the evidence is two cherry-picked demos.

- Techniques: Requirements file, then generate; Enable Composer before first use; Generate, then re-prompt for design, then fix bugs; Scope chat with @-references; Ctrl+K for local edits
- Tools: Cursor, Cursor Composer, Cursor Tab (completions), Cursor Chat (@-references), Cursor Ctrl+K inline edit

## [The MIND-BLOWING Way to Create Videos with Kling AI!](../videos/r4eCgDR3_MU.md)
`r4eCgDR3_MU` · AI LABS · 2024-11-02 · q2 · intro · review · topics: voice-multimodal

A short walkthrough of the Kling AI web app for generating AI videos and images from text prompts, with its free daily credits and settings. Thin on substance and not relevant to our projects.

- Techniques: Generate a text-to-video clip in Kling's web app; Generate images with reference and count settings
- Tools: Kling AI (web app: AI Video, AI Image, AI Video Editor which is marked coming soon)

## [Fragments by E2B: The FREE AI Tool Surpassing Bolt.new & v0.dev?](../videos/Au5ixSJ4C3w.md)
`Au5ixSJ4C3w` · AI LABS · 2024-11-02 · q2 · intro · review · topics: vibe-coding-app-building

A short walkthrough of Fragments by E2B, an open-source Claude Artifacts-style tool that turns prompts or screenshots into live-previewed UI, with a free-tier and local-run note.

- Techniques: Iterative prompt-to-UI with targeted fix prompts; Screenshot-to-clone prompt; Persona-first generation; Local run from the open-source repo
- Tools: Fragments (by E2B), E2B, Claude Artifacts, Claude, Gemini (website used as the clone target), Google sign-in, Bolt.new (named in the title and intro only), v0.dev (named in the title only)

