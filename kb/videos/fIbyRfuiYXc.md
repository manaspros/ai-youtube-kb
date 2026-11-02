# Could FOKS Be the FUTURE of Secure Git Hosting?

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `fIbyRfuiYXc` · [watch](https://youtu.be/fIbyRfuiYXc) · **date:** 2025-11-02 · **length:** 5:49 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Keybase, fox.app
- **topics:** security-guardrails, dev-tools · **tags:** end-to-end-encryption, git, secrets-management, key-management, post-quantum, federated, keybase-alternative, homebrew, self-hosting

> Walkthrough of FOKS, an open-source, federated, Go-based alternative to Keybase for end-to-end encrypted git and key-value secrets, with post-quantum hybrid encryption and a short setup demo.

## Summary
The video introduces FOKS (Federated Open Key Service; captions render it as "Fox"), an open-source Keybase-style tool written in Go for end-to-end encrypted git repos and key-value storage, aimed at API keys, configs and sensitive files. The speaker's main claims are that clients, not the server, hold the keys, so a server breach exposes only ciphertext, and that users can pick or self-host a federated server to avoid vendor lock-in. The demo runs the setup on the default fox.app federated server: start the control agent, sign up with an email, username and device name, list keys, create a remote repo, then clone it, which turns on encryption automatically. Pushed files reach the server as ciphertext, and keys can be revoked by ID. For post-quantum security the speaker says FOKS layers Curve25519 with the ML-KEM algorithm, so an attacker would need to break both, though he admits he does not fully understand ML-KEM. The product is in beta, and the speaker says mobile apps, sync-based file systems and encrypted chat are planned. The video offers no benchmarks, threat model or independent audit, so the security claims are the vendor's.

## Key ideas
- **Client-held keys are the core security claim** — The speaker says the client, not the server, controls the keys, so a hacked server yields only ciphertext. This is a vendor claim; the video shows no threat model or audit. ([0:00](https://youtu.be/fIbyRfuiYXc?t=0))
- **Federation is pitched as the answer to vendor lock-in** — Users can pick a server whose policies they trust or self-host one. Being open source, the code can be audited, forked or run as a hosting service. ([0:00](https://youtu.be/fIbyRfuiYXc?t=0))
- **Git contents are encrypted on the client, including file names and history** — Commits, file names and history are encrypted locally, so the server stores only ciphertext. The speaker presents this as the main differentiator. ([1:09](https://youtu.be/fIbyRfuiYXc?t=69))
- **The remote repo is created first, and cloning turns on encryption** — fox git create makes the remote repo on the server. Cloning it locally initializes FOKS and enables encryption automatically; after that, normal add, commit and push work and are encrypted transparently. ([3:14](https://youtu.be/fIbyRfuiYXc?t=194))
- **Key revocation by ID is the recovery story for lost devices** — Keys are listed on the server and can be revoked by ID, e.g. after a stolen laptop. The speaker says the other keys then rotate automatically; the video does not show this happening. ([3:14](https://youtu.be/fIbyRfuiYXc?t=194))
- **Post-quantum protection is a hybrid of Curve25519 and ML-KEM** — An attacker would have to break both schemes. The speaker says he does not really understand ML-KEM and is trusting the security experts, so treat this as an unverified summary. ([4:36](https://youtu.be/fIbyRfuiYXc?t=276))
- **Single-key risk is shown, then waved off for the demo** — fox key list warns that losing the only key means losing all access. The demo acknowledges the warning and skips backup-key setup, a step a real deployment needs. ([2:11](https://youtu.be/fIbyRfuiYXc?t=131))
- **Beta status and roadmap** — The speaker says FOKS is still beta, with mobile apps, sync-based file systems and encrypted chats planned, and that communities could run their own federated servers. ([4:36](https://youtu.be/fIbyRfuiYXc?t=276))

## Techniques
- **Set up FOKS and create a user** — Install FOKS (the speaker uses Homebrew and says to check the install docs for other platforms). Run `foxctl start` to start the control agent. Run `fox sign up`, press Enter, choose to create a new user, choose a home server (the default is the federated fox.app server, or a custom one), enter an email, optionally an invite code, a username, and a device name for the access key. The captions say `fox` and `foxctl`; the exact binary names should be checked against the docs. *When:* First-time setup on a workstation, or when evaluating FOKS against a self-hosted alternative.
- **Create an encrypted git repo** — Run `fox git create <repo>` to create the remote repo on the server first. Clone it locally. Cloning shows FOKS initializing, which enables encryption for the repo. Then add, commit and push as usual; encryption happens transparently on push. *When:* Storing config files, API keys or sensitive files in git without the server being able to read them.
- **Inspect and revoke keys** — Run `fox key list` to show all keys on the server, then revoke a key by its ID. The speaker says other keys rotate automatically after a revoke; the command names were not clearly captured for this step. *When:* Responding to a lost or stolen device, or auditing which devices hold access.
- **Acknowledge the single-key warning** — When `fox key list` warns that losing the only key means losing access, the demo uses a clear-device-message command to accept the risk. The exact command name is garbled in the captions. In real use, create a backup key first, which the sign-up flow offers. *When:* Only for throwaway demos. Production accounts need a second key or backup first.

## Numbers
- No benchmarks, latency figures, costs, adoption stats or test results are given. The video runs 5:49 and is a setup walkthrough. ([0:00](https://youtu.be/fIbyRfuiYXc?t=0))
- Two encryption layers: Curve25519 plus the ML-KEM post-quantum algorithm; an attacker must break both. ([4:36](https://youtu.be/fIbyRfuiYXc?t=276))

## Hot takes
- Hype title ("Could FOKS Be the FUTURE of Secure Git Hosting?") and "game changer" framing, but the demo is concrete.
- The speaker admits he does not understand ML-KEM and relies on trusting security experts, so the post-quantum claim is not checked in the video.
- Claims that keys rotate automatically on revoke and that a hacked server reveals nothing are not shown in the demo.
- Still beta, and the demo skips backup-key setup, which the video itself flags as the main single-key risk.
- Sponsorship: none visible in the transcript.

## Tools mentioned
FOKS (Federated Open Key Service), foxctl, fox CLI, Homebrew, Go, Curve25519, ML-KEM, Keybase, YubiKey, fox.app federated server

## Relevance to our work
- **agentos** (1/3): AgentOS guardrails and the Crucible/exec-gate work touch secrets and credentials for agents. FOKS is a prior-art example of client-held keys and encrypted config storage, but it is not an agent-facing tool. → *Read the FOKS white paper and compare its client-held key model with how AgentOS would store provider API keys if that is designed later.*
- **prosharness** (1/3): ProsHarness has zero-token credential handling. FOKS's client-held keys and encrypted per-repo config are a related pattern for storing secrets that agent runs need. → *Compare ProsHarness's credential handling against the FOKS key model (client-held keys, revoke by ID, backup key); consider whether it is worth a spike for secret storage.*
