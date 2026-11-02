# TypeScript 5.9: Lazy Imports Are Finally Here (and more)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `BkzKn4EYjcM` · [watch](https://youtu.be/BkzKn4EYjcM) · **date:** 2025-11-02 · **length:** 4:40 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** Bernard · **orgs:** Better Stack, Microsoft
- **topics:** dev-tools · **tags:** typescript, tsc, tsconfig, import-defer, module-resolution, nodenext, node20, esm, typescript-7, go-compiler, expandable-hovers

> A 4-minute Better Stack news rundown of TypeScript 5.9: a cleaner tsc --init, nodenext as the new default, the import defer syntax, a stable node20 module mode, expandable hovers in preview, and a look ahead to TS 6 and a Go-based TS 7.

## Summary
Better Stack's host Bernard walks through the TypeScript 5.9 release in a short news-style video. The tsc --init command now generates a much shorter tsconfig instead of a full file of commented-out settings, and the generated config defaults to the nodenext module setting. The headline feature is import defer, which loads and evaluates a module only when one of its exports is first accessed, aimed at reducing startup time. The presenter warns that tsc does not transform this syntax, so runtimes without support will throw syntax errors, and that it requires the module setting to be esnext or preserve. TypeScript 5.9 also adds a node20 module mode, presented as a stable alternative to nodenext that will not change over time and that implies an ES2023 target. Expandable hovers (quick info) are in preview. The video closes by saying TS 6 will be a transitional release ahead of TS 7, a compiler being rewritten from JavaScript to Go and referred to as "Corsa". The content is accurate but shallow, with no benchmarks and no hands-on demo.

## Key ideas
- **tsc --init now writes a much cleaner tsconfig instead of a full file of commented-out settings.** — The presenter argues most developers rely on autocomplete or the docs rather than reading every commented setting, so a short file is the change. ([0:00](https://youtu.be/BkzKn4EYjcM?t=0))
- **The generated tsconfig now defaults to the nodenext module setting.** — Stated as a way to ensure files are scoped as modules and avoid common setup headaches. ([0:00](https://youtu.be/BkzKn4EYjcM?t=0))
- **import defer loads and runs a module only when one of its exports is accessed.** — Pitched for reducing startup time or deferring logic-heavy modules until needed. ([0:00](https://youtu.be/BkzKn4EYjcM?t=0))
- **import defer is not downleveled, so unsupported runtimes will hit a syntax error.** — tsc emits the syntax as-is; it is only allowed when the module setting is esnext or preserve. The presenter says to check runtime support first. ([1:12](https://youtu.be/BkzKn4EYjcM?t=72))
- **A node20 module mode is added as a stable alternative to nodenext.** — It is meant to mirror Node.js 20 behavior and is said not to change in the future; it also implies an ES2023 target. ([2:21](https://youtu.be/BkzKn4EYjcM?t=141))
- **Expandable hovers (quick info) are previewed in 5.9.** — They let you expand type information for parameters and interfaces without jumping to the definition. The presenter notes it is preview and may not work in every case. ([2:21](https://youtu.be/BkzKn4EYjcM?t=141))
- **TS 6 is described as a transitional release before TS 7, a compiler moving from JavaScript to Go.** — The presenter says the Go-based compiler is faster to compile, and mentions the codename Corsa. No numbers are given. ([3:24](https://youtu.be/BkzKn4EYjcM?t=204))

## Techniques
- **Deferred module loading with import defer** — Write `import defer * as ns from "<module>"` (the only supported form, per the presenter; named imports are not allowed). The module is evaluated on first access to an export. Set the TS module option to esnext or preserve, and confirm the target runtime supports the syntax, because tsc does not down-level it. *When:* Startup-heavy or logic-heavy modules that are not needed on every code path, where the runtime is known to support the syntax.
- **Node 20 module mode for stable Node 20 semantics** — Set the module option to the Node 20 mode instead of nodenext. The presenter says it implies target ES2023 and will not change in future releases. The transcript does not spell out the exact setting value, so check the TS 5.9 release notes for it. *When:* When you want module behavior pinned to Node 20 rather than tracking the latest nodenext behavior.
- **Bootstrap a tsconfig with tsc --init and rely on autocomplete** — Run tsc --init on 5.9 to get the shorter generated config, which defaults to nodenext, and use editor autocomplete or the docs for the settings that are no longer listed as commented-out lines. *When:* Starting a new TypeScript project on 5.9 and wanting a minimal config.

## Numbers
- Video length is 4:40 and covers a single release. ([0:00](https://youtu.be/BkzKn4EYjcM?t=0))
- The node20 module mode implies an ES2023 target. ([2:21](https://youtu.be/BkzKn4EYjcM?t=141))
- No benchmarks or timings are given for the claimed faster compile in the Go-based TS 7. ([3:24](https://youtu.be/BkzKn4EYjcM?t=204))

## Hot takes
- The presenter says the Go-based TS 7 compiles faster but gives no measurements.
- import defer is pitched as a startup-time win, but the presenter warns it will throw syntax errors on runtimes without support.
- A 4-minute recap of release notes with no hands-on demo; the content is accurate but thin, so quality is capped at 2.

## Tools mentioned
TypeScript 5.9, tsc, Node.js 20, Node.js (nodenext module mode), TypeScript 6 (announced as transitional), TypeScript 7 (Go-based compiler, codename Corsa)
