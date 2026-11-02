# Google Just Solved The Greatest Limitation of AI Agents

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `uprZUcv0FSc` · [watch](https://youtu.be/uprZUcv0FSc) · **date:** 2026-03-02 · **length:** 10:11 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** AI LABS host (unnamed in transcript) · **orgs:** Google, Microsoft, Brilliant (sponsor)
- **topics:** mcp-and-tools, voice-multimodal, coding-agents · **tags:** webmcp, browser-agents, declarative-api, imperative-api, contextual-tool-loading, chrome-canary, claude-code, nextjs, tool-design, tool-descriptions

> Walkthrough of WebMCP, a proposed browser standard where websites register callable tools for agents instead of agents guessing from screenshots or DOM. Covers declarative and imperative APIs, per-page tool loading, and current limits.

## Summary
The host argues that vision-based and DOM-parsing browser agents are non-deterministic, and that WebMCP (Google with Microsoft) inverts this by having sites declare their actions as tools that agents call directly. He demos a restaurant booking form filled and submitted by Claude Code through a community WebMCP bridge. WebMCP has two APIs: a declarative one, where tool name, description and parameter descriptions are declared on an HTML form, and an imperative one for multi-page apps, where tools are registered and unregistered as the user navigates (a Next.js demo). He reports the official state as early: no official docs, a Chrome Labs repo with two demos, and support only in Chrome Canary, with Gemini as the intended agent. He notes the bridge breaks on tool switching in the imperative demo. Practical advice: keep to about 50 tools per page, write descriptions for someone who has never seen the site, and treat it as a dev trial until Chrome 146. The video is a practitioner demo with real implementation detail, but the title overstates what is shown.

## Key ideas
- **Invert the browser-agent problem: sites expose actions as tools rather than agents guessing from pixels or HTML** — Vision-based (annotated screenshots) and DOM-parsing agents both make a best guess each time, so results are non-deterministic. WebMCP has the site register its available actions as tools, and the agent reads the list and calls them directly. ([0:00](https://youtu.be/uprZUcv0FSc?t=0))
- **Two APIs for two complexity levels** — The declarative API covers simple workflows such as HTML forms. The imperative API covers full web apps with multiple pages and JavaScript execution, and needs more implementation work. ([2:04](https://youtu.be/uprZUcv0FSc?t=124))
- **Current status is early and Chrome-locked** — No official documentation yet. The Chrome Labs WebMCP repo has two demos, only one hosted. The official support is in Chrome Canary only, and the host says Claude Code cannot use it natively because it is meant for browser agents. A community bridge plus extension makes Claude Code work. ([2:43](https://youtu.be/uprZUcv0FSc?t=163))
- **Declarative API: declare the tool on the form and let the browser read it** — For a plain HTML form, you declare the tool name, tool description and parameter descriptions. The agent adds these declarations, and the browser reads them from the HTML. The host's guides were reverse-engineered from the demos in the WebMCP repo. ([4:11](https://youtu.be/uprZUcv0FSc?t=251))
- **Imperative API: register tools per page with contextual loading** — In a Next.js/React app, one library file declares all tools as functions with definitions. Each page's tools are registered on landing and unregistered on leaving, so the agent only sees tools for the current page. This avoids context overload when a site has 100+ tools. ([5:12](https://youtu.be/uprZUcv0FSc?t=312))
- **Bridge limitation: tool switching breaks on the community bridge** — In the imperative demo, Claude Code's session could not see the homepage tools after starting on checkout, and could not see the add-to-cart button on the product page. The host had to add an item manually. Once on checkout, the agent completed the order. ([6:28](https://youtu.be/uprZUcv0FSc?t=388))
- **Platform advantage favours Gemini inside Chrome; still worth implementing** — The intended agent is Gemini, built into Chrome, so non-Google agents need a bridge. The host says the standard is useful regardless. Guidance: at most 50 tools per page, focus on specific page actions, and write descriptions as if explaining to someone who has never seen the site. ([7:54](https://youtu.be/uprZUcv0FSc?t=474))
- **Dev trial only for now** — The API surface may change. The host says Chrome 146 (March) brings broader support, and advises against shipping to production until then. ([9:00](https://youtu.be/uprZUcv0FSc?t=540))

## Techniques
- **Declarative WebMCP tool on an HTML form** — Declare three things inside the form: the tool name, the tool description and the parameter descriptions. The browser reads these from the HTML. The host let the agent (Claude Code) add the declarations, using a guide reverse-engineered from the WebMCP repo demos. Exact attribute names are not shown in the video. *When:* A single-page or simple form workflow such as a booking form, where one set of fields maps to one action.
- **Imperative WebMCP tool registration per route** — In a Next.js/React app, create a library file that declares every tool as a function with a definition. On page mount call the page's register function (for example, register home tools), and on unmount call the matching unregister function. Only the current page's tools are visible to the agent. *When:* Multi-page web apps with many actions, where loading every tool at once would overload the agent's context.
- **Scope tool lists to the page (contextual loading)** — Expose only the tools for the current page, so the agent sees a small, focused set. Keep under the spec's suggested 50 tools per page. The host says the tool list changed between homepage (3 tools) and cart (4 tools). *When:* Any site with more tools than a page's actions need, to avoid context bloat and wrong-tool choices.
- **Write tool descriptions for a cold reader** — Describe each tool as if explaining the action to someone who has never seen the site. The host says agents pick tools from these descriptions, and vague ones lead to the wrong tool or no tool. *When:* Whenever you define any WebMCP tool, since descriptions drive tool selection.
- **Inspect tool schemas with the Model Context Tool Inspector extension** — Install the extension, then open a page that has WebMCP. It detects the tools on the page and shows each tool's input schema. The host also used it to see the tool list change after filters were applied. *When:* Verifying what a page exposes, and debugging a tool whose arguments look wrong.
- **Test with the Gemini-backed demo paths** — The flight-search demo offers two modes: fill custom input arguments yourself, or set a Gemini API key and give a plain English prompt that the page turns into tool calls. The demo was run in Chrome Canary. *When:* Trying the standard without a bridge, using Chrome Canary and a key for Gemini.

## Numbers
- Recommended maximum of 50 tools per page in the spec ([7:54](https://youtu.be/uprZUcv0FSc?t=474))
- Restaurant booking demo: one tool, BookTable, on the page ([0:00](https://youtu.be/uprZUcv0FSc?t=0))
- Flight search demo: 1 tool, which grew to 4 tools (3 of them filters) after switching to the travel site ([2:43](https://youtu.be/uprZUcv0FSc?t=163))
- Next.js demo: 3 tools on the homepage, 4 tools on the cart page ([5:12](https://youtu.be/uprZUcv0FSc?t=312))
- Chrome 146 expected in March with broader support ([9:00](https://youtu.be/uprZUcv0FSc?t=540))

## Hot takes
- The title overstates the result. The video shows a working form demo and a shaky imperative demo, with no official docs and Chrome Canary only, so the 'solved' claim is not supported.
- The host argues Google is not locking anyone out, only using its browser and audience advantage. This is opinion, not evidence.
- The host advises not shipping to production until Chrome 146, so the video is best read as an early preview.
- Brilliant sponsor segment at about 9:00 is short and separate from the technical content. It does not lower the quality score.

## Tools mentioned
WebMCP, Chrome Canary, Chrome 146, Chrome Labs WebMCP repo, Model Context Tool Inspector extension, Claude Code, Gemini (built into Chrome; Gemini API key option in the demo), Next.js, React, Zen browser, Community WebMCP bridge (unnamed, not identified), Brilliant (sponsor)

## Relevance to our work
- **agentos** (1/3): Page-scoped tool exposure is a control-plane idea that could sit alongside AgentOS's budget and guardrail pillars, but WebMCP is browser-side and not a proxy concern. → *Read the WebMCP spec's per-page tool limit and descriptions as a reference when designing per-route tool allowlists for AgentOS agents.*
- **prosharness** (1/3): ProsHarness drives Claude Code. This video shows a community bridge that lets Claude Code call browser-page tools, and documents where it breaks (tool switching). → *If ProsHarness needs browser control, compare the community WebMCP bridge's behaviour on route changes before relying on it.*
- **general** (1/3): The idea that sites should expose deterministic actions instead of agents guessing from pixels or DOM is a general pattern for agent-facing web design. → *Read the WebMCP repo's two demos to see the tool schema shape before deciding whether to adopt it.*
