# This App Works WITHOUT Internet?! (Jack Dorsey’s BitChat)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `hdRn3DQ_C_Y` · [watch](https://youtu.be/hdRn3DQ_C_Y) · **date:** 2025-11-02 · **length:** 4:20 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Block, Square, Bluesky, Twitter
- **topics:** security-guardrails, vibe-coding-app-building · **tags:** bitchat, bluetooth-low-energy, mesh-networking, noise-protocol, end-to-end-encryption, vibe-coding, security-review, cross-platform-testing, open-source

> Quick hands-on look at Jack Dorsey's open-source BitChat, a Bluetooth mesh messenger with no internet or servers. The reviewer finds the iOS build buggy, and the app is a weekend vibe-coded project that drew security criticism.

## Summary
The video explains BitChat, an open-source peer-to-peer messaging app published by Jack Dorsey, which sends messages over Bluetooth Low Energy in a phone-to-phone mesh with no central server. Messages are encrypted with a NoiseXX handshake, and ephemeral keys rotate every 5 to 15 minutes. The narrator says Dorsey described it as a weekend project vibe-coded with Goose, an open-source AI assistant from Block, and that security experts quickly found serious architectural flaws. The repo now warns that features have not had an external security review. In a short test, iOS could not receive messages from Android, while Android received iOS messages without issue. The narrator judges the UI subpar and the crypto design promising but unproven, and suggests the app is not yet safe to call secure. Use cases mentioned are crowded events, protests, confidential corporate meetings, and journalist source protection. The piece is a 4-minute news-style review with no sponsor segment and little independent technical depth.

## Key ideas
- **BitChat is a serverless peer-to-peer messenger. Phones send and relay messages over Bluetooth Low Energy, so messages hop device to device across a mesh with no internet or cell service.** — Each phone acts as both sender and relay, so reach extends beyond one Bluetooth range. The narrator compares it to AirTags piggybacking on nearby iPhones. ([0:00](https://youtu.be/hdRn3DQ_C_Y?t=0))
- **Security rests on a NoiseXX handshake with ephemeral keys rotated every 5 to 15 minutes. The narrator says this is meant to make tracking nearly impossible.** — The narrator presents this as the reason the app is interesting technically, but does not verify the implementation. ([1:18](https://youtu.be/hdRn3DQ_C_Y?t=78))
- **The project was reportedly a weekend vibe-coded build made with Goose, an open-source AI assistant from Block. Security experts found serious architectural flaws soon after release.** — The author added a GitHub warning that features have not had external security review and may contain vulnerabilities. Outside contributors are shipping patches. ([1:18](https://youtu.be/hdRn3DQ_C_Y?t=78))
- **The narrator advises against labeling the app secure yet. Its open-source status lets others audit it or fork it.** — The fork-and-extend point is presented as a reason it could still matter, not as evidence of security. ([1:18](https://youtu.be/hdRn3DQ_C_Y?t=78))
- **Cross-platform messaging was broken in the reviewer's test. iOS could not detect messages sent from Android, while Android received iOS messages instantly.** — The narrator calls the iOS app not production-ready and says the UI feels like a regular messenger with a subpar design. ([2:35](https://youtu.be/hdRn3DQ_C_Y?t=155))
- **Target use cases are crowded events with overloaded cell networks, protests, confidential corporate meetings, and journalist source protection.** — The narrator's verdict is that the tech is cool and the project has potential, but it needs iOS fixes and a real security audit first. ([2:35](https://youtu.be/hdRn3DQ_C_Y?t=155))

## Techniques
- **Cross-platform two-device messaging test** — Install the app on one iOS and one Android device, send messages in both directions, and confirm each side receives them. This surfaced the one-way iOS receive failure in the video. *When:* Before trusting any peer-to-peer or mesh messaging app, or when checking a client build that is still early.
- **Check the repo's security status before trusting an app** — Read the README or security notice for a statement about external security review or known vulnerabilities. In this case the GitHub repo warned that features had not been externally reviewed. *When:* When evaluating open-source security or privacy tools, especially ones built quickly or with AI assistance.

## Numbers
- Ephemeral keys rotate every 5 to 15 minutes in the NoiseXX-based design. ([1:18](https://youtu.be/hdRn3DQ_C_Y?t=78))
- Video length is 4:20. The reviewer's cross-platform test covered two devices, one iOS and one Android. ([2:35](https://youtu.be/hdRn3DQ_C_Y?t=155))

## Hot takes
- The title says the app works without internet, but the reviewer treats the security claims as unverified and says it should not be labeled secure yet.
- Calling BitChat a secure app is premature. It was a vibe-coded weekend project that drew security criticism, and the repo itself warns of unreviewed features.
- The iOS build appears not production-ready based on one-way message reception.
- The video is a short news-style review with thin technical depth. The title's hype about working without internet is thin on substance, which caps quality at 2.

## Tools mentioned
BitChat, Bluetooth Low Energy (BLE), NoiseXX handshake, Goose, AirTags, iOS, Android
