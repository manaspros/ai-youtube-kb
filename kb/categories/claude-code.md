# claude-code — 192 videos

*Claude Code specifically — features, CLAUDE.md, hooks, skills, plugins, subagents, slash commands, power-user tips*

By channel: AI Engineer 22 · Kai Explains 11 · AI LABS 98 · Better Stack 61

**Synthesized guide:** [guides/claude-code.md](../guides/claude-code.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [This Gateway Makes Claude Code 30% Cheaper (Context Mode)](../videos/Afm-GNrJbEQ.md)
`Afm-GNrJbEQ` · Better Stack · 2026-11-01 · q3 · practitioner · review · also: token-cost-efficiency, infra-cost-scaling, security-guardrails

Better Stack tests Context Mode's hosted Claude Code gateway: same answers, about 31% lower cost on log-heavy sessions, a command firewall, but all prompts pass through vendor servers.

- Techniques: Route Claude Code through a proxy gateway by base URL; Fold bulky tool output and keep an archive; Command-rule firewall with a preset; Side-by-side cost benchmark for a proxy or optimizer
- Tools: Claude Code, Context Mode gateway (hosted), Context Mode open-source plugin, Anthropic API, Claude Max plan, Opus 5.5 (as named in the video), NASA Kennedy Space Center web server logs, July 1995 (test data)

## [Claude Code Is Wasting Your Tokens on This](../videos/F4h3a8HFBSE.md)
`F4h3a8HFBSE` · Better Stack · 2026-11-01 · q3 · practitioner · review · also: token-cost-efficiency, observability

Claude Code's background-agent summaries re-send full conversations every 30 seconds, costing an estimated 2-20% of usage with no off switch; the video gives measurements and workarounds.

- Techniques: Measure hidden agent-side LLM calls with OTel; Disable background summaries via the subagent setting; Block the summary timer with a preload script (advanced, risky); Budget background agents by wallclock time
- Tools: Claude Code, OpenTelemetry, Better Stack, ccusage, Bun, T3 Code, TanStack, Claude Opus, Claude Haiku

## [Anthropic Just Released A New System For Using Claude Code](../videos/S49gppZl8H0.md)
`S49gppZl8H0` · AI LABS · 2026-10-31 · q2 · practitioner · tutorial · also: pr-code-review, testing-verification, multi-agent

Walkthrough of Anthropic's Claude Code review system, rebuilt as skills: eval.md gates before build, a fresh-context builder/verifier/reviewer loop, risk tiers, and git rollback.

- Techniques: Eval-first feature gating; Fresh-context builder/verifier/reviewer loop; Reviewer loop stop rules; review.md with a learned-rules section; Consequence-based risk tiering; First-time-user agent test; Git branch per feature with rollback
- Tools: Claude Code, CLAUDE.md, review.md, eval.md, state.md, Claude Code code review command, skills, subagents, hooks, git, Codex, Cursor

## [This Is Microsoft's New Tool Finally Fixed Claude's Usage Limits](../videos/1kQ_1_QL5Es.md)
`1kQ_1_QL5Es` · AI LABS · 2026-10-29 · q2 · practitioner · review · also: token-cost-efficiency, skills-self-improvement, context-engineering

Walkthrough of Microsoft's Token Economizer, a Claude Code plugin that learns per-project token waste (repeated mistakes, unused tools, stuck loops) and cuts it; reports 21-31% savings and a cold-start caveat.

- Techniques: Install the plugin for your agent; Enable micro skills only for your own projects; Per-project repeated-failure facts; Prune unused tools per project, then restore on demand; Measure the tool-definition overhead; Two-step stuck escalation; Seed a new tool from existing session history; Three-hook layout for an agent harness
- Tools: Token Economizer (Microsoft; Claude Code and Codex plugin, install from GitHub repo, version not stated), Claude Code, Codex (OpenAI), GitHub Copilot, Sonnet 5, Opus 4.8, Graft (map-based token saver, mentioned as a comparison, not shown in use), Data Impulse (sponsor; residential proxy network)

## [Your PS5 Can Now Run Open Models (And It's Surprisingly Fast)](../videos/TgmC_VZEKTE.md)
`TgmC_VZEKTE` · Kai Explains · 2026-10-27 · q4 · practitioner · review · also: local-ai, inference-serving

A viral claim that a PS5 runs a 27B open model at 20 tokens/s, checked against a 613-second Claude Code first prompt. The lesson: prefill (reading) speed, driver limits and OS sandboxing decide agent usefulness more than writing speed.

- Techniques: Split latency into prefill and decode; Estimate decode ceiling from bandwidth; Use a smaller model for agent/harness work; Chunk long prompts to avoid GPU watchdog timeouts; Multi-token prediction for decode speedup; Serve a household local API
- Tools: PS5LM (llama.cpp port for PS5; started by Mert Kobanov Oct 1; fork PS5LM+ by ABI245E; the two later merged), llama.cpp, llama.cpp Vulkan build (RedStapler, Linux), RADV (Mesa Vulkan driver, ported to PS5), Unsloth UD-IQ2 2-bit quant (6.8 GB; 9.2 GB sibling), Qwen 27B dense model (Apache 2.0, released Aug by Alibaba; caption reads 'Quen 3.827B'), Qwen 9B (4-bit on PS5 Slim, 55 tokens/s; caption reads 'Quen 3.59b'), Qwen 8B Flash Next (caption reads 'Quen 3.8 Flash Next'; the host says 180B parameters, split across PC and PS5), Gemma 4B (61 tokens/s, reads images; caption reads 'Gemma 44B'), Llama 3.2 3B (124 tokens/s), Claude Code, Relapse (PS5 jailbreak, firmware 7.00-13.60, public Sep 29)

## [EGM: Google's New Way To Use Claude Code Is Insane](../videos/xxf6D9jynFw.md)
`xxf6D9jynFw` · AI LABS · 2026-10-26 · q2 · practitioner · tutorial · also: context-engineering, multi-agent, coding-agents

Walkthrough of Google's EGM, a spec-first workflow where zero-context goldfish sub-agents critique a plan before any code is written, with install, bootstrap, review and drift steps for Claude Code. A sponsor segment caps quality.

- Techniques: Isolated-context plan critique; Multi-lens rubric reviewers; Fan-out with a single merged report; Staged plan authoring with per-section approval; Round-based review gate; Drift check against per-folder docs; Make per-folder docs agent-readable; Verify the installer's CLAUDE.md edits; Install by agent-specific command or by prompt; Command sequence
- Tools: EGM (Google Elephant Goldfish Model, free on Google's GitHub), Claude Code, Codex (named as a supported agent), Hydra (sponsor, video generation for app promos)

## [Anthropic Just Revealed How Their Engineers Use Claude Code](../videos/92ZDgn8bgLM.md)
`92ZDgn8bgLM` · AI LABS · 2026-10-22 · q3 · practitioner · tutorial · also: context-engineering, multi-agent, testing-verification

AI Labs video on Felix Rieseberg's article: get more from Claude Code by asking for outcomes, expert methods, varied viewpoints, an outside judge, and the tools to verify results.

- Techniques: Outcome-first prompt (altitude); Expert-method meta-prompt (depth); Impossible-sounding goal reframing; Outside judge via a second model; Noun-to-verb role discovery and sequential specialist sub-agents (range); Verification resources for agents
- Tools: Claude Code, Claude (Anthropic), Codex CLI, MCP (Model Context Protocol), GoLogin (sponsor segment, not a recommended tool), AI Labs Pro (paid community, mentioned in closing)

## [AI Just Made Physics Interactive. This Is Insane. (Anatomy)](../videos/lyGYidIZK4I.md)
`lyGYidIZK4I` · Better Stack · 2026-10-22 · q3 · practitioner · review · also: skills-self-improvement, coding-agents, token-cost-efficiency

Better Stack demos "anatomy", an agent skill that explains concepts as physical machines in interactive HTML/SVG/React figures; useful, but very slow, token-hungry, and its metaphors need checking.

- Techniques: Install and invoke the anatomy skill; Truth-first figure generation; Steering the output with modifiers; Verify the metaphor and the draft; Budget before running
- Tools: anatomy (Claude skill, tool name as spoken in the video), skills CLI, Claude Code, Codex, OpenCode, Antigravity, Chrome, WebGL, React, SVG, Mermaid, D2

## [Anthropic Barely Reads Claude's Code Anymore](../videos/d8QpDbBKbAU.md)
`d8QpDbBKbAU` · Better Stack · 2026-10-20 · q4 · practitioner · news · also: pr-code-review, evals, multi-agent

Secondhand summary of how Anthropic reviews Claude Code's own PRs: layered automated review, risk-tiered human sign-off, incident-derived reviewer evals, and round caps for agent-vs-agent loops.

- Techniques: Layered review pipeline with a voting gate; Turn repeated reviewer findings into durable rules; Per-directory review.md written by code owners; Merge gate with explicit false-positive dismissal; Incident-derived reviewer eval with a keep-or-drop rule; Noise metric from comment outcomes; Round cap, scoped re-review, and whole-class flagging for agent loops; Risk tiering with a classifier agent and a second check
- Tools: Claude Code, CLAUDE.md, review.md, PR template, lint rules, CI (tests, type checking, linting)

## [Vercel's CEO Just Unveiled The Greatest AI Coding Workflow Ever](../videos/y2ifUC9_zuU.md)
`y2ifUC9_zuU` · AI LABS · 2026-10-20 · q2 · intro · tutorial · also: context-engineering, testing-verification, security-guardrails

Recap of a Vercel CEO interview: judge progress by direction rather than volume, run a plan-drift "direction" check, and use breaker, first-time-user and E2E agents plus MCP-based feedback triage. Partly a sponsor segment, with thin detail.

- Techniques: Direction drift-check command; Specs-first project setup; Must-not-trade-off rules with runnable tests; Quality gate checklist; Breaker agent loop; First-time-user agent with a hook-restricted bash tool; E2E path agent with JSON results; DeepSec security scan; Feedback triage with MCP connectors
- Tools: Claude Code, CLAUDE.md, DeepSec (Vercel security scanner), Gmail MCP, Sentry MCP, Victor (sponsor, AI hire in Slack/Teams)

## [Why Your Mac Is Slow at Local AI (And It's Not the Chip)](../videos/x_qmqqp6d7s.md)
`x_qmqqp6d7s` · Kai Explains · 2026-10-19 · q4 · practitioner · tutorial · also: local-ai, inference-serving, token-cost-efficiency

Kai Explains on why local AI on a Mac feels slow: prompt prefill and prefix-cache misses, not memory bandwidth, dominate agent turns, and a settings checklist finds the cache-breaking causes.

- Techniques: Split prefill from decode when measuring; Audit cache-token counts per turn; Raise server log verbosity to find cache misses; Check Ollama's context window; Pin the Claude Code version and attribution header; Keep thinking tokens in history; Lower reasoning effort on Qwen models; Test frontends against the same server before committing
- Tools: Claude Code, Ollama, LM Studio, llama.cpp, Qwen 27B (dense model; spoken as 'Quen 27B'), Qwen 3.8 27B as spoken ('Quen 3.827B'; name likely garbled by captions, unverified), OpenClaw (agent frontend), Hermes (agent frontend), Xcode (passing example app), Apple M5 Max, M5 Pro, M5 chip, M4 Max, M1 Max (hardware), Mac Mini 'M6' (as spoken at 1:26; likely a caption or naming error, unverified)

## [GitHub's #1 Trending Skill Is Insane (5 Use Cases)](../videos/rw0fqnrZgNM.md)
`rw0fqnrZgNM` · AI LABS · 2026-10-19 · q2 · practitioner · review · also: skills-self-improvement, testing-verification, security-guardrails

Walkthrough of the Reverse Engineer Anything (REA) MCP skill for Claude Code: feature cloning, black-box QA, competitor teardown, security sweep. Takeaway: tag findings by evidence, not guesses.

- Techniques: Behavior spec before implementation; Evidence-tagged findings; Black-box feature QA; Check the site against your written rules and promises; Competitor teardown; Pre-publish security and performance sweep
- Tools: Claude Code, Codex, Reverse Engineer Anything (REA) MCP server and skill, Hopper (binary analysis, optional), Firecrawl MCP server (sponsor), Notion MCP, Obsidian, Notion, OpenAI API, Stripe, GitHub

## [This Just Fixed Your Claude Code Setup's Biggest Flaw](../videos/jlEMo6Dsh9E.md)
`jlEMo6Dsh9E` · AI LABS · 2026-10-12 · q2 · practitioner · review · also: testing-verification, context-engineering, token-cost-efficiency

Walkthrough of eight Claude Code add-ons, mostly from one vendor, that put an LLM yes/no judge at decision points: action gating, rule checks, stop gates, message routing, compaction, file shortlisting and SEO audits.

- Techniques: Judge-gated pre-action hook (Toolgate pattern); Rules-to-rubric compilation (Abide pattern); Completion gate with a confidence threshold (Belay pattern); Three-way routing of mid-run messages (Steer/Queue/Interrupt); Advised compaction timing; Shortlist-then-read file retrieval (Quicksilver pattern); Browser-driven test pass with judge verdicts; Site audit with a fixed checklist plus per-page judgment
- Tools: Claude Code, Codex, Jev (decision model; name as transcribed, provider TypeSafe), Toolgate, Abide, Jev Browser, Jev Belay, Jev Steer/Queue, Compact Advisor, Quicksilver, Jev SEO, OpenRouter

## [Claude Mods Are Insane... You Need To Try These Right Now](../videos/ERNqRK6sMJY.md)
`ERNqRK6sMJY` · AI LABS · 2026-10-12 · q3 · practitioner · review · also: context-engineering, multi-agent

AI LABS demos seven Claude Code "mods" they built (prompt enhancer, design picker, assumption reviewer, idea shelf, session dashboard, same-folder tracker, plain-language answers) and explains how to create and install them.

- Techniques: Build a mod from a prompt; Prompt enhancer before send; Assumption ledger with targeted correction; Visual option picker before a design choice; Two-pass answer rewrite with a cheap check
- Tools: Claude Code, Claude mods (Claude Code feature), plugin-authoring skill, Haiku model (answer rule check), Runway, Gen-4.5 (Runway video model, sponsor segment), Stride (AI LABS' own running-coach app, sponsor segment)

## [Claude Code Features That 90% Don't Know Exist](../videos/i6Q7bXnWGlM.md)
`i6Q7bXnWGlM` · AI LABS · 2026-10-12 · q3 · practitioner · tutorial · also: context-engineering, token-cost-efficiency

Walkthrough of about 20 hidden Claude Code settings, commands and shortcuts for context hygiene, permissions, plan mode, multi-session work and model routing, with exact setting names.

- Techniques: Enable New Init; Import setup from another agent; Prompt audit after a model release; Prune skills by token cost and usage; Auto Mode Setup; Fewer permission prompts allowlist; Disable connectors and artifacts; Build eval and hillclimb for LLM apps; Clear context on plan accept and save plans in-repo; Output styles; Show thinking summaries; Focus mode; Branch, fork and subtask; Cross-session messaging; Ask User Question Timeout and notifications; opusplan model routing; Pin sub-agent model; Prompt-editing shortcuts
- Tools: Claude Code, Claude app (connectors, artifacts), Claude.md, Claude API command (prompt audit, build eval, hillclimb), Codex, Cursor, Opus, Sonnet, Scrimba Explain (sponsor)

## [Do Claude Get Quietly Nerfed After Launch..(We Have Proof)](../videos/SxLUx8-hN1o.md)
`SxLUx8-hN1o` · Kai Explains · 2026-10-12 · q4 · practitioner · review · also: evals, token-cost-efficiency, models-research

Claude "nerfs" are usually config changes (effort defaults, harness bugs, silent model fallback) rather than weight changes; track output tokens, tool calls and app version alongside any score.

- Techniques: Pin and set effort explicitly per model; Disable silent model switching in Claude Code; Choose effort by task type; Mine local session logs for token and tool-call metrics; Regression diagnosis by three signals; Multi-sample tracker with a detection threshold
- Tools: Claude Code, Claude Opus 5.5, Claude Opus 5, Claude Opus 4.6, Claude Opus 4.7, Claude Opus 4.8, Claude Sonnet 4, GPT-6 Astra (as named in the talk), LiveNerf (daily tracker), Nerfbench (daily tracker), MarginLab (daily SWE-Bench Pro tracker), SWE-Bench Pro

## [You're Prompting Opus 5.5 Wrong (Anthropic's Guide to Mastering Opus 5.5)](../videos/5TNXByrtHc4.md)
`5TNXByrtHc4` · Better Stack · 2026-10-12 · q3 · practitioner · tutorial · also: context-engineering, multi-agent

Better Stack walkthrough of Anthropic's Opus 5.5 prompting guide: state the finish line up front, drop "think carefully" lines, steer with CLAUDE.md stop rules, split audits across subagents, track tasks in a file, and handle safeguard flags.

- Techniques: One-message task with explicit finish line; Remove thinking-nudge lines; Ban specific styles for design; Queue follow-ups during a run; CLAUDE.md stop-rule; Sub-agent split with evidence check; tasks.md progress file; Structured end-of-run summary; Merge-blocker diff review; Cross-model review; Recover from safeguard flags; Answer quickly prompt
- Tools: Claude Code, Claude Opus 5.5, CLAUDE.md, tasks.md, OpenAI model (named Astra in transcript)

## [From Vibes to Production: Evaluating and Shipping AI Agents That Work 201 — Laurie Voss, Arize AI](../videos/F0TNSmbo5hE.md)
`F0TNSmbo5hE` · AI Engineer · 2026-10-06 · q2 · practitioner · workshop · also: observability, evals, software-factory

Arize workshop on closing the agent improvement loop: instrument an OpenAI Agents app with OpenInference, have a coding agent mine traces and patch failures, then automate it with Arize Signal. Vendor-heavy.

- Techniques: Turn on OpenInference tracing for an agent app; Install vendor agent skills into the repo for the coding agent; Trace triage that looks past error status; Single-problem fix loop with re-verification; Triage automated findings into issues, dataset rows, evaluators or PRs; Regression and guardrail evals before merging an automated fix
- Tools: Arize AX, Arize Signal, Alex (Arize in-product assistant), OpenAI Agents SDK, OpenInference, Arize AX CLI, Claude Code (VS Code extension), npx skills (arise-ai skills), npm, GitHub, WonderToys demo app (Arize sample)

## [Lifestyles of the AI-Native — Nick Nisi & Zack Proser, WorkOS](../videos/AgBAOXVxt4A.md)
`AgBAOXVxt4A` · AI Engineer · 2026-10-06 · q3 · practitioner · workshop · also: coding-agents, testing-verification, context-engineering

WorkOS engineers run a hands-on workshop on operating fleets of Claude Code agents: voice dictation, goal vs loop, verification hooks, Codex adversarial review, worktrees and scheduled tasks.

- Techniques: Goal with a measurable done condition; Loop for recurring or open-ended monitoring; Checksum-verified evidence of test runs; Hook-enforced gates; Cross-model adversarial review; Retrospective agent with curated memory; State machine for ordered steps; Git worktrees for parallel agents; Interactive first, then schedule; Session fleet management; Triage automated PR review output by score
- Tools: Claude Code, Codex CLI, Handy, WhisperFlow, Granola, Greptile, CodeRabbit, Devin, Linear, Slack, tmux, Fleet (nicknesey/fleet)

## [Claude Code Mods Can Do Basically Anything...](../videos/EiThSVZ8pME.md)
`EiThSVZ8pME` · Better Stack · 2026-10-05 · q3 · practitioner · review · also: agent-architecture, dev-tools

Better Stack demos Claude Code "mods," in-process TypeScript plugins that can draw panes, status lines and rewrite events, by building a subscription-usage HUD and a Haiku-powered fake chat.

- Techniques: Build a status-line HUD mod by prompting; Map usage meters to status-bar stats; Read undocumented usage data from the /usage endpoint; Reactive commentary from Haiku; Terminal image fallback; Reopen a closed mod pane with a slash command; Persist a mod across sessions
- Tools: Claude Code, Claude Code mods, Claude Code hooks (comparison), TypeScript, Claude Haiku, Claude desktop app, /usage slash command, /backseat slash command, AGENTS.md support, diff pane

## [He Finally 10x Claude Code With This Method](../videos/qLfSDQ5NGh0.md)
`qLfSDQ5NGh0` · AI LABS · 2026-10-05 · q3 · practitioner · tutorial · also: testing-verification, skills-self-improvement, multi-agent

Walkthrough of a Karpathy-style loop for Claude Code: frozen checks, fresh builder subagents, and an outer loop that rewrites instructions from failure logs. The "10x" claim is not measured.

- Techniques: Loop-fit test before building a loop; Project-context skill as app memory; Write, review, approve, lock, and commit checks; Fresh feature-builder subagent per feature, with a results file; Karpathy-style keep-or-undo loop with program.md; Outer auto loop that rewrites instructions from failures; Wire-up and sweep instructions
- Tools: Claude Code, Karpathy autoresearch (Auto Research), Upstash Box (sponsor; per-agent cloud sandbox), Approve Checks (custom script), program.md, features.md (feature tracking file), results file (custom per-round log), Project Context skill (custom), build skill (custom), write checks skill (custom), auto loop skill (custom), feature builder agent (custom subagent)

## [Shopify Just Released The Greatest AI Coding Workflow Ever](../videos/bBMp5tLxShQ.md)
`bBMp5tLxShQ` · AI LABS · 2026-10-02 · q2 · practitioner · tutorial · also: software-factory, multi-agent, testing-verification

AI LABS rebuilds Shopify's checkpoint-and-gates agent loop as a Claude Code orchestrator skill; the key idea is enforcing gates with a stop hook, not advisory rules.

- Techniques: Checkpointed build with human plan approval; Stop-hook gate; Test-first behavior gate without a browser; Prototype-driven visual gate; Adversarial critic and fixer loop; Learnings file for cross-task feedback; Single orchestrator entry skill
- Tools: Helix (Shopify internal, not released), Claude Code, Claude sub-agents, Gemini (used by Shopify as UI reviewer), Hedra MCP server (sponsor segment), design.md, Ralph loop (transcribed as RALF), AI LABS orchestrator skill (their own), Checkpoint Planner agent (their own), tdd planner skill (modified, their own), prototype skill (their own), adversarial loop skill (their own)

## [Your AI Agent Just Changed 40 Files... Now What? (Whiteboard)](../videos/cP5PRDo3u6Q.md)
`cP5PRDo3u6Q` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: pr-code-review, coding-agents, dev-tools

Walkthrough of Whiteboard, an open-source Mac app that lets a coding agent draw linked review diagrams of its own branch changes, with a privacy warning about its default telemetry.

- Techniques: Install Whiteboard as a Claude Code plugin; Turn telemetry off before opening a private repo; Review-only prompt with tool-call approval; Click-through verification of diagram blocks; Typed diagram blocks instead of free-form output; Diff reduction for large agent branches; Own-backend OpenTelemetry instead of vendor telemetry; Check trace storage before enabling trace capture
- Tools: Whiteboard (open-source Mac app, MIT, VS Code fork), Claude Code, Codex, Cursor, OpenCode, VS Code / Code OSS, Electron, Rust (diff engine), MCP, Mermaid, Archify, CodeRabbit

## [Claude Code Can Now Take Your App Live (GoLive)](../videos/HTscIrJhjDs.md)
`HTscIrJhjDs` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: dev-tools, security-guardrails

Walkthrough of GoLive, an early agent skill plus Node CLI that takes a repo live (Vercel, Supabase, Resend, Stripe) via plan, approve, apply, verify gates, with candid caveats about consent and credential storage.

- Techniques: Plan-then-approve-then-apply with a plan ID; Verify webhooks both negatively and positively after deploy; Separate confirm flags for destructive, DNS and production-live actions; Refuse-list for paid or account-creating actions; Ownership-tagged teardown; Borrow existing CLI logins instead of minting credentials; Post-run written report with no secrets; Skill file plus a small CLI, not an MCP server
- Tools: GoLive (agent skill plus Node CLI; repo name not shown in the transcript), Claude Code, Codex, Vercel, Netlify, Supabase, Neon, Resend, Stripe (test and live modes), Terraform, SST, Lovable

## [Agent Harness explained in 8min.. Why its more Important then AI Agent](../videos/qXo1P5H2RXk.md)
`qXo1P5H2RXk` · Kai Explains · 2026-10-02 · q3 · intro · talk · also: agent-architecture, context-engineering, token-cost-efficiency

Explainer building an agent harness from scratch (agent loop, context management, permission gate, config) and arguing that the harness, not the model, now drives much of a coding agent's score and cost.

- Techniques: Minimal agent loop; Externalize state and use clean-context sub-agents; Harness-owned permission gate; One git work tree per agent; Move repeated instructions into configuration; Audit tool-description overhead; Compare harnesses by trips per task, not only by score
- Tools: Claude Code (Anthropic), Codex (OpenAI), Cursor, Cline (auto-caption reads 'Klein'; the open-source repo is discussed), Anthropic model card (benchmark scaffold footnote), git work trees, NVIDIA H200 (hardware, mentioned as a comparison, not used)

## [LangGraph vs OpenAI Agents SDK vs Claude Agent SDK](../videos/8C3LB6TPxwk.md)
`8C3LB6TPxwk` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: agent-architecture, multi-agent, governance-compliance

A practitioner comparison of LangGraph, the OpenAI Agents SDK and the Claude Agent SDK: the architectures have converged, but licensing, billing, language support, version stability and data-retention terms are what should drive the choice.

- Techniques: In-distribution test for harness choice; Pick by constraint, not by benchmark; Read the terms section before building; Verify checkpoint and resume claims against release notes; Measure latency on a representative task early; Trace handoffs as tool calls
- Tools: LangGraph, LangChain middleware, OpenAI Agents SDK (0.22; 0.14, 0.20 referenced), Claude Agent SDK (Python and TypeScript; 0.2.x patch 152), Claude Code (transcribed as 'clawed code'), Claude managed agents, OpenAI managed deep agents (public beta, US, CLI first), Microsoft AutoGen, Google ADK, Microsoft's new agent framework (unnamed), Postgres checkpointer (LangGraph), GPT-4o (transcribed as 'GPT-40')

## [Your AI Subscription Is Now Worth Less](../videos/FWShtLCP4OY.md)
`FWShtLCP4OY` · Kai Explains · 2026-10-02 · q3 · practitioner · other · also: token-cost-efficiency, context-engineering, governance-compliance

Why Claude's Max-plan limits feel smaller: unpublished capacity fractions, per-turn overhead from CLAUDE.md and MCP servers re-billed every turn, and default high reasoning effort. Practical fixes included.

- Techniques: Read the floor before a session; Prune idle MCP servers; Set reasoning effort per task instead of leaving it on high; Ask for markdown when fetching docs; Write specific prompts with form and constraints; Measure what an hour of your work costs
- Tools: Claude Code, Claude Pro, Claude Max 5x, Claude Max 20x, CLAUDE.md, MCP servers, Extended thinking (reasoning effort setting), Limit Reset command, Low Priority Mode, OpenAI Codex, GitHub Copilot

## [Insane Jev Use Cases You Need To Use Right Now](../videos/2nc_QMuNp18.md)
`2nc_QMuNp18` · AI LABS · 2026-10-02 · q2 · practitioner · review · also: token-cost-efficiency, context-engineering, pr-code-review

AI LABS shows seven Claude Code workflow hooks that offload yes/no, ranking and routing decisions to "Jev", a decision-only model with a confidence value, to cut latency and token spend.

- Techniques: Decision-model offload via gateway; Compaction replacement via project-local hook; Doc-rule to test coverage hook; Per-prompt skill picker hook; Keyword search then batched LLM rerank for Explore; Seven yes/no review gate; Browser agent with model-picked clicks; Pre-edit rule enforcement hook
- Tools: Jev (TypeSafe decision model, as auto-captioned), Vercel AI Gateway, OpenRouter, Claude Code, Codex, Fast Jev Compaction plugin, Claude Code Explore subagent, Opus (caption reads 'Opus 2'), Zapier (sponsor segment)

## [Claude Code + GPT 6 Astra Just Killed AI Video Editing](../videos/p565AqELA8M.md)
`p565AqELA8M` · AI LABS · 2026-10-02 · q2 · practitioner · tutorial · also: coding-agents, voice-multimodal, token-cost-efficiency

Tutorial for making agent-generated product videos in Claude Code: plan first, review in the browser, render shots one by one, then add music. Sponsored in part, and the title oversells it.

- Techniques: Route Claude Code to a Codex subscription via a local proxy; Plan-first with browser preview, comments, and an explicit lock; Render shots individually at full resolution, approve, then fix; Polish and combine with explicit timing; Music skill driven by plan style and shot cadence
- Tools: Claude Code, GPT-6 Astra (OpenAI model, accessed through Codex), Codex, CLI Proxy API, Homebrew (brew), Hyperframes (video-creation tool with skills), Mixkit (free music library), Luma Ray 3.2 (sponsor), Ray 3 (comparison), Kling 3.0 (mentioned in sponsor segment), Gen 4.5 (mentioned in sponsor segment), Fable (model compared to Astra on design in an earlier video)

## [You Are Using Fable 5.1 Wrong (Do This Instead)](../videos/7au4tWVG8a0.md)
`7au4tWVG8a0` · AI LABS · 2026-10-02 · q3 · practitioner · review · also: token-cost-efficiency, context-engineering

Practical tips for getting better results and lower cost from Anthropic's Fable 5.1 in Claude Code: lower effort, prune old-model instructions, scope edits, and give whole-feature prompts. Mostly anecdotal.

- Techniques: Start at low effort and escalate only on evidence; Ablation test to prune CLAUDE.md; Unattended-run preamble; Explicit scope fence; Minimal-diff editing instruction; Remove mannered prose; Whole-feature prompts instead of step-by-step prompts
- Tools: Claude Code, Fable 5.1, Fable 5, Opus 5, CLAUDE.md, Claude API prompt audit (command name as spoken; exact invocation not shown), Artificial Analysis (independent model benchmarking), Porkbun (sponsor, domain registrar)

## [How To Use Claude Code To Build Amazing Sites With Opus 5.5](../videos/DP7mgLUKN_U.md)
`DP7mgLUKN_U` · AI LABS · 2026-10-02 · q3 · intro · tutorial · also: vibe-coding-app-building, pr-code-review, context-engineering

Six-stage tutorial for building non-generic websites with Claude Code: plan mode, CLAUDE.md business context, a design-rules skill, design.md, git/GitHub/Vercel deployment, branch + PR review, and a 3D scroll skill.

- Techniques: Plan mode before building; Enrich CLAUDE.md with business context; Install and apply a design-rules skill to an existing project; Lock visual style with design.md; Commit checkpoints and set up GitHub via the CLI; Deploy from GitHub to Vercel; Feature branch, PR, and automated review loop; Scroll-driven 3D site via ScrollWorld skill
- Tools: Claude Code, Opus 5.5, Sonnet, Fable, Warp, VS Code, Next.js, Vercel, Vercel CLI, GitHub, GitHub CLI (gh), CodeRabbit

## [We Let Claude Code and Codex Race Human Researchers — Elie Bakouch, Prime Intellect](../videos/oVsEddfhdxc.md)
`oVsEddfhdxc` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: coding-agents, models-research, evals

Prime Intellect's Elie Bakouch runs Claude Code and Codex on an optimizer speedrun against human records, finding both beat the records but neither produced a novel optimizer, and that Claude Code idled while Codex kept working.

- Techniques: Speedrun as a verifiable research environment; Constrained variants to force novelty; Goal file plus rules file as the agent's contract; Restart with the latest best state; Behavior logs normalized by active time; Generator, judge and scale-up loop
- Tools: Claude Code, Codex, Slurm, AGENTS.md, goal.md, Verifiers, Prime-RL, Hosted Training, Kimi K2.7, GLM

## [The Era of Compound Engineering — Kieran Klaassen, Every/Cora](../videos/_ehJyfHg1Vk.md)
`_ehJyfHg1Vk` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: skills-self-improvement, software-factory, context-engineering

Kieran Klaassen (Every/Cora) on compound engineering: extract your judgment and repeated corrections into repo knowledge so each feature makes the next one easier, with a demo of his open-source plugin's commands.

- Techniques: Compound engineering loop; Ideation against strategy docs; Doc review for sharp questions; Brainstorm with minimal questions; Unattended end-to-end run (/lfg); PR polish with explanation; Extract a design rule from a review fix
- Tools: Claude Code, Codex, Cursor, Claude Cowork, Linear, GitHub, Slack, Intercom, Rails, React, MCP

## [Tethered: Our Agents Are Us — Shu Fang, Two Sigma](../videos/wCIYViPd4SU.md)
`wCIYViPd4SU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: security-guardrails, enterprise-adoption, observability

Two Sigma explains how it runs cloud agents as each employee's own identity, using a propagated attribution header and enterprise-grounded web search to cut exfiltration risk.

- Techniques: Run agents as the user identity in existing per-user namespaces; Propagate an attribution header like a trace ID; Deny native web tools and route through enterprise grounding; Enforce tool behaviour with existing harness primitives
- Tools: Claude Code, Google Web Grounding for Enterprise, MCP CLI, Kubernetes, Brave Search (native web tool in Claude Code, per speaker)

## [Every Level Of Claude Code Loop Engineering Explained](../videos/PLyRe6Zk--8.md)
`PLyRe6Zk--8` · AI LABS · 2026-09-02 · q4 · practitioner · tutorial · also: software-factory, agent-architecture, testing-verification

A three-level walkthrough of "loop engineering" in Claude Code: spec-as-/goal for one feature, a queue-driven software factory with a separate adversarial reviewer per branch, then phone control of the loop. Substantive, with the skills and steps shown.

- Techniques: Spec file as a /goal with explicit verification; Queue-file tracker for overnight multi-feature runs; Builder and adversarial verifier split; Clickable HTML mock per feature as planning and verification oracle; PR as the human approval gate; CLI-based platform setup driven by the agent; Minimal CLAUDE.md that points at AGENTS.md; Mobile control of a laptop-resident Claude Code session
- Tools: Claude Code, /goal (Claude Code slash command), /loop (Claude Code slash command), Codex (said to work with the same system), GSAP, Next.js, GitHub (and gh-style CLI), Supabase (and its best-practices skill), Vercel (and deploy-to-Vercel skill), Warp, VS Code, Paseo

## [Insane Claude Design Skills You Need To Actually Build Beautiful Sites](../videos/Ysr7oNDajJI.md)
`Ysr7oNDajJI` · AI LABS · 2026-09-02 · q2 · intro · review · also: skills-self-improvement, product-ux

AI LABS walks through design-focused agent skill packs (Emil Kowalski, Conard Lee, Elia Design, Meng To, Jakub Krehel, Tastemaker, perception laws) for Claude Design and says they steer models away from generic layouts. Mostly an overview; little measured evidence.

- Techniques: Install and invoke a design skill in Claude Design; Layer skills by stage; Score-and-iterate loop; Regression-aware review via GitHub; Script-based reference extraction; Landing-page as one-action structure; Install only the skills that fit your workflow
- Tools: Claude Design, Claude Code, Codex, GitHub, Emil Kowalski design skills (design-engineering skill, Animate, Apple Design, animation vocabulary), Conard Lee garden skills (web design engineer skill), Elia Design landing-page skill, Meng To skills (video-to-prompt, awards-quality sites), Jakub Krehel skills (review, better layout), Tastemaker, screen critique skill, perception laws skill

## [This Claude Code Skill make Building 10x Faster](../videos/b9k-AE4v5yI.md)
`b9k-AE4v5yI` · AI LABS · 2026-09-02 · q2 · practitioner · review · also: skills-self-improvement, multi-agent

AI LABS walks through two Claude Code/Codex skills: one checks existing products and open-source projects before building, and one searches academic papers when nothing is shipped yet. Also covers a publish-once skill distribution setup. Partly a promo.

- Techniques: Clarify-then-search gate with logged assumptions; New-idea vs existing-project branch; Applicability-vs-scale notes for each prior-art project; Three-stage cost check; Install a skill from a GitHub link; Paper-per-sub-agent research fan-out; Publish-once, auto-pull skill distribution; Cheap-first, escalate-on-novelty cascade
- Tools: Claude Code, Codex, GitHub, Advise Project Approach (skill), NeuroArchive (skill), Head Start (skill), skills CLI, Claude Code plugins, Archive (preprint platform), Stream (chat API), Sendbird (chat API), Lovable (sponsor)

## [How To Never Run Out Of Codex and Claude Usage Limits](../videos/jwje1JK8Nqs.md)
`jwje1JK8Nqs` · AI LABS · 2026-09-02 · q3 · practitioner · tutorial · also: token-cost-efficiency, context-engineering, coding-agents

AI Labs walks through 24 tactics for stretching Claude Code and Codex usage limits, from habits (clear, compact, rewind, one big prompt) to settings (model and effort, skill and CLAUDE.md size, memory, bundled skills, output caps, advisor).

- Techniques: Clear between unrelated tasks; Compact with explicit keep-instructions, before breaks; Rewind instead of correcting; Batch changes into one prompt; Turn off automatic session recaps (Claude Code only); Set model per task with /model and effort with /effort; Pin sub-agent model in the prompt, or route automatically with a skill; Keep skills small with reference files; Write a lean CLAUDE.md and per-folder CLAUDE.md files; Check spend with the usage command; Use a CLI instead of an MCP server when the CLI is enough (Supabase example); Turn off memory and bundled skills; Disable or cap sub-agent workflows; Filter passing tests out of tool output with a hook; Cap bash output length; Replace the built-in advisor with a custom on-demand agent; Message between Claude Code sessions with only the relevant part
- Tools: Claude Code, Codex, Claude Opus, Claude Sonnet, Claude Haiku, GPT-5.6 Sol (spoken as GPT 5.6 Soul), GPT-5.6 Terra (spoken; name uncertain), GPT-5.4 Mini, ChatGPT plans (Free, Go, Plus, Pro), Claude Pro and Max plans, Supabase, Supabase CLI

## [This Makes Claude Code Free Forever](../videos/vxrZWbZ2fZA.md)
`vxrZWbZ2fZA` · Better Stack · 2026-09-02 · q3 · intro · review · also: token-cost-efficiency, coding-agents, local-ai

Free Claude Code, an open-source local proxy that keeps Claude Code's interface but sends its requests to a free, cheaper, or local model. Useful for routing easy tasks off premium models; the speaker says it is not a replacement for Claude.

- Techniques: Proxy-based model swap behind an unchanged coding client; Tiered per-task model routing; Bounded refactor as a smoke test for a new model route; Reliability-first fallback to premium model
- Tools: Free Claude Code (FCC), Claude Code, Codex, Pi, NVIDIA NIM, OpenRouter, Opus 5 (model name shown in Claude Code UI)

## [These New Claude Skills Are Actually Insane](../videos/jyLKRN36-Dc.md)
`jyLKRN36-Dc` · AI LABS · 2026-09-02 · q3 · practitioner · review · also: skills-self-improvement, context-engineering, product-ux

AI LABS walks through six new agent skills: a self-improving skill-learning log, a four-rule coding baseline, a logged-in website CLI (OpenCLI), a variant-picker for UI, and two product-business skill sets for onboarding, paywalls, churn and validation.

- Techniques: Per-project learning log for skills; Parent-folder CLAUDE.md for base coding rules; Onboarding and paywall pattern; Cancellation save flow; Logged-in site commands via OpenCLI; Variant exploration for one UI section; Demand validation before building
- Tools: Claude Code, CLAUDE.md, Agent skills, log.md (task-observer output file), OpenCLI, Chrome extension (OpenCLI), Variate skill, Hallmark design skill (mentioned, not shown), Next.js, Supabase, Corey's 48-skill marketing collection, SVG (brand logo format)

## [The Python YouTuber Who Never Missed an Upload in 7 Years | Better Stack Podcast Ep. 19](../videos/90t4HgAFqZU.md)
`90t4HgAFqZU` · Better Stack · 2026-09-02 · q2 · intro · interview · also: coding-agents, models-research, dev-tools

Better Stack podcast with Florian of Neural9 on growing a 500k-subscriber Python channel, daily Claude Code use, the agentic-engineering vs vibe-coding line, and open-weight model claims. Mostly career anecdote, thin on technique.

- Techniques: Minimal, concise CLAUDE.md for Claude Code; Work on a second project while a long agent run finishes; Hand-written proof of concept, then agent implementation; Tiered review: line-by-line for backend, skim for frontend; Learn a new technology by building first; Continue a Claude Code session from a phone; Use uv for all Python package installs
- Tools: Claude Code, Claude Opus 4.8 (as named by speaker), Fable (model, as named by speaker), GLM 5.2 Max (model, as named by speaker), Kimi K3 (model, as named by speaker), LiteRT (Google, formerly TensorFlow Lite), LiteRT.js, TensorFlow, PyTorch, JAX, uv, pip

## [Anthropic's Biggest Lie! (The Harness War)](../videos/_DZ4kJwQ50s.md)
`_DZ4kJwQ50s` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: context-engineering, agent-architecture, evals

Compares Claude Code's compaction-based context handling with Prime Intellect's open-source Prime Agent (an RLM-style persistent kernel plus a self-editing "continual harness"). Vendor-reported benchmarks; the context-rot argument is the useful part.

- Techniques: Single persistent kernel as the only tool; Context as a variable (RLM-style chunked processing); Externalized session state instead of compaction; Continual harness: log failures, promote tactics; Guard self-improvement against reward hacking
- Tools: Claude Code, Prime Agent (Prime Intellect, MIT license, installs via a single curl command on Linux or macOS), Claude Opus 5, IPython kernel, Codex (OpenAI coding harness, mentioned by name), GPT-5.4, Gemini, ARC-AGI-3, LongCoT-Mini

## [Want to Run Your Agents For Hours? Use These 12 Rules for Claude.md](../videos/D4uBfIe7SzA.md)
`D4uBfIe7SzA` · Better Stack · 2026-09-02 · q3 · practitioner · tutorial · also: context-engineering, testing-verification, coding-agents

Warren from Better Stack walks through 12 rules for a CLAUDE.md file so agents can run longer without constant correction: a living failure log, TDD, clarifying questions, strict types, vetted packages, naming, testing, performance, error handling, and architecture notes.

- Techniques: Failure-log CLAUDE.md with an automated update skill; Size budget for CLAUDE.md, with nesting and skills; Tests as the definition of done; Clarify-before-assuming rule; Strict type rules in CLAUDE.md; Dependency vetting rule; Human-style end-to-end and screenshot verification; Endpoint latency budget and database-first queries; Fail-fast error convention referenced from CLAUDE.md; Architecture lookup table in CLAUDE.md
- Tools: Claude, CLAUDE.md, AGENTS.md, Codex, Claude memory, Chrome, iOS Simulator, Playwright, PostgreSQL, Rust, TypeScript, GitHub

## [Agentic Development Security — Ezra Tanzer, Snyk](../videos/cgimkNGNjvU.md)
`cgimkNGNjvU` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails, coding-agents, skills-self-improvement

Snyk on securing agent development in three pillars: the code agents generate, the skills and MCP servers they use, and the actions they take. Mainly a product showcase, with a useful hook-based scanning pattern.

- Techniques: Async post-write scan hook with deferred fix at stop; Steer vs ask policy actions in pre-tool hooks; Static scan of skills and MCP tool descriptions; Per-workspace guardrail profiles
- Tools: Snyk, Claude Code, Codex, Cursor, MCP, Python hooks, VS Code, Electron, ClawHub

## [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](../videos/Z-c11pV_uvU.md)
`Z-c11pV_uvU` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: agent-architecture, context-engineering, multi-agent

Frank Coyle (UC Berkeley) walks through the Claude Certified Architect exam's scenarios and uses each one's anti-patterns to teach agent loops, subagent context isolation, compaction, and non-interactive runs.

- Techniques: Stop-reason-driven agent loop; Three-level CLAUDE.md hierarchy; Single-purpose subagents with minimal tools; Context slicing for critic and reviewer agents; Forked subtask context with summary return; Threshold-triggered compaction; Non-interactive CI runs with batch processing
- Tools: Claude Code, Claude API (messages, stop_reason, tool use), CLAUDE.md, MCP (Model Context Protocol), Message Batches API

## [Claude Code Setup Guide By The Creator Himself](../videos/pGro_uKt-_M.md)
`pGro_uKt-_M` · AI LABS · 2026-08-02 · q2 · practitioner · tutorial · also: context-engineering, evals, token-cost-efficiency

AI LABS walks through Claude Code creator Boris Cherny's setup advice: strip your Claude Code setup to a baseline with each new model, keep only what Claude can't infer, and gate work with evals that can fail. Includes a sponsored segment.

- Techniques: Baseline-then-add-back setup audit; Usage triage; Keep-rule for CLAUDE.md; Doctor audit; Fail-able acceptance checks written first; Built-in headless browser verification; Outcome-first prompting; Escalation ladder for model mistakes; Recurring cloud routines for maintenance
- Tools: Claude Code, CLAUDE.md, Claude Code skills, MCP server, Claude Code hooks, Claude Code plugins, context command (Claude Code), usage command (Claude Code), doctor command (Anthropic), safe mode (Claude Code), headless Chrome, sub-agents

## [Anthropic Just Fixed Graph Engineering's Greatest Flaw](../videos/H7t3uUp3HVw.md)
`H7t3uUp3HVw` · AI LABS · 2026-08-02 · q2 · intro · tutorial · also: testing-verification, multi-agent, skills-self-improvement

Graph engineering fans agent work across parallel nodes but hides failures; the video's fix is layered verification skills built with Skill Creator, plus a fresh-context Opus second opinion.

- Techniques: Install Skill Creator as a plugin; Standalone deep-review skill; Embedded verification skill that runs after each feature; Embedded rule-gate skill; Second-opinion skill via claude -p; Headless browser for visual verification; One skill per review angle, chained by an orchestrator skill; Write build, test and lint commands into CLAUDE.md; Pin the judging node to a stronger model
- Tools: Claude Code, Claude Opus, Claude Haiku, Codex, Skill Creator plugin, verify skill, code review skill, simplify skill, design skill, design.md, second opinion skill, CLAUDE.md

## [Run Claude Code with Ollama for 99% Cheaper AI](../videos/LPDWUWP9SCk.md)
`LPDWUWP9SCk` · Better Stack · 2026-08-02 · q2 · intro · tutorial · also: local-ai, token-cost-efficiency

Better Stack setup walkthrough for pointing Claude Code and OpenCode at a local Ollama server to run open models such as Gemma 4 and Qwen 3.6. Setup only: the "99% cheaper" claim is never measured.

- Techniques: Redirect Claude Code to a local Ollama server; Launch a harness through the Ollama CLI; Pull and run a model from the CLI; Match the model to VRAM when choosing context length; Run Ollama in Docker and call its API
- Tools: Ollama, Claude Code, OpenCode, Codex, OpenClaw, Gemma 4, Qwen 3.6, MiniMax, DeepSeek, GLM, vLLM, LM Studio

## [LangChain Open Sourced Claude Code (Works With ANY Model)](../videos/jtWjkdBNqlk.md)
`jtWjkdBNqlk` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: agent-architecture, memory, multi-agent

Kai Explains reviews LangChain's open-source DeepAgent, a model-agnostic take on Claude Code's harness, arguing it wins for shipping agents to users while Claude Code still wins for personal terminal coding.

- Techniques: Audit your harness against the five-part checklist; Subagents with isolated context returning one summary; Keep agent memory in a store you control; Swap the model behind a fixed harness; Use a lighter agent abstraction for bounded tasks
- Tools: DeepAgent (Deep Agents, LangChain), LangChain 1.0, LangGraph, LangSmith deployment, Claude Code, Claude Opus 4.8 (as stated), Claude Managed Agents, Codex, Cursor agent mode, GPT 5.5 (as stated), PostgreSQL, agents.md

## [Open Source Is Back. Goodbye Claude.](../videos/wOfm7x0i3sw.md)
`wOfm7x0i3sw` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: coding-agents, token-cost-efficiency, multi-agent

Better Stack walkthrough of OpenCode, an open-source terminal coding agent with bring-your-own models and custom subagents, weighed against Claude Code; the cost verdict depends on whether you pay per API token or hold a subscription.

- Techniques: Pin a cheap model to a specialist subagent; Low-temperature review subagent; Same agent definition in one JSON file; Enable LSP for type-aware feedback; Generate AGENTS.md with /init; Plan then build
- Tools: OpenCode, Ghostty, models.dev, big pickle (free default model in OpenCode), GLM 5.2, DeepSeek 4, Claude Sonnet 4, Fable 5 (named as a comparison model), Claude Code, GitHub Copilot (comparison), Design Arena (benchmark), AGENTS.md

## [The Largest Supply Chain Attack Ever Just Infected Go](../videos/lNsSxWQDqaU.md)
`lNsSxWQDqaU` · Better Stack · 2026-08-02 · q3 · practitioner · news · also: security-guardrails, coding-agents, dev-tools

Better Stack explains how the self-replicating npm worm (Shai-Hulud) jumped to a Go module, hiding hooks in Claude Code and VS Code config so code runs on folder open, and lists five hardening steps.

- Techniques: Audit agent and editor config before opening untrusted code; Turn off VS Code automatic tasks; Treat .claude/ and .vscode/ as executable code in review; Short-lived, least-privilege CI credentials via OIDC; Egress filtering on CI runners; Minimum release age for packages; Keep secrets out of plaintext on dev machines
- Tools: npm, Go modules, Claude Code (called 'clawed code' in the auto-captions), VS Code (tasks.json, folder-open tasks), Bun (runtime the payload uses to stage its code), Node.js (runs the setup script), TruffleHog (secret scanner the worm reuses), GitHub Actions (CI workflows named as the risk surface), Socket.dev (security firm that flagged the wave), CrowdStrike, Microsoft Defender, SentinelOne (endpoint products the malware checks for), OIDC (short-lived CI credentials), .npmrc (minimum release age setting)

## [Claude Sonnet 5 is a Disappointment... (Fable is Back Though!)](../videos/JR9emVyAQTY.md)
`JR9emVyAQTY` · Better Stack · 2026-08-02 · q3 · intro · news · also: token-cost-efficiency, models-research

Sonnet 5 review: strong benchmarks, but it uses so many tokens that cost per task exceeds Opus 4.8 despite a lower list price. Also covers Fable 5's return and Claude Code date-string fingerprinting.

- Techniques: Compare models by cost per completed task, not list price; Check the pricing basis of any cost comparison; Compare effort tiers on the same benchmark
- Tools: Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Fable 5, Claude Haiku 4.5, Claude Code, GPT 5.4, GPT 5.5, GPT 5.6 Terra (named; the host says he has no access), Gemini 3.5 Flash

## [All The Types Of Claude Loops Explained In 13 Minutes](../videos/8wsM0euQOvc.md)
`8wsM0euQOvc` · AI LABS · 2026-08-02 · q2 · practitioner · tutorial · also: agent-architecture, multi-agent, testing-verification

AI LABS sorts Claude Code agent loops into five types (stateless, learning, multi-agent review, verification, workflow-improvement) with setup steps; anecdotal, with a sponsor segment.

- Techniques: Goal-command loop with tests as the acceptance criterion; Save-every-working-version rule in CLAUDE.md; Skill-improvement loop (learning loop); Multi-agent review loop with an orchestrator; Implementer vs. scorer verification loop; Workflow-improvement loop with a process optimizer
- Tools: Claude Code, CLAUDE.md, Haiku (completion checker in the goal loop), Ralph loop (named as a stateless loop example), goal command, skill loop command (name as spoken), learning.md, thermonuclear review (review skill, named as spoken), orchestrate command, review loop command, iterate command, JSON files (findings and scores)

## [Kimi K3 Is INSANE with Claude Code (FREE + Local + open Source)](../videos/M48WuCSjmHs.md)
`M48WuCSjmHs` · Kai Explains · 2026-08-02 · q3 · intro · review · also: token-cost-efficiency, models-research, local-ai

Kimi K3 can drive Claude Code through an Anthropic-style endpoint at about a third of frontier price, but 'local' is unrealistic: the full weights need ~1.4 TB.

- Techniques: Swap the backend model under Claude Code via environment variables; Route through OpenRouter for a one-line switch; Acceptance test on a real repo bug before switching; Tiered model routing for cost; Lean on cached input pricing for repeated context; Self-host only with real GPU capacity, for privacy or compliance
- Tools: Claude Code, Kimi K3, Kimi K3 Swarm, Claude Fable 5, Claude Opus 4.8, GPT 5.5, OpenRouter, Artificial Analysis intelligence index, GDPval (transcribed as 'GDP Vol'), Mac Studio, Nvidia H100, Nvidia B200

## [Bonsai runs on iPhone, Claude Browser ,Muse Spark, ARDY by Nvidia, 1X Robot Hand & More AI News](../videos/4TlbzLB3IgE.md)
`4TlbzLB3IgE` · Kai Explains · 2026-08-02 · q3 · intro · news · also: models-research, local-ai, voice-multimodal

Weekly roundup (Aug 2026): Meta Muse Spark 1.1, a built-in browser in Claude Code, Bonsai 27B running in 1-bit on a phone, several open vision and edge models, NVIDIA's ARTI motion model, and 1X NEO's tendon-driven hands.

- Techniques: Open the Claude Code built-in browser; Expect a domain prompt and per-write classifier on external browsing; Run Bonsai 27B locally on Apple or NVIDIA hardware; Interleaved token stream plus silence token for live video; Output format as the task selector for a unified vision model; Mid-generation constraints with a look-ahead window for motion
- Tools: Muse Spark 1.1 (Meta Superintelligence Labs), Meta Model API (public preview), Meta AI app (thinking mode on meta.ai), Claude Code (desktop Code tab built-in browser), Claude Desktop, Bonsai 27B (PrismML), MLX, CUDA, Hugging Face, GitHub, MoSVL Realtime (name as captioned; 11B), X-RopeE positional encoding (as captioned)

## [Facebook's Release Just Gave Claude Code A New Design System](../videos/-HEdqzzYKco.md)
`-HEdqzzYKco` · AI LABS · 2026-08-02 · q2 · practitioner · review · also: context-engineering, vibe-coding-app-building, skills-self-improvement

Walkthrough of Meta's open-source React/StyleX component library (transcribed as "Asterix"), built to be read by coding agents via a CLI, plus a sponsor read and a plug for the presenter's skills.

- Techniques: Install the design system with the package manager; Run the init command to write agent instructions; Prompt for a whole site and let the agent pull from the CLI; Generate a manifest of CLI commands and flags for grounding; Screenshot and fix loop in headless Chrome; Chain a generic anti-slop review skill after the build
- Tools: Asterix (Meta's design system, transcript name; likely a caption misspelling), React, StyleX, shadcn/ui (transcribed as ShadCN), Next.js (App Router and Pages Router), npm, Claude Code, CLAUDE.md, AGENTS.md, globals.css, headless Chrome, AI Slop Detector skill (presenter's AI Labs design system)

## [This Skill Just Made Kimi K3 a 10X Better Designer](../videos/EwTOiqWWqEc.md)
`EwTOiqWWqEc` · AI LABS · 2026-08-02 · q2 · practitioner · review · also: skills-self-improvement, vibe-coding-app-building, coding-agents

Walkthrough of running Kimi K3 inside Claude Code via a local proxy on a Kimi subscription, then using the Hallmark anti-slop design skill to push Kimi, Opus and Codex off their default visual styles.

- Techniques: Run a non-Claude model inside Claude Code via a local subscription proxy; Install Hallmark for the right agent; Invoke a skill manually with its slash command when the model is not Claude; Prompt Hallmark with the three pre-flight answers; Run the audit verb, then pick which findings to fix; Use the study verb, not a clone request; Manage context manually on long design sessions
- Tools: Kimi K3, Kimi Code, Claude Code, Codex, Codex app, CLIProxy API, Hallmark, Next.js, Opus 4.8, Sonnet 4.5, GPT 5.6, Fable 5

## [Claude Code Loop Explained | Loop VS Prompts](../videos/pGS7ku-4Fbs.md)
`pGS7ku-4Fbs` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: agent-architecture, token-cost-efficiency, testing-verification

Walks through Anthropic's "Getting Started with Loops" post for Claude Code: four loop types (turn, goal, time, proactive) defined by who decides when to stop, plus the skill.md, turn-cap and token-control practices that keep loops safe.

- Techniques: Define the stop condition before starting a loop; Write skill.md as a measured verification protocol; Goal loop with deterministic success criteria and a hard turn cap; Choose local or cloud for time-based polling; Fresh-context adversarial reviewer; Pilot, then scale, and monitor spend mid-run; Route models by task
- Tools: Claude Code, /loop, /schedule, /goal, /usage, /workflows, skill.md, Lighthouse (named as a score example), Opus (named as an example of a capable model)

## [Fleet Engineering Is Insane... The Next Evolution Of Vibe Coding](../videos/qxjII6x2yPY.md)
`qxjII6x2yPY` · AI LABS · 2026-08-02 · q2 · practitioner · tutorial · also: multi-agent, sandboxing-execution, coding-agents

Walkthrough for running many Claude Code sessions in parallel: resume and handoff basics, file ownership, background dashboards, git worktrees, issue-driven orchestration, and Docker Sandbox isolation.

- Techniques: Session recovery with continue, resume, recap, export; File ownership by prompt; Plan-mode task decomposition; Handoff documents via the handoff skill; Background sessions and the agent dashboard; Git worktrees per session; Issue-driven background orchestration; Docker Sandbox for isolated execution with clone mode
- Tools: Claude Code, Claude Code plan mode, Claude Code background sessions, Claude Code agent dashboard, handoff skill, git worktrees, OpenAI Symphony, Codex, Linear, GitHub, Docker Sandbox (sbx), Docker micro-VM sandboxes

## [How To Use Claude Fable 5 Better Than 90% Of The People](../videos/GM7-ei-4Xc8.md)
`GM7-ei-4Xc8` · AI LABS · 2026-08-02 · q2 · practitioner · tutorial · also: token-cost-efficiency, testing-verification, multi-agent

How a small AI-coding team runs Claude Fable 5 in Claude Code: keep effort at low-high, plan big and implement small, test-first with a separate test author, and layered code and security review subagents.

- Techniques: Keep effort between low and high; PRD-first planner/implementer split; Subagent routing tiers in CLAUDE.md; Ponytail with a test net; Separate test-author subagent (TDD); Parallel scoped security review; Architecture review subagent; HTML mock-up before build; Pre-merge comprehension quiz
- Tools: Claude Code, Claude Fable 5, Claude Sonnet 5, Claude Opus, Claude Mythos, OpenAI Codex CLI, OpenAI Codex plugin for Claude Code, Ponytail, Cursor Thermonuclear Code Quality Review skill, Claude Code security review GitHub Action, CLAUDE.md, Veed (sponsor)

## [Building Great Agent Skills: The Missing Manual](../videos/UNzCG3lw6O0.md)
`UNzCG3lw6O0` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: skills-self-improvement, context-engineering

Matt Pocock's prerecorded talk gives a four-part checklist (trigger, structure, steering, pruning) for judging and writing agent skills, to escape "skill hell".

- Techniques: Choose user-invoked vs model-invoked per skill; Steps plus reference split with external context pointers; Leading words; Split phases into separate skills to force legwork; Deletion test and sediment audit
- Tools: SKILL.md agent skills, superpowers (comparison skill set), Matt Pocock skills repo (writing-great-skills skill)

## [Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com](../videos/MpZzWMdmQCE.md)
`MpZzWMdmQCE` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: testing-verification, coding-agents, agent-architecture

Talha Sheikh (Checkout.com) argues coding agents need deterministic, shareable verification hooks, not better instructions, and that the real engineering work is designing the verification harness.

- Techniques: Stop-hook deterministic verifier; Fail-and-retry feedback loop; Layered enforcement at multiple points; Language-agnostic check contract; Executor plus advisor loop; Cheap model plus strong harness
- Tools: Claude Code, Claude Code hooks (Stop hook), VectorV1 / Vector Harness, Haiku, Opus, Anthropic Glasswing / Project Mythos (named, not described)

## [Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison](../videos/uU5Gv2h8-9g.md)
`uU5Gv2h8-9g` · AI Engineer · 2026-07-18 · q3 · practitioner · interview · also: pr-code-review, security-guardrails, context-engineering

Anthropic's Thariq Shihipar and Cat Wu, with Simon Willison, on how Claude Code and Claude Tag change team workflows, code review, auto mode safety, and prompt design, with internal claims about PR share and prompt size.

- Techniques: Staged trust ramp for AI code review; Eval-gated model swap; Behavioral evals built from user complaints; Conditional prompt wording over absolute rules; Per-model system prompts; Classifier-based permissions using user intent; Credential injection through a proxy; Fewer tools with distinct functions; Multiplayer channel agent with shared memory; Dogfooding gate before launch
- Tools: Claude Code, Claude Tag, Slack, GitHub, Datadog, FFmpeg, Remotion, Gemini API, Mountain Project, Claude Fable, Claude Opus 4.8, Claude Mythos

## [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON](../videos/4kYl2_mqmnQ.md)
`4kYl2_mqmnQ` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: multi-agent, context-engineering, coding-agents

A KRAFTON engineer runs AI coding agents across three machines, organizes them as a hierarchy, keeps state in files, and lists the five failures and four open problems that followed.

- Techniques: Agent org hierarchy with scoped context; File-backed agent state with handoff folders; Clear-and-reload instead of compaction; Blocking review gateway with approval hook; Force delegation through a CLI harness; Git-based context sync with per-machine partitions; Single always-on control plane and chat router; Boot command that restores the fleet from state files
- Tools: Claude Code, tmux, tmux capture-pane, SSH, Git, Discord, MCP servers, Kubernetes, Linux, macOS

## [Field Guide to Fable — Thariq Shihipar, Anthropic](../videos/9fubhllmsBU.md)
`9fubhllmsBU` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: coding-agents, context-engineering, models-research

Anthropic's Thariq Shihipar gives a practical field guide to working with the Fable model: unhobble Claude with tools, find your unknowns, stay in the loop, and be less reasonable about trade-offs.

- Techniques: Blind-spot pass; Brainstorm via throwaway prototypes; Interview me before building; Reference as the map; Implementation-note log for unknowns; Quiz the agent on its own work; Shrink the system prompt for newer models; Give the agent a tool rather than more context
- Tools: Claude Code, Bash tool, code execution tool, AskUserQuestion tool

## [4 Ways to Actually Build Stunning Websites with Claude Code](../videos/HqD5a2Cae60.md)
`HqD5a2Cae60` · AI LABS · 2026-07-02 · q3 · practitioner · tutorial · also: vibe-coding-app-building, skills-self-improvement, context-engineering

AI LABS walks through four ways to get better websites and UIs from Claude Code: refresh design skills from model prompting guides, use design.md files, plan functional UIs as HTML mockups, and clone existing UIs. Mostly anecdotal, with a sponsor segment.

- Techniques: Refresh a design skill from the model's prompting guide; Mine older prompting guides for dropped fixes; Set effort by task type; Conditionally load a sub-skill from a rule; Apply design.md after generation for marketing pages; Functional UI pipeline: plan, mockups, gallery, port; Consistent variants via a shared design.md; CLAUDE.md as product context and verify contract; Verify with a sub-agent against design.md; Clone a marketing site with a capture CLI and sitemap; Clone an auth-gated app from screenshots
- Tools: Claude Code, Claude, Fable 5, Opus 4.8, Anthropic front-end design skill, design.md, GetDesign.md, GSAP, Single File CLI (as named in the video), sitemap.xml, HTML, CLAUDE.md

## [Headroom: The Netflix Tool That Makes AI Agents 10x Cheaper](../videos/KqdRWE1en8k.md)
`KqdRWE1en8k` · Better Stack · 2026-07-02 · q3 · practitioner · review · also: token-cost-efficiency, context-engineering

Walkthrough of Headroom, an open-source proxy that compresses tool-call output, code and RAG text before it reaches the LLM, with reversible retrieval via hashes. The demo shows 98% savings on one log read, with honest caveats about round trips and low effort.

- Techniques: Run Headroom as a local proxy in front of the model API; Compress tool results explicitly from the Python SDK; Check savings through the proxy stats endpoint; Pair input compression with output brevity; Use Headroom Learn to tune compression from failed sessions
- Tools: Headroom (proxy plus Python and TypeScript SDKs), CompressBase (local plain-text compression model used by Headroom), Claude Code, Claude Agent/SDK (Python), uv, Python 3.12, Rust (proxy internals), jq, Caveman (prompt-based output brevity, covered in another video by a different presenter), Opus (Claude model used in the Claude Code demo), Codex (cross-agent memory feature mentioned), Headroom Learn (feature)

## [PAI: The Life OS for AI-Powered Development](../videos/JukZ7WWtOSg.md)
`JukZ7WWtOSg` · Better Stack · 2026-07-02 · q3 · intro · review · also: memory, skills-self-improvement, context-engineering

Better Stack reviews PAI (Personal AI Infrastructure), a memory-and-skills operating layer on Claude Code. Its value is cross-session continuity; it needs terminal comfort and ongoing upkeep.

- Techniques: Persistent project memory loaded every session; Planning prompt that requires risks, assumptions and verification; One custom skill per role or review type; Fixed action order through a multi-step process
- Tools: Claude Code, PAI (Personal AI Infrastructure), Pulse (PAI local dashboard), Telos (PAI goals/ideal-state file, as named in the video), Fabric (named as a prior project of the PAI creator), SecLists (spelled 'SecList' in captions; named as a prior project of the PAI creator), LangChain (compared against), CrewAI (compared against), Next.js (example skill domain)

## [They Finally Fixed Claude Code's Biggest Problem](../videos/KiTmBtyaeXg.md)
`KiTmBtyaeXg` · AI LABS · 2026-07-02 · q2 · practitioner · review · also: security-guardrails, skills-self-improvement

A walkthrough of NVIDIA's Skill Specter, a scanner for agent skills, plus a Claude Code wrapper that adds an LLM-based second scan through headless mode and a discover-scan-fix loop around skills.sh.

- Techniques: Two-tier skill scan before install; Use Claude headless mode as the LLM judge; Discover, scan, show, fix, rescan loop in SKILL.md; Check tool-name identity at the code-point level; Compare declared behavior with code behavior; Check dependencies against a live bad-package list
- Tools: Skill Specter (NVIDIA scanner, named by the host; version not stated), Claude Code, Claude headless mode (claude -p), skills.sh (skill registry with CLI search), OpenAI API (the AI check's default backend, per the host), Codex (mentioned only in the sponsor segment), Nimblist (sponsor; open-source visual workspace for Claude Code and Codex sessions, with a Kanban board, red/green diffs, auto-generated commit messages, and a mobile app)

## [These Claude Workflows Turn Claude Code Into A Whole OS](../videos/5LnwJyi1il4.md)
`5LnwJyi1il4` · AI LABS · 2026-07-02 · q3 · intro · review · also: coding-agents, multi-agent, token-cost-efficiency

Walkthrough of how Claude Code's pieces (CLAUDE.md, MCP, skills, loops/routines, dynamic workflows) form an "OS", with guidance on when a deterministic workflow beats goal or a plain skill; mostly a sponsored-style pitch with thin hands-on steps.

- Techniques: Start a dynamic workflow; Strict output schemas for sub-agents; Choose workflow vs goal vs skill; Convert a skill from a session; Coding-project OS setup; Second-brain audit workflow
- Tools: Claude Code, Claude Opus 4.8, CLAUDE.md, MCP, Google Calendar MCP, Notion MCP, Deep Research workflow, goal command, loops, routines, hooks, skills

## [Hermes Agent under Claude Code Is Insane](../videos/Sb96po6S67k.md)
`Sb96po6S67k` · AI LABS · 2026-07-02 · q2 · practitioner · tutorial · also: skills-self-improvement, mcp-and-tools, memory

Setup-and-use walkthrough for running the Hermes agent alongside Claude Code: Hermes adds persistent memory and self-evolving skills, and can run as an MCP server, cron-driven monitor, or Claude Code launcher.

- Techniques: Install Hermes and run the manual setup; Onboard Hermes with your context; Expose Hermes to Claude Code as an MCP server; Cron-driven living PRD skill from a Slack channel; Delegate feature work to Claude Code from a Hermes channel; Health-check skill loop for a deployed app
- Tools: Hermes Agent (Nous Research), OpenClaw, Claude Code, Claude Code subscription / non-interactive mode, Anthropic Agent SDK credit (policy claim), hermes setup command, hermes mcp serve command, .mcp.json, user.md and memory.md (Hermes memory files), soul file (Hermes agent personality/instructions), Hermes Skill Hub, Hermes bundled Claude Code skill

## [Why I Quit My Dev Job Before AI Could Take It | Better Stack Podcast Ep. 16](../videos/VuMf2ZVA0RE.md)
`VuMf2ZVA0RE` · Better Stack · 2026-07-02 · q3 · practitioner · interview · also: coding-agents, context-engineering, dev-tools

Better Stack podcast with Dreams of Code's Elliot on leaving dev work, betting on Rust, and practical AI-coding habits: stub-first interfaces, git-staged checkpoints, human-steered architecture.

- Techniques: Stub-first public interface; Hand-built spike before delegating; Git staging as manual checkpoints; Architecture-owner, typing-delegate split; Codec backend abstraction
- Tools: Claude Code, Codex CLI, Cursor, OpenCode, Bun, Zig 0.16, Rust, GPUI, gpui-component, Iced, egui, Tauri

## [MemPalace: The Tool That Makes Claude Stop Forgetting](../videos/kRACHOx1p8s.md)
`kRACHOx1p8s` · Better Stack · 2026-07-02 · q3 · practitioner · review · also: memory, context-engineering, mcp-and-tools

Better Stack demos MemPalace, a local tool that stores coding-agent conversations verbatim and exposes them to Claude Code over MCP so decisions persist across sessions.

- Techniques: Verbatim store plus compact index; Local project memory setup; Claude Code plugin with a memory protocol; Run alongside context mode; Load pointers instead of project lore; Install hygiene for memory tools
- Tools: MemPalace (mempalace; spoken as Mem Palace; version not stated), uv, pip, ChromaDB, SQLite, MCP (Model Context Protocol), Claude Code (captioned as Cloud Code), Claude Code hooks and plugin, context mode, Memzero, Zapp (transcript spelling; product name unverified)

## [Google Replaced The Karpathy's LLM Wiki](../videos/k4sMSsMzX2g.md)
`k4sMSsMzX2g` · AI LABS · 2026-07-02 · q2 · practitioner · review · also: context-engineering, memory, rag-retrieval

AI LABS walks through Google's Open Knowledge Format (OKF), a folder, index.md and YAML-frontmatter convention for markdown knowledge bases, and reports a small team test with lower token use and faster lookups.

- Techniques: Index.md per folder as the agent's entry point; YAML frontmatter with name, description and type on every concept document; Script-first markdown-to-OKF conversion with evals; CLAUDE.md navigation section that documents the bundle; Trial on a Git branch and visualize the bundle
- Tools: Open Knowledge Format (OKF, Google), BigQuery, Claude Code, CLAUDE.md, Obsidian (comparison only), Git / GitHub, Karpathy LLM-wiki pattern (concept, not a product), Google design.md standard (named in passing), Mobbin MCP (sponsor), Cursor, Lovable, v0 (named in sponsor segment), Markdown to OKF skill (the team's own, unnamed script)

## [Loop Engineering Totally 10x Hermes agents](../videos/AQRDjI5owZI.md)
`AQRDjI5owZI` · AI LABS · 2026-07-02 · q2 · practitioner · tutorial · also: agent-architecture, multi-agent, skills-self-improvement

Explains "loop engineering": replacing hand-written prompts with self-driving agent loops, split into deterministic loops (tests as the goal) and non-deterministic loops (UI judged by a skill plus a second verifier model), run on the Hermes agent and Claude Code.

- Techniques: Five-step loop; Deterministic loop with tests as the goal; Adversarial builder/verifier loop for judgment tasks; Explicit verification gates and termination; External state files
- Tools: Hermes agent (always-on agent, self-evolving skills), Claude Code (non-interactive and interactive modes), Claude Code hooks, Ralph loop, Claude goal command, Goal Buddy 2, OpenClaw, GitHub CLI (gh), GPT models (named as verifier, no version given), Claude Opus 4.5 (mentioned), Fable 5 (mentioned, no detail)

## [This Claude Code Plugin Writes 94% Less Code (ponytail)](../videos/2xuFcmUAQUc.md)
`2xuFcmUAQUc` · Better Stack · 2026-07-02 · q3 · practitioner · review · also: token-cost-efficiency, coding-agents, evals

Better Stack tests Ponytail, a Claude Code plugin that applies a YAGNI decision ladder to make agents write less code. Its cost claims come with a caveat, and one A/B test shows fewer lines and lower cost.

- Techniques: YAGNI decision ladder in the agent prompt; Native-first replacement check; Record deferred decisions in a code comment; Benchmark cost next to correctness; Side-by-side A/B of a coding agent with and without a plugin
- Tools: Ponytail (Claude Code plugin; benchmark compares no skill, Caveman, and Ponytail), Claude Code, Caveman, Radix UI (React dialog library, the default-agent choice in the modal example), npm (npm package dialog example), Python server (default-run output, not a named tool)

## [The Top Claude Code Features We Use](../videos/ECQA6oOyfIk.md)
`ECQA6oOyfIk` · AI LABS · 2026-07-02 · q2 · intro · review · also: multi-agent, pr-code-review, token-cost-efficiency

AI LABS walks through the Claude Code features its team uses most (Agent Teams, Advisor, goal, auto mode, worktree sub-agents, review commands, loop, monitor), with a Scalekit sponsor segment and little measured detail.

- Techniques: Adversarial finder/fixer agent team for code review; Cheap executor with strong advisor escalation; Goal-driven run to a verifiable end state; Auto mode instead of skip-permissions; Worktree-isolated sub-agents for design variants; Layered review commands before merge; Daily knowledge-base sync with loop; Anomaly-only monitor for agent logs
- Tools: Claude Code, Claude Agent SDK, Claude Haiku, Claude Sonnet, Claude Opus 4.8, tmux, Scalekit, ChromaDB, Notion, Gmail, Slack, Mac mini

## [Skill issue: Lessons from skilling up coding agents to use Langfuse - Marc Klingen, Clickhouse](../videos/vNCY9kXXyDQ.md)
`vNCY9kXXyDQ` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: skills-self-improvement, observability, evals

Langfuse's founder explains how they built an installable skill that teaches coding agents to add Langfuse tracing and evals, and what they learned about docs, eval checks and auto-tuning skills.

- Techniques: Skill with progressive disclosure; Agent-facing docs surface; Wrap the API as a CLI and advertise --help; Natural-language checks for skill evals; Auto-research loop on a skill with human review; Timestamped skill copies for staleness
- Tools: Claude Code, Langfuse, OpenAI SDK

## [Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer](../videos/zKk7sDMGDEQ.md)
`zKk7sDMGDEQ` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: rag-retrieval, evals, coding-agents

Turbopuffer's Kuba Rogut benchmarks semantic code search as an extra tool for Claude Code, using a windowed-grep baseline and file, line and symbol precision and recall on human-labelled context tasks; semantic search helps precision but the gain is smaller than Cursor's because Claude Code does not know when to call it.

- Techniques: Chunk-embed-index semantic code search as a CLI tool; Windowed file reads as a retrieval baseline; Trajectory-level retrieval evaluation; Inline comments as embedding context
- Tools: Turbopuffer, Voyage code-3, Claude Code, Cursor, TurboGrep, tree splitter

## [Your Attention Is the Bottleneck, Not Your Agents — Zack Proser, WorkOS](../videos/so9l_MwS2yg.md)
`so9l_MwS2yg` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: software-factory, testing-verification, skills-self-improvement

Zack Proser (WorkOS) argues human attention, not agent capacity, is the bottleneck, and shares remote Claude Code from a phone, verification gates, and session-log mining to protect focus.

- Techniques: Three-tier verification ladder for agent output; Closed-loop ticket fixing with explicit done criteria; Remote-controlled session from a phone; Scheduled session-log retrospective; Ticket-tagged overnight agent loop; Parallel large features with worktrees and agent teams; Voice-first brainstorm, then written artifact
- Tools: Claude Code, Claude Opus 4.6, Slack MCP, Linear MCP, GitHub Mobile, Cursor, Codex, Vercel bot, OpenClaw, Twilio, ChatGPT advanced voice mode, git worktrees

## [Anthropic Workshop: Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson](../videos/mR-WAvEPRwE.md)
`mR-WAvEPRwE` · AI Engineer · 2026-06-18 · q4 · practitioner · workshop · also: agent-architecture, multi-agent, testing-verification

Two Anthropic Applied AI engineers explain how long-running agent harnesses evolved, and how a planner, generator and evaluator loop with rubric grading builds multi-hour apps that a single agent loop cannot finish.

- Techniques: Generator-evaluator loop with a live-app evaluator; Rubric-as-taste with calibrated examples; Sprint contracts negotiated in files; Thin planner that stays high level; Structured state on disk with JSON feature lists and progress files; Breadcrumb logs for later pickup; Read full traces, then tune prompts from them; Ralph-style stop-hook loop with exit criteria; Hooks for human check-ins; Split model roles for cost; Put the human-readable spec back into long sessions
- Tools: Claude Code, Claude Agent SDK, Playwright MCP, Chrome MCP, Claude Code skills, Claude Code sub-agents, Claude Code agent teams, Claude Code stop hooks, Claude Code auto mode, git, Puppeteer

## [Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs](../videos/V-L0INGTEOg.md)
`V-L0INGTEOg` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: coding-agents, skills-self-improvement

Boris Starkov (ElevenLabs) shows how Claude Code reverse-engineered an undocumented 1990s-style VoIP phone's protocol through port probing, command brute-force, and a traffic-capture proxy, then packaged the result as a reusable skill.

- Techniques: Black-box command sweep with error classification; Intermediary proxy for vendor-client traffic capture; Closed-loop hypothesis confirmation; Persisting a learned protocol as a skill; Using the full session transcript as context to generate a deliverable; Human as actuator for physical steps
- Tools: Claude Code, Twilio (SIP trunk), ElevenLabs conversational agents, Windows virtual machine, TCP proxy on macOS, PoE router

## [The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry](../videos/li0SaBt9RDM.md)
`li0SaBt9RDM` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: skills-self-improvement, coding-agents

Sentry engineer Priscila Andre de Oliveira on using AI mainly for codebase comprehension: she mined her own sessions, found 67% were comprehension and 2% generation, and built a reusable "Catch Me Up" skill.

- Techniques: Session-log classification audit; Repeated prompt to personal skill; Onboarding via a 'new contributor' framing; Comprehension pass before PR review; Research, then comprehension check, then plan, then implement; Codebase hygiene sprint for agent legibility
- Tools: Claude Code, Claude Opus, Catch Me Up (personal skill), Warden (Sentry code review agent), Junior (Sentry Slack bot that turns threads into PRs), Abacus (Sentry internal AI usage tracker)

## [It’s Broken… The Codex vs Claude Code Debate Is Finally Over](../videos/8ImlAQOyVTs.md)
`8ImlAQOyVTs` · AI LABS · 2026-06-02 · q3 · practitioner · review · also: coding-agents, context-engineering, multi-agent

A single-author head-to-head of Claude Code (Opus 4.7) vs Codex CLI (GPT 5.5) across usability, planning, greenfield builds, context, memory and sub-agents; Codex wins on cost and autonomy, Claude on UX, hooks and ecosystem.

- Techniques: Count tokens per session from the CLI's session files; Set a Codex personality to reduce sycophancy; Use Claude Code's expanded thinking to course-correct; Use Codex's attempt flag for best-of-n; Keep AGENTS.md or CLAUDE.md lean; Design sub-agents for isolation or inheritance deliberately
- Tools: Claude Code, Codex CLI, Opus 4.7, GPT 5.5, FastAPI, Flask, Next.js, ShadCN UI, Gemini API, Claude desktop app, Codex web app, Stream Vision Agents

## [This Is The Greatest Shift In Codex CLI And Claude Code](../videos/B44bXmzU60s.md)
`B44bXmzU60s` · AI LABS · 2026-06-02 · q2 · practitioner · review · also: mcp-and-tools, context-engineering

Walkthrough of Mirage, a virtual file system that mounts Gmail, Drive, Slack and similar services as folders so Claude Code can read them with bash instead of MCP tool calls. Partly sponsored, with a hype title.

- Techniques: Mount a SaaS service as a folder; Run the mount as a long-lived process; Start the agent inside the mounted workspace; Chain bash commands across services instead of MCP calls; Read attachments as files; Preserve a session across restarts; Wrap any API as a file system; macOS FUSE prerequisite
- Tools: Mirage (virtual file system for agents, cloned from source), Claude Code, MCP (Model Context Protocol), Gmail MCP, Google Drive MCP, Google Chat, Slack, Notion, Telegram, Figma (mentioned as a possible target), Claude Design (mentioned in passing, unverified), Google Cloud Console

## [I Didn't Know You Could Use Claude Code Like This](../videos/KQDVDtklf34.md)
`KQDVDtklf34` · AI LABS · 2026-06-02 · q2 · intro · tutorial · also: context-engineering, vibe-coding-app-building

Shows non-coding uses of Claude Code (second brain in Obsidian, Remotion video, grounded research pipeline, Canvas design skill, Claude Video watch skill, NotebookLM/Notion ops, role-based finance/teacher/legal setups) mostly as sponsored, shallow tutorials.

- Techniques: CLAUDE.md priority-tiered instructions for a non-code knowledge base; Remotion skill install and plan-first video generation; Step-file research pipeline with verification and cited output; Claude Video skill setup for watching videos; Canvas design skill workflow for posters and infographics; Local Claude Code over NotebookLM CLI and Notion MCP for content systems
- Tools: Claude Code, Claude.md, Obsidian, Remotion, Remotion skill, Anthropic Canvas design skill, Claude Video (watch skill), Groq, SERP API, Google Gemini, NotebookLM CLI, Notion MCP

## [The NPM Worm Is Back And It's So Much Worse (TanStack Hacked)](../videos/BOABEBwNnvk.md)
`BOABEBwNnvk` · Better Stack · 2026-06-02 · q3 · practitioner · news · also: security-guardrails, dev-tools

Walkthrough of the Shai-Hulud npm worm's fourth wave, which hit TanStack and about 160 other packages. It explains the persistence, credential theft, and how a poisoned CI cache plus OIDC publishing let attackers ship validly signed malicious releases.

- Techniques: Audit for agent-hook persistence after installing a package; Incident response order for a suspected worm; Trace install-time payloads through lifecycle scripts and optional dependencies; Treat CI cache restores as a trust boundary; Scope OIDC publishing to the release job only; Find 2FA-bypassing npm tokens on dev machines
- Tools: npm, npm trusted publishing (OIDC), pnpm, Bun (bun run task runner), GitHub Actions, GitHub pull_request_target, Claude Code (hooks, settings, session history), VS Code tasks, AWS IMDSv2, AWS ECS task metadata, Kubernetes service accounts, HashiCorp Vault

## [ADLC: Claude Code's New Lifecycle for AI Coding](../videos/aMBQB_IJ0dQ.md)
`aMBQB_IJ0dQ` · AI LABS · 2026-06-02 · q2 · intro · other · also: agent-architecture, evals, context-engineering

Conceptual walkthrough of the agentic development lifecycle (ADLC), a phase-by-phase SDLC analogue for non-deterministic agents with a validation gate and staged rollout. Thin on code and data, with a sponsor segment.

- Techniques: Behavior-first planning mode; Human-agent responsibility model; Ground-truth dataset plus baselines as a validation gate; Single orchestration layer for multiple agents; Context hygiene against context rot; Staged rollout with behavioral alerting; Feedback signals and periodic data refresh
- Tools: Claude Code (planning mode, agent view), Cursor, Google Calendar MCP, Gmail MCP, Notion MCP, RAGAS, DeepEval, Gemini (1M-token context, mentioned), Claude Opus (1M-token context, mentioned), ChatGPT (feedback UI example, mentioned), Softr (sponsor, transcribed as 'Softer')

## [The Greatest AI Coding System I've Ever Used, Forget Codex Vs Claude Code](../videos/q7Am0pV6FjQ.md)
`q7Am0pV6FjQ` · AI LABS · 2026-06-02 · q3 · practitioner · review · also: multi-agent, agent-architecture, context-engineering

Goal Buddy, an open-source plugin for Claude Code and Codex, wraps the native goal command with file-based state, an upfront "oracle" for done, and Scout/Worker/Judge agent roles.

- Techniques: Oracle-first done criteria; Role-separated agents with access limits; File-based run state instead of chat history; Slice contracts; Clarify before looping; Install and start a run
- Tools: Goal Buddy, Claude Code (goal command, resume command), Codex, Ralph Wiggum plugin, Haiku (native goal evaluator)

## [Why Anthropic Banned Every Third-Party Claude Tool](../videos/Fl6QT86n1P4.md)
`Fl6QT86n1P4` · Better Stack · 2026-06-02 · q3 · practitioner · news · also: token-cost-efficiency, governance-compliance

Better Stack on Anthropic's Programmatic Credits (opt-in from June 15): subscription use of the Agent SDK and claude -p moves to API-rate credits, after earlier blocks on third-party harnesses. The speaker reads it as vendor lock-in.

- Techniques: Move recurring automation to first-party surfaces such as routines and official connectors; Estimate programmatic spend at API rates before running a loop on a subscription
- Tools: Claude Code, Claude Agent SDK, claude -p (headless CLI mode), Claude routines, Remote control (Claude feature), Managed agents (Claude feature), Opus 4.7, Sandcastle, T3 Code, Zed, OpenCode, OpenClaw

## [This AI Tool Maps Any Codebase Before You Touch It (Understand-Anything)](../videos/VmIUXVlt7_I.md)
`VmIUXVlt7_I` · Better Stack · 2026-06-02 · q3 · practitioner · review · also: context-engineering, dev-tools

Walkthrough of Understand-Anything, a Claude Code plugin that builds an interactive knowledge graph of a repo for onboarding and pre-change impact checks; the speaker also flags its heavy token cost.

- Techniques: Install and run Understand-Anything in Claude Code; Onboarding order: map, then tour, then questions; Use the graph as agent context; Pre-refactor impact check
- Tools: Understand-Anything (open-source Claude Code plugin, MIT license), Claude Code, Claude Max (subscription plan referenced for rate usage), Cursor, GitHub Copilot, Gemini CLI, Google microservices sample repo (demo target)

## [3 Design Levels For a Free Claude Code Boost (People Stop At Level 1)](../videos/5lycYTOYbPM.md)
`5lycYTOYbPM` · AI LABS · 2026-06-02 · q3 · practitioner · tutorial · also: context-engineering, testing-verification, vibe-coding-app-building

Three levels of getting non-generic UI from Claude Code: a structured single-page design prompt, a CLAUDE.md plus design.md system for cross-page consistency, and design tests written before the code, including visual TDD with Visly.

- Techniques: Structured single-page design prompt; CLAUDE.md for project context, design.md for the visual system; Lint design.md against Google's open template; Install an external design-principles audit skill per project; Derive design tests from design.md before writing UI code; Visly local visual TDD loop
- Tools: Claude Code, Claude Opus 4.7 (model named in the video), CLAUDE.md, design.md, OKLCH, Google design.md template (open-sourced), Versalab design-audit skill, Playwright, Visly CLI (transcribed as 'Visly Test' and 'Visley'), Zilliz Cloud (sponsor), Inter (named as banned font), Geist (named as banned font)

## [Claude Code Just Killed Every Shopify Agency Ever](../videos/x2pRavsHdls.md)
`x2pRavsHdls` · AI LABS · 2026-06-02 · q2 · practitioner · tutorial · also: coding-agents, vibe-coding-app-building, context-engineering

A walkthrough for building and syncing a Shopify storefront with Claude Code, using the Shopify CLI, AI toolkit MCP, HTML prototype skill, Gemini image skill and settings.json hooks. Quality is capped by a sponsor segment and a thin, hype-titled setup guide.

- Techniques: Two-phase skill: HTML preview, then apply; Image generation through a CLI skill; Pre-tool-use hook as an approval gate; Shopify project bootstrap; Admin API auth with incremental scopes
- Tools: Shopify Partner account, Shopify CLI (React app template, TypeScript), Shopify AI toolkit (MCP), Shopify plugin (agents and skills), Shopify Admin API, Claude Code, CLAUDE.md, Gemini CLI (image generation), settings.json hooks, Willow Voice (sponsor segment, not a tool used in the setup)

## [Anthropic Just Revealed The Best Claude Code Setup](../videos/lGalJmyI78w.md)
`lGalJmyI78w` · AI LABS · 2026-06-02 · q2 · practitioner · tutorial · also: context-engineering, multi-agent, mcp-and-tools

Practitioner checklist for setting up Claude Code harnesses on large codebases: layered CLAUDE.md, hooks, path-scoped skills, plugins, LSP, MCP, sub-agents, and periodic pruning.

- Techniques: Layered CLAUDE.md; Stop-hook learning loop; Hooks for enforcement; Path-scoped skills; Team plugin distribution; LSP before code; Custom sub-agents with an overridden Explore agent; Per-subdirectory tests and codebase map; Quarterly harness pruning with ignore files
- Tools: Claude Code, Codex, Gemini CLI, superpowers, CLAUDE.md, Claude Code hooks (SessionStart, PreToolUse, Stop, exit-code-2), skill-creator, Claude Code plugins and plugin marketplace, LSP (Language Server Protocol), MCP (Model Context Protocol), Explore sub-agent (built-in, overridable), .gitignore

## [Claude Code + Better Stack: The Only Error Debugging Setup You Need](../videos/u2tqAXKkb4c.md)
`u2tqAXKkb4c` · Better Stack · 2026-06-02 · q2 · intro · tutorial · also: observability, mcp-and-tools

Better Stack demo of triaging a live React frontend error from the terminal: Claude Code pulls error data through the Better Stack MCP server, opens a fix PR, then resolves the issue. Short, vendor-led.

- Techniques: MCP-backed error triage loop; Deferred tool loading for MCP servers; Frontend error capture with a vendor DSN and an agent setup prompt; Scheduled error-triage routine
- Tools: Claude Code, Better Stack (error tracking, session replay, MCP server), Sentry React SDK, Telegram, WhatsApp, email

## [How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom](../videos/4_VQBbs2iQA.md)
`4_VQBbs2iQA` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: enterprise-adoption, skills-self-improvement, pr-code-review

Intercom's platform lead explains how they set a goal to double engineering throughput by standardizing on Claude Code, backed by skills, hooks, calibrated auto-approval and telemetry.

- Techniques: Single-platform standardization with internal plugin distribution; Guidance flywheel; Problem-first prompting; Backtested skill authoring; Calibrated automatic approval; Agent telemetry and transcript mining
- Tools: Claude Code, GitHub Copilot, Cursor, Augment, Honeycomb, S3, DX, Ruby on Rails, React, GitHub

## [Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser](../videos/pFsfax19yOM.md)
`pFsfax19yOM` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: skills-self-improvement, evals, context-engineering

Hands-on WorkOS workshop on writing Claude skills: description-based routing, constraints over prose, progressive disclosure, confidence gates, with-and-without-skill evals, and sharing skills.

- Techniques: Description-as-router; Constraints over prescription; Bang-backtick command injection; Progressive disclosure via reference map; Subagent for verbose checks; Confidence-gated clarification; With-and-without-skill eval; Transcript-driven skill refinement; Looped connector poll
- Tools: Claude Code, Codex, Cursor, Pi, OpenClaw, Claude Desktop, Claude Agent SDK, WorkOS CLI, Obsidian, Linear, Slack connector, Remotion

## ["Software Fundamentals Matter More Than Ever" — Matt Pocock](../videos/v4F1gFy-hqg.md)
`v4F1gFy-hqg` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: testing-verification, context-engineering, coding-agents

Matt Pocock argues software fundamentals (deep modules, shared language, TDD, good feedback loops) matter more with AI agents, because bad code is now the most expensive it has been.

- Techniques: Grill-me interview before planning; Generated ubiquitous-language glossary; Small-step TDD with feedback loops; Codebase architecture improvement skill; Design the interface, delegate the implementation
- Tools: Claude Code

## [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase — Pedro Rodrigues, Supabase](../videos/GmAQKINjv1E.md)
`GmAQKINjv1E` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: skills-self-improvement, evals, context-engineering

Pedro Rodrigues (Supabase) walks through writing agent skills, testing their triggering, and running with/without-skill evals, using a Postgres RLS view bug as the running example.

- Techniques: Progressive-disclosure skill layout; Trigger-accuracy testing via headless CLI; With/without skill eval comparison; Deterministic state assertions before LLM judging; MCP tool plus skill split for data access; security_invoker for Postgres views over RLS tables; Skill install via npm skills package with symlinks
- Tools: Claude Code, Supabase MCP server, Supabase CLI via npx, Postgres, Next.js, Braintrust, Langfuse, Vercel skills npm package, Python (DB reset and eval scripts), VS Code

## [I Tried Every Skill. These Best Claude Skills Are Bizarre](../videos/qQ5uObNKBOU.md)
`qQ5uObNKBOU` · AI LABS · 2026-05-02 · q2 · intro · review · also: skills-self-improvement, testing-verification, token-cost-efficiency

Walkthrough of nine community Claude Code skills (notifications, adversarial app QA, output compression, git audit, premortem, mutation testing, plan stress-testing, Reddit research, UI color guidance). Mostly README-level tours, with a mid-video sponsor segment.

- Techniques: Per-event voice notifications for parallel Claude sessions; Adversarial browser QA sweep; Terse-output mode to cut response tokens; Git-history audit with a skill; Premortem pass before go-live; Mutation testing for test-suite strength; Stress-test a plan with selectable challenge modes; Fallback chain for scraping Reddit; Grounded design-reference skill for UI
- Tools: P on Ping (skill, transcript name), Claude Code, agent-browser (CLI), Dogfood skill, Caveman plugin, Git, Git Time Travel skill, Premortem skill, Mutation testing skill, The Fool skill, Gemini CLI, tmux

## [Claude Routines: The Hidden Costs Nobody Talks About](../videos/yVnsU-xqng4.md)
`yVnsU-xqng4` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: token-cost-efficiency, agent-architecture

Walkthrough of Claude Routines (cloud-run scheduled, GitHub-event and API-triggered Claude Code tasks), covering setup gotchas, daily run caps and why the presenter finds them too expensive for most automation.

- Techniques: Schedule a remote routine from the CLI; Write prompts for unattended runs; Work around the Bash network block with a custom environment; Ship skills and hooks to the cloud instance through a repo; Trigger PR reviews from GitHub events; Compare routine cost with a self-hosted webhook agent
- Tools: Claude Code, Claude Routines, Claude desktop app, /schedule slash command, Bash, WebFetch, curl, GitHub, GitHub MCP server, Slack, n8n, Hermes Agent

## [This Is The Anthropic Team's Greatest Advice](../videos/O1XLCh-uA_E.md)
`O1XLCh-uA_E` · AI LABS · 2026-05-02 · q2 · practitioner · tutorial · also: context-engineering, multi-agent, agent-architecture

Practical habits for managing Claude Code's context window (compaction, clear, rewind, sub-agents, recaps) to limit context rot and goal drift in long runs; mostly attributed advice with a sponsored segment.

- Techniques: Manual compaction with an explicit instruction; Clear on task switch; Structured state handoff (save, clear, reload); Periodic recap to reinforce goals; Sub-agent isolation for raw-heavy subtasks; Rewind, then re-prompt
- Tools: Claude Code, Claude (Opus 4.5 and later models, 1M context window), CLAUDE.md, Verdant (sponsor)

## [Claude Ultraplan vs Superpowers: I Found a WINNER and It's Not Even Close](../videos/-qFf7v2399E.md)
`-qFf7v2399E` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: coding-agents, testing-verification, token-cost-efficiency

A single-repo demo comparing Claude Code's cloud Ultraplan with the Superpowers plugin for planning a release pipeline: Ultraplan is faster and cheaper but thinner, and the host plans locally about 90% of the time.

- Techniques: Launch Ultraplan from the Claude Code CLI; Review and revise an Ultraplan plan in the browser; Superpowers two-stage planning; Stop the planner from using a skill when comparing
- Tools: Claude Code (CLI), Ultraplan (Claude Code feature), Claude Code on the web (Claude Code for Web), Claude Code desktop app for Mac, Superpowers (Claude Code plugin), Claude Routines (mentioned as newly released), GitHub

## [This Claude Skill Cuts Your Token Costs In HALF](../videos/RuH3uiJy84A.md)
`RuH3uiJy84A` · Better Stack · 2026-05-02 · q2 · practitioner · review · also: token-cost-efficiency, skills-self-improvement, context-engineering

Better Stack tests Caveman, a Claude Code skill that makes answers terse to cut output tokens. Output savings are real (45%), but the skill's own input overhead erases them on single prompts.

- Techniques: Terse-output skill file; Three-arm token A/B; Count the instruction file as input cost; Compressed instruction files; Terse commit and review outputs
- Tools: Claude Code (captions say 'claw code'), Codex (named as compatible), Caveman skill, Next.js (demo app), Better Stack RUM (demo app context), skills package installer (name garbled in captions as 'Vasell'), prompt caching (provider feature referenced by the presenter)

## [Fallow: The Code Intelligence Tool Every Claude User Needs](../videos/-lCfwIoDXq8.md)
`-lCfwIoDXq8` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: pr-code-review, dev-tools

Better Stack walks through Fallow, a Rust-built static analyzer for JS/TS (dead code, duplication, complexity), and shows how it works as a guardrail for Claude Code runs and branch-level PR audits.

- Techniques: Snapshot the project with the summary report; Drill into one category with machine-readable output; Preview fixes with dry run before any write; Guard an agent run with the Fallow skill and a scoped prompt; Scope a config file to ignore noise; Audit only the current branch against main; Generate Claude Code hooks for Fallow; CI with baselines and PR annotations
- Tools: Fallow, Claude Code, knip, jscpd, ESLint, bunx, Oxc, VS Code extension, Cursor, MCP server, V8 runtime coverage, GitHub Action

## [Anthropic Just Fixed The Token Problem](../videos/sncxStbRSwI.md)
`sncxStbRSwI` · AI LABS · 2026-05-02 · q2 · practitioner · review · also: coding-agents, token-cost-efficiency, multi-agent

AI LABS walks through Anthropic's advisor strategy in Claude Code: a Sonnet executor does all the work and calls Opus only when stuck. Three anecdotal tests show it helps simple-to-medium apps but needs nudging.

- Techniques: Executor/advisor model split in Claude Code; Escalate after repeated failure; Consult before a high-blast-radius change; Name the advisor explicitly for non-trivial tasks; Choose the main model by app scope
- Tools: Claude Code, Claude Opus 4.6, Claude Sonnet, Claude Haiku, Playwright MCP, SWE-bench, Junie (JetBrains, sponsor segment)

## [Give Me 13mins, I Will Show You The Right Agent Setup](../videos/ywIhw15za9Y.md)
`ywIhw15za9Y` · AI LABS · 2026-05-02 · q2 · intro · tutorial · also: context-engineering, testing-verification, coding-agents

AI LABS walks through a pre-build setup checklist for Claude Code: product-focused PRD, hand-written CLAUDE.md, agents and skills, spec-first tests, progress and learnings files, and load planning. Generic, sponsored, no benchmarks.

- Techniques: Agent-led PRD interview; Lean hand-written CLAUDE.md that links the PRD; Agent vs skill split; Path-scoped rules linked from CLAUDE.md; Negative-constraints docs file; Progress file plus learnings file; Spec-first test generation; Commit-per-implementation with worktrees; Concurrency-aware load test planning
- Tools: Claude Code, CLAUDE.md, Supabase MCP, shadcn/ui, Playwright, Playwright MCP, skill-creator, GitHub, Git (commits, worktrees), Notion MCP, Trello, OpenClaw (sponsor's skill)

## [Knowing This Gives You An Unfair Advantage With AI Coding](../videos/fMY5Sdj2DMk.md)
`fMY5Sdj2DMk` · AI LABS · 2026-05-02 · q3 · practitioner · tutorial · also: context-engineering, coding-agents, testing-verification

Tutorial for writing CLAUDE.md rules that keep Claude Code on task: think-first, simplicity, surgical edits, verifiable goals, git safety, scoped rule files and a corrections log.

- Techniques: Behavioral rule block for CLAUDE.md (Karpathy-derived); Verification gate before reporting completion; List only non-default tooling; Corrections-to-learnings loop; Destructive-command confirmation rule; Path-scoped rule files and nested CLAUDE.md; CLAUDE.md structure: description first, priority tiers, length cap
- Tools: Claude Code, CLAUDE.md, AGENTS.md, Karpathy skills repo (referenced, not named as a package), Claude Chrome extension, Puppeteer MCP, Git, GitHub CLI (gh), npm, pnpm, Klaus (sponsor, AI agent hosting), OpenClaw (sponsor, open-source AI agent)

## [The Claude Code Skill Boris Cherny Runs on Every Project](../videos/AhXfI1rSUPc.md)
`AhXfI1rSUPc` · AI LABS · 2026-05-02 · q2 · practitioner · review · also: skills-self-improvement, multi-agent, testing-verification

A walkthrough of skills, plugins and slash commands the Claude Code team reportedly uses, including batch worktree fan-out, a verify skill and an end-of-session tech debt skill. Several are internal and unverified, and a sponsor segment is included.

- Techniques: Batch fan-out with worktrees; Project-specific verify skill; Skillify-style session capture; End-of-session tech-debt pass; Inner-loop slash commands; Issue dedupe with a confidence threshold; Security scan, then fix
- Tools: Claude Code, Claude Code batch command, git worktrees, frontend-design plugin, Code Simplifier plugin, Simplify (built-in), Claude Code security scan (built-in), commit command plugin, Remotion skill, skill creator skill, Skillify (internal), verify skill (internal)

## [Anthropic's Managed Agents Are Different (Here's Why)](../videos/uxHolzq1NcA.md)
`uxHolzq1NcA` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: agent-architecture, security-guardrails, mcp-and-tools

Better Stack walks through Anthropic's Claude Managed Agents: building a Slack-connected agent with no hand-written orchestration code, its per-session-hour pricing, and the session/harness/orchestrator architecture with runtime credential vaulting.

- Techniques: Scaffold a managed agent via the Claude Code skill; Read-only toolset for a retrieval agent; Run setup once, then the runtime; Iterate in the Console and keep version history; Runtime credential injection (vault pattern); Separate durable session log from the executor
- Tools: Claude Managed Agents, Claude Console, Claude Code (managed-agent onboarding skill, `/claude-api managed agents onboarding`), Claude Agent SDK, TypeScript Claude SDK, Claude Opus, Claude Sonnet, Slack (Slack app and bot), Notion (built-in integration), MCP servers, OpenClaw, GitHub (private repo as data source)

## [How To Never Hit Your Claude Code Limit Again](../videos/YsdQE6juGXY.md)
`YsdQE6juGXY` · AI LABS · 2026-05-02 · q3 · practitioner · tutorial · also: token-cost-efficiency, context-engineering

Practitioner tips for stretching Claude Code's usage limits: explains the 5-hour window, then covers context hygiene, lean CLAUDE.md, model and effort routing, hooks, and settings toggles. Partly sponsored; leaked-source claims are unverified.

- Techniques: Clear or compact between tasks; Side questions in a separate context via the by-the-way command; Rewind to before a misaligned turn instead of re-prompting; Lean CLAUDE.md with linked, progressively loaded docs; Path-scoped rules files; Skills with bundled scripts for repetitive workflows; Session-only instructions via the append-system-prompt flag; Task-based model and effort routing; Disable unused MCP servers per project; Hook that keeps only failing tests in context; Settings toggles for token use
- Tools: Claude Code, Claude (Pro and Max plans), Claude Desktop, Cowork, Claude Opus, Claude Sonnet, Claude Haiku, Claude.md (CLAUDE.md), MCP servers, Twin (sponsor), Zapier (named in sponsor segment), n8n (named in sponsor segment)

## [We Already Have Something Better Than Claude Design](../videos/GbuwosWEvHo.md)
`GbuwosWEvHo` · AI LABS · 2026-05-02 · q2 · intro · review · also: coding-agents, product-ux, context-engineering

AI LABS argues Claude Design is mostly hype: Claude Code with Opus 4.7 can match it, and it adds Git, parallel worktrees, and skills. The evidence is one anecdotal comparison plus sponsor-heavy, unverified claims.

- Techniques: Clarifying-question skill to replace Claude Design's intake flow; Hero video background plus animation libraries; Component libraries and MCP for UI consistency; Parallel design variants in git worktrees; Prototype as HTML mock-ups
- Tools: Claude Code, Claude Design, Claude Opus 4.7, Claude Opus 4.6, GSAP, Lenis, ShadCN, ShadCN MCP server, Aceternity UI, Hero UI, scrollytelling skill, Figma

## [Your AI Output Sucks Because You’re Not Doing This](../videos/cop_G65D7PA.md)
`cop_G65D7PA` · AI LABS · 2026-04-02 · q2 · intro · tutorial · also: context-engineering, multi-agent, token-cost-efficiency

AI LABS' pre-setup tips for Cowork: a per-folder manifest.md with tiered sources, voice and working-style files, global instructions that demand plans and questions, end-state prompts, batching and guardrails.

- Techniques: Per-folder manifest.md with tiered sources; Identity, voice and working-style context files; Global instructions as a default operating contract; State the end state and the edge-case rule; Batch by shared context, keep unrelated work apart; Scheduled report from meeting notes via the schedule skill; Build a plugin with the plugin-creation skill; Guardrails for agent file access
- Tools: Cowork, Claude Code (clawed code in transcript), Claude desktop app, CLAUDE.md (global and per-folder instructions), manifest.md (the presenter's convention), schedule skill, plugin-creation skill, OpenClaud (auto-caption; used for research, tool-release tracking and a Discord report; spelling uncertain), Discord, Gmail connector, Google Drive connector, cron jobs

## [Google's New CLI Is The Missing Piece for Claude Code](../videos/EKG9kX86u0s.md)
`EKG9kX86u0s` · Better Stack · 2026-04-02 · q3 · practitioner · review · also: mcp-and-tools, token-cost-efficiency, coding-agents

Walkthrough of Google's new Rust Workspace CLI for agents: OAuth setup pain, CLI vs MCP token trade-offs, and design choices (nested JSON, runtime schema lookup, field masks) that keep context use low.

- Techniques: Agent-discoverable CLI with runtime help and schema; Nested JSON params flag for complex calls; Field selection to trim API responses; Layer skills on top of the CLI for guidance; Google Workspace OAuth setup for a CLI; Choose CLI vs MCP by token and portability trade-offs
- Tools: Google Workspace CLI (GWS CLI, Rust, written by a developer named Justin; no version stated), Claude / Claude Code, gcloud CLI (Google Cloud CLI, installed with Homebrew), Google Cloud Console (OAuth client, consent screen, Audience), Gmail, Google Drive, Google Slides, Google Sheets, Google Calendar (Workspace APIs used in the demos), SkillsSH (skills registry; over 100 Workspace skills), MCP (Model Context Protocol; compared, not reviewed in depth), Playwright CLI (mentioned as a prior example of an MCP server turned into a CLI; covered in an earlier video), Electrobun (Electron alternative powered by Bun; promoted at the end, not covered)

## [12 Hidden Settings To Enable In Your Claude Code Setup](../videos/pDoBe4qbFPE.md)
`pDoBe4qbFPE` · AI LABS · 2026-04-02 · q2 · practitioner · tutorial · also: context-engineering, multi-agent

Tour of under-documented Claude Code settings: session retention, output and read caps, sub-agent flags, auto-compact at 75%, commit attribution, telemetry, and exit-code-2 hooks. Includes a sponsored segment.

- Techniques: Extend session retention; Path-scoped rules; Raise the bash output cap; Run a session as a sub-agent; Raise the file read cap and enforce full reads; Lower the auto-compact threshold; Remove commit co-author lines; Opt out of telemetry without losing updates; Prompt stash with Ctrl+S; Exit-code-2 hook to block and steer; Loop-until-done with exit-code hooks (Ralph-style); Claude CTX profiles
- Tools: Claude Code, Claude CTX (open-source profile switcher), Opus 4.6 (cited as the 1M-token-context model), uv (transcribed as 'uvicorn'; likely the pip replacement in the hook example), Statsig (analytics sink, named by speaker), Sentry (error reporting sink, named by speaker), Make.com (sponsor), Ralph loops (named concept, not a tool)

## [How to use Claude Code and Gemini Cli Together](../videos/XdtBAm2pM-0.md)
`XdtBAm2pM-0` · AI LABS · 2026-04-02 · q3 · practitioner · tutorial · also: multi-agent, coding-agents, context-engineering

Walkthrough of Agent Chatter, a shared chat layer where Claude Code, Gemini CLI and Codex agents run in tmux and coordinate through channels, with planning, peer review and loop-guard setup.

- Techniques: Shared multi-model chat via per-agent tmux sessions; Per-agent settings.json permissions instead of skip-permissions; Shared agents.md as the single instruction source; Named personas per agent; Loop guard and continue gate; Planner-first with PRD and spec templates; Three-phase presenter/challenger/synthesizer review; Planner as orchestrator with an ask-don't-assume rule; Git worktrees per agent (suggested, not tested); Initialize the app framework before starting agents
- Tools: Agent Chatter, Claude Code, Opus 4.6, Gemini CLI, Codex, Kimi, Qwen, GLM, tmux, Next.js, MCP, agents.md

## [Claude Code + CMUX: The Ultimate AI Coding Terminal](../videos/8oLP8oxqtOE.md)
`8oLP8oxqtOE` · Better Stack · 2026-04-02 · q3 · intro · review · also: coding-agents, multi-agent, dev-tools

Walkthrough of cmux, a native macOS terminal whose CLI and Unix socket let Claude Code or OpenCode drive browser panes, spawn sub-agent panes, and send attention notifications.

- Techniques: Agent-driven browser pane for live testing; Sub-agents in split panes that report back and close; Attention notifications with pane flash; Sidebar status from the agent; Setup with cmux skills and hooks; Cheap demo runs by switching the model
- Tools: cmux, Claude Code, OpenCode, libghostty, Ghostty, WebKit, Bonsplit, tmux, Warp, soloterm, Demux, Haiku

## [The toolkit from Y Combinator CEO that Will Makes Claude Code Amazing](../videos/kLq5p43huYQ.md)
`kLq5p43huYQ` · Better Stack · 2026-04-02 · q3 · practitioner · review · also: coding-agents, pr-code-review, testing-verification

A Better Stack walkthrough of GStack, Gary Tan's Claude Code skill pack, showing a plan, review, ship and QA pipeline that builds, tests and opens a PR for a tweet-screenshot feature.

- Techniques: Install GStack into a Claude Code project; Plan-mode CEO scope review before coding; Diff-aware review, ship and QA chain; Let the review command resolve PR review comments; Put tool preferences in CLAUDE.md, not hooks; Skill template plus generated SKILL.md
- Tools: Claude Code, GStack, Bun, Playwright, Greptile, Superpowers (Claude Code plugin), Conductor, React, Vite, TypeScript, Opus, CLAUDE.md

## [Why Every Claude Code User Needs To Try AgentMail (Not Gmail)](../videos/U3TXAdpmvVk.md)
`U3TXAdpmvVk` · Better Stack · 2026-04-02 · q3 · practitioner · review · also: mcp-and-tools, agent-architecture

Better Stack walkthrough of AgentMail, an email-inbox API for agents, shown through the CLI in Claude Code and a 30-second polling reply agent built on the Claude SDK. Mostly a demo, with no benchmarks.

- Techniques: Give each agent its own inbox via CLI + skill, not an MCP server; Split inboxes by purpose or by agent; Poll for mail with a Claude Code loop for short-lived checks; Custom polling reply agent on the Claude SDK
- Tools: AgentMail (API, dashboard, CLI, skill, MCP server, Python and TypeScript SDKs), Claude Code (loop feature, skills), Claude SDK, Claude Haiku, Google Workspace CLI (mentioned, previous video), Gmail, Codex, Gemini CLI, Electron (transcript says "Electrobon"; desktop app framework, mentioned only)

## [Claude Code Loop: The Feature Everyone Misunderstands](../videos/Xxqu-kz00gw.md)
`Xxqu-kz00gw` · Better Stack · 2026-04-02 · q4 · practitioner · review · also: agent-architecture

Better Stack walks through Claude Code's new loop skill (repeat a prompt on an interval), argues it is for re-running tasks inside one session rather than a durable assistant, and lists its limits: 3-day auto-expiry and session-only storage.

- Techniques: In-session interval polling with loop; Clock-time daily job; List and delete scheduled jobs; Durable schedules via Claude Desktop or Cowork; Avoid loop for long-lived listeners or Ralph loops
- Tools: Claude Code, loop skill, cron create skill, cron list tool, Claude Desktop, Cowork, Claude Sonnet, Claude Haiku, OpenClaw, Telegram, WhatsApp, Discord

## [Anthropic Just Killed All Your Agent Harnesses](../videos/nBH07G-zayk.md)
`nBH07G-zayk` · AI LABS · 2026-04-02 · q2 · practitioner · review · also: agent-architecture, testing-verification, context-engineering

Walkthrough of Anthropic's reported harness ablations: with Opus 4.5/4.6, keep a planner, a generator and a separate graded evaluator, and drop micro-level plans, context resets and sprint contracts for strong models.

- Techniques: Product-level planner agent; Separate evaluator with an adversarial stance; Weighted rubric with a score per criterion; Generator and evaluator as agent-team members; Sprint contract for weaker models; Bolt Anthropic's evaluator onto GSD
- Tools: Claude Code, Claude Opus 4.5, Claude Opus 4.6, Claude Sonnet, Claude Haiku, Anthropic agent harness, BMAD, GSD, SpecKit, Superpowers, Ralph Loop, Playwright MCP

## [I Didn't Know This Was Possible Until Now](../videos/LqN_ItMqovA.md)
`LqN_ItMqovA` · AI LABS · 2026-04-02 · q3 · practitioner · review · also: mcp-and-tools, token-cost-efficiency, context-engineering

A team's walkthrough of MCP context bloat and a runtime MCP-to-CLI converter (MCP2CLI), plus CLAUDE.md and skills rules that keep large tool outputs out of the context window.

- Techniques: Run MCP2CLI without installing it; Give the agent the MCP access tokens through environment or file references; Verify MCP connections by asking the agent to count the tools; CLAUDE.md rule to consult docs before coding; Move per-MCP guidance from CLAUDE.md into one skill per MCP; Ask for TOON output for verbose documentation MCPs; Redirect large MCP output to a file and grep it; Use Claude's browser extension for stateful browser testing

## [Opus 4.6 + Agent Teams Makes Claude Code Insane](../videos/LZyWuPqvvjU.md)
`LZyWuPqvvjU` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: multi-agent, coding-agents, token-cost-efficiency

Walkthrough of Claude Code's experimental Agent Teams: independent teammates with a shared task list that can message each other, viewed in tmux or in-process. Two teammates used 29% of usage, so the presenter would restrict it.

- Techniques: Enable agent teams; Give the team lead a plan and let it spawn teammates; Watch teammates in tmux; Switch teammates in a single window; Inspect team state on disk; Reserve teams for cross-checking and research
- Tools: Claude Code, Claude Opus 4.6, Claude Haiku, tmux, iTerm2, OpenCode

## [10 Crazy Claude Code Tips That Give You An Unfair Advantage](../videos/TmsH-RIHvas.md)
`TmsH-RIHvas` · AI LABS · 2026-03-02 · q3 · practitioner · tutorial · also: context-engineering, testing-verification, multi-agent

AI LABS walks through ten Claude Code practices: session-insight reviews, Claude-written planning docs, exit-code-2 hooks, worktree-based parallel agents, adversarial fact-checking, and browser-based self-verification.

- Techniques: Session insights review into CLAUDE.md; Claude-authored planning docs as context; Context7 MCP for current library docs; Exit-code-2 PreToolUse guard for protected paths; MCP CLI mode to keep tool schemas out of context; One git worktree per parallel agent; Strict TypeScript and user stories before implementation; Adversarial researcher and fact-checker agents; Agent Browser for self-verification, with CLAUDE.md fallback order; Failure-prediction review pass
- Tools: Claude Code, CLAUDE.md, Claude Code hooks (PreToolUse), MCPCLI (experimental MCP CLI mode), Context7 MCP, git worktrees, TypeScript, Claude in Chrome extension, Puppeteer MCP, Agent Browser (Vercel), Kimi K2.5 (named as comparison in a research example), Opus 4.6 (named as subject of a research example)

## [The Correct Way to Use Claude Code Teams](../videos/MSyWjPDrHJw.md)
`MSyWjPDrHJw` · AI LABS · 2026-03-02 · q3 · practitioner · tutorial · also: multi-agent, coding-agents, token-cost-efficiency

AI LABS walks through Claude Code agent teams, an experimental upgrade over sub-agents where teammates message each other directly, and shows three uses plus practical rules for keeping them on track.

- Techniques: Enable agent teams behind the experimental flag; Reviewer and fixer pair for parallel code review; Multi-perspective bug hunt; Staged build with a blocking foundation agent; Per-assignment task documents to bound scope; Lead supervision rules
- Tools: Claude Code, Claude Code agent teams (experimental), Claude Code sub-agents, Claude Opus 4.6

## [This Changed The Way I Design With AI](../videos/sdxJEd7nqiQ.md)
`sdxJEd7nqiQ` · AI LABS · 2026-03-02 · q3 · practitioner · review · also: coding-agents, product-ux, skills-self-improvement

Pencil.dev design-to-code workflow with Claude Code: a file-watcher syncs .pen edits to code, subagents build pages, and a UX-audit skill raised the site grade from C to B.

- Techniques: Design file as a repo artifact; Save-triggered sync watcher; Pre-approve permissions for unattended claude runs; One subagent per page with shared docs; XML-tagged task prompts; Layer Lenis over GSAP for scroll; UX Audit skill with a scored re-run loop
- Tools: Pencil.dev, Claude Code, Claude CLI, Claude Opus 4.6, Codex, Figma MCP, Stitch, Bolt, npm, Git, GSAP, Lenis

## [NanoClaw: The Lightweight, Secure AI Assistant OpenClaw Should Have Been](../videos/AQ5uiLyr8bQ.md)
`AQ5uiLyr8bQ` · Better Stack · 2026-03-02 · q2 · intro · review · also: sandboxing-execution, agent-architecture

Better Stack walkthrough of NanoClaw, a ~500-line personal AI assistant on the Claude Agent SDK with WhatsApp, containers and self-extension by asking the agent; a short overview with a single feature-add demo.

- Techniques: Self-extending assistant via chat-driven code change; Hardened VPS install for a personal agent; Use a Claude subscription for an SDK-based agent
- Tools: NanoClaw, OpenClaw, Claude Agent SDK, Claude Code, Claude Sonnet (default model), Docker, Apple containers, Node.js (above v20), WhatsApp, Tailscale, Vercel agent-browser, Unsplash (image tool demo)

## [Anthropic Released Another Official Process](../videos/aEqKWI-0N0c.md)
`aEqKWI-0N0c` · AI LABS · 2026-03-02 · q2 · practitioner · tutorial · also: skills-self-improvement, context-engineering, testing-verification

A team rebuilds a Nano Banana image skill for Claude Code, then shows the skill-design fixes that mattered: trigger-rich descriptions, progressive disclosure, scripts, validation gates and error tables.

- Techniques: Trigger-rich skill descriptions with negative triggers; Three-level progressive disclosure layout; Move constraints out of prompts into post-processing; CLI scripts with modes and a preview mode; Two-stage validation gates with regenerate-on-fail; Error table with error, cause, and fix; Split domain knowledge into reference packets; Iterate against real outputs and refresh the skill-creator
- Tools: Claude Code, Google Antigravity, Nano Banana Pro, skill-creator (Claude Code official skill), Next.js, Cream (sponsor, merchant of record), Cursor, Windsurf

## [This Is The Only Claude Code Plugin You'll EVER Need (Superpowers)](../videos/lq3rzXP4_vs.md)
`lq3rzXP4_vs` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: skills-self-improvement, multi-agent, testing-verification

Walkthrough of Superpowers, a Claude Code skills plugin that forces brainstorm, planning, sub-agent TDD and per-step commits. It beat plain plan mode in one demo, but the agent skipped TDD once.

- Techniques: Brainstorm into a design doc before code; Split the design into sub-agent-sized tasks; Pick the execution mode deliberately; Per-task red-green loop with a git commit per step; Plan doc, clear context, then execute (presenter's own workflow, not part of Superpowers)
- Tools: Superpowers (agentic skills framework / Claude Code plugin; 14 skills per the presenter), Claude Code, Opus 4.6 (Anthropic model, used for both builds), React, Vite, Hono (server framework), CSS-in-JS styling library (unnamed in the video), Tailwind CSS (suggested by the presenter in hindsight, not used), XDL (CLI that downloads videos from Twitter; the demo app wraps it), git, Beads (planning tool, comparison only), spec-kit (spec-driven development, comparison only)

## [A Code Editor That Actually Scales](../videos/kCWwrx51IS4.md)
`kCWwrx51IS4` · Better Stack · 2026-03-02 · q2 · intro · review · also: dev-tools, coding-agents

A short tour of Zed, a Rust editor pitched against Cursor on large-repo speed and real-time multiplayer. The Claude integration via ACP is the headline, but the evidence for speed is anecdotal.

- Techniques: Inline AI edit on a selection; Opt-in Claude Code sidebar; Live collaboration channel for pairing and review; Keyboard navigation for large repos
- Tools: Zed, Claude (via Agent Client Protocol, ACP), Claude Code (sidebar in Zed, transcript says 'Cloud Code'), Cursor (comparison only), GitHub (invites)

## [How To Use NotebookLM - 7 Crazy Ways](../videos/eFCHwtufjJc.md)
`eFCHwtufjJc` · AI LABS · 2026-03-02 · q3 · practitioner · tutorial · also: context-engineering, rag-retrieval, coding-agents

AI LABS shows seven ways to wire Google's NotebookLM CLI into Claude Code as a grounded knowledge base: a second brain, research store, codebase onboarding, debugging KB, agent-readable visualizations, and a security handbook.

- Techniques: Install and verify the NotebookLM CLI; Notebook as project second brain via CLAUDE.md; Research offload to a notebook; Codebase onboarding via Repomix; Debugging knowledge base in place of web search; Export mind maps and tables as agent-readable artifacts; Security handbook notebook for grounded reviews; Shared notebook as knowledge base for people and other agents
- Tools: NotebookLM (Google), NotebookLM CLI (version not stated), Claude Code, CLAUDE.md, Repomix (CLI, installed via npm), GitHub CLI (gh), Gemini (answers NotebookLM queries, per the speaker), Cursor, Gemini CLI, OWASP cheat sheets, Make (sponsor, pre-built market research agent)

## [Give Claude Persistent Memory in 5 Minutes](../videos/ryqpGVWRQxA.md)
`ryqpGVWRQxA` · Better Stack · 2026-03-02 · q2 · intro · review · also: memory, context-engineering, token-cost-efficiency

Shows Claude-Mem, an open-source local tool that auto-captures Claude Code session events (bug fixes, decisions, diffs) and recalls compressed context in new sessions.

- Techniques: Automatic session-event capture into a local memory store; Compressed-summary-first recall with expand-on-demand; Tag and keyword search over memories; Reproducing the demo test for a memory tool
- Tools: Claude Code, Claude-Mem (open-source Claude Code memory plugin; version not stated)

## [Native Worktrees Just Killed Traditional Claude Code Workflows](../videos/lj_xZn-Yf18.md)
`lj_xZn-Yf18` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: coding-agents, multi-agent, dev-tools

A 4-minute walkthrough of Claude Code's native git worktree support: run parallel feature branches in isolated worktrees, resume them by name, and use worktree-isolated subagents, with a note on a recent breakage.

- Techniques: Parallel feature branches with named worktrees; Isolate a broken feature and ship the rest; Return to or resume a worktree; Open a shell in a worktree directory with tmux; Worktree isolation for custom subagents; Clean up temporary worktrees
- Tools: Claude Code, Claude Desktop, git, React, tmux, Claude Squad, React Doctor, SVN, Jujutsu

## [The Last Claude Code Tutorial You'll Ever Need](../videos/EHDzlot7LKU.md)
`EHDzlot7LKU` · AI LABS · 2026-02-02 · q3 · intro · tutorial · also: context-engineering, multi-agent, skills-self-improvement

Principles for building your own agent workflow in Claude Code: progressive disclosure, external note files, context-budget hygiene, subagents, git and slash commands.

- Techniques: Progressive disclosure via skills; External note files for long tasks; Manual context hygiene; Delegating research to subagents; Format selection for context files; Git as memory and parallelism; Slash commands for repeated procedures
- Tools: Claude Code, Claude (Anthropic models, 200k context), Gemini (1M context), Sonnet 4.5, BMAD, SpecKit, agent.md / AGENTS.md, CLAUDE.md, Jira MCP, Figma MCP, Git, git worktrees

## [Anthropic Have FINALLY Solved the MCP Context Nightmare](../videos/1RpGVqgqLaE.md)
`1RpGVqgqLaE` · Better Stack · 2026-02-02 · q2 · intro · news · also: mcp-and-tools, token-cost-efficiency, context-engineering

Claude Code's MCP tool search loads only the 3-5 most relevant tools on demand instead of preloading every schema, cutting context use. A short explainer that compares it with Cloudflare's code-orchestration approach.

- Techniques: Threshold-gated tool search; Programmatic tool orchestration; Wrap MCP servers as CLI commands
- Tools: Claude Code, Claude Opus, MCP (Model Context Protocol), Cloudflare Workers, Cloudflare (programmatic tool calling), Cursor, Agent Skills, mcporter, Python, TypeScript, Better Stack MCP server, Gemini (1M-token window, mentioned only)

## [Claude Code's HIDDEN Agent Swarm (Better Than Kimi K2.5?)](../videos/eRu5kIYAAz8.md)
`eRu5kIYAAz8` · Better Stack · 2026-02-02 · q2 · intro · review · also: multi-agent, coding-agents

Better Stack demos an unreleased Claude Code "agent swarm" mode, hidden behind a flag, where an orchestrator spawns specialized sub-agents on the fly, then argues Anthropic is unlikely to ship it soon as-is.

- Techniques: Plan-file to swarm execution (reproducing the demo); Checking existing sub-agents before a swarm run; Manual sub-agent memory via shared markdown files
- Tools: Claude Code, Claude Sneak Peek (fork of CC Mirror), CC Mirror, Kimi K2.5, Opus (mentioned as a benchmark comparison, no version detail), XDL (X/Twitter video downloader, the demo target), Better Stack (log monitoring, anomaly detection, AI-native error tracking)

## [This Exceeded Every Expectation I Had](../videos/iC9loBJjduM.md)
`iC9loBJjduM` · AI LABS · 2026-02-02 · q3 · practitioner · tutorial · also: context-engineering, mcp-and-tools, token-cost-efficiency

Applies Cursor's dynamic context discovery ideas to Claude Code via CLAUDE.md: offload big tool output and chat history to files, lazy-load MCP tools, and grep logs instead of re-running them.

- Techniques: Offload large MCP responses to files; Per-session history file as compaction insurance; Timestamped terminal logs with grep-and-tail retrieval; Progressive-disclosure skills; Lazy MCP tool loading with the experimental MCP CLI flag
- Tools: Claude Code, Cursor, Antigravity, Codex, Gemini CLI, Claude Chrome extension, CLAUDE.md, MCP (Model Context Protocol), MCP CLI (experimental Claude Code flag), Claude advanced tool search (developer platform), Cursor semantic search, grep

## [Claude Code Just Got a Brain Upgrade Inspired By Beads](../videos/-xOAYPjhigY.md)
`-xOAYPjhigY` · Better Stack · 2026-02-02 · q3 · intro · review · also: multi-agent, context-engineering, agent-architecture

Better Stack walkthrough of Claude Code's new task system (v2.1.6+), which replaces todos with JSON-backed tasks that support dependencies, sub-agents, and shared task lists across sessions; compared against Beads and the Ralph Wiggum loop.

- Techniques: Plan file to tasks, then sub-agent execution; Shared task list across sessions via env var; Version-control task state
- Tools: Claude Code (v2.1.6+), Beads, Ralph Wiggum loop, Opus 4.5, XDL (CLI for downloading videos from X/Twitter, used as the demo project), Better Stack

## [Claude Code's Creator Does This Before Every Single Project](../videos/B-UXpneKw6M.md)
`B-UXpneKw6M` · AI LABS · 2026-02-02 · q2 · practitioner · tutorial · also: testing-verification, context-engineering, multi-agent

Boris, who created Claude Code at Anthropic, shares a short workflow: give the agent a way to verify its work, keep CLAUDE.md lean and team-maintained, use plan mode and scoped permissions, and run parallel or background sessions.

- Techniques: Verification line in CLAUDE.md; Tests-first or tests alongside each feature; Browser or screenshot verification for UI; Team-maintained CLAUDE.md; Mistakes from PR review go into CLAUDE.md; Project-scoped allow/ask/deny permissions; Plan mode before execution; Parallel sessions with numbered tabs; Cloud background agents with teleport; Background verification tasks; Stop hook for verification; Loop plugin for autonomous runs; Per-language linters and formatters; Committed slash commands; Narrow subagents
- Tools: Claude Code, CLAUDE.md, Claude Code GitHub action, Claude Code on the web (cloud sessions), Claude browser extension, Opus 4.5, Sonnet, Haiku, Ralph Wiggum plugin, MCP servers (Slack, Notion), BigQuery CLI, Sentry CLI

## [I Can't Believe Anthropic Messed Up The Ralph Wiggum](../videos/XVAhQ-EcrWA.md)
`XVAhQ-EcrWA` · Better Stack · 2026-02-02 · q3 · practitioner · tutorial · also: agent-architecture, context-engineering, coding-agents

Better Stack explains the Ralph loop (a bash while-loop that reruns one prompt with a fresh context each time) and why the official Claude Code Ralph plugin, with compaction and iteration caps, drifts from the canonical design.

- Techniques: Fresh-context bash Ralph loop; Plan-file task selection; Keep fixed context small; Human-on-the-loop review; GitHub-issues task queue; Filter error output with an MCP server
- Tools: Ralph loop (bash while-loop pattern), Claude Code, Claude Code Ralph Wiggum plugin (Anthropic, slash command with max iterations and completion promise), agents.md, Raz Mike's Ralphie bash script, agent-browser tool (named Vasell in the captions), GitHub issues, Better Stack MCP server (log and frontend error search), GPT-5 tokenizer (used for a token-count comparison)

## [Claude Now Builds Custom Interfaces to Plan Your Life](../videos/jRBiWoSKpIo.md)
`jRBiWoSKpIo` · Better Stack · 2026-02-02 · q2 · intro · review · also: coding-agents, mcp-and-tools

A 4-minute demo of Claude Canvas, an open-source Claude Code plugin that opens tmux split panes rendered with Ink to preview emails, flights and calendar items, with the pane sending user choices back to Claude. The data shown is invented, and the "future of terminal assistants" claim is opinion.

- Techniques: Skill-routed CLI that spawns a split pane; Preview a draft in a pane before sending; Bidirectional pane-to-agent IPC for user selections
- Tools: Claude Code, Claude Canvas (Claude Code plugin), tmux, bun, Ink, Ghostty, iTerm, Apple Terminal, Gmail MCP server (mentioned as a possible source of From/To fields, not demoed), Astro (creator mentioned as suggesting generated UI)

## [ShadCN is Way too Powerful Now](../videos/MFJ0mH72_qI.md)
`MFJ0mH72_qI` · AI LABS · 2026-02-02 · q2 · practitioner · tutorial · also: testing-verification, agent-architecture, context-engineering

Ralph stop-hook loop plus TDD and screenshot checks for ShadCN UI work; a separate verification iteration before the completion promise fixed premature "done" claims.

- Techniques: Stop-hook completion-promise loop; Test-first workflow inside the loop; Screenshot verification protocol; Two-phase completion gate
- Tools: ShadCN (UI component library), Claude Code, Ralph plugin (Anthropic, Ralph loop), Claude Code stop hooks, Playwright, Playwright MCP (named only to say it was not used), Notion (reference point for the board view), Automata (sponsor)

## [I Couldn't Believe Claude Tasks Could Do This](../videos/li8bIt-mjbA.md)
`li8bIt-mjbA` · AI LABS · 2026-02-02 · q2 · intro · review · also: multi-agent, agent-architecture, coding-agents

Walkthrough of Claude Code's new built-in task system: a coordinator splits work into a dependency graph, runs independent sub-agents in parallel, and persists tasks outside the context window so they survive /clear and restarts.

- Techniques: Explicit dependency breakdown prompt; Fan out independent sections of a spec; Named long-running sessions; Inspect task state on disk; Batch folder documentation with Cowork; Research-then-implement handoff
- Tools: Claude Code, Cowork, Claude Chat, Opus 4.5, Haiku, Sonnet, CLAUDE.md, Notion, Lovart (sponsor segment, not evaluated)

## [Anthropic's Latest Move: Why OpenCode Users Are Worried](../videos/vLecpJt_8jM.md)
`vLecpJt_8jM` · Better Stack · 2026-02-02 · q2 · intro · news · also: coding-agents, token-cost-efficiency, governance-compliance

Speaker reports Anthropic restricting Claude Pro/Max subscriptions to Claude Code, hitting third-party agents like OpenCode, and describes a temporary tool-name workaround. Mostly speculation.

- Techniques: Keep the harness model-agnostic and route each workflow to a cheaper or better model; Use subscription quota first, then fall back to API billing; Tool-name prefix workaround reported by OpenCode (unverified; the speaker says it is temporary)
- Tools: Claude Code, Claude Pro, Claude Max, Claude Opus 4.5, OpenCode, OpenCode Black, OpenCode TUI, ClaudeBot, Ralph loop, npm, GitHub, OpenAI models

## [The Greatest Problem With AI Coding Is Solved](../videos/3FZIdRZsUMM.md)
`3FZIdRZsUMM` · AI LABS · 2026-02-02 · q2 · intro · talk · also: context-engineering, testing-verification, coding-agents

AI LABS argues the implementation middle of software work is being replaced by agents, so developers should focus on planning, context setup, and reviewing or testing agent output.

- Techniques: Refine the plan, then run one-shot implementation; Split spec into per-concern documents; Test-first with a context reset and locked tests; Black-box testing from user stories with a browser agent; White-box review with an XML test plan and a slash command; Layered project structure for agents
- Tools: Linear, Dart AI, VS Code, Claude Code, Claude Chrome extension, Cursor, Slack, CLAUDE.md, skill.md, MCP, XML

## [How I Made Claude Code WAY Better With Vercel Agent Skills](../videos/PkeC2hNQ9Zw.md)
`PkeC2hNQ9Zw` · Better Stack · 2026-02-02 · q2 · intro · review · also: skills-self-improvement, coding-agents

Better Stack explains the Agent Skills format, Vercel's add-skill installer and skills.sh discovery, and Cloudflare's proposed well-known skills index, then closes with a sponsor read.

- Techniques: Write a skill file with frontmatter; Install one skill into several agents; Discover skills by popularity; Publish a skill index at a well-known path (proposal)
- Tools: Claude Code, Agent Skills (Anthropic), add-skill (Vercel, npx add-skill), skills.sh, Cloudflare well-known skills index proposal, Cursor, Wrangler, Remotion, React Native skills, Better Stack

## [Claude Cluster is Insane… Upgrade Your Claude Code Workflow ](../videos/V-xBaFveTvA.md)
`V-xBaFveTvA` · AI LABS · 2026-01-02 · q2 · intro · review · also: multi-agent, coding-agents, dev-tools

AI LABS walkthrough of Claude Code background subagents, using git worktrees to run parallel agents on isolated branches, plus a few changelog features. Hype title, sponsored segment, and shallow on mechanics.

- Techniques: Background a research or review subagent; Parallel review fan-out; Worktree-per-agent via a custom slash command; Named project agents via --agent flag; Fork a session on resume; Keep background tasks isolated and named
- Tools: Claude Code (background agents, tasks command, --agent flag, resume flag, custom slash commands, instant auto-compact, prompt suggestions), git worktree

## [Claude Ralph - The Bizarre Anthropic Plugin That Every Developer Is Missing](../videos/ny_BAA3eYaI.md)
`ny_BAA3eYaI` · Better Stack · 2026-01-02 · q3 · intro · review · also: coding-agents, agent-architecture, token-cost-efficiency

Walkthrough of the Ralph Wiggum Claude Code plugin, which re-runs the same prompt through a stop hook until a completion promise appears, with a max-iterations cap as a cost guard.

- Techniques: Ralph-style re-prompt loop (manual); Ralph Claude Code plugin with stop hook; Iteration cap as a spend limit; Tests in the prompt file as the completion gate; Decompose before looping
- Tools: Claude Code, Ralph Wiggum plugin (Anthropic Claude Code plugin, /ralph command), Claude Code stop hook, AMP (agent named as a comparison; no details given), bun test (Bun test runner), beads (suggested pairing, not demonstrated), TypeScript, Python

## [Claude Just Introduced a New Way To Fix Your UI](../videos/eLDq5TfIHys.md)
`eLDq5TfIHys` · AI LABS · 2025-12-02 · q2 · practitioner · review · also: skills-self-improvement, context-engineering, vibe-coding-app-building

AI LABS tests Anthropic's front-end design skill guidance in Claude Code: typography and theme prompts, a 400k-token mega-prompt, and skills that often fail to auto-load.

- Techniques: Turn a design prompt into a project skill; Force-invoke the skill by name; Describe design as implementation, not taste; Name the fonts explicitly; Stage the design prompt per dimension, then combine; Artifacts builder skill for componentized output
- Tools: Claude Code, Claude skills, Claude desktop app, Google Fonts, React, shadcn-style UI (as generated by Claude), Zen Browser, Arc Browser, Anthropic front-end design cookbook, Claude Code front-end design plugin

## [I Was Using Claude Skills Wrong... The Ultimate System](../videos/fHGMA8hLNt8.md)
`fHGMA8hLNt8` · AI LABS · 2025-12-02 · q2 · intro · review · also: skills-self-improvement, context-engineering

A list of about 21 to 22 use cases for Claude Skills, from coding tasks like tests and CI/CD to business, personal and content workflows. Mostly unmeasured ideas, with a sponsor segment.

- Techniques: Skill folder with references, assets and scripts; Test-and-report skill; Clarify then generate; Template-driven document generation; Stateful skill with a maintained data file; Saved personal profile for planners
- Tools: Claude Code, Claude Desktop app, Claude Skills, Docker, GitHub Actions, npm package (unnamed), Appify (sponsor)

## [Claude 4 is HERE and is taking on Cursor... (Claude Code)](../videos/-Qdlg-dkrX8.md)
`-Qdlg-dkrX8` · Better Stack · 2025-11-02 · q3 · intro · news · also: coding-agents, models-research, mcp-and-tools

Better Stack's launch-day recap of Claude 4 (Sonnet 4, Opus 4) with a short Claude Code VS Code demo. It mostly relays Anthropic's benchmark and behavior claims, with light skepticism.

- Techniques: Claude Code inside VS Code or JetBrains via the CLI; Paste-the-error bug fix; Agent-maintained memory file; Remote MCP servers through the Claude API; One-hour prompt cache TTL; Tagging Claude Code in GitHub PRs
- Tools: Claude Opus 4, Claude Sonnet 4, Claude 3.7 Sonnet, Claude Code, Claude Code SDK, Claude API (remote MCP connector), VS Code, JetBrains IDEs, Next.js, Excalidraw, GitHub Copilot agent, Codex 1

## [How to 10X Your Claude Code Workflow](../videos/xhrqmAWI_cw.md)
`xhrqmAWI_cw` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, multi-agent, context-engineering

Walkthrough of a compound-engineering Claude Code plugin (plan, work, review, triage, codify, resolve commands) that persists to-dos and runs parallel review agents. Practical, but the 10X title is unmeasured.

- Techniques: Plan, work, review, triage, codify, resolve command loop; Built-in to-do tool as the phase ledger; Pause-per-phase human checkpoint; Context check before each phase; Language- and concern-specific parallel review agents; Dependency-graph parallel resolution of to-dos; Git ingest for Q&A on a repo; Install as a plugin via marketplace
- Tools: Claude Code, compound engineering (Claude Code plugin), Claude Code plugin marketplace, Claude Code built-in to-do tool, GitHub issues, git worktrees, git ingest, BMAD method (compared, not used), Next.js, FastAPI, Python, TypeScript

## [Time to UPGRADE... Agent OS Replaces 95% of AI Coding](../videos/0rK4-8TryBo.md)
`0rK4-8TryBo` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, context-engineering

Walkthrough of Agent OS for Claude Code and Cursor: base and tool installs, opinionated standards files, roadmap-driven builds, and spec/resume commands. Mostly one demo run; the 95% claim is unsupported.

- Techniques: Two-stage install; Edit the standards folder before the first plan; Plan-product prompt structure; Roadmap-driven build loop; create-spec for new features; Custom tool-routing rule for a component library; Resume with execute-task; Retrofit with analyze-product; Invoke rules by tool syntax
- Tools: Agent OS (spoken as AgentOS), Claude Code, Cursor, Next.js, pnpm, npm (avoided in demo), ShadCN UI, ShadCN MCP server, TweakCN (spoken as tweak cn)

## [Cursor AI Just Got a Massive Upgrade Over Claude Code](../videos/WKy71aZHx20.md)
`WKy71aZHx20` · AI LABS · 2025-11-02 · q2 · practitioner · review · also: coding-agents, token-cost-efficiency

A solo creator's hands-on comparison of Cursor's new agent features (plan mode, hooks, slash commands, worktrees, browser control) against Claude Code, concluding Cursor wins on usability and that subscribing to both is the best setup.

- Techniques: Share custom commands between Cursor and Claude Code; Plan first, then build; One git worktree per agent; Browser test-and-fix loop; Shareable prompt deep links; Guard auto-run with before/after tool hooks; Split models across two subscriptions
- Tools: Cursor, Cursor Auto mode, Cursor CLI, Claude Code, Claude Code VS Code extension, Claude Sonnet 4.5, Playwright, Playwright MCP, Conductor, Warp Code, Claude Router, Linear

## [How I Build Beautiful Websites With AI](../videos/1cB2iqz_vnM.md)
`1cB2iqz_vnM` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: coding-agents, vibe-coding-app-building, context-engineering

Walkthrough of Drawbridge, an open-source Chrome extension that turns clicks on a localhost page into a queued task list for Claude Code or Cursor, with landing-page and client-prototyping use cases. Main takeaway: UI fixes become batched, position-aware agent tasks.

- Techniques: Install Drawbridge as an unpacked Chrome extension; Queue element-level UI changes; Have the agent process the queue; Turn the Cursor workflow rule into a Claude Code slash command; Build a landing page section by section; Keep a design language in files the agent reads
- Tools: Drawbridge (open-source Chrome extension and visual editor for coding agents), Chrome (extensions, load unpacked), Cursor, Claude Code, shadcn/ui, TweakCN (shadcn theme site), Lumi (sponsored AI website builder), Git (used to revert the demo project)

## [Time to SWITCH...Claude Code vs Cursor debate just ended](../videos/tCy5cJRErTg.md)
`tCy5cJRErTg` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, dev-tools, mcp-and-tools

Walkthrough of Claudia, a build-from-source desktop GUI over Claude Code with custom agents, per-prompt checkpoints, a preview pane and GUI MCP setup, pitched as a reason to leave Cursor. Hype title; single-tool demo.

- Techniques: Read-only research subagent; Checkpoint before a risky AI change; Visual bug loop with a preview pane; Add MCP servers through a form; Build Claudia from source
- Tools: Claudia, Claude Code, Cursor, Rust, Bun, git, Next.js, shadcn/ui, Claude Pro plan ($20), MCP (stdio and SSE servers), CLAUDE.md, HTML

## [3 Ways to Make GENUINELY Stunning Websites Using Claude Code](../videos/McJluKfjVGk.md)
`McJluKfjVGk` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: vibe-coding-app-building, mcp-and-tools, coding-agents

A walkthrough of three Claude Code workflows for building polished UIs: SuperDesign for iterative design canvases, ShadCN MCP for component-library builds, and Firecrawl or Figma MCPs for cloning existing designs.

- Techniques: SuperDesign canvas setup; Layout-then-theme-then-polish staging; Targeted correction round; ShadCN MCP plus a saved usage-rule slash command; Theme import from tweakcn; Site cloning with Firecrawl MCP; Figma MCP selection import; Animation snippet import from Animatopy
- Tools: Claude Code, SuperDesign (superdesign.dev, VS Code / Cursor extension), Cursor, VS Code, ShadCN UI, ShadCN MCP server, Firecrawl MCP, Figma MCP server, tweakcn, Animatopy, Colors (palette generator website), Next.js

## [What Cursor Doesn't Have: Claude Code Subagents](../videos/Ppu6pJ5yyD4.md)
`Ppu6pJ5yyD4` · AI LABS · 2025-11-02 · q2 · practitioner · review · also: multi-agent, coding-agents, context-engineering

Walkthrough of Claude Code's native subagents: creating project agents with /agents, why isolated context windows help, and how auto-delegation and chaining work. Practical but thin, with a sponsor segment.

- Techniques: Create a project-scoped subagent with /agents; Write a specific description and scope tools tightly; Spec file plus rules file handed to a builder subagent; Theme swap through a subagent; Chain subagents in a custom slash command; Invoke a subagent explicitly
- Tools: Claude Code, Claude Code subagents (/agents), Cursor, ShadCN UI, ShadCN UI MCP server, Next.js, Tailwind CSS v3, TweakCN, TestSprite MCP server, BMAD workflow, SuperClaude workflow, GitHub subagents collection (unnamed)

## [Why Crush Is the Best‑Looking AI Coding CLI (RIP Claude Code?)](../videos/kCcCxzCSf_w.md)
`kCcCxzCSf_w` · Better Stack · 2025-11-02 · q2 · intro · review · also: coding-agents, dev-tools

A short hands-on look at Charm's Crush, a terminal AI coding CLI, compared against Claude Code and OpenCode on one React app prompt. It looks polished, but it trails on features and only supports API keys.

- Techniques: Same-prompt cross-CLI comparison; Permission modal: allow for session; Init a project memory file; Keyboard navigation in Crush; Configure LSPs and MCP servers in crush.json; Check where generated apps put API keys
- Tools: Crush (Charm terminal coding agent), OpenCode (original project, later renamed to Crush), OpenCode (SST, TypeScript version), Claude Code, Claude Sonnet 4, OpenAI Whisper API, Vite, React, LSP servers, MCP servers, crush.json, CRUSH.md

## [The BEST Way To Use Claude Code Anywhere (Thanks To Levelsio)](../videos/N434yhINnHo.md)
`N434yhINnHo` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: coding-agents, dev-tools

Better Stack walkthrough for running Claude Code on a cheap always-on Hetzner server and driving it from a phone via SSH or Mosh in Terminus or Termux.

- Techniques: Always-on remote Claude Code host; Terminus SSH host setup (iOS/Android); Termux setup (Android); Mosh for roaming and reconnects; Docker isolation for the agent
- Tools: Claude Code, Hetzner, Node.js, NVM, Terminus, Termux, Termux Style, OpenSSH, fish shell, Mosh, Docker, GitHub

## [The Cursor CLI is Actually Good!?](../videos/onaIazLEVi8.md)
`onaIazLEVi8` · Better Stack · 2025-11-02 · q3 · intro · review · also: coding-agents

Better Stack's hands-on head-to-head of the Cursor CLI beta against Claude Code on the same Sonnet 4 model: Cursor planned and implemented better, and the host recommends it for language coverage, IDE consistency and single-subscription setups.

- Techniques: Plan-only prompt before implementation; Shell command from inside the agent chat; Headless Cursor agent in CI; Review mode with file-scoped follow-ups; Rules file to prevent inline React components
- Tools: Cursor CLI (beta), Cursor Agent, Cursor IDE, Claude Code, Claude Sonnet 4, Next.js, Better T-Stack, GitHub Actions, OpenCode (mentioned for UI comparison), Vim, npm

## [Sonnet 4.5 Just Unlocked a New Breed of Agents](../videos/t7VuWwukO3I.md)
`t7VuWwukO3I` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: coding-agents, mcp-and-tools, agent-architecture

AI LABS walkthrough of running Claude Code as a scheduled GitHub Actions agent (model-news monitor to Slack) and as an issue-triggered background coder, with two rules learned from failed runs: auto-approve tools and test MCP servers first.

- Techniques: Install the Claude Code GitHub app into a repo; Scheduled news monitor on GitHub Actions; Whitelist all tools for headless runs (Rule 1); Verify MCP servers before automation (Rule 2); Post to Slack via incoming webhook with curl; Hand off a background coding task via a GitHub issue; Paste SDK documentation into the task; Verify auth end to end on a branch
- Tools: Claude Code (version 2 announced with Sonnet 4.5), Claude Sonnet 4.5, Claude Code GitHub app, GitHub Actions, GitHub, Slack (incoming webhook via curl), Supabase (auth), Supabase MCP server, Claude Agent SDK (TypeScript and Python docs), BMAD method (referenced), OpenAI Codex (referenced as inspiration for cloud agents), Cursor (referenced for code rewind), GPT-5 (mentioned in the opening)

## [Claude 3.7 Sonnet is INSANE + Claude Code? (Best Coding Model)](../videos/6KGH47rdeBs.md)
`6KGH47rdeBs` · Better Stack · 2025-11-02 · q2 · intro · review · also: coding-agents, models-research

Walkthrough of Claude 3.7 Sonnet's hybrid extended-thinking mode, its published benchmarks, and the Claude Code research preview, shown on a single demo project.

- Techniques: Toggle extended thinking in the chat UI; Set a thinking budget on API calls; Quick-start Claude Code on an existing project; Approve Claude Code actions with scoped trust; Have Claude Code create the commit; Custom scaffolding for SWE-bench-style agents
- Tools: Claude 3.7 Sonnet, Claude Code, Cursor, Gemini, DeepSeek, Next.js, TypeScript, Tailwind CSS, npm, git, SWE-bench, TAU-bench

## [How I ACTUALLY Use Claude Code... My Complete Workflow](../videos/7Sx0o-41r2k.md)
`7Sx0o-41r2k` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: multi-agent, context-engineering, coding-agents

A host walks through a multi-agent Claude Code workflow for building an app: specialized sub-agents run in sequence, each writing its output to docs, with checkpoints for rollback and a generated agent-workflow setup.

- Techniques: Phased sub-agent chain driven by one prompt; Parallel sub-agent fan-out; Docs-first planning with scoped agents; Two-stage requirements before agent planning; Rewind with double-Escape checkpoints; Generate an agent workflow from a repo; Verbose view of sub-agent activity
- Tools: Claude Code, Claude Code sub-agents, Claude Desktop, Claude Opus, Cursor (checkpointing, as cited by the host), BMAD method, SuperClaude, gitingest.com, Next.js, UX researcher agent, sprint prioritizer agent, UI designer agent

## [Wait... Cursor AI Just Launched a New Agent?](../videos/QOJdhje6Vnc.md)
`QOJdhje6Vnc` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, models-research

Hands-on first look at Cursor's new terminal agent CLI (beta) using GPT-5: install, slash commands, a Kanban app test, and why the host would not switch from Claude Code yet.

- Techniques: First-run setup for Cursor agent CLI; Switch models with /model inside the agent; Retry a stalled agent run with the same prompt; Fixed-prompt smoke test for a coding agent; Give visual feedback when the CLI cannot take images
- Tools: Cursor agent CLI (`cursor agent`), Cursor IDE, GPT-5 (OpenAI), Claude Code, Claude Code Router

## [TMUX Coding Is INSANE... Upgrade Your Claude Code Workflow](../videos/UgHbHqg_Wmo.md)
`UgHbHqg_Wmo` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: multi-agent, software-factory

Walkthrough of a tmux-based orchestrator that lets one Claude Code agent spawn and manage several Claude Code teams via scheduled check-ins, spec-driven phases, and a skip-permissions setting. Useful pattern, but the live demo never ran.

- Techniques: tmux-based agent orchestrator setup; Fix hard-coded paths and permission command in the orchestrator; Spec folder as the build blueprint; Team start prompt pattern; Scheduled check-ins with restore-point commits; Summarize an unfamiliar repo with GitIngest
- Tools: tmux, Claude Code, tmuxorchestrator (repo name as spoken), Cursor (used only to show the folder structure on screen), shadcn, shadcn MCP, GitIngest (gitingest.com), ChatGPT (mentioned as a comparison for the summary step), Git (version control and restore-point commits)

## [Time to SWITCH… 20X your Claude Code Workflow](../videos/PRqHKpTHQVE.md)
`PRqHKpTHQVE` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, models-research

AI LABS compares Claude Opus 4.1 with Opus 4 inside Claude Code on two single-run builds (a Pac-Man game and a ShadCN/Framer Motion site); the 4.1 gains look real but the evidence is anecdotal.

- Techniques: Identical-prompt A/B across model versions; Requirement checklist for generated UI; Model upgrade inside Claude Code; API model-name swap
- Tools: Claude Code, Claude Opus 4.1, Claude Opus 4, Claude Sonnet 3.7, Claude Sonnet 4, shadcn/ui, Framer Motion, SWE-bench Verified

## [3 Simple Ways To EARN Money With Claude Code Apps](../videos/Y2oK0nubq9A.md)
`Y2oK0nubq9A` · AI LABS · 2025-11-02 · q2 · intro · review · also: product-ux, vibe-coding-app-building

Walkthrough of consumer-app paywall patterns (instant-value previews, habit hooks, usage caps, tier ladders) plus a Claude Code design-command workflow for cloning paywall screens. Middle segment is sponsored.

- Techniques: Progress-gated free tier for education apps; Anchored yearly pricing; Progress hook with time or feature gating; Usage cap at point of need; Three-tier ladder with a highlighted middle; Slash-command design pass for prototypes; Screenshot-to-clone reference
- Tools: Claude Code, Cursor, VS Code, SuperDesign, design.md (prompt file), Flowbite, Paywall Screens, Make, HabitKit, Sleep Cycle, Babbel, CapCut

## [How Claude Solved AI's Biggest Problem](../videos/Z9glbip8pZc.md)
`Z9glbip8pZc` · AI LABS · 2025-11-02 · q3 · intro · review · also: skills-self-improvement, mcp-and-tools, context-engineering

Walkthrough of Claude Skills: SKILL.md folders loaded on demand, how they differ from MCP, building one with skill-creator, and HTML visualization widgets. Mostly demo, with one sponsor segment.

- Techniques: Skill folder layout; Keep the description one line; push detail into referenced files; Install shared skills into Claude Code; Bootstrap a skill with skill-creator; Visualization widget skill
- Tools: Claude Skills, Claude Desktop app, Claude Code, skill-creator skill (Anthropic skills repo), MCP builder skill, MCP, Figma MCP server, Figma API, PDF Extractor skill, Algorithm art skill, Canvas design skill, Word, PDF, Excel and PowerPoint document skills

## [This One Claude Code Feature Replaced My ENTIRE Team (Subagents)](../videos/zYPNfkDxgMg.md)
`zYPNfkDxgMg` · Better Stack · 2025-11-02 · q2 · intro · review · also: multi-agent, context-engineering

Walkthrough of Claude Code's Custom Subagents (v1.0.60+): creating a read-only reviewer agent via the agents command, then running about ten subagents from one prompt, with token and time costs.

- Techniques: Create a personal-scope read-only reviewer subagent; Restrict a subagent to specific MCP tools; Delegate a task to a named subagent in the prompt; Batch several subagents in one prompt
- Tools: Claude Code (v1.0.60 or later, Custom Subagents), Claude Code agents command, GitHub (agent sharing), Claude Max subscription (speaker's plan; he notes the API would cost much more)

## [Claude Code Tutorial: Full Setup, MCP, and Cursor AI Integration (Claude Squad Guide)](../videos/u-GGktUnSgg.md)
`u-GGktUnSgg` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, multi-agent

Tutorial on running Claude Code inside Cursor and installing Claude Squad to run several Claude Code instances in tmux; the IDE link fails on camera and the MCP in the title is never covered.

- Techniques: Install Claude Code and open it in Cursor; Check the IDE connection from Claude Code; Install Claude Squad; Prepare a repository for Claude Squad; Run parallel sessions for front end and back end; One-shot build prompt that yields a to-do list
- Tools: Claude Code, Cursor, Claude Code extension for Cursor, Claude Squad (cs), tmux, GitHub CLI (gh), git, GitHub, OpenAI Codex, Claude Opus, Claude Max plan, Claude Pro plan

## [The GPT-5 Backlash, AI CLI Tools & AI Agent Protocols | Better Stack Podcast Ep 1](../videos/no8ijoB4qxM.md)
`no8ijoB4qxM` · Better Stack · 2025-11-02 · q2 · intro · other · also: coding-agents, mcp-and-tools, evals

Better Stack podcast on GPT-5's messy rollout, Claude Code's lead among CLI coding tools, benchmark contamination, and why MCP won while rival agent protocols stalled. Opinion-heavy, little hard data.

- Techniques: Benchmark contamination check; Plan with the strong model, execute with the cheaper one; Turn an existing REST API into an MCP server; Convert web pages to Markdown before sending them to the model; Pair a strong general model with a browser MCP server; Custom Claude Code status line
- Tools: GPT-5, GPT-5 medium, GPT-5 high, OpenAI Codex (Codex CLI), Claude Code, Claude Sonnet, Claude Opus (4.1), Cursor, GitHub Copilot, VS Code, Goose, OpenCode (SST)

## [Claude Code Is an MCP Now?...3 CRAZY Things You Never Saw Coming](../videos/diTuQaSJ3nI.md)
`diTuQaSJ3nI` · AI LABS · 2025-11-02 · q3 · practitioner · review · also: mcp-and-tools, multi-agent, token-cost-efficiency

Community tools that extend Claude Code: calling it as an MCP server from Cursor, routing it to other models (Kimi K2 via OpenRouter), a multi-agent "hive mind" mode, and a dedicated Claude Code Chat extension.

- Techniques: Expose Claude Code as an MCP server and call it from another client; Canvas-to-code handoff from Claude Desktop; Route Claude Code to OpenRouter models with Claude Code Router; Hive mind multi-agent sessions in Claude Flow; Dedicated Claude Code Chat window in the editor
- Tools: Claude Code, Claude Code SDK, Claude Code MCP server (community wrapper, unnamed in video), Claude Code Router (ccr), Cursor, Claude Desktop, Claude 3, OpenRouter, Kimi K2, Gemini, OpenAI models, DeepSeek

## [3 Things I Wish I Knew Before using Claude Code](../videos/_9T-6dw-CZs.md)
`_9T-6dw-CZs` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools, coding-agents, context-engineering

A beginner-level walkthrough of five Claude Code features: custom slash commands, Cursor integration with multi-line input, adding MCP servers (Sentry example), plan mode with CLAUDE.md, and the "ultrathink" keyword.

- Techniques: Custom slash command as a prompt file; Claude Code inside Cursor; Add an MCP server from an existing Cursor or Windsurf JSON config; Use MCP server commands from slash commands; Plan first, then save rules to CLAUDE.md; Add 'ultrathink' to a prompt for hard problems
- Tools: Claude Code, Cursor, Windsurf, Sentry, Sentry MCP server, Seer (Sentry AI agent), Claude Agent SDK, Claude GitHub app

## [Claude Sonnet 4.5 is HERE + Claude Code Upgrades](../videos/dDsa7_G7djc.md)
`dDsa7_G7djc` · Better Stack · 2025-11-02 · q3 · practitioner · news · also: coding-agents, models-research, context-engineering

Better Stack's roundup of Anthropic's Claude Sonnet 4.5 launch and Claude Code 2.0 updates (VS Code extension, checkpoints, prompt history), with a one-prompt comparison against GPT-5 and Sonnet 4.

- Techniques: Rewind to a checkpoint in Claude Code; Search prompt history with Ctrl+R; Use the VS Code extension with editor context; Compare models on one prompt in the same harness; Enable context editing and the memory tool in the Claude API
- Tools: Claude Sonnet 4.5, Claude Sonnet 4, Claude Code 2.0, Claude Code VS Code extension, Claude Agent SDK (renamed from Claude Code SDK), Claude API context editing, Claude API memory tool, Imagine with Claude (research preview), Claude in Chrome extension, GPT-5, GPT-5 Codex, OpenCode

## [Claude Engineer is INSANE... Upgrade Your Claude Code Workflow](../videos/6Rg5M69bMgQ.md)
`6Rg5M69bMgQ` · AI LABS · 2025-11-02 · q2 · intro · review · also: context-engineering, coding-agents, mcp-and-tools

A walkthrough of two free add-ons for Claude Code: the SuperClaude configuration framework (slash commands, flags, personas, MCP-wired workflows) and a basic browser web UI for reaching Claude Code from other devices on the LAN.

- Techniques: Install SuperClaude from its GitHub repo; Have an AI write a usage guide from the framework's own config; Turn a phase into a runnable slash command plus prompt; Wire MCPs yourself, then reference them through flags; Reach Claude Code from a phone on the same LAN
- Tools: SuperClaude (configuration framework for Claude Code; no version stated), Claude Code, Cursor (used to read config and generate docs.md), Context7 MCP, Sequential MCP, Magic UI MCP, Puppeteer MCP, React, Next.js (spoken as 'xjs'), ElevenLabs API, OpenAI API, Warp (terminal, used to get the LAN IP)

## [Wait.. Claude Code is MADE Slow on Purpose? Heres How to Fix It](../videos/wYWyJNs1HVk.md)
`wYWyJNs1HVk` · AI LABS · 2025-11-02 · q2 · intro · review · also: context-engineering, mcp-and-tools, token-cost-efficiency

Walkthrough of installing the Serena MCP (semantic code retrieval over a project index) and a Claude Code usage monitor, to keep Claude's context window focused and token use lower; the title's "made slow on purpose" claim is not supported in the video.

- Techniques: Per-project Serena MCP install; Index the project before using Serena; Prime Claude with Serena's instructions; Use the Serena dashboard for logs and clean shutdown; Track plan-window usage in a terminal tab
- Tools: Serena (MCP server for semantic code retrieval and indexing), Context7 (MCP for up-to-date library documentation), Claude Code, Cursor, Windsurf, uv (Python package runner used to install Serena), Claude Code usage monitor (terminal tool; name not stated in the transcript), Next.js, Python, Claudia and the Claude Code web UI (mentioned as alternatives)

## [Task Master AI Has Changed How I Code FOREVER (w/ Claude Code)](../videos/1I73OFAnvdg.md)
`1I73OFAnvdg` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: coding-agents, context-engineering, software-factory

Better Stack walkthrough of Task Master AI with Claude Code: a PRD is parsed into dependency-tracked tasks, scored for complexity, expanded into subtasks, then run one at a time. The demo app built in one pass, but the claims rest on one example.

- Techniques: Pick models per Task Master role; Have the model write the PRD from an example template; Parse the PRD into tasks, then score complexity and expand the hardest tasks; Drive the work loop by task status; Keep project hooks in the loop
- Tools: Task Master AI (taskmaster / task-master-ai), Claude Code, Claude Sonnet, Claude Opus, OpenAI API, Next.js, IndexedDB, MCP (mcp.json), fish shell, Git, bun, npm

## [Claude code vs Codex vs Cursor: Who gets the cake?](../videos/_Xbe7MQ2NxI.md)
`_Xbe7MQ2NxI` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, mcp-and-tools, agent-architecture

Argues Claude Code and other AI CLIs are "portable agent engines": terminal agents can call each other via bash, run headless (-p), deploy to GitHub Actions and act as MCP servers. Opinion-heavy, with a sponsor segment.

- Techniques: Headless single-shot invocation; Cross-agent delegation through bash; Scheduled agent via GitHub Actions; Claude Code GitHub app for PR review; Mixed local and remote MCP servers
- Tools: Claude Code, Claude Code GitHub app, Claude Code for Chrome, Claude for Excel, Agent SDK (formerly Claude Code SDK), Codex CLI, Gemini CLI, Qwen Code (transcript: QuenCode), Cursor CLI, gitingest, GitHub Actions, Slack

## [Bash Apps Are INSANE… A New Way To Use Claude Code](../videos/1_twhMU9AxM.md)
`1_twhMU9AxM` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: coding-agents, context-engineering

Wrap any terminal CLI as a Claude Code agent via CLAUDE.md; builds a Git Agent on GitIngest and Click that stores repo context in the repo. Practical pattern, light on code.

- Techniques: Document a CLI as an agent tool in CLAUDE.md; Token-size gate before repo extraction; Persist extractions and analyses as repo files; Wrap an existing CLI in a Click command group; PRD-first build loop with Claude Code
- Tools: Claude Code, Claude Desktop, Cursor, GalleryDL, aria2, GitIngest (git ingest, open-source CLI with a GitHub URL mode), Git Agent (the speaker's own CLI wrapper, not released in the transcript), BMAD method (framework mentioned as a past featured video, not demoed), Click (Python CLI framework; auto-captions say Qlik), CLAUDE.md, ScaleKit (sponsor; OAuth and auth layer for AI apps)

## [I've Been Using the n8n MCP WRONG - The Correct Workflow](../videos/jUfpYmN9q6Y.md)
`jUfpYmN9q6Y` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: coding-agents, context-engineering, mcp-and-tools

Driving the n8n MCP from Claude Code works better with a phased, file-based workflow: plan, research, build and validate in separate sessions, delete-and-recreate on update, and OAuth instead of API keys.

- Techniques: Phased file-based workflow pipeline; Clear context between phases; Put standing rules in CLAUDE.md; Pre-build version and health check; Delete-and-recreate instead of in-place update; OAuth-first credentials; Single-node isolation debugging; Documentation re-check prompt
- Tools: n8n, n8n MCP server, Claude Code, Claude Desktop, Claude.md (CLAUDE.md), OpenAI node in n8n, Google Calendar node, Gmail, Google Cloud Platform, Brave Search (from the previous video), Gamma (sponsor segment)

## [Sora 2 Cameos & Jailbreaks & Claude Agent SDK | Better Stack Podcast Ep. 5](../videos/YjdMscni2CI.md)
`YjdMscni2CI` · Better Stack · 2025-11-02 · q2 · intro · panel · also: agent-architecture, voice-multimodal, context-engineering

Better Stack podcast: hosts riff on Sora 2's cameo feature, memorized training data and weak guardrails, then on the Claude Agent SDK for custom agents with their own prompts, tools and hooks. Mostly opinion.

- Techniques: Custom agent on the Claude Agent SDK with an owned system prompt; Local functions as agent tools in place of MCP tools; Hook-based output enforcement with automatic redo; Coaching agent that withholds answers
- Tools: Sora 2, VO3, Claude Agent SDK, Claude Code, Claude Code hooks, MCP, Claude Sonnet 4.5, Claude Opus, GPT-5, GPT-5 Codex, Codex, Grok 4

## [Codex CLI Has Just Got WAY Better!](../videos/Szi4SHB4nNs.md)
`Szi4SHB4nNs` · Better Stack · 2025-11-02 · q3 · intro · review · also: coding-agents, sandboxing-execution, mcp-and-tools

Better Stack tours the late-2025 Codex CLI update (Rust rewrite, ChatGPT login, sandbox and approval modes, config profiles) and candidly compares it with Claude Code.

- Techniques: Separate sandbox from approval when setting agent autonomy; Named config profiles in config.toml run with -p; Audit an agent run via the transcript view; Tune model and reasoning effort per task; Point Codex at an OpenAI-compatible endpoint for non-OpenAI models; Notify script for event alerts; Everyday workflow commands
- Tools: Codex CLI (OpenAI terminal coding agent), GPT-5, GPT-OSS, DeepSeek (tested, errored), AGENTS.md, config.toml, Ink (previous TypeScript UI), Ratatui (Rust TUI library), ChatGPT login, Codex VS Code plugin, Claude Code (comparison), Better Stack MCP (host plug)

## [Claude Code SDK: Build Real AI Apps with Python & MCP](../videos/h1AGjM9IeBM.md)
`h1AGjM9IeBM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, mcp-and-tools, pr-code-review

A short walkthrough of the Claude Code SDK (Python, with the docs' example script and a GitHub Actions demo) that frames Claude Code as a programmable subprocess. The example broke for the speaker, and the video shows no working SDK run beyond that.

- Techniques: Run Claude Code as a subprocess from Python; Cap agent iterations with max_turns; Attach external MCP servers to programmatic Claude Code; Mention-triggered issue-to-PR workflow in GitHub Actions
- Tools: Claude Code, Claude Code SDK (Python, TypeScript, CLI), ClaudeCodeOptions, query(), Cursor, GitHub Actions, Claude Code GitHub Actions workflow, Jira MCP server, Slack MCP server, pip

## [Auto Claude is HERE… Upgrade your Claude Code Workflow](../videos/ytn0aXK2gzE.md)
`ytn0aXK2gzE` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: testing-verification, dev-tools

AI LABS shows how to attach Claude Code hooks (formatter, linter, build, stop-sound) to settings.json, and how to have a general LLM draft per-language hook rules. Mostly a SwiftUI demo with a sponsor segment.

- Techniques: Post-edit hooks as hard quality gates; Feed check output back to the agent; Stop-event sound notification; Generate hooks from a rules file; Accessibility audit as a hook; Autonomous run from a task file
- Tools: Claude Code, Claude Code hooks (settings.json), ChatGPT (used to draft lint and format rules), swift-format, SwiftLint (swiftlint.yml), SwiftUI, SQLite (local database in the demo app), Prettier (example formatter for other languages), Black (Python formatter, example in the rule-to-hook walkthrough), BMAD method (mentioned as a better approach, not used), claude code rule to hook (GitHub repo, name as spoken; exact repo not confirmed), tools.md (presenter's reference file of Claude Code tools and execution points; not shown)

## [Program Claude Code to be your new UI Designer (+ works with any IDE)](../videos/TyGx277x9hQ.md)
`TyGx277x9hQ` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building, coding-agents, context-engineering

Walkthrough of using Claude Code plus ChatGPT planning to turn an HTML UI prototype into a SwiftUI iOS app and re-skin it in Apple's Liquid Glass style; practical but anecdotal.

- Techniques: Plan-in-chat, then execute in agent; Screenshot-to-HTML prototype; Conversion rules file; Style transfer from references; Visual bug reporting; Start from the native project template
- Tools: Claude Code, Claude 4 Sonnet, Claude Opus (Claude 4), Cursor (Max mode), ChatGPT, Xcode, SwiftUI, Swift, Next.js, HTML/CSS, iOS Simulator, Apple Liquid Glass design

## [Building Custom AI Agents Just Got EASIER - Claude Agent SDK](../videos/NsROagHaKxA.md)
`NsROagHaKxA` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: agent-architecture, mcp-and-tools, coding-agents

Better Stack walkthrough of the Claude Code SDK (now also called the Agent SDK): a single-prompt query, a streaming-input REPL, replacing the system prompt, and adding a custom MCP tool, all in one short TypeScript file.

- Techniques: One-shot query; Streaming-input REPL; Full system-prompt replacement; Appending to the system prompt; In-process custom MCP tool; Combined demo structure
- Tools: Claude Code SDK (the video also calls it the Claude Agent SDK in its title), Claude Code CLI, Claude Haiku (model option example), TypeScript, zod, MCP (createSdkMcpServer, tool), Bash tool (built-in), Glob tool (built-in)

## [10 Pro Claude Code Tips & Tricks NO ONE Shares](../videos/Br5Ofobq6Is.md)
`Br5Ofobq6Is` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, token-cost-efficiency, dev-tools

A 4-minute Better Stack listicle of ten Claude Code tips: phone notifications via hooks, permission and thinking-budget settings, CLAUDE.md emphasis, session recovery, parallel sessions, and cheaper model use. Quick ideas, few exact configs.

- Techniques: Stop/Notification hook for completion alerts and phone pings; Alias the skip-permissions flag and toggle it off with shift+tab; Deny read access to sensitive files at global or project scope; Thinking budget by keyword in the prompt; CLAUDE.md emphasis, file links and memory; Custom slash commands with chained arguments and nested folders; Session recovery with --continue, --resume and double-escape rewind; Parallel agents on git worktrees with Claude Squad or tmux; Browser access to a terminal with Vibe Tunnel; /clear on topic change plus a cheaper model
- Tools: Claude Code, CLAUDE.md, Claude Squad, tmux, git worktrees, Vibe Tunnel, Kimi K2, BetterStack

## [Agents.md Is HERE… 90% of AI Tools Will Use This Now](../videos/Pmc4OfSlhbE.md)
`Pmc4OfSlhbE` · AI LABS · 2025-11-02 · q2 · intro · news · also: context-engineering, coding-agents

Host argues OpenAI's AGENTS.md should become the single cross-tool agent context file, replacing per-tool rules files, and says Claude Code's absence is the gap. Includes a sponsor segment.

- Techniques: Single AGENTS.md as shared project context; Rely on the auto-loaded context file for session bootstrap
- Tools: AGENTS.md, CLAUDE.md, Model Context Protocol (MCP), Figma MCP server, Claude Code, OpenAI Codex, Gemini CLI, Qwen Code, Cursor, Windsurf, Kiro, GitHub Copilot

## [Build Sites That Sell 99% of Products with Claude AI](../videos/VtmBevBcDzI.md)
`VtmBevBcDzI` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: vibe-coding-app-building, context-engineering

A landing-page design walkthrough: reverse-engineer a strong v0 site, then steer Claude Code with named libraries (paper shaders, Framer Motion), Google Fonts, layout screenshots and SVG code. Mostly a practical tip list with a sponsor segment.

- Techniques: Reference-site reverse engineering; Named-library prompt with a focused context; Framer Motion for animations; Two-step gooey morph; One-word font accent; Layout from a gallery screenshot; SVG logos and icons as code
- Tools: Claude Code, v0, Cursor (mentioned as a tool to use, no steps shown), Paper Shaders (library for animated website backgrounds), Framer Motion (React version named), GitIngest ("Git Ingest", converts a repo to AI-readable text), Google Fonts, Landbook (layout and design gallery), ChatLLM by Abacus (sponsor)

## [Claude FINALLY Fixed AI Coding By Releasing This](../videos/oj44Vrh0XyM.md)
`oj44Vrh0XyM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: context-engineering, multi-agent, memory

Walks through four Claude Code context-engineering techniques from Anthropic's "Effective Context Engineering for AI Agents" paper: compaction, context editing and memory, structured note-taking, and subagents. Mostly a conceptual intro with small demos; the main takeaway is to pick the technique that fits the task.

- Techniques: Manual compaction with retain instructions; Persistent instruction via the # memory shortcut; CLAUDE.md as the project brief; Structured note files maintained by the agent; Coordinator plus specialist subagents
- Tools: Claude Code, Claude Sonnet 4.5, CLAUDE.md, Claude memory tool, ACI.dev Gate22 (open-source MCP gateway, sponsor), Anthropic paper: Effective Context Engineering for AI Agents

## [6 INSANE Repos I Wish I Knew Before...](../videos/tmj4_HhX7jI.md)
`tmj4_HhX7jI` · AI LABS · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, context-engineering, vibe-coding-app-building

Six-repo roundup for Claude Code and MCP: awesome-claude-code, BMAD agile agents, UI component libraries, GitMCP, FastAPI-MCP and mcp-use. Mostly quick pitches plus a mid-video sponsor segment.

- Techniques: Repo to remote MCP server via GitMCP; Expose FastAPI endpoints as MCP tools (fastapi_mcp); Use an MCP server from code with mcp-use; Repo dump into markdown as Claude Code context; BMAD staged agile agents; Pick UI components with the agent; Parallel Claude Code sessions and usage monitoring
- Tools: Claude Code, Claude Desktop, Claude Squad, Claude Code usage monitor, awesome-claude-code, BMAD method, Cursor, shadcn/ui (ShadCN), awesome-ui-component-library, Ant Design, Recharts, Next.js

