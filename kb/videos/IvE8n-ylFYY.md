# Privacy-Preserving Intelligence — Steve Korshakov, Bee (acq. Amazon)

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `IvE8n-ylFYY` · [watch](https://youtu.be/IvE8n-ylFYY) · **date:** 2026-08-18 · **length:** 15:53 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Steve Korshakov · **orgs:** Bee, Amazon
- **topics:** security-guardrails, sandboxing-execution, governance-compliance, agent-architecture · **tags:** privacy, end-to-end-encryption, attestation, transparency-log, confidential-compute, wearable, personal-agent, key-management, sandboxing, stateful-runtime, private-ca, release-engineering

> Steve Korshakov (Bee, acquired by Amazon) explains how an always-on personal-agent wearable keeps data unreadable even to its own company, using client-held keys, attested workloads, and two-tier release controls.

## Summary
The speaker describes Bee, an AI wearable that records everything the user says and builds a personal agent from it, roughly 10 million tokens per person per year. Because that data is so sensitive, the team designed the system so that not even Amazon staff can read it. The keys are generated on the user's phone and never stored elsewhere, and a backend releases them only after an attestation pipeline checks the workload against a public transparency log. Keys expire after seven days, a horizon chosen as the realistic time frame for useful work. Releases are split into a slow, heavily signed base image and a faster deployment manifest, all recorded in the log so outside auditors can trace any deployed image. The speaker also argues that agents should run continuously rather than on request/response, and that sandboxing with minimal capabilities is the only real safety lever. The Q&A adds that the core code is small (about 20k lines of memory-safe language) and that they avoided inventing their own cryptography. The talk is more architecture overview than benchmark, and several details (such as the attestation math) were deferred to later publication.

## Key ideas
- **Always-on personal agents need a stateful runtime, not request/response** — The speaker says request/response backends are not enough once agents run for hours or days; they built a stateful runtime with persistent memory that runs without the user's device being online, while staying under user control. ([2:36](https://youtu.be/IvE8n-ylFYY?t=156))
- **Keys are born and stay on the customer device** — The encryption key is created on the phone and never persisted by the company. Encryption has no opt-out or bypass. Internal-threat protection is handled through transparent auditing of all workloads and by minimizing what must be trusted. ([3:33](https://youtu.be/IvE8n-ylFYY?t=213))
- **Attestation gates key release** — Before the backend gets the key, the phone runs an attestation pipeline that checks the workload's integrity and that it appears in a public transparency log. The key is then replicated only to confidential-compute nodes that have passed the same check. ([4:34](https://youtu.be/IvE8n-ylFYY?t=274))
- **Time-boxed keys** — Keys held in memory expire after seven days. The speaker says 24 hours would drop data when a user simply does not open the phone for a day, so seven days was picked as the useful horizon. ([5:34](https://youtu.be/IvE8n-ylFYY?t=334))
- **Two-tier release to prevent unnoticed shipping** — A separate privacy/transparency team controls the signing keys, which are hard-coded into client apps and backends, so the product team can influence but not control releases. The base image and the per-deploy manifest are split so that the slow, multi-sign-off part happens rarely, while every deployed manifest is logged. ([6:55](https://youtu.be/IvE8n-ylFYY?t=415))
- **Auditability through full image history and a private CA** — Every image and manifest ever deployed can be given to outside audit firms. A private CA issues the certificates that embed the attestation and transparency proofs, because a public CA would write them into the public log. ([8:21](https://youtu.be/IvE8n-ylFYY?t=501))
- **Keep the trusted code small and reuse common software** — They avoided building their own crypto and reused popular, well-known software wherever possible. Their own code is about 20k lines in a memory-safe language, which made it small enough to audit. Amazon's internal-threat model was the biggest change after acquisition. ([11:21](https://youtu.be/IvE8n-ylFYY?t=681))
- **Sandboxing is the real safety control for agents** — In the Q&A, the speaker argues that the only dependable approach is to limit what agents can do and sandbox them, rather than trying to make them behave. He says tightening a popular agent's permissions made it much less useful, and that the sandbox should be per agent. ([14:41](https://youtu.be/IvE8n-ylFYY?t=881))

## Techniques
- **Client-held keys with attested key release** — Generate the key on the user's device and never persist it server-side. Release it to the backend only after the workload passes attestation and is shown to be in a public transparency log. Replicate the key only to nodes that have passed the same check. *When:* Any product that stores sensitive personal data and must stay unreadable to its own operator, including internal staff.
- **Forced key expiry window** — Put a hard expiry on any in-memory key, for example seven days, picked so that the window covers the longest realistic gap in user activity without creating data loss. *When:* Long-lived sessions where keys sit in memory for long stretches and you want to limit exposure to a compromised node.
- **Split base image and deployment manifest** — Build and heavily sign a base image slowly, under many sign-offs. For each deploy, publish only a manifest that references that base image to the transparency log. This keeps the frequent path fast while the trusted base stays tightly controlled. *When:* Confidential or audited systems where releases must be provable and traceable but still need to ship often.
- **Private CA for internal attestation certificates** — Issue certificates that embed the attestation documents and transparency proofs from a private CA, so the certificates do not appear in a public log. *When:* Internal attestation flows where public certificate issuance would leak metadata.
- **Minimal, auditable trusted code base** — Keep the self-written trusted code small, in a memory-safe language, and reuse well-known libraries for everything else. Avoid writing custom cryptography. *When:* Security-critical components that an outside auditor must be able to review.
- **Per-agent sandbox with minimal capabilities** — Deploy each agent in a sandbox that allows only the tools and actions it needs. Anything outside that scope should fail by default rather than be blocked after the fact. *When:* Running agents that act on a user's behalf or have access to personal data.

## Numbers
- A single person generates about 10 million tokens of captured data per year ([0:08](https://youtu.be/IvE8n-ylFYY?t=8))
- Almost everything sensitive about a person can be learned from about one week of recording ([1:11](https://youtu.be/IvE8n-ylFYY?t=71))
- Keys in memory are forcibly expired after 7 days; 24 hours was judged too short ([5:34](https://youtu.be/IvE8n-ylFYY?t=334))
- Company acquired by Amazon about 8 months before the talk ([0:08](https://youtu.be/IvE8n-ylFYY?t=8))
- Own trusted code is about 20k lines in a memory-safe language ([11:21](https://youtu.be/IvE8n-ylFYY?t=681))

## Hot takes
- Nothing works to control AI agents except sandboxing and not giving them a way to hurt themselves.
- Personal agents will move from request/response to continuous operation, as coding agents already have.
- Strong encryption can coexist with a large company only if the company itself cannot change the release path alone.
- Tightening agent permissions makes the agent much less useful, which the speaker sees as a sign that some approaches are not good.

## Tools mentioned
Sigstore-style transparency log (auto-caption reads as 'six store'), Confidential compute nodes, Private certificate authority, OpenClaw (auto-caption reads as 'open claw'), Claude Code (auto-caption reads as 'cloud code')

## Relevance to our work
- **agentos** (1/3): Persistent, always-on personal agent with sensitive data needs the same key and sandbox ideas that AgentOS's memory and sandbox layers would need. → *Read the talk's key-custody model (client-held key, 7-day expiry) and check whether MemoryMesh's stored personal memory could use client-side encryption with a forced key expiry.*
- **prosharness** (1/3): ProsHarness runs long checkpointed agent jobs and handles credentials, which matches the talk's concern about continuous agents holding keys. → *Check whether any credential or key cached across ProsHarness checkpoints has an enforced expiry, and consider a fixed expiry window like the talk's 7 days.*
- **general** (1/3): Talk's central safety argument, that minimal per-agent capabilities beat behavioral controls, applies to any agent harness. → *Adopt a deny-by-default capability list per agent role in the harness and compare it with the current allowlist approach.*
