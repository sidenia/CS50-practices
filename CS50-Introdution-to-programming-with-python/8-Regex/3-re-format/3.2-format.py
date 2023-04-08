import re

name = input("Enter your name: ").strip()
                    #   G1     G2
matches = re.search(r"^(.+), ?(.+)?$", name)

if matches:
    # name = f"{matches[1]} {matches[2]}"
    name = f"{matches.group(1)} {matches.group(2)}"

print(f"Hello, {name}")
