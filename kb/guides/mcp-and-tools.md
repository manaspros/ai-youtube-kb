# Guide: mcp-and-tools
*Synthesized by Sonnet from 112 talks since 2026-05-18.*

## State of the art
As of October 2026, practitioners treat MCP as the standard plug for tools and data. They no longer treat it as the whole answer. The work has moved to four areas.

**1. Keep the tool surface small and load it late.**
- Context bloat is the most common complaint. Practitioners now expose few tools, or let the model search for the tools it needs.
- GitHub cut its default server to about 40 tools and trimmed output tokens (`0n3MKk7r60w`).
- Prosodica routes each query to the top-K tools by embedding search (`vh2VGuQ3zhY`).
- Apify argues that bloat is a harness problem, not a protocol problem (`pAnLpiAG6Es`).
- LinkedIn serves search, get-schema and execute as three meta tools (`9wZpvF3QleU`).

**2. Code mode and CLIs are replacing one-tool-per-endpoint.**
- Cloudflare gives the model search and execute tools that take code. This covers 2,600 endpoints in about 1,000 tokens (`8txf05vVVl4`).
- Witan replaced about 15 spreadsheet tools with one persistent REPL (`HEFSExa0xl0`).
- Several speakers wrap MCP in a CLI with JSON in and JSON out (`3wj6sgbi1YA`, `pAnLpiAG6Es`).
- Reducto deleted its endpoint-wrapper MCP server and rebuilt it with fewer, workflow-shaped tools (`jJQoVkd5yLg`).

**3. Identity, credentials and policy are now the main production problem.**
- The pattern is one MCP gateway, zero credentials in the sandbox, and short-lived tokens per tool call.
- Per-call token exchange is shown in `I3znWC3MEXM` and `ws9XcGGPBDk`.
- Gateways are covered in `CD6R4Wf3jnY`, `17-YSUHo6Lk`, `ZUZVNKFSmTM` and `tZycGA_Fbfo`.
- Anthropic's managed agents inject credentials at an egress proxy (`Uv0nAf_7tyU`). Google's managed agents do the same (`8aVbXXvJUY4`).

**4. The protocol surface is growing.**
- MCP Apps let a tool return sandboxed UI (`o-zkvb0iFDQ`, `sAOBXCDiDOs`, `lbaXnx0KLA8`).
- MCP Tasks cover async work (`s4r6nk5WsZw`).
- WebMCP lets a web page expose tools (`ghJmWQCIHRM`, `LMbeDEQO6QM`).
- ACP standardizes the client-to-agent link (`HsxQICTLF84`, `YkNulwcc5jk`, `9WiBJRO84yY`).
- x402 and similar protocols handle agent payments (`KLSuFPj2ld0`, `h6mi88VrPtQ`).

Skills are now seen as the partner to MCP. A skill holds the procedure. MCP does the execution (`LC3-P7v3yoI`, `JT3OzDKrucU`).

## Consensus patterns
1. **Fewer tools beat more tools.** Accuracy drops and cost rises as the catalog grows. Reduce the default set, group CRUD, and trim outputs. `0n3MKk7r60w`, `vh2VGuQ3zhY`, `9wZpvF3QleU`, `vJukHCIv7Ck`
2. **Progressive discovery.** Load tool schemas only when the model asks. This takes the form of search tools, top-K routing, or deferred tools. `v3Fr2JR47KA`, `pAnLpiAG6Es`, `9WiBJRO84yY`, `x2bH0RKPgdc`
3. **Let the model write code instead of chaining calls.** Code gives loops, state and parallel calls in one run. It must run in a deny-by-default sandbox. `8txf05vVVl4`, `SKDJo2CopRs`, `HEFSExa0xl0`
4. **Design tools for agents, not humans.** Return semantic summaries, not raw dumps. Error text should say the next step. Tool descriptions should carry trigger conditions and ordering. `_B4Pv9ttFgY`, `ynJyIKwjonM`, `jJQoVkd5yLg`, `3wj6sgbi1YA`
5. **Keep credentials out of the model and the sandbox.** Inject them at a proxy or gateway. Issue short-lived, audience-bound tokens per call. `Uv0nAf_7tyU`, `8aVbXXvJUY4`, `ws9XcGGPBDk`, `xn8EsW0wxyc`, `ZUZVNKFSmTM`
7. **Put the gate in the tool path, not in the prompt.** Use approval nodes, hooks and out-of-model policy checks. Prompts are only suggestions. `tDArkCqjA-c`, `YXiLj4tJt5A`, `q-WOjZhOMCA`
8. **Give agents their own identity.** Bind the agent to a principal. Use fine-grained, time-bound capabilities. Log every action with both actor and subject. `lMCxVorb9wM`, `JvKO40CFq-s`, `q-WOjZhOMCA`, `EmhRyw6xeT0`
9. **Skills point to live docs and wrap MCP.** Put must-not-miss rules inline. Test with baseline, tool-only and tool-plus-skill runs. `JT3OzDKrucU`, `LC3-P7v3yoI`, `9wZpvF3QleU`
10. **MCP Apps: keep data and UI separate.** Whatever the UI shows must also reach the model as data. Hide app-only tools from the model. Route UI events through the host. `lbaXnx0KLA8`, `_xIwFcnHqp4`, `c-2eEv2ou7Y`, `sAOBXCDiDOs`
11. **Keep payment deterministic and outside the agent loop.** Use scoped tokens, spend caps and HTTP 402. The agent never holds keys. `KLSuFPj2ld0`, `qTZirYu9pr0`, `xKzU_3riL6s`, `G7cgLjZtmMU`
12. **Context beats model size for tool-heavy agents.** Missing organizational or data context, not intelligence, is the failure. Build graphs grounded in code or telemetry. `k2ClBT4aqAg`, `KhRjivBSwiw`, `KcVkq5L-0f0`, `jt1Pbr_n6oU`
13. **Make the web agent-readable.** Offer markdown, hand-written llms.txt, structured catalogs and WebMCP tools. `V_5bn4q-vAI`, `ghJmWQCIHRM`, `waI44NP1abk`

## Disagreements & open questions
- **MCP vs CLI.** Corey Gallon cites a study where both reach about 83% success, but the CLI is far cheaper and faster (`26RtyAm9y_Q`). Apify says CLIs lack enterprise control and credential injection, so use MCP for remote and CLI for local (`pAnLpiAG6Es`). Block's ACP talk does not weigh in on CLIs. It treats MCP for tools and ACP for clients as complementary layers (`YkNulwcc5jk`). No clean benchmark settles this.
- **Where to fix bloat.** Some say the server should shrink its surface (`0n3MKk7r60w`). Others say the harness should defer tools (`pAnLpiAG6Es`). Sam Morrow notes that users keep defaults and that no client filters on the read-only hint, so this stays unsolved.
- **Is MCP enough for async work?** MCP Tasks v1 has no client support. Davis says v2 is simpler, but polling does not scale (`s4r6nk5WsZw`).
- **Human approval as a control.** Many talks use it (`tDArkCqjA-c`). Maida argues it shifts control to a consent-fatigued user and proposes mission-scoped approval (`ws9XcGGPBDk`). Mission-based authorization is not a standard yet.
- **x402 maturity.** Vendors push it (`xKzU_3riL6s`, `qTZirYu9pr0`). Apify lists a double-spend window and a clash with MCP auth (`h6mi88VrPtQ`). Raskar-style open agent discovery is still a vision (`sum9DgexFRQ`).
- **Agent-readiness files.** About half of tested sites publish llms.txt, but most agents skip it (`waI44NP1abk`). Hand-written ones may still help (`V_5bn4q-vAI`).
- **Skill safety.** A scan of about 10,000 third-party skills flagged 367 as malware, per the speaker (`ZyC56eV8sVw`). Governance of shared skills is open (`u-o0sW9nwmk`).
- **Browser agents vs structured tools.** Some bet on pixels (`Ki980nV0__0`). Others bet on WebMCP and APIs (`ghJmWQCIHRM`, `G7cgLjZtmMU`).

## How thinking changed over time
- **2026-05-18.** Focus on scale and surface size. GitHub passes 100 tools and cuts back. Code mode appears as the fix for huge APIs. MCP Apps and WebMCP are introduced. Skills plus MCP beat MCP alone (`0n3MKk7r60w`, `8txf05vVVl4`, `JT3OzDKrucU`, `v3Fr2JR47KA`).
- **2026-06-18.** Generative UI and agent payments move to the foreground. Chrome DevTools shows that agent users need summaries and next-step errors. Double-iframe isolation is explained (`hCMrEfPG2Yg`, `KLSuFPj2ld0`, `_B4Pv9ttFgY`, `c-2eEv2ou7Y`).
- **2026-07-18.** Tool routing gets numbers. A single REPL beats many tools. ACP gets a live build (`vh2VGuQ3zhY`, `HEFSExa0xl0`, `HsxQICTLF84`).
- **2026-08-18.** Security and identity take over. Token exchange, per-agent keys and CLI-over-MCP arguments appear. MCP Tasks are found unsupported by clients (`I3znWC3MEXM`, `JvKO40CFq-s`, `26RtyAm9y_Q`, `s4r6nk5WsZw`, `LC3-P7v3yoI`).
- **2026-09-18.** Enterprise platforms arrive: Uber and LinkedIn gateways and playbooks. Skills become MCP-served assets. Payments get critiqued (`17-YSUHo6Lk`, `9wZpvF3QleU`, `9R--1tg45Jg`, `h6mi88VrPtQ`).
- **2026-10.** Defense in depth and rebuild lessons. Teams delete naive MCP servers, wrap them in CLIs, inject credentials at proxies, and split the agent into brain and hands (`jJQoVkd5yLg`, `pAnLpiAG6Es`, `Uv0nAf_7tyU`, `ZUZVNKFSmTM`, `ws9XcGGPBDk`).

## Numbers worth remembering
- Tool-selection accuracy about 78% at 10 tools, about 40% near 100, and 13.6% at 741. 741 schemas cost about 127,000 tokens per request. Routing injects 3 to 5 schemas, about 1,000 tokens (`vh2VGuQ3zhY`).
- Cloudflare: 2,600 endpoints at about 1.2M tokens as separate tools, versus about 1,000 with search plus execute (`8txf05vVVl4`).
- GitHub: default near 40 tools, about 49% less initial load, over 75% fewer tokens on PR list output, about 17% of users on read-only mode (`0n3MKk7r60w`).
- Naive loading of 10 MCP servers is about 100 tools and roughly one third of context (`pAnLpiAG6Es`).
- Witan spreadsheets: about 50% to 92% accuracy, 74% after the REPL change alone (`HEFSExa0xl0`).
- Snorkel: a 4B model RL-tuned for tool use beat a 235B model, under $500 per run (`TNwJ1LMiENk`).
- Fix from one distilled skill: 36% to 100% success on one task, a single anecdote (`u-o0sW9nwmk`).
- CLI vs MCP study: both about 83% success. 71 round trips and about 8 minutes for MCP, versus 7 turns and under 1 minute for the CLI (`26RtyAm9y_Q`).
- Supabase: skill plus MCP scored highest on all 4 agents, but no scores were given (`JT3OzDKrucU`).
- Lazy sandbox provisioning cut time to first token about 90% (`Uv0nAf_7tyU`).
- Credit Karma context optimizer: about 24,000 tokens down to about 2,400 in one demo (`tZycGA_Fbfo`).
- Uber: more than 100 million model requests a day, guard under 100 ms, PII redaction across 20-plus types (`17-YSUHo6Lk`).
- Context graph on API tasks: similar quality with about half to one third of the tokens (`k2ClBT4aqAg`). Typedef reports about 35 points higher task success (vendor benchmark, `KhRjivBSwiw`).
- Prefab: Python UI representation about 70% smaller than JSON (`Krzs8GeiWTc`).
- Google MCP Toolbox: about 20 million tool calls last month (`9R--1tg45Jg`).
- Scan: about 10,000 skills, 367 flagged as malware (`ZyC56eV8sVw`).
- Agent payments: Stripe demo capped a token at $25 and rejected a $50 charge (`KLSuFPj2ld0`). Card fees of $0.25 plus 2.5% make micropayments uneconomic (`qTZirYu9pr0`).
- Agent-readiness: about 50% of sites publish llms.txt, and about 40% of agents that use it only do so when the docs point to it (`waI44NP1abk`).

## From creator channels (Kai Explains, AI LABS, Better Stack)
Source: 152 creator notes (tutorials, news, reviews). Most numbers come from one creator's own run, so treat them as practitioner signals, not benchmarks. Sponsored segments are flagged where they appear.

### Practical playbook
1. **Cap the MCP servers attached to each agent.** One creator saw instruction-following and tool choice slip past 5-6 connected servers, and cut from 8-9 back down (`Rrju5Y0iiBM`). Single anecdote.
2. **Measure tool-definition cost before blaming the protocol.** Compare context use with and without a server. One creator saw three MCP servers take about 10% of the window before any message (`opZpIN8g_6M`). A Playwright MCP run loaded about 3.6k tokens of definitions, about 15% of context, before the task started (`V2qjnBDZZ7A`).
3. **Load tool schemas on demand in Claude Code.** The tip is Claude Code's experimental MCP CLI flag. It moves schemas out of upfront context and routes calls through a bash layer. The flag name is not spoken in the video, so check the current docs first (`iC9loBJjduM`).
4. **Write big tool output to files, and grep logs instead of re-running.** Add a CLAUDE.md rule: MCP responses over 50 lines go to a folder under `.context`, and later steps read that file (`iC9loBJjduM`). The same creator logs stdout and stderr to timestamped files, then greps and reads the last 20 lines.
5. **Keep a per-session history file.** Have the agent append key decisions after each task. It recovers details that compaction summaries drop (`iC9loBJjduM`). `QUHrntlfPo4` uses a similar snapshot idea.
6. **Shape results in code before they reach the model.** A script can filter or slice a large result, for example return the first 5 of 10,000 rows (`opZpIN8g_6M`). This summarizes an Anthropic write-up. The video shows no code.
7. **For browser steps in a terminal agent, try a CLI skill.** Install the Playwright CLI, name its skill in the prompt, and describe steps in plain language. The skill cost about 68 tokens. The whole task used about 16% of context, against about 18% for MCP, in one run (`V2qjnBDZZ7A`). Keep MCP when the loop must run outside a terminal, and turn off optional tools you do not use.
8. **Drive UI checks by snapshot, then verify with a screenshot.** Run the tool's `--help`, take a snapshot, act on element references, screenshot, and re-check. Use a multimodal model. The demo used a text-only model that could not read its own screenshots (`P7JrP57AxR0`).
9. **Attach to your real Chrome only when you need login state.** Chrome 144 or later, with remote debugging on, lets Chrome DevTools MCP attach to your running session. For untrusted work, point it at a separate user-data directory so it sees no cookies (`51m_GGbXAng`).
10. **Split draft from send, and gate send in the UI.** Expose only a draft tool to the model. Put send, delete and pay behind a button the model cannot call. A founder says a model once sent an email when asked only to draft. Also give the agent one write-only workspace with no delete or move rights (`46EsyQYKMjA`). Single founder interview, no evaluation.
11. **Design remote MCP servers to be stateless.** The July 2026 spec drops the handshake and session ID. Protocol info moves into a per-request meta field, and gateways can route on MCP headers (`f4mI3d-nTrI`). This is the creator's reading of the spec, not a test.
12. **Own state with opaque handles.** When a tool holds a live transaction, cursor or login, mint a handle, store state server-side, and check ownership on every call. Never trust a handle the model echoes back (`k5f1uID3GcU`).
13. **Scope WebMCP tools to the current page.** Register tools on mount and unregister on unmount. Keep the list under the spec's suggested 50 tools. Write each description for someone who has never seen the site (`uprZUcv0FSc`). WebMCP is early and Chrome-only (`jI2mYU8-PqU`).
14. **Smoke-test a local model on tool calls before you trust it.** Check that calls parse, that no tool syntax leaks into plain text, and that a no-tool question gets a direct answer. For tool calls, the model card advises thinking off and temperature 0 (`XKejQWnispc`). One community tester reported 200 of 200 clean calls.

### Tools creators recommend (tool — what for — `video_id`)
- Playwright CLI, with its Claude Code skill — browser steps in a terminal agent at low context cost — `V2qjnBDZZ7A`
- Playwright MCP server — browser control outside a terminal; trim its optional tools — `V2qjnBDZZ7A`
- Agent Browser (Vercel) — snapshot-and-act browser CLI for coding agents; Chromium only — `P7JrP57AxR0`
- Chrome DevTools MCP, auto-connect — debug against your logged-in Chrome — `51m_GGbXAng`
- Context Mode — indexes large tool output in local SQLite FTS5, keeps a snapshot across compaction — `QUHrntlfPo4`
- Claude Context — indexes a repo for hybrid vector and keyword search over MCP; slow on very large repos — `gPeWb4_DMok`
- ACI.dev unified MCP server — search and execute meta-tools that reach many apps through one server — `eWvaItBefYw`
- MCP2CLI — converts MCP servers to bash CLIs at runtime, one-hour cache — `LqN_ItMqovA`
- Google Workspace CLI — agent-friendly CLI with runtime schema lookup and field selection — `EKG9kX86u0s`
- Claude Managed Agents — hosted agents billed per session-hour; idle sessions free — `uxHolzq1NcA`
- SkyBridge (Alpic) — framework for MCP apps, with a local dashboard and tunnel — `9X8GRGcl5oA`
- AgentMail — email inboxes for agents via a CLI and skill, no MCP config — `U3TXAdpmvVk`
- Manifest — self-hosted LLM router behind a drop-in base URL; claims up to 70% cost cut in one demo — `BXme4u4uoyA`
- Docker Agent — agents as YAML, served over A2A or MCP with one command — `Mph1H5u3yeA`
- Flint (Microsoft Research) — model emits small semantic JSON, compiler emits chart specs; research preview — `xFWhiWe91BE`
- DBX — free database client with an MCP server; plaintext passwords flagged as a blocker — `b6rVCrBPbe8`
- Lightpanda — low-memory headless browser for agent fetches; fails on single-page apps — `yFWYK3wN88w`
- Bumblebee (Perplexity) — read-only scanner of dev machine packages, extensions and MCP configs — `L6iAw5yitfc`

### Where creators agree or clash with the conference talks
- **Agree: bloat and on-demand loading.** Creators land where the conference section above does: few tools up front, schemas loaded when needed (`iC9loBJjduM`, `Rrju5Y0iiBM`, `k5f1uID3GcU`). One creator says the fix belongs in the client, not the server (`k5f1uID3GcU`).
- **Agree: CLIs are cheap for agents.** Several creators pick a CLI for token cost (`V2qjnBDZZ7A`, `EKG9kX86u0s`, `LqN_ItMqovA`). This matches the MCP-vs-CLI split above. The creator evidence is single runs, so no clean winner. Kai's view is to learn MCP first and add A2A only for several independent agents (`psszX04xeGU`).
- **Agree: auth is the hard part.** `k5f1uID3GcU` says authorization is the top issue server authors raise, and clients implement it differently. This matches the identity and credentials section above.
- **Agree: WebMCP is early.** The conference section lists it as a proposal. The creators add that it is Chrome-only, and a community bridge breaks tool switching (`uprZUcv0FSc`, `jI2mYU8-PqU`).
- **Clash: is MCP dying?** Creators disagree. Kai calls "MCP is dead" a misreading and says adoption grew (`Rrju5Y0iiBM`). A founder says MCP is unreliable today and will end up hidden behind connectors (`46EsyQYKMjA`). Better Stack says the July spec fixes the early design (`f4mI3d-nTrI`). The conference section does not settle this.
- **Possible change: MCP Tasks.** The conference section says Tasks lack client support. `f4mI3d-nTrI` describes Tasks as official in the July 2026 spec. Check the spec before relying on either claim.
- **Clash: pixels or structure in the browser.** Creators favor snapshot and element-reference loops (`P7JrP57AxR0`, `V2qjnBDZZ7A`). The Better Stack host of the Lightpanda review says Chrome is still needed for SPAs (`yFWYK3wN88w`). Both are single tests.
- **Caveats.** The 46.9% MCP-discovery saving in `iC9loBJjduM` is Cursor's own figure, repeated by the creator. The 70% router saving in `BXme4u4uoyA` comes from one demo. `iC9loBJjduM` also has a sponsored read (about 2:30 to 3:50), which this section does not rely on.

### Watch first (3-6 `video_id` — why)
- `Rrju5Y0iiBM` — clearest creator take on why "MCP is dead" misreads the moment, with the tool-bloat and stateless-spec points. Host's figures are secondhand.
- `f4mI3d-nTrI` — short walkthrough of the July 2026 stateless spec: meta field, headers, handles, input-required round trips, tasks.
- `iC9loBJjduM` — concrete CLAUDE.md rules for offloading tool output and the experimental MCP CLI flag. Has a sponsored segment.
- `V2qjnBDZZ7A` — the one clean cost test of CLI vs MCP tool-definition overhead. One run, small gap.
- `k5f1uID3GcU` — owner-checked handles and why auth fragmentation matters more than the transport change.
- `opZpIN8g_6M` — MCP-as-code idea and its trade-off with sandboxing. No code shown, and the 10% figure is from one three-server setup.

## Watch first
- `vh2VGuQ3zhY` — the clearest numbers on why large tool catalogs fail and how top-K routing fixes it.
- `0n3MKk7r60w` — a year of running a big public MCP server: tool count, output trimming, scope-filtered auth, stateless design.
- `8txf05vVVl4` — code mode with search plus execute and a zero-capability sandbox.
- `jJQoVkd5yLg` — a practical story of deleting a thin endpoint-wrapper MCP server and rebuilding it workflow-shaped.
- `pAnLpiAG6Es` — the best map of fixes for context bloat: sub-agents, discovery, code mode, CLIs.
- `ws9XcGGPBDk` — per-tool-call token exchange and mission-scoped authorization for the lethal trifecta.
- `Uv0nAf_7tyU` — brain, hands and session split, with credentials kept out of the sandbox.
- `_B4Pv9ttFgY` — agent-facing interface lessons from Chrome DevTools MCP: summaries, tokens per success, errors that guide.

## Implications for our projects
- Add a risk review for third-party skills and MCP servers, with tool-description scanning (`1EZdpEhwmNc`, `1tpqdglI3T0`, `ZyC56eV8sVw`).
- Track agent-friction traces and tokens per successful outcome as registry health signals (`Lrw0jqBNaw0`, `_B4Pv9ttFgY`).

**AgentOS**
- L1 Govrix Scout: add per-call token exchange and policy-before-mint (`I3znWC3MEXM`, `ws9XcGGPBDk`). Add an egress credential-injecting proxy so the model never holds secrets (`Uv0nAf_7tyU`, `8aVbXXvJUY4`).
- Add progressive tool discovery or top-K tool routing as a proxy pillar, with a K-sweep eval (`vh2VGuQ3zhY`, `x2bH0RKPgdc`). This also fits the benchmark-first thesis.
- Add a per-tool hard cap, such as three calls per request, as a deterministic guard (`YXiLj4tJt5A`).
- Spend caps live in the proxy, not the agent (`KLSuFPj2ld0`, `qTZirYu9pr0`).
- L2C Crucible: start sandboxes with zero capability and grant named functions (`8txf05vVVl4`, `SKDJo2CopRs`). Match the sandbox to the task and keep tokens outside (`ZUZVNKFSmTM`). Fuzz-test the sandbox with agent-written workflows, with results in SQLite (`k72eLcYpVys`).
- L2D SkillForge: use trace-to-skill distillation and learn from failures (`u-o0sW9nwmk`). Add scan-before-publish for prompt injection and PII. Skills need versioning, evals and lint (`LC3-P7v3yoI`, `17-YSUHo6Lk`). Test skills with baseline, tool-only and tool-plus-skill runs (`JT3OzDKrucU`).
- L2A MemoryMesh: graphs hold only metadata and links, with deterministic structure first (`kRkcNOsRyYg`, `KhRjivBSwiw`). Hybrid BM25 plus vector with RRF, and a reranker only if latency allows (`ksjwtQop4os`). Ground every node in code or a trace (`k2ClBT4aqAg`).
- L4 observability: log every tool call with actor, subject and plan ID as receipts (`q-WOjZhOMCA`). Record retrieval traces (`cKhpeEBnT1o`).
- DuckDB read tier: Neo4j and Postgres-style graphs and warehouse metadata can serve agents through MCP while the data stays in place (`kRkcNOsRyYg`).

**ProsHarness**
- Keep the approval gate in the tool path, not the prompt. The phone-approval flow fits this (`tDArkCqjA-c`, `q-WOjZhOMCA`). Treat approvals as a policy check and not the whole control (`ws9XcGGPBDk`).
- Credential handling: the zero-token design matches runtime injection at a proxy (`Uv0nAf_7tyU`, `xn8EsW0wxyc`).
- Checkpoint and resume: an append-only event log with a stateless brain makes resume easy (`Uv0nAf_7tyU`). Temporal-style per-step activities also help (`VjEP0xqTUI0`).
- Use ACP to drive Codex and Claude Code through one client, and bundle a pinned harness binary (`HsxQICTLF84`, `9WiBJRO84yY`, `YkNulwcc5jk`).
- Skill ranking: show only name and description up front, and load bodies on demand (`ynJyIKwjonM`, `LC3-P7v3yoI`).

**Recurring interests**
- Entity resolution and Haiku pipelines: a cheap model can handle search and browsing steps (`zTZ0qunQXnM`, `XsvUhpnHepE`). Code mode over a spec saves tokens for rule-matcher style tools (`8txf05vVVl4`). Validate content before the LLM sees it (`XsvUhpnHepE`).
