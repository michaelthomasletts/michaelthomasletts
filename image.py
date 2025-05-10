from laudanum import Logo


text = """mike
letts"""

if __name__ == "__main__":
    logo = Logo(text=text, font="twisted", filename="img.png")
    logo.create()
