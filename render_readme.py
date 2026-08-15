#!/usr/bin/env python3
"""Render README.md from README_template.md using PyPI download stats.

Download counts are published as shields.io endpoint JSON by
michaelthomasletts/pepy-stats, e.g.

    {"schemaVersion": 1, "label": "Downloads", "message": "286.2K"}

Each entry in PACKAGES maps a Jinja2 variable in README_template.md to the
package whose ``message`` value fills it.
"""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

from jinja2 import Environment, StrictUndefined

STATS_URL = (
    "https://raw.githubusercontent.com/michaelthomasletts/pepy-stats/"
    "refs/heads/main/stats/{package}.json"
)

PACKAGES = {
    "bcc_downloads": "boto3-client-cache",
    "brs_downloads": "boto3-refresh-session",
    "elhaz_downloads": "elhaz",
}

ROOT = Path(__file__).parent
TEMPLATE = ROOT / "README_template.md"
README = ROOT / "README.md"


def downloads(package: str) -> str:
    """Return the formatted download count for ``package``."""
    url = STATS_URL.format(package=package)
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            payload = json.load(response)
    except (urllib.error.URLError, json.JSONDecodeError) as e:
        raise RuntimeError(f"failed fetching stats for {package}: {e}") from e

    message = payload.get("message")
    if not message:
        raise RuntimeError(f"no download count in stats for {package}")
    return message


def main() -> int:
    context = {
        variable: downloads(package) for variable, package in PACKAGES.items()
    }

    env = Environment(undefined=StrictUndefined, keep_trailing_newline=True)
    rendered = env.from_string(TEMPLATE.read_text()).render(**context)

    if README.exists() and README.read_text() == rendered:
        print("README.md already up to date")
        return 0

    README.write_text(rendered)
    print("README.md updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
