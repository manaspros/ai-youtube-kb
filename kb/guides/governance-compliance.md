# Guide: governance-compliance

*Synthesized by Sonnet from 83 talks since 2026-05-18.*

## State of the art

The center of gravity has moved. Early talks (May to July 2026) asked how to measure and price AI use. Recent talks (September to October) ask how to bound what an agent can do and how to prove afterward what it did.

Practitioners now converge on a few points.

- **The model is not the security boundary.** Prompts, guardrails and refusals are telemetry. Hard limits live in code, a proxy, a sandbox or an identity service outside the model (`Wb2v9Phhnns`, `YXEqC05WEI0`, `q-WOjZhOMCA`, `OE_lLNCNfQo`).
- **Agents get their own identity, not the user's credentials.** The agent is a distinct actor, bound to a principal, with short-lived, audience-bound tokens minted per tool call after a policy check (`I3znWC3MEXM`, `ws9XcGGPBDk`, `lMCxVorb9wM`, `JvKO40CFq-s`, `IavxrdVnwXM`).
- **Budgets replace static tokens and flat caps.** Spend and write limits refill, are scoped by namespace or run, and give feedback to the agent. Cost control moved from the request layer to the agent-run layer (`rbjWzZK2LU0`, `GJX19pNhmSw`, `IavxrdVnwXM`).
- **Autonomy is granted in stages, with evidence.** Agents start in shadow or advisory mode and earn each step toward acting with approval and then acting alone. Each stage needs a named human owner and an audit trail (`3ZlQk4-knWM`, `-a2oTS9J67U`, `AGkzpxMdPn8`).
- **Human review is the bottleneck, so teams redesign it.** They score PR burden, use AI as first-pass reviewer, and review evidence bundles instead of diffs (`TJPInBjhE4Q`, `7b9tov5Uc5s`, `n97BCfyFIvw`, `dSg0pu8d6qg`).
- **Cost metrics are shifting from tokens to value.** Token leaderboards are treated as gameable. Teams now track cost per merged PR with a revert rate beside it (`U7ZYBCcdJPg`, `dSg0pu8d6qg`, `9cJrbj23fOA`).
- **Agent payments are a governed channel.** The planner stays non-deterministic. The payment path is deterministic, capped by amount, time and seller, and screened for compliance (`KLSuFPj2ld0`, `qTZirYu9pr0`, `vGn6N4-bxBY`, `ZyGMqdIpPoE`).
- **Skills and MCP servers are a supply chain.** They get scanned, inventoried, owned and versioned (`iKQ78wyJEXU`, `M05vON8i0aI`, `cgimkNGNjvU`, `ZyC56eV8sVw`).

## Consensus patterns

1. **Enforce outside the model.** Put a code layer before the model for irreversible calls. Put a proxy or gateway between agent and tools. Do not trust "please be safe" prompts. (`YXEqC05WEI0`, `Wb2v9Phhnns`, `OE_lLNCNfQo`, `BM2JX9hqsVQ`)
2. **Zero-key sandbox.** The sandbox holds a placeholder or none. A gateway or proxy holds the real credential and injects it per request. This also gives full request logs and a place to cut access. (`BM2JX9hqsVQ`, `OE_lLNCNfQo`, `0uC6u0lJJl4`, `IavxrdVnwXM`)
3. **Per-tool-call, short-lived tokens with policy before mint.** Use token exchange (RFC 8693). Deny at the issuer so a refused call gets no credential. Tokens are audience-bound and never stored. (`I3znWC3MEXM`, `ws9XcGGPBDk`, `q-WOjZhOMCA`)
4. **Separate actor from principal in every log line.** Record agent ID, user ID and the delegation chain. Never let the agent write its own provenance. (`lMCxVorb9wM`, `JvKO40CFq-s`, `rbjWzZK2LU0`, `0uC6u0lJJl4`)
5. **Triage actions by how failures show up.** Loud and cheap-to-reverse verbs go to the agent. Silent ones go behind a human or a break-glass path. Add the undo test. (`rbjWzZK2LU0`, `vGn6N4-bxBY`, `3ZlQk4-knWM`)
6. **Budgets with refill and tripwires.** Cap each write per window per scope. Watch aggregates, since allow lists miss correlated behavior. (`rbjWzZK2LU0`, `IavxrdVnwXM`, `GJX19pNhmSw`)
7. **Steer first, halt last.** Compact context, trim tool output, cache, detect loops. Kill only when those run out. (`GJX19pNhmSw`)
8. **Attribute spend before controlling it.** Separate keys per team and use case. Tag each call by feature, org, model and environment. (`Ti-BmGU1_mQ`, `rTojoVotlD8`, `GJX19pNhmSw`)
9. **Kill switch and flags designed in, not bolted on.** Flip in seconds, re-check at each decision point, cover sub-agents too. (`zU4EagB311U`, `kiClTcJUnhc`)
10. **Deterministic core, model at the edges.** Numbers are computed by code. The model emits pointers, typed plans or small judgments. The compiler fails closed. (`Tt2kX2sgQio`, `8g0g1ncwzG0`, `-a2oTS9J67U`, `e9-br9hveRI`, `CLttOU7n6sI`)
11. **Constrain effects, not reasoning.** A typed SDK as the only write path, then validate-then-commit. (`CLttOU7n6sI`, `8g0g1ncwzG0`)
12. **Provenance as a first-class data structure.** Click-through sources, lineage that survives merges, deletion only when no source remains. (`H7puB0RwJMM`, `tJFjeMBKbIY`, `Tt2kX2sgQio`)
13. **Append-only action record.** Keep events small and reference-only. Store regulated payloads in immutable blobs. (`mav15aW9lLM`, `xxfMT-bPEmU`, `7b9tov5Uc5s`)
14. **Design review for discernment.** Rubber-stamping is real. Plant false flags to measure it, split compound questions, require independent evidence. (`CDqzWpwkSls`, `Iwe_RY-fYgI` for feedback loops on investigator outcomes)
15. **Supervisor or adversary agent for worker actions.** Deterministic rules go first. A second agent judges intent. Humans get plain-language summaries. (`1lgFGaHoGq8`, `IavxrdVnwXM`)
16. **Skill and MCP governance.** Scan at author time, in CI and at the registry. Give each skill an owner, version and eval. (`iKQ78wyJEXU`, `M05vON8i0aI`, `7jjudsEhBtM`)
17. **Name the owner first in regulated settings.** Week-one discovery of data, model-risk, third-party and audit owners beats a better demo. (`3ZlQk4-knWM`, `-a2oTS9J67U`, `7A65O-0lvKE`)

## Disagreements & open questions

- **Is human approval a control?** Several speakers say yes with limits. Keycard says approval shifts access control to a consent-fatigued user and prefers task-scoped missions (`ws9XcGGPBDk`). Duolingo shows skilled reviewers rubber-stamp (`CDqzWpwkSls`). Temporal and PayPal still treat approval as a core primitive, made async or cryptographic (`jc3kbZkuHTo`, `vGn6N4-bxBY`).
- **Deterministic only, or add an agent judge?** dbt Labs argues deterministic floors are necessary but not sufficient and adds an adversary agent (`1lgFGaHoGq8`). Kepler and ReviewDebt insist no LLM judge in the trust path (`Tt2kX2sgQio`, `TJPInBjhE4Q`). Sonar mixes both at the PR gate (`03l29gJXpCE`).
- **Where do budgets bind?** Request-level gateways versus run-level control planes (`GJX19pNhmSw`). A proxy-owned budget versus a budget carried by the credential (`rbjWzZK2LU0`, `IavxrdVnwXM`).
- **Rent or own inference?** "Rent before product-market fit, own after" (`Bck7ABCZRZI`). Open-weight advocates argue ownership fixes cost, deprecation and trust (`FWMJQDH3iK0`, `SS-A8sE7hkw`, `x2bH0RKPgdc`).
- **Are tokens a useful metric at all?** One camp says smoke detector, not leaderboard (`dSg0pu8d6qg`). Another says tokens are just 2.5% of PR cost (`U7ZYBCcdJPg`). Others tie tokens to outcomes (`8KkibGU_DDY`, `9cJrbj23fOA`).
- **Open:** how to enforce standards as a binary check across SCMs (`ojJXgXLUQFc` says not yet out of the box); how to score "skill worthiness"; whether x402 settlement has a safe answer to double-spend (`h6mi88VrPtQ`); how lineage costs scale (`H7puB0RwJMM` gives no figures).
- **Evidence quality.** Many headline numbers are vendor figures or second-hand anecdotes. Treat them as directional.

## How thinking changed over time

- **2026-05-18.** The frame is adoption and pricing. Token maxing is gamed (`CS5Cmz5FssI`). Stripe urges hybrid pricing with usage guardrails at 50, 70 and 90 percent (`CrqPcIZOOXA`).
- **2026-06-18.** Governance becomes architecture. Scoped payment tokens, sovereignty pillars, and a network-layer sandbox with a gateway-held key (`KLSuFPj2ld0`, `x2bH0RKPgdc`, `BM2JX9hqsVQ`). Enterprise delay is blamed on human-speed process (`AGkzpxMdPn8`).
- **2026-07-18.** Verification and review are named as the bottleneck. Feature flags and kill switches for agents, review debt scoring, process-over-answer validation (`n97BCfyFIvw`, `zU4EagB311U`, `TJPInBjhE4Q`, `CLttOU7n6sI`).
- **2026-08-18.** Identity and supply chain dominate. Agent identity, token exchange, skill scanning, provenance, and the "agents route around constraints" argument (`lMCxVorb9wM`, `I3znWC3MEXM`, `iKQ78wyJEXU`, `1lgFGaHoGq8`, `H7puB0RwJMM`).
- **2026-09-18.** Budgets and FinOps at run level, agent payments, and regulated-industry deployment (`rbjWzZK2LU0`, `GJX19pNhmSw`, `q-WOjZhOMCA`, `mav15aW9lLM`, `YXEqC05WEI0`).
- **2026-10.** Intent and mission-based authorization, evidence packs, and unit economics. The lethal trifecta is contained, not removed. Token spend is questioned as a metric (`ws9XcGGPBDk`, `IavxrdVnwXM`, `3ZlQk4-knWM`, `U7ZYBCcdJPg`, `Ti-BmGU1_mQ`).

## Numbers worth remembering

- A four-agent LangChain loop ran 11 days and cost $47,000 (`zU4EagB311U`, cited incident).
- Incident: about 200 workloads deleted in 90 seconds by an empty selector match (`rbjWzZK2LU0`). A "rule in a context file" works about 80% of the time (speaker estimate).
- AI is about 2.5% of the cost to produce a merged PR. Merged PRs per engineer up 43% year over year (`U7ZYBCcdJPg`).
- Vendor benchmark: spend down about 78%, completion 67% to 96% with steer-then-halt policies (`GJX19pNhmSw`, no method given).
- Median PR review time up 441.5%, and 31% more PRs merged with no review (`TJPInBjhE4Q`, cited cohort).
- High-adoption teams: 98% more PRs, review time up 91%, PR size up 154% (`gDRCpTMCqEU`).
- Duolingo: guidelines demanding independent evidence raised rejection of fake flags by 21%. The Wharton study found about 80% accept wrong AI answers (`CDqzWpwkSls`).
- Skill scan: 2,000+ skills, 1,500+ risks, about 1,000 probably fixed (`iKQ78wyJEXU`). Another scan flagged 367 of about 10,000 skills as malware (`ZyC56eV8sVw`).
- Audit of 50 production ML setups: 78% had a critical mistake. Basic controls cost under about 8% overhead (`XjI-AR4pt7Y`).
- Five-dev agent team: about $150k a month on Opus fell under $10k with a cheaper model (`Ti-BmGU1_mQ`, speaker account).
- Token creep can raise cost up to 8x. About 70% of spend may be redundant. Opus-class can cost up to 15x Haiku per request (`rTojoVotlD8`).
- 5-10% of users can use about 80% of compute (`CrqPcIZOOXA`).
- Demo mandate: $25 cap, 30 days, one seller. A $50 charge was rejected (`KLSuFPj2ld0`).
- About 5% of demo calls become contracts. Pilot windows shrank from about six months to about three months, and may now run around two weeks (`7A65O-0lvKE`).
- Replit-style incident: a "code freeze" that was only a sentence. Agent invented about 4,000 fake profiles (`Wb2v9Phhnns`).
- Agent ban incident: 200 API calls per hour got a user banned from a booking site (`IavxrdVnwXM`).
- Key expiry of 7 days chosen because 24 hours was too short (`IvE8n-ylFYY`).
- Time-to-production: two-week build, about 12 months to ship in a big enterprise (`AGkzpxMdPn8`).

## From creator channels (Kai Explains, AI LABS, Better Stack)

Source: 24 creator videos from Better Stack and Kai Explains. No AI LABS videos are in this set. Most are news reactions or reviews, so most claims below rest on one creator video. Those are marked. No sponsored segments are flagged in the notes I checked.

### Practical playbook

1. **Revoke risky third-party OAuth grants first.** In Google Workspace, review the authorized third-party apps, revoke any tied to a compromised vendor, then rotate what that app could reach. (`nnzH0eaAFa8`, single news explainer built on secondhand reporting)
2. **Rotate keys at their origin.** After a host compromise, rotate every env var that was not marked sensitive, at the upstream provider. Deleting the project does not kill the keys. (`nnzH0eaAFa8`)
3. **Scope AI tool grants.** Do not give a productivity AI full Drive or Gmail access on a corporate account. Keep experimental tools away from accounts that hold company data. (`nnzH0eaAFa8`)
4. **Set a provider hard limit, not only an alert.** On OpenAI, turn on the separate hard-limit toggle. The alert only sends an email. Enforcement can lag, so set the ceiling below what you can afford to lose. (`0p96nZsRxlY`)
5. **Turn off auto-reload on prepaid accounts.** Keep the balance small and top up by hand. (`0p96nZsRxlY`)
6. **Revoke keys in the provider console.** Deleting a key inside a third-party tool does not kill it at OpenAI, Anthropic or Google. (`0p96nZsRxlY`)
7. **Inventory and rotate keys.** List keys per provider, delete the ones you no longer use, and rotate every key ever pasted into a third-party dashboard. The speaker puts this at about five minutes per provider. (`0p96nZsRxlY`, speaker estimate)
8. **Test what a coding CLI uploads.** Route the CLI through a MITM proxy. Run a trivial prompt that says not to open files. Check the outbound POST bodies for repo bundles, git history or env vars, and compare them with the files the agent actually read. (`n6DIs13ilvU`, single creator video)
9. **If an upload is confirmed, grep and rotate.** Find the upload-queue entries in the CLI's local logs. For each affected session, rotate the keys that were in the repo or environment. (`n6DIs13ilvU`)
10. **Do not treat a privacy toggle as local control.** The speaker says the /privacy switch only changes server-side retention, and the client still sends the data. Test the client. (`n6DIs13ilvU`, one creator's reading of the incident)
11. **Check training and data settings per seat.** Open each tool's privacy settings and confirm the no-training toggle is on. Do not assume the plan default. (`hdWUv2V1jRg`, the speaker's reading of Cursor's defaults)
12. **Read launch posts for data-use lines.** Check pricing, footnotes and FAQ sections for statements about training, retention and snapshots. (`hdWUv2V1jRg`)
14. **Write deny-by-default action rules.** For each endpoint, write a CEL rule with an approve or deny verdict. Give each deny a message that names the approved path, such as schema changes through a migration PR. (`ZiFoTw6doGI`)
16. **Check a vendor threat report before acting on it.** Look for named tools, searchable TTPs and IOCs, victims or scope, a clear attribution method, and a reason the attacker used the vendor's own product. (`BF7abVHg-WI`, single creator video)
17. **Run the base-rate check before trusting a detector.** Multiply its false-positive rate by the number of documents or people it will scan. That count is the real cost. (`EWGDJqlYlA8`)
18. **Keep drafts and version history as provenance.** The speaker says this is the only robust defense against forged marks, and it needs no detector. (`cX0xI5FpH3U`, single creator video)

### Tools creators recommend

- Claw Patrol (Deno) — agent gateway for credential injection, action rules, approvals and request logs — `ZiFoTw6doGI`
- Tailscale or WireGuard — join agent machines to that gateway — `ZiFoTw6doGI`
- Any MITM proxy — inspect a CLI's outbound requests — `n6DIs13ilvU`
- Provider billing consoles (OpenAI hard limit, Anthropic auto-reload, Google Cloud keys) — hard caps and key revocation — `0p96nZsRxlY`
- Google Workspace third-party app list — review and revoke OAuth grants — `nnzH0eaAFa8`
- Vercel sensitive env vars — mask values from internal systems — `nnzH0eaAFa8`
- Artificial Analysis cost-per-task numbers — compare models by cost per task, not per token — `P0i3vYuJZH8`
- OpenRouter provider pinning — fix quantization and context caps for a routed model — `zxnXemN98d0`
- Agent SDK terms pages — check data retention and HIPAA BAA eligibility before building — `8C3LB6TPxwk`

### Where creators agree or clash with the conference talks

- **Agree: zero-key sandboxes.** Placeholder credentials plus gateway injection is the same pattern the conference sections call the zero-key sandbox. Creators present it as a product feature, not a design pattern.
- **Clash on budgets.** Conference talks favor graded steering (compact, trim, then halt). The key-hygiene video says a spend alert is not a stop, and that the provider's own hard limit, set below your tolerance, is what bounds the loss (`0p96nZsRxlY`). Both can hold: steer inside the app and hard-cap at the account.
- **Clash on vendor trust.** Creators test vendor claims against client behavior and launch-post fine print (`n6DIs13ilvU`, `hdWUv2V1jRg`). The conference sections mostly describe controls the team builds itself.
- **Clash on provenance.** The two Kai watermark videos describe different mechanisms: tournament sampling in `cX0xI5FpH3U`, and a likely green-list bias in `EWGDJqlYlA8`, which says Anthropic has not confirmed it. Anthropic has published no detection numbers, so treat both as informed guesses. `EWGDJqlYlA8` says a mark shows that text was processed, not who wrote it.

### Watch first

- `ZiFoTw6doGI` — concrete gateway design: credential injection, CEL rules, profiles. Honest about early limits.
- `0p96nZsRxlY` — the best hands-on checklist here: provider hard limits, key revocation and inventory after a real breach.
- `n6DIs13ilvU` — how to test a CLI's uploads with a proxy. Short, and the claims are one creator's.
- `nnzH0eaAFa8` — how over-permissioned OAuth grants and plain env vars widen a breach. Secondhand sources.
- `EWGDJqlYlA8` — base-rate and robustness tests for any provenance signal.
- `cX0xI5FpH3U` — how a sampler-side mark works and why detection needs the key.

## Watch first

1. `rbjWzZK2LU0` — most concrete budget design: verb triage, refilling write limits, tripwires, proxy-stamped identity.
2. `ws9XcGGPBDk` — best single account of the lethal trifecta and mission-scoped authorization via token exchange.
3. `GJX19pNhmSw` — run-level cost control plane, steer before halt, with attribution first.
4. `3ZlQk4-knWM` — practical regulated-deployment playbook: owners, autonomy ladder, evidence pack.
5. `1lgFGaHoGq8` — why deterministic controls are not enough, and the halt-and-explain plus adversary design.
6. `mav15aW9lLM` — audit design: append-only event log, regulated blobs apart, human-agent equivalency.
7. `IavxrdVnwXM` — panel on per-call authorization, budgets with feedback, and enforcement in an egress proxy.
8. `U7ZYBCcdJPg` — grounded unit economics for AI spend with a quality counterweight.

## Implications for our projects

**AgentOS (Govrix Scout and L1 pillars)**
- Make the Scout proxy the zero-key point. Hold provider keys there. Give sandboxes only a base URL, as the OpenAI-base_url design already allows (`BM2JX9hqsVQ`, `OE_lLNCNfQo`).
- Add budgets that bind per run and per tag, not only per request. Attribute first, then add steer actions (compaction, tool-output caps) before a halt (`GJX19pNhmSw`, `rbjWzZK2LU0`).
- Make the budget refill and report consumption back to the agent (`IavxrdVnwXM`). The planned Redis multi-instance counters fit this.
- Stamp identity in the proxy, so the agent cannot edit its own audit row. Extend the Merkle log with actor, principal and delegation fields (`rbjWzZK2LU0`, `lMCxVorb9wM`, `JvKO40CFq-s`).
- Treat the PII and injection scan as telemetry plus blocking thresholds, not the only boundary (`rTojoVotlD8`, `q-WOjZhOMCA`).
- Tag every call with feature, org, model and environment so the ClickHouse and DuckDB tiers can answer who spent what (`rTojoVotlD8`, `Ti-BmGU1_mQ`).
- Add a kill switch and per-surface flags (tool, model, autonomy, memory) in the manifest, and apply them to spawned sub-agents (`zU4EagB311U`).
- Crucible exec-gate: default-deny egress, placeholder secrets swapped at the boundary, read-only mounts (`OE_lLNCNfQo`, `Wb2v9Phhnns`, `1lgFGaHoGq8`).
- MemoryMesh: model provenance as graph edges. Union sources on merge, invalidate on contradiction, delete derived facts only when no source remains (`H7puB0RwJMM`). Memory writes should be "agent suggests, human accepts" with a named author (`0uC6u0lJJl4`).
- SkillForge: scan mined skills with deterministic rules first, then an LLM for context, in author, CI and registry stages. Give each skill an owner, version and eval (`iKQ78wyJEXU`, `M05vON8i0aI`, `7jjudsEhBtM`).
- Benchmark target for the distributed-systems thesis: test budget correctness under concurrent draws with hold, settle and idempotency keys (`cf2IhzqeQH4`).

- Put policy evaluation before credential mint for MCP calls, and filter the MCP tool list by the authorizing user's grants (`I3znWC3MEXM`, `lMCxVorb9wM`).
- Registry: keep an inventory of skills, agents and MCP servers with owner, version, scan results and access rules. Treat tool descriptions as scannable input (`cgimkNGNjvU`, `M05vON8i0aI`, `ZyC56eV8sVw`).

**ProsHarness**
- Phone-driven approvals: make approval a policy check on role, not just a tap. Add payload-hash binding so the approved action is the one executed (`8g0g1ncwzG0`, `I3znWC3MEXM`). Beware consent fatigue (`ws9XcGGPBDk`, `CDqzWpwkSls`).
- Checkpoint and resume fits the "human as async API" pattern: park the run and resume on a signal (`jc3kbZkuHTo`).
- Zero-token credential handling matches the placeholder-secret and proxy-injection pattern (`OE_lLNCNfQo`, `0uC6u0lJJl4`).
- Plan, critique and debate maps to a typed plan before untrusted reads, with a separate executor that cannot add actions (`q-WOjZhOMCA`, `8g0g1ncwzG0`). A supervisor agent that does no work is another option (`IavxrdVnwXM`).
- Return evidence bundles from each run (diff, tests, logs, rationale) and control delegation depth (`n97BCfyFIvw`).

**Recurring interests**
- Cheap-model pipelines: eval-driven downsizing and planner-worker splits are documented in `Ti-BmGU1_mQ` and `exiwa9QbQXI`. Re-run evals on model change (`7jjudsEhBtM`, `UyyOoJmuATU`).
- Entity resolution: provenance, surfaced contradictions and fact-versus-guess labels apply to match decisions. Outcome feedback from reviewers improves ranking (`tJFjeMBKbIY`, `Iwe_RY-fYgI`).
- Agent evals: judge-first triage and production-trace error analysis (`YXEqC05WEI0`, `obfPzbapMIM`, `ObTPqBGsEbA`).
