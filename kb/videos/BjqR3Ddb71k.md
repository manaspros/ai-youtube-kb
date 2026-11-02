# The WhatsApp Trick That’s Running My Business for Me

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `BjqR3Ddb71k` · [watch](https://youtu.be/BjqR3Ddb71k) · **date:** 2025-11-02 · **length:** 6:29 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** ElevenLabs, Anthropic
- **topics:** mcp-and-tools, voice-multimodal · **tags:** whatsapp, mcp, elevenlabs, claude-desktop, voice-agent, customer-support, local-first, uv, golang

> A 6-minute setup tutorial for a local WhatsApp MCP server plus the ElevenLabs MCP in Claude Desktop, so an agent can read WhatsApp chats and reply with a synthesized voice note.

## Summary
The narrator argues that automated WhatsApp replies for small businesses are weak and that LLM and voice models can now handle customer messages. The video is a setup walkthrough: install a local WhatsApp MCP server (a Go bridge linked by QR code) and the ElevenLabs MCP into Claude Desktop, then configure both with uv/uvx and the Claude config file. Setup covers Windows caveats (CGO and a C compiler for the WhatsApp server). The demo has the agent fetch the latest messages from a contact called "Dad" and send a reply as a generated voice note. The narrator finds the default voice unnatural and points to ElevenLabs voice cloning as the fix. The closing section previews a planned Swift app that would run several separately configured WhatsApp "businesses" with voice assistants. Steps are described aloud, and exact commands and config keys are mostly not shown on screen.

## Key ideas
- **Automated WhatsApp Business replies are weak, and LLM plus voice models can read and answer customer messages in place of a human agent.** — The motivating claim for the whole video. It is stated as opinion, with no evidence or customer data. ([0:00](https://youtu.be/BjqR3Ddb71k?t=0))
- **The WhatsApp MCP server runs fully locally and talks to any MCP client, so messages are not sent to a third-party server.** — The speaker says the server runs on the user's own machine. The ElevenLabs MCP is a cloud API, which the video does not address. ([0:00](https://youtu.be/BjqR3Ddb71k?t=0))
- **Claude Desktop is the chosen client. Cursor and Windsurf are dismissed as coding IDEs that do not fit this use case.** — The speaker says any MCP client works and mentions newer open MCP clients as alternatives. The choice depends on the agent inside the client. ([1:20](https://youtu.be/BjqR3Ddb71k?t=80))
- **The WhatsApp bridge links to the phone by QR code, the same way WhatsApp Web does.** — The Go program in the bridge directory is run, and its QR code is scanned from the mobile app. The Go toolchain must be installed first. ([1:20](https://youtu.be/BjqR3Ddb71k?t=80))
- **Both MCP servers run through uvx, so uv must be installed. Cursor and Windsurf use a JSON MCP config file, and all three major clients follow the same format.** — The speaker says the three main clients share this config format. Cursor now uses a JSON file rather than the command method. ([2:35](https://youtu.be/BjqR3Ddb71k?t=155))
- **Windows needs an extra step only for the WhatsApp server: enable CGO and have a C compiler installed. The ElevenLabs MCP works unchanged.** — This is the only platform-specific caveat the speaker gives. ([2:35](https://youtu.be/BjqR3Ddb71k?t=155))
- **Test by asking the agent for the latest messages, naming the contact explicitly to avoid ambiguity, then reply with an ElevenLabs voice message.** — The demo specifies which of two contacts named Dad to use. The reply is a generated voice note. The speaker says it sounds slightly unnatural with the stock voice. ([4:00](https://youtu.be/BjqR3Ddb71k?t=240))
- **Voice cloning in ElevenLabs is presented as the fix for the robotic default voice, and the whole flow can then be prompted and automated.** — The speaker says two clone types exist and that a clone can be selected through a prompt. No cloning procedure is shown. ([5:31](https://youtu.be/BjqR3Ddb71k?t=331))
- **The next step is a custom tool or agent that assigns each tool individually, plus a planned Swift app that runs several WhatsApp chats as separate businesses, each with its own voice assistant.** — Both are described as future work. The speaker is exploring them and has not built them. ([5:31](https://youtu.be/BjqR3Ddb71k?t=331))

## Techniques
- **Local WhatsApp MCP setup in Claude Desktop** — 1) Install Go and uv (check with `which uv`). 2) Open Claude Desktop's Edit Config, paste the template block from the WhatsApp MCP repo, and add API keys where the template needs them. 3) Clone the repo. 4) Run the Go main.go in the whatsapp-bridge folder and scan the QR code from the phone's WhatsApp, as with WhatsApp Web. 5) Replace the paths in the config with the uv path and the working directory (`pwd`). The server name appears only once in the config. 6) Restart Claude, which can then read and send WhatsApp messages. The video does not show the exact commands on screen; they are in the linked repo. *When:* Running a personal WhatsApp-connected agent on your own machine where message data should stay local.
- **Adding the ElevenLabs MCP with one env var** — Add the ElevenLabs MCP block to the same MCP config, supplying the ElevenLabs API key as its single environment variable. Run it through uvx. A paid account exposes the key in account settings. Then ask the agent to send a message as a voice note. *When:* Adding speech output to an agent. Expect the default voice to sound robotic; use a voice clone for a realistic result.
- **Prompt the agent with an explicit contact name** — When a contact name is ambiguous (two contacts named Dad), name the one you mean in the prompt before asking the agent to read or reply to messages. *When:* Acting on a messaging or CRM-style tool where the tool may match several records.
- **Windows build fix for the WhatsApp bridge** — Enable CGO (one extra command) and install a C compiler on Windows before running the Go bridge. The speaker does not name the exact compiler or command. *When:* Running the WhatsApp MCP bridge on Windows.

## Numbers
- Three MCP servers are installed: Blender, WhatsApp and ElevenLabs. Two of them (WhatsApp and ElevenLabs) are set up in the video. ([1:20](https://youtu.be/BjqR3Ddb71k?t=80))
- The ElevenLabs MCP needs one environment variable, the API key. Paid accounts get the key from account settings. ([2:35](https://youtu.be/BjqR3Ddb71k?t=155))
- No benchmarks, latency figures, prices or adoption stats are given. ElevenLabs is described only as 'a bit expensive' with no figures. ([0:00](https://youtu.be/BjqR3Ddb71k?t=0))

## Hot takes
- The title ('running my business for me') overstates the demo, which is one personal reply to a contact named Dad.
- The claims that ElevenLabs gives the 'best' audio and TTS models and sounds 'nothing else sounds as real' are unsupported opinion.
- The 'fully local, no server' privacy claim covers only the WhatsApp MCP. The ElevenLabs step sends text to a cloud service, which the video does not mention.
- Quality is capped at 2: the hype title and thin substance outweigh the real setup outline, and exact commands and config keys are not shown.

## Tools mentioned
Claude Desktop, WhatsApp MCP server (Go bridge + MCP), ElevenLabs MCP, ElevenLabs voice cloning, uv / uvx, Go, Cursor, Windsurf, Blender MCP, Swift (planned app), MCP

## Relevance to our work
- **agentos** (1/3): AgentOS is an MCP-style, multi-tool agent platform. This video shows one personal messaging integration built from local MCP servers, a pattern that could be used as a reference for a channel tool. The video gives no architecture, security or audit detail. → *Low priority: if AgentOS needs a messaging-channel example for its tool layer, read the WhatsApp MCP repo's bridge code for how it handles local session and QR linking.*
