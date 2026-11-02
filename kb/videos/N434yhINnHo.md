# The BEST Way To Use Claude Code Anywhere (Thanks To Levelsio)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `N434yhINnHo` · [watch](https://youtu.be/N434yhINnHo) · **date:** 2025-11-02 · **length:** 5:03 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack presenter (unnamed) · **orgs:** Better Stack, Hetzner, Anthropic, Levels.io
- **topics:** coding-agents, claude-code, dev-tools · **tags:** remote-server, ssh, mosh, termux, terminus, hetzner, phone-access, vibe-coding, docker-isolation, nvm

> Better Stack walkthrough for running Claude Code on a cheap always-on Hetzner server and driving it from a phone via SSH or Mosh in Terminus or Termux.

## Summary
The video shows how to run Claude Code on a remote Linux server so a coding session survives when the phone sleeps, loses battery or is lost. The presenter recommends a Hetzner server (about $4 a month) over EC2 or DigitalOcean, then installs Node via NVM and Claude Code, signs in to Anthropic, and copies over custom hooks and sub-agents. He sets up phone SSH clients: Terminus on iOS and Android, and Termux (Android only) with OpenSSH and optionally fish. He then argues plain SSH breaks when switching networks and switches to Mosh, which runs over UDP and reconnects automatically. He also suggests isolating Claude Code in a Docker container and notes home servers such as a Synology can be used with SSH firewall rules. The exact shell commands are mostly not spoken aloud, so the steps are high-level. The content is a basic setup tutorial with no sponsor and no benchmarks.

## Key ideas
- **Run Claude Code on a remote server instead of the phone** — Phones are less powerful and sleep often, so the coding session should live on an always-on server. If the phone dies or is lost, the project stays on the server. ([0:00](https://youtu.be/N434yhINnHo?t=0))
- **A cheap VPS is enough** — The presenter prefers Hetzner, at about $4 a month for an always-on server. EC2 and DigitalOcean droplets are named as alternatives. ([0:00](https://youtu.be/N434yhINnHo?t=0))
- **Bring hooks and sub-agents over during server setup** — Custom hooks and sub-agents should be copied to the server at install time, because configuring them from a phone is fiddly. ([1:18](https://youtu.be/N434yhINnHo?t=78))
- **Plain SSH breaks on network changes** — SSH uses TCP and does not roam, so switching from Wi-Fi to cellular drops the session. Mosh uses UDP, keeps the session alive and reconnects automatically. ([2:45](https://youtu.be/N434yhINnHo?t=165))
- **Isolate Claude Code in Docker** — The presenter would run Claude Code in a separate Docker container so it is isolated from the rest of the host. He defers the details to a future video. ([4:09](https://youtu.be/N434yhINnHo?t=249))
- **Terminal app choice: Terminus or Termux** — Terminus is an SSH client for iOS and Android with Mosh built in as a per-connection toggle. Termux is a full terminal on Android only, which needs Mosh installed separately. ([1:18](https://youtu.be/N434yhINnHo?t=78))

## Techniques
- **Always-on remote Claude Code host** — Create an SSH key locally and add its public key to the server. Create the server, connect, and update packages. Install Node via NVM, then install Claude Code and sign in to the Anthropic account. Copy custom hooks and sub-agents, clone the GitHub project, and check that Claude Code runs. *When:* You want to start or continue agent sessions from a phone without keeping the phone awake or connected.
- **Terminus SSH host setup (iOS/Android)** — Generate a new SSH key in Terminus, or import the private key of an existing one (it derives the public key). Create a host with an alias, the server IP and a username. Add the key. If the key is new, add its public key to authorized_keys on the server by hand, because access fails otherwise. Turn on the Mosh toggle in the connection settings for roaming. *When:* You want a simple phone SSH client, or Mosh without a manual install on the phone.
- **Termux setup (Android)** — Update packages and install OpenSSH. Optionally install fish for colours and autocomplete. Generate an SSH key, add it to the server, and connect with an ssh command. The exact command is shown on screen, not spoken. *When:* You want a full local terminal on an Android phone rather than a pure SSH client.
- **Mosh for roaming and reconnects** — Install mosh on the server and in Termux. Replace the ssh command with mosh in the connection command. On a home server with a firewall, enable the SSH firewall rules so Mosh can connect. Mosh uses UDP and needs its own server component. The exact command is shown on screen, not spoken. *When:* The phone moves between Wi-Fi and cellular, or the connection drops often.
- **Docker isolation for the agent** — Install Claude Code inside a separate Docker container on the server so it cannot touch the rest of the host. No steps are given in this video. *When:* You want the coding agent sandboxed from the rest of the server.

## Numbers
- Hetzner server for about $4 a month, always on ([0:00](https://youtu.be/N434yhINnHo?t=0))
- Termux Style is a paid app for changing fonts and themes ([4:09](https://youtu.be/N434yhINnHo?t=249))

## Hot takes
- Hetzner is better value than EC2 or DigitalOcean for an always-on agent server, because it costs about $4 a month.
- Mosh is better than plain SSH for phones because it handles Wi-Fi to cellular roaming.
- Claude Code should run in a separate Docker container on the server for isolation.
- A real terminal on the phone is preferred to a browser-based terminal such as Vibetunnel.
- Commands are not spoken in the video, so the walkthrough is thin for anyone who does not watch the screen.

## Tools mentioned
Claude Code, Hetzner, Node.js, NVM, Terminus, Termux, Termux Style, OpenSSH, fish shell, Mosh, Docker, GitHub, Vibetunnel, Kisuke, Synology, EC2, DigitalOcean

## Relevance to our work
- **prosharness** (1/3): ProsHarness drives Claude Code with phone-based approvals and long runs. This shows the basic phone-to-server-to-Claude-Code pattern and the reconnect problem that Mosh addresses. → *Check whether phone-driven approvals in ProsHarness need a roaming-tolerant transport such as Mosh, or whether checkpoint/resume already covers dropped sessions.*
