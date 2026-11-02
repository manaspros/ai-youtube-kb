# dev-tools — 379 videos

*non-AI developer tooling — terminals, git, editors, languages/frameworks, databases, self-hosting, Linux, logging libraries*

By channel: AI Engineer 7 · Kai Explains 7 · AI LABS 7 · Better Stack 358

**Synthesized guide:** [guides/dev-tools.md](../guides/dev-tools.md)

Newest first. Each entry: one-liner, techniques, tools. Full notes in `videos/<id>.md`.

## [I Can Control My PC From Anywhere in the World (JetKVM)](../videos/jNFv1Lr2Db4.md)
`jNFv1Lr2Db4` · Better Stack · 2026-11-01 · q3 · intro · tutorial · also: —

Better Stack walkthrough of wiring a JetKVM (open-source KVM-over-IP) plus its ATX power-button extension board into a workstation so it can be powered on and used remotely from a browser or phone.

- Techniques: Parallel power-button wiring with an ATX extension board; Four-cable JetKVM hookup; Pick a KVM connection for remote access; Browser troubleshooting for JetKVM video
- Tools: JetKVM (open-source KVM-over-IP device, ATX extension board, cloud service at app.jetkvm.com), Chrome, Windows 11, Ubuntu, Gigabyte Z890 motherboard, Nvidia RTX 5090 (GPU, HDMI source), Nvidia RTX 1590 (mentioned as the workstation GPU in the opening), WebRTC

## [The Best Git Worktree Tool I've Used (Worktrunk)](../videos/mNo24Omj8X4.md)
`mNo24Omj8X4` · Better Stack · 2026-10-31 · q3 · practitioner · review · also: coding-agents, multi-agent

Review of Worktrunk (wt), a Rust CLI on top of git worktrees that adds per-branch switching, a multi-agent status view, one-command merge, copy-on-write cloning of ignored files, and per-worktree dev ports for parallel coding agents.

- Techniques: Worktree per parallel agent; One-screen status across agents; Shell integration before first use; Cheap clone of ignored dependencies and caches; Per-worktree dev server ports; Single-command merge back
- Tools: Worktrunk (wt, Rust CLI, MIT/Apache dual license, v0.81 as stated), Claude Code (native worktrees and its worktree-creation hook), Codex, OpenCode, Gemini CLI, git, Vibe Kanban (mentioned as a Kanban-board alternative), APFS (macOS copy-on-write filesystem), ext4 (Linux filesystem, full copies)

## [I Hid a Raspberry Pi in a Pumpkin to Fix Smart Speakers](../videos/t9Jro9BAIMw.md)
`t9Jro9BAIMw` · Better Stack · 2026-10-30 · q3 · intro · tutorial · also: voice-multimodal, local-ai

Better Stack builds a Raspberry Pi voice assistant inside a pumpkin: local wake word and speech-to-text, a fast remote LLM for replies, and remote TTS. Practical on latency and soldering, light on reproducible detail.

- Techniques: Wake word -> local STT -> remote fast LLM -> TTS voice loop; Pick the LLM on measured reply speed first, then check quality; Keep TTS remote when local voice quality or speed falls short; Solder to a separate hat, then mate it to the Pi header; Check clearance between solder joints and the cooler before power-up; Insulate the pumpkin's internals with cling film
- Tools: Raspberry Pi, Perma-Proto hat (Adafruit board, as named in captions), sherpa-onnx, Parakeet (speech-to-text model), Python, DeepSeek Flash, Gemini Flash, Haiku, ElevenLabs Flash, multimeter, active cooler (Raspberry Pi)

## [Exploits Now Beat Patches: Open Source Security in the AI Era - Patrick Smyth, Chainguard](../videos/xZX3pmaB8Hk.md)
`xZX3pmaB8Hk` · AI Engineer · 2026-10-28 · q3 · practitioner · review · also: security-guardrails, skills-self-improvement

Chainguard's Patrick Smyth argues frontier AI has made exploits beat patches: cooldowns, signed artifacts, tiered SLAs, minimal rebuilt images and vetted agent skills, wrapped in a vendor pitch.

- Techniques: Package cooldown period; Sign and verify every artifact; Build dependencies from clean source; Severity-tiered remediation SLA; Minimal, frequently rebuilt base images; Treat CI/CD as an attack surface; Vet agent skills before use; Hardware-backed developer identity
- Tools: Chainguard (vendor), Wolfi (Chainguard's rolling Linux distro), Chainguard Libraries (build-from-source packages), Chainguard Actions (hardened CI/CD actions), Chainguard agent skills (hardened third-party skills), Sigstore, SLSA (captioned 'Salsa'), Mandiant mTrends report (captioned 'Mandia'), Trivy (scanner, captioned 'Trivi', attacked in the supply chain incident), Grype (captioned 'Gripe', scanner named as an example), LiteLLM (captioned 'LightedLM', described as an agent router), Axios (npm package, compromised)

## [The AI Bug Apocalypse Has Officially Started](../videos/sZaMmVUmq-I.md)
`sZaMmVUmq-I` · Better Stack · 2026-10-25 · q3 · intro · news · also: security-guardrails

Better Stack news roundup on "Black October" 2026: a leaked batch of Linux kernel SMB bugs, a wave of AI-found vulnerability disclosures, and what to patch this week.

- Techniques: Unload an unused kernel SMB server; Update-by-default patch policy; Read-only scope for agents that touch accounts
- Tools: Linux kernel, ksmbd, SMB / SMB Direct, PHP, GitLab, Node.js, VMware graphics driver, NVMe target code, Chrome, Microsoft SharePoint, Microsoft Patch Tuesday, Anthropic Mythos model

## [Why Rust Is The New GOAT For AI](../videos/R-tLX37Xgx8.md)
`R-tLX37Xgx8` · Better Stack · 2026-10-24 · q3 · intro · other · also: coding-agents, infra-cost-scaling

Better Stack argues Rust is taking over AI tooling: memory safety, no GC pauses, and single native binaries, with GitHub Copilot, Codex CLI and Bun as examples. Mostly company anecdotes.

- Techniques: Rust core behind a Python API; Ship a native library instead of a helper process; Feed compiler errors back into the agent loop; Ownership-based memory for latency-critical services
- Tools: Rust, Cargo, GitHub Copilot, Copilot SDK, Bun, Zig, Claude Code, Codex CLI, Node.js, TypeScript, Go, Python

## [The Best Agent IDE I've ever used (Orca)](../videos/8QgBcI40VC8.md)
`8QgBcI40VC8` · Better Stack · 2026-10-24 · q3 · intro · review · also: coding-agents, multi-agent

Walkthrough of Orca, a free open-source desktop app that runs Claude Code, Codex and other coding CLIs side by side with per-task git worktrees, a browser with element annotation, and multi-agent orchestration.

- Techniques: Worktree-per-task agent launch; Element-annotated fix requests from an embedded browser; Forced multi-provider split for comparison; Run the orca CLI from the terminal
- Tools: Orca, Claude Code, Codex, Goose, Kimi (transcript says 'kimmy'), Cursor, Herdr (transcript says 'Herder'), Ghostty (transcript says 'Ghosty'), GitHub, Linear, caffeinate, Apple Design skill (named in demo, source not stated)

## [A Certificate Authority Just Got Caught Using a Private Key of 4](../videos/yW1RnJ5oaMk.md)
`yW1RnJ5oaMk` · Better Stack · 2026-10-23 · q4 · practitioner · news · also: security-guardrails

Breakdown of the eMudra CA incident: eight intermediate CA private keys were trivially guessable (one was just 4). Browsers blocked them, but non-browser TLS clients that trust on-disk CA bundles stayed exposed.

- Techniques: Check EC public keys for small private keys; Upgrade on-disk CA bundles and the Go toolchain, then rebuild; Verify client trust against a known-bad test host; Verify key provenance during CA and HSM key ceremonies; Treat signature mismatches on revocation lists as incidents
- Tools: Certificate Transparency logs, Python, curl, Node.js, Go 1.27.3, Git, certifi 2026.10.19, Cloudflare WARP client, Cloudflare 1.1.1.1 app, Cloudflare Tunnel, Chrome, Firefox

## [This Looks Like Spy Software... It's Just Public Data](../videos/PQN76wcEt10.md)
`PQN76wcEt10` · Better Stack · 2026-10-23 · q3 · intro · review · also: mcp-and-tools, voice-multimodal, data-engineering

Walkthrough of God's Eye View, an open-source local globe that fuses public live feeds (planes, ships, satellites, cameras, quakes), with its feed-smoothing design and honest data caveats.

- Techniques: Run God's Eye View locally; Render the last update one step behind and interpolate; Dead reckoning for dropped feeds; Ration a free API quota with a budget; Hard spend cap for a realtime voice API; Unlock 3D tiles through an external key
- Tools: God's Eye View (open-source globe project, about 55,000 GitHub stars), Cesium JS, Vite, Node.js (24.14 or newer required; 25 unsupported), npm, SGP4 orbit model, ADS-B, AIS, OpenSky Network, MCP (Model Context Protocol) server, Claude, Codex

## [A PHP Bug Just Took Websites Offline Worldwide](../videos/Gxi_n-PtQBo.md)
`Gxi_n-PtQBo` · Better Stack · 2026-10-22 · q3 · intro · news · also: security-guardrails, governance-compliance

Better Stack news explainer on the "PHP to Shell" pair of PHP bugs (CVSS 9.2 per the video): unauthenticated remote code execution in PHP itself, a coordinated-disclosure mess that pulled the patch forward, and a warning that AI speeds up exploit building.

- Techniques: Immediate PHP runtime patching when a language-level RCE is announced; Take the service offline when an unpatched RCE is live and the patch is not yet available; Pre-deploy WAF rules before public disclosure
- Tools: PHP, Chainguard PHP images, Cloudflare WAF, GPT 5.6 Sol, Gemini 4 Argon, Claude Mythos, Debian packages, Ubuntu packages, WordPress, Drupal, Joomla, Laravel

## [Voyager's 16 Billion Mile Software Update](../videos/1NXUw8QK1L4.md)
`1NXUw8QK1L4` · Better Stack · 2026-10-19 · q3 · intro · review · also: —

How NASA keeps patching Voyager 1's 1970s flight software: rewritable memory, a dead chip worked around by relocating code, and revived thrusters. Not AI-related.

- Techniques: Dump-and-diff fault localization; Relocate code around a dead memory block; Staged reload of critical code; Test a state-flag hypothesis before declaring hardware dead; Power budgeting by shutting subsystems off
- Tools: Horizons (NASA JPL ephemeris system, queried with curl), Deep Space Network (NASA ground dishes)

## [The Internets Master Key Just Changed](../videos/NXCFYzRfQIk.md)
`NXCFYzRfQIk` · Better Stack · 2026-10-19 · q3 · intro · other · also: —

Explainer on the DNS root zone master key: why DNS needed signatures (DNSSEC), how the root key is generated and guarded in a Virginia ceremony, and the October 2026 key rollover that can break resolvers.

- Techniques: Check the root's published DNS keys; Update resolver or OS trust anchors after a root key rollover; Understand the signing chain to debug DNSSEC failures
- Tools: DNS, DNSSEC, Google Public DNS (named as Google's 8.8.8.8 resolver)

## [AI Apps in a Flash: Ship to GPUs Without Docker — Dean Quiñanola, Runpod](../videos/XczFLWEntiE.md)
`XczFLWEntiE` · AI Engineer · 2026-10-12 · q2 · intro · demo · also: infra-cost-scaling, inference-serving

RunPod's Dean Quiñanola demos RunPod Flash, a Python-first way to run and deploy GPU functions on serverless endpoints without writing a Docker image; the main takeaway is that the Docker build-push loop is the bottleneck for AI app iteration.

- Techniques: Docker-free function iteration with a local dev server; Dependencies installed at worker start-up instead of baked into an image; Endpoint-to-endpoint function calls; Network volumes for warm caches across scale-ups; Teardown of dev endpoints on cancel; Spreadsheet-driven experiment fan-out
- Tools: RunPod Flash, RunPod serverless endpoints, Docker, Docker Hub, FastAPI, PyTorch, Hugging Face, Python, GitHub

## [The Apollo 11 Code Is Open Source (and it's hilarious)](../videos/ACAd_w3D-io.md)
`ACAd_w3D-io` · Better Stack · 2026-10-12 · q3 · intro · review · also: agent-architecture

Walkthrough of the open-sourced Apollo 11 Guidance Computer code: 1960s hardware limits, a priority job scheduler that raised alarm 1202 under overload, restart checkpoints, and how to run it in an emulator.

- Techniques: Fixed-slot priority job scheduler with overflow alarm; Checkpoint-based restart protection; Interpreter VM to trade speed for code size; Verb/noun command language for constrained input; Reproducing Apollo 11 in the Virtual AGC emulator
- Tools: Apollo 11 source code (AGC assembly, GitHub), Virtual AGC (emulator project), DSKY keypad (emulated), VS Code, Raspberry Pi Pico (comparison only)

## [Deno Is Over (Cloudflare Shut It Down)](../videos/W_g7WKMwNeo.md)
`W_g7WKMwNeo` · Better Stack · 2026-10-12 · q3 · intro · news · also: infra-cost-scaling, agent-architecture

Deno's team is joining Cloudflare. The Deno runtime gets one more year of monthly fixes, Deno Deploy shuts after six months, and Cloudflare is mainly buying the team and CellD, a self-hostable durable-objects runtime.

- Techniques: Durable objects as per-entity state; Open-source the runtime to remove lock-in fear
- Tools: Deno, Deno Deploy, JSR, Cloudflare Workers, Durable Objects, workerd (WorkerD), CellD, SQLite, RustyV8 (auto-caption 'RustyVA'), Node.js, Supabase Edge Functions, Netlify Edge Functions

## [Effect 4.0 Just Got a Lot Harder to Ignore](../videos/OsL9EJWz9UY.md)
`OsL9EJWz9UY` · Better Stack · 2026-10-12 · q3 · practitioner · review · also: —

Better Stack reviews Effect 4.0, a TypeScript library that puts errors, retries, timeouts and dependency needs into the type system, and argues the stable release still carries unstable modules and inflated download numbers.

- Techniques: Encode failures in the signature with typed errors; Verify a timeout by forcing it to fail; Install the single consolidated package; Migrate with a coding agent using the migration guide; Adoption triage: where Effect fits
- Tools: Effect 4.0 (npm package `effect`), Effect Schema, TypeScript 7, Bun, npm, Zod, FP-TS (merged into Effect)

## [Move Fast and Don't Break Things: Scaling Databases for the AI Era — PlanetScale](../videos/uKUA1a0Kdfc.md)
`uKUA1a0Kdfc` · AI Engineer · 2026-10-07 · q3 · intro · talk · also: infra-cost-scaling, governance-compliance

PlanetScale's Ben argues that agent-driven change can be safe if databases are isolated, sharded, back-pressured, and branched like code, with agents given the same primitives humans use.

- Techniques: Per-segment traffic budgets with graceful degradation; Shard with a routing proxy plus per-shard replicas; Declarative sharding config as JSON for agent drafting; Schema branch, deploy request, one-click revert; Isolation by failure domain
- Tools: PlanetScale, Vitess, VTGate, MySQL, Postgres, SQLite, MCP server, CLI, VSchema

## [Claude Code Mods Can Do Basically Anything...](../videos/EiThSVZ8pME.md)
`EiThSVZ8pME` · Better Stack · 2026-10-05 · q3 · practitioner · review · also: claude-code, agent-architecture

Better Stack demos Claude Code "mods," in-process TypeScript plugins that can draw panes, status lines and rewrite events, by building a subscription-usage HUD and a Haiku-powered fake chat.

- Techniques: Build a status-line HUD mod by prompting; Map usage meters to status-bar stats; Read undocumented usage data from the /usage endpoint; Reactive commentary from Haiku; Terminal image fallback; Reopen a closed mod pane with a slash command; Persist a mod across sessions
- Tools: Claude Code, Claude Code mods, Claude Code hooks (comparison), TypeScript, Claude Haiku, Claude desktop app, /usage slash command, /backseat slash command, AGENTS.md support, diff pane

## [Columnar Databases Are Incredibly Fast. Here's Why.](../videos/mR06J55fLvo.md)
`mR06J55fLvo` · Better Stack · 2026-10-02 · q4 · practitioner · review · also: data-engineering, infra-cost-scaling

Better Stack compares Postgres, ClickHouse and DuckDB on 100M rows: columnar stores win big on aggregations, but lose on point lookups and single-row updates.

- Techniques: Split workloads by access pattern; Choose the ClickHouse sort key for the dominant filter; Insert in key order to make min/max skipping work; Avoid per-row updates on columnar stores; Benchmark with identical SQL on the same data
- Tools: PostgreSQL, ClickHouse (open-source server, shown as local server), DuckDB (embedded, single-file library)

## [Lovable Rewrote Vite in Rust... (kind of)](../videos/msSZ4CL_sNg.md)
`msSZ4CL_sNg` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: vibe-coding-app-building, infra-cost-scaling

Better Stack tests Lovable's claim that OJ, a Rust rewrite of Vite's dev server, is 4x lighter and 2x faster to start, finds small gains on a small app and larger gains on a 5000-component app, and summarizes Evan You's critique.

- Techniques: Benchmark a dev server by time-to-deepest-component plus process-tree memory; Check fast refresh state preservation with a counter component; Coalesce agent write bursts into one hot update
- Tools: OJ (Orange Juice, Lovable's Rust dev server), Vite (8.1 per the transcript; Bundle Dev Mode is experimental), Rolldown (VoidZero), Oxc (VoidZero), Rust, React, TanStack Start, Tailwind CSS, esbuild (mentioned, not used), Vite Plugin Checker, Google Chrome (benchmark harness)

## [Your AI Agent Just Changed 40 Files... Now What? (Whiteboard)](../videos/cP5PRDo3u6Q.md)
`cP5PRDo3u6Q` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: pr-code-review, coding-agents, claude-code

Walkthrough of Whiteboard, an open-source Mac app that lets a coding agent draw linked review diagrams of its own branch changes, with a privacy warning about its default telemetry.

- Techniques: Install Whiteboard as a Claude Code plugin; Turn telemetry off before opening a private repo; Review-only prompt with tool-call approval; Click-through verification of diagram blocks; Typed diagram blocks instead of free-form output; Diff reduction for large agent branches; Own-backend OpenTelemetry instead of vendor telemetry; Check trace storage before enabling trace capture
- Tools: Whiteboard (open-source Mac app, MIT, VS Code fork), Claude Code, Codex, Cursor, OpenCode, VS Code / Code OSS, Electron, Rust (diff engine), MCP, Mermaid, Archify, CodeRabbit

## [React-Native Is Dead... Thanks to AI.](../videos/r0u83Ss7QRc.md)
`r0u83Ss7QRc` · Better Stack · 2026-10-02 · q3 · intro · news · also: software-factory, testing-verification, coding-agents

Better Stack commentary on Shopify dropping React Native for native apps, with Shopify's Helix checkpoint-gated agent loop and headless app logic for fast agent testing. Opinion-led, relays Shopify's blog post.

- Techniques: Checkpoint-gated agent migration (Helix pattern); Headless state plus CLI driver for agent testing; Avoid out-of-process UI automation for agent verification
- Tools: React Native, Shopify React Native packages (FlashList, React Native Skia, Restart), Helix (Shopify in-house agent migration system), Swift, Kotlin, SwiftUI, CloudKit, Apple XCUITest

## [Claude Code Can Now Take Your App Live (GoLive)](../videos/HTscIrJhjDs.md)
`HTscIrJhjDs` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: claude-code, security-guardrails

Walkthrough of GoLive, an early agent skill plus Node CLI that takes a repo live (Vercel, Supabase, Resend, Stripe) via plan, approve, apply, verify gates, with candid caveats about consent and credential storage.

- Techniques: Plan-then-approve-then-apply with a plan ID; Verify webhooks both negatively and positively after deploy; Separate confirm flags for destructive, DNS and production-live actions; Refuse-list for paid or account-creating actions; Ownership-tagged teardown; Borrow existing CLI logins instead of minting credentials; Post-run written report with no secrets; Skill file plus a small CLI, not an MCP server
- Tools: GoLive (agent skill plus Node CLI; repo name not shown in the transcript), Claude Code, Codex, Vercel, Netlify, Supabase, Neon, Resend, Stripe (test and live modes), Terraform, SST, Lovable

## [DBX Is Almost the Perfect Free Database Client](../videos/b6rVCrBPbe8.md)
`b6rVCrBPbe8` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: mcp-and-tools, security-guardrails

Hands-on review of DBX, a free desktop database client with an optional MCP server that lets coding agents query saved connections; the reviewer praises the workflow but flags plaintext passwords in its local SQLite file as a blocker for production credentials.

- Techniques: Stand up a multi-engine local test rig; Add a connection with a test-before-save step; Register the DBX MCP server with Claude Code and check it appears; Agent prompts used for smoke testing; Audit a local client's credential store before storing production secrets
- Tools: DBX (free desktop database client, version not stated), DBX MCP server (separate binary), Claude Code (used to register and call the MCP tools), Docker Compose, MySQL, Redis, MongoDB, Postgres, SQLite (dbxdb file), DuckDB, Navicat, DataGrip

## [This Open-Source Tool Makes Claude Create Architecture Diagrams](../videos/iuJszJuiuSg.md)
`iuJszJuiuSg` · Better Stack · 2026-10-02 · q3 · practitioner · tutorial · also: coding-agents, context-engineering

Better Stack walkthrough of Archify, an open-source agent skill where the coding agent emits validated typed JSON that a local compiler renders into HTML architecture diagrams; useful for PR and design-review artifacts, not for READMEs or mapping huge repos.

- Techniques: Schema-validated diagram IR; Evidence-gated nodes; Narrow architecture question prompt; Diff two architecture snapshots; Install as an agent skill
- Tools: Archify, Claude Code, Cursor, Codex, Mermaid, GitHub

## [Cloudflare Just Saved 100TB of Memory](../videos/RTmTebnxwKc.md)
`RTmTebnxwKc` · Better Stack · 2026-10-02 · q4 · practitioner · review · also: infra-cost-scaling

Cloudflare cut DNS cache memory per entry by 56% with five Rust data-layout changes (Vec to Box, flattened lists, deduped owner names, boxed enum variants, raw wire-format bytes), freeing about 100TB fleet-wide.

- Techniques: Swap growable Vec/String for Box<[T]> / Box<str> on write-once data; Flatten parallel same-length-lifecycle lists into one list plus small offsets; Store a field only when it differs from a value already stored; Box rare large enum variants, keep common small ones inline; Keep cached payloads in the wire or serialized format; Audit per-entry footprint and allocated bytes separately
- Tools: Rust, Cloudflare 1.1.1.1 (public DNS resolver), Big Pineapple (Cloudflare's DNS resolver software, Rust), gemmalloc (allocator, as transcribed; may be an auto-caption error), DNS wire format

## [Shadcn Just Fixed Tailwind's Biggest Problem](../videos/tPQgw_DPIoM.md)
`tPQgw_DPIoM` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: coding-agents, vibe-coding-app-building

shadcn's new agent-first linter for Tailwind v4 design systems. It turns design-system rules into lint errors that AI agents can fix against, which the presenter says cut violations to zero in his eight-task test.

- Techniques: Lint the design system instead of prompting it; Use lint messages as the agent's fix instructions; Per-component contracts; Custom messages and a global note; Strict component APIs as a prerequisite
- Tools: shadcn linter (shadcn's new Tailwind design-system linter, no version stated), Oxlint, ESLint, Tailwind CSS v4, shadcn/ui, CVA (class-variance-authority, read by the linter for variant lists), Biome (no plugin yet; open GitHub issue), Starlex (transcribed name; presenter cites it as the alternative people switch to)

## [Mojo Is Finally Open Source... So I Tested It](../videos/uIqjWeO91p4.md)
`uIqjWeO91p4` · Better Stack · 2026-10-02 · q3 · practitioner · review · also: inference-serving

Better Stack tests Mojo 1.0 and its newly open-sourced compiler: a real same-file GPU kernel on a laptop, but inflated benchmarks, unstable APIs and a Qualcomm acquisition cloud the picture.

- Techniques: Benchmark against the right baseline; One-file prototype-to-kernel path; Check the stability promise against the release notes
- Tools: Mojo 1.0 (Modular), Python, NumPy, C++, CUDA, Metal, Swift, Triton, LLVM, Clang, Modular MAX (kernels), Rust

## [Polars 2.0 Says 5× Faster... So What's Changed?](../videos/uHELj20WrOc.md)
`uHELj20WrOc` · Better Stack · 2026-10-02 · q3 · practitioner · news · also: data-engineering

Better Stack walks through the Polars 2.0 release candidate: mostly a cleanup release that makes the streaming engine the default, drops row-order guarantees, and removes old APIs with replacement-naming errors. The 5x speedup is unbenchmarked.

- Techniques: Pin row order explicitly; Pre-upgrade audit for unsorted group_bys; Error-driven migration on the RC; Schema check before execution; Hold back RC features that have open bugs
- Tools: Polars 2.0 release candidate (pre-release, installed with the pre flag), Polars Python API (LazyFrame, scan_csv, collect_schema, explain), Pandas, DuckDB, Dask, Spark, uv (uv pip install), Polars Cloud (not open source), polars Rust crate 0.55, Parquet, CSV

## [Apple Hasn’t Put an LLM on Your Watch. So I Did.](../videos/IGQZuZkwVLI.md)
`IGQZuZkwVLI` · Better Stack · 2026-10-02 · q3 · intro · demo · also: local-ai, inference-serving

Better Stack runs a 90M-parameter hybrid LLM offline on a 2020 Apple Watch Series 6 via llama.cpp built for watchOS, and explains the ARM64_32 and Core ML limits that shape the port.

- Techniques: Build llama.cpp for watchOS (ARM64_32); Check the 32-bit address ceiling before picking a model; Prefer small hybrid SSM models for memory-bounded edge devices; Register tools by renaming a samples file; Voice as the input channel on a wearable
- Tools: Falcon H1 (90M, hybrid attention + Mamba-2), small M2 135M model (caption-garbled name), llama.cpp, Core ML, Xcode, watchOS / ARM64_32, Mamba 2, GGUF model format, Wikipedia tool call (sample), weather tool call (sample)

## [JavaScript's Biggest Update in Years (ES2027)](../videos/DLT6n3wCkuc.md)
`DLT6n3wCkuc` · Better Stack · 2026-09-02 · q3 · intro · news · also: —

Better Stack walkthrough of JavaScript's ES2027 proposals: Temporal, explicit resource management (using), iterator.zip and Atomics.pause are stage 4; import defer, keyed Promise.all and decorators are stage 3; signals are stage 1.

- Techniques: Replace Date with Temporal types by job; Check DST transitions with getTimeZoneTransition; Scope-bound cleanup with using and Symbol.dispose; Compose resources with DisposableStack; Parallel iteration with iterator.zip and zipKeyed; Spin-wait hint with Atomics.pause; Named results with Promise.all keyed; Lazy execution with import defer
- Tools: Temporal, Date, moment, luxon, Firefox, Chrome, Node.js, Deno, Bun, Safari, using keyword, Symbol.dispose

## [TanStack Did It Again... They Fixed Charts](../videos/odbQhwcIo4Q.md)
`odbQhwcIo4Q` · Better Stack · 2026-09-02 · q3 · intro · review · also: mcp-and-tools

Better Stack walks through TanStack Charts, a week-old framework-agnostic charting library built on a grammar-of-graphics model, and claims a much smaller bundle than Recharts and Chart.js.

- Techniques: Declare a chart as marks plus scales; Add reference lines and overlays as marks; Data-driven mark styling; Three-level theming
- Tools: TanStack Charts, React, ggplot2 (referenced as the inspiration for the grammar of graphics), Recharts (comparison), Chart.js (comparison), TanStack (library family)

## [This Tool Runs Real AWS Services on Your Laptop For Free (Floci)](../videos/7s462S-qRY4.md)
`7s462S-qRY4` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: testing-verification

Better Stack walkthrough of Floci, a free open-source Docker emulator for AWS services (S3, DynamoDB, Lambda) pitched as a LocalStack alternative after LocalStack's free-tier change; the host re-measures the benchmark claims and runs an end-to-end thumbnail pipeline.

- Techniques: Swap LocalStack for Floci in an existing Compose setup; Run AWS CLI commands against the local emulator; Measure emulator startup and idle memory yourself; Test Lambda handlers against a real runtime container; Inspect state in the bundled web UI; Use the Testcontainers module for Lambda tests
- Tools: Floci, LocalStack, Docker, Docker Compose, AWS CLI, Amazon S3, Amazon DynamoDB, AWS Lambda, Lambda Python runtime image, Testcontainers

## [This Tool Finds the Perfect AI Model for Your Hardware (llmfit)](../videos/zf8jpD77sKY.md)
`zf8jpD77sKY` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: local-ai, inference-serving

Better Stack walks through llmfit, a terminal tool that detects your CPU, RAM and GPU, scores local models for fit and speed, and tests its estimates on machines from a 2012 Raspberry Pi to an RTX 5090.

- Techniques: Pre-download hardware fit check; Back-of-envelope decode speed check; Calibrate the tool against a real run; Use-case-weighted ranking
- Tools: llmfit (spoken as LLM Fit; no version stated), Hugging Face, DeepSeek R1, Qwen 3.6 12B (transcribed as Quen 3.6), Qwen 3.x models (transcribed as Quen 3.8 on the RTX 5090), Gemma 4 12B, Kimi K2.7 Flash variant (transcribed as Kimi K 2.7 D flash), Falcon H1 Mini, Llama 3 (mentioned, not tested), MLX, CUDA, Metal

## [Solid 2 is a MASSIVE Update (Goodbye SolidStart)](../videos/sr4q-Jj7uiM.md)
`sr4q-Jj7uiM` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: —

Walkthrough of Solid 2's breaking changes: async becomes part of the reactive graph, effects and JSX are reworked, a Rust compiler ships, and the Vite plugin's start mode makes Solid Start unnecessary.

- Techniques: Async data with an async memo and a Loading boundary; Optimistic mutation with action and createOptimisticStore; Split effect into compute and apply; Read a just-written signal with flush(); Index-style list rendering and count-based Repeat; Migrate with the official migration guide and a coding agent; Deploy a Solid 2 app via the Vite start mode
- Tools: Solid 2 (SolidJS), Solid 1 (SolidJS, comparison), Solid Start 2 / Solid Start, Vite plugin for Solid (the 'v plugin'; start mode), Oxc-based Rust compiler toolchain (auto-caption 'Box C'), React (comparison: Suspense, use), Svelte (comparison: await), Claude Code (anecdote: used the migration guide), Cloudflare Workers, Netlify, Nitro, Bun

## [Spotify Made an Agent Harness... I Don't Hate It](../videos/TK1LvtX-Bqs.md)
`TK1LvtX-Bqs` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: coding-agents, multi-agent

Walkthrough of Spotify's closed-source agent session manager "Zerp" (Claude Code, Codex, Gemini in one GUI). Useful session features, but the host finds nothing that justifies the account and closed-source tradeoff.

- Techniques: Dependent worktree chains for agent work; Forking a session to test alternatives; Mid-session agent handoff; Grid monitoring of parallel agents
- Tools: Zerp (Spotify internal agentic development environment; auto-captions transcribe it as Zurb), Claude Code, Codex, Gemini, Portal (Spotify product, related to Zerp), tmux, CMUX, Conductor, T3 Code, Matt Pocock's skills (referenced, not in the video)

## [This New Postgres Feature Is Crazy Powerful](../videos/_0A2BnRYVCo.md)
`_0A2BnRYVCo` · Better Stack · 2026-09-02 · q3 · practitioner · news · also: data-engineering

Better Stack walks through the headline features of the upcoming Postgres 19 (beta 2): atomic insert-or-select, SQL property graphs over existing tables, REPACK CONCURRENTLY, plan pinning, and smaller changes.

- Techniques: Atomic get-or-create with ON CONFLICT DO SELECT; Declare a property graph over existing tables; Path-style graph query with explicit columns; REPACK CONCURRENTLY to reclaim disk space on large tables; Pin a known-good query plan with pg_plan_advice; Parallel index vacuum (opt-in)
- Tools: PostgreSQL 19 (beta 2), pg_plan_advice (spoken as 'pg plan advice'), PG Repack / pg_repack (extension, referenced as a previous workaround), VACUUM FULL, Neo4j, pg_durable (spoken as 'pg durable', linked for further reading)

## [9 Open Source AI Tools That Will Kill Your Monthly Subscriptions](../videos/DOC9mbZOMW0.md)
`DOC9mbZOMW0` · Kai Explains · 2026-09-02 · q2 · intro · review · also: local-ai, token-cost-efficiency

Nine self-hostable open-source tools (Karakeep, Steno, Audio.cpp, Harper, Open Notebook, LibreChat, Open WebUI) pitched as replacements for about $150/month of AI subscriptions. Listicle, light on technical detail.

- Techniques: Multi-provider chat front end on one self-hosted UI; Self-hosted bookmark archive with local LLM tagging; On-device meeting transcription with live speaker labels; Editor-native local grammar checking
- Tools: Karakeep (formerly Hoarder), Pocket, Readwise Reader, Ollama, Meilisearch (transcribed as 'Mail-A-Search'), Steno, whisper.cpp, Whisper, Parakeet, llama.cpp, GGML, GGUF

## [This Linter Rejects AI Slop From Your Code](../videos/mmrSYvYKD9g.md)
`mmrSYvYKD9g` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: coding-agents, testing-verification, token-cost-efficiency

Better Stack demo of the anti-slop rule package for oxlint, which hard-fails low-evidence TypeScript/JavaScript patterns and whose error messages give coding agents a fix to apply.

- Techniques: Hand-picked lint gate for agent-written TS/JS; Agent self-repair loop on lint output; Validate untrusted input at the boundary instead of casting
- Tools: oxlint (Oxc; Rust-based JavaScript and TypeScript linter), anti-slop (rule package for oxlint; created the week before the video), Oxc (the toolchain that oxlint belongs to), Claude Code, CLAUDE.md, TypeScript, ESLint (comparison point only), Zod (suggested runtime validation)

## [This Open-Source Tool Fixes Browser History (Hister)](../videos/NMk9XVNTygA.md)
`NMk9XVNTygA` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: rag-retrieval, security-guardrails

Hister is a self-hosted tool that indexes the full rendered text of every page you read in Chrome or Firefox, so you can search your browsing by content; useful, but pre-1.0 with real security gaps.

- Techniques: Local recall index for your own reading; Scoped full-text queries; Backfilling from existing browser history; Hardening before exposure; Agent access to a personal reading index
- Tools: Hister, Chrome extension for Hister, Firefox extension for Hister, Docker (multi-arch image), Nix flake (Darwin module), MCP, Karakeep (transcribed as 'Para Keep', 28k stars), ArchiveBox, Wallabag, Readwise Reader, Gatekeeper (macOS)

## [4 Billion Free LLM Tokens… One API (FreeLLMAPI)](../videos/sHOwbyMbun0.md)
`sHOwbyMbun0` · Better Stack · 2026-09-02 · q3 · intro · review · also: token-cost-efficiency, infra-cost-scaling

Better Stack walkthrough of FreeLLM API, a self-hosted gateway that pools free LLM tiers from about 28 providers behind one OpenAI-compatible endpoint with failover. Useful for cheap prototyping; the speaker warns free-tier quality and availability drift.

- Techniques: Single OpenAI-compatible endpoint over pooled free tiers; Choose a routing strategy in the dashboard; Smoke-test in the Playground before wiring tools; Check monthly token usage per model before long runs; Reserve the pool for latency-tolerant work
- Tools: FreeLLM API (Free LLM API), Docker, Docker Compose, Git, OpenAI-compatible client SDK, OpenRouter, LiteLLM, Grok (xAI), Cerebras, Google models, Mistral, NVIDIA (free models mentioned as 'open route')

## [I replaced my entire tech stack with Postgres](../videos/MZfhhl6ej-k.md)
`MZfhhl6ej-k` · Better Stack · 2026-09-02 · q3 · intro · tutorial · also: rag-retrieval, infra-cost-scaling

Better Stack walks through replacing separate cache, vector DB, search, geo, cron and document-store services with Postgres features, framed for small apps rather than scale.

- Techniques: Postgres as a cache using UNLOGGED tables; pgvector for embeddings and similarity search; Full-text search with a generated tsvector column and a GIN index; Geospatial radius and polygon queries with PostGIS; Scheduled SQL with pg_cron; Document storage with JSONB, a GIN index and containment queries
- Tools: PostgreSQL, pgvector, PostGIS, pg_cron, JSONB, DocumentDB, Redis, Memcached, Pinecone, Qdrant, Elasticsearch, MongoDB

## [I Tested a File Transfer Tool With No Network At All (decimen)](../videos/MnS0TvxLzaU.md)
`MnS0TvxLzaU` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: —

Better Stack tests Deciman, a fountain-coded QR file transfer tool that needs no network; its defaults work phone-to-phone but fail laptop-to-phone until bytes per frame and fps are retuned.

- Techniques: Fountain-coded one-way transfer over a screen and camera; Tune bytes per frame and fps to the capture setup; Diagnose with capture fps versus decode fps; Check the camera's real frame rate and resolution budget before tuning
- Tools: Deciman (optical file transfer tool by Evan Crawley; the title spells it 'decimen'), QR codes (version 40 = 177x177 modules, 2953 bytes per frame), fountain coding (concept), main.ts (Deciman source file, sender/receiver logic), iOS camera capture

## [The Python YouTuber Who Never Missed an Upload in 7 Years | Better Stack Podcast Ep. 19](../videos/90t4HgAFqZU.md)
`90t4HgAFqZU` · Better Stack · 2026-09-02 · q2 · intro · interview · also: coding-agents, claude-code, models-research

Better Stack podcast with Florian of Neural9 on growing a 500k-subscriber Python channel, daily Claude Code use, the agentic-engineering vs vibe-coding line, and open-weight model claims. Mostly career anecdote, thin on technique.

- Techniques: Minimal, concise CLAUDE.md for Claude Code; Work on a second project while a long agent run finishes; Hand-written proof of concept, then agent implementation; Tiered review: line-by-line for backend, skim for frontend; Learn a new technology by building first; Continue a Claude Code session from a phone; Use uv for all Python package installs
- Tools: Claude Code, Claude Opus 4.8 (as named by speaker), Fable (model, as named by speaker), GLM 5.2 Max (model, as named by speaker), Kimi K3 (model, as named by speaker), LiteRT (Google, formerly TensorFlow Lite), LiteRT.js, TensorFlow, PyTorch, JAX, uv, pip

## [Bun 1.4 Just Deleted 15 of Your Dependencies](../videos/IcoB5AZ6TJ0.md)
`IcoB5AZ6TJ0` · Better Stack · 2026-09-02 · q3 · practitioner · review · also: —

Walkthrough of Bun 1.4 (the Rust rewrite) and its built-in standard library: headless browser, image processing, markdown, pseudo-terminal, cron, parallel scripts and tar archives, each replacing an npm package.

- Techniques: Replace Playwright/Puppeteer for light scraping with BunWebView; Render markdown with Bun.markdown and sanitize it yourself; Spawn a subprocess with a pseudo-terminal using bun.spawn; Choose in-process cron or OS-level cron with bun.cron; Run package.json scripts in parallel or sequence with bun run; Create, compress and partially read tar archives with Bun.Archive; Enable the isolated linker with the global virtual store
- Tools: Bun 1.4, BunWebView (Bun.WebView), Bun.Image, Bun.markdown, Bun.Terminal, bun.spawn, bun.cron, bun run --parallel / --sequential, Bun.Archive, Bun.serve (static files), Bun JSON5 and XML support, Bun.sliceAnsi / Bun.wrapAnsi / Bun.stringWidth

## [Github's Biggest Release In Years. Stacked PRs.](../videos/3Z1xcfF2xlY.md)
`3Z1xcfF2xlY` · Better Stack · 2026-09-02 · q3 · intro · tutorial · also: pr-code-review, coding-agents

Better Stack walks through GitHub's stacked PRs: splitting a large change into a chain of dependent PRs, managing the chain with the gh CLI, and merging the whole stack at once.

- Techniques: Stacked PR workflow with gh stack; Manual stacking without the CLI; Layer the stack by dependency
- Tools: GitHub (stacked pull requests, Merge stack, stack UI), GitHub CLI (gh), with gh stack init / add / submit subcommands, git

## [fighting slop with slop — Vaibhav Gupta, Boundary](../videos/AMiyLItEtLA.md)
`AMiyLItEtLA` · AI Engineer · 2026-08-18 · q3 · practitioner · talk · also: software-factory, context-engineering, testing-verification

Vaibhav Gupta of Boundary argues that teams without code review can keep AI-written code stable by building internal tools that enforce invariants, mine agent transcripts, and rethink the language and tooling layers underneath.

- Techniques: Invariant-only architecture file; CLI guard checks for architecture invariants; Required reading as the gate for design docs; Transcript triage loop; A/B test skills or features by agent outcomes; Per-function CLI and describe tool
- Tools: BAML, Claude, Codex, TypeScript, Python, Rust, Go, Ruby, Java, WASM, ripgrep, Notion

## [This Free Go Alternative to Firebase is Just One File](../videos/WZoC1HA1vec.md)
`WZoC1HA1vec` · Better Stack · 2026-08-02 · q3 · intro · review · also: infra-cost-scaling

Walkthrough of PocketBase, a single Go binary with embedded SQLite giving realtime DB, auth and file storage, tested on a React bug tracker, with a VPS deployment and pre-v1 caveats.

- Techniques: Singleton SDK client module; Auth state from the auth store; Load-then-subscribe for live lists; Multipart create with a file attachment; Collection API rules for access control; Hooks for server-side side effects; Single-VPS deployment with persistent data
- Tools: PocketBase, SQLite, Go, JavaScript, TypeScript, React, Supabase, Firebase, Render, Railway, OpenCode, Claude Code

## [Microsoft Built a New Charting Language for AI Agents](../videos/xFWhiWe91BE.md)
`xFWhiWe91BE` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: mcp-and-tools, data-engineering

Better Stack walks through Microsoft Research's Flint, a local MCP chart tool where the LLM writes about 10 lines of semantic JSON and a deterministic compiler emits Vega-Lite, ECharts or Chart.js specs; a research preview with no benchmarks yet.

- Techniques: Semantic spec plus deterministic compiler; Change the meaning, not the geometry; Local MCP chart rendering; Validate the IR, not the generated code
- Tools: Flint (Microsoft Research chart language and MCP server, v0.28), Vega-Lite, ECharts, Chart.js, Mermaid, Data Formulator (Microsoft analytics tool that uses Flint), Claude (Claude Code MCP client), Node 18 / TypeScript, npm

## [WebAssembly 3.0: It's Not Just for Browsers Anymore](../videos/McB108-FExg.md)
`McB108-FExg` · Kai Explains · 2026-08-02 · q3 · intro · news · also: sandboxing-execution, infra-cost-scaling

Kai Explains argues WebAssembly 3.0 (component model plus WASI) makes Wasm a cross-language, server and edge runtime, while JavaScript keeps the DOM and is not being replaced.

- Techniques: Polyglot components via the component model; Wasm instead of containers for short-lived edge or per-request execution; Split UI from logic across the JS/Wasm boundary
- Tools: WebAssembly 3.0, Wasm component model, WASI, Spin framework, Cloudflare Workers, Fastly Compute, Docker, Chrome DevTools, npm, React, Figma, Photoshop

## [TypeScript 7 Officially Released And Boy Is It Fast](../videos/kl42N7pI7lM.md)
`kl42N7pI7lM` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: —

Better Stack walks through why TypeScript 7 (the Go port of the compiler) is much faster, with build and type-check benchmarks on a VS Code checkout and an M3 Max.

- Techniques: Benchmark tsc across versions on your own repo; Raise the type-checker count to use more cores; Install the TypeScript 7 VS Code extension for editor use; Wait on tooling that uses the compiler API
- Tools: TypeScript 7 (tsc, Go-based compiler), TypeScript 6 (baseline), Go, VS Code, TypeScript 7 VS Code extension, typescript-eslint, ts-jest, Node.js, Playwright, Bluesky codebase (benchmark repo), Apple M3 Max (test machine)

## [DuckDB is becoming unstoppable...](../videos/dKbV8MEzVPA.md)
`dKbV8MEzVPA` · Better Stack · 2026-08-02 · q3 · intro · review · also: data-engineering

A six-minute Better Stack walkthrough of DuckDB 1.4 and 1.5, separating their features, showing in-place Parquet queries, and stating where the single-machine analytics engine should not be used.

- Techniques: Query files in place from the DuckDB CLI; Single-statement upserts with MERGE INTO (DuckDB 1.4+); VARIANT column for messy semi-structured data (DuckDB 1.5+); Page-level AES-256 encryption with your own key
- Tools: DuckDB 1.4, DuckDB 1.5, SQLite, Pandas, Snowflake, Google BigQuery, Apache Parquet, Apache Iceberg, Apache Spark, Postgres, CSV, JSON

## [Tauri vs Electrobun vs Deno Desktop: One Clear Winner](../videos/ktkDGQyRx3Y.md)
`ktkDGQyRx3Y` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: —

Better Stack builds the same screen-recorder app in Tauri, Electrobun, Deno Desktop and Electron and measures size, startup, memory and developer experience; Tauri wins on size and recording, Electron is the mature TypeScript option.

- Techniques: Measure startup as a median over repeated launches; Sum all related processes when measuring memory; Keep screen capture in the native backend; Keep a Deno Desktop app alive with no visible windows
- Tools: Tauri, Electrobun, Deno Desktop, Electron, Bun, Chromium, FFmpeg, ScreenCaptureKit, Rust, TypeScript, Three.js, Babylon.js

## [This component library is mind-blowing (Canvas UI)](../videos/JZf_m_BVDaQ.md)
`JZf_m_BVDaQ` · Better Stack · 2026-08-02 · q3 · intro · review · also: vibe-coding-app-building, voice-multimodal

Better Stack walkthrough of Canvas UI, an open-source, shadcn-installable library of 33 WebGL and HTML-in-Canvas effects, plus using those effects on code-generated video through HyperFrames.

- Techniques: Install a Canvas UI component with the shadcn CLI; Progressive enhancement for HTML-in-Canvas effects; Test HTML-in-Canvas in Chrome with the feature flag; Apply shader-style effects to generated video with an agent; Match effects to the UX intent
- Tools: Canvas UI, shadcn (CLI), Three.js, HTML-in-Canvas (WICG proposal, browser API), drawElementImage, TextElementImage2D (WebGL), CopyElementImageToTexture (WebGPU), Chrome (feature flag), Firefox, Claude, HyperFrames, Remotion

## [Git Can’t Handle Games… So Epic Built Lore](../videos/i66Bsnv12ZA.md)
`i66Bsnv12ZA` · Better Stack · 2026-08-02 · q3 · intro · review · also: data-engineering

Epic Games' Lore, a Rust, MIT-licensed, centralized-but-local-first version control system for large binary game assets; a walkthrough of its demo plus an honest take that it is pre-1.0 and benchmarks are unverified.

- Techniques: Run a local Lore demo server; Basic Lore workflow
- Tools: Lore (Epic Games, Rust, MIT license, pre-1.0), Git, Git LFS, Perforce, ZStandard, dd, Fortnite (mentioned as Epic's game)

## [Is MOJO actually better than NVIDIA's CUDA?](../videos/KL7pMJ2nkAk.md)
`KL7pMJ2nkAk` · Kai Explains · 2026-08-02 · q3 · intro · review · also: inference-serving, models-research

Analysis of Qualcomm's $3.9B all-stock acquisition of Modular and whether the Mojo language can dent NVIDIA's CUDA moat; the verdict is that Mojo is not faster than CUDA today but wins on portability.

- Techniques: Benchmark vendor speedup claims against an optimized baseline; Score hardware-software stacks on separate axes; Assess neutrality risk after an acquisition
- Tools: Mojo, Modular MAX, CUDA, NumPy, LLVM, Clang, Swift, MLIR, TensorFlow Lite, XLA, ROCm, Triton

## [Granola, But Open Source and Local (Meetily)](../videos/LCoF8dCVkIw.md)
`LCoF8dCVkIw` · Better Stack · 2026-08-02 · q3 · intro · review · also: local-ai

Short walkthrough of Meetily, an open-source, local-first meeting transcriber that captures system audio without joining calls. Speech-to-text runs on-device; summaries can use a local model or a cloud API key.

- Techniques: Bot-free system-audio capture; Split local-audio / optional-cloud-summary pipeline; Setup on a Mac (Apple Silicon); Offline-verification test
- Tools: Meetily, Granola, Otter, Fireflies, OpenAI Whisper, NVIDIA Parakeet, Ollama (likely; transcript says 'llama'/'Alamo'), Claude (cloud API key), Grok (cloud API key), Zoom, Google Meet, Microsoft Teams

## [Homebrew 6.0 Just Changed How Your Mac Installs Software](../videos/IwzVzvDw68w.md)
`IwzVzvDw68w` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: security-guardrails

Walkthrough of Homebrew 6.0, a security-focused release: third-party taps must be explicitly trusted, installs show a plan and wait for approval, and CI that relies on silent installs or untrusted taps will break.

- Techniques: Explicitly trust third-party taps; Review the install plan before approving; Run a tool once with brew execute; Scan installed packages with brew vulns; Pre-upgrade CI audit
- Tools: Homebrew 6.0, brew trust, brew execute, brew vulns, brew doctor, brew update, GitHub Actions, Ruby, npx (named as the comparison for brew execute; transcript reads 'MPX'), Nix (named as a comparison; transcript reads 'Nyx')

## [Postgres Just Got It's Biggest Upgrade In Years](../videos/4Lmqvn_yz-c.md)
`4Lmqvn_yz-c` · Better Stack · 2026-08-02 · q3 · intro · tutorial · also: agent-architecture

Better Stack walkthrough of PG Durable, a Microsoft open-source Postgres extension for crash-proof durable functions, scheduling, retries and human-in-the-loop approval in plain SQL.

- Techniques: Run a recurring job inside Postgres; Park a workflow until a human approves; Fan out and fan in; Local dev via Docker Compose
- Tools: PG Durable (pgdurable, Postgres extension, Microsoft, open source), PostgreSQL 17, Docker Compose, npm (demo scripts)

## [No API Key. No Cloud. Just Mac AI (Apfel)](../videos/wiQo9gayiqU.md)
`wiQo9gayiqU` · Better Stack · 2026-08-02 · q3 · intro · review · also: local-ai, token-cost-efficiency

Better Stack demos Apfel, an MIT-licensed macOS CLI that exposes Apple's built-in ~3B on-device model through a terminal prompt, shell workflows and an OpenAI-compatible localhost server, and is candid about its limits.

- Techniques: Install and one-shot streaming prompt; Generate code straight into a file; Feed an existing file for feedback; Drop-in OpenAI SDK replacement for local dev; Tiered routing for cheap tasks
- Tools: Apfel (transcribed as Appful; MIT-licensed CLI and local server), Apple Foundation Models framework, Apple Intelligence (on-device ~3B model), Homebrew (brew), OpenAI SDK (Python, used unchanged), Ollama (transcribed as Olama; comparison only), MLX (comparison only), Llama and Qwen (open-weight models named in comparison)

## [An Ex-Bun Dev Just Built The Anti-Bun (Nub)](../videos/6YRpXxbtc2c.md)
`6YRpXxbtc2c` · Better Stack · 2026-08-02 · q3 · intro · review · also: —

Better Stack's hands-on review of Nub, a single Rust binary on top of stock Node.js that bundles a TypeScript runner, Node version manager and pnpm-compatible package manager; the speed claims hold up only partly in the host's own tests.

- Techniques: Run TypeScript files directly with nub instead of tsx or ts-node; Let the env loader handle .env files; Pin the Node version in a version file; Adopt an existing lockfile in place; Run package binaries with nubx instead of npx or pnpm exec; Use nub run for scripts with lifecycle hooks; Harden installs with defaults nub ships with
- Tools: Nub, Node.js (Node 26, Node 24 shown), Bun, pnpm, npm, Yarn, TSX, ts-node, nvm, fnm, mise (transcribed as 'Mies'), OBE (package manager library by JDX; name garbled in captions)

## [The Largest Supply Chain Attack Ever Just Infected Go](../videos/lNsSxWQDqaU.md)
`lNsSxWQDqaU` · Better Stack · 2026-08-02 · q3 · practitioner · news · also: security-guardrails, claude-code, coding-agents

Better Stack explains how the self-replicating npm worm (Shai-Hulud) jumped to a Go module, hiding hooks in Claude Code and VS Code config so code runs on folder open, and lists five hardening steps.

- Techniques: Audit agent and editor config before opening untrusted code; Turn off VS Code automatic tasks; Treat .claude/ and .vscode/ as executable code in review; Short-lived, least-privilege CI credentials via OIDC; Egress filtering on CI runners; Minimum release age for packages; Keep secrets out of plaintext on dev machines
- Tools: npm, Go modules, Claude Code (called 'clawed code' in the auto-captions), VS Code (tasks.json, folder-open tasks), Bun (runtime the payload uses to stage its code), Node.js (runs the setup script), TruffleHog (secret scanner the worm reuses), GitHub Actions (CI workflows named as the risk surface), Socket.dev (security firm that flagged the wave), CrowdStrike, Microsoft Defender, SentinelOne (endpoint products the malware checks for), OIDC (short-lived CI credentials), .npmrc (minimum release age setting)

## [Meta Just Open Sourced 8 Years of Ul Components (Astryx)](../videos/4GaR7k9VMp4.md)
`4GaR7k9VMp4` · Better Stack · 2026-08-02 · q2 · intro · review · also: context-engineering, vibe-coding-app-building

Walkthrough of Meta's open-source Astryx React component library (built on StyleX): theming via tokens, component-level overrides, Tailwind bridge, and an AI-oriented CLI.

- Techniques: Theme from one brand color plus scale settings; Override a token per light/dark mode; Component-scoped override by variant; Custom component variant; One-off style override with xstyle; Tailwind bridge; Feed component docs to agents with the Astryx CLI
- Tools: Astryx (Meta component library; transcribed as 'Asterix'), StyleX (styling library Astryx is built on; transcribed as 'Starlex'), React, shadcn/ui (transcribed as 'ShadCN'), Tailwind CSS, Material UI, Panda CSS (transcribed as 'panda'), Next.js, Inter (transcribed as 'into'), AGENTS.md, TypeScript

## [Google Just Made TensorFlow.js Obsolete (LiteRT.js)](../videos/8c68vFpT9Tk.md)
`8c68vFpT9Tk` · Better Stack · 2026-08-02 · q3 · intro · review · also: local-ai, inference-serving

Better Stack walks through LiteRT.js, Google's WebAssembly on-device inference runtime for browsers, and builds a client-side webcam pose-capture app to test its CPU and WebGPU speed against TensorFlow.js.

- Techniques: Select a backend per device tier; A/B the backends on your own hardware before trusting vendor numbers; Port existing models instead of rewriting them; Client-side webcam pose pipeline; Export pose recordings for retargeting
- Tools: LiteRT.js, LiteRT, TensorFlow.js, WebAssembly, XNNPack, ML Drift, WebGPU, WebNN, LiteRT Torch, AI Edge Quantizer, LiteRT-LM.js (announced, not shipped), BlazePose

## [OpenCV 5 Is Here - The Biggest Update Since 2018 (We Tested It)](../videos/piHpZWcgQyc.md)
`piHpZWcgQyc` · Better Stack · 2026-08-02 · q3 · intro · review · also: local-ai, inference-serving

Better Stack tests OpenCV 5's rewritten CPU-only DNN engine (ONNX operator coverage 22% to 80%) on colorization, detection, diffusion inpainting and VLM captioning; only detection looks practical.

- Techniques: Choose the DNN engine by backend need; Benchmark a vendor speed claim on your own model before switching; Tune diffusion inpainting steps to trade artifacts for latency
- Tools: OpenCV 5, OpenCV 4 (classic DNN engine), ONNX Runtime, PyTorch, YOLOv8, OWLv2, PaliGemma, Gemma 4 (12B, run locally), CUDA, OpenVINO, C++17

## [Postgres was rewritten in Rust… and somehow passed every test](../videos/WvfacC0FtbE.md)
`WvfacC0FtbE` · Better Stack · 2026-08-02 · q3 · intro · review · also: coding-agents

Better Stack reviews PG Rust, a from-scratch Rust reimplementation of Postgres that passes the official regression suite but is not production ready, with its headline performance claims unverified.

- Techniques: Use an upstream regression suite as the compatibility oracle; Smoke-test compatibility with unmodified clients; Check on-disk compatibility by booting an existing data directory; Triage performance claims by asking for the code or benchmark
- Tools: PG Rust (Postgres 18.3 compatible target), PostgreSQL, Docker, psql, Bun (mentioned as another Rust rewrite), CockroachDB, YugaByte, GitHub, Hacker News

## [The Best File Transfer Tool You've Never Heard Of (croc)](../videos/o_psX5meBo8.md)
`o_psX5meBo8` · Better Stack · 2026-08-02 · q3 · intro · review · also: security-guardrails

Better Stack walkthrough of croc, an open-source Go CLI for sending files peer-to-peer through a relay, with PAKE code phrases and resumable transfers; a tool intro with a self-hosted relay option.

- Techniques: Send a file with a one-time code phrase; Resume an interrupted transfer; Self-host the relay for corporate use
- Tools: croc (open-source Go CLI, by Zach Scholl), Docker (croc relay image), WeTransfer, Dropbox, AirDrop, SCP, SSH, FTP, Discord

## [Mojo is Quietly Replacing Python in AI](../videos/zuDmoLI1dZc.md)
`zuDmoLI1dZc` · Kai Explains · 2026-08-02 · q2 · practitioner · news · also: inference-serving, models-research

Kai Explains argues Qualcomm's reported $3.9B Modular deal makes Mojo a threat to the Python-plus-CUDA ML stack, while flagging vendor-only benchmarks, a closed compiler and missing MoE support.

- Techniques: Triage performance claims by evidence type; Check model-architecture coverage before reading benchmarks; Incremental migration via Python interop
- Tools: Mojo (1.0 Beta 1, shipped May 7 per 4:03; the intro says about three weeks before June 24), Modular Platform 26.2, Modular (company, acquired by Qualcomm per the video), MLIR (captioned as MLR), LLVM / LLVM IR, Clang, Swift, CUDA, CPython, PyTorch, NumPy, Python

## [Harper: The Free, Private Grammarly Alternative Built in Rust](../videos/lU_jse27kWA.md)
`lU_jse27kWA` · Better Stack · 2026-08-02 · q3 · intro · review · also: —

Better Stack demos Harper, a free, offline, rule-based grammar checker written in Rust that runs in editors and covers comments, commits and docs. The main takeaway is predictable, private, instant checks in exchange for narrower coverage than ML tools.

- Techniques: Editor-integrated deterministic prose linting; Verify the privacy claim offline; Calibrate coverage with probe sentences; Split the work: rules for correctness, ML for rewrites
- Tools: Harper, Grammarly, LanguageTool, Homebrew, VS Code, Obsidian, Neovim, Zed, Helix, Emacs, writewithharper.com, Rust

## [PewDiePie is a software engineer now...](../videos/gQUQZxrM5Ts.md)
`gQUQZxrM5Ts` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: local-ai, security-guardrails

Walkthrough of Odysseus, a viral self-hosted AI workspace with a local model cookbook, deep research and cross-session memory. The host calls it a fun local playground but not a production dependency, citing code quality and an agent threat model that needs a locked-down host.

- Techniques: Setup on macOS via Docker script; Hardware-aware local model selection; Blinded side-by-side model comparison; Zero-API local deep research loop; Persistent memory via vector store; Keep Mac GPU inference outside Docker
- Tools: Odysseus, Docker, llama.cpp (transcript: 'Llama CPP'), Metal, SearXNG (transcript: 'Sear XNG'), ChromaDB, FastAPI (transcript: 'fast API'), ntfy (transcript: 'Nifty', for push notifications), IMAP, OpenCode, LLM Fit, Alibaba Deep Research

## [HTMX Explained: The "Dumb" HTML Secret Replacing React](../videos/HPAh1uiE2z0.md)
`HPAh1uiE2z0` · Kai Explains · 2026-08-02 · q3 · intro · review · also: —

Kai Explains argues HTMX lets plain HTML talk to the server and swap returned HTML fragments, replacing most React-style SPA plumbing, and is honest that SPAs still win for highly interactive apps.

- Techniques: Fragment-swap request on any element; Live search without an API; Delete as a real HTTP DELETE with empty response; Out-of-band swap for multi-region updates; Progressive enhancement with boost; Loading indicator as one attribute; Small sprinkle library for client-only behavior
- Tools: HTMX, React, React DOM, Alpine.js, Hyperscript, Google Sheets (example of a spreadsheet-style app)

## [Mojo + Vulkan is INSANE: Run Local AI on ANY GPU (Goodbye CUDA)](../videos/CbNrKGMDM7g.md)
`CbNrKGMDM7g` · Kai Explains · 2026-08-02 · q3 · practitioner · review · also: local-ai, inference-serving

Kai Explains argues Vulkan (llama.cpp) and Mojo are weakening the CUDA lock-in, so local AI runs on AMD, Intel, Apple and iGPU hardware, with CUDA still fastest at the top end.

- Techniques: Run local models on a non-NVIDIA GPU via llama.cpp Vulkan backend; Benchmark Vulkan against the vendor stack on the same hardware; Write a GPU kernel once in Mojo and compile per vendor; Compare a rewritten kernel to a vendor-tuned kernel on the same chip
- Tools: CUDA, Vulkan, llama.cpp, ROCm, Metal, SYCL, MoltenVK, Mojo, Modular, PyTorch, TensorFlow, JAX

## [Open-Source Dictation Is Here… Goodbye Subscriptions](../videos/mIL4sZa8M0E.md)
`mIL4sZa8M0E` · Better Stack · 2026-08-02 · q2 · intro · review · also: local-ai

Better Stack demos Fluid Voice, a free open-source Mac dictation app that runs speech-to-text and LLM cleanup fully on-device. Its main pitch is no subscription and no cloud; it is Mac-only and needs a ~3.5 GB model.

- Techniques: Local two-stage dictation with LLM cleanup; Install and permission setup for macOS dictation tools
- Tools: Fluid Voice, Parakeet, Fluid Intelligence, Wispr Flow, SuperWhisper, Cursor, Claude, Slack, Homebrew (brew install mentioned, command not spoken)

## [Wails: Golang's Bet On Desktop Grade Apps To Beat Electron](../videos/Q1TL2AKoy00.md)
`Q1TL2AKoy00` · Better Stack · 2026-08-02 · q3 · practitioner · review · also: —

Better Stack builds the same screen recorder in Wails (Go), Tauri and Electron and compares bundle size, startup, capture performance and developer experience. Wails wins on size, Electron on startup, and Tauri on ecosystem.

- Techniques: Wails app layout and entry config; Calling Go from the frontend through generated bindings; Dev-loop check for Go/TS contract drift; Native macOS screen capture from Go via cgo; Startup benchmark method
- Tools: Wails, Go, Tauri (called Torii in the captions), Electron, React, TypeScript, Rust, ScreenCaptureKit (transcript says CaptureKit), cgo, Objective-C

## [Burp Suite Costs $499/year… This Tool Is Free (Yakit)](../videos/4XSx19ul-MU.md)
`4XSx19ul-MU` · Better Stack · 2026-08-02 · q3 · intro · review · also: —

Walkthrough of Yakit, a free, Chinese-first offensive security platform (Yaklang scripting) positioned as a Burp Suite alternative, with its proxy-to-fuzzer debugging loop and its drawbacks.

- Techniques: Capture, pause, edit, forward to localise a bug; Replay captured requests in a fuzzer with systematic mutations; Automate repeated security test steps with scripts
- Tools: Yakit, Yaklang, Burp Suite (Community and Pro), Burp Intruder, Burp Repeater, OWASP ZAP (transcribed as "Zap")

## [The Guy Who Coined "Event Gateways" Explains Why Webhooks Are Dying | Better Stack Podcast Ep. 17](../videos/ElaEGr2t9XQ.md)
`ElaEGr2t9XQ` · Better Stack · 2026-08-02 · q3 · practitioner · interview · also: infra-cost-scaling, agent-architecture, product-ux

Hookdeck's founder explains why he built an event gateway and the open-source Outpost to replace fragile webhook handling with queuing, replay, push-based rate control and per-vendor latency monitoring. Substantive but vendor-led.

- Techniques: Push-based webhook intake in front of your endpoint; Respond fast, queue the work; Per-vendor delivery latency baseline and alerting; Per-tenant queues with a shared push consumer; Event destinations instead of HTTP webhook transport; Open-source-first with a managed twin; Verify agent-written contributions against real APIs
- Tools: Hookdeck (Event Gateway), Outpost (Apache 2.0, open source), Hookdeck Radar, Kafka, RabbitMQ, Amazon SQS, Google Cloud Pub/Sub, AWS EventBridge, Azure Event Grid, Kong event gateway, Cloudflare Queues, BullMQ

## [I Haven't Typed in a Week (Thanks to This App)](../videos/ZRsDQp9CrXc.md)
`ZRsDQp9CrXc` · Better Stack · 2026-08-02 · q3 · intro · review · also: local-ai, voice-multimodal

Better Stack host tours Handy, an open-source, MIT-licensed, fully offline dictation app with user-chosen models, and compares its output against Google Docs voice typing and Wispr Flow on one passage.

- Techniques: Handy push-to-talk or toggle dictation setup; Choosing a model by speed/accuracy trade-off; Adding a custom fine-tuned Whisper model; Side-by-side dictation accuracy check
- Tools: Handy (open-source offline dictation app, MIT, built by CJ Pace), Tauri (transcribed as "talk"; the Rust-plus-web-UI shell is implied by the description), React, TypeScript, Transcribe CPP (runtime for Whisper-family GGML/GGUF models), transcribe-rs (runs Parakeet), Parakeet Unified 0.6B (CPU-only speech model), Whisper (GGML models, including custom fine-tunes), Silero VAD (transcribed as "Cilero VAD"), cpal (cross-platform audio input), rdev (global keyboard shortcuts), rubato (real-time resampling)

## [MAX + Mojo Are Quietly Replacing Python in AI](../videos/fOj8TgAdDGE.md)
`fOj8TgAdDGE` · Kai Explains · 2026-08-02 · q3 · intro · news · also: inference-serving

Kai Explains argues Mojo, Modular's Python-syntax compiled language, could remove the research-to-kernel handoff, with the Qualcomm acquisition as context and caveats on MoE support and vendor benchmarks.

- Techniques: Check architecture coverage before trusting a portable-kernel benchmark; Separate vendor claims from independent evidence
- Tools: Mojo (1.0 Beta 1), Modular Platform (26.2), MAX (named in the video title), MLIR (captioned as MLR), LLVM, Clang, Swift, CUDA, PyTorch, NumPy, CPython, llama.cpp

## [Deno Desktop Can Make Your Apps 70% Smaller](../videos/BZ5JuEK4_Xc.md)
`BZ5JuEK4_Xc` · Better Stack · 2026-08-02 · q3 · intro · review · also: —

Better Stack walks through Deno 2.9's new `deno desktop` command for building TypeScript desktop apps, comparing it to Electron: a 70 MB binary versus 248 MB, similar startup, with a caveat that the test apps are tiny.

- Techniques: Build a desktop app from one TypeScript file; Call backend code from the web view with `bind`; Choose the renderer per build; Package for one or several platforms with flags or dino.json; Keep the default dependency age guard
- Tools: Deno 2.9, deno desktop, Dino (global runtime object), Electron, Chromium, CEF (Chromium Embedded Framework), WebView2, WebKit, Next.js, Remix, dino.json, npm

## [Is This WordPress's Worst Hack In History?](../videos/38z2hdzV_DM.md)
`38z2hdzV_DM` · Better Stack · 2026-08-02 · q3 · intro · news · also: security-guardrails

Better Stack walks through a WordPress REST API batch-endpoint bug (6.9.x and 7.0.x) that chains a validation desync into unauthenticated SQL injection, admin account creation and a malicious plugin upload.

- Techniques: Check batch endpoint nested requests against the same allow-list; Escape or parameterize values reaching SQL on internal dispatch paths; Patch and check your WordPress version
- Tools: WordPress, WordPress REST API (batch/v1, wp/v2 posts, wp/v2 users), A public proof-of-concept repo (the video does not name it; the link is in the description)

## [A Song of Types and Agents - Roberto Stagi, Ratel](../videos/UlFB6efYN5Q.md)
`UlFB6efYN5Q` · AI Engineer · 2026-07-18 · q2 · intro · talk · also: agent-architecture, coding-agents

Roberto Stagi argues TypeScript is overtaking Python for the agent and application layer, because coding agents default to it, npm is deep, and one Zod schema can type the whole stack; Python keeps training and serving.

- Techniques: Shared Zod schema across the full stack; Single-language monorepo for agent apps; Split by layer: Python for training and serving, TypeScript for the app and agent layer
- Tools: TypeScript, Python, Zod, npm, Vercel AI SDK, FastAPI, React, Claude Code, Cursor, Codex, Lovable

## [remobi.app: Don't change your terminal workflow for mobile](../videos/5192csoTkVo.md)
`5192csoTkVo` · AI Engineer · 2026-07-18 · q2 · intro · demo · also: coding-agents, product-ux

Connor Adams demos Remobi, an open-source progressive web app that gives phone access to tmux sessions running Claude Code and other coding agents, reached over a private network such as Tailscale.

- Techniques: tmux as the agent session host; Private-network remote access to a dev box; Gesture-mapped terminal UI; Diff review in a side window; Skill-driven environment setup
- Tools: Remobi, tmux, Tailscale, Cloudflare Tunnels, ngrok, Claude Code, Happy, lazygit, critique, agent-browser, npm, Conductor

## [Big Tech Is Buying Up Open Source... Vite Is Next](../videos/wxKRGs7FS6s.md)
`wxKRGs7FS6s` · Better Stack · 2026-07-02 · q2 · intro · news · also: infra-cost-scaling

Better Stack's take on Cloudflare buying VoidZero (Vite, Vitest, Rolldown, Oxc): what the deal promises, why it happened, and the consolidation risk for open source.

- Techniques: Vet a dependency after a vendor acquisition
- Tools: Vite, Vitest (called 'Vite for Test' in the captions), Rolldown, Oxc, Vite+ ('Vite Plus' in the captions), Vue, Void (VoidZero deployment platform), Cloudflare Vite plugin, Cloudflare CLI (cfdev, cfdeploy, announced), Astro, Bun, uv

## [Why I Quit My Dev Job Before AI Could Take It | Better Stack Podcast Ep. 16](../videos/VuMf2ZVA0RE.md)
`VuMf2ZVA0RE` · Better Stack · 2026-07-02 · q3 · practitioner · interview · also: coding-agents, claude-code, context-engineering

Better Stack podcast with Dreams of Code's Elliot on leaving dev work, betting on Rust, and practical AI-coding habits: stub-first interfaces, git-staged checkpoints, human-steered architecture.

- Techniques: Stub-first public interface; Hand-built spike before delegating; Git staging as manual checkpoints; Architecture-owner, typing-delegate split; Codec backend abstraction
- Tools: Claude Code, Codex CLI, Cursor, OpenCode, Bun, Zig 0.16, Rust, GPUI, gpui-component, Iced, egui, Tauri

## [I Turned Cheap Cloud Storage Into a 1PB Local Drive (With JuiceFS)](../videos/ZoBEQWxosGg.md)
`ZoBEQWxosGg` · Better Stack · 2026-07-02 · q3 · intro · tutorial · also: infra-cost-scaling, observability

Walkthrough of JuiceFS, a POSIX file system that stores data in cheap S3-style object storage with metadata in Redis and a local SSD cache, plus wiring its Prometheus metrics into Better Stack.

- Techniques: JuiceFS volume with Redis metadata and S3 data; Cold vs warm read benchmark with dd; Scraping JuiceFS metrics into a hosted dashboard
- Tools: JuiceFS, Redis, PostgreSQL, TiKV, Amazon S3, Google Cloud Storage, Backblaze B2, Docker, macFUSE, dd, ngrok, Prometheus

## [I Tried the Tool Trying to Kill Apache Airflow (Kestra)](../videos/b8-surdRWKo.md)
`b8-surdRWKo` · Better Stack · 2026-07-02 · q2 · intro · review · also: data-engineering

Quick tour of Kestra, a self-hosted, YAML-first workflow orchestrator pitched against Airflow: pipelines as config and live visual runs, but JVM memory cost, weak dynamic branching, and paywalled SSO.

- Techniques: Declarative flow: list of tasks plus a trigger (YAML); Run a local instance with one Docker command; Debug runs in the visual timeline and per-step logs
- Tools: Kestra, Apache Airflow, n8n, Zapier, Make, cron, Docker, Java / JVM, Python, Node.js, bash, SQL

## [Finally… A NotebookLM Alternative With an API](../videos/DnMtDdkSIi0.md)
`DnMtDdkSIi0` · Better Stack · 2026-07-02 · q2 · intro · review · also: rag-retrieval, local-ai

Walkthrough of Open Notebook, a self-hosted NotebookLM alternative with a REST API, swappable model providers including local Ollama, and podcast generation. Privacy and API access are the main draw; the Docker-first setup is a barrier.

- Techniques: Self-host via Docker Compose, then open the web UI; One notebook per project as a scoped research workspace; Structural codebase questions over an ingested repo; Custom podcast from dense documents; Pick the model provider per notebook based on sensitivity and cost
- Tools: Open Notebook, NotebookLM, AnythingLLM, Ollama, Docker / Docker Compose, SurrealDB, Gemini (named as the default-style provider the tool is not locked to)

## [herdr: Is This the Ultimate Agent Multiplexer?](../videos/PlN86TvzGy4.md)
`PlN86TvzGy4` · Better Stack · 2026-07-02 · q3 · intro · review · also: coding-agents, multi-agent

A walkthrough of herdr, a single Rust terminal multiplexer that adds agent awareness (working, blocked, done) to tmux-style panes, lets agents drive it through a CLI or socket, and works over SSH.

- Techniques: Install and launch herdr; Remap the prefix key; Agent-spawned panes with herdr CLI; Remote session over SSH with local config
- Tools: herdr, tmux, Warp, cmux, Claude Code, Codex CLI, OpenCode, Vim, Bash, Fish, Ratatui, Rust

## [Apple Just Built WSL for the Mac (Container Machines)](../videos/xXtsuDnapqc.md)
`xXtsuDnapqc` · Better Stack · 2026-07-02 · q3 · practitioner · review · also: sandboxing-execution

Walkthrough of Apple's new Container Machines, persistent per-container Linux VMs on macOS built on Apple's open-source container CLI, with benchmarks against OrbStack and Docker Desktop and the main caveats.

- Techniques: Build a dev machine image from a Dockerfile; Create, list and run a container machine; Use the Mac project files from inside Linux; Edit files over SSH for breakpoints and hot reload; One machine per distro target; Narrow the home mount before running untrusted code
- Tools: Apple container (Swift OCI container CLI and runtime, released last year), Apple Container Machines (persistent Linux VMs on macOS 26+), Apple Virtualization framework, Docker Desktop, OrbStack, Lima, Dockerfile / OCI images, Ubuntu 24, Alpine, Debian, Bun (bun dev server), PostgreSQL

## [You Don't Need React Portals For Modals Anymore (react-call)](../videos/K8TAc_EtDVc.md)
`K8TAc_EtDVc` · Better Stack · 2026-07-02 · q2 · intro · review · also: —

Better Stack walkthrough of react-call, a small library that lets you await React modals and dialogs like async functions, with upsert for singleton UI and useMutationFlow for async confirms.

- Techniques: Awaitable modal via createCallable HOC; Upsert for singleton UI; useMutationFlow for confirm-then-mutate
- Tools: react-call, React, window.confirm (referenced as the mental model, not used)

## [Scrapling: The Web Scraper That Repairs Itself](../videos/q-uj7wk0LRI.md)
`q-uj7wk0LRI` · Better Stack · 2026-07-02 · q3 · intro · review · also: data-engineering, rag-retrieval

Walkthrough of Scrapling, a Python scraping framework whose adaptive parser relocates moved or renamed elements without rewriting selectors, plus its fetcher tiers and spider framework.

- Techniques: Adaptive selector recovery; Tiered fetcher selection; Grow a script into a spider
- Tools: Scrapling (about 53,000+ GitHub stars, per the presenter; no version stated), Python, Requests, Beautiful Soup, Playwright, Selenium, Scrapy

## [TypeScript 7 is HERE (The Go Update)](../videos/e7Id_PKwSCQ.md)
`e7Id_PKwSCQ` · Better Stack · 2026-07-02 · q3 · intro · news · also: —

Better Stack walks through the TypeScript 7 release candidate, a Go port of the compiler: a Playwright type-check drops from about 6s to 0.87s, new checkers and builders flags add parallelism, and the speaker reports no breaking changes from TS 6.

- Techniques: Benchmark a type check across TS versions on your own repo; Single-thread TS 7 for debugging or constrained machines; Tune checkers and builders for parallel type checking; Upgrade path from TS 5 to TS 7; Run TS 6 and TS 7 side by side
- Tools: TypeScript 7 (RC), TypeScript 6, TypeScript 5, Go, Playwright, Parcel file watcher, VS Code, Claude, Bun

## [Dolt: This Makes SQL Feel Like Git](../videos/SDLfjrUyBw4.md)
`SDLfjrUyBw4` · Better Stack · 2026-07-02 · q3 · intro · tutorial · also: data-engineering

Quick walkthrough of Dolt, a MySQL-compatible SQL database with Git-style branch, diff, commit and merge on tables, plus where it sits relative to Git, DVC and LakeFS.

- Techniques: Clone a DoltHub database and make a versioned change; Branch, change, diff, merge on tables; Serve Dolt over the MySQL protocol for apps and BI tools
- Tools: Dolt (DoltHub getting-started database; CLI commands sql, diff, add, commit, branch, checkout, merge, log, status; SQL server mode), Git, DVC, LakeFS, MySQL-compatible clients, ORMs and BI tools (generic category, not a specific product)

## [Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry](../videos/ugUeZ8-b-u0.md)
`ugUeZ8-b-u0` · AI Engineer · 2026-06-18 · q3 · intro · talk · also: coding-agents, testing-verification

Argues Rust's strict compiler suits agent-written code better than Python or TypeScript: compile-time checks rule out bug classes that tests and LLM review miss, and compiler errors give agents concrete fix signals. Sponsored by Sentry.

- Techniques: Compile-in-the-loop repair; Deterministic checks before LLM review; Use error messages that name the concrete type; Choose a language by how strongly its checker constrains output; Write tests first when an agent writes tests
- Tools: Rust, rustc (Rust compiler), TypeScript, Python, Sentry

## [Terax: One Developer Built an AI Terminal Better Than Warp](../videos/3L8htHUzAI4.md)
`3L8htHUzAI4` · Better Stack · 2026-06-02 · q3 · intro · review · also: coding-agents, context-engineering

Review of Terax, a small open-source AI terminal and code editor built with Tauri 2 and Rust, compared against Warp and CMUX; the reviewer keeps Warp and Neovim for daily work.

- Techniques: Lean desktop shell for a terminal-plus-agent app; Read-only plan mode, then build mode, for agent edits; Generate a project context file with init, then review it as a diff; Hide sensitive tabs from the agent with a privacy page; Keep API keys in the OS keyring
- Tools: Terax, Tauri 2, Rust, React, Electron (comparison), Xterm.js (WebGPU renderer), CodeMirror 6, Vercel AI SDK, Warp, CMUX, Helix, Neovim

## [Why Claude Recommends Resend & Building in Public | Better Stack Podcast Ep. 15](../videos/8ahyAKK2l9Y.md)
`8ahyAKK2l9Y` · Better Stack · 2026-06-02 · q2 · intro · interview · also: security-guardrails, product-ux

Better Stack podcast with Resend's DX engineer on getting LLMs to recommend a vendor, scoping per-team AI agents with narrow API keys, and email deliverability basics. Mostly biographical, with a few practitioner nuggets.

- Techniques: One scoped identity per agent or team; Scheduled weekly digest agent; Weekly competitor watch, on demand; Research agent before writing a changelog or post; Scaffold landing pages from existing repo patterns; LLM-discoverability checklist for a docs or marketing site; Deliverability setup for a transactional email service; Obsidian vault synced to GitHub as a personal task store
- Tools: Resend, React Email, Claude, Hermes (OpenClaw-based agent), OpenClaw, Cursor, GitHub CLI, 1Password, Slack, Obsidian, Linear, Raycast

## [Stop Using Claude Code CLI. Use THIS Instead! (Oh-My-Pi)](../videos/8ukl-0tlVgM.md)
`8ukl-0tlVgM` · Better Stack · 2026-06-02 · q2 · intro · review · also: coding-agents, token-cost-efficiency, agent-architecture

A 5-minute Better Stack walkthrough of Oh My Pi, an open-source terminal agent harness built on the Pi framework, covering LSP refactoring, debugger attach, per-task models, hashline edits, and Pi package support.

- Techniques: Hashline edits (anchor-based line editing); LSP-backed workspace refactor; Per-task model routing in a harness; Debugger attach for agent debugging
- Tools: Oh My Pi (open-source terminal agent harness), Pi framework (base for Oh My Pi; source of the Doom package), Claude Code CLI (compared against; plugins and settings are imported on login), Claude Opus (named as the model that reproduces full edit text in Claude Code), Grok 4 Fast (model used for the 61% token-savings claim), DLV (Go debugger), DebugPy (Python debugger), Chrome (launched by the built-in browser tool), Hindsight (agent memory management, mentioned only), Rust (language of the demo app)

## [Vercel made a programming language](../videos/Koop0_nkNtc.md)
`Koop0_nkNtc` · Better Stack · 2026-06-02 · q3 · practitioner · review · also: coding-agents, context-engineering

Better Stack walkthrough of Xero, a new systems language whose toolchain emits JSON diagnostics with fix guidance so agents can repair code. A Claude fix run succeeded without docs, but the presenter doubts a new language was needed.

- Techniques: Self-describing toolchain for agents; Zero-context fix-loop test; Explicit capability marking for IO; Error propagation with raises and check; Scoped cleanup with owned values, drop and defer; Running a Xero program
- Tools: Xero (systems language and toolchain, named as 'Xero' or 'zero' in the transcript), Claude (Claude Code, used for the fix run), Rust, Zig, Go, jq, Bun (mentioned only as a possible future rewrite target), WebAssembly (compile target)

## [This New Syntax Wants To Replace JSX](../videos/B_N-O8_eG34.md)
`B_N-O8_eG34` · Better Stack · 2026-06-02 · q3 · intro · review · also: coding-agents

Walkthrough of TSRX, a statement-based JSX syntax from the creator of Ripple that compiles to React, Preact, Solid, Vue and Ripple. The presenter likes several control-flow ideas but will stay with React and Tailwind.

- Techniques: Statement-based conditional rendering; for...of list rendering with key and index; try/catch error boundary plus pending block for async; Hooks after conditions and early returns; Component-scoped CSS with shared style keyword; Escaped text vs raw HTML; Lazy destructuring with ampersand
- Tools: TSRX, Ripple, Ripple View, React, Preact, Solid, Vue, Svelte, Vite, Tailwind CSS, Claude, llms.txt

## [This One File Fixed My Dev Environment (Devbox)](../videos/U7YDcqP0dlI.md)
`U7YDcqP0dlI` · Better Stack · 2026-06-02 · q3 · intro · tutorial · also: —

Devbox (a Nix-backed CLI) puts a project's tool versions and scripts in a committed devbox.json plus lock file, so every developer and CI run gets the same environment.

- Techniques: Project-scoped toolchain with devbox.json; Shared project scripts through devbox run; Offload complex setup to a shell script; Export the same environment to CI and containers
- Tools: Devbox, Nix, Docker, Docker dev containers, VS Code, Node.js, Go, Python, Postgres, Codespaces

## [Bun.Image Makes Your Entire Image Pipeline Obsolete](../videos/Tnmyb_pdM10.md)
`Tnmyb_pdM10` · Better Stack · 2026-06-02 · q3 · practitioner · review · also: infra-cost-scaling

Short walkthrough of Bun.Image, the built-in image API in Bun 1.3.14, with resize, WebP conversion and ThumbHash placeholders, and a claim that it is faster than Sharp.

- Techniques: Resize, convert and compress with Bun.Image; Optional image operations; ThumbHash blur placeholders; Progressive JPEG for a loading effect
- Tools: Bun 1.3.14 (Bun.Image / image API), Sharp, libvips, WebP, ThumbHash, Waku, Next.js, Bun SQLite, Bun S3, Bun Postgres, Vercel Zero (referenced, not discussed)

## [npm installs can hack your laptop (Here's how to stop it)](../videos/Wq6yMdt11LM.md)
`Wq6yMdt11LM` · Better Stack · 2026-06-02 · q3 · practitioner · tutorial · also: security-guardrails

Seven practical npm/pnpm/bun supply-chain hardening steps: release-age gating, disabling install scripts, blocking git deps, pre-install scanners, lockfile checks, frozen CI installs, and dependency habits.

- Techniques: Release-age gating per package manager; Disable install scripts and allow-list exceptions; Block git and exotic dependencies; Scan packages before install via alias; Lockfile hygiene with lockfile-lint; Frozen installs in CI and production; Dependency hygiene habits
- Tools: npm, pnpm, bun, npx, bunx, MPQ, Socket Firewall, lockfile-lint, lavamoat allow-scripts, esbuild, TanStack React Start, Snyk vulnerability database

## [The NPM Worm Is Back And It's So Much Worse (TanStack Hacked)](../videos/BOABEBwNnvk.md)
`BOABEBwNnvk` · Better Stack · 2026-06-02 · q3 · practitioner · news · also: security-guardrails, claude-code

Walkthrough of the Shai-Hulud npm worm's fourth wave, which hit TanStack and about 160 other packages. It explains the persistence, credential theft, and how a poisoned CI cache plus OIDC publishing let attackers ship validly signed malicious releases.

- Techniques: Audit for agent-hook persistence after installing a package; Incident response order for a suspected worm; Trace install-time payloads through lifecycle scripts and optional dependencies; Treat CI cache restores as a trust boundary; Scope OIDC publishing to the release job only; Find 2FA-bypassing npm tokens on dev machines
- Tools: npm, npm trusted publishing (OIDC), pnpm, Bun (bun run task runner), GitHub Actions, GitHub pull_request_target, Claude Code (hooks, settings, session history), VS Code tasks, AWS IMDSv2, AWS ECS task metadata, Kubernetes service accounts, HashiCorp Vault

## [Vercel Built a Terminal Emulator and It's Only 12KB](../videos/MxACQUVS5mE.md)
`MxACQUVS5mE` · Better Stack · 2026-06-02 · q3 · intro · review · also: sandboxing-execution

Better Stack walks through Vercel's Wterm, a web terminal that renders to the DOM instead of a canvas, with a 12KB Zig/WASM core and an optional libghostty renderer; it covers WebSocket wiring and the rough edges.

- Techniques: DOM-rendered web terminal; WebSocket pty bridge; Swap in the libghostty renderer; Browser demo fallback without a backend
- Tools: Wterm (Vercel), WtermGhostty, libghostty, Ghostty, GhosttyWeb (Coda), xterm.js, Zig, WebAssembly, React, Vue, Node.js, Bun

## [This AI Tool Maps Any Codebase Before You Touch It (Understand-Anything)](../videos/VmIUXVlt7_I.md)
`VmIUXVlt7_I` · Better Stack · 2026-06-02 · q3 · practitioner · review · also: claude-code, context-engineering

Walkthrough of Understand-Anything, a Claude Code plugin that builds an interactive knowledge graph of a repo for onboarding and pre-change impact checks; the speaker also flags its heavy token cost.

- Techniques: Install and run Understand-Anything in Claude Code; Onboarding order: map, then tour, then questions; Use the graph as agent context; Pre-refactor impact check
- Tools: Understand-Anything (open-source Claude Code plugin, MIT license), Claude Code, Claude Max (subscription plan referenced for rate usage), Cursor, GitHub Copilot, Gemini CLI, Google microservices sample repo (demo target)

## [Perplexity Open-Sourced a Scanner Every Dev Should Know (Bumblebee)](../videos/L6iAw5yitfc.md)
`L6iAw5yitfc` · Better Stack · 2026-06-02 · q3 · practitioner · review · also: security-guardrails, mcp-and-tools

Better Stack demos Perplexity's open-source Bumblebee, a read-only Go binary that inventories a dev machine's packages, editor and browser extensions, and MCP configs from local metadata, for supply-chain incident response.

- Techniques: Weekly baseline inventory dumped centrally; Escalate scan depth by incident state; Query NDJSON with jq or a SIEM; Treat MCP configs as part of the secret and dependency surface
- Tools: Bumblebee (Perplexity open-source scanner), Go (go install, single binary), npm, pnpm, yarn, bun, Go modules, VS Code, Cursor, Claude, jq, MDM

## [OpenTUI: React for Your Terminal, Powered by Bun and Zig](../videos/zr4ctBgKAOU.md)
`zr4ctBgKAOU` · Better Stack · 2026-06-02 · q3 · intro · review · also: coding-agents

Walkthrough of OpenTUI, a Zig-core terminal UI library with React and Solid bindings running on Bun, compared against Ink. The speaker builds a small React TUI and argues JSX is the best way to compose terminal UIs.

- Techniques: Scaffold a React TUI project with the Bun template wizard; Choose a screen mode; Bind input state with useState and onInput; Style and lay out with Box props and Yoga flexbox; Animate with the useTimeline hook; Use other OpenTUI hooks and components; Live reload during development
- Tools: OpenTUI, Zig, React, Solid, Bun, Bun FFI, Yoga, Ink, Bubble Tea, Ratatui (spoken as 'Ratatouille'), Three.js (spoken as '3.js', WebGPU rendering), OpenCode

## [Yeah it’s over for NextJS... 13 NEW vulnerabilities](../videos/mYdx6hZG9qo.md)
`mYdx6hZG9qo` · Better Stack · 2026-06-02 · q3 · practitioner · news · also: security-guardrails

Better Stack walks through five of the 13 React and Next.js CVEs in one security release (middleware bypass, RSC denial of service, SSRF, cache poisoning, script XSS) and argues for moving off Next.js.

- Techniques: Enforce auth in the data loader, not only in middleware; Regression-test matcher and data-route coverage; Load-test server action endpoints with large or repetitive payloads; Make CDN cache keys match the content-type routing logic; Keep untrusted input out of inline script props; Limit what the app server can reach internally; Patch to the fixed Next.js release
- Tools: Next.js (Pages Router, i18n, middleware/proxy, getServerSideProps, next/script beforeInteractive), React Server Components and the React Flight serialization protocol (react-server-dom), TanStack Start, Astro, Vinext, Cloudflare, Python http.server (used as the internal target in the SSRF demo), curl, Browser devtools (Network tab, inspect element), Claude Mythos (suggested by the presenter for auditing the React and Next.js codebase)

## [Pake: This CLI Tool Makes 5MB Desktop Apps](../videos/6bu8zc6lsHQ.md)
`6bu8zc6lsHQ` · Better Stack · 2026-06-02 · q2 · intro · review · also: —

Short demo of Pake, a Rust CLI that wraps any live website as a ~5 MB native desktop app on the system webview. Useful for web apps, but it only handles running URLs and needed a source patch to build.

- Techniques: Wrap a live website as a desktop app; Restyle a wrapped site with injected CSS or JS; Native-app window options; Recover from a Pake build failure caused by pnpm version skew
- Tools: Pake, Tauri 2, Electron, Electrobun, ZeroNative, Bun, pnpm, npm, Mole, Claude Code, Rust, Zig

## [Vercel Just Killed Electron With Zig](../videos/GXNjnu7UqFs.md)
`GXNjnu7UqFs` · Better Stack · 2026-06-02 · q2 · intro · review · also: vibe-coding-app-building

Walkthrough of zero-native, a thin Zig shell that hosts a system WebView for small desktop apps, covering setup, dev loop, 2.9 MB packaging, Electrobun comparison and limits.

- Techniques: Scaffold a zero-native app; Dev loop and packaging; Add zero-native to an existing JS project; Configure the app via app.zon; Call native or C code from the frontend
- Tools: zero-native (CLI and build via zig build), Zig, mise, Homebrew, Vite, React, Svelte, Vue, Next.js, Electron, Electrobun, Bun

## [The Open-Source ngrok Alternative Devs Are Switching To (Zrok)](../videos/dLW0cT-iTjs.md)
`dLW0cT-iTjs` · Better Stack · 2026-05-02 · q3 · intro · review · also: security-guardrails

A 5-minute walkthrough of zrok, an open-source, self-hostable ngrok alternative that shares localhost publicly or to token-holders without port forwarding, plus its tradeoffs versus ngrok.

- Techniques: Public share of a local dev server; Token-gated private share; Share a directory as a browsable drive
- Tools: zrok, OpenZiti, ngrok, Cloudflare Tunnel, Tailscale, Next.js

## [HTML In Canvas Is Wild And I Love It](../videos/1zfRSiZBLyQ.md)
`1zfRSiZBLyQ` · Better Stack · 2026-05-02 · q3 · intro · tutorial · also: vibe-coding-app-building

Better Stack demo of HTML in Canvas, an experimental proposal that lets live DOM elements render into WebGL or 2D canvases, with the basic setup steps and its drawbacks.

- Techniques: Render live DOM into a WebGL scene as a texture; 2D canvas: draw a DOM element directly; Custom input with a DOM element behind a canvas skin
- Tools: HTML in Canvas (browser proposal), Chrome Canary (experiment behind a flag), three.js, WebGL, WebGPU, Canvas 2D context drawElementImage, requestAnimationFrame

## [Stop Rebuilding Backends… Just Use Directus](../videos/o9-tFFcAhXo.md)
`o9-tFFcAhXo` · Better Stack · 2026-05-02 · q3 · intro · review · also: data-engineering

Better Stack walkthrough of Directus, an open-source data platform that sits on top of an existing SQL database and adds APIs, permissions, an admin UI and flows, built in about 8 minutes from a blank install.

- Techniques: Rapid internal backend on an existing SQL database with Directus; Event-driven email notification with a Directus flow; Local testing of outbound email with Mailpit
- Tools: Directus, PostgreSQL, MySQL, Oracle Database, Docker Compose, Mailpit, Strapi, Payload, Hasura, n8n, Zapier

## [Run S3 on Your Laptop? This Changes Everything (MinIO)](../videos/GHeLgENOBb4.md)
`GHeLgENOBb4` · Better Stack · 2026-05-02 · q2 · intro · review · also: infra-cost-scaling

Short intro to running MinIO, an S3-compatible object store, on a laptop for local dev and prototypes, with the caveats that the repo is archived and the project is moving to a paid AI Store.

- Techniques: Run a local S3-compatible store in Docker; Register the local server with the MinIO client (mc) as an alias; Keep the S3 SDK code and only change the endpoint; Tiered environments behind one S3 API; Browse and preview objects in the MinIO web console
- Tools: MinIO, MinIO AI Store, mc (MinIO client), Docker, boto3, Python, Kubernetes, Ceph, Garage, AWS S3

## [Netflix's New AI Can Now Remove Actors From Scenes (VOID Model Breakdown)](../videos/1yj46x45-QI.md)
`1yj46x45-QI` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: voice-multimodal, models-research

Walkthrough of Netflix's open-source VOID model, which removes an object from video and also rewrites the physical consequences of its removal, plus a self-built web UI and the setup gotchas the speaker hit.

- Techniques: Two-stage video object removal with an intermediate mask; Counterfactual training data from paired simulations; Running VOID on RunPod (speaker's setup); Web UI workflow, tab by tab; Prompting for the counterfactual background; Segment every part of the target
- Tools: VOID (Video Object and Interaction Deletion, Netflix open source), SAM2 (Segment Anything Model 2), SAM3 (gated; required for the inference command, per the speaker), Gemini API (pose estimation for quad mask generation), Video diffusion model (unnamed in transcript), Vision-language model (unnamed in transcript), Flow Warp Noise (second-pass shape stabilization), Kubric/'Kubrick' physics simulator (likely; caption), RunPod (H100 GPU pods), Hugging Face (model downloads), Gradio (VOID's official demo), run.sh (speaker's repo install script)

## [Stop Building Login Systems… Use This Instead (Authentik)](../videos/LVuspKy4P2w.md)
`LVuspKy4P2w` · Better Stack · 2026-05-02 · q2 · intro · review · also: security-guardrails

Short walkthrough of Authentik, a self-hosted open-source identity provider for SSO, OAuth login and MFA across your own apps, with a Docker Compose quick start and a take on its costs versus Keycloak, Authelia, Okta and Auth0.

- Techniques: Stand up Authentik with Docker Compose; Register an app with OAuth2/OIDC in the admin UI; Model login logic as flow stages plus Python policies; Weigh Authentik against other self-hosted IdPs by RAM, ops load and scale
- Tools: Authentik, Docker Compose, Kubernetes, OAuth2/OIDC, Keycloak, Authelia, Okta, Auth0

## [PostgREST Deletes 80% of Your Backend Code](../videos/DVYVvewa2kc.md)
`DVYVvewa2kc` · Better Stack · 2026-05-02 · q2 · intro · tutorial · also: security-guardrails

Short Better Stack tutorial showing PostgREST turning a Postgres table into a REST API with Row Level Security and Swagger docs, with no backend code, plus its trade-offs.

- Techniques: Run PostgREST as a REST layer over Postgres via Docker Compose; Enforce access with Row Level Security instead of middleware; Query and write through HTTP with curl; Keep a thin backend layer for complex logic
- Tools: PostgREST, PostgreSQL, Docker Compose, Swagger UI, Supabase (named as a production user of PostgREST), curl

## [Fallow: The Code Intelligence Tool Every Claude User Needs](../videos/-lCfwIoDXq8.md)
`-lCfwIoDXq8` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: claude-code, pr-code-review

Better Stack walks through Fallow, a Rust-built static analyzer for JS/TS (dead code, duplication, complexity), and shows how it works as a guardrail for Claude Code runs and branch-level PR audits.

- Techniques: Snapshot the project with the summary report; Drill into one category with machine-readable output; Preview fixes with dry run before any write; Guard an agent run with the Fallow skill and a scoped prompt; Scope a config file to ignore noise; Audit only the current branch against main; Generate Claude Code hooks for Fallow; CI with baselines and PR annotations
- Tools: Fallow, Claude Code, knip, jscpd, ESLint, bunx, Oxc, VS Code extension, Cursor, MCP server, V8 runtime coverage, GitHub Action

## [Why Developers Are Quietly Switching to This Note App (SiYuan)](../videos/2L3txd8_Psk.md)
`2L3txd8_Psk` · Better Stack · 2026-05-02 · q2 · intro · review · also: —

Better Stack reviews SiYuan, a self-hosted, open-source, block-based note app, arguing that permanent block IDs, built-in databases and SQL suit developer documentation better than file-based Obsidian or cloud Notion.

- Techniques: Block-reference notes for moving content safely; Lightweight bug tracker inside a notes app; Local self-hosting with Docker Compose
- Tools: SiYuan, Obsidian, Notion, Docker, Docker Compose, SQL, Python (incidental code block)

## [This is WAY better than NextJS (TanStack Server Components)](../videos/pWxRvFFUHcY.md)
`pWxRvFFUHcY` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: —

Demo of TanStack Start server components: server functions return server-rendered trees, and composite components with slots let client components render inside without server-side use client boundaries.

- Techniques: Server component via server function plus loader; Composite component with children slot; Render-prop slot for passing server data to client code; Component-prop slot; Streaming slow server components with the use hook and Suspense
- Tools: TanStack Start, TanStack Router (loader, useLoaderData), TanStack Query, React Server Components, React use hook and Suspense, Next.js (comparison only)

## [This Open-Source Tool Might Fix Design Handoff Forever (PenPot)](../videos/9AGrepjrbqY.md)
`9AGrepjrbqY` · Better Stack · 2026-05-02 · q2 · intro · review · also: vibe-coding-app-building

Better Stack walkthrough of Penpot, an open-source browser design tool whose output is real SVG/CSS, pitched as a Figma alternative that reduces design-to-code handoff; self-hosting via Docker is shown.

- Techniques: Self-host Penpot with Docker Compose; Design in flex layout so the inspect CSS maps to code; Use inspect mode for handoff instead of a dev-mode plugin
- Tools: Penpot, Figma, Sketch, Docker, Docker Compose, SVG, CSS, Flexbox, CSS Grid, HTML

## [The Open-Source Alternative to Tableau and Power BI (ReDash)](../videos/ouKwtFoT1ZY.md)
`ouKwtFoT1ZY` · Better Stack · 2026-05-02 · q2 · intro · review · also: observability

Short Better Stack overview of Redash, a self-hosted, open-source SQL editor and dashboard builder, with a quick demo of query, chart, dashboard, and scheduled refresh, and a frank list of trade-offs against Metabase, Superset, Tableau and Power BI.

- Techniques: Self-host Redash with Docker; Query, chart, parameter, dashboard flow; Scheduled dashboard refresh; Joining API data with database queries
- Tools: Redash, Docker, Docker Compose, PostgreSQL, MySQL, BigQuery, Snowflake, MongoDB, Metabase, Apache Superset, Tableau, Power BI

## [GitHub Was NOT Made for AI Agents (So Cloudflare Built Their Own)](../videos/PWj6GnTUBnk.md)
`PWj6GnTUBnk` · Better Stack · 2026-05-02 · q3 · practitioner · review · also: software-factory, agent-architecture, sandboxing-execution

Walkthrough of Cloudflare Artifacts, a Git-compatible repo store on Durable Objects built for agents, with a fork-per-task demo the speaker could not run because the product is in private beta.

- Techniques: Fork-per-task repo workspaces; Git-backed agent tools: read, write, commit (commit also pushes); Durable Object SQLite as the persistence layer for agent repos; Verification loop idea: run the agent's changed code in a sandbox, and check front-end work in a browser; Reconstructing a diff without git diff
- Tools: Cloudflare Artifacts (private beta), Cloudflare Workers, Cloudflare Durable Objects, Cloudflare Dynamic Workers, Cloudflare Sandboxes, Cloudflare Browser (Puppeteer), Wrangler (wrangler.jsonc / wrangler.toml bindings), isomorphic-git, Zig (compiled to WASM), Anthropic SDK, Git protocol, S3 Files

## [How IBM’s Bob uses "Review Mode" to solve the hardest coding tasks (Full Breakdown)](../videos/pSzLkt0NfJQ.md)
`pSzLkt0NfJQ` · Better Stack · 2026-05-02 · q2 · intro · review · also: coding-agents, pr-code-review

Better Stack walkthrough of IBM's Bob IDE, which separates ask/code/plan modes and runs a security Review mode with a findings panel and one-click fixes; tested on the ZBank COBOL repo, with a short sponsored-style pitch for the free trial.

- Techniques: Mode-separated agent workflow; Scoped auto-approval; Review-then-fix-then-test loop; Atomic SQLite write for a race condition
- Tools: IBM Bob, Bob Shell, IBM Granite, ZBank (open-source COBOL repo), Streamlit, SQLite, COBOL, VS Code

## [Why GUIs Will Replace TUIs for AI Developer Tools | Better Stack Podcast Ep. 14](../videos/zr-Xk0UVHEU.md)
`zr-Xk0UVHEU` · Better Stack · 2026-04-02 · q3 · practitioner · interview · also: coding-agents, pr-code-review, multi-agent

Better Stack podcast with Warp DevRel Ben Holmes on why GUI-style wrappers around coding agents will beat TUIs, plus practical patterns for agent code review, cloud agents, and multi-agent delegation.

- Techniques: Fresh-session review pass; Ask why, do not accuse; Two-lens review passes; Agent review as a GitHub Action; Keep READMEs and CLAUDE.md thin; Two clones instead of worktrees for parallel agents; Cloud research, then fork locally; Multi-repo sandbox environment; Route by task complexity; Tune the harness per model; Figma for design, agent for implementation
- Tools: Warp, Oz (Warp cloud agent platform), Claude Code, Codex (CLI and app), OpenCode, Pi, OpenClaw, Cursor, GitHub Copilot, Ghostty, tmux, cmux

## [T3 Code: Better Than Codex?](../videos/6x7hh6Qzm9U.md)
`6x7hh6Qzm9U` · Better Stack · 2026-04-02 · q3 · intro · review · also: coding-agents, multi-agent

Walkthrough of T3 Code, an open-source desktop GUI for running multiple coding agents (currently Codex) on your existing subscription, with per-thread git worktrees, plan mode, one-click commit/PR, and a list of missing features.

- Techniques: One git worktree per agent thread; Plan first, then implement; Supervised vs full-access tool calls; One-click commit, push and PR; Quick-action buttons for setup commands; Fork the agent GUI and let the agent extend it
- Tools: T3 Code, Codex, Codex app, Claude Code, Cursor, OpenCode, Gemini, git worktrees, Finder

## [This Shouldn’t Be Better Than 1Password… But It Is](../videos/NLmYjFe_Gg4.md)
`NLmYjFe_Gg4` · Better Stack · 2026-04-02 · q2 · intro · tutorial · also: security-guardrails

Better Stack walkthrough of self-hosting Vaultwarden (a lightweight Rust Bitwarden-compatible server) via Docker Compose, connecting the Bitwarden browser extension and the Bitwarden CLI for scripted secret retrieval.

- Techniques: Run Vaultwarden with Docker Compose; Point Bitwarden clients at a self-hosted server; Pull credentials into scripts with the Bitwarden CLI
- Tools: Vaultwarden, Bitwarden (clients, browser extension, CLI, server), 1Password, NordPass, Docker, Docker Compose, Homebrew, Google Chrome, YubiKey, M4 Pro (hardware)

## [Fix Slow React Components in Seconds! (New GitHub Storybook Addon)](../videos/fv9wj8nkDVM.md)
`fv9wj8nkDVM` · Better Stack · 2026-04-02 · q2 · intro · review · also: testing-verification

Walkthrough of GitHub's new Storybook performance-panel add-on for measuring component frame timing, DOM churn, layout thrashing and React render cascades before code reaches production.

- Techniques: Component-level performance check in Storybook; Mark hero and call-to-action elements for render timing; Avoid setState in useLayoutEffect for updates that repeat; Batch style reads and writes to prevent layout thrashing; Memoize components to cut redundant renders
- Tools: Storybook, GitHub Storybook performance add-on (unnamed in transcript), React, useLayoutEffect (React hook), Vue, Svelte, Web Components, Lighthouse, Chrome, Edge

## [Stop Using Docker for GPUs! (RunPod Flash is INSANE!)](../videos/Biv4fKGsTcE.md)
`Biv4fKGsTcE` · Better Stack · 2026-04-02 · q2 · intro · review · also: infra-cost-scaling

Walkthrough of RunPod Flash, which turns decorated Python functions into on-demand serverless GPU endpoints without Docker, shown via a two-stage CPU-resize then RTX 5090 video-generation pipeline.

- Techniques: Split a pipeline by hardware class; Expose each heavy step as an on-demand endpoint; Local setup sequence; Budget for the cold first run; Monitor through the analytics tab
- Tools: RunPod Flash, Flash SDK, RunPod serverless, uv, Python, CogVideoX ("cog video X", 5B parameters), NVIDIA RTX 5090, Docker (contrasted, not used), Discord (example trigger)

## [Claude Code + CMUX: The Ultimate AI Coding Terminal](../videos/8oLP8oxqtOE.md)
`8oLP8oxqtOE` · Better Stack · 2026-04-02 · q3 · intro · review · also: claude-code, coding-agents, multi-agent

Walkthrough of cmux, a native macOS terminal whose CLI and Unix socket let Claude Code or OpenCode drive browser panes, spawn sub-agent panes, and send attention notifications.

- Techniques: Agent-driven browser pane for live testing; Sub-agents in split panes that report back and close; Attention notifications with pane flash; Sidebar status from the agent; Setup with cmux skills and hooks; Cheap demo runs by switching the model
- Tools: cmux, Claude Code, OpenCode, libghostty, Ghostty, WebKit, Bonsplit, tmux, Warp, soloterm, Demux, Haiku

## [Postman Killer? I Didn’t Expect This (Hoppscotch)](../videos/Jf9DGIyBkm4.md)
`Jf9DGIyBkm4` · Better Stack · 2026-04-02 · q2 · intro · review · also: —

Better Stack's quick review of Hoppscotch, a free, open-source, browser-first API client, as a lighter alternative to Postman, with its speed and collaboration advantages and its gaps.

- Techniques: Quick REST check in the browser; Environment variables for switching targets; WebSocket test; Migrate from Postman or Insomnia; Local, offline or self-hosted use for privacy; Use the CLI in CI/CD
- Tools: Hoppscotch, Postman, Insomnia, Hoppscotch CLI (CI/CD), Hoppscotch browser extension, WebSocket, GraphQL, Server-Sent Events (SSE), MQTT

## [The Open-Source Firebase Alternative Might Be Better (AppWrite)](../videos/PuH4Wq5Smwg.md)
`PuH4Wq5Smwg` · Better Stack · 2026-04-02 · q2 · intro · tutorial · also: infra-cost-scaling

Better Stack walkthrough of self-hosting Appwrite, an open-source Firebase alternative, with a Docker Compose setup, a to-do app sync demo, and trade-offs versus Supabase and Firebase.

- Techniques: Self-host Appwrite with Docker Compose; Register a localhost web platform; Per-role collection permissions; Wire the client through env variables
- Tools: Appwrite, Docker, Docker Compose, Firebase, Supabase, Cloudflare, MariaDB, PostgreSQL, React, Flutter, Better Stack

## [Chrome Just Became the Ultimate Agent Browser (Finally!)](../videos/51m_GGbXAng.md)
`51m_GGbXAng` · Better Stack · 2026-04-02 · q3 · practitioner · tutorial · also: mcp-and-tools, coding-agents

Chrome 144+ lets the Chrome DevTools MCP server auto-attach to your running browser for login-state debugging, element selection and network inspection, plus an experimental CLI alternative that avoids MCP context cost.

- Techniques: Attach the Chrome DevTools MCP server to your running Chrome (auto-connect); Select an element in DevTools to hand it to the agent; Isolated profile for security-sensitive use; Sandboxed MCP server with an HTTP remote debugging port; Chrome DevTools CLI instead of the MCP server; Persist the debugging profile across sessions
- Tools: Chrome DevTools MCP server (auto-connect option), Chrome DevTools CLI (experimental, in the MCP skills directory), Google Chrome 144+, OpenCode, Claude Code (terminal), Lighthouse (audit tool used by the agent), Playwright (mentioned as a comparison), Agent Browser (mentioned as the presenter's preferred tool), Comet (mentioned as an AI browser), Claude Chrome extension (mentioned), React Grab (mentioned), Arc (mentioned; the presenter wishes the feature came to it)

## [The NPM Package Everyone Is Adding To Their Site (Web Haptics)](../videos/zAbQE6K0d1k.md)
`zAbQE6K0d1k` · Better Stack · 2026-04-02 · q3 · intro · tutorial · also: product-ux

Walkthrough of web-haptics, an npm package that adds vibration feedback to websites through a React hook, custom patterns, and a hidden-switch trick that makes it work on iOS.

- Techniques: Basic React trigger; Preset patterns; Custom vibration array; Hidden-switch fallback for iOS; Feature detection before rendering haptic UI
- Tools: web-haptics (npm package, the video spells it 'webhaptics'), React hook (useWebHaptics, captioned as 'use web haptics'), Svelte helper, Vanilla JavaScript API, navigator.vibrate (Web Vibration API), web-haptics package website editor

## [This Open-Source Tool Replaces Ollama + LangChain + Your UI](../videos/pSYEcJTt4t4.md)
`pSYEcJTt4t4` · Better Stack · 2026-04-02 · q3 · intro · review · also: local-ai, rag-retrieval

Better Stack walkthrough of AnythingLLM, a self-hosted open-source AI workspace that bundles local LLM chat, drag-and-drop RAG, no-code agents and a REST API into one desktop app, with an honest pros/cons take.

- Techniques: Single-app local RAG setup; Citation-grounded codebase Q&A; Visual agent with tool embedding; Swap providers mid-chat; Embed private RAG in other products
- Tools: AnythingLLM, Ollama, LanceDB, pgvector, Qdrant, LangChain, Open WebUI, PrivateGPT, Flowise, Langflow, SERP API, MCP servers

## [AFFiNE: The Open-Source Alternative for Notion, Miro and Airtable](../videos/PK5B_xapfxg.md)
`PK5B_xapfxg` · Better Stack · 2026-04-02 · q3 · intro · review · also: —

Better Stack walkthrough of AFFiNE, an open-source, local-first, self-hostable workspace that combines docs, databases and an infinite whiteboard canvas, with a candid list of its rough edges.

- Techniques: Self-host AFFiNE with Docker Compose; Doc plus architecture diagram on one canvas; Sticky notes to Kanban database; Embed external context in the page; Custom blocks with BlockSuite
- Tools: AFFiNE, BlockSuite, Y-Octo (CRDT sync, as captioned), Octobase (Rust backend, as captioned), Docker Compose, Notion, Obsidian, Miro, AppFlowy, AnyType, Figma, GitHub

## [Millions of JS Devs Just Got Hacked... (axios pwned)](../videos/5xWSezMFweE.md)
`5xWSezMFweE` · Better Stack · 2026-04-02 · q3 · intro · news · also: security-guardrails

News recap of the March 31, 2026 npm compromise of the axios package: two backdoored releases used a postinstall script to drop a cross-platform RAT. Mitigations are committed lockfiles, npm ci, a minimum package age, and blocking install scripts.

- Techniques: Detect affected installs; Commit the lockfile and install with npm ci in pipelines; Enforce a minimum package age; Block install scripts by default; Treat an affected host as a full credential compromise
- Tools: npm, npm CLI, npm ci, npm install --ignore-scripts, axios 1.14.1, axios 0.30.4, plain-crypto-js, setup.js (postinstall script), package.json, package-lock.json (lockfile), node_modules, GitHub Actions

## [This Open-Source Tool Replaces Bubble and Retool (Appsmith)](../videos/8O7AjZIAkpk.md)
`8O7AjZIAkpk` · Better Stack · 2026-04-02 · q2 · intro · review · also: vibe-coding-app-building

Short Better Stack walkthrough of Appsmith, a self-hostable open-source low-code tool for internal dashboards, showing a Postgres employee search and CRUD-style table in about two minutes, with an honest list of limits and a Retool comparison.

- Techniques: Bind a Postgres table to a low-code table widget; Search query driven by an input widget; Keep logic in JS and source in Git; Server-side pagination for large tables
- Tools: Appsmith, PostgreSQL, React, Docker, Kubernetes, Git, Retool, Bubble, Webflow, ToolJet

## [Age Verification Is Coming For Linux...](../videos/TbLLYN4ftnY.md)
`TbLLYN4ftnY` · Better Stack · 2026-04-02 · q2 · intro · news · also: governance-compliance

Better Stack commentary on California's Digital Age Assurance Act, which would make OS providers collect age brackets and expose them to apps, and why the speaker thinks Linux distros are caught in its scope.

- Techniques: Minimal-disclosure age signal over D-Bus (proposal)
- Tools: D-Bus, apt, Homebrew, Ubuntu, Debian, Arch Linux, Fedora, MidnightBSD, Kicksecure, Whonix

## [Electrobun: No Node, No Chromium, Just Pure Bun Performance](../videos/ONFLLhNfcx4.md)
`ONFLLhNfcx4` · Better Stack · 2026-04-02 · q3 · intro · tutorial · also: —

A 6-minute Better Stack walkthrough of Electrobun, a Bun-based desktop app framework that uses OS-native webviews instead of Chromium, with a from-scratch React example and an honest list of its rough edges.

- Techniques: Scaffold from an Electrobun template; Config file, entry point and views for a Bun app; Window chrome and menu tweaks; Scripted dev and production builds
- Tools: Electrobun, Bun, React, Electron, Tauri (transcribed as 'Towery'), Chromium Embedded Framework, WebKit, Edge WebView2, WebKitGTK, Svelte, Vue, SolidJS

## [The End of .env Files as We Know Them](../videos/nxH-BrsCPTo.md)
`nxH-BrsCPTo` · Better Stack · 2026-04-02 · q3 · intro · tutorial · also: security-guardrails

Better Stack walkthrough of Varlock, an open-source tool that replaces plaintext .env files with a typed, committable schema whose secrets resolve at runtime from 1Password and similar vaults.

- Techniques: Commit a typed env schema instead of a .env file; Inject config at process start with varlock run; Pull a secret from 1Password into the schema; Unlock 1Password with biometrics for local development
- Tools: Varlock (open source env schema tool, npm package and standalone CLI, version not stated), varlock 1Password plugin, 1Password, 1Password desktop app and CLI, Bitwarden, AWS plugin, GCP plugin, Vite, Next.js, Cloudflare Workers integration, VS Code Varlock extension, GitHub Action for Varlock

## [The Open-Source Copilot Alternative Devs Are Switching To (Tabby)](../videos/eZ3J45K7gXU.md)
`eZ3J45K7gXU` · Better Stack · 2026-04-02 · q2 · intro · review · also: local-ai, coding-agents

Walkthrough of Tabby, a self-hosted AI coding server run via Docker and used from a VS Code extension, giving Copilot-style completions and repo-aware chat with code kept on your own machine. Short promotional demo with little exact setup detail.

- Techniques: Run a self-hosted completion and chat server, then point the IDE at it; Use selected-code actions for refactor, perf and tests; Match the model to hardware before judging quality
- Tools: Tabby (self-hosted AI coding server, Docker), VS Code (Tabby extension), Docker, GitHub Copilot, Cursor, Continue (transcribed as 'Continued Dev'), Tab9 (transcript name; likely Tabnine), Mac M4 Pro (hardware used for the demo)

## [I Replaced Vercel with Dokploy](../videos/v6fn0KMCtEo.md)
`v6fn0KMCtEo` · Better Stack · 2026-04-02 · q2 · intro · review · also: infra-cost-scaling

Better Stack's 4-minute walkthrough of Dokploy, a self-hosted, Docker-native PaaS that turns a rented VPS into a Vercel/Heroku-style deploy target with HTTPS, logs, rollback and optional Swarm scaling.

- Techniques: Self-hosted push-to-deploy on a cheap VPS; Docker Swarm for multi-server scaling via Dokploy; Built-in ops bundle instead of extra tools
- Tools: Dokploy, Docker, Docker Compose, Docker Swarm, Traefik, Hetzner VPS, GitHub, Next.js, Vercel, Railway, Heroku, Coolify

## [I Let Aider AI Refactor My App](../videos/cTSvN0YLMgw.md)
`cTSvN0YLMgw` · Better Stack · 2026-03-02 · q3 · intro · review · also: coding-agents, token-cost-efficiency

Short walkthrough of Aider, a terminal AI pair programmer that makes git-committed, repo-wide edits. Its architect-then-code split and per-change undo are the useful parts; the speed and cost claims are mostly unverified.

- Techniques: Architect-then-code two-pass edit; Git-as-checkpoint for agent edits; Passing-tests-plus-clean-commit as the done bar; Model swap via YAML config for cheaper runs; Diff review before accepting
- Tools: Aider, DeepSeek (cited as DeepSeq in captions), Claude (model), OpenAI models, Ollama, Flask, Flask-Login, bcrypt, React, TypeScript, tree-sitter, Git

## [The Fastest Way to Debug Docker Containers (Dozzle)](../videos/cyNv7UzNaU4.md)
`cyNv7UzNaU4` · Better Stack · 2026-03-02 · q2 · intro · review · also: observability

A short walkthrough of Dozzle, a lightweight open-source live log viewer for Docker and Kubernetes that streams container logs to the browser without storing them; v10 adds alerts, webhooks and DuckDB-based SQL queries.

- Techniques: Live container log tail in the browser; Compose service for a live log viewer; Lock down before exposing beyond localhost; Log alerts to a webhook (v10)
- Tools: Dozzle (v10 cited), Docker, Docker Compose, Docker Swarm, Kubernetes, Helm, DuckDB, Slack (webhook target)

## [Coding Locally Is Slowing You Down](../videos/-b1qrPFl04A.md)
`-b1qrPFl04A` · Better Stack · 2026-03-02 · q2 · intro · tutorial · also: sandboxing-execution

Better Stack walkthrough of Code Server (VS Code in a browser on a remote machine), run locally in Docker on a Mac for the demo; covers pros (reproducible, consistent env, lighter laptops) and cons (latency, RAM needs, basic default security).

- Techniques: Run Code Server in Docker for a quick trial; Move the heavy environment to a remote host and keep the laptop as a thin client; Pair with dev containers for reproducible environments; Harden before exposing publicly
- Tools: Code Server, VS Code, Docker, Django, pip, GitHub Copilot, GitHub Codespaces, dev containers, Postgres, Node.js, Python

## [Headscale - The Tool That Made Me DELETE My Tailscale Subscription!](../videos/8t8FZaBamqA.md)
`8t8FZaBamqA` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: infra-cost-scaling

Walkthrough of Headscale, a self-hosted open-source control plane for Tailscale clients: Docker setup, pre-auth keys, a permissive ACL, and an honest verdict that setup is involved and the web UI is buggy.

- Techniques: Dockerized Headscale control plane with a reverse proxy; User-scoped pre-auth keys for joining nodes; Permissive starter ACL plus SSH rule; Checking reachability from inside and outside the tailnet
- Tools: Headscale, Tailscale (client and reference control plane), Docker / Docker Compose, Caddy, SQLite, PostgreSQL (optional backend), Headscale web UI (community, unnamed), Cloudflare (DNS), Ubuntu (test servers), Claude Opus (mentioned as a tool for building a UI), OpenClaw (mentioned as a possible offline local-LLM target)

## [Vercel Just DESTROYED Port Numbers Forever (Portless)](../videos/DzGwnTbQjjg.md)
`DzGwnTbQjjg` · Better Stack · 2026-03-02 · q3 · intro · review · also: coding-agents

Short walkthrough of Portless, a Vercel Labs CLI that gives dev servers stable named localhost URLs through a local proxy instead of fixed port numbers, aimed at humans and parallel AI agents.

- Techniques: Named stable dev hostnames via a local proxy; Portless URLs without a port suffix; Debugging Portless itself; Making a framework respect a dynamic port
- Tools: Portless (Vercel Labs CLI), Bun (bun run dev in the demo), Vite, Next.js, Agent Browser (Vercel Labs; plugged for next video, not covered), JSON Render (Vercel Labs; named only in passing)

## [A Code Editor That Actually Scales](../videos/kCWwrx51IS4.md)
`kCWwrx51IS4` · Better Stack · 2026-03-02 · q2 · intro · review · also: coding-agents, claude-code

A short tour of Zed, a Rust editor pitched against Cursor on large-repo speed and real-time multiplayer. The Claude integration via ACP is the headline, but the evidence for speed is anecdotal.

- Techniques: Inline AI edit on a selection; Opt-in Claude Code sidebar; Live collaboration channel for pairing and review; Keyboard navigation for large repos
- Tools: Zed, Claude (via Agent Client Protocol, ACP), Claude Code (sidebar in Zed, transcript says 'Cloud Code'), Cursor (comparison only), GitHub (invites)

## [SQLite is 138x Slower Than This?! (Testing Stoolap)](../videos/t6fbNGC_48c.md)
`t6fbNGC_48c` · Better Stack · 2026-03-02 · q3 · intro · review · also: data-engineering

Tests Stoolap, a Rust embedded analytics DB with a native Node.js binding: 4-6x faster than SQLite on COUNT DISTINCT, well short of the 138x headline, and the npm package was broken at the time.

- Techniques: Head-to-head embedded DB micro-benchmark; Second benchmark for DISTINCT with ORDER BY; Building an unpublished native-binding package from source; Why a native addon beats a socket bridge (napi-rs pattern)
- Tools: Stoolap (embedded Rust OLAP database, Node.js driver), SQLite, Node.js, Rust, napi-rs, Rayon, DuckDB (mentioned as analytics comparison), BigQuery (mentioned as analytics comparison), PostgreSQL (mentioned as OLTP comparison), npm

## [I thought I was a Senior React Dev... until I ran React Doctor.](../videos/k3vyIIEZfU4.md)
`k3vyIIEZfU4` · Better Stack · 2026-03-02 · q2 · intro · review · also: coding-agents

A short walkthrough of React Doctor, a Rust-fast (OXLint-based) CLI that flags React anti-patterns, shown on an old personal project and an open-source CRM monorepo.

- Techniques: Run a React anti-pattern scan on a repo; Fix the three demonstrated findings; Use the scanner as a coding-agent skill
- Tools: React Doctor (CLI, Aidan Bai), OXLint (Rust-based JavaScript linter), React, Recharts, Node.js (programmatic API), Million.js (creator's earlier project, mentioned), React Grab (creator's project, mentioned), React Scan (creator's project, mentioned), Amy (named as a creator project, caption may be imprecise), Twenty (open-source Salesforce-alternative CRM, captioned as "20"), useTransition (React hook referenced)

## [We Tested The Smallest "OpenClaw" AI Agent in the World (zclaw)](../videos/MCTTe8nZEgc.md)
`MCTTe8nZEgc` · Better Stack · 2026-03-02 · q2 · intro · review · also: agent-architecture, coding-agents

Better Stack installs zclaw, a tiny ESP-IDF AI assistant for ESP32 boards driven over Telegram, then adds a custom display tool; a hands-on hardware demo with reproducible setup steps and candid limits.

- Techniques: zclaw install and provisioning flow; Wi-Fi bench workaround; Adding a custom tool to zclaw; Natural-language pin aliases stored on-device; Hello-world LED sanity circuit; Telegram allow-list for device control
- Tools: zclaw, ESP32, ESP32-C3, ESP-IDF, Telegram, BotFather (Telegram bot), Telegram user-info bot, OpenRouter, OpenAI, Anthropic, Ollama, Claude Code

## [TanStack Has A New Package (And Its Awesome)](../videos/EdKTZ7WsaiY.md)
`EdKTZ7WsaiY` · Better Stack · 2026-03-02 · q3 · intro · review · also: —

A feature tour of TanStack Hotkeys, an alpha, type-safe, framework-agnostic keyboard-shortcut package for React and vanilla JS, covering cross-platform bindings, scoping, sequences, recording UI and DevTools.

- Techniques: Cross-platform hotkey binding; Scoped hotkey via target; Avoid key-repeat re-triggering; Allow shortcuts inside inputs; Multi-key sequences; User-customizable shortcuts; Display shortcuts per platform; Debug registrations with DevTools
- Tools: TanStack Hotkeys (React package, alpha; vanilla JS package also available; other framework packages announced as coming), TanStack DevTools (hotkeys panel), React

## [Is This A Better Way to Use Git?](../videos/3BAhV2xpzZ8.md)
`3BAhV2xpzZ8` · Better Stack · 2026-03-02 · q3 · intro · review · also: coding-agents

A 5-minute walkthrough of GitButler, a GUI layer over Git that adds virtual branches, AI commit messages, and easier history rewriting, with an honest pros and cons take.

- Techniques: Virtual branches for parallel work on one working tree; AI-generated commit messages; Drag, squash and amend commits with undo; Open a PR from the app; Adoption path for GitButler
- Tools: GitButler (GUI and CLI, beta, free during beta per the presenter), Git, GitHub, VS Code, Claude, Cursor, MCP

## [How AI Will Transform DevOps and SRE Practices | Better Stack Podcast Ep. 12](../videos/K7y8ZAHQYGY.md)
`K7y8ZAHQYGY` · Better Stack · 2026-03-02 · q3 · practitioner · interview · also: observability, software-factory

Better Stack podcast with SRE consultant Amin Astani on how AI-written code floods CI/CD and on-call, arguing for SLOs, constrained automation and reliability incentives over AI-run production changes.

- Techniques: Error-budget decision test for SLO maturity; Compensatory automation split for production changes; Agentic first-pass alert triage with human escalation; Release-path check before scaling AI code output; Postmortem framing beyond human error; Operational excellence in performance criteria; Self-hosted CI with Concourse
- Tools: Kubernetes, Prometheus, OpenTelemetry, Claude Code (captioned as 'Cloud Code'), incident.io, Honeycomb, Scuba (Meta internal observability tool), Conveyor (Meta internal CD system), Concourse CI, Jenkins, GitHub, Nagios

## [This Makes AI Agents WAY More Powerful (just-bash)](../videos/EoyLzyJUcfI.md)
`EoyLzyJUcfI` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: sandboxing-execution, token-cost-efficiency

Short walkthrough of just-bash, a TypeScript simulated bash with an in-memory virtual filesystem for agents, and how wiring it into an AI SDK chat cut input tokens from 133k to 6k on one JSON query.

- Techniques: Virtual bash tool for an agent; Mount files into a virtual workspace; Include the package's agent instructions; Restrict outbound network with a curl allowlist
- Tools: just-bash (TypeScript simulated bash with in-memory virtual filesystem), bash-tool package (AI SDK bash tool built on just-bash), AI SDK, GPT-5.2 (model used for the chat demo, as named by the presenter), jq, Python 3 (inside just-bash), SQLite (inside just-bash), curl (inside just-bash, host whitelist), head

## [Native Worktrees Just Killed Traditional Claude Code Workflows](../videos/lj_xZn-Yf18.md)
`lj_xZn-Yf18` · Better Stack · 2026-03-02 · q3 · practitioner · review · also: claude-code, coding-agents, multi-agent

A 4-minute walkthrough of Claude Code's native git worktree support: run parallel feature branches in isolated worktrees, resume them by name, and use worktree-isolated subagents, with a note on a recent breakage.

- Techniques: Parallel feature branches with named worktrees; Isolate a broken feature and ship the rest; Return to or resume a worktree; Open a shell in a worktree directory with tmux; Worktree isolation for custom subagents; Clean up temporary worktrees
- Tools: Claude Code, Claude Desktop, git, React, tmux, Claude Squad, React Doctor, SVN, Jujutsu

## [I Replaced Notion, Linear, and Slack With One Tool (Huly)](../videos/gGKtoykrNYA.md)
`gGKtoykrNYA` · Better Stack · 2026-03-02 · q2 · intro · review · also: infra-cost-scaling

Walkthrough of Huly, a self-hosted open-source all-in-one workspace (tasks, docs, chat, calendar, GitHub sync) pitched as a replacement for Notion, Linear, Slack and GitHub. Short, shallow demo; the speaker judges it good but flags RAM and setup costs.

- Techniques: Self-host an all-in-one workspace in Docker; Two-way GitHub issue sync into a project board; Link specs, tasks and code in one place
- Tools: Huly (captioned as Hooli), GitHub, Docker, Notion, Linear, Slack, TypeScript

## [Vite, Rust & The Future of JavaScript Tooling | Better Stack Podcast Ep. 11](../videos/LSGZtHafiM4.md)
`LSGZtHafiM4` · Better Stack · 2026-03-02 · q4 · practitioner · review · also: coding-agents, context-engineering

Vite creator Evan You explains why the Vite toolchain is moving to Rust (Rolldown, OXC), the unified Vite+ CLI, guardrails for agent-written code, and his skepticism about React Server Components.

- Techniques: Pre-bundle dependencies in dev, serve source as native ESM; Bundle for production when module count crosses a threshold; Built-in transforms instead of plugin chains; Check the data-boundary cost before offloading to native code; Arena-allocate ASTs in one contiguous buffer; One config, one resolver for the whole toolchain; Vite+ commands and version pinning; Ship AGENTS.md and skills with the package, patched on upgrade; Guardrails against agent shortcuts in PR review; Schedule debt-paydown passes between feature pushes; Plan mode, then write AGENTS.md, and run agents in parallel; Run downstream ecosystem CI before a major release
- Tools: Vite (v7 current, v8 in beta per the speaker), Vite+ (vp CLI), Rollup, Rolldown, esbuild, webpack, Rspack, SWC, OXC (parser, resolver, transformer, minifier), oxlint, oxfmt, Vitest (auto-caption 'VTest')

## [AI, Terminal Tools & Building a Supportive Developer Community | Better Stack Podcast Ep. 10](../videos/SwYENemHJp4.md)
`SwYENemHJp4` · Better Stack · 2026-02-02 · q2 · intro · interview · also: coding-agents

Better Stack podcast ep. 10: guest Bash Bunny (ex-Charm) on switching to Doom Emacs and org mode, Sway and Linux, and a case for limiting AI in hobby work; mostly anecdote.

- Techniques: Ease into Vim motions with VS Code Vim keybindings, then VimTutor; Doom Emacs command discovery via M-x; Org mode task basics; End-of-day brain dump, one dated file per day; Keep inline completion on, but write the code yourself; Scoped AI questions, then implement by hand; Learn an OSS feature by reading its introducing PR; Trust filter for OSS learning sources; Docs-first, then tweak and break the example; Remote development from a Mac into a Linux machine; Time-boxed MVP with visible pain points
- Tools: Neovim, Vim, VimTutor, Doom Emacs, Emacs, LazyVim, LunarVim, Org mode, Notion, Obsidian, Trello, Cursor

## [Docker’s Best Security Feature Is Now FREE](../videos/AcCJ678kV34.md)
`AcCJ678kV34` · Better Stack · 2026-02-02 · q2 · intro · news · also: security-guardrails

Docker is making its Docker Hardened Images (DHI) free and Apache 2.0 licensed, pitching minimal, patched base images as a supply-chain fix; a short announcement-style explainer with no benchmarks.

- Techniques: Swap the base image for its hardened equivalent; Explicitly install only needed tools during the build; Start Kubernetes deployments from hardened Helm charts
- Tools: Docker, Docker Hardened Images (DHI), Debian, Alpine, Helm, Kubernetes, Apache 2.0 license

## [This Framework Might Be the FUTURE of Cross-Platform Apps (Dioxus)](../videos/bDwr_7n1AZg.md)
`bDwr_7n1AZg` · Better Stack · 2026-02-02 · q2 · intro · tutorial · also: —

Better Stack walkthrough of Dioxus, a Rust UI framework that targets web, desktop, iOS and Android from one codebase, ending with a small Chuck Norris joke app that fetches from a REST API.

- Techniques: Dioxus project bootstrap and multi-target dev loop; Props and hot-reload behaviour; Fetch JSON into a typed struct with reqwest and serde; Component state with a fetch-on-click and fetch-on-mount
- Tools: Dioxus (0.7 cited), dx (Dioxus CLI), Rust, wasm32 toolchain, RSX, Tailwind CSS, Radix UI, Dioxus native GPU renderer (name unverified in captions), Bevy, reqwest, serde, Chuck Norris joke API (unnamed REST endpoint)

## [Astro is Joining Cloudflare (Here's Why)](../videos/vpbNP4loCiE.md)
`vpbNP4loCiE` · Better Stack · 2026-02-02 · q2 · intro · news · also: vibe-coding-app-building

Astro, the MIT-licensed framework for content-driven sites, is joining Cloudflare. The team says it stays open source, multi-host and governed the same way, and the host sees the move as a funding fix for Astro.

- Techniques: Server-rendered static HTML with islands
- Tools: Astro (6 in beta), Cloudflare (Workers), Next.js, Nuxt, Svelte, Angular, Blazor, React, Vue, Solid, Hono, TanStack

## [Stack Overflow is Dead (Here's Why)](../videos/dsfqyVYkrbM.md)
`dsfqyVYkrbM` · Better Stack · 2026-02-02 · q2 · intro · other · also: product-ux, rag-retrieval

Opinion essay (Better Stack) arguing Stack Overflow's question volume collapsed after 2014 moderation changes, was accelerated by ChatGPT, and that AI is gatekeeping public developer knowledge.
- Tools: Stack Overflow, ChatGPT, Answer Overflow, Discord, Slack, Reddit, Apollo (third-party Reddit app, mentioned as shut down)

## [Tailwind is Dying... (this is bad!)](../videos/YIRugFtqBsM.md)
`YIRugFtqBsM` · Better Stack · 2026-02-02 · q2 · intro · news · also: vibe-coding-app-building, product-ux

A Better Stack commentary on a Tailwind CSS maintainer's refusal to review an LLMs.txt PR, arguing AI is eroding docs traffic and the paid products that fund open source.

- Techniques: Publish an LLM-optimized docs endpoint (LLMs.txt); Tie docs funnel to paid products, and track docs traffic against usage
- Tools: Tailwind CSS, Tailwind Plus, Tailwind v4, LLMs.txt, npm, ShadCN, Laravel, Sidekiq, Elastic, Redis, Anthropic, OpenAI

## [This Keyboard Tool is BETTER Than Karabiner (Here's Why)](../videos/YKjl2f5-ZSE.md)
`YKjl2f5-ZSE` · Better Stack · 2026-02-02 · q3 · practitioner · review · also: —

Kanata, an open-source Rust keyboard remapper, adds tap-hold, layers and home-row mods at the software level. The speaker prefers it to Karabiner Elements for home-row mods, despite its Lisp-style config and some gaps.

- Techniques: Basic key remap with def src and def layer; Tap-hold for one key; Home-row mods via def var; Extra named layers with a layer-switch key; External integration through the TCP server
- Tools: Kanata, Karabiner Elements, Karabiner for Mac, QMK, SketchyBar, MX Master (mouse), Rust

## [The Free Open Source Jira Killer Devs Love](../videos/pgWHATQzkHk.md)
`pgWHATQzkHk` · Better Stack · 2026-02-02 · q2 · intro · review · also: product-ux

Short hands-on review of Plane, an open-source, self-hostable issue tracker pitched as a Jira/Linear alternative. Covers Docker self-hosting in about two minutes and the cloud-only AI features, with honest notes on paywalls.

- Techniques: Self-host Plane with Docker; Enable AI in a self-hosted or cloud workspace
- Tools: Plane, Docker, Kubernetes (optional self-host path), curl, nano, OpenAI API, React, TypeScript, Django, PostgreSQL, Redis, Jira

## [Ship LLM Apps Locally with Dify](../videos/V-YvJdZx6sY.md)
`V-YvJdZx6sY` · Better Stack · 2026-02-02 · q2 · intro · review · also: agent-architecture, rag-retrieval

Better Stack's short walkthrough of Dify, a self-hosted visual builder for LLM apps (RAG, chained prompts, agents), with a file-summarization demo and a candid list of drawbacks.

- Techniques: Branch a workflow on input file type; Add a model provider via Settings; Run Dify locally with Docker; Choose between visual builder and code orchestration
- Tools: Dify, LangChain, LlamaIndex, n8n, OpenAI API, Google Gemini, Docker, Vercel, Supabase, ReAct agent pattern

## [I Tried Agentic AI from the Terminal... Here’s What Actually Works](../videos/KRT-7xK97WQ.md)
`KRT-7xK97WQ` · Better Stack · 2026-02-02 · q2 · intro · review · also: agent-architecture

Short hands-on look at ASI-1's new Python CLI for its agent API: it works in scripts and keeps session state, but the pip-installed mode drops context, and the API is hard to find.

- Techniques: Script-wrapped agent CLI with a remembered session; Test the agent in the script path before trusting it in automation; Pick the invocation mode by whether state must persist
- Tools: ASI-1 CLI, ASI-1 API, ASI-1 (agentic model platform), Python, pip

## [Could This Framework Replace Flask, Django, and FastAPI? (Reflex)](../videos/9QmH6DDyLCQ.md)
`9QmH6DDyLCQ` · Better Stack · 2026-02-02 · q3 · intro · tutorial · also: vibe-coding-app-building

Better Stack walkthrough of Reflex, a pure-Python full-stack web framework; builds a counter, list, conditional and async fetch app, then concludes it is a React wrapper and not worth it over React for the frontend.

- Techniques: Reflex project bootstrap; State class with event handlers; Render lists with rx.foreach; Conditional rendering with rx.cond; Async handler with intermediate yield; Load data on page load; Inspect the compiled output
- Tools: Reflex, Reflex Build, Python, pip, httpx, asyncio, React, Vite, Tailwind CSS, React Router, Random Useless Facts API, Databricks

## [Radix is a problem...](../videos/TLUWRThKijg.md)
`TLUWRThKijg` · Better Stack · 2026-02-02 · q3 · practitioner · review · also: vibe-coding-app-building

Better Stack argues against Radix UI in favor of Base UI, a headless React component library from the original Radix/Floating UI/MUI creators, comparing render props, data-driven collections, multi-select, and function-based styling.

- Techniques: Migrate asChild to the render prop; Function-as-render-prop for state-aware rendering; Function className with variant libraries; Data-driven collections via the root; Enable multi-select on Select
- Tools: Radix UI, Base UI, React Aria, shadcn/ui, Tailwind CSS, tailwind-variants, CSS Modules, React Hook Form, TanStack Form, Material UI, Floating UI, React

## [jQuery 4 FINALLY released... (What!?)](../videos/HNp8naNxS0w.md)
`HNp8naNxS0w` · Better Stack · 2026-02-02 · q2 · intro · news · also: —

Better Stack walkthrough of jQuery 4, the first major release since 2016: dropped browsers, ES module source, removed utilities, focus-order fix, and a 19.5 KB slim build.

- Techniques: Gate an upgrade on your browser matrix; Consume jQuery as an ES module in the bundler; Prefer the slim build when you do not need the removed extras; Replace utility calls with platform code; Move deferred chains to promises and simple animations to CSS
- Tools: jQuery 4, jQuery 5 (announced future release, no details given), jQuery slim build, Webpack, V (auto-caption error, likely Vite), React, WordPress, Internet Explorer 10 and 11, Edge Legacy, Firefox, Android browser

## [1 in 9 Apps Ship Supabase Keys: Here’s How It Happens](../videos/pE6A3bHLM4o.md)
`pE6A3bHLM4o` · Better Stack · 2026-02-02 · q3 · intro · tutorial · also: security-guardrails

Public-prefixed env vars (NEXT_PUBLIC_, VITE_, PUBLIC_) ship into the client bundle, so a private Supabase key behind one leaks to every visitor; the fix is server-side calls, bundle checks and CI guardrails.

- Techniques: Audit the shipped build for secrets; Proxy privileged calls through your own server; Enable and test RLS on user-facing tables; Review rule for public-prefixed variables; CI secret scanning as a build gate; Rotate on suspicion
- Tools: Supabase, Next.js, Vite, SvelteKit, Chrome DevTools, npm

## [This Free Whisper App Runs Fully Offline (No Cloud, No API)](../videos/-Z-Clxo-v-g.md)
`-Z-Clxo-v-g` · Better Stack · 2026-02-02 · q2 · intro · review · also: local-ai

Quick walkthrough of Buzz, a free open-source desktop and CLI app that runs Whisper transcription and translation fully offline, with an honest list of its drawbacks.

- Techniques: Fully offline transcription with Buzz; Word-level timestamps from JSON output; Foreign-language audio to English from the CLI; Scripted batch of transcription scenarios
- Tools: Buzz, OpenAI Whisper, Python, GitHub

## [Security in 2026 Is Going to Look Very Different](../videos/__izQwBMqw0.md)
`__izQwBMqw0` · Better Stack · 2026-02-02 · q2 · intro · news · also: security-guardrails

Better Stack's 2026 security outlook: record CVE counts, AI-accelerated exploits, memory-safe languages and smaller dependency surfaces, with a product plug for its monitoring tool.

- Techniques: Input sanitization against XSS and SQLi; Minimize third-party plugins and dependencies; Choose memory-safe languages for new code; Automated behavioral anomaly detection
- Tools: WordPress, Rust, Go, Java, C#, Python, Swift, C, C++, Linux kernel, React (React-to-Shell exploit, as named in the video), Better Stack (AI error tracking, AI SRE)

## [React’s Worst Vulnerability Ever (RCE Exploit Explained)](../videos/iV48tEiHFDY.md)
`iV48tEiHFDY` · Better Stack · 2026-01-02 · q3 · intro · news · also: security-guardrails

Explainer on the critical unauthenticated RCE in React Server Components (React2Shell, CVSS 10) affecting React and Next.js servers. Main takeaway: upgrade now, since WAF rules are not a full fix.

- Techniques: Patch React and Next.js before anything else; Guard property lookups in any deserializer or path resolver; Audit for dynamic path traversal on untrusted input
- Tools: React, React Server Components, React Flight Protocol, Next.js, Node.js, Cloudflare WAF, AWS

## [How Crypto Is Secretly Taking Over Banking with @SarahBensonCodes  | Better Stack Podcast Ep. 8](../videos/taTXejPts4E.md)
`taTXejPts4E` · Better Stack · 2026-01-02 · q2 · intro · interview · also: mcp-and-tools, enterprise-adoption

Better Stack podcast with Sarah Benson (Amber Data) on crypto vs Web3, tokenized real-world assets and smart-contract basics. Mostly opinion, with a short note on exposing data to LLMs via MCP.

- Techniques: Start a smart contract from an audited template; Expose analytics data to agent LLMs via MCP plus semantic tags; Private permissioned chain for institutional settlement; Vet a Web3 project before trusting it; Full-build tutorial structure
- Tools: Solidity, Rust, Forge (Foundry), Hardhat, React, TypeScript, web3.js, ethers.js, Thirdweb, Polymarket, pump.fun, Canton Network

## [This Tool Turns Claude Into an Automation Engine (ActivePieces)](../videos/K_6IYK2cIqs.md)
`K_6IYK2cIqs` · Better Stack · 2026-01-02 · q2 · intro · review · also: mcp-and-tools, infra-cost-scaling

Quick review of ActivePieces, a self-hostable, MIT-licensed Zapier/Make alternative whose integrations are also exposed as MCP servers; shallow demo, with the Claude angle mostly asserted rather than shown.

- Techniques: Self-host ActivePieces with Docker; Start from a template in New flow; Build a flow from scratch: trigger, AI step, sink; Expose automation pieces to Claude Desktop through their MCP URL
- Tools: ActivePieces, Docker, Claude Desktop, Claude, Cursor, MCP, Zapier, Make.com, Gmail, OpenAI, Notion, VPS

## [The ONLY package manager you'll ever need for macOS](../videos/tKqBLvjka8o.md)
`tKqBLvjka8o` · Better Stack · 2026-01-02 · q2 · intro · tutorial · also: —

A short walkthrough of using Nix with nix-darwin and nix-homebrew to manage packages, Mac App Store apps and macOS defaults declaratively, as a possible replacement for Homebrew.

- Techniques: Install nix-darwin from a flake; Declarative packages with rebuild; Mac App Store and cask apps via nix-homebrew; macOS system defaults in Nix
- Tools: Nix, nix-darwin, darwin-rebuild, nix-homebrew, Homebrew, Determinate Nix installer, Nix shell, Neovim, Zellij, Mackup (spoken as 'MacUp'), mise (spoken as 'Mez'), Vim

## [Building a One-Man Empire with AI & the Future of Developer Education | Better Stack Podcast Ep. 9](../videos/XG6ToBSg2HU.md)
`XG6ToBSg2HU` · Better Stack · 2026-01-02 · q3 · practitioner · interview · also: coding-agents, infra-cost-scaling, data-engineering

Better Stack podcast with solo developer David Flanagan (Raw Code Academy) on running a one-person, AI-assisted business: Cloudflare automation, LLM transcript correction, Kubernetes vs serverless cost trade-offs, QEnv and Dagger.

- Techniques: LLM-assisted transcript correction loop; Cron-driven content publishing on Cloudflare Workers; Spec-first delegation to coding agents; Hierarchical env with secret references (QEnv); Per-package CI definitions in a monorepo; Dagger pipelines in TypeScript; Cost-inflection planning for hosting; Reproducible machine via NixOS config
- Tools: Cloudflare Workers, Cloudflare R2, Cloudflare D1, Cloudflare service bindings, Gemini 3, Claude Code, Codex, Droid (multi-model agent CLI), Deepgram Nova 3, Whisper, ElevenLabs, Bluesky

## [I Tried TanStack AI... (it's good)](../videos/sdL6bF74t68.md)
`sdL6bF74t68` · Better Stack · 2026-01-02 · q3 · intro · review · also: mcp-and-tools

Hands-on flyby of TanStack AI (alpha): server-side streaming chat, a typed useChat client hook, and isomorphic tool definitions wired to web search. The speaker finds little that differs from Vercel's AI SDK.

- Techniques: Typed server chat route with stream response; Client useChat hook with server-sent events; Shared tool definition for server execution and client typing
- Tools: TanStack AI (alpha), Vercel AI SDK, OpenAI adapter, Anthropic adapter, Gemini adapter, Ollama (captioned as 'Alarma'), OpenRouter (no adapter yet), React, Solid, Vanilla JS client, Svelte (planned), GPT-5

## [I Let AI Argue About a Stock](../videos/ce3_LzVm2Jg.md)
`ce3_LzVm2Jg` · Better Stack · 2026-01-02 · q2 · intro · tutorial · also: multi-agent, agent-architecture

Better Stack demo of Trading Agents, an open-source Python multi-agent project that simulates a trading firm with LLM analyst agents and a bull/bear debate; a quick CLI walkthrough with cost and non-determinism caveats.

- Techniques: Role-specialized analyst agents plus adversarial bull/bear debate; Scripted run instead of CLI; Model-agnostic setup
- Tools: Trading Agents (open source Python project, multi-agent trading simulation), LangGraph, OpenAI API, Alpha Vantage API, Yahoo Finance, Anthropic API, Google models, Conda, Python 3

## [This Open-Source Auth Stack Might Replace Auth0 (Ory Kratos)](../videos/cvJKfqZrtgI.md)
`cvJKfqZrtgI` · Better Stack · 2026-01-02 · q3 · intro · tutorial · also: security-guardrails

Tutorial on self-hosting Ory Kratos, an open-source identity server, in Docker and wiring it to a Next.js app with prebuilt Ory Elements login, signup, verification, settings and 2FA screens, pitched as an Auth0 alternative.

- Techniques: Kratos local dev stack via Docker Compose; Kratos YAML checklist for localhost; Next.js integration with Ory Elements; Enabling 2FA through the built-in settings page
- Tools: Ory Kratos, Ory Elements, Ory Next.js integration package, Ory Hydra, Ory Keto, Ory Polis, Ory Oathkeeper, Docker, Docker Compose, Next.js, SQLite, Auth0

## [Shadcn is now PERFECT for Vibe Coding (v2 changes)](../videos/sIvYbCZzAts.md)
`sIvYbCZzAts` · Better Stack · 2026-01-02 · q2 · intro · review · also: vibe-coding-app-building

Walkthrough of shadcn v2: a new visual customizer, Base UI as the component core instead of Radix, and a one-prompt comparison showing that AI-built UI looks better when constrained to shadcn components.

- Techniques: Customizer-first scaffold for vibe-coded UI; Constrain AI generation to a component library; Use the shuffle button and open the customizer in a second tab; Migrate v1 to v2 by copying components (unverified)
- Tools: shadcn/ui (v2), Base UI, Radix UI, Tailwind CSS, TanStack Start, bun, components.json, Tabler Icons, Lucide, Hugeicons, Phosphor, JetBrains Mono

## [Claude Cluster is Insane… Upgrade Your Claude Code Workflow ](../videos/V-xBaFveTvA.md)
`V-xBaFveTvA` · AI LABS · 2026-01-02 · q2 · intro · review · also: claude-code, multi-agent, coding-agents

AI LABS walkthrough of Claude Code background subagents, using git worktrees to run parallel agents on isolated branches, plus a few changelog features. Hype title, sponsored segment, and shallow on mechanics.

- Techniques: Background a research or review subagent; Parallel review fan-out; Worktree-per-agent via a custom slash command; Named project agents via --agent flag; Fork a session on resume; Keep background tasks isolated and named
- Tools: Claude Code (background agents, tasks command, --agent flag, resume flag, custom slash commands, instant auto-compact, prompt suggestions), git worktree

## [It Happened Again... 2 New React CVE's](../videos/N1Dyym6WH7o.md)
`N1Dyym6WH7o` · Better Stack · 2026-01-02 · q3 · intro · news · also: security-guardrails

Better Stack walks through two new React and Next.js vulnerabilities disclosed after the React Server Components RCE the week before: a high-severity denial of service and a medium-severity leak of server action source code, both triggered by a single crafted POST, with the earlier patch not covering them.

- Techniques: Verify the patched version before trusting an earlier fix; Test a staging deployment for hang-on-request behavior; Keep secrets out of server action source; Treat neighbors of a fixed bug as suspect
- Tools: React, Next.js, React Server Components, React Flight Protocol, Server Actions, GitHub Security Advisories

## [This Is What React Apps Should Look Like...](../videos/aKZOjku1pyg.md)
`aKZOjku1pyg` · Better Stack · 2026-01-02 · q3 · intro · review · also: —

A short walkthrough of Vike, a modular meta-framework on Vite, as a lighter alternative to Next.js for React apps, covering per-page rendering, islands, and type-safe server functions, with an honest list of drawbacks.

- Techniques: Per-page rendering modes in a single Vike app; Islands for incremental framework migration; Telefunc server functions in place of API routes; Edge deployment through Photon
- Tools: Vike, Vite, React, Vue, Solid, Next.js, Zod, TanStack Query, Telefunc, Photon, Cloudflare Workers, Vercel

## [This Tiny Linux Setting Fixed My Next.js Builds (Swap)](../videos/HU5CV64vLg4.md)
`HU5CV64vLg4` · Better Stack · 2026-01-02 · q3 · intro · tutorial · also: infra-cost-scaling

Tutorial on fixing out-of-memory Next.js builds on a 1 GB DigitalOcean droplet by adding swap files and capping the Node heap, instead of upscaling the server.

- Techniques: Diagnose swap and disk before creating a swap file; Create and activate a swap file; Stack extra swap files to reach a larger total; Lower the Node heap cap to match swap; Set a swap budget against steady-state use
- Tools: Next.js, Node.js, pnpm, npm, create-payload-app (pnpx create payload app@latest), Payload CMS, SQLite, DigitalOcean droplet, Ubuntu, fallocate, mkswap, swapon

## [Django 6.0 Just Changed Everything](../videos/JCRu3zyMz54.md)
`JCRu3zyMz54` · Better Stack · 2026-01-02 · q3 · intro · review · also: —

Django 6.0 adds a built-in tasks API for background jobs: you define and enqueue tasks, but there is no worker, retry system or scheduler. It suits simple offload work, not a Celery replacement.

- Techniques: Declare tasks with the task decorator and context injection; Enqueue after the DB commit; Status endpoint over stored result IDs; Keep task arguments JSON-serializable; Adopt on Django 5 via the backport, then migrate
- Tools: Django 6.0, Django Tasks (django.tasks module), Django Tasks backport for Django 5, Celery, Huey, RQ, Redis (community adapters), Django tasks worker (separate process, referenced generically)

## [10 NEW CSS Features You Need To Know For 2026](../videos/svqu6FDiMAs.md)
`svqu6FDiMAs` · Better Stack · 2026-01-02 · q3 · intro · news · also: —

Better Stack walkthrough of ten CSS features it calls new for 2026 (corner shapes, shape(), styleable select, scroll markers, scroll-state queries, stretch, text trimming, sibling-index(), if(), custom functions), each positioned as replacing a JavaScript or hack-based pattern.

- Techniques: JS-free carousel with scroll markers and scroll buttons; Scroll-state container queries instead of scroll listeners; Native select styling with appearance: base-select; CSS-only staggering with sibling-index(); Trimming text whitespace for alignment; Inline conditionals with if(); Reusable logic with CSS custom functions; Using stretch for full box-model fill; Shapes with shape() on clip-path
- Tools: CSS, clip-path, offset-path, path() (compared against shape()), shape(), corner shapes (bevel, notch, scoop, squircle), appearance: base-select, ::picker and picker icon, ::scroll-marker and scroll-marker-group, scroll-button pseudo-element, container-type: scroll state, stretch keyword

## [Anthropic Just Bought Bun?!?!](../videos/UOpzufhECNg.md)
`UOpzufhECNg` · Better Stack · 2026-01-02 · q2 · intro · news · also: coding-agents

News recap of Anthropic's acquisition of the Bun JavaScript runtime, drawn from the two companies' blog posts; Bun will power Claude Code and the Agent SDK while staying MIT-licensed.
- Tools: Bun, Claude Code, Claude Agent SDK, Node.js, Factory AI, OpenCode

## [Run AWS Locally with Docker (LocalStack)](../videos/jz7oq-Viwew.md)
`jz7oq-Viwew` · Better Stack · 2026-01-02 · q2 · intro · tutorial · also: testing-verification, sandboxing-execution

Short intro to LocalStack, a Docker-based AWS emulator. The main takeaway is to use it for the inner dev loop and CI, and still verify critical paths on real AWS.

- Techniques: Point AWS SDK, CLI and IaC at a local emulator; Ephemeral LocalStack in CI; Split test tiers: emulator for the inner loop, real AWS for critical paths
- Tools: LocalStack, Docker, AWS CLI, AWS SDKs, Terraform, AWS CDK, Serverless Framework, Testcontainers, Homebrew (brew), AWS Lambda, Amazon S3, Amazon DynamoDB

## [SQL Used to Be Mandatory… But Not Anymore (Here’s the Shift)](../videos/nTRzoISgDpo.md)
`nTRzoISgDpo` · Better Stack · 2025-12-02 · q2 · intro · tutorial · also: data-engineering

Beginner tutorial arguing Python developers can skip raw SQL by using SQLModel, an ORM that combines SQLAlchemy and Pydantic, while still learning SQL basics.

- Techniques: Model-as-table with SQLModel; Object-based insert and fetch instead of raw SQL; Drop to raw SQL when needed
- Tools: SQLModel, SQLAlchemy, Pydantic, FastAPI

## [React Is Falling Behind: How Astro Creates Blazing FAST Sites in Minutes](../videos/sNhRsQSPn5Q.md)
`sNhRsQSPn5Q` · Better Stack · 2025-12-02 · q2 · intro · tutorial · also: —

Better Stack walkthrough of a Markdown blog built with Astro, showing how Astro ships near-zero JavaScript and hydrates a single React component only when it is visible.

- Techniques: Island-style partial hydration; Markdown posts with front matter; Tag pages from front matter; Quick Astro blog setup as shown; Compare load behavior in DevTools
- Tools: Astro, VS Code Astro extension, React, Markdown, npm, Chrome DevTools, Lighthouse

## [Why Leaving React Was Remix 3's BIGGEST Gamble (That Paid Off)](../videos/ZXcQR2jZL8s.md)
`ZXcQR2jZL8s` · Better Stack · 2025-12-02 · q2 · intro · review · also: —

A 4-minute first look at Remix 3's experimental React-free reactivity, components, events, frames and server roots, with the presenter saying it is not production-ready and not clearly a payoff.

- Techniques: Counter component with plain state and manual re-render; Press handling via the on prop; Custom interaction with dispatched events; Frames for route-keyed partial updates; Server root function
- Tools: Remix 3 (experimental, 'jam' dist-tag), Vite, React, Ripple, SolidJS, Alpine Ajax, Node, Bun, Cloudflare, TypeScript, Remix Jam 2025 talks

## [The Ripple UI Shift: Why So Many Developers Might Replace React](../videos/ANPbRu5cWFQ.md)
`ANPbRu5cWFQ` · Better Stack · 2025-12-02 · q2 · intro · review · also: —

Short walkthrough of the Ripple UI framework: a counter, a to-do list, and a FastAPI backend wired through a Vite dev proxy. The speaker concludes Ripple will not replace React yet, and offers no benchmarks for its speed claims.

- Techniques: Vite dev proxy to a Python API; track() for reactive state instead of hooks; if and for in templates instead of map
- Tools: Ripple, Vite, FastAPI, Python, Flask, Django, React, Svelte, Solid JS, app.ripple.ts

## [Meta's Tailwind Alternative Built to Scale (StyleX)](../videos/DqMwqBfawC4.md)
`DqMwqBfawC4` · Better Stack · 2025-12-02 · q3 · intro · review · also: —

Better Stack walkthrough of Meta's StyleX: CSS-like styles written in JavaScript, compiled at build time to atomic CSS, with type-safe props, design tokens and themes. Shallow intro, no benchmarks.

- Techniques: Define styles as a StyleX object; Conditional values via nested keys; Apply with stylex.props and spread; Last-wins style composition and conditionals; Type-constrained style props for components; Design tokens with defineVars; Themes with createTheme and partial overrides
- Tools: StyleX (stylex.create, stylex.props, stylex.defineVars, stylex.createTheme, StyleX styles TypeScript types; version not stated), Tailwind CSS (comparison only), Tailwind Variants (mentioned as a Tailwind add-on), Panda CSS (mentioned as an alternative), TypeScript, React, CSS custom properties

## [Meta Just Dropped a NEW Python Type Checker!](../videos/O7zP2XCs0do.md)
`O7zP2XCs0do` · Better Stack · 2025-12-02 · q3 · intro · review · also: —

Overview of Pyrefly, Meta's open-source Python type checker and language server, covering its speed claims, IDE features, mypy/Pyre migration path, and beta maturity.

- Techniques: Migrate an existing mypy or Pyre setup to Pyrefly; Adopt a type checker gradually in a large legacy repo; Share one checker config between editor and CLI; Trial a new type checker on a small project before committing
- Tools: Pyrefly (Meta, beta; version not stated), mypy, Pyre, Pyright (likely; the captions read 'Pyrite'), Pydantic v2, Django ORM, NumPy stubs, Jupyter, VS Code, PyCharm, Neovim, Vim

## [Why Bun is 7x FASTER Than NPM (Speed Secret Revealed)](../videos/rdomc8BxoSc.md)
`rdomc8BxoSc` · Better Stack · 2025-12-02 · q3 · intro · review · also: —

Walks through Bun's blog post on why its package installs are fast: fewer system calls via Zig, cache-friendly lockfile layout, and tarball extraction without buffer regrowth.

- Techniques: Cut syscall overhead with native code; Cache-friendly structure-of-arrays for parsed metadata; Preallocate decompression output from the archive trailer; Parallelize heavy install steps across cores
- Tools: Bun, npm, pnpm, yarn, Node.js, libuv, Zig, TypeScript (as the example of a large package)

## [300+ npm Packages COMPROMISED: The Shai-Hulud Worm Is Back!](../videos/ncRrh7zS1gY.md)
`ncRrh7zS1gY` · Better Stack · 2025-12-02 · q3 · intro · news · also: security-guardrails

Better Stack explains the Shai-Hulud npm worm, which steals developer secrets on install and republishes itself through maintainer accounts, and gives a short remediation checklist.

- Techniques: Credential rotation after a malicious install; Audit package.json for injected install scripts; Inspect .github/workflows for unfamiliar YAML; Harden npm publishing
- Tools: npm, GitHub, GitHub Actions workflows (.github YAML), Bun (named only as the filename the malware imitates)

## [Zod 4 is AMAZING - Here's Everything New (and whats broken!)](../videos/ZBTc0W1lWss.md)
`ZBTc0W1lWss` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: data-engineering

Better Stack's 7-minute walkthrough of Zod 4: Zod Mini for tree-shaking, z.interface, top-level z.email, z.toJSONSchema, a unified error param, and the breaking changes to plan for.

- Techniques: Switch bundle-sensitive code to Zod Mini; Use z.interface for value-optional properties and recursive types; Migrate string formats to top-level functions; Attach metadata with .meta() and export JSON Schema with z.toJSONSchema; Replace old error customization with the unified error parameter; Update error-handling code for the new ZodError; Use z.overwrite for type-preserving transforms
- Tools: Zod 4, Zod Mini, Zod 3, TypeScript, RFC5322 email rule, HTML5 email rule, Gmail email rule

## [OpenTelemetry Collector - Explanation & Setup](../videos/4ACQhkJBKyA.md)
`4ACQhkJBKyA` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: observability, infra-cost-scaling

Beginner tutorial on the OpenTelemetry Collector: receivers, processors and exporters, why to put it between apps and an observability backend, and a Docker setup that adds host and self-metrics and ships data to Better Stack.

- Techniques: Minimal collector config.yaml with OTLP in, batch, OTLP out; Per-signal pipelines with different processors; Adding a backend source token with the attributes processor; Host and self-metrics via receivers
- Tools: OpenTelemetry Collector, OpenTelemetry SDK (Node.js), OTLP (OpenTelemetry Protocol), Docker, Better Stack, Prometheus, Prometheus Remote Write exporter, Jaeger, Zipkin, VS Code, hostmetrics receiver, batch processor

## [I Found the BEST UI Library](../videos/aQB0B3a1fh8.md)
`aQB0B3a1fh8` · Better Stack · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building

A 5-minute tour of 21st.dev, a catalog of shadcn-style React component collections, showing how to install a component with the shadcn CLI or paste a copy-prompt into an AI editor to adapt it.

- Techniques: Install a registry component with the shadcn CLI; Install by copying the code manually; Use the copy-prompt button for an AI editor; Iterate on the pasted component with small prompts
- Tools: 21st.dev, shadcn/ui and the shadcn CLI, shadcn registry, Aceternity UI, Origin UI, Magic UI, Next.js, Tailwind CSS, v0, Lovable, Bolt.new

## [Superfile - AMAZING Terminal File Manager Created by a High School Kid](../videos/3LEctgQWG10.md)
`3LEctgQWG10` · Better Stack · 2025-11-02 · q3 · intro · review · also: —

Short walkthrough of Superfile, a customizable Vim-keybinding terminal file manager, covering navigation, copy/move/delete, pinning, and TOML config for themes, editor and hotkeys.

- Techniques: Install and launch Superfile; Vim-style navigation and preview; Select, yank, paste; Pin frequently used folders; Locate and edit the config; Editor handoff; Remap hotkeys
- Tools: Superfile (spf), Neovim, Homebrew, Nerd Fonts, Finder (named as the comparison), Tokyo Night theme, Blood theme

## [Shadcn's AI Elements are AWESOME (easiest way to build a chat app)](../videos/dS7hyPNvIb8.md)
`dS7hyPNvIb8` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: vibe-coding-app-building, product-ux

A quick tour of Vercel's AI Elements, shadcn-style chat components built for the AI SDK, and a claimed five-minute build of a chat app with web search and markdown rendering.

- Techniques: Install AI Elements into an existing shadcn project; Chat screen composition; Per-request web-search switch
- Tools: AI Elements (Vercel), AI SDK (Vercel), shadcn/ui, shadcn CLI, Tailwind CSS, react-markdown, react-syntax-highlighter, Prism, Perplexity (model with built-in web search), GPT-5, Claude (model, transcribed as 'ClaudeForce'), ChatGPT (named as a clone example)

## [CSS Just Got 10 New Features (and they're actually good)](../videos/DNixvXUOGhc.md)
`DNixvXUOGhc` · Better Stack · 2025-11-02 · q3 · intro · review · also: —

Better Stack walkthrough of ten recent CSS features (popover, @starting-style, interpolate-size, field-sizing, light-dark(), anchor positioning, and more) that replace JavaScript for common UI patterns.

- Techniques: Popover without JavaScript; @starting-style entry animation; Animated details disclosure; Animating to auto height and width; Content-sized form fields; Stroke behind fill text; Colour scheme aware values inline; Anchor-based tooltip positioning; Vertical centering of a block
- Tools: CSS, HTML, Popover API, @starting-style, details/summary, interpolate-size, field-sizing, paint-order, light-dark(), CSS anchor positioning, align-content, Popper.js (named as the old approach)

## [Copilot Kit Made My React App Think For Itself Using AI](../videos/rYVbw1wSnMk.md)
`rYVbw1wSnMk` · Better Stack · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, product-ux

A 5-minute walkthrough of CopilotKit, which lets a React app expose its data to an LLM, let the model change app state, and call MCP tools, with a self-hosted Express runtime.

- Techniques: Server-side runtime endpoint for the LLM key; Expose app data to the model via a readable-context hook; Let the model change app state via an action hook; Self-hosted MCP through the Vercel AI SDK MCP client; Cloud-hosted MCP as a frontend-only change
- Tools: CopilotKit, React, Vite, Tailwind CSS, Next.js, Express, Anthropic API (Claude), Composio (MCP server), GitHub (via Composio MCP tools), Model Context Protocol SDK, Vercel AI SDK (experimental MCP client), LiteLLM (mentioned as a wish, unmet)

## [Warp Terminal - 6 GAME-CHANGING Features You Need to Know](../videos/HSgHiRxsFzg.md)
`HSgHiRxsFzg` · Better Stack · 2025-11-02 · q2 · intro · review · also: coding-agents

A six-feature walkthrough of the Warp terminal (command blocks, Warp Drive, agent mode, customization), with a Better Stack sponsor segment in the middle. Light on depth, no benchmarks.

- Techniques: Save recurring commands as Warp workflows; Use notebooks as runnable Markdown runbooks; Run long commands as background blocks; Share a block for debugging; Persist a split layout with launch configurations; Keep an existing prompt framework
- Tools: Warp, Warp Drive, Starship, Powerlevel10k, zsh, VS Code, JetBrains, Cursor, Better Stack

## [Running Docker on Cloudflare is FINALLY possible...](../videos/c6TEXxpUEUw.md)
`c6TEXxpUEUw` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: sandboxing-execution, infra-cost-scaling

Better Stack walkthrough of Cloudflare Containers: deploying a Bun + ffmpeg container behind a Worker with a Durable Object, then reviewing limits, beta pricing and a Rivet/Fly cost comparison.

- Techniques: Container server behind a Worker; Durable Object container class; wrangler config for containers; Monitoring containers
- Tools: Cloudflare Containers (beta), Cloudflare Workers, Durable Objects, Wrangler CLI, Docker, Bun, ffmpeg, Rivet containers, Fly Machines (Fly.io), index.html static assets

## [Does GitHub's New MCP Server KILL Git Commands? (w/ Cursor)](../videos/3ivTdBgzMMI.md)
`3ivTdBgzMMI` · Better Stack · 2025-11-02 · q2 · intro · review · also: mcp-and-tools, coding-agents

Better Stack runs one timed repo-and-PR task through the GitHub MCP server inside Cursor, finds it about twice as slow as Git aliases and the GitHub CLI, and advises against it for simple Git work.

- Techniques: Run the GitHub MCP server in Cursor; Manual Git and PR flow with aliases (baseline); Fall back to direct git when the agent stalls
- Tools: GitHub MCP server (new, Docker-based; the older server ran via npx), Cursor (IDE with MCP settings), Docker, Git, GitHub CLI / Git aliases (baseline), NeoVim, macOS dictation feature, Supabase MCP server, Figma MCP server, Playwright MCP server

## [Neon: The FUTURE of Postgres? Branching, HTTP Queries, and More!](../videos/7KglfRnIlfc.md)
`7KglfRnIlfc` · Better Stack · 2025-11-02 · q2 · intro · review · also: infra-cost-scaling

Short Better Stack review of Neon serverless Postgres, covering scale-to-zero compute, copy-on-write branches, time travel, and an HTTP driver for edge runtimes; mostly feature claims with one Cloudflare Worker demo.

- Techniques: Per-PR or per-environment database branches; Scale-to-zero for idle databases; Query Postgres from edge runtimes over HTTP/WebSocket; Point-in-time restore and time travel
- Tools: Neon (serverless Postgres), Neon CLI, Neon serverless driver (HTTP/WebSocket to TCP proxy), Cloudflare Workers, Hono, GitHub integration, Vercel edge functions (caption reads 'cell edge functions'; the host does not name a provider)

## [TikTok built an IDE to rival Cursor - Trae AI](../videos/OKmwTv0BHwE.md)
`OKmwTv0BHwE` · Better Stack · 2025-11-02 · q2 · intro · review · also: coding-agents

Hands-on first look at Trae, ByteDance's free VS Code-based AI IDE with an agent "builder" mode, inline edit and tab completion; the host finds it not yet compelling enough to replace Cursor.

- Techniques: Scaffold a project from a builder-mode prompt; Attach context to builder mode; Screenshot-to-UI with split inputs; Inline edit for scoped changes
- Tools: Trae (ByteDance AI IDE), VS Code, Cursor, Windsurf, Claude 3.5 Sonnet, GPT-4o, Next.js, Tailwind CSS, create-next-app, JetBrains Fleet, DeepSeek

## [OpenTelemetry Sampling with Go - Simplify Chaos and Get Better Insights](../videos/WtX3Nlnjffs.md)
`WtX3Nlnjffs` · Better Stack · 2025-11-02 · q2 · practitioner · tutorial · also: observability, infra-cost-scaling

Walkthrough of OpenTelemetry sampling for logs and traces in a local Go app: collector probabilistic sampling, SDK trace samplers, and tail-based sampling with error and probabilistic policies.

- Techniques: Probabilistic log sampling in the collector; Consistent sampling across multiple collectors; Trace-correlated logs in a Go app; SDK head-based trace sampling; Collector probabilistic trace sampling; Tail-based trace sampling with policies; Error-only policy with context; Memory guard for tail sampling
- Tools: OpenTelemetry Collector, OpenTelemetry Go SDK (traces, logs), OTel slog bridge (Go log/slog), OTLP exporter, Probabilistic sampling processor (logs and traces), Tail sampling processor, Memory limiter processor, Go, FNV hash, Better Stack (sponsor, logs UI)

## [Traces vs Spans Explained (with real examples)](../videos/A-nbuPugjxo.md)
`A-nbuPugjxo` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: observability

Beginner primer on distributed tracing: a trace is one request's whole journey, spans are the units of work inside it, and the common mistake is starting new traces instead of child spans.

- Techniques: One trace per inbound request, one span per operation; Propagate trace context into every outbound call; Instrument selectively; Audit for disconnected traces; Read the trace graph and span tree in Jaeger
- Tools: Jaeger, OpenTelemetry (documentation referenced; no version stated)

## [Python Logging Made EASY with Loguru](../videos/y8qLhov8QU8.md)
`y8qLhov8QU8` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: observability

Tutorial on Python logging with the loguru package: one-import setup, reconfiguring sinks and levels, context binding, exception capture, JSON and file output, and shipping logs to Better Stack.

- Techniques: Reconfigure loguru with remove() and add(); Add contextual fields with bind() or contextualize(); Capture exceptions with logger.catch(); Switch to JSON output with serialize=True; Write to a rotated file sink; Send logs to Better Stack alongside the console
- Tools: loguru, Python, pip, Better Stack (Logtail), LogtailHandler (logtail Python package), sys.stderr

## [Tanstack's NEW Package - Tanstack DB](../videos/LH84SQ15Cho.md)
`LH84SQ15Cho` · Better Stack · 2025-11-02 · q3 · intro · review · also: —

A 7-minute alpha walkthrough of TanStack DB, a reactive client store built on TanStack Query with collections, SQL-style live queries, and optimistic mutations, plus an Electric SQL sync path.

- Techniques: Query-backed collection over an existing REST API; Electric-backed collection for local-first sync; SQL-style live query with cross-collection join; Optimistic mutation with invalidate-after-await
- Tools: TanStack DB, TanStack Query, Electric SQL, Postgres, D2TS (differential dataflow engine, named as the live-query engine), Zod, Convex (mentioned as comparable, not used)

## [Time to SWITCH...Claude Code vs Cursor debate just ended](../videos/tCy5cJRErTg.md)
`tCy5cJRErTg` · AI LABS · 2025-11-02 · q2 · intro · review · also: claude-code, coding-agents, mcp-and-tools

Walkthrough of Claudia, a build-from-source desktop GUI over Claude Code with custom agents, per-prompt checkpoints, a preview pane and GUI MCP setup, pitched as a reason to leave Cursor. Hype title; single-tool demo.

- Techniques: Read-only research subagent; Checkpoint before a risky AI change; Visual bug loop with a preview pane; Add MCP servers through a form; Build Claudia from source
- Tools: Claudia, Claude Code, Cursor, Rust, Bun, git, Next.js, shadcn/ui, Claude Pro plan ($20), MCP (stdio and SSE servers), CLAUDE.md, HTML

## [5 Deadly ENV Mistakes Everybody Makes](../videos/zLDDq1HNSgU.md)
`zLDDq1HNSgU` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: security-guardrails

Five common .env mistakes (committing secrets, undocumented projects, rewriting git history, one env file for all environments, and leaking secrets through frontend bundles) and the fix for each.

- Techniques: Commit a .env.example with variable names only; Document required env vars in the README; Respond to a leaked secret by rotating it; Separate env files per environment, selected by NODE_ENV; Use framework prefixes only for values safe to expose
- Tools: GitHub, Git (.gitignore, commit history), Next.js, Vite, React, Node.js (NODE_ENV), Supabase (publishable API key example)

## [Semantic Conventions - The SECRET to Crystal Clear Telemetry Data](../videos/ckcbPgZb3TU.md)
`ckcbPgZb3TU` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: observability

Better Stack walkthrough of OpenTelemetry semantic conventions: renaming tracers, spans, metrics and events in a small Node/Hono dice app, and keeping existing logs aligned with ECS via Vector.

- Techniques: Name tracers after the instrumentation scope; HTTP server span with semconv names; Use the standard HTTP duration metric; Format event names like attribute names; Check stability before adopting an attribute; Normalize existing logs with Vector instead of rewriting them; Use ECS as the log field reference for now
- Tools: OpenTelemetry semantic conventions, OpenTelemetry Node SDK, OpenTelemetry Logs SDK, Hono (TypeScript web framework), TypeScript, Node.js, Elastic Common Schema (ECS), Vector, Better Stack, Prometheus, PostgreSQL, Nginx

## [Warp + Neovim + Superfile: This Terminal Setup CHANGED How I Code](../videos/IGnbTs5HWvY.md)
`IGnbTs5HWvY` · Better Stack · 2025-11-02 · q2 · intro · review · also: coding-agents

A Better Stack presenter walks through a terminal-only workflow: Vim motions learned over about a month, NeoVim on top of LazyVim/NVChad, Warp as the terminal with its Agent used to maintain the NeoVim config, plus superfile, lazygit and fish. Mostly personal anecdote with a few transferable tips.

- Techniques: Vim motions bootstrap via VS Code Vim extension; Migrate from the VS Code/Cursor Vim plugin to NeoVim; Agent-maintained editor config; Terminal styling that matches the editor; Inline image previews in the terminal; Split AI roles inside the editor
- Tools: Warp (terminal, with Warp Agent), Neovim, LazyVim, NVChad, nvim-tree, mason, lualine, noice, supermaven, avante, OpenCode, VS Code Vim extension

## [I Switched from tRPC to oRPC (Here’s Why)](../videos/vl-Iir69lUA.md)
`vl-Iir69lUA` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: —

Better Stack walks through switching a Next.js app from tRPC to oRPC, covering the same procedure/router/client setup and what oRPC adds: first-party OpenAPI with Scalar docs, typed error classes, and contract-first APIs.

- Techniques: Minimal oRPC procedure with Standard Schema input validation; Router as a plain object and Next.js catch-all route; Typed client via RPC link; Public/protected procedure chain; OpenAPI route metadata and Scalar reference; Typed error definitions; Contract-first definition
- Tools: oRPC (orpc), tRPC, Next.js, Zod, Standard Schema (Valibot, ArkType mentioned), Scalar (OpenAPI reference UI), OpenAPI, TanStack Query, Vue, Svelte, Solid, Pinia Colada

## [React Router Now Supports Server Components](../videos/bTx2RTNlRoc.md)
`bTx2RTNlRoc` · Better Stack · 2025-11-02 · q2 · intro · review · also: —

Quick walkthrough of a React Router preview with React Server Components, using a toy app to show loaders, server actions and root middleware, plus the speaker's guess about Remix's future.

- Techniques: Export a server component by name instead of default; Loader for server-side data before render; Server action with the use server directive for form submits; Client-only pending UI inside a server-rendered form; Root middleware for logging and request-scoped context; Parcel setup with a virtual import behind an Express server
- Tools: React Router (preview, no version stated), React Server Components, Parcel, Vite, Express, Remix, React

## [ViewTransition: The BEST Way to Animate React Components](../videos/6oL-skHq5Tk.md)
`6oL-skHq5Tk` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: —

Short Better Stack tutorial on React's canary <ViewTransition> component: wrap elements, trigger updates with startTransition, customize the default fade, and use it with Suspense. Advises keeping router-level view transitions for existing apps for now.

- Techniques: Enable React canary for ViewTransition; Wrap a list in ViewTransition and trigger with startTransition; Replace the default fade with a CSS keyframe animation; Animate page-to-page navigation; Shared-element morph with the name prop; Animate Suspense boundaries
- Tools: React (canary), react-dom (canary), Bun, animate.css, Next.js, React Router, Browser View Transitions API (document.startViewTransition)

## [Vercel goes ALL IN on AI (Vercel Ship Recap)](../videos/idBEifQwlGI.md)
`idBEifQwlGI` · Better Stack · 2025-11-02 · q2 · intro · news · also: sandboxing-execution, infra-cost-scaling

Better Stack's 5-minute recap of Vercel Ship: AI Gateway and AI SDK v5 betas, a hosted sandbox for untrusted code with active-CPU billing, BotID, rolling releases, and several limited-beta features.

- Tools: Vercel AI Gateway, AI SDK v5, Vercel Sandbox, Fluid compute, Active CPU billing, BotID, CheckBotID, Rolling Releases, Microfrontends, Vercel Queues, Vercel Agent, Amazon Linux 2023

## [Add an Uptime Badge to ANY Website](../videos/r43TKZspxzo.md)
`r43TKZspxzo` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: observability

Better Stack walkthrough: set up uptime monitors and a status page, then build a custom status badge in Next.js that reads monitor-group status from the Better Stack API.

- Techniques: Server-side fetch of a status API; Derive a status label from monitor counts; Discover IDs from API example requests; Env config for badge; Escalation policy on uptime monitors
- Tools: Better Stack (uptime monitors, status pages, API tokens, monitor groups API), Next.js (server components), React, Tailwind CSS, curl, jq, Nextforge (Next.js template that includes a Better Stack system status component; plugged, no version given)

## [You’re Writing Vue Wrong — Use This Instead (Options vs Composition API)](../videos/XigQ813IMs0.md)
`XigQ813IMs0` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: —

Better Stack walkthrough comparing Vue's Options API and Composition API (script setup) on structure, scalability, readability, and whether mixing them is worth doing; mostly opinion with a light code walkthrough.

- Techniques: Group logic by feature in Composition API setup; Extract shared logic into composables; Use script setup for Composition API; Avoid mixing APIs in new components
- Tools: Vue.js, Vue Composition API, Vue Options API, script setup

## [Build Apps Using ONLY your Voice (WARP 2.0 is Insane)](../videos/4n7z4eb_aKU.md)
`4n7z4eb_aKU` · Better Stack · 2025-11-02 · q2 · intro · review · also: coding-agents, vibe-coding-app-building

Better Stack demos Warp 2.0's Code and Agents features by building several small web apps mostly from voice prompts, then deploys one. Mostly a demo with a few practical notes, and the title oversells it.

- Techniques: Refine-with-docs correction; Reference image plus voice prompt for UI; Auto-approve for unattended agent runs; Parallel agent panels by concern; Deploy by asking for a host, then letting the agent run it
- Tools: Warp 2.0 (Warp Code, Warp Agents, Warp Drive), Tailwind CSS (Vite plugin), Vue.js, React (mentioned only), Vanilla JavaScript, HTML5 canvas, Framer (used for the reference design), GitHub Pages, Vercel CLI (mentioned), npm, Cursor (comparison), Claude Code (comparison)

## [TypeScript 5.9: Lazy Imports Are Finally Here (and more)](../videos/BkzKn4EYjcM.md)
`BkzKn4EYjcM` · Better Stack · 2025-11-02 · q2 · intro · news · also: —

A 4-minute Better Stack news rundown of TypeScript 5.9: a cleaner tsc --init, nodenext as the new default, the import defer syntax, a stable node20 module mode, expandable hovers in preview, and a look ahead to TS 6 and a Go-based TS 7.

- Techniques: Deferred module loading with import defer; Node 20 module mode for stable Node 20 semantics; Bootstrap a tsconfig with tsc --init and rely on autocomplete
- Tools: TypeScript 5.9, tsc, Node.js 20, Node.js (nodenext module mode), TypeScript 6 (announced as transitional), TypeScript 7 (Go-based compiler, codename Corsa)

## [Go 1.24 Just RELEASED – Weak Pointers, Generic Aliases & More! (HUGE UPDATE)](../videos/cmtFI9eZ_UE.md)
`cmtFI9eZ_UE` · Better Stack · 2025-11-02 · q3 · intro · news · also: testing-verification

Better Stack's five-minute roundup of Go 1.24's new features: weak pointers, cleanup functions, a go.mod tool directive, Swiss-table maps, os.Root, testing/synctest, and more.

- Techniques: Weak-reference cache for large objects; Cleanup on unreachable objects; Executable dependencies via go.mod tool directive; Directory-confined file access with os.Root; Context-aware and self-restoring tests; Instant time-dependent tests with synctest; Iterator string splitting
- Tools: Go 1.24, weak package (weak.Make, Value), add cleanup (replaces set-finalizer), go.mod tool directive, os.Root (open-root function), testing/synctest (synctest.Run), testing.B.Loop, crypto/sha3, HKDF, PBKDF2, net/http protocols field, encoding/json zero-value tag (transcribed 'emit zero', described as omit-zero behavior)

## [SDKs, Stealth Models, and LLM Myths | Better Stack Podcast Ep. 2](../videos/w8x5Kdv-Za8.md)
`w8x5Kdv-Za8` · Better Stack · 2025-11-02 · q2 · practitioner · panel · also: models-research, security-guardrails, mcp-and-tools

Better Stack panel (Aug 2025) on the Vercel AI SDK, stealth models like Sonic, OpenAI GPT Realtime, and Anthropic's model-behavior research, with much opinion and few verified numbers.

- Techniques: AI SDK backend core plus UI hooks; Per-provider reasoning option pass-through; Explicit stack pinning in prompts; Smell-test models with known-hard setup tasks; Scenario-based goal-conflict red-teaming; Jailbreak testing with non-English or fictional framing
- Tools: Vercel AI SDK, AI Elements, Next.js, Turborepo, React Server Components, OpenRouter, vLLM, Ollama, Mastra, Sonic (stealth model; hosts suspect Grok Code Fast 1), Horizon Alpha (stealth model), GPT-5

## [UV - Every Python Developer NEEDS This](../videos/_OxoyLGmYbA.md)
`_OxoyLGmYbA` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: —

A Better Stack walkthrough of uv, Astral's Rust-based Python package and project manager, covering projects, lockfiles, inline script dependencies, uvx tools and Python version management.

- Techniques: Project bootstrap with lockfile; Targeted lockfile upgrades; Ad hoc script dependencies; Inline script metadata; Ephemeral CLI tool runs; Interpreter pinning; Legacy pip compatibility
- Tools: uv (Astral), Ruff (spoken as "rough" in the captions; described as made by Astral), pip, pip-tools, pipx, Poetry, pyenv, twine, virtualenv, pnpm (analogy), npm (analogy), Cursor

## [Mise: The BEST Way to Manage Versions of Node, Python, Go (and Much More...)](../videos/eKJCnc0t8V0.md)
`eKJCnc0t8V0` · Better Stack · 2025-11-02 · q3 · intro · review · also: —

Walkthrough of mise, a Rust polyglot tool and version manager, shown as a per-project toolchain file, with npm packages, tasks, scoped tools and shared env vars; a reasonable intro, with the narrator's own caveats.

- Techniques: Pin a repo's toolchain in config.toml; Install a CLI from the registry on a fresh box; Bump tools to latest, or pin a specific version; Install npm CLIs as mise-managed tools; Define npm-script-style tasks in config.toml; Scope a tool to a single project; Share env vars across projects with mise.toml; Split global CLIs from project dependencies
- Tools: mise (polyglot tool and version manager, written in Rust; author Jeff Dickey), zoxide, Node.js (pinned to 23, bumped to 24), Go (shown as 1.250 in the auto-captions, likely 1.25.0), npm, vitest, pm2, killport (spoken as KillPorts), React, Next.js, Vercel, asdf (compared)

## [I Played DuckDB Doom And It's ACTUALLY Good](../videos/1Q_62NigzN8.md)
`1Q_62NigzN8` · Better Stack · 2025-11-02 · q2 · intro · review · also: data-engineering

Better Stack demo of a Doom-like raycasting game whose 3D rendering runs entirely as DuckDB SQL queries in the browser (WASM); a stunt that shows how far an embedded analytical DB can be pushed, not a practical recipe.

- Techniques: Recursive CTE as a ray-march loop; Game state as tables, render as views; Timer-driven full-query refresh; Distance-based glyph shading; Embedded DuckDB WASM from a CDN
- Tools: DuckDB, DuckDB WASM, SQL, Node.js, ClickHouse, BigQuery, Docker Compose, Cursor (editor), CSS

## [LazyGIt - A Faster, Easier Way to Use Git on Terminal & NeoVim](../videos/A6F_8ajlrYQ.md)
`A6F_8ajlrYQ` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: —

Better Stack's 7-minute tour of lazygit, a keyboard-driven terminal UI for git, covering hunk staging, commits, push, reset, merge, conflict resolution and squashing.

- Techniques: Launch lazygit inside a repo; Create and switch branches; Hunk-level staging; Commit and skip hooks; Push a new branch with upstream; Recover from a diverged branch; Merge with squash options; Resolve conflicts by hunk; Squash a range of commits; Toggle full-screen and commit graph view
- Tools: lazygit, git, Homebrew, Neovim

## [NuShell - A New Type of Shell](../videos/nbbVJGNxnic.md)
`nbbVJGNxnic` · Better Stack · 2025-11-02 · q3 · intro · review · also: —

A walkthrough of Nushell, a shell and programming language where every command emits structured data, so you can sort, filter, convert and explore pipelines by column type instead of by text.

- Techniques: Sort and reverse typed columns; Filter a command's table with where; Convert output to another format; Use $in when a command does not take piped input; Build complex pipelines interactively with explore; Discover commands and examples from the shell; Run Nushell alongside your existing shell
- Tools: Nushell (nu), Homebrew, PowerShell (mentioned for comparison only), ls, sort-by, reverse, describe, processes, where, first, find, any

## [Docker Image BEST Practices - From 1.2GB to 10MB](../videos/t779DVjCKCs.md)
`t779DVjCKCs` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: infra-cost-scaling

Better Stack walkthrough that shrinks a React/Node Docker image from 1.2 GB to 10 MB using Alpine bases, layer ordering, .dockerignore, single-RUN cleanup, multi-stage builds and the slim tool.

- Techniques: Switch to a minimal base image variant; Dependency-first layer ordering; .dockerignore to trim the build context; Do cleanup in the same RUN as the install or build; Multi-stage build: build in one stage, serve from a small stage; Inspect layers and minify with Dive and slim
- Tools: Docker, Dockerfile, Node.js (node:latest, node alpine variant), npm, React, Nginx, Alpine Linux, Distroless (Google), Python, Kubernetes, Dive, Slim (slim build, x-ray, lint)

## [Meta Just Changed Data Compression FOREVER (OpenZL Explained)](../videos/_BsjI3IUtlg.md)
`_BsjI3IUtlg` · Better Stack · 2025-11-02 · q2 · intro · review · also: data-engineering, infra-cost-scaling

Better Stack explainer of Meta's open-source OpenZL: format-aware compression with a per-format plan and one universal decoder. The claimed gains are on structured data, from a single Meta test.

- Techniques: Schema-first format description with SDDL; Offline plan training over reversible transforms; Evolve the compression plan without redeploying the decoder
- Tools: OpenZL (Meta, open source, no version stated), SDDL (Simple Data Description Language, OpenZL schema format), ZStandard (ZSTD, used as the fallback backend and as the speed baseline), GZip (named as a general-purpose baseline)

## [Why Crush Is the Best‑Looking AI Coding CLI (RIP Claude Code?)](../videos/kCcCxzCSf_w.md)
`kCcCxzCSf_w` · Better Stack · 2025-11-02 · q2 · intro · review · also: coding-agents, claude-code

A short hands-on look at Charm's Crush, a terminal AI coding CLI, compared against Claude Code and OpenCode on one React app prompt. It looks polished, but it trails on features and only supports API keys.

- Techniques: Same-prompt cross-CLI comparison; Permission modal: allow for session; Init a project memory file; Keyboard navigation in Crush; Configure LSPs and MCP servers in crush.json; Check where generated apps put API keys
- Tools: Crush (Charm terminal coding agent), OpenCode (original project, later renamed to Crush), OpenCode (SST, TypeScript version), Claude Code, Claude Sonnet 4, OpenAI Whisper API, Vite, React, LSP servers, MCP servers, crush.json, CRUSH.md

## [The BEST Way To Use Claude Code Anywhere (Thanks To Levelsio)](../videos/N434yhINnHo.md)
`N434yhINnHo` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: coding-agents, claude-code

Better Stack walkthrough for running Claude Code on a cheap always-on Hetzner server and driving it from a phone via SSH or Mosh in Terminus or Termux.

- Techniques: Always-on remote Claude Code host; Terminus SSH host setup (iOS/Android); Termux setup (Android); Mosh for roaming and reconnects; Docker isolation for the agent
- Tools: Claude Code, Hetzner, Node.js, NVM, Terminus, Termux, Termux Style, OpenSSH, fish shell, Mosh, Docker, GitHub

## [Portainer will CHANGE the way you use Docker!](../videos/CelLibFSDoo.md)
`CelLibFSDoo` · Better Stack · 2025-11-02 · q2 · intro · review · also: observability

Quick tour of four self-hosted Docker web UIs (Portainer, Dockge, Dozzle, Yacht) with a verdict: Portainer for general container management, Dozzle for log viewing, avoid Yacht; includes a Better Stack sponsor read.

- Techniques: Run Portainer CE as a container for a web UI; Install Dockge with extra Docker Desktop directories; Merged multi-container logs in Dozzle
- Tools: Portainer (Community Edition), Docker, Docker Desktop, Docker Compose, Dockge, Dozzle, Yacht, Uptime Kuma, Nginx (sample Compose app in Dockge demo), Vector, Better Stack, AWS EC2

## [This Framework Replaces Your ENTIRE Backend (Motia)](../videos/xvwY4ZKklrc.md)
`xvwY4ZKklrc` · Better Stack · 2025-11-02 · q3 · intro · review · also: agent-architecture, observability

Better Stack walks through Motia, a framework that runs APIs, cron jobs, background tasks and AI steps in one runtime built from small "step" files, and demos a four-step tweet pipeline.

- Techniques: One file per step (config + handler); Event chaining between steps; Cron polling of pending work in shared state; Trace-ID-keyed status endpoint; Manual triggering from the dashboard or curl
- Tools: Motia, OpenAI GPT-4, Bluesky, Better Stack, TypeScript, Python, curl

## [This Single Line of Code Saves 440GB a WEEK](../videos/V6qjdQhe3Mo.md)
`V6qjdQhe3Mo` · Better Stack · 2025-11-02 · q2 · intro · news · also: —

A one-line PR that inlined a micro-package cut about 440 GB/week of npm bandwidth, and the video uses it to argue about micro-libraries, supply-chain risk and copy-paste versus dependencies.

- Techniques: Inline a tiny dependency; Replace with a native check; Find redundant dependencies with eslint-plugin-depend
- Tools: npm, to-regex-range, is-number (v7 per the video), chokidar, isOdd, isEven, ansi-colors, left-pad, polyfill.io, eslint-plugin-depend, E18E (Ecosystem Performance Initiative)

## [Vector vs OpenTelemetry Collector - The Ultimate Observability Showdown](../videos/uRA7qee4Frg.md)
`uRA7qee4Frg` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: observability

Hands-on comparison of Vector and the OpenTelemetry Collector on three tasks: nginx log structuring, Docker metrics to Prometheus, and traces to Jaeger. Vector wins logs and metrics; OTel handles traces better but is harder to set up.

- Techniques: Vector nginx log structuring; OTel Collector nginx log parsing; Docker metrics to Prometheus via OTel Collector; Docker metrics to Prometheus via Vector; Traces to Jaeger via OTel Collector
- Tools: Vector, Vector Remap Language (VRL), OpenTelemetry Collector, Docker, Docker Compose, Nginx, Prometheus, Jaeger, telemetry-gen (OpenTelemetry telemetry generator), Better Stack, Datadog Agent (mentioned only as a hypothetical source), OTLP

## [10 Chrome DevTools Tricks You Didn't Know! (3rd is Crazy)](../videos/EAxdMoyKf5Y.md)
`EAxdMoyKf5Y` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: observability

A 7-minute, beginner-level tour of ten Chrome DevTools tricks: local overrides, keyboard shortcuts, focus emulation, node screenshots, the animation editor, network throttling, styled console logs and AI assistance.

- Techniques: Persist page edits with local overrides; Keyboard navigation of DevTools; Keep focus-dependent UI open for inspection; Capture screenshots from DevTools; Edit CSS animations in the Animations panel; Simulate slow networks; Style console output with %c; Ask the built-in AI assistant
- Tools: Chrome DevTools, Chrome, Google Docs, ChatGPT (mentioned in passing as a comparison)

## [WebAssembly vs AWS Lambda vs Cloudflare Workers: Which Actually Performs Best?](../videos/5vCGMrYadBI.md)
`5vCGMrYadBI` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: infra-cost-scaling, sandboxing-execution

Better Stack runs one TypeScript app on Fermyon Spin (WebAssembly), Cloudflare Workers and AWS Lambda, comparing latency, recursion limits, sandbox behavior and resource use. Workers win on JS speed, Wasm has the smallest footprint, and the test is small and single-region.

- Techniques: Per-minute uptime probe for latency distribution; Local warm-up timing with repeated curl; Recursion vs iteration as a stress test; Eval-injection sandbox probe; Host-level resource sampling per process; OpenTelemetry trace export from a Spin app
- Tools: Fermyon Spin (captioned 'Thermian Spin'), Fermyon Cloud (captioned 'Thermian Cloud'), Cloudflare Workers, Wrangler, workerd, esbuild, Node.js, V8 / V8 isolates, QuickJS, AWS Lambda, Better Stack uptime monitors, OpenTelemetry

## [The EASIEST Way To Switch From ESLint & Prettier to Biome — Ultracite](../videos/lEkXbneUnWg.md)
`lEkXbneUnWg` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: context-engineering, coding-agents

Better Stack walks through Ultracite, a zero-config preset that sets up Biome (a Rust linter and formatter) with AI rule files, editor settings and pre-commit hooks in one init command.

- Techniques: Zero-config Biome bootstrap; Biome config that only extends the preset; Thin CLI wrappers for lint and format; Pre-commit format gate via Husky; Shift lint rules left into the agent's context; Expose rules through an MCP server
- Tools: Ultracite (npx ultracite init, lint, format), Biome (biome check, biome check --write), ESLint, Prettier, Husky, lint-staged, lefthook, Bun, shadcn/ui, VS Code, Cursor, Zed

## [Jsonnet & Grafonnet: Automate & Scale Grafana Dashboards Like a PRO](../videos/u6git2AjoEo.md)
`u6git2AjoEo` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: observability

A five-minute tutorial on defining Grafana dashboards in Jsonnet with the Grafonnet library, so they can be version-controlled, generated and reused instead of hand-built in the UI.

- Techniques: Install the Jsonnet toolchain; Compile Jsonnet to JSON with a jpath flag; Bootstrap Grafonnet with jb; Build a time-series panel with Grafonnet helpers; Generate repeated targets with a function; Factor panels into a lib/*.libsonnet module; Use the $ and self references in Jsonnet objects
- Tools: Jsonnet, Go jsonnet, C++ jsonnet, jsonnet-bundler (jb), Jsonnet language server (VS Code), Grafana, Grafonnet, Prometheus, PromQL, Node Exporter, Grafana Tanker, Better Stack

## [Why WezTerm Beats Ghostty, Warp, and tmux COMBINED](../videos/kYBvkzwM8Iw.md)
`kYBvkzwM8Iw` · Better Stack · 2025-11-02 · q3 · intro · review · also: —

A Better Stack walkthrough of configuring WezTerm (a Lua-configured, GPU-accelerated Rust terminal) to look like Warp, rebind keys, and use its built-in remote multiplexer as a tmux replacement.

- Techniques: Minimal ~/.wezterm.lua skeleton; Warp-style visuals; Close pane without confirmation; Split bindings with domain awareness; Clear-screen binding; Fish PATH for the WezTerm CLI; Remote multiplexing without tmux; Terminal session recording with the CLI
- Tools: WezTerm, Lua (config language), fish shell, Starship, Warp, Ghostty, tmux, AeroSpace, Neovim, TokyoNight Night (color scheme, as spoken), Nerd Font (named 'Black's Mono Nerd Font' in the auto-captions), asciicast

## [Add Social Logins to Next.js in 5 Minutes (Supabase UI)](../videos/jg6XAc-hhc8.md)
`jg6XAc-hhc8` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building

Better Stack walkthrough of adding GitHub social login to a Next.js app using Supabase UI, shadcn's CLI, and a registry-installed component; mostly UI clicking through Supabase and GitHub settings.

- Techniques: Install a Supabase UI auth component via shadcn registry; Wire GitHub OAuth into Supabase Auth; Env vars from the Supabase connect dialog
- Tools: Next.js, shadcn/ui (shadcn CLI, `npx shadcn@latest`), Supabase, Supabase UI, GitHub OAuth, VS Code, Vercel (mentioned only as the look to imitate)

## [Redis 8 Makes AI Search Blazingly FAST](../videos/YwoaqLsrHew.md)
`YwoaqLsrHew` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: rag-retrieval

Short Better Stack tutorial showing Redis 8 vector sets for product similarity search in a small Express app, plus a clarification of how they differ from the Redis vector database.

- Techniques: Embed product text for similarity, then store vectors in a Redis vector set; Query neighbours by element ID with VSIM; Keep a plain cosine-similarity function as a fallback; Turn on persistence for an in-memory vector store; Choose between vector sets and the Redis vector database
- Tools: Redis 8, Redis vector sets (beta, VADD / VSIM), Redis vector database (hash or JSON storage; RediSearch / Redis Query Engine, referred to as 'ready search'), Redis vector library, Express, EJS, Docker, OpenAI embeddings API

## [The BEST Shell You’re Not Using - Fish](../videos/lzTDo1KsL-I.md)
`lzTDo1KsL-I` · Better Stack · 2025-11-02 · q3 · intro · review · also: —

Walkthrough of the fish shell's out-of-the-box features (autosuggestions, highlighting, abbreviations, history, config UI) and its main tradeoff: scripting syntax that is intentionally not POSIX.

- Techniques: Install fish and try it as your interactive shell; Regenerate completions after installing software; Define abbreviations instead of aliases; Run a private session that leaves no history; Open the web-based config UI; Port simple bash scripts to fish syntax; Keep bash scripts running under a shared shell
- Tools: fish shell, Ghostty, bash, zsh, MacPorts, WSL, grep, node

## [5 Must-Have CLI Tools in 2025](../videos/mvWYdrn7m2c.md)
`mvWYdrn7m2c` · Better Stack · 2025-11-02 · q3 · intro · review · also: —

A short walkthrough of five terminal upgrades (tldr, duf, bat, fzf, zoxide) that replace man, df, cat, history/ps lookups and cd, with the commands shown.

- Techniques: Replace man with tldr for quick command examples; Use duf for disk usage; Use bat as a cat replacement and to expose hidden characters; Build an fzf file finder with a bat preview; Search shell history and processes with fzf; Replace cd with zoxide
- Tools: tldr, man, duf, df, bat, cat, fzf, zoxide, ps, git, history, Docker

## [Leaving AWS to Build a Better Redis w/ Roman Gershman (Dragonfly Co-Founder)](../videos/tXdDddCgGnE.md)
`tXdDddCgGnE` · Better Stack · 2025-11-02 · q3 · intro · interview · also: infra-cost-scaling

Founder interview with Dragonfly's co-founder and CTO Roman Gershman on why he left AWS ElastiCache to rewrite Redis from scratch, plus the license and language choices behind it.

- Techniques: Rewrite the core instead of forking when the bottleneck is architectural; Keep the wire API for ecosystem compatibility; Time-delayed source-available license; Stay hands-on with the community
- Tools: DragonflyDB, Dragonfly Cloud, Dragonfly Swarm (announced by host, not detailed), Redis, Redis API, AWS ElastiCache, KeyDB (captions read it as KDB; the reference is inferred, not stated), Lua scripting, C++, Rust, Visual Studio Code, GitHub Copilot

## [Hotwire Spark for Ruby on Rails — Hot Reloading… FINALLY!](../videos/b7SWkjgcuMU.md)
`b7SWkjgcuMU` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: —

One development-only gem, Hotwire Spark, gives Rails hot reloading for HTML, CSS and Stimulus edits. Under JS bundling, HTML and Stimulus changes fall back to a full page visit.

- Techniques: Install Hotwire Spark in a Rails app; Expect import-maps update semantics; Plan around full visits under JS bundling
- Tools: Hotwire Spark, Ruby on Rails, Bundler (bundle command), Gemfile, Turbo (Turbo visit), Stimulus, Import Maps, Hotwire Live Reload (mentioned as an alternative), Vite Ruby (full reload, mentioned as an alternative), Vim (aside about keybinds)

## [Why Your Applications NEED Distributed Tracing](../videos/E956jBlMKcA.md)
`E956jBlMKcA` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: observability

Intro to distributed tracing: why logs and metrics fall short for microservices, what traces and spans are, and a Node.js demo sending OpenTelemetry data through an OTel Collector to Jaeger.

- Techniques: Collector-based OTLP export to Jaeger; Instrument a Node.js app with an instrumentation file; Add custom span attributes, events and exceptions for debugging; Trace search for root-cause isolation
- Tools: OpenTelemetry, OpenTelemetry Collector, Jaeger, Zipkin, Docker, Node.js, Express, OTLP (OpenTelemetry Protocol)

## [Has This Just Made Every Other Performance Optimization Obsolete?](../videos/5n9JjFRdeh4.md)
`5n9JjFRdeh4` · Better Stack · 2025-11-02 · q2 · intro · review · also: —

Better Stack demos Foresight.js, a 5KB framework-agnostic library that preloads links and images from predicted mouse movement, then argues it should come only after cheaper performance fixes.

- Techniques: Intent-based preload via register/unregister; Tune trajectory prediction live in the debugger; Enlarge hit slop for early triggering; Compare preload strategies under throttled network; Performance ordering
- Tools: Foresight.js, TanStack Router, Next.js, React Router, React, Vue, Svelte

## [Why I Love TanStack Router](../videos/WADPOyv15MA.md)
`WADPOyv15MA` · Better Stack · 2025-11-02 · q3 · intro · review · also: —

A 12-minute Better Stack tour of TanStack Router: full type safety across links, params and search params, file-based routing, and loaders wired to TanStack Query.

- Techniques: File-based routing with generated boilerplate; Validate path params in the route definition; Validate search params with defaults and let the URL be state; Loader prefetch into React Query via router context; Not-found and auth redirects in the route definition; Link active state and preloading; Code splitting
- Tools: TanStack Router, TanStack Query (React Query), TanStack Start, Zod, React, Solid, TypeScript

## [Build an AI Video Generator Like Sora (with ComfyUI)](../videos/DxvC2B0eVkc.md)
`DxvC2B0eVkc` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: local-ai, voice-multimodal

Step-by-step tutorial for running ComfyUI on a rented DigitalOcean GPU droplet, chaining an OmniGen2 text-to-image workflow into a WAN video workflow, and serving the export through ViewComfy over SSH tunnels.

- Techniques: Remote GPU with SSH-tunneled ComfyUI; Downloading models into the path the workflow expects; Chain text-to-image into image-to-video; Shared prompt node across two text encoders; Export ComfyUI workflow as API JSON and run it in ViewComfy; Cost control for rented GPU droplets
- Tools: ComfyUI, comfy-cli, DigitalOcean GPU Droplets, NVIDIA RTX 4000 Ada, WAN video generation model (speaker says 2.25B parameters, auto-caption), OmniGen2, ViewComfy, Next.js, pip3, SSH

## [Dokku - Is This FREE Heroku Clone Better Than The Original?](../videos/J8gPLpcgUOs.md)
`J8gPLpcgUOs` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: infra-cost-scaling

Walkthrough of Dokku, a Docker-based single-server Heroku alternative: create a $6 DigitalOcean droplet, git-push deploy a Node app, add subdomain routing and a linked Postgres database.

- Techniques: Provision a Dokku droplet from the DigitalOcean marketplace; Create the app and deploy with git push; Enable subdomains on an IP with nip.io and vhost routing; Add a linked Postgres database; Inspect and debug with Docker commands
- Tools: Dokku, Docker, Heroku buildpacks, Procfile, DigitalOcean droplet, Nginx, Let's Encrypt (Dokku plugin), nip.io, PostgreSQL, Dokku Postgres plugin, Node.js, node-postgres client

## [Docker + Django: Containerize the Right Way with Nginx, Postgresql & Gunicorn](../videos/1v3lqIITRJA.md)
`1v3lqIITRJA` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: infra-cost-scaling

Better Stack tutorial on running Django in production with Docker: gunicorn instead of runserver, nginx serving static files, a multi-stage non-root Dockerfile, and Postgres wired together with docker-compose.

- Techniques: gunicorn as the app server with entrypoint script; Environment-driven settings.py with two env files; Static file serving through a shared volume and nginx; nginx config with mime types, static alias and reverse proxy; Multi-stage Dockerfile with cache-friendly ordering and non-root user; docker-compose three-service stack; .dockerignore with env files first
- Tools: Django, Docker, Docker Compose, Gunicorn (version 23 as stated), Nginx, PostgreSQL, Python 3.13-slim (base image), python-dotenv (load_dotenv for local dev)

## [This Next.js Server Actions Pattern is AWESOME (Validated & Authenticated Actions)](../videos/pBQ-WlhiGbw.md)
`pBQ-WlhiGbw` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: security-guardrails

Tutorial on two reusable wrapper functions for Next.js server actions: one validates FormData with Zod, the other also checks a Better Auth session before the action runs.

- Techniques: Validated server-action wrapper; Auth-checked server-action wrapper; Front-end consumption of ActionState
- Tools: Next.js (server actions, headers()), Next.js SaaS starter kit, Zod, Better Auth, TypeScript, React useActionState hook

## [Monitoring Made EASY with Grafana and Prometheus!](../videos/pGSkPutCKtQ.md)
`pGSkPutCKtQ` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: observability

Step-by-step Docker Compose setup of Prometheus, node_exporter and Grafana to chart host CPU and root-disk usage, with a sponsored Better Stack plug.

- Techniques: Compose file for a host-metrics stack; Minimal prometheus.yml; Verify the scrape in Prometheus before Grafana; Add Prometheus as a Grafana data source; CPU utilization panel; Root disk usage panel; Dashboard layout and iteration
- Tools: Grafana, Prometheus, node_exporter (Prometheus Node Exporter), Docker, Docker Compose, PromQL, Better Stack (hosted, sponsored mention)

## [Google Just Released the ULTIMATE AI SDK (And It's Good)](../videos/Ksac1CuaBvQ.md)
`Ksac1CuaBvQ` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: voice-multimodal

A short Better Stack walkthrough of Google's new Gen AI JavaScript SDK for Gemini: one client for text, image and video analysis and generation, plus the speaker's complaints about API design, model access and cost.

- Techniques: Single client, method per modality; Poll-then-download for video generation; Express plus Multer upload endpoint; OpenAI SDK pointed at Gemini for text
- Tools: Google Gen AI SDK for JavaScript (Gemini API), Gemini, Veo 3 (said as VO3; the transcript caption is unclear), Express, Multer, Vertex AI, OpenAI SDK, Replicate, Google Search grounding

## [Everyone HATES Frameworks?!? - State of JavaScript 2024](../videos/6vXC-kxTGfI.md)
`6vXC-kxTGfI` · Better Stack · 2025-11-02 · q2 · intro · review · also: —

A Better Stack walkthrough of the State of JavaScript 2024 survey: demographics, feature usage, framework/meta-framework/runtime sentiment, pain points and AI tool usage.

- Techniques: Rank tools by sentiment among users, not only by usage; Track usage and sentiment over survey years together
- Tools: JavaScript, TypeScript, React, Vue, Angular, Svelte, Solid, Next.js, Astro, Nuxt, Gatsby, Jest

## [The Last Authentication Library You'll Ever Need...](../videos/hFtufpaMcLM.md)
`hFtufpaMcLM` · Better Stack · 2025-11-02 · q3 · intro · review · also: security-guardrails

Better Stack walkthrough of BetterAuth, an open-source TypeScript auth framework: an overview of its frameworks, databases, auth methods and plugins, then a live Next.js + Drizzle + Postgres setup for email/password and GitHub login.

- Techniques: Minimal BetterAuth config for email/password plus GitHub; Generate the auth schema with the CLI, then push with Drizzle; Mount a single catch-all auth route; Enable the nextCookies plugin for server actions; Email sign-up and login from a server action; Protect a server-component page by session; Sign out and social sign-in from a client component
- Tools: BetterAuth, Next.js, Drizzle ORM, Postgres, Docker, shadcn/ui, Zod, GitHub OAuth, Kysely, Hono, Express, Expo

## [React's NEW Activity Component Explained](../videos/MeYCmCqnG3o.md)
`MeYCmCqnG3o` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: —

Walks through React's experimental Activity component, which hides a subtree while keeping its state and pre-rendering it, compared with conditional rendering and CSS hiding. Practical for tab UIs, with caveats.

- Techniques: Replace conditional rendering with Activity for tab-like UIs; Put media playback in an effect with cleanup; Compare the three approaches before choosing
- Tools: React, React Activity (unstable_Activity, experimental React build), React Strict Mode, CSS (display toggling), Cursor

## [Watchtower -The PERFECT Docker Automation Tool?](../videos/GHeZaoUpVcQ.md)
`GHeZaoUpVcQ` · Better Stack · 2025-11-02 · q2 · intro · review · also: infra-cost-scaling

A short walkthrough of Watchtower, a Docker tool that auto-updates and restarts containers, with the host's view that it suits homelabs but not production, where monitor-only alerting is safer.

- Techniques: Watchtower as a sidecar compose service; Excluding Watchtower from itself; Monitor-only mode with Slack alerts; Digest-based change detection
- Tools: Watchtower, Docker, Docker Compose, Docker Hub, Slack (webhook notifications)

## [Svelte's Next Big Change? (server components soon?)](../videos/nQB9iRijqBY.md)
`nQB9iRijqBY` · Better Stack · 2025-11-02 · q2 · intro · review · also: —

Short walkthrough of Rich Harris's experimental Svelte async branch, which lets components use top-level await, await in $derived and in templates, and hints at future server components.

- Techniques: Top-level await in a component script behind a boundary; Await a promise inside $derived; Await inside template expressions; Start independent requests together to avoid waterfalls
- Tools: Svelte (experimental async branch), SvelteKit, Svelte 6 (expected destination, not released)

## [Vuetify vs PrimeVue — BEST UI Framework Breakdown](../videos/CL8xW84S-lA.md)
`CL8xW84S-lA` · Better Stack · 2025-11-02 · q2 · intro · review · also: —

Better Stack compares Vuetify (opinionated, Material Design, polished out of the box) with PrimeVue (unstyled, highly customizable, pairs with Tailwind) for Vue.js projects.

- Techniques: Vuetify global theme setup; PrimeVue unstyled mode with pass-through attributes; Tailwind for layout on top of PrimeVue; Build from scratch for a strongly branded UI
- Tools: Vue.js, Vuetify, PrimeVue, Tailwind CSS, Material Design, ChatGPT (mentioned as a help source)

## [Build Your Own Shadcn/ui](../videos/_JqUWzI0AXA.md)
`_JqUWzI0AXA` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: vibe-coding-app-building

Better Stack walkthrough of publishing your own components and blocks as a shadcn registry: registry.json, npx shadcn build, hosted JSON installed by URL, plus v0 and theme hooks.

- Techniques: Registry folder layout; registry.json item entries; Build to hostable JSON; Install into another project; Compose a block from registry dependencies; Open a registry item in v0; Distribute a theme through the registry
- Tools: shadcn/ui CLI (npx shadcn build, npx shadcn add), Next.js, React Aria Components, v0 (v0.dev), TweakCN, Cursor (mentioned as writing the remaining primitives from the first one), Supabase UI (transcript says 'Superbase UI'; mentioned as a shadcn-style collection), GitHub (mentioned as a possible host for the JSON)

## [Take Back Your PRIVACY and Run DeepSeek on EC2 in 5 Minutes!](../videos/DCWtyd9AW4w.md)
`DCWtyd9AW4w` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: local-ai, infra-cost-scaling

Step-by-step tutorial for running distilled DeepSeek (Qwen-based) models on a CPU-only AWS EC2 instance using Ollama, Open WebUI in Docker, and an Nginx reverse proxy, framed around keeping prompts private.

- Techniques: Run Ollama in Docker with a persistent volume and a published port; Open WebUI as a front end for a Docker-hosted Ollama; Nginx reverse proxy from port 80 to a local app port; Pick a quantization level by tradeoff
- Tools: AWS EC2, Amazon Linux, Docker, Ollama, Open WebUI, Nginx, Caddy (mentioned, not used), DeepSeek (distilled models, Qwen-based per the speaker), Qwen (distilled base for the 1.5B and 7B models), vim / nano

## [Cloudflare Just Made AI Agents WAY Easier (Agents SDK)](../videos/l4tHKJFQvRg.md)
`l4tHKJFQvRg` · Better Stack · 2025-11-02 · q3 · intro · review · also: agent-architecture, infra-cost-scaling

Better Stack demos Cloudflare's Agents SDK starter: durable-object agents that persist state, sync across browsers, schedule tasks and pause for human approval. Demo-driven, with no benchmarks.

- Techniques: Single shared agent for multi-window sync; Per-user or per-workflow agent routing; Chat agent setup; Persisting UI state; Human-in-the-loop tool approval; Scheduling tasks from chat
- Tools: Cloudflare Agents SDK (starter template), Cloudflare Durable Objects, Cloudflare Workers AI, AI SDK (used for tools and model calls), AIChatAgent (Agents SDK base class for chat), useAgent (React hook from the SDK), React, WebSocket, Hono (official middleware mentioned), OpenAI-compatible API schema (for model choice)

## [Setup Centralized Logging with Rsyslog](../videos/JocDslKu3j4.md)
`JocDslKu3j4` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: observability

Six-minute Better Stack tutorial on centralizing Linux logs with rsyslog: enable TCP reception on a collector, forward from clients over TCP 514, and verify with logger.

- Techniques: Enable TCP syslog reception on the collector; Forward all logs from a client with one rule; Verify forwarding end to end
- Tools: rsyslog, syslog, systemctl, ufw, nano, logger, ss, hostname, Ubuntu, Better Stack

## [The BEST Way to Log in Node.js - Winston](../videos/He7Dc6DuxdI.md)
`He7Dc6DuxdI` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: observability

Node.js Winston logging tutorial: JSON logger setup, env-driven levels, default and child metadata, error stacks, exception and rejection files, then shipping logs to Better Stack.

- Techniques: Minimal Winston logger; defaultMeta for service-wide fields; Child logger for request or scope metadata; Logging errors with stack traces; Separate files for crashes and rejections; Ship logs to Better Stack via Logtail
- Tools: Winston (Node.js logging library), Node.js, pnpm, Bun, jq (pretty-printing JSON output in the terminal), Better Stack (hosted log search; Telemetry Sources), Logtail Node client and Winston transport (@logtail/node, @logtail/winston, inferred from spoken names)

## [Deno 2 vs Bun: Which Should You Choose?](../videos/m6hlrk2Jwrw.md)
`m6hlrk2Jwrw` · Better Stack · 2025-11-02 · q2 · intro · review · also: —

Better Stack compares Deno 2, Bun and Node.js: shared web-standard APIs and tooling, Deno's deny-by-default security and built-in stdlib, Bun's speed and drop-in Node compatibility, with a pick-by-use-case verdict.

- Techniques: Adopt Bun as a package manager in an existing package.json project; Run a file with hot reloading in Bun; Use Deno's permission model to limit what dependencies can do
- Tools: Node.js, Deno 2, Bun, JSR (Deno registry), npm, pnpm, V8, WebKit JavaScriptCore, Rust (Deno implementation language), Zig (Bun implementation language), ESLint, Prettier

## [STOP Using Docker Compose. Switch to Kubernetes in 6 Mins (With Kompose)](../videos/cyGF_PLBx4c.md)
`cyGF_PLBx4c` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: infra-cost-scaling

Tutorial that converts a two-container Docker Compose app to Kubernetes manifests with Kompose, runs it on a local kind cluster, and fixes two first-deploy failures (image pull policy and ClusterIP).

- Techniques: Convert Compose to Kubernetes manifests with Kompose; Create a local kind cluster with exposed ports; Load a locally built image into kind; Inspect a kind node's images with docker exec; Fix pulls of :latest-tagged local images by setting imagePullPolicy; Expose a Service on a fixed host port with NodePort; Check cluster state with kubectl get all
- Tools: Docker Compose, Kompose (auto-caption reads it as 'Compose'), kubectl, kind, Kubernetes, Docker, nginx, Bun, Minikube, Docker Desktop, Homebrew, Docker Swarm

## [MASTER Apache Kafka in just 8 minutes to Build Real-Time Apps](../videos/feKBnsvO2Pk.md)
`feKBnsvO2Pk` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: data-engineering, infra-cost-scaling

Beginner Kafka tutorial: topics and pub/sub, disk-backed replayable events, brokers and KRaft, then a two-producer, two-consumer Python log demo run through Docker Compose and uv.

- Techniques: Local single-node Kafka via Docker Compose in KRaft mode; Minimal Python producer writing to a topic; Minimal Python consumer printing a topic; Replay a topic from the beginning; Run Python producers and consumers with uv in separate tabs
- Tools: Apache Kafka, Docker Compose, Python, uv, ZooKeeper (named as the replaced component), KRaft (Kafka Raft, Kafka's built-in metadata management), A Python Kafka client library (not named in the transcript), WebSockets (comparison only), Amazon SQS (comparison only), RabbitMQ (comparison only), Prometheus 3 (plug for another Better Stack video)

## [12 Logging BEST Practices in 12 minutes](../videos/I2mWnh66Bkg.md)
`I2mWnh66Bkg` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: observability, infra-cost-scaling, security-guardrails

A generic logging best-practices list: plan what to log, use levels and structured fields, sample high-volume logs, emit one canonical line per request, centralize, set retention, redact secrets, and watch logging overhead.

- Techniques: Canonical log line per request; Selective sampling; Redaction in the pipeline; Tiered retention policy; Load test logging overhead
- Tools: OpenTelemetry, OpenTelemetry Collector, Vector, Go slog (log/slog), Logrus (transcribed as Logris), Go

## [Redis vs DragonflyDB - A Faster, Modern, Drop-In Replacement?](../videos/OlsENj_LpEQ.md)
`OlsENj_LpEQ` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: infra-cost-scaling

Better Stack benchmarks DragonflyDB against Redis on one node and as Redis Cluster, finds Dragonfly several times faster on a single node, but cluster Redis closes most of the gap.

- Techniques: Single-node memtier_benchmark comparison; Redis Cluster baseline for fair comparison; Drop-in migration trial by endpoint swap
- Tools: Redis (single-node and cluster mode, redis-cli), DragonflyDB (single binary or Docker container), memtier_benchmark (load-testing tool described as Redis's), Docker, AWS EC2 (benchmark hosts, 8-core 32GB and 16-core 64GB)

## [The BEST way to Create Desktop Apps (Electron)](../videos/IzONNPX-tE4.md)
`IzONNPX-tE4` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: —

Beginner Electron tutorial: scaffold an npm project, load local HTML in a BrowserWindow, and use a preload script with contextBridge to build a simple audio player.

- Techniques: Bootstrap a minimal Electron project; Create a window and load local HTML; Preload script with contextBridge for one privileged method; Renderer-side player wiring
- Tools: Electron, npm, Figma (cited only as a web app that also ships a desktop version)

## [Why Parcel's React Server Components Is A GAME-CHANGER Sorry Next JS](../videos/mymZBLPmfLo.md)
`mymZBLPmfLo` · Better Stack · 2025-11-02 · q2 · intro · review · also: —

A 4-minute Better Stack walkthrough of Parcel's beta React Server Components: the Parcel-specific directives, the hydrate entry, server actions and fetchRSC. Still complicated, in the speaker's view.

- Techniques: Parcel RSC page entry with use server; Client bootstrap entry with use client entry and hydrate; Server actions through callServer; Fetching server component payloads with fetchRSC
- Tools: Parcel (beta, React Server Components support), React Server Components, React, Next.js, Waku, Express, Bun, Deno, Cloudflare Workers, React Static (mentioned; the captions say "React static")

## [INK: The React Library POWERING AI Terminal Tools (For Now...)](../videos/qSZwx5_EmSA.md)
`qSZwx5_EmSA` · Better Stack · 2025-11-02 · q2 · intro · review · also: coding-agents

Quick Ink (React for terminals) counter tutorial that measures its memory cost against Bubble Tea and points to OpenTUI as a leaner TypeScript alternative.

- Techniques: Ink counter component pattern; Measure the runtime footprint before choosing a TUI framework; Keep the TUI process alive until an explicit exit key
- Tools: Ink, React, TypeScript, Yoga (WASM build, flexbox layout), Bubble Tea (Go), OpenTUI (Zig and TypeScript), Bun FFI, SolidJS implementation of OpenTUI, OpenTUI core, OpenCode, Qwen Code, Gemini CLI

## [Can AI Agents Finally Automate the Web? (BrowserOS Review)](../videos/rIZ8OBHL7Zo.md)
`rIZ8OBHL7Zo` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: voice-multimodal, local-ai

Better Stack reviews BrowserOS, an open-source Chromium-based agentic browser; the built-in agent works on Gemini, but local Ollama models mostly failed the Amazon cart task.

- Techniques: Run BrowserOS's agent on a local Ollama model; Evaluate candidate models on a browser-agent task before relying on them; Customize an agent's instructions by rebuilding from source
- Tools: BrowserOS, Chromium, Chrome, Perplexity Comet, Opera Neon, Fellow AI, OpenAI Operator, Brave, Arc, Dia, Ollama, Gemini 2.5

## [React 19.2 Explained in 5 Minutes (it's awesome)](../videos/8B1Nw2ajYbM.md)
`8B1Nw2ajYbM` · Better Stack · 2025-11-02 · q3 · intro · news · also: observability

Quick tour of React 19.2's six new features: Activity for state-preserving hide/show, useEffectEvent, cache signal for aborting renders, performance tracks in Chrome DevTools, partial pre-rendering in react-dom, and an upgraded ESLint plugin.

- Techniques: Keep component state across hide/show with Activity; Read latest state inside an effect with useEffectEvent; Cancel wasted server work with cache signal; Profile React in Chrome DevTools using the built-in tracks; Enable React Compiler lint rules via the updated ESLint plugin
- Tools: React 19.2, React DOM, Chrome DevTools (Performance profiles), React DevTools (mentioned as unnecessary for the performance tracks), ESLint (react-hooks plugin, flat config), React Compiler

## [OpenTelemetry Makes Istio's Telemetry AMAZING!](../videos/76O-1qakUTM.md)
`76O-1qakUTM` · Better Stack · 2025-11-02 · q2 · practitioner · tutorial · also: observability

Walkthrough of putting an OpenTelemetry Collector between Istio sidecars and backends (Jaeger, Prometheus, console), then adding Node.js OTel auto-instrumentation to the app; short tutorial with the config described rather than shown.

- Techniques: Mesh-first telemetry baseline; Separate observability namespace; Hand-written collector config instead of the Istio sample; Enable OTLP ingest on the backends; Verify the pipeline with kubectl; Node.js auto-instrumentation in each service
- Tools: Kubernetes, Istio, istiod, Istio Ingress Gateway, OpenTelemetry Collector, OpenTelemetry Node.js auto-instrumentation, Jaeger, Prometheus, MongoDB, kubectl, Node.js, Azure

## [Dagger - The End of Slow, Messy YAML CI/CD Forever!](../videos/cwa_MBL1kek.md)
`cwa_MBL1kek` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: testing-verification, observability

Short Better Stack tutorial on Dagger: write CI pipelines as functions in Go (or Python, TypeScript, PHP), run them identically locally and in GitHub Actions, cache volumes, and debug with a terminal breakpoint.

- Techniques: Daggerize a Go project; Write a test function that runs in a container; Replace GitHub Actions YAML with a single Dagger call; Cache dependency downloads with a volume; Debug a failing pipeline interactively; Reuse modules from the Daggerverse
- Tools: Dagger, Dagger Go SDK, Dagger Python SDK, Dagger TypeScript SDK, Dagger PHP SDK, Docker, GitHub Actions, Act, Go, Alpine container image, Homebrew, OpenTelemetry

## [TypeScript 5.8 Has 2 AWESOME Features](../videos/vcVoyLQMCxU.md)
`vcVoyLQMCxU` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: —

Better Stack walkthrough of two TypeScript 5.8 changes: the Erasable Syntax Only flag, which bans runtime-emitting features so Node can run .ts files directly, and checked return types for conditional and indexed access types, demoed on the nightly build.

- Techniques: Enable the Erasable Syntax Only flag to keep code runnable without a transpiler; Conditional return type with a never fallback, typed by input generic; Overloads as the pre-5.8 fallback for conditional returns; Key-driven return type with an indexed access type; Trying TypeScript features early on the nightly build
- Tools: TypeScript 5.8 (nightly build), Node.js 23.6+ (native type stripping), ts-node, tsx

## [Why Astro 5 is a Game-Changer](../videos/kIftpNnN_8I.md)
`kIftpNnN_8I` · Better Stack · 2025-11-02 · q3 · intro · news · also: —

A 5-minute Better Stack rundown of Astro 5's headline features: the content layer, server islands, simplified output modes, astro:env, and experimental image and SVG improvements.

- Techniques: Load content from multiple sources with loaders into one collection; Server islands for personalized parts of a cached page; Per-route opt-out of prerendering in static mode; Typed, scoped environment variables with astro:env; Crop and responsive images with the Sharp service
- Tools: Astro 5, Astro content layer, Astro content collections, Astro server islands, astro:env, Sharp (default image service), Storyblok, Cloudinary, Hygraph, Markdown, MDX, JSON

## [Go's Built-in Package for Better Logging (using slog)](../videos/_mqB7LLgwgs.md)
`_mqB7LLgwgs` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: observability

A short Go tutorial on the standard-library log/slog package: JSON output, levels, typed attributes, groups, child loggers, and swappable handlers.

- Techniques: JSON logger as the process default; Set the minimum level through handler options; Typed attributes with helpers; Strict logging with LogAttrs; Nested objects with Group; Child logger for shared fields; Group the custom fields under one key; Keep call sites on slog and choose the backend in one place
- Tools: Go (log/slog standard library, Go 1.21+), log (standard library, migrated to slog output via SetDefault), go vet, zap (Uber logging library, mentioned as a possible handler backend), zerolog (mentioned as a possible handler backend), IDE (unnamed, showing vet errors)

## [K9s | The BEST Terminal UI for Kubernetes (2025)](../videos/AMUQzyPvO04.md)
`AMUQzyPvO04` · Better Stack · 2025-11-02 · q3 · intro · review · also: infra-cost-scaling

A 5-minute walkthrough of K9s, a terminal UI for Kubernetes, covering navigation, per-resource shortcuts, port-forwarding, live edits, aliases and skins. The speaker keeps kubectl for applying manifests.

- Techniques: Port-forward a pod from K9s; Edit a deployment's image or replica count live; Open a shell in a container; Command mode and filtering; Custom aliases and config; Enable image vulnerability scans (preview)
- Tools: K9s, kubectl, Kubernetes metrics server, MongoDB shell, Tokyo Night skin (community variant, linked in the video description), Dracula skin (from the official K9s skins repo)

## [Lynx: TikTok’s Blazing Fast Framework – The Next React Native Killer?](../videos/dtvbEiLy1xg.md)
`dtvbEiLy1xg` · Better Stack · 2025-11-02 · q3 · intro · review · also: —

Hands-on review of ByteDance's open-source Lynx, a web-tech (HTML/CSS/JS) mobile UI framework with a dual-threaded design; the verdict is promising but not yet a React Native replacement.

- Techniques: Keep gesture and animation handlers on the main thread; Split work for instant first frame; Embed Lynx View in a native app; Hands-on iOS trial of Lynx
- Tools: Lynx, Lynx Explorer, Lynx View, React Native, Expo, bun, iOS Simulator

## [Bun is now the ULTIMATE Frontend Toolchain? (Replace Vite)](../videos/IDHHDnWjhAc.md)
`IDHHDnWjhAc` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building

Walkthrough of Bun 1.2.3's front-end toolchain: a template picker (bun init), a built-in router in Bun.serve, module-based hot reload, auto-installed deps, and bun create from a single file. Presented as a Vite replacement, but only the dev server is shown.

- Techniques: Scaffold a React + Tailwind + shadcn/ui app interactively; Routes in Bun.serve with dynamic params; Turn a single LLM-generated component file into a project; Find and install missing imports across source files
- Tools: Bun (1.2.3 cited), React, Tailwind CSS, shadcn/ui, Vite (named as the tool being replaced), Next.js (named as an alternative the presenter is moving away from), Svelte (plugin said to be coming), Vue (plugin said to be coming), Cursor (used to write components), framer-motion (installed by the analysis step), Anthropic (chat link import idea)

## [Bun.js Just Got WAY Faster (1.2.21  Update)](../videos/ptT8mFkm7z8.md)
`ptT8mFkm7z8` · Better Stack · 2025-11-02 · q2 · intro · news · also: —

Better Stack walkthrough of Bun 1.2.20 and 1.2.21 release notes: yarn-to-bun.lock migration, faster AbortSignal timeouts and postMessage, bun test return-value matchers, unified SQL client, native YAML, idle CPU fix.

- Techniques: Migrate a yarn project to bun.lock; Assert mock return values with the three bun test matchers
- Tools: Bun 1.2.20, Bun 1.2.21, bun test, bun install, Bun SQL, bun update, bun audit, Bun.secrets, bun.lock, yarn, mysql2, Node.js

## [The BEST Terminal Just Launched - Ghostty 👻](../videos/heRfqBEhwr0.md)
`heRfqBEhwr0` · Better Stack · 2025-11-02 · q2 · intro · review · also: —

Better Stack walkthrough of Ghostty 1.0, a fast native terminal emulator; covers theme and font setup, native macOS features, quick terminal, and its standards-first approach. Mostly a feature tour with little depth.

- Techniques: Switch theme via the Ghostty CLI; Global quick terminal; Use bundled font with ligatures
- Tools: Ghostty (version 1), Zig, Metal, OpenGL, iTerm2 color schemes, JetBrains Mono, Nerd Fonts, Oh My Zsh, tmux, Kitty graphics protocol, Alacritty, Warp

## [Remix is DROPPING React (and I'm excited)](../videos/5hExNPuzMQs.md)
`5hExNPuzMQs` · Better Stack · 2025-11-02 · q2 · intro · news · also: —

Short news recap: Remix v3 is being rebuilt without React on a forked Preact, with AI-first, web-API-first, runtime-only, zero-dependency principles, and no upgrade path from React Router v7 or Remix v2.

- Techniques: Own a small runtime by forking it instead of depending on it; Build on web platform APIs instead of framework-specific abstractions
- Tools: Remix, React Router, React, Preact, Next.js

## [This AI Code Builder ACTUALLY Works (backend too!)](../videos/4ASZpNNG0f4.md)
`4ASZpNNG0f4` · Better Stack · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building

Hands-on test of AI app builders on one backend-heavy prompt; Convex's Chef produced working auth, storage and database from a single prompt, while Firebase Studio, Bolt.new (with Supabase) and v0 failed or stalled.

- Techniques: One long, feature-complete prompt, then test each feature end to end; Bring your own model key to avoid builder token markup
- Tools: Chef by Convex, Convex (backend, dashboard, file storage, auth, durable functions), Bolt.new, Firebase Studio (preview), v0, Supabase, Anthropic API (BYOK)

## [Build Docker Images 40x FASTER with This Tool (depot.dev)](../videos/Xdhtmqd8gHs.md)
`Xdhtmqd8gHs` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: infra-cost-scaling

Better Stack walkthrough of Depot, a remote Docker build service with cloud machines and shared caching, cutting one project's rebuild from 7m44s to 12s with depot build and depot bake.

- Techniques: Offload Docker builds to a remote builder with a shared cache; Point the build at a non-root Dockerfile with the file flag; Build all compose services in one remote run with depot bake
- Tools: Depot (depot.dev) CLI, depot build, depot bake, Docker, Docker Compose, Dockerfile, VS Code

## [Why Everyone’s Talking About PostgreSQL 18](../videos/rlyIa7-ow-4.md)
`rlyIa7-ow-4` · Better Stack · 2025-11-02 · q2 · intro · news · also: data-engineering

A 4-minute Better Stack recap of PostgreSQL 18's headline changes: async I/O, skip scans, upgrade-preserved planner stats, virtual generated columns, OAuth 2, and replication and checksum defaults. It is a release-notes summary with no benchmarks or SQL shown.

- Techniques: Single-statement audit of updates via RETURNING old/new; Rely on virtual generated columns for derived fields; Skip-scan-aware index reuse; Major upgrade with preserved planner statistics
- Tools: PostgreSQL 18, pg_upgrade, EXPLAIN, SCRAM, OAuth 2

## [Why Isn't Anyone Talking About This Vibe Coding Tool?](../videos/BXBwikXMb6Q.md)
`BXBwikXMb6Q` · AI LABS · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building

A walkthrough of Convex's Chef, a prompt-to-full-stack-app builder, using it to make a Splitwise clone and a tool-rental app; the main takeaways are that prompt detail up front matters and that text-only prompting is a real limitation.

- Techniques: Front-load a comprehensive prompt; Bring your own API key when quota runs out, then re-prompt; Start from a preset and adjust the prompt; Verify by walking through the core flows; Export and run locally
- Tools: Chef (Convex's AI app builder), Convex, Lovable, Supabase, Bolt.new, v0 (Vercel), ChatGPT, Anthropic API (Claude), React, TypeScript

## [GitHub MCP Server: Let AI Handle Your GitHub](../videos/TrDW2Puhw0Y.md)
`TrDW2Puhw0Y` · AI LABS · 2025-11-02 · q3 · intro · tutorial · also: mcp-and-tools, coding-agents

Step-by-step setup of the GitHub MCP server in Cursor, then a live demo of an agent creating a repo, pushing a file, cloning and searching GitHub from the chat.

- Techniques: Wrap the GitHub token in a shell script for Cursor's MCP command; Create a GitHub classic personal access token for the MCP server; Register the script as a command-type MCP server in Cursor; Smoke-test the MCP connection with a read-only query
- Tools: GitHub MCP server (GitHub's official MCP server, run through npx), Cursor (IDE, agent mode, MCP settings), npx, bash, nano, realpath, GitHub classic personal access tokens, Claude Desktop (mentioned as the server's reference client), Archon (another creator's agent-building repo, mentioned in passing)

## [Tailwind v4 Is FINALLY Out – Here’s What’s New (and how to migrate!)](../videos/ud913ekwAOQ.md)
`ud913ekwAOQ` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: —

Walkthrough of Tailwind CSS v4's release: JS config moves into CSS (@theme), auto content detection, OKLCH colors, and breaking renames, plus a live upgrade of a 130-component library with the official upgrade tool.

- Techniques: Run the official upgrade codemod; Move config into the stylesheet; Simplify the PostCSS or Vite setup; Rename changed utilities in templates; Use var() instead of theme() where possible; Use native arbitrary values without brackets
- Tools: Tailwind CSS v4, @tailwindcss/upgrade (run via npx), @tailwindcss/postcss, Tailwind Vite plugin, tailwindcss-animate, PostCSS, autoprefixer, postcss-import, Motion (JS animation library, mentioned as a consumer of CSS-variable tokens), shadcn/ui (the presenter's library is described as shadcn-like), Tailwind container queries plugin (now built in), tailwind.config.js (legacy, supported via @config)

## [Jsonnet & Grizzly: The ULTIMATE Grafana Dashboard Duo!](../videos/E1wi-8w2xdA.md)
`E1wi-8w2xdA` · Better Stack · 2025-11-02 · q2 · practitioner · tutorial · also: observability

Tutorial on managing Grafana dashboards as code with Grizzly, a CLI that watches Jsonnet source and pushes dashboard changes to Grafana live, with a short Better Stack product plug.

- Techniques: Grizzly watch loop in Docker Compose; Grafana service account token for Grizzly; Add the Grizzly library through the Jsonnet bundler; Split dashboard definitions from the main file
- Tools: Grizzly (Grafana CLI for dashboards and alerts), Jsonnet, Jsonnet bundler, Grafana, Docker Compose, Prometheus, Grafana Cloud, Better Stack

## [This Tool Codes for FREE – Here’s How to Install It!](../videos/xsJAA3vhy0E.md)
`xsJAA3vhy0E` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: vibe-coding-app-building, coding-agents

Install-and-try walkthrough of Bolt DIY, a self-hosted, free alternative to Bolt.new, driven by DeepSeek V3 through OpenRouter. The demo works for a whiteboard app, but shapes stay broken, and the title overstates what is free.

- Techniques: Clone, install and run Bolt DIY locally; Configure OpenRouter as the provider with DeepSeek V3; Set a model from the dropdown and check its voice and image support; Iterate with one bug per follow-up prompt
- Tools: Bolt DIY (bolt.diy), Bolt.new, DeepSeek V3, DeepSeek chat, deepseek-coder, OpenRouter, ShadCN UI, Claude 3.5 Sonnet, Perplexity AI, Hugging Face, pnpm, git

## [Deploying your Own Vercel in MINUTES (open-source alternative)](../videos/pjrEaRSSQck.md)
`pjrEaRSSQck` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: infra-cost-scaling

A 7-minute walkthrough of self-hosting Appwrite Sites on a DigitalOcean droplet as an open-source Vercel alternative: Git deploys, branch previews, and bundled auth, database and storage.

- Techniques: Self-host Appwrite Sites with Docker Compose; Connect Git to self-hosted Appwrite via a GitHub App; Create a site from a Git repo with framework presets; Preview-then-promote with Activate
- Tools: Appwrite (Sites, Auth, Databases, Storage, Functions, Messaging, Appwrite Cloud), Vercel (comparison baseline), Docker Compose, DigitalOcean droplet, GitHub App, React (framework preset), npm, Better Stack (logging), .env file

## [Could FOKS Be the FUTURE of Secure Git Hosting?](../videos/fIbyRfuiYXc.md)
`fIbyRfuiYXc` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: security-guardrails

Walkthrough of FOKS, an open-source, federated, Go-based alternative to Keybase for end-to-end encrypted git and key-value secrets, with post-quantum hybrid encryption and a short setup demo.

- Techniques: Set up FOKS and create a user; Create an encrypted git repo; Inspect and revoke keys; Acknowledge the single-key warning
- Tools: FOKS (Federated Open Key Service), foxctl, fox CLI, Homebrew, Go, Curve25519, ML-KEM, Keybase, YubiKey, fox.app federated server

## [Everything New in Nuxt 4 — Should You Switch?](../videos/9dI_FENApz0.md)
`9dI_FENApz0` · Better Stack · 2025-11-02 · q3 · intro · news · also: —

Better Stack's 5-minute walkthrough of Nuxt 4: the new app/ directory layout, shared data-fetch keys, a references-based tsconfig, the upgrade steps, and one module incompatibility.

- Techniques: Upgrade a Nuxt 3 app to Nuxt 4; Move app code into app/; Give shared fetch calls explicit keys with matching options
- Tools: Nuxt 4, Nuxt 3, Nuxt CLI (npx nuxt upgrade), TypeScript, tsconfig references, Next.js (referenced as the layout the change resembles), Nuxt Apollo module (disabled, incompatible), Nuxt modules

## [OpenTelemetry in Node.js - Traces, Metrics and Logs](../videos/NbVVZlSsvvM.md)
`NbVVZlSsvvM` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: observability

Step-by-step Node.js tutorial for OpenTelemetry: NodeSDK bootstrap, auto-instrumentation, manual spans, metrics and Winston logs, then switching exporters to an OTLP collector and a Better Stack backend.

- Techniques: NodeSDK bootstrap file loaded with --import; Manual span per unit of work with startActiveSpan; Attributes and events on spans; Error status plus recorded exception; Counter and histogram with the meter API; Winston logs with auto-instrumented trace context; Switch exporters to OTLP and run an OpenTelemetry Collector; Dashboard chart from a custom counter
- Tools: OpenTelemetry JS SDK (@opentelemetry/sdk-node, sdk-trace, sdk-metrics, sdk-logs, api, resources, semantic-conventions), @opentelemetry/auto-instrumentations-node, @opentelemetry/winston-transport, OTLP exporters (trace, metric, log), OpenTelemetry Collector (Docker image), Prometheus receiver (collector self-metrics), Express, Winston, tsx, Node.js (--import / --require), Insomnia (request testing), Docker

## [OpenFeature Will CHANGE How You Deploy Code](../videos/ZJzQLSfuNUI.md)
`ZJzQLSfuNUI` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: observability

A 5-minute Better Stack walkthrough of OpenFeature, a vendor-neutral feature-flag API, showing flagd flags, device-type targeting, and an OpenTelemetry tracing hook.

- Techniques: Backend OpenFeature setup with flagd; React client setup with the flagd web provider; Device-type targeting via evaluation context; Flag data on OpenTelemetry traces
- Tools: OpenFeature, OpenFeature SDK (Python), OpenFeature React SDK, flagd, flagd web provider, OpenTelemetry (traces), OpenTelemetry Collector, Docker Compose, React, LaunchDarkly, GrowthBook

## [Leap Year Bugs: From Satellites to Spreadsheets](../videos/2VtNFOaRgTw.md)
`2VtNFOaRgTw` · Better Stack · 2025-11-02 · q2 · intro · other · also: testing-verification

Better Stack walkthrough of leap-year bugs in satellites, Excel, Python, JavaScript and Zune, with the Gregorian leap-year rule and the Lotus 1-2-3 1900 bug that Excel kept for compatibility.

- Techniques: Gregorian leap-year check; Edge-case test years for date logic; Check for silent date rollover
- Tools: Python, JavaScript (Date object), Excel, Lotus 1-2-3, Zune, Claude (used to generate the buggy GPS-to-UTC example code), The Register (cited source)

## [The BEST way to use Docker on MacOS](../videos/raUJQms00xY.md)
`raUJQms00xY` · Better Stack · 2025-11-02 · q3 · intro · review · also: —

Walkthrough of OrbStack as a macOS replacement for Docker Desktop: faster startup, automatic .orb.local domains with HTTPS, a debug shell for distroless containers, Finder file access, a local Kubernetes cluster, and Linux VMs.

- Techniques: Debugging distroless or read-only containers with the OrbStack debug shell; Editing container files from macOS in place; Using automatic container domains instead of port mapping; Local Kubernetes without a registry push; Running a Linux VM alongside macOS dev tools
- Tools: OrbStack, Docker Desktop, Docker Engine, Docker CLI, Docker Compose, Kubernetes, kubectl, Homebrew, Ubuntu, nginx, Finder, Preview

## [HUGE Next.js Authorization Bypass... Are You Safe? (9.1 CVSS)](../videos/D_Tt39FEIiU.md)
`D_Tt39FEIiU` · Better Stack · 2025-11-02 · q3 · practitioner · news · also: security-guardrails

Walkthrough of the Next.js 15.2.2 middleware authorization bypass (CVSS 9.1): a client-sent internal subrequest header skips middleware, what it exposes, how it was patched, and edge mitigations.

- Techniques: Re-check auth in every data-bearing route; Strip the internal subrequest header at the edge until patched; Check the vulnerable and patched source at the release tags
- Tools: Next.js 15.2.2 (vulnerable), Next.js 15.2.3 (patched), Next.js 14 (patched line), Vercel, Netlify, Cloudflare (managed firewall rule), Replit (named in the public discussion), GitHub (source and PR review), Chrome (password warning)

## [Prisma founder is solving local-first (LiveStore)](../videos/ZW9dVJ_eFIU.md)
`ZW9dVJ_eFIU` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: agent-architecture

Prisma founder's LiveStore: a local-first, reactive-SQLite state manager with an immutable event log and git-style push/pull sync, shown via a to-do app on Cloudflare Durable Objects plus D1.

- Techniques: Schema-first LiveStore app structure; Event-sourced state with materialized projections; Reactive queries via queryDb and store.useQuery
- Tools: LiveStore, SQLite, React, Cloudflare Durable Objects, Cloudflare D1, Cloudflare Workers / WebSockets

## [Podman vs Docker in 2026: What's Really Different?](../videos/SIvoAOpXZPg.md)
`SIvoAOpXZPg` · Better Stack · 2025-11-02 · q3 · intro · review · also: sandboxing-execution

Better Stack's short comparison of Podman and Docker: Podman is a near drop-in, daemonless, rootless alternative with native pods; Docker wins on ecosystem, Swarm and maturity.

- Techniques: Group multi-container apps as Podman pods; Run containers rootless for a smaller host blast radius; Use systemd to manage container lifecycle; Run Docker and Podman side by side
- Tools: Podman, Podman Desktop, Docker, Docker Desktop, Docker Compose, Docker Swarm, Docker Hub, Kubernetes, systemd, OrbStack, Nginx, PHP

## [GSAP Is Now 100% FREE](../videos/sDdqMEHHEZ8.md)
`sDdqMEHHEZ8` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: —

Better Stack beginner walkthrough of GSAP after Webflow made GSAP and its plugins free: tweens, stagger, timelines, paused playback and ScrollTrigger scrubbing a video. No benchmarks; the main news is the pricing change.

- Techniques: Basic tween on a selector; from / fromTo / set variants; Animate a custom object property; Looping with repeat and yoyo; Stagger for ordered starts; Timeline with position parameter; Paused timeline with manual play; Scroll-scrubbed video
- Tools: GSAP, GSAP ScrollTrigger plugin, GSAP ScrollSmoother plugin, GSAP SplitText plugin, GSAP Observer plugin, GSAP Motion Path plugin, Webflow (named as the company that made GSAP free, not a tool used in the demos)

## [Goodbye HTMX: Why Alpine Ajax is My New Go-To Library](../videos/ij6pOHqfhts.md)
`ij6pOHqfhts` · Better Stack · 2025-11-02 · q3 · intro · review · also: —

Better Stack compares HTMX and Alpine Ajax on the same Express/EJS to-do app; Alpine Ajax needed no server changes and still works with JavaScript off, so the author prefers it for progressive-enhancement apps.

- Techniques: HTMX partial-swap CRUD on an EJS list; Alpine Ajax full-HTML swap, no server changes; Alpine x-data/x-model form reset after Ajax success
- Tools: HTMX, Alpine Ajax, Alpine.js, Express.js, EJS, Hono, Next.js, React, Vue

## [Bash Script BEST Practices You Need to Know, According to Google](../videos/Y_erZnIhgKg.md)
`Y_erZnIhgKg` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: —

Better Stack summarizes ten takeaways from Google's Shell Style Guide: move long scripts to Python, brace variables, prefer [[ ]], declare locals carefully, and run ShellCheck. Short recap with no code shown.

- Techniques: Move long scripts to Python; Purpose comment after the shebang; Formatting baseline; One pipeline stage per line; Brace all variable references; Arrays only for flat argument lists; Functions instead of aliases in scripts; Double brackets for conditionals; Local variables with separate command substitution; Lint scripts with ShellCheck
- Tools: Bash, Python, ShellCheck, VS Code, Google Shell Style Guide

## [Docker Containers - How Hackers Can ESCAPE Them in Seconds!](../videos/giXlSlFLKwA.md)
`giXlSlFLKwA` · Better Stack · 2025-11-02 · q3 · practitioner · tutorial · also: sandboxing-execution, security-guardrails

Shows two ways to escape misconfigured Docker containers, via a mounted Docker socket and via privileged mode or CAP_SYS_ADMIN, then lists the hardening steps (proxy, drop caps, seccomp, gVisor).

- Techniques: Avoid mounting the Docker socket into containers; Audit a container's capabilities with capsh; Replace privileged mode with specific capabilities, then add a seccomp profile; Run untrusted or agent-generated workloads under gVisor; Check Docker hardening with docker-bench-security; Move host-level metrics collection out of containers
- Tools: Docker, Docker Desktop, Docker Compose, Bun, Nginx, Vector, cAdvisor, Alpine Linux, capsh, Docker socket proxy, gVisor, docker-bench-security

## [Auto Claude is HERE… Upgrade your Claude Code Workflow](../videos/ytn0aXK2gzE.md)
`ytn0aXK2gzE` · AI LABS · 2025-11-02 · q2 · intro · tutorial · also: claude-code, testing-verification

AI LABS shows how to attach Claude Code hooks (formatter, linter, build, stop-sound) to settings.json, and how to have a general LLM draft per-language hook rules. Mostly a SwiftUI demo with a sponsor segment.

- Techniques: Post-edit hooks as hard quality gates; Feed check output back to the agent; Stop-event sound notification; Generate hooks from a rules file; Accessibility audit as a hook; Autonomous run from a task file
- Tools: Claude Code, Claude Code hooks (settings.json), ChatGPT (used to draft lint and format rules), swift-format, SwiftLint (swiftlint.yml), SwiftUI, SQLite (local database in the demo app), Prettier (example formatter for other languages), Black (Python formatter, example in the rule-to-hook walkthrough), BMAD method (mentioned as a better approach, not used), claude code rule to hook (GitHub repo, name as spoken; exact repo not confirmed), tools.md (presenter's reference file of Claude Code tools and execution points; not shown)

## [The ULTIMATE Arch Linux + Hyprland Dev Setup – Omarchy](../videos/WquApbCYgcE.md)
`WquApbCYgcE` · Better Stack · 2025-11-02 · q2 · intro · review · also: —

Better Stack walks through Omarchy, DHH's single-script setup for a keyboard-driven, developer-ready Arch Linux and Hyprland desktop, and how to install and customize it.

- Techniques: Keyboard-only desktop navigation; Scripted developer-environment bootstrap on fresh Arch; Keep personal desktop config separate from distro defaults; Turn web apps into desktop apps; Global theme switching
- Tools: Omarchy, Arch Linux, Hyprland, Wofi, Alacritty, Neovim, LazyVim, LazyGit, LazyDocker, btop, fastfetch, mise

## [Is Kafka OUTDATED? Could RedPanda Be the Future of Event Streaming?](../videos/tHXWAkJeWmA.md)
`tHXWAkJeWmA` · Better Stack · 2025-11-02 · q2 · intro · review · also: infra-cost-scaling, data-engineering

Better Stack compares Kafka and Redpanda: Redpanda wins architecture and deployment, Kafka wins ecosystem and licensing, and performance depends on the workload, per conflicting benchmarks.

- Techniques: Test Kafka-compatible brokers with existing clients; Minimal Docker Compose deployment for comparison; Benchmark on your own workload with OpenMessaging Benchmark
- Tools: Apache Kafka, Redpanda, Redpanda Console, Redpanda Connect, Kafka Connect, Kafka Streams, MirrorMaker, ZooKeeper, Docker, Docker Compose, Kafka Python client, OpenMessaging Benchmark framework

## [Vue 3.6 ALPHA is out! and it's FAST! — Vapor](../videos/FvzAvnVfgoA.md)
`FvzAvnVfgoA` · Better Stack · 2025-11-02 · q3 · intro · review · also: —

Short overview of Vue 3.6 alpha's headline feature, Vapor mode (a compiler strategy that drops the virtual DOM), with opt-in steps, a single benchmark, and alpha install caveats.

- Techniques: Opt a single SFC into Vapor; Install the Vue 3.6 alpha in an existing project; Mix Vapor and VDOM with the interop plugin; Start a new Vapor app; Confirm Vapor is active
- Tools: Vue 3.6 (alpha), Vue Vapor mode, Vue 3.5.13 (benchmark baseline), Svelte (comparison only), npm (--legacy-peer-deps), Vuetify, Vapor interop plugin, Vapor app scaffolder (create-vapor-app)

## [Vite 6 is a Game-Changer for Web Development](../videos/43iPaLSaJ6M.md)
`43iPaLSaJ6M` · Better Stack · 2025-11-02 · q2 · intro · news · also: —

A 4-minute overview of Vite 6: the experimental Environment API for running one app across Node, edge and browser runtimes with HMR, plus minor changes and VoidZero's Rust tooling.

- Techniques: Split transformation from execution for multi-runtime apps; Single-command multi-environment build
- Tools: Vite 6, Vite Environment API (experimental), Module runner, Runner transport, Rolldown, Oxc, Hono, Node.js, Cloudflare Workers, Deno, Bun, React server components

## [The BEST Type-Safe URL State Manager](../videos/t4d1cJarJqs.md)
`t4d1cJarJqs` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: —

Tutorial on nuqs, a type-safe URL search-param state hook for React frameworks. It keeps UI state in the query string so it survives refresh, bookmarks and back/forward, and covers parsing, throttling, history mode and server-component sync.

- Techniques: Install and wrap the framework adapter; Replace useState with useQueryState plus a parser; Throttle URL writes for fetch-triggering params; Choose history mode per param; Sync params to server components; Use serialize and URL keys for links
- Tools: nuqs (React URL search-param state library; version not stated), Next.js (App Router, adapter and server-component cache demo), React Router (adapter supported), Remix (adapter supported), TanStack (Router) with first-party type-safe search params, referenced but not used, Zod (JSON parsing for query params via a parser), React (useState comparison, hooks), Safari (history rate-limit example)

## [This Framework DESTROYS Next.js With 7x Faster Performance!](../videos/7gTj5RLyMXw.md)
`7gTj5RLyMXw` · Better Stack · 2025-11-02 · q2 · intro · review · also: infra-cost-scaling

Better Stack benchmarks Fastify with React (Vite SSR) against Next.js and finds a 5x gap on a local hello-page test, but only about 4% on a realistic to-do app once Vercel hosting is included. The "7x" headline comes from one maintainer benchmark.

- Techniques: Fastify + Vite SSR wiring for React; Confirm SSR before benchmarking; AutoCannon 10-second load test; Separate warm and cold start numbers
- Tools: Fastify, Fastify React (fastify-react renderer), Vite, React, Next.js, AutoCannon, Vercel, DigitalOcean, Webpack, React Server Components (discussed, not adopted by Fastify React), Nuxt, Vue

## [Warp CLI: Access the Latest AI Models Anywhere For FREE](../videos/dxvowd5bdoI.md)
`dxvowd5bdoI` · Better Stack · 2025-11-02 · q2 · intro · review · also: coding-agents, mcp-and-tools

A short walkthrough of Warp CLI, which runs Warp's saved prompts, agent profiles and MCP servers from any terminal, including headless one-shot runs for scripts and CI.

- Techniques: Headless one-shot agent run; Reuse a saved Warp Drive prompt from the CLI; Run a saved workflow with arguments; Pin model and permissions with an agent profile; Attach an MCP server to a single run; Chain prompts in a shell script
- Tools: Warp CLI (warp command, beta), Warp agent profiles, Warp Drive (saved prompts, workflows, notebooks, rules), Warp MCP servers, GPT-5, Context7 MCP server, Better Stack MCP server, WezTerm, Ghostty, iTerm, Next.js, OpenCode

## [FINALLY Say Goodbye to Unstructured Logs with Vector.dev](../videos/We7s8KFY7Qg.md)
`We7s8KFY7Qg` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: observability

A short Better Stack tutorial on turning Nginx access logs in Docker into structured JSON with Vector, using its VRL nginx parser, and printing the result as JSON.

- Techniques: Run Vector as a Compose sidecar that tails Docker logs; Parse Nginx access logs with a VRL remap transform; Debug the pipeline by formatting the last log line with jq; Use Bruno's collection runner to generate repeatable test traffic
- Tools: Vector (vector.dev), with the VRL remap language and its parse_nginx_log parser, Docker and Docker Compose, Nginx, Bun (demo API on port 3000), Bruno (API client and collection runner), jq

## [JavaScript Dates SUCK — Here's What's Replacing Them](../videos/zwFlVPdtKvE.md)
`zwFlVPdtKvE` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: —

A walkthrough of the Temporal date/time API (polyfilled today) covering the seven types, strict parsing, overflow and DST disambiguation, immutable durations, rounding and comparison, as a replacement for JavaScript Date.

- Techniques: Get current time in a chosen type; Build values with from() and explicit zone/offset; Pick the right Plain type for the data; Reject out-of-range fields; Resolve DST ambiguity explicitly; Date arithmetic with durations; Round and compare temporal values
- Tools: Temporal API (TC39 proposal), JavaScript Date object, Moment.js, Luxon, a Temporal polyfill package (name not shown)

## [Bun 1.2 is a HUGE update (its a bundler now!)](../videos/rtj-zd93Vfs.md)
`rtj-zd93Vfs` · Better Stack · 2025-11-02 · q3 · intro · news · also: vibe-coding-app-building

Walkthrough of Bun 1.2's release notes: HTML-import bundling, built-in Postgres and S3 clients, a text lockfile, Node compatibility gains, a richer test runner, and cross-compiled executables. Mostly vendor-reported numbers.

- Techniques: Serve a bundled frontend straight from Bun.serve via an HTML import; Presigned S3 URLs so the server never relays file bytes; Put dependency pins and reasons in package.json comments; Review dependency changes as text diffs; Patch a broken dependency locally and commit the .patch file; Wire CI test reporting through JUnit or LCOV output; Cross-compile a standalone executable and enable bytecode caching
- Tools: Bun 1.2, Bun.serve, Bun SQL (Postgres client), postgres.js, Bun S3 client, AWS SDK for JavaScript, Bun test, bun outdated, bun publish, Tailwind CSS, Bun Tailwind plugin, Express

## [Why Ripple.js Is The Most Interesting Framework of 2025](../videos/AnkhdbrrTlo.md)
`AnkhdbrrTlo` · Better Stack · 2025-11-02 · q2 · intro · review · also: —

A four-minute walkthrough of Ripple.js, an early-stage front-end framework with JSX-like syntax, compiled reactivity and no virtual DOM. It is a quick tour of the API, not an evaluation.

- Techniques: Component with track() and @ reads; Tracked collections for lists; Wrapper component for repeated controls; Scoped styles and effects; Sharing reactive state via context; Feeding framework docs to coding agents via llms.txt
- Tools: Ripple.js, React, Svelte, Tailwind CSS, VS Code (Ripple extension), Neovim, llms.txt, React Server Components

## [The BEST way to make NPM packages](../videos/Hf6u1RA7dTg.md)
`Hf6u1RA7dTg` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: —

Beginner tutorial on building a small npm package (a Fisher-Yates array shuffle), testing it with npm link, publishing it, and linking it to a GitHub repo.

- Techniques: Scoped npm package setup; Write the entry point and export it; Local testing with npm link; Publish a scoped package publicly; Link the npm package to source
- Tools: Node.js, npm, npm link, npm login, npm publish, npm init, Git, GitHub, npmjs.com, VS Code

## [Your Own Mini AWS in Under 30 Minutes (Incus Tutorial)](../videos/zaAtYkM24hU.md)
`zaAtYkM24hU` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: sandboxing-execution, local-ai

Better Stack walkthrough of installing Incus (a community fork of LXD) on Ubuntu to run system containers and VMs, host Ollama in a container, and set up per-customer projects with quotas.

- Techniques: Install Incus from the signed apt repo; Initialize Incus and launch a container; Launch a VM with the same command; Add a bridge network so containers can reach the internet; Run Ollama as a service in a container; Create per-tenant projects with resource limits
- Tools: Incus (version not stated), LXD (upstream fork origin), LXC (container layer), QEMU (VM layer), Ubuntu (server image and host OS), Ollama, orca-mini (small test LLM), Zabbly apt repo (Incus package source), apt, gpg, curl

## [I Switched from Zod to ArkType (Here's Why)](../videos/Jgcs9SPupI0.md)
`Jgcs9SPupI0` · Better Stack · 2025-11-02 · q3 · practitioner · review · also: —

Walkthrough of ArkType as a Zod replacement for TypeScript runtime validation: TS-style schema syntax, editor-visible errors, built-in constraints, custom narrow validators, morphs, and pattern matching. The "up to 100x faster" claim is not benchmarked on screen.

- Techniques: Define a schema with string-syntax types; Validate and branch on errors; Add constraints inline with keywords and ranges; Custom validator with narrow and a custom message; Parse and transform with morphs; Pattern matching on runtime types
- Tools: ArkType (called 'archetype' in the captions; version 2.1 mentioned for pattern matching), Zod (comparison baseline), TypeScript, npm, ArkType VS Code extension (published by ArkType), Error Lens (VS Code extension), tRPC, React Hook Form, Hono

## [Expo, AI, and the Future of Mobile Development with Beto | Better Stack Podcast Ep. 6](../videos/kIU7rdHz2XE.md)
`kIU7rdHz2XE` · Better Stack · 2025-11-02 · q3 · practitioner · interview · also: vibe-coding-app-building

Expo developer advocate Beto on React Native in 2025: safe OTA updates with EAS Update, prebuild instead of eject, store submission, and the Flutter-vs-RN debate. Vendor-side anecdotes, little AI content.

- Techniques: Ship JS-only fixes with EAS Update and expo-updates; Check native compatibility before each OTA bundle; Prebuild instead of ejecting; Iterate in Expo Go, then switch to a dev build; First store submission with Expo Launch; Add widgets, Live Activities and Apple Watch targets with Apple Targets; Generate app icons from one source image with SnapAI
- Tools: Expo, Expo Launch, Expo Go, EAS Update, expo-updates, Expo UI, Expo Router, Expo API routes, Expo modules (native module API), React Native, React Native Skia (Shopify), React Native macOS and Windows (Microsoft)

## [The BEST Way To Start a Project (Better-T-Stack)](../videos/CWwkWJmT_zU.md)
`CWwkWJmT_zU` · Better Stack · 2025-11-02 · q2 · intro · review · also: vibe-coding-app-building, coding-agents

A Better Stack walkthrough of Better-T-Stack, a scaffolder that builds a full TypeScript monorepo (TanStack Router, Hono on Bun, oRPC, Postgres, Drizzle, Better Auth) from one command, with auth working on first run.

- Techniques: Scaffold a full-stack TS monorepo from a builder; Bring up the stack locally; First-run smoke test of the full path; Hand the scaffold to a coding agent
- Tools: Better-T-Stack (scaffolder with website Builder and CLI), TanStack Router, Hono, Bun, oRPC, tRPC (listed as an alternative API layer), PostgreSQL, Docker / Docker Compose, Drizzle ORM, Prisma (listed as an alternative ORM), Better Auth, Turborepo

## [I Cracked a Password using ONLY Response Times...](../videos/OxZknIoZuy0.md)
`OxZknIoZuy0` · Better Stack · 2025-11-02 · q3 · intro · demo · also: security-guardrails

Better Stack demo of a timing attack: an early-exit string comparison leaks key length and characters through response times, then the speaker covers why real-world impact is limited and how to mitigate it.

- Techniques: Timing-based key length discovery; Per-position timing recovery; Constant-time comparison for secrets; Rate limiting as the cheap mitigation; Timing check for username enumeration
- Tools: Bun, Node.js (crypto.randomBytes, crypto.timingSafeEqual), TypeScript (generatekey.ts, crack scripts), SQLite (named as a susceptible operation in the cited paper), Claude (named as the summariser of the Minerva attack, not used in the demo)

## [5 Vue.js BEST Practices in 4 Minutes](../videos/QB1p2iuQm_0.md)
`QB1p2iuQm_0` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: —

Four-minute Vue.js listicle on reusable components, slots, composables, props/emits and prop validation with TypeScript; generic frontend advice with no bearing on our projects.

- Techniques: Slots for reusable component structure; useCounter-style composable; Visible prop plus close event for modals; Modal open-state composable; Typed props via TypeScript interface
- Tools: Vue.js, Vue Composition API, TypeScript

## [Sick of Digging Through Logs? Find Errors FAST with OpenTelemetry and Go!](../videos/gOag7kWHJ5c.md)
`gOag7kWHJ5c` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: observability

A Go tutorial that wires an existing slog logger into OpenTelemetry (bridge, provider, OTLP/HTTP exporter, Collector) so logs can correlate with traces and metrics. Covers only Go; the video says JS and Python were not yet supported.

- Techniques: OTel log bridge for an existing slog logger (Go); Local OTel Collector for log debugging via Docker Compose
- Tools: OpenTelemetry (OTel) logs SDK, OTLP over HTTP, OpenTelemetry Collector, Go, log/slog, Go Fiber (GoFiberApp service name), Bruno (API client), Docker Compose, otelbin (config visualizer), Prometheus, Grafana, Better Stack (promoted)

## [10 Pro Claude Code Tips & Tricks NO ONE Shares](../videos/Br5Ofobq6Is.md)
`Br5Ofobq6Is` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: claude-code, coding-agents, token-cost-efficiency

A 4-minute Better Stack listicle of ten Claude Code tips: phone notifications via hooks, permission and thinking-budget settings, CLAUDE.md emphasis, session recovery, parallel sessions, and cheaper model use. Quick ideas, few exact configs.

- Techniques: Stop/Notification hook for completion alerts and phone pings; Alias the skip-permissions flag and toggle it off with shift+tab; Deny read access to sensitive files at global or project scope; Thinking budget by keyword in the prompt; CLAUDE.md emphasis, file links and memory; Custom slash commands with chained arguments and nested folders; Session recovery with --continue, --resume and double-escape rewind; Parallel agents on git worktrees with Claude Squad or tmux; Browser access to a terminal with Vibe Tunnel; /clear on topic change plus a cheaper model
- Tools: Claude Code, CLAUDE.md, Claude Squad, tmux, git worktrees, Vibe Tunnel, Kimi K2, BetterStack

## [Warp Terminal: The AI Terminal That Transformed My Workflow...](../videos/C8vL-VKcJgo.md)
`C8vL-VKcJgo` · AI LABS · 2025-11-02 · q2 · intro · review · also: coding-agents

A feature tour of the Warp terminal: natural-language commands with approve-before-run, Ctrl+R and Ctrl+I AI modes, an agent that installs a repo from its README, Warp Drive team sharing, and a WSL route for Windows.

- Techniques: Natural-language command generation with approve-before-run; README-driven repo setup via agent; Environment variable for API keys before launch; Team sharing through Warp Drive; Windows install via WSL
- Tools: Warp (terminal, built-in AI agent, Warp Drive), Aider (transcribed as "Adr"/"AIDR"; a repo the host installs, probably Aider), OpenAI API (key set as an environment variable), WSL (Windows Subsystem for Linux), Debian .deb installer for Warp, Python (the wrong version was caught in the README setup), Windsurf (teased for a later video)

## [React Scan - My New Favorite Debugging Tool](../videos/m_1VgKLSGKU.md)
`m_1VgKLSGKU` · Better Stack · 2025-11-02 · q2 · practitioner · tutorial · also: —

Better Stack walkthrough of React Scan, a free Million tool that highlights unnecessary React re-renders and shows why, then fixes them with useMemo, useCallback, React.memo and state colocation. Not AI-related.

- Techniques: Find re-renders with React Scan; Memoize an expensive derived value with useMemo; Stabilize object and array props passed from a parent; Skip child re-renders with React.memo; Stabilize handler props with useCallback and functional state updates; Move state down before memoizing; Use a state manager for shared state
- Tools: React Scan, React, React.memo, useMemo, useCallback, Redux, Zustand, React Compiler, Million

## [5 Zustand BEST Practices in 5 Minutes](../videos/6tEQ1nJZ51w.md)
`6tEQ1nJZ51w` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: —

Five Zustand best practices in five minutes: export only custom hooks, use atomic or useShallow selectors, keep actions in a stable object modeled as events, keep stores small, and add middleware.

- Techniques: Wrap selectors in custom hooks and hide the store hook; Atomic selectors, or useShallow for object selectors; Stable actions object exposed through one hook; Event-style actions that own business logic; One small store per concern; Middleware for immer, persist and devtools
- Tools: Zustand, React, Redux DevTools, immer, Redux (named only as the origin of object-selector habits), TypeScript, useShallow (Zustand export), Chrome

## [Redis 8 Just Made Every Other Database Obsolete](../videos/b8yANadT0Y4.md)
`b8yANadT0Y4` · Better Stack · 2025-11-02 · q2 · intro · review · also: data-engineering

Six-minute Redis 8 walkthrough of time-series downsampling and RedisJSON, using a sensor dashboard and a user-profile app. Command-level detail is useful; the title overclaims and no benchmarks are shown.

- Techniques: One raw time-series key per sensor with a retention window; Automatic downsampled series via a compaction rule; Pick the series and bucket size by requested time window; Store profile and history as JSON with per-field commands; Credentials as hashes and sessions in Redis; Local Redis for the demo
- Tools: Redis 8, RedisTimeSeries (TS.CREATE, TS.ADD, TS.RANGE, time-series rules), RedisJSON (JSON.SET, JSON.GET, array append, numeric increment), Redis hashes (HSET), Docker, Express.js, DuckDB (named as comparison), ClickHouse (named as comparison), MongoDB (named as comparison), Redis 7 (named as baseline)

## [The EASIEST way to build AI apps – AI SDK Overview](../videos/TbjBzopteO4.md)
`TbjBzopteO4` · Better Stack · 2025-11-02 · q3 · intro · tutorial · also: mcp-and-tools, agent-architecture

Better Stack's tour of Vercel's AI SDK for TypeScript: it builds a Next.js chat app with streaming, file input, reasoning display, manual, provider and MCP tools, and streamed structured output, all in about 17 minutes.

- Techniques: Streaming chat endpoint; Per-provider options for reasoning; Manual tool with zod schema; External search and page-fetch tools; Provider-defined tools plus source output; MCP server as tools; Agent loop step cap; Smooth streaming; Streamed structured output; Local dev with an AI gateway
- Tools: AI SDK (Vercel), Next.js, React, Svelte, Angular, Zod, Vercel AI Gateway, OpenAI GPT-5, GPT-5 nano, gpt-image-1, Anthropic Claude Sonnet 4, Google Gemini 2.5 Flash

## [Why CapnWeb is the LAST RPC Library You'll Need](../videos/7cA94oBqr9E.md)
`7cA94oBqr9E` · Better Stack · 2025-11-02 · q2 · intro · tutorial · also: —

A 4.5-minute walkthrough of Cap'n Web, Cloudflare's tiny object-capability RPC library, showing HTTP batch and WebSocket bidirectional setups in Bun/React and Node.

- Techniques: HTTP batch RPC server; Typed HTTP batch client with disposable stubs; Shared stub via React context; Bidirectional RPC over WebSockets
- Tools: Cap'n Web (capnweb, Cloudflare), Cap'n Proto, Bun, React, Node.js, ws (WebSocket library for Node), Wrangler, tRPC, oRPC, GraphQL, TypeScript

## [Docker Logging - "docker logs" Command | Log Drivers | Logging Strategies](../videos/Zlj39xXPu2k.md)
`Zlj39xXPu2k` · Better Stack · 2024-11-02 · q3 · practitioner · tutorial · also: observability

Better Stack beginner walkthrough of Docker logging: docker logs flags (tail, since, until, grep), the default json-file driver, how the official nginx image symlinks logs to stdout/stderr, daemon.json log options, and four logging strategies.

- Techniques: Read container logs with filters; Make a container's file logs visible to Docker; Rotate and compress json-file logs globally; Stamp each log entry with custom fields; Choose a log architecture
- Tools: Docker, Docker Desktop, docker logs, docker run, docker ps, docker exec, NGINX, Windows Subsystem for Linux, Fluentd, AWS CloudWatch, Google Cloud Logging, syslog

## [AWS CloudWatch: How to Set Up EC2, RDS, Lambda and API logging](../videos/4tCj9kfc_cA.md)
`4tCj9kfc_cA` · Better Stack · 2024-11-02 · q3 · practitioner · tutorial · also: observability

A 30-minute AWS CloudWatch setup tutorial covering EC2 agent logs, Lambda, API Gateway access logs, RDS log exports, alarms, canaries, and forwarding logs to Better Stack.

- Techniques: EC2 custom log shipping to CloudWatch; API Gateway access logging; RDS log exports to CloudWatch; Static-threshold alarm with a test trigger; Alarm to incident tool via SNS webhook; Log forwarding with a vendor Lambda and subscription filter; Synthetic endpoint canary
- Tools: AWS CloudWatch, CloudWatch Logs (log groups, log streams, Live Tail, subscription filters), CloudWatch Metrics and automatic dashboards, CloudWatch Alarms, CloudWatch Synthetics canaries, CloudWatch agent (amazon-cloudwatch-agent), Amazon SNS, AWS IAM, Amazon EC2, Amazon RDS, AWS Lambda (Node.js 18, x86_64), Amazon API Gateway

## [fluentd Data Collector | Collecting, Transforming and Routing Log Events](../videos/ephdg9usWyc.md)
`ephdg9usWyc` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: observability

Hands-on Fluentd tutorial: tail an Apache access log, parse it to JSON, strip a field, and ship it to Better Stack. Solid practical config walkthrough with a vendor-flavored destination.

- Techniques: Install Fluent Package on Ubuntu and verify; Minimal tail source with pos_file and tag; Stdout-first validation before wiring a remote destination; Remote destination with LogTail plugin; Redact fields with record_transformer; Field search on structured logs; Operate by tag, not by file
- Tools: Fluentd, Fluent Package 5.0.2, Calyptia Fluentd, td-agent (named as the pos_file directory), Better Stack Logs, LogTail (Fluentd output plugin for Better Stack), Apache HTTP Server (apache2 parser), Ubuntu 22.04 LTS (jammy), systemctl, truncate, nano, fluent-gem

## [Python Job Scheduling - with the Schedule package](../videos/nurgToSGoUM.md)
`nurgToSGoUM` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: observability

Tutorial on running periodic Python jobs with the schedule package, scraping Hacker News, and alerting on missed runs with a Better Stack heartbeat.

- Techniques: Declarative recurring jobs with schedule; Decorator-based job registration; HTML scrape to dict list with BeautifulSoup; Heartbeat ping at the end of each scheduled job; Choose the scheduler by requirement
- Tools: schedule (Python package), requests, BeautifulSoup 4 (bs4) with html.parser, pprint, Better Stack (Heartbeats, incidents, on-call escalation), VS Code, Hacker News (scraped source), Unix cron, Celery, Celery Beat, Django, AWS Lambda

## [Python QueueHandler & QueueListener - Offload Log Processing to Separate Thread | FastAPI demo](../videos/_UgXBArTWOA.md)
`_UgXBArTWOA` · Better Stack · 2024-11-02 · q3 · practitioner · tutorial · also: observability

Walkthrough: Python QueueHandler and QueueListener move slow log sinks like SMTP email onto a background thread, shown in FastAPI. Gotcha: stop the listener on shutdown or queued records are dropped.

- Techniques: Level-gated SMTP alerting; QueueHandler + QueueListener offload; Lifespan-managed listener for FastAPI; Module split for logging config; Quick before/after latency check
- Tools: Python logging (logging.handlers: SMTPHandler, QueueHandler, QueueListener), Python queue module, contextlib asynccontextmanager (called 'context lib' in transcript), FastAPI (lifespan parameter), uvicorn (main:app, --reload), time module, VS Code, a free SMTP test service (unnamed in transcript)

## [Node.js Job Scheduling with Agenda | JSDOM web-scraping task](../videos/ZE_P7uXZm2c.md)
`ZE_P7uXZm2c` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: observability, data-engineering

Tutorial on scheduling Node.js jobs with Agenda, MongoDB-backed persistence, priorities, one-off and cron schedules, a JSDOM Hacker News scraper, and Better Stack heartbeat alerts. Not AI-related.

- Techniques: Run MongoDB as the Agenda backing store in Docker; Minimal Agenda setup in an ES module; Graceful shutdown with cancel; Priority via define options; One-off and immediate runs; Dead-man heartbeat for scheduled jobs; Scraping Hacker News with fetch and JSDOM
- Tools: Agenda (npm agenda), MongoDB, mongosh (MongoDB Shell), Docker, Docker Hub (mongo image), Node.js, npm, JSDOM, Better Stack (heartbeats and incidents), VS Code, fetch (Node built-in), fs (Node built-in)

## [Laravel Scheduled Tasks](../videos/gMOkw_x9ByY.md)
`gMOkw_x9ByY` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: observability

Walkthrough of Laravel's task scheduler (kernel schedule method, schedule:run vs schedule:work, cron), building a custom artisan command that publishes scheduled blog posts, and monitoring it with a Better Stack heartbeat.

- Techniques: Define a scheduled artisan task; Run the scheduler in production via cron; SQLite database for a demo project; Scaffold model, migration and seeder; Seed test data with a randomized schedule; Custom command to release due posts; Better Stack heartbeat after the job succeeds; Verify DB state with tinker
- Tools: Laravel, Artisan, PHP, SQLite, Eloquent, Faker, Carbon, Better Stack heartbeats, VS Code, cron

## [Pino JS - Logging in JavaScript / Node.js applications](../videos/fluDEkA1h6w.md)
`fluDEkA1h6w` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: observability

Better Stack walkthrough of Pino, the fast JSON logger for Node.js: log levels, formatters, child loggers, error logging, worker-thread transports, redaction, Fastify integration, and shipping logs to Better Stack.

- Techniques: Minimal Pino setup and pretty output; Log level from environment; Custom log level; Uppercase level label via formatter; Child logger for fixed context; Logging errors with stack traces; File transport with pino.transport; pino-pretty to a file without colour; Multiple log destinations; Redacting sensitive fields; Fastify with Pino; Shipping logs to Better Stack
- Tools: Pino, pino-pretty, npm, Node.js, npx, VS Code, Fastify, Better Stack Logs, @logtail/pino (Logtail Pino transport), Express (mentioned), NestJS (mentioned), Winston (mentioned)

## [How to Setup Redis Caching in Node](../videos/QqTB97aMa4c.md)
`QqTB97aMa4c` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: infra-cost-scaling

A beginner Node.js tutorial that adds Redis caching to an Express endpoint, load-tests before and after with Artillery, and briefly compares cache-aside, write-through, write-behind and refresh-ahead.

- Techniques: Redis server setup on Ubuntu (systemd-supervised); Node client connection with error, ready and connect handling; Cache-aside (lazy loading) on an HTTP search endpoint; Normalizing cache keys; Before and after load test with Artillery; Write-through; Write-behind (write-back); Refresh-ahead; Deciding what to cache
- Tools: Redis (server, default port 6379), redis (npm client for Node.js), Node.js, Express, npm, Artillery (load testing, installed globally), redis-cli, Ubuntu (apt-get, systemd), VS Code, PM2 (npx pm2), Git (used to diff benchmark results), Hacker News API (external upstream in the demo)

## [Logging in FastAPI Apps / Writing a FastAPI Middleware](../videos/1RLFSOwpf88.md)
`1RLFSOwpf88` · Better Stack · 2024-11-02 · q2 · intro · tutorial · also: observability

Step-by-step FastAPI logging tutorial: a configured Python logger, a per-request logging and timing middleware, and shipping logs to Better Stack, with the slow-request search as the payoff.

- Techniques: Central logger module with formatter and multiple handlers; Ship logs to Better Stack with the Logtail handler; Request logging middleware; Middleware in a separate module (class-based registration); Structured log fields via extra=; Per-request latency via timing middleware
- Tools: FastAPI, Uvicorn, Starlette, Python logging module, Python time module, Python asyncio, Logtail Python package, Better Stack (Logtail source and Live Tail UI), VS Code

## [Winston - Logging in JavaScript & Node.js applications](../videos/YjEqmINAQpI.md)
`YjEqmINAQpI` · Better Stack · 2024-11-02 · q3 · intro · demo · also: observability

Tutorial on Winston, the Node.js logging library: levels, transports, JSON and printf formats, child and named loggers, error stacks, startTimer profiling, and shipping logs to Better Stack.

- Techniques: Basic Winston logger with console and file transports; Per-transport level; Readable console output and a custom timestamped line; Child logger for request-scoped fields; Stack traces for errors; Named loggers per service; Timing a block of code; Shipping logs to Better Stack with the Winston transport
- Tools: Winston (Node.js logging library, version not stated), Node.js, npm, VS Code, GitHub (Winston readme), Better Stack (log service, with its Winston/Logtail transport), Winston community transports: MongoDB, Syslog, Telegram, MySQL

## [Logging in Django and Python Applications - Handlers / Formatters / Better Stack aggregation](../videos/XSwIUnGXrwY.md)
`XSwIUnGXrwY` · Better Stack · 2024-11-02 · q3 · practitioner · tutorial · also: observability

Step-by-step Django and Python logging: stdlib loggers, handlers and formatters, a Django LOGGING dict driven by .env, named-logger propagation, then shipping logs to Better Stack.

- Techniques: Module-scoped loggers; Python stdlib setup without a framework; Django LOGGING dictConfig; Formatter styles; Env-driven log config with django-environ; Named-logger propagation control; Shipping logs to Better Stack
- Tools: Python logging (stdlib), Django (LOGGING setting, dev server, manage.py migrate, SQLite), django-environ, logtail-python (Better Stack Python package), Better Stack (log management: sources, live tail, SQL dashboards), VS Code

## [Log Levels Explained (with practical examples!)](../videos/myxlDVC2K74.md)
`myxlDVC2K74` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: observability

Better Stack walkthrough of logging levels (fatal/critical through trace), with Python examples of when to use each and how levels drive filtering, alerting and log volume in production.

- Techniques: Classify each log call by recoverability and required action; Fail fast on missing configuration with a critical log; Try/except around IO with an error log and a fallback; Log an HTTP fetch as info on success and error on failure, with a debug payload dump; Route deprecation warnings into the logger; Set the production threshold to info and keep debug and trace out; Alert on error and critical, and watch the count after deploys
- Tools: Python logging module, Python os and sys modules, requests (Python HTTP library), telnetlib (deprecated Python stdlib module, slated for removal in Python 3.13), Loguru (external Python logging package, referenced for trace level), go-zero log package (Go, has trace method), Pino.js (Node.js logger, custom levels), log4j, log4net, syslog, Better Stack (Logtail) log service, JSONPlaceholder (sample JSON API used in the info and debug examples)

## [How to Setup Node.js and TypeScript](../videos/u_GQSEjis48.md)
`u_GQSEjis48` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: —

Walkthrough of adding TypeScript to a Node/Express project: install tsc and @types/node, extend a community base tsconfig, migrate JS incrementally, and run tsx watch mode for development without a compile step.

- Techniques: Install TypeScript and Node typings; Minimal project tsconfig.json; Build and run compiled output; Incremental JS-to-TS migration; Dev loop with tsx and a type-check watcher; Safer emit on error
- Tools: TypeScript (tsc), 5.5.4 shown in the demo, @types/node, @types/express, @types/morgan, @tsconfig/node20 (community base tsconfig, tsconfig/bases repo), tsx (TypeScript execute), npm, Node.js 20 (speaker also mentions Node 21 at 3:32), Express, Axios, Morgan, nodemon

## [Dozzle - Web-based Docker Log Viewer!](../videos/4ynKW5rwd1E.md)
`4ynKW5rwd1E` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: observability

Beginner walkthrough of Dozzle, a lightweight web UI for real-time Docker container logs, run as a container with the Docker socket mounted read-only.

- Techniques: Run sample containers with port mapping; Run Dozzle with read-only Docker socket and port mapping; Run Dozzle via Docker Compose; Use the log UI for triage
- Tools: Dozzle, Docker, Docker CLI, Docker Compose, Docker Hub, Nginx, Redis, GitHub

## [JSON logs in Python apps - with FastAPI & python-json-logger!](../videos/aJCK0LWz8kg.md)
`aJCK0LWz8kg` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: observability

Tutorial on turning Python standard-library logs into JSON with python-json-logger in a FastAPI app, passing per-request fields via extra=, and shipping the logs to Better Stack with a Logtail handler.

- Techniques: Install python-json-logger and swap the formatter; Add per-request fields with extra= and let the formatter see them; Logtail / Better Stack handler alongside local handlers; Log outcome and return 404 from a lookup endpoint; Filter structured logs by field in Live Tail
- Tools: Python logging module, python-json-logger, FastAPI, Uvicorn, Better Stack (Logtail), Logtail Python handler, VS Code, venv, pip, Vector (mentioned as an alternative), Fluentd (mentioned as an alternative)

## [Logrotate - Log Management on Linux Servers](../videos/-tM6DsYam0c.md)
`-tM6DsYam0c` · Better Stack · 2024-11-02 · q3 · practitioner · tutorial · also: observability

Practical walkthrough of logrotate on Ubuntu: per-service configs, create vs copytruncate, compression, scheduling via cron, and a heartbeat curl in postrotate to alert when rotation stops.

- Techniques: Check the installed logrotate version and defaults; Per-service rotation block in /etc/logrotate.d/; Choose the rotation strategy per app; Force a rotation to test a config; Run logrotate hourly instead of daily; Heartbeat alert on successful rotation
- Tools: logrotate 3.19, cron (cron.daily, cron.hourly), Apache 2 (apache2), rsyslog, UFW, gzip / gunzip, mail, nano, tmux, curl, Better Stack Heartbeats, Ubuntu

## [Build a HackerNews Clone: Hono, Tanstack Router, Drizzle, React Query, Lucia & more](../videos/eHbO5OWBBpg.md)
`eHbO5OWBBpg` · Better Stack · 2024-11-02 · q3 · practitioner · tutorial · also: —

Ten-hour Better Stack build-along of a Hacker News clone on Hono, Bun, Drizzle, Postgres, TanStack Router/Query/Form and Lucia, covering typed APIs, session auth, transactional voting, pagination and optimistic updates, then Fly.io deployment.

- Techniques: Typed API envelope with a global error handler; Zod validator middleware with shared schemas; Derive API schemas from Drizzle tables with drizzle-zod; Sessions with Lucia as a thin helper; Transactional toggle with denormalized counters; Drizzle relations for self-referencing comment trees without foreign keys; Offset pagination with a separate count query; Helper to return dates as ISO UTC strings from SQL; Optimistic mutation with TanStack Query and rollback; URL search params as state, with validated search schemas; Prettier and ESLint setup per folder; Docker Compose for local Postgres, Fly.io for hosting; Drizzle Kit push for schema sync
- Tools: Hono, Bun, Drizzle ORM, drizzle-kit, drizzle-zod, postgres.js (postgres), PostgreSQL 17, TanStack Router, TanStack Query (React Query), TanStack Form, TanStack Table, TanStack Virtual

## [Docker with Node.js: Build, Run, and Manage Containers](../videos/ozFFCrMedFM.md)
`ozFFCrMedFM` · Better Stack · 2024-11-02 · q2 · intro · tutorial · also: observability, infra-cost-scaling

Beginner Docker tutorial for a Node.js app: write a Dockerfile and .dockerignore, run on a custom network with a Postgres container, bind 0.0.0.0, orchestrate with Docker Compose and healthchecks, then ship logs to Better Stack.

- Techniques: Dockerfile skeleton for a Node app; .dockerignore for Node projects; Build and run with a tag, env file and network; Point the DB host at the container name; Bind the HTTP server to 0.0.0.0 (Fastify); docker-compose.yml with healthcheck gating; Container log and resource inspection; Vector log shipping to Better Stack
- Tools: Docker, Docker Compose, Docker Hub, Node.js (20.16 LTS base image, node:20.16-alpine3.19), npm, Alpine Linux, Fastify, Express, PostgreSQL, Vector, Better Stack

## [Introduction to Node Clustering](../videos/Nz0OfV2L5m0.md)
`Nz0OfV2L5m0` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: infra-cost-scaling

Better Stack tutorial on Node.js's cluster module: fork one worker per CPU core to get past single-threaded Node, benchmark the gain with autocannon (22k to 61k requests in 10s), then do the same with PM2 and note the state and logging caveats.

- Techniques: Hand-rolled cluster primary with respawn; Benchmark before and after with autocannon; PM2 cluster mode; Move shared state out of workers
- Tools: Node.js, cluster module (node:cluster), os.availableParallelism, Express, autocannon, PM2, Pino, Winston, Better Stack

## [Fastify Application Development | Logging with Pino.js](../videos/vUDH8OX5DTM.md)
`vUDH8OX5DTM` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: observability

Beginner tutorial on building a small Fastify API in Node.js, configuring its built-in Pino logger, and shipping the logs to Better Stack through a Pino transport.

- Techniques: Fastify app bootstrap with ESM and nodemon; Enable Pino logging in Fastify by config object; Log from inside a route with reply.log; Route extraction into a plugin; Ship Fastify logs to Better Stack via the Logtail Pino transport; Fan out logs to multiple transports; Search hosted logs by a structured field
- Tools: Fastify, Node.js, npm, Pino (Fastify's default logger), @logtail/pino (Better Stack Logtail Pino transport), nodemon, Better Stack (log platform, Live tail and search), VS Code

## [Loguru - Simplified Python Logging with Loguru!](../videos/gSc1oHcwkE4.md)
`gSc1oHcwkE4` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: observability

Intro tutorial on Loguru, a Python logging library: sinks, format, JSON output, context binding, exception capture, file rotation, and shipping logs to Better Stack.

- Techniques: Minimal Loguru setup; Replace the default sink with a custom stdout sink; Colors via format markup; JSON output; Custom JSON shape with logger.patch; Per-sink level threshold; Multiple sinks; Bound context; Scoped context; Exception capture; File rotation and retention; Better Stack sink
- Tools: Loguru, Python standard library logging (comparison only), pip, VS Code, Better Stack (Logs & Metrics, Live Tail), Better Stack Python driver with LogTail handler, GitHub (Loguru repo page)

## [Monitoring Linux Authentication Logs with Vector & Better Stack](../videos/H4LSiY7I4ps.md)
`H4LSiY7I4ps` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: observability, security-guardrails

Better Stack tutorial: collect /var/log/auth.log with Vector, convert syslog to JSON with a remap transform, ship it to Better Stack, then chart sudo authentication failures on a dashboard.

- Techniques: Verify what auth.log captures before building a pipeline; Vector file source plus remap transform for auth logs; Validate, then test with a console sink; Ship to a remote source with an HTTP sink and bearer auth; Create a log-to-metrics group-by from the parsed event name; Build a bar chart of one event type
- Tools: Vector (version not stated), Better Stack (sources, live tail, log-to-metrics, dashboards, alerting), Ubuntu (WSL), auth.log / syslog / rsyslog, PAM (pluggable authentication modules), sudo, sshd, nano, Vector Remap Language (VRL) functions: parse_linux_authorization, parse_regex, json_extract (SQL)

## [How to Setup Uptime Kuma - Self Hosted Monitoring](../videos/t4Nb-09oZSw.md)
`t4Nb-09oZSw` · Better Stack · 2024-11-02 · q2 · intro · tutorial · also: observability, infra-cost-scaling

Walkthrough of self-hosting Uptime Kuma with Docker to monitor sites, then building public status pages and incidents. The back half pitches Better Stack's managed service.

- Techniques: Uptime Kuma Docker install; HTTP(s) monitor settings; Keyword check; Status page setup; Better Stack escalation and recovery
- Tools: Uptime Kuma, Docker, Node.js, PM2, Better Stack, Playwright, Plausible, Google Analytics, Discord, Slack

## [How to Schedule Tasks in Node using node-cron](../videos/_WFcUzO_9CY.md)
`_WFcUzO_9CY` · Better Stack · 2024-11-02 · q3 · practitioner · tutorial · also: observability

Tutorial on scheduling Node.js functions with node-cron (crontab syntax, validation, start/stop control) and wrapping a SQLite backup job with a Better Stack heartbeat so missed runs alert someone.

- Techniques: Basic node-cron schedule; Validate a cron expression before scheduling; Round-robin job state with a closure; Create a deferred, controllable task; Schedule an existing function without modifying it; Dead-man-switch heartbeat monitoring; Set heartbeat grace from measured duration
- Tools: node-cron, Node.js, npm, VS Code, crontab.guru, ChatGPT (mentioned as a way to draft cron expressions), dotenv, SQLite, Better Stack (Uptime heartbeats)

## [How To Start Logging With MySQL](../videos/4nrbbGiG0x4.md)
`4nrbbGiG0x4` · Better Stack · 2024-11-02 · q3 · practitioner · tutorial · also: observability

Walkthrough of MySQL's four log types (error, general, slow query, binary) on Ubuntu, then shipping them and server metrics to Better Stack with a slow-query anomaly alert.

- Techniques: Enable general log at runtime; Enable logs persistently in my.cnf; Slow query log threshold check; Locate binary logs; Ship MySQL logs and metrics to Better Stack; Dashboard template plus anomaly alert
- Tools: MySQL server (version not stated), mysql command-line client, Ubuntu, systemctl, less / cat / nano, mysqldumpslow, Better Stack (logs, Live Tail, dashboards, alerts), Vector, Better Stack MySQL exporter

## [Rsyslog - Log Processing in Linux](../videos/fgdXuqiyUKs.md)
`fgdXuqiyUKs` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: observability

Hands-on Ubuntu tutorial on rsyslog: read rules from 50-default.conf, route cron output to its own file, tail a FastAPI app's log file into the syslog file, and add JSON templates and constant fields.

- Techniques: Install and verify rsyslog; Map the config layout; Route a service's output to its own file; Application log file tailed by rsyslog; Add JSON output and constant fields
- Tools: rsyslog, systemd / systemctl, apt, yum, cron / crontab, nano, Python logging, Python venv, FastAPI, Uvicorn, VS Code, Ubuntu

## [Django Middleware - Defining a Custom Logging Middleware](../videos/_FZfjYVhnwA.md)
`_FZfjYVhnwA` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: observability

Step-by-step build of a Django middleware that logs request method, IP, path, status and duration, then ships the logs to Better Stack with structured fields.

- Techniques: Class-based request/response logging middleware; Register middleware by dotted path; In-module logger with stream output; Per-request duration with time.time(); Structured fields with extra=; Adding a Better Stack Python handler; Moving network log shipping off the request path
- Tools: Django, Python logging (getLogger, StreamHandler, Formatter, QueueHandler, QueueListener), Python venv and pip, Python time module, VS Code, Better Stack (log sources, Live Tail, search), Logtail Python package (Better Stack handler), Vector, FluentD, Celery

## [What is OpenTelemetry? - Explanation and Demo](../videos/LzLULxhyIpU.md)
`LzLULxhyIpU` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: observability

Intro and live Node/Express demo of OpenTelemetry: why unified logs, metrics and traces matter, how the SDK and collector fit together, and exporting to Better Stack.

- Techniques: Bootstrap OTel in a Node/Express app with an instrumentation file loaded before the app; Use OTLP exporters for every signal, and keep the app pointed at a local Collector; Collector config: receivers, processors, exporters, service pipelines; Run the Collector in Docker with the OTel JS getting-started command; Build a custom chart from an auto-generated HTTP metric
- Tools: OpenTelemetry (API, Node SDK, OTLP exporters, Collector), OpenTelemetry Collector (otel/opentelemetry-collector Docker image), getNodeAutoInstrumentations (OTel Node auto-instrumentation package), Node.js 20.15, Express.js, Bunyan (logging, JSON output), Pino, Winston, Better Stack (Telemetry source, Live Tail, dashboards), Prometheus, Jaeger, Docker

## [PHP Logging with Monolog](../videos/GLbeuxNAcn8.md)
`GLbeuxNAcn8` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: observability

Intro tutorial on PHP logging with Monolog (channels, handlers, formatters, exceptions) that ends by shipping logs to Better Stack; useful basics, mostly vendor-tied at the end.

- Techniques: Install Monolog with Composer; Bootstrap the autoloader and import aliases; One logger per channel with a level-filtered file handler; Fan out to multiple destinations; Switch output format with a formatter; Log exceptions with context; Ship logs to Better Stack (Logtail)
- Tools: Monolog (PHP logging package), PHP 8.2, Composer, Ubuntu, Windows Subsystem for Linux (WSL), VS Code, Better Stack Logs (Live tail, sources), Better Stack PHP client (Logtail handler, installed via Composer), php8.2-curl, Laravel, Symfony, Elasticsearch / MongoDB / FluentD formatters (listed, not used)

## [Log Shipping with Vector | Collecting, Transforming and Routing Log Events](../videos/EKHjPK6CHFw.md)
`EKHjPK6CHFw` · Better Stack · 2024-11-02 · q3 · practitioner · tutorial · also: observability

Hands-on tutorial on installing Vector, tailing syslog and a FastAPI JSON log file, transforming logs with Vector Remap Language (VRL), and shipping the result to Better Stack over HTTP.

- Techniques: Install Vector from the apt repo and manage the service; Minimal Vector config: file source to console sink, then validate; Python JSON logging for Vector to tail; Remap transform for parsing and enrichment (VRL); HTTP sink to Better Stack with bearer auth
- Tools: Vector (version not stated), Vector Remap Language (VRL), apt / apt-get, systemctl, nano, Python FastAPI, uvicorn, python-json-logger, Better Stack Logs and Metrics, Linux syslog (/var/log/syslog), WSL (Ubuntu), VS Code

## [Go Structured Logging with the slog Package (Golang)](../videos/ptoKy-COIlE.md)
`ptoKy-COIlE` · Better Stack · 2024-11-02 · q3 · practitioner · tutorial · also: observability

Better Stack walkthrough of Go's log/slog package (Go 1.21+): levels, text and JSON handlers, attributes, groups, child loggers, file and multi-writer output, and redaction via LogValuer.

- Techniques: Replace the default logger with a configured one; Switch to JSON for aggregation; Typed attributes; Group related fields; Request-scoped child logger; Log to a file and to stderr; Redact fields with LogValuer
- Tools: Go 1.21 (speaker's version shown as 1.21.0.4 in the captions), log/slog (NewTextHandler, NewJSONHandler, HandlerOptions, Group, With, SetDefault, LogValuer), log (standard library: New, SetOutput, Default, Lshortfile, LDate flags), io.MultiWriter, os.OpenFile, os.Getenv, math/rand (Intn), VS Code, Better Stack (log platform)

## [JavaScript Console Logging Essentials](../videos/j7XwVztvKH4.md)
`j7XwVztvKH4` · Better Stack · 2024-11-02 · q2 · intro · tutorial · also: observability

Beginner tutorial on the 20+ browser/Node console methods beyond console.log: format specifiers, log levels, trace, table, count, time, group and clear, with a note that Winston-style libraries are better for production.

- Techniques: printf-style substitution in console.log; Using log levels to separate message types; Using console.trace to find how code was reached; Tabular output with console.table; Counting calls with a label; Timing code with labelled timers; Grouping related output with console.group; Clearing the console after a successful stage
- Tools: Chrome DevTools, Node.js, Winston (mentioned as a logging library for production), Hacking Scale newsletter (Better Stack plug)

## [Modern Redis Crash Course: Backend with Express, TypeScript and Zod](../videos/dQV0xzOeGzU.md)
`dQV0xzOeGzU` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: token-cost-efficiency

Project-based Redis crash course for Express + TypeScript + Zod: cache-aside, write-through, and the hash, list, set, sorted-set, JSON, search and Bloom filter types on a restaurant-directory API.

- Techniques: Project setup and scripts; Singleton Redis client; Key-name helper; Hash entity plus atomic counters; Promise.all for independent Redis ops; Paginated list read; Sets as manual indexes; Sorted-set leaderboard with running average; Cache-aside with TTL for a third-party API; RedisJSON storage; RedisSearch one-time index script; Bloom filter for duplicate guard; Zod validation middleware and standard responses
- Tools: Redis, Redis Stack, RedisInsights, RedisJSON, RedisSearch, Bloom filter (RedisBloom), node-redis (redis npm package), ioredis (mentioned as the alternative), Express 4, Express 5 (mentioned), TypeScript, tsx

## [Cron Task Scheduling in Linux | User Crontabs | python-crontab package](../videos/t1QWq7IzbKw.md)
`t1QWq7IzbKw` · Better Stack · 2024-11-02 · q3 · intro · tutorial · also: observability

Better Stack walkthrough of Linux cron: install and start the cron service, write user crontab entries, schedule Python scripts with python-crontab, and monitor jobs with heartbeat pings.

- Techniques: Install and start the cron service; Five-field crontab entry; Backup a SQLite file on a schedule; Register a Python job from code using python-crontab; Manage existing cron jobs from Python; Dead-man's-switch heartbeat for each scheduled run
- Tools: cron, crontab, python-crontab, Python 3, venv, pip, requests, pathlib, shutil, sqlite3, nano, VS Code

