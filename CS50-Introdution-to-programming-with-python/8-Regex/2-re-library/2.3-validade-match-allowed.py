import re

# re.search(pattern, string, flags=0)
email = input("Enter your email: ").strip()

if re.search(r"^[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.com$", email):  
    print('valid')
else:
    print('invalid')


"""
^[a-zA-Z0-9_]+@[^@]+\.com$ 

first ^ means: match the string
[a-zA-Z0-9_]: just allow a-z, A-Z, 0-9 and _ . and -
@ means: match @
[a-zA-Z0-9_]: just allow a-z, A-Z, 0-9 and _ . and -
\.com$ means: match .com at the end of the string
$ means: match the end of the string
"""

"""
if I turn the example like this: ".{1}.*@.*" the curly braces is used to specify the specific number of caracters you are looking fore.. but is too verbose, the previous one is the best solutions.
"""