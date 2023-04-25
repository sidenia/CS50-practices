# create our own objects

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if not house in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    
    def __str__(self):
        return f"{self.name} is in {self.house}"


    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             print("Stag charm")
    #         case "Otter":
    #             print("Otter charm")
    #         case "Rabbit":
    #             print("Rabbit charm")
    #         case "Snake":
    #             print("Snake charm")
    #         case _:
    #             print("No charm")


def main():
    student = get_student()
    print(student)
    print("Expecto Patronum!")
    # print(student.charm())


def get_student():
    name = input("Enter student name: ")
    house = input("Enter student house: ")
    patronus = input("Enter student patronus: ")
    return Student(name, house, patronus)


if "__name__" == "__main__":
    main()
