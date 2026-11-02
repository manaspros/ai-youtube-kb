# How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `XBaznoTRDFI` · [watch](https://youtu.be/XBaznoTRDFI) · **date:** 2026-06-18 · **length:** 20:43 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Phil Hetzel · **orgs:** Braintrust, Slalom, Grafana, Datadog, ClickHouse, SingleStore
- **topics:** observability, evals, data-engineering · **tags:** agent observability, tracing, full-text index, trace clustering, human annotation, LLM scorers, online scoring, Braintrust, ClickHouse, Tantivy

> Braintrust's solutions lead argues agent observability differs from uptime-focused tracing: quality, non-determinism, huge text-heavy traces, and domain experts in the loop.

## Summary
Phil Hetzel of Braintrust argues that agent observability is a different problem from traditional observability. Traditional tools like Grafana and Datadog answer whether a system is up, how fast it responds, and whether it returns errors. Agent observability also has to answer quality questions: whether the answer is grounded in retrieved context, whether the right tools were used, and whether the output matches the brand rules in the system prompt. Agent traces are also far larger and more text-heavy than normal traces, with some over 1 GB and single spans reaching 20 MB. That pushes teams toward a database built for agent traces, with real-time ingest, full-text indexing, and SQL access. He says the best teams include non-technical domain experts such as clinicians and lawyers in trace review. He also argues observability and evals are one system, differing only in whether inputs are known in advance and run in batch. The last part covers clustering traces with a light LLM to find topics, intent, sentiment and issues, and turning human grades with written justifications into automated scorers. The talk is mostly conceptual, with light product mentions and a Q&A.

## Key ideas
- **Agent observability measures quality, not just uptime and latency** — Traditional tooling answers whether the system is up and responding with errors or latency. Agent tooling must also check groundedness in retrieved context, correct tool use, and alignment with the brand rules in the system prompt. ([6:07](https://youtu.be/XBaznoTRDFI?t=367))
- **Agents are non-deterministic, so the metrics must be broader** — Traditional apps follow fixed control flow that can be measured with a few known metrics. Agents pick different paths, so the team needs to see why a path was taken, not just that it ran. ([4:55](https://youtu.be/XBaznoTRDFI?t=295))
- **Agent traces are very large and semi-structured** — A single agent trace can exceed 1 GB and one span can reach 20 MB, with lots of unstructured text. Ingesting and querying this is a different systems problem, and it still has to be near real time. ([7:26](https://youtu.be/XBaznoTRDFI?t=446))
- **Two read patterns are needed at once** — Teams need fast live views of an agent action as it happens, and also SQL or CLI access for batch queries that feed automated improvement of the app. ([8:54](https://youtu.be/XBaznoTRDFI?t=534))
- **Full-text indexing is needed because people search traces by words** — Questions like finding every trace that mentions a given word are hard without a full-text index. Braintrust uses Tantivy, a Rust library similar to Lucene, and he says ClickHouse lacked text indexes at the time, so they built their own database. ([10:03](https://youtu.be/XBaznoTRDFI?t=603))
- **Non-technical domain experts belong in trace review** — Clinicians, nurses, wealth advisors and lawyers look at traces and improve prompts in plain language. Traditional observability is run by systems engineers, but agent quality depends on people close to the users and the domain. ([11:29](https://youtu.be/XBaznoTRDFI?t=689))
- **Observability and evals are the same system** — The only difference is that evals run in batch on inputs known in advance, while observability sees unknown inputs in real time. ([12:36](https://youtu.be/XBaznoTRDFI?t=756))
- **Clustering traces with a light LLM surfaces topics, intent, sentiment and issues** — Braintrust embeds traces and clusters them with a lightweight LLM to see how users use the agent, how they feel about it, and what problems they hit. The aim is to shorten the loop from a production problem to an experiment that fixes it. ([13:38](https://youtu.be/XBaznoTRDFI?t=818))
- **Expert grades with justifications can become automated scorers** — Experts grade traces and explain their reasoning. The explanations are then run through an LLM to build scalable scoring functions, and the failure modes they reveal become automated checks. ([16:18](https://youtu.be/XBaznoTRDFI?t=978))

## Techniques
- **Split quality metrics from technical metrics** — Keep standard metrics such as time to first token, total tokens, duration and cache hits from tracing. Add quality scores on top for grounding, tool use and brand alignment. *When:* When an agent is in production and you need to know whether it behaves well, not just whether it is up.
- **Full-text index on traces with SQL access** — Index the text in traces with a full-text engine so word searches are fast, and expose the data through SQL or a CLI so batch jobs can query it. *When:* When traces are large, text-heavy and searched by content, and standard columnar indexes are too weak for word search.
- **Trace to offline dataset to experiment** — Take a production trace, add it to an offline dataset, and rerun experiments on it. *When:* When a production failure needs to be reproduced and tested against a fix before release.
- **Human grades with justification to LLM judges** — Have domain experts score traces and write why. Feed the justifications to an LLM to draft scoring functions, then use the failure modes they expose as automated checks. *When:* When you need a scalable judge but have no rubric yet, and experts can explain their grades.
- **Embed and cluster traces to find unknown unknowns** — Embed traces, cluster them with a light LLM, and look for clusters that show intent, sentiment or recurring issues. Pair known issues with online scores, and use open-ended clusters to find issues nobody defined. *When:* When you do not know what users are doing or what is going wrong with the agent in production.

## Numbers
- An agent trace can be over 1 GB in size, seen in Braintrust's own customers ([7:26](https://youtu.be/XBaznoTRDFI?t=446))
- An individual span can be as large as 20 MB ([7:26](https://youtu.be/XBaznoTRDFI?t=446))
- The clustering feature for traces was rolled out about a month before the talk ([13:38](https://youtu.be/XBaznoTRDFI?t=818))

## Hot takes
- Observability and evals should be built as one system, not two.
- Non-technical domain experts are essential to agent observability, unlike traditional observability.
- Agent observability is a systems problem with the text and volume of traces, not a dashboard problem.
- Teams that use ClickHouse or other columnar stores may need a text index for trace search.

## Tools mentioned
Braintrust, Grafana, Datadog, ClickHouse, Tantivy, Apache Lucene, SQL, CLI

## Relevance to our work
- **agentos** (2/3): AgentOS L4 observability and L2A evals could use trace-to-dataset promotion and expert-grade-to-judge workflows. → *Read the Braintrust blog on trace storage and see whether AgentOS can promote a proxy trace into an offline eval dataset, then score it with an LLM judge trained on expert justifications.*
