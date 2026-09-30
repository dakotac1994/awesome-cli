# Awesome CLI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of **110 command-line tools** — shells, TUIs, CLIs, cloud CLIs, AI coding assistants, and the frameworks for building them. Every license was verified against an official source on 2026-09-30; proprietary tools are explicitly labeled `proprietary`.

- ✅ **110/110** licenses verified from official sources
- 🧰 **9** frameworks for building CLIs
- 🔒 **6** proprietary-but-notable tools, honestly labeled
- 📦 Machine-readable data in [`data/cli.json`](data/cli.json)

## Contents

- [🐚 Shells and Prompts](#shells-and-prompts) (6)
- [🪟 Terminal Multiplexers](#terminal-multiplexers) (3)
- [🗂️ File and Navigation](#file-and-navigation) (7)
- [🔎 Search](#search) (4)
- [🌿 Git and VCS](#git-and-vcs) (7)
- [✏️ Editors](#editors) (5)
- [📊 System Monitoring](#system-monitoring) (6)
- [🌐 Networking and HTTP](#networking-and-http) (7)
- [🧮 Data, JSON and YAML](#data-json-and-yaml) (7)
- [📝 Text Processing](#text-processing) (7)
- [🎬 Media](#media) (7)
- [☁️ DevOps and Cloud CLIs](#devops-and-cloud-clis) (10)
- [🔐 Security and Secrets](#security-and-secrets) (9)
- [🤖 AI Coding CLIs](#ai-coding-clis) (7)
- [🧰 Frameworks for Building CLIs](#frameworks-for-building-clis) (9)
- [🔒 Proprietary but Notable](#proprietary-but-notable) (3)
- [🎉 Fun and Misc](#fun-and-misc) (6)
- [Notable exclusions](#notable-exclusions)
- [Related](#related)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## 🐚 Shells and Prompts

Command-line shells and prompt customizers.

- **[atuin](https://github.com/atuinsh/atuin)** — Sync, search and back up your shell history across machines. [`MIT`](https://github.com/atuinsh/atuin) ⭐ 31.9k [website](https://atuin.sh/) linux/macos
- **[bash](https://git.savannah.gnu.org/cgit/bash.git)** — The GNU Bourne-Again SHell — the default interactive shell on most Linux systems. [`GPL-3.0-or-later`](https://www.gnu.org/software/bash/) [website](https://www.gnu.org/software/bash/) linux/macos/windows
- **[fish](https://github.com/fish-shell/fish-shell)** — A friendly interactive shell with autosuggestions and sane scripting out of the box. [`GPL-2.0`](https://github.com/fish-shell/fish-shell) ⭐ 34.2k [website](https://fishshell.com/) linux/macos/windows
- **[nushell](https://github.com/nushell/nushell)** — A modern shell where everything is structured data instead of plain text. [`MIT`](https://github.com/nushell/nushell) ⭐ 40.6k [website](https://www.nushell.sh/) linux/macos/windows
- **[starship](https://github.com/starship/starship)** — A minimal, fast and endlessly customizable shell prompt. [`ISC`](https://github.com/starship/starship) ⭐ 60.1k [website](https://starship.rs/) linux/macos/windows
- **[zsh](https://github.com/zsh-users/zsh)** — A powerful interactive shell with advanced tab completion and globbing. [`MIT-style`](https://github.com/zsh-users/zsh) ⭐ 4.3k [website](https://www.zsh.org/) linux/macos/windows *Custom MIT-style license (LICENCE file), not verbatim MIT.*

## 🪟 Terminal Multiplexers

Manage multiple terminal sessions in one window.

- **[screen](https://git.savannah.gnu.org/cgit/screen.git)** — GNU's venerable terminal multiplexer for persistent remote sessions. [`GPL-3.0-or-later`](https://www.gnu.org/software/screen/) [website](https://www.gnu.org/software/screen/) linux/macos
- **[tmux](https://github.com/tmux/tmux)** — Terminal multiplexer: persistent sessions, windows and panes you can detach and reattach. [`ISC`](https://github.com/tmux/tmux) ⭐ 49.6k [website](https://github.com/tmux/tmux/wiki) linux/macos
- **[zellij](https://github.com/zellij-org/zellij)** — A Rust terminal workspace — multiplexer with layouts, plugins and floating panes. [`MIT`](https://github.com/zellij-org/zellij) ⭐ 35.6k [website](https://zellij.dev/) linux/macos

## 🗂️ File and Navigation

File managers, directory jumpers, and ls replacements.

- **[broot](https://github.com/Canop/broot)** — A tree-oriented file navigator and fuzzy searcher for large directory trees. [`MIT`](https://github.com/Canop/broot) ⭐ 13k [website](https://dystroy.org/broot/) linux/macos/windows
- **[eza](https://github.com/eza-community/eza)** — A modern, maintained replacement for ls with colors, icons and git integration. [`EUPL-1.2`](https://github.com/eza-community/eza) ⭐ 23.4k [website](https://eza.rocks/) linux/macos/windows
- **[fd](https://github.com/sharkdp/fd)** — A fast, user-friendly alternative to find with sensible defaults and colorized output. [`MIT OR Apache-2.0`](https://github.com/sharkdp/fd) ⭐ 44.6k linux/macos/windows
- **[fzf](https://github.com/junegunn/fzf)** — A general-purpose command-line fuzzy finder for files, history and anything piped in. [`MIT`](https://github.com/junegunn/fzf) ⭐ 83.3k [website](https://junegunn.github.io/fzf/) linux/macos/windows
- **[ranger](https://github.com/ranger/ranger)** — Console file manager with vi key bindings, previews and a Miller-column view. [`GPL-3.0`](https://github.com/ranger/ranger) ⭐ 17.4k [website](https://ranger.github.io/) linux/macos
- **[yazi](https://github.com/sxyazi/yazi)** — A blazing-fast terminal file manager written in Rust, with image previews. [`MIT`](https://github.com/sxyazi/yazi) ⭐ 42.5k [website](https://yazi-rs.github.io/) linux/macos
- **[zoxide](https://github.com/ajeetdsouza/zoxide)** — A smarter cd command that learns your habits and jumps to frecent directories. [`MIT`](https://github.com/ajeetdsouza/zoxide) ⭐ 39.8k linux/macos/windows

## 🔎 Search

Find files and text at speed.

- **[ag](https://github.com/ggreer/the_silver_searcher)** — The Silver Searcher — a fast code-searching tool built for programmers. [`Apache-2.0`](https://github.com/ggreer/the_silver_searcher) ⭐ 27.1k [website](https://geoff.greer.fm/ag/) linux/macos/windows
- **[ast-grep](https://github.com/ast-grep/ast-grep)** — Structural search and rewrite for code — grep that understands syntax trees. [`MIT`](https://github.com/ast-grep/ast-grep) ⭐ 16.1k [website](https://ast-grep.github.io/) linux/macos/windows
- **[ripgrep](https://github.com/BurntSushi/ripgrep)** — An extremely fast recursive search tool that respects your gitignore. [`MIT OR Unlicense`](https://github.com/BurntSushi/ripgrep) ⭐ 68.7k linux/macos/windows
- **[skim](https://github.com/lotabout/skim)** — A fuzzy finder in Rust, similar to fzf, usable as a library or filter. [`MIT`](https://github.com/lotabout/skim) ⭐ 7k linux/macos

## 🌿 Git and VCS

Version control from the terminal.

- **[delta](https://github.com/dandavison/delta)** — A syntax-highlighting pager for git, diff and grep output. [`MIT`](https://github.com/dandavison/delta) ⭐ 32.4k linux/macos/windows
- **[gh](https://github.com/cli/cli)** — GitHub's official command-line tool for issues, PRs, releases and more. [`MIT`](https://github.com/cli/cli) ⭐ 46.5k [website](https://cli.github.com/) linux/macos/windows
- **[gitui](https://github.com/extrawurst/gitui)** — A blazing-fast terminal UI for git written in Rust. [`MIT`](https://github.com/extrawurst/gitui) ⭐ 22.5k linux/macos/windows
- **[glab](https://gitlab.com/gitlab-org/cli)** — An open-source GitLab CLI that brings merge requests and CI to your terminal. [`MIT`](https://gitlab.com/gitlab-org/cli/-/raw/main/LICENSE) [website](https://glab.readthedocs.io/) linux/macos/windows *Upstream moved from github.com/profclems/glab (archived) to gitlab.com/gitlab-org/cli after GitLab adopted it.*
- **[jj](https://github.com/jj-vcs/jj)** — Jujutsu — a Git-compatible version control system with a simpler mental model. [`Apache-2.0`](https://github.com/jj-vcs/jj) ⭐ 31.8k [website](https://jj-vcs.github.io/jj/) linux/macos/windows
- **[lazygit](https://github.com/jesseduffield/lazygit)** — A simple, keyboard-driven TUI for git commands. [`MIT`](https://github.com/jesseduffield/lazygit) ⭐ 82.8k linux/macos/windows
- **[tig](https://github.com/jonas/tig)** — A classic ncurses text-mode interface for git repositories. [`GPL-2.0-or-later`](https://github.com/jonas/tig) ⭐ 13.4k [website](https://jonas.github.io/tig/) linux/macos

## ✏️ Editors

Terminal text editors.

- **[emacs](https://git.savannah.gnu.org/cgit/emacs.git)** — The extensible, self-documenting editor — an OS disguised as an editor. [`GPL-3.0-or-later`](https://www.gnu.org/software/emacs/) [website](https://www.gnu.org/software/emacs/) linux/macos/windows
- **[helix](https://github.com/helix-editor/helix)** — A post-modern modal text editor inspired by Kakoune, written in Rust. [`MPL-2.0`](https://github.com/helix-editor/helix) ⭐ 46.4k [website](https://helix-editor.com/) linux/macos/windows
- **[kakoune](https://github.com/mawww/kakoune)** — A modal editor with multiple selections as the central editing primitive. [`Unlicense`](https://github.com/mawww/kakoune) ⭐ 11.1k [website](https://kakoune.org/) linux/macos
- **[neovim](https://github.com/neovim/neovim)** — A hyperextensible, Vim-based text editor built for the modern terminal. [`Apache-2.0`](https://github.com/neovim/neovim) ⭐ 102.7k [website](https://neovim.io/) linux/macos/windows
- **[vim](https://github.com/vim/vim)** — The ubiquitous, highly configurable modal text editor. [`Vim`](https://www.vim.org/about.php) ⭐ 41k [website](https://www.vim.org/) linux/macos/windows

## 📊 System Monitoring

Watch processes, disks, networks, and resources.

- **[bandwhich](https://github.com/imsnif/bandwhich)** — Shows current network bandwidth utilization by process, connection and host. [`MIT`](https://github.com/imsnif/bandwhich) ⭐ 12k linux/macos
- **[btop](https://github.com/aristocratos/btop)** — A beautiful, themeable resource monitor with mouse support. [`Apache-2.0`](https://github.com/aristocratos/btop) ⭐ 34.8k linux/macos
- **[duf](https://github.com/muesli/duf)** — A better df — disk usage and free space with colors and a clean table. [`MIT`](https://github.com/muesli/duf) ⭐ 15.3k linux/macos/windows
- **[glances](https://github.com/nicolargo/glances)** — A cross-platform system monitoring tool with a curses and web interface. [`LGPL-3.0`](https://github.com/nicolargo/glances) ⭐ 33.7k [website](https://nicolargo.github.io/glances/) linux/macos/windows
- **[htop](https://github.com/htop-dev/htop)** — An interactive, full-screen process viewer and system monitor. [`GPL-2.0-or-later`](https://github.com/htop-dev/htop) ⭐ 8.4k [website](https://htop.dev/) linux/macos
- **[procs](https://github.com/dalance/procs)** — A modern replacement for ps with color, multi-column and tree views. [`MIT`](https://github.com/dalance/procs) ⭐ 6.2k linux/macos/windows

## 🌐 Networking and HTTP

Requests, tunnels, and network diagnostics.

- **[aria2](https://github.com/aria2/aria2)** — A lightweight, multi-protocol download utility with metalink and BitTorrent support. [`GPL-2.0-or-later`](https://github.com/aria2/aria2) ⭐ 42.9k [website](https://aria2.github.io/) linux/macos/windows
- **[curl](https://github.com/curl/curl)** — The ubiquitous command-line tool for transferring data with URLs. [`curl`](https://github.com/curl/curl) ⭐ 43k [website](https://curl.se/) linux/macos/windows
- **[httpie](https://github.com/httpie/cli)** — A user-friendly HTTP client with a natural CLI syntax and pretty output. [`BSD-3-Clause`](https://github.com/httpie/cli) ⭐ 38.6k [website](https://httpie.io/) linux/macos/windows
- **[hurl](https://github.com/Orange-OpenSource/hurl)** — Run and test HTTP requests defined in a simple plain-text format. [`Apache-2.0`](https://github.com/Orange-OpenSource/hurl) ⭐ 19.2k [website](https://hurl.dev/) linux/macos/windows
- **[nmap](https://github.com/nmap/nmap)** — The standard network discovery and security auditing scanner. [`NPSL`](https://github.com/nmap/nmap) ⭐ 13.7k [website](https://nmap.org/) linux/macos/windows *NPSL (Nmap Public Source License) v0.95 — source-available, not OSI-approved.*
- **[wget](https://git.savannah.gnu.org/cgit/wget.git)** — GNU's non-interactive network downloader for files over HTTP/FTP. [`GPL-3.0-or-later`](https://www.gnu.org/software/wget/) [website](https://www.gnu.org/software/wget/) linux/macos
- **[wrk](https://github.com/wg/wrk)** — A modern HTTP benchmarking tool with Lua scripting. [`Apache-2.0`](https://github.com/wg/wrk) ⭐ 40.4k linux/macos *LICENSE file is titled 'Modified Apache 2.0 License Version 2.0.1' — Apache-2.0-derived permissive terms.*

## 🧮 Data, JSON and YAML

Slice, query, and transform structured data.

- **[csvkit](https://github.com/wireservice/csvkit)** — A suite of command-line tools for converting and wrangling CSV files. [`MIT`](https://github.com/wireservice/csvkit) ⭐ 6.4k [website](https://csvkit.readthedocs.io/) linux/macos
- **[dasel](https://github.com/TomWright/dasel)** — Query and modify JSON, YAML, TOML, XML and CSV with selector expressions. [`MIT`](https://github.com/TomWright/dasel) ⭐ 8k [website](https://daseldocs.tomwright.me/) linux/macos/windows
- **[duckdb](https://github.com/duckdb/duckdb)** — An in-process analytical database with a handy interactive SQL shell. [`MIT`](https://github.com/duckdb/duckdb) ⭐ 41.8k [website](https://duckdb.org/) linux/macos/windows
- **[jq](https://github.com/jqlang/jq)** — A lightweight command-line JSON processor with a tiny functional language. [`MIT`](https://github.com/jqlang/jq) ⭐ 35.7k [website](https://jqlang.github.io/jq/) linux/macos/windows
- **[miller](https://github.com/johnkerl/miller)** — Like awk, sed and sort for structured data: CSV, JSON, TSV and more. [`BSD-2-Clause`](https://github.com/johnkerl/miller) ⭐ 10k [website](https://miller.readthedocs.io/) linux/macos
- **[sqlite3](https://sqlite.org/src)** — The self-contained, serverless SQL database engine and its CLI shell. [`public-domain`](https://www.sqlite.org/copyright.html) [website](https://www.sqlite.org/) linux/macos/windows
- **[yq](https://github.com/mikefarah/yq)** — A portable jq wrapper for YAML, JSON, XML and TOML documents. [`MIT`](https://github.com/mikefarah/yq) ⭐ 16k [website](https://mikefarah.gitbook.io/yq/) linux/macos/windows

## 📝 Text Processing

View, convert, and summarize text and documents.

- **[bat](https://github.com/sharkdp/bat)** — A cat clone with syntax highlighting, git integration and paging. [`MIT OR Apache-2.0`](https://github.com/sharkdp/bat) ⭐ 60.6k linux/macos/windows
- **[glow](https://github.com/charmbracelet/glow)** — Render Markdown beautifully in the terminal. [`MIT`](https://github.com/charmbracelet/glow) ⭐ 27.5k linux/macos/windows
- **[gum](https://github.com/charmbracelet/gum)** — Glamorous building blocks — prompts, spinners and styling — for shell scripts. [`MIT`](https://github.com/charmbracelet/gum) ⭐ 24.4k linux/macos/windows
- **[navi](https://github.com/denisidoro/navi)** — An interactive cheatsheet tool: fuzzy-find commands and fill in arguments. [`Apache-2.0`](https://github.com/denisidoro/navi) ⭐ 17.7k linux/macos
- **[pandoc](https://github.com/jgm/pandoc)** — The universal document converter: Markdown, HTML, LaTeX, docx and dozens more. [`GPL-2.0-or-later`](https://github.com/jgm/pandoc) ⭐ 46.5k [website](https://pandoc.org/) linux/macos/windows
- **[sd](https://github.com/chmln/sd)** — An intuitive find-and-replace CLI with simpler syntax than sed. [`MIT`](https://github.com/chmln/sd) ⭐ 7.4k linux/macos/windows
- **[tealdeer](https://github.com/tealdeer-rs/tealdeer)** — A very fast tldr client that shows simplified, community-driven man pages. [`MIT OR Apache-2.0`](https://github.com/tealdeer-rs/tealdeer) ⭐ 6.6k [website](https://tealdeer-rs.github.io/tealdeer/) linux/macos/windows

## 🎬 Media

Audio, video, and image tools for the terminal.

- **[beets](https://github.com/beetbox/beets)** — The music library manager: autotags, organizes and deduplicates your collection. [`MIT`](https://github.com/beetbox/beets) ⭐ 15.7k [website](https://beets.io/) linux/macos
- **[cmus](https://github.com/cmus/cmus)** — A small, fast and powerful console music player. [`GPL-2.0-or-later`](https://github.com/cmus/cmus) ⭐ 6.3k [website](https://cmus.github.io/) linux/macos
- **[ffmpeg](https://github.com/FFmpeg/FFmpeg)** — The complete cross-platform solution to record, convert and stream audio/video. [`LGPL-2.1-or-later`](https://ffmpeg.org/legal.html) ⭐ 64.7k [website](https://ffmpeg.org/) linux/macos/windows *LGPL-2.1-or-later by default; GPL-2.0-or-later applies if built with --enable-gpl.*
- **[imagemagick](https://github.com/ImageMagick/ImageMagick)** — Create, edit, compose and convert bitmap images from the command line. [`ImageMagick`](https://imagemagick.org/license/) ⭐ 17.6k [website](https://imagemagick.org/) linux/macos/windows
- **[mpv](https://github.com/mpv-player/mpv)** — A free, keyboard-driven media player with powerful scripting. [`GPL-2.0-or-later`](https://github.com/mpv-player/mpv) ⭐ 37.2k [website](https://mpv.io/) linux/macos/windows
- **[sox](https://sourceforge.net/projects/sox/)** — The Swiss Army knife of sound processing: play, record and convert audio. [`GPL-2.0-or-later AND LGPL-2.1-or-later`](https://sox.sourceforge.net/) [website](https://sox.sourceforge.net/) linux/macos/windows
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** — A feature-rich downloader for YouTube and hundreds of other video sites. [`Unlicense`](https://github.com/yt-dlp/yt-dlp) ⭐ 194.5k linux/macos/windows

## ☁️ DevOps and Cloud CLIs

Infrastructure, containers, and cloud provider CLIs.

- **[ansible](https://github.com/ansible/ansible)** — Agentless IT automation for configuration management and deployments. [`GPL-3.0-or-later`](https://github.com/ansible/ansible) ⭐ 70.8k [website](https://www.ansible.com/) linux/macos
- **[aws-cli](https://github.com/aws/aws-cli)** — The unified command-line interface for Amazon Web Services. [`Apache-2.0`](https://github.com/aws/aws-cli) ⭐ 17.3k [website](https://aws.amazon.com/cli/) linux/macos/windows
- **[docker](https://github.com/docker/cli)** — The container platform's official CLI for building and running containers. [`Apache-2.0`](https://github.com/docker/cli) ⭐ 6.1k [website](https://www.docker.com/) linux/macos/windows
- **[gcloud](https://cloud.google.com/sdk)** — Google Cloud's official SDK command-line interface. `proprietary` linux/macos/windows *Free to download; governed by Google Cloud commercial terms.*
- **[helm](https://github.com/helm/helm)** — The package manager for Kubernetes charts. [`Apache-2.0`](https://github.com/helm/helm) ⭐ 30.3k [website](https://helm.sh/) linux/macos/windows
- **[k9s](https://github.com/derailed/k9s)** — A terminal UI to interact with your Kubernetes clusters. [`Apache-2.0`](https://github.com/derailed/k9s) ⭐ 34.7k [website](https://k9scli.io/) linux/macos/windows
- **[kubectl](https://github.com/kubernetes/kubectl)** — The command-line tool for controlling Kubernetes clusters. [`Apache-2.0`](https://github.com/kubernetes/kubectl) ⭐ 3.4k [website](https://kubernetes.io/docs/reference/kubectl/) linux/macos/windows
- **[opentofu](https://github.com/opentofu/opentofu)** — The open-source Terraform fork, maintained by the Linux Foundation. [`MPL-2.0`](https://github.com/opentofu/opentofu) ⭐ 30.3k [website](https://opentofu.org/) linux/macos/windows
- **[pulumi](https://github.com/pulumi/pulumi)** — Infrastructure as code using real programming languages. [`Apache-2.0`](https://github.com/pulumi/pulumi) ⭐ 25.7k [website](https://www.pulumi.com/) linux/macos/windows
- **[terraform](https://github.com/hashicorp/terraform)** — Infrastructure as code by HashiCorp — now under the BUSL source-available license. [`BUSL-1.1`](https://github.com/hashicorp/terraform) ⭐ 49.8k [website](https://www.terraform.io/) linux/macos/windows *Source-available under BUSL-1.1 (not OSI-approved); license now names IBM as licensor. OpenTofu is the MPL-2.0 fork.*

## 🔐 Security and Secrets

Encryption, secrets management, and security scanning.

- **[age](https://github.com/FiloSottile/age)** — A simple, modern and secure file encryption tool by Filippo Valsorda. [`BSD-3-Clause`](https://github.com/FiloSottile/age) ⭐ 23.8k linux/macos/windows
- **[bitwarden-cli](https://github.com/bitwarden/clients)** — Bitwarden's official command-line vault — fetch and manage secrets. [`GPL-3.0`](https://github.com/bitwarden/clients) ⭐ 13.9k [website](https://bitwarden.com/help/cli/) linux/macos/windows
- **[doppler](https://github.com/DopplerHQ/cli)** — A secrets-management platform with a first-class CLI for every environment. [`Apache-2.0`](https://github.com/DopplerHQ/cli) ⭐ 397 [website](https://www.doppler.com/) linux/macos/windows *CLI is Apache-2.0; requires Doppler's proprietary cloud service.*
- **[pass](https://git.zx2c4.com/password-store/)** — The standard Unix password manager: GPG-encrypted passwords in plain git. [`GPL-2.0-or-later`](https://www.passwordstore.org/) [website](https://www.passwordstore.org/) linux/macos
- **[semgrep](https://github.com/semgrep/semgrep)** — Fast static analysis that finds bugs and enforces code standards (open-core). [`LGPL-2.1`](https://github.com/semgrep/semgrep) ⭐ 16.8k [website](https://semgrep.dev/) linux/macos
- **[snyk](https://github.com/snyk/cli)** — Developer-first security scanning CLI with a free tier for open source. [`Apache-2.0`](https://github.com/snyk/cli) ⭐ 5.7k [website](https://snyk.io/) linux/macos/windows *CLI is Apache-2.0; the Snyk platform is commercial (free tier available).*
- **[sops](https://github.com/getsops/sops)** — Encrypt secrets inside YAML/JSON/INI files, with AWS/GCP/Azure/PGP backends. [`MPL-2.0`](https://github.com/getsops/sops) ⭐ 23.3k [website](https://getsops.io/) linux/macos/windows
- **[tailscale](https://github.com/tailscale/tailscale)** — Zero-config mesh VPN; the CLI manages your tailnet from the terminal. [`BSD-3-Clause`](https://github.com/tailscale/tailscale) ⭐ 37k [website](https://tailscale.com/) linux/macos/windows
- **[trivy](https://github.com/aquasecurity/trivy)** — Find vulnerabilities and misconfigurations in containers, filesystems and repos. [`Apache-2.0`](https://github.com/aquasecurity/trivy) ⭐ 38.1k [website](https://trivy.dev/) linux/macos/windows

## 🤖 AI Coding CLIs

AI assistants that live in your terminal. Licenses labeled honestly.

- **[aider](https://github.com/Aider-AI/aider)** — AI pair programming in your terminal, editing files in your git repo. [`Apache-2.0`](https://github.com/Aider-AI/aider) ⭐ 49.3k [website](https://aider.chat/) linux/macos
- **[amazon-q-developer-cli](https://github.com/aws/amazon-q-developer-cli)** — Amazon's AI coding assistant for the command line (successor to Fig/CodeWhisperer). [`Apache-2.0`](https://github.com/aws/amazon-q-developer-cli) ⭐ 2k [website](https://aws.amazon.com/q/developer/) linux/macos
- **[claude-code](https://github.com/anthropics/claude-code)** — Anthropic's agentic coding tool that lives in your terminal. `proprietary` ⭐ 148.7k [website](https://www.anthropic.com/claude-code) linux/macos/windows *Requires Claude Pro/Max or API billing; no open-source license.*
- **[codex-cli](https://github.com/openai/codex)** — OpenAI's open-source local coding agent for the terminal. [`Apache-2.0`](https://github.com/openai/codex) ⭐ 127.4k linux/macos
- **[gemini-cli](https://github.com/google-gemini/gemini-cli)** — Google's open-source AI agent that brings Gemini to the command line. [`Apache-2.0`](https://github.com/google-gemini/gemini-cli) ⭐ 107.2k linux/macos/windows
- **[github-copilot-cli](https://github.com/github/copilot-cli)** — GitHub Copilot's agentic CLI — ask it to explain, run and fix shell commands. `proprietary` ⭐ 11.2k [website](https://github.com/features/copilot/cli) linux/macos/windows *Requires a paid GitHub Copilot subscription; distributed under a custom license.*
- **[opencode](https://github.com/sst/opencode)** — An open-source, terminal-based AI coding agent. [`MIT`](https://github.com/sst/opencode) ⭐ 211.1k [website](https://opencode.ai/) linux/macos/windows

## 🧰 Frameworks for Building CLIs

Libraries for building command-line apps, by language.

- **[argparse](https://docs.python.org/3/library/argparse.html)** — Python's standard-library parser for command-line options and subcommands. [`PSF-2.0`](https://docs.python.org/3/license.html) linux/macos/windows
- **[bubbletea](https://github.com/charmbracelet/bubbletea)** — A Go framework for building terminal apps on the Elm architecture. [`MIT`](https://github.com/charmbracelet/bubbletea) ⭐ 45.2k linux/macos/windows
- **[clap](https://github.com/clap-rs/clap)** — The de-facto command-line argument parser for Rust. [`MIT OR Apache-2.0`](https://github.com/clap-rs/clap) ⭐ 16.7k [website](https://docs.rs/clap) linux/macos/windows
- **[click](https://github.com/pallets/click)** — Python's composable toolkit for building command-line interfaces. [`BSD-3-Clause`](https://github.com/pallets/click) ⭐ 17.8k [website](https://click.palletsprojects.com/) linux/macos/windows
- **[cobra](https://github.com/spf13/cobra)** — The standard library for creating powerful Go CLIs (used by kubectl, gh). [`Apache-2.0`](https://github.com/spf13/cobra) ⭐ 44.7k [website](https://cobra.dev/) linux/macos/windows
- **[commander.js](https://github.com/tj/commander.js)** — The complete solution for Node.js command-line interfaces. [`MIT`](https://github.com/tj/commander.js) ⭐ 28.4k linux/macos/windows
- **[typer](https://github.com/fastapi/typer)** — Build CLIs from Python type hints — the FastAPI of command-line apps. [`MIT`](https://github.com/fastapi/typer) ⭐ 20k [website](https://typer.tiangolo.com/) linux/macos/windows
- **[urfave/cli](https://github.com/urfave/cli)** — A simple, fast and fun package for building command-line apps in Go. [`MIT`](https://github.com/urfave/cli) ⭐ 24.3k linux/macos/windows
- **[yargs](https://github.com/yargs/yargs)** — Yargs helps you build interactive command-line tools in Node.js. [`MIT`](https://github.com/yargs/yargs) ⭐ 11.5k [website](https://yargs.js.org/) linux/macos/windows

## 🔒 Proprietary but Notable

Closed-source CLIs too useful to ignore. Explicitly labeled.

- **[1password-cli](https://1password.com/downloads/command-line/)** — 1Password's official CLI (op): manage vaults and inject secrets into workflows. `proprietary` linux/macos/windows *Requires a 1Password account/subscription; no open-source license.*
- **[cursor-cli](https://cursor.com/)** — Cursor's AI coding agent for the terminal (cursor-agent / agent CLI) — codebase understanding, planning, building, and bug fixing from the command line. `proprietary` macos/linux/windows *Requires a Cursor account/subscription; closed-source binary.*
- **[ngrok](https://ngrok.com/)** — Secure tunnels that expose localhost to the internet in one command. `proprietary` linux/macos/windows *Free tier available; agent is proprietary per ToS.*

## 🎉 Fun and Misc

Because the terminal is also a toy.

- **[asciiquarium](https://github.com/cmatsuoka/asciiquarium)** — An aquarium/sea animation rendered in ASCII art in your terminal. [`GPL-2.0-or-later`](https://github.com/cmatsuoka/asciiquarium) ⭐ 1.3k linux/macos
- **[cmatrix](https://github.com/abishekvashok/cmatrix)** — The Matrix digital rain, screensaver-style, in your terminal. [`GPL-3.0-or-later`](https://github.com/abishekvashok/cmatrix) ⭐ 5.3k linux/macos
- **[cowsay](https://github.com/tnalpgge/rank-amateur-cowsay)** — A talking ASCII cow (and other animals) for your terminal messages. [`GPL-3.0`](https://github.com/tnalpgge/rank-amateur-cowsay) ⭐ 418 linux/macos *License taken from the maintained tnalpgge/rank-amateur-cowsay fork (GPLv3 text, no or-later clause). Note: that fork is archived; the program itself is stable/complete and still shipped by all major distros.*
- **[fastfetch](https://github.com/fastfetch-cli/fastfetch)** — A maintained, fast system-information tool — the neofetch successor. [`MIT`](https://github.com/fastfetch-cli/fastfetch) ⭐ 24.8k linux/macos/windows
- **[figlet](https://github.com/cmatsuoka/figlet)** — Creates large ASCII-art text banners from ordinary words. [`BSD-3-Clause`](https://github.com/cmatsuoka/figlet) ⭐ 1.7k linux/macos
- **[lolcat](https://github.com/busyloop/lolcat)** — Rainbows and unicorns: concatenate files with rainbow coloring. [`BSD-3-Clause`](https://github.com/busyloop/lolcat) ⭐ 6.6k linux/macos

## Notable exclusions

Popular terminal tools deliberately left out, and why:

# Excluded candidates — awesome-cli research (2026-09-30)

Tools that were considered and deliberately left out of `entries.json`, with reasons.
Nothing here is a guess: each row cites the observed evidence.

## Archived / dead upstream

| Tool | Reason |
|---|---|
| neofetch | Upstream repo `dylanaraps/neofetch` archived in 2024; project is dead. (fastfetch is the maintained successor and is included.) |
| exa | Upstream `ogham/exa` archived; unmaintained. Superseded by eza (included, EUPL-1.2). |
| fasd | Upstream archived; unmaintained. (zoxide is the maintained successor and is included.) |
| hub | Deprecated by GitHub itself in favor of `gh` (included). |
| rye | Upstream archived; Astral wound it down in favor of `uv`. |
| googler | Archived by jarun (author archived all his CLI search tools). |
| ddgr | Archived by jarun, same as googler. |
| rtv | Upstream archived; Reddit API changes killed its use case. |
| http-prompt | Upstream archived; unmaintained. (httpie/xh/hurl cover the interactive-HTTP niche.) |
| kingpin | `alecthomas/kingpin` archived; unmaintained CLI-framework. (clap/cobra/urfave-cli cover the niche.) |
| thefuck | Effectively unmaintained upstream; no meaningful activity. |

## Discontinued / deprecated in favor of a successor

| Tool | Reason |
|---|---|
| Fig | Discontinued by Amazon (Aug 2024); service shut down. |
| structopt | Deprecated by its author in favor of clap (included). |
| profclems/glab (GitHub mirror) | Archived after GitLab officially adopted the project; canonical repo is now `gitlab.com/gitlab-org/cli` (that URL is what `entries.json` uses). |

## Out of scope for a CLI-tools list

| Tool | Reason |
|---|---|
| oh-my-zsh | A zsh plugin/configuration framework, not a command-line tool. |
| sl | No license statement anywhere in the upstream `mtoyoda/sl` repo (only a copyright notice) — license could not be verified after reasonable effort, so it was cut rather than shipped as an unverified entry. |

## Cut for the ~110-entry cap (overlap)

| Tool | Reason |
|---|---|
| xh | A Rust reimplementation of HTTPie; heavy overlap with httpie (included). Cut to hold the 110-entry ceiling. |

## Reclassified, not excluded

- **doppler** and **snyk** were initially filed as proprietary, but verification showed both CLIs are Apache-2.0 open source (`DopplerHQ/cli`, `snyk/cli`). They are included under `security` with notes that their cloud platforms are commercial.
- **amazon-q-developer-cli** was initially filed as proprietary, but `aws/amazon-q-developer-cli` is Apache-2.0. Included under `ai-coding-clis`.

## Related

- [awesome-oss-cli](https://github.com/dakotac1994/awesome-oss-cli) — the companion list covering strictly open-source CLI tools.
- [awesome-oss-macos](https://github.com/Awesome-llms-labs/awesome-oss-macos) — open-source macOS applications, including terminal emulators.

## Documentation

- [Choosing a CLI tool](docs/choosing-a-cli-tool.md)
- [Glossary](docs/glossary.md)
- [Status changes](docs/status-changes.md)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New entries need a verified license label (or an explicit `proprietary` / unverified flag with a reason), a public repository or official product page, and must be installable on at least one major platform.

## License

This list is MIT licensed. The tools listed keep their own licenses.
