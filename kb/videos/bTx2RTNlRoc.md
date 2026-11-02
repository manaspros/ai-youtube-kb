# React Router Now Supports Server Components

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `bTx2RTNlRoc` · [watch](https://youtu.be/bTx2RTNlRoc) · **date:** 2025-11-02 · **length:** 5:27 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Remix, Better Stack
- **topics:** dev-tools · **tags:** react-router, react-server-components, server-actions, remix, parcel, preview-release, frontend-frameworks

> Quick walkthrough of a React Router preview with React Server Components, using a toy app to show loaders, server actions and root middleware, plus the speaker's guess about Remix's future.

## Summary
The Better Stack host walks through a preview release of React Server Components in React Router, using a small demo project with a home page, an about page and one server action. He describes the setup as an Express server importing React Router through Parcel's virtual imports, with routing happening on the server and a root.tsx that holds layouts, an error boundary and unstable middleware. Pages export a named server component instead of a default export, loaders run on the server before render, and a form posts to a function marked "use server" that logs the value and updates the page. A pending-state button is the one client component in the form. He reports that reading the name from URL query params did not work for him, so he moved the value through the server action instead. He closes by saying Remix itself is unlikely to get server component support, and that Remix 3 may use a custom renderer, based on a forked copy of a blog post that was later taken down. The video is short, shows no benchmarks, and relies on the speaker's interpretation for the Remix and Parcel points.

## Key ideas
- **React Router preview adds server components, and the speaker reads the blog post as a move to a custom renderer instead of plain React** — Speaker says the team has released a preview of server components in React Router and seems to have moved to its own renderer rather than React. He flags that he will return to the renderer point later. ([0:00](https://youtu.be/bTx2RTNlRoc?t=0))
- **The demo is built on Parcel rather than Vite, which the speaker says lacks server component support** — A Express server imports React Router through a Parcel virtual import and serves static files. The speaker's stated reason for Parcel is that Vite does not support server components yet. ([1:21](https://youtu.be/bTx2RTNlRoc?t=81))
- **Routing runs on the server, which differs from React Router's usual client-side routing** — root.ts maps the browser URL to pages on the server. root.tsx holds the layouts, an error boundary and a server component export. The speaker assumes this from reading the code. ([1:21](https://youtu.be/bTx2RTNlRoc?t=81))
- **Server components are exported by name, not as a default export, and loaders run on the server before render** — The home page has a loader plus a server component that renders most of the markup. The speaker calls the named export a React Router convention and notes that the loader acts like the client-side loader but runs on the server. ([2:46](https://youtu.be/bTx2RTNlRoc?t=166))
- **Reading query params in the server component did not work for the speaker, so he passed the value through a server action** — He first took the name from the URL query string and passed it into the server component, but that failed. He switched to reading the name from the form submission in the action, and the message comes from middleware context. ([2:46](https://youtu.be/bTx2RTNlRoc?t=166))
- **Functions marked use server run only on the server, and a client-only pending button shows form state** — The action logs the submitted name to the server console and updates the rendered value. A separate pending button, a client component, shows the submitting state while the action runs. ([4:08](https://youtu.be/bTx2RTNlRoc?t=248))
- **Speaker expects Remix not to get server component support and sees Remix 3 as a separate renderer effort** — He says the Remix team is working on a version 3 that appears to build its own renderer because React is too complicated for them. He notes the source is a forked copy of a blog post that was taken down, so he treats the claim as unconfirmed and expects more at Remix Jam. ([4:08](https://youtu.be/bTx2RTNlRoc?t=248))

## Techniques
- **Export a server component by name instead of default** — In a React Router route module, export the server component as a named export (the speaker calls this the convention) rather than default. The page component then renders the server-side markup. *When:* When trying React Router's preview server components and wiring a route page to a server component.
- **Loader for server-side data before render** — Define a loader in the route module that runs before the server component renders, similar to the client-side loader pattern. In the demo, the loader reads a value from root middleware context and passes it into the component. *When:* When a server component needs data from the request or from middleware before it renders.
- **Server action with the use server directive for form submits** — Add the use server directive to a function that reads the form field (the demo reads name from the form data), logs it server-side and returns updated values. Hook the form's action to that function so the page updates after submit. *When:* When a form submission should run only on the server, including logging or touching server resources.
- **Client-only pending UI inside a server-rendered form** — Put a small client component (the demo uses a pending button) inside the server-rendered form to show the pending text while the action is in flight. Only that component ships to the browser. *When:* When the rest of the page should stay server-rendered but a piece of UI needs browser state, such as a submitting indicator.
- **Root middleware for logging and request-scoped context** — Use unstable middleware in root.tsx to log requests and provide a value (the demo passes a Map with a string) that loaders can read. The speaker says this could also be used for batching and caching, but does not show that. *When:* When several routes need shared request-scoped data or logging without repeating the code in each loader.
- **Parcel setup with a virtual import behind an Express server** — Serve the app through an Express server that imports React Router via a Parcel virtual import and serves static files. The speaker chose Parcel because Vite does not yet support server components in his account. *When:* Only as a reference for the demo's build setup. The speaker does not give the config or commands.

## Numbers
- Demo app has two pages (home and about) plus one server action; no benchmarks, latency or adoption numbers are given ([0:00](https://youtu.be/bTx2RTNlRoc?t=0))
- Video length is 5:27 ([0:00](https://youtu.be/bTx2RTNlRoc?t=0))

## Hot takes
- Speaker says React Server Components were once widely bashed and that the React Router and Remix team has now caved on them, which is an editorial framing and not evidence.
- Speaker thinks Remix will probably never get server component support and that Remix 3 builds its own renderer because React is too complicated. He cites a forked copy of a blog post that was taken down, so the claim is secondhand and unverified.
- Speaker prefers React Router's server components over Parcel's implementation, based on one toy project.
- Thin substance: a single short demo with no benchmarks, no real-world app, and hearsay on the renderer and Remix points. Caps quality at 2.

## Tools mentioned
React Router (preview, no version stated), React Server Components, Parcel, Vite, Express, Remix, React
