# Contributing to Awesome CLI

Thanks for helping keep this list honest and current.

## What belongs here

- Real command-line / terminal tools: shells, TUIs, CLIs, and frameworks for building them.
- **Open-source and proprietary tools are both welcome** — but the license label must be accurate. A proprietary tool must be labeled `proprietary`, never implied to be open source.
- Must be installable and runnable on at least one major platform (Linux, macOS, Windows).
- Verifiable via a public repository or an official product page.

## What does not belong

- Vaporware, unreleased announcements, or "coming soon" pages.
- Web apps or GUI apps with a token CLI flag — the command line must be the point.
- Forks that add nothing over the upstream project.

## How to add an entry

1. Add an object to `data/cli.json` with all required fields (see `scripts/validate_data.py` for the schema).
2. Set `verified: true` only if you personally confirmed the license on an official source (license file, package metadata, or official pricing/docs page). Otherwise set `verified: false` and explain in `unverified_reason`.
3. Regenerate the README: `python3 scripts/build_site.py` (reads `data/cli.json`, rewrites `README.md`).
4. Run the validator: `python3 scripts/validate_data.py` — it must pass.
5. Open a PR. CI runs the same validator plus a link check.

## Honesty rules

- Never invent a license, star count, or platform claim. If you can't verify it, flag it.
- If a project's license changed (e.g., relicensed to a proprietary or source-available license), update the entry and note it in `docs/status-changes.md`.
- Archived or discontinued projects are removed or moved to `docs/status-changes.md`, not left to rot in the list.
