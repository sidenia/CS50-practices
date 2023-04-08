#fragile program 

url = input("Enter your twitter url: ").strip()
username = url.replace("https://twitter.com/", "")
print(username)