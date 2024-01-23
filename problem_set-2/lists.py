#working with lists
#
#
def main():
    member = ['umar', 'hajera', 'eesa'] #this is a list
    #new_member = (input("Add family member "))
    #member = new_member

    count(member)

def count(member):
    for i in range(len(member)): #get how many members and place it in variable i
        print(i + 1, member[i]) # print members including postion startingg with 1 instead of 0.

if __name__ == "__main__":
    main()


