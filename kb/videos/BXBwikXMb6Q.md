# Why Isn't Anyone Talking About This Vibe Coding Tool?

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `BXBwikXMb6Q` · [watch](https://youtu.be/BXBwikXMb6Q) · **date:** 2025-11-02 · **length:** 11:20 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Convex, Vercel, Supabase, Anthropic, OpenAI, Lovable, StackBlitz
- **topics:** vibe-coding-app-building, dev-tools · **tags:** chef, convex, vibe-coding, prompt-quality, byok, typescript, react, full-stack-generation, splitwise-clone, no-image-input

> A walkthrough of Convex's Chef, a prompt-to-full-stack-app builder, using it to make a Splitwise clone and a tool-rental app; the main takeaways are that prompt detail up front matters and that text-only prompting is a real limitation.

## Summary
The creator argues that AI app builders like Lovable and Bolt are weak on backend, and that Convex (via its Chef builder) is a better backend for AI-generated apps than Supabase. He demos a Splitwise-style expense app built from a detailed prompt, showing auth, group creation, expenses, payments and balances. A first attempt with the default prompt was missing features, so a more comprehensive prompt was needed. Balances were initially wrong until he hit the token limit, added his own Anthropic API key in the settings, and re-prompted, after which the balances were correct. He then builds a tool-rental app ("Neighbor Gear") from a prompt drafted in ChatGPT, tests a one-day booking priced at $80, and argues that a TypeScript/React backend suits AI models because of their training data. The main criticisms are that Chef does not accept images in prompts, which makes UI fixes tedious, and that the only paid plan he saw was $25. Substance is mostly a single-tool walkthrough, with the Convex-is-best claim unsupported by comparison.

## Key ideas
- **The creator claims Convex is the best backend for AI-built apps, and says Lovable's Supabase backend is less seamless when AI models are involved. He gives no head-to-head comparison.** — Frames Chef (Convex's builder) as a full-stack tool; Lovable is cited as a builder that depends on Supabase for its backend. ([0:00](https://youtu.be/BXBwikXMb6Q?t=0))
- **Prompt detail up front matters most. A default-prompt attempt at a Splitwise clone lacked features, and a more comprehensive prompt produced a working version.** — He argues that adding major features later gets harder and breaks more often, so the first prompt should be thorough. ([1:27](https://youtu.be/BXBwikXMb6Q?t=87))
- **Chef generates the backend schema along with the frontend. The demo shows auth (including anonymous login), group creation, adding unregistered members, expenses and payments.** — The Convex dashboard shows tables and schemas generated automatically; a duplicate group appeared because of earlier anonymous-login test sessions. ([2:46](https://youtu.be/BXBwikXMb6Q?t=166))
- **Balances were wrong after the first build. Running out of tokens led him to add his own Anthropic API key, and re-prompting fixed the balances.** — The re-prompt ran on Claude, and the balances then matched the expected split. A later $100 dinner expense and $50 payment both reconciled to zero. ([4:07](https://youtu.be/BXBwikXMb6Q?t=247))
- **Text-only prompting is a major drawback. Images and mockups cannot be uploaded, so UI inconsistencies (theme not matching across pages) take many text-based fixes.** — He says an earlier version needed manual layout tweaks because the prompt had no visual reference. ([5:27](https://youtu.be/BXBwikXMb6Q?t=327))
- **Starting from a preset, then tailoring it, was his workflow for the first app. He then built a new app, Neighbor Gear, from a prompt drafted in ChatGPT.** — The preset gave a Splitwise-style foundation that needed a few prompt adjustments to work. ([6:52](https://youtu.be/BXBwikXMb6Q?t=412))
- **His argument for the stack: Convex uses TypeScript on the backend and React on the frontend, and models are heavily trained on that combination, so they edit it accurately. The generated code can be downloaded and run locally.** — This is his own reasoning, not a benchmark; he calls the approach a 'backend for AI'. ([8:06](https://youtu.be/BXBwikXMb6Q?t=486))
- **The generated app includes a built-in database and is hostable. A booking flow on the rental app computed an $80 price for a one-day rental.** — Booking test: start date May 20, one-day period, price calculated immediately. ([10:25](https://youtu.be/BXBwikXMb6Q?t=625))

## Techniques
- **Front-load a comprehensive prompt** — Write one detailed prompt that lists every required feature (auth, groups, expenses, payments, balances) before generation. Avoid relying on later feature additions, which he found break more easily. *When:* Starting a full-stack app in a prompt-to-app builder where the first prompt sets the baseline.
- **Bring your own API key when quota runs out, then re-prompt** — When the builder shows a token-limit message, open the API Keys section of the settings, add your own Anthropic API key, then resend the same prompt. The builder then uses Claude and the previously wrong output was corrected. *When:* The built-in token allowance is exhausted mid-project, and you want to keep iterating without the paid plan.
- **Start from a preset and adjust the prompt** — Pick a built-in preset that matches the app type (he used a Splitwise-style one), then edit the prompt to fill in the missing features before generating. *When:* A close-enough template exists and you want a working base quickly.
- **Verify by walking through the core flows** — After generation, test the core money or booking flows in the preview (add an expense, record a payment, confirm balances return to zero; set a booking date and duration, confirm the price). He checks the outputs by hand rather than with an automated test. *When:* Validating a generated app with business logic such as balances or pricing.
- **Export and run locally** — Download the generated source and run it on your own machine. He says this needs no additional setup. *When:* You want to keep the generated code or move beyond the hosted builder.

## Numbers
- Only plan seen at the time of recording costs $25; no alternative pricing options were visible. ([4:07](https://youtu.be/BXBwikXMb6Q?t=247))
- Convex's tool had been released about three weeks before the video. ([0:00](https://youtu.be/BXBwikXMb6Q?t=0))
- Test booking for a one-day rental priced at $80. ([10:25](https://youtu.be/BXBwikXMb6Q?t=625))
- Test expense of $100 (sports items) and a $50 payment, used to check balances. ([2:46](https://youtu.be/BXBwikXMb6Q?t=166))

## Hot takes
- Claims Convex is 'currently the best backend solution' for AI-built apps without comparing it to alternatives.
- Says the 'backend for AI' advantage comes from React/TypeScript being common in model training data. This is his reasoning, not evidence.
- Says the app was built in a single run with one prompt and no later changes, but the balances were wrong and needed a re-prompt with a personal API key. The claim is contradicted in the same video.
- Calls the lack of image input a major limitation for UI work, which he found frustrating in practice.

## Tools mentioned
Chef (Convex's AI app builder), Convex, Lovable, Supabase, Bolt.new, v0 (Vercel), ChatGPT, Anthropic API (Claude), React, TypeScript
