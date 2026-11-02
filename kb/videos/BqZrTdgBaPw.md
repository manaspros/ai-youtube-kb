# Running a Chess YouTube Channel entirely by AI — Stephan Steinfurt, TNG

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `BqZrTdgBaPw` · [watch](https://youtu.be/BqZrTdgBaPw) · **date:** 2026-07-18 · **length:** 16:31 · **format:** demo · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Stephan Steinfurt · **orgs:** TNG
- **topics:** mcp-and-tools, agent-architecture, product-ux · **tags:** chess, tool-calling, agent-pipeline, nightly-batch, text-to-speech, content-generation, conflicting-tool-outputs, cost-per-run, redundant-tool-calls, gemini, grok, elevenlabs, maia

> Stephan Steinfurt (TNG) shows a nightly, fully automated chess-explainer pipeline: a Gemini 3.1 Pro agent with chess tools narrates analysed human games as YouTube videos.

## Summary
The speaker describes a chess YouTube channel that is generated entirely by AI. Each night the system downloads human games from chess sites, analyses them in the background, lets an agent analyse them more deeply, and turns the result into a structured format that a text-to-speech step renders as a video. The core problem is that chess engines play strongly but cannot explain moves, while LLMs can explain but play poorly, so the team combines them in one tool-using agent. The agent uses Gemini 3.1 Pro with tools for legal moves, a board it can move on and take back, an engine, a checks/captures/threats summary, a human-move model, historical game lookup and web search. The main design shift was moving from Python scripts that pre-assembled analysis to letting reasoning models decide which tools to call. The channel had roughly 500k views and over 4,000 subscribers at the time of the talk, mostly gained in the last month, with no monetisation yet. The speaker reports an error rate of about one odd video in twenty, a cost of roughly 20 to 30 cents per short video, and redundant tool calls where the agent re-analyses a game. The open questions are which videos to publish and how to balance difficulty for beginners versus strong players.

## Key ideas
- **The core problem is that chess engines are strong but cannot explain, while LLMs can explain but cannot play well, so the design has to combine them.** — The speaker frames it as the main challenge and builds one agent that has both an engine and LLM reasoning. ([3:36](https://youtu.be/BqZrTdgBaPw?t=216))
- **The agent gets many tools instead of pre-computed analysis, and it decides which to call.** — The tool set covers legal moves, a board it can move on and take back, an engine, a checks/captures/threats summary, a human-move model, game history and web search. The earlier Python pipeline that pre-assembled the analysis was dropped once reasoning models could choose the tools themselves. ([5:01](https://youtu.be/BqZrTdgBaPw?t=301))
- **Give the agent a legal-moves tool so it never reasons about illegal moves.** — This is a guardrail placed on the model's output space, with the legal-move list as the source of truth. ([5:01](https://youtu.be/BqZrTdgBaPw?t=301))
- **A checks/captures/threats tool gives the model forcing candidates that it might otherwise miss.** — It is a common beginner heuristic in chess. The speaker notes that some suggested checks are obviously bad, and that the best move (a rook sacrifice) is not obvious, so the model has to judge among the candidates. ([6:22](https://youtu.be/BqZrTdgBaPw?t=382))
- **Conflicting tool outputs are deliberate: the engine's best move is balanced against the most human move.** — A human-move model (Maia, conditioned on a rating) and historical games are added so the commentary does not focus only on the engine's top choice. The speaker says this balance is very useful. ([9:07](https://youtu.be/BqZrTdgBaPw?t=547))
- **The agent also makes presentation choices: it picks the squares to highlight, the arrows to draw and whether a move is brilliant.** — The structured output from the analysis is handed to a text-to-speech step (ElevenLabs v3), which can follow the emotional cues the agent writes in. ([9:07](https://youtu.be/BqZrTdgBaPw?t=547))
- **The speaker is cautious about publishing unreviewed output and is mostly watching for errors rather than checking every video.** — He says the error rate is low (about one video in twenty is odd). Odd outputs are treated as useful signals about missed tool calls. He has moved to accepting most videos and taking down bad ones later. ([12:41](https://youtu.be/BqZrTdgBaPw?t=761))

## Techniques
- **Engine plus LLM split with tools** — Keep the engine as a tool for ground truth on the best move. Give the LLM a legal-move tool, a board it can move on and take back, and separate tools for threats and for human-likely moves. Let the agent explore variations itself. *When:* Any domain where a deterministic solver is strong but cannot explain its results, and the explanation needs to be fluent.
- **Let the reasoning model choose tools rather than pre-computing** — Replace a Python script that gathers analysis and then prompts the model with an agent that calls tools on demand. The speaker says this became workable once reasoning models were good enough to call tools at the right moments. *When:* When the set of relevant facts depends on the position, and fixed pre-computation either over-supplies or misses context.
- **Deliberately conflicting tool outputs** — Offer the engine's best move and a human-likely move side by side, plus history, so the agent has to weigh them and cannot simply repeat the top engine line. *When:* When the output should reflect how people actually behave, not only what is objectively optimal.
- **Nightly batch with a structured intermediate format** — Pull data on a schedule, analyse it in the background, have the agent do deeper analysis, write a structured intermediate format, and then render from that format into media (text-to-speech plus video). *When:* High-volume content or report generation where a human reviews only a sample.
- **Monitor odd outputs and treat them as signals** — Track the rate of odd outputs. Use each one to see where a tool call was skipped. Take down bad items afterwards rather than gating each one. *When:* When the cost of a bad item is low and the volume is high, so review sampling is cheaper than a pre-publish gate.

## Numbers
- Channel reached about 500k views and more than 4,000 subscribers at the time of the talk, most of them gained in the last month. ([11:26](https://youtu.be/BqZrTdgBaPw?t=686))
- The channel does not yet make money, so it is net negative for now. ([11:26](https://youtu.be/BqZrTdgBaPw?t=686))
- Error rate is about one odd video in twenty (for example a missed checkmate or a missed tool call). ([12:41](https://youtu.be/BqZrTdgBaPw?t=761))
- A short video costs roughly 20 to 30 cents to generate. Much longer videos can reach a few euros. Cost is not being optimised yet. ([12:41](https://youtu.be/BqZrTdgBaPw?t=761))
- Newspaper quote in the opening: AI could take about five more years to explain chess as well as a human trainer (cited by the speaker, not verified). ([0:00](https://youtu.be/BqZrTdgBaPw?t=0))

## Hot takes
- Gemini 3.1 Pro is the best model the speaker has seen so far for chess, probably after deep post-training on chess.
- Once reasoning models arrived, letting the agent call tools itself beat a fixed Python pipeline that pre-computed the analysis.
- The speaker prefers accuracy in the explanation over minimising cost, so he is not optimising spend yet.

## Tools mentioned
Gemini 3.1 Pro, Grok 4, ElevenLabs v3, Maia (captioned as Maya), chess engine (unnamed), web search

## Relevance to our work
- **agentos** (1/3): The per-video cost data and the redundant tool calls (the agent re-analysing a game twice) show how a run's spend can be wasted on repeated work. This is a budget signal, not a design for the proxy. → *When adding per-run budget tracking in the proxy layer, flag repeated identical tool calls within one run as a cost event.*
- **prosharness** (1/3): This is a nightly unattended agent run with a tool loop, and the redundant-call problem is the kind of waste a checkpointed harness should avoid. → *Cache per-item analysis results in scheduled ProsHarness loops so a retried or resumed run does not redo finished work.*
- **general** (1/3): A short practitioner example of how an agent should combine conflicting tool outputs (engine best move versus human-likely move) and choose among them. → *Read the notes on balancing conflicting tool outputs as a worked example for context and tool design.*
