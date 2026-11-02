# Podman vs Docker in 2026: What's Really Different?

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `SIvoAOpXZPg` · [watch](https://youtu.be/SIvoAOpXZPg) · **date:** 2025-11-02 · **length:** 6:15 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Red Hat, Docker, Open Container Initiative, Kubernetes, OrbStack
- **topics:** dev-tools, sandboxing-execution · **tags:** podman, docker, containers, rootless, daemonless, pods, kubernetes, security, systemd, docker-swarm, podman-desktop, oci

> Better Stack's short comparison of Podman and Docker: Podman is a near drop-in, daemonless, rootless alternative with native pods; Docker wins on ecosystem, Swarm and maturity.

## Summary
The speaker introduces Podman (developed by Red Hat, OCI-compliant, with a CLI that mirrors most Docker commands and a Podman Desktop GUI) as a near drop-in replacement for Docker. The main conceptual difference he highlights is pods, which group related containers (for example nginx, PHP and MySQL for WordPress) under a shared namespace, network and security context, and which can be exported to Kubernetes YAML. The architectural contrast is the bigger point: Docker runs a root-privileged client-server daemon, while Podman is daemonless and rootless, using a fork-exec model and integrating with systemd for lifecycle management. He argues this makes Podman more secure by default and more auditable, while Docker has the more mature ecosystem, more pre-built images and tooling, and Swarm support that Podman lacks. He closes by recommending a per-priority choice, noting that Docker and Podman can coexist on one machine and that Podman Desktop can manage Docker Desktop containers. The video contains no benchmarks or commands; it is a conceptual overview.

## Key ideas
- **Podman is positioned as a near drop-in replacement for Docker** — It follows the Open Container Initiative standard, its CLI maps closely to Docker's syntax, and it supports containers, images, volumes and compose. Podman Desktop is the GUI option. ([0:00](https://youtu.be/SIvoAOpXZPg?t=0))
- **Podman pods group containers natively** — A pod shares a namespace, network and security context, so a web server, PHP and MySQL for WordPress start, stop and are managed as one unit without a full Kubernetes setup. Pod definitions can be exported to Kubernetes-compatible YAML. ([0:00](https://youtu.be/SIvoAOpXZPg?t=0))
- **Docker's root daemon is the main architectural difference** — Docker uses a client-server model with a central daemon that runs as root, so a compromised daemon or container can expose the whole host. Podman has no daemon: it uses fork-exec, so the Podman process forks and the child becomes the container. ([1:23](https://youtu.be/SIvoAOpXZPg?t=83))
- **Rootless by default is the security argument** — Containers run as a non-root user, which limits host access and makes activity traceable to a specific user for auditing. Even container root has only non-root access once outside the container. ([2:49](https://youtu.be/SIvoAOpXZPg?t=169))
- **Docker's ecosystem maturity is the main reason to stay with it** — Docker has more third-party tools, resources and pre-built images on Docker Hub. Podman has fewer pre-built images, so teams may build their own more often. Podman Desktop can reportedly run some Docker extensions. ([2:49](https://youtu.be/SIvoAOpXZPg?t=169))
- **Choice depends on priorities, and Swarm is a hard constraint** — Pick Podman for security, Kubernetes-heavy work, lightweight engines and systemd integration. Pick Docker for ecosystem breadth, team familiarity and Docker Swarm, which Podman does not support natively. ([4:10](https://youtu.be/SIvoAOpXZPg?t=250))
- **The two can coexist** — Both can be installed on one system, and Podman Desktop can manage containers running in Docker Desktop, which allows experimenting with Podman while keeping Docker workflows. ([5:25](https://youtu.be/SIvoAOpXZPg?t=325))

## Techniques
- **Group multi-container apps as Podman pods** — Put related services (for example web server, PHP-FPM and database) into one pod so they share network and namespaces and start and stop together. Export the pod definition to Kubernetes YAML when moving to a cluster. No commands are shown in the video. *When:* Local development of a multi-container stack that will later deploy to Kubernetes.
- **Run containers rootless for a smaller host blast radius** — Use Podman's default rootless mode so containers run under a normal user instead of a root daemon, which limits the damage from a container escape and ties activity to a user for auditing. *When:* Running untrusted or semi-trusted workloads, or on security-sensitive hosts.
- **Use systemd to manage container lifecycle** — Integrate Podman with systemd for starting, stopping and monitoring containers, instead of a background daemon. *When:* Long-running containers on Linux servers where systemd is already the service manager.
- **Run Docker and Podman side by side** — Install both on the same machine. Use Podman Desktop to manage running Docker Desktop containers while trying Podman workflows. *When:* Evaluating Podman without breaking an existing Docker-based workflow or team habits.

## Numbers
- No benchmarks or measured figures are given. The claimed smaller footprint and faster container startup are asserted without numbers. ([4:10](https://youtu.be/SIvoAOpXZPg?t=250))
- Example pod for a WordPress site groups three containers: a web server, PHP and MySQL. ([0:00](https://youtu.be/SIvoAOpXZPg?t=0))
- The Open Container Initiative is credited to a Docker-started effort in 2015 (speaker's statement). ([0:00](https://youtu.be/SIvoAOpXZPg?t=0))

## Hot takes
- Podman is 'inherently more secure than Docker out of the box' because of its daemonless, rootless design.
- Docker Swarm support is a deal-breaker for switching to Podman.
- Switching to Podman may require retraining, especially when new hires know Docker but not Podman.
- The video ends with a plug for an OrbStack video for Mac users who stay with Docker.

## Tools mentioned
Podman, Podman Desktop, Docker, Docker Desktop, Docker Compose, Docker Swarm, Docker Hub, Kubernetes, systemd, OrbStack, Nginx, PHP, MySQL, WordPress

## Relevance to our work
- **agentos** (1/3): Crucible runs opt-in sandboxed code execution, and rootless, daemonless containers are a possible isolation option compared with a root Docker daemon. This video is only a conceptual overview with no tests. → *When designing the L2C Crucible sandbox runtime, check whether celld can run rootless under Podman, and benchmark startup and footprint before choosing it.*
