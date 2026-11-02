# Guide: pr-code-review

*Synthesized by Sonnet from 48 talks since 2026-05-18.*

Scope: AI code review, PR review bots, review workflows, and quality gates on agent-written code. Several talks are vendor pitches (Sonar, Qodo, Meticulous, Greptile). Their numbers are self-reported. Treat them as signals, not facts.

## State of the art

Practitioners agree on one thing. Agents write code faster than humans can review it. Review is now the bottleneck, not generation. Evidence: `_mi3alkqy4s`, `EL123UNokkI`, `TJPInBjhE4Q`, `YgEv7IQzGdM`, `LlgiOCmFG_w`.

What teams do now (most recent talks weigh most):

- **Layered review.** Cheap deterministic checks first (lint, types, tests, static analysis). Then an agent reviewer. Then a human. The first two layers exist to make the human step short. (`LlgiOCmFG_w`, `7b9tov5Uc5s`)
- **The reviewer is a separate agent with its own context.** The writer must not check its own work. Pocock keeps coding standards out of the implementer's context and gives them to a reviewer sub-agent that commits fixes instead of leaving comments. (`LlgiOCmFG_w`, `ZpK5PWX2YRM`, `kZsf_Sfm7RU`)
- **Review effort follows risk.** Auth, money and irreversible data changes get a human reading every line. Low-risk changes (docs, dependency bumps) can be auto-approved under written policies. (`ZpK5PWX2YRM`, `7b9tov5Uc5s`, `LlgiOCmFG_w`)
- **Trust is earned in stages.** Advisory comments, then blocking on critical findings, then autofix until CI is green, then auto-approve for named paths, then auto-merge. Move up only when precision is shown at the current step. (`XqF-IFHBCkM`, `uuwDWRbxoYo`, `uU5Gv2h8-9g`)
- **Repeated review comments become rules.** Each recurring finding is turned once into a lint rule, a doc, or a reviewer instruction. Nobody writes the same comment twice. (`YgEv7IQzGdM`, `E3KbFLAGD6A`, `ZpK5PWX2YRM`, `LlgiOCmFG_w`)
- **The review unit is evidence, not a diff.** Intent, acceptance criteria, test results, screenshots, traces and rationale travel with the PR. (`n97BCfyFIvw`, `VktrqzQgytY`, `kR64LOqBBCU`, `YgEv7IQzGdM`)
- **Reviewer quality is measured by developer behavior.** Uber tracks reply sentiment and whether the developer changed code after a comment. (`EL123UNokkI`)
- **Human review shrinks but does not vanish.** Humans move to the outer loop: design the reviewer, set the definition of good, gate risky and irreversible changes. (`EL123UNokkI`, `_mi3alkqy4s`, `n97BCfyFIvw`)

## Consensus patterns

1. **Deterministic checks before AI, AI before humans.** Deterministic checks cost CPU, not tokens, and they do not hallucinate. Mix them with an LLM pass for intent and business logic. (`LlgiOCmFG_w`, `VrpEyglYgeU`, `03l29gJXpCE`, `-AKPRSYccJc`, `NuePCNMpWGc`)
2. **Run verification inside the agent loop.** The agent calls an analyzer or one local verification command, fixes findings and reruns before it says done. Cheap checks run every iteration. Expensive ones (agentic QA, mutation tests) run once when the PR opens. (`NuePCNMpWGc`, `03l29gJXpCE`, `X6l4lpA0_NY`, `-AKPRSYccJc`, `17-YSUHo6Lk`)
3. **Separate writer, reviewer and test author.** A fresh-context review agent gates agent-written PRs. Humans see only PRs the agent approved. (`kZsf_Sfm7RU`, `L173Z8DpaJg`, `ZpK5PWX2YRM`, `LlgiOCmFG_w`, `VrpEyglYgeU`)
4. **Codify tribal knowledge as rules the reviewer can cite.** Rules have severity, good and bad examples, and links. Track per-rule hit and acceptance rates. Drop noisy rules. Only some rules should block a merge. (`s-aixZYJG4c`, `-AKPRSYccJc`, `YgEv7IQzGdM`, `E3KbFLAGD6A`, `504PvfXou5Y`)
5. **Turn mistakes into system changes.** When a reviewer corrects an agent, update the skill, lint rule or checklist. A meta loop mines logs, PRs and comments for recurring errors. (`X6l4lpA0_NY`, `E3KbFLAGD6A`, `ZpK5PWX2YRM`, `tUPPVhBBcoM`, `TeErpYBUIeM`)
6. **Keep PRs small and single-purpose.** Stack PRs. Have an agent split big changes before review. Cap size (Maven uses about 500 lines). One logical change per PR, one owner's territory. (`ZpK5PWX2YRM`, `OXMMN-XbxwA`, `WJRdLNhrsLQ`, `TJPInBjhE4Q`, `6qkzlT962es`)
7. **Move design review ahead of the PR.** Align on a plan or spec first. Review the PR against the plan. (`Ib5GBkD555M`, `tUPPVhBBcoM`, `-AKPRSYccJc`, `OXMMN-XbxwA`)
8. **Filter reviewer noise before it reaches people.** Use multi-pass consensus, post-processing (rate, dedupe, filter), or a trained noise filter. (`_mi3alkqy4s`, `EL123UNokkI`, `ojJXgXLUQFc`)
9. **Gate on runtime proof where it is cheap.** Boot the app, drive a browser, screenshot, diff. Use canary comparison for performance fixes. (`474j-n1Ltxc`, `YgEv7IQzGdM`, `HLTa7Vcs4X0`, `CgsWxRUY5Eo`, `I2LL_wd89-A`)
10. **Rebuild CI and the merge queue for agent volume.** Test combinations of pending commits in parallel and evict breakers. Cache and shard builds. Keep an audit record of what was checked. (`7b9tov5Uc5s`, `VktrqzQgytY`)
11. **Do not let an agent approve its own change.** Approver must differ from author. (`7b9tov5Uc5s`, `ZpK5PWX2YRM`)

## Disagreements & open questions

- **Kill human review or keep it?** Jain says review is really about alignment, so replace diff reading with intent and evidence (`YgEv7IQzGdM`). Voss says generation has outrun review, so build a review harness and let humans define good (`_mi3alkqy4s`). Dex says lights-off factories hit a wall, so restore review and plan up front (`Ib5GBkD555M`). Friedman splits teams into two camps (review every line vs ship and fix later) and says pick one before buying tools (`s-aixZYJG4c`). Maven lets engineers self-declare review tiers and holds them accountable (`WJRdLNhrsLQ`).
- **Are agent PRs worse than human PRs?** Greptile data says roughly no on reverts, severity and review rounds, but failure modes differ by agent (`474j-n1Ltxc`). DX data says quality volatility and falling change confidence (`Se8jHLliLXE`). Sonar says defects are fewer but subtler in newer models (`NuePCNMpWGc`). Mergeability checks show tests passing is a weak proxy (`_mi3alkqy4s`).
- **Build or buy the reviewer?** Pocock says build your own because team standards are the leverage (`LlgiOCmFG_w`). Uber built uReview with team-owned customization (`EL123UNokkI`). Vendors (Sonar, Qodo, Greptile) argue for platforms. Model quality is not the barrier, context is (`s-aixZYJG4c`).
- **Deterministic score or LLM judge?** eBay insists the review-burden score has no LLM (`TJPInBjhE4Q`). Others use an LLM judge plus rules (`03l29gJXpCE`, `Ib5GBkD555M`).
- **Can LLM reviewers be trusted?** They default to approving plausible code and can be fooled by an innocent commit message (`_mi3alkqy4s`). Agents also game lint rules, so rules must state intent (`E3KbFLAGD6A`).
- **Open:** a binary pass/fail org standard check is not yet out of the box (`ojJXgXLUQFc`). Code-review benchmarks barely moved across model releases (`s-aixZYJG4c`). Block's author says review volume is not fully solved (`whue9_YquGA`). Production trajectories as the "last reviewer" is an idea, not a practice (`_mi3alkqy4s`).

## How thinking changed over time

- **2026-05-18.** Framing is "CI/CD and review were built for human pace." Ideas: pre-merge queue, spec-driven loops, review bundles with rationale and visuals (`VktrqzQgytY`, `kR64LOqBBCU`). Codex presents review as a separate fresh process with repo-wide context (`MhHEGMFCEB0`).
- **2026-06-18.** Focus on enforcement and context. ADRs plus lint rules in the repo (`504PvfXou5Y`). Sonar's verify-in-loop pitch (`NuePCNMpWGc`). Qodo says more context makes review worse, so use specialist agents plus a judge (`EcqMYoIV57A`). Hybrid scripted plus agent PR triage with JSON handoffs (`VaS2h-dY1-4`).
- **2026-07-18.** The bottleneck gets numbers. A review-burden score (`TJPInBjhE4Q`). Risk-tiered review (`ZpK5PWX2YRM`). Humans own the verdict, evidence bundles, explain-it-or-don't-ship (`n97BCfyFIvw`). Staged trust ramp with 100% catch-rate criterion (`uU5Gv2h8-9g`). Security moves before the PR (`7JgIS42mz7U`).
- **2026-08-18.** Skeptics arrive. "Kill the code review" (`YgEv7IQzGdM`). Software factories fail because models are trained on passing tests, not maintainability (`Ib5GBkD555M`). Security needs multiple passes, one concern each (`yWS0udrIOc8`). Skills are supply-chain items that need PR gates (`iKQ78wyJEXU`).
- **2026-09-18 to 09-27.** Production systems and builder-level advice. Uber's uReview with addressal-rate evals (`EL123UNokkI`). Layered brakes and a committing reviewer (`LlgiOCmFG_w`). Rule-linked comments and per-rule analytics (`s-aixZYJG4c`). Reviewer-commits-fixes replaces comment-only bots.
- **2026-10.** Data and calibration. Agent PR quality is about even with human PRs, but failure profiles differ (`474j-n1Ltxc`). Review capacity limits quantified, mergeability rubrics, multi-pass consensus (`_mi3alkqy4s`). Trust ladders formalized (`XqF-IFHBCkM`, `uuwDWRbxoYo`). CI and merge queues must be rebuilt (`7b9tov5Uc5s`). Lint rules from mined feedback (`E3KbFLAGD6A`). Hands-on gating workshop (`-AKPRSYccJc`).

Net trend: from "make review faster" to "make review mostly automatic, with humans at risk gates and standard setting."

## Numbers worth remembering

- Review time to first review: about 3 hours (2024) to about 9 hours (2026) at Uber. uReview posts about 25,000 comments per week. (`EL123UNokkI`)
- Agent users wrote about 741% more code but shipped about 30% more software. Review quality drops past about 400 lines per sitting; a 10,000-line PR needs 3 to 4 working days. About half of SWE-bench-passing PRs were judged mergeable by maintainers. (`_mi3alkqy4s`)
- Median PR review time up 441.5% and 31% more PRs merged with no review (Pharos cohort, as cited). (`TJPInBjhE4Q`)
- Greptile: about 25% of PRs in a month are largely AI-generated by footers and branch prefixes. Under 1% by author field. Review rounds about 2.1 to 2.45 for agents vs humans in between. Agent revert rates are close to human. (`474j-n1Ltxc`)
- More than 70% of PRs at Uber come from agents. (`17-YSUHo6Lk`)
- Claude Tag lands about 65% of product-engineering PRs at Anthropic. Dropping human review for outer-layer code took six-plus months of trust building. (`uU5Gv2h8-9g`)
- Review agents produce about 10x more PRs per day than a three-person team can review. A fix PR can be ready about 30 minutes after detection. (`kZsf_Sfm7RU`)
- Atlassian's noise filter: about 40% comment resolution vs a human baseline of about 45%. (`ojJXgXLUQFc`)
- Multi-pass agreement raised review quality by up to 44% in a Peking University study cited by one talk. A vulnerable diff with an innocent message fooled an agent reviewer 88% of the time vs 35% for humans. (`_mi3alkqy4s`)
- Code survival at VS Code: 55% with GPT-4.1 to 86% with Claude Opus 4.6. (`I2LL_wd89-A`)
- Incremental CI from about 10 minutes to under 1 minute with a warm cache. Serial merging can take about 20 days to get everything green. (`7b9tov5Uc5s`)
- Rule of five: LLM work often needs four or five review passes. A scanner found 241 issues in a codebase that looked clean. (`yWS0udrIOc8`)
- Sonar Java eval: 4,444+ assignments across 53+ models. Top pass rate (84.17%) came with high verbosity and bug density. (`NuePCNMpWGc`)
- Pass-rate gating for non-deterministic tests: about 90% over repeated runs. PR size cap about 500 lines. Sample about 20% of live conversations for new features. (`WJRdLNhrsLQ`)
- Review-burden score: about 10 checks, five families, 0-100. Calibrate on about 200 merged PRs. (`TJPInBjhE4Q`)
- Skill scanner: 2,000+ skills scanned, over 1,500 risks found. (`iKQ78wyJEXU`)
- DX: change failure rate up to 2 points above a roughly 4% benchmark for some companies. (`Se8jHLliLXE`)

## From creator channels (Kai Explains, AI LABS, Better Stack)

Scope: 22 creator videos from AI LABS and Better Stack. No Kai Explains video is in this category's input, so this section does not cover that channel. Most claims come from one creator video, one project, or one demo. Treat numbers as anecdotes unless the note says otherwise. Sponsored or sponsor-style segments: `pSzLkt0NfJQ` (IBM Bob pitch) and `S49gppZl8H0` (names a sponsor).

### Practical playbook

1. **Commit each chunk, then gate on the review.** Run `git init`, then commit after each agent chunk. The commit triggers the CodeRabbit extension. Feed its comments back to the agent before the next chunk. If no review fires, check that the branch is visible in the branch list. (`LXk8nWwOPuY`, single project; the branch bug is secondhand.)
2. **Review in a fresh session.** Open a new session in the same repo. Paste a saved prompt that asks for a review of the code another agent wrote, a PR-readiness check, and a simplify pass. Optionally use a different model. Ask the agent why it made a choice before you judge it. (`zr-Xk0UVHEU`, podcast guest's advice, not measured.)
3. **Fix the evals before the build.** Write an `eval.md` per feature with strict pass/fail checks. A human approves it before any code is written. Add a hook that blocks "done" until the evals pass. (`S49gppZl8H0`, the host's own skills, based on Anthropic's process as relayed.)
4. **Run a builder, verifier and reviewer loop.** Use three fresh-context subagents under one orchestrator. Keep a `state.md` with the round and open failures. Cap the rounds: after three, tell the builder to rethink the approach. After round one, review only the delta from the last fix. Tag each finding with its problem class so the builder fixes every instance. (`S49gppZl8H0`, `d8QpDbBKbAU`; the team cap is three, the host uses five.)
5. **Keep review rules in `review.md`, linked from CLAUDE.md.** Define what counts as a real failure, the severity levels and the report format. Add a learned-rules section. The loop proposes one-line rules, and you add them only after approval. (`S49gppZl8H0`.)
6. **Set risk tiers by consequence.** Ask what breaks for a customer. Cosmetic issues get light checks. Lost money, lockout or another person's data gets the full review. One setup routes some fixed paths to two human reviewers. (`S49gppZl8H0`, `d8QpDbBKbAU`; the tier classifier is one team's setup.)
7. **Block merge on open bug and security findings.** Each finding is either fixed or closed with a short reason. The reason records the false positive. (`d8QpDbBKbAU`, secondhand summary.)
8. **Measure reviewer noise by what authors do.** Track whether each comment is fixed or dismissed. An agent acts on every nitpick, so noise costs more on agent PRs than human ones. Score any reviewer change against past incident PRs, and keep the change only if the score rises. (`d8QpDbBKbAU`.)
9. **Set Cursor BugBot to comment only when asked.** Connect GitHub under Cursor's integrations. Enable "run only when mentioned" or "run once per PR", and hide the "no bugs found" comments. Use "Fix in Cursor" to make the fix yourself. (`Ig-cfiqWJCs`, feature tour, not a measured test.)
10. **Resolve bot comments with one command, and name the false positives.** On an open PR, run the review command over the Greptile comments. It applies fixes and pushes. Reject false positives explicitly. (`kLq5p43huYQ`, one demo.)
11. **Ship stacked PRs with the `gh` CLI.** Run `gh stack init <first-branch>`, commit on each branch, then `gh stack add <next-branch>` for each layer. Run `gh stack submit` to push and open all PRs at once. Merge the stack from the top PR. Put shared types and schema in the lowest PR. (`3Z1xcfF2xlY`, about three minutes of demo.)
12. **Run a CRAP check after the unit tests.** Collect coverage first, then run `cargo crap` (Rust). Flag functions above your complexity budget. Test the metric: comment out one function's tests and confirm its score jumps. (`XuMR1pgc6pc`; the tool default cutoff is 30, and the speaker suggests 5 as a strict example.)
13. **Scope a repo-wide security scan.** Run a regex pass first to pick candidate files. Send batches of about five files to read-only agents. Write an `info.md` with the auth flow and threat model, but do not list known bugs, or the scan skips them. (`qkc1j3_k8gs`, one planted-vulnerability app; 3 of 10 found on the first run.)

### Tools creators recommend

- CodeRabbit extension (Cursor) — per-commit AI review — `LXk8nWwOPuY`
- Cursor BugBot — PR diff review that only comments, with a "Fix in Cursor" link — `Ig-cfiqWJCs`
- Claude Code skills, hooks and `review.md` — builder/verifier/reviewer loop and eval gates — `S49gppZl8H0`
- GStack (Claude Code skill pack) — plan, review, ship and QA slash-command chain — `kLq5p43huYQ`
- Greptile — PR comments that the review command resolves — `kLq5p43huYQ`
- Warp's review skill (open-sourced) — fresh-session review or a GitHub Action review — `zr-Xk0UVHEU`
- Fallow — dead code, duplication and complexity for JS/TS, with dry-run fixes — `-lCfwIoDXq8`
- cargo crap — per-function CRAP score for Rust, after coverage — `XuMR1pgc6pc`
- DeepSec — regex prefilter, then batched read-only agent scan (closing pitch is for a paid tier) — `qkc1j3_k8gs`
- `gh stack` CLI — build and submit stacked PRs — `3Z1xcfF2xlY`
- Strix — multi-agent pen test that can fail a CI check on validated findings — `vRTliPb8fjg`
- Whiteboard (Mac app) — linked diagrams of a branch's changes, with click-through — `cP5PRDo3u6Q`
- Continue (VS Code) — markdown-defined review agents run on a PR — `LRwc64Ui_MQ`
- Routa — Kanban lanes with gates and evidence per task — `_16PhraFYjQ`
- IBM Bob — IDE review mode with a findings panel and auto-fix plus test (sponsor-style pitch) — `pSzLkt0NfJQ`

### Where creators agree or clash with the conference talks

Agree:
- **Fresh-context reviewer.** Matches consensus pattern 3. Creator sources: `zr-Xk0UVHEU`, `S49gppZl8H0`, `d8QpDbBKbAU`.
- **Deterministic screens first.** Fallow, cargo crap and DeepSec's regex pass all filter code before an agent or human reads it. Matches consensus pattern 1. (`-lCfwIoDXq8`, `XuMR1pgc6pc`, `qkc1j3_k8gs`)
- **Repeated findings become rules.** Matches consensus patterns 4 and 5. (`d8QpDbBKbAU`, `S49gppZl8H0`)
- **Risk tiers.** Matches "review effort follows risk." (`d8QpDbBKbAU`, `S49gppZl8H0`)
- **Review the evidence, not the diff.** Eval-first gates and click-through diagram checks. Matches the evidence-bundle view. (`S49gppZl8H0`, `cP5PRDo3u6Q`)

Clash or caveat:
- **Who fixes the code.** The conference view is that the reviewer commits fixes. Creators mostly keep the human in the fix path. BugBot only comments (`Ig-cfiqWJCs`). Whiteboard suggests denying writes in review runs (`cP5PRDo3u6Q`).
- **Unattended autofix.** The Fallow host does not trust the automatic fix to run unattended (`-lCfwIoDXq8`). The guide's trust ladder moves toward autofix once precision is shown. Creators would test fixes before trusting them.
- **Round caps are creator-only.** The conference notes in this guide have no stop rule for review loops. Only `S49gppZl8H0` and `d8QpDbBKbAU` add one, and both are secondhand from Anthropic.
- **Weaker evidence.** Anthropic's figures (about 40% fewer reverts, changes per day rising from about 2,500 to over 30,000) come from a secondhand summary (`d8QpDbBKbAU`, `S49gppZl8H0`). Weigh them below the talks that show data.
- **Cost.** DeepSec runs the strongest models in parallel, and the host says token use grows fast (`qkc1j3_k8gs`). None of the talks in this guide measure review cost this way.

### Watch first

- `S49gppZl8H0` — the full builder, verifier and reviewer loop with eval gates, stop rules and risk tiers. Secondhand from Anthropic, shown as the host's own skills.
- `d8QpDbBKbAU` — the layered gate and the incident-based reviewer eval, in a short summary (quality 4/5).
- `LXk8nWwOPuY` — the commit-gated loop with concrete git steps. One project, so treat results as anecdotal.
- `kLq5p43huYQ` — a full plan, review, ship and QA chain on one PR. The 100-PR claim is unverified.
- `XuMR1pgc6pc` — a cheap second check on complex, untested code, with a test you can run yourself.
- `3Z1xcfF2xlY` — the shortest concrete recipe for stacking PRs.

## Watch first

- `LlgiOCmFG_w` — the most practical recipe: layered brakes, separate reviewer context, reviewer commits fixes, one-way vs two-way door labels, retro skill.
- `EL123UNokkI` — Uber's real multi-agent review engine. Best source on eval signals (addressal rate), trajectory tuning and team-owned rules.
- `_mi3alkqy4s` — the most data-dense talk. Capacity limits, mergeability rubrics, multi-pass consensus, and limits of automated reviewers.
- `474j-n1Ltxc` — measured comparison of agent and human PRs, plus a three-question validation gate.
- `ZpK5PWX2YRM` — clear risk-tiered routing model and writer/inspector separation.
- `uU5Gv2h8-9g` — the staged trust ramp with a concrete exit criterion, and eval-gated change.
- `7b9tov5Uc5s` — CI, merge queue, auto-approve policy, provenance and audit for agent volume.
- `YgEv7IQzGdM` — the strongest argument that review is about alignment, with the slop registry technique.

## Implications for our projects

**ProsHarness.**
- Add a review stage after implementation. Implementer and reviewer run in separate contexts. Reviewer reads a standards file, not the global instructions, and commits fixes. Only open questions become comments. (`LlgiOCmFG_w`, `kZsf_Sfm7RU`)
- ProsHarness already has plan, then Codex critique. Extend it with a trust ladder per repo area and path: advisory, then blocking, then autofix until green. Promote only after the reviewer catches everything humans caught. Log incidents as eval cases. (`uU5Gv2h8-9g`, `XqF-IFHBCkM`)
- Use one local verification command (lint, types, tests, scanners) as the checkpoint gate before a resume or commit. (`-AKPRSYccJc`, `X6l4lpA0_NY`)
- The phone-driven approval flow should show an evidence bundle (intent, test results, rationale, diagram) and not a raw diff. Add a risk tier so only high-risk changes ping the phone. (`n97BCfyFIvw`, `ZpK5PWX2YRM`, `LlgiOCmFG_w`)
- Keep the approver separate from the author agent. (`7b9tov5Uc5s`)
- Add a retro skill that reads past sessions and review comments and proposes lint rules or checks. (`E3KbFLAGD6A`, `LlgiOCmFG_w`)

**AgentOS.**
- Govrix Scout: add an optional "exec-gate" style check that tags agent-written changes with provenance (agent, session, trigger) in the Merkle audit log. Log overrides with named reasons. (`7b9tov5Uc5s`, `7JgIS42mz7U`)
- Crucible: use its sandbox for the "run the change and drive it" validation (install, start, mock inputs, browse). (`474j-n1Ltxc`, `YgEv7IQzGdM`)
- SkillForge: skill-worthiness can use review data. Repeated reviewer corrections are a signal worth mining, and manual takeovers per PR are a KPI one talk tracks. Gate mined skills with lint, scan and review before publish. (`X6l4lpA0_NY`, `iKQ78wyJEXU`, `17-YSUHo6Lk`)
- MemoryMesh and evals: store accepted and rejected review outcomes with provenance and use per-rule analytics to prune noisy rules. (`s-aixZYJG4c`, `TeErpYBUIeM`)
- Benchmarks fit the "distributed system with correctness checks" thesis. Measure addressal rate, revert rate and review rounds, not demos. (`EL123UNokkI`, `474j-n1Ltxc`)

- Registry entries for skills and MCP servers should be scanned in three places: locally, in CI on the PR, and on the published artifact. Use deterministic rules first, LLM only for ambiguous items, and emit SARIF. Back-scan old entries. (`iKQ78wyJEXU`)
- Skill publish needs versioning, owner approval and permissions. (`X6l4lpA0_NY`, `17-YSUHo6Lk`)
- Use review-burden scoring and "time to first review" as team-health metrics, posted non-blocking. (`TJPInBjhE4Q`, `EL123UNokkI`)

**Recurring interests.**
- Entity-resolution and Haiku pipelines: reuse the layered pattern. Cheap deterministic rules first, a cheap-model reviewer second, a human on high-risk cases. Use repeated-run pass-rate gating for non-deterministic checks. (`WJRdLNhrsLQ`, `LlgiOCmFG_w`)
- Evals for agents: build behavioral evals from complaints and incidents, and make model swaps eval-gated. (`uU5Gv2h8-9g`, `TeErpYBUIeM`)
