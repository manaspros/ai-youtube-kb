# Coding Locally Is Slowing You Down

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `-b1qrPFl04A` · [watch](https://youtu.be/-b1qrPFl04A) · **date:** 2026-03-02 · **length:** 4:40 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Better Stack presenter (unnamed in transcript) · **orgs:** Better Stack, Microsoft (VS Code), GitHub (Codespaces, Copilot)
- **topics:** dev-tools, sandboxing-execution · **tags:** code-server, vs-code, remote-dev, docker, dev-containers, github-codespaces, django, self-hosting, battery-life, reproducible-environments

> Better Stack walkthrough of Code Server (VS Code in a browser on a remote machine), run locally in Docker on a Mac for the demo; covers pros (reproducible, consistent env, lighter laptops) and cons (latency, RAM needs, basic default security).

## Summary
The video introduces Code Server, an open-source project that runs VS Code on a remote machine and serves it through a browser. The presenter runs it locally in Docker on a Mac M4 Pro, retrieves the generated password, opens localhost, and shows a small Django project with the terminal, Git and extensions working. The main argument is that the environment lives on one machine, so laptops become thin screens, teams share one consistent setup, and builds stop draining the laptop battery. The presenter lists the downsides: latency on bad internet, the need for real server RAM (not tiny VMs), and basic security that requires configuring auth if exposed publicly. He compares it to GitHub Codespaces as more manual but more controllable, and suggests pairing it with dev containers for reproducible environments. The demo is shallow (a landing page), and there are no benchmarks or cost figures. Overall it is a practical but introductory tool overview.

## Key ideas
- **Code Server runs real VS Code on a remote machine and you access it from a browser, so the laptop acts only as a screen while compute happens elsewhere.** — Terminal, extensions and Git all work in the browser session. The presenter frames it as installing the toolchain once on the server rather than on every device. ([0:00](https://youtu.be/-b1qrPFl04A?t=0))
- **Local Docker setup is a quick way to try it before paying for a cloud VM.** — The presenter runs it in Docker on a Mac M4 Pro, retrieves the generated password from the container output, and opens it at localhost. ([0:51](https://youtu.be/-b1qrPFl04A?t=51))
- **A single remote environment removes 'works on my machine' drift for teams.** — Same Node version, Docker setup and extensions for every device connecting to the same place. He argues this matters more for hybrid teams. ([2:14](https://youtu.be/-b1qrPFl04A?t=134))
- **Battery and fan load from builds move to the server, and the server can be upgraded independently.** — He notes that if more power is needed, you upgrade the VM rather than the laptop. ([2:14](https://youtu.be/-b1qrPFl04A?t=134))
- **The main downside is network dependence: bad internet gives a bad experience.** — Latency is directly felt in the editor. He also says the server needs real RAM and warns against tiny VMs. ([3:13](https://youtu.be/-b1qrPFl04A?t=193))
- **Security is basic out of the box; public exposure needs auth configured manually.** — He calls out this gap explicitly as a caveat. ([3:13](https://youtu.be/-b1qrPFl04A?t=193))
- **Compared to GitHub Codespaces, Code Server gives more control but less plug-and-play.** — He says Codespaces is turnkey while Code Server is more of a self-managed option. Suggests starting small (Docker on a home machine or a basic VM). ([3:13](https://youtu.be/-b1qrPFl04A?t=193))
- **Pairing with dev containers makes the environment reproducible for onboarding and debugging.** — Presented as the next step after trying Code Server, not demonstrated in the video. ([4:09](https://youtu.be/-b1qrPFl04A?t=249))

## Techniques
- **Run Code Server in Docker for a quick trial** — Start the Docker setup command (the video does not show the exact image name or flags), confirm the container is running, read the generated password from the output, then open the Code Server URL on localhost and enter the password. Drag a project folder into the browser window. Create a virtualenv, pip install dependencies, and run the app from the integrated terminal. *When:* Evaluating remote VS Code on a personal machine before moving to a cloud VM or home server.
- **Move the heavy environment to a remote host and keep the laptop as a thin client** — Install Node, Docker, Postgres and Python once on a VM or home server. Access the editor from any device over the browser. Scale by upgrading the VM. *When:* Laptops overheat or drain during builds, or you switch between machines often.
- **Pair with dev containers for reproducible environments** — Define the dev environment in a dev container config so onboarding and debugging start from the same setup. The video only mentions this; no config is shown. *When:* Team onboarding, or when you need an environment that matches across machines.
- **Harden before exposing publicly** — Configure authentication correctly before exposing the server beyond localhost. The video does not show the specific auth settings. *When:* Any internet-reachable Code Server deployment.

## Numbers
- Demo hardware: Mac M4 Pro, run locally in Docker (no cloud VM used for the demo). ([0:51](https://youtu.be/-b1qrPFl04A?t=51))
- Runtime length of the video: 4:40. ([4:40](https://youtu.be/-b1qrPFl04A?t=280))
- No benchmarks, latency figures, costs or adoption stats are given. ([0:00](https://youtu.be/-b1qrPFl04A?t=0))

## Hot takes
- Code Server is described as production-ready infrastructure, though the presenter also notes default security is basic.
- Codespaces is 'plug and play' while Code Server offers more control; the trade-off is framed as acceptable for solo users with lower platform costs.

## Tools mentioned
Code Server, VS Code, Docker, Django, pip, GitHub Copilot, GitHub Codespaces, dev containers, Postgres, Node.js, Python

## Relevance to our work
- **prosharness** (1/3): A remote-runner pattern for long Claude Code sessions could be relevant if ProsHarness runs on a server, but the video does not discuss agents. → *Only if ProsHarness needs a remote workspace for checkpointed runs, evaluate a Code Server-style remote workspace; otherwise skip.*
