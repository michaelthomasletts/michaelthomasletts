#!/usr/bin/env python3

from laudanum import Logo


text = """mike
letts"""

if __name__ == "__main__":
    Logo(text=text, font="twisted", filename="img.png").create()
