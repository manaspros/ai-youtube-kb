# Get Started with Claude’s Computer Use API – Full Setup & Demo

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `XSXaGvCRJ3c` · [watch](https://youtu.be/XSXaGvCRJ3c) · **date:** 2025-11-02 · **length:** 4:31 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** AI LABS presenter (unnamed) · **orgs:** Anthropic, AI LABS
- **topics:** voice-multimodal, sandboxing-execution, token-cost-efficiency · **tags:** computer-use, browser-agents, docker, sandbox, beta, claude-api, setup-demo

> A 4-minute walkthrough of Anthropic's Computer Use API beta: run the setup container locally with Docker and your API key, then watch Claude operate a sandboxed virtual Linux desktop from a chat prompt.

## Summary
The presenter introduces Anthropic's Computer Use API as a beta that lets Claude act on a screen from a text prompt. Setup follows the docs site's link to a GitHub page, where he copies the setup code, pastes it into a terminal, adds his own Claude API key, and runs it. Docker is required; he used WSL2 with Ubuntu on Windows. The container starts a web UI on a local port, with a chat box on the left and an isolated virtual Linux desktop on the right. He gives one prompt, asking it to find his most popular videos, and the agent browses YouTube by itself and identifies his top video. He says each step is a screenshot followed by an action, that the process is slow and token-expensive, and that he sped up the footage. There are no cost, latency or token figures, no code shown beyond the setup, and no coding task. He promises a follow-up video on coding tasks.

## Key ideas
- **Computer Use API lets Claude act on a screen from prompts** — The presenter frames it as a new beta where Claude performs tasks and takes actions on a computer based on a prompt. ([0:00](https://youtu.be/XSXaGvCRJ3c?t=0))
- **Setup is copy-paste from the GitHub repo linked from the docs site** — He copies the setup code from the GitHub page, pastes it into a terminal, replaces the placeholder with his own Claude API key, and runs it. The video does not show the exact commands. ([0:00](https://youtu.be/XSXaGvCRJ3c?t=0))
- **Docker is a hard prerequisite and the container exposes a local port** — Running the setup pulls a Docker container. When it finishes, a message gives a local port to open in the browser. He used WSL2 with Ubuntu on Windows. ([1:26](https://youtu.be/XSXaGvCRJ3c?t=86))
- **The model drives a virtual Linux desktop, not the host machine** — The right-hand pane is an isolated Linux desktop with basic apps. He says this is deliberate for security and because the feature is beta, so Claude has no control of his own computer. ([1:26](https://youtu.be/XSXaGvCRJ3c?t=86))
- **The action loop is screenshot, then action, then repeat, and it is slow and costly** — Claude takes a screenshot, decides the next action, and repeats. The speaker calls this very slow and token-expensive, and he sped up the footage. ([1:26](https://youtu.be/XSXaGvCRJ3c?t=86))
- **The demo prompt needs browsing and multi-step navigation** — The test prompt was to find the most popular videos on the presenter's YouTube channel. The agent can reach the internet and use a browser, so it has to navigate the site itself. ([1:26](https://youtu.be/XSXaGvCRJ3c?t=86))
- **The single successful run is the evidence for the claim** — After about two minutes of navigation the agent identifies his most popular video, a Bolt.new video. The speaker takes that one run as proof of capability, and no failures or repeated attempts are shown. ([3:16](https://youtu.be/XSXaGvCRJ3c?t=196))

## Techniques
- **Run computer use inside a disposable container** — Install Docker (WSL2 + Ubuntu on Windows in the video). Get the setup code from the Computer Use API GitHub README linked from the docs page. Paste it into a terminal, set your Claude API key in place of the placeholder, and run it. Wait for the container to pull and print a local port, then open that port in a browser. The UI shows a chat pane on the left and a virtual Linux desktop on the right. The desktop is isolated, so the agent cannot touch the host. *When:* Trying the beta without giving the model access to your real desktop. Use it for evaluating the feature, not for anything that needs your own apps or credentials.
- **Give a multi-step browsing prompt and watch the screenshot loop** — Write a plain-language goal (the demo used: go to my channel and find my most popular videos). The agent screenshots the desktop, picks an action (open browser, search, click), and repeats until done. Expect many steps and high token use per task. *When:* Quick smoke tests to see what the agent can do on a live site. Budget for slow runs and token cost before using it for repeated work.

## Numbers
- Video length is 4:31; the setup and demo are shown at roughly real speed for the setup and sped up for the agent run. No cost, latency, step-count or token figures are given. ([1:26](https://youtu.be/XSXaGvCRJ3c?t=86))
- The agent took a long time (the speaker says it took its sweet time) to reach the channel and identify the top video. The speaker gives no duration. ([3:16](https://youtu.be/XSXaGvCRJ3c?t=196))

## Hot takes
- The speaker calls Computer Use a game-changing feature and says this is where AI stands today, based on one successful run with one prompt.
- He says the feature is slow and expensive and still beta, which undercuts the enthusiasm in the intro and the closing claim.
- The title promises a full setup and demo, but the video covers setup in about a minute and shows no failures, prompts beyond one, or code.

## Tools mentioned
Claude Computer Use API (Anthropic, beta), Claude API key (Anthropic), Docker, WSL2, Ubuntu, Bolt.new (named only as the video the agent found on the channel, not used as a tool)

## Relevance to our work
- **agentos** (1/3): Crucible needs a sandboxed execution environment, and this shows a containerized virtual desktop for a GUI agent. It is a comparison point, not a design input. → *Note the Docker-isolated virtual desktop as one reference for a GUI or browser tier in Crucible, and compare it with the celld sandbox model before deciding whether Crucible needs a desktop tier at all.*
