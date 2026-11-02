# This AI Code Builder ACTUALLY Works (backend too!)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `4ASZpNNG0f4` · [watch](https://youtu.be/4ASZpNNG0f4) · **date:** 2025-11-02 · **length:** 8:44 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Convex, StackBlitz, Google, Supabase, Anthropic
- **topics:** vibe-coding-app-building, dev-tools · **tags:** Chef by Convex, Convex, Bolt.new, Firebase Studio, v0, Supabase, BYOK Anthropic key, auth, file storage, app builder comparison, self-hostable backend, row level security

> Hands-on test of AI app builders on one backend-heavy prompt; Convex's Chef produced working auth, storage and database from a single prompt, while Firebase Studio, Bolt.new (with Supabase) and v0 failed or stalled.

## Summary
The host gives Chef by Convex (an AI app builder that the speaker assumes is a fork of open-source Bolt.new) one long prompt asking for an A/B image-voting app with login, image storage, a one-hour test duration and login-required voting. Chef generated the app, ran and fixed a failing type check, deployed to Convex in about five seconds, and the speaker reports auth, file storage, the database and voting all working without a follow-up prompt. Chef also lets users supply their own Anthropic API key, so Convex token usage is not billed, and the Convex backend is open source and self-hostable. The same prompt in Firebase Studio (preview) produced only a placeholder page, and in Bolt.new with Supabase it spent 5 to 10 minutes retrying, then failed at sign-up with a "sign up is not a function" error. v0 produced a surprise £20 charge, and its Supabase version let the user sign up but failed on test creation with a row-level-security policy violation. The speaker concludes that Chef is the strongest of the four, but this is a single-run, one-prompt comparison with no repeated trials.

## Key ideas
- **Chef by Convex builds the full stack from one prompt, including auth, file storage, database and voting, with no follow-up prompts needed, according to the speaker.** — The app is an A/B image test with login-required voting and a one-hour duration. The speaker checks sign-up, sign-in, test creation, voting and results across two users and says the backend features were all wired up. ([2:34](https://youtu.be/4ASZpNNG0f4?t=154))
- **Deployment to Convex is near-instant, and the Convex dashboard exposes the tables, functions, logs, schedules and files the builder created.** — The deploy step took about five seconds. Auto-generated tables included auth rate limits, tests, users and votes, along with functions such as sign in and sign out. ([0:00](https://youtu.be/4ASZpNNG0f4?t=0))
- **Convex's pitch for AI builders is that the whole backend is defined in TypeScript, and the Convex backend is open source and self-hostable, which the speaker cites as protection against vendor lock-in.** — The speaker frames this as the reason Convex is well suited to end-to-end AI app generation, since the agent can express the backend as code. ([0:00](https://youtu.be/4ASZpNNG0f4?t=0))
- **Chef accepts the user's own Anthropic API key, so token spend goes to Anthropic and not Convex. The free Convex tier also has a usage cap.** — The key is added under Settings, in the API key section. The speaker's free-tier account showed 19M tokens used against an 18M quota at the time of the video. Paid Convex plans include more usage. ([1:18](https://youtu.be/4ASZpNNG0f4?t=78))
- **Firebase Studio, then in preview, returned a blueprint describing the requested features but generated only a single placeholder page.** — The speaker inspected the generated files and found only the page. The speaker says there was no clear reason why. ([6:19](https://youtu.be/4ASZpNNG0f4?t=379))
- **Bolt.new with a Supabase backend ran into repeated errors while generating, and sign-up then failed with a runtime error.** — Generation took five to ten minutes of retries. The final sign-up failed with a 'sign up is not a function' error at the form handler. ([6:19](https://youtu.be/4ASZpNNG0f4?t=379))
- **v0 succeeded on sign-up through Supabase, but test creation failed on a row-level-security policy violation. The speaker also reports an unexpected £20 charge on v0.** — The failure shows the generated app did not configure the Supabase RLS policies needed for inserts. The speaker's conclusion is that Chef is the winner, with a caveat that Firebase is still in preview. ([7:13](https://youtu.be/4ASZpNNG0f4?t=433))

## Techniques
- **One long, feature-complete prompt, then test each feature end to end** — Write one prompt that lists the app, the auth requirement, storage needs and specific behaviours (duration, login-required voting). Generate, deploy, then exercise sign-up, sign-in, create, vote and results with two separate user accounts. Check the backend dashboard (tables, functions, logs, schedules, file storage) to confirm the backend was actually provisioned. *When:* Evaluating an AI app builder's backend capability, or checking whether a generated app actually works beyond the preview.
- **Bring your own model key to avoid builder token markup** — In Chef, open Settings, scroll to the API key section, and paste an Anthropic API key. Generation then bills Anthropic directly, and the built-in free token allowance is no longer needed. *When:* You want to use an AI app builder without paying its per-token fees, or you have an existing model account with credit.

## Numbers
- Convex deploy of the generated app took about five seconds. ([2:34](https://youtu.be/4ASZpNNG0f4?t=154))
- Free Convex tier showed 19M tokens used against an 18M quota. ([4:58](https://youtu.be/4ASZpNNG0f4?t=298))
- Bolt.new with Supabase took about 5 to 10 minutes of retries before producing a result. ([6:19](https://youtu.be/4ASZpNNG0f4?t=379))
- v0 charged the speaker £20 for an integration they did not expect. ([7:13](https://youtu.be/4ASZpNNG0f4?t=433))

## Hot takes
- Chef by Convex is 'the absolute winner' and 'the next step in AI builders', based on one run per tool with a single prompt.
- Firebase Studio is still in preview, but it could catch up by adding Firebase Auth, databases and deployment, so it is not out of the race.
- Builders that promise 'add this in later' for backend features are 'very annoying', a complaint about the status quo rather than a measured finding.

## Tools mentioned
Chef by Convex, Convex (backend, dashboard, file storage, auth, durable functions), Bolt.new, Firebase Studio (preview), v0, Supabase, Anthropic API (BYOK)
