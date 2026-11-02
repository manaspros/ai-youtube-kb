# A PHP Bug Just Took Websites Offline Worldwide

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Gxi_n-PtQBo` · [watch](https://youtu.be/Gxi_n-PtQBo) · **date:** 2026-10-22 · **length:** 7:07 · **format:** news · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed) · **orgs:** Better Stack, PHP Foundation, NSA, CISA, FBI, UK NCSC, Cloudflare, Vercel, Chainguard, Wiz, Calif, OpenAI, Watchtower, Railway, Wikimedia, 4chan, Breach Forums, Debian, Ubuntu, WordPress, Drupal, Joomla, Laravel, Google
- **topics:** security-guardrails, dev-tools, governance-compliance · **tags:** php, cve, remote-code-execution, responsible-disclosure, embargo, patching, ai-vulnerability-discovery, php-to-shell, exploit-development, security-incident, cloudflare-waf, supply-chain

> Better Stack news explainer on the "PHP to Shell" pair of PHP bugs (CVSS 9.2 per the video): unauthenticated remote code execution in PHP itself, a coordinated-disclosure mess that pulled the patch forward, and a warning that AI speeds up exploit building.

## Summary
The video covers two PHP core bugs, nicknamed "PHP to Shell," that allow unauthenticated remote code execution. The speaker says the root cause is PHP running out of memory at the wrong moment, leaving half-built data that is later trusted. Patching the application does not help; PHP itself must be updated. Agencies including the NSA, CISA, the FBI and the UK NCSC told organizations to take systems offline if they could not patch, and several sites did. The disclosure went badly: CVE details leaked early with wrong severity, a vendor published a patch before the embargo lifted, and PHP moved the release up a day. Cloudflare and Vercel had pre-built firewall rules. The speaker's main takeaway is that AI has shortened the time from patch to working exploit, so disclosure norms need to change. Much of the attribution dispute (OpenAI, Calif, Wiz) is reported as claims, not verified facts.

## Key ideas
- **The bugs are in PHP itself, not in apps or plugins, so updating the application does not fix them. PHP must be updated.** — The speaker says the bugs are in the language runtime, so a fresh Hello World app is also affected. The speaker says every PHP version from the last decade can be exploited. Older versions may only get patches that users must build themselves. ([0:10](https://youtu.be/Gxi_n-PtQBo?t=10))
- **The mechanism is an out-of-memory condition at the wrong moment, which leaves partially built data that PHP later trusts.** — The speaker paraphrases the PHP Foundation's explanation: if a request runs PHP out of memory at exactly the wrong moment, PHP can leave half-built data behind and later trust it. Combined with the right request, this gives unauthenticated remote code execution. ([0:10](https://youtu.be/Gxi_n-PtQBo?t=10))
- **Disclosure fell apart: details leaked early with wrong severity, a vendor published its patch before the embargo lifted, and PHP pulled the release forward.** — CVE numbers were posted to Hacker News on Tuesday with a wrong severity of 10. PHP then gave advance notice and moved the release up a day. Chainguard published patched PHP images more than six hours before release, which the PHP Foundation said broke the embargo. Calif accidentally published a working exploit video that was later deleted. ([1:00](https://youtu.be/Gxi_n-PtQBo?t=60))
- **Agencies told organizations to take systems offline if they could not patch right away, and many sites went down.** — The NSA, CISA, FBI and UK NCSC all gave this advice. Named casualties include DigiD in the Netherlands, Parliament's website, 4chan, parts of Wikimedia and Breach Forums. The speaker describes this as an unusual response to a bug. ([2:04](https://youtu.be/Gxi_n-PtQBo?t=124))
- **Cloudflare, Vercel and others were told early and quietly built firewall rules, and Cloudflare enabled them for all customers before the patch.** — Cloudflare switched the rules on at 3am UTC on Wednesday and reports watching attackers modify payloads to get around them. Watchtower reports real exploit attempts that use AI-written tooling, but no confirmed success. CISA also reports no successful exploitation yet. ([3:23](https://youtu.be/Gxi_n-PtQBo?t=203))
- **The long tail of unpatched servers is the main risk: one scan found 59% of servers running PHP 8.1 or older.** — Only PHP 8.2 and newer received official releases. The speaker says the Debian and Ubuntu package maintainer shipped fixes back to PHP 7.4, which he calls a good move. ([3:23](https://youtu.be/Gxi_n-PtQBo?t=203))
- **Attribution of the discovery is disputed; the speaker says the bug class dates to 2004 and AI sped up exploit development.** — OpenAI credits Calif's researcher using GPT 5.6 Sol. Wiz says it found the bug independently with help from Gemini 4 Argon. Calif says its researcher was first, and says no special harness was used. A 2024 PHP Foundation audit had flagged the issue without proving it was exploitable. Wiz says one researcher did in a week what would have taken a world-class team months. ([4:40](https://youtu.be/Gxi_n-PtQBo?t=280))
- **AI has changed the disclosure math: a few hours is enough for people with agents to build exploits, so disclosure models built for hard bug-finding no longer fit.** — The speaker quotes Taylor Otwell saying PHP is probably not the last such case. He also quotes OpenAI saying it expects the number of findings to rise sharply in the coming months. Railway reported a breach of customer environment variables the same day, but it has not been linked to this bug. ([5:55](https://youtu.be/Gxi_n-PtQBo?t=355))

## Techniques
- **Immediate PHP runtime patching when a language-level RCE is announced** — The speaker's advice is to update the PHP runtime itself, not the app. Check PHP versions on all servers, including forgotten ones. Versions 8.2+ get official releases. For older versions, use distro packages with backported fixes or build patches yourself. *When:* When a CVE is in PHP core and affects every app regardless of framework or plugins.
- **Take the service offline when an unpatched RCE is live and the patch is not yet available** — Agencies such as the NSA, CISA, FBI and UK NCSC advised taking systems offline if they could not be patched immediately. Some sites did this, and one business disconnected all its servers before the patch. *When:* When a severe unauthenticated RCE is public and you cannot patch within hours. Treat it as a tradeoff between uptime and exposure.
- **Pre-deploy WAF rules before public disclosure** — Cloudflare and Vercel received early notice and built firewall rules first. Cloudflare enabled them for every customer at 3am UTC and then watched attackers adjust payloads. The speaker presents this as a reason the impact was smaller than it could have been. *When:* When a vendor has early access to a vulnerability and wants to block exploitation before the patch is public. Mention it when your platform sits in front of user traffic.

## Numbers
- Disclosed severity of the PHP bugs: 9.2 out of 10 (the speaker's figure; the CVE numbers were initially posted with a wrong severity of 10). ([0:10](https://youtu.be/Gxi_n-PtQBo?t=10))
- PHP runs roughly 70% of the internet. ([0:10](https://youtu.be/Gxi_n-PtQBo?t=10))
- Cloudflare enabled its firewall rules for every customer at 3am UTC on Wednesday. ([3:23](https://youtu.be/Gxi_n-PtQBo?t=203))
- Chainguard published patched PHP images more than six hours before the official release. ([2:04](https://youtu.be/Gxi_n-PtQBo?t=124))
- The patch landed at 2am UTC. ([2:04](https://youtu.be/Gxi_n-PtQBo?t=124))
- 59% of scanned servers show a PHP version of 8.1 or older. ([3:23](https://youtu.be/Gxi_n-PtQBo?t=203))
- Debian and Ubuntu package fixes were backported to PHP 7.4. ([3:23](https://youtu.be/Gxi_n-PtQBo?t=203))
- Wiz says one researcher did in a week what would have taken a world-class team months. ([4:40](https://youtu.be/Gxi_n-PtQBo?t=280))
- The bug class goes back to a 2004 research paper. ([4:40](https://youtu.be/Gxi_n-PtQBo?t=280))
- The 2024 PHP Foundation security audit had already flagged the first signs of the problem. ([4:40](https://youtu.be/Gxi_n-PtQBo?t=280))
- The speaker says about 80 viewers were not subscribed. This is a channel plea, not a finding. ([0:56](https://youtu.be/Gxi_n-PtQBo?t=56))

## Hot takes
- The bug itself was the least interesting part. The real story is that disclosure was built for a world where finding the bug was the hard part, and that world has passed.
- AI has shrunk the time from patch to working exploit to a few hours.
- Attribution claims (OpenAI credits Calif's researcher using GPT 5.6 Sol; Wiz credits Gemini 4 Argon; Calif says its researcher was first) are contested and were not verified in the video.

## Tools mentioned
PHP, Chainguard PHP images, Cloudflare WAF, GPT 5.6 Sol, Gemini 4 Argon, Claude Mythos, Debian packages, Ubuntu packages, WordPress, Drupal, Joomla, Laravel, Hacker News

## Relevance to our work
- **agentos** (1/3):  → *Add a patch-SLA and runtime-version check for the proxy and sandbox images. Review whether Crucible's sandbox images run supported language runtimes.*
