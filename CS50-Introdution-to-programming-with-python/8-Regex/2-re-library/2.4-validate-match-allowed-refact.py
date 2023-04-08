import re

# re.search(pattern, string, flags=0)
email = input("Enter your email: ").strip()

if re.search(r"^\w+@\w+\.(com|org|edu|gov|net)$", email, re.IGNORECASE):  
    print('valid')
else:
    print('invalid')


"""
^\w+@\w+\.(com|org|edu|gov|net)$

first ^ means: match the string
\w: just alphanumberic and _
@ means: match @
\w: just alphanumberic and _ 
\.(com|org|edu|gov|net) means: match . and  any of the list
$ means: match the end of the string

if I want to allow white space so I can use one of the two exemples:
    1) ^(\w|\s)+@\w+\.(com|org|edu|gov|net)$
    2) ^[a-zA-Z0-9_ ]+@\w+\.(com|org|edu|gov|net)$
"""  

"""
if I turn the example like this: ".{1}.*@.*" the curly braces is used to specify the specific number of caracters you are looking fore.. but is too verbose, the previous one is the best solutions.
"""