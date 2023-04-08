import csv

name = input("Enter your name: ")
house = input("Enter your city: ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house"])
    writer.writerow({"name": name, "house": house})
