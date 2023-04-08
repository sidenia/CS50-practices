with open("names.txt", "r") as f:
    lines = f.readlines() #readlines returns a list

for line in lines:
    # print("Hello,", line, end="")
    print("Hello,", line.rstrip())
