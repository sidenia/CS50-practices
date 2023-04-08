import csv

students = []

with open("names.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # student = {"name": row["name"], "house": row["house"]}
        # students.append(student)
        students.append(row)

#sorting students NAME before printing, using LAMBDA functions
for student in sorted(students, key=lambda student: student["name"], reverse=False):
    print(f"{student['name']} lives at {student['house']}")




# you could also use this sintax:
with open("names.csv") as file:
    reader = csv.reader(file)
    for name, house in reader:
        student = {"name": name, "house": house}
        students.append(student)