# How I Made Claude Code WAY Better With Vercel Agent Skills

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `PkeC2hNQ9Zw` · [watch](https://youtu.be/PkeC2hNQ9Zw) · **date:** 2026-02-02 · **length:** 6:27 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Vercel, Cloudflare, Anthropic, Microsoft, OpenAI, OpenCode, Cursor
- **topics:** skills-self-improvement, coding-agents, claude-code · **tags:** agent-skills, skills.sh, add-skill, progressive-disclosure, well-known-index, skill-discovery, claude-code-skills, telemetry

> Better Stack explains the Agent Skills format, Vercel's add-skill installer and skills.sh discovery, and Cloudflare's proposed well-known skills index, then closes with a sponsor read.

## Summary
The video explains how Agent Skills work: a folder with a skill file whose YAML frontmatter (name, description) is always loaded, while the body loads only when the description matches the task. It then covers Vercel's add-skill CLI, which clones a repo, checks for a skill file, and symlinks the skill into each detected agent's directory, supporting 16 agents. It describes skills.sh as a discovery list populated by anonymous install telemetry, with per-agent download counts and 24-hour trends. Last, it covers Cloudflare's proposal to publish an index.json at a well-known location so agents can find skills from a vendor's domain, and the presenter's view that this could complement skills.sh. The video ends with a sponsor segment. It gives no before-and-after result showing Claude Code getting better.

## Key ideas
- **A skill is a folder under the agent's skills directory (for Claude Code, .claude/skills) containing a skill file. The file has YAML frontmatter with at least name and description, followed by the instructions.** — Instructions go below the frontmatter and are loaded into context when the skill is used. The skill file can also link reference files that the model fetches when it decides it needs them. ([0:00](https://youtu.be/PkeC2hNQ9Zw?t=0))
- **Progressive disclosure keeps context small.** — At startup only each skill's frontmatter is loaded. When a prompt matches a skill's description, the full instructions enter the active context. Linked files are pulled in only if the model asks for them. ([1:15](https://youtu.be/PkeC2hNQ9Zw?t=75))
- **Vercel's add-skill CLI installs any skill repo into many agents.** — The presenter says it supports 16 agents. It runs npx add-skill with a skill name or repo, clones the repo, and looks for a skill file. If none is found it deletes the clone. If one is found, it detects the installed agents from their config and symlinks the skill into each agent's directory. ([1:15](https://youtu.be/PkeC2hNQ9Zw?t=75))
- **skills.sh is a discovery directory filled by install telemetry.** — Installing through add-skill sends anonymous telemetry with the skill name, agents and other details. That populates skills.sh and drives download counts per agent and a 24-hour trending list. The presenter says telemetry can be disabled but does not show how. ([2:28](https://youtu.be/PkeC2hNQ9Zw?t=148))
- **Cloudflare proposes that agents discover skills from a well-known index.json on a site.** — The index lists each skill's name, description and file count. The agent reads the index, picks a skill that matches the prompt, fetches its files, and caches them for follow-up prompts. The presenter notes the index is at a well-known path, though his wording on the exact path is unclear. ([3:33](https://youtu.be/PkeC2hNQ9Zw?t=213))
- **The presenter sees the two discovery models as complementary, not competing.** — He argues the extra publishing steps in the Cloudflare approach could disadvantage small developers. He suggests skills.sh for indie and lesser-known skills and the well-known index for large vendors such as Cloudflare and Vercel. He also says it is unclear who would review and accept the proposal. ([4:51](https://youtu.be/PkeC2hNQ9Zw?t=291))

## Techniques
- **Write a skill file with frontmatter** — Create .claude/skills/<skill-name>/ and put a skill file in it. Start with YAML frontmatter containing name and description, then the instructions. Link reference files from the body. The presenter says the file is called skills.md in the transcript; the Claude Code convention is SKILL.md, so check the official docs before relying on either name. *When:* Authoring your own skill. Write the description so the agent can match it to prompts, because only the description is loaded before a skill is used.
- **Install one skill into several agents** — Run npx add-skill <skill-name-or-owner/repo>. The tool clones the repo, checks for a skill file, detects installed agents from their config, and symlinks the skill into each agent's skills directory. The presenter names .agents/skills as the shared location, with per-agent directories such as .cursor and .claude. *When:* Sharing one skill set across Claude Code, Cursor and other agents without copying the repo by hand.
- **Discover skills by popularity** — Browse skills.sh, which lists skills with per-agent download counts and a 24-hour trending view. The presenter says it is populated by add-skill install telemetry, which can be disabled. *When:* Finding well-used skills, or checking whether a skill is popular before installing it.
- **Publish a skill index at a well-known path (proposal)** — Per the presenter's description of Cloudflare's proposal, publish a JSON index that lists each skill's name, description and file count at a well-known URL. The agent fetches the index first, then fetches and caches the full skill files only for the skill it picks. The presenter does not give the exact path or the JSON schema. *When:* Thinking about how an organization could let agents discover its skills automatically, but this is a proposal and not a standard the presenter says is accepted.

## Numbers
- add-skill supports 16 agents. ([1:15](https://youtu.be/PkeC2hNQ9Zw?t=75))
- Only the frontmatter of each skill is loaded at startup; the full instructions load after a prompt matches the skill's description. ([1:15](https://youtu.be/PkeC2hNQ9Zw?t=75))
- skills.sh shows per-agent download counts and a trending list over the last 24 hours, populated by install telemetry. ([2:28](https://youtu.be/PkeC2hNQ9Zw?t=148))
- The Cloudflare index.json lists name, description and number of files for each skill. ([3:33](https://youtu.be/PkeC2hNQ9Zw?t=213))

## Hot takes
- The sponsor segment for Better Stack at 6:03 is the closing segment, so quality is capped at 2.
- The title promises that Claude Code gets 'WAY better', but no before-and-after run or benchmark is shown. The video is an ecosystem explainer.
- The Cloudflare index is an unaccepted proposal. The presenter says he is unsure who reviews it, so presenting it as a near-term option is speculative.
- The claim that the Cloudflare approach harms smaller developers is the presenter's opinion, with no data.

## Tools mentioned
Claude Code, Agent Skills (Anthropic), add-skill (Vercel, npx add-skill), skills.sh, Cloudflare well-known skills index proposal, Cursor, Wrangler, Remotion, React Native skills, Better Stack

## Relevance to our work
- **agentos** (2/3): SkillForge (L2D) needs a governed, reusable skill store. The skills.sh telemetry and the index-then-fetch-on-demand discovery pattern are relevant prior art for it. → *Compare SkillForge's skill registry design with the index.json-then-fetch-and-cache model, and decide which fields (name, description, file count) belong in the index.*
- **prosharness** (2/3): ProsHarness does skill ranking around the Claude Code CLI. Install counts and 24-hour trends are a popularity signal that could feed the ranking. → *Evaluate whether skills.sh download and trending counts can be an input signal for skillrank, and what privacy trade-off that implies.*
