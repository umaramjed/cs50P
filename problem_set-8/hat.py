import random


class Hat:

    houses = ["Luton", "Enfield", "Edmonton"]
    name = ["Umar", "Eesa", "Hajera"]

    @classmethod
    def sort(cls):
        print(random.choice(cls.name), "is in", random.choice(cls.houses))


Hat.sort()
