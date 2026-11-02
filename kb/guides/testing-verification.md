# Guide: testing-verification

*Synthesized by Sonnet from 79 talks since 2026-05-18.*

Scope: tests, verification, proving an agent is done, QA automation, TDD with agents, and the evals that grade agents. Notes are paraphrased. Vendor talks (Sonar, Meticulous, Qodo) are flagged where used.

## State of the art

By October 2026 the field has moved from "write better prompts" to "build a verification harness." The model's claim of "done" is treated as untrusted. Evidence must come from a record the model did not write.

What practitioners do now:

- **Deterministic gates first, LLM review second.** Lint, types, compiler and tests run before any agent reviewer. A human reads last. Matt Pocock calls these layered brakes (`LlgiOCmFG_w`). Figma uses the same pyramid (`5Bn0xro2ol8`). Sentry says to stop re-prompting and turn repeat feedback into lint rules (`E3KbFLAGD6A`).
- **Done must be provable.** WorkOS stores a hash of real test output in a receipt and checks it at a gate (`vy7o1g2iHY8`). Their newest talk builds a per-app verifier CLI with doctor, drive, inspect, prove and judge steps (`q4WC4TowkBo`). Proofs are tied to the current code, so a stale receipt cannot pass.
- **Separate the writer from the checker.** Factory writes a validation contract before any code. Validators check against the contract, not the implementation (`ow1we5PzK-o`, `vGCJ7diEtrw`). Anthropic splits generator and evaluator into separate contexts. The evaluator drives the live app with Playwright (`mR-WAvEPRwE`).
- **Agents drive the real app.** Screenshots are weak proof. Recordings, full click-through flows and DB snapshots are stronger (`6MudaeKdBSk`, `YgEv7IQzGdM`, `q4WC4TowkBo`).
- **Hooks enforce what prompts cannot.** A Stop hook runs a checker and feeds failures back until all checks pass (`MpZzWMdmQCE`). Gates are code in a state machine, not text in a prompt (`vy7o1g2iHY8`).
- **Evals are tests for non-deterministic output.** The loop is: read traces, do error analysis, write code evals for hard rules and LLM judges for semantic ones, validate the judge against human labels, then gate CI (`qZj7sqmidqA`, `SHMCGrNJJGc`, `NdrSPm6NCdk`, `obfPzbapMIM`).
- **Benchmarks are suspect.** Verifiers are weak, tasks leak, and agents cheat. Teams build private benchmarks from production traces (`jWq-aZIU0kM`, `Yk87oUPVaxU`, `Ib5t2RLtxvM`).
- **Review is shrinking to a risk-routed step.** Human reading is reserved for auth, money and irreversible changes (`ZpK5PWX2YRM`, `_mi3alkqy4s`).

## Consensus patterns

1. **Never accept "done" from the agent. Require evidence.** Evidence means test output, a recording, a hash receipt, or a diff plus tool output. Sources: `vy7o1g2iHY8`, `q4WC4TowkBo`, `7P0elyLIxXo`, `bI8WyG9YB0I`, `iRcX54EO5g8`, `dYh7TQkuYFE`.
2. **Use one pinned, deterministic verification command.** Lint, types, security scan and tests all run from it. Run it after every step and again after review fixes. Sources: `-AKPRSYccJc`, `q4WC4TowkBo`, `TeGsFFNqRLA`.
3. **Order checks: deterministic, then agent review, then human.** The first two layers exist to make the third faster. Sources: `LlgiOCmFG_w`, `5Bn0xro2ol8`, `6MudaeKdBSk`, `VrpEyglYgeU`.
4. **Write the pass criteria before the code.** Examples are a validation contract, a sprint contract, a spec with property tests, and a red-green TDD prompt. Sources: `ow1we5PzK-o`, `mR-WAvEPRwE`, `IddXPepIAS4`, `5Bn0xro2ol8`, `v4F1gFy-hqg`, `-QFHIoCo-Ko`.
5. **The writer must not be the checker.** Use a fresh context, a different agent, or a different model family. Sources: `ZpK5PWX2YRM`, `mR-WAvEPRwE`, `7P0elyLIxXo`, `LlgiOCmFG_w`, `imFedndyXYQ`. Agent-written tests and self-critique are not an independent oracle (`bI8WyG9YB0I`).
6. **Turn every repeated mistake into a rule once.** The rule can be a lint rule, an AGENTS.md line or a named review check. Sources: `rnDm57Py54A`, `Wmp2Tku2PrI`, `E3KbFLAGD6A`, `YgEv7IQzGdM`, `ZpK5PWX2YRM`, `pqlWNihgdjI`. Rules must state intent, because agents game narrow lint rules (`E3KbFLAGD6A`).
7. **Make the codebase checkable.** Strict types, strong compilers, deep modules with small test surfaces and import-boundary lints all help. Sources: `ugUeZ8-b-u0`, `H7vFrcNWXzs`, `504PvfXou5Y`, `LlgiOCmFG_w`, `wpOA-UXynoM`. Factory measures agent readiness as the count of deterministic validation loops.
8. **Constrain effects, not reasoning.** Let the agent write code freely, but restrict what it may touch. Use typed SDKs, plan-as-data with a checker, and a harness that owns the final commit. Sources: `CLttOU7n6sI`, `-CnA2lGfymY`, `Lc8zRh9muoY`.
9. **Read traces before writing evals.** Do open coding, then group into root causes. Pick binary pass/fail judges with observable criteria. Sources: `qZj7sqmidqA`, `SHMCGrNJJGc`, `FB-MLPhL9Ms`, `obfPzbapMIM`, `QuuIywMG4s8`.
10. **Calibrate every LLM judge against human labels.** Check it as a classifier on a held-out split. Give it the same context the agent had. Sources: `NdrSPm6NCdk`, `SHMCGrNJJGc`, `McknwOzbmyg`, `xLxhT2ZI7UM`, `qZj7sqmidqA`.
11. **Record and replay for agent tests.** Save tool and LLM outputs at the node boundary, then replay them offline with selective stubbing. Sources: `Lc8zRh9muoY`, `0RNNfxpdbQk`, `Ib5t2RLtxvM`, `HLTa7Vcs4X0`.
12. **Reproduce first, then fix.** A bug fix with no failing reproduction counts as unverified. Sources: `iRcX54EO5g8`, `-QFHIoCo-Ko`, `q4WC4TowkBo`. Also `ZGzthw4BZiA` shows verification chained automatically after each agent edit.
13. **Verify the process and artifact, not just the answer.** Check a completed business artifact with deterministic code. Sources: `5xi_S1f9sDU`, `CLttOU7n6sI`, `dYh7TQkuYFE`.

## Disagreements & open questions

- **Should humans still read code?** Pocock and Volkov keep humans on the big picture and critical paths (`ZpK5PWX2YRM`, `LlgiOCmFG_w`). Voss and Gupta say hand review is at capacity and should be replaced by an engineered harness (`_mi3alkqy4s`, `AMiyLItEtLA`). Jain says review is mainly alignment, so review intent and evidence instead of diffs (`YgEv7IQzGdM`). Litt adds that humans must understand code to stay creative, not only to verify it (`WkBPX-oDMnA`).
- **Is the LLM judge trustworthy?** Some use it heavily. Others show it confidently mis-grades. A web-agent judge scored 74% while the stricter verifier scored 38% on the same agent (`xLxhT2ZI7UM`). Meijer and Lean advocates want proofs instead of judges (`-CnA2lGfymY`, `lRa9sPaMyy4`).
- **Spec-first vs feedback-first.** AWS and Resonate push specs and simulation before code (`IddXPepIAS4`, `DqtmZE6Hl0g`). Jain calls spec-driven development waterfall without a feedback loop (`YgEv7IQzGdM`). Kelley finds agents write shallow tests and need humans to choose what to test (`H7vFrcNWXzs`).
- **Rigid vs human-like tests.** Poolside prefers ephemeral, human-like checks that let the AI notice problems (`iRcX54EO5g8`). Meticulous argues for near-exhaustive screenshot diffs of recorded flows (`HLTa7Vcs4X0`, vendor).
- **Full rewrite of benchmarks vs repair.** DeepSWE writes tasks from scratch (`Yk87oUPVaxU`). SWE-rebench uses fresh time-split PR tasks plus manual checks (`wcUJWP6WpGM`). Programma says static environments are replayable and need stochastic variants (`CTLa_p6iOiY`).
- **Open:** how to test "taste" and polish (`oixzVKMAXG0`, `mR-WAvEPRwE`); how to stop agents gaming lint, tests and verifiers (`E3KbFLAGD6A`, `LlgiOCmFG_w`); how to measure code quality beyond pass rate (`NuePCNMpWGc`, vendor).

## How thinking changed over time

- **2026-05-18.** Fundamentals first: small TDD steps, deep modules, feedback speed as the speed limit (`v4F1gFy-hqg`). Fix the harness, not the prompt (`C_GG5g38vLU`). Factory publishes validation contracts and fresh-context validators (`ow1we5PzK-o`). Cursor and Granola have agents verify UI via previews and screenshots (`rnDm57Py54A`, `ON5LIT0M4do`).
- **2026-06-18.** Evals get honest: they are broken but useful, and need failure-trace triage (`QuuIywMG4s8`). Maturity stages of evals appear (`FB-MLPhL9Ms`). Agents fake completion, so receipts and gates arrive (`vy7o1g2iHY8`). Benchmark hygiene shows up: leakage, infra noise, cheating (`wcUJWP6WpGM`).
- **2026-07-18.** The question shifts to "what proof does this change need?" (`ZpK5PWX2YRM`). Done becomes a structured object (`7P0elyLIxXo`). Replayable traces replace chasing determinism (`Lc8zRh9muoY`). Stop hooks make verification shareable (`MpZzWMdmQCE`).
- **2026-08-18.** Benchmarks themselves are audited (`jWq-aZIU0kM`, `CTLa_p6iOiY`, `Yk87oUPVaxU`). Production traces become private simulation benchmarks (`Ib5t2RLtxvM`). Verification debt is named, mostly by vendors (`03l29gJXpCE`, `VrpEyglYgeU`).
- **2026-09 to 2026-10.** Code survival becomes a metric (`I2LL_wd89-A`). The review-is-dead argument gets data (`_mi3alkqy4s`). Workshops teach the full eval loop (`qZj7sqmidqA`, `SHMCGrNJJGc`, `obfPzbapMIM`). The newest talks make verification a first-class CLI with proof receipts (`q4WC4TowkBo`). Formal proof for agent code appears (`lRa9sPaMyy4`).

## Numbers worth remembering

- Code survival of agent-written code: 55% with GPT-4.1, 86% with Claude Opus 4.6 (`I2LL_wd89-A`).
- SWE-Bench Pro verifiers: about 8.5% of tasks accept wrong code and over 24% reject correct code (`jWq-aZIU0kM`, per a DeepSWE comparison).
- Replay of recorded traces matches a frontier model on OS World and Mobile World. The script is under 1 MB. Rollout-only 95% CIs cover truth only about 17-20% of the time (`CTLa_p6iOiY`).
- Web-agent judge: 74% (old judge) vs 38% (universal verifier) for the same agent. Cohen's kappa 0.58, equal to human-human (`xLxhT2ZI7UM`).
- Judge calibration target: 80-85% agreement on about 30 hand-labelled cases. A live demo reached 27 of 30 (`NdrSPm6NCdk`). A clinical judge reached F1 0.96 on 240 examples (`McknwOzbmyg`).
- Built-in correctness judge scored 0 of 13 and 0 of 16 on live-data reports, because it could not verify fresh facts. Faithfulness judge flagged 14 of 16 as unfaithful (`qZj7sqmidqA`, `SHMCGrNJJGc`).
- Per-step 99% success over 100 steps gives about 36% end to end. A 50% run reaches about 94% per transaction with four retries (`5xi_S1f9sDU`).
- Reviewers lose effectiveness past about 400 lines per sitting (Cisco study, cited). Agent users wrote about 741% more code but shipped about 30% more (`_mi3alkqy4s`).
- Mission validators: about 50% of final lines are tests, about 90% coverage, longest run 16 days (`ow1we5PzK-o`).
- Spreadsheet agent: 50% to 92% accuracy over four months. One REPL replacing 15 tools reached 74% (`HEFSExa0xl0`).
- Eval of a flag-cleanup agent: 7 of 7 PRs passed CI, about $1.26 per PR (`6MudaeKdBSk`).
- Amazon pilot: 4.5x median deployment velocity for teams that changed how they work, under 3x for tool-only teams (`pqlWNihgdjI`).
- Cedar runs about 100 million differential random tests nightly before any release (`lRa9sPaMyy4`).
- Threat-model-aided vulnerability triage: about 90% true positives, and above 75% is called good (`imFedndyXYQ`).
- Survey figures from vendors: 96% of developers do not fully trust AI code; under half fully verify before merge (`bI8WyG9YB0I`).

## From creator channels (Kai Explains, AI LABS, Better Stack)

Scope: 74 creator videos in this category. Most are single-creator tutorials or news pieces. Few measure anything, so most items below rest on one video. Sponsored or plug segments sit in `S49gppZl8H0`, `qLfSDQ5NGh0`, `5lycYTOYbPM` and `y2ifUC9_zuU`.

### Practical playbook

1. **Name the pass/fail command before the loop starts.** Cap the retries. A decompilation loop allows up to 12 attempts per function and feeds the byte diff back each time (`hl6VOfzky5E`). Skip loops where no grader exists (`hl6VOfzky5E`).
2. **Freeze the checks.** Write the checks first and have the user approve them in plain words. A script moves them to a locked folder. A Claude Code settings rule blocks edits there, and the folder is committed (`qLfSDQ5NGh0`). The video does not show the settings key.
3. **Gate each feature on `eval.md`.** Each feature gets a spec and an eval file of strict pass/fail checks. A human approves the evals before any code is written. A hook blocks marking the task done until the evals pass (`S49gppZl8H0`).
4. **Use a stop hook for completion.** When the agent tries to stop, a check runs. On failure the hook exits with code 2 and the agent keeps working (`bBMp5tLxShQ`). The hook config and check script are not shown.
5. **Guard protected paths with a PreToolUse hook.** The hook reads the target path. For a test folder it prints a message and exits 2. Exit 0 lets the action run. Other non-zero codes are logged but do not block (`TmsH-RIHvas`).
6. **Add a lint gate whose messages tell the agent the fix.** Add a `lint` script with a hand-picked oxlint rule set. The agent runs it, reads the messages and repairs until clean (`mmrSYvYKD9g`).
7. **Write tests first, then ban test edits.** Tell the agent to write tests first, then implement without touching the test files. The speakers had a forced-TDD problem that this cue fixed (`romGzY0Xu0s`). Check the commit history to confirm the red step ran (`lq3rzXP4_vs`).
8. **Print only failures into the agent context.** Write full logs to a file the agent opens when it needs detail (`SVREdZHPG1I`).
9. **Verify UI with a snapshot, act, screenshot loop.** Install the CLI globally with npm (`npm install -g agent-browser`) and have the agent run `agent-browser --help`. Snapshot the page, act on element refs such as E2, then screenshot. Fall back to ARIA role or label if refs are unstable (`P7JrP57AxR0`). In the demo a text-only model could not read the screenshots, so the presenter would pick a multimodal model (`P7JrP57AxR0`).
10. **Run a fresh-chat review after each task.** A review command reads the task status and lists what to test. Start a new chat first. Ask for high, medium and low findings, and apply them before the next task (`TVetQbcgdMU`).
11. **Demand the artifact, not the claim.** Read the walkthrough with screenshots or recordings, not only "tests passed" (`KLq250wGeEg`). Screenshots miss timing bugs, so add a recording or a state check (`PLyRe6Zk--8`).
12. **Run a builder, verifier and reviewer loop with stop rules.** Use fresh-context sub-agents. The orchestrator keeps a `state.md` with the round and open failures. Cap rounds at three or five. After round one, review only the delta from the last fix. Tag each finding with its problem class so every instance gets fixed (`S49gppZl8H0`). The delta rule and the repeat-finding figure come from one team's report, relayed in the video.
13. **Give adversarial reviewers only the diff.** Two reviewers see the diff without the implementer's reasoning. A fixer applies their suggestions. If a fix needs a long comment to justify it, the fix is wrong (`0TSxrzBVEwQ`).
14. **Keep agents off shared git state.** When agents share one repo, allow only commits. Forbid stash, reset and slow builds. Shard the work across worktrees (`0TSxrzBVEwQ`). Or give each agent its own clone and push back (`SVREdZHPG1I`).
15. **Stop on plateau, not only on a threshold.** Track the critic score per round, by category. Change strategy when it flattens. One run stalled in the 70s after 19 hours (`viHqe5QqTd0`).
16. **Tag claims by evidence.** Each agent claim is seen (with an evidence ID), guessed or unknown. Review the guessed items before acting on them (`rw0fqnrZgNM`).
17. **Check self-reported coverage against an answer key.** Plant canary tokens across test pages. Compare the agent's marker list with the key. Agents have reached content through side paths that their own pipeline could not use (`OlNZCtk100Q`).

### Tools creators recommend (tool — what for — `video_id`)

- agent-browser (Vercel) — Chromium-only CLI for snapshots, clicks and screenshots in agent UI tests — `P7JrP57AxR0`
- Playwright CLI skill — headless browser runs with less context than MCP; skill load about 68 tokens vs about 3.6k for MCP definitions (host's count) — `V2qjnBDZZ7A`
- Claude in Chrome extension — visual review of a running dev server after each task; early access — `TVetQbcgdMU`
- browser-tools MCP — Cursor accessibility, SEO and performance audits, with screenshots fed back to the agent — `G25UyWfYogQ`
- Puppeteer MCP — runs each feature's steps in a browser before the feature is marked done — `XWp4k9K6oK8`
- Reticle — browser check of app builds with worked / did not work / insufficient info verdicts — `Ua0APTMVcb8`
- Reverse Engineer Anything (REA) — MCP plus skill; black-box QA that follows a UI click to the request and server response — `rw0fqnrZgNM`
- objdiff with Ghidra — byte-compare loop for decompilation — `hl6VOfzky5E`
- cargo crap — per-function complexity times lack of coverage, for Rust; flags untested complexity — `XuMR1pgc6pc`
- oxlint anti-slop rules — deterministic lint gate for TypeScript and JavaScript — `mmrSYvYKD9g`
- Superpowers plugin — brainstorm, sub-agent TDD, one git commit per step — `lq3rzXP4_vs`
- GStack — review, ship and qa commands; qa tests only the pages the diff touches — `kLq5p43huYQ`
- Floci — free Docker emulator for S3, DynamoDB and Lambda for tests; host measured about 129 ms startup vs 24 ms claimed — `7s462S-qRY4`
- Agent Reading Test — canary-token check that an agent's fetch pipeline reads full pages — `OlNZCtk100Q`
- Toolgate, Abide, Belay — LLM judges at pre-action, rule-check and stop points; no judge accuracy shown — `jlEMo6Dsh9E`
- Codex CLI — outside reviewer from a different model family — `92ZDgn8bgLM`
- Visly — pixel-level visual diffs for design tests; product claim only, no benchmark — `5lycYTOYbPM`

### Where creators agree or clash with the conference talks

- **Agree: deterministic checks first.** Hooks and lint enforce rules that prompts cannot (`bBMp5tLxShQ`, `TmsH-RIHvas`, `mmrSYvYKD9g`). This matches the layered-gates consensus above.
- **Agree: the writer is not the checker.** Creators use a separate reviewer (`S49gppZl8H0`), a different model (`92ZDgn8bgLM`) and adversarial reviewers (`0TSxrzBVEwQ`).
- **Agree: lock the checks before code.** `qLfSDQ5NGh0` and `S49gppZl8H0` both fix the evals or checks before the build.
- **Agree: benchmark headlines hide the grader and budget.** `hl6VOfzky5E` shows a 99.2% within-four-attempts figure against 88% first-attempt, and a spread of about 25 points from budgets, harnesses and grading rules.
- **Clash: screenshots as proof.** Creators lean on screenshots and screenshot critics (`G25UyWfYogQ`, `TVetQbcgdMU`, `viHqe5QqTd0`). The conference section calls screenshots weak proof. `PLyRe6Zk--8` agrees with that view. Treat the creator screenshot uses as visual checks only.
- **Clash: LLM judges as gates.** `jlEMo6Dsh9E` lets judges decide completion, gated by a confidence threshold (75 in the Belay demo). The conference section shows judges that mis-grade. The creator video gives no judge accuracy data, so treat these plugins as untested.
- **Clash: TDD.** Creators say tests first fixes agent output (`lq3rzXP4_vs`, `romGzY0Xu0s`, `D4uBfIe7SzA`). The conference section finds agents write shallow tests that need human choice. `lq3rzXP4_vs` reports one skipped TDD step, and `romGzY0Xu0s` needed the anti-test-edit cue.
- **Clash: spec-first.** `M0ivqkQ5mF4` and `em3vIT9aUsg` promote GitHub Spec Kit. The conference section is split on spec-first vs feedback-first. `M0ivqkQ5mF4` gives a mixed verdict: the spec flow works, tasks run by hand, and the UI came out cluttered.
- **Human review.** `S49gppZl8H0` says review cannot be skipped, but routes it by consequence: cosmetic, broken but harmless, or lost money and data. The conference section says review is shrinking to a risk-routed step. Both agree on routing.
- **Unmeasured numbers.** The "10x" claim (`qLfSDQ5NGh0`) and the cost figures (`viHqe5QqTd0`) are single runs. The token audit in `hl6VOfzky5E` is the best-documented cost figure here.
- **Process claims.** `y2ifUC9_zuU` gives a direction-drift check and must-not-trade-off tests in CLAUDE.md, with thin detail and sponsor claims. Treat it as a pointer, not evidence.

### Watch first (3-6 `video_id` — why)

- `hl6VOfzky5E` — grader-first loops, budget-stated benchmarks, and the API-vs-subscription cost gap. Kai Explains. The most checkable data in this set.
- `S49gppZl8H0` — full review loop with eval gates, round caps and risk tiers. Has a sponsored segment, but the method is practical.
- `0TSxrzBVEwQ` — a large port run by adversarial reviewers and shared-git guardrails. The Bun numbers are the speaker's report.
- `qLfSDQ5NGh0` — frozen checks, one builder per feature, and an outer loop that rewrites rules. One app only; the 10x claim is unmeasured.
- `P7JrP57AxR0` — the snapshot-act-screenshot browser loop. No benchmark is shown, so tool comparisons rest on the presenter's preference.

## Watch first

- `q4WC4TowkBo` — newest and most concrete: verifier CLI, proof receipts, stale-proof detection, deterministic prove plus fast judge.
- `ow1we5PzK-o` — validation contract written before code, two-layer validators, structured handoffs.
- `mR-WAvEPRwE` — generator-evaluator loop with Playwright evaluator, rubric as taste, sprint contracts.
- `vy7o1g2iHY8` — gates in code, hash-verified test receipts, paired evals for skills.
- `SHMCGrNJJGc` — hands-on eval workflow: traces, code evals, five-part judge prompt, judge validation.
- `xLxhT2ZI7UM` — why LLM judges mis-grade, and a rubric-plus-evidence verifier design.
- `jWq-aZIU0kM` — how to audit any benchmark's verifiers and prompts.
- `Lc8zRh9muoY` — record at the node boundary, replay with stubs as regression tests.

## Implications for our projects

**AgentOS**
- **Crucible and the exec gate.** Add a "done receipt" for sandboxed runs: store a hash of real command output and check it before reporting success (`vy7o1g2iHY8`, `q4WC4TowkBo`). Separate controls on what code may do from checks on what it produced (`bI8WyG9YB0I`).
- **Next-phase thesis (benchmarks plus correctness checks).** Copy Snorkel's anatomy: pinned environment, oracle solution that proves the task is solvable, hidden verifiers (`Ib5t2RLtxvM`). Replay-baseline your own benchmarks to see if they are gameable, and use hierarchical CIs for p95 claims (`CTLa_p6iOiY`).
- **Govrix Scout.** Record at the boundary and replay offline. Scout already sees every call, so it can write node-boundary traces for zero-model-call regression tests (`Lc8zRh9muoY`, `0RNNfxpdbQk`). Fix guardrails on tools, not on the LLM.
- **MemoryMesh RAGAS evals.** Do trace-first error analysis. Use faithfulness judges that see the retrieved context, not correctness judges that rely on training data (`qZj7sqmidqA`, `SHMCGrNJJGc`). Calibrate each judge on about 30 labelled cases (`NdrSPm6NCdk`).
- **InferCraft.** Use a keep-or-revert benchmark loop with a correctness check and a guard against reward hacking for kernel and cache-strategy tuning (`vrDvatGtIxs`). Do napkin math before benchmarking (`jQDXzEVHMSE`). Check external numbers on your own stack (`wcUJWP6WpGM`). Seeded fault injection suits the priority scheduler (`DqtmZE6Hl0g`, `jQDXzEVHMSE`).
- **SkillForge.** Measure each mined skill with and without it, and keep it only if pass rate rises (`vy7o1g2iHY8`). Keep skills as short gotcha lists. Validate code examples inside skill documents (`E3KbFLAGD6A`).
- **Redis budget counters and DuckDB tier.** Use differential testing against a simple spec model, run nightly (`lRa9sPaMyy4`). Add proxy-based fault injection in CI (`jQDXzEVHMSE`).

- **Registry.** Treat catalog entries like skills: test with and without (`vy7o1g2iHY8`).

**ProsHarness**
- **Checkpoint/resume.** Add a work log with commit-hook enforcement so a fresh session can resume (`6MudaeKdBSk`). Use fresh-context loops with disk state (`c35YoMdnI78`, `Wmp2Tku2PrI`).
- **Plan, critique (Codex), debate.** Cross-model verification matches the pattern (`7P0elyLIxXo`, `AgBAOXVxt4A`). Keep the critic in a separate context (`mR-WAvEPRwE`). Have the author tag claims as measured, checked, inferred or assumed (`dYh7TQkuYFE`).
- **Run completion.** Make "done" a structured object with artifact, evidence, verifier and residual risk (`7P0elyLIxXo`). Use a Stop hook that returns failing checks to the agent (`MpZzWMdmQCE`).
- **Phone approvals.** Gate only high-impact steps and send evidence with the approval request (`so9l_MwS2yg`, `e9-br9hveRI`).
- **Zero-token credentials.** Inject secrets from deterministic pre-turn code, not the prompt (`C_GG5g38vLU`). Add a secret-blocking hook (`bI8WyG9YB0I`).
- **Skill ranking.** Use paired with/without evals as the signal (`vy7o1g2iHY8`).

**Entity resolution with cheap models**
- Keep a hand-labelled golden set, run deterministic checks first, then a binary judge from a different model family (`NdrSPm6NCdk`, `SHMCGrNJJGc`). Use control-total anchoring and a source-anchored adjudicator for disagreements (`dYh7TQkuYFE`). Write code evals for fixed rules and judge only the fuzzy cases (`obfPzbapMIM`). For cheap-model pipelines, strong guardrails move cost from the model to the harness (`MpZzWMdmQCE`).
