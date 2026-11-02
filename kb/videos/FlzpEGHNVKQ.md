# Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `FlzpEGHNVKQ` · [watch](https://youtu.be/FlzpEGHNVKQ) · **date:** 2026-05-18 · **length:** 18:22 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Anant Dole, Asbjorn Steinskog · **orgs:** Take Take Take
- **topics:** evals, context-engineering, mcp-and-tools · **tags:** chess, LLM-as-judge, grounded generation, latency budget, Claude Code Channels, human-in-the-loop, consumer AI, OpenRouter, Stockfish

> How a consumer chess app grounds LLM game commentary in Stockfish and detectors, hits a sub-3s latency target, and closes a feedback loop where a Claude Code agent triages bad comments and opens PRs.

## Summary
The speakers from Take Take Take, a chess app, explain how their AI chess coach works in production. LLMs play chess badly because they are trained on language, so the team does not let the LLM analyse positions. Each finished game runs through Stockfish, a set of tactical and positional detectors, and a human-move model (Maia). The LLM only turns these grounded facts into English commentary. The pipeline must return in about 3 seconds, so they use Gemini 3 Flash and avoid long reasoning on the user path. Evaluation uses 16 scenarios mined from real games, scored by an LLM judge and checked by chess-expert humans, with OpenRouter used to swap models quickly. For the feedback loop, a user's "bad commentary" report goes to Slack and into a running Claude Code session through the Channels feature. A triage skill then changes prompts or detectors, regenerates the commentary, self-verifies, asks the team questions on Slack, and opens a PR that is merged from a phone. The talk closes with a few learnings on separating data from generation and on pruning a large context JSON step by step.

## Key ideas
- **Keep the LLM away from analysis; let deterministic engines do the thinking** — Stockfish gives the best move, detectors flag forks, pins and structure, and a human-move model estimates how hard the move is to find. All of this is passed to the LLM, whose only job is to translate it into English, because letting it reason on its own hallucinates. ([7:48](https://youtu.be/FlzpEGHNVKQ?t=468))
- **LLMs are weak at chess because they are trained on language** — Reasoning models can play out a few moves but fall apart quickly. A transformer trained to predict evaluations from millions of positions can reach grandmaster strength, but such a model cannot explain its moves in language. The gap is bridged by pairing the two. ([5:14](https://youtu.be/FlzpEGHNVKQ?t=314))
- **Close the loop from user feedback to a coding agent that opens a PR** — A bad-comment report posts to Slack and is injected into a running Claude Code session via Channels. The agent runs a triage skill, changes detectors or prompts, regenerates the commentary, verifies its own output, asks the team on Slack, and opens a PR that a human merges from a phone. ([10:23](https://youtu.be/FlzpEGHNVKQ?t=623))
- **Set a hard latency budget and choose the model to fit it** — The coach must respond in under about 3 seconds because users cycle through moves. Gemini 3 Flash was chosen for its roughly 1 second time to first token and about 3 seconds average. Slower reasoning models were rejected because their completion time is unpredictable. Longer, chat-style coaching is planned for later. ([12:38](https://youtu.be/FlzpEGHNVKQ?t=758))
- **Evaluate with mined scenarios, an LLM judge and expert humans** — They built 16 scenarios from real games covering tactics, blunders and hallucination traps. An LLM judges the outputs, and the two chess-strong authors make the final call. OpenRouter lets them swap models as new releases arrive. ([13:52](https://youtu.be/FlzpEGHNVKQ?t=832))
- **Model choice is a trade-off between accuracy and latency, not a single winner** — Gemini Flash passes about 75% of scenarios and still fails some. Claude with more thinking gets just under 60% but is much slower. GPT-5 Mini is faster but less accurate. The team re-runs the scenarios whenever a new model appears. ([15:02](https://youtu.be/FlzpEGHNVKQ?t=902))
- **Build the context extraction as one large JSON and prune it step by step** — The early process is slow. You start with a big JSON context and remove pieces one at a time while watching quality. Automated evals help, and domain experts who may not be the builders should check the output. ([16:11](https://youtu.be/FlzpEGHNVKQ?t=971))

## Techniques
- **Deterministic analysis then LLM narration** — Run a classical engine (Stockfish), rule-based detectors and a human-likelihood model first. Pass the structured facts to the LLM and restrict it to verbalising them, so every claim in the text is grounded. *When:* Any domain where explanations must be factual and the latency budget is tight, for example commentary or review text generated from computed results.
- **Scenario-based LLM-as-judge regression set** — Extract real cases from production data, group them into themed scenarios (tactics, blunders, hallucination traps), score outputs with an LLM judge, and have domain experts spot-check. Run each candidate model through the same set via a router such as OpenRouter. *When:* Gating model swaps or prompt changes when new models ship often and quality is hard to measure automatically.
- **Channel-injected events into a running coding agent** — Use Claude Code's Channels feature (a research-preview MCP server) to push external events such as user feedback into an already running session. Pair it with a triage skill that holds the investigation procedure and scripts, and have the agent ask clarifying questions back in Slack. *When:* Human-in-the-loop autonomous fixes where a person reports a problem from a phone and approves the resulting PR later.
- **Latency-first model selection for interactive output** — Set a time budget (about 3 seconds here), measure time to first token and total time separately, and pick a fast model that fits. Move slow reasoning to an asynchronous chat-style feature where users expect to wait. *When:* Consumer or interactive surfaces where users click through results and cannot wait on long reasoning.
- **Iterative context pruning** — Begin with a large structured context file and remove items one by one, re-running evals after each removal to see whether quality rises or falls. *When:* Early in building an LLM feature when you do not yet know which context is necessary.

## Numbers
- Target latency for coach feedback is under about 3 seconds ([12:38](https://youtu.be/FlzpEGHNVKQ?t=758))
- Gemini 3 Flash has about 1 second time to first token and about 3 seconds average latency ([12:38](https://youtu.be/FlzpEGHNVKQ?t=758))
- 16 chess evaluation scenarios ([13:52](https://youtu.be/FlzpEGHNVKQ?t=832))
- Gemini Flash passes about 75% of scenarios ([15:02](https://youtu.be/FlzpEGHNVKQ?t=902))
- Claude with more thinking is just under 60%, with much longer latency ([15:02](https://youtu.be/FlzpEGHNVKQ?t=902))
- GPT-5 Mini is faster and less accurate than the other models tested (no percentage given) ([15:02](https://youtu.be/FlzpEGHNVKQ?t=902))

## Hot takes
- LLMs should narrate computed facts and not analyse positions themselves, because free reasoning hallucinates.
- A consumer AI feature with a sub-3-second budget cannot rely on reasoning models; the chat-style experience is where long reasoning belongs.
- Domain experts who did not build the system are needed as final judges of model output.

## Tools mentioned
Stockfish, Maia (human-move prediction model), Gemini 3 Flash, Claude Code, Claude Code Channels, GPT-5 Mini, OpenRouter, Slack, GitHub

## Relevance to our work
- **agentos** (2/3): The talk's scenario-based LLM-as-judge eval over mined production cases, run across swappable models, maps to AgentOS evals and to choosing models behind the proxy. → *Mine 15-20 themed scenarios from real proxied requests, score them with an LLM judge plus a human spot-check, and use the set to gate model or routing changes in the L1 router.*
- **prosharness** (2/3): Claude Code Channels pushes external events into a running session and the agent asks for approval back, which is close to ProsHarness's phone-driven approvals. → *Read the Claude Code Channels documentation and compare it with ProsHarness's current approval path to see whether channel injection could replace or simplify phone-based approvals.*
