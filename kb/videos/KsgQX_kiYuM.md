# How hardware product is made with Tomas Susanka

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `KsgQX_kiYuM` · [watch](https://youtu.be/KsgQX_kiYuM) · **date:** 2024-11-02 · **length:** 12:50 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Tomáš Sušánka · **orgs:** Trezor, Ledger, Altium, STMicroelectronics
- **topics:** product-ux · **tags:** hardware-development, consumer-electronics, pcb-design, prototyping, supply-chain, hardware-wallet, product-development

> Trezor's CTO walks through how a consumer hardware wallet gets made: spec, parallel design and engineering, prototypes, supplier loops, in-house testing, and stock planning. Off-topic for AI engineering.

## Summary
Tomáš Sušánka, CTO of Trezor (a cryptocurrency hardware wallet maker), describes how the company developed a facelift of its entry-level wallet: replacing micro-USB with USB-C and adding a secure element. He says the process runs as a spec followed by parallel product-design and engineering tracks. Design uses 3D-printed prototypes so the team can judge feel, and the team spent time on cable-connection UX after users connected cables only halfway. Engineering covers component choice, schematic and PCB layout, and small prototype runs. The main point is that hardware iteration loops run for weeks or months with suppliers, unlike software. He also covers certification, temperature testing, an in-house test fixture that replaced outsourced testing, and the difficulty of stock planning around Bitcoin halving demand spikes. The talk contains no AI content and ends with a conference invitation.

## Key ideas
- **Hardware starts from a product spec and then runs two parallel tracks: product design and engineering.** — The facelift spec was a new entry-level self-custody wallet that swapped micro-USB for USB-C and added a secure element for physical security. Design and engineering then proceed together. ([1:05](https://youtu.be/KsgQX_kiYuM?t=65))
- **Keeping a signature shape can be a hard constraint, and 3D-printed prototypes are used to judge feel in hand.** — The team kept the device shape because it differentiates them from competitors and changed the buttons. They relied on many 3D-printed prototypes because a slide cannot show how the device feels. ([2:11](https://youtu.be/KsgQX_kiYuM?t=131))
- **Small UX details like how a cable seats can matter a lot.** — Users of the previous model often pushed the USB cable in only halfway, so it did not connect. The team invested significant time in making the cable connection feel right. ([3:33](https://youtu.be/KsgQX_kiYuM?t=213))
- **The hardware loop is slow: prototype, test, discuss with stakeholders, send changes to suppliers, repeat.** — Proof of concept, user research testing, and supplier fixes repeat many times. A supplier turnaround of about a month plus two or three weeks per fix makes each cycle very long, which the speaker calls the main difference from software. ([7:05](https://youtu.be/KsgQX_kiYuM?t=425))
- **Certification, EMC, and environmental testing are part of the product schedule.** — The device needs certifications and must not interfere with other devices. It is also tested at extreme temperatures, from about -50 to +60 degrees, in manufacturing. ([8:22](https://youtu.be/KsgQX_kiYuM?t=502))
- **The company moved from outsourcing hardware testing to building its own test fixtures.** — The in-house tester takes the PCB, the operator closes a lid, and the fixture tests electronics over USB-C, uploads software, and checks the display. The speaker says the company was once a software company accidentally making hardware and is now both. ([9:17](https://youtu.be/KsgQX_kiYuM?t=557))
- **Demand spikes in crypto, such as Bitcoin halvings, make stock planning hard.** — Under-building forces pre-orders because devices cannot be made in weeks. Over-building risks financial loss. The speaker says Ledger took market share in 2017 when Trezor lacked stock. ([10:37](https://youtu.be/KsgQX_kiYuM?t=637))
- **Marketing needs photos before production stock exists, so teams use a few golden samples.** — About ten hand-made samples go to the marketing team while manufacturing is still in progress. The firmware and companion website are developed in parallel. ([10:37](https://youtu.be/KsgQX_kiYuM?t=637))

## Techniques
- **Parallel design and engineering tracks from one spec** — Write a product spec, then run industrial design (shape, size, buttons, color, material) and engineering (MCU, components, lifetime and supply, display) in parallel. *When:* Starting any physical product where form and internals must converge on the same spec.
- **Feel-first 3D-printed prototyping** — Print multiple physical prototypes of the enclosure and controls so the team can handle and judge them before finalizing the design. *When:* Early design stage, when specs on a slide cannot show ergonomics, buttons, or connector feel.
- **Schematic to PCB to small prototype run** — Capture the component-level schematic, lay out the PCB in Altium, then build about 20 to 50 prototypes before any volume production. Publish the design files on GitHub. *When:* Moving from concept to a testable hardware prototype with limited budget.
- **Automated in-house end-of-line test fixture** — Place the PCB in a tester, close the lid, connect over USB-C, run electrical checks, upload firmware, and verify the display. *When:* Production testing where outsourced testing is slow or where you need fast in-house iteration.
- **Golden samples for marketing** — Produce about ten hand-finished units for photos and ads before stock is ready. *When:* A launch needs marketing assets before manufacturing volume exists.

## Numbers
- The Model One was about ten years old and was the first hardware wallet on the market, according to the speaker. ([1:05](https://youtu.be/KsgQX_kiYuM?t=65))
- The first prototype runs were about 20 to 50 units. ([5:49](https://youtu.be/KsgQX_kiYuM?t=349))
- A supplier turnaround of about one month plus two to three weeks per revision cycle. ([8:22](https://youtu.be/KsgQX_kiYuM?t=502))
- Temperature testing range of about -50 to +60 degrees. ([8:22](https://youtu.be/KsgQX_kiYuM?t=502))
- Trezor says it is the number two hardware wallet vendor worldwide. ([10:37](https://youtu.be/KsgQX_kiYuM?t=637))
- Bitcoin halving happens about every four years and causes demand spikes. ([9:17](https://youtu.be/KsgQX_kiYuM?t=557))
- About ten golden samples were made for marketing. ([10:37](https://youtu.be/KsgQX_kiYuM?t=637))

## Hot takes
- Hardware iteration loops are measured in months, so software-style fast iteration does not carry over to physical products.
- Small UX details, such as how far a cable seats, can dominate user complaints.
- Crypto demand cycles make manufacturing planning a financial risk comparable to product design.

## Tools mentioned
Altium (PCB design), 3D printing (prototype enclosures), USB-C, GitHub (open-source hardware files), STMicroelectronics MCU products (named as the MCU vendor, no model stated), Secure element (component type, unnamed)
