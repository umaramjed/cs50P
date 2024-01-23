#script to read a file and print out as a list
family = []
with open("names.csv") as file:
    for line in file:
        name, location = line.rstrip().split(",") #comma seperated row
        fam = {"name": name, "location": location}
        family.append(fam)


for fam in sorted(family, key=lambda fam: fam["location"], reverse=True): #use a key to set on specific item in a dictionary in sorted function, 'lambda is an anonymos function'
        print(f"{fam['name']} lives in -- {fam['location']}")

        '''print(f"{name[0]} lives in {location[1]}") #[0] is first ford and [1] is second word'''

'''for row in sorted(names, reverse=True): #reverse=True put's it in reverse order the default is False
    print(f"{name}")'''
