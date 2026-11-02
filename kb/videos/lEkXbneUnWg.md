# The EASIEST Way To Switch From ESLint & Prettier to Biome — Ultracite

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `lEkXbneUnWg` · [watch](https://youtu.be/lEkXbneUnWg) · **date:** 2025-11-02 · **length:** 8:02 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Better Stack, Biome, shadcn
- **topics:** dev-tools, context-engineering, coding-agents · **tags:** biome, ultracite, linting, formatting, eslint, prettier, husky, pre-commit, ai-rule-files, mcp, typescript, cursor, claude-code

> Better Stack walks through Ultracite, a zero-config preset that sets up Biome (a Rust linter and formatter) with AI rule files, editor settings and pre-commit hooks in one init command.

## Summary
The host presents Biome, a Rust-based linter and formatter that replaces ESLint and Prettier, and Ultracite, a zero-config wrapper that installs and configures Biome in a project. Setup is one command (npx ultracite init, run with Bun in the video), followed by a wizard that asks for the package manager, editors, AI assistants and pre-commit hook tool. The generated Biome config is essentially just "extends ultracite", a highly opinionated preset covering strict TypeScript, ESLint-recommended rules, React, Next.js, Node and accessibility, plus formatting defaults such as two-space indentation. The host argues Ultracite is a helper rather than a new toolchain: the CLI wrappers are thin shims over biome check, and the preset can be removed without breaking the project. A distinctive feature is generated plain-English rule files for Claude and Cursor, which the host argues reduce lint fixes by steering the assistant before code is written. Ultracite also scaffolds Husky, lint-staged or lefthook pre-commit hooks (Husky runs npx ultracite format) and ships an MCP server so any chat client can query the rules. The video is a product walkthrough with no sponsor segment shown, and the speed claim is the vendor's own benchmark.

## Key ideas
- **Ultracite is a setup helper, not a new toolchain** — Its CLI commands are wrappers around biome check and biome check --write, and the Biome config only needs extends ultracite. Deleting the preset and package leaves the project working, and individual rules can be overridden in the Biome config. ([2:16](https://youtu.be/lEkXbneUnWg?t=136))
- **Biome is pitched as an all-in-one ESLint and Prettier replacement** — The host describes Biome as a fast Rust toolchain covering linting and formatting, claims the site benchmark shows it close to 35x faster than Prettier, and says that is the vendor's own figure. ([0:00](https://youtu.be/lEkXbneUnWg?t=0))
- **Generated AI rule files are the main differentiator** — The setup wizard writes plain-English rule files for each selected assistant (the host used Claude and Cursor). The argument is that an assistant that knows the rules writes code that needs fewer lint and format fixes afterwards, and the host complains that every agent wants its own markdown filename. ([3:20](https://youtu.be/lEkXbneUnWg?t=200))
- **Pre-commit hook scaffolding is the 'plays nicely with others' feature** — Ultracite installs and configures Husky, and the pre-commit hook runs a single npx ultracite format command. It also supports lint-staged and lefthook, though the host says those take more configuration. ([4:37](https://youtu.be/lEkXbneUnWg?t=277))
- **An MCP server brings the rules into any AI chat** — The host uses it in Claude Desktop, where it can quiz the assistant on specific rules and their rationale, and get rules into chats even when the tool does not support rule files. ([4:37](https://youtu.be/lEkXbneUnWg?t=277))
- **Setup writes editor settings into the project, not global config** — The wizard sets Biome as the formatter with format on save and format on paste in project-level editor settings (VS Code, Cursor, and Zed are mentioned). The Biome editor extension must still be installed. ([5:50](https://youtu.be/lEkXbneUnWg?t=350))
- **The preset is opinionated and can be edited rule by rule** — Rules cover strict TypeScript, ESLint-recommended behaviour where Biome supports it, React, Next.js, Node and accessibility, with formatting defaults such as two-space indentation and a maximum line width. The full rule set can be read in the GitHub config or in the generated AI rule files. ([2:16](https://youtu.be/lEkXbneUnWg?t=136))

## Techniques
- **Zero-config Biome bootstrap** — Run `npx ultracite init` (or `bunx ultracite init`, as in the video). In the wizard, pick the package manager, the editors to configure (VS Code, Cursor, Zed are offered), the AI assistants to generate rule files for, and the pre-commit tool (Husky, lint-staged or lefthook). It installs packages (ultracite, @biomejs/biome, husky) and writes the Biome config, editor settings, AI rule files and hook config. *When:* Starting a new JS/TS project, or retrofitting one, when you want consistent lint and format rules with minimal setup and no hand-written Biome config.
- **Biome config that only extends the preset** — The generated biome config just extends ultracite. Override individual rules in the same config file when the preset is too strict. Removing the extends line and the package keeps the project working because the preset is only a bundle of Biome rules. *When:* When you want Biome's behaviour without depending on an extra package, or need to tune rules for a codebase.
- **Thin CLI wrappers for lint and format** — `npx ultracite lint` wraps biome check. `npx ultracite format` wraps biome check --write and applies the fixes it can make. Use them in scripts or hooks in place of the raw Biome commands. *When:* For a shorter command in scripts and git hooks, or when you do not want to type the full Biome subcommands.
- **Pre-commit format gate via Husky** — Let Ultracite configure Husky so the pre-commit hook runs `npx ultracite format`. Committed code is then formatted automatically without a manual step. For lint-staged or lefthook, the host says the configuration is more involved, so check the generated files. *When:* When you want every commit formatted without relying on developers or agents to run the formatter.
- **Shift lint rules left into the agent's context** — Select the AI assistants during setup so the generated plain-English rule files (one per assistant, for example a Claude file and a Cursor file) are created. Keep the lint and format gate as a backstop, because the rules guide generation but do not guarantee compliance. *When:* When coding agents keep producing code that fails the project's lint or format rules and you want fewer fix-up rounds.
- **Expose rules through an MCP server** — Connect Ultracite's MCP server to an AI client such as Claude Desktop. The assistant can then look up specific rules and their rationale, and apply the rules in chats where project rule files are not loaded. *When:* For ad-hoc code snippets in chat tools that do not read project rule files, or when you want to ask why a rule exists.

## Numbers
- Biome benchmarks on the vendor site show it close to 35x faster than Prettier (host repeats this, unverified) ([0:00](https://youtu.be/lEkXbneUnWg?t=0))
- Setup needs one command: npx ultracite init ([0:00](https://youtu.be/lEkXbneUnWg?t=0))
- Ultracite default formatting includes two-space indentation and a max line width ([2:16](https://youtu.be/lEkXbneUnWg?t=136))

## Hot takes
- Ultracite is a helper rather than another JavaScript toolchain, and the host says removing it leaves the project working.
- Generated AI rule files reduce lint and format fixes later, and the host wants a single markdown standard across AI tools.
- Vendor benchmark speed claims are presented as the reason to switch, with no independent measurement shown.
- Video is a product walkthrough and does not weigh Biome's gaps against ESLint plugins or Prettier's ecosystem.

## Tools mentioned
Ultracite (npx ultracite init, lint, format), Biome (biome check, biome check --write), ESLint, Prettier, Husky, lint-staged, lefthook, Bun, shadcn/ui, VS Code, Cursor, Zed, Claude Code, Claude Desktop, Model Context Protocol (MCP)

## Relevance to our work
- **prosharness** (1/3): Generated per-assistant rule files for Claude Code and Cursor are a context-engineering pattern (rules as agent context), but ProsHarness is a Claude Code CLI harness, not a JS/TS codebase, so the Biome tooling itself does not apply. → *Compare Ultracite's generated per-assistant rule files with the CLAUDE.md layout ProsHarness uses; only worth a look if any ProsHarness-adjacent code is JS/TS.*
