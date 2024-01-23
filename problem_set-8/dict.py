def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}") #example of getting key value pairs in dict


def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


if __name__ == "__main__":
    main()
