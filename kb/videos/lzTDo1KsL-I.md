# The BEST Shell You’re Not Using - Fish

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `lzTDo1KsL-I` · [watch](https://youtu.be/lzTDo1KsL-I) · **date:** 2025-11-02 · **length:** 9:48 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** dev-tools · **tags:** fish, shell, bash, zsh, ghostty, macos, shell-scripting, autosuggestions, abbreviations, posix, fish_config

> Walkthrough of the fish shell's out-of-the-box features (autosuggestions, highlighting, abbreviations, history, config UI) and its main tradeoff: scripting syntax that is intentionally not POSIX.

## Summary
The presenter, a Mac user installing via MacPorts and running fish in Ghostty, shows what fish provides with no plugins: live syntax highlighting that marks invalid commands red and valid paths underlined, history- and path-aware autosuggestions, and tab completion with option descriptions. He covers fish_update_completions for regenerating completions after installing software, abbreviations that expand on space so history stores the real command, Ctrl+R history search, and a private mode that keeps commands out of history. Other built-ins he highlights are automatic cd by typing a path, directory history navigation, a prompt that shows git state and error codes, and fish_config, which opens a local web UI for theme, prompt, functions, variables and keybindings. He then compares fish scripting with bash (set instead of assignment, for/end instead of for/do/done, better handling of spaces in filenames, the string command, fish_indent). The main negative is that fish is intentionally not POSIX compatible, so it is not a default and bash-only habits break; his workaround is to keep writing bash scripts with a bash shebang and stay on bash for portability across teams and servers. The video is a short, unsponsored intro with no benchmarks.

## Key ideas
- **Fish ships with autosuggestions and syntax highlighting enabled, with no plugin installs or config files needed.** — The presenter argues this is what he wanted from zsh or bash plugin setups, available immediately after install. ([0:00](https://youtu.be/lzTDo1KsL-I?t=0))
- **Highlighting catches typos before Enter: invalid commands show in red and valid paths are underlined.** — Shown with a mistyped grep command and a valid path. ([0:00](https://youtu.be/lzTDo1KsL-I?t=0))
- **Autosuggestions draw on history, paths and options, and tab completion shows option descriptions.** — Suggestions are tailored to what the user ran earlier in the same folder. fish_update_completions regenerates completion files from installed man pages. ([1:09](https://youtu.be/lzTDo1KsL-I?t=69))
- **Abbreviations expand when you press space, so history records the full command rather than the short name.** — The presenter's point is that this suits shared machines, since new team members see the real command rather than an alias. ([2:25](https://youtu.be/lzTDo1KsL-I?t=145))
- **Interactive history search with Ctrl+R, plus a private mode for keeping commands out of history.** — Private mode stops commands being saved to history or disk, which helps when screen sharing or typing secrets. Leaving private mode with exit returns to the previous session. ([3:14](https://youtu.be/lzTDo1KsL-I?t=194))
- **Built-in navigation and prompt features remove the need for plugins: typing a path cds into it, directory history is browsable, and the prompt shows git state and the last error code.** — Directory history can be navigated with previous/next commands, Alt+Left/Right, or cdh to pick a folder by number. ([3:14](https://youtu.be/lzTDo1KsL-I?t=194))
- **fish_config starts a local web server with a settings UI covering theme, prompt, functions, variables, history and keybindings.** — The presenter calls this an unusual configuration approach for a shell. ([5:36](https://youtu.be/lzTDo1KsL-I?t=336))
- **Scripting syntax differs from bash, and the presenter's main objection is that fish is intentionally not POSIX compatible.** — Bash scripts still run if they carry a bash shebang. He keeps bash for portability across teams and servers because fish is not a default shell. ([7:47](https://youtu.be/lzTDo1KsL-I?t=467))

## Techniques
- **Install fish and try it as your interactive shell** — Presenter installed via MacPorts on macOS. Packages also exist for Linux, BSD and Windows via WSL. Launch fish from your terminal, such as Ghostty. Features like highlighting and autosuggestions work with no config. *When:* When you want a zero-plugin interactive shell with suggestions and highlighting built in.
- **Regenerate completions after installing software** — Run `fish_update_completions`, which reads installed man pages and writes completion files into the fish config directory. *When:* After installing new CLI tools, so tab completion and option descriptions work for them.
- **Define abbreviations instead of aliases** — Presenter's example: `abbr --add gco git checkout` (spoken as 'abbreviation --add'). Typing gco then space expands it in place, so history stores the full command. *When:* For short names of commands you use often, especially on shared machines where teammates should see what actually ran.
- **Run a private session that leaves no history** — Start with `fish --private` (spoken as 'fish --private' or '-P'). Commands are not saved to history or disk. Type `exit` to return to the normal session. *When:* When screen sharing or when a command includes a secret such as a database password.
- **Open the web-based config UI** — Run `fish_config` in a graphical environment. It starts a local web server and opens a page for theme, prompt, functions, variables, history and keybindings. *When:* When you want to change prompt, theme or keybindings without editing config files by hand.
- **Port simple bash scripts to fish syntax** — Replace `VAR=value` with `set VAR value`. Use `for f in *.txt` ... `end` instead of `do`/`done`. Use the `string` builtin for substitutions (presenter's example: `string replace` for swapping one word). Format a script with `fish_indent <script>`. Quoting spaces in filenames is handled without extra quotes. *When:* When writing new scripts that will only run under fish. For scripts that must run on other machines, keep bash with a shebang.
- **Keep bash scripts running under a shared shell** — Add `#!/bin/bash` (or your bash path) as the first line of each script. Fish runs the script with bash when the shebang names it, so bash syntax keeps working. *When:* When your default interactive shell is fish but scripts must stay portable across teams and servers.

## Hot takes
- Fish's built-in features (suggestions, highlighting, git and error info in the prompt) replace the plugin setups that bash and zsh users normally need.
- Non-POSIX syntax is a deal-breaker for many users, and the presenter still sticks to bash for cross-team and server portability.
- The presenter says fish's syntax will be divisive and that you have to try it to decide.

## Tools mentioned
fish shell, Ghostty, bash, zsh, MacPorts, WSL, grep, node

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI and may run shell scripts or hooks; fish is not POSIX, so bash-style syntax needs an explicit bash shebang if fish is the user's login shell. → *Pin any ProsHarness shell scripts and hooks to #!/bin/bash, and test them under a fish login shell before relying on them.*
