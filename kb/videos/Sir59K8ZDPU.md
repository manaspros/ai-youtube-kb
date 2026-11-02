# Why Agentic Systems Need Ontologies — Frank Coyle, UC Berkeley

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Sir59K8ZDPU` · [watch](https://youtu.be/Sir59K8ZDPU) · **date:** 2026-08-18 · **length:** 21:18 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Frank Coyle · **orgs:** UC Berkeley
- **topics:** agent-architecture, security-guardrails, data-engineering · **tags:** ontology, neurosymbolic, OWL, RDFS, knowledge-graph, tool-calling, validation, pydantic, guardrails, agent-loops

> Frank Coyle argues agents need ontologies as a symbolic validator around LLM tool loops, checking outputs against domain constraints before acting.

## Summary
Frank Coyle, a Berkeley educator, argues that agentic LLM systems should be paired with ontologies, which are formal representations of entities, relationships and constraints. He frames this as neurosymbolic AI, where the probabilistic LLM is kept on guardrails by symbolic rules. He covers how ontologies get built (top-down with experts, bottom-up from customer interactions) and points to existing vocabularies like schema.org, FOAF and Dublin Core. He then explains RDFS and OWL features (domain/range inference, transitive and functional properties, disjointness, enumerated values) that derive new facts or reject bad ones. The practical core is a tool-calling loop with a validation step: Pydantic checks types at the boundary, an ontology checks results, and invalid output goes back to the model or to a human. He also warns that loops can drift, go off the rails, or run up token costs, and recommends keeping agent steps side-effect free until they pass validation. The talk is conceptual with a short code walkthrough and no benchmarks.

## Key ideas
- **Neurosymbolic pairing keeps the LLM on guardrails** — The speaker says LLMs are probabilistic and that hallucination is a feature of how they work. Pairing them with symbolic rule systems and knowledge graphs constrains them. ([4:18](https://youtu.be/Sir59K8ZDPU?t=258))
- **Ontologies can be built top-down or bottom-up** — Top-down means experts analyse a domain and define entities and relationships. Bottom-up means mining customer interactions for entities and relationships. Existing vocabularies like schema.org, FOAF and Dublin Core should be reused first. ([6:16](https://youtu.be/Sir59K8ZDPU?t=376))
- **RDFS and OWL derive facts and enforce constraints from the side of the graph** — Domain and range can infer types from a triple. Transitive properties chain relationships. Functional properties (one father) can imply two names refer to the same individual. These sit beside the graph rather than inside it. ([9:42](https://youtu.be/Sir59K8ZDPU?t=582))
- **Agent loops are general but can drift and cost money** — The speaker ties sequence, conditionals and loops to Turing completeness and argues agents now have the loop. Loops can run away, let agents drift when they talk to each other, and inflate token counts. ([12:09](https://youtu.be/Sir59K8ZDPU?t=729))
- **Put a validation gate between tool output and the next model turn** — In the loop, the tool runs, its output is put into a form the validator can read, and an ontology check decides whether to accept it, send it back to the LLM, or bring in a human. ([16:03](https://youtu.be/Sir59K8ZDPU?t=963))
- **Pydantic at the door, ontology at the ledger, agents side-effect free** — Pydantic enforces types on tool parameters. The ontology checks results. Agents should avoid writing to the database until the proposed action has been checked against the ontology. ([17:31](https://youtu.be/Sir59K8ZDPU?t=1051))
- **OWL constraints catch business-logic errors that are hard to catch in free text** — Examples: a second refund on the same order (functional property), a payout routed to the support desk instead of the buyer (disjoint classes), and an invalid status outside paid, shipped or refunded (enumerated values). ([19:02](https://youtu.be/Sir59K8ZDPU?t=1142))

## Techniques
- **Validator gate after each tool call** — Run each tool result through a schema or ontology check before feeding it back to the model. On failure, return the error to the LLM for retry or escalate to a human. Only accept results that pass. *When:* Agent loops that call tools whose outputs drive later decisions or writes.
- **Two-layer boundary checks (Pydantic plus ontology)** — Use Pydantic to enforce parameter and output types at the boundary. Then check semantic validity against a domain ontology, such as allowed status values or disjoint entity types. *When:* Python agents where free-text model output needs typed and domain-level checks.
- **Side-effect-free planning, then commit** — Have the agent produce a proposed action without executing it. Validate the proposal against the ontology. Only then execute the write. *When:* Agents that modify databases or external systems, where a bad write is costly.
- **OWL constraints for business rules** — Model business rules as functional properties (at most one value), disjoint classes (entities that must not be confused), and enumerated value sets. A reasoner checks the data against them. *When:* Domains like orders, refunds, payouts or statuses, where invariants must hold.
- **Reuse existing vocabularies** — Start from established ontologies such as schema.org, FOAF or Dublin Core rather than defining every term from scratch. *When:* Starting a new knowledge graph or ontology for a common domain.
- **Bounding and monitoring agent loops** — Watch for infinite loops, drift between agents, and rising token counts. The speaker implies these need explicit limits, though he does not describe a specific mechanism. *When:* Any autonomous loop with multiple agents or tool calls.

## Numbers
- Around 5,000 people attending the conference (audience size, not a benchmark) ([0:08](https://youtu.be/Sir59K8ZDPU?t=8))
- Speaker has taught computer science for 30 to 35 years ([0:08](https://youtu.be/Sir59K8ZDPU?t=8))
- Existing taxonomies such as schema.org and Dublin Core have been developed over the last 15 to 20 years ([8:18](https://youtu.be/Sir59K8ZDPU?t=498))
- Böhm and Jacopini (1966) showed sequence, conditionals and loops are sufficient for Turing completeness ([12:09](https://youtu.be/Sir59K8ZDPU?t=729))

## Hot takes
- LLM hallucination is a feature of probabilistic generation, not just a bug.
- Agents now have loops, and loops make them capable of computing anything a computational device can compute, but also make them risky.
- Symbolic AI and expert systems from the 1980s are coming back as the validation layer for agents.
- Agents should have no side effects until their proposed actions pass an ontology check.

## Tools mentioned
Claude API (Python client, stop_reason tool-use loop), Pydantic, OWL, RDFS, schema.org, DBpedia, Dublin Core, FOAF

## Relevance to our work
- **agentos** (1/3): AgentOS has a gateway with PII and injection scanning and an exec-gate. A typed and ontology-based validator stage for tool results is a related but separate idea, and the talk gives no implementation detail.
- **prosharness** (1/3): ProsHarness runs long Claude Code loops with checkpoints. The talk's warnings about loop drift and runaway cost apply, and its validate-before-advance pattern could guard checkpoints. → *Consider adding a schema check on Claude Code step outputs before a checkpoint is saved, and a hard iteration and token cap on loops and schedules.*
