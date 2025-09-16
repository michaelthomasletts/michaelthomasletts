#!/usr/bin/env python3

import re
from pathlib import Path

import requests


def fetch(package: str = "boto3-refresh-session") -> str:
    url = f"https://michaelthomasletts.github.io/pepy-stats/{package}.json"
    resp = requests.get(url, headers={"Accept": "application/json"}, timeout=10)
    resp.raise_for_status()
    return resp.json()["message"]  # e.g., "85.0K"


def update(downloads: str, readme_path: Path = Path("README.md")):
    formatted = f"{downloads} :tada:"

    content = readme_path.read_text(encoding="utf-8")

    pattern = re.compile(
        r"(downloads of)\s*[0-9][0-9,]*(?:\.[0-9]+)?[KMB]?(?:\s*:tada:)?",
        flags=re.IGNORECASE,
    )

    new_content, count = pattern.subn(rf"\1 {formatted}", content)

    if count:
        readme_path.write_text(new_content, encoding="utf-8")
    else:
        raise RuntimeError("Marker 'Total Downloads:' not found in README.md")


if __name__ == "__main__":
    downloads = fetch()
    update(downloads=downloads)
