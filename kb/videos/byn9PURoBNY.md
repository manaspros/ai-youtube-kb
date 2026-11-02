# Infra behind Krea 2: How to train and serve at scale — Gabriel Jorge Menezes, Krea.ai

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `byn9PURoBNY` · [watch](https://youtu.be/byn9PURoBNY) · **date:** 2026-09-18 · **length:** 16:55 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Gabriel Jorge Menezes · **orgs:** Krea.ai
- **topics:** infra-cost-scaling, training-finetuning-rl, inference-serving · **tags:** diffusion-transformer, pre-training, gpu-cluster, kubernetes, checkpointing, infiniband, gang-scheduling, virtual-kubelet, preemption, gpu-bursting, open-source-model, krea

> Krea's infra engineer on training the from-scratch Krea 2 diffusion transformer at scale: which metrics matter, why to let crashing runs restart, frequent checkpoints, and bursting training and inference across clusters and rented GPUs.

## Summary
Gabriel Menezes from Krea.ai describes the infrastructure used to train Krea 2, a diffusion transformer built from scratch and released as an open-source model with a raw pre-train checkpoint and a fast turbo post-trained version. At scale (128 to 512+ GPUs), runs failed often and often silently, and his team found it cheaper to let jobs crash and restart on the same machines than to swap nodes. The main lesson is to invest heavily in metrics: he recommends removing any GPU above about 78°C, not trusting GPU utilization, and exporting InfiniBand and NVLink error counters, since most failures were cross-node. Checkpointing every 20 to 30 minutes to a fast paid file system (Weka, rather than Ceph) kept checkpoint writes from stalling training. Scheduling uses a queue with two priority tiers in front of Kubernetes, so training can preempt inference on the shared cluster. When the cluster is full of training, Virtual Kubelet creates a fake node that forwards overflow pods to external GPU providers, with taints and a descheduler moving pods back gradually. The talk is an experience report from one company with no benchmarks against alternatives, and it ends with a hiring pitch.

## Key ideas
- **Krea 2 was trained from scratch and released open source** — Built for creative exploration rather than the usual polished AI look. Two checkpoints are public: a raw pre-train for others to post-train, and a turbo post-trained version that makes an image in under a second. ([0:14](https://youtu.be/byn9PURoBNY?t=14))
- **At scale, failures are frequent and often silent; let crashing runs restart** — Small experiments ran for days, but at 128 to 512+ GPUs runs crashed every 1 to 24 hours, often with healthy-looking metrics. The team stopped swapping nodes and let the same job restart on the same machines and data. ([3:02](https://youtu.be/byn9PURoBNY?t=182))
- **Metrics are the foundation, and some default ones mislead** — GPU utilization reads 100% even when the GPU is badly underused, so he tracks tensor core utilization instead. Any GPU above about 78°C is removed immediately, without trying to fix it. ([4:22](https://youtu.be/byn9PURoBNY?t=262))
- **Cross-node network metrics matter most** — Most failures were cross-node communication problems. DCGM does not export InfiniBand metrics by default, so the team built its own collection for fabric wait time, error types and packet counts. NVLink errors were also collected for single-node faults. ([5:45](https://youtu.be/byn9PURoBNY?t=345))
- **Frequent cheap checkpoints are the main recovery tool** — The team moved from Ceph, which they did not trust, to a paid high-throughput file system. It can write about a terabyte in under 30 seconds, so checkpointing every 20 to 30 minutes does not stall training. ([8:11](https://youtu.be/byn9PURoBNY?t=491))
- **Training is queued and can preempt inference on one shared cluster** — Researchers submit jobs without thinking about GPUs. A queue with two priority tiers sits in front of Kubernetes, and admitted training pods can evict inference pods. Queue quotas are set by hand and can drift as nodes come and go, which can break gang scheduling. ([8:11](https://youtu.be/byn9PURoBNY?t=491))
- **Virtual Kubelet bursts overflow pods to external GPU providers** — A fake Kubernetes node receives pod specs, picks a provider using a cost-based algorithm, translates the spec, deploys, and reconciles state on both sides. Failed remote pods are simply marked failed so Kubernetes creates a replacement. ([10:52](https://youtu.be/byn9PURoBNY?t=652))
- **Taints plus a slow descheduler move inference back safely** — A taint is added when the cluster has free GPUs and removed when training takes them. The descheduler migrates pods back gradually. A NoExecute taint would evict everything at once and take production down. ([15:02](https://youtu.be/byn9PURoBNY?t=902))

## Techniques
- **Let crashing jobs restart instead of debugging each crash** — Mark the pod failed and let Kubernetes create a replacement. Do not try to recover the failed node in place. Keep checkpoints frequent so each restart loses little work. *When:* Large multi-node training where crashes are frequent and the same hardware can often run again after a restart.
- **Hard GPU health gate on temperature** — Set a fixed temperature threshold (about 78°C) and remove any GPU above it right away. Ask the provider to replace it. *When:* Dense GPU clusters where one hot GPU slows the whole job or makes training unstable.
- **Checkpoint every 20 to 30 minutes to a high-throughput file system** — Write full checkpoints to a fast parallel file system so the write does not block training. Measure how long a full checkpoint takes. *When:* Long pre-training runs where losing progress after a crash is expensive.
- **Two-tier priority queue in front of Kubernetes** — A queue with explicit workload priority sits before the scheduler. Training is admitted first, and training pods can preempt inference pods on the shared cluster. Set queue quotas to match the real node pool. *When:* One cluster serving both production inference and large training jobs, where training should take priority on idle GPUs.
- **Overflow to external GPUs with a virtual node** — Use Virtual Kubelet to expose an external provider as a fake Kubernetes node. Translate the pod spec for the provider, deploy, reconcile status, and create a replacement when a remote pod fails. Add or remove taints based on free local GPUs, and use a descheduler to move pods back gradually. *When:* When local GPUs are often full and external rentals are cheaper or are needed as burst capacity.

## Numbers
- Krea 2 turbo returns an image in under a second ([1:38](https://youtu.be/byn9PURoBNY?t=98))
- Runs crashed after roughly 1 hour to 12 to 24 hours; the team saw shorter runs than an external paper's failure estimate, and runs were under 8 hours ([3:02](https://youtu.be/byn9PURoBNY?t=182))
- GPU removal threshold: any GPU above about 78°C is pulled ([4:22](https://youtu.be/byn9PURoBNY?t=262))
- Checkpoints about 1 TB every 20 to 30 minutes, written in under 30 seconds on the paid file system (captioned as 'almost a terabyte of writes' with garbled units; roughly 1.2 TB/s read) ([8:11](https://youtu.be/byn9PURoBNY?t=491))
- Training scaled through 128, 256 and 512 GPUs, one cluster on InfiniBand ([1:38](https://youtu.be/byn9PURoBNY?t=98))
- Tensor core utilization rises as image resolution scales from 128 to 1024 px across pre-training, mid-training and post-training ([5:45](https://youtu.be/byn9PURoBNY?t=345))

## Hot takes
- GPU utilization is a lie; track tensor core utilization instead.
- If you run large pre-training without InfiniBand metrics, you are doing something wrong.
- Don't swap nodes on every crash; let it crash, restart on the same set, and checkpoint often.
- Silent failures are the real cost; invest in metrics or you will go blind.

## Tools mentioned
Kubernetes, Virtual Kubelet, Kubernetes descheduler, Kubernetes taints and tolerations, Queue system (captioned as 'Q') for gang scheduling, Prometheus, NVIDIA DCGM, Weka (parallel file system), Ceph, InfiniBand, NVLink, Hugging Face, vLLM / Ray Serve (not mentioned)

## Relevance to our work
- **prosharness** (2/3): The talk's main recovery approach is cheap, frequent checkpoints and treating failure as normal. This matches ProsHarness's checkpoint/resume for long Claude Code runs and suggests making resume the default path. → *Set ProsHarness to write a checkpoint on each plan step and on a fixed short interval, and log crash-to-resume time as a metric to track the cost of failures.*
- **agentos** (1/3): InferCraft runs vLLM and Ray Serve on one 5090 with a 4-class priority scheduler and preemption. The talk's two-tier priority with training preempting inference is a close pattern, but the talk is about multi-node pre-training at much larger scale. → *Compare InferCraft's 4-class priority scheduler and preemption rules with the talk's queue-then-preempt model. Confirm that preempted inference requests are re-queued, not dropped.*
