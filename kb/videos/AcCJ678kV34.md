# Docker’s Best Security Feature Is Now FREE

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `AcCJ678kV34` · [watch](https://youtu.be/AcCJ678kV34) · **date:** 2026-02-02 · **length:** 4:54 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** Andrus (Better Stack) · **orgs:** Docker, Better Stack, Debian, Alpine
- **topics:** dev-tools, security-guardrails · **tags:** docker, docker-hardened-images, container-security, supply-chain, base-images, helm, kubernetes, open-source-license

> Docker is making its Docker Hardened Images (DHI) free and Apache 2.0 licensed, pitching minimal, patched base images as a supply-chain fix; a short announcement-style explainer with no benchmarks.

## Summary
Better Stack explains that Docker is making its Docker Hardened Images free and open source, covering more than 1000 images under Apache 2.0 with no hidden costs. The speaker argues container security is a supply-chain problem, since every image built on a vulnerable base inherits its packages and CVEs. Previously hardened images were paywalled because patching SLAs and the build service cost money. Migration is pitched as a swap of the base image for its DHI equivalent, which usually works unchanged because DHIs are built on Debian or Alpine. The typical breakage is that bash, curl, apt and other utilities are missing or package managers are locked down, which shows up at image build time and is fixed by explicitly installing the few tools needed. Docker also publishes hardened Helm charts as secure Kubernetes defaults. The video offers no measurements such as image size or CVE counts, so it is an announcement walkthrough rather than evidence.

## Key ideas
- **Docker Hardened Images (DHI) are now free and open source, with the free tier under Apache 2.0** — More than 1000 images are available to any developer with no hidden costs or restrictive licenses. Previously DHI was a commercial offering. ([0:00](https://youtu.be/AcCJ678kV34?t=0))
- **Container security is a supply-chain problem** — Every image built on a vulnerable base inherits its outdated packages and known CVEs. Common base images ship with extra tools and legacy packages that most apps never use. ([0:00](https://youtu.be/AcCJ678kV34?t=0))
- **Paywall rationale** — Hardened images were paid because patching SLAs and the build service carry real operating cost. Docker says the aim is for this level of security to be available to everyone. ([1:52](https://youtu.be/AcCJ678kV34?t=112))
- **Adoption is meant to be a base-image swap** — Replace the existing FROM base with the DHI equivalent. The Dockerfile, build process and app code stay largely the same. DHIs are built on familiar Debian or Alpine foundations. ([1:52](https://youtu.be/AcCJ678kV34?t=112))
- **Minimal images break in predictable ways at build time** — Debugging tools such as bash, curl and apt may be absent, package managers may be locked down, and build steps that assume system utilities can fail. The usual fix is to explicitly install the few tools the build needs. ([3:08](https://youtu.be/AcCJ678kV34?t=188))
- **Hardened Helm charts are also offered** — Instead of community charts that must be hardened by hand, Docker provides charts with secure defaults that remain customizable for Kubernetes deployments. ([3:08](https://youtu.be/AcCJ678kV34?t=188))

## Techniques
- **Swap the base image for its hardened equivalent** — Replace the existing base image in the Dockerfile's FROM line with the DHI version of the same base (Debian or Alpine). Leave the rest of the Dockerfile, the build and the application code unchanged. The video does not show exact image names or commands. *When:* Any Dockerfile built on a common base image where you want a smaller, lower-CVE base with minimal rework.
- **Explicitly install only needed tools during the build** — When the build fails on a missing utility (curl, bash, apt, or a system tool a build step assumes), add an explicit install of just that tool in the build stage. Failures are caught at image build rather than at runtime. *When:* After moving to a minimal, locked-down base image where package managers or debugging tools have been removed.
- **Start Kubernetes deployments from hardened Helm charts** — Use Docker's hardened Helm charts instead of pulling random community charts and securing them manually. Customize values as needed. *When:* Deploying third-party or standard services to Kubernetes where you want secure defaults without becoming a Kubernetes security expert.

## Numbers
- More than 1000 Docker Hardened Images are now free and open source ([0:00](https://youtu.be/AcCJ678kV34?t=0))
- Free tier licensed under Apache 2.0 ([1:52](https://youtu.be/AcCJ678kV34?t=112))
- Speaker says last year was a record year for newly discovered supply-chain attacks (no figure given) ([1:01](https://youtu.be/AcCJ678kV34?t=61))
- No benchmarks given: no image size, CVE count or latency comparisons ([0:00](https://youtu.be/AcCJ678kV34?t=0))

## Hot takes
- The title's 'best security feature' framing is stronger than the content. The video is a short restatement of Docker's announcement with no measurements, comparisons or hands-on testing.
- The 'record year' claim about supply-chain attacks is asserted without a source or figure.
- Calling the free tier 'no hidden costs' is the vendor's framing; the video does not examine what remains paid, such as patching SLAs or support.

## Tools mentioned
Docker, Docker Hardened Images (DHI), Debian, Alpine, Helm, Kubernetes, Apache 2.0 license

## Relevance to our work
- **agentos** (1/3): Relevant only if Crucible sandbox or celld container images are built on generic bases; the video is about base-image supply-chain hygiene, not agents. → *If celld or Crucible sandbox images use generic Debian or Alpine bases, check whether DHI equivalents build cleanly and what extra tools the build needs.*
