#!/usr/bin/env python3

from laudanum import Logo

text = """mike
letts"""

if __name__ == "__main__":
    Logo(text=text, font="crawford", filename="img.png").create()
