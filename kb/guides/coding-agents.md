# Guide: coding-agents

*Synthesized by Sonnet from 130 talks since 2026-05-18.*

## State of the art

By October 2026, coding agents write most of the code at leading teams. Anthropic says about 80% of its code is AI-written (`ZpK5PWX2YRM`). Greptile estimates that about 25% of PRs it reviews are fully or largely AI-generated (`474j-n1Ltxc`). The talks agree that the bottleneck is no longer typing. It is human attention, verification and deciding what to build (`pMggiOb18tc`, `so9l_MwS2yg`, `_ehJyfHg1Vk`, `_fHTqOs5wQA`).

What practitioners do now:

- **Run many agents, supervise few.** Some run 5 to 10 async agents (`rnDm57Py54A`). Some run 15 to 20 (`GdvKNwMcfd0`). Past about five minutes of runtime, humans stop watching and parallelize (`W76woOYHlvY`). Two speakers say the human is now the limit (`4kYl2_mqmnQ`, `YIVkERhy8xo`).
- **Harness over model.** Value sits in rules, skills, hooks, verifiers and sandboxes. A cheaper model with strong gates can win (`MpZzWMdmQCE`, `CoEIs6Xm8m8`).
- **Long-lived loops.** Goals with a verifier, heartbeats, pinned threads and compaction now keep work going for hours or weeks (`il1c1a2FufU`, `FwiS44-xyYw`). Manager agents delegate to worker agents and surface only a reviewed PR (`pMggiOb18tc`).
- **Verification is the product.** Hooks, test-first prompts, e2e flows, computer use and evidence receipts replace "the agent said it is done" (`q4WC4TowkBo`, `iRcX54EO5g8`, `bI8WyG9YB0I`).
- **Review is the new choke point.** Teams route review by risk, score PR burden, and ramp trust in AI reviewers in stages (`ZpK5PWX2YRM`, `TJPInBjhE4Q`, `uU5Gv2h8-9g`).
- **Shorter prompts for newer models.** Anthropic removed about 80% of the Claude Code system prompt for the newer model class (`9fubhllmsBU`). Cline and others also say each added instruction can hurt (`yUmS-F9IX90`).

## Consensus patterns

1. **Write a rule for each observed failure, not in bulk.** Failure-driven AGENTS.md or skills growth is the most repeated pattern. Prune rules when a new model no longer needs them. (`rnDm57Py54A`, `4_VQBbs2iQA`, `pqlWNihgdjI`, `Wmp2Tku2PrI`)
2. **Keep the always-loaded file thin; use progressive disclosure.** The index file is a map. Skills are folders with a short SKILL.md and reference files. Descriptions act as routers. (`pFsfax19yOM`, `GmAQKINjv1E`, `aeTb5BdmTTc`, `shRR1e2HXMk`)
3. **Back pressure must be deterministic.** Strict types, custom lint rules, ast-grep, compilers and stop hooks catch what prose rules miss. Rules should state intent, because agents game lint. (`Wmp2Tku2PrI`, `E3KbFLAGD6A`, `ugUeZ8-b-u0`, `MpZzWMdmQCE`, `xIt_mTQp6mY`)
4. **Reproduce first, verify end to end.** Make the agent write a failing test or repro before a fix. Then drive the real flow. A screenshot is not proof. (`iRcX54EO5g8`, `5Bn0xro2ol8`, `q4WC4TowkBo`, `bdHaOXZOhcM`, `W76woOYHlvY`)
5. **The writer should not be the checker.** Use a fresh context or a different agent or model for review and tests. Blind sub-agents beat self-review. (`ZpK5PWX2YRM`, `2TLXsxkz0zI`, `SQMCtZX3trg`, `AgBAOXVxt4A`)
6. **Plan before code, with a human on the plan.** Clarifying-question interviews, co-edited plans and spec docs come before execution. About 5 minutes of planning saves about 30 minutes of review. (`v4F1gFy-hqg`, `W76woOYHlvY`, `ClWD8OEYgp8`, `IddXPepIAS4`, `9fubhllmsBU`)
7. **Fresh context per unit of work.** Ralph-style loops work on small tickets with file-backed state. Reset and reload beats compaction for some teams. (`2TLXsxkz0zI`, `Wmp2Tku2PrI`, `4kYl2_mqmnQ`, `Kz4QJmNrVXU`)
8. **Make loops incremental and measurable, not blind.** Use a sensor, a controller and an actuator. Keep a ratchet in CI. One small PR a day. (`xIt_mTQp6mY`, `pmoDeA3RBZY`, `CgsWxRUY5Eo`, `JJGbw4ggaFs`)
9. **Isolate agents.** One clone, VM or pod per session. Least privilege. Secrets stay outside the agent. (`iH_wV8BbS24`, `rnDm57Py54A`, `iQ5xldZ9StU`, `pmoDeA3RBZY`)
10. **Retrieval: grep first, add semantic search as a tool.** Semantic search raises precision but costs more and is not always better. (`zKk7sDMGDEQ`, `T3SS931wU0I`, `UM6sFg_jdlE`, `dRmWYHuIJxM`)
11. **Give agents fresh and local context.** Fresh docs, vendored library source, dependency or API graphs and web search close the knowledge gap. (`juoNbJiZUi0`, `Wmp2Tku2PrI`, `k2ClBT4aqAg`, `cKhpeEBnT1o`, `9wZpvF3QleU`)
12. **Design tools for agents.** Small tool sets, JSON in and out, non-interactive CLIs, progressive tool discovery, code mode. (`3wj6sgbi1YA`, `aV_vgUSatqs`, `pAnLpiAG6Es`, `shRR1e2HXMk`)
13. **Cap writes and spend at the infrastructure.** Budgets, refilling rate limits, proxy-stamped identity and per-user spend limits beat static tokens. (`rbjWzZK2LU0`, `CoEIs6Xm8m8`, `iQ5xldZ9StU`)
14. **Close the loop with evals on traces.** Read traces, then write code or judge evals, and let a coding agent drive the fix loop. Guard the eval set from the optimizer. (`aHhB3sjGjkI`, `qZj7sqmidqA`, `_zUp6y9bDU8`, `BOCjybvJYM4`, `L2r6vLlLgs8`)

## Disagreements & open questions

- **Read the code or not?** Volkov says route by risk (`ZpK5PWX2YRM`). Litt says understanding matters for creativity, not only verification (`WkBPX-oDMnA`). Greptile finds agent PRs roughly even with human PRs on proxy metrics (`474j-n1Ltxc`). eBay warns of review debt (`TJPInBjhE4Q`).
- **Blind loops vs controlled loops.** Parsons ships with simple Ralph loops (`2TLXsxkz0zI`). Mistele calls blind loops the wrong default for teams (`xIt_mTQp6mY`). Koc wants a reward signal (`pmoDeA3RBZY`).
- **Worktrees vs clones vs VMs.** Worktrees overloaded one machine (`pmoDeA3RBZY`). Cursor says worktrees share databases and leak side effects (`rnDm57Py54A`).
- **Semantic search.** Cursor reports gains (`zKk7sDMGDEQ`, `UM6sFg_jdlE`). Braintrust found equal accuracy at 4x the cost (`T3SS931wU0I`). Open: does the agent know when to call it?
- **Skills vs MCP vs CLI.** Skills replace MCP for some (`ns9f1fjLD7Y`). Others say they are complementary (`GmAQKINjv1E`). Apify says MCP bloat is a harness bug (`pAnLpiAG6Es`). LinkedIn serves skills over MCP (`9wZpvF3QleU`).
- **Speed metrics.** Token counts get gamed and individual gains may not reach teams (`CS5Cmz5FssI`, `Kz4QJmNrVXU`). Jellyfish says tokens are about 2.5% of cost per merged PR (`U7ZYBCcdJPg`).
- **Small agent count vs fleets.** Orosz advises one or two agents (`CS5Cmz5FssI`). Others run dozens (`pmoDeA3RBZY`) or 15 to 20 (`GdvKNwMcfd0`).
- **Open:** how to measure review quality, how to avoid skill sprawl (`7gujZrJ9L5I`), how long an agent can run before reliability drops (`7vn4WpqNpck`), and how to score skill-worthiness (`Z-c11pV_uvU` covers context isolation only).

## How thinking changed over time

- **2026-05-18.** Fundamentals first. Matt Pocock argues deep modules, shared language and TDD matter more with agents (`v4F1gFy-hqg`). Companies standardize on one tool and a guidance flywheel (`4_VQBbs2iQA`). Skill writing becomes a craft (`pFsfax19yOM`).
- **2026-06-18.** Factory and attention framing. Dark factory, swim lanes, fast models that need slow developers (`pmoDeA3RBZY`, `TeGsFFNqRLA`). Benchmark hygiene comes up (`wcUJWP6WpGM`, `QuuIywMG4s8`). Rust is pitched as the best language for agents (`ugUeZ8-b-u0`).
- **2026-07-18.** Understanding and review become the worry. Cognitive debt, review debt, trust ramps (`WkBPX-oDMnA`, `TJPInBjhE4Q`, `uU5Gv2h8-9g`). Recursive language models appear (`8oyalrfwgjw`, `3hXJI2q0Jz8`). ACP standardizes editor-agent links (`HsxQICTLF84`).
- **2026-08-18.** Harness and governance. Loop engineering, goal verifiers, cost routing (`xIt_mTQp6mY`, `il1c1a2FufU`, `CoEIs6Xm8m8`). Agent security gets its own talks (`cgimkNGNjvU`, `1EZdpEhwmNc`).
- **2026-09-18.** Way of working beats tool choice. Amazon's data shows 4.5x for teams that changed habits and under 3x for tool-only teams (`pqlWNihgdjI`). Budgets replace tokens (`rbjWzZK2LU0`). Compound engineering and skill engineering mature (`_ehJyfHg1Vk`, `SQMCtZX3trg`).
- **2026-10.** Proof and cost. Verifier CLIs, receipts, sandboxes, sub-agent teams at scale, cost per merged PR (`q4WC4TowkBo`, `iH_wV8BbS24`, `buHC7bQE1X4`, `U7ZYBCcdJPg`).

## Numbers worth remembering

- Amazon pilot: median 4.5x deployment velocity for teams that changed habits, under 3x for tool-only teams (`pqlWNihgdjI`).
- Greptile: about 25% of PRs largely AI-generated, under 1% by author field. Revert rates are close between agents and humans (`474j-n1Ltxc`).
- Pharos AI 2026 data, cited in an eBay talk: median PR review time up about 441.5%, 31% more PRs merged with no review (`TJPInBjhE4Q`).
- Jellyfish: AI is about 2.5% of the cost of a merged PR. Merged PRs per engineer up 43% year over year (`U7ZYBCcdJPg`).
- Cursor semantic search: about 12 to 13% accuracy gain across models, +2.6% code retention. Claude Code file precision about 65% to about 87% (`zKk7sDMGDEQ`).
- Braintrust: vector search cost about 4x agentic search at the same accuracy (`T3SS931wU0I`).
- Tesco: about 90% of coding cost is input. A local index cut input tokens about 94% on one small benchmark (`dRmWYHuIJxM`).
- Postman: a code-grounded API graph gave similar quality at half to one third of the tokens (`k2ClBT4aqAg`).
- Fast model: about 1,200 tok/s vs 40 to 60 for Sonnet and Opus (`TeGsFFNqRLA`).
- Sentry: 67% of one engineer's AI use was comprehension, 2% generation (`li0SaBt9RDM`).
- Agent improving agent: 18% to 83% in about 10 iterations (`aHhB3sjGjkI`).
- Antigravity: 93 subagents, 12 hours, about 2 billion tokens, under $1,000 (`buHC7bQE1X4`).
- Incident: about 200 workloads deleted in 90 seconds by an empty selector (`rbjWzZK2LU0`).
- Linear: about 10% of bugs fixed by one-shot agent PRs (`wjk0ulMAkbc`).
- Rule of thumb: 5 minutes of planning saves about 30 minutes of review (`W76woOYHlvY`).
- Snyk scan: 367 of about 10,000 third-party skills flagged as malware (`ZyC56eV8sVw`).
- MCP: 10 servers can eat about a third of context up front (`pAnLpiAG6Es`).
- Eval: a correctness judge scored 0 of 13 traces because of stale training data (`qZj7sqmidqA`).

## From creator channels (Kai Explains, AI LABS, Better Stack)

Most of this comes from single creator videos: tutorials, reviews and news. Most numbers are the creators' own and unmeasured. Items that rest on one video or on a sponsored segment say so.

### Practical playbook

1. **Keep the always-loaded file small.** Aim for CLAUDE.md and SKILL.md under about 200 lines. Put folder detail in per-folder CLAUDE.md files and long detail in skill reference files. Keep only what the agent cannot find in the repo (`jwje1JK8Nqs`, 9:14). Another creator uses a 500-line ceiling (`D4uBfIe7SzA`, 0:00). The two numbers disagree, so measure on your own repo.
2. **Write one rule per real mistake.** Keep CLAUDE.md in git as a failure log. Build a skill that drafts the new rule after each mistake (`D4uBfIe7SzA`, 1:03). Single video.
3. **Put passive framework knowledge in AGENTS.md, and keep skills for explicit workflows.** Use a short index of version-matched doc files on disk, not the docs themselves. Use skills for upgrades and migrations (`i0W90tlKfYg`, 2:21 and 4:36). The evidence is one creator reporting Vercel's evals. There, the skill went unused in 56% of runs. An explicit "use the skill" prompt raised trigger rate to 95%, but pass rate reached only 79%.
4. **Cap command output and filter test output.** Lower the bash max output from 30,000 to 10,000 characters in .claude/settings.json (key name spoken, verify it). Add a hook that passes only failing test results into context (`jwje1JK8Nqs`, 16:21).
5. **Turn off default-on token costs.** Disable auto-memory and bundled skills. Cap or disable sub-agent workflows on low-tier plans. Replace the built-in advisor with a custom agent of the same name that runs only on request (`jwje1JK8Nqs`, 14:54). Exact setting names are not clearly spoken.
6. **Hygiene per session.** Run clear between unrelated tasks. Compact before a break, with an explicit list of what to keep, because the prompt cache expires when idle. Rewind a bad turn instead of correcting it on top. Batch related edits into one prompt (`jwje1JK8Nqs`, 3:44 to 5:12).
7. **Prefer a CLI to an MCP server when the CLI can do the job.** MCP tool schemas stay in context all session. A CLI loads only when called (`jwje1JK8Nqs`, 9:14).
8. **Pick model and effort per task, and compare cost per finished task.** Default to medium effort and raise it for hard work (`jwje1JK8Nqs`, 7:47). Rank models by cost per completed task, not list price (`0lBvjhcRqyU`, `93iYf9wp7Qw`). Single reviews, with the creators' own test setups.
9. **Give an unattended loop a settled answer key.** Turn open decisions into a map with a pass/fail checklist. Point the critic at the checklist, not at the builder's judgment (`D_uojDHkbw4`, 8:21). This rests on one anecdotal build: 1h33m, about 40% of a Max session limit.
10. **Encode taste and brand in files.** In AGENTS.md, add a standing rule to verify its own work: start the server, run the build, check desktop and phone widths in a browser. Write a design.md brand file before prompting a design tool to break default palettes (`bBlY5YOsKN8`). Exclude the OpenAI site skill from design work, ideally by writing that exclusion into AGENTS.md (`pHstb0JGGhE`). Both are single tutorials. The first has a mid-video sponsor read.
11. **Use lint, not prose, for rules that must hold.** Enable only the rules your team needs and make lint a required pass. Let the agent fix from the error text (`mmrSYvYKD9g`). For Tailwind design systems, lint the design tokens (`tPQgw_DPIoM`). The linter checks rules, not whether a design is good.
12. **Stack PRs for agent chains.** Run gh stack init, then gh stack add per branch, then gh stack submit. Merge the stack from the top PR. Put shared types and schema in the lowest PR (`3Z1xcfF2xlY`, 0:00 to 3:14). Short demo. The agent use case is the creator's suggestion, not tested.
13. **One worktree per parallel agent, with one status view.** Run the shell setup for wt before the first switch, or the cd never happens. Use wt list to see working or waiting agents. Copy ignored build caches with copy-on-write. The author's figures (14 GB copy from about 2m14s to about 20s) are unverified (`mNo24Omj8X4`).
14. **Review agent and editor config before opening untrusted code.** Check .claude/settings.json for SessionStart hooks and .vscode/tasks.json for folder-open tasks. Turn off VS Code automatic tasks. Use short-lived OIDC tokens in CI and a default-deny egress list on runners (`lNsSxWQDqaU`). Single news video, based on reporting from Socket.dev.
15. **Sandbox agents with default-deny egress.** Start with no network. Read the denial in the logs. Add one narrow rule for the method and endpoint you need. Keep real keys outside the sandbox. Test the setup directly. On a Mac, the creator found that the doctor command reported green on a broken setup (`SbwckhZkPGs`, 6:02).
16. **Test the harness before the model when going local.** Run a trivial read, run-tests and one-line-edit task. If tool calls fail, switch harness before you change the model. Raise Ollama's context from the 4,096 default to about 64k, or it truncates silently. Point the harness at localhost:11434 (`uefMWJ1GBWg`, `qS5ZUEaKwNw`). The creator does not show exact config keys.

### Tools creators recommend

- AGENTS.md via /init (Codex) — writes project context from the first prompt, so later threads match — `pHstb0JGGhE`
- Wayfinder (planning skill) — turns open decisions into a map and a pass/fail answer key — `D_uojDHkbw4`
- Stitch CLI (Google) — drives the design tool from Claude Code without the MCP setup — `au2TI8sdq8E`
- Graft — code knowledge graph; hooks inject file:line matches per prompt — `cyIWQHYoUg8`
- Archify — agent emits validated JSON that a compiler turns into architecture HTML — `iuJszJuiuSg`
- Whiteboard — linked diagrams of a branch's changes for review; check the telemetry setting first — `cP5PRDo3u6Q`
- Agit — git model for agent sessions: revert, cherry-pick, fork into Codex — `CHHEjuNBxoQ`
- Worktrunk (wt) — worktree CLI with a status view and copy-on-write copies — `mNo24Omj8X4`
- Orca — desktop app for side-by-side coding CLIs, one worktree per task — `8QgBcI40VC8`
- OpenShell (NVIDIA) — sandbox with per-request policy and credential injection — `SbwckhZkPGs`
- Free Claude Code — proxy that keeps Claude Code's UI and routes requests to other models — `vxrZWbZ2fZA`
- OpenCode — open-source terminal agent with pinned-model subagents and LSP — `wOfm7x0i3sw`
- Qwen Code with Ollama — local agent harness; needs the context bump — `qS5ZUEaKwNw`
- oMLX — Apple Silicon local server with an SSD KV cache and an Anthropic-style endpoint — `j557WxWtdZk`
- Anti-slop oxlint rules — lint gate for agent-written TypeScript — `mmrSYvYKD9g`
- shadcn Tailwind linter — lints design-system rules for Tailwind v4 — `tPQgw_DPIoM`
- gh stack (GitHub CLI) — builds and submits stacked PRs — `3Z1xcfF2xlY`

### Where creators agree or clash with the conference talks

The conference talks are cited by their consensus numbers above, since their ids are not in this category's creator notes.

**Agree**
- Small, failure-driven instruction files and deterministic gates (consensus 1 to 3). Creators add lint rules with fix-oriented messages (`mmrSYvYKD9g`, `tPQgw_DPIoM`).
- Isolation and least privilege (consensus 9 and 13). `SbwckhZkPGs` and `lNsSxWQDqaU` add concrete config checks.
- Parallel fleets with a writer-checker split. The Bun port (`0TSxrzBVEwQ`) ran an implementer, two adversarial reviewers and a fixer per file. It also forbade every git command except committing, after parallel agents broke the shared repo. This is one news video, and the cost figure is an API-equivalent estimate.

**Clash**
- Skills versus passive context. `i0W90tlKfYg` reports that a passive index beat skills in one vendor eval. Conference talks treat skills and MCP as complementary, or as partial replacements (consensus 2 and the disagreements list). The evidence on the creator side is one eval.
- Size ceiling. `jwje1JK8Nqs` says 200 lines, and `D4uBfIe7SzA` says 500. Neither is measured.
- Blind comparison as a stop condition. `D_uojDHkbw4` says a blind pairwise judge needs a shipped reference, and invents a drifting standard without one. Consensus 5 treats a fresh-context checker as enough. The creator adds that the checklist must be settled before the loop starts.
- Cost lens. Creators optimize per-token spend against plan limits (`jwje1JK8Nqs`, `P0i3vYuJZH8`). The conference data says tokens are a small share of cost per merged PR. Both can hold: on a personal plan, the token budget is the binding limit.
- Worktrees. Creators promote one worktree per agent (`mNo24Omj8X4`, `8QgBcI40VC8`). Conference talks report that worktrees overloaded one machine and shared databases. Worktrunk's copy-on-write only fixes setup cost. It does not fix shared databases.

### Watch first

- `jwje1JK8Nqs` — 24 concrete habits and settings for token budgets. Mostly unmeasured, but each one is checkable.
- `D4uBfIe7SzA` — short list of CLAUDE.md rules and the failure-log pattern.
- `i0W90tlKfYg` — the only creator video that reports skill trigger rate against eval pass rate.
- `D_uojDHkbw4` — critique of blind critic loops and the answer-key fix. Anecdotal, but the failure modes are clear.
- `SbwckhZkPGs` — sandbox review with honest caveats on macOS and on the doctor output.
- `0TSxrzBVEwQ` — the largest reported agent-run rewrite, and the coordination rules that made it work.

## Watch first

- `v4F1gFy-hqg` — fundamentals, grill-me interviews, deep modules, small TDD steps.
- `xIt_mTQp6mY` — loops as control systems, ratchets and a daily small PR.
- `q4WC4TowkBo` — deterministic verifier CLIs and evidence receipts.
- `pqlWNihgdjI` — data on what separates 4.5x teams from tool-only teams.
- `rbjWzZK2LU0` — budgets, rate limits and proxy identity for agent writes.
- `ZpK5PWX2YRM` — risk-tiered review and writer/checker separation.
- `4_VQBbs2iQA` — guidance flywheel and backtested skills at Intercom.
- `pmoDeA3RBZY` — swim lanes and practical limits of parallel agents.

## Implications for our projects

**ProsHarness**
- Add a stop-hook verifier step that runs one deterministic command and feeds failures back (`MpZzWMdmQCE`, `q4WC4TowkBo`). Store pass evidence as a receipt tied to the current commit.
- Checkpoint and resume fits file-backed state and clear-and-reload (`4kYl2_mqmnQ`, `L2r6vLlLgs8`). Keep per-run state in files, so a run restarts without redoing finished work.
- The plan, critique (Codex), debate flow matches cross-model adversarial review (`AgBAOXVxt4A`, `SQMCtZX3trg`). Keep writer, inspector and test author separate (`ZpK5PWX2YRM`).
- Loops and schedules: copy the one-open-PR flow control and a feedback file (`xIt_mTQp6mY`). Add a reversibility gate where irreversible actions are only drafted (`2TLXsxkz0zI`).
- Phone approvals: remote-control sessions and a blocking review gateway are proven (`so9l_MwS2yg`, `4kYl2_mqmnQ`).
- Skill ranking: trigger-accuracy tests and with/without evals give a ranking signal (`GmAQKINjv1E`).

**AgentOS**
- Govrix Scout: use refilling per-write rate limits, proxy-stamped identity and break-glass verbs (`rbjWzZK2LU0`). Add steer-vs-ask hook decisions and secret brokering (`cgimkNGNjvU`, `iQ5xldZ9StU`).
- Crucible: pick the isolation tier by blast radius. Mount only what the task needs (`iH_wV8BbS24`). Treat containment as separate from correctness (`bI8WyG9YB0I`).
- SkillForge: mine session logs for repeated prompts and failures (`li0SaBt9RDM`, `so9l_MwS2yg`, `E3KbFLAGD6A`). Success signal: verifier pass plus no revert (`474j-n1Ltxc`). Write playbooks back through a PR with human approval (`9wZpvF3QleU`). Scan third-party skills first (`ZyC56eV8sVw`).
- InferCraft: planner-and-fast-executor split and per-task routing are priority-scheduler use cases (`TeGsFFNqRLA`, `FvxY8oPoI8o`, `48YUYDjwfYY`).
- MemoryMesh: a markdown pattern catalog in git worked as memory at Netflix (`CgsWxRUY5Eo`). Test grep against hybrid retrieval, since vector search cost 4x more at equal accuracy in one eval (`T3SS931wU0I`).
- Benchmarks: report variance, cost and configuration, not one score (`YIxzNZDDy1A`, `wcUJWP6WpGM`).

- A thin MCP surface with search, schema and execute tools handles large catalogs (`9wZpvF3QleU`, `3wj6sgbi1YA`). This suits the registry of skills, agents and MCP servers.
- Registry entries should be scanned and risk-scored before adoption (`cgimkNGNjvU`, `1EZdpEhwmNc`).

**Entity resolution and cheap-model pipelines**
- Use deterministic checks first and LLM judges second. Give judges the same context the agent saw (`qZj7sqmidqA`).
- Per-step verification is cheap with fast models, so run it on every step (`TeGsFFNqRLA`).
