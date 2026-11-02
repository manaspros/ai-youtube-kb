# Why Your LLM Answers Are Mediocre (And How to Fix It)

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `Ym-iMJ-sds0` · [watch](https://youtu.be/Ym-iMJ-sds0) · **date:** 2025-11-02 · **length:** 14:46 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed narrator (AI LABS channel host) · **orgs:** OpenAI, Anthropic, Google
- **topics:** context-engineering, memory, product-ux · **tags:** prompting, context-window, system-prompt, chatgpt-projects, custom-instructions, chat-memory, deep-research, canvas, image-generation, reasoning-models

> Beginner tips for getting better LLM answers in ChatGPT (prompting, context windows, memory, Projects, deep research, Canvas), with a brief tour of Codex, Gemini CLI and Claude Code.

## Summary
A 14-minute beginner guide to using ChatGPT well, presented as general advice for LLMs. It covers choosing a model by task (Claude for coding, ChatGPT for ideation, Gemini for research and long documents), writing specific prompts and iterating on them, and using reasoning or "thinking" modes for hard problems. It explains that the context window fills up and makes older instructions drop out, so the speaker advises starting a new chat for each idea. It then covers chat memory, user memory and custom instructions, and recommends Projects with a role-based system prompt and a sample output for repeated tasks. The last section covers web search versus deep research, Canvas for editing parts of a document, image generation, and a one-line mention each of Codex, Gemini CLI and Claude Code. The speaker says most viewers already know the first part.

## Key ideas
- **Pick the model by task: Claude is cited for coding, ChatGPT for creative ideation and ecosystem breadth, Gemini for research, Google-product access and long documents.** — The speaker frames these as stated strengths with no benchmarks or sources. The claims are general and not tested in the video. ([0:56](https://youtu.be/Ym-iMJ-sds0?t=56))
- **Be specific and iterate. Vague wording such as 'not too long' is weak, and a follow-up prompt that narrows the output is the normal way to improve a response.** — Mentioning the desired output style in the prompt is recommended. The speaker calls the repeated refinement loop iterative feedback. ([2:05](https://youtu.be/Ym-iMJ-sds0?t=125))
- **Reasoning or thinking models break problems into sub-steps and take longer. Newer models such as GPT-5 may switch to extended reasoning on their own, and users can turn thinking mode on manually.** — The speaker describes ChatGPT's thinking mode as cancellable mid-response, after which it falls back to the standard model. ([3:04](https://youtu.be/Ym-iMJ-sds0?t=184))
- **The context window is limited and measured in tokens. As it fills, earlier instructions fall out of attention, which is why brainstorms start to repeat.** — Every turn resends the whole conversation, so the advice is to start a fresh chat for each new idea. ([3:54](https://youtu.be/Ym-iMJ-sds0?t=234))
- **Chat memory and user memory are separate. Chat memory recalls earlier conversations, and user memory stores facts the model keeps across all chats, viewable under personalization settings.** — Custom instructions, a nickname, an occupation and a chosen personality also shape responses. The speaker gives a lactose-intolerance example. ([6:08](https://youtu.be/Ym-iMJ-sds0?t=368))
- **For repeated work, put the instructions in a Project's system prompt. Assign a specific role, write the prompt in Markdown, and include a sample output to fix the format.** — The speaker's examples are a trip-planning project for a one-off data-heavy task, and a fact-check and grammar-check project for essays used repeatedly. ([8:43](https://youtu.be/Ym-iMJ-sds0?t=523))
- **Web search only scratches the surface. Deep research digs further, may ask clarifying questions, and takes longer to produce a fuller report.** — The speaker presents this as the fallback when normal search does not return what is needed. ([10:54](https://youtu.be/Ym-iMJ-sds0?t=654))
- **Canvas lets the user edit one part of a document and restore earlier versions, instead of regenerating the whole thing. It can also be shared for collaboration.** — The speaker also suggests it for quick UI prototyping, where code can be run in the canvas. ([12:01](https://youtu.be/Ym-iMJ-sds0?t=721))
- **Brief tool roundup: ChatGPT's image generation (described as integrated from version 4.0), Codex as a terminal coding agent, Gemini CLI, and Claude Code as Anthropic's terminal interface.** — Each tool gets one line with no demo, no comparison and no version details beyond the 4.0 mention. ([13:18](https://youtu.be/Ym-iMJ-sds0?t=798))

## Techniques
- **Specific, iterated prompting** — Replace vague length or tone words with concrete instructions. Mention the desired output style. Send follow-up prompts that narrow the result until it matches. *When:* Any one-off request to a chat model where the first answer misses.
- **Fresh chat per idea** — Start a new conversation for each new topic or brainstorm, so earlier turns do not crowd out the instructions that matter. *When:* Long brainstorms where ideas start repeating, or when switching topics in a chat.
- **Project system prompt with role and sample output** — Create a Project. Write the system prompt in Markdown with sections. Give the model a specific role, which the speaker says narrows the training data it draws on. Add one sample output to fix structure and style. Attach reference files there. *When:* Recurring tasks where the same instructions get retyped, or a one-off data-heavy task such as trip planning.
- **Escalate from web search to deep research** — Use normal web search first. If results are shallow, switch to deep research, answer its clarifying questions, and wait for the longer report. *When:* Comprehensive research where a standard search misses key details.
- **Canvas for partial edits** — Open Canvas, select or ask for changes to one section, review the diff, and restore an earlier version if an edit is wrong. *When:* Editing long writing or code without losing the good parts of the draft.

## Hot takes
- Quality is capped at 2 because the content is beginner-level and ChatGPT-centric. The speaker says most viewers already know the first section.
- The model-strength claims (Claude for coding, Gemini for research and long context) are stated with no evidence.
- Auto-captions misspell Claude Code as 'CloudCode'. The speaker also calls image generation integrated from version 4.0 without naming the model.
- The one Claude Code mention is a single sentence describing it as a terminal interface. There is nothing about CLAUDE.md, skills or subagents.

## Tools mentioned
ChatGPT, GPT-5, Claude, Gemini, Gemini CLI, Codex, Claude Code, Nano Banana, ChatGPT Canvas, ChatGPT Deep Research, ChatGPT Projects, ChatGPT Voice Mode, ChatGPT Dictate Mode

## Relevance to our work
- **agentos** (1/3): Only the context-window and fresh-chat advice touches context engineering. The video has no infrastructure, gateway, proxy or eval content relevant to AgentOS. → *No change to AgentOS. Use kb/guides for context-engineering sources instead of this video.*
- **prosharness** (1/3): The talk's point that long sessions lose early instructions is the same failure ProsHarness checkpoint/resume is meant to handle. The talk only covers chat UIs and offers no mechanism. → *Nothing to build. Cite it only if ProsHarness docs need a plain-language reason for starting fresh sessions.*
