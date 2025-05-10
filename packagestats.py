#!/usr/bin/env python3

from pathlib import Path
import re
import requests


def fetch(package: str = "boto3-refresh-session") -> int:
    url = f"https://pepy.tech/api/v2/projects/{package}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data.get("total_downloads", 0)


def update(downloads: int, readme_path: Path = Path("README.md")):
    formatted = f"{downloads:,} :tada:"
    content = readme_path.read_text(encoding="utf-8")
    pattern = r"(\*\*Total Downloads:\*\*)\s*[0-9,]+(?:\s*:tada:)?"
    new_content, count = re.subn(pattern, rf"\1 {formatted}", content)

    if count:
        readme_path.write_text(new_content, encoding="utf-8")


if __name__ == "__main__":
    downloads = fetch()
    update(downloads=downloads)
