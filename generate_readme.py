from art import text2art, font_list
from jinja2 import Environment, FileSystemLoader
import random

# Define sample text for preview
sample_text = "Sample"

# Favorite fonts list
favorite_fonts = [
    "3d_diagonal",
    "alpha",
    "avatar",
    "braced",
    "bulbhead",  # <-- FIXED: Added missing comma
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

# Function to generate ASCII preview for each font
def generate_font_previews():
    previews = {}
    for f in favorite_fonts:  # <-- FIXED: Avoid overwriting 'font'
        try:
            previews[f] = text2art(sample_text, font=f)
        except Exception as e:
            previews[f] = f"Error generating preview: {e}"
    return previews

# Get font previews
font_previews = generate_font_previews()

# Ask user for font selection
print("Do you want to:")
print("1. Choose a font from the list")
print("2. Use a random font")
choice = input("Enter 1 or 2: ").strip()

font = ""

if choice == "1":
    print("\nAvailable fonts:")
    for i, f in enumerate(favorite_fonts):  
        print(f"{i + 1}. {f}")

    try:
        font_choice = int(input("Enter the number of the font you want: ").strip()) - 1
        if 0 <= font_choice < len(favorite_fonts):
            font = favorite_fonts[font_choice]
        else:
            print("Invalid choice, using a random font.")
            font = random.choice(favorite_fonts)
    except ValueError:
        print("Invalid input, using a random font.")
        font = random.choice(favorite_fonts)
else:
    font = random.choice(favorite_fonts)

print(f"Font ({font_choice+1}) '{font}' has been used. Check README.md for previews.")

# Generate ASCII art
text = """mike
letts"""
art = text2art(text, font=font)

# Initialize Jinja environment
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("template.md")

# Render template with ASCII logo
rendered_markdown = template.render(art=f"```\n{art}\n```")

# Append font previews to README

count = 1
rendered_markdown += "\n\n## Font Previews\n"
for f, preview in font_previews.items():
    rendered_markdown += f"### {count}) {f}\n```\n{preview}\n```\n"
    count += 1

# Save to README
if __name__ == "__main__":
    with open("README.md", "w") as f:
        f.write(rendered_markdown)


