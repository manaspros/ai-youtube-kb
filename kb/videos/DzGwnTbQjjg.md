# Vercel Just DESTROYED Port Numbers Forever (Portless)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `DzGwnTbQjjg` · [watch](https://youtu.be/DzGwnTbQjjg) · **date:** 2026-03-02 · **length:** 5:42 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Vercel Labs, Better Stack
- **topics:** dev-tools, coding-agents · **tags:** portless, port-conflicts, local-dev, dev-servers, reverse-proxy, vite, nextjs, parallel-agents, websockets, https-localhost

> Short walkthrough of Portless, a Vercel Labs CLI that gives dev servers stable named localhost URLs through a local proxy instead of fixed port numbers, aimed at humans and parallel AI agents.

## Summary
The video demos Portless, a Vercel Labs CLI, which replaces port numbers in local dev with stable hostnames such as name.localhost, so parallel projects and agents stop colliding on "address already in use." You start the proxy once (default port 1355), then run `portless <name> <command>`; Portless picks a random free port in the 4000-4999 range, records the name-to-port mapping in a routes JSON file, and passes the port to the app via the PORT environment variable. A browser request hits the proxy on 1355, which looks up the hostname in the routes file and forwards the request (including WebSockets) to the app's real port. The speaker shows running the proxy on port 80 with sudo to drop the port suffix, an optional HTTPS flag, and debug options (foreground proxy, run without proxy). The caveats are that non-Next.js apps like Vite must honor the PORT variable and need a host-check workaround that the speaker says allowedHosts did not solve, and Windows is not yet supported. No benchmarks; this is a single-user demo, and the video is not sponsored.

## Key ideas
- **Portless gives each dev server a stable hostname, so the port number changes behind the scenes while the URL stays the same.** — The motivating failure is the EADDRINUSE 'address is already in use' error when a forgotten background server holds a port. The pitch is that agents running in several tabs always get a predictable address. ([0:00](https://youtu.be/DzGwnTbQjjg?t=0))
- **Basic usage: `portless <name> <command>` gives a free port and a name.localhost URL.** — The speaker runs `bun run dev` under a name and gets a random free port in the 4000-4999 range, exposed at name.localhost:1355. A second project gets a different port with the same name pattern. ([1:13](https://youtu.be/DzGwnTbQjjg?t=73))
- **Moving the proxy to port 80 removes the port from the URL entirely.** — This needs sudo for both the proxy and the process. The HTTPS flag can be added on top. Vite additionally needs its port and hosts settings adjusted. ([1:13](https://youtu.be/DzGwnTbQjjg?t=73))
- **Startup path: the CLI starts the proxy if it is not running, picks a random free port, writes a routes JSON file, and sets PORT.** — Proxy ports below 1024 prompt for confirmation, and the default is 1355. The port is chosen randomly within 4000-4999 because a sequential scan would be slow when many processes are running. ([2:35](https://youtu.be/DzGwnTbQjjg?t=155))
- **Request path: the browser's DNS lookup and TCP connection go to the proxy on 1355, which maps the hostname to the app port and relays the response.** — The browser always sees a response from 1355, not the randomly assigned port. The speaker says WebSockets also work through this path. ([4:00](https://youtu.be/DzGwnTbQjjg?t=240))
- **Non-Next.js frameworks need extra setup: the app must read the PORT variable, and Vite may need a hosts setting that disables its origin check.** — The speaker says Vite rejects unrecognized origins, so the hosts key has to be set to a permissive value. He reports that the allowedHosts key with different values did not work. The exact value is not shown in the transcript. ([4:00](https://youtu.be/DzGwnTbQjjg?t=240))
- **The speaker treats the security trade-offs as acceptable for local use and expects Windows support and fixes to come later.** — Dropping the origin check and running the proxy on port 80 are presented as low-risk on a developer machine. Windows support is listed as missing. ([5:16](https://youtu.be/DzGwnTbQjjg?t=316))

## Techniques
- **Named stable dev hostnames via a local proxy** — Install Portless, start its proxy (default port 1355), then run `portless <name> <dev command>` for each project. Open http://<name>.localhost:1355. The app reads PORT from the environment, and the proxy maps <name> to that port via the routes JSON file. *When:* Several dev servers or parallel AI agents run on one machine and port collisions or forgotten background processes are a problem.
- **Portless URLs without a port suffix** — Start the proxy on port 80 with sudo and run the app through portless with sudo too. Use http://<name>.localhost. Optionally add the HTTPS flag. For Vite, also set the port key from PORT and the hosts setting as the speaker describes. *When:* You want clean URLs for demos, OAuth callback URLs, or cookie-scoped subdomains on localhost.
- **Debugging Portless itself** — Run the proxy in the foreground to watch requests. Run a command without the proxy as an escape hatch. The speaker mentions these options but does not show the flag names. *When:* Requests are not reaching the app, or you need to confirm whether the proxy or the app is at fault.
- **Making a framework respect a dynamic port** — Make the dev server read the port from the PORT environment variable, not a hard-coded number. Next.js does this out of the box per the speaker; Vite needs its config to read PORT. *When:* Any non-Next.js bundler is used with Portless.

## Numbers
- Default Portless proxy port is 1355 (the speaker says 'less' as a pun on port-less). ([1:13](https://youtu.be/DzGwnTbQjjg?t=73))
- Randomly assigned app ports fall in the 4000-4999 range. ([1:13](https://youtu.be/DzGwnTbQjjg?t=73))
- Proxy ports below 1024 prompt for confirmation before starting; higher ports start automatically. ([2:35](https://youtu.be/DzGwnTbQjjg?t=155))
- Video length is 5:42; no benchmarks or latency measurements are given. ([0:00](https://youtu.be/DzGwnTbQjjg?t=0))

## Hot takes
- Portless solves a real local collision problem, but the speaker is frank that it asks for a risky-looking setting (disabling the Vite host check) and sudo on port 80, and dismisses both as fine for local use.
- The routes file and random-port approach is a clever way to get stable URLs without changing the app's code, but the video shows only one user on one machine, so multi-agent claims are untested here.
- Quality is capped by length and depth: a short tool walkthrough with no sponsor, no benchmarks, and no comparison to alternatives such as hard-coded ports or existing proxies.

## Tools mentioned
Portless (Vercel Labs CLI), Bun (bun run dev in the demo), Vite, Next.js, Agent Browser (Vercel Labs; plugged for next video, not covered), JSON Render (Vercel Labs; named only in passing)

## Relevance to our work
- **agentos** (1/3): AgentOS's L1 proxy (Govrix Scout) is on :4000, which falls inside Portless's 4000-4999 random pool. Local stacks that run many services could collide if Portless is adopted alongside it. → *If Portless is used locally, check that its 4000-4999 pool does not overlap with Scout's :4000 or other fixed AgentOS ports, or set the pool range before running the stack.*
- **prosharness** (1/3): ProsHarness runs Claude Code in long, possibly parallel sessions that start dev servers. The video's point that agents in multiple tabs hit port collisions applies directly to its loops and schedules. → *Try having ProsHarness set PORT (or use a named Portless hostname) for each agent-started dev server, so parallel or resumed runs get predictable URLs and do not leave orphaned ports.*
