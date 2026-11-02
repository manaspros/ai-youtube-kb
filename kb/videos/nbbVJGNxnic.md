# NuShell - A New Type of Shell

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `nbbVJGNxnic` · [watch](https://youtu.be/nbbVJGNxnic) · **date:** 2025-11-02 · **length:** 7:15 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** dev-tools · **tags:** nushell, shell, terminal, structured-data, pipelines, cli, powershell, homebrew, data-manipulation

> A walkthrough of Nushell, a shell and programming language where every command emits structured data, so you can sort, filter, convert and explore pipelines by column type instead of by text.

## Summary
The presenter introduces Nushell as a shell that doubles as a programming language, with its main strength being that every command outputs structured, typed data rather than text. The demo covers piping ls into sort-by and reverse to sort files by size, and shows that Nushell knows the size column is a filesize, so it sorts 577 bytes below 26.8 KB, unlike a string sort. Filtering is shown with processes piped into where, and the speaker lists other filter commands (any, first, find, every). Output can be converted to JSON, CSV or YAML, and files such as package.json can be loaded with open and queried with get. The $in placeholder is used to place a piped value into a command that takes multiple arguments, and the error messages underline the bad token and suggest a fix. The explore command provides an interactive table view for building pipelines, and --help plus F1 give command examples. The speaker recommends installing Nushell alongside your main shell rather than replacing it. This is a short, demo-only intro with no benchmarks or discussion of tradeoffs.

## Key ideas
- **Every Nushell command outputs structured data, not text** — The table view from ls is not the point. What matters is that output is data that later commands can manipulate. ([0:00](https://youtu.be/nbbVJGNxnic?t=0))
- **Pipelines operate on typed columns, so sorting is type-aware** — ls | sort-by size | reverse sorts files largest to smallest. Nushell knows the size column is a filesize type, so it sorts correctly. ([0:00](https://youtu.be/nbbVJGNxnic?t=0))
- **Typed sorting avoids string-sort errors** — The speaker contrasts this with tools that sort as strings or numbers, where 577 bytes ranks above 26.8 KB. ([1:09](https://youtu.be/nbbVJGNxnic?t=69))
- **describe exposes the column types** — Piping into describe shows that name is a string, size is a filesize, and modified is a date shown in a human-readable form. ([1:09](https://youtu.be/nbbVJGNxnic?t=69))
- **Filtering is pipe-based with built-in predicate commands** — The processes command lists all processes, and piping into where status == running narrows it to running ones. The speaker also lists any, first, find and every. ([1:09](https://youtu.be/nbbVJGNxnic?t=69))
- **Input and output formats are converted through commands** — to json, to csv and to yaml change the output format. open loads files like package.json as tables, and get pulls out a field such as version. ([2:30](https://youtu.be/nbbVJGNxnic?t=150))
- **$in places a piped value into commands with several arguments** — $in holds the previous command's output. It can be used as a whole value, or as an object with .name, to feed commands like cp that do not take piped input. ([3:44](https://youtu.be/nbbVJGNxnic?t=224))
- **Errors point at the exact token and suggest a fix** — A mistyped column name is underlined and the shell offers a 'did you mean name?' suggestion. ([3:44](https://youtu.be/nbbVJGNxnic?t=224))
- **explore is an interactive table view for building pipelines** — You can iterate on a filter in the table view without re-editing the history line, and pipe any command's output into explore. ([5:02](https://youtu.be/nbbVJGNxnic?t=302))

## Techniques
- **Sort and reverse typed columns** — ls | sort-by size | reverse. sort-by uses the column's type, and reverse then flips the order. *When:* Sorting by size, date or other typed data where text or lexical sorting would give wrong results.
- **Filter a command's table with where** — processes | where status == running. Other filters mentioned by the speaker: any, first, find, every. *When:* Narrowing the output of a built-in command that returns a table, such as process or file listings.
- **Convert output to another format** — Append | to json, | to csv or | to yaml to the pipeline. Load files as tables with open package.json | get version. *When:* Exporting pipeline results for other tools, or reading structured config files directly.
- **Use $in when a command does not take piped input** — Pipe the value into a command that takes arguments, then reference it as $in in the argument list. The speaker's example pipes ls through where, first and get name, then runs cp $in large2.json. Exact filter literal not clearly spoken; reconstructed from narration. Alternative: $in.name when the value is a record. *When:* Passing a piped value to a normal (non-Nushell) or multi-argument command, while keeping control of where the value goes.
- **Build complex pipelines interactively with explore** — Type explore, then :try to get a REPL-style view, enter a command, and page through rows and columns with the keyboard. Or run ls | explore to view any output as a table. *When:* Building or debugging a long pipeline without re-editing history.
- **Discover commands and examples from the shell** — Run <command> --help for usage examples (the speaker's example lists directories not modified in 7 days). Run help commands to list all built-ins. Press F1 to browse commands, select an example and press Enter to pre-fill it. *When:* Learning Nushell idioms or finding the right built-in for a task.
- **Run Nushell alongside your existing shell** — Install via Homebrew (the exact formula is not shown), then start it with the nu command while keeping your main shell as default. *When:* Trying Nushell without switching your default shell, as the speaker does.

## Numbers
- Nushell ships with 432 built-in commands ([6:27](https://youtu.be/nbbVJGNxnic?t=387))
- String or number sorting can rank 577 bytes ahead of 26.8 KB, which Nushell's typed sort avoids ([1:09](https://youtu.be/nbbVJGNxnic?t=69))
- Video length is 7:15 and it is a single-session demo with no benchmarks ([0:00](https://youtu.be/nbbVJGNxnic?t=0))

## Hot takes
- Install Nushell alongside your main shell instead of replacing it. The speaker runs it this way and calls it the first shell they see many use cases for.
- The structured tables are not the killer feature. Pipeline manipulation of typed data is.
- Nushell is 'superb' for working with structured data, and developers who document their commands well earn praise. The demos are toy examples, so the claims about daily use are not tested.

## Tools mentioned
Nushell (nu), Homebrew, PowerShell (mentioned for comparison only), ls, sort-by, reverse, describe, processes, where, first, find, any, every, get, to json, to csv, to yaml, open, cp, explore, help, date
