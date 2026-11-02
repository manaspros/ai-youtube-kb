# From 15% to 90% GPU Utilization: Fix the Data Pipeline, Not the Model

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `tNAV259UhCM` · [watch](https://youtu.be/tNAV259UhCM) · **date:** 2026-10-10 · **length:** 17:02 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** ?
- **topics:** data-engineering, training-finetuning-rl, infra-cost-scaling · **tags:** multimodal-sft, ray, ray-actors, data-loading, prefetching, zero-copy, object-store, gil, wait-time-ratio, megatron, qwen3-vl, s3, scheduling-spread, scaling-ablation

> Fixing a multimodal SFT data pipeline on Ray (concurrency, prefetch, zero-copy, scheduling) took GPU utilization from 15% to about 90%. The lesson: profile the data path, not the model.

## Summary
The speaker trains a Qwen3-VL-style model with SFT on multimodal chat data stored as JSONL with images in S3, and argues that GPUs starve because of data loading, transform, and transport, not because of the model. They define a "wait time ratio" (data prep plus transfer time over total pipeline time) and start from a serial baseline where fetching a 256-sample batch takes over 100 seconds against a 15 to 20 second train step, giving about 15% utilization. They fix bottlenecks one at a time: async IO for S3 fetches with Ray actors for CPU preprocessing, a background prefetch queue that stays ahead of the trainer, and Ray object references so tensors are not pickled and copied through the coordinator. The wait ratio drops from 85% to about 20% after these three changes. When they scale to 4x data-parallel ranks, co-located workers saturate a node's NIC, and enabling zero-copy retrieval together with spread scheduling gives about 50% more throughput at scale even though neither flag helped at small scale. The main takeaway is to match the fix to the bottleneck, profile the baseline, and ablate across the scaling ladder because the best config changes with scale.

## Key ideas
- **Measure a wait time ratio: time spent on data prep and transfer divided by total pipeline time. Use it to see whether the trainer is blocked on data.** — The baseline spends about 85% of its time waiting on data. Multimodal training is CPU-heavy (image load, resize, normalize, tokenize), and clusters usually have more CPUs than GPUs, yet the GPU is the one starving. ([2:33](https://youtu.be/tNAV259UhCM?t=153))
- **The serial baseline is the bottleneck. Fetching one batch takes far longer than the train step.** — For a batch of 256 the fetch takes over 100 seconds, while the train step takes 15 to 20 seconds. Images are fetched and processed one by one, and profiling shows most time in S3 loads with a smaller tail in PIL image loading. ([5:24](https://youtu.be/tNAV259UhCM?t=324))
- **Match the concurrency model to the bottleneck. Use async IO for network fetches and processes or Ray actors for CPU-bound preprocessing.** — Samples are independent, so the work is embarrassingly parallel. Threads only help if the operation releases the GIL, and the speaker warns that which operations do this is not obvious. The speaker picked async IO for S3 fetches and Ray actors for processing, and reports about 40 seconds of fetch per batch and a 25% speedup. ([6:46](https://youtu.be/tNAV259UhCM?t=406))
- **Prefetching with a background producer that stays ahead of the consumer removes data wait, but it adds checkpointing and cold-start complexity.** — A background thread fills a queue so the trainer always finds data ready. Data fetch time per batch drops to close to zero. Costs: the model and data loader must resume cleanly from checkpoints, and the queue needs a cold-start period to fill. ([8:06](https://youtu.be/tNAV259UhCM?t=486))
- **Default object return copies large arrays between processes several times per sample. Pass references to a shared object store instead.** — Each sample is pickled on the worker, copied to the coordinator, and re-pickled to the trainer. Multimodal tensors are megabytes per sample, which can cause OOM on the data generator. With Ray's object store, samples carry references, the driver holds only pointers, and the DP ranks fetch data directly. ([9:31](https://youtu.be/tNAV259UhCM?t=571))
- **Scale can flip which configuration is best. Test at the target scale, not only on small runs.** — At 4x DP ranks and 200 data streams, co-located workers saturate the NIC of one node. Spread scheduling plus zero-copy retrieval are each neutral at small scale, but together they add about 50% throughput at large scale. ([13:24](https://youtu.be/tNAV259UhCM?t=804))
- **Profile the baseline first, and expect the bottleneck to move after each fix.** — The speaker's sequence was throughput, then wait time, then memory, then retrieval cost. The advice is to ask whether the job is CPU-bound or GPU-bound and IO-bound or compute-bound before applying any standard fix. ([14:47](https://youtu.be/tNAV259UhCM?t=887))

## Techniques
- **Wait time ratio as the pipeline health metric** — Compute (data fetch + preprocess + host-to-device transfer time) / (total step time) per step. Track it over time to see the sawtooth pattern from the trainer waiting on data. *When:* Before tuning a training job, to tell whether the GPU is blocked on data or on compute.
- **Async IO for object-store fetches, process pool for CPU preprocessing** — Fetch a whole batch of images from S3 concurrently with asyncio, and run decode, resize, normalize, and tokenize in Ray actors so the work spreads across cores. *When:* The bottleneck is network IO on the fetch side plus CPU work on the transform side, and samples are independent.
- **Background prefetch queue** — A producer thread or process fills a bounded queue ahead of the consumer (trainer), so requests are served from memory. Plan for checkpointing the queue state and a cold-start fill. *When:* Data fetch and transform latency is large but steady, and the consumer requests data in a predictable order.
- **Pass object references instead of data** — Use Ray's object store: samples carry an ObjectRef, the coordinator only holds pointers, and consumers fetch tensors directly from the store. This avoids pickling and re-copying megabyte-scale arrays. *When:* Samples are large (images, audio, video tensors) and pass through several process boundaries.
- **Spread scheduling and zero-copy retrieval at scale** — Set Ray to spread workers across nodes instead of co-locating them, and enable zero-copy retrieval. Together they spread NIC load and avoid copies. *When:* Worker count and data throughput grow past one node's network bandwidth. Validate on a large-scale run, because small-scale tests may show no gain.
- **Scaling-ladder ablation** — Run each configuration option at several scale points, not only the smallest, and pick the best at the target scale. *When:* A config change looks neutral or negative in a small test, but the production run is much larger.

## Numbers
- GPU utilization goes from about 15% in the serial baseline to about 90% after all optimizations (headline claim). ([0:08](https://youtu.be/tNAV259UhCM?t=8))
- Baseline spends about 85% of its time waiting on data acquisition; after the optimizations, under 10%. ([2:33](https://youtu.be/tNAV259UhCM?t=153))
- Baseline train step is about 15 to 20 seconds, but fetching data for a batch of 256 takes over 100 seconds. ([5:24](https://youtu.be/tNAV259UhCM?t=324))
- Concurrent fetch and processing with a worker pool brings fetch time to about 40 seconds per batch, a 25% speedup. ([8:06](https://youtu.be/tNAV259UhCM?t=486))
- Prefetching brings data fetch and processing per batch to close to zero seconds. ([9:31](https://youtu.be/tNAV259UhCM?t=571))
- Multimodal tensors are megabytes per sample, and each sample is copied across processes multiple times. ([10:56](https://youtu.be/tNAV259UhCM?t=656))
- After concurrency, prefetching, and the object store, the wait time ratio falls from 85% to about 20%. ([11:58](https://youtu.be/tNAV259UhCM?t=718))
- Production scale-up: 4x data-parallel ranks, 200 data streams, and 4x batch size. ([11:58](https://youtu.be/tNAV259UhCM?t=718))
- Zero-copy retrieval plus spread scheduling together give about 50% additional throughput at scale. ([14:47](https://youtu.be/tNAV259UhCM?t=887))

## Hot takes
- The hardest part of optimizing multimodal throughput is not kernel optimization. It is keeping GPUs constantly fed with data.
- GPUs are expensive, but the biggest battles often happen outside the GPU.
- Scale always changes the answer. A config that looks neutral at small scale can be the best one at large scale.
- Classic moves like parallelism and prefetching are not the end. The framework semantics and constraints matter as much.

## Tools mentioned
Ray, Ray actors, Ray object store, Megatron, Qwen3-VL (auto-caption reads as "QN3VL"), PIL, NumPy, Hugging Face Transformers tokenizers, pandas, S3, JSONL, asyncio

## Relevance to our work
- **agentos** (1/3): The talk is about data-path bottlenecks for training, not serving. The only overlap is the Ray-based batch ingest pattern and the wait-time framing. AgentOS InferCraft runs vLLM and Ray Serve on one GPU, and its serving path is not what this talk covers. → *If a batch job on Ray is ever added (for example, MemoryMesh ingest or a large RAGAS eval over documents), first measure fetch vs compute time with a wait-time ratio before changing parallelism. Do not change InferCraft serving from this talk.*
- **general** (1/3): The profiling-first method (classify as CPU- or IO-bound, measure wait ratio, ablate at target scale) applies to any batch job that feeds a model, including the LLM-based data-quality work in the recurring interests. → *For the next LLM-over-data job (such as the entity-resolution pipeline), log per-stage wait time before tuning concurrency or batch size, and re-test any flag at the production data size.*
