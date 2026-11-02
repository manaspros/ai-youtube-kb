# Automate Your Browser with AI Using StageHand AI Agent

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `PPutzww1RaM` · [watch](https://youtu.be/PPutzww1RaM) · **date:** 2025-11-02 · **length:** 5:49 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed AI LABS presenter · **orgs:** Browserbase, Cursor, OpenAI
- **topics:** voice-multimodal, coding-agents · **tags:** stagehand, browser-automation, playwright, browserbase, zod, structured-extraction, cursor, quickstart, gpt-4

> Short quickstart for Stagehand, a Playwright-based browser agent with plain-language act, goto and extract APIs, scaffolded with a create-app command and driven from Cursor.

## Summary
The presenter opens with a demo in which Cursor's Cmd+K generates a Stagehand script that scrapes IMDb for movies releasing in January, using GPT-4 through an API under the hood. He then describes Stagehand as a browser-controlling agent built on Playwright, with three APIs: an action API that takes plain-text instructions for the current page, a goto API for navigation, and an extract API that returns structured data matching a Zod schema. He claims the generated Playwright code is durable, self-healing and repeatable, but does not show any of that. The setup walkthrough covers scaffolding the project with the create-app command, entering an OpenAI key, choosing between a local Chromium browser and Browserbase cloud sessions, then running npm install and npm start. A second demo has Cursor write a step that opens a GitHub repo and extracts its description. The video is a thin quickstart with no evaluation, error handling or cost discussion.

## Key ideas
- **Cursor's Cmd+K writes the Stagehand script from a plain-English request, and the presenter accepts it and runs it.** — The demo asks for upcoming January movie names from IMDb. The browser scans the page and GPT-4, called through an API, returns the names. The same workflow is repeated for a GitHub repo description. ([0:00](https://youtu.be/PPutzww1RaM?t=0))
- **Stagehand exposes three APIs: act (plain-text action on the current page), goto (navigate to a URL), and extract (structured output).** — The act API is spoken as 'DAC' in the captions, which is probably an auto-caption error. Extract takes a Zod schema and returns data in that shape, for example search results. ([1:13](https://youtu.be/PPutzww1RaM?t=73))
- **The presenter claims Stagehand writes durable, self-healing, repeatable Playwright code, but does not demonstrate it.** — No retry, failure or drift example is shown. The claim is the speaker's, so treat it as unverified. ([1:13](https://youtu.be/PPutzww1RaM?t=73))
- **Setup asks for a model API key and whether to run the browser locally or in Browserbase sessions.** — The key can be entered during setup or later in .env. Browserbase is offered with 10 free sessions. The presenter picks local, which downloads a Chromium build during npm install. ([2:41](https://youtu.be/PPutzww1RaM?t=161))
- **The starter project keeps its example code in a main file, and the presenter puts new code below the instructions there.** — The presenter opens the project in Cursor and writes the new step in the main file. He then runs npm start, which launches Chromium, navigates to the target page and extracts the data. ([4:09](https://youtu.be/PPutzww1RaM?t=249))

## Techniques
- **Scaffold a Stagehand project** — Run `npx create-browser-app` (the caption reads 'npx create browser app'). Accept the defaults or pick a custom model provider, name the project, enter the model API key now or later in .env, and choose local or Browserbase browser sessions. Then cd into the project directory (quoted in single quotes), run `npm install` (this downloads a local Chromium build), and run `npm start` to run the example script. *When:* First run, when you want a working Stagehand project with the least configuration.
- **Plain-language page actions and extraction** — Call the act API with a natural-language instruction for the current page. Use goto to change the URL. Call extract with a Zod schema describing the fields you want, and get back a typed object. *When:* Scraping or browsing a site where selectors would be brittle, and you want structured output instead of raw HTML.
- **Generate Stagehand code in Cursor** — Open the project in Cursor, select the spot below the instructions, and use Cmd+K to describe the browser step in English. Review the generated code, accept it, save, and run npm start. *When:* Drafting small automation scripts quickly with an AI editor. The presenter does not show any review or testing step.

## Numbers
- Browserbase offers 10 free browser sessions in the setup prompt. ([2:41](https://youtu.be/PPutzww1RaM?t=161))
- The demo's model is GPT-4 called through an API, and the setup asks for an OpenAI API key. ([0:00](https://youtu.be/PPutzww1RaM?t=0))
- Total video length is 5:49. ([5:37](https://youtu.be/PPutzww1RaM?t=337))

## Hot takes
- The durable, self-healing, repeatable claim for Stagehand is not shown in the video, and the demos succeed on the first run.
- Cursor's Cmd+K is presented as the way to write the automation, with no review or testing step before running it.
- Overall this is a quickstart that copies the install steps from the README. The Zod-based extract API is the only reusable idea.

## Tools mentioned
Stagehand, Playwright, Browserbase, Cursor, Zod, Chromium, GPT-4 (via OpenAI API), Node.js / npm / npx

## Relevance to our work
- **agentos** (1/3): Browser automation with structured extraction could be a tool option for Crucible's sandboxed execution, but the video says nothing about sandboxing, safety or cost. → *If Crucible ever needs a browser tool, compare Stagehand's extract API (Zod schema to typed output) with the output-schema approach already used in AgentOS tool calls.*
