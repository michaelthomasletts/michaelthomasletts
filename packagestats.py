#!/usr/bin/env python3

import re
from os import getenv
from pathlib import Path

from pepy_chart import PepyStats


def fetch(package: str = "boto3-refresh-session") -> int:
    pepy = PepyStats(
        package=package,
        api_key=getenv("PEPY_API_KEY"),
        create_image=False,
    )
    return pepy.total_downloads


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
