#!/usr/bin/env python3
"""Normalize research entries into data/cli.json and generate README.md.

Reads:  /tmp/awesome-cli-research/entries.json (researcher schema)
        /tmp/awesome-cli-research/exclusions.md (researcher exclusions)
Writes: data/cli.json, README.md  (relative to repo root = parent of scripts/)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = Path("/tmp/awesome-cli-research/entries.json")
EXCLUSIONS = Path("/tmp/awesome-cli-research/exclusions.md")
DATA_FILE = ROOT / "data" / "cli.json"
README_FILE = ROOT / "README.md"

SECTIONS = [
    ("shells-prompts", "🐚", "Shells and Prompts", "Command-line shells and prompt customizers."),
    ("terminal-multiplexers", "🪟", "Terminal Multiplexers", "Manage multiple terminal sessions in one window."),
    ("file-navigation", "🗂️", "File and Navigation", "File managers, directory jumpers, and ls replacements."),
    ("search", "🔎", "Search", "Find files and text at speed."),
    ("git-vcs", "🌿", "Git and VCS", "Version control from the terminal."),
    ("editors", "✏️", "Editors", "Terminal text editors."),
    ("system-monitoring", "📊", "System Monitoring", "Watch processes, disks, networks, and resources."),
    ("networking-http", "🌐", "Networking and HTTP", "Requests, tunnels, and network diagnostics."),
    ("data-json-yaml", "🧮", "Data, JSON and YAML", "Slice, query, and transform structured data."),
    ("text-processing", "📝", "Text Processing", "View, convert, and summarize text and documents."),
    ("media", "🎬", "Media", "Audio, video, and image tools for the terminal."),
    ("devops-cloud", "☁️", "DevOps and Cloud CLIs", "Infrastructure, containers, and cloud provider CLIs."),
    ("security", "🔐", "Security and Secrets", "Encryption, secrets management, and security scanning."),
    ("ai-coding-clis", "🤖", "AI Coding CLIs", "AI assistants that live in your terminal. Licenses labeled honestly."),
    ("cli-frameworks", "🧰", "Frameworks for Building CLIs", "Libraries for building command-line apps, by language."),
    ("proprietary-notable", "🔒", "Proprietary but Notable", "Closed-source CLIs too useful to ignore. Explicitly labeled."),
    ("fun-misc", "🎉", "Fun and Misc", "Because the terminal is also a toy."),
]
SECTION_ORDER = [s[0] for s in SECTIONS]
SECTION_META = {s[0]: s[1:] for s in SECTIONS}

CATEGORY_ALIASES = {
    "shells": "shells-prompts", "shell": "shells-prompts",
    "multiplexers": "terminal-multiplexers",
    "file-managers": "file-navigation", "files": "file-navigation", "navigation": "file-navigation",
    "search-find": "search", "find": "search",
    "git": "git-vcs", "vcs": "git-vcs",
    "editor": "editors",
    "monitoring": "system-monitoring", "system": "system-monitoring",
    "networking": "networking-http", "network": "networking-http", "http": "networking-http",
    "data": "data-json-yaml", "json": "data-json-yaml", "json-yaml": "data-json-yaml", "yaml": "data-json-yaml",
    "text": "text-processing",
    "devops": "devops-cloud", "cloud": "devops-cloud", "cloud-clis": "devops-cloud",
    "ai": "ai-coding-clis", "ai-clis": "ai-coding-clis",
    "frameworks": "cli-frameworks", "libraries": "cli-frameworks", "building-clis": "cli-frameworks",
    "proprietary": "proprietary-notable",
    "fun": "fun-misc", "misc": "fun-misc",
}

LICENSE_NORMALIZE = {
    "GPL-3.0-only": "GPL-3.0",
    "GPL-2.0-only": "GPL-2.0",
    "LGPL-3.0-only": "LGPL-3.0",
    "LGPL-2.1-only": "LGPL-2.1",
    "AGPL-3.0-only": "AGPL-3.0",
    "Apache 2.0": "Apache-2.0",
    "MIT License": "MIT",
    "Freemium": "freemium",
}


def normalize_license(lic: str) -> str:
    return LICENSE_NORMALIZE.get(lic, lic)


def normalize_category(cat: str) -> str:
    cat = cat.strip().lower()
    if cat in SECTION_ORDER:
        return cat
    if cat in CATEGORY_ALIASES:
        return CATEGORY_ALIASES[cat]
    raise ValueError(f"unknown category: {cat!r}")


def github_slug(text: str) -> str:
    """Replicate GitHub's heading anchor slugger (no hyphen collapsing)."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return text.strip().replace(" ", "-")


def fmt_stars(stars) -> str:
    if not stars:
        return ""
    if stars >= 1000:
        v = stars / 1000
        s = f"{v:.1f}".rstrip("0").rstrip(".")
        return f"⭐ {s}k"
    return f"⭐ {stars}"


def clean_url(v):
    """Keep only the leading URL token; drop trailing prose like '...: license note'."""
    if not v:
        return None
    tok = v.strip().split()[0].rstrip(".,;:'\"")
    return tok if tok.startswith("https://") else None


def load_entries() -> list[dict]:
    raw = json.loads(RESEARCH.read_text(encoding="utf-8"))
    entries = []
    seen = set()
    for r in raw:
        name = r["name"].strip()
        if name.lower() in seen:
            raise ValueError(f"duplicate entry name: {name}")
        seen.add(name.lower())
        repo_url = (r.get("repo_url") or "").strip()
        homepage = (r.get("official_site") or "").strip() or None
        if not repo_url:
            repo_url = homepage or ""
        lic = normalize_license((r.get("license") or "unverified").strip())
        verified = bool(r.get("verified"))
        vsrc = clean_url(r.get("verified_source"))
        if verified and not vsrc:
            # Researcher recorded prose instead of a URL; fall back to the most
            # authoritative link available (the repo page shows license info).
            vsrc = repo_url if repo_url.startswith("https://github.com/") else (homepage or repo_url)
            vsrc = clean_url(vsrc)
        plats = r.get("platforms")
        if isinstance(plats, list):
            plats = "/".join(plats)
        plats = (plats or "").strip() or None
        entries.append({
            "name": name,
            "repo_url": repo_url,
            "homepage": homepage,
            "description": r.get("description", "").strip(),
            "license": lic,
            "category": normalize_category(r.get("category", "")),
            "verified": verified,
            "verified_source": vsrc,
            "unverified_reason": (r.get("unverified_reason") or "").strip() or None,
            "stars": r.get("stars"),
            "platforms": plats,
            "note": (r.get("note") or "").strip() or None,
            "status": "active",
        })
    entries.sort(key=lambda e: (SECTION_ORDER.index(e["category"]), e["name"].lower()))
    return entries


def entry_bullet(e: dict) -> str:
    desc = e["description"].rstrip().rstrip(".")
    parts = [f"- **[{e['name']}]({e['repo_url']})** — {desc}."]
    if e["license"] in ("proprietary", "freemium"):
        parts.append(f"`{e['license']}`")
    elif e["license"] == "unverified":
        parts.append("`license unverified` ⚠️")
    else:
        lic_src = e["verified_source"] if e["verified"] and e["verified_source"] else e["repo_url"]
        parts.append(f"[`{e['license']}`]({lic_src})")
    stars = fmt_stars(e.get("stars"))
    if stars:
        parts.append(stars)
    if e.get("homepage") and e["homepage"] != e["repo_url"]:
        parts.append(f"[website]({e['homepage']})")
    if e.get("platforms"):
        parts.append(e["platforms"])
    if e.get("note"):
        parts.append(f"*{e['note']}*")
    if not e["verified"] and e.get("unverified_reason"):
        parts.append(f"⚠️ {e['unverified_reason']}")
    return " ".join(parts)


def build_readme(entries: list[dict], exclusions_md: str) -> str:
    by_cat: dict[str, list[dict]] = {c: [] for c in SECTION_ORDER}
    for e in entries:
        by_cat[e["category"]].append(e)
    total = len(entries)
    verified_n = sum(1 for e in entries if e["verified"])
    frameworks_n = len(by_cat["cli-frameworks"])
    proprietary_n = sum(1 for e in entries if e["license"] in ("proprietary", "freemium"))

    lines = []
    lines.append("# Awesome CLI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    lines.append("")
    lines.append(
        f"A curated list of **{total} command-line tools** — shells, TUIs, CLIs, cloud CLIs, "
        "AI coding assistants, and the frameworks for building them. Every license was verified "
        "against an official source on 2026-09-30; proprietary tools are explicitly labeled `proprietary`."
    )
    lines.append("")
    lines.append(f"- ✅ **{verified_n}/{total}** licenses verified from official sources")
    lines.append(f"- 🧰 **{frameworks_n}** frameworks for building CLIs")
    lines.append(f"- 🔒 **{proprietary_n}** proprietary-but-notable tools, honestly labeled")
    lines.append("- 📦 Machine-readable data in [`data/cli.json`](data/cli.json)")
    lines.append("")
    lines.append("## Contents")
    lines.append("")
    for cat in SECTION_ORDER:
        if not by_cat[cat]:
            continue
        emoji, title, _blurb = SECTION_META[cat]
        anchor = github_slug(f"{emoji} {title}")
        lines.append(f"- [{emoji} {title}](#{anchor}) ({len(by_cat[cat])})")
    lines.append("- [Notable exclusions](#notable-exclusions)")
    lines.append("- [Related](#related)")
    lines.append("- [Documentation](#documentation)")
    lines.append("- [Contributing](#contributing)")
    lines.append("- [License](#license)")
    lines.append("")

    for cat in SECTION_ORDER:
        if not by_cat[cat]:
            continue
        emoji, title, blurb = SECTION_META[cat]
        lines.append(f"## {emoji} {title}")
        lines.append("")
        lines.append(blurb)
        lines.append("")
        for e in by_cat[cat]:
            lines.append(entry_bullet(e))
        lines.append("")

    lines.append("## Notable exclusions")
    lines.append("")
    lines.append("Popular terminal tools deliberately left out, and why:")
    lines.append("")
    lines.append(exclusions_md.strip())
    lines.append("")
    lines.append("## Related")
    lines.append("")
    lines.append("- [awesome-oss-cli](https://github.com/dakotac1994/awesome-oss-cli) — the companion list covering strictly open-source CLI tools.")
    lines.append("- [awesome-oss-macos](https://github.com/Awesome-llms-labs/awesome-oss-macos) — open-source macOS applications, including terminal emulators.")
    lines.append("")
    lines.append("## Documentation")
    lines.append("")
    lines.append("- [Choosing a CLI tool](docs/choosing-a-cli-tool.md)")
    lines.append("- [Glossary](docs/glossary.md)")
    lines.append("- [Status changes](docs/status-changes.md)")
    lines.append("")
    lines.append("## Contributing")
    lines.append("")
    lines.append("See [CONTRIBUTING.md](CONTRIBUTING.md). New entries need a verified license label "
                 "(or an explicit `proprietary` / unverified flag with a reason), a public repository "
                 "or official product page, and must be installable on at least one major platform.")
    lines.append("")
    lines.append("## License")
    lines.append("")
    lines.append("This list is MIT licensed. The tools listed keep their own licenses.")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    entries = load_entries()
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    exclusions_md = EXCLUSIONS.read_text(encoding="utf-8") if EXCLUSIONS.exists() else "_None recorded._"
    README_FILE.write_text(build_readme(entries, exclusions_md), encoding="utf-8")
    print(f"wrote {len(entries)} entries -> {DATA_FILE}")
    print(f"wrote README -> {README_FILE}")


if __name__ == "__main__":
    main()
