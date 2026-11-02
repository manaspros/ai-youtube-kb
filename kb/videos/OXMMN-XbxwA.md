# Research to Reality: Bringing Frontier ML Research to Production - Vaidas Razgaitis, Higharc

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `OXMMN-XbxwA` · [watch](https://youtu.be/OXMMN-XbxwA) · **date:** 2026-07-18 · **length:** 14:57 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Vaidas Razgaitis · **orgs:** Higharc, Graphite
- **topics:** enterprise-adoption, pr-code-review, context-engineering, agent-architecture · **tags:** research-to-production, design-docs, monorepo, microservices, stacked-prs, ml-engineering-handoff, fastapi

> Higharc's labs team on moving ML research prototypes into production via three levers: a design-doc-style "research prototype taxonomy," a decoupled Python microservice monorepo, and stacked-PR decomposition for review.

## Summary
Vaidas Razgaitis, a senior research engineer on Higharc's labs team, describes how his R&D group moves frontier ML work (computer vision on sketched floor plans, reasoning agents, custom transformers, diffusion) into a production home-building product. He frames the core problem as a handoff gap: ML researchers can prototype novel ideas but lack production API experience, while platform and backend engineers know production practice but not the ML methods. He treats this as a systems and process problem and offers three levers. First, a "research prototype taxonomy" document, essentially an RFC/technical design doc with ML-specific sections: domain context, business goal, type contracts, persistence, system architecture, and decomposition plan. Second, a monorepo of cleanly isolated Python microservices, roughly one per researcher, behind a gateway, each built as a layered FastAPI app with its own Dockerfile and lock file. Third, decomposing large prototypes into stacked PRs (Graphite) so domain experts can review slices asynchronously. He closes with diagnostic questions to find which lever is weak. The talk is process-level and light on hard numbers or code, so its value is mainly as a template for handoff docs and repo layout.

## Key ideas
- **Research-to-production is a handoff and process problem, not just a modeling problem** — Researchers can prototype but lack production API experience; SWE/platform engineers know production code but not the ML methods. The speaker attacks the gap with three process levers rather than individual skill. ([1:02](https://youtu.be/OXMMN-XbxwA?t=62))
- **A 'research prototype taxonomy' doc acts as the handoff contract** — Modeled on engineering RFCs/design docs (he cites a Pragmatic Engineer piece on pre-build specs for aligning growing teams). It is required for every prototype and written in Notion. ([3:19](https://youtu.be/OXMMN-XbxwA?t=199))
- **Domain context section is written for an outsider engineer** — The doc starts with domain vocabulary and data representations (e.g., party diagrams, circulation graphs, embeddings or latent spaces). The test is whether a newly hired engineer from a non-ML background could get up to speed from it. ([4:29](https://youtu.be/OXMMN-XbxwA?t=269))
- **Type contracts between the product repo and the ML repo are set up front** — The doc specifies what types cross the boundary and how they are shared and kept in sync. This is a standard TDD-style concern carried into the research doc. ([4:29](https://youtu.be/OXMMN-XbxwA?t=269))
- **Keep researchers out of the persistence layer** — The doc only maps how far the persistence design got. Engineers take over the database work, which the speaker sees as the natural first entry point for software engineering help. ([5:51](https://youtu.be/OXMMN-XbxwA?t=351))
- **One researcher maps to one decoupled microservice behind a gateway** — All services sit in one Python monorepo on a shared Docker bridge network. Clients call a gateway that routes to the right service, so each research line can iterate without affecting others. ([7:12](https://youtu.be/OXMMN-XbxwA?t=432))
- **Uniform layered skeleton for every microservice** — Services layer holds business logic (LLM calls, model weights pulled in CI/CD), wrapped by controllers, then API routers in FastAPI. Each service is standalone, with metadata, a Dockerfile, dependencies, and a poetry or uv lock file. The repeated skeleton makes the codebase easy to audit and easy for agents to navigate. ([8:39](https://youtu.be/OXMMN-XbxwA?t=519))
- **Decompose monolithic prototypes into stacked PRs, sliced by a dependency graph** — The team studies which axes to slice a large platform-wide agent feature along, maps the dependency graph, then uses Graphite stacked diffs. Stacking lets an author keep building while a domain specialist reviews an earlier slice asynchronously. ([11:26](https://youtu.be/OXMMN-XbxwA?t=686))
- **The taxonomy doc should drive the decomposition plan** — Once layers, architecture, persistence, and types are mapped, the decomposition and merge order mostly follows from the doc. Weak decomposition is read as a symptom of upstream handoff or codebase problems. ([12:25](https://youtu.be/OXMMN-XbxwA?t=745))
- **Diagnostic questions for each lever** — Is it clear what researchers should do and what engineers should pick up? Are there templates to copy in the repo, or has it outgrown its abstractions? Can timelines and SME reviewers be estimated consistently? Failures in the third point usually trace back to the first two. ([13:24](https://youtu.be/OXMMN-XbxwA?t=804))

## Techniques
- **Research prototype taxonomy (RPT) doc** — Write a design doc with fixed sections: domain context and vocabulary, business goal, type contract with the product repo, persistence sketch, system architecture (workflows, external LLM calls), and decomposition/merge plan. Keep it in a shared doc tool such as Notion. *When:* Before any research prototype is handed to engineers for productionization, especially when researchers and engineers are on different teams.
- **One researcher, one decoupled microservice in a shared monorepo** — Each research initiative gets its own FastAPI service with a standard layout (services, controllers, routers) and its own Dockerfile and lock file. A gateway routes client calls, and all services share CI, lint, type checks, and tests. *When:* When several research tracks must iterate independently but ship through one codebase and one deploy pipeline.
- **Slice by dependency graph, then stack PRs** — Map the prototype's components and their dependencies, choose slicing axes, and split the work into a stack of small PRs using Graphite. Route each slice to the relevant domain expert. *When:* When a large monolithic prototype must be reviewed by several subject-matter experts without blocking the author.
- **Use the design doc to plan the merge** — Derive the PR decomposition and the order of merges from the architecture and type-contract sections of the design doc rather than planning from scratch. *When:* When estimating timelines for moving a prototype into the main repo.
- **Notebooks on Modal for GPU experiments** — Run Jupyter notebooks on Modal for GPU compute during research studies, separate from the production microservices. *When:* When researchers need on-demand GPU for experiments that are not yet productionized.

## Numbers
- Roughly a one-to-one ratio of ML researchers to microservices in the monorepo ([7:12](https://youtu.be/OXMMN-XbxwA?t=432))
- Three microservices in production, all sharing one skeleton ([9:00](https://youtu.be/OXMMN-XbxwA?t=540))
- Each research prototype requires a taxonomy doc before code moves to the monorepo ([3:19](https://youtu.be/OXMMN-XbxwA?t=199))

## Hot takes
- Research prototypes should get a design doc with type contracts and a persistence sketch before any production code is written, the same way SWE teams write RFCs.
- Researchers should not spend much time on the persistence layer; engineers should take over the database design.
- Stacked PRs with asynchronous domain-expert review are the right way to bring a large research prototype into production.
- If decomposition estimates are unreliable, the root cause is usually the handoff doc or the codebase, not the review process.

## Tools mentioned
Notion, Graphite, GitHub Actions, Modal, Docker, FastAPI, Poetry, uv, Jupyter

## Relevance to our work
- **general** (2/3): Concrete handoff artifacts (design doc with fixed sections, one-service-per-researcher monorepo, diagnostic questions for each lever) apply directly to any team bringing ML or agent prototypes into production. → *Adapt the RPT section list into a team template and use the three diagnostic questions as a retro checklist after the next prototype handoff.*
- **agentos** (1/3): The talk is about process and repo layout for ML teams, not infra or pillars. Its gateway-routes-to-isolated-services pattern is loosely analogous to the one-proxy design, but nothing here changes how AgentOS pillars are built. → *Consider adding a short research-prototype-style design template (domain context, type contract, persistence, architecture, merge plan) for new AgentOS pillars like InferCraft or SkillForge.*
- **prosharness** (1/3): The stacked-PR review workflow and slicing a large feature by its dependency graph could structure ProsHarness PRs, but the talk does not address agent-run checkpointing or CLI harnesses. → *If ProsHarness changes get large, try Graphite-style stacked PRs and review each slice as its own unit.*
