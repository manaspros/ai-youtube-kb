# Insights: prosharness

*Synthesized by Sonnet from 298 talks since 2026-05-18.*

Scope note. ProsHarness M1-M7 are built and tested, plus a cleanup pass and the zero-token rework (`docs/11-project-status.md`). So this review does not ask for checkpoints, plan/critique/debate, two gates, or draft PRs. Those exist. It asks what the talks say is still missing or weak. Every gap below was checked against the talk's own note in the KB.

## What we're doing right (validated by talks)

- **Park, do not wait.** A run that waits on a human owns no live process. Talks on durable agents reach the same rule. Brain, hands and session are split. State lives in an append-only log. A fresh harness resumes by reading it. See `Uv0nAf_7tyU`, `NaOkR3VSfR4`, `9QebvrrY3KY`, `4kYl2_mqmnQ`.
- **Resume from files, not from the window.** The manifest sets cwd on every resume. Fresh context beats compaction in several talks. `4kYl2_mqmnQ` clears and reloads from handoff files. `WP3hjUXd918` found full history beat compaction on their tutor, so the lesson is "do not summarise lossy", which fits our file-backed approach.
- **Independent critic.** Codex critiques the Claude finding in a separate session. Talks say self-review is a trap. Use a separate context with its own rubric. See `mR-WAvEPRwE`, `9QebvrrY3KY`, `imFedndyXYQ`, `u6jJcIFDLE4` (one owner of the final judgment; helpers return evidence only).
- **Humans gate only two points.** Plan approval and PR review. The talks agree human attention is the scarce part. See `ow1we5PzK-o`, `Ib5GBkD555M`, `rnDm57Py54A`.
- **The agent cannot merge.** The model gets no GitHub credential. The orchestrator is plain code. This matches "model proposes, harness commits" in `BInpv7lGp1o`, `NaOkR3VSfR4` and `LqLoYksJ6do`. The docs already admit the residual trust issue, which is honest.
- **Proposals only, never auto-install.** Skillrank and the miner write proposals. This fits the caution in `0vphxNt4wyk` (AI-written skills can hurt) and the loop-safety advice in `2TLXsxkz0zI`.
- **Admission control.** A concurrency lease and per-run token ceilings. `rbjWzZK2LU0` and `IavxrdVnwXM` argue for budgets over bare permission.
- **Deterministic review aids.** The session graph has zero inference. Hunks are risk-ranked by code. The talks favour deterministic checks first. See `LlgiOCmFG_w`, `6MudaeKdBSk`.
- **Ambient triggers with dedup and a lease** line up with the signal-to-PR pipeline in `zMiSRliEzv4`.

## Where we diverge from what practitioners found (risks)

- **Gate 2 relies on a human reading a diff.** `_mi3alkqy4s` and `Ib5GBkD555M` say review capacity is the real limit. `CDqzWpwkSls` showed skilled reviewers upheld fake AI flags about half the time. Our review page helps. But an approve is still a plain choice plus an effect. Risk: rubber-stamping from a phone.
- **`bypass` permission mode.** The docs add `--dangerously-skip-permissions` for machines with a command-rewriting hook. `4lXks428C9o` argues for deterministic deny rules that run before any model. A bypass run drops that layer. The file-allowlist and clean-worktree checks remain, which is something, but it is the weakest point in the safety story.
- **Worktrees per run.** `pmoDeA3RBZY` reports 70 to 80 worktrees a day crashing a machine and regrets not using one clone per session. Our concurrency cap is 3, so the risk is low today. It matters if the cap rises.
- **Model self-report in verify.** The docs describe verify as a background session that returns a verdict. `vy7o1g2iHY8` and `q4WC4TowkBo` say agents fake completion, so status must come from records, not model prose. The docs do not mention a hash-bound receipt.
- **Skillrank ranks by usage.** `0vphxNt4wyk` says usage does not show a skill helps. The catalog is also 11 hand-written entries (known gap 1).
- **No watchdog on the scheduler** (known gap 3). `BInpv7lGp1o` says every wait needs an ending and a watchdog should make stuck work visible. Killing the loop silently stops everything.
- **Headless runs inherit the user's Claude settings.** Our own docs show a case: an org hook rewrote Bash commands and broke the scoped allowlist. This is non-determinism from leaked settings.

## Gaps: things we should build or change (ranked by impact/effort)

1. **Deterministic verify receipt.**
   - What: at the verify gate, run the project's test command in the harness. Store the SHA-256 of its real output and the code state. Accept the step only if the receipt matches. Keep the model verdict as a second signal.
   - Why: agents fake completion. A touched marker file should not pass. Proofs must go stale when code changes.
   - Evidence: `vy7o1g2iHY8`, `q4WC4TowkBo`, `6MudaeKdBSk`.
   - First step: find where `verify_verdict` is journaled and add a `verify_receipt` entry. Add the kind to `KNOWN_JOURNAL_KINDS` in `lib/health.ts` (the docs warn about this).
   - Effort: small. Impact: high.

2. **Hermetic headless runs.**
   - What: run model subprocesses with a clean settings and skills surface. Record the claude version and effort setting in the manifest. Stop depending on `bypass` for hook clashes.
   - Why: leaked user settings cause non-determinism. Our RTK clash is a real example.
   - Evidence: `4lXks428C9o`, `wcUJWP6WpGM` (same stack, check external numbers locally).
   - First step: run one plan twice, once with the normal `~/.claude` and once with an isolated home, and diff the journals.
   - Effort: small. Impact: medium-high.

3. **An eval set for the harness itself.**
   - What: a fixed set of 10 to 20 real past tasks. Each has a verifier. Run raw Claude Code and ProsHarness on it. Repeat runs. Report mean, floor and ceiling, not one score.
   - Why: 321 unit tests prove the code works. They do not prove plans or fixes get better. `QuuIywMG4s8` says a score mixes model, harness and task, so test them apart.
   - Evidence: `QuuIywMG4s8`, `Xfl50508LZM`, `YIxzNZDDy1A`, `wcUJWP6WpGM`.
   - First step: take the 321-test repo's own fixed bugs as tasks. Split capability tasks from regression tasks (`Xfl50508LZM`).
   - Effort: medium. Impact: high, because every other change gets measured.

4. **Calibrate and harden the Codex critique.**
   - What: hand-label about 30 past critiques. Measure how often Codex agrees with you. Run order-swapped pairs. Try three blind passes and keep findings seen twice. Tell the critic not to trust the plan.
   - Why: the critic is a judge, and judges have named biases. The critic already runs separately, so this is tuning, not new structure.
   - Evidence: `NdrSPm6NCdk` (80 to 85 percent agreement target), `_mi3alkqy4s`, `imFedndyXYQ`, `xLxhT2ZI7UM`.
   - First step: label 30 critiques from existing run journals.
   - Effort: medium. Impact: medium-high.

5. **Validation contract in the plan.**
   - What: the plan lists checkable done-conditions before any code. Gate 2 grades against that list. Mark any step with no automated check as unverified.
   - Why: validators written after the code only confirm the code.
   - Evidence: `ow1we5PzK-o`, `mR-WAvEPRwE`, `Ib5GBkD555M` (staged plan, vertical slices).
   - First step: add a `done_when` field to the plan document and feed it to the verify and review stages.
   - Effort: small-medium. Impact: high.

6. **Approvals bound to the exact thing approved.**
   - What: record each approval with run, step, tool, exact payload hash and expiry. Re-check the hash before acting. Let an expired approval end the run. Show assumptions and trade-offs in the Gate 1 view, and log what the human edited.
   - Why: a bare approve is weak when you tap it from a phone.
   - Evidence: `BInpv7lGp1o`, `8g0g1ncwzG0`, `CDqzWpwkSls`.
   - First step: add `payload_hash` and `expires_at` to the answer record.
   - Effort: small-medium. Impact: medium.

7. **Scheduler watchdog and stall detection.**
   - What: write a heartbeat file. Alert on the phone if it goes stale. Flag a run with no file or state change for N minutes. Treat "I cannot make more progress" as a signal to resume with a new direction.
   - Why: a dead scheduler looks like a quiet day. Claude Code was seen idling about a third of the time.
   - Evidence: `BInpv7lGp1o`, `oVsEddfhdxc`.
   - First step: the `/schedule` page already reads status files. Add a "last beat older than 2x interval" check and a ntfy push.
   - Effort: small. Impact: medium.

8. **With/without ablation for skills.**
   - What: for each proposed skill, run its cases with and without it, three or more trials. Add should-load and should-not-load prompts. Keep a skill only if it wins.
   - Why: usage rank is not benefit. Skills are tied to a model, so re-run on upgrades.
   - Evidence: `0vphxNt4wyk`, `GmAQKINjv1E`, `vy7o1g2iHY8`, `7jjudsEhBtM`.
   - First step: use headless `claude -p` on two skills from the weekly proposals.
   - Effort: medium. Impact: medium.

9. **End-of-run retrospective (a cheap Stage B).**
   - What: add one closing question to each run: what was missing, what was contradictory, what would have helped. Log it. Group across runs.
   - Why: it finds missing tools and bad instructions that outside metrics miss. It also avoids the privacy problem of sending history to a model, since it only covers the run's own output.
   - Evidence: `juoNbJiZUi0`, `LqLoYksJ6do`.
   - First step: a Stop hook on the finding and implement sessions that writes to the journal.
   - Effort: small. Impact: medium.

Lower priority, noted for later: reversibility gate for loops that send or post (`2TLXsxkz0zI`); success-rate estimate before launching long unattended runs (`7vn4WpqNpck`); one clone per run if the lease cap grows (`pmoDeA3RBZY`).

## Ideas to steal

- **Receipt plus stale-proof check.** Tie each proof to the current code state so an old receipt cannot pass a new change (`q4WC4TowkBo`).
- **Gotchas-only skills.** WorkOS cut 10k generated lines to 553 lines of gotchas and kept only skills that raised pass rate (`vy7o1g2iHY8`).
- **Judge calibration loop.** About 30 labelled cases. For each disagreement, find the missing fact and add it to the prompt. Also set an upper bound to catch overfit at 100 percent (`NdrSPm6NCdk`).
- **Consensus filter.** Several independent review passes, keep recurring findings. A cited study reports up to 44 percent better review quality (`_mi3alkqy4s`).
- **Blind adversarial verifier.** Give the verifier only the claim and tell it to assume the claim is false (`imFedndyXYQ`).
- **Rubric first, evidence per criterion.** One verifier moved a measured success rate from 74 to 38 percent on the same agent, because the old judge was too generous (`xLxhT2ZI7UM`).
- **Reversible actions run, irreversible ones are drafted.** The loop writes its stop reason to a file (`2TLXsxkz0zI`).
- **Loud versus silent failure triage.** Automate verbs that fail loudly. Send silent ones to the phone. Add a per-hour cap on deletes (`rbjWzZK2LU0`).
- **Loop gate.** Skip a scheduled run while the last PR from that loop is still open. Commit a baseline of violations and fail PRs that add new ones (`xIt_mTQp6mY`).
- **Harness-owned commit.** Keep push, PR and CI calls in plain code, and vet for empty files and stray binaries before commit (`LqLoYksJ6do`).
- **Retry classes.** Split model errors from infrastructure errors so only infrastructure failures are rerun (`wcUJWP6WpGM`).
- **Event-triggered resume.** Resume a parked run when CI fails, not only on a manual command (`zMiSRliEzv4`).
- **Check the tool is actually called.** Measure whether the model uses a tool or skill you add, over repeated runs (`KhRjivBSwiw`).
- **Work log with a commit hook.** Block a commit that does not update the log, so a new session can resume (`6MudaeKdBSk`).
- **Prompt search later.** GEPA-style reflective optimisation of plan and critique prompts, with a held-out split and a rule that the optimiser cannot edit the eval (`OA-Mc60Rboo`, `A48uhxfxbsM`, `aHhB3sjGjkI`). Do this only after gap 3 exists.

## From creator channels (Kai Explains, AI LABS, Better Stack)

Source: 1,096 creator-channel notes (163 Kai Explains, 285 AI LABS, 648 Better Stack), eight of them opened for detail. Most are single creator videos, so treat them as leads to test, not proof.

### Ideas and tools to try (ranked, each: what, why for this project, `video_id`)

1. **Log effort, resolved model, Claude Code version, output tokens and tool calls for every run.** A quality drop then points to a model change, a default change or a harness change. This is a small change to the checkpoint record. `SxLUx8-hN1o`
2. **Check loops and schedules against the two limits of Claude Code's built-in loop.** Its cron tasks expire after three days and live only in session memory. Confirm ProsHarness schedules persist to disk, survive a restart, and fail loudly on expiry. `Xxqu-kz00gw`
3. **Give every unattended loop a named automated pass/fail check and a retry cap.** The decompilation loop in the talk stops at 12 attempts per function and feeds the diff back each time. Refuse to run a loop that has no check. `hl6VOfzky5E`
4. **Allow only commits for agents on a shared repo, shard worktrees, and give reviewers only the diff.** The Bun port hit stash and reset collisions between parallel agents. The fix was commit-only git, no slow builds inside agent loops, and diff-only reviewers. Apply it to any parallel plan or critique fan-out. `0TSxrzBVEwQ`
5. **Bind each approval to the exact plan hash, with an expiry.** GoLive ties approval to one plan ID. The host notes its confirm flags are agent-set, so they are not proof of consent. The same gap applies to ProsHarness phone approvals. This adds evidence for gap 6 above. `HTscIrJhjDs`
6. **Measure hidden background-agent calls with OpenTelemetry, grouped by query source.** One talk reports a status-summary call every 30 seconds per active agent, each re-sending the whole conversation. Measure this in ProsHarness before choosing forked or fresh subagents as the default. `F4h3a8HFBSE`
7. **Trial a per-turn judge with a stop condition on one loop type.** Claude Code's /goal keeps working until a stated condition holds, and a small model checks after each turn. Compare it with ProsHarness loop stop rules on one feature. Pair it with a fresh-context reviewer for each branch. `PLyRe6Zk--8`
8. **Add skill trigger rate to skill ranking, and A/B a passive CLAUDE.md index against a skill.** One vendor eval found skills were never invoked in 56% of runs. Measure whether a ranked skill actually fires before trusting the ranking. `i0W90tlKfYg`

### Claims to treat with caution

- Items 2 and 4 rest on one creator video each. Claude Code's loop limits may have changed since the video, so check the current docs first.
- `PLyRe6Zk--8` is one AI LABS walkthrough. The 38-minute run and the per-turn judge description are not measured. A sponsor segment (Hedra) runs around 11:20 to 12:47. The video also promotes a paid community.
- `0TSxrzBVEwQ` relies on the speaker's summary of Bun's posts. The $165,000 cost is an API-equivalent estimate, and the 20% smaller binary is unverified. Zig's creator disputes that the rewrite was needed. Treat it as one large, unusual case.
- `i0W90tlKfYg` reports a Vercel eval secondhand. The video gives no task count, model, harness or variance, and the speaker calls the mechanism a guess. Do not assume the result holds for Claude Code skills.
- `F4h3a8HFBSE` gives cost shares from 2 to 6 percent (Anthropic) to 8 to 20 percent (community). The speaker's own figures come from two tests: about 12% in a sleep-loop session and about 8% in a three-agent Opus build. The subagent setting's exact name is not confirmed in the captions. The preload-script workaround is risky, and the speaker advises against installing it unread.
- `SxLUx8-hN1o` takes regression figures from third-party trackers and a secondhand study. The setting that pauses on model switching is not named in the talk.
- `HTscIrJhjDs` covers a new, single-author deploy tool with unverified star counts. Its critique of confirm flags is the host's reading, which cites the maintainer's own trust document. Copy the plan-ID pattern as a design idea, not as a tested design.
- `hl6VOfzky5E` uses numbers from press, Reddit posts and vendor tables. Part of the 426x cost gap is subscription pricing, not compute. The 99.2% figure is a within-four-attempts result.

## Reading list (top 10)

1. `vy7o1g2iHY8` - gates in code, hash receipts, and gotchas-only skills; closest match to our verify gate.
2. `q4WC4TowkBo` - verifier CLI and receipts; shows how to make "done" provable and stale-proof.
3. `BInpv7lGp1o` - harness failure framework: deadlines, watchdog, scoped approvals, run receipts.
4. `ow1we5PzK-o` - validation contract written before code, fresh-context validators, structured handoffs.
5. `QuuIywMG4s8` - how to test a harness apart from the model; failure-trace triage.
6. `NdrSPm6NCdk` - calibrating an LLM judge, which is what the Codex critique is.
7. `_mi3alkqy4s` - multi-pass consensus and suspicious-by-default review.
8. `SHMCGrNJJGc` - eval workflow for agents: validate judges against human labels, and use pass^k because runs are non-deterministic.
9. `0vphxNt4wyk` - skill evals, ablation, and when to retire a skill.
10. `Uv0nAf_7tyU` - brain, hands and session log; the cleanest comparison for our checkpoint design.
