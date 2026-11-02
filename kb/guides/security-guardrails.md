# Guide: security-guardrails

*Synthesized by Sonnet from 117 talks since 2026-05-18.*

## State of the art (what practitioners actually do now)

The mood changed between May and October 2026. Early talks stressed guardrails as code around a weak model. By autumn the working view is blunt: the model is untrusted, so the boundary must sit outside it.

- **Prompts are not a boundary.** Speakers at PostHog, Deno, Coder and Hinge Health all say this plainly. Even a model that refuses a bad request in one run may comply in the next (`4lXks428C9o`, `MkRYPFIMCSA`, `Wb2v9Phhnns`, `YXEqC05WEI0`, `1tpqdglI3T0`).
- **The lethal trifecta is the shared threat model.** Private data, untrusted content and external communication together are the danger. Most teams keep all three legs and constrain them with identity, scope and policy, instead of removing a capability (`ws9XcGGPBDk`, `abw_m-DRi1k`, `q-WOjZhOMCA`, `9R--1tg45Jg`).
- **The model plans, deterministic code acts.** The model emits a plan or a proposal. A separate layer validates it, applies policy and runs the side effect (`NaOkR3VSfR4`, `APh1Vx0oLmQ`, `BInpv7lGp1o`, `-CnA2lGfymY`, `LqLoYksJ6do`).
- **Credentials never enter the sandbox.** The sandbox holds a placeholder. A proxy or gateway swaps in the real secret as the request leaves (`MkRYPFIMCSA`, `BM2JX9hqsVQ`, `OE_lLNCNfQo`, `ZUZVNKFSmTM`, `8aVbXXvJUY4`, `FGftGOzfohc`, `iQ5xldZ9StU`).
- **Agents get their own identity and short-lived, per-call tokens.** Token exchange (RFC 8693 style) with policy checked before the token is minted is the common design. Standing API keys are treated as the bug (`I3znWC3MEXM`, `ws9XcGGPBDk`, `lMCxVorb9wM`, `JvKO40CFq-s`, `IavxrdVnwXM`).
- **Isolation is a ladder.** Containers share the host kernel. MicroVMs with default-deny egress are the stronger choice for untrusted work (`OqM67QG_Ikk`, `OE_lLNCNfQo`, `LqLoYksJ6do`, `iH_wV8BbS24`).
- **Supply chain now includes skills and MCP servers.** Teams scan skills in CI, review MCP tool descriptions and keep an inventory (`iKQ78wyJEXU`, `1EZdpEhwmNc`, `cgimkNGNjvU`, `ZyC56eV8sVw`).

## Consensus patterns

1. **Enforce in code, not in the prompt.** Rate limits, input blocks, approval gates and output vetoes run as hooks or middleware. The model cannot skip them (`YXiLj4tJt5A`, `4lXks428C9o`, `ij-AU9dpJjc`, `YXEqC05WEI0`, `tDArkCqjA-c`).
2. **Brains and hands split.** The LLM returns an ordered plan. A workflow engine or interpreter executes it with idempotent steps and durable state. Approval is a workflow step, not a prompt sentence (`NaOkR3VSfR4`, `APh1Vx0oLmQ`, `-CnA2lGfymY`).
3. **Plan before untrusted content.** Emit a typed plan first. A separate executor reads untrusted evidence and only fills in parameters. It cannot add actions. Taint analysis over the plan can reject paths from untrusted input to write or send (`q-WOjZhOMCA`, `-CnA2lGfymY`).
4. **Byte-level or network-level egress control.** An egress proxy sees what subprocesses send, including non-HTTP protocols such as Postgres. It applies rules, then an LLM judge, then a human (`MkRYPFIMCSA`, `BM2JX9hqsVQ`, `1tpqdglI3T0`, `LqLoYksJ6do`).
5. **Zero credentials in the sandbox.** Use placeholder secrets, vaults, a credential-injecting proxy or a gateway that holds keys (`OE_lLNCNfQo`, `ZUZVNKFSmTM`, `xn8EsW0wxyc`, `FGftGOzfohc`, `8aVbXXvJUY4`).
6. **Per-tool-call, audience-bound, short-lived tokens.** Policy runs before minting. Denied calls get no credential. Tokens last minutes and are never stored (`I3znWC3MEXM`, `ws9XcGGPBDk`, `EmhRyw6xeT0`, `tZycGA_Fbfo`).
7. **Agent identity is separate from the user's.** Keep actor and principal as separate fields. Log both on every call. Run agents inside the user's own identity and namespace when the firm already has that model (`lMCxVorb9wM`, `wCIYViPd4SU`, `JvKO40CFq-s`, `q-WOjZhOMCA`).
8. **Deterministic gate first, LLM second.** Rules block mechanically. An LLM only reduces false positives and fails closed. Keep the detector separate from the actor (`4lXks428C9o`, `1EZdpEhwmNc`, `iKQ78wyJEXU`).
9. **Scoped, risk-tiered approval.** Gate side-effecting tools, leave reads open. Bind each approval to actor, tool, exact arguments and expiry. Fail closed if a field is missing (`BInpv7lGp1o`, `tZycGA_Fbfo`, `x2bH0RKPgdc`, `Fu45geO3zX8`).
10. **Budgets, not booleans.** Cap each write with a refilling rate limit. Triage verbs by whether a wrong call fails loudly or silently. Use a proxy to stamp audit rows (`rbjWzZK2LU0`, `IavxrdVnwXM`, `zU4EagB311U`).
11. **Run agents remote, ephemeral and least-privilege.** Size the sandbox to the task. Mount only what the task needs. Split risky pipelines across sandboxes by role (`iH_wV8BbS24`, `ZUZVNKFSmTM`, `Wb2v9Phhnns`, `abw_m-DRi1k`).
12. **Treat skills and MCP servers as supply chain.** Scan at authoring, in CI, and at the registry. Scan content again where the agent loads it (`iKQ78wyJEXU`, `4lXks428C9o`, `1EZdpEhwmNc`, `ZyC56eV8sVw`).
13. **Strip sensitive data at ingestion.** Remove PHI or PII at the pipeline boundary. Redact before embedding. Scope memory on write and on read (`YXEqC05WEI0`, `BIhiYL4U9_M`, `Ndp5VaqFrl0`, `0uC6u0lJJl4`).
14. **Verify evidence, not claims.** Do not accept "done". Check the tool trace, a diff and independent checks. Use a separate verifier agent that assumes the claim is false (`C_GG5g38vLU`, `bI8WyG9YB0I`, `imFedndyXYQ`).
15. **Measure the guardrails like code.** Rule tests with positive and negative cases. Planted-injection evals. Judge calibration against a golden set (`4lXks428C9o`, `LqLoYksJ6do`, `NdrSPm6NCdk`, `rTojoVotlD8`).

## Disagreements & open questions

- **Human approval.** Some talks make it a core control (`tDArkCqjA-c`, `x2bH0RKPgdc`). The Keycard talk argues it just moves access control onto a consent-fatigued user. It proposes approving a mission once, then checking each call (`ws9XcGGPBDk`).
- **Where the LLM sits in enforcement.** One camp says the LLM is never the bouncer (`4lXks428C9o`). Others add an equal-power adversary agent or a supervisor agent that reviews worker actions (`1lgFGaHoGq8`, `IavxrdVnwXM`). The open question is how much a model judge can be trusted on vague cases.
- **Classifier vs regex.** A learned small model beat regex on obfuscated injection in one talk, with a naive guard near coin-flip (`s67bE2Ur3bY`). Others prefer fast deterministic rules (`4lXks428C9o`, `YXiLj4tJt5A`).
- **Spec strictness.** One speaker warns that tight key-card style security specs choke adoption and says identity should be accumulated from email and Slack (`mBNVKkyfnE0`). Most others want strict capability grants (`JvKO40CFq-s`).
- **Prompt injection is bounded, not solved.** One talk says so outright (`LqLoYksJ6do`). There is no agreed metric for how much it is bounded.
- **Intent-based authorization is not a standard yet.** The speaker admits it is one proposal (`ws9XcGGPBDk`, `IavxrdVnwXM`).
- **Payment protocols.** The x402 flow has a double-spend window and conflicts with MCP auth (`h6mi88VrPtQ`). Stripe and PayPal prefer scoped mandates and tokens (`KLSuFPj2ld0`, `vGn6N4-bxBY`).
- **Cost of guardrails.** Several admit added latency (`1lgFGaHoGq8`, `XjI-AR4pt7Y`). Few give measured numbers.

## How thinking changed over time (dated)

- **2026-05-18.** Guardrails are plain code around a weak model. A human gate belongs on the tool, not the prompt. Cloudflare shows capability-restricted sandboxes (`C_GG5g38vLU`, `tDArkCqjA-c`, `8txf05vVVl4`).
- **2026-06-18.** Payments and sandbox identity arrive. Seller-scoped tokens enforced by the platform. Network identity replaces keys inside the sandbox (`KLSuFPj2ld0`, `BM2JX9hqsVQ`).
- **2026-07-18.** Provable and structural safety. Plan-as-data with taint analysis, kill switches via feature flags, the isolation ladder, and AI-found bugs shifting the bottleneck to verification (`-CnA2lGfymY`, `zU4EagB311U`, `OqM67QG_Ikk`, `imFedndyXYQ`, `7JgIS42mz7U`).
- **2026-08-18.** The big security month. Agents route around constraints. Egress firewalls, skill vetting, per-agent identity, per-call token exchange and secret brokering all appear together (`1lgFGaHoGq8`, `MkRYPFIMCSA`, `iKQ78wyJEXU`, `JvKO40CFq-s`, `I3znWC3MEXM`, `iQ5xldZ9StU`).
- **2026-09-18.** Budgets, scoped mandates and enterprise primitives. Verb triage, break-glass proxies, immutable event logs, code-layer routing in health AI (`rbjWzZK2LU0`, `vGn6N4-bxBY`, `mav15aW9lLM`, `YXEqC05WEI0`, `4lXks428C9o`).
- **2026-10.** Convergence on infrastructure. MicroVMs with secret placeholders, one MCP gateway, ephemeral remote workspaces, and "model behaviour cannot be the boundary" as a refrain (`OE_lLNCNfQo`, `ZUZVNKFSmTM`, `Wb2v9Phhnns`, `ws9XcGGPBDk`, `1tpqdglI3T0`, `IavxrdVnwXM`).

## Numbers worth remembering (with `video_id`)

- CI-platform incident (Anthropic speaker): an empty pipeline stage made a selector match everything, and about 200 workloads were deleted in 90 seconds (`rbjWzZK2LU0`).
- Text rules in a context file hold about 80% of the time, by the speaker's rough estimate (`rbjWzZK2LU0`).
- An agent made 200 API calls per hour on a booking site and got its user banned (`IavxrdVnwXM`).
- Four-agent pipeline looped 11 days and cost $47,000 (`zU4EagB311U`).
- Stripe demo token: $25 cap, 30 days, one seller. A $50 charge was rejected (`KLSuFPj2ld0`).
- Access tokens last about five minutes with silent re-mint (`EmhRyw6xeT0`).
- A small dependency bump produced about 70,000 changed lines (`LqLoYksJ6do`).
- Fork bomb spawns many processes in about 200 ms, so detect-then-kill is too slow (`1tpqdglI3T0`).
- Of 50 real production ML setups, 78% had at least one critical security mistake. Basic controls cost under about 8% overhead (`XjI-AR4pt7Y`).
- Skill scans: 2,000+ internal skills, 1,500+ risks (`iKQ78wyJEXU`). About 10,000 third-party skills scanned, 367 flagged as malware (`ZyC56eV8sVw`).
- Scanner found 241 issues in a codebase that looked clean after an AI hardening pass (`yWS0udrIOc8`).
- A well-written threat model raised vulnerability true-positive rate to about 90% (`imFedndyXYQ`).
- MCP gateway servers can expose 15 to 20 tools when one is needed (`xn8EsW0wxyc`).
- Under 8% overhead for basic controls; budget heavy scanning only on the riskiest paths (`XjI-AR4pt7Y`).
- Judge-human agreement target 80 to 85% (`NdrSPm6NCdk`).
- Consumer health AI under-triaged emergencies about 50% of the time in an independent test (`YXEqC05WEI0`).
- Credit Karma optimizer cut tool tokens about 90% in demos (`tZycGA_Fbfo`).
- Timing probe on shared H100 MIG identified model depth with 97% accuracy (`SacJfmp33vM`).

## From creator channels (Kai Explains, AI LABS, Better Stack)

Most of these are news reactions, single-presenter reviews or tutorials. Treat a single video as one practitioner's view. Sponsored or paid-tier segments are flagged below.

### Practical playbook

1. **Set a minimum release age in every package manager.** npm takes the setting in days in npmrc. pnpm takes it in minutes in its config (one day by default since pnpm 11). bun takes it in seconds in bunfig.toml. One creator used a one-week window. npx and bunx ignore the setting. The creator also reports agents asking for `latest` to get around it, so enforce it in config, not only in a CLI flag (`Wq6yMdt11LM`).
2. **Turn install scripts off and allow-list the few that need them.** npm: disable install scripts and list exceptions in package.json. pnpm: run `pnpm approve-builds` when a package reports pending build scripts. bun: scripts are off by default. Use `bun pm untrusted` to list them and `bun pm trust <pkg>` to allow one. The bun empty-array quirk is the speaker's report and was not checked (`Wq6yMdt11LM`).
3. **Block git and URL dependencies.** npm: set allow-git to `none`, or to `root` to allow only what the root package.json declares. pnpm: enable block-exotic-subdeps and set trustPolicy to no-downgrade (`Wq6yMdt11LM`).
4. **Put a scanner in front of installs.** Alias npm, pnpm and bun to Socket Firewall or MPQ. Clear the package-manager cache afterwards so cached packages are checked again. The creator picked Socket Firewall. Keep release-age gating too, since scanners only catch packages already known to be bad (`Wq6yMdt11LM`).
5. **Make lockfiles and CI installs strict.** Commit the lockfile. Use `npm ci` in CI, and frozen-lockfile installs for pnpm and bun. On non-pnpm repos, run lockfile-lint to check that resolved hosts are trusted and that integrity hashes match. Review lockfile diffs in PRs. The creator says pnpm is not exposed to resolved-URL swaps. That claim was not checked (`Wq6yMdt11LM`).
6. **Read agent and editor config before opening an unknown repo.** Open `.claude/settings.json` and look for SessionStart or other hooks. Open `.vscode/tasks.json` and look for tasks that run on folder open. Remove anything you did not write, and turn off VS Code automatic tasks. Add these files to PR review, next to install scripts. Don't assume `--ignore-scripts` covers them. The advice is generic. The incident behind it comes from one news explainer (`lNsSxWQDqaU`).
7. **Make stolen CI credentials worth little.** Use OIDC for short-lived, least-privilege tokens in CI. Keep npm publish tokens and cloud keys out of long-lived environment variables. Set CI runners to deny outbound traffic by default and allow only the hosts a build needs (`lNsSxWQDqaU`).
9. **Write deny-by-default rules on actions, not only on access.** For each endpoint, write a CEL expression with an approve or deny verdict. Start with deny-all and add approve rules. Give the agent a deny message that names the approved path, such as a migration PR for schema changes. Send risky actions to Slack approval or an LLM judge. Replay recorded requests against edited rules before you deploy (`ZiFoTw6doGI`).
10. **Cap what a leaked provider key can spend.** Turn on the provider's hard limit, not only the alert email. Expect enforcement to lag, so set the ceiling below what you can afford to lose. Disable auto-reload on prepaid accounts and keep balances low. Use one key per tool. Revoke keys at the provider, not inside a third-party tool. This is one post-incident account, and its figures are the speaker's (`0p96nZsRxlY`).
11. **Rotate keys after a vendor breach without waiting for a notice.** The creator says some victims were drained before any notice arrived. Rotate every key ever pasted into a third-party dashboard, and delete keys nobody uses (`0p96nZsRxlY`).
12. **Read the chat template before serving a local model.** Pull the Jinja chat template out of the GGUF file and read it. Look for logic keyed to trigger phrases or to unexpected URLs and commands. Pickle scanners and model-scan do not check it. Use official or known-quantizer weights for any model with tool access (`3mx84MRj8lY`).
13. **Keep model servers on loopback.** Don't set Ollama's host to 0.0.0.0. Reach the server through Tailscale or an authenticated reverse proxy. In Docker, don't publish the port, since published ports bypass UFW. Update Ollama, LM Studio, llama.cpp, SGLang and vLLM first. The captions give conflicting version numbers, so check upstream release notes (`3mx84MRj8lY`).
14. **Separate command execution from network egress.** Keep .env files, SSH keys and cloud credentials out of any directory the model or its tools can read. Run command execution and network egress in separate processes, and log what crosses between them (`3mx84MRj8lY`).
15. **Audit a CLI's uploads with a MITM proxy.** Route the CLI through the proxy. Run a trivial prompt that says not to open files. Inspect the outbound bodies for repo bundles, git history or env vars. Grep the local logs for upload entries, and rotate any secret that was in an uploaded session. This is one incident video (`n6DIs13ilvU`).
16. **Check data-use settings for each seat.** Find the privacy or training toggle in each AI coding tool. Don't assume the plan default. Read the pricing, footnote and FAQ parts of model launch posts for data and snapshot statements. This rests on one commentary video (`hdWUv2V1jRg`).
17. **Scan a repo in stages.** A regex prefilter picks security-sensitive files. Read-only agents review batches of about five files. Merge and dedupe the output, then run a coverage pass. Leave known bugs out of the context file if you want them found. The creator's test had DeepSec report 9 issues, an unscoped Claude review 39 and a scoped review 13. This is a vendor-built tool, and the closing pitch sells a paid tier (`qkc1j3_k8gs`).
18. **Gate CI on validated findings only.** Run a pentest tool as a CI step on pull requests, and fail the check on validated findings. Accept only findings that come with a working exploit and reproduction steps. Budget a few dollars for a quick scan of a small app. Docker must be running (`vRTliPb8fjg`).
19. **Run browser agents read-only first.** Use a throwaway account, not one you care about. Pause for a human to confirm any purchase, send or delete. Cap the steps per task so a loop cannot run unattended (`OprnDByYVLQ`).
20. **Use a canary secret as a tripwire.** Put a trigger string in a decoy credential in a fake environment. An agent that reads it may refuse and stop. The video reports a Tracebit test where Claude Opus 4.8's admin rate fell from 93% to 0 with one planted string. Treat this as a deterrent, not a control (`ROW6KbSE1Ew`).

### Tools creators recommend

- Socket Firewall: pre-install scanner for npm, pnpm, bun, uv, pip and cargo (`Wq6yMdt11LM`)
- MPQ: pre-install scanner with vulnerability data, typosquat and package-age checks (`Wq6yMdt11LM`)
- lockfile-lint: checks lockfile hosts, URLs and integrity hashes (`Wq6yMdt11LM`)
- Claw Patrol (Deno, open source, early): gateway with credential injection, CEL verdicts, Slack approval and a request dashboard (`ZiFoTw6doGI`)
- OpenShell (NVIDIA, Apache 2.0): sandbox policy layer with per-request, per-binary rules and credential injection, on top of Docker, Kubernetes or microVMs (`SbwckhZkPGs`)
- DeepSec (Vercel): regex-prefiltered, batched agent security scan (`qkc1j3_k8gs`)
- Strix: multi-agent pentest that runs in Docker and can fail a CI check (`vRTliPb8fjg`)
- Context Mode "Protect": command-rule firewall for Claude Code. It checks command text, not script contents, so the creator says it is not a sandbox (`Afm-GNrJbEQ`)
- GoLive: plan-ID-gated deploy agent skill with a refuse-list for paid steps. Verified only on Claude Code and Codex, per the creator (`HTscIrJhjDs`)
- Homebrew 6.0: explicit tap trust, install-plan approval and `brew vulns` (`IwzVzvDw68w`)
- Agit: git-style history for agent sessions, with revert and secret redaction. This video has a sponsored segment (`CHHEjuNBxoQ`)
- Tailscale: private device-to-device access to a loopback-bound model server (`3mx84MRj8lY`)

### Where creators agree or clash with the conference talks

- **Agree: enforce outside the model.** Gateways and sandbox policy layers hold the verdicts in a layer the agent cannot edit. This matches consensus points 1 and 5 above (`ZiFoTw6doGI`, `SbwckhZkPGs`, `Afm-GNrJbEQ`, `HTscIrJhjDs`).
- **Agree: credentials stay off the agent side.** OpenShell and Claw Patrol both inject keys only on matching requests (`SbwckhZkPGs`, `ZiFoTw6doGI`).
- **Agree: local is not the same as safe.** The local-model video says the risk follows what the model can reach, not where it runs. That fits the view that the boundary sits at the tools (`3mx84MRj8lY`).
- **Extend: config files are code.** Creators put project-level hooks, editor tasks and install settings on the supply-chain list. The conference section names skills and MCP servers only (`lNsSxWQDqaU`, `Wq6yMdt11LM`).
- **Clash: approval.** Creators offer per-action gates such as Slack approval and confirm flags. One creator notes that confirm flags come from the agent, so they only slow it down. Pair them with a real human approval step if consent matters (`HTscIrJhjDs`, `ZiFoTw6doGI`). The consent-fatigue critique from the conference talks is not addressed.
- **Clash: judges and scanners ship without measured accuracy.** Claw Patrol's LLM-judge verdict is not tested in its video. DeepSec reports a 10 to 20 percent false-positive rate from one test. The conference guide asks for judge calibration against a golden set (`ZiFoTw6doGI`, `qkc1j3_k8gs`).
- **Refusal is a tripwire, not a wall.** Creators treat a model refusal on hostile input as a signal to log. The conference view says model behavior cannot be the boundary. Both hold: a refusal is a cheap alert (`ROW6KbSE1Ew`).
- **Scanners cover their scope only.** DeepSec found fewer issues than an unscoped agent review and missed runtime, concurrency and logic bugs (`qkc1j3_k8gs`).
- **Numbers are more common here, but mostly single-run.** Context Mode's 31 percent saving comes from two single runs, a log-analysis task and a JSON task (`Afm-GNrJbEQ`). Most headline figures in the local-model video are third-party research (`3mx84MRj8lY`).
- **Sponsored or paid-tier content.** DeepSec and Agit carry promotional segments (`qkc1j3_k8gs`, `CHHEjuNBxoQ`). Discount their claims.

### Watch first

- `Wq6yMdt11LM` — Copy-ready npm, pnpm and bun hardening settings in one 10-minute tutorial. Best starting point for developer machines.
- `ZiFoTw6doGI` — Gateway design with credential injection, CEL verdicts and profiles. Early and tedious to set up, but the model is clear.
- `3mx84MRj8lY` — A 26-minute map of local-model risk by layer. Quality 4/5, with a template check and hardening list.
- `0p96nZsRxlY` — Spend limits and key hygiene after a real breach. Read for the checklist.
- `SbwckhZkPGs` — Per-request, per-binary policy in a live sandbox, with a default-deny demo. Vendor-adjacent, so check the claims.
- `ROW6KbSE1Ew` — Refusal as a signal and canary secrets. Short, and the idea is new to this guide.

## Watch first

- `MkRYPFIMCSA` — Deno's byte-level egress proxy: rules, credential injection, policy as code, chained verdicts. Best single design to copy.
- `ws9XcGGPBDk` — Lethal trifecta with a clear token-exchange and mission-approval answer. Admits what is not standardized.
- `4lXks428C9o` — How PostHog secured a shell-capable agent. Deterministic gate, LLM only as advisor, paired rule tests.
- `LqLoYksJ6do` — Form3: agent with production access as supply-chain actor. Withhold write and CI credentials, microVM, injection evals.
- `BInpv7lGp1o` — Harness failures: scoped approval objects, run receipts, deadlines and ordered commits.
- `NaOkR3VSfR4` — Brains and hands with a durable workflow engine and code-enforced approval.
- `I3znWC3MEXM` — Why API keys fail agents, with per-call token exchange and policy before minting.
- `rbjWzZK2LU0` — Budgets, verb triage and proxy-stamped audit. Practical for write-heavy agents.

## Implications for our projects

**AgentOS (Govrix Scout proxy, Crucible, MemoryMesh)**
- Scout is already the right place for the egress and credential pattern. Add placeholder-secret swapping so sandboxes in Crucible never hold real keys (`MkRYPFIMCSA`, `OE_lLNCNfQo`, `BM2JX9hqsVQ`).
- Keep Scout's PII and injection scan as a deterministic gate that blocks first. Use an LLM only to cut false positives, fail closed, and ship positive and negative tests per rule (`4lXks428C9o`, `Ndp5VaqFrl0`).
- Add per-identity budgets and refilling write limits in the proxy. This also covers the Redis multi-instance budget counters on the roadmap (`rbjWzZK2LU0`, `BM2JX9hqsVQ`, `Bck7ABCZRZI`).
- Crucible exec-gate: use the isolation ladder. A container is not enough for untrusted code. Prefer microVM, default-deny egress, read-only mounts for context repos (`OqM67QG_Ikk`, `OE_lLNCNfQo`, `iH_wV8BbS24`).
- MemoryMesh: redact before embedding. Check scope on write and on read. Keep provenance (`BIhiYL4U9_M`, `0uC6u0lJJl4`).
- SkillForge: gate distilled skills with injection and PII scans before they enter the shared library (`u-o0sW9nwmk`, `iKQ78wyJEXU`).
- The Merkle audit log fits the receipt pattern. Record actor, principal, plan ID, arguments and result per call (`BInpv7lGp1o`, `q-WOjZhOMCA`).

- Registry: scan skills and MCP tool descriptions at registration and keep an inventory. Add a Nubank-style three-point scan (`iKQ78wyJEXU`, `1EZdpEhwmNc`).

**ProsHarness**
- Phone-driven approvals should be scoped objects bound to run, tool, exact arguments and expiry. Missing fields fail closed (`BInpv7lGp1o`, `tDArkCqjA-c`).
- Zero-token credential handling matches the proxy-injection pattern. Keep secrets outside the model context and the sandbox (`8aVbXXvJUY4`, `xn8EsW0wxyc`).
- Checkpoint and resume: use idempotent steps, recorded side effects and an action log, so a resumed run does not repeat writes (`NaOkR3VSfR4`, `ZD9-4fW2HhM`).
- Critique and debate: use a separate reviewer context with fresh state, and verify claims against the trace (`kiClTcJUnhc`, `imFedndyXYQ`).
- Remote access to tmux sessions should stay on a private network, never the open internet (`5192csoTkVo`).

**Recurring interests**
- Cheap-model pipelines: Haiku-class models fit the broad scanning phase. Keep stronger models for review (`kiClTcJUnhc`).
- Evals: calibrate any LLM judge against a hand-labelled golden set before gating on it (`NdrSPm6NCdk`).
- Entity resolution: validate generated queries in code, deny by default, and inject tenant filters in code, not in the prompt (`spxoDAfh5ig`, `ORVh4GivEU0`).
