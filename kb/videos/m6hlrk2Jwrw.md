# Deno 2 vs Bun: Which Should You Choose?

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `m6hlrk2Jwrw` · [watch](https://youtu.be/m6hlrk2Jwrw) · **date:** 2025-11-02 · **length:** 7:52 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Deno, Bun, Node.js, WebKit, Better Stack
- **topics:** dev-tools · **tags:** deno, bun, node.js, javascript, typescript, javascript-runtime, npm, jsr, sqlite, permissions, supply-chain-security, package-manager, comparison

> Better Stack compares Deno 2, Bun and Node.js: shared web-standard APIs and tooling, Deno's deny-by-default security and built-in stdlib, Bun's speed and drop-in Node compatibility, with a pick-by-use-case verdict.

## Summary
The video frames Deno 2 and Bun as two modern JavaScript runtimes that aim to replace Node.js, with Deno 2 now also backwards compatible with Node. Both ship built-in TypeScript and JSX support, use web-standard APIs, work with npm packages, and include a test runner. Deno, written in Rust on V8, locks down file and network access by default, bundles a standard library, and includes linting, formatting, a single-command binary compile, and the JSR registry. Bun, written in Zig on WebKit's JavaScriptCore, emphasizes startup speed, a built-in SQLite driver, a fast package manager, a hot-reload flag, optimized native APIs, Bun Shell, and experimental C compilation. The speaker gives no independent benchmarks and says vendor numbers should be checked against your own use case. Their verdict: choose Deno for security, standardization, and new projects; choose Bun for performance and minimal-friction drop-in replacement of Node. The speaker says they use Bun on existing projects and plan to start new ones on Deno.

## Key ideas
- **Deno 2 is now backwards compatible with Node, so there are three viable JavaScript runtimes (Node, Deno, Bun).** — Deno was created in 2018 by Ryan Dahl, Node's original creator. Bun followed in 2021 as a drop-in Node replacement. Deno 2 added Node backwards compatibility in 2025. ([0:00](https://youtu.be/m6hlrk2Jwrw?t=0))
- **Both runtimes share the same developer-experience baseline.** — Built-in TypeScript and JSX with no config, web-standard APIs (fetch, WebSockets, ReadableStream) so code runs on server and browser, npm package support, and a built-in test runner. The speaker says Bun's test runner is Jest-compatible. ([1:15](https://youtu.be/m6hlrk2Jwrw?t=75))
- **Deno's main differentiator is security: deny-by-default permissions.** — Node and Bun give packages full system access by default. Deno requires explicit permission for file and network access, which the speaker says helps against supply-chain attacks. ([2:28](https://youtu.be/m6hlrk2Jwrw?t=148))
- **Deno reduces dependency sprawl with a standard library and built-in tooling.** — The stdlib covers path, JSON-C, encoding, YAML, semver and text, and the modules are audited by the core team. Linting and formatting are built in, with no ESLint or Prettier config. Compiling to a binary is a single command. ([3:37](https://youtu.be/m6hlrk2Jwrw?t=217))
- **Deno moved away from URL imports toward JSR, a cross-runtime registry.** — The speaker names URL imports' problems: long URLs, dependency management, and reliability (an unreachable host can break CI). JSR is described as a superset of npm that interoperates with it, generates docs and type declarations, and transpiles source you publish. ([3:37](https://youtu.be/m6hlrk2Jwrw?t=217))
- **Bun's pitch is speed plus a batteries-included toolkit.** — Claimed about 4x faster startup than Node. Bun bundles a native SQLite 3 driver, a package manager usable in any package.json project, a hot-reload flag, and optimized Bun-global APIs such as hashing. Its WebSocket implementation is claimed to have about 7x Node's throughput. ([4:41](https://youtu.be/m6hlrk2Jwrw?t=281))
- **Bun has more experimental, niche features (Bun Shell, native C).** — Bun Shell is a cross-platform bash-like shell with JS interop. Bun also has experimental support for compiling and running C with shared memory and near-zero call overhead. The speaker presents these as curiosities rather than core reasons to choose Bun. ([5:45](https://youtu.be/m6hlrk2Jwrw?t=345))
- **Benchmarks from each vendor disagree, so pick by your own workload.** — The speaker says both Bun and Deno claim superior performance in their own benchmarks and both generally beat Node. Real-world results vary by use case. ([5:45](https://youtu.be/m6hlrk2Jwrw?t=345))
- **Decision rule: Deno for security, standardization and new projects; Bun for speed and Node compatibility with less friction.** — The speaker cites the 2023 State of JavaScript survey, where Bun was used more than Deno as a runtime. They say Bun's drop-in feel explains this. They use Bun on existing projects and plan to start new projects on Deno 2. ([6:45](https://youtu.be/m6hlrk2Jwrw?t=405))

## Techniques
- **Adopt Bun as a package manager in an existing package.json project** — Bun's package manager can be dropped into any JavaScript project with a package.json, and the speaker uses it as a pnpm-like replacement on legacy projects. No exact commands are shown in the video. *When:* When you want faster installs in an existing Node project without switching the runtime.
- **Run a file with hot reloading in Bun** — Use Bun's hot flag to run a file. Bun reruns the file whenever any module it depends on changes. The flag is named only as 'hot' in the video; the exact invocation is not shown. *When:* During local development of an API or server where you want fast feedback without a separate watcher.
- **Use Deno's permission model to limit what dependencies can do** — Deno denies file and network access unless it is explicitly granted. The video does not show the permission flags. Treat the default-deny model as the security property to rely on. *When:* When running third-party code or new projects where supply-chain risk matters.

## Numbers
- Node.js dominated server-side JavaScript for about 9 years before competition arrived ([0:00](https://youtu.be/m6hlrk2Jwrw?t=0))
- Deno announced in 2018, Bun in 2021 ([0:00](https://youtu.be/m6hlrk2Jwrw?t=0))
- Bun startup claimed about 4x faster than Node.js (vendor claim, not verified) ([4:41](https://youtu.be/m6hlrk2Jwrw?t=281))
- Bun WebSocket throughput claimed about 7x Node.js (vendor claim, not verified) ([4:41](https://youtu.be/m6hlrk2Jwrw?t=281))
- Compiling to a binary takes one command in Deno versus an 8-step process in Node (speaker's description) ([3:37](https://youtu.be/m6hlrk2Jwrw?t=217))
- 2023 State of JavaScript survey: Bun used more than Deno as a runtime ([6:45](https://youtu.be/m6hlrk2Jwrw?t=405))

## Hot takes
- Deno 2 is now the speaker's default for any new JavaScript project because of its developer experience and standard library.
- Bun's popularity over Deno comes from how easily it drops into existing Node projects, not from raw technical superiority.
- Vendor benchmarks from both Bun and Deno are not decisive; the speaker says to benchmark your own use case.
- The speaker says there is little reason to keep using npm alone when Bun or Deno and pnpm are available.

## Tools mentioned
Node.js, Deno 2, Bun, JSR (Deno registry), npm, pnpm, V8, WebKit JavaScriptCore, Rust (Deno implementation language), Zig (Bun implementation language), ESLint, Prettier, Jest, Lodash, Jupyter, SQLite, Bun Shell, State of JavaScript survey

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, which is a Node.js program. A Bun or Deno swap is not discussed, but the sandboxing and permission model of Deno is a relevant idea for running agent subprocesses. → *No change now. If ProsHarness adds JS/TS tooling, benchmark its test or startup time on Bun against Node, and note Deno's default-deny permissions as a design reference for sandboxing agent subprocesses.*
