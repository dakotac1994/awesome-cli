#!/usr/bin/env python3
"""Validate data/cli.json and its sync with README.md. Used by CI."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "cli.json"
README_FILE = ROOT / "README.md"

REQUIRED_FIELDS = {
    "name",
    "repo_url",
    "homepage",
    "description",
    "license",
    "category",
    "verified",
    "verified_source",
    "unverified_reason",
    "stars",
    "platforms",
    "note",
    "status",
}
VALID_STATUSES = {"active", "maintenance", "archived"}
VALID_CATEGORIES = {
    "shells-prompts",
    "terminal-multiplexers",
    "file-navigation",
    "search",
    "git-vcs",
    "editors",
    "system-monitoring",
    "networking-http",
    "data-json-yaml",
    "text-processing",
    "media",
    "devops-cloud",
    "security",
    "ai-coding-clis",
    "cli-frameworks",
    "proprietary-notable",
    "fun-misc",
}


def github_slug(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return text.strip().replace(" ", "-")


def load_data() -> list[dict]:
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    assert isinstance(data, list) and data, "cli.json must be a non-empty list"
    for i, entry in enumerate(data):
        missing = REQUIRED_FIELDS - entry.keys()
        assert not missing, f"entry {i} ({entry.get('name')}) missing {sorted(missing)}"
        assert entry["category"] in VALID_CATEGORIES, f"entry {i} bad category {entry['category']}"
        assert entry["status"] in VALID_STATUSES, f"entry {i} bad status {entry['status']}"
        assert isinstance(entry["verified"], bool), f"entry {i} verified not bool"
        assert entry["repo_url"].startswith("https://"), f"entry {i} repo_url must be https"
        if entry["homepage"]:
            assert entry["homepage"].startswith("https://"), f"entry {i} homepage must be https"
        if entry["verified"]:
            assert entry["verified_source"] and entry["verified_source"].startswith("https://"), (
                f"entry {i} verified entry needs https verified_source"
            )
            assert entry["license"] != "unverified", (
                f"entry {i} verified entry must name a license"
            )
        else:
            assert entry["unverified_reason"], (
                f"entry {i} unverified entry needs unverified_reason"
            )
        if entry["stars"] is not None:
            assert isinstance(entry["stars"], int) and entry["stars"] >= 0, (
                f"entry {i} stars must be a non-negative int"
            )
    names = [e["name"] for e in data]
    assert len(names) == len(set(n.lower() for n in names)), "duplicate names"
    urls = [e["repo_url"] for e in data]
    assert len(urls) == len(set(urls)), "duplicate repo_urls"
    return data


def validate_readme(data: list[dict]) -> None:
    text = README_FILE.read_text(encoding="utf-8")
    m = re.search(r"A curated list of \*\*(\d+) command-line tools\*\*", text)
    assert m, "README summary line is missing the total entry count"
    assert int(m.group(1)) == len(data), (
        f"README summary count ({m.group(1)}) != data file ({len(data)})"
    )
    # Section counts must match the data.
    from collections import Counter
    counts = Counter(e["category"] for e in data)
    for cat, n in counts.items():
        assert f"({n})" in text, f"README missing count ({n}) for {cat}"
    # Every category present in the data must have a heading anchor in the README.
    headings = set(re.findall(r"^## (.+)$", text, flags=re.M))
    anchors = {github_slug(h) for h in headings}
    toc_anchors = set(re.findall(r"\(#([a-z0-9-]+)\)", text))
    assert toc_anchors <= anchors, f"TOC anchors without headings: {sorted(toc_anchors - anchors)}"


def main() -> None:
    data = load_data()
    validate_readme(data)
    verified = sum(1 for e in data if e["verified"])
    print(f"OK: {len(data)} entries, {verified} verified, README in sync")


if __name__ == "__main__":
    main()
