# Build Docker Images 40x FASTER with This Tool (depot.dev)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Xdhtmqd8gHs` · [watch](https://youtu.be/Xdhtmqd8gHs) · **date:** 2025-11-02 · **length:** 4:34 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Depot
- **topics:** dev-tools, infra-cost-scaling · **tags:** docker, remote-build, build-cache, docker-compose, depot, ci-speed, developer-productivity

> Better Stack walkthrough of Depot, a remote Docker build service with cloud machines and shared caching, cutting one project's rebuild from 7m44s to 12s with depot build and depot bake.

## Summary
The presenter demonstrates Depot, a remote Docker build service that runs builds on a cloud machine with a remote cache that persists across builds and team members. On a project with backend and frontend services, a rebuild dropped from 7 minutes 44 seconds to 12 seconds. Setup is a Depot account, a project, and a depot build run that authenticates through a browser URL and creates a depot.json file, which must have the same project ID across the team. Builds fail if the Dockerfile is not in the root, so the file flag is used to point at each service's Dockerfile. The first build is slow because it uploads the build context and fills the cache; later builds are fast. For a multi-service project, depot bake takes the existing Docker Compose file so both services build in one run, and teammates who connect to the same project benefit from the cached layers. The presenter says Depot is premium and suggests optimizing local builds as a cheaper alternative, without quantifying pricing.

## Key ideas
- **Remote build offload plus shared cache is the source of the speedup** — Depot runs the Docker build on a faster cloud machine and keeps a cache, so rebuilds do not start from scratch. The presenter credits both factors for the 7m44s to 12s drop on one project. ([0:00](https://youtu.be/Xdhtmqd8gHs?t=0))
- **Project setup creates a shared depot.json** — Create a Depot account and a project, then run depot build to authenticate via a URL and select the project. This generates depot.json, which must hold the same project ID for every team member. ([0:54](https://youtu.be/Xdhtmqd8gHs?t=54))
- **Dockerfiles outside the root break the default invocation** — With no Dockerfile at the repo root, depot build fails with a failed-to-solve error about a missing Dockerfile. Pointing the file flag at each service's Dockerfile fixes it. ([1:51](https://youtu.be/Xdhtmqd8gHs?t=111))
- **First build is the slow one** — The first build uploads the whole build context and fills the remote cache, so it takes a while. Subsequent builds reuse most layers and finish much faster. ([1:51](https://youtu.be/Xdhtmqd8gHs?t=111))
- **Teammates share the cache** — Once teammates install Depot and connect to the same project, their builds populate the cache that others then benefit from. ([2:57](https://youtu.be/Xdhtmqd8gHs?t=177))
- **depot bake handles multi-service compose files** — Instead of running depot build per service, depot bake with the file flag pointing at the existing docker-compose file builds all services with their own contexts and Dockerfiles. ([2:57](https://youtu.be/Xdhtmqd8gHs?t=177))
- **Cost is the stated barrier, with local optimization as the alternative** — The presenter calls Depot a premium service aimed at teams that value time savings. For smaller budgets he points to optimizing local Docker builds and a separate Better Stack Docker best-practices video, without giving prices. ([4:06](https://youtu.be/Xdhtmqd8gHs?t=246))

## Techniques
- **Offload Docker builds to a remote builder with a shared cache** — Install the Depot CLI, run `depot build` once to log in through the browser URL and select a project, which creates depot.json. Commit depot.json so every teammate uses the same project ID. Set the image tag (the transcript says to tag it bs articles) and build; the first run fills the cache. *When:* Several developers or CI runs rebuild the same images, and local builds are slow or the machine is weak.
- **Point the build at a non-root Dockerfile with the file flag** — When Dockerfiles live in service subfolders (backend/, frontend/), pass the file flag with each service's Dockerfile path to depot build. Without it, depot build looks for a Dockerfile at the root and fails with failed to solve. *When:* A monorepo where each service keeps its own Dockerfile and there is none at the repo root.
- **Build all compose services in one remote run with depot bake** — Reuse the existing docker-compose.yml, which already lists each service's build context and Dockerfile. Run `depot bake` with the file flag pointing at that compose file so both services build together. *When:* A docker-compose project with several services, where you want one build command and cache shared across them.

## Numbers
- Rebuild of one Docker image set dropped from 7 minutes 44 seconds to 12 seconds with Depot's remote build and cache (roughly 40x, the title's figure) ([0:00](https://youtu.be/Xdhtmqd8gHs?t=0))
- First-ever Depot build is slower because it uploads the full build context and fills the remote cache; later builds are much faster, with no timing given ([1:51](https://youtu.be/Xdhtmqd8gHs?t=111))
- Pricing is not quantified; the presenter only calls Depot premium ([4:06](https://youtu.be/Xdhtmqd8gHs?t=246))

## Hot takes
- The 40x headline compares a warm-cache rebuild on one project against an uncached local build. The first build is not shown as faster, and the speedup depends on the team sharing the cache.
- Depot is presented as premium with no pricing, and the presenter suggests local build optimization for smaller budgets. Nothing in the transcript shows a sponsorship disclosure.
- Short tutorial with real commands and a clear setup order, but it is thin on caching internals, failure modes, and CI integration.

## Tools mentioned
Depot (depot.dev) CLI, depot build, depot bake, Docker, Docker Compose, Dockerfile, VS Code

## Relevance to our work
- **agentos** (1/3): AgentOS is a multi-service self-hosted stack (proxy, Postgres, Redis, observability), so slow multi-service docker builds could matter, but the video only covers a generic two-service compose project. → *If AgentOS image builds get slow on the single 5090 box or in shared CI, try a remote builder with a shared cache (Depot or similar) on the compose file and measure cold vs warm build times before adopting it.*
