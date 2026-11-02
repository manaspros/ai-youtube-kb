# The BEST way to use Docker on MacOS

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `raUJQms00xY` · [watch](https://youtu.be/raUJQms00xY) · **date:** 2025-11-02 · **length:** 9:39 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, OrbStack, Docker, Grafana Labs
- **topics:** dev-tools · **tags:** docker, macos, orbstack, docker-desktop, containers, kubernetes, linux-vm, debugging, local-dev, file-sharing

> Walkthrough of OrbStack as a macOS replacement for Docker Desktop: faster startup, automatic .orb.local domains with HTTPS, a debug shell for distroless containers, Finder file access, a local Kubernetes cluster, and Linux VMs.

## Summary
The host presents OrbStack as a drop-in replacement for Docker Desktop on macOS, bundling the Docker engine, CLI, Compose and some third-party tools that it keeps updated with the app. He claims it provisions a dev machine 2.6x faster, builds images 2.7x faster, and uses 1.5-4x less power and CPU than Docker Desktop, and shows a startup race on his own machine. Most of the video is a feature tour: each container gets a name.project.orb.local domain with automatic HTTPS and port detection, and a debug shell adds tools to containers that have no shell. Containers' files are browsable and editable from Finder, the bundled single-node Kubernetes cluster skips registry pushes and exposes services on the Mac, and lightweight Linux VMs share files with macOS. The video is a demo with no commands for the Docker side, and the benchmark numbers come with no method or hardware details.

## Key ideas
- **OrbStack is positioned as a drop-in Docker Desktop replacement that bundles the Docker engine, CLI, Compose and third-party tools, and keeps them updated while the app is updated.** — Installed as a Mac app or via Homebrew (the Homebrew command is not shown on screen). No Docker-side commands are demonstrated. ([0:00](https://youtu.be/raUJQms00xY?t=0))
- **Performance is the headline claim: faster provisioning, faster image builds, and lower power and CPU use than Docker Desktop, plus a visibly faster startup race.** — Speaker-cited benchmark figures, with no methodology, hardware or workload described. Treat as vendor-style claims until reproduced. ([1:07](https://youtu.be/raUJQms00xY?t=67))
- **Every container gets an automatic name.project.orb.local domain, web ports are detected automatically, and HTTPS (certificate generation, installation, reverse proxy) is handled with no setup.** — Example uses an OpenTelemetry demo project: the frontend proxy's website on 8080 and Grafana on 10000 are served at project-based domains without port numbers. Non-web services such as Postgres or Redis still use port numbers. Custom domains and wildcards are supported. An index page at orb.local lists services. ([1:58](https://youtu.be/raUJQms00xY?t=118))
- **A debug shell lets you inspect minimal or distroless containers that have no shell, and packages installed in it do not modify the containers.** — The debug shell ships with htop, curl, strace, nano and vim, and a package manager with 80,000+ packages. Installed packages are visible across all containers, so this also works with read-only containers. ([3:20](https://youtu.be/raUJQms00xY?t=200))
- **Container files are exposed as a macOS Finder folder, so any Mac app can edit a file inside a running container.** — Finder shows an OrbStack location with Docker containers, images and volumes. The demo replaces a banner image by editing it in Preview, then refreshing the page shows the change. The same approach is suggested for VS Code and terminal workflows. ([4:21](https://youtu.be/raUJQms00xY?t=261))
- **The bundled single-node Kubernetes cluster removes local registry pushes and port forwarding, with services reachable directly from the Mac.** — Locally built images are usable by pods immediately. LoadBalancer, NodePort and ClusterIP services are reachable from macOS, with service-name domains like k8s.orb.local and cluster.local domains working. Pod IPs are reachable for debugging. kubectl is included. The cluster is started and stopped with orbstart k8 / orbstop k8 commands (spelled as in the captions). ([6:44](https://youtu.be/raUJQms00xY?t=404))
- **Lightweight Linux VMs run alongside containers, share files both ways with macOS, and behave like a normal Ubuntu machine.** — An Ubuntu VM is created from the UI and entered with the orb CLI. macOS files are visible inside it and vice versa. Packages install with sudo apt install (nginx shown), and services start the usual Linux way. ([7:42](https://youtu.be/raUJQms00xY?t=462))

## Techniques
- **Debugging distroless or read-only containers with the OrbStack debug shell** — In the OrbStack UI, open a container and click Debug to get a shell with tools such as curl, htop, strace, vim and nano. Install extra tools (e.g. neovim) through its package manager. Installs are not written into the container, and they apply across all containers. *When:* When a minimal, distroless or read-only image has no shell or utilities and you need to inspect processes, network or files without rebuilding the image.
- **Editing container files from macOS in place** — Open Finder, go to the OrbStack location, and navigate to Docker, then containers, images or volumes. Open the file in any Mac app (the demo used Preview), save, and refresh the page to see the change in the running container. *When:* For quick edits, such as swapping a static asset during local development, without copying files in with docker cp or rebuilding.
- **Using automatic container domains instead of port mapping** — Reach web containers at <container>.<project>.orb.local (HTTPS is automatic). Use the orb.local index page to find services. Keep port numbers for non-web services such as Postgres or Redis, and set custom domains or wildcards if needed. *When:* For local multi-service setups where remembering port numbers is error-prone, such as the OpenTelemetry demo stack shown in the video.
- **Local Kubernetes without a registry push** — Enable the bundled single-node cluster, build images locally, and reference them in pod specs directly; they are immediately available. Reach services at service-name domains such as <service>.k8s.orb.local, or connect to pod IPs for debugging. Use kubectl as normal. *When:* For fast inner-loop development on a Mac against a cluster, avoiding a local registry and port-forward steps.
- **Running a Linux VM alongside macOS dev tools** — Create a distro (Ubuntu shown) in the UI, enter it with the orb command, then install and run services with the normal Linux commands (sudo apt install nginx). Access the shared macOS files through the OrbStack folder in Finder. *When:* When you need a real Linux userland on a Mac, for example to test install scripts or Linux-only services, without a heavy VM.

## Numbers
- OrbStack provisions a dev machine 2.6x faster than Docker Desktop (speaker-cited benchmark). ([1:07](https://youtu.be/raUJQms00xY?t=67))
- OrbStack builds images 2.7x faster than Docker Desktop (speaker-cited benchmark). ([1:07](https://youtu.be/raUJQms00xY?t=67))
- OrbStack uses between 1.5x and 4x less power and CPU than Docker Desktop (speaker-cited benchmark). ([1:07](https://youtu.be/raUJQms00xY?t=67))
- The debug shell package manager gives access to over 80,000 packages. ([3:20](https://youtu.be/raUJQms00xY?t=200))
- The OpenTelemetry demo example exposes a website on port 8080 and Grafana on port 10000, each reachable at a project domain without a port number. ([1:58](https://youtu.be/raUJQms00xY?t=118))

## Hot takes
- The benchmark multipliers (2.6x, 2.7x, 1.5-4x) are the speaker's figures with no methodology, hardware or workload shown, and the only comparison is a single live startup race.
- Mostly a feature tour with product-enthusiastic framing ('awesome drop-in replacement', 'changes the way you debug'), and no sponsorship disclosure appears in the transcript.
- The video does not cover any downsides, Docker Desktop features OrbStack may lack, licensing, or how well 'drop-in' holds for real Compose projects.
- macOS-only: the features (Finder integration, Mac-side domains, Mac-to-VM file sharing) have no equivalent on the Linux machines this team works on.

## Tools mentioned
OrbStack, Docker Desktop, Docker Engine, Docker CLI, Docker Compose, Kubernetes, kubectl, Homebrew, Ubuntu, nginx, Finder, Preview, Neovim, vim, nano, htop, curl, strace, Grafana, Valkey, Postgres, Redis, OpenTelemetry demo, VS Code

## Relevance to our work
- **general** (1/3): Only useful if local dev moves to a Mac; the Docker-on-macOS workflow is otherwise unrelated to current work. → *If a Mac becomes a dev machine, compare OrbStack with Docker Desktop on container startup and build time before adopting it.*
