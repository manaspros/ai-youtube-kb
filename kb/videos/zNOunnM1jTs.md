# 8 Vibe Coded Apps That Generated Millions Overnight

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `zNOunnM1jTs` · [watch](https://youtu.be/zNOunnM1jTs) · **date:** 2026-05-02 · **length:** 12:35 · **format:** other · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Scrimba, Cursor, Anthropic, OpenAI, xAI, Google, Midjourney, ElevenLabs, Supabase, Vercel, Figma, Mistral, LangChain, Hugging Face, Medvi, Cal AI, Wave, Flypeter, Trendfeed, Aura, Sleek, CiteShore, Jenny AI
- **topics:** vibe-coding-app-building, product-ux, coding-agents · **tags:** vibe-coding, indie-hackers, case-studies, cursor, claude, chatgpt, mrr, icp, websockets, webrtc, outsourcing, incremental-prompting, sponsored, listicle

> Anecdotal roundup of eight solo, vibe-coded apps with self-reported revenue; the useful part is a few habits (small prompts, outsourced dependencies, defining an ICP first), not the numbers.

## Summary
The video profiles eight apps reportedly built almost entirely with AI coding tools by founders who were non-developers or working solo: Medvi, Cal AI, Wave, Flypeter, Trendfeed, Aura, Sleek and CiteShore. For each, it gives the founder's reported revenue, user counts or MRR, and the tools used, mostly Cursor, Claude and ChatGPT. The recurring pattern is building in small increments with simple prompts, offloading commodity dependencies (pharmacy, consultancy, call support, infrastructure) to third-party services, and picking a clearly defined customer before building. Several stories also cover distribution, such as influencers, X or TikTok posts, and zero-spend launches. The figures come from founder statements and social posts and are not independently verified. Roughly a minute of the runtime is a sponsor read for Scrimba. The actionable content is thin, so treat this as a motivational case-study roundup rather than a how-to.

## Key ideas
- **Treat every non-core dependency as a service instead of a hire or a build. Medvi's founder outsourced pharmacy fulfilment and consultancy and focused his own time on product judgment.** — Medvi's workflow was to assemble existing services into one product, and the video credits this, not novel tooling, for scale. ([1:12](https://youtu.be/zNOunnM1jTs?t=72))
- **Solo operation has a single point of failure. Medvi's founder broke production while away, and the video says the company lost 200 customers in an hour, so he hired two engineers as a safety net rather than to scale.** — The incident is the only operational failure story in the video and is the most concrete lesson about running a vibe-coded product in production. ([1:12](https://youtu.be/zNOunnM1jTs?t=72))
- **Build the app in chunks, one prompt per part, rather than asking for the whole app at once. Wave's founder used ChatGPT this way.** — The same pattern recurs across Flypeter (one prompt, then iterate per feature) and Aura (incremental changes, prompts under three sentences). ([3:50](https://youtu.be/zNOunnM1jTs?t=230))
- **Multiplayer and real-time features were where the vibe-coded game broke down. WebRTC worked only for two players, and switching to WebSockets fixed it.** — Flypeter's founder reports that Cursor's founder reached out directly during the fix. The video gives this as the one technical detail about a real architecture change. ([6:30](https://youtu.be/zNOunnM1jTs?t=390))
- **Define the ideal customer profile (ICP) before building. Sleek's founder says a clear ICP let them shape the product around one audience, which the video presents as the difference between impressive apps and profitable ones.** — Sleek also repurposed earlier design tools the team had already built, and got its first customers through X with an early-access announcement. ([10:05](https://youtu.be/zNOunnM1jTs?t=605))
- **Use a fallback model chain. Aura's founder starts with Claude for coding and switches to Gemini or GPT only when Claude fails the task.** — He also says to supply minimal but correct context rather than the full documentation, and to keep prompts under three sentences. ([9:03](https://youtu.be/zNOunnM1jTs?t=543))
- **Vibe design, not just vibe coding. AI tends to produce generic UIs, so give it templates and component libraries to steer the look. Aura's founder says he moved his design work from Figma to Cursor.** — He recommends component libraries such as 21.dev as the source of guiding templates. ([9:03](https://youtu.be/zNOunnM1jTs?t=543))
- **Distribution does most of the work. Several products reached meaningful revenue with zero paid marketing, relying on influencers (Cal AI), TikTok, Instagram and YouTube (Trendfeed), or X algorithm-friendly early-access launches (Sleek).** — Cal AI's reported 90% accuracy and 4.8 rating are presented as secondary to influencer-driven spikes in users. ([2:34](https://youtu.be/zNOunnM1jTs?t=154))

## Techniques
- **Incremental, chunked prompting** — Split the app into small parts and ask the model to write one part per prompt, then merge. Keep each prompt under about three sentences. Iterate one feature or fix at a time, starting from one initial prompt and then adding features with new prompts. *When:* Building a new app end to end with a coding agent when a single large prompt produces unfocused output.
- **Minimal correct context** — Give the agent only the documentation and context the current task needs, rather than dumping all the docs into the prompt. *When:* Working with a coding agent on a narrow task, where extra context dilutes focus.
- **Model fallback chain** — Start the coding task with Claude models. If they fail the task, switch to a Gemini or GPT model and retry. *When:* A coding task stalls with one model and you want a second opinion without changing the whole toolchain.
- **Design first, then modular build** — Analyse the target UI first, research competitors (using AI to summarise them), define data schemas, lay out onboarding and the core framework, then break the app into modular components that the AI builds separately and merges. *When:* Starting a SaaS or content app from zero with an AI coding tool and wanting a consistent structure.
- **Template-guided UI generation** — Provide design templates and component-library references (for example 21.dev) instead of asking for a UI from scratch, so the output does not default to a generic look. *When:* Generating frontend UI with AI, where the default output looks basic.
- **Stack choice for AI tools** — Use mainstream web stacks the AI tools handle well. The video's examples are Next.js, React, shadcn/ui, Supabase and Vercel. *When:* Choosing a stack for a vibe-coded web app, to reduce the friction of AI-generated code.
- **Outsource commodity operations** — For any function that is not core product (fulfilment, consultancy, support calls), buy an existing service and integrate it, and keep the founder focused on product decisions. Medvi used voice AI (ElevenLabs) for call handling. *When:* Running a small team or solo business where operations would otherwise need building or hiring.
- **Real-time multiplayer transport** — If WebRTC works only for a small number of peers, move the real-time channel to WebSockets, which the video reports solved multiplayer for everyone in Flypeter. *When:* A browser game or collaborative app needs more than a couple of concurrent connections.
- **Define the ICP before the build** — Write down the target customer profile first, then choose features and launch channels that serve that person, as Sleek did. *When:* Deciding what to build and how to launch a product that needs to make revenue.

## Numbers
- Medvi: over 500,000 active users; $401M revenue in first year (founder-reported, as stated in the video); on track for a billion-dollar valuation ([0:00](https://youtu.be/zNOunnM1jTs?t=0))
- Medvi: a production outage lost 200 customers in one hour ([1:12](https://youtu.be/zNOunnM1jTs?t=72))
- Cal AI: over 5 million downloads in 8 months; over $2M revenue in one month; 30% retention; 4.8 rating on both app stores; about 90% accuracy ([2:34](https://youtu.be/zNOunnM1jTs?t=154))
- Wave: about $7M revenue ([3:50](https://youtu.be/zNOunnM1jTs?t=230))
- Flypeter: first version in 30 minutes; about 80% done after 3 hours of Cursor work; scaled to $500,000 per month; paid plane at $29 ([5:18](https://youtu.be/zNOunnM1jTs?t=318))
- Trendfeed: about $12,000 in four weeks; 5.5 thousand in revenue on launch day (the transcript says 'pounds', likely a caption error for dollars); zero marketing spend ([7:35](https://youtu.be/zNOunnM1jTs?t=455))
- Aura: $15,000 MRR and over 21.7k users in one month (founder's X post) ([9:03](https://youtu.be/zNOunnM1jTs?t=543))
- Sleek: $10,000 MRR in six weeks, with no marketing spend ([10:05](https://youtu.be/zNOunnM1jTs?t=605))
- CiteShore: about $10,000 MRR, then acquired by another AI platform (price not stated) ([11:32](https://youtu.be/zNOunnM1jTs?t=692))
- Aura's guidance: prompts under three sentences ([10:05](https://youtu.be/zNOunnM1jTs?t=605))

## Hot takes
- Every revenue and user figure is founder-reported or from social posts and is not verified. Medvi's $401M first-year claim and Flypeter's 'Elon Musk endorsed' claim carry no sources in the video.
- Sponsored segment for Scrimba at about 5:18 to 6:00. It is not product substance and it lowers the quality rating.
- Survivorship framing: the video picks eight successes and gives no failure rate, so 'vibe coding leads to millions' is not supported by this sample.
- Caption errors to be aware of: 'Trendfeed 5.5 thousand pounds' is probably dollars, and the acquirer 'Jenny AI' is an unverified caption spelling.
- The one concrete engineering detail is the WebRTC to WebSockets switch for multiplayer. The rest is business and marketing anecdote.
- The strongest transferable habit is the ICP-first advice. The claim that prompts should stay under three sentences is a single founder's rule of thumb, not evidence.

## Tools mentioned
Claude, Claude Code, Cursor, ChatGPT, Grok, Grok 3, Claude Sonnet 3.7, Gemini, GPT, Midjourney, ElevenLabs, Next.js, React, shadcn/ui, Supabase, Vercel, Figma, 21.dev, WebRTC, WebSockets, Scrimba, Mistral, LangChain, Hugging Face

## Relevance to our work
- **prosharness** (1/3): Anecdotal support for keeping per-step agent prompts short and chunked, and for minimal context per run. Weak evidence. → *When writing ProsHarness step prompts for Claude Code, check whether each step can be stated in under three sentences with only the context it needs. Use this as a hypothesis to test, not a validated rule.*
