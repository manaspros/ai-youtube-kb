# Every Building Is a Balance Sheet: Spatial Memory for Real-World Assets — Jordi Spranger, Spranic

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `Fe4aSMXsOZ4` · [watch](https://youtu.be/Fe4aSMXsOZ4) · **date:** 2026-10-14 · **length:** 10:29 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Jordi Spranger · **orgs:** Spranic, Neo4j, Kroll
- **topics:** data-engineering, voice-multimodal, product-ux · **tags:** spatial-memory, graph-database, change-detection, provenance, real-estate, insurance, 3d-scanning, neo4j, digital-twin, natural-language-query

> Jordi Spranger (Spranic, with Neo4j) pitches walk-through 3D scans stored as a time-aligned graph, so real buildings become queryable, change-tracked data for insurance and lending.

## Summary
The speaker argues that real estate, the largest asset class at about 400 trillion globally, is tracked in financial books updated quarterly while the buildings themselves are only re-checked every few years. He proposes "spatial memory": anyone walks a space with an off-the-shelf sensor, a scan is produced in about a minute, and recognised objects are stored in a Neo4j graph. Repeat walks are aligned on a time axis so that object-by-object changes can be detected, and each observation keeps a reference to its source capture as evidence. The map can then be queried in natural language, with examples such as finding a radiator or a mug in a kitchen, and displaced chairs shown as a change between two passes. The main use case is insurance, where a renewal walk gives the insurer a delta to price against, with cited figures on underinsurance and certification discounts. The talk is a short product pitch from a company founded in June 2026, so the claims are largely unverified in the talk itself.

## Key ideas
- **Real-estate records lag reality** — Financial books on buildings are updated quarterly, but the physical assets behind them are only re-checked about every few years, leaving a black box between updates. ([1:07](https://youtu.be/Fe4aSMXsOZ4?t=67))
- **Capture a building by walking it** — An off-the-shelf sensor is walked through a space; the speaker says a scan is ready about a minute later, and recognised assets are written into a graph database. ([3:21](https://youtu.be/Fe4aSMXsOZ4?t=201))
- **Repeat walks align on a time axis** — Each walk is kept as a time-stamped layer, so the same space can be compared across months or quarters and its evolution tracked. ([3:53](https://youtu.be/Fe4aSMXsOZ4?t=233))
- **Ask ledger-style questions of a building** — The required questions are what changed, when it changed (each observation carries its source), and who must be told about the delta. ([4:58](https://youtu.be/Fe4aSMXsOZ4?t=298))
- **Change detection with proof** — In a kitchen demo, three displaced chairs are flagged between two passes, and the answer links back to the capture that shows the change. ([7:10](https://youtu.be/Fe4aSMXsOZ4?t=430))
- **Insurance uses the renewal delta** — An initial walk at policy start and a second walk at renewal give the insurer a measured upkeep delta to price premiums against. ([8:17](https://youtu.be/Fe4aSMXsOZ4?t=497))

## Techniques
- **Repeat-capture alignment and diffing** — Capture the same space at several points in time, match objects between captures, and compare them object by object and surrounding by surrounding to get a delta. *When:* Any domain where the same environment is snapshotted repeatedly and you need to know what changed.
- **Graph as the world model** — Store recognised objects and spaces as graph nodes and link each observation to its capture, so new relationships and attributes can be added per asset. *When:* When the data needs flexible, asset-specific connections rather than a fixed schema.
- **Provenance on every observation** — Attach a reference to the originating capture to each fact so claims can be checked against the raw evidence. *When:* Audit, insurance or compliance settings where a claim must be backed by source material.
- **Natural-language query over a graph map** — Let users ask questions of the mapped space and return answers tied to specific objects, with the delta and source shown. *When:* When non-technical users need to query structured spatial data.

## Numbers
- Real estate is about 400 trillion globally, more than global equities, debt and gold combined (residential ~300T, commercial ~60T, agriculture ~50T) ([0:34](https://youtu.be/Fe4aSMXsOZ4?t=34))
- Kroll research on 1,500 properties found about 70% of buildings underinsured (speaker does not know the cause) ([2:48](https://youtu.be/Fe4aSMXsOZ4?t=168))
- The underinsurance problem affects about 4 trillion US commercial mortgages ([2:48](https://youtu.be/Fe4aSMXsOZ4?t=168))
- Real estate records are typically updated about every 5 years (year 0 to year 5 gap) ([1:42](https://youtu.be/Fe4aSMXsOZ4?t=102))
- A full scan of a conference hall took about a minute of walking ([3:21](https://youtu.be/Fe4aSMXsOZ4?t=201))
- One in three commercial buildings are on the books with the wrong construction class ([8:49](https://youtu.be/Fe4aSMXsOZ4?t=529))
- A 35% hurricane-premium deduction is available for certified buildings ([8:49](https://youtu.be/Fe4aSMXsOZ4?t=529))
- 73% of insurers agree they claim fewer hurricane damages when buildings are checked and certified (transcript reads '70% 73%', exact figure unclear) ([9:23](https://youtu.be/Fe4aSMXsOZ4?t=563))

## Hot takes
- A building should be as queryable as a ledger, answering in milliseconds rather than after a site visit.
- Every walk should become a memory of the building.
- Insurance should be priced on measured, verified property upkeep rather than old, coarse records.

## Tools mentioned
Neo4j, off-the-shelf 3D scanning sensor

## Relevance to our work
- **agentos** (1/3): MemoryMesh could use the same idea of time-aligned, provenance-linked observations across sessions, but the talk gives no retrieval or consistency detail. → *Read the talk's time-aligned provenance pattern as a loose idea for MemoryMesh conflict resolution and provenance; no implementation change needed yet.*
- **general** (1/3): Matching the same object across two captures is an entity-alignment problem, which is a recurring interest, but the talk does not describe the method. → *Skip unless a real-world-asset or spatial-data project comes up; the talk has no transferable technique detail.*
