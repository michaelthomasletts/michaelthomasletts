#!/usr/bin/env python3

from pepy_chart.core import PepyStats


if __name__ == "__main__":
    PepyStats(
        package="boto3-refresh-session",
        output_path="downloads.png",
        automatically_open_img=False,
    )
