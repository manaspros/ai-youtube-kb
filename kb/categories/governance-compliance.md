# governance-compliance — 138 videos

*policy, audit, cost control, budgets, enterprise governance of AI*

By channel: AI Engineer 114 · Kai Explains 11 · Better Stack 13

**Synthesized guide:** [guides/governance-compliance.md](../guides/governance-compliance.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [Your AI Pilots Won't Move the P&L. Here's What Will - Adam Nahari, Apollo](../videos/vUJDyDnqT4c.md)
`vUJDyDnqT4c` · AI Engineer · 2026-11-02 · q3 · intro · talk · also: enterprise-adoption, product-ux

Adam Nahari (Apollo) argues AI pilots fail to move EBIT because most spend goes to general tools and change management, and sets out six moves (pick one or two P&L-linked problems, redesign the process end to end, get CEO sponsorship, build with the business, put tools in everyone's hands, pre-set kill metrics) to make AI show up in margin.

- Techniques: Work-backward use-case screen; End-to-end workflow redesign over assistive tooling; Embedded domain champions in the build loop; Pre-registered kill gates; At-scale unit economics check

## [78% Wanted This AI Feature. Almost Nobody Used It - Supriya Subudhi, Bumble](../videos/CvmZtAPmAW4.md)
`CvmZtAPmAW4` · AI Engineer · 2026-10-31 · q4 · practitioner · talk · also: evals, product-ux, token-cost-efficiency

Bumble's Supriya Subudhi argues that a positive A/B test is only the start for AI features, and lays out five checks: real adoption, tail-of-distribution outputs, cost versus benefit, model cost-quality tradeoffs, and legal market readiness.

- Techniques: Adoption-first AI feature rollout; Segment-level eval review over averages; Guardrails on advice scope; Eval-driven model and prompt selection under a cost budget; Write down the business reason for each AI feature; Regulatory check before building
- Tools: Meta Muse AI (mentioned as an example of a US/Canada-only launch), Amazon AI shopping assistant (mentioned as an example), Spotify AI DJ (mentioned as an example)

## [Voice AI Where One Wrong Question Breaks the Rules - Shiv Indap, Upstart & Brooke Hopkins, Coval](../videos/3osCbSufv8g.md)
`3osCbSufv8g` · AI Engineer · 2026-10-31 · q4 · practitioner · talk · also: evals, voice-multimodal, observability

Coval and Upstart walk through a regulated voice-agent (lending verification calls) eval loop: human review, judge calibration, failure routing, and simulation before release.

- Techniques: Judge-human calibration loop; Structured human review queues; Clustering and anomaly detection for unknown failure modes; Failure-to-owner routing; Voice simulation before release; Feature-flagged agent changes with named approvers
- Tools: Coval (voice-agent evaluation and simulation platform), Google Sheets (initial manual review tracking), LLM-as-judge, RL pipelines and fine-tuned LLMs (mentioned as options for self-healing, not shown)

## [Your Agent Just Paid for Nothing: 6 Attacks on x402 Payments - Ishween Kaur, SoFi](../videos/YU1uD_YkpjU.md)
`YU1uD_YkpjU` · AI Engineer · 2026-10-30 · q3 · practitioner · talk · also: security-guardrails, observability

Ishveen Kaur (SoFi) walks through six ways an autonomous agent can lose money on x402 machine payments, with guards, a probation-list pattern, and a trace-one-payment-ID method for finding them.

- Techniques: Compare listed price against 402 quoted price, network and wallet before paying; Shared payment-number ledger on the seller side; Buyer retries reuse one payment number; Choose release timing by data cost; Paywall test across all endpoints and no-store caching for paid output; Allow list, block list and probation list for discovered sellers; Per-plan call cap against prompt injection; Single-ID tracing with a 20-25 case dataset
- Tools: x402 (HTTP 402 payment protocol), Llama 3.2 (agent model in the prompt-injection demo), Base Sepolia testnet (auto-caption reads 'Bayes Cipolia'; probably Base Sepolia), x402.org facilitator (testnet), Bazaar (x402 seller directory), Ethereum and Solana (named as alternative chains), Cloudflare pay-per-crawl (cited as a parallel)

## [Why Humans Can't Keep Up With AI-Written Code - Tariq Shaukat, Sonar](../videos/LQW_Wvqhp04.md)
`LQW_Wvqhp04` · AI Engineer · 2026-10-30 · q3 · practitioner · talk · also: software-factory, testing-verification, evals

Vendor talk arguing AI-generated code makes volume cheap but confidence scarce, so software factories need intent, guide rails, independent verification and evidence, with LLM judges treated as unreliable.

- Techniques: Code confidence formula as a factory checklist; Guide rails over guard rails; Deterministic plus agentic verification mix; Measure judge stability before trusting an LLM judge; Model per-step reliability to pick task length
- Tools: SonarQube, Sonar Vortex, Claude Mythos preview (named as the model in the Meter study, version as stated in talk)

## [Why AI Won't Replace Stock Pickers - Jack Woodruff, Candlestick & Vinoo Ganesh, Kepler](../videos/y2dyD6slKxE.md)
`y2dyD6slKxE` · AI Engineer · 2026-10-30 · q2 · intro · interview · also: data-engineering, enterprise-adoption

Fireside chat between a hedge fund founder and a Kepler co-founder on how AI changes stock picking: AI raises the baseline, auditability is the trust gate, and edge comes from divergent views and idea velocity.

- Techniques: Audit-first verification of model-produced numbers; AI as attention triage for human research; Automate prep, reinvest time in differentiated work

## [Your $200 ChatGPT Plan is now worth less!](../videos/P0i3vYuJZH8.md)
`P0i3vYuJZH8` · Kai Explains · 2026-10-29 · q4 · practitioner · review · also: token-cost-efficiency, coding-agents

OpenAI halves the Codex allowance for grandfathered $200 Pro plans from Oct 30, 2026, and the undocumented 28-day reset run ends with it. The video works out per-model cost math and a checklist for what to do.

- Techniques: Convert a subscription allowance into API dollars; Weight cost by cache-read share; State the baseline when comparing a price change; Default cheap, escalate only on demonstrated failure; Keep your own log of allowance burn and resets
- Tools: OpenAI Codex (agentic coding system), ChatGPT Pro 200 / Pro 100 / Pro 500 / Plus plans, GPT-6 Astra (flagship), GPT-6.1 Sol, GPT-6.1 Terra, GPT-6 Sol, GPT-6 Luna, GPT-5.6 Sol, Claude Max 20x / Claude Pro (Anthropic), codexresets.com (community reset tracker), Artificial Analysis benchmark index (cost per task), SemiAnalysis (token-mix and allowance measurements)

## [How Revolut Cut AI Coding Costs 90% With Self-Hosted Open Models - David Abitbol, Revolut](../videos/Ok6QdZHCcI8.md)
`Ok6QdZHCcI8` · AI Engineer · 2026-10-29 · q4 · practitioner · talk · also: token-cost-efficiency, inference-serving, sandboxing-execution

Revolut's AI ops lead explains how self-hosting GLM on dedicated GPUs cut its coding-AI invoice to about a tenth, and which serving metrics and tuning levers mattered.

- Techniques: Lead-time-first AI adoption metric; Latency-led GPU capacity planning; Serving parameter sweep; Local router for multimodal fallback; Harness-agnostic OpenAI-compatible endpoint; Sandbox with per-command allow/deny rules; Compliance and telemetry baseline
- Tools: GLM (GLM 5.1 and a later GLM 5.x model; caption reads 'GLM 5.3'), GLM-5 Flash (caption reads 'Glam5G Flash'), Gemini, Claude Code, Codex, Codex app, OpenCode (caption reads 'OpenCodex'), Anthropic API, OpenAI API, OpenAI Responses API (compatible endpoints), NVIDIA B200 GPUs, Blackwell GPUs

## [How Anthropic Merges 30,000 Code Changes a Day - Manish Kapur, Sonar & Addy Osmani, Anthropic](../videos/AnsXWH2_EBU.md)
`AnsXWH2_EBU` · AI Engineer · 2026-10-29 · q3 · practitioner · panel · also: pr-code-review, testing-verification, software-factory

Sonar and Anthropic discuss verification as the bottleneck for agent-written code, covering layered checks, codified taste in CLAUDE.md/AGENTS.md, labeling agent PRs and the lights-on vs dark software factory spectrum.

- Techniques: Verification-first agent loop with a first-pass reviewer; Codify taste in CLAUDE.md or AGENTS.md for review agents; Require verification evidence before human review; Layered verification stack; Label agent-authored PRs and keep a named human owner; Agent guide rails and permission control
- Tools: Claude Code (called 'Cloud Code' in the transcript), Claude (claude.ai web product), Opus 5.5 (Anthropic model, named as a reference point for model quality), Anthropic code review product (named only as a product Anthropic offers), CircleCI (cited statistic), Sonar (verification vendor; survey and product referenced), CLAUDE.md / AGENTS.md (agent instruction files)

## [What a $900M Bank Error Teaches Us About AI Agents - John Feminella, Two Sigma](../videos/iniryju23Sk.md)
`iniryju23Sk` · AI Engineer · 2026-10-28 · q4 · practitioner · talk · also: security-guardrails, evals

Two Sigma's John Feminella ties a 2020 bank loan-payment error to AI agent governance and lays out five composable controls: registry, risk scoring, declared guardrails, shared evals, tiered approvals.

- Techniques: Tiered approval routing; Registry auto-registration through approved frameworks; Declared-capability manifest enforced at init; Risk-based review routing; Platform-owned shared eval harness
- Tools: FlexCube (internal bank processing software, as named in the talk), Claude Code, Pi (open-ended coding agent, as named in the talk), OpenClaw (named as 'open claw' in the talk)

## [Who Is Making This Request? Agent Auth 101 - Kamil Potrec, Keycard](../videos/58ulJViGFgU.md)
`58ulJViGFgU` · AI Engineer · 2026-10-28 · q3 · practitioner · talk · also: security-guardrails, mcp-and-tools

Keycard's Kamil Potrec argues agents need their own authenticated identities, short-lived scoped credentials via OAuth-style delegation, and a gateway that injects credentials outside the agent's reach, so every request is attributable and revocable.

- Tools: Keycard (control plane, client and service SDKs, gateway), MCP (Model Context Protocol), OAuth, agentbaseline.org (software factory reference implementation, named by the speaker)

## [Why Are We Still Governing AI Agents Like Software? - Tim Tyler, Gravitee](../videos/h8jgniNJcbQ.md)
`h8jgniNJcbQ` · AI Engineer · 2026-10-27 · q3 · intro · talk · also: security-guardrails, enterprise-adoption

Tim Tyler (Gravitee) argues AI agents should be governed like employees: a unique identity, a named human sponsor, a scoped role and authority, and tiered recourse, with rules as a deterministic floor and intents judged probabilistically.

- Techniques: Three-stage agent accountability model; Scope-lineage delegation check; Deterministic floor plus probabilistic scorecard; Confidence-tiered action ladder; Guardian agents at machine speed
- Tools: Gravitee (AI agent management), Claude (transcribed as 'Clyde'), MCP (Model Context Protocol), FGA policies (fine-grained authorization, generic reference), Mobile device management (MDM, analogy only), Agent accountability framework (agentaccountabilityframework.org)

## [300 Agents, 60 People: How We Secured Our Own AI Agents - Aiden Sochowski, Runlayer](../videos/BgLdvF7Qkh8.md)
`BgLdvF7Qkh8` · AI Engineer · 2026-10-27 · q3 · practitioner · talk · also: security-guardrails, observability, token-cost-efficiency

Runlayer's founding engineer describes how a 50-60 person company monitored its own 300+ daily agents through a gateway, then used the session data for security (intent drift, over-permissioning, cross-agent contamination) and for cost control (erroring MCP tools, model tier jumps).

- Techniques: Gateway-first agent telemetry; Per-tool-call intent classifier; Baseline-and-flag on tool-use history; Inbound and outbound content policies; Tight write scoping per agent; MCP error and retry monitoring with rate limits; Budgets and default model tiers
- Tools: MCP (Model Context Protocol), Claude Code (captioned as 'cloud code'), Opus (Claude model, mentioned as hard to prompt-inject), Runlayer (the speaker's company; product is a gateway, not named in detail)

## [Proving Alpha: How a Hedge Fund Measures AI's ROI - Hari Kumar, Contour Asset Management](../videos/ZMZlAn6Pyfg.md)
`ZMZlAn6Pyfg` · AI Engineer · 2026-10-24 · q3 · practitioner · talk · also: enterprise-adoption, evals, mcp-and-tools

A hedge-fund head of AI explains how Contour measures AI ROI: live A/B tests of analyst workflows, process metrics over slow P&L, cost per useful insight, and connector-maintenance time counted as a cost.

- Techniques: Live A/B workflow capture; Agent-synthesized vs analyst-synthesized expert calls; Cost per useful insight; Idea-resurfacing agent; Alt-data via MCP or API connectors into agents; Connector-maintenance time as an ROI line item
- Tools: AlphaSense, Yipit, Rogo, Hebbia, Bloomberg, MCP, APIs (vendor data)

## [Why Compute Still Trades in Group Chats — Affaan Mustafa & Alejandro Soumah Fernandez, Jump Trading](../videos/GCse4OMzY8U.md)
`GCse4OMzY8U` · AI Engineer · 2026-10-24 · q3 · intro · talk · also: infra-cost-scaling, token-cost-efficiency

Jump Trading's compute leads explain how GPU capacity trades bilaterally over chats, why cheaper tokens still raise compute demand, and how prepayments and financing gate startup capacity.

- Techniques: Prepayment step-function capacity model; On-demand bridge versus financed prepayment comparison; Build-vs-rent by utilization curve; Decompose a quote into fungible and non-fungible parts; Risk-first structure selection
- Tools: H100, H200, B300, CoreWeave, Slack, Telegram, Bloomberg chat, ICE chat

## [How to Let AI Agents Sign Up for Your App Safely — Isabelle Williams, WorkOS](../videos/uTrY8slys0w.md)
`uTrY8slys0w` · AI Engineer · 2026-10-23 · q3 · practitioner · talk · also: security-guardrails, mcp-and-tools, product-ux

WorkOS PM walks through letting AI agents sign up for and act inside an app safely, using AuthMD, ID-JAG identity assertions, and agent tokens scoped to a user-bounded ceiling.

- Techniques: AuthMD discovery file; Anonymous trial with claim token; ID-JAG identity assertion grant; Blueprint ceiling with scope intersection; Separate agent principal from user session
- Tools: AuthMD (open markdown-based agent onboarding protocol), WorkOS Agent Auth, ID-JAG (Identity Assertion JWT Authorization Grant, IETF spec), OAuth 2.0, MCP authorization spec (Enterprise Managed Authorization), Okta Cross App Access, Claude (referred to as Claude / Cloud Code in the transcript), Cursor (used to vibe-code the demo app), Waypoint (speaker's demo travel-planning app), Muse and Instinct (personal agents mentioned, no detail given), Maple Itinerary and Trip Ledger (other planning tools the demo agent tried)

## [Don't Trust Your AI Agents. Test Them Like a Scientist — Stephanie Jarmak, Omni Analytics](../videos/A3FL_zTQKU0.md)
`A3FL_zTQKU0` · AI Engineer · 2026-10-23 · q4 · practitioner · talk · also: evals, testing-verification, observability

Stephanie Jarmak (Omni Analytics) argues agent evals should be done like experiments: check the tool pipeline end to end, match the benchmark to your own workload, decouple flags from enforcement, and trust independent traces.

- Techniques: Tool-use pipeline audit; Harness-plus-model pairing as the unit under test; Workload-representative internal benchmark; Explicit metric choice per use case; Separate flagging from enforcement; Independent record comparison for trust; Shadow deployment and production measurement; Autonomy boundary spec for each action
- Tools: Amp (coding agent), Sourcegraph code search MCP tool, Claude (as used in the grep example), grep, Terminal Bench (transcribed as 'Terminal Bench 4'), OpenHands (open coding-agent harness), Opus 5 (model, as transcribed), Astra (model or harness, as transcribed; unverified), Code Scale Bench (speaker's own public benchmark for large codebases), LLM-as-judge (generic pattern), Omni Analytics evaluation harness (in progress)

## [A PHP Bug Just Took Websites Offline Worldwide](../videos/Gxi_n-PtQBo.md)
`Gxi_n-PtQBo` · Better Stack · 2026-10-22 · q3 · intro · news · also: security-guardrails, dev-tools

Better Stack news explainer on the "PHP to Shell" pair of PHP bugs (CVSS 9.2 per the video): unauthenticated remote code execution in PHP itself, a coordinated-disclosure mess that pulled the patch forward, and a warning that AI speeds up exploit building.

- Techniques: Immediate PHP runtime patching when a language-level RCE is announced; Take the service offline when an unpatched RCE is live and the patch is not yet available; Pre-deploy WAF rules before public disclosure
- Tools: PHP, Chainguard PHP images, Cloudflare WAF, GPT 5.6 Sol, Gemini 4 Argon, Claude Mythos, Debian packages, Ubuntu packages, WordPress, Drupal, Joomla, Laravel

## [1,368 AI Failures and What They Teach About Evals — Vishal Srivastava, New York Life & Tanmay Sah](../videos/mMw3arwQsL0.md)
`mMw3arwQsL0` · AI Engineer · 2026-10-22 · q3 · practitioner · talk · also: evals, agent-architecture

Talk using AI Incident Database cases to argue for risk-based, system-level evals: test the whole deployment and the evaluator, try to falsify claims, and prioritize by harm.

- Techniques: Three-dimension, 13-sub-dimension incident taxonomy; Prioritize controls by harm association, not frequency; Materiality scale per AI use case; Four-part risk decomposition; System-level stress testing of the deployment; Evaluator reliability check; Build-break-fix falsification loop
- Tools: AI Incident Database (publicly available database of AI failure reports, used as the analysis corpus)

## [Same GPU, 50% More Output: Why the Operator Matters — Oliver Kennon, SemiAnalysis](../videos/3axY1wz2OvA.md)
`3axY1wz2OvA` · AI Engineer · 2026-10-21 · q3 · practitioner · talk · also: inference-serving, infra-cost-scaling, token-cost-efficiency

Oliver Kennan (SemiAnalysis) argues GPU cost per useful token depends on the operator's serving software and ops discipline, not just the chip, and that cost positions are relative to competitors, which matters for compute futures and rental price hedges.

- Techniques: Cost per acceptable token; Compare on the same chip at a fixed interactivity target; Assess the operator, not just the hardware; Safe update and rollback process for serving
- Tools: SemiAnalysis inference calculator (public), ClusterMax 3.0 (SemiAnalysis operator rating; a 4.0 is mentioned as upcoming), NVIDIA B200 GPU

## [OpenCode Got Hacked Badly (My API Keys Got Drained)](../videos/0p96nZsRxlY.md)
`0p96nZsRxlY` · Kai Explains · 2026-10-21 · q4 · practitioner · news · also: security-guardrails, token-cost-efficiency

OpenCode console breach postmortem: a legacy database with plaintext provider keys survived a "remove legacy" commit, and per-key spend limits, not the attacker, set who lost $16 vs $3,000. Ends with a key-hygiene checklist.

- Techniques: Set a provider hard limit, not just a spend alert; Prepaid credit balances without auto-reload; Revoke keys at the provider, not in the tool; Key inventory and rotation; One key per tool or service; Verify decommissioning of the underlying resource; Encrypt third-party credentials at the application layer
- Tools: OpenCode (terminal coding assistant and console web dashboard), OpenAI API, Anthropic API / Claude API console, Google Gemini API, Google Cloud, Claude, GPT, Gemini

## [The Investor's Edge Lives in Their Head — Anekha Sokhal, Moshi](../videos/UHbODjuviAU.md)
`UHbODjuviAU` · AI Engineer · 2026-10-20 · q2 · intro · talk · also: product-ux, data-engineering

Vendor talk from Moshi's founder arguing that an investor's edge is human judgment: machines should do the data grind, while every AI claim stays traceable and the human makes the call.

- Techniques: Split grind from judgment; Per-claim traceability and measured hallucination; Deterministic multi-agent decomposition
- Tools: Moshi (the speaker's own product, described as a 24-7 quant analyst for institutional traders)

## [Why AI Agents Will Need Their Own Bank Accounts — Lincoln Murr, Coinbase](../videos/f_HwzoYrZ7s.md)
`f_HwzoYrZ7s` · AI Engineer · 2026-10-20 · q2 · intro · talk · also: product-ux, mcp-and-tools

Coinbase's head of AI product on agentic finance: agents that pay and grow money, the X402 HTTP 402 micropayment standard, and trust that is earned in steps. Largely a vendor pitch with some useful adoption data.

- Techniques: Gate content or APIs behind HTTP 402 micropayments (X402); Staged autonomy for agents that handle money; Delegated conditional execution; Ship features as skills that write code on the user's machine; Proactive widgets against chat cold start
- Tools: X402, Agent Kit, LangChain, Coinbase MCP, Coinbase CLI, Coinbase Advisor, GrokBot, Muse, Stripe Link, Stablecoins

## [Shipping AI Into 5 Major Banks Without a 12-Month Compliance Wait — Al Chen, Cisco](../videos/Bz1HFxQA1o8.md)
`Bz1HFxQA1o8` · AI Engineer · 2026-10-20 · q4 · practitioner · talk · also: security-guardrails, enterprise-adoption, sandboxing-execution

Al Chen (Cisco) on shipping AI into five major banks in weeks rather than a year: CVE remediation with agent-run exploit tests, ClickHouse cross-region DR with data-correctness checks, and keeping PII/MNPI out of LLM-judge reasoning, with showing evidence as the main lever for compliance speed.

- Techniques: Agent-driven exploit verification for CVE remediation (Harbor task); Cross-region ClickHouse DR with backup, restore and correctness checks; Split replication of IDs and metadata from core trace data for residency; Gating LLM-judge reasoning behind a sensitive-data check; Audit the judge prompt, not only the UI
- Tools: Harbor, Docker, Modal, Daytona, ClickHouse, ClickHouse backup (Altinity), Sysdig, Wiz, Prisma, NVD, CISA, MITRE CVE database

## [How to Know When an AI Agent Can Work Unsupervised — Evan Kormos, Coinbase](../videos/_4Ph2dhmUFI.md)
`_4Ph2dhmUFI` · AI Engineer · 2026-10-20 · q3 · practitioner · talk · also: evals, agent-architecture, multi-agent

Coinbase's Evan Kormos on deciding when an agent can run unsupervised: keep the process deterministic on the outside, model it as a graph with policy boundaries, and earn autonomy per node through measured evals.

- Techniques: Policy-bounded DAG process map; Cyclic review node with a bounded loop; Per-node automation checklist; Graduated autonomy rollout; DAG state injected into agent context; Statistical evaluation over repeated runs; Exception-flow and volume monitoring
- Tools: Apache Airflow, LangGraph (transcript says LangChain Langraph)

## [Why AI Agents Still Won't Pay for Anything — Jan Curn, Apify](../videos/-AOxpwVeIWw.md)
`-AOxpwVeIWw` · AI Engineer · 2026-10-19 · q3 · practitioner · talk · also: product-ux, security-guardrails

Jan Curn (Apify) argues agents still don't pay for services because the payment funnel (need, setup, trust, buy) has friction at each step, and pay-per-use is the missing piece.

- Techniques: Exact-plus-refund for metered agent billing; Charge before work for non-trivial cost; Escrow then micro-charge (batch settlement); Curated directory as the trust layer for agent-discoverable tools
- Tools: Apify (actors marketplace, about 80k actors), X402 (Coinbase, scheme exact, upto and batch settlement), MPP (Stripe and Tempo; sessions), L402 (Lightning Labs), MasterCard Agent Pay, KYA Pay (Skyfire with Visa), AP2 (Google), ACP (OpenAI and Stripe, Agentic Commerce Protocol), TAP (Visa, Trusted Agents Protocol), UCP (Google and Shopify, Universal Commerce Protocol), ACTP (Alipay), AMP (Alipay, Agentic Mobile Protocol)

## [Buy, Build, Deploy: Using M&A to Drive AI Transformation — Prathik Naidu, Long Lake](../videos/J7n3WJnFTto.md)
`J7n3WJnFTto` · AI Engineer · 2026-10-19 · q2 · intro · talk · also: product-ux, enterprise-adoption

Long Lake's founding partner explains why buying services businesses and then deploying AI inside them beats selling AI agents from outside, using a J-curve and a services-economy margin argument.

- Techniques: Outcome-ownership screening filter for AI deployment targets; Value-capture math for outside-in AI vendors; J-curve tracking for AI deployment

## [An AI Agent Got Its User Banned From Resy — Keycard, JPMorgan Chase & AAuth](../videos/IavxrdVnwXM.md)
`IavxrdVnwXM` · AI Engineer · 2026-10-18 · q3 · practitioner · panel · also: security-guardrails, enterprise-adoption, agent-architecture

Panel on intent-based runtime authorization for agents: per-call authz with mission context, budgets instead of rate limits, and enforcement outside the agent. Core claim: coarse OAuth scopes don't fit autonomous agents.

- Techniques: Budget-as-token grant with live feedback; Brains/hands split with egress-proxy enforcement; Separate supervising agent for worker actions; Deterministic must-never policy plus intent-derived bounds; Dynamic tool gating by task phase; Intent and environment in trace spans
- Tools: OAuth, OIDC, MCP, Claude Code, Squid proxy, Chrome, Firefox, AAuth

## [Insurance Claims Are AI's Messiest Data Problem — Denys Linkov, Wisedocs](../videos/W4pnzOURwHQ.md)
`W4pnzOURwHQ` · AI Engineer · 2026-10-18 · q3 · practitioner · workshop · also: data-engineering, evals, enterprise-adoption

Insurance claims data is messy, so AI claims work needs layered extraction, duplicate detection, human verification, and calibrated tiered benchmarks before cross-claim analytics pay off.

- Techniques: Layered extraction with per-level verification; Tiered benchmark with a private held-out tier; Calibrated multi-judge verification; Back-test on historical samples before pilot; Duplicate and co-mingling detection at intake; Human-in-the-loop surfacing with page references
- Tools: Artificial Analysis MLCR benchmark, GPT models, Anthropic models, ChatGPT, Gemini, Claude

## [Evals for High-Stakes AI Agents — Doneyli De Jesus & Annabell Schäfer, Langfuse](../videos/obfPzbapMIM.md)
`obfPzbapMIM` · AI Engineer · 2026-10-18 · q3 · practitioner · workshop · also: evals, observability, testing-verification

Langfuse workshop on evaluating high-stakes agents: trace everything, build datasets from production via expert error analysis, mix LLM-judge with deterministic evaluators, and gate prompt changes in CI.

- Techniques: Annotation queue for expert error analysis; Free-text comments to failure-mode taxonomy via LLM; Mixed evaluator suite (LLM judge + code checks); Prompt-promotion-triggered CI eval gate; Mask PII before persisting traces; Shadow runs for ground-truth building; Judge calibration against a human-labeled sample
- Tools: Langfuse, GitHub Actions, ClickHouse, PostgreSQL, Amazon S3, OpenAI chat API, Anthropic models, Whisper Flow, Claude, Langfuse skill (agent skill)

## [Why One AI Agent Isn’t Enough (And How to Run 1,000) - CJ Avilla & Harrison Stall, Anthropic](../videos/kiClTcJUnhc.md)
`kiClTcJUnhc` · AI Engineer · 2026-10-17 · q4 · practitioner · talk · also: multi-agent, agent-architecture, security-guardrails

Anthropic's Claude Managed Agents "flows" (dynamic multi-agent workflows) talk: how to fan out hundreds of isolated sub-agents, control cost with budgets, and contain risk with credential vaults, egress rules and auto mode.

- Techniques: Plan, fan out, phase-gate; Per-phase model and agent-count allocation; Separate reviewer context for adversarial checks; Two-stage review with verification; Budget as a resumable circuit breaker; Credential injection at the egress proxy; Declare, contain, detect; Transcript audit agent; Gradual context reveal via linked markdown index; Filesystem as the inter-agent channel; Interrupt and redirect
- Tools: Claude Managed Agents, Claude Code, Claude API skill, ant CLI, Terraform provider for Claude agents, Dynamic workflows (Claude Code), Hill-climb skill, Dreaming (memory consolidation product), Auto mode (permission classifier), Bug Hunter flow, Explainer Video Maker flow, Claude Tag (Slack bot)

## [The AI Bill Is Too Damn High: Tokenomics 101 — Eugene Cheah, Featherless AI](../videos/Ti-BmGU1_mQ.md)
`Ti-BmGU1_mQ` · AI Engineer · 2026-10-17 · q4 · practitioner · workshop · also: token-cost-efficiency, infra-cost-scaling, models-research

Eugene Cheah (Featherless AI) walks through "tokenomics" in four moves (measure, right-size, buy capacity, check processes) to cut inference spend, with per-key tracking, model labels per department, and a warning that tokens are not work done.

- Techniques: Per-team and per-use-case API key split; Speed tier per workload; Planner-worker model split; Eval-driven model downsizing; Department-level model labels; Dedicated capacity for base load, burst to public cloud
- Tools: Claude Code, Pi coding agent harness, simple-classifier (open source, speaker's project), tokenomics tracking tool (open-sourced by speaker's company)

## [Stop Chatting With Spreadsheets — Francesco Galletta & Felippe Felisola Caso, Monzo](../videos/e9-br9hveRI.md)
`e9-br9hveRI` · AI Engineer · 2026-10-17 · q3 · practitioner · workshop · also: agent-architecture, testing-verification, data-engineering

Hands-on workshop on building a trustworthy financial-analysis harness around five principles (shared domain, deterministic calculations, evidence, accountability, verification), demoed on a wedding-budget planner.

- Techniques: Interview-style shared-domain planning with a decision tree; Calculation-as-code with tests and golden examples; Fact / assumption / interpretation labelling with provenance; Branching challenge agent with merge or dismiss; Tiered accountability gates
- Tools: Claude Code, Codex, Looker Studio, Google Slides, Google Sheets

## [Your AI Isn’t the Problem. Your Infrastructure Is. — Jiachen Jiang, Coder](../videos/Wb2v9Phhnns.md)
`Wb2v9Phhnns` · AI Engineer · 2026-10-15 · q3 · practitioner · talk · also: security-guardrails, sandboxing-execution

Coder's staff PM walks through three real AI-agent incidents (a Replit prod wipe, a Copilot-enabled bank exfiltration, the NX supply-chain attack) and argues that infrastructure controls, not smarter models, prevent them.

- Techniques: Ephemeral remote workspaces with no route to production; Per-task short-lived, narrow-scope credentials; Identity-aligned access control for AI tools; Model proxy layer; Agent sandboxing as a firewall; Externally owned audit logs with real-time alerting; Planning-only mode and automatic dev/prod DB separation; Premortem with the team
- Tools: Replit Agent, Microsoft Copilot, Nx (build tool), Coder workspaces, Claude Code, Codex

## [Rebuilding CI for AI-Scale Commit Volume — Gautam Korlam, Sonar](../videos/7b9tov5Uc5s.md)
`7b9tov5Uc5s` · AI Engineer · 2026-10-15 · q3 · practitioner · talk · also: pr-code-review, software-factory, infra-cost-scaling

Gautam Korlam (Sonar/QAR, ex-Uber) on why CI, merge queues and review were built for human speed, and how to keep agent-scale commits green, fast and auditable in regulated teams.

- Techniques: Parallel speculative merge queue; Move checks left and offload expensive checks; Cache, shard and reduce compiler churn; Layered AI review with a fast first pass; Policy-based auto-approval with escalation; Durable decision record on the PR
- Tools: Rust, GitHub, Next.js (captioned 'next text'), Uber SubmitQueue (captioned 'summit cube')

## [Tokens Are the Cheap Part — Steve Jamison, Jellyfish](../videos/U7ZYBCcdJPg.md)
`U7ZYBCcdJPg` · AI Engineer · 2026-10-14 · q4 · practitioner · talk · also: token-cost-efficiency, enterprise-adoption, coding-agents

Steve Jamison (Jellyfish) argues AI tokens are a small share of PR cost; tracking total intelligence cost per merged PR, with revert rates as a counterweight, beats watching the token bill alone.

- Techniques: Blended cost per merged PR; Token-spend quintile cohorts; Within-developer baseline comparison; Counterweight metrics beside throughput

## [Judge a Transaction by the Company It Keeps — Somya Rai & MD Sharique, EXL](../videos/SHvwutPSeZg.md)
`SHvwutPSeZg` · AI Engineer · 2026-10-14 · q4 · practitioner · talk · also: models-research, inference-serving

EXL engineers show a graph neural network feeding XGBoost for card fraud, lifting true-positive capture 27-33% at a fixed alert rate and serving it in about 3 ms P99.

- Techniques: Soft-target sampling that keeps graph connectivity; Disjoint time-window graphs for leakage control; Order-invariant multi-statistic neighbor aggregation; GNN embeddings as features for an existing gradient-boosted model; Entity-behavior deviation features; Layer-wise full-graph precomputation with a cached serving path; Edge-level prediction with entity-only embedding cache; Subgraph attribution for analyst-facing explanations; Latency hygiene for Python model serving
- Tools: XGBoost

## [What Technical Due Diligence Finds When the Deck Says “70% Automated” — Soukaïna Abelhad](../videos/gDRCpTMCqEU.md)
`gDRCpTMCqEU` · AI Engineer · 2026-10-14 · q4 · practitioner · talk · also: evals, enterprise-adoption

A technical due diligence checklist for AI productivity claims: check the arithmetic of workload vs. human labor, define what "automated" means, and verify quality with experts before trusting a number.

- Techniques: Workload-vs-labor arithmetic check; Straight-through processing boundary; Blind expert review of grader output; Cost per accepted autonomous task; Diligence questions checklist
- Tools: Faros telemetry, Meta grader study

## [The Agent Works. Does Anyone Trust It? — Michele Grant, Leading at Scale](../videos/-a2oTS9J67U.md)
`-a2oTS9J67U` · AI Engineer · 2026-10-14 · q3 · practitioner · talk · also: enterprise-adoption, observability

Michele Grant on earning trust in enterprise AI agents: define value, name an accountable owner, and grant autonomy in stages backed by audit evidence, using an M&A integration example.

- Techniques: Pre-deployment value case with baselines; Human work standard (one-page decision map); Deterministic core for financial math; Telemetry as proof, not the model's summary; Four-stage autonomy scorecard; Regression triggers in the model inventory

## [Deploying AI Inside a Bank Is Not an Engineering Problem — Paden Gayle, Applied AI Engineers](../videos/3ZlQk4-knWM.md)
`3ZlQk4-knWM` · AI Engineer · 2026-10-14 · q3 · practitioner · talk · also: enterprise-adoption, evals

Paden Gayle argues that shipping AI inside a bank is a discovery problem: find the people who own each decision in week one, shrink the scope, limit the model's authority, and build an evidence pack from sprint one.

- Techniques: Week-one decision discovery; Dependency-mapped architecture diagram; Shadow, draft, shrink; Four-rung autonomy ladder; Model proposes, human submits boundary; Five-file evidence pack with failure table; Decision-time record capture; Segment-first evaluation reporting; Five-question readiness scorecard

## [Your Agent Is a Lethal Trifecta (And What to Do About It) — Kim Maida, Keycard](../videos/ws9XcGGPBDk.md)
`ws9XcGGPBDk` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · also: security-guardrails, mcp-and-tools

Kim Maida (Keycard) argues agents with private data, untrusted content and external comms form a "lethal trifecta" and shows how token exchange (OAuth 2 RFC 8693-style STS), task-scoped ephemeral tokens and mission-based authorization contain the blast radius without removing capabilities.

- Techniques: Per-tool-call token exchange through an STS; Mission-scoped approval before tool use; Keep all three trifecta legs and control access instead; Audit with attributed identity chains
- Tools: Keycard, OAuth 2 token exchange (RFC 8693 style), MCP servers, MCP gateway, Snowflake, Incident pager API, Google login

## [Reliable, Smart Workflows for Finance, Wealth and Insurance — Karthic Rao, Perpetual](../videos/8g0g1ncwzG0.md)
`8g0g1ncwzG0` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · also: agent-architecture, enterprise-adoption

Karthik Rao (Perpetual CTO) on building reliable, regulated wealth-management workflows: an LLM planner emits a typed graph, a deterministic compiler fails closed, and models make only small typed judgments.

- Techniques: Planner emits typed semantic graph, compiler verifies with no model; Closed action grammar with typed contracts; Payload-hash-bound approval gates; Provisional judgments awaiting human confirmation; Side-effect lifecycle with no automatic retry; Rule-based timeouts instead of model decisions; Route judgments to a small tier and log frontier calls as training data

## [AI Security Engineer Foundations + Certificate — Micah Silverman, Snyk](../videos/p-2MT8KYZqU.md)
`p-2MT8KYZqU` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: security-guardrails, mcp-and-tools, vibe-coding-app-building

Two-hour Snyk workshop on AI security foundations: OWASP LLM Top 10 risks, shadow AI and AI bills of materials, AI threat modeling, MCP tool poisoning, vibe-coding failures, and a live CTF chatbot exercise.

- Techniques: Layered prompt-injection defense; Keep secrets out of prompts and enforce access outside the model; Scope chatbot data to what may be disclosed; AI threat modeling workflow; Adversarial review of an architecture; AI BOM as a CI gate; Audit MCP configs and servers before enabling; Secure-by-design playbook for agentic coding; Probe a chatbot in a CTF-style sandbox; Offer an approved alternative when restricting a tool
- Tools: Snyk Evo, Snyk Agent Scan, Snyk Code, Snyk (SCA/SAST), OWASP Top 10 for LLM Applications, STRIDE, DREAD, SBOM (SPDX, CycloneDX), CycloneDX (AI/ML BOM support), Model Context Protocol (MCP), Figma Framelink MCP server, OpenClaw

## [The SDLC You Build Yourself — Andy Wong, Andrei Bocan & Shane Wolf, Atlassian](../videos/ojJXgXLUQFc.md)
`ojJXgXLUQFc` · AI Engineer · 2026-10-12 · q2 · intro · workshop · also: software-factory, pr-code-review, context-engineering

Atlassian team walks through its AI SDLC stack (Jira Coding Agent, AI Reviewer, AutoDev, AI SRE, AI Planner) built on a shared context engine, with a hands-on workshop that was largely lost to Wi-Fi problems.

- Techniques: Org-wide standards as enforceable PR rules; Trained filter on review comments; Human-set authority flag on context sources; Acceptance-criteria self-check in a sandbox; Progressive migration with per-engineer quotas; Automation-triggered agent session per sub-ticket; Per-skill and per-subagent model selection; Spend caps and WIP limits on autonomous work
- Tools: Jira Coding Agent, AI Reviewer, AI AutoDev, AI SRE, AI Planner, Rovo Dev, Teamwork Graph CLI, Confluence, Bitbucket, Slack, Docker, Claude

## [The Tiny TTS Everyone Loved Isn't Tiny Anymore (KittenTTS 2)](../videos/9YzLI8-uF4s.md)
`9YzLI8-uF4s` · Better Stack · 2026-10-12 · q3 · practitioner · review · also: voice-multimodal, local-ai

Hands-on review of KittenTTS 2: it has grown to 1.7B parameters, runs slower than real time on a Mac CPU, and ships source-available weights under a revocable, revenue-gated license, unlike the tiny Apache-2.0 original.

- Techniques: Clone a voice from a short reference clip; Check that the GPU is actually used; Turn off text normalization for non-English text; License gate before shipping model weights
- Tools: KittenTTS 2 (Kitten TTS v2), Kitten TTS (original, Apache 2.0), S3 Gen vocoder (Resemble AI, Chatterbox Turbo), Whisper (reference-clip transcription), PyTorch (torch), transformers, diffusers, Activity Monitor, ElevenLabs, VoxCPM2, libtorch (C++ port), Hugging Face

## [Containment Is Lying to You: Measuring AI Agents Like Employees — Druid AI](../videos/PwCSYy-oGsM.md)
`PwCSYy-oGsM` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: evals, enterprise-adoption, product-ux

Druid AI argues containment rate misleads agent evaluation and proposes a weighted, 0-2 scored framework (six pillars, 26 components) judged like an employee and re-run weekly against a human baseline.

- Techniques: Component scoring with weighted clusters; Mandate-first agent definition; Success criteria attached to each task; Weekly re-run against a human baseline; Hybrid accuracy measurement; Central handoff and action-center check; Skill-source and granularity review; Error tolerance set by mode; ROI as freed human time

## [AI Security Engineer Foundations + Certificate — Javier Garza, Snyk](../videos/ZyC56eV8sVw.md)
`ZyC56eV8sVw` · AI Engineer · 2026-10-12 · q2 · intro · workshop · also: security-guardrails, mcp-and-tools, coding-agents

A two-hour Snyk workshop on AI security basics: OWASP LLM Top 10, shadow AI and AI bills of materials, AI threat modeling, MCP and skill supply-chain risk, and secure-by-default coding hooks.

- Techniques: Treat LLM input and output as untrusted data; Read-only database views for agents; Approval gate for high-risk actions; Full action logging plus a background log scanner; Scan-fix-rescan agent hook; Pre-install scanning of MCP servers and skills; AI-BOM inventory with query by component; Security requirements inside the prompt
- Tools: Snyk agent-scan (MCP and tool scanner), Snyk AI-BOM (CycloneDX-style inventory), Gandalf (Lakera) prompt-injection game, Claude Code, Cursor, Windsurf, OpenClaw, CycloneDX, SPDX, STRIDE, MITRE ATLAS, uvx

## [AI Agents Don't Read Your Policy Docs. They Hit Your APIs — Gravitee](../videos/7v2myBde05o.md)
`7v2myBde05o` · AI Engineer · 2026-10-11 · q2 · practitioner · review · also: security-guardrails, infra-cost-scaling, mcp-and-tools


- Techniques: Per-task scoped agent identity via token exchange; Gateway-level rate limiting on agent requests; Semantic cache keyed on prompt similarity; Pre-request prompt size and relevance policies; Narrowing MCP servers to a per-agent tool subset; Export gateway telemetry to existing observability stack
- Tools: Gravitee AI Gateway, Anthropic Claude (Sonnet), Groq (inference), Databricks, Redis (built-in semantic cache), MCP (Model Context Protocol), A2A (agent-to-agent protocol), OpenTelemetry, Datadog, Splunk, Prometheus, Kubernetes

## [An AI Future Without the Lock-In — Remy Guercio, Tailscale](../videos/s-glGHAa1a4.md)
`s-glGHAa1a4` · AI Engineer · 2026-10-11 · q2 · intro · talk · also: infra-cost-scaling, mcp-and-tools

Tailscale's Remy Guercio argues for "ROI maxing" over token maxing: keep choice at every AI layer through an identity-aware AI gateway (Aperture) to avoid lock-in. Mostly a product pitch.

- Tools: Tailscale, Aperture (Tailscale AI gateway), WireGuard, TSNet, Entra, Okta, Anthropic API, OpenAI API, Vercel AI gateway, AWS Bedrock, Codex, Claude Code

## [Let Anyone at Your Company Ship Internal Apps with AI — Garrett Galow, WorkOS](../videos/HTzgC3FoYsI.md)
`HTzgC3FoYsI` · AI Engineer · 2026-10-09 · q3 · practitioner · talk · also: vibe-coding-app-building, enterprise-adoption

WorkOS's Garrett Galow on a CLI, a Cloudflare-based platform and SSO-by-default that let non-engineers build and ship internal apps; 37% of about 60 apps had no engineer commits.

- Techniques: Pre-flight local setup CLI with template scaffolding; SSO gate on every deployed app by default; Platform abstraction over deploy target; Pair non-engineer driver with engineer consultant in timed hackathons; Push-to-register catalog with shared skills
- Tools: Claude Code, Codex, Lovable, Cloudflare Workers, Cloudflare D1, Cloudflare KV, Doppler, Okta, GitHub, Webflow, Slack, Node.js

## [The Software Factory: From Bug Report to Production Code — Davis Palmie, Factory](../videos/exiwa9QbQXI.md)
`exiwa9QbQXI` · AI Engineer · 2026-10-08 · q3 · intro · talk · also: software-factory, context-engineering

Factory's Davis Palmie argues engineers should build a "software factory" of agents that turns signals like bug reports into production code, starting narrow, measuring outcomes, and staying model- and surface-agnostic.

- Techniques: Narrow-first, verifiable agent pillar; Close the loop only after tying outputs to input signals; Agent readiness checklist (eight pillars); Per-task model routing for cost versus quality; Single harness and context shared across surfaces; Outcome-based agent metrics
- Tools: Sentry, Slack, AGENTS.md, Factory

## [Every AI Company Is Accidentally Building a Bank — Dor Sasson, Stigg](../videos/cf2IhzqeQH4.md)
`cf2IhzqeQH4` · AI Engineer · 2026-10-07 · q3 · intro · talk · also: infra-cost-scaling, product-ux

Stigg's CEO argues AI usage pricing needs bank-style runtime controls: synchronous entitlement checks before consumption, hold-and-settle for concurrency, and layered credit pools, not invoice-time reconciliation.

- Techniques: Synchronous pre-consumption check with async settlement; Hold, settle, and idempotency for concurrent draws; Ordered draw-down across credit sources; Deterministic decision waterfall; Metering ledger inside the customer VPC
- Tools: Stigg, OpenClaw, Claude Max, GitHub Copilot

## [Move Fast and Don't Break Things: Scaling Databases for the AI Era — PlanetScale](../videos/uKUA1a0Kdfc.md)
`uKUA1a0Kdfc` · AI Engineer · 2026-10-07 · q3 · intro · talk · also: dev-tools, infra-cost-scaling

PlanetScale's Ben argues that agent-driven change can be safe if databases are isolated, sharded, back-pressured, and branched like code, with agents given the same primitives humans use.

- Techniques: Per-segment traffic budgets with graceful degradation; Shard with a routing proxy plus per-shard replicas; Declarative sharding config as JSON for agent drafting; Schema branch, deploy request, one-click revert; Isolation by failure domain
- Tools: PlanetScale, Vitess, VTGate, MySQL, Postgres, SQLite, MCP server, CLI, VSchema

## [From Raw Documents to AI-Ready Data — Leo Platzer & Jeff Koss](../videos/wzWNYDY7toc.md)
`wzWNYDY7toc` · AI Engineer · 2026-10-06 · q2 · intro · demo · also: data-engineering, rag-retrieval

Vendor talk (DZ Labs, now Colibra) on turning millions of messy SharePoint documents into AI-ready data by tagging, deduplicating, freshness-filtering and scoping them before RAG.

- Techniques: Conditional tag tree with AI suggestions and human review; Dedupe and freshness pruning before indexing; Hybrid pattern plus LLM sensitive-data scan; Folder-level context index file; Scheduled data slices
- Tools: SharePoint, DZ Labs (DZ data curation platform, DZ SDK), Colibra, Claude Code, Codex, vector database, knowledge graph

## [The Human Is an Async API — Melanie Warrick, Temporal](../videos/jc3kbZkuHTo.md)
`jc3kbZkuHTo` · AI Engineer · 2026-10-05 · q3 · practitioner · demo · also: agent-architecture, multi-agent

Melanie Warrick (Temporal) shows durable execution for multi-agent systems: a human approval is a wait condition plus a signal on a parked workflow, so the rest of the system keeps running and survives restarts. It is a vendor-led talk with a live ice-cream delivery demo.

- Techniques: Human approval as wait condition plus signal; Wrap every model and tool call as an activity; LangGraph interrupt bridged to a durable wait; Child workflow per entity; Cost-of-being-wrong gate for human review
- Tools: Temporal, Google ADK, LangGraph, Google Maps API, Google Search, Python, TypeScript, Rust

## [The Chief AI Officer: Scientist, Architect, Coach — Rania Khalaf, WSO2](../videos/9cJrbj23fOA.md)
`9cJrbj23fOA` · AI Engineer · 2026-10-04 · q3 · intro · talk · also: enterprise-adoption, product-ux

WSO2's Chief AI Officer Rania Khalaf on running the role as scientist, architect and coach, with adoption-based metrics instead of token counts.

- Techniques: Three-dimension role mapping; LLM-assisted role analysis; Adoption depth ladder; Agent-ready product checklist; Dogfooding with a closed feedback loop
- Tools: Claude, Gemini, BERT, MCP, Databricks

## [YOLO Mode, Safely: MicroVM Sandboxes for Any Agent — Rowan Christmas, Docker](../videos/OE_lLNCNfQo.md)
`OE_lLNCNfQo` · AI Engineer · 2026-10-04 · q2 · intro · talk · also: sandboxing-execution, security-guardrails

Docker's product manager argues coding agents need micro-VM sandboxes with secret placeholders and default-deny egress, and shows a self-test where Claude Code found his bank data. Mostly a product pitch.

- Techniques: Run agents in a micro-VM with bypass permissions on; Placeholder secrets swapped at the network boundary; Default-deny egress with an allowlist; Read-only mounts of context repos; Self red-teaming with real personal data
- Tools: Docker SBX, Claude Code, Claude Desktop, Codex, CrowdStrike, Cedar, Datadog

## [Your Agents Are in Solitary Confinement: Why MCP & A2A Aren't Enough — Vlad Luzin, Band](../videos/UOcHfR3_tys.md)
`UOcHfR3_tys` · AI Engineer · 2026-10-04 · q2 · practitioner · talk · also: multi-agent, mcp-and-tools, agent-architecture

Vendor talk by Band's CTO arguing that multi-agent coordination needs a conversation-level collaboration layer (rooms, consent, routing, governance), not just MCP or A2A, then demoing that product.

- Techniques: Bilateral consent before agent-to-agent contact; Rooms and channels with deterministic routing as the agent primitive; Network-level traffic capture for cost and attribution; Live architecture layout reporting from agents; Human-in-the-loop pings and manager kill switch
- Tools: Band (collaboration layer / platform, speaker's company), Jam (desktop app built on Band, also called 'GEM' near the end of the transcript; the name is ambiguous in captions), Claude Code, Codex (OpenAI), LangGraph (LangChain), MCP (Model Context Protocol), A2A (Agent-to-Agent protocol), ACP (protocol, named without detail), Telegram, Discord, Slack, WhatsApp

## [Your LLM App Returned 200 OK. It Was Still Wrong. — Marina Petzel, Datadog](../videos/rTojoVotlD8.md)
`rTojoVotlD8` · AI Engineer · 2026-10-04 · q3 · intro · talk · also: observability, evals, security-guardrails

Datadog's Marina Petzel argues LLM apps need cost, safety and quality monitoring on top of the golden signals, since a 200 OK can still hide a wrong answer; gives tagging and metric recommendations.

- Techniques: Mandatory four-level cost tagging; Track token creep and model drift as separate alerts; Caching layer to remove redundant completions; Guardrail metrics as blocking thresholds; LLM-as-judge for completeness, embeddings for relevance; Score RAG retrieval separately
- Tools: Datadog agent observability

## [DeepSeek and Kimi Secretly Sent Your Prompts to Claude](../videos/hSVCYzphZjQ.md)
`hSVCYzphZjQ` · Better Stack · 2026-10-02 · q3 · intro · news · also: security-guardrails, models-research

Recap of Anthropic's report accusing Alibaba, Moonshot, DeepSeek, Z.ai, Xiaomi and others of industrial-scale distillation of Claude via fake accounts and proxies, plus the API changes it prompted.

- Techniques: Preserved Thinking constraint (Anthropic API, per speaker); Do not depend on raw reasoning text; Platform-side extraction defenses (extrapolated, not stated in the video)
- Tools: Claude Opus 4.6, Claude Opus 4.7, Claude Opus 4.8, Claude Haiku, Fable (model name as spoken; Fable 5.1 cited for Preserved Thinking), Claude Code, Claude Agent SDK, OpenCode, Qwen 3.5/3.6/3.7 (Alibaba), Kimi (Moonshot), DeepSeek, GLM 5.3 (Z.ai)

## [Oracle’s $288B Lease: The Debt They Can’t Escape](../videos/mNozPwLvJIY.md)
`mNozPwLvJIY` · Kai Explains · 2026-10-02 · q3 · intro · news · also: infra-cost-scaling, models-research

Kai Explains argues Oracle's Project Jupiter force majeure notice is not an exit signal; the real constraint on AI capacity is power and permits, not demand.

- Techniques: Read the contract and filing before the headline; Trace cash flow by layer and strip out one-off inflows; Compare market timestamps with news timestamps
- Tools: Oracle Cloud Infrastructure, OpenAI, Bloom Energy fuel cells, GE Vernova gas turbines, Energy Transfer pipeline, Blue Owl Capital, Stack Infrastructure

## [LangGraph vs OpenAI Agents SDK vs Claude Agent SDK](../videos/8C3LB6TPxwk.md)
`8C3LB6TPxwk` · Kai Explains · 2026-10-02 · q4 · practitioner · review · also: agent-architecture, multi-agent, claude-code

A practitioner comparison of LangGraph, the OpenAI Agents SDK and the Claude Agent SDK: the architectures have converged, but licensing, billing, language support, version stability and data-retention terms are what should drive the choice.

- Techniques: In-distribution test for harness choice; Pick by constraint, not by benchmark; Read the terms section before building; Verify checkpoint and resume claims against release notes; Measure latency on a representative task early; Trace handoffs as tool calls
- Tools: LangGraph, LangChain middleware, OpenAI Agents SDK (0.22; 0.14, 0.20 referenced), Claude Agent SDK (Python and TypeScript; 0.2.x patch 152), Claude Code (transcribed as 'clawed code'), Claude managed agents, OpenAI managed deep agents (public beta, US, CLI first), Microsoft AutoGen, Google ADK, Microsoft's new agent framework (unnamed), Postgres checkpointer (LangGraph), GPT-4o (transcribed as 'GPT-40')

## [Your AI Subscription Is Now Worth Less](../videos/FWShtLCP4OY.md)
`FWShtLCP4OY` · Kai Explains · 2026-10-02 · q3 · practitioner · other · also: token-cost-efficiency, claude-code, context-engineering

Why Claude's Max-plan limits feel smaller: unpublished capacity fractions, per-turn overhead from CLAUDE.md and MCP servers re-billed every turn, and default high reasoning effort. Practical fixes included.

- Techniques: Read the floor before a session; Prune idle MCP servers; Set reasoning effort per task instead of leaving it on high; Ask for markdown when fetching docs; Write specific prompts with form and constraints; Measure what an hour of your work costs
- Tools: Claude Code, Claude Pro, Claude Max 5x, Claude Max 20x, CLAUDE.md, MCP servers, Extended thinking (reasoning effort setting), Limit Reset command, Low Priority Mode, OpenAI Codex, GitHub Copilot

## [Open Source AI is dying (and I know why)](../videos/zxnXemN98d0.md)
`zxnXemN98d0` · Kai Explains · 2026-10-02 · q4 · practitioner · talk · also: local-ai, inference-serving, token-cost-efficiency

Kai argues open-weight AI died at the size where models no longer fit on hardware you own. Below that line the freedom holds, and frontier open weights now work mainly as a price ceiling on hosted APIs.

- Techniques: Break-even check for self-hosting vs API; Local memory budget before choosing a model; Pin the provider, not just the model name; Detect silent compaction and context caps; Pre-adoption license and file audit
- Tools: Kimi K3, DeepSeek V4 Flash, DeepSeek V4 Pro, DeepSeek V3, Llama 3.3 70B, Llama 2, Gemma 4, Qwen 3.6, Alibaba Qwen, Ollama, OpenRouter, Lambda Labs

## [IT Admin for the AI Workforce — Sarthak Aggarwal, Decawork](../videos/q-WOjZhOMCA.md)
`q-WOjZhOMCA` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: security-guardrails, agent-architecture, mcp-and-tools

Sarthak Aggarwal (DecaWork) argues agents should be governed like employees: each needs an identity, scoped short-lived capabilities, a policy gate outside the model, and receipts plus fast revocation.

- Techniques: Typed plan before evidence (plan-then-execute split); Out-of-model policy gate per tool call; Runtime agent identity card; Short-lived, audience-bound capability tokens
- Tools: Microsoft 365 Copilot, Microsoft Agent 365, Okta, AWS AgentCore Identity, MCP, A2A, Replit

## [The Design-Code Roundtrip That Isn't — Jonathan Gordon, ReWeaver AI](../videos/NW-jwOVr32w.md)
`NW-jwOVr32w` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: product-ux, vibe-coding-app-building

Jonathan Gordon (ReWeaver AI) argues a lossless design-code round trip is not yet solved and proposes deterministic guardrails plus provenance to control drift around LLM-generated UI code.

- Techniques: Design-system extraction from code into the design canvas; Joint drift report across code and design; Deterministic guardrails around LLM generation; Fidelity metric per iteration (production drift ratio); Undo and review loop for AI code edits
- Tools: Figma, Sketch, Cursor, Claude Code, ReWeaver

## [From coding to Knowledge work agents — Karan Vaidya, Composio](../videos/xxfMT-bPEmU.md)
`xxfMT-bPEmU` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: agent-architecture, sandboxing-execution, memory

Composio CTO on why coding agents work and knowledge-work agents don't: six missing primitives (centralization, history, context, verification, governance, reversibility), enforced with walls and sandboxes rather than prompts.

- Techniques: Single connection hub for agents; Cross-app action record; Skill distillation from run logs; Pre-send style check against past outputs; Sandbox mirror of production tools; Two-layer walls: access scope plus behavior policy; Tiered gates scaled to blast radius; Undo for reversible actions, sandbox for the rest
- Tools: Composio, Claude Code, Codex, Cursor, OpenClaw, Git, Salesforce, Notion, Gmail, Slack, Zendesk, bugbot.md (named in passing)

## [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../videos/zrZ1amZBSPw.md)
`zrZ1amZBSPw` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: infra-cost-scaling, security-guardrails

Principal engineer at Twilio on running an LLM gateway in production: per-request fallbacks, per-route latency timeouts, guardrail fail-open/closed choices, load shedding, and centralizing governance without centralizing traffic.

- Techniques: Per-request provider fallback; Cool-down for failing providers; Per-route P99 and timeouts; Hedged requests for the tail; Guardrail time budget and explicit fail mode; Guardrail placement by output type; Bounded queues and load shedding with priorities; Per-route API key segregation; Decentralized traffic, centralized governance

## [Reverse-Engineering the AI Buyer — Aliisa Rosenthal, Acrew Capital](../videos/wdTRsfw0KG0.md)
`wdTRsfw0KG0` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: product-ux, enterprise-adoption

A former OpenAI go-to-market leader on building automated sales machinery before hiring humans, launching self-serve first, avoiding pilots, and pricing usage instead of seats.

- Techniques: Automation-first go-to-market build-out; Self-serve first, then sales-assisted; Pilot alternatives that keep control of the deal; Trust portal and automated security review; Usage-based pricing with spend controls; Design partner on non-production internal product
- Tools: Clay, Nooks, Microsoft Copilot, ChatGPT Enterprise

## [From Tokenmaxxing to Trusted Throughput — Mingsheng Hong, Ironclad](../videos/dSg0pu8d6qg.md)
`dSg0pu8d6qg` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: token-cost-efficiency, pr-code-review

Ironclad's VP of AI Engineering on controlling AI token spend: measure cost against value, treat usage dashboards as smoke detectors, and fix the review and CI bottlenecks that code generation creates.

- Techniques: Cross-tool cost aggregation; Usage as an anomaly signal; LLM T-shirt sizing of merged PRs; Three-bucket trusted-throughput check; AI-first review gate; Bounded agent fix loops; Prompt-cache-friendly prompt layout; Context pruning and summarizing in long sessions; Buy non-differentiating tools, build a prompt playbook; Developer-experience metrics for CI
- Tools: Claude Code, Codex, Cursor, vendor usage dashboards, LLMs for PR complexity scoring, CI/CD pipeline

## [Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health](../videos/YXEqC05WEI0.md)
`YXEqC05WEI0` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: security-guardrails, evals, observability

Hinge Health's AI lead on shipping member-facing health AI: put irreversible decisions in code above the model, strip PHI at ingestion, monitor live traffic, and verify the judge before fixing the agent.

- Techniques: Code-layer routing above the model; PHI stripping at ingestion with environment and region separation; Layered live scoring of production traffic; Judge-first triage before agent changes; Severity triage for launch decisions

## [Your Agent Just Authorized What?! — Jay Mok & Ben Coumes, Paypal](../videos/vGn6N4-bxBY.md)
`vGn6N4-bxBY` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: security-guardrails, enterprise-adoption

PayPal's Jay Mok and Ben Coumes propose a stakes-and-counterparty matrix for deciding how much proof an agent's payment authorization needs, ending with verifiable mandates for high-stakes, open-ecosystem transactions.

- Techniques: Stakes x counterparty evidence matrix; Scoped, time-bound, amount-capped mandates; Layered selective-disclosure credentials; Pre-authorize intent before the action target is known; Scoped OAuth access to stored credentials
- Tools: Claude Code, FIDO verifiable intents, AP2 mandate, PayPal approval token, PayPal vault, OAuth, Passkeys, GitHub, Jira, Linear

## [Loophole: Adversarial Agents To Stress Test Your Morality — Brendan Rappazzo, Morgan Stanley](../videos/hOWU0KPUp1k.md)
`hOWU0KPUp1k` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: evals, multi-agent, context-engineering

Brendan Rappazzo presents Loophole, an open-source game where two adversarial agents hunt contradictions in a legal code codified from the user's morals, then extends it to chatbot prompts, contracts, and simulated Senate votes.

- Techniques: Adversarial loophole and overreach search; Judge with auto-patch first, human escalation second; Formalize natural-language values into numbered legal text first; Persona-conditioned rule generation for simulation; Hill-climbing text against an adversarial judge
- Tools: Claude, GitHub

## [x402 isn’t good (yet) — Jan Curn, Apify](../videos/h6mi88VrPtQ.md)
`h6mi88VrPtQ` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: security-guardrails, mcp-and-tools

Apify's CEO lists x402 agent-payment flaws (double-spend before settlement, HTTP 402 vs MCP 401 conflict, poor fit for metered jobs) and his team's workarounds, including an agent-facing markdown gateway.

- Techniques: Charge-then-refund for metered jobs; Work-after-settlement for near-zero-cost calls; Agent-facing markdown instructions plus prepaid token; Batch micropayments via escrow and signed vouchers; Local wallet with cryptographic key and QR code
- Tools: x402 (Coinbase), MPP (Stripe, Tempo), HTTP 402 Payment Required, MCP, Apify actors, agi.apify.com, Coinbase facilitator

## [Why Your AI Agent Needs a Wallet: USDC and Nanopayments — Harshal Bhangale, Circle](../videos/xKzU_3riL6s.md)
`xKzU_3riL6s` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: infra-cost-scaling, mcp-and-tools

Circle engineer argues agents need wallets: x402 pay-per-request with USDC nanopayments and wallet-enforced spend caps, shown in a live Claude Code demo. Vendor pitch with a real but partly failed demo.

- Techniques: Wallet-enforced spend caps; HTTP 402 pay-per-request (x402); Off-chain signed authorizations with later settlement
- Tools: Claude Code, Circle Agent Wallet, x402, USDC, Circle Gateway, Nanopayments, Gmail, Blockrun (data provider), Polymarket data

## [FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](../videos/GJX19pNhmSw.md)
`GJX19pNhmSw` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: token-cost-efficiency, observability, agent-architecture

Microsoft's Tisha Chawla and Susheem Koul argue agent cost control belongs at the agent-run layer, not the request layer. They show an out-of-band "TokenOps" plane that attributes spend per run, steers runs toward budget before halting them, and reports vendor benchmarks.

- Techniques: Run-scoped attribution tags and budgets; Boundary decorator on agent methods; Governor with a developer-declared action allowlist; Tiered policy ladder: steer, then halt; Cost guard: projected-overrun steering; Preview (shadow) mode for guardrails; Benchmark against throttling baseline
- Tools: OpenTelemetry, LangChain, LangSmith, LiteLLM, Portkey, Cloudflare AI Gateway, browser-use, MetaGPT

## [Teaching agents to pay — Anna Spysz, Stripe](../videos/A-zeQiYkmXk.md)
`A-zeQiYkmXk` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: security-guardrails, mcp-and-tools, product-ux

Stripe engineer builds an agentic-commerce agent to buy headphones, covering the Universal Commerce Protocol, merchant manifests, shared payment tokens, persona effects on behavior, and a guardrail checklist.

- Techniques: Merchant capabilities manifest at /.well-known; Structured catalog and policy JSON; Attribute-match decision logging; Persona-driven behavior control and A/B testing of system prompts; Scoped payment token instead of raw credentials; Provider-enforced transaction limits; Agent commerce guardrail checklist
- Tools: Universal Commerce Protocol (UCP), Stripe payments, Google Pay, Apple Pay, shared payment token

## [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../videos/M05vON8i0aI.md)
`M05vON8i0aI` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: skills-self-improvement, enterprise-adoption, context-engineering

Imad Touil (QuantumBlack) argues org know-how should live in governed agent skills: a central registry with owners, versions, access control and evals. Ungoverned skills bring duplication, quality decay, security risk and wasted tokens.

- Techniques: Skill catalog with metadata and an MCP search front end; Microservice-style skill design; Progressive disclosure of skills; Runtime composition of regulatory skills into a review workflow; Static skill tests before any evaluation; Individual-to-team-to-platform promotion path
- Tools: Claude Code, Cursor, MCP, Backstage (IDP), GitHub

## [Your company brain will leak secrets: how we stopped it for big banks — Tanmai Gopal, PromptQL](../videos/0uC6u0lJJl4.md)
`0uC6u0lJJl4` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: memory, security-guardrails

Tanmay Gopal (PromptQL) on why a shared company brain leaks secrets and how to gate it: one company-wide markdown wiki with per-page scopes, human-approved agent suggestions, and user credentials injected at tool execution.

- Techniques: Single linked markdown wiki with per-page scopes; Agent suggests, human accepts; Attribute every wiki change to a named human; Per-request user credential injection at the HTTP and SQL layer; Proxy and virtualize real-data access
- Tools: Claude Code, Slack, GitHub, OpenTelemetry, Opus 4.5, PromptQL, Hasura GraphQL engine

## [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents — Vasant Kearney, Onlay](../videos/UyyOoJmuATU.md)
`UyyOoJmuATU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: agent-architecture, evals, enterprise-adoption

Vasant Kearney (Onlay) argues healthcare agents should run on X12 insurance transactions as a public, strict contract that guardrails can reject, with tiered memory and skeptical use of models.

- Techniques: Standard-format tool contract; Strict guardrail rejection per step; Separated, tiered memory; Full-system regression evals before model swaps; Hybrid hard-coded and agentic execution; Write-action audit logging
- Tools: X12, FHIR, EHR, Claude Code, Codex, OpenClaw, Hermes Agent

## [The Last Human Code Review: Building Trust in AI-Generated Code — Itamar Friedman, Qodo](../videos/s-aixZYJG4c.md)
`s-aixZYJG4c` · AI Engineer · 2026-09-18 · q2 · practitioner · talk · also: pr-code-review, context-engineering, enterprise-adoption

Qodo's CEO argues human code review will become optional only once teams codify tribal knowledge into a context engine that serves both humans and agents, with per-rule analytics and graduated auto-approve/block.

- Techniques: Rule-linked review comments; Agent-directed PR summary comments; Per-rule analytics for review standards; Learning context from accept/reject history; Graduated auto-approve and auto-block; Service-contract graph for PR impact
- Tools: Qodo, Claude Code, AGENTS.md, CLAUDE.md

## [When AI Agents Pay and Sellers Monetize: Building x402 Apps on AWS — Anil Nadiminti, AWS](../videos/qTZirYu9pr0.md)
`qTZirYu9pr0` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: security-guardrails, infra-cost-scaling, mcp-and-tools

AWS walkthrough of letting AI agents pay for content via the x402 HTTP 402 protocol, with AgentCore Payments on the buy side and WAF bot pricing on the sell side. Mostly product pitch, with some useful architecture.

- Techniques: Payment session spend caps with expiry; Deterministic payment layer decoupled from the agent loop; Key custody behind KMS, with agent-level capability only; x402 request/402/pay/retry flow; Edge bot classification and differential pricing
- Tools: AgentCore Payments, Bedrock AgentCore Gateway, Bedrock AgentCore Runtime, AWS WAF, Amazon CloudFront, AWS KMS, x402, Coinbase wallets, Stripe wallets, Base (L2 chain)

## [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../videos/mJqwmmOx4WA.md)
`mJqwmmOx4WA` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: vibe-coding-app-building, coding-agents, product-ux

Andrew Garvin (Metronome, now part of Stripe) live-demos using Stripe Projects and a Metronome billing agent to build a usage-based billing setup from one natural-language prompt, arguing for sandboxed agent-built billing and for usage or credit pricing when agents are the users.

- Techniques: Portable skills files as agent context for a complex API; Verbose, machine-readable errors for agent self-correction; Sandbox-first agent-built billing with synthetic usage; Natural-language provisioning through a CLI orchestrator; Classify agent roles before designing pricing
- Tools: Stripe Projects, Stripe CLI, Metronome, Claude (selected as the coding agent in the demo), Vercel, Postgres, skills files

## [Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic](../videos/rbjWzZK2LU0.md)
`rbjWzZK2LU0` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: security-guardrails, coding-agents

Sachin Malhotra (Anthropic CI) on giving agents budgets instead of tokens: classify verbs by how they fail, cap every write with refilling rate limits, watch aggregates with tripwires, and take identity from infrastructure.

- Techniques: Verb triage by failure visibility; Break-glass verbs with proxy-stamped audit; Refilling per-write rate limits with scope-sized budgets; Bypass that asks the human inside agent sessions; Aggregate tripwires paired with context fixes; Undo test for sizing controls; Identity stamping at the proxy with inherited labels; Two-layer policy: text plus deterministic proxy
- Tools: Kubernetes, admission webhook, Slack, Claude Code

## [Mousepower: agents that can’t be measured, can’t be managed. — Maximillian Piras, Yutori](../videos/8KkibGU_DDY.md)
`8KkibGU_DDY` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: evals, token-cost-efficiency, product-ux

Maximillian Piras (Yutori) argues agents have a measurement problem: token spend must trace to verifiable outcomes, and tasks should be triaged by step and acceptance-criteria uncertainty before building an agent.

- Techniques: Two-axis task triage; Verifier agent alongside worker agent; Background parallel agents for peripheral work; Outcome-tied token accounting
- Tools: Claude

## [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents — Christopher Lovejoy & Saul Howard](../videos/mav15aW9lLM.md)
`mav15aW9lLM` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: enterprise-adoption, evals, security-guardrails

Christopher Lovejoy (Anthropic) and Saul Howard (Anterior) argue that enterprise AI agents need audit, data-boundary, escalation and eval primitives designed in from the start, not bolted onto a proof of concept.

- Techniques: Immutable append-only event log as system of record; Event log plus schema-driven immutable blob store; Token-based access at point of use; Human-agent equivalency in the action model; Replay plus human-vs-agent diff as eval; Run evals inside the customer environment

## [Agent Spending Without Controls — Rodrigo Coelho & Pranav Maheshwari, Edge & Node](../videos/ZyGMqdIpPoE.md)
`ZyGMqdIpPoE` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: security-guardrails, mcp-and-tools

Edge & Node's pitch for Ampersend, a payment and compliance layer letting agents pay for paid MCP tools and checkouts, with a sanctions-screening demo. Mostly product pitch.

- Techniques: Pre-authorization counterparty screening; Skill file as the payment-aware tool gateway; Per-call micropayment for paywalled endpoints; Prompt-level spend constraint
- Tools: x402, Shopify UCP, TRM (wallet screening), MCP, Claude Code, Claude Cowork, Ampersend, Exa, Firecrawl, Circle nano-payments

## [Beyond the Lethal Trifecta: Agentic Commerce on the Open Internet — David Levine, Kiduna Club](../videos/tE2z8-hqoLY.md)
`tE2z8-hqoLY` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: security-guardrails, multi-agent

Founder talk on the "lethal trifecta" (private data + untrusted content + actions) and a proposed fix: agents as identity-bearing members of legally registered, blockchain-verified organizations. Mostly a pitch for Kaduna Club.

- Techniques: Ally build sequence (inform, instruct, empower, enact, align); Scoped identity tokens for agents (JWT with claims); Decision markets for policy; Per-action audit trail back to a responsible principal
- Tools: OpenCloud (caption spelling; likely OpenClaw, an agent product that the speaker says blew up in January 2026), MOO / LambdaMOO (text-based virtual world the speaker used in 1993), MCP servers (cited as a way enterprises integrate agents), Slack, Salesforce, Notion, Telegram, Twitter, JWT, Vector database (generic, no product named), Blockchain (generic, no chain named), Polymarket (cited as an analogy for decision markets)

## [Which AI startups actually land enterprise contracts? — Brian Lewis, Millennium](../videos/7A65O-0lvKE.md)
`7A65O-0lvKE` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, security-guardrails, product-ux

A buyer at a hedge fund explains why most AI startup pilots fail: value, security, reliability and legal gaps, not model quality. He argues most AI-native work is unglamorous data, architecture and change management.

- Techniques: Enterprise-readiness intake checklist for vendors; Verify retention claims in a pilot, not on paper; Gate features by group and by release; Track documentation and terms as versioned artifacts; Set buyer-written success criteria and a 90-day plan that deploys into the buyer's own cloud; Build-versus-buy check on vendor pitches; Breach-response question as a red flag test

## [How America Turned Against the AI Industry?](../videos/xu-i-Zeu46s.md)
`xu-i-Zeu46s` · Kai Explains · 2026-09-02 · q2 · intro · other · also: infra-cost-scaling, product-ux

Kai Explains essay on why US public opinion turned against AI and data centers: broken promises, local costs, and water as the proxy grievance. Opinion piece, not a technical talk.

- Techniques: Tangible-unit framing for infrastructure costs; Treat stated concerns as evidence before explaining; Cost-locality check on advocacy
- Tools: ChatGPT

## [Claude is watermarking AI text: Everything you need to know](../videos/EWGDJqlYlA8.md)
`EWGDJqlYlA8` · Kai Explains · 2026-09-02 · q3 · practitioner · news · also: security-guardrails, models-research

Explainer on Anthropic's announced machine-readable watermarking of Claude text: the likely statistical mechanism, what it detects, how fragile it is, and why the EU AI Act is the trigger.

- Techniques: Keyed green-list token biasing (watermark generation, as described); Z-score detection on the green fraction; Base-rate check before acting on any detector; Robustness testing of provenance signals
- Tools: Claude, claude.ai, Claude API, Claude Code, Claude Cowork, Claude on AWS, Claude on Google Cloud, Claude on Microsoft Foundry, Gemini, GPT, EU AI Act (regulation, Article 50), Dipper study (paraphrase attack study)

## [Ox Alpha is Lying to You!](../videos/kFajz5bNO6M.md)
`kFajz5bNO6M` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: models-research, evals, security-guardrails

Kai investigates "Stealth Ox Alpha", a free OpenRouter model with no stated developer, using tokenizer offsets, error strings and a leaked system prompt; he concludes the evidence points to GLM but is unproven.

- Techniques: Tokenizer offset fingerprinting; Error-string matching; Temperature-zero output comparison; Controlled video token test; Report benchmark counts with intervals; Cost and time comparison on a fixed build task; Check retention claims at both the aggregator and the provider
- Tools: OpenRouter, OpenCode, GLM 5.3 (Zhipu), GLM-5, Gemini 2.5 Pro, GPT-4o, Claude Fable, Claude Code, Hermes Agent, DeepSeek Harness, Grok, DeepSeek

## [Claude Now Watermarks Its Text. How is it Possible?](../videos/cX0xI5FpH3U.md)
`cX0xI5FpH3U` · Kai Explains · 2026-09-02 · q4 · practitioner · news · also: security-guardrails, inference-serving, models-research

Kai Explains on how Anthropic's text watermark works (sampler-side, keyed tournament sampling, no added characters), why detection and spoofing numbers are unpublished, and what engineers should actually do about it.

- Techniques: Tournament sampling for keyed watermarks; Keyed detection by re-deriving scores; Provenance by drafts and version history; Control the mark by running an open-weight model locally; Check provider support for provenance metadata before relying on it; Avoid invisible-character and character-swap tricks
- Tools: Claude (Anthropic API), Claude 4.7 (sampling parameter restriction mentioned), SynthID-Text (Google DeepMind; transcribed as 'Synth ID text'), Gemini (DeepMind watermark user study), GPTZero (transcribed as 'GPT-0'), Pangram, Turnitin, Amazon Bedrock, Google Cloud, Microsoft Foundry, C2PA-style signed provenance metadata (transcribed as 'C2 Pascal'), Digits of pi (Anthropic's Monopoly analogy)

## [We Vetted 2000 AI Skills Before They Reached Developers — Lucas Palma, Nubank](../videos/iKQ78wyJEXU.md)
`iKQ78wyJEXU` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails, skills-self-improvement, pr-code-review

Nubank's product security team built SkillVector, a CI scanner that vets internal AI skills (hybrid regex plus LLM) before they reach an internal marketplace, and reports 2,000+ skills scanned.

- Techniques: Three-point skill scanning; Hybrid deterministic plus LLM review; Findings as PR comments plus SARIF; Historical back-scan; Verify approval gates, not model confirmations
- Tools: SkillVector (spoken as 'SkillVetor' in the transcript), SARIF, Regex-based determinstic scanners, LLM reviewer, Internal skills marketplace

## [Security Firewall for Agents — Ryan Dahl, Deno](../videos/MkRYPFIMCSA.md)
`MkRYPFIMCSA` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: security-guardrails, infra-cost-scaling

Ryan Dahl (Deno) on Claw Patrol, an open-source byte-level egress proxy that gates what production agents send to databases, Kubernetes and SaaS, with rules, credential injection and human or LLM approval.

- Techniques: Byte-level egress proxy for agents; Credential injection at the proxy; Policy-as-code in HCL with Git review; Chained verdicts: rule, LLM judge, then human approval; Network-level placement with existing identity
- Tools: OpenClaw, Claw Patrol, Deno Deploy, PostgreSQL, Kubernetes, ClickHouse, AWS (Sigv4), GitHub, Slack, PagerDuty, HCL, Terraform

## [Build for the Memo, Not the Demo — Shawn Chan, China Resources Holdings](../videos/tJFjeMBKbIY.md)
`tJFjeMBKbIY` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: product-ux, rag-retrieval

A finance investor argues AI products should be built as auditable memos, not impressive demos. He lists six ways trust breaks and five plumbing fixes: provenance, number agreement, surfaced contradictions, fact/guess labels and human approval.

- Techniques: Click-through provenance with source trust levels; Fact vs guess labelling; Automatic cross-document number reconciliation; Surface contradictions instead of resolving them silently; Locked human approval gate with audit log; Accountability-first architecture

## [Stop Renting Your Cognitive Infrastructure - Thiyagarajan Maruthavanan, Kalmantic Labs](../videos/Bck7ABCZRZI.md)
`Bck7ABCZRZI` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: token-cost-efficiency, local-ai, infra-cost-scaling

Thiyagarajan Maruthavanan (Kalmantic Labs) argues teams should rent inference to learn and own it to earn, using his own runaway-cost incident and enterprise objections to self-hosting as evidence.

- Techniques: Per-key spend monitoring with a cutoff; Input compression and context management in agent loops; Rent-to-own decision gate; Small local inference box for personal agents
- Tools: DGX Spark, Headroom, JustTokenMax, JustInfo, Suno, NemoClaw

## [AI’s Jurassic Park Period — Aaron Stanley, dbt Labs](../videos/1lgFGaHoGq8.md)
`1lgFGaHoGq8` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails, agent-architecture

Aaron Stanley (CISO, former forensic consultant) argues that agents routing around constraints is the hidden risk, and proposes a corrigible, four-layer defense: deterministic floor, halt-and-explain agent, adversary agent, and structured human escalation.

- Techniques: Halt-and-explain default for constraint conflicts; Equal-power adversary agent reviewing worker actions; Natural-language escalation to humans; Layered deterministic floor; Intercept at the harness or tool-call hook; Runtime input policies instead of output string matching
- Tools: gVisor, egress filters, Chrome extension (installation blocked by a layered control)

## [Full Workshop: Better Auth — Paola Estefania, Better Auth](../videos/JvKO40CFq-s.md)
`JvKO40CFq-s` · AI Engineer · 2026-08-18 · q3 · practitioner · workshop · also: security-guardrails, mcp-and-tools

Paola Estefania (Better Auth) argues agents should get their own identity and scoped capabilities instead of borrowing user credentials, and demos a draft open protocol with approvals, audit logs and revocation.

- Techniques: Per-agent identity with own key pair; Capability grants with default-read policy; Device-flow approval for agents; OpenAPI-to-capability translation; Full revocation: agent, host and tokens
- Tools: MCP, OAuth, OpenAPI, OIDC, Gmail, Notion, Claude, Cursor

## [Privacy-Preserving Intelligence — Steve Korshakov, Bee (acq. Amazon)](../videos/IvE8n-ylFYY.md)
`IvE8n-ylFYY` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails, sandboxing-execution, agent-architecture

Steve Korshakov (Bee, acquired by Amazon) explains how an always-on personal-agent wearable keeps data unreadable even to its own company, using client-held keys, attested workloads, and two-tier release controls.

- Techniques: Client-held keys with attested key release; Forced key expiry window; Split base image and deployment manifest; Private CA for internal attestation certificates; Minimal, auditable trusted code base; Per-agent sandbox with minimal capabilities
- Tools: Sigstore-style transparency log (auto-caption reads as 'six store'), Confidential compute nodes, Private certificate authority, OpenClaw (auto-caption reads as 'open claw'), Claude Code (auto-caption reads as 'cloud code')

## [Local Models: Trust, Control, Optimization — Carter Abdallah, NVIDIA](../videos/FWMJQDH3iK0.md)
`FWMJQDH3iK0` · AI Engineer · 2026-08-18 · q3 · practitioner · panel · also: local-ai, training-finetuning-rl, models-research

A panel from NVIDIA, Prime Intellect and Arcee argues open-weight models give trust, cost control and data ownership, and that post-training them on your own harness and traces beats generalist frontier APIs for narrow work.

- Techniques: Harness-specific post-training of an open base model; RL environment, then deploy, then train on production traces; Trace capture as a fine-tuning dataset; Specialize a small model to one or two tasks; Verify open weights and inference code before trusting them
- Tools: vLLM, SGLang, PrimeRL, NeMo RL, NeMo Gym (captioned as 'Nemo Jim'), verifiers, Hugging Face, Nemotron, Trinity (Arcee model), Hermes (harness), Pi (harness), OpenMDW license

## [How Kepler Built Verifiable AI for Financial Services — Vinoo Ganesh](../videos/Tt2kX2sgQio.md)
`Tt2kX2sgQio` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: data-engineering, enterprise-adoption, agent-architecture

Kepler's CEO argues finance AI needs a deterministic substrate: the model points to sources and decides what to compute, while code extracts, checks and calculates numbers, with replayable derivation chains.

- Techniques: Atomic provenance ledger; Model decides, code computes; Derivation chains for derived metrics; Deterministic sanity gate on model output
- Tools: Claude, XBRL, ChatGPT, GLM 5.2, Opus 4.8

## [Guide, Verify, Solve — Anirban Chatterjee, Sonar](../videos/03l29gJXpCE.md)
`03l29gJXpCE` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: testing-verification, pr-code-review, coding-agents

Sonar's product marketer argues AI-written code needs zero-trust, multilayered verification inside agent loops and in CI/CD, framed as a Guide-Verify-Solve (ACDC) cycle, with vendor product pitches throughout.

- Techniques: In-loop verifier callback with fix-and-rerun; Task-scoped context retrieval for agents; Machine-enforced quality rulebook; Dual PR gate: LLM review plus deterministic scan; Cross-model or cross-method review; Graduated automation of review bots; Remediation agent for backlog debt; Per-task model choice from a quality profile
- Tools: SonarQube, Sonar Vortex, Guitar (AI code-review tool, name from captions), Cursor, Claude Code, Codex, Antigravity

## [You Didn't Ship a Bug. You Just Wrote It for a Human. - Ravi Madabhushi, Scalekit](../videos/lMCxVorb9wM.md)
`lMCxVorb9wM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails, mcp-and-tools

Ravi Madabhushi (Scalekit) argues agents break the human and service-account identity model: they need a distinct identity bound to a principal, fine-grained time-bound scopes, and full action audit, beyond OAuth.

- Techniques: Coalesce high-frequency timestamp writes; Bind agent identity to principal; Context-filtered MCP tool surface; Least-privilege, time-bound, just-in-time grants; Full-provenance action audit
- Tools: OAuth, SPIFFE, MCP, Gmail API, Salesforce API, Databricks, HubSpot, Notion

## [Can Oncology Workflows Run Without Human Touch? - Anant Shankhdhar, Risa Labs](../videos/_cVfz88_j7A.md)
`_cVfz88_j7A` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: agent-architecture, data-engineering

Risa Labs (oncology) walks through automating prior-authorization workflows end to end, using confidence-gated multi-agent routing so only some orders skip human review.

- Techniques: Deterministic-first gating before LLM steps; Corroboration across independent sources before automating; Confidence-gated escalation to humans; Evidence-structured questionnaire answering; LLM-generated integration configs from a reusable action library; Self-healing loop for production automations
- Tools: RPA (robotic process automation, unnamed product), SQL database (unnamed), LLM (unnamed model) for extraction and config generation, Patient biomarker graph (internal, unnamed)

## [Skills are new features: Building Skill-Centric Harness — Yogendra Miraje, FactSet](../videos/7jjudsEhBtM.md)
`7jjudsEhBtM` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: skills-self-improvement, agent-architecture, context-engineering

FactSet's principal AI engineer argues skills are the new product features and engineers should ship harnesses, then covers a minimal skill harness, routing via descriptions, eval-gated skills, and skill-library governance.

- Techniques: Minimal skill registry and loop; Write descriptions as routing signals; Cut skills by user intent; Front-load critical instructions and re-run evals on model upgrades; Shortlist skills before they hit the system prompt; Governance as a skill PR pipeline
- Tools: Anthropic Agent Skills (SKILL.md format), Claude Code, Codex, bash or code sandbox for skill scripts

## [Your LLM Stack Is a 2008 Database With Better Marketing — Lovina Dmello, NVIDIA](../videos/XjI-AR4pt7Y.md)
`XjI-AR4pt7Y` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: security-guardrails, infra-cost-scaling

Production ML breaches are mostly boring misconfigurations, not AI attacks; the talk argues for layered infra security, a maturity model, and budgeting guardrails by latency overhead tier.

- Techniques: Tiered guardrail budget; Maturity self-assessment with overhead budgets; Least privilege with short-lived credentials; Segment by service identity, not network location; Secrets and model artifacts hygiene; Treat ML infra like a database
- Tools: Ray, NIST AI RMF

## [It's 10pm. Do You Know Where Your Agents Are? — Kim Maida, Keycard](../videos/I3znWC3MEXM.md)
`I3znWC3MEXM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails, mcp-and-tools, agent-architecture

Kim Maida (Keycard) shows why API keys give agents overprivileged, unattributed access, and how OAuth token exchange (RFC 8693) per tool call, with policy checked before minting, fixes it.

- Techniques: Per-tool-call token exchange (RFC 8693); Policy-before-mint; Policy-gated human approval; Ephemeral, audience-bound bearer tokens; Layered scope design
- Tools: Keycard (security token service and policy governance), OAuth 2.0 token exchange (RFC 8693), Google sign-in (identity provider in demo), MCP (client, server, gateway)

## [Citation Needed: Provenance for LLM-Built Knowledge Graphs — Daniel Chalef, Zep AI](../videos/H7puB0RwJMM.md)
`H7puB0RwJMM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: memory, data-engineering

Daniel Chalef (Zep) on why LLM-built knowledge graphs need provenance modeled as a graph, covering lineage through merges, contradictions, tagging, and deletion.

- Techniques: Provenance as graph edges; Merge-safe lineage; Ingestion-time tagging with inheritance; Lineage-based deletion; Single-shot extraction plus deterministic dedupe
- Tools: Graphiti, Zep, Vector similarity search, Full-text search, BFS graph traversal

## [Your Finance Agent's Bottleneck Is You — Ramana Siddanth Emani, Auditoria AI](../videos/z0sh8HyTrDo.md)
`z0sh8HyTrDo` · AI Engineer · 2026-08-18 · q2 · practitioner · talk · also: software-factory, multi-agent, coding-agents

Auditoria AI speaker says human attention bottlenecks agent work: use parallel worktree subagents, skills, one-pane UX, goals and loops, and self-improving harnesses, keeping humans at intake and sign-off.

- Techniques: Worktree-per-task parallel subagents; Ticket-to-stage pipeline with two human gates; Encode organizational procedure as skills; Single-pane minimal UX for orchestration; Daily self-retrospective on the agent's own loop; Goals plus loops, monitored from a phone; Background dreaming for pattern compaction
- Tools: Claude Code, git worktrees, Kubernetes, Docker, Jira, GitHub, MCP

## [Grok Was Caught Uploading Your Entire Codebase](../videos/n6DIs13ilvU.md)
`n6DIs13ilvU` · Better Stack · 2026-08-02 · q3 · intro · news · also: security-guardrails, coding-agents

Better Stack summarizes reports that Grok's coding CLI uploaded whole repos, git history and env vars to xAI, what xAI changed afterward, and why the /privacy toggle is not real local protection.

- Techniques: Audit a CLI's uploads with a MITM proxy; Grep CLI logs for upload sessions; Rotate secrets if an upload is confirmed; Harden the CLI config and verify the flags
- Tools: Grok CLI (Grok Build), xAI API / account settings, MITM proxy, Claude Code, Codex, Gemini CLI

## [Grok 4.5 Was Trained on YOUR Cursor Sessions (What SpaceX Isn't Telling You)](../videos/hdWUv2V1jRg.md)
`hdWUv2V1jRg` · Kai Explains · 2026-08-02 · q3 · intro · news · also: security-guardrails, models-research, coding-agents

Commentary arguing Grok 4.5 was partly trained on Cursor user sessions captured while privacy mode was off by default, and that behavioral coding data is now the valuable asset.

- Techniques: Audit training and privacy settings in each AI coding tool; Treat codebase-derived vendor benchmarks as possibly contaminated; Scan launch posts for buried data-use disclosures
- Tools: Cursor, Grok 4.5, CursorBench, SWE-Bench Pro (transcribed as "WE Bench Pro"), Terminal Bench 2.1, Fable (model, as named in transcript), Opus 4.8, Opus 4.7, GPT 5.5

## [Agents Need Feature Flags - Sachin Gupta](../videos/zU4EagB311U.md)
`zU4EagB311U` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: security-guardrails, agent-architecture

Sachin Gupta argues agents need feature-flag discipline: six flag types (prompt, tool, model, memory, autonomy, kill switch), a middleware layer, and a kill switch shipped first, with four metrics to track.

- Techniques: Six-surface flag taxonomy; Flag middleware between user and agent loop; Kill switch with three properties; Canary prompt variant; Five-step rollout order; Resolve flags per turn and log segment context; Bypass caching for flag-sensitive responses; Flag hygiene rules
- Tools: LaunchDarkly, Unleash, Lift (as spoken), homegrown flag service

## [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](../videos/ObTPqBGsEbA.md)
`ObTPqBGsEbA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: evals, observability, enterprise-adoption

A five-pillar playbook (evaluation, tracing, data foundation, orchestration, governance) for taking enterprise AI agents to production, illustrated with a retail banking chatbot case study.

- Techniques: Business-metric eval spec before build; Living golden eval set seeded from human answers; Three-layer eval stack; Automated eval pipeline with human review threshold; Trace-driven duplicate-call detection and retry cap; Tiered CI eval runs; Prompt versioning as change management; Model selection on your own eval set; Incident playbook: detect, diagnose, contain, fix, regress
- Tools: Databricks, MLflow, Delta Lake, Apache Spark, Unity Catalog, Genie, Agent Bricks, Databricks Apps, Mosaic AI, Git, Python, LLM-as-judge

## [ReviewDebt: a practical framework for scoring every pull request — Sachin Gupta, Ebay](../videos/TJPInBjhE4Q.md)
`TJPInBjhE4Q` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: pr-code-review, coding-agents, evals

Sachin Gupta (eBay) argues coding agents create unmeasured review debt and offers a deterministic 0-100 PR review-burden score built from five signal families, plus a rollout plan.

- Techniques: Deterministic review-burden score; Backfill calibration; Non-blocking rollout ladder; Shape rules for agent PRs; Authorship detection as a weak amplifier
- Tools: GitHub, GitHub Copilot, Codex, Cursor

## [The AI bugpocalypse is here. Now what? - Jack Cable, Corridor](../videos/7JgIS42mz7U.md)
`7JgIS42mz7U` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: security-guardrails, pr-code-review, models-research

Jack Cable (Corridor, ex-CISA) argues frontier models now find and exploit vulnerabilities at scale, but the bug classes are old and preventable, so rewrite toward memory safety and add guardrails before the PR for AI-written code.

- Techniques: Rewrite critical components in a memory-safe language; Pre-PR guardrails and visibility for agent-written code; Give the reviewer business and threat context; Use defenders' frontier models to harden systems
- Tools: Claude Code, Cursor, Rust, Slack, BaxBench

## [AI-Driven Multi-Document Correlation for Financial Compliance - Varsha Shah, Independent](../videos/Iwe_RY-fYgI.md)
`Iwe_RY-fYgI` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: data-engineering, enterprise-adoption

Varsha Shah proposes a framework that correlates records across payroll, tax, procurement and finance systems with graph-based entity linking, adaptive risk scoring and jurisdiction normalization to catch compliance fraud that per-document checks miss.

- Techniques: Cross-document entity graph for compliance; Multi-signal risk scoring instead of single rules; Outcome feedback loop; Normalize before scoring across jurisdictions

## [Respect The Process - Andrew Dumit, Watershed Technology Inc.](../videos/CLttOU7n6sI.md)
`CLttOU7n6sI` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: coding-agents, testing-verification, sandboxing-execution

Andrew Dumit (Watershed) on deploying coding agents for sustainability supply-chain graph edits: constrain the effects through a typed SDK and deterministic execution, not the agent's reasoning, so the process can be validated.

- Techniques: Typed SDK as the only write path; Deterministic run executor (validate-then-commit); Review artifact instead of code review; Constrain effects, not reasoning; Eval-driven hill-climbing on the agent task
- Tools: Claude Code, TypeScript SDK, React agent (earlier version)

## [Build AI Systems for Discernment, Not Approval - Angel Ortmann Lee, Duolingo](../videos/CDqzWpwkSls.md)
`CDqzWpwkSls` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: product-ux, evals

Duolingo shows skilled reviewers accepted half of fake AI cheating flags; guidelines demanding independent evidence raised rejections 21%. Design human-in-the-loop interactions for discernment, not approval.

- Techniques: Calibration test with planted false signals; Reframe the AI output as a preliminary alert; Split compound questions into separate signals; Inline anchored feedback instead of a long essay; Surface assumptions and trade-offs for sign-off in agent plans; Capture the edit diff as the training signal; Log the questions users ask as a trust signal

## ["The engineer of the future is the person who chooses what is worth doing." — Addy Osmani, Anthropic](../videos/n97BCfyFIvw.md)
`n97BCfyFIvw` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: software-factory, pr-code-review, product-ux

Addy Osmani argues engineers are defined by owning the verdict on agent work: choosing what is worth doing, backing it with evidence, and accepting accountability. Keep humans at the highest-leverage checkpoint.

- Techniques: Inner loop / outer loop split; Evidence bundle as the review unit; Explain-it-or-don't-ship gate with named owners; Review as a control system for long runs; Move verification into the harness; Clean code for agents as well as humans
- Tools: Git

## [Claude Mythos is FINALLY here (Fable 5)](../videos/Ubazoyagym0.md)
`Ubazoyagym0` · Better Stack · 2026-07-02 · q2 · intro · news · also: models-research, coding-agents, token-cost-efficiency

Anthropic's Fable 5, a safeguarded Mythos-class model: vendor benchmarks, a one-shot UI test, steep pricing, plan-limit burn, and a 30-day retention requirement. Mostly a reaction to launch claims.

- Techniques: Same-prompt side-by-side model comparison; Screenshot-to-site cloning
- Tools: Fable 5 (Anthropic model, Mythos class), Claude Mythos, Opus 4.8, GPT 5.5 (OpenAI), SWE-Bench Pro, Frontier Code (Cognition benchmark), Terminal Bench, Devin (referenced as Cognition product), Claude Max, Team and Enterprise plans

## [BREAKING: US Government BANNED Mythos and Fable](../videos/Q5_e2v7WZEQ.md)
`Q5_e2v7WZEQ` · Better Stack · 2026-07-02 · q2 · intro · news · also: security-guardrails, models-research

Better Stack breaking-news reaction to a reported US export-control directive that suspended Fable 5 and Mythos 5 access for foreign nationals, with Anthropic's response read out and the speaker's speculation.
- Tools: Fable 5, Mythos 5, GPT 5.5 (OpenAI, named by Anthropic as having similar capability)

## [Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe](../videos/KLSuFPj2ld0.md)
`KLSuFPj2ld0` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: security-guardrails, mcp-and-tools

Stripe's Steve Kaliski on letting agents spend safely: scope shared payment tokens to amount, time and seller, use HTTP 402 for paid tools, and keep discovery non-deterministic while payments stay deterministic.

- Techniques: Seller-scoped delegated payment credential; Deterministic transaction layer behind a non-deterministic planner; HTTP 402 pay-per-call; Round-trip checkout state; Forward risk signals to the counterparty
- Tools: Stripe shared payment tokens, Stripe Payment Intents, Stripe Issuing, Machine payments protocol (with Tempo), Agentic Commerce Protocol (with OpenAI), curl (demo), Tempo blockchain (pathUSD), Base

## [Sovereign Escape Velocity: Ownership w Open Models — Gus Martins, & Ian Ballantyne, Google DeepMind](../videos/SS-A8sE7hkw.md)
`SS-A8sE7hkw` · AI Engineer · 2026-06-18 · q2 · intro · talk · also: local-ai, models-research, inference-serving

Google DeepMind's Gemma team pitches open-weight Gemma 4 models (E2B to 31B) as a way to own, customize and run models locally, with on-device and single-GPU demos.

- Techniques: Drop-in local endpoint swap; Local sub-agent fan-out for batch work; Threshold-based task routing; Latency-class scheduling for on-device tasks; Own-eval-first model adoption
- Tools: Gemma 4, Gemini, Google AI Edge Gallery, LM Studio, Ollama, MedGemma, OpenRouter, LM Arena

## [What if the network was the sandbox? — Remy Guercio, Tailscale](../videos/BM2JX9hqsVQ.md)
`BM2JX9hqsVQ` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: sandboxing-execution, security-guardrails, observability

Tailscale's Remy Guercio argues the network layer can act as an agent sandbox: identity-tagged WireGuard connections let an LLM gateway hold the provider key so the sandbox never has one, and every model call and tool call is visible and cuttable there.

- Techniques: Zero-key sandbox behind an identity-aware gateway; Per-identity budgets and quotas across providers; Per-tool-call webhooks for external policy; Identity-aware internal services with tsnet; Policy as code for network identity
- Tools: Tailscale, WireGuard, Aperture, tsnet, Claude Code, Codex, Gemini CLI, GitHub Actions, Opus 4.6

## [What Breaks When You Build AI Under Sovereignty Constraints - Bilge Yücel, deepset GmbH](../videos/x2bH0RKPgdc.md)
`x2bH0RKPgdc` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: security-guardrails, mcp-and-tools, observability

Bilge Yücel (deepset) on building AI under sovereignty constraints: four pillars, what breaks when you move from frontier APIs to self-hosted, and a guardrail-agent-guardrail reference design built on Haystack.

- Techniques: Sovereignty checklist as a design gate; Safe/unsafe router as an input guardrail; Per-agent tool allowlist plus BM25 tool search; Per-tool human confirmation strategies; Pipeline serialized to YAML for version control; Tracer component wrapping the pipeline
- Tools: Haystack, MCP, BM25, OpenTelemetry, YAML, Kubernetes, Mistral, Google models, Nvidia models, Jina

## [Most Enterprise Agentic Projects Are Doomed, Here's Why — Jess Grogan-Avignon & Jack Wang, Accenture](../videos/AGkzpxMdPn8.md)
`AGkzpxMdPn8` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: enterprise-adoption, product-ux

Accenture talk on why enterprise agentic projects stall: human-speed governance, business cases, and trust. Argues for hypothesis-driven delivery, portfolio funding, progressive autonomy, and feedback loops as the moat.

- Techniques: Exposure ladder for agent rollout; Approval-as-code; Hypothesis-driven agent delivery; Portfolio funding for AI bets; Kill switches and hard limits on autonomous actions; Instrument every feature as a feedback source

## [Rewiring the State — Eoin Mulgrew, No. 10 (Downing Street)](../videos/ObNKGf9YR0g.md)
`ObNKGf9YR0g` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: enterprise-adoption, product-ux, evals

Eoin Mulgrew of No. 10's data science team describes an outsider "insurgency" unit with forward-deployed engineers that ships small government AI tools in weeks; mostly a recruitment pitch.

- Techniques: Insurgency unit with a mandate; Forward-deployed engineers embedded in workflows; Internal tool instead of outsourced one-off analysis; Policy simulation sandbox; Pre-deployment sycophancy red-teaming and user coaching; Benchmark-based guardrails for classroom AI
- Tools: Gemini, Inspect (AI Safety Institute evaluation tool), Xtract (planning-application digitisation)

## [Deno Just Open Sourced Their Agent Firewall (Claw Patrol)](../videos/ZiFoTw6doGI.md)
`ZiFoTw6doGI` · Better Stack · 2026-06-02 · q3 · intro · review · also: security-guardrails, infra-cost-scaling

Walkthrough of Claw Patrol, an open-source agent firewall from the Deno team: a gateway injects real credentials into agent requests, enforces per-action rules, and logs every request.

- Tools: Claw Patrol (Deno, open source), Deno, Tailscale, WireGuard, OpenClaw, Claude (Claude Code CLI; transcript spells it "Clawed"), Codex, Postgres, ClickHouse, Slack, GitHub, Kubernetes

## [Why Anthropic Banned Every Third-Party Claude Tool](../videos/Fl6QT86n1P4.md)
`Fl6QT86n1P4` · Better Stack · 2026-06-02 · q3 · practitioner · news · also: token-cost-efficiency, claude-code

Better Stack on Anthropic's Programmatic Credits (opt-in from June 15): subscription use of the Agent SDK and claude -p moves to API-rate credits, after earlier blocks on third-party harnesses. The speaker reads it as vendor lock-in.

- Techniques: Move recurring automation to first-party surfaces such as routines and official connectors; Estimate programmatic spend at API rates before running a loop on a subscription
- Tools: Claude Code, Claude Agent SDK, claude -p (headless CLI mode), Claude routines, Remote control (Claude feature), Managed agents (Claude feature), Opus 4.7, Sandcastle, T3 Code, Zed, OpenCode, OpenClaw

## [Gateways are All You Need — Karan Sampath, Anthropic](../videos/CD6R4Wf3jnY.md)
`CD6R4Wf3jnY` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: mcp-and-tools, security-guardrails, infra-cost-scaling

Anthropic forward-deployed engineer Karan Sampath argues enterprises should put one gateway in front of all MCP servers for auth, access control, observability and credentials, so teams build only business logic.

- Tools: MCP, Claude Code, Claude Agent SDK, claude.ai, Claude managed agents

## [Mastering AI Pricing — Mayank Pant, Stripe](../videos/CrqPcIZOOXA.md)
`CrqPcIZOOXA` · AI Engineer · 2026-05-18 · q3 · intro · talk · also: product-ux, infra-cost-scaling

Stripe's billing architect on AI pricing: treat the first price as a hypothesis, use base-plus-usage hybrid pricing with credits, add usage guardrails, and choose billing infrastructure that lets you change prices quickly.

- Techniques: Credit abstraction layer; Base fee plus usage fee (hybrid); Usage guardrail stack; Value-to-metric mapping; Grandfathered pricing versions; Per-event rating with explainable invoices
- Tools: Stripe Billing, Metronome

## [How AI is changing Software Engineering: A Conversation with Gergely Orosz, @The Pragmatic Engineer](../videos/CS5Cmz5FssI.md)
`CS5Cmz5FssI` · AI Engineer · 2026-05-18 · q3 · practitioner · interview · also: enterprise-adoption, coding-agents, infra-cost-scaling

Gergely Orosz (Pragmatic Engineer) on "token maxing": how usage leaderboards get gamed, why individual gains do not yet show up as team gains, and why big companies build their own agent infrastructure.

- Techniques: Enable non-engineers to build with coding agents; Keep agent count small and treat orchestration like tech lead mentoring; Single MCP gateway tied to service discovery; Risk-tiered code review for agent-written changes; Trade early access for structured feedback
- Tools: Claude Code, Cursor, GitHub Copilot, MCP gateway

## [Someone Cheated at Roblox and Broke Vercel](../videos/nnzH0eaAFa8.md)
`nnzH0eaAFa8` · Better Stack · 2026-05-02 · q3 · intro · news · also: security-guardrails

A news explainer on how a Roblox cheat download on a Context.ai employee's laptop led to a breach of Vercel, with the lesson that over-permissioned OAuth tokens and non-sensitive env vars made the blast radius large.

- Techniques: Audit OAuth grants for third-party apps; Rotate secrets at the source after a platform compromise; Mark env vars as sensitive for hosted platforms; Least-privilege grants for AI tools on corporate accounts; Treat OAuth tokens as credentials
- Tools: Vercel, Context.ai (AI Office Suite), Google Workspace, Roblox, Luma Stealer, Amazon Web Services, Linear, Supabase, Datadog, AuthKit, Next.js, Turbopack

## [Age Verification Is Coming For Linux...](../videos/TbLLYN4ftnY.md)
`TbLLYN4ftnY` · Better Stack · 2026-04-02 · q2 · intro · news · also: dev-tools

Better Stack commentary on California's Digital Age Assurance Act, which would make OS providers collect age brackets and expose them to apps, and why the speaker thinks Linux distros are caught in its scope.

- Techniques: Minimal-disclosure age signal over D-Bus (proposal)
- Tools: D-Bus, apt, Homebrew, Ubuntu, Debian, Arch Linux, Fedora, MidnightBSD, Kicksecure, Whonix

## [Anthropic's Latest Move: Why OpenCode Users Are Worried](../videos/vLecpJt_8jM.md)
`vLecpJt_8jM` · Better Stack · 2026-02-02 · q2 · intro · news · also: coding-agents, claude-code, token-cost-efficiency

Speaker reports Anthropic restricting Claude Pro/Max subscriptions to Claude Code, hitting third-party agents like OpenCode, and describes a temporary tool-name workaround. Mostly speculation.

- Techniques: Keep the harness model-agnostic and route each workflow to a cheaper or better model; Use subscription quota first, then fall back to API billing; Tool-name prefix workaround reported by OpenCode (unverified; the speaker says it is temporary)
- Tools: Claude Code, Claude Pro, Claude Max, Claude Opus 4.5, OpenCode, OpenCode Black, OpenCode TUI, ClaudeBot, Ralph loop, npm, GitHub, OpenAI models

## [Something’s Off About Anthropic’s “AI-Orchestrated Attack” Story (Report Analysis)](../videos/BF7abVHg-WI.md)
`BF7abVHg-WI` · Better Stack · 2025-12-02 · q2 · intro · review · also: security-guardrails

Better Stack critiques Anthropic's report on an "AI-orchestrated" espionage campaign as vague and marketing-driven, and argues threat reports need TTPs, IOCs and named tools.

- Techniques: Vendor threat-report credibility checklist
- Tools: Claude Code, Claude

## [Unmasking hidden costs of microservices with Vojtech Vondra](../videos/nw2oVC3ycd4.md)
`nw2oVC3ycd4` · Better Stack · 2024-11-02 · q3 · practitioner · talk · also: infra-cost-scaling

A Microsoft identity engineer argues microservices carry hidden costs that multiply with each service, and that teams should stay small (about five services) unless they are very large.

- Techniques: Count n before splitting into services; Cross-cutting concerns checklist; Design interfaces and communication first; Measure boilerplate ratio
- Tools: Azure

