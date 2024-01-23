#
#
# user match to build a common list
name = input("What's your name buddy? ")

match name:
    case "Umar" | "Hajera" | "Eesa":
        print("Luton")
    case "Ayesha" | "Waqas" | "Taha":
        print("Enfield")
    case _:
        print("Who the hell are you?")
