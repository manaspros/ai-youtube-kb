# TypeScript 5.8 Has 2 AWESOME Features

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `vcVoyLQMCxU` · [watch](https://youtu.be/vcVoyLQMCxU) · **date:** 2025-11-02 · **length:** 6:34 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Better Stack
- **topics:** dev-tools · **tags:** typescript, typescript-5.8, conditional-types, indexed-access-types, erasable-syntax, node-type-stripping, overloads, nightly-build

> Better Stack walkthrough of two TypeScript 5.8 changes: the Erasable Syntax Only flag, which bans runtime-emitting features so Node can run .ts files directly, and checked return types for conditional and indexed access types, demoed on the nightly build.

## Summary
The presenter previews two TypeScript 5.8 features, demoed on the nightly build about a month before release. The first is the Erasable Syntax Only flag, which makes TypeScript error on enums, namespaces and class parameter shorthands because these emit runtime JavaScript instead of being erased. The speaker's argument is that this lets Node run TypeScript files without ts-node or tsx, since Node 23.6 strips types by default. The second change is that TypeScript 5.8 now checks return statements against conditional return types and indexed access return types, where earlier versions reported false errors. The speaker shows a person-or-website example where the function's return type depends on the input type. The conditional version still needs a never fallback branch, and the speaker notes that pre-5.8 code can get the same result with function overloads. The video is short and has no benchmarks or deep internals, but the code examples are concrete and reproducible.

## Key ideas
- **Erasable Syntax Only flag bans enums, namespaces and class parameter shorthands** — These features emit runtime JavaScript rather than being erased at compile time. With the flag on, TypeScript errors on them in the codebase. ([0:00](https://youtu.be/vcVoyLQMCxU?t=0))
- **Erasable-only code can run directly on Node without a transpiler** — The speaker argues the flag gives confidence that Node can execute the TypeScript files as-is. Node 23.6 runs TS by stripping types by default, so ts-node or tsx is not needed. The speaker also says this moves TypeScript closer to running in the browser, which is speculation attributed to Matt. ([0:00](https://youtu.be/vcVoyLQMCxU?t=0))
- **Pre-5.8, conditional return types were not checked against their branches** — A function returning string for Person and URL for Website still typed its callers' results as string or URL, and the implementation's returns showed errors even though the values were correct. ([1:25](https://youtu.be/vcVoyLQMCxU?t=85))
- **5.8 checks conditional return statements, shown on the nightly build** — The return errors go away and the callers get the narrowed types, so person.address is a string and website.url is a URL. ([2:45](https://youtu.be/vcVoyLQMCxU?t=165))
- **A never fallback branch is still required for conditional return types** — Replacing the final branch with plain URL fails again. Narrowing needs the last branch of the conditional to be never. ([3:58](https://youtu.be/vcVoyLQMCxU?t=238))
- **Overloads give the same typing before 5.8** — Separate overload signatures per input type, with one broader implementation signature, produce the same caller-side types on older versions. ([3:58](https://youtu.be/vcVoyLQMCxU?t=238))
- **Indexed access return types get the same fix** — A function generic over keyof Config, where prod is a string and dev is a boolean, previously errored on its return. 5.8 checks the indexed access type and the error goes away. ([3:58](https://youtu.be/vcVoyLQMCxU?t=238))

## Techniques
- **Enable the Erasable Syntax Only flag to keep code runnable without a transpiler** — Turn on the Erasable Syntax Only flag in TypeScript 5.8. TypeScript then reports errors for enum, namespace and class parameter-property shorthand. The video does not show a replacement for those features. *When:* When you want Node 23.6+ to execute .ts files directly, with type stripping, and no ts-node or tsx step.
- **Conditional return type with a never fallback, typed by input generic** — Make the function generic over the union of input types, e.g. T extends Person | Website. Set the return type to a conditional: T extends Person gives string, T extends Website gives URL, and the final branch is never. Narrow inside the body with a type guard on the input. Under 5.8 the body's returns are checked against the conditional. *When:* A function's return type depends on which member of a union was passed in. Requires TypeScript 5.8 (nightly in the video) for the body to be checked.
- **Overloads as the pre-5.8 fallback for conditional returns** — Declare one overload signature per input type with the matching concrete return type, then one implementation signature with the wide union return. Callers see the per-input types. *When:* You are on a TypeScript version before 5.8 and need the same caller-side typing.
- **Key-driven return type with an indexed access type** — Make the function generic over T extends keyof Config and declare the return type as Config[T]. Branch on the key in the body, returning the matching value type. The 5.8 checker accepts the return; earlier versions error and need overloads. *When:* A lookup function returns a different value type depending on which key is passed.
- **Trying TypeScript features early on the nightly build** — Install the nightly TypeScript build to test upcoming features before the stable release, as the presenter did for 5.8 about a month ahead. *When:* You want to verify a language change against your own code before it ships, accepting that the behavior may still change.

## Numbers
- TypeScript 5.8 described as about a month from full release at recording time ([0:00](https://youtu.be/vcVoyLQMCxU?t=0))
- Node 23.6 runs TypeScript files by erasing types by default, without ts-node or tsx ([0:00](https://youtu.be/vcVoyLQMCxU?t=0))
- Conditional narrowing requires the final branch of the conditional to be never ([3:58](https://youtu.be/vcVoyLQMCxU?t=238))

## Hot takes
- The browser-TypeScript outlook is the presenter's extrapolation from the flag, not a shipped feature.
- Both demos run on the nightly build, so behavior could change before the stable 5.8 release.
- The conditional-return change is framed as a bug fix for a long-standing problem, which the demos support for the specific cases shown.

## Tools mentioned
TypeScript 5.8 (nightly build), Node.js 23.6+ (native type stripping), ts-node, tsx
