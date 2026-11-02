# I Found a Tool That Breaks MCP (In a Good Way)

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `6R7CoIKKkDE` · [watch](https://youtu.be/6R7CoIKKkDE) · **date:** 2025-11-02 · **length:** 7:55 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed AI LABS host · **orgs:** Tempo Labs, Supabase, Firecrawl, ElevenLabs, Google, OpenAI, Anthropic
- **topics:** vibe-coding-app-building, mcp-and-tools · **tags:** mcp, mcp-app-store, vibe-coding, tempo-labs, elevenlabs, supabase, firecrawl, api-integrations, prd, nextjs

> Tempo Labs' MCP app store packages third-party APIs as MCP servers with docs built in; the host builds an ElevenLabs quotes app by installing integrations and prompting. Promotional, single happy-path demo.

## Summary
AI LABS walks through Tempo Labs' new MCP app store, where third-party APIs are packaged as MCP servers with their documentation bundled, so a vibe-coding app builder can call them without the user reading docs. The host connects Supabase, installs Firecrawl and ElevenLabs by pasting provider API keys, and has Tempo generate a PRD and mermaid user flow for a quotes app that reads quotes aloud. He then prompts for a multi-voice dropdown, which pulls every voice from his ElevenLabs library, and says the share and save features appeared from the generated user flow. The evidence is one happy-path build with no failure cases, no cost, latency or quality data, and no comparison against simply putting API docs in context. Setup still needs accounts and API keys, which the host acknowledges. The tone is product-promotional and the transcript carries no sponsorship disclosure.

## Key ideas
- **Vibe-coding tools often lack third-party API docs, so integrations are hard to wire up even though the models know React and TypeScript well.** — The host frames the problem: builders such as Lovable, Bolt and Firebase Studio do not fetch external API documentation, and the docs must otherwise be read or fed to the model by hand. ([0:00](https://youtu.be/6R7CoIKKkDE?t=0))
- **Tempo's MCP app store puts each external API on an MCP server with its full documentation built in, so installing the integration is the setup step.** — The host's claim is that the agent then knows how to connect to each service without the user reading docs or explaining the API. API keys are still required. ([1:14](https://youtu.be/6R7CoIKKkDE?t=74))
- **Backend first: connect Supabase before adding other integrations.** — Create a Supabase account and an organization, authorize Tempo, then pick an existing project to link it. Supabase then shows as linked and usable. ([1:14](https://youtu.be/6R7CoIKKkDE?t=74))
- **Integration install is paste-a-key: open the provider's dashboard, copy the API key, paste it into the store, connect, then tell the agent the app is installed.** — Demonstrated with Firecrawl (web crawling, optionally piped to an LLM such as Gemini for summaries) and ElevenLabs (text-to-speech). ([2:25](https://youtu.be/6R7CoIKKkDE?t=145))
- **PRD first: the tool drafts a PRD, a user flow and a mermaid diagram from the idea, and the user edits the PRD before any building starts.** — The quotes app PRD is generated automatically. The flow is expandable and editable, and build prompts run against the PRD and flow. ([2:25](https://youtu.be/6R7CoIKKkDE?t=145))
- **Starter template gives a landing page and auth, and the build is then steered by prompts such as anonymous test-mode sign-in.** — The Next.js starter kit includes authentication and shadcn-style components. The agent builds the app, then adds a test mode that signs users in anonymously. ([3:35](https://youtu.be/6R7CoIKKkDE?t=215))
- **A feature prompt that describes the whole behavior gets the integration's full catalog: the voice dropdown pulled every voice from the ElevenLabs library.** — The host says the prompt covered the multi-voice dropdown and how the setup should work. An earlier voice-generation bug was caught by error logging the host had added, and was fixed before the feature prompt. ([5:00](https://youtu.be/6R7CoIKKkDE?t=300))
- **Share and save features appeared from the generated user flow without separate prompting; the host says he never checked the ElevenLabs docs.** — Share opens the macOS share sheet and save stores quotes in a saved-quotes section. The host calls the integration seamless but says he has not explored the rest of the app. ([6:29](https://youtu.be/6R7CoIKKkDE?t=389))

## Techniques
- **Connect the backend before the integrations** — In Tempo: create a Supabase account and an org, authorize Tempo under Supabase, pick a project (the host used one named Test) and connect it. Supabase then shows as linked. *When:* When the app needs a database or auth and you want the agent to have it from the start.
- **Install an integration from the MCP app store** — Open the app store's Browse section, click the integration (Firecrawl, ElevenLabs, and others such as OpenAI, Anthropic and Gemini are shown), click Install, paste the provider's API key from its dashboard, click Connect, then tell the agent the app is installed so it starts using it. *When:* When the model does not know a third-party API well enough to integrate it from memory, and you want to avoid pasting docs into context.
- **PRD and user flow as the build spec** — Describe the app; the tool generates a PRD and a user flow with an expandable mermaid diagram. Edit the PRD or add detail, then prompt the agent to build from the PRD and flow. *When:* For greenfield app builds where you want a reviewable spec before code is generated.
- **Describe the full behavior in one feature prompt** — The host prompted for a dropdown of ElevenLabs voices and explained how the multi-voice setup should work in the same prompt. The exact prompt text is not shown on screen. *When:* When you want an integration feature built end-to-end, including the list of options from an external API.
- **Add error logging before debugging a broken integration** — The host added logging so that an integration failure (voice generation) would surface a notification, then used the log to find the fault. *When:* When an external API call fails silently or the cause is unclear.

## Hot takes
- Promotional framing ('It really is that simple', 'honestly this looks amazing') with one happy-path build and no failure cases, so quality is capped at 2.
- The title 'Breaks MCP' is not substantiated in the video; MCP appears only as the packaging layer Tempo uses.
- The 'no docs needed' claim rests on the host's own observation from one ElevenLabs build; the video does not show the agent failing without docs.
- The host says he has not fully tested the quote playback or explored the rest of the app, yet calls the integration 'super seamless'.
- The transcript has no sponsorship disclosure, but the content is product-only with a vendor-style pitch.

## Tools mentioned
Tempo (Tempo Labs app builder, with its MCP app store), Model Context Protocol (MCP), Supabase, Firecrawl, ElevenLabs (Eleven Labs API), Google Gemini, OpenAI, Anthropic (auto-caption reads 'Tropic'), Next.js (starter template kit), shadcn/ui (auto-caption reads 'Shadzian'), Mermaid, React, TypeScript, Lovable (mentioned), Bolt (mentioned), Firebase Studio (mentioned), ChatGPT (mentioned as an example API), macOS share sheet

## Relevance to our work
- **agentos** (1/3): The MCP app store packages each integration as an MCP server with its docs bundled, which is the same packaging question AgentOS's tool and skill catalog faces, but this is a product demo, not an architecture. → *Note how the store bundles per-integration docs with the MCP server; check whether AgentOS's registry entries carry usage docs and setup steps alongside the server endpoint.*
- **prosharness** (1/3): Each integration asks the user to paste an API key into a dashboard, which is the credential-handling problem ProsHarness is designed to avoid with zero-token handling. → *Compare the paste-API-key flow here with ProsHarness's zero-token credential handling; check whether an integration catalog could hold keys outside the model context.*
