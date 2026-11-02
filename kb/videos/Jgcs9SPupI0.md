# I Switched from Zod to ArkType (Here's Why)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Jgcs9SPupI0` · [watch](https://youtu.be/Jgcs9SPupI0) · **date:** 2025-11-02 · **length:** 11:25 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Unnamed Better Stack presenter · **orgs:** Better Stack
- **topics:** dev-tools · **tags:** arktype, zod, typescript, runtime-validation, schema-validation, developer-experience, morphs, pattern-matching, custom-validators, error-messages

> Walkthrough of ArkType as a Zod replacement for TypeScript runtime validation: TS-style schema syntax, editor-visible errors, built-in constraints, custom narrow validators, morphs, and pattern matching. The "up to 100x faster" claim is not benchmarked on screen.

## Summary
A Better Stack presenter explains why they are switching from Zod to ArkType for runtime validation. They show installing the npm package, defining an object schema with TypeScript-like string syntax, and getting type errors and a syntax-highlighting extension in the editor. Next they cover built-in constraints (numeric ranges, integer and email keywords, many string validators), validating data with an errors-or-data return, and writing custom validators with narrow() and custom messages. The video then covers morphs (transforms piped before, after, or between validators, such as JSON parsing) and the pattern-matching API added in ArkType 2.1. The speaker claims ArkType is up to 100x faster than Zod, but no benchmark is shown. The walkthrough is a single-user anecdote, not a comparison study.

## Key ideas
- **ArkType schemas use TypeScript-like syntax, so an object type reads almost like a TS type declaration** — Field types such as string, a literal union of Android or iOS, and number or string array are written the way they would be in TypeScript. The speaker says the first reaction was skepticism, which the walkthrough then reverses. ([0:00](https://youtu.be/Jgcs9SPupI0?t=0))
- **Type errors show up in the editor, including on the schema itself** — A misspelled keyword or missing bracket in the schema produces TypeScript errors on hover, which the speaker found surprising. An editor extension adds syntax highlighting for schema strings, and Error Lens shows inline messages. ([1:04](https://youtu.be/Jgcs9SPupI0?t=64))
- **Constraints and built-in keywords are written inside the schema string** — Numeric bounds (greater than 0, less than 120), integer keyword, and string keywords like email, alphanumeric, base64 and credit card replace hand-written regex checks. Autocomplete lists the keywords. The speaker says regex for email is a nightmare to hand-write. ([2:20](https://youtu.be/Jgcs9SPupI0?t=140))
- **Validation returns either the validated data or an errors object with a human-readable summary** — The result is checked with instanceof against the errors type. The errors object is a list of individual errors and also has a summary string meant to be returned to end users. Failed-type messages are specific, such as 'must be a number but found string'. ([3:09](https://youtu.be/Jgcs9SPupI0?t=189))
- **Custom validators via narrow() with either an auto-generated or a custom message** — Because ArkType has divisor checks only for divisible-by, an odd-number check is built with a narrow function. Inside it, ctx.mustBe produces a generated message, and ctx.reject takes a custom message string. The speaker calls custom messages on Zod a pain point for complex forms. ([5:31](https://youtu.be/Jgcs9SPupI0?t=331))
- **Morphs transform data as part of the validation pipeline** — Transforms can sit before, after, or between validators. Examples are JSON parsing of a string, trimming, and numeric-string-to-number then a divisibility check. Shorthand forms such as a built-in JSON parser and a 'to' shorthand avoid writing the pipe by hand. ([6:30](https://youtu.be/Jgcs9SPupI0?t=390))
- **Pattern matching API in ArkType 2.1 uses runtime types as match cases** — A match() function branches on types such as string or array, number, and bigint, with a .case clause for structural checks and a default that asserts. The speaker calls it the first syntactic matcher in JavaScript, a claim not verified in the video. ([8:53](https://youtu.be/Jgcs9SPupI0?t=533))

## Techniques
- **Define a schema with string-syntax types** — Install the arktype npm package. Import the type function from arktype and pass an object literal of field types. Mark optional fields as optional in the schema, for example a versions field that is number or string array. The video shows this but does not read out the exact schema text, so check the linked docs for exact key syntax. *When:* Replacing Zod object schemas in TypeScript code where TS-like syntax and editor errors are wanted.
- **Validate and branch on errors** — Call the schema with unknown input: result = User(data). If result instanceof type.errors, return result.summary to the user, or log the list of errors. Otherwise use result as the typed, validated value. *When:* Request bodies, form input, or config files where a readable error summary goes back to the caller.
- **Add constraints inline with keywords and ranges** — Write number bounds such as greater than 0 and less than 120 inside the schema, use number.integer for integers, and use string keywords like email and alphanumeric instead of custom regex. Autocomplete lists available keywords after typing a dot. *When:* Fields that need range or format checks but where hand-written regex is error-prone.
- **Custom validator with narrow and a custom message** — On a number or string type, call .narrow((n, ctx) => ...). Return true when valid. When invalid, return ctx.reject('your message') for a custom string, or ctx.mustBe('...') to get a generated message that includes the expected description and the actual value. *When:* Domain rules the built-in keywords do not cover, such as oddness or cross-field checks needing good messages.
- **Parse and transform with morphs** — Use string.json.parse for JSON strings, a trim transform for strings, and numeric-string parsing piped to a validator for checks like even numbers. A 'to' shorthand parses a string and validates it against a second type in one step. The speaker shows the pipe operator but the caption renders it unclearly, so check the docs for the exact operator. *When:* Inputs arrive as strings (JSON bodies, form fields, query params) and need parsing plus validation in one schema.
- **Pattern matching on runtime types** — Import match from arktype. Chain .case on a match with a type and a structural check, such as an object with a numeric length property, and end with a default. The speaker uses assert in the default to reject unsupported types, and returns 0 in another example. *When:* Dispatching on the runtime shape of unknown values, for example a size() helper over strings, arrays, numbers and bigints.

## Numbers
- ArkType is claimed to be up to 100 times faster than Zod. No benchmark, harness, or workload is shown. ([0:00](https://youtu.be/Jgcs9SPupI0?t=0))
- Pattern matching was added in ArkType 2.1 (version stated by the speaker). ([8:53](https://youtu.be/Jgcs9SPupI0?t=533))
- Example constraint: a number must be greater than 0 and less than 120 (age field example). ([2:20](https://youtu.be/Jgcs9SPupI0?t=140))

## Hot takes
- The 100x faster claim is stated without any benchmark or workload on screen. Treat it as unverified.
- The 'first syntactic matcher in JavaScript' claim for the pattern-matching API is unverified.
- The speaker says 'there is no scenario ArkType cannot handle', which is an overclaim from a short tutorial.
- The video is a one-person walkthrough of DX (editor errors, extension, error summaries). It is not a comparison of Zod and ArkType on correctness, bundle size, or edge cases.

## Tools mentioned
ArkType (called 'archetype' in the captions; version 2.1 mentioned for pattern matching), Zod (comparison baseline), TypeScript, npm, ArkType VS Code extension (published by ArkType), Error Lens (VS Code extension), tRPC, React Hook Form, Hono

## Relevance to our work
- **agentos** (1/3): Runtime validation of JSON payloads is relevant only if AgentOS has TypeScript surfaces (SDK, dashboard, manifest tooling). Its core proxy is Rust, so most of the video does not apply. → *If an AgentOS TypeScript SDK or dashboard exists, spike ArkType on the manifest schema and one request-body schema and compare its error summaries against the current validator.*
- **prosharness** (1/3): ProsHarness checkpoint and config files need shape validation with readable errors, which is the main use case shown. → *If ProsHarness is TypeScript, validate the checkpoint/resume state file with a narrow() rule and a custom reject message, and compare against the existing approach.*
