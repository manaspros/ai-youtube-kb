# HTMX Explained: The "Dumb" HTML Secret Replacing React

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `HPAh1uiE2z0` · [watch](https://youtu.be/HPAh1uiE2z0) · **date:** 2026-08-02 · **length:** 7:56 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Unnamed narrator (Kai Explains channel) · **orgs:** Context (company cited for React-to-HTMX rewrite, self-reported numbers)
- **topics:** dev-tools · **tags:** htmx, hypermedia, react, spa-vs-ssr, html-over-the-wire, frontend, alpine-js, hyperscript, rest, locality-of-behavior

> Kai Explains argues HTMX lets plain HTML talk to the server and swap returned HTML fragments, replacing most React-style SPA plumbing, and is honest that SPAs still win for highly interactive apps.

## Summary
The narrator explains HTMX as a roughly 16 KB, dependency-free library where elements send HTTP requests and swap the HTML the server returns into the page, instead of fetching JSON and re-rendering on the client. The core mechanism is a request, response, swap loop controlled by four attributes (post/get target, swap mode, trigger). The video frames this with a restaurant analogy: server-rendered pages send finished plates, while SPAs send ingredients and make the client assemble them, leaving two copies of state and an API to keep them in sync. It lists capabilities such as any element making any request on any event, any HTTP verb, out-of-band swaps that update several page regions in one response, and hx-boost style progressive enhancement. It claims HTMX restores hypermedia and REST as Roy Fielding defined it, and cites one company's React-to-HTMX rewrite (67% less code, JS dependencies 255 to 9, build times down about 90%) as evidence, though that is a single anecdote with no source. The honest-catch section says React remains the right choice for spreadsheet-like, offline, or many-interdependent-widget apps, that each interaction costs a round trip, that server load rises per click, and that small add-ons like Alpine.js or Hyperscript are needed for dropdowns and animations.

## Key ideas
- **HTMX sends the server's finished HTML fragment rather than JSON, so the backend returns the view directly and no client-side re-render or duplicate state is needed.** — Framed as the 'two kitchens' problem: SPAs keep a copy of the menu on both server and client and maintain an API just to keep them agreeing. HTMX's question is 'why don't we just send the plate?' ([1:23](https://youtu.be/HPAh1uiE2z0?t=83))
- **The whole library reduces to a request, response, swap loop driven by four attributes.** — The attributes named are post (where to send), target (which element changes), swap (replace inner, replace outer, or append), and trigger (click, form change, key press, debounce, or polling timer). The speaker says these cover nearly the whole surface. ([1:23](https://youtu.be/HPAh1uiE2z0?t=83))
- **Any element can issue a request on any event with any HTTP verb, not just links and forms.** — Examples: a delete button sends a real HTTP DELETE, the server returns nothing, and the row is swapped out. A text input with a keyup-triggered GET gives live search. ([2:46](https://youtu.be/HPAh1uiE2z0?t=166))
- **The backend can be any language because it only has to return HTML.** — Python, Ruby, Go, PHP, or Node are all named as viable. The speaker calls the stack HAL (hypermedia on whatever you'd like) and says there is no API to build. ([2:46](https://youtu.be/HPAh1uiE2z0?t=166))
- **Out-of-band swaps let one response update several page regions, such as the clicked item and a cart counter.** — One request, two updates, no glue code. This is the speaker's answer to the usual need for shared client state. ([2:46](https://youtu.be/HPAh1uiE2z0?t=166))
- **The speaker claims HTMX restores hypermedia and REST as Roy Fielding defined it, and locality of behavior (behavior readable in the markup).** — This is a contested framing presented as fact. The speaker gives no citation for the Fielding claim. ([4:08](https://youtu.be/HPAh1uiE2z0?t=248))
- **Honest limits: HTMX is for roughly the other 90% of the web (forms, dashboards, CRUD, content), not spreadsheets, maps, offline apps, or thousands of interdependent widgets.** — Costs named: every interaction is a network round trip, a flaky connection feels worse, the server does more work per click, and any dropdown, toggle, or animation needs a small companion such as Alpine.js or Hyperscript. ([5:29](https://youtu.be/HPAh1uiE2z0?t=329))
- **The closing 'four numbers' summary: about 16 KB vs React's roughly 45 KB before the app starts, four attributes, 255 dependencies down to 9 in one rewrite, and one copy of state.** — The speaker reads the single-copy-of-state point as the reason a category of sync bugs disappears. The rewrite figures come from one company, not a controlled benchmark. ([6:54](https://youtu.be/HPAh1uiE2z0?t=414))

## Techniques
- **Fragment-swap request on any element** — Put an HTTP-method attribute (hx-post or hx-get) on an element, set a target element for the response, choose a swap mode (replace inner, replace outer, or append), and set a trigger (click, change, keyup, debounce delay, or a polling timer). The server returns an HTML fragment that HTMX inserts. The speaker names the attributes as HxPost, HxTarget, HxSwap, HxTrigger. *When:* Forms, CRUD screens, dashboards with periodic refresh, and any page where the server already renders HTML. Prefer over a JSON endpoint plus client state when the UI is mostly server-driven.
- **Live search without an API** — On a text input, trigger a GET request on keyup, targeting a results element. The server returns table rows as HTML and HTMX swaps them in. The speaker says this takes about three lines. *When:* Search or filter lists where the backend can already render rows and no separate JSON API is wanted.
- **Delete as a real HTTP DELETE with empty response** — Attach a delete request to the row's button. The server deletes the record and returns an empty body. The swap removes the row, so no client state needs reconciling. *When:* CRUD tables where the row should disappear immediately after the server confirms.
- **Out-of-band swap for multi-region updates** — Have one server response carry the main fragment for the target plus extra fragments that update other page regions, such as a cart count in the header (the speaker calls this an out-of-band swap; the attribute name is not shown in the video). *When:* A single action changes several parts of the page, such as an add-to-cart that also updates a badge.
- **Progressive enhancement with boost** — Apply the boost attribute (captioned as HXE Boost; the real attribute is hx-boost) to a container so ordinary links and forms become background requests. The page still works as plain HTML if JavaScript is off. *When:* Content or form-heavy sites that should feel like a single-page app without a rewrite.
- **Loading indicator as one attribute** — Add the loading-indicator attribute to an element so a spinner shows while a request is in flight. No state is handwritten (the attribute name is not shown in the video). *When:* Any HTMX request that may take noticeable time.
- **Small sprinkle library for client-only behavior** — Pair HTMX with Alpine.js or Hyperscript for dropdowns, toggles, and animations that do not need a server round trip. *When:* When a server round trip would feel wrong for a purely local UI effect.

## Numbers
- HTMX is about 16 KB, zero dependencies. ([1:23](https://youtu.be/HPAh1uiE2z0?t=83))
- React plus React DOM core is roughly 45 (KB, before the app is written). ([4:08](https://youtu.be/HPAh1uiE2z0?t=248))
- A real single-page app ships hundreds of KB before showing anything (general claim, no measurement shown). ([4:08](https://youtu.be/HPAh1uiE2z0?t=248))
- One company's React-to-HTMX rewrite reported 67% less code, JavaScript dependencies down from 255 to 9, and build times down nearly 90%. Single anecdote, self-reported, no source given. ([4:08](https://youtu.be/HPAh1uiE2z0?t=248))
- Four attributes cover essentially the whole surface area of HTMX. ([1:23](https://youtu.be/HPAh1uiE2z0?t=83))

## Hot takes
- HTMX is 'what REST actually means' per Roy Fielding, and the modern JSON-API meaning of REST is a hijacked term (stated without citation).
- For the 'other 90%' of the web, React is unnecessary, though the speaker concedes React is right for deeply interactive client apps.
- 'The website was the framework all along.'
- The title 'Replacing React' is a hype framing; the body is more measured and includes a real honest-catch section, so quality is not capped at 2.

## Tools mentioned
HTMX, React, React DOM, Alpine.js, Hyperscript, Google Sheets (example of a spreadsheet-style app)
