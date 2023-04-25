import random

class Hat:
    # We dont a constructor, because we will not create multiple instances of this class -> singleton
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):  # cls is the class itself
        house = random.choice(cls.houses)
        print(f"{name} is in, {house}")


def main():
    # hat = Hat() # I dont need it anymore, because we will not instanciate
    Hat.sort("Harry")

if __name__ == "__main__":
    main()