# What Really Happens Inside ChatGPT (AI Explained)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ZTmZOdB5o0U` · [watch](https://youtu.be/ZTmZOdB5o0U) · **date:** 2026-10-12 · **length:** 8:24 · **format:** other · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, GitHub, Slack
- **topics:** models-research, rag-retrieval, mcp-and-tools, training-finetuning-rl · **tags:** llm-basics, tokenization, transformer, embeddings, vector-database, lora, quantization, tool-calling, mcp, agents, explainer

> An eight-minute beginner tour of LLM internals (tokens, weights, transformers, training, LoRA, quantization, RAG, tool calling, MCP, agent loops) with no product pitch, pitched at newcomers rather than builders.

## Summary
The video walks through 16 basic LLM concepts in about eight minutes, from next-token prediction and tokenization up to agents. It explains that models are stateless, so chat "memory" is stored text that gets resent with every message, and that providers price and limit by tokens (about three quarters of a word each). It covers weights and parameters, transformer attention plus feed-forward layers, and the training stages of pre-training, fine-tuning and reinforcement learning, where the reward can come from humans (RLHF) or from a computer check such as passing tests. It then covers cheaper adaptation and deployment (LoRA and quantization) and how to give a model knowledge it was not trained on (embeddings in a vector database with RAG). The last part covers tool calling, MCP, and agents as an LLM running in a loop. Content is simplified and has no benchmarks, but the stateless-memory and agent-loop framing is accurate and directly useful for designing our harness and registry.

## Key ideas
- **LLMs are stateless; chat memory is stored text that is re-sent with every message, so the 'memory' is an illusion created by replaying the conversation.** — Every request carries the whole conversation again, even when the product seems to remember the user from last week. Memory is plain text kept in a file and added to the prompt. ([0:00](https://youtu.be/ZTmZOdB5o0U?t=0))
- **Models process tokens, not characters or words, and tokens are the unit providers use for pricing and limits.** — Text is split by a tokenizer into chunks that recur often (common words get one token, rare words split into pieces). A token is roughly three quarters of a word on average. ([0:00](https://youtu.be/ZTmZOdB5o0U?t=0))
- **A model is billions of weights set during training; inference uses the frozen weights.** — Most LLMs have around 100 layers of many neurons. Each layer runs attention (tokens mix in context from earlier tokens) then a feed-forward step. The last position's scores pick the next token. ([2:05](https://youtu.be/ZTmZOdB5o0U?t=125))
- **Pre-training is next-token prediction with backpropagation; fine-tuning and RL then shape the model toward tasks and preferences.** — Each wrong guess nudges weights via backpropagation, repeated trillions of times. Fine-tuning uses a small curated set. RL scores the model's own answers, from human raters (RLHF) or a checker such as a passing test. ([3:18](https://youtu.be/ZTmZOdB5o0U?t=198))
- **LoRA trains a small add-on on top of frozen weights, which is what most people doing their own fine-tuning actually run.** — The add-on is often under 1% of the original model's size, so fine-tuning can fit on a single GPU at much lower cost. ([4:23](https://youtu.be/ZTmZOdB5o0U?t=263))
- **Quantization trades accuracy for memory by storing weights in fewer bits.** — Storing an 8B-parameter model at 16 bits takes about 16 GB; at 4 bits about 5 GB, which fits a laptop. Fewer bits lose more accuracy, and the speaker warns against pushing it too far. ([4:23](https://youtu.be/ZTmZOdB5o0U?t=263))
- **RAG gives a model knowledge it was never trained on by retrieving embedded chunks and pasting them into the prompt.** — Text is embedded as vectors and stored next to the source text. A query is embedded the same way and the nearest chunks are retrieved, so a search for 'how do I get my money back' can find a 'refund policy' doc with no shared words. ([5:38](https://youtu.be/ZTmZOdB5o0U?t=338))
- **Tool calling and MCP let a model act on the outside world; the model emits JSON naming a tool and arguments, and the app executes it.** — The app runs the tool and returns the result. MCP standardizes this: each service (GitHub, Slack) publishes its tool list and usage instructions once, and any MCP-capable app can connect. ([7:06](https://youtu.be/ZTmZOdB5o0U?t=426))
- **An agent is an LLM in a loop: take a task, call a tool, read the result, decide the next step, and repeat until done; agents can hand sub-jobs to other agents.** — The loop lets an agent take on jobs far larger than one turn, such as fixing a bug across a whole codebase. ([7:06](https://youtu.be/ZTmZOdB5o0U?t=426))

## Techniques
- **Stateless chat memory via replay** — Persist conversation history or memory notes outside the model (as stored text) and prepend them to every request, since the model keeps no state between calls. *When:* Designing chat or agent memory, or session resume, where the app must carry all context itself.
- **Tool-calling loop** — Declare the tools the model may use. The model replies with a JSON payload naming the tool and its arguments. The app runs the tool and sends the result back as the next message. Repeat until the model answers without a tool call. *When:* Any agent that must read or change external systems (search, shell, databases, APIs).
- **Agent loop with task handoff** — Run the LLM in a loop: receive a task, call a tool or MCP server, read the result, choose the next step. Delegate sub-parts of the job to other agents. *When:* Multi-step jobs that exceed one model turn, such as codebase-wide changes.
- **Retrieval-augmented generation (RAG)** — Chunk documents, embed each chunk, and store vectors next to the text in a vector database. At query time, embed the question, fetch the closest chunks, and paste them into the prompt with the question. *When:* Answering questions over private or recent documents the model was not trained on.
- **LoRA fine-tuning** — Freeze the base model's weights and train a small set of new low-rank weights on top. The add-on is often under 1% of the base model's size. *When:* Customizing an open model for a task on limited hardware, such as a single GPU.
- **Weight quantization for local models** — Store weights at fewer bits (16 to 8 or 4). An 8B model drops from about 16 GB at 16-bit to about 5 GB at 4-bit, at some accuracy cost that grows as bits fall. *When:* Fitting a model into laptop or consumer-GPU memory, after checking quality on your own evals.
- **Reinforcement learning with a programmatic checker** — Let the model write answers, score them with a computer check (such as whether code passes its tests), and nudge weights toward high-scoring outputs. *When:* Tasks with automatically verifiable outcomes, such as code with a test suite.

## Numbers
- A token is about three quarters of a word on average; providers use tokens for pricing and limits. ([1:01](https://youtu.be/ZTmZOdB5o0U?t=61))
- Most LLMs have around 100 layers, each with thousands of neurons. ([1:01](https://youtu.be/ZTmZOdB5o0U?t=61))
- Pre-training repeats the guess-check-adjust cycle trillions of times. ([3:18](https://youtu.be/ZTmZOdB5o0U?t=198))
- LoRA add-ons are often less than 1% of the original model's size. ([4:23](https://youtu.be/ZTmZOdB5o0U?t=263))
- An 8-billion-parameter model at 16 bits per weight is about 16 GB; at 4 bits it is about 5 GB. ([4:23](https://youtu.be/ZTmZOdB5o0U?t=263))

## Hot takes
- The stateless-replay framing (memory is stored text re-sent each turn) is the most practically useful point for builders and is stated correctly.
- The 'predicts the next word' opener is a simplification: the model predicts tokens, which the video itself explains a minute later.
- Numbers are rough and unbenchmarked; the 4-bit size figure ignores KV cache and runtime overhead, and no accuracy loss figures are given.
- The '100 layers' figure is a generalization that varies widely across models.
- Introductory content for newcomers; little for practitioners beyond the framing.

## Tools mentioned
ChatGPT, GitHub, Slack, Better Stack, Model Context Protocol (MCP)

## Relevance to our work
- **agentos** (1/3): Covers quantization and RAG basics that InferCraft and MemoryMesh build on, but at intro level with no new mechanism. → *Use the 16-bit versus 4-bit sizing arithmetic (8B model: about 16 GB versus about 5 GB) as a quick sanity check when listing which models fit on the RTX 5090 for InferCraft, then confirm quality with our own evals.*
- **prosharness** (1/3): Confirms that the model is stateless and the agent is a loop of tool calls and results, which is what checkpoint and resume must persist. → *For checkpoint/resume in ProsHarness, persist the full message history and every tool result, so a resumed run can rebuild the context it needs; the model keeps no state between calls.*
