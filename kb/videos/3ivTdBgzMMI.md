# Does GitHub's New MCP Server KILL Git Commands? (w/ Cursor)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `3ivTdBgzMMI` · [watch](https://youtu.be/3ivTdBgzMMI) · **date:** 2025-11-02 · **length:** 5:26 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Better Stack presenter (unnamed in transcript) · **orgs:** Better Stack, Cursor, GitHub, Docker, Supabase, Figma, Playwright
- **topics:** mcp-and-tools, coding-agents, dev-tools · **tags:** github-mcp-server, mcp, cursor, git, github-cli, git-aliases, docker, neovim, pull-requests, agent-reliability, latency-comparison, mcp-security

> Better Stack runs one timed repo-and-PR task through the GitHub MCP server inside Cursor, finds it about twice as slow as Git aliases and the GitHub CLI, and advises against it for simple Git work.

## Summary
The presenter sets up the new GitHub MCP server in Cursor (Docker container plus a classic GitHub token) and uses it to create a repo, push a file, branch, change the H1, open a pull request and comment on it, all by dictated prompt. The same task done by hand in NeoVim with Git aliases took just under two minutes, while the MCP run took roughly twice as long, with several agent failures that it recovered from by falling back to direct git commands. The presenter's conclusion is that the server is not worth it for ordinary Git work, and that it would matter more for history surgery such as scrubbing sensitive data from commits or fixing a messy rebase. The video closes with an unsupported claim that MCP servers are a security nightmare, with the details promised for a follow-up video. This is a single-run anecdote with a clickbait title, not a controlled benchmark.

## Key ideas
- **The GitHub MCP server can run the whole repo-to-PR flow from natural-language prompts in Cursor: create repo, push a file, branch, edit, open PR, comment.** — No git commands were typed by the presenter; the prompt was dictated and the agent called MCP tools for repo creation and PR operations, and used git commands for cloning and pushing. ([0:00](https://youtu.be/3ivTdBgzMMI?t=0))
- **Setup needs Docker and a classic GitHub token. The official server ships as a Docker container, and the only build option is from source.** — The presenter says the earlier server could run through npx, which he counts as a reason not to like the new one. He also says Cursor states that the token is stored safely. ([0:00](https://youtu.be/3ivTdBgzMMI?t=0))
- **On a hand-driven task, Git aliases and the GitHub CLI finished in just under two minutes.** — The sequence was: new public repo, clone, edit index.html in NeoVim, commit and push with upstream set, branch 'feet' (features), change the H1, push, open PR with title and body, add a comment. ([2:11](https://youtu.be/3ivTdBgzMMI?t=131))
- **The MCP run took about twice as long, with failures along the way.** — The agent retried twice on the H1 update, hit a model error, then fell back to direct git commands to fetch the branch, edit, commit and push, before using the MCP tool for the PR and comment. The presenter did not time the code-generation part, but says it did not affect timing. ([3:35](https://youtu.be/3ivTdBgzMMI?t=215))
- **The presenter recommends the GitHub MCP server only for work beyond simple Git.** — He argues that people familiar with Git do not need an LLM and a Docker container to fork a repo, and that a subscription is paid just for that. He says the server would earn its place on history rewriting, such as removing sensitive data from commits or a messy rebase. He contrasts it with the Supabase, Figma and Playwright MCP servers, which he calls useful. ([4:39](https://youtu.be/3ivTdBgzMMI?t=279))
- **MCP servers are a security risk, a claim made without evidence in this video.** — The presenter says MCP servers are a security nightmare and points to a follow-up video. No attack, threat model or evidence is shown here. ([4:39](https://youtu.be/3ivTdBgzMMI?t=279))

## Techniques
- **Run the GitHub MCP server in Cursor** — Install Docker and open the GitHub MCP server repo. Copy its MCP config, then in Cursor open Settings > MCP and paste it. Add a classic GitHub personal access token (the presenter ticks the classic box, scopes not shown). Confirm that a GitHub MCP container runs. The build-from-source path is the only alternative to Docker, which he counts as a drawback. *When:* When you want an agent to drive GitHub actions (repo creation, PRs, comments) and you accept a Docker dependency and the token setup.
- **Manual Git and PR flow with aliases (baseline)** — Create a repo, clone it, edit a file in NeoVim, commit, then git push with the upstream flag (he forgot it once and reran). Create a branch, edit, commit and push again. Open a PR with a title and body and add a PR comment. This took about two minutes for the task. *When:* For routine Git and PR operations where you already know the commands. It is the speed baseline in the video.
- **Fall back to direct git when the agent stalls** — When the MCP agent fails repeatedly on a file edit, inspect the proposed command, approve it, and let the agent use git directly for fetch, edit, commit and push, then return to MCP for the PR and comment. *When:* When an MCP tool step keeps failing and plain git commands are the reliable path.

## Numbers
- Manual Git and alias workflow for the full repo-to-PR task took just under two minutes. ([2:11](https://youtu.be/3ivTdBgzMMI?t=131))
- GitHub MCP run took almost twice as long as the CLI and Git-alias run. ([4:39](https://youtu.be/3ivTdBgzMMI?t=279))
- The MCP run hit several failures and retries on the H1 update step before falling back to direct git commands. ([3:35](https://youtu.be/3ivTdBgzMMI?t=215))
- Cursor subscription cost cited as about $20 per month. ([4:39](https://youtu.be/3ivTdBgzMMI?t=279))

## Hot takes
- The GitHub MCP server is not worth using for simple Git work when you already know Git; the presenter would use it for complex history operations such as removing sensitive data from commits or fixing a messy rebase.
- MCP servers are a security nightmare. This is asserted without evidence in this video.
- The new Docker-based GitHub MCP server is a regression from the earlier npx-runnable server because it removes the easy local run option.
- Title overstated: the video does not show Git commands being killed, and the comparison is a single run of one task.

## Tools mentioned
GitHub MCP server (new, Docker-based; the older server ran via npx), Cursor (IDE with MCP settings), Docker, Git, GitHub CLI / Git aliases (baseline), NeoVim, macOS dictation feature, Supabase MCP server, Figma MCP server, Playwright MCP server

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, which already uses git directly. The video supports keeping simple git operations on the CLI path rather than routing them through MCP. → *Keep routine git and PR steps on the CLI path in ProsHarness, and reserve MCP for operations that need its extra capability.*
