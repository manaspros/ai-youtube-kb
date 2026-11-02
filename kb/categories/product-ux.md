# product-ux — 211 videos

*AI product design, UX for agents, PM, building AI startups, go-to-market*

By channel: AI Engineer 159 · Kai Explains 2 · AI LABS 29 · Better Stack 21

**Synthesized guide:** [guides/product-ux.md](../guides/product-ux.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [Your AI Pilots Won't Move the P&L. Here's What Will - Adam Nahari, Apollo](../videos/vUJDyDnqT4c.md)
`vUJDyDnqT4c` · AI Engineer · 2026-11-02 · q3 · intro · talk · also: enterprise-adoption, governance-compliance

Adam Nahari (Apollo) argues AI pilots fail to move EBIT because most spend goes to general tools and change management, and sets out six moves (pick one or two P&L-linked problems, redesign the process end to end, get CEO sponsorship, build with the business, put tools in everyone's hands, pre-set kill metrics) to make AI show up in margin.

- Techniques: Work-backward use-case screen; End-to-end workflow redesign over assistive tooling; Embedded domain champions in the build loop; Pre-registered kill gates; At-scale unit economics check

## [I Don't Fear AI Slop. I Fear Untold Stories - Zack Proser, WorkOS](../videos/1et3Lb_KLQo.md)
`1et3Lb_KLQo` · AI Engineer · 2026-11-02 · q3 · intro · talk · also: enterprise-adoption

WorkOS's Zack Proser argues you should encode your taste into an AI "factory" and hand it to others. Examples: an internal blog-drafting bot and a bedtime-story app. A named human still signs off.

- Techniques: Codify your taste as a fixed pipeline, then expose it behind a simple interface; Connector-backed context assembly before drafting; Draft, iterate in plain language, then human sign-off; Four-question review rubric for AI-assisted output; Playtest a factory with a small audience and measure repeat use
- Tools: BlogBot (internal WorkOS blog-drafting system; name as stated in talk), Cloudflare (hosting for BlogBot), Slack (entry point for colleagues), Granola (meeting recordings as a data source), Claude Opus (captioned as 'Opus 5-5 extra high'; the version string is uncertain from auto-captions)

## [Most of Your Docs Readers Are Now AI Agents - Hahnbee Lee, Mintlify & Lincoln Murr, Coinbase](../videos/YX4Z4XqZ9Vo.md)
`YX4Z4XqZ9Vo` · AI Engineer · 2026-11-01 · q2 · intro · interview · also: mcp-and-tools, enterprise-adoption

A Mintlify and Coinbase fireside chat on designing docs and APIs for agent readers and agent payments; mostly opinion, with one notable agent-traffic stat and a closing build-vs-buy plug.

- Techniques: Keep docs lean for agent readers; Track agent share of docs traffic; Automate doc upkeep, keep prose human; Expose the product as APIs first, then wrap; Pay per call with a wallet instead of API keys
- Tools: Mintlify, x402, MCP, CLI, API, OpenClaw

## [78% Wanted This AI Feature. Almost Nobody Used It - Supriya Subudhi, Bumble](../videos/CvmZtAPmAW4.md)
`CvmZtAPmAW4` · AI Engineer · 2026-10-31 · q4 · practitioner · talk · also: evals, token-cost-efficiency, governance-compliance

Bumble's Supriya Subudhi argues that a positive A/B test is only the start for AI features, and lays out five checks: real adoption, tail-of-distribution outputs, cost versus benefit, model cost-quality tradeoffs, and legal market readiness.

- Techniques: Adoption-first AI feature rollout; Segment-level eval review over averages; Guardrails on advice scope; Eval-driven model and prompt selection under a cost budget; Write down the business reason for each AI feature; Regulatory check before building
- Tools: Meta Muse AI (mentioned as an example of a US/Canada-only launch), Amazon AI shopping assistant (mentioned as an example), Spotify AI DJ (mentioned as an example)

## [He Built the First Chatbot in 1966, Then Tried to Stop It (here's why)](../videos/O1Bab7biaGo.md)
`O1Bab7biaGo` · Better Stack · 2026-10-26 · q3 · intro · demo · also: context-engineering, security-guardrails

Better Stack runs the 1966 ELIZA chatbot's original code on a Mac, explains how its keyword-rule engine and swappable script work, and ties its "Eliza Effect" warnings to today's chatbot attachment problem.

- Techniques: Keyword-ranked rule matching with pronoun reflection and template fill; Recall-on-no-match fallback; Separate engine from persona script, with runtime rule edits; Treat the script or system prompt as leakable
- Tools: ELIZA (1966 DOCTOR script), IBM 7094 (transcribed as 'IBM 1794' in the captions), SLIP list-processing language, Lisp (BBN clone), BASIC (1977 magazine version), ARPANET, ChatGPT, Inventing Eliza (MIT Press book, July release)

## [How Bridgewater Turned 100 Million Documents Into an Edge - Sam Green & Aaron Linsky, Bridgewater](../videos/CLve4Nx_RwI.md)
`CLve4Nx_RwI` · AI Engineer · 2026-10-25 · q4 · practitioner · talk · also: rag-retrieval, enterprise-adoption, data-engineering

Bridgewater's Applied AI team describes the Vault, a governed corpus of 100M+ unstructured documents, and the lessons from making it useful to both human investors and agents: separate design for each reader, benchmark-driven search, and feeding agent-human synthesis back into the corpus.

- Techniques: Hand-labelled retrieval benchmark before tuning; Cluster-aware native filtering in the vector store; Infer a time window from the question and scope retrieval to it; Separate human and agent retrieval design; Migrate existing user habits into the new tool first; Write synthesis back into the corpus
- Tools: Turbopuffer (vector database, native filtering), Bridgewater Vault (internal unstructured data platform), Aya (internal artificial investment associate), Pocket Analyst (internal AI analyst), Researcher (internal, next-generation analyst), Forecaster (internal, custom model plus foundation models), Slack, IDE integration, CLI for agents, phone app, enterprise chat client (unnamed)

## [AI Writes the Code. So What's Left for Engineers? - Laurie Voss, Arize AI](../videos/kspZP5BgkEU.md)
`kspZP5BgkEU` · AI Engineer · 2026-10-25 · q3 · practitioner · talk · also: context-engineering, pr-code-review, evals

Laurie Voss (Arize AI) argues coding agents have made code writing nearly free, so the bottleneck moves to code review, ops and security, and ultimately to defining what "good" means, which makes "product engineers" the lasting role.

- Techniques: Theory-of-constraints bottleneck mapping; Review only high blast-radius code; Automatic verification for cheap-to-check work; Turn reviewer feedback into rules; Mergeability benchmark instead of test pass rate; Measure outcomes, not output volume
- Tools: Claude Code, GitHub Copilot, Cognition Devin, Cursor Bugbot, OpenAI Codex, Claude, Pragmatic Engineer newsletter, Arize AI

## [Buying GPUs Should Work Like Buying Stocks — Carmen Li, Compute Exchange](../videos/laQ8wMysnkk.md)
`laQ8wMysnkk` · AI Engineer · 2026-10-24 · q2 · intro · talk · also: infra-cost-scaling, token-cost-efficiency

Carmen Lee (Compute Exchange / Silicon Data) pitches a neutral GPU-procurement exchange and GPU term-structure and residual-value indices; useful market context, but mostly a company talk with few reusable engineering techniques.

- Techniques: Forward-curve reading from GPU rental indices; Discounted-cash-flow residual valuation of GPU servers; Neutral exchange model for compute procurement
- Tools: NVIDIA DGX, InferenceX, MLPerf, CME futures

## [How OpenAI Built ChatGPT for Bankers and Analysts — Joseph Kim, OpenAI](../videos/opHmX7qClzE.md)
`opHmX7qClzE` · AI Engineer · 2026-10-24 · q3 · practitioner · talk · also: mcp-and-tools, enterprise-adoption, models-research

OpenAI's Joseph Kim explains how ChatGPT for Financial Services was built on the plugin platform (MCP, skills, artifact tools), why finance lagged in AI use, and his 2027 bets on finance models and persistent agents.

- Techniques: Host and index licensed data yourself, expose it through MCP; Split tool/instruction layer from domain post-training; Firm templates for generated artifacts; Citation viewers for reviewable answers; Plan features around the usefulness threshold; Build on the plugin platform building blocks
- Tools: ChatGPT, ChatGPT plugin platform, MCP (Model Context Protocol), MCP apps, Skills, Codex, Codex desktop app, Excel, PowerPoint, GPT-4

## [How to Let AI Agents Sign Up for Your App Safely — Isabelle Williams, WorkOS](../videos/uTrY8slys0w.md)
`uTrY8slys0w` · AI Engineer · 2026-10-23 · q3 · practitioner · talk · also: security-guardrails, mcp-and-tools, governance-compliance

WorkOS PM walks through letting AI agents sign up for and act inside an app safely, using AuthMD, ID-JAG identity assertions, and agent tokens scoped to a user-bounded ceiling.

- Techniques: AuthMD discovery file; Anonymous trial with claim token; ID-JAG identity assertion grant; Blueprint ceiling with scope intersection; Separate agent principal from user session
- Tools: AuthMD (open markdown-based agent onboarding protocol), WorkOS Agent Auth, ID-JAG (Identity Assertion JWT Authorization Grant, IETF spec), OAuth 2.0, MCP authorization spec (Enterprise Managed Authorization), Okta Cross App Access, Claude (referred to as Claude / Cloud Code in the transcript), Cursor (used to vibe-code the demo app), Waypoint (speaker's demo travel-planning app), Muse and Instinct (personal agents mentioned, no detail given), Maple Itinerary and Trip Ledger (other planning tools the demo agent tried)

## [Why AI Startups Will Disappear Without Compute Markets — Evan Conrad, San Francisco Compute](../videos/Wk2bUUGFC_o.md)
`Wk2bUUGFC_o` · AI Engineer · 2026-10-23 · q3 · intro · talk · also: infra-cost-scaling

Evan Conrad (San Francisco Compute) argues AI startups need compute markets because credit, deposits and forecasting risk make GPU capacity unfinanceable without liquidity; physical settlement requires operating the clusters too.

- Techniques: Build-then-sell capacity financing; Physically settled forward contracts; Take-or-pay contracts for AI capacity
- Tools: San Francisco Compute (company, compute market and operator), Junlark (former company name, as transcribed; an AI music lab), Suno and Udio (as transcribed 'Suno or UDO'; music generation products named as context), Kubernetes (via CNCF Infrastructure Group, mentioned as background)

## [This Open-Source Tool Generates UI Like Magic](../videos/AhVHtwh5k3E.md)
`AhVHtwh5k3E` · Better Stack · 2026-10-23 · q3 · intro · review · also: vibe-coding-app-building

Better Stack demos OpenUI, a spec and streamable language for generative UI, and argues it beats JSON-based UI rendering on tokens and latency. Mostly a demo with unbenchmarked claims.

- Techniques: Line-streamed generative UI DSL; Component allowlist as the UI boundary; On-demand app generation from a title; Pick model by output quality, not raw speed
- Tools: OpenUI, OpenUI Lang, OpenUI Dev React lang package, Gemini 3.8 Flash (as spoken), Cerebras, Qwen 3.8 (as spoken, likely Qwen 3), Vercel JSON Render (auto-caption reads 'Versa'), Google A2UI, ChatGPT intelligent UI (OpenAI), React, Svelte, shadcn/ui

## [The AI Content System Behind 200M Views — Sarah Chieng, Cerebras & Cova Lee, OpenAI](../videos/CFbnVpSsDFQ.md)
`CFbnVpSsDFQ` · AI Engineer · 2026-10-22 · q3 · practitioner · workshop · also: context-engineering, skills-self-improvement, voice-multimodal

Two creators (Cerebras and OpenAI DevEx) walk through a six-stage AI content pipeline: swipe-file ideation, voice-captured scripts, shot lists, agent-driven editing, captioning, scheduling and a periodic process-review skill.

- Techniques: Swipe-file reference library for agents; Build a voice skill from your own past content; Voice-first script interview; Outlier analysis against channel baseline; Two-pass shot list from a script; Organize footage before editing; Agent-driven editing via API or desktop control; Brand design system generated from your own videos; Background and visual enhancement with image generation; Fix mistakes with short inserts; Repurposing into short-form cut-downs; Scheduling with human approval; Remove AI tells from captions and prose; Weekly process-review skill
- Tools: ChatGPT, Codex (CLI, computer use; transcribed as 'Astra/Astro'), GPT-5.6 Sol Ultrafast (as named in the talk; runs on Cerebras at ~750 tokens/sec), Cerebras, Wispr Flow (transcribed as 'whisper flow'), Figma (MCP and plugins), Notion, Obsidian, HyperFrames (HeyGen), HeyGen (avatars), CapCut, Adobe Premiere

## [The Investor's Edge Lives in Their Head — Anekha Sokhal, Moshi](../videos/UHbODjuviAU.md)
`UHbODjuviAU` · AI Engineer · 2026-10-20 · q2 · intro · talk · also: governance-compliance, data-engineering

Vendor talk from Moshi's founder arguing that an investor's edge is human judgment: machines should do the data grind, while every AI claim stays traceable and the human makes the call.

- Techniques: Split grind from judgment; Per-claim traceability and measured hallucination; Deterministic multi-agent decomposition
- Tools: Moshi (the speaker's own product, described as a 24-7 quant analyst for institutional traders)

## [Why AI Agents Will Need Their Own Bank Accounts — Lincoln Murr, Coinbase](../videos/f_HwzoYrZ7s.md)
`f_HwzoYrZ7s` · AI Engineer · 2026-10-20 · q2 · intro · talk · also: governance-compliance, mcp-and-tools

Coinbase's head of AI product on agentic finance: agents that pay and grow money, the X402 HTTP 402 micropayment standard, and trust that is earned in steps. Largely a vendor pitch with some useful adoption data.

- Techniques: Gate content or APIs behind HTTP 402 micropayments (X402); Staged autonomy for agents that handle money; Delegated conditional execution; Ship features as skills that write code on the user's machine; Proactive widgets against chat cold start
- Tools: X402, Agent Kit, LangChain, Coinbase MCP, Coinbase CLI, Coinbase Advisor, GrokBot, Muse, Stripe Link, Stablecoins

## [Why AI Agents Still Won't Pay for Anything — Jan Curn, Apify](../videos/-AOxpwVeIWw.md)
`-AOxpwVeIWw` · AI Engineer · 2026-10-19 · q3 · practitioner · talk · also: governance-compliance, security-guardrails

Jan Curn (Apify) argues agents still don't pay for services because the payment funnel (need, setup, trust, buy) has friction at each step, and pay-per-use is the missing piece.

- Techniques: Exact-plus-refund for metered agent billing; Charge before work for non-trivial cost; Escrow then micro-charge (batch settlement); Curated directory as the trust layer for agent-discoverable tools
- Tools: Apify (actors marketplace, about 80k actors), X402 (Coinbase, scheme exact, upto and batch settlement), MPP (Stripe and Tempo; sessions), L402 (Lightning Labs), MasterCard Agent Pay, KYA Pay (Skyfire with Visa), AP2 (Google), ACP (OpenAI and Stripe, Agentic Commerce Protocol), TAP (Visa, Trusted Agents Protocol), UCP (Google and Shopify, Universal Commerce Protocol), ACTP (Alipay), AMP (Alipay, Agentic Mobile Protocol)

## [Buy, Build, Deploy: Using M&A to Drive AI Transformation — Prathik Naidu, Long Lake](../videos/J7n3WJnFTto.md)
`J7n3WJnFTto` · AI Engineer · 2026-10-19 · q2 · intro · talk · also: enterprise-adoption, governance-compliance

Long Lake's founding partner explains why buying services businesses and then deploying AI inside them beats selling AI agents from outside, using a J-curve and a services-economy margin argument.

- Techniques: Outcome-ownership screening filter for AI deployment targets; Value-capture math for outside-in AI vendors; J-curve tracking for AI deployment

## [AI Agents Cut 3-Day Portfolio Builds to Minutes — Jack McDonald, Apollo & Michael Manapat, Rowspace](../videos/BOWYujhIQuo.md)
`BOWYujhIQuo` · AI Engineer · 2026-10-17 · q2 · intro · interview · also: data-engineering, enterprise-adoption

Customer case study: Rowspace agents and an embedded team cut Apollo's portfolio builds from days to minutes and weekly trade recaps from hours to a one-minute report, with trust earned through per-field source validation.

- Techniques: Embedded discovery with domain teams; Per-field source precedence; Agent draft then human refinement; Automate recurring reports, keep human QA

## [The Cost of Accessibility in AI — Jemima Abu, CAIS](../videos/ZccJsdOE54M.md)
`ZccJsdOE54M` · AI Engineer · 2026-10-15 · q3 · intro · talk · also: context-engineering, skills-self-improvement, testing-verification

Jemima Abu (CAIS) argues accessibility is cheaper when built in from the start with AI agents, backed by a one-off experiment (58% lower cost, one-third the time) using a custom accessibility skill.

- Techniques: Accessibility skill for coding agents; Pre-run self-audit against a checklist; Audit the codebase before introducing an agent; Reusable component library as an accessibility lever
- Tools: Figma, Chrome Modern Web Guidance skill, WebAIM (cited study)

## [I Spent Two Years Building the Median — Hariprasad Sudharshan](../videos/0JZy5AuuQzc.md)
`0JZy5AuuQzc` · AI Engineer · 2026-10-15 · q3 · practitioner · talk · also: agent-architecture, infra-cost-scaling

Hariprasad Sudharshan argues that with rented models and harnesses, most AI-built products converge on a "median," so durable value needs a deliberate novelty, a strong opinion, and distribution.

- Techniques: Novelty budget; Three-question pre-build check; Separate model, harness and product in comparisons; Treat agent done as a median baseline; Self-hosting break-even calculator
- Tools: Claude Code, Codex, Cursor, Lovable, Replit, LlamaIndex, vLLM, Max plan

## [Every Building Is a Balance Sheet: Spatial Memory for Real-World Assets — Jordi Spranger, Spranic](../videos/Fe4aSMXsOZ4.md)
`Fe4aSMXsOZ4` · AI Engineer · 2026-10-14 · q2 · intro · talk · also: data-engineering, voice-multimodal

Jordi Spranger (Spranic, with Neo4j) pitches walk-through 3D scans stored as a time-aligned graph, so real buildings become queryable, change-tracked data for insurance and lending.

- Techniques: Repeat-capture alignment and diffing; Graph as the world model; Provenance on every observation; Natural-language query over a graph map
- Tools: Neo4j, off-the-shelf 3D scanning sensor

## [Please… Enough with the Sloppy, One-Shot SaaS Replacements — Mahmoud Abdelwahab, Railway](../videos/oixzVKMAXG0.md)
`oixzVKMAXG0` · AI Engineer · 2026-10-13 · q3 · practitioner · talk · also: coding-agents, testing-verification, skills-self-improvement

Railway's Mahmoud Abdelwahab on why agent-built internal tools feel broken: agents skip product polish (autosave, optimistic updates, undo, URL state) unless asked, so encode taste in skills, reference existing pages, and force end-to-end verification.

- Techniques: Pattern-following via existing abstractions; Named UX patterns as explicit asks; Reference-page anchoring; Taste packaged as skills; End-to-end verification loop
- Tools: Railway, Payload CMS, TanStack, Claude Code

## [We Let Our Financial Planners Write the Agents — Matthew Ragone, Range](../videos/gpmze-6ueGU.md)
`gpmze-6ueGU` · AI Engineer · 2026-10-13 · q3 · practitioner · talk · also: enterprise-adoption, skills-self-improvement, context-engineering

A financial planner at Range explains how non-engineers wrote Claude skills that drafts client work, using a five-step method: pick, teach, pack, test, ship.

- Techniques: Five-step skill build method; Narrated walkthrough as skill source; Ask-first and never-do sections in a skill; Background drafting while the expert is busy; Owner plus non-author reviewer for shared skills
- Tools: Claude

## [Stop Renting Intelligence: The Train-to-Deploy Loop for Specialized AI — Fireworks AI](../videos/13YZ1EB9hjU.md)
`13YZ1EB9hjU` · AI Engineer · 2026-10-12 · q2 · intro · demo · also: training-finetuning-rl, inference-serving

Fireworks AI talk on the train-to-deploy loop: moving from closed models to open-source models by fine-tuning (SFT, RFT, DPO) on the same platform used for hosting, with hot-loading and a training agent. Mostly a product pitch, with a few usable workflow ideas.

- Techniques: Continuous train-deploy-monitor-retrain loop; RFT with a vendor-built evaluator function; Training agent with plan approval gate; Draft model training for speculative decoding; Clone-and-compare training runs
- Tools: Fireworks AI platform, FireAttention, Weights & Biases, Qwen3 8B

## [Hiring Employable Agents + Startup Battlefield Finals — Howie Liu, HyperAgent](../videos/EEt3ZSG4a1s.md)
`EEt3ZSG4a1s` · AI Engineer · 2026-10-12 · q2 · intro · other · also: agent-architecture, multi-agent, enterprise-adoption

Howie Liu (HyperAgent) argues agents are moving toward always-on "claws" that humans unblock and orchestrate, then the video covers the Startup Battlefield finals (Kamad, Common.io, Foundry).

- Techniques: Heartbeat re-invocation for always-on agents; Human approval gate on high-impact actions; Correction-to-memory loop; Specialist triage and handoff pipeline; Deny-condition state machine for agent actions; Sandbox VM per agent thread
- Tools: HyperAgent, OpenClaw, Claude Code (workflows, fan-out to parallel agents), FFmpeg, Slack, email, Gmail, Stripe, Salesforce, WhatsApp, Google Docs, GitHub

## [Parsing the Epstein Files for JMail — Palak Agarwal & Omar Alhait, Reducto](../videos/HGfsfKaVuGY.md)
`HGfsfKaVuGY` · AI Engineer · 2026-10-12 · q2 · intro · workshop · also: data-engineering, evals

Reducto staff show how their parse-then-extract pipeline turned 3M+ messy Epstein-file PDFs into the JMail sites, then run a hands-on extraction exercise.

- Techniques: Parse-then-extract pipeline; Agentic OCR with self-correction; Schema review in a playground before deploy; Content-aware schema generation; Separate citation pass; Per-use-case prompts on specialized sub-models; Tiered evaluation with your own benchmark
- Tools: Reducto Studio, Reducto parse, split, extract, edit and classify APIs, Claude Code or Codex (paste-in setup instructions via a QR code, per the speaker)

## [Auth for Agents: Let AI Sign Up for Your Product with auth.md — Michael Grinich, WorkOS](../videos/nSkmXakJ6eo.md)
`nSkmXakJ6eo` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: security-guardrails, mcp-and-tools

WorkOS founder argues agents need their own sign-up step, and proposes auth.md, an open markdown spec that tells an agent how to register for a service without a human clicking through.

- Techniques: auth.md registration spec; Identity assertion exchange for agent sign-up; Risk-scored registration with time-boxed free access; Deferred human claim; Approval-only supervision
- Tools: auth.md, MCP, ID-JAG, Wrangler, Pi (agent harness), Claude, OpenClaw, x402, Cloudflare

## [Inside the AI Economy: What Stripe's Data Reveals — Nilofer Rajpurkar, Stripe](../videos/T3wRyXg_yVg.md)
`T3wRyXg_yVg` · AI Engineer · 2026-10-12 · q3 · intro · talk · also: enterprise-adoption, mcp-and-tools

Stripe product talk using payments data to show AI companies build fast, sell globally on day one, price by usage/credits, and build enterprise sales early; includes an agent-driven Stripe setup demo.

- Techniques: Agent-driven sandbox provisioning; Clarifying-question recommender tool plus domain skills; Guardrails on sensitive actions; Hybrid subscription plus credits pricing; Unified customer and catalog model across channels
- Tools: Claude Code, Stripe MCP server, Stripe agent skills, Stripe CLI, Stripe Checkout, Stripe Tax, Stripe Link, Intercom Fin

## [The Next Trillion Internet Users Still Don’t Have an Identity — Adi Singh, AgentMail](../videos/mBNVKkyfnE0.md)
`mBNVKkyfnE0` · AI Engineer · 2026-10-12 · q3 · intro · talk · also: security-guardrails, mcp-and-tools

Adi Singh (AgentMail) argues agent identity will be accumulated from existing human-facing surfaces like email and Slack rather than issued from scratch, and that over-tight key-card style security specs hurt adoption.

- Techniques: skill.md signup flow with inbox provisioning API; Dedicated per-agent inbox as the identity and contact point; Use existing surfaces as the bridge for new agent identity
- Tools: AgentMail, Telnyx, Clawk, OpenClaw, MCP, DKIM/SPF/DMARC, DIDs, agent cards, skill.md

## [Building AIE: Open Q&A and Feedback Session with swyx](../videos/snTZtttfL70.md)
`snTZtttfL70` · AI Engineer · 2026-10-12 · q1 · intro · other · also: enterprise-adoption

Open Q&A with swyx after the AI Engineer World's Fair: no AI-safety track, the same venue and size next year, a partner-run country model, the CFP bar, and attendee app feedback. Little engineering content.

- Techniques: Publish conference data as open JSON; Partner-run local meetups with a fixed cadence
- Tools: Twitter, LinkedIn, YouTube, Slack

## [Containment Is Lying to You: Measuring AI Agents Like Employees — Druid AI](../videos/PwCSYy-oGsM.md)
`PwCSYy-oGsM` · AI Engineer · 2026-10-12 · q3 · practitioner · talk · also: evals, governance-compliance, enterprise-adoption

Druid AI argues containment rate misleads agent evaluation and proposes a weighted, 0-2 scored framework (six pillars, 26 components) judged like an employee and re-run weekly against a human baseline.

- Techniques: Component scoring with weighted clusters; Mandate-first agent definition; Success criteria attached to each task; Weekly re-run against a human baseline; Hybrid accuracy measurement; Central handoff and action-center check; Skill-source and granularity review; Error tolerance set by mode; ROI as freed human time

## [Generation Is Cheap, Review Is Expensive: How to Stop Shipping AI Slop — Gabriel Martinez, G2i](../videos/6qkzlT962es.md)
`6qkzlT962es` · AI Engineer · 2026-10-10 · q3 · intro · talk · also: pr-code-review, context-engineering, software-factory

Gabo (G2i) argues AI slop comes from generation outrunning judgment. His fixes are conventions, small reviewable chunks, visible accountability, and ORC, an orchestration workflow built around review.

- Techniques: Single canonical pattern per concept; Diagram-first review surface; Small reviewable chunks with explicit ownership; Built-in adversarial and planning gates before merge
- Tools: ORC (G2i's orchestration system, described only at a high level), Ruby on Rails (convention-over-configuration example), SQLite (quoted maintainer comment on PR maintenance cost)

## [Why We Deleted Our MCP Server and Rebuilt It — Abhi Arya, Reducto](../videos/jJQoVkd5yLg.md)
`jJQoVkd5yLg` · AI Engineer · 2026-10-09 · q4 · practitioner · talk · also: mcp-and-tools, observability

Reducto deleted its one-tool-per-endpoint MCP server after a team rollout showed agents were confidently wrong; the rebuild uses fewer workflow-shaped tools, legible uncertainty, and session logs that feed back into guidance.

- Techniques: Workflow-shaped MCP tools instead of endpoint wrappers; Per-step next-action guidance in tool responses; Snapshot / live-state tool with specific error codes; Confidence and provenance in tool outputs fed back to the model; Evals that score clarifying questions as correct behaviour; Session logging, then mining for override and low-confidence signals; Require an explanation of what was built and why
- Tools: Claude Code, MCP, Slack, Notion, Circleback

## [Why 80% Reliability Isn't Good Enough — Felipe Blanes, Amazon AGI Lab](../videos/Emo5FGGY-wM.md)
`Emo5FGGY-wM` · AI Engineer · 2026-10-09 · q3 · practitioner · talk · also: evals, observability

Amazon AGI Lab's Felipe Blanes on why static evals fail in production: run an eval flywheel fed by real customer signals, and be transparent about product limits, since trust rises more from honesty than from higher benchmark scores.

- Techniques: Eval flywheel with customer signals; Trajectory caching with model fallback; Stated-limitations disclosure; Non-technical authoring layer on an agent core
- Tools: Amazon Nova Act

## [Every AI Company Is Accidentally Building a Bank — Dor Sasson, Stigg](../videos/cf2IhzqeQH4.md)
`cf2IhzqeQH4` · AI Engineer · 2026-10-07 · q3 · intro · talk · also: governance-compliance, infra-cost-scaling

Stigg's CEO argues AI usage pricing needs bank-style runtime controls: synchronous entitlement checks before consumption, hold-and-settle for concurrency, and layered credit pools, not invoice-time reconciliation.

- Techniques: Synchronous pre-consumption check with async settlement; Hold, settle, and idempotency for concurrent draws; Ordered draw-down across credit sources; Deterministic decision waterfall; Metering ledger inside the customer VPC
- Tools: Stigg, OpenClaw, Claude Max, GitHub Copilot

## [Build the Right Thing: Product Engineering (Part 2) — Kent C. Dodds, EpicProduct.engineer](../videos/s0hFne6EeOI.md)
`s0hFne6EeOI` · AI Engineer · 2026-10-06 · q3 · practitioner · talk · also: —

Kent C. Dodds on product engineering: turn feature requests into jobs-to-be-done, classify them with the Kano model, and build the right thing before building it well.

- Techniques: Problem tree via repeated 'why'; Job statement template; Little-hire tracking; Mom Test validation; Kano classification for prioritisation; Feedback aggregation channel

## [How AI Agents Pay: Checkout in ChatGPT and Google AI Mode — Sam Parsons, PayPal](../videos/c5U-XbbEN-g.md)
`c5U-XbbEN-g` · AI Engineer · 2026-10-06 · q2 · intro · talk · also: mcp-and-tools, security-guardrails

PayPal Enterprise Payments (Braintree) walks through three ways merchants accept payments from AI agents: ChatGPT instant checkout, Google AI Mode via UCP, and MCP apps with external checkout.

- Techniques: Host-side tokenization with scoped payment tokens; MCP app widget that triggers host-native checkout; Discovery file plus session endpoints for headless checkout; External checkout handoff linked to a session
- Tools: MCP Apps, Agentic Commerce Protocol (ACP), Universal Commerce Protocol (UCP), Google Pay, Braintree / PayPal Enterprise Payments, ChatGPT, Claude connectors, Goose

## [Build the Right Thing: Product Engineering (Part 1) — Kent C. Dodds, EpicProduct.engineer](../videos/_fHTqOs5wQA.md)
`_fHTqOs5wQA` · AI Engineer · 2026-10-06 · q3 · intro · workshop · also: coding-agents

Kent C. Dodds argues that once agents level implementation, the durable engineering skill is deciding what to build, using Mom Test-style validation and smallest-slice thinking. Part 1 of a workshop, mostly framing.

- Techniques: Mom Test customer interviews; Ask what the problem costs; Smallest slice / minimal demonstrable solution; Throwaway prototype, then rebuild with agents; Check the neighbors before building; Build the agent playground
- Tools: Slido, Cursor, OpenCode, Claude (captioned as 'cloud')

## [Keyword Search Is Dying. Is Your Catalog Ready for AI Agents? — PayPal](../videos/YXb2Wx1r_Pk.md)
`YXb2Wx1r_Pk` · AI Engineer · 2026-10-05 · q2 · intro · talk · also: rag-retrieval, data-engineering

PayPal's agentic-commerce director argues merchant catalogs were built for human search, not agents, and shows that enrichment helps semantic recommendations while over-enrichment and boilerplate hurt.

- Techniques: Catalog enrichment for semantic retrieval; Head-to-head baseline test of enriched vs unenriched records; Hybrid keyword plus semantic retrieval; Strip boilerplate from agent-facing text

## [We're the bottleneck, but we don't have to be — Ido Salomon, AgentCraft](../videos/YIVkERhy8xo.md)
`YIVkERhy8xo` · AI Engineer · 2026-10-04 · q2 · intro · talk · also: multi-agent, coding-agents, software-factory

Ido Salomon (AgentCraft) argues that humans are the bottleneck in agent work and demos a game-style orchestrator with attention-jumping, a map view, review kits, shared rooms, and a simpler "loopers" mode for non-engineers.

- Techniques: Attention queue with jump-to-next; Spatial projection of agent activity; Review kit for parallel agent output; Orchestrator with isolated local containers and background loops; Shared room with cross-agent notice board; Progressive disclosure for low-floor use
- Tools: AgentCraft, Claude Code, Codex, OpenCode, OpenClaw, Git, Telegram, MCP Apps (MCPUI)

## [Get Out of the Model's Way — Kevin Hou, Google Antigravity](../videos/buHC7bQE1X4.md)
`buHC7bQE1X4` · AI Engineer · 2026-10-04 · q3 · practitioner · talk · also: multi-agent, coding-agents, agent-architecture

Google's Antigravity lead on building agent products that get out of the model's way: subagent teams, sidecar triggers and generative UI, with cost and token stats from a kernel-building run.

- Techniques: Dynamic subagent teams under a lead agent; One subagent per hypothesis fan-out for eval deltas; Skills file plus natural language for internal workflow automation; Sidecar trigger process; Generative UI in the conversation instead of fixed screens; Separate the orchestration surface from the editor; Primitive audit against the next model
- Tools: Google Antigravity, Antigravity CLI, Antigravity 2.0 agent manager, Gemini 3.5 Flash, MCP, Cloud sandboxes and remote execution (unnamed), Windsurf (reference only)

## [Dashboards Are Dead — Sarah Simionescu, Composio](../videos/YiFqcu9YA38.md)
`YiFqcu9YA38` · AI Engineer · 2026-10-04 · q2 · intro · talk · also: mcp-and-tools, context-engineering

Composio's Sarah Simionescu argues agents should replace dashboards, and that MCP servers need task-scoped tool discovery to work. Vendor pitch with a mock-up demo.

- Techniques: Task-first tool discovery; Parallel fetch after planning; Keep bulky results out of context; Schema-first exploration before querying; Bug-report prompt to an agent with connected tools
- Tools: Composio (MCP, CLI, native tools, Composio Search, Composio Remote Workbench), Claude, MCP (Model Context Protocol, announced by Anthropic Nov 2024), Datadog, Sentry, Slack, GitHub, Jira (JQL), VS Code, PostHog, Metabase, SQL

## [The Chief AI Officer: Scientist, Architect, Coach — Rania Khalaf, WSO2](../videos/9cJrbj23fOA.md)
`9cJrbj23fOA` · AI Engineer · 2026-10-04 · q3 · intro · talk · also: enterprise-adoption, governance-compliance

WSO2's Chief AI Officer Rania Khalaf on running the role as scientist, architect and coach, with adoption-based metrics instead of token counts.

- Techniques: Three-dimension role mapping; LLM-assisted role analysis; Adoption depth ladder; Agent-ready product checklist; Dogfooding with a closed feedback loop
- Tools: Claude, Gemini, BERT, MCP, Databricks

## [The 5 Levels of Self-Driving Production — Eric Schwartz, Traversal](../videos/y-OVWZD4j6U.md)
`y-OVWZD4j6U` · AI Engineer · 2026-10-04 · q2 · intro · talk · also: observability, enterprise-adoption

Traversal's PM argues AI coding agents shift engineering time from building to troubleshooting, and proposes a five-level "self-driving production" autonomy scale plus five criteria for judging AI SRE tools.

- Techniques: Five-level autonomy scale for incident response; Five-question checklist for evaluating AI SRE tools; Causal root cause framing for multi-hop incidents; Agent-first incident intake; Alert triage pass before on-call
- Tools: Traversal (AI SRE product; production world model and causal search engine), Claude Code (auto-caption "Cloud Code"), Codex, Cursor, Datadog, Elastic, Splunk, ServiceNow, Slack

## [Apple Won the AI Race](../videos/Ba3xunEk8Y8.md)
`Ba3xunEk8Y8` · Better Stack · 2026-10-02 · q2 · intro · news · also: models-research, local-ai

Better Stack argues Apple can win the AI race through distribution, device data and an on-device model that is good enough, not frontier model quality. Mostly speculative commentary with few verifiable facts.

- Techniques: Distill a frontier model into smaller deployable models; Run large MoE models locally by streaming experts from SSD and caching hot experts in RAM
- Tools: Apple Intelligence, Siri, Apple Foundation Models (AFM3 variants, names partly garbled in captions: AFM3 Core, AFM3 Core Advanced, AFM3 Cloud Pro, and one cloud variant), Private Cloud Compute, Google Gemini, Anthropic Fable (described as the public version of Mythos), Mythos (described as too dangerous for public release), OpenAI Sol Ultra (as captioned), Grok 4.6 (xAI), DeepSeek, Kimi, MiniMax

## [Grok Bot Use Cases That Are Actually Insane](../videos/90pwPVrydHg.md)
`90pwPVrydHg` · AI LABS · 2026-10-02 · q2 · intro · review · also: multi-agent, voice-multimodal, testing-verification

Walkthrough of GrokBot's eight use cases: a hosted, always-on bot group sharing one logged-in browser, used for app testing, support triage, monitoring and AI-search checks. Light on setup detail; sponsor and paid-tier plugs.

- Techniques: Role-bot test fan-out with a lead bot; Backend-verified UI failure triage; Agent-triggered test round; Support email to draft reply and PR; Fresh-account onboarding audit; Unbranded AI-search visibility check; Scheduled morning monitoring routine; Coordinator bot over functional bots
- Tools: GrokBot, Grok, SuperGrok, Cursor, Hermes, Claude Code, Codex, Supabase, Stripe, Gmail, Sentry, GitHub

## [Why LLM Recommenders Will Be AI's Biggest Consumer App — Devansh Tandon, Meta](../videos/lIgdnF0s0kQ.md)
`lIgdnF0s0kQ` · AI Engineer · 2026-09-27 · q3 · practitioner · talk · also: models-research, infra-cost-scaling

Devansh Tandon (Meta) argues recommenders scale like LLMs, lays out four recommender S-curves, gives a three-step recipe for LLM recommenders built on semantic IDs, and claims feeds are far more token-efficient than chat apps.

- Techniques: Semantic ID tokenization of content; Bilingual LLM pre-training on semantic IDs; Post-training LLM rerankers with chain of thought; Shared base model with thin per-surface fine-tuning; Agentic recommendation loop
- Tools: Semantic IDs, HSTU, Tiger, Plum, Gemini, Claude Code, Codex

## [The Loop Is the Product — Roland Gavrilescu, Introspection](../videos/7taOQBfjDyE.md)
`7taOQBfjDyE` · AI Engineer · 2026-09-27 · q2 · intro · talk · also: skills-self-improvement, evals, agent-architecture

Introspection's Roland Gavrilescu argues self-improving agent loops should distill a team's taste into versioned recipes of evals, judges and skills, validated in production and measured as value per watt.

- Techniques: Trace pattern clustering to find signals; Agent-drafted judges with human calibration; Recipe diffs as reviewable candidates; Production A/B or bandit promotion; Per-model harness profiles
- Tools: Py.Recipes, Harbor, OpenClaw (originally CloudBot), Claude Code, Codex, Cursor, Cognition

## [Teaching LLMs to Speak Spotify — Yves Raimond & Jacqueline Wood, Spotify](../videos/2LRIAfng7eA.md)
`2LRIAfng7eA` · AI Engineer · 2026-09-27 · q4 · practitioner · talk · also: training-finetuning-rl, evals

Spotify's engineers explain turning recommendations into a steerable LLM: semantic-ID tokens, a four-stage NEO training recipe, and LLM judges grounded in behavioral data.

- Techniques: Semantic-ID tokenization and vocabulary extension; Frozen-backbone domain grounding; Staged training: grounding, then multi-task instruction tuning, then optional RL; Beam search over constrained decoding for ID generation; Grounding LLM judges with user profiles and behavioral signals; LLM judges for Cranfield-style relevance pools
- Tools: Qwen, LLaMA, LoRA, NEO (Spotify's training paradigm, linked paper), Discover Weekly, Spotify DJ

## [I Gave an AI a Body — Cyrus Clarke, MIT Media Lab](../videos/jgWY66RaSrQ.md)
`jgWY66RaSrQ` · AI Engineer · 2026-09-27 · q3 · intro · talk · also: voice-multimodal, agent-architecture

MIT Media Lab researcher Cyrus Clarke gives an OpenClaw agent a 900-pin shape display and has it build its own gesture vocabulary, arguing for non-humanoid, aesthetics-led physical AI.

- Techniques: Closed-loop gesture generation with gates and scoring; Pre-authored action repertoire to cut latency; Neutral embodiment with no affordances; Open-ended exploration prompt with machine access
- Tools: OpenClaw, openFrameworks, Numalab (speaker's own system), Shape display (physical pixel grid, 900 pins)

## [The Design-Code Roundtrip That Isn't — Jonathan Gordon, ReWeaver AI](../videos/NW-jwOVr32w.md)
`NW-jwOVr32w` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: vibe-coding-app-building, governance-compliance

Jonathan Gordon (ReWeaver AI) argues a lossless design-code round trip is not yet solved and proposes deterministic guardrails plus provenance to control drift around LLM-generated UI code.

- Techniques: Design-system extraction from code into the design canvas; Joint drift report across code and design; Deterministic guardrails around LLM generation; Fidelity metric per iteration (production drift ratio); Undo and review loop for AI code edits
- Tools: Figma, Sketch, Cursor, Claude Code, ReWeaver

## [Reverse-Engineering the AI Buyer — Aliisa Rosenthal, Acrew Capital](../videos/wdTRsfw0KG0.md)
`wdTRsfw0KG0` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: enterprise-adoption, governance-compliance

A former OpenAI go-to-market leader on building automated sales machinery before hiring humans, launching self-serve first, avoiding pilots, and pricing usage instead of seats.

- Techniques: Automation-first go-to-market build-out; Self-serve first, then sales-assisted; Pilot alternatives that keep control of the deal; Trust portal and automated security review; Usage-based pricing with spend controls; Design partner on non-production internal product
- Tools: Clay, Nooks, Microsoft Copilot, ChatGPT Enterprise

## [Rebuilding the web for agents — Liad Yosef, MCP Apps](../videos/waI44NP1abk.md)
`waI44NP1abk` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: mcp-and-tools

Liad Yosef (MCP Apps co-maintainer) argues the web is shifting to assistant-driven, headless-plus-UI interaction, and that agent-readiness should be measured from agents' real behaviour, not from best-practice files.

- Techniques: Expose UI as MCP Apps for the last mile; WebMCP: publish page tools instead of screenshots; Measure agent paths, not best-practice checklists; Per-domain AI Catalog.json plus a queryable directory; Design an API-first surface, then add UI for the last mile
- Tools: MCP Apps, WebMCP, llms.txt, AI Catalog.json, Agentic Resource Discovery standard, auth.md, pricing.md, x402, Aura Journey, Aura readiness benchmark, Claude Code, ChatGPT

## [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../videos/G7cgLjZtmMU.md)
`G7cgLjZtmMU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: mcp-and-tools, evals, security-guardrails

Best Buy's Ahnaf Priyo maps the agentic commerce protocol stack (MCP, A2A, ACP, UCP, AP2), argues for pushed product feeds and checkout APIs over browser agents, and makes the case for behavior and protocol evals with a live cat-bakery demo.

- Techniques: Push product feed to platforms; Checkout as an explicit state machine; Scoped, single-use, revocable payment mandate; Layered evals for conversational commerce agents; Timeline view of agent calls; Agent skills for domain roles
- Tools: MCP, A2A, ACP, UCP, AP2, Cerebras, ChatGPT, Gemini, Chrome DevTools

## [AI is the World’s largest Relationship Therapist — Clay Cockrell & Tony Fabrikant, CoupleWork AI](../videos/yoONZwV2smc.md)
`yoONZwV2smc` · AI Engineer · 2026-09-18 · q2 · practitioner · talk · also: evals, security-guardrails

Clay Cockrell and Tony Fabrikant of CoupleWork AI argue that relationship AI often acts as a sycophantic validation machine, and describe their clinician-led design of Maxine: risk screening, protocol escalation, privacy, and clinician-written evals.

- Techniques: Clinician-first TDD evals; Background risk screen with protocol handoff; Reflect patterns instead of validating; Dogfood the agent for tone drift; Treat sensitive chat data as privileged
- Tools: Gottman Method, Emotionally focused therapy (EFT), Maxine (CoupleWork AI coach)

## [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../videos/B0fjR3yaZFU.md)
`B0fjR3yaZFU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, evals, agent-architecture

Long Lake co-founder on why AI adoption in real services businesses lags: climb an autonomy ladder, turn real work traces into evals, and co-design with users on-site.

- Techniques: Autonomy ladder rollout; Sandboxed async coding agent with PR output; Traces to ground-truth evals; Diff-based implicit feedback; Post-training on enterprise data; Layered customization; Co-design embedded in existing tools
- Tools: Claude Code, Codex, Claude Cowork, MCP

## [One Designer + AI. Hundreds of Deliverables. — Vincent Wendy, AI Engineer](../videos/O1FN4awNEtM.md)
`O1FN4awNEtM` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: context-engineering, testing-verification

A solo designer at AI Engineer uses agents (Devin, GPT, Figma) to produce hundreds of conference deliverables by fixing design tokens first, automating data-driven outputs, and checking results with an agent.

- Techniques: Tokens-first design system for agents; Annotated spec sheet as handoff; Single data source to many assets; Agent as checklist QA on visual output; Vision-based photo matching; Raster first, then vectorize
- Tools: Devin, GPT, Figma, MCP, Slack, PNG export, Figma spec-sheet plugin

## [Act, Confirm, or Stop? Smarter behavior for AI assistants, wearables & robots — Amit Desai, Roku](../videos/Zd5b40Jbp_k.md)
`Zd5b40Jbp_k` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: voice-multimodal, evals

Voice assistant satisfaction can rise without better accuracy: gate act/confirm/stop on calibrated confidence and pick thresholds by minimizing a user-cost function ("ouch").

- Techniques: Outcome user-cost minimization for act/confirm/stop; Two-threshold three-band policy with grid search; Sensitivity check on unit costs
- Tools: Interactive threshold-sweep graph built with a coding assistant (no specific library named)

## [Voice Agents Can Just Do Things — Charlie Guo, OpenAI](../videos/OpY6MmZFeHo.md)
`OpY6MmZFeHo` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: voice-multimodal, mcp-and-tools

Charlie Guo (OpenAI) argues voice agents need not always talk back and lays out three voice modes (speech-to-speech, speech-to-action, event-to-speech), with GPT Realtime 2 as the example stack.

- Techniques: Three-mode voice design; Expose app verbs as tools; Escalating attention ladder; Preamble prompting; Native audio streaming; Role-first voice design checklist
- Tools: GPT Realtime 2, OpenAI Realtime API, Codex, ChatGPT advanced voice mode, CarPlay, Google Maps, Spotify

## ["My name is... my name is...": A Linguistic Map for Voice Agents — Midam Kim, ServiceNow](../videos/IDNfAZVKvPE.md)
`IDNfAZVKvPE` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: voice-multimodal, evals

Midam Kim (ServiceNow) uses a linguistics framework to explain why voice agents fail and proposes diagnosing them by listen/speak channels, timing, and the user's mental model.

- Techniques: Linguistic diagnostic grid for voice agents; Interactive clarification on recognition errors; Locale-aware pre-processing for TTS and vocabulary; Turn-taking and barge-in control; Dynamic per-call context retention; EvaBench for diagnosing voice agents
- Tools: EvaBench

## [MCP Apps: Give the Model Data, Give the User a UI — Dustin Mihalik, Indeed](../videos/lbaXnx0KLA8.md)
`lbaXnx0KLA8` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: mcp-and-tools, context-engineering

Dustin Mihalik (Indeed) shares lessons from building MCP Apps for Claude and ChatGPT: model-visible data parity, separate data from rendering, and feeding UI interactions back to the model.

- Techniques: Model-visible data parity; Description steering of UI vs text output; Explore/render split; Interaction feedback via update model context; Render tools that take model-generated rationale; Small composable tool set
- Tools: MCP Apps, Apps SDK (OpenAI), update-model-context method, Claude, ChatGPT, CareerScout (Indeed internal agent)

## [The Spatial Harness: Bringing Agents to the Canvas — Max Drake, tldraw](../videos/XWcXwnysmpY.md)
`XWcXwnysmpY` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: multi-agent, agent-architecture, coding-agents

tldraw's Max Drake on giving LLM agents a spatial canvas: teaching them to read screenshots plus shape data, running multi-agent fairies, and driving live apps and the desktop through code.

- Techniques: Screenshot plus structured data as canvas context; Agentic canvas harness with self-set goals; Visual agent identity and on-canvas task state; Orchestrator agent posting tasks to a shared board; Local editor server for code-mode agents; Dependency graph of agent tasks
- Tools: tldraw SDK, tldraw desktop app, Claude Code, Notion, Gmail, Conductor, OpenAI Symphony

## [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../videos/6pbQgnJ9Voc.md)
`6pbQgnJ9Voc` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, mcp-and-tools, security-guardrails

Exa's co-founder argues go-to-market is an AI engineering data problem and shows the internal agents, ICP dashboard, and JeffBot clone that run his GTM team.

- Techniques: Decision-log to eval calibration for a personal proxy agent; Caller-scoped agent permissions; Semantic web search as a segmentation pipeline; API/MCP-first, then customize the SaaS; Signal-triggered alerts on customer events
- Tools: Exa, Opus 4.5, Slack, Salesforce MCP

## [Teaching agents to pay — Anna Spysz, Stripe](../videos/A-zeQiYkmXk.md)
`A-zeQiYkmXk` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: security-guardrails, mcp-and-tools, governance-compliance

Stripe engineer builds an agentic-commerce agent to buy headphones, covering the Universal Commerce Protocol, merchant manifests, shared payment tokens, persona effects on behavior, and a guardrail checklist.

- Techniques: Merchant capabilities manifest at /.well-known; Structured catalog and policy JSON; Attribute-match decision logging; Persona-driven behavior control and A/B testing of system prompts; Scoped payment token instead of raw credentials; Provider-enforced transaction limits; Agent commerce guardrail checklist
- Tools: Universal Commerce Protocol (UCP), Stripe payments, Google Pay, Apple Pay, shared payment token

## [Everyone Gets A Software Company — Benjamin Guo, Zo Computer](../videos/Qr15lGAGKpo.md)
`Qr15lGAGKpo` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: agent-architecture, sandboxing-execution

Zo Computer co-founder Ben Guo pitches a personal cloud server with built-in AI as a way out of SaaS silos and vendor-owned cloud agents. Mostly a product pitch, with a few ownership arguments worth noting.

- Techniques: Single personal server as the agent home; Scheduled agent automations; Agent as a gatekeeper for inbound bookings; Chat-driven site editing and hosting
- Tools: Zo Computer, Claude Code, Codex, Gemini, Claude Tag, OpenClaw, Hermes, Calendly, Squarespace

## [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](../videos/V_5bn4q-vAI.md)
`V_5bn4q-vAI` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: context-engineering, mcp-and-tools, coding-agents

Christopher Burns (Inth) on making LLMs recommend and correctly use his open-source cookie-banner library by shipping agent-friendly docs: hand-written llms.txt, markdown twins, web MCP, and grep-able docs inside node_modules.

- Techniques: Hand-curated llms.txt index; Markdown twin per page with discovery header; Three ways to reach markdown; Bundle docs in the package with an agents.md pointer; Web MCP for docs; Agent-readiness checks as a loop
- Tools: LeadType, llms.txt, llms-full.txt, AGENTS.md, Next.js, Aura AI, Cloudflare agent-readiness checker, MCP

## [The Search Engine for the Agentic Web — Will Bryk, Exa](../videos/59AA5kIoqjA.md)
`59AA5kIoqjA` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: rag-retrieval, infra-cost-scaling

Exa's CEO pitches Exa as a search engine built for AI agents rather than humans, covering its history, API features (fast endpoint, token extraction, structured output) and a data marketplace.

- Techniques: Hybrid embedding plus keyword retrieval; Token-budget extraction before the LLM; Schema-based structured search output; Per-tenant search configuration; Latency tiers by consumer type
- Tools: Exa search API, Exa Connect, Cursor, HubSpot, Similarweb, GPT-3, ChatGPT

## [Speech-to-Speech Model Research at Google DeepMind — Valeria Wu Fon & Tom Ouyang, Google DeepMind](../videos/18Um2VjMM_g.md)
`18Um2VjMM_g` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: voice-multimodal, models-research

Google DeepMind's Gemini speech-to-speech team explains why one natively multimodal, promptable model beats cascaded ASR+LLM+TTS for voice agents, with live translation, Search Live and Live API demos.

- Techniques: Native multimodal pretraining for audio tasks; Streaming translation as a prompt; Proactive audio gating; Managing the latency vs intelligence knob; One promptable model for many modes
- Tools: Gemini Live, Search Live, Gemini Live API, Google Meet speech translation

## [The End of the Static Screen: Architecting Intent-Driven UX — Gus Iwanaga, commercetools](../videos/QrMcNe2jjt8.md)
`QrMcNe2jjt8` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: mcp-and-tools, agent-architecture

Gus Iwanaga (commercetools) on intent-driven generative UI: an orchestrator picks data and components, and the LLM emits a validated declarative UI spec, not free-form UI. Main lessons are on placement, the component catalog as contract, and changing team roles.

- Techniques: Declarative UI spec validated against a component catalog; Three-tier control spectrum for generated UI; Intent-to-UI orchestration pipeline; Layout hierarchy with templates, built bottom-up; Synthetic query-to-component data for curation
- Tools: MCP, Zod, React, A2UI, JSON Render (Vercel), OpenUI, ChatGPT, Claude

## [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI — Ayush Bhardwaj, Allos AI](../videos/Yphdry8ttAQ.md)
`Yphdry8ttAQ` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: evals, data-engineering, enterprise-adoption

A seven-step recipe for building vertical AI (finance, pharma) where domain experts in a learning loop, not LLM-as-judge, drive quality and proprietary data is the moat.

- Techniques: Narrow task decomposition; LLM workflow for unstructured-to-structured data curation; Observability traces as the first improvement loop; Domain expert as user in a learning loop; Post-training ladder; AI-in-the-loop reduction of expert time

## [Agentic Sites: Building Hyper Personalized Websites — Carlos Sanchez, Adobe](../videos/jebp4V0vh30.md)
`jebp4V0vh30` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: evals, inference-serving, rag-retrieval

Adobe's Carlos Sanchez demos "agentic sites" that personalize page blocks in real time from browsing intent, grounded on the existing site, with provider choice driven by latency and accuracy evals.

- Techniques: Multi-provider eval matrix for accuracy and latency; Grounded block-level generation; Signal bucketing into personas or intents; Pre-generate and prefetch; Fast inference provider for the hot path
- Tools: Adobe Experience Manager, Edge Delivery Services, Cerebras, Gemma 4, Promptfoo, AWS Bedrock, Cloudflare, Google Cloud

## [Generative UI... in Python? — Jeremiah Lowin, Prefect](../videos/Krzs8GeiWTc.md)
`Krzs8GeiWTc` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: mcp-and-tools, vibe-coding-app-building

Jeremiah Lowin (Prefect) on Prefab, a Python DSL for composing MCP App UIs; the talk argues scoping UIs to pre-built components makes Python-only front ends viable and that streaming compact Python beats streaming JSON.

- Techniques: Return a UI component from a tool; Reactive bindings for client-side interactivity; App class with app.ui and app.tools; Agent-bypass upload via MCP app; Stream generative UI as code
- Tools: Prefab, FastMCP, MCP Apps, React, shadcn/ui, Goose

## [Building an Agentic Video Editor for Mass Consumer — Ekaterina Deyneka, Reelful](../videos/pPj_tjlvYjA.md)
`pPj_tjlvYjA` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: sandboxing-execution, testing-verification, voice-multimodal

Reelful's founder shows how an agentic video editor turns real footage into a clip: media understanding, a user-approved plan, a sandboxed agent with skills, Remotion rendering, and a verification loop.

- Techniques: Sandbox per approved job; Plan approval gate; Skills as encoded craft; Code-defined render target; Verification-then-reiterate loop; Directional templates plus manual editor fallback
- Tools: Remotion, React

## [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../videos/Lrw0jqBNaw0.md)
`Lrw0jqBNaw0` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: evals, mcp-and-tools, observability

Sourcegraph's agent advocate argues DevRel must now serve AI agents as users and recommenders, and shows how to measure agent friction and recommendation rates.

- Techniques: Agent friction logging from traces; With-and-without-tool agent benchmark; Intent-split GEO prompt experiments; Agent experience report; Machine-readable authoritative content
- Tools: Sourcegraph code navigation MCP tool, CodeScaleBench (speaker's benchmark), llm.txt, MCP registries, Discord

## [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../videos/mJqwmmOx4WA.md)
`mJqwmmOx4WA` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: governance-compliance, vibe-coding-app-building, coding-agents

Andrew Garvin (Metronome, now part of Stripe) live-demos using Stripe Projects and a Metronome billing agent to build a usage-based billing setup from one natural-language prompt, arguing for sandboxed agent-built billing and for usage or credit pricing when agents are the users.

- Techniques: Portable skills files as agent context for a complex API; Verbose, machine-readable errors for agent self-correction; Sandbox-first agent-built billing with synthetic usage; Natural-language provisioning through a CLI orchestrator; Classify agent roles before designing pricing
- Tools: Stripe Projects, Stripe CLI, Metronome, Claude (selected as the coding agent in the demo), Vercel, Postgres, skills files

## [The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu](../videos/VBCDhRrvlYo.md)
`VBCDhRrvlYo` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: vibe-coding-app-building, agent-architecture, context-engineering

Arturo Nunez (ex-Unity, MongoDB) pitches Nereu, a tag-driven, describe-it-to-build game engine where an AI assistant (Bibi) edits scenes via an Asset Tag System, so creators never touch engine vocabulary or code.

- Techniques: Entity tags as an intent layer over ECS; LLM-as-editor with a tool-only interface; Level-of-detail context assembly; Vision-model asset captioning; Domain expert in the loop while building with a coding agent
- Tools: Claude Code, Unity, Unreal, vision model

## [While my guitar gently speaks — Todd Fisher, Philo Ventures](../videos/E_Txocq-Lrw.md)
`E_Txocq-Lrw` · AI Engineer · 2026-09-18 · q2 · intro · demo · also: voice-multimodal, vibe-coding-app-building

A guitar that speaks and sings: pitch detection, word slicing, vocoder synthesis and a local Whisper-to-LLM loop. Mainly a call to build passion projects with AI.

- Techniques: Energy-gap plus sonority-peak word segmentation; YIN pitch detection to synthesized tone to vocoder; Pre-bake heavy DSP, then map to controls; Local voice loop: STT, then local LLM, then TTS; Plugin packaging inside a DAW
- Tools: JUCE, Logic Pro, Piper TTS, Whisper, YIN pitch algorithm, WORLD vocoder/pitch-shift, VocalSet, Apple built-in TTS

## [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../videos/DrTdD-ttjCY.md)
`DrTdD-ttjCY` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: enterprise-adoption, observability, evals

Snowflake's sales-team GTM agent (6,000 users): launch with quality over coverage, stage the rollout, manage activation, and use question logs as the feedback loop.

- Techniques: Question bank as the first eval set; Narrow-scope, high-accuracy launch; Pilot, beta, GA with metric gates; LLM classification of usage logs; Closed loop from logs to content; Agent instructions under version control with tests; Build on a managed agent platform with inherited access control
- Tools: Snowflake Cowork (formerly Snowflake Intelligence), Cortex Analyst, Cortex Search, Snowflake semantic views, MCP connections, Confluence, Jira, Slack, Gmail, Salesforce, Google Docs

## [The Next Medium: Why Real-Time Interactive Video Changes Everything — Ahmed Ahres, Reactor](../videos/5dCAmSDOAjI.md)
`5dCAmSDOAjI` · AI Engineer · 2026-09-18 · q2 · intro · talk · also: voice-multimodal, inference-serving, infra-cost-scaling

Ahmed Ahres (Reactor) argues real-time interactive video and world models will change how content is made and consumed, then describes the infra gaps: streaming, session memory, and sub-100 ms global latency. Mostly a company pitch.

- Techniques: Stream frames over a live session instead of returning a file; Regional GPU routing for a latency budget; Session memory to keep generated worlds consistent; Multi-GPU serving plus quantization for cost and speed; Human-in-the-loop evaluation for real-time output
- Tools: Reactor API (real-time world model platform, roughly 10 lines to integrate per the speaker), Helios (ByteDance, interactive video model), LingBot (Alibaba, world model), LongLive 2 (NVIDIA, multi-shot film model), StreamDiffusion (NVIDIA, video-to-video; transcript reads 'SoundCloud Streaming', likely a caption error), Veo, Sora, Genie 3 (mentioned as comparisons)

## [Multimodal Collaborative Agents for Next-Gen Commerce — Nidhi Kaushik Vyas, Google DeepMind](../videos/AhQpRalYlyg.md)
`AhQpRalYlyg` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: evals, context-engineering

Google DeepMind product lead on shopping agents for fuzzy intent: build a working state, ask the highest-value clarifying question, elicit preferences visually, adapt the answer format, and grade every step with autoraters.

- Techniques: Working state with confidence and live refresh; Counterfactual sensitivity test for constraint extraction; Information-gain question selection; Elicitation-channel choice by preference type; Per-step autoraters with user simulator; Response format chosen by query intent
- Tools: MCP (expected interface between agents and merchants), UCP (merchant common-language protocol, named in the talk without detail)

## [The Missing Layer: Design Taste in AI Agents — Hassan El Mghari, Together AI](../videos/7GMKdpLsxwU.md)
`7GMKdpLsxwU` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: vibe-coding-app-building, context-engineering, coding-agents

Hassan El Mghari (Together AI) on getting AI-built UIs out of "AI slop": codify the tells as anti-patterns, feed in references, iterate with a cheaper model.

- Techniques: Slop-gate anti-pattern list in a design skill; Theme library as inspiration; Screenshot inspiration vault; Two-tier model routing for UI work; agents.md as a taste log; Batched feature prompting
- Tools: Codex, Claude Code, Cursor, Hallmark, agents.md, GLM 5.2, Opus 4.8, Composer 2.5, Together AI

## [Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia](../videos/McknwOzbmyg.md)
`McknwOzbmyg` · AI Engineer · 2026-09-18 · q4 · practitioner · talk · also: evals, testing-verification, voice-multimodal

Jared Joselowitz (Ufonia) on shipping a clinical voice agent to patients without A/B tests or rollback, using simulated patients, a calibrated LLM judge, and prompt optimization gated by hazard-linked evidence.

- Techniques: Hazard-first safety case; Scenario-conditioned simulated user; Calibrated LLM judge; Reflective prompt optimization (GEPA) with a cost-weighted metric; Synthetic edge-case generation; Staged gated rollout with evidence-based autonomy; Pin prompt versions and keep full traces
- Tools: Matrix (internal simulation framework), PatBot (internal LLM patient), BevJudge (internal LLM judge), GEPA (genetic-Pareto prompt optimizer), DSPy (mentioned as the origin of GEPA), Gemini 2.5 Pro (judge model at the time of the paper)

## [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../videos/bMjlRrWjdT0.md)
`bMjlRrWjdT0` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: evals, enterprise-adoption, observability

DoorDash GenAI platform team on building a cross-functional AI evals platform: UI-first, then API-first, then workflow-first, so non-engineers can run annotation and judge calibration themselves.

- Techniques: Continuous eval loop; API-first eval platform with vibe-coded UIs; Self-serve judge calibration with prompt optimization; Platform-level model choice for judges
- Tools: Claude Code, Codex, DSPy-style prompt optimizer (transcribed as JEPA), MCP, LLM gateway, agent gateway

## [Mousepower: agents that can’t be measured, can’t be managed. — Maximillian Piras, Yutori](../videos/8KkibGU_DDY.md)
`8KkibGU_DDY` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: governance-compliance, evals, token-cost-efficiency

Maximillian Piras (Yutori) argues agents have a measurement problem: token spend must trace to verifiable outcomes, and tasks should be triaged by step and acceptance-criteria uncertainty before building an agent.

- Techniques: Two-axis task triage; Verifier agent alongside worker agent; Background parallel agents for peripheral work; Outcome-tied token accounting
- Tools: Claude

## [The Signal Layer: What to Build When Anything Can Be Built — Lena Hall, Akamai](../videos/1KOdiGgMtpY.md)
`1KOdiGgMtpY` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: enterprise-adoption

Lena Hall argues that when AI makes building cheap, value moves to choosing what to build and keeping that choice intact through shipping and marketing, using a thin "signal layer."

- Techniques: Stranger readme read-back check; Promise welded to its limit; Human point of view, AI for the rest; Thin signal layer across handoffs; Hamming list of important problems

## [Training Taste — Thais Castello Branco, Taste Labs](../videos/sDMGWK4wZ_w.md)
`sDMGWK4wZ_w` · AI Engineer · 2026-09-18 · q3 · intro · talk · also: evals, vibe-coding-app-building, context-engineering

Thais Castello Branco (Taste Labs) on measuring and fighting "AI slop" in design: decompose subjective quality into checkable parts, build feature classifiers that flag slop, and turn a brand into structured context the agent both follows and is graded against.

- Techniques: Decompose subjective quality into probes; Split objective checks from aesthetic judgment; Rule-aware intentional divergence; Brand spec as both generation context and rubric; Retrieve pre-built brand systems
- Tools: Claude Design, Wayback Machine-style web crawl

## [Design at the Speed of Adjectives — Paul Bakaus, Renaissance Geek, Inc.](../videos/v42opQpCy60.md)
`v42opQpCy60` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: vibe-coding-app-building, coding-agents, context-engineering

Paul Bakaus on steering coding agents toward good design with a skill (Impeccable) that maps vague design adjectives like "bolder" to project-specific meanings, keeping humans in the loop instead of one-shotting.

- Techniques: Project-defined verb and adjective commands; Self-check against a stated failure test; Pre-brief questions before generation; Workflow-stage command mapping; Community-tested experimental commands
- Tools: Impeccable, Claude Code, GitHub Copilot, Cursor, Codex, Figma, Webflow, Claude Design, Radiant Shaders

## [Which AI startups actually land enterprise contracts? — Brian Lewis, Millennium](../videos/7A65O-0lvKE.md)
`7A65O-0lvKE` · AI Engineer · 2026-09-18 · q3 · practitioner · talk · also: enterprise-adoption, security-guardrails, governance-compliance

A buyer at a hedge fund explains why most AI startup pilots fail: value, security, reliability and legal gaps, not model quality. He argues most AI-native work is unglamorous data, architecture and change management.

- Techniques: Enterprise-readiness intake checklist for vendors; Verify retention claims in a pilot, not on paper; Gate features by group and by release; Track documentation and terms as versioned artifacts; Set buyer-written success criteria and a 90-day plan that deploys into the buyer's own cloud; Build-versus-buy check on vendor pitches; Breach-response question as a red flag test

## [We Need to Talk About Gemini...](../videos/tSjG4Nl6VNA.md)
`tSjG4Nl6VNA` · Kai Explains · 2026-09-02 · q3 · intro · news · also: models-research

Commentary on how Google fell from the top of the model rankings in 2026: a delayed Gemini 3.5 Pro, senior researcher departures, and a pace problem that distribution cannot fix.

- Techniques: Read a lab's roadmap by what actually ships; Use an aggregate index as a rough prior, then check the rank over time
- Tools: Gemini 3.1 Pro, Gemini 3.5 Pro, Gemini 3.5 Flash, Gemini 3.6 Flash, Gemini 3.5 Flashlight, Flash Cyber, Gemini 4, Artificial Analysis Intelligence Index, Google TPU, Claude Mythos 5, Claude Fable 5, Claude Sonnet 5

## [How America Turned Against the AI Industry?](../videos/xu-i-Zeu46s.md)
`xu-i-Zeu46s` · Kai Explains · 2026-09-02 · q2 · intro · other · also: governance-compliance, infra-cost-scaling

Kai Explains essay on why US public opinion turned against AI and data centers: broken promises, local costs, and water as the proxy grievance. Opinion piece, not a technical talk.

- Techniques: Tangible-unit framing for infrastructure costs; Treat stated concerns as evidence before explaining; Cost-locality check on advocacy
- Tools: ChatGPT

## [Insane Claude Design Skills You Need To Actually Build Beautiful Sites](../videos/Ysr7oNDajJI.md)
`Ysr7oNDajJI` · AI LABS · 2026-09-02 · q2 · intro · review · also: skills-self-improvement, claude-code

AI LABS walks through design-focused agent skill packs (Emil Kowalski, Conard Lee, Elia Design, Meng To, Jakub Krehel, Tastemaker, perception laws) for Claude Design and says they steer models away from generic layouts. Mostly an overview; little measured evidence.

- Techniques: Install and invoke a design skill in Claude Design; Layer skills by stage; Score-and-iterate loop; Regression-aware review via GitHub; Script-based reference extraction; Landing-page as one-action structure; Install only the skills that fit your workflow
- Tools: Claude Design, Claude Code, Codex, GitHub, Emil Kowalski design skills (design-engineering skill, Animate, Apple Design, animation vocabulary), Conard Lee garden skills (web design engineer skill), Elia Design landing-page skill, Meng To skills (video-to-prompt, awards-quality sites), Jakub Krehel skills (review, better layout), Tastemaker, screen critique skill, perception laws skill

## [These New Claude Skills Are Actually Insane](../videos/jyLKRN36-Dc.md)
`jyLKRN36-Dc` · AI LABS · 2026-09-02 · q3 · practitioner · review · also: skills-self-improvement, claude-code, context-engineering

AI LABS walks through six new agent skills: a self-improving skill-learning log, a four-rule coding baseline, a logged-in website CLI (OpenCLI), a variant-picker for UI, and two product-business skill sets for onboarding, paywalls, churn and validation.

- Techniques: Per-project learning log for skills; Parent-folder CLAUDE.md for base coding rules; Onboarding and paywall pattern; Cancellation save flow; Logged-in site commands via OpenCLI; Variant exploration for one UI section; Demand validation before building
- Tools: Claude Code, CLAUDE.md, Agent skills, log.md (task-observer output file), OpenCLI, Chrome extension (OpenCLI), Variate skill, Hallmark design skill (mentioned, not shown), Next.js, Supabase, Corey's 48-skill marketing collection, SVG (brand logo format)

## [This Is How Forward Deployed Engineering Is Actually Done](../videos/AD-EmZ3v6-g.md)
`AD-EmZ3v6-g` · AI LABS · 2026-09-02 · q2 · intro · tutorial · also: enterprise-adoption, evals, mcp-and-tools

How to do forward deployed engineering: audit a business process before building, sort each step into software, model or human, then eval against real cases. Useful method, but includes a sponsored segment and unsourced stats.

- Techniques: Shadow-and-document the process; Three-filter triage per step; Connect to existing systems instead of migrating; Keep process steps visible with checkpoints; Labelled-case eval loop; Value-and-error-cost accounting; Process audit as the first deliverable
- Tools: Claude Code (used for the internal chatbot case study), MCP (Model Context Protocol), Notion (named as the example system for MCP connection), Slack, Cursor (as a company example), OpenAI (as a company example), Anthropic (as a company example), Dex (job-matching sponsor; named in a sponsored segment)

## [From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com](../videos/Btk8wDUVs74.md)
`Btk8wDUVs74` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: memory, context-engineering, data-engineering

monday.com's Omri Bruchim and Tomer Ast argue agents fail because they lack understanding, not data, and describe a two-speed "world model" of the user (slow learned profile plus fast live signals) built ahead of time.

- Techniques: Two-speed user model (slow profile + fast signals); Precompute meaning ahead of time, recompute a thin slice at serve time; Source isolation with fallback to last verified context; Urgency gating for proactive notifications
- Tools: monday.com Sidekick, Monday Vibe, Monday Agent, Monday Workflows, Slack, Claude, Gemini, GPT

## [Gadgets: Personal app vibe coding that is actually safe — Kenton Varda, Cloudflare](../videos/RmS5s6Wbin4.md)
`RmS5s6Wbin4` · AI Engineer · 2026-08-18 · q3 · practitioner · demo · also: vibe-coding-app-building, sandboxing-execution, security-guardrails

Kenton Varda (Cloudflare) argues personal AI codegen needs new infrastructure, and demos "Gadgets": per-user apps with platform-enforced sharing and sandboxed generated code, run on open-source workerd.

- Techniques: Platform-enforced sharing via single-purpose instances; Sandboxed generated UI with postMessage-only RPC; Give the agent the app source and a brief, let it add primitives; Export code-only templates (blueprints); Run the production runtime locally
- Tools: Cloudflare Workers, Durable Objects, Dynamic Workers, workerd, Claude, Cap'n Web RPC

## [How Forward Deployed Engineering is done at Cognition — Jia Wu](../videos/RVxym6mmIns.md)
`RVxym6mmIns` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: enterprise-adoption, software-factory

Jia Wu (Cognition) on forward-deployed engineering: embed in enterprise customers, map Devin to real backlog problems, and measure outcomes from agent sessions. Mostly a company pitch, with some case-study numbers.

- Techniques: Session-based value measurement; Event-triggered agent automation; Map backlog to capabilities; Before/after delivery metrics; Autonomous legacy migration
- Tools: Devin, Devin Cloud, Windsurf, Claude Code, Cursor

## [Build for the Memo, Not the Demo — Shawn Chan, China Resources Holdings](../videos/tJFjeMBKbIY.md)
`tJFjeMBKbIY` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: governance-compliance, rag-retrieval

A finance investor argues AI products should be built as auditable memos, not impressive demos. He lists six ways trust breaks and five plumbing fixes: provenance, number agreement, surfaced contradictions, fact/guess labels and human approval.

- Techniques: Click-through provenance with source trust levels; Fact vs guess labelling; Automatic cross-document number reconciliation; Surface contradictions instead of resolving them silently; Locked human approval gate with audit log; Accountability-first architecture

## [The New Primitives: Building AI Native Software — Kwindla Kramer, Daily](../videos/LZuWZRze3MU.md)
`LZuWZRze3MU` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: multi-agent, voice-multimodal, agent-architecture

Kwindla Kramer (Daily, PipeCat) argues agents are a stage on the way to AI-native software, using 80 years of computing history and demos of a real-time Knowledge Navigator and a multiplayer LLM game.

- Techniques: Asynchronous non-blocking context compression for sub-agents; Long-running sub-agents that share context; Progressive skills loading; Dynamic UI generation driven by the agent; Real-time voice plus LLM orchestration with a pipeline framework
- Tools: PipeCat, Gradient Bang, Daily, Tavus

## [HTML Is All Agents Need — James Russo, HeyGen](../videos/Cz4v1WHVyZc.md)
`Cz4v1WHVyZc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: voice-multimodal, context-engineering, skills-self-improvement

HeyGen's Hyperframes turns agent-written HTML into deterministic MP4 video by freezing the browser clock and seeking frame by frame; the thinnest HTML wrapper beat heavier DSLs.

- Techniques: Thin HTML as the agent output format; Deterministic frame-by-frame browser rendering; Single render path for preview and output; Taste-focused skills instead of syntax skills; Small model as a format canary; Storyboard, iterate, then human last-mile edit; Website-to-asset single-shot skill
- Tools: Hyperframes, HTML/CSS/JS, Three.js, WebGL, WebGPU, Lottie, Rive, Remotion (transcribed as "Promotion"), After Effects, Premiere Pro, Gemini 3 Flash, Claude Code

## [MCP Apps: Extending the Frontier — Ido Salomon & Liad Yosef](../videos/-jY2T2PiJBE.md)
`-jY2T2PiJBE` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: mcp-and-tools, agent-architecture

Ido Salomon and Liad Yosef, the creators of MCPUI and maintainers of the MCP Apps spec, explain how MCP Apps lets servers ship interactive UI into chat hosts and how control of the user journey shifts to the host.

- Techniques: Serve UI as an MCP resource linked to a tool call; Host-mediated event flow from app to model; Three control levels for app-driven steps; Interop: wrap one generative UI payload for several hosts
- Tools: MCP (Model Context Protocol), MCP Apps (official MCP extension), MCPUI, MCP Apps SDK / spec repo (spoken as 'Xtaps' in captions; the official model context protocol repository), ChatGPT Apps / Apps SDK, Claude (including its generative UI feature), VS Code, Slack, Cursor, GitHub Copilot, Goose, Block agent e-commerce

## [AI tools for Forward Deployed Engineering — Vasuman Moza, Varick Agents](../videos/l0FLhNqBOic.md)
`l0FLhNqBOic` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: enterprise-adoption, training-finetuning-rl, rag-retrieval

Varick Agents explain why process understanding, not model execution, is now the bottleneck, and describe the forward-deployed engineering agent they built for it.

- Techniques: Failure-path process interviews; Per-step autonomy split; Dependency graph as shared state; Post-training an open model for analysis style; RL environment with domain traversal tools; Assistant embedded in the authoring tool
- Tools: Varick OS (in-house platform), Claude, Codex, Granola, Kimi (open-source base model, named as K2.6), NetSuite, Microsoft Dynamics, SAP, Salesforce

## [How Forward Deployed Engineering is done at Kepler — Vinoo Ganesh](../videos/1OMHGsUZiqA.md)
`1OMHGsUZiqA` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: enterprise-adoption, data-engineering

Vinoo Ganesh on running forward-deployed engineering as a product strategy: go on site, solve small problems fast, define shared terms, and avoid shipping hacks that become permanent.

- Techniques: Three-question discovery before building; Ship-it threshold for small problems; On-site workflow observation; Pain-signal scan; Canonical glossary and ontology; Production-readiness gate for quick fixes
- Tools: Palantir Foundry, Cassandra, Parquet, S3, Groovy, Elasticsearch, Snowflake, Databricks, Tableau, SAP, Slack

## [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../videos/jHMiYtjoJfA.md)
`jHMiYtjoJfA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, observability

Ben Hylak (Raindrop) argues teams should "raise the floor" by finding production agent failures, tracking when they started and how many users they hit, and using code-based classifiers over traces instead of clustering or big eval sets.

- Techniques: Evals as local code tests; Per-issue onset and affected-user tracking; Code-based trace classifiers; Deterministic signal first, agent investigates second; Scale-dependent experimentation
- Tools: Raindrop, Workshop (open-source tracing tool), vitest (vitest evals), howtoeval.com, Sentry (mentioned as a model for issue detection)

## [The Dirty Secret of Forward Deployed Engineering — Natalie Meurer, Sierra](../videos/Byv311hdoHE.md)
`Byv311hdoHE` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: enterprise-adoption

Sierra's head of agent engineering traces forward-deployed engineering from Palantir's 2008-2020 eras to today, argues the title is vague, and says customer accountability and outcome pricing make most engineering roles trend toward it.

- Techniques: Write-back dashboards; Ontology-first data modeling; Customer-accountable build loop; Outcome-attribution test for pricing; FDE vintage interview question
- Tools: Palantir Foundry, Palantir AIP, Palantir Slate, AWS EC2, Airbus Skywise, Retool (comparison only)

## [Lessons from Studying Every Memory System — Shlok Khemani, Independent](../videos/5ZGyKWjQDr0.md)
`5ZGyKWjQDr0` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: memory, context-engineering, agent-architecture

Shlok Khemani traces how ChatGPT and Claude memory evolved from 2024 to 2026, and argues memory is a product and compute problem, not a RAG problem, with context as the real cap.

- Techniques: Running profile with background re-synthesis (dreaming); Search tools over past conversations instead of stored facts; User-visible and user-editable profile with re-synthesis on edit; Dense keyword-clue memory entries; Timestamped memory entries
- Tools: ChatGPT, Claude, Gemini, Poke, Claude Code, OpenClaw, Hermes

## [The UX of AI: Making AI-Powered Apps Your Users Don't Hate - Kathryn Grayson Nanz, Progress Software](../videos/L3RuP_q8Bwc.md)
`L3RuP_q8Bwc` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: security-guardrails

Kathryn Grayson Nanz (Progress Software) on designing AI features users trust. Organizes UX problems into five areas (trust, clarity, control, transparency, meaningful benefit) and gives concrete UI patterns for each.

- Techniques: Source citations with graded surfaces; Plan approval before agent execution; AI content labeling; Streaming and visible reasoning; Change highlighting; Prominent kill switch; Task-scaled version history; Granular revocable permissions; Pre-approval cost and time estimates; Guided starts and next-step actions
- Tools: Claude, ChatGPT, Microsoft Copilot, Microsoft Teams

## [How Forward Deployed Engineering is done at Decagon — Sunny Rekhi](../videos/7wu2hsRfvV0.md)
`7wu2hsRfvV0` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: enterprise-adoption

Decagon's CTO of Forward Deployed Engineering explains how FDEs configure enterprise AI support agents, funnel customer asks into the product, and productize repeated custom work as the company grew from 50 to 500 people.

- Techniques: Define success in writing at scoping; Productize on repetition (the 25th-integration rule); Field-to-product feedback loop; Same-vertical deal staffing; ROI-ranked first automation; Natural-language configuration as a platform rule; Two-lane split for scaling agent work
- Tools: Decagon, Codex, Claude Code

## [How Forward Deployed Engineering is done at Factory — Eno Reyes](../videos/wpOA-UXynoM.md)
`wpOA-UXynoM` · AI Engineer · 2026-08-18 · q4 · practitioner · talk · also: software-factory, enterprise-adoption, testing-verification

Eno Reyes (Factory CTO) on forward-deployed engineering as the way to build software factories. The bottleneck is agent readiness, meaning deterministic validators in the codebase, not model capability.

- Techniques: Audit validation loops before deploying agents; Bounded long-running harness with an explicit definition of done; Map the signal-to-deploy stages per org; Land-and-expand with a reference implementation; Split automation into one-click fixes and workflow changes; Model-independent harness with owned traces and self-hosted deployment
- Tools: Factory Droid, Missions, LegalDroid, linters, type checkers, security scanners, end-to-end test suites

## [Local Agentic Theory For Mobile Games — Shafik Quoraishee & Joanne Song, The New York Times](../videos/418t26CVz-w.md)
`418t26CVz-w` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: local-ai, agent-architecture, inference-serving

NYT engineers on running small agents on-device inside mobile games, under per-frame time, memory and battery budgets, with live accessibility tuning through graded dials instead of fixed menus.

- Techniques: Per-frame perceive-predict-decide-act agent loop; Constraint graph over space, time and energy; Constraint satisfaction with backtracking; Graded accessibility dials driven by live signals; Live focus-path monitoring and layout auditing
- Tools: Efficient Zero V2 (sample-efficient RL, mentioned as state of the art up to 2024), WCAG 2.2 and WCAG 3.0 draft, Gaze estimation CNN, Google SIMA (transcript reads 'SEMA'; generalist agent framework mentioned briefly)

## [Persona Engineering: A Field Guide to AI Synthetic Personas — Ishan Anand, InsightSciences.ai](../videos/YnNF55QV0zs.md)
`YnNF55QV0zs` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: evals, context-engineering, models-research

Ishan Anand (InsightSciences) on synthetic personas as bounded forecasts: where LLM personas fail (confounders, order bias, attitudes vs behavior), and how to measure them against human distributions and noise floors.

- Techniques: Validate personas against held-out human ground truth; Ground the persona in the full world of the study; Durability tests for option order and wording; Attitude-to-behavior triangulation; Free-text answers mapped to scale via semantic similarity; Fine-tune on survey distributions conditioned on demographics; Noise floor via split-half simulation

## [Forward Deployed Engineering 101 — Kevin Bai, Anthropic, ex Palantir & Rippling Founding FDE](../videos/KwhgfwOSToQ.md)
`KwhgfwOSToQ` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: enterprise-adoption

Kevin Bai (Anthropic, ex-Palantir and Rippling) explains the forward deployed engineer role: when to use it, why it needs a shared platform, and how to scope bespoke versus generalizable work.

- Techniques: FDE fit test before adoption; Bespoke vs generalizable split; Two engineers per customer project; Granularity of primitives matched to user base
- Tools: Palantir Foundry

## [Every Harness Will Become A Claw — Sam Bhagwat, Mastra](../videos/8qWIPUia2O8.md)
`8qWIPUia2O8` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: agent-architecture, sandboxing-execution, skills-self-improvement

Sam Bhagwat (Mastra) argues agent harnesses will keep expanding into always-on "claws" with durability, initiative and learning, then shake out to a few winners. Mostly conceptual, with little hard data.

- Techniques: Durable turn streaming with resume; Queue, steer and interrupt on running threads; Session-scoped tool approval; Heartbeat wake-ups; Trace-driven continual learning; Cloud sandbox per parallel subagent
- Tools: Mastra, Claude Code, Codex, OpenClaw, Hermes Agent, Slack, Telegram, WhatsApp, GitHub

## [Content Is Code - Matt Palmer, Conductor](../videos/yv6xovSsB1U.md)
`yv6xovSsB1U` · AI Engineer · 2026-08-18 · q3 · intro · talk · also: context-engineering, coding-agents

Matt Palmer (Conductor) argues code is becoming the medium for technical content, so docs, changelogs and product videos should be generated from a structured source of truth.

- Techniques: Generate product tour videos with React and Remotion; Derive changelogs and product updates from the diff; Keep design tokens separate from app code; Write internal docs and skills for agents
- Tools: React, TypeScript, Remotion, CSS, HTML, Claude

## [Jev CEO: I made ChatGPT, now I'm building what's next](../videos/cJ0EOzey--o.md)
`cJ0EOzey--o` · AI Engineer · 2026-08-18 · q2 · intro · talk · also: training-finetuning-rl, models-research

Former OpenAI post-training lead Diego Almeida argues RLHF models are built for assistance, not automation, and pitches a new post-training objective (calibrated decision making) at his stealth startup TypeSafe.

- Techniques: Assistance vs automation diagnostic; Cost-shifting to the user as a deployment pattern; Name the optimization target before choosing a post-training method
- Tools: Claude Code

## [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing - Bala Ramdoss, Amazon Lens](../videos/maTp79FD9gI.md)
`maTp79FD9gI` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: mcp-and-tools, agent-architecture

Bala Ramdoss (Amazon Lens) on why LLM agent output needs a typed rendering layer between model and screen: a versioned UI contract, streamed typed chunks, and a BFF that hydrates actions, so mobile clients stay dumb and safe.

- Techniques: Versioned rendering contract; Typed streaming UI blocks; BFF as renderer and hydrator; Design loading around streaming
- Tools: A2UI, CopilotKit, MCP apps

## [The Guy Who Coined "Event Gateways" Explains Why Webhooks Are Dying | Better Stack Podcast Ep. 17](../videos/ElaEGr2t9XQ.md)
`ElaEGr2t9XQ` · Better Stack · 2026-08-02 · q3 · practitioner · interview · also: infra-cost-scaling, agent-architecture, dev-tools

Hookdeck's founder explains why he built an event gateway and the open-source Outpost to replace fragile webhook handling with queuing, replay, push-based rate control and per-vendor latency monitoring. Substantive but vendor-led.

- Techniques: Push-based webhook intake in front of your endpoint; Respond fast, queue the work; Per-vendor delivery latency baseline and alerting; Per-tenant queues with a shared push consumer; Event destinations instead of HTTP webhook transport; Open-source-first with a managed twin; Verify agent-written contributions against real APIs
- Tools: Hookdeck (Event Gateway), Outpost (Apache 2.0, open source), Hookdeck Radar, Kafka, RabbitMQ, Amazon SQS, Google Cloud Pub/Sub, AWS EventBridge, Azure Event Grid, Kong event gateway, Cloudflare Queues, BullMQ

## [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals - Jacob E. Thomas, Results Gen](../videos/IJXjTLPzvAU.md)
`IJXjTLPzvAU` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: evals, context-engineering

Jacob Thomas argues persona/role-play agents are judged by fluency metrics that cannot catch anachronistic "composite" historical figures, and proposes a pre-registered, expert-scored, context-window-based eval (Lincoln case study).

- Techniques: Pre-registered fidelity eval for personas; Anachronism-first rubric with voice excluded; Encounter-as-configuration with receipts; Context window grounding over persona fine-tuning; Expert-authored gold set as a CI gate
- Tools: Claude Opus 4.7, Companion (open-source persona prompt framework built by the speaker), Character AI, Hello History, KOSIR, PsyMem, In-Character benchmark

## [Running a Chess YouTube Channel entirely by AI — Stephan Steinfurt, TNG](../videos/BqZrTdgBaPw.md)
`BqZrTdgBaPw` · AI Engineer · 2026-07-18 · q3 · practitioner · demo · also: mcp-and-tools, agent-architecture

Stephan Steinfurt (TNG) shows a nightly, fully automated chess-explainer pipeline: a Gemini 3.1 Pro agent with chess tools narrates analysed human games as YouTube videos.

- Techniques: Engine plus LLM split with tools; Let the reasoning model choose tools rather than pre-computing; Deliberately conflicting tool outputs; Nightly batch with a structured intermediate format; Monitor odd outputs and treat them as signals
- Tools: Gemini 3.1 Pro, Grok 4, ElevenLabs v3, Maia (captioned as Maya), chess engine (unnamed), web search

## [OpenClaw in Your Hand: Building a Physical AI Terminal - Lech Kalinowski, Callstack](../videos/akk6KRlcwW4.md)
`akk6KRlcwW4` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: local-ai, inference-serving

Callstack engineer Lech Kalinowski builds a handheld text-terminal for OpenClaw and local LLMs on an ESP32, with a thin-client design backed by a 120B model on a DGX Spark. Mostly a hardware showcase with useful field notes.

- Techniques: Thin-client MCU with a heavy backend; Pre-allocated one-bit page buffers; Dual-display split by job; OpenAI-style proxy in front of open models; Graceful degradation across hardware parts
- Tools: OpenClaw, ESP32, NVIDIA DGX Spark, NVIDIA serving stack (auto-caption: 'Tensor Earth'), OLED display, e-paper display

## [remobi.app: Don't change your terminal workflow for mobile](../videos/5192csoTkVo.md)
`5192csoTkVo` · AI Engineer · 2026-07-18 · q2 · intro · demo · also: coding-agents, dev-tools

Connor Adams demos Remobi, an open-source progressive web app that gives phone access to tmux sessions running Claude Code and other coding agents, reached over a private network such as Tailscale.

- Techniques: tmux as the agent session host; Private-network remote access to a dev box; Gesture-mapped terminal UI; Diff review in a side window; Skill-driven environment setup
- Tools: Remobi, tmux, Tailscale, Cloudflare Tunnels, ngrok, Claude Code, Happy, lazygit, critique, agent-browser, npm, Conductor

## [500 people vibe-coded for 30 days. I was one of them. - Sanja Grbic, Automattic](../videos/UcYoMg-8-L8.md)
`UcYoMg-8-L8` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: enterprise-adoption, vibe-coding-app-building, coding-agents

Automattic's 30-day "Radical Speed Month" experiment, in which about 500 people in paired teams shipped roughly 794 projects, and how the speaker moved from designer to design engineer by prototyping in code before Figma.

- Techniques: Time-boxed paired ship sprint; Prototype-in-code before design tool; Shared file-based exploration log; Aggregating scattered sources into a status tracker; Engineer as enabler in mixed-skill pairs
- Tools: Claude Code, Figma, Storybook, GitHub, Nano Banana, Context MCP server, WordPress.com, Jetpack, WooCommerce

## [HTML is All You Need (for Agents to Make Graphics) - Amol Kapoor, Nori](../videos/JRTAtZ5iBkU.md)
`JRTAtZ5iBkU` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: vibe-coding-app-building, coding-agents

Amol Kapoor (Nori) argues agents fail at graphics because of the medium, not the model, and that HTML is a better authoring format than canvas tools or SVG for slides, docs and video.

- Techniques: HTML as the agent's authoring format for visual artifacts; Pick the format the model is strongest in, separate from the delivery format; Ground the artifact in source data, not in the layout; Avoid screenshot-and-replace loops and canvas-driving tools for agents
- Tools: HTML, CSS, SVG, Figma MCP, PowerPoint CLI, PDF export, Nori Sessions

## [Imagination Engineering: "Live in the future and then build what's missing."](../videos/Z2Erdirpudo.md)
`Z2Erdirpudo` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: vibe-coding-app-building, context-engineering

A YC design lead shows "software on demand" built from a week of public stream-of-consciousness Slack posts, plus a one-morning personal tool, and argues idea generation is the new bottleneck.

- Techniques: Public thought log as agent input; Distil a voice file from public writing; Self-updating design language; Agent-readable glossary markdown; Checklist-driven completeness; Timeboxing with a timer
- Tools: Claude / Claude Code, Opus 4.8, Fable 5, Conductor, Slack, Paper (design tool), ChatGPT (used to make the header image)

## [Chat and citations won't save your vertical AI - Atul Ramachandran, Filed Inc](../videos/RGiXcVxSD3s.md)
`RGiXcVxSD3s` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, observability, skills-self-improvement

Vertical AI talk by the Filed CTO arguing chat and citations are not enough; products should be built for delegating long-running work to agents, with skills, traces, pause-and-intervene and plan approval.

- Techniques: Delegation-first task selection; Implicit skill capture from usage; Per-value trace-back for trust; Pause-and-tag intervention; Plan approval gate for irreversible actions
- Tools: Wispr Flow

## [6 Things to Know about AIE World's Fair 2026](../videos/0S8xe9ftGTM.md)
`0S8xe9ftGTM` · AI Engineer · 2026-07-18 · q1 · intro · other · also: enterprise-adoption

Swix's promo-style update on AIE World's Fair 2026 (July, Moscone West): bigger show, new tracks, leadership and vertical focus, and expo/networking tips. No technical content.

## [Your AI Product Will Fail Unless You Can Explain It - Veronica Hylak, Hey AI](../videos/d_Ftrl3vfV0.md)
`d_Ftrl3vfV0` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: enterprise-adoption

Short pitch-craft talk: explain an AI product by opening with the user's pain, tying it to a picturable story, and showing a concrete before/after.

- Techniques: Wound-first opening; Viral-story anchor; Picturable-phrase rule; Before/after transformation with numbers
- Tools: Devin (cited as an example of a picturable product name), McDonald's AI drive-through clips (cited as a viral story example)

## [Understanding is the new bottleneck — Geoffrey Litt, Notion](../videos/WkBPX-oDMnA.md)
`WkBPX-oDMnA` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: coding-agents, testing-verification, skills-self-improvement

Geoffrey Litt (Notion) argues humans must still understand agent-written code to stay creative participants, not only to verify it, and shows explainer docs, comprehension quizzes, agent-built micro-worlds and shared spaces for doing so.

- Techniques: Explainer doc per agent change (ExplainDiff-style skill); Comprehension quiz gate before sharing code; Intuition-first, literate ordering; Agent-built micro-world debugger; Step-through simulation for a migration; Shared threads and commentable docs with agents
- Tools: Claude Code, Claude, Cursor, Notion, Notion HTML blocks

## [Stop Writing Tone Instructions. Layer Them. - Isadora Martin-Dye, Isadora & Co](../videos/ij-AU9dpJjc.md)
`ij-AU9dpJjc` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: context-engineering, security-guardrails

Isadora Martin-Dye on layering a brand-voice AI agent into four stages: non-overridable identity rules, situational context, voice examples, and a deterministic post-generation veto, with fail-loud multi-tenant identity.

- Techniques: Four-layer ordered prompt stack via single assembly; Non-overridable identity layer; Soft context as tone guidance, never quoted; Deterministic post-generation veto with soft flags and hard rejects; Fail-loud multi-tenant identity; Shared veto gate by default; Trainable voice dial from staff edits
- Tools: Threadline (her own missing-persons tool, not a third-party product)

## [The Prompt Is Still a Punch Card - Ted Johnson, JoinIn AI](../videos/hVJOnuhFmTA.md)
`hVJOnuhFmTA` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: voice-multimodal, context-engineering

Ted Johnson (JoinIn AI) argues that prompting is a batch-style punch-card protocol that leaves users doing the work, and that AI interfaces should become turn-taking, conversation-like, and aware of who is being addressed.

- Techniques: Classify each utterance, then act only at a floor-free moment; Full-duplex turn-taking with yield and resume; Ask what burden the human still carries; Voice-driven record edits in a meeting
- Tools: NVIDIA Personaplex, OpenAI GPT Realtime 2

## [You Can't Prompt the Room: The Last Skill AI Won't Replace - Balázs Horváth, VisualLabs](../videos/6bmM45jkMDY.md)
`6bmM45jkMDY` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: context-engineering

Balázs Horváth (VisualLabs) argues that deciding what to build, through requirements elicitation, story mapping and value-first design, is now the bottleneck, not writing code.

- Techniques: Story map MVP slice; Persona/what/need/why stories with acceptance criteria as agent input; Four-question value check kept in the repo; Value-first design order (VAD); Usage-frequency success metric; Paired build comparison
- Tools: Story mapping, Business model canvas, Value canvas, User story templates with acceptance criteria, Markdown files in the repo as agent context

## [Forward Deployed Engineering at Cursor — Pauline Brunet](../videos/APqXGyCoGW4.md)
`APqXGyCoGW4` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: enterprise-adoption

Cursor's forward deployed engineering lead on where FDE fits, whom to hire, and how to scope short, ROI-driven customer projects without drifting into staff augmentation.

- Techniques: FDE placement matrix; Staff-augmentation check; Success defined before build; Directional six-week phased scope; Three-bucket ROI statement; Mission statement for the FDE team
- Tools: Cursor, Cursor SDK, Cursor cloud agents

## [AI System Design: From Idea to Production - Apoorva Joshi, MongoDB](../videos/T0HhO4YtTfE.md)
`T0HhO4YtTfE` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: agent-architecture, evals, context-engineering

A MongoDB developer advocate walks through a four-phase framework (product requirements, system design, evaluation and monitoring, cost/latency optimization) using a health insurance claims review system as the worked example.

- Techniques: Four-phase AI system design framework; Quantified solution-agnostic business problem; Three-axis AI role classification; Per-source retrieval strategy from update cadence and content type; Simplest-design-first, evaluate, then iterate; Guardrails as measurable rates; Production signals from human behaviour; Structured outputs as a reliability guard
- Tools: MongoDB, Voyage AI

## [MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc](../videos/sAOBXCDiDOs.md)
`sAOBXCDiDOs` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: mcp-and-tools, security-guardrails

Pietro Zullo (Manufact) explains MCP Apps: tools that return sandboxed UI widgets, the primitives behind them, and how the new client app stores distribute MCP servers.

- Techniques: Widget-returning tool; Split structured output (UI vs model); Set-state to sync UI to model; Stream tool input into the UI; Widget actions that call tools; Client-aware output; Pre-submission checks for stores
- Tools: MCP, MCP Apps, MCP-UI, MCP SDK, MCP Inspector, React, Remotion, Excalidraw, Granola MCP, Linear MCP, Postgres MCP, Claude Code

## [Everything we knew about software has changed — Theo Browne, @t3dotgg ​](../videos/xUnRQ9vLXxo.md)
`xUnRQ9vLXxo` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: coding-agents, agent-architecture, multi-agent

Theo Browne argues that models have moved coding into an orchestration era, so tools, product tiers and software defaults should be rethought, with a markdown file running on cron as his example.

- Techniques: Markdown as a recurring program; Prompt-driven sub-agent orchestration; Breadth-first product with extension points; Assumption audit
- Tools: Claude Code, Codex, Git, GitHub, S3, Cron, Vercel, Slack bot APIs, Reddit, OBS, tmux, GNU Screen

## [The Pipeline Is Dead - Iris ten Teije, Sky Valley Ambient Computing](../videos/bRnoEpoK5m4.md)
`bRnoEpoK5m4` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: agent-architecture, observability

Argues the one-version-for-everyone software pipeline ends as code gets cheap; proposes a canonical stem with per-user, bounded, reversible divergences and names the hard problems: provenance, testing, measurement, trust, coordination.

- Techniques: Stem plus bounded, reversible divergences; Developer-declared adaptation boundaries; Behavior-driven personalization with a spirit-of-the-software check; Traceable adaptation provenance; Goal-metric gating for changes; Recommend-first autonomy as a trust ladder; Coordination by intent and outcome

## [Voice In, Visuals Out: The Agony and the Ecstasy - Allen Pike, Forestwalk Labs](../videos/65X0pQ6Lmbg.md)
`65X0pQ6Lmbg` · AI Engineer · 2026-07-18 · q3 · practitioner · talk · also: voice-multimodal, infra-cost-scaling

Allen Pike (Forestwalk Labs) on why voice input with visual output beats voice-to-voice for AI now, and the latency tactics (fast small model, eager short inference turns, stable prompt prefixes) that make it feel responsive.

- Techniques: Two-tier model split (fast responder plus async thinker); Eager short-interval inference; Prefix-stable context layout for caching; Visual response envelope
- Tools: Linear, Slack, GPT-5 Mini, Haiku

## [Build AI Systems for Discernment, Not Approval - Angel Ortmann Lee, Duolingo](../videos/CDqzWpwkSls.md)
`CDqzWpwkSls` · AI Engineer · 2026-07-18 · q4 · practitioner · talk · also: evals, governance-compliance

Duolingo shows skilled reviewers accepted half of fake AI cheating flags; guidelines demanding independent evidence raised rejections 21%. Design human-in-the-loop interactions for discernment, not approval.

- Techniques: Calibration test with planted false signals; Reframe the AI output as a preliminary alert; Split compound questions into separate signals; Inline anchored feedback instead of a long essay; Surface assumptions and trade-offs for sign-off in agent plans; Capture the edit diff as the training signal; Log the questions users ask as a trust signal

## [Think You Can Build a Game with AI? Think Again! - Danielle An & David Hoe, Meta](../videos/grdoOC1BT1s.md)
`grdoOC1BT1s` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: vibe-coding-app-building, multi-agent

Two Meta game-creation leads argue that AI prompting makes basic games easy, so taste, art cohesion, playtesting and runtime-LLM NPCs decide quality, with undeterminism as the open engineering problem.

- Techniques: Key-art anchoring for image generation; Personality-driven LLM NPCs in a shared game loop; Parallel AI-assisted production with frequent playtests; Runtime LLM game master for per-player adjustment
- Tools: Gemini, Nano Banana, Meshy, Manus, Labubu (demo subject)

## ["The engineer of the future is the person who chooses what is worth doing." — Addy Osmani, Anthropic](../videos/n97BCfyFIvw.md)
`n97BCfyFIvw` · AI Engineer · 2026-07-18 · q3 · intro · talk · also: software-factory, governance-compliance, pr-code-review

Addy Osmani argues engineers are defined by owning the verdict on agent work: choosing what is worth doing, backing it with evidence, and accepting accountability. Keep humans at the highest-leverage checkpoint.

- Techniques: Inner loop / outer loop split; Evidence bundle as the review unit; Explain-it-or-don't-ship gate with named owners; Review as a control system for long runs; Move verification into the harness; Clean code for agents as well as humans
- Tools: Git

## [GTM Is You - Victoria Melnikova, Evil Martians](../videos/G6IlDzj8OjA.md)
`G6IlDzj8OjA` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: —

A go-to-market talk for developer-tool founders: distribution is now the bottleneck, so use a signal-vs-revenue check, a six-step GTM routine, and personal brand to get customers.

- Techniques: PMF Compass diagnostic; Six-step GTM hygiene checklist; Founder-as-channel distribution; Visible, low-cost proof of momentum

## [The Rise of Generative UI for Developers (CopilotKit)](../videos/kVL_7csy_ZM.md)
`kVL_7csy_ZM` · Better Stack · 2026-07-02 · q3 · intro · review · also: mcp-and-tools

Better Stack walkthrough of CopilotKit as a front-end stack for agent UIs: AG-UI event protocol, generative UI, shared state, and approval gates, with a candid trade-off section versus Vercel AI SDK and building in-house.

- Techniques: Generative UI: agent triggers real components; Bidirectional shared state between UI and agent (co-agents); Approval gate before state-changing tool calls; Scaffold the stack from the project's install command
- Tools: CopilotKit, AG-UI, Vercel AI SDK, LangGraph, CrewAI, Mastra, React, Next.js

## [Insane Claude Design Skills You Need To Build Beautiful Websites](../videos/Ot582-E61ac.md)
`Ot582-E61ac` · AI LABS · 2026-07-02 · q3 · intro · review · also: skills-self-improvement, coding-agents, mcp-and-tools

A walkthrough of Claude design skills (Anthropic frontend-design, ShadCN, UI UX Pro Max, GSAP, Material 3, SwiftUI, Expo) for building less generic websites and mobile apps, with a sponsor segment.

- Techniques: Commit to a design direction before generating; Separate functional and marketing design skills; Pair a rules skill with a component-registry MCP; Separate layout reasoning from component work for dashboards; Use a taste preset instead of a full design system; Prefer compositor-friendly animation properties
- Tools: Claude, Anthropic frontend-design skill, Opus 4.8, Fable 5, ShadCN, ShadCN MCP, UI UX Pro Max, GSAP, Higgsfield, C-Dance (as captioned; video model), Material 3, SwiftUI

## [Introducing WebMCP: Agents in the Browser — RL Nabors](../videos/LMbeDEQO6QM.md)
`LMbeDEQO6QM` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: mcp-and-tools, voice-multimodal

A practical tour of MCP over HTTP, MCP Apps for in-chat UI with CSP and sandbox gotchas, and WebMCP, which lets agents call tools exposed by a web page's own JavaScript.

- Techniques: Single server, multiple client surfaces; Remote connector onboarding over HTTP; App-only tool visibility for UI navigation; Bundle MCP App into one file with explicit CSP; WebMCP imperative registration with feature detection; Declarative WebMCP on existing forms
- Tools: MCP, MCP Apps, WebMCP, navigator.modelContext.registerTool, Vite single-file plugin, Web Speech API, MCP Inspector-style debugging extension

## [The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google](../videos/ghJmWQCIHRM.md)
`ghJmWQCIHRM` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: mcp-and-tools, voice-multimodal

Google Chrome DevRel on WebMCP, a proposed browser standard that lets a website expose its actions as structured tools for in-browser AI agents, with declarative and imperative APIs and an early-preview setup guide.

- Techniques: Declarative tool exposure from HTML forms; Imperative registerTool for multi-step UI; Mirror tool calls in the visible UI; Hybrid browse-then-delegate flow; Test tools with an inspector and evals CLI
- Tools: WebMCP, Chrome Canary, Model Context Tool Inspector (Chrome extension), Gemini, Chrome DevTools-style flag (WebMCP testing flag), WebMCP evals CLI

## [Beyond Components: Designing Generative UI for MCP Apps — Ruben Casas, Postman](../videos/hCMrEfPG2Yg.md)
`hCMrEfPG2Yg` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: mcp-and-tools, sandboxing-execution

Ruben Casas (Postman) maps generative UI from static components to declarative JSON to runtime-generated HTML/JS, argues MCP apps are the right sandboxed delivery layer, and says collaborative canvases are the next step.

- Techniques: Declarative generative UI with a component catalog; Static client-tool to component mapping; Runtime generated HTML/CSS/JS in a sandboxed MCP app; Use MCP apps as the default delivery for generated UI
- Tools: MCP apps, AG-UI, Goose (auto visualizer), json-render (Vercel), FastMCP, Excalidraw MCP app (transcribed as ScallyDraw), Claude Visualizer, GPT-5.2, Claude Opus 4.5, React

## [Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub](../videos/_xIwFcnHqp4.md)
`_xIwFcnHqp4` · AI Engineer · 2026-06-18 · q3 · practitioner · demo · also: mcp-and-tools, coding-agents

Marlene Mhangami and Liam Hampton (GitHub) show how MCP Apps let a tool return an interactive HTML UI rendered in a sandboxed iframe inside VS Code chat, with a live Go flame-graph demo.

- Techniques: MCP App tool-plus-resource pattern; Skill-driven MCP app scaffolding; Tool visibility scoping; Profiler-to-flame-graph bridge; Install MCP servers from curated lists only
- Tools: VS Code, GitHub Copilot, Copilot CLI, MCP, Go pprof, React, Excalidraw, Figma

## [How We Built Zeta2: Training an Edit Prediction Model in Production — Ben Kunkle, Zed](../videos/phchDt63qAA.md)
`phchDt63qAA` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: training-finetuning-rl, evals

Zed's Edit Predictions lead explains how Zeta 2, a small fine-tuned next-edit model, was distilled from frontier teachers using opt-in production snapshots, settled-state labels, and multi-sample filtering.

- Techniques: Teacher repair loop; Cache the teacher, vary the formatting; Settled-state labels via idle detection; Multi-sample consensus filter with a distance band; Multi-reference offline eval; Percentage-based live experiment rollout
- Tools: Zed, Zeta 2, Seed Coder, Levenshtein distance, JSONL

## [What the Best Agents Share — Mardu Swanepoel, Flinn AI](../videos/7CrPrHgoEYk.md)
`7CrPrHgoEYk` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: coding-agents, context-engineering

Mardu Swanepoel (Flinn AI) on four UX patterns shared by strong agents: focus modes, transparent execution, personalization, and reversibility, illustrated with Cursor, Claude Cowork, Harvey and Manus.

- Techniques: Mode-scoped agent configuration; Plan-only mode; Hypothesis-driven debug mode; Visible execution trace; Playbook and memory personalization; Layered undo; Native host integration for review
- Tools: Cursor, Claude Cowork, Claude skills and connectors, Manus, Harvey, Microsoft Word API

## [Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic](../videos/c-2eEv2ou7Y.md)
`c-2eEv2ou7Y` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: mcp-and-tools, security-guardrails

Frédéric Barthelet (Alpic) explains why ChatGPT and Claude render third-party MCP app UI in nested "double" iframes: CSP and origin isolation rule out simpler options, and the nesting is the workable compromise.

- Techniques: Double-iframe isolation for untrusted UI; Declare-then-enforce external domains; CSP inspection in dev tools
- Tools: MCP Apps extension, OpenAI Apps SDK, SkyBridge, HTML iframe (srcdoc, sandbox, allow-same-origin), Content Security Policy (frame-src, script-src, connect-src)

## [Does GenAI "belong" to data scientists? — Phil Hetzel, Braintrust](../videos/NKwIX3CiRgU.md)
`NKwIX3CiRgU` · AI Engineer · 2026-06-18 · q2 · intro · talk · also: enterprise-adoption, evals

Phil Hetzel (Braintrust) argues GenAI agent work should not belong only to data scientists or ML engineers. He says it needs a diverse product team, with domain experts shaping prompts and eval, and data scientists supplying rigorous eval discipline.

- Techniques: Judge calibration against human labels; Production traces feed the offline eval set; Domain-expert trace annotation; Prompt playground for non-engineers; Functional eval over technical metrics
- Tools: Braintrust

## [How to talk to statues — Joe Reeve, ElevenLabs](../videos/u-rJwPPU3QA.md)
`u-rJwPPU3QA` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: voice-multimodal, vibe-coding-app-building

ElevenLabs growth lead on the viral "Statue" app, built in two hours, and on voice-agent UX. Main points: glue code and storytelling matter most, and voice agents need visual co-presence and interruptible, editable transcripts.

- Techniques: Research-to-persona-to-agent chain; Thin glue layer on managed APIs; Playback-position transcript truncation for barge-in; Visual side panel for voice conversations; Hook-first short video with late music
- Tools: ElevenLabs Agents, ElevenLabs Voice Design API, ElevenLabs music generation, OpenAI deep research, Cursor, Supabase, Facebook Instant Games API (deprecated), CapCut, Claude app voice UI, OpenClaw

## [Most Enterprise Agentic Projects Are Doomed, Here's Why — Jess Grogan-Avignon & Jack Wang, Accenture](../videos/AGkzpxMdPn8.md)
`AGkzpxMdPn8` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: enterprise-adoption, governance-compliance

Accenture talk on why enterprise agentic projects stall: human-speed governance, business cases, and trust. Argues for hypothesis-driven delivery, portfolio funding, progressive autonomy, and feedback loops as the moat.

- Techniques: Exposure ladder for agent rollout; Approval-as-code; Hypothesis-driven agent delivery; Portfolio funding for AI bets; Kill switches and hard limits on autonomous actions; Instrument every feature as a feedback source

## [Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google](../videos/_B4Pv9ttFgY.md)
`_B4Pv9ttFgY` · AI Engineer · 2026-06-18 · q4 · practitioner · talk · also: mcp-and-tools, security-guardrails

Four engineering lessons from the Chrome DevTools MCP team on designing agent-facing interfaces: token cost, error recovery, tool discoverability, and trust boundaries.

- Techniques: Semantic summaries instead of raw tool output; Tokens per successful outcome; Tool categorization and slim mode; CLI with piping for local post-processing; Self-healing error messages; Proactive detours; Tool descriptions as UI for the agent; Trust tiers with deliberate consent friction
- Tools: Chrome DevTools MCP server, Gemini CLI, Claude Code, Codex, OpenClaw

## [Gemini Nano on device — Florina Muntenescu & Oli Gaymond, Google DeepMind](../videos/owH1f0N-keY.md)
`owH1f0N-keY` · AI Engineer · 2026-06-18 · q3 · practitioner · talk · also: inference-serving, local-ai

Google DeepMind's Android team on using Gemini Nano on-device via ML Kit GenAI and Firebase hybrid fallback, with Q&A on battery, shared-model scheduling and device reach.

- Techniques: Runtime hybrid routing with cloud fallback; Use the ML Kit GenAI Prompt API for on-device structured tasks; Offload non-urgent batch work to background, charging-time windows; Prompt-stuffed retrieval as a stopgap RAG; Device testing and profiling for custom models
- Tools: Gemini Nano, AICore, ML Kit GenAI APIs, Prompt API, Firebase AI Logic, LiteRT-LM, AI Edge Gallery, Gemma 4

## [Rewiring the State — Eoin Mulgrew, No. 10 (Downing Street)](../videos/ObNKGf9YR0g.md)
`ObNKGf9YR0g` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: enterprise-adoption, governance-compliance, evals

Eoin Mulgrew of No. 10's data science team describes an outsider "insurgency" unit with forward-deployed engineers that ships small government AI tools in weeks; mostly a recruitment pitch.

- Techniques: Insurgency unit with a mandate; Forward-deployed engineers embedded in workflows; Internal tool instead of outsourced one-off analysis; Policy simulation sandbox; Pre-deployment sycophancy red-teaming and user coaching; Benchmark-based guardrails for classroom AI
- Tools: Gemini, Inspect (AI Safety Institute evaluation tool), Xtract (planning-application digitisation)

## [Why Claude Recommends Resend & Building in Public | Better Stack Podcast Ep. 15](../videos/8ahyAKK2l9Y.md)
`8ahyAKK2l9Y` · Better Stack · 2026-06-02 · q2 · intro · interview · also: security-guardrails, dev-tools

Better Stack podcast with Resend's DX engineer on getting LLMs to recommend a vendor, scoping per-team AI agents with narrow API keys, and email deliverability basics. Mostly biographical, with a few practitioner nuggets.

- Techniques: One scoped identity per agent or team; Scheduled weekly digest agent; Weekly competitor watch, on demand; Research agent before writing a changelog or post; Scaffold landing pages from existing repo patterns; LLM-discoverability checklist for a docs or marketing site; Deliverability setup for a transactional email service; Obsidian vault synced to GitHub as a personal task store
- Tools: Resend, React Email, Claude, Hermes (OpenClaw-based agent), OpenClaw, Cursor, GitHub CLI, 1Password, Slack, Obsidian, Linear, Raycast

## [Open Design: Why 40k Developers Abandoned Claude Design](../videos/B3coWv2ZV68.md)
`B3coWv2ZV68` · Better Stack · 2026-06-02 · q3 · intro · review · also: vibe-coding-app-building, coding-agents

Walkthrough of OpenDesign, an open-source, local alternative to Anthropic's Claude Design that generates HTML prototypes and slides on top of whichever coding agent is installed; the speaker argues design systems plus per-output skills drive quality more than the model.

- Techniques: Run OpenDesign from source; Harness and model selection per project; Seed a design from a live URL; Pick a design system before prompting; Finalize, export and hand off; Iterate with follow-up prompts
- Tools: OpenDesign (open-source Claude Design alternative, Nexa team), Claude Design (Anthropic, proprietary, cloud-only, $20/month per the speaker), Claude Code, Claude Opus 4.7 (speaker's claim that it is strong at front-end design), Codex, OpenCode, GLM 5.1 (used as the generation model), GPT-Image2 (OpenAI image model, default image provider via OpenAI key), ElevenLabs (TTS and sound effects, optional), agent-browser (browser tool the agent used), Chrome (opened via curl by the agent), Docker (optional install path)

## [This Is Insane... This Just Ended The Google Stitch VS Claude Design Debate](../videos/PJ9CmTODmVo.md)
`PJ9CmTODmVo` · AI LABS · 2026-06-02 · q2 · intro · review · also: mcp-and-tools, coding-agents, context-engineering

Hands-on head-to-head of Claude Design and Google Stitch across features, limits, design quality, animation, iteration and handoff; each tool wins different categories.

- Techniques: Batch design comments before sending; Import a design system from a URL; Portable design.md design system; Coding agent drives the design tool through MCP; Generate the design system before the screens
- Tools: Claude Design, Claude Opus 4.7, Google Stitch, Gemini 3, Nano Banana, Claude Code, Figma, Google AI Studio, Firebase, GitHub, design.md

## [The End of Apps — Kitze, Sizzy.co](../videos/4fntwuOoedA.md)
`4fntwuOoedA` · AI Engineer · 2026-05-18 · q2 · intro · talk · also: agent-architecture, multi-agent, memory

Kitze (Sizzy.co) on his personal-agent journey, from to-do apps to OpenClaw-style agents, and his view that apps will give way to a personal agent OS that prompts the user.

- Techniques: Nested topic description injection; Per-topic specialized agents; Labeled cron messages with full conversation context; Visible tool-call UI
- Tools: OpenClaw, Hermes, Paperclip, Codex, Claude Code, Claude Cowork, Tmux, Telegram, Discord, Tasker, IFTTT, Notion

## [MCP UI: Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps](../videos/o-zkvb0iFDQ.md)
`o-zkvb0iFDQ` · AI Engineer · 2026-05-18 · q3 · intro · talk · also: mcp-and-tools

MCP Apps lets an MCP tool return an interactive UI that the host renders in a sandbox, with UI events routed back through the host so vendors keep their branding and the host keeps conversation context.

- Techniques: Tool returns a UI resource; Route UI events through the host; Choose the message type by how much control you need; Sandboxed host renderer; Pick a UI generation mode per host; Build with the official SDK and skills
- Tools: MCP Apps, MCP-UI, Claude, ChatGPT, VS Code, Cursor, GitHub Copilot, PostHog, Shopify, Hugging Face, Booking, Airbnb

## [Viktor: AI Coworker That Lives in Slack — Fryderyk Wiatrowski](../videos/ohKt066uFhg.md)
`ohKt066uFhg` · AI Engineer · 2026-05-18 · q2 · intro · talk · also: enterprise-adoption, security-guardrails, memory

Viktor's co-founder on building a company AI employee that lives in Slack: shared integrations, scoped access, memory across many users, and why tone and staged rollout matter.

- Techniques: Shared-integration inheritance with per-integration scoping; Thread roll-over on new DM; Treat edits and deletes as control signals; A/B test model personality, not only task scores; Staged proactivity rollout; Analytics check before acting on a claim; Browser-DOM web agent (2023 baseline)
- Tools: Slack, Viktor, OpenClaw, Claude Code, Claude Cowork, Opus 4.6, GPT-5.4, PostHog, Gmail, Meta Ads, WebArena

## [Agents on the Canvas in tldraw — Steve Ruiz, tldraw](../videos/sPUjIBH5Cwg.md)
`sPUjIBH5Cwg` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: multi-agent, sandboxing-execution, security-guardrails

Steve Ruiz (tldraw) shows how agents moved from one-shot drawing on a whiteboard to multiple agents working as a team on a shared canvas, and the safety trade-offs of letting them script a desktop app.

- Techniques: Structured-output shape drawing; Produce-review-iterate loop; Leader/follower multi-agent on shared state; Expose a runtime API for agent-written code; Prompt for spatial and coordinate conventions
- Tools: tldraw, Electron, Claude, Cursor, Make Real

## [Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub](../videos/ClWD8OEYgp8.md)
`ClWD8OEYgp8` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: coding-agents, multi-agent, context-engineering

Maggie Appleton (GitHub Next) argues agents have shifted the bottleneck from building to agreeing on what to build, and previews ACE, a shared multiplayer environment for team-plus-agent work.

- Techniques: Shared always-on agent session per task; Whole-conversation context as prompt input; Plan first, co-edit, then execute; Session summary for switching between parallel sessions; Backward-compatible PRs that link back to the session
- Tools: GitHub ACE (Agent Collaboration Environment, research prototype), Claude Opus 4.6 (model used in the demo), Bun (bun install / bun dev in the demo project), VS Code (real-time multiplayer editing in the shared cloud machine), Slack, Jira, Linear (named as coordination tools that are not built for agentic work)

## [Agents for Everything Else — swyx](../videos/zepu8Kk6FBQ.md)
`zepu8Kk6FBQ` · AI Engineer · 2026-05-18 · q3 · intro · keynote · also: enterprise-adoption, coding-agents

swyx describes how the nine-person AI Engineer team runs its business with coding agents (Devin, Claude Cowork), and argues agents should handle the routine "everything else" work, not just code.

- Techniques: Figma-to-site via coding agent; Code as the CMS source of truth, maintained by an agent; Agent as ops triage for routine requests; Prioritised concern reduction for AI adoption
- Tools: Devin, Claude Cowork, Figma, Sanity, Notion, Google Sheets, Sessionize, Supabase, React, OpenClaw, tldraw

## [AgentCraft: Putting the Orc in Orchestration — Ido Salomon](../videos/kR64LOqBBCU.md)
`kR64LOqBBCU` · AI Engineer · 2026-05-18 · q2 · intro · demo · also: multi-agent, coding-agents, pr-code-review

Ido Salomon demos AgentCraft, an RTS-style orchestrator for many coding agents, arguing the human is the bottleneck and offering visibility, campaigns, review bundles and shared workspaces as fixes.

- Techniques: Filesystem-projected agent map with collision heat map; Hotkey cycling to agents that need attention; Campaign mode: broad goal in a container, plan first; Review bundles with rationale and visual evidence; Best-of-N parallel attempts with human selection; Soft coordination via shared human and agent chat
- Tools: AgentCraft, MCPUI, MCP Apps, Cursor, Claude Code, Codex, OpenClaw, Git, Chrome

## [Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably](../videos/YNJvm7t3yq8.md)
`YNJvm7t3yq8` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: agent-architecture, multi-agent

Ably's Mike Christensen argues that AI chat UX breaks under direct HTTP/SSE streaming and proposes durable sessions (a shared, resumable channel between agents and clients) to get resilient streams, multi-device sync, and live steering or cancel.

- Techniques: Durable session as a shared channel; Hand-rolled resumable stream (the baseline he contrasts with); Bidirectional transport to separate cancel from disconnect; Multi-agent writes straight to the shared session; Any-client control through the session; Human handoff as another session participant
- Tools: Ably channels, Ably AI Transport, Server-Sent Events (SSE), WebSockets, Redis, Vercel AI SDK, TanStack AI

## [Agents need more than a chat - Jacob Lauritzen, CTO Legora](../videos/XNtkiQJ49Ps.md)
`XNtkiQJ49Ps` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: agent-architecture, evals, skills-self-improvement

Legora's CTO argues that vertical agents need more than chat: make work verifiable, let humans steer through skills and decision logs, and use persistent artifacts as the collaboration surface.

- Techniques: Proxy verification with golden examples; Task decomposition by verifiability; Allowlist guardrails for agent actions; Skills as judgment encoded at work nodes; Elicit-or-decide with a decision log; Persistent, scoped artifacts as the collaboration surface
- Tools: Claude Code

## [The New Application Layer - Malte Ubl, CTO Vercel](../videos/XKup1pj-34M.md)
`XKup1pj-34M` · AI Engineer · 2026-05-18 · q3 · intro · keynote · also: agent-architecture, sandboxing-execution, enterprise-adoption

Vercel CTO Malte Ubl argues agents are a new kind of software that makes long-tail automation affordable, names practical agent archetypes, and says harnesses should run apart from the code they generate.

- Techniques: Compress-the-research agent; Information-surfacing agent; Ask-what-you-hate discovery; Harness and code execution split; CLI and API first for agent-facing products; Lightweight bash sandbox for agents
- Tools: Vercel AI SDK, Chat SDK, JustBash, Claude, Codex, Granola, Pi, OpenClaw

## [Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban](../videos/W76woOYHlvY.md)
`W76woOYHlvY` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: software-factory, coding-agents, agent-architecture

Louis Knight-Webb (Vibe Kanban) argues engineers will mostly plan and review as agents run longer, then live-demos shutting his company down through the tool.

- Techniques: Task-type mode selection; Clarifying-question planning; Parallel agent workspaces; PR comment shepherding
- Tools: Vibe Kanban, Claude Code, Codex, Cursor, GitHub Copilot, Playwright MCP, GitHub, Cloudflare CDN

## [Taste & Craft: A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @The Pragmatic Engineer](../videos/wjk0ulMAkbc.md)
`wjk0ulMAkbc` · AI Engineer · 2026-05-18 · q3 · practitioner · interview · also: testing-verification, coding-agents

Linear's CTO and Gergely Orosz on why AI makes taste and quality the scarce advantage. Linear's practices: Quality Wednesdays, a zero-bug policy, and week-long paid work trials.

- Techniques: Quality Wednesday; Zero-bug policy with agent triage; Single-shot agent PRs for incoming bugs; Human-judged feel in agent output; Paid greenfield work trial; Open, tagged customer meeting archive
- Tools: Claude Code, Opus 4.5, Linear, Apple Human Interface Guidelines

## [Feedback Loops are All You Need — Mehedi Hassan, Granola](../videos/ON5LIT0M4do.md)
`ON5LIT0M4do` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: observability, testing-verification

Granola's Mehdi Hassan argues that shipping LLM features needs your own tracing, per-PR web previews, and fast feedback loops, not better one-shot prompts.

- Techniques: Home-built LLM tracing store with an internal UI; Web-shell preview per PR; Agent self-verification with screenshot evidence; Own the web search path
- Tools: Electron, Cursor, AI SDK, CloudWatch, OpenTelemetry, Tauri, Figma

## [Mastering AI Pricing — Mayank Pant, Stripe](../videos/CrqPcIZOOXA.md)
`CrqPcIZOOXA` · AI Engineer · 2026-05-18 · q3 · intro · talk · also: infra-cost-scaling, governance-compliance

Stripe's billing architect on AI pricing: treat the first price as a hypothesis, use base-plus-usage hybrid pricing with credits, add usage guardrails, and choose billing infrastructure that lets you change prices quickly.

- Techniques: Credit abstraction layer; Base fee plus usage fee (hybrid); Usage guardrail stack; Value-to-metric mapping; Grandfathered pricing versions; Per-event rating with explainable invoices
- Tools: Stripe Billing, Metronome

## [How to Leverage Domain Expertise — Chris Lovejoy, Notius Labs](../videos/kfSDc2eVLo4.md)
`kfSDc2eVLo4` · AI Engineer · 2026-05-18 · q3 · practitioner · talk · also: enterprise-adoption, evals

Chris Lovejoy (Notius Labs) argues winning in vertical AI is an organizational problem, and gives a three-role framework (oracle, evaluator, architect) for placing domain experts, with Granola, Tandem and Anterior as cases.

- Techniques: Oracle role (domain expert edits the product directly); Decentralized oracle; Evaluator role (expert defines metrics; engineers improve); Architect role (self-improving system); Role progression check
- Tools: LLM-as-judge, clinician review dashboard

## [Build & deploy AI-powered apps — Paige Bailey, Google DeepMind](../videos/G_bHFmEAarM.md)
`G_bHFmEAarM` · AI Engineer · 2026-05-18 · q2 · intro · demo · also: models-research, vibe-coding-app-building

Paige Bailey (Google DeepMind) gives a demo-heavy tour of Gemini models, AI Studio tools (grounding, URL context, code execution), Build for prompt-to-app, Genie 3, Veo 3.1 Lite, Gemma 4 and Gemini Live.

- Techniques: Clip video by time and frame rate; Let code execution do the exact work; URL context as lightweight grounding; Per-task thinking level; Prompt expansion before generation; Plan with a big model, act with a local model; Compare mode for model choice; Export UI experiments to code; System instructions for voice output style
- Tools: Google AI Studio, Gemini API, Gemini Live, Gemini 3.1 Pro, Gemini 3.1 Flash, Gemini 3.1 Flash-Lite, Google Search grounding, URL context, code execution, Build (AI Studio app builder), Firebase / Firestore, Cloud Run

## [8 Vibe Coded Apps That Generated Millions Overnight](../videos/zNOunnM1jTs.md)
`zNOunnM1jTs` · AI LABS · 2026-05-02 · q2 · intro · other · also: vibe-coding-app-building, coding-agents

Anecdotal roundup of eight solo, vibe-coded apps with self-reported revenue; the useful part is a few habits (small prompts, outsourced dependencies, defining an ICP first), not the numbers.

- Techniques: Incremental, chunked prompting; Minimal correct context; Model fallback chain; Design first, then modular build; Template-guided UI generation; Stack choice for AI tools; Outsource commodity operations; Real-time multiplayer transport; Define the ICP before the build
- Tools: Claude, Claude Code, Cursor, ChatGPT, Grok, Grok 3, Claude Sonnet 3.7, Gemini, GPT, Midjourney, ElevenLabs, Next.js

## [We Already Have Something Better Than Claude Design](../videos/GbuwosWEvHo.md)
`GbuwosWEvHo` · AI LABS · 2026-05-02 · q2 · intro · review · also: claude-code, coding-agents, context-engineering

AI LABS argues Claude Design is mostly hype: Claude Code with Opus 4.7 can match it, and it adds Git, parallel worktrees, and skills. The evidence is one anecdotal comparison plus sponsor-heavy, unverified claims.

- Techniques: Clarifying-question skill to replace Claude Design's intake flow; Hero video background plus animation libraries; Component libraries and MCP for UI consistency; Parallel design variants in git worktrees; Prototype as HTML mock-ups
- Tools: Claude Code, Claude Design, Claude Opus 4.7, Claude Opus 4.6, GSAP, Lenis, ShadCN, ShadCN MCP server, Aceternity UI, Hero UI, scrollytelling skill, Figma

## [The NPM Package Everyone Is Adding To Their Site (Web Haptics)](../videos/zAbQE6K0d1k.md)
`zAbQE6K0d1k` · Better Stack · 2026-04-02 · q3 · intro · tutorial · also: dev-tools

Walkthrough of web-haptics, an npm package that adds vibration feedback to websites through a React hook, custom patterns, and a hidden-switch trick that makes it work on iOS.

- Techniques: Basic React trigger; Preset patterns; Custom vibration array; Hidden-switch fallback for iOS; Feature detection before rendering haptic UI
- Tools: web-haptics (npm package, the video spells it 'webhaptics'), React hook (useWebHaptics, captioned as 'use web haptics'), Svelte helper, Vanilla JavaScript API, navigator.vibrate (Web Vibration API), web-haptics package website editor

## [Anthropic's Head of Design Just Killed The Old Process](../videos/X4vAlWtsJD4.md)
`X4vAlWtsJD4` · AI LABS · 2026-04-02 · q2 · practitioner · tutorial · also: vibe-coding-app-building, context-engineering, coding-agents

A walkthrough of how an AI Labs team now builds app prototypes: actors and constraints first, PRD and architecture files, a Next.js and Supabase prototype with mock data, then a backend added only when needed.

- Techniques: Actor-first requirements; Constraints instead of tool instructions; PRD interview prompt; Layer prompt to architecture.md; Scaffold Next.js with Supabase, then apply a frontend-design skill; Mock-data prototype for sign-off; Task lists from architecture.md; API spec from frontend code plus PRD plus architecture; Supabase MCP for schema and migrations; Front end talks directly to the database; backend only when needed; Delegate the backend layer to a cloud agent
- Tools: Figma, Next.js, Supabase, Supabase MCP, Python, Warp Oz (sponsored cloud-agent orchestration), Stripe, Google authentication, Anthropic general-purpose frontend-design skill

## [Pencil, AI Agents & The Future of Design | Better Stack Podcast Ep. 13](../videos/FqD_hlQSQIk.md)
`FqD_hlQSQIk` · Better Stack · 2026-04-02 · q3 · intro · interview · also: multi-agent, coding-agents, models-research

Pencil's CEO on "vibe designing": a canvas stored as structured JSON in git that humans and agents edit together, with elicitation, parallel agents and speed as the real bottlenecks.

- Techniques: Keep the design as a structured file in the repo; Drop references into the agent chat as a rules-plus-libraries-plus-images bundle; Extract a palette from a vibe image; Partition a page across parallel agents by region; Run the same task across several models side by side; Elicit requirements before building; Correct the agent in a second round instead of restarting; Edit other regions while the agent works
- Tools: Pencil (pencil.dev), Cursor, Windsurf, Antigravity, VS Code, Codex, Claude Code, Opus 4.6, Opus 4.5, Sonnet 3.5, Sonnet 3.7, Gemini

## [This Changed The Way I Design With AI](../videos/sdxJEd7nqiQ.md)
`sdxJEd7nqiQ` · AI LABS · 2026-03-02 · q3 · practitioner · review · also: claude-code, coding-agents, skills-self-improvement

Pencil.dev design-to-code workflow with Claude Code: a file-watcher syncs .pen edits to code, subagents build pages, and a UX-audit skill raised the site grade from C to B.

- Techniques: Design file as a repo artifact; Save-triggered sync watcher; Pre-approve permissions for unattended claude runs; One subagent per page with shared docs; XML-tagged task prompts; Layer Lenis over GSAP for scroll; UX Audit skill with a scored re-run loop
- Tools: Pencil.dev, Claude Code, Claude CLI, Claude Opus 4.6, Codex, Figma MCP, Stitch, Bolt, npm, Git, GSAP, Lenis

## [Stack Overflow is Dead (Here's Why)](../videos/dsfqyVYkrbM.md)
`dsfqyVYkrbM` · Better Stack · 2026-02-02 · q2 · intro · other · also: dev-tools, rag-retrieval

Opinion essay (Better Stack) arguing Stack Overflow's question volume collapsed after 2014 moderation changes, was accelerated by ChatGPT, and that AI is gatekeeping public developer knowledge.
- Tools: Stack Overflow, ChatGPT, Answer Overflow, Discord, Slack, Reddit, Apollo (third-party Reddit app, mentioned as shut down)

## [Tailwind is Dying... (this is bad!)](../videos/YIRugFtqBsM.md)
`YIRugFtqBsM` · Better Stack · 2026-02-02 · q2 · intro · news · also: dev-tools, vibe-coding-app-building

A Better Stack commentary on a Tailwind CSS maintainer's refusal to review an LLMs.txt PR, arguing AI is eroding docs traffic and the paid products that fund open source.

- Techniques: Publish an LLM-optimized docs endpoint (LLMs.txt); Tie docs funnel to paid products, and track docs traffic against usage
- Tools: Tailwind CSS, Tailwind Plus, Tailwind v4, LLMs.txt, npm, ShadCN, Laravel, Sidekiq, Elastic, Redis, Anthropic, OpenAI

## [The Free Open Source Jira Killer Devs Love](../videos/pgWHATQzkHk.md)
`pgWHATQzkHk` · Better Stack · 2026-02-02 · q2 · intro · review · also: dev-tools

Short hands-on review of Plane, an open-source, self-hostable issue tracker pitched as a Jira/Linear alternative. Covers Docker self-hosting in about two minutes and the cloud-only AI features, with honest notes on paywalls.

- Techniques: Self-host Plane with Docker; Enable AI in a self-hosted or cloud workspace
- Tools: Plane, Docker, Kubernetes (optional self-host path), curl, nano, OpenAI API, React, TypeScript, Django, PostgreSQL, Redis, Jira

## [The Greatest Design System I've Ever Used](../videos/61Z2jLH4yGU.md)
`61Z2jLH4yGU` · AI LABS · 2026-01-02 · q2 · intro · review · also: vibe-coding-app-building, mcp-and-tools

A short AI-design tool roundup: Design OS for guided planning, image generators, competitor-screenshot style extraction, Figma-to-Lottie animation and an HTML-to-Figma MCP, with a sponsored agency pitch at the end.

- Techniques: Design OS planning loop before building; Competitor style extraction into Claude Code; Figma animation to Lottie to Claude Code; HTML to Figma via MCP
- Tools: Design OS (Builder Methods), Claude Code, Claude, Cursor, GitHub Copilot, Viscom, Google Mixboard, Nano Banana, Go Full Page (browser extension), Figma, Magic Animator (Figma plugin), Lottie (Figma plugin)

## [Gemini Designer is INSANE... Build Beautiful Websites in Minutes](../videos/v9Rd_l6gLjU.md)
`v9Rd_l6gLjU` · AI LABS · 2025-12-02 · q3 · practitioner · tutorial · also: vibe-coding-app-building, coding-agents, context-engineering

Walkthrough of Google Stitch, an AI UI designer, plus a six-phase Klein rules-file workflow that turns exported Stitch HTML into a Next.js app and validates it against the designs.

- Techniques: Iterative screen-by-screen prompting in Stitch; Design-system extraction from exported HTML (phase 1); Per-page analysis and component library (phases 2-3); Navigation-flow mapping (phase 4); Blueprint-then-implement (phase 5); Validation checklist and scorecard (phase 6); Build from HTML, not screenshots
- Tools: Google Stitch, Klein (VS Code extension, multi-model, rules file, MCP store), VS Code, Next.js, Figma (via Klein's MCP store), ChatGPT (GPT-5 Temporary), Claude Pro, Material UI, Arc browser (example prompt)

## [A Problem You Never Knew About](../videos/w3pmfaczpLc.md)
`w3pmfaczpLc` · AI LABS · 2025-12-02 · q2 · intro · review · also: mcp-and-tools

Sponsored demo of Thesis's C1, a generative UI API that turns LLM output into interactive components (forms, tables, dashboards) via a React SDK. Pitch-level; no evaluation data.

- Techniques: Generative UI middleware in front of the LLM; Two-step retrofit of an existing AI app; Form submission as the next prompt; Documentation skill for coding agents
- Tools: Thesis C1 (generative UI API), C1 React SDK, Vercel AI SDK (transcribed as 'Versal AI SDK'), GPT-5, Claude, Claude skill (custom, for C1)

## [Shadcn's AI Elements are AWESOME (easiest way to build a chat app)](../videos/dS7hyPNvIb8.md)
`dS7hyPNvIb8` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: vibe-coding-app-building, dev-tools

A quick tour of Vercel's AI Elements, shadcn-style chat components built for the AI SDK, and a claimed five-minute build of a chat app with web search and markdown rendering.

- Techniques: Install AI Elements into an existing shadcn project; Chat screen composition; Per-request web-search switch
- Tools: AI Elements (Vercel), AI SDK (Vercel), shadcn/ui, shadcn CLI, Tailwind CSS, react-markdown, react-syntax-highlighter, Prism, Perplexity (model with built-in web search), GPT-5, Claude (model, transcribed as 'ClaudeForce'), ChatGPT (named as a clone example)

## [Copilot Kit Made My React App Think For Itself Using AI](../videos/rYVbw1wSnMk.md)
`rYVbw1wSnMk` · Better Stack · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, dev-tools

A 5-minute walkthrough of CopilotKit, which lets a React app expose its data to an LLM, let the model change app state, and call MCP tools, with a self-hosted Express runtime.

- Techniques: Server-side runtime endpoint for the LLM key; Expose app data to the model via a readable-context hook; Let the model change app state via an action hook; Self-hosted MCP through the Vercel AI SDK MCP client; Cloud-hosted MCP as a frontend-only change
- Tools: CopilotKit, React, Vite, Tailwind CSS, Next.js, Express, Anthropic API (Claude), Composio (MCP server), GitHub (via Composio MCP tools), Model Context Protocol SDK, Vercel AI SDK (experimental MCP client), LiteLLM (mentioned as a wish, unmet)

## [Tempo Labs Tutorial: The Ultimate Vibe Coding Package](../videos/k6uBbUZ9MZg.md)
`k6uBbUZ9MZg` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building

Tutorial walkthrough of Tempo Labs, an AI app builder that wires Next.js, Supabase auth/database and Stripe payments before generating a gradient-wallpaper SaaS from a PRD-first prompt. Mostly a promotional demo with few verified claims.

- Techniques: Pre-wire integrations before the first build prompt; Supabase connection via Tempo; Stripe test-mode wiring; Adding plans through the Stripe product catalog; PRD-first build prompt with a subtask loop; Fix client-side rendering by prompting
- Tools: Tempo Labs (Tempo), Next.js, Supabase, Supabase edge functions, Supabase MCP, Stripe, Stripe webhooks, Mermaid, Cursor, Windsurf, Aceternity UI, Expo

## [Add this Chrome Extension to 10X your productivity](../videos/j8KcvLrZ9uU.md)
`j8KcvLrZ9uU` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: agent-architecture

A walkthrough of MindStudio's Chrome extension for running prebuilt browser agents and building a simple word-lookup agent with its visual block builder. Mostly a product tour with a hype title and thin technical depth.

- Techniques: Install and pin the MindStudio extension; Build a selection-driven lookup agent in the visual builder; Workaround for end-session returning JSON
- Tools: MindStudio (Chrome extension and agent builder), Chrome Web Store, Arc browser, Claude 3.5 Haiku (free model in builder), GPT 4.0 Mini (free model in builder), ChatGPT (mentioned as the manual alternative), Cursor (mentioned), Windsurf (mentioned)

## [ChatGPT Apps vs n8n vs AgentKit: The Future of AI Automation](../videos/lcqlgif2hFA.md)
`lcqlgif2hFA` · AI LABS · 2025-11-02 · q2 · practitioner · tutorial · also: mcp-and-tools, vibe-coding-app-building

Walkthrough of building a ChatGPT app as a self-hosted MCP server (Express, Google Places API) exposed through ngrok and registered in ChatGPT developer mode. Title promises an n8n/AgentKit comparison that never appears.

- Techniques: Prompt-driven MCP server scaffold for a ChatGPT app; Reuse an existing MCP server as a ChatGPT app; Expose localhost with ngrok for ChatGPT; Register the MCP endpoint in ChatGPT developer mode; Widget output over plain text, polished with ShadCN
- Tools: ChatGPT apps (OpenAI), OpenAI apps SDK, MCP (Model Context Protocol) SDK, Express, Google Places API, ngrok, ShadCN, Cursor, Codex, Claude Code, Make.com (sponsor), n8n (named in title only)

## [AI Tool Converts Your Sketch into Code Instantly!](../videos/p5hEVQIisgc.md)
`p5hEVQIisgc` · AI LABS · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building, inference-serving

Demo and local-install walkthrough of Groq App Gen, an open-source web app that generates and iterates on small web apps from a sketch plus text prompts on Groq inference; speed is asserted, not measured.

- Techniques: Local install of Groq App Gen; Sketch then prompt; One change per prompt, verify each; Generate the edit list with a second LLM
- Tools: Groq App Gen (open-source web app, GitHub repo), Groq API / Groq inference, Llama 3.3 70B (spoken as 'Lama 3.37 70 billion' in captions), Next.js, TypeScript, npm, Python, VS Code, Windsurf, Cursor, ChatGPT

## [GitHub Spark Is INSANE – A Full App in Just 20 Minutes!](../videos/Lwi6VKBl7EU.md)
`Lwi6VKBl7EU` · Better Stack · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building, coding-agents

A Better Stack walkthrough of GitHub Spark, a browser-based vibe-coding platform, building a movie-rating app from one prompt in about 4 minutes, with the caveats that it is React/TypeScript-only, needed a manual API key, and was not responsive.

- Techniques: Front-load the full feature list in one prompt; Supply the missing credential the builder asks for, and verify it; Iterate through the suggestion panel while using the app; Tune the in-app LLM through the prompts tab; Check responsiveness explicitly
- Tools: GitHub Spark, Claude Sonnet 4, Kiro (Amazon IDE, mentioned only), React, TypeScript, Tailwind CSS, TMDB movie API, Unsplash, GitHub Copilot Pro Plus

## [Why Your LLM Answers Are Mediocre (And How to Fix It)](../videos/Ym-iMJ-sds0.md)
`Ym-iMJ-sds0` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: context-engineering, memory

Beginner tips for getting better LLM answers in ChatGPT (prompting, context windows, memory, Projects, deep research, Canvas), with a brief tour of Codex, Gemini CLI and Claude Code.

- Techniques: Specific, iterated prompting; Fresh chat per idea; Project system prompt with role and sample output; Escalate from web search to deep research; Canvas for partial edits
- Tools: ChatGPT, GPT-5, Claude, Gemini, Gemini CLI, Codex, Claude Code, Nano Banana, ChatGPT Canvas, ChatGPT Deep Research, ChatGPT Projects, ChatGPT Voice Mode

## [3 Simple Ways To EARN Money With Claude Code Apps](../videos/Y2oK0nubq9A.md)
`Y2oK0nubq9A` · AI LABS · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building, claude-code

Walkthrough of consumer-app paywall patterns (instant-value previews, habit hooks, usage caps, tier ladders) plus a Claude Code design-command workflow for cloning paywall screens. Middle segment is sponsored.

- Techniques: Progress-gated free tier for education apps; Anchored yearly pricing; Progress hook with time or feature gating; Usage cap at point of need; Three-tier ladder with a highlighted middle; Slash-command design pass for prototypes; Screenshot-to-clone reference
- Tools: Claude Code, Cursor, VS Code, SuperDesign, design.md (prompt file), Flowbite, Paywall Screens, Make, HabitKit, Sleep Cycle, Babbel, CapCut

## [Replits NEW AI Agents Are INSANE](../videos/v1jLYiW0AWc.md)
`v1jLYiW0AWc` · AI LABS · 2025-11-02 · q3 · intro · review · also: vibe-coding-app-building, mcp-and-tools

Hands-on beta test of Replit Agent 3's Agents and Automations builder: guided setup via Slack, Telegram or scheduled triggers, OAuth connectors, and automatic app testing, with real gaps in memory, integrations and Slack deployment.

- Techniques: Least-privilege Notion OAuth; Test memory after deployment; Ask the agent to explain a missing action; Telegram publishing setup; Verify side effects end to end
- Tools: Replit Agent 3, Replit Agents and Automations, Replit app testing, Replit Stripe integration, OpenAI API, Notion (connector), Outlook (connector), OneDrive (connector), Spotify (connector), Linear (connector), Slack (connector and deployment target), Telegram (deployment target)

## [Google Firebase is an AI IDE now... (and its good!?)](../videos/dAE4YloBUgI.md)
`dAE4YloBUgI` · Better Stack · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building, coding-agents

A Better Stack walkthrough of Google's Firebase Studio, a browser IDE that turns a prompt into a blueprint, a built app, and a Firebase deployment. The presenter finds the prototyping flow useful but the annotation and AI-injection behavior unreliable.

- Techniques: Confirm the blueprint before the build; Auto-provision the Gemini key from the build prompt; Scoped edit with inspect-element; Annotation overlay (lower reliability); Phone check via public preview link; Drop into the code view for manual fixes; Publish with Firebase App Hosting
- Tools: Firebase Studio, Project IDX (earlier name of Firebase Studio), Gemini 2.5 Pro, Gemini Flash, Gemini 2.5 Pro Experimental, Gemini API, Google AI Studio, Excalidraw, ShadCN UI, Next.js, Astro, Firebase App Hosting

## [ChatGPT Search Just Launched! Say Goodbye to Google?](../videos/f57EGI35bwI.md)
`f57EGI35bwI` · AI LABS · 2025-11-02 · q2 · intro · review · also: rag-retrieval

Short AI LABS walkthrough of ChatGPT's web search for Plus users, with cited sources, live stock and flight queries, and a Chrome extension that routes browser searches to ChatGPT.

- Techniques: Run a cited web search in ChatGPT; Make ChatGPT the browser's default search
- Tools: ChatGPT, ChatGPT web search, Google Search, Perplexity, Google Chrome, Chrome Web Store

## [MCP-UI could be the future - Here's Why](../videos/aziRV2DAWew.md)
`aziRV2DAWew` · Better Stack · 2025-11-02 · q3 · intro · review · also: mcp-and-tools

Better Stack demos MCP-UI, an add-on that lets MCP tools return sandboxed UI components (mainly iframes) instead of text, and argues it could shape how chat apps handle commerce and brand-controlled UI.

- Techniques: Return an iframe UI resource from an MCP tool; Extract one component into its own route; Auto-size the iframe from the page; Send component actions back to the host as messages; Pick the content type by complexity
- Tools: MCP-UI, Model Context Protocol (MCP) SDK (Anthropic), Goose (client), ChatGPT, Remote DOM (Shopify), React, TanStack Router, iframe / window.postMessage

## [The Windsurf vs Cursor rivalry just reached a turning point](../videos/gejEvBWbgHA.md)
`gejEvBWbgHA` · AI LABS · 2025-11-02 · q2 · intro · news · also: coding-agents, vibe-coding-app-building

Windsurf feature tour: select a live page element in the preview, describe the change to Cascade, and it edits the code. Also covers Tab to Import, linter integration, suggested actions, built-in MCP docs and admin model controls. Mostly unmeasured demos.

- Techniques: Select-and-describe UI edits; Batch section edits for animations; Let the agent fix its own build errors; Drag files into the agent instead of referencing them
- Tools: Windsurf, Cascade, Cursor, Claude 3.7 (thinking mode, as named by the host), GPT-4.5 (as named by the host), DeepSeek V3, MCP

## [We Tested Google’s New AI Coding Tool Opal (Honest Review)](../videos/Uz3p1dovTeo.md)
`Uz3p1dovTeo` · Better Stack · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building

Hands-on review of Google's Opal, a node-based no-code tool for building AI "mini apps" from text prompts. The reviewer finds weak output control, broken image embedding, and no real sharing or embedding path.

- Techniques: Precise API-naming node prompt; Separating a broken image from a bad URL; Re-running to measure variance
- Tools: Google Opal, Gemini, Imagen 4 (heard as Imogen4 in captions), Google Maps API, Google Maps Static API, Google Search, Claude Code (heard as Cloud Code in captions), Kiro, Spark

## [AI Coding with Cursor & Claude: Build Apps That People Keep Using in 5 Simple Steps](../videos/i_31WoayEIo.md)
`i_31WoayEIo` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building, context-engineering, mcp-and-tools

Tutorial on building a photo-cleaner iOS app with Cursor and Claude: user journey saved in a markdown file, HTML prototype, palette, fonts, icon, Swift port and animations guided by Context7 docs.

- Techniques: Persistent context files in the repo; Specify the user journey first, then build an HTML prototype; Palette-from-elements prompt sequence; Google Fonts embed into the HTML prototype; App icon via ChatGPT image model with palette constraint; Context7 MCP for framework docs; Fresh chat per task plus Cursor to-do list; Two-stage animation pipeline; Screenshot-driven bug fixing
- Tools: Cursor, Windsurf, Lovable, bolt.new, Claude Code, Gemini CLI, Claude, ChatGPT, ChatGPT image model (called ChatGPT 4 image model in the video), Context7 MCP, Google Fonts, HTML

## [Hao Sheng on Building Human-Business Interfaces with AI | Better Stack Podcast Ep 3](../videos/IFSK3_M6Fuk.md)
`IFSK3_M6Fuk` · Better Stack · 2025-11-02 · q2 · intro · interview · also: rag-retrieval, enterprise-adoption

Hao Sheng (Expertise AI) on a human-to-business interface that generates per-visitor pages, with founder lessons from Dialogflow, Cresta and bootstrapping; mostly narrative, thin technical detail.

- Techniques: Start-from-problem validation before building; Query rewriting before retrieval; Multimodal retrieval with cross-modal consistency checks; Human-in-the-loop labeling for intent classifiers; Per-visitor generated page from conversation
- Tools: Dialogflow (Google), Expertise AI (formerly Chat Simple), Cresta, HubSpot, AlexNet, ImageNet

## [OpenAI Agent Builder vs Claude: Who Wins Multi-Agent Workflows? (Complete Comparison)](../videos/sLiVXlIlSBQ.md)
`sLiVXlIlSBQ` · AI LABS · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, agent-architecture, coding-agents

A walkthrough of OpenAI's AgentKit (Agent Builder, ChatKit, widgets), with a Speechmatics sponsor segment up front; practical for seeing the visual workflow and ChatKit setup, thin as a head-to-head comparison.

- Techniques: Classifier-then-route agent workflow; Human approval gate in a workflow; Remote MCP server registration per agent; ChatKit starter quickstart; Theme via Playground, then hand off to a coding agent; Prompt-to-widget, then pin the format in the agent prompt; Custom widgets with Claude Code and agents.md
- Tools: OpenAI Agent Builder, OpenAI AgentKit, OpenAI ChatKit, ChatKit Playground, OpenAI Widget Builder, OpenAI vector store / file search, OpenAI guardrails node, ChatGPT apps, Zapier (MCP servers), Pipedream (MCP servers), n8n (comparison only), Next.js

## [3 Ways to Build ACTUALLY Beautiful Websites Using Cursor AI](../videos/djDZHAi75dk.md)
`djDZHAi75dk` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building

Three Cursor workflows for less generic AI-built sites: clone a reference design via an extracted design JSON, theme shadcn/ui with TweakCN, and drop in React Bits components, plus font and layout prompting tips.

- Techniques: Reference design to JSON design system, then build from it; TweakCN theme to shadcn/ui project; Drop a copied component into a named section; Font via embed code; Spec the layout explicitly and keep it in a file; Animation restraint
- Tools: Cursor, Claude, ChatGPT, TweakCN, shadcn/ui, React Bits, Aceternity UI, Google Fonts, Next.js, framer-motion, React, HTML

## [Claude Code Can Finally Make Beautiful Websites](../videos/idccdssOZQ8.md)
`idccdssOZQ8` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building, coding-agents

Three UI design principles (depth through layered color and shadows, box-based responsive layout, and a four-role color palette) for making AI-generated sites look better, shown on a cloned Airbnb-style page.

- Techniques: Color-layer depth instead of borders; Dual shadow with depth levels and a gradient; Flexible box layout with parent-child structure; Priority-based responsiveness; Four-role palette; Prompt per principle, with before/after comparison
- Tools: Claude Code (named in the title only; the transcript does not name it), Colors (palette-browsing site, named in the transcript, no URL given), Airbnb-style page clone (demo subject, not a tool)

## [Complete Guide to ChatGPT’s Canvas Update  New Tools & Features You Need](../videos/-ajtoeyu4go.md)
`-ajtoeyu4go` · AI LABS · 2024-11-02 · q2 · intro · review · also: coding-agents

A roughly 11-minute walkthrough of ChatGPT Canvas, the side-by-side editor for code and writing, covering inline edits, auto-comments, logging, port-to-language, and version navigation. Little hard data; mostly a UI tour.

- Techniques: Iterate in place with Canvas instead of re-prompting; Canvas editor actions for code: review, comments, logs, port; Canvas writing actions: Suggest Edits, reading level, polish, emojis
- Tools: ChatGPT, ChatGPT Canvas, GPT-4 (with Canvas), Python, Pygame, VS Code, C++, SFML

## [The 1 Click Solution to PRESENTATION PERFECTION No One Tells You!](../videos/de71tQ3k5xA.md)
`de71tQ3k5xA` · AI LABS · 2024-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building

Step-by-step walkthrough of generating a slide deck from pasted notes in Gamma AI, covering input methods, generation settings, and editing images and layout.

- Techniques: Generate a deck from pasted notes in Gamma; Replace a generated image; Reorganize a card's information layout; Keep AI-generation cost in check
- Tools: Gamma AI (gamma.app web app), Flux (image model used by Gamma for AI image generation, default option), Google account sign-in, PowerPoint (mentioned only as the familiar format being replaced)

## [How to hire, motivate and retain 10x engineers with David Pavlik](../videos/yr_8HIZNQOw.md)
`yr_8HIZNQOw` · Better Stack · 2024-11-02 · q3 · intro · talk · also: enterprise-adoption

Engineering leader David Pavlik on hiring, motivating and retaining top engineers, drawing on Netflix, SpaceX, Microsoft and Amazon: mission and people beat perks, and hiring is the manager's job.

- Techniques: Paid collaborative trial instead of a coding interview; Outside bar raiser in the hiring loop; Ask what motivates the candidate, then align the pitch; Recruit with an extra-mile experience; Engagement check via a best-friend-at-work question; Re-validate team alignment after a mission pivot; Life-event review and environment adjustment; Dual-track promotion with a step-back path; Stock refresher grants instead of four-year cliffs

## [AI Images Are Getting Shockingly Real - FLUX 1.1 PRO](../videos/sFZR6EG4WxU.md)
`sFZR6EG4WxU` · AI LABS · 2024-11-02 · q2 · intro · tutorial · also: voice-multimodal

Short tutorial on generating photoreal images with Flux 1.1 through Together AI, using a prompt-template trick; anecdotal, hype-driven, and untested.

- Techniques: Flux 1.1 generation on Together AI (UI steps); Photo-style prompt template (speaker's 'secret trick'); Type-word plus file-type prompt
- Tools: Flux 1.1 (Flux 1.1 Pro per the title; the transcript says Flux 1.1), Together AI (website, Google sign-in)

## [How hardware product is made with Tomas Susanka](../videos/KsgQX_kiYuM.md)
`KsgQX_kiYuM` · Better Stack · 2024-11-02 · q2 · intro · talk · also: —

Trezor's CTO walks through how a consumer hardware wallet gets made: spec, parallel design and engineering, prototypes, supplier loops, in-house testing, and stock planning. Off-topic for AI engineering.

- Techniques: Parallel design and engineering tracks from one spec; Feel-first 3D-printed prototyping; Schematic to PCB to small prototype run; Automated in-house end-of-line test fixture; Golden samples for marketing
- Tools: Altium (PCB design), 3D printing (prototype enclosures), USB-C, GitHub (open-source hardware files), STMicroelectronics MCU products (named as the MCU vendor, no model stated), Secure element (component type, unnamed)

