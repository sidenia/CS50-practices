import csv

students = []

with open("names.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        student = {"name": row[0], "house": row[1]}
        students.append(student)

#sorting students NAME before printing, using LAMBDA functions
for student in sorted(students, key=lambda student: student["name"], reverse=False):
    print(f"{student['name']} lives at {student['house']}")




# you could also use this sintax:
with open("names.csv") as file:
    reader = csv.reader(file)
    for name, house in reader:
        student = {"name": name, "house": house}
        students.append(student)