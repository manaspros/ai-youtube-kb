# This $8/hr AI Engineer Could Replace Junior Devs | Devin AI | Agentic Developer.

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `rfWx5zB0Cws` · [watch](https://youtu.be/rfWx5zB0Cws) · **date:** 2025-11-02 · **length:** 7:53 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** AI LABS narrator (unnamed), Walden (Cognition developer) · **orgs:** Cognition, AI LABS, GitHub, Slack, Upwork
- **topics:** coding-agents, software-factory, security-guardrails · **tags:** devin, cognition, autonomous-coding-agent, slack-integration, github-pull-requests, agent-self-qa, pricing, live-share-leak, swe-bench

> AI LABS walks through Devin's general availability: Slack/GitHub-driven autonomous coding, a self-QA demo, a $500/month plan the narrator converts to about $8/hour, and a live-share security leak. Mostly demo and hype, few hard numbers.

## Summary
AI LABS covers the general availability of Devin, Cognition's autonomous coding agent, opening with about a minute of Cognition's own promo clip. The narrator describes the Slack and GitHub integration: tag Devin in Slack to assign a task and get progress updates, and have it open pull requests and respond to review comments on them. A demo has Devin QA-testing its own web app by logging in with a test Google account plus 2FA, exercising features, and returning structured output, with the check set to run on every push. The sign-up flow shows a $500/month plan priced in agent compute units, which the narrator converts to about $8 per hour. A Cognition developer (Walden) runs an Upwork-style task where Devin sets up an unfamiliar computer-vision repo, fixes version conflicts, debugs with print statements, and produces a report with sample outputs. The narrator closes with mixed reception, including claims that Cursor is better, and a security incident where a leaked VS Code Live Share URL reportedly gave access to the agent's machine. The video gives no independent benchmark figures; the SWE-bench and o1-preview comparisons are vendor claims only.

## Key ideas
- **Devin is positioned as an autonomous engineer for bugs, refactors and small feature requests, and is assigned work by tagging it in Slack. Progress comes back in the thread.** — The GA announcement is shown in a Cognition-supplied clip at the start. Work is started from Slack, and Devin posts progress there. ([0:00](https://youtu.be/rfWx5zB0Cws?t=0))
- **On GitHub, Devin opens pull requests and responds to pull requests the team has opened.** — The narrator describes this as the integration that makes Devin useful day to day. The video shows no PR-level example. ([1:02](https://youtu.be/rfWx5zB0Cws?t=62))
- **Cognition uses Devin to QA Devin: the agent logs into the web app and tests features, and the check runs on every push.** — The setup is one prompt plus a test account (Google login with password and 2FA). The agent creates a session, sends messages, and ends with structured output. The narrator calls this an unusual self-test loop. ([1:02](https://youtu.be/rfWx5zB0Cws?t=62))
- **Vendor benchmark claims are not verified in the video. The SWE-bench results are compared against older models, and a proprietary benchmark is said to beat o1-preview.** — No scores or methodology are shown. Treat these as marketing claims. ([1:02](https://youtu.be/rfWx5zB0Cws?t=62))
- **Pricing is an agent-compute-unit model. The narrator's own arithmetic puts the $500/month plan at about $8/hour.** — The $8/hour figure is the narrator's derivation, not a price shown in the product. Sign-up also asks for name, GitHub and Slack access, and org name before the plan screen. ([2:30](https://youtu.be/rfWx5zB0Cws?t=150))
- **On an unfamiliar repo, Devin works in a fix-and-run loop: it updates code when versions break, adds print statements to trace data flow, removes them, then applies the fix.** — It keeps repeating this until the full pipeline runs across all rows, then produces a report with sample annotated images and a text file. ([3:57](https://youtu.be/rfWx5zB0Cws?t=237))
- **Devin's trajectory shows which tools it picks: shell to clone and install deps, the editor to read the README, a browser to read the issue, and a docs lookup to debug a Rust compiler error.** — The narrator uses this to show tool switching. It ends with a summary of changes. ([5:04](https://youtu.be/rfWx5zB0Cws?t=304))
- **The narrator flags a security incident: a team member exposed a VS Code Live Share URL, which let outsiders reach the agent's machine. He argues it needs more permission controls.** — The incident is described as quickly resolved. It is reported secondhand, not documented in the video. ([6:12](https://youtu.be/rfWx5zB0Cws?t=372))

## Techniques
- **Assign work from Slack, get progress in-thread** — Tag Devin in a Slack channel with the task. Connect GitHub and Slack during sign-up. Devin posts updates in the thread; on GitHub it opens PRs and answers comments on them. *When:* Small bugs, refactors and feature requests you can hand off asynchronously. The narrator calls Devin a junior engineer that works best with a good manager.
- **Agent-driven E2E QA on every push** — Give the agent a test account for the web app (login with password and 2FA). Prompt it once to exercise named features (e.g. create a session, send a message). Require structured output, and run it automatically on each push to the repo. *When:* Regression checks for agent-written changes to a web app; a cheap smoke layer that complements unit tests.
- **Bootstrap an unfamiliar repo by fix-and-run loop** — Clone the repo in the shell, read the README in the editor, install dependencies from the shell, and read the issue in a browser. Run the code, and when it fails, add temporary print statements to trace data flow. Remove them, apply the fix, and rerun until the pipeline completes. Ask for a final report with sample outputs. *When:* Onboarding to a repo with unclear setup, such as an ML or data project with version conflicts. The loop is what gets the run to finish, not a single shot.
- **Sign-up sequence to start a Devin account** — Go to app.devin.ai and sign up or log in. Enter your name, grant GitHub and Slack access, enter an organization name, then pick a plan. Pricing is in agent compute units. *When:* Trying the product. The plan screen is the first point where cost appears, so check it before committing to a run.

## Numbers
- Sign-up shows a $500 per month plan, priced in agent compute units. ([2:30](https://youtu.be/rfWx5zB0Cws?t=150))
- Narrator's own estimate: about $8 per hour for the agent, derived from the plan price. ([2:30](https://youtu.be/rfWx5zB0Cws?t=150))
- Vendor says its SWE-bench results beat older models, and its proprietary benchmark beats o1-preview. No scores are shown. ([1:02](https://youtu.be/rfWx5zB0Cws?t=62))
- Devin runs the image model across all rows of the dataset worldwide. No row count or run time is given. ([3:57](https://youtu.be/rfWx5zB0Cws?t=237))

## Hot takes
- The 'could replace junior devs' title is hype. The video's own demos show repeated fix-run loops, print-statement debugging and a leaked URL, not a finished junior-dev replacement.
- The $8/hour figure is the narrator's arithmetic on a $500/month plan, not a number the product states.
- The first minute is Cognition's own GA clip, so the opening is a vendor pitch.
- Claims that Cursor is better and that Devin is a waste of money are reported as things the narrator read, with no evidence cited.
- The live-share leak is reported secondhand. The narrator's takeaway, that agents need more permission controls, is his opinion.

## Tools mentioned
Devin (Cognition), Slack, GitHub, VS Code Live Share, Rust documentation (consulted by the agent), SWE-bench (vendor-reported results), o1-preview (comparison model, named in video), Cursor (mentioned in others' takes)

## Relevance to our work
- **agentos** (1/3): Devin is a hosted coding agent with a remote shell and editor, and its live-share leak shows what happens when remote agent-machine URLs are not access-controlled. This is a sandbox-access lesson, not a design to copy. → *Audit Crucible's remote access paths (celld shell or editor URLs) for auth and expiry; a leaked link should not give full agent-machine access.*
- **prosharness** (1/3): ProsHarness wants phone-driven approvals and status on long runs. Devin's Slack-assign and in-thread progress loop is a concrete pattern for that feedback channel. → *Compare Devin's Slack task-and-progress loop with ProsHarness's phone-approval flow, and borrow the in-thread progress feed.*
