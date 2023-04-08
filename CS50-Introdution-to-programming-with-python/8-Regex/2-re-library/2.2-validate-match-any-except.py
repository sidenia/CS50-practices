import re

# re.search(pattern, string, flags=0)
email = input("Enter your email: ").strip()

if re.search(r"^[^@]+@[^@]+\.com$", email):  
    print('valid')
else:
    print('invalid')

"""
"^[^@]+@[^@]+\.com$ 
first ^ means: match the string
[^@]+ means: match any character except @
@ means: match @
[^@]+ means: match any character except @
\.com$ means: match .com at the end of the string
$ means: match the end of the string
"""

"""
if I turn the example like this: 
    ".{1}.*@.*" the curly braces is used to specify the specific number of caracters you are looking fore.. but is too verbose, the previous one is the best solutions.
"""