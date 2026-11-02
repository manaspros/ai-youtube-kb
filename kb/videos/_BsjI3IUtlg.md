# Meta Just Changed Data Compression FOREVER (OpenZL Explained)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `_BsjI3IUtlg` · [watch](https://youtu.be/_BsjI3IUtlg) · **date:** 2025-11-02 · **length:** 5:10 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Andres · **orgs:** Meta, Better Stack
- **topics:** data-engineering, dev-tools, infra-cost-scaling · **tags:** data-compression, format-aware-compression, openzl, zstandard, sddl, open-source, decoder-decoupling, structured-data

> Better Stack explainer of Meta's open-source OpenZL: format-aware compression with a per-format plan and one universal decoder. The claimed gains are on structured data, from a single Meta test.

## Summary
Better Stack (host Andres) explains OpenZL, a Meta open-source compressor that uses the structure of a data format rather than treating files as flat byte streams. The design splits the work: an offline trainer picks a sequence of reversible transforms for each format, the chosen plan is embedded in the compressed file, and a single universal decoder reverses whatever plan the file carries. The speaker argues this avoids maintaining and auditing one bespoke decoder per format while still beating general compressors on structured data. The only performance figures are from one Meta test: a 5.5 MB dataset reduced to 3.5 MB, compressing at 340 MB/s (vs 220 MB/s for ZStandard) and decompressing above 1.2 GB/s. The speaker is candid about limits: unstructured text falls back to ZSTD internally, and parsing formats like CSV adds overhead that can slow compression even when ratios improve. The video is a five-minute overview with no code, no SDDL syntax, and no reproducible benchmark setup, so treat it as a pointer to the project rather than evidence for adoption.

## Key ideas
- **Format-aware compression: OpenZL models the structure of the data (fields, types, repeated values) instead of compressing a flat byte stream.** — General compressors such as ZStandard and GZip miss patterns like repeated enums or integer ranges in CSV, protobuf and nested JSON. Hand-built format-specific compressors do better but scale badly because each needs its own decoder, audit and tests. ([0:00](https://youtu.be/_BsjI3IUtlg?t=0))
- **Plan and decoder are separated: each format gets its own compression plan, but every file decodes with one universal decoder.** — The plan is embedded in the compressed file. The decoder reads the recipe and runs the transforms in reverse, so the binary is the same regardless of format. Compression plans can change without changing the decoder, which the speaker says avoids breaking backward compatibility and makes security auditing easier. ([1:05](https://youtu.be/_BsjI3IUtlg?t=65))
- **Plans are produced offline: a schema in SDDL is written first, then a trainer searches over reversible transform sequences.** — Transforms named in the video are delta encoding, dictionary building and rearranging nested records. The chosen plan is embedded in the output file at encode time. The video does not show SDDL syntax or the trainer's CLI. ([1:05](https://youtu.be/_BsjI3IUtlg?t=65))
- **The speed comes from exposing structure before entropy coding, which lets the backend compressor work on more predictable data.** — The speaker attributes OpenZL's throughput to the transforms running ahead of the entropy coder, not to a faster entropy coder itself. ([3:18](https://youtu.be/_BsjI3IUtlg?t=198))
- **The limits: unstructured text falls back to ZSTD internally, and CSV parsing adds overhead that can slow compression even when the ratio improves.** — The speaker says the gains are largest for logs, telemetry and analytics data. Plain text gets no benefit. ([3:18](https://youtu.be/_BsjI3IUtlg?t=198))
- **Extensibility: because the project is open source, new transforms and parsers can be added for specialised formats such as time series, nested objects and scientific data.** — The speaker expects third parties to contribute parsers for their own data types. ([3:18](https://youtu.be/_BsjI3IUtlg?t=198))

## Techniques
- **Schema-first format description with SDDL** — Describe the input's byte layout, field boundaries and types in an SDDL (Simple Data Description Language) schema so OpenZL knows how bytes map to fields. The video names SDDL but shows no syntax, so the exact file format is not covered. *When:* Use for a recurring structured format (logs, telemetry, analytics exports, protobuf, nested JSON) where the schema is known in advance.
- **Offline plan training over reversible transforms** — Run the offline trainer on sample data from the schema. It searches transform sequences such as delta encoding, dictionary building and nested-record rearrangement, then picks one plan. Encoding embeds the plan in the output file, and any OpenZL decoder reverses it. *When:* Use when you compress large volumes of one format and can afford a training pass to get better ratios than a generic compressor.
- **Evolve the compression plan without redeploying the decoder** — Ship a new or updated plan for a format while keeping the universal decoder unchanged. Old files still decode because their plans are embedded. *When:* Use when you want to change compression settings for a format without breaking readers that are already deployed, or when decoder security review is a bottleneck.

## Numbers
- Test dataset compressed from 5.5 MB to 3.5 MB with OpenZL (about 64% of original size). Dataset type not stated, from a single Meta test. ([2:07](https://youtu.be/_BsjI3IUtlg?t=127))
- OpenZL compression throughput 340 MB/s, versus 220 MB/s for ZStandard, on the same Meta test. ([2:07](https://youtu.be/_BsjI3IUtlg?t=127))
- OpenZL decompression throughput above 1.2 GB/s. ([2:07](https://youtu.be/_BsjI3IUtlg?t=127))

## Hot takes
- The title says Meta 'changed data compression forever'. The video itself concedes the approach is not a magic bullet and falls back to ZSTD on unstructured data, so the headline overstates it.
- All performance figures come from a single unnamed Meta test. No dataset, ZSTD level, hardware or compression settings are given, so the speed and ratio comparison cannot be reproduced from this video.
- Decoupling the plan from the decoder is presented as the main win. The argument is that one decoder means less code to audit and less breakage, which may matter more to some teams than the ratio gain.

## Tools mentioned
OpenZL (Meta, open source, no version stated), SDDL (Simple Data Description Language, OpenZL schema format), ZStandard (ZSTD, used as the fallback backend and as the speed baseline), GZip (named as a general-purpose baseline)

## Relevance to our work
- **agentos** (1/3): L3 storage roadmap includes Parquet + DuckDB archive and ClickHouse analytics. Format-aware compression could apply to structured telemetry archives, but the video gives no comparison on data like ours. → *Benchmark OpenZL against ZSTD on a sample of our own Parquet or telemetry archive before deciding whether the per-format plan workflow is worth the extra step.*
