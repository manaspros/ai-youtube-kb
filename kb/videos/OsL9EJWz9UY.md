# Effect 4.0 Just Got a Lot Harder to Ignore

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `OsL9EJWz9UY` · [watch](https://youtu.be/OsL9EJWz9UY) · **date:** 2026-10-12 · **length:** 8:17 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Josh · **orgs:** Better Stack, Effect, FP-TS
- **topics:** dev-tools · **tags:** typescript, effect, typed-errors, retries, timeouts, dependency-injection, migration, bun, npm, zod, fp-ts, effect-schema

> Better Stack reviews Effect 4.0, a TypeScript library that puts errors, retries, timeouts and dependency needs into the type system, and argues the stable release still carries unstable modules and inflated download numbers.

## Summary
The video explains Effect's core idea: an Effect type carries success value, error type and requirements, so failures and dependencies show up in the function signature instead of hiding in the implementation. A live demo in Bun on a Mac shows the error union changing as retry, timeout and catch are piped in, and a 50 ms timeout producing a real TimeoutError. It then covers the 4.0 release: a rewritten fiber runtime, a much smaller minimum bundle, packaging merged into one package with zero core runtime dependencies, renamed APIs, and long-term bug-fix support until September 2029. The reviewer pushes back on the headline numbers, noting the benchmarks are vendor-reported, the bundle size differs between the blog and migration guide, and most of the 50M weekly downloads were betas and release candidates. He also points out that AI, CLI, Cluster, HTTP, RPC and SQL remain marked unstable and Schema was heavily reworked, and that there is no official codemod. His verdict is to try it on legacy code with untyped failure paths, upgrade v3 users carefully, and skip it for small apps because a half-adoption is worse than none.

## Key ideas
- **Effect changes the function contract from a promise of a value to a typed effect with three channels: success, error and requirements.** — Failures such as network errors, not-found, and hangs become part of the signature, so TypeScript describes how a call can fail, not just what it returns. ([0:00](https://youtu.be/OsL9EJWz9UY?t=0))
- **The compiler tracks the error union as behavior is piped in and out.** — Handling a NotFound error removes it from the error channel. Adding a timeout adds a TimeoutError. The type always reflects the failures possible at that point in the pipeline. ([1:31](https://youtu.be/OsL9EJWz9UY?t=91))
- **Forcing a timeout to 50 ms confirms the type-level prediction at runtime.** — The demo run produces the TimeoutError the type had already declared, which the speaker uses to explain the model's value. ([2:53](https://youtu.be/OsL9EJWz9UY?t=173))
- **The 4.0 runtime is a rewrite of the fiber scheduler, and the vendor reports large gains.** — Claimed minimum bundle drops from about 35.5 KB (v3) to about 7 KB, task throughput is about 6.5x higher, and memory for 50,000 fibers falls from about 157 MB to about 22 MB. These are vendor numbers and the speaker has not reproduced them. ([2:53](https://youtu.be/OsL9EJWz9UY?t=173))
- **Packaging collapses into one package with one version number.** — Platform, RPC and Cluster now live inside the main effect package, and the core has zero runtime dependencies. This removes version-matching across several packages. ([2:53](https://youtu.be/OsL9EJWz9UY?t=173))
- **Several APIs are renamed and LTS is set to September 2029.** — Context.Tag becomes Context.Service, catchAll becomes catch, Either becomes Result, and runtime is removed. Bug fixes are promised until September 2029. ([4:06](https://youtu.be/OsL9EJWz9UY?t=246))
- **The headline numbers need heavy caveats.** — The launch blog gives a 7.1 KB minimal bundle while the migration guide says about 6.3 KB. Of roughly 50M weekly downloads, about 29M went to v4 betas and RCs, and stable 4.0 had around 150k on day one. ([5:00](https://youtu.be/OsL9EJWz9UY?t=300))
- **Stable does not mean every module is stable.** — AI, CLI, Cluster, HTTP, RPC and SQL are still marked unstable and can break in minor releases. Schema was heavily reworked during beta and has its own migration guide. ([5:00](https://youtu.be/OsL9EJWz9UY?t=300))
- **Adopting Effect deeply changes the architecture, not just one utility.** — The speaker compares full adoption to switching languages that still compile to JavaScript, and warns that partial adoption can be worse than none. ([6:19](https://youtu.be/OsL9EJWz9UY?t=379))

## Techniques
- **Encode failures in the signature with typed errors** — Define custom error types (the demo uses NotFound and an HTTP error), wrap the operation in an Effect, then pipe in retry, timeout and catch. Hover over the function to read the success, error and requirements types. Handled errors drop out of the error channel and new ones such as TimeoutError appear. *When:* Codebases full of retries, timeouts and error paths that the type system cannot see, where you want the compiler to catch unhandled failure modes.
- **Verify a timeout by forcing it to fail** — Set the timeout to a value far below the real latency (the demo uses 50 ms instead of 2 s) and run it, confirming the TimeoutError the type predicted actually appears. *When:* Checking that the typed error channel matches runtime behavior before relying on it.
- **Install the single consolidated package** — Run `bun add effect` or `npm install effect`. Platform, RPC and Cluster ship inside it, so no per-feature packages are needed. *When:* Starting a new Effect 4.0 project or consolidating from v3's multi-package setup.
- **Migrate with a coding agent using the migration guide** — There is no official codemod. The launch blog suggests giving the migration guide to a coding agent. Treat Schema and unstable modules as separate migration work. *When:* Upgrading an existing codebase from v3 to v4.
- **Adoption triage: where Effect fits** — Adopt where existing code already has retries, timeouts and error handling that the type system cannot track. Upgrade v3 users, but move Schema and unstable modules like their own project. Skip it for small apps that will not fully adopt the model. *When:* Deciding whether to introduce Effect into an existing or new TypeScript codebase.

## Numbers
- Effect gets about 50 million weekly npm downloads, but about 29 million of last week's were v4 betas and release candidates. ([0:00](https://youtu.be/OsL9EJWz9UY?t=0))
- Minimum bundle size goes from about 35.5 KB (v3) to about 7 KB (v4), roughly 5x smaller, per vendor. ([2:53](https://youtu.be/OsL9EJWz9UY?t=173))
- Task throughput is about 6.5x higher in v4 (vendor benchmark, not independently reproduced). ([2:53](https://youtu.be/OsL9EJWz9UY?t=173))
- Memory for 50,000 fibers drops from about 157 MB to about 22 MB (vendor benchmark). ([2:53](https://youtu.be/OsL9EJWz9UY?t=173))
- Launch blog states a 7.1 KB minimal bundle, while the migration guide says about 6.3 KB. ([5:00](https://youtu.be/OsL9EJWz9UY?t=300))
- Stable 4.0 had about 150,000 downloads on day one. ([5:00](https://youtu.be/OsL9EJWz9UY?t=300))
- Bug-fix support for 4.0 runs until September 2029. ([4:06](https://youtu.be/OsL9EJWz9UY?t=246))

## Hot takes
- The typed error channel is the real value of Effect, not the bundle size or runtime speed.
- Effect 4.0's headline numbers (bundle, throughput, memory, downloads) carry asterisks and should be reproduced before being trusted.
- Partial adoption of Effect can be worse than never adopting it, so small apps should skip it.
- Feeding the migration guide to a coding agent will probably work, since there is no official codemod.

## Tools mentioned
Effect 4.0 (npm package `effect`), Effect Schema, TypeScript 7, Bun, npm, Zod, FP-TS (merged into Effect)

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, where timeouts, retries and typed errors around subprocess calls are relevant, but the language is not confirmed as TypeScript. → *If ProsHarness is TypeScript, try a typed error and timeout wrapper around one Claude Code CLI call in a spike before adopting Effect; treat Effect 4.0 as unstable for AI, CLI and RPC modules.*
