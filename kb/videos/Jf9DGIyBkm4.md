# Postman Killer? I Didn’t Expect This (Hoppscotch)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Jf9DGIyBkm4` · [watch](https://youtu.be/Jf9DGIyBkm4) · **date:** 2026-04-02 · **length:** 5:26 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Hoppscotch, Postman, Insomnia
- **topics:** dev-tools · **tags:** api-client, postman-alternative, websocket, sse, open-source, self-hosting, local-first, pwa, collections, environments

> Better Stack's quick review of Hoppscotch, a free, open-source, browser-first API client, as a lighter alternative to Postman, with its speed and collaboration advantages and its gaps.

## Summary
The presenter tours Hoppscotch, an open-source API client that runs in the browser, works offline as a PWA, and stores data locally. The demo covers a GET request to an echo endpoint with query params and a custom header, saving to a collection, switching environments, and a WebSocket connection. He then compares it with Postman on launch time (about 10 seconds vs under a second), RAM use (about 400 MB vs a 40 MB desktop app), login and cloud dependence, free collaboration limits (3 members vs unlimited workspaces), and per-seat pricing. He also covers one-click Postman and Insomnia import, a browser extension, and a CLI for CI/CD. The downsides he names are light telemetry in the cloud version, fewer advanced features (monitoring, complex mocking), beta docs features, and a WebSocket flow that felt flaky in his demo. His verdict: a good fit for solo testers, speed-focused engineers, and small-to-medium teams, while large teams still need Postman for heavy workflows. The title oversells it, but the review is fairly balanced and light on depth.

## Key ideas
- **Browser-first, local-first design with no install needed** — Hoppscotch runs in a browser tab with zero install for basic use, works fully offline as a PWA, and stores data locally rather than in the cloud. A desktop app is also available for heavier use. ([0:00](https://youtu.be/Jf9DGIyBkm4?t=0))
- **Multi-protocol API client in one tool** — The tool covers REST, GraphQL, WebSocket, SSE and MQTT, all in the browser, without an Electron-style app. ([0:00](https://youtu.be/Jf9DGIyBkm4?t=0))
- **Free unlimited workspaces and collaborators, with self-host option** — The main contrast with Postman is unlimited free workspaces and collaborators. It can be self-hosted, or run without logging in for the lightest version. ([1:00](https://youtu.be/Jf9DGIyBkm4?t=60))
- **Speed and footprint are the headline advantage** — The presenter says Hoppscotch opens in under a second and its desktop app is about 40 MB, versus Postman at about 10 seconds to launch and roughly 400 MB of RAM. ([2:16](https://youtu.be/Jf9DGIyBkm4?t=136))
- **Low-friction migration from Postman and Insomnia** — One-click import of Postman collections (and Insomnia) lets teams move existing requests without rebuilding them. ([2:16](https://youtu.be/Jf9DGIyBkm4?t=136))
- **Honest caveats: telemetry, fewer advanced features, beta docs** — The cloud version sends light telemetry, so self-hosting or local use is the privacy option. Advanced monitoring and complex mocking are still stronger in Postman, some docs features are in beta, and the WebSocket flow was flaky in the demo. ([3:15](https://youtu.be/Jf9DGIyBkm4?t=195))
- **Verdict depends on team size and workload** — Solo testers and speed-focused engineers should switch easily. Small-to-medium teams can switch without hitting collaboration limits. Large teams may use Hoppscotch for daily work but still rely on Postman for heavy workflows. ([4:28](https://youtu.be/Jf9DGIyBkm4?t=268))

## Techniques
- **Quick REST check in the browser** — Open Hoppscotch in a browser (no install). Create a new request, set the method to GET, enter the echo endpoint URL, add query params and a custom header, then press Send. The response comes back as formatted JSON. The demo does not show the endpoint URL. Save the request to a collection. *When:* Fast smoke tests of an endpoint, or when you want to avoid installing a desktop client.
- **Environment variables for switching targets** — Create an environment variable, select that environment, and resend the saved request. The presenter describes this as the way to point the same request at different targets without editing it. *When:* Running one saved request set against several hosts, such as local, staging and prod.
- **WebSocket test** — Paste the WebSocket endpoint URL, click Connect, send a message, and watch the response stream in. The presenter noted this flow was flaky and used a URL that worked reliably for him. *When:* Checking a WebSocket or streaming endpoint without a separate tool.
- **Migrate from Postman or Insomnia** — Use the one-click import for a Postman collection (or Insomnia export) instead of rebuilding requests by hand. *When:* Moving an existing team's request library over to Hoppscotch.
- **Local, offline or self-hosted use for privacy** — Use the offline PWA or the desktop app, or self-host the instance, to avoid the cloud version's light telemetry and keep data local. *When:* When telemetry or cloud storage of API requests is a concern, or when working against localhost backends offline.
- **Use the CLI in CI/CD** — A CLI is available for CI and CD workflows. The video does not show commands or flags. *When:* Running saved collections automatically in a pipeline.

## Numbers
- Postman takes around 10 seconds to launch and uses hundreds of MB of RAM (about 400 MB stated later) ([0:00](https://youtu.be/Jf9DGIyBkm4?t=0))
- Hoppscotch opens in under a second; its desktop app is about 40 MB ([2:16](https://youtu.be/Jf9DGIyBkm4?t=136))
- Postman free tier limits collaboration to 3 members; Hoppscotch offers unlimited free workspaces and collaborators ([2:16](https://youtu.be/Jf9DGIyBkm4?t=136))
- Postman charges per seat for Teams; the presenter says Hoppscotch is free for now and claims it will stay free ([2:16](https://youtu.be/Jf9DGIyBkm4?t=136))

## Hot takes
- Title frames Hoppscotch as a Postman killer, but the presenter concludes that large teams and heavy workflows still need Postman.
- Speed and footprint claims are presenter observations with no benchmark method shown.
- Hoppscotch's free-forever pricing is described as a current claim ('at least they are right now'), not a commitment.
- Telemetry in the cloud version is a privacy trade-off the review mentions but does not dig into.

## Tools mentioned
Hoppscotch, Postman, Insomnia, Hoppscotch CLI (CI/CD), Hoppscotch browser extension, WebSocket, GraphQL, Server-Sent Events (SSE), MQTT

## Relevance to our work
- **agentos** (1/3): Could be a lightweight local client for poking AgentOS proxy endpoints, including SSE streaming, but it is a generic dev tool with no agent-specific features. → *Optional: try a local Hoppscotch or its CLI to smoke-test the Govrix proxy's OpenAI-compatible endpoints and streaming responses. Not a priority.*
