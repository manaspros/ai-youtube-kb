# context-engineering — 399 videos

*prompt/context design, CLAUDE.md/AGENTS.md, context windows, compaction, specs*

By channel: AI Engineer 211 · Kai Explains 15 · AI LABS 127 · Better Stack 46

**Synthesized guide:** [guides/context-engineering.md](../guides/context-engineering.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [Your AI Agent Wants Your Data. Here's How to Lock It Down - Jeff Smith, Oracle](../videos/LnQce-eHm8k.md)
`LnQce-eHm8k` · AI Engineer · 2026-11-01 · q3 · practitioner · review · also: mcp-and-tools, security-guardrails, data-engineering

Oracle's Jeff Smith on locking down agent access to databases: expose curated reports as MCP tools instead of raw NL-to-SQL, give agents a compact schema tool, and enforce identity-based row and column security inside the database.

- Techniques: Curated report catalogue exposed through two MCP tools; Three server modes: ad hoc SQL, custom tools and reports only, or both; Reveal report SQL to agents under a privileged scope; Action-grouped tools instead of single-purpose tools; Compressed deterministic schema-info tool; Generate schema annotations from enterprise documents; Identity-driven row and column filtering at the database; Diagnose production performance on a read-only standby
- Tools: Oracle AI Database, Oracle MCP server, MCP (Model Context Protocol), MCP apps (spec feature, speaker says added to the spec in July; Oracle plans a GUI for later this year), Claude, Codex, Gemini, LangChain, Azure Entra ID (spoken as 'Azure IntraID'), Oracle Data Guard, AWR (Automatic Workload Repository, Oracle performance report), Confluence

## [How to Decide What Your AI Agent Should Remember - Wojciech Pluta, Oracle](../videos/qq2Hm4XNRgI.md)
`qq2Hm4XNRgI` · AI Engineer · 2026-10-31 · q2 · intro · talk · also: memory, agent-architecture, security-guardrails

Oracle's Wojciech Pluta argues agent memory is a write path that needs a promotion gate with provenance, scoped memory tiers, and per-turn context cards. Vendor talk with a demo.

- Techniques: Memory promotion gate; Provenance plus supersede, not overwrite; Three-tier memory scoping; Per-turn context card; Enforce user isolation in the database layer
- Tools: Oracle AI Database, Oracle agent memory package (named as an early-year release; no version given)

## [Your AI Agent Starts Every Session Like a New Hire - Killian Carlsen-Phelan, Sonar](../videos/8vDzncmzxyg.md)
`8vDzncmzxyg` · AI Engineer · 2026-10-31 · q2 · practitioner · talk · also: coding-agents, testing-verification, security-guardrails

Sonar pitches Vortex, a plugin that gives coding agents project context before they write and runs deterministic checks on every edit, so issues are caught before PR review.

- Techniques: Pre-write context retrieval from a verifier; Per-edit plus end-of-turn verification hooks; Enforce on changed lines only, surface the rest; Explicit-permission rule for sensitive resources; Deterministic layer between AI reviews
- Tools: Sonar Vortex (Sonar's agent plugin, named in the talk), SonarQube (static analysis, CI scan, data-flow and security analysis), Sonar CLI and MCP clients, Claude Code, Codex, Antigravity, Guitar (Sonar's AI reviewer, named in the captions; the speaker did not cover it), Java (language guidelines used in the demo)

## [Catch the Bugs Your Code Review Misses - Killian Carlsen-Phelan & Taylor Luttrell-Williams, Sonar](../videos/wP3P89YB9fA.md)
`wP3P89YB9fA` · AI Engineer · 2026-10-30 · q2 · practitioner · review · also: pr-code-review, testing-verification

Sonar's hands-on workshop for Guitar, a PR-level verification agent that reviews agent-written code, diagnoses CI failures, auto-fixes and auto-merges. Vendor pitch with a usable setup walkthrough.

- Techniques: Install Guitar as a GitHub app and connect a repo; Fork the workshop repo with all branches and enable Actions; Open PRs against your own fork, not upstream; Apply Guitar fixes; Steer reviews with project context in .guitar/review; Write conditional rules in .guitar/rules; Turn on auto-merge safely with a branch ruleset
- Tools: Guitar (Sonar's code change verification agent, GitHub app, app.guitar.ai), SonarQube (called SonarCube in the transcript, static analysis), GitHub (PRs, Actions, branch rulesets, auto-merge), Jira, Linear, Slack, MCP (Guitar supports MCP connectivity for custom context), Python (sample Box Office ticketing app, orders.py, check-in.py)

## [This Is Microsoft's New Tool Finally Fixed Claude's Usage Limits](../videos/1kQ_1_QL5Es.md)
`1kQ_1_QL5Es` · AI LABS · 2026-10-29 · q2 · practitioner · review · also: token-cost-efficiency, claude-code, skills-self-improvement

Walkthrough of Microsoft's Token Economizer, a Claude Code plugin that learns per-project token waste (repeated mistakes, unused tools, stuck loops) and cuts it; reports 21-31% savings and a cold-start caveat.

- Techniques: Install the plugin for your agent; Enable micro skills only for your own projects; Per-project repeated-failure facts; Prune unused tools per project, then restore on demand; Measure the tool-definition overhead; Two-step stuck escalation; Seed a new tool from existing session history; Three-hook layout for an agent harness
- Tools: Token Economizer (Microsoft; Claude Code and Codex plugin, install from GitHub repo, version not stated), Claude Code, Codex (OpenAI), GitHub Copilot, Sonnet 5, Opus 4.8, Graft (map-based token saver, mentioned as a comparison, not shown in use), Data Impulse (sponsor; residential proxy network)

## [Why a One-Line Change Can Break Your Whole Stack - Cole Gannaway, Qodo](../videos/YqxpPI7YUjE.md)
`YqxpPI7YUjE` · AI Engineer · 2026-10-29 · q2 · intro · talk · also: pr-code-review, multi-agent, software-factory

A Qodo solutions engineer argues PR review is the bottleneck in AI software factories and needs cross-repo blast-radius context, independent reviewers and rules learned from past reviews. Mostly a product demo.

- Techniques: Blast-radius-aware review over a software graph; Rules learned from review comments; Pre-generation context injection; Independent, varied reviewers; Mid-run review checkpoints via skill; Ticket-linked PR review
- Tools: Qodo (spoken as Kodo), Jira, Linear, MCP servers, Claude Code, Anthropic models, OpenAI models, Bitwarden (example repo, open source password manager), CLI

## [We Kept Rebuilding Our AI Agent. Here's What Survived - Fuad Ali, Arize AI](../videos/YIhvrvHtonk.md)
`YIhvrvHtonk` · AI Engineer · 2026-10-28 · q4 · practitioner · talk · also: agent-architecture, memory, evals

Arize's PM on two years of shipping Alex, its in-product agent: keep the loop, plan, stop rule and memory in harness code, use small capped memory files, and treat production traces as regression tests.

- Techniques: Render the plan into the harness on every call; Explicit finish call as a harness gate; Tool results as pointers, not inline content; One small capped markdown memory file per user; Single model call instead of a loop for narrow features; Production sessions as living regression fixtures; Trace-reading agent for silent failures
- Tools: Arize AX, Alex (Arize in-product agent), Signal (Arize trace-reading agent), Sonnet 4.5 (auto-caption 'Sonic 4.5'), jq, Arize experiments

## [How to Build an AI Code Review Agent - Daksh Gupta, Greptile](../videos/4UtrRVtUN_g.md)
`4UtrRVtUN_g` · AI Engineer · 2026-10-26 · q4 · practitioner · talk · also: pr-code-review, token-cost-efficiency, testing-verification

Greptile co-founder Daksh Gupta walks through building a production AI code review agent: sandboxed test runs, historical bug catalogs, model inversion, a living code wiki for context, and tiered model routing to cut per-PR cost.

- Techniques: Prompt the reviewer for a catalog of bug types, not generic review; Historical-PR regression eval for the review agent; Model inversion for reviews; Codebase knowledge base indexed by subsystem; Dependency-rich sandbox with computer-use end-to-end tests; Tiered model routing across review subtasks; Model-agnostic harness for the review agent
- Tools: Firecracker, OpenCode, Pi, Codex, Claude Code, GitHub review API, GitHub, GitLab, Jira, Linear, Confluence, Notion

## [EGM: Google's New Way To Use Claude Code Is Insane](../videos/xxf6D9jynFw.md)
`xxf6D9jynFw` · AI LABS · 2026-10-26 · q2 · practitioner · tutorial · also: multi-agent, coding-agents, claude-code

Walkthrough of Google's EGM, a spec-first workflow where zero-context goldfish sub-agents critique a plan before any code is written, with install, bootstrap, review and drift steps for Claude Code. A sponsor segment caps quality.

- Techniques: Isolated-context plan critique; Multi-lens rubric reviewers; Fan-out with a single merged report; Staged plan authoring with per-section approval; Round-based review gate; Drift check against per-folder docs; Make per-folder docs agent-readable; Verify the installer's CLAUDE.md edits; Install by agent-specific command or by prompt; Command sequence
- Tools: EGM (Google Elephant Goldfish Model, free on Google's GitHub), Claude Code, Codex (named as a supported agent), Hydra (sponsor, video generation for app promos)

## [He Built the First Chatbot in 1966, Then Tried to Stop It (here's why)](../videos/O1Bab7biaGo.md)
`O1Bab7biaGo` · Better Stack · 2026-10-26 · q3 · intro · demo · also: security-guardrails, product-ux

Better Stack runs the 1966 ELIZA chatbot's original code on a Mac, explains how its keyword-rule engine and swappable script work, and ties its "Eliza Effect" warnings to today's chatbot attachment problem.

- Techniques: Keyword-ranked rule matching with pronoun reflection and template fill; Recall-on-no-match fallback; Separate engine from persona script, with runtime rule edits; Treat the script or system prompt as leakable
- Tools: ELIZA (1966 DOCTOR script), IBM 7094 (transcribed as 'IBM 1794' in the captions), SLIP list-processing language, Lisp (BBN clone), BASIC (1977 magazine version), ARPANET, ChatGPT, Inventing Eliza (MIT Press book, July release)

## [AI Writes the Code. So What's Left for Engineers? - Laurie Voss, Arize AI](../videos/kspZP5BgkEU.md)
`kspZP5BgkEU` · AI Engineer · 2026-10-25 · q3 · practitioner · talk · also: pr-code-review, product-ux, evals

Laurie Voss (Arize AI) argues coding agents have made code writing nearly free, so the bottleneck moves to code review, ops and security, and ultimately to defining what "good" means, which makes "product engineers" the lasting role.

- Techniques: Theory-of-constraints bottleneck mapping; Review only high blast-radius code; Automatic verification for cheap-to-check work; Turn reviewer feedback into rules; Mergeability benchmark instead of test pass rate; Measure outcomes, not output volume
- Tools: Claude Code, GitHub Copilot, Cognition Devin, Cursor Bugbot, OpenAI Codex, Claude, Pragmatic Engineer newsletter, Arize AI

## [Google's Harness² Is This the End of Harness Engineering?](../videos/yCgfyQmqhPM.md)
`yCgfyQmqhPM` · Kai Explains · 2026-10-24 · q4 · practitioner · review · also: skills-self-improvement, evals, token-cost-efficiency

Critical read of Google's Harness² paper, where a second model rewrites an agent's harness files through a Propose/Probe/Compose loop. Headline gains are measured against an empty harness with a frontier editor, and token cost runs 8x to 40x a plain run.

- Techniques: Propose, Probe, Compose harness editing; A/B probe before keeping any harness edit; Trigger line on every skill; Place guidance by cost: skill, then script, then sub-agent, then plugin, then always-on text; Reopen-and-verify rule before declaring done; Exact output path and filename rule; Forbid plain-text tool calls; Restrict network before running a self-improvement loop; Put a cap on multi-run loops
- Tools: Harness Square (Google Cloud AI Research paper, Oct 2026), GLM-5 (Z.ai), Gemini 3.5 Flash, Claude Opus 4.8 (editor and judge in the paper), Claude Code, OpenCode, CodeBuddy, Codex (OpenAI Codex agent), MetaHarness (Hugging Face legal tool), WorkBuddy (benchmark), Jobbench (benchmark), Harvey legal agent benchmark

## [Does Code Quality Still Matter? It Depends on This — Max Kanat-Alexander, Capital One](../videos/bU5gDVyu_28.md)
`bU5gDVyu_28` · AI Engineer · 2026-10-22 · q3 · practitioner · talk · also: software-factory, testing-verification

Max Kanat-Alexander (Capital One) argues code quality only matters for durable software: it's worth rigor when consequences, replacement cost, dependencies and maintenance are high, and rigor is cheaper when you standardize and automate it.

- Techniques: Place software on a durable-to-disposable spectrum; Make software more disposable on purpose; Standardize to reduce the cost of rigor; Build in-workflow tooling; Provide in-memory fakes for services; Turn lint rules to maximum from the start
- Tools: Chromium (example codebase), Linux (example Hello World)

## [Anthropic Just Revealed How Their Engineers Use Claude Code](../videos/92ZDgn8bgLM.md)
`92ZDgn8bgLM` · AI LABS · 2026-10-22 · q3 · practitioner · tutorial · also: claude-code, multi-agent, testing-verification

AI Labs video on Felix Rieseberg's article: get more from Claude Code by asking for outcomes, expert methods, varied viewpoints, an outside judge, and the tools to verify results.

- Techniques: Outcome-first prompt (altitude); Expert-method meta-prompt (depth); Impossible-sounding goal reframing; Outside judge via a second model; Noun-to-verb role discovery and sequential specialist sub-agents (range); Verification resources for agents
- Tools: Claude Code, Claude (Anthropic), Codex CLI, MCP (Model Context Protocol), GoLogin (sponsor segment, not a recommended tool), AI Labs Pro (paid community, mentioned in closing)

## [The AI Content System Behind 200M Views — Sarah Chieng, Cerebras & Cova Lee, OpenAI](../videos/CFbnVpSsDFQ.md)
`CFbnVpSsDFQ` · AI Engineer · 2026-10-22 · q3 · practitioner · workshop · also: skills-self-improvement, voice-multimodal, product-ux

Two creators (Cerebras and OpenAI DevEx) walk through a six-stage AI content pipeline: swipe-file ideation, voice-captured scripts, shot lists, agent-driven editing, captioning, scheduling and a periodic process-review skill.

- Techniques: Swipe-file reference library for agents; Build a voice skill from your own past content; Voice-first script interview; Outlier analysis against channel baseline; Two-pass shot list from a script; Organize footage before editing; Agent-driven editing via API or desktop control; Brand design system generated from your own videos; Background and visual enhancement with image generation; Fix mistakes with short inserts; Repurposing into short-form cut-downs; Scheduling with human approval; Remove AI tells from captions and prose; Weekly process-review skill
- Tools: ChatGPT, Codex (CLI, computer use; transcribed as 'Astra/Astro'), GPT-5.6 Sol Ultrafast (as named in the talk; runs on Cerebras at ~750 tokens/sec), Cerebras, Wispr Flow (transcribed as 'whisper flow'), Figma (MCP and plugins), Notion, Obsidian, HyperFrames (HeyGen), HeyGen (avatars), CapCut, Adobe Premiere

## [One Day, $1,000 in Tokens: An AI War Room for Legacy Code — Ford Prior, GEICO](../videos/DouK81O8R3o.md)
`DouK81O8R3o` · AI Engineer · 2026-10-21 · q4 · practitioner · talk · also: software-factory, multi-agent, enterprise-adoption

GEICO's Ford Pryor describes an AI "war room" for legacy code modernization: a roster of decision makers, a driver, and fleet-managed Claude agents that take a major change from goal to approved design and agent-callable APIs, with human gates along the way.

- Techniques: War room composition for a major change; Three-repo split of enterprise agent context; Goal-to-approval-to-build loop with a queue; Milestone artifacts plus deterministic gate checks; Taxonomy for modernization missions; Local bindings file for agents on a laptop; Cost guardrails for agent-run work
- Tools: Claude Code, Anthropic Code Modernization plugin, Fleet Kit (Anthropic-collaborated fleet manager, markdown rules; not open source yet), beads (per-agent state tracking), Claude artifacts (HTML worksheets), draw.io, Figma, Slack (mission channel), GitHub Issues (example queue), Fable (model, named in the talk), Sonnet 5.5 (model), Opus 4.8 (model, named as too weak for this steering)

## [Vercel's CEO Just Unveiled The Greatest AI Coding Workflow Ever](../videos/y2ifUC9_zuU.md)
`y2ifUC9_zuU` · AI LABS · 2026-10-20 · q2 · intro · tutorial · also: testing-verification, claude-code, security-guardrails

Recap of a Vercel CEO interview: judge progress by direction rather than volume, run a plan-drift "direction" check, and use breaker, first-time-user and E2E agents plus MCP-based feedback triage. Partly a sponsor segment, with thin detail.

- Techniques: Direction drift-check command; Specs-first project setup; Must-not-trade-off rules with runnable tests; Quality gate checklist; Breaker agent loop; First-time-user agent with a hook-restricted bash tool; E2E path agent with JSON results; DeepSec security scan; Feedback triage with MCP connectors
- Tools: Claude Code, CLAUDE.md, DeepSec (Vercel security scanner), Gmail MCP, Sentry MCP, Victor (sponsor, AI hire in Slack/Teams)

## [Is the Agent Harness Dead? — Jediah Katz, SpaceXAI](../videos/7Y4sbZgBdnc.md)
`7Y4sbZgBdnc` · AI Engineer · 2026-10-20 · q4 · practitioner · talk · also: agent-architecture, coding-agents, token-cost-efficiency

Jediah Katz (SpaceXAI, formerly Cursor's harness lead) argues the agent harness is not dead: smarter models absorb coding scaffolding, but the harness keeps unlocking new frontiers, handles runtime, trust, and cost, and is moving toward agents as building blocks.

- Techniques: Two-layer harness split; Shim registry with a removal bot; Event subscription primitive; Nudge guardrails for responsiveness; Efficiency tuning levers
- Tools: Cursor, Cursor Agent Harness, GrokBot, Grind Swarm, Rollouts, Claude Code, Pi, Codex, SWE-bench Lite, MLE-bench

## [Stop Telling Agents How](../videos/7T-gldvgfpo.md)
`7T-gldvgfpo` · AI Engineer · 2026-10-19 · q3 · practitioner · talk · also: agent-architecture, multi-agent, evals

OpenProse founders argue agents should be given declarative Markdown contracts plus triggers, not step-by-step prompts; the talk is largely a product demo of their hosted runner.

- Techniques: Contract-first workflow spec; Codify a golden trace into pinned steps; Event-driven job = contract + trigger; Fresh-session verifier against the contract; Kernel as a bootloader index; Templated multi-agent shapes; Cheap verifier or router (planned, not shipped)
- Tools: OpenProse, run.pros.md (hosted OpenProse runner), pros CLI (pros write, pros run), npx skills (skill install mechanism), Claude Code, Codex, Exa (search), DSPy (contrasted), n8n (contrasted), pi (agent harness without sub-agents, transcribed as 'pie'), Matt Pocock's skill workflow (grill-me, TDD) used as an example, Haiku (cheaper model mentioned)

## [Google Just Fixed AI Design By Releasing This](../videos/au2TI8sdq8E.md)
`au2TI8sdq8E` · AI LABS · 2026-10-19 · q3 · practitioner · tutorial · also: coding-agents, skills-self-improvement, testing-verification

Google's Stitch design tool now has a terminal CLI, so Claude Code can drive it through a brief-to-design-to-site workflow with review and story-review skills; the video is a tutorial-style walkthrough with a sponsor segment.

- Techniques: Stitch CLI install with the skill in .claude; brief.md interview before any design generation; Loop of generate, check, and re-prompt in Stitch; Build from Stitch via download of HTML, images and fonts; Two-stage review: design fidelity, then story quality
- Tools: Stitch (Google), Stitch CLI, Claude Code, Stitch skill, scrollytelling skill, design.md, brief.md, Whisperflow (sponsor)

## [Teach Your Agent to Prove It's Done — Nick Nisi & Zack Proser, WorkOS](../videos/q4WC4TowkBo.md)
`q4WC4TowkBo` · AI Engineer · 2026-10-18 · q3 · practitioner · workshop · also: testing-verification, evals, coding-agents

Build deterministic verifier CLIs and evidence "receipts" so coding agents can prove their own work is done, closing the loop without the human reading every line of code.

- Techniques: Per-app verifier CLI with subcommands; Deterministic end-to-end prove step with Playwright; System-one LLM judge for fuzzy outcomes; Doctor/preflight plus stale-proof detection; Centralized verifier gate on workflow nodes (CTX); Babysitter agent for PR follow-through; Generate many variants and select via eval; Saboteur/detective bug-injection test of the verifier; Evidence attached to PRs; Outcome-first prompting with clear stop conditions; Error messages written for agents; Post-deploy monitoring agent
- Tools: Playwright, Chrome DevTools, pnpm, GitHub CLI (gh), GitHub API, Cloudflare Workers, MCP, Reptile, CodeRabbit, Datadog, Claude Code, Pi

## [Memory-Aware Agent Harnesses for Anti-Money Laundering — Nacho Martinez, Oracle](../videos/KtBivPzmOM8.md)
`KtBivPzmOM8` · AI Engineer · 2026-10-17 · q3 · practitioner · workshop · also: agent-architecture, memory, rag-retrieval

Oracle workshop on memory-aware agent harnesses for AML: treat the harness (loop, memory tiers, skill retrieval, context budget) as the thing to engineer, not the frontier model.

- Techniques: Two-tier memory with promote-to-long-term; Vector-indexed skill and tool box with top-k retrieval; Hybrid keyword plus embedding retrieval with RRF; Compaction or summarization of old context; Skill distillation from past runs; Pre-vetted query tools instead of free-form SQL; Bounded agent loop for unattended runs; Stable request prefix for caching
- Tools: Oracle Database, OCI (Oracle Cloud), GitHub Codespaces, OpenAI chat completions API, vector store, MCP, RRF, Claude Code, Codex, Pi harness, Hermes agent, OpenClaw

## [Paving the Road to Production: Governed Enterprise AI Agents — Harish Gaggar, Credit Karma](../videos/tZycGA_Fbfo.md)
`tZycGA_Fbfo` · AI Engineer · 2026-10-15 · q3 · practitioner · talk · also: mcp-and-tools, security-guardrails, observability

Credit Karma's senior staff engineer walks through a governed enterprise agent stack: scaffolded agent repos, a central MCP gateway, risk-gated execution, per-run evals, PII blocking, and a context optimizer that cut token use about 90% in demos.

- Techniques: Dev-portal agent scaffolding; Gateway token exchange with namespace routing; Risk-classified plan graph with HITL gate; Thread, run and checkpoint memory; Severity-based redaction before every sink; Context pipeline: budget, re-rank, dedupe, compress; Per-run eval scoreboard with nested detail; Three-layer monitoring split
- Tools: LangGraph, LangChain, FastMCP, Redis, JWT, Docker, Kubernetes, OpenTelemetry, Grafana Tempo, Prometheus, ELK, Loki

## [The Cost of Accessibility in AI — Jemima Abu, CAIS](../videos/ZccJsdOE54M.md)
`ZccJsdOE54M` · AI Engineer · 2026-10-15 · q3 · intro · talk · also: skills-self-improvement, product-ux, testing-verification

Jemima Abu (CAIS) argues accessibility is cheaper when built in from the start with AI agents, backed by a one-off experiment (58% lower cost, one-third the time) using a custom accessibility skill.

- Techniques: Accessibility skill for coding agents; Pre-run self-audit against a checklist; Audit the codebase before introducing an agent; Reusable component library as an accessibility lever
- Tools: Figma, Chrome Modern Web Guidance skill, WebAIM (cited study)

## [How to Actually Tokenmaxx and Save Millions — Alvin Pane, OutRival](../videos/8g1N_a3h9H0.md)
`8g1N_a3h9H0` · AI Engineer · 2026-10-15 · q4 · practitioner · talk · also: token-cost-efficiency, evals, observability

Alvin Pane (OutRival) on cutting LLM token spend in production: measure baseline variance with a ceiling test, shrink prompts with DSPy-style optimization, downsize models, then gate release on paired shadow-deployment stats with a lower confidence bound above zero.

- Techniques: Ceiling test (self-agreement baseline); Prompt optimization as search (DSPy-style); Prefix-cache-friendly prompt structure; Split pipeline by model size; Paired shadow-deployment statistics
- Tools: OpenTelemetry, DSPy, Jeepa optimizer (as transcribed; likely DSPy's GEPA optimizer)

## [We Let Our Financial Planners Write the Agents — Matthew Ragone, Range](../videos/gpmze-6ueGU.md)
`gpmze-6ueGU` · AI Engineer · 2026-10-13 · q3 · practitioner · talk · also: enterprise-adoption, skills-self-improvement, product-ux

A financial planner at Range explains how non-engineers wrote Claude skills that drafts client work, using a five-step method: pick, teach, pack, test, ship.

- Techniques: Five-step skill build method; Narrated walkthrough as skill source; Ask-first and never-do sections in a skill; Background drafting while the expert is busy; Owner plus non-author reviewer for shared skills
- Tools: Claude

## [This Just Fixed Your Claude Code Setup's Biggest Flaw](../videos/jlEMo6Dsh9E.md)
`jlEMo6Dsh9E` · AI LABS · 2026-10-12 · q2 · practitioner · review · also: claude-code, testing-verification, token-cost-efficiency

Walkthrough of eight Claude Code add-ons, mostly from one vendor, that put an LLM yes/no judge at decision points: action gating, rule checks, stop gates, message routing, compaction, file shortlisting and SEO audits.

- Techniques: Judge-gated pre-action hook (Toolgate pattern); Rules-to-rubric compilation (Abide pattern); Completion gate with a confidence threshold (Belay pattern); Three-way routing of mid-run messages (Steer/Queue/Interrupt); Advised compaction timing; Shortlist-then-read file retrieval (Quicksilver pattern); Browser-driven test pass with judge verdicts; Site audit with a fixed checklist plus per-page judgment
- Tools: Claude Code, Codex, Jev (decision model; name as transcribed, provider TypeSafe), Toolgate, Abide, Jev Browser, Jev Belay, Jev Steer/Queue, Compact Advisor, Quicksilver, Jev SEO, OpenRouter

## [Burn Your Flags: Interactive CLIs for Agents — Mark Lummus & Navinkumar Patil, PayPal](../videos/aV_vgUSatqs.md)
`aV_vgUSatqs` · AI Engineer · 2026-10-12 · q3 · intro · workshop · also: coding-agents, mcp-and-tools

PayPal's developer tools leads run a live workshop where attendees make a coffee-ordering CLI work for agents. Main point: interactive prompts fail silently under agents, so CLIs need machine-readable side channels, injected context, and determinism.

- Techniques: Side-channel JSON interface for CLIs; Tmux driver for interactive CLIs; Context injection via a single input file; Deterministic CLI, reasoning outside; Have an agent build the solver
- Tools: tmux, Claude Code, Codex, Claude Agent SDK, Opus 4.8, Slack

## [Claude Mods Are Insane... You Need To Try These Right Now](../videos/ERNqRK6sMJY.md)
`ERNqRK6sMJY` · AI LABS · 2026-10-12 · q3 · practitioner · review · also: claude-code, multi-agent

AI LABS demos seven Claude Code "mods" they built (prompt enhancer, design picker, assumption reviewer, idea shelf, session dashboard, same-folder tracker, plain-language answers) and explains how to create and install them.

- Techniques: Build a mod from a prompt; Prompt enhancer before send; Assumption ledger with targeted correction; Visual option picker before a design choice; Two-pass answer rewrite with a cheap check
- Tools: Claude Code, Claude mods (Claude Code feature), plugin-authoring skill, Haiku model (answer rule check), Runway, Gen-4.5 (Runway video model, sponsor segment), Stride (AI LABS' own running-coach app, sponsor segment)

## [Claude Code Features That 90% Don't Know Exist](../videos/i6Q7bXnWGlM.md)
`i6Q7bXnWGlM` · AI LABS · 2026-10-12 · q3 · practitioner · tutorial · also: claude-code, token-cost-efficiency

Walkthrough of about 20 hidden Claude Code settings, commands and shortcuts for context hygiene, permissions, plan mode, multi-session work and model routing, with exact setting names.

- Techniques: Enable New Init; Import setup from another agent; Prompt audit after a model release; Prune skills by token cost and usage; Auto Mode Setup; Fewer permission prompts allowlist; Disable connectors and artifacts; Build eval and hillclimb for LLM apps; Clear context on plan accept and save plans in-repo; Output styles; Show thinking summaries; Focus mode; Branch, fork and subtask; Cross-session messaging; Ask User Question Timeout and notifications; opusplan model routing; Pin sub-agent model; Prompt-editing shortcuts
- Tools: Claude Code, Claude app (connectors, artifacts), Claude.md, Claude API command (prompt audit, build eval, hillclimb), Codex, Cursor, Opus, Sonnet, Scrimba Explain (sponsor)

## [How to Build Quality Gates into Agentic Coding Workflows — Nnenna Ndukwe, Qodo AI](../videos/-AKPRSYccJc.md)
`-AKPRSYccJc` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: pr-code-review, coding-agents, testing-verification

Hands-on workshop by a Qodo DevRel on wiring codified rules, skills, structured plans and deterministic gates into an agentic coding loop from planning through PR review and autofix.

- Techniques: Codified rules and skills pulled per phase; Structured high-level plan plus execution plan; Read-only plan mode with an explicit skill handoff; Local verification command as the gate; Audit skills during implementation; Review-findings autofix loop; Severity-tiered rules with merge blocking
- Tools: Qodo, Claude Code, Codex, Semgrep, Ruff, Pyright, Bandit, pytest, GitHub CLI, uv, conventional commits, git worktrees

## [The SDLC You Build Yourself — Andy Wong, Andrei Bocan & Shane Wolf, Atlassian](../videos/ojJXgXLUQFc.md)
`ojJXgXLUQFc` · AI Engineer · 2026-10-12 · q2 · intro · workshop · also: software-factory, pr-code-review, governance-compliance

Atlassian team walks through its AI SDLC stack (Jira Coding Agent, AI Reviewer, AutoDev, AI SRE, AI Planner) built on a shared context engine, with a hands-on workshop that was largely lost to Wi-Fi problems.

- Techniques: Org-wide standards as enforceable PR rules; Trained filter on review comments; Human-set authority flag on context sources; Acceptance-criteria self-check in a sandbox; Progressive migration with per-engineer quotas; Automation-triggered agent session per sub-ticket; Per-skill and per-subagent model selection; Spend caps and WIP limits on autonomous work
- Tools: Jira Coding Agent, AI Reviewer, AI AutoDev, AI SRE, AI Planner, Rovo Dev, Teamwork Graph CLI, Confluence, Bitbucket, Slack, Docker, Claude

## [SonarQube + OpenAI: Agentic Development — Killian Carlsen-Phelan, Sonar](../videos/bI8WyG9YB0I.md)
`bI8WyG9YB0I` · AI Engineer · 2026-10-12 · q3 · practitioner · demo · also: testing-verification, coding-agents, security-guardrails

A Codex deployment engineer and a Sonar developer advocate argue that agent "done" needs evidence, containment is not correctness, and feedback checks belong inside the agent loop, then demo SonarQube hooks, MCP and CLI wired into Codex.

- Techniques: Evidence-backed definition of done; Layered execution and artifact controls; Secret-blocking lifecycle hook; Guide, verify, solve loop (ACDC); Taint analysis across files; Changed-code-only verification for agent edits; Custom rules targeting agent-written code
- Tools: Codex (OpenAI coding agent CLI), SonarQube Cloud, SonarQube CLI, SonarQube MCP server, SonarQube Codex plugin / marketplace, Docker, Git Bash (for setup script)

## [Decoupling the Brain from the Hands: Claude Managed Agents (Part 1 of 4) — Anthropic](../videos/Uv0nAf_7tyU.md)
`Uv0nAf_7tyU` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: agent-architecture, sandboxing-execution, mcp-and-tools

Anthropic engineers explain how they split Claude Managed Agents into a session log, a harness "brain" and swappable sandbox "hands", then start a hands-on workshop building a first agent.

- Techniques: Brain / hands / session split; Credential-injecting egress proxy; Append-only event log with pluggable context strategy; Lazy sandbox provisioning; One container per task; Custom tools as an event round-trip
- Tools: Claude Managed Agents, Claude Platform console (quick start), Claude Code, MCP, Sonnet 4.5, Opus 4.5, Haiku, Sonnet

## [Parameter Golf with AutoResearch — Vayum Arora, Zhengyao Jiang, Dixing Xu & Dhruv Srikanth, Weco AI](../videos/7RFJRDYroic.md)
`7RFJRDYroic` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: evals, software-factory, agent-architecture

Hands-on workshop on autoresearch loops, where an agent edits code, a fixed eval scores each attempt, and only improvements are kept. Covers eval design, bounded runs, steerability and the Parameter Golf results.

- Techniques: Fixed-budget eval contract; Tree-of-attempts search with per-node diffs; Guidance file as the steering channel; Hidden validation set for contests and benchmarks; Constrained single-metric optimisation; Bridged session for direct steering
- Tools: Weco, Modal, Claude Code, Opus 4.8, OpenAI MLE-bench

## [The End of AI Hallucinations? Meta's New Fix (CLM's)](../videos/9-iiHFQyzuM.md)
`9-iiHFQyzuM` · Kai Explains · 2026-10-12 · q4 · practitioner · review · also: agent-architecture, token-cost-efficiency, local-ai

Meta/UW's Context Language Model lets the model prune its own context through a bash-edited file instead of harness summaries. Gains are mostly compute; KV-cache costs hurt local use.

- Techniques: Notes-file handoff for long agent runs; Context-as-file self-editing (CLM pattern); Keep edits rare and context small; Suffix Cache Reuse (paper's serving fix)
- Tools: Meta CLM paper (Context Language Model, Meta and University of Washington), Qwen 27B, Qwen 9B, Claude Sonnet, Claude Opus 5.5, GPT, bash, Python, SGLang, vLLM, llama.cpp, Ollama

## [You're Prompting Opus 5.5 Wrong (Anthropic's Guide to Mastering Opus 5.5)](../videos/5TNXByrtHc4.md)
`5TNXByrtHc4` · Better Stack · 2026-10-12 · q3 · practitioner · tutorial · also: claude-code, multi-agent

Better Stack walkthrough of Anthropic's Opus 5.5 prompting guide: state the finish line up front, drop "think carefully" lines, steer with CLAUDE.md stop rules, split audits across subagents, track tasks in a file, and handle safeguard flags.

- Techniques: One-message task with explicit finish line; Remove thinking-nudge lines; Ban specific styles for design; Queue follow-ups during a run; CLAUDE.md stop-rule; Sub-agent split with evidence check; tasks.md progress file; Structured end-of-run summary; Merge-blocker diff review; Cross-model review; Recover from safeguard flags; Answer quickly prompt
- Tools: Claude Code, Claude Opus 5.5, CLAUDE.md, tasks.md, OpenAI model (named Astra in transcript)

## [The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef](../videos/KhRjivBSwiw.md)
`KhRjivBSwiw` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: evals, data-engineering, mcp-and-tools

TypeDef's talk and workshop argue that data and code agents need a computed, traversable context graph; deterministic structure comes first, and agents still default to grep unless tools are shaped and measured.

- Techniques: Deterministic structure first, LLM last; Layered extraction ladder for code; Persistent typed graph with subgraph traversal; Blast-radius tool before edits; Incremental re-indexing keyed to changed files; Isolated data clones for evals, with injected bugs; Tool renaming and shape-matching; Consistency and adoption metrics; Many small focused LLM questions; Eval set pinned to a snapshot, with near-failing tasks
- Tools: Neo4j, Cypher, tree-sitter, rustdoc JSON, Pydantic AI, pydantic evals, Fennec, OpenRouter, Logfire, dbt, Snowflake, Databricks

## [Beyond RAG: A Relational Context Engine That Cuts Token Burn — Unblocked](../videos/ORVh4GivEU0.md)
`ORVh4GivEU0` · AI Engineer · 2026-10-11 · q3 · practitioner · demo · also: rag-retrieval, token-cost-efficiency, data-engineering

Unblocked (Peter) argues RAG misses structured questions, then builds a schema-aware query engine over a document store with validation and self-correction; the talk is a demo-heavy speed run.

- Techniques: Dynamic schema discovery by document sampling; Fuzzy identity resolution with LLM tiebreak; Validate-then-inject for generated queries; Bounded self-correction loop; Per-task context bundle with an A/B harness
- Tools: Claude, MongoDB, GitHub, Slack, Notion

## [Beyond RAG: Build a Relational Context Engine from Scratch — Peter Werry, Unblocked](../videos/spxoDAfh5ig.md)
`spxoDAfh5ig` · AI Engineer · 2026-10-11 · q4 · practitioner · workshop · also: rag-retrieval, data-engineering, security-guardrails

Peter Werry (Unblocked) builds a schema-aware natural-language-to-database-query engine from scratch, covering schema sampling, identity mapping, allow-list validation and an error-retry loop, as the structured half of retrieval beyond RAG.

- Techniques: Dynamic schema discovery by document sampling; Deny-by-default query validation; Error-feedback retry loop; Forced tool call for entity extraction, with a fallback; Fuzzy identity mapping; Date-aware prompting for temporal queries; Two-stage schema selection; Hybrid entry point, then structured queries; Webhook-driven ingest and re-embed
- Tools: MongoDB, Postgres (mentioned as a comparison with table definitions), GitHub, Linear, Jira, Slack, MCP, Levenshtein distance

## [RAG Needs a Map: Using GraphRAG to Retrieve Connected Context — Nyah Macklin, Neo4j](../videos/LJ2a9nX3vlo.md)
`LJ2a9nX3vlo` · AI Engineer · 2026-10-11 · q2 · intro · workshop · also: rag-retrieval, data-engineering

Neo4j workshop on GraphRAG: when vector RAG falls short (3+ hops, cross-document aggregation), how an LLM can build a knowledge graph, and how to pair vector search with Cypher in a Neo4j Aura agent.

- Techniques: Hybrid vector-plus-Cypher retrieval tool; Text-to-Cypher tool beside the search tool; Schema-pinned LLM entity extraction; Chunk, embed, extract, load pipeline; Direct Cypher audit after each rebuild; Grounding instruction to restrict the agent to graph content
- Tools: Neo4j, Neo4j Aura (free instance), Aura Agents, GraphAcademy, GraphRAG for Python (neo4j-graphrag), OpenAI (LLM and text-embedding-3-small), Cypher, GitHub Codespaces, VS Code

## [Building on the Codex Harness — Dominik Kundel, OpenAI](../videos/9WiBJRO84yY.md)
`9WiBJRO84yY` · AI Engineer · 2026-10-10 · q3 · practitioner · talk · also: coding-agents, agent-architecture, mcp-and-tools

OpenAI's Dominik Kundel shows how to build your own client on the open-source Codex app server, the JSON-RPC protocol that wraps the Codex harness, and gives three rules for customizing it safely.

- Techniques: Append developer instructions instead of replacing the system prompt; Deferred dynamic tools with tool search; Pin and bundle the harness binary; Per-thread config overrides; Integrate by delegating to the coding agent; Choose exec or app server by parallelism and interactivity
- Tools: Codex app server, Codex CLI, Codex exec, Codex desktop app, Python SDK (Codex), Agent Client Protocol (ACP), LM Studio, Ollama, Electron, Cloudflare Doom WASM renderer, T3 Code, Claude Code Codex plugin

## [Stop Prompting — Greg Pstrucha, Sentry](../videos/E3KbFLAGD6A.md)
`E3KbFLAGD6A` · AI Engineer · 2026-10-10 · q3 · practitioner · talk · also: testing-verification, coding-agents, pr-code-review

Sentry's Greg Pstrucha argues teams should stop re-prompting coding agents and instead codify repeated conventions as deterministic lint rules, skills checks, and policy-driven review loops.

- Techniques: Mine feedback to find lint-worthy rules; Custom AST lint rules with ast-grep or ESLint-style tools; Lint for schema sync; Validate code examples inside skill documents; Policy files plus per-policy sub-agent review loop; Hooks to run deterministic checks at the right moment
- Tools: ast-grep, ESLint, OxLint, Flake8, Clippy, Claude Code skills, OpenAPI schema, Django REST Framework, a plain-English lint tool transcribed as 'TaskLessware' (name uncertain from auto-captions)

## [Generation Is Cheap, Review Is Expensive: How to Stop Shipping AI Slop — Gabriel Martinez, G2i](../videos/6qkzlT962es.md)
`6qkzlT962es` · AI Engineer · 2026-10-10 · q3 · intro · talk · also: pr-code-review, software-factory, product-ux

Gabo (G2i) argues AI slop comes from generation outrunning judgment. His fixes are conventions, small reviewable chunks, visible accountability, and ORC, an orchestration workflow built around review.

- Techniques: Single canonical pattern per concept; Diagram-first review surface; Small reviewable chunks with explicit ownership; Built-in adversarial and planning gates before merge
- Tools: ORC (G2i's orchestration system, described only at a high level), Ruby on Rails (convention-over-configuration example), SQLite (quoted maintainer comment on PR maintenance cost)

## [Why Your Company Needs a Context Graph (and How to Build It) — Gil Feig, Merge](../videos/cSz7aL2nl2U.md)
`cSz7aL2nl2U` · AI Engineer · 2026-10-10 · q2 · practitioner · talk · also: memory, mcp-and-tools, rag-retrieval

Gil Feig (Merge) argues every company needs a "context graph" (a company brain of synced data, live lookups, memory, skills) and lays out how to route, cache, and trace it. Conceptual talk with a closing product plug.

- Techniques: Split retrieval: live MCP vs. synced vector cache; Router plus summarizer; Skills and memory first; Freshness SLA check on cache; Derived-context write-back; Bounded live pulls; Provenance metadata on every record
- Tools: MCP (Model Context Protocol), Zendesk, Jira, NetSuite, Stripe, Qualtrics, vector database (unnamed), Merge Unified, Merge Agent Handler, Merge Gateway

## [From Context to Memory: Your Agents Need a Real Memory Layer — Anders Swanson, Oracle](../videos/BIhiYL4U9_M.md)
`BIhiYL4U9_M` · AI Engineer · 2026-10-10 · q3 · practitioner · talk · also: memory, rag-retrieval, security-guardrails

Oracle's Anders Swanson argues agent memory should be a governed, typed database layer with redaction, hybrid retrieval, scoped access, and feedback loops, not files or bigger context windows.

- Techniques: Typed memory schema with per-type lookup; Write pipeline: redact, enrich, scope, embed, episode-link; Weighted hybrid retrieval with fused scores and provenance; Governance on write and on read; Feedback signals that rank and promote or demote memories; Expose memory as a runtime function
- Tools: Oracle AI Database, Oracle Python SDK for agent memory (speaker's; referenced, not shown), Claude Code, Codex, MCP, hooks, skills

## [Giving AI Agents Memory That Learns — Jake Broekhuizen, LangChain](../videos/KGFyOtl5ktI.md)
`KGFyOtl5ktI` · AI Engineer · 2026-10-09 · q4 · practitioner · talk · also: agent-architecture, memory, evals

Jake Broekhuizen (LangChain) argues agent memory is a read-write loop: capture traces, filter them into signal, and promote only the durable parts into long-term context, with human review for procedural memory.

- Techniques: Trace-to-memory capture, analyze, update loop; Classify memory into semantic, episodic and procedural buckets; Gate procedural memory updates with human review and evals; Check the hot path for memory staleness
- Tools: LangSmith, LangSmith Context Hub, LangChain, OpenClaw, HermesAgent

## [We Mapped 115 Microservices for Our Coding Agents — Kamalakannan Nandagopal, Postman](../videos/k2ClBT4aqAg.md)
`k2ClBT4aqAg` · AI Engineer · 2026-10-09 · q4 · practitioner · talk · also: coding-agents, evals

Postman's engineer describes an API context graph over 115+ microservices, grounded in code and telemetry, that improves coding-agent answers on API discovery, shape analysis and impact assessment, with a token-efficiency gain and a staleness warning.

- Techniques: Code- and telemetry-grounded API context graph; Retrospective PR-based eval with quality-vs-tokens plot; Context layer exposed as a skill next to a generic coding agent; Treat graph staleness as an eval regression; Run expensive architecture checks cheaper and earlier
- Tools: Postman API context graph, Claude Code, GitHub code search, Postman AI agent

## [Your AI Agent Has No Nervous System — Matt Gibiec, Dynatrace](../videos/YNT7Plf9KIg.md)
`YNT7Plf9KIg` · AI Engineer · 2026-10-09 · q2 · intro · talk · also: observability, coding-agents

Vendor pitch for Dynatrace's "Blue Box" agent, which argues AI coding agents need live environment context (service dependencies, production telemetry, change history) to avoid hallucinated or breaking changes.

- Techniques: Dependency-mapped local testing; Baseline-deviation alerts to the coding agent; Change-correlated incident triage; Context-scoped fix suggestion with human approval
- Tools: Dynatrace Blue Box

## [Why Bigger Context Windows Won't Save Your Agent — Elizabeth Fuentes Leone, AWS](../videos/DrfyORO8RqA.md)
`DrfyORO8RqA` · AI Engineer · 2026-10-08 · q3 · practitioner · talk · also: memory, agent-architecture

AWS speaker on why larger context windows don't fix agents; she covers externalizing big tool output, summarizing and isolating context, loop caps and async tool calls, using Strands Agents.

- Techniques: Memory pointer for large tool output; Summarizing conversation manager with a ratio and a keep-last-N; Tiered memory: short-term, vector long-term, entity graph; Shared invocation-state pointer for multi-agent swarms; Per-tool invocation cap; Async job start/check tool pair
- Tools: Strands Agents, FastAPI, MCP, Neo4j, AWS API Gateway, Amazon Bedrock, Ollama, Gemini, Anthropic, OpenAI

## [Why AI Agents Should Have Their Own Sandbox — Philipp Schmid, Google DeepMind](../videos/oWTEiYpxl80.md)
`oWTEiYpxl80` · AI Engineer · 2026-10-08 · q3 · practitioner · talk · also: sandboxing-execution, agent-architecture

Philipp Schmid (Google DeepMind) argues agents need their own managed, persistent sandbox per API call, shows Gemini Interactions and Agents APIs, and demos a remote Antigravity environment.

- Techniques: Environment snapshot as a reusable agent base; Persistent per-conversation sandbox with server-side state; Filesystem handoff between agents; File-based agent configuration; Mount sources into the sandbox
- Tools: Gemini API, Interactions API, Agents API, Google AI Studio, Antigravity agent, Gemini CLI (for agents, not a coding agent), Google Search tool, URL context tool, Nano Banana Lite, Omni Flash, Gemini TTS, Gemma

## [The Software Factory: From Bug Report to Production Code — Davis Palmie, Factory](../videos/exiwa9QbQXI.md)
`exiwa9QbQXI` · AI Engineer · 2026-10-08 · q3 · intro · talk · also: software-factory, governance-compliance

Factory's Davis Palmie argues engineers should build a "software factory" of agents that turns signals like bug reports into production code, starting narrow, measuring outcomes, and staying model- and surface-agnostic.

- Techniques: Narrow-first, verifiable agent pillar; Close the loop only after tying outputs to input signals; Agent readiness checklist (eight pillars); Per-task model routing for cost versus quality; Single harness and context shared across surfaces; Outcome-based agent metrics
- Tools: Sentry, Slack, AGENTS.md, Factory

## [Grep or Embeddings? Agentic Search Over Company Documents — George He, LlamaIndex](../videos/X4w2Pkz5tDY.md)
`X4w2Pkz5tDY` · AI Engineer · 2026-10-07 · q3 · practitioner · talk · also: rag-retrieval, data-engineering

George He (LlamaIndex) argues that agent document search should be a harness of primitives (list, grep, read by offset, semantic search, page screenshots) chosen by corpus scale, not a single RAG pipeline.

- Techniques: Agent retrieval harness with a small primitive set; Hybrid retrieval with weighted fusion and LLM rerank; Parse once, persist, and store page screenshots; Metadata tagging at ingest; Chunked reads with grep then offset and length; Evaluate parsers on table and layout fidelity
- Tools: LlamaIndex, LlamaParse, LightParse, Turbopuffer, Claude Code, grep, BM25, Textract, Tesseract, MCP, Google Drive, SharePoint

## [Agent Memory Is Solved. Agent Learning Isn't. — Karthik Ranganathan, Yugabyte](../videos/9_oy4owGtPI.md)
`9_oy4owGtPI` · AI Engineer · 2026-10-06 · q3 · practitioner · talk · also: memory, multi-agent, observability

Yugabyte's CEO argues agent memory is solved but cross-agent learning is not, and demos Mako, a private-to-shared context store where humans promote memories and provenance is traceable.

- Techniques: Private-to-shared promotion gate; Provenance on every memory; Scoped data packs with a skill-driven MCP interface; Cross-session resumability via shared memory; One-variable-at-a-time RAG tuning with traces; Trace-based token accounting
- Tools: Mako (Yugabyte agent-native persistence layer), YugabyteDB, Claude Desktop, Claude Design, Codex, ChatGPT, MCP, Postgres

## [Cooking with Codex — Charlie Guo & Gabriel Chua, OpenAI](../videos/FwiS44-xyYw.md)
`FwiS44-xyYw` · AI Engineer · 2026-10-06 · q3 · practitioner · workshop · also: coding-agents, multi-agent, software-factory

OpenAI's hands-on Codex workshop walks through context, computer use, long-running goals, subagents, hooks and automations, then shows the app server for embedding Codex in your own product.

- Techniques: Verifiable goal with milestone files; Milestone-triggered review and goal-audit threads; Side-thread unblock and status query; Subagent vs thread handoff split; Hook-based deterministic guardrails; Heartbeat automation for external waits; Scheduled triage that spawns worktree threads to PRs; Choosing a control surface: computer use vs Chrome extension vs in-app browser; Embedding via the App Server protocol
- Tools: Codex app, Codex CLI, Codex remote (ChatGPT mobile), Codex Chrome extension, Codex computer use, Codex in-app browser, Agents SDK, Sites, Chronicle (research preview, Pro), AppShots (screenshot with embedded text), AGENTS.md, config.toml hooks

## [Lifestyles of the AI-Native — Nick Nisi & Zack Proser, WorkOS](../videos/AgBAOXVxt4A.md)
`AgBAOXVxt4A` · AI Engineer · 2026-10-06 · q3 · practitioner · workshop · also: claude-code, coding-agents, testing-verification

WorkOS engineers run a hands-on workshop on operating fleets of Claude Code agents: voice dictation, goal vs loop, verification hooks, Codex adversarial review, worktrees and scheduled tasks.

- Techniques: Goal with a measurable done condition; Loop for recurring or open-ended monitoring; Checksum-verified evidence of test runs; Hook-enforced gates; Cross-model adversarial review; Retrospective agent with curated memory; State machine for ordered steps; Git worktrees for parallel agents; Interactive first, then schedule; Session fleet management; Triage automated PR review output by score
- Tools: Claude Code, Codex CLI, Handy, WhisperFlow, Granola, Greptile, CodeRabbit, Devin, Linear, Slack, tmux, Fleet (nicknesey/fleet)

## [AI Coding Agents Are Breaking Big Codebases — Dan Adler, Sourcegraph](../videos/Bdrs3uAX0_M.md)
`Bdrs3uAX0_M` · AI Engineer · 2026-10-05 · q3 · practitioner · talk · also: coding-agents, software-factory, rag-retrieval

Sourcegraph CEO Dan Adler argues that large, decades-old codebases are decaying under the flood of AI-written code, and that agents need code-graph and search infrastructure to see and change them across thousands of repos.

- Techniques: Deterministic scripts for mechanical sweep changes; Hybrid agent and script batch change loop; Code-graph plus search as agent context; Coverage audit for sweeping changes
- Tools: Sourcegraph, agentic batch changes, Claude Code, Codex, Cursor

## [We Built an AI Support Agent That Resolves 80% of Tickets — AssemblyAI](../videos/pyvRID_CZZU.md)
`pyvRID_CZZU` · AI Engineer · 2026-10-05 · q3 · practitioner · talk · also: agent-architecture, voice-multimodal, enterprise-adoption

AssemblyAI's FDE team built "Joey," a Claude Agent SDK support agent over local markdown docs, lifting end-to-end ticket resolution from 10% to 80% for about $700/month; the talk also argues for dogfooding your own product.

- Techniques: Docs-as-markdown synced into the agent's workspace; Two-stage retrieval: embeddings first, then agentic file search; Guardrail CLAUDE.md as the behavior-tuning loop; Escalation reason taxonomy as a product backlog; PaaS deploy from a Dockerfile for fast fix cycles; Monitoring through the existing support tool
- Tools: Claude Agent SDK, Claude Code, CLAUDE.md, Railway, Docker, Pylon, Voyage AI embeddings, AssemblyAI voice agent API, Slack, WebSocket

## [Scale the Judgment, Not the Model — Andrew Orobator, Reddit](../videos/6MudaeKdBSk.md)
`6MudaeKdBSk` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · also: skills-self-improvement, testing-verification, software-factory

Reddit's Andrew Orobator on scaling agent judgment rather than model size: encode institutional judgment as skills, work logs, personas and hard gates, verified by recordings, so coding agents can ship with less human review.

- Techniques: Skills as encoded review judgment; Work log plus commit-hook enforcement; Persona prompting for perspective; Recording-based agent QA; Rules-first funnel for LLM cleanup; OS-level gate with operator-only bypass; Three operating modes; Scheduled skill drift audit
- Tools: Codex, git pre-commit and commit hooks, CI, lint, screenshot-based model review

## [No, That's Not a Software Factory — Ryan Cooke, WorkOS](../videos/HvboD89DyQ8.md)
`HvboD89DyQ8` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: software-factory, mcp-and-tools, skills-self-improvement

Ryan Cooke (WorkOS) on why a sandbox plus coding agent is not a software factory. Build around outcome metrics, webhook-driven product workflows, and an internal MCP gateway.

- Techniques: Outcome-based factory metrics; Webhook-driven ticket pipeline; Agent plan refresh after each step; Agent-drafted PRD with human approval gate; Context-rich MCP gateway; Session mining for skill gaps
- Tools: Linear, Slack, GitHub, Notion, Snowflake, Cloudflare sandboxes, Claude Code, Devin, OpenCode, MCP

## [MCP Doesn't Suck. Your Agent Does. — Jan Čurn, Apify](../videos/pAnLpiAG6Es.md)
`pAnLpiAG6Es` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: mcp-and-tools, coding-agents

Apify's CEO argues MCP's problems come from agent harnesses, not the protocol. He covers progressive tool discovery, code mode, and CLIs, then pitches MCPC, a CLI wrapper for MCP.

- Techniques: Progressive tool discovery; Code mode for tool calls; Keep large or sensitive tool output out of context; Wrap MCP in a CLI and give the agent bash; Async tool invocation with detach and poll; Connector evals
- Tools: MCP, MCPC, Claude Code, Claude Tool Search Tool, Cloudflare code mode, Bash, jq, Terminal Bench

## [Stop Fine-Tuning to Fix Retrieval Problems — Anant Srivastava](../videos/qflLT3SoVbw.md)
`qflLT3SoVbw` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: rag-retrieval, training-finetuning-rl, memory

Anant Srivastava argues enterprise teams should decide deliberately whether knowledge lives in the prompt, in retrieval/memory, or in fine-tuned weights, using rate of change, scope, and behavior-vs-facts as the test.

- Techniques: Knowledge placement diagnostic; Retrieval-first debugging; Fine-tune the stable center, keep humans on the edge; Code-aware chunking with denormalized metadata; Promote-and-prune memory loop; Small fine-tuned model for cost

## [Dashboards Are Dead — Sarah Simionescu, Composio](../videos/YiFqcu9YA38.md)
`YiFqcu9YA38` · AI Engineer · 2026-10-04 · q2 · intro · talk · also: mcp-and-tools, product-ux

Composio's Sarah Simionescu argues agents should replace dashboards, and that MCP servers need task-scoped tool discovery to work. Vendor pitch with a mock-up demo.

- Techniques: Task-first tool discovery; Parallel fetch after planning; Keep bulky results out of context; Schema-first exploration before querying; Bug-report prompt to an agent with connected tools
- Tools: Composio (MCP, CLI, native tools, Composio Search, Composio Remote Workbench), Claude, MCP (Model Context Protocol, announced by Anthropic Nov 2024), Datadog, Sentry, Slack, GitHub, Jira (JQL), VS Code, PostHog, Metabase, SQL

## [How VS Code Went from Monthly to Weekly Releases with AI — Harald Kirschner](../videos/I2LL_wd89-A.md)
`I2LL_wd89-A` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · also: software-factory, pr-code-review, testing-verification

How the VS Code team moved from monthly to weekly releases by rebuilding its own dev system around agents: code-survival metrics, agent-readable repos, fast CI, UI feedback loops, AI triage, and staged rollouts.

- Techniques: Code survival metric; Agent-readable repo docs; Expert knowledge as a shared skill with an area owner; Screenshot-diff component browser; Self-correcting launch loop; Tiered AI code review; Deterministic filtering before agent action; Staged rollouts with error monitoring; Evals bootstrapped from issues; Prototypes instead of PRs for design talks
- Tools: VS Code, GitHub, GitHub Issues, GitHub Copilot code review, TypeScript Go, Playwright, Electron, Xcode MCP, AGENTS.md, Chrome extension

## [What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory](../videos/vGCJ7diEtrw.md)
`vGCJ7diEtrw` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · also: software-factory, infra-cost-scaling, testing-verification

Factory's engineer defines a "software factory" as a full autonomous lifecycle, not coding agents. Covers model routing for cost, verifiable done-criteria, sequential worker and validator missions, deferred tool loading, and codebase readiness.

- Techniques: Difficulty-classified model routing; Validation contract written before coding; Sequential workers with fresh context per handoff; Two-tier validation; Deferred tool loading; Codebase readiness audit; Codify tacit rules as skills or plugins
- Tools: Factory (software factory platform), Factory missions (orchestrator, worker and validator agents), Automatic model routing, Deferred context engine, Agent readiness framework, Plugins, Auto-wiki, Slack, GitHub, Figma, Notion, Gmail

## [Github Top Trending Tool Just Fixed The AI Agent’s Biggest Problem](../videos/cyIWQHYoUg8.md)
`cyIWQHYoUg8` · AI LABS · 2026-10-02 · q3 · practitioner · review · also: token-cost-efficiency, coding-agents, rag-retrieval

Walkthrough of Graft, a free open-source CLI that builds a code knowledge graph and hooks into Claude Code to cut search turns, tokens and cost; the benchmark is self-reported by its makers.

- Techniques: Code knowledge graph for impact-aware retrieval; Pre-prompt context injection via a UserPromptSubmit hook; Hook trio for a Claude Code workflow; Pick CLI injection or MCP on-demand lookup; Long autonomous run setup for a token-hungry model; Install and initialize Graft in a Claude Code project
- Tools: Graft, Claude Code, Codex, MCP, Opus, GPT 5.6, GPT Astra (as transcribed, unverified), Fable 5.1 (as transcribed), Hydra (sponsor; API for AI generation)

## [This Open-Source Tool Makes Claude Create Architecture Diagrams](../videos/iuJszJuiuSg.md)
`iuJszJuiuSg` · Better Stack · 2026-10-02 · q3 · practitioner · tutorial · also: coding-agents, dev-tools

Better Stack walkthrough of Archify, an open-source agent skill where the coding agent emits validated typed JSON that a local compiler renders into HTML architecture diagrams; useful for PR and design-review artifacts, not for READMEs or mapping huge repos.

- Techniques: Schema-validated diagram IR; Evidence-gated nodes; Narrow architecture question prompt; Diff two architecture snapshots; Install as an agent skill
- Tools: Archify, Claude Code, Cursor, Codex, Mermaid, GitHub

## [Agent Harness explained in 8min.. Why its more Important then AI Agent](../videos/qXo1P5H2RXk.md)
`qXo1P5H2RXk` · Kai Explains · 2026-10-02 · q3 · intro · talk · also: agent-architecture, claude-code, token-cost-efficiency

Explainer building an agent harness from scratch (agent loop, context management, permission gate, config) and arguing that the harness, not the model, now drives much of a coding agent's score and cost.

- Techniques: Minimal agent loop; Externalize state and use clean-context sub-agents; Harness-owned permission gate; One git work tree per agent; Move repeated instructions into configuration; Audit tool-description overhead; Compare harnesses by trips per task, not only by score
- Tools: Claude Code (Anthropic), Codex (OpenAI), Cursor, Cline (auto-caption reads 'Klein'; the open-source repo is discussed), Anthropic model card (benchmark scaffold footnote), git work trees, NVIDIA H200 (hardware, mentioned as a comparison, not used)

## [Your AI Subscription Is Now Worth Less](../videos/FWShtLCP4OY.md)
`FWShtLCP4OY` · Kai Explains · 2026-10-02 · q3 · practitioner · other · also: token-cost-efficiency, claude-code, governance-compliance

Why Claude's Max-plan limits feel smaller: unpublished capacity fractions, per-turn overhead from CLAUDE.md and MCP servers re-billed every turn, and default high reasoning effort. Practical fixes included.

- Techniques: Read the floor before a session; Prune idle MCP servers; Set reasoning effort per task instead of leaving it on high; Ask for markdown when fetching docs; Write specific prompts with form and constraints; Measure what an hour of your work costs
- Tools: Claude Code, Claude Pro, Claude Max 5x, Claude Max 20x, CLAUDE.md, MCP servers, Extended thinking (reasoning effort setting), Limit Reset command, Low Priority Mode, OpenAI Codex, GitHub Copilot

## [Insane Jev Use Cases You Need To Use Right Now](../videos/2nc_QMuNp18.md)
`2nc_QMuNp18` · AI LABS · 2026-10-02 · q2 · practitioner · review · also: claude-code, token-cost-efficiency, pr-code-review

AI LABS shows seven Claude Code workflow hooks that offload yes/no, ranking and routing decisions to "Jev", a decision-only model with a confidence value, to cut latency and token spend.

- Techniques: Decision-model offload via gateway; Compaction replacement via project-local hook; Doc-rule to test coverage hook; Per-prompt skill picker hook; Keyword search then batched LLM rerank for Explore; Seven yes/no review gate; Browser agent with model-picked clicks; Pre-edit rule enforcement hook
- Tools: Jev (TypeSafe decision model, as auto-captioned), Vercel AI Gateway, OpenRouter, Claude Code, Codex, Fast Jev Compaction plugin, Claude Code Explore subagent, Opus (caption reads 'Opus 2'), Zapier (sponsor segment)

## [You Are Using Fable 5.1 Wrong (Do This Instead)](../videos/7au4tWVG8a0.md)
`7au4tWVG8a0` · AI LABS · 2026-10-02 · q3 · practitioner · review · also: claude-code, token-cost-efficiency

Practical tips for getting better results and lower cost from Anthropic's Fable 5.1 in Claude Code: lower effort, prune old-model instructions, scope edits, and give whole-feature prompts. Mostly anecdotal.

- Techniques: Start at low effort and escalate only on evidence; Ablation test to prune CLAUDE.md; Unattended-run preamble; Explicit scope fence; Minimal-diff editing instruction; Remove mannered prose; Whole-feature prompts instead of step-by-step prompts
- Tools: Claude Code, Fable 5.1, Fable 5, Opus 5, CLAUDE.md, Claude API prompt audit (command name as spoken; exact invocation not shown), Artificial Analysis (independent model benchmarking), Porkbun (sponsor, domain registrar)

## [This New Open Source Tool Just Fixed Your Claude Code Workflow](../videos/CHHEjuNBxoQ.md)
`CHHEjuNBxoQ` · AI LABS · 2026-10-02 · q3 · practitioner · review · also: coding-agents, memory, security-guardrails

Walkthrough of Agit, an open-source tool that applies git's model (repos, sessions as branches, turns as commits) to agent conversations, with sharing, revert, cross-agent fork and secret redaction.

- Techniques: Versioned agent sessions via a git-style repo; Reverting a session to an earlier turn; Cherry-picking messages between sessions; Forking a Claude Code session into Codex; Registering known passwords before a session is saved
- Tools: Agit, createagit (installer), npm, GitHub, Claude Code, Codex, AGENTS.md, CLAUDE.md, Runnable (sponsor)

## [How To Use Claude Code To Build Amazing Sites With Opus 5.5](../videos/DP7mgLUKN_U.md)
`DP7mgLUKN_U` · AI LABS · 2026-10-02 · q3 · intro · tutorial · also: vibe-coding-app-building, claude-code, pr-code-review

Six-stage tutorial for building non-generic websites with Claude Code: plan mode, CLAUDE.md business context, a design-rules skill, design.md, git/GitHub/Vercel deployment, branch + PR review, and a 3D scroll skill.

- Techniques: Plan mode before building; Enrich CLAUDE.md with business context; Install and apply a design-rules skill to an existing project; Lock visual style with design.md; Commit checkpoints and set up GitHub via the CLI; Deploy from GitHub to Vercel; Feature branch, PR, and automated review loop; Scroll-driven 3D site via ScrollWorld skill
- Tools: Claude Code, Opus 5.5, Sonnet, Fable, Warp, VS Code, Next.js, Vercel, Vercel CLI, GitHub, GitHub CLI (gh), CodeRabbit

## [Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA](../videos/OA-Mc60Rboo.md)
`OA-Mc60Rboo` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: skills-self-improvement, evals, training-finetuning-rl

GEPA's Lakshya Agrawal explains reflective, text-space optimization: LLMs read full rollout traces and rewrite prompts, skills or harness code, with a Pareto pool, beating GRPO on sample efficiency.

- Techniques: Reflective prompt / artifact optimization loop; Pareto candidate pool selection; Actionable side information from the evaluator; Three optimization modes in one API; Optimize the agent file itself; Repo skill learning from trajectories; Judge-then-agent data flywheel
- Tools: GEPA (open-source, includes the optimize_anything API and a skill-learning feature), GRPO (used as the RL baseline), Claude Opus, Claude Sonnet 4.5, GPT-5 mini, GPT-4.1, GPT-4.1 nano, Gemini Flash, mini-SWE-agent, Claude Code, Codex, LLM-as-judge

## [The Dark Arts of Skill Engineering — Paul Bakaus, Renaissance Geek (Impeccable)](../videos/SQMCtZX3trg.md)
`SQMCtZX3trg` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: skills-self-improvement, coding-agents, evals

Paul Bakaus (Impeccable) on building production agent skills as harness extensions: blind sub-agents, forced divergence, scripts, hooks and per-model builds, rather than prose alone.

- Techniques: Blind adversarial critique; Anti-attractor divergence; Register routing inside one skill; Cross-session skill memory; Scripts that print next-step instructions; Pre-tool-use blocking hooks for weaker models; Hook-driven feedback loop from a skill; Unskippable gates with logged results; Per-harness and per-model builds; Ablation testing of rules; LLM-as-user with a judge panel; Inverted judges
- Tools: Claude Code, Codex, Cursor, GitHub Copilot, Gemini, Playwright, skills.sh, npx skills

## [Fixing the PR Bottleneck — Matt Pocock, AIHero](../videos/LlgiOCmFG_w.md)
`LlgiOCmFG_w` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: pr-code-review, software-factory, testing-verification

Matt Pocock on clearing the PR backlog that AI agents create: layer cheap deterministic checks, have an agent review and commit fixes, design deep modules so tests stop being brittle, and run a retro on each session.

- Techniques: Layered brakes for agent PRs; Deep-module design for agent-testable code; Separate implementer and reviewer contexts; Reviewer commits fixes, comments only on open questions; Door-type and blast-radius PR summary; Pseudocode and diagram PR explanations; Retro over sessions and PRs
- Tools: AGENTS.md, coding-standards.md, CodeRabbit, Cursor BugBot, PlanetScale, Opus 5 (model mentioned in the tautological-test example), AIHero skills (version 1.3 announced for the same week)

## [You’re Not Thinking Big Enough: Rebuilding Food Systems with AI Agents — Cody Menefee, Firecrawl](../videos/ztlXKfPCT3Q.md)
`ztlXKfPCT3Q` · AI Engineer · 2026-09-27 · q2 · intro · talk · also: data-engineering

Firecrawl growth engineer Cody Menefee argues LLM agents could help automate rotational grazing for livestock, with the LLM suggesting moves and a human confirming, plus a recruiting pitch for Firecrawl.

- Techniques: Human-confirmed LLM suggestions over multivariate data; Knowledge base from scattered web sources; Context gathering and packaging for LLM reasoning; Fixed reference object for remote measurement; Model the decision at several levels
- Tools: Firecrawl, OpenPasture, Halter, NoFence, Planet satellite imagery, trail camera

## [Building the Document Context Layer for AI Agents — Jerry Liu, LlamaIndex](../videos/RQi7x-navxU.md)
`RQi7x-navxU` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: rag-retrieval, data-engineering

Jerry Liu (LlamaIndex) argues agents need a document context layer: fast local parsing by default, VLM escalation for hard pages, and cost-aware routing between specialized and frontier models.

- Techniques: Fast-pass then escalate parsing; Hybrid pipeline plus VLM parsing with routing; Regime-based pipeline selection; Structured extraction with provenance and confidence gating; Multi-tool agent retrieval over documents; Accuracy-cost-latency Pareto benchmarking
- Tools: LlamaParse, LightParse, ParseBench, Claude Code, Claude Cowork, Codex, OpenClaw, MCP, BM25, grep, PyPDF, PyMuPDF

## [Total Recall: Agent Memory and Harness Engineering — Ignacio Martinez, Oracle](../videos/xs-ob87TTzg.md)
`xs-ob87TTzg` · AI Engineer · 2026-09-20 · q3 · practitioner · workshop · also: memory, agent-architecture, skills-self-improvement

Oracle workshop on agent harness design: a 30-minute framework for agent memory (files vs databases, memory types, context rot, skill promotion), then a hands-on notebook build, with heavy Oracle product promotion.

- Techniques: Hybrid storage split; Per-agent git worktrees for file edits; Context card; Toolbox / skillbox index with vector retrieval; LLM-enhanced tool descriptions; Patience (hysteresis) budget for agent loops; Skill promotion by distillation; Difficulty-based model routing
- Tools: Oracle Database (converged: JSON, relational, spatial, graph, vector), Oracle DBFS, Oracle Agent Memory Package (OAMP), LangChain Oracle DB integration, OCI Generative AI service, GitHub Codespaces, Grok 4.1 Fast Reasoning, HNSW vector indexes, git worktrees, Python 3.12 notebook

## [If we want them to do Knowledge Work, design them as Knowledge Agents — Benjamin Clavié, Mixedbread](../videos/O84lhGc1OOI.md)
`O84lhGc1OOI` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: rag-retrieval, multi-agent, evals

Benjamin Clavié (Mixedbread) argues agents should be designed as knowledge workers, not coding agents, and uses BrowseComp-Plus and MatQA results to show that tooling and search orchestration drive accuracy.

- Techniques: Manager-plus-searcher subagents for open-ended retrieval; Optimize the lexical baseline before comparing; Hybrid search harness; Multimodal PDF search instead of OCR text; Teach the agent its retrieval primitives
- Tools: BM25, Gemini, Claude Code, Codex, Mixedbread search tool

## [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../videos/qdAkxLoYNI8.md)
`qdAkxLoYNI8` · AI Engineer · 2026-09-18 · q2 · intro · review · also: rag-retrieval, pr-code-review, mcp-and-tools

Unblocked vendor talk arguing coding agents need an organizational context engine over code, PRs, Slack and docs, with cited sources; one live comparison, mostly product pitch.

- Techniques: Cited-source answers for agents; With/without context comparison; Expertise-weighted review comments; Query historical PR data with an open-source engine; Engineering social graph from review edges
- Tools: Unblocked, Claude Code, Claude 4.8, Slack, Notion, GitHub, MCP, Document Query Engine, context engine simulator

## [How We Solved Agent Building — Andrew Qu, Vercel](../videos/9dYcwOkpCE8.md)
`9dYcwOkpCE8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: agent-architecture, skills-self-improvement, multi-agent

Vercel's chief of software traces an internal data-science agent from a mega-prompt, to a multi-agent chain, to one file-system agent with distilled skills, then introduces the Eve agent framework.

- Techniques: Decompose-then-collapse; File-system agent with minimal tools; Query-to-skill distillation job; Convention-based agent folders; Built-in run observability
- Tools: Vercel AI SDK, Eve, Vercel Workflows, Vercel Sandbox, Vercel Connect, bash-tool (npm), SkillsSH, Claude Code, Claude Opus 4.5, Snowflake, Next.js, Postgres

## [What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../videos/0I6aoPSRzVc.md)
`0I6aoPSRzVc` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: multi-agent, memory, enterprise-adoption

AIDAChip's VP of AIML argues chip-design teams are limited by alignment, not intelligence, and shows a "system of intent" living graph, tribal-knowledge layer and SME agents, plus failure lessons on substrate-level controls.

- Techniques: Living system-of-intent graph with human-gated edits; Rule-based conflict detection instead of LLM-based; Scoped spec hierarchy with file isolation per agent; Block forbidden actions at the system level, not per tool; Alignment-focused evaluation grid; Domain-specific SME agents instead of one general agent

## [500 Skills, Zero Fine-Tuning: LinkedIn's Playbook for AI Agents — Ajay Prakash, LinkedIn](../videos/9wZpvF3QleU.md)
`9wZpvF3QleU` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: skills-self-improvement, mcp-and-tools, coding-agents

LinkedIn's Ajay Prakash on an internal MCP server that serves tools plus self-contained markdown "playbooks" teaching coding agents company workflows, kept current by a PR-based self-update loop.

- Techniques: Playbooks as MCP-served instruction docs; Compose playbooks by reference; Session-end playbook self-update PR; Three meta tools for large tool catalogues; Central plus repo-local instruction split; Single pre-installed local MCP server with hourly auto-update
- Tools: MCP, Claude Code, GitHub Copilot, Cursor, Airflow, Jira, Slack

## [Building Agents Is Trivial Now, Context Is the Next Frontier — Jeff Ng, Unblocked](../videos/HvMyYLTfvhg.md)
`HvMyYLTfvhg` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: memory, agent-architecture, mcp-and-tools

Jeff Ng (Unblocked) argues agent infrastructure is now easy to assemble, so the real gap is organizational context. He demos a context engine that feeds agents synthesized, permission-scoped knowledge instead of raw MCP results.

- Techniques: Durable per-step checkpoints for agent runs; Isolated sandboxes for agent and third-party code; Context engine queried before the agent reasons; Synthesized context over raw tool results
- Tools: Cloudflare, Vercel, Mastra, Flu (transcript spelling of the framework), Linear, Slack, GitHub MCP, Claude Code, Codex, Unblocked context engine

## [Tolan: Voice-First AI Companion — Paula Dozsa, Tolan](../videos/xLUQOqjudtA.md)
`xLUQOqjudtA` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: voice-multimodal, memory, software-factory

Tolan's engineers explain how a voice-first AI companion needs sub-two-second turns, stakes-based model routing, retrieval-style memory, and per-turn context rebuilding, plus how they use Claude agent fleets to ship iOS code.

- Techniques: Smart turn-taking from speech patterns; Per-stage latency instrumentation; Stakes-based model tiering with a cheap per-turn router; Retrieval-based memory with nightly consolidation; Stable-versus-volatile memory blocks; Character identity held separately from tone; Multi-judge eval loop for persona changes; Agent fleet with reviewer and PR-shepherd roles
- Tools: Claude, GPT-5.1, OpenAI Responses API, MCP, Linear, Sentry, Datadog, App Store

## [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../videos/Qw_tC68KKes.md)
`Qw_tC68KKes` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: skills-self-improvement, enterprise-adoption, multi-agent

Cloudflare's Justin Joyce on scaling go-to-market analysis with curated skill files, a three-agent report pipeline and a self-service agent workspace; a practitioner account with few hard metrics.

- Techniques: Role-specific skill files with embedded question catalogue; Pre-shaped analytical data for agents; Draft, verify, then tone multi-agent report pipeline; Push generated narratives instead of dashboards; Reviewed central skill catalogue; Per-user persistent agent workspace
- Tools: Cloudflare Workers, Cloudflare Durable Objects, MCP, AI Gateway, Salesforce, Gemini (mentioned as a phone analogy)

## [Agents' next frontier: agent-to-agent and network effects — Jean-Denis Greze, Town](../videos/REascnFlq_8.md)
`REascnFlq_8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: multi-agent, security-guardrails, rag-retrieval

Jean-Denis Greze (Town CTO) reframes agent-to-agent work as a context-window search problem and compares five ways to get cross-silo data into an LLM call safely.

- Techniques: Benchmark against an ideal single-context agent; Privacy-preserving derived tool; Per-silo sweeper agent; Write-step-only approval for cross-silo queries; Tiered autonomy by sensitivity
- Tools: Gmail, Slack, Airtable, LinkedIn

## [The Era of Compound Engineering — Kieran Klaassen, Every/Cora](../videos/_ehJyfHg1Vk.md)
`_ehJyfHg1Vk` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: skills-self-improvement, claude-code, software-factory

Kieran Klaassen (Every/Cora) on compound engineering: extract your judgment and repeated corrections into repo knowledge so each feature makes the next one easier, with a demo of his open-source plugin's commands.

- Techniques: Compound engineering loop; Ideation against strategy docs; Doc review for sharp questions; Brainstorm with minimal questions; Unattended end-to-end run (/lfg); PR polish with explanation; Extract a design rule from a review fix
- Tools: Claude Code, Codex, Cursor, Claude Cowork, Linear, GitHub, Slack, Intercom, Rails, React, MCP

## [Why AI Agents Need Million-Token Context — Thomas Wolf & Olive Song, MiniMax](../videos/5Cxe5dv2Xlw.md)
`5Cxe5dv2Xlw` · AI Engineer · 2026-09-18 · q3 · practitioner · interview · also: models-research, inference-serving

MiniMax's Olive Song and Hugging Face's Thomas Wolf on how M3 reaches 1M-token context with sparse attention and native multimodal pretraining, and why agents need that context for multi-round tool use.

- Techniques: Index-then-sparse attention over context blocks; Train vision from the first pretraining step with interleaved data; Open project intake for research; Research harness for automating model-lab workflows
- Tools: MiniMax Sparse Attention (MSA), Hugging Face model card

## [One Designer + AI. Hundreds of Deliverables. — Vincent Wendy, AI Engineer](../videos/O1FN4awNEtM.md)
`O1FN4awNEtM` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: product-ux, testing-verification

A solo designer at AI Engineer uses agents (Devin, GPT, Figma) to produce hundreds of conference deliverables by fixing design tokens first, automating data-driven outputs, and checking results with an agent.

- Techniques: Tokens-first design system for agents; Annotated spec sheet as handoff; Single data source to many assets; Agent as checklist QA on visual output; Vision-based photo matching; Raster first, then vectorize
- Tools: Devin, GPT, Figma, MCP, Slack, PNG export, Figma spec-sheet plugin

## [It’s Tokens All The Way Down: How RLMs are Different — Kevin Madura, AlixPartners](../videos/xo68uCibfm8.md)
`xo68uCibfm8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: agent-architecture, multi-agent, data-engineering

Kevin Madura (AlixPartners) explains recursive language models (RLMs): the context lives as a variable in a Python REPL, and the model writes code and delegates subcalls to sub-LMs, so only useful results return to the main context.

- Techniques: REPL-held context with sub-LM delegation; Typed I/O shell around an autonomous core; Schema-enforced sub-LM handoff; Bounded self-terminating loop; Dataframes in the REPL instead of JSON tool results; Trace-driven harness optimization (Halo)
- Tools: DSPy, PredictRLM, fastRLM, AXE, Halo, Claude Code, GPT-5, Anthropic Workflows, pandas

## [Your Fine-Tuned Model Is Tech Debt: A 50x ROI House of Cards — Dan Bjornn, Lease End](../videos/4loPnxvWWhg.md)
`4loPnxvWWhg` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: training-finetuning-rl, evals, enterprise-adoption

A LeaseEnd data scientist explains how fine-tuning an intent classifier for customer texts became costly tech debt, and how replacing it with editable skills and prompts on a frontier model cut fix time from a week to under an hour.

- Techniques: Skill and prompt edits as the default fix; Curated production regression set as the gate; Markdown-file deploys to object storage; Triage gate before retraining; Fine-tuning pre-check list; LLM-judge labeling with manual review and holdout sets
- Tools: Claude Code, Amazon S3, OpenAI, Anthropic

## [Loophole: Adversarial Agents To Stress Test Your Morality — Brendan Rappazzo, Morgan Stanley](../videos/hOWU0KPUp1k.md)
`hOWU0KPUp1k` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: evals, governance-compliance, multi-agent

Brendan Rappazzo presents Loophole, an open-source game where two adversarial agents hunt contradictions in a legal code codified from the user's morals, then extends it to chatbot prompts, contracts, and simulated Senate votes.

- Techniques: Adversarial loophole and overreach search; Judge with auto-patch first, human escalation second; Formalize natural-language values into numbered legal text first; Persona-conditioned rule generation for simulation; Hill-climbing text against an adversarial judge
- Tools: Claude, GitHub

## [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../videos/5Bn0xro2ol8.md)
`5Bn0xro2ol8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, testing-verification, coding-agents

Figma engineer on rolling out coding agents across an org: verification-first testing, plan-before-prompt with phase validation gates, and labeling AI-written text so reviewer attention is spent well.

- Techniques: Verification-first agent workflows; Encode agent discoveries as deterministic tests or flows; Testing pyramid for agent-written code; Red-green prompting; Why-first phased plan with validation gates; Human-first labeled communication; Agent-in-thread invitation
- Tools: Playwright MCP, Slack, cloud coding agent (unnamed)

## [MCP Apps: Give the Model Data, Give the User a UI — Dustin Mihalik, Indeed](../videos/lbaXnx0KLA8.md)
`lbaXnx0KLA8` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: mcp-and-tools, product-ux

Dustin Mihalik (Indeed) shares lessons from building MCP Apps for Claude and ChatGPT: model-visible data parity, separate data from rendering, and feeding UI interactions back to the model.

- Techniques: Model-visible data parity; Description steering of UI vs text output; Explore/render split; Interaction feedback via update model context; Render tools that take model-generated rationale; Small composable tool set
- Tools: MCP Apps, Apps SDK (OpenAI), update-model-context method, Claude, ChatGPT, CareerScout (Indeed internal agent)

## [Building ambitious software — Jonathan Kelley, Dioxus Labs & Cognition](../videos/H7vFrcNWXzs.md)
`H7vFrcNWXzs` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: coding-agents, testing-verification

Dioxus Labs (now part of Cognition) on building an ambitious Rust framework with coding agents: fast on knowledge work and mundane upkeep, weak at tests, and architecture plus review now carry the load.

- Techniques: Let the compiler's strictness act as the agent's guardrail; Agents as a knowledge oracle for platform and spec behavior; Delegate checklist-style maintenance to agents; Agent-built fuzzing harnesses; Human-enumerated test conditions with agent brainstorming; Architecture-first, then implementation, with full PR reading
- Tools: Claude Code, Rust, Dioxus, Blitz, SubSecond, Firefox (CSS engine), Electron, React Native, Flutter, Kotlin, Swift, Zed

## [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](../videos/V_5bn4q-vAI.md)
`V_5bn4q-vAI` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: mcp-and-tools, product-ux, coding-agents

Christopher Burns (Inth) on making LLMs recommend and correctly use his open-source cookie-banner library by shipping agent-friendly docs: hand-written llms.txt, markdown twins, web MCP, and grep-able docs inside node_modules.

- Techniques: Hand-curated llms.txt index; Markdown twin per page with discovery header; Three ways to reach markdown; Bundle docs in the package with an agents.md pointer; Web MCP for docs; Agent-readiness checks as a loop
- Tools: LeadType, llms.txt, llms-full.txt, AGENTS.md, Next.js, Aura AI, Cloudflare agent-readiness checker, MCP

## [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../videos/M05vON8i0aI.md)
`M05vON8i0aI` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: skills-self-improvement, enterprise-adoption, governance-compliance

Imad Touil (QuantumBlack) argues org know-how should live in governed agent skills: a central registry with owners, versions, access control and evals. Ungoverned skills bring duplication, quality decay, security risk and wasted tokens.

- Techniques: Skill catalog with metadata and an MCP search front end; Microservice-style skill design; Progressive disclosure of skills; Runtime composition of regulatory skills into a review workflow; Static skill tests before any evaluation; Individual-to-team-to-platform promotion path
- Tools: Claude Code, Cursor, MCP, Backstage (IDP), GitHub

## [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../videos/pqlWNihgdjI.md)
`pqlWNihgdjI` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: enterprise-adoption, coding-agents, testing-verification

Amazon's frontier-dev habits from AWS's Clare Liguori: teams that changed how they worked (context files, self-validating agents, spec-first, local tests) hit a 4.5x median in deployment velocity; tool-only teams got under 3x.

- Techniques: Living steering/skills file with a rule per agent mistake; Self-validating agent loop; Spec-first iteration; Local deterministic mock services; Agent-friendly language and error design; Deployment velocity as the productivity metric; Decision-speed audit
- Tools: Kiro, MCP servers, Bedrock, TypeScript, Rust

## [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](../videos/yqF6XhzbWBk.md)
`yqF6XhzbWBk` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: evals, enterprise-adoption

Sebastian Fox (Composo) on why LLM judges miss serious clinical-note errors: "which error matters" is tacit and shifting, so keep it as retrieved, case-specific expert judgments and run a discover-capture-calibrate loop.

- Techniques: Failure-mode discovery from production outputs; Free-text expert comments as the raw eval data; Retrieval of similar judged cases into the judge context; Generate-then-check with a narrower checker; Severity vs. detectability map of errors
- Tools: ambient AI scribes (product category discussed), LLM-as-judge with rubric, RLHF (conceptual reference)

## [How long can your skills be before your agent forgets what you told it? — Laurie Voss, Arize AI](../videos/XzJD1bvXKjs.md)
`XzJD1bvXKjs` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: evals, skills-self-improvement, models-research

Laurie Voss re-runs the 200-instruction IFScale benchmark on 2026 frontier models and finds the ceiling moved about 10x, to roughly 2,000 to 5,000 rules, but reliability and verification remain open problems.

- Techniques: Instruction density probe; Model-specific failure profiling; Pre-screening test vocabulary for safety filters; Per-output eval of long rule sets; Robustness check by rewording and reordering
- Tools: IFScale benchmark, Arize AI (speaker's employer; no product detail given), Chroma context rot study, Firebench, CCRbench, Guidebench (names as captioned; may be misspelled)

## [Agents Are Where Microservices Were in 2015 — Roberto Milev & Uday Kanagala, Navan](../videos/32nrHU6zHU8.md)
`32nrHU6zHU8` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: agent-architecture, observability, evals

Navan's chief architect and a colleague argue agent infrastructure is repeating the microservices shift: skills as context units, hook-based tracing, trajectory evals, and tool-call guardrails.

- Techniques: Pre/post tool-call and session hooks for tracing and gating; Trace signals: goal, reasons, belief, tool calls, confidence; Trajectory evaluation; Skills as composable, testable context units; Single master agent with progressively loaded sub-skills; Per-tool-call authorization for on-behalf-of agents; A2A skill contracts across team boundaries
- Tools: AWS AgentCore, OpenTelemetry, Claude Code hooks, MCP, A2A protocol, Braintrust (inferred from auto-caption 'brain trusts')

## [The Last Human Code Review: Building Trust in AI-Generated Code — Itamar Friedman, Qodo](../videos/s-aixZYJG4c.md)
`s-aixZYJG4c` · AI Engineer · 2026-09-18 · q2 · practitioner · talk · also: pr-code-review, governance-compliance, enterprise-adoption

Qodo's CEO argues human code review will become optional only once teams codify tribal knowledge into a context engine that serves both humans and agents, with per-rule analytics and graduated auto-approve/block.

- Techniques: Rule-linked review comments; Agent-directed PR summary comments; Per-rule analytics for review standards; Learning context from accept/reject history; Graduated auto-approve and auto-block; Service-contract graph for PR impact
- Tools: Qodo, Claude Code, AGENTS.md, CLAUDE.md

## [The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu](../videos/VBCDhRrvlYo.md)
`VBCDhRrvlYo` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: vibe-coding-app-building, agent-architecture, product-ux

Arturo Nunez (ex-Unity, MongoDB) pitches Nereu, a tag-driven, describe-it-to-build game engine where an AI assistant (Bibi) edits scenes via an Asset Tag System, so creators never touch engine vocabulary or code.

- Techniques: Entity tags as an intent layer over ECS; LLM-as-editor with a tool-only interface; Level-of-detail context assembly; Vision-model asset captioning; Domain expert in the loop while building with a coding agent
- Tools: Claude Code, Unity, Unreal, vision model

## [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../videos/ZIYYsAzaLlA.md)
`ZIYYsAzaLlA` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: mcp-and-tools, evals

Figma's engineer on building its first MCP server in about three months: which context format worked, how evals were automated, and how a remote server followed a local one.

- Techniques: Pick the representation the model knows best; Code plus screenshot as paired context; Reference-by-pointer via a component mapping; Two-step ask-then-act to emulate elicitation and sampling; Automated eval mixing deterministic checks and LLM judges; Local-first MCP server with an IPC bridge; Per-tool-call instructions when clients ignore server instructions
- Tools: Figma MCP server, Figma Code Connect, MCP Inspector, React, Tailwind CSS, Electron, Node.js, Cursor, VS Code, Claude Desktop

## [Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl](../videos/zCJtYuqwm7E.md)
`zCJtYuqwm7E` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, software-factory

Patrick Debois (Tessl) argues that scaling coding agents is an organizational problem: teams must shift effort from fixing agent output to improving shared context, harnesses, and platform-owned reusable parts.

- Techniques: Convert skeptic critique into context and harness work; System-level retro; Split planning by agent readiness; Platform-owned reusable registry with a named owner; Per-team cost and iteration dashboards; Three-step AI-friendly hiring loop; Risk-tiered autonomy
- Tools: Claude Code

## [Pinecone 2.0 — Edo Liberty, Pinecone](../videos/IN-rb-9WmiY.md)
`IN-rb-9WmiY` · AI Engineer · 2026-09-18 · q2 · practitioner · talk · also: memory, rag-retrieval

Pinecone's Edo Liberty argues agents need a persistent, domain-owned company knowledge layer (Nexus) that goes beyond RAG, with query-time code generation and budgeted queries. Mostly a product pitch with vendor-reported numbers.

- Techniques: Manifest-declared knowledge base; Curate-on-ingest; Budgeted agent queries; Query-time code generation over a knowledge layer; Compact interface spec in place of tool sprawl
- Tools: Pinecone Nexus, vector database, SQL tables, graph database, markdown notes

## [Multimodal Collaborative Agents for Next-Gen Commerce — Nidhi Kaushik Vyas, Google DeepMind](../videos/AhQpRalYlyg.md)
`AhQpRalYlyg` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: product-ux, evals

Google DeepMind product lead on shopping agents for fuzzy intent: build a working state, ask the highest-value clarifying question, elicit preferences visually, adapt the answer format, and grade every step with autoraters.

- Techniques: Working state with confidence and live refresh; Counterfactual sensitivity test for constraint extraction; Information-gain question selection; Elicitation-channel choice by preference type; Per-step autoraters with user simulator; Response format chosen by query intent
- Tools: MCP (expected interface between agents and merchants), UCP (merchant common-language protocol, named in the talk without detail)

## [Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](../videos/lRa9sPaMyy4.md)
`lRa9sPaMyy4` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: testing-verification, coding-agents

Varun Pant (AWS) argues that formal verification in Lean, Verus and similar tools can prove code correct for all inputs, which tests and LLM judges cannot, and that humans should own the specification while agents write code and proofs.

- Techniques: Spec-first verified agent coding; Spec model plus differential random testing; Lemma decomposition for AI proofs; In-code pre- and post-conditions checked by a solver; Intermediate-representation dialect to many backends
- Tools: Lean, Lean 4 browser playground, Kiro (transcript shows 'Kero', likely the AWS agentic IDE), Verus, Z3, Aeneas, Strata / Strata Core, Cedar, SMT solvers, model checkers, ArenaLang (kernel registry)

## [Where RL Will Take Search — Maximilian-David Rumpf, SID.ai](../videos/iJVxxxHM_Oc.md)
`iJVxxxHM_Oc` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: rag-retrieval, training-finetuning-rl, multi-agent

Founder of SID.ai argues search should move from fixed retrieval pipelines to one RL-trained model, reporting about 20x faster and 100x cheaper than frontier-model search agents.

- Techniques: Search as a delegated RL-trained sub-agent; Verifiable retrieval reward for RL; Mixed reward with latency; Learned loop in place of a fixed pipeline; Parallel sub-agent searches
- Tools: BM25, PageRank, vector search, rerankers

## [The Missing Layer: Design Taste in AI Agents — Hassan El Mghari, Together AI](../videos/7GMKdpLsxwU.md)
`7GMKdpLsxwU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: vibe-coding-app-building, product-ux, coding-agents

Hassan El Mghari (Together AI) on getting AI-built UIs out of "AI slop": codify the tells as anti-patterns, feed in references, iterate with a cheaper model.

- Techniques: Slop-gate anti-pattern list in a design skill; Theme library as inspiration; Screenshot inspiration vault; Two-tier model routing for UI work; agents.md as a taste log; Batched feature prompting
- Tools: Codex, Claude Code, Cursor, Hallmark, agents.md, GLM 5.2, Opus 4.8, Composer 2.5, Together AI

## [Agent Frameworks Considered Harmful — Rémi Louf, .txt](../videos/KHudyx5wW3U.md)
`KHudyx5wW3U` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: agent-architecture, observability

Rémi Louf (CEO of .text) on building a small event-driven agent runtime in two weeks: typed events, an append-only log, and content-addressed prompts for auditable, replayable agents.

- Techniques: Markdown-defined agents in a versioned folder; Event-typed agent contracts; Append-only event log with causal ids; Content-addressed prompt assembly; Replay a stored request against another model; Two-boundary enforcement
- Tools: Codex, Slack, Linear, llama.cpp

## [Your agents lack context: Here's how to fix "You're absolutely right!" — Brandon Waselnuk, Unblocked](../videos/KcVkq5L-0f0.md)
`KcVkq5L-0f0` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: rag-retrieval, mcp-and-tools

Brandon Waselnuk (Unblocked) argues AI coding agents fail on missing company context, not intelligence, and outlines context-engine design: avoid curated markdown, separate access from understanding, and use schema discovery for relational questions.

- Techniques: Derive context from systems instead of hand-curated files; Deterministic team graph from GitHub; Rules-file discovery and index; Schema-less lookup, then deterministic query; Two retrieval modes: deep research and fast unfurl; Context hydration to avoid repeated discovery searches
- Tools: MCP, GitHub, Slack, OAuth, SSO, OpenAI API, Anthropic API

## [The unreasonable effectiveness of BM25 for agentic search — Jo Kristian Bergum, Hornet.dev](../videos/fZH97QHHYjY.md)
`fZH97QHHYjY` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: rag-retrieval, evals

Jo Kristian Bergum argues BM25 is back for agentic search: LLM agents write long, precise queries that suit lexical matching, and the baseline was undertuned. Retrieval results can be exposed as a filesystem workspace for grep-style use.

- Techniques: Workspace-as-filesystem retrieval; Tuned BM25 baseline before any embedding comparison; Hybrid lexical plus grep for agent search; End-to-end task evaluation for search agents; Evidence-stuffing ablation
- Tools: BM25, grep, ripgrep, sed, BrowseComp-Plus, Hornet (vendor BM25 engine)

## [Training Taste — Thais Castello Branco, Taste Labs](../videos/sDMGWK4wZ_w.md)
`sDMGWK4wZ_w` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: evals, product-ux, vibe-coding-app-building

Thais Castello Branco (Taste Labs) on measuring and fighting "AI slop" in design: decompose subjective quality into checkable parts, build feature classifiers that flag slop, and turn a brand into structured context the agent both follows and is graded against.

- Techniques: Decompose subjective quality into probes; Split objective checks from aesthetic judgment; Rule-aware intentional divergence; Brand spec as both generation context and rubric; Retrieve pre-built brand systems
- Tools: Claude Design, Wayback Machine-style web crawl

## [Design at the Speed of Adjectives — Paul Bakaus, Renaissance Geek, Inc.](../videos/v42opQpCy60.md)
`v42opQpCy60` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: vibe-coding-app-building, product-ux, coding-agents

Paul Bakaus on steering coding agents toward good design with a skill (Impeccable) that maps vague design adjectives like "bolder" to project-specific meanings, keeping humans in the loop instead of one-shotting.

- Techniques: Project-defined verb and adjective commands; Self-check against a stated failure test; Pre-brief questions before generation; Workflow-stage command mapping; Community-tested experimental commands
- Tools: Impeccable, Claude Code, GitHub Copilot, Cursor, Codex, Figma, Webflow, Claude Design, Radiant Shaders

## [7 Ways you can Avoid Claude Session Limit](../videos/MXclE0yaDXc.md)
`MXclE0yaDXc` · Kai Explains · 2026-09-02 · q3 · intro · tutorial · also: token-cost-efficiency

Kai's seven tips for stretching Claude chat and Cowork usage limits: trim attachments, plan in chat before building, write short prompts, edit instead of correcting, batch asks, shorten output, and spread sessions across the rolling window.

- Techniques: Convert attachments to plain markdown before upload; Tight-crop screenshots; Plan in chat, then build in Cowork; Short structured prompt with clarifying questions; Edit-and-regenerate instead of follow-up corrections; Single batched message; Terse-output mode via Caveman; Split sessions across the five-hour window
- Tools: Claude (Anthropic chat), Claude Cowork, Google Docs (via doc.new), Caveman (open-source output-compression tool, named by the host)

## [You Don't Need Frontier Models Anymore (Qwen 3.8 27B + DeepSeek Harness)](../videos/3DVRznjCIS8.md)
`3DVRznjCIS8` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: local-ai, agent-architecture, evals

Same local Qwen model, same weights and prompt: the outcome changed with the harness around it (feedback loop, tools, session log, context), so the software matters as much as the model.

- Techniques: Attribute failures to the harness before blaming the model; Close the feedback loop so the agent can verify its own output; Persistent session log as source of truth for long runs; Sweep reasoning effort on a fixed prompt rather than assuming max is best; Size the local model by capacity and bandwidth, then pick quantization; Hybrid local-then-frontier handoff
- Tools: Qwen 3.8 27B (transcript: 'Quen 3.8'), Qwen 3.6, Qwen 3.7 Plus, DeepSeek Harness (transcript: 'DeepSeq Harness'; MIT licensed, plugin components, developer preview), DeepSeek v4 (2-bit quant, transcript: 'DeepSeq v4'), Claude Code (Qwen's benchmark harness for four agentic evals), Opus API (cost comparison), VS Code Copilot (failed reproduction run), Unsloth Q6 build of Qwen 3.8, Simon Willison's test prompt (reasoning-effort test), DeepSWE 1.1 (benchmark), OSWorld (computer-use benchmark)

## [China Just Open-Sourced Humanlike Memory for AI Agents (Tencent DB)](../videos/W3yHP9_jYNk.md)
`W3yHP9_jYNk` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: memory, token-cost-efficiency, agent-architecture

Teardown of Tencent's open-source agent memory plugin: folding tool output into disk files plus a layered memory store. Claims 33% to 50% pass rate with 61% fewer tokens, which the speaker partly rechecked.

- Techniques: Offload tool output to disk with an ID-indexed map in context; Pressure-scaled folding; Layered consolidation memory; Persona-first recall; Keep the memory prefix cache-stable; Treat shared memory writes as untrusted input; Recompute vendor benchmark tables
- Tools: Tencent Cloud memory plugin (MIT, GitHub, about 10k stars in four months; the repo name is not stated), OpenClaw (install target, one command), SQLite (default local store), Tencent Cloud Vector database backend, Chroma (context-rot study), Mermaid (diagram format for the in-context map), Mem0 (published its own memory benchmark, per the speaker), Zep (published a rebuttal, per the speaker), WideSearch (ByteDance Seed benchmark), WeBench (name as transcribed), SWE-bench (token columns checked by the speaker), PersonaMem (persona benchmark)

## [How To Use Claude Design To Build Beautiful Sites](../videos/bBlY5YOsKN8.md)
`bBlY5YOsKN8` · AI LABS · 2026-09-02 · q3 · practitioner · tutorial · also: vibe-coding-app-building, coding-agents, skills-self-improvement

A five-stage workflow for building a site with Claude Design: write a design.md brand file first, build a design system from it, wireframe, produce the full design, then hand off to Claude Code with a Supabase backend.

- Techniques: design.md-first planning skill; Preview design.md outside the token-metered tool; Design system from design.md; Wireframe, then batched comments; Full design from a chosen wireframe; Claude Design to Claude Code handoff; Post-build design.md conformance review; Supabase skill install and MCP connection
- Tools: Claude Design, Claude Code, Opus 5, Opus 4.7, Haiku, Fable, design.md (Google format), Supabase, Supabase agent skills (general and best-practices), Supabase MCP, Supabase CLI, VS Code

## [How To Never Run Out Of Codex and Claude Usage Limits](../videos/jwje1JK8Nqs.md)
`jwje1JK8Nqs` · AI LABS · 2026-09-02 · q3 · practitioner · tutorial · also: token-cost-efficiency, claude-code, coding-agents

AI Labs walks through 24 tactics for stretching Claude Code and Codex usage limits, from habits (clear, compact, rewind, one big prompt) to settings (model and effort, skill and CLAUDE.md size, memory, bundled skills, output caps, advisor).

- Techniques: Clear between unrelated tasks; Compact with explicit keep-instructions, before breaks; Rewind instead of correcting; Batch changes into one prompt; Turn off automatic session recaps (Claude Code only); Set model per task with /model and effort with /effort; Pin sub-agent model in the prompt, or route automatically with a skill; Keep skills small with reference files; Write a lean CLAUDE.md and per-folder CLAUDE.md files; Check spend with the usage command; Use a CLI instead of an MCP server when the CLI is enough (Supabase example); Turn off memory and bundled skills; Disable or cap sub-agent workflows; Filter passing tests out of tool output with a hook; Cap bash output length; Replace the built-in advisor with a custom on-demand agent; Message between Claude Code sessions with only the relevant part
- Tools: Claude Code, Codex, Claude Opus, Claude Sonnet, Claude Haiku, GPT-5.6 Sol (spoken as GPT 5.6 Soul), GPT-5.6 Terra (spoken; name uncertain), GPT-5.4 Mini, ChatGPT plans (Free, Go, Plus, Pro), Claude Pro and Max plans, Supabase, Supabase CLI

## [Hermes Agent Skills That Make It 10x More Powerful](../videos/WJgxX0Eib6k.md)
`WJgxX0Eib6k` · AI LABS · 2026-09-02 · q2 · intro · review · also: skills-self-improvement, token-cost-efficiency, multi-agent

Walkthrough of third-party skills for the Hermes agent (planning-with-files hook, Delegate Setup, RTK, Mantis security reviews, Agent Reach, Skill Retriever), most of which work with any coding agent; thin on exact commands and partly sponsored.

- Techniques: File-backed plan injected by a hook; Orchestrate several installed coding agents from one agent; Route shell commands through RTK via a skill; Scheduled security review with alerts; Retrieval-filtered skill list
- Tools: Hermes Agent, Claude Code, Codex, Cursor, planning-with-files, Delegate Setup, RTK, Mantis (Google), Agent Reach, Skill Retriever, Plural Workbench, Opus

## [These New Claude Skills Are Actually Insane](../videos/jyLKRN36-Dc.md)
`jyLKRN36-Dc` · AI LABS · 2026-09-02 · q3 · practitioner · review · also: skills-self-improvement, claude-code, product-ux

AI LABS walks through six new agent skills: a self-improving skill-learning log, a four-rule coding baseline, a logged-in website CLI (OpenCLI), a variant-picker for UI, and two product-business skill sets for onboarding, paywalls, churn and validation.

- Techniques: Per-project learning log for skills; Parent-folder CLAUDE.md for base coding rules; Onboarding and paywall pattern; Cancellation save flow; Logged-in site commands via OpenCLI; Variant exploration for one UI section; Demand validation before building
- Tools: Claude Code, CLAUDE.md, Agent skills, log.md (task-observer output file), OpenCLI, Chrome extension (OpenCLI), Variate skill, Hallmark design skill (mentioned, not shown), Next.js, Supabase, Corey's 48-skill marketing collection, SVG (brand logo format)

## [If You Understand These 5 AI Terms, You’re Ahead of 90% of People](../videos/04rRN1oqO2A.md)
`04rRN1oqO2A` · Kai Explains · 2026-09-02 · q2 · intro · review · also: rag-retrieval, local-ai

Kai Explains walks through five foundational AI terms (tokens, context window, temperature, hallucination, RAG) for non-engineers, using plain analogies and personal anecdotes.

- Techniques: Verify-before-trust workflow for AI output; Restate critical context in long sessions; Adjust temperature for the task; Mental model of RAG for debugging products
- Tools: Claude, ChatGPT, Gemini

## [MCP is Dead...](../videos/Rrju5Y0iiBM.md)
`Rrju5Y0iiBM` · Kai Explains · 2026-09-02 · q3 · practitioner · news · also: mcp-and-tools, security-guardrails

Kai Explains argues "MCP is dead" misreads the moment: the protocol's own pain points (tool-definition context bloat, session state) were real, and a July 2026 spec rewrite addresses them, while adoption kept growing.

- Techniques: Cap the number of MCP servers attached to an agent; Diagnose tool-definition bloat before blaming the protocol; Design remote MCP servers to be stateless for load balancing; Vet community MCP servers before installing
- Tools: Model Context Protocol (MCP) with July 28 2026 spec, MCP SDKs (Anthropic-maintained; one other SDK referenced), GitHub MCP server, Filesystem MCP server, Notion (database connector), Hyperframes (video framework), Google Cloud managed remote MCP servers, JetBrains, Cursor, Windsurf, Replit

## [Anthropic's Biggest Lie! (The Harness War)](../videos/_DZ4kJwQ50s.md)
`_DZ4kJwQ50s` · Kai Explains · 2026-09-02 · q3 · practitioner · review · also: agent-architecture, claude-code, evals

Compares Claude Code's compaction-based context handling with Prime Intellect's open-source Prime Agent (an RLM-style persistent kernel plus a self-editing "continual harness"). Vendor-reported benchmarks; the context-rot argument is the useful part.

- Techniques: Single persistent kernel as the only tool; Context as a variable (RLM-style chunked processing); Externalized session state instead of compaction; Continual harness: log failures, promote tactics; Guard self-improvement against reward hacking
- Tools: Claude Code, Prime Agent (Prime Intellect, MIT license, installs via a single curl command on Linux or macOS), Claude Opus 5, IPython kernel, Codex (OpenAI coding harness, mentioned by name), GPT-5.4, Gemini, ARC-AGI-3, LongCoT-Mini

## [Want to Run Your Agents For Hours? Use These 12 Rules for Claude.md](../videos/D4uBfIe7SzA.md)
`D4uBfIe7SzA` · Better Stack · 2026-09-02 · q3 · practitioner · tutorial · also: claude-code, testing-verification, coding-agents

Warren from Better Stack walks through 12 rules for a CLAUDE.md file so agents can run longer without constant correction: a living failure log, TDD, clarifying questions, strict types, vetted packages, naming, testing, performance, error handling, and architecture notes.

- Techniques: Failure-log CLAUDE.md with an automated update skill; Size budget for CLAUDE.md, with nesting and skills; Tests as the definition of done; Clarify-before-assuming rule; Strict type rules in CLAUDE.md; Dependency vetting rule; Human-style end-to-end and screenshot verification; Endpoint latency budget and database-first queries; Fail-fast error convention referenced from CLAUDE.md; Architecture lookup table in CLAUDE.md
- Tools: Claude, CLAUDE.md, AGENTS.md, Codex, Claude memory, Chrome, iOS Simulator, Playwright, PostgreSQL, Rust, TypeScript, GitHub

## [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j](../videos/Q0VkgCyNVUg.md)
`Q0VkgCyNVUg` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: memory, rag-retrieval

Neo4j's Stephen Chin argues agent memory stored as markdown or vector lookups fails on multi-hop questions, and shows a live home-lab demo where a vector-seeded graph traversal beats a vector-only store.

- Techniques: Vector-seeded graph traversal; Graph as the agent's write target; Inspect-and-fix retrieval loop; Let the coding agent write the graph layer; Same-source backend A/B test; Keep destructive memory tools away from the agent
- Tools: Neo4j, Cypher, Cognee, OpenClaw, Goose, Hermes Agent, pgvector, LanceDB, Claude, Proxmox, pfSense, HAProxy

## [Scaling to Long Horizons — Ross Taylor & Chengxi Taylor, General Reasoning](../videos/2bvtay8wGYI.md)
`2bvtay8wGYI` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: training-finetuning-rl, agent-architecture, evals

GR's Ross and Chengxi Taylor trace RL-for-reasoning from Galactica and 2022 PPO recipes to long-horizon agents: value models, compaction, pipeline RL, and a benchmark where frontier models lost money.

- Techniques: Value-model (critic) RL for long, variable-length trajectories; RL-trained compaction; File-system scratchpad, self-search and archive tools for long-horizon context; Pipeline RL with bounded off-policy lag; Verifiable-reward PPO after continued pretraining (2022 recipe); Open-ended, outcome-scored long-horizon benchmark
- Tools: Galactica (Meta science LLM; 30B variant cited), Llama 2, Llama 3, Reasoning Llama (named, no details), ChatGPT, GPT-3.5, GPT-4, OpenAI o1, DeepSeek-R1, InstructGPT (2022, cited for RLHF results), PaLM (540B, cited for comparison), Chinchilla (cited for comparison)

## [Stop Burning Tokens: Why self-improvement needs domain expertise first - Annabell Schäfer, Langfuse](../videos/eAXxdtNlK04.md)
`eAXxdtNlK04` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, observability

Langfuse's Annabell Schäfer shows that a clear-cut yes/no target function (single-label paper classification) lets an optimizer loop improve a small model's prompt, and argues teams need domain experts and high-signal evaluators before auto-improvement pays off.

- Techniques: Fit / validate / test split for prompt optimization; Error clustering to drive hypotheses; Binary, criterion-specific judges instead of Likert-style scores; Task markdown as the loop spec
- Tools: Langfuse, Claude Code, GPT-5 Nano, Claude Opus 4.8

## [From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com](../videos/Btk8wDUVs74.md)
`Btk8wDUVs74` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: memory, data-engineering, product-ux

monday.com's Omri Bruchim and Tomer Ast argue agents fail because they lack understanding, not data, and describe a two-speed "world model" of the user (slow learned profile plus fast live signals) built ahead of time.

- Techniques: Two-speed user model (slow profile + fast signals); Precompute meaning ahead of time, recompute a thin slice at serve time; Source isolation with fallback to last verified context; Urgency gating for proactive notifications
- Tools: monday.com Sidekick, Monday Vibe, Monday Agent, Monday Workflows, Slack, Claude, Gemini, GPT

## [Enterprise Agents Have a Structure Problem - Ishita Daga, Tesla](../videos/B8l81jhvHbI.md)
`B8l81jhvHbI` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: memory, evals, enterprise-adoption

Ishita Daga (Tesla) argues enterprise data agents fail from ambiguity, staleness and team-level preference, not model size, and proposes a tiered source-of-truth structure, a context lifecycle, and open questions on preference.

- Techniques: Tiered source-of-truth hierarchy; Context lifecycle with live sources and event logging; Replay-based evaluation of recent questions; Metric variants in a semantic layer with user selection
- Tools: mem0, Tableau, dbt, GitHub, memory.md files

## [How Codex Works — Dominik Kundel, OpenAI](../videos/shRR1e2HXMk.md)
`shRR1e2HXMk` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: agent-architecture, coding-agents, sandboxing-execution

OpenAI's Dominik Kundel walks through what happens when a message is sent to Codex: context assembly, sub-agents, computer use, sandboxing, auto-review, WebSocket transport, goal loops and compaction.

- Techniques: Deferred tool loading with tool search; Capping the skills list as a share of the context window; Sub-agent tool set: spawn, send input, wait, shutdown; Code-execution computer use with a persistent REPL; Auto-review sub-agent for escalated actions; Stateful WebSocket transport for agent loops; Goal loop with an explicit done tool; Server-side compaction item
- Tools: Codex, OpenAI Responses API, Codex app server, ripgrep, PowerShell, Node REPL, Chromium, Seatbelt (macOS sandbox), Bubblewrap (Linux sandbox), Cerebras (GPT-5.3 Codex Spark), Ollama, LM Studio

## [Don't Let the LLM Drive - Ornella Bahidika & Joel Allou, Microsoft](../videos/m24UKZomm7k.md)
`m24UKZomm7k` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, voice-multimodal

Microsoft's ACE live voice tutor: run a lesson as a state machine where the model only proposes narrow outputs and a harness validates them and decides the next step.

- Techniques: Lesson-as-state-machine harness; Per-step narrow prompts; Model proposes, harness decides; Right-size the model to the harness; Reliability coin-flip test
- Tools: Claude Opus 4.7, Claude Haiku 4.5

## [Autonomous Agents for Scientific Tasks - Sina Shahandeh, Radicait](../videos/XLEYtv3cMlw.md)
`XLEYtv3cMlw` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, multi-agent, evals

Sina Shahandeh (Radicait) on why coding-agent research loops stall on open-ended science, and how decomposing a codebase into linked component docs plus cross-model critique gets better hypotheses.

- Techniques: Hierarchical component docs as a scaffold; Hypothesis generation over each component; Multimodal model as a qualitative metric; Split roles across models in the loop; Per-iteration outcome review
- Tools: Codex, Obsidian, Gemini, Oracle CLI, GPT-5.5 Pro (as transcribed)

## [fighting slop with slop — Vaibhav Gupta, Boundary](../videos/AMiyLItEtLA.md)
`AMiyLItEtLA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: software-factory, testing-verification, dev-tools

Vaibhav Gupta of Boundary argues that teams without code review can keep AI-written code stable by building internal tools that enforce invariants, mine agent transcripts, and rethink the language and tooling layers underneath.

- Techniques: Invariant-only architecture file; CLI guard checks for architecture invariants; Required reading as the gate for design docs; Transcript triage loop; A/B test skills or features by agent outcomes; Per-function CLI and describe tool
- Tools: BAML, Claude, Codex, TypeScript, Python, Rust, Go, Ruby, Java, WASM, ripgrep, Notion

## [AI on Your Lakehouse: Context Comes in Shapes, Not Queries — Zach Blumenfeld, Neo4j](../videos/kRkcNOsRyYg.md)
`kRkcNOsRyYg` · AI Engineer · 2026-08-18 · q3 · practitioner · workshop · also: rag-retrieval, data-engineering

Neo4j workshop on graph shapes for agents over a lakehouse: a metadata semantic layer over the warehouse, a deterministic document-tree-plus-links graph, and Leiden community "themes" built without LLM labels.

- Techniques: Metadata-only semantic layer graph; Deterministic document-structure graph; Hierarchical URI IDs for scoped search and traversal; Semantic query expansion for full-text search; Structure-only community themes; Spec-driven Cypher generation with a vendor skill; Agent with a database CLI for ad hoc graph reasoning; Partial re-sync of a deterministic graph
- Tools: Neo4j, Neo4j CLI, Cypher, Graph Data Science (GDS), NeoCarta, Neo4j Virtual Graph, Lucene full-text index, Leiden, Louvain (mentioned), Claude Code, Claude Opus 4.8 (model used in demo), BigQuery

## [In the Land of AI Agents, the Verifiers Are King — Tariq Shaukat, Sonar](../videos/VrpEyglYgeU.md)
`VrpEyglYgeU` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: testing-verification, pr-code-review

Sonar's CEO argues AI coding agents need verification built into the loop: guide them with context and constraints, layer algorithmic and agentic checks, and keep the codebase clean. It is a vendor talk, and its numbers are self-reported.

- Techniques: Guide with context and constraints; Zero-trust multi-layer verification; Verification inside the agentic loop; CI verification loop with agent PR review and quality gates; Scheduled code-maintenance and remediation agents
- Tools: Sonar Vortex (product launched the day before the talk, per the speaker), METR time-horizon benchmark chart, Models named: Mythos, Fable, GPT 5.5

## [Why Software Factories Fail](../videos/Ib5GBkD555M.md)
`Ib5GBkD555M` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: software-factory, pr-code-review, evals

Dex (HumanLayer) argues that agent "lights-off" software factories fail because coding models are trained on tests passing, not maintainable code, so teams must restore code review and plan up front.

- Techniques: Staged plan before agent implementation; Review the plan so the PR review is short; Check for test gaming with pre-patch runs and a quality judge; Diagnose RL-style reward gaps
- Tools: Claude Code, Codex, SWE-bench Multilingual, SWE-Marathon, DeepSWE, Frontier Code, Linear, Jira, HumanLayer

## [HTML Is All Agents Need — James Russo, HeyGen](../videos/Cz4v1WHVyZc.md)
`Cz4v1WHVyZc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: voice-multimodal, skills-self-improvement, product-ux

HeyGen's Hyperframes turns agent-written HTML into deterministic MP4 video by freezing the browser clock and seeking frame by frame; the thinnest HTML wrapper beat heavier DSLs.

- Techniques: Thin HTML as the agent output format; Deterministic frame-by-frame browser rendering; Single render path for preview and output; Taste-focused skills instead of syntax skills; Small model as a format canary; Storyboard, iterate, then human last-mile edit; Website-to-asset single-shot skill
- Tools: Hyperframes, HTML/CSS/JS, Three.js, WebGL, WebGPU, Lottie, Rive, Remotion (transcribed as "Promotion"), After Effects, Premiere Pro, Gemini 3 Flash, Claude Code

## [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](../videos/R3-anFK1YM8.md)
`R3-anFK1YM8` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: memory, evals, local-ai

Sakana AI researcher on memory harnesses for long-horizon research agents running on local models; a ranked decision-ledger recall policy beat both no memory and plain vector RAG, at lower cost.

- Techniques: Write-manage-read memory loop; Ranked decision-ledger recall; Recall-mode ladder with an oracle; Ablate with wrong and recent memory; Local, controlled eval pipeline
- Tools: DeepSeek V4 Flash, Qwen (4-bit quantised), XBench, vector RAG, Spyder V2 benchmark

## [Medic for Apache Spark - First Aid for Failing Jobs - Drasko Profirovic, Pinterest](../videos/0RNNfxpdbQk.md)
`0RNNfxpdbQk` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: observability, multi-agent, testing-verification

Pinterest's Drasko Profirovic on Medic, an agentic Spark failure-diagnosis tool, and how its prototype became a multi-agent system with record/playback testing, log and metrics handling, and sub-agents.

- Techniques: Record/playback end-to-end agent harness; Learned red-herring filtering for logs; Metrics as a collaged graph image in a quarantined sub-agent; Supervisor with parallel hypothesis researchers; Per-agent prompt plus MCP tool subset; OpenTelemetry traces as step waterfalls
- Tools: Apache Spark, LangGraph, LangGraph DeepAgents, LangFuse, OpenTelemetry, Model Context Protocol (MCP), Grafana, Airflow, Slack, vector database

## [Why We Killed Our Multi-Agent Pipeline — Subbiah Sethuraman and Abhilash Asokan, ZS Associates](../videos/u6jJcIFDLE4.md)
`u6jJcIFDLE4` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: multi-agent, agent-architecture, enterprise-adoption

ZS Associates explain why their multi-agent pharma analytics pipeline failed and how they rebuilt it: deterministic signal detection, one reasoning agent, and a knowledge graph used as a control plane.

- Techniques: Probe the design with a coding agent; Deterministic signal gate feeding an investigator agent; Single reasoning owner with scoped investigation subagents; Knowledge graph as the agent's control plane; Hypothesis-traversal investigation loop
- Tools: Claude Code, bash, knowledge graph (tool not named), relational database (not named)

## [Scaling Compute on Context — Jack Morris, Engram](../videos/WiqDvX6isc4.md)
`WiqDvX6isc4` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: memory, training-finetuning-rl, models-research

Jack Morris (Engram) frames "scaling compute on context": with a fixed private dataset and a pretrained model, the only scaling axis left is compute, and he surveys why naive, compaction, distillation, synthetic-data and RL approaches all saturate.

- Techniques: Naive continued training on a private corpus; KV compaction of in-context data; On-policy distillation toward in-context behaviour; Self-study (generated QA conditioned on the corpus); Synthetic continued pretraining; Unsupervised RL environments over the corpus; Gradually harder self-generated curriculum
- Tools: Cartridges (self-study paper, named on slide), On-policy distillation, GRPO (named as an RL loss example), KV cache compaction (named approach)

## [Claude Managed Agents and Evolution of Agentic Surfaces — Gagan Bhat & Isabella Kai He, Anthropic](../videos/K0X9QDRkIdg.md)
`K0X9QDRkIdg` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, sandboxing-execution, evals

Anthropic engineers explain how agent surfaces moved from the Messages API to Claude Managed Agents, which separates the brain from the hands, logs sessions durably, and adds vaults, dreaming and outcomes.

- Techniques: Brain/hands decoupling with on-demand sandboxes; Append-only session log as the resume point; Re-reading discarded context from the log; Vault-based credential injection; Restricted network allowlist per environment; Rubric and failure-case grader loop (outcomes); Batch dreaming over transcripts and memory; Harness-debt audit when models change
- Tools: Claude Managed Agents, Claude Agent SDK, Claude Code, MCP servers, MCP tunnels, self-hosted sandboxes

## [How Evals and Prompts Shape Agent Behavior — Preetika Bhateja & Daniel Bump, YouTube Ads](../videos/xyL2Ltkh-SA.md)
`xyL2Ltkh-SA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, observability

Two YouTube Ads team members on building evals for agents: tools first, intuition before scale, human rater rubrics, reading traces, and pattern-level launch gates.

- Techniques: Tools-first, then critique agent with remediation loop; Intuition-first review before scaled evals; Rubric with examples plus mandatory rater explanations; Negative test cases in the golden set; Judge calibration by sampled agreement monitoring; Trace-based failure diagnosis; Pattern-level metrics with a refreshed test set and online evals; Launch gate defined up front with regression triage

## [How to Kill the Code Review — Ankit Jain, Aviator](../videos/YgEv7IQzGdM.md)
`YgEv7IQzGdM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: pr-code-review, testing-verification, skills-self-improvement

Ankit Jain (Aviator) argues code review's real job is alignment, not bug-catching, and proposes reviewing agent session intent, test-plan evidence and a codified "AI slop registry" instead of diffs.

- Techniques: AI slop registry; Capture session decisions as acceptance criteria; Test plan from criteria plus registry invariants, run against a preview; Agent-driven UI evidence with DB snapshots; Review the plan and evidence, not the diff
- Tools: GitHub, Aviator Verify

## [A Practitioner's Guide to Graphs - Tim Ainge, Good Collective](../videos/3ySF0I5iE_0.md)
`3ySF0I5iE_0` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: rag-retrieval, data-engineering

Tim Ainge (Good Collective) on when graphs help AI apps: schema-first graph extraction, entity matching, and graph-native retrieval (personalized PageRank, shortest paths, subgraph pattern matching) for cheaper, more reliable results.

- Techniques: Schema-constrained graph extraction; Ontology normalisation instructions; Embedding-based entity resolution before node creation; Personalized PageRank from a seed node; Subgraph context retrieval via path queries; Subgraph pattern matching on code graphs
- Tools: Cypher (graph query language, ASR-garbled as 'cipher'), SQL (used as the comparison baseline), HippoRAG, Pinterest PixieRank (cited as the PPR reference), Embedding models, Structured outputs from an LLM, eShop (.NET reference codebase)

## [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization - May Walter, Hud](../videos/JJGbw4ggaFs.md)
`JJGbw4ggaFs` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: software-factory, observability, coding-agents

May Walter (HUD) shows how HUD runs a weekly agentic workflow on GitHub Actions with Claude Code that mines production traces, scores performance fixes by ROI, verifies them at runtime, and sends a human-readable report to Slack.

- Techniques: Scheduled agentic investigation with runtime verification; Function-level production context map; Query language plus task skills; ROI and risk scoring with a human-readable gist; Vendor-neutral workflow layer; Targeted automatic checks for known performance smells
- Tools: Claude Code, GitHub Actions, MCP, ClickHouse, Slack

## [LLM Knowledge Bases: a practical guide — Ben Holmes, Warp](../videos/I3bpdgFJCUY.md)
`I3bpdgFJCUY` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: memory, skills-self-improvement, agent-architecture

Ben Holmes (Warp) shows a markdown-first personal knowledge base: voice-dictate raw notes, have an agent enrich and link them, generate wikis, run it on a cloud schedule, and build graph views with HTML.

- Techniques: Enrich-note skill with a processed-timestamp marker; Controlled tag vocabulary with a no-invention rule; Backlinks via key-term search over a file tree; Raw folder to wiki generation; Sync-in, run, sync-out cloud schedule
- Tools: Obsidian, Obsidian Headless CLI, Warp, oz.dev, Hubble, Claude, Codex app, Exa, Tailwind CSS, Whisper Flow, Handy, GLM 5.2

## [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../videos/Kz4QJmNrVXU.md)
`Kz4QJmNrVXU` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: multi-agent, coding-agents

Matt Dailey (Ref) argues that AI makes individual engineers faster but not teams, and proposes working in shared docs for decisions, with agents as stateless actions, so humans keep ownership of the product.

- Techniques: Doc as shared state, agents as stateless workers; Two-gear workflow: plan vs polish; Front-load decisions before code; Plan as a portal to the system; Idea exploration before build

## [Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI](../videos/WP3hjUXd918.md)
`WP3hjUXd918` · AI Engineer · 2026-08-18 · q4 · practitioner · workshop · also: token-cost-efficiency, evals, rag-retrieval

Towards AI workshop on context engineering: prompt caching makes compaction costly, and on their AI tutor keeping full history beat every compaction preset on recall, cost and latency.

- Techniques: Head and tail truncation of big tool outputs; Sliding window and clearing old tool outputs; Selective retention and summarization with a threshold; Filesystem knowledge base with progressive disclosure; Hybrid retrieval with a token cap; Eval harness: presets by tasks, then grade; Planted-fact recall probe; Log every turn
- Tools: LangChain (create_agent, middleware), FastAPI, Next.js, Gemini 3.5 Flash, DeepSeek V4 Flash, Claude Code, Codex, Opik (transcribed as 'OPIC'), Hugging Face Spaces, BM25, Dense embedding retrieval

## [How Forward Deployed Engineering is done at Ramp — Leo Mehr](../videos/ITMXwI6QL6A.md)
`ITMXwI6QL6A` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: enterprise-adoption, software-factory, evals

Leo Mehr (Ramp) on forward deployed engineering: scope hard before building, then replace each FDE pipeline stage with agents, with evals and good context as the hard parts.

- Techniques: Scoping questionnaire before any build; Clarifying-question intake agent before spec; Stage-by-stage agent factory for the FDE lifecycle; Per-stage quality checks with evals, rubrics and human feedback
- Tools: Notion, Notion Agents, Slack

## [Lessons from Studying Every Memory System — Shlok Khemani, Independent](../videos/5ZGyKWjQDr0.md)
`5ZGyKWjQDr0` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: memory, product-ux, agent-architecture

Shlok Khemani traces how ChatGPT and Claude memory evolved from 2024 to 2026, and argues memory is a product and compute problem, not a RAG problem, with context as the real cap.

- Techniques: Running profile with background re-synthesis (dreaming); Search tools over past conversations instead of stored facts; User-visible and user-editable profile with re-synthesis on edit; Dense keyword-clue memory entries; Timestamped memory entries
- Tools: ChatGPT, Claude, Gemini, Poke, Claude Code, OpenClaw, Hermes

## [Skills are new features: Building Skill-Centric Harness — Yogendra Miraje, FactSet](../videos/7jjudsEhBtM.md)
`7jjudsEhBtM` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: skills-self-improvement, agent-architecture, governance-compliance

FactSet's principal AI engineer argues skills are the new product features and engineers should ship harnesses, then covers a minimal skill harness, routing via descriptions, eval-gated skills, and skill-library governance.

- Techniques: Minimal skill registry and loop; Write descriptions as routing signals; Cut skills by user intent; Front-load critical instructions and re-run evals on model upgrades; Shortlist skills before they hit the system prompt; Governance as a skill PR pipeline
- Tools: Anthropic Agent Skills (SKILL.md format), Claude Code, Codex, bash or code sandbox for skill scripts

## [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../videos/aeTb5BdmTTc.md)
`aeTb5BdmTTc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: enterprise-adoption, coding-agents, skills-self-improvement

How a 10-person team got to shipping with coding agents: treat agent setup as a leadership job, share the best practices, invest in one high-value skill, and close the loop on slop.

- Techniques: Thin CLAUDE.md/AGENTS.md index; Skill as a folder with a short SKILL.md; Runbooks in code comments as discovery hooks; One end-to-end ship-it skill; Nightly code-gardener agent; Shared setup with an opt-out for experiments; First-prompt context audit
- Tools: Claude Code, CLAUDE.md, AGENTS.md, CI/CD, issue boards

## [AI Agents for Performance: Ship Faster, Pay Less — Rajat Shah, Netflix](../videos/CgsWxRUY5Eo.md)
`CgsWxRUY5Eo` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: infra-cost-scaling, coding-agents, pr-code-review

Netflix's playbook for using coding agents on production profiling data to find CPU hot spots, open reviewed fixes, and grow a shared pattern catalog, with a canary gate and an autonomy ladder.

- Techniques: Profile-to-PR agent pipeline; Central anti-pattern catalog in git; Cross-repo sweep for recurring patterns; Canary-gated review; Shift-left catalog injection; Scheduled fixed workflow before autonomy
- Tools: Continuous profilers (sampled call stacks with CPU time), Git and code search across repos, Canary deployment infrastructure, TorchFix (public PyTorch anti-pattern catalog), Spectator (metrics library, named as the source of the counter-object pattern)

## [Persona Engineering: A Field Guide to AI Synthetic Personas — Ishan Anand, InsightSciences.ai](../videos/YnNF55QV0zs.md)
`YnNF55QV0zs` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, models-research, product-ux

Ishan Anand (InsightSciences) on synthetic personas as bounded forecasts: where LLM personas fail (confounders, order bias, attitudes vs behavior), and how to measure them against human distributions and noise floors.

- Techniques: Validate personas against held-out human ground truth; Ground the persona in the full world of the study; Durability tests for option order and wording; Attitude-to-behavior triangulation; Free-text answers mapped to scale via semantic similarity; Fine-tune on survey distributions conditioned on demographics; Noise floor via split-half simulation

## [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../videos/il1c1a2FufU.md)
`il1c1a2FufU` · AI Engineer · 2026-08-18 · q4 · practitioner · workshop · also: coding-agents, skills-self-improvement, multi-agent

Jason Liu (OpenAI) shows how he runs Codex as a personal ops system: pinned long-lived threads, a git-tracked memory vault, heartbeats, and goal verifiers. Main takeaway: compaction makes long threads workable.

- Techniques: Long-lived pinned thread per workstream; Heartbeat / loop in the same thread; /goal with a verifier and file-backed goal; App shot plus accessibility tree; Git-tracked personal memory vault with agents.md routing; Monitor thread that spawns per-issue threads; Skill from one completed run, with self-edit permission; Annotate a localhost preview to steer the agent; Model and reasoning tiering
- Tools: Codex app, Codex CLI, Codex in-app browser, computer use, Chrome extension, Slack connector, Gmail connector, Google Drive connector, Notion, Linear, Obsidian, GitHub

## [Claude for Long-Horizon Tasks — Lance Martin, Anthropic](../videos/9QebvrrY3KY.md)
`9QebvrrY3KY` · AI Engineer · 2026-08-18 · q4 · practitioner · workshop · also: agent-architecture, memory, multi-agent

Lance Martin (Anthropic) on designing long-horizon async agents: decouple brain from hands, verify in a separate context, dream offline to fix memory, and run org-level shared harnesses.

- Techniques: Brain/hands split with an append-only session log; Non-destructive context via append-only session object; Build/verifier loop in separate contexts; Dreaming: offline memory consolidation; General memory substrate with the model managing its own structure; Org-level shared harness with its own identity
- Tools: Claude Managed Agents, Claude Agent SDK, Claude Code, Claude Tag, Message API, Continued Learning Bench, METR time-horizon benchmark, Slack

## [Skills are the New SDKs - Elvin Aghammadzada, DataRobot](../videos/LC3-P7v3yoI.md)
`LC3-P7v3yoI` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: skills-self-improvement, mcp-and-tools

Elvin Aghammadzada (DataRobot) argues agent skills are a progressive-disclosure context tool that complements MCP, and that skills are software needing versioning, evals and security review.

- Techniques: Progressive disclosure via a skill index; Context budget ceiling; Skill as a wrapper around an MCP server; Split by role: skill for reasoning, MCP for execution; Treat skills as versioned, tested software
- Tools: Claude Code, Codex, Copilot, Gemini CLI, OpenClaw, ClawHub, MCP

## [Content Is Code - Matt Palmer, Conductor](../videos/yv6xovSsB1U.md)
`yv6xovSsB1U` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: product-ux, coding-agents

Matt Palmer (Conductor) argues code is becoming the medium for technical content, so docs, changelogs and product videos should be generated from a structured source of truth.

- Techniques: Generate product tour videos with React and Remotion; Derive changelogs and product updates from the diff; Keep design tokens separate from app code; Write internal docs and skills for agents
- Tools: React, TypeScript, Remotion, CSS, HTML, Claude

## [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](../videos/Z-c11pV_uvU.md)
`Z-c11pV_uvU` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: agent-architecture, claude-code, multi-agent

Frank Coyle (UC Berkeley) walks through the Claude Certified Architect exam's scenarios and uses each one's anti-patterns to teach agent loops, subagent context isolation, compaction, and non-interactive runs.

- Techniques: Stop-reason-driven agent loop; Three-level CLAUDE.md hierarchy; Single-purpose subagents with minimal tools; Context slicing for critic and reviewer agents; Forked subtask context with summary return; Threshold-triggered compaction; Non-interactive CI runs with batch processing
- Tools: Claude Code, Claude API (messages, stop_reason, tool use), CLAUDE.md, MCP (Model Context Protocol), Message Batches API

## [Claude Code Setup Guide By The Creator Himself](../videos/pGro_uKt-_M.md)
`pGro_uKt-_M` · AI LABS · 2026-08-02 · q2 · practitioner · tutorial · also: claude-code, evals, token-cost-efficiency

AI LABS walks through Claude Code creator Boris Cherny's setup advice: strip your Claude Code setup to a baseline with each new model, keep only what Claude can't infer, and gate work with evals that can fail. Includes a sponsored segment.

- Techniques: Baseline-then-add-back setup audit; Usage triage; Keep-rule for CLAUDE.md; Doctor audit; Fail-able acceptance checks written first; Built-in headless browser verification; Outcome-first prompting; Escalation ladder for model mistakes; Recurring cloud routines for maintenance
- Tools: Claude Code, CLAUDE.md, Claude Code skills, MCP server, Claude Code hooks, Claude Code plugins, context command (Claude Code), usage command (Claude Code), doctor command (Anthropic), safe mode (Claude Code), headless Chrome, sub-agents

## [LLM Wiki + OKF Every Local AI Now Shares ONE Memory](../videos/9ciGYHHOLyU.md)
`9ciGYHHOLyU` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: memory, mcp-and-tools, local-ai

A solo builder turns Karpathy's LLM-wiki idea and Google's OKF spec into a deterministic, local MCP memory layer, then documents the failures that showed up with a local model.

- Techniques: Librarian agent over a deterministic markdown store; Seed memory in MCP instructions and tool descriptions; Enrich-before-create and bidirectional linking rules for memory writes; Deterministic graph lint for orphans and broken links; Contradiction handling by rewrite, not append; Give the memory a model that makes write decisions well
- Tools: Karpathy LLM wiki (concept), Google OKF spec, MCP, llama.cpp server, llamaswap2, Qwen3 30B-A3B, Gemma 12B, Claude Opus (cited as the level of model needed for spec-following), Author's own memory tool, with web UI and graph visualizer (open source, link in description, not named)

## [How To Use Codex To Build Insanely Beautiful Websites Using GPT 5.6 Sol](../videos/pHstb0JGGhE.md)
`pHstb0JGGhE` · AI LABS · 2026-08-02 · q3 · practitioner · tutorial · also: coding-agents, vibe-coding-app-building, skills-self-improvement

Seven-stage tutorial for building a non-generic landing page with the Codex app and GPT 5.6, using AGENTS.md, a design skill, a design.md brand file, generated images, and a deploy step. Main lesson: encode taste and brand in files, not in each prompt.

- Techniques: Scoped seed prompt; AGENTS.md via /init, plus a self-verify rule; Install a design skill and forbid the default one; Browser verification loop; design.md brand system; Plan-mode image generation into an assets folder; Screenshot-based layout cloning; Single-section component swap; Performance pass; Local commits as checkpoints; Deploy with the site skill
- Tools: Codex (in the ChatGPT app), GPT 5.6, GPT image model, Next.js, AGENTS.md, GPT Taste skill, OpenAI site skill, Anthropic front-end design skill, design.md (format introduced by Google through Stitch), Aura Build design.md library, 21.dev, Godly components

## [Meta Just Open Sourced 8 Years of Ul Components (Astryx)](../videos/4GaR7k9VMp4.md)
`4GaR7k9VMp4` · Better Stack · 2026-08-02 · q2 · intro · review · also: dev-tools, vibe-coding-app-building

Walkthrough of Meta's open-source Astryx React component library (built on StyleX): theming via tokens, component-level overrides, Tailwind bridge, and an AI-oriented CLI.

- Techniques: Theme from one brand color plus scale settings; Override a token per light/dark mode; Component-scoped override by variant; Custom component variant; One-off style override with xstyle; Tailwind bridge; Feed component docs to agents with the Astryx CLI
- Tools: Astryx (Meta component library; transcribed as 'Asterix'), StyleX (styling library Astryx is built on; transcribed as 'Starlex'), React, shadcn/ui (transcribed as 'ShadCN'), Tailwind CSS, Material UI, Panda CSS (transcribed as 'panda'), Next.js, Inter (transcribed as 'into'), AGENTS.md, TypeScript

## [Graphify + Obsidian is INSANE: Build an AI Second Brain That Never Forgets](../videos/8Kv2tn22QNo.md)
`8Kv2tn22QNo` · Kai Explains · 2026-08-02 · q3 · intro · review · also: memory, rag-retrieval, token-cost-efficiency

Walkthrough of Graphify, which builds a queryable code and docs graph, paired with Obsidian as a markdown second brain; the useful parts are provenance labels, tiered data egress, and the lint maintenance loop.

- Techniques: Persistent codebase graph, queried by traversal instead of re-reading files; Provenance labels on every derived link (Extracted / Inferred / Ambiguous); Tiered data egress across ingestion sources; Three-layer LLM wiki (Karpathy design); Anti-fabrication rule and weekly lint loop for an AI-maintained notes vault; Staged write access to an Obsidian vault
- Tools: Graphify, Obsidian, Claude Code, Codex, Cursor, TreeSitter, faster-whisper, Neo4j, MCP (Model Context Protocol), Claudian (Obsidian plugin for Claude Code), Smart Connections (Obsidian plugin), Khoj (self-hosted Obsidian plugin)

## [Context Window Lie | Why AI Doesn't Actually Remember (ChatGPT, Claude & Gemini)](../videos/Nf8j9w523pw.md)
`Nf8j9w523pw` · Kai Explains · 2026-08-02 · q3 · intro · talk · also: memory, token-cost-efficiency

Explainer arguing a context window is a finite reading limit, not memory: models re-read the whole transcript each call, attention favors the start and end, so reliable agents budget context deliberately.

- Techniques: Itemized context budget audit; Rolling summarization of old turns; Just-in-time file and tool injection; Position-aware instruction placement; External notes injected at conversation start; Pair large windows with retrieval, summarization and prompt caching
- Tools: ChatGPT, Claude, Gemini

## [7 Rules To Use GPT 5.6 Sol Better Than 90% Of People](../videos/STczJBYJf7w.md)
`STczJBYJf7w` · AI LABS · 2026-08-02 · q3 · practitioner · review · also: coding-agents, multi-agent, token-cost-efficiency

AI LABS' four-day hands-on comparison of GPT 5.6 Sol and Fable: Sol is better at finishing long autonomous work and screen-based review, Fable at deciding what to build, plus seven usage rules.

- Techniques: Git checkpoint before a long autonomous run; Codex app sandbox and approval configuration; Single-session delegation of multi-session work; Role-by-role journey review after the build; One-instruction-removal test for prompts and skills; Plan with one model, build with another
- Tools: GPT 5.6 Sol, GPT 5.6 Terra, GPT 5.6 Luna, Ultra (Sol multi-agent mode), Codex (app and CLI), ChatGPT app, Fable, Opus 4.8, Opus, Sonnet, Qwen 3.6, Cursor

## [Facebook's Release Just Gave Claude Code A New Design System](../videos/-HEdqzzYKco.md)
`-HEdqzzYKco` · AI LABS · 2026-08-02 · q2 · practitioner · review · also: claude-code, vibe-coding-app-building, skills-self-improvement

Walkthrough of Meta's open-source React/StyleX component library (transcribed as "Asterix"), built to be read by coding agents via a CLI, plus a sponsor read and a plug for the presenter's skills.

- Techniques: Install the design system with the package manager; Run the init command to write agent instructions; Prompt for a whole site and let the agent pull from the CLI; Generate a manifest of CLI commands and flags for grounding; Screenshot and fix loop in headless Chrome; Chain a generic anti-slop review skill after the build
- Tools: Asterix (Meta's design system, transcript name; likely a caption misspelling), React, StyleX, shadcn/ui (transcribed as ShadCN), Next.js (App Router and Pages Router), npm, Claude Code, CLAUDE.md, AGENTS.md, globals.css, headless Chrome, AI Slop Detector skill (presenter's AI Labs design system)

## [Best Local Agent Harness Right Now (My Top 3)](../videos/YgyyWDGeQWM.md)
`YgyyWDGeQWM` · Kai Explains · 2026-08-02 · q3 · intro · review · also: coding-agents, local-ai, agent-architecture

A survey of local/open coding-agent harnesses (OpenCode, Aider, Pi, plus OpenHands, Cline, Goose) arguing the harness now matters more than the model, with local-model pairing advice and a warning that the list goes stale fast.

- Techniques: Git-native atomic AI commits (Aider); Mid-session model downgrade for cost; Lazy-loaded skill blocks to keep the base prompt small (Pi); Custom subagents with per-agent model and permissions (OpenCode); Parallel agents on one GPU via vLLM; Local model sizing by memory footprint; Pre-standardization vetting checklist
- Tools: OpenCode (172k+ GitHub stars per speaker; 1.68M weekly npm installs as of June 2026), Aider, Pi (by Armin Ronacher), OpenClaw, OpenHands (spoken as 'Open hands'), Cline (spoken as 'Klein'), Goose, Roo Code (archived May 2026), Gemini CLI, Claude Code, Claude Opus 4.8, GPT-5.5

## [Google OKF + RAG: The Ultimate AI Agent Architecture](../videos/CnfuoBYmkJE.md)
`CnfuoBYmkJE` · Kai Explains · 2026-08-02 · q2 · intro · review · also: rag-retrieval, mcp-and-tools

Explainer arguing agents should route high-stakes facts to a curated, Git-versioned markdown knowledge bundle (Google's OKF) and open-ended queries to RAG; a thin router decides per query.

- Techniques: Curated-first hybrid routing; OKF-style concept files; Governing knowledge in Git; Single retrieval facade; Baseline RAG ingestion
- Tools: Google Cloud OKF (Open Knowledge Format, June 2026 per speaker), RAG (retrieval-augmented generation), Pinecone, Weaviate, Qdrant, Milvus, Chroma, PostgreSQL with pgvector, LangChain, LlamaIndex, MCP (Model Context Protocol), Claude

## [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals - Jacob E. Thomas, Results Gen](../videos/IJXjTLPzvAU.md)
`IJXjTLPzvAU` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: evals, product-ux

Jacob Thomas argues persona/role-play agents are judged by fluency metrics that cannot catch anachronistic "composite" historical figures, and proposes a pre-registered, expert-scored, context-window-based eval (Lincoln case study).

- Techniques: Pre-registered fidelity eval for personas; Anachronism-first rubric with voice excluded; Encounter-as-configuration with receipts; Context window grounding over persona fine-tuning; Expert-authored gold set as a CI gate
- Tools: Claude Opus 4.7, Companion (open-source persona prompt framework built by the speaker), Character AI, Hello History, KOSIR, PsyMem, In-Character benchmark

## [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../videos/c35YoMdnI78.md)
`c35YoMdnI78` · AI Engineer · 2026-07-18 · q3 · practitioner · panel · also: software-factory, testing-verification, agent-architecture

Panel debate on whether agent "loops" (Ralph-style, bash-while-true) are hype or working practice; the consensus is loops work for verifiable tasks, need deterministic feedback and human-owned architecture, and are not yet a full software factory.

- Techniques: Fresh-context loop with file-system state; Back-pressure hooks that talk back; Deterministic controller around the LLM step; Context budget with headroom; Bare-model baseline on each new release; Explicit cost decision for high-value verification; Start small and iterate on real users; Vendor code and minimise open-source dependencies; Prefer statically typed languages for agent-maintained code
- Tools: Claude Code, Ralph loop (bash while-true), pre-commit hooks, PostHog, Notion, Sentry, Git, npm, Rust, Haskell, Python, TypeScript

## [On AI and Knowledge — Pablo Castro, Distinguished Engineer & CVP for AI Knowledge, Microsoft](../videos/RGSFUqzqErE.md)
`RGSFUqzqErE` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: rag-retrieval, evals, skills-self-improvement

Microsoft's Pablo Castro splits agent knowledge into intrinsic, extrinsic and learned, and demos Foundry knowledge bases and an Agent Optimizer that tunes agent config from traces.

- Techniques: Three-way knowledge split for agent design; Hybrid retrieval over combined methods; Layered retrieval API; Agentic retrieval with a satisfaction check; Knowledge base as MCP server; Eval generated from traces, then hill-climb the agent config
- Tools: Microsoft Foundry, Foundry IQ, Azure AI Search, Work IQ, Fabric IQ, WebIQ, Agent Optimizer, Foundry Toolkit for VS Code, GitHub Copilot, MCP

## [Building Great Agent Skills: The Missing Manual](../videos/UNzCG3lw6O0.md)
`UNzCG3lw6O0` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: skills-self-improvement, claude-code

Matt Pocock's prerecorded talk gives a four-part checklist (trigger, structure, steering, pruning) for judging and writing agent skills, to escape "skill hell".

- Techniques: Choose user-invoked vs model-invoked per skill; Steps plus reference split with external context pointers; Leading words; Split phases into separate skills to force legwork; Deletion test and sediment audit
- Tools: SKILL.md agent skills, superpowers (comparison skill set), Matt Pocock skills repo (writing-great-skills skill)

## [Imagination Engineering: "Live in the future and then build what's missing."](../videos/Z2Erdirpudo.md)
`Z2Erdirpudo` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: product-ux, vibe-coding-app-building

A YC design lead shows "software on demand" built from a week of public stream-of-consciousness Slack posts, plus a one-morning personal tool, and argues idea generation is the new bottleneck.

- Techniques: Public thought log as agent input; Distil a voice file from public writing; Self-updating design language; Agent-readable glossary markdown; Checklist-driven completeness; Timeboxing with a timer
- Tools: Claude / Claude Code, Opus 4.8, Fable 5, Conductor, Slack, Paper (design tool), ChatGPT (used to make the header image)

## [Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison](../videos/uU5Gv2h8-9g.md)
`uU5Gv2h8-9g` · AI Engineer · 2026-07-18 · q3 · practitioner · interview · also: claude-code, pr-code-review, security-guardrails

Anthropic's Thariq Shihipar and Cat Wu, with Simon Willison, on how Claude Code and Claude Tag change team workflows, code review, auto mode safety, and prompt design, with internal claims about PR share and prompt size.

- Techniques: Staged trust ramp for AI code review; Eval-gated model swap; Behavioral evals built from user complaints; Conditional prompt wording over absolute rules; Per-model system prompts; Classifier-based permissions using user intent; Credential injection through a proxy; Fewer tools with distinct functions; Multiplayer channel agent with shared memory; Dogfooding gate before launch
- Tools: Claude Code, Claude Tag, Slack, GitHub, Datadog, FFmpeg, Remotion, Gemini API, Mountain Project, Claude Fable, Claude Opus 4.8, Claude Mythos

## [Every company should have a Brain — Garry Tan, Y Combinator](../videos/eBUyTS7SzV4.md)
`eBUyTS7SzV4` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: memory, skills-self-improvement, enterprise-adoption

Y Combinator's Garry Tan argues that AI productivity comes from how work is wired (skills as employees, routing tables, company memory with hygiene), not the model, and pitches an open-source "company brain" called GBrain.

- Techniques: Skill file as a single-job employee; Resolver table for routing context; Trigger evals on routing; Skillify at task end; Split latent and deterministic compute; Curated company brain; Select a small working set per task
- Tools: Claude Code, Codex, OpenClaw, Hermes agent, GBrain, Postgres, TypeScript, Markdown skill files

## [The Prompt is the Platform - Dominik Tornow, Resonate HQ](../videos/DqtmZE6Hl0g.md)
`DqtmZE6Hl0g` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: testing-verification, agent-architecture

Dominik Tornow (Resonate) argues the spec, not the code, becomes the product: agents should design a system via deterministic simulation before writing the production implementation.

- Techniques: Intermediate concrete spec between abstract spec and implementation; Simulation-first design loop for the agent; Deterministic simulation of target dependencies with legal fault injection; Forbidden-fruit trace events; Shrink the protocol and build on target primitives
- Tools: NATS.io, Postgres, Rust, Python, TypeScript, Go, Java, Resonate SDK

## [Build Systems, Not Code - Angie Jones, Agentic AI Foundation](../videos/ZD9-4fW2HhM.md)
`ZD9-4fW2HhM` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, multi-agent, security-guardrails

Angie Jones on designing agentic systems like software: systems thinking, workflow paths, decomposition, code-vs-model-vs-human splits, contracts, idempotent retries, and maintainable agents.md files.

- Techniques: Decompose a giant agent prompt by responsibility; Route work by task type: code, model, or human; Structured decision records as agent memory; Idempotent action log with state-based resume; Evidence-not-instructions handling for untrusted content; agents.md at every level with a cold-start test
- Tools: agents.md, agent skills, subagents, Karpathy LLM Wiki (agent memory layer)

## [The Log Is The Agent - Ishaan Sehgal, Omnara](../videos/UPwGaM2MKHY.md)
`UPwGaM2MKHY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, observability

Argues an agent's identity is its append-only event log, not the model or runtime; once workers are disposable, reliability, forking, sharing and ownership follow from the log design.

- Techniques: Log-first agent loop; Persist pending permissions as events; Projections over one record; Compaction as forked log; Fork at a point in the log; Share by access grant, not transcript copy
- Tools: Claude Code, Codex, OpenCode, Claude SDK, Cloudflare Durable Objects, SQLite, JSONL

## [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON](../videos/4kYl2_mqmnQ.md)
`4kYl2_mqmnQ` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: multi-agent, claude-code, coding-agents

A KRAFTON engineer runs AI coding agents across three machines, organizes them as a hierarchy, keeps state in files, and lists the five failures and four open problems that followed.

- Techniques: Agent org hierarchy with scoped context; File-backed agent state with handoff folders; Clear-and-reload instead of compaction; Blocking review gateway with approval hook; Force delegation through a CLI harness; Git-based context sync with per-machine partitions; Single always-on control plane and chat router; Boot command that restores the fleet from state files
- Tools: Claude Code, tmux, tmux capture-pane, SSH, Git, Discord, MCP servers, Kubernetes, Linux, macOS

## [Field Guide to Fable — Thariq Shihipar, Anthropic](../videos/9fubhllmsBU.md)
`9fubhllmsBU` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: claude-code, coding-agents, models-research

Anthropic's Thariq Shihipar gives a practical field guide to working with the Fable model: unhobble Claude with tools, find your unknowns, stay in the loop, and be less reasonable about trade-offs.

- Techniques: Blind-spot pass; Brainstorm via throwaway prototypes; Interview me before building; Reference as the map; Implementation-note log for unknowns; Quiz the agent on its own work; Shrink the system prompt for newer models; Give the agent a tool rather than more context
- Tools: Claude Code, Bash tool, code execution tool, AskUserQuestion tool

## [Don't Ship Skills Without Evals — Philipp Schmid, Google DeepMind](../videos/0vphxNt4wyk.md)
`0vphxNt4wyk` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: skills-self-improvement, evals

Philipp Schmid (Google DeepMind) argues skills need evals like code does, and gives a lean eval-harness recipe: trigger tests, regex asserts, repeated trials, and with/without-skill ablations to decide when to retire a skill.

- Techniques: Trigger and negative-case eval set; JSON cases plus regex asserts; LLM-as-judge for trace-level checks; CI gate on skill diffs; With/without-skill ablation; Isolated, repeated trials; Lean skill plus reference files; Goal-and-constraint skills, scripts for fixed workflows
- Tools: Gemini CLI, Gemini API, Gemini Interactions API, SkillsBench, Claude Code, Codex, Cursor, Antigravity, Python, regex, LLM-as-judge

## [Your agent is blindfolded — Johan Lajili, Poolside AI](../videos/iRcX54EO5g8.md)
`iRcX54EO5g8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: testing-verification, coding-agents

Johan Lajili (Poolside) argues agent trust comes from verification: give agents a CLI to drive and test the app, make them reproduce bugs before fixing, and make the codebase easy for AI to check.

- Techniques: Reproduce-first gate; App-driving CLI for non-web apps; Token-compressed UI snapshot; Let the agent discover its own UI problems; Periodic self-review of logs and repeated actions; Human-like exploratory testing by the agent
- Tools: Poolside internal app-testing CLI (unnamed), VS Code extension, G-Stack (mentioned as an existing tool for screenshots and snapshots)

## [Stop Writing Tone Instructions. Layer Them. - Isadora Martin-Dye, Isadora & Co](../videos/ij-AU9dpJjc.md)
`ij-AU9dpJjc` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: security-guardrails, product-ux

Isadora Martin-Dye on layering a brand-voice AI agent into four stages: non-overridable identity rules, situational context, voice examples, and a deterministic post-generation veto, with fail-loud multi-tenant identity.

- Techniques: Four-layer ordered prompt stack via single assembly; Non-overridable identity layer; Soft context as tone guidance, never quoted; Deterministic post-generation veto with soft flags and hard rejects; Fail-loud multi-tenant identity; Shared veto gate by default; Trainable voice dial from staff edits
- Tools: Threadline (her own missing-persons tool, not a third-party product)

## [The Prompt Is Still a Punch Card - Ted Johnson, JoinIn AI](../videos/hVJOnuhFmTA.md)
`hVJOnuhFmTA` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: voice-multimodal, product-ux

Ted Johnson (JoinIn AI) argues that prompting is a batch-style punch-card protocol that leaves users doing the work, and that AI interfaces should become turn-taking, conversation-like, and aware of who is being addressed.

- Techniques: Classify each utterance, then act only at a floor-free moment; Full-duplex turn-taking with yield and resume; Ask what burden the human still carries; Voice-driven record edits in a meeting
- Tools: NVIDIA Personaplex, OpenAI GPT Realtime 2

## [The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica](../videos/vh2VGuQ3zhY.md)
`vh2VGuQ3zhY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: mcp-and-tools, rag-retrieval, evals

Giving an agent every tool schema on every request breaks accuracy, latency and cost as the catalog grows; the fix is semantic routing that injects only the top-K relevant tools per query.

- Techniques: Semantic tool routing (tool RAG); Just-in-time tool and context injection; K-sweep routing evaluation; Router miss fallbacks; Description writing for retrieval; Routing observability
- Tools: Qdrant, Chroma, Pinecone, Berkeley Function Calling Leaderboard, ToolBench, Anthropic MCP on-demand tool loading write-up, Aurelio Labs semantic-router (open source), MCP0 (cited as an open-source routing project at large scale)

## [You Can't Prompt the Room: The Last Skill AI Won't Replace - Balázs Horváth, VisualLabs](../videos/6bmM45jkMDY.md)
`6bmM45jkMDY` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: product-ux

Balázs Horváth (VisualLabs) argues that deciding what to build, through requirements elicitation, story mapping and value-first design, is now the bottleneck, not writing code.

- Techniques: Story map MVP slice; Persona/what/need/why stories with acceptance criteria as agent input; Four-question value check kept in the repo; Value-first design order (VAD); Usage-frequency success metric; Paired build comparison
- Tools: Story mapping, Business model canvas, Value canvas, User story templates with acceptance criteria, Markdown files in the repo as agent context

## [We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco](../videos/dRmWYHuIJxM.md)
`dRmWYHuIJxM` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: token-cost-efficiency, rag-retrieval, coding-agents

Rajkumar Sakthivel (Tesco) on cutting AI coding-tool token spend by sending less context: a local code index with hybrid search, slimmed results and a relevance threshold, reporting about 94% fewer input tokens on one small benchmark.

- Techniques: Code-aware chunking; Parallel hybrid retrieval; Result slimming; Call-graph expansion; Heuristic relevance gate instead of LLM self-grading; Shared local index across tools; Per-query savings accounting
- Tools: Claude Code, Cursor, GitHub Copilot, Codex, CCE (speaker's free open-source local code index; name as spoken)

## [AI System Design: From Idea to Production - Apoorva Joshi, MongoDB](../videos/T0HhO4YtTfE.md)
`T0HhO4YtTfE` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, evals, product-ux

A MongoDB developer advocate walks through a four-phase framework (product requirements, system design, evaluation and monitoring, cost/latency optimization) using a health insurance claims review system as the worked example.

- Techniques: Four-phase AI system design framework; Quantified solution-agnostic business problem; Three-axis AI role classification; Per-source retrieval strategy from update cadence and content type; Simplest-design-first, evaluate, then iterate; Guardrails as measurable rates; Production signals from human behaviour; Structured outputs as a reliability guard
- Tools: MongoDB, Voyage AI

## [From Writing Code to Designing Systems: How the Developer Role is Changing — Chris Noring, Microsoft](../videos/GdvKNwMcfd0.md)
`GdvKNwMcfd0` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: coding-agents, software-factory, multi-agent

Microsoft's Chris Noring on moving from writing code to running agents: start in the CLI, use AGENTS.md, skills and custom agents as guardrails, and delegate background work that comes back as draft PRs for human review.

- Techniques: Layered repo guardrails (AGENTS.md, skills, custom agents); Tools allowlist to constrain an agent; Delegate to a background cloud agent that returns a draft PR; Parallel terminals as a scaling model; Ask the agent to write its own skill or instructions
- Tools: GitHub Copilot CLI, Claude Code, Claude Desktop, VS Code, GitHub Copilot cloud agent, GitHub MCP server, Playwright MCP, AGENTS.md, SKILL.md skills, custom agents (.github/agents)

## [Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI](../videos/2IxD9OB3XuQ.md)
`2IxD9OB3XuQ` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: skills-self-improvement, evals, memory

Soheil Feizi (RELAI) argues agents should learn from production failures only through verifiable updates: turn logs into replayable test environments, route fixes to model, harness or memory, and gate each change with regression tests. Second half is a product demo.

- Techniques: Log-to-replayable-environment lift; Instruction-first environment bootstrap; Three-gate fix verification; Layer routing by smallest durable change; Regression-aware optimization; Regression trap in benchmark design; Reviewable change proposal as output
- Tools: RELAI Rely (rely optimize CLI), GEPA, Letta, mem0, LoRA, DPO, GRPO, RLVR, SFT

## [When All Context Matters: Extended Cache Augmented Generation - Luis Romero-Sevilla, Orbis](../videos/XovaGv4f39A.md)
`XovaGv4f39A` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: rag-retrieval, multi-agent, infra-cost-scaling

Luis Romero-Sevilla (Orbis) on Extended Cache Augmented Generation (ECAG): for large, frequently replaced, densely interrelated document collections, split docs across parallel KV-cached context buckets and let a supervisor model interrogate them, instead of RAG or GraphRAG.

- Techniques: Parallel context buckets with a supervisor (ECAG); Dropping topical sharding for bucketing; Caching KV state per context bucket
- Tools: GraphRAG, vector database, KV cache

## [Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS](../videos/uiP88SpCi1Q.md)
`uiP88SpCi1Q` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: token-cost-efficiency, infra-cost-scaling, agent-architecture

An AWS developer advocate lists five ways to cut agent token spend: cache the system prompt, route by task difficulty, offload large tool results, cap tool loops, and trim conversation history, with per-tool observability to check each one.

- Techniques: System prompt and tool caching; Difficulty-based model routing; Tool result offload and summarization; Max-iteration cap on tool loops; Per-tool loop and latency observability; Sliding window history with summarization
- Tools: Strands Agents, Claude Haiku, Claude Sonnet

## [The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents](../videos/spNAUEgq_A8.md)
`spNAUEgq_A8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: multi-agent, agent-architecture, infra-cost-scaling

Justin Schroeder (Standard Agents) argues that small, isolated domain-specific agents composed under a coordinator beat ever-growing context-stuffed general agents on cost, scope, portability and scaling.

- Techniques: Composition of isolated domain agents; Scoped delegation requests; Per-task model routing; Hook-injected runtime facts; Capability scoping per agent; Recursive sub-agent tree
- Tools: Claude, Codex, OpenClaw, Hermes, MCP, Vercel AI SDK, Vercel Eve, Figma, Playwright, Gmail, Google Sheets, Google Workspace

## [Research to Reality: Bringing Frontier ML Research to Production - Vaidas Razgaitis, Higharc](../videos/OXMMN-XbxwA.md)
`OXMMN-XbxwA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: enterprise-adoption, pr-code-review, agent-architecture

Higharc's labs team on moving ML research prototypes into production via three levers: a design-doc-style "research prototype taxonomy," a decoupled Python microservice monorepo, and stacked-PR decomposition for review.

- Techniques: Research prototype taxonomy (RPT) doc; One researcher, one decoupled microservice in a shared monorepo; Slice by dependency graph, then stack PRs; Use the design doc to plan the merge; Notebooks on Modal for GPU experiments
- Tools: Notion, Graphite, GitHub Actions, Modal, Docker, FastAPI, Poetry, uv, Jupyter

## [Frontier results, on device - RL Nabors, Arize](../videos/fWXJM-J0ZB8.md)
`fWXJM-J0ZB8` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: local-ai, inference-serving, evals

Rachel Lee Neighbors shows how to right-size a model: prototype with a frontier model, build a golden eval set, then pick the smallest local model (Llama 3.2 3B) that meets latency and quality targets, closing the gap with prompt changes and deterministic post-processing.

- Techniques: Prototype-big-deploy-small pipeline; Golden dataset with multi-metric eval in Phoenix; Latency budget by percentile; Single-variable prompt ablation; Deterministic post-processing instead of prompt tuning; Auditing the LLM judge; Regression evals in CI
- Tools: Phoenix (Arize), Goose, Gemma 4 E2B, Gemma 3, Llama 3.2 3B, Qwen 2.5 1.5B, Qwen 3 1.7B, Claude Sonnet, Claude Opus, MobileNet, YOLO, MediaPipe

## [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech](../videos/YZQsWVeN3rE.md)
`YZQsWVeN3rE` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: multi-agent, evals, rag-retrieval

Alex Bauer (Upside.tech) on building trust in AI for go-to-market data: manage agents like people, scaffold business context first, use a librarian and a jury-and-judge pattern, and use only tier-two agent harnesses for important work.

- Techniques: Commander's intent prompting; Anchor assets and scaffolding; Citation tracing for verification; Librarian pre-query lookup; Jury and judge; Tiered tool selection
- Tools: Claude, Claude Opus, Slackbot, ChatGPT

## [Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS](../videos/IddXPepIAS4.md)
`IddXPepIAS4` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: coding-agents, testing-verification, mcp-and-tools

Erik Hanchett (AWS) on spec-driven development: write requirements, design and task markdown before code, keep a human reviewer in the loop, and use property-based tests to check the result.

- Techniques: Manual spec loop with any coding assistant; Clarifying questions before requirements; EARS-format requirements; Property tests generated from requirements and design; MVP-first task ordering; Steering docs plus on-demand skills; Pull requirements from PM tools via MCP
- Tools: Kiro, spec-kit, MCP, FastCheck, Mermaid, EARS, Jira, Asana, agents.md, CLAUDE.md

## [WTF Is the Context Layer? The Missing Infrastructure for Production Agents — Prukalpa Sankar](../videos/8G_1-3IO4ZQ.md)
`8G_1-3IO4ZQ` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: memory, skills-self-improvement, enterprise-adoption

Atlan's founder argues production agents fail on missing business context, not model intelligence, and proposes a shared, versioned "context layer" (a company brain) that agents draw from.

- Techniques: Jobs-to-be-done scaling factor for agent selection; Shared context layer as a company brain; Context lifecycle management like software; Trace-driven maintainer loop; Reverse-construct the data stack to bootstrap context
- Tools: Claude Code, Codex, Claude Cowork, Google ADK, Glean, Relevance AI, MCP, Qualified, Artisan

## [Semantic Blindness: 500,000 Sensors Confused an LLM - Raahul Singh & Vanč Levstik, Phaidra](../videos/EUsPvBeIx70.md)
`EUsPvBeIx70` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: rag-retrieval, data-engineering, agent-architecture

Phaidra engineers explain "semantic blindness": why RAG and LLM-only lookups fail on 400K+ equipment names, and how a hierarchy-based planner plus deterministic set-resolver stays accurate with flat cost at data-center scale.

- Techniques: Hierarchy summary as LLM context; LLM emits a structured search plan; deterministic resolver executes it; Pre-indexed subtrees for set operations; Two- or three-step planner/resolver pipeline in place of an agent loop; Pattern-based search for vague queries; Head-to-head eval against the old system at increasing scale; Move deterministic work out of the prompt

## [Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat](../videos/9arM9b7JgOo.md)
`9arM9b7JgOo` · AI Engineer · 2026-07-18 · q2 · intro · workshop · also: coding-agents, multi-agent

Snapchat engineer Jeffrey Lee-Chan demos his personal coding-agent workflow built on OpenClaw: a manager agent with memory delegates work to parallel worktree workers, and separating the manager's context from the workers' reduces overclaiming.

- Techniques: Manager and worker split with a separate-context reviewer; Layered verification with humans last; Context budgeting for the orchestrator; Local, staging, then production flow for agent changes; Cost-tiered model switching
- Tools: OpenClaw, CMUX, Claude Code, Claude Code Teams, Codex 5.3, GPT-5.4, MiniMax, git worktrees, Docker

## [RLM: Recursive Language Models for Large Codebases - Shashi, Superagentic AI](../videos/8oyalrfwgjw.md)
`8oyalrfwgjw` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: coding-agents, agent-architecture

Shashi (Superagentic AI) explains Recursive Language Models (RLM) for large codebases: keep the repo in a REPL, let the model write code to slice it, and call sub-models in a loop. He demos his open-source RLM Code harness with Gemini.

- Techniques: REPL-based context slicing (RLM loop); Recursive sub-calls with a budget; Full trajectory capture as JSONL; Sandboxed REPL execution; Model-agnostic sub-calls
- Tools: RLM Code, DSPy, Gemini, Docker, Codex, Pydantic AI, Google ADK, JSONL trace export

## [Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI](../videos/ZRM_TfEZcIo.md)
`ZRM_TfEZcIo` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: memory, rag-retrieval

Two builders show a file-based personal research system: raw sources, an index.yaml catalog and an LLM-written wiki, queried in tiers and fed by every question. No vector DB needed.

- Techniques: Tiered index-first retrieval; Immutable raw layer with LLM-owned derivatives; Query write-back with a log; Seeded multi-round deep research; Depth knob for research runs; Repo ingestion into per-repo and cross-repo notes
- Tools: Obsidian, Readwise, NotebookLM, Notion, Google Drive, Granola, Claude Code, Codex, Gemini Deep Research, Gemini (grounded Google search), Bright Data, YAML

## [Structuring the Unstructured - Cedric Clyburn, Red Hat](../videos/-x5GEVnkuRw.md)
`-x5GEVnkuRw` · AI Engineer · 2026-07-18 · q3 · practitioner · demo · also: data-engineering, rag-retrieval, mcp-and-tools

Red Hat's Cedric Clyburn demos Docling, an open-source local tool that converts messy PDFs into layout-aware Markdown, JSON, or Pydantic data, plus chunkless RAG over a document outline.

- Techniques: Layout-aware PDF to structured document conversion; Picture enrichment with a local vision-language model; Chunkless agentic RAG over a document outline; Schema-driven extraction from parsed documents; Document conversion as a microservice plus MCP tool; PII removal model before ingestion
- Tools: Docling, docling-serve, Docling MCP server, Pydantic, Ollama, Granite (IBM model), Qwen (via MLX), Jupyter, VS Code, Kubernetes, uvx

## [Browser Agents Don't Need Better Models. They Need Better Eyes. - Kushan Raj, Sarvam AI](../videos/JnubYCYunk8.md)
`JnubYCYunk8` · AI Engineer · 2026-07-18 · q2 · intro · demo · also: voice-multimodal, token-cost-efficiency

Kushan Raj (Sarvam AI) argues browser agents fail because of their infrastructure, not model quality, and shows a compact page representation plus change feedback that makes a cheap model faster and more reliable.

- Techniques: Compact page representation for agents; Delta feedback to the agent; Invest in the environment instead of the model; Expose a browser task as an API
- Tools: browser agent harness (speaker's own, to be open sourced), Claude (used as the baseline in demos)

## [4 Ways to Actually Build Stunning Websites with Claude Code](../videos/HqD5a2Cae60.md)
`HqD5a2Cae60` · AI LABS · 2026-07-02 · q3 · practitioner · tutorial · also: vibe-coding-app-building, claude-code, skills-self-improvement

AI LABS walks through four ways to get better websites and UIs from Claude Code: refresh design skills from model prompting guides, use design.md files, plan functional UIs as HTML mockups, and clone existing UIs. Mostly anecdotal, with a sponsor segment.

- Techniques: Refresh a design skill from the model's prompting guide; Mine older prompting guides for dropped fixes; Set effort by task type; Conditionally load a sub-skill from a rule; Apply design.md after generation for marketing pages; Functional UI pipeline: plan, mockups, gallery, port; Consistent variants via a shared design.md; CLAUDE.md as product context and verify contract; Verify with a sub-agent against design.md; Clone a marketing site with a capture CLI and sitemap; Clone an auth-gated app from screenshots
- Tools: Claude Code, Claude, Fable 5, Opus 4.8, Anthropic front-end design skill, design.md, GetDesign.md, GSAP, Single File CLI (as named in the video), sitemap.xml, HTML, CLAUDE.md

## [Use This To Make The Hermes Agent Basically Free](../videos/5d02TYoOzfE.md)
`5d02TYoOzfE` · AI LABS · 2026-07-02 · q2 · practitioner · tutorial · also: token-cost-efficiency, agent-architecture, coding-agents

Hermes Agent cost-reduction tutorial from AI LABS: where the tokens go, and which model, context, tool, and hard-limit settings cut the bill without hurting output.

- Techniques: Audit token spend before tuning; Route auxiliary and sub-agent work to a cheaper model; Use the OpenRouter Pareto router; Match effort level to task, and turn thinking off for simple work; Compress context early with a lower threshold and target ratio; Cap tool output in context; Use ephemeral system prompts for one-session instructions; Keep knowledge in files the agent loads on demand; Undo the last message and re-prompt with the failure described; Trim tools, skills, and MCP servers to what is used; Set hard limits on output, turns, and loops
- Tools: Hermes Agent, OpenRouter, Pareto router (OpenRouter), OpenAI Codex subscription, OpenAI subscription, Claude Code, Anthropic API, Gemini, MCP servers, Slack, Luma (sponsor), config.yaml

## [Headroom: The Netflix Tool That Makes AI Agents 10x Cheaper](../videos/KqdRWE1en8k.md)
`KqdRWE1en8k` · Better Stack · 2026-07-02 · q3 · practitioner · review · also: token-cost-efficiency, claude-code

Walkthrough of Headroom, an open-source proxy that compresses tool-call output, code and RAG text before it reaches the LLM, with reversible retrieval via hashes. The demo shows 98% savings on one log read, with honest caveats about round trips and low effort.

- Techniques: Run Headroom as a local proxy in front of the model API; Compress tool results explicitly from the Python SDK; Check savings through the proxy stats endpoint; Pair input compression with output brevity; Use Headroom Learn to tune compression from failed sessions
- Tools: Headroom (proxy plus Python and TypeScript SDKs), CompressBase (local plain-text compression model used by Headroom), Claude Code, Claude Agent/SDK (Python), uv, Python 3.12, Rust (proxy internals), jq, Caveman (prompt-based output brevity, covered in another video by a different presenter), Opus (Claude model used in the Claude Code demo), Codex (cross-agent memory feature mentioned), Headroom Learn (feature)

## [PAI: The Life OS for AI-Powered Development](../videos/JukZ7WWtOSg.md)
`JukZ7WWtOSg` · Better Stack · 2026-07-02 · q3 · intro · review · also: claude-code, memory, skills-self-improvement

Better Stack reviews PAI (Personal AI Infrastructure), a memory-and-skills operating layer on Claude Code. Its value is cross-session continuity; it needs terminal comfort and ongoing upkeep.

- Techniques: Persistent project memory loaded every session; Planning prompt that requires risks, assumptions and verification; One custom skill per role or review type; Fixed action order through a multi-step process
- Tools: Claude Code, PAI (Personal AI Infrastructure), Pulse (PAI local dashboard), Telos (PAI goals/ideal-state file, as named in the video), Fabric (named as a prior project of the PAI creator), SecLists (spelled 'SecList' in captions; named as a prior project of the PAI creator), LangChain (compared against), CrewAI (compared against), Next.js (example skill domain)

## [19 Hidden Features To Unlock The True Potential Of Your Hermes Agent Setup](../videos/nN6DZi_fiSo.md)
`nN6DZi_fiSo` · AI LABS · 2026-07-02 · q2 · practitioner · tutorial · also: agent-architecture, token-cost-efficiency, multi-agent

AI LABS walks through about 19 Hermes agent config settings (context limits, compression, sub-agents, auxiliary models, quick commands, checkpoints, YOLO, isolation mode) that they changed to fix workflow problems, with defaults and new values.

- Techniques: Per-profile config tuning; Compression threshold and tail tuning; Sub-agent concurrency, depth and permission settings; Cheap auxiliary models and effort control; Exec and alias quick commands; File checkpoints and rollback; Ephemeral system-prompt variable; Isolation mode for config debugging
- Tools: Hermes (agent, config.yaml, Hermes config / auth / personality / rollback commands), Claude Code (compared; dangerously-skip-permissions mode compared to YOLO), Codex (compared; compression threshold comparison), OpenRouter (provider; default auxiliary model fallback), Gemini Flash (auxiliary model used in their setup), Opus (main model example), Gemini (1M-token window model mentioned), Slack (used to coordinate the team via Hermes), Notion, Jira, Airtable (integrations named in the sponsor segment), Helix (sponsor, not evaluated)

## [Why I Quit My Dev Job Before AI Could Take It | Better Stack Podcast Ep. 16](../videos/VuMf2ZVA0RE.md)
`VuMf2ZVA0RE` · Better Stack · 2026-07-02 · q3 · practitioner · interview · also: coding-agents, claude-code, dev-tools

Better Stack podcast with Dreams of Code's Elliot on leaving dev work, betting on Rust, and practical AI-coding habits: stub-first interfaces, git-staged checkpoints, human-steered architecture.

- Techniques: Stub-first public interface; Hand-built spike before delegating; Git staging as manual checkpoints; Architecture-owner, typing-delegate split; Codec backend abstraction
- Tools: Claude Code, Codex CLI, Cursor, OpenCode, Bun, Zig 0.16, Rust, GPUI, gpui-component, Iced, egui, Tauri

## [MemPalace: The Tool That Makes Claude Stop Forgetting](../videos/kRACHOx1p8s.md)
`kRACHOx1p8s` · Better Stack · 2026-07-02 · q3 · practitioner · review · also: memory, claude-code, mcp-and-tools

Better Stack demos MemPalace, a local tool that stores coding-agent conversations verbatim and exposes them to Claude Code over MCP so decisions persist across sessions.

- Techniques: Verbatim store plus compact index; Local project memory setup; Claude Code plugin with a memory protocol; Run alongside context mode; Load pointers instead of project lore; Install hygiene for memory tools
- Tools: MemPalace (mempalace; spoken as Mem Palace; version not stated), uv, pip, ChromaDB, SQLite, MCP (Model Context Protocol), Claude Code (captioned as Cloud Code), Claude Code hooks and plugin, context mode, Memzero, Zapp (transcript spelling; product name unverified)

## [Google Replaced The Karpathy's LLM Wiki](../videos/k4sMSsMzX2g.md)
`k4sMSsMzX2g` · AI LABS · 2026-07-02 · q2 · practitioner · review · also: memory, rag-retrieval, claude-code

AI LABS walks through Google's Open Knowledge Format (OKF), a folder, index.md and YAML-frontmatter convention for markdown knowledge bases, and reports a small team test with lower token use and faster lookups.

- Techniques: Index.md per folder as the agent's entry point; YAML frontmatter with name, description and type on every concept document; Script-first markdown-to-OKF conversion with evals; CLAUDE.md navigation section that documents the bundle; Trial on a Git branch and visualize the bundle
- Tools: Open Knowledge Format (OKF, Google), BigQuery, Claude Code, CLAUDE.md, Obsidian (comparison only), Git / GitHub, Karpathy LLM-wiki pattern (concept, not a product), Google design.md standard (named in passing), Mobbin MCP (sponsor), Cursor, Lovable, v0 (named in sponsor segment), Markdown to OKF skill (the team's own, unnamed script)

## [Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS](../videos/iUWwcG-C8OU.md)
`iUWwcG-C8OU` · AI Engineer · 2026-06-18 · q4 · practitioner · demo · also: data-engineering, agent-architecture, enterprise-adoption

WorkOS product lead Garrett Galow demos Studio, an internal agent that answers business questions and turns repeat questions into live widgets. Main lessons: pre-flight checks, runtime tool context, query validation, and keeping the LLM out of widget refresh.

- Techniques: Generated declarative widgets; Pre-flight checks and clarifying questions; Runtime tool-context injection; Layered prompts; Distrust model priors for product facts; Execute-and-validate before deploy; Org-level connectors with role-based defaults
- Tools: Snowflake, Linear, Notion, Convex, LangGraph, Claude Opus, Slack bot, Retool, WorkOS Pipes

## [Context Graphs for Explainable, Decision-Aware AI Agents — Andreas Kollegger & Zaid Zaim, Neo4j](../videos/abvQEhvRI_c.md)
`abvQEhvRI_c` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: memory, agent-architecture, rag-retrieval

Neo4j speakers argue agents need context graphs that store policies and rules as well as facts, so they can make and record decisions. They give a decision framework: frame, check global rules, assess risk, propose, then act, defer or escalate.

- Techniques: Propose, then decide, as two agents; Pre-decision risk screen; Decision log as a graph of precedent; Tiered memory in one graph; Framework as a skill or graph workflow
- Tools: Neo4j, Text2Cypher, LangGraph, ADK

## [Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind](../videos/3_gYbhABcAE.md)
`3_gYbhABcAE` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: agent-architecture, evals, mcp-and-tools

Philipp Schmid (Google DeepMind) lists five habits from deterministic software that break when building agents: text as state, handing control to the LLM, errors as inputs, pass-rate evals, and agent-ready tools.

- Techniques: Goal-first dispatcher prompting; Free-text approval with edits; Preferences as natural language in context; Errors as observations; Repeated-run pass-rate evals with judges; Agent-ready tool definitions
- Tools: Gemini API, Gemini

## [Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind](../videos/BcWFc3H7Khg.md)
`BcWFc3H7Khg` · AI Engineer · 2026-06-18 · q3 · practitioner · workshop · also: voice-multimodal, models-research

Live workshop from Google DeepMind's Guillaume Vernade building an illustrated children's book with Gemini, Nano Banana, Veo, Lyria and TTS, plus API tips on retries, service tiers and stateful chats.

- Techniques: Retry wrapper around the media client; Service tier choice per request; Iterate cheap, then upscale; Structured output as a scene manifest; Style and composition system instructions; Streamed Lyria output; Lyria RealTime as a live, steerable stream
- Tools: Gemini API, Vertex AI, Google AI Studio, Google GenAI SDK, Google Colab, Nano Banana 2, Veo 3.1 and Veo 3.1 Lite, Lyria 3 clip and full-song models, Lyria RealTime, Gemini TTS, Interactions API, Gutenberg (source book)

## [Fast Models Need Slow Developers — Sarah Chieng, Cerebras](../videos/TeGsFFNqRLA.md)
`TeGsFFNqRLA` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: coding-agents, inference-serving, testing-verification

Cerebras's Sarah Chieng argues that fast coding models (Codex Spark, ~1,200 tok/s) demand new habits: plan with a large model, execute with a fast one, verify every step, and keep context in bounded goals.

- Techniques: Planner-executor model split; Session-to-skill distillation; Per-step automatic verification; Parallel variant generation with cherry-picking; Scoped steering constraints; Automatic refactor pass after each task; Bounded goals with a context budget; Four-file external memory (AGENTS/PLAN/PROGRESS/VERIFY)
- Tools: Codex Spark, Codex, GPT-5.4, GPT-5.3 Codex, Sonnet, Opus, REAP (router-weighted expert activation pruning)

## [Personalization in the Era of LLMs - Shivam Verma, Spotify](../videos/5YSJEP0HWzM.md)
`5YSJEP0HWzM` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: training-finetuning-rl, enterprise-adoption

Spotify's AI Foundation tech lead explains how it personalizes recommendations with user embeddings, semantic IDs for catalog items, and soft user tokens fed into a fine-tuned open-weight LLM.

- Techniques: Semantic ID tokenization of item embeddings; Soft user token injection; Tokenized listening-history prompting for domain adaptation; Daily batch user-embedding generation; User-editable text profile as a steering signal
- Tools: Llama, Qwen

## [Cooking with Agents in VS Code — Liam Hampton, Microsoft](../videos/dyHpnnlkTc8.md)
`dyHpnnlkTc8` · AI Engineer · 2026-06-18 · q2 · intro · demo · also: coding-agents, multi-agent, sandboxing-execution

A Microsoft product tour of running local, background (worktree) and cloud coding agents side by side in VS Code, with advice on which mode fits which task.

- Techniques: Worktree-per-background-agent; Route tasks by hands-on level; Plan first, autopilot second, pause before PR; Task-specific custom agents; Cloud agent with MCP and browser testing
- Tools: GitHub Copilot, VS Code, GitHub Copilot CLI, Git worktree, GitHub Actions, GitHub MCP server, Playwright MCP server, Microsoft Learn MCP server, awesome-copilot (open-source repo of agent customizations), Claude Opus 4.6 (used for the local agent)

## [RAG is dead, right?? — Kuba Rogut, Turbopuffer](../videos/UM6sFg_jdlE.md)
`UM6sFg_jdlE` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: rag-retrieval, coding-agents, infra-cost-scaling

Kuba Rogut (Turbopuffer) argues that "RAG is dead" misreads the problem: retrieval should be a toolbox (vector, BM25, grep, filters) used in iterative agent loops, and embeddings work best as precomputed cache compute.

- Techniques: Multi-modal retrieval toolbox for agents; Iterative search-read-assess loop; Index once, query at runtime; Merkle-tree index reuse across near-identical corpora; Staged narrowing before the context window
- Tools: Claude Code, Codex, Cursor, Turbopuffer, BM25, Merkle trees

## [What the Best Agents Share — Mardu Swanepoel, Flinn AI](../videos/7CrPrHgoEYk.md)
`7CrPrHgoEYk` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: product-ux, coding-agents

Mardu Swanepoel (Flinn AI) on four UX patterns shared by strong agents: focus modes, transparent execution, personalization, and reversibility, illustrated with Cursor, Claude Cowork, Harvey and Manus.

- Techniques: Mode-scoped agent configuration; Plan-only mode; Hypothesis-driven debug mode; Visible execution trace; Playbook and memory personalization; Layered undo; Native host integration for review
- Tools: Cursor, Claude Cowork, Claude skills and connectors, Manus, Harvey, Microsoft Word API

## [Bounded Autonomy: Between Free Will and Determinism — Angus J. McLean, Oliver](../videos/t4359sKBu4w.md)
`t4359sKBu4w` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: agent-architecture, enterprise-adoption

An ad-agency AI director argues for "bounded autonomy": treat LLM context as a soft constraint, keep systems simple, store knowledge in several representations, and never automate work you cannot do yourself.

- Techniques: Self-imposed context budget; Curated documentation over open web access; Simple-first prototype with fast reality checks; Multi-representation knowledge storage; Cluster-then-report pipeline; Teach yourself on older, smaller models and your own harness; Automate only what you can do yourself

## [Stop babysitting your agents... — Brandon Waselnuk, Unblocked](../videos/BiG2ssibKGc.md)
`BiG2ssibKGc` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: memory, rag-retrieval

Unblocked's Brandon Waselnuk argues agents need a runtime context engine, not more MCP access or static docs: exhaustive retrieval, surfaced conflicts, a social graph, and hard-won lessons.

- Techniques: Exhaustive retrieval before first-hit answers; Research packet before planning; Expert / social graph built from the code repo; Surface conflicts instead of silently picking; Permission-preserving delivery over MCP; Confidence-gated auto-answering; No answer caching for latency
- Tools: Claude Code, MCP, Codex, Anthropic API, AWS Bedrock, CLAUDE.md, AGENTS.md, Zendesk, Slack, Microsoft Teams

## [Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo](../videos/EcqMYoIV57A.md)
`EcqMYoIV57A` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: multi-agent, pr-code-review

Qodo's Nupur Sharma argues that dumping more context into an agent makes results worse, and shows how selecting, splitting and judging context across specialist agents fixed this in their PR review system.

- Techniques: Context selection instead of context dumping; Iterative retrieval with a library-card index; Hierarchical summarization; Knowledge graph for dependencies; 80/20 research and gate split; Specialist agents with a judge agent; Feedback-weighted calibration
- Tools: Jira, MCP, Claude Opus

## [BDD, ADR, PRD, WTF: Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence](../videos/504PvfXou5Y.md)
`504PvfXou5Y` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: testing-verification, pr-code-review

Michal Cichra on keeping agents and humans aligned by storing ADRs, PRDs and executable BDD specs in the repo, then enforcing them through git hooks, CI and import-boundary lints.

- Techniques: ADR with enforcing lint rule; Import-boundary restriction to eliminate bug classes; Executable BDD scenarios linked to PRDs; Shared checks in git hooks and CI; Design system as enforced rules and previews; Scoped test selection per task
- Tools: Cucumber, git hooks, CI, linters, type checkers, architecture import lint, Markdown docs

## [Why your agents need decision traces, not just documents — Zach Blumenfeld, Neo4j](../videos/B9h9ovW5H9U.md)
`B9h9ovW5H9U` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: memory, rag-retrieval, data-engineering

Neo4j's Zach Blumenfeld on context graphs: why agents need stored decision traces and precedents, not just documents, plus a one-line scaffold (create-context-graph) and the Neo4j agent memory pipeline.

- Techniques: Hybrid precedent retrieval over decision traces; Scaffold a context-graph app from a domain; Staged entity extraction from text into a graph; Ontology-first graph schema generation; Separate memory stores by kind
- Tools: Neo4j, Neo4j agent memory package, Graph Data Science (GDS), Cypher, uvx create-context-graph, Pydantic AI, Claude, OpenAI embeddings, Next.js, spaCy, GLiNER, MCP

## [Don't Build Slop (4 Levels of AI Agent Maturity) - Ara Khan, Cline](../videos/yUmS-F9IX90.md)
`yUmS-F9IX90` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: agent-architecture, coding-agents, software-factory

Ara Khan (Cline) argues for four maturity levels of agent building: framework, hand-built state machine, Kanban as the UX, and cloud execution. Core warnings: keep prompts minimal, keep agents CLI-testable, and keep architecture human-owned.

- Techniques: Agent as explicit state machine; Prune the system prompt on every change; CLI-first agent interface for agent-driven development; Exact reasoning-trace round-tripping; Kanban board as the multi-agent control surface; Per-task cloud agent dispatch; Human-owned architecture before code generation
- Tools: Claude Code, Codex, Cursor, Factory, Cline, LangChain, LangGraph, OpenRouter, Linear, AGENTS.md, VS Code

## [Terax: One Developer Built an AI Terminal Better Than Warp](../videos/3L8htHUzAI4.md)
`3L8htHUzAI4` · Better Stack · 2026-06-02 · q3 · intro · review · also: dev-tools, coding-agents

Review of Terax, a small open-source AI terminal and code editor built with Tauri 2 and Rust, compared against Warp and CMUX; the reviewer keeps Warp and Neovim for daily work.

- Techniques: Lean desktop shell for a terminal-plus-agent app; Read-only plan mode, then build mode, for agent edits; Generate a project context file with init, then review it as a diff; Hide sensitive tabs from the agent with a privacy page; Keep API keys in the OS keyring
- Tools: Terax, Tauri 2, Rust, React, Electron (comparison), Xterm.js (WebGPU renderer), CodeMirror 6, Vercel AI SDK, Warp, CMUX, Helix, Neovim

## [It’s Broken… The Codex vs Claude Code Debate Is Finally Over](../videos/8ImlAQOyVTs.md)
`8ImlAQOyVTs` · AI LABS · 2026-06-02 · q3 · practitioner · review · also: coding-agents, claude-code, multi-agent

A single-author head-to-head of Claude Code (Opus 4.7) vs Codex CLI (GPT 5.5) across usability, planning, greenfield builds, context, memory and sub-agents; Codex wins on cost and autonomy, Claude on UX, hooks and ecosystem.

- Techniques: Count tokens per session from the CLI's session files; Set a Codex personality to reduce sycophancy; Use Claude Code's expanded thinking to course-correct; Use Codex's attempt flag for best-of-n; Keep AGENTS.md or CLAUDE.md lean; Design sub-agents for isolation or inheritance deliberately
- Tools: Claude Code, Codex CLI, Opus 4.7, GPT 5.5, FastAPI, Flask, Next.js, ShadCN UI, Gemini API, Claude desktop app, Codex web app, Stream Vision Agents

## [This Is The Greatest Shift In Codex CLI And Claude Code](../videos/B44bXmzU60s.md)
`B44bXmzU60s` · AI LABS · 2026-06-02 · q2 · practitioner · review · also: mcp-and-tools, claude-code

Walkthrough of Mirage, a virtual file system that mounts Gmail, Drive, Slack and similar services as folders so Claude Code can read them with bash instead of MCP tool calls. Partly sponsored, with a hype title.

- Techniques: Mount a SaaS service as a folder; Run the mount as a long-lived process; Start the agent inside the mounted workspace; Chain bash commands across services instead of MCP calls; Read attachments as files; Preserve a session across restarts; Wrap any API as a file system; macOS FUSE prerequisite
- Tools: Mirage (virtual file system for agents, cloned from source), Claude Code, MCP (Model Context Protocol), Gmail MCP, Google Drive MCP, Google Chat, Slack, Notion, Telegram, Figma (mentioned as a possible target), Claude Design (mentioned in passing, unverified), Google Cloud Console

## [Vercel made a programming language](../videos/Koop0_nkNtc.md)
`Koop0_nkNtc` · Better Stack · 2026-06-02 · q3 · practitioner · review · also: dev-tools, coding-agents

Better Stack walkthrough of Xero, a new systems language whose toolchain emits JSON diagnostics with fix guidance so agents can repair code. A Claude fix run succeeded without docs, but the presenter doubts a new language was needed.

- Techniques: Self-describing toolchain for agents; Zero-context fix-loop test; Explicit capability marking for IO; Error propagation with raises and check; Scoped cleanup with owned values, drop and defer; Running a Xero program
- Tools: Xero (systems language and toolchain, named as 'Xero' or 'zero' in the transcript), Claude (Claude Code, used for the fix run), Rust, Zig, Go, jq, Bun (mentioned only as a possible future rewrite target), WebAssembly (compile target)

## [I Didn't Know You Could Use Claude Code Like This](../videos/KQDVDtklf34.md)
`KQDVDtklf34` · AI LABS · 2026-06-02 · q2 · intro · tutorial · also: claude-code, vibe-coding-app-building

Shows non-coding uses of Claude Code (second brain in Obsidian, Remotion video, grounded research pipeline, Canvas design skill, Claude Video watch skill, NotebookLM/Notion ops, role-based finance/teacher/legal setups) mostly as sponsored, shallow tutorials.

- Techniques: CLAUDE.md priority-tiered instructions for a non-code knowledge base; Remotion skill install and plan-first video generation; Step-file research pipeline with verification and cited output; Claude Video skill setup for watching videos; Canvas design skill workflow for posters and infographics; Local Claude Code over NotebookLM CLI and Notion MCP for content systems
- Tools: Claude Code, Claude.md, Obsidian, Remotion, Remotion skill, Anthropic Canvas design skill, Claude Video (watch skill), Groq, SERP API, Google Gemini, NotebookLM CLI, Notion MCP

## [ADLC: Claude Code's New Lifecycle for AI Coding](../videos/aMBQB_IJ0dQ.md)
`aMBQB_IJ0dQ` · AI LABS · 2026-06-02 · q2 · intro · other · also: agent-architecture, evals, claude-code

Conceptual walkthrough of the agentic development lifecycle (ADLC), a phase-by-phase SDLC analogue for non-deterministic agents with a validation gate and staged rollout. Thin on code and data, with a sponsor segment.

- Techniques: Behavior-first planning mode; Human-agent responsibility model; Ground-truth dataset plus baselines as a validation gate; Single orchestration layer for multiple agents; Context hygiene against context rot; Staged rollout with behavioral alerting; Feedback signals and periodic data refresh
- Tools: Claude Code (planning mode, agent view), Cursor, Google Calendar MCP, Gmail MCP, Notion MCP, RAGAS, DeepEval, Gemini (1M-token context, mentioned), Claude Opus (1M-token context, mentioned), ChatGPT (feedback UI example, mentioned), Softr (sponsor, transcribed as 'Softer')

## [Impeccable Makes Claude Build Sites That Don't Look Like AI](../videos/Ln11hm7jieM.md)
`Ln11hm7jieM` · Better Stack · 2026-06-02 · q3 · intro · review · also: coding-agents, token-cost-efficiency

Better Stack walks through Impeccable, a design-quality skill/toolchain that steers AI coding agents away from generic-looking sites, builds a homepage with it, and concludes it suits people who want good-looking output without deep design control, and that Claude Code is token-expensive for it.

- Techniques: Staged design workflow with persistent design MD files; Forcing an image-model probe step when the harness has no image generation; Browser-driven live iteration with impeccable live; Run document after the visual pass
- Tools: Impeccable (design-quality toolchain / agent skill, installed via skills.sh), Claude Code, Astro, Tailwind CSS, GPT Image 2 (OpenAI image model, used for probes), OpenAI API key via shell environment, Codex CLI, Codex GUI, Pencil (design tool, mentioned as the precise alternative; earlier Better Stack video), Superpowers (Claude plugin, mentioned for comparison), jQuery UI (creator's earlier project, mentioned)

## [The Greatest AI Coding System I've Ever Used, Forget Codex Vs Claude Code](../videos/q7Am0pV6FjQ.md)
`q7Am0pV6FjQ` · AI LABS · 2026-06-02 · q3 · practitioner · review · also: claude-code, multi-agent, agent-architecture

Goal Buddy, an open-source plugin for Claude Code and Codex, wraps the native goal command with file-based state, an upfront "oracle" for done, and Scout/Worker/Judge agent roles.

- Techniques: Oracle-first done criteria; Role-separated agents with access limits; File-based run state instead of chat history; Slice contracts; Clarify before looping; Install and start a run
- Tools: Goal Buddy, Claude Code (goal command, resume command), Codex, Ralph Wiggum plugin, Haiku (native goal evaluator)

## [This AI Tool Maps Any Codebase Before You Touch It (Understand-Anything)](../videos/VmIUXVlt7_I.md)
`VmIUXVlt7_I` · Better Stack · 2026-06-02 · q3 · practitioner · review · also: claude-code, dev-tools

Walkthrough of Understand-Anything, a Claude Code plugin that builds an interactive knowledge graph of a repo for onboarding and pre-change impact checks; the speaker also flags its heavy token cost.

- Techniques: Install and run Understand-Anything in Claude Code; Onboarding order: map, then tour, then questions; Use the graph as agent context; Pre-refactor impact check
- Tools: Understand-Anything (open-source Claude Code plugin, MIT license), Claude Code, Claude Max (subscription plan referenced for rate usage), Cursor, GitHub Copilot, Gemini CLI, Google microservices sample repo (demo target)

## [3 Design Levels For a Free Claude Code Boost (People Stop At Level 1)](../videos/5lycYTOYbPM.md)
`5lycYTOYbPM` · AI LABS · 2026-06-02 · q3 · practitioner · tutorial · also: claude-code, testing-verification, vibe-coding-app-building

Three levels of getting non-generic UI from Claude Code: a structured single-page design prompt, a CLAUDE.md plus design.md system for cross-page consistency, and design tests written before the code, including visual TDD with Visly.

- Techniques: Structured single-page design prompt; CLAUDE.md for project context, design.md for the visual system; Lint design.md against Google's open template; Install an external design-principles audit skill per project; Derive design tests from design.md before writing UI code; Visly local visual TDD loop
- Tools: Claude Code, Claude Opus 4.7 (model named in the video), CLAUDE.md, design.md, OKLCH, Google design.md template (open-sourced), Versalab design-audit skill, Playwright, Visly CLI (transcribed as 'Visly Test' and 'Visley'), Zilliz Cloud (sponsor), Inter (named as banned font), Geist (named as banned font)

## [Claude Code Just Killed Every Shopify Agency Ever](../videos/x2pRavsHdls.md)
`x2pRavsHdls` · AI LABS · 2026-06-02 · q2 · practitioner · tutorial · also: coding-agents, claude-code, vibe-coding-app-building

A walkthrough for building and syncing a Shopify storefront with Claude Code, using the Shopify CLI, AI toolkit MCP, HTML prototype skill, Gemini image skill and settings.json hooks. Quality is capped by a sponsor segment and a thin, hype-titled setup guide.

- Techniques: Two-phase skill: HTML preview, then apply; Image generation through a CLI skill; Pre-tool-use hook as an approval gate; Shopify project bootstrap; Admin API auth with incremental scopes
- Tools: Shopify Partner account, Shopify CLI (React app template, TypeScript), Shopify AI toolkit (MCP), Shopify plugin (agents and skills), Shopify Admin API, Claude Code, CLAUDE.md, Gemini CLI (image generation), settings.json hooks, Willow Voice (sponsor segment, not a tool used in the setup)

## [Anthropic Just Revealed The Best Claude Code Setup](../videos/lGalJmyI78w.md)
`lGalJmyI78w` · AI LABS · 2026-06-02 · q2 · practitioner · tutorial · also: claude-code, multi-agent, mcp-and-tools

Practitioner checklist for setting up Claude Code harnesses on large codebases: layered CLAUDE.md, hooks, path-scoped skills, plugins, LSP, MCP, sub-agents, and periodic pruning.

- Techniques: Layered CLAUDE.md; Stop-hook learning loop; Hooks for enforcement; Path-scoped skills; Team plugin distribution; LSP before code; Custom sub-agents with an overridden Explore agent; Per-subdirectory tests and codebase map; Quarterly harness pruning with ignore files
- Tools: Claude Code, Codex, Gemini CLI, superpowers, CLAUDE.md, Claude Code hooks (SessionStart, PreToolUse, Stop, exit-code-2), skill-creator, Claude Code plugins and plugin marketplace, LSP (Language Server Protocol), MCP (Model Context Protocol), Explore sub-agent (built-in, overridable), .gitignore

## [This Is Insane... This Just Ended The Google Stitch VS Claude Design Debate](../videos/PJ9CmTODmVo.md)
`PJ9CmTODmVo` · AI LABS · 2026-06-02 · q2 · intro · review · also: product-ux, mcp-and-tools, coding-agents

Hands-on head-to-head of Claude Design and Google Stitch across features, limits, design quality, animation, iteration and handoff; each tool wins different categories.

- Techniques: Batch design comments before sending; Import a design system from a URL; Portable design.md design system; Coding agent drives the design tool through MCP; Generate the design system before the screens
- Tools: Claude Design, Claude Opus 4.7, Google Stitch, Gemini 3, Nano Banana, Claude Code, Figma, Google AI Studio, Firebase, GitHub, design.md

## [Your AI UI Looks Generic… This Fixes It (DESIGN.md)](../videos/pY52H5gKhGg.md)
`pY52H5gKhGg` · Better Stack · 2026-06-02 · q2 · intro · review · also: vibe-coding-app-building, coding-agents

Google's open-sourced DESIGN.md: a repo-root markdown file of design tokens plus intent prose that keeps AI-generated UI from looking generic. Practical but thin.

- Techniques: Repo-root DESIGN.md with tokens then intent; Fixed-prompt A/B for design context; Start from a community template, then customize; Write the design rules once, not in every prompt
- Tools: DESIGN.md (Google open-source format), Cursor, Claude Code (transcribed as 'Cloud Code'), v0, Figma, CLAUDE.md, Cursor rules, Tailwind (default styling referenced in demo)

## [How we solved Context Management in Agents — Sally-Ann Delucia](../videos/esY99nYXxR4.md)
`esY99nYXxR4` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: memory, multi-agent, evals

Arize's product head explains how their Alex agent escaped a context-growth loop: head/tail truncation with the middle moved to memory, long-session evals, and sub-agents for heavy data search.

- Techniques: Head + tail truncation with middle spill to memory; Reference-by-ID retrieval tool; Long-session eval (seed N turns, test turn N+1); Sub-agent for data-heavy search
- Tools: Alex (Arize's in-product agent), Arize observability platform, Claude Code (referenced, not used by speaker)

## [Vibe Engineering Effect Apps — Michael Arnaldi, Effectful](../videos/Wmp2Tku2PrI.md)
`Wmp2Tku2PrI` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: coding-agents, testing-verification, agent-architecture

Michael Arnaldi builds a TypeScript Effect HTTP to-do API from an empty repo, arguing agents need the real source repo, strict lint back pressure, and generated pattern docs.

- Techniques: Clone the library source into the repo; Strict diagnostics plus lint as back pressure; AGENTS.md as a living rulebook; Spec file plus Ralph-style loop; Self-selected pattern docs; Single execute tool instead of many tools; Per-test rollback transactions for DB tests; Test layers with it.layer; Lint reference checks in CI for pattern docs
- Tools: Effect v4 (beta), Effect SQL with SQLite, Bun, Vitest, TypeScript native preview (tsgo), ESLint, OpenCode, GPT-5.4, Claude Opus, Codex, Cursor, Temporal

## [Human-in-the-Loop Automation with n8n — Liam McGarrigle](../videos/tDArkCqjA-c.md)
`tDArkCqjA-c` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: security-guardrails, agent-architecture, mcp-and-tools

Workshop on building a Gmail and Google Calendar agent in n8n, then gating sensitive tool calls behind human approval steps that the model cannot skip.

- Techniques: Approval gate in front of sensitive tools; Free-text decline as feedback; Dry runs with dummy data before real accounts; Rules in tool descriptions, not one system prompt; Per-field descriptions for argument mistakes; Wait with an auto-deny timeout; Confirm sub-workflow as a tool; Sub-agent per domain as a tool; Date and time injection via expression; Memory window sizing
- Tools: n8n, OpenRouter, Gmail, Google Calendar, Slack, Notion, Postgres, Redis, Claude, Claude Code, Luxon, Swagger

## [Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take](../videos/FlzpEGHNVKQ.md)
`FlzpEGHNVKQ` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: evals, mcp-and-tools

How a consumer chess app grounds LLM game commentary in Stockfish and detectors, hits a sub-3s latency target, and closes a feedback loop where a Claude Code agent triages bad comments and opens PRs.

- Techniques: Deterministic analysis then LLM narration; Scenario-based LLM-as-judge regression set; Channel-injected events into a running coding agent; Latency-first model selection for interactive output; Iterative context pruning
- Tools: Stockfish, Maia (human-move prediction model), Gemini 3 Flash, Claude Code, Claude Code Channels, GPT-5 Mini, OpenRouter, Slack, GitHub

## [Agents Don't Do Standups: Building the Post-Engineer Engineering Org — Mike Spitz, PFF](../videos/VMemhtlsoNk.md)
`VMemhtlsoNk` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: software-factory, enterprise-adoption, testing-verification

Mike Spitz (PFF) reports a Jan–Mar 2026 case study where agent-driven spec, design doc, ticket and PR flow cut delivery time and dropped Scrum for a 20-engineer team.

- Techniques: Agent-interviewed spec then skill-generated LDD; Auto-generated, non-blocking tickets and PR-driven status; Agent code review limited to opinion-level nits; Post-staging QA agent against acceptance criteria; Composable per-step skills for the delivery lifecycle; Customer survey as the primary retro signal; Phased, non-critical-first rollout
- Tools: Claude Code, Claude Opus, Codex

## [Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser](../videos/pFsfax19yOM.md)
`pFsfax19yOM` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: skills-self-improvement, claude-code, evals

Hands-on WorkOS workshop on writing Claude skills: description-based routing, constraints over prose, progressive disclosure, confidence gates, with-and-without-skill evals, and sharing skills.

- Techniques: Description-as-router; Constraints over prescription; Bang-backtick command injection; Progressive disclosure via reference map; Subagent for verbose checks; Confidence-gated clarification; With-and-without-skill eval; Transcript-driven skill refinement; Looped connector poll
- Tools: Claude Code, Codex, Cursor, Pi, OpenClaw, Claude Desktop, Claude Agent SDK, WorkOS CLI, Obsidian, Linear, Slack connector, Remotion

## [Combine Skills and MCP to Close the Context Gap — Pedro Rodrigues, Supabase](../videos/JT3OzDKrucU.md)
`JT3OzDKrucU` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: skills-self-improvement, mcp-and-tools, evals

Pedro Rodrigues (Supabase) on writing a product skill for agents, using a three-condition eval to show skills plus MCP beat MCP alone. Main lesson: agents need guidance, not more context.

- Techniques: Three-condition skill eval; Inline must-not-miss rules; Skill as pointer to live docs; Dev-first schema workflow with a deferred migration; Start minimal and iterate
- Tools: Supabase, Supabase advisor, Braintrust, Claude Code, Codex, Vercel skills package, MCP, SSH, Postgres

## [Agentic Search for Context Engineering — Leonie Monigatti, Elastic](../videos/ynJyIKwjonM.md)
`ynJyIKwjonM` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: rag-retrieval, mcp-and-tools, skills-self-improvement

Leonie Monigatti (Elastic) argues context engineering is mostly agentic search, then walks through live demos of semantic search, ES|QL query tools, skill loading, and grep-style shell search, and when to use each.

- Techniques: Layered tool descriptions; Errors returned to the agent; Progressive disclosure for skills; Outsource aggregation to the search engine; Shell tool with semantic grep; Hybrid shell plus database verification; Log tool calls to find where specialization is needed; Use the file store as memory and offload old results
- Tools: LangChain, Elasticsearch, ES|QL, Jina embeddings v5, Jina grep (captioned as Gina grep), OpenAI GPT-5.4 nano and mini, shell / bash tool, Claude Code, OpenClaw (captioned as OpenCloud, exec tool)

## [MCP = Mega Context Problem - Matt Carey](../videos/YBYUvGOuotE.md)
`YBYUvGOuotE` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: mcp-and-tools, sandboxing-execution

Cloudflare's Matt Carey argues that dumping every API endpoint into MCP tools blows up agent context, and that progressive discovery (tool search, CLIs, or code mode with typed SDKs run in isolates) is the way out.

- Techniques: Progressive tool discovery via tool search; Code mode over a generated typed SDK; Isolated execution of model-written code with programmable guardrails; Save agent-generated code as mini-scripts; Rate-limit APIs for agent callers
- Tools: MCP (Model Context Protocol), MCP SDK, OpenAPI, TypeScript, Cloudflare Workers, Dynamic Workers (workerd), V8 isolates, Wrangler, Cloudflare D1, Cloudflare Access, Claude Code, OpenClaw

## [I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com)](../videos/sJ2jc7leKBk.md)
`sJ2jc7leKBk` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: memory, agent-architecture

An OpenClaw maintainer shows how he grew a personal agent into a life-running system step by step, using an Obsidian knowledge base, scheduled maintenance and channel-per-job routing, plus its failure modes.

- Techniques: Incremental capability ladder; Channel-per-job-type routing; Link-capture enrichment into a markdown vault; Verified overnight maintenance; Deterministic scripts beside LLM judgment; Critical-rules block high in the instruction file; Draft-don't-send attention filtering; Routine memory hygiene
- Tools: OpenClaw, Obsidian, QMD, Discord, Telegram, WhatsApp

## [Ralph Loops: Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick](../videos/2TLXsxkz0zI.md)
`2TLXsxkz0zI` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: software-factory, coding-agents, agent-architecture

Chris Parsons runs a live workshop on Ralph loops: re-running Claude Code on fresh context until work ships, fed by ticket files, a sequential queue, and reversibility limits on unattended agents.

- Techniques: Bash while-loop over fresh Claude sessions; Next-most-important-ticket selection over flat markdown tickets; Recovery check for mid-flight work; Reversibility gate with stop-and-report; Fresh-subagent adversarial review; Claude /loop for timed repetition; Resume a project in an interactive session; Simulated audience personas run in parallel subagents; Nightly session digest
- Tools: Claude Code, Codex, Cursor, n8n, Docker Sandbox, Playwright, Obsidian, Lian (embeddings CLI), Beads, Linear, Jira, Telegram

## [The Future of MCP — David Soria Parra, Anthropic](../videos/v3Fr2JR47KA.md)
`v3Fr2JR47KA` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: mcp-and-tools, agent-architecture

David Soria Parra (Anthropic) on where MCP is heading: MCP apps, progressive tool discovery, code-style tool composition, and the 2026 protocol roadmap.

- Techniques: Progressive tool discovery; Programmatic tool calling / code mode; Use structured output to enable composition; Agent-first tool design; Pick connectivity per task; Skills-over-MCP approximation
- Tools: MCP, MCP Apps, Claude Code, Cloudflare MCP server, V8 isolate, Lua interpreter, FastMCP, Python SDK, TypeScript SDK, OpenAI Agents SDK, Google ADK, LangChain

## [Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub](../videos/ClWD8OEYgp8.md)
`ClWD8OEYgp8` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: coding-agents, multi-agent, product-ux

Maggie Appleton (GitHub Next) argues agents have shifted the bottleneck from building to agreeing on what to build, and previews ACE, a shared multiplayer environment for team-plus-agent work.

- Techniques: Shared always-on agent session per task; Whole-conversation context as prompt input; Plan first, co-edit, then execute; Session summary for switching between parallel sessions; Backward-compatible PRs that link back to the session
- Tools: GitHub ACE (Agent Collaboration Environment, research prototype), Claude Opus 4.6 (model used in the demo), Bun (bun install / bun dev in the demo project), VS Code (real-time multiplayer editing in the shared cloud machine), Slack, Jira, Linear (named as coordination tools that are not built for agentic work)

## [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../videos/_QAVExf_1uw.md)
`_QAVExf_1uw` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: rag-retrieval, skills-self-improvement, enterprise-adoption

A staff engineer at IKEA argues enterprise agents fail on undocumented institutional knowledge, and proposes a pull-based loop where agents surface knowledge gaps and curate context blocks before retrieval.

- Techniques: Pull-based knowledge capture from failed agent runs; Failing-tasks-as-tests for knowledge bases; Historical-incident replay as a probe source; Three-step gap scanner: probe generation, probe run, gap analysis; Freshness labels, flagged for human decision; Git-backed curated context blocks with a metamodel; 80/20 context cache with links to the monolith; Full-context before graph RAG, for small domains; Claude Code skills, rules, agents and hooks as the implementation
- Tools: Claude Code, GitHub Copilot, Confluence, Jira, Slack, GitHub, MCP, RAG, GraphRAG, Replit, Kanban board

## [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../videos/5ID22ACI7IM.md)
`5ID22ACI7IM` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: memory, rag-retrieval, security-guardrails

Peter Werry and Brandon (Unblocked) argue that agents need a "context engine" that understands org history, permissions and conflicts, not just MCP access to data, then run a hands-on social-graph workshop. Much of it is product pitch.

- Techniques: Compartmentalized, permission-tagged retrieval; Ingestion-time tags plus runtime judge for conflicts; Expert graph from contribution edges; Focus-repo-biased two-stage retrieval; Feedback weighted by source trust; Split cadence by source type
- Tools: Claude Code, Cursor, Codex, GitHub Copilot, MCP, Slack, Microsoft Teams, Sentry, Datadog, GraphRAG, pgvector-style vector retrieval, Composio

## ["Software Fundamentals Matter More Than Ever" — Matt Pocock](../videos/v4F1gFy-hqg.md)
`v4F1gFy-hqg` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: testing-verification, coding-agents, claude-code

Matt Pocock argues software fundamentals (deep modules, shared language, TDD, good feedback loops) matter more with AI agents, because bad code is now the most expensive it has been.

- Techniques: Grill-me interview before planning; Generated ubiquitous-language glossary; Small-step TDD with feedback loops; Codebase architecture improvement skill; Design the interface, delegate the implementation
- Tools: Claude Code

## [Give Your Agent a Computer — Nico Albanese, Vercel](../videos/wflNENRSUb4.md)
`wflNENRSUb4` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: agent-architecture, sandboxing-execution, mcp-and-tools

Nico Albanese (Vercel) live-builds a coding-style agent with AI SDK 6: a tool loop, web search, a persistent named sandbox running bash, file-based memory and self-written scripts, plus notes on context pruning and subagents.

- Techniques: Single-definition tool loop agent; Typed UI messages from the agent definition; Named persistent sandbox per session; Bash-only tool for a coding-style agent; Call options plus runtime context injection; File-backed memory injected into the system prompt; Per-step hook for message slicing; Subagents and handoff instead of compaction; Plan file with objective and checkboxes
- Tools: Vercel AI SDK 6, Vercel AI Gateway, Vercel Sandbox (persistent named sandboxes, beta), Next.js, Zod, OpenAI provider (web search tool), Anthropic provider (bash/computer tools), Vercel Workflow (durable steps), OpenCode, Amp (handoff tool)

## [Context Is the New Code — Patrick Debois, Tessl](../videos/bSG9wUYaHWU.md)
`bSG9wUYaHWU` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: evals, skills-self-improvement, security-guardrails

Patrick Debois argues that agent context (instructions, skills, specs) needs its own lifecycle like code: generate, test with evals, distribute as packages, observe logs, then adapt.

- Techniques: Layered context tests (lint, judge, end-to-end); Repeated runs with error budgets; Commit-scoped context A/B scenarios; Turning feedback into context fixes; Context filter before loading; Packaging context with provenance and scanning; Parallel generation as a spec-quality check
- Tools: Claude Code, AGENTS.md, CLAUDE.md, SKILL.md, MCP, Tessl, GitHub, GitLab, Slack, Snyk, Gemini, GitHub Copilot

## [LLM codegen fails and how to stop 'em — Danilo Campos, PostHog](../videos/juoNbJiZUi0.md)
`juoNbJiZUi0` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: coding-agents, skills-self-improvement, security-guardrails

Danilo Campos (PostHog) on making an autonomous integration agent reliable: feed fresh docs, use thin "model airplane" example apps, breadcrumb the task, interrogate the agent at each stop, and lock down secrets.

- Techniques: Agent-selected fresh docs menu; Model airplane example apps; Breadcrumbed multi-stage prompting; Stop-hook self-interrogation; Tool-gated secret access
- Tools: PostHog Wizard, Claude Agent SDK, Claude Code, Cursor, MCP, PostHog LLM gateway

## [Full Walkthrough: Workflow for AI Coding — Matt Pocock](../videos/-QFHIoCo-Ko.md)
`-QFHIoCo-Ko` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: software-factory, testing-verification, multi-agent

Matt Pocock's live workshop on an AI coding workflow: grill-me alignment, PRD, vertical-slice issues with blocking edges, AFK Ralph loops with TDD and feedback loops, and deep-module codebases.

- Techniques: Smart-zone sizing and clear-over-compact; Grill-me alignment skill; Destination doc plus journey issues; Ralph loop (sequential AFK runner); Red-green-refactor TDD for agents; Self-review in a fresh context; Interface-first deep modules with grey-box delegation; Push vs pull for coding standards; Sandcastle-style parallel runs; Delete plans and PRDs after they ship
- Tools: Claude Code, Sandcastle, Docker, TypeScript, GitHub Issues, TLDraw, Slido, Playwright MCP, Sonnet, Opus, Spec Kit, OpenSpec

## [Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind](../videos/cVzf49yg0D8.md)
`cVzf49yg0D8` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: voice-multimodal, agent-architecture, mcp-and-tools

Google DeepMind hands-on workshop on building agents with the Gemini Interactions API (server-side state, background runs, skills) and the Live API (native-audio voice agents), with live demos that partly failed.

- Techniques: Chained interactions via previous ID; Async background runs with polling or webhooks; Skill that links to live docs; Tool loop with recursion; Server-to-server Live proxy; Ephemeral token for direct browser connection; Context window compression for long Live sessions; Voice persona through system instructions; Send a single image and then audio
- Tools: Gemini Interactions API, Gemini Live API, Google AI Studio, Gemini 3 Flash / 3.1 Flash Live, Lyria 3, Nano Banana, Google Search grounding, uv, FastAPI, Context7, skills.sh, Antigravity

## [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase — Pedro Rodrigues, Supabase](../videos/GmAQKINjv1E.md)
`GmAQKINjv1E` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: skills-self-improvement, evals, claude-code

Pedro Rodrigues (Supabase) walks through writing agent skills, testing their triggering, and running with/without-skill evals, using a Postgres RLS view bug as the running example.

- Techniques: Progressive-disclosure skill layout; Trigger-accuracy testing via headless CLI; With/without skill eval comparison; Deterministic state assertions before LLM judging; MCP tool plus skill split for data access; security_invoker for Postgres views over RLS tables; Skill install via npm skills package with symlinks
- Tools: Claude Code, Supabase MCP server, Supabase CLI via npx, Postgres, Next.js, Braintrust, Langfuse, Vercel skills npm package, Python (DB reset and eval scripts), VS Code

## [Harnesses in AI: A Deep Dive — Tejas Kumar, IBM](../videos/C_GG5g38vLU.md)
`C_GG5g38vLU` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: agent-architecture, testing-verification, security-guardrails

Tejas Kumar (IBM) walks through building a "poor man's" agent harness live: deterministic guardrails, outcome verification, and credential injection around a weak model, with the prompt left unchanged.

- Techniques: Deterministic pre-turn hook for state and secrets; Outcome verification from the trace; Guardrails as composable functions; Two-level retry around an attempt; Naive head-and-tail context trimming; Tool definitions in the OpenAI SDK shape
- Tools: Playwright, Chromium, OpenAI Agents SDK-style tool definitions, GPT-3.5 Turbo, Claude Code, Cursor, Codex, Qwen, GPT-OSS, OpenRAG

## [Agent Optimization with Pydantic AI: GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic](../videos/A48uhxfxbsM.md)
`A48uhxfxbsM` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: evals, observability

Samuel Colvin (Pydantic) live-demos optimizing a structured-output extraction prompt with GEPA against a golden dataset, then serving managed prompt variables from Logfire without redeploying. Main takeaway: deterministic golden-set evals plus automated prompt search help most for cheaper models and private data.

- Techniques: Golden-dataset structured-output eval with a custom deterministic evaluator; Compare-two-runs error analysis; GEPA prompt search with an expert-prompt-engineer proposer; Keyed-component optimization instead of free-form prompt rewrites; Typed managed variables for live prompt and config changes; Trace the optimizer itself; Train/eval split with extra coverage
- Tools: Pydantic AI, Pydantic Logfire, GEPA (called JEPA in captions), DSPy, OpenFeature, Beautiful Soup, FastAPI, Pydantic AI Gateway, uv

## [Building your own software factory — Eric Zakariasson, Cursor](../videos/rnDm57Py54A.md)
`rnDm57Py54A` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: software-factory, testing-verification, coding-agents

Cursor engineer Eric Zakariasson on building a "software factory": how to structure repos, grow rules from observed failures, make agents verify their own work, and automate the human loops. Practical, with a product pitch.

- Techniques: Failure-driven rule growth; Reviewer bot enforces house conventions the model lacks; Self-verification with e2e tests and recorded runs; Scoped, parallel async tasks with front-loaded specs; Per-agent VM with a single dev command; Agentic code owners with risk tiering; Loop and stall detection for background agents; Event-triggered cleanup agents
- Tools: Cursor, Cursor cloud agents, BugBot, Playwright, AGENTS.md, Linear, Slack, GitHub, Datadog, Notion, MCP, Cursor workers

## [Scaling GitHub for your Agents — Sam Morrow, GitHub](../videos/0n3MKk7r60w.md)
`0n3MKk7r60w` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: mcp-and-tools, security-guardrails

GitHub's MCP server lead on scaling a remote MCP server: why too many tools hurt agents, how defaults and tool-set grouping work, token-trimmed outputs, scope-based auth, and a stateless design.

- Techniques: Per-request server construction with policy-filtered tools; Scope-filtered tool listing with step-up auth; Tool-set grouping with defaults tuned from usage data; Output-token tailoring per tool; Server-side composition to encode intent; Cross-tool eval for description tuning; Wrap read-only tools in a CLI to test agent use
- Tools: GitHub MCP server, Claude Code, VS Code, Redis, Cloudflare code mode, Anthropic tool search, Pi

## [Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi](../videos/mYSRn6PC1mc.md)
`mYSRn6PC1mc` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: agent-architecture, evals, mcp-and-tools

Workshop on building a deep-research agent (MCP server plus Claude Code skills) that feeds a separate LinkedIn writer workflow with evaluator-optimizer review and a calibrated LLM-judge eval loop.

- Techniques: Autonomy-ladder architecture choice; Tools as specialists inside one agent; Delegation to keep context lean; Files as the inter-agent contract; Guideline plus static style profiles; Start with many few-shot examples, then trim; Evaluator-optimizer with fresh context and typed feedback; Synthetic eval inputs, real outputs, binary labels with critiques; Judge calibration with dev/test F1; MCP server exposes tools, prompts and resources; skills wrap prompts for progressive disclosure; Trace-based debugging with threads and traces
- Tools: Claude Code, FastMCP, MCP, Gemini API (grounding, multimodal YouTube), Firecrawl, Perplexity, Opik, Pydantic, git-ingest, uv, Python

## [Hermes: The Self-Improving Agent That Gets Smarter Every Day](../videos/HdxtLpL9CC8.md)
`HdxtLpL9CC8` · Better Stack · 2026-05-02 · q3 · intro · review · also: skills-self-improvement, memory, token-cost-efficiency

Hands-on test of Hermes, an open-source self-improving agent from Nous Research: it stores memory and writes skills from use, and the video shows how it manages context. A single-user demo, so the evidence is anecdotal.

- Techniques: Bounded memory preload plus full-text session archive; Early, selective context compression; Periodic persistence nudge; Style-learning loop that ends in a skill; Mid-session model switch for cost
- Tools: Hermes (open-source self-improving agent, Nous Research), OpenRouter (model provider; Gemma 4 selected), Gemma 4 (default model in the demo), GLM (cheaper model used mid-session; transcribed as 'glm5 turbo'), OpenClaw (compared agent, more channels and sandboxing), NanoClaw (compared agent, built on the Claude Agent SDK), Claude Agent SDK, Claude Code (compaction threshold comparison), SuperMemory (optional external memory processor), Mem0 (optional external memory processor; transcribed as 'Memzero'), OpenViking (optional external memory processor), SQLite with FTS5 (session store and search)

## [ChatGPT is OBSESSED with Goblins (Here’s Why)](../videos/RGIrw2G70wE.md)
`RGIrw2G70wE` · Better Stack · 2026-05-02 · q3 · intro · news · also: training-finetuning-rl, models-research

Explains OpenAI's investigation into why ChatGPT kept inserting goblins and gremlins: a reward signal for the nerdy persona rewarded those words, and the habit spread through training and self-generated data.

- Techniques: Spurious-reward audit via matched pairs; Track lexical quirk frequency across releases, personas and training steps; Break self-generated training feedback loops; Negative system-prompt rule with a relevance condition as a stopgap
- Tools: ChatGPT, Codex, GPT-5.1, GPT-5.4, GPT-5.5

## [This Is The Anthropic Team's Greatest Advice](../videos/O1XLCh-uA_E.md)
`O1XLCh-uA_E` · AI LABS · 2026-05-02 · q2 · practitioner · tutorial · also: claude-code, multi-agent, agent-architecture

Practical habits for managing Claude Code's context window (compaction, clear, rewind, sub-agents, recaps) to limit context rot and goal drift in long runs; mostly attributed advice with a sponsored segment.

- Techniques: Manual compaction with an explicit instruction; Clear on task switch; Structured state handoff (save, clear, reload); Periodic recap to reinforce goals; Sub-agent isolation for raw-heavy subtasks; Rewind, then re-prompt
- Tools: Claude Code, Claude (Opus 4.5 and later models, 1M context window), CLAUDE.md, Verdant (sponsor)

## [This Claude Skill Cuts Your Token Costs In HALF](../videos/RuH3uiJy84A.md)
`RuH3uiJy84A` · Better Stack · 2026-05-02 · q2 · practitioner · review · also: token-cost-efficiency, claude-code, skills-self-improvement

Better Stack tests Caveman, a Claude Code skill that makes answers terse to cut output tokens. Output savings are real (45%), but the skill's own input overhead erases them on single prompts.

- Techniques: Terse-output skill file; Three-arm token A/B; Count the instruction file as input cost; Compressed instruction files; Terse commit and review outputs
- Tools: Claude Code (captions say 'claw code'), Codex (named as compatible), Caveman skill, Next.js (demo app), Better Stack RUM (demo app context), skills package installer (name garbled in captions as 'Vasell'), prompt caching (provider feature referenced by the presenter)

## [This Tool Fixes AI Coding at Scale with 70x Fewer Tokens (Graphify)](../videos/WNru_PFycT8.md)
`WNru_PFycT8` · Better Stack · 2026-05-02 · q3 · intro · review · also: token-cost-efficiency, coding-agents, memory

Better Stack demo of Graphify, a tool that builds a relationship graph of a repo and its docs so Claude Code answers from the map instead of re-reading files. Claims over 70% fewer tokens; the evidence is one small-repo anecdote.

- Techniques: Pre-built repo knowledge graph as the agent's map; Hybrid extraction: parser for structure, LLM for meaning; Label edges with provenance and confidence; Incremental re-indexing with a persisted report
- Tools: Graphify, Claude Code, Cursor, tree-sitter

## [Give Me 13mins, I Will Show You The Right Agent Setup](../videos/ywIhw15za9Y.md)
`ywIhw15za9Y` · AI LABS · 2026-05-02 · q2 · intro · tutorial · also: claude-code, testing-verification, coding-agents

AI LABS walks through a pre-build setup checklist for Claude Code: product-focused PRD, hand-written CLAUDE.md, agents and skills, spec-first tests, progress and learnings files, and load planning. Generic, sponsored, no benchmarks.

- Techniques: Agent-led PRD interview; Lean hand-written CLAUDE.md that links the PRD; Agent vs skill split; Path-scoped rules linked from CLAUDE.md; Negative-constraints docs file; Progress file plus learnings file; Spec-first test generation; Commit-per-implementation with worktrees; Concurrency-aware load test planning
- Tools: Claude Code, CLAUDE.md, Supabase MCP, shadcn/ui, Playwright, Playwright MCP, skill-creator, GitHub, Git (commits, worktrees), Notion MCP, Trello, OpenClaw (sponsor's skill)

## [Knowing This Gives You An Unfair Advantage With AI Coding](../videos/fMY5Sdj2DMk.md)
`fMY5Sdj2DMk` · AI LABS · 2026-05-02 · q3 · practitioner · tutorial · also: claude-code, coding-agents, testing-verification

Tutorial for writing CLAUDE.md rules that keep Claude Code on task: think-first, simplicity, surgical edits, verifiable goals, git safety, scoped rule files and a corrections log.

- Techniques: Behavioral rule block for CLAUDE.md (Karpathy-derived); Verification gate before reporting completion; List only non-default tooling; Corrections-to-learnings loop; Destructive-command confirmation rule; Path-scoped rule files and nested CLAUDE.md; CLAUDE.md structure: description first, priority tiers, length cap
- Tools: Claude Code, CLAUDE.md, AGENTS.md, Karpathy skills repo (referenced, not named as a package), Claude Chrome extension, Puppeteer MCP, Git, GitHub CLI (gh), npm, pnpm, Klaus (sponsor, AI agent hosting), OpenClaw (sponsor, open-source AI agent)

## [How To Never Hit Your Claude Code Limit Again](../videos/YsdQE6juGXY.md)
`YsdQE6juGXY` · AI LABS · 2026-05-02 · q3 · practitioner · tutorial · also: token-cost-efficiency, claude-code

Practitioner tips for stretching Claude Code's usage limits: explains the 5-hour window, then covers context hygiene, lean CLAUDE.md, model and effort routing, hooks, and settings toggles. Partly sponsored; leaked-source claims are unverified.

- Techniques: Clear or compact between tasks; Side questions in a separate context via the by-the-way command; Rewind to before a misaligned turn instead of re-prompting; Lean CLAUDE.md with linked, progressively loaded docs; Path-scoped rules files; Skills with bundled scripts for repetitive workflows; Session-only instructions via the append-system-prompt flag; Task-based model and effort routing; Disable unused MCP servers per project; Hook that keeps only failing tests in context; Settings toggles for token use
- Tools: Claude Code, Claude (Pro and Max plans), Claude Desktop, Cowork, Claude Opus, Claude Sonnet, Claude Haiku, Claude.md (CLAUDE.md), MCP servers, Twin (sponsor), Zapier (named in sponsor segment), n8n (named in sponsor segment)

## [We Already Have Something Better Than Claude Design](../videos/GbuwosWEvHo.md)
`GbuwosWEvHo` · AI LABS · 2026-05-02 · q2 · intro · review · also: claude-code, coding-agents, product-ux

AI LABS argues Claude Design is mostly hype: Claude Code with Opus 4.7 can match it, and it adds Git, parallel worktrees, and skills. The evidence is one anecdotal comparison plus sponsor-heavy, unverified claims.

- Techniques: Clarifying-question skill to replace Claude Design's intake flow; Hero video background plus animation libraries; Component libraries and MCP for UI consistency; Parallel design variants in git worktrees; Prototype as HTML mock-ups
- Tools: Claude Code, Claude Design, Claude Opus 4.7, Claude Opus 4.6, GSAP, Lenis, ShadCN, ShadCN MCP server, Aceternity UI, Hero UI, scrollytelling skill, Figma

## [Your AI Output Sucks Because You’re Not Doing This](../videos/cop_G65D7PA.md)
`cop_G65D7PA` · AI LABS · 2026-04-02 · q2 · intro · tutorial · also: claude-code, multi-agent, token-cost-efficiency

AI LABS' pre-setup tips for Cowork: a per-folder manifest.md with tiered sources, voice and working-style files, global instructions that demand plans and questions, end-state prompts, batching and guardrails.

- Techniques: Per-folder manifest.md with tiered sources; Identity, voice and working-style context files; Global instructions as a default operating contract; State the end state and the edge-case rule; Batch by shared context, keep unrelated work apart; Scheduled report from meeting notes via the schedule skill; Build a plugin with the plugin-creation skill; Guardrails for agent file access
- Tools: Cowork, Claude Code (clawed code in transcript), Claude desktop app, CLAUDE.md (global and per-folder instructions), manifest.md (the presenter's convention), schedule skill, plugin-creation skill, OpenClaud (auto-caption; used for research, tool-release tracking and a Discord report; spelling uncertain), Discord, Gmail connector, Google Drive connector, cron jobs

## [How to Use Google Stitch to Make Sites 10X More Beautiful](../videos/b0lwCDNOFUY.md)
`b0lwCDNOFUY` · AI LABS · 2026-04-02 · q2 · practitioner · tutorial · also: vibe-coding-app-building, coding-agents, skills-self-improvement

Tutorial on pairing Google Stitch with Claude Code: design.md design systems, screenshot-based redesign, Stitch skills and MCP, then React and shadcn conversion. Includes sponsor segments.

- Techniques: design.md-first design system; Extract design.md from an existing Stitch project; Screenshot as style reference (Redesign); Import style from a URL; Sketch plus theme to correct drift; Annotate-and-apply targeted edits; CLAUDE.md pipeline for Stitch skills; Convert a Stitch project to shadcn/ui
- Tools: Google Stitch, Claude Code, design.md, Stitch MCP, Stitch Enhance Prompt skill, Stitch Loop skill, Stitch React component skill, Stitch design.md skill, Google Stitch skills repo, Chrome DevTools, NanoBanana (image generation), GoFullPage (Chrome extension)

## [12 Hidden Settings To Enable In Your Claude Code Setup](../videos/pDoBe4qbFPE.md)
`pDoBe4qbFPE` · AI LABS · 2026-04-02 · q2 · practitioner · tutorial · also: claude-code, multi-agent

Tour of under-documented Claude Code settings: session retention, output and read caps, sub-agent flags, auto-compact at 75%, commit attribution, telemetry, and exit-code-2 hooks. Includes a sponsored segment.

- Techniques: Extend session retention; Path-scoped rules; Raise the bash output cap; Run a session as a sub-agent; Raise the file read cap and enforce full reads; Lower the auto-compact threshold; Remove commit co-author lines; Opt out of telemetry without losing updates; Prompt stash with Ctrl+S; Exit-code-2 hook to block and steer; Loop-until-done with exit-code hooks (Ralph-style); Claude CTX profiles
- Tools: Claude Code, Claude CTX (open-source profile switcher), Opus 4.6 (cited as the 1M-token-context model), uv (transcribed as 'uvicorn'; likely the pip replacement in the hook example), Statsig (analytics sink, named by speaker), Sentry (error reporting sink, named by speaker), Make.com (sponsor), Ralph loops (named concept, not a tool)

## [How to use Claude Code and Gemini Cli Together](../videos/XdtBAm2pM-0.md)
`XdtBAm2pM-0` · AI LABS · 2026-04-02 · q3 · practitioner · tutorial · also: multi-agent, coding-agents, claude-code

Walkthrough of Agent Chatter, a shared chat layer where Claude Code, Gemini CLI and Codex agents run in tmux and coordinate through channels, with planning, peer review and loop-guard setup.

- Techniques: Shared multi-model chat via per-agent tmux sessions; Per-agent settings.json permissions instead of skip-permissions; Shared agents.md as the single instruction source; Named personas per agent; Loop guard and continue gate; Planner-first with PRD and spec templates; Three-phase presenter/challenger/synthesizer review; Planner as orchestrator with an ask-don't-assume rule; Git worktrees per agent (suggested, not tested); Initialize the app framework before starting agents
- Tools: Agent Chatter, Claude Code, Opus 4.6, Gemini CLI, Codex, Kimi, Qwen, GLM, tmux, Next.js, MCP, agents.md

## [GSD Is the Missing Piece For Claude Code](../videos/uEit1oOJK0w.md)
`uEit1oOJK0w` · AI LABS · 2026-04-02 · q2 · practitioner · review · also: coding-agents, multi-agent, testing-verification

AI LABS walks through GSD (Get Shit Done), a planning-and-execution framework for Claude Code, and compares it with BMAD and Superpowers. Main takeaway: choose the framework by how fixed your requirements are.

- Techniques: Choose the framework by requirement certainty; Per-project install with project scope; Initialise GSD on existing vs blank codebases; Keep the planning anchor short; Per-phase discuss, then concise context file; Ground phase research in docs with Context7; Adversarial plan verification and waves; Phase verification gates
- Tools: GSD (Get Shit Done), BMAD method, Superpowers, Claude Code, Claude Opus 4.6, Claude Sonnet, Next.js, Playwright, Context7 MCP, GenSpark (sponsor segment), Speakly (sponsor segment)

## [Anthropic Just Killed All Your Agent Harnesses](../videos/nBH07G-zayk.md)
`nBH07G-zayk` · AI LABS · 2026-04-02 · q2 · practitioner · review · also: agent-architecture, testing-verification, claude-code

Walkthrough of Anthropic's reported harness ablations: with Opus 4.5/4.6, keep a planner, a generator and a separate graded evaluator, and drop micro-level plans, context resets and sprint contracts for strong models.

- Techniques: Product-level planner agent; Separate evaluator with an adversarial stance; Weighted rubric with a score per criterion; Generator and evaluator as agent-team members; Sprint contract for weaker models; Bolt Anthropic's evaluator onto GSD
- Tools: Claude Code, Claude Opus 4.5, Claude Opus 4.6, Claude Sonnet, Claude Haiku, Anthropic agent harness, BMAD, GSD, SpecKit, Superpowers, Ralph Loop, Playwright MCP

## [Anthropic's Head of Design Just Killed The Old Process](../videos/X4vAlWtsJD4.md)
`X4vAlWtsJD4` · AI LABS · 2026-04-02 · q2 · practitioner · tutorial · also: vibe-coding-app-building, product-ux, coding-agents

A walkthrough of how an AI Labs team now builds app prototypes: actors and constraints first, PRD and architecture files, a Next.js and Supabase prototype with mock data, then a backend added only when needed.

- Techniques: Actor-first requirements; Constraints instead of tool instructions; PRD interview prompt; Layer prompt to architecture.md; Scaffold Next.js with Supabase, then apply a frontend-design skill; Mock-data prototype for sign-off; Task lists from architecture.md; API spec from frontend code plus PRD plus architecture; Supabase MCP for schema and migrations; Front end talks directly to the database; backend only when needed; Delegate the backend layer to a cloud agent
- Tools: Figma, Next.js, Supabase, Supabase MCP, Python, Warp Oz (sponsored cloud-agent orchestration), Stripe, Google authentication, Anthropic general-purpose frontend-design skill

## [I Didn't Know This Was Possible Until Now](../videos/LqN_ItMqovA.md)
`LqN_ItMqovA` · AI LABS · 2026-04-02 · q3 · practitioner · review · also: mcp-and-tools, token-cost-efficiency, claude-code

A team's walkthrough of MCP context bloat and a runtime MCP-to-CLI converter (MCP2CLI), plus CLAUDE.md and skills rules that keep large tool outputs out of the context window.

- Techniques: Run MCP2CLI without installing it; Give the agent the MCP access tokens through environment or file references; Verify MCP connections by asking the agent to count the tools; CLAUDE.md rule to consult docs before coding; Move per-MCP guidance from CLAUDE.md into one skill per MCP; Ask for TOON output for verbose documentation MCPs; Redirect large MCP output to a file and grep it; Use Claude's browser extension for stateful browser testing

## [Claude Code is Expensive. This MCP Server Fixes It (Context Mode)](../videos/QUHrntlfPo4.md)
`QUHrntlfPo4` · Better Stack · 2026-04-02 · q3 · intro · review · also: token-cost-efficiency, mcp-and-tools

Better Stack demo of Context Mode, a Claude Code MCP plugin that indexes large tool outputs in local SQLite FTS5 and keeps a small snapshot across compaction. Practical, with one small measured example.

- Techniques: Index large tool output into a local FTS5 store; Priority-tiered snapshot injected on compaction; Remember failed attempts across resets; Install Context Mode in Claude Code; Install Context Mode in Gemini CLI or VS Code Copilot; Measure the savings with the stats command; Demo prompt for indexed log analysis
- Tools: Claude Code, Context Mode, SQLite, FTS5, Playwright, GitHub, Gemini CLI, VS Code Copilot, npm, Python

## [10 Crazy Claude Code Tips That Give You An Unfair Advantage](../videos/TmsH-RIHvas.md)
`TmsH-RIHvas` · AI LABS · 2026-03-02 · q3 · practitioner · tutorial · also: claude-code, testing-verification, multi-agent

AI LABS walks through ten Claude Code practices: session-insight reviews, Claude-written planning docs, exit-code-2 hooks, worktree-based parallel agents, adversarial fact-checking, and browser-based self-verification.

- Techniques: Session insights review into CLAUDE.md; Claude-authored planning docs as context; Context7 MCP for current library docs; Exit-code-2 PreToolUse guard for protected paths; MCP CLI mode to keep tool schemas out of context; One git worktree per parallel agent; Strict TypeScript and user stories before implementation; Adversarial researcher and fact-checker agents; Agent Browser for self-verification, with CLAUDE.md fallback order; Failure-prediction review pass
- Tools: Claude Code, CLAUDE.md, Claude Code hooks (PreToolUse), MCPCLI (experimental MCP CLI mode), Context7 MCP, git worktrees, TypeScript, Claude in Chrome extension, Puppeteer MCP, Agent Browser (Vercel), Kimi K2.5 (named as comparison in a research example), Opus 4.6 (named as subject of a research example)

## [OpenAI is Winning... (Opus 4.6 + Codex 5.3)](../videos/OI6DkkNDf6o.md)
`OI6DkkNDf6o` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: coding-agents, models-research

Better Stack runs Claude Opus 4.6 and GPT-5.3 Codex through an AI SDK v6 migration, a Three.js Club Penguin clone and a landing page; each test is one run, so the verdicts are soft.

- Techniques: Migration prompt with guardrails; Review the diff for reimplemented library helpers; Cross-model second opinion; Steer instead of interrupt
- Tools: Claude Opus 4.6, GPT-5.3 Codex, GPT-5.2 Codex, GPT-5.2, Claude Code, Codex app, Convex, Convex Agent package, AI SDK v6, Three.js, Terminal-Bench 2.0, Artificial Analysis

## [Copilot Helps You Type…. This Helps You Ship](../videos/LRwc64Ui_MQ.md)
`LRwc64Ui_MQ` · Better Stack · 2026-03-02 · q2 · intro · review · also: coding-agents, pr-code-review

A short walkthrough of Continue, an open-source VS Code extension for model-agnostic codebase chat, diff-based edits and markdown-defined PR review agents, positioned as complementary to Copilot.

- Techniques: Model-agnostic Continue setup; Repo-aware explanation of unfamiliar code; Review and apply diffs in chat; Markdown-defined PR review agent; Split autocomplete and review tools
- Tools: Continue (VS Code extension, open source), GitHub Copilot, VS Code, Ollama, Llama 3 (Llama3), GPT-4, Claude, OpenAI, Slack, Cursor, Claude Code

## [Anthropic Released Another Official Process](../videos/aEqKWI-0N0c.md)
`aEqKWI-0N0c` · AI LABS · 2026-03-02 · q2 · practitioner · tutorial · also: skills-self-improvement, claude-code, testing-verification

A team rebuilds a Nano Banana image skill for Claude Code, then shows the skill-design fixes that mattered: trigger-rich descriptions, progressive disclosure, scripts, validation gates and error tables.

- Techniques: Trigger-rich skill descriptions with negative triggers; Three-level progressive disclosure layout; Move constraints out of prompts into post-processing; CLI scripts with modes and a preview mode; Two-stage validation gates with regenerate-on-fail; Error table with error, cause, and fix; Split domain knowledge into reference packets; Iterate against real outputs and refresh the skill-creator
- Tools: Claude Code, Google Antigravity, Nano Banana Pro, skill-creator (Claude Code official skill), Next.js, Cream (sponsor, merchant of record), Cursor, Windsurf

## [How To Use NotebookLM - 7 Crazy Ways](../videos/eFCHwtufjJc.md)
`eFCHwtufjJc` · AI LABS · 2026-03-02 · q3 · practitioner · tutorial · also: rag-retrieval, claude-code, coding-agents

AI LABS shows seven ways to wire Google's NotebookLM CLI into Claude Code as a grounded knowledge base: a second brain, research store, codebase onboarding, debugging KB, agent-readable visualizations, and a security handbook.

- Techniques: Install and verify the NotebookLM CLI; Notebook as project second brain via CLAUDE.md; Research offload to a notebook; Codebase onboarding via Repomix; Debugging knowledge base in place of web search; Export mind maps and tables as agent-readable artifacts; Security handbook notebook for grounded reviews; Shared notebook as knowledge base for people and other agents
- Tools: NotebookLM (Google), NotebookLM CLI (version not stated), Claude Code, CLAUDE.md, Repomix (CLI, installed via npm), GitHub CLI (gh), Gemini (answers NotebookLM queries, per the speaker), Cursor, Gemini CLI, OWASP cheat sheets, Make (sponsor, pre-built market research agent)

## [Give Claude Persistent Memory in 5 Minutes](../videos/ryqpGVWRQxA.md)
`ryqpGVWRQxA` · Better Stack · 2026-03-02 · q2 · intro · review · also: memory, claude-code, token-cost-efficiency

Shows Claude-Mem, an open-source local tool that auto-captures Claude Code session events (bug fixes, decisions, diffs) and recalls compressed context in new sessions.

- Techniques: Automatic session-event capture into a local memory store; Compressed-summary-first recall with expand-on-demand; Tag and keyword search over memories; Reproducing the demo test for a memory tool
- Tools: Claude Code, Claude-Mem (open-source Claude Code memory plugin; version not stated)

## [Vite, Rust & The Future of JavaScript Tooling | Better Stack Podcast Ep. 11](../videos/LSGZtHafiM4.md)
`LSGZtHafiM4` · Better Stack · 2026-03-02 · q4 · practitioner · review · also: dev-tools, coding-agents

Vite creator Evan You explains why the Vite toolchain is moving to Rust (Rolldown, OXC), the unified Vite+ CLI, guardrails for agent-written code, and his skepticism about React Server Components.

- Techniques: Pre-bundle dependencies in dev, serve source as native ESM; Bundle for production when module count crosses a threshold; Built-in transforms instead of plugin chains; Check the data-boundary cost before offloading to native code; Arena-allocate ASTs in one contiguous buffer; One config, one resolver for the whole toolchain; Vite+ commands and version pinning; Ship AGENTS.md and skills with the package, patched on upgrade; Guardrails against agent shortcuts in PR review; Schedule debt-paydown passes between feature pushes; Plan mode, then write AGENTS.md, and run agents in parallel; Run downstream ecosystem CI before a major release
- Tools: Vite (v7 current, v8 in beta per the speaker), Vite+ (vp CLI), Rollup, Rolldown, esbuild, webpack, Rspack, SWC, OXC (parser, resolver, transformer, minifier), oxlint, oxfmt, Vitest (auto-caption 'VTest')

## [The Last Claude Code Tutorial You'll Ever Need](../videos/EHDzlot7LKU.md)
`EHDzlot7LKU` · AI LABS · 2026-02-02 · q3 · intro · tutorial · also: claude-code, multi-agent, skills-self-improvement

Principles for building your own agent workflow in Claude Code: progressive disclosure, external note files, context-budget hygiene, subagents, git and slash commands.

- Techniques: Progressive disclosure via skills; External note files for long tasks; Manual context hygiene; Delegating research to subagents; Format selection for context files; Git as memory and parallelism; Slash commands for repeated procedures
- Tools: Claude Code, Claude (Anthropic models, 200k context), Gemini (1M context), Sonnet 4.5, BMAD, SpecKit, agent.md / AGENTS.md, CLAUDE.md, Jira MCP, Figma MCP, Git, git worktrees

## [How to Build a RAG System That Actually Works](../videos/pvCabUerwss.md)
`pvCabUerwss` · Better Stack · 2026-02-02 · q3 · intro · tutorial · also: rag-retrieval

Better Stack walkthrough of building a RAG system over Star Wars scripts with LangChain, OpenAI embeddings and local Qdrant, focused on scene-aware chunking and prompt grounding.

- Techniques: Scene-aware recursive chunking; Persist-or-build vector store; Fixed-k retrieval with a deterministic chat model; Prompt grounding tuned with a scope test set
- Tools: LangChain, langchain-openai, langchain-qdrant, qdrant-client, langchain-text-splitters, BeautifulSoup4, requests, uv, Qdrant (local vector database, written in Rust), OpenAI text-embedding-3-small, GPT-4o

## [Anthropic Have FINALLY Solved the MCP Context Nightmare](../videos/1RpGVqgqLaE.md)
`1RpGVqgqLaE` · Better Stack · 2026-02-02 · q2 · intro · news · also: mcp-and-tools, token-cost-efficiency, claude-code

Claude Code's MCP tool search loads only the 3-5 most relevant tools on demand instead of preloading every schema, cutting context use. A short explainer that compares it with Cloudflare's code-orchestration approach.

- Techniques: Threshold-gated tool search; Programmatic tool orchestration; Wrap MCP servers as CLI commands
- Tools: Claude Code, Claude Opus, MCP (Model Context Protocol), Cloudflare Workers, Cloudflare (programmatic tool calling), Cursor, Agent Skills, mcporter, Python, TypeScript, Better Stack MCP server, Gemini (1M-token window, mentioned only)

## [This Exceeded Every Expectation I Had](../videos/iC9loBJjduM.md)
`iC9loBJjduM` · AI LABS · 2026-02-02 · q3 · practitioner · tutorial · also: claude-code, mcp-and-tools, token-cost-efficiency

Applies Cursor's dynamic context discovery ideas to Claude Code via CLAUDE.md: offload big tool output and chat history to files, lazy-load MCP tools, and grep logs instead of re-running them.

- Techniques: Offload large MCP responses to files; Per-session history file as compaction insurance; Timestamped terminal logs with grep-and-tail retrieval; Progressive-disclosure skills; Lazy MCP tool loading with the experimental MCP CLI flag
- Tools: Claude Code, Cursor, Antigravity, Codex, Gemini CLI, Claude Chrome extension, CLAUDE.md, MCP (Model Context Protocol), MCP CLI (experimental Claude Code flag), Claude advanced tool search (developer platform), Cursor semantic search, grep

## [Claude Code Just Got a Brain Upgrade Inspired By Beads](../videos/-xOAYPjhigY.md)
`-xOAYPjhigY` · Better Stack · 2026-02-02 · q3 · intro · review · also: claude-code, multi-agent, agent-architecture

Better Stack walkthrough of Claude Code's new task system (v2.1.6+), which replaces todos with JSON-backed tasks that support dependencies, sub-agents, and shared task lists across sessions; compared against Beads and the Ralph Wiggum loop.

- Techniques: Plan file to tasks, then sub-agent execution; Shared task list across sessions via env var; Version-control task state
- Tools: Claude Code (v2.1.6+), Beads, Ralph Wiggum loop, Opus 4.5, XDL (CLI for downloading videos from X/Twitter, used as the demo project), Better Stack

## [Claude Code's Creator Does This Before Every Single Project](../videos/B-UXpneKw6M.md)
`B-UXpneKw6M` · AI LABS · 2026-02-02 · q2 · practitioner · tutorial · also: claude-code, testing-verification, multi-agent

Boris, who created Claude Code at Anthropic, shares a short workflow: give the agent a way to verify its work, keep CLAUDE.md lean and team-maintained, use plan mode and scoped permissions, and run parallel or background sessions.

- Techniques: Verification line in CLAUDE.md; Tests-first or tests alongside each feature; Browser or screenshot verification for UI; Team-maintained CLAUDE.md; Mistakes from PR review go into CLAUDE.md; Project-scoped allow/ask/deny permissions; Plan mode before execution; Parallel sessions with numbered tabs; Cloud background agents with teleport; Background verification tasks; Stop hook for verification; Loop plugin for autonomous runs; Per-language linters and formatters; Committed slash commands; Narrow subagents
- Tools: Claude Code, CLAUDE.md, Claude Code GitHub action, Claude Code on the web (cloud sessions), Claude browser extension, Opus 4.5, Sonnet, Haiku, Ralph Wiggum plugin, MCP servers (Slack, Notion), BigQuery CLI, Sentry CLI

## [I Can't Believe Anthropic Messed Up The Ralph Wiggum](../videos/XVAhQ-EcrWA.md)
`XVAhQ-EcrWA` · Better Stack · 2026-02-02 · q3 · practitioner · tutorial · also: agent-architecture, coding-agents, claude-code

Better Stack explains the Ralph loop (a bash while-loop that reruns one prompt with a fresh context each time) and why the official Claude Code Ralph plugin, with compaction and iteration caps, drifts from the canonical design.

- Techniques: Fresh-context bash Ralph loop; Plan-file task selection; Keep fixed context small; Human-on-the-loop review; GitHub-issues task queue; Filter error output with an MCP server
- Tools: Ralph loop (bash while-loop pattern), Claude Code, Claude Code Ralph Wiggum plugin (Anthropic, slash command with max iterations and completion promise), agents.md, Raz Mike's Ralphie bash script, agent-browser tool (named Vasell in the captions), GitHub issues, Better Stack MCP server (log and frontend error search), GPT-5 tokenizer (used for a token-count comparison)

## [Skills Had ONE Job (They Failed)](../videos/i0W90tlKfYg.md)
`i0W90tlKfYg` · Better Stack · 2026-02-02 · q4 · practitioner · review · also: skills-self-improvement, evals, coding-agents

Vercel's Next.js eval found a passive AGENTS.md doc index beat on-demand skills (100% vs. skills that were often never invoked); skills suit explicit workflows, AGENTS.md suits framework knowledge.

- Techniques: Passive documentation index in AGENTS.md; Split context by trigger type; Measure skill trigger rate, not just existence
- Tools: Next.js, Agent Skills (open standard, Anthropic), Vercel skills CLI and skills repository (named as 'skill CLI' in the transcript), AGENTS.md, CLAUDE.md

## [ShadCN is Way too Powerful Now](../videos/MFJ0mH72_qI.md)
`MFJ0mH72_qI` · AI LABS · 2026-02-02 · q2 · practitioner · tutorial · also: claude-code, testing-verification, agent-architecture

Ralph stop-hook loop plus TDD and screenshot checks for ShadCN UI work; a separate verification iteration before the completion promise fixed premature "done" claims.

- Techniques: Stop-hook completion-promise loop; Test-first workflow inside the loop; Screenshot verification protocol; Two-phase completion gate
- Tools: ShadCN (UI component library), Claude Code, Ralph plugin (Anthropic, Ralph loop), Claude Code stop hooks, Playwright, Playwright MCP (named only to say it was not used), Notion (reference point for the board view), Automata (sponsor)

## [Vercel Just Revealed Claude Code's Greatest Advantage](../videos/gZr5VmsXmXQ.md)
`gZr5VmsXmXQ` · AI LABS · 2026-02-02 · q3 · practitioner · talk · also: rag-retrieval, sandboxing-execution

Argues that LLM agents can retrieve context with plain bash (ls, find, grep, cat) instead of a vector DB, sending only a small slice to the model; shows a Gemini 2.5 Flash policy-docs demo and states when RAG still wins.

- Techniques: Bash-tool retrieval over a document directory; Scoped execution for agent shell access; Markdown-defined multi-phase evaluation pipeline; Route retrieval by data shape and query type
- Tools: Vercel bash tool (open-sourced; name not stated), Vercel sandbox (full VM isolation), Claude Code, CLAUDE.md, Gemini 2.5 Flash, Chroma (vector DB the speaker would normally have used), grep, ls, find, cat

## [Why Google Antigravity Suddenly Makes Sense](../videos/e4giCKHIJy8.md)
`e4giCKHIJy8` · AI LABS · 2026-02-02 · q2 · practitioner · review · also: coding-agents, testing-verification, skills-self-improvement

A walkthrough of Google Antigravity as a coding agent, using Cursor's published harness principles: plan-first with commented revisions, on-demand context, TDD, Git as knowledge base, and skills-based debug mode.

- Techniques: Comment-driven plan revision; On-demand context instead of manual file tagging; Conversation reset policy; Project rules as markdown in .agent/rules; Skill folders following Anthropic's open standard; TDD with a committed test baseline; Screenshot as design and bug input; Git workflows as reusable commands; Agent-run code review with severity sorting; Parallel agents on separate branches; Skill-based debug mode; Watch the agent and redirect early
- Tools: Google Antigravity (AI code editor with planning mode, rules, skills and workflows), Gemini 3 (model used in Antigravity), Claude Code, Claude Opus, Cursor, Cursor's agent harness article (referenced, not named as a product), Anthropic's long-running agent harness (referenced), Anthropic's open Agent Skills standard (SKILL.md), Git, GitHub (built-in PR code review), CodeRabbit, Sentry

## [The Greatest Problem With AI Coding Is Solved](../videos/3FZIdRZsUMM.md)
`3FZIdRZsUMM` · AI LABS · 2026-02-02 · q2 · intro · talk · also: testing-verification, coding-agents, claude-code

AI LABS argues the implementation middle of software work is being replaced by agents, so developers should focus on planning, context setup, and reviewing or testing agent output.

- Techniques: Refine the plan, then run one-shot implementation; Split spec into per-concern documents; Test-first with a context reset and locked tests; Black-box testing from user stories with a browser agent; White-box review with an XML test plan and a slash command; Layered project structure for agents
- Tools: Linear, Dart AI, VS Code, Claude Code, Claude Chrome extension, Cursor, Slack, CLAUDE.md, skill.md, MCP, XML

## [I Wasn't Ready For What This Does](../videos/XP6TJRbOdGo.md)
`XP6TJRbOdGo` · AI LABS · 2026-02-02 · q2 · intro · tutorial · also: vibe-coding-app-building, voice-multimodal

A step-by-step landing-page workflow: Google Whisk keyframes, Google Flow frame-to-video, MP4-to-animated-WebP for a scroll-mapped hero, then Claude adds HeroUI, Motion.dev and 21st.dev components in Next.js.

- Techniques: Two-keyframe hero animation; MP4 to animated WebP for scroll mapping; XML-sectioned prompt for an AI coding agent; Install individual UI components instead of the whole library; Copy-paste component prompts from 21st.dev
- Tools: Google Whisk, Nano Banana (image generation, via Whisk), Gemini 3 (prompt expansion layer in Whisk; planning in Flow), Google MixBoard, Google Flow, VO 3.1 (video model; 20 credits per video), Claude (coding agent), Next.js, Tailwind CSS, HeroUI (library, formerly Hero UI), framer-motion, Motion.dev (motion library)

## [The Best MCP Servers of 2025](../videos/kRxdsv1ZY1E.md)
`kRxdsv1ZY1E` · AI LABS · 2026-01-02 · q2 · intro · review · also: mcp-and-tools, coding-agents

AI LABS roundup of six MCP servers for AI coding agents: Context7, Docker MCP, ShadCN, Google's managed servers, Notion and Supabase. Anecdotal, partly sponsored, and thin on measurements.

- Tools: Model Context Protocol (MCP), Context7, Ref, Docker MCP (MCP Find, MCP Add), Cloudflare code mode (concept), ShadCN registry MCP, shadcn components.json, Aceternity UI, Magic UI, Gemini 3, Google Maps MCP, BigQuery MCP

## [Google's Biggest Fail of the year](../videos/PB9sJnZyQ7g.md)
`PB9sJnZyQ7g` · AI LABS · 2026-01-02 · q2 · intro · review · also: coding-agents, testing-verification

A solo review of Google's Conductor, a Gemini CLI extension for spec-driven "track" workflows. The host finds the file layout sound but the command instructions weak, with destructive and falsely-completed steps.

- Techniques: Per-track spec + plan with a status index; Commit per task with git notes and git-aware revert; Default test gate on every task; Review each generated doc before auto-generation; Scope context updates to what changed; Verify completion against real state
- Tools: Conductor (Google Gemini CLI extension), Gemini CLI, Gemini (model), Claude Code plugins (mentioned as comparison), BMAD (recommended alternative), Supabase, npm, pnpm, git, git notes, GitHub

## [Anthropic Released A New Way To "Vibe Code"](../videos/XWp4k9K6oK8.md)
`XWp4k9K6oK8` · AI LABS · 2026-01-02 · q3 · practitioner · tutorial · also: coding-agents, agent-architecture, testing-verification

Anthropic's long-running-agent harness: an initializer agent sets up a JSON feature list, progress file and git repo, then a coding agent implements one feature per session with browser testing and commits, so work survives compaction.

- Techniques: Initializer + incremental coder harness; Forced browser verification via Puppeteer; Resume from state, not from context
- Tools: Claude Code, Claude.md, Puppeteer, Git, Next.js, BMAD

## [Claude Released Something To Fix Your Errors](../videos/NuKrtiJqW3Y.md)
`NuKrtiJqW3Y` · AI LABS · 2026-01-02 · q2 · practitioner · tutorial · also: testing-verification, coding-agents, voice-multimodal

Tips for testing web apps with Claude Code's Chrome extension: full-page screenshot scripts, CLAUDE.md context and cookie-banner rules, split test files, progress reports across compaction.

- Techniques: Full-page screenshot script behind a slash command; CLAUDE.md rule to limit DOM extraction; Cookie-banner dismissal script run first; Authenticate before handing off the task; Split end-to-end testing into per-area test files; Progress report after each test file; Compact and check context before browser test runs; Guided testing slash command
- Tools: Claude Code, Claude Code Chrome extension (Claude in Chrome integration), Playwright MCP, Puppeteer MCP, Google Chrome, Google Docs, Google Sheets, CLAUDE.md, Chrome Manifest V3 extensions

## [I Gave Claude Code Permanent Memory - The Results Are Shocking](../videos/EsFa7W-FYdM.md)
`EsFa7W-FYdM` · Better Stack · 2026-01-02 · q2 · intro · review · also: coding-agents, mcp-and-tools

Beads gives coding agents a git-synced issue tracker (SQLite locally, JSON Lines in git) so task state survives context resets. A 4-minute overview with claimed context savings and no measured results.

- Techniques: Repo-local issue tracker as agent working memory; Dependency-graph querying instead of loading planning docs; Compaction of closed issues; Spec first, then issues
- Tools: Beads, Beads MCP server, SQLite, JSON Lines, Git, Jira, SpecKit, Kiro, Claude Code, Sourcegraph, AMP

## [JSON Is Dead: TOON Saves Massive Tokens for LLMs and Changes Everything](../videos/r5u3ViTbWyc.md)
`r5u3ViTbWyc` · Better Stack · 2025-12-02 · q2 · practitioner · tutorial · also: token-cost-efficiency

Better Stack demos TOON, an indentation-based format with tabular arrays, cutting one JSON dataset from 1,236 to 454 tokens (~63%) in a TypeScript script. Strong for uniform records, weaker for deeply nested data; the evidence is a single dataset.

- Techniques: Benchmark a JSON-to-TOON conversion on your own payload before adopting it; Use TOON for uniform arrays of records, keep JSON for nested objects; Quick visual comparison with a web converter
- Tools: TOON (JSON-to-TOON format and encoder; installed via npm, captioned 'tune format slash tune'), gpt-3-encoder (GPT-3 tokenizer library used for token counts; captioned 'GPT-3 encoder'), TypeScript, npm, npx tsx, Node.js fs module

## [Building AI That Actually Helps You Live Better | Better Stack Podcast Ep. 7](../videos/46EsyQYKMjA.md)
`46EsyQYKMjA` · Better Stack · 2025-12-02 · q3 · intro · interview · also: security-guardrails, agent-architecture, mcp-and-tools

Better Stack podcast interview with Ben, founder of Spec, a macOS-native personal-context assistant; main engineering points are local-first data, OS-level access, and side effects gated outside the model.

- Techniques: Permission-scoped local data access for apps with no API; Split draft and send tools, with the send gated by a human click; Write-only agent sandbox; Event listeners and timed services instead of a single chat loop; Living context with distilled per-thread summaries as the trigger input; Route models by task type, separating persona from reasoning
- Tools: Spec (macOS/iOS app, Swift), Swift, Granola, Riverside, Claude Opus 4, Claude Sonnet 4, Claude Sonnet 4.5, Claude Haiku 4.5, GPT-5, GPT-OSS, Gemini 2.5, MCP

## [The Missing Layer in Your AI Stack: Supermemory](../videos/GETMfbGWc0k.md)
`GETMfbGWc0k` · Better Stack · 2025-12-02 · q2 · intro · review · also: memory, rag-retrieval

Walkthrough of Supermemory, a hosted persistent-memory layer with API, SDK, and proxy "memory router" modes, demoed on a Next.js chatbot over imported YouTube stats. Vendor-led; no evaluation of recall quality.

- Techniques: Memory via proxy base URL; Scope memory with a container tag; Force memory lookup with a system instruction; Memory as an agent tool via SDK; Bulk seed from tabular data; Write chat turns back as memories
- Tools: Supermemory (memory API, SDK, memory router proxy, dashboard memory graph), SuperMemoryTools SDK package, Vercel AI SDK, Next.js, OpenAI client, GPT-4 (as the provider in the demo), CSV (ingest format)

## [Claude Just Solved Their Biggest Problem](../videos/opZpIN8g_6M.md)
`opZpIN8g_6M` · AI LABS · 2025-12-02 · q3 · intro · review · also: mcp-and-tools, token-cost-efficiency, sandboxing-execution

Walkthrough of Anthropic's paper on running MCP servers as code files instead of direct tool calls, to cut context bloat; no implementation shown.

- Techniques: Filesystem-based MCP tool catalogue with progressive disclosure; Result shaping inside the execution script; Code-owned control flow between tool calls; Placeholder returns for sensitive data; File-based state for resumable runs
- Tools: MCP (Model Context Protocol), Claude, Claude skills, Memory tool, Cloudflare code mode, TypeScript, index.ts (file convention from the paper)

## [Gemini Designer is INSANE... Build Beautiful Websites in Minutes](../videos/v9Rd_l6gLjU.md)
`v9Rd_l6gLjU` · AI LABS · 2025-12-02 · q3 · practitioner · tutorial · also: vibe-coding-app-building, product-ux, coding-agents

Walkthrough of Google Stitch, an AI UI designer, plus a six-phase Klein rules-file workflow that turns exported Stitch HTML into a Next.js app and validates it against the designs.

- Techniques: Iterative screen-by-screen prompting in Stitch; Design-system extraction from exported HTML (phase 1); Per-page analysis and component library (phases 2-3); Navigation-flow mapping (phase 4); Blueprint-then-implement (phase 5); Validation checklist and scorecard (phase 6); Build from HTML, not screenshots
- Tools: Google Stitch, Klein (VS Code extension, multi-model, rules file, MCP store), VS Code, Next.js, Figma (via Klein's MCP store), ChatGPT (GPT-5 Temporary), Claude Pro, Material UI, Arc browser (example prompt)

## [Here's What They Didn't Tell You About Gemini 3](../videos/kyflIo3EKLw.md)
`kyflIo3EKLw` · AI LABS · 2025-12-02 · q2 · intro · review · also: models-research, coding-agents, vibe-coding-app-building

Hands-on review of Gemini 3 vs Claude and GPT-5.1 for UI generation and multi-phase coding; the speaker finds Gemini 3 strong at UI design but credits the agent harness, not the model, for most of the difference.

- Techniques: Same-spec head-to-head coding test; Separate model from harness; One-shot UI test with no guidance; Track context-window use per story
- Tools: Gemini 3 Pro, Gemini CLI, Google Antigravity (VS Code fork), Google AI Studio (Code Assistant), Claude 4.5, Claude Code, Claude desktop app, Claude canvas, GPT-5.1, GPT-5, nano banana (image model, named by the speaker)

## [Claude Just Introduced a New Way To Fix Your UI](../videos/eLDq5TfIHys.md)
`eLDq5TfIHys` · AI LABS · 2025-12-02 · q2 · practitioner · review · also: skills-self-improvement, claude-code, vibe-coding-app-building

AI LABS tests Anthropic's front-end design skill guidance in Claude Code: typography and theme prompts, a 400k-token mega-prompt, and skills that often fail to auto-load.

- Techniques: Turn a design prompt into a project skill; Force-invoke the skill by name; Describe design as implementation, not taste; Name the fonts explicitly; Stage the design prompt per dimension, then combine; Artifacts builder skill for componentized output
- Tools: Claude Code, Claude skills, Claude desktop app, Google Fonts, React, shadcn-style UI (as generated by Claude), Zen Browser, Arc Browser, Anthropic front-end design cookbook, Claude Code front-end design plugin

## [I Was Using Claude Skills Wrong... The Ultimate System](../videos/fHGMA8hLNt8.md)
`fHGMA8hLNt8` · AI LABS · 2025-12-02 · q2 · intro · review · also: claude-code, skills-self-improvement

A list of about 21 to 22 use cases for Claude Skills, from coding tasks like tests and CI/CD to business, personal and content workflows. Mostly unmeasured ideas, with a sponsor segment.

- Techniques: Skill folder with references, assets and scripts; Test-and-report skill; Clarify then generate; Template-driven document generation; Stateful skill with a maintained data file; Saved personal profile for planners
- Tools: Claude Code, Claude Desktop app, Claude Skills, Docker, GitHub Actions, npm package (unnamed), Appify (sponsor)

## [How to 10X Your Claude Code Workflow](../videos/xhrqmAWI_cw.md)
`xhrqmAWI_cw` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, claude-code, multi-agent

Walkthrough of a compound-engineering Claude Code plugin (plan, work, review, triage, codify, resolve commands) that persists to-dos and runs parallel review agents. Practical, but the 10X title is unmeasured.

- Techniques: Plan, work, review, triage, codify, resolve command loop; Built-in to-do tool as the phase ledger; Pause-per-phase human checkpoint; Context check before each phase; Language- and concern-specific parallel review agents; Dependency-graph parallel resolution of to-dos; Git ingest for Q&A on a repo; Install as a plugin via marketplace
- Tools: Claude Code, compound engineering (Claude Code plugin), Claude Code plugin marketplace, Claude Code built-in to-do tool, GitHub issues, git worktrees, git ingest, BMAD method (compared, not used), Next.js, FastAPI, Python, TypeScript

## [The PERFECT Design Workflow with Claude Code](../videos/9uFVCxfkLCo.md)
`9uFVCxfkLCo` · AI LABS · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building, coding-agents, mcp-and-tools

Walkthrough of capturing a website component with the Web2 MCP Chrome extension, cloning it one-to-one with a Claude Code/Cursor agent using a modified CLAUDE.md, and generating variants with SuperDesign. Mixed results, with a Rocket.new sponsor segment.

- Techniques: Capture an element with Web2 MCP and reference it by ID; Initialize SuperDesign rule files and edit CLAUDE.md for one-to-one cloning; Two-session workflow: clone first, then generate variants; Use SuperDesign's canvas view to inspect how a design was produced
- Tools: Web2 MCP (paid Chrome extension and MCP server; $2.50/month Pro tier as stated), MCP Pointer (open-source alternative, judged weaker), SuperDesign (superdesign.dev; editor extension with rule files for Cursor, Windsurf and CLAUDE.md), Claude Code, Cursor, Windsurf, Stagewise (mentioned as a prior featured tool), Arc browser, shadcn/ui (described as the common component library), Rocket.new (sponsor; no version), Netlify (mentioned in the Rocket.new segment)

## [Time to UPGRADE... Agent OS Replaces 95% of AI Coding](../videos/0rK4-8TryBo.md)
`0rK4-8TryBo` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, claude-code

Walkthrough of Agent OS for Claude Code and Cursor: base and tool installs, opinionated standards files, roadmap-driven builds, and spec/resume commands. Mostly one demo run; the 95% claim is unsupported.

- Techniques: Two-stage install; Edit the standards folder before the first plan; Plan-product prompt structure; Roadmap-driven build loop; create-spec for new features; Custom tool-routing rule for a component library; Resume with execute-task; Retrofit with analyze-product; Invoke rules by tool syntax
- Tools: Agent OS (spoken as AgentOS), Claude Code, Cursor, Next.js, pnpm, npm (avoided in demo), ShadCN UI, ShadCN MCP server, TweakCN (spoken as tweak cn)

## [How the 1% ACTUALLY Build Apps with Cursor's Context Engineering](../videos/QgA55EnmUp4.md)
`QgA55EnmUp4` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: coding-agents, vibe-coding-app-building

A hands-on workflow for building a full app with Cursor or Claude Code by splitting context into a PRD-generated docs folder, a short always-on rule, and a staged implementation plan.

- Techniques: Four-file documentation set generated from a PRD; Small always-attached workflow rule that routes to on-demand docs; Staged implementation plan with optional subtask lists; Put the foundations and scope into the generate prompt; Claude Code slash command for the generate step; Parallelize only independent work
- Tools: Cursor, Claude Code, CLAUDE.md, ChatGPT, Next.js, FastAPI

## [I Found the Simplest AI Dev Tool Ever](../videos/cQv3ocbsKHY.md)
`cQv3ocbsKHY` · Better Stack · 2025-11-02 · q3 · intro · review · also: coding-agents, token-cost-efficiency

Walkthrough of OpenSpec, a lightweight spec-driven development tool, building a small Vite/React charting app through a propose, review tasks, apply, archive loop with OpenCode.

- Techniques: Three-step spec loop; Project file bootstrap; Scope a change by editing its tasks; Track progress from the terminal; Apply and archive via slash commands; Parallel changes in separate tabs
- Tools: OpenSpec, OpenCode, Vite, React, Kiro, GitHub SpecKit

## [Goose + Qwen3 Is INSANE — Best AI Tool I’ve Tried So Far](../videos/thCFAzPJBZo.md)
`thCFAzPJBZo` · Better Stack · 2025-11-02 · q3 · intro · review · also: coding-agents, token-cost-efficiency

Better Stack reviews Goose, Block's open-source local coding agent, paired with Qwen3 Coder via OpenRouter; three small web apps built, with a hints file steering stack choices and a few real failure modes.

- Techniques: Point an open agent at a cheap open-weight coder via a routing gateway; Hints file for per-project or global conventions; Override defaults explicitly in the prompt; Iterate by feature request instead of re-specifying
- Tools: Goose (Block; open-source agent, CLI and desktop client; version not stated), Qwen3 Coder (coding model, called Quen 3 Coder in the transcript), OpenRouter (model gateway used as the provider), Ollama (local model runner Goose can use; not used in this video), Anthropic, OpenAI and Gemini (commercial providers Goose can connect to; not used in this video), Goose AI (named as an unrelated project; not reviewed), MediaPipe (hand detection library the agent chose), SQLite, Node.js, Express, VS Code, React

## [How I Build Beautiful Websites With AI](../videos/1cB2iqz_vnM.md)
`1cB2iqz_vnM` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: claude-code, coding-agents, vibe-coding-app-building

Walkthrough of Drawbridge, an open-source Chrome extension that turns clicks on a localhost page into a queued task list for Claude Code or Cursor, with landing-page and client-prototyping use cases. Main takeaway: UI fixes become batched, position-aware agent tasks.

- Techniques: Install Drawbridge as an unpacked Chrome extension; Queue element-level UI changes; Have the agent process the queue; Turn the Cursor workflow rule into a Claude Code slash command; Build a landing page section by section; Keep a design language in files the agent reads
- Tools: Drawbridge (open-source Chrome extension and visual editor for coding agents), Chrome (extensions, load unpacked), Cursor, Claude Code, shadcn/ui, TweakCN (shadcn theme site), Lumi (sponsored AI website builder), Git (used to revert the demo project)

## [Replit Has Become Essential to My Vibe Coding Workflow.](../videos/YtgqzCEeHVw.md)
`YtgqzCEeHVw` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, vibe-coding-app-building

Walkthrough of a vibe-coding workflow: Claude brainstorms and writes a no-code front-end prompt, Replit generates a shadcn-based responsive UI with exposed APIs, and Windsurf builds the FastAPI backend from the exported API docs.

- Techniques: Planning prompt with pages and modals; Front end first, API docs as the contract; Dependency and run step for a generated front end; Send browser context to the agent; In-memory storage first, database later
- Tools: Claude (Anthropic), Replit, shadcn/ui, Windsurf, Cascade, Cursor, v0, FastAPI, npm, SuperWhisper, macOS voice dictation, Supabase

## [The $10B System Prompts Behind Cursor AI and Others Just Leaked…](../videos/A5r2tfifYfY.md)
`A5r2tfifYfY` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, agent-architecture, sandboxing-execution

Walkthrough of leaked system prompts from Cursor, Windsurf, Replit, Manus and others, with the host's takeaways on tool design, background execution, memory, sandboxing and a repo-to-text trick. Useful as prompt-design evidence, but the verdicts are overreaching.

- Techniques: Repo subfolder to LLM-readable text; Post-edit verification loop; Background command execution with process status checks; Persistent memory with semantic auto-retrieval; Ask-for-secrets and stuck-fallback behavior; Sandbox-scoped guardrails in the system prompt
- Tools: Cursor, Windsurf (Cascade), Replit, Manus, Lovable, Devin, Bolt, Roo Code (transcript: 'Rucode'), Netlify, Next.js, shadcn/ui (transcript: 'Shad CNUI'), PostgreSQL

## [How to Use Cursor in the Smartest Way Possible](../videos/LXk8nWwOPuY.md)
`LXk8nWwOPuY` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: pr-code-review, coding-agents

A tutorial on pairing Cursor's agent with the CodeRabbit extension: commit each implementation chunk, run a review, feed suggestions back, and drive a phased implementation plan.

- Techniques: Commit-gated review loop; Branch-visibility workaround for missing reviews; One-comment-per-paste fix loop; Phase-by-phase plan with a structure file
- Tools: Cursor, CodeRabbit (VS Code / Cursor / Windsurf extension), Windsurf, Git, GitHub (CodeRabbit sign-in), Gemini 2.5 Pro, Next.js, FastAPI, shadcn/ui (spoken as 'shad cn')

## [Cursor AI Had a BIG PROBLEM — I Just Found the FIX](../videos/UngBxJ9uy70.md)
`UngBxJ9uy70` · AI LABS · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, coding-agents, multi-agent

AI LABS walkthrough of GitMCP, which turns any GitHub repo into a hosted MCP docs server, shown as an alternative to Context7 for keeping Cursor grounded in current docs, with a three-agent A2A demo.

- Techniques: Per-repo hosted MCP docs via URL swap; Scope docs to one repo instead of a broad doc index; Use the hosted repo chat as a post-build spec check; Router agent plus domain specialist agents over A2A; Routing check by server log
- Tools: Cursor, Gemini 2.5, GitMCP (gitmcp.io), Context7 MCP, MCP (Model Context Protocol), A2A (Google Agent-to-Agent protocol), Claude Desktop, Windsurf, VS Code, Claude, LangGraph (docs example), Three.js (demo project)

## [Shadcn Isn’t Just a Library Anymore… Here’s How to 10x Your UI](../videos/V8rGgwQ-VJ0.md)
`V8rGgwQ-VJ0` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: mcp-and-tools, vibe-coding-app-building

Shows how a shadcn/ui MCP server (component demos and blocks) plus Cursor rule files and a plan-first workflow produces better React UI, then how TweakCN restyles the result.

- Techniques: Fetch-before-build loop with the shadcn MCP; Rule file that forces the MCP lookup order; Plan first, with components named and no code; Theme with TweakCN after the structure is done
- Tools: shadcn/ui, shadcn UI MCP server (GitHub repo), Cursor, Claude (chat, used for the initial plan), Claude desktop MCP configuration, Windsurf, Claude Code, TweakCN, GitHub personal access token

## [What Cursor Doesn't Have: Claude Code Subagents](../videos/Ppu6pJ5yyD4.md)
`Ppu6pJ5yyD4` · AI LABS · 2025-11-02 · q2 · practitioner · review · also: claude-code, multi-agent, coding-agents

Walkthrough of Claude Code's native subagents: creating project agents with /agents, why isolated context windows help, and how auto-delegation and chaining work. Practical but thin, with a sponsor segment.

- Techniques: Create a project-scoped subagent with /agents; Write a specific description and scope tools tightly; Spec file plus rules file handed to a builder subagent; Theme swap through a subagent; Chain subagents in a custom slash command; Invoke a subagent explicitly
- Tools: Claude Code, Claude Code subagents (/agents), Cursor, ShadCN UI, ShadCN UI MCP server, Next.js, Tailwind CSS v3, TweakCN, TestSprite MCP server, BMAD workflow, SuperClaude workflow, GitHub subagents collection (unnamed)

## [Poml: Microsoft's Secret Tool for PERFECT AI Prompts](../videos/tfOwh6YCY8M.md)
`tfOwh6YCY8M` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: coding-agents, data-engineering

Walkthrough of POML, Microsoft's open-source markup language for prompts, showing components, data embedding, templating, and a script that generates an AGENTS.md file.

- Techniques: Compile a POML file to an API-ready message list; Embed a spreadsheet as a prompt data component; Parameterize a prompt with templating and Python context; Generate an AGENTS.md from style documents with a cheap model; Run a compiled prompt through a non-interactive coding agent
- Tools: POML (Microsoft open-source prompt markup language), POML Python SDK, POML TypeScript SDK (said to be unstable at the time), POML VS Code extension, OpenAI Python SDK, GPT-5 mini, GPT-5 nano, Codex CLI (non-interactive), Claude Code, OpenCode, Gemini CLI, LangChain

## [The EASIEST Way To Switch From ESLint & Prettier to Biome — Ultracite](../videos/lEkXbneUnWg.md)
`lEkXbneUnWg` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: dev-tools, coding-agents

Better Stack walks through Ultracite, a zero-config preset that sets up Biome (a Rust linter and formatter) with AI rule files, editor settings and pre-commit hooks in one init command.

- Techniques: Zero-config Biome bootstrap; Biome config that only extends the preset; Thin CLI wrappers for lint and format; Pre-commit format gate via Husky; Shift lint rules left into the agent's context; Expose rules through an MCP server
- Tools: Ultracite (npx ultracite init, lint, format), Biome (biome check, biome check --write), ESLint, Prettier, Husky, lint-staged, lefthook, Bun, shadcn/ui, VS Code, Cursor, Zed

## [How I ACTUALLY Use Claude Code... My Complete Workflow](../videos/7Sx0o-41r2k.md)
`7Sx0o-41r2k` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: claude-code, multi-agent, coding-agents

A host walks through a multi-agent Claude Code workflow for building an app: specialized sub-agents run in sequence, each writing its output to docs, with checkpoints for rollback and a generated agent-workflow setup.

- Techniques: Phased sub-agent chain driven by one prompt; Parallel sub-agent fan-out; Docs-first planning with scoped agents; Two-stage requirements before agent planning; Rewind with double-Escape checkpoints; Generate an agent workflow from a repo; Verbose view of sub-agent activity
- Tools: Claude Code, Claude Code sub-agents, Claude Desktop, Claude Opus, Cursor (checkpointing, as cited by the host), BMAD method, SuperClaude, gitingest.com, Next.js, UX researcher agent, sprint prioritizer agent, UI designer agent

## [How to Use Cursor AI with Its Own Cursor Memory Bank](../videos/azXNHRtzd5s.md)
`azXNHRtzd5s` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: memory, coding-agents

A short walkthrough of Cline's "Memory Bank" pattern: a set of structured markdown files that keep a coding agent's project context across sessions, set up in Cursor via pasted global rules. Practical but thin, with an admitted rules bug.

- Techniques: Paste a memory-bank rules file into Cursor User Rules; Initialize the memory bank with a single agent-mode prompt; Force plan-then-act with edit blocking; Keep the bank current in act mode
- Tools: Cline (Memory Bank, named 'Klein' in the transcript), Cursor (agent mode, User Rules, Cursor 2), Windsurf, Next.js, React Router, Unsplash API, Mermaid

## [3 Things Before You FINALLY Switch to Codex CLI](../videos/gRXrOuFn9dE.md)
`gRXrOuFn9dE` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, multi-agent

Hands-on comparison of Codex CLI against Claude Code: a single-prompt game test, the GUI options for each, an MCP workaround for missing sub-agents, and the BMAD planning method for multi-step builds. Sponsored intro; thin evidence.

- Techniques: Sub-agent delegation through an MCP server; Fork and patch an unmaintained community tool; BMAD-style plan-then-build workflow; Manual agent wiring for Codex; Edit MCP config from inside the Codex IDE extension
- Tools: Codex CLI (OpenAI), Codex IDE extension, GPT-5 Codex High (model used in the test), Claude Code, Phaser 3 (game engine), Kenney assets (spoken as Kenny), Three.js (spoken as 3.js), React, Next.js, shadcn/ui, Opcode (formerly Claudia), Conductor

## [GLM 4.6 Review: Better Than Claude for Coding? (Real Project Tests)](../videos/wEHWvzWOjt0.md)
`wEHWvzWOjt0` · AI LABS · 2025-11-02 · q2 · practitioner · review · also: coding-agents, token-cost-efficiency, models-research

Hands-on test of GLM 4.6 against Claude Sonnet 4.5 on a UI-design prompt and a multi-epic Svelte 5 build; GLM is far cheaper per message but needed Sonnet to finish integration.

- Techniques: Same-prompt model bake-off for UI work; BMAD epic-to-story decomposition for agent builds; Provision the backend through the database MCP; Commit per fix to attribute regressions to a model; Cheap model for most of the build, strong model for integration; Use a stack with thin training data as a stress test
- Tools: GLM 4.6, GLM 4.5, GLM coding plan (GLM Lite and Max tiers), Claude Sonnet 4.5, Claude Max plan, Claude Code, BMAD method, Svelte 5, Supabase, Supabase MCP, shadcn-svelte, CodeRabbit CLI (sponsor)

## [How to Make Cursor CODE What You ACTUALLY Want.....](../videos/Dv_tSxAA0HE.md)
`Dv_tSxAA0HE` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: coding-agents

A short Cursor feature tour: scoped project rules that replace the deprecated .cursorrules file, plus reusable prompts in Notepads, @web search, and custom doc indexing.

- Techniques: Global user rules for all projects; Scoped project rules with description and globs; Reuse community rule files; Reusable prompts in Notepads; Web search and custom docs in chat
- Tools: Cursor, Cursor Composer, cursor.directory, Supabase (examples/prompts repo), Next.js, TypeScript, Python, Tailwind, n8n, MCP (Model Context Protocol)

## [Why Your LLM Answers Are Mediocre (And How to Fix It)](../videos/Ym-iMJ-sds0.md)
`Ym-iMJ-sds0` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: memory, product-ux

Beginner tips for getting better LLM answers in ChatGPT (prompting, context windows, memory, Projects, deep research, Canvas), with a brief tour of Codex, Gemini CLI and Claude Code.

- Techniques: Specific, iterated prompting; Fresh chat per idea; Project system prompt with role and sample output; Escalate from web search to deep research; Canvas for partial edits
- Tools: ChatGPT, GPT-5, Claude, Gemini, Gemini CLI, Codex, Claude Code, Nano Banana, ChatGPT Canvas, ChatGPT Deep Research, ChatGPT Projects, ChatGPT Voice Mode

## [The Only Guide You Need to Build MCP Server.](../videos/kfTDFkhNDFU.md)
`kfTDFkhNDFU` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools, coding-agents

Walkthrough of building a minimal Python MCP server with the official SDK, wiring it into Cursor, and using docs and AI generation to wrap a web crawler and a Figma API.

- Techniques: Minimal Python MCP server; Register a local MCP server in Cursor; Feed SDK docs to the coding agent; gitingest to turn a repo into LLM context; Wrap an existing script as an MCP tool; API-to-tool generation from endpoint docs
- Tools: MCP Python SDK (mcp, installed with pip; no version stated), Cursor (agent, Composer, docs feature, MCP settings), Crawl4AI (open-source web crawler and data extractor), Figma REST API (get file endpoint), gitingest (gitingest.com, GitHub URL swap), GitHub (SDK repo, README)

## [Spec Kit: Github's NEW tool That FINALLY Fixes AI Coding](../videos/em3vIT9aUsg.md)
`em3vIT9aUsg` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: coding-agents, testing-verification

Walkthrough of GitHub's open-source Spec Kit, a four-phase (specify, plan, tasks, implement) spec-driven workflow for AI coding agents, shown building a small Pokedex app.

- Techniques: Four-phase spec-driven loop; Resolve 'needs clarification' blocks before planning; Put performance guardrails in the plan prompt; Track progress through the tasks file
- Tools: Spec Kit (GitHub open-source spec-driven toolkit with CLI, templates and steering prompts), GitHub Copilot (agent used in the demo), Claude Code (referred to as 'CloudCode' in the auto-captions; listed as a supported agent), Gemini CLI (listed as a supported agent), Amazon Kiro (earlier spec-driven framework, mentioned only), Grok Code Fast 1 (base model for the demo; auto-captions say 'grokcodefast1'), GPT-4.1 (comparison model, one run), Zod (schema library used in the generated data model), shadcn/ui (likely; auto-captions say 'Shotzi' for the UI library)

## [How Claude Solved AI's Biggest Problem](../videos/Z9glbip8pZc.md)
`Z9glbip8pZc` · AI LABS · 2025-11-02 · q3 · intro · review · also: claude-code, skills-self-improvement, mcp-and-tools

Walkthrough of Claude Skills: SKILL.md folders loaded on demand, how they differ from MCP, building one with skill-creator, and HTML visualization widgets. Mostly demo, with one sponsor segment.

- Techniques: Skill folder layout; Keep the description one line; push detail into referenced files; Install shared skills into Claude Code; Bootstrap a skill with skill-creator; Visualization widget skill
- Tools: Claude Skills, Claude Desktop app, Claude Code, skill-creator skill (Anthropic skills repo), MCP builder skill, MCP, Figma MCP server, Figma API, PDF Extractor skill, Algorithm art skill, Canvas design skill, Word, PDF, Excel and PowerPoint document skills

## [Turn Cursor AI into the 500$ Devin (Just Paste this...)](../videos/wJk2_Ds-9cM.md)
`wJk2_Ds-9cM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, skills-self-improvement

Walkthrough of a Cursor rules file that adds a lessons log and task scratchpad, used to build a full-stack Trello clone; one anecdotal demo with overstated "Devin" framing.

- Techniques: Per-project .cursor rules file; Lesson log inside the rules file; Scratchpad task plan with checkboxes and a current-focus section; Generate the rules prompt with another model, then run it in the IDE agent
- Tools: Cursor, Cursor Composer, Windsurf, Devin, GPT (used to write the prompt), PostgreSQL, Docker, OpenAI API (gpt-4 model name), Trello (clone target, not a tool used)

## [This Designer is INSANE... The Ultimate UI Setup](../videos/uayt-IVbh8E.md)
`uayt-IVbh8E` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, multi-agent, vibe-coding-app-building

Walkthrough of a Claude Code sub-agent pipeline for UI work: a UX agent drafts layout from requirements, a UI agent applies color variants, and a converter agent ports the HTML to SwiftUI.

- Techniques: Stage-separated UI sub-agent pipeline; Explicit agent count for variants; Split HTML output into HTML, CSS and JS files; Keep emoji placeholders, then fix icons in the target platform; Doc-grounded conversion guide via Context7, then bake into the agent
- Tools: Claude Code (sub-agents defined as markdown files), Cursor (mentioned in the intro as an AI coding tool, not used in the walkthrough), Context7 MCP, SwiftUI, iOS Simulator, HTML / CSS / JavaScript

## [How to use Reasoning Models Correctly?](../videos/w42_sbxa08w.md)
`w42_sbxa08w` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: models-research, multi-agent

Walkthrough of OpenAI's Reasoning Best Practices doc: keep prompts direct, skip chain-of-thought instructions, use delimiters, go zero-shot first, and use reasoning models as planners with cheaper models executing.

- Techniques: Section the prompt into Context / Examples / Instructions; Drop chain-of-thought scaffolding; Zero-shot first, then few-shot; Explicit constraints plus goal; Re-enable markdown in developer message (API); Planner/workhorse agent split
- Tools: OpenAI Reasoning Best Practices documentation, o1, o3-mini, GPT-4o, GPT-4o mini, Claude, Gemini, DeepSeek

## [Using this will make your AI AGENTS EVEN SMARTER!](../videos/2G-xavWw1bY.md)
`2G-xavWw1bY` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: rag-retrieval, token-cost-efficiency

A 5-minute tip for loading a whole GitHub repo into an LLM, either through a chat tool or a repo-to-text converter (gitingest), to answer questions and find install steps.

- Techniques: Repo URL swap into a chat-with-repo tool; gitingest repo-to-text conversion; Pick the model by token count; Explicit completeness prompting; Iterative setup questions on an ingested repo
- Tools: gitingest (named 'git ingest' in the transcript), DeepSeek (model, transcribed as 'DeepSeq'), Gemini (model), Cursor IDE, Claude (install instructions in the repo), GitHub, MCP server (example repo, unnamed)

## [This One Claude Code Feature Replaced My ENTIRE Team (Subagents)](../videos/zYPNfkDxgMg.md)
`zYPNfkDxgMg` · Better Stack · 2025-11-02 · q2 · intro · review · also: claude-code, multi-agent

Walkthrough of Claude Code's Custom Subagents (v1.0.60+): creating a read-only reviewer agent via the agents command, then running about ten subagents from one prompt, with token and time costs.

- Techniques: Create a personal-scope read-only reviewer subagent; Restrict a subagent to specific MCP tools; Delegate a task to a named subagent in the prompt; Batch several subagents in one prompt
- Tools: Claude Code (v1.0.60 or later, Custom Subagents), Claude Code agents command, GitHub (agent sharing), Claude Max subscription (speaker's plan; he notes the API would cost much more)

## [3 More Ways To ACTUALLY Build Beautiful Websites with Cursor IDE](../videos/U1_nzjWUpL4.md)
`U1_nzjWUpL4` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: vibe-coding-app-building, coding-agents, mcp-and-tools

Three practical ways to turn website designs into working Next.js UI in Cursor: a structured front-end spec prompt, a design.json built from screenshots, Browser MCP for cloning structure, and stagewise for precise element-level edits.

- Techniques: Structured front-end spec prompt; Screenshot to design.json style profile; Clone a site's structure with Browser MCP; Element-level UI edits with stagewise
- Tools: Cursor, Claude, ChatGPT, Claude Code, Next.js, Tailwind CSS, Browser MCP, stagewise, mcp.json, design.json

## [Build Apps with Cursor Like the 1% Using This NEW Method](../videos/OZaxtm3RyCw.md)
`OZaxtm3RyCw` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: coding-agents, agent-architecture

Walkthrough of building a wallpaper app in Cursor with Taskmaster AI: the PRD becomes a dependency-ordered task list the agent works through one task at a time, so one chat holds the whole build.

- Techniques: Install and initialize Taskmaster globally, then init per project; Configure keys in .env; Brainstorm with a no-edit instruction; Generate the PRD from an example template; Parse the PRD into tasks, then work them sequentially; Handle implementation drift with an explicit change list; Work in the correct subdirectory
- Tools: Cursor, Taskmaster AI, Claude (Anthropic API), Perplexity API, Unsplash API, Next.js

## [Generate Multiple Cursor Rules with ONE CLICK!](../videos/ztT6Bu1MPpY.md)
`ztT6Bu1MPpY` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents

Short tutorial on using Cursor Directory's generate-project-rules feature to turn package.json or requirements.txt into Cursor .rules files, with a UI demo and no evaluation of rule quality.

- Techniques: Generate project rules from dependency manifests; Generate rules per manifest in polyglot repos
- Tools: Cursor, Cursor Directory, Grok (named by the speaker as the generation model), Next.js, React, TypeScript, Tailwind CSS, FastAPI, SQLAlchemy, Obsidian (markdown MCP server example), MCP servers

## [Coding Test: Can CLAUDE COMPUTER USE Build Apps?](../videos/XbL5nzTLtag.md)
`XbL5nzTLtag` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, voice-multimodal

A short hands-on test of Claude Computer Use building a budget-manager app: it handled terminal setup but failed at front-end code generation, and a page refresh wiped the project.

- Techniques: Staged prompt decomposition for agent app builds; Verify toolchain installs in the agent's terminal; Keep recoverable copies of agent-generated work outside the agent's UI
- Tools: Claude Computer Use API, Claude (Claude 3.5 mentioned as the comparison model), ChatGPT (used to write and split the build prompt), Node.js, npm

## [3 Things I Wish I Knew Before using Claude Code](../videos/_9T-6dw-CZs.md)
`_9T-6dw-CZs` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: claude-code, mcp-and-tools, coding-agents

A beginner-level walkthrough of five Claude Code features: custom slash commands, Cursor integration with multi-line input, adding MCP servers (Sentry example), plan mode with CLAUDE.md, and the "ultrathink" keyword.

- Techniques: Custom slash command as a prompt file; Claude Code inside Cursor; Add an MCP server from an existing Cursor or Windsurf JSON config; Use MCP server commands from slash commands; Plan first, then save rules to CLAUDE.md; Add 'ultrathink' to a prompt for hard problems
- Tools: Claude Code, Cursor, Windsurf, Sentry, Sentry MCP server, Seer (Sentry AI agent), Claude Agent SDK, Claude GitHub app

## [Claude Sonnet 4.5 is HERE + Claude Code Upgrades](../videos/dDsa7_G7djc.md)
`dDsa7_G7djc` · Better Stack · 2025-11-02 · q3 · practitioner · news · also: claude-code, coding-agents, models-research

Better Stack's roundup of Anthropic's Claude Sonnet 4.5 launch and Claude Code 2.0 updates (VS Code extension, checkpoints, prompt history), with a one-prompt comparison against GPT-5 and Sonnet 4.

- Techniques: Rewind to a checkpoint in Claude Code; Search prompt history with Ctrl+R; Use the VS Code extension with editor context; Compare models on one prompt in the same harness; Enable context editing and the memory tool in the Claude API
- Tools: Claude Sonnet 4.5, Claude Sonnet 4, Claude Code 2.0, Claude Code VS Code extension, Claude Agent SDK (renamed from Claude Code SDK), Claude API context editing, Claude API memory tool, Imagine with Claude (research preview), Claude in Chrome extension, GPT-5, GPT-5 Codex, OpenCode

## [Cursor AI Shotgun Code (FREE): Fix Any Next.js App with AI (Full Tutorial)](../videos/4A66bMRiPQ0.md)
`4A66bMRiPQ0` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, vibe-coding-app-building

A walkthrough of Shotgun Code, which packs a whole Next.js repo into one prompt, gets a full diff from Gemini 2.5 Pro, and applies it in Cursor to overhaul a personal app.

- Techniques: Setup and launch from repo root; Curate the context before generating the prompt; Write one task plus custom rules into the packed prompt; Generate the diff in Google AI Studio; Apply the diff with a coding agent in chunks; Control visual style through the task text
- Tools: Shotgun Code (the GitHub repo demoed, a Go app with a frontend), Go, Node.js, Wails CLI (captioned as 'Wales'), Next.js, Google AI Studio, Gemini 2.5 Pro, Gemini Flash (mentioned as the option not to use), Cursor, Windsurf (mentioned as an alternative executor), Claude 3.5 Sonnet, shadcn/ui (captioned as 'shad cn')

## [Claude Engineer is INSANE... Upgrade Your Claude Code Workflow](../videos/6Rg5M69bMgQ.md)
`6Rg5M69bMgQ` · AI LABS · 2025-11-02 · q2 · intro · review · also: claude-code, coding-agents, mcp-and-tools

A walkthrough of two free add-ons for Claude Code: the SuperClaude configuration framework (slash commands, flags, personas, MCP-wired workflows) and a basic browser web UI for reaching Claude Code from other devices on the LAN.

- Techniques: Install SuperClaude from its GitHub repo; Have an AI write a usage guide from the framework's own config; Turn a phase into a runnable slash command plus prompt; Wire MCPs yourself, then reference them through flags; Reach Claude Code from a phone on the same LAN
- Tools: SuperClaude (configuration framework for Claude Code; no version stated), Claude Code, Cursor (used to read config and generate docs.md), Context7 MCP, Sequential MCP, Magic UI MCP, Puppeteer MCP, React, Next.js (spoken as 'xjs'), ElevenLabs API, OpenAI API, Warp (terminal, used to get the LAN IP)

## [Wait.. Claude Code is MADE Slow on Purpose? Heres How to Fix It](../videos/wYWyJNs1HVk.md)
`wYWyJNs1HVk` · AI LABS · 2025-11-02 · q2 · intro · review · also: claude-code, mcp-and-tools, token-cost-efficiency

Walkthrough of installing the Serena MCP (semantic code retrieval over a project index) and a Claude Code usage monitor, to keep Claude's context window focused and token use lower; the title's "made slow on purpose" claim is not supported in the video.

- Techniques: Per-project Serena MCP install; Index the project before using Serena; Prime Claude with Serena's instructions; Use the Serena dashboard for logs and clean shutdown; Track plan-window usage in a terminal tab
- Tools: Serena (MCP server for semantic code retrieval and indexing), Context7 (MCP for up-to-date library documentation), Claude Code, Cursor, Windsurf, uv (Python package runner used to install Serena), Claude Code usage monitor (terminal tool; name not stated in the transcript), Next.js, Python, Claudia and the Claude Code web UI (mentioned as alternatives)

## [People Are Getting RICH With AI Mobile Apps – Let’s Build One](../videos/HQJUvSLO91o.md)
`HQJUvSLO91o` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building, coding-agents

A walkthrough of building a macOS menu-bar Swift app by prompting Windsurf with a docs-first template and Gemini 2.5, after Claude failed on the same prompt; mostly process, with the prompt itself left in the video description.

- Techniques: Docs-first agent prompt for a new app; Scaffold the native project and place it in the agent workspace; Relay errors as text, and switch models for visual bugs; Turbo mode for unattended builds; Export a standalone macOS app from Xcode
- Tools: Windsurf, Cursor, Gemini 2.5, Claude 3.7, Claude, ChatGPT, Xcode, Swift, SwiftUI, Taskmaster (mentioned, as needing Claude and Perplexity API keys), Perplexity API (mentioned), Next.js (analogy only)

## [Context7 MCP Tutorial: Get Instant RAG for Your AI Coders](../videos/323l56VqJQw.md)
`323l56VqJQw` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools, coding-agents

Tutorial on wiring the Context7 MCP server into Cursor so the agent pulls current, targeted library docs instead of stale training data or whole doc files; the evidence is one informal before/after build.

- Techniques: Add Context7 as an MCP server in Cursor; Recover missing MCP tools; Pull targeted doc sections instead of attaching whole docs; Keep API keys out of agent context
- Tools: Cursor, Context7 MCP server (context7.com), mcp-use (auto-caption 'mcpus'; the Python agent framework built in the demo), Playwright MCP, Claude 3.7 (model named by the speaker), shadcn/ui (example library), Next.js (example framework), Windsurf, VS Code with GitHub Copilot agent, .cursorignore

## [Supabase MCP Cursor Integration (Step by Step)](../videos/b_hr1TB2GYQ.md)
`b_hr1TB2GYQ` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: mcp-and-tools, coding-agents

Step-by-step setup of Supabase's MCP server in Cursor so the agent can see the live database schema, with a connection-string walkthrough and a bash-wrapper trick. Anecdotal, short, and light on verification data.

- Techniques: Add Supabase MCP to Cursor via the command type; Wrap the MCP command in a bash script; Make the agent verify schema before and after each DB step
- Tools: Supabase, Supabase MCP server, Supabase CLI (`supabase status`, local instances), Cursor, Windsurf, Claude Desktop, GitHub MCP server, bash

## [Task Master AI Has Changed How I Code FOREVER (w/ Claude Code)](../videos/1I73OFAnvdg.md)
`1I73OFAnvdg` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: claude-code, coding-agents, software-factory

Better Stack walkthrough of Task Master AI with Claude Code: a PRD is parsed into dependency-tracked tasks, scored for complexity, expanded into subtasks, then run one at a time. The demo app built in one pass, but the claims rest on one example.

- Techniques: Pick models per Task Master role; Have the model write the PRD from an example template; Parse the PRD into tasks, then score complexity and expand the hardest tasks; Drive the work loop by task status; Keep project hooks in the loop
- Tools: Task Master AI (taskmaster / task-master-ai), Claude Code, Claude Sonnet, Claude Opus, OpenAI API, Next.js, IndexedDB, MCP (mcp.json), fish shell, Git, bun, npm

## [How I Build Apps 10x Faster with this 7-Step Cursor Workflow](../videos/cAFIUiE_8DM.md)
`cAFIUiE_8DM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, vibe-coding-app-building

A solo builder walks through a seven-step AI app workflow (idea, MVP, HTML prototype, design.json styling, SwiftUI conversion, Supabase backend, UI polish) for an iOS habit app, using Cursor and Claude Code.

- Techniques: Stage-gated AI app build; Screenshot-driven correction loop; design.json from a reference image; Rules-file-driven framework conversion; MCP-based backend provisioning; Image model for app icon iteration; Model switching by task
- Tools: Cursor, Claude Code, Claude (chat), ChatGPT, OpenAI image generation model, Supabase, Supabase MCP server, Supabase SDK, SwiftUI, Swift, Xcode, Next.js (mentioned as an example template)

## [Warp Code Tutorial: Save 90% of Time with Warp AI Agents (vs Claude Code) Agentic Development](../videos/STd07QswCpk.md)
`STd07QswCpk` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, multi-agent, mcp-and-tools

Sponsored walkthrough of building a full-stack notes app with Warp's agentic development environment, covering PRD planning, parallel agents split by API contract, saved prompts and rules, and MCP context.

- Techniques: PRD-first, then API contract, then fan out; Saved prompts as reusable commands; Templated workflows for known-hard setup steps; Rules to pin dependency and library behavior; Notebooks as context documents; Explicit task list for long runs; Parallel agent tabs with completion monitoring
- Tools: Warp (agentic development environment and terminal, with a built-in AI agent), Warp Drive (saved prompts, rules, MCP servers, workflows, notebooks), Context7 MCP, Playwright MCP, ChatGPT, Express Validator, Zod, Next.js, SWE-bench (vendor claim: 75.8%), Terminal Bench (vendor claim: #1)

## [Here Is How to Vibe Code Large Scale Projects](../videos/k9fPAzS5_Kw.md)
`k9fPAzS5_Kw` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: coding-agents, vibe-coding-app-building

AI LABS walkthrough of Plandex, a self-hosted CLI coding agent aimed at large projects: local Docker setup, chat-then-tell workflow, reviewable sandboxed changes, and one Swift app demo. Context-size claims are unverified.

- Techniques: Self-host Plandex in local mode; Set keys and initialize a repo; Chat to brainstorm and understand, then tell to implement; Review before applying, and debug failed commands
- Tools: Plandex, Docker, OpenRouter API, OpenAI API, Tree-sitter, Cursor, Xcode, Swift, SwiftUI, Gemini 2.5

## [Traycer is INSANE… Cursor AI is Not Enough Anymore](../videos/0hAS1xCeixQ.md)
`0hAS1xCeixQ` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, testing-verification

A product walkthrough of Traycer, an IDE extension that runs a planning stage (gap-filling questions, phased plan), implementation, and a self-review pass before or alongside coding agents such as Claude Code and Cursor.

- Techniques: Clarify-before-plan requirements file; Phased plan as the unit of execution; Plan handoff to a coding agent; Severity-classed self-review pass; Change tracking with M/N badges; Version-conflict repair by dependency pinning
- Tools: Traycer (IDE extension, sign-up required), Next.js, TypeScript, Tailwind CSS (v3 before the intentional upgrade), HeroUI (named as Hero UI), NextUI (mentioned as the wrong provider), shadcn (mentioned as a common library), Claude Code, Cursor

## [Bash Apps Are INSANE… A New Way To Use Claude Code](../videos/1_twhMU9AxM.md)
`1_twhMU9AxM` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: claude-code, coding-agents

Wrap any terminal CLI as a Claude Code agent via CLAUDE.md; builds a Git Agent on GitIngest and Click that stores repo context in the repo. Practical pattern, light on code.

- Techniques: Document a CLI as an agent tool in CLAUDE.md; Token-size gate before repo extraction; Persist extractions and analyses as repo files; Wrap an existing CLI in a Click command group; PRD-first build loop with Claude Code
- Tools: Claude Code, Claude Desktop, Cursor, GalleryDL, aria2, GitIngest (git ingest, open-source CLI with a GitHub URL mode), Git Agent (the speaker's own CLI wrapper, not released in the transcript), BMAD method (framework mentioned as a past featured video, not demoed), Click (Python CLI framework; auto-captions say Qlik), CLAUDE.md, ScaleKit (sponsor; OAuth and auth layer for AI apps)

## [I Built 5 Websites Without Touching HTML:  Here's How (Kibo UI)](../videos/6odlDS7-G8k.md)
`6odlDS7-G8k` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: vibe-coding-app-building, mcp-and-tools, coding-agents

Tutorial on wiring the shadcn MCP server and a custom 1100-component Kibo UI registry into a coding agent, plus TweakCN's live-embed theming flow for building Next.js UIs.

- Techniques: Wire the shadcn MCP into a Next.js or React project; Host a custom component registry from shadcn's registry template; Category-guided component selection for very large catalogs; Two-command design-first workflow (init once, build per session); Embed a TweakCN live theme preview into a Next.js app
- Tools: shadcn, shadcn CLI, shadcn MCP server, shadcn registry template, Kibo UI (patterns registry, ~1100 components), TweakCN, TweakCN MCP server, Next.js, React, Claude Code, Cursor, components.json

## [OpenAI Codex Hacked: Use It with Gemini 2.5 PRO (The Best Coding Model)](../videos/e3yxrNoC7mc.md)
`e3yxrNoC7mc` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents

Walkthrough of setting up a multi-provider fork of OpenAI's Codex CLI with Gemini 2.5 Pro, including config files and full-auto use, plus a failed full-scope attempt and a narrowed retry.

- Techniques: Swap the model behind a forked CLI agent; Persist per-project agent setup in files, not shell exports; Run the agent inside a git repo; Full-auto single-prompt build, then narrow scope on stall
- Tools: OpenAI Codex CLI, OpenCodex (community fork of Codex CLI, name as spoken in the video; exact package name not stated), npm, Gemini 2.5 Pro, Google AI Studio, Google Cloud, OpenRouter, Ollama, shadcn/ui, Next.js, Cursor (used as the editor to open config.json), git

## [I've Been Using the n8n MCP WRONG - The Correct Workflow](../videos/jUfpYmN9q6Y.md)
`jUfpYmN9q6Y` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: coding-agents, claude-code, mcp-and-tools

Driving the n8n MCP from Claude Code works better with a phased, file-based workflow: plan, research, build and validate in separate sessions, delete-and-recreate on update, and OAuth instead of API keys.

- Techniques: Phased file-based workflow pipeline; Clear context between phases; Put standing rules in CLAUDE.md; Pre-build version and health check; Delete-and-recreate instead of in-place update; OAuth-first credentials; Single-node isolation debugging; Documentation re-check prompt
- Tools: n8n, n8n MCP server, Claude Code, Claude Desktop, Claude.md (CLAUDE.md), OpenAI node in n8n, Google Calendar node, Gmail, Google Cloud Platform, Brave Search (from the previous video), Gamma (sponsor segment)

## [How to Use Figma AI To Make Sites 10X More Beautiful](../videos/_-FEgdQ_L4I.md)
`_-FEgdQ_L4I` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: vibe-coding-app-building, mcp-and-tools

A walkthrough of a prompt-chained Figma Make workflow for planning and generating a React app, then converting it with a coding agent and feeding Figma designs to agents through the Dev Mode MCP server.

- Techniques: Plan-first prompt chain for Figma Make; Universal full-stack conversion prompt; Figma Dev Mode MCP setup; Implementation-rules configuration file; Screen triage before implementation; Add shadcn MCP for component context
- Tools: Figma Make, Figma desktop app (Dev Mode), Figma Dev Mode MCP server (local and remote variants), ChatGPT (web interface, for planning and prompt outputs), Warp (Warp Code agent, referred to as Warpcode in captions), Supabase, React, Next.js, GitHub, shadcn MCP server, shadcn/ui, Aceternity UI

## [Sora 2 Cameos & Jailbreaks & Claude Agent SDK | Better Stack Podcast Ep. 5](../videos/YjdMscni2CI.md)
`YjdMscni2CI` · Better Stack · 2025-11-02 · q2 · intro · panel · also: claude-code, agent-architecture, voice-multimodal

Better Stack podcast: hosts riff on Sora 2's cameo feature, memorized training data and weak guardrails, then on the Claude Agent SDK for custom agents with their own prompts, tools and hooks. Mostly opinion.

- Techniques: Custom agent on the Claude Agent SDK with an owned system prompt; Local functions as agent tools in place of MCP tools; Hook-based output enforcement with automatic redo; Coaching agent that withholds answers
- Tools: Sora 2, VO3, Claude Agent SDK, Claude Code, Claude Code hooks, MCP, Claude Sonnet 4.5, Claude Opus, GPT-5, GPT-5 Codex, Codex, Grok 4

## [These Hidden Cursor Features Will Make You 10x More Productive](../videos/A9BiNPf34Z4.md)
`A9BiNPf34Z4` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: coding-agents, mcp-and-tools

A feature tour of Cursor's hidden productivity tools: global and project rules, notepads, indexed docs, MCP servers (Docker example), and YOLO mode for auto-running tools.

- Techniques: Global behaviour rules; Scoped project rules as .mdc files; Borrowing rule sets; Notepads as prompt templates; Web and indexed-doc references in Composer; Adding an MCP server in Cursor; YOLO mode with allow and deny lists
- Tools: Cursor, Cursor Rules (.cursor/rules, .mdc files), cursor.directory, Supabase (Postgres rule examples on GitHub), Tailwind CSS v4, Next.js, Better Stack docs, Model Context Protocol (MCP), Claude desktop app, docker-mcp (Docker MCP server, run with uvx), uv / uvx, npx

## [The BMAD Method: The Ultimate AI Coding System](../videos/fD8NLPU0WYU.md)
`fD8NLPU0WYU` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: multi-agent, coding-agents

BMAD Method tutorial: role-based agents (PO, scrum master, dev, QA) shard a PRD and architecture doc into epics and stories with approval gates, run in Cursor or Claude Code.

- Techniques: Two-document spec bootstrap; Shard then epic/story decomposition; Manual approval gate via story status field; Fresh chat per agent role; Story packet handoff; Learn an unfamiliar repo by feeding it to an LLM; Per-project install with npx; Asterisk commands and role switching
- Tools: BMAD Method (BMAD Code's agile workflow; version not stated), Cursor, Claude Code, Windsurf, ChatGPT, Claude, Gemini, GitIngest, npx (BMAD installer)

## [Amazon's NEW AI IDE is Actually Different (in a good way!) – Kiro](../videos/Z9fUPyowRLI.md)
`Z9fUPyowRLI` · Better Stack · 2025-11-02 · q3 · intro · review · also: coding-agents, software-factory

Walkthrough of Amazon's Kiro, a VS Code fork built around spec-driven development (requirements, design, tasks gated by the human) and event-driven agent hooks saved in the repo.

- Techniques: Staged spec gate before implementation; Spec re-sync after manual edits; Event-driven hook for doc or test upkeep; Steering documents
- Tools: Kiro, VS Code, Claude (Sonnet 3.7 and 4 model options), Cursor (comparison only), React, TypeScript, tRPC, Mermaid, Storybook, MCP servers, GitHub, Google login

## [Github Spec Kit FINALLY Fixed AI Coding](../videos/M0ivqkQ5mF4.md)
`M0ivqkQ5mF4` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: coding-agents, multi-agent, testing-verification

A walkthrough of GitHub Spec Kit's specify, plan and tasks workflow driving Claude Code on a demo app, with an honest verdict: the spec-first flow works, but tasks run by hand and the UI came out cluttered.

- Techniques: Requirements in a general chat model before spec-kit; Run /specify with the requirements and answer the clarification flags; Run /plan after the spec is settled; Run /tasks and write tests before implementation; Run independent tasks in parallel with sub-agents
- Tools: GitHub Spec Kit ("Specify"), Claude Code, ChatGPT, Gemini (supported assistant), GitHub Copilot (supported assistant), ShadCN UI components, Notion (visual theme followed), git

## [Windsurf vs Cursor: The AI IDE Battle](../videos/AD4BLcJf5Bg.md)
`AD4BLcJf5Bg` · Better Stack · 2025-11-02 · q3 · intro · review · also: coding-agents, token-cost-efficiency

Side-by-side walkthrough of Windsurf (Codeium) and Cursor, both VS Code forks: inline edits and tab completion are about even, while Windsurf's Cascade agent felt more context-aware and cheaper on paper.

- Techniques: Inline edit with a model picker; Terminal command prompt with undo context; Agentic scaffold with per-step accept and mid-run redirect; Continue-my-work after manual edits; Chat-only mode for AI suggestions without edits
- Tools: Windsurf (Codeium editor), Cascade (Windsurf agent: chat, write and terminal modes), Super Complete (Windsurf next-edit prediction), Cursor, Tab (Cursor next-edit prediction), Composer (Cursor agent), Claude 3.5 Sonnet, GPT-4o, React, Vite, create-react-app (rejected by the agent in the demo), Tailwind CSS

## [ShadCN Dropped Something to FINALLY Fix Your UI](../videos/mSMflOx5pq8.md)
`mSMflOx5pq8` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: mcp-and-tools, coding-agents, multi-agent

Tutorial on shadcn's official registry MCP: add extra community component registries, then run a multi-subagent workflow (requirements, component research, implementation) to build UIs without unnecessary components.

- Techniques: Install the shadcn registry MCP; Add third-party component registries; Preview a registry's visual style before using it; Three-stage subagent workflow for UI builds; Express agent for small changes; Port the commands to Cursor; Apply a TweakCN theme
- Tools: shadcn (CLI and registry MCP server), Claude Code, Cursor, VS Code, Next.js, React, npm, components.json, mcp.json, Aceternity UI, Origin UI, Neo Brutalism (registry, failed)

## [I Tried Building an Expo App in 360 Seconds… Here’s What Happened](../videos/Dmgu7jE2toM.md)
`Dmgu7jE2toM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building, coding-agents

Walkthrough of a two-tool flow for Expo mobile apps: Tempolabs generates the PRD, user flow and wireframes, then Cursor takes over the code via a synced docs folder. Single-project demo with no measurements.

- Techniques: PRD and user flow from a requirements prompt; Connect the builder to the IDE via the Tempolabs extension; Commit the spec into the repo as context for the coding agent; Route stubborn bugs to the agent that made the code; Verify gestures on a device, not the desktop preview
- Tools: Tempolabs, Cursor, Expo, Expo Go, Gemini 2.5 Pro, ChatGPT, Mermaid, Windsurf, Next.js, Supabase, Stripe, SSH

## [Google won't STOP... They Just Upped the Gemini CLI Again](../videos/A3AOeX1s7yw.md)
`A3AOeX1s7yw` · AI LABS · 2025-11-02 · q2 · practitioner · review · also: coding-agents, mcp-and-tools

A walkthrough of Gemini CLI's recent updates: free-tier quotas, MCP setup via settings.json, slash commands, VS Code inline diffs, and "extensions" as shareable bundles of context, MCP servers and commands.

- Techniques: Custom slash commands as TOML files for page and component generation; Adding MCP servers by editing settings.json; YOLO mode toggle for uninterrupted runs; Reviewing agent edits in VS Code via the IDE companion; Built-in session helpers; Packaging a team extension
- Tools: Gemini CLI, Gemini 2.5 Pro, ShadCN MCP (shadcn), Gemini CLI companion extension (VS Code), VS Code, Claude Code (compared, not demoed), Cursor (compared, not demoed), ChatGPT (used to draft the to-do app), TweakCN (theme source), Qwen (named as a competing free agent, no version), Skywork Super Agents (sponsor, not demoed)

## [How To Use Open AI Codex Absolute Beginners](../videos/KpZYZwaHBc0.md)
`KpZYZwaHBc0` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: coding-agents, software-factory

Beginner walkthrough of OpenAI's Codex CLI and cloud agents: approval modes, AGENTS.md, MCP setup, role-specialized agent files, and running background tasks that end in a GitHub PR.

- Techniques: Full Access approval mode for unattended runs; Model selection by task difficulty; Compact to manage context; Generate AGENTS.md with /init; Role-specialized agent files; Build MCP config from a repo-to-text dump; Cloud task per branch with PR handoff; Plan mode before implementation; BMAD-style planning loop
- Tools: Codex CLI, Codex IDE extension, Codex cloud (ChatGPT app), GPT-5, GPT-5 Codex (Low, High), AGENTS.md, config.toml, Claude Code, Claude Desktop, Cursor, ChatGPT, GitHub

## [Llama 4 Has a 10M Token Context Window... (and its the best)](../videos/xCxuNE2wMPA.md)
`xCxuNE2wMPA` · Better Stack · 2025-11-02 · q2 · intro · news · also: models-research, local-ai

Better Stack recap of Meta's Llama 4 launch: open-weight Scout and Maverick (MoE, 17B active) with a claimed 10M-token context, plus the unreleased Behemoth teacher model. All benchmark and efficiency claims are Meta's, repeated without independent checks.

- Techniques: Teacher-to-student distillation for deployable models; Sparse mixture-of-experts for cheaper inference; Three-stage post-training recipe
- Tools: Llama 4 Scout, Llama 4 Maverick, Llama 4 Behemoth, Llama.com, Hugging Face, OpenRouter, Groq (transcript says 'Grok'), LM Arena, GPT-4.5, Claude Sonnet 3.7, Gemini 2.0 Pro, Gemma 3

## [Generate The PERFECT App UI Every Time with this 2-Step Cursor Guide](../videos/H-ok6Zx9SR8.md)
`H-ok6Zx9SR8` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: vibe-coding-app-building, coding-agents

AI LABS tutorial on generating varied app UI designs inside Cursor with manually invoked rule files, replacing a paid-API design extension, with a Claude Code port and a plain-English method for writing rule files.

- Techniques: Manual-mode Cursor rule files as invocable workflows; Extract a design.json from a reference image; Targeted variation rules (persona, device, geolocation); Infinite-design iteration loop; Fresh chat per generation round; Writing rule files in plain English; Porting a rule to Claude Code custom commands
- Tools: Cursor (rules, agent, .mdc rule files), Super Design Dev (Cursor extension by Jason Zhao), Claude Code (custom commands, parallel agents), Claude 3.5 Sonnet, Anthropic Claude API

## [AI Coding with Cursor & Claude: Build Apps That People Keep Using in 5 Simple Steps](../videos/i_31WoayEIo.md)
`i_31WoayEIo` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building, product-ux, mcp-and-tools

Tutorial on building a photo-cleaner iOS app with Cursor and Claude: user journey saved in a markdown file, HTML prototype, palette, fonts, icon, Swift port and animations guided by Context7 docs.

- Techniques: Persistent context files in the repo; Specify the user journey first, then build an HTML prototype; Palette-from-elements prompt sequence; Google Fonts embed into the HTML prototype; App icon via ChatGPT image model with palette constraint; Context7 MCP for framework docs; Fresh chat per task plus Cursor to-do list; Two-stage animation pipeline; Screenshot-driven bug fixing
- Tools: Cursor, Windsurf, Lovable, bolt.new, Claude Code, Gemini CLI, Claude, ChatGPT, ChatGPT image model (called ChatGPT 4 image model in the video), Context7 MCP, Google Fonts, HTML

## [You Need Claude Sandboxes... 90% Faster AI Coding](../videos/xckU9n9r8Rs.md)
`xckU9n9r8Rs` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: coding-agents, multi-agent, software-factory

Walkthrough of running BMAD-planned stories in parallel with git worktrees and one Claude Code instance per subtask, with a QA agent review loop. The 90% title claim is not backed by the numbers shown.

- Techniques: BMAD planning-first pipeline; Prompt the story generator to split stories into non-conflicting parallel subtasks; One git worktree per subtask, managed through Conductor; QA review then fix loop per story; PR per story, merged by Claude Code
- Tools: BMAD method (planning agents, Scrum Manager, dev and QA agents), Claude Code, Claude Desktop, ChatGPT, Cursor, Conductor (multi-workspace UI for parallel Claude Code runs), git worktrees, GitHub, Next.js (initialized in story 1), OutSkill (sponsor segment, not used in the demo)

## [RAG Just Got Updated…](../videos/EgXOaH-ZqfU.md)
`EgXOaH-ZqfU` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: rag-retrieval, mcp-and-tools, coding-agents

Setup and demo of Archon, a beta self-hosted tool that gives Claude Code or Cursor project docs, a task backlog, and on-demand RAG over crawled docs via MCP. Includes a sponsor segment and an oversold title.

- Techniques: Local Archon stack setup; Project docs and backlog from a feature description; Rules-file-driven on-demand RAG; Crawl vendor docs into a knowledge base
- Tools: Archon, Claude Code, Cursor, Supabase, Docker, Docker Compose, MCP (Model Context Protocol), OpenAI API (embeddings), Google Gemini API (embeddings, free tier), SwiftUI, Xcode, Liquid Glass (Apple UI design)

## [Program Claude Code to be your new UI Designer (+ works with any IDE)](../videos/TyGx277x9hQ.md)
`TyGx277x9hQ` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: claude-code, vibe-coding-app-building, coding-agents

Walkthrough of using Claude Code plus ChatGPT planning to turn an HTML UI prototype into a SwiftUI iOS app and re-skin it in Apple's Liquid Glass style; practical but anecdotal.

- Techniques: Plan-in-chat, then execute in agent; Screenshot-to-HTML prototype; Conversion rules file; Style transfer from references; Visual bug reporting; Start from the native project template
- Tools: Claude Code, Claude 4 Sonnet, Claude Opus (Claude 4), Cursor (Max mode), ChatGPT, Xcode, SwiftUI, Swift, Next.js, HTML/CSS, iOS Simulator, Apple Liquid Glass design

## [AI Memory Explained: SuperMemory MCP for Cursor, Claude & Windsurf](../videos/mKXzPVIMFYE.md)
`mKXzPVIMFYE` · AI LABS · 2025-11-02 · q2 · intro · review · also: memory, mcp-and-tools

Walkthrough of SuperMemory MCP: one hosted memory store shared across Cursor, Claude Desktop and Windsurf through add and search MCP tools, plus an IDE rule that auto-saves project changes.

- Techniques: Cross-client memory via a hosted MCP server; Milestone summary saved to memory; Auto-sync rule for memory updates; Resume by searching memory first
- Tools: SuperMemory MCP, SuperMemory API, Cursor, Claude Desktop, Windsurf, Next.js, React

## [This Free Tool Makes Cursor 10x Smarter](../videos/52FC3qObp9E.md)
`52FC3qObp9E` · Better Stack · 2025-11-02 · q2 · intro · review · also: coding-agents, mcp-and-tools

Better Stack demo: Cursor's built-in docs indexing misses newer APIs, so adding "use context7" to a prompt fetches current library docs through an MCP server. Install is a single npx entry.

- Techniques: Install Context7 as a global MCP server in Cursor; Trigger doc retrieval with 'use context7' in the prompt; Manual doc snippet pull without MCP
- Tools: Cursor, Context7 (MCP server, run via npx; maintained by Upstash), Next.js 15.3 (onNavigate handler), Claude 3.5 Sonnet (model used in Cursor), MCP (Model Context Protocol), npx

## [Agents.md Is HERE… 90% of AI Tools Will Use This Now](../videos/Pmc4OfSlhbE.md)
`Pmc4OfSlhbE` · AI LABS · 2025-11-02 · q2 · intro · news · also: coding-agents, claude-code

Host argues OpenAI's AGENTS.md should become the single cross-tool agent context file, replacing per-tool rules files, and says Claude Code's absence is the gap. Includes a sponsor segment.

- Techniques: Single AGENTS.md as shared project context; Rely on the auto-loaded context file for session bootstrap
- Tools: AGENTS.md, CLAUDE.md, Model Context Protocol (MCP), Figma MCP server, Claude Code, OpenAI Codex, Gemini CLI, Qwen Code, Cursor, Windsurf, Kiro, GitHub Copilot

## [Build Sites That Sell 99% of Products with Claude AI](../videos/VtmBevBcDzI.md)
`VtmBevBcDzI` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: vibe-coding-app-building, claude-code

A landing-page design walkthrough: reverse-engineer a strong v0 site, then steer Claude Code with named libraries (paper shaders, Framer Motion), Google Fonts, layout screenshots and SVG code. Mostly a practical tip list with a sponsor segment.

- Techniques: Reference-site reverse engineering; Named-library prompt with a focused context; Framer Motion for animations; Two-step gooey morph; One-word font accent; Layout from a gallery screenshot; SVG logos and icons as code
- Tools: Claude Code, v0, Cursor (mentioned as a tool to use, no steps shown), Paper Shaders (library for animated website backgrounds), Framer Motion (React version named), GitIngest ("Git Ingest", converts a repo to AI-readable text), Google Fonts, Landbook (layout and design gallery), ChatLLM by Abacus (sponsor)

## [Claude FINALLY Fixed AI Coding By Releasing This](../videos/oj44Vrh0XyM.md)
`oj44Vrh0XyM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: claude-code, multi-agent, memory

Walks through four Claude Code context-engineering techniques from Anthropic's "Effective Context Engineering for AI Agents" paper: compaction, context editing and memory, structured note-taking, and subagents. Mostly a conceptual intro with small demos; the main takeaway is to pick the technique that fits the task.

- Techniques: Manual compaction with retain instructions; Persistent instruction via the # memory shortcut; CLAUDE.md as the project brief; Structured note files maintained by the agent; Coordinator plus specialist subagents
- Tools: Claude Code, Claude Sonnet 4.5, CLAUDE.md, Claude memory tool, ACI.dev Gate22 (open-source MCP gateway, sponsor), Anthropic paper: Effective Context Engineering for AI Agents

## [6 INSANE Repos I Wish I Knew Before...](../videos/tmj4_HhX7jI.md)
`tmj4_HhX7jI` · AI LABS · 2025-11-02 · q2 · intro · review · also: claude-code, mcp-and-tools, vibe-coding-app-building

Six-repo roundup for Claude Code and MCP: awesome-claude-code, BMAD agile agents, UI component libraries, GitMCP, FastAPI-MCP and mcp-use. Mostly quick pitches plus a mid-video sponsor segment.

- Techniques: Repo to remote MCP server via GitMCP; Expose FastAPI endpoints as MCP tools (fastapi_mcp); Use an MCP server from code with mcp-use; Repo dump into markdown as Claude Code context; BMAD staged agile agents; Pick UI components with the agent; Parallel Claude Code sessions and usage monitoring
- Tools: Claude Code, Claude Desktop, Claude Squad, Claude Code usage monitor, awesome-claude-code, BMAD method, Cursor, shadcn/ui (ShadCN), awesome-ui-component-library, Ant Design, Recharts, Next.js

## [I Built an App in 10 Minutes WITHOUT Coding! | Using Cursor Composer](../videos/LrIhNW2BN28.md)
`LrIhNW2BN28` · AI LABS · 2024-11-02 · q2 · intro · review · also: vibe-coding-app-building, coding-agents

Short Cursor promo that builds a budget tracker and a task app from plain-text requirements with Composer; shows multi-file generation, but the evidence is two cherry-picked demos.

- Techniques: Requirements file, then generate; Enable Composer before first use; Generate, then re-prompt for design, then fix bugs; Scope chat with @-references; Ctrl+K for local edits
- Tools: Cursor, Cursor Composer, Cursor Tab (completions), Cursor Chat (@-references), Cursor Ctrl+K inline edit

