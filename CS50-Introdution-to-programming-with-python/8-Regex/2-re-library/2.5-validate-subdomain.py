import re

# re.search(pattern, string, flags=0)
email = input("Enter your email: ").strip()

if re.search(r"^[a-zA-Z0-9_\.-]+@(\w+\.)?\w+\.(com|org|edu|gov|net)$", email, re.IGNORECASE):  
    print('valid')
else:
    print('invalid')


#(\w+\.)? this part means that a subdomain is optional. THe parenteses is necessary to the expression
#(\w+\.)*? this allows more than one subdomain
# to allow just . we could use (\w|\.) or [a-zA-Z0-9_\.-] to allow . - and _