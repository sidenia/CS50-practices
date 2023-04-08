"""
REGEX nowadays used in most of the browsers to valida most of the e-mails

^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$

"""

import re

def validate_email(email):
    # Regex to validate most of the e-mails
    regex = "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"

    if(re.search(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")

def main():
    email = input("Enter your email: ")
    validate_email(email)

if __name__ == '__main__':
    main()