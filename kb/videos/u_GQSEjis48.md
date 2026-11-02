# How to Setup Node.js and TypeScript

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `u_GQSEjis48` · [watch](https://youtu.be/u_GQSEjis48) · **date:** 2024-11-02 · **length:** 20:18 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed in transcript) · **orgs:** Better Stack
- **topics:** dev-tools · **tags:** typescript, nodejs, tsconfig, tsc, tsx, migration, allowjs, checkjs, source-maps, express, npm

> Walkthrough of adding TypeScript to a Node/Express project: install tsc and @types/node, extend a community base tsconfig, migrate JS incrementally, and run tsx watch mode for development without a compile step.

## Summary
The video sets up TypeScript for an existing Node project with Express, Axios and Morgan. It installs the TypeScript compiler and @types/node as dev dependencies, then replaces the generated tsc --init defaults with a community base config (@tsconfig/node20) that the project extends. Project-specific options cover outDir dist, allowJs for migration, an include of source/**/* and an exclude of node_modules. It then shows how to migrate JavaScript incrementally with checkJs and per-file comment directives, and how to fix missing type declarations for third-party libraries with @types packages. For development it installs tsx for running TypeScript directly in watch mode, paired with a separate tsc --watch --noEmit terminal for type errors, and notes that tsx is not for production. The content is basic and beginner-oriented, and it is a tutorial with no sponsor segment.

## Key ideas
- **Node cannot run .ts files, so tsc must compile source to JavaScript first, and the project must run from the compiled output.** — The compiler reads the include folder, strips type annotations, and writes JS to outDir. Scripts must point at dist/, for example node dist/example.js, and a build script can chain tsc before node. ([6:47](https://youtu.be/u_GQSEjis48?t=407))
- **Install @types/node because Node's own APIs (console, fetch) have no bundled declarations.** — Without @types/node, TypeScript reports errors when Node globals are used. Third-party libraries may need their own @types packages, such as @types/express and @types/morgan. ([1:11](https://youtu.be/u_GQSEjis48?t=71))
- **Discard the tsc --init defaults and extend a community base tsconfig matched to the Node major version.** — The speaker deletes the generated compilerOptions and extends a runtime-specific base config. That base covers Node 10 through 22, and the project then only overrides what it needs. ([2:11](https://youtu.be/u_GQSEjis48?t=131))
- **allowJs and checkJs make a large JS-to-TS migration incremental rather than all at once.** — checkJs type-checks JS files. Per-file // @ts-nocheck or // @ts-check opt files in or out, // @ts-ignore suppresses one line, and // @ts-expect-error suppresses one line but warns when it is no longer needed. The speaker treats all of these as temporary. ([11:25](https://youtu.be/u_GQSEjis48?t=685))
- **By default tsc still emits JavaScript even when there are type errors, so a broken build can still run.** — The speaker shows that a type error prints but still emits the file. noEmitOnError stops emission on errors. It is not used in the demo because a later tool covers the same check. ([8:00](https://youtu.be/u_GQSEjis48?t=480))
- **Enable sourceMap so the debugger maps the compiled JS back to the original TS lines.** — After conversion, line numbers in the emitted JS shift. The .map files let a debugger such as VS Code's point at the correct TypeScript line. ([15:41](https://youtu.be/u_GQSEjis48?t=941))
- **Development loop: tsx watch runs TS directly, and a separate tsc --watch --noEmit terminal reports type errors without writing dist files.** — tsx (TypeScript execute) replaces nodemon for development. The speaker states that tsx should not be used in production, where tsc output is run with node. ([18:11](https://youtu.be/u_GQSEjis48?t=1091))

## Techniques
- **Install TypeScript and Node typings** — npm install -D typescript @types/node. Check with npx tsc -v and get the Node major version with node -v. Install a matching base config with npm install -D @tsconfig/node20 (use the Node major you run). *When:* Starting TypeScript in any new or existing Node project.
- **Minimal project tsconfig.json** — Delete the generated compilerOptions from tsc --init, then set: "extends": "@tsconfig/node20/tsconfig.json" (at the top), "compilerOptions": {"outDir": "dist", "allowJs": true (only while migrating), "sourceMap": true}, "include": ["source/**/*"], "exclude": ["node_modules"]. Remove allowJs once all files are .ts so new JS files raise errors. *When:* Configuring a project with a source/ folder and a dist/ build output. The base config owns the rest of the compiler options.
- **Build and run compiled output** — Run npx tsc to emit to dist/, then node dist/example.js. Add a script such as "build": "tsc && node dist/server.js" so the compiler always runs before the server starts. Point nodemon or the start script at dist/. *When:* Production runs, or any time you need the real compiled artifact.
- **Incremental JS-to-TS migration** — Set "checkJs": true with allowJs to type-check JS first. Install @types packages for third-party libraries that have no declarations (speaker uses @types/express and @types/morgan). Per file: // @ts-nocheck to skip a file, or drop checkJs and use // @ts-check per file to opt in. Per line: // @ts-ignore, or // @ts-expect-error (preferred, since it flags unused directives). Rename .js to .ts when the file is ready, then fix errors such as unknown results from external API calls by typing the response shape. *When:* Migrating a larger JavaScript codebase that cannot be converted in one pass.
- **Dev loop with tsx and a type-check watcher** — npm install -D tsx. Script: "dev": "tsx watch source/server.ts". In a second terminal run npx tsc --watch --noEmit to report type errors on save without rewriting dist/. *When:* Local development where you want instant restarts on save and type feedback without a compile step. Do not use tsx in production.
- **Safer emit on error** — Set "noEmitOnError": true in compilerOptions (or pass --noEmitOnError). Compilation then writes no JS when there are type errors. *When:* CI or build scripts where a type error should block the output. The speaker does not use it in the demo.

## Numbers
- TypeScript 5.5.4 installed in the demo ([2:11](https://youtu.be/u_GQSEjis48?t=131))
- tsconfig/bases base configs cover Node 10 through Node 22 ([3:32](https://youtu.be/u_GQSEjis48?t=212))
- Demo runs on Node 20 (speaker also says he uses Node 21 at this point, so the transcript is inconsistent) ([3:32](https://youtu.be/u_GQSEjis48?t=212))
- No performance, latency or cost benchmarks are given; the only figures are version numbers ([2:11](https://youtu.be/u_GQSEjis48?t=131))

## Hot takes
- Advises discarding tsc --init defaults and extending a community base config instead of hand-writing compiler options (2:11).
- Calls // @ts-expect-error a better choice than // @ts-ignore because it reports directives that are no longer needed (12:47).
- Says tsx is fine for development but should not be used in production; run tsc output with node instead (18:11).

## Tools mentioned
TypeScript (tsc), 5.5.4 shown in the demo, @types/node, @types/express, @types/morgan, @tsconfig/node20 (community base tsconfig, tsconfig/bases repo), tsx (TypeScript execute), npm, Node.js 20 (speaker also mentions Node 21 at 3:32), Express, Axios, Morgan, nodemon, VS Code
