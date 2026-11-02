# When Agents Meet Physical Data: The Other Physics of Agent Harnesses - Dmitry Petrov, DataChain

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `bUJgirn4_yc` · [watch](https://youtu.be/bUJgirn4_yc) · **date:** 2026-08-18 · **length:** 27:32 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Dmitry Petrov · **orgs:** DataChain, Anthropic, OpenAI
- **topics:** data-engineering, agent-architecture, memory · **tags:** unstructured-data, physical-ai, video, pydantic, data-harness, incremental-processing, checkpointing, lineage, knowledge-base, claude-code

> DataChain's Dmitry Petrov argues coding agents need a "data harness" for physical and unstructured data (video, sensors), built on Pydantic schemas, incremental checkpoints and reusable derived datasets.

## Summary
The speaker, from DataChain, says coding agents fail on physical data such as video, sensor and robot telemetry, and cites a 21% accuracy figure for data tasks from Anthropic and a six-layer context setup from OpenAI. He argues the missing piece is a data harness: a schema layer, an execution engine and a knowledge base. In his demo, Claude Code with a DataChain skill runs YOLO detection over 91 dash-cam clips, stores results as typed rows in a local database, and answers questions with simple queries. He recommends Pydantic models as the one language for schemas and code, typed functions that the engine can parallelise, and incremental runs that reuse finished work. He also argues that agents should check for an existing derived dataset before recomputing, and should keep a per-dataset markdown note with source code and lineage. The talk is partly a pitch for the open-source DataChain project, so the performance claims are mostly the speaker's own and no independent benchmarks are shown.

## Key ideas
- **Agents do poorly on physical and unstructured data, and the fix is a data harness rather than a stronger model** — The speaker cites a claimed 21% accuracy for data tasks without a data harness and argues that the brain (the LLM) is not the missing piece. He says the agent also needs a way to see data, run code, verify results and remember useful datasets. ([0:01](https://youtu.be/bUJgirn4_yc?t=1))
- **One raw file expands into a very large number of structured objects** — A video holds clips, frames, objects and labels, and the speaker says 2,000 video files can yield millions of objects. Metadata kept as JSON files on object storage is slow and inconsistent, and a separate central database adds a second stack that researchers avoid. ([3:04](https://youtu.be/bUJgirn4_yc?t=184))
- **Use Pydantic models as the single schema language for code and storage** — The schema is an ordinary Pydantic class that also maps to SQL, so there are no SQL islands in the codebase. The speaker says this is the easiest route for researchers. ([4:03](https://youtu.be/bUJgirn4_yc?t=243))
- **Ask scope questions before the run, then answer later questions from the database** — In the demo the harness asks which model, which size, which tracking granularity and which dataset slice to use. The run over 91 clips took about 24 minutes, and later questions are answered by fast queries over the stored results rather than by re-parsing JSON. ([7:55](https://youtu.be/bUJgirn4_yc?t=475))
- **Parallelise by typed function signatures, not by hand-written job code** — A function is typed with Pydantic input and output, and it either maps one file to one row or generates many rows. The engine uses those types and the file set to spread work across machines, and the user just states how many machines to use. ([16:09](https://youtu.be/bUJgirn4_yc?t=969))
- **Incremental, checkpointed runs are essential when LLM calls make compute expensive** — If a run fails halfway, the engine should keep finished results and process only the new or failed files. The speaker says losing half of an expensive run is common and is the thing to avoid. ([17:38](https://youtu.be/bUJgirn4_yc?t=1058))
- **Build a reusable derived layer before answering, and test against one correct answer** — The speaker says data tasks have one right answer, unlike code, so tests matter more. Agents should stop running Python over raw files each time, and should ask whether a general dataset already exists that can answer the question with one query. ([19:40](https://youtu.be/bUJgirn4_yc?t=1180))
- **Store a knowledge note per dataset with source code and lineage so teammates and agents can reuse it** — Each dataset has a markdown note with its purpose, session context, an LLM-written description, a schema preview, stats and the source code, linked to the source files and the output table. The speaker says the source code is the most important part of that context. ([22:39](https://youtu.be/bUJgirn4_yc?t=1359))

## Techniques
- **Pydantic schema as the only data model** — Define each output record as a Pydantic class with nested fields such as file path, checksum, ETag and size. Use that class for storage, queries and function signatures, so no separate SQL schema is kept. *When:* Use it when unstructured or nested outputs must be queried later and the team wants one language for code and schemas.
- **Typed mapper and generator functions for parallel processing** — Write a plain Python function with typed inputs and outputs. A mapper returns one row per input file, and a generator returns many rows that are saved as one table. The engine runs it in parallel from the stated resource count. *When:* Use it for per-file LLM or vision processing where each file gives one or more records.
- **Incremental runs with checkpoints** — Record which inputs have finished. On a rerun, process only new or failed inputs and keep the completed results, without recomputing the rest. *When:* Use it for long, expensive batch jobs that can fail partway, or where new files arrive over time.
- **Check for an existing derived dataset before computing** — Before running expensive extraction, the agent asks whether a dataset covering the question already exists. If not, it builds a dataset general enough for related questions and saves it for reuse. *When:* Use it when several people or agents ask related questions about the same raw corpus.
- **Per-dataset knowledge note with lineage** — For each dataset, keep a markdown file with purpose, session context, schema preview, stats, the source code and links from source files to output tables. *When:* Use it to share derived data across a team and let agents reuse past work without rerunning it.

## Numbers
- Anthropic's cited accuracy for data projects on its agents without a data harness: 21%. This is the speaker's citation of a third-party result, not verified here. ([0:01](https://youtu.be/bUJgirn4_yc?t=1))
- OpenAI's data agent setup described as six layers of context (speaker's citation). ([1:01](https://youtu.be/bUJgirn4_yc?t=61))
- 2,000 video files can produce millions of objects (speaker's estimate). ([3:04](https://youtu.be/bUJgirn4_yc?t=184))
- Demo: 91 January dash-cam clips processed in 24 minutes using the smallest YOLO model and per-frame speed tracking. ([7:55](https://youtu.be/bUJgirn4_yc?t=475))
- Demo result: 82 of 91 clips contain at least one detected person. ([7:55](https://youtu.be/bUJgirn4_yc?t=475))
- About 90 videos produced roughly 100,000 records in the database. The speaker says object-level records can be 10x to 100x that, and at thousands of videos the count reaches the million scale. ([10:49](https://youtu.be/bUJgirn4_yc?t=649))

## Hot takes
- Frontier models alone will not fix physical-data work; you need a data harness instead (speaker: "you don't use stronger models").
- Unlike software, a data problem usually has one correct answer, so testing and verification matter more in data projects.
- Agents should stop running Python over raw binaries each time and should build a reusable metadata layer first, in the style of dimensional modelling.

## Tools mentioned
DataChain, Pydantic, Claude Code, YOLO, Ray, Spark, Dask, Git4Data

## Relevance to our work
- **prosharness** (2/3): The talk's incremental checkpoint model (keep finished units, rerun only new or failed ones) bears directly on ProsHarness checkpoint/resume of long agent runs. → *Check whether ProsHarness resume skips already-completed units and reruns only failed or new ones, and write a test with a mid-run failure to confirm it.*
- **agentos** (1/3): The per-dataset knowledge note with lineage and the check-for-existing-derived-data step relate to MemoryMesh knowledge buckets, but the talk is about file-derived tabular data rather than agent memory. → *Compare DataChain's per-dataset markdown note with source code and lineage against MemoryMesh knowledge buckets, and test whether a retrieval step checks for an existing derived artifact before recomputing.*
