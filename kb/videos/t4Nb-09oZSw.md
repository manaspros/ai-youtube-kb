# How to Setup Uptime Kuma - Self Hosted Monitoring

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `t4Nb-09oZSw` · [watch](https://youtu.be/t4Nb-09oZSw) · **date:** 2024-11-02 · **length:** 20:58 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed) · **orgs:** Better Stack
- **topics:** dev-tools, observability, infra-cost-scaling · **tags:** uptime-monitoring, uptime-kuma, self-hosting, docker, status-page, incident-management, keyword-check, retries, on-call, better-stack

> Walkthrough of self-hosting Uptime Kuma with Docker to monitor sites, then building public status pages and incidents. The back half pitches Better Stack's managed service.

## Summary
The host installs Uptime Kuma, a self-hosted open-source uptime monitor, with Docker and shows the admin setup and dashboard. He walks through HTTP(s), keyword and upside-down monitor settings, retries, timeouts, certificate alerts and accepted status codes, then forces a site outage to show down and recovery states. He builds a public status page with branding, custom CSS, and a manually posted incident. The second half is a Better Stack pitch covering multi-location checks, Playwright scenarios, on-call escalation, recovery periods, and a hosted status page. The concrete self-hosting content is practical but shallow and has no code beyond the README's Docker command.

## Key ideas
- **Uptime Kuma is a self-hosted open-source monitor for websites, APIs, DNS and other services, with 70+ notification integrations and built-in public status pages.** — The host cites about 55,000 GitHub stars and lists email, Slack and Discord among the notification options. ([0:00](https://youtu.be/t4Nb-09oZSw?t=0))
- **Monitoring a service on the host's localhost from inside Docker needs host networking.** — Without --network=host, localhost inside the container refers to the container itself, so a service on localhost:3000 is unreachable from Uptime Kuma. He says he skips this because his target is on the LAN. ([1:23](https://youtu.be/t4Nb-09oZSw?t=83))
- **A keyword check marks a service down when a keyword is missing from the response, and upside-down mode inverts the result.** — This works on HTML or JSON responses. Upside-down mode can assert a keyword is absent, for example by marking the site down if 'Hello World' appears. ([3:37](https://youtu.be/t4Nb-09oZSw?t=217))
- **Retries and a separate retry interval keep a single failed heartbeat from flipping the service to down.** — With retries set to 3 and the retry interval dropped from 60s to 10s, a failure is retried three times before the service is marked down. ([3:37](https://youtu.be/t4Nb-09oZSw?t=217))
- **Uptime Kuma records heartbeat history only on status changes, not on every check.** — The response-time graph shows every check, but the status list only logs transitions such as up, down, and back up. ([6:51](https://youtu.be/t4Nb-09oZSw?t=411))
- **Status pages are public-facing and separate from the admin dashboard. Manual incidents are posted there, and open pages refresh only every five minutes.** — The host creates a status page with a slug, adds the monitor as a resource, and posts an incident with a title and description. Refreshing the page forces an update. ([9:55](https://youtu.be/t4Nb-09oZSw?t=595))
- **Better Stack's managed pitch: monitors and status pages do not depend on your own infrastructure. Its checks are verified from several regions, and on-call escalation is built in.** — The host says each HTTP or ping incident is verified from at least three locations before alerting. He also describes Playwright scenarios, escalation after a few minutes without acknowledgment, and a recovery period before auto-resolve. ([12:21](https://youtu.be/t4Nb-09oZSw?t=741))
- **A recovery period auto-resolves an incident only after the monitor stays up for the set time.** — In the example it is three minutes. After the site came back, the incident sat in a validating state until that window passed or the host resolved it manually. ([14:25](https://youtu.be/t4Nb-09oZSw?t=865))

## Techniques
- **Uptime Kuma Docker install** — Copy the Docker command from the GitHub README and run it in a terminal. The container then serves the UI on port 3001, reachable at localhost:3001 or the host IP and port. Create an admin account on first load. For Docker container monitoring, bind an extra volume as documented in the project wiki (not shown in the video). Non-Docker alternative: Node with PM2. Add --network=host only when monitoring services bound to the host's localhost. The exact flags were not shown on screen beyond that. *When:* Self-hosting a monitor on a machine you control, when you want to monitor services on the same LAN or host.
- **HTTP(s) monitor settings** — Monitor type HTTP(s), a friendly name, and the URL (the video uses a LAN address with port 4173). Set heartbeat interval (default 60s), retries (example 3), retry interval (example 10s, down from 60s), request timeout (default 48s), and resend-notification-every-N-down. Advanced: certificate-expiry notification, ignore TLS errors for local targets, upside-down mode, max redirects, and accepted status codes (default 200-299). For APIs, set the HTTP method, body and headers. Attach notification channels, then save to run the first check. *When:* Basic up/down monitoring of websites and APIs where you want to reduce false alarms from transient failures.
- **Keyword check** — Choose the keyword monitor type, set the URL and the keyword. It searches the HTML or the JSON body and marks the service down if the keyword is missing. Enable upside-down mode to alert when the keyword is present instead, such as to catch unwanted text on a page. *When:* Detecting broken content behind a 200 response, or asserting a string such as a version or a health flag in an API response.
- **Status page setup** — Open Status Pages, click New status page, set a name and slug, then configure the title, description and footer (both Markdown), theme (auto, light or dark), show tags, show powered-by, certificate expiry, domain names, Google Analytics ID, and custom CSS. Add a section and drag monitors in as resources. Post incidents from edit mode with a title and description. The Better Stack equivalent includes a custom domain, a logo link, a get-in-touch link, a pinned announcement, a minimum incident length (example 30s), and embeds for badges or announcements. *When:* Sharing service health with users or internal stakeholders while keeping the monitor separate from the app being monitored.
- **Better Stack escalation and recovery** — Create a monitor for 'if the URL becomes unavailable' or keyword matching, or a Playwright scenario for custom checks. Pick check regions (defaults to all). Build an on-call escalation policy with email, SMS or push, and an escalation step (example: escalate if not acknowledged within 3 minutes). Set the recovery period (example 3 minutes) before an incident auto-resolves. Acknowledging an incident stops repeat alerts. *When:* Team-facing alerting where you need multi-region confirmation, acknowledgment-based escalation, and a status page hosted outside your own infrastructure.

## Numbers
- Uptime Kuma has about 55,000 GitHub stars (as stated by the host). ([0:00](https://youtu.be/t4Nb-09oZSw?t=0))
- Default heartbeat interval is 60 seconds. ([3:37](https://youtu.be/t4Nb-09oZSw?t=217))
- Example retry setup: retries 3, retry interval changed from 60s to 10s. ([3:37](https://youtu.be/t4Nb-09oZSw?t=217))
- Default request timeout is 48 seconds. ([4:42](https://youtu.be/t4Nb-09oZSw?t=282))
- Default accepted status codes are 200-299. ([5:41](https://youtu.be/t4Nb-09oZSw?t=341))
- Example response time for a local site was 10 ms. ([6:51](https://youtu.be/t4Nb-09oZSw?t=411))
- Uptime Kuma offers more than 70 notification integrations. ([6:51](https://youtu.be/t4Nb-09oZSw?t=411))
- Public status pages refresh about every five minutes while open. ([9:55](https://youtu.be/t4Nb-09oZSw?t=595))
- Better Stack verifies each HTTP or ping incident from at least three locations before alerting (as claimed by the host). ([12:21](https://youtu.be/t4Nb-09oZSw?t=741))
- Example on-call escalation: escalate if not acknowledged within 3 minutes. Example recovery period: 3 minutes before auto-resolve. ([14:25](https://youtu.be/t4Nb-09oZSw?t=865))

## Hot takes
- Vendor pitch: the back half (about 12:21 to 19:56) promotes Better Stack's managed service and its feature list. The claims about multi-location verification and escalation are the host's own and were not checked.
- Thin substance: the self-hosting part is a GUI walkthrough with no config files and only one shell command, mostly copied from the README. Anyone who has used a monitor before gets little new information.
- Useful framing: a monitor and its status page should not run on the infrastructure they monitor. The host says this, though he implies it is a reason to pay for a managed service rather than a general rule.
- Retries plus a separate retry interval are the most practical idea here for cutting false down alerts. The video does not explain how this interacts with resend-notification settings.

## Tools mentioned
Uptime Kuma, Docker, Node.js, PM2, Better Stack, Playwright, Plausible, Google Analytics, Discord, Slack

## Relevance to our work
- **agentos** (1/3): AgentOS L4 covers observability with Prometheus, Grafana, OTel and Locust, but external liveness monitoring of the L1 proxy is not covered. A cheap uptime checker sits outside that stack. → *Add an external HTTP monitor with retries (not a single failed check) against the Govrix Scout proxy health endpoint on :4000, so downtime alerts do not depend on the proxy being up.*
