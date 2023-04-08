# CREATING AND WRITING | REWRITING IN A FILE

name = input("Whats your name?")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()