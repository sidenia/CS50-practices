#fragile program 

url = input("Enter your twitter url: ").strip()
username = url.removeprfix("https://twitter.com/")
print(f'USERNAME: {username}')