# Why AI Agents Need Million-Token Context — Thomas Wolf & Olive Song, MiniMax

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `5Cxe5dv2Xlw` · [watch](https://youtu.be/5Cxe5dv2Xlw) · **date:** 2026-09-18 · **length:** 20:48 · **format:** interview · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Thomas Wolf, Olive Song · **orgs:** Hugging Face, MiniMax
- **topics:** models-research, inference-serving, context-engineering · **tags:** long-context, sparse-attention, native-multimodal, open-weights, research-harness, MiniMax-M3, interleaved-data

> MiniMax's Olive Song and Hugging Face's Thomas Wolf on how M3 reaches 1M-token context with sparse attention and native multimodal pretraining, and why agents need that context for multi-round tool use.

## Summary
Thomas Wolf (Hugging Face) interviews Olive Song (MiniMax) about the M3 open model, which she describes as about 400B total parameters with about 20B active (later given as 428B/23B), a 1M-token context window, and image and video understanding. The main argument is that agents need long context because each tool call and response adds to the working context across many rounds, and earlier MiniMax models (M1/01) had very long context but were not agentic. The long context comes from MiniMax Sparse Attention, which uses an index branch to pick important blocks and a sparse branch that computes attention only over those blocks. Multimodality is trained from the first pretraining step on interleaved image and video data, because adding vision adapters after text pretraining hurt text performance and did not scale. MiniMax's research process lets anyone propose a project, with interns contributing real architecture work that can ship into final training. The team also says its own research harnesses automate kernel optimization and synthetic data generation, and that M3 is helping build the next version. The talk is candid and technical in places but light on benchmarks, and several numbers are self-reported.

## Key ideas
- **Agents need long context because tool responses and multiple rounds pile up in the window** — Earlier MiniMax models handled up to 10M tokens but were not agentic (e.g., dumping a book and reviewing it). Once an agent gets tool outputs over many rounds, short context is not enough, so M3 targets a 1M-token window. ([4:09](https://youtu.be/5Cxe5dv2Xlw?t=249))
- **MiniMax Sparse Attention: pick blocks with an index branch, then attend only to them** — The index branch scores the context at a coarse level to pick what matters. A sparse branch then computes attention only over the selected blocks. The design is meant to scale context length and later model size together. ([4:09](https://youtu.be/5Cxe5dv2Xlw?t=249))
- **Attention efficiency is being revisited from first principles** — Speaker notes that linear attention work faded after FlashAttention arrived, and the field is returning to asking what attention needs to do and how to make it cheaper. ([5:37](https://youtu.be/5Cxe5dv2Xlw?t=337))
- **Native multimodal pretraining from step one instead of adding vision after text** — Adapters added after text pretraining hurt text performance and gave weak vision convergence, and results were recipe-sensitive so they did not scale. Training vision from the start needed ViT work, interleaved image and video data kept in the sequence, data cleaning and masking, and reward modeling to avoid collapse. ([10:26](https://youtu.be/5Cxe5dv2Xlw?t=626))
- **Open research process where anyone can propose and ship a project** — After each release, team members pick weaknesses from their own evals, propose fixes, and work on them for weeks or months. Accepted work goes into the final training run. Architecture work can take longer, including redoing pretraining evals. The sparse attention design came from an intern. ([8:06](https://youtu.be/5Cxe5dv2Xlw?t=486))
- **Multimodal agents could read messy documents and act on long video** — Speaker suggests use cases such as reading PowerPoint decks or unstructured reports, understanding long videos, and then calling tools on what was seen. Says multimodal agent use is underexplored in coding agents. ([18:05](https://youtu.be/5Cxe5dv2Xlw?t=1085))
- **Internal research harnesses automate much of MiniMax's own work** — The team builds its own harnesses for research workflows, including kernel optimization, automated data building, and pulling in other models. Speaker says M3 is being used to help build M3.1. ([19:24](https://youtu.be/5Cxe5dv2Xlw?t=1164))

## Techniques
- **Index-then-sparse attention over context blocks** — A cheap index branch scores blocks of the context and selects the important ones. A sparse attention branch then computes attention only over those blocks, which keeps cost low as context grows toward 1M tokens. *When:* When you need very long context in an agent loop and full attention is too costly.
- **Train vision from the first pretraining step with interleaved data** — Keep images and video inline with text in the training sequence instead of masking them out. Pair this with ViT work, cleaning and masking of the data, and reward modeling to prevent collapse. *When:* When you want a model to handle text and vision together without vision hurting text quality, and you want results that scale to larger models.
- **Open project intake for research** — Give everyone access to the model and infrastructure. After a release, people run their own evals, find weaknesses, and propose projects; other interested people join. Good results are folded into the next training run. *When:* When you want many contributors, including interns, to ship model improvements, with a clear path from proposal to training.
- **Research harness for automating model-lab workflows** — Build internal harnesses that run repeatable research tasks such as kernel optimization and auto data generation, and use the current model to speed up those harnesses. *When:* When routine research steps are repetitive and the model is capable enough to run long, multi-step tasks.

## Numbers
- M3 offers a 1 million token context window ([2:46](https://youtu.be/5Cxe5dv2Xlw?t=166))
- M3 described as about 400B total parameters and 20B active; later given as 428B total and 23B active ([2:46](https://youtu.be/5Cxe5dv2Xlw?t=166))
- Earlier MiniMax M1/01 supported 10M-token context (not agentic) ([4:09](https://youtu.be/5Cxe5dv2Xlw?t=249))
- Apps reach more than 300M people in about 200 countries and over 1M companies (speaker's claim) ([14:33](https://youtu.be/5Cxe5dv2Xlw?t=873))
- Plans to go past 1 trillion parameters in future models ([11:49](https://youtu.be/5Cxe5dv2Xlw?t=709))

## Hot takes
- Long context matters for agents mainly because tool outputs accumulate over many rounds, not for dumping books.
- Adding vision after text pretraining hurts text performance; multimodal training should start at step one.
- Interns can design core architecture (the sparse attention came from one) if they have access to the work.

## Tools mentioned
MiniMax Sparse Attention (MSA), Hugging Face model card

## Relevance to our work
- **general** (2/3): Strong fit with context-engineering and agent-evals interests: it argues agents need long, multi-round context and shows how a lab uses its own harness to automate research. → *Add a note on how long-context needs for agents change compaction or retrieval design, and compare with the MemoryMesh retrieval approach.*
- **agentos** (1/3): Sparse block selection over long context is a model-side idea; InferCraft already plans KV-cache strategies (H2O, CPU offload) on the single 5090, so this is a useful comparison point, not a direct change. → *Read the MiniMax Sparse Attention description and compare its block selection with the H2O KV-eviction strategy planned for InferCraft.*
- **prosharness** (1/3): The claim that multi-round tool outputs push context past short windows is relevant to long-run checkpointing and context limits in the Claude Code harness. → *Check whether ProsHarness checkpoint/resume thresholds account for context growth across tool rounds in long runs.*
