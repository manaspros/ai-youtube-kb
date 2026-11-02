# Cloudflare Just Killed Mac Minis? OpenClaw Runs Serverless – Here's How!

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `DQdYE02TkIQ` · [watch](https://youtu.be/DQdYE02TkIQ) · **date:** 2026-03-02 · **length:** 9:31 · **format:** tutorial · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Unnamed Better Stack presenter · **orgs:** Cloudflare, Better Stack, Anthropic, OpenAI, Hetzner, Tailscale
- **topics:** sandboxing-execution, agent-architecture, infra-cost-scaling · **tags:** openclaw, cloudflare-workers, cloudflare-sandbox, browser-rendering, r2, durable-objects, cloudflare-access, wrangler, serverless-agents, self-hosted-agents, sponsored

> Walkthrough of running the OpenClaw agent gateway serverlessly on Cloudflare Workers, Sandboxes, Browser Rendering and R2, with setup steps and a serverless-versus-VPS verdict. Ends with a Better Stack sponsor read.

## Summary
The video shows OpenClaw (captions say "Clawdbot" or "MaltBot") running on Cloudflare: a Worker fronts an admin UI and auth, the gateway runs inside a Cloudflare Sandbox (a Docker container), headless Chromium comes from Browser Rendering, and R2 holds persistent config and sessions. Authentication goes through Cloudflare Access, with JWTs validated in the Worker. The presenter walks through prerequisites (paid Workers plan, local Docker, an Anthropic or OpenAI key), the bindings that must exist after deploy, the two Access secrets that must be set in Wrangler, and how to clear a stale sandbox container before redeploying. Device pairing and the gateway token come last. The key caveat is that anything saved inside the sandbox is wiped on rebuild, so state must go to R2. The presenter concludes that serverless suits people who want less ops, while a VPS or Mac mini with Ollama suits anyone who wants flexibility and privacy. The last ~1.5 minutes are a Better Stack sponsor segment.

## Key ideas
- **OpenClaw can run on Cloudflare with no server to manage: Workers, Sandboxes, Browser Rendering and R2 together, billed by compute used.** — The presenter demos a live instance that answers questions about its own infrastructure. Channels (WhatsApp, Telegram, Discord, Slack), skills, config, debug and logs are all reachable from the admin UI. ([0:00](https://youtu.be/DQdYE02TkIQ?t=0))
- **Architecture is three layers: Cloudflare Access for login, a Worker (Hono routes plus JWT validation) for admin, and a sandboxed gateway container.** — The Worker serves admin routes and uses the Chrome DevTools Protocol to drive Cloudflare's headless Chromium for browsing. The gateway itself runs in a Docker-based sandbox, which isolates agent code execution. ([1:00](https://youtu.be/DQdYE02TkIQ?t=60))
- **The gateway is the 'brains' of OpenClaw (dashboard, WebSocket for nodes and clients, agent runtime, session and channel managers), listening on port 18789.** — On Cloudflare this whole gateway sits inside the sandbox rather than on a host. Model access is either your own OpenAI or Anthropic key or Cloudflare AI Gateway. Local LLMs are not possible in this setup. ([2:23](https://youtu.be/DQdYE02TkIQ?t=143))
- **Sandbox disk is ephemeral. Restarting or rebuilding the container wipes it, so session management and config go into an R2 bucket.** — This is the main design constraint of the serverless option: anything that must survive a redeploy has to be written to object storage. ([3:48](https://youtu.be/DQdYE02TkIQ?t=228))
- **Setup has several non-obvious post-deploy steps spread across the README: bindings check, enabling Access, two Wrangler secrets, and removing a stale sandbox container.** — The presenter says the steps are hard to find because they are scattered. The Deploy-to-Cloudflare button did not work for him, so he recommends cloning the repo. ([5:07](https://youtu.be/DQdYE02TkIQ?t=307))
- **First access requires approving a pending device pairing in the admin page, and the gateway token is passed as a query param on first browser access.** — Once paired and healthy, the bot can be reached from Slack, which the Cloudflare team wired up in the README's examples. ([6:31](https://youtu.be/DQdYE02TkIQ?t=391))
- **The verdict favors a VPS or Mac mini over serverless for people who can run a server. Serverless gives Cloudflare-managed security and less ops, but a VPS gives flexibility, privacy and local models through Ollama.** — The presenter's own recommendation is a VPS set up over Tailscale, which he covers in an earlier video. He also notes the GitHub repo still shows the old Clawdbot logo. ([7:40](https://youtu.be/DQdYE02TkIQ?t=460))

## Techniques
- **Prerequisites checklist before deploying OpenClaw on Cloudflare** — Have a paid Workers plan (about $5/month plus usage), a local Docker runtime (Docker Desktop, or OrbStack, auto-captioned 'Kolyma'), and an Anthropic or OpenAI API key. Clone the OpenClaw-on-Cloudflare GitHub repo (name not spoken in the video) and follow its README. Save the MoltBot/OpenClaw gateway token somewhere safe. *When:* Starting a fresh serverless OpenClaw deployment.
- **Verify Durable Object, R2 and browser bindings after deploy** — In the Worker's binding section, confirm there is a Durable Object for the sandbox, an R2 bucket, and a browser renderer binding. If any are missing, rebuild the Docker image and deploy again. *When:* Right after the first wrangler deploy, before wiring auth.
- **Enable Cloudflare Access and set two Wrangler secrets** — Open the Worker's Domains and Routes, then enable Cloudflare Access. The first time, a setup pop-up appears. Copy the Access AUD tag from the Access application settings and the Access team domain from the account settings, and store both as Wrangler secrets (the captions say 'cfaccess.aud' and 'cfaccess.teen domain'; the exact secret names are in the repo README). Then run deploy again. *When:* Before the gateway admin page will load for the first time.
- **Clear a stale sandbox container before redeploying** — List the existing containers with the Wrangler container listing command (not shown on screen), note the ID of the old container, and delete it with 'delete <ID>'. Then redeploy to create the new one. *When:* Redeploying when a sandbox container from an earlier deploy already exists. The presenter says this is the cause of the conflict error.
- **Pair the device and authenticate the browser** — Open the admin page. Approve the pending pairing request shown on it. On the first browser visit, open the worker URL with the gateway token added as a query parameter. After that, the health check should read OK. *When:* First access after deployment, and again for each new browser.
- **Persist state in R2, not the sandbox disk** — Store session management data and configuration in the attached R2 bucket. Assume anything written inside the sandbox is lost on restart or rebuild. *When:* Designing any sandboxed agent that must keep state across restarts or redeploys.

## Numbers
- Cloudflare Workers paid plan costs about $5/month, plus additional usage. ([3:48](https://youtu.be/DQdYE02TkIQ?t=228))
- OpenClaw gateway listens on port 18789 for WebSocket and HTTP channel traffic. ([2:23](https://youtu.be/DQdYE02TkIQ?t=143))
- A Hetzner VPS is cheaper than the Cloudflare setup, per the presenter's own comparison. ([3:48](https://youtu.be/DQdYE02TkIQ?t=228))
- The video runs 9:31 in total, and the sponsor segment starts at about 9:00. ([9:00](https://youtu.be/DQdYE02TkIQ?t=540))

## Hot takes
- Serverless OpenClaw is good for people who do not want to manage a server, but a VPS or Mac mini is more secure and flexible in the long run for people who can handle it.
- The Deploy-to-Cloudflare button did not work for the presenter, and the setup steps are scattered across the README.
- Persistence on sandboxes is a real trap: restarts and rebuilds wipe local state, so R2 is required.
- Ends with a Better Stack sponsor read (about 9:00 to 9:31), which caps quality at 2 under the rubric.

## Tools mentioned
OpenClaw (captioned as Clawdbot / MoltBot / MaltBot), Cloudflare Workers, Cloudflare Sandboxes (Docker-based), Cloudflare Browser Rendering (headless Chromium), Cloudflare R2, Cloudflare Durable Objects, Cloudflare Access, Cloudflare AI Gateway, Wrangler, Hono, Chrome DevTools Protocol, Docker, Docker Desktop, OrbStack (auto-captioned 'Kolyma'), Ollama, Tailscale, Telegram, WhatsApp, Discord, Slack

## Relevance to our work
- **agentos** (1/3): Crucible runs sandboxed execution with a Cloudflare backend, and this video shows the sandbox-persistence trap (wiped on rebuild) that would apply there. → *Document which Crucible/celld state survives a container rebuild and keep session and config state in external object storage, following the R2 pattern shown at 3:48.*
- **prosharness** (1/3): ProsHarness does checkpoint/resume of long Claude Code runs, which fails if checkpoints live on sandbox-local disk. → *Write ProsHarness checkpoints to durable external storage, not container-local files, and add a test that a container rebuild still allows resume.*
