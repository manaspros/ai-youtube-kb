# What Lies Beneath the API — Benjamin Cowen, Modal

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `HvZXAOZ3iv8` · [watch](https://youtu.be/HvZXAOZ3iv8) · **date:** 2026-06-18 · **length:** 12:40 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Benjamin Cowen · **orgs:** Modal, Intercom, Pinterest, Decagon
- **topics:** training-finetuning-rl, inference-serving, infra-cost-scaling · **tags:** fine-tuning, reinforcement-learning, serverless, sandboxes, rollouts, hyperparameter-sweep, vLLM, SGLang, Triton, inference-serving, domain-specific-models, sales-pitch

> Modal forward-deployed engineer argues that once a product is differentiated, fine-tuning becomes worth it, and that serverless compute and open-source libraries now make it accessible without a cluster team. Sales-leaning, with a few concrete signals and code-size claims.

## Summary
Benjamin Cowen, a forward-deployed ML engineer at Modal, argues that as AI products mature and specialize, more companies move from frontier APIs to fine-tuning for better cost, latency, throughput and task performance. He lists signals that it is time: API spend exceeding what customers pay you, plateaued evals, and latency or throughput limits that prompt engineering cannot fix. His main point is that teams with an agent harness and eval data already hold the raw material for RL training, so collecting that data is the real prerequisite. He says supervised fine-tuning and RL can each be done in roughly 300 lines of Python with open-source libraries on serverless platforms. Serverless also lets hyperparameter sweeps fan out to containers and stop unpromising runs early. RL rollouts are embarrassingly parallel, and he reports customers scaling to 50,000 to 100,000 sandboxes. For serving, he names vLLM, SGLang, Triton and custom Python, autoscaled to traffic. The talk is mostly a pitch for Modal, with little benchmark detail.

## Key ideas
- **Fine-tuning becomes worth it as a product specializes; the question is when the app crosses into needing a custom model.** — Frontier APIs allow only prompt-level customization. Latency, throughput and custom business metrics are hard to meet with them, so specialized companies move toward custom models. ([0:00](https://youtu.be/HvZXAOZ3iv8?t=0))
- **Signals that it is time to fine-tune.** — API spend is higher than what customers pay you, evals have plateaued, or enterprise contracts demand latency or throughput the API cannot provide. ([6:23](https://youtu.be/HvZXAOZ3iv8?t=383))
- **Collected product data is the training set; an agent harness already provides what RL needs.** — If you have built a product with evals and feedback on what works, you have training signal. Garbage data still means no training, so collect data and mature evals first. ([7:14](https://youtu.be/HvZXAOZ3iv8?t=434))
- **Supervised fine-tuning and RL are now short scripts, not infrastructure projects.** — He says each can be done in about 300 lines of Python using open-source libraries on a serverless platform, with no cluster team required. ([8:39](https://youtu.be/HvZXAOZ3iv8?t=519))
- **Serverless fan-out turns hyperparameter search into an early-stopping evolutionary search.** — Containers are launched on demand, and any run that looks unpromising is killed right away, so the cluster is no longer a fixed resource. ([8:39](https://youtu.be/HvZXAOZ3iv8?t=519))
- **RL rollouts are massively parallel and map well onto sandboxes.** — Each rollout is an independent evaluation, so the workload can run across very many sandboxes. He reports customers scaling to 50,000 to 100,000 sandboxes in the last quarter. ([9:55](https://youtu.be/HvZXAOZ3iv8?t=595))
- **Serving the custom model is also small code and can autoscale on serverless.** — vLLM, SGLang, Triton, or a plain Python inference workflow can be autoscaled to incoming traffic, which is what a frontier API does internally. ([10:54](https://youtu.be/HvZXAOZ3iv8?t=654))

## Techniques
- **Signal-based fine-tuning decision** — Check whether API cost per customer dollar, eval plateau, or latency/throughput limits are blocking growth. Fine-tune only once data and evals exist. *When:* Deciding whether to move from a frontier API to a custom model.
- **Harness outcomes as RL training data** — Log the agent harness's eval results and success or failure signals, and use them as the reward or training set for RL. *When:* You already run an agent product with evals and want a model that improves on your task.
- **Parallel hyperparameter sweep with early kill** — Launch many training containers on demand, score them as they run, and terminate the weak ones immediately. *When:* Tuning fine-tuning hyperparameters without a fixed training cluster.
- **Sandbox-fanned RL rollouts** — Run each RL rollout in its own sandbox so the evaluation work runs in parallel across a large number of sandboxes. *When:* RL training where rollouts are independent and CPU or sandbox-bound.
- **Autoscaled serving of custom models** — Serve the fine-tuned model with vLLM, SGLang, or Triton on serverless GPUs, scaled to incoming traffic. *When:* Replacing a frontier API endpoint with a custom model that has latency or cost targets.

## Numbers
- Intercom beats its Frontier API at one-fifth of the cost after fine-tuning (speaker's report of a customer result). ([3:37](https://youtu.be/HvZXAOZ3iv8?t=217))
- Pinterest reports gains of orders of magnitude; no exact figure is given. ([3:37](https://youtu.be/HvZXAOZ3iv8?t=217))
- Supervised fine-tuning can be written in about 300 lines of Python. ([8:39](https://youtu.be/HvZXAOZ3iv8?t=519))
- RL training can be written in about 300 lines of code. ([9:55](https://youtu.be/HvZXAOZ3iv8?t=595))
- Customers scaled RL to 50,000 to 100,000 sandboxes in the last quarter. ([9:55](https://youtu.be/HvZXAOZ3iv8?t=595))

## Hot takes
- It is just a matter of time until most products step into being domain-specific; a differentiated product is custom by nature.
- If you have built a product, you have at least touched everything needed to train a model.
- Frontier labs do not share your exact goal, so they will not optimize for your business logic.
- Teams no longer need infrastructure experts to fine-tune; open-source libraries plus serverless are enough.

## Tools mentioned
Modal, vLLM, SGLang, Triton Inference Server, Python

## Relevance to our work
- **general** (2/3): The talk's main point, that eval data and an agent harness are the prerequisites for fine-tuning, applies to the recurring interest in cheap Haiku-class pipelines and evals. → *Before any fine-tuning of a small model for a narrow task, first set up the eval set and log the labeled outcomes from current runs.*
- **agentos** (1/3): InferCraft already runs vLLM with Ray Serve; the talk offers a serverless alternative for serving custom models, but gives no benchmarks. → *Read the Modal serverless serving examples for vLLM to compare autoscaling against the Ray Serve setup, if fine-tuning enters the roadmap.*
- **prosharness** (1/3): Harness run outcomes (plan, critique verdicts, pass or fail) could become labeled data for a later model, though the talk gives no implementation detail. → *Consider logging ProsHarness run outcomes as a structured dataset. This is low priority and does not change current work.*
