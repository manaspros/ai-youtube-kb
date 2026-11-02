# Docker Containers - How Hackers Can ESCAPE Them in Seconds!

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `giXlSlFLKwA` · [watch](https://youtu.be/giXlSlFLKwA) · **date:** 2025-11-02 · **length:** 5:01 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Docker
- **topics:** sandboxing-execution, security-guardrails, dev-tools · **tags:** docker, container-escape, docker-socket, privileged-containers, linux-capabilities, cadvisor, vector, gvisor, seccomp, docker-bench-security, docker-socket-proxy, sandboxing

> Shows two ways to escape misconfigured Docker containers, via a mounted Docker socket and via privileged mode or CAP_SYS_ADMIN, then lists the hardening steps (proxy, drop caps, seccomp, gVisor).

## Summary
The presenter demonstrates container escape locally with Docker Desktop, using a Compose stack (Bun app, Nginx, Vector) in which Vector mounts the Docker socket to read Nginx logs. From inside Vector, they install the Docker CLI and use the socket to start a privileged container that bind-mounts the host root filesystem, which exposes host files including a .env file of fake secrets. The second demo swaps Vector for cAdvisor. With default capabilities the container is limited, but once privileged is enabled it has every capability, can recursively bind-mount the host, and can reach the Docker socket. The video's point is that the socket is the daemon's API, so mounting it gives host-level control. Mitigations offered: mount log directories instead of the socket, use a Docker socket proxy, run cAdvisor on the host or use Prometheus exporters, avoid privileged mode and add only specific capabilities, apply a seccomp profile, run gVisor for stronger isolation, and run docker-bench-security. The video also notes that SYS_ADMIN and SYS_PTRACE remain dangerous even when added individually. It is a short demo with no benchmarks.

## Key ideas
- **A container with the Docker socket mounted can control the host's Docker daemon, so it is effectively root on the host.** — Vector mounts the socket to read Nginx logs. From inside it, the presenter installs the Docker CLI and lists host containers with docker ps. The socket is the daemon's API endpoint. ([0:00](https://youtu.be/giXlSlFLKwA?t=0))
- **From a socket-enabled container, a privileged container can bind-mount the host root and read host files, including .env secrets.** — The new container runs privileged, mounts a volume with the host filesystem, and changes root into it so the attacker gets a shell with the host's files. Privileged mode disables most Docker security. ([1:19](https://youtu.be/giXlSlFLKwA?t=79))
- **Mounting the socket is a bad default. Mount only the specific log directory, or put a socket proxy in front of the daemon.** — The presenter suggests passing the Nginx log path as a volume instead of the socket. If the socket is required, use a security-hardened Docker socket proxy. ([1:19](https://youtu.be/giXlSlFLKwA?t=79))
- **Without privileged mode, cAdvisor is limited by its capability set. Privileged mode gives it all capabilities, and CAP_SYS_ADMIN is enough to bind-mount the host.** — The presenter uses capsh to compare capabilities, enables privileged mode, creates a host directory, and does a recursive bind mount of the host. They can then view containers and volumes and reach the socket. ([2:43](https://youtu.be/giXlSlFLKwA?t=163))
- **Dropping privileged mode and adding specific capabilities is still not safe. SYS_ADMIN and SYS_PTRACE remain dangerous.** — SYS_ADMIN allows changing kernel parameters and using mount. SYS_PTRACE allows injecting code into host processes. The presenter says a seccomp profile can restrict the allowed syscalls. ([4:01](https://youtu.be/giXlSlFLKwA?t=241))
- **For stronger isolation, run containers under gVisor, and run docker-bench-security to check common best practices. Running cAdvisor on the host or using Prometheus exporters avoids the risky container setup entirely.** — gVisor mediates calls before they reach the host kernel. Docker-bench-security is a script that checks for common best practices. ([4:01](https://youtu.be/giXlSlFLKwA?t=241))

## Techniques
- **Avoid mounting the Docker socket into containers** — Instead of mounting /var/run/docker.sock, bind-mount only the directory the tool needs, such as the Nginx log folder, and pass it to Vector as a volume. If the socket is unavoidable, put Docker socket proxy in front of the daemon to restrict which API calls get through. *When:* Any log, metrics, or monitoring agent that runs as a container, such as Vector or cAdvisor.
- **Audit a container's capabilities with capsh** — Open a shell in the container, install libcap tools, and run capsh to list capabilities. Missing capabilities are marked with an exclamation mark. Compare the default set against privileged mode, where every capability is granted. *When:* Checking how much a container can do before shipping it, or after a change to its run flags or Compose file.
- **Replace privileged mode with specific capabilities, then add a seccomp profile** — Remove the privileged flag and add only the capabilities the process needs. Then apply a seccomp profile with a JSON file that restricts syscalls. Keep in mind that SYS_ADMIN and SYS_PTRACE are still high risk. *When:* A container needs more than default privileges, but full privileged mode is not acceptable.
- **Run untrusted or agent-generated workloads under gVisor** — Install gVisor, which mediates system calls before they reach the host kernel. The presenter presents this as a strong isolation layer without giving configuration details. *When:* Running code you do not fully trust in containers, where a shared kernel is the main concern.
- **Check Docker hardening with docker-bench-security** — Run the docker-bench-security script on the host to check for common best-practice misconfigurations. *When:* Periodic review of a Docker host, or as a check after changing container configuration.
- **Move host-level metrics collection out of containers** — Install cAdvisor directly on the host instead of in a container, or use Prometheus with the node exporter and container exporter, so the metrics agent does not need privileged access. *When:* Collecting host and container metrics without giving a monitoring container host-level privileges.

## Numbers
- Video length is 5:01. The video gives no benchmarks, costs, latencies, or adoption stats. ([0:00](https://youtu.be/giXlSlFLKwA?t=0))

## Hot takes
- Mounting the Docker socket into a container is effectively root on the host.
- Privileged containers disable most Docker security.
- SYS_ADMIN and SYS_PTRACE are dangerous even when added one at a time, so dropping privileged mode alone is not enough.
- Stop mounting docker.sock. Mount only the log directory the tool needs.

## Tools mentioned
Docker, Docker Desktop, Docker Compose, Bun, Nginx, Vector, cAdvisor, Alpine Linux, capsh, Docker socket proxy, gVisor, docker-bench-security, Prometheus, node exporter, container exporter

## Relevance to our work
- **agentos** (2/3): AgentOS Crucible runs opt-in sandboxed code execution in containers (celld). Mounting the Docker socket or running privileged would give agent-generated code a route to the host. The video's escape paths apply directly to that setup. → *Audit the Crucible/celld container config: confirm docker.sock is never mounted, run without privileged, drop capabilities to the minimum, apply a seccomp profile, and evaluate gVisor for untrusted exec. Run docker-bench-security on the host.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, which runs shell commands and could run in containers. If it does, the same socket and privilege escalation paths apply. → *If ProsHarness ever runs Claude Code inside Docker, do not mount docker.sock, drop privileged mode, and restrict capabilities. Treat agent-run shell commands as untrusted.*
