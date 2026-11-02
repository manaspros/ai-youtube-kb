# Everyone HATES Frameworks?!? - State of JavaScript 2024

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `6vXC-kxTGfI` · [watch](https://youtu.be/6vXC-kxTGfI) · **date:** 2025-11-02 · **length:** 10:04 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, State of JavaScript
- **topics:** dev-tools · **tags:** javascript, typescript, state-of-js, survey, frameworks, react, svelte, angular, vue, nextjs, astro, webpack, vite, bun, deno, hono, fastify, ai-tool-usage, static-typing, temporal

> A Better Stack walkthrough of the State of JavaScript 2024 survey: demographics, feature usage, framework/meta-framework/runtime sentiment, pain points and AI tool usage.

## Summary
The presenter walks through the 2024 State of JavaScript survey results and mostly reads charts aloud. Demographics come first (US salaries dominate, degree makes little difference to pay). Feature usage follows: nullish coalescing and dynamic imports are widely used, Promise.allSettled is at 47%, private fields at 45%, and top-level await is used by very few respondents. The pain-point section is the main thread: lack of static typing is the top complaint every year, browser support is second, and dates are a persistent library-dependent pain. The TypeScript share is high (67% write more TS than JS). For frameworks, React is the most used, but Svelte has the best positive-to-negative ratio and Angular gained the most ground in that ratio. Next.js leads meta-frameworks, Astro has the best sentiment, and Next.js complexity is the main complaint. Build tools show Webpack still most used but heavily criticized, with Vite (transcribed as "V") much better liked. Express remains the most used backend while Fastify and Hono grow, and Bun outranks Deno among non-browser, non-Node runtimes. On AI, ChatGPT is first, Copilot second, Claude third and Cursor fifth, and 20% of respondents use no AI at all. The video is light on analysis and mostly reports what the survey shows.

## Key ideas
- **Lack of static typing is the top JavaScript pain point every year, and TypeScript has become the default: 67% of respondents write more TypeScript than JavaScript and 34% use only TypeScript.** — Static typing is also the most-wanted language feature, ahead of a standard library and signals. Browser support is the second pain point, with Safari singled out. ([2:46](https://youtu.be/6vXC-kxTGfI?t=166))
- **Modern JS features are adopted unevenly: nullish coalescing and dynamic imports are common, Promise.allSettled is used by 47%, and private fields by 45%. Top-level await and Set methods have very low usage.** — The speaker notes that Set methods are underused and worth learning. Only 13 respondents reported using top-level await. ([1:00](https://youtu.be/6vXC-kxTGfI?t=60))
- **Front-end frameworks: React is still the most used, but sentiment is a separate axis. Svelte ranks first on the positive-to-negative ratio, React drops to third and Vue rises to second, and Angular jumped from 10th to 7th.** — The speaker's read is that most frameworks become more negatively discussed as they get more popular, which he attributes partly to forced use at employers and, for React, to server components. ([4:05](https://youtu.be/6vXC-kxTGfI?t=245))
- **Meta-frameworks: Next.js is the most used, but Astro has the best sentiment (only 0.88 of users reported negative sentiment). Next.js has the largest complaint cluster, excessive complexity and issues.** — Next.js sentiment has trended more negative since 2022, which the presenter links to the pages-to-app-router move. Gatsby's sentiment improved, which he could not explain. ([5:02](https://youtu.be/6vXC-kxTGfI?t=302))
- **Build tools tell a legacy-versus-new story. Webpack is still most used but has a large negative share (31%), while Vite is second in usage with a much smaller negative share.** — Backends: Express is still the most used, but Fastify and Hono are gaining. The presenter says he would now pick Fastify or Hono for a new backend. ([7:02](https://youtu.be/6vXC-kxTGfI?t=422))
- **Runtimes: Node.js is still top and the browser second, but Bun is the most popular option beyond those two, ahead of Deno.** — The speaker points viewers to a separate Bun vs Deno video for a comparison. ([7:02](https://youtu.be/6vXC-kxTGfI?t=422))
- **AI tool usage is still modest: ChatGPT is the most used, Copilot second, Claude third and Cursor fifth. About 20% of respondents use no AI, and most AI users apply it to under 30% of their code.** — Only 18 respondents said that 100% of their code is written with AI. ([8:23](https://youtu.be/6vXC-kxTGfI?t=503))

## Techniques
- **Rank tools by sentiment among users, not only by usage** — For each library, framework or runtime, compare the share of users who used it with the share of those users who report positive or negative sentiment. Sort by the sentiment ratio to see which tools are well liked, separately from which are popular. *When:* When choosing a framework or library and popularity alone would mislead, for example when a widely used tool has a high negative share (Webpack in this survey).
- **Track usage and sentiment over survey years together** — Plot each tool's usage rank and sentiment trend across yearly survey results. A tool that gains usage while sentiment turns negative is a warning sign, while rising sentiment with flat usage points to a strong newcomer. *When:* When tracking the trajectory of a technology rather than a single snapshot, for example to judge whether a meta-framework's complexity complaints are growing.

## Numbers
- 67% of respondents say they write more TypeScript than JavaScript, and 34% say they use only TypeScript. ([7:02](https://youtu.be/6vXC-kxTGfI?t=422))
- 47% of respondents have used Promise.allSettled and 45% have used private fields. Top-level await was used by only 13 respondents. ([1:00](https://youtu.be/6vXC-kxTGfI?t=60))
- 20% of respondents do not use AI at all, and most AI users apply it to under 30% of their code. 18 respondents write 100% of their code with AI. ([8:23](https://youtu.be/6vXC-kxTGfI?t=503))
- Vitest has the best sentiment among testing tools, with a reported negative share of 0.48 (the transcript says percent, but the value looks like a ratio). ([5:50](https://youtu.be/6vXC-kxTGfI?t=350))
- Astro has the best meta-framework sentiment, with 0.88 of users reporting a negative share (transcribed as a percentage). ([5:02](https://youtu.be/6vXC-kxTGfI?t=302))
- Vite has a 0.88 negative share despite being the second most used build tool, and Webpack has a 31% negative share. ([7:02](https://youtu.be/6vXC-kxTGfI?t=422))
- The most common reported annual income band is US$40,000 to $60,000, and the 10th and 90th percentile salaries are the same whether or not the respondent has a degree. ([0:00](https://youtu.be/6vXC-kxTGfI?t=0))

## Hot takes
- The presenter says most frameworks become more negatively discussed as they get more popular, which he links to forced use at employers. This is his interpretation, not a survey finding.
- He reads the sentiment figures as percentages, but several values (Vitest 0.48, Vite 0.88, Astro 0.88) look like ratios, so check them against the survey before quoting them.
- Quality is capped at 2 because the video is mostly chart reading with little analysis beyond the presenter's opinions. Its main value is the raw survey numbers.

## Tools mentioned
JavaScript, TypeScript, React, Vue, Angular, Svelte, Solid, Next.js, Astro, Nuxt, Gatsby, Jest, Vitest, React Native, Expo, Electron, Webpack, Vite, Rolldown, Analog, Lodash, date-fns, Moment, Luxon, Temporal, Express, Fastify, Hono, Node.js, Bun, Deno, ChatGPT, GitHub Copilot, Claude, Cursor, VS Code, Better Stack, Hono, Frontend Masters, Udemy, Codecademy, Egghead, JavaScript Weekly

## Relevance to our work
- **general** (1/3): Useful background if we ever build a JavaScript or TypeScript front end, but there is no agent-specific content. → *Only if a JS front end is needed: check the 2024 State of JavaScript results directly before choosing a framework or meta-framework.*
