# for loop
def main():
    i = int(input("How many meow's would you like? "))
    count(i)

def count(i):
    for i in range(i): # range is the option the user inputs
        print("meow!")
        #i = i - 1 #counter making sure it reduces by 1 to make it stop if range is not defined

if __name__ == "__main__":
    main()
