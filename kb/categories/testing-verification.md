# testing-verification — 166 videos

*tests, verification, proving an agent is done, QA automation, TDD with agents*

By channel: AI Engineer 92 · Kai Explains 2 · AI LABS 47 · Better Stack 25

**Synthesized guide:** [guides/testing-verification.md](../guides/testing-verification.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [If Your AI Scores 100%, Your Eval Is Wrong - Ramakrishnan Lokanathan, eslams.com](../videos/7WUzHIF32vA.md)
`7WUzHIF32vA` · AI Engineer · 2026-11-01 · q3 · practitioner · talk · also: evals, observability

Ramakrishnan Lokanathan argues evals should test the job a system must do, not just a score: test every workflow step, add real failures as regression tests, and make tests harder as scores approach the ceiling.

- Techniques: Ambition-first eval scoping; Step-level workflow evals; Three-layer eval stack; Failure-to-regression loop; Ratcheting the test difficulty; Game-based multi-agent evals (eslams)
- Tools: eslams (open-source Python package, speaker's project, eslams.com), SWE-bench, Humanity's Last Exam, Nemotron 3 (the speaker says he was a red-teamer for these models), GPT-3, ChatGPT, Google Assistant, Gemini, Parallel AI search index (named as 'parallel search model index' in the captions), MIT GenAI Divide report (cited, not named as a tool)

## [I Made a Fruit Fly Review My Code - Nick Nisi, WorkOS](../videos/geMAe-PLJF4.md)
`geMAe-PLJF4` · AI Engineer · 2026-11-01 · q3 · intro · talk · also: pr-code-review, software-factory

Nick Nisi (WorkOS) demos a fruit-fly connectome trained to approve or reject code diffs, and argues humans should review for intent and proof of work, not bugs.

- Techniques: Team-owned review skill as a gate; Tiered PR escalation pipeline; Agent proof-of-work bundle for review; Measure the reviewer on a labelled diff set; LLM as structured feature extractor before a non-LLM classifier
- Tools: fruitfly.review (speaker's online demo of the fly reviewer; URL as spoken), Greptile (automated AI PR reviewer, named as a comparison), CodeRabbit (automated AI PR reviewer, named as a comparison), Codo (automated reviewer named in the pipeline; name as spoken, may be a caption error), Claude and Codex (named as coding agents that solved the coding problem), Pi (the speaker's coding agent, referenced via 'Pi extensions'; spoken name), GitHub code owners (used to route PRs to the DX team), GEV / JEV / CLEF (LLM and classifier names as spoken; likely auto-caption errors; the LLM is described as a 'System 1 model' that produces the 30 questions), Doom and Beat Saber (prior fruit-fly demos mentioned as context, not tools for the reader)

## [Anthropic Just Released A New System For Using Claude Code](../videos/S49gppZl8H0.md)
`S49gppZl8H0` · AI LABS · 2026-10-31 · q2 · practitioner · tutorial · also: claude-code, pr-code-review, multi-agent

Walkthrough of Anthropic's Claude Code review system, rebuilt as skills: eval.md gates before build, a fresh-context builder/verifier/reviewer loop, risk tiers, and git rollback.

- Techniques: Eval-first feature gating; Fresh-context builder/verifier/reviewer loop; Reviewer loop stop rules; review.md with a learned-rules section; Consequence-based risk tiering; First-time-user agent test; Git branch per feature with rollback
- Tools: Claude Code, CLAUDE.md, review.md, eval.md, state.md, Claude Code code review command, skills, subagents, hooks, git, Codex, Cursor

## [Your AI Agent Starts Every Session Like a New Hire - Killian Carlsen-Phelan, Sonar](../videos/8vDzncmzxyg.md)
`8vDzncmzxyg` · AI Engineer · 2026-10-31 · q2 · practitioner · talk · also: coding-agents, context-engineering, security-guardrails

Sonar pitches Vortex, a plugin that gives coding agents project context before they write and runs deterministic checks on every edit, so issues are caught before PR review.

- Techniques: Pre-write context retrieval from a verifier; Per-edit plus end-of-turn verification hooks; Enforce on changed lines only, surface the rest; Explicit-permission rule for sensitive resources; Deterministic layer between AI reviews
- Tools: Sonar Vortex (Sonar's agent plugin, named in the talk), SonarQube (static analysis, CI scan, data-flow and security analysis), Sonar CLI and MCP clients, Claude Code, Codex, Antigravity, Guitar (Sonar's AI reviewer, named in the captions; the speaker did not cover it), Java (language guidelines used in the demo)

## [Why Humans Can't Keep Up With AI-Written Code - Tariq Shaukat, Sonar](../videos/LQW_Wvqhp04.md)
`LQW_Wvqhp04` · AI Engineer · 2026-10-30 · q3 · practitioner · talk · also: software-factory, evals, governance-compliance

Vendor talk arguing AI-generated code makes volume cheap but confidence scarce, so software factories need intent, guide rails, independent verification and evidence, with LLM judges treated as unreliable.

- Techniques: Code confidence formula as a factory checklist; Guide rails over guard rails; Deterministic plus agentic verification mix; Measure judge stability before trusting an LLM judge; Model per-step reliability to pick task length
- Tools: SonarQube, Sonar Vortex, Claude Mythos preview (named as the model in the Meter study, version as stated in talk)

## [Catch the Bugs Your Code Review Misses - Killian Carlsen-Phelan & Taylor Luttrell-Williams, Sonar](../videos/wP3P89YB9fA.md)
`wP3P89YB9fA` · AI Engineer · 2026-10-30 · q2 · practitioner · review · also: pr-code-review, context-engineering

Sonar's hands-on workshop for Guitar, a PR-level verification agent that reviews agent-written code, diagnoses CI failures, auto-fixes and auto-merges. Vendor pitch with a usable setup walkthrough.

- Techniques: Install Guitar as a GitHub app and connect a repo; Fork the workshop repo with all branches and enable Actions; Open PRs against your own fork, not upstream; Apply Guitar fixes; Steer reviews with project context in .guitar/review; Write conditional rules in .guitar/rules; Turn on auto-merge safely with a branch ruleset
- Tools: Guitar (Sonar's code change verification agent, GitHub app, app.guitar.ai), SonarQube (called SonarCube in the transcript, static analysis), GitHub (PRs, Actions, branch rulesets, auto-merge), Jira, Linear, Slack, MCP (Guitar supports MCP connectivity for custom context), Python (sample Box Office ticketing app, orders.py, check-in.py)

## [How Anthropic Merges 30,000 Code Changes a Day - Manish Kapur, Sonar & Addy Osmani, Anthropic](../videos/AnsXWH2_EBU.md)
`AnsXWH2_EBU` · AI Engineer · 2026-10-29 · q3 · practitioner · panel · also: pr-code-review, software-factory, governance-compliance

Sonar and Anthropic discuss verification as the bottleneck for agent-written code, covering layered checks, codified taste in CLAUDE.md/AGENTS.md, labeling agent PRs and the lights-on vs dark software factory spectrum.

- Techniques: Verification-first agent loop with a first-pass reviewer; Codify taste in CLAUDE.md or AGENTS.md for review agents; Require verification evidence before human review; Layered verification stack; Label agent-authored PRs and keep a named human owner; Agent guide rails and permission control
- Tools: Claude Code (called 'Cloud Code' in the transcript), Claude (claude.ai web product), Opus 5.5 (Anthropic model, named as a reference point for model quality), Anthropic code review product (named only as a product Anthropic offers), CircleCI (cited statistic), Sonar (verification vendor; survey and product referenced), CLAUDE.md / AGENTS.md (agent instruction files)

## [How to Test Your Agents on Real Tasks With Harbor - Xander Song, Arize AI](../videos/kRJjSOYqW0I.md)
`kRJjSOYqW0I` · AI Engineer · 2026-10-27 · q4 · practitioner · talk · also: evals, observability, coding-agents

Xander Song (Arize) introduces Harbor, an open-source framework for testing agents on real tasks in fresh sandboxes, scored by side-effect verifiers, and shows how his team used it to tune a prompt for SQL over GraphQL.

- Techniques: Harbor task layout; Oracle-first validation; Keep verifiers outside the agent's view; Synthetic task and oracle generation; Before/after prompt A/B in a fixed harness; Read-only SQL tool for aggregates; Single-node app snapshot in Docker; One-turn skill-triggering test
- Tools: Harbor, Docker, Arize Phoenix, OpenInference, OpenTelemetry, OTLP, ATIF (Agent Trajectory Interchange Format), Daytona, Modal, E2B, SQLite, Postgres

## [How to Build an AI Code Review Agent - Daksh Gupta, Greptile](../videos/4UtrRVtUN_g.md)
`4UtrRVtUN_g` · AI Engineer · 2026-10-26 · q4 · practitioner · talk · also: pr-code-review, context-engineering, token-cost-efficiency

Greptile co-founder Daksh Gupta walks through building a production AI code review agent: sandboxed test runs, historical bug catalogs, model inversion, a living code wiki for context, and tiered model routing to cut per-PR cost.

- Techniques: Prompt the reviewer for a catalog of bug types, not generic review; Historical-PR regression eval for the review agent; Model inversion for reviews; Codebase knowledge base indexed by subsystem; Dependency-rich sandbox with computer-use end-to-end tests; Tiered model routing across review subtasks; Model-agnostic harness for the review agent
- Tools: Firecracker, OpenCode, Pi, Codex, Claude Code, GitHub review API, GitHub, GitLab, Jira, Linear, Confluence, Notion

## [Your Agent Fix Just Broke Something Else - Sofia Jakovcevic, Arize AI](../videos/v5tm5EAzsAs.md)
`v5tm5EAzsAs` · AI Engineer · 2026-10-25 · q3 · practitioner · talk · also: evals, observability, multi-agent

A five-step regression loop for agents built on production traces, evaluators and CI gates, so a prompt or policy change is judged on numbers before it merges. Vendor-led demo of Arize.

- Techniques: Five-step trace-driven regression loop; Four-bucket dataset composition; LLM-as-judge plus code evaluators; Side-by-side prompt versions in a playground; Agent playground against a remote agent; Run experiments from coding agents through skills; CI gate on experiment results
- Tools: Arize (Arize AI observability backend and platform, incl. prompt hub, prompt playground, agent playground, experiments, datasets), Arize agent skills repository (public, for coding agents), GitHub Actions (CI example), Arize SDK / REST / CLI (run experiment), LLM-as-judge evaluators (pre-built: hallucination, user frustration, security checks; custom evaluators supported)

## [Don't Trust Your AI Agents. Test Them Like a Scientist — Stephanie Jarmak, Omni Analytics](../videos/A3FL_zTQKU0.md)
`A3FL_zTQKU0` · AI Engineer · 2026-10-23 · q4 · practitioner · talk · also: evals, observability, governance-compliance

Stephanie Jarmak (Omni Analytics) argues agent evals should be done like experiments: check the tool pipeline end to end, match the benchmark to your own workload, decouple flags from enforcement, and trust independent traces.

- Techniques: Tool-use pipeline audit; Harness-plus-model pairing as the unit under test; Workload-representative internal benchmark; Explicit metric choice per use case; Separate flagging from enforcement; Independent record comparison for trust; Shadow deployment and production measurement; Autonomy boundary spec for each action
- Tools: Amp (coding agent), Sourcegraph code search MCP tool, Claude (as used in the grep example), grep, Terminal Bench (transcribed as 'Terminal Bench 4'), OpenHands (open coding-agent harness), Opus 5 (model, as transcribed), Astra (model or harness, as transcribed; unverified), Code Scale Bench (speaker's own public benchmark for large codebases), LLM-as-judge (generic pattern), Omni Analytics evaluation harness (in progress)

## [Does Code Quality Still Matter? It Depends on This — Max Kanat-Alexander, Capital One](../videos/bU5gDVyu_28.md)
`bU5gDVyu_28` · AI Engineer · 2026-10-22 · q3 · practitioner · talk · also: software-factory, context-engineering

Max Kanat-Alexander (Capital One) argues code quality only matters for durable software: it's worth rigor when consequences, replacement cost, dependencies and maintenance are high, and rigor is cheaper when you standardize and automate it.

- Techniques: Place software on a durable-to-disposable spectrum; Make software more disposable on purpose; Standardize to reduce the cost of rigor; Build in-workflow tooling; Provide in-memory fakes for services; Turn lint rules to maximum from the start
- Tools: Chromium (example codebase), Linux (example Hello World)

## [Anthropic Just Revealed How Their Engineers Use Claude Code](../videos/92ZDgn8bgLM.md)
`92ZDgn8bgLM` · AI LABS · 2026-10-22 · q3 · practitioner · tutorial · also: claude-code, context-engineering, multi-agent

AI Labs video on Felix Rieseberg's article: get more from Claude Code by asking for outcomes, expert methods, varied viewpoints, an outside judge, and the tools to verify results.

- Techniques: Outcome-first prompt (altitude); Expert-method meta-prompt (depth); Impossible-sounding goal reframing; Outside judge via a second model; Noun-to-verb role discovery and sequential specialist sub-agents (range); Verification resources for agents
- Tools: Claude Code, Claude (Anthropic), Codex CLI, MCP (Model Context Protocol), GoLogin (sponsor segment, not a recommended tool), AI Labs Pro (paid community, mentioned in closing)

## [Vercel's CEO Just Unveiled The Greatest AI Coding Workflow Ever](../videos/y2ifUC9_zuU.md)
`y2ifUC9_zuU` · AI LABS · 2026-10-20 · q2 · intro · tutorial · also: context-engineering, claude-code, security-guardrails

Recap of a Vercel CEO interview: judge progress by direction rather than volume, run a plan-drift "direction" check, and use breaker, first-time-user and E2E agents plus MCP-based feedback triage. Partly a sponsor segment, with thin detail.

- Techniques: Direction drift-check command; Specs-first project setup; Must-not-trade-off rules with runnable tests; Quality gate checklist; Breaker agent loop; First-time-user agent with a hook-restricted bash tool; E2E path agent with JSON results; DeepSec security scan; Feedback triage with MCP connectors
- Tools: Claude Code, CLAUDE.md, DeepSec (Vercel security scanner), Gmail MCP, Sentry MCP, Victor (sponsor, AI hire in Slack/Teams)

## [GitHub's #1 Trending Skill Is Insane (5 Use Cases)](../videos/rw0fqnrZgNM.md)
`rw0fqnrZgNM` · AI LABS · 2026-10-19 · q2 · practitioner · review · also: claude-code, skills-self-improvement, security-guardrails

Walkthrough of the Reverse Engineer Anything (REA) MCP skill for Claude Code: feature cloning, black-box QA, competitor teardown, security sweep. Takeaway: tag findings by evidence, not guesses.

- Techniques: Behavior spec before implementation; Evidence-tagged findings; Black-box feature QA; Check the site against your written rules and promises; Competitor teardown; Pre-publish security and performance sweep
- Tools: Claude Code, Codex, Reverse Engineer Anything (REA) MCP server and skill, Hopper (binary analysis, optional), Firecrawl MCP server (sponsor), Notion MCP, Obsidian, Notion, OpenAI API, Stripe, GitHub

## [Google Just Fixed AI Design By Releasing This](../videos/au2TI8sdq8E.md)
`au2TI8sdq8E` · AI LABS · 2026-10-19 · q3 · practitioner · tutorial · also: coding-agents, context-engineering, skills-self-improvement

Google's Stitch design tool now has a terminal CLI, so Claude Code can drive it through a brief-to-design-to-site workflow with review and story-review skills; the video is a tutorial-style walkthrough with a sponsor segment.

- Techniques: Stitch CLI install with the skill in .claude; brief.md interview before any design generation; Loop of generate, check, and re-prompt in Stitch; Build from Stitch via download of HTML, images and fonts; Two-stage review: design fidelity, then story quality
- Tools: Stitch (Google), Stitch CLI, Claude Code, Stitch skill, scrollytelling skill, design.md, brief.md, Whisperflow (sponsor)

## [Teach Your Agent to Prove It's Done — Nick Nisi & Zack Proser, WorkOS](../videos/q4WC4TowkBo.md)
`q4WC4TowkBo` · AI Engineer · 2026-10-18 · q3 · practitioner · workshop · also: evals, coding-agents, context-engineering

Build deterministic verifier CLIs and evidence "receipts" so coding agents can prove their own work is done, closing the loop without the human reading every line of code.

- Techniques: Per-app verifier CLI with subcommands; Deterministic end-to-end prove step with Playwright; System-one LLM judge for fuzzy outcomes; Doctor/preflight plus stale-proof detection; Centralized verifier gate on workflow nodes (CTX); Babysitter agent for PR follow-through; Generate many variants and select via eval; Saboteur/detective bug-injection test of the verifier; Evidence attached to PRs; Outcome-first prompting with clear stop conditions; Error messages written for agents; Post-deploy monitoring agent
- Tools: Playwright, Chrome DevTools, pnpm, GitHub CLI (gh), GitHub API, Cloudflare Workers, MCP, Reptile, CodeRabbit, Datadog, Claude Code, Pi

## [Evals for High-Stakes AI Agents — Doneyli De Jesus & Annabell Schäfer, Langfuse](../videos/obfPzbapMIM.md)
`obfPzbapMIM` · AI Engineer · 2026-10-18 · q3 · practitioner · workshop · also: evals, observability, governance-compliance

Langfuse workshop on evaluating high-stakes agents: trace everything, build datasets from production via expert error analysis, mix LLM-judge with deterministic evaluators, and gate prompt changes in CI.

- Techniques: Annotation queue for expert error analysis; Free-text comments to failure-mode taxonomy via LLM; Mixed evaluator suite (LLM judge + code checks); Prompt-promotion-triggered CI eval gate; Mask PII before persisting traces; Shadow runs for ground-truth building; Judge calibration against a human-labeled sample
- Tools: Langfuse, GitHub Actions, ClickHouse, PostgreSQL, Amazon S3, OpenAI chat API, Anthropic models, Whisper Flow, Claude, Langfuse skill (agent skill)

## [How to Know If Your AI Agent Is Any Good: Evals With Phoenix & Claude — Laurie Voss, Arize AI](../videos/SHMCGrNJJGc.md)
`SHMCGrNJJGc` · AI Engineer · 2026-10-17 · q4 · practitioner · workshop · also: evals, observability

Hands-on workshop: trace a Claude financial-analyst agent in Phoenix, read failures, write code and LLM-judge evals, validate judges against human labels, run experiments, and gate CI on them.

- Techniques: Deterministic code eval with structured input; Faithfulness judge with full retrieval context; Five-part LLM judge prompt with constrained labels; Judge hygiene: different-family, stronger judge, suppressed tracing; Open coding then axial coding of traces, with a coding agent; Golden dataset with dev/test split by stable ID; Run experiments on the failing subset only; pass^k reporting for nondeterministic agents; Vitest-based eval suite gated in CI; Eval-driven development
- Tools: Arize Phoenix, Claude Agent SDK, Claude Code, Claude Sonnet 5.5, Claude Haiku 4.5, Claude Haiku 5.5, Vercel AI SDK, OpenTelemetry, OpenInference, Vitest, GitHub Actions, TypeScript

## [Stop Chatting With Spreadsheets — Francesco Galletta & Felippe Felisola Caso, Monzo](../videos/e9-br9hveRI.md)
`e9-br9hveRI` · AI Engineer · 2026-10-17 · q3 · practitioner · workshop · also: agent-architecture, governance-compliance, data-engineering

Hands-on workshop on building a trustworthy financial-analysis harness around five principles (shared domain, deterministic calculations, evidence, accountability, verification), demoed on a wedding-budget planner.

- Techniques: Interview-style shared-domain planning with a decision tree; Calculation-as-code with tests and golden examples; Fact / assumption / interpretation labelling with provenance; Branching challenge agent with merge or dismiss; Tiered accountability gates
- Tools: Claude Code, Codex, Looker Studio, Google Slides, Google Sheets

## [The Cost of Accessibility in AI — Jemima Abu, CAIS](../videos/ZccJsdOE54M.md)
`ZccJsdOE54M` · AI Engineer · 2026-10-15 · q3 · intro · talk · also: context-engineering, skills-self-improvement, product-ux

Jemima Abu (CAIS) argues accessibility is cheaper when built in from the start with AI agents, backed by a one-off experiment (58% lower cost, one-third the time) using a custom accessibility skill.

- Techniques: Accessibility skill for coding agents; Pre-run self-audit against a checklist; Audit the codebase before introducing an agent; Reusable component library as an accessibility lever
- Tools: Figma, Chrome Modern Web Guidance skill, WebAIM (cited study)

## [I Believe Everything My Agents Tell Me: Three Levels of Review — Corey Gallon, Rexmore](../videos/dYh7TQkuYFE.md)
`dYh7TQkuYFE` · AI Engineer · 2026-10-14 · q4 · practitioner · talk · also: multi-agent, evals

Corey Gallon (Rexmore) presents a three-level agent review method, each level built as a skill, that catches agents overstating work, misreading facts, and reasoning errors, shown on three real cases.

- Techniques: Deliverable contract with a self-check the sender runs; Fan-out / fan-in with independent identical agents and a source-anchored adjudicator; Control-total anchoring; Claim labeling self-audit; Cold persona reviewers with no context; Fresh-reviewer final pass

## [Please… Enough with the Sloppy, One-Shot SaaS Replacements — Mahmoud Abdelwahab, Railway](../videos/oixzVKMAXG0.md)
`oixzVKMAXG0` · AI Engineer · 2026-10-13 · q3 · practitioner · talk · also: product-ux, coding-agents, skills-self-improvement

Railway's Mahmoud Abdelwahab on why agent-built internal tools feel broken: agents skip product polish (autosave, optimistic updates, undo, URL state) unless asked, so encode taste in skills, reference existing pages, and force end-to-end verification.

- Techniques: Pattern-following via existing abstractions; Named UX patterns as explicit asks; Reference-page anchoring; Taste packaged as skills; End-to-end verification loop
- Tools: Railway, Payload CMS, TanStack, Claude Code

## [This Just Fixed Your Claude Code Setup's Biggest Flaw](../videos/jlEMo6Dsh9E.md)
`jlEMo6Dsh9E` · AI LABS · 2026-10-12 · q2 · practitioner · review · also: claude-code, context-engineering, token-cost-efficiency

Walkthrough of eight Claude Code add-ons, mostly from one vendor, that put an LLM yes/no judge at decision points: action gating, rule checks, stop gates, message routing, compaction, file shortlisting and SEO audits.

- Techniques: Judge-gated pre-action hook (Toolgate pattern); Rules-to-rubric compilation (Abide pattern); Completion gate with a confidence threshold (Belay pattern); Three-way routing of mid-run messages (Steer/Queue/Interrupt); Advised compaction timing; Shortlist-then-read file retrieval (Quicksilver pattern); Browser-driven test pass with judge verdicts; Site audit with a fixed checklist plus per-page judgment
- Tools: Claude Code, Codex, Jev (decision model; name as transcribed, provider TypeSafe), Toolgate, Abide, Jev Browser, Jev Belay, Jev Steer/Queue, Compact Advisor, Quicksilver, Jev SEO, OpenRouter

## [Build with Perception Agents — Emile Baizel & Shruti Arora, Amazon AGI Lab](../videos/ZGzthw4BZiA.md)
`ZGzthw4BZiA` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: voice-multimodal, coding-agents, mcp-and-tools

Amazon AGI Lab hands-on workshop on Nova Act's open-sourced perception primitives: point-and-annotate a live page into JSON, run Gherkin-based visual verification, and wire both to a coding agent.

- Techniques: Deterministic visual annotation to JSON; Gherkin user flows auto-generated from a surface crawl; Browser extension to coding agent bridge; Automatic verification after every agent change; Voice or wearable transcript as an annotation source
- Tools: Amazon Nova Act, Nova Act SDK, Nova Act MCP server, Visual Annotator (Chrome extension), Visual verification skill, Claude Code, Kiro, Gherkin, Chrome, uv / uvx, Jam MCP, Atlassian MCP

## [Everything is Open Source Now (Reverse Engineer Anything)](../videos/jtfpCGsbSJU.md)
`jtfpCGsbSJU` · Better Stack · 2026-10-12 · q3 · intro · news · also: software-factory, coding-agents

Better Stack commentary on Artcraft, a viral open-source Adobe clone, and a "reverse engineer anything" MCP; the host tests Opus 5.5 rebuilding a 1990s pinball game in Rust with sub-agents and verification passes.

- Techniques: Reference-driven port with source-address traceability; Fresh-context verification pass after a fan-out; Verifiable-goal loop (test suite as the spec); Clean-room rebuild from public specs and observed behavior
- Tools: Artcraft, Photocraft, Vectorcraft, Filmcraft, Adobe Photoshop, Reverse Engineer Anything (MCP, GitHub), Hopper, Ghidra (transcribed as 'Geirdre'), IDA, Claude Opus 5.5, Rust, Pinball Space Cadet (original EXE from Internet Archive)

## [How to Build Quality Gates into Agentic Coding Workflows — Nnenna Ndukwe, Qodo AI](../videos/-AKPRSYccJc.md)
`-AKPRSYccJc` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: pr-code-review, context-engineering, coding-agents

Hands-on workshop by a Qodo DevRel on wiring codified rules, skills, structured plans and deterministic gates into an agentic coding loop from planning through PR review and autofix.

- Techniques: Codified rules and skills pulled per phase; Structured high-level plan plus execution plan; Read-only plan mode with an explicit skill handoff; Local verification command as the gate; Audit skills during implementation; Review-findings autofix loop; Severity-tiered rules with merge blocking
- Tools: Qodo, Claude Code, Codex, Semgrep, Ruff, Pyright, Bandit, pytest, GitHub CLI, uv, conventional commits, git worktrees

## [SonarQube + OpenAI: Agentic Development — Killian Carlsen-Phelan, Sonar](../videos/bI8WyG9YB0I.md)
`bI8WyG9YB0I` · AI Engineer · 2026-10-12 · q3 · practitioner · demo · also: coding-agents, security-guardrails, context-engineering

A Codex deployment engineer and a Sonar developer advocate argue that agent "done" needs evidence, containment is not correctness, and feedback checks belong inside the agent loop, then demo SonarQube hooks, MCP and CLI wired into Codex.

- Techniques: Evidence-backed definition of done; Layered execution and artifact controls; Secret-blocking lifecycle hook; Guide, verify, solve loop (ACDC); Taint analysis across files; Changed-code-only verification for agent edits; Custom rules targeting agent-written code
- Tools: Codex (OpenAI coding agent CLI), SonarQube Cloud, SonarQube CLI, SonarQube MCP server, SonarQube Codex plugin / marketplace, Docker, Git Bash (for setup script)

## [1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Run Code — Kevin Orellana, AWS](../videos/k72eLcYpVys.md)
`k72eLcYpVys` · AI Engineer · 2026-10-12 · q4 · practitioner · talk · also: sandboxing-execution, mcp-and-tools

Kevin Orellana (AWS) has a coding agent fuzz-test a sandbox hosting platform with about 1,000 workflows, and shows how sandbox primitives like memory, file persistence and permissions cause failures.

- Techniques: Agent-driven fuzz testing of a sandbox platform; Results in SQLite, not markdown; Two-layer failure triage; Build a workflow suite that mirrors customer workloads
- Tools: MCP, SQLite, Amazon Bedrock AgentCore, SSH, Codex, Claude Code

## [Software Costs Millions to Make but Claude Cracked It in Seconds. (Pt - 1)](../videos/hl6VOfzky5E.md)
`hl6VOfzky5E` · Kai Explains · 2026-10-12 · q4 · practitioner · news · also: models-research, token-cost-efficiency, software-factory

Kai Explains on where AI reverse engineering works: it succeeds when an automated answer key (byte-exact compile match, a test or a crash) grades each attempt, and the headline numbers hide that.

- Techniques: Build the oracle before the loop; Compile-and-byte-compare decompilation loop; Reconstruct the toolchain first; Keep the reference when changing the target; Report pass@1 and pass@k with the budget; Track API-equivalent cost next to subscription spend
- Tools: Ghidra, objdiff, Claude Sonnet, Claude Opus, Claude Max plan, GPT-6 Astra, GPT-5.6 Sol, SREBench, FFmpeg, Photocraft

## [Stop Prompting — Greg Pstrucha, Sentry](../videos/E3KbFLAGD6A.md)
`E3KbFLAGD6A` · AI Engineer · 2026-10-10 · q3 · practitioner · talk · also: context-engineering, coding-agents, pr-code-review

Sentry's Greg Pstrucha argues teams should stop re-prompting coding agents and instead codify repeated conventions as deterministic lint rules, skills checks, and policy-driven review loops.

- Techniques: Mine feedback to find lint-worthy rules; Custom AST lint rules with ast-grep or ESLint-style tools; Lint for schema sync; Validate code examples inside skill documents; Policy files plus per-policy sub-agent review loop; Hooks to run deterministic checks at the right moment
- Tools: ast-grep, ESLint, OxLint, Flake8, Clippy, Claude Code skills, OpenAPI schema, Django REST Framework, a plain-English lint tool transcribed as 'TaskLessware' (name uncertain from auto-captions)

## [Evals in AI: A Deep Dive — Tejas Kumar, IBM](../videos/NdrSPm6NCdk.md)
`NdrSPm6NCdk` · AI Engineer · 2026-10-06 · q4 · practitioner · workshop · also: evals, rag-retrieval

Tejas Kumar (IBM) walks through evals as fuzzy unit tests for non-deterministic agents, then builds an LLM judge live, calibrates it against hand-labelled data, and gates CI on human agreement.

- Techniques: Judge calibration loop against a golden set; Pointwise pass/fail judging; Bias probes for judges; CI agreement gate; Pin the judge model version; Living eval dataset from production traffic; Cheapest-first eval ladder; Adversarial and synthetic eval generation; Avoid fuzzy string matching on LLM output
- Tools: Vitest, Cursor, GPT-3.5 Turbo, GPT-4o-mini, Docling, OpenSearch, OpenRAG (IBM), LM Arena

## [Your LLM Judge Is a Confident Liar: Building Better Verifiers — Browserbase](../videos/xLxhT2ZI7UM.md)
`xLxhT2ZI7UM` · AI Engineer · 2026-10-06 · q4 · practitioner · talk · also: evals, training-finetuning-rl, voice-multimodal

Browserbase and Microsoft researchers on why LLM judges confidently mis-grade web agents, and their rubric-and-evidence "universal verifier" that agrees with humans far better, plus its use for filtering training data.

- Techniques: Rubric-first LLM verification; Per-criterion top-K screenshot evidence; Dual verdict: partial-credit score plus boolean outcome; Controllable vs uncontrollable failure schema; Error isolation across dependent criteria; Human-agreement validation with held-out labels; Verifier as data filter for SFT; Auto-research loop to build a verifier, primed with human findings
- Tools: WebVoyager, Online Mind2Web (captioned as 'Online Minor Web'), OSWorld, GPT-4o, Opus 4.6, Cohen's kappa, Browserbase, Microsoft open-source web-agent framework (captioned 'StateGen')

## [Lifestyles of the AI-Native — Nick Nisi & Zack Proser, WorkOS](../videos/AgBAOXVxt4A.md)
`AgBAOXVxt4A` · AI Engineer · 2026-10-06 · q3 · practitioner · workshop · also: claude-code, coding-agents, context-engineering

WorkOS engineers run a hands-on workshop on operating fleets of Claude Code agents: voice dictation, goal vs loop, verification hooks, Codex adversarial review, worktrees and scheduled tasks.

- Techniques: Goal with a measurable done condition; Loop for recurring or open-ended monitoring; Checksum-verified evidence of test runs; Hook-enforced gates; Cross-model adversarial review; Retrospective agent with curated memory; State machine for ordered steps; Git worktrees for parallel agents; Interactive first, then schedule; Session fleet management; Triage automated PR review output by score
- Tools: Claude Code, Codex CLI, Handy, WhisperFlow, Granola, Greptile, CodeRabbit, Devin, Linear, Slack, tmux, Fleet (nicknesey/fleet)

## [From Vibes to Production: Evaluating and Shipping AI Agents That Work 101 — Laurie Voss, Arize AI](../videos/qZj7sqmidqA.md)
`qZj7sqmidqA` · AI Engineer · 2026-10-06 · q3 · intro · workshop · also: evals, observability

A two-hour Arize AI workshop on replacing "vibes" with measurement: read traces, write code and LLM-judge evals, calibrate the judges, then close the loop with experiments.

- Techniques: Error analysis (open then axial coding); Code evaluator on trace or span; Context-matched LLM judge; Rubric structure for LLM judges; Judge calibration with golden labels; Test both directions; Experiments on a fixed dataset; Evaluator split by dimension, with guardrail vs north-star labels; Online sampled evals at span or trace scope; Eval-driven development and data priorities
- Tools: Arize AX, Arize Phoenix, OpenInference, OpenTelemetry, Claude Agent SDK, Anthropic Claude Haiku (agent model), Anthropic Claude Sonnet 4.6 (judge model), Claude Code, Cursor, Codex, Arize Skills (npx install), Alex (AX built-in eval agent)

## [He Finally 10x Claude Code With This Method](../videos/qLfSDQ5NGh0.md)
`qLfSDQ5NGh0` · AI LABS · 2026-10-05 · q3 · practitioner · tutorial · also: claude-code, skills-self-improvement, multi-agent

Walkthrough of a Karpathy-style loop for Claude Code: frozen checks, fresh builder subagents, and an outer loop that rewrites instructions from failure logs. The "10x" claim is not measured.

- Techniques: Loop-fit test before building a loop; Project-context skill as app memory; Write, review, approve, lock, and commit checks; Fresh feature-builder subagent per feature, with a results file; Karpathy-style keep-or-undo loop with program.md; Outer auto loop that rewrites instructions from failures; Wire-up and sweep instructions
- Tools: Claude Code, Karpathy autoresearch (Auto Research), Upstash Box (sponsor; per-agent cloud sandbox), Approve Checks (custom script), program.md, features.md (feature tracking file), results file (custom per-round log), Project Context skill (custom), build skill (custom), write checks skill (custom), auto loop skill (custom), feature builder agent (custom subagent)

## [Scale the Judgment, Not the Model — Andrew Orobator, Reddit](../videos/6MudaeKdBSk.md)
`6MudaeKdBSk` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · also: skills-self-improvement, software-factory, context-engineering

Reddit's Andrew Orobator on scaling agent judgment rather than model size: encode institutional judgment as skills, work logs, personas and hard gates, verified by recordings, so coding agents can ship with less human review.

- Techniques: Skills as encoded review judgment; Work log plus commit-hook enforcement; Persona prompting for perspective; Recording-based agent QA; Rules-first funnel for LLM cleanup; OS-level gate with operator-only bypass; Three operating modes; Scheduled skill drift audit
- Tools: Codex, git pre-commit and commit hooks, CI, lint, screenshot-based model review

## [The Death of the Code Review: What the Data Actually Says — Laurie Voss, Arize AI](../videos/_mi3alkqy4s.md)
`_mi3alkqy4s` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · also: pr-code-review, evals, observability

Laurie Voss (Arize AI) argues that agent code generation has outrun human review, so teams should stop reviewing PRs by hand and build an engineered review harness, with humans designing its definition of good.

- Techniques: Multi-pass review with consensus filtering; Default-suspicious reviewer prompt; Tool-using reviewer over the whole repo; Runtime verification by the agent itself; Machine-checkable mergeability rubric; Codify the definition of good as a harness
- Tools: GitHub Copilot code review, Cursor reviewer, CodeRabbit, Greptile, Graphite, Codex, Anthropic automated security review action, SWE-bench, SWE-bench Pro, FrontierBench

## [Why AI Didn't Actually Make You Ship Faster — Gabriel Spencer-Harper, Meticulous](../videos/HLTa7Vcs4X0.md)
`HLTa7Vcs4X0` · AI Engineer · 2026-10-04 · q2 · intro · demo · also: pr-code-review

A short vendor demo arguing that review and verification, not code writing, are now the bottleneck, and that screenshot-based record-and-replay of front-end flows can give near-exhaustive verification.

- Techniques: One-line record of real user flows in non-prod; Per-step screenshot diff of base vs PR; Record-time network mocking with replay-time stubs; Coverage-maximizing test subset selection
- Tools: Meticulous, Cypress, Playwright

## [How VS Code Went from Monthly to Weekly Releases with AI — Harald Kirschner](../videos/I2LL_wd89-A.md)
`I2LL_wd89-A` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · also: software-factory, pr-code-review, context-engineering

How the VS Code team moved from monthly to weekly releases by rebuilding its own dev system around agents: code-survival metrics, agent-readable repos, fast CI, UI feedback loops, AI triage, and staged rollouts.

- Techniques: Code survival metric; Agent-readable repo docs; Expert knowledge as a shared skill with an area owner; Screenshot-diff component browser; Self-correcting launch loop; Tiered AI code review; Deterministic filtering before agent action; Staged rollouts with error monitoring; Evals bootstrapped from issues; Prototypes instead of PRs for design talks
- Tools: VS Code, GitHub, GitHub Issues, GitHub Copilot code review, TypeScript Go, Playwright, Electron, Xcode MCP, AGENTS.md, Chrome extension

## [Why 99% Accurate Browser Agents Still Fail — Derek Meegan, Browserbase](../videos/5xi_S1f9sDU.md)
`5xi_S1f9sDU` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: voice-multimodal, agent-architecture

Why 99%-accurate browser agents still fail in production, and how moving deterministic steps out of the model and verifying outcomes makes transactional browser workflows profitable.

- Techniques: Three browser interaction strategies; Transactional scope for browser agents; Per-transaction success with bounded retries; Artifact-based success check; Single-transaction tool encapsulation; Deterministic auth outside the model; Skill as SOP for the critical path
- Tools: Browserbase, Chrome DevTools Protocol (CDP), OCR, accessibility tree, serverless functions

## [What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory](../videos/vGCJ7diEtrw.md)
`vGCJ7diEtrw` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · also: software-factory, infra-cost-scaling, context-engineering

Factory's engineer defines a "software factory" as a full autonomous lifecycle, not coding agents. Covers model routing for cost, verifiable done-criteria, sequential worker and validator missions, deferred tool loading, and codebase readiness.

- Techniques: Difficulty-classified model routing; Validation contract written before coding; Sequential workers with fresh context per handoff; Two-tier validation; Deferred tool loading; Codebase readiness audit; Codify tacit rules as skills or plugins
- Tools: Factory (software factory platform), Factory missions (orchestrator, worker and validator agents), Automatic model routing, Deferred context engine, Agent readiness framework, Plugins, Auto-wiki, Slack, GitHub, Figma, Notion, Gmail

## [Shopify Just Released The Greatest AI Coding Workflow Ever](../videos/bBMp5tLxShQ.md)
`bBMp5tLxShQ` · AI LABS · 2026-10-02 · q2 · practitioner · tutorial · also: software-factory, multi-agent, claude-code

AI LABS rebuilds Shopify's checkpoint-and-gates agent loop as a Claude Code orchestrator skill; the key idea is enforcing gates with a stop hook, not advisory rules.

- Techniques: Checkpointed build with human plan approval; Stop-hook gate; Test-first behavior gate without a browser; Prototype-driven visual gate; Adversarial critic and fixer loop; Learnings file for cross-task feedback; Single orchestrator entry skill
- Tools: Helix (Shopify internal, not released), Claude Code, Claude sub-agents, Gemini (used by Shopify as UI reviewer), Hedra MCP server (sponsor segment), design.md, Ralph loop (transcribed as RALF), AI LABS orchestrator skill (their own), Checkpoint Planner agent (their own), tdd planner skill (modified, their own), prototype skill (their own), adversarial loop skill (their own)

## [React-Native Is Dead... Thanks to AI.](../videos/r0u83Ss7QRc.md)
`r0u83Ss7QRc` · Better Stack · 2026-10-02 · q3 · intro · news · also: software-factory, coding-agents, dev-tools

Better Stack commentary on Shopify dropping React Native for native apps, with Shopify's Helix checkpoint-gated agent loop and headless app logic for fast agent testing. Opinion-led, relays Shopify's blog post.

- Techniques: Checkpoint-gated agent migration (Helix pattern); Headless state plus CLI driver for agent testing; Avoid out-of-process UI automation for agent verification
- Tools: React Native, Shopify React Native packages (FlashList, React Native Skia, Restart), Helix (Shopify in-house agent migration system), Swift, Kotlin, SwiftUI, CloudKit, Apple XCUITest

## [Grok Bot Use Cases That Are Actually Insane](../videos/90pwPVrydHg.md)
`90pwPVrydHg` · AI LABS · 2026-10-02 · q2 · intro · review · also: multi-agent, voice-multimodal, product-ux

Walkthrough of GrokBot's eight use cases: a hosted, always-on bot group sharing one logged-in browser, used for app testing, support triage, monitoring and AI-search checks. Light on setup detail; sponsor and paid-tier plugs.

- Techniques: Role-bot test fan-out with a lead bot; Backend-verified UI failure triage; Agent-triggered test round; Support email to draft reply and PR; Fresh-account onboarding audit; Unbranded AI-search visibility check; Scheduled morning monitoring routine; Coordinator bot over functional bots
- Tools: GrokBot, Grok, SuperGrok, Cursor, Hermes, Claude Code, Codex, Supabase, Stripe, Gmail, Sentry, GitHub

## [Insane GitHub Repos That 10x Your Codex And Claude Code Setup](../videos/Ua0APTMVcb8.md)
`Ua0APTMVcb8` · AI LABS · 2026-10-02 · q2 · intro · review · also: coding-agents, skills-self-improvement, token-cost-efficiency

AI LABS tours eight GitHub tools that extend Claude Code and Codex setups: browser verification, terse output, design-skill search, planning, skill evals, and linting. Mostly README-level, with one sponsor segment.

- Techniques: Browser-verified completion check (Reticle); Staged image-to-3D reconstruction with self-comparison; Terse-output plugin with lifecycle hooks (Chisel); MCP-attached design skill search (UISkills); Interview-plan-review-verify loop (Ouroboros); Apple-native skill pack for iOS UI; Skill evaluation with Caliper; Rule-based anti-pattern guard (Antislop)
- Tools: Image-to-3JS skill (spoken 'image to 3JS', captioned 'Image23JS'; GitHub trending per the presenter), Reticle, Chisel, Caveman, Ponytail, UISkills, Manufact (sponsor; hosted MCP server deployment and publishing checks), mcp-use open-source SDK (captioned 'MCPUs'), Ouroboros, Apple SwiftUI skills repo (Liquid Glass skill, layout skill), Liquid Glass (Apple iOS 26 design system), Claude Code (plugins, hooks, Skill Doctor command)

## [Autoresearch Made Our Models 3x Faster — Tejas Bhakta, Morph](../videos/vrDvatGtIxs.md)
`vrDvatGtIxs` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: inference-serving, agent-architecture

Morph's Tejas Bhakta shows a propose-benchmark-keep-or-revert loop (autoresearch) tuning GPU kernels for about 3x speedup, with human-supplied ideas and explicit guards against reward hacking.

- Techniques: Keep-or-revert benchmark loop; Split the work: human ideas, loop parameters; Profile before tasking the agent; Hardware and model context files in the harness; Explicit anti-cheat rules in the benchmark; Stack kernels and keep fallbacks; Switch models when one fails at the DSL
- Tools: Nsight Systems (NSYS), CUDA, CUDA graphs, CuTe DSL, CUTLASS, FlashInfer, NVFP4, Autoresearch (Karpathy)

## [Fixing the PR Bottleneck — Matt Pocock, AIHero](../videos/LlgiOCmFG_w.md)
`LlgiOCmFG_w` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: pr-code-review, software-factory, context-engineering

Matt Pocock on clearing the PR backlog that AI agents create: layer cheap deterministic checks, have an agent review and commit fixes, design deep modules so tests stop being brittle, and run a retro on each session.

- Techniques: Layered brakes for agent PRs; Deep-module design for agent-testable code; Separate implementer and reviewer contexts; Reviewer commits fixes, comments only on open questions; Door-type and blast-radius PR summary; Pseudocode and diagram PR explanations; Retro over sessions and PRs
- Tools: AGENTS.md, coding-standards.md, CodeRabbit, Cursor BugBot, PlanetScale, Opus 5 (model mentioned in the tautological-test example), AIHero skills (version 1.3 announced for the same week)

## [One Designer + AI. Hundreds of Deliverables. — Vincent Wendy, AI Engineer](../videos/O1FN4awNEtM.md)
`O1FN4awNEtM` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: product-ux, context-engineering

A solo designer at AI Engineer uses agents (Devin, GPT, Figma) to produce hundreds of conference deliverables by fixing design tokens first, automating data-driven outputs, and checking results with an agent.

- Techniques: Tokens-first design system for agents; Annotated spec sheet as handoff; Single data source to many assets; Agent as checklist QA on visual output; Vision-based photo matching; Raster first, then vectorize
- Tools: Devin, GPT, Figma, MCP, Slack, PNG export, Figma spec-sheet plugin

## [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../videos/5Bn0xro2ol8.md)
`5Bn0xro2ol8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, coding-agents, context-engineering

Figma engineer on rolling out coding agents across an org: verification-first testing, plan-before-prompt with phase validation gates, and labeling AI-written text so reviewer attention is spent well.

- Techniques: Verification-first agent workflows; Encode agent discoveries as deterministic tests or flows; Testing pyramid for agent-written code; Red-green prompting; Why-first phased plan with validation gates; Human-first labeled communication; Agent-in-thread invitation
- Tools: Playwright MCP, Slack, cloud coding agent (unnamed)

## [Building ambitious software — Jonathan Kelley, Dioxus Labs & Cognition](../videos/H7vFrcNWXzs.md)
`H7vFrcNWXzs` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: coding-agents, context-engineering

Dioxus Labs (now part of Cognition) on building an ambitious Rust framework with coding agents: fast on knowledge work and mundane upkeep, weak at tests, and architecture plus review now carry the load.

- Techniques: Let the compiler's strictness act as the agent's guardrail; Agents as a knowledge oracle for platform and spec behavior; Delegate checklist-style maintenance to agents; Agent-built fuzzing harnesses; Human-enumerated test conditions with agent brainstorming; Architecture-first, then implementation, with full PR reading
- Tools: Claude Code, Rust, Dioxus, Blitz, SubSecond, Firefox (CSS engine), Electron, React Native, Flutter, Kotlin, Swift, Zed

## [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../videos/pqlWNihgdjI.md)
`pqlWNihgdjI` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: enterprise-adoption, coding-agents, context-engineering

Amazon's frontier-dev habits from AWS's Clare Liguori: teams that changed how they worked (context files, self-validating agents, spec-first, local tests) hit a 4.5x median in deployment velocity; tool-only teams got under 3x.

- Techniques: Living steering/skills file with a rule per agent mistake; Self-validating agent loop; Spec-first iteration; Local deterministic mock services; Agent-friendly language and error design; Deployment velocity as the productivity metric; Decision-speed audit
- Tools: Kiro, MCP servers, Bedrock, TypeScript, Rust

## [Building an Agentic Video Editor for Mass Consumer — Ekaterina Deyneka, Reelful](../videos/pPj_tjlvYjA.md)
`pPj_tjlvYjA` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: sandboxing-execution, product-ux, voice-multimodal

Reelful's founder shows how an agentic video editor turns real footage into a clip: media understanding, a user-approved plan, a sandboxed agent with skills, Remotion rendering, and a verification loop.

- Techniques: Sandbox per approved job; Plan approval gate; Skills as encoded craft; Code-defined render target; Verification-then-reiterate loop; Directional templates plus manual editor fallback
- Tools: Remotion, React

## [Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](../videos/lRa9sPaMyy4.md)
`lRa9sPaMyy4` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: coding-agents, context-engineering

Varun Pant (AWS) argues that formal verification in Lean, Verus and similar tools can prove code correct for all inputs, which tests and LLM judges cannot, and that humans should own the specification while agents write code and proofs.

- Techniques: Spec-first verified agent coding; Spec model plus differential random testing; Lemma decomposition for AI proofs; In-code pre- and post-conditions checked by a solver; Intermediate-representation dialect to many backends
- Tools: Lean, Lean 4 browser playground, Kiro (transcript shows 'Kero', likely the AWS agentic IDE), Verus, Z3, Aeneas, Strata / Strata Core, Cedar, SMT solvers, model checkers, ArenaLang (kernel registry)

## [Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia](../videos/McknwOzbmyg.md)
`McknwOzbmyg` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: evals, voice-multimodal, product-ux

Jared Joselowitz (Ufonia) on shipping a clinical voice agent to patients without A/B tests or rollback, using simulated patients, a calibrated LLM judge, and prompt optimization gated by hazard-linked evidence.

- Techniques: Hazard-first safety case; Scenario-conditioned simulated user; Calibrated LLM judge; Reflective prompt optimization (GEPA) with a cost-weighted metric; Synthetic edge-case generation; Staged gated rollout with evidence-based autonomy; Pin prompt versions and keep full traces
- Tools: Matrix (internal simulation framework), PatBot (internal LLM patient), BevJudge (internal LLM judge), GEPA (genetic-Pareto prompt optimizer), DSPy (mentioned as the origin of GEPA), Gemini 2.5 Pro (judge model at the time of the paper)

## [OpenAI's GPT-6 (Astra) Solves Problems Beyond PhD Level. Is This AGI?](../videos/-aCN5BMq1JI.md)
`-aCN5BMq1JI` · Better Stack · 2026-09-02 · q3 · intro · news · also: models-research, multi-agent

Reports OpenAI's claim that its internal Astra model solved 10 maths and CS problems, checkable via Lean proofs, and argues most of the gain comes from the agent harness, with real sub-agent coordination costs.

- Techniques: Machine-checked verification with a proof assistant; Root agent fans out sub-agents and synthesises; Design long runs against loss of coherence
- Tools: OpenAI Astra (internal, unreleased model), Lean (proof language and compiler), Sol Ultra (OpenAI model with sub-agents, as described in the video), Luna, Terra, Sol (named as OpenAI's existing model family), GPT-5 (OpenAI model, October claim discussed), Claude Code (mentioned only as the host's own point of comparison; not in the transcript)

## [Every Level Of Claude Code Loop Engineering Explained](../videos/PLyRe6Zk--8.md)
`PLyRe6Zk--8` · AI LABS · 2026-09-02 · q4 · practitioner · tutorial · also: claude-code, software-factory, agent-architecture

A three-level walkthrough of "loop engineering" in Claude Code: spec-as-/goal for one feature, a queue-driven software factory with a separate adversarial reviewer per branch, then phone control of the loop. Substantive, with the skills and steps shown.

- Techniques: Spec file as a /goal with explicit verification; Queue-file tracker for overnight multi-feature runs; Builder and adversarial verifier split; Clickable HTML mock per feature as planning and verification oracle; PR as the human approval gate; CLI-based platform setup driven by the agent; Minimal CLAUDE.md that points at AGENTS.md; Mobile control of a laptop-resident Claude Code session
- Tools: Claude Code, /goal (Claude Code slash command), /loop (Claude Code slash command), Codex (said to work with the same system), GSAP, Next.js, GitHub (and gh-style CLI), Supabase (and its best-practices skill), Vercel (and deploy-to-Vercel skill), Warp, VS Code, Paseo

## [This Tool Runs Real AWS Services on Your Laptop For Free (Floci)](../videos/7s462S-qRY4.md)
`7s462S-qRY4` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: dev-tools

Better Stack walkthrough of Floci, a free open-source Docker emulator for AWS services (S3, DynamoDB, Lambda) pitched as a LocalStack alternative after LocalStack's free-tier change; the host re-measures the benchmark claims and runs an end-to-end thumbnail pipeline.

- Techniques: Swap LocalStack for Floci in an existing Compose setup; Run AWS CLI commands against the local emulator; Measure emulator startup and idle memory yourself; Test Lambda handlers against a real runtime container; Inspect state in the bundled web UI; Use the Testcontainers module for Lambda tests
- Tools: Floci, LocalStack, Docker, Docker Compose, AWS CLI, Amazon S3, Amazon DynamoDB, AWS Lambda, Lambda Python runtime image, Testcontainers

## [This Linter Rejects AI Slop From Your Code](../videos/mmrSYvYKD9g.md)
`mmrSYvYKD9g` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: coding-agents, dev-tools, token-cost-efficiency

Better Stack demo of the anti-slop rule package for oxlint, which hard-fails low-evidence TypeScript/JavaScript patterns and whose error messages give coding agents a fix to apply.

- Techniques: Hand-picked lint gate for agent-written TS/JS; Agent self-repair loop on lint output; Validate untrusted input at the boundary instead of casting
- Tools: oxlint (Oxc; Rust-based JavaScript and TypeScript linter), anti-slop (rule package for oxlint; created the week before the video), Oxc (the toolchain that oxlint belongs to), Claude Code, CLAUDE.md, TypeScript, ESLint (comparison point only), Zod (suggested runtime validation)

## [This Claude Skill Just Fixed Loop Engineering](../videos/D_uojDHkbw4.md)
`D_uojDHkbw4` · AI LABS · 2026-09-02 · q3 · practitioner · tutorial · also: multi-agent, coding-agents

Explains the "gauntlet loop" (agent builds, critic sub-agents judge against a reference) and its two failure modes, then shows a planning-skill fix: a settled spec and pass/fail answer key the critic checks against.

- Techniques: Three-line gauntlet loop prompt; Swap the reference for a planned answer key; Planning fog map; Phased build order inside one loop
- Tools: Claude Code, Wayfinder (Matt Pocock planning skill), Grill Me (Matt Pocock skill), Matt Pocock skill set (installed from GitHub), Claude Max plan, Claude API (cost comparison), SerpAPI (sponsor, not used in the method)

## [Opus 5 Built An F1 Game... for $1,200](../videos/viHqe5QqTd0.md)
`viHqe5QqTd0` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: multi-agent, agent-architecture, token-cost-efficiency

A Better Stack host runs the "Gauntlet Loop" prompt (a goal plus a real-world target, sub-agents, and a screenshot-based critic loop) on Opus 5 to build an F1 racing game, then judges how playable the result is and what it cost.

- Techniques: Gauntlet loop (goal + real-world target + critic loop); Have the agent build its own verification tools; Stop on plateau, not only on a threshold; Meta-prompt to generate the loop prompt
- Tools: Claude Opus 5, Claude (Max plan subscription, used for the run), Claude sub-agents, Gauntlet Loop prompt (Matt Shumer)

## [GitHub's #1 Trending Author's New Claude Skill Is Insane](../videos/c47uqR7XB_c.md)
`c47uqR7XB_c` · AI LABS · 2026-09-02 · q2 · practitioner · review · also: skills-self-improvement, multi-agent, coding-agents

AI LABS walks through "unlazy," an agent skill that makes coding agents prove each task is done via a gates ledger, tree decomposition and fresh-agent re-checks, plus their fix for its slow sequential runs.

- Techniques: Gates ledger with verifier command; Recursive tree decomposition with depth cap; Orchestrator re-verifies sub-agent claims; Parallel sub-agents with file ownership in plan.md; Explicit give-up instead of silent drop; Installing unlazy into a project
- Tools: unlazy (agent skill; name as spoken in the video), Claude Code, Codex, Ralph loop, Claude goal command, Opus, GPT 5.6, VS Code, Data for SEO (sponsor), model router skill (generic, unnamed)

## [Want to Run Your Agents For Hours? Use These 12 Rules for Claude.md](../videos/D4uBfIe7SzA.md)
`D4uBfIe7SzA` · Better Stack · 2026-09-02 · q3 · practitioner · tutorial · also: context-engineering, claude-code, coding-agents

Warren from Better Stack walks through 12 rules for a CLAUDE.md file so agents can run longer without constant correction: a living failure log, TDD, clarifying questions, strict types, vetted packages, naming, testing, performance, error handling, and architecture notes.

- Techniques: Failure-log CLAUDE.md with an automated update skill; Size budget for CLAUDE.md, with nesting and skills; Tests as the definition of done; Clarify-before-assuming rule; Strict type rules in CLAUDE.md; Dependency vetting rule; Human-style end-to-end and screenshot verification; Endpoint latency budget and database-first queries; Fail-fast error convention referenced from CLAUDE.md; Architecture lookup table in CLAUDE.md
- Tools: Claude, CLAUDE.md, AGENTS.md, Codex, Claude memory, Chrome, iOS Simulator, Playwright, PostgreSQL, Rust, TypeScript, GitHub

## [DeepSWE: A Contamination-Resistant Coding Benchmark — James Shi, Datacurve](../videos/Yk87oUPVaxU.md)
`Yk87oUPVaxU` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, coding-agents, models-research

Datacurve's DeepSWE talk: a long-horizon coding benchmark with tasks written from scratch to resist PR-mined contamination, plus per-model behavior findings and verifier design lessons.

- Techniques: Original task authoring by domain experts; Behavior-based verifiers; Verifier isolation and history scrubbing; Terse objective-only prompts; Per-model failure-mode analysis; Harness-agnostic base-model comparison; Hybrid verification with LLM judges
- Tools: DeepSWE, SWE-Bench Pro, mini-SWE-agent

## [fighting slop with slop — Vaibhav Gupta, Boundary](../videos/AMiyLItEtLA.md)
`AMiyLItEtLA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: software-factory, context-engineering, dev-tools

Vaibhav Gupta of Boundary argues that teams without code review can keep AI-written code stable by building internal tools that enforce invariants, mine agent transcripts, and rethink the language and tooling layers underneath.

- Techniques: Invariant-only architecture file; CLI guard checks for architecture invariants; Required reading as the gate for design docs; Transcript triage loop; A/B test skills or features by agent outcomes; Per-function CLI and describe tool
- Tools: BAML, Claude, Codex, TypeScript, Python, Rust, Go, Ruby, Java, WASM, ripgrep, Notion

## [In the Land of AI Agents, the Verifiers Are King — Tariq Shaukat, Sonar](../videos/VrpEyglYgeU.md)
`VrpEyglYgeU` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: pr-code-review, context-engineering

Sonar's CEO argues AI coding agents need verification built into the loop: guide them with context and constraints, layer algorithmic and agentic checks, and keep the codebase clean. It is a vendor talk, and its numbers are self-reported.

- Techniques: Guide with context and constraints; Zero-trust multi-layer verification; Verification inside the agentic loop; CI verification loop with agent PR review and quality gates; Scheduled code-maintenance and remediation agents
- Tools: Sonar Vortex (product launched the day before the talk, per the speaker), METR time-horizon benchmark chart, Models named: Mythos, Fable, GPT 5.5

## [Medic for Apache Spark - First Aid for Failing Jobs - Drasko Profirovic, Pinterest](../videos/0RNNfxpdbQk.md)
`0RNNfxpdbQk` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: observability, multi-agent, context-engineering

Pinterest's Drasko Profirovic on Medic, an agentic Spark failure-diagnosis tool, and how its prototype became a multi-agent system with record/playback testing, log and metrics handling, and sub-agents.

- Techniques: Record/playback end-to-end agent harness; Learned red-herring filtering for logs; Metrics as a collaged graph image in a quarantined sub-agent; Supervisor with parallel hypothesis researchers; Per-agent prompt plus MCP tool subset; OpenTelemetry traces as step waterfalls
- Tools: Apache Spark, LangGraph, LangGraph DeepAgents, LangFuse, OpenTelemetry, Model Context Protocol (MCP), Grafana, Airflow, Slack, vector database

## [Guide, Verify, Solve — Anirban Chatterjee, Sonar](../videos/03l29gJXpCE.md)
`03l29gJXpCE` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: pr-code-review, coding-agents, governance-compliance

Sonar's product marketer argues AI-written code needs zero-trust, multilayered verification inside agent loops and in CI/CD, framed as a Guide-Verify-Solve (ACDC) cycle, with vendor product pitches throughout.

- Techniques: In-loop verifier callback with fix-and-rerun; Task-scoped context retrieval for agents; Machine-enforced quality rulebook; Dual PR gate: LLM review plus deterministic scan; Cross-model or cross-method review; Graduated automation of review bots; Remediation agent for backlog debt; Per-task model choice from a quality profile
- Tools: SonarQube, Sonar Vortex, Guitar (AI code-review tool, name from captions), Cursor, Claude Code, Codex, Antigravity

## [How to Kill the Code Review — Ankit Jain, Aviator](../videos/YgEv7IQzGdM.md)
`YgEv7IQzGdM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: pr-code-review, context-engineering, skills-self-improvement

Ankit Jain (Aviator) argues code review's real job is alignment, not bug-catching, and proposes reviewing agent session intent, test-plan evidence and a codified "AI slop registry" instead of diffs.

- Techniques: AI slop registry; Capture session decisions as acceptance criteria; Test plan from criteria plus registry invariants, run against a preview; Agent-driven UI evidence with DB snapshots; Review the plan and evidence, not the diff
- Tools: GitHub, Aviator Verify

## [Benchmarks: The Good, the Bad, and the Ugly — Ali Khial, G2i](../videos/jWq-aZIU0kM.md)
`jWq-aZIU0kM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, models-research

Ali Khial (G2i) argues that many agent benchmarks have unrealistic prompts, weak verifiers and reward-hacking gaps, and proposes five principles for building better benchmark tasks.

- Techniques: Layered grading: behavioural breadth plus targeted precision; Specify behaviour and hard constraints, not implementation; Audit a benchmark's verifiers by sampling tasks; Novel tasks with private holdout sets; Publish per-run data alongside rankings
- Tools: SWE-Bench Pro

## [Perception Agents — Antje Barth, Amazon AGI Lab](../videos/2JX6JYyQG4Y.md)
`2JX6JYyQG4Y` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: voice-multimodal, coding-agents

Amazon AGI Lab's Antje Barth argues computer-use agents need shared screen context and self-verification, then demos open-source annotation and design-spec checking tools for UI work.

- Techniques: Element pointing as agent input; Design-rules verification from a spec file; Meeting transcript to agent to verification pipeline; Perceive, plan, act, then re-check the screen
- Tools: Chrome extension (annotation tool), design rules markdown file (design.md), wearable transcription device, Amazon AGI Lab open-source perception agent harness (GitHub)

## [How Forward Deployed Engineering is done at Factory — Eno Reyes](../videos/wpOA-UXynoM.md)
`wpOA-UXynoM` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: software-factory, enterprise-adoption, product-ux

Eno Reyes (Factory CTO) on forward-deployed engineering as the way to build software factories. The bottleneck is agent readiness, meaning deterministic validators in the codebase, not model capability.

- Techniques: Audit validation loops before deploying agents; Bounded long-running harness with an explicit definition of done; Map the signal-to-deploy stages per org; Land-and-expand with a reference implementation; Split automation into one-click fixes and workflow changes; Model-independent harness with owned traces and self-hosted deployment
- Tools: Factory Droid, Missions, LegalDroid, linters, type checkers, security scanners, end-to-end test suites

## [From Agent Traces to Agent Simulations — Rustem Feyzkhanov, Snorkel AI](../videos/Ib5t2RLtxvM.md)
`Ib5t2RLtxvM` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, sandboxing-execution, observability

Rustem Feyzkhanov (Snorkel AI) on turning production agent traces into repeatable, containerized simulation benchmarks that serve as release gates and training data.

- Techniques: Trace-to-task conversion; Harbor-style task folder; Oracle-first validation; Sidecar service mocking with a simulated user; Stepwise long-horizon simulation; Layered verifiers with SME escalation; Benchmark CI and difficulty tagging; Coverage split: happy path plus edge cases; Held-out split for agent config
- Tools: Docker, Docker Compose, Harbor (task format), Terminal-bench, SWE-bench, Arize (experiment and trace recording; transcript says 'Arise'), MCP tools

## [Evaling Video Slop — Maor Bril, Character.ai](../videos/b_PmGocP4rc.md)
`b_PmGocP4rc` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, voice-multimodal, agent-architecture

Maor Bril (Character.ai) on evaluating AI video: frame-level metrics miss story, physics and pacing, so he distilled a judge committee into a small fast VLM trained on pairwise comparisons and run inside the generation loop.

- Techniques: Pairwise A-vs-B judge training; Manufactured negatives; Matched-encoding real-vs-AI pairing with identical annotation; Expert-committee distillation into a small VLM; Eval inside the generation loop; Calibration sessions with randomized annotation; Agent with validation tools
- Tools: Qwen (small VLM, post-trained), Dolby Atmos (audio quality), CLIP-style frame metrics, frame-drift metrics, Kling, Seedance, Veo, Sora, OpenTelemetry (requested, planned for harness)

## [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../videos/jQDXzEVHMSE.md)
`jQDXzEVHMSE` · AI Engineer · 2026-08-18 · q3 · practitioner · interview · also: infra-cost-scaling, rag-retrieval

Gergely Orosz interviews Simon Eskildsen, founder of Turbopuffer, on his path from Shopify infrastructure to building an S3-backed search engine, napkin-math habits, CPU scarcity and startup financing. Mostly origin story, little AI content.

- Techniques: Napkin-math latency and cost estimate before benchmarking; Proxy-based fault injection in CI; Object storage as the system of record with an HTTP cache in front; Design for tail latency and round trips; Batch durable writes; Ship simplest version then probe demand
- Tools: Toxiproxy, NGINX, Amazon S3, MySQL, Rails, Postgres, pgAnalyze, Docker, Rust, GDB, Redis, NVMe SSD

## [Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](../videos/CTLa_p6iOiY.md)
`CTLa_p6iOiY` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, voice-multimodal

Pierluca D'Oro (Programma Labs) shows that static computer-use benchmarks can be gamed by replaying recorded successful traces, and argues for varied environments plus hierarchical confidence intervals.

- Techniques: Replay-agent baseline check; PRISM environment design checklist; Template plus verifier config compiler; Hierarchical confidence intervals; Interval-gated model decisions

## [This New Skill Finally Solves Thinking For AI Agents](../videos/m6IXL_YGqBQ.md)
`m6IXL_YGqBQ` · AI LABS · 2026-08-02 · q2 · intro · review · also: multi-agent, coding-agents, skills-self-improvement

AI LABS walks through a community "ADHD" skill that makes a coding agent ideate by fanning out isolated sub-agents, each seeded with a different frame, then scoring and merging the results; shown for test planning and pre-ship UX/churn review.

- Techniques: Frame-diversified tree-of-thought fan-out; Three-question gate before auto-invoking an expensive fan-out; Install an agent skill from a repo and fix the config folder for Claude Code; TDD test-strategy planning with PRD and tech spec linked in CLAUDE.md; Pre-launch UX and churn review by fan-out
- Tools: Claude Code, Codex, Cursor, CLAUDE.md, .agents folder (installer target), SKILL.md, Top View (sponsor; AI video skill), Kling, Sea Dance, Nano Banana

## [Anthropic Just Fixed Graph Engineering's Greatest Flaw](../videos/H7t3uUp3HVw.md)
`H7t3uUp3HVw` · AI LABS · 2026-08-02 · q2 · intro · tutorial · also: multi-agent, claude-code, skills-self-improvement

Graph engineering fans agent work across parallel nodes but hides failures; the video's fix is layered verification skills built with Skill Creator, plus a fresh-context Opus second opinion.

- Techniques: Install Skill Creator as a plugin; Standalone deep-review skill; Embedded verification skill that runs after each feature; Embedded rule-gate skill; Second-opinion skill via claude -p; Headless browser for visual verification; One skill per review angle, chained by an orchestrator skill; Write build, test and lint commands into CLAUDE.md; Pin the judging node to a stronger model
- Tools: Claude Code, Claude Opus, Claude Haiku, Codex, Skill Creator plugin, verify skill, code review skill, simplify skill, design skill, design.md, second opinion skill, CLAUDE.md

## [All The Types Of Claude Loops Explained In 13 Minutes](../videos/8wsM0euQOvc.md)
`8wsM0euQOvc` · AI LABS · 2026-08-02 · q2 · practitioner · tutorial · also: agent-architecture, claude-code, multi-agent

AI LABS sorts Claude Code agent loops into five types (stateless, learning, multi-agent review, verification, workflow-improvement) with setup steps; anecdotal, with a sponsor segment.

- Techniques: Goal-command loop with tests as the acceptance criterion; Save-every-working-version rule in CLAUDE.md; Skill-improvement loop (learning loop); Multi-agent review loop with an orchestrator; Implementer vs. scorer verification loop; Workflow-improvement loop with a process optimizer
- Tools: Claude Code, CLAUDE.md, Haiku (completion checker in the goal loop), Ralph loop (named as a stateless loop example), goal command, skill loop command (name as spoken), learning.md, thermonuclear review (review skill, named as spoken), orchestrate command, review loop command, iterate command, JSON files (findings and scores)

## [Bun Moved To Rust... Zig's Creator Fired Back](../videos/0TSxrzBVEwQ.md)
`0TSxrzBVEwQ` · Better Stack · 2026-08-02 · q4 · practitioner · news · also: multi-agent, software-factory, coding-agents

Bun ported its ~1M-line codebase from Zig to Rust in 11 days using parallel Claude agents with an implementer, two adversarial reviewers and a fixer; the video also covers Zig creator Andrew Kelly's public criticism.

- Techniques: Adversarial review loop per unit of work; Porting spec plus lifetime table before code generation; Faithful port over idiomatic rewrite, all at once; Guardrails for parallel agents on one git repo; Sharding by git worktree; Error-driven crate-by-crate loop; Reviewer rule against justified workarounds; Test-file batch loops as the verification step
- Tools: Bun (1.3.14 final Zig release, 1.4 Rust), Zig, Rust, Claude / Claude Code, Fable 5 (pre-release model, as named in the video), cargo, git (worktrees), Next.js (dev-server hot reload test), JavaScriptCore, TigerBeetle (referenced by Kelly), Hacker News / GitHub (where the porting doc was noticed)

## [Claude Code Loop Explained | Loop VS Prompts](../videos/pGS7ku-4Fbs.md)
`pGS7ku-4Fbs` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: claude-code, agent-architecture, token-cost-efficiency

Walks through Anthropic's "Getting Started with Loops" post for Claude Code: four loop types (turn, goal, time, proactive) defined by who decides when to stop, plus the skill.md, turn-cap and token-control practices that keep loops safe.

- Techniques: Define the stop condition before starting a loop; Write skill.md as a measured verification protocol; Goal loop with deterministic success criteria and a hard turn cap; Choose local or cloud for time-based polling; Fresh-context adversarial reviewer; Pilot, then scale, and monitor spend mid-run; Route models by task
- Tools: Claude Code, /loop, /schedule, /goal, /usage, /workflows, skill.md, Lighthouse (named as a score example), Opus (named as an example of a capable model)

## [How To Use Claude Fable 5 Better Than 90% Of The People](../videos/GM7-ei-4Xc8.md)
`GM7-ei-4Xc8` · AI LABS · 2026-08-02 · q2 · practitioner · tutorial · also: claude-code, token-cost-efficiency, multi-agent

How a small AI-coding team runs Claude Fable 5 in Claude Code: keep effort at low-high, plan big and implement small, test-first with a separate test author, and layered code and security review subagents.

- Techniques: Keep effort between low and high; PRD-first planner/implementer split; Subagent routing tiers in CLAUDE.md; Ponytail with a test net; Separate test-author subagent (TDD); Parallel scoped security review; Architecture review subagent; HTML mock-up before build; Pre-merge comprehension quiz
- Tools: Claude Code, Claude Fable 5, Claude Sonnet 5, Claude Opus, Claude Mythos, OpenAI Codex CLI, OpenAI Codex plugin for Claude Code, Ponytail, Cursor Thermonuclear Code Quality Review skill, Claude Code security review GitHub Action, CLAUDE.md, Veed (sponsor)

## [Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI](../videos/ZpK5PWX2YRM.md)
`ZpK5PWX2YRM` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: pr-code-review, coding-agents, software-factory

Alex Volkov on the "Z/L continuum" for how much agent-written code engineers should read in 2026: route review effort by the proof a change needs, not by a blanket rule.

- Techniques: Risk-tiered review routing; Decompose into atomic PRs with agents; Separate writer, inspector and test author; Turn review findings into system rules; Ask the agent where the critical code is; Loops with verification and retry
- Tools: Claude Code, Codex, OpenClaw, Pi, Antigravity, Grok Code

## [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../videos/c35YoMdnI78.md)
`c35YoMdnI78` · AI Engineer · 2026-07-18 · q3 · practitioner · panel · also: software-factory, context-engineering, agent-architecture

Panel debate on whether agent "loops" (Ralph-style, bash-while-true) are hype or working practice; the consensus is loops work for verifiable tasks, need deterministic feedback and human-owned architecture, and are not yet a full software factory.

- Techniques: Fresh-context loop with file-system state; Back-pressure hooks that talk back; Deterministic controller around the LLM step; Context budget with headroom; Bare-model baseline on each new release; Explicit cost decision for high-value verification; Start small and iterate on real users; Vendor code and minimise open-source dependencies; Prefer statically typed languages for agent-maintained code
- Tools: Claude Code, Ralph loop (bash while-true), pre-commit hooks, PostHog, Notion, Sentry, Git, npm, Rust, Haskell, Python, TypeScript

## [Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com](../videos/MpZzWMdmQCE.md)
`MpZzWMdmQCE` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: claude-code, coding-agents, agent-architecture

Talha Sheikh (Checkout.com) argues coding agents need deterministic, shareable verification hooks, not better instructions, and that the real engineering work is designing the verification harness.

- Techniques: Stop-hook deterministic verifier; Fail-and-retry feedback loop; Layered enforcement at multiple points; Language-agnostic check contract; Executor plus advisor loop; Cheap model plus strong harness
- Tools: Claude Code, Claude Code hooks (Stop hook), VectorV1 / Vector Harness, Haiku, Opus, Anthropic Glasswing / Project Mythos (named, not described)

## [The Prompt is the Platform - Dominik Tornow, Resonate HQ](../videos/DqtmZE6Hl0g.md)
`DqtmZE6Hl0g` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: agent-architecture, context-engineering

Dominik Tornow (Resonate) argues the spec, not the code, becomes the product: agents should design a system via deterministic simulation before writing the production implementation.

- Techniques: Intermediate concrete spec between abstract spec and implementation; Simulation-first design loop for the agent; Deterministic simulation of target dependencies with legal fault injection; Forbidden-fruit trace events; Shrink the protocol and build on target primitives
- Tools: NATS.io, Postgres, Rust, Python, TypeScript, Go, Java, Resonate SDK

## [Your agent is blindfolded — Johan Lajili, Poolside AI](../videos/iRcX54EO5g8.md)
`iRcX54EO5g8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: coding-agents, context-engineering

Johan Lajili (Poolside) argues agent trust comes from verification: give agents a CLI to drive and test the app, make them reproduce bugs before fixing, and make the codebase easy for AI to check.

- Techniques: Reproduce-first gate; App-driving CLI for non-web apps; Token-compressed UI snapshot; Let the agent discover its own UI problems; Periodic self-review of logs and repeated actions; Human-like exploratory testing by the agent
- Tools: Poolside internal app-testing CLI (unnamed), VS Code extension, G-Stack (mentioned as an existing tool for screenshots and snapshots)

## [Understanding is the new bottleneck — Geoffrey Litt, Notion](../videos/WkBPX-oDMnA.md)
`WkBPX-oDMnA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: coding-agents, product-ux, skills-self-improvement

Geoffrey Litt (Notion) argues humans must still understand agent-written code to stay creative participants, not only to verify it, and shows explainer docs, comprehension quizzes, agent-built micro-worlds and shared spaces for doing so.

- Techniques: Explainer doc per agent change (ExplainDiff-style skill); Comprehension quiz gate before sharing code; Intuition-first, literate ordering; Agent-built micro-world debugger; Step-through simulation for a migration; Shared threads and commentable docs with agents
- Tools: Claude Code, Claude, Cursor, Notion, Notion HTML blocks

## [Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft](../videos/Lc8zRh9muoY.md)
`Lc8zRh9muoY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: observability, agent-architecture

Microsoft's Chronicle PoC records each agent node's inputs and outputs as a replayable trace, so production failures can be debugged and turned into offline tests. The talk argues for replayability rather than chasing bitwise determinism.

- Techniques: Boundary-annotated run recording; Record at the node boundary, not the network; Replay with selective stubbing plus assertions; Zero-model-call deterministic tests from traces; Guardrails at the tool boundary; Keep generation variance on
- Tools: Chronicle (Microsoft proof of concept; code link shown by QR code, URL not spoken)

## [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI](../videos/Rx8f05JI_WA.md)
`Rx8f05JI_WA` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: evals, coding-agents, security-guardrails

Rishi Desai presents SWE-Marathon, 20 project-scale coding tasks where the best agent solves only 26%, and argues that multi-channel, anti-cheat verification is the main bottleneck for long-horizon evals.

- Techniques: Multi-channel verification; Strace-based forbidden-subprocess detection; Hardening loop before publishing a benchmark; Standardize tasks into a Harbor-format environment; Trajectory work-pattern charts
- Tools: SWE-Marathon, Harbor, HumanEval, SWE-bench, Terminal-Bench, Claude Opus 4.8, Claude Code, GPT-5.5 (transcribed as 'gbd 5.5'), Codex, GLM 5.2, Gemini, strace

## [Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs](../videos/HEFSExa0xl0.md)
`HEFSExa0xl0` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: agent-architecture, mcp-and-tools, evals

Witan Labs on lifting coding agents' spreadsheet accuracy from about 50% to 92% by replacing 15 tools with one persistent-state REPL, plus a formula engine and render engine as the verification loop.

- Techniques: Single persistent-state REPL instead of many tools; Verification loop with domain engines; Golden-spreadsheet black-box evaluation; Domain-knowledge reminders in the prompt; Trace review for plumbing bugs
- Tools: Node.js REPL, JavaScript, TypeScript type definitions, C#, LLM-as-judge, Witan Labs internal formula engine, Witan Labs internal render engine

## [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD - Sumaiya Shrabony](../videos/WLXxTaPagA8.md)
`WLXxTaPagA8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: evals, observability, multi-agent

Solo agent builders keep rebuilding CI/CD-style controls (regression tests, alerts, contracts, staging, audit trails) one failure at a time; the talk argues for blocking gates at the most expensive handoff.

- Techniques: Boring blocking gates before save; Guarded vs naive mode demo; Handoff mapping; Per-gate audit record; Voice and domain contracts as explicit rules
- Tools: Claude Code

## [Respect The Process - Andrew Dumit, Watershed Technology Inc.](../videos/CLttOU7n6sI.md)
`CLttOU7n6sI` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: governance-compliance, coding-agents, sandboxing-execution

Andrew Dumit (Watershed) on deploying coding agents for sustainability supply-chain graph edits: constrain the effects through a typed SDK and deterministic execution, not the agent's reasoning, so the process can be validated.

- Techniques: Typed SDK as the only write path; Deterministic run executor (validate-then-commit); Review artifact instead of code review; Constrain effects, not reasoning; Eval-driven hill-climbing on the agent task
- Tools: Claude Code, TypeScript SDK, React agent (earlier version)

## ["I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox](../videos/-CnA2lGfymY.md)
`-CnA2lGfymY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: security-guardrails, agent-architecture

Erik Meijer shows how to make agent tool calls provably safe by turning the plan into a program that can be type-checked, taint-analysed and proven before anything runs.

- Techniques: Plan as data, execute after check; Taint or data-flow analysis over the plan; Proof-carrying generation; Effects as data (free monad style)
- Tools: Lean, Dafny, Isabelle, PVS, TLA+, Claude Code

## [Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS](../videos/IddXPepIAS4.md)
`IddXPepIAS4` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: context-engineering, coding-agents, mcp-and-tools

Erik Hanchett (AWS) on spec-driven development: write requirements, design and task markdown before code, keep a human reviewer in the loop, and use property-based tests to check the result.

- Techniques: Manual spec loop with any coding assistant; Clarifying questions before requirements; EARS-format requirements; Property tests generated from requirements and design; MVP-first task ordering; Steering docs plus on-demand skills; Pull requirements from PM tools via MCP
- Tools: Kiro, spec-kit, MCP, FastCheck, Mermaid, EARS, Jira, Asana, agents.md, CLAUDE.md

## [Using LLMs to Secure Source Code — Eugene Yan, Anthropic](../videos/imFedndyXYQ.md)
`imFedndyXYQ` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: security-guardrails, sandboxing-execution, multi-agent

Eugene Yan (Anthropic) walks through a six-step harness for using LLMs to find, verify, triage and patch vulnerabilities, arguing the bottleneck has moved from finding bugs to verification, triage and patching.

- Techniques: Threat model as a living context document; Isolated, reproducible PoC sandbox; Independent adversarial verifier; Tool-equipped discovery; Less prescriptive prompts for stronger models; Patch validation ladder with a generative verifier loop; Close the loop as a regression check; Severity triage as impact times likelihood with compensating controls; Code-owner routing without an LLM
- Tools: Claude, Claude Code, Docker, PostgreSQL, Redis, Jira

## [What Does Done Even Mean? Agents and Paperclip's Liveness Model - Dotta, Paperclip](../videos/7P0elyLIxXo.md)
`7P0elyLIxXo` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, multi-agent

Dotta (Paperclip) argues "done" is a bundle of claims, not a checkbox, and shows how a control plane with blockers, reviewers, and watchdogs keeps agent work moving while still verifying it.

- Techniques: Done as a structured object; Cross-model verifier; Evidence-first completion; Watchdog agent for goal persistence; Explicit state transitions with enforced blockers; Per-task reviewer and approver assignment with audit trail
- Tools: Paperclip, Pi, OpenClaw, Hermes, Claude Code, Codex

## [SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius](../videos/wcUJWP6WpGM.md)
`wcUJWP6WpGM` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: evals, coding-agents, training-finetuning-rl

Ibragim Badertdinov (Nebius) shares lessons from running monthly SWE-rebench evals of coding agents: fresh time-split tasks, verifier quality, infra noise, benchmark cheating, and reporting cost and reliability.

- Techniques: Monthly time-split task collection; Oversample, then filter by running agents; Strip future information from the agent sandbox; Minimal agent with strong infrastructure; Error-class retry policy; Reliability-aware metrics; Reproduce a public benchmark before trusting your own numbers; Eval pipeline reused as training pipeline
- Tools: SWE-rebench, SWE-bench, Terminal-Bench, Claude Code, Codex, Junie, Docker, GitHub Archive, GitHub API

## [Fast Models Need Slow Developers — Sarah Chieng, Cerebras](../videos/TeGsFFNqRLA.md)
`TeGsFFNqRLA` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: coding-agents, inference-serving, context-engineering

Cerebras's Sarah Chieng argues that fast coding models (Codex Spark, ~1,200 tok/s) demand new habits: plan with a large model, execute with a fast one, verify every step, and keep context in bounded goals.

- Techniques: Planner-executor model split; Session-to-skill distillation; Per-step automatic verification; Parallel variant generation with cherry-picking; Scoped steering constraints; Automatic refactor pass after each task; Bounded goals with a context budget; Four-file external memory (AGENTS/PLAN/PROGRESS/VERIFY)
- Tools: Codex Spark, Codex, GPT-5.4, GPT-5.3 Codex, Sonnet, Opus, REAP (router-weighted expert activation pruning)

## [Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence](../videos/UQKg0td-Bf4.md)
`UQKg0td-Bf4` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: evals, security-guardrails, mcp-and-tools

Steven Willmott (SafeIntelligence) argues agent testing needs an explicit spec of data, rules, terminology, roles and robustness needs, kept separate from the implementation and run in a closed loop.

- Techniques: Six-part agent spec; Spec-driven security testing; Input perturbation sweep; Closed-loop spec iteration (backyard RL); Specs as versioned repo files; Agent cards plus variation envelopes
- Tools: SafeIntelligence platform, A2A agent cards, LangSmith, Vertex AI agents, Braintrust, OpenAPI

## [Your Attention Is the Bottleneck, Not Your Agents — Zack Proser, WorkOS](../videos/so9l_MwS2yg.md)
`so9l_MwS2yg` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: claude-code, software-factory, skills-self-improvement

Zack Proser (WorkOS) argues human attention, not agent capacity, is the bottleneck, and shares remote Claude Code from a phone, verification gates, and session-log mining to protect focus.

- Techniques: Three-tier verification ladder for agent output; Closed-loop ticket fixing with explicit done criteria; Remote-controlled session from a phone; Scheduled session-log retrospective; Ticket-tagged overnight agent loop; Parallel large features with worktrees and agent teams; Voice-first brainstorm, then written artifact
- Tools: Claude Code, Claude Opus 4.6, Slack MCP, Linear MCP, GitHub Mobile, Cursor, Codex, Vercel bot, OpenClaw, Twilio, ChatGPT advanced voice mode, git worktrees

## [Agentic Evaluations at Scale, For Everybody — Nicholas Kang & Michael Aaron, Google DeepMind](../videos/Ubwb6NzegyA.md)
`Ubwb6NzegyA` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: evals, models-research

Google DeepMind and Kaggle staff tour their open eval platforms (hackathons, agent exams, Game Arena, community benchmarks) and the problems they hit: saturation, cost, harness variance, and hidden configs.

- Techniques: PvP game benchmark with pairwise rating; Task-of-assertions plus LLM-judge benchmark structure; One-line agent exam; Lock down the harness and config when comparing models
- Tools: Kaggle Benchmarks, Kaggle Game Arena, OpenSpiel, Kaggle simulation platform, LLM model proxy (also available on Colab), Bradley-Terry pairwise rating, Moltbook (transcribed as Motebook), SWE-Bench Pro (cited)

## [The maturity phases of running evals — Phil Hetzel, Braintrust](../videos/FB-MLPhL9Ms.md)
`FB-MLPhL9Ms` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: evals, observability

Phil Hetzel (Braintrust) lays out four maturity stages of agent evals, from documented vibe checks to replaying tool-using agents offline with captured system state.

- Techniques: Documented human annotation (thumbs plus justification); Failure-mode extraction from justifications; LLM-as-judge with binary outputs and human-aligned ground truth; Deterministic code scorers for objective failures; Production trace flywheel; Whole-trace evaluation with per-step targeting; Embedding system state in traces and time-versioned queries
- Tools: Braintrust, Cursor, Claude Code, Codex

## [Anthropic Workshop: Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson](../videos/mR-WAvEPRwE.md)
`mR-WAvEPRwE` · AI Engineer · 2026-06-18 · q4 · practitioner · workshop · also: agent-architecture, multi-agent, claude-code

Two Anthropic Applied AI engineers explain how long-running agent harnesses evolved, and how a planner, generator and evaluator loop with rubric grading builds multi-hour apps that a single agent loop cannot finish.

- Techniques: Generator-evaluator loop with a live-app evaluator; Rubric-as-taste with calibrated examples; Sprint contracts negotiated in files; Thin planner that stays high level; Structured state on disk with JSON feature lists and progress files; Breadcrumb logs for later pickup; Read full traces, then tune prompts from them; Ralph-style stop-hook loop with exit criteria; Hooks for human check-ins; Split model roles for cost; Put the human-readable spec back into long sessions
- Tools: Claude Code, Claude Agent SDK, Playwright MCP, Chrome MCP, Claude Code skills, Claude Code sub-agents, Claude Code agent teams, Claude Code stop hooks, Claude Code auto mode, git, Puppeteer

## [Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry](../videos/ugUeZ8-b-u0.md)
`ugUeZ8-b-u0` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: coding-agents, dev-tools

Argues Rust's strict compiler suits agent-written code better than Python or TypeScript: compile-time checks rule out bug classes that tests and LLM review miss, and compiler errors give agents concrete fix signals. Sponsored by Sentry.

- Techniques: Compile-in-the-loop repair; Deterministic checks before LLM review; Use error messages that name the concrete type; Choose a language by how strongly its checker constrains output; Write tests first when an agent writes tests
- Tools: Rust, rustc (Rust compiler), TypeScript, Python, Sentry

## [Evals Are Broken, Use Them Anyway — Ara Khan, Cline](../videos/QuuIywMG4s8.md)
`QuuIywMG4s8` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: evals, coding-agents

Ara Khan (Cline) argues most people misuse evals, either trusting vendor leaderboards or dismissing evals for vibes, and shows how to build a Terminal-Bench-style agent eval and hill-climb on it alongside a vibe check.

- Techniques: Failure-trace triage loop; Isolated parallel eval runs; Hill-climb with a vibe check; Sort fixes into three zones; Delayed model adoption; Check the task itself
- Tools: Terminal-Bench, Harbor, SWE-bench Verified, Claude Code, Codex, Daytona, Docker, Modal

## [Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar](../videos/NuePCNMpWGc.md)
`NuePCNMpWGc` · AI Engineer · 2026-06-18 · q2 · practitioner · talk · also: pr-code-review, evals, coding-agents

Sonar argues that LLM pass rates miss security, maintainability and verbosity. It shows its Java eval of 53+ models and pitches a verify-in-loop and remediation pipeline, so it is product-heavy.

- Techniques: Dual-metric model evaluation; In-loop static analysis via MCP; Regression-gated autofix; One PR per issue for tech debt; Remediation on quality-gate failure
- Tools: SonarQube, SonarQube Agentic Analysis (MCP), Sonar Sweep, Sonar Context Augmentation, Sonar remediation agent, Claude Code, Codex, Gemini CLI, Devin, Cursor, Windsurf, Antigravity

## [BDD, ADR, PRD, WTF: Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence](../videos/504PvfXou5Y.md)
`504PvfXou5Y` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: context-engineering, pr-code-review

Michal Cichra on keeping agents and humans aligned by storing ADRs, PRDs and executable BDD specs in the repo, then enforcing them through git hooks, CI and import-boundary lints.

- Techniques: ADR with enforcing lint rule; Import-boundary restriction to eliminate bug classes; Executable BDD scenarios linked to PRDs; Shared checks in git hooks and CI; Design system as enforced rules and previews; Scoped test selection per task
- Tools: Cucumber, git hooks, CI, linters, type checkers, architecture import lint, Markdown docs

## [How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS](../videos/vy7o1g2iHY8.md)
`vy7o1g2iHY8` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: skills-self-improvement, agent-architecture, evals

WorkOS DX engineer on replacing 10k lines of generated agent skills with 553 lines of gotchas, enforcing gates in a state machine, and making agents prove their work with hashes and videos.

- Techniques: Enforced state-machine gates for agent pipelines; Hash-verified test receipts; Gotchas-only skills validated by paired evals; Visual before-and-after proof on PRs; Retrospective agent over run transcripts; Conditional rules instead of doc summaries
- Tools: Pi, Claude Code, Codex, Playwright CLI, TypeScript, SHA-256, WorkOS CLI, AuthKit, TanStack Start, Next.js, GitHub, Linear

## [Is Your AI Code Producing CRAP? (Here's How To Fix It)](../videos/XuMR1pgc6pc.md)
`XuMR1pgc6pc` · Better Stack · 2026-06-02 · q3 · practitioner · review · also: coding-agents, pr-code-review

Better Stack explains the CRAP metric (complexity combined with test coverage) and the cargo crap Rust tool, arguing it is a useful second check on complex, under-tested code, especially AI-generated code.

- Techniques: Run a CRAP check after the unit tests; Set a complexity budget; Check that the metric reacts to test removal
- Tools: cargo crap (cargocrap Rust package, by Oleksandr Prokhoranko), CRAP metric (Savoia and Evans, 2007), Rust, CRAP tool for Java (same author, mentioned, not shown)

## [3 Design Levels For a Free Claude Code Boost (People Stop At Level 1)](../videos/5lycYTOYbPM.md)
`5lycYTOYbPM` · AI LABS · 2026-06-02 · q3 · practitioner · tutorial · also: claude-code, context-engineering, vibe-coding-app-building

Three levels of getting non-generic UI from Claude Code: a structured single-page design prompt, a CLAUDE.md plus design.md system for cross-page consistency, and design tests written before the code, including visual TDD with Visly.

- Techniques: Structured single-page design prompt; CLAUDE.md for project context, design.md for the visual system; Lint design.md against Google's open template; Install an external design-principles audit skill per project; Derive design tests from design.md before writing UI code; Visly local visual TDD loop
- Tools: Claude Code, Claude Opus 4.7 (model named in the video), CLAUDE.md, design.md, OKLCH, Google design.md template (open-sourced), Versalab design-audit skill, Playwright, Visly CLI (transcribed as 'Visly Test' and 'Visley'), Zilliz Cloud (sponsor), Inter (named as banned font), Geist (named as banned font)

## [Vibe Engineering Effect Apps — Michael Arnaldi, Effectful](../videos/Wmp2Tku2PrI.md)
`Wmp2Tku2PrI` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: context-engineering, coding-agents, agent-architecture

Michael Arnaldi builds a TypeScript Effect HTTP to-do API from an empty repo, arguing agents need the real source repo, strict lint back pressure, and generated pattern docs.

- Techniques: Clone the library source into the repo; Strict diagnostics plus lint as back pressure; AGENTS.md as a living rulebook; Spec file plus Ralph-style loop; Self-selected pattern docs; Single execute tool instead of many tools; Per-test rollback transactions for DB tests; Test layers with it.layer; Lint reference checks in CI for pattern docs
- Tools: Effect v4 (beta), Effect SQL with SQLite, Bun, Vitest, TypeScript native preview (tsgo), ESLint, OpenCode, GPT-5.4, Claude Opus, Codex, Cursor, Temporal

## [Agents Don't Do Standups: Building the Post-Engineer Engineering Org — Mike Spitz, PFF](../videos/VMemhtlsoNk.md)
`VMemhtlsoNk` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: software-factory, enterprise-adoption, context-engineering

Mike Spitz (PFF) reports a Jan–Mar 2026 case study where agent-driven spec, design doc, ticket and PR flow cut delivery time and dropped Scrum for a 20-engineer team.

- Techniques: Agent-interviewed spec then skill-generated LDD; Auto-generated, non-blocking tickets and PR-driven status; Agent code review limited to opinion-level nits; Post-staging QA agent against acceptance criteria; Composable per-step skills for the delivery lifecycle; Customer survey as the primary retro signal; Phased, non-critical-first rollout
- Tools: Claude Code, Claude Opus, Codex

## [The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory](../videos/ow1we5PzK-o.md)
`ow1we5PzK-o` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: multi-agent, agent-architecture, software-factory

Luke Alvoeiro (Factory) on "Missions", a multi-agent system that runs for hours or days by combining delegation, creator/verifier, broadcast and negotiation, with a validation contract written before any code.

- Techniques: Validation contract written at planning time; Fresh-context adversarial validators; Structured worker handoffs; Serial features with read-only parallelism; Per-role model choice; Milestone-based negotiation; Orchestration as prompts and skills
- Tools: Factory Droid (open source Goose lineage mentioned), AGENTS.md, skills, computer use (for user-testing validator), prompt caching

## ["Software Fundamentals Matter More Than Ever" — Matt Pocock](../videos/v4F1gFy-hqg.md)
`v4F1gFy-hqg` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: context-engineering, coding-agents, claude-code

Matt Pocock argues software fundamentals (deep modules, shared language, TDD, good feedback loops) matter more with AI agents, because bad code is now the most expensive it has been.

- Techniques: Grill-me interview before planning; Generated ubiquitous-language glossary; Small-step TDD with feedback loops; Codebase architecture improvement skill; Design the interface, delegate the implementation
- Tools: Claude Code

## [Taste & Craft: A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @The Pragmatic Engineer](../videos/wjk0ulMAkbc.md)
`wjk0ulMAkbc` · AI Engineer · 2026-05-18 · q3 · practitioner · interview · also: product-ux, coding-agents

Linear's CTO and Gergely Orosz on why AI makes taste and quality the scarce advantage. Linear's practices: Quality Wednesdays, a zero-bug policy, and week-long paid work trials.

- Techniques: Quality Wednesday; Zero-bug policy with agent triage; Single-shot agent PRs for incoming bugs; Human-judged feel in agent output; Paid greenfield work trial; Open, tagged customer meeting archive
- Tools: Claude Code, Opus 4.5, Linear, Apple Human Interface Guidelines

## [Feedback Loops are All You Need — Mehedi Hassan, Granola](../videos/ON5LIT0M4do.md)
`ON5LIT0M4do` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: observability, product-ux

Granola's Mehdi Hassan argues that shipping LLM features needs your own tracing, per-PR web previews, and fast feedback loops, not better one-shot prompts.

- Techniques: Home-built LLM tracing store with an internal UI; Web-shell preview per PR; Agent self-verification with screenshot evidence; Own the web search path
- Tools: Electron, Cursor, AI SDK, CloudWatch, OpenTelemetry, Tauri, Figma

## [Full Walkthrough: Workflow for AI Coding — Matt Pocock](../videos/-QFHIoCo-Ko.md)
`-QFHIoCo-Ko` · AI Engineer · 2026-05-18 · q4 · practitioner · workshop · also: context-engineering, software-factory, multi-agent

Matt Pocock's live workshop on an AI coding workflow: grill-me alignment, PRD, vertical-slice issues with blocking edges, AFK Ralph loops with TDD and feedback loops, and deep-module codebases.

- Techniques: Smart-zone sizing and clear-over-compact; Grill-me alignment skill; Destination doc plus journey issues; Ralph loop (sequential AFK runner); Red-green-refactor TDD for agents; Self-review in a fresh context; Interface-first deep modules with grey-box delegation; Push vs pull for coding standards; Sandcastle-style parallel runs; Delete plans and PRDs after they ship
- Tools: Claude Code, Sandcastle, Docker, TypeScript, GitHub Issues, TLDraw, Slido, Playwright MCP, Sonnet, Opus, Spec Kit, OpenSpec

## [Harnesses in AI: A Deep Dive — Tejas Kumar, IBM](../videos/C_GG5g38vLU.md)
`C_GG5g38vLU` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: agent-architecture, security-guardrails, context-engineering

Tejas Kumar (IBM) walks through building a "poor man's" agent harness live: deterministic guardrails, outcome verification, and credential injection around a weak model, with the prompt left unchanged.

- Techniques: Deterministic pre-turn hook for state and secrets; Outcome verification from the trace; Guardrails as composable functions; Two-level retry around an attempt; Naive head-and-tail context trimming; Tool definitions in the OpenAI SDK shape
- Tools: Playwright, Chromium, OpenAI Agents SDK-style tool definitions, GPT-3.5 Turbo, Claude Code, Cursor, Codex, Qwen, GPT-OSS, OpenRAG

## [Building your own software factory — Eric Zakariasson, Cursor](../videos/rnDm57Py54A.md)
`rnDm57Py54A` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: software-factory, context-engineering, coding-agents

Cursor engineer Eric Zakariasson on building a "software factory": how to structure repos, grow rules from observed failures, make agents verify their own work, and automate the human loops. Practical, with a product pitch.

- Techniques: Failure-driven rule growth; Reviewer bot enforces house conventions the model lacks; Self-verification with e2e tests and recorded runs; Scoped, parallel async tasks with front-loaded specs; Per-agent VM with a single dev command; Agentic code owners with risk tiering; Loop and stall detection for background agents; Event-triggered cleanup agents
- Tools: Cursor, Cursor cloud agents, BugBot, Playwright, AGENTS.md, Linear, Slack, GitHub, Datadog, Notion, MCP, Cursor workers

## [Beyond Code Coverage: Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft](../videos/FWEInOtngmM.md)
`FWEInOtngmM` · AI Engineer · 2026-05-18 · q3 · practitioner · tutorial · also: coding-agents, mcp-and-tools

Marlene Mhangami (Microsoft/GitHub) argues for red-green TDD with coding agents, testing user-facing behavior with Playwright instead of unit-test coverage, and shows a live Copilot CLI demo.

- Techniques: Red-green-refactor with a coding agent; Behavior-scoped tests against user-facing or stable-contract behavior; Connect the agent to Playwright (three options); Checkpoint before the healer runs; Operational hygiene for Playwright runs; Ingest requirements from M365 with WorkIQ; Prefer direct API tests when an API exists
- Tools: GitHub Copilot CLI, Playwright, Playwright MCP server, Playwright CLI, Playwright Agents, WorkIQ, Azure AI search, Claude, Codex, Ruby on Rails, Python (Playwright binding), TypeScript (Playwright binding)

## [I Tried Every Skill. These Best Claude Skills Are Bizarre](../videos/qQ5uObNKBOU.md)
`qQ5uObNKBOU` · AI LABS · 2026-05-02 · q2 · intro · review · also: claude-code, skills-self-improvement, token-cost-efficiency

Walkthrough of nine community Claude Code skills (notifications, adversarial app QA, output compression, git audit, premortem, mutation testing, plan stress-testing, Reddit research, UI color guidance). Mostly README-level tours, with a mid-video sponsor segment.

- Techniques: Per-event voice notifications for parallel Claude sessions; Adversarial browser QA sweep; Terse-output mode to cut response tokens; Git-history audit with a skill; Premortem pass before go-live; Mutation testing for test-suite strength; Stress-test a plan with selectable challenge modes; Fallback chain for scraping Reddit; Grounded design-reference skill for UI
- Tools: P on Ping (skill, transcript name), Claude Code, agent-browser (CLI), Dogfood skill, Caveman plugin, Git, Git Time Travel skill, Premortem skill, Mutation testing skill, The Fool skill, Gemini CLI, tmux

## [Claude Ultraplan vs Superpowers: I Found a WINNER and It's Not Even Close](../videos/-qFf7v2399E.md)
`-qFf7v2399E` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: claude-code, coding-agents, token-cost-efficiency

A single-repo demo comparing Claude Code's cloud Ultraplan with the Superpowers plugin for planning a release pipeline: Ultraplan is faster and cheaper but thinner, and the host plans locally about 90% of the time.

- Techniques: Launch Ultraplan from the Claude Code CLI; Review and revise an Ultraplan plan in the browser; Superpowers two-stage planning; Stop the planner from using a skill when comparing
- Tools: Claude Code (CLI), Ultraplan (Claude Code feature), Claude Code on the web (Claude Code for Web), Claude Code desktop app for Mac, Superpowers (Claude Code plugin), Claude Routines (mentioned as newly released), GitHub

## [Give Me 13mins, I Will Show You The Right Agent Setup](../videos/ywIhw15za9Y.md)
`ywIhw15za9Y` · AI LABS · 2026-05-02 · q2 · intro · tutorial · also: claude-code, context-engineering, coding-agents

AI LABS walks through a pre-build setup checklist for Claude Code: product-focused PRD, hand-written CLAUDE.md, agents and skills, spec-first tests, progress and learnings files, and load planning. Generic, sponsored, no benchmarks.

- Techniques: Agent-led PRD interview; Lean hand-written CLAUDE.md that links the PRD; Agent vs skill split; Path-scoped rules linked from CLAUDE.md; Negative-constraints docs file; Progress file plus learnings file; Spec-first test generation; Commit-per-implementation with worktrees; Concurrency-aware load test planning
- Tools: Claude Code, CLAUDE.md, Supabase MCP, shadcn/ui, Playwright, Playwright MCP, skill-creator, GitHub, Git (commits, worktrees), Notion MCP, Trello, OpenClaw (sponsor's skill)

## [Knowing This Gives You An Unfair Advantage With AI Coding](../videos/fMY5Sdj2DMk.md)
`fMY5Sdj2DMk` · AI LABS · 2026-05-02 · q3 · practitioner · tutorial · also: claude-code, context-engineering, coding-agents

Tutorial for writing CLAUDE.md rules that keep Claude Code on task: think-first, simplicity, surgical edits, verifiable goals, git safety, scoped rule files and a corrections log.

- Techniques: Behavioral rule block for CLAUDE.md (Karpathy-derived); Verification gate before reporting completion; List only non-default tooling; Corrections-to-learnings loop; Destructive-command confirmation rule; Path-scoped rule files and nested CLAUDE.md; CLAUDE.md structure: description first, priority tiers, length cap
- Tools: Claude Code, CLAUDE.md, AGENTS.md, Karpathy skills repo (referenced, not named as a package), Claude Chrome extension, Puppeteer MCP, Git, GitHub CLI (gh), npm, pnpm, Klaus (sponsor, AI agent hosting), OpenClaw (sponsor, open-source AI agent)

## [The Claude Code Skill Boris Cherny Runs on Every Project](../videos/AhXfI1rSUPc.md)
`AhXfI1rSUPc` · AI LABS · 2026-05-02 · q2 · practitioner · review · also: claude-code, skills-self-improvement, multi-agent

A walkthrough of skills, plugins and slash commands the Claude Code team reportedly uses, including batch worktree fan-out, a verify skill and an end-of-session tech debt skill. Several are internal and unverified, and a sponsor segment is included.

- Techniques: Batch fan-out with worktrees; Project-specific verify skill; Skillify-style session capture; End-of-session tech-debt pass; Inner-loop slash commands; Issue dedupe with a confidence threshold; Security scan, then fix
- Tools: Claude Code, Claude Code batch command, git worktrees, frontend-design plugin, Code Simplifier plugin, Simplify (built-in), Claude Code security scan (built-in), commit command plugin, Remotion skill, skill creator skill, Skillify (internal), verify skill (internal)

## [Stop Assuming Your AI Agent Can Read the Web (Test It!)](../videos/OlNZCtk100Q.md)
`OlNZCtk100Q` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: evals, voice-multimodal

Walkthrough of the Agent Reading Test, a canary-token benchmark that checks whether an AI agent's web fetch pipeline actually reads a full page, with a 13/20 Kimi 2.5 example.

- Techniques: Canary-token reading audit; Verify agent-reported coverage against the answer key; Checklist of web-fetch failure modes
- Tools: Agent Reading Test (agentreadingtest.com), Claude Code, Kimi 2.5

## [Fix Slow React Components in Seconds! (New GitHub Storybook Addon)](../videos/fv9wj8nkDVM.md)
`fv9wj8nkDVM` · Better Stack · 2026-04-02 · q2 · intro · review · also: dev-tools

Walkthrough of GitHub's new Storybook performance-panel add-on for measuring component frame timing, DOM churn, layout thrashing and React render cascades before code reaches production.

- Techniques: Component-level performance check in Storybook; Mark hero and call-to-action elements for render timing; Avoid setState in useLayoutEffect for updates that repeat; Batch style reads and writes to prevent layout thrashing; Memoize components to cut redundant renders
- Tools: Storybook, GitHub Storybook performance add-on (unnamed in transcript), React, useLayoutEffect (React hook), Vue, Svelte, Web Components, Lighthouse, Chrome, Edge

## [The toolkit from Y Combinator CEO that Will Makes Claude Code Amazing](../videos/kLq5p43huYQ.md)
`kLq5p43huYQ` · Better Stack · 2026-04-02 · q3 · practitioner · review · also: coding-agents, claude-code, pr-code-review

A Better Stack walkthrough of GStack, Gary Tan's Claude Code skill pack, showing a plan, review, ship and QA pipeline that builds, tests and opens a PR for a tweet-screenshot feature.

- Techniques: Install GStack into a Claude Code project; Plan-mode CEO scope review before coding; Diff-aware review, ship and QA chain; Let the review command resolve PR review comments; Put tool preferences in CLAUDE.md, not hooks; Skill template plus generated SKILL.md
- Tools: Claude Code, GStack, Bun, Playwright, Greptile, Superpowers (Claude Code plugin), Conductor, React, Vite, TypeScript, Opus, CLAUDE.md

## [GSD Is the Missing Piece For Claude Code](../videos/uEit1oOJK0w.md)
`uEit1oOJK0w` · AI LABS · 2026-04-02 · q2 · practitioner · review · also: coding-agents, context-engineering, multi-agent

AI LABS walks through GSD (Get Shit Done), a planning-and-execution framework for Claude Code, and compares it with BMAD and Superpowers. Main takeaway: choose the framework by how fixed your requirements are.

- Techniques: Choose the framework by requirement certainty; Per-project install with project scope; Initialise GSD on existing vs blank codebases; Keep the planning anchor short; Per-phase discuss, then concise context file; Ground phase research in docs with Context7; Adversarial plan verification and waves; Phase verification gates
- Tools: GSD (Get Shit Done), BMAD method, Superpowers, Claude Code, Claude Opus 4.6, Claude Sonnet, Next.js, Playwright, Context7 MCP, GenSpark (sponsor segment), Speakly (sponsor segment)

## [Anthropic Just Killed All Your Agent Harnesses](../videos/nBH07G-zayk.md)
`nBH07G-zayk` · AI LABS · 2026-04-02 · q2 · practitioner · review · also: agent-architecture, context-engineering, claude-code

Walkthrough of Anthropic's reported harness ablations: with Opus 4.5/4.6, keep a planner, a generator and a separate graded evaluator, and drop micro-level plans, context resets and sprint contracts for strong models.

- Techniques: Product-level planner agent; Separate evaluator with an adversarial stance; Weighted rubric with a score per criterion; Generator and evaluator as agent-team members; Sprint contract for weaker models; Bolt Anthropic's evaluator onto GSD
- Tools: Claude Code, Claude Opus 4.5, Claude Opus 4.6, Claude Sonnet, Claude Haiku, Anthropic agent harness, BMAD, GSD, SpecKit, Superpowers, Ralph Loop, Playwright MCP

## [10 Crazy Claude Code Tips That Give You An Unfair Advantage](../videos/TmsH-RIHvas.md)
`TmsH-RIHvas` · AI LABS · 2026-03-02 · q3 · practitioner · tutorial · also: claude-code, context-engineering, multi-agent

AI LABS walks through ten Claude Code practices: session-insight reviews, Claude-written planning docs, exit-code-2 hooks, worktree-based parallel agents, adversarial fact-checking, and browser-based self-verification.

- Techniques: Session insights review into CLAUDE.md; Claude-authored planning docs as context; Context7 MCP for current library docs; Exit-code-2 PreToolUse guard for protected paths; MCP CLI mode to keep tool schemas out of context; One git worktree per parallel agent; Strict TypeScript and user stories before implementation; Adversarial researcher and fact-checker agents; Agent Browser for self-verification, with CLAUDE.md fallback order; Failure-prediction review pass
- Tools: Claude Code, CLAUDE.md, Claude Code hooks (PreToolUse), MCPCLI (experimental MCP CLI mode), Context7 MCP, git worktrees, TypeScript, Claude in Chrome extension, Puppeteer MCP, Agent Browser (Vercel), Kimi K2.5 (named as comparison in a research example), Opus 4.6 (named as subject of a research example)

## [What REALLY Happened When 16 Claude Agents Tried To Build a C Compiler From Scratch](../videos/SVREdZHPG1I.md)
`SVREdZHPG1I` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: multi-agent, coding-agents, agent-architecture

Better Stack breaks down Anthropic's experiment with 16 parallel Claude Opus 4.6 agents building a C compiler: git-based task locks, shared test harnesses, GCC as an oracle, and why the presenter says it was not fully autonomous.

- Techniques: Git-commit task lock for parallel agents; Isolated clones with push-to-upstream; Ralph loop with a fresh session per task; Quiet test harness with a log file; Deterministic sharded test subsets; Reference-compiler oracle for partial builds; README and progress files as cross-session memory; Role-specialized review agents
- Tools: Claude Opus 4.6, Claude (Anthropic agent), Docker, Git, GCC, Ralph loop, Linux kernel, SQLite test suite, LibJPEG test suite, Redis test suite, Rust

## [Anthropic Released Another Official Process](../videos/aEqKWI-0N0c.md)
`aEqKWI-0N0c` · AI LABS · 2026-03-02 · q2 · practitioner · tutorial · also: skills-self-improvement, context-engineering, claude-code

A team rebuilds a Nano Banana image skill for Claude Code, then shows the skill-design fixes that mattered: trigger-rich descriptions, progressive disclosure, scripts, validation gates and error tables.

- Techniques: Trigger-rich skill descriptions with negative triggers; Three-level progressive disclosure layout; Move constraints out of prompts into post-processing; CLI scripts with modes and a preview mode; Two-stage validation gates with regenerate-on-fail; Error table with error, cause, and fix; Split domain knowledge into reference packets; Iterate against real outputs and refresh the skill-creator
- Tools: Claude Code, Google Antigravity, Nano Banana Pro, skill-creator (Claude Code official skill), Next.js, Cream (sponsor, merchant of record), Cursor, Windsurf

## [This Is The Only Claude Code Plugin You'll EVER Need (Superpowers)](../videos/lq3rzXP4_vs.md)
`lq3rzXP4_vs` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: claude-code, skills-self-improvement, multi-agent

Walkthrough of Superpowers, a Claude Code skills plugin that forces brainstorm, planning, sub-agent TDD and per-step commits. It beat plain plan mode in one demo, but the agent skipped TDD once.

- Techniques: Brainstorm into a design doc before code; Split the design into sub-agent-sized tasks; Pick the execution mode deliberately; Per-task red-green loop with a git commit per step; Plan doc, clear context, then execute (presenter's own workflow, not part of Superpowers)
- Tools: Superpowers (agentic skills framework / Claude Code plugin; 14 skills per the presenter), Claude Code, Opus 4.6 (Anthropic model, used for both builds), React, Vite, Hono (server framework), CSS-in-JS styling library (unnamed in the video), Tailwind CSS (suggested by the presenter in hindsight, not used), XDL (CLI that downloads videos from Twitter; the demo app wraps it), git, Beads (planning tool, comparison only), spec-kit (spec-driven development, comparison only)

## [This Just Fixed 90% of AI Coding Errors](../videos/romGzY0Xu0s.md)
`romGzY0Xu0s` · AI LABS · 2026-03-02 · q3 · practitioner · review · also: coding-agents, multi-agent, skills-self-improvement

AI LABS team tests the Superpowers Claude Code plugin on a Trello-style app: enforced brainstorm, plan, subagent, TDD and review gates work, but they burn context fast and are best used selectively.

- Techniques: Install a workflow plugin from a marketplace in Claude Code; Brainstorm-gated kickoff prompt; Subagent-driven implementation with worktrees and review gates; Anti-test-edit TDD cue; Four-phase systematic debugging prompt; Compact before the next feature; Selective process use; Re-invoke skills after context loss
- Tools: Claude Code, Superpowers (Claude Code plugin), git, git worktrees, BMAD, OpenSpec, Trello (the example app being cloned)

## [Playwright CLI vs MCP Server: Which is Actually BETTER for Claude Code?](../videos/V2qjnBDZZ7A.md)
`V2qjnBDZZ7A` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: mcp-and-tools, token-cost-efficiency, coding-agents

Better Stack runs the same Twitter-video download task through the Playwright CLI and the Playwright MCP server in Claude Code, and finds the CLI cheaper in context, with MCP better for portable agent loops.

- Techniques: Drive the browser through a CLI skill instead of an MCP server (in Claude Code); Turn a repeated browser check into a bash script for humans and agents; Keep MCP for portable agent loops and trim its tool list
- Tools: Playwright CLI, Playwright MCP server, Claude Code, agent-browser (a Rust CLI that runs Playwright under the hood; spelled 'Vasell' in the auto-captions)

## [Anthropic Shows What Most Developers Are Missing](../videos/LC7kGTDoWRY.md)
`LC7kGTDoWRY` · AI LABS · 2026-02-02 · q2 · intro · news · also: coding-agents, multi-agent, enterprise-adoption

AI LABS argues that engineering is shifting from writing code to orchestrating agents, reviewing exceptions, and stating intent clearly, with a short sponsored segment and little measured evidence.

- Techniques: CLAUDE.md verification loop for long autonomous runs; Commit each verified unit, with decisions in the message; Split work into small independent units and run agents in parallel; Custom specialist subagents with chosen models and instructions; Plan mode with agent questions before building; Agent first-pass review with human review of exceptions; Layered security agents plus an external scanner
- Tools: Claude Code, CLAUDE.md, Claude Chrome extension, Puppeteer MCP, git, CodeRabbit, Cowork (Anthropic), Claude Opus 4.5, GPT-5.2, Golang, COBOL, Fortran

## [Claude Code's Creator Does This Before Every Single Project](../videos/B-UXpneKw6M.md)
`B-UXpneKw6M` · AI LABS · 2026-02-02 · q2 · practitioner · tutorial · also: claude-code, context-engineering, multi-agent

Boris, who created Claude Code at Anthropic, shares a short workflow: give the agent a way to verify its work, keep CLAUDE.md lean and team-maintained, use plan mode and scoped permissions, and run parallel or background sessions.

- Techniques: Verification line in CLAUDE.md; Tests-first or tests alongside each feature; Browser or screenshot verification for UI; Team-maintained CLAUDE.md; Mistakes from PR review go into CLAUDE.md; Project-scoped allow/ask/deny permissions; Plan mode before execution; Parallel sessions with numbered tabs; Cloud background agents with teleport; Background verification tasks; Stop hook for verification; Loop plugin for autonomous runs; Per-language linters and formatters; Committed slash commands; Narrow subagents
- Tools: Claude Code, CLAUDE.md, Claude Code GitHub action, Claude Code on the web (cloud sessions), Claude browser extension, Opus 4.5, Sonnet, Haiku, Ralph Wiggum plugin, MCP servers (Slack, Notion), BigQuery CLI, Sentry CLI

## [This is How I Design With Stitch Now](../videos/VNx9Gy5pHZI.md)
`VNx9Gy5pHZI` · AI LABS · 2026-02-02 · q3 · practitioner · tutorial · also: coding-agents, mcp-and-tools, vibe-coding-app-building

A Stitch-as-MCP design workflow in Claude Code: plan first, generate one long landing page, pull its HTML, then test with Vercel's snapshot-based Agent Browser. The Stitch MCP wrapper is unofficial.

- Techniques: Stitch MCP for agent-driven design generation; Plan-mode UI guide before design; One long page prompt instead of per-section prompts; Pulling Stitch screen code into a project; Follow-up refactor after code dump; CLAUDE.md rules that mandate a test tool; Snapshot-driven UI testing with Vercel Agent Browser
- Tools: Google Stitch, Stitch MCP (community, unofficial), Google Cloud SDK / gcloud CLI, Homebrew (brew), Claude Code (plan mode, CLAUDE.md), Gemini 3 Flash, Next.js, curl, Vercel Agent Browser, Claude's Chrome extension (compared), Playwright (compared), Puppeteer (compared)

## [ShadCN is Way too Powerful Now](../videos/MFJ0mH72_qI.md)
`MFJ0mH72_qI` · AI LABS · 2026-02-02 · q2 · practitioner · tutorial · also: claude-code, agent-architecture, context-engineering

Ralph stop-hook loop plus TDD and screenshot checks for ShadCN UI work; a separate verification iteration before the completion promise fixed premature "done" claims.

- Techniques: Stop-hook completion-promise loop; Test-first workflow inside the loop; Screenshot verification protocol; Two-phase completion gate
- Tools: ShadCN (UI component library), Claude Code, Ralph plugin (Anthropic, Ralph loop), Claude Code stop hooks, Playwright, Playwright MCP (named only to say it was not used), Notion (reference point for the board view), Automata (sponsor)

## [Why Google Antigravity Suddenly Makes Sense](../videos/e4giCKHIJy8.md)
`e4giCKHIJy8` · AI LABS · 2026-02-02 · q2 · practitioner · review · also: coding-agents, context-engineering, skills-self-improvement

A walkthrough of Google Antigravity as a coding agent, using Cursor's published harness principles: plan-first with commented revisions, on-demand context, TDD, Git as knowledge base, and skills-based debug mode.

- Techniques: Comment-driven plan revision; On-demand context instead of manual file tagging; Conversation reset policy; Project rules as markdown in .agent/rules; Skill folders following Anthropic's open standard; TDD with a committed test baseline; Screenshot as design and bug input; Git workflows as reusable commands; Agent-run code review with severity sorting; Parallel agents on separate branches; Skill-based debug mode; Watch the agent and redirect early
- Tools: Google Antigravity (AI code editor with planning mode, rules, skills and workflows), Gemini 3 (model used in Antigravity), Claude Code, Claude Opus, Cursor, Cursor's agent harness article (referenced, not named as a product), Anthropic's long-running agent harness (referenced), Anthropic's open Agent Skills standard (SKILL.md), Git, GitHub (built-in PR code review), CodeRabbit, Sentry

## [The Greatest Problem With AI Coding Is Solved](../videos/3FZIdRZsUMM.md)
`3FZIdRZsUMM` · AI LABS · 2026-02-02 · q2 · intro · talk · also: context-engineering, coding-agents, claude-code

AI LABS argues the implementation middle of software work is being replaced by agents, so developers should focus on planning, context setup, and reviewing or testing agent output.

- Techniques: Refine the plan, then run one-shot implementation; Split spec into per-concern documents; Test-first with a context reset and locked tests; Black-box testing from user stories with a browser agent; White-box review with an XML test plan and a slash command; Layered project structure for agents
- Tools: Linear, Dart AI, VS Code, Claude Code, Claude Chrome extension, Cursor, Slack, CLAUDE.md, skill.md, MCP, XML

## [Claude Code Can Now Control Your Browser (Thanks to Vercel)](../videos/P7JrP57AxR0.md)
`P7JrP57AxR0` · Better Stack · 2026-02-02 · q3 · practitioner · review · also: coding-agents, voice-multimodal, mcp-and-tools

Walkthrough of Vercel's open-source Agent Browser, a headless-Chromium CLI that lets a coding agent snapshot, click and test web pages, with a comparison to Browser Use and the Playwright MCP server.

- Techniques: Agent-driven UI verification loop; Install the CLI globally and let the agent discover it; Generate a bash regression test from the browser session; Prefer snapshot references, fall back to semantic locators
- Tools: Agent Browser (Vercel, open source), Rust, Node.js, Playwright, Chromium, OpenCode, GLM 4.7, npm, shadcn/ui (transcribed as 'Shadxian'), React (transcribed as 'Riat'), Vite, Browser Use

## [Google's Biggest Fail of the year](../videos/PB9sJnZyQ7g.md)
`PB9sJnZyQ7g` · AI LABS · 2026-01-02 · q2 · intro · review · also: context-engineering, coding-agents

A solo review of Google's Conductor, a Gemini CLI extension for spec-driven "track" workflows. The host finds the file layout sound but the command instructions weak, with destructive and falsely-completed steps.

- Techniques: Per-track spec + plan with a status index; Commit per task with git notes and git-aware revert; Default test gate on every task; Review each generated doc before auto-generation; Scope context updates to what changed; Verify completion against real state
- Tools: Conductor (Google Gemini CLI extension), Gemini CLI, Gemini (model), Claude Code plugins (mentioned as comparison), BMAD (recommended alternative), Supabase, npm, pnpm, git, git notes, GitHub

## [Inngest's New Tool Is Insane For AI Coding](../videos/8vvTHnta59A.md)
`8vvTHnta59A` · AI LABS · 2026-01-02 · q2 · intro · review · also: mcp-and-tools, coding-agents

Short demo of Inngest's MCP server for its local dev server, showing a coding agent sending test events, polling run status and checking its own workflow runs in Claude Code.

- Techniques: Wire an event-driven dev server into Claude Code via MCP; Agent-driven verify loop: send event, poll run, check result; Switch model provider through a gateway in one prompt
- Tools: Inngest, Inngest dev server, Inngest MCP server, Claude Code, Cursor, Next.js, OpenAI API, Vercel AI Gateway (auto-captioned as 'Versal'), Puppeteer MCP, CLAUDE.md, .mcp.json

## [Anthropic Released A New Way To "Vibe Code"](../videos/XWp4k9K6oK8.md)
`XWp4k9K6oK8` · AI LABS · 2026-01-02 · q3 · practitioner · tutorial · also: coding-agents, context-engineering, agent-architecture

Anthropic's long-running-agent harness: an initializer agent sets up a JSON feature list, progress file and git repo, then a coding agent implements one feature per session with browser testing and commits, so work survives compaction.

- Techniques: Initializer + incremental coder harness; Forced browser verification via Puppeteer; Resume from state, not from context
- Tools: Claude Code, Claude.md, Puppeteer, Git, Next.js, BMAD

## [Claude Released Something To Fix Your Errors](../videos/NuKrtiJqW3Y.md)
`NuKrtiJqW3Y` · AI LABS · 2026-01-02 · q2 · practitioner · tutorial · also: coding-agents, context-engineering, voice-multimodal

Tips for testing web apps with Claude Code's Chrome extension: full-page screenshot scripts, CLAUDE.md context and cookie-banner rules, split test files, progress reports across compaction.

- Techniques: Full-page screenshot script behind a slash command; CLAUDE.md rule to limit DOM extraction; Cookie-banner dismissal script run first; Authenticate before handing off the task; Split end-to-end testing into per-area test files; Progress report after each test file; Compact and check context before browser test runs; Guided testing slash command
- Tools: Claude Code, Claude Code Chrome extension (Claude in Chrome integration), Playwright MCP, Puppeteer MCP, Google Chrome, Google Docs, Google Sheets, CLAUDE.md, Chrome Manifest V3 extensions

## [5 Ways To Build Beautiful Websites Using Claude Code](../videos/VGYsHicpp34.md)
`VGYsHicpp34` · AI LABS · 2026-01-02 · q2 · intro · review · also: vibe-coding-app-building, coding-agents

A design-first workflow for building websites with Claude Code: shadcn presets, Coolers palettes, Google Stitch designs and prototypes, background browser-testing agents, and Drawbridge for visual fixes. Partly a promo for the presenter's agency.

- Techniques: shadcn preset import; Palette before layout; Design in Stitch, then hand off to Claude; Screenshot-driven inspiration; Background browser-test subagent; Drawbridge visual issue reporting
- Tools: shadcn/ui, Coolers, Google Stitch, Gemini 3 Pro, Nano Banana, Google AI Studio, Jules, Claude Code, Claude subagents (background mode), Puppeteer MCP, Drawbridge, Opus 4.5 (named as context)

## [Run AWS Locally with Docker (LocalStack)](../videos/jz7oq-Viwew.md)
`jz7oq-Viwew` · Better Stack · 2026-01-02 · q2 · intro · tutorial · also: dev-tools, sandboxing-execution

Short intro to LocalStack, a Docker-based AWS emulator. The main takeaway is to use it for the inner dev loop and CI, and still verify critical paths on real AWS.

- Techniques: Point AWS SDK, CLI and IaC at a local emulator; Ephemeral LocalStack in CI; Split test tiers: emulator for the inner loop, real AWS for critical paths
- Tools: LocalStack, Docker, AWS CLI, AWS SDKs, Terraform, AWS CDK, Serverless Framework, Testcontainers, Homebrew (brew), AWS Lambda, Amazon S3, Amazon DynamoDB

## [I Tried Google’s New AI IDE… Here’s the Truth (Antigravity)](../videos/KLq250wGeEg.md)
`KLq250wGeEg` · Better Stack · 2025-12-02 · q3 · intro · review · also: coding-agents, security-guardrails

Hands-on tour of Google's Antigravity agent IDE: a useful agent manager, plan-review flow and browser self-testing, undercut by quotas, a markdown-image prompt-injection exfiltration issue, and a half-baked preview.

- Techniques: Plan-first review gate for agent work; Browser-subagent UI self-test with visual evidence; Agent-generated visual assets for prototypes; Red-team the agent with a markdown image exfiltration test
- Tools: Google Antigravity, Gemini 3 Pro, Nano Banana Pro (speaker thinks it is used under the hood, unconfirmed), Google Jules (captions say 'Google Jewels'; speaker's comparison only), Cursor, VS Code, Chrome

## [There’s a New Way To Corrupt AI Models](../videos/D5QeUQ4VbjM.md)
`D5QeUQ4VbjM` · AI LABS · 2025-12-02 · q2 · intro · news · also: models-research, security-guardrails

Recap of an Anthropic study: teaching a model to reward-hack in coding generalized into broader misalignment, and some fixes only masked it. Secondhand and hype-titled.

- Techniques: Permissive framing for hacking in a research environment (reported mitigation); Avoid explicit 'do not hack' system prompts for measurement; Test mitigations on hard tasks, not only simple ones
- Tools: Claude Code, Claude Sonnet 3.7, Claude Sonnet 4.5, Code Cloud (sponsor, not relevant)

## [Go 1.24 Just RELEASED – Weak Pointers, Generic Aliases & More! (HUGE UPDATE)](../videos/cmtFI9eZ_UE.md)
`cmtFI9eZ_UE` · Better Stack · 2025-11-02 · q3 · intro · news · also: dev-tools

Better Stack's five-minute roundup of Go 1.24's new features: weak pointers, cleanup functions, a go.mod tool directive, Swiss-table maps, os.Root, testing/synctest, and more.

- Techniques: Weak-reference cache for large objects; Cleanup on unreachable objects; Executable dependencies via go.mod tool directive; Directory-confined file access with os.Root; Context-aware and self-restoring tests; Instant time-dependent tests with synctest; Iterator string splitting
- Tools: Go 1.24, weak package (weak.Make, Value), add cleanup (replaces set-finalizer), go.mod tool directive, os.Root (open-root function), testing/synctest (synctest.Run), testing.B.Loop, crypto/sha3, HKDF, PBKDF2, net/http protocols field, encoding/json zero-value tag (transcribed 'emit zero', described as omit-zero behavior)

## [Roo Code is AMAZING - AI VSCode Extension (better than Cursor?)](../videos/r5T3h0BOiWw.md)
`r5T3h0BOiWw` · Better Stack · 2025-11-02 · q3 · intro · review · also: coding-agents, token-cost-efficiency

Walkthrough of Roo Code, an open-source VS Code agent extension: built-in modes, auto-approve, browser self-testing, per-mode model choice and custom modes, with a Claude Sonnet vs Gemini Flash cost comparison.

- Techniques: Architect-then-code split; Enhance Prompt before sending; Category-scoped auto-approve; Browser self-check loop for UI work; Per-mode model assignment; Custom mode via prompt, then scope with file regex; Edit support prompts and attach diagnostics
- Tools: Roo Code, VS Code, OpenRouter, Claude Sonnet, Gemini 2 Flash 001, DeepSeek, Next.js, create-next-app, npm, Tailwind CSS, Cursor (comparison only), MCP (Model Context Protocol) servers

## [Spec Kit: Github's NEW tool That FINALLY Fixes AI Coding](../videos/em3vIT9aUsg.md)
`em3vIT9aUsg` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: context-engineering, coding-agents

Walkthrough of GitHub's open-source Spec Kit, a four-phase (specify, plan, tasks, implement) spec-driven workflow for AI coding agents, shown building a small Pokedex app.

- Techniques: Four-phase spec-driven loop; Resolve 'needs clarification' blocks before planning; Put performance guardrails in the plan prompt; Track progress through the tasks file
- Tools: Spec Kit (GitHub open-source spec-driven toolkit with CLI, templates and steering prompts), GitHub Copilot (agent used in the demo), Claude Code (referred to as 'CloudCode' in the auto-captions; listed as a supported agent), Gemini CLI (listed as a supported agent), Amazon Kiro (earlier spec-driven framework, mentioned only), Grok Code Fast 1 (base model for the demo; auto-captions say 'grokcodefast1'), GPT-4.1 (comparison model, one run), Zod (schema library used in the generated data model), shadcn/ui (likely; auto-captions say 'Shotzi' for the UI library)

## [Trae AI: The New Cursor AI Alternative](../videos/cdLnorNbewA.md)
`cdLnorNbewA` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, vibe-coding-app-building

Hands-on test of Trae, ByteDance's VS Code-fork IDE with a single-agent workflow and free Claude access; a to-do app and a Spotify screenshot clone show a basic UI with missing-config errors, verdict "hype".

- Techniques: Screenshot-to-app clone prompt; Built-in web view preview; Manual behavioural check of agent output; Config-first debugging for missing styles
- Tools: Trae (ByteDance IDE), Claude 3.5 Sonnet, GPT-4.0 (mentioned as promised, not available), Cursor, Windsurf, VS Code, React, Tailwind CSS, PostCSS

## [Dagger - The End of Slow, Messy YAML CI/CD Forever!](../videos/cwa_MBL1kek.md)
`cwa_MBL1kek` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: dev-tools, observability

Short Better Stack tutorial on Dagger: write CI pipelines as functions in Go (or Python, TypeScript, PHP), run them identically locally and in GitHub Actions, cache volumes, and debug with a terminal breakpoint.

- Techniques: Daggerize a Go project; Write a test function that runs in a container; Replace GitHub Actions YAML with a single Dagger call; Cache dependency downloads with a volume; Debug a failing pipeline interactively; Reuse modules from the Daggerverse
- Tools: Dagger, Dagger Go SDK, Dagger Python SDK, Dagger TypeScript SDK, Dagger PHP SDK, Docker, GitHub Actions, Act, Go, Alpine container image, Homebrew, OpenTelemetry

## [Traycer is INSANE… Cursor AI is Not Enough Anymore](../videos/0hAS1xCeixQ.md)
`0hAS1xCeixQ` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, context-engineering

A product walkthrough of Traycer, an IDE extension that runs a planning stage (gap-filling questions, phased plan), implementation, and a self-review pass before or alongside coding agents such as Claude Code and Cursor.

- Techniques: Clarify-before-plan requirements file; Phased plan as the unit of execution; Plan handoff to a coding agent; Severity-classed self-review pass; Change tracking with M/N badges; Version-conflict repair by dependency pinning
- Tools: Traycer (IDE extension, sign-up required), Next.js, TypeScript, Tailwind CSS (v3 before the intentional upgrade), HeroUI (named as Hero UI), NextUI (mentioned as the wrong provider), shadcn (mentioned as a common library), Claude Code, Cursor

## [Develop Faster using the browser tools MCP Cursor/Windsurf.](../videos/G25UyWfYogQ.md)
`G25UyWfYogQ` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: mcp-and-tools, coding-agents

Walkthrough of the browser-tools MCP server, which lets Cursor's agent run accessibility/SEO/performance audits, read screenshots and selected DOM elements from Chrome, and iterate on front-end fixes.

- Techniques: Install browser-tools MCP into Cursor; Load the Chrome extension and start the connector; Accessibility audit and fix loop; Configure screenshot folder and auto-paste; Select-element targeting; Voice mode for prompting
- Tools: browser-tools MCP server (browser-tools-mcp, GitHub repo linked in the description), Cursor (IDE and agent), Windsurf (mentioned for its select-element feature), Chrome browser extension (browser-tools), Chrome DevTools (Browser Tools MCP tab for settings and screenshot folder), mcp.json (Cursor MCP config file), React (demo app's calendar component)

## [Anthropic Claude AI Agentic Browser: The Claude Chrome Extension for Builders (EXCLUSIVE DEMO)](../videos/TVetQbcgdMU.md)
`TVetQbcgdMU` · AI LABS · 2025-11-02 · q3 · practitioner · review · also: coding-agents, voice-multimodal

Hands-on demo of Anthropic's Claude Chrome extension as a visual-testing partner for Claude Code: a slash command reviews each finished task on a running dev server, and the browser agent reports visual and functional issues.

- Techniques: Per-task visual review slash command; Fresh chat per task; Prioritized improvement triage before the next task; Batch review of several tasks; Per-site approval allowlist for browser actions
- Tools: Claude Code, Claude Chrome extension (Claude browser extension, research preview), Claude 4 series models, Next.js, GPT (used to brainstorm the app idea), BMAD method (mentioned, not used), Playwright MCP (compared, not used), Cursor (mentioned as a competitor)

## [Automation Testing Tutorial Using Cursor AI + Operative.sh & Claude 4 (Setup + Demo)](../videos/GuKdinu64Z0.md)
`GuKdinu64Z0` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: mcp-and-tools, coding-agents

Walkthrough of installing operative.sh's web-eval MCP agent into Cursor and using plain-English test cases, including edge cases, to drive a Playwright browser against a local login page. Vendor-specific, thin on evidence.

- Techniques: Install operative.sh web-eval MCP into Cursor; Call the web eval agent with url, task and headless; Save an authenticated session once with setup-browser-state; Generate test cases to a file, then run them sequentially and write results back
- Tools: operative.sh (web eval agent, setup-browser-state tool, MCP installer, API key), Cursor (IDE, MCP host), Playwright (browser automation, installed by the setup), Claude 4 (Anthropic model; the presenter says it was released 2-3 days before recording and praises it), Aceternity UI (the demo site's UI library; auto-caption reads it as 'as eternity ui'), MCP (Model Context Protocol, the integration path)

## [Leap Year Bugs: From Satellites to Spreadsheets](../videos/2VtNFOaRgTw.md)
`2VtNFOaRgTw` · Better Stack · 2025-11-02 · q2 · intro · other · also: dev-tools

Better Stack walkthrough of leap-year bugs in satellites, Excel, Python, JavaScript and Zune, with the Gregorian leap-year rule and the Lotus 1-2-3 1900 bug that Excel kept for compatibility.

- Techniques: Gregorian leap-year check; Edge-case test years for date logic; Check for silent date rollover
- Tools: Python, JavaScript (Date object), Excel, Lotus 1-2-3, Zune, Claude (used to generate the buggy GPS-to-UTC example code), The Register (cited source)

## [Auto Claude is HERE… Upgrade your Claude Code Workflow](../videos/ytn0aXK2gzE.md)
`ytn0aXK2gzE` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: claude-code, dev-tools

AI LABS shows how to attach Claude Code hooks (formatter, linter, build, stop-sound) to settings.json, and how to have a general LLM draft per-language hook rules. Mostly a SwiftUI demo with a sponsor segment.

- Techniques: Post-edit hooks as hard quality gates; Feed check output back to the agent; Stop-event sound notification; Generate hooks from a rules file; Accessibility audit as a hook; Autonomous run from a task file
- Tools: Claude Code, Claude Code hooks (settings.json), ChatGPT (used to draft lint and format rules), swift-format, SwiftLint (swiftlint.yml), SwiftUI, SQLite (local database in the demo app), Prettier (example formatter for other languages), Black (Python formatter, example in the rule-to-hook walkthrough), BMAD method (mentioned as a better approach, not used), claude code rule to hook (GitHub repo, name as spoken; exact repo not confirmed), tools.md (presenter's reference file of Claude Code tools and execution points; not shown)

## [Github Spec Kit FINALLY Fixed AI Coding](../videos/M0ivqkQ5mF4.md)
`M0ivqkQ5mF4` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: context-engineering, coding-agents, multi-agent

A walkthrough of GitHub Spec Kit's specify, plan and tasks workflow driving Claude Code on a demo app, with an honest verdict: the spec-first flow works, but tasks run by hand and the UI came out cluttered.

- Techniques: Requirements in a general chat model before spec-kit; Run /specify with the requirements and answer the clarification flags; Run /plan after the spec is settled; Run /tasks and write tests before implementation; Run independent tasks in parallel with sub-agents
- Tools: GitHub Spec Kit ("Specify"), Claude Code, ChatGPT, Gemini (supported assistant), GitHub Copilot (supported assistant), ShadCN UI components, Notion (visual theme followed), git

## [Agents Can FINALLY See the Frontend (Chrome DevTools MCP)](../videos/zaXKZjJvaAs.md)
`zaXKZjJvaAs` · Better Stack · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, coding-agents

Walkthrough of Chrome's DevTools MCP server, which lets a coding agent open, inspect, audit, and automate pages in a real Chrome instance. Mostly a prompt-driven demo with little setup detail.

- Techniques: Attach Chrome DevTools MCP to a coding agent; Prompt for a performance audit targeting LCP; Repeat the audit under network throttling; End-to-end flow and API check through the browser; Debug console errors and failed network requests
- Tools: Chrome DevTools MCP (Chrome's MCP server for coding agents), GitHub Copilot (agent used in the demo), Recommendoo (demo app built by the host with vibe-coding), OpenAI API (used by the demo app for suggestions), Watch Mode API (used by the demo app for title data)

## [Clone Any Website INSTANTLY! New V0 Updates You Need to See.](../videos/gNgxnECvLWM.md)
`gNgxnECvLWM` · AI LABS · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building

Walkthrough of v0's new URL-to-clone, built-in console logs, version rollback and click-to-edit features, shown on one Notion homepage clone; thin substance behind a hype title.

- Techniques: Clone a page from its URL; Log-driven debugging loop; Roll back and rebase on a known-good version; Scoped edits by element selection
- Tools: v0

