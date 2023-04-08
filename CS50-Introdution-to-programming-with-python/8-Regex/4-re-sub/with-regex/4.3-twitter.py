import re
#re.sub for substitutions

url = input("Enter your twitter url: ").strip()
matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)

if matches:
    print(f"username: {matches.group(2)}")

# teste with https://twitter.com/username