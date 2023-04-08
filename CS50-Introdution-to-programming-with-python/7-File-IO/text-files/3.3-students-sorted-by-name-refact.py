students = []

with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


def get_name(student):
    return student['name']


def get_house(student):
    return student['house']
    

#sorting students NAME before printing
for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} lives at {student['house']}")

print('\n')

#sorting students HOUSES before printing
for student in sorted(students, key=get_house, reverse=True):
    print(f"{student['name']} lives at {student['house']}")