import random

#Get user to enter to input level, if in negative range it loops back into asking again
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level #if negative number return to input
        except ValueError:
            return get_level() #loop back into get_level()

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess >= 0:
                return guess
        except ValueError:
            return get_guess()

def main():
    level = get_level()
    target = random.randint(1, level)

    while True:
        guess = get_guess()

        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
