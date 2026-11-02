# The Open-Source ngrok Alternative Devs Are Switching To (Zrok)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `dLW0cT-iTjs` · [watch](https://youtu.be/dLW0cT-iTjs) · **date:** 2026-05-02 · **length:** 5:23 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, OpenZiti, NetFoundry
- **topics:** dev-tools, security-guardrails · **tags:** zrok, ngrok, localhost tunneling, private sharing, zero trust, OpenZiti, self-hosting, UDP tunneling, Cloudflare Tunnel, Tailscale, file sharing

> A 5-minute walkthrough of zrok, an open-source, self-hostable ngrok alternative that shares localhost publicly or to token-holders without port forwarding, plus its tradeoffs versus ngrok.

## Summary
The video pitches zrok as an open-source ngrok alternative built on OpenZiti's zero-trust mesh, for sharing local HTTP, TCP and UDP services without opening ports or having a public IP. The presenter runs a local Next.js app, first making it public with a one-time enable step and a single share command, then stopping it and re-sharing it privately so access is granted with a token. He also shows a drive mode that shares a directory as a browsable drive. The comparison positions zrok against ngrok (polished but a tight free tier), Cloudflare Tunnel (more setup) and Tailscale (overkill for quick shares). He is candid about the downsides: no request replay or inspection, a learning curve when self-hosting, and possible latency. Overall it is a light, practical tool intro with no benchmarks or adoption data behind the "devs are switching" framing.

## Key ideas
- **The problem is that ngrok-style tunnels force a trade-off between speed, privacy and control.** — Ngrok is polished but its free tier is tight, Cloudflare Tunnel needs extra setup, and Tailscale feels heavy for a quick share. The video says zrok aims to cover all three. ([3:12](https://youtu.be/dLW0cT-iTjs?t=192))
- **zrok shares localhost publicly over HTTPS with no port forwarding, firewall changes or public IP.** — After a one-time enable step, a single command produces a public HTTPS URL for a local app. The presenter says there is no config file. The traffic runs over a zero-trust mesh and is end-to-end encrypted. ([0:00](https://youtu.be/dLW0cT-iTjs?t=0))
- **Private sharing grants access with a token instead of opening a URL to everyone.** — The shared app is reachable only by someone who runs the access command with the issued token. The presenter argues this stops bots and random traffic from reaching the endpoint. ([1:55](https://youtu.be/dLW0cT-iTjs?t=115))
- **zrok can share a directory as a browsable drive, not just a port.** — A backend mode switch turns a share into a drive for a whole directory, which the presenter frames as controlled sharing rather than plain tunneling. ([1:55](https://youtu.be/dLW0cT-iTjs?t=115))
- **zrok covers HTTP, TCP and UDP, and presents itself as privacy-first, whereas ngrok focuses on HTTP and TCP.** — UDP support is pitched for game servers, VoIP and IoT. Private sharing is built into the core design rather than added on. The presenter cites self-hosting as the main control benefit. ([4:14](https://youtu.be/dLW0cT-iTjs?t=254))
- **The presenter names zrok's trade-offs: no request inspection or replay, a self-hosting learning curve and possible latency.** — He says ngrok still has request replay and inspection, which zrok lacks. He also says self-hosting has a learning curve and that latency may show up depending on the setup. He concludes it is worth it for quick sharing where privacy and control matter. ([4:14](https://youtu.be/dLW0cT-iTjs?t=254))

## Techniques
- **Public share of a local dev server** — Run the one-time enable step (presented as `zrok enable <token>`, its argument not shown), then run a single share command pointed at the local app (the public share subcommand is spoken, not shown on screen; the exact flags are not stated). The output is a public HTTPS URL. Stop with Ctrl-C to end the share. *When:* Quickly demoing a localhost app or webhook endpoint to someone outside your network without touching the router.
- **Token-gated private share** — Run the private share command against the local target (spoken as 'zrok share private localhost'). It prints a token instead of a public URL. The recipient runs `zrok access private <token>` to reach the app. *When:* Sharing a dev app with a specific collaborator without exposing it to bots or random traffic.
- **Share a directory as a browsable drive** — Use the share command with a drive backend mode (spoken as 'backend mode drive'; the flag name is inferred, not shown). Point it at a directory to expose it as a browsable drive, optionally behind a private token. *When:* Sending a folder of files to someone without setting up an HTTP server or a file-transfer service.

## Numbers
- Video length is 5:23 and the demo is a single default Next.js page on localhost. No benchmarks, latency figures, pricing or adoption numbers are given, despite the title's 'devs are switching' claim. ([0:00](https://youtu.be/dLW0cT-iTjs?t=0))

## Hot takes
- The title claims devs are switching to zrok, but the video offers no adoption or usage data to back that up.
- The presenter says zrok lacks request inspection and replay, which are a key ngrok feature for debugging webhooks, so the 'better fit for most devs' verdict is opinion.
- Auto-captions garbled product names (zrok, OpenZiti, ngrok). The notes restore them, and the exact command flags are inferred because they were not legible on screen.

## Tools mentioned
zrok, OpenZiti, ngrok, Cloudflare Tunnel, Tailscale, Next.js

## Relevance to our work
- **agentos** (1/3): Could expose a locally running AgentOS proxy or agent endpoint to a single collaborator for testing without a public port, but it is a dev-tool convenience, not a pillar of the system. → *Try a private zrok share on a local AgentOS proxy (:4000) to test a webhook-driven agent flow with a teammate, and check that the token-gated access holds.*
- **prosharness** (1/3): Phone-driven approvals need a reachable endpoint on the harness host. A private, token-gated tunnel is a possible alternative to a public port, but it is only a minor option. → *Evaluate whether a token-gated zrok private share can expose the local ProsHarness approval endpoint to a phone without opening a public port.*
