import re
#re.sub for substitutions

url = input("Enter your twitter url: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

print(username)