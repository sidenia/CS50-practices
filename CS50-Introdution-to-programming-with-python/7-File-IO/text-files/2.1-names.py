with open("names.txt", "r") as f:
    for line in f:
        print("Hello,", line.rstrip())