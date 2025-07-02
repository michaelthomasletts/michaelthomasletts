#!/usr/bin/env python3

from pathlib import Path
import re
import requests


def fetch(package: str = "boto3-refresh-session") -> int:
    with requests.Session() as session:
        url = f"https://pypistats.org/api/packages/{package}/overall"

        # SSL verification deactivated due to issues with pypistats cert
        response = session.get(url=url, verify=False)
        response.raise_for_status()
        stats = 0

        for daily_downloads in response.json()["data"]:
            if daily_downloads["category"] == "with_mirrors":
                stats += daily_downloads["downloads"]

        return stats


def update(downloads: int, readme_path: Path = Path("README.md")):
    formatted = f"{downloads:,} :tada:"
    content = readme_path.read_text(encoding="utf-8")
    pattern = r"(Total Downloads:)\s*[0-9,]+(?:\s*:tada:)?"
    new_content, count = re.subn(pattern, rf"\1 {formatted}", content)

    if count:
        readme_path.write_text(new_content, encoding="utf-8")


if __name__ == "__main__":
    downloads = fetch()
    update(downloads=downloads)
