import csv

name = input("Enter your name: ")
house = input("Enter your city: ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, house])