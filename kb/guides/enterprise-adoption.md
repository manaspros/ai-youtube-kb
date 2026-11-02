# Guide: enterprise-adoption

*Synthesized by Sonnet from 119 talks since 2026-05-18.*

## State of the art

By autumn 2026 the story has moved from "does AI help?" to "why does it not scale?". Most firms have deployed agents. Few have scaled them (`XqF-IFHBCkM`, `AGkzpxMdPn8`). The blockers are rarely the model. They are process, ownership, context, review capacity and trust.

What practitioners do now:

- **Change the way of working, not just the tool.** Amazon's 50-team pilot saw a 4.5x median deployment-velocity gain for teams that changed habits. Tool-only teams stayed under 3x (`pqlWNihgdjI`). Block found 90% of engineers "using AI", but mostly in the IDE, with no change in shipping speed (`whue9_YquGA`).
- **Pick one platform and push it.** Intercom standardised on Claude Code, shipped internal plugins to every laptop, and turned each failure into a guidance update (`4_VQBbs2iQA`). Uber put all model traffic and all MCP traffic behind gateways (`17-YSUHo6Lk`).
- **Make repos agent-ready.** Layered context files, deterministic checks, fast local CI and reviewable PRs come first (`whue9_YquGA`, `aeTb5BdmTTc`, `wpOA-UXynoM`, `Se8jHLliLXE`).
- **Codified know-how is the asset.** Skills, SOPs, ontologies and context layers hold what the company knows. Skills need owners, versions, evals and security scans (`M05vON8i0aI`, `u-o0sW9nwmk`, `dQ-_i1tZiws`, `8G_1-3IO4ZQ`).
- **Autonomy is earned in steps.** Shadow, then advisory, then narrow action with limits and kill switches (`-a2oTS9J67U`, `3ZlQk4-knWM`, `XqF-IFHBCkM`, `B0fjR3yaZFU`).
- **Code review is the new bottleneck.** Volume goes up, PRs get bigger, and review and CI become the queue (`whue9_YquGA`, `Se8jHLliLXE`, `dSg0pu8d6qg`, `gDRCpTMCqEU`).
- **Forward-deployed engineering (FDE) is a named enterprise motion.** Many vendors now describe it (`APqXGyCoGW4`, `KwhgfwOSToQ`, `wpOA-UXynoM`, `ITMXwI6QL6A`, `1OMHGsUZiqA`, `RVxym6mmIns`).
- **Non-engineers now build.** Planners write skills, ops and PMs run workflows through coding agents, and staff ship internal apps (`gpmze-6ueGU`, `bMjlRrWjdT0`, `HTzgC3FoYsI`).

## Consensus patterns

1. **Measure value, not tokens.** Token leaderboards get gamed (`CS5Cmz5FssI`). Use dashboards as smoke detectors (`dSg0pu8d6qg`). Track blended cost per merged PR with revert rate beside it (`U7ZYBCcdJPg`). Compare AI-usage cohorts on existing metrics (`Se8jHLliLXE`). Set a baseline before adding agents (`XqF-IFHBCkM`, `-a2oTS9J67U`).
2. **Verification before autonomy.** Count your deterministic validators and add the missing ones first (`wpOA-UXynoM`, `VMemhtlsoNk`). Layer checks: linters and tests, then agent review, then humans on function (`5Bn0xro2ol8`, `VrpEyglYgeU`). Write the failing test first, then verify end to end (`5Bn0xro2ol8`, `bdHaOXZOhcM`).
3. **One shared gateway for models and tools.** Auth, PII redaction, attribution and cost control sit in one place (`CD6R4Wf3jnY`, `17-YSUHo6Lk`). Cross-app access via the IdP gives short-lived tokens and real revocation (`EmhRyw6xeT0`).
4. **Run agents as the user, with attribution.** Two Sigma runs cloud agents under each employee's identity and propagates an attribution header like a trace ID (`wCIYViPd4SU`). Enforce limits outside the agent, per call (`IavxrdVnwXM`, `vGn6N4-bxBY`).
5. **Failures become harness changes.** A correction counts only when it becomes an executable change: a write gate, a classifier eval, a rule (`dQ-_i1tZiws`, `4_VQBbs2iQA`, `pyvRID_CZZU`, `jtzh-GBXBWc`). Replay past cases with writes disabled (`dQ-_i1tZiws`, `aeTb5BdmTTc`).
6. **Domain experts are in the loop, not around it.** They annotate traces, write rubrics and own skills (`kfSDc2eVLo4`, `NKwIX3CiRgU`, `yqF6XhzbWBk`, `u6q-byPWUuo`, `Yphdry8ttAQ`). Judges are calibrated on hand labels (`3z2uT5aDx_Y`, `bMjlRrWjdT0`).
7. **Evals come from real work.** Seed a question bank before building (`DrTdD-ttjCY`, `ObTPqBGsEbA`). Use simulated users, but calibrate them on real users so scores drop to honest levels (`3z2uT5aDx_Y`, `KMR_RBoCa4M`). Turn traces and human edits into ground truth (`B0fjR3yaZFU`).
8. **Context is the bottleneck, so build a shared context layer.** Knowledge gaps, not model quality, stall agents (`_QAVExf_1uw`, `8G_1-3IO4ZQ`, `B8l81jhvHbI`). Tiered sources of truth, ontologies and graphs help (`B8l81jhvHbI`, `VGN22pPpb-8`, `jt1Pbr_n6oU`). Give each context item a lifecycle and an owner.
9. **Deterministic code does the work. The model plans or judges.** Examples: Phaidra's planner plus set resolver (`EUsPvBeIx70`), Kepler's atomic provenance (`Tt2kX2sgQio`), Perpetual's typed plan compiler that fails closed (`8g0g1ncwzG0`), Flywire's YAML workflows with per-step permissions (`rAUyRDOFyHU`).
10. **Staged rollout with gates.** Pilot, 10% beta, then GA, gated on metrics (`DrTdD-ttjCY`, `u6q-byPWUuo`). Start with low-risk tasks, then widen (`WJRdLNhrsLQ`). A written value case and a named human overseer come before deployment (`-a2oTS9J67U`).
11. **Find the people who own each decision in week one.** In a bank, the blocker is unnamed owners for data, model risk, third-party risk and audit, not the demo (`3ZlQk4-knWM`).
12. **Enablement is a people programme.** Hand-picked champions (`whue9_YquGA`), protected-time cohorts (`3XI90A3ENSg`), time-boxed company-wide sprints (`UcYoMg-8-L8`), and leadership ownership of the setup (`aeTb5BdmTTc`, `zCJtYuqwm7E`).
13. **Own the abstraction because the stack changes in months.** Box reviews its agent stack every six months and gates switches on evals (`sM1iYgz93HI`). Notion routes by task difficulty and keeps model optionality (`-I5W5QVAT8E`). Fine-tuned models can become tech debt next to editable skills (`4loPnxvWWhg`).

## Disagreements & open questions

- **Multi-agent or one agent?** ZS killed its multi-agent pipeline for one reasoning agent plus a deterministic signal gate (`u6jJcIFDLE4`). Vercel collapsed a chain into one file-system agent (`9dYcwOkpCE8`). Machinecraft runs about 36 narrow agents with an orchestrator (`jtzh-GBXBWc`). Rule of thumb from the first two: split only where one prompt breaks.
- **Review every PR, or relax the gate?** Maven lets engineers self-declare review tiers (`WJRdLNhrsLQ`). Qodo says review has a teaching job too and wants codified rules first (`s-aixZYJG4c`). Sonar and McKinsey suggest a staged trust ladder up to auto-merge (`XqF-IFHBCkM`). Block says the bottleneck is not solved (`whue9_YquGA`).
- **Do individual gains become team gains?** Gains of 4.5x are reported at Amazon (`pqlWNihgdjI`). DX sees only a modest org-level lift (`Se8jHLliLXE`). A due-diligence view finds more PRs but also longer reviews and bigger PRs (`gDRCpTMCqEU`). Most of these figures are self-reported.
- **Is FDE a real model or a dev shop?** Several say it needs a shared platform and a KPI, or it is staff augmentation (`KwhgfwOSToQ`, `APqXGyCoGW4`). Sierra says the title is vague and customer accountability is the constant (`Byv311hdoHE`). AssemblyAI says FDE does not scale to high inbound volume (`pyvRID_CZZU`).
- **Is MCP the integration layer?** Uber leans on gateways (`17-YSUHo6Lk`). WorkOS leans on identity brokering through the IdP (`EmhRyw6xeT0`). Maersk avoids MCP because the backing systems are bloated (`dQ-_i1tZiws`). Skill-versus-MCP roles are still being worked out (`LC3-P7v3yoI`, `u-o0sW9nwmk`).
- **How to price and measure agents?** Containment alone misleads (`PwCSYy-oGsM`). Seat pricing is under pressure (`Byv311hdoHE`, `9cJrbj23fOA`).
- **Pilot failure rates (95%, 87%, 1 in 5, 50%) are quoted often and rarely sourced** (`X6NShR2ccOg`, `l0FLhNqBOic`, `8G_1-3IO4ZQ`, `kfSDc2eVLo4`). Treat them as rhetoric.

## How thinking changed over time

- **2026-05-18.** Case studies lead: spec and design doc as the planning layer, PR state driving tickets (`VMemhtlsoNk`). A guidance flywheel at Intercom (`4_VQBbs2iQA`). One gateway for MCP (`CD6R4Wf3jnY`). The IKEA pull-based knowledge loop (`_QAVExf_1uw`). Token-maxing is already being questioned (`CS5Cmz5FssI`).
- **2026-06-18.** Governance and org shape: human-speed scaffolding is the drag, so fund a portfolio of bets and use an exposure ladder (`AGkzpxMdPn8`). Cross-functional teams, not only data scientists, own agents (`NKwIX3CiRgU`).
- **2026-07-18.** Maturity models and champions (`whue9_YquGA`). FDE appears as a named motion (`APqXGyCoGW4`). Company "brains" and context layers (`eBUyTS7SzV4`, `8G_1-3IO4ZQ`). Production playbooks (`ObTPqBGsEbA`).
- **2026-08-18.** FDE wave across vendors. Evals and simulation mature (`3z2uT5aDx_Y`, `KMR_RBoCa4M`). Cost becomes a first-class constraint (`RGe6EjucbzI`, `-I5W5QVAT8E`). Verification is named the key lever (`VrpEyglYgeU`, `wpOA-UXynoM`).
- **2026-09-18.** Software factories at scale (`17-YSUHo6Lk`). The "tokenmaxxing to trusted throughput" turn (`dSg0pu8d6qg`). Habits, not tools, explain gains (`pqlWNihgdjI`). Skills get governance (`M05vON8i0aI`). Regulated-industry patterns arrive: audit logs, SOPs, mandates (`mav15aW9lLM`, `dQ-_i1tZiws`, `vGn6N4-bxBY`).
- **October 2026.** Evidence turns skeptical and measured. Org-level data from 400+ orgs (`Se8jHLliLXE`). Cost per PR (`U7ZYBCcdJPg`). Due-diligence arithmetic (`gDRCpTMCqEU`). Trust, owners and overseers (`-a2oTS9J67U`, `3ZlQk4-knWM`). Per-call authorization for agents (`IavxrdVnwXM`). Skill distillation from traces (`u-o0sW9nwmk`).

## Numbers worth remembering

- 4.5x median deployment velocity for teams that changed habits, under 3x for tool-only teams (`pqlWNihgdjI`).
- About 90% of Block's engineers used AI, mostly in the IDE, with no shipping change. Champions: about 50 people at 30% of their time (`whue9_YquGA`).
- DX: perceived delivery speed up about 4.5%, change confidence down about 6%, average PR size 44 to 72 lines (`Se8jHLliLXE`).
- Faros data: high-adoption teams merged 98% more PRs, review time up 91%, PR size up 154% (`gDRCpTMCqEU`).
- AI is about 2.5% of the cost of a merged PR. AI cost is up about 60x, merged PRs per engineer up 43% (`U7ZYBCcdJPg`).
- Uber: over 70% of PRs from agents, 100M+ model requests a day, PII guard under 100 ms (`17-YSUHo6Lk`).
- A two-week agent build can take about 12 months to reach production (`AGkzpxMdPn8`).
- About 5% of demo calls become contracts. Pilot windows shrank from about 6 months to about 2 weeks (`7A65O-0lvKE`).
- AssemblyAI support agent: resolution from 10% to 80%, about $700 a month (`pyvRID_CZZU`).
- Snowflake GTM agent: 6,000 users, 40,000 questions a week. Quality over coverage at launch (`DrTdD-ttjCY`).
- Maersk: 200+ agents, 100,000+ corrections over nine months, SOP corpus about 20x the runtime (`dQ-_i1tZiws`).
- Phaidra: LLM-only lookup fell from about 80% to about 30% correct at scale. Planner plus resolver stayed at 100% (`EUsPvBeIx70`).
- First simulation eval showed 90%+ accuracy, judged too good to be true (`3z2uT5aDx_Y`).
- One distilled skill lifted success from 36% to 100%. This is a single anecdote (`u-o0sW9nwmk`).
- 37% of about 60 internal apps had no engineer commits (`HTzgC3FoYsI`).
- Token-count targets and spend minimums are second-hand and easy to game (`CS5Cmz5FssI`).
- Typical project time on the data foundation: about 60% (`ObTPqBGsEbA`).
- Survey of 1,048 engineers: evals are the top challenge, multi-model is the norm, and agents now mostly have write access (`RGe6EjucbzI`).

## From creator channels (Kai Explains, AI LABS, Better Stack)

Six of the 11 creator videos carry usable method. The rest are off-topic or thin. Almost every creator claim is one creator's experience. Two videos carry sponsor segments (`AD-EmZ3v6-g`, `LC7kGTDoWRY`). Treat their numbers as color.

### Practical playbook

1. **Shadow the job before you pick a tool.** Spend about an hour next to the person doing the most repetitive task. Write each step in the order it happens. Ask why each step exists. "We've always done it" marks a workaround to question. The creator's refund example: an unwritten check was the real policy (`AD-EmZ3v6-g`, 1:24).
2. **Pick a high-volume process.** Automating one message a few times a day saves little. Support history is a good place to find volume (`AD-EmZ3v6-g`, 5:36).
3. **Triage every step with three filters.** A fixed rule that must always be right stays ordinary software. Messy input that needs judgment goes to a model. An expensive failure keeps a human, even if a model could do it. Expect a mix of all three (`AD-EmZ3v6-g`, 8:31).
4. **Connect to existing systems instead of migrating.** Expose the team's current tools to the agent through MCP. The creator's examples are Notion and a finance system that cost $5M over five years (`AD-EmZ3v6-g`, 5:36).
5. **Keep the old step structure visible.** Collapsing an 11-step process into one step made people stop trusting it. Show intermediate results inside each step. The creator budgets more time for trust than for building (`AD-EmZ3v6-g`, 7:04).
6. **Build a labelled eval before go-live.** Collect real cases with known correct outcomes. Run the full set, count correct answers, read every miss, fix the cause, and repeat. A few runs will miss rare failures (`AD-EmZ3v6-g`, 9:55).
7. **Record the cost of a wrong answer next to the value.** For each use case, write what it earns or saves and what a wrong output costs. In the creator's example, one wrong dispatch cost more than the agent's daily spend (`AD-EmZ3v6-g`, 11:22).
8. **Put a verify-then-commit rule in CLAUDE.md.** Tell the agent to run tests after each change and check UI work in a browser before moving on. Commit each verified unit, and ask the agent to record its decisions in the message. Use git to undo edits to code or tests the agent should not have touched. The creator does not show the file wording (`LC7kGTDoWRY`, 3:41).
9. **Use plan mode in an unfamiliar stack.** Let the agent ask questions, answer them, approve a plan, then build from it. The creator built a backend in a language he did not know this way (`LC7kGTDoWRY`, 7:41).
10. **Sample model decisions against your own labels.** Track how often the model agrees with you on a sample before you let it decide automatically. The example is sentiment and marketing calls (`nfX_SQYDoBI`, 16:52).
11. **Plan before fanning out parallel agents.** One host reported large token bills from many parallel Claude instances on one feature. The 20-instance figure is illustrative, not measured (`nfX_SQYDoBI`, 1:10:34).
12. **Gate tool calls by path in sandboxed agents.** Intercept each call. Block edits outside the sandbox path and allow reads only on named files. The creator uses pi's tool-call event. No code is shown (`nfX_SQYDoBI`, 1:13:03).
13. **Route each job to the cheapest model that meets its bar.** Put one gateway in front of several providers and switch models with a config change. The creator names Bedrock, Azure AI Foundry and Vertex (`EK8y8O5st_M`, 9:15).
14. **Set permissions in two layers.** The org sets a ceiling (strict, auto or dangerous). Teams can only tighten it. A command deny list for recursive deletes and destructive SQL applies in every mode. Personal space is private by default, and credentials stay private unless shared on purpose. This is one two-week-old project (`GrZ-X3-2TVs`, 1:59 and 3:05).

### Tools creators recommend

- MCP servers — connect existing systems such as Notion without migrating data — `AD-EmZ3v6-g`
- Claude Code with CLAUDE.md and git — verify-then-commit loop for long runs — `LC7kGTDoWRY`
- Claude Chrome extension — visual check of UI work — `LC7kGTDoWRY`
- Puppeteer MCP — browser testing option, named in passing — `LC7kGTDoWRY`
- CodeRabbit — external scanner for known vulnerability patterns — `LC7kGTDoWRY`
- QM (YC open-source multiplayer harness) — self-hosted, multi-user agent harness with Slack access and org approval modes. Two weeks old at the video date — `GrZ-X3-2TVs`
- pi — default harness inside QM, with per-tool-call events for gating — `GrZ-X3-2TVs`, `nfX_SQYDoBI`
- Marimo — notebook that exposes live variables to an LLM scratchpad — `nfX_SQYDoBI`
- uv — Python package manager, framed as the Python counterpart to the npm workflow and preferred over pip — `nfX_SQYDoBI`
- AWS Bedrock, Azure AI Foundry, Google Vertex — model marketplaces for per-task routing — `EK8y8O5st_M`
- AnyWidget — browser widget in Python for labelling LLM outputs by hand — `nfX_SQYDoBI`

The two sponsor segments (`AD-EmZ3v6-g`, `LC7kGTDoWRY`) are not listed as recommendations.

### Where creators agree or clash with the conference talks

- **Agree: process before tool.** `AD-EmZ3v6-g` says most AI failures are process failures. This matches consensus 1 and the "change the way of working" point above. The creator repeats the MIT "95% no return" figure without a source. The guide already treats that figure as rhetoric.
- **Agree: verify before autonomy.** `LC7kGTDoWRY` pushes verify-then-commit. `7s2IIIP47GM` pushes human gating by cost of error. This matches consensus 2 and the autonomy ladder.
- **Agree: measure cost against outcome.** `AD-EmZ3v6-g` frames value against the cost of a wrong answer. `7s2IIIP47GM` says to judge tools by whether the work shipped and worked. This matches consensus 1.
- **Clash: review.** `LC7kGTDoWRY` says agents should do first-pass review and humans should review only exceptions. The guide's disagreements section says review is the bottleneck. The creator gives no data. The conference data (`gDRCpTMCqEU`) shows longer reviews and bigger PRs.
- **Clash: multi-agent.** `LC7kGTDoWRY` recommends an orchestrator with subagents to isolate context. The guide's rule of thumb is to split only where one prompt breaks. The token-bill warning in `nfX_SQYDoBI` supports the cautious view.
- **Clash: MCP as default.** `AD-EmZ3v6-g` treats MCP as the default way to connect existing systems. The guide notes that Maersk avoids MCP because its backing systems are bloated, and that Uber leans on gateways. This is one creator's view.
- **Tone gap: autonomy timelines.** `LC7kGTDoWRY` predicts agents will work for days unattended in 2026. This is a forecast. The conference evidence says autonomy is earned in steps.

### Watch first

- `AD-EmZ3v6-g` — the clearest creator method for choosing AI use cases. Process audit, three-filter triage and error-cost accounting. Has a sponsor segment and quality 2/5.
- `LC7kGTDoWRY` — a concrete verify-then-commit loop with CLAUDE.md, git and plan mode. Mostly the team's anecdotes. Has a sponsor segment.
- `GrZ-X3-2TVs` — a hands-on look at an org-deployed agent harness with approval ceilings and a command deny list. Good for enterprise permission design. Two weeks old.
- `EK8y8O5st_M` — the unit-economics test for vendors and the per-task routing idea. Figures are second-hand. Watch for the framing, not the numbers.
- `nfX_SQYDoBI` — long podcast. Watch around 1:10:34 (planning before parallel agents) and 1:13:03 (path-based tool gating). Otherwise mostly opinion.

## Watch first

- `pqlWNihgdjI` — best evidence that habits, not tools, drive gains. Five habits you can copy.
- `whue9_YquGA` — a full large-org playbook: maturity stages, champions, repo kit, review bottleneck.
- `Se8jHLliLXE` — the sober org-level data. Use it to check hype.
- `17-YSUHo6Lk` — the most complete platform blueprint: gateways, skills marketplace, context graph.
- `3ZlQk4-knWM` — regulated deployment as a discovery problem. Autonomy ladder and evidence pack.
- `dQ-_i1tZiws` — SOP to agent, and every failure mapped to a preventive fix.
- `AGkzpxMdPn8` — why enterprise projects stall and how to fund and roll out.
- `-a2oTS9J67U` — value case, named owner and staged autonomy for trust.

## Implications for our projects

**AgentOS (Govrix Scout, MemoryMesh, SkillForge, Crucible).**
- Add per-call, mission-scoped authorisation and budgets that report consumption back to the agent (`IavxrdVnwXM`). Enforce at the proxy, not in the agent.
- Cost tracking per project and per merged unit of work fits budgets. Show blended cost, not only token spend (`U7ZYBCcdJPg`, `dSg0pu8d6qg`).
- SkillForge: the open question was success signal and skill-worthiness. Use trace-to-skill distillation from successes and failures (`u-o0sW9nwmk`), a lint, scan and review gate before a skill enters the library (`17-YSUHo6Lk`, `M05vON8i0aI`), and per-skill trace evals. Keep owner, version and dependency metadata (`M05vON8i0aI`).
- MemoryMesh: correction precedence over stored facts and a nightly consolidation job (`jtzh-GBXBWc`). Treat context as a lifecycle with logged correction events (`B8l81jhvHbI`).
- Crucible: keep the harness apart from the code it runs (`XKup1pj-34M`). Replayable runs with writes disabled give a correctness check (`dQ-_i1tZiws`).
- For the "benchmarks, not demos" thesis, copy the calibrated simulation approach and report the sim-to-real gap (`KMR_RBoCa4M`, `3z2uT5aDx_Y`).

- The registry is the sub-registry and skills catalogue pattern: owner, version, access rules, MCP search front end (`CD6R4Wf3jnY`, `M05vON8i0aI`, `u-o0sW9nwmk`).
- Gateway as root of trust, with pluggable credentials and policy for allowed patterns (`CD6R4Wf3jnY`). Short-lived tokens through the IdP (`EmhRyw6xeT0`).
- Uber's tool-token tax result (discovery MCP, then CLI projection) is a useful design input for MCP listings (`17-YSUHo6Lk`).

**ProsHarness.**
- Overnight runs need acceptance criteria and a morning review (`bdHaOXZOhcM` runs overnight with context gathering at 5 pm and a morning review; `qqrk7CtkuIw` covers end-state delegation).
- Planning with a critic fits staged autonomy and bounded long-running harnesses with an explicit definition of done (`wpOA-UXynoM`, `kiqubc5b5Yo`).
- Checkpoint and resume matches durable execution, where each model and tool call is a checkpointed activity (`VjEP0xqTUI0`).
- Phone-driven approvals match payload-hash-bound gates and approval interrupts (`8g0g1ncwzG0`, `4uFVSLgD2Q4`, `EEt3ZSG4a1s`).
- Zero-token credentials fit agent-provisioned sandboxes where humans never paste keys (`T3wRyXg_yVg`) and the brains-and-hands split with an egress proxy (`IavxrdVnwXM`).

**Recurring interests.**
- Entity resolution and data quality: per-field source precedence and golden-source agreement before building (`BOWYujhIQuo`). Layered extraction with verification per level (`W4pnzOURwHQ`). Cross-document entity graphs (`Iwe_RY-fYgI`).
- Cheap-model pipelines: tier by task difficulty and use code for deterministic steps (`-I5W5QVAT8E`). Gate cascades with cheap triggers before expensive models (`u6q-byPWUuo`).
- Evals: judge as classifier, validated on about 100 hand labels (`3z2uT5aDx_Y`).
