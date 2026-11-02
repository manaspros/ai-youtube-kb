# Add an Uptime Badge to ANY Website

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `r43TKZspxzo` · [watch](https://youtu.be/r43TKZspxzo) · **date:** 2025-11-02 · **length:** 8:34 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Nextforge
- **topics:** observability, dev-tools · **tags:** uptime-monitoring, status-page, status-badge, nextjs, server-components, api-tokens, tailwind, react, curl, jq

> Better Stack walkthrough: set up uptime monitors and a status page, then build a custom status badge in Next.js that reads monitor-group status from the Better Stack API.

## Summary
The presenter wants a public status badge so customers see incidents without flooding support. They create HTTP uptime monitors for three endpoints (landing page, dashboard app, API) in Better Stack, check every 30 seconds, and set an escalation path: email the on-call person, then alert the whole team if nobody acknowledges within three minutes. The monitors are grouped under one "demo" group, and a status page is built from them in the Structure tab. The simplest badge is an iframe copied from the status page's advanced settings. For a custom badge, the presenter creates a team-scoped uptime API token, stores the API key and the status page URL as environment variables, and calls the API from a Next.js server component so the key never reaches the client. The flow is: list monitor groups to get the group ID, then list the monitors in that group, which return each monitor's status. A React component with Tailwind counts monitors whose status is "up" and maps the ratio to all normal, partial outage, or major outage. The presenter suggests a reduce-based status-count object for finer labels. The video is short, mostly UI clicking, and the badge logic is only a few lines.

## Key ideas
- **Create one HTTP uptime monitor per endpoint (landing page, app, API) and set an escalation policy.** — Monitors fire when the URL becomes unavailable and can also check for a keyword, an unexpected HTTP status code, or a failing Playwright scenario. Checks run every 30 seconds. Alerts go by email first, then to the whole team if nobody acknowledges within 3 minutes. ([0:57](https://youtu.be/r43TKZspxzo?t=57))
- **Group monitors and build a status page from them.** — Monitors are grouped under one name ("demo") for organization. The status page's Structure tab adds a section ("services") that lists the monitors. The page shows uptime and can also host maintenance notices and incident history. ([1:50](https://youtu.be/r43TKZspxzo?t=110))
- **Two badge options: copy an iframe (easy) or build a custom badge from the API (customizable).** — The easy path copies the embeddable badge iframe from the status page's advanced settings. The custom path uses the Better Stack API with a team-scoped uptime token. ([2:51](https://youtu.be/r43TKZspxzo?t=171))
- **Keep the API key on the server.** — The presenter says never to expose API keys in client code. Use a backend or server components to make the call. The fetch pattern works in any framework; Next.js server components are used in the demo. ([3:52](https://youtu.be/r43TKZspxzo?t=232))
- **Discover IDs with the API docs' example curl commands, then fetch group status.** — Run the list-monitor-groups example (pre-filled with the token) to find the group ID. Then run the list-monitors-of-a-group example, which returns each monitor's attributes, including its checked URL and status. Possible statuses are up, down, validating, paused, and pending. ([4:57](https://youtu.be/r43TKZspxzo?t=297))
- **Derive the badge label from the monitor statuses.** — Counting the monitors with status up and dividing by the total gives all normal, partial outage, or major outage. A reduce that counts each status type gives more flexibility, for example a stricter label for a high-priority API. ([6:06](https://youtu.be/r43TKZspxzo?t=366))
- **Status logic is the only real code in the tutorial, and it is customizable.** — Mapping over the returned monitors can list each system. Labels can depend on which monitor is down, so a critical service can escalate to major outage on its own. ([7:17](https://youtu.be/r43TKZspxzo?t=437))

## Techniques
- **Server-side fetch of a status API** — In a Next.js server component (or your own backend route), call the monitor-group endpoint with the API token from an env var, and return only the derived status to the client. The token stays out of client bundles. *When:* Any third-party status or monitoring API that needs a secret key on a public site.
- **Derive a status label from monitor counts** — Filter monitors where status === 'up' and compare the count with the total. All up = all systems normal; some down = partial outage; all down = major outage. For more detail, reduce the monitors into an object of counts per status (up, down, validating, paused, pending) and map those counts to labels. *When:* A custom status badge or dashboard tile that should summarize many checks in one label.
- **Discover IDs from API example requests** — Open the API docs, select the team so the example curl is pre-filled with your token, copy it, run it in a terminal, and pipe to jq for readable JSON. Run the list-monitor-groups call to get the group ID, paste that ID into the list-monitors-of-a-group example, and run that to see each monitor's status. *When:* Wiring any REST API where you need IDs before you can call the endpoint you actually want.
- **Env config for badge** — Two env vars: the Better Stack API key (server-only) and the status page URL, used as the badge's click target so visitors can open the full status page. *When:* Any badge or widget that links to a hosted status page.
- **Escalation policy on uptime monitors** — Set the first notification channel (email here), then add a rule that alerts all team members if the on-call person does not acknowledge within a set time (3 minutes in the demo). *When:* Any service where an unacknowledged alert should not sit unseen.

## Numbers
- Monitor check interval is 30 seconds. ([0:57](https://youtu.be/r43TKZspxzo?t=57))
- Escalation to the whole team happens if the on-call person does not acknowledge within 3 minutes. ([0:57](https://youtu.be/r43TKZspxzo?t=57))
- Demo uses 3 monitors (landing page, app, API). Status page shows 100% uptime after setup. ([1:50](https://youtu.be/r43TKZspxzo?t=110))
- Status ratio example: 2 of 3 monitors up gives a partial outage label. ([6:06](https://youtu.be/r43TKZspxzo?t=366))
- Monitor status values listed in the API: up, down, validating, pause, pending. ([4:57](https://youtu.be/r43TKZspxzo?t=297))

## Hot takes
- The status badge is mainly a marketing and trust feature. The video says it turns incidents into a positive customer experience. Customer-facing status pages are presented as a support-load reducer.
- The easy iframe badge is enough for most sites. The custom API badge is only worth it for custom layout or label logic.
- The presenter's own product (Better Stack) is the only monitoring tool shown, with no comparison. The Nextforge plug at 8:16 is a template shout-out, not a sponsored segment.

## Tools mentioned
Better Stack (uptime monitors, status pages, API tokens, monitor groups API), Next.js (server components), React, Tailwind CSS, curl, jq, Nextforge (Next.js template that includes a Better Stack system status component; plugged, no version given)

## Relevance to our work
- **agentos** (1/3):  → *Add one external HTTP uptime monitor for the AgentOS proxy health endpoint and compare its alerts with the Prometheus alerting.*
