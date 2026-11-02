# Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `YZQsWVeN3rE` · [watch](https://youtu.be/YZQsWVeN3rE) · **date:** 2026-07-18 · **length:** 17:09 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Alex Bauer · **orgs:** Upside.tech, Exa, Slack
- **topics:** multi-agent, evals, context-engineering, rag-retrieval · **tags:** trust, go-to-market, jury-and-judge, librarian, commanders-intent, agent-tiers, multi-touch-attribution, scaffolding, anchor-assets, citations

> Alex Bauer (Upside.tech) on building trust in AI for go-to-market data: manage agents like people, scaffold business context first, use a librarian and a jury-and-judge pattern, and use only tier-two agent harnesses for important work.

## Summary
The speaker argues that the main problem with AI in go-to-market work is now trust, not hallucination: the model gives a confident wrong answer, such as a wrong revenue number. His main thesis is to manage agents the way you would manage capable people, and above all to give them the reason behind a task (commander's intent). He shows a failed "YOLO" attempt to rebuild a company website from raw sources, which worked only after he wrote down business knowledge as anchor assets and a product capability reference with citations. He describes an in-product "librarian" that agents consult before answering, which supplies company definitions (fiscal year, what counts as new pipeline) and schemas of past failed queries. For ambiguous questions such as multi-touch attribution, his product spins up several independent analysts who each produce an evidence-cited opinion, and a judge weighs their reasoning and escalates when consensus is weak. He ends with a warning that cheap, chat-wrapped AI products are not capable enough for important work, and that teams need agent harnesses with subagents, plan mode, full MCP support and file editing. Parts of the talk are a sales pitch for his company, and most claims come from his own experience rather than measured results.

## Key ideas
- **The current AI failure is a trust problem: the model gives a confidently wrong answer instead of saying it is unsure.** — He says the hallucination talk has been replaced by a trust problem. For example, asked to report revenue, the model gives a wrong number that looks right. ([7:13](https://youtu.be/YZQsWVeN3rE?t=433))
- **Manage agents like human team members, and tell them why.** — Use commander's intent: give the purpose of the task, not step-by-step micromanagement. Agents trained on human text tend to micromanage themselves, so you must pull them back to the why. He says the same is true for people. ([8:31](https://youtu.be/YZQsWVeN3rE?t=511))
- **Do not YOLO a complex deliverable. Scaffold business knowledge first.** — A one-shot website rebuild from raw sources failed even in plan mode. It worked after he maintained anchor assets: a product capability reference (with personas) that AI compiled and that cites the connected systems it came from. ([9:58](https://youtu.be/YZQsWVeN3rE?t=598))
- **Define the structure first, then let the model fill it in.** — The product capability cards laddered directly up to the homepage and product pages. The citations let him check for hallucinated key facts. He adds a general style skill and persona review agents to critique drafts. ([11:13](https://youtu.be/YZQsWVeN3rE?t=673))
- **A librarian gives agents just-in-time company knowledge before they answer.** — Before answering, the agent consults a store of company documentation, knowledge items, and the schema of prior failed queries. This prevents naive answers, such as treating Q1 as January to March when the fiscal year is February to April, or counting all pipeline when new pipeline means stage two or later. ([12:22](https://youtu.be/YZQsWVeN3rE?t=742))
- **For questions with no empirically correct answer, use a jury of independent analysts and a judge.** — Several analysts each research the same question independently and write evidence-cited opinions. A judge treats them as inputs, weighs the quality of their reasoning rather than counting votes, and expands the jury if consensus is weak. He compares this to human peer review. ([13:26](https://youtu.be/YZQsWVeN3rE?t=806))
- **Use only capable agent harnesses for important work.** — Chat wrappers built on cheap subscriptions do not leave enough margin for strong reasoning. He calls a tier-two setup the minimum, with subagents, plan mode, full MCP support and file editing. His example is Slackbot's new MCP client, which he found poor. ([15:57](https://youtu.be/YZQsWVeN3rE?t=957))

## Techniques
- **Commander's intent prompting** — State the goal and the reason for the task rather than the exact steps. Re-anchor the agent on the why when it starts micromanaging itself. *When:* Any delegated task where the agent has room to choose its approach.
- **Anchor assets and scaffolding** — Maintain a small set of canonical company documents (product capabilities, personas, and so on). Have the model compile them from connected systems, with citations back to sources, then generate deliverables from them. *When:* Before any large generated deliverable, such as website copy or product pages, where facts must be accurate.
- **Citation tracing for verification** — Require each claim in a generated reference to cite the systems it came from, so a reviewer can follow the trail to check key facts. *When:* When reviewing AI-compiled reference material before it is published.
- **Librarian pre-query lookup** — Before the agent answers a business question, have it consult a store of company definitions, documentation and a log of failed query patterns, then answer with citations. *When:* Business analytics questions where company-specific definitions (fiscal calendar, pipeline stages) change the answer.
- **Jury and judge** — Run several independent analysts on the same question, each producing an evidence-cited opinion. A judge agent weighs their reasoning quality, synthesizes a final answer, and expands the jury when consensus is weak. *When:* Questions with no single correct answer, such as multi-touch attribution credit.
- **Tiered tool selection** — Before trusting an agent product with important work, check for subagents, plan mode, full MCP support and file editing. Avoid flat-subscription chat wrappers for those tasks. *When:* Choosing which AI tools a team should use for consequential work.

## Numbers
- Estimated website rebuild at a 600-person prior company: several product marketers, a designer, consulting PMs and a web team over two months. This is his estimate of the old way, not an AI measurement. ([8:31](https://youtu.be/YZQsWVeN3rE?t=511))
- Multi-touch attribution took his company about two years to get close to working before the AI-native data layer and Opus-based approach. ([13:26](https://youtu.be/YZQsWVeN3rE?t=806))
- Example definitions: fiscal year runs February to April, and new pipeline counts only opportunities at stage two or later. ([12:22](https://youtu.be/YZQsWVeN3rE?t=742))

## Hot takes
- The hallucination problem has become a trust problem: confident wrong answers are worse than admitted uncertainty.
- Do not tell Claude to improve itself. You get micromanagement; give the why instead.
- You cannot fix stupid: friends do not let friends use weak harnesses or low-intelligence models for important work.
- Chat products built on pre-AI subscription pricing do not leave enough margin for strong reasoning, so they are unsafe for important work.
- Non-engineers with AI are like an infinite supply of valedictorian interns, which speeds iteration but needs guardrails.

## Tools mentioned
Claude, Claude Opus, Slackbot, ChatGPT

## Relevance to our work
- **prosharness** (2/3): ProsHarness runs plan, then critique, then debate. The jury-and-judge pattern (several independent critiques, a judge that weighs reasoning and escalates on low consensus) is a concrete option for that critique stage. The tier-two harness checklist also maps onto what ProsHarness needs from Claude Code. → *Prototype a critique stage where three independent Codex critiques of a plan go to a judge step that re-runs the critique when they disagree, and measure whether it catches more plan defects than a single critique.*
- **agentos** (1/3): MemoryMesh already has provenance and conflict resolution. The librarian idea (a business-definitions and failed-query store consulted before answering) overlaps with its retrieval, but the talk gives no measured results. → *Read the librarian pattern and consider whether MemoryMesh should store a schema of failed queries as retrieval context for agents.*
