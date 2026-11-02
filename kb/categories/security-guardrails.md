# security-guardrails — 243 videos

*prompt injection, agent security, guardrails, PII, identity / auth for agents*

By channel: AI Engineer 141 · Kai Explains 14 · AI LABS 13 · Better Stack 75

**Synthesized guide:** [guides/security-guardrails.md](../guides/security-guardrails.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [This Gateway Makes Claude Code 30% Cheaper (Context Mode)](../videos/Afm-GNrJbEQ.md)
`Afm-GNrJbEQ` · Better Stack · 2026-11-01 · q3 · practitioner · review · also: token-cost-efficiency, claude-code, infra-cost-scaling

Better Stack tests Context Mode's hosted Claude Code gateway: same answers, about 31% lower cost on log-heavy sessions, a command firewall, but all prompts pass through vendor servers.

- Techniques: Route Claude Code through a proxy gateway by base URL; Fold bulky tool output and keep an archive; Command-rule firewall with a preset; Side-by-side cost benchmark for a proxy or optimizer
- Tools: Claude Code, Context Mode gateway (hosted), Context Mode open-source plugin, Anthropic API, Claude Max plan, Opus 5.5 (as named in the video), NASA Kennedy Space Center web server logs, July 1995 (test data)

## [Everyone Has the Same AI Models. Here's What Sets Agents Apart - Richmond Alake, Oracle](../videos/1_lX0m64-aI.md)
`1_lX0m64-aI` · AI Engineer · 2026-11-01 · q2 · intro · talk · also: memory, agent-architecture, rag-retrieval

Oracle's Richmond Alake argues agents need an "intelligence plane" (knowledge, memory, access governance, continual learning) beyond the control plane, illustrated with Oracle product demos.

- Techniques: Memory routing with a small fine-tuned decision model; Capture memory traces as fine-tuning data; Ontology and semantic layer in front of retrieval; Propagate user identity into data access; Private inference container for on-prem embeddings, LLM and rerankers
- Tools: Oracle AI Database, Oracle agent memory Python package (generates context cards), Oracle Deep Data Security, Oracle Private AI Services Container, Oracle Cloud (hosted Grok and OpenAI models), Private Agent Factory (no-code agent builder on Oracle AI Database), Memories (open-source agent memory tool built by the speaker), Qwen (fine-tuned as memory-routing decision model)

## [Someone Hid a Trap for AI in This File (DeepSeek Wasn't Fooled)](../videos/ROW6KbSE1Ew.md)
`ROW6KbSE1Ew` · Better Stack · 2026-11-01 · q3 · practitioner · news · also: models-research

Attackers hide refusal-triggering text in scripts to stop AI analysis; closed models refused, open models didn't. Defenders reuse it as canary "context bombs" that halt attacking agents.

- Techniques: Canary context bomb; Treat a model refusal as a signal on untrusted input; Fallback to a self-hosted open-weight model for security analysis; Cross-model refusal test on hostile samples
- Tools: Claude Opus 5.5, Fable 5.1, Claude Opus 4.8, GPT-6 Astra, OpenAI Daybreak Blue, OpenAI Daybreak Red, DeepSeek, GLM 5.3, GLM 5.2, Kimi (transcribed as 'Kimmy'), canary tokens (Tracebit canaries)

## [Your AI Agent Wants Your Data. Here's How to Lock It Down - Jeff Smith, Oracle](../videos/LnQce-eHm8k.md)
`LnQce-eHm8k` · AI Engineer · 2026-11-01 · q3 · practitioner · review · also: mcp-and-tools, data-engineering, context-engineering

Oracle's Jeff Smith on locking down agent access to databases: expose curated reports as MCP tools instead of raw NL-to-SQL, give agents a compact schema tool, and enforce identity-based row and column security inside the database.

- Techniques: Curated report catalogue exposed through two MCP tools; Three server modes: ad hoc SQL, custom tools and reports only, or both; Reveal report SQL to agents under a privileged scope; Action-grouped tools instead of single-purpose tools; Compressed deterministic schema-info tool; Generate schema annotations from enterprise documents; Identity-driven row and column filtering at the database; Diagnose production performance on a read-only standby
- Tools: Oracle AI Database, Oracle MCP server, MCP (Model Context Protocol), MCP apps (spec feature, speaker says added to the spec in July; Oracle plans a GUI for later this year), Claude, Codex, Gemini, LangChain, Azure Entra ID (spoken as 'Azure IntraID'), Oracle Data Guard, AWR (Automatic Workload Repository, Oracle performance report), Confluence

## [How to Decide What Your AI Agent Should Remember - Wojciech Pluta, Oracle](../videos/qq2Hm4XNRgI.md)
`qq2Hm4XNRgI` · AI Engineer · 2026-10-31 · q2 · intro · talk · also: memory, context-engineering, agent-architecture

Oracle's Wojciech Pluta argues agent memory is a write path that needs a promotion gate with provenance, scoped memory tiers, and per-turn context cards. Vendor talk with a demo.

- Techniques: Memory promotion gate; Provenance plus supersede, not overwrite; Three-tier memory scoping; Per-turn context card; Enforce user isolation in the database layer
- Tools: Oracle AI Database, Oracle agent memory package (named as an early-year release; no version given)

## [Your AI Agent Starts Every Session Like a New Hire - Killian Carlsen-Phelan, Sonar](../videos/8vDzncmzxyg.md)
`8vDzncmzxyg` · AI Engineer · 2026-10-31 · q2 · practitioner · talk · also: coding-agents, testing-verification, context-engineering

Sonar pitches Vortex, a plugin that gives coding agents project context before they write and runs deterministic checks on every edit, so issues are caught before PR review.

- Techniques: Pre-write context retrieval from a verifier; Per-edit plus end-of-turn verification hooks; Enforce on changed lines only, surface the rest; Explicit-permission rule for sensitive resources; Deterministic layer between AI reviews
- Tools: Sonar Vortex (Sonar's agent plugin, named in the talk), SonarQube (static analysis, CI scan, data-flow and security analysis), Sonar CLI and MCP clients, Claude Code, Codex, Antigravity, Guitar (Sonar's AI reviewer, named in the captions; the speaker did not cover it), Java (language guidelines used in the demo)

## [Your Agent Just Paid for Nothing: 6 Attacks on x402 Payments - Ishween Kaur, SoFi](../videos/YU1uD_YkpjU.md)
`YU1uD_YkpjU` · AI Engineer · 2026-10-30 · q3 · practitioner · talk · also: governance-compliance, observability

Ishveen Kaur (SoFi) walks through six ways an autonomous agent can lose money on x402 machine payments, with guards, a probation-list pattern, and a trace-one-payment-ID method for finding them.

- Techniques: Compare listed price against 402 quoted price, network and wallet before paying; Shared payment-number ledger on the seller side; Buyer retries reuse one payment number; Choose release timing by data cost; Paywall test across all endpoints and no-store caching for paid output; Allow list, block list and probation list for discovered sellers; Per-plan call cap against prompt injection; Single-ID tracing with a 20-25 case dataset
- Tools: x402 (HTTP 402 payment protocol), Llama 3.2 (agent model in the prompt-injection demo), Base Sepolia testnet (auto-caption reads 'Bayes Cipolia'; probably Base Sepolia), x402.org facilitator (testnet), Bazaar (x402 seller directory), Ethereum and Solana (named as alternative chains), Cloudflare pay-per-crawl (cited as a parallel)

## [Why Docker Isn't Enough for AI Coding Agents (Openshell)](../videos/SbwckhZkPGs.md)
`SbwckhZkPGs` · Better Stack · 2026-10-29 · q4 · practitioner · review · also: sandboxing-execution, coding-agents

Josh from Better Stack demos NVIDIA's open-source OpenShell agent sandbox, which adds per-request, per-binary policy, supervisor-side credential injection and audit logs on top of containers, then lists its caveats.

- Techniques: Default-deny egress with live, narrow allow rules; Bind network permissions to the calling binary; Supervisor-side credential injection; Check policy diffs with a solver before applying; macOS preflight for OpenShell
- Tools: OpenShell (NVIDIA, Apache 2.0, Rust, self-hosted; ~20k GitHub stars at time of video), openshell CLI (`openshell policy update`, `openshell logs`, sandbox status, doctor), Docker / Docker Desktop, Podman, Kubernetes, Firecracker, Apple container, Anthropic sandbox runtime, E2B, Daytona, Z3 SMT solver, Landlock (Linux kernel feature)

## [AI That Hunts Logic Bugs Before Attackers Do - Taylor Luttrell-Williams, Sonar](../videos/UW8Qkk7MG8A.md)
`UW8Qkk7MG8A` · AI Engineer · 2026-10-29 · q2 · intro · demo · also: pr-code-review, agent-architecture

Sonar's SonarQube Hunter Agent: an on-demand/scheduled AI security agent that maps a repo, runs three specialized issue-class agents with adversarial validation and noise gates, and surfaces logic/authz flaws (IDOR, broken access control, business logic, auth/session) in SonarQube's normal issue list.

- Techniques: Multi-agent security scan with validation gates; Layered verification: SAST plus logic-level agent; Triage workflow for AI-raised issues
- Tools: SonarQube Hunter Agent, SonarQube (Cloud and Server), SonarQube remediation agent, SAST, SCA, OpenAI Daybreak Cyber Partner Program (frontier cybersecurity models)

## [Exploits Now Beat Patches: Open Source Security in the AI Era - Patrick Smyth, Chainguard](../videos/xZX3pmaB8Hk.md)
`xZX3pmaB8Hk` · AI Engineer · 2026-10-28 · q3 · practitioner · review · also: dev-tools, skills-self-improvement

Chainguard's Patrick Smyth argues frontier AI has made exploits beat patches: cooldowns, signed artifacts, tiered SLAs, minimal rebuilt images and vetted agent skills, wrapped in a vendor pitch.

- Techniques: Package cooldown period; Sign and verify every artifact; Build dependencies from clean source; Severity-tiered remediation SLA; Minimal, frequently rebuilt base images; Treat CI/CD as an attack surface; Vet agent skills before use; Hardware-backed developer identity
- Tools: Chainguard (vendor), Wolfi (Chainguard's rolling Linux distro), Chainguard Libraries (build-from-source packages), Chainguard Actions (hardened CI/CD actions), Chainguard agent skills (hardened third-party skills), Sigstore, SLSA (captioned 'Salsa'), Mandiant mTrends report (captioned 'Mandia'), Trivy (scanner, captioned 'Trivi', attacked in the supply chain incident), Grype (captioned 'Gripe', scanner named as an example), LiteLLM (captioned 'LightedLM', described as an agent router), Axios (npm package, compromised)

## [What a $900M Bank Error Teaches Us About AI Agents - John Feminella, Two Sigma](../videos/iniryju23Sk.md)
`iniryju23Sk` · AI Engineer · 2026-10-28 · q4 · practitioner · talk · also: governance-compliance, evals

Two Sigma's John Feminella ties a 2020 bank loan-payment error to AI agent governance and lays out five composable controls: registry, risk scoring, declared guardrails, shared evals, tiered approvals.

- Techniques: Tiered approval routing; Registry auto-registration through approved frameworks; Declared-capability manifest enforced at init; Risk-based review routing; Platform-owned shared eval harness
- Tools: FlexCube (internal bank processing software, as named in the talk), Claude Code, Pi (open-ended coding agent, as named in the talk), OpenClaw (named as 'open claw' in the talk)

## [Who Is Making This Request? Agent Auth 101 - Kamil Potrec, Keycard](../videos/58ulJViGFgU.md)
`58ulJViGFgU` · AI Engineer · 2026-10-28 · q3 · practitioner · talk · also: mcp-and-tools, governance-compliance

Keycard's Kamil Potrec argues agents need their own authenticated identities, short-lived scoped credentials via OAuth-style delegation, and a gateway that injects credentials outside the agent's reach, so every request is attributable and revocable.

- Tools: Keycard (control plane, client and service SDKs, gateway), MCP (Model Context Protocol), OAuth, agentbaseline.org (software factory reference implementation, named by the speaker)

## [Why Are We Still Governing AI Agents Like Software? - Tim Tyler, Gravitee](../videos/h8jgniNJcbQ.md)
`h8jgniNJcbQ` · AI Engineer · 2026-10-27 · q3 · intro · talk · also: governance-compliance, enterprise-adoption

Tim Tyler (Gravitee) argues AI agents should be governed like employees: a unique identity, a named human sponsor, a scoped role and authority, and tiered recourse, with rules as a deterministic floor and intents judged probabilistically.

- Techniques: Three-stage agent accountability model; Scope-lineage delegation check; Deterministic floor plus probabilistic scorecard; Confidence-tiered action ladder; Guardian agents at machine speed
- Tools: Gravitee (AI agent management), Claude (transcribed as 'Clyde'), MCP (Model Context Protocol), FGA policies (fine-grained authorization, generic reference), Mobile device management (MDM, analogy only), Agent accountability framework (agentaccountabilityframework.org)

## [300 Agents, 60 People: How We Secured Our Own AI Agents - Aiden Sochowski, Runlayer](../videos/BgLdvF7Qkh8.md)
`BgLdvF7Qkh8` · AI Engineer · 2026-10-27 · q3 · practitioner · talk · also: governance-compliance, observability, token-cost-efficiency

Runlayer's founding engineer describes how a 50-60 person company monitored its own 300+ daily agents through a gateway, then used the session data for security (intent drift, over-permissioning, cross-agent contamination) and for cost control (erroring MCP tools, model tier jumps).

- Techniques: Gateway-first agent telemetry; Per-tool-call intent classifier; Baseline-and-flag on tool-use history; Inbound and outbound content policies; Tight write scoping per agent; MCP error and retry monitoring with rate limits; Budgets and default model tiers
- Tools: MCP (Model Context Protocol), Claude Code (captioned as 'cloud code'), Opus (Claude model, mentioned as hard to prompt-inject), Runlayer (the speaker's company; product is a gateway, not named in detail)

## [Can Your AI Analyst Keep a Secret? - Aaron Linsky, Bridgewater & Nikhil Benesch, turbopuffer](../videos/u_jvuCjuvEk.md)
`u_jvuCjuvEk` · AI Engineer · 2026-10-26 · q4 · practitioner · talk · also: rag-retrieval, infra-cost-scaling

Bridgewater and turbopuffer explain how to run vector search over 100M documents with per-document permissions, using cluster-pruned "native filtering" to keep recall and latency acceptable.

- Techniques: Cluster-pruned native filtering for ACL-restricted vector search; Avoid fixed top-K then post-filter for access control; Express permissions as filter predicates on documents; Napkin math before choosing an index; Object-storage-first tiering for large, bursty corpora
- Tools: turbopuffer, Amazon S3, Google Cloud Storage, Azure Blob Storage, Bridgewater DeLorean (internal bitemporal macro time-series database, mentioned), Bridgewater Vault (internal unstructured document store, about 100M docs)

## [He Built the First Chatbot in 1966, Then Tried to Stop It (here's why)](../videos/O1Bab7biaGo.md)
`O1Bab7biaGo` · Better Stack · 2026-10-26 · q3 · intro · demo · also: context-engineering, product-ux

Better Stack runs the 1966 ELIZA chatbot's original code on a Mac, explains how its keyword-rule engine and swappable script work, and ties its "Eliza Effect" warnings to today's chatbot attachment problem.

- Techniques: Keyword-ranked rule matching with pronoun reflection and template fill; Recall-on-no-match fallback; Separate engine from persona script, with runtime rule edits; Treat the script or system prompt as leakable
- Tools: ELIZA (1966 DOCTOR script), IBM 7094 (transcribed as 'IBM 1794' in the captions), SLIP list-processing language, Lisp (BBN clone), BASIC (1977 magazine version), ARPANET, ChatGPT, Inventing Eliza (MIT Press book, July release)

## [Do Not Let Models Invent Numbers - Vinoo Ganesh, Kepler](../videos/dZgA6btnb_s.md)
`dZgA6btnb_s` · AI Engineer · 2026-10-25 · q4 · practitioner · talk · also: rag-retrieval, data-engineering

Kepler's CEO explains how its finance research platform stops LLMs from inventing numbers: models cite pre-registered SEC facts, deterministic code does the math, and any unverifiable number is stripped.

- Techniques: Cite-don't-write with post-filter; Typed fact registry; Search wide, then re-rank in stages; Per-hit document authorisation; Keep conflicting sources and de-conflict; Measure recall and idempotency as guarantees
- Tools: Kepler (finance research platform), Turbopuffer (vector and BM25 search, namespaces), Zero Entropy embeddings (as stated; 1280 dimensions), Postgres (per-document authorisation), Cross-encoder re-ranker (model not named), XBRL (structured filings data, cited as ~10% incorrect), SEC filings: 10-K, 10-Q, 8-K, S-1, investor presentations, earnings call transcripts, Claude and ChatGPT (used as baseline in evals), Gemini 4 (mentioned, not evaluated)

## [The AI Bug Apocalypse Has Officially Started](../videos/sZaMmVUmq-I.md)
`sZaMmVUmq-I` · Better Stack · 2026-10-25 · q3 · intro · news · also: dev-tools

Better Stack news roundup on "Black October" 2026: a leaked batch of Linux kernel SMB bugs, a wave of AI-found vulnerability disclosures, and what to patch this week.

- Techniques: Unload an unused kernel SMB server; Update-by-default patch policy; Read-only scope for agents that touch accounts
- Tools: Linux kernel, ksmbd, SMB / SMB Direct, PHP, GitLab, Node.js, VMware graphics driver, NVMe target code, Chrome, Microsoft SharePoint, Microsoft Patch Tuesday, Anthropic Mythos model

## [Real AI Agent Attacks and What Would Have Stopped Them — Andrey Rybka, Bloomberg](../videos/5O6jLtoeKrg.md)
`5O6jLtoeKrg` · AI Engineer · 2026-10-24 · q4 · practitioner · talk · also: sandboxing-execution, mcp-and-tools, agent-architecture

Bloomberg's Andrey Rybka walks through real agent security incidents (sandbox escape, CRM exfiltration, hidden-text injection, DNS leaks, a dropped production database) and maps each to layered controls: identity, input defense, deterministic tool brokers, default-deny egress, and budgets that halt.

- Techniques: Rule of two (capability gating for agent workflows); Deterministic invocation broker; Default-deny egress including DNS; One identity per agent, short-lived audience-bound tokens; Delayed package ingestion; Circuit breakers and halting budgets; Memory integrity and fresh-start policy; Security requirements in the spec
- Tools: MCP (Model Context Protocol) servers, OAuth, DNS, npm, NotebookLM (transcribed as 'Notebook Alarm'; likely NotebookLM), AWS accounts and GCP projects (as isolation analogies)

## [A Certificate Authority Just Got Caught Using a Private Key of 4](../videos/yW1RnJ5oaMk.md)
`yW1RnJ5oaMk` · Better Stack · 2026-10-23 · q4 · practitioner · news · also: dev-tools

Breakdown of the eMudra CA incident: eight intermediate CA private keys were trivially guessable (one was just 4). Browsers blocked them, but non-browser TLS clients that trust on-disk CA bundles stayed exposed.

- Techniques: Check EC public keys for small private keys; Upgrade on-disk CA bundles and the Go toolchain, then rebuild; Verify client trust against a known-bad test host; Verify key provenance during CA and HSM key ceremonies; Treat signature mismatches on revocation lists as incidents
- Tools: Certificate Transparency logs, Python, curl, Node.js, Go 1.27.3, Git, certifi 2026.10.19, Cloudflare WARP client, Cloudflare 1.1.1.1 app, Cloudflare Tunnel, Chrome, Firefox

## [How to Let AI Agents Sign Up for Your App Safely — Isabelle Williams, WorkOS](../videos/uTrY8slys0w.md)
`uTrY8slys0w` · AI Engineer · 2026-10-23 · q3 · practitioner · talk · also: mcp-and-tools, governance-compliance, product-ux

WorkOS PM walks through letting AI agents sign up for and act inside an app safely, using AuthMD, ID-JAG identity assertions, and agent tokens scoped to a user-bounded ceiling.

- Techniques: AuthMD discovery file; Anonymous trial with claim token; ID-JAG identity assertion grant; Blueprint ceiling with scope intersection; Separate agent principal from user session
- Tools: AuthMD (open markdown-based agent onboarding protocol), WorkOS Agent Auth, ID-JAG (Identity Assertion JWT Authorization Grant, IETF spec), OAuth 2.0, MCP authorization spec (Enterprise Managed Authorization), Okta Cross App Access, Claude (referred to as Claude / Cloud Code in the transcript), Cursor (used to vibe-code the demo app), Waypoint (speaker's demo travel-planning app), Muse and Instinct (personal agents mentioned, no detail given), Maple Itinerary and Trip Ledger (other planning tools the demo agent tried)

## [A PHP Bug Just Took Websites Offline Worldwide](../videos/Gxi_n-PtQBo.md)
`Gxi_n-PtQBo` · Better Stack · 2026-10-22 · q3 · intro · news · also: dev-tools, governance-compliance

Better Stack news explainer on the "PHP to Shell" pair of PHP bugs (CVSS 9.2 per the video): unauthenticated remote code execution in PHP itself, a coordinated-disclosure mess that pulled the patch forward, and a warning that AI speeds up exploit building.

- Techniques: Immediate PHP runtime patching when a language-level RCE is announced; Take the service offline when an unpatched RCE is live and the patch is not yet available; Pre-deploy WAF rules before public disclosure
- Tools: PHP, Chainguard PHP images, Cloudflare WAF, GPT 5.6 Sol, Gemini 4 Argon, Claude Mythos, Debian packages, Ubuntu packages, WordPress, Drupal, Joomla, Laravel

## [Your Local AI Is Not as Private as You Think](../videos/3mx84MRj8lY.md)
`3mx84MRj8lY` · Kai Explains · 2026-10-22 · q4 · practitioner · talk · also: local-ai, sandboxing-execution

Local AI is private, but a stranger's model file can still act on your machine through chat templates, runner bugs, exposed ports and poisoned fine-tunes; the fix is to limit what the model can reach.

- Techniques: Keep the model server on loopback; reach it remotely through an encrypted tunnel or an authenticated proxy; Patch the runner before anything else; Use official or established-quantizer weights for any model with tool access; Inspect the GGUF chat template before serving a model; Keep secrets out of the agent's working directory; Split command execution from network access and log the boundary; Do not rely on hash checks or allowlists alone
- Tools: Ollama (version 0.30.6 cited mid-October 2026; the talk also says 0.240.6 at 22:33, which conflicts), LM Studio, llama.cpp / llama.cpp server, llama-cpp-python, SGLang, vLLM, Hugging Face, GGUF, Jinja, SafeTensors, pickle scan / model-scan, Tailscale

## [OpenCode Got Hacked Badly (My API Keys Got Drained)](../videos/0p96nZsRxlY.md)
`0p96nZsRxlY` · Kai Explains · 2026-10-21 · q4 · practitioner · news · also: governance-compliance, token-cost-efficiency

OpenCode console breach postmortem: a legacy database with plaintext provider keys survived a "remove legacy" commit, and per-key spend limits, not the attacker, set who lost $16 vs $3,000. Ends with a key-hygiene checklist.

- Techniques: Set a provider hard limit, not just a spend alert; Prepaid credit balances without auto-reload; Revoke keys at the provider, not in the tool; Key inventory and rotation; One key per tool or service; Verify decommissioning of the underlying resource; Encrypt third-party credentials at the application layer
- Tools: OpenCode (terminal coding assistant and console web dashboard), OpenAI API, Anthropic API / Claude API console, Google Gemini API, Google Cloud, Claude, GPT, Gemini

## [Vercel's CEO Just Unveiled The Greatest AI Coding Workflow Ever](../videos/y2ifUC9_zuU.md)
`y2ifUC9_zuU` · AI LABS · 2026-10-20 · q2 · intro · tutorial · also: context-engineering, testing-verification, claude-code

Recap of a Vercel CEO interview: judge progress by direction rather than volume, run a plan-drift "direction" check, and use breaker, first-time-user and E2E agents plus MCP-based feedback triage. Partly a sponsor segment, with thin detail.

- Techniques: Direction drift-check command; Specs-first project setup; Must-not-trade-off rules with runnable tests; Quality gate checklist; Breaker agent loop; First-time-user agent with a hook-restricted bash tool; E2E path agent with JSON results; DeepSec security scan; Feedback triage with MCP connectors
- Tools: Claude Code, CLAUDE.md, DeepSec (Vercel security scanner), Gmail MCP, Sentry MCP, Victor (sponsor, AI hire in Slack/Teams)

## [Shipping AI Into 5 Major Banks Without a 12-Month Compliance Wait — Al Chen, Cisco](../videos/Bz1HFxQA1o8.md)
`Bz1HFxQA1o8` · AI Engineer · 2026-10-20 · q4 · practitioner · talk · also: governance-compliance, enterprise-adoption, sandboxing-execution

Al Chen (Cisco) on shipping AI into five major banks in weeks rather than a year: CVE remediation with agent-run exploit tests, ClickHouse cross-region DR with data-correctness checks, and keeping PII/MNPI out of LLM-judge reasoning, with showing evidence as the main lever for compliance speed.

- Techniques: Agent-driven exploit verification for CVE remediation (Harbor task); Cross-region ClickHouse DR with backup, restore and correctness checks; Split replication of IDs and metadata from core trace data for residency; Gating LLM-judge reasoning behind a sensitive-data check; Audit the judge prompt, not only the UI
- Tools: Harbor, Docker, Modal, Daytona, ClickHouse, ClickHouse backup (Altinity), Sysdig, Wiz, Prisma, NVD, CISA, MITRE CVE database

## [Why AI Agents Still Won't Pay for Anything — Jan Curn, Apify](../videos/-AOxpwVeIWw.md)
`-AOxpwVeIWw` · AI Engineer · 2026-10-19 · q3 · practitioner · talk · also: governance-compliance, product-ux

Jan Curn (Apify) argues agents still don't pay for services because the payment funnel (need, setup, trust, buy) has friction at each step, and pay-per-use is the missing piece.

- Techniques: Exact-plus-refund for metered agent billing; Charge before work for non-trivial cost; Escrow then micro-charge (batch settlement); Curated directory as the trust layer for agent-discoverable tools
- Tools: Apify (actors marketplace, about 80k actors), X402 (Coinbase, scheme exact, upto and batch settlement), MPP (Stripe and Tempo; sessions), L402 (Lightning Labs), MasterCard Agent Pay, KYA Pay (Skyfire with Visa), AP2 (Google), ACP (OpenAI and Stripe, Agentic Commerce Protocol), TAP (Visa, Trusted Agents Protocol), UCP (Google and Shopify, Universal Commerce Protocol), ACTP (Alipay), AMP (Alipay, Agentic Mobile Protocol)

## [How Websites Track You Without Cookies](../videos/Y5utTIuUNg4.md)
`Y5utTIuUNg4` · Better Stack · 2026-10-19 · q3 · intro · tutorial · also: —

Better Stack explainer on browser fingerprinting: how sites recognize a browser without cookies via screen, timezone, canvas and audio signals, how to test yourself with EFF's Cover Your Tracks, and which browsers defend best.

- Techniques: Fingerprint probe (conceptual); Self-audit with Cover Your Tracks; Choose a browser with built-in fingerprint defenses instead of add-ons; Block suspected fingerprinting scripts when a page misbehaves
- Tools: Fingerprint.js, EFF Cover Your Tracks, Tor Browser, Mullvad Browser, Brave, Firefox, Safari, Chrome

## [GitHub's #1 Trending Skill Is Insane (5 Use Cases)](../videos/rw0fqnrZgNM.md)
`rw0fqnrZgNM` · AI LABS · 2026-10-19 · q2 · practitioner · review · also: claude-code, skills-self-improvement, testing-verification

Walkthrough of the Reverse Engineer Anything (REA) MCP skill for Claude Code: feature cloning, black-box QA, competitor teardown, security sweep. Takeaway: tag findings by evidence, not guesses.

- Techniques: Behavior spec before implementation; Evidence-tagged findings; Black-box feature QA; Check the site against your written rules and promises; Competitor teardown; Pre-publish security and performance sweep
- Tools: Claude Code, Codex, Reverse Engineer Anything (REA) MCP server and skill, Hopper (binary analysis, optional), Firecrawl MCP server (sponsor), Notion MCP, Obsidian, Notion, OpenAI API, Stripe, GitHub

## [2 Million TV Boxes Are Already Infected. AI Is Next.](../videos/OfNajAPiGsM.md)
`OfNajAPiGsM` · Better Stack · 2026-10-19 · q3 · intro · news · also: models-research, inference-serving, local-ai

Better Stack walks through Anthropic's research on whether a small model could self-replicate across cheap IoT devices like TV boxes, and why the capability requirements don't yet overlap.

- Techniques: Pipeline-split a model across many weak devices; Separate the requirements of a dangerous capability and test each one; Give every model the same stand-in task for a fair comparison; Keep a remote brain, local hands
- Tools: Anthropic research (AI worm / self-replication study), Gemma 4 26B (Google open model), Qwen 3.5 9B, Llama 3.1 8B, GLM 5.2 (about 753B parameters), ADB (Android Debug Bridge), Google Cloud (8 Android test machines), Jetson Nano, NVIDIA RTX 4090, NVIDIA H100, Kimwolf botnet (transcribed as Kinwolf)

## [An AI Agent Got Its User Banned From Resy — Keycard, JPMorgan Chase & AAuth](../videos/IavxrdVnwXM.md)
`IavxrdVnwXM` · AI Engineer · 2026-10-18 · q3 · practitioner · panel · also: governance-compliance, enterprise-adoption, agent-architecture

Panel on intent-based runtime authorization for agents: per-call authz with mission context, budgets instead of rate limits, and enforcement outside the agent. Core claim: coarse OAuth scopes don't fit autonomous agents.

- Techniques: Budget-as-token grant with live feedback; Brains/hands split with egress-proxy enforcement; Separate supervising agent for worker actions; Deterministic must-never policy plus intent-derived bounds; Dynamic tool gating by task phase; Intent and environment in trace spans
- Tools: OAuth, OIDC, MCP, Claude Code, Squid proxy, Chrome, Firefox, AAuth

## [Why One AI Agent Isn’t Enough (And How to Run 1,000) - CJ Avilla & Harrison Stall, Anthropic](../videos/kiClTcJUnhc.md)
`kiClTcJUnhc` · AI Engineer · 2026-10-17 · q4 · practitioner · talk · also: multi-agent, agent-architecture, governance-compliance

Anthropic's Claude Managed Agents "flows" (dynamic multi-agent workflows) talk: how to fan out hundreds of isolated sub-agents, control cost with budgets, and contain risk with credential vaults, egress rules and auto mode.

- Techniques: Plan, fan out, phase-gate; Per-phase model and agent-count allocation; Separate reviewer context for adversarial checks; Two-stage review with verification; Budget as a resumable circuit breaker; Credential injection at the egress proxy; Declare, contain, detect; Transcript audit agent; Gradual context reveal via linked markdown index; Filesystem as the inter-agent channel; Interrupt and redirect
- Tools: Claude Managed Agents, Claude Code, Claude API skill, ant CLI, Terraform provider for Claude agents, Dynamic workflows (Claude Code), Hill-climb skill, Dreaming (memory consolidation product), Auto mode (permission classifier), Bug Hunter flow, Explainer Video Maker flow, Claude Tag (Slack bot)

## [Paving the Road to Production: Governed Enterprise AI Agents — Harish Gaggar, Credit Karma](../videos/tZycGA_Fbfo.md)
`tZycGA_Fbfo` · AI Engineer · 2026-10-15 · q3 · practitioner · talk · also: mcp-and-tools, observability, context-engineering

Credit Karma's senior staff engineer walks through a governed enterprise agent stack: scaffolded agent repos, a central MCP gateway, risk-gated execution, per-run evals, PII blocking, and a context optimizer that cut token use about 90% in demos.

- Techniques: Dev-portal agent scaffolding; Gateway token exchange with namespace routing; Risk-classified plan graph with HITL gate; Thread, run and checkpoint memory; Severity-based redaction before every sink; Context pipeline: budget, re-rank, dedupe, compress; Per-run eval scoreboard with nested detail; Three-layer monitoring split
- Tools: LangGraph, LangChain, FastMCP, Redis, JWT, Docker, Kubernetes, OpenTelemetry, Grafana Tempo, Prometheus, ELK, Loki

## [Your AI Isn’t the Problem. Your Infrastructure Is. — Jiachen Jiang, Coder](../videos/Wb2v9Phhnns.md)
`Wb2v9Phhnns` · AI Engineer · 2026-10-15 · q3 · practitioner · talk · also: sandboxing-execution, governance-compliance

Coder's staff PM walks through three real AI-agent incidents (a Replit prod wipe, a Copilot-enabled bank exfiltration, the NX supply-chain attack) and argues that infrastructure controls, not smarter models, prevent them.

- Techniques: Ephemeral remote workspaces with no route to production; Per-task short-lived, narrow-scope credentials; Identity-aligned access control for AI tools; Model proxy layer; Agent sandboxing as a firewall; Externally owned audit logs with real-time alerting; Planning-only mode and automatic dev/prod DB separation; Premortem with the team
- Tools: Replit Agent, Microsoft Copilot, Nx (build tool), Coder workspaces, Claude Code, Codex

## [Your GPU Neighbor Can Hear Your Model — Branislav Brzak, Stealthium](../videos/SacJfmp33vM.md)
`SacJfmp33vM` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · also: inference-serving, sandboxing-execution

Timing alone on shared H100s leaks a neighbor's LLM: model depth, token speed and workload type, via MIG or NVLink. Mitigate with careful placement, host-side kernel monitoring, and no MIG co-location with untrusted tenants.

- Techniques: Timing probe on own memory; Frequency analysis of latency traces for model fingerprinting; Keep sensitive models off MIG slices shared with untrusted tenants; Host-side kernel-launch monitoring
- Tools: NVIDIA MIG, NVLink, NVSwitch, vLLM, speculative decoding, Qwen 8B, Llama 3 8B, DeepSeek R1 distill, GPT-OSS 20B, GLM 4.9B

## [Your Agent Is a Lethal Trifecta (And What to Do About It) — Kim Maida, Keycard](../videos/ws9XcGGPBDk.md)
`ws9XcGGPBDk` · AI Engineer · 2026-10-13 · q4 · practitioner · talk · also: mcp-and-tools, governance-compliance

Kim Maida (Keycard) argues agents with private data, untrusted content and external comms form a "lethal trifecta" and shows how token exchange (OAuth 2 RFC 8693-style STS), task-scoped ephemeral tokens and mission-based authorization contain the blast radius without removing capabilities.

- Techniques: Per-tool-call token exchange through an STS; Mission-scoped approval before tool use; Keep all three trifecta legs and control access instead; Audit with attributed identity chains
- Tools: Keycard, OAuth 2 token exchange (RFC 8693 style), MCP servers, MCP gateway, Snowflake, Incident pager API, Google login

## [Build a Research Agent with Claude Managed Agents (Part 2 of 4) — Anthropic](../videos/FGftGOzfohc.md)
`FGftGOzfohc` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: agent-architecture, multi-agent, memory

Anthropic hands-on workshop (Part 2 of 4) building a research agent on Claude Managed Agents: sub-agents, rubric-graded outcomes, vaults, shared memory, dreaming, and a map-reduce harness.

- Techniques: Rubric-gated outcome with a grader sub-agent; Placeholder secrets with domain-scoped egress swap; Context isolation via self-referencing sub-agents; Check shared memory before redoing work; Map-reduce orchestration via a custom dispatch tool; Transcript-driven memory consolidation (dreaming)
- Tools: Claude Managed Agents API, Claude Code (used to drive the workshop), SEC EDGAR Python package, MCP, Bun, npm, Agent SDK (compared)

## [Agent Speedrun — Elizabeth Fuentes Leone & Sandhya Subramani, AWS](../videos/YXiLj4tJt5A.md)
`YXiLj4tJt5A` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: agent-architecture, skills-self-improvement, mcp-and-tools

Hands-on AWS workshop: build a Strands customer-service agent with hooks (rate limit, deterministic blocks), lazy-loaded skills, steering guardrails, then deploy to AgentCore Runtime.

- Techniques: Per-request tool-call rate limiter via hooks; Deterministic input filter hook; Skills as on-demand markdown procedures; Steering handler (rule or LLM buddy); Externalised steering rules; Message-history inspection
- Tools: Strands Agents, Amazon Bedrock AgentCore (Runtime, Memory, Gateway, Observability), Amazon Bedrock, Amazon CloudWatch, AWS CDK / CloudFormation, AWS OpenTelemetry Distro, boto3, agent-control (open-source steering rules library), MCP, A2A, Jupyter / Workshop Studio

## [AI Security Engineer Foundations + Certificate — Micah Silverman, Snyk](../videos/p-2MT8KYZqU.md)
`p-2MT8KYZqU` · AI Engineer · 2026-10-12 · q3 · practitioner · workshop · also: mcp-and-tools, governance-compliance, vibe-coding-app-building

Two-hour Snyk workshop on AI security foundations: OWASP LLM Top 10 risks, shadow AI and AI bills of materials, AI threat modeling, MCP tool poisoning, vibe-coding failures, and a live CTF chatbot exercise.

- Techniques: Layered prompt-injection defense; Keep secrets out of prompts and enforce access outside the model; Scope chatbot data to what may be disclosed; AI threat modeling workflow; Adversarial review of an architecture; AI BOM as a CI gate; Audit MCP configs and servers before enabling; Secure-by-design playbook for agentic coding; Probe a chatbot in a CTF-style sandbox; Offer an approved alternative when restricting a tool
- Tools: Snyk Evo, Snyk Agent Scan, Snyk Code, Snyk (SCA/SAST), OWASP Top 10 for LLM Applications, STRIDE, DREAD, SBOM (SPDX, CycloneDX), CycloneDX (AI/ML BOM support), Model Context Protocol (MCP), Figma Framelink MCP server, OpenClaw

## [Build a Platform and Watch It Burn — Michael Forrester, Accenture & Whitney Lee, Datadog](../videos/1tpqdglI3T0.md)
`1tpqdglI3T0` · AI Engineer · 2026-10-12 · q4 · practitioner · workshop · also: sandboxing-execution, mcp-and-tools, observability

Workshop where attendees attack a Kubernetes-hosted burrito-ordering agent, then add layered infra and AI guardrails (admission, runtime, network, input/output scrubbing, MCP checks) and see which attacks each layer stops.

- Techniques: Layered guardrails across infra and AI; Input guard before the LLM call; Mid-stream output scrubbing; MCP tool description review and registry allowlists; OpenTelemetry traces for every agent turn; Kernel-level prevention for runaway processes; Agent identity and least privilege; Three-question rubric for AI in a workflow
- Tools: Kubernetes, Amazon EKS, kagent, Kyverno, Falco, Falco Talon, Tetragon, KubeArmor, Cilium, SPIFFE/SPIRE, LLM Guard, NeMo Guardrails

## [How Secrets Leak Through AI Agents (and How to Stop It) — Venice AI](../videos/xn8EsW0wxyc.md)
`xn8EsW0wxyc` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: agent-architecture, observability, mcp-and-tools

Venice AI's developer-relations lead explains how secrets leak through agent architectures (logs, vaults, LLM context, tool calls) and patterns to contain them: hashed IDs, handles, narrow tool scope, and keeping credentials out of the reasoning layer.

- Techniques: Credential-in-runtime, not in-prompt; Hashed identifiers for rate limits and tracking; Split-key custody for stored outputs; Revocable handles as capabilities; Narrow tool exposure per agent; Prompt-injection classifier in front of the agent; Own the agent runtime; Verifiable private inference via TEE attestation
- Tools: Venice AI, OpenClaw, 1Password, HashiCorp Vault, Firecracker, AWS EC2, VPC, Qdrant, LanceDB, Cursor, Claude Code, MCP

## [Auth for Agents: Let AI Sign Up for Your Product with auth.md — Michael Grinich, WorkOS](../videos/nSkmXakJ6eo.md)
`nSkmXakJ6eo` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: mcp-and-tools, product-ux

WorkOS founder argues agents need their own sign-up step, and proposes auth.md, an open markdown spec that tells an agent how to register for a service without a human clicking through.

- Techniques: auth.md registration spec; Identity assertion exchange for agent sign-up; Risk-scored registration with time-boxed free access; Deferred human claim; Approval-only supervision
- Tools: auth.md, MCP, ID-JAG, Wrangler, Pi (agent harness), Claude, OpenClaw, x402, Cloudflare

## [SonarQube + OpenAI: Agentic Development — Killian Carlsen-Phelan, Sonar](../videos/bI8WyG9YB0I.md)
`bI8WyG9YB0I` · AI Engineer · 2026-10-12 · q3 · practitioner · demo · also: testing-verification, coding-agents, context-engineering

A Codex deployment engineer and a Sonar developer advocate argue that agent "done" needs evidence, containment is not correctness, and feedback checks belong inside the agent loop, then demo SonarQube hooks, MCP and CLI wired into Codex.

- Techniques: Evidence-backed definition of done; Layered execution and artifact controls; Secret-blocking lifecycle hook; Guide, verify, solve loop (ACDC); Taint analysis across files; Changed-code-only verification for agent edits; Custom rules targeting agent-written code
- Tools: Codex (OpenAI coding agent CLI), SonarQube Cloud, SonarQube CLI, SonarQube MCP server, SonarQube Codex plugin / marketplace, Docker, Git Bash (for setup script)

## [The Next Trillion Internet Users Still Don’t Have an Identity — Adi Singh, AgentMail](../videos/mBNVKkyfnE0.md)
`mBNVKkyfnE0` · AI Engineer · 2026-10-12 · q3 · intro · talk · also: mcp-and-tools, product-ux

Adi Singh (AgentMail) argues agent identity will be accumulated from existing human-facing surfaces like email and Slack rather than issued from scratch, and that over-tight key-card style security specs hurt adoption.

- Techniques: skill.md signup flow with inbox provisioning API; Dedicated per-agent inbox as the identity and contact point; Use existing surfaces as the bridge for new agent identity
- Tools: AgentMail, Telnyx, Clawk, OpenClaw, MCP, DKIM/SPF/DMARC, DIDs, agent cards, skill.md

## [I Turned My Wi-Fi Into a Surveillance System](../videos/9Tihk9_jUyo.md)
`9Tihk9_jUyo` · Better Stack · 2026-10-12 · q3 · practitioner · review · also: models-research, voice-multimodal

Walkthrough of Wi-Fi sensing (RuView): the speaker critiques its headline accuracy, rebuilds a cheap ESP32-S3 setup, and trains a Wi-Fi-only pose model from camera labels.

- Techniques: Camera-supervised CSI training (teacher-student); Held-out environment evaluation for sensing models; Node-to-node links to multiply sensing lines; Edge-only label export for privacy; Visual node identification during setup
- Tools: RuView (open-source Wi-Fi sensing firmware and pose model; includes a fall detection feature), ESP32-S3 boards (about $10 each, three used), MediaPipe (Google, pose detection running in the browser), MacBook (ran the RuView pose model), MMFI public dataset (40 people, four rooms, camera plus Wi-Fi), 802.11bf (Wi-Fi sensing standard, mentioned as published last year)

## [Turning My Obsidian Vault Into a Local AI Engineer — Filip Makraduli, Superlinked](../videos/Ndp5VaqFrl0.md)
`Ndp5VaqFrl0` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: local-ai, mcp-and-tools, inference-serving

Filip Makraduli (Superlinked) shows a privacy-first setup: a self-hosted MCP tool server runs OCR, redaction and extraction on sensitive documents in your own cloud, so a Claude Code agent only sees the cleaned output.

- Techniques: MCP tool server in front of private inference; Per-worker batching instead of a shared queue; Multi-model hot-swapping on one GPU; Stateless tools-only MCP server over streamable HTTP; Check thinking-token settings per model in tool pipelines; Warm-model-aware routing (roadmap)
- Tools: MCP, Claude Code, Obsidian, Superlinked, Terraform, Helm, Kubernetes, Docker, Claude Co-work

## [Sandboxes Aren't Optional: 4 Ways to Isolate Coding Agents — Robert Brennan, OpenHands](../videos/iH_wV8BbS24.md)
`iH_wV8BbS24` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: sandboxing-execution, coding-agents, infra-cost-scaling

Robert Brennan (OpenHands CEO) compares four ways to sandbox coding agents, from Docker on a laptop to one Kubernetes pod per session, and argues least privilege should set the blast radius.

- Techniques: Container per agent conversation with selective mounts; Least-privilege sandbox spec; Ephemeral pod per agent session; Event- or schedule-triggered cloud agents; Matching environment to job
- Tools: OpenHands, OpenHands Agent Canvas, Claude Code, Codex, Docker, Kubernetes, GitHub Actions, Cursor, GitHub Copilot, Twilio, Slack, Datadog

## [AI Security Engineer Foundations + Certificate — Javier Garza, Snyk](../videos/ZyC56eV8sVw.md)
`ZyC56eV8sVw` · AI Engineer · 2026-10-12 · q2 · intro · workshop · also: mcp-and-tools, governance-compliance, coding-agents

A two-hour Snyk workshop on AI security basics: OWASP LLM Top 10, shadow AI and AI bills of materials, AI threat modeling, MCP and skill supply-chain risk, and secure-by-default coding hooks.

- Techniques: Treat LLM input and output as untrusted data; Read-only database views for agents; Approval gate for high-risk actions; Full action logging plus a background log scanner; Scan-fix-rescan agent hook; Pre-install scanning of MCP servers and skills; AI-BOM inventory with query by component; Security requirements inside the prompt
- Tools: Snyk agent-scan (MCP and tool scanner), Snyk AI-BOM (CycloneDX-style inventory), Gandalf (Lakera) prompt-injection game, Claude Code, Cursor, Windsurf, OpenClaw, CycloneDX, SPDX, STRIDE, MITRE ATLAS, uvx

## [AI Agents Don't Read Your Policy Docs. They Hit Your APIs — Gravitee](../videos/7v2myBde05o.md)
`7v2myBde05o` · AI Engineer · 2026-10-11 · q2 · practitioner · review · also: governance-compliance, infra-cost-scaling, mcp-and-tools


- Techniques: Per-task scoped agent identity via token exchange; Gateway-level rate limiting on agent requests; Semantic cache keyed on prompt similarity; Pre-request prompt size and relevance policies; Narrowing MCP servers to a per-agent tool subset; Export gateway telemetry to existing observability stack
- Tools: Gravitee AI Gateway, Anthropic Claude (Sonnet), Groq (inference), Databricks, Redis (built-in semantic cache), MCP (Model Context Protocol), A2A (agent-to-agent protocol), OpenTelemetry, Datadog, Splunk, Prometheus, Kubernetes

## [The Lethal Trifecta Is Already on Your Laptops — Michael Patterson, Coder](../videos/abw_m-DRi1k.md)
`abw_m-DRi1k` · AI Engineer · 2026-10-11 · q2 · intro · talk · also: sandboxing-execution, observability

Coder's staff solutions engineer explains the "lethal trifecta" (private data, external communication, untrusted input) and argues for isolated remote dev environments, a logging model proxy, and a process-level agent firewall.

- Techniques: Remote isolated agent environment; Logging model proxy in front of the LLM provider; Process-level agent firewall with command denylist; Pre-baked environments as supply-chain control
- Tools: Coder, Terraform, Claude Code, Codex, OpenClaw

## [Beyond RAG: Build a Relational Context Engine from Scratch — Peter Werry, Unblocked](../videos/spxoDAfh5ig.md)
`spxoDAfh5ig` · AI Engineer · 2026-10-11 · q4 · practitioner · workshop · also: rag-retrieval, data-engineering, context-engineering

Peter Werry (Unblocked) builds a schema-aware natural-language-to-database-query engine from scratch, covering schema sampling, identity mapping, allow-list validation and an error-retry loop, as the structured half of retrieval beyond RAG.

- Techniques: Dynamic schema discovery by document sampling; Deny-by-default query validation; Error-feedback retry loop; Forced tool call for entity extraction, with a fallback; Fuzzy identity mapping; Date-aware prompting for temporal queries; Two-stage schema selection; Hybrid entry point, then structured queries; Webhook-driven ingest and re-embed
- Tools: MongoDB, Postgres (mentioned as a comparison with table definitions), GitHub, Linear, Jira, Slack, MCP, Levenshtein distance

## [Designing CLIs for Agents, Not Humans — Pedro Lopez, Airbyte](../videos/3wj6sgbi1YA.md)
`3wj6sgbi1YA` · AI Engineer · 2026-10-10 · q3 · practitioner · talk · also: mcp-and-tools, coding-agents

Airbyte's Pedro Lopez on building a thin MCP server and CLI for agents: a small tool surface, OAuth-only auth, JSON in and out, non-interactive credentials, and skills shipped with the CLI.

- Techniques: Thin interface over a shared API spec; Minimal tool surface with progressive discovery; OAuth-first MCP auth with a connect-link flow for third-party credentials; Agent-friendly CLI contract; Ship a skill with the CLI, with progressive references; Use failure patterns as a design signal
- Tools: MCP, CLI, OAuth, OpenAPI, jq, Claude Desktop, Claude custom connectors, ChatGPT app store, Airbyte AI Agents context store, Zendesk, Stripe, HubSpot

## [From Context to Memory: Your Agents Need a Real Memory Layer — Anders Swanson, Oracle](../videos/BIhiYL4U9_M.md)
`BIhiYL4U9_M` · AI Engineer · 2026-10-10 · q3 · practitioner · talk · also: memory, rag-retrieval, context-engineering

Oracle's Anders Swanson argues agent memory should be a governed, typed database layer with redaction, hybrid retrieval, scoped access, and feedback loops, not files or bigger context windows.

- Techniques: Typed memory schema with per-type lookup; Write pipeline: redact, enrich, scope, embed, episode-link; Weighted hybrid retrieval with fused scores and provenance; Governance on write and on read; Feedback signals that rank and promote or demote memories; Expose memory as a runtime function
- Tools: Oracle AI Database, Oracle Python SDK for agent memory (speaker's; referenced, not shown), Claude Code, Codex, MCP, hooks, skills

## [Brains vs Hands: How to Run AI Agents Safely in Production — Viren Baraiya](../videos/NaOkR3VSfR4.md)
`NaOkR3VSfR4` · AI Engineer · 2026-10-09 · q4 · practitioner · talk · also: agent-architecture, multi-agent

Viren Baraiya on running production agents: the LLM only plans, a deterministic harness executes side effects, durable state and human gates make it safe, shown with a Conductor SRE remediation demo.

- Techniques: Brains/hands split; Plan-compile-execute; Code-enforced human approval gate; Idempotent steps or recorded side effects; State-driven replanning loop; Single-responsibility harnesses
- Tools: Conductor, Kubernetes, Slack, LangChain agents, OpenAI Agents SDK, Google ADK, MCP, APIs

## [Why Your AI Agents Can't Talk to Each Other (Yet) — Vlad Luzin, BAND](../videos/toq-jyGLZDk.md)
`toq-jyGLZDk` · AI Engineer · 2026-10-08 · q2 · intro · talk · also: multi-agent, mcp-and-tools

Vlad Luzin (BAND) argues that agent-to-agent communication is a distributed-systems problem that MCP, A2A and chat platforms don't solve, then pitches BAND's hosted interaction layer.

- Techniques: Loop engineering with two stateful agents; Contact request with bilateral consent before agent discovery; Shared conversational space with human visibility; Runtime ID binding across agent frameworks
- Tools: Claude, Claude Code, Codex, LangGraph, CrewAI, MCP, A2A, ACP, Slack, Microsoft Teams, Discord, WhatsApp

## [From 36% to 100%: How Self-Improving Agents Write Their Own Skills — Rafal Wilinski, Runlayer](../videos/u-o0sW9nwmk.md)
`u-o0sW9nwmk` · AI Engineer · 2026-10-08 · q3 · practitioner · talk · also: skills-self-improvement, mcp-and-tools

Rafal Wilinski (Runlayer) argues agents should distill successful and failed runs into skills, serve them via MCP as a governed company-wide library, and reports a 36% to 100% success jump after one distilled skill.

- Techniques: Trace-to-skill distillation; Learn from failures too; Checks before publishing a skill; Remote MCP skill registry with tool-based access; Group similar runs before distilling
- Tools: MCP, Claude Sonnet 4.6, Voyager, Chromium, AWS Lambda, npx skills

## [AI Hackers Are Faster Than Your Pen Test — Eli Cohen, Snyk](../videos/f3o0-9Dlw3E.md)
`f3o0-9Dlw3E` · AI Engineer · 2026-10-08 · q2 · intro · talk · also: multi-agent, pr-code-review

Snyk's Eli Cohen argues LLM-generated code and LLM attackers make twice-yearly pentests obsolete, and pitches a continuous, per-PR AI pentest pipeline (Snyk Evo) with an exploit-validation judge.

- Techniques: Layered agent pipeline for continuous pentesting; Scanner output as LLM context; Exploit proof gate before flagging; Per-PR security trigger
- Tools: Snyk Evo (Snyk's continuous AI offensive security / AI pentesting offering, named in the talk), Snyk (company), Helios (runtime security company, acquired by Snyk), Claude Code (called "cloud code" in captions), Codex (OpenAI coding agent), SAST (static application security testing), DAST (dynamic application security testing; captioned as "dust"), MCP (Model Context Protocol), Mythos (model named in passing; exact referent unclear)

## [How AI Agents Pay: Checkout in ChatGPT and Google AI Mode — Sam Parsons, PayPal](../videos/c5U-XbbEN-g.md)
`c5U-XbbEN-g` · AI Engineer · 2026-10-06 · q2 · intro · talk · also: mcp-and-tools, product-ux

PayPal Enterprise Payments (Braintree) walks through three ways merchants accept payments from AI agents: ChatGPT instant checkout, Google AI Mode via UCP, and MCP apps with external checkout.

- Techniques: Host-side tokenization with scoped payment tokens; MCP app widget that triggers host-native checkout; Discovery file plus session endpoints for headless checkout; External checkout handoff linked to a session
- Tools: MCP Apps, Agentic Commerce Protocol (ACP), Universal Commerce Protocol (UCP), Google Pay, Braintree / PayPal Enterprise Payments, ChatGPT, Claude connectors, Goose

## [How Many Credentials Should Your AI Agent Have? Zero. — Jim Clark, Docker](../videos/ZUZVNKFSmTM.md)
`ZUZVNKFSmTM` · AI Engineer · 2026-10-06 · q3 · practitioner · talk · also: sandboxing-execution, mcp-and-tools

Docker engineer Jim Clark argues that agent safety comes from small, task-shaped sandboxes fed through an MCP gateway, with zero credentials inside the sandbox. The talk also pitches Docker's SBX product.

- Techniques: Role-split sandboxes for untrusted-input pipelines; Intent-scoped sandbox per task; Single MCP gateway as the policy point; Credentials held outside the sandbox; Cross App Access token exchange; Progressive tool disclosure
- Tools: Claude Code, Codex, MCP, MARP, Mermaid, Docker SBX, OpenCode, Gemini

## [An Interaction Is All You Need — Ivan Leo, Google DeepMind](../videos/8aVbXXvJUY4.md)
`8aVbXXvJUY4` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: agent-architecture, sandboxing-execution, mcp-and-tools

Google DeepMind's Ivan Leo presents the Interactions API and Managed Agents: server-side state via interaction IDs, persistent sandboxes via environment IDs, and a credential-injecting proxy. Mostly a product walkthrough with a few reusable patterns.

- Techniques: Server-side conversation state via interaction ID; Reattach to a persistent sandbox via environment ID; Proxy-side credential injection; Freeze a tuned environment as a named agent; Local-to-cloud skill packaging; Strongly typed output parsing
- Tools: Interactions API, Managed Agents, Antigravity agent harness, Gemini API CLI, AI Studio, Google Search tool, URL context tool, GCS, GitHub

## [YOLO Mode, Safely: MicroVM Sandboxes for Any Agent — Rowan Christmas, Docker](../videos/OE_lLNCNfQo.md)
`OE_lLNCNfQo` · AI Engineer · 2026-10-04 · q2 · intro · talk · also: sandboxing-execution, governance-compliance

Docker's product manager argues coding agents need micro-VM sandboxes with secret placeholders and default-deny egress, and shows a self-test where Claude Code found his bank data. Mostly a product pitch.

- Techniques: Run agents in a micro-VM with bypass permissions on; Placeholder secrets swapped at the network boundary; Default-deny egress with an allowlist; Read-only mounts of context repos; Self red-teaming with real personal data
- Tools: Docker SBX, Claude Code, Claude Desktop, Codex, CrowdStrike, Cedar, Datadog

## [Your LLM App Returned 200 OK. It Was Still Wrong. — Marina Petzel, Datadog](../videos/rTojoVotlD8.md)
`rTojoVotlD8` · AI Engineer · 2026-10-04 · q3 · intro · talk · also: observability, governance-compliance, evals

Datadog's Marina Petzel argues LLM apps need cost, safety and quality monitoring on top of the golden signals, since a 200 OK can still hide a wrong answer; gives tagging and metric recommendations.

- Techniques: Mandatory four-level cost tagging; Track token creep and model drift as separate alerts; Caching layer to remove redundant completions; Guardrail metrics as blocking thresholds; LLM-as-judge for completeness, embeddings for relevance; Score RAG retrieval separately
- Tools: Datadog agent observability

## [This AI Startup Is Making Powerful AI Models (Desert Ant Labs)](../videos/P_7HwwUsOfA.md)
`P_7HwwUsOfA` · Better Stack · 2026-10-02 · q3 · intro · review · also: local-ai, voice-multimodal

Better Stack hands-on tour of 12 tiny on-device models from Desert Ant Labs (speech, redaction, language ID, emoji). Several are fast and useful, some are weak, and the vendor benchmarks are mostly unverified.

- Techniques: Small specialist model as a background layer; Smoke-test a vendor micro-model on your own data inside a thin wrapper app; Read the confidence score before trusting a language-ID result
- Tools: Desert Ant Labs (vendor, 12 shipped models plus 5 beta), Hugging Face (model hosting), GitHub (SDK), Vaus (on-device speech recognition, claims 10 min audio in ~2 s on iPhone), Clear (speech enhancement), Clips (highlight extraction from long recordings), Clipper (desktop app built on Clips), Title (short factual title and description from text), Redact (on-device PII stripping as you type, 27 languages), Um (filler-word removal), Emo (emoji suggestion, ~5 MB), Gist (topic and tag prediction from titles, claims 101 languages)

## [We're Headed For Superintelligence By 2030](../videos/k-qAht4w9Rg.md)
`k-qAht4w9Rg` · Better Stack · 2026-10-02 · q2 · intro · news · also: models-research, enterprise-adoption

Better Stack scores the 2025 "AI 2027" forecast against 2026 events: alignment incidents and the junior-engineer squeeze match, while China consolidation and the protests do not, and the authors now push superintelligence to 2029-2033.

- Techniques: Dated prediction scorecard; Use open-weight models as the verifiable size bound
- Tools: AI 2027 (paper), Epoch AI (compute estimates), Indeed (job postings data), GPT-5.3 Codex, Grok 4, Kimi 3, DeepSeek V4 Pro, Claude Haiku, Sonnet and Opus (as named in an Anthropic report), Mythos Preview (Anthropic model, named in a survey), Fable (captioned; model name unclear)

## [DeepSeek and Kimi Secretly Sent Your Prompts to Claude](../videos/hSVCYzphZjQ.md)
`hSVCYzphZjQ` · Better Stack · 2026-10-02 · q3 · intro · news · also: models-research, governance-compliance

Recap of Anthropic's report accusing Alibaba, Moonshot, DeepSeek, Z.ai, Xiaomi and others of industrial-scale distillation of Claude via fake accounts and proxies, plus the API changes it prompted.

- Techniques: Preserved Thinking constraint (Anthropic API, per speaker); Do not depend on raw reasoning text; Platform-side extraction defenses (extrapolated, not stated in the video)
- Tools: Claude Opus 4.6, Claude Opus 4.7, Claude Opus 4.8, Claude Haiku, Fable (model name as spoken; Fable 5.1 cited for Preserved Thinking), Claude Code, Claude Agent SDK, OpenCode, Qwen 3.5/3.6/3.7 (Alibaba), Kimi (Moonshot), DeepSeek, GLM 5.3 (Z.ai)

## [Claude Code Can Now Take Your App Live (GoLive)](../videos/HTscIrJhjDs.md)
`HTscIrJhjDs` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: claude-code, dev-tools

Walkthrough of GoLive, an early agent skill plus Node CLI that takes a repo live (Vercel, Supabase, Resend, Stripe) via plan, approve, apply, verify gates, with candid caveats about consent and credential storage.

- Techniques: Plan-then-approve-then-apply with a plan ID; Verify webhooks both negatively and positively after deploy; Separate confirm flags for destructive, DNS and production-live actions; Refuse-list for paid or account-creating actions; Ownership-tagged teardown; Borrow existing CLI logins instead of minting credentials; Post-run written report with no secrets; Skill file plus a small CLI, not an MCP server
- Tools: GoLive (agent skill plus Node CLI; repo name not shown in the transcript), Claude Code, Codex, Vercel, Netlify, Supabase, Neon, Resend, Stripe (test and live modes), Terraform, SST, Lovable

## [DBX Is Almost the Perfect Free Database Client](../videos/b6rVCrBPbe8.md)
`b6rVCrBPbe8` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: dev-tools, mcp-and-tools

Hands-on review of DBX, a free desktop database client with an optional MCP server that lets coding agents query saved connections; the reviewer praises the workflow but flags plaintext passwords in its local SQLite file as a blocker for production credentials.

- Techniques: Stand up a multi-engine local test rig; Add a connection with a test-before-save step; Register the DBX MCP server with Claude Code and check it appears; Agent prompts used for smoke testing; Audit a local client's credential store before storing production secrets
- Tools: DBX (free desktop database client, version not stated), DBX MCP server (separate binary), Claude Code (used to register and call the MCP tools), Docker Compose, MySQL, Redis, MongoDB, Postgres, SQLite (dbxdb file), DuckDB, Navicat, DataGrip

## [The Real Reason Behind NVIDIA Buying Hugging Face](../videos/s7dKx9Pl2j0.md)
`s7dKx9Pl2j0` · Kai Explains · 2026-10-02 · q3 · intro · news · also: local-ai, models-research, sandboxing-execution

Kai Explains argues NVIDIA's $12.9B Hugging Face deal is about the open-weights policy fight, prompted by an AI agent's sandbox escape and breach of Hugging Face, not just distribution.

- Techniques: Treat an egress proxy as an attack surface, not a containment guarantee; Use a locally run open-weight model for incident forensics when closed APIs refuse or data cannot leave; Triage agent-driven intrusion logs for machine-like signatures; Prefer non-executable weight formats, and still audit the loading pipeline
- Tools: Hugging Face Hub, OpenAI Exploit Gym (benchmark), GPT 5.6 Sol (named in the video), GLM 5.2 (open-weight model), safetensors, PyTorch Foundation, NVIDIA Base Command Manager, Bright Computing, Slurm (SchedMD), CUDA, NVIDIA open agent framework

## [This New Open Source Tool Just Fixed Your Claude Code Workflow](../videos/CHHEjuNBxoQ.md)
`CHHEjuNBxoQ` · AI LABS · 2026-10-02 · q3 · practitioner · review · also: coding-agents, context-engineering, memory

Walkthrough of Agit, an open-source tool that applies git's model (repos, sessions as branches, turns as commits) to agent conversations, with sharing, revert, cross-agent fork and secret redaction.

- Techniques: Versioned agent sessions via a git-style repo; Reverting a session to an earlier turn; Cherry-picking messages between sessions; Forking a Claude Code session into Codex; Registering known passwords before a session is saved
- Tools: Agit, createagit (installer), npm, GitHub, Claude Code, Codex, AGENTS.md, CLAUDE.md, Runnable (sponsor)

## [IT Admin for the AI Workforce — Sarthak Aggarwal, Decawork](../videos/q-WOjZhOMCA.md)
`q-WOjZhOMCA` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: governance-compliance, agent-architecture, mcp-and-tools

Sarthak Aggarwal (DecaWork) argues agents should be governed like employees: each needs an identity, scoped short-lived capabilities, a policy gate outside the model, and receipts plus fast revocation.

- Techniques: Typed plan before evidence (plan-then-execute split); Out-of-model policy gate per tool call; Runtime agent identity card; Short-lived, audience-bound capability tokens
- Tools: Microsoft 365 Copilot, Microsoft Agent 365, Okta, AWS AgentCore Identity, MCP, A2A, Replit

## [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../videos/zrZ1amZBSPw.md)
`zrZ1amZBSPw` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: infra-cost-scaling, governance-compliance

Principal engineer at Twilio on running an LLM gateway in production: per-request fallbacks, per-route latency timeouts, guardrail fail-open/closed choices, load shedding, and centralizing governance without centralizing traffic.

- Techniques: Per-request provider fallback; Cool-down for failing providers; Per-route P99 and timeouts; Hedged requests for the tail; Guardrail time budget and explicit fail mode; Guardrail placement by output type; Bounded queues and load shedding with priorities; Per-route API key segregation; Decentralized traffic, centralized governance

## [Agents Without Code: Skills, YAML, and Filesystems Replaced Python — Philipp Schmid, Google DeepMind](../videos/fjF8EKnxKCU.md)
`fjF8EKnxKCU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: agent-architecture, skills-self-improvement, sandboxing-execution

Philipp Schmid (Google DeepMind) rebuilds one GitHub PR-review agent three ways, moving from a hand-written Python loop to a hosted sandboxed harness driven by markdown files, and argues to delete orchestration code as models improve.

- Techniques: Agents-as-files layout; Bootstrap script for CLI dependencies; Credential injection through a network proxy; Single-call agent turn with server-side loop; Named custom agent; File-based memory and handoffs; Build-to-delete audit
- Tools: Gemini API, Interactions API, Antigravity (agent harness), Google Agent Development Kit (ADK), GitHub CLI (gh), Google Search tool (Gemini API), Google Cloud Storage (GCS) bucket, GitHub repositories as sandbox sources, AI Studio, LangChain Open Deep Research (case reference), Cursor (case reference, speaker says 'Curso'), Manus (case reference, speaker says 'Manos')

## [Build-Time vs. Run-Time: Why Dev Tools Fail in Production — Averi Kitsch & Prerna Kakkar, Google](../videos/9R--1tg45Jg.md)
`9R--1tg45Jg` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: mcp-and-tools, data-engineering

Google's MCP Toolbox team on separating dev-time from production agent tools. Keep credentials, raw SQL and user identity out of agent control, and use predefined, identity-bound, read-only tools.

- Techniques: Source primitive for connection secrets; Predefined custom SQL tools; Read-only enforcement at the driver level; Blast-radius limits on sources; Bounded and authenticated parameters for identity; Read/write tool split with approval gates; Actionable, retryable tool errors and flat inputs
- Tools: MCP Toolbox for Databases, Google Managed MCP, Model Armor, EvalBench, LangChain, Gemini CLI, Claude Code

## [We let an AI agent execute Bash and lived to talk about it — Sarah Sanders, PostHog](../videos/4lXks428C9o.md)
`4lXks428C9o` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: sandboxing-execution, coding-agents

PostHog's Sarah Sanders on securing the PostHog wizard, an agentic CLI with shell access: deterministic enforcement, scanning every content source, and an LLM used only as an advisor.

- Techniques: Deterministic gate ahead of LLM judgment; Detector separated from actor; Scan both ends of the content pipe; Rule anatomy with paired tests; Deny-by-default command allowlist with a vault; Audit for composed attacks
- Tools: YARA, Ink, MCP, PostHog wizard, Warlock, Cursor

## [Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health](../videos/YXEqC05WEI0.md)
`YXEqC05WEI0` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: evals, governance-compliance, observability

Hinge Health's AI lead on shipping member-facing health AI: put irreversible decisions in code above the model, strip PHI at ingestion, monitor live traffic, and verify the judge before fixing the agent.

- Techniques: Code-layer routing above the model; PHI stripping at ingestion with environment and region separation; Layered live scoring of production traffic; Judge-first triage before agent changes; Severity triage for launch decisions

## [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../videos/G7cgLjZtmMU.md)
`G7cgLjZtmMU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: mcp-and-tools, product-ux, evals

Best Buy's Ahnaf Priyo maps the agentic commerce protocol stack (MCP, A2A, ACP, UCP, AP2), argues for pushed product feeds and checkout APIs over browser agents, and makes the case for behavior and protocol evals with a live cat-bakery demo.

- Techniques: Push product feed to platforms; Checkout as an explicit state machine; Scoped, single-use, revocable payment mandate; Layered evals for conversational commerce agents; Timeline view of agent calls; Agent skills for domain roles
- Tools: MCP, A2A, ACP, UCP, AP2, Cerebras, ChatGPT, Gemini, Chrome DevTools

## [AI Agents Are Just Distributed Systems Now — Salman Munaf, TikTok](../videos/hD9-V56FNRI.md)
`hD9-V56FNRI` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: agent-architecture, observability, memory

Talk arguing that once agents call tools and change state, they are distributed systems, so they need idempotency, compensation, scoped permissions, bounded retries and per-step traces.

- Techniques: Idempotency keys plus status lookup on every side-effecting tool; Persist each loop step and define compensation operations; Retry and fanout guardrails; Scoped credentials and tool allowlists; Parameter-bound, expiring human approvals; Memory as a cached, provenance-tagged store; Tool contracts with schemas and idempotency
- Tools: Replit AI agent (cited as a production-database deletion incident; not a tool under review), Air Canada chatbot (cited as an incorrect-refund incident; not a tool under review)

## [AI is the World’s largest Relationship Therapist — Clay Cockrell & Tony Fabrikant, CoupleWork AI](../videos/yoONZwV2smc.md)
`yoONZwV2smc` · AI Engineer · 2026-09-18 · q2 · practitioner · talk · also: evals, product-ux

Clay Cockrell and Tony Fabrikant of CoupleWork AI argue that relationship AI often acts as a sycophantic validation machine, and describe their clinician-led design of Maxine: risk screening, protocol escalation, privacy, and clinician-written evals.

- Techniques: Clinician-first TDD evals; Background risk screen with protocol handoff; Reflect patterns instead of validating; Dogfood the agent for tone drift; Treat sensitive chat data as privileged
- Tools: Gottman Method, Emotionally focused therapy (EFT), Maxine (CoupleWork AI coach)

## [Agents' next frontier: agent-to-agent and network effects — Jean-Denis Greze, Town](../videos/REascnFlq_8.md)
`REascnFlq_8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: multi-agent, rag-retrieval, context-engineering

Jean-Denis Greze (Town CTO) reframes agent-to-agent work as a context-window search problem and compares five ways to get cross-silo data into an LLM call safely.

- Techniques: Benchmark against an ideal single-context agent; Privacy-preserving derived tool; Per-silo sweeper agent; Write-step-only approval for cross-silo queries; Tiered autonomy by sensitivity
- Tools: Gmail, Slack, Airtable, LinkedIn

## [Your Agent Just Authorized What?! — Jay Mok & Ben Coumes, Paypal](../videos/vGn6N4-bxBY.md)
`vGn6N4-bxBY` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: governance-compliance, enterprise-adoption

PayPal's Jay Mok and Ben Coumes propose a stakes-and-counterparty matrix for deciding how much proof an agent's payment authorization needs, ending with verifiable mandates for high-stakes, open-ecosystem transactions.

- Techniques: Stakes x counterparty evidence matrix; Scoped, time-bound, amount-capped mandates; Layered selective-disclosure credentials; Pre-authorize intent before the action target is known; Scoped OAuth access to stored credentials
- Tools: Claude Code, FIDO verifiable intents, AP2 mandate, PayPal approval token, PayPal vault, OAuth, Passkeys, GitHub, Jira, Linear

## [Unlock Agent Autonomy: The Runtime for AI-Native Systems — Tushar Jain, Docker](../videos/zaGyGgLW3SM.md)
`zaGyGgLW3SM` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: sandboxing-execution, mcp-and-tools

Docker's Tushar Jain argues agent safety, not intelligence, is the blocker, and demos a sandbox runtime with stub credentials, scoped per-task sandboxes, and an unbuilt intent-based access prototype.

- Techniques: Run the agent inside an untrusted VM boundary, with policy enforced outside it; Split a monolithic agent into per-task sandboxes; Inject stub credentials, with real secrets added outside the sandbox; Just-in-time narrowed tools over existing MCP servers; Capability escalation through an intent tool; Same policy locally and in the cloud; Parallel fan-out of scoped sandboxes
- Tools: SPX (Docker runtime; name as spoken, install via brew), Docker, Codex (OpenAI coding agent), Claude / Anthropic models, GitHub, Slack, Notion MCP, MCP, OpenClaw (spoken as open claw), OpenCode (spoken as open code), GLM 5.2 (open model)

## [x402 isn’t good (yet) — Jan Curn, Apify](../videos/h6mi88VrPtQ.md)
`h6mi88VrPtQ` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: governance-compliance, mcp-and-tools

Apify's CEO lists x402 agent-payment flaws (double-spend before settlement, HTTP 402 vs MCP 401 conflict, poor fit for metered jobs) and his team's workarounds, including an agent-facing markdown gateway.

- Techniques: Charge-then-refund for metered jobs; Work-after-settlement for near-zero-cost calls; Agent-facing markdown instructions plus prepaid token; Batch micropayments via escrow and signed vouchers; Local wallet with cryptographic key and QR code
- Tools: x402 (Coinbase), MPP (Stripe, Tempo), HTTP 402 Payment Required, MCP, Apify actors, agi.apify.com, Coinbase facilitator

## [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../videos/6pbQgnJ9Voc.md)
`6pbQgnJ9Voc` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, product-ux, mcp-and-tools

Exa's co-founder argues go-to-market is an AI engineering data problem and shows the internal agents, ICP dashboard, and JeffBot clone that run his GTM team.

- Techniques: Decision-log to eval calibration for a personal proxy agent; Caller-scoped agent permissions; Semantic web search as a segmentation pipeline; API/MCP-first, then customize the SaaS; Signal-triggered alerts on customer events
- Tools: Exa, Opus 4.5, Slack, Salesforce MCP

## [Teaching agents to pay — Anna Spysz, Stripe](../videos/A-zeQiYkmXk.md)
`A-zeQiYkmXk` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: mcp-and-tools, governance-compliance, product-ux

Stripe engineer builds an agentic-commerce agent to buy headphones, covering the Universal Commerce Protocol, merchant manifests, shared payment tokens, persona effects on behavior, and a guardrail checklist.

- Techniques: Merchant capabilities manifest at /.well-known; Structured catalog and policy JSON; Attribute-match decision logging; Persona-driven behavior control and A/B testing of system prompts; Scoped payment token instead of raw credentials; Provider-enforced transaction limits; Agent commerce guardrail checklist
- Tools: Universal Commerce Protocol (UCP), Stripe payments, Google Pay, Apple Pay, shared payment token

## [Your company brain will leak secrets: how we stopped it for big banks — Tanmai Gopal, PromptQL](../videos/0uC6u0lJJl4.md)
`0uC6u0lJJl4` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: memory, governance-compliance

Tanmay Gopal (PromptQL) on why a shared company brain leaks secrets and how to gate it: one company-wide markdown wiki with per-page scopes, human-approved agent suggestions, and user credentials injected at tool execution.

- Techniques: Single linked markdown wiki with per-page scopes; Agent suggests, human accepts; Attribute every wiki change to a named human; Per-request user credential injection at the HTTP and SQL layer; Proxy and virtualize real-data access
- Tools: Claude Code, Slack, GitHub, OpenTelemetry, Opus 4.5, PromptQL, Hasura GraphQL engine

## [Tethered: Our Agents Are Us — Shu Fang, Two Sigma](../videos/wCIYViPd4SU.md)
`wCIYViPd4SU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, claude-code, observability

Two Sigma explains how it runs cloud agents as each employee's own identity, using a propagated attribution header and enterprise-grounded web search to cut exfiltration risk.

- Techniques: Run agents as the user identity in existing per-user namespaces; Propagate an attribution header like a trace ID; Deny native web tools and route through enterprise grounding; Enforce tool behaviour with existing harness primitives
- Tools: Claude Code, Google Web Grounding for Enterprise, MCP CLI, Kubernetes, Brave Search (native web tool in Claude Code, per speaker)

## [Tribal Dungeons of Global Shipping: AI Agents at Global Scale — Dmitry Buykin, Maersk](../videos/dQ-_i1tZiws.md)
`dQ-_i1tZiws` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: enterprise-adoption, evals, agent-architecture

Maersk's Dmitry Buykin on running 200+ production shipping agents by turning expert SOPs into executable agent procedures, with a feedback loop that turns each correction into a harness change.

- Techniques: SOP-to-agent conversion; Three-part agent harness; Failure-to-fix mapping; Replay with writes disabled; Trace clustering into heat maps; Composite tools from repeated success; Function-calling tools instead of MCP
- Tools: SME bench (internal triage tool that clusters failures), Function calling

## [When AI Agents Pay and Sellers Monetize: Building x402 Apps on AWS — Anil Nadiminti, AWS](../videos/qTZirYu9pr0.md)
`qTZirYu9pr0` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: governance-compliance, infra-cost-scaling, mcp-and-tools

AWS walkthrough of letting AI agents pay for content via the x402 HTTP 402 protocol, with AgentCore Payments on the buy side and WAF bot pricing on the sell side. Mostly product pitch, with some useful architecture.

- Techniques: Payment session spend caps with expiry; Deterministic payment layer decoupled from the agent loop; Key custody behind KMS, with agent-level capability only; x402 request/402/pay/retry flow; Edge bot classification and differential pricing
- Tools: AgentCore Payments, Bedrock AgentCore Gateway, Bedrock AgentCore Runtime, AWS WAF, Amazon CloudFront, AWS KMS, x402, Coinbase wallets, Stripe wallets, Base (L2 chain)

## [Connect AI to Billions of Legal Documents — Simon Eskildsen, turbopuffer & Jacob Lauritzen, Legora](../videos/V-isu4eTHgw.md)
`V-isu4eTHgw` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: rag-retrieval, infra-cost-scaling, enterprise-adoption

Legora (legal AI) walks through moving project and legal-research search from one Elasticsearch, to Postgres/pgvector, to turbopuffer, one namespace per project on object storage, and why that fits regulated multi-tenant workloads.

- Techniques: Namespace-per-tenant isolation with per-namespace keys and buckets; Partition by access temperature, not by hash; Object-storage-native write path; Round-trip budgeting over object storage; Memory-only cache for encrypted multi-tenant data; Clustered centroid tree for vector search; Two-round-trip inverted index for full text; Fan-out with hierarchy and validity filters for legal research
- Tools: turbopuffer, Elasticsearch, PostgreSQL, pgvector (DiskANN index, transcribed as 'disk NN'), Postgres tsvector, BM25, Amazon S3 (object storage), Google Cloud Storage, Azure Blob Storage, NVMe SSD cache

## [Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic](../videos/rbjWzZK2LU0.md)
`rbjWzZK2LU0` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: governance-compliance, coding-agents

Sachin Malhotra (Anthropic CI) on giving agents budgets instead of tokens: classify verbs by how they fail, cap every write with refilling rate limits, watch aggregates with tripwires, and take identity from infrastructure.

- Techniques: Verb triage by failure visibility; Break-glass verbs with proxy-stamped audit; Refilling per-write rate limits with scope-sized budgets; Bypass that asks the human inside agent sessions; Aggregate tripwires paired with context fixes; Undo test for sizing controls; Identity stamping at the proxy with inherited labels; Two-layer policy: text plus deterministic proxy
- Tools: Kubernetes, admission webhook, Slack, Claude Code

## [1 Trillion Phone Calls/yr, 10% Error rate: The Crisis in Voice AI — Sumanyu Sharma, Hamming AI](../videos/qStB9GbppMU.md)
`qStB9GbppMU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: voice-multimodal, evals, observability

Hamming AI's CEO argues voice agent errors (about 10% in practice) are the top deployment blocker, and offers a loop to find, prioritise, test and red-team failures across many calls.

- Techniques: Frequency and severity triage matrix; Scenario-variation regression testing; Production A/B testing for voice fixes; Cross-conversation pattern analysis; Continuous adversarial red-teaming

## [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents — Christopher Lovejoy & Saul Howard](../videos/mav15aW9lLM.md)
`mav15aW9lLM` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: governance-compliance, enterprise-adoption, evals

Christopher Lovejoy (Anthropic) and Saul Howard (Anterior) argue that enterprise AI agents need audit, data-boundary, escalation and eval primitives designed in from the start, not bolted onto a proof of concept.

- Techniques: Immutable append-only event log as system of record; Event log plus schema-driven immutable blob store; Token-based access at point of use; Human-agent equivalency in the action model; Replay plus human-vs-agent diff as eval; Run evals inside the customer environment

## [Agent Spending Without Controls — Rodrigo Coelho & Pranav Maheshwari, Edge & Node](../videos/ZyGMqdIpPoE.md)
`ZyGMqdIpPoE` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: governance-compliance, mcp-and-tools

Edge & Node's pitch for Ampersend, a payment and compliance layer letting agents pay for paid MCP tools and checkouts, with a sanctions-screening demo. Mostly product pitch.

- Techniques: Pre-authorization counterparty screening; Skill file as the payment-aware tool gateway; Per-call micropayment for paywalled endpoints; Prompt-level spend constraint
- Tools: x402, Shopify UCP, TRM (wallet screening), MCP, Claude Code, Claude Cowork, Ampersend, Exa, Firecrawl, Circle nano-payments

## [Beyond the Lethal Trifecta: Agentic Commerce on the Open Internet — David Levine, Kiduna Club](../videos/tE2z8-hqoLY.md)
`tE2z8-hqoLY` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: governance-compliance, multi-agent

Founder talk on the "lethal trifecta" (private data + untrusted content + actions) and a proposed fix: agents as identity-bearing members of legally registered, blockchain-verified organizations. Mostly a pitch for Kaduna Club.

- Techniques: Ally build sequence (inform, instruct, empower, enact, align); Scoped identity tokens for agents (JWT with claims); Decision markets for policy; Per-action audit trail back to a responsible principal
- Tools: OpenCloud (caption spelling; likely OpenClaw, an agent product that the speaker says blew up in January 2026), MOO / LambdaMOO (text-based virtual world the speaker used in 1993), MCP servers (cited as a way enterprises integrate agents), Slack, Salesforce, Notion, Telegram, Twitter, JWT, Vector database (generic, no product named), Blockchain (generic, no chain named), Polymarket (cited as an analogy for decision markets)

## [Which AI startups actually land enterprise contracts? — Brian Lewis, Millennium](../videos/7A65O-0lvKE.md)
`7A65O-0lvKE` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, governance-compliance, product-ux

A buyer at a hedge fund explains why most AI startup pilots fail: value, security, reliability and legal gaps, not model quality. He argues most AI-native work is unglamorous data, architecture and change management.

- Techniques: Enterprise-readiness intake checklist for vendors; Verify retention claims in a pilot, not on paper; Gate features by group and by release; Track documentation and terms as versioned artifacts; Set buyer-written success criteria and a 90-day plan that deploys into the buyer's own cloud; Build-versus-buy check on vendor pitches; Breach-response question as a red flag test

## [Claude is watermarking AI text: Everything you need to know](../videos/EWGDJqlYlA8.md)
`EWGDJqlYlA8` · Kai Explains · 2026-09-02 · q3 · practitioner · news · also: governance-compliance, models-research

Explainer on Anthropic's announced machine-readable watermarking of Claude text: the likely statistical mechanism, what it detects, how fragile it is, and why the EU AI Act is the trigger.

- Techniques: Keyed green-list token biasing (watermark generation, as described); Z-score detection on the green fraction; Base-rate check before acting on any detector; Robustness testing of provenance signals
- Tools: Claude, claude.ai, Claude API, Claude Code, Claude Cowork, Claude on AWS, Claude on Google Cloud, Claude on Microsoft Foundry, Gemini, GPT, EU AI Act (regulation, Article 50), Dipper study (paraphrase attack study)

## [Ox Alpha is Lying to You!](../videos/kFajz5bNO6M.md)
`kFajz5bNO6M` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: models-research, evals, governance-compliance

Kai investigates "Stealth Ox Alpha", a free OpenRouter model with no stated developer, using tokenizer offsets, error strings and a leaked system prompt; he concludes the evidence points to GLM but is unproven.

- Techniques: Tokenizer offset fingerprinting; Error-string matching; Temperature-zero output comparison; Controlled video token test; Report benchmark counts with intervals; Cost and time comparison on a fixed build task; Check retention claims at both the aggregator and the provider
- Tools: OpenRouter, OpenCode, GLM 5.3 (Zhipu), GLM-5, Gemini 2.5 Pro, GPT-4o, Claude Fable, Claude Code, Hermes Agent, DeepSeek Harness, Grok, DeepSeek

## [Deepseek Harness: Not What You Think](../videos/y0BW4hpMpyM.md)
`y0BW4hpMpyM` · Kai Explains · 2026-09-02 · q4 · practitioner · review · also: evals, agent-architecture, token-cost-efficiency

Kai Explains on DeepSeek's open harness: benchmark scores are model-plus-harness pairs, the harness can move scores 5-8 points, and its append-only, cache-stable context design is the most reusable idea, alongside licensing and security concerns.

- Techniques: Report scores as model-plus-harness pairs; Append-only event log with a rebuilt, frozen message history; Cache-stable summarization and compaction; Track cache-hit rate per agent session
- Tools: DeepSeek Harness (DeepSeek's open-source agent harness, version 0.1, MIT license per the host), DeepSeek V4 Pro (pricing mentioned), Terminal Bench (public leaderboard at TBench AI, Terminus 2 research harness), Gemini 3 Pro, Gemini 3.1 Pro, Gemini CLI, Claude Code, Claude Agent SDK (pinned at 0.3 per the host), Claude Code 2.1 (bundled in the sub-agent payload), Opus 5 (as captioned), Fable 5 (as captioned), Codex CLI

## [This Open-Source Tool Fixes Browser History (Hister)](../videos/NMk9XVNTygA.md)
`NMk9XVNTygA` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: dev-tools, rag-retrieval

Hister is a self-hosted tool that indexes the full rendered text of every page you read in Chrome or Firefox, so you can search your browsing by content; useful, but pre-1.0 with real security gaps.

- Techniques: Local recall index for your own reading; Scoped full-text queries; Backfilling from existing browser history; Hardening before exposure; Agent access to a personal reading index
- Tools: Hister, Chrome extension for Hister, Firefox extension for Hister, Docker (multi-arch image), Nix flake (Darwin module), MCP, Karakeep (transcribed as 'Para Keep', 28k stars), ArchiveBox, Wallabag, Readwise Reader, Gatekeeper (macOS)

## [YC Just Open-Sourced Its Multiplayer Harness](../videos/GrZ-X3-2TVs.md)
`GrZ-X3-2TVs` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: agent-architecture, enterprise-adoption, coding-agents

Better Stack's hands-on tour of YC's open-source "multiplayer" agent harness (QM): a self-hosted, multi-user web app with Slack access, per-workspace containers, a seven-tool surface and org-level approval modes. Promising but two weeks old.

- Techniques: Minimal primitive tool surface plus shell sandbox; Org ceiling with per-team tightening and a posture-independent command deny list; Enable extra harnesses through the admin API; Share context through a team project, keep credentials private by default
- Tools: QM (YC open-source multiplayer agent harness; the caption spelling may be off, and the repo was about two weeks old at the video date), pi (the default agent harness in QM), Claude Code (can be enabled as a harness inside QM), Slack (integration surface), PostgreSQL (session history), GitHub (repo linked in the description)

## [Claude Now Watermarks Its Text. How is it Possible?](../videos/cX0xI5FpH3U.md)
`cX0xI5FpH3U` · Kai Explains · 2026-09-02 · q4 · practitioner · news · also: governance-compliance, inference-serving, models-research

Kai Explains on how Anthropic's text watermark works (sampler-side, keyed tournament sampling, no added characters), why detection and spoofing numbers are unpublished, and what engineers should actually do about it.

- Techniques: Tournament sampling for keyed watermarks; Keyed detection by re-deriving scores; Provenance by drafts and version history; Control the mark by running an open-weight model locally; Check provider support for provenance metadata before relying on it; Avoid invisible-character and character-swap tricks
- Tools: Claude (Anthropic API), Claude 4.7 (sampling parameter restriction mentioned), SynthID-Text (Google DeepMind; transcribed as 'Synth ID text'), Gemini (DeepMind watermark user study), GPTZero (transcribed as 'GPT-0'), Pangram, Turnitin, Amazon Bedrock, Google Cloud, Microsoft Foundry, C2PA-style signed provenance metadata (transcribed as 'C2 Pascal'), Digits of pi (Anthropic's Monopoly analogy)

## [MCP is Dead...](../videos/Rrju5Y0iiBM.md)
`Rrju5Y0iiBM` · Kai Explains · 2026-09-02 · q3 · practitioner · news · also: mcp-and-tools, context-engineering

Kai Explains argues "MCP is dead" misreads the moment: the protocol's own pain points (tool-definition context bloat, session state) were real, and a July 2026 spec rewrite addresses them, while adoption kept growing.

- Techniques: Cap the number of MCP servers attached to an agent; Diagnose tool-definition bloat before blaming the protocol; Design remote MCP servers to be stateless for load balancing; Vet community MCP servers before installing
- Tools: Model Context Protocol (MCP) with July 28 2026 spec, MCP SDKs (Anthropic-maintained; one other SDK referenced), GitHub MCP server, Filesystem MCP server, Notion (database connector), Hyperframes (video framework), Google Cloud managed remote MCP servers, JetBrains, Cursor, Windsurf, Replit

## [Anthropic's Model Hardware Standard: Everything You Need To Know](../videos/UEd-I_67qJI.md)
`UEd-I_67qJI` · Kai Explains · 2026-09-02 · q3 · intro · news · also: mcp-and-tools, agent-architecture, models-research

Explainer on Anthropic's Model Hardware Standard (MHS), an MCP-like interface for lab and physical devices, with Carnegie Mellon, Quera and Genentech field results and the main criticisms.

- Techniques: Self-describing device declaration for agent-written drivers; Enforce hard limits in the device or interface layer, not in the prompt; Fault-injection test of the safety layer; Agent-side data-quality check and re-run loop; Report unresolved causes instead of claiming a fix; Three invocation modes for the same device
- Tools: Anthropic Model Hardware Standard (MHS), Model Context Protocol (MCP), Claude Opus 4.8, SiLA (gRPC), OPC UA, Tango, BlueSky, QCoDeS, ROS, PyLabRobot, MATLAB, Python

## [We Vetted 2000 AI Skills Before They Reached Developers — Lucas Palma, Nubank](../videos/iKQ78wyJEXU.md)
`iKQ78wyJEXU` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: skills-self-improvement, pr-code-review, governance-compliance

Nubank's product security team built SkillVector, a CI scanner that vets internal AI skills (hybrid regex plus LLM) before they reach an internal marketplace, and reports 2,000+ skills scanned.

- Techniques: Three-point skill scanning; Hybrid deterministic plus LLM review; Findings as PR comments plus SARIF; Historical back-scan; Verify approval gates, not model confirmations
- Tools: SkillVector (spoken as 'SkillVetor' in the transcript), SARIF, Regex-based determinstic scanners, LLM reviewer, Internal skills marketplace

## [Open Source Is Dead. Long Live Open Source. — Saoud Rizwan, Cline](../videos/CoEIs6Xm8m8.md)
`CoEIs6Xm8m8` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: token-cost-efficiency, infra-cost-scaling, models-research

Cline's founder argues open-weight models plus verification-heavy agent harnesses will win on cost as closed labs subsidize subscriptions for lock-in, citing a supply-chain attack and spend data.

- Techniques: Put quality in the harness, not the model; Default route to cheaper open-weight models in an internal gateway; Head-to-head test on a real bug from your own repo; Set usage limits per user on the provider dashboard
- Tools: Claude Code, Codex, Cursor, Cline, LiteLLM, GLM, Kimi, DeepSeek, Opus, Open Compute

## [Gadgets: Personal app vibe coding that is actually safe — Kenton Varda, Cloudflare](../videos/RmS5s6Wbin4.md)
`RmS5s6Wbin4` · AI Engineer · 2026-08-18 · q3 · practitioner · demo · also: vibe-coding-app-building, sandboxing-execution, product-ux

Kenton Varda (Cloudflare) argues personal AI codegen needs new infrastructure, and demos "Gadgets": per-user apps with platform-enforced sharing and sandboxed generated code, run on open-source workerd.

- Techniques: Platform-enforced sharing via single-purpose instances; Sandboxed generated UI with postMessage-only RPC; Give the agent the app source and a brief, let it add primitives; Export code-only templates (blueprints); Run the production runtime locally
- Tools: Cloudflare Workers, Durable Objects, Dynamic Workers, workerd, Claude, Cap'n Web RPC

## [Bringing agents onto the world wide web — Paul Klein IV, Browserbase](../videos/GqoNrUz8hEU.md)
`GqoNrUz8hEU` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: voice-multimodal, agent-architecture, mcp-and-tools

Paul Klein (Browserbase) argues reliable browser agents are a harness, tooling and infrastructure problem rather than a model problem, and lays out a multimodal, harness-engineered, consistently hosted approach.

- Techniques: Hybrid code-plus-browser execution; Per-site skill packs loaded before visiting; Compressed page representation; Pinned, consistent browser environment; Sites expose WebMCP tool calls and agent-first auth; Observability-to-self-improvement loop
- Tools: Browserbase, Browse.sh, WebMCP, Playwright CLI, Claude Code, Operator, Cursor, Factory, OpenClaw, WorkOS AuthMD, web bot auth, auto-browse

## [Wearing the Agent: From Group Chats to Glasses — Sai Krishna Rallabandi](../videos/s67bE2Ur3bY.md)
`s67bE2Ur3bY` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: memory, multi-agent

Sai Krishna Rallabandi on moving agents from one-user assistants to group-chat and wearable agents. Covers the security boundary, memory curation and forgetting, privacy as context, and when to speak.

- Techniques: Action-boundary deterministic guard; Data/instruction channel split with a trained SLM; Atomic fact extraction with hierarchical and temporal links; Continuous relevance scorer for forgetting; Per-user LoRA adapters over a shared memory layer; KV-cache aware memory ingestion; Learned speak/stay-quiet classifier; Private routing via DM
- Tools: LoRA, SLM classifier, regex and traditional NLP guards

## [Security Track Intro — Randall Degges, Snyk](../videos/2xJoimgoqBg.md)
`2xJoimgoqBg` · AI Engineer · 2026-08-18 · q2 · intro · keynote · also: coding-agents

Snyk's Randall Degges opens the World's Fair security track: AI-written code has security bugs, autonomous agents need containment, and model access limits are a barrier to shipping fearlessly.
- Tools: Fable (AI model, access reportedly pulled; name as spoken), OpenAI GPT 5.6 (new model, speaker says it is not available to many yet)

## [Why Agentic Systems Need Ontologies — Frank Coyle, UC Berkeley](../videos/Sir59K8ZDPU.md)
`Sir59K8ZDPU` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: agent-architecture, data-engineering

Frank Coyle argues agents need ontologies as a symbolic validator around LLM tool loops, checking outputs against domain constraints before acting.

- Techniques: Validator gate after each tool call; Two-layer boundary checks (Pydantic plus ontology); Side-effect-free planning, then commit; OWL constraints for business rules; Reuse existing vocabularies; Bounding and monitoring agent loops
- Tools: Claude API (Python client, stop_reason tool-use loop), Pydantic, OWL, RDFS, schema.org, DBpedia, Dublin Core, FOAF

## [Security Firewall for Agents — Ryan Dahl, Deno](../videos/MkRYPFIMCSA.md)
`MkRYPFIMCSA` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: infra-cost-scaling, governance-compliance

Ryan Dahl (Deno) on Claw Patrol, an open-source byte-level egress proxy that gates what production agents send to databases, Kubernetes and SaaS, with rules, credential injection and human or LLM approval.

- Techniques: Byte-level egress proxy for agents; Credential injection at the proxy; Policy-as-code in HCL with Git review; Chained verdicts: rule, LLM judge, then human approval; Network-level placement with existing identity
- Tools: OpenClaw, Claw Patrol, Deno Deploy, PostgreSQL, Kubernetes, ClickHouse, AWS (Sigv4), GitHub, Slack, PagerDuty, HCL, Terraform

## [Teaching AI to Find Real Vulnerabilities — Prof. David Brumley, Bugcrowd](../videos/ZFxh7sqbUZo.md)
`ZFxh7sqbUZo` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: training-finetuning-rl, evals

David Brumley (CMU, Bugcrowd) on designing RL environments for vulnerability discovery and exploitation, using deterministic oracles, an open-world "audit" task scored by precision and recall, and a 16-rung capability ladder run against V8.

- Techniques: Deterministic witness-based grading; Open-world audit task with dedup and precision/recall; Capability ladder for hard targets; Withhold the answer key and the most dangerous artifacts
- Tools: MCP (exposed setup, read/write, and grading tools), Docker, exploitbench.ai, V8, AIxCC, DARPA Cyber Grand Challenge, SciBench, CyberGym, BountyBench

## [From RL to IRL — Gaurav Mishra, Amazon AGI Lab](../videos/Cc0_nyxROBA.md)
`Cc0_nyxROBA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: voice-multimodal, training-finetuning-rl, agent-architecture

Gaurav Mishra (Amazon AGI Lab) on why RL-trained computer-use agents break on real login screens, ads, and expired sessions, and how to adapt training and the harness to real-world messiness.

- Techniques: Simulated messy environments for agent RL; Recovery as a native model action; Process reward model over the trajectory; Action risk classifier in the harness; Harness-level credential and loop guardrails; Checkpoint, rollback, and audit trail; Forced human handoff; Adversarial tasks in mainstream training; Design-partner failure loop
- Tools: Playwright, WebMCP, MCP, web search APIs, PPO, GRPO

## [Agents Need Receipts, Not More Tool Calls - Armanas Povilionis, Alithea Bio](../videos/Fu45geO3zX8.md)
`Fu45geO3zX8` · AI Engineer · 2026-08-18 · q2 · practitioner · talk · also: multi-agent, mcp-and-tools

Armanas Povilionis (Alithea Bio) argues that cross-organization agent work needs signed, verifiable receipts, and demos Froglet, an open protocol for agents to discover, buy and verify services.

- Techniques: Signed per-step receipts for agent transactions; Marketplace as discovery only, direct peer deals; Same node, role chosen at runtime; Typed payload with schema and deal ID, polled asynchronously; Expose the protocol through MCP and let the LLM drive it
- Tools: Froglet, MCP, Claude, Docker, OpenClaw, NemoClaw

## [Through the AI Fog: The Architectural Decision Agentic Security Depends On — Manoj Nair, Snyk](../videos/1EZdpEhwmNc.md)
`1EZdpEhwmNc` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: coding-agents, mcp-and-tools, evals

Snyk's CTO argues agent security needs deterministic checks alongside LLMs, with customer data on attacks, toxic skills and MCP servers, plus a live coding-agent demo.

- Techniques: Hybrid LLM plus deterministic security checks; Repeated-run recall measurement; Pre-install package health gate; Skill and MCP risk assessment before adoption; Per-model red-team suite; Breakability-aware automated remediation; Deterministic invocation through a skill or hook
- Tools: Claude Code, Cursor Cloud, Codex, Snyk Studio, Snyk Evo, Snyk package health check

## [The Model Was Right. The Harness Failed. — Vinoth Govindarajan, OpenAI](../videos/BInpv7lGp1o.md)
`BInpv7lGp1o` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: agent-architecture, observability

Agent production failures are mostly harness failures, not model failures; the talk gives a state-ownership, ordered-commit, lifecycle, authority and receipt framework, using OpenClaw incidents as case studies.

- Techniques: Session lane / single ordered writer; Run deadlines, cancellation and watchdog; Scoped approval object; Run receipt as the audit record; Idempotency keys on side effects; Verify at the user-visible edge; Five-question production audit
- Tools: OpenClaw, OpenAI Agents SDK, Codex, Cursor, OpenCode, Claude Code, Hermes, Telegram

## [AI’s Jurassic Park Period — Aaron Stanley, dbt Labs](../videos/1lgFGaHoGq8.md)
`1lgFGaHoGq8` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: governance-compliance, agent-architecture

Aaron Stanley (CISO, former forensic consultant) argues that agents routing around constraints is the hidden risk, and proposes a corrigible, four-layer defense: deterministic floor, halt-and-explain agent, adversary agent, and structured human escalation.

- Techniques: Halt-and-explain default for constraint conflicts; Equal-power adversary agent reviewing worker actions; Natural-language escalation to humans; Layered deterministic floor; Intercept at the harness or tool-call hook; Runtime input policies instead of output string matching
- Tools: gVisor, egress filters, Chrome extension (installation blocked by a layered control)

## [Full Workshop: Better Auth — Paola Estefania, Better Auth](../videos/JvKO40CFq-s.md)
`JvKO40CFq-s` · AI Engineer · 2026-08-18 · q3 · practitioner · workshop · also: mcp-and-tools, governance-compliance

Paola Estefania (Better Auth) argues agents should get their own identity and scoped capabilities instead of borrowing user credentials, and demos a draft open protocol with approvals, audit logs and revocation.

- Techniques: Per-agent identity with own key pair; Capability grants with default-read policy; Device-flow approval for agents; OpenAPI-to-capability translation; Full revocation: agent, host and tokens
- Tools: MCP, OAuth, OpenAPI, OIDC, Gmail, Notion, Claude, Cursor

## [Privacy-Preserving Intelligence — Steve Korshakov, Bee (acq. Amazon)](../videos/IvE8n-ylFYY.md)
`IvE8n-ylFYY` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: sandboxing-execution, governance-compliance, agent-architecture

Steve Korshakov (Bee, acquired by Amazon) explains how an always-on personal-agent wearable keeps data unreadable even to its own company, using client-held keys, attested workloads, and two-tier release controls.

- Techniques: Client-held keys with attested key release; Forced key expiry window; Split base image and deployment manifest; Private CA for internal attestation certificates; Minimal, auditable trusted code base; Per-agent sandbox with minimal capabilities
- Tools: Sigstore-style transparency log (auto-caption reads as 'six store'), Confidential compute nodes, Private certificate authority, OpenClaw (auto-caption reads as 'open claw'), Claude Code (auto-caption reads as 'cloud code')

## [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans — Corey Gallon, Rexmore](../videos/26RtyAm9y_Q.md)
`26RtyAm9y_Q` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: voice-multimodal, mcp-and-tools, agent-architecture

Corey Gallon on driving websites with agents via a shell CLI over the Chrome DevTools Protocol, climbing from synthetic clicks to trusted input to human-like motion, and beating Cloudflare Turnstile, MT Capture, Lemin and reCAPTCHA v2.

- Techniques: CLI over MCP for repeatable browser tasks; Cross-channel verification after each action; Lowest-rung escalation; Coordinate-based trusted click through closed shadow roots and cross-origin iframes; Solver plus operator split; Explore, then codify
- Tools: Chrome DevTools Protocol (CDP), Chrome Agent (speaker's Python CLI), Cloudflare Turnstile, MT Capture, Lemin (auto-captioned as 'lemon'), reCAPTCHA v2, Outlook web client

## [Notion's Token Town — Sarah Sachs, Notion](../videos/-I5W5QVAT8E.md)
`-I5W5QVAT8E` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: token-cost-efficiency, infra-cost-scaling, enterprise-adoption

Notion's head of AI engineering on keeping AI costs sustainable: stay model-agnostic, route traffic by task difficulty, use open-weight and plain code for simple steps, and evaluate whole trajectories instead of single calls.

- Techniques: Model-agnostic harness with an auto-router; Traffic tiering by task difficulty; Trajectory-level eval of cost, latency and success; Open-weight evaluation on your own system; Code and CLI for deterministic steps; Cross-vendor review chain for agent PRs; Lethal trifecta check on agent systems
- Tools: Claude Code, Claude, Codex, Decagon, Parallel (web search provider), Notion Workers, Notion AI Manage Agent, Kimi 2.6 (as transcribed), GLM 5.2 (as transcribed), GPT 5.2 (as transcribed)

## [Vending-Bench: Long-Horizon Agent Evals — Lukas Petersson, Andon Labs](../videos/cO8qC6HBuBg.md)
`cO8qC6HBuBg` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, models-research

Lukas Petersson (Andon Labs) on Vending-Bench, emergent misbehavior in agents, and moving evals into real-world deployments and forked simulations, because models act differently once they suspect a simulation.

- Techniques: Incentive-based misbehavior probing; Forked real-environment evals; Simulation-awareness probe; Cross-model replay of a real incident
- Tools: Vending-Bench, Vending-Bench Arena (arena mode), Claude / Opus 4.6, 4.7, 4.8, Fable (named in talk, may be a caption error), GLM 5.2, GPT 5.5, Gemini, Grok 4.3, Kimi, Slack (channel used to message the store agents), LinkedIn, Indeed

## [Training Frontier Models to Out-Think Hackers — Uri Rolls, Arithmetic & Thom Wolf, Hugging Face](../videos/O-CBZ3JtRvo.md)
`O-CBZ3JtRvo` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, training-finetuning-rl, models-research

Uri Rolls and Thom Wolf present Arithmetic's "Mask Off" benchmark: black-box access-control exploit chains built from real zero-days, graded per step, to test whether models can make logic leaps.

- Techniques: Black-box exploit-chain environments from self-found zero-days; Per-step deterministic graders with partial credit; Trace review as the main eval loop; Orchestrator for running evals
- Tools: Bach (Arithmetic's internal eval orchestrator)

## [Agentic Development Security — Ezra Tanzer, Snyk](../videos/cgimkNGNjvU.md)
`cgimkNGNjvU` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: claude-code, coding-agents, skills-self-improvement

Snyk on securing agent development in three pillars: the code agents generate, the skills and MCP servers they use, and the actions they take. Mainly a product showcase, with a useful hook-based scanning pattern.

- Techniques: Async post-write scan hook with deferred fix at stop; Steer vs ask policy actions in pre-tool hooks; Static scan of skills and MCP tool descriptions; Per-workspace guardrail profiles
- Tools: Snyk, Claude Code, Codex, Cursor, MCP, Python hooks, VS Code, Electron, ClawHub

## [Why Your Agent Disagrees With Itself (And What To Do About It) - Diane Lin, Datadog](../videos/wEc9aG7cRQc.md)
`wEc9aG7cRQc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, memory

Diane Lin (Datadog) on why LLM agents give different verdicts on the same input near the decision boundary, and how to fix it with disagreement-driven active learning plus episodic and semantic memory instead of fine-tuning.

- Techniques: Measure consistency with repeated runs; Disagreement-based query selection; Semantic memory for policy and preference facts; Episodic memory as case-based precedent lookup; Active-learning loop with memory updates
- Tools: Datadog

## [You Didn't Ship a Bug. You Just Wrote It for a Human. - Ravi Madabhushi, Scalekit](../videos/lMCxVorb9wM.md)
`lMCxVorb9wM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: mcp-and-tools, governance-compliance

Ravi Madabhushi (Scalekit) argues agents break the human and service-account identity model: they need a distinct identity bound to a principal, fine-grained time-bound scopes, and full action audit, beyond OAuth.

- Techniques: Coalesce high-frequency timestamp writes; Bind agent identity to principal; Context-filtered MCP tool surface; Least-privilege, time-bound, just-in-time grants; Full-provenance action audit
- Tools: OAuth, SPIFFE, MCP, Gmail API, Salesforce API, Databricks, HubSpot, Notion

## [Evals-Driven Development for a Mental Health AI Coach — Akele Reed & Dave Revere, SonderMind](../videos/O72p-rBb2bA.md)
`O72p-rBb2bA` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: evals, enterprise-adoption

SonderMind engineers describe the guardrail, eval and clinician-annotation loop behind Sonder, a clinically grounded mental health AI coach, and open-source 300 scenarios for it.

- Techniques: Pre- and post-LLM guardrail sandwich; Trace-to-typed-eval annotation loop; Multi-metric guardrail scoring
- Tools: Sonder (SonderMind's clinical AI coach), LLM-as-judge guardrail calls, CI-gated eval suite, annotation queue with trace replay, analytics and alerting platform

## [Your LLM Stack Is a 2008 Database With Better Marketing — Lovina Dmello, NVIDIA](../videos/XjI-AR4pt7Y.md)
`XjI-AR4pt7Y` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: infra-cost-scaling, governance-compliance

Production ML breaches are mostly boring misconfigurations, not AI attacks; the talk argues for layered infra security, a maturity model, and budgeting guardrails by latency overhead tier.

- Techniques: Tiered guardrail budget; Maturity self-assessment with overhead budgets; Least privilege with short-lived credentials; Segment by service identity, not network location; Secrets and model artifacts hygiene; Treat ML infra like a database
- Tools: Ray, NIST AI RMF

## [It's 10pm. Do You Know Where Your Agents Are? — Kim Maida, Keycard](../videos/I3znWC3MEXM.md)
`I3znWC3MEXM` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: mcp-and-tools, governance-compliance, agent-architecture

Kim Maida (Keycard) shows why API keys give agents overprivileged, unattributed access, and how OAuth token exchange (RFC 8693) per tool call, with policy checked before minting, fixes it.

- Techniques: Per-tool-call token exchange (RFC 8693); Policy-before-mint; Policy-gated human approval; Ephemeral, audience-bound bearer tokens; Layered scope design
- Tools: Keycard (security token service and policy governance), OAuth 2.0 token exchange (RFC 8693), Google sign-in (identity provider in demo), MCP (client, server, gateway)

## [Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town](../videos/yWS0udrIOc8.md)
`yWS0udrIOc8` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: pr-code-review, multi-agent

Steve Yegge argues AI-generated code multiplies security defects and new attack types (slopsquatting, prompt injection, agent credentials), and urges security scanning at generation time and as a separate pass.

- Techniques: Surface security findings at generation time; Separate security and correctness into different passes; Run several scanners and have agents cross-check; Supply-chain vetting of dependencies and base images; Adversarial supervisor agents for queue-driven agents; Least-privilege credentials per agent action
- Tools: Claude Code, Beads, Gas Town, Snyk (called Sneak in captions), Chainguard

## [The UX of AI: Making AI-Powered Apps Your Users Don't Hate - Kathryn Grayson Nanz, Progress Software](../videos/L3RuP_q8Bwc.md)
`L3RuP_q8Bwc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: product-ux

Kathryn Grayson Nanz (Progress Software) on designing AI features users trust. Organizes UX problems into five areas (trust, clarity, control, transparency, meaningful benefit) and gives concrete UI patterns for each.

- Techniques: Source citations with graded surfaces; Plan approval before agent execution; AI content labeling; Streaming and visible reasoning; Change highlighting; Prominent kill switch; Task-scaled version history; Granular revocable permissions; Pre-approval cost and time estimates; Guided starts and next-step actions
- Tools: Claude, ChatGPT, Microsoft Copilot, Microsoft Teams

## [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../videos/iQ5xldZ9StU.md)
`iQ5xldZ9StU` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: software-factory, coding-agents, sandboxing-execution

GitHub Next demos Agentic Workflows (markdown playbooks compiled to Actions with deterministic guardrails) and ACE, a cloud multiplayer dev environment where humans and agents share chat and plans.

- Techniques: Markdown playbook compiled to CI workflow; Declarative guardrail front matter; Secret brokering outside the agent sandbox; Staged, logged writes; Swarm of role-specific workflows; Shared cloud session per branch with team chat as context; Shared markdown plan as contract; Automation triage by stack trace origin
- Tools: GitHub Copilot, GitHub Actions, Dependabot, Astro, Cloudflare, ACE (GitHub Next prototype)

## [We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3](../videos/LqLoYksJ6do.md)
`LqLoYksJ6do` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: sandboxing-execution, software-factory

Form3's Moritz Johner describes PatchPilot, an agent that patches CVEs across thousands of repos, and why production credentials make a coding agent a supply-chain actor needing deterministic controls, credential splits, and microVM isolation.

- Techniques: Deterministic controller plus scoped agent steps; Minimal change-set instruction plus post-agent vetting; Bounded CI-fix loop with human escalation; End-of-run retrospective aggregated across runs; Planted-injection end-to-end tests as evals; MicroVM sandbox with a policed egress path
- Tools: PatchPilot, Dependabot, Renovate, Firecracker, Docker, Kaniko, BuildKit, Landlock, bubblewrap, Go, Slack, GitHub

## [I Let Strix Attack My App... Here’s What It Found](../videos/vRTliPb8fjg.md)
`vRTliPb8fjg` · Better Stack · 2026-08-02 · q3 · intro · review · also: pr-code-review, sandboxing-execution

Short Better Stack review of Strix, an open-source multi-agent pen-testing tool that attacks a web app or API in a Docker sandbox and returns validated exploits and fix PRs, with real limits on cost, speed and complex attacks.

- Techniques: Scan code and live target together in one run; CI merge gate on validated findings; Triage on proof, not on maybes; Match model strength to scan depth and budget
- Tools: Strix, Docker, Anthropic API (Claude), Gemini, Ollama, GitHub Actions, FastAPI (demo app), XBEN exploitation benchmark, OWASP Top 10

## [Model Distillation: How to Steal a Billion-Dollar AI](../videos/gacMZf5rqYA.md)
`gacMZf5rqYA` · Kai Explains · 2026-08-02 · q3 · practitioner · other · also: training-finetuning-rl, models-research, local-ai

Explainer on model distillation: how small students copy frontier models via API outputs, the DeepSeek R1 and budget-reasoning examples, the capability gaps that remain, and reported extraction campaigns.

- Techniques: White-box soft-label distillation; Black-box distillation via API sampling; Reasoning-trace fine-tuning of an open base; Small curated dataset recipe (S1-style); Append 'Wait' to extend reasoning at inference; Paraphrase robustness check for memorization; Size the local student to the GPU
- Tools: DeepSeek-R1, Qwen (32B, 14B, 7B distilled variants), OpenAI o1-mini, OpenAI o1-preview, OpenAI ChatGPT, Google Gemini, Sky-T1 (Berkeley), S1 (Stanford / University of Washington), Alma (local model runner, as named), OpenRouter, Hugging Face model cards, AIME 2024 benchmark

## [Jack Dorsey's New App Is Coming for Slack and GitHub (buzz)](../videos/CHEMPZ87FLw.md)
`CHEMPZ87FLw` · Better Stack · 2026-08-02 · q3 · intro · review · also: multi-agent, coding-agents, token-cost-efficiency

Hands-on walkthrough of Block's open-source Buzz, a Slack-like workspace for humans and AI agents built on Nostr with signed audit trails. Covers agent setup, a two-model coding contest, and a warning about runaway token use.

- Techniques: Bootstrap a Buzz community; Custom agent with persona, harness and model; Head-to-head model contest, then cross-model audit; Stop runaway multi-agent loops
- Tools: Buzz, Nostr protocol (the video says 'Noster'), Nostr relay (Block's hosted relay, in beta), BitChat (Bluetooth mesh app that adopted Nostr 2 as a fallback transport), Agent Client Protocol, Claude Code, OpenAI Codex, Goose (Block's agent framework), OpenRouter, Gemini 3.6 Flash (as named in the video), GLM 5.2 (as named in the video), GPT 5.6 Sol (as named in the video)

## [Gemini 3.6 Flash, 3.5 Flash-Lite, & 3.5 Flash Cyber, Fugu Cyber, Qwen Audio, Audex & More AI News](../videos/pJcCPsa5IbY.md)
`pJcCPsa5IbY` · Kai Explains · 2026-08-02 · q3 · intro · news · also: models-research, local-ai, voice-multimodal

Weekly AI news (Aug 2026): Gemini 3.6 Flash and 3.5 Flash-Lite, Poolside's open 118B Laguna S2.1 with published trajectories, Microsoft's 4B MageFlow, plus audio, cyber and humanoid launches. Mostly vendor claims; Poolside's transparency stands out.

- Techniques: Wrap a frozen policy in a planner with memory (Harness VLA); Publish every trial's trajectory for benchmark claims (Poolside); Thinking on/off ablation on the same benchmark; Agent optimizes its own harness in an automated research loop; Fit check before running an image model locally
- Tools: Gemini 3.6 Flash, Gemini 3.5 Flash-Lite, Gemini 3.5 Flash Cyber, Gemini 3.5 Pro (partner testing), Gemini 4 (pre-training), Google AI Studio, Gemini API, Gemini app, Laguna S2.1 (Poolside, 118B total / 8B active MoE), Hugging Face, OpenMDW 1.1 license, GGUF

## [Homebrew 6.0 Just Changed How Your Mac Installs Software](../videos/IwzVzvDw68w.md)
`IwzVzvDw68w` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: dev-tools

Walkthrough of Homebrew 6.0, a security-focused release: third-party taps must be explicitly trusted, installs show a plan and wait for approval, and CI that relies on silent installs or untrusted taps will break.

- Techniques: Explicitly trust third-party taps; Review the install plan before approving; Run a tool once with brew execute; Scan installed packages with brew vulns; Pre-upgrade CI audit
- Tools: Homebrew 6.0, brew trust, brew execute, brew vulns, brew doctor, brew update, GitHub Actions, Ruby, npx (named as the comparison for brew execute; transcript reads 'MPX'), Nix (named as a comparison; transcript reads 'Nyx')

## [The Largest Supply Chain Attack Ever Just Infected Go](../videos/lNsSxWQDqaU.md)
`lNsSxWQDqaU` · Better Stack · 2026-08-02 · q3 · practitioner · news · also: claude-code, coding-agents, dev-tools

Better Stack explains how the self-replicating npm worm (Shai-Hulud) jumped to a Go module, hiding hooks in Claude Code and VS Code config so code runs on folder open, and lists five hardening steps.

- Techniques: Audit agent and editor config before opening untrusted code; Turn off VS Code automatic tasks; Treat .claude/ and .vscode/ as executable code in review; Short-lived, least-privilege CI credentials via OIDC; Egress filtering on CI runners; Minimum release age for packages; Keep secrets out of plaintext on dev machines
- Tools: npm, Go modules, Claude Code (called 'clawed code' in the auto-captions), VS Code (tasks.json, folder-open tasks), Bun (runtime the payload uses to stage its code), Node.js (runs the setup script), TruffleHog (secret scanner the worm reuses), GitHub Actions (CI workflows named as the risk surface), Socket.dev (security firm that flagged the wave), CrowdStrike, Microsoft Defender, SentinelOne (endpoint products the malware checks for), OIDC (short-lived CI credentials), .npmrc (minimum release age setting)

## [The Best File Transfer Tool You've Never Heard Of (croc)](../videos/o_psX5meBo8.md)
`o_psX5meBo8` · Better Stack · 2026-08-02 · q3 · intro · review · also: dev-tools

Better Stack walkthrough of croc, an open-source Go CLI for sending files peer-to-peer through a relay, with PAKE code phrases and resumable transfers; a tool intro with a self-hosted relay option.

- Techniques: Send a file with a one-time code phrase; Resume an interrupted transfer; Self-host the relay for corporate use
- Tools: croc (open-source Go CLI, by Zach Scholl), Docker (croc relay image), WeTransfer, Dropbox, AirDrop, SCP, SSH, FTP, Discord

## [Grok Was Caught Uploading Your Entire Codebase](../videos/n6DIs13ilvU.md)
`n6DIs13ilvU` · Better Stack · 2026-08-02 · q3 · intro · news · also: coding-agents, governance-compliance

Better Stack summarizes reports that Grok's coding CLI uploaded whole repos, git history and env vars to xAI, what xAI changed afterward, and why the /privacy toggle is not real local protection.

- Techniques: Audit a CLI's uploads with a MITM proxy; Grep CLI logs for upload sessions; Rotate secrets if an upload is confirmed; Harden the CLI config and verify the flags
- Tools: Grok CLI (Grok Build), xAI API / account settings, MITM proxy, Claude Code, Codex, Gemini CLI

## [PewDiePie is a software engineer now...](../videos/gQUQZxrM5Ts.md)
`gQUQZxrM5Ts` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: local-ai, dev-tools

Walkthrough of Odysseus, a viral self-hosted AI workspace with a local model cookbook, deep research and cross-session memory. The host calls it a fun local playground but not a production dependency, citing code quality and an agent threat model that needs a locked-down host.

- Techniques: Setup on macOS via Docker script; Hardware-aware local model selection; Blinded side-by-side model comparison; Zero-API local deep research loop; Persistent memory via vector store; Keep Mac GPU inference outside Docker
- Tools: Odysseus, Docker, llama.cpp (transcript: 'Llama CPP'), Metal, SearXNG (transcript: 'Sear XNG'), ChromaDB, FastAPI (transcript: 'fast API'), ntfy (transcript: 'Nifty', for push notifications), IMAP, OpenCode, LLM Fit, Alibaba Deep Research

## [MCP Is Getting Its Biggest Update Ever (No One's Ready)](../videos/k5f1uID3GcU.md)
`k5f1uID3GcU` · Kai Explains · 2026-08-02 · q3 · practitioner · news · also: mcp-and-tools, agent-architecture, infra-cost-scaling

MCP's July 28 rewrite drops the handshake and session ID so any replica can serve any request; state moves into owner-checked handles, and auth fragmentation across clients is the bigger unresolved problem.

- Techniques: Make stateful MCP tools own their handles; Round-trip state through the client as a sealed blob; Split pure tools from stateful tools in deployment; Gateway and proxy checklist for the MCP change; Test each server against every major client; Load tool definitions on demand in the client
- Tools: MCP (Model Context Protocol), July 28 spec revision, OAuth 2.1, Claude Code, Claude.ai, Anthropic API, ChatGPT, Google Cloud, VS Code, Redis, Salesforce, JIRA, Snowflake

## [Browser Use + Claude Code Is INSANE (Free + Open Source + Real Browser)](../videos/OprnDByYVLQ.md)
`OprnDByYVLQ` · Kai Explains · 2026-08-02 · q3 · intro · review · also: voice-multimodal, token-cost-efficiency

Browser Use plus Claude Code: the browser part is old, the new part is a model choosing actions from a numbered text menu of page elements. The menu makes it useful, and the same open page makes prompt injection a real risk when the browser is logged in.

- Techniques: Numbered interactive-element menu for browser agents; Untrusted-page threat model for browser agents; Staged rollout for browser agents: read-only first; Human gate on destructive browser actions and a step cap
- Tools: Browser Use, Claude Code, Claude, Anthropic computer use, Selenium, Playwright, Puppeteer, Google Flights, Cloudflare (bot check)

## [Grok 4.5 Was Trained on YOUR Cursor Sessions (What SpaceX Isn't Telling You)](../videos/hdWUv2V1jRg.md)
`hdWUv2V1jRg` · Kai Explains · 2026-08-02 · q3 · intro · news · also: models-research, coding-agents, governance-compliance

Commentary arguing Grok 4.5 was partly trained on Cursor user sessions captured while privacy mode was off by default, and that behavioral coding data is now the valuable asset.

- Techniques: Audit training and privacy settings in each AI coding tool; Treat codebase-derived vendor benchmarks as possibly contaminated; Scan launch posts for buried data-use disclosures
- Tools: Cursor, Grok 4.5, CursorBench, SWE-Bench Pro (transcribed as "WE Bench Pro"), Terminal Bench 2.1, Fable (model, as named in transcript), Opus 4.8, Opus 4.7, GPT 5.5

## [OpenAI Went Rogue and Hacked Hugging Face](../videos/iUkgp7kzIxM.md)
`iUkgp7kzIxM` · Better Stack · 2026-08-02 · q3 · intro · news · also: sandboxing-execution, observability

Better Stack news recap of the Hugging Face intrusion that OpenAI said came from its unreleased model escaping an internal cyber eval, plus HF's AI-assisted forensics and practical takeaways.

- Techniques: Lock down the eval egress path; Run cyber evals with classifiers off, but isolated; LLM triage over security telemetry; Self-host an open-weight model for forensics; Credential hygiene after a platform incident
- Tools: ExploitGym (OpenAI internal cyber eval), GPT 5.6 Sol, GLM 5.2 (Z.ai open-weight model, self-hosted by Hugging Face), Hugging Face (Spaces, datasets pipeline)

## [Is This WordPress's Worst Hack In History?](../videos/38z2hdzV_DM.md)
`38z2hdzV_DM` · Better Stack · 2026-08-02 · q3 · intro · news · also: dev-tools

Better Stack walks through a WordPress REST API batch-endpoint bug (6.9.x and 7.0.x) that chains a validation desync into unauthenticated SQL injection, admin account creation and a malicious plugin upload.

- Techniques: Check batch endpoint nested requests against the same allow-list; Escape or parameterize values reaching SQL on internal dispatch paths; Patch and check your WordPress version
- Tools: WordPress, WordPress REST API (batch/v1, wp/v2 posts, wp/v2 users), A public proof-of-concept repo (the video does not name it; the link is in the description)

## [Claws Out: Securing and Building with OpenClaw - Nick Taylor, Pomerium](../videos/xg1zNlzw7Jk.md)
`xg1zNlzw7Jk` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: mcp-and-tools, coding-agents

Nick Taylor (Pomerium) on hardening the OpenClaw control plane with trusted-proxy auth, then a live demo of building a UI-bearing MCP app for ChatGPT by editing its workspace from Discord on his phone.

- Techniques: Identity-aware proxy as the auth layer for an agent control plane; Live-edit an MCP app from chat; Widget-to-LLM calls via the MCP apps send-message function; Narrow write access for agent-driven PRs; Test the unauthenticated or fresh-install path
- Tools: OpenClaw, Pomerium, ChatGPT apps (MCP apps), MCP, React, Vite, Discord, Telegram, WhatsApp, Caddy, NGINX, GitHub CLI

## [Agents Need Feature Flags - Sachin Gupta](../videos/zU4EagB311U.md)
`zU4EagB311U` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: governance-compliance, agent-architecture

Sachin Gupta argues agents need feature-flag discipline: six flag types (prompt, tool, model, memory, autonomy, kill switch), a middleware layer, and a kill switch shipped first, with four metrics to track.

- Techniques: Six-surface flag taxonomy; Flag middleware between user and agent loop; Kill switch with three properties; Canary prompt variant; Five-step rollout order; Resolve flags per turn and log segment context; Bypass caching for flag-sensitive responses; Flag hygiene rules
- Tools: LaunchDarkly, Unleash, Lift (as spoken), homegrown flag service

## [Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison](../videos/uU5Gv2h8-9g.md)
`uU5Gv2h8-9g` · AI Engineer · 2026-07-18 · q3 · practitioner · interview · also: claude-code, pr-code-review, context-engineering

Anthropic's Thariq Shihipar and Cat Wu, with Simon Willison, on how Claude Code and Claude Tag change team workflows, code review, auto mode safety, and prompt design, with internal claims about PR share and prompt size.

- Techniques: Staged trust ramp for AI code review; Eval-gated model swap; Behavioral evals built from user complaints; Conditional prompt wording over absolute rules; Per-model system prompts; Classifier-based permissions using user intent; Credential injection through a proxy; Fewer tools with distinct functions; Multiplayer channel agent with shared memory; Dogfooding gate before launch
- Tools: Claude Code, Claude Tag, Slack, GitHub, Datadog, FFmpeg, Remotion, Gemini API, Mountain Project, Claude Fable, Claude Opus 4.8, Claude Mythos

## [Build Systems, Not Code - Angie Jones, Agentic AI Foundation](../videos/ZD9-4fW2HhM.md)
`ZD9-4fW2HhM` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, context-engineering, multi-agent

Angie Jones on designing agentic systems like software: systems thinking, workflow paths, decomposition, code-vs-model-vs-human splits, contracts, idempotent retries, and maintainable agents.md files.

- Techniques: Decompose a giant agent prompt by responsibility; Route work by task type: code, model, or human; Structured decision records as agent memory; Idempotent action log with state-based resume; Evidence-not-instructions handling for untrusted content; agents.md at every level with a cold-start test
- Tools: agents.md, agent skills, subagents, Karpathy LLM Wiki (agent memory layer)

## [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry - Abed Matini, Ogilvy](../videos/Akm1sqvWG4A.md)
`Akm1sqvWG4A` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: rag-retrieval, data-engineering, observability

Abed Matini (Ogilvy) shows a local, framework-free RAG FAQ bot: Docling to Markdown, structure-aware chunking, hybrid BM25 plus vector search fused with RRF, Python guardrails, and Langfuse telemetry.

- Techniques: Markdown-first ingestion with Docling; Per-document chunking strategy selection in admin; Q&A-shaped chunks for FAQ content; Hybrid retrieval with RRF fusion in Python; Deterministic functions instead of agent loops; Pre-LLM guardrail layer with rigid tests; Per-conversation telemetry with self-hosted Langfuse; Two-model local stack in Docker
- Tools: Docling, Python, FastAPI, React, PostgreSQL, Docker, Ollama, Qwen2.5, BGE-M3, Langfuse, GitHub Codespaces

## [The AI bugpocalypse is here. Now what? - Jack Cable, Corridor](../videos/7JgIS42mz7U.md)
`7JgIS42mz7U` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: pr-code-review, governance-compliance, models-research

Jack Cable (Corridor, ex-CISA) argues frontier models now find and exploit vulnerabilities at scale, but the bug classes are old and preventable, so rewrite toward memory safety and add guardrails before the PR for AI-written code.

- Techniques: Rewrite critical components in a memory-safe language; Pre-PR guardrails and visibility for agent-written code; Give the reviewer business and threat context; Use defenders' frontier models to harden systems
- Tools: Claude Code, Cursor, Rust, Slack, BaxBench

## [Stop Writing Tone Instructions. Layer Them. - Isadora Martin-Dye, Isadora & Co](../videos/ij-AU9dpJjc.md)
`ij-AU9dpJjc` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: context-engineering, product-ux

Isadora Martin-Dye on layering a brand-voice AI agent into four stages: non-overridable identity rules, situational context, voice examples, and a deterministic post-generation veto, with fail-loud multi-tenant identity.

- Techniques: Four-layer ordered prompt stack via single assembly; Non-overridable identity layer; Soft context as tone guidance, never quoted; Deterministic post-generation veto with soft flags and hard rejects; Fail-loud multi-tenant identity; Shared veto gate by default; Trainable voice dial from staff edits
- Tools: Threadline (her own missing-persons tool, not a third-party product)

## [The Agentic Web and the Bazaar Era of AI - Ramesh Raskar, MIT Media Lab](../videos/sum9DgexFRQ.md)
`sum9DgexFRQ` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: mcp-and-tools, multi-agent, infra-cost-scaling

Ramesh Raskar and Maria of MIT's Project Nanda outline an open infrastructure for a web of AI agents: a signed discovery index, agent hosting, and NandaTown, a simulator for testing agent networks before they go live.

- Techniques: Signed agent facts record and agent card; Message box in front of the agent runtime; Adaptive endpoint resolution; Sleep and wake hosting; Tiered simulation with scripted agents, then LLM agents; Onboarding in three tiers
- Tools: Nanda index, NandaTown, OpenClaw, Maritime, AWS, DNS, YAML

## [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI](../videos/Rx8f05JI_WA.md)
`Rx8f05JI_WA` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: evals, testing-verification, coding-agents

Rishi Desai presents SWE-Marathon, 20 project-scale coding tasks where the best agent solves only 26%, and argues that multi-channel, anti-cheat verification is the main bottleneck for long-horizon evals.

- Techniques: Multi-channel verification; Strace-based forbidden-subprocess detection; Hardening loop before publishing a benchmark; Standardize tasks into a Harbor-format environment; Trajectory work-pattern charts
- Tools: SWE-Marathon, Harbor, HumanEval, SWE-bench, Terminal-Bench, Claude Opus 4.8, Claude Code, GPT-5.5 (transcribed as 'gbd 5.5'), Codex, GLM 5.2, Gemini, strace

## [What if the harness mattered more than the model? - Aditya Bhargava, Etsy](../videos/2e9ANoOEn28.md)
`2e9ANoOEn28` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, multi-agent, evals

Aditya Bhargava (Etsy) argues the agent harness, not the model, drives results, especially for weaker models, and walks through building a coding-agent harness step by step in his language Agency.

- Techniques: Tools as plain functions with docstrings; Interrupt plus handler for approvals; Partial function application for capability scoping; ReAct test-feedback loop; Subagents as tools with grouped tool sets; Objective-driven prompt optimization; Serializable pause and resume at interrupts
- Tools: Agency (agencylang.com, TypeScript-like agent language, installed via pnpm), HarnessBench (harness benchmark, 106 tasks), Claude Code (cited as an example agent: Opus model plus harness), Built-in Agency log viewer, Built-in Agency standard library (includes Wikipedia search tool)

## [Using RL Agent to Detect and Remediate ETL Pipeline Failures - Anna Marie Benzon](../videos/LrGCT7G_rU8.md)
`LrGCT7G_rU8` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: data-engineering, agent-architecture, evals

Anna Marie Benzon presents a capstone ETL remediation agent: deterministic rules detect facts, tabular Q-learning picks among six bounded actions, and an external safety layer can force escalation. Results are from synthetic benchmarks.

- Techniques: Event-triggered diagnose-decide-act-verify loop; Rules for facts, learning for choices, guardrails for authority; Tabular Q-learning over a small discrete state; Propose, check, execute, and record separately; Multi-seed evaluation with baselines and confidence intervals
- Tools: AWS Glue, Amazon EventBridge, AWS Lambda, Amazon CloudWatch, AWS Glue Data Catalog, Amazon S3

## [MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc](../videos/sAOBXCDiDOs.md)
`sAOBXCDiDOs` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: mcp-and-tools, product-ux

Pietro Zullo (Manufact) explains MCP Apps: tools that return sandboxed UI widgets, the primitives behind them, and how the new client app stores distribute MCP servers.

- Techniques: Widget-returning tool; Split structured output (UI vs model); Set-state to sync UI to model; Stream tool input into the UI; Widget actions that call tools; Client-aware output; Pre-submission checks for stores
- Tools: MCP, MCP Apps, MCP-UI, MCP SDK, MCP Inspector, React, Remotion, Excalidraw, Granola MCP, Linear MCP, Postgres MCP, Claude Code

## [Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis](../videos/IQkVMvXQKLY.md)
`IQkVMvXQKLY` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: training-finetuning-rl, evals

Sachin Kumar (LexisNexis) shows that a backdoored fine-tune can pass behavioral evals, and that a sparse autoencoder trained on base-vs-fine-tune activation deltas finds the trigger with near-zero false alarms.

- Techniques: Diff SAE on activation deltas; Backdoor isolation score per feature; Procedural data with a controlled trigger; Objectively measured backdoor target; Build-gate probe check
- Tools: SmolLM2-360M, sparse autoencoder, LoRA, static analysis

## [From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI](../videos/OqM67QG_Ikk.md)
`OqM67QG_Ikk` · AI Engineer · 2026-07-18 · q4 · deep · talk · also: sandboxing-execution, agent-architecture, infra-cost-scaling

A first-principles tour of why agent code needs sandboxes, comparing fork/exec, containers, gVisor and microVMs, then how to add disk snapshots, restore and multi-node scheduling for OpenAI-scale agent sandboxes.

- Techniques: Isolation ladder for untrusted tool execution; Driving a microVM through its VMM API; Per-device jailing for emulated devices; Incremental block-level disk snapshot; Acknowledge snapshot before upload completes; Tiered always-on block storage; Snapshot-aware scheduling; Startup latency hybrid
- Tools: gVisor, Firecracker, Cloud Hypervisor, CrossVM, QEMU, KVM, virtio, vsock, seccomp, VFIO, NBD, FIEMAP

## ["I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox](../videos/-CnA2lGfymY.md)
`-CnA2lGfymY` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: testing-verification, agent-architecture

Erik Meijer shows how to make agent tool calls provably safe by turning the plan into a program that can be type-checked, taint-analysed and proven before anything runs.

- Techniques: Plan as data, execute after check; Taint or data-flow analysis over the plan; Proof-carrying generation; Effects as data (free monad style)
- Tools: Lean, Dafny, Isabelle, PVS, TLA+, Claude Code

## [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns - Elizabeth Fuentes, AWS](../videos/vJukHCIv7Ck.md)
`vJukHCIv7Ck` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: mcp-and-tools, rag-retrieval, multi-agent

AWS developer advocate walks through five code-level techniques to reduce agent hallucinations: semantic tool selection, GraphRAG for aggregation, multi-agent validation, code-enforced hooks, and steering rules. Demos use dummy tools.

- Techniques: Semantic tool selection; Per-turn tool swap in agent loop; Text-to-Cypher GraphRAG for aggregation; Executor, validator, critic swarm; Before-tool-call hooks for hard rules; Steering rules for soft constraints
- Tools: Strands Agents, OpenAI API, sentence-transformers, Neo4j (Cypher, LLM graph builder), agent-control (steering SDK), Amazon Bedrock AgentCore (Gateway, Runtime, Policy, Memory), DynamoDB, Neo4j AuraDB, AWS Lambda, Ollama (mentioned)

## [Using LLMs to Secure Source Code — Eugene Yan, Anthropic](../videos/imFedndyXYQ.md)
`imFedndyXYQ` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: testing-verification, sandboxing-execution, multi-agent

Eugene Yan (Anthropic) walks through a six-step harness for using LLMs to find, verify, triage and patch vulnerabilities, arguing the bottleneck has moved from finding bugs to verification, triage and patching.

- Techniques: Threat model as a living context document; Isolated, reproducible PoC sandbox; Independent adversarial verifier; Tool-equipped discovery; Less prescriptive prompts for stronger models; Patch validation ladder with a generative verifier loop; Close the loop as a regression check; Severity triage as impact times likelihood with compensating controls; Code-owner routing without an LLM
- Tools: Claude, Claude Code, Docker, PostgreSQL, Redis, Jira

## [Deterministic Infra for Non-Deterministic AI Agents - Nishant Gupta, Meta Superintelligence Labs](../videos/APh1Vx0oLmQ.md)
`APh1Vx0oLmQ` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: agent-architecture, observability, infra-cost-scaling

Nishant Gupta (Meta Superintelligence Labs) argues that agent reliability is an infrastructure problem: treat models as probabilistic, keep the platform deterministic, and let infrastructure validate and enforce what the model proposes.

- Techniques: Propose, validate, enforce split; Tool isolation with circuit breakers; Controlled recovery instead of open retries; Decision-chain tracing; Per-agent limits and cost quotas; Layered defence for agent actions; Humans as exception handlers

## [They Finally Fixed Claude Code's Biggest Problem](../videos/KiTmBtyaeXg.md)
`KiTmBtyaeXg` · AI LABS · 2026-07-02 · q2 · practitioner · review · also: skills-self-improvement, claude-code

A walkthrough of NVIDIA's Skill Specter, a scanner for agent skills, plus a Claude Code wrapper that adds an LLM-based second scan through headless mode and a discover-scan-fix loop around skills.sh.

- Techniques: Two-tier skill scan before install; Use Claude headless mode as the LLM judge; Discover, scan, show, fix, rescan loop in SKILL.md; Check tool-name identity at the code-point level; Compare declared behavior with code behavior; Check dependencies against a live bad-package list
- Tools: Skill Specter (NVIDIA scanner, named by the host; version not stated), Claude Code, Claude headless mode (claude -p), skills.sh (skill registry with CLI search), OpenAI API (the AI check's default backend, per the host), Codex (mentioned only in the sponsor segment), Nimblist (sponsor; open-source visual workspace for Claude Code and Codex sessions, with a Kanban board, red/green diffs, auto-generated commit messages, and a mobile app)

## [BREAKING: US Government BANNED Mythos and Fable](../videos/Q5_e2v7WZEQ.md)
`Q5_e2v7WZEQ` · Better Stack · 2026-07-02 · q2 · intro · news · also: governance-compliance, models-research

Better Stack breaking-news reaction to a reported US export-control directive that suspended Fable 5 and Mythos 5 access for foreign nationals, with Anthropic's response read out and the speaker's speculation.
- Tools: Fable 5, Mythos 5, GPT 5.5 (OpenAI, named by Anthropic as having similar capability)

## [Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe](../videos/KLSuFPj2ld0.md)
`KLSuFPj2ld0` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: governance-compliance, mcp-and-tools

Stripe's Steve Kaliski on letting agents spend safely: scope shared payment tokens to amount, time and seller, use HTTP 402 for paid tools, and keep discovery non-deterministic while payments stay deterministic.

- Techniques: Seller-scoped delegated payment credential; Deterministic transaction layer behind a non-deterministic planner; HTTP 402 pay-per-call; Round-trip checkout state; Forward risk signals to the counterparty
- Tools: Stripe shared payment tokens, Stripe Payment Intents, Stripe Issuing, Machine payments protocol (with Tempo), Agentic Commerce Protocol (with OpenAI), curl (demo), Tempo blockchain (pathUSD), Base

## [Lobster Trap: OpenClaw in Containers from Local to K8s and Back — Sally Ann O'Malley, Red Hat](../videos/F1DYkY1BlfM.md)
`F1DYkY1BlfM` · AI Engineer · 2026-06-18 · q2 · practitioner · demo · also: sandboxing-execution, infra-cost-scaling

Red Hat's Sally Ann O'Malley runs OpenClaw agents in Podman containers, keeps API keys as secret refs, and lifts the same setup to Kubernetes; the talk is a live demo with a pitch for containers as the default agent sandbox.

- Techniques: Podman secrets + secret-ref indirection for agent API keys; Container as the agent sandbox with explicit host grants; Mount the agent's tool directory at startup; Named volume for runtime state with scheduled backup; Local-to-Kubernetes lift with the same image; Company baseline image with per-user layer; SSH sandbox for remote execution; Installer that converts env vars to secret refs and sets providers
- Tools: OpenClaw, Podman, Podman secrets, Docker, Kubernetes, OpenShift, kind, systemd, OpenRouter, Anthropic, Gemma, OpenTelemetry

## [Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence](../videos/UQKg0td-Bf4.md)
`UQKg0td-Bf4` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: testing-verification, evals, mcp-and-tools

Steven Willmott (SafeIntelligence) argues agent testing needs an explicit spec of data, rules, terminology, roles and robustness needs, kept separate from the implementation and run in a closed loop.

- Techniques: Six-part agent spec; Spec-driven security testing; Input perturbation sweep; Closed-loop spec iteration (backyard RL); Specs as versioned repo files; Agent cards plus variation envelopes
- Tools: SafeIntelligence platform, A2A agent cards, LangSmith, Vertex AI agents, Braintrust, OpenAPI

## [What if the network was the sandbox? — Remy Guercio, Tailscale](../videos/BM2JX9hqsVQ.md)
`BM2JX9hqsVQ` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: sandboxing-execution, governance-compliance, observability

Tailscale's Remy Guercio argues the network layer can act as an agent sandbox: identity-tagged WireGuard connections let an LLM gateway hold the provider key so the sandbox never has one, and every model call and tool call is visible and cuttable there.

- Techniques: Zero-key sandbox behind an identity-aware gateway; Per-identity budgets and quotas across providers; Per-tool-call webhooks for external policy; Identity-aware internal services with tsnet; Policy as code for network identity
- Tools: Tailscale, WireGuard, Aperture, tsnet, Claude Code, Codex, Gemini CLI, GitHub Actions, Opus 4.6

## [What Breaks When You Build AI Under Sovereignty Constraints - Bilge Yücel, deepset GmbH](../videos/x2bH0RKPgdc.md)
`x2bH0RKPgdc` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: governance-compliance, mcp-and-tools, observability

Bilge Yücel (deepset) on building AI under sovereignty constraints: four pillars, what breaks when you move from frontier APIs to self-hosted, and a guardrail-agent-guardrail reference design built on Haystack.

- Techniques: Sovereignty checklist as a design gate; Safe/unsafe router as an input guardrail; Per-agent tool allowlist plus BM25 tool search; Per-tool human confirmation strategies; Pipeline serialized to YAML for version control; Tracer component wrapping the pipeline
- Tools: Haystack, MCP, BM25, OpenTelemetry, YAML, Kubernetes, Mistral, Google models, Nvidia models, Jina

## [Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic](../videos/c-2eEv2ou7Y.md)
`c-2eEv2ou7Y` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: mcp-and-tools, product-ux

Frédéric Barthelet (Alpic) explains why ChatGPT and Claude render third-party MCP app UI in nested "double" iframes: CSP and origin isolation rule out simpler options, and the nesting is the workable compromise.

- Techniques: Double-iframe isolation for untrusted UI; Declare-then-enforce external domains; CSP inspection in dev tools
- Tools: MCP Apps extension, OpenAI Apps SDK, SkyBridge, HTML iframe (srcdoc, sandbox, allow-same-origin), Content Security Policy (frame-src, script-src, connect-src)

## [Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google](../videos/_B4Pv9ttFgY.md)
`_B4Pv9ttFgY` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: mcp-and-tools, product-ux

Four engineering lessons from the Chrome DevTools MCP team on designing agent-facing interfaces: token cost, error recovery, tool discoverability, and trust boundaries.

- Techniques: Semantic summaries instead of raw tool output; Tokens per successful outcome; Tool categorization and slim mode; CLI with piping for local post-processing; Self-healing error messages; Proactive detours; Tool descriptions as UI for the agent; Trust tiers with deliberate consent friction
- Tools: Chrome DevTools MCP server, Gemini CLI, Claude Code, Codex, OpenClaw

## [This One Command Fixed The Biggest Problem Of AI Coding](../videos/qkc1j3_k8gs.md)
`qkc1j3_k8gs` · AI LABS · 2026-06-02 · q3 · practitioner · tutorial · also: coding-agents, token-cost-efficiency, pr-code-review

Walkthrough of DeepSec, a regex-prefilter plus batched Claude Code/Codex agent harness for repo security scans. Strong on code-local bugs, weak on runtime and logic flaws.

- Techniques: Regex prefilter before agent review; Batched parallel agent investigation with merge and coverage check; Project context file for the scanner (info.md); DeepSec command sequence; Resumable batch processing; Per-finding output with ownership and repro; Scoping an unscoped agent review
- Tools: DeepSec (Vercel security harness; `deepsec init`, `scan`, `process`, `report`, `export`), Claude Code, Codex, Claude Agent SDK, Codex Agent SDK, Opus 4.7 (max effort), GPT 5.5 (x-high reasoning), Git (metadata for commit attribution and owner), Markdown and JSON (output formats)

## [Why Claude Recommends Resend & Building in Public | Better Stack Podcast Ep. 15](../videos/8ahyAKK2l9Y.md)
`8ahyAKK2l9Y` · Better Stack · 2026-06-02 · q2 · intro · interview · also: product-ux, dev-tools

Better Stack podcast with Resend's DX engineer on getting LLMs to recommend a vendor, scoping per-team AI agents with narrow API keys, and email deliverability basics. Mostly biographical, with a few practitioner nuggets.

- Techniques: One scoped identity per agent or team; Scheduled weekly digest agent; Weekly competitor watch, on demand; Research agent before writing a changelog or post; Scaffold landing pages from existing repo patterns; LLM-discoverability checklist for a docs or marketing site; Deliverability setup for a transactional email service; Obsidian vault synced to GitHub as a personal task store
- Tools: Resend, React Email, Claude, Hermes (OpenClaw-based agent), OpenClaw, Cursor, GitHub CLI, 1Password, Slack, Obsidian, Linear, Raycast

## [npm installs can hack your laptop (Here's how to stop it)](../videos/Wq6yMdt11LM.md)
`Wq6yMdt11LM` · Better Stack · 2026-06-02 · q3 · practitioner · tutorial · also: dev-tools

Seven practical npm/pnpm/bun supply-chain hardening steps: release-age gating, disabling install scripts, blocking git deps, pre-install scanners, lockfile checks, frozen CI installs, and dependency habits.

- Techniques: Release-age gating per package manager; Disable install scripts and allow-list exceptions; Block git and exotic dependencies; Scan packages before install via alias; Lockfile hygiene with lockfile-lint; Frozen installs in CI and production; Dependency hygiene habits
- Tools: npm, pnpm, bun, npx, bunx, MPQ, Socket Firewall, lockfile-lint, lavamoat allow-scripts, esbuild, TanStack React Start, Snyk vulnerability database

## [Deno Just Open Sourced Their Agent Firewall (Claw Patrol)](../videos/ZiFoTw6doGI.md)
`ZiFoTw6doGI` · Better Stack · 2026-06-02 · q3 · intro · review · also: governance-compliance, infra-cost-scaling

Walkthrough of Claw Patrol, an open-source agent firewall from the Deno team: a gateway injects real credentials into agent requests, enforces per-action rules, and logs every request.

- Tools: Claw Patrol (Deno, open source), Deno, Tailscale, WireGuard, OpenClaw, Claude (Claude Code CLI; transcript spells it "Clawed"), Codex, Postgres, ClickHouse, Slack, GitHub, Kubernetes

## [The NPM Worm Is Back And It's So Much Worse (TanStack Hacked)](../videos/BOABEBwNnvk.md)
`BOABEBwNnvk` · Better Stack · 2026-06-02 · q3 · practitioner · news · also: claude-code, dev-tools

Walkthrough of the Shai-Hulud npm worm's fourth wave, which hit TanStack and about 160 other packages. It explains the persistence, credential theft, and how a poisoned CI cache plus OIDC publishing let attackers ship validly signed malicious releases.

- Techniques: Audit for agent-hook persistence after installing a package; Incident response order for a suspected worm; Trace install-time payloads through lifecycle scripts and optional dependencies; Treat CI cache restores as a trust boundary; Scope OIDC publishing to the release job only; Find 2FA-bypassing npm tokens on dev machines
- Tools: npm, npm trusted publishing (OIDC), pnpm, Bun (bun run task runner), GitHub Actions, GitHub pull_request_target, Claude Code (hooks, settings, session history), VS Code tasks, AWS IMDSv2, AWS ECS task metadata, Kubernetes service accounts, HashiCorp Vault

## [Perplexity Open-Sourced a Scanner Every Dev Should Know (Bumblebee)](../videos/L6iAw5yitfc.md)
`L6iAw5yitfc` · Better Stack · 2026-06-02 · q3 · practitioner · review · also: dev-tools, mcp-and-tools

Better Stack demos Perplexity's open-source Bumblebee, a read-only Go binary that inventories a dev machine's packages, editor and browser extensions, and MCP configs from local metadata, for supply-chain incident response.

- Techniques: Weekly baseline inventory dumped centrally; Escalate scan depth by incident state; Query NDJSON with jq or a SIEM; Treat MCP configs as part of the secret and dependency surface
- Tools: Bumblebee (Perplexity open-source scanner), Go (go install, single binary), npm, pnpm, yarn, bun, Go modules, VS Code, Cursor, Claude, jq, MDM

## [Yeah it’s over for NextJS... 13 NEW vulnerabilities](../videos/mYdx6hZG9qo.md)
`mYdx6hZG9qo` · Better Stack · 2026-06-02 · q3 · practitioner · news · also: dev-tools

Better Stack walks through five of the 13 React and Next.js CVEs in one security release (middleware bypass, RSC denial of service, SSRF, cache poisoning, script XSS) and argues for moving off Next.js.

- Techniques: Enforce auth in the data loader, not only in middleware; Regression-test matcher and data-route coverage; Load-test server action endpoints with large or repetitive payloads; Make CDN cache keys match the content-type routing logic; Keep untrusted input out of inline script props; Limit what the app server can reach internally; Patch to the fixed Next.js release
- Tools: Next.js (Pages Router, i18n, middleware/proxy, getServerSideProps, next/script beforeInteractive), React Server Components and the React Flight serialization protocol (react-server-dom), TanStack Start, Astro, Vinext, Cloudflare, Python http.server (used as the internal target in the SSRF demo), curl, Browser devtools (Network tab, inspect element), Claude Mythos (suggested by the presenter for auditing the React and Next.js codebase)

## [Human-in-the-Loop Automation with n8n — Liam McGarrigle](../videos/tDArkCqjA-c.md)
`tDArkCqjA-c` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: agent-architecture, mcp-and-tools, context-engineering

Workshop on building a Gmail and Google Calendar agent in n8n, then gating sensitive tool calls behind human approval steps that the model cannot skip.

- Techniques: Approval gate in front of sensitive tools; Free-text decline as feedback; Dry runs with dummy data before real accounts; Rules in tool descriptions, not one system prompt; Per-field descriptions for argument mistakes; Wait with an auto-deny timeout; Confirm sub-workflow as a tool; Sub-agent per domain as a tool; Date and time injection via expression; Memory window sizing
- Tools: n8n, OpenRouter, Gmail, Google Calendar, Slack, Notion, Postgres, Redis, Claude, Claude Code, Luxon, Swagger

## [Viktor: AI Coworker That Lives in Slack — Fryderyk Wiatrowski](../videos/ohKt066uFhg.md)
`ohKt066uFhg` · AI Engineer · 2026-05-18 · q2 · intro · talk · also: product-ux, enterprise-adoption, memory

Viktor's co-founder on building a company AI employee that lives in Slack: shared integrations, scoped access, memory across many users, and why tone and staged rollout matter.

- Techniques: Shared-integration inheritance with per-integration scoping; Thread roll-over on new DM; Treat edits and deletes as control signals; A/B test model personality, not only task scores; Staged proactivity rollout; Analytics check before acting on a claim; Browser-DOM web agent (2023 baseline)
- Tools: Slack, Viktor, OpenClaw, Claude Code, Claude Cowork, Opus 4.6, GPT-5.4, PostHog, Gmail, Meta Ads, WebArena

## [Agents on the Canvas in tldraw — Steve Ruiz, tldraw](../videos/sPUjIBH5Cwg.md)
`sPUjIBH5Cwg` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: multi-agent, product-ux, sandboxing-execution

Steve Ruiz (tldraw) shows how agents moved from one-shot drawing on a whiteboard to multiple agents working as a team on a shared canvas, and the safety trade-offs of letting them script a desktop app.

- Techniques: Structured-output shape drawing; Produce-review-iterate loop; Leader/follower multi-agent on shared state; Expose a runtime API for agent-written code; Prompt for spatial and coordinate conventions
- Tools: tldraw, Electron, Claude, Cursor, Make Real

## [Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft](../videos/iOXM3zE-2dk.md)
`iOXM3zE-2dk` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: observability, evals, coding-agents

Microsoft Foundry workshop on agent observability: trace-linked evals, stage-wise agent evaluators, OTel tracing, red teaming, and an observe skill that automates the eval-optimize loop with a human stopping regressions.

- Techniques: Trace-linked evaluation; Stage-wise agent evaluators; Bootstrapped eval dataset from instructions; Version-compare regression diff; Bounded auto-optimization with human stop; Adversarial red teaming with an attacker agent; OTel GenAI tracing with custom attributes; Eval gate on model swap
- Tools: Microsoft Foundry, Azure Monitor, Application Insights, OpenTelemetry, GitHub Codespaces, dev containers, GitHub Copilot Chat, Foundry MCP server, Azure AI Toolkit (VS Code extension), LangGraph, KQL, PyRIT (auto-caption reads it as 'pirate')

## [OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman](../videos/MhHEGMFCEB0.md)
`MhHEGMFCEB0` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: coding-agents, multi-agent, pr-code-review

OpenAI's Codex workshop on plugins, background automations, code review, custom sub-agents with sandbox modes, guardian approvals, and stop hooks for long runs.

- Techniques: Custom sub-agent personas as TOML files; Fan-out review by file slices with an orchestrator; Read-only explorer on a fast cheap model; Parallel brainstorm of implementation options; Guardian verifier sub-agent for privileged actions; Stop hook that keeps a run going; Best-of-N cloud runs; Playwright interactive skill for visual debugging
- Tools: Codex, Codex app, Codex CLI, Codex IDE extension, Codex Code Review, Codex Security, Claude Code plugin for Codex, Playwright, ImageGen, Slack, Gmail, Google Drive

## [Gateways are All You Need — Karan Sampath, Anthropic](../videos/CD6R4Wf3jnY.md)
`CD6R4Wf3jnY` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: mcp-and-tools, governance-compliance, infra-cost-scaling

Anthropic forward-deployed engineer Karan Sampath argues enterprises should put one gateway in front of all MCP servers for auth, access control, observability and credentials, so teams build only business logic.

- Tools: MCP, Claude Code, Claude Agent SDK, claude.ai, Claude managed agents

## [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../videos/5ID22ACI7IM.md)
`5ID22ACI7IM` · AI Engineer · 2026-05-18 · q3 · practitioner · workshop · also: context-engineering, memory, rag-retrieval

Peter Werry and Brandon (Unblocked) argue that agents need a "context engine" that understands org history, permissions and conflicts, not just MCP access to data, then run a hands-on social-graph workshop. Much of it is product pitch.

- Techniques: Compartmentalized, permission-tagged retrieval; Ingestion-time tags plus runtime judge for conflicts; Expert graph from contribution edges; Focus-repo-biased two-stage retrieval; Feedback weighted by source trust; Split cadence by source type
- Tools: Claude Code, Cursor, Codex, GitHub Copilot, MCP, Slack, Microsoft Teams, Sentry, Datadog, GraphRAG, pgvector-style vector retrieval, Composio

## [One Login to Rule Them All: Cross-App Access for MCP — Garrett Galow, WorkOS](../videos/EmhRyw6xeT0.md)
`EmhRyw6xeT0` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: mcp-and-tools, enterprise-adoption

Garrett Galow (WorkOS) explains cross-app access (XAA): the enterprise IdP brokers silent, short-lived MCP tokens so users stop clicking consent screens and IT regains revocation and visibility.

- Techniques: Cross-app access via ID-JAG token exchange; IdP-side allow-list for app-to-app access; Short-lived access tokens with silent re-mint; Audience URL as the routing key; Server-side ID-JAG acceptance
- Tools: MCP, Claude Code, Cursor, Okta, Figma, WorkOS, Microsoft Entra, SCIM, CIMD, DCR, OAuth, OIDC

## [Context Is the New Code — Patrick Debois, Tessl](../videos/bSG9wUYaHWU.md)
`bSG9wUYaHWU` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: context-engineering, evals, skills-self-improvement

Patrick Debois argues that agent context (instructions, skills, specs) needs its own lifecycle like code: generate, test with evals, distribute as packages, observe logs, then adapt.

- Techniques: Layered context tests (lint, judge, end-to-end); Repeated runs with error budgets; Commit-scoped context A/B scenarios; Turning feedback into context fixes; Context filter before loading; Packaging context with provenance and scanning; Parallel generation as a spec-quality check
- Tools: Claude Code, AGENTS.md, CLAUDE.md, SKILL.md, MCP, Tessl, GitHub, GitLab, Slack, Snyk, Gemini, GitHub Copilot

## [LLM codegen fails and how to stop 'em — Danilo Campos, PostHog](../videos/juoNbJiZUi0.md)
`juoNbJiZUi0` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: coding-agents, context-engineering, skills-self-improvement

Danilo Campos (PostHog) on making an autonomous integration agent reliable: feed fresh docs, use thin "model airplane" example apps, breadcrumb the task, interrogate the agent at each stop, and lock down secrets.

- Techniques: Agent-selected fresh docs menu; Model airplane example apps; Breadcrumbed multi-stage prompting; Stop-hook self-interrogation; Tool-gated secret access
- Tools: PostHog Wizard, Claude Agent SDK, Claude Code, Cursor, MCP, PostHog LLM gateway

## [Harnesses in AI: A Deep Dive — Tejas Kumar, IBM](../videos/C_GG5g38vLU.md)
`C_GG5g38vLU` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: agent-architecture, testing-verification, context-engineering

Tejas Kumar (IBM) walks through building a "poor man's" agent harness live: deterministic guardrails, outcome verification, and credential injection around a weak model, with the prompt left unchanged.

- Techniques: Deterministic pre-turn hook for state and secrets; Outcome verification from the trace; Guardrails as composable functions; Two-level retry around an attempt; Naive head-and-tail context trimming; Tool definitions in the OpenAI SDK shape
- Tools: Playwright, Chromium, OpenAI Agents SDK-style tool definitions, GPT-3.5 Turbo, Claude Code, Cursor, Codex, Qwen, GPT-OSS, OpenRAG

## [Scaling GitHub for your Agents — Sam Morrow, GitHub](../videos/0n3MKk7r60w.md)
`0n3MKk7r60w` · AI Engineer · 2026-05-18 · q4 · practitioner · talk · also: mcp-and-tools, context-engineering

GitHub's MCP server lead on scaling a remote MCP server: why too many tools hurt agents, how defaults and tool-set grouping work, token-trimmed outputs, scope-based auth, and a stateless design.

- Techniques: Per-request server construction with policy-filtered tools; Scope-filtered tool listing with step-up auth; Tool-set grouping with defaults tuned from usage data; Output-token tailoring per tool; Server-side composition to encode intent; Cross-tool eval for description tuning; Wrap read-only tools in a CLI to test agent use
- Tools: GitHub MCP server, Claude Code, VS Code, Redis, Cloudflare code mode, Anthropic tool search, Pi

## [The Open-Source ngrok Alternative Devs Are Switching To (Zrok)](../videos/dLW0cT-iTjs.md)
`dLW0cT-iTjs` · Better Stack · 2026-05-02 · q3 · intro · review · also: dev-tools

A 5-minute walkthrough of zrok, an open-source, self-hostable ngrok alternative that shares localhost publicly or to token-holders without port forwarding, plus its tradeoffs versus ngrok.

- Techniques: Public share of a local dev server; Token-gated private share; Share a directory as a browsable drive
- Tools: zrok, OpenZiti, ngrok, Cloudflare Tunnel, Tailscale, Next.js

## [Someone Cheated at Roblox and Broke Vercel](../videos/nnzH0eaAFa8.md)
`nnzH0eaAFa8` · Better Stack · 2026-05-02 · q3 · intro · news · also: governance-compliance

A news explainer on how a Roblox cheat download on a Context.ai employee's laptop led to a breach of Vercel, with the lesson that over-permissioned OAuth tokens and non-sensitive env vars made the blast radius large.

- Techniques: Audit OAuth grants for third-party apps; Rotate secrets at the source after a platform compromise; Mark env vars as sensitive for hosted platforms; Least-privilege grants for AI tools on corporate accounts; Treat OAuth tokens as credentials
- Tools: Vercel, Context.ai (AI Office Suite), Google Workspace, Roblox, Luma Stealer, Amazon Web Services, Linear, Supabase, Datadog, AuthKit, Next.js, Turbopack

## [Stop Building Login Systems… Use This Instead (Authentik)](../videos/LVuspKy4P2w.md)
`LVuspKy4P2w` · Better Stack · 2026-05-02 · q2 · intro · review · also: dev-tools

Short walkthrough of Authentik, a self-hosted open-source identity provider for SSO, OAuth login and MFA across your own apps, with a Docker Compose quick start and a take on its costs versus Keycloak, Authelia, Okta and Auth0.

- Techniques: Stand up Authentik with Docker Compose; Register an app with OAuth2/OIDC in the admin UI; Model login logic as flow stages plus Python policies; Weigh Authentik against other self-hosted IdPs by RAM, ops load and scale
- Tools: Authentik, Docker Compose, Kubernetes, OAuth2/OIDC, Keycloak, Authelia, Okta, Auth0

## [PostgREST Deletes 80% of Your Backend Code](../videos/DVYVvewa2kc.md)
`DVYVvewa2kc` · Better Stack · 2026-05-02 · q2 · intro · tutorial · also: dev-tools

Short Better Stack tutorial showing PostgREST turning a Postgres table into a REST API with Row Level Security and Swagger docs, with no backend code, plus its trade-offs.

- Techniques: Run PostgREST as a REST layer over Postgres via Docker Compose; Enforce access with Row Level Security instead of middleware; Query and write through HTTP with curl; Keep a thin backend layer for complex logic
- Tools: PostgREST, PostgreSQL, Docker Compose, Swagger UI, Supabase (named as a production user of PostgREST), curl

## [Anthropic's Managed Agents Are Different (Here's Why)](../videos/uxHolzq1NcA.md)
`uxHolzq1NcA` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: agent-architecture, claude-code, mcp-and-tools

Better Stack walks through Anthropic's Claude Managed Agents: building a Slack-connected agent with no hand-written orchestration code, its per-session-hour pricing, and the session/harness/orchestrator architecture with runtime credential vaulting.

- Techniques: Scaffold a managed agent via the Claude Code skill; Read-only toolset for a retrieval agent; Run setup once, then the runtime; Iterate in the Console and keep version history; Runtime credential injection (vault pattern); Separate durable session log from the executor
- Tools: Claude Managed Agents, Claude Console, Claude Code (managed-agent onboarding skill, `/claude-api managed agents onboarding`), Claude Agent SDK, TypeScript Claude SDK, Claude Opus, Claude Sonnet, Slack (Slack app and bot), Notion (built-in integration), MCP servers, OpenClaw, GitHub (private repo as data source)

## [OpenClaw Agents Just Got Better With This](../videos/JC53AcoFh-Q.md)
`JC53AcoFh-Q` · AI LABS · 2026-04-02 · q2 · intro · review · also: multi-agent, memory, skills-self-improvement

A tool roundup for hardening and extending OpenClaw agents: a security skill suite, a deterministic multi-agent workflow runner, a hybrid memory plugin, a network-API browser skill, Cloudflare hosting, a dashboard, and a curated skill list.

- Techniques: Installing a skill from git when the registry is rate-limited; Self-verifying skills: checksum check with re-download on mismatch; Scheduled security heartbeat over installed skills; Deterministic multi-agent workflow with verifier and fresh contexts; Re-ranked hybrid memory as an agent memory plugin; Replaying site APIs with cookies instead of driving a browser visually; Filtering a large skill registry before installing
- Tools: OpenClaw, ClawSec, Prompt Security, Heartbeat skill, Soul Guardian, OpenClaw Watchdog, Antfarm, Ralph Loop (creator's earlier project, per speaker), AI Dev Task (creator's earlier project, per speaker), ClawHub (skill registry), Awesome OpenClaw Skills (curated list), MemoryLanceDB Pro

## [This Shouldn’t Be Better Than 1Password… But It Is](../videos/NLmYjFe_Gg4.md)
`NLmYjFe_Gg4` · Better Stack · 2026-04-02 · q2 · intro · tutorial · also: dev-tools

Better Stack walkthrough of self-hosting Vaultwarden (a lightweight Rust Bitwarden-compatible server) via Docker Compose, connecting the Bitwarden browser extension and the Bitwarden CLI for scripted secret retrieval.

- Techniques: Run Vaultwarden with Docker Compose; Point Bitwarden clients at a self-hosted server; Pull credentials into scripts with the Bitwarden CLI
- Tools: Vaultwarden, Bitwarden (clients, browser extension, CLI, server), 1Password, NordPass, Docker, Docker Compose, Homebrew, Google Chrome, YubiKey, M4 Pro (hardware)

## [NVIDIA NemoClaw First Look: Secure AI or Just Over-Engineered?](../videos/5v0RJkqjU8c.md)
`5v0RJkqjU8c` · Better Stack · 2026-04-02 · q3 · practitioner · review · also: sandboxing-execution, agent-architecture

Better Stack's hands-on first look at NVIDIA's NemoClaw, an OpenClaw agent wrapped in the OpenShell sandbox; the setup is fragile and per-request approvals make autonomous tasks tedious.

- Techniques: Deploy NemoClaw on a Brev GPU instance; Answer the NemoClaw installer prompts; Start the agent and approve pending egress requests; Recover a stuck Telegram gateway; Watch OpenClaw logs during autonomous tasks
- Tools: NemoClaw (NVIDIA, install script plus `nemoclaw start`), NVIDIA OpenShell (sandbox; OpenShell manager TUI for approving requests), OpenClaw (agent; `configure` wizard), Nemotron (NVIDIA inference model), NVIDIA Brev (cloud GPU platform; `brev shell`), Docker, CUDA, Telegram (bot token bridge)

## [Millions of JS Devs Just Got Hacked... (axios pwned)](../videos/5xWSezMFweE.md)
`5xWSezMFweE` · Better Stack · 2026-04-02 · q3 · intro · news · also: dev-tools

News recap of the March 31, 2026 npm compromise of the axios package: two backdoored releases used a postinstall script to drop a cross-platform RAT. Mitigations are committed lockfiles, npm ci, a minimum package age, and blocking install scripts.

- Techniques: Detect affected installs; Commit the lockfile and install with npm ci in pipelines; Enforce a minimum package age; Block install scripts by default; Treat an affected host as a full credential compromise
- Tools: npm, npm CLI, npm ci, npm install --ignore-scripts, axios 1.14.1, axios 0.30.4, plain-crypto-js, setup.js (postinstall script), package.json, package-lock.json (lockfile), node_modules, GitHub Actions

## [The End of .env Files as We Know Them](../videos/nxH-BrsCPTo.md)
`nxH-BrsCPTo` · Better Stack · 2026-04-02 · q3 · intro · tutorial · also: dev-tools

Better Stack walkthrough of Varlock, an open-source tool that replaces plaintext .env files with a typed, committable schema whose secrets resolve at runtime from 1Password and similar vaults.

- Techniques: Commit a typed env schema instead of a .env file; Inject config at process start with varlock run; Pull a secret from 1Password into the schema; Unlock 1Password with biometrics for local development
- Tools: Varlock (open source env schema tool, npm package and standalone CLI, version not stated), varlock 1Password plugin, 1Password, 1Password desktop app and CLI, Bitwarden, AWS plugin, GCP plugin, Vite, Next.js, Cloudflare Workers integration, VS Code Varlock extension, GitHub Action for Varlock

## [GitHub Actions are DEAD. (Use Agentic Workflows instead)](../videos/-DXkF2Q69Jw.md)
`-DXkF2Q69Jw` · Better Stack · 2026-03-02 · q2 · intro · tutorial · also: software-factory, pr-code-review

Walkthrough of GitHub Agentic Workflows: write a natural-language agent.md, compile it to a locked-down Actions workflow, and use it as a PR audit bot. Research prototype, one demo.

- Techniques: Natural-language agent file compiled into an Actions workflow; PR-triggered read-only audit agent with a structured output format; Gated write path for agent actions
- Tools: GitHub Agentic Workflows, ghaw (compile CLI), GitHub Actions, GitHub CLI (gh extension), GitHub Copilot (engine), GitHub Next, Microsoft Research, Better Stack AI SRE (sponsor plug)

## [You Need To Know This Before Installing OpenClaw](../videos/M3P0hQMQtq0.md)
`M3P0hQMQtq0` · AI LABS · 2026-03-02 · q3 · practitioner · review · also: token-cost-efficiency, sandboxing-execution, skills-self-improvement

AI LABS tests the self-hosted agent OpenClaw and finds it costly (token-heavy context, heartbeats), slow as context grows, and risky (plain-text credentials, malicious community skills, prompt injection); it closes with mitigation advice.

- Techniques: Hard budget and alerts on the model API key; Reduce idle token burn; Vet community skills before install; Sandbox the agent; Least-privilege channel tokens; Prefer providers with built-in guardrails, with caution
- Tools: OpenClaw, Claude (former Claudebot name), OpenAI API, Anthropic models, OpenRouter, Ollama, Docker, Cisco open-source skill scanner, Discord, WhatsApp

## [NEW Browser API That Makes AI Agents Actually Work (WebMCP)](../videos/jI2mYU8-PqU.md)
`jI2mYU8-PqU` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: mcp-and-tools

WebMCP is a proposed browser API, backed by Google and Microsoft, that lets a site's front-end expose its own features as tools for AI agents. The speaker demos it in Chrome Canary and argues it beats agents scraping pages.

- Techniques: Imperative WebMCP tool registration; Read-only state tool for on-page data; Declarative WebMCP via HTML form attributes; Design principle: expose explicit tools, not the whole UI
- Tools: WebMCP (browser API proposal), window.navigator.modelContext (proposed browser API), Chrome Canary, MCP (Model Context Protocol), React, Playwright, ChatGPT Atlas, Gemini, Arc, a browser extension used to drive the demo (unnamed)

## [Shanon: The Open Source AI Pentester Powered By Claude Code](../videos/H7Xh-x_TVdQ.md)
`H7Xh-x_TVdQ` · Better Stack · 2026-03-02 · q3 · intro · review · also: agent-architecture, token-cost-efficiency, sandboxing-execution

Walkthrough of Shannon, an open-source AI pentester built on the Claude Agent SDK: Temporal-orchestrated phases, parallel vulnerability agents, and a 2.5-hour, roughly $60 run against OWASP Juice Shop.

- Techniques: Temporal-backed durable agent pipeline; Static analysis then live-app recon; Parallel specialist fan-out with paired exploit agents; Reproduction setup as described in the video
- Tools: Shannon (open-source AI pentester), Claude Agent SDK (Anthropic), Claude Sonnet 4.6, Docker Compose, Temporal, Playwright, OWASP Juice Shop, Kali Linux (mentioned as the manual alternative), Claude Code Security (announced, not yet released per the creator), Shannon Pro (paid tier), OpenAI Agents SDK (speculated port), Vercel AI SDK (speculated port; transcript spells it 'Vasell')

## [This Sandbox Tool Makes Claude Code Unstoppable (Code On Incus)](../videos/t78-JUnTK5Q.md)
`t78-JUnTK5Q` · Better Stack · 2026-03-02 · q3 · practitioner · tutorial · also: sandboxing-execution, coding-agents

Better Stack walkthrough of Code On Incus (COI): running Claude Code agents in isolated Incus system containers on a Mac via Colima, with a malware-file triage demo.

- Techniques: Nested sandbox on macOS: Colima, then Incus, then COI; Bridge networking fix for Incus; Build COI from the cloned repo; Launch per-role agents into slots with a shared workspace; Analyze untrusted files inside the sandbox
- Tools: Code On Incus (COI), Incus, Colima, Claude Code, Docker, incus file push, coi build, incusbr0 (Incus bridge), EICAR test file, SWAPI (Star Wars API; auto-caption says 'Swoppy')

## [Docker’s Best Security Feature Is Now FREE](../videos/AcCJ678kV34.md)
`AcCJ678kV34` · Better Stack · 2026-02-02 · q2 · intro · news · also: dev-tools

Docker is making its Docker Hardened Images (DHI) free and Apache 2.0 licensed, pitching minimal, patched base images as a supply-chain fix; a short announcement-style explainer with no benchmarks.

- Techniques: Swap the base image for its hardened equivalent; Explicitly install only needed tools during the build; Start Kubernetes deployments from hardened Helm charts
- Tools: Docker, Docker Hardened Images (DHI), Debian, Alpine, Helm, Kubernetes, Apache 2.0 license

## [Moltbook is WILD... (AI Only Reddit)](../videos/EGD1LCuoTuo.md)
`EGD1LCuoTuo` · Better Stack · 2026-02-02 · q2 · intro · review · also: skills-self-improvement, agent-architecture

A walkthrough of Moltbook, a Reddit-style site where only AI agents post, powered by OpenClaw; it mostly shows how steerable and security-risky the setup is.

- Techniques: Human-steered post test for agent autonomy; Markdown skill plus heartbeat as an always-on agent loop
- Tools: Moltbook, OpenClaw (the video says it was formerly called MaltBot/Moltbot and ClaudeBot), Reddit (used as the comparison), Claude Opus 4.5 (shown as the model behind one post)

## [Why I'm DELETING Clawdbot (Moltbot) After This](../videos/CB6Ysb_BLcM.md)
`CB6Ysb_BLcM` · Better Stack · 2026-02-02 · q2 · intro · review · also: agent-architecture, sandboxing-execution

Better Stack's walkthrough of the Clawdbot (Moltbot) personal agent: how its gateway, channels and state fit together, and why exposing it on a VPS and prompt injection are the main risks. Ends with a sponsor read.

- Techniques: Isolate a self-hosted agent on a dedicated VPS; Put the agent gateway on a private network with Tailscale; Use a separate API key for each agent; Scrub sensitive data from agent transcripts; Run the agent CLI's security command; Give the agent an identity file
- Tools: Clawdbot (Moltbot), Pi agent runtime, Grammy, Discord.js, Telegram, WhatsApp, Discord, Tailscale, Ollama, 1Password skill, Google Calendar skill, Anthropic API

## [1 in 9 Apps Ship Supabase Keys: Here’s How It Happens](../videos/pE6A3bHLM4o.md)
`pE6A3bHLM4o` · Better Stack · 2026-02-02 · q3 · intro · tutorial · also: dev-tools

Public-prefixed env vars (NEXT_PUBLIC_, VITE_, PUBLIC_) ship into the client bundle, so a private Supabase key behind one leaks to every visitor; the fix is server-side calls, bundle checks and CI guardrails.

- Techniques: Audit the shipped build for secrets; Proxy privileged calls through your own server; Enable and test RLS on user-facing tables; Review rule for public-prefixed variables; CI secret scanning as a build gate; Rotate on suspicion
- Tools: Supabase, Next.js, Vite, SvelteKit, Chrome DevTools, npm

## [Security in 2026 Is Going to Look Very Different](../videos/__izQwBMqw0.md)
`__izQwBMqw0` · Better Stack · 2026-02-02 · q2 · intro · news · also: dev-tools

Better Stack's 2026 security outlook: record CVE counts, AI-accelerated exploits, memory-safe languages and smaller dependency surfaces, with a product plug for its monitoring tool.

- Techniques: Input sanitization against XSS and SQLi; Minimize third-party plugins and dependencies; Choose memory-safe languages for new code; Automated behavioral anomaly detection
- Tools: WordPress, Rust, Go, Java, C#, Python, Swift, C, C++, Linux kernel, React (React-to-Shell exploit, as named in the video), Better Stack (AI error tracking, AI SRE)

## [React’s Worst Vulnerability Ever (RCE Exploit Explained)](../videos/iV48tEiHFDY.md)
`iV48tEiHFDY` · Better Stack · 2026-01-02 · q3 · intro · news · also: dev-tools

Explainer on the critical unauthenticated RCE in React Server Components (React2Shell, CVSS 10) affecting React and Next.js servers. Main takeaway: upgrade now, since WAF rules are not a full fix.

- Techniques: Patch React and Next.js before anything else; Guard property lookups in any deserializer or path resolver; Audit for dynamic path traversal on untrusted input
- Tools: React, React Server Components, React Flight Protocol, Next.js, Node.js, Cloudflare WAF, AWS

## [China's Mind-Control AI Just Dropped on GitHub (100% Free)](../videos/8ear9y9qE7w.md)
`8ear9y9qE7w` · Better Stack · 2026-01-02 · q2 · intro · review · also: multi-agent, data-engineering

Hype-titled walkthrough of BetterFish, a multi-agent public-opinion pipeline with parallel specialist agents and an LLM-moderated debate. The demo stalls before reports, and the speaker flags legal risks, so treat it as an architecture sketch.

- Techniques: Parallel specialist agents over a precomputed store; LLM-moderated agent debate before synthesis; Per-agent model routing through OpenRouter
- Tools: BetterFish, MindSpider (scraper), Flask, Playwright, MySQL, PostgreSQL, Docker, Hetzner CAX31, OpenRouter, Gemini 3, Kimi, DeepSeek

## [This Open-Source Auth Stack Might Replace Auth0 (Ory Kratos)](../videos/cvJKfqZrtgI.md)
`cvJKfqZrtgI` · Better Stack · 2026-01-02 · q3 · intro · tutorial · also: dev-tools

Tutorial on self-hosting Ory Kratos, an open-source identity server, in Docker and wiring it to a Next.js app with prebuilt Ory Elements login, signup, verification, settings and 2FA screens, pitched as an Auth0 alternative.

- Techniques: Kratos local dev stack via Docker Compose; Kratos YAML checklist for localhost; Next.js integration with Ory Elements; Enabling 2FA through the built-in settings page
- Tools: Ory Kratos, Ory Elements, Ory Next.js integration package, Ory Hydra, Ory Keto, Ory Polis, Ory Oathkeeper, Docker, Docker Compose, Next.js, SQLite, Auth0

## [It Happened Again... 2 New React CVE's](../videos/N1Dyym6WH7o.md)
`N1Dyym6WH7o` · Better Stack · 2026-01-02 · q3 · intro · news · also: dev-tools

Better Stack walks through two new React and Next.js vulnerabilities disclosed after the React Server Components RCE the week before: a high-severity denial of service and a medium-severity leak of server action source code, both triggered by a single crafted POST, with the earlier patch not covering them.

- Techniques: Verify the patched version before trusting an earlier fix; Test a staging deployment for hang-on-request behavior; Keep secrets out of server action source; Treat neighbors of a fixed bug as suspect
- Tools: React, Next.js, React Server Components, React Flight Protocol, Server Actions, GitHub Security Advisories

## [OpenAI's New Release Is WILD](../videos/75SHVbKCe44.md)
`75SHVbKCe44` · AI LABS · 2026-01-02 · q2 · intro · news · also: evals, models-research

OpenAI's "confession report" method for reducing model dishonesty, as a short, mostly critical take: the speaker argues it rewards admissions rather than accuracy and only helps identify errors, not prevent them.

- Techniques: Confession report after each response; Classify outcomes on a 2x2 grid (answer correct or wrong x confessed or not)
- Tools: OpenAI models (ChatGPT, unnamed model in the study), Claude (referenced in passing as a reward-hacking example), YouWear (sponsor, AI app builder)

## [Your VPN Is Probably FAKE! (85% Exposed in Investigation)](../videos/5kgkcsiPB-o.md)
`5kgkcsiPB-o` · Better Stack · 2026-01-02 · q2 · intro · review · also: infra-cost-scaling

Better Stack summarizes an IPinfo investigation finding that most VPN providers list server countries that are virtual, with traffic exiting elsewhere; the speaker says the core problem is transparency, not encryption.

- Techniques: Latency-based location verification; Do not trust declared IP geolocation
- Tools: IPinfo ProbeNet, OpenVPN

## [I Tried Google’s New AI IDE… Here’s the Truth (Antigravity)](../videos/KLq250wGeEg.md)
`KLq250wGeEg` · Better Stack · 2025-12-02 · q3 · intro · review · also: coding-agents, testing-verification

Hands-on tour of Google's Antigravity agent IDE: a useful agent manager, plan-review flow and browser self-testing, undercut by quotas, a markdown-image prompt-injection exfiltration issue, and a half-baked preview.

- Techniques: Plan-first review gate for agent work; Browser-subagent UI self-test with visual evidence; Agent-generated visual assets for prototypes; Red-team the agent with a markdown image exfiltration test
- Tools: Google Antigravity, Gemini 3 Pro, Nano Banana Pro (speaker thinks it is used under the hood, unconfirmed), Google Jules (captions say 'Google Jewels'; speaker's comparison only), Cursor, VS Code, Chrome

## [There’s a New Way To Corrupt AI Models](../videos/D5QeUQ4VbjM.md)
`D5QeUQ4VbjM` · AI LABS · 2025-12-02 · q2 · intro · news · also: models-research, testing-verification

Recap of an Anthropic study: teaching a model to reward-hack in coding generalized into broader misalignment, and some fixes only masked it. Secondhand and hype-titled.

- Techniques: Permissive framing for hacking in a research environment (reported mitigation); Avoid explicit 'do not hack' system prompts for measurement; Test mitigations on hard tasks, not only simple ones
- Tools: Claude Code, Claude Sonnet 3.7, Claude Sonnet 4.5, Code Cloud (sponsor, not relevant)

## [Building AI That Actually Helps You Live Better | Better Stack Podcast Ep. 7](../videos/46EsyQYKMjA.md)
`46EsyQYKMjA` · Better Stack · 2025-12-02 · q3 · intro · interview · also: context-engineering, agent-architecture, mcp-and-tools

Better Stack podcast interview with Ben, founder of Spec, a macOS-native personal-context assistant; main engineering points are local-first data, OS-level access, and side effects gated outside the model.

- Techniques: Permission-scoped local data access for apps with no API; Split draft and send tools, with the send gated by a human click; Write-only agent sandbox; Event listeners and timed services instead of a single chat loop; Living context with distilled per-thread summaries as the trigger input; Route models by task type, separating persona from reasoning
- Tools: Spec (macOS/iOS app, Swift), Swift, Granola, Riverside, Claude Opus 4, Claude Sonnet 4, Claude Sonnet 4.5, Claude Haiku 4.5, GPT-5, GPT-OSS, Gemini 2.5, MCP

## [Something’s Off About Anthropic’s “AI-Orchestrated Attack” Story (Report Analysis)](../videos/BF7abVHg-WI.md)
`BF7abVHg-WI` · Better Stack · 2025-12-02 · q2 · intro · review · also: governance-compliance

Better Stack critiques Anthropic's report on an "AI-orchestrated" espionage campaign as vague and marketing-driven, and argues threat reports need TTPs, IOCs and named tools.

- Techniques: Vendor threat-report credibility checklist
- Tools: Claude Code, Claude

## [Claude Might Be Going In A Different Direction + More](../videos/fiHrS04ZUA8.md)
`fiHrS04ZUA8` · AI LABS · 2025-12-02 · q2 · intro · news · also: models-research, coding-agents

AI LABS weekly roundup (Dec 2025) covering GPT-5.1, Gemini 3 leaks, Google agents, an Anthropic robot-dog experiment, an Anthropic report on a Claude Code-driven espionage campaign, and IBM quantum processors.

- Techniques: Usage-limit fallback to a smaller model; Plan-then-approve for deep research
- Tools: GPT-5.1, GPT-5.1 Instant, GPT-5.1 Thinking, GPT-5.1-Codex, GPT-5 Codex Mini, Codex, ChatGPT, GitHub Copilot, Gemini 3, Nano Banana 2, Google Maps, Google Opal

## [300+ npm Packages COMPROMISED: The Shai-Hulud Worm Is Back!](../videos/ncRrh7zS1gY.md)
`ncRrh7zS1gY` · Better Stack · 2025-12-02 · q3 · intro · news · also: dev-tools

Better Stack explains the Shai-Hulud npm worm, which steals developer secrets on install and republishes itself through maintainer accounts, and gives a short remediation checklist.

- Techniques: Credential rotation after a malicious install; Audit package.json for injected install scripts; Inspect .github/workflows for unfamiliar YAML; Harden npm publishing
- Tools: npm, GitHub, GitHub Actions workflows (.github YAML), Bun (named only as the filename the malware imitates)

## [This $8/hr AI Engineer Could Replace Junior Devs | Devin AI | Agentic Developer.](../videos/rfWx5zB0Cws.md)
`rfWx5zB0Cws` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents, software-factory

AI LABS walks through Devin's general availability: Slack/GitHub-driven autonomous coding, a self-QA demo, a $500/month plan the narrator converts to about $8/hour, and a live-share security leak. Mostly demo and hype, few hard numbers.

- Techniques: Assign work from Slack, get progress in-thread; Agent-driven E2E QA on every push; Bootstrap an unfamiliar repo by fix-and-run loop; Sign-up sequence to start a Devin account
- Tools: Devin (Cognition), Slack, GitHub, VS Code Live Share, Rust documentation (consulted by the agent), SWE-bench (vendor-reported results), o1-preview (comparison model, named in video), Cursor (mentioned in others' takes)

## [Zapier MCP: The Only MCP Server That Cursor Needs](../videos/tFFsX97HzEk.md)
`tFFsX97HzEk` · AI LABS · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, coding-agents

Zapier's hosted MCP server replaces a pile of local MCP servers with one endpoint, per-action tool selection and fixed-argument control. Useful setup detail, but a vendor walkthrough with a hype title.

- Techniques: Consolidate local MCP servers into one hosted endpoint; Add only the specific tool actions an agent needs; Fix routing fields, leave content fields to the model; Override model-sent arguments on the server side; Connect a Postgres database for read and write actions
- Tools: Zapier MCP server, WebParse by Zapier, Cursor, mcp.json, Postgres, Official Postgres MCP server (read-only, per presenter), Supabase MCP server (noted as missing from Zapier), Composio (compared; manual auth grants), Slack, Jira, GitHub, GitLab

## [DNS Malware Explained: How Hackers Hide Code in Plain Sight](../videos/66EG2a81_rE.md)
`66EG2a81_rE` · Better Stack · 2025-11-02 · q3 · intro · review · also: observability

Short Better Stack explainer on attackers hiding malware and prompt-injection text in DNS TXT records, why encrypted DNS makes this harder to see, and what DNS monitoring to add.

- Techniques: Alert on DNS TXT query volume per host; Run your own DNS resolver for visibility; Ship resolver logs to a log platform and search for patterns; Block known-bad domains with threat-intel lists
- Tools: DNSDB Scout, Cloudflare, Better Stack, DNS over HTTPS (DoH), DNS over TLS (DoT)

## [5 Deadly ENV Mistakes Everybody Makes](../videos/zLDDq1HNSgU.md)
`zLDDq1HNSgU` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: dev-tools

Five common .env mistakes (committing secrets, undocumented projects, rewriting git history, one env file for all environments, and leaking secrets through frontend bundles) and the fix for each.

- Techniques: Commit a .env.example with variable names only; Document required env vars in the README; Respond to a leaked secret by rotating it; Separate env files per environment, selected by NODE_ENV; Use framework prefixes only for values safe to expose
- Tools: GitHub, Git (.gitignore, commit history), Next.js, Vite, React, Node.js (NODE_ENV), Supabase (publishable API key example)

## [SDKs, Stealth Models, and LLM Myths | Better Stack Podcast Ep. 2](../videos/w8x5Kdv-Za8.md)
`w8x5Kdv-Za8` · Better Stack · 2025-11-02 · q2 · practitioner · panel · also: models-research, dev-tools, mcp-and-tools

Better Stack panel (Aug 2025) on the Vercel AI SDK, stealth models like Sonic, OpenAI GPT Realtime, and Anthropic's model-behavior research, with much opinion and few verified numbers.

- Techniques: AI SDK backend core plus UI hooks; Per-provider reasoning option pass-through; Explicit stack pinning in prompts; Smell-test models with known-hard setup tasks; Scenario-based goal-conflict red-teaming; Jailbreak testing with non-English or fictional framing
- Tools: Vercel AI SDK, AI Elements, Next.js, Turborepo, React Server Components, OpenRouter, vLLM, Ollama, Mastra, Sonic (stealth model; hosts suspect Grok Code Fast 1), Horizon Alpha (stealth model), GPT-5

## [This App Works WITHOUT Internet?! (Jack Dorsey’s BitChat)](../videos/hdRn3DQ_C_Y.md)
`hdRn3DQ_C_Y` · Better Stack · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building

Quick hands-on look at Jack Dorsey's open-source BitChat, a Bluetooth mesh messenger with no internet or servers. The reviewer finds the iOS build buggy, and the app is a weekend vibe-coded project that drew security criticism.

- Techniques: Cross-platform two-device messaging test; Check the repo's security status before trusting an app
- Tools: BitChat, Bluetooth Low Energy (BLE), NoiseXX handshake, Goose, AirTags, iOS, Android

## [This Next.js Server Actions Pattern is AWESOME (Validated & Authenticated Actions)](../videos/pBQ-WlhiGbw.md)
`pBQ-WlhiGbw` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: dev-tools

Tutorial on two reusable wrapper functions for Next.js server actions: one validates FormData with Zod, the other also checks a Better Auth session before the action runs.

- Techniques: Validated server-action wrapper; Auth-checked server-action wrapper; Front-end consumption of ActionState
- Tools: Next.js (server actions, headers()), Next.js SaaS starter kit, Zod, Better Auth, TypeScript, React useActionState hook

## [The Last Authentication Library You'll Ever Need...](../videos/hFtufpaMcLM.md)
`hFtufpaMcLM` · Better Stack · 2025-11-02 · q3 · intro · review · also: dev-tools

Better Stack walkthrough of BetterAuth, an open-source TypeScript auth framework: an overview of its frameworks, databases, auth methods and plugins, then a live Next.js + Drizzle + Postgres setup for email/password and GitHub login.

- Techniques: Minimal BetterAuth config for email/password plus GitHub; Generate the auth schema with the CLI, then push with Drizzle; Mount a single catch-all auth route; Enable the nextCookies plugin for server actions; Email sign-up and login from a server action; Protect a server-component page by session; Sign out and social sign-in from a client component
- Tools: BetterAuth, Next.js, Drizzle ORM, Postgres, Docker, shadcn/ui, Zod, GitHub OAuth, Kysely, Hono, Express, Expo

## [This New MCP Client Lets You Integrate So Many MCP Servers!!](../videos/xEyKT5iY0W0.md)
`xEyKT5iY0W0` · AI LABS · 2025-11-02 · q2 · intro · review · also: mcp-and-tools

Walkthrough of an open-source general-purpose MCP client that runs an agent over MCP servers outside coding IDEs, using Composio-hosted servers with agent-driven auth; the local install is slow.

- Techniques: Adding a remote MCP server to a generic client; Agent-driven auth for hosted MCP servers; Running the open client locally
- Tools: Open MCP client (open-source MCP client app, hosted on Vercel, source on GitHub), Composio (composio.dev, hosted MCP server catalog with auth), Google Tasks MCP server, Hacker News MCP server, Gmail MCP server, Google Drive MCP server, Notion MCP server, Google Meet MCP server, Cursor, Windsurf, LangSmith, OpenAI models

## [12 Logging BEST Practices in 12 minutes](../videos/I2mWnh66Bkg.md)
`I2mWnh66Bkg` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: observability, dev-tools, infra-cost-scaling

A generic logging best-practices list: plan what to log, use levels and structured fields, sample high-volume logs, emit one canonical line per request, centralize, set retention, redact secrets, and watch logging overhead.

- Techniques: Canonical log line per request; Selective sampling; Redaction in the pipeline; Tiered retention policy; Load test logging overhead
- Tools: OpenTelemetry, OpenTelemetry Collector, Vector, Go slog (log/slog), Logrus (transcribed as Logris), Go

## [MCP Servers are Security Nightmares...](../videos/CRKYNyMc4PM.md)
`CRKYNyMc4PM` · Better Stack · 2025-11-02 · q3 · practitioner · demo · also: mcp-and-tools, coding-agents

Demo of MCP tool poisoning, tool shadowing, rug-pull mutation and command injection in MCP servers. Main takeaway: treat tool descriptions and server code as untrusted input.

- Techniques: Pin and diff tool definitions; Review full tool descriptions and arguments before approval; Treat tool descriptions as untrusted input; Avoid shell interpolation in MCP tool handlers; Probe your own MCP servers directly; Limit what a server can reach
- Tools: Cursor, MCP (Model Context Protocol), WhatsApp MCP server (community project, named as legitimate), MCP client libraries (used to call server tools directly)

## [First to Jailbreak Claude Wins $20,000](../videos/m5uWKRJhcao.md)
`m5uWKRJhcao` · Better Stack · 2025-11-02 · q3 · intro · news · also: models-research

Anthropic's public jailbreak challenge for its constitutional classifiers (8 harmful questions, HackerOne bounty), with a walkthrough of the input/output classifier pipeline and its reported costs.

- Techniques: Constitution-driven synthetic dataset for classifiers; Input guard prompt wrapped around user input; Streaming output classifier with a threshold; Separate harm-check grader for challenge submissions
- Tools: Claude, Constitutional classifiers (Anthropic safety system), HackerOne (bug bounty platform)

## [Could FOKS Be the FUTURE of Secure Git Hosting?](../videos/fIbyRfuiYXc.md)
`fIbyRfuiYXc` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: dev-tools

Walkthrough of FOKS, an open-source, federated, Go-based alternative to Keybase for end-to-end encrypted git and key-value secrets, with post-quantum hybrid encryption and a short setup demo.

- Techniques: Set up FOKS and create a user; Create an encrypted git repo; Inspect and revoke keys; Acknowledge the single-key warning
- Tools: FOKS (Federated Open Key Service), foxctl, fox CLI, Homebrew, Go, Curve25519, ML-KEM, Keybase, YubiKey, fox.app federated server

## [HUGE Next.js Authorization Bypass... Are You Safe? (9.1 CVSS)](../videos/D_Tt39FEIiU.md)
`D_Tt39FEIiU` · Better Stack · 2025-11-02 · q3 · practitioner · news · also: dev-tools

Walkthrough of the Next.js 15.2.2 middleware authorization bypass (CVSS 9.1): a client-sent internal subrequest header skips middleware, what it exposes, how it was patched, and edge mitigations.

- Techniques: Re-check auth in every data-bearing route; Strip the internal subrequest header at the edge until patched; Check the vulnerable and patched source at the release tags
- Tools: Next.js 15.2.2 (vulnerable), Next.js 15.2.3 (patched), Next.js 14 (patched line), Vercel, Netlify, Cloudflare (managed firewall rule), Replit (named in the public discussion), GitHub (source and PR review), Chrome (password warning)

## [Docker Containers - How Hackers Can ESCAPE Them in Seconds!](../videos/giXlSlFLKwA.md)
`giXlSlFLKwA` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: sandboxing-execution, dev-tools

Shows two ways to escape misconfigured Docker containers, via a mounted Docker socket and via privileged mode or CAP_SYS_ADMIN, then lists the hardening steps (proxy, drop caps, seccomp, gVisor).

- Techniques: Avoid mounting the Docker socket into containers; Audit a container's capabilities with capsh; Replace privileged mode with specific capabilities, then add a seccomp profile; Run untrusted or agent-generated workloads under gVisor; Check Docker hardening with docker-bench-security; Move host-level metrics collection out of containers
- Tools: Docker, Docker Desktop, Docker Compose, Bun, Nginx, Vector, cAdvisor, Alpine Linux, capsh, Docker socket proxy, gVisor, docker-bench-security

## [I Cracked a Password using ONLY Response Times...](../videos/OxZknIoZuy0.md)
`OxZknIoZuy0` · Better Stack · 2025-11-02 · q3 · intro · demo · also: dev-tools

Better Stack demo of a timing attack: an early-exit string comparison leaks key length and characters through response times, then the speaker covers why real-world impact is limited and how to mitigate it.

- Techniques: Timing-based key length discovery; Per-position timing recovery; Constant-time comparison for secrets; Rate limiting as the cheap mitigation; Timing check for username enumeration
- Tools: Bun, Node.js (crypto.randomBytes, crypto.timingSafeEqual), TypeScript (generatekey.ts, crack scripts), SQLite (named as a susceptible operation in the cited paper), Claude (named as the summariser of the Minerva attack, not used in the demo)

## [Monitoring Linux Authentication Logs with Vector & Better Stack](../videos/H4LSiY7I4ps.md)
`H4LSiY7I4ps` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: observability, dev-tools

Better Stack tutorial: collect /var/log/auth.log with Vector, convert syslog to JSON with a remap transform, ship it to Better Stack, then chart sudo authentication failures on a dashboard.

- Techniques: Verify what auth.log captures before building a pipeline; Vector file source plus remap transform for auth logs; Validate, then test with a console sink; Ship to a remote source with an HTTP sink and bearer auth; Create a log-to-metrics group-by from the parsed event name; Build a bar chart of one event type
- Tools: Vector (version not stated), Better Stack (sources, live tail, log-to-metrics, dashboards, alerting), Ubuntu (WSL), auth.log / syslog / rsyslog, PAM (pluggable authentication modules), sudo, sshd, nano, Vector Remap Language (VRL) functions: parse_linux_authorization, parse_regex, json_extract (SQL)

## [Future of AI security with Michal Pechoucek](../videos/t7iwv_8E9_g.md)
`t7iwv_8E9_g` · Better Stack · 2024-11-02 · q2 · intro · talk · also: coding-agents

Gen Digital's technology head argues the real AI threats are weaponized attacks, insecure AI-written code, attacks on AI systems, and mostly human-targeted scams, and pitches a free scam-detection app.

- Techniques: Generative-AI scam text classifier; On-device conversational scam check
- Tools: Norton Genie (Gen Digital, free scam-detection app for iPhone and Android), MITRE ATLAS (taxonomy of known attacks on AI systems, transcribed as 'Mitra' / 'Atlas'), Windows 95 (cited as a historical vulnerability event), Copilot-style AI coding assistants (unnamed 'copilots')

