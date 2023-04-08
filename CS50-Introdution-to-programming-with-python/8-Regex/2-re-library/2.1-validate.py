import re

# re.search(pattern, string, flags=0)
email = input("Enter your email: ").strip()

if re.search(r"^.+@.+\.com$", email): #still accept many @ :(, lets change
    print('valid')
else:
    print('invalid')

"""
# check many caracters before and after @. it could be also "..*@..*"  
# ^start the string   $ end the string
#use r(rawstring) and use \ scape character, so the regex understands its a . not any character
#unfortunately if you type any sentence before @ including spaces it will take a valid...bc this treatment
"""