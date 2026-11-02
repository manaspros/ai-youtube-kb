# How to talk to statues — Joe Reeve, ElevenLabs

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `u-rJwPPU3QA` · [watch](https://youtu.be/u-rJwPPU3QA) · **date:** 2026-06-18 · **length:** 33:28 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Joe Reeve · **orgs:** ElevenLabs, British Museum, Science Museum, Facebook, OpenAI, Bonhams, Christie's
- **topics:** voice-multimodal, product-ux, vibe-coding-app-building · **tags:** voice agents, barge-in, vibe coding, viral growth, ElevenLabs, voice design, museums, transcript editing, generative UI, short-form video

> ElevenLabs growth lead on the viral "Statue" app, built in two hours, and on voice-agent UX. Main points: glue code and storytelling matter most, and voice agents need visual co-presence and interruptible, editable transcripts.

## Summary
Joe Reeve, who works on growth at ElevenLabs, describes the Statue app: a user photographs a statue, OpenAI deep research identifies it and drafts its history, the ElevenLabs voice design API generates a matching voice, an ElevenLabs agent is created, and a phone call starts in about 30 seconds. He built it in roughly two hours with Cursor, shared the prompt and a short demo video, and the spread brought in museums and auction houses. He argues the valuable work is not the glue between managed APIs but the curation of real narratives with museum curators, and that museum databases are the right data source. The second half is speculative design discussion: voice interfaces are too polite to interrupt, spoken answers need skimming controls rather than concision, and barge-in can be handled by editing the stored transcript to what was actually played. He also describes a social-game growth pattern (a cheap clone on the deprecated Facebook Instant Games API) and gives practical short-video tips. Much of the talk is conversational, and several ideas are untested by his own admission.

## Key ideas
- **The glue is the product.** — Almost everything in the Statue app is stitched from existing scalable APIs. User management is commodity; the hard parts (maintaining agents and voice design) are handled by third-party APIs. The speaker says telling a good story about the glue matters more than solving hard technical problems. ([5:25](https://youtu.be/u-rJwPPU3QA?t=325))
- **Fast prototype, then the story spreads it.** — A two-hour Cursor build, a shared prompt, and a short demo video reached about 50k impressions on day one and roughly 1.5M on day two. Reposting with a 'vibe coded in two hours' framing drove the second wave. The reach then brought inbound interest from museums, auction houses and other businesses. ([2:37](https://youtu.be/u-rJwPPU3QA?t=157))
- **Photo-to-research is not the long-term museum product.** — Taking a photo and getting research back is a demo. The durable work is having curators shape the actual narrative, and museums often already expose their collections as databases or APIs that can be pulled from. Right now the museums could only edit the system prompt and knowledge files in the ElevenLabs dashboard. ([6:51](https://youtu.be/u-rJwPPU3QA?t=411))
- **Voice needs a visual channel alongside it.** — Voice is a binary mode today. He wants parallel input and output, where speech is the single input and the output is generated UI, diagrams or text that can be read at once. He also suggests a planner-style voice agent in front of a coding agent, so the user talks to the agent that decides, not the one that executes. ([10:21](https://youtu.be/u-rJwPPU3QA?t=621))
- **Users are too polite to interrupt voice agents.** — He says aggressive interruption makes the experience better, but the hard part is giving users permission to interrupt. Concise spoken answers can also sound rude, unlike concise text. ([21:33](https://youtu.be/u-rJwPPU3QA?t=1293))
- **Skim navigation for audio.** — People skim text by concept, not sentence. He proposes audio controls that move forward or back by idea, like scrubbing an iPod wheel. The Claude app's section-level voice view is a partial version of this. ([21:33](https://youtu.be/u-rJwPPU3QA?t=1293))
- **Barge-in by editing the transcript, not regenerating.** — Most platforms generate the full text, then TTS, and append the user's interruption to the end. Because the platform knows how far audio has played, it could rewrite the stored assistant turn to what was actually heard. He says this is untested and was not built by anyone he knows of. ([28:03](https://youtu.be/u-rJwPPU3QA?t=1683))
- **Cheap social-game clone as a growth template.** — A £15 Fruit Ninja-style clone wired to the Facebook Instant Games primitives (user info, friends, leaderboard, key-value storage, rewarded and interstitial ads) reached about 15M users overnight in one market, mostly Vietnam. He thinks this social-graph-plus-ads template is the likeliest winner for social vibe-coded apps. This is one anecdote. ([17:19](https://youtu.be/u-rJwPPU3QA?t=1039))

## Techniques
- **Research-to-persona-to-agent chain** — Image in, then an LLM deep-research call for identity and history, then a generated persona or voice description, then a voice design API, then create an agent with that prompt and knowledge, then start an outbound call. Each step uses a managed API. *When:* Any 'talk to X' product where the persona should come from research about the subject, and speed (about 30 seconds end to end) matters.
- **Thin glue layer on managed APIs** — Use managed services for auth, voice, agents and data. Build only the orchestration layer in an AI IDE such as Cursor. The speaker says the prototype was built in about two hours, and he would still need to check the generated code and harden it for production. *When:* Rapid prototyping or a demo. Do not rebuild infrastructure that a third-party API covers.
- **Playback-position transcript truncation for barge-in** — Track the audio position already played. When the user interrupts, rewrite the stored assistant message to end at the played position, and drop the rest of the generated text, rather than appending the user's words to the full message. This is a proposal from the speaker, not a shipped feature. *When:* Voice agents that stream TTS from full-text generation and need accurate conversation history after interruptions.
- **Visual side panel for voice conversations** — Show the structured items the agent is extracting or thinking about in a UI next to the voice stream, so the user can tap or act on them while still talking. *When:* Voice assistants that produce structured knowledge or plans the user will need to review or edit.
- **Hook-first short video with late music** — Put the most interesting moment in the first seconds, since median view time was 6 to 12 seconds. Add captions. Pick music either before writing the narrative (to set the vibe) or after (to fit the sections of the speech). Edit on a phone for quick cuts. *When:* Short-form demo or marketing video for a developer or AI product.

## Numbers
- Photo to phone call with the statue agent takes about 30 seconds. ([2:37](https://youtu.be/u-rJwPPU3QA?t=157))
- Statue app built in about 2 hours on a Sunday, from one prompt in Cursor. ([2:37](https://youtu.be/u-rJwPPU3QA?t=157))
- About 50,000 impressions on the first day of posting, rising to about 1.5 million on the second day after the repost. ([4:03](https://youtu.be/u-rJwPPU3QA?t=243))
- A £15 Fruit Ninja-style clone on Facebook Instant Games reached about 15 million users overnight, mostly in Vietnam (anecdote, earnings were small). ([18:41](https://youtu.be/u-rJwPPU3QA?t=1121))
- Median view time for his videos is 6 to 12 seconds, so the hook has to come early. ([30:00](https://youtu.be/u-rJwPPU3QA?t=1800))
- Editing the statue video on a phone took about 20 to 25 minutes. ([30:00](https://youtu.be/u-rJwPPU3QA?t=1800))
- He used a borrowed Bluetooth lapel mic that cost about £200. ([31:26](https://youtu.be/u-rJwPPU3QA?t=1886))

## Hot takes
- The glue code and the story around it matter more than the hard technical problems.
- Voice interfaces are too polite; users should interrupt agents much more aggressively.
- Concise answers feel rude in speech but fine in text.
- Consumer vibe coding has not gone mainstream yet; the winning pattern may look like a social game template.
- Barge-in should be handled by editing the stored transcript, not by regenerating the answer.

## Tools mentioned
ElevenLabs Agents, ElevenLabs Voice Design API, ElevenLabs music generation, OpenAI deep research, Cursor, Supabase, Facebook Instant Games API (deprecated), CapCut, Claude app voice UI, OpenClaw

## Relevance to our work
- **agentos** (1/3): The idea of storing only the text that was actually delivered when a stream is cut off applies to any streaming proxy with a memory or audit tier, but this talk does not address the proxy, budgets or audit. → *When a client aborts a streamed response, store only the bytes actually delivered as the assistant turn in MemoryMesh, instead of the full generated text. Check this against the conflict-resolution and provenance rules before adopting it.*
- **prosharness** (1/3): The speaker wants a front agent that turns a user's rough intent into direction for a coding agent, which is loosely like ProsHarness's plan step, but he only describes this as a wish. → *Compare the ProsHarness plan step against a front-agent pattern where a planner agent rewrites the user's short request into a spec before handing off to the Claude Code run. Judge it by whether the rewritten spec reduces rework.*
- **general** (1/3): Treating the stored conversation as editable state is a useful context-engineering idea across any agent that gets cut off mid-output. → *Audit the stored conversation state of any agent that can be interrupted, and check whether the saved assistant turn matches what the user actually saw or heard.*
