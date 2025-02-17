from art import *
from jinja2 import Environment, FileSystemLoader
from random import randint

# cataloguing my favorite fonts
favorite_fonts = [
    "3d_diagonal",
    "alpha",
    "avatar",
    "braced",
    "bulbhead"
    "cricket",
    "fire_font-s",
    "funfaces",
    "fuzzy",
    "ghost",
    "ghoulish",
    "graffiti",
    "larry3d",
    "merlin1",
    "twisted",
    "wetletter",

]
favorite = randint(a=0, b=len(favorite_fonts) - 1)
font = favorite_fonts[favorite]

# generating ascii logo with a lil bit of chaos
text = """mike
letts"""
art = text2art(text, font=font)

# initializing jinja env
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("template.md")

# rendering template with the ascii logo
rendered_markdown = template.render(art=f"```\n{art}\n```")

# save to readme
if __name__ == "__main__":
    with open("README.md", "w") as f:
        f.write(rendered_markdown)