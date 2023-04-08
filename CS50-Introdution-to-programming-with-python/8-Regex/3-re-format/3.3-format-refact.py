import re

name = input("Enter your name: ").strip()

#AO INVÉS DISSO:
matches = re.search(r"^(.+), ?(.+)?$", name)
if matches:
    name = f"{matches.group(1)} {matches.group(2)}"


# USE WALRUS OPERATOR:
if matchs := re.search(r"^(.+), ?(.+)?$", name):
    name = f"{matches.group(1)} {matches.group(2)}"

print(f"Hello, {name}")
