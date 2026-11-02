# How I Built a ChatGPT Powered Voice Agent with MCP + LiveKit

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `jRk63S3v-UQ` · [watch](https://youtu.be/jRk63S3v-UQ) · **date:** 2025-11-02 · **length:** 9:31 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** Unnamed AI LABS host · **orgs:** LiveKit, OpenAI, Cartesia, ElevenLabs
- **topics:** voice-multimodal, mcp-and-tools · **tags:** voice-agent, livekit, mcp, whatsapp-mcp, tts, vad, cartesia, whisper, mcp-use, python, uv

> Tutorial on building a voice agent with a LiveKit + Cartesia + OpenAI base, then wiring a local WhatsApp MCP server into it so speech can trigger tool calls.

## Summary
The host sets up an open-source real-time voice agent (LiveKit transport, VAD for barge-in, GPT-4o mini as the LLM, Cartesia Sonic for TTS) and walks through the install: git clone, uv instead of pip, a .env with three API credential sets, then running the agent and connecting from a browser. The main code knobs are the LLM model, the system prompt (which also constrains output to TTS-friendly text), and the greeting. The main extension is MCP integration via the MCP-use library, which exposes every tool on a registered MCP server as a callable function the agent chooses from. The demo uses a locally running WhatsApp MCP server to read and send messages by voice, with about 2 to 3 seconds of end-to-end latency as described by the host. The host also suggests swapping in other MCP servers such as Airbnb or Brave Search by editing the MCP configuration. Known issues include interruption handling and a transcription error in an outgoing message. The video is a practitioner walkthrough built on someone else's open-source base, with little depth on architecture or evaluation.

## Key ideas
- **Start from an existing open-source voice agent and extend it rather than building from scratch** — The host credits another developer's open-source voice agent as the base and layers MCP server support on top. The base already handles the real-time audio loop. ([0:00](https://youtu.be/jRk63S3v-UQ?t=0))
- **Voice activity detection is what makes interruption feel natural** — A VAD component pauses the assistant when the user starts speaking, so the user can cut in mid-reply. The host compares this to real-time assistants from OpenAI. ([2:53](https://youtu.be/jRk63S3v-UQ?t=173))
- **The system prompt doubles as a TTS-safety filter** — The prompt sets a witty, short-answer persona and tells the model to avoid hard-to-pronounce words and emojis, because those break the text-to-speech engine. Persona and output format are both steered here. ([4:19](https://youtu.be/jRk63S3v-UQ?t=259))
- **Cartesia is chosen for TTS on cost and free-tier grounds** — The host uses Cartesia's Sonic preview model with a configurable voice ID. The host argues its free tier and pricing beat ElevenLabs, which he says restricts API use without a paid plan. These are the host's claims, not verified figures. ([4:19](https://youtu.be/jRk63S3v-UQ?t=259))
- **An MCP-use library turns any registered MCP server into callable tools for the voice agent** — The library takes the MCP server, passes in the transcribed utterance, and lets an agent pick the right tool automatically. The host says the number of tools registered does not matter because each one becomes a callable function. ([5:26](https://youtu.be/jRk63S3v-UQ?t=326))
- **The demo routes speech through a local WhatsApp MCP server before the LLM responds** — The host describes the flow as: speech is transcribed, the transcript goes to the WhatsApp MCP server, the server returns a result, and the agent speaks it. The host reports about 2 to 3 seconds of processing before the spoken reply. ([6:47](https://youtu.be/jRk63S3v-UQ?t=407))
- **Swapping data sources is a config change, not a code change** — Other MCP servers such as an Airbnb listings server or Brave Search can be added by editing the MCP configuration. The host says any MCP can be dropped into the setup. ([8:15](https://youtu.be/jRk63S3v-UQ?t=495))
- **Known weak spots remain: interruption handling and transcription accuracy** — The host says interruption handling still has bugs he is working on. He also points to a Whisper transcription error in a sent message as a minor glitch he did not fix. ([8:15](https://youtu.be/jRk63S3v-UQ?t=495))

## Techniques
- **Clone, install with uv, and run the voice agent locally** — git clone the repo, open the folder, create a Python environment in the editor, then install dependencies with uv rather than pip. The exact uv command is not spoken in the transcript. Create a .env file in the project directory with the OpenAI key, the Cartesia API key, and the LiveKit server URL, API key and API secret. Start the agent from the terminal, open the link it prints in a browser, and connect to the LiveKit project. *When:* Use as the baseline setup before any customization. LiveKit requires a project created in its dashboard, and the same project must be the one whose credentials were put in .env.
- **Change the LLM and the system prompt in the main agent file** — The main file holds the model name (GPT-4o mini in the demo) and the system prompt. Swap the model for a stronger one if longer answers are needed. Keep the prompt short and speech-friendly: a persona plus rules to avoid hard-to-pronounce words and emojis. Add a character description to the prompt if a named character is not recognized. The greeting message is also a string in the file. *When:* Use when tuning persona or answer length for voice output, where text that reads well on screen can fail in TTS.
- **Wire an MCP server into the voice agent through the MCP-use library** — Run the MCP server locally, such as the WhatsApp MCP server. Register it in the MCP configuration file that the MCP-use library reads. The library passes the transcribed utterance to an agent that selects the matching tool and returns the result for speech output. Other MCP servers are added the same way by editing the configuration. *When:* Use when a voice front end needs to call external tools or private data, and the tool choice should be made by the model rather than hard-coded.

## Numbers
- Cartesia free tier gives 20,000 credits; the host says about 25 minutes of audio was possible with the credits he had left, at 15 credits per second of audio. ([4:19](https://youtu.be/jRk63S3v-UQ?t=259))
- End-to-end latency for the WhatsApp MCP flow: about 2 to 3 seconds of processing before the spoken reply (the host's own description). ([6:47](https://youtu.be/jRk63S3v-UQ?t=407))

## Hot takes
- Cartesia is cheaper and more flexible than ElevenLabs. This is the host's comparison, and no pricing was shown on screen.
- The base project is someone else's open-source work; the host adds the MCP layer on top and says the interruption handling is still buggy.
- The demo sends a real WhatsApp message to a family member from a live account. The host skipped showing the chat for privacy, but the transcription error in the sent message was visible.

## Tools mentioned
LiveKit (voice agent transport and dashboard), OpenAI GPT-4o mini (LLM; transcribed as GPT-40 mini), OpenAI Whisper (speech-to-text), Cartesia Sonic preview (TTS), MCP-use library (MCP tool-use agent), WhatsApp MCP server (local), Brave Search MCP, Airbnb MCP (mentioned as a possible example), uv (Python package manager), Cursor (editor), git

## Relevance to our work
- **agentos** (1/3): AgentOS is an OpenAI-compatible proxy, and this shows a voice front end calling MCP tools through an agent loop. Voice is not on the AgentOS roadmap, so the fit is weak. → *Low priority: if AgentOS ever adds a voice channel, reuse the MCP-server-as-tool-source pattern and check how the MCP-use agent loop selects tools.*
