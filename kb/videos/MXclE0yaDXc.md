# 7 Ways you can Avoid Claude Session Limit

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `MXclE0yaDXc` · [watch](https://youtu.be/MXclE0yaDXc) · **date:** 2026-09-02 · **length:** 9:01 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** Kai (Kai Explains channel host) · **orgs:** Anthropic
- **topics:** token-cost-efficiency, context-engineering · **tags:** claude-chat, cowork, usage-limits, token-cost, prompt-economy, attachments, output-compression, rolling-window, peak-hours

> Kai's seven tips for stretching Claude chat and Cowork usage limits: trim attachments, plan in chat before building, write short prompts, edit instead of correcting, batch asks, shorten output, and spread sessions across the rolling window.

## Summary
The host argues that Claude's usage cost is driven mostly by re-reading the whole conversation on every turn, citing a developer who measured 98.5% of tokens going to history and 1.5% to the new response. He then gives seven habits to cut that cost: convert PDFs to plain markdown and crop screenshots before attaching them, do the planning in regular chat before building files in Cowork, keep prompts short and answer clarifying multiple-choice questions, edit an earlier message instead of stacking corrections, combine several asks into one message, and ask for terse output (he points to an open-source tool called Caveman). The last tip is to split work across the rolling five-hour window and avoid weekday peak hours. The numbers are mostly the speaker's own illustrations or quoted claims without shown methods, and the advice is generic beginner-level usage hygiene rather than Claude Code or API-level engineering.

## Key ideas
- **Input re-reading dominates cost** — Each new message makes Claude re-read the full conversation history, so the cost of later turns grows with the thread. A developer the host cites measured 98.5% of tokens going to re-reading history and 1.5% to the response. The host also claims a 30th message can cost about 46 times a first message, but he does not show the method. ([0:00](https://youtu.be/MXclE0yaDXc?t=0))
- **Attachments are token-heavy** — A PDF page is estimated at 1,500-3,000 tokens and a full screenshot at about 1,300, plus hidden metadata. Re-uploading the same 15-page PDF to four chats is said to cost over 180,000 tokens, versus about 2,000 as plain text. ([1:20](https://youtu.be/MXclE0yaDXc?t=80))
- **Convert documents to plain text and crop screenshots** — Paste PDF text into a markdown file and upload that instead (his example drops about 3,000 tokens to about 200). Crop screenshots to the relevant region (about 1,300 tokens down to under 100). ([1:20](https://youtu.be/MXclE0yaDXc?t=80))
- **Plan in chat, build in Cowork** — File-generation work (spreadsheets, Word docs, presentations) costs more than chat messages, which the host attributes to Anthropic's usage-limit docs. Agree on structure and assumptions in regular chat first, then hand the finished plan to Cowork as a single build instruction. ([2:39](https://youtu.be/MXclE0yaDXc?t=159))
- **Short prompts with clarifying questions** — Long prompts are re-billed on every later turn. Use a short structure ('I want to X to achieve Y. Ask me questions before you start.') and answer the multiple-choice questions Claude surfaces, since clicking is cheap and typed correction chains are expensive. ([3:54](https://youtu.be/MXclE0yaDXc?t=234))
- **Edit the earlier message instead of correcting it** — Corrections pile up in history and are re-read on every later turn. Editing the original prompt and regenerating replaces the bad exchange, which the host says also gives better results. ([3:54](https://youtu.be/MXclE0yaDXc?t=234))
- **Batch asks into one message** — Three separate messages mean three full history reloads. Combining the asks into one message costs one reload and gives Claude the full picture at once. ([5:16](https://youtu.be/MXclE0yaDXc?t=316))
- **Output tokens count too, so ask for terse output** — Output tokens count against the limit, and default replies are verbose. He recommends the open-source Caveman tool, which makes Claude answer in compressed prose while keeping code blocks and technical details exact. ([6:34](https://youtu.be/MXclE0yaDXc?t=394))
- **Limits use a rolling five-hour window** — Usage from more than five hours ago drops out of the window, so splitting work into morning, afternoon and evening sessions frees capacity earlier than a single long session would. ([6:34](https://youtu.be/MXclE0yaDXc?t=394))
- **Peak-hour usage drains limits faster** — He says weekday usage roughly 8 a.m. to 2 p.m. Eastern costs more per task than the same work in the evening or on weekends. He says Anthropic added this recently, but he gives no source beyond that. ([7:58](https://youtu.be/MXclE0yaDXc?t=478))

## Techniques
- **Convert attachments to plain markdown before upload** — Open a blank doc (he uses doc.new in the browser), paste the document text, download it as markdown, and upload that file instead of the PDF. *When:* Reusing a long PDF or document across several chats, or any time a plain-text version of the content exists.
- **Tight-crop screenshots** — Crop the screenshot to only the region that matters before attaching it. *When:* Sharing a screenshot where only one part is relevant to the question.
- **Plan in chat, then build in Cowork** — Do the structure, sections and assumptions in regular chat first, then send the locked plan to Cowork as one instruction such as 'build this exact thing'. *When:* Producing spreadsheets, documents or presentations whose requirements are still vague.
- **Short structured prompt with clarifying questions** — Use the template 'I want to X to achieve Y. Ask me questions before you start.' and answer the clickable multiple-choice options rather than writing long instructions. *When:* Starting a task where you are unsure what details the model needs.
- **Edit-and-regenerate instead of follow-up corrections** — Hover over an earlier user message in Claude Chat, click edit, fix the original prompt, save, and let Claude regenerate from that point. *When:* The model misread the first request; stacking correction messages inflates history.
- **Single batched message** — Combine related asks into one message (e.g. 'summarize this article, list the main points, and suggest a headline'). *When:* Several small requests about the same input would otherwise be sent one after another.
- **Terse-output mode via Caveman** — Install the open-source Caveman tool (linked in the video description, not shown in the transcript) so Claude replies in compressed style with articles and filler dropped; code blocks and technical details stay exact. *When:* Output is mostly prose you skim, and you want to cut output tokens (he claims about 65% on average).
- **Split sessions across the five-hour window** — Run separate morning, afternoon and evening sessions instead of one long session so earlier usage rolls off the window sooner. Move heavy work to evenings or weekends, outside weekday peak hours (about 8 a.m. to 2 p.m. Eastern, per the host). *When:* Working against a plan limit and hitting the cap during the day.

## Numbers
- Share of tokens going to re-reading history vs generating the response: 98.5% vs 1.5%, from a developer's measurement the host cites ([0:00](https://youtu.be/MXclE0yaDXc?t=0))
- A 30th message reportedly costs about 46 times a first message (host's claim, method not shown) ([0:00](https://youtu.be/MXclE0yaDXc?t=0))
- Rough conversion: 1 token is about 4 characters or 0.75 words ([0:00](https://youtu.be/MXclE0yaDXc?t=0))
- One PDF page costs roughly 1,500-3,000 tokens; a full-size screenshot about 1,300 tokens ([1:20](https://youtu.be/MXclE0yaDXc?t=80))
- A 15-page PDF uploaded to four chats is said to cost over 180,000 tokens, vs about 2,000 as text ([1:20](https://youtu.be/MXclE0yaDXc?t=80))
- Converting a PDF page to markdown drops it from about 3,000 to about 200 tokens (host's example) ([1:20](https://youtu.be/MXclE0yaDXc?t=80))
- A tight screenshot crop drops from about 1,300 tokens to under 100 ([1:20](https://youtu.be/MXclE0yaDXc?t=80))
- Each 500-word prompt costs about 500 tokens on every later turn (illustrative) ([3:54](https://youtu.be/MXclE0yaDXc?t=234))
- Caveman cuts output tokens by about 65% on average (host's claim, sourced from the tool's own measurement) ([6:34](https://youtu.be/MXclE0yaDXc?t=394))
- Peak hours are roughly 8 a.m. to 2 p.m. Eastern on weekdays ([7:58](https://youtu.be/MXclE0yaDXc?t=478))

## Hot takes
- Most tips are generic usage hygiene (shorter prompts, fewer messages, fewer attachments) and not specific to Claude Code or the API.
- The headline numbers (46x per message, 98.5% re-read, 65% output cut) are presented without a shown method, and the video mixes up 'five' and 'seven' tips.
- The rolling five-hour window and peak-hour weighting are described as plan-limit behavior from the host's experience. They are not verified in the video, and the host does not cite the Anthropic docs he mentions for the file-cost point beyond that single reference.

## Tools mentioned
Claude (Anthropic chat), Claude Cowork, Google Docs (via doc.new), Caveman (open-source output-compression tool, named by the host)

## Relevance to our work
- **agentos** (1/3): Per-turn history re-reading as the main cost driver is a useful framing for the token economics of AgentOS's gateway and budget pillars, but the video is about consumer chat limits, not an API or proxy. → *Measure the input-history vs output-token split on our own gateway traces for a few multi-turn sessions to check whether a re-read share like 98.5% holds for agent traffic.*
- **prosharness** (1/3): ProsHarness's plan -> critique -> debate flow maps onto the plan-in-cheap-chat, build-in-expensive-tool split, though the video does not discuss Claude Code or the CLI. → *Consider running the planning and clarifying-question stage on a cheaper model and passing only the finished plan to the expensive build step, as the video suggests for chat vs Cowork.*
