# Build Apps Using ONLY your Voice (WARP 2.0 is Insane)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `4n7z4eb_aKU` · [watch](https://youtu.be/4n7z4eb_aKU) · **date:** 2025-11-02 · **length:** 7:39 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Bernard (Better Stack presenter, name as given in the transcript) · **orgs:** Better Stack, Warp, Tailwind CSS, Vercel, GitHub, Framer, Cursor
- **topics:** coding-agents, vibe-coding-app-building, dev-tools · **tags:** warp, agent-terminal, voice-prompting, multi-agent, auto-approve, deployment, github-pages, tailwind, vue

> Better Stack demos Warp 2.0's Code and Agents features by building several small web apps mostly from voice prompts, then deploys one. Mostly a demo with a few practical notes, and the title oversells it.

## Summary
The presenter introduces Warp 2.0, which adds Code (an agent builds features and diffs can be edited in a built-in editor) and Agents (several agents run in parallel). He tours the UI: Warp Drive for shared commands, rules, workflows and MCP servers, an input that auto-detects commands versus prompts, and voice input. He builds a Tailwind landing page, fixes an outdated install command by pointing the agent at the official docs via the Refine button, and adds Vue.js with one agent while another writes a README. He generates a login/registration full-stack app and a single-file agar.io-style canvas game from one prompt each, asks for hosting advice, and deploys the game to GitHub Pages using the agent's CLI commands. His verdict is that Warp's developer experience beats Cursor for web apps with fewer errors. His one complaint is that the agent does not notice npm run dev is already running and starts a second one. The video has no benchmarks and ends with a subscribe call-to-action.

## Key ideas
- **Warp 2.0 adds two features: Code, which builds features with an agent and lets you edit diffs in a built-in editor, and Agents, which runs and manages several agents at once.** — Framed as moving from a terminal to an agentic development environment (ADE). The video's stated plan is to build apps using only voice input and to try both features. ([0:00](https://youtu.be/4n7z4eb_aKU?t=0))
- **The UI has Warp Drive for shared team or personal commands, rules, workflows and MCP servers. The input bar auto-detects commands versus prompts, changes directory like cd, and accepts voice dictation and image or wireframe uploads.** — A mode switch sets terminal-command focus versus agent focus, or auto. The presenter uploads a Framer-made design as a reference image before prompting. ([1:03](https://youtu.be/4n7z4eb_aKU?t=63))
- **The Refine button corrects an agent's outdated setup steps. The presenter points it at the official docs for the install command, which fixes the Tailwind setup.** — Diffs can be edited in Warp's editor and then applied, which updates the diff again. A later instruction can change page content the same way. ([2:16](https://youtu.be/4n7z4eb_aKU?t=136))
- **Parallel agents work on separate tasks. One agent migrates the vanilla JS landing page to Vue components while another creates a git project and a README with improvement recommendations.** — Auto-approve actions is switched on so the agents run without review. The presenter notes the README agent ran before the app existed, so its output was weaker, and the Vue result changed little visually. ([3:39](https://youtu.be/4n7z4eb_aKU?t=219))
- **Single prompts produce larger apps. One yields a landing page, login/signup and a dashboard for projects and tasks, though navigation was missing because it was not requested. Another yields a single-file HTML5 canvas game inspired by agar.io.** — The presenter says the agent needs to be very specific about what it needs. The full-stack run is described with a time figure that the transcript wording makes ambiguous. ([4:54](https://youtu.be/4n7z4eb_aKU?t=294))
- **Deployment: the Deploy tab has no native Vercel or AWS integration. The agent recommended free hosts, favored GitHub Pages, and ran the deploy commands itself. Vercel CLI was mentioned as the path for other targets.** — The deployed game page opened successfully, but the presenter says it was 'not really a game'. ([4:54](https://youtu.be/4n7z4eb_aKU?t=294))
- **The presenter's verdict is that Warp's developer experience is better than Cursor's for web apps, with less distraction and fewer errors. His main criticism is that the agent does not detect a running npm run dev and starts a second one.** — He compares it to Cursor and asks viewers whether Warp beats Cursor or Claude Code. The comparison rests on his own experience with a few projects. ([6:15](https://youtu.be/4n7z4eb_aKU?t=375))

## Techniques
- **Refine-with-docs correction** — When the agent uses an outdated install or setup command, click Refine and tell it to follow the official docs. The presenter cites the Tailwind docs and asks for the npm install of the Tailwind Vite plugin (captions garble the package name, which is likely @tailwindcss/vite). *When:* The agent's first output relies on stale documentation or a deprecated install path.
- **Reference image plus voice prompt for UI** — Upload a wireframe or design screenshot to the agent input, then dictate the change with voice. Ask it to match the screenshot in its components. *When:* Recreating a design from a mockup or making a UI change hands-free.
- **Auto-approve for unattended agent runs** — Turn on the auto-approve actions setting before starting a long agent task, so it runs without review. *When:* Several agent tasks run in the background and you check the results later.
- **Parallel agent panels by concern** — Start a second agent panel for an unrelated task, such as docs or a README, while the first one builds the frontend. *When:* Frontend and docs or backend work are independent. Be aware the agents do not share state, so later results may be inconsistent.
- **Deploy by asking for a host, then letting the agent run it** — In the Deploy tab, ask which free host to use. Accept the recommendation and let the agent run the platform's CLI. *When:* Deploying a static page or simple app, and no platform integration exists in the tool.

## Numbers
- Keyboard shortcut for a new terminal tab: Cmd+T on macOS or Ctrl+T on Windows. ([1:03](https://youtu.be/4n7z4eb_aKU?t=63))
- Full-stack login/registration app generated from one prompt; the presenter gives a time of 'six and a half hours' (the transcript wording is ambiguous, and the figure may refer to the agent run). ([4:54](https://youtu.be/4n7z4eb_aKU?t=294))
- Ran 3 or more projects total (landing page, full-stack app, canvas game), and the deployed game is one of the outputs; no benchmarks or success rates are given. ([4:54](https://youtu.be/4n7z4eb_aKU?t=294))

## Hot takes
- Warp is better than Cursor for building web apps (developer experience, fewer errors, less distraction), based on the presenter's own experience.
- Warp's agent is not reliable about already-running processes: it starts a second npm run dev instead of detecting the first.

## Tools mentioned
Warp 2.0 (Warp Code, Warp Agents, Warp Drive), Tailwind CSS (Vite plugin), Vue.js, React (mentioned only), Vanilla JavaScript, HTML5 canvas, Framer (used for the reference design), GitHub Pages, Vercel CLI (mentioned), npm, Cursor (comparison), Claude Code (comparison), MCP servers

## Relevance to our work
- **prosharness** (1/3): Relevant only as a concrete example of a coding-agent harness that does not detect already-running dev servers, a problem ProsHarness's checkpoint and resume work may hit too. → *When ProsHarness resumes a run, check for an already-running dev server or process before starting another, and cover that case in its resume tests.*
