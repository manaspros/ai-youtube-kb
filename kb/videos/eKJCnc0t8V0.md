# Mise: The BEST Way to Manage Versions of Node, Python, Go (and Much More...)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `eKJCnc0t8V0` · [watch](https://youtu.be/eKJCnc0t8V0) · **date:** 2025-11-02 · **length:** 6:13 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** dev-tools · **tags:** mise, version-managers, polyglot-toolchain, npm, task-runner, env-vars, dev-environment, reproducible-setup

> Walkthrough of mise, a Rust polyglot tool and version manager, shown as a per-project toolchain file, with npm packages, tasks, scoped tools and shared env vars; a reasonable intro, with the narrator's own caveats.

## Summary
The host introduces mise (transcript spells it "Mies"), a Rust-based polyglot manager that replaces per-language version managers and some package-manager use for installing dev tools. He SSHes into a fresh Linux server, installs mise, runs mise doctor, activates it for bash, and installs zoxide, which gets written to a committable config.toml so teammates can run mise install. He shows listing and upgrading tools (mise registry, mise upgrade --bump, pinning Node versions), installing npm CLIs such as vitest through mise, and defining a tasks block similar to npm scripts that runs tests in selected directories. Tools can be scoped to a single project directory (Go is visible only inside that project). Environment variables can be shared across projects through a separate mise.toml, loaded from .env files, and redacted for CI logs. The host concludes that project dependencies should still go through npm and package.json (for deployment platforms like Vercel), and that mise suits global CLIs such as pm2; the claim that mise is faster and safer than asdf is not benchmarked.

## Key ideas
- **One committable per-project config replaces per-language version managers** — mise records installed tools and versions in config.toml, so a colleague or a fresh server can run mise install to get the same toolchain. The host presents this as the main benefit. ([0:00](https://youtu.be/eKJCnc0t8V0?t=0))
- **Tools from the registry install globally or per project** — The demo installs zoxide on a fresh server, then shows it written to config.toml. mise registry lists available tools (SQLite, OpenCode, GitHub CLI, ClaudeSquad, and more). ([0:00](https://youtu.be/eKJCnc0t8V0?t=0))
- **Version bumps and pins are explicit** — mise upgrade --bump moves a tool to its latest version (Node goes to 24). A version can also be set by hand in the TOML and applied with mise install (the demo pins Node 23). ([1:23](https://youtu.be/eKJCnc0t8V0?t=83))
- **npm CLIs can be installed through mise** — Global npm CLIs like vitest are installed and run through mise, which removes the need for a global npm install step. ([1:23](https://youtu.be/eKJCnc0t8V0?t=83))
- **Tasks give per-directory npm-script-style commands** — A tasks block in config.toml defines a named test task that runs vitest only in selected directories, excluding the Go project. ([2:43](https://youtu.be/eKJCnc0t8V0?t=163))
- **Tool versions can be scoped to one project** — Running mise use go inside the Go project makes go available only in that directory tree. go is not found from the root. ([2:43](https://youtu.be/eKJCnc0t8V0?t=163))
- **Shared env vars and secrets live in a separate mise.toml** — Variables set through mise are exported as shell variables to every project. A .env file can be loaded, and values can be redacted so they stay masked in CI logs. ([4:08](https://youtu.be/eKJCnc0t8V0?t=248))
- **Keep project dependencies in npm, not mise** — The host says project packages like React or Next.js should stay in package.json, so deploy platforms can install them. mise fits global CLIs like pm2 and killport. ([5:05](https://youtu.be/eKJCnc0t8V0?t=305))

## Techniques
- **Pin a repo's toolchain in config.toml** — In the project, run mise use node (the demo pins a specific Node version). Commit the generated config.toml. On a new machine or server, run mise install to get the same tools. mise ls lists what is installed, and mise tool node shows details for one tool. *When:* Sharing a repo with teammates, or rebuilding a server or laptop with the same dev tools.
- **Install a CLI from the registry on a fresh box** — Run mise install-style setup after installing mise, check it with mise doctor, and activate it for the shell (the demo uses bash). Then install a registry tool such as zoxide. The exact install command was not fully shown on screen, so check mise's docs for the exact form. *When:* Replacing a Homebrew-managed toolset on a remote Linux server or a new machine.
- **Bump tools to latest, or pin a specific version** — mise upgrade --bump moves tools to their latest versions. To pin, edit the version in config.toml by hand, then run mise install. *When:* Routine updates, or pinning Node or Go to a version the project needs.
- **Install npm CLIs as mise-managed tools** — Install an npm package through mise (the demo installs vitest; the transcript caption reads "npm vtest", and the exact prefix syntax was not shown). Once installed, the command is available in the scoped directories. *When:* Global test or lint CLIs you want version-controlled per repo, without a global npm install.
- **Define npm-script-style tasks in config.toml** — Add a tasks block to config.toml with a named task (demo: test) and a shell script that runs vitest in chosen directories. The demo runs it through mise, so it covers only the directories listed in the script. *When:* Running the same command across several subdirectories of a monorepo, excluding others.
- **Scope a tool to a single project** — cd into the project and run mise use go. The tool is active only inside that directory tree, and outside it the command is not found. *When:* Projects that need different toolchain versions side by side.
- **Share env vars across projects with mise.toml** — Set a variable through mise (the demo's command was not fully shown on screen; it writes to mise.toml, separate from config.toml). Check it with mise env. To reuse an existing .env file, point mise at it. For CI, mark values as redacted so they are masked in logs. *When:* Shared deployment variables across several repos, or secrets that should be masked in CI logs.
- **Split global CLIs from project dependencies** — Install global CLIs such as pm2 or killport with mise. Keep React, Next.js and other project packages in npm's package.json so deploy platforms can install them. *When:* Deciding what belongs in mise and what belongs in a project's package manager.

## Numbers
- Video length is 6:13, a short overview with no benchmark data. ([0:00](https://youtu.be/eKJCnc0t8V0?t=0))
- mise upgrade --bump takes Node from 23 to 24 in the demo. ([1:23](https://youtu.be/eKJCnc0t8V0?t=83))
- Go is shown as version 1.250 in the auto-captions, most likely 1.25.0. ([2:43](https://youtu.be/eKJCnc0t8V0?t=163))
- The narrator says mise is faster and more secure than the Bash and Go versions of asdf, with no benchmark shown. ([5:05](https://youtu.be/eKJCnc0t8V0?t=305))

## Hot takes
- The title and intro say mise "will change the way you develop forever", which is hype. The demo itself is a modest feature tour.
- Narrator's own view: mise replaces global CLI installs, but project dependencies such as React should stay in npm and package.json for deployment.
- Speed and security claims against asdf are asserted without benchmarks or evidence.
- The npm-package feature is pitched as a way to skip node_modules, and the narrator then walks that back for project-level packages.

## Tools mentioned
mise (polyglot tool and version manager, written in Rust; author Jeff Dickey), zoxide, Node.js (pinned to 23, bumped to 24), Go (shown as 1.250 in the auto-captions, likely 1.25.0), npm, vitest, pm2, killport (spoken as KillPorts), React, Next.js, Vercel, asdf (compared), Homebrew (spoken as Brew), .NET, Cargo, Ruby gems, SQLite, OpenCode, GitHub CLI, ClaudeSquad, config.toml, mise.toml, .env

## Relevance to our work
- **agentos** (1/3): A per-repo mise.toml could pin Python, Go and Node versions for benchmark and load-test harnesses, making runs reproducible on the RTX 5090 setup. The video does not cover GPU, CUDA or Python-specific behavior. → *Try mise on the AgentOS benchmark or load-test repo: pin Python and Node versions in mise.toml and check whether a fresh checkout reproduces the same toolchain with mise install.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, which is an npm package. mise can pin that CLI version per project through its npm support, and its tasks block may suit a loop or schedule runner. Neither was tested in the video. → *Test whether mise can pin the Claude Code CLI version and the ProsHarness dependencies per repo, and whether a tasks entry can run a ProsHarness loop for consistent setup.*
