# React Is Falling Behind: How Astro Creates Blazing FAST Sites in Minutes

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `sNhRsQSPn5Q` · [watch](https://youtu.be/sNhRsQSPn5Q) · **date:** 2025-12-02 · **length:** 6:19 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed Better Stack presenter · **orgs:** Better Stack
- **topics:** dev-tools · **tags:** astro, static-site-generation, islands-architecture, partial-hydration, markdown, react, web-performance, blog

> Better Stack walkthrough of a Markdown blog built with Astro, showing how Astro ships near-zero JavaScript and hydrates a single React component only when it is visible.

## Summary
A Better Stack presenter (unnamed in the transcript) builds a simple blog with Astro and argues Astro suits content-heavy sites such as blogs, docs, help centers and community boards. Posts are plain Markdown files with front matter for title, description and tags, and Astro handles layouts, routing, SEO tags and bundling. The presenter compares load behavior in Chrome DevTools against a React site and says Astro pages load faster because they ship static HTML rather than fully hydrating the page. To show partial hydration, he imports a React-style like button into a Markdown post and marks it with a client directive (spoken as "client is visible"), so it becomes interactive only when needed. The video is a short, mostly qualitative demo with no measured benchmarks, and the Lighthouse score claim is not shown.

## Key ideas
- **Astro outputs pure static HTML and sends almost no JavaScript to the browser by default, which is the basis of its speed claim.** — The presenter says a page ships virtually zero JS and that Astro does not fully hydrate static content the way a typical React site does. ([0:00](https://youtu.be/sNhRsQSPn5Q?t=0))
- **Astro fits content-heavy sites such as blogs, documentation, help centers and community boards, where most content needs no JavaScript.** — The argument is that the framework's default of static output matches content sites. The video does not test other site types. ([1:11](https://youtu.be/sNhRsQSPn5Q?t=71))
- **Speed is compared informally in Chrome DevTools Network tab against a React site.** — The presenter opens an Astro blog post and a React marketing site and shows load timing side by side. Only qualitative comparison, one site each, no numbers. ([2:19](https://youtu.be/sNhRsQSPn5Q?t=139))
- **Posts are plain Markdown with front matter, and Astro supplies layouts, routing, SEO tags and bundling.** — Front matter sits between three-hyphen delimiters at the top of each .md file and holds title, description and tags; tag pages are generated from those front-matter tags. ([3:31](https://youtu.be/sNhRsQSPn5Q?t=211))
- **Partial hydration (islands): a single React component hydrates only when a directive says so, and the rest of the page stays static.** — The presenter imports a like button into a Markdown post and adds a client directive (spoken as client is visible), so JavaScript loads only when the component becomes visible. ([4:26](https://youtu.be/sNhRsQSPn5Q?t=266))

## Techniques
- **Island-style partial hydration** — Write the interactive part as a component (the video uses a React-style like button), import it into the .md or .astro page, and attach a client directive that the video speaks as 'client is visible' (presumably client:visible). Everything else stays static HTML with no JS. *When:* Mostly static content pages that need one or two interactive widgets, such as a like button or a form.
- **Markdown posts with front matter** — One .md file per post. Put metadata (title, description, tags) in a front-matter block delimited by three hyphens above and below. Write the body as plain Markdown. Astro applies the layout and routing and generates SEO tags. *When:* Blogs, docs and help centers where authors write Markdown and the site should ship no client JS.
- **Tag pages from front matter** — Keep tags in each post's front matter and generate tag listing pages from the slugs under a pages/tags folder, alongside pages/posts. The video does not show the route file syntax. *When:* Content sites that need browsable tag or category indexes built from post metadata.
- **Quick Astro blog setup as shown** — 1) Install the Astro extension for VS Code. 2) Scaffold the project with components/, layouts/ and pages/ folders (pages contains tags/ and posts/). 3) Write posts as Markdown with front matter. 4) Run npm run dev. 5) Import an interactive component into a page and add the client directive. *When:* A first walkthrough of Astro for someone who already knows React and Markdown.
- **Compare load behavior in DevTools** — Open the same kind of page on two sites (a static Astro page and a React page) with Chrome DevTools, go to the Network tab, and compare how long resources and the page take to load. *When:* A quick, informal check of whether a page is shipping hydration JS. It is not a controlled benchmark.

## Numbers
- Presenter says Astro sites 'consistently get hundreds on Lighthouse' (a score out of 100, so 'hundreds' is not literal). No score or measurement is shown. ([3:31](https://youtu.be/sNhRsQSPn5Q?t=211))
- Presenter describes the Astro page as shipping virtually zero JavaScript, but no byte counts or timings are shown. ([0:00](https://youtu.be/sNhRsQSPn5Q?t=0))
- The video is 6:19 long, with one Astro blog and one React comparison site, so the sample is n=1 per side. ([2:19](https://youtu.be/sNhRsQSPn5Q?t=139))

## Hot takes
- Astro is pitched as competing with React for content sites, but the video shows one personal blog and one React site, both chosen by the presenter, with no controlled test.
- The Lighthouse claim (hundreds on Lighthouse) is asserted without a score on screen.
- Title says 'React Is Falling Behind' and 'Blazing FAST Sites in Minutes', which is more hype than the demo supports.

## Tools mentioned
Astro, VS Code Astro extension, React, Markdown, npm, Chrome DevTools, Lighthouse
