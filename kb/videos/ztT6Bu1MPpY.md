# Generate Multiple Cursor Rules with ONE CLICK!

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `ztT6Bu1MPpY` · [watch](https://youtu.be/ztT6Bu1MPpY) · **date:** 2025-11-02 · **length:** 6:12 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Cursor
- **topics:** coding-agents, context-engineering · **tags:** cursor, cursor-rules, project-rules, dependency-manifests, package-json, requirements-txt, rules-files

> Short tutorial on using Cursor Directory's generate-project-rules feature to turn package.json or requirements.txt into Cursor .rules files, with a UI demo and no evaluation of rule quality.

## Summary
The speaker says Cursor has deprecated the legacy Cursor Rules setting in favor of per-framework or per-language .rules files. He presents Cursor Directory's "generate cursor project rules" feature, which takes a .cursorrules file, a package.json, or a requirements.txt and produces one rule per dependency. He demonstrates uploading a Next.js/React frontend package.json and a FastAPI/SQLAlchemy requirements.txt backend, then manually adding each generated rule (name, description, globs, body) through Cursor's project rules settings. The result lands in the .cursor/rules folder. He closes by pointing to the community rules library and a curated list of MCP server integrations, using an Obsidian example. The video contains no measurements, no comparison of rule quality, and no discussion of failure cases beyond the lock-file rejection.

## Key ideas
- **Cursor has deprecated the legacy Cursor Rules setting in favor of .rules files, which are separated by framework or language (per the speaker).** — Background framing for why per-framework rules files are the unit of configuration. The speaker's claim about the deprecation is not shown on screen; verify against Cursor's docs. ([0:00](https://youtu.be/ztT6Bu1MPpY?t=0))
- **Cursor Directory's generate-project-rules feature builds rules from dependency files rather than hand-written rules.** — Accepted inputs: a .cursorrules file, package.json, or requirements.txt. The speaker says the output is powered by Grok, and that the tool generates one rule per dependency, for example Next.js, React, TypeScript and Tailwind from package.json. ([0:00](https://youtu.be/ztT6Bu1MPpY?t=0))
- **Only specific manifest files are accepted; a lock file was rejected.** — The speaker tried a lock file and it did not work, so he told viewers to use package.json. He describes this as a constraint of the tool, not a general limit. ([1:27](https://youtu.be/ztT6Bu1MPpY?t=87))
- **Each generated rule has four parts: name, description, globs, and rule body.** — Globs scope the rule to matching file paths. The speaker says the rule set is optimized to work together across dependencies, but he shows no evidence for that claim. ([1:27](https://youtu.be/ztT6Bu1MPpY?t=87))
- **Rules are added by hand in Cursor's settings, and there is no automatic import.** — In Settings > General > Rules, the project rules section takes the name without the .mdc extension, then the description and globs. The body is pasted into the file that opens. The speaker says the file then appears under .cursor/rules. ([3:05](https://youtu.be/ztT6Bu1MPpY?t=185))
- **Frontend and backend manifests are processed separately.** — The requirements.txt for the FastAPI backend generated rules for FastAPI and SQLAlchemy, which the speaker added the same way. This is the only multi-manifest workflow shown. ([3:05](https://youtu.be/ztT6Bu1MPpY?t=185))
- **The Cursor Directory site also has a community library of rules and a curated list of MCP server integrations.** — The speaker opens an Obsidian markdown MCP server entry as an example, with a basic overview and a link to the GitHub repo for setup. He points to an earlier video for MCP background. ([4:34](https://youtu.be/ztT6Bu1MPpY?t=274))

## Techniques
- **Generate project rules from dependency manifests** — 1) Open Cursor Directory's generate-project-rules feature. 2) Upload a .cursorrules file, package.json, or requirements.txt (not a lock file such as package-lock.json). 3) For each generated rule, copy its name, description, globs, and rule body. Stage the output in a scratch .txt file first if needed. 4) In Cursor, open Settings > General, go to the project rules section, and enter the name without .mdc. 5) Paste the description and globs, then paste the rule body into the file that opens. 6) Confirm the file appears under .cursor/rules in the project. *When:* Starting a new project, or adding a framework to a repo that has only a single rules file. It replaces writing one rules file per dependency by hand.
- **Generate rules per manifest in polyglot repos** — Run the generator once with the frontend package.json and again with the backend requirements.txt. Add each generated set to the project rules, as the speaker does with Next.js (frontend) and FastAPI plus SQLAlchemy (backend). *When:* A repo has more than one language or service, and you want each area to get its own dependency-specific rules.

## Hot takes
- Hype title and intro ('doing it wrong', 'ONE CLICK', 'no more wasted time') over a 6-minute UI walkthrough with no evidence about rule quality or accuracy.
- The claim that generated rules are 'optimized' to work together across dependencies is asserted, not shown.
- The deprecation claim about Cursor Rules is the speaker's statement and is not shown on screen. Verify it before relying on it.

## Tools mentioned
Cursor, Cursor Directory, Grok (named by the speaker as the generation model), Next.js, React, TypeScript, Tailwind CSS, FastAPI, SQLAlchemy, Obsidian (markdown MCP server example), MCP servers

## Relevance to our work
- **prosharness** (1/3): Generating context rules from dependency manifests touches context engineering for coding agents. ProsHarness runs Claude Code, not Cursor, so this is only a weak idea. → *Low priority: if ProsHarness bootstraps a CLAUDE.md for a repo, test whether it can seed project guidance from package.json or pyproject.toml, then compare the output with a hand-written file.*
