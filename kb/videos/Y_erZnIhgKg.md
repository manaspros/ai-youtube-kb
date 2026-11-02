# Bash Script BEST Practices You Need to Know, According to Google

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Y_erZnIhgKg` · [watch](https://youtu.be/Y_erZnIhgKg) · **date:** 2025-11-02 · **length:** 4:14 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Google, Better Stack
- **topics:** dev-tools · **tags:** bash, shell-scripting, shellcheck, style-guide, linting, linux, python

> Better Stack summarizes ten takeaways from Google's Shell Style Guide: move long scripts to Python, brace variables, prefer [[ ]], declare locals carefully, and run ShellCheck. Short recap with no code shown.

## Summary
The creator walks through ten recommendations from Google's public Shell Style Guide in a four-minute video. The core advice is to stop writing Bash once a script passes about 100 lines and move to Python, which is preinstalled on most modern Linux distributions. Other points cover script hygiene (a purpose comment below the shebang, two-space indentation, no tabs, 80-character lines, heredocs for long strings) and readability (one pipeline segment per line, braced variables, arrays only for simple argument lists, functions instead of aliases). The last points are correctness habits: use [[ ]] instead of [ ], declare function variables as local on a separate line from command substitution so exit codes are not masked, and run ShellCheck. The video shows no runnable code, so the guidance is only as detailed as the spoken summary.

## Key ideas
- **Stop writing Bash once a script goes past roughly 100 lines** — Bash is hard to maintain and debug at that size. The speaker recommends Python, which is installed by default on modern Linux distributions. ([0:00](https://youtu.be/Y_erZnIhgKg?t=0))
- **Give every script a purpose comment below the shebang** — A short overview lets a first-time reader understand what the script does. ([0:00](https://youtu.be/Y_erZnIhgKg?t=0))
- **Use fixed formatting rules: two-space indent, no tabs, 80-column lines** — For long string literals, use a here-document, or embedded newlines if the script can tolerate many backslashes. ([0:00](https://youtu.be/Y_erZnIhgKg?t=0))
- **Split long pipelines and logical chains one segment per line** — Pipes or operators start each new line, indented two spaces. Very short pipelines can stay on one line. ([1:15](https://youtu.be/Y_erZnIhgKg?t=75))
- **Always brace variable references, except positional and special parameters** — Braced variables are easier to read, safer in string concatenation and loops, and easier to debug. ([1:15](https://youtu.be/Y_erZnIhgKg?t=75))
- **Keep arrays for simple lists such as command arguments, not complex data** — If you need richer data structures, the speaker says to switch to Python. Strings do not work for list-style arguments. ([1:15](https://youtu.be/Y_erZnIhgKg?t=75))
- **Avoid aliases in scripts and use functions instead** — Aliases can hide the real command, and they expand once at definition time, so a value like $RANDOM inside an alias is fixed. A function avoids both problems. ([1:15](https://youtu.be/Y_erZnIhgKg?t=75))
- **Prefer [[ ]] over [ ] for tests** — Double brackets support logical operators and pattern matching, and they avoid the word-splitting failures single brackets have with unquoted variables. ([2:37](https://youtu.be/Y_erZnIhgKg?t=157))
- **Declare function variables as local, and split the declaration from command substitution** — Writing local and the assignment on one line makes local's exit status replace the command's, hiding failures. Declaring first, then assigning, keeps the real exit code. ([2:37](https://youtu.be/Y_erZnIhgKg?t=157))
- **Run ShellCheck to catch warnings and bugs** — It is available as a web version, through a package manager for the terminal, and as a VS Code extension. ([2:37](https://youtu.be/Y_erZnIhgKg?t=157))

## Techniques
- **Move long scripts to Python** — Once a Bash script passes about 100 lines, or needs structured data beyond simple arrays, rewrite it in Python (preinstalled on most modern Linux distros). *When:* Any shell script that is growing, is hard to debug, or manipulates complex data.
- **Purpose comment after the shebang** — Put a short comment directly below the shebang line that states what the script does. *When:* Every script that someone else may read.
- **Formatting baseline** — Indent with two spaces, never tabs. Keep lines at 80 characters. For long literal strings, use a here-document; use embedded newlines if many backslashes are acceptable. *When:* All scripts, to match Google's shell style guide.
- **One pipeline stage per line** — Split any non-trivial pipeline so each command is on its own line, with the leading pipe indented two spaces. Apply the same layout to && and || chains. *When:* Pipelines that would be hard to read on one line. Very short ones can stay on one line.
- **Brace all variable references** — Write ${var} rather than $var. Use unbraced form only for positional parameters such as $1 and for special parameters such as $@ or $?. *When:* Every variable reference in a script, especially inside string concatenation and loops.
- **Arrays only for flat argument lists** — Store the arguments for a command in an array and expand it there, rather than building a string. *When:* Passing a variable number of arguments to a command. For nested or record-style data, use Python instead.
- **Functions instead of aliases in scripts** — Replace any alias used in a script with a function of the same name, so the command stays visible and the body runs on every call. *When:* Scripts that need a reusable shortcut for a command. Aliases stay in interactive shell config.
- **Double brackets for conditionals** — Write [[ ... ]] for file, string and numeric tests. Use it for logical operators (&&, ||) and pattern matching, and rely on it not to word-split unquoted variables. *When:* Any conditional in a Bash script.
- **Local variables with separate command substitution** — Inside a function, declare with local on one line, then assign the command substitution on the next line, e.g. declare local var first, then var=$(cmd). *When:* Any function that stores the output of a command, so its exit status is not masked by local.
- **Lint scripts with ShellCheck** — Paste the script into the ShellCheck website, install it through the system package manager, or add the VS Code extension, then fix its warnings. *When:* Before committing or running any Bash script. The speaker presents it as the final and most important step.

## Numbers
- Recommended size threshold for abandoning Bash: about 100 lines ([0:00](https://youtu.be/Y_erZnIhgKg?t=0))
- Indentation: 2 spaces, no tabs. Maximum line length: 80 characters ([0:00](https://youtu.be/Y_erZnIhgKg?t=0))
- Video length: 4:14, covering 10 takeaways from the style guide ([0:00](https://youtu.be/Y_erZnIhgKg?t=0))

## Hot takes
- Bash scripts longer than about 100 lines should be rewritten in Python.
- Aliases should stay out of scripts entirely; use functions instead.
- The video is a recap of Google's public style guide with no code demonstrations, so it is thin on how-to detail.

## Tools mentioned
Bash, Python, ShellCheck, VS Code, Google Shell Style Guide

## Relevance to our work
- **agentos** (1/3): AgentOS has shell-based ops and benchmark helpers that could follow the same rules, but most of the stack is Python and Rust. → *Run ShellCheck over any repo shell scripts (launch, deploy, or load-test helpers) and move any script longer than ~100 lines to Python.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI and may include shell helpers for checkpoints, loops, or schedules. → *Add ShellCheck to ProsHarness's shell helpers and check the local/command-substitution pattern in any function that captures command output.*
