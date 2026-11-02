# Your Agent Just Authorized What?! — Jay Mok & Ben Coumes, Paypal

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `vGn6N4-bxBY` · [watch](https://youtu.be/vGn6N4-bxBY) · **date:** 2026-09-18 · **length:** 16:07 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Jay Mok, Ben Coumes · **orgs:** PayPal, Gemini (Google), ChatGPT (OpenAI), Nevermind (partner, as transcribed), FIDO Alliance
- **topics:** security-guardrails, governance-compliance, enterprise-adoption · **tags:** agent-authorization, payments, mandates, verifiable-intent, selective-disclosure, stakes-matrix, oauth-scopes, audit-evidence, human-in-the-loop, reversibility

> PayPal's Jay Mok and Ben Coumes propose a stakes-and-counterparty matrix for deciding how much proof an agent's payment authorization needs, ending with verifiable mandates for high-stakes, open-ecosystem transactions.

## Summary
The talk frames agent authorization around three questions: did the human authorize this, is it allowed now within scope, and can it be proven later. The speakers argue the right answer depends on context, mainly stakes (low or high) and whether the ecosystem is open or closed. They walk through three tiers: Claude Code connectors and tool permissions (low stakes, system logs and revert are enough), a travel-data marketplace using a payment vault and OAuth scopes (medium stakes, closed ecosystem, existing transaction logs for disputes), and a high-stakes open-ecosystem case where they recommend FIDO verifiable intents and AP2 mandates. The mandate is a layered, selectively disclosed credential: a credential-provider layer, a user-signed instruction layer, and an optional agent-signed layer, so each party checks only its own part. They describe PayPal's approval token, which lets a user pre-approve payment instructions before the agent has picked an item or merchant, and say it is about to ship with Gemini. They close by arguing the same model applies to any hard-to-reverse action, such as medical orders, e-signatures or securities trades. The talk is short and conceptual, with a fair amount of PayPal product promotion.

## Key ideas
- **Agent authorization reduces to three questions** — Did the human authorize this, is it allowed right now within scope (time limit, amount, merchant or product intent), and can we prove it later if something goes wrong, such as in a dispute. ([1:09](https://youtu.be/vGn6N4-bxBY?t=69))
- **The answer depends on context: stakes and ecosystem openness** — The speakers use stakes (low or high) and counterparty (open or closed ecosystem, whether the parties already know each other) as the two axes. The badge analogy: inside a trusted building, a badge check is enough; meeting a stranger on the street needs something verifiable. ([2:33](https://youtu.be/vGn6N4-bxBY?t=153))
- **Low stakes in a closed ecosystem needs only logs and reversibility** — Claude Code connectors and per-tool allow/deny/ask permissions are set once by the human. Because the actions can be reverted, system logs are enough and no cryptographic proof is needed. ([5:04](https://youtu.be/vGn6N4-bxBY?t=304))
- **Medium stakes: money moves, but a known platform vouches for both sides** — A payment vault stores buyer credentials, which only become useful when access is granted through OAuth scopes in a closed partner ecosystem. Scopes come from the user's mandate, and disputes are handled with existing transaction logs rather than cryptographic receipts. ([6:29](https://youtu.be/vGn6N4-bxBY?t=389))
- **High stakes with strangers needs a verifiable, layered mandate** — The speakers say the industry should converge on FIDO verifiable intents and AP2 mandates. The credential is layered: a trusted credential provider issues the outer layer, the user signs the instructions, and the agent signs the autonomous action. Each party verifies only the layer it cares about, so no direct trust relationship is needed. ([10:36](https://youtu.be/vGn6N4-bxBY?t=636))
- **Pre-authorize before the agent has found a merchant** — PayPal's approval token flips the usual synchronous checkout. The user confirms the agent's instructions first, and PayPal returns an opaque, approved payload with the amount, expiry and intended merchant. The speakers say this ships to production soon, starting with Gemini users who pick PayPal. ([11:37](https://youtu.be/vGn6N4-bxBY?t=697))
- **The model generalises to any hard-to-reverse action** — The speakers say the same tiering applies to medical orders, e-signatures and securities trading: wherever an agent action is hard to undo, the evidence bar goes up. ([14:25](https://youtu.be/vGn6N4-bxBY?t=865))

## Techniques
- **Stakes x counterparty evidence matrix** — Classify each agent action by stakes (reversible or not, money or not) and by whether the counterparty is in a known, closed ecosystem. Use the result to pick the evidence level: logs and revert for low stakes, platform-enforced mandates for medium stakes, cryptographic verifiable mandates for high stakes with strangers. *When:* When deciding how much authorization and audit machinery a new agent action needs before shipping.
- **Scoped, time-bound, amount-capped mandates** — Each authorization carries an expiry, a spending cap, and a merchant or product-intent restriction. The agent is allowed to act only within those limits. *When:* Any agent that can spend money or take an irreversible action on the user's behalf.
- **Layered selective-disclosure credentials** — Build a signed token in layers: an issuer layer, a user-signed instructions layer, and an optional agent-signed layer for autonomous steps. Each verifier checks only the layer relevant to it, so parties do not need to share the full mandate. *When:* When multiple parties with no prior relationship must each check one part of an agent's authority.
- **Pre-authorize intent before the action target is known** — Ask the human to approve the instructions and limits first, and return an opaque approved token. The agent later uses the token to act only on a matching item or merchant. *When:* Autonomous shopping or booking, where the target is discovered after the human has given consent.
- **Scoped OAuth access to stored credentials** — Keep credentials in a vault and grant access only through OAuth scopes tied to the mandate, so partner agents never hold raw secrets. *When:* A platform mediates agent payments between known participants.

## Numbers
- Verifiable-intent credential has three layers: issuer, user-signed instructions, optional agent-signed autonomous step ([10:36](https://youtu.be/vGn6N4-bxBY?t=636))
- PayPal approval token payload carries amount, expiry and intended merchant (opaque string, approved only by PayPal) ([11:37](https://youtu.be/vGn6N4-bxBY?t=697))

## Hot takes
- A badge is not enough trust for a stranger; agent payments with unknown counterparties need verifiable, signed proof.
- The high-stakes tier (verifiable intents and AP2 mandates) is only seen in theory, not yet in production, per the speakers.

## Tools mentioned
Claude Code, FIDO verifiable intents, AP2 mandate, PayPal approval token, PayPal vault, OAuth, Passkeys, GitHub, Jira, Linear

## Relevance to our work
- **agentos** (2/3): The L1 gateway already has budgets, a Merkle audit log and an exec-gate. The stakes tiers and scoped, expiring mandates map directly onto those pillars. → *Add a stakes tier to the AgentOS budget and exec-gate policy: reversible actions get logs only, while money-moving or hard-to-reverse actions require a scoped, time-bound, amount-capped approval, which the Merkle audit log records as evidence.*
- **prosharness** (2/3): ProsHarness has phone-driven approvals and checkpoint/resume. The talk's 'did the human authorize, is it in scope now, can we prove it later' questions fit a checkpoint approval step. → *Store each phone approval as a time-bound, scope-limited record (action class, expiry, budget) alongside the checkpoint, and re-check it on resume before the run continues.*
