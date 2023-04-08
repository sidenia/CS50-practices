email = input("Enter your email: ").strip() #remove spaces before and after

username, domain = email.split("@") #split the email at the @ symbol

if username and domain.endswith(".com"):
    print("valid")
else:
    print("invalid")
