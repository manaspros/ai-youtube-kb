# Your LLM Stack Is a 2008 Database With Better Marketing — Lovina Dmello, NVIDIA

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `XjI-AR4pt7Y` · [watch](https://youtu.be/XjI-AR4pt7Y) · **date:** 2026-08-18 · **length:** 20:36 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Lovina Dmello · **orgs:** NVIDIA, Ray, NIST
- **topics:** security-guardrails, infra-cost-scaling, governance-compliance · **tags:** ml-security, misconfiguration, least-privilege, multi-tenant-gpu, prompt-injection, rag-poisoning, supply-chain, maturity-model, defense-in-depth, secrets-management

> Production ML breaches are mostly boring misconfigurations, not AI attacks; the talk argues for layered infra security, a maturity model, and budgeting guardrails by latency overhead tier.

## Summary
Lovina Dmello (NVIDIA, deep learning infrastructure) argues that most production ML and LLM security failures are old infrastructure mistakes, such as auth switched off by default, over-privileged accounts, flat networks, and secrets or model weights in reachable storage. She says ML broke three assumptions from the 2008 era: behavior is probabilistic, weights are copyable, and shared multi-tenant GPUs add cross-tenant risk. She cites a 2023 Ray exposure and an audit of 50 production ML setups where 78% had at least one critical misconfiguration. She frames defense as four layers (infrastructure, access control, runtime monitoring, and practice/compliance) and sorts controls by latency overhead, with cheap checks everywhere and expensive ones only for sensitive workloads. She offers a maturity model mapped to NIST AI RMF, and says most teams think they are at level 3 but are often at level 1 or 2. She closes with four forward-looking threats (prompt injection, RAG poisoning, GPU side channels, supply chain) and says the field has enough defenses but needs deployable ones.

## Key ideas
- **Most production ML breaches come from basic infrastructure mistakes, not exotic adversarial attacks.** — Her example is 2023 Ray clusters found open on the internet, with dashboards and job APIs reachable because auth was off by default. She says the exposure was over a billion dollars, and stresses that no zero-day was needed. ([0:08](https://youtu.be/XjI-AR4pt7Y?t=8))
- **ML broke three assumptions that classic security was built on.** — Classic apps were deterministic, single-tenant, and had fixed parameters. ML makes behavior probabilistic (correct is a distribution), makes weights copyable, and packs tenants onto shared GPUs. Prompts become control flow and agents take actions, yet security assumptions were not updated. ([4:02](https://youtu.be/XjI-AR4pt7Y?t=242))
- **Defense is four stacked layers, and a weak lower layer undoes the ones above it.** — Infrastructure (containers, networks, GPU virtualization, encryption) is the base, then access control, then runtime monitoring of live traffic, and practice/compliance/culture on top. Perfect access policy is decoration if the cluster underneath is open. ([5:25](https://youtu.be/XjI-AR4pt7Y?t=325))
- **Misconfiguration, not a missing feature, is the top failure mode.** — Her cited audit of 50 production ML setups found at least one critical mistake in 78%. The recurring problems were overly broad permissions, no separation between system parts, and passwords or trained models in storage anyone could reach. Security teams build the controls, but ML teams often do not configure them. ([8:08](https://youtu.be/XjI-AR4pt7Y?t=488))
- **Controls have a latency cost, so budget them by tier.** — She puts basic controls (logins, input checks, cost limits) under about 8% overhead and says they should always run. Heavier workload isolation costs 10-20% and is used selectively. Real-time malicious-input detection costs about 15-30% and depends heavily on how well it is built. ([10:25](https://youtu.be/XjI-AR4pt7Y?t=625))
- **Map your real maturity against NIST AI RMF with an overhead budget per level.** — Level 1 (under 5% overhead) is fine for test only. Level 2 (5-10%) is the production baseline: proper logins, encryption, network separation, basic monitoring. Level 3 adds controls that regulated industries need. Most teams overestimate their level. ([14:18](https://youtu.be/XjI-AR4pt7Y?t=858))
- **Three misconfigurations cause most of the risk, and each has a simple fix.** — Default full-admin accounts and non-expiring credentials: use least privilege and short expiry. Flat networks: wall off parts of the system and require verified service identity, not just network reach. Hard-coded secrets and model files in open storage: use a secret manager, encryption, and automatic scanning. ([15:14](https://youtu.be/XjI-AR4pt7Y?t=914))
- **Four threats she expects to matter most next.** — Prompt injection (the model cannot reliably separate instructions from input), RAG poisoning (a tainted document store poisons every answer), GPU side channels between tenants on shared hardware, and supply chain risk from unvetted public models and add-ons. She calls these a direction, not settled guidance. ([17:40](https://youtu.be/XjI-AR4pt7Y?t=1060))

## Techniques
- **Tiered guardrail budget** — Run cheap controls (auth, input validation, cost limits) on every request. Apply heavier isolation to sensitive or untrusted workloads only. Put expensive real-time malicious-input scanning on the highest-risk paths, after measuring its overhead. *When:* When deciding which security checks go on the request path and how much latency you can spend on them.
- **Maturity self-assessment with overhead budgets** — Score the current setup against levels that each carry an overhead ceiling and a control list (for example level 1 under 5%, level 2 at 5-10%, level 3 for regulated needs). Map each level to NIST AI RMF categories. Be honest about where you are, not where you aim to be. *When:* Before a production launch or a compliance review, to find the real gap and pick the next fix.
- **Least privilege with short-lived credentials** — Give each account only the permissions its task needs. Set credential expiry short enough that a leaked key goes stale quickly. Check for non-expiring credentials and default admin roles. *When:* When auditing service accounts, CI credentials, or any default-config deployment.
- **Segment by service identity, not network location** — Split the system into walled parts so one compromised part does not reach all others. Require a verified identity on each service-to-service call, instead of trusting anything on the internal network. *When:* When many services or tenants share one network or cluster.
- **Secrets and model artifacts hygiene** — Keep passwords out of code and load them from a secret manager. Encrypt model weights at rest. Scan repos and storage buckets automatically for exposed secrets or model files before release. *When:* In CI pipelines and for any bucket or registry that holds weights or keys.
- **Treat ML infra like a database** — Apply the usual database discipline: lock down who can access what, segment the network, and protect data at rest. She argues this covers most of the real breach surface. *When:* When planning the security baseline for a new LLM serving stack.

## Numbers
- 2023 Ray exposure: thousands of clusters open on the internet; the speaker puts the exposure at over a billion dollars (her figure, not verified). ([1:30](https://youtu.be/XjI-AR4pt7Y?t=90))
- Audit of 50 real production ML setups: 78% had at least one critical security mistake. ([8:08](https://youtu.be/XjI-AR4pt7Y?t=488))
- Basic controls (logins, input checks, cost limits) cost under about 8% overhead. ([10:25](https://youtu.be/XjI-AR4pt7Y?t=625))
- Workload isolation between tenants costs about 10-20% overhead; use selectively. ([10:25](https://youtu.be/XjI-AR4pt7Y?t=625))
- Real-time malicious-input detection costs about 15-30% overhead, depending on implementation quality. ([11:37](https://youtu.be/XjI-AR4pt7Y?t=697))
- Maturity levels: level 1 under 5% overhead (test only); level 2 at 5-10% (production baseline); level 3 for regulated industries. ([14:18](https://youtu.be/XjI-AR4pt7Y?t=858))

## Hot takes
- Most ML breaches that make the news are misconfigurations (an exposed key, an over-privileged account, a model in a public bucket), not adversarial attacks.
- Most teams think they are at maturity level 3, but they are actually at level 1 or 2.
- The field has enough defenses already; the frontier is making existing controls run in production within an overhead budget.
- A model cannot reliably tell its instructions from user input, so prompt injection can hijack the whole system.
- Research studies one model in isolation, while production runs many models on shared infrastructure.

## Tools mentioned
Ray, NIST AI RMF

## Relevance to our work
- **agentos** (2/3): AgentOS already has PII and prompt-injection scanning in the Rust proxy and runs several services on one GPU. The talk's overhead tiers and multi-tenant GPU risks apply directly to those choices. → *Measure per-pillar latency overhead in the Govrix proxy against the talk's tiers (basics under 8%, heavy isolation 10-20%, malicious-input scan 15-30%). Keep cheap checks always on and gate the expensive scan per tenant or manifest toggle.*
- **prosharness** (1/3): ProsHarness handles approval flows and credentials around the Claude Code CLI. The talk's point on non-expiring credentials and least privilege bears on that. → *Check that ProsHarness credentials and approval tokens have an expiry and scope only what the run needs.*
