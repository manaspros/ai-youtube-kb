# AI Coding Agents Are Breaking Big Codebases — Dan Adler, Sourcegraph

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Bdrs3uAX0_M` · [watch](https://youtu.be/Bdrs3uAX0_M) · **date:** 2026-10-05 · **length:** 12:23 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Dan Adler · **orgs:** Sourcegraph, Mercari
- **topics:** coding-agents, software-factory, context-engineering, rag-retrieval · **tags:** large-codebases, code-graph, batch-changes, agent-sweeps, code-health, vulnerability-remediation, monorepo-scale, code-search

> Sourcegraph CEO Dan Adler argues that large, decades-old codebases are decaying under the flood of AI-written code, and that agents need code-graph and search infrastructure to see and change them across thousands of repos.

## Summary
Dan Adler (CEO of Sourcegraph) argues that most engineers work in huge, long-lived codebases, and that AI coding agents are producing code faster than owners can review or keep healthy. He says duplication, inconsistent standards, brittle cross-service dependencies and new vulnerabilities are piling up. He claims grep-style search and AGENTS.md files cannot give agents enough understanding of 50k+ repo estates. His proposed fix is a foundational code graph combining search with compiler-accurate analysis. Sourcegraph's new agentic batch changes beta applies changes across many repos, using agents where judgment is needed and deterministic scripts elsewhere, with tracking for coverage. An early-access Mercari example shows one vulnerability fix expanding to about 80 more findings. The talk is mainly a product pitch, but it has a usable framing for large-scale agent changes.

## Key ideas
- **Volume of AI-written code is the core problem for large codebases** — The speaker says AI tools make code faster to write but cause decay: duplicated code, inconsistent standards, brittle cross-service dependencies, and new vulnerabilities that need constant upkeep. ([2:22](https://youtu.be/Bdrs3uAX0_M?t=142))
- **Repo docs like AGENTS.md barely help at large scale** — He says a repo architecture in agent instruction files barely moves the needle. Agents will grep their way to understanding, and grep cannot cover codebases of tens of thousands of repos. ([6:51](https://youtu.be/Bdrs3uAX0_M?t=411))
- **Understanding is a context problem that needs a code graph** — The proposed foundation is a graph of the whole codebase, combining search with compiler-accurate analysis, so agents can see how to make changes safely. ([8:06](https://youtu.be/Bdrs3uAX0_M?t=486))
- **Batch changes across many repos with mixed agent and script steps** — Sourcegraph's agentic batch changes (beta) run one prompt across hundreds or thousands of repos. Coding agents handle judgment steps, deterministic scripts handle the rest, and the system responds to CI status and PR comments. ([9:10](https://youtu.be/Bdrs3uAX0_M?t=550))
- **Coverage tracking matters more than one-off fixes** — Audit tracking is meant to prove that the change reached 100% of the places it was needed, which he presents as what confidence means in the agentic era. ([9:10](https://youtu.be/Bdrs3uAX0_M?t=550))
- **Unknown repo inventory is a security risk** — He raises forks, copies, and libraries imported from unknown repos as a source of live risk. He says finding what runs in production is the first step. ([10:34](https://youtu.be/Bdrs3uAX0_M?t=634))

## Techniques
- **Deterministic scripts for mechanical sweep changes** — Apply one known patch with a deterministic script across many matching locations, so the change is applied consistently. Agents are used only where judgment is needed. *When:* Repeated security or config fixes across many repos, such as a fix that appears in many config files.
- **Hybrid agent and script batch change loop** — Iterate on a single prompt across repos. Agents handle judgment, scripts handle the rest, and the loop reacts to CI status and PR comments until the change is complete. *When:* Org-wide migrations or patches where some sites need judgment and others are mechanical.
- **Code-graph plus search as agent context** — Build a graph of the codebase with search and compiler-accurate analysis, and expose it to agents, instead of relying on grep and repo docs. *When:* Codebases too large to fit in a context window or clone in real time.
- **Coverage audit for sweeping changes** — Track each target location and verify that the change reached all of them, not just the ones the agent found first. *When:* Any multi-repo change where missing a site is a security or correctness risk.

## Numbers
- 72% of software industry employment is in companies with more than 500 people ([0:12](https://youtu.be/Bdrs3uAX0_M?t=12))
- A Mercari early-access run on two repos found about 80 other potential vulnerabilities across the codebase ([10:34](https://youtu.be/Bdrs3uAX0_M?t=634))
- A top-10 US bank has about 90,000 repositories ([5:16](https://youtu.be/Bdrs3uAX0_M?t=316))
- Codebases discussed run from 500 to 500,000 repos, and an example of 50,000 repos ([5:16](https://youtu.be/Bdrs3uAX0_M?t=316))

## Hot takes
- Repo architecture docs like AGENTS.md barely move the needle for large codebases.
- Major coding-agent vendors are not building infrastructure to see and understand 50,000-repo estates.
- The volume of AI-written code, not model quality, is the main threat to large codebases.

## Tools mentioned
Sourcegraph, agentic batch changes, Claude Code, Codex, Cursor

## Relevance to our work
- **prosharness** (2/3): ProsHarness runs checkpointed Claude Code loops. The deterministic-script plus agent-judgment split and coverage tracking map directly onto long batch runs. → *Consider adding a coverage check to ProsHarness plan steps that apply one change across many files, and split mechanical steps from judgment steps.*
- **general** (2/3): Practical framing for codebase decay and agent-driven sweeps, relevant to work on large enterprise codebases. → *Use the hybrid script-plus-agent batch loop and the coverage audit as a checklist for any large org-wide agent change.*
- **agentos** (1/3): AgentOS L2A MemoryMesh and L2D SkillForge deal with retrieval and telemetry-derived skills. The talk raises code-graph and search infra, which is adjacent but not directly in scope. → *Read Sourcegraph's batch changes write-up to compare its audit-tracking approach with SkillForge's success signal.*
