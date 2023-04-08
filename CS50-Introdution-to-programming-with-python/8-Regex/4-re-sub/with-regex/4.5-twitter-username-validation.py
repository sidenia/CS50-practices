#re.sub for substitutions

url = input("Enter your twitter url: ").strip()
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"username: {matches.group(1)}")


"""
If we dont want that the (www\.) is counted as a group, you must change the syntax to (?:www\.)
"""
# teste with https://twitter.com/username