def main():
    z = input("Fraction: ")#prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer,
    p = convert(z)
    print(gauge(p))

def convert(fraction):
            x, y = fraction.split("/") #splitting input and extracting the two integers
            x = int(x) #defining int to x
            y = int(y) # defining int to y
            if (x)/(y) > 1:
                  raise ValueError
            elif (y) == 0:
                  raise ZeroDivisionError
            return int(int(x)/int(y) * 100)

def gauge(percentage):
            try:
                if 0 <= percentage <= 1:
                    return "E"
                elif 99 <= percentage <= 100:
                    return "F"
                elif 1 < percentage < 99:
                    return f"{int(percentage)}%"
                else:
                    raise TypeError
            except TypeError:
                pass

if __name__ == "__main__":
    main()
