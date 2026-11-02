# Browser Agents Don't Need Better Models. They Need Better Eyes. - Kushan Raj, Sarvam AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `JnubYCYunk8` · [watch](https://youtu.be/JnubYCYunk8) · **date:** 2026-07-18 · **length:** 4:26 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** Kushan Raj · **orgs:** Sarvam AI
- **topics:** voice-multimodal, context-engineering, token-cost-efficiency · **tags:** browser agents, page representation, DOM compression, screenshots, token cost, agent feedback loop, long-horizon tasks, open source

> Kushan Raj (Sarvam AI) argues browser agents fail because of their infrastructure, not model quality, and shows a compact page representation plus change feedback that makes a cheap model faster and more reliable.

## Summary
The speaker, Kushan Raj, a former founding engineer at Sarvam, says browser agents are not getting wide adoption and that the problem is the infrastructure around the model rather than the model itself. He describes a browser benchmark with about 30 sequential steps where a typical agent spent 10 to 20 seconds just to click a start button. His fix is a compressed representation of the page that lets the agent see the whole page in very few tokens, which he contrasts with a roughly 20,000-token full DOM and a roughly 1,100-token screenshot. He also feeds the agent explicit change feedback (new popups, removed blockers, clicks that had no effect) by tracking the page end to end. Demos compare a Claude-driven Aadhaar download that stalled for about two minutes with his faster agent, and a Kannada-language booking site where the baseline got stuck on the date picker. He plans to open source the project and expose it as an API that takes a URL and an intent, or as a website or plugin. The talk has no formal benchmark results and is short, so the claims rest on live demos and anecdotes.

## Key ideas
- **Browser agents underperform because the infrastructure around the model is weak, not because the models are not smart enough.** — The speaker's core thesis is that a good environment for the agent matters more than a bigger model. Long multi-step tasks fail because the agent cannot tell where it went wrong. ([0:00](https://youtu.be/JnubYCYunk8?t=0))
- **A 30-step browser benchmark exposes the problem, since one click can take 10 to 20 seconds.** — Long sequencing of tasks is what makes the benchmark useful. The speaker says the baseline agent took 10 to 20 seconds just to press the start button, and the run then needed about 30 steps. ([0:00](https://youtu.be/JnubYCYunk8?t=0))
- **Compress the page into a compact representation the model can read in very few tokens.** — The representation lets the agent see the whole page at once. The speaker compares it with a full DOM of around 20,000 tokens and a screenshot of around 1,100 tokens. ([1:14](https://youtu.be/JnubYCYunk8?t=74))
- **Give the agent change feedback, not only a snapshot.** — The agent is told which new elements appeared, which disappeared (for example a blocking overlay that was removed), and when a click did not take effect. The speaker says this comes from tracking the whole browser page end to end. ([3:58](https://youtu.be/JnubYCYunk8?t=238))
- **Pair the compressed representation with a screenshot, which keeps token cost low enough for a cheap model to plan long sequences.** — The speaker says the combination is cheap in tokens, so a cheaper model can reason well and build a long sequence of actions. ([3:58](https://youtu.be/JnubYCYunk8?t=238))
- **Claude-driven browsing stalled in both demos, and his setup finished quickly.** — In the Aadhaar download, the baseline took screenshots and scrolled for about two minutes after the button click. On a Kannada booking site, the baseline could not pick a date, while his agent selected it and finished. ([1:14](https://youtu.be/JnubYCYunk8?t=74))
- **The product direction is an API: give a URL and an intent, get the result back.** — The speaker plans to open source the code, since the code alone is not very defensible. The product could be an API, a website, or a plugin. His stated goal is faster, cheaper and more reliable browser agents. ([2:56](https://youtu.be/JnubYCYunk8?t=176))

## Techniques
- **Compact page representation for agents** — Replace the full DOM with a compressed view of the page that keeps the actionable elements and layout, then send it with a screenshot. The speaker says this cuts the token cost from around 20,000 tokens to a few thousand. *When:* Use when a browser agent's full-DOM prompts are too large or too slow, or when a cheap model must drive the page.
- **Delta feedback to the agent** — After each action, report what changed on the page: new elements, removed blockers, and actions that had no visible effect. Track the whole page state across steps so the agent can see where it failed. *When:* Use in long multi-step UI tasks where the agent loses track of state or retries the same failing click.
- **Invest in the environment instead of the model** — Improve the harness around the model (page representation, feedback, planning of multi-step sequences) and keep a cheaper model. *When:* Use when a browser agent is slow or unreliable and the model is already capable enough for the task.
- **Expose a browser task as an API** — Accept a target URL and a natural-language intent, run the browser agent, and return the result. The speaker suggests this as a product shape (or a website or plugin). *When:* Use when the same browser workflow should be reusable by other systems.

## Numbers
- Browser challenge benchmark has about 30 steps; the baseline agent took 10 to 20 seconds just to click the start button. ([0:00](https://youtu.be/JnubYCYunk8?t=0))
- Full DOM for the page is around 20,000 tokens. ([2:56](https://youtu.be/JnubYCYunk8?t=176))
- A screenshot of the page is about 1,100 tokens. ([2:56](https://youtu.be/JnubYCYunk8?t=176))
- The speaker's compressed representation is about 1,800 tokens. The caption reads 'my laptop got 1800 tokens', which is probably a transcription error, so this figure is uncertain. ([2:56](https://youtu.be/JnubYCYunk8?t=176))
- Baseline Claude run for an Aadhaar download took about two minutes after the button click, from about the 46-second mark until the end of the clip. ([1:14](https://youtu.be/JnubYCYunk8?t=74))

## Hot takes
- Browser agents are held back by infrastructure, not model intelligence.
- A cheap model with a good page representation beats a stronger model working from raw screenshots or full DOMs.

## Tools mentioned
browser agent harness (speaker's own, to be open sourced), Claude (used as the baseline in demos)

## Relevance to our work
- **agentos** (1/3): AgentOS Crucible (L2C) runs sandboxed execution and could host browser tools; the page-compression and delta-feedback ideas are relevant there but only if browser tools are added. → *If browser tools are ever added to Crucible, test a compact page-state format with change deltas against a full-DOM tool output on token cost and step count.*
- **prosharness** (1/3): ProsHarness runs long agent sessions with checkpoint and resume; the delta-feedback idea (report what changed after each action) may help long UI-driven runs. → *Read the speaker's open-source repo when published and compare its change-feedback format with ProsHarness checkpoint state.*
- **general** (1/3): Practical point that compact, delta-based observations can cut token cost for any tool that returns large UI state. → *Consider the same compact-plus-delta pattern for any agent tool that returns large state (for example, a long DOM or a big log).*
