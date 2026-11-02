# This Tiny Qwen 27B Model Runs on a 12GB GPU

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `XKejQWnispc` · [watch](https://youtu.be/XKejQWnispc) · **date:** 2026-10-24 · **length:** 8:51 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Josh (Better Stack) · **orgs:** Better Stack, Unsloth, ISTA-DAS Lab, PrismML, Underdog
- **topics:** local-ai, inference-serving, mcp-and-tools, evals · **tags:** quantization, tool-calling, local-llm, llama-cpp, benchmarks, gguf-sizing, agent-throughput, prefill

> Better Stack reviews Saluki 27B, a ~7.9GB quantization of a 27B Qwen-family model tuned to keep tool calling intact at the cost of math, and tests it on local llama.cpp and a DGX Spark.

## Summary
The video covers a heavily quantized (about 2.35 bits per weight) 27B model called Saluki, which is built from an existing 2-bit quant rather than full precision and was tuned to preserve tool calling. The presenter runs it under llama.cpp with GPU offload and a 32k context, checks that it emits tool calls only when needed, and compares it with Unsloth quants and Ternary Bonsai 2. Vendor-reported benchmarks show it scoring above the original on tool calling (88 vs 84) but well below on AIME 2025 math (79 vs 96.7). Community tests report tool-call reliability on 200 calls and throughput on a 12GB RTX 3060 and an RTX 3080. The key caveats are that no training details or full-precision checkpoint have been released, the benchmarks are unverified, and a smaller file does not make an agent loop faster, since prefill dominates. The presenter's bottom line is that the model is worth trying for local tool-calling agents on 12 to 16GB, while a normal Q4 is the better pick if coding and math matter and 24GB is available.

## Key ideas
- **Quantization can be aimed at one capability instead of protecting everything evenly.** — Saluki is tuned to preserve tool calling, on the reasoning that an agent needs to pick the right tool and pass correct arguments more than it needs hard math. The presenter argues this is the point of the design. ([2:15](https://youtu.be/XKejQWnispc?t=135))
- **The model was built on top of an existing 2-bit quant, not from full precision.** — The base is a 2-bit quant from ISTA-DAS Lab at 8.42GB. Saluki is slightly smaller, and its tool-calling score rises from 76 to 88 on the publisher's benchmark, which is above the 84 reported for the full-size model. ([2:15](https://youtu.be/XKejQWnispc?t=135))
- **The source of the tool-calling gain is unclear.** — No training details have been published, the model card calls it a preview checkpoint, and there is no full-precision checkpoint to compare against. So it is hard to separate what came from quantization and what came from extra tuning. ([3:17](https://youtu.be/XKejQWnispc?t=197))
- **Tool-calling gains come with real regressions elsewhere.** — Eight of nine model-card benchmarks are tool-calling related. AIME 2025 drops from 96.7 to 79, the 50-task SWE-bench Verified subset from 33 to 30, and parallel tool calls score 42 with a strict parser and 55 with a lenient one. ([5:26](https://youtu.be/XKejQWnispc?t=326))
- **A smaller file does not make an agent faster.** — On a DGX Spark agent loop, Saluki was the slowest of three models at about 10 steps per minute. The bottleneck was prefill, the processing of the input context before generation, so the file size is not the constraint that matters. ([6:52](https://youtu.be/XKejQWnispc?t=412))
- **Alternatives at the same size are less tested.** — Unsloth's IQ2_XXS (7.27GB) and IQ2_S (8.37GB) quants are about the same size but have not been run on the same tool-calling benchmark. Ternary Bonsai 2 is close to 6GB and scored 70, but it needs PrismML's custom llama.cpp fork, whereas Saluki runs on stock llama.cpp and Ollama. ([4:14](https://youtu.be/XKejQWnispc?t=254))
- **Verify the benchmarks yourself before relying on them.** — All benchmark numbers come from the publisher, and the original model's figures come from public benchmarks run with a different harness. The presenter's advice is to test locally and treat the numbers with caution. ([6:52](https://youtu.be/XKejQWnispc?t=412))

## Techniques
- **Serve a GGUF quant locally with llama.cpp** — Run the model through the llama.cpp server with GPU offload, flash attention enabled and a 32,000-token context. The exact flag names are not shown in the video. Ollama also works for this model, though the presenter does not show that path. *When:* Local agent experiments on a single consumer GPU where you want a 12 to 16GB footprint.
- **Two-part tool-calling smoke test** — Give the model a weather tool and ask for the weather in several cities (Salt Lake City, Dubai, Saigon). Check that the tool-call arguments are well formed. Then ask a question that needs no tool and confirm the model answers directly instead of calling one. *When:* Before choosing a local model for an agent. It checks both correct tool use and knowing when not to use a tool.
- **Tool-call reliability count** — Run many tool-call trials and count how many come back parseable, with no tool-call syntax leaking into the normal text. The community tester did this with 200 calls and got 200 clean results. *When:* Comparing models for agents, where a malformed call can break a whole workflow. A small sample is only directional.
- **Recommended settings for tool calls** — Turn thinking off and set temperature to 0, as the model card recommends for tool calls. *When:* Running this model specifically as an agent tool caller. Use different settings for reasoning-heavy work.
- **Report strict and lenient parser scores separately** — For parallel tool calls, the same run scored 42 with a strict parser and 55 with a lenient one. Record which parser produced each score. *When:* Any tool-calling benchmark, because parser strictness can change the result by more than 10 points.
- **Measure agent throughput, not just file size** — Run the model through a real multi-step agent loop and count steps per minute. Check where the time goes, since prefill dominated here. *When:* Choosing a local model for long agent runs, where a smaller quant may still be slower end to end.
- **Pick by workload** — Use the tool-tuned quant for an agent on 12 to 16GB. If you have about 24GB and care about coding and math, use the standard Q4, which is roughly twice the size but keeps more of the original capabilities. *When:* Deciding between a small specialized quant and a larger general quant.

## Numbers
- Original 27B model is about 55GB; Unsloth 4-bit is 16.5GB; Saluki is 7.9GB. ([0:00](https://youtu.be/XKejQWnispc?t=0))
- Saluki averages about 2.35 bits per weight, versus 16 for the original. ([2:15](https://youtu.be/XKejQWnispc?t=135))
- ISTA-DAS 2-bit base quant is 8.42GB; the publisher's tool-calling benchmark scores are 76 (base), 88 (Saluki), 84 (full-size model). ([3:17](https://youtu.be/XKejQWnispc?t=197))
- Unsloth IQ2_XXS is 7.27GB and IQ2_S is 8.37GB; Ternary Bonsai 2 is close to 6GB and scored 70 on the same benchmark. ([4:14](https://youtu.be/XKejQWnispc?t=254))
- One user ran Saluki on a 12GB RTX 3060 with 170k context at about 22 tokens per second. ([4:14](https://youtu.be/XKejQWnispc?t=254))
- A community multi-token prediction version lifted generation on an RTX 3080 from 41 to 66 tokens per second. ([4:14](https://youtu.be/XKejQWnispc?t=254))
- On a DGX Spark, BFCL single-turn scores were 86 for Saluki and 72 for Qwen 3.8 Flash at 4-bit (a smaller model). ([5:26](https://youtu.be/XKejQWnispc?t=326))
- 200 tool calls through Saluki all came back clean and parseable. ([5:26](https://youtu.be/XKejQWnispc?t=326))
- AIME 2025: original 96.7, Saluki 79. ([5:26](https://youtu.be/XKejQWnispc?t=326))
- SWE-bench Verified 50-task subset: original 33, Saluki 30. ([5:26](https://youtu.be/XKejQWnispc?t=326))
- Parallel tool calls: 42 with a strict parser, 55 with a lenient parser. ([5:26](https://youtu.be/XKejQWnispc?t=326))
- Agent loop on a DGX Spark: Saluki was the slowest of three models at about 10 steps per minute. ([6:52](https://youtu.be/XKejQWnispc?t=412))

## Hot takes
- The headline that a 7.9GB model beats the original is true only for tool calling, not general capability, and the presenter says so.
- Vendor benchmarks are unverified, and the comparison to the original uses a different harness, so the 88 vs 84 gap is not conclusive.
- A smaller quant does not guarantee a faster agent, because prefill dominates agent loops.
- For coding and math on a 24GB card, the presenter recommends the standard Q4 over this model.

## Tools mentioned
Saluki 27B (model name as captioned; the transcript attributes it to Underdog), Qwen 27B base model (captioned as 'QEN 3.827B'), Qwen 3.8 Flash (captioned as 'Quen 3.8 Flash next'; used as a comparison model at 4-bit), llama.cpp (llama-server, stock build), Ollama, Unsloth quants (4-bit, IQ2_XXS, IQ2_S), ISTA-DAS Lab 2-bit quant (RCO quantization search), Ternary Bonsai 2 (PrismML custom llama.cpp fork), MLX (an unfinished port was mentioned), BFCL (Berkeley function-calling benchmark, single-turn), AIME 2025, SWE-bench Verified (50-task subset), NVIDIA DGX Spark, RTX 3060 12GB, RTX 3080, Community multi-token prediction head variant

## Relevance to our work
- **general** (2/3): The most reusable lesson is about measurement: tool-calling scores depend on parser strictness, vendor benchmarks differ in harness, and step throughput is not file size. These points apply to any model choice for agents. → *Use the 'tool-call reliability count' and 'agent steps per minute' checks as a standard model-selection step for cheap-model pipelines, such as the Haiku extraction pipeline.*
- **agentos** (1/3): AgentOS InferCraft targets vLLM on one RTX 5090 and already has quantization on its roadmap (NVFP4). This video covers llama.cpp and Ollama on 12 to 16GB cards, which is a different serving path. Its tool-call measurement ideas could still apply to evals. → *Add a tool-call conformance check to the eval set (parse-failure rate, leaked tool-call text, strict vs lenient parser score) before choosing a quantized local model for InferCraft.*
