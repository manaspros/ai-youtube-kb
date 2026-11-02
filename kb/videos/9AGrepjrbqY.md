# This Open-Source Tool Might Fix Design Handoff Forever (PenPot)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `9AGrepjrbqY` · [watch](https://youtu.be/9AGrepjrbqY) · **date:** 2026-05-02 · **length:** 6:02 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Penpot, Figma, Sketch, Docker, Better Stack
- **topics:** dev-tools, vibe-coding-app-building · **tags:** penpot, figma-alternative, open-source, design-handoff, design-to-code, self-hosting, docker, css, svg, flexbox, design-tokens, inspect-mode

> Better Stack walkthrough of Penpot, an open-source browser design tool whose output is real SVG/CSS, pitched as a Figma alternative that reduces design-to-code handoff; self-hosting via Docker is shown.

## Summary
The host presents Penpot, an open-source, browser-based UI design and prototyping tool, as an alternative to Figma and Sketch. The main claim is that Penpot works on real web standards (SVG, CSS, Flexbox, Grid, HTML), so designs map more directly to code and there is no conversion layer for developers to decode. He says it is free with unlimited files and collaborators, and that it can be self-hosted with Docker in one command. A short live demo builds a simple card layout with a flex container, padding, a title, text and a button, then switches to inspect mode to show the generated CSS, which can be copied into a project. He also lists export to SVG, variants, design tokens and prototype flows. The argument against Figma is about handoff friction: Figma uses proprietary files and seat pricing, and its dev mode and plugins are an extra layer, while Penpot's inspect view is built in. The caveats he gives are that Penpot can struggle with very large files, has a much smaller plugin ecosystem, and has a learning curve for Figma users. He concludes it suits side projects, MVPs and privacy-sensitive or self-hosted setups, but big design-system teams already on Figma are unlikely to switch. No benchmarks or measured handoff times are given, and the video has no AI content.

## Key ideas
- **Penpot is open source and built on real web standards (SVG, CSS, Flexbox, Grid, HTML), so its output is closer to code than Figma's and needs no later conversion layer.** — The host's core argument is that designing directly in web primitives shrinks the gap between design and implementation. ([0:00](https://youtu.be/9AGrepjrbqY?t=0))
- **Self-hosting is pitched as a one-command Docker setup, shown in a live demo.** — He ran it on his own instance using the official Docker Compose file, and says the first startup took some time. ([1:14](https://youtu.be/9AGrepjrbqY?t=74))
- **Inspect mode shows the actual CSS (flex properties, spacing, layout) for a selection, which can be copied straight into a project.** — He presents this as the key difference: it is not a rough translation of the design into code. ([2:24](https://youtu.be/9AGrepjrbqY?t=144))
- **Handoff is built into the tool instead of coming from Figma-style dev mode, plugins and extra steps.** — Design data is stored as SVG, CSS and JSON, which he says keeps the design readable outside the tool and avoids proprietary-file lock-in. ([3:32](https://youtu.be/9AGrepjrbqY?t=212))
- **Honest caveats: Penpot can struggle with very large files, its plugin ecosystem is much smaller, and Figma users face a learning curve.** — He says big teams with mature Figma design systems are unlikely to switch, but that Penpot covers most needs for side projects and MVPs. ([3:32](https://youtu.be/9AGrepjrbqY?t=212))
- **Options are the free cloud version or self-hosting with Docker for more control.** — Self-hosting is recommended for privacy, internal tools and CI/CD concerns. ([5:43](https://youtu.be/9AGrepjrbqY?t=343))

## Techniques
- **Self-host Penpot with Docker Compose** — Use the official Penpot Docker Compose file and start it with a single docker compose up. The video does not show the file name, image tags or any config keys, so those must come from Penpot's own docs. *When:* When you want a self-hosted design tool for privacy, internal use or control over the stack.
- **Design in flex layout so the inspect CSS maps to code** — Build components with flex containers, padding and spacing, then use inspect mode to read and copy the CSS for the selection into the project. *When:* When designs are handed to developers who build with CSS and you want to avoid manual translation.
- **Use inspect mode for handoff instead of a dev-mode plugin** — Open the design's inspect view to read layout, spacing and tokens, rather than relying on extra plugins or a separate dev-mode step. *When:* For small teams or MVPs where the handoff step is a bottleneck.

## Numbers
- Penpot is free, with unlimited files and unlimited collaborators (as stated by the host). ([1:14](https://youtu.be/9AGrepjrbqY?t=74))
- Self-hosting is a single Docker Compose up command using the official compose file (the host's claim, not benchmarked). ([1:14](https://youtu.be/9AGrepjrbqY?t=74))
- The video gives no benchmarks, file-size limits, handoff-time measurements or pricing figures beyond the 'free, unlimited' statement. ([0:00](https://youtu.be/9AGrepjrbqY?t=0))

## Hot takes
- Penpot 'works on real web standards' so handoff is 'much smaller', but the video shows only one small demo and gives no measured handoff time.
- Figma is described as using proprietary files with seat pricing and a dev-mode layer, which is the host's framing and is not sourced.
- Penpot is positioned as enough for most teams, while the host concedes large design-system teams will stay on Figma.

## Tools mentioned
Penpot, Figma, Sketch, Docker, Docker Compose, SVG, CSS, Flexbox, CSS Grid, HTML
