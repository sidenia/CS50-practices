students = []

with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


#sorting students NAME before printing, using LAMBDA functions
for student in sorted(students, key=lambda student: student["name"], reverse=False):
    print(f"{student['name']} lives at {student['house']}")


# lambda é uma função anônima


# ao invés de usar isso:
def get_name(student):
    return student["name"]

#use isso:
#sintax-> param:   return
lambda student: student["name"]