# Perplexity Open-Sourced a Scanner Every Dev Should Know (Bumblebee)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `L6iAw5yitfc` · [watch](https://youtu.be/L6iAw5yitfc) · **date:** 2026-06-02 · **length:** 8:22 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Better Stack host (unnamed) · **orgs:** Perplexity, Better Stack
- **topics:** security-guardrails, dev-tools, mcp-and-tools · **tags:** supply-chain-security, endpoint-inventory, ndjson, mcp-config-audit, incident-response, go, read-only-scanner, bumblebee

> Better Stack demos Perplexity's open-source Bumblebee, a read-only Go binary that inventories a dev machine's packages, editor and browser extensions, and MCP configs from local metadata, for supply-chain incident response.

## Summary
The host introduces Bumblebee, a single-binary, read-only scanner that Perplexity open-sourced days before the video, built for the case where a supply-chain advisory drops and you need to know which developer machines are exposed. He installs it with go install from GitHub, runs its built-in self test against fixture data, and runs a baseline scan that emits one NDJSON record per finding (ecosystem, name, version, source file, confidence, metadata). The scanner only reads metadata files and never invokes npm, pip, or project code, which is the argument for using it during an incident. It has three profiles: baseline for routine inventory, a project profile for known workspace folders, and a deep incident-response profile over explicit roots with an exposure catalog and a duration limit. The host argues it fills a gap between CI, container, and EDR visibility, and recommends a weekly baseline scan with the output sent to a central store. Caveats: it is brand new, macOS and Linux only, and only as good as its advisory data. It is not EDR and does not replace a security stack.

## Key ideas
- **Bumblebee is a read-only scanner for local developer state. It inventories packages, editor and browser extensions, and AI tool configs from metadata, without running package managers or project code.** — The host's core argument: running npm or the package manager during an incident might trigger the malicious lifecycle scripts you are trying to find. Reading files avoids that. ([0:00](https://youtu.be/L6iAw5yitfc?t=0))
- **It fills a gap that SCA, SBOM, CI, container, and EDR tooling leaves open. SCA covers app dependencies, SBOMs cover what you shipped, and EDR covers what was executed. Bumblebee covers what is installed on the developer machine.** — Dev laptops hold half-finished projects, old clones, global packages, test virtualenvs, and AI tooling that never appear in the official inventory. ([2:37](https://youtu.be/L6iAw5yitfc?t=157))
- **Output is NDJSON with one structured record per finding. Each record has ecosystem, package name, version, source file, confidence, metadata, and where it was found.** — The host frames the boring format as a feature: it pipes into jq, ships to a file, goes through MDM or a SIEM, or feeds an agent workflow. ([1:24](https://youtu.be/L6iAw5yitfc?t=84))
- **Three scan profiles map to three situations. Baseline is for routine recurring inventory, project covers known workspace directories, and the deep incident-response profile takes explicit roots (even home) with an exposure catalog and a duration limit.** — The host's rule of thumb: baseline when things are calm, deep scan when there is smoke. ([3:46](https://youtu.be/L6iAw5yitfc?t=226))
- **MCP configs are treated as the new .env files and are a first-class scan target alongside package and extension inventories.** — Coverage includes npm, pnpm, yarn, bun, and Go modules, plus supported MCP JSON configs. ([4:45](https://youtu.be/L6iAw5yitfc?t=285))
- **The tool is a single Go binary with zero non-standard-library dependencies, no daemon, and no service. The host calls it fast and dev-friendly.** — Speed is asserted, not measured. The only figure given is the 'local inventory in seconds' claim at the start. ([1:24](https://youtu.be/L6iAw5yitfc?t=84))
- **Limits: it is brand new and expect changes, it targets macOS and Linux only, and its exposure matching is only as good as its advisory data. The host explicitly says it is not EDR and not a replacement for the security stack.** — The recommended use is a weekly baseline dumped to a central store, so that during an incident you can search across machines instead of asking in Slack. ([5:54](https://youtu.be/L6iAw5yitfc?t=354))

## Techniques
- **Weekly baseline inventory dumped centrally** — Install via `go install` from the GitHub repo, run `bumblebee self test`, then `bumblebee scan profile baseline` redirected to an NDJSON file (the exact flag syntax is not clearly shown in the auto-captions). Ship the NDJSON to a central location via MDM, a file share, or a SIEM. *When:* Run weekly on developer endpoints so that when an advisory drops, you can search existing snapshots instead of polling everyone.
- **Escalate scan depth by incident state** — Use the baseline profile for routine checks. For an active advisory, switch to the deep incident profile, passing explicit roots (for example the home directory) plus an exposure catalog and a duration limit. The exact command was not captured in the auto-captions. *When:* When a supply-chain advisory or suspicious package appears and you need exposure data quickly.
- **Query NDJSON with jq or a SIEM** — Pipe the NDJSON output to jq to filter by ecosystem or package name, or ingest it into a SIEM and search for a package name across all machines. *When:* After a scan, to answer 'which laptops have package X at version Y' in the first hour of an incident.
- **Treat MCP configs as part of the secret and dependency surface** — Include supported MCP JSON configs in periodic inventory, alongside package managers and editor and browser extensions. *When:* On any machine where local AI agents or MCP servers run.

## Numbers
- Local inventory returned in seconds (the host's claim, not a measured benchmark) ([0:00](https://youtu.be/L6iAw5yitfc?t=0))
- Three scan profiles: baseline, project, and deep incident-response ([3:46](https://youtu.be/L6iAw5yitfc?t=226))
- Single Go binary with zero non-standard-library dependencies ([4:45](https://youtu.be/L6iAw5yitfc?t=285))
- Coverage: npm, pnpm, yarn, bun, Go modules, editor and browser extensions, and supported MCP JSON configs ([4:45](https://youtu.be/L6iAw5yitfc?t=285))
- Recommended cadence: a baseline scan once a week ([7:12](https://youtu.be/L6iAw5yitfc?t=432))

## Hot takes
- Supply-chain incident response should not run the package manager on the suspect machine. Scanners should read metadata only.
- MCP configs are becoming the new .env files and deserve the same inventory treatment.
- Dev machines are the blind spot between CI, container, and EDR visibility.
- Most of the video is a plug for subscribing, and the substance is one tool demo with light caveats. The tool is also brand new, so the claims are untested.

## Tools mentioned
Bumblebee (Perplexity open-source scanner), Go (go install, single binary), npm, pnpm, yarn, bun, Go modules, VS Code, Cursor, Claude, jq, MDM, SIEM

## Relevance to our work
- **agentos** (1/3): Local MCP and agent config inventory is adjacent to AgentOS's security pillar (PII and prompt-injection scanning) and the zero-trust framing of L1 Govrix. It is a dev-machine scanner, not a gateway feature, so the fit is indirect. → *Evaluate Bumblebee's MCP-config coverage as a reference for listing which MCP servers a developer machine exposes, before deciding whether AgentOS should document or check this during setup.*
