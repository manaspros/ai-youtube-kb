# Bun 1.2 is a HUGE update (its a bundler now!)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `rtj-zd93Vfs` · [watch](https://youtu.be/rtj-zd93Vfs) · **date:** 2025-11-02 · **length:** 6:43 · **format:** news · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Bun
- **topics:** dev-tools, vibe-coding-app-building · **tags:** bun, javascript, typescript, bundler, package-manager, lockfile, s3, postgres, node-compat, testing, bun-test, standalone-executable, release-notes

> Walkthrough of Bun 1.2's release notes: HTML-import bundling, built-in Postgres and S3 clients, a text lockfile, Node compatibility gains, a richer test runner, and cross-compiled executables. Mostly vendor-reported numbers.

## Summary
Better Stack summarizes the Bun 1.2 release as a near-2.0 update. The main claim is that Bun can now cover a full-stack app (bundled frontend, HTTP server, database driver, API routes and an S3 client) with minimal configuration. Headline features are HTML imports with a built-in CSS bundler, a built-in Postgres client (MySQL promised), a built-in S3 client that issues presigned URLs, and a text-based lockfile replacing the binary one. On the package-manager side the video covers JSONC package.json, npmrc support, bun outdated, bun publish, and local dependency patches stored as .patch files. Node.js compatibility gets attention: the full Node test suite now runs on Bun builds with about 90% passing, plus HTTP/2, dgram, cluster, zlib and native-addon support. The test runner gains JUnit and LCOV output, inline snapshots and test.only. Other items are musl/Alpine support, cross-platform standalone compilation, bytecode caching, several ES features, and performance figures. The speaker is reading from release notes and shows no live demo or benchmark setup, so every number is the vendor's claim.

## Key ideas
- **Bun 1.2 is pitched as a full-stack runtime: bundled frontend, HTTP server, DB driver, API routes and S3 client without a separate toolchain.** — The speaker frames it as replacing webpack-style configs with a single HTML import. Stated as a vendor claim, not demonstrated. ([0:00](https://youtu.be/rtj-zd93Vfs?t=0))
- **HTML imports: Bun.serve bundles the script and link tags of an imported HTML file and serves the result as static routes.** — The CSS parser and bundler were rewritten from Rust to Zig for integration. It minifies and combines CSS, and Tailwind works through a Bun plugin in about three lines. Static routes are described as up to 40% faster than the manual approach. ([0:00](https://youtu.be/rtj-zd93Vfs?t=0))
- **Built-in Postgres client, API-compatible with postgres.js as a drop-in replacement, with prepared statements, pooling and pipelining. MySQL is said to be coming.** — Speaker claims it is about 50% faster than postgres.js. SQLite has been built in since Bun 1.0. ([1:18](https://youtu.be/rtj-zd93Vfs?t=78))
- **Built-in S3 client: read, write, delete, presigned URLs, and s3:// URLs usable in fetch or bundles. Bundle serving with S3 files generates presigned URLs rather than proxying bytes through the server.** — Claimed 5x faster than the AWS SDK on Node.js. Multipart uploads for large files are automatic. The bandwidth argument is that the server never relays file bytes. ([1:18](https://youtu.be/rtj-zd93Vfs?t=78))
- **Text-based lockfile replaces the binary one so dependency changes are reviewable in git and merge conflicts are easier to resolve.** — Speaker says it is about 30% faster than the old lockfile. Also listed: JSONC support in package.json (comments allowed), full npmrc support, bun outdated, and bun publish to npm. ([2:31](https://youtu.be/rtj-zd93Vfs?t=151))
- **Local dependency patching without forking: patches are saved as plain .patch files in the repo for review and sharing.** — Covered briefly; the speaker does not show the exact command. ([2:31](https://youtu.be/rtj-zd93Vfs?t=151))
- **Node compatibility: the full Node.js test suite runs on Bun builds with about 90% passing. HTTP/2, dgram (UDP), cluster and zlib were added, and V8 C++ APIs are emulated so native addons can load.** — Speaker says Express runs about 3x faster over HTTP/2 than on Node.js, and zlib compression is about 2x faster. The native-addon claim matters because it targets packages with compiled extensions. ([3:51](https://youtu.be/rtj-zd93Vfs?t=231))
- **bun test gains JUnit and LCOV reporters for CI (Jenkins, GitLab), inline snapshots, test.only, new expect matchers, and better error reporting for uncaught exceptions between tests.** — Note that Bun 1.2 also adds musl support for Alpine and similar minimal Docker images, with a performance caveat the speaker does not expand on. ([3:51](https://youtu.be/rtj-zd93Vfs?t=231))
- **Standalone executables can be cross-compiled (Windows from Linux and back), with bytecode caching for faster startup and Windows icon and console options. The release also adds several ES features: import attributes, `using` declarations, Promise.withResolvers, iterator helpers and new array methods.** — Speaker claims ESLint starts about 2x faster with bytecode caching. Using declarations are described as Python-style context managers for deterministic resource cleanup. ([5:11](https://youtu.be/rtj-zd93Vfs?t=311))

## Techniques
- **Serve a bundled frontend straight from Bun.serve via an HTML import** — Import the app's HTML file into the Bun.serve routes instead of running a separate bundler. Bun bundles its script and link tags, minifies CSS, and serves them as static routes. Tailwind is added through the Bun Tailwind plugin. The exact import syntax is not shown on screen. *When:* Small-to-medium full-stack apps where you want to drop webpack/Vite-style config and keep frontend and API in one process.
- **Presigned S3 URLs so the server never relays file bytes** — Use Bun's built-in S3 client with s3:// URLs in fetch or bundled assets. The server generates presigned URLs and clients fetch or upload directly to S3. Large uploads use automatic multipart. *When:* Apps that serve or accept large user files and want to cut server bandwidth and CPU.
- **Put dependency pins and reasons in package.json comments** — With JSONC support in package.json, add a comment next to a pinned or workaround dependency explaining why it is pinned. *When:* Teams that pin a broken transitive or direct dependency and want the reason visible months later.
- **Review dependency changes as text diffs** — The text-based lockfile produces readable git diffs. Review and resolve lockfile conflicts as normal text instead of regenerating a binary file. *When:* PR-heavy repos where lockfile churn currently blocks review or causes merge conflicts.
- **Patch a broken dependency locally and commit the .patch file** — Make the fix in the installed dependency, let Bun record it as a .patch file in the repo, and commit that file. Exact command is not shown in the video. *When:* An upstream bug blocks you but forking the package is not worth it.
- **Wire CI test reporting through JUnit or LCOV output** — Use bun test's JUnit or LCOV reporter so Jenkins or GitLab can ingest results and coverage. Reporter flags are not shown in the video. *When:* CI systems that expect JUnit XML or LCOV and where Bun is the test runner.
- **Cross-compile a standalone executable and enable bytecode caching** — Build Windows executables from Linux or macOS and vice versa with Bun's standalone compiler. Enable the bytecode caching option to cut startup time for large CLI tools such as ESLint. Flag names are not shown. *When:* Shipping a single-binary CLI to several platforms where cold start matters.

## Numbers
- Static routes served from HTML imports are up to 40% faster than the manual approach (vendor claim) ([0:00](https://youtu.be/rtj-zd93Vfs?t=0))
- Built-in Postgres client is about 50% faster than postgres.js (vendor claim) ([1:18](https://youtu.be/rtj-zd93Vfs?t=78))
- Built-in S3 client is about 5x faster than the AWS SDK on Node.js (vendor claim) ([1:18](https://youtu.be/rtj-zd93Vfs?t=78))
- Text lockfile is about 30% faster than the old binary lockfile (vendor claim) ([2:31](https://youtu.be/rtj-zd93Vfs?t=151))
- About 90% of the Node.js test suite passes on Bun builds (speaker's figure from release notes) ([2:31](https://youtu.be/rtj-zd93Vfs?t=151))
- Express over HTTP/2 about 3x faster than on Node.js (vendor claim) ([3:51](https://youtu.be/rtj-zd93Vfs?t=231))
- zlib compression about 2x faster (vendor claim) ([3:51](https://youtu.be/rtj-zd93Vfs?t=231))
- ESLint startup about 2x faster with bytecode caching (vendor claim) ([5:11](https://youtu.be/rtj-zd93Vfs?t=311))
- path.resolve about 30x faster; fetch DNS resolution about 2x faster; JSON parse up to 4x faster; Bun.serve about 2x throughput (vendor claims) ([5:11](https://youtu.be/rtj-zd93Vfs?t=311))

## Hot takes
- The 'feels like Bun 2.0' framing and 'best package manager' claim are hype. The video reads release notes and shows no live demo, benchmark setup or independent measurement, so every number is a vendor claim.
- Presenting '90% of the Node test suite passing' as a win skips that roughly 10% still fails. For teams running Node-only packages, that gap matters more than the headline.
- The speaker warns about musl performance implications but does not explain them, which is a loose end for anyone deploying on Alpine.
- Quality is 3 rather than lower: the feature list is accurate and specific enough to act on, but the content is a release summary, not practitioner testing.

## Tools mentioned
Bun 1.2, Bun.serve, Bun SQL (Postgres client), postgres.js, Bun S3 client, AWS SDK for JavaScript, Bun test, bun outdated, bun publish, Tailwind CSS, Bun Tailwind plugin, Express, ESLint, Node.js, npm, Alpine Linux, Docker, JavaScriptCore, Jenkins, GitLab, JUnit, LCOV, Zig, Rust

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, which is Node-based. If ProsHarness is JS/TS, Bun's Node compatibility and CI-friendly test output could matter, but only after checking its Node API usage. → *If ProsHarness is JS/TS, try running its test suite under Bun 1.2 and check Bun's JUnit reporter for CI, after confirming the Node APIs it uses (child_process, fs, streams) are covered.*
