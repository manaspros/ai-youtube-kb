# Bun.js Just Got WAY Faster (1.2.21  Update)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ptT8mFkm7z8` · [watch](https://youtu.be/ptT8mFkm7z8) · **date:** 2025-11-02 · **length:** 6:16 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** Bernard · **orgs:** Bun, Better Stack
- **topics:** dev-tools · **tags:** bun, javascript-runtime, bun-test, lockfile, yarn-migration, bun-sql, mysql, postgres, sqlite, yaml, postmessage, abortsignal, idle-cpu, bun-secrets, release-notes, zig

> Better Stack walkthrough of Bun 1.2.20 and 1.2.21 release notes: yarn-to-bun.lock migration, faster AbortSignal timeouts and postMessage, bun test return-value matchers, unified SQL client, native YAML, idle CPU fix.

## Summary
The video narrates the Bun 1.2.20 and 1.2.21 release notes from November 2025, mostly by reading them out with short demos of the new bun test matchers. Headline changes are an automatic yarn-to-bun.lock migration that preserves resolved versions, an AbortSignal timeout reimplemented on the setTimeout mechanism (said to be 40x faster), and faster worker messaging via postMessage. A new bun test matcher set asserts mock return values, and a single Bun SQL client now covers PostgreSQL, MySQL, MariaDB and SQLite with a Zig-written MySQL driver. Other items are a fix that stops the server from firing a per-second timer when idle, native YAML import and parsing, Bun.secrets using OS-native credential storage, and about 69 fixed issues. The presenter also announces this is his last video for the channel. Most performance numbers are the release notes' own claims and are not independently benchmarked on screen.

## Key ideas
- **Bun 1.2.20 and 1.2.21 both shipped in the same month; the video covers the highlights rather than the full changelog.** — Speaker says about 69 issues were fixed across the two releases and that he cannot cover them all; the full list is in Bun's blog, linked in the description. ([0:00](https://youtu.be/ptT8mFkm7z8?t=0))
- **Bun now migrates a yarn.lock to bun.lock automatically, keeping the resolved dependency versions.** — Pitched as making a move from yarn to Bun easier. The video shows no commands, so the exact trigger (install vs. a separate step) is not stated. ([0:00](https://youtu.be/ptT8mFkm7z8?t=0))
- **AbortSignal timeouts were reimplemented on the same mechanism as setTimeout and are said to be about 40x faster.** — The speaker links this to sharper async behaviour and immediate cancellation of in-flight fetch requests. ([0:00](https://youtu.be/ptT8mFkm7z8?t=0))
- **bun test gained three return-value matchers for mock functions, letting you target any call, the last call, or the nth call.** — Demoed on mocks that return an object, a string based on input, and input multiplied by 10. Matcher names are reconstructed from garbled auto-captions, so check the exact spelling in the Bun docs. ([1:03](https://youtu.be/ptT8mFkm7z8?t=63))
- **Bun SQL is one client for PostgreSQL, MySQL, MariaDB and SQLite with zero external dependencies, using the same API across them.** — The MySQL/MariaDB driver is written in Zig and is claimed to be up to 9x faster than the mysql2 package on Node.js. No code is shown for the unified client. ([2:05](https://youtu.be/ptT8mFkm7z8?t=125))
- **postMessage between workers is far faster for large payloads, and idle servers no longer burn CPU on a per-second timer.** — Worker messaging is claimed up to 500x faster for large strings with about 20x less memory. The server used to refresh the HTTP Date header every second; now that timer runs only while requests are in flight. ([3:06](https://youtu.be/ptT8mFkm7z8?t=186))
- **Bun now imports, bundles, requires and parses YAML natively, with the parser also written in Zig.** — YAML files can be imported like modules and accessed with dot notation. A built-in yaml module exposes a parse function. The speaker says Bun will be 100% Zig, and asks viewers to quote him. ([4:06](https://youtu.be/ptT8mFkm7z8?t=246))
- **One release-to-release benchmark in the video drops from about 2 seconds (1.2.19) to 0.02 seconds (1.2.21).** — The on-screen benchmark is not named in the transcript, so the workload behind the number is unknown. ([4:06](https://youtu.be/ptT8mFkm7z8?t=246))
- **Bun.secrets now uses OS-native credential storage.** — Mentioned briefly among smaller fixes such as a scrollable bun update UI and new filters for bun audit. ([5:07](https://youtu.be/ptT8mFkm7z8?t=307))

## Techniques
- **Migrate a yarn project to bun.lock** — Per the release notes read in the video, Bun converts yarn.lock to bun.lock automatically and keeps the resolved versions. The video shows no commands, so verify the trigger in Bun's docs before relying on it. *When:* Moving an existing yarn-based project to Bun while keeping dependency versions pinned.
- **Assert mock return values with the three bun test matchers** — Use the return-value matcher for 'returned this value at least once' (any call), the last-returned matcher for the most recent call, and the nth-returned matcher to pin a specific call number. Matcher names are inferred from garbled captions, so confirm them in the docs. Demo: a mock called with 1, 2, 3 that returns input times 10 has its second call checked for 20. *When:* Writing precise tests for mocks whose output changes between calls, instead of only checking call arguments.

## Numbers
- AbortSignal timeout is about 40x faster after reimplementation on the setTimeout mechanism (release notes, as read by speaker). ([0:00](https://youtu.be/ptT8mFkm7z8?t=0))
- Worker postMessage up to 500x faster for large strings, with about 20x less memory use. ([3:06](https://youtu.be/ptT8mFkm7z8?t=186))
- MySQL/MariaDB driver in Bun SQL up to 9x faster than mysql2 on Node.js (vendor benchmark, as stated). ([2:05](https://youtu.be/ptT8mFkm7z8?t=125))
- Benchmark from 1.2.19 to 1.2.21 drops from about 2 seconds to 0.02 seconds (benchmark not named). ([4:06](https://youtu.be/ptT8mFkm7z8?t=246))
- About 69 issues fixed across these releases. ([4:06](https://youtu.be/ptT8mFkm7z8?t=246))

## Hot takes
- Speaker claims Bun will be written 100% in Zig; this is his prediction, not a stated project plan.
- Quality capped at 2: this is mostly a narrated changelog with vendor-supplied benchmarks and no hands-on depth, and the captions garble several API names.
- The 0.02-second benchmark and the 9x and 500x speedups are vendor claims shown without methodology.

## Tools mentioned
Bun 1.2.20, Bun 1.2.21, bun test, bun install, Bun SQL, bun update, bun audit, Bun.secrets, bun.lock, yarn, mysql2, Node.js, MySQL, MariaDB, SQLite, PostgreSQL, Zig, setTimeout, fetch
