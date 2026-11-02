# Guide: context-engineering
*Synthesized by Sonnet from 205 talks since 2026-05-18.*

Scope: prompt and context design, CLAUDE.md / AGENTS.md, context windows, compaction, skills, specs, retrieval as context. Newest talks (Aug to Oct 2026) weigh most. Only talks present in the compact notes are cited.

## State of the art

**Context is a budget, and it is spent before the user types.** Practitioners now treat the window as a scarce resource even at 1M tokens. Quality drops well before the limit. Rules of thumb vary: about 100k tokens (`-QFHIoCo-Ko`), about 40% of the window (`LC3-P7v3yoI`), and "256k already loaded is worse than near zero" (`KtBivPzmOM8`). Tools and skills make up about 80% of each API request, which the provider caches (`KtBivPzmOM8`). Ten MCP servers can burn about a third before any question (`pAnLpiAG6Es`).

**The always-loaded file is small and grows from failures.** CLAUDE.md / AGENTS.md is a short map plus commands plus one rule per observed agent mistake. Teams do not install rule packs in bulk (`rnDm57Py54A`, `Wmp2Tku2PrI`, `pqlWNihgdjI`). After each model upgrade, they audit the file and delete rules the new model no longer needs (`pqlWNihgdjI`). An in-house support agent that replaced a bought docs bot went from about 10% to a self-reported 80% end-to-end resolution, and its CLAUDE.md of guardrails is updated after every bad conversation (`pyvRID_CZZU`).

**Skills are the main unit of context.** Only name and description sit in the prompt. The body and reference files load on demand (`pFsfax19yOM`, `GmAQKINjv1E`, `7jjudsEhBtM`, `BKWpYIWvAo4`). The description is a routing rule, written from the user's side, with a "when not to fire" line (`0vphxNt4wyk`, `7jjudsEhBtM`). Skills are now treated as software. They get owners, versions, evals and a registry (`M05vON8i0aI`, `zCJtYuqwm7E`).

**Tools load lazily too.** Deferred tool loading with a tool-search tool is standard (`shRR1e2HXMk`, `9WiBJRO84yY`, `v3Fr2JR47KA`). Cap the skills list as a share of the window (about 2% in Codex, `shRR1e2HXMk`). Wrap large catalogues in three meta tools: search, get schema, execute (`9wZpvF3QleU`). Code mode lets the model write one script instead of chaining calls (`v3Fr2JR47KA`, `pAnLpiAG6Es`).

**Compaction is contested; append-only plus re-fetch is the leading design.** Anthropic keeps an append-only session log and builds context from it, so the compaction strategy can change without data loss (`Uv0nAf_7tyU`, `9QebvrrY3KY`). Many harness builders clear and reload from file-based handoffs instead of summarizing (`4kYl2_mqmnQ`, `-QFHIoCo-Ko`). Head and tail truncation with the middle spilled to a store, plus fetch-by-ID, is a common middle path (`esY99nYXxR4`, `WP3hjUXd918`, `DrfyORO8RqA`).

**Retrieval is now agentic search over files.** Agents get small primitives (list, grep, read with offset, semantic search, page screenshots) and chain them (`X4w2Pkz5tDY`, `ynJyIKwjonM`). Tuned BM25 plus grep is strong because agents write long, exact queries (`fZH97QHHYjY`, `O84lhGc1OOI`). Docs as local markdown the agent can search work well (`pyvRID_CZZU`, `ZRM_TfEZcIo`).

**Verification is the next problem after context fit.** Fitting rules into the prompt is mostly solved. Checking that the model followed them is not (`XzJD1bvXKjs`).

## Consensus patterns

1. **Progressive disclosure everywhere.** Metadata always, body on demand, references on demand. Applies to skills, tools, docs, memory. (`GmAQKINjv1E`, `pFsfax19yOM`, `LC3-P7v3yoI`, `BKWpYIWvAo4`, `7jjudsEhBtM`, `ZRM_TfEZcIo`)
2. **Keep the main context clean by delegating.** Sub-agents do heavy search or data work and return summaries only. (`esY99nYXxR4`, `0RNNfxpdbQk`, `u6jJcIFDLE4`, `iJVxxxHM_Oc`, `O84lhGc1OOI`). Caveat: sub-agents move the problem and do not remove it (`pAnLpiAG6Es`).
3. **Fresh context per unit of work.** Ralph loops run one small task per run, then exit. State lives in files, tickets and git, not in the window. (`2TLXsxkz0zI`, `Wmp2Tku2PrI`, `-QFHIoCo-Ko`, `4kYl2_mqmnQ`)
4. **Verify in a separate context from the builder.** Self-review in the same context confirms its own work. (`mR-WAvEPRwE`, `9QebvrrY3KY`, `2TLXsxkz0zI`, `SQMCtZX3trg`, `LlgiOCmFG_w`)
5. **Rules come from failures, and they go into deterministic checks where possible.** Lint, hooks, types and tests beat prose. (`Wmp2Tku2PrI`, `E3KbFLAGD6A`, `FwiS44-xyYw`, `AgBAOXVxt4A`, `SQMCtZX3trg`). Agents game lint rules, so state the intent in the rule (`E3KbFLAGD6A`).
6. **Give goals and constraints, not step lists.** Move fixed workflows into scripts. (`pFsfax19yOM`, `0vphxNt4wyk`). Inject deterministic command output instead of letting the model guess (`pFsfax19yOM`).
7. **Spec and plan first, with an interview.** A "grill me" interview, then a PRD, then vertical-slice issues. (`v4F1gFy-hqg`, `-QFHIoCo-Ko`, `VMemhtlsoNk`, `pqlWNihgdjI`, `Ib5GBkD555M`). Planners stay high level so errors do not cascade (`mR-WAvEPRwE`).
8. **Put the real source and fresh docs in context.** Models are frozen snapshots. Clone library source into the repo, or serve current docs as markdown. (`Wmp2Tku2PrI`, `juoNbJiZUi0`, `V_5bn4q-vAI`)
9. **Layer the prompt in a fixed order, with one assembly point.** Identity rules, situation, voice, then a post-generation veto. Inject tool context at call time, not up front. (`ij-AU9dpJjc`, `iUWwcG-C8OU`)
10. **Tool descriptions and tool count decide behavior.** Trigger conditions, ordering rules, trimmed outputs, fewer tools. (`ynJyIKwjonM`, `0n3MKk7r60w`, `Wmp2Tku2PrI`)
11. **Return errors to the model, with a bounded retry.** (`ynJyIKwjonM`, `spxoDAfh5ig`, `ORVh4GivEU0`)
12. **Skills need evals.** Trigger and negative cases, with/without comparison, deterministic assertions before LLM judges, CI gate on skill diffs. (`0vphxNt4wyk`, `GmAQKINjv1E`, `7jjudsEhBtM`)
13. **Derive context from systems, not hand-curated markdown, when the knowledge is large.** Ground every graph node in code or traces. (`KcVkq5L-0f0`, `k2ClBT4aqAg`, `KhRjivBSwiw`). Compute structure deterministically, use the LLM last.
14. **Let the LLM plan, let code execute, when sets are large.** (`EUsPvBeIx70`, `xo68uCibfm8`, `u6jJcIFDLE4`)
15. **Spec the agent-readiness of the repo.** Docs, fast CI, modular code, reproducible env. (`Se8jHLliLXE`, `exiwa9QbQXI`, `I2LL_wd89-A`)

## Disagreements & open questions

- **Compact or not.** Summarizing kills the prompt cache, so compaction must beat about 50x compression to pay off. On one tutor eval, full history beat every compaction preset (`WP3hjUXd918`). Codex relies on compaction to keep weeks-long threads alive (`il1c1a2FufU`). Matt Pocock says clear, do not compact (`-QFHIoCo-Ko`). Small samples on all sides.
- **Curated markdown vs derived context.** Unblocked calls curated context a trap that rots (`KcVkq5L-0f0`). Others treat a carefully written CLAUDE.md as onboarding (`TRfzFJCJ7ZE`). Sourcegraph says repo docs barely help at large scale (`Bdrs3uAX0_M`). Likely both: small curated file, large derived layer.
- **Vector index or not.** Claude Code dropped its index; local files are fine for roughly 100 to 1,000 files, above that you need retrieval (`X4w2Pkz5tDY`). A personal wiki needs no vector DB (`ZRM_TfEZcIo`). Enterprise memory wants typed, governed DB records (`BIhiYL4U9_M`).
- **MCP vs skills vs CLI.** Some say context bloat is a harness problem, not a protocol problem (`pAnLpiAG6Es`). Others say skills carry procedure and MCP carries execution (`LC3-P7v3yoI`, `GmAQKINjv1E`).
- **One agent or many.** ZS killed a multi-agent pipeline for one reasoning agent plus scoped subagents (`u6jJcIFDLE4`). Splitting is advised only past about 20 tools or very large context (`mYSRn6PC1mc`).
- **Does prose matter?** Durable value lives in prose (`juoNbJiZUi0`). But 250 lines of prose could not change model defaults, so scripts and blind sub-agents were needed (`SQMCtZX3trg`).
- **How long can a skill be?** The old 200-rule limit moved about 10x, but models fail in four different ways (`XzJD1bvXKjs`). Older advice caps SKILL.md near 500 lines (`0vphxNt4wyk`).
- **Open:** no principled context budget or quality metric (`esY99nYXxR4`); memory consolidation ("dreaming") needs evals before paying for it (`9QebvrrY3KY`); cross-agent learning is unsolved (`9_oy4owGtPI`); staleness of derived context (`k2ClBT4aqAg`).

## How thinking changed over time (dated)

- **2026-05-18.** Fundamentals first: shared language, TDD, deep modules (`v4F1gFy-hqg`). Context engineering is seen as mostly search tool choice (`ynJyIKwjonM`). Truncation and summarization are tried and found wanting (`esY99nYXxR4`). Rules grow from failures (`rnDm57Py54A`).
- **2026-06 to 07.** Evals for prompts and skills arrive: GEPA and golden sets (`A48uhxfxbsM`), skill ablations (`0vphxNt4wyk`). Layering and specs become themes (`ij-AU9dpJjc`, `DqtmZE6Hl0g`). Long runs need a separate evaluator (`mR-WAvEPRwE`).
- **2026-08-18.** Compaction doubts and the append-only log (`WP3hjUXd918`, `9QebvrrY3KY`). Skills become the product surface (`7jjudsEhBtM`, `LC3-P7v3yoI`). Memory moves from RAG to profile plus search tools (`5ZGyKWjQDr0`). "The model was right, the harness failed" (`BInpv7lGp1o`).
- **2026-09-18.** Instruction capacity jumps about 10x; verification becomes the bottleneck (`XzJD1bvXKjs`). Playbooks over MCP and governed skill catalogs (`9wZpvF3QleU`, `M05vON8i0aI`). BM25 and grep return for agentic search (`fZH97QHHYjY`).
- **2026-10.** Skill engineering moves from prose to scripts, hooks and blind sub-agents (`SQMCtZX3trg`). Codified rules become lint (`E3KbFLAGD6A`). Memory becomes typed and governed (`BIhiYL4U9_M`). Verification receipts and evidence replace model prose (`q4WC4TowkBo`, `bI8WyG9YB0I`). Context graphs for code and data (`KhRjivBSwiw`, `k2ClBT4aqAg`).

## Numbers worth remembering

- Smart zone about 100k tokens, whatever the window size (`-QFHIoCo-Ko`). About 40% of window (`LC3-P7v3yoI`, speaker experience, not measured).
- Context rot starts around 200k by one rule of thumb (`mYSRn6PC1mc`). A Chroma study across 18 models showed 30 to 50% loss before the window filled (`XzJD1bvXKjs`).
- Instruction ceiling: about 200 to 300 rules in 2025, about 2,000 (best about 5,000) in 2026. Study cost $209 (`XzJD1bvXKjs`).
- Prompt caching: about 90% savings typical; compaction must compress over 50x to pay off (`WP3hjUXd918`).
- One skill body about 1.3k tokens, much less than the equivalent MCP tool set (`GmAQKINjv1E`). Skill definitions can run 3k to 5k tokens each (`KtBivPzmOM8`).
- Skills list in prompt breaks past about 10 skills (`7jjudsEhBtM`). MCP degrades past 30 to 40 tools, a claim with no data (`9wZpvF3QleU`). GitHub MCP passed 100 tools, settled near 40 by default, trimmed output by over 75% and reached over 95% success (`0n3MKk7r60w`).
- Skills help about 15% on average on SkillsBench; almost none of about 50,000 skills have evals (`0vphxNt4wyk`).
- Code-and-telemetry context graph: similar quality at half to one third of the tokens (`k2ClBT4aqAg`). Context-layer vendor benchmark: about 35 points higher task success (`KhRjivBSwiw`, vendor claim).
- Context optimizer: about 24,000 to about 2,400 tokens in demos (`tZycGA_Fbfo`). Context bundle run: about 50% lower cost ($1.29 versus up to $2.60), one task only with no variance reported (`ORVh4GivEU0`).
- Planner/resolver over agent loop: 100% at all scales versus about 30% at 460,000 GPUs for the old approach (`EUsPvBeIx70`).
- Hybrid search on BrowseComp-Plus: about 90% accuracy with about 20% fewer tool calls; badly tuned BM25 about 60% (`O84lhGc1OOI`).
- GEPA prompt: 92% hand-written to 96.7% optimized (`A48uhxfxbsM`). Prompt optimizer first iteration gained about 10 points (`eAXxdtNlK04`).
- Lazy sandbox provisioning cut time to first token about 90% (`Uv0nAf_7tyU`).
- Code survival rate: 55% with GPT-4.1, 86% with Opus 4.6 (`I2LL_wd89-A`).
- Teams that changed their way of working: 4.5x median deploy velocity; tool-only teams under 3x (`pqlWNihgdjI`).
- Long-session eval: seed 10 turns, test turn 11 (`esY99nYXxR4`).

## From creator channels (Kai Explains, AI LABS, Better Stack)

Sources: creator-channel videos in the context-engineering notes. Mostly tutorials and single-author reviews. Most numbers are the creators' own or relayed secondhand. Sponsored segments and vendor claims are flagged where they matter.

### Practical playbook

1. **Audit the window as a budget before a long session.** List what occupies it: system prompt, tool definitions, recent turns, file reads, tool output, and room for the reply. Start a fresh session and run the usage command before the first prompt to see the fixed floor. One creator measured about 70k tokens before typing, with three MCP servers connected. (`FWShtLCP4OY`, `Nf8j9w523pw`. The floor figure is one creator's measurement.)
2. **Disconnect idle MCP servers and unused connectors.** One creator removed one unused server and cut about 15k tokens of per-turn overhead. Connectors and artifacts also load into every session, even when unused. (`FWShtLCP4OY`, `i6Q7bXnWGlM`)
3. **Keep always-loaded files short and split them.** One creator sets about 200 lines for CLAUDE.md and SKILL.md (`jwje1JK8Nqs`). Another sets about 500 lines for CLAUDE.md (`D4uBfIe7SzA`). Put folder detail in per-folder CLAUDE.md files, which load only when a file in that folder opens. Move procedures into skills.
4. **Make CLAUDE.md a failure log.** Each line should trace to a mistake the agent actually made. One creator has a skill draft the new rule after a failure, so the user does not write it by hand. (`D4uBfIe7SzA`)
5. **Audit instructions after each model release.** Run the prompt-audit command, which uses sub-agents to check the whole setup, and review its fixes. Delete any instruction whose removal does not change the output. (`i6Q7bXnWGlM`, `7au4tWVG8a0`. The ablation step is one creator's method, not tested by others.)
6. **Clear between unrelated tasks.** A new prompt should not carry old context. (`jwje1JK8Nqs`)
7. **Rewind instead of correcting.** A correction in the next prompt leaves the bad turn in context for every later message. Rewind, or double-tap Escape, drops the turn. Editing an earlier message does the same job. (`jwje1JK8Nqs`, `MXclE0yaDXc`)
8. **Compact only before a break, and say what must survive.** The cached copy of the conversation expires while idle, so compacting after a long pause pays full read cost. Put the keep-instructions in the compact command. (`jwje1JK8Nqs`). See the clash section below.
9. **Cap command output, and filter passing tests with a hook.** The example cap is 10,000 characters. (`jwje1JK8Nqs`)
10. **Set reasoning effort per task.** Use medium for renames and for tests against code you already understand. Keep high for subtle debugging. One creator cites about a 45% token drop from high to medium, relayed secondhand. (`FWShtLCP4OY`). Another found the lowest effort gave the best result on one local-model coding test. (`3DVRznjCIS8`)
11. **Fetch docs as markdown, not HTML.** One measured example: about 38k tokens for the HTML page versus about 2.8k for markdown. The creator did not show the mechanism. (`FWShtLCP4OY`)
12. **Offload large tool output to disk and keep an ID map in context.** Write full logs to markdown files. Keep a small step diagram in the prompt, with an ID on each node, and fetch raw text by ID. Cap the map near 20% of the token budget. Fold mildly near half the window and more aggressively near 85%. (`W3yHP9_jYNk`. Single creator, reviewing one open-source plugin. The reviewer partly rechecked the benchmark arithmetic.)
13. **Hand off with a notes file, not a summary.** Ask the agent to keep a notes file with decisions, current state and what it already tried. A fresh session starts by reading it. (`9-iiHFQyzuM`)
14. **Write interface stubs first, then delegate.** Hand-write structs, traits and signatures. Let the agent fill in bodies, then check that it did not widen public surfaces or edit the stubs. Stage git changes after each accepted step as a checkpoint. (`VuMf2ZVA0RE`. One developer's workflow, podcast format.)
15. **Ask for the outcome, and use an outside judge.** Ask for the result and the diagnosis, not just the artifact. Have a different model review the build. (`92ZDgn8bgLM`. AI LABS tutorial relaying an Anthropic engineer's article.)
16. **Plan in chat, then build once.** Agree on structure and assumptions in plain chat first. Send the locked plan as one build instruction. (`MXclE0yaDXc`)

### Tools creators recommend

- **Graphify**: persistent code and docs graph, queried by traversal; git hook rebuilds it. `8Kv2tn22QNo`
- **Graft**: code graph plus a per-prompt hook that injects up to three file:line matches; CLI or MCP mode. `cyIWQHYoUg8` (benchmark is self-reported by its makers)
- **Headroom**: local proxy that compresses tool output, with hash links back to originals. `KqdRWE1en8k` (60 to 95% reduction is a vendor claim; one fake-log demo)
- **Caveman**: output-brevity skill, suggested as a pair with Headroom. Not tested in the video. `KqdRWE1en8k`
- **MemPalace**: local verbatim memory exposed over MCP, with Claude Code hooks. `kRACHOx1p8s`
- **PAI**: memory and skills layer on top of Claude Code for cross-session continuity. `JukZ7WWtOSg`
- **Agit**: git-style history for agent sessions, with revert, cherry-pick and fork to another agent. `CHHEjuNBxoQ`
- **Aider**: one git commit per AI edit, and a mid-session model switch for cost. `YgyyWDGeQWM`
- **OpenCode and Pi**: open harnesses; Pi keeps the base prompt small by loading skill blocks on need. `YgyyWDGeQWM`
- **Goal Buddy**: file-based goal state with judge, scout and worker roles, and an upfront "done" check. `q7Am0pV6FjQ`
- **Archify**: the model emits validated architecture JSON, and a local compiler draws the diagram. `iuJszJuiuSg`
- **Understand-Anything**: repo knowledge graph plugin for onboarding; the first scan was about 30 minutes. `VmIUXVlt7_I`
- **Prime Agent**: one persistent IPython kernel as the only tool, so large outputs live in variables. Benchmarks are vendor-reported. `_DZ4kJwQ50s`
- **Tencent memory plugin**: offload tool output, plus a four-layer memory store. Open source. `W3yHP9_jYNk`
- **Claude Code built-ins** (New Init, prompt audit, skill doctor, skills list sorted by token cost): named in the video, check your version. `i6Q7bXnWGlM`
- **Mods**: a Claude Code extension layer that runs alongside sessions and can change what Claude Code shows. `ERNqRK6sMJY`

### Where creators agree or clash with the conference talks

**Agree**

- Context is a per-call budget, and quality falls before the window is full. Creators say this with the same mechanism (`Nf8j9w523pw`, `W3yHP9_jYNk`). The second cites Chroma's context-rot study, where accuracy fell well before the window was full. That study is relayed, not checked.
- Prompt caching decides cost. The CLM paper, as relayed, reports that an edit near the start of context made the next turn about 7.7 times as costly, and the cache hit rate fell from 73.9% to 29.9% (`9-iiHFQyzuM`). This matches the cache math in Numbers worth remembering.
- Rules come from failures, and the always-loaded file stays small (`D4uBfIe7SzA`, `i6Q7bXnWGlM`). Matches consensus 5 and the always-loaded point in State of the art.
- Clear between unrelated tasks (`jwje1JK8Nqs`). Matches the clear-over-compact view in Disagreements.
- Use a different model as the outside reviewer (`92ZDgn8bgLM`). Matches consensus 4.

**Clash**

- **Compaction.** The conference notes lean toward append-only logs and re-fetch. Kai Explains argues compaction is lossy and that summaries can invent details. One test run fabricated 11 of 12 codes (`_DZ4kJwQ50s`, `9-iiHFQyzuM`). AI LABS still recommends compacting with keep-instructions before breaks (`jwje1JK8Nqs`). The fabrication case is one anecdote from one test.
- **Skills versus passive docs.** The conference view says skills are the main unit of context and need evals. `i0W90tlKfYg` relays a Vercel eval, as summarized by Better Stack. A compressed doc index in AGENTS.md scored 100%. Skills were never invoked in 56% of runs. Secondhand. The same video still says skills suit explicit, user-triggered workflows.
- **CLAUDE.md size.** Creators give 200 lines (`jwje1JK8Nqs`) and 500 lines (`D4uBfIe7SzA`). The conference notes cite about 500 for SKILL.md. None of these was measured.
- **Memory.** Verbatim storage with a compact index beats summarized memory for recall (`kRACHOx1p8s`). Layered consolidation with atoms, scenes and a persona is the other design (`W3yHP9_jYNk`). The conference view is that enterprise memory should be typed and governed. Each creator view is a single tool demo.
- **MCP.** `Rrju5Y0iiBM` says MCP is not dead. Its speaker saw instruction-following and tool choice degrade past five or six attached servers. `jwje1JK8Nqs` prefers a CLI over MCP when the CLI can do the job. The conference notes leave MCP versus skills versus CLI open. The server cap is a number they do not give.
- **Harness over model.** Creators argue the harness can move results as much as the model (`qXo1P5H2RXk`, `3DVRznjCIS8`). The second case is identical weights with a different harness. Single-creator evidence, so check it against the other guides before relying on it.

### Watch first

- `9-iiHFQyzuM`: the summary-fabrication case, the cache math, and how small the paper's absolute gains are. Paper figures are relayed, not checked.
- `jwje1JK8Nqs`: the most complete practitioner checklist. Covers cache timing, rewind, output caps and MCP versus CLI. Most numbers are the speaker's own.
- `W3yHP9_jYNk`: offload-to-disk with an ID map, and pressure-scaled folding. Read the benchmark caveats first.
- `FWShtLCP4OY`: the only measured fixed-floor figure in this set (about 70k tokens), with a pricing critique. Lawsuit figures are secondhand.
- `i0W90tlKfYg`: the skills-versus-passive-index eval. Watch how it was designed, then run the same test on your own repo.

## Watch first

- `-QFHIoCo-Ko` — Pocock's full workflow: smart zone, clear over compact, grill-me, PRD, vertical slices, Ralph loop.
- `WP3hjUXd918` — the best evidence on compaction versus full history, with the prompt-cache math.
- `XzJD1bvXKjs` — how many instructions a model can hold now, four failure modes, and why verification is next.
- `9QebvrrY3KY` — Anthropic on append-only context, separate verifier, and offline memory consolidation.
- `Uv0nAf_7tyU` — the brain/hands/session split in detail, with credential proxy.
- `esY99nYXxR4` — a concrete context-growth fix with a long-session eval you can copy.
- `0vphxNt4wyk` — skill evals: trigger tests, regex asserts, CI gate, retire-a-skill ablation.
- `SQMCtZX3trg` — why prose skills are not enough; blind sub-agents, scripts, per-skill memory.

## Implications for our projects

**AgentOS MemoryMesh.** Keep tiered memory but add an append-only event log as the source of truth. Build context from it with a swappable strategy (`Uv0nAf_7tyU`, `9QebvrrY3KY`). Add a background re-synthesis pass with provenance, and eval it before running it by default (`5ZGyKWjQDr0`, `9QebvrrY3KY`). Use typed records and check scope on write and read (`BIhiYL4U9_M`). Add private-to-shared promotion with provenance for cross-agent memory (`9_oy4owGtPI`). Treat memory content as a prompt-injection path, which fits Govrix Scout scanning (`BIhiYL4U9_M`, `4lXks428C9o`). Retrieval: tune BM25 first, then fuse with pgvector, and expose grep-like drill-down (`fZH97QHHYjY`, `O84lhGc1OOI`, `X4w2Pkz5tDY`). Add a long-session eval (seed N turns, probe N+1) to the RAGAS set (`esY99nYXxR4`).

**AgentOS Govrix Scout.** Put the deterministic gate before any LLM judgment, and separate the scanner from the policy actor (`4lXks428C9o`). Log the exact prompt as hashed parts so each request is replayable and diffable (`KHudyx5wW3U`). A run receipt with state snapshot, authority and result suits the Merkle audit log (`BInpv7lGp1o`). Add a proxy-side token trimmer for tool output, in the style of the context optimizer (`tZycGA_Fbfo`).

**AgentOS SkillForge / EvolveCraft.** Skill-worthiness could use ablation: with and without skill, plus trigger and negative sets (`0vphxNt4wyk`, `GmAQKINjv1E`). Record the rule-drop rate per skill on the target model before publishing (`XzJD1bvXKjs`). Use failure-driven rule growth as the telemetry signal: repeated corrections become skill edits (`rnDm57Py54A`, `Wmp2Tku2PrI`, `E3KbFLAGD6A`). Mine agent transcripts for lint-worthy rules (`E3KbFLAGD6A`). For optimization, GEPA-style reflection with a Pareto pool and rich evaluator side information fits EvolveCraft (`OA-Mc60Rboo`, `A48uhxfxbsM`). Prefer binary criteria over 0-10 judge scores (`eAXxdtNlK04`).


**ProsHarness.** Prefer clear-and-reload from handoff files over compaction for checkpoint/resume (`4kYl2_mqmnQ`, `-QFHIoCo-Ko`). Make the checkpoint barrier an append-only log with the harness stateless (`Uv0nAf_7tyU`). Verification: pin "done" to one deterministic command, store evidence with a checksum, and detect stale proofs (`q4WC4TowkBo`, `AgBAOXVxt4A`). Run the critic (Codex) in a separate context, and make the reviewer commit fixes (`LlgiOCmFG_w`, `AgBAOXVxt4A`). Add a rule-by-rule compliance check for long CLAUDE.md or skill files (`XzJD1bvXKjs`). Keep standards out of the implementer context and give them to the reviewer only (`LlgiOCmFG_w`). Use a reversibility gate in loops: draft irreversible actions, stop and report (`2TLXsxkz0zI`). Credentials stay out of the sandbox, injected by a proxy, which matches zero-token credential handling (`Uv0nAf_7tyU`).

**Cheap-model (Haiku) pipelines and entity resolution.** Prototype big, then pick the smallest model that passes a golden set (`fWXJM-J0ZB8`). Use a ceiling test (the production model against itself) to set the target (`8g1N_a3h9H0`). Let the LLM emit a structured plan and let deterministic code resolve sets (`EUsPvBeIx70`). Try fuzzy matching first with an LLM as tiebreaker (`ORVh4GivEU0`). Probe how many rules a Haiku-class model holds before writing long prompts (`XzJD1bvXKjs`).
