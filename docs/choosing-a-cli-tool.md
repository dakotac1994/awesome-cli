# Choosing a CLI Tool

How to pick the right command-line tool without regretting it later.

## 1. Start with your package manager

The best CLI tool is the one you can install and update in one command. Before falling in love with a tool, check it's in your package manager: Homebrew (`brew install`), apt/dnf/pacman, Winget/Scoop/Chocolatey, or a language toolchain (`cargo install`, `go install`, `pipx install`, `npm i -g`). Tools distributed only as manual downloads rot faster.

## 2. Check the license honestly

This list labels every tool's license as verified on 2026-09-30. `proprietary` means the tool is closed-source — fine for daily use, but think twice before building automation or a business on top of it. Copyleft licenses (GPL/AGPL) matter if you redistribute the tool or embed it in a product.

## 3. Mind the runtime

Rust and Go tools ship as single static binaries — no runtime to install, fast startup. Python tools need a Python environment (prefer `pipx` over `pip install --user`). Node tools need Node. For scripts you run hundreds of times a day, startup time matters.

## 4. Shell integration

The best modern CLI tools ship shell completions and integrate with your prompt (starship, etc.). Check for `completions/` in the repo or a `completions` subcommand before committing.

## 5. TUI vs. plain CLI

TUI (terminal user interface) tools like lazygit or yazi are interactive and discoverable; plain CLIs like ripgrep or jq compose better in scripts and pipes. Know which job you're hiring for.

## 6. Maintenance signals

Look at the commit history: steady commits in the last few months beat a burst two years ago. This list re-verifies activity on a schedule and moves dead projects to `status-changes.md` rather than leaving them in the list.

## 7. Try before you alias

Live with a tool for a week before aliasing it over the built-in (`ls`, `cat`, `find`). The modern replacements are genuinely better, but muscle memory is real — give it a fair trial.
