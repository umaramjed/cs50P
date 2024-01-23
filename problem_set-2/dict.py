#working with dictionary
#
#
def main():
    family = [
        {"name":"John", "role": "Father"},
        {"name":"Marry", "role": "Mother"},
        {"name": "Zak", "role": "Son"}
    ] #this is a dictionary, a collection of values (keys with values)
    check(family)#you need to call all functions under main() for it to execute

def check(family):
    print("\nThis is the list of family members....\n")
    for roles in family:
        print(roles["name"], roles["role"], sep="- ") #print list of names and roles from above dictionary

if __name__ == "__main__": #required
    main()
