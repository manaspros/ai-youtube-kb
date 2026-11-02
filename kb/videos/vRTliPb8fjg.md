# I Let Strix Attack My App... Here’s What It Found

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `vRTliPb8fjg` · [watch](https://youtu.be/vRTliPb8fjg) · **date:** 2026-08-02 · **length:** 5:42 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed) · **orgs:** Better Stack, Anthropic, Google, Ollama, GitHub
- **topics:** security-guardrails, pr-code-review, sandboxing-execution · **tags:** pen-testing, strix, ai-security, docker, github-actions, ci-gating, owasp, validated-findings, autofix-pr, fastapi

> Short Better Stack review of Strix, an open-source multi-agent pen-testing tool that attacks a web app or API in a Docker sandbox and returns validated exploits and fix PRs, with real limits on cost, speed and complex attacks.

## Summary
The host demos Strix, an open-source (Apache 2.0 per the talk) multi-agent security tool that acts like a team of hackers: one agent maps the app, others target OWASP Top 10 issues such as SQL injection, XSS and broken access control. Setup is a one-line curl install, and scans run in a Docker sandbox that is pulled on first run. The demo runs a quick-mode scan against a small FastAPI expense app, using both the code path and a live URL, with an Anthropic model; the scan took about 10 minutes. Strix's key claim is that it only reports vulnerabilities it has exploited, returning the endpoint, a working exploit, the extracted data, reproduction steps and a fix. It can chain attacks and open autofix pull requests, and it has a CLI with native GitHub Actions support that exits non-zero on findings so CI can block a merge. The host cites a 96% solve rate on the XBEN exploitation benchmark at about 19 minutes per challenge, a figure not verified in the video. The main caveats are that output quality depends on the model (weak local models give weak findings), a quick scan costs roughly $3-5 in tokens, deep scans take hours, Docker adds friction, and complex logic or long attack chains are not handled well. The host's advice is to use it for pre-merge checks, side projects and staging, as one layer alongside existing scanners and human review.

## Key ideas
- **Strix is an open-source multi-agent pen-testing tool (about 38k GitHub stars) that behaves like a crew of hackers rather than a single model guessing** — One agent does recon and maps the app; others target OWASP Top 10 classes such as SQL injection, XSS and broken access control in APIs. ([0:00](https://youtu.be/vRTliPb8fjg?t=0))
- **It reports only exploited vulnerabilities, not possible ones** — Each finding comes with a working exploit, the data pulled, exact reproduction steps and a suggested fix, which the host contrasts with scanners that say 'this might be exploitable'. ([1:02](https://youtu.be/vRTliPb8fjg?t=62))
- **Setup is a one-line curl install; the run needs Docker, and the first run pulls a sandbox image** — The sandbox lets agents act without affecting real systems. The host stresses testing only systems you have permission to test. ([1:02](https://youtu.be/vRTliPb8fjg?t=62))
- **Quick mode takes about 10 minutes on a small app and uses tokens; deeper modes run much longer** — The host says a quick scan of their demo app took about 10 minutes, and deep mode can take hours and use far more tokens. ([2:21](https://youtu.be/vRTliPb8fjg?t=141))
- **Agents chain attacks, run sandboxed, and can open autofix pull requests** — The loop closes from finding to fix PR, which is the main differentiator the host draws against manual pen tests (accurate but slow and pricey) and static scanners (fast but never run the code). ([3:21](https://youtu.be/vRTliPb8fjg?t=201))
- **CI integration exits with an error code on findings, so a bad merge can be blocked** — The CLI supports GitHub Actions natively. The host frames 'validated findings' as the key feature because it removes the pile of unverified maybes. ([3:21](https://youtu.be/vRTliPb8fjg?t=201))
- **Output quality is bounded by the model you supply** — Brings your own model (Claude, Gemini, or a local Ollama model). A weak local model gives weak findings, a strong one costs a lot of tokens, and a quick scan is budgeted at about $3-5. ([3:21](https://youtu.be/vRTliPb8fjg?t=201))
- **Positioning: a layer, not a replacement for a human pen test** — Suggested uses are pre-merge checks, side projects and staging; complex logic and long chained attacks are still weak, so it should sit beside existing scanners and human review. ([4:46](https://youtu.be/vRTliPb8fjg?t=286))

## Techniques
- **Scan code and live target together in one run** — Point the CLI at the running app URL and the project code path in one command, choose a scan mode (quick first; the speaker says deeper modes cost more tokens and time), and choose the model provider (Anthropic API used in the demo; Gemini or a local Ollama model also supported). Docker must be running. Exact flag names are not shown in the video. *When:* Staging or side projects where you want coverage of both source and runtime behavior before production.
- **CI merge gate on validated findings** — Add the Strix CLI as a GitHub Actions step on pull requests; the step exits non-zero when it finds a validated vulnerability, which fails the check and blocks the merge. *When:* Pre-merge checks on routine, repeatable changes, sitting next to existing scanners.
- **Triage on proof, not on maybes** — Accept only findings that include a working exploit and reproduction steps, and review the proposed autofix PR as you would any other change. *When:* Any time scanner output is noisy and you need to decide what to fix first.
- **Match model strength to scan depth and budget** — Use a stronger hosted model for real findings; a local Ollama model keeps data local but the speaker warns it gives weaker results. Budget roughly $3-5 for a quick scan on a small project, and expect more for larger projects. *When:* Choosing between cost, privacy and finding quality for a given scan.

## Numbers
- Strix has almost 38,000 GitHub stars ([0:00](https://youtu.be/vRTliPb8fjg?t=0))
- Quick scan of the demo app took about 10 minutes ([2:21](https://youtu.be/vRTliPb8fjg?t=141))
- Claimed 96% solve rate on the XBEN exploitation benchmark, about 19 minutes per challenge (vendor or benchmark figure, not checked in the video) ([3:21](https://youtu.be/vRTliPb8fjg?t=201))
- Budget of about $3-5 for a quick scan, depending on project size ([3:21](https://youtu.be/vRTliPb8fjg?t=201))
- Deep scans take hours rather than minutes ([3:21](https://youtu.be/vRTliPb8fjg?t=201))

## Hot takes
- Security tooling should show exploit proof; 'maybe' findings are noise. The host treats validated findings as the main reason to use Strix.
- Running an AI pen tester is like renting a hacker for a few minutes: its quality depends entirely on the model you pay for.
- Strix is a strong layer, not a single wall, and not a stand-in for a human pen test on critical systems.
- The 96% benchmark figure is cited without verification in the video; treat it as a claim.

## Tools mentioned
Strix, Docker, Anthropic API (Claude), Gemini, Ollama, GitHub Actions, FastAPI (demo app), XBEN exploitation benchmark, OWASP Top 10

## Relevance to our work
- **agentos** (1/3): Strix-style exploit validation is a pattern for testing the proxy and the exec-gate guardrails, but the video is a short tool demo with no architecture detail. → *Consider a one-off Strix run against the AgentOS gateway proxy in a staging setup to see what it finds on the proxy's own API surface.*
