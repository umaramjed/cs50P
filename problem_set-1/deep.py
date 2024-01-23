# user match to build a common list
question = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")).lower().strip() #user lower for case incensative and strip to ignore any space

match question:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
