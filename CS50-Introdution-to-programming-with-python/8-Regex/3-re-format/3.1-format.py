import re

name = input("Enter your name: ").strip()
                    #   G1     G2
matches = re.search(r"^(.+), ?(.+)$", name)

if matches:
    first = matches.group(1)
    last = matches.group(2)
    name = "{}{}".format(first, last)

print(f"Hello, {name}")
