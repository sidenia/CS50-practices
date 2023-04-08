students = []

with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
       
        # creating a dict
        student = {}
        student["name"] = name
        student["house"] = house

        #appeding the dicts in a list
        students.append(student)

for student in students:
    print(f"{student['name']} lives at {student['house']}")