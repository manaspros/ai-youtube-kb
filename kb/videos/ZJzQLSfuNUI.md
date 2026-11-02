# OpenFeature Will CHANGE How You Deploy Code

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ZJzQLSfuNUI` · [watch](https://youtu.be/ZJzQLSfuNUI) · **date:** 2025-11-02 · **length:** 5:25 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** OpenFeature, LaunchDarkly, GrowthBook, Better Stack, OpenTelemetry
- **topics:** dev-tools, observability · **tags:** feature-flags, openfeature, flagd, opentelemetry, a-b-testing, canary-release, react, python, docker-compose, targeting

> A 5-minute Better Stack walkthrough of OpenFeature, a vendor-neutral feature-flag API, showing flagd flags, device-type targeting, and an OpenTelemetry tracing hook.

## Summary
The video introduces OpenFeature as a standard API and rule set for feature flags that works across languages and vendors, so switching providers (the example is LaunchDarkly to GrowthBook) should not require rewriting application code. It explains the evaluation path: the app calls the evaluation API, evaluation context is attached, before-hooks run, the provider fetches flag state from the management system, and after-hooks run before the value reaches the app. The demo wires a Python API and a React app to flagd, an open-source flag engine, using a boolean flag that defaults to false when flagd is unreachable. It then adds targeting: React passes device type (derived from window width) as evaluation context, and a targeting object in the flags JSON turns the feature off for mobile. Finally it adds the OpenTelemetry tracing hook so flag values appear on trace spans, with an OTel collector added to Docker Compose. The walkthrough is short and follows a clear sequence, but it skips the collector config and full flags JSON and gives no tradeoffs or production guidance.

## Key ideas
- **OpenFeature is a vendor-neutral standard API and rule set for feature flags, so the provider can change without rewriting app code.** — The speaker's example is switching from LaunchDarkly to GrowthBook. Works across many languages. ([0:00](https://youtu.be/ZJzQLSfuNUI?t=0))
- **Flag evaluation has a defined pipeline of evaluation API, evaluation context, before-hooks, provider, and after-hooks.** — The provider is the adapter to any flag management system (LaunchDarkly, flagd, etc.). After-hooks run on the result before the value reaches the app. ([0:00](https://youtu.be/ZJzQLSfuNUI?t=0))
- **Safe defaults matter: the boolean evaluation takes a default value that is used when the flag engine is down.** — The demo sets the default to false. The backend returns 404 when the flag is not found and the payment-success response when it is. ([1:26](https://youtu.be/ZJzQLSfuNUI?t=86))
- **Flag changes in flagd take effect without a page refresh.** — The speaker edits the flags JSON while the app is open and the feature appears on the next click, with no reload. ([2:51](https://youtu.be/ZJzQLSfuNUI?t=171))
- **Targeting is driven by evaluation context sent from the client, which makes device-type rollouts possible.** — React sends device type derived from window width. A targeting object in the flags JSON sets the flag off when device type is mobile. The speaker notes the same mechanism can use user ID, user agent, or any other value for A/B tests and canary rollouts. ([2:51](https://youtu.be/ZJzQLSfuNUI?t=171))
- **Flag evaluation data can be attached to OpenTelemetry trace spans through a tracing hook.** — The hook fires after the provider returns the flag state. Hooks can also run before evaluation. Once the collector is in Docker Compose, each API call's trace span includes flag data. ([4:16](https://youtu.be/ZJzQLSfuNUI?t=256))

## Techniques
- **Backend OpenFeature setup with flagd** — Install the OpenFeature SDK and the flagd provider in the Python API. Configure OpenFeature with a provider and a client. Get a boolean with the flag name and default false, return 404 when the flag is missing, and return the success response when it is on. Run flagd with Docker Compose and point its flags JSON at a flag with on and off variants, default variant off. *When:* Replacing hard-coded feature checks in a service so the flag source can change later without code edits.
- **React client setup with the flagd web provider** — Install the OpenFeature React SDK and the flagd web provider. Set the provider to flagd on localhost port 8013. Wrap the app in the OpenFeature provider component. In components, call the useFlag hook with the flag name and a default value, then render with a ternary that shows the feature only when the flag exists. *When:* Gating UI features behind a flag while the flag can be toggled live in flagd.
- **Device-type targeting via evaluation context** — On the client, pass an evaluation context object whose device-type field is derived from window width. In the flags JSON, add a targeting object that checks device type equals mobile and returns the off variant when it matches, and the on variant otherwise. Refresh to test each width. *When:* A/B tests or canary rollouts that need segmentation by user attribute, such as device, user ID, or user agent.
- **Flag data on OpenTelemetry traces** — Add the OpenTelemetry packages and an exporter function that sends trace data to the OTel collector. Install the OpenFeature tracing hook and add it to the OpenFeature client. Add an OTel collector service to docker-compose.yml with its configuration (the speaker does not show the file contents). *When:* Debugging whether a request's behaviour came from a particular flag value, by filtering traces on flag attributes.

## Numbers
- flagd is configured to listen on localhost port 8013 for the React client. ([1:26](https://youtu.be/ZJzQLSfuNUI?t=86))
- Boolean flag evaluation uses default value false when flagd is unavailable. ([1:26](https://youtu.be/ZJzQLSfuNUI?t=86))
- Flag variants are on (true) and off (false), with the default variant set to off. ([2:51](https://youtu.be/ZJzQLSfuNUI?t=171))
- Video length is 5:25. No benchmarks, costs or adoption figures are given. ([0:00](https://youtu.be/ZJzQLSfuNUI?t=0))

## Hot takes
- OpenFeature's vendor-neutral API means flag providers can be swapped without changing application code.
- Title promises it will change how you deploy code, but the content is a basic setup tutorial.

## Tools mentioned
OpenFeature, OpenFeature SDK (Python), OpenFeature React SDK, flagd, flagd web provider, OpenTelemetry (traces), OpenTelemetry Collector, Docker Compose, React, LaunchDarkly, GrowthBook

## Relevance to our work
- **agentos** (1/3): L4 observability uses OTel. Per-request flag or pillar-config values on trace spans would help debugging, but AgentOS toggles pillars through a manifest rather than a flag service. → *Attach the active manifest pillar settings or flag-style toggle values as attributes on OTel spans so traces show which configuration each request ran under.*
