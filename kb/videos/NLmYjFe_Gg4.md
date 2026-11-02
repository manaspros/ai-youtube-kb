# This Shouldn’t Be Better Than 1Password… But It Is

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `NLmYjFe_Gg4` · [watch](https://youtu.be/NLmYjFe_Gg4) · **date:** 2026-04-02 · **length:** 5:56 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Bitwarden, 1Password, NordPass, Apple
- **topics:** dev-tools, security-guardrails · **tags:** vaultwarden, bitwarden, password-manager, self-hosting, docker-compose, bitwarden-cli, secrets, macos

> Better Stack walkthrough of self-hosting Vaultwarden (a lightweight Rust Bitwarden-compatible server) via Docker Compose, connecting the Bitwarden browser extension and the Bitwarden CLI for scripted secret retrieval.

## Summary
The speaker replaces a paid password manager with Vaultwarden, a Rust reimplementation of the Bitwarden server, running on an M4 Pro Mac under Docker. The setup is one Docker Compose file with a single container, a volume and an admin token, started with docker compose up and reached on localhost port 8080. The Bitwarden Chrome extension is pointed at the self-hosted server through its environment setting, and autofill works as before. The Bitwarden CLI, installed with Homebrew, can log in, unlock and fetch a password (bw get password GitHub) so secrets can be scripted into workflows. The speaker's argument is cost, control and low resource use (under 100 MB RAM), with the trade-off that you own updates and backups. The video is short and has no benchmarks or full config file, so it is mostly a setup overview.

## Key ideas
- **Vaultwarden is a lightweight Rust reimplementation of the Bitwarden server that works with the existing Bitwarden clients.** — Speaker claims it usually uses under 100 MB RAM, versus the official Bitwarden self-host, which he calls heavier than most devs need. It supports the Bitwarden apps and extensions, end-to-end encryption, CLI access, WebAuthn and YubiKey. ([1:12](https://youtu.be/NLmYjFe_Gg4?t=72))
- **The whole server is one Docker Compose file with one container, a volume and an admin token.** — After saving the file, docker compose up starts it. The web vault is then at localhost:8080, where you create an account. The compose file itself is not shown on screen. ([1:12](https://youtu.be/NLmYjFe_Gg4?t=72))
- **Browser clients connect by switching the Bitwarden extension's environment to self-hosted.** — The extension is installed as normal. Its environment is set to self-hosted, the account is created, and the same credentials are used to log in. Autofill keeps working. ([2:29](https://youtu.be/NLmYjFe_Gg4?t=149))
- **The Bitwarden CLI makes secrets scriptable, which is the main developer use case.** — After brew install of the CLI, the sequence is bw login, bw unlock (re-enter the master password for each session), then bw get password <item>. The example fetches a GitHub login. ([2:29](https://youtu.be/NLmYjFe_Gg4?t=149))
- **The case for self-hosting is cost and control, and the cost is that you own updates and backups.** — Speaker says data stays on the machine and there are no paywalls. Downsides he names: you handle updates and backups, there is no official mobile app (the Bitwarden app is used), and SCIM is missing. He still recommends cloud Bitwarden for people who want zero maintenance. ([4:40](https://youtu.be/NLmYjFe_Gg4?t=280))

## Techniques
- **Run Vaultwarden with Docker Compose** — Write one docker-compose file with a single Vaultwarden container, one data volume and an admin token (exact keys and image tag not shown in the video), run docker compose up, then open localhost:8080 and create an account. Use the web vault to add logins and generate passwords. *When:* You want a local, free password vault that the Bitwarden clients can use without a subscription.
- **Point Bitwarden clients at a self-hosted server** — Install the normal Bitwarden browser extension, open its account/create screen, set the environment to self-hosted with the Vaultwarden URL, then log in with the same username and password used on the web vault. *When:* Moving existing Bitwarden clients (browser extension, desktop or mobile apps) onto your own server.
- **Pull credentials into scripts with the Bitwarden CLI** — brew install the Bitwarden CLI, then run bw login (email and master password), bw unlock to start a session, and bw get password <item name> to print a secret, e.g. bw get password GitHub. Capture the output inside a script or workflow instead of hard-coding it. *When:* Local scripts or dev workflows need secrets at run time without storing them in files or env exports.

## Numbers
- Vaultwarden usually runs under 100 MB of RAM (speaker's claim, not measured on screen) ([1:12](https://youtu.be/NLmYjFe_Gg4?t=72))
- Web vault served on localhost port 8080 ([1:12](https://youtu.be/NLmYjFe_Gg4?t=72))
- Video length 5:56 ([0:00](https://youtu.be/NLmYjFe_Gg4?t=0))

## Hot takes
- The title says it 'shouldn't be better than 1Password', but the case made is about cost, control and self-hosting. No feature or security comparison is shown.
- Speed is claimed ('let me show you how fast this actually is') but no timing or benchmark is shown.
- The 'costs nothing' framing leaves out the maintenance the speaker himself admits at 4:40 (updates, backups). Quality is capped at 2 because the title is hype and the setup has no config file or verification steps.

## Tools mentioned
Vaultwarden, Bitwarden (clients, browser extension, CLI, server), 1Password, NordPass, Docker, Docker Compose, Homebrew, Google Chrome, YubiKey, M4 Pro (hardware)

## Relevance to our work
- **prosharness** (1/3): Bitwarden CLI (bw unlock / bw get password) is a concrete self-hosted secret source that a zero-token credential handling flow could read from without the secret entering model context. → *Compare ProsHarness's zero-token credential path with a self-hosted vault (Vaultwarden + bw CLI) as the backing store, checking that bw unlock output never reaches the model.*
