# Watchtower -The PERFECT Docker Automation Tool?

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `GHeZaoUpVcQ` · [watch](https://youtu.be/GHeZaoUpVcQ) · **date:** 2025-11-02 · **length:** 4:22 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Docker, Docker Hub, Slack
- **topics:** dev-tools, infra-cost-scaling · **tags:** docker, watchtower, container-updates, docker-compose, homelab, slack-notifications, monitor-only, docker-socket

> A short walkthrough of Watchtower, a Docker tool that auto-updates and restarts containers, with the host's view that it suits homelabs but not production, where monitor-only alerting is safer.

## Summary
The host introduces Watchtower, a tool that watches running Docker containers, pulls newer images when they appear, and restarts the containers. He says it is meant for homelabs, media servers and local development rather than production, and that the Docker socket should never be exposed in production. He demos a compose file with a front-end service pulled from Docker Hub and a Watchtower service in the same file, although Watchtower can run from a separate compose file since it monitors all running containers. The demo config uses a 10-second poll (the default is 24 hours), debug logging, cleanup of old images after updates, Slack notifications through a webhook, and a label that stops Watchtower from monitoring itself. After he pushes a new image, Watchtower compares the local and remote digests, pulls the image, stops and removes the old container, recreates it, and posts a Slack message. He then reports that in his own local-registry tests Watchtower found new images but could never update them, and that pulls from a remote registry sometimes failed even when they had worked before. His recommendation is monitor-only mode: Watchtower alerts in Slack and the operator updates manually.

## Key ideas
- **Watchtower automatically updates base images and restarts containers, and the host says it is designed for homelabs, media centers and local development, not production.** — He also says the Docker socket should never be exposed in a production environment. ([0:00](https://youtu.be/GHeZaoUpVcQ?t=0))
- **Watchtower does not have to live in the same compose file as the containers it watches, because it monitors all running containers on the host.** — The demo compose file has a front-end service pulled from Docker Hub and a Watchtower service next to it. ([0:00](https://youtu.be/GHeZaoUpVcQ?t=0))
- **Polling interval and scheduling are configurable; the demo uses a 10-second poll even though the default is 24 hours.** — A cron-style schedule is offered as an alternative to a fixed interval. ([0:00](https://youtu.be/GHeZaoUpVcQ?t=0))
- **The demo config turns on debug logging, removes old images after updating, sends Slack notifications via a webhook, and labels the Watchtower container so it does not monitor itself.** — Containers can be scoped by passing names in the command, and the env-var settings could equally be written as command flags, which he finds less readable. ([1:24](https://youtu.be/GHeZaoUpVcQ?t=84))
- **Update mechanics: Watchtower compares the local image digest with the remote digest, and pulls, stops, removes and recreates the container only when they differ.** — After a rebuild and push of the front-end image, the sequence in the demo was: find image, check for pull, check credentials, compare digests, pull, stop, remove, create, start, then notify Slack. ([2:23](https://youtu.be/GHeZaoUpVcQ?t=143))
- **His local-registry tests showed Watchtower detecting new images but failing to update them, and remote pulls sometimes broke even when they had worked before.** — He could not identify the missing information in the container message, so he would not use auto-stop-and-pull in production. ([2:23](https://youtu.be/GHeZaoUpVcQ?t=143))
- **Recommended mode for anything important is monitor-only: Watchtower alerts on new images and the operator decides when to update.** — He presents this as his own choice and notes that other tools also do monitoring-only update alerts. ([3:47](https://youtu.be/GHeZaoUpVcQ?t=227))

## Techniques
- **Watchtower as a sidecar compose service** — Add a watchtower service to a compose file on the host (it can also live in a separate compose file). It discovers all running containers by itself. Set the poll interval (demo 10s, default 24h) or use a cron-style schedule, and enable debug logging, old-image cleanup and Slack webhook notifications. The video does not spell out the exact environment variable names, only that the same settings can be passed as command flags. *When:* Homelab, media-server or local dev stacks where you want images kept current without manual restarts.
- **Excluding Watchtower from itself** — Put Watchtower's self-exclusion label on its own container so it does not update itself. The same label works on any container you want to skip. Alternatively, pass container names in the Watchtower command to limit what it monitors (opt-in scope). *When:* When some containers must be pinned or updated by hand, or when you want Watchtower to watch only a subset of the host.
- **Monitor-only mode with Slack alerts** — Run Watchtower so it only checks for newer images and sends a notification, without pulling or restarting. The operator then updates each chosen image manually. The video does not give the flag name. *When:* Production or any service where an unattended restart is risky. This is the mode the host recommends.
- **Digest-based change detection** — Watchtower compares the digest of the locally running image with the digest of the remote tag. It pulls and recreates the container only when the digests differ, so an unchanged tag causes no restart. *When:* To understand why a rebuilt and pushed tag triggers a restart, or when debugging unexpected updates.

## Numbers
- Demo Watchtower poll interval is 10 seconds; the default is 24 hours. ([0:00](https://youtu.be/GHeZaoUpVcQ?t=0))
- Video length is 4:22. ([0:00](https://youtu.be/GHeZaoUpVcQ?t=0))
- Watchtower's pull-and-recreate cycle is shown as a sequence of log steps: find image, check pull, check credentials, compare digests, pull, stop, remove, create, start, notify. ([2:23](https://youtu.be/GHeZaoUpVcQ?t=143))

## Hot takes
- Watchtower is designed not to be used in production, though it suits homelabs, media centers and local development.
- The Docker socket should never be exposed in a production environment.
- He would not use Watchtower to stop containers and pull images automatically; he would run it in monitor-only mode.
- Auto-updates failed in his local-registry tests even though Watchtower found the new images.
- The video is a thin, short walkthrough with a personal opinion; there are no benchmarks or detailed failure analysis.

## Tools mentioned
Watchtower, Docker, Docker Compose, Docker Hub, Slack (webhook notifications)

## Relevance to our work
- **agentos** (1/3): AgentOS is self-hosted infra that may run in Docker containers on one box; the auto-update risk is the one useful point here, but there is no direct link to the pillars. → *If AgentOS services run as Docker containers, check that none mount the Docker socket and that image updates are alert-only (monitor mode) rather than automatic restarts.*
