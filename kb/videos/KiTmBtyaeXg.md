# They Finally Fixed Claude Code's Biggest Problem

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `KiTmBtyaeXg` · [watch](https://youtu.be/KiTmBtyaeXg) · **date:** 2026-07-02 · **length:** 9:17 · **format:** review · **quality:** 2/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** NVIDIA, Anthropic, OpenAI, skills.sh, Nimblist
- **topics:** security-guardrails, skills-self-improvement, claude-code · **tags:** agent-skills, skill-scanning, supply-chain, prompt-injection, unicode-homoglyphs, headless-mode, claude-p, skills-sh, sponsored

> A walkthrough of NVIDIA's Skill Specter, a scanner for agent skills, plus a Claude Code wrapper that adds an LLM-based second scan through headless mode and a discover-scan-fix loop around skills.sh.

## Summary
The host argues that agent skills are plain text instructions that agents follow without checks, and that many contain security problems. They present Skill Specter, which scans a skill and gives a 0-100 danger score with file and line references. The scanner covers six grouped attack types: hidden instructions, lookalike-character tool impersonation, descriptions that contradict code behavior, credential theft, known malware fingerprints, and typosquatted dependencies. The default mode is pattern matching and produces false positives, so an optional AI check adds context. That check normally needs an OpenAI key, so the host runs it through Claude Code's headless mode instead, using plan credits. They wrap the scanner in scan.sh and a SKILL.md workflow, combined with skills.sh search, to form a "discover skills" loop: find, scan, show findings, fix, rescan. A worked example shows one skill scoring 10 and another scoring 100 before the AI check drops it to 0. The video is a tool tour with little reproducible detail, and it includes a sponsor segment for Nimblist.

## Key ideas
- **Agent skills are a trust gap** — A skill is a text file the agent treats as orders, and the host says a large share of skills (they cite 30,000+ studied, over a quarter with a vulnerability, source not given) contain security problems. Nobody checks them before install. ([0:00](https://youtu.be/KiTmBtyaeXg?t=0))
- **Six attack classes after grouping 14 categories** — Hidden instructions (comments, invisible characters, encoded text); impersonation by name collision; description-vs-behavior mismatch; credential theft; known malware such as reverse shells; poisoned dependencies (typosquatted packages). ([1:07](https://youtu.be/KiTmBtyaeXg?t=67))
- **Impersonation is a Unicode identity problem** — A malicious skill can ship a tool named like a trusted built-in (e.g. read) with one Cyrillic letter swapped in. It looks identical to humans and agents, so the scanner checks the actual code point of every character. ([2:20](https://youtu.be/KiTmBtyaeXg?t=140))
- **Pattern-only scanning produces false positives, so add an AI pass** — The default no-LLM mode matches patterns without context and flags benign code. The AI check adds context and catches behavior that pattern matching misses, such as a skill whose description says it only reads files while the code writes and runs commands. ([3:48](https://youtu.be/KiTmBtyaeXg?t=228))
- **The AI check is the one that catches the test skills** — On the bundled dangerous test skills, the no-LLM run scored 0 (looks safe) and the AI-check run scored 100 with a do-not-install verdict. The default setting is the weak one. ([4:47](https://youtu.be/KiTmBtyaeXg?t=287))
- **Wrap the scanner in a discover-scan-fix loop** — Packaged as a Claude Code skill. Search skills.sh from the CLI, scan each candidate before install, show findings, fix them, then rescan until clean. Install only after the scan passes. ([5:48](https://youtu.be/KiTmBtyaeXg?t=348))
- **Worked example: scan first, install after** — Two candidate skills were installed to test and scanned first. One scored 10 and was usable. The other scored 100, and after the AI check it scored 0. The host says the workflow makes skill installs a checked step rather than blind grabs. ([7:16](https://youtu.be/KiTmBtyaeXg?t=436))

## Techniques
- **Two-tier skill scan before install** — Run the scanner in fast pattern mode first. Then run the AI check, which the host says is an option that omits the no-LLM flag. Treat any high score as a block. The exact flag name is not spoken in the transcript; check the repo. *When:* Before installing any third-party skill, or before enabling one found through search.
- **Use Claude headless mode as the LLM judge** — Instead of an OpenAI key, the scan script calls Claude Code in headless mode (claude -p, run in the background with no chat UI). Per the host, this runs on plan credits. The main agent session does not do the judging itself. *When:* When you want an LLM second opinion on a skill without a separate API key or budget, and your plan includes headless credits.
- **Discover, scan, show, fix, rescan loop in SKILL.md** — The SKILL.md steps are: identify the target, scan it, show findings, fix issues, then run the full loop again to confirm it is clean. scan.sh wraps the scanner and bakes in the headless-mode fix. Discovery uses skills.sh via its CLI search. *When:* When an agent should find skills on its own and only install ones that pass the scan.
- **Check tool-name identity at the code-point level** — Compare tool and function names by their Unicode code points, not visually. Flag any non-ASCII character in names that match built-in tools, such as a Cyrillic a in read. *When:* When loading skills or MCP tools that could shadow trusted built-in tools.
- **Compare declared behavior with code behavior** — Check the skill description or declared permissions against what the code does: network calls, file writes, shell commands. Flag mismatches, such as a formatter that makes outbound requests. *When:* When reviewing a skill whose metadata claims narrower permissions than its scripts use.
- **Check dependencies against a live bad-package list** — For every package a skill pulls in, look it up in a live database of known-bad packages. Flag names one typo away from popular packages, and flag download-and-run commands. *When:* When a skill installs CLI tools or packages at run time.

## Numbers
- Over 30,000 skills studied by researchers; more than a quarter had a security vulnerability (source not cited in the video). ([0:00](https://youtu.be/KiTmBtyaeXg?t=0))
- 14 attack categories, grouped into 6 for the explanation. ([0:00](https://youtu.be/KiTmBtyaeXg?t=0))
- Danger score runs 0 to 100, where higher means more dangerous. Findings include file name and line number. ([1:07](https://youtu.be/KiTmBtyaeXg?t=67))
- Bundled dangerous test skill: no-LLM scan scored 0, AI-check scan scored 100. ([4:47](https://youtu.be/KiTmBtyaeXg?t=287))
- Worked example: one candidate scored 10 (safe), another scored 100 (do not install), and the AI check gave 0 after the rerun. ([7:16](https://youtu.be/KiTmBtyaeXg?t=436))

## Hot takes
- The title says Claude Code's biggest problem is finally fixed. The video is about a third-party skill scanner and a wrapper script, not a Claude Code change.
- The sponsor segment (Nimblist) sits in the middle of a content video. Under the rubric it caps quality at 2.
- The 30,000-skill and one-quarter-vulnerable figures are presented with no source or method.
- The host says one attack class slips past the default scan and that the setting catching it is off by default. The transcript does not name the attack class, and the AI check is only implied as the fix.
- The AI-check workaround depends on headless credits in a paid Anthropic plan. The host says it is not free and gives no price or credit amount.
- The host's own workflow uses one LLM to judge skills, with no discussion of whether that judge can be fooled by the skill text it is checking.

## Tools mentioned
Skill Specter (NVIDIA scanner, named by the host; version not stated), Claude Code, Claude headless mode (claude -p), skills.sh (skill registry with CLI search), OpenAI API (the AI check's default backend, per the host), Codex (mentioned only in the sponsor segment), Nimblist (sponsor; open-source visual workspace for Claude Code and Codex sessions, with a Kanban board, red/green diffs, auto-generated commit messages, and a mobile app)

## Relevance to our work
- **agentos** (2/3): SkillForge is meant to turn mined telemetry into governed, reusable skills. A pre-install scan gate with a pattern pass plus an LLM pass is a concrete governance step for that pipeline. → *Add a scan stage to the SkillForge promotion path: pattern scan (hidden Unicode, tool-name homoglyphs, typosquat package names) plus an LLM check on skills that pass, with the score stored as provenance.*
- **prosharness** (2/3): ProsHarness has skill ranking and wraps the Claude Code CLI. The video's search, scan, install loop and headless-mode judge both map onto that stack. → *Gate ProsHarness skill installs behind a scan step that runs claude -p headless as the second opinion, and read the scan.sh and SKILL.md pattern before building it.*
