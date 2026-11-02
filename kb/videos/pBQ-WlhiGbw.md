# This Next.js Server Actions Pattern is AWESOME (Validated & Authenticated Actions)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `pBQ-WlhiGbw` · [watch](https://youtu.be/pBQ-WlhiGbw) · **date:** 2025-11-02 · **length:** 9:54 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Unnamed Better Stack presenter · **orgs:** Better Stack
- **topics:** dev-tools, security-guardrails · **tags:** nextjs, server-actions, zod, input-validation, authentication, better-auth, typescript, middleware-pattern, react-useActionState, dry

> Tutorial on two reusable wrapper functions for Next.js server actions: one validates FormData with Zod, the other also checks a Better Auth session before the action runs.

## Summary
The presenter shows a middleware-style pattern for Next.js server actions that moves input validation and login checks out of each action body. A validatedAction wrapper takes a Zod schema and a handler, converts the incoming FormData to an object, runs safeParse, and returns the first error message on failure or calls the handler with the parsed data on success. A second wrapper, validatedActionWithUser, repeats this and adds a Better Auth session lookup via Next.js headers(); it throws an error when no user is found, which the presenter prefers so the attempt shows up in logs. The pattern is credited to the Next.js SaaS starter kit and to Lee Robinson. The demo converts a sign-up action to the wrapper, shows a password-length error surfacing in a useActionState form, then wraps a login action with the auth variant. The content is general web-development tooling with no AI or agent component.

## Key ideas
- **Separate validation and auth from action bodies by wrapping each server action in a reusable higher-order function, so actions receive already-validated data.** — The presenter says this is DRY: the action body only handles business logic, and the same wrapper is applied to every action that needs it. The pattern is credited to the Next.js SaaS starter kit and to Lee Robinson. ([0:00](https://youtu.be/pBQ-WlhiGbw?t=0))
- **Name the helper file something other than middleware.ts to avoid confusion with Next.js route middleware.** — The presenter says the starter kit calls it middleware.ts, but he prefers action-helpers because this wrapper is a separate concept from Next.js middleware. ([0:00](https://youtu.be/pBQ-WlhiGbw?t=0))
- **Use one standard result type for every action so the client can read errors and success the same way.** — ActionState has optional error and success strings, plus an index signature so an action can attach extra custom data such as field-level errors, loading flags or metadata without type complaints. ([2:07](https://youtu.be/pBQ-WlhiGbw?t=127))
- **Infer handler types from the Zod schema with generics rather than writing them by hand.** — The wrapper is generic over the schema and the return type. The handler receives the schema-inferred data as its first argument and the original FormData as its second, so the action gets typed input. ([2:07](https://youtu.be/pBQ-WlhiGbw?t=127))
- **Validate inside the wrapper and return the first error message instead of throwing for normal input failures.** — The wrapper turns FormData into a plain object with Object.fromEntries, calls the schema's safeParse, returns the first error message on failure, and otherwise calls the action with result.data plus the untouched FormData. ([4:50](https://youtu.be/pBQ-WlhiGbw?t=290))
- **Make the auth wrapper throw on a missing session, on purpose.** — validatedActionWithUser reads the Better Auth session from Next.js headers() and throws a not-authenticated error when there is no user. The presenter prefers a throw so an unauthenticated call to a protected action shows clearly in logs, reasoning that a logged-in-only action should never be reached by a logged-out user. ([7:00](https://youtu.be/pBQ-WlhiGbw?t=420))
- **Adopting the pattern is a one-line change per action, and the front end keeps reading state.error from useActionState.** — The presenter swaps the wrapper name in each action (validatedAction, or validatedActionWithUser for protected ones). Form UIs read state.error from the ActionState returned by useActionState and render it. ([5:54](https://youtu.be/pBQ-WlhiGbw?t=354))

## Techniques
- **Validated server-action wrapper** — Define a shared ActionState type with optional error and success strings and an index signature. Write a generic validatedAction(schema, handler) that returns an async server action. Inside it, convert FormData to an object with Object.fromEntries, run schema.safeParse, return the first error message on failure, and otherwise call handler(result.data, formData). Keep the wrapper in its own helper file, for example action-helpers, not middleware.ts. *When:* Any Next.js app where several server actions take form input and need the same Zod validation, and you want action bodies to contain only business logic.
- **Auth-checked server-action wrapper** — Copy the validated wrapper into a validatedActionWithUser variant with a user argument in its handler type. In the wrapper, get the session from Better Auth using Next.js headers(), and throw a not-authenticated error if no user exists. Wrap protected actions with it, so user is available in the handler and typed. *When:* Server actions that should run only for logged-in users. The presenter's advice is to throw rather than return an error, because reaching these actions while logged out means something upstream is wrong and should show in logs.
- **Front-end consumption of ActionState** — Bind the server action with React's useActionState hook. The state it returns is the ActionState type. Check state.error before rendering, and print it under the form. The presenter says the error type can be changed to an object if per-field errors are needed. *When:* Forms that post to a server action and need to show validation errors returned from the server.

## Numbers
- Three server actions live in actions.ts before the refactor: sign-up email, log-in email, and an auth action. ([0:00](https://youtu.be/pBQ-WlhiGbw?t=0))
- Demo password validation rule is a minimum of 8 characters; the demo error reads 'password must be at least eight characters'. ([8:19](https://youtu.be/pBQ-WlhiGbw?t=499))
- Video length is 9:54. ([9:54](https://youtu.be/pBQ-WlhiGbw?t=594))

## Hot takes
- The pattern is framed as production-ready, but the video shows no tests, no error-path tests, and no role or permission checks beyond logged-in status.
- Throwing on an unauthenticated call is presented as a logging decision, not a security decision; the transcript does not discuss what a client sees when the error is thrown.
- No AI or agent content: this is general Next.js and TypeScript web tooling. It only fits the channel as dev-tools and auth-adjacent guidance, so quality is capped as off-topic for the knowledge base even though the pattern is solid.
- The presenter states any validation library works, but the demo only uses Zod and the wrapper's safeParse call is Zod-specific.

## Tools mentioned
Next.js (server actions, headers()), Next.js SaaS starter kit, Zod, Better Auth, TypeScript, React useActionState hook
