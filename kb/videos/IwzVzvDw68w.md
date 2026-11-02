# Homebrew 6.0 Just Changed How Your Mac Installs Software

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `IwzVzvDw68w` · [watch](https://youtu.be/IwzVzvDw68w) · **date:** 2026-08-02 · **length:** 5:32 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Homebrew, Better Stack, Apple, GitHub
- **topics:** dev-tools, security-guardrails · **tags:** homebrew, macos, package-managers, supply-chain-security, tap-trust, ci, brew-doctor, release-notes

> Walkthrough of Homebrew 6.0, a security-focused release: third-party taps must be explicitly trusted, installs show a plan and wait for approval, and CI that relies on silent installs or untrusted taps will break.

## Summary
The host presents Homebrew 6.0 as the first major release in years, with its headline change being a security overhaul rather than new features. Previously, adding a third-party tap made Homebrew run that repo's Ruby code without any check. In 6.0, an untrusted tap is blocked until the user approves it with brew trust, while the official Homebrew taps are trusted by default. Ask mode is on by default for developers: brew shows a summary of what it will install and waits for confirmation. The release also makes the internal metadata system the default, so brew update is faster, adds brew execute (run a tool once without installing it) and brew vulns (scan installed packages against known advisories), and patches three security holes. The breaking change is for CI: brew doctor now errors on untrusted taps, and many GitHub Actions run brew doctor as their first step, so those builds fail until taps are marked trusted in config. Scripts that assumed silent installs can also hang on the new prompt. The host says Homebrew is not being rewritten in Rust, Intel Mac support is being retired over a multi-year timeline, and M5 chips are supported. The video is short and has no sponsor segment; the host gives no exact commands for the config file or non-interactive flags.

## Key ideas
- **Homebrew 6.0's main change is security, not features** — The host frames the release as a security overhaul: package managers are a major supply-chain attack target, and running any tap's code by default is a bad default. ([0:00](https://youtu.be/IwzVzvDw68w?t=0))
- **Third-party taps are blocked until explicitly trusted (tap trust)** — Previously, adding a third-party tap made brew run its Ruby code without questions. Now an untrusted tap will not run any code until the user approves it with brew trust. Official Homebrew taps are trusted out of the box, so normal install workflows are unchanged. ([0:44](https://youtu.be/IwzVzvDw68w?t=44))
- **Ask mode is on by default for developers** — Before installing packages, including their dependencies, brew shows a summary of the full plan and waits for a yes, so the user sees what will land on the machine first. ([0:44](https://youtu.be/IwzVzvDw68w?t=44))
- **Metadata is now a single download, which speeds up brew update** — The internal metadata system is the default, so package info arrives in one download instead of many small network requests. ([2:06](https://youtu.be/IwzVzvDw68w?t=126))
- **New commands: brew execute and brew vulns** — brew execute runs a tool once without permanently installing it (described as the npx equivalent). brew vulns checks installed packages against known security advisories. Six point zero also patched three security holes, one of which could run code as root through the Mac installer package. ([2:06](https://youtu.be/IwzVzvDw68w?t=126))
- **Breaking change for CI that uses third-party taps or silent installs** — brew doctor now errors on any untrusted tap. Many GitHub Actions run brew doctor as their first step, so builds fail after upgrading. The fix is to mark those taps trusted in config, which users must do themselves. Scripts that assumed silent installs may hang on the new prompt. ([3:09](https://youtu.be/IwzVzvDw68w?t=189))
- **Upgrade guidance: most people should upgrade; CI owners should prepare first** — For most users the host says yes, since 6.0 gets pulled in by brew update anyway and includes the security fixes. CI that touches third-party taps or expects silent installs should be fixed before upgrading. Intel Mac support will be retired over the next couple of years. ([4:11](https://youtu.be/IwzVzvDw68w?t=251))
- **Homebrew is not being rewritten in Rust** — The host says a Rust rewrite was an experiment and is not happening now. Development stays on the Ruby codebase. ([3:09](https://youtu.be/IwzVzvDw68w?t=189))

## Techniques
- **Explicitly trust third-party taps** — When adding a non-official tap, run brew trust for that tap before brew will execute its code. Official taps need nothing. For CI, mark the required third-party taps as trusted in config so brew doctor does not fail (the config file and key are not shown in the video). *When:* Any time you add a tap from a GitHub repo or README you do not fully control, or when upgrading CI that installs from third-party taps.
- **Review the install plan before approving** — With ask mode on by default, brew prints the full dependency list and waits for confirmation before installing. Read the plan before saying yes. Scripts that relied on silent installs must be updated to handle the prompt; the video does not show a non-interactive flag. *When:* Interactive installs on developer machines. Unattended automation must be changed first, since the prompt can block it indefinitely.
- **Run a tool once with brew execute** — Use brew execute to run a package's tool without permanently installing it onto the system. *When:* Trying a CLI you do not want to keep, or running a one-off tool without adding it to the machine's install state.
- **Scan installed packages with brew vulns** — Run brew vulns to check packages you already have installed against known security advisories. *When:* Periodic audit of a developer machine or build host after upgrading Homebrew.
- **Pre-upgrade CI audit** — Before upgrading Homebrew in CI, find pipelines that use third-party taps or GitHub Actions that run brew doctor first, then add trust configuration for those taps. Check any script that depends on non-interactive installs. *When:* Before moving CI runners or pinned workflows to Homebrew 6.0.

## Numbers
- Homebrew 6.0 patched three security holes, including one that could run code as root via the Mac installer package ([2:06](https://youtu.be/IwzVzvDw68w?t=126))
- The same three-security-fix count is repeated in the upgrade advice ([4:11](https://youtu.be/IwzVzvDw68w?t=251))
- Many standard GitHub Actions run brew doctor as their first step, which is why untrusted-tap errors break builds ([3:09](https://youtu.be/IwzVzvDw68w?t=189))
- Intel Mac support retirement timeline spans the next couple of years (no exact date given) ([4:11](https://youtu.be/IwzVzvDw68w?t=251))
- Video length is 5:32 ([0:00](https://youtu.be/IwzVzvDw68w?t=0))

## Hot takes
- Homebrew has turned from a convenience tool into a checkpoint where incoming code must prove it is trusted, and the package manager finally matches the threat model.
- The version number matters less than what came with it; the host says 6.1 and later matter less than what 6.0 introduced.
- A supply-chain attack framing: package managers are the top target right now, so running arbitrary tap code by default was a bad default.

## Tools mentioned
Homebrew 6.0, brew trust, brew execute, brew vulns, brew doctor, brew update, GitHub Actions, Ruby, npx (named as the comparison for brew execute; transcript reads 'MPX'), Nix (named as a comparison; transcript reads 'Nyx')

## Relevance to our work
- **agentos** (1/3): Tap trust and ask mode are a small, concrete example of gating installs on approval and treating third-party code as untrusted by default. This is adjacent to Crucible's sandboxing and exec-gate guardrails, not a direct change. → *When designing Crucible's package or tool install path, consider whether third-party sources need an explicit trust step and a plan-before-install prompt, similar to brew trust and ask mode.*
- **prosharness** (1/3): The plan-then-approve ask-mode pattern and the 'do not run untrusted code until approved' trust gate parallel ProsHarness's phone-driven approvals and zero-token credential handling. The idea is useful, but the video does not show agent-facing mechanisms. → *If ProsHarness ever shells out to package installs during unattended runs, add an explicit trust allowlist and a non-interactive failure mode, so a prompt cannot hang a long run.*
