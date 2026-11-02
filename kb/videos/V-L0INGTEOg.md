# Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `V-L0INGTEOg` · [watch](https://youtu.be/V-L0INGTEOg) · **date:** 2026-06-18 · **length:** 20:11 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Boris Starkov · **orgs:** ElevenLabs, Twilio
- **topics:** claude-code, coding-agents, skills-self-improvement · **tags:** reverse-engineering, hardware, protocol-discovery, brute-force, mitm-proxy, claude-code, skills, sip, twilio, elevenlabs, long-running-session

> Boris Starkov (ElevenLabs) shows how Claude Code reverse-engineered an undocumented 1990s-style VoIP phone's protocol through port probing, command brute-force, and a traffic-capture proxy, then packaged the result as a reusable skill.

## Summary
The speaker from ElevenLabs describes reverse engineering a legacy Viking VoIP phone with Claude Code so it could be wired to a voice agent via Twilio SIP. The phone only had Windows XP-era vendor software, and a prior team had given up a year earlier. Claude Code probed the network to find the right port, then brute-forced two-letter command codes, and found about 80 valid ones. Settings it wrote were lost on reboot, which led to a long dead end. The breakthrough came from running the vendor software in a Windows VM and routing its traffic through a logging TCP proxy on the Mac, which exposed a command with a binary payload and a one-byte checksum. Claude inferred the checksum and confirmed it on more samples. The speaker then packaged the protocol as a skill that lets Claude program the phone directly, and open-sourced it. He is candid that the agent made the work possible for a non-security engineer, and that he acted as the agent's hands for physical steps.

## Key ideas
- **Claude Code works as a black-box explorer on hardware with no docs** — It mapped the available ports and found that the first one was an unrelated electronics tunnel, then found the real control port by iterating. It sent a sequence and read the replies to confirm an actual protocol exists. ([3:59](https://youtu.be/V-L0INGTEOg?t=239))
- **Brute-force a small command space and sort replies into errors and valid responses** — The protocol used two-letter command codes. Claude tried every two-letter combination. Most returned an error string, and about 80 returned a different, valid-looking reply. ([5:01](https://youtu.be/V-L0INGTEOg?t=301))
- **A successful write can still be a dead end if it is not persistent** — Credentials were accepted, but the settings vanished on reboot because they were only in temporary memory. A multi-hour search for a save command, including a sweep of three-letter commands, found nothing. ([7:37](https://youtu.be/V-L0INGTEOg?t=457))
- **Capture the vendor software's traffic with a man-in-the-middle proxy when direct access fails** — The Windows VM had no internet bridge, so a TCP proxy on the Mac relayed traffic between the vendor software and the phone while logging it. That revealed a command, TS, with a binary payload that earlier probing had missed. ([9:40](https://youtu.be/V-L0INGTEOg?t=580))
- **Infer a checksum in a closed loop, then confirm it on fresh samples** — Because the agent knew the inputs and outputs, it could fit the one-byte checksum rule and then test it on more values. The speaker says the encryption turned out to be a simple one-byte addition, and he calls this lucky. ([10:43](https://youtu.be/V-L0INGTEOg?t=643))
- **Package the learned protocol as a skill so the VM is no longer needed** — After a factory reset, the phone can be programmed directly from the skill. The speaker open-sourced the skill so that another agent could set up the same phone without a Windows machine. ([12:55](https://youtu.be/V-L0INGTEOg?t=775))
- **The agent can direct a human to do physical steps when it cannot act itself** — The speaker counted beeps, rebooted the phone, and controlled the VM at the agent's request. He says the agent was orchestrating and he was its hands, and that he could not unblock it on the protocol itself. ([17:37](https://youtu.be/V-L0INGTEOg?t=1057))
- **The vendor's proprietary software is no longer required** — The speaker says that a year ago a company-supplied interface was needed. With the protocol known, any home device can be reached in the same way, so the approach may extend to other hardware. ([16:00](https://youtu.be/V-L0INGTEOg?t=960))

## Techniques
- **Black-box command sweep with error classification** — Enumerate candidate ports and commands systematically, then treat error replies as the baseline and flag any other reply as a valid command. *When:* An undocumented serial or network device whose command set is small enough to enumerate.
- **Intermediary proxy for vendor-client traffic capture** — Run the vendor's client in a VM that cannot reach the device directly. Route it through a host-side TCP proxy that relays packets to the device and logs both directions, then analyse the log. *When:* The vendor client only runs on an OS or network setup you cannot use directly, and you need the exact wire protocol.
- **Closed-loop hypothesis confirmation** — Propose a rule from observed input and output pairs, such as a checksum, then test it on new samples and iterate until it holds. *When:* A small, opaque field whose inputs and outputs you can observe.
- **Persisting a learned protocol as a skill** — Write the discovered commands, sequence and format into a skill that a fresh agent session can load, so it can drive the device without repeating the full investigation. *When:* Knowledge that took days to uncover and must be reused across sessions or shared with others.
- **Using the full session transcript as context to generate a deliverable** — Give the whole working conversation as context and ask for slides built from it. *When:* You need a write-up of a long technical session without writing it from scratch.
- **Human as actuator for physical steps** — The agent directs a person through physical actions it cannot take, such as listening for beeps or power-cycling a device, and feeds back the observations. *When:* Computer use is unavailable or the task needs a physical action in the loop.

## Numbers
- The phone was bought about a year before the talk, and a team of three senior engineers plus ChatGPT could not get it working ([2:29](https://youtu.be/V-L0INGTEOg?t=149))
- Of all two-letter command codes tried, about 80 returned valid responses and the rest returned errors ([5:01](https://youtu.be/V-L0INGTEOg?t=301))
- The dead end on persistence took a multi-hour search, including a sweep of all three-letter commands with no result ([7:37](https://youtu.be/V-L0INGTEOg?t=457))
- The checksum is one byte ([10:43](https://youtu.be/V-L0INGTEOg?t=643))
- The phone has a 256-byte memory, which was also cracked ([12:55](https://youtu.be/V-L0INGTEOg?t=775))
- Reverse engineering the protocol took the speaker a couple of days ([13:56](https://youtu.be/V-L0INGTEOg?t=836))
- Total token cost of the work was in the order of $10 to $100 of corporate ElevenLabs tokens ([16:00](https://youtu.be/V-L0INGTEOg?t=960))

## Hot takes
- Without the agent the demo would not have been possible at all, not just ten times faster, because the speaker is not a security engineer.
- The old barrier was the vendor's proprietary software. Now a device can be talked to the same way as any other device on the home network.
- Packaging the discovered protocol as a skill lets anyone give an agent the file and get the device set up without a Windows machine.
- The speaker avoids the word hack and says reverse engineering, and he calls the one-byte checksum lucky.

## Tools mentioned
Claude Code, Twilio (SIP trunk), ElevenLabs conversational agents, Windows virtual machine, TCP proxy on macOS, PoE router

## Relevance to our work
- **agentos** (1/3): L2D SkillForge needs a success signal for skill scoring. This talk checks each step against a concrete device readback, and that gives a clear verifier to borrow. → *When designing the SkillForge success signal, consider whether a readback-style verifier (write, reboot, read back) can serve as one signal.*
- **prosharness** (1/3): Multi-hour runs stall on dead ends. The talk shows how a repeated, failed sweep wastes time, and that a resumed run needs to know what was already tried. → *Record failed attempts (for example, the three-letter command sweep) in the ProsHarness checkpoint so that a resumed run does not repeat them.*
- **general** (1/3): Matches the context-engineering interest. The speaker feeds the full working transcript into the agent to produce the slides. → *Try generating a write-up from the full session transcript as context, and compare it with a summary written from memory.*
