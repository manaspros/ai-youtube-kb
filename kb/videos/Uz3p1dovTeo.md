# We Tested Google’s New AI Coding Tool Opal (Honest Review)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Uz3p1dovTeo` · [watch](https://youtu.be/Uz3p1dovTeo) · **date:** 2025-11-02 · **length:** 10:49 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Andrus · **orgs:** Better Stack, Google, Google Labs
- **topics:** vibe-coding-app-building, product-ux · **tags:** google-opal, no-code, node-based-workflows, hands-on-review, google-maps-api, image-generation, content-security-policy, prompt-variance, app-sharing

> Hands-on review of Google's Opal, a node-based no-code tool for building AI "mini apps" from text prompts. The reviewer finds weak output control, broken image embedding, and no real sharing or embedding path.

## Summary
The host (Better Stack's Andrus) builds a traffic-planner mini app in Google's Opal from a single text prompt, which generates a node graph of search, Maps, weather, summary, image-generation and output steps. He reports that the first run produced an AI illustration instead of a map and missing transit or time details, and that the Theme tab only changed the app's thumbnail icon. Rewriting one node's prompt to name the Google Maps Static API and build a map URL produced a more detailed route summary on the next run, but the image was still broken. Inspecting the element and opening the image URL directly showed a valid key and a working image, so the failure was a content security policy on the output page, which he could not edit. The same unchanged summary prompt also gave noticeably different answers across runs. Sharing gave only a plain URL with no embed or API, and an incognito visit was redirected to the product page. His verdict is that Opal needs finer node control, access to the underlying code, and embedding or an API layer before it is usable. He names Claude Code, Kiro and Spark as the vibe-coding tools Google needs to beat, and says it is free but US-only through Google Labs.

## Key ideas
- **Opal is pitched as a no-code, node-based builder where a plain-text description becomes a graph of prompts, models and tools that run as a shareable mini app.** — The app is generated from one prompt, with each node editable in natural language or by drag and drop. No backend or API setup is needed. ([0:00](https://youtu.be/Uz3p1dovTeo?t=0))
- **The reviewer's core question is how much control users get over individual nodes and whether they can bind in other Google APIs.** — He tests this by asking for Google Maps data in a route app. The question frames the rest of the review. ([1:03](https://youtu.be/Uz3p1dovTeo?t=63))
- **The auto-generated graph is opaque: it searched the web and maps, added an image-generation step with a free-quota warning, and included a prompt that claims real-time traffic data.** — The graph runs search, Maps, weather and summary nodes in sequence. The reviewer flags the real-time traffic claim as hallucinated by the underlying Gemini model. ([2:16](https://youtu.be/Uz3p1dovTeo?t=136))
- **Output quality varied a lot between runs with the same summary prompt, and the first run missed details that a later run included.** — The reviewer had not changed the summary prompt. He suggests the variance is the LLM output, since no seed is available, and he does not measure it. ([7:09](https://youtu.be/Uz3p1dovTeo?t=429))
- **Naming the exact API in a node prompt, here the Google Maps Static API, changed what the node produced.** — The rewritten instruction got the model to build a map image URL. The result was an image that the page would not display. ([5:50](https://youtu.be/Uz3p1dovTeo?t=350))
- **The broken image came from a content security policy on the generated output page, not from a bad API key or a bad image.** — The image URL worked when opened directly in a new tab. The reviewer could not edit the generated HTML to relax the policy. ([7:09](https://youtu.be/Uz3p1dovTeo?t=429))
- **Sharing and reuse are limited: apps can be shared only as a plain URL, with no embed option, no code access and no API layer.** — The shared link was not reachable in incognito and redirected to the main product page. The reviewer calls this the main gap for real use. ([8:27](https://youtu.be/Uz3p1dovTeo?t=507))

## Techniques
- **Precise API-naming node prompt** — Instead of asking an LLM node to 'use Maps', state the exact API and the artifact to build, for example 'construct a URL for the Google Maps Static API that shows the route between the two addresses'. The reviewer reports the model then picked the right service and built a URL. *When:* When a generated no-code node picks the wrong output type or vague tool, so the prompt must name the exact service and return format.
- **Separating a broken image from a bad URL** — Inspect the element to read the image src. Open that URL in a fresh tab. If it loads, the URL and key are fine and the failure is in the page, for example a content security policy. The reviewer used the browser console to see the CSP error. *When:* When an AI-generated page shows a broken image and you need to tell whether the problem is the asset, the credentials or the page's security policy.
- **Re-running to measure variance** — Run the same app with the same input several times and compare how much the output differs. The reviewer does this informally, with two runs of the summary node that differed in detail. *When:* Before trusting a single run of a generated LLM workflow, especially when there is no seed and the prompt has not changed.

## Numbers
- Video length is 10:49. The review covers three app runs, one per prompt or key change, and no benchmarks or latency figures are reported. ([0:00](https://youtu.be/Uz3p1dovTeo?t=0))
- Image generation in the generated flow shows a warning about a limited free quota. ([3:25](https://youtu.be/Uz3p1dovTeo?t=205))
- Opal is free but available only in the US, through Google Labs. ([9:45](https://youtu.be/Uz3p1dovTeo?t=585))

## Hot takes
- Opal's Theme tab produced an icon, not a theme, and nothing in the layout changed when toggled.
- The reviewer calls the generated real-time traffic claim hallucinated, and he says the output needs user control to be usable.
- Sharing an app is a plain URL with no embed or API, so the reviewer asks what the point of sharing is.

## Tools mentioned
Google Opal, Gemini, Imagen 4 (heard as Imogen4 in captions), Google Maps API, Google Maps Static API, Google Search, Claude Code (heard as Cloud Code in captions), Kiro, Spark

## Relevance to our work
- **agentos** (1/3): Shows run-to-run output variance and a broken-output debugging path in a generated LLM workflow, which applies to any eval or harness design. → *When adding evals for agent workflows, run each case several times and report the spread, not one sample.*
