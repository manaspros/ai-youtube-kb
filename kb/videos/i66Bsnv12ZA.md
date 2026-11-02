# Git Can’t Handle Games… So Epic Built Lore

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `i66Bsnv12ZA` · [watch](https://youtu.be/i66Bsnv12ZA) · **date:** 2026-08-02 · **length:** 7:44 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed) · **orgs:** Epic Games, Better Stack
- **topics:** dev-tools, data-engineering · **tags:** version-control, git-alternative, perforce, git-lfs, large-binary-assets, merkle-tree, chunking, deduplication, zstandard, rust, self-hosted, game-dev

> Epic Games' Lore, a Rust, MIT-licensed, centralized-but-local-first version control system for large binary game assets; a walkthrough of its demo plus an honest take that it is pre-1.0 and benchmarks are unverified.

## Summary
Better Stack walks through Lore, an open-source version control system Epic Games built in Rust for large binary assets such as textures, audio, video and 3D models. The demo runs a local demo server with one install command, commits a 100 MB file, and shows that content-defined chunks hashed with ZStandard and stored in a Merkle tree avoid storing full copies on each change. Branching, staging, committing and switching run locally, so day-to-day work does not need the server. The speaker frames Lore as a centralized system with one server of record that sits between Perforce and Git, and notes it is MIT licensed with SDKs. The caveats are that it is pre-1.0 with APIs that may change, has no Git interop, is self-hosted only, and that its performance claims come mostly from Epic with no independent benchmarks. The speaker's verdict is to try it on a non-critical project rather than replace Perforce or Git.

## Key ideas
- **Git and Git LFS were built for small text diffs, so large binary assets (textures, audio, video, 3D models) cause repo bloat, slow clones and quota pain.** — Perforce works for studios but is costly and needs a dedicated maintainer. Lore is positioned as a response to this gap. ([0:00](https://youtu.be/i66Bsnv12ZA?t=0))
- **Lore chunks files, hashes them, compresses them with ZStandard, and stores them in a content-addressed Merkle tree, so unchanged chunks are reused across versions.** — Demo: a 100 MB file generated with dd is committed; later versions only store the changed chunks rather than a full new copy. ([2:17](https://youtu.be/i66Bsnv12ZA?t=137))
- **Lore is centralized with one server of record, but most operations (stage, commit, branch, switch, diff) run locally, so it works offline and feels fast.** — The speaker places it between Perforce (central access control) and Git (fast local operations). ([3:41](https://youtu.be/i66Bsnv12ZA?t=221))
- **Lore can hydrate files on demand, so a clone of a very large repo does not require downloading every asset up front.** — You pull only the parts of the project you are working on. ([4:49](https://youtu.be/i66Bsnv12ZA?t=289))
- **Lore is pre-1.0. APIs may change, there is no Git interop (no history import from an existing Git repo), and it is self-hosted only.** — The desktop GUI seen in circulation is not part of the MIT-licensed open-source release. That release includes the core library, server, CLI and SDKs. ([4:49](https://youtu.be/i66Bsnv12ZA?t=289))
- **Performance claims for huge repos come mostly from Epic, and the speaker says there are no solid independent benchmarks yet.** — The speaker's recommendation is to test it on a non-critical or new project before considering it for production. ([6:05](https://youtu.be/i66Bsnv12ZA?t=365))

## Techniques
- **Run a local Lore demo server** — Install Lore with a single install command, start the demo mode server (it runs on local ports, needs no account, key or cert, and stores data in a temporary folder that is lost on stop). Verify it is alive by hitting its health endpoint. The speaker does not spell out the exact command names. Production: run `lore server` with a config file and persistent storage directories or object storage, and keep the same CLI workflow. *When:* Evaluating Lore on a non-critical project or prototyping large-binary version control.
- **Basic Lore workflow** — Create a repo folder and commit a large binary (the demo uses dd to generate a 100 MB file). Create a branch with `lore branch create <name>`, switch to it, modify and stage a text file, commit it, then switch back. The commands mirror Git's flow (stage/commit/branch/switch/diff) and run locally. *When:* Trying the Git-like workflow on large-asset repos. The speaker says the flow is roughly the same as Git.

## Numbers
- Demo file size is 100 MB, generated with dd and committed. ([2:17](https://youtu.be/i66Bsnv12ZA?t=137))
- Binary assets in games can be hundreds of MB or several GB each. ([0:00](https://youtu.be/i66Bsnv12ZA?t=0))
- Lore is pre-1.0 and has no independent benchmarks. Performance claims are from Epic. ([6:05](https://youtu.be/i66Bsnv12ZA?t=365))

## Hot takes
- Version control for huge binary assets is not a solved problem, even though Git works well for text.
- Lore is not a replacement for a production Perforce setup yet.
- Epic's performance claims lack independent verification.

## Tools mentioned
Lore (Epic Games, Rust, MIT license, pre-1.0), Git, Git LFS, Perforce, ZStandard, dd, Fortnite (mentioned as Epic's game)

## Relevance to our work
- **prosharness** (1/3): Checkpointing agent runs is a related idea. Lore's content-addressed chunk store is a tangential pattern for artifact checkpoints. → *If ProsHarness snapshots large run artifacts, consider content-addressed chunking with dedup as the storage approach. Lore is a reference, not a dependency.*
