students = []

with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f'{name} lives at {house}')

for student in sorted(students):
    print(student)
