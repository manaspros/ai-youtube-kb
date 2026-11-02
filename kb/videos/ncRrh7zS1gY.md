# 300+ npm Packages COMPROMISED: The Shai-Hulud Worm Is Back!

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ncRrh7zS1gY` · [watch](https://youtu.be/ncRrh7zS1gY) · **date:** 2025-12-02 · **length:** 4:51 · **format:** news · **quality:** 3/5 · **depth:** intro
- **speakers:** Andres (Better Stack host) · **orgs:** Better Stack, npm, GitHub, Zapier, ENS, AsyncAPI, PostHog, Browserbase, Postman, Helixgard
- **topics:** security-guardrails, dev-tools · **tags:** npm, supply-chain-attack, shai-hulud, worm, secrets-leak, preinstall-script, github-actions, 2fa, dependency-pinning, credential-rotation

> Better Stack explains the Shai-Hulud npm worm, which steals developer secrets on install and republishes itself through maintainer accounts, and gives a short remediation checklist.

## Summary
A short news explainer on a second npm supply-chain worm, nicknamed Shai-Hulud, which the speaker says has hit more than 300 packages, with one vendor estimate of up to 25,000 downstream repositories. The malicious code sits in a preinstall script that runs during npm install, before installation finishes, and it harvests GitHub tokens, cloud keys, API keys and npm publish tokens. It ships the stolen secrets to an attacker-controlled GitHub repo, and in some cases flips the victim's private repos to public. The worm spreads through npm: from a machine with publish rights, it takes over every package that maintainer can reach, bumps the patch version and injects a new install script. It also drops its own GitHub workflow files to automate exfiltration. The video closes with a remediation list: rotate every secret on any machine that ran the infected package, audit package.json scripts and version bumps, remove unfamiliar workflows, enforce MFA and limit publishers on npm, and pin dependency versions.

## Key ideas
- **Second Shai-Hulud npm worm: more than 300 infected packages, and a vendor report (Helixgard, as cited in the video) estimates up to 25,000 downstream repos affected** — The video calls this a second wave, after an earlier attack on September 16, 2025. Affected packages named as examples come from Zapier, ENS, AsyncAPI, PostHog, Browserbase and Postman. The 25,000 figure is a third-party estimate the speaker relays, not something he verifies. ([0:00](https://youtu.be/ncRrh7zS1gY?t=0))
- **The payload runs on install, before npm finishes** — Malicious code sits in a preinstall script under a filename that looks like a Bun setup file. It executes as soon as npm install touches a compromised package, so being a transitive dependency is enough to be exposed. ([1:04](https://youtu.be/ncRrh7zS1gY?t=64))
- **Secrets are exfiltrated to attacker-controlled GitHub** — It scans the environment for GitHub tokens, cloud keys, API keys and npm publish tokens, then uploads them to a newly created public-looking attacker repo named Shai-Hulud. In some cases it also turns the victim's private repos public. The speaker describes this as smash-and-grab. ([1:04](https://youtu.be/ncRrh7zS1gY?t=64))
- **It is a worm that propagates through maintainer publish rights** — On a machine with npm publish permission, it pulls every package that maintainer can reach, bumps the patch version in package.json, and injects a new postinstall script. No manual step by the attacker is needed. This is why compromised maintainer credentials are the main amplifier. ([2:15](https://youtu.be/ncRrh7zS1gY?t=135))
- **The worm drops its own GitHub workflow files** — It writes unfamiliar YAML workflows under .github to automate exfiltration, so a repo can stay compromised even after the package is removed. Reviewing .github is part of cleanup. ([3:29](https://youtu.be/ncRrh7zS1gY?t=209))
- **Remediation: treat every install on an affected machine as a breach** — Rotate GitHub tokens, cloud keys, API keys and npm publish tokens, not just the one package. Audit dependencies for unexpected patch bumps from recent days, then enforce 2FA on npm, limit who can publish, and pin dependency versions. ([2:15](https://youtu.be/ncRrh7zS1gY?t=135))

## Techniques
- **Credential rotation after a malicious install** — Assume any machine that ran npm install on an infected package is compromised. Rotate GitHub tokens, cloud provider keys, third-party API keys and npm publish tokens. Do not limit it to the infected package itself. *When:* Immediately after a supply-chain advisory names a package you install, or after a suspicious install in CI or on a laptop.
- **Audit package.json for injected install scripts** — Check package.json files for preinstall and postinstall scripts you did not add yourself. Also look for patch versions that changed unexpectedly in the last few days, which is the worm's propagation signature. *When:* During incident triage, and as a recurring check on lockfile or manifest diffs in PRs that touch dependencies.
- **Inspect .github/workflows for unfamiliar YAML** — Look for workflow files you did not write under .github/workflows. Delete any unknown ones, then check the rest of the repo for other changes. *When:* After a suspected compromise, before re-enabling CI or pushing new commits.
- **Harden npm publishing** — Enforce MFA on npm accounts, restrict which accounts can publish each package, and pin dependency versions so an automatic patch bump cannot pull in new code without review. *When:* For any maintainer account or org that publishes packages, and for projects that install many third-party npm packages.

## Numbers
- More than 300 infected npm packages ([0:00](https://youtu.be/ncRrh7zS1gY?t=0))
- Possibly more than 25,000 downstream repositories affected, per a Helixgard report the speaker cites (unverified in the video) ([0:00](https://youtu.be/ncRrh7zS1gY?t=0))
- The first Shai-Hulud attack is dated September 16, 2025 in the video ([0:00](https://youtu.be/ncRrh7zS1gY?t=0))

## Hot takes
- Every npm install is a point of trust, and one maintainer account can ripple across thousands of projects.
- Compromised maintainer credentials are the strongest amplifier, so MFA and publisher limits matter more than scanning alone.

## Tools mentioned
npm, GitHub, GitHub Actions workflows (.github YAML), Bun (named only as the filename the malware imitates)

## Relevance to our work
- **agentos** (1/3): AgentOS sandboxes and governs agent code execution, and this worm shows how install-time code can exfiltrate every token an agent or CI job holds. Only tangentially relevant. → *Check that the Crucible sandbox and any Node tooling run installs without the host's GitHub, cloud and npm publish tokens in the environment.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI and handles credentials with zero-token handling, so a worm that scans the environment for tokens is a real risk to a harness that runs installs. → *Add a check that the harness and its install step do not expose npm publish, GitHub or cloud tokens to package install scripts, and flag new preinstall or postinstall scripts in dependency diffs.*
