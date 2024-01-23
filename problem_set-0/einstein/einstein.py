#e = energy
#m=mass
#c=speed '300000000'
#e=mc2

# Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

def main():
    mass = int(input("m: "))
    c = 300000000
    c2 = pow(c, 2)
    e = int(mass)*c2
    print(f"E={e}")

main()

