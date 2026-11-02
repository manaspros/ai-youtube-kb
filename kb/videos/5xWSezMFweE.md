# Millions of JS Devs Just Got Hacked... (axios pwned)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `5xWSezMFweE` · [watch](https://youtu.be/5xWSezMFweE) · **date:** 2026-04-02 · **length:** 4:17 · **format:** news · **quality:** 3/5 · **depth:** intro
- **speakers:** Unnamed Better Stack host · **orgs:** Better Stack, npm, Axios
- **topics:** security-guardrails, dev-tools · **tags:** npm, supply-chain, axios, postinstall, lockfile, ci-cd, rat, credential-theft, incident-response, minimum-release-age

> News recap of the March 31, 2026 npm compromise of the axios package: two backdoored releases used a postinstall script to drop a cross-platform RAT. Mitigations are committed lockfiles, npm ci, a minimum package age, and blocking install scripts.

## Summary
A roughly four-minute Better Stack news segment on a supply-chain attack on the axios npm package. The speaker says an attacker took over the lead maintainer's npm account and published two backdoored versions on March 31, 2026: 1.14.1, tagged latest, and 0.30.4, tagged legacy. The malicious package pulled in a phantom dependency, plain-crypto-js, whose postinstall script (setup.js) fingerprinted the OS and downloaded an OS-specific second payload, a remote access trojan. The speaker describes the RAT as enumerating files, beaconing every 60 seconds with host and process details, and accepting four remote commands, and says it cleaned up after itself. The likely targets are developer workstations and CI/CD runners, where .env files, npm tokens and SSH keys sit. The maintainer had 2FA and GitHub Actions auth enabled, and the speaker thinks a long-lived npm token was used, with recovery codes as a possible route, but how the token was obtained is unknown. The segment closes with detection steps and four prevention habits: commit lockfiles, use npm ci, enforce a minimum package age, and block install scripts. The transcript has no primary source links, so the detailed indicators are deferred to a linked write-up.

## Key ideas
- **The axios npm account of the lead maintainer was compromised, and two backdoored versions were published on March 31, 2026: 1.14.1 (tagged latest) and 0.30.4 (tagged legacy).** — The speaker frames it as one of the largest npm supply-chain breaches. The releases were live only briefly before removal. ([0:00](https://youtu.be/5xWSezMFweE?t=0))
- **The attack used a phantom dependency with a postinstall script, so any install or CI run executed it.** — The dependency is plain-crypto-js, which the captions render as 'plain crypto.js'. It mimics the real crypto-js package. Its setup.js postinstall script checks the OS and downloads a second, OS-specific payload. The macOS payload was built for both Intel and Apple Silicon. ([0:00](https://youtu.be/5xWSezMFweE?t=0))
- **The second payload is a cross-platform RAT, and the speaker describes its capabilities in detail.** — It scans documents, desktop and config folders (on Windows also OneDrive, AppData and every drive letter) and uploads the file list. It beacons every 60 seconds with hostname, username, OS, time zone, hardware model and the running process list. The attacker can browse directories, run shell commands, drop and execute more malware, or kill the process. ([1:26](https://youtu.be/5xWSezMFweE?t=86))
- **The malware cleans up its traces, so inspecting package.json afterward can look clean.** — The setup script deletes itself, then deletes the package.json carrying the postinstall hook and replaces it with a clean version. The speaker says it should be handled as full credential theft wherever it ran. ([1:26](https://youtu.be/5xWSezMFweE?t=86))
- **Initial access is unexplained: the maintainer had 2FA and GitHub Actions auth on, and the packages were published with the npm CLI using a long-lived token.** — The speaker thinks the token was obtained somehow, and that account recovery codes may have been taken. The method is still unknown in the transcript. ([2:37](https://youtu.be/5xWSezMFweE?t=157))
- **Mitigations are committed lockfiles, npm ci in pipelines, a minimum package age, and disabling install scripts.** — The speaker says the malicious axios release was discovered and removed about three hours after publishing, which a 48-hour minimum age would have blocked. Install scripts can be skipped with the ignore-scripts flag, or a package manager can block them by default and run only listed trusted dependencies. ([3:31](https://youtu.be/5xWSezMFweE?t=211))

## Techniques
- **Detect affected installs** — Search lockfiles for axios 1.14.1 or 0.30.4 and for plain-crypto-js, and search node_modules for the package. Also check the machine for RAT artifacts, using the write-up the speaker links, since the transcript gives no indicator details. Do not rely on package.json alone, because the malware swaps it for a clean copy. *When:* After any install or CI run between the malicious publish and its removal, or whenever a lockfile may contain these versions.
- **Commit the lockfile and install with npm ci in pipelines** — Commit package-lock.json, and make CI run npm ci instead of npm install so resolved versions match the lockfile. *When:* For every CI pipeline and any repo with JS dependencies.
- **Enforce a minimum package age** — Configure the package manager to refuse packages younger than a threshold. The speaker recommends 48 hours, the window in which this malicious release was caught. The exact config key is not named in the transcript. *When:* To reduce exposure to freshly published malicious versions, at the cost of delaying urgent security patches (not discussed).
- **Block install scripts by default** — Run npm install with --ignore-scripts, or use a package manager that disables postinstall scripts by default and runs them only for an explicit allowlist of trusted dependencies. *When:* Wherever untrusted or transitive dependencies are installed, including developer machines and CI runners.
- **Treat an affected host as a full credential compromise** — The speaker says any machine that ran the payload should be treated as a full credential theft scenario. Target .env files, npm tokens and SSH keys, so the implied response includes rotating those secrets. *When:* After confirming an install of an affected version on a workstation or CI runner.

## Numbers
- axios installed about 101 million times in the week of the incident (speaker's figure) ([0:00](https://youtu.be/5xWSezMFweE?t=0))
- Roughly 174,000 packages depend on axios. The caption reads 'defendants', so this is probably 'dependents'. ([0:00](https://youtu.be/5xWSezMFweE?t=0))
- Malicious releases were published March 31, 2026: 1.14.1 (latest) and 0.30.4 (legacy). ([0:00](https://youtu.be/5xWSezMFweE?t=0))
- Malicious axios release was discovered and deleted about three hours after publishing. ([3:31](https://youtu.be/5xWSezMFweE?t=211))
- The RAT beacons to the attacker every 60 seconds. ([1:26](https://youtu.be/5xWSezMFweE?t=86))
- Recommended minimum package age before install: 48 hours. ([3:31](https://youtu.be/5xWSezMFweE?t=211))

## Hot takes
- The title 'Millions of JS Devs Just Got Hacked' overstates the evidence: the speaker's numbers are installs and dependents, not confirmed infected machines.
- The claims 'one of the largest npm supply-chain breaches' and the North Korea link are asserted without sources in the transcript.
- The 48-hour minimum-age rule is a practical mitigation, but the speaker presents it without discussing the tradeoff against urgent security patches. The incident was caught in about three hours, so this rule would have blocked it.
- At about four minutes this is a news recap, not a technical deep dive. The detailed indicators and removal steps are deferred to a linked write-up that is not in the transcript.

## Tools mentioned
npm, npm CLI, npm ci, npm install --ignore-scripts, axios 1.14.1, axios 0.30.4, plain-crypto-js, setup.js (postinstall script), package.json, package-lock.json (lockfile), node_modules, GitHub Actions, Datadog, OpenClaw, WordPress

## Relevance to our work
- **agentos** (2/3): AgentOS is a Node-or-Python agent infrastructure project with a sandboxed execution layer. A postinstall RAT is the kind of supply-chain threat that its exec-gate and sandbox layers are meant to contain, and it applies to any project's dependency installs. → *Add a CI check that fails when any lockfile contains axios 1.14.1, axios 0.30.4 or plain-crypto-js, and make CI installs use npm ci with install scripts disabled for untrusted dependencies.*
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI and handles credentials, and the RAT's stated targets are .env files, npm tokens and SSH keys on dev workstations, so a postinstall payload in its dependency tree could read those secrets. → *Audit the ProsHarness dependency tree for the affected axios versions and plain-crypto-js, and set install-script blocking as the default for its npm installs.*
