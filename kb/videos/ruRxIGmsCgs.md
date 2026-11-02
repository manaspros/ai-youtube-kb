# Deploy Project to Netlify Instantly.

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `ruRxIGmsCgs` · [watch](https://youtu.be/ruRxIGmsCgs) · **date:** 2025-11-02 · **length:** 6:31 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Windsurf (Codeium), Netlify, GitHub, Cursor
- **topics:** vibe-coding-app-building, coding-agents · **tags:** windsurf, cascade, deploy, netlify, static-hosting, landing-page, wave-6, github-claim, deploy-logs, mcp, turbo-mode, commit-message

> Windsurf Wave 6 adds "deploys": Cascade publishes a static site to Netlify under a windsurf.build subdomain, which must be claimed in your own Netlify account within 24 hours.

## Summary
The creator demos Windsurf Wave 6's new deploy feature, which lets you ask the Cascade agent to publish a project without leaving the editor. It is hosted on Netlify, so it only suits static sites; full-stack apps with microservices are not supported. The walkthrough covers creating a netlify.toml, choosing a subdomain (the main windsurf.build domain is fixed), uploading files, and viewing the live URL. Deployments are removed after 24 hours unless claimed by linking GitHub to your own Netlify account, which the speaker calls the most important step. A second, journal-app deploy failed because of a deprecated component; the fix path shown is copying the Netlify deploy log back into Windsurf, but the speaker dropped that project rather than fixing it on camera. The rest of the video lists other Wave 6 features (MCP and turbo mode on enterprise plans, commit-message generation from the diff, a chat table of contents, and long conversations without starting a new chat). Overall this is a short product feature demo with a few practical habits, not a deep technical talk.

## Key ideas
- **Windsurf Wave 6 adds a deploy feature: you ask Cascade to deploy and it publishes the project from inside the editor without an external host.** — The demo landing page was served from a windsurf.build URL rather than localhost, so the deploy is a hosted static site. ([0:00](https://youtu.be/ruRxIGmsCgs?t=0))
- **Under the hood the deploy target is Netlify, which only hosts static sites. Full-stack apps and microservices do not fit this path.** — The speaker recommends it mainly for landing pages, which are mostly static. ([0:00](https://youtu.be/ruRxIGmsCgs?t=0))
- **The first step is generating a netlify.toml. Then the agent asks for a subdomain, uploads files, and reports build status and a link to view the deployment.** — The main domain is fixed to windsurf.build; only the subdomain (here clarity-minimal-landing) can be changed. ([1:35](https://youtu.be/ruRxIGmsCgs?t=95))
- **Unclaimed deploys are hosted for only 24 hours. To keep one, you authenticate Netlify with GitHub and claim the project into your own Netlify account.** — The speaker calls claiming the most important step; after claiming, the site appears in the Netlify sites list. ([1:35](https://youtu.be/ruRxIGmsCgs?t=95))
- **Responsive output comes from the prompt. The speaker asked for a responsive page using only HTML, CSS and JavaScript and tested it on a phone.** — Minor UI issues still needed manual fixes after generation. ([2:58](https://youtu.be/ruRxIGmsCgs?t=178))
- **Ask for both pages and modals during brainstorming before handing the spec to the agent. The speaker says this produced a UI with no errors in the journal app.** — This is a single anecdote, not a measured comparison. ([3:20](https://youtu.be/ruRxIGmsCgs?t=200))
- **A failed deploy can be debugged by copying the full deploy log from the Netlify dashboard and pasting it back into Windsurf.** — The failure came from a deprecated component. The speaker chose to skip that project instead of fixing it on camera. ([4:20](https://youtu.be/ruRxIGmsCgs?t=260))
- **Other Wave 6 features include MCP support and turbo mode (enterprise plan only), commit-message generation from the diff, a chat table of contents, and long conversations without starting a new chat.** — The speaker says MCP support was the main reason they had not used Windsurf before, having used Cursor. ([5:20](https://youtu.be/ruRxIGmsCgs?t=320))

## Techniques
- **Agent-driven static deploy** — Prompt Cascade to deploy the project. It creates netlify.toml, asks for a subdomain, uploads all files, then reports build status and gives a view-deployment link. Static sites only. *When:* Quick hosting of a landing page or other static front end without leaving the editor.
- **Claim within 24 hours** — Log into GitHub, authenticate Netlify with GitHub, open the claim page the deploy prompt links to, and claim the project. Once claimed it appears in your Netlify sites. *When:* Any deploy you want to keep past 24 hours. Without a claim it expires.
- **Deploy-log feedback loop** — If the deploy fails, open the Netlify dashboard's deploy section, copy the full build log, and paste it into Windsurf so the agent can troubleshoot. *When:* A build fails for a reason the agent cannot see, such as a deprecated dependency or component.
- **Plan pages and modals first** — During brainstorming, ask the AI for the full list of pages and modals before building, then pass that plan to Windsurf or Cursor. *When:* Starting a multi-screen front-end app so UI gaps show up before code is written.
- **Specify constraints in the build prompt** — State the stack (HTML, CSS, JavaScript only) and the requirement (responsive) in the prompt that generates the landing page. *When:* Generating simple static pages that must work on mobile.

## Numbers
- Unclaimed Windsurf deploys are hosted for 24 hours before the claim is needed. ([1:35](https://youtu.be/ruRxIGmsCgs?t=95))
- Subdomain is the only part of the URL the user can change; the windsurf.build main domain is fixed. ([1:35](https://youtu.be/ruRxIGmsCgs?t=95))
- Video runtime is 6:31; the landing-page demo and the failed journal-app deploy each take roughly 1-2 minutes. ([0:00](https://youtu.be/ruRxIGmsCgs?t=0))

## Hot takes
- Windsurf deploys are only for static sites on Netlify, so the feature is not a general hosting answer. The speaker says so directly.
- The 24-hour expiry without a claim is the most important detail and the video treats it as a hidden gotcha.
- The failed deploy was not fixed on camera. The speaker moved to a simpler project, so the troubleshooting loop is shown but not proven.
- The title 'Deploy Project to Netlify Instantly' overstates it: the feature needs a claim step and only works for static sites.
- Quality is capped at 2 because this is a single-product feature walkthrough with thin general lessons; it is not a sponsored segment.

## Tools mentioned
Windsurf (Wave 6, Cascade agent), Netlify, GitHub, Cursor, netlify.toml

## Relevance to our work
- **prosharness** (1/3): The deploy-failure loop (copy the build log back to the coding agent) is a small example of the feedback pattern ProsHarness uses for long runs, but this video does not add anything new to it. → *Optional: if ProsHarness ever deploys a static artifact, check whether its failure path already passes build logs back to the agent. No change needed based on this video alone.*
