# Your Own Mini AWS in Under 30 Minutes (Incus Tutorial)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `zaAtYkM24hU` · [watch](https://youtu.be/zaAtYkM24hU) · **date:** 2025-11-02 · **length:** 8:00 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** Andrus (Better Stack presenter, as named in the outro; captions spell it 'Andrus') · **orgs:** Better Stack, Canonical, Zabbly, Ollama, Ubuntu
- **topics:** dev-tools, sandboxing-execution, local-ai · **tags:** incus, lxd, system-containers, virtual-machines, linux, ubuntu, multi-tenant, resource-quotas, ollama, self-hosting, bridge-networking, apt-repo, home-lab

> Better Stack walkthrough of installing Incus (a community fork of LXD) on Ubuntu to run system containers and VMs, host Ollama in a container, and set up per-customer projects with quotas.

## Summary
Better Stack presents Incus as a single interface for system containers and virtual machines on Linux, described as a community-driven fork of Canonical's LXD that builds on LXC and QEMU. The walkthrough installs Incus on a fresh Ubuntu VM by adding the Zabbly apt repo with its GPG key, then runs `incus admin init` with default answers and launches an Ubuntu container. It notes that VMs need bare metal or nested virtualization, which the Mac-hosted VM did not support. The presenter then creates a bridge network (incusbr0), attaches it to the default profile, and restarts the container so curl and Ollama can install and reach the network. An Ollama container runs a tiny model (orca-mini) as a test, with weak jokes as the output. The final section creates an Incus project per imaginary customer, switches into it, and applies CPU and memory limits as a basis for multi-tenant isolation. The exact command flags are only partly spoken in the captions, so the steps should be checked against Incus's own install docs.

## Key ideas
- **Incus is a community fork of Canonical's LXD that manages both system containers and VMs through one CLI, and it runs only on Linux.** — The presenter says it builds on LXC for containers and QEMU for VMs, so LXD users will find it familiar. Containers share the host kernel, while VMs get their own kernel. ([1:20](https://youtu.be/zaAtYkM24hU?t=80))
- **Installing Incus on Ubuntu is fiddly (signed apt repo setup), but first-run use is quick.** — The install needs the Zabbly apt repo's GPG key converted to binary form and saved into the apt keyrings directory. After `incus admin init` with default answers, launching an Ubuntu container takes seconds. ([1:20](https://youtu.be/zaAtYkM24hU?t=80))
- **VMs need hardware virtualization, so the demo only launches containers on a Mac-hosted VM.** — The same launch command with the VM flag creates a VM, but nested virtualization is unsupported in the presenter's setup. On bare metal, VMs can run inside VMs. ([3:23](https://youtu.be/zaAtYkM24hU?t=203))
- **Containers have no network by default, so a bridge plus a NIC on the default profile is required before installing software that downloads packages.** — Curl and Ollama installs fail until a bridge network named incusbr0 is created, attached to the default profile as eth0, and the container is restarted. ([4:28](https://youtu.be/zaAtYkM24hU?t=268))
- **A model can be served from a container as a service, though the test model's output was poor.** — Ollama runs in its own container with the small orca-mini model. The joke prompt gave repetitive, unfunny answers, so the demo shows wiring, not model quality. ([4:28](https://youtu.be/zaAtYkM24hU?t=268))
- **Incus projects give separate namespaces for tenants, and per-project limits cap resource use.** — Resources created inside a project are invisible from other projects. The presenter sets a 4-CPU and 8 GB memory limit per project and calls this a basis for a multi-tenant private cloud. ([5:40](https://youtu.be/zaAtYkM24hU?t=340))
- **The presenter's claim of isolation rests on projects and quotas, without an analysis of the security boundary.** — Projects and limits separate tenants and cap usage. The video does not discuss escape risk, shared kernel exposure for containers, or network isolation between tenants, which matter for real customer workloads. ([5:40](https://youtu.be/zaAtYkM24hU?t=340))

## Techniques
- **Install Incus from the signed apt repo** — Run `sudo apt update`, install curl and gpg, create the apt keyrings directory, then curl the Zabbly repo's GPG key and pipe it through `gpg --dearmor` into the keyrings directory so apt trusts packages signed by it. Add the repo, then install the incus package. Check with `sudo incus list`. The exact repo URL and keyring filename are not spoken in the captions, so take them from the Incus install docs. *When:* Installing Incus on Ubuntu for the first time.
- **Initialize Incus and launch a container** — Run `sudo incus admin init` and accept the defaults. Launch an Ubuntu container with a name, then open a shell with `incus exec <name>`. Verify inside the container by checking system folders. *When:* Bootstrapping a local Incus host for dev environments.
- **Launch a VM with the same command** — Use the same image and launch command with the VM flag (`--vm`) to get a VM with its own kernel instead of a shared-kernel container. *When:* You need stronger isolation than a container, on a host with hardware virtualization.
- **Add a bridge network so containers can reach the internet** — Create a bridged network named incusbr0. Attach it to the default profile by adding an eth0 NIC device that points at the bridge. Restart the container so the new interface comes up, then retry the network-dependent install. The captions give the steps but not every flag. *When:* Containers fail to download packages or reach external services.
- **Run Ollama as a service in a container** — Launch a separate Ubuntu container for Ollama, install curl, install Ollama inside it, then pull and run a small model (the demo uses orca-mini) to confirm the service answers. *When:* Hosting a local model behind a container boundary or on a home lab box.
- **Create per-tenant projects with resource limits** — Run `incus project create <name>`, enable the features the project needs (profiles, networks, storage volumes; the presenter corrected a wrong key to storage.volumes), then `incus project switch` into it. Set CPU and memory caps (the demo uses 4 CPUs and 8 GB, which correspond to the limits.cpu and limits.memory config keys). Anything launched in the project is hidden from other projects. *When:* Separating several customers or workloads on one machine with basic quotas.

## Numbers
- Per-project limits in the demo: 4 CPUs and 8 GB memory. ([5:40](https://youtu.be/zaAtYkM24hU?t=340))
- Claimed setup time: under 30 minutes (title). Spoken: installing Incus, launching containers, and deploying an AI model took 'just few minutes'. ([5:40](https://youtu.be/zaAtYkM24hU?t=340))
- Launching a container takes only a few seconds once Incus is initialized. ([2:27](https://youtu.be/zaAtYkM24hU?t=147))
- Video length 8:00. No benchmarks, latency, or cost figures are given. ([0:00](https://youtu.be/zaAtYkM24hU?t=0))

## Hot takes
- The presenter calls Incus 'incredibly efficient' with containers sharing the host kernel, but gives no measurements.
- Incus is described as a basis for a multi-tenant private cloud, but the demo only shows projects and CPU/memory caps. No security analysis of the tenant boundary is given.
- The Ollama section is filler: the test model gave poor answers and the demo shows plumbing, not model quality.
- The walkthrough omits some exact commands and flags, so it is not fully reproducible from the captions alone.
- Quality is capped at 3 because this is a beginner-level tutorial with no sponsor segment, but it still contains usable steps.

## Tools mentioned
Incus (version not stated), LXD (upstream fork origin), LXC (container layer), QEMU (VM layer), Ubuntu (server image and host OS), Ollama, orca-mini (small test LLM), Zabbly apt repo (Incus package source), apt, gpg, curl

## Relevance to our work
- **agentos** (1/3): Incus system containers with per-project CPU/memory quotas are an alternative self-hosted isolation layer to compare against the planned celld sandbox in Crucible. → *Compare Incus (system containers, quotas, startup time) with the planned self-hosted celld backend for Crucible's opt-in sandboxed code execution, before picking one.*
- **prosharness** (1/3): Running long Claude Code CLI runs in isolated, resource-capped containers could support checkpoint/resume and per-run isolation, but the video does not cover agents. → *Prototype one ProsHarness run inside an Incus container with CPU and memory limits, then check whether the checkpoint/resume flow still works from inside the container.*
- **general** (1/3): Useful as a self-hosted home-lab and dev-environment option; the video is an introduction and not a production guide. → *Read the Incus docs on networking and project quotas before using Incus for any multi-tenant workload.*
