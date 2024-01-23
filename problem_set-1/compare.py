


def main():
    user_input()
    calculate()

def user_input():
    x = int(input("whats x? "))
    y = int(input("whats y? "))

def calculate():
    if x != y:
        print("x is not equal to y")
    else:
        print("x is equal to y")

if __name__ == "__main__":
    main()

