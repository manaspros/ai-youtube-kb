# Deploying your Own Vercel in MINUTES (open-source alternative)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `pjrEaRSSQck` · [watch](https://youtu.be/pjrEaRSSQck) · **date:** 2025-11-02 · **length:** 7:27 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Appwrite, Vercel, DigitalOcean, GitHub, Better Stack
- **topics:** dev-tools, infra-cost-scaling · **tags:** appwrite, vercel, self-hosting, docker-compose, digitalocean, github-app, preview-deployments, environment-variables, deployment, baas

> A 7-minute walkthrough of self-hosting Appwrite Sites on a DigitalOcean droplet as an open-source Vercel alternative: Git deploys, branch previews, and bundled auth, database and storage.

## Summary
The speaker self-hosts Appwrite (transcribed as "AppRite") with Docker Compose on a DigitalOcean droplet and judges its Sites feature against Vercel. Setup covers creating a server account, linking GitHub through a GitHub App, and setting environment variables in a .env file. A React chat project deploys from a connected Git repo in about a minute, with a 1m10s build on the small droplet. Branch pushes produce preview deployments on random UUID subdomains behind the Appwrite login, and promotion or rollback is a single Activate click. The main gap noted is that all sites and previews share one set of environment variables, which Vercel handles per preview. The video also tours the bundled auth, database, and storage consoles. The speaker concludes the deploy experience mirrors Vercel while adding ownership and open source, and does not discuss the operational cost of running the stack.

## Key ideas
- **Appwrite Sites is pitched as an open-source Vercel; the speaker judges it on how fast and stress-free Git-to-deploy is.** — The benchmark for deployment is Vercel: minutes from Git push to live, with little friction. The speaker tests whether the self-hosted version matches that. ([0:00](https://youtu.be/pjrEaRSSQck?t=0))
- **Self-hosting is a Docker Compose stack on a VPS; the dashboard account belongs to the server, not to a cloud service.** — The speaker ran it on a DigitalOcean droplet with a purchased domain. The first sign-in creates an account on the server itself. Appwrite Cloud is the managed alternative. ([0:00](https://youtu.be/pjrEaRSSQck?t=0))
- **Git-driven deploys need a GitHub App, configured through the environment file and a compose restart.** — The speaker follows Appwrite's docs to create a GitHub App, sets the required variables in the .env file, restarts docker compose, and then can link repositories. ([1:06](https://youtu.be/pjrEaRSSQck?t=66))
- **Creating a site from a repo auto-fills framework build settings, and the first deploy takes about a minute.** — Connecting a repo asks for a production branch. Picking the React framework pre-fills install, build and output directories. The speaker sets environment variables before deploying. The first build took 1m10s on the droplet and the site got an auto-generated subdomain. ([2:20](https://youtu.be/pjrEaRSSQck?t=140))
- **Pushing a branch creates a protected preview deployment, and promoting it is a single Activate click.** — A new branch produced a deployment on a random UUID subdomain behind the Appwrite login, built in 1m7s. Activate promotes a deployment to production, which also makes rollback easy. ([3:11](https://youtu.be/pjrEaRSSQck?t=191))
- **Environment variables are global rather than per preview, which is the main gap against Vercel.** — All sites and previews share one set of variables. The speaker wants per-preview variables so a backend change can be tested beside production, then promoted together. He hopes this gets added. ([4:34](https://youtu.be/pjrEaRSSQck?t=274))
- **The same console bundles auth, database, and storage for the deployed app.** — Auth shows users, verification, MFA and OAuth providers, and needs an SMTP server for email. The database console browses and edits tables and rows. Storage lists uploaded files with permissions and delete. Functions and messaging are present but were not used. ([5:51](https://youtu.be/pjrEaRSSQck?t=351))
- **The speaker's verdict is that the Vercel-like experience comes with ownership and open source, and logging should go to a separate tool.** — He says the deploy experience mirrors Vercel and praises the status page. He would still use Better Stack for logs rather than the built-in log viewer. ([7:02](https://youtu.be/pjrEaRSSQck?t=422))

## Techniques
- **Self-host Appwrite Sites with Docker Compose** — Deploy the full Appwrite stack with docker compose on a VPS, open the dashboard by server IP or domain, and create a server admin account. The video shows no exact commands or compose file contents. *When:* When you want a self-hosted Vercel-style deploy target with bundled auth, database and storage on one box.
- **Connect Git to self-hosted Appwrite via a GitHub App** — Create a GitHub App by following Appwrite's docs, put the required GitHub app variables in the .env file, restart docker compose, then link repos from the dashboard. *When:* Before creating Git-linked sites, so pushes trigger automated builds and previews.
- **Create a site from a Git repo with framework presets** — Click Create site, choose Connect to repository, select the production branch, and pick the framework (React here). The preset fills install (npm install), build and output directory. Upload environment variables, save, then deploy. *When:* For standard SPA or framework projects where the defaults build correctly.
- **Preview-then-promote with Activate** — Push a new branch or commit so a preview deployment builds. Test it at its protected UUID URL behind the Appwrite login, then press Activate on that deployment to publish it on the main domain. Activate an older deployment to roll back. *When:* For staged verification of changes before they reach production, and for quick rollbacks.

## Numbers
- First site deploy took about a minute to succeed, with a build time of 1 minute 10 seconds on a small DigitalOcean droplet. ([2:20](https://youtu.be/pjrEaRSSQck?t=140))
- A preview deployment from a new branch finished building in 1 minute 7 seconds. ([3:11](https://youtu.be/pjrEaRSSQck?t=191))

## Hot takes
- The self-hosted deploy flow is presented as matching Vercel for Git-based deploys, but this is one repo, one branch and one deploy, so it is an anecdote and not a benchmark.
- Shared environment variables across production and previews is the real gap versus Vercel, and the speaker hopes it gets fixed.
- The video pitches ownership and open source but does not discuss the ongoing ops burden of running the stack (updates, backups, scaling).
- The speaker would send logs to Better Stack rather than use the built-in log viewer.

## Tools mentioned
Appwrite (Sites, Auth, Databases, Storage, Functions, Messaging, Appwrite Cloud), Vercel (comparison baseline), Docker Compose, DigitalOcean droplet, GitHub App, React (framework preset), npm, Better Stack (logging), .env file

## Relevance to our work
- **agentos** (1/3): AgentOS is also an opt-in, self-hosted, one-compose-file platform bundling several services. Appwrite is a close reference for the self-hosted BaaS and admin-console side, though not for agent infrastructure. → *Skim Appwrite's self-hosting and compose setup as a comparison point for how AgentOS packages opt-in services and admin UIs.*
