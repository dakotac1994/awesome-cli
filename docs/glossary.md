# Glossary

Terms you'll meet in the command-line world.

- **CLI** — Command-Line Interface. A program you operate by typing commands, as opposed to clicking.
- **TUI** — Terminal User Interface. A text-based interactive interface inside the terminal (menus, lists, mouse support) — e.g., lazygit, htop. Richer than a plain CLI, lighter than a GUI.
- **REPL** — Read-Eval-Print Loop. An interactive prompt that executes what you type immediately (Python, Node, database shells).
- **Pipe (`|`)** — Sends one program's output into another's input. The Unix superpower: small tools composed into pipelines.
- **Stdout / stderr** — Standard output (the result) and standard error (diagnostics). Well-behaved CLIs keep them separate so pipes only carry data.
- **Exit code** — A number a program returns when it finishes; `0` means success. Scripts branch on it.
- **Flag / option** — A modifier like `--verbose` or `-v`. Single dash + letter is the short form; double dash + word is the long form.
- **Subcommand** — A verb after the program name, e.g., `git commit`, `kubectl get`. Modern CLIs are organized this way.
- **Man page** — The built-in manual (`man rg`). The fastest authoritative documentation.
- **Shell completion** — Tab-completion definitions for a tool's flags and subcommands, installed into your shell.
- **Dotfiles** — Your shell and tool configuration files (`~/.zshrc`, `~/.config/...`), often version-controlled.
- **Multiplexer** — A tool (tmux, zellij) that manages multiple terminal sessions in one window, with persistence across disconnects.
- **Prompt** — The text your shell shows before each command (customized by starship, powerlevel10k, etc.).
- **Static binary** — A compiled program with no external dependencies. Rust and Go CLIs ship this way: download and run.
- **Copyleft** — Licenses (GPL, AGPL) requiring derivative works to stay open. Matters if you redistribute or embed the tool.
- **Source-available** — You can read the source, but the license restricts use (not open source). Labeled honestly in this list wherever it appears.
