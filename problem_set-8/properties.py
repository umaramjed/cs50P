class Student:
    def __init__(self, name, house, patronus): #adding instance variables to objects, this is a method
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self): #this is a method
        return f"{self.name} from {self.house} AND {self.charm()}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return ":)"
            case "lion":
                return ":("
            case _:
                return "@"

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    @property #Getter function
    def house(self):
        return self._house
    @house.setter #Setter function
    def house(self, house):
        if house not in ["Luton", "Edmonton", "Enfield"]:
            raise ValueError("Invalid house")
        self._house = house



def main():
    student = get_student()
    '''print(f"{student.name} from {student.house}") #example of getting key value pairs in dict'''
    print(student)
    '''print(student.charm()) #it will return what's in __str__(self)'''


def get_student(): #this is an object of class Student
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    student = Student(name, house, patronus)
    return student


if __name__ == "__main__":
    main()
