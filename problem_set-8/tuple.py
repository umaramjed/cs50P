def main():
    student = get_student()
    if student[0] == "umar": #this will ensure if umar puts any location it will print out Luton
        student[1] = "Luton"
    print(f"{student[0]} from {student[1]}") #example of tuple, getting a sequence of return value


def get_student():
    name = input("Name: ")
    house = input("House? ")
    return [name, house] #using [ becomes a list] and using (name,house) becomes a tuples


if __name__ == "__main__":
    main()
