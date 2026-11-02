# Portainer will CHANGE the way you use Docker!

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `CelLibFSDoo` · [watch](https://youtu.be/CelLibFSDoo) · **date:** 2025-11-02 · **length:** 6:21 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Better Stack presenter (not named in transcript) · **orgs:** Better Stack, Docker, AWS
- **topics:** dev-tools, observability · **tags:** docker, portainer, dockge, dozzle, yacht, docker-compose, container-management, log-viewer, self-hosting, ec2, vector, better-stack

> Quick tour of four self-hosted Docker web UIs (Portainer, Dockge, Dozzle, Yacht) with a verdict: Portainer for general container management, Dozzle for log viewing, avoid Yacht; includes a Better Stack sponsor read.

## Summary
The presenter compares four web UIs for managing Docker containers as an alternative to Docker Desktop: Portainer, Dockge (captioned as "Dockage"/"Dockch"), Dozzle and Yacht. Portainer gets the most attention, with its free Community Edition, a dashboard of containers, images, volumes and networks, container logs, stats and exec, a template library, and a browser-based Compose stack editor. The speaker notes that because it is a web UI it can run on a remote host such as an EC2 instance. Dockge is narrower: it only manages Compose stacks created inside Dockge, but its stack creation and editing is judged better than Portainer's. Dozzle is presented as a fast, open-source log viewer with merged logs across containers, regex search and log-level filtering. Yacht fails in the presenter's install: containers vanish from the dashboard and show no processes, logs or stats, so it is not recommended, though the speaker notes it is being rewritten in TypeScript. The video closes with a sponsor segment for Better Stack's hosted log management (receiving Docker logs via Vector) inside the Dozzle section. Overall it is a shallow, screen-recording tour with no benchmarks or deep configuration.

## Key ideas
- **Portainer Community Edition is a free, browser-based UI for containers: dashboard, containers, images, volumes, networks, events, templates and a Compose stack editor.** — Presenter calls it essentially a web UI for managing containers and says it is the one to reach for when you want more than log viewing. Because it is a web UI, it can be deployed on a remote machine (example given: an EC2 instance) to manage containers there. ([0:00](https://youtu.be/CelLibFSDoo?t=0))
- **Portainer's per-container tools are the practical draw: logs, stats (memory, CPU, network), exec into a container, and IP and published-port views.** — Presented as a click-through of the container detail pages. Nothing here is benchmarked; it is a feature walkthrough. ([0:00](https://youtu.be/CelLibFSDoo?t=0))
- **Portainer templates and the Compose stack editor let you deploy and edit apps from the browser without writing files locally.** — Templates provide pre-configured apps; you can create a custom template from an existing one and edit its Compose file. Stacks let you write a Compose file from scratch inside the browser. ([1:06](https://youtu.be/CelLibFSDoo?t=66))
- **Dockge is a Compose-stack manager, so it shows less than Portainer, but its stack creation and editing is judged better.** — Dockge only manages stacks created in Dockge, which the presenter lists as the main limitation. Deploy, logs, terminal, restart, stop and delete are available per stack. ([2:33](https://youtu.be/CelLibFSDoo?t=153))
- **Dozzle is a fast open-source log viewer whose standout feature is merged logs across containers in one view.** — Also offers per-container log scrolling with position percentage, memory and load display, log download, log-level toggling, Cmd+F find with regex search, and browsing host logs (on Docker Desktop). The presenter's verdict: use Dozzle to view and search logs, and Portainer when you need more. ([4:01](https://youtu.be/CelLibFSDoo?t=241))
- **The Dozzle section carries a Better Stack sponsor read: Better Stack can ingest Docker logs through Vector, with search, filtering, alerts, dashboards, metrics and status pages on a free tier.** — Sponsored content. The pitch is for hosted log management instead of self-hosting a Docker web UI. No pricing or limits are stated. ([4:01](https://youtu.be/CelLibFSDoo?t=241))
- **Yacht gives a broken experience in the presenter's install: containers disappear from the dashboard and show no processes, logs or stats, and images and volumes are empty.** — The presenter suspects a setup mistake ('skill issue') but does not confirm one. The verdict is to avoid Yacht for now and stick with Portainer, with a note that a TypeScript rewrite may fix the issues. ([5:27](https://youtu.be/CelLibFSDoo?t=327))

## Techniques
- **Run Portainer CE as a container for a web UI** — Install Community Edition with the two commands shown on screen (commands are not spoken in the transcript, so they are not reproduced here). If running locally, change the published port to 9000 as the presenter instructs. If you already have Docker Desktop, the install is said to need only those two commands. *When:* You want a browser UI over local Docker, or a remote host you want to manage from a browser.
- **Install Dockge with extra Docker Desktop directories** — Install with Docker as for Portainer. On Docker Desktop, add the extra directories the install calls for, otherwise it will not work. Stacks are created and edited inside Dockge. *When:* You mainly manage Docker Compose stacks and want a stack editor in the browser. Only stacks created in Dockge are managed.
- **Merged multi-container logs in Dozzle** — Open Dozzle to see all containers' logs in a single merged view, or pick one container and use Cmd+F with regex, log-level toggles and download. *When:* You need to search or tail logs across several containers quickly without a hosted log stack.

## Numbers
- The Portainer dashboard showed 56 images on the presenter's machine. ([0:00](https://youtu.be/CelLibFSDoo?t=0))
- Local Portainer setup uses port 9000 (presenter's instruction). ([0:00](https://youtu.be/CelLibFSDoo?t=0))
- Video length is 6:21, covering four tools at about 1.5 minutes each. ([0:00](https://youtu.be/CelLibFSDoo?t=0))

## Hot takes
- Yacht is not usable in its current state and should be avoided.
- Dockge's Compose stack creation is better than Portainer's, even though Dockge manages far less.
- Portainer is the recommended default web UI for Docker containers.
- The title ('will CHANGE the way you use Docker') overstates a shallow screen tour of four tools; the sponsor segment is inside the Dozzle section.

## Tools mentioned
Portainer (Community Edition), Docker, Docker Desktop, Docker Compose, Dockge, Dozzle, Yacht, Uptime Kuma, Nginx (sample Compose app in Dockge demo), Vector, Better Stack, AWS EC2

## Relevance to our work
- **agentos** (1/3): Container log viewing and stats for local infra work (the L3 storage stack and L4 Prometheus/Grafana stack run in containers). Dozzle is a lightweight way to check logs during load tests, but it does not replace OTel or Prometheus metrics. → *Try Dozzle locally while running the AgentOS docker stack for quick merged-log triage during load tests; keep Prometheus/Grafana for metrics.*
