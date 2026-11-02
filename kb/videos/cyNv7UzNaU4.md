# The Fastest Way to Debug Docker Containers (Dozzle)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `cyNv7UzNaU4` · [watch](https://youtu.be/cyNv7UzNaU4) · **date:** 2026-03-02 · **length:** 4:42 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Slack
- **topics:** dev-tools, observability · **tags:** dozzle, docker, container-logs, live-logs, log-viewer, docker-compose, duckdb, webhooks, kubernetes, helm

> A short walkthrough of Dozzle, a lightweight open-source live log viewer for Docker and Kubernetes that streams container logs to the browser without storing them; v10 adds alerts, webhooks and DuckDB-based SQL queries.

## Summary
The presenter introduces Dozzle, an open-source real-time log viewer that streams Docker container logs to a browser and does not store them, which keeps the image small (about seven megabytes, as stated) and fast. Setup is a single container run that mounts the Docker socket and exposes a port, with a Docker Compose equivalent that adds a no-analytics flag; the only stated gotchas are socket permissions and running version 10 or newer. In the UI, containers are listed and can be found by partial name search, and log lines appear live as errors happen, so the user does not need to switch terminals. Version 10 is said to add a SQL mode powered by DuckDB for querying logs, alerts on conditions such as CPU above 80% with webhook delivery to Slack or another endpoint, and cloud support. The presenter says Dozzle covers Docker, Swarm, Kubernetes (via manifests or Helm) and multi-host agent setups, and is explicitly not for long-term retention or dashboards. Before exposing it beyond localhost, the video says to enable authentication with a users configuration file. The video is a product walkthrough with no sponsor segment, but it is thin on exact commands and config keys, which are not spoken clearly.

## Key ideas
- **Dozzle streams container logs live to the browser and does not store them, so there is no database or indexing to set up.** — Positioned as a lightweight alternative to heavy logging stacks; the presenter calls it tiny (about seven megabytes) and fast because it holds nothing. ([0:00](https://youtu.be/cyNv7UzNaU4?t=0))
- **Setup is one container run that mounts the Docker socket and maps a port, then open localhost in a browser.** — Compose equivalent: define a service with the image, port mapping and socket mount, pass the no-analytics flag, then run docker compose up. The presenter changed the host port because other containers already used the default. ([1:06](https://youtu.be/cyNv7UzNaU4?t=66))
- **The practical gotchas are Docker socket permissions and needing version 10 or newer for the latest features.** — The presenter describes the whole setup loop as short; no other prerequisites are mentioned. ([1:06](https://youtu.be/cyNv7UzNaU4?t=66))
- **Live search by partial container name replaces juggling terminals and rerunning docker logs.** — Typing a fragment such as DB filters to the matching container, and a failing request shows up in the browser as soon as it happens. ([2:27](https://youtu.be/cyNv7UzNaU4?t=147))
- **Version 10 adds SQL querying of logs (DuckDB), condition-based alerts and webhooks.** — Example condition: CPU usage above 80 percent, with a webhook to Slack or another endpoint. Shown only briefly, so the query syntax and alert config are not demonstrated in detail. ([2:27](https://youtu.be/cyNv7UzNaU4?t=147))
- **Dozzle is for live visibility only; long-term retention and dashboards belong to other tools.** — Because it does not store logs, it is considered more privacy-friendly, but not suitable for persistence. Enable authentication with a users config file before exposing it outside the local machine. ([3:34](https://youtu.be/cyNv7UzNaU4?t=214))

## Techniques
- **Live container log tail in the browser** — Run the Dozzle image with the Docker socket mounted and a host port mapped to its web port, then open localhost on that port. Pick a host port that does not collide with existing containers. Watch socket permissions. Use the search bar with a partial container name to filter, then click a container to stream its logs. *When:* Local or dev debugging of several containers at once, when you want to watch errors appear live instead of running docker logs in multiple terminals. Not for retention or dashboards.
- **Compose service for a live log viewer** — Add a service with the Dozzle image, map the port, mount the Docker socket, pass the no-analytics flag (exact flag and env var names are not spoken clearly in the video; check the project docs), then run docker compose up. *When:* When the containers under debug are already managed by a Compose file and you want the log viewer to live alongside them.
- **Lock down before exposing beyond localhost** — Enable authentication and supply a users configuration file, as the presenter describes. The variable name is not clearly spoken. *When:* Before publishing the Dozzle port on a shared network or server, since the socket gives access to container logs.
- **Log alerts to a webhook (v10)** — Define a condition on a container metric, such as CPU usage above 80 percent, and attach a webhook to Slack or another HTTP endpoint. *When:* When you want to be notified of a resource or error condition without watching the UI. The presenter does not show the config screen.

## Numbers
- Image or footprint described as tiny, around seven megabytes. ([0:00](https://youtu.be/cyNv7UzNaU4?t=0))
- Setup described as taking under 60 seconds. ([1:06](https://youtu.be/cyNv7UzNaU4?t=66))
- Example alert threshold: CPU usage above 80 percent. ([2:27](https://youtu.be/cyNv7UzNaU4?t=147))

## Hot takes
- The title's 'fastest way' is a setup-speed claim; the video only shows the idea of the setup and does not speak the exact command, so reproduce from the project docs rather than this video.
- Dozzle is pitched as privacy-friendly because it does not store logs. That is a property of the design, not something measured in the video.
- Sold as a replacement for terminal log-watching, but the video itself admits it is not a persistent logging or dashboard tool.

## Tools mentioned
Dozzle (v10 cited), Docker, Docker Compose, Docker Swarm, Kubernetes, Helm, DuckDB, Slack (webhook target)

## Relevance to our work
- **agentos** (1/3): AgentOS runs a multi-container self-hosted stack (Postgres, Redis, Neo4j, vLLM, Prometheus/Grafana); a live log viewer helps local debugging but does not replace OTel traces or Prometheus metrics. → *During local bring-up of the L1-L4 Docker stack, run a live container log viewer (Dozzle or similar) next to Grafana for quick error triage. Keep the Prometheus/OTel path for anything you need to keep.*
