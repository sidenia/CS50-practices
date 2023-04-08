import re

# re.search(pattern, string, flags=0)
email = input("Enter your email: ").strip()

if re.search("@", email):
    print('valid email')
else:
    print('invalid email')

