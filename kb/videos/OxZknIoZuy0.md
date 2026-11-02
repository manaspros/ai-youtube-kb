# I Cracked a Password using ONLY Response Times...

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `OxZknIoZuy0` · [watch](https://youtu.be/OxZknIoZuy0) · **date:** 2025-11-02 · **length:** 6:51 · **format:** demo · **quality:** 3/5 · **depth:** intro
- **speakers:** James · **orgs:** Better Stack
- **topics:** security-guardrails, dev-tools · **tags:** timing-attack, side-channel, api-key, constant-time-comparison, timingSafeEqual, username-enumeration, rate-limiting, node-crypto, bun, typescript

> Better Stack demo of a timing attack: an early-exit string comparison leaks key length and characters through response times, then the speaker covers why real-world impact is limited and how to mitigate it.

## Summary
James from Better Stack builds a small Bun API protected by an API key, using a deliberately slowed string comparison (2 ms sleep per step) that exits early on the first mismatch or length mismatch. He first recovers the key length by timing requests for lengths 1 to 50, five samples each, and picks the length with the longest average response (12 characters, about 2.64 ms versus about 0.4 ms for the others). He then recovers each character by brute-forcing each position and keeping the slowest candidate, and the attack succeeds against his own key. He then admits the real JavaScript comparison produces noise that swamps the signal, so the attack fails against it on localhost. He notes that prior research suggests operations taking around 30 microseconds can be enough for a timing attack, and cites username enumeration and the Minerva ECDSA attack as real-world cases. The fixes he recommends are Node's constant-time crypto.timingSafeEqual, a hand-written constant-time comparison, or rate limiting to make brute force impractical.

## Key ideas
- **An early-exit string comparison leaks timing. Length is checked first, then characters are compared one by one and the function returns at the first mismatch, so a longer response means more matching steps.** — The demo's slowCompare adds a 2 ms sleep per step to exaggerate the effect. The speaker presents this as the same logic most string comparisons use in all languages. ([0:49](https://youtu.be/OxZknIoZuy0?t=49))
- **Key length can be recovered first by picking the length that gives the slowest average response time.** — Each length from 1 to 50 is tried five times and averaged. The slowest length is taken as the key length because a matching length means more comparison steps run. ([2:12](https://youtu.be/OxZknIoZuy0?t=132))
- **Characters can then be recovered one position at a time, using the same timing signal.** — Starting from a candidate padded with 'a' characters, every character is tried at each position and the slowest one is kept. The sampling is repeated for accuracy. This recovered a 12-character key the speaker had never seen before. ([3:16](https://youtu.be/OxZknIoZuy0?t=196))
- **The attack fails against the real JavaScript string comparison, because network and runtime noise hides the tiny differences in timing.** — The length guess came back as 1 instead of 12, and the character guesses were wrong. The speaker says that in practice comparison time is negligible next to network latency, even on localhost. ([4:15](https://youtu.be/OxZknIoZuy0?t=255))
- **Prior research suggests operations taking around 30 microseconds can be exploitable, so the practical threat is not limited to artificial sleeps.** — The speaker cites a paper listing susceptible operations, including MD5 of an 8x string, complex JSON parsing and SQLite memory select. He does not give the paper's method or results beyond that list. ([4:15](https://youtu.be/OxZknIoZuy0?t=255))
- **Timing differences leak more than secrets, and username enumeration is a common example.** — If the code checks the password only when the username is valid, valid usernames respond more slowly. An attacker could use this to find which accounts from a list to target. He also cites the Minerva attack, which recovers ECDSA keys from signing-time differences, with CVEs up to 2024. ([5:20](https://youtu.be/OxZknIoZuy0?t=320))
- **The fixes are a constant-time comparison for secret checks and rate limiting to keep brute force impractical.** — Node's crypto.timingSafeEqual compares two buffers in constant time with no early exit. A custom constant-time equal function also works. Rate limiting is presented as the simpler defence. ([5:20](https://youtu.be/OxZknIoZuy0?t=320))

## Techniques
- **Timing-based key length discovery** — Send requests with candidate keys of each length (1 to 50 in the demo), repeat each five times, average the response times, and take the length with the highest average. Use a large enough signal, since the demo's 2 ms per-step sleep exaggerated the difference (about 2.64 ms vs about 0.4 ms). *When:* Probing an endpoint that compares a secret with an early-exit comparison, to test whether it leaks length. Useful as a self-audit: check whether length-dependent timing is measurable on your own endpoint.
- **Per-position timing recovery** — Start with a candidate of repeated 'a' characters of the known length. For each position in turn, try every character, sample each several times, and keep the slowest one as the correct character. Build up the full key from these choices. *When:* Demonstrating or testing a character-by-character early-exit comparison. Only realistic when timing noise is far below the per-character cost.
- **Constant-time comparison for secrets** — Replace the early-exit comparison with crypto.timingSafeEqual in Node, which takes two Buffers and runs in constant time regardless of early mismatch. A hand-written constant-time equal function is an alternative. *When:* Checking API keys, tokens, HMACs or any secret against user input on a critical path.
- **Rate limiting as the cheap mitigation** — Limit requests per client or per key on authentication endpoints so the number of timing samples an attacker can take is too small for brute force. *When:* Authentication endpoints where a constant-time compare is not yet in place, or as a second layer on top of one.
- **Timing check for username enumeration** — Compare response times for valid and invalid usernames when the password check runs only for valid users. If the difference is measurable, make both paths do comparable work, for example by running a dummy password check when the username is not found. *When:* Login or password-reset endpoints where account existence should not be revealed.

## Numbers
- Demo API key length is random between 5 and 15 characters. ([0:00](https://youtu.be/OxZknIoZuy0?t=0))
- The slow comparison adds a 2 ms sleep per step. ([0:49](https://youtu.be/OxZknIoZuy0?t=49))
- Length search covers lengths up to 50, sampled five times each. ([0:49](https://youtu.be/OxZknIoZuy0?t=49))
- Correct length 12 measured at about 2.64 ms, versus around 0.4 ms for most other lengths. ([2:12](https://youtu.be/OxZknIoZuy0?t=132))
- Prior research suggests operations taking about 30 microseconds can be enough for a timing attack. ([4:15](https://youtu.be/OxZknIoZuy0?t=255))

## Hot takes
- The attack is shown only against an artificial 2 ms sleep. Against the real JavaScript comparison, the speaker's own test failed, so the title's 'ONLY response times' overstates what was shown.
- Timing attacks are real but mostly mitigated in mainstream libraries. The speaker himself says the common examples have largely been mitigated.
- Rate limiting is presented as the simpler practical defence, even though it does not remove the leak.

## Tools mentioned
Bun, Node.js (crypto.randomBytes, crypto.timingSafeEqual), TypeScript (generatekey.ts, crack scripts), SQLite (named as a susceptible operation in the cited paper), Claude (named as the summariser of the Minerva attack, not used in the demo)

## Relevance to our work
- **agentos** (2/3): The AgentOS proxy and its opt-in layers presumably validate API keys or tokens. Any such check that uses early-exit comparison leaks timing, which is a direct security gap for a proxy meant to guard agents. → *Audit every API-key, token and budget-key comparison in the Rust proxy and any Node or Python auth code. Replace them with a constant-time comparison (for example the subtle crate's ConstantTimeEq in Rust) and add rate limiting on auth failures.*
- **prosharness** (1/3): ProsHarness has phone-driven approvals and zero-token credential handling. Approval tokens or credential checks that use early-exit comparison would be exposed to the same timing leak. → *Make sure approval-token and credential checks in ProsHarness use a constant-time comparison, for example crypto.timingSafeEqual on Buffers.*
