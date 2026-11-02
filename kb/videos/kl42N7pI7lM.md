# TypeScript 7 Officially Released And Boy Is It Fast

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `kl42N7pI7lM` · [watch](https://youtu.be/kl42N7pI7lM) · **date:** 2026-08-02 · **length:** 8:32 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Microsoft, Better Stack, Bluesky, Playwright
- **topics:** dev-tools · **tags:** typescript, tsc, go, compiler, type-checking, language-server, performance, vs-code, parallelism, benchmarks

> Better Stack walks through why TypeScript 7 (the Go port of the compiler) is much faster, with build and type-check benchmarks on a VS Code checkout and an M3 Max.

## Summary
TypeScript 7 is released as a port of the compiler from JavaScript to Go, and npm install typescript now gets this version. The presenter argues JavaScript is single-threaded and that worker-based parallelism needs costly serialization, while Go offers compiled code and shared-memory concurrency across all cores. He attributes roughly half the speedup to native code and half to shared-memory concurrency. Reported build times for VS Code, Bluesky and Playwright drop by roughly 8 to 12x. On his M3 Max he runs tsc on a local VS Code checkout, where TypeScript 7 takes 5.4s (4.7s in type checking) against 45.3s for TypeScript 6, and 3.5s with the checkers flag raised to 12. He also claims a much more stable language server with fewer failed commands and crashes, and notes that it is a port rather than a rewrite, so API-dependent tooling such as typescript-eslint and ts-jest will lag until the programmatic API ships in 7.1. The VS Code extension is still needed for now. The benchmarks are single-machine and self-reported, and the presenter's ratios differ slightly from his own raw numbers.

## Key ideas
- **TypeScript 7 is a port of the compiler to Go, and it is the version npm install typescript now resolves to.** — The presenter says it took over a year of porting, and that the port is the same feature set as TypeScript 6 (he calls it a port, not a rewrite). ([0:00](https://youtu.be/kl42N7pI7lM?t=0))
- **The speedup comes from the language, not just the port: JS is single-threaded and worker-based parallelism is expensive.** — Workers can only share raw bytes via SharedArrayBuffer, so passing an AST to a worker means serializing and copying it, which can cost more than the work itself on big files. Go gives compiled code plus shared-memory concurrency. ([1:05](https://youtu.be/kl42N7pI7lM?t=65))
- **About half the speedup is attributed to native code and about half to shared-memory concurrency.** — Rough split given by the presenter. The gap is expected to widen because core counts are growing faster than single-core speed. ([2:00](https://youtu.be/kl42N7pI7lM?t=120))
- **Parallel type checking is the main lever, and it is tunable.** — Go spins up four type checkers by default, each handling a quarter of the codebase. Raising the count (he uses 12) shortens the check phase further. ([2:58](https://youtu.be/kl42N7pI7lM?t=178))
- **On a real local repo, the gain is large and the checker count matters.** — VS Code checkout diagnostics on an M3 Max: TypeScript 6 took 45.3s, TypeScript 7 took 5.4s (4.7s of it in checking), and TypeScript 7 with 12 checkers took 3.5s (2.9s checking). ([4:05](https://youtu.be/kl42N7pI7lM?t=245))
- **Concurrency in the new code is just queueing work and waiting, with no thread management.** — A bindSourceFiles loop queues a bind task per file and waits for all of them. The Go runtime distributes the work, and the same code in JS would run sequentially even with promises. ([5:03](https://youtu.be/kl42N7pI7lM?t=303))
- **Editor responsiveness is the everyday payoff, not just CI build time.** — The presenter says the language server now gives near-instant error feedback, and that TypeScript 7 cut failing language-server commands by over 80% and server crashes by over 60%, reducing IDE restarts. ([6:24](https://youtu.be/kl42N7pI7lM?t=384))
- **Ecosystem tooling lags: programmatic API arrives in 7.1, and the VS Code extension is needed for now.** — Packages that depend on the compiler API (typescript-eslint, ts-jest and similar) will need to wait for 7.1. Until the default VS Code package is updated, you install the separate TypeScript 7 extension. ([6:24](https://youtu.be/kl42N7pI7lM?t=384))

## Techniques
- **Benchmark tsc across versions on your own repo** — Install TypeScript 7 (npm install typescript gives v7 now), run tsc diagnostics on a large repo, then run the TypeScript 6 build on the same repo and compare total and check-phase times. The presenter used the VS Code repo. *When:* Before upgrading a large monorepo, to measure the real gain on your hardware rather than trust the headline numbers.
- **Raise the type-checker count to use more cores** — Pass a checkers flag to tsc with a higher count (the presenter says 'checkers 12', so the flag is likely --checkers 12). Default is 4 checkers, each taking a share of the files. *When:* On machines with many cores (he uses a 14-core M3 Max) when type checking dominates the build. Note it steals CPU from other processes, so only use it when the machine is otherwise idle.
- **Install the TypeScript 7 VS Code extension for editor use** — Install the separately published 'TypeScript 7' extension from the VS Code marketplace. The presenter says the default VS Code package will be updated later. *When:* When you want the new language server in the editor before the default TypeScript package in VS Code is updated.
- **Wait on tooling that uses the compiler API** — Hold off on upgrading typescript-eslint, ts-jest or other packages that call the programmatic API until their TypeScript 7 support ships (presenter says the programmatic API arrives in 7.1). *When:* When your build or lint pipeline depends on a compiler-API consumer, to avoid breakage.

## Numbers
- VS Code (1.3M lines, about 8,000 files) builds in 10 seconds on TypeScript 7 versus 125 seconds on TypeScript 6, quoted as 11.9x (raw figures 125.7s vs 10.6s). ([0:00 and 2:00](https://youtu.be/kl42N7pI7lM?t=0))
- Bluesky: 24.3s to 2.8s, quoted as 8.7x. ([2:00](https://youtu.be/kl42N7pI7lM?t=120))
- Playwright: 12.8s to 1.5s, quoted as 8.7x (the raw ratio is about 8.5x). ([2:00](https://youtu.be/kl42N7pI7lM?t=120))
- A large project compile drops from 45 seconds on TypeScript 6 to as little as 3 seconds on TypeScript 7 on a 14-core M3 Max (presenter's claim, project not identified). ([2:58](https://youtu.be/kl42N7pI7lM?t=178))
- VS Code checkout tsc diagnostics: TypeScript 6 45.3s; TypeScript 7 5.4s total with 4.7s in check; TypeScript 7 with 12 checkers 3.5s total with 2.9s in check. Presenter calls the 45.3s to 3.5s gap about 15x, but the arithmetic gives about 12.9x. ([4:05](https://youtu.be/kl42N7pI7lM?t=245))
- Language server: failing commands cut by over 80% and server crashes cut by over 60% versus the previous version (presenter's claim). ([6:24](https://youtu.be/kl42N7pI7lM?t=384))
- Default checkers: 4 type checkers, each checking a quarter of the codebase. ([2:58](https://youtu.be/kl42N7pI7lM?t=178))

## Hot takes
- The benchmarks are one machine and self-reported. The presenter's ratios differ slightly from his raw numbers: the VS Code 45.3s to 3.5s gap is about 12.9x, not the 15x he states, and the Playwright ratio is about 8.5x, not 8.7x.
- The 'about half native code, half shared memory' split is an offhand estimate, not a measurement.
- The video is an enthusiastic walkthrough with some filler (the 'emotional' and 'environment' jokes, and an unverified claim that TypeScript is the number one language on GitHub). The technical explanation of workers versus shared-memory concurrency is the useful part.
- Not sponsored. Substance is practitioner-level with real but limited benchmarks; the content is not a pure pitch, so quality stays at 3.

## Tools mentioned
TypeScript 7 (tsc, Go-based compiler), TypeScript 6 (baseline), Go, VS Code, TypeScript 7 VS Code extension, typescript-eslint, ts-jest, Node.js, Playwright, Bluesky codebase (benchmark repo), Apple M3 Max (test machine)

## Relevance to our work
- **prosharness** (1/3): ProsHarness is a harness around the Claude Code CLI, which may be TypeScript-based. The video shows tsc build and type-check time can be a real bottleneck on big repos. → *If ProsHarness has a TypeScript build or typecheck step that is slow, benchmark tsc 6 against tsc 7 on the repo with --checkers set to the core count before deciding whether to upgrade.*
