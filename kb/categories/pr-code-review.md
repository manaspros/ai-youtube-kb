# pr-code-review — 77 videos

*AI code review, PR review bots, review workflows, quality gates on agent-written code*

By channel: AI Engineer 55 · AI LABS 8 · Better Stack 14

**Synthesized guide:** [guides/pr-code-review.md](../guides/pr-code-review.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [AI Writes Code Faster Than Your Team Can Review It - Andrew Norrish, Sourcegraph](../videos/-X3yXTwGs9A.md)
`-X3yXTwGs9A` · AI Engineer · 2026-11-02 · q2 · practitioner · talk · also: enterprise-adoption, observability

Sourcegraph's field director argues AI code outpaces human review, so SRE and platform teams need code-search-driven investigation, monitors and bulk remediation. Mostly a vendor pitch.

- Techniques: Deterministic cross-repo code search for incident root cause; Commit-pattern monitors for AI-written code; Bulk remediation across repos; Webhook-triggered agentic triage; Automated RCA from deploy history; Eval-gated code-review agent over historical branches
- Tools: Sourcegraph (code search, code graph, Deep Search, MCP server), HackerOne, git (history search for incident commits)

## [I Made a Fruit Fly Review My Code - Nick Nisi, WorkOS](../videos/geMAe-PLJF4.md)
`geMAe-PLJF4` · AI Engineer · 2026-11-01 · q3 · intro · talk · also: testing-verification, software-factory

Nick Nisi (WorkOS) demos a fruit-fly connectome trained to approve or reject code diffs, and argues humans should review for intent and proof of work, not bugs.

- Techniques: Team-owned review skill as a gate; Tiered PR escalation pipeline; Agent proof-of-work bundle for review; Measure the reviewer on a labelled diff set; LLM as structured feature extractor before a non-LLM classifier
- Tools: fruitfly.review (speaker's online demo of the fly reviewer; URL as spoken), Greptile (automated AI PR reviewer, named as a comparison), CodeRabbit (automated AI PR reviewer, named as a comparison), Codo (automated reviewer named in the pipeline; name as spoken, may be a caption error), Claude and Codex (named as coding agents that solved the coding problem), Pi (the speaker's coding agent, referenced via 'Pi extensions'; spoken name), GitHub code owners (used to route PRs to the DX team), GEV / JEV / CLEF (LLM and classifier names as spoken; likely auto-caption errors; the LLM is described as a 'System 1 model' that produces the 30 questions), Doom and Beat Saber (prior fruit-fly demos mentioned as context, not tools for the reader)

## [Anthropic Just Released A New System For Using Claude Code](../videos/S49gppZl8H0.md)
`S49gppZl8H0` · AI LABS · 2026-10-31 · q2 · practitioner · tutorial · also: claude-code, testing-verification, multi-agent

Walkthrough of Anthropic's Claude Code review system, rebuilt as skills: eval.md gates before build, a fresh-context builder/verifier/reviewer loop, risk tiers, and git rollback.

- Techniques: Eval-first feature gating; Fresh-context builder/verifier/reviewer loop; Reviewer loop stop rules; review.md with a learned-rules section; Consequence-based risk tiering; First-time-user agent test; Git branch per feature with rollback
- Tools: Claude Code, CLAUDE.md, review.md, eval.md, state.md, Claude Code code review command, skills, subagents, hooks, git, Codex, Cursor

## [Catch the Bugs Your Code Review Misses - Killian Carlsen-Phelan & Taylor Luttrell-Williams, Sonar](../videos/wP3P89YB9fA.md)
`wP3P89YB9fA` · AI Engineer · 2026-10-30 · q2 · practitioner · review · also: testing-verification, context-engineering

Sonar's hands-on workshop for Guitar, a PR-level verification agent that reviews agent-written code, diagnoses CI failures, auto-fixes and auto-merges. Vendor pitch with a usable setup walkthrough.

- Techniques: Install Guitar as a GitHub app and connect a repo; Fork the workshop repo with all branches and enable Actions; Open PRs against your own fork, not upstream; Apply Guitar fixes; Steer reviews with project context in .guitar/review; Write conditional rules in .guitar/rules; Turn on auto-merge safely with a branch ruleset
- Tools: Guitar (Sonar's code change verification agent, GitHub app, app.guitar.ai), SonarQube (called SonarCube in the transcript, static analysis), GitHub (PRs, Actions, branch rulesets, auto-merge), Jira, Linear, Slack, MCP (Guitar supports MCP connectivity for custom context), Python (sample Box Office ticketing app, orders.py, check-in.py)

## [Why a One-Line Change Can Break Your Whole Stack - Cole Gannaway, Qodo](../videos/YqxpPI7YUjE.md)
`YqxpPI7YUjE` · AI Engineer · 2026-10-29 · q2 · intro · talk · also: context-engineering, multi-agent, software-factory

A Qodo solutions engineer argues PR review is the bottleneck in AI software factories and needs cross-repo blast-radius context, independent reviewers and rules learned from past reviews. Mostly a product demo.

- Techniques: Blast-radius-aware review over a software graph; Rules learned from review comments; Pre-generation context injection; Independent, varied reviewers; Mid-run review checkpoints via skill; Ticket-linked PR review
- Tools: Qodo (spoken as Kodo), Jira, Linear, MCP servers, Claude Code, Anthropic models, OpenAI models, Bitwarden (example repo, open source password manager), CLI

## [AI That Hunts Logic Bugs Before Attackers Do - Taylor Luttrell-Williams, Sonar](../videos/UW8Qkk7MG8A.md)
`UW8Qkk7MG8A` · AI Engineer · 2026-10-29 · q2 · intro · demo · also: security-guardrails, agent-architecture

Sonar's SonarQube Hunter Agent: an on-demand/scheduled AI security agent that maps a repo, runs three specialized issue-class agents with adversarial validation and noise gates, and surfaces logic/authz flaws (IDOR, broken access control, business logic, auth/session) in SonarQube's normal issue list.

- Techniques: Multi-agent security scan with validation gates; Layered verification: SAST plus logic-level agent; Triage workflow for AI-raised issues
- Tools: SonarQube Hunter Agent, SonarQube (Cloud and Server), SonarQube remediation agent, SAST, SCA, OpenAI Daybreak Cyber Partner Program (frontier cybersecurity models)

## [How Anthropic Merges 30,000 Code Changes a Day - Manish Kapur, Sonar & Addy Osmani, Anthropic](../videos/AnsXWH2_EBU.md)
`AnsXWH2_EBU` · AI Engineer · 2026-10-29 · q3 · practitioner · panel · also: testing-verification, software-factory, governance-compliance

Sonar and Anthropic discuss verification as the bottleneck for agent-written code, covering layered checks, codified taste in CLAUDE.md/AGENTS.md, labeling agent PRs and the lights-on vs dark software factory spectrum.

- Techniques: Verification-first agent loop with a first-pass reviewer; Codify taste in CLAUDE.md or AGENTS.md for review agents; Require verification evidence before human review; Layered verification stack; Label agent-authored PRs and keep a named human owner; Agent guide rails and permission control
- Tools: Claude Code (called 'Cloud Code' in the transcript), Claude (claude.ai web product), Opus 5.5 (Anthropic model, named as a reference point for model quality), Anthropic code review product (named only as a product Anthropic offers), CircleCI (cited statistic), Sonar (verification vendor; survey and product referenced), CLAUDE.md / AGENTS.md (agent instruction files)

## [Agents That Self Improve While You Sleep - Fuad Ali, Arize AI](../videos/UGuNt2_Oz8s.md)
`UGuNt2_Oz8s` · AI Engineer · 2026-10-27 · q3 · practitioner · workshop · also: evals, observability, skills-self-improvement

A vendor-led workshop on closing an agent self-improvement loop: scheduled trace review, failure datasets, evals, replay experiments, and human checkpoints at the high-leverage points.

- Techniques: Trace-to-fixture pipeline; Trajectory-level LLM-judge eval; Cheap-first evaluator stack; Replay-based fix validation; Confidence-threshold human routing; Session-level eval signals; Stop criteria for eval depth
- Tools: Arize AX (tracing and evals platform), AX CLI, Arize Signal (always-on trace-review agent), Arize Alex (in-house agent), Phoenix (mentioned, not demonstrated), Arize managed sandboxes, GitHub, Codex, Cursor, Claude Code, OpenCode, Modal

## [How to Build an AI Code Review Agent - Daksh Gupta, Greptile](../videos/4UtrRVtUN_g.md)
`4UtrRVtUN_g` · AI Engineer · 2026-10-26 · q4 · practitioner · talk · also: context-engineering, token-cost-efficiency, testing-verification

Greptile co-founder Daksh Gupta walks through building a production AI code review agent: sandboxed test runs, historical bug catalogs, model inversion, a living code wiki for context, and tiered model routing to cut per-PR cost.

- Techniques: Prompt the reviewer for a catalog of bug types, not generic review; Historical-PR regression eval for the review agent; Model inversion for reviews; Codebase knowledge base indexed by subsystem; Dependency-rich sandbox with computer-use end-to-end tests; Tiered model routing across review subtasks; Model-agnostic harness for the review agent
- Tools: Firecracker, OpenCode, Pi, Codex, Claude Code, GitHub review API, GitHub, GitLab, Jira, Linear, Confluence, Notion

## [AI Writes the Code. So What's Left for Engineers? - Laurie Voss, Arize AI](../videos/kspZP5BgkEU.md)
`kspZP5BgkEU` · AI Engineer · 2026-10-25 · q3 · practitioner · talk · also: context-engineering, product-ux, evals

Laurie Voss (Arize AI) argues coding agents have made code writing nearly free, so the bottleneck moves to code review, ops and security, and ultimately to defining what "good" means, which makes "product engineers" the lasting role.

- Techniques: Theory-of-constraints bottleneck mapping; Review only high blast-radius code; Automatic verification for cheap-to-check work; Turn reviewer feedback into rules; Mergeability benchmark instead of test pass rate; Measure outcomes, not output volume
- Tools: Claude Code, GitHub Copilot, Cognition Devin, Cursor Bugbot, OpenAI Codex, Claude, Pragmatic Engineer newsletter, Arize AI

## [Anthropic Barely Reads Claude's Code Anymore](../videos/d8QpDbBKbAU.md)
`d8QpDbBKbAU` · Better Stack · 2026-10-20 · q4 · practitioner · news · also: claude-code, evals, multi-agent

Secondhand summary of how Anthropic reviews Claude Code's own PRs: layered automated review, risk-tiered human sign-off, incident-derived reviewer evals, and round caps for agent-vs-agent loops.

- Techniques: Layered review pipeline with a voting gate; Turn repeated reviewer findings into durable rules; Per-directory review.md written by code owners; Merge gate with explicit false-positive dismissal; Incident-derived reviewer eval with a keep-or-drop rule; Noise metric from comment outcomes; Round cap, scoped re-review, and whole-class flagging for agent loops; Risk tiering with a classifier agent and a second check
- Tools: Claude Code, CLAUDE.md, review.md, PR template, lint rules, CI (tests, type checking, linting)

## [Rebuilding CI for AI-Scale Commit Volume — Gautam Korlam, Sonar](../videos/7b9tov5Uc5s.md)
`7b9tov5Uc5s` · AI Engineer · 2026-10-15 · q3 · practitioner · talk · also: software-factory, governance-compliance, infra-cost-scaling

Gautam Korlam (Sonar/QAR, ex-Uber) on why CI, merge queues and review were built for human speed, and how to keep agent-scale commits green, fast and auditable in regulated teams.

- Techniques: Parallel speculative merge queue; Move checks left and offload expensive checks; Cache, shard and reduce compiler churn; Layered AI review with a fast first pass; Policy-based auto-approval with escalation; Durable decision record on the PR
- Tools: Rust, GitHub, Next.js (captioned 'next text'), Uber SubmitQueue (captioned 'summit cube')

## [How to Build Quality Gates into Agentic Coding Workflows — Nnenna Ndukwe, Qodo AI](../videos/-AKPRSYccJc.md)
`-AKPRSYccJc` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: context-engineering, coding-agents, testing-verification

Hands-on workshop by a Qodo DevRel on wiring codified rules, skills, structured plans and deterministic gates into an agentic coding loop from planning through PR review and autofix.

- Techniques: Codified rules and skills pulled per phase; Structured high-level plan plus execution plan; Read-only plan mode with an explicit skill handoff; Local verification command as the gate; Audit skills during implementation; Review-findings autofix loop; Severity-tiered rules with merge blocking
- Tools: Qodo, Claude Code, Codex, Semgrep, Ruff, Pyright, Bandit, pytest, GitHub CLI, uv, conventional commits, git worktrees

## [The SDLC You Build Yourself — Andy Wong, Andrei Bocan & Shane Wolf, Atlassian](../videos/ojJXgXLUQFc.md)
`ojJXgXLUQFc` · AI Engineer · 2026-10-12 · q2 · intro · workshop · also: software-factory, context-engineering, governance-compliance

Atlassian team walks through its AI SDLC stack (Jira Coding Agent, AI Reviewer, AutoDev, AI SRE, AI Planner) built on a shared context engine, with a hands-on workshop that was largely lost to Wi-Fi problems.

- Techniques: Org-wide standards as enforceable PR rules; Trained filter on review comments; Human-set authority flag on context sources; Acceptance-criteria self-check in a sandbox; Progressive migration with per-engineer quotas; Automation-triggered agent session per sub-ticket; Per-skill and per-subagent model selection; Spend caps and WIP limits on autonomous work
- Tools: Jira Coding Agent, AI Reviewer, AI AutoDev, AI SRE, AI Planner, Rovo Dev, Teamwork Graph CLI, Confluence, Bitbucket, Slack, Docker, Claude

## [Stop Prompting — Greg Pstrucha, Sentry](../videos/E3KbFLAGD6A.md)
`E3KbFLAGD6A` · AI Engineer · 2026-10-10 · q3 · practitioner · talk · also: context-engineering, testing-verification, coding-agents

Sentry's Greg Pstrucha argues teams should stop re-prompting coding agents and instead codify repeated conventions as deterministic lint rules, skills checks, and policy-driven review loops.

- Techniques: Mine feedback to find lint-worthy rules; Custom AST lint rules with ast-grep or ESLint-style tools; Lint for schema sync; Validate code examples inside skill documents; Policy files plus per-policy sub-agent review loop; Hooks to run deterministic checks at the right moment
- Tools: ast-grep, ESLint, OxLint, Flake8, Clippy, Claude Code skills, OpenAPI schema, Django REST Framework, a plain-English lint tool transcribed as 'TaskLessware' (name uncertain from auto-captions)

## [Generation Is Cheap, Review Is Expensive: How to Stop Shipping AI Slop — Gabriel Martinez, G2i](../videos/6qkzlT962es.md)
`6qkzlT962es` · AI Engineer · 2026-10-10 · q3 · intro · talk · also: context-engineering, software-factory, product-ux

Gabo (G2i) argues AI slop comes from generation outrunning judgment. His fixes are conventions, small reviewable chunks, visible accountability, and ORC, an orchestration workflow built around review.

- Techniques: Single canonical pattern per concept; Diagram-first review surface; Small reviewable chunks with explicit ownership; Built-in adversarial and planning gates before merge
- Tools: ORC (G2i's orchestration system, described only at a high level), Ruby on Rails (convention-over-configuration example), SQLite (quoted maintainer comment on PR maintenance cost)

## [AI Writes More PRs. Who Validates Them? — Ali-Reza Adl-Tabatabai, Sonar](../videos/uuwDWRbxoYo.md)
`uuwDWRbxoYo` · AI Engineer · 2026-10-09 · q2 · intro · talk · also: software-factory, observability

Sonar's Ali-Reza Adl-Tabatabai pitches an agentic PR validation system (ex-Guitar) that reviews, fixes, and auto-merges PRs, with a trust ladder for rollout. Mostly product pitch, few numbers.

- Techniques: Trust-gated automation ladder; Autofix loop until green; Flaky-test detection and rule-based retry; Agent plus static-analysis hybrid; Model routing proxy with failover; Aggregate PR and CI analytics
- Tools: Sonar, SonarQube, Guitar (agent platform)

## [AI Hackers Are Faster Than Your Pen Test — Eli Cohen, Snyk](../videos/f3o0-9Dlw3E.md)
`f3o0-9Dlw3E` · AI Engineer · 2026-10-08 · q2 · intro · talk · also: security-guardrails, multi-agent

Snyk's Eli Cohen argues LLM-generated code and LLM attackers make twice-yearly pentests obsolete, and pitches a continuous, per-PR AI pentest pipeline (Snyk Evo) with an exploit-validation judge.

- Techniques: Layered agent pipeline for continuous pentesting; Scanner output as LLM context; Exploit proof gate before flagging; Per-PR security trigger
- Tools: Snyk Evo (Snyk's continuous AI offensive security / AI pentesting offering, named in the talk), Snyk (company), Helios (runtime security company, acquired by Snyk), Claude Code (called "cloud code" in captions), Codex (OpenAI coding agent), SAST (static application security testing), DAST (dynamic application security testing; captioned as "dust"), MCP (Model Context Protocol), Mythos (model named in passing; exact referent unclear)

## [Redesigning How Software Gets Built With AI Agents — Sonar & McKinsey Panel](../videos/XqF-IFHBCkM.md)
`XqF-IFHBCkM` · AI Engineer · 2026-10-08 · q3 · intro · panel · also: enterprise-adoption, software-factory

Sonar and McKinsey panel on why most companies stall before scaling AI agents in the SDLC, and a staged trust ladder for moving from agent review to fully automated PR merge.

- Techniques: Staged autonomy ladder for agent PR workflows; Derive verification evals from the PRD; Lighthouse teams for best practice; Baseline developer metrics before automation; Write down implicit conventions as explicit specs

## [The State of AI in Software Development: Data from 400+ Orgs — Justin Reock, DX](../videos/Se8jHLliLXE.md)
`Se8jHLliLXE` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: enterprise-adoption, observability

DX's deputy CTO shares 2025-26 data from 400+ orgs: AI lifts delivery speed only modestly, quality volatility grows, and PR size and falling change confidence are the warning signs.

- Techniques: Cohort-vs-foundational-metric comparison; Utilization, impact, cost framing; Agent feedback as telemetry; Agent-readiness audit; Agent first-pass PR review kept in the PR thread; Bottleneck-first AI adoption
- Tools: DORA metrics, DX platform

## [The Death of the Code Review: What the Data Actually Says — Laurie Voss, Arize AI](../videos/_mi3alkqy4s.md)
`_mi3alkqy4s` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · also: evals, testing-verification, observability

Laurie Voss (Arize AI) argues that agent code generation has outrun human review, so teams should stop reviewing PRs by hand and build an engineered review harness, with humans designing its definition of good.

- Techniques: Multi-pass review with consensus filtering; Default-suspicious reviewer prompt; Tool-using reviewer over the whole repo; Runtime verification by the agent itself; Machine-checkable mergeability rubric; Codify the definition of good as a harness
- Tools: GitHub Copilot code review, Cursor reviewer, CodeRabbit, Greptile, Graphite, Codex, Anthropic automated security review action, SWE-bench, SWE-bench Pro, FrontierBench

## [Why AI Didn't Actually Make You Ship Faster — Gabriel Spencer-Harper, Meticulous](../videos/HLTa7Vcs4X0.md)
`HLTa7Vcs4X0` · AI Engineer · 2026-10-04 · q2 · intro · demo · also: testing-verification

A short vendor demo arguing that review and verification, not code writing, are now the bottleneck, and that screenshot-based record-and-replay of front-end flows can give near-exhaustive verification.

- Techniques: One-line record of real user flows in non-prod; Per-step screenshot diff of base vs PR; Record-time network mocking with replay-time stubs; Coverage-maximizing test subset selection
- Tools: Meticulous, Cypress, Playwright

## [How VS Code Went from Monthly to Weekly Releases with AI — Harald Kirschner](../videos/I2LL_wd89-A.md)
`I2LL_wd89-A` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · also: software-factory, testing-verification, context-engineering

How the VS Code team moved from monthly to weekly releases by rebuilding its own dev system around agents: code-survival metrics, agent-readable repos, fast CI, UI feedback loops, AI triage, and staged rollouts.

- Techniques: Code survival metric; Agent-readable repo docs; Expert knowledge as a shared skill with an area owner; Screenshot-diff component browser; Self-correcting launch loop; Tiered AI code review; Deterministic filtering before agent action; Staged rollouts with error monitoring; Evals bootstrapped from issues; Prototypes instead of PRs for design talks
- Tools: VS Code, GitHub, GitHub Issues, GitHub Copilot code review, TypeScript Go, Playwright, Electron, Xcode MCP, AGENTS.md, Chrome extension

## [AI-Generated Code Is Already Competing With Human Code — Daksh Gupta, Greptile](../videos/474j-n1Ltxc.md)
`474j-n1Ltxc` · AI Engineer · 2026-10-04 · q4 · practitioner · talk · also: coding-agents, evals

Greptile's Daksh Gupta uses review data from its own PR pipeline to test whether fully agent-written PRs are worse than human PRs; his answer is roughly no on reverts, severity and review rounds, but failure modes differ by agent.

- Techniques: Signal-based detection of agent-authored PRs; Proxy quality metrics for agent PRs; Per-agent failure-mode profiling via keyword counts; Three-question PR validation gate
- Tools: Greptile, Codex, Claude Code, Devin, Cursor, GitHub

## [Software Engineering Is Becoming Factory Engineering — Zach Lloyd, Warp](../videos/tUPPVhBBcoM.md)
`tUPPVhBBcoM` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: software-factory, skills-self-improvement, observability

Warp's founder argues software engineering is becoming factory engineering: agent loops run from triage to spec to implementation to monitoring, with humans gating stuck points and observer agents improving the skills.

- Techniques: Software factory loop with human gates; Triage routing by ambiguity; Product spec plus tech spec; Observer agent skill loop; Verification by running the product
- Tools: Warp, Claude Code, CI/CD, GitHub, Computer use

## [Your AI Agent Just Changed 40 Files... Now What? (Whiteboard)](../videos/cP5PRDo3u6Q.md)
`cP5PRDo3u6Q` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: coding-agents, claude-code, dev-tools

Walkthrough of Whiteboard, an open-source Mac app that lets a coding agent draw linked review diagrams of its own branch changes, with a privacy warning about its default telemetry.

- Techniques: Install Whiteboard as a Claude Code plugin; Turn telemetry off before opening a private repo; Review-only prompt with tool-call approval; Click-through verification of diagram blocks; Typed diagram blocks instead of free-form output; Diff reduction for large agent branches; Own-backend OpenTelemetry instead of vendor telemetry; Check trace storage before enabling trace capture
- Tools: Whiteboard (open-source Mac app, MIT, VS Code fork), Claude Code, Codex, Cursor, OpenCode, VS Code / Code OSS, Electron, Rust (diff engine), MCP, Mermaid, Archify, CodeRabbit

## [Insane Jev Use Cases You Need To Use Right Now](../videos/2nc_QMuNp18.md)
`2nc_QMuNp18` · AI LABS · 2026-10-02 · q2 · practitioner · review · also: claude-code, token-cost-efficiency, context-engineering

AI LABS shows seven Claude Code workflow hooks that offload yes/no, ranking and routing decisions to "Jev", a decision-only model with a confidence value, to cut latency and token spend.

- Techniques: Decision-model offload via gateway; Compaction replacement via project-local hook; Doc-rule to test coverage hook; Per-prompt skill picker hook; Keyword search then batched LLM rerank for Explore; Seven yes/no review gate; Browser agent with model-picked clicks; Pre-edit rule enforcement hook
- Tools: Jev (TypeSafe decision model, as auto-captioned), Vercel AI Gateway, OpenRouter, Claude Code, Codex, Fast Jev Compaction plugin, Claude Code Explore subagent, Opus (caption reads 'Opus 2'), Zapier (sponsor segment)

## [How To Use Claude Code To Build Amazing Sites With Opus 5.5](../videos/DP7mgLUKN_U.md)
`DP7mgLUKN_U` · AI LABS · 2026-10-02 · q3 · intro · tutorial · also: vibe-coding-app-building, claude-code, context-engineering

Six-stage tutorial for building non-generic websites with Claude Code: plan mode, CLAUDE.md business context, a design-rules skill, design.md, git/GitHub/Vercel deployment, branch + PR review, and a 3D scroll skill.

- Techniques: Plan mode before building; Enrich CLAUDE.md with business context; Install and apply a design-rules skill to an existing project; Lock visual style with design.md; Commit checkpoints and set up GitHub via the CLI; Deploy from GitHub to Vercel; Feature branch, PR, and automated review loop; Scroll-driven 3D site via ScrollWorld skill
- Tools: Claude Code, Opus 5.5, Sonnet, Fable, Warp, VS Code, Next.js, Vercel, Vercel CLI, GitHub, GitHub CLI (gh), CodeRabbit

## [Fixing the PR Bottleneck — Matt Pocock, AIHero](../videos/LlgiOCmFG_w.md)
`LlgiOCmFG_w` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: software-factory, testing-verification, context-engineering

Matt Pocock on clearing the PR backlog that AI agents create: layer cheap deterministic checks, have an agent review and commit fixes, design deep modules so tests stop being brittle, and run a retro on each session.

- Techniques: Layered brakes for agent PRs; Deep-module design for agent-testable code; Separate implementer and reviewer contexts; Reviewer commits fixes, comments only on open questions; Door-type and blast-radius PR summary; Pseudocode and diagram PR explanations; Retro over sessions and PRs
- Tools: AGENTS.md, coding-standards.md, CodeRabbit, Cursor BugBot, PlanetScale, Opus 5 (model mentioned in the tautological-test example), AIHero skills (version 1.3 announced for the same week)

## [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../videos/qdAkxLoYNI8.md)
`qdAkxLoYNI8` · AI Engineer · 2026-09-18 · q2 · intro · review · also: context-engineering, rag-retrieval, mcp-and-tools

Unblocked vendor talk arguing coding agents need an organizational context engine over code, PRs, Slack and docs, with cited sources; one live comparison, mostly product pitch.

- Techniques: Cited-source answers for agents; With/without context comparison; Expertise-weighted review comments; Query historical PR data with an open-source engine; Engineering social graph from review edges
- Tools: Unblocked, Claude Code, Claude 4.8, Slack, Notion, GitHub, MCP, Document Query Engine, context engine simulator

## [Building uReview, Uber’s Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../videos/EL123UNokkI.md)
`EL123UNokkI` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: evals, multi-agent, observability

Uber's engineers explain uReview, their multi-agent code review system: how they built feedback-driven evals, team-owned customizations, and a cost/quality loop, plus why they think humans move up to an expanded outer loop.

- Techniques: Reply-sentiment and addressal-rate tracking; Trajectory-based runtime tuning with turn guardrails; Tiered review generators with post-processing; Few-shot AI linters with deterministic context; Ownership-coupled rule distribution
- Tools: GitHub, Fabricator, Claude

## [From Tokenmaxxing to Trusted Throughput — Mingsheng Hong, Ironclad](../videos/dSg0pu8d6qg.md)
`dSg0pu8d6qg` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: token-cost-efficiency, governance-compliance

Ironclad's VP of AI Engineering on controlling AI token spend: measure cost against value, treat usage dashboards as smoke detectors, and fix the review and CI bottlenecks that code generation creates.

- Techniques: Cross-tool cost aggregation; Usage as an anomaly signal; LLM T-shirt sizing of merged PRs; Three-bucket trusted-throughput check; AI-first review gate; Bounded agent fix loops; Prompt-cache-friendly prompt layout; Context pruning and summarizing in long sessions; Buy non-differentiating tools, build a prompt playbook; Developer-experience metrics for CI
- Tools: Claude Code, Codex, Cursor, vendor usage dashboards, LLMs for PR complexity scoring, CI/CD pipeline

## [How to build an AI-Native Health Company — Dan Feng, Maven Clinic](../videos/WJRdLNhrsLQ.md)
`WJRdLNhrsLQ` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, evals

Maven Clinic's CTO-level account of becoming an "AI-native" health company: AI in internal work and product, shorter planning cycles, changed code review, and tiered reliability bars with rubric-based evals.

- Techniques: Staged AI-coding adoption from low-risk tasks; Self-declared review tiers with accountability; Repeated-run pass-rate gating for non-deterministic tests; Rubric scoring plus human spot-checks on live conversations; Per-feature failure tolerance with multi-model agreement and human fallback
- Tools: Cursor, Claude Code, Jira

## [The Last Human Code Review: Building Trust in AI-Generated Code — Itamar Friedman, Qodo](../videos/s-aixZYJG4c.md)
`s-aixZYJG4c` · AI Engineer · 2026-09-18 · q2 · practitioner · talk · also: context-engineering, governance-compliance, enterprise-adoption

Qodo's CEO argues human code review will become optional only once teams codify tribal knowledge into a context engine that serves both humans and agents, with per-rule analytics and graduated auto-approve/block.

- Techniques: Rule-linked review comments; Agent-directed PR summary comments; Per-rule analytics for review standards; Learning context from accept/reject history; Graduated auto-approve and auto-block; Service-contract graph for PR impact
- Tools: Qodo, Claude Code, AGENTS.md, CLAUDE.md

## [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../videos/qqrk7CtkuIw.md)
`qqrk7CtkuIw` · AI Engineer · 2026-09-18 · q3 · practitioner · interview · also: software-factory, coding-agents, enterprise-adoption

Anthropic's Mike Krieger on how Labs builds: delegate end states to agents, be less constrained with tools, share intent instead of 2,000-line PRs, and run fast persevere-or-pivot cycles.

- Techniques: Describe the end state, then review the trade-offs; Give agents a full environment instead of a narrow tool set; Port-verify-cross-read loop for large code migrations; Capture production runtime types to guide migrations; Share intent, trade-offs and production measurements in place of raw diffs; Tiered review: deep human review for architecture, fix-forward for cosmetic; Agent as a shared teammate in team channels; Instrument before you need it; use flags and dynamic config; Short bets with two-week persevere-or-pivot reviews; Unship primitives superseded by newer ones
- Tools: Claude Code, Claude Design, Cowork, Claude Code artifacts, Bun, MonkeyType, Slack, Python, TypeScript

## [The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp](../videos/L173Z8DpaJg.md)
`L173Z8DpaJg` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: software-factory, multi-agent, sandboxing-execution

Safia Abdalla (Warp) on building the Oz cloud agent platform: hide infra complexity, allow any harness, expose everything via API, and run the open-source repo with agent-gated triage and PR review.

- Techniques: Managed plus self-hosted sandboxes behind one model; Harness-agnostic layer with platform guardrails; Orchestrator with mixed-model sub-agents; Agent-gated PR review before human review; Agent-driven issue intake; API-first primitives for agents, sub-agents, environments and artifacts
- Tools: Warp, Oz, Claude Code, Codex, GitHub, Slack

## [Building Blocks for Uber’s Software Factory— Uday Kiran Medisetty & Adam Huda, Uber](../videos/17-YSUHo6Lk.md)
`17-YSUHo6Lk` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: software-factory, mcp-and-tools, enterprise-adoption

Uber's engineers walk through six building blocks (model gateway, MCP gateway, agent devpods, skills marketplace, context graph, Cortana) behind its managed software factory, then show one feature built end-to-end by an agent.

- Techniques: Single gateway with middleware chain and project attribution; Progressive MCP projection (direct, discovery, CLI, generated code); Pre-warmed agent workspaces; Skill marketplace with lint, review and trace feedback; Shared context graph queried before tool calls; Split review between an inner loop and an outer loop; Managed scheduled maintenance loops with bounded output

## [Github's Biggest Release In Years. Stacked PRs.](../videos/3Z1xcfF2xlY.md)
`3Z1xcfF2xlY` · Better Stack · 2026-09-02 · q3 · intro · tutorial · also: dev-tools, coding-agents

Better Stack walks through GitHub's stacked PRs: splitting a large change into a chain of dependent PRs, managing the chain with the gh CLI, and merging the whole stack at once.

- Techniques: Stacked PR workflow with gh stack; Manual stacking without the CLI; Layer the stack by dependency
- Tools: GitHub (stacked pull requests, Merge stack, stack UI), GitHub CLI (gh), with gh stack init / add / submit subcommands, git

## [We Vetted 2000 AI Skills Before They Reached Developers — Lucas Palma, Nubank](../videos/iKQ78wyJEXU.md)
`iKQ78wyJEXU` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails, skills-self-improvement, governance-compliance

Nubank's product security team built SkillVector, a CI scanner that vets internal AI skills (hybrid regex plus LLM) before they reach an internal marketplace, and reports 2,000+ skills scanned.

- Techniques: Three-point skill scanning; Hybrid deterministic plus LLM review; Findings as PR comments plus SARIF; Historical back-scan; Verify approval gates, not model confirmations
- Tools: SkillVector (spoken as 'SkillVetor' in the transcript), SARIF, Regex-based determinstic scanners, LLM reviewer, Internal skills marketplace

## [In the Land of AI Agents, the Verifiers Are King — Tariq Shaukat, Sonar](../videos/VrpEyglYgeU.md)
`VrpEyglYgeU` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: testing-verification, context-engineering

Sonar's CEO argues AI coding agents need verification built into the loop: guide them with context and constraints, layer algorithmic and agentic checks, and keep the codebase clean. It is a vendor talk, and its numbers are self-reported.

- Techniques: Guide with context and constraints; Zero-trust multi-layer verification; Verification inside the agentic loop; CI verification loop with agent PR review and quality gates; Scheduled code-maintenance and remediation agents
- Tools: Sonar Vortex (product launched the day before the talk, per the speaker), METR time-horizon benchmark chart, Models named: Mythos, Fable, GPT 5.5

## [Why Software Factories Fail](../videos/Ib5GBkD555M.md)
`Ib5GBkD555M` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: software-factory, evals, context-engineering

Dex (HumanLayer) argues that agent "lights-off" software factories fail because coding models are trained on tests passing, not maintainable code, so teams must restore code review and plan up front.

- Techniques: Staged plan before agent implementation; Review the plan so the PR review is short; Check for test gaming with pre-patch runs and a quality judge; Diagnose RL-style reward gaps
- Tools: Claude Code, Codex, SWE-bench Multilingual, SWE-Marathon, DeepSWE, Frontier Code, Linear, Jira, HumanLayer

## [Guide, Verify, Solve — Anirban Chatterjee, Sonar](../videos/03l29gJXpCE.md)
`03l29gJXpCE` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: testing-verification, coding-agents, governance-compliance

Sonar's product marketer argues AI-written code needs zero-trust, multilayered verification inside agent loops and in CI/CD, framed as a Guide-Verify-Solve (ACDC) cycle, with vendor product pitches throughout.

- Techniques: In-loop verifier callback with fix-and-rerun; Task-scoped context retrieval for agents; Machine-enforced quality rulebook; Dual PR gate: LLM review plus deterministic scan; Cross-model or cross-method review; Graduated automation of review bots; Remediation agent for backlog debt; Per-task model choice from a quality profile
- Tools: SonarQube, Sonar Vortex, Guitar (AI code-review tool, name from captions), Cursor, Claude Code, Codex, Antigravity

## [How to Kill the Code Review — Ankit Jain, Aviator](../videos/YgEv7IQzGdM.md)
`YgEv7IQzGdM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: testing-verification, context-engineering, skills-self-improvement

Ankit Jain (Aviator) argues code review's real job is alignment, not bug-catching, and proposes reviewing agent session intent, test-plan evidence and a codified "AI slop registry" instead of diffs.

- Techniques: AI slop registry; Capture session decisions as acceptance criteria; Test plan from criteria plus registry invariants, run against a preview; Agent-driven UI evidence with DB snapshots; Review the plan and evidence, not the diff
- Tools: GitHub, Aviator Verify

## [Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town](../videos/yWS0udrIOc8.md)
`yWS0udrIOc8` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: security-guardrails, multi-agent

Steve Yegge argues AI-generated code multiplies security defects and new attack types (slopsquatting, prompt injection, agent credentials), and urges security scanning at generation time and as a separate pass.

- Techniques: Surface security findings at generation time; Separate security and correctness into different passes; Run several scanners and have agents cross-check; Supply-chain vetting of dependencies and base images; Adversarial supervisor agents for queue-driven agents; Least-privilege credentials per agent action
- Tools: Claude Code, Beads, Gas Town, Snyk (called Sneak in captions), Chainguard

## [AI Agents for Performance: Ship Faster, Pay Less — Rajat Shah, Netflix](../videos/CgsWxRUY5Eo.md)
`CgsWxRUY5Eo` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: infra-cost-scaling, coding-agents, context-engineering

Netflix's playbook for using coding agents on production profiling data to find CPU hot spots, open reviewed fixes, and grow a shared pattern catalog, with a canary gate and an autonomy ladder.

- Techniques: Profile-to-PR agent pipeline; Central anti-pattern catalog in git; Cross-repo sweep for recurring patterns; Canary-gated review; Shift-left catalog injection; Scheduled fixed workflow before autonomy
- Tools: Continuous profilers (sampled call stacks with CPU time), Git and code search across repos, Canary deployment infrastructure, TorchFix (public PyTorch anti-pattern catalog), Spectator (metrics library, named as the source of the counter-object pattern)

## [I Let Strix Attack My App... Here’s What It Found](../videos/vRTliPb8fjg.md)
`vRTliPb8fjg` · Better Stack · 2026-08-02 · q3 · intro · review · also: security-guardrails, sandboxing-execution

Short Better Stack review of Strix, an open-source multi-agent pen-testing tool that attacks a web app or API in a Docker sandbox and returns validated exploits and fix PRs, with real limits on cost, speed and complex attacks.

- Techniques: Scan code and live target together in one run; CI merge gate on validated findings; Triage on proof, not on maybes; Match model strength to scan depth and budget
- Tools: Strix, Docker, Anthropic API (Claude), Gemini, Ollama, GitHub Actions, FastAPI (demo app), XBEN exploitation benchmark, OWASP Top 10

## [Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI](../videos/ZpK5PWX2YRM.md)
`ZpK5PWX2YRM` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: testing-verification, coding-agents, software-factory

Alex Volkov on the "Z/L continuum" for how much agent-written code engineers should read in 2026: route review effort by the proof a change needs, not by a blanket rule.

- Techniques: Risk-tiered review routing; Decompose into atomic PRs with agents; Separate writer, inspector and test author; Turn review findings into system rules; Ask the agent where the critical code is; Loops with verification and retry
- Tools: Claude Code, Codex, OpenClaw, Pi, Antigravity, Grok Code

## [Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison](../videos/uU5Gv2h8-9g.md)
`uU5Gv2h8-9g` · AI Engineer · 2026-07-18 · q3 · practitioner · interview · also: claude-code, security-guardrails, context-engineering

Anthropic's Thariq Shihipar and Cat Wu, with Simon Willison, on how Claude Code and Claude Tag change team workflows, code review, auto mode safety, and prompt design, with internal claims about PR share and prompt size.

- Techniques: Staged trust ramp for AI code review; Eval-gated model swap; Behavioral evals built from user complaints; Conditional prompt wording over absolute rules; Per-model system prompts; Classifier-based permissions using user intent; Credential injection through a proxy; Fewer tools with distinct functions; Multiplayer channel agent with shared memory; Dogfooding gate before launch
- Tools: Claude Code, Claude Tag, Slack, GitHub, Datadog, FFmpeg, Remotion, Gemini API, Mountain Project, Claude Fable, Claude Opus 4.8, Claude Mythos

## [ReviewDebt: a practical framework for scoring every pull request — Sachin Gupta, Ebay](../videos/TJPInBjhE4Q.md)
`TJPInBjhE4Q` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: coding-agents, evals, governance-compliance

Sachin Gupta (eBay) argues coding agents create unmeasured review debt and offers a deterministic 0-100 PR review-burden score built from five signal families, plus a rollout plan.

- Techniques: Deterministic review-burden score; Backfill calibration; Non-blocking rollout ladder; Shape rules for agent PRs; Authorship detection as a weak amplifier
- Tools: GitHub, GitHub Copilot, Codex, Cursor

## [The AI bugpocalypse is here. Now what? - Jack Cable, Corridor](../videos/7JgIS42mz7U.md)
`7JgIS42mz7U` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: security-guardrails, governance-compliance, models-research

Jack Cable (Corridor, ex-CISA) argues frontier models now find and exploit vulnerabilities at scale, but the bug classes are old and preventable, so rewrite toward memory safety and add guardrails before the PR for AI-written code.

- Techniques: Rewrite critical components in a memory-safe language; Pre-PR guardrails and visibility for agent-written code; Give the reviewer business and threat context; Use defenders' frontier models to harden systems
- Tools: Claude Code, Cursor, Rust, Slack, BaxBench

## [Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation](../videos/whue9_YquGA.md)
`whue9_YquGA` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: software-factory, enterprise-adoption, multi-agent

Angie Jones (Block) describes moving a 3,500-person engineering org to autonomous agent delegation via a maturity model, a power-user champions program, AI-ready repos, and an orchestrator.

- Techniques: Stage-based maturity model for agent use; Champions program of hand-picked power users; Layered repo context files; Delegation from the tools people already use; Review agent plus auto-fix loop; Isolated cloud workspace per agent; Machine-readable system map for orchestration
- Tools: Claude Code, Goose, Codex, BuilderBot, GitHub, Jira, Linear, Slack, MCP, AGENTS.md, CLAUDE.md

## [Research to Reality: Bringing Frontier ML Research to Production - Vaidas Razgaitis, Higharc](../videos/OXMMN-XbxwA.md)
`OXMMN-XbxwA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: enterprise-adoption, context-engineering, agent-architecture

Higharc's labs team on moving ML research prototypes into production via three levers: a design-doc-style "research prototype taxonomy," a decoupled Python microservice monorepo, and stacked-PR decomposition for review.

- Techniques: Research prototype taxonomy (RPT) doc; One researcher, one decoupled microservice in a shared monorepo; Slice by dependency graph, then stack PRs; Use the design doc to plan the merge; Notebooks on Modal for GPU experiments
- Tools: Notion, Graphite, GitHub Actions, Modal, Docker, FastAPI, Poetry, uv, Jupyter

## [The Missing Layer After Launch - Raphael Kalandadze, Wandero AI](../videos/kZsf_Sfm7RU.md)
`kZsf_Sfm7RU` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: observability, evals, multi-agent

Shipping an agent is where the real work starts. Raphael Kalandadze shows a post-launch loop: a log-monitor agent opens PRs, a fresh-context review agent critiques them, and a session analyzer scores every conversation for health.

- Techniques: Hourly log-monitor agent that opens PRs; Fresh-context review agent as a PR gate; Session analyzer for health scoring; Computer-use QA agent with a site-specific skill; Meta-harness: connect all context to the monitoring agents
- Tools: Claude Code, Codex, HTML artifacts, log and trajectory store, browser computer-use agent

## ["The engineer of the future is the person who chooses what is worth doing." — Addy Osmani, Anthropic](../videos/n97BCfyFIvw.md)
`n97BCfyFIvw` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: software-factory, governance-compliance, product-ux

Addy Osmani argues engineers are defined by owning the verdict on agent work: choosing what is worth doing, backing it with evidence, and accepting accountability. Keep humans at the highest-leverage checkpoint.

- Techniques: Inner loop / outer loop split; Evidence bundle as the review unit; Explain-it-or-don't-ship gate with named owners; Review as a control system for long runs; Move verification into the harness; Clean code for agents as well as humans
- Tools: Git

## [The Top Claude Code Features We Use](../videos/ECQA6oOyfIk.md)
`ECQA6oOyfIk` · AI LABS · 2026-07-02 · q2 · intro · review · also: claude-code, multi-agent, token-cost-efficiency

AI LABS walks through the Claude Code features its team uses most (Agent Teams, Advisor, goal, auto mode, worktree sub-agents, review commands, loop, monitor), with a Scalekit sponsor segment and little measured detail.

- Techniques: Adversarial finder/fixer agent team for code review; Cheap executor with strong advisor escalation; Goal-driven run to a verifiable end state; Auto mode instead of skip-permissions; Worktree-isolated sub-agents for design variants; Layered review commands before merge; Daily knowledge-base sync with loop; Anomaly-only monitor for agent logs
- Tools: Claude Code, Claude Agent SDK, Claude Haiku, Claude Sonnet, Claude Opus 4.8, tmux, Scalekit, ChromaDB, Notion, Gmail, Slack, Mac mini

## [Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar](../videos/NuePCNMpWGc.md)
`NuePCNMpWGc` · AI Engineer · 2026-06-18 · q2 · practitioner · talk · also: evals, coding-agents, testing-verification

Sonar argues that LLM pass rates miss security, maintainability and verbosity. It shows its Java eval of 53+ models and pitches a verify-in-loop and remediation pipeline, so it is product-heavy.

- Techniques: Dual-metric model evaluation; In-loop static analysis via MCP; Regression-gated autofix; One PR per issue for tech debt; Remediation on quality-gate failure
- Tools: SonarQube, SonarQube Agentic Analysis (MCP), Sonar Sweep, Sonar Context Augmentation, Sonar remediation agent, Claude Code, Codex, Gemini CLI, Devin, Cursor, Windsurf, Antigravity

## [Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo](../videos/EcqMYoIV57A.md)
`EcqMYoIV57A` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: context-engineering, multi-agent

Qodo's Nupur Sharma argues that dumping more context into an agent makes results worse, and shows how selecting, splitting and judging context across specialist agents fixed this in their PR review system.

- Techniques: Context selection instead of context dumping; Iterative retrieval with a library-card index; Hierarchical summarization; Knowledge graph for dependencies; 80/20 research and gate split; Specialist agents with a judge agent; Feedback-weighted calibration
- Tools: Jira, MCP, Claude Opus

## [BDD, ADR, PRD, WTF: Capturing Decisions for Humans and AI Alike — Michal Cichra, Safe Intelligence](../videos/504PvfXou5Y.md)
`504PvfXou5Y` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: context-engineering, testing-verification

Michal Cichra on keeping agents and humans aligned by storing ADRs, PRDs and executable BDD specs in the repo, then enforcing them through git hooks, CI and import-boundary lints.

- Techniques: ADR with enforcing lint rule; Import-boundary restriction to eliminate bug classes; Executable BDD scenarios linked to PRDs; Shared checks in git hooks and CI; Design system as enforced rules and previews; Scoped test selection per task
- Tools: Cucumber, git hooks, CI, linters, type checkers, architecture import lint, Markdown docs

## [Scaling Agents on Kubernetes with acpx and ACP — Onur Solmaz, OpenClaw](../videos/VaS2h-dY1-4.md)
`VaS2h-dY1-4` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: multi-agent, mcp-and-tools, sandboxing-execution

An OpenClaw maintainer shows acpx, a CLI and workflow engine over the Agent Client Protocol (ACP), used to automate PR triage and to run disposable per-task agents on Kubernetes.

- Techniques: ACP as the client-side adapter layer; Channel-bound agent sessions; Hybrid PR-triage workflow with JSON handoffs; Shallow-fix loop with a human escalation gate; Feedback bin for PR outcomes; Per-task disposable agent pods via a Kubernetes operator
- Tools: acpx, ACP (Agent Client Protocol), Codex, Claude Code, Zed, Discord, Slack, MS Teams, Kubernetes, Helm, Go operator, rsync

## [This One Command Fixed The Biggest Problem Of AI Coding](../videos/qkc1j3_k8gs.md)
`qkc1j3_k8gs` · AI LABS · 2026-06-02 · q3 · practitioner · tutorial · also: security-guardrails, coding-agents, token-cost-efficiency

Walkthrough of DeepSec, a regex-prefilter plus batched Claude Code/Codex agent harness for repo security scans. Strong on code-local bugs, weak on runtime and logic flaws.

- Techniques: Regex prefilter before agent review; Batched parallel agent investigation with merge and coverage check; Project context file for the scanner (info.md); DeepSec command sequence; Resumable batch processing; Per-finding output with ownership and repro; Scoping an unscoped agent review
- Tools: DeepSec (Vercel security harness; `deepsec init`, `scan`, `process`, `report`, `export`), Claude Code, Codex, Claude Agent SDK, Codex Agent SDK, Opus 4.7 (max effort), GPT 5.5 (x-high reasoning), Git (metadata for commit attribution and owner), Markdown and JSON (output formats)

## [Is Your AI Code Producing CRAP? (Here's How To Fix It)](../videos/XuMR1pgc6pc.md)
`XuMR1pgc6pc` · Better Stack · 2026-06-02 · q3 · practitioner · review · also: testing-verification, coding-agents

Better Stack explains the CRAP metric (complexity combined with test coverage) and the cargo crap Rust tool, arguing it is a useful second check on complex, under-tested code, especially AI-generated code.

- Techniques: Run a CRAP check after the unit tests; Set a complexity budget; Check that the metric reacts to test removal
- Tools: cargo crap (cargocrap Rust package, by Oleksandr Prokhoranko), CRAP metric (Savoia and Evans, 2007), Rust, CRAP tool for Java (same author, mentioned, not shown)

## [What Happens When AI Coding Gets a Delivery Pipeline (Routa)](../videos/_16PhraFYjQ.md)
`_16PhraFYjQ` · Better Stack · 2026-06-02 · q3 · intro · review · also: software-factory, coding-agents, multi-agent

Walkthrough of Routa, a free, local-first, open-source Kanban desktop app that runs AI coding agents through backlog, dev, and review lanes with evidence and gates instead of one chat thread.

- Techniques: Lane-per-stage agent pipeline; Evidence-backed review gates; Per-task traceability; Self-hosted setup
- Tools: Routa (open-source AI coding delivery tool; spelled Ruta in captions, Routa in the title; desktop app and Docker Compose), OpenCode (agent runtime used for the agents), Anthropic API / Claude (model provider via synced API key), MCP (Model Context Protocol, supported for agent connections), ACP (Agent Client Protocol, supported for agent connections), Docker Compose (self-hosting path), Cursor (chat-first comparison), Claude Code (chat-first comparison), CrewAI (agent framework comparison), LangGraph (agent framework comparison; spelled LaneGraph in captions)

## [How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom](../videos/4_VQBbs2iQA.md)
`4_VQBbs2iQA` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: claude-code, enterprise-adoption, skills-self-improvement

Intercom's platform lead explains how they set a goal to double engineering throughput by standardizing on Claude Code, backed by skills, hooks, calibrated auto-approval and telemetry.

- Techniques: Single-platform standardization with internal plugin distribution; Guidance flywheel; Problem-first prompting; Backtested skill authoring; Calibrated automatic approval; Agent telemetry and transcript mining
- Tools: Claude Code, GitHub Copilot, Cursor, Augment, Honeycomb, S3, DX, Ruby on Rails, React, GitHub

## [CI/CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner](../videos/VktrqzQgytY.md)
`VktrqzQgytY` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: software-factory, sandboxing-execution, multi-agent

Talk arguing CI/CD was built for human-paced PRs and breaks under agent volume; proposes spec-driven agent loops with in-loop validation, a pre-merge queue, and stateful compute.

- Techniques: Spec-first agent loop with a known-commit start; External review agents inside the loop; Pre-merge queue for serializable commits; Approve intent and evidence, not diffs; Stateful, incremental execution environments
- Tools: GitHub Actions, Claude Code, Amp, Cursor, Factory, GitHub Copilot, Namespace

## [OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman](../videos/MhHEGMFCEB0.md)
`MhHEGMFCEB0` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: coding-agents, multi-agent, security-guardrails

OpenAI's Codex workshop on plugins, background automations, code review, custom sub-agents with sandbox modes, guardian approvals, and stop hooks for long runs.

- Techniques: Custom sub-agent personas as TOML files; Fan-out review by file slices with an orchestrator; Read-only explorer on a fast cheap model; Parallel brainstorm of implementation options; Guardian verifier sub-agent for privileged actions; Stop hook that keeps a run going; Best-of-N cloud runs; Playwright interactive skill for visual debugging
- Tools: Codex, Codex app, Codex CLI, Codex IDE extension, Codex Code Review, Codex Security, Claude Code plugin for Codex, Playwright, ImageGen, Slack, Gmail, Google Drive

## [AgentCraft: Putting the Orc in Orchestration — Ido Salomon](../videos/kR64LOqBBCU.md)
`kR64LOqBBCU` · AI Engineer · 2026-05-18 · q2 · intro · demo · also: multi-agent, coding-agents, product-ux

Ido Salomon demos AgentCraft, an RTS-style orchestrator for many coding agents, arguing the human is the bottleneck and offering visibility, campaigns, review bundles and shared workspaces as fixes.

- Techniques: Filesystem-projected agent map with collision heat map; Hotkey cycling to agents that need attention; Campaign mode: broad goal in a container, plan first; Review bundles with rationale and visual evidence; Best-of-N parallel attempts with human selection; Soft coordination via shared human and agent chat
- Tools: AgentCraft, MCPUI, MCP Apps, Cursor, Claude Code, Codex, OpenClaw, Git, Chrome

## [Fallow: The Code Intelligence Tool Every Claude User Needs](../videos/-lCfwIoDXq8.md)
`-lCfwIoDXq8` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: claude-code, dev-tools

Better Stack walks through Fallow, a Rust-built static analyzer for JS/TS (dead code, duplication, complexity), and shows how it works as a guardrail for Claude Code runs and branch-level PR audits.

- Techniques: Snapshot the project with the summary report; Drill into one category with machine-readable output; Preview fixes with dry run before any write; Guard an agent run with the Fallow skill and a scoped prompt; Scope a config file to ignore noise; Audit only the current branch against main; Generate Claude Code hooks for Fallow; CI with baselines and PR annotations
- Tools: Fallow, Claude Code, knip, jscpd, ESLint, bunx, Oxc, VS Code extension, Cursor, MCP server, V8 runtime coverage, GitHub Action

## [How IBM’s Bob uses "Review Mode" to solve the hardest coding tasks (Full Breakdown)](../videos/pSzLkt0NfJQ.md)
`pSzLkt0NfJQ` · Better Stack · 2026-05-02 · q2 · intro · review · also: coding-agents, dev-tools

Better Stack walkthrough of IBM's Bob IDE, which separates ask/code/plan modes and runs a security Review mode with a findings panel and one-click fixes; tested on the ZBank COBOL repo, with a short sponsored-style pitch for the free trial.

- Techniques: Mode-separated agent workflow; Scoped auto-approval; Review-then-fix-then-test loop; Atomic SQLite write for a race condition
- Tools: IBM Bob, Bob Shell, IBM Granite, ZBank (open-source COBOL repo), Streamlit, SQLite, COBOL, VS Code

## [Why GUIs Will Replace TUIs for AI Developer Tools | Better Stack Podcast Ep. 14](../videos/zr-Xk0UVHEU.md)
`zr-Xk0UVHEU` · Better Stack · 2026-04-02 · q3 · practitioner · interview · also: coding-agents, multi-agent, dev-tools

Better Stack podcast with Warp DevRel Ben Holmes on why GUI-style wrappers around coding agents will beat TUIs, plus practical patterns for agent code review, cloud agents, and multi-agent delegation.

- Techniques: Fresh-session review pass; Ask why, do not accuse; Two-lens review passes; Agent review as a GitHub Action; Keep READMEs and CLAUDE.md thin; Two clones instead of worktrees for parallel agents; Cloud research, then fork locally; Multi-repo sandbox environment; Route by task complexity; Tune the harness per model; Figma for design, agent for implementation
- Tools: Warp, Oz (Warp cloud agent platform), Claude Code, Codex (CLI and app), OpenCode, Pi, OpenClaw, Cursor, GitHub Copilot, Ghostty, tmux, cmux

## [The toolkit from Y Combinator CEO that Will Makes Claude Code Amazing](../videos/kLq5p43huYQ.md)
`kLq5p43huYQ` · Better Stack · 2026-04-02 · q3 · practitioner · review · also: coding-agents, claude-code, testing-verification

A Better Stack walkthrough of GStack, Gary Tan's Claude Code skill pack, showing a plan, review, ship and QA pipeline that builds, tests and opens a PR for a tweet-screenshot feature.

- Techniques: Install GStack into a Claude Code project; Plan-mode CEO scope review before coding; Diff-aware review, ship and QA chain; Let the review command resolve PR review comments; Put tool preferences in CLAUDE.md, not hooks; Skill template plus generated SKILL.md
- Tools: Claude Code, GStack, Bun, Playwright, Greptile, Superpowers (Claude Code plugin), Conductor, React, Vite, TypeScript, Opus, CLAUDE.md

## [GitHub Actions are DEAD. (Use Agentic Workflows instead)](../videos/-DXkF2Q69Jw.md)
`-DXkF2Q69Jw` · Better Stack · 2026-03-02 · q2 · intro · tutorial · also: software-factory, security-guardrails

Walkthrough of GitHub Agentic Workflows: write a natural-language agent.md, compile it to a locked-down Actions workflow, and use it as a PR audit bot. Research prototype, one demo.

- Techniques: Natural-language agent file compiled into an Actions workflow; PR-triggered read-only audit agent with a structured output format; Gated write path for agent actions
- Tools: GitHub Agentic Workflows, ghaw (compile CLI), GitHub Actions, GitHub CLI (gh extension), GitHub Copilot (engine), GitHub Next, Microsoft Research, Better Stack AI SRE (sponsor plug)

## [Copilot Helps You Type…. This Helps You Ship](../videos/LRwc64Ui_MQ.md)
`LRwc64Ui_MQ` · Better Stack · 2026-03-02 · q2 · intro · review · also: coding-agents, context-engineering

A short walkthrough of Continue, an open-source VS Code extension for model-agnostic codebase chat, diff-based edits and markdown-defined PR review agents, positioned as complementary to Copilot.

- Techniques: Model-agnostic Continue setup; Repo-aware explanation of unfamiliar code; Review and apply diffs in chat; Markdown-defined PR review agent; Split autocomplete and review tools
- Tools: Continue (VS Code extension, open source), GitHub Copilot, VS Code, Ollama, Llama 3 (Llama3), GPT-4, Claude, OpenAI, Slack, Cursor, Claude Code

## [AI Coding Finally Fixed, New AI Models, Huge Gemini Deal and More!](../videos/noxDpgSsops.md)
`noxDpgSsops` · AI LABS · 2025-12-02 · q2 · intro · news · also: models-research, coding-agents

AI LABS' first Context Weekly roundup: GitHub Agent HQ as a multi-agent command center, Cursor 2.0 with its Composer model, and assorted model, product and robotics announcements, mostly relayed from press coverage.

- Techniques: Clarify-then-dispatch planning for multiple agents; Side-by-side model comparison on one prompt; Select-and-ask UI fix loop in a built-in browser; Mid-reasoning context injection
- Tools: GitHub Agent HQ, Cursor 2.0, Composer (Cursor model), Chrome DevTools, Gemini 3 Pro (preview, expected), Nano Banana 2 (image model, expected), GPT-5.1 (rumored), Design Arena, ChatGPT, Claude (financial services features), Excel, 1X NEO

## [How to Use Cursor in the Smartest Way Possible](../videos/LXk8nWwOPuY.md)
`LXk8nWwOPuY` · AI LABS · 2025-11-02 · q3 · practitioner · tutorial · also: coding-agents, context-engineering

A tutorial on pairing Cursor's agent with the CodeRabbit extension: commit each implementation chunk, run a review, feed suggestions back, and drive a phased implementation plan.

- Techniques: Commit-gated review loop; Branch-visibility workaround for missing reviews; One-comment-per-paste fix loop; Phase-by-phase plan with a structure file
- Tools: Cursor, CodeRabbit (VS Code / Cursor / Windsurf extension), Windsurf, Git, GitHub (CodeRabbit sign-in), Gemini 2.5 Pro, Next.js, FastAPI, shadcn/ui (spoken as 'shad cn')

## [OpenAI Agent Builder... n8n Killer?](../videos/RBlHcHUvFKY.md)
`RBlHcHUvFKY` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: agent-architecture, mcp-and-tools

Hands-on walkthrough of OpenAI's new drag-and-drop Agent Builder, used to build a GitHub PR code-review agent; covers guardrails, structured outputs, MCP, widgets and evals, with bugs noted and a verdict that it does not yet replace n8n.

- Techniques: Input guardrail with a fail branch; Structured extraction gate before tool calls; Transform node to flatten nested outputs for a tool; Isolated reviewer context; Natural-language graders over traces; Widget output from a final agent; Adding a custom MCP server
- Tools: OpenAI Agent Builder, ChatKit, Agents SDK, Apps SDK, GitHub MCP server, Context7 MCP server, GPT-5, GPT-4.1, OpenAI vector store (file search), web search tool, code interpreter, n8n

## [Claude Code SDK: Build Real AI Apps with Python & MCP](../videos/h1AGjM9IeBM.md)
`h1AGjM9IeBM` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: claude-code, coding-agents, mcp-and-tools

A short walkthrough of the Claude Code SDK (Python, with the docs' example script and a GitHub Actions demo) that frames Claude Code as a programmable subprocess. The example broke for the speaker, and the video shows no working SDK run beyond that.

- Techniques: Run Claude Code as a subprocess from Python; Cap agent iterations with max_turns; Attach external MCP servers to programmatic Claude Code; Mention-triggered issue-to-PR workflow in GitHub Actions
- Tools: Claude Code, Claude Code SDK (Python, TypeScript, CLI), ClaudeCodeOptions, query(), Cursor, GitHub Actions, Claude Code GitHub Actions workflow, Jira MCP server, Slack MCP server, pip

## [Cursor 1.0 is their BEST update yet... (Agents, BugBot, Memories and more)](../videos/Ig-cfiqWJCs.md)
`Ig-cfiqWJCs` · Better Stack · 2025-11-02 · q3 · intro · review · also: coding-agents, sandboxing-execution, mcp-and-tools

Feature tour of Cursor 1.0 covering BugBot PR review, remote background agents, per-project memories and one-click MCP install with OAuth, plus the security caveats of background agents.

- Techniques: BugBot on GitHub PRs with trigger control; Launching a background agent from a prompt; Background agent environment via snapshot or environment.json; Saving persistent project rules as memories; One-click MCP install with OAuth
- Tools: Cursor 1.0, Cursor BugBot, Cursor Agent, Cursor background agents, Cursor memories, Cursor dashboards, GitHub, GitHub Copilot, Claude Code (transcribed as 'clawed code'), Notion MCP server, Bun / bunx, Create React App (npx)

