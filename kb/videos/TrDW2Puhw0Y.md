# GitHub MCP Server: Let AI Handle Your GitHub

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `TrDW2Puhw0Y` · [watch](https://youtu.be/TrDW2Puhw0Y) · **date:** 2025-11-02 · **length:** 6:54 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** GitHub, Cursor, Anthropic
- **topics:** mcp-and-tools, coding-agents, dev-tools · **tags:** github, mcp, cursor, personal-access-token, agent-mode, shell-script, setup-guide, pull-requests

> Step-by-step setup of the GitHub MCP server in Cursor, then a live demo of an agent creating a repo, pushing a file, cloning and searching GitHub from the chat.

## Summary
The host argues that developers can skip the terminal and GitHub website for routine repo work once an agent is connected to GitHub through an MCP server. He demos Cursor's agent creating a repository, pushing an HTML file (after recovering from an error by calling a different tool), and cloning the result. The bulk of the 6:54 video is setup for Cursor: generating a GitHub classic personal access token, storing it in a shell script because Cursor will not take an environment variable inline, and registering the script as a command-type MCP server. He closes with a search for a GitHub user and their repositories. The video shows a working setup but no evaluation, failure modes, or permission hygiene beyond the token scope he recommends.

## Key ideas
- **An agent connected to the GitHub MCP server can do repo work from inside the editor: create a repository, push files, clone, search, and open pull requests, without visiting GitHub.** — The demo has the Cursor agent call the create-repository tool, then the push-files tool to add index.html with a greeting, then the host clones the repo locally and finds the file. ([0:00](https://youtu.be/TrDW2Puhw0Y?t=0))
- **The agent recovered from a tool error on its own by switching to another MCP tool and retrying the push.** — The host presents this as the agent fixing the error automatically. He shows one instance and does not analyze how often this happens. ([0:00](https://youtu.be/TrDW2Puhw0Y?t=0))
- **Cursor does not accept environment variables inline in an MCP command, so the GitHub token has to live in a wrapper script.** — The host's workaround is a shell script that exports the personal access token and runs the npx command. Cursor then launches the script. ([3:06](https://youtu.be/TrDW2Puhw0Y?t=186))
- **The token he recommends is a GitHub classic personal access token with the repo scope, which he says the MCP server needs to work with private repositories.** — He says GitHub shows the token only once, so it should be saved immediately. He does not discuss fine-grained tokens or narrower scopes. ([3:06](https://youtu.be/TrDW2Puhw0Y?t=186))
- **Cursor only runs MCP tool calls when the chat is in agent mode, and the server is registered as a command-type entry that runs bash on the script.** — Cursor's MCP settings show a green status light and the list of available tools once the server connects. Tool calls fail silently outside agent mode, per the host's warning. ([4:44](https://youtu.be/TrDW2Puhw0Y?t=284))
- **The server exposes a broad tool surface beyond the demo: search issues, search code, create branches, fork repos, and create pull requests from a plain-language request.** — He says the pull-request tool is his favorite because it keeps the developer in flow, but he does not show a PR being created in the video. ([1:43](https://youtu.be/TrDW2Puhw0Y?t=103))
- **The host says he did not test most features, so the video is a setup guide and a sample of behavior, not a capability review.** — He states that the installation was covered thoroughly so viewers avoid setup problems, and he leaves the other tools untested. ([5:48](https://youtu.be/TrDW2Puhw0Y?t=348))

## Techniques
- **Wrap the GitHub token in a shell script for Cursor's MCP command** — 1) In a terminal run `touch script.sh` (he uses `run.sh` for his own setup). 2) Open it with `nano script.sh` and paste the GitHub MCP npx command, replacing the placeholder with your personal access token. The exact npx command is shown on screen and is not spoken in the transcript. 3) Save with Ctrl+O, Enter, then exit with Ctrl+X. 4) Run `realpath script.sh` and copy the absolute path it prints. *When:* Use when an MCP server needs an environment variable such as a token and the client (here Cursor) will not accept inline env vars in the server command.
- **Create a GitHub classic personal access token for the MCP server** — GitHub profile > Settings > Developer settings > Personal access tokens > Tokens (classic) > Generate new token (classic). Give it a name, set an expiration date, and tick the repo scope. Copy the token right away because GitHub shows it only once. *When:* Use for the setup in this video, where the speaker wants access to private repositories. The video does not cover fine-grained tokens or least-privilege scopes.
- **Register the script as a command-type MCP server in Cursor** — Cursor Settings > MCP > add a new MCP server. Give it any nickname, set the type to `command`, and enter `bash <absolute path to script.sh>`. Wait for the green status light and the tool list to appear. Then switch the chat to agent mode before prompting. *When:* Use when wiring any stdio MCP server into Cursor that needs a wrapper script to set environment variables.
- **Smoke-test the MCP connection with a read-only query** — In agent mode, ask a simple read-only question, such as searching for a GitHub user. Watch for the MCP tool call (here search users, then search repositories) before trying write actions like creating a repo or pushing files. *When:* Use after setup to confirm the server works before giving it write access to real repos.

## Numbers
- Demo tool calls shown: create repository, push files, search users, search repositories. The host names about five other tools (search issues, search code, create branches, fork repos, create pull requests) without a count. ([0:00-5:48](https://youtu.be/TrDW2Puhw0Y?t=0))
- No benchmarks, latencies, token counts or costs are reported. The only figure is the video length of 6:54. ([0:00](https://youtu.be/TrDW2Puhw0Y?t=0))

## Hot takes
- Claim: you no longer need the terminal or GitHub website for GitHub work. The video shows only a few tool calls, so this is a claim about convenience, not measured reliability.
- The setup is described as complex, but the host recommends a classic PAT with full repo scope and a plaintext token in a shell script without discussing least privilege or rotation.
- The error-recovery moment is shown as proof of autonomy, but it is one anecdote from a single run.
- The host openly says he did not test most of the features, so the claimed breadth (PRs, forks, branches) is largely unverified in the video.

## Tools mentioned
GitHub MCP server (GitHub's official MCP server, run through npx), Cursor (IDE, agent mode, MCP settings), npx, bash, nano, realpath, GitHub classic personal access tokens, Claude Desktop (mentioned as the server's reference client), Archon (another creator's agent-building repo, mentioned in passing)

## Relevance to our work
- **prosharness** (1/3): The video stores a classic PAT in a plaintext shell script. ProsHarness claims zero-token credential handling, so this is a useful contrast to check against. → *Compare ProsHarness's credential path with this plaintext-script pattern to confirm the harness never exposes a token to the model or to a shell file.*
