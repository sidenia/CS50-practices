email = input("Enter your email: ").strip() #remove spaces before and after

if "@" in email and "." in email:
    print("valid")
else:
    print("invalid")