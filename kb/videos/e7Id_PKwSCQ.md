# TypeScript 7 is HERE (The Go Update)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `e7Id_PKwSCQ` · [watch](https://youtu.be/e7Id_PKwSCQ) · **date:** 2026-07-02 · **length:** 4:59 · **format:** news · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Microsoft
- **topics:** dev-tools · **tags:** typescript, typescript-7, go-port, type-checking, build-performance, parallelism, tsc, playwright, upgrade-path, parcel-watcher, compatibility

> Better Stack walks through the TypeScript 7 release candidate, a Go port of the compiler: a Playwright type-check drops from about 6s to 0.87s, new checkers and builders flags add parallelism, and the speaker reports no breaking changes from TS 6.

## Summary
TypeScript has published a release candidate for version 7, which is a line-by-line port of the TypeScript compiler from TypeScript to Go. The speaker says the stable release is about a month away, with a stable programmatic API landing in 7.1. On the Playwright repo (about 1,400 files and 500k lines), a type check took about 6 seconds on TS 6 and 0.87 seconds on the TS 7 RC, with identical errors. Single-threaded TS 7 still ran about 3x faster than TS 6 (around 2 seconds). TS 7 adds a checkers flag (default 4) for parallel type-checker workers and a builders flag for parallel project-reference builds, both at the cost of memory. Watch mode needed the Parcel file watcher ported from C++ to Go, because Go's standard library has no file watching. The speaker says there are no breaking changes going from 6 to 7, but upgrading from 5 means moving to 6 first, since TS 6 removed the ES5 target and baseUrl, deprecated AMD/UMD/SystemJS modules, and made strict the default. The only language change is that template literal types now split on Unicode code points instead of UTF-16 units. A compatibility package allows TS 6 and 7 to run side by side.

## Key ideas
- **TypeScript 7 RC is a port of the TypeScript compiler from TypeScript to Go; the port was done largely line by line, so behavior is intended to match TS 6, and the release is claimed to be about 10x faster.** — The speaker says the team began the port about a year ago, reasoning that JavaScript is poorly suited to CPU-bound type checking. The 10x figure is the release claim; the speaker's own measurement is covered in the next item. ([0:00](https://youtu.be/e7Id_PKwSCQ?t=0))
- **On the Playwright repo, the TS 7 RC type-checks much faster with identical results.** — TS 6 took about 6s and TS 7 RC about 0.87s across roughly 1,400 files and 500k lines. The error count and error set matched, and the same files were checked. ([0:56](https://youtu.be/e7Id_PKwSCQ?t=56))
- **Speedup has two sources: native Go code, and shared-memory parallelism across cores, which the single-threaded JS compiler could not use.** — A single-threaded mode is available via a flag for debugging or constrained machines. In that mode, the same Playwright check took about 2s, still roughly 3x faster than TS 6. ([0:56](https://youtu.be/e7Id_PKwSCQ?t=56))
- **New tuning knobs: a checkers flag (default 4) and a builders flag for project references, which multiply.** — Setting checkers to 8 on Playwright cut another roughly third off the time. The speaker warns that builders times checkers can mean up to 16 concurrent type checkers at four each, and that more workers cost more memory. ([0:56](https://youtu.be/e7Id_PKwSCQ?t=56))
- **Watch mode was the hard part of the port because Go's standard library has no file-watching API and third-party options were unstable or not cross-platform.** — The team ported the parts they needed of the Parcel file watcher (C++, used by VS Code) to Go. The speaker says it works smoothly. ([2:13](https://youtu.be/e7Id_PKwSCQ?t=133))
- **The speaker reports no breaking changes from 6 to 7, but says that upgrading from 5 should go through 6 first.** — TS 6 removed the ES5 target and baseUrl, deprecated the AMD, UMD and SystemJS module systems, and made strict true the default. Module now defaults to ESNext, and target to the current stable ECMAScript version before ESNext. ([2:13](https://youtu.be/e7Id_PKwSCQ?t=133))
- **The one language-level change in the 7 release notes is that template literal types split on whole Unicode code points rather than UTF-16 code units.** — Before, an emoji could be split in half when used with template literal type inference, producing broken head and tail types. The speaker presents this as a minor fix that few people will have hit. ([3:27](https://youtu.be/e7Id_PKwSCQ?t=207))
- **Release timing and compatibility: stable is expected in about a month, a stable programmatic API arrives in 7.1, and a compatibility package lets TS 6 and 7 coexist.** — The programmatic API is what tooling authors build on, so tools that depend on it may wait for 7.1. Side-by-side install avoids conflicts during migration. ([3:27](https://youtu.be/e7Id_PKwSCQ?t=207))

## Techniques
- **Benchmark a type check across TS versions on your own repo** — Run the same type-check command with the TS 6 and TS 7 RC compilers without changing anything else, and compare wall-clock time and the error output. The speaker verified that the error set and file count matched before trusting the timing. The exact command is not shown in the video. *When:* Before upgrading a large codebase, or when deciding whether a CI type-check step is worth tuning.
- **Single-thread TS 7 for debugging or constrained machines** — Use the TS 7 single-threaded flag. The exact flag name is not stated in the video; check the TS 7 docs for it. *When:* Debugging type-checker behavior, or on a machine with few cores or limited memory. Still about 3x faster than TS 6 on the Playwright repo.
- **Tune checkers and builders for parallel type checking** — Set the checkers option (default 4) to raise the number of parallel type-checker workers, and the builders option to set how many project-reference projects build in parallel. Their product is the peak number of concurrent type checkers. Watch memory use when raising either. *When:* Large monorepos with many CPU cores and spare memory. The speaker saw about a third more speedup going from 4 to 8 checkers on Playwright.
- **Upgrade path from TS 5 to TS 7** — Go to TS 6 first and fix the breaking changes there: ES5 target removed, baseUrl removed, AMD/UMD/SystemJS module output deprecated, strict now on by default, module now defaults to ESNext. Then bump to TS 7. *When:* Migrating a legacy project from TS 5 to TS 7.
- **Run TS 6 and TS 7 side by side** — Install the TS 7 compatibility package so both compilers can coexist in one project or workspace during migration. *When:* Migrating a monorepo gradually, or when some tooling still depends on the TS 6 programmatic API before 7.1 ships a stable one.

## Numbers
- Release claim: TypeScript 7 is about 10x faster than TS 6 (not measured by the speaker). ([0:00](https://youtu.be/e7Id_PKwSCQ?t=0))
- Playwright repo: TS 6 type check about 6s vs TS 7 RC 0.87s, about 1,400 files and about 500k lines, identical error set. ([0:56](https://youtu.be/e7Id_PKwSCQ?t=56))
- Playwright repo, TS 7 single-threaded: about 2s, roughly 3x faster than TS 6. ([0:56](https://youtu.be/e7Id_PKwSCQ?t=56))
- checkers default is 4; setting it to 8 cut roughly another third off the Playwright type check. ([0:56](https://youtu.be/e7Id_PKwSCQ?t=56))
- With builders and checkers at 4 each, up to 16 type checkers can run concurrently; more workers increase memory use. ([2:13](https://youtu.be/e7Id_PKwSCQ?t=133))
- Stable TS 7 release expected in about a month; stable programmatic API in 7.1. ([3:27](https://youtu.be/e7Id_PKwSCQ?t=207))

## Hot takes
- Title says TypeScript 7 is HERE, but the video covers a release candidate, and the speaker says stable is about a month away.
- The 10x figure is the release's claim. The only measurement in the video is one repo, one run, with no method given: about 7x wall-clock on Playwright (6s to 0.87s), and about 3x single-threaded.
- The claim of no breaking changes from 6 to 7 comes from reading the release blog, not from testing a migration.
- The speaker calls the template-literal Unicode fix something few people will ever hit; the speaker's own framing suggests it is low-impact.

## Tools mentioned
TypeScript 7 (RC), TypeScript 6, TypeScript 5, Go, Playwright, Parcel file watcher, VS Code, Claude, Bun
