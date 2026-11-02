# The Largest Supply Chain Attack Ever Just Infected Go

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `lNsSxWQDqaU` · [watch](https://youtu.be/lNsSxWQDqaU) · **date:** 2026-08-02 · **length:** 4:58 · **format:** news · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Warren (Better Stack host) · **orgs:** Better Stack, Socket.dev, Team PCP (group that open-sourced the worm, per the transcript)
- **topics:** security-guardrails, claude-code, coding-agents, dev-tools · **tags:** supply-chain-attack, npm, worm, shai-hulud, go-modules, claude-code-hooks, vs-code-tasks, ci-security, egress-filtering, oidc, least-privilege-tokens, credential-theft

> Better Stack explains how the self-replicating npm worm (Shai-Hulud) jumped to a Go module, hiding hooks in Claude Code and VS Code config so code runs on folder open, and lists five hardening steps.

## Summary
The video recaps Shai-Hulud, a self-replicating worm that runs at package install, harvests secrets (npm, GitHub, cloud and SSH keys), and uses stolen npm tokens to publish poisoned versions of the victim's packages. A new wave flagged by Socket.dev in late June shipped inside a Go module's source archive instead of an npm package. Its payload sits in project-level config: a .claude/settings.json SessionStart hook and a .vscode/tasks.json folder-open task, so it fires when a folder is opened or a Claude Code session starts. The speaker argues this sidesteps --ignore-scripts and that uninstalling the package does not remove the config-resident code. The stated risk extends to CI (for example GitHub workflows) if the poisoned config is committed and run. The mitigations are: treat agent and editor config as executable, turn off VS Code automatic tasks, use short-lived least-privilege tokens (OIDC), add egress filtering on CI runners, and keep secrets out of plaintext. The episode is a short security news explainer with no benchmarks and no first-hand incident data.

## Key ideas
- **The worm is self-propagating: a poisoned package runs on install, harvests tokens, and publishes poisoned versions of the victim's own packages, so no attacker is needed in the loop.** — Install-time script scans for npm, GitHub, AWS, GCP and Azure credentials and SSH keys; it also runs TruffleHog to find exposed keys for itself. Stolen npm tokens are used to republish infected packages. ([1:06](https://youtu.be/lNsSxWQDqaU?t=66))
- **The new wave crosses ecosystems. Nothing in Go tooling runs it; a Go module's source archive carries JavaScript and editor/agent config files.** — The Go module is named 'Varana Blockchain Project' in the auto-captions. Socket.dev flagged the wave at the end of June 2026. ([1:06](https://youtu.be/lNsSxWQDqaU?t=66))
- **The payload lives in project config that auto-runs: a Claude Code SessionStart hook and a VS Code folder-open task.** — .claude/settings.json registers a SessionStart hook and .vscode/tasks.json runs node on a setup script, so code executes on folder open or session start, before any build or install step. ([2:10](https://youtu.be/lNsSxWQDqaU?t=130))
- **Standard defenses are bypassed: --ignore-scripts does not cover this path, and uninstalling the package does not remove code that lives in project config.** — The speaker says the threat has moved from app dependencies to the dev environment itself, and that poisoned config can be committed and reach production or CI. ([2:10](https://youtu.be/lNsSxWQDqaU?t=130))
- **Before opening a cloned repo or a dependency's source, read the agent and editor config files as you would executable code.** — Check .claude/ hooks, settings and .vscode/tasks.json before the editor or agent opens the folder. ([3:13](https://youtu.be/lNsSxWQDqaU?t=193))
- **Make stolen credentials worthless: short-lived, least-privilege tokens via OIDC in CI, and egress allowlists on runners.** — If a token cannot be reused, the worm cannot replicate through the developer. Default-deny outbound traffic on CI runners stops exfiltration even when malicious code runs. ([3:13](https://youtu.be/lNsSxWQDqaU?t=193))
- **The payload also checks for endpoint security products (CrowdStrike, Defender, SentinelOne) before it acts.** — The speaker says the malware checks for these tools before staging its payload, but gives no detail on what it does when one is found. ([2:10](https://youtu.be/lNsSxWQDqaU?t=130))

## Techniques
- **Audit agent and editor config before opening untrusted code** — Before opening a freshly cloned repo or an unpacked dependency source, read .claude/settings.json (look for SessionStart or other hooks) and .vscode/tasks.json (look for tasks with runOn folderOpen running node or shell scripts). Remove or refuse anything unexpected before the agent or editor starts. *When:* Any time you clone a repo, pull a dependency's source archive, or open a project from an unknown author.
- **Turn off VS Code automatic tasks** — Run the 'Tasks: Manage Automatic Tasks' command (named as in the speaker's wording) and keep automatic tasks disabled, so a folder-open task only runs after you approve it. *When:* On every developer machine, as a default setting.
- **Treat .claude/ and .vscode/ as executable code in review** — In code review and dependency intake, put hooks in .claude/settings.json and task definitions in .vscode/tasks.json on the same review list as install scripts. Don't assume ignore-scripts covers them. *When:* PR review and when vetting third-party repos or archives.
- **Short-lived, least-privilege CI credentials via OIDC** — Replace long-lived tokens stored in CI environments with OIDC-issued short-lived credentials scoped to the minimum needed. Keep npm publish tokens and cloud keys out of long-lived environment variables. *When:* All CI pipelines that publish packages or touch cloud resources.
- **Egress filtering on CI runners** — Set the runner's outbound network to deny by default and allow only the hosts the build needs. The speaker's example is a GitHub-hosted CI runner with an allowlist of permitted destinations. *When:* Any CI runner that executes third-party dependency code.
- **Minimum release age for packages** — The speaker recommends setting a minimum release age in .npmrc. The video does not give the exact key name or explain the mechanism, so check the npm docs before relying on it. *When:* When installing from npm and you want a delay before picking up brand-new versions.
- **Keep secrets out of plaintext on dev machines** — Store sensitive tokens in a password manager instead of plain files or environment variables that malware can read. *When:* Developer workstations that hold npm, GitHub or cloud credentials.

## Numbers
- Shai-Hulud first hit in September 2025 and returned bigger in November 2025. ([1:06](https://youtu.be/lNsSxWQDqaU?t=66))
- In 2026 the group Team PCP open-sourced the worm and ran a contest for the biggest attack, producing copycat waves. ([1:06](https://youtu.be/lNsSxWQDqaU?t=66))
- The new wave was flagged by Socket.dev at the end of June 2026. ([1:06](https://youtu.be/lNsSxWQDqaU?t=66))
- The video gives no counts of infected packages, victims or dollar losses. The title's 'largest supply chain attack ever' is not quantified in the video. ([0:00](https://youtu.be/lNsSxWQDqaU?t=0))

## Hot takes
- The title's 'largest supply chain attack ever' is not backed by any scale data in the video.
- The strongest point is that project-level agent and editor config (Claude Code hooks, VS Code tasks) is an execution surface that an install-script allowlist does not cover.
- The 'npm uninstall no longer works' claim is asserted, not demonstrated. The transcript never shows removal being tested.
- The transcript reads '.m file' where .npmrc is probably meant (auto-caption error, not verified).
- The episode ends with a plug for a Burp Suite alternative video, but it is not a sponsored segment.

## Tools mentioned
npm, Go modules, Claude Code (called 'clawed code' in the auto-captions), VS Code (tasks.json, folder-open tasks), Bun (runtime the payload uses to stage its code), Node.js (runs the setup script), TruffleHog (secret scanner the worm reuses), GitHub Actions (CI workflows named as the risk surface), Socket.dev (security firm that flagged the wave), CrowdStrike, Microsoft Defender, SentinelOne (endpoint products the malware checks for), OIDC (short-lived CI credentials), .npmrc (minimum release age setting), Burp Suite (named only as a plug for a free alternative covered in another video)

## Relevance to our work
- **agentos** (2/3): Crucible's exec-gate guardrails and sandboxed execution have to treat project-level agent config (.claude/settings.json hooks) as executable, not as passive data. This talk is a concrete threat case for that.
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI and may launch it in repos it has not vetted. The video's hook-based attack lands at session start, which is exactly where a harness starts the agent. → *Before ProsHarness starts Claude Code in a repo, read .claude/settings.json and .vscode/tasks.json and refuse to run if they contain unexpected SessionStart hooks or folder-open tasks. Keep its zero-token credential handling so no tokens reach the hook environment.*
