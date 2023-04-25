import random

class Hat:
    # We dont need it, because we will not create multiple instances of this class -> singleton
    # def __init__(self):
    #     self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        house = random.choice(self.houses)
        print(f"{name} is in, {house}")


def main():
    hat = Hat()
    hat.sort("Harry")

if __name__ == "__main__":
    main()