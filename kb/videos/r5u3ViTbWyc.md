# JSON Is Dead: TOON Saves Massive Tokens for LLMs and Changes Everything

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `r5u3ViTbWyc` · [watch](https://youtu.be/r5u3ViTbWyc) · **date:** 2025-12-02 · **length:** 8:49 · **format:** tutorial · **quality:** 2/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Better Stack
- **topics:** token-cost-efficiency, context-engineering · **tags:** TOON, JSON, token-cost, tokenization, tabular-arrays, structured-data-for-llms, TypeScript, tsx, gpt-3-encoder

> Better Stack demos TOON, an indentation-based format with tabular arrays, cutting one JSON dataset from 1,236 to 454 tokens (~63%) in a TypeScript script. Strong for uniform records, weaker for deeply nested data; the evidence is a single dataset.

## Summary
The host argues that JSON's quotes, brackets, braces and repeated keys are billed as tokens, and that TOON (captioned as "Tune") removes most of that syntax. TOON uses YAML-style indentation and a table layout for arrays, so keys are declared once per array instead of once per row. The video walks through a small TypeScript script that reads a JSON file, encodes it to TOON, and counts tokens for both forms with a GPT-3 tokenizer library. On his own log dataset, JSON came to 1,236 tokens and TOON to 454, and the TOON version was 11 lines against 94 for the JSON. He says TOON suits logs, metrics, events, catalogs and config tables, but is confusing for heavily nested structures, where he would keep JSON. He closes by extrapolating a 40-50% token cut across pipelines into thousands of dollars saved, without measuring that figure.

## Key ideas
- **JSON syntax is paid for as tokens** — Quotes, brackets, braces, commas and repeated keys are tokens the model must read, so they add cost without adding data. The host frames this as the main reason to change format. ([0:00](https://youtu.be/r5u3ViTbWyc?t=0))
- **TOON declares structure once and uses tables for uniform arrays** — TOON uses YAML-like indentation and a tabular layout for arrays of records. Keys appear once in the header instead of on every row. Uniform arrays such as logs benefit most. ([1:07](https://youtu.be/r5u3ViTbWyc?t=67))
- **Measure before switching: count tokens on your own data** — The video does not rely on the format's claims. It encodes a real JSON file and counts tokens for both versions with the same tokenizer, so the comparison is on the reader's data. ([2:17](https://youtu.be/r5u3ViTbWyc?t=137))
- **Headline result on one dataset: 1,236 to 454 tokens** — The host's log dataset dropped from 1,236 JSON tokens to 454 TOON tokens, about 63%. The 30-60% range he quotes at the start is a general claim, and this is the single measurement behind it. ([6:05](https://youtu.be/r5u3ViTbWyc?t=365))
- **Why it works: arrays get a table, syntax disappears** — The gain comes from removing structural syntax and repeated keys. The host also says models make fewer mistakes with the tabular form, but he does not measure this. ([6:58](https://youtu.be/r5u3ViTbWyc?t=418))
- **Nested data is the failure case** — TOON is not recommended for heavily nested structures, where the host expects the model to get confused. For those he keeps JSON. ([6:58](https://youtu.be/r5u3ViTbWyc?t=418))
- **Savings extrapolation is unmeasured** — He suggests a 40-50% token reduction across all pipelines could save thousands of dollars. The figure is an estimate with no workload behind it. ([8:03](https://youtu.be/r5u3ViTbWyc?t=483))

## Techniques
- **Benchmark a JSON-to-TOON conversion on your own payload before adopting it** — 1) Install the TOON encoder library from npm (captioned as 'tune format slash tune'; the exact package name is not spoken clearly, so check it on npm). 2) Install a GPT-3 tokenizer package (captioned as 'gpt-3 encoder', likely gpt-3-encoder) with npm install. 3) Create convert.ts. 4) Read the file with fs.readFileSync("data.json", "utf-8") and JSON.parse it. 5) Call TOON's encode(json) to get the TOON string. 6) Build the JSON baseline with JSON.stringify(json, null, 2). 7) Count tokens for each string with the tokenizer's tokenize(...).length. 8) Print both counts and the reduction. 9) Run with `npx tsx convert.ts`. *When:* Before switching a pipeline's prompt payloads from JSON to TOON, to get the real savings on your data instead of the 30-60% headline.
- **Use TOON for uniform arrays of records, keep JSON for nested objects** — Send arrays of same-shape rows (logs, metrics, events, product catalogs, config tables) as TOON, where keys are declared once and rows are tabular. Keep deeply nested or irregular structures in JSON. *When:* When the prompt payload contains large lists of records with the same fields, and the cost of repeated keys matters.
- **Quick visual comparison with a web converter** — Paste a JSON sample into a web-based JSON-to-TOON converter and compare the output side by side with the original. The host uses this only to visualize the format; he does not name the site. *When:* For a fast look at what TOON output will look like before writing any code.

## Numbers
- Reduction range claimed for TOON vs JSON, 30-60%, with the speaker personally reaching 63% ([0:00](https://youtu.be/r5u3ViTbWyc?t=0))
- JSON tokens 1,236 vs TOON 454 on the host's log dataset, a 63% reduction ([6:05](https://youtu.be/r5u3ViTbWyc?t=365))
- JSON file 94 lines vs TOON output 11 lines ([6:58](https://youtu.be/r5u3ViTbWyc?t=418))
- Speaker's extrapolation: 40-50% token reduction across all pipelines could save thousands of dollars (unmeasured estimate) ([8:03](https://youtu.be/r5u3ViTbWyc?t=483))

## Hot takes
- The title says JSON is dead and TOON changes everything, but the evidence is one converted log dataset counted with a GPT-3-era tokenizer library. Treat the 63% as a single data point.
- Token count is not cost. The video never checks output tokens, the model's own tokenizer, or answer quality, and the 'fewer mistakes' claim is asserted, not tested.
- The dollar-savings extrapolation has no workload behind it and should not be used for planning.
- The 'JSON is dead' framing is overstated. The video itself says nested data should stay in JSON, which is most of what agent tool calls and responses look like.

## Tools mentioned
TOON (JSON-to-TOON format and encoder; installed via npm, captioned 'tune format slash tune'), gpt-3-encoder (GPT-3 tokenizer library used for token counts; captioned 'GPT-3 encoder'), TypeScript, npm, npx tsx, Node.js fs module

## Relevance to our work
- **agentos** (1/3): AgentOS L1 handles budgets and cost control at the proxy. Payload-format token savings could feed that accounting, but the video offers only one measurement. → *Measure JSON vs TOON token counts on the actual log and telemetry payloads AgentOS forwards, using the model's own tokenizer, before deciding whether to add a serialization option.*
