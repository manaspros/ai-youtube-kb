# Stop Renting Your AI's Memory — Dylan Couzon, Qdrant

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `apyrzaWj0Z4` · [watch](https://youtu.be/apyrzaWj0Z4) · **date:** 2026-10-04 · **length:** 15:17 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Dylan Couzon · **orgs:** Qdrant
- **topics:** memory, rag-retrieval, local-ai · **tags:** local-first, vector-search, embedded-vector-db, agent-memory, quantization, edge, data-ownership, open-weights, robotics-demo, yolo

> Dylan Couzon (Qdrant) argues agent memory should be owned locally: models are rented, but a private, retrieval-based memory store compounds and stays portable. Includes a live offline drone-vision memory demo.

## Summary
Dylan Couzon, a developer relations engineer at Qdrant, argues that the real question about advanced AI is who owns it, not when it arrives. He says compute, model, and harness are all typically rented, and that the memory which personalizes an assistant is the part that should compound and belong to the user. He frames memory as three operations (write, retrieve, forget) and says retrieval with filters and decay gives more control than stuffing everything into a prompt. He uses the model-as-CPU, context-as-RAM, memory-as-disk analogy and argues the disk should be local. He presents an embedded, in-process vector store with per-app folders, quantization for small footprints, and a live demo where a drone's object labels and embeddings run fully offline. He ends by arguing that cloud sync and sharing should be opt-in. The talk is part philosophy and part vendor pitch, but the demo and storage design give it some practical content.

## Key ideas
- **Ownership is the real issue: compute, model and harness are rented, and the personal memory that should compound is rented too.** — The speaker says owning inference gives autonomy, but only memory gives continuity. Labs ship memory features because models carry nothing between sessions. ([2:33](https://youtu.be/apyrzaWj0Z4?t=153))
- **Memory is three verbs: write, retrieve, forget.** — Retrieval gives control that a big prompt does not: filter by topic, decay by recency and frequency, and let relevance shift over time. ([5:01](https://youtu.be/apyrzaWj0Z4?t=301))
- **Model is CPU, context window is RAM, memory is disk.** — This framing comes from Karpathy, as the speaker quotes it. The argument is that the disk holding the record of the user should be local and durable. ([6:01](https://youtu.be/apyrzaWj0Z4?t=361))
- **Use an embedded vector store inside the app process, with one isolated folder per app.** — Writes embeddings with payloads and queries offline. The folder is portable, and the speaker says keeping the same embedding model keeps it usable across reasoning models and hardware. ([7:00](https://youtu.be/apyrzaWj0Z4?t=420))
- **Live demo: perception labels become embedded memories for a drone.** — YOLO detections are labeled, the label and image are embedded with timestamps, and semantic search runs fully offline. The memory tracks first and last seen times and how often each object was seen. ([8:31](https://youtu.be/apyrzaWj0Z4?t=511))
- **Cloud sync should be an opt-in layer on top of local stores.** — Local stores can sync to a shared cloud memory for a swarm or family, but sharing is opt-in and consent-based. The speaker says memory can also be extracted without consent, which is why it should start local. ([9:59](https://youtu.be/apyrzaWj0Z4?t=599))
- **Memory compounds: a mediocre model with long memory feels better than a brilliant stranger.** — The speaker says the gain comes from the model never stopping learning the user's corrections, preferences and dead ends, not from the model changing. ([11:29](https://youtu.be/apyrzaWj0Z4?t=689))

## Techniques
- **Write-retrieve-forget memory loop** — Store observations as embeddings with payload metadata, retrieve by semantic similarity with topic filters, and apply recency and frequency decay so old or rarely used items fade. *When:* Long-lived assistants or agents that must remember corrections, preferences and past dead ends across sessions.
- **Embedded in-process vector store with per-app folder** — Open a local vector store inside the app process, write embeddings with payloads, query offline, and keep each app's store in its own isolated folder that can be copied between devices. *When:* Single-user or local-first agents where data should stay on the user's machine and the store must be portable.
- **Quantized vectors for small footprint** — Apply quantization to the stored vectors so the memory store is small enough for phones or small boards. *When:* Edge devices or when many memories must fit in limited RAM or disk.
- **Pin the embedding model for portability** — Keep the same embedding model when swapping reasoning models or hardware, so the stored vectors stay valid. *When:* Any memory store that must outlive a change of LLM or device.
- **Detector labels then embeddings for perception memory** — Run an object detector, turn each label and its frame into an embedding, and record first-seen and last-seen timestamps plus a count per object. *When:* Robots, drones or video agents that should recall what they have seen.
- **Opt-in sync of local memory to a shared store** — Keep memory local by default and push selected parts to a shared cloud store only when the user chooses, so several devices can learn from each other. *When:* Fleets of robots or families who want a shared memory they control.

## Numbers
- A machine under $2,500 can run what was roughly last year's frontier model (speaker's estimate). ([1:33](https://youtu.be/apyrzaWj0Z4?t=93))
- Some developers reportedly burn over $5,000 a month of compute on a $200 plan (speaker's anecdote, implying subsidy). ([3:59](https://youtu.be/apyrzaWj0Z4?t=239))
- HNSW dates to 2016 and local embeddings have run since 2019 (historical context). ([6:01](https://youtu.be/apyrzaWj0Z4?t=361))
- Sub-millisecond queries; claimed the same raw score as the cloud engine when run locally. ([7:00](https://youtu.be/apyrzaWj0Z4?t=420))
- With quantization, a million memories fit in under 1 GB, small enough for a phone or Raspberry Pi (speaker's claim). ([7:00](https://youtu.be/apyrzaWj0Z4?t=420))
- Demo: 92 distinct objects, over 300 vectors, total engine footprint about 15 MB, semantic search under 1 ms, fully offline. ([8:31](https://youtu.be/apyrzaWj0Z4?t=511))

## Hot takes
- Memory, not the model, is the moat: a model that never forgets you beats a smarter one that starts from zero.
- Labs ship memory features because models carry nothing between sessions, and that continuity is what they want to sell back to users.
- Frontier labs already build an index of users, so local-first memory has to exist whether or not users opt in.
- Owning weights and inference only gives autonomy; continuity requires owning the memory store.

## Tools mentioned
Qdrant, YOLO

## Relevance to our work
- **agentos** (2/3): MemoryMesh (L2A) needs per-app or per-tenant memory stores; the talk's embedded, folder-portable, quantized store is a concrete alternative to the pgvector-only path worth measuring. → *Prototype an embedded local vector store for one MemoryMesh bucket with quantized vectors and compare footprint and query latency against the current pgvector path on the 5090 box, keeping the embedding model pinned so stores stay portable.*
- **prosharness** (1/3): The RAM-versus-disk framing maps to checkpoint and resume; cross-run facts such as corrections and dead ends could persist in a store instead of being re-stuffed into the context on resume. → *Consider keeping cross-run facts (corrections, dead ends) in a small local retrieval store that is queried on resume, instead of replaying them through the context window.*
