# Dokku - Is This FREE Heroku Clone Better Than The Original?

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `J8gPLpcgUOs` · [watch](https://youtu.be/J8gPLpcgUOs) · **date:** 2025-11-02 · **length:** 5:07 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, DigitalOcean, Heroku
- **topics:** dev-tools, infra-cost-scaling · **tags:** dokku, paas, self-hosting, heroku-alternative, docker, digitalocean, postgres, nip-io, git-push-deploy, buildpacks, vhost

> Walkthrough of Dokku, a Docker-based single-server Heroku alternative: create a $6 DigitalOcean droplet, git-push deploy a Node app, add subdomain routing and a linked Postgres database.

## Summary
The video sets up Dokku, a lightweight, Docker-based platform-as-a-service that runs on one server and builds apps with Heroku buildpacks. The speaker uses the DigitalOcean marketplace image on a $6/month, 1 GB droplet, which he says is the minimum Dokku needs. He deploys a Heroku Node.js getting-started app with a git push to a Dokku remote, then enables virtual-host routing with nip.io so the app gets a subdomain on a bare IP. He links a Dokku-managed Postgres database to the app, which sets a database URL environment variable, creates a table, and checks a /db route. He closes by pointing to Docker inspection commands, zero-downtime deploys, and plugins for Redis and MongoDB. The video is a single five-minute demo: it gives no benchmarks or cost comparison with Heroku, and it does not answer the title question in a measured way.

## Key ideas
- **Dokku is a Docker-powered mini Heroku that runs on one server, so you can self-host it anywhere and skip writing YAML for apps with Postgres and Redis.** — The speaker positions it as a lighter option than Kubernetes, CapRover or Coolify, aimed at personal projects, internal tools or small production apps. ([0:00](https://youtu.be/J8gPLpcgUOs?t=0))
- **The DigitalOcean marketplace has a Dokku image, which makes setup easier than a manual Linux install.** — The speaker picks the $6/month plan with 1 GB RAM, which he says is the minimum Dokku needs, and notes that multiple or data-heavy apps need more. ([0:00](https://youtu.be/J8gPLpcgUOs?t=0))
- **Dokku installs Nginx by default, so the droplet IP shows the Nginx welcome page once Dokku is up.** — This is the check that the server is reachable before SSH setup. ([0:00](https://youtu.be/J8gPLpcgUOs?t=0))
- **Deploys are git pushes: add a Dokku remote and push main, and Dokku runs the Heroku-style build and prints the app URL.** — A Procfile in the repo is read, because Dokku uses Heroku buildpacks behind the scenes. ([1:26](https://youtu.be/J8gPLpcgUOs?t=86))
- **Bare IP addresses cannot do virtual-host subdomains, so the speaker uses nip.io wildcard DNS on the IP.** — With vhost enabled, each app gets its own subdomain. A real domain would allow Let's Encrypt certificates through a Dokku plugin, which the video does not demonstrate. ([2:53](https://youtu.be/J8gPLpcgUOs?t=173))
- **Database setup is a plugin plus a link step. Linking the Postgres service to the app grants permissions, sets credentials, and creates a database URL env var.** — The link step also makes the database start before the app when the server restarts. ([2:53](https://youtu.be/J8gPLpcgUOs?t=173))
- **Dokku apps stay inspectable with normal Docker commands, and the video claims zero-downtime deploys without showing one.** — Other plugins mentioned are Redis and MongoDB. ([4:19](https://youtu.be/J8gPLpcgUOs?t=259))

## Techniques
- **Provision a Dokku droplet from the DigitalOcean marketplace** — Create a droplet, change the region, open the Marketplace tab and search for Dokku, choose the regular size and the $6/month 1 GB plan, add an SSH key, then create the droplet. Open the IP to confirm the Nginx welcome page, then SSH in. *When:* Cheapest one-command way to get a single-server PaaS. Use it for personal or internal apps, not for workloads that need more than 1 GB RAM.
- **Create the app and deploy with git push** — On the server, run dokku apps create <name> (spoken form; the CLI command is apps:create). List apps to check. On the local machine, add a git remote that points at the server IP and app name, then run git push dokku main. Dokku builds with Heroku buildpacks and prints the URL. The app repo needs a Procfile. *When:* Heroku-style deploys from a repo that already has a Procfile, with no Dockerfile or YAML.
- **Enable subdomains on an IP with nip.io and vhost routing** — Set a base domain for Dokku. With no domain, use the droplet IP with nip.io wildcard DNS. Enable vhost for the app so it is served on <app>.<ip>.nip.io. The speaker also ran a server command to move the default port to 80, without naming it in the transcript. *When:* A test or staging host with no DNS of your own. For production, use a real domain and Dokku's Let's Encrypt plugin.
- **Add a linked Postgres database** — Install the Node Postgres client, then wire a connection and a /db endpoint that renders rows. Install the Dokku Postgres plugin, create a service, and link it to the app. Linking grants permissions, sets the username and password, and creates DATABASE_URL. Create a test table and insert a row through the Postgres CLI, then push and check /db in the browser. *When:* When an app needs a managed Postgres without writing compose files or provisioning a separate database host.
- **Inspect and debug with Docker commands** — Use standard docker ps / docker logs style commands on the server to inspect running app containers. The transcript does not show exact commands. *When:* Debugging a Dokku app that does not behave like a Heroku dyno.

## Numbers
- Cheapest recommended plan is $6/month with 1 GB RAM, described as the minimum for Dokku. ([0:00](https://youtu.be/J8gPLpcgUOs?t=0))
- Full setup of droplet, app, domain, database and deploy takes about 5 minutes of video (5:07 total). No timed benchmark or cost comparison with Heroku is shown. ([0:00](https://youtu.be/J8gPLpcgUOs?t=0))
- Zero-downtime deployment is asserted but not demonstrated. ([4:19](https://youtu.be/J8gPLpcgUOs?t=259))

## Hot takes
- The title asks whether Dokku is better than Heroku, but the video never compares cost, performance or features with Heroku. It is a setup walkthrough.
- The tutorial is basic. It sets up one app with a bare IP and nip.io, and does not show TLS, backups, scaling, or a production domain.
- Claims of zero-downtime deploys and the Heroku-like experience are stated, not tested.
- The 'subscribe to BetterStack' aside is a light self-promotion beat, not a sponsored segment.

## Tools mentioned
Dokku, Docker, Heroku buildpacks, Procfile, DigitalOcean droplet, Nginx, Let's Encrypt (Dokku plugin), nip.io, PostgreSQL, Dokku Postgres plugin, Node.js, node-postgres client, git, Redis (Dokku plugin), MongoDB (Dokku plugin)

## Relevance to our work
- **agentos** (1/3): A cheap single-VPS PaaS with a linked Postgres service could host a demo of the AgentOS API or dashboard. It does not cover GPU serving, vLLM, the Rust proxy, or any distributed-systems concern. → *Low priority: if a cheap public demo host is needed, test the AgentOS API on a Dokku droplet. Keep InferCraft (GPU) on the local RTX 5090, since a $6 droplet cannot run it.*
