#loops with while

def main():
    i = int(input("How many meow's would you like? "))
    count(i)

def count(i):
    while i != 0: #always true if not 0
        print("meow!")
        i = i - 1 #counter making sure it reduces by 1 to make it stop

if __name__ == "__main__":
    main()
