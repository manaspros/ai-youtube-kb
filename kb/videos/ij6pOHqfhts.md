# Goodbye HTMX: Why Alpine Ajax is My New Go-To Library

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ij6pOHqfhts` · [watch](https://youtu.be/ij6pOHqfhts) · **date:** 2025-11-02 · **length:** 6:37 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** ?
- **topics:** dev-tools · **tags:** htmx, alpine-ajax, alpine-js, progressive-enhancement, server-rendered, ejs, express, hono, nextjs, ajax, frontend

> Better Stack compares HTMX and Alpine Ajax on the same Express/EJS to-do app; Alpine Ajax needed no server changes and still works with JavaScript off, so the author prefers it for progressive-enhancement apps.

## Summary
The video walks through converting a server-rendered Express.js and EJS to-do app to non-refreshing updates, first with HTMX and then with Alpine Ajax. HTMX is described as a 2020 library under 14 KB min+gzip that swaps server-returned HTML into the page through attributes. Alpine Ajax is a 2023 Alpine.js plugin, just under 3 KB gzipped, that does similar work. With HTMX, the author replaces the form with hx-style attributes and changes the server to return small EJS partials instead of redirecting. With Alpine Ajax, the server code stays untouched, the full HTML is returned, and only the targeted list element is updated, so the app still works with JavaScript turned off. Alpine's x-data and x-model handle clearing the input after a successful submit. The author found Alpine Ajax easier after a few hours of use, while noting he is not an expert in either library and would not pick either for his own React-based projects. His stated use case is apps that must work with JavaScript on or off, where he would choose Alpine Ajax with Hono over Next.js. The evidence is a single toy app with no timing or benchmark data.

## Key ideas
- **HTMX sends requests and swaps server HTML into the page via attributes, with no full refresh; the library is under 14 KB min+gzip.** — HTMX (released 2020) is driven by HTML attributes. Client-side reactivity or state needs hand-written JavaScript, which is where Alpine comes in. ([0:00](https://youtu.be/ij6pOHqfhts?t=0))
- **Alpine Ajax is an Alpine plugin (2023) that covers much of what HTMX does and is just under 3 KB gzipped.** — It works well alongside Alpine and, like HTMX, takes its behavior from HTML attributes, so no JavaScript has to be written. ([0:00](https://youtu.be/ij6pOHqfhts?t=0))
- **With HTMX, the server must return partials. The author changed the routes so each action renders only the changed item.** — Adding a to-do returns the to-dos partial, toggling returns the single to-do partial, and delete uses hx-delete. The redirects are gone, so the server returns fragments of the page. ([2:53](https://youtu.be/ij6pOHqfhts?t=173))
- **Alpine Ajax lets the server stay unchanged: it returns the full page and the plugin swaps only the targeted element.** — The author changed only the EJS template. Because the form keeps its normal action and method, the app still works with JavaScript disabled, which the author calls a progressive enhancement. ([2:53](https://youtu.be/ij6pOHqfhts?t=173))
- **Alpine x-data and x-model clear the input after a successful Ajax submit.** — The form gets an x-data object with a task key set to an empty string. The input is bound with x-model, and the value is reset when the request succeeds. ([4:19](https://youtu.be/ij6pOHqfhts?t=259))
- **The main cost of both libraries is a mental shift: updates happen on the server, and the client receives HTML rather than JSON.** — The author says he had to stop thinking of the client as a data-driven view and treat the server as the place where the markup is produced. ([5:44](https://youtu.be/ij6pOHqfhts?t=344))
- **Overall verdict: Alpine Ajax was easier after a few hours, and it is the author's pick for apps that must work with JavaScript on or off.** — The author says he is more comfortable with React and would not use either library for personal projects. He says he would choose Alpine Ajax with Hono over Next.js for progressive-enhancement apps. ([5:44](https://youtu.be/ij6pOHqfhts?t=344))

## Techniques
- **HTMX partial-swap CRUD on an EJS list** — Replace the form's submit handling with attributes: hx-post on the form targeting the to-do list element by its ID, plus a request that resets the input after success. Change the POST, toggle and delete routes to render small EJS partials (the list for add, the single item for toggle) instead of redirecting. Use hx-delete for deletion. Exact attribute names are as read from auto-captions (HX post, hxdelete). *When:* Use when you want the smallest responses and are willing to split server templates into partials. Good for server-rendered apps that need snappy updates without a SPA.
- **Alpine Ajax full-HTML swap, no server changes** — Keep the existing form action and method attributes and add three Ajax attributes: one from Alpine Ajax that names the target element (here the todos list ID) and two from Alpine.js. The server keeps returning the full page, and Alpine Ajax updates only the targeted block. The exact target attribute name is not clearly captured in the auto-captions. *When:* Use when the same routes must serve full pages to non-JS clients and partial updates to JS clients. It is the progressive-enhancement path the author prefers.
- **Alpine x-data/x-model form reset after Ajax success** — Put x-data on the form with an object holding task set to an empty string. Bind the input with x-model="task". Reset task to '' when the Ajax submission succeeds. The success hook is not named in the captions. *When:* Use when a form's input must clear after an Ajax submit without custom JavaScript, or when a small amount of client state is needed alongside Ajax swaps.

## Numbers
- HTMX is released in 2020 and the library is under 14 KB minified and gzipped. ([0:00](https://youtu.be/ij6pOHqfhts?t=0))
- Alpine Ajax is an Alpine plugin released in 2023 and is just under 3 KB gzipped. ([0:00](https://youtu.be/ij6pOHqfhts?t=0))
- The author spent a few hours comparing the two libraries on the to-do app before judging Alpine Ajax easier to work with. No timing or benchmark numbers are given. ([5:44](https://youtu.be/ij6pOHqfhts?t=344))

## Hot takes
- Alpine Ajax is easier to work with than HTMX for this author, and he would choose it over Next.js for apps that must work with JavaScript on or off.
- The title's 'Goodbye HTMX' overstates the case. The speaker says he is not an expert in either library, that he would not use either for personal projects, and that the test is a single toy app.
- Server-returned full HTML with progressive enhancement is a better default than SPA-style JSON plus client rendering, at least for simple CRUD apps (this is the author's opinion, not measured).

## Tools mentioned
HTMX, Alpine Ajax, Alpine.js, Express.js, EJS, Hono, Next.js, React, Vue

## Relevance to our work
- **prosharness** (1/3): Phone-driven approvals may need a small web page. Server-rendered HTML with partial swaps could cover it without a SPA. → *If the phone-approval screen is a plain web page, try server-rendered HTML with partial swaps before reaching for a SPA framework.*
- **general** (1/3): Shows a concrete progressive-enhancement pattern: keep form action and method, return full HTML, and swap partials only when JS is present. → *Skim the Alpine Ajax docs for the progressive-enhancement pattern if we build any small server-rendered admin UI.*
