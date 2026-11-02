# Voyager's 16 Billion Mile Software Update

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `1NXUw8QK1L4` · [watch](https://youtu.be/1NXUw8QK1L4) · **date:** 2026-10-19 · **length:** 8:16 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** NASA, NASA JPL, Deep Space Network
- **topics:** dev-tools · **tags:** voyager, spacecraft, flight-software, assembly, memory-patching, fault-diagnosis, memory-dump, embedded, nasa, horizons

> How NASA keeps patching Voyager 1's 1970s flight software: rewritable memory, a dead chip worked around by relocating code, and revived thrusters. Not AI-related.

## Summary
The video explains how Voyager 1 flies itself because a command round-trip takes about a day, using three flight computers with spares and roughly 69 KB of total memory written in assembly. Unlike Apollo's hardwired code, Voyager's memory is rewritable, and the team sent 18 patches during the 1979 Jupiter flyby. In November 2023 a dead memory chip corrupted about 3% of the data computer's memory, so the team diagnosed the fault with a full memory dump and then split the affected routines into fragments placed in free gaps, updating every call site by hand without an assembler or ground test. The speaker also covers the 2025 revival of thrusters that had been dead since 2004, the power budget that has forced most instruments off, and how to check the spacecraft's distance and signal delay with JPL's Horizons system.

## Key ideas
- **Voyager's constraints: about 69 KB of total memory across six computers (three functions, each with a spare), all written in assembly, with a round-trip command delay of about a day.** — Autonomy is forced because a human reaction takes a day; the pointing computer launched with only two words of memory free. ([0:00](https://youtu.be/1NXUw8QK1L4?t=0))
- **Unlike Apollo 11's hardwired code, Voyager's memory is rewritable, so the team uploaded 18 new programs during the 1979 Jupiter flyby.** — Updatability is what makes later repairs possible at all. ([2:19](https://youtu.be/1NXUw8QK1L4?t=139))
- **Diagnosis by memory dump: when telemetry became repeating ones and zeros, a POKE command made the data computer run different routines and dump its full memory, which was diffed against a pre-fault dump.** — The comparison pinpointed a single dead chip that corrupted about 3% of memory. ([3:11](https://youtu.be/1NXUw8QK1L4?t=191))
- **The dead chip held one bit from each of 256 consecutive 16-bit words, so every word in that row had a bad bit, and those words held routines called from across the program.** — Because a fixed block was lost, the fix had to relocate the code rather than replace hardware. ([3:11](https://youtu.be/1NXUw8QK1L4?t=191))
- **Workaround: no single free gap could hold 256 words, so the code was split into pieces placed in whatever gaps existed, and every caller was updated to the new addresses.** — The changes were translated to binary by hand because no assembler or test machine was available; it was the first flight load not tested thoroughly on the ground. ([4:23](https://youtu.be/1NXUw8QK1L4?t=263))
- **Staged reload: the telemetry-packing code went up first and readable data returned two days later, then the science-data code moved in May and all powered instruments were sending data by June.** — Loading the health-monitoring path first gave a verifiable signal before touching the riskier path. ([4:23](https://youtu.be/1NXUw8QK1L4?t=263))
- **Thruster revival: the team hypothesized that a glitch had flipped a switch, not that the heaters were dead, and tested it on 20 March 2025 despite the risk of an explosion if the spacecraft drifted.** — The heater temperature rose within 20 minutes, reviving thrusters dormant for 21 years. ([5:31](https://youtu.be/1NXUw8QK1L4?t=331))
- **Power is the real end-of-life limit: the RTG loses about 4 W a year, so the team keeps switching instruments off; 8 of 10 are now off, and the speaker expects signal reception to last until about 2036.** — Horizons (JPL) can be queried with a curl command for the current distance and light-time to the spacecraft. ([6:32](https://youtu.be/1NXUw8QK1L4?t=392))

## Techniques
- **Dump-and-diff fault localization** — When a remote system still accepts commands but its output becomes garbage, trigger a full memory dump (the Voyager team used a command they called POKE that made the computer run different parts of its software). Diff the dump against a dump taken before the fault to find the corrupted region, then map that region to hardware (here, one bit per word across 256 words pointed to one dead chip). *When:* Telemetry is nonsensical but the system is still responsive, and you have a known-good baseline snapshot to diff against.
- **Relocate code around a dead memory block** — Split the affected routines into fragments, find whatever free gaps exist in memory (no contiguous block was big enough), place each fragment there, then update every call site so it points at the new addresses. *When:* A fixed block of memory is permanently unusable and no hardware fix is possible; fragmented placement is acceptable but every reference must be patched.
- **Staged reload of critical code** — Upload and verify the path that returns health data first (the engineering-data packer), wait for the readable signal, then upload the science-data path, then bring up each instrument. *When:* You must patch a live system you cannot fully test beforehand, so you want a verifiable checkpoint after each step.
- **Test a state-flag hypothesis before declaring hardware dead** — Before writing off a component, check whether the fault could be a corrupted or flipped control state rather than failed hardware, then try the recovery while watching a telemetry signal (heater temperature) within a short window. *When:* A component is assumed dead but the failure mode might be a configuration glitch, and the recovery attempt is risky but observable.
- **Power budgeting by shutting subsystems off** — Track the declining power budget and disable lower-priority instruments in sequence so the remaining ones can keep operating as generation falls. *When:* Available power is decreasing over time (for example, a decaying radioisotope source) and you must choose what to keep running.

## Numbers
- Light-day distance is about 25.9 billion km (about 16 billion miles); Voyager 1 is roughly that far away by 18 November. ([0:00](https://youtu.be/1NXUw8QK1L4?t=0))
- Voyager 1 launched in 1977, has flown for just over 49 years, and moves at nearly 38,000 mph. ([0:59](https://youtu.be/1NXUw8QK1L4?t=59))
- Six computers (three functions plus spares) hold about 69,000 bytes of memory total (under 70 KB). ([0:59](https://youtu.be/1NXUw8QK1L4?t=59))
- Pointing computer had two words of memory free at launch; 18 flight-software uploads during the 1979 Jupiter flyby. ([2:19](https://youtu.be/1NXUw8QK1L4?t=139))
- A dead chip corrupted about 3% of the data computer's memory: 256 words of 16 bits, one bit per word. ([3:11](https://youtu.be/1NXUw8QK1L4?t=191))
- Engineering data became readable again two days after the 18 April 2024 upload, after about five months of unreadable data. ([4:23](https://youtu.be/1NXUw8QK1L4?t=263))
- Thruster fuel-line opening shrank from about 0.25 mm to about 0.035 mm. ([4:23](https://youtu.be/1NXUw8QK1L4?t=263))
- Main thrusters failed in 2004; they were revived on 20 March 2025 (heater temperature rose within 20 minutes), about 21 years later. ([5:31](https://youtu.be/1NXUw8QK1L4?t=331))
- Power loss is about 4 W per year; 8 of 10 instruments are now off, and at least one is expected to run into the 2030s; signal reception expected until about 2036. ([6:32](https://youtu.be/1NXUw8QK1L4?t=392))
- Signal light-time on 18 November reaches exactly 1440 minutes (24 hours). ([7:34](https://youtu.be/1NXUw8QK1L4?t=454))

## Hot takes
- Voyager's engineering is a strong case study in working under severe constraints and in patching systems you cannot test on the ground, though it has no direct AI content.
- The speaker's framing is accessible and well-sourced by its own account, but it is a popular-science explainer rather than practitioner material.

## Tools mentioned
Horizons (NASA JPL ephemeris system, queried with curl), Deep Space Network (NASA ground dishes)
