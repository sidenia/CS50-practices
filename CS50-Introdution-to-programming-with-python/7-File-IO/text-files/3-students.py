with open("names.csv") as file:
    for line in file:
        # row = line.rstrip().split(",")
        # print(f"{row[0]} lives at {row[1]}")
        
        name, house = line.rstrip().split(",")
        print(f"{name} lives at {house}")
