name = input("Whats your name?")

# using with the file will be automatically closed
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
