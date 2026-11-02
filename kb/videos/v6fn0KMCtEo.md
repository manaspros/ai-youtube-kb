# I Replaced Vercel with Dokploy

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `v6fn0KMCtEo` · [watch](https://youtu.be/v6fn0KMCtEo) · **date:** 2026-04-02 · **length:** 4:15 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed) · **orgs:** Better Stack, Dokploy, Hetzner, Vercel, Railway, Heroku, Coolify
- **topics:** dev-tools, infra-cost-scaling · **tags:** dokploy, self-hosting, vps, docker, traefik, docker-swarm, paas, deployment, cost, hetzner, nextjs, coolify

> Better Stack's 4-minute walkthrough of Dokploy, a self-hosted, Docker-native PaaS that turns a rented VPS into a Vercel/Heroku-style deploy target with HTTPS, logs, rollback and optional Swarm scaling.

## Summary
The host argues that Vercel, Railway and Heroku get expensive as usage grows, and proposes running a similar push-to-deploy workflow on a cheap VPS using Dokploy. Dokploy is described as Docker-native with Traefik underneath, installed with one command, and driven from a web UI. The demo uses a Hetzner VPS and a simple Next.js app connected from GitHub: the deploy finishes in under 30 seconds, HTTPS works once a domain is added, and logs, metrics, one-click rollback and redeploy-on-push are shown. The host positions Dokploy against Coolify (lighter UI, built-in Swarm) and against managed platforms (no usage fees, can run non-static and multi-service apps). Downsides acknowledged are a newer project with fewer docs, some volume quirks, and a mix of open-source and paid features where the core is free. The verdict is that it suits solo devs and small teams who want Vercel-style simplicity on their own hardware. The video shows no exact install command or config, so it is a product overview rather than a reproducible tutorial.

## Key ideas
- **Managed PaaS costs climb quickly with usage, and the pitch is to keep a similar deploy experience on a cheap VPS you already own.** — Cites Vercel, Railway and Heroku bills rising from tens to hundreds of dollars. Dokploy is presented as the middle ground between expensive managed clouds and hand-wired Docker. ([0:00](https://youtu.be/v6fn0KMCtEo?t=0))
- **Dokploy is a Docker-native layer over Docker and Traefik; the workflow is what it adds.** — Install is a single command on the VPS. Then you create a project, connect a GitHub repo, and deploy. Built-in databases, automatic backups, real-time monitoring, Docker Compose support and Docker Swarm are listed as included. ([0:00](https://youtu.be/v6fn0KMCtEo?t=0))
- **End-to-end demo: a simple Next.js app goes live in under 30 seconds with HTTPS, logs, metrics and one-click rollback.** — Setup used a Hetzner VPS. After adding a domain, HTTPS was working with no extra steps. A minor code change pushed to the repo redeployed cleanly. ([1:28](https://youtu.be/v6fn0KMCtEo?t=88))
- **Because it is Docker-native, existing stacks deploy as they are instead of being rewritten.** — The host says this is the main reason the tool fits without changing the app. Multi-service stacks and APIs are mentioned alongside Next.js and Python. ([2:28](https://youtu.be/v6fn0KMCtEo?t=148))
- **Claimed advantages over alternatives: no usage fees compared with managed platforms, a lighter and cleaner UI than Coolify, and built-in Swarm for multi-server scaling.** — These are the host's comparative claims, made without benchmarks or a side-by-side test. ([3:15](https://youtu.be/v6fn0KMCtEo?t=195))
- **Honest downsides: a newer project with fewer docs, volume quirks, and a mix of open-source and paid features, though the core is free.** — The host judges the downsides small relative to the features. No details are given on which volume issues or paid features are meant. ([2:28](https://youtu.be/v6fn0KMCtEo?t=148))
- **Best fit is a solo dev or small team trying to cut cloud bills without becoming a DevOps engineer.** — Skip it if you need a large template ecosystem or do not want to self-host at all. Hetzner's price increase is mentioned as a caveat on the VPS cost. ([3:15](https://youtu.be/v6fn0KMCtEo?t=195))

## Techniques
- **Self-hosted push-to-deploy on a cheap VPS** — Rent a VPS (the host used Hetzner). Install Dokploy with the single install command from its docs (the command is not shown on screen). Log in, create a project, connect the GitHub repo, and hit deploy. Add a domain to get HTTPS. Redeploy by pushing to the connected repo. Roll back from the UI. *When:* Solo devs or small teams running Next.js, Python APIs or multi-service Docker stacks who want Vercel-style deploys without per-usage platform fees.
- **Docker Swarm for multi-server scaling via Dokploy** — Swarm is built into Dokploy. The host says scaling across servers is simpler than expected, but gives no steps or config. *When:* When a single VPS is no longer enough and you want multi-node Docker without adopting Kubernetes.
- **Built-in ops bundle instead of extra tools** — Use the platform's own logs, real-time metrics, automatic backups and built-in databases rather than wiring separate monitoring and backup tools. *When:* When you want fewer moving parts in production and the platform's metrics and backups are good enough for your needs.

## Numbers
- Managed platform bills can climb from about $50 to $100, sometimes more, as usage grows (host's description, not a measurement). ([0:00](https://youtu.be/v6fn0KMCtEo?t=0))
- Dokploy setup suggested on a $5 VPS (host's estimate). ([0:00](https://youtu.be/v6fn0KMCtEo?t=0))
- The Next.js app deploy from connect to live, with HTTPS, took under 30 seconds. ([1:28](https://youtu.be/v6fn0KMCtEo?t=88))
- Some users report among the fastest deploys they have seen, especially incremental ones (secondhand claim, no numbers). ([2:28](https://youtu.be/v6fn0KMCtEo?t=148))

## Hot takes
- Dokploy is a better fit than Coolify for most small teams because its UI is cleaner and Swarm is built in.
- Self-hosting on a VPS is a smart middle ground for most devs, not only for people who enjoy DevOps.
- Vercel-style simplicity on your own hardware is the main value, with no lock-in.

## Tools mentioned
Dokploy, Docker, Docker Compose, Docker Swarm, Traefik, Hetzner VPS, GitHub, Next.js, Vercel, Railway, Heroku, Coolify

## Relevance to our work
- **agentos** (1/3): AgentOS is self-hosted infrastructure on one RTX 5090 box, so a self-hosted PaaS is only tangentially related to its pillars. Dokploy is not a serving, gateway or storage layer. → *Low priority: when deciding how to deploy AgentOS demo services, compare Dokploy with Coolify on Docker Swarm support and built-in metrics. No change to core pillars.*
