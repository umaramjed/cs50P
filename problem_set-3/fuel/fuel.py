
#TODO  outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank

#TODO  If, though, 1% or less remains, output E

#TODO  if 99% or more remains, output F instead to indicate that the tank is essentially full.


#TODO If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

def main():
    z = get_fraction("Fraction: ") #prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer,
    print(z)

def get_fraction(prompt):
    while True:
        try:
            x, y = input(prompt).split("/") #splitting input and extracting the two integers
            x = int(x) #defining int to x
            y = int(y) # defining int to y
            if x <= y: #
                z = x/y
            else:
                continue
        except (ValueError, ZeroDivisionError):
            pass
        else:
            z *= 100 #convert to % value
            if z >= 99:
                z = "F"
            elif z <= 1:
                z = "E"
            else:
                z = f"{z:.0f}%"
            return z

main()
