from pyfiglet import Figlet
from jinja2 import Environment, FileSystemLoader
from random import randint

# cataloguing my favorite fonts
faves = [
    "isometric3",
    "smisome1",
    "ticksslant",
    "drpepper",
]

# generating ascii logo with a lil bit of chaos
figlet = Figlet(font=faves[randint(a=0, b=len(faves) - 1)])
figlet_logo = figlet.renderText("mike letts")

# initializing jinja env
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("template.md")

# rendering template with the ascii logo
rendered_markdown = template.render(figlet_logo=f"```\n{figlet_logo}\n```")

# save to readme
with open("README.md", "w") as f:
    f.write(rendered_markdown)