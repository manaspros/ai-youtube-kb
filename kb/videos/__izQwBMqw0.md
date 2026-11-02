# Security in 2026 Is Going to Look Very Different

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `__izQwBMqw0` · [watch](https://youtu.be/__izQwBMqw0) · **date:** 2026-02-02 · **length:** 6:32 · **format:** news · **quality:** 2/5 · **depth:** intro
- **speakers:** Andres (Better Stack) · **orgs:** Better Stack, WordPress, Google, Microsoft, CISA, NSA, White House, Linux kernel project
- **topics:** security-guardrails, dev-tools · **tags:** CVE, vulnerabilities, memory safety, Rust, supply chain, XSS, SQL injection, WordPress, plugins, AI-driven monitoring, vibe coding, Better Stack

> Better Stack's 2026 security outlook: record CVE counts, AI-accelerated exploits, memory-safe languages and smaller dependency surfaces, with a product plug for its monitoring tool.

## Summary
The speaker opens with 2025 vulnerability stats: over 48,000 CVEs published (up about 18%, roughly 130 a day), and about 28% of observed early-2025 exploits launched within a day of disclosure. He argues that AI and vibe coding add weakly secured surfaces, while attackers use AI to scan for and script exploits faster. He points out that XSS and SQL injection are still among the most common attack vectors, so input sanitization remains basic hygiene. WordPress is singled out for CVE volume, with most of its bugs attributed to third-party plugins rather than core. The video then argues for memory-safe languages such as Rust, Go, Java, C#, Python and Swift over C and C++, citing a Google 2025 density figure, and notes the Linux kernel is the most-scrutinized and most-vulnerable OS. It closes with three recommendations (memory safety, AI-driven behavioral monitoring, and minimizing supply-chain dependencies) and a sponsor-style plug for Better Stack's AI error tracking and AI SRE. The stats are stated without sources in the video.

## Key ideas
- **Record vulnerability volume in 2025** — More than 48,000 CVEs were published, the highest count the speaker cites for a single year, with vulnerabilities up about 18% (about 130 new flaws per day). ([0:00](https://youtu.be/__izQwBMqw0?t=0))
- **Exploits are arriving within a day of disclosure** — Roughly 28% of observed exploits in early 2025 were launched within one day of disclosure, so attackers often act before a patch ships. AI-assisted scanning and script generation are cited as making this faster. ([0:00](https://youtu.be/__izQwBMqw0?t=0))
- **AI coding adds weaker security surfaces** — The speaker links vibe coding and AI coding agents to new systems with weaker security measures, on both the defender and attacker sides. ([0:00](https://youtu.be/__izQwBMqw0?t=0))
- **Input sanitization still matters most for web apps** — XSS and SQL injection remain among the most popular attack vectors, so sanitizing input is presented as one of the easiest protections. ([1:08](https://youtu.be/__izQwBMqw0?t=68))
- **Plugins, not WordPress core, carry most WordPress risk** — WordPress has about 7,000 new CVEs. The speaker attributes about 90% of WordPress-related bugs to third-party plugins, about 6% to themes and about 4% to core, so he advises minimal plugins. ([1:08](https://youtu.be/__izQwBMqw0?t=68))
- **Memory-safe languages and code density** — Memory-safe languages are presented as more secure than C, C++ or Assembly. The speaker cites Google 2025 data of about 0.2 vulnerabilities per million lines for Rust versus nearly 1,000 per million lines for historical C/C++ code. The transcript for the 70% figure is garbled. ([2:15](https://youtu.be/__izQwBMqw0?t=135))
- **Linux kernel as the most-scrutinized OS** — The Linux kernel is called the most vulnerable OS, which the speaker attributes to its ubiquity, heavy research scrutiny and open-source visibility rather than to a uniquely weak design. ([3:25](https://youtu.be/__izQwBMqw0?t=205))
- **Three pillars for 2026** — Prioritize memory safety for new development, deploy automated behavioral anomaly detection in real time, and minimize the supply-chain surface by reducing dependencies. ([4:40](https://youtu.be/__izQwBMqw0?t=280))
- **Dependency reduction tied to a named exploit** — The speaker cites the React-to-Shell exploit from last year as an example of third-party code risk, and points to a separate deep-dive video. ([4:40](https://youtu.be/__izQwBMqw0?t=280))

## Techniques
- **Input sanitization against XSS and SQLi** — Sanitize all user-supplied input on web apps and systems; the speaker gives no code or library. *When:* Any web app or API accepting untrusted input, since XSS and SQL injection remain common vectors.
- **Minimize third-party plugins and dependencies** — Use as few plugins, themes and libraries as possible. The speaker's WordPress example: about 90% of bugs come from plugins and about 6% from themes. *When:* Choosing a CMS or framework, or any project where third-party code expands the attack surface.
- **Choose memory-safe languages for new code** — Prefer Rust, Go, Java, C#, Python or Swift over C/C++ for new development. Transitioning away from C/C++ is presented as the most effective way to cut vulnerability density. *When:* Starting a new project, or deciding between C and Rust for a security-sensitive component.
- **Automated behavioral anomaly detection** — Deploy monitoring that uses behavioral analysis to flag anomalies in real time instead of relying on manual review. The speaker mentions Better Stack's AI error tracking and AI SRE as an example, without implementation detail. *When:* Production systems where exploits may be attempted within hours of disclosure.

## Numbers
- More than 48,000 CVEs published last year, the highest count the speaker cites for a single year ([0:00](https://youtu.be/__izQwBMqw0?t=0))
- Vulnerabilities up about 18%, about 130 new flaws per day on average ([0:00](https://youtu.be/__izQwBMqw0?t=0))
- About 28% of observed exploits launched within one day of disclosure (early 2025) ([0:00](https://youtu.be/__izQwBMqw0?t=0))
- WordPress: about 7,000 new vulnerabilities; about 90% of WordPress bugs from plugins, about 6% from themes, about 4% from core ([1:08](https://youtu.be/__izQwBMqw0?t=68))
- About 70% of high-severity vulnerabilities in large codebases are memory-safety issues (garbled in the transcript, so unclear) ([2:15](https://youtu.be/__izQwBMqw0?t=135))
- Google 2025 data: about 0.2 vulnerabilities per million lines of Rust versus nearly 1,000 per million lines of historical C/C++ ([3:25](https://youtu.be/__izQwBMqw0?t=205))

## Hot takes
- Better Stack's own product is pitched as the answer to AI-driven attacks, in the closing recommendation at 4:40, so the monitoring advice is a product plug.
- The figures (48,000 CVEs, 28% within a day, WordPress split, Rust density) are given without citations and are not verified here; the 70% memory-safety claim is garbled in the transcript.
- Attributing the Linux kernel's high count mainly to scrutiny and ubiquity is the speaker's reading, not shown data.
- The video is a short stats roundup with a sponsor-style plug and no reproducible technique, so its substance is thin.

## Tools mentioned
WordPress, Rust, Go, Java, C#, Python, Swift, C, C++, Linux kernel, React (React-to-Shell exploit, as named in the video), Better Stack (AI error tracking, AI SRE)

## Relevance to our work
- **agentos** (1/3): The memory-safety and dependency-reduction points touch AgentOS's Rust proxy and its sandboxed execution (Crucible), but the video covers general web and OS vulnerabilities, not LLM or agent security. → *Audit the dependency count of the Rust proxy and Crucible sandbox components as a supply-chain check, since the video cites third-party code as the main source of risk.*
