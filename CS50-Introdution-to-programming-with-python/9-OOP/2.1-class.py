# create our own objects

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self._name = name
        self._house = house

    
    def __str__(self):
        return f"{self.name} is in {self.house}"


    #getter
    @property
    def house(self):
        return self._house


    @property
    def name(self):
        return self._name


    #setter
    @house.setter
    def house(self, house):
        if not house in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


    @name.setter
    def name(self, name):
        self._name = name


    @classmethod
    def get(cls):
        name = input("name: ")
        house = input("house: ")
        return cls(name, house)



def main():
    student = Student.get()
    print(student)

if "__name__" == "__main__":
    main()
