# The Half Life of Agent Infrastructure — Ben Kus, Box

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `sM1iYgz93HI` · [watch](https://youtu.be/sM1iYgz93HI) · **date:** 2026-09-18 · **length:** 19:26 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Ben Kus · **orgs:** Box, IBM
- **topics:** agent-architecture, evals, enterprise-adoption, rag-retrieval · **tags:** agent infrastructure, change management, half-life of technology, eval-gated switching, abstraction layers, adaptive model selection, agentic search, hybrid search, skills, sandboxes, bring your own harness, enterprise AI, vendor selection

> Box CTO Ben Kus argues AI agent infrastructure has a half-life of months, not years, so teams should build abstractions, gate changes on eval sets, and get good at changing.

## Summary
Ben Kus, CTO of Box, argues that the usual enterprise advice of picking one stack and going deep no longer holds for AI agent infrastructure. He walks through how agent design has shifted from single-shot calls to graphs, then to plan-driven agents with skills and sandboxes, and says the approach he would pick today will likely change again. Classic infrastructure like databases or identity has a half-life of three to five years, while AI infrastructure may have one measured in months. His advice is to prepare teams for change, build abstractions so the layer underneath can be swapped without changing customer behavior, and switch only when an eval set shows the new approach is better. He also recommends relying on vendors with a track record of reinventing themselves, and Box now reviews its stack every six months. The talk is mostly leadership and strategy, with few concrete benchmarks or implementation details.

## Key ideas
- **Standard advice to pick one technology and go deep is weaker now because the rate of change is much higher.** — Speaker says the usual approach (choose a stack, master it, optimize it) worked through past shifts but breaks when most of the AI stack changes every few months. ([2:44](https://youtu.be/sM1iYgz93HI?t=164))
- **Agent design has moved through several approaches in a year, and last year's advice is already dated.** — He says his own prior talk recommended graph-based agent workflows, but a plan-driven generic agent with skills, sandboxes, or bring-your-own harness now looks better to him. ([4:10](https://youtu.be/sM1iYgz93HI?t=250))
- **His current pick is a stack, but he expects it to be replaced.** — Current picks: adaptive model selection across big and small models, an RLM-style agent, and agentic search over hybrid lexical and semantic retrieval. He says he would not bet long-term on any one of them. ([7:41](https://youtu.be/sM1iYgz93HI?t=461))
- **Infrastructure half-life is now measured in months.** — Databases, identity and multi-cloud storage keep a three-to-five-year life. AI components may need replacing a few months after adoption, which hurts engineers, startups and buyers with multi-year deals. ([11:17](https://youtu.be/sM1iYgz93HI?t=677))
- **Change is a leadership and morale problem, not only a technical one.** — At Box, an engineer rebuilt a feature on a new agent approach, then was asked to rebuild again two months later. Teams became skeptical, so people had to be prepared to expect change. ([12:39](https://youtu.be/sM1iYgz93HI?t=759))
- **Three practices make change manageable: prepare people, abstract the layer underneath, and review regularly.** — Box builds an abstraction so the agent behaves the same for customers while the internals can be swapped, and reviews its approach every six months. ([14:38](https://youtu.be/sM1iYgz93HI?t=878))
- **Switch only when evals show a real gain.** — Speaker says not to change just because a new paper or trend appears. Use fixed eval sets (same input, expected output, graded on cost, speed and quality) and switch only if the customer-relevant results improve. ([15:56](https://youtu.be/sM1iYgz93HI?t=956))
- **Choose vendors by how they handled past transitions, not only by today's features.** — He suggests checking a vendor's roadmap, but also how it handled change over the last year, since teams cannot track every new technique on their own. ([17:22](https://youtu.be/sM1iYgz93HI?t=1042))

## Techniques
- **Abstraction layer over agent internals** — Put a stable interface in front of the agent so the underlying approach (model, orchestration, search) can be swapped without changing customer-facing behavior. *When:* Any component of the agent stack that is likely to be replaced within months.
- **Eval-gated switching** — Keep fixed eval sets with the same inputs and expected outputs, grade candidate approaches on cost, speed, quality and capability, and switch only when the customer-relevant eval improves. *When:* Deciding whether a new model, pattern or paper is worth a migration.
- **Scheduled stack review** — Review the agent architecture on a fixed cadence (Box uses six months) instead of waiting for a crisis. *When:* Fast-moving AI infrastructure where a three-year plan is unrealistic.
- **Adaptive model selection** — Route each task to a big or small model based on which one performs well for it, instead of using one model everywhere. *When:* Mixed workloads with different cost and quality needs.
- **Hybrid lexical plus semantic retrieval with rank fusion** — Run keyword (BM25-style) and embedding search, then merge the ranked lists with rank fusion. He calls this the current best option, not a final one. *When:* Retrieval over large unstructured content where neither method is enough alone.
- **Agentic search** — Let the agent search and reason over data itself instead of relying on a fixed retrieval index. *When:* When the agent can apply its own reasoning to find documents, which he argues can beat fixed retrieval pipelines.

## Numbers
- Box holds over an exabyte of data, with tens of millions of users and hundreds of billions of content items. ([0:08](https://youtu.be/sM1iYgz93HI?t=8))
- Token usage is around a trillion tokens, and he expects about 10 trillion soon. ([1:25](https://youtu.be/sM1iYgz93HI?t=85))
- Classic infrastructure such as databases has a half-life of about three to five years, while AI infrastructure is measured in months. ([11:17](https://youtu.be/sM1iYgz93HI?t=677))
- Box reviews its agent architecture every six months, while other infrastructure is reviewed about every three years. ([14:38](https://youtu.be/sM1iYgz93HI?t=878))
- Trillions of dollars of investment are driving the pace of change. ([9:05](https://youtu.be/sM1iYgz93HI?t=545))
- A team shipped a product on one approach, then rebuilt it on a new approach about two months later. ([13:39](https://youtu.be/sM1iYgz93HI?t=819))

## Hot takes
- The company that will dominate tomorrow is being born today.
- Change is not a mistake; nobody knew six months ago and nobody will know six months from now.
- Adaptability is the moat until the technology changes again.
- Agents may be better at finding data themselves than any retrieval pipeline.
- The half-life of AI infrastructure is measured in months, not years.

## Tools mentioned
Claude, Opus, OpenAI and Anthropic frontier models, open-weight models, BM25, embeddings and approximate nearest neighbor search, MySQL

## Relevance to our work
- **general** (2/3): Strong, practical framing for AI infra decisions: abstraction boundaries, eval-gated change, and periodic review cadence are reusable across projects. → *Write a short review checklist for AI infra changes: abstraction seam, eval set result, vendor track record, and next review date.*
- **agentos** (1/3): AgentOS L1 already has strategy routing across models; the talk's point about adaptive model selection and eval-gated switching is a useful framing but only one data point. → *Add a per-task model-selection eval to the routing strategy and gate any routing-policy change on the same eval set.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, and the talk's advice to abstract the underlying harness and keep an eval set to justify switches applies directly. → *Define a harness interface in ProsHarness and keep a small fixed eval set for the plan, critique and resume flows before switching any of them.*
