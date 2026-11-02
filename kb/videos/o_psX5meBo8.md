# The Best File Transfer Tool You've Never Heard Of (croc)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `o_psX5meBo8` · [watch](https://youtu.be/o_psX5meBo8) · **date:** 2026-08-02 · **length:** 8:30 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Andres (Better Stack host) · **orgs:** Better Stack, croc (project by Zach Scholl)
- **topics:** dev-tools, security-guardrails · **tags:** croc, file-transfer, pake, p2p, self-hosted-relay, cli, go, docker, wetransfer, scp

> Better Stack walkthrough of croc, an open-source Go CLI for sending files peer-to-peer through a relay, with PAKE code phrases and resumable transfers; a tool intro with a self-hosted relay option.

## Summary
The host argues that most file transfer tools trade off speed, security and simplicity, and presents croc as hitting all three. Croc is an open-source Go CLI that runs a full-duplex relay session instead of upload-then-download, and switches to a local transfer when both machines share a LAN. Security comes from PAKE: a disposable code phrase drives a key exchange, so a wrong phrase makes the transfer fail, and the relay only sees encrypted bytes and metadata. The default relay is a public one run by the tool's creator, and the video shows that a self-hosted relay can be started with a built-in command using a Docker image. The demo covers sending from a Windows machine to a MacBook with one command, receiving with a code phrase, and resuming a broken transfer. The video is a short product intro with little depth on internals or benchmarks.

## Key ideas
- **Most file transfer tools miss at least one of fast, secure, simple.** — The host frames speed, security and simplicity as three pillars and says link-based tools (WeTransfer-style) are simple but slow and only as secure as the link, while SCP/SSH/FTP are fast and secure but need a server and port forwarding. ([0:00](https://youtu.be/o_psX5meBo8?t=0))
- **Upload-then-download is slower than it needs to be.** — With 5 Mbps up and 8 Mbps down, sequential transfer gives about 3.1 Mbps effective, which is below either link speed. A full-duplex relay avoids this by sending and receiving at the same time. ([2:05](https://youtu.be/o_psX5meBo8?t=125))
- **Croc uses a relay for full-duplex transfer and goes direct on the LAN.** — Croc relays both sides through a server so they send and receive simultaneously. If both machines are on the same local network, it detects that and transfers locally, which is faster still. ([3:06](https://youtu.be/o_psX5meBo8?t=186))
- **PAKE replaces a static shared password.** — The disposable code phrase is not used directly as an encryption key. Both sides run a cryptographic exchange with it to derive a stronger key; an interceptor with the wrong phrase makes the exchange fail and no data moves. ([4:25](https://youtu.be/o_psX5meBo8?t=265))
- **The default public relay sees only ciphertext and metadata.** — The file is encrypted end-to-end before leaving the sender, so the relay operator cannot read contents. The host still flags that a third-party relay in the middle may be a blocker for data-residency or policy reasons. ([4:25](https://youtu.be/o_psX5meBo8?t=265))
- **Self-hosting the relay is presented as a short setup.** — Croc has a built-in relay command that starts your own relay, with a Docker image included. Transfers are then pointed at it with a relay flag. The host calls it a five-minute setup for corporate environments. ([5:45](https://youtu.be/o_psX5meBo8?t=345))
- **The user experience is one send command and one code phrase.** — The sender runs croc send with a file and gets a generated code phrase. The receiver runs croc, enters the phrase, and accepts. Transfers resume from where they left off after a connection break. ([6:20](https://youtu.be/o_psX5meBo8?t=380))

## Techniques
- **Send a file with a one-time code phrase** — Sender: `croc send <file>` prints a randomly generated code phrase. Receiver: run `croc`, type the code phrase when prompted, then type y to accept. The video says install is a one-line command on Windows and Mac, with platform instructions on the project's GitHub page (the exact install commands are not shown). *When:* Quick one-off transfers between machines with no accounts, shared servers or port forwarding, for example a Windows PC to a Mac.
- **Resume an interrupted transfer** — After a connection drops mid-transfer, resume from the sending side. The transfer continues where it stopped instead of restarting. The video does not show the exact command. *When:* Large files over unreliable networks.
- **Self-host the relay for corporate use** — Start your own relay with croc's built-in relay command, which ships with a Docker image. Point transfers at it with the relay flag instead of the default public relay (the video does not spell out the flag name). *When:* Data-residency rules, or a policy against routing transfers through infrastructure you do not control.

## Numbers
- Sequential upload-then-download with 5 Mbps up and 8 Mbps down gives about 3.1 Mbps effective (below either link), which is the basis for the full-duplex argument. ([2:05](https://youtu.be/o_psX5meBo8?t=125))
- Demo transfer between a Windows machine and a MacBook; no specific transfer speed or file size is reported. ([6:20](https://youtu.be/o_psX5meBo8?t=380))
- Video length 8:30. ([0:00](https://youtu.be/o_psX5meBo8?t=0))

## Hot takes
- Calls croc 'the best file transfer tool I've ever used' with no benchmark against alternatives.
- Says self-hosting a relay is a 'five-minute setup' and 'not a deal breaker' without showing it.
- The 3.1 Mbps figure assumes a strictly sequential upload-then-download model; it is a simple illustration, not a measurement.

## Tools mentioned
croc (open-source Go CLI, by Zach Scholl), Docker (croc relay image), WeTransfer, Dropbox, AirDrop, SCP, SSH, FTP, Discord

## Relevance to our work
- **prosharness** (1/3): Its one-time code phrase with PAKE is a reference pattern for short-lived pairing between two devices, which relates to phone-driven approvals. → *If ProsHarness needs a phone-to-machine pairing step, skim croc's PAKE code-phrase design as a reference for short-lived pairing codes. Do not treat this as a security audit.*
