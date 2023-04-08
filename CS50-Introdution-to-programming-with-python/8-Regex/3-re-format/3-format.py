import re

name = input("Enter your name: ").strip()
matches = re.search(r"^(.+), ?(.+)$", name)

if matches:
    first, last = matches.groups()
    name = f'{first} {last}'

print(f"Hello, {name}")


# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"

    # name = name.split(",")[1].strip() + " " + name.split(",")[0].strip()
