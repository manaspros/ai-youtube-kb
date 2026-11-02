# We Already Have Something Better Than Claude Design

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `GbuwosWEvHo` · [watch](https://youtu.be/GbuwosWEvHo) · **date:** 2026-05-02 · **length:** 12:38 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** AI LABS host (unnamed) · **orgs:** Anthropic, AI LABS, HeyGen, Figma
- **topics:** claude-code, coding-agents, product-ux, context-engineering · **tags:** claude-design, claude-code, opus-4.7, vision, frontend-design, git-worktrees, parallel-agents, skills, gsap, lenis, shadcn, mcp, token-limits

> AI LABS argues Claude Design is mostly hype: Claude Code with Opus 4.7 can match it, and it adds Git, parallel worktrees, and skills. The evidence is one anecdotal comparison plus sponsor-heavy, unverified claims.

## Summary
The video claims Claude Design is essentially Claude Code repackaged, and that the output quality comes mainly from the Opus 4.7 vision upgrade (about 3.6 MP image input versus 1.15 MP on Opus 4.6), not the product. The speaker's test was a single community-site prompt run in Claude Code on Opus 4.7 at high effort, which he judges on par with Claude Design's two outputs. He argues Claude Design's weekly quota burns quickly (one user reportedly ran out after about 20 iterations on the top plan), while Claude Code is cheaper for iteration. He recommends replicating Claude Design's clarifying-question flow with a custom skill, and building animated hero sections with GSAP, Lenis, ShadCN, Aceternity UI, Hero UI, or an open-source scrollytelling skill. The strongest practical point is that Claude Code produces real code with full Git operations (commits, branches, reverts), and parallel subagents in separate git worktrees can explore design variants. Sponsor segments (HeyGen) are present. Much of the case rests on the speaker's own assertions, not measured comparisons.

## Key ideas
- **Claude Design is positioned as a separate product, but the speaker argues it is Claude Code repackaged with a design harness.** — His test was one community-website prompt; Claude Code on Opus 4.7 (high effort) with no design harness produced a design he judged on par with Claude Design's output. ([0:00](https://youtu.be/GbuwosWEvHo?t=0))
- **The quality gain is attributed to the model, not the tool: Opus 4.7 vision resolution rose from about 1.15 MP (4.6) to 3.6 MP.** — The speaker says this makes reference-image understanding better, and that Anthropic closed a front-end design gap in the model itself. ([2:51](https://youtu.be/GbuwosWEvHo?t=171))
- **Claude Design's quota is a weekly limit counted separately, and it burns fast; the speaker cites users running out after about 20 iterations even on the top plan.** — Anecdotal user reports only. The argument is that short quotas cut iteration short, so Claude Code's limits are better for exploration. ([2:51](https://youtu.be/GbuwosWEvHo?t=171))
- **A custom skill can reproduce Claude Design's clarifying-question flow in Claude Code.** — The skill holds the questioning rules, follow-up triggers, a question library and ASCII layouts for positioning, and it outputs code directly, so there is no design-to-code handoff. ([4:09](https://youtu.be/GbuwosWEvHo?t=249))
- **Most viral Claude Design showcase sites rely on video backgrounds and copied prompt templates rather than something the product does uniquely.** — In a test, the speaker gave Claude Code a downloaded video as the hero background plus a colour theme, and it built the rest of the site with a single correction. ([6:47](https://youtu.be/GbuwosWEvHo?t=407))
- **Claude Code's advantage is Git: it can commit, branch and revert, while Claude Design's GitHub integration is read-only in practice.** — Reverting to an older version is one of the reasons given for choosing Claude Code over Claude Design. ([9:37](https://youtu.be/GbuwosWEvHo?t=577))
- **Parallel subagents in separate git worktrees can explore design variants, and the winner merges into main.** — Each agent implements a different variation of the same design in its own worktree; you review the results, merge the preferred one and delete the rest. ([10:51](https://youtu.be/GbuwosWEvHo?t=651))

## Techniques
- **Clarifying-question skill to replace Claude Design's intake flow** — Write a skill that defines when to ask follow-up questions, includes example questions and a question library, and uses ASCII layouts for element placement. The agent asks questions for gaps in the prompt, then builds directly as code. (The speaker says the skill is shared via AI LABS Pro, and he does not show its contents.) *When:* When you want a Claude Design-style discovery session for a landing page or UI, and want to keep iterating without quota limits.
- **Hero video background plus animation libraries** — Download a background video, then prompt Claude Code to use it as the hero section with a chosen colour theme. For production-style motion, name GSAP for animations and Lenis for smooth scrolling. The speaker says a scrollytelling open-source skill adds scroll-driven story animations. *When:* For an immersive marketing or landing page where you want more motion than the default generated design.
- **Component libraries and MCP for UI consistency** — Name ShadCN, Aceternity UI or Hero UI components in the prompt, or connect the ShadCN MCP server so the agent installs components itself. Add front-end design skills or a skill-creator-generated project skill. *When:* To keep generated UIs from looking model-generated and to speed up component work.
- **Parallel design variants in git worktrees** — Prompt: use sub-agents, each in a separate git worktree, and have each implement a different variation of the same design. When they finish, review the variants, merge the chosen one into main and remove the other worktrees. *When:* When exploring several visual directions at once and you want to keep the winner in Git and discard the rest.
- **Prototype as HTML mock-ups** — Build prototypes as plain HTML instead of starting in Figma or Claude Design. The result is real code that can be shipped. *When:* For fast prototyping where the output must become production code.

## Numbers
- Opus 4.7 image analysis resolution is about 3.6 MP, up from about 1.15 MP on Opus 4.6. ([2:51](https://youtu.be/GbuwosWEvHo?t=171))
- A user reportedly hit the Claude Design limit after about 20 design iterations, even on the highest Max plan (anecdotal). ([2:51](https://youtu.be/GbuwosWEvHo?t=171))
- Some users reportedly hit the limit within one hour (anecdotal). ([2:51](https://youtu.be/GbuwosWEvHo?t=171))
- The head-to-head test was one prompt, with Claude Design producing two designs, one of them cut off at pricing with no footer (per the speaker). ([0:00](https://youtu.be/GbuwosWEvHo?t=0))

## Hot takes
- Claude Design is mostly Claude Code plus a skill and hype, and the real gains come from Opus 4.7 vision.
- Claude Code is a better design tool than Claude Design because it commits real code and supports Git.
- Viral Claude Design showcase sites are mostly video-background templates copied from prompt sites, not evidence of the tool's capability.

## Tools mentioned
Claude Code, Claude Design, Claude Opus 4.7, Claude Opus 4.6, GSAP, Lenis, ShadCN, ShadCN MCP server, Aceternity UI, Hero UI, scrollytelling skill, Figma, GitHub, Git

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code; worktree-based parallel variant exploration and a clarifying-question skill are patterns it could reuse in its orchestration. → *Read the parallel-worktree subagent pattern and consider a skill that runs a clarifying-question intake before long runs.*
