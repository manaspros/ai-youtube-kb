# Guide: sandboxing-execution

*Synthesized by Sonnet from 60 talks since 2026-05-18.*

## State of the art

Practitioners now treat the sandbox as the default home for any agent that runs model-written code. The question is no longer whether to isolate, but how strong the wall is and who holds the secrets.

- **Isolation strength.** The OpenAI sandbox talk ranks options by how much host-kernel surface they expose: fork/exec, then containers, then gVisor, then microVMs. It says containers are not a real security boundary and advises startups to begin with microVMs (`OqM67QG_Ikk`). Docker sells the same view as a product: a per-project microVM with default-deny egress (`OE_lLNCNfQo`). Not everyone goes that far. Red Hat and OpenHands still use plain containers and pods, with explicit mounts (`F1DYkY1BlfM`, `iH_wV8BbS24`).
- **Zero credentials inside the sandbox.** This is the strongest recent pattern. The sandbox holds a placeholder or nothing. A proxy or gateway outside it adds the real token on the way out. Anthropic, Google, Docker, Deno, and Tailscale all describe this (`Uv0nAf_7tyU`, `8aVbXXvJUY4`, `ZUZVNKFSmTM`, `MkRYPFIMCSA`, `BM2JX9hqsVQ`).
- **Brain and hands are split.** The agent loop runs in one place. The sandbox is a replaceable tool, started only when a tool call needs it. Durable state lives outside the sandbox, in a session log or step store (`Uv0nAf_7tyU`, `K0X9QDRkIdg`, `X1kp-ABIIxQ`).
- **Persistence through snapshots.** Idle sandboxes are paused and resumed instead of rebuilt. Disk and memory are snapshotted, forked, and restored (`fz6-NS7qpZc`, `svCnShDvgQg`, `OqM67QG_Ikk`). Managed offerings expose an environment ID to reattach to the same machine (`8aVbXXvJUY4`, `oWTEiYpxl80`).
- **Agents move off the laptop.** Cloud sandboxes per project or per session are the norm for long, unattended runs (`iH_wV8BbS24`, `OL7kfezynJM`, `TRfzFJCJ7ZE`, `abw_m-DRi1k`).
- **Deny by default for generated code.** Cloudflare starts code with no network and no APIs, then grants named functions (`8txf05vVVl4`, `SKDJo2CopRs`).
- **Sandboxes as eval infrastructure.** An environment is an instruction, a sandbox, and a verifier. Rollouts run in fresh sandboxes at scale (`jRCpXUjz4CI`, `Ib5t2RLtxvM`, `YIxzNZDDy1A`).

## Consensus patterns

1. **Never trust the prompt as a boundary.** Put controls in infrastructure: network, kernel, identity. Examples include Docker's self-test where an agent found personal data (`OE_lLNCNfQo`), Deno's point that refusals do not stop prompt injection (`MkRYPFIMCSA`), PostHog's rule that prompts are not security (`4lXks428C9o`), and the Replit and bank incidents (`Wb2v9Phhnns`).
2. **Keep secrets outside the sandbox.** Use a credential-injecting proxy, a vault, or a gateway. Sources: `Uv0nAf_7tyU`, `K0X9QDRkIdg`, `8aVbXXvJUY4`, `BM2JX9hqsVQ`, `MkRYPFIMCSA`, `ZUZVNKFSmTM`, `F1DYkY1BlfM`.
3. **Default-deny egress with an allowlist, and log what is blocked.** Sources: `OE_lLNCNfQo`, `fz6-NS7qpZc`, `imFedndyXYQ`, `abw_m-DRi1k`, `Wb2v9Phhnns`.
4. **One sandbox per task, sized to the task (least privilege).** Mount only the repo and secrets the task needs. Sources: `iH_wV8BbS24`, `ZUZVNKFSmTM`, `Uv0nAf_7tyU`, `Wb2v9Phhnns`.
5. **Split roles across sandboxes when input is untrusted.** Do not combine untrusted reading with dangerous write access. A research stage gets the web and no write tools. A publish stage gets writes and no network (`ZUZVNKFSmTM`). The "lethal trifecta" framing says the same (`abw_m-DRi1k`, `Wb2v9Phhnns`).
6. **Separate deterministic orchestration from agentic steps.** Plain code does clone, commit, push, and CI. The agent gets file edits only (`LqLoYksJ6do`, `rAUyRDOFyHU`, `CLttOU7n6sI`). Put hard rules before any LLM judge, and fail closed (`4lXks428C9o`).
7. **Persist the session outside the sandbox.** Sandboxes are ephemeral, so durability belongs in a log or step store (`X1kp-ABIIxQ`, `svCnShDvgQg`, `K0X9QDRkIdg`, `HvMyYLTfvhg`).
8. **Snapshot, pause, resume, and fork instead of cold starting.** Sources: `fz6-NS7qpZc`, `svCnShDvgQg`, `OqM67QG_Ikk`.
9. **Gate risky actions with a chain.** Rules first, then an LLM judge, then a human (`MkRYPFIMCSA`). Use a deterministic approval interrupt for mutating tools (`4uFVSLgD2Q4`).
10. **Route model and tool traffic through one policy point.** This can be an LLM gateway, model proxy, or MCP gateway (`BM2JX9hqsVQ`, `abw_m-DRi1k`, `ZUZVNKFSmTM`, `Wb2v9Phhnns`).
11. **Layer defenses.** Admission control, runtime enforcement, network policy, and input/output guards all matter. A fork bomb needs prevention, not detect-and-kill (`1tpqdglI3T0`).

## Disagreements & open questions

- **How strong is strong enough?** The OpenAI talk says every option short of a VM can still reach the host kernel, so it recommends microVMs from the start for untrusted code (`OqM67QG_Ikk`). The Ona talk argues dev tasks should run in a VM, not a container (`5Sui_OnSRlY`). Red Hat and OpenHands ship containers and pods and call them reasonable (`F1DYkY1BlfM`, `iH_wV8BbS24`). OpenHands also admits sandboxes are only a first pass, citing an escape (`iH_wV8BbS24`).
- **Where to put the guard.** Options are the network layer (`BM2JX9hqsVQ`), a byte-level proxy that understands protocols like Postgres (`MkRYPFIMCSA`), an MCP gateway (`ZUZVNKFSmTM`), a process-level command denylist (`abw_m-DRi1k`), or Kubernetes admission and eBPF (`1tpqdglI3T0`). No talk shows these compared head to head.
- **Persistent versus fresh environments.** Long-lived VMs give persistence but let co-located agents damage each other's state (`iH_wV8BbS24`). Managed products push persistent per-conversation environments (`oWTEiYpxl80`, `8aVbXXvJUY4`). Resumed sandboxes also collect orphan processes (`fz6-NS7qpZc`).
- **Snapshot approach.** Process-level checkpointing (CRIU) was not enough for Trigger.dev, who moved to Firecracker (`svCnShDvgQg`). OpenAI favours block-level disk snapshots (`OqM67QG_Ikk`). Replay-based durability is judged a poor fit for agent loops (`svCnShDvgQg`).
- **Containers or Wasm and isolates for startup speed.** Cloudflare and Akamai claim near-zero cold starts (`SKDJo2CopRs`, `Zf_e45GiNCE`). These are vendor claims, not measured in the talks.
- **Computer use inside sandboxes.** Reliability is low on real professional tasks. Cua reports no model above 30% reward on KiCad tasks (`ZSQb5fzRFPw`). Simular argues for replaying successful runs as code (`tyFPqtyOK5w`).
- **Open: GPU access.** GPUs are a known weak spot for microVM isolation (`OqM67QG_Ikk`).
- **Open: realistic training environments.** Single-node sandboxes only partly simulate real infra (`zkX03APVj0M`).

## How thinking changed over time

- **2026-05-18.** Sandboxing is framed as a runtime design choice. Cloudflare's code mode starts from zero capabilities (`8txf05vVVl4`). Vercel says harnesses should run apart from the code they generate (`XKup1pj-34M`). Trigger.dev splits durability into a log plus VM snapshots (`svCnShDvgQg`).
- **2026-06-18.** Containers are the default recommendation (`F1DYkY1BlfM`). Voices start to push VMs over containers (`5Sui_OnSRlY`). Tailscale proposes the network as the sandbox, with zero keys inside (`BM2JX9hqsVQ`).
- **2026-07-18.** First-principles case for microVMs, and for storage and snapshots as the next unlock (`OqM67QG_Ikk`). Sandboxes become a standard step in security harnesses: no egress, pinned baseline (`imFedndyXYQ`). Constrain effects through a typed SDK, not reasoning (`CLttOU7n6sI`).
- **2026-08-18.** Brain/hands split becomes a product (`K0X9QDRkIdg`). Production access is the worry: egress firewalls and credential injection (`MkRYPFIMCSA`, `LqLoYksJ6do`). Sandboxes also become the unit for evals and RL rollouts (`jRCpXUjz4CI`, `Ib5t2RLtxvM`).
- **2026-09-18.** Sandbox per approved job or per cloud agent is assumed (`pPj_tjlvYjA`, `L173Z8DpaJg`). Teams treat enforced walls as better than prompts (`xxfMT-bPEmU`, `4lXks428C9o`).
- **2026-10-04 to 2026-10-15.** Peak of the topic. Docker pushes microVMs with placeholder secrets (`OE_lLNCNfQo`, `ZUZVNKFSmTM`). Google ships persistent managed sandboxes with environment IDs (`8aVbXXvJUY4`, `oWTEiYpxl80`). E2B teaches snapshot, fork, and timeouts (`fz6-NS7qpZc`). OpenHands lays out a four-way comparison (`iH_wV8BbS24`). Coder frames infra controls, not smarter models, as the fix (`abw_m-DRi1k`, `Wb2v9Phhnns`). AWS fuzz-tests a sandbox platform with agents (`k72eLcYpVys`).

## Numbers worth remembering

- Time to first token fell about 60% at P50 and over 90% at P95 after splitting the brain from the sandbox (`K0X9QDRkIdg`). The workshop version cites about 90% from lazy sandbox provisioning (`Uv0nAf_7tyU`).
- A 512 MB default VM snapshot shrank to about 14 MB with seekable compression and layering (`svCnShDvgQg`).
- E2B aims for sandbox startup under 100 ms. This is a stated aim, not a measurement. The workshop made about 200 copies from one snapshotted template (`fz6-NS7qpZc`).
- A first request on a fresh remote managed environment takes about 7 to 10 seconds (`oWTEiYpxl80`).
- Search plus execute cut a roughly 2,600-endpoint API from about 1.2M tokens to about 1,000 (speaker figure) (`8txf05vVVl4`).
- A fork bomb can spawn many processes in about 200 ms, so response-based controls are too slow (`1tpqdglI3T0`).
- A laptop runs about one agent comfortably, while Kubernetes can run thousands (`iH_wV8BbS24`).
- Agent-written fuzz test of a sandbox platform: about 1,000 tests across 10 domains. The cloud browser failed mostly from memory exhaustion (`k72eLcYpVys`).
- The agent needed git signing keys for about 2 of 60 minutes, so credentials should be scoped per step (`ZUZVNKFSmTM`).
- Docker's self-test: Claude Code found browser history and bank data in about five prompts (`OE_lLNCNfQo`).
- Cua Driver raised pass rate from about 62% to about 80% with 34% fewer tokens (`ZSQb5fzRFPw`).
- Terminal-Bench 2.0 has 89 tasks. Run each configuration at least five times (`YIxzNZDDy1A`). A demo ran 64 parallel rollouts (`jRCpXUjz4CI`).
- A documented threat model reportedly lifted vulnerability true-positive rate to about 90% (`imFedndyXYQ`).
- Replit incident: about 4,000 fabricated profiles (`Wb2v9Phhnns`).

## From creator channels (Kai Explains, AI LABS, Better Stack)

Source: 43 creator videos, mostly Better Stack tutorials and reviews. Most points rest on one video each. Sponsored segments and vendor numbers are flagged where they appear.

### Practical playbook

1. Match the wall to the job. For a quick laptop sandbox, plain containers or Anthropic's lighter sandbox runtime are much less work. Move to a stronger wall, such as OpenShell or a micro-VM, once the agent holds real credentials or runs unattended (`SbwckhZkPGs`).
2. Never give a container the Docker socket. Mount only the directory the tool needs, or put a socket proxy in front of the daemon. Drop privileged mode and add only the capabilities the process needs. SYS_ADMIN and SYS_PTRACE stay dangerous even then. Check the capability set with capsh from inside the container (`giXlSlFLKwA`).
3. Start the sandbox with no network. When a call fails, read the denial in the logs, then add one narrow rule for the exact method and endpoint. For OpenShell that means `openshell logs` and then `openshell policy update`. Confirm that writes are still denied (`SbwckhZkPGs`).
4. Keep keys out of the sandbox. Attach credentials at the egress point, only on requests that match an approved endpoint, so the agent process never holds the secret. Give each agent its own key so one can be revoked alone (`SbwckhZkPGs`, `CB6Ysb_BLcM`).
5. Bind network rules to the calling binary. The same host can then be open to one process and closed to another inside one sandbox (`SbwckhZkPGs`).
6. Review each policy diff before it goes live. OpenShell runs a Z3 check, with a 10-second default limit, that shows what new access a rule grants. It catches wildcards that match more than intended (`SbwckhZkPGs`).
7. Do not trust a green doctor check. On a Mac, confirm that Docker Desktop's VM provides the Landlock feature and enable host networking if your policies need it. Turn off telemetry with the environment variable (the video does not name it). Then test the real blocked call (`SbwckhZkPGs`).
8. Run an always-on agent on its own non-root VPS user, not on your main machine. Keep its admin UI off the public internet: use Tailscale, Tailscale serve, or an SSH tunnel, and disable public SSH. Expect prompt injection to remain. Scrub stored transcripts, since they hold anything shared in chat (`CB6Ysb_BLcM`).
9. Keep local model servers off the network. Do not bind Ollama to 0.0.0.0, because that also turns off its host-header check. Docker port publishing bypasses UFW rules. Patch the runner, and read a GGUF's chat template by hand before serving it. Scanners do not check templates. The video's version numbers are inconsistent in the captions, so confirm them in upstream release notes (`3mx84MRj8lY`).
10. Gate merges on validated findings. Run a security scanner as a GitHub Actions step that exits non-zero on a validated finding. Accept only findings that come with a working exploit and reproduction steps. Review any autofix PR like any other change (`vRTliPb8fjg`).
11. For parallel coding agents, give each subtask its own sandbox in clone mode. Pull each diff back, then delete the sandbox after you confirm. Assign each shared file to one session in its prompt. This is a sponsored segment (`qxjII6x2yPY`).
12. For generated code, create a sandbox per run and discard it afterwards. Keep the app's own services outside the sandbox. Read the container logs while a task runs, because some errors appear only there (`idBEifQwlGI`, `aqF8ItxLCRA`).
13. Pick the runtime by need. A Cloudflare Dynamic Worker is fast and JavaScript only, and its network can be turned off. A Cloudflare Sandbox has a full OS and any language (`7Re3HReM5SQ`). For the Sandbox SDK, wire a Worker, a Durable Object and a container. Get a sandbox by ID, run exec, and re-export the class from the entry module (`0bkeZOXNJBg`).
14. Scope shell access to one folder. Give the agent read-only tools over that folder and nothing outside it. Log each tool call so you can see the path it took (`gZr5VmsXmXQ`).
15. For evals, run the strict version too. Remove git history, deny network by default, and allow only a package-registry proxy. Compare scores both ways. Count runs that fetched the upstream fix instead of deriving it (`pHAbwL7w83Q`).

### Tools creators recommend

- OpenShell — per-request egress policy, supervisor-side credential injection, audit log, on top of containers — `SbwckhZkPGs`
- Docker Sandbox (sbx) — disposable micro-VM per task, with clone mode — `qxjII6x2yPY` (sponsored segment)
- Cloudflare Sandbox SDK — container sandbox driven from a Worker for untrusted code — `0bkeZOXNJBg`
- Cloudflare Dynamic Workers — runtime child Workers on V8 isolates, JavaScript only — `7Re3HReM5SQ`
- Vercel Sandbox — ephemeral sandbox per generated-code run, billed on active CPU — `idBEifQwlGI`
- Strix — multi-agent pen test with a CI exit code and autofix PRs — `vRTliPb8fjg`
- Shannon — AI pentester with Temporal checkpoints for multi-hour runs — `H7Xh-x_TVdQ`
- Tailscale — private network for gateways and admin UIs — `CB6Ysb_BLcM`
- Incus and Code On Incus — system containers per agent role, with a shared workspace — `t78-JUnTK5Q`, `zaAtYkM24hU`
- Apple Container Machines — persistent per-container Linux VM on macOS — `xXtsuDnapqc`
- Agent of Empires — one git worktree per agent, with an optional Docker sandbox — `fPz9OB3Bau8`
- just-bash — in-memory bash for agents, with no container — `EoyLzyJUcfI`
- Podman, rootless — daemonless Docker alternative with less host exposure — `SIvoAOpXZPg`
- Cisco open-source skill scanner — scan third-party skills before install — `M3P0hQMQtq0`
- Cloudflare Artifacts — git-compatible repo store for fork-per-task agents, in private beta — `PWj6GnTUBnk`

### Where creators agree or clash with the conference talks

- Agree on the core rule. Creators also say a prompt is not a boundary. OpenShell puts the boundary in the supervisor, and the Clawdbot walkthrough says no hardening step stops prompt injection (`SbwckhZkPGs`, `CB6Ysb_BLcM`).
- Agree that privacy is not safety. Kai Explains argues that a local model can act on the machine through its template, runner, port or tools. This matches the conference view that the fix is to limit what the model can reach (`3mx84MRj8lY`).
- Clash on how strong the wall must be. The creator view is that plain containers are fine for a quick laptop task, and stronger walls pay off only when credentials or unattended runs are involved (`SbwckhZkPGs`). The conference talks say containers are not a real boundary and push micro-VMs. Creators frame the choice as cost against task risk, not kernel escape.
- Clash on the claim that micro-VMs are the only option. The Docker Sandbox segment calls it the only sandbox approach that lets a coding agent build and run containers while staying isolated. The notes flag that claim as unverified (`qxjII6x2yPY`).
- Speed claims stay unmeasured on both sides. The Cloudflare claims of 100x faster and up to a million dynamic workers per second are quoted from the announcement, not measured (`7Re3HReM5SQ`).
- Vendor maturity is a warning. OpenShell is version 0.x, and the creator cites about 12% failed sandbox creations in vendor telemetry. He says the README's stable-release claim does not match (`SbwckhZkPGs`).
- Benchmark claims need checking. Strix cites a 96% solve rate on a benchmark that the video does not verify (`vRTliPb8fjg`). A full Shannon run took about 2.5 hours and about $60 on one target. That is a single run (`H7Xh-x_TVdQ`).

### Watch first

1. `SbwckhZkPGs` — the clearest creator walk-through of per-request egress policy and credential injection, with honest caveats.
2. `3mx84MRj8lY` — five-layer threat model for local models. Long, but the most careful creator treatment of model-file risk (Kai Explains).
3. `CB6Ysb_BLcM` — VPS isolation, Tailscale access, and why hardening does not solve prompt injection.
4. `vRTliPb8fjg` — CI merge gate and triage on proof. Short and practical.
5. `0bkeZOXNJBg` — hands-on Worker and Durable Object sandbox wiring.
6. `qxjII6x2yPY` — parallel sandboxes and file ownership. Skip the sponsored segment at about 10 to 12 minutes.

## Watch first

1. `OqM67QG_Ikk` — the clearest first-principles case for microVMs, plus disk snapshots and fleet scheduling.
2. `Uv0nAf_7tyU` — brain/hands/session split, credential proxy, lazy sandbox start.
3. `iH_wV8BbS24` — short, practical comparison of four isolation setups with a least-privilege rule.
4. `fz6-NS7qpZc` — hands-on snapshot, fork, timeouts, and orphan-process lessons.
5. `MkRYPFIMCSA` — why the guard must sit outside the agent, with protocol-aware rules and chained approval.
6. `ZUZVNKFSmTM` — role-split sandboxes and a single MCP gateway.
7. `svCnShDvgQg` — log plus VM snapshot durability, and why CRIU fell short.
8. `k72eLcYpVys` — what actually breaks when agents run code in a sandbox at volume.

## Implications for our projects

**AgentOS Crucible (L2C).**
- Pick the default backend by an isolation ladder. Benchmark a microVM backend (Firecracker or Cloud Hypervisor) against celld on startup latency and per-call overhead, and write down the escape assumptions of each (`OqM67QG_Ikk`).
- Make credentials a gateway feature. Crucible sandboxes should get placeholder keys, with Govrix Scout or a sibling proxy injecting the real ones (`Uv0nAf_7tyU`, `BM2JX9hqsVQ`, `OE_lLNCNfQo`).
- Default egress to deny with a per-manifest allowlist and a log of blocked calls (`OE_lLNCNfQo`, `imFedndyXYQ`).
- Add a test with two agents on one shared workspace to confirm one cannot read or edit the other (`iH_wV8BbS24`).
- Borrow the zero-capability model for generated code, and grant named functions only (`8txf05vVVl4`).
- Add snapshot, pause, resume, and an idle timeout to the spec. Watch for orphan processes after resume (`fz6-NS7qpZc`).

**AgentOS Govrix Scout (L1).**
- It sees only model traffic. Scope a protocol-aware extension for Postgres and ClickHouse, with fixture requests as unit tests (`MkRYPFIMCSA`).
- Add chained verdicts: rule, then LLM judge, then human (`MkRYPFIMCSA`).
- Run hard rules before any LLM check and fail closed. Keep the detector separate from the policy that acts on its findings (`4lXks428C9o`).

**AgentOS memory, scheduling, and benchmarks.**
- Prototype an append-only per-run event log with a swappable context builder (`Uv0nAf_7tyU`, `K0X9QDRkIdg`).
- For the benchmark-first thesis, shape tasks as instruction, sandbox, and verifier directories. Validate each with a scripted oracle before scoring models (`jRCpXUjz4CI`, `Ib5t2RLtxvM`). Try to break each environment before trusting it (`ZSQb5fzRFPw`).
- Pin versions and run each config several times (`YIxzNZDDy1A`).
- Fuzz-test Crucible itself with an agent and a SQLite results table. Tag each failure as interface or sandbox layer (`k72eLcYpVys`).

**ProsHarness.**
- Check whether checkpoints capture the working directory as well as harness state. If not, prototype an incremental workspace snapshot saved alongside each checkpoint (`OqM67QG_Ikk`, `svCnShDvgQg`).
- Test resuming a killed run from its last logged event (`Uv0nAf_7tyU`).
- Zero-token credentials map onto placeholder secrets plus a local injecting proxy, and phone approvals map onto the rule, judge, human chain (`MkRYPFIMCSA`, `OE_lLNCNfQo`).
- Audit what each Claude Code launch can see. Give it only the repo and secrets it needs, and consider running long jobs in a disposable container or VM (`iH_wV8BbS24`).
- Keep push and CI credentials away from the agent. Do clone, commit, and push in plain code (`LqLoYksJ6do`).

- Registry and MCP calls could route through one credential-injecting proxy so agents never hold tokens (`Uv0nAf_7tyU`).
- For the registry, take MCP tool descriptions through a review step and source servers from an allowlist (`1tpqdglI3T0`).
- A single MCP gateway is the natural place to set per-sandbox tool subsets (`ZUZVNKFSmTM`).
