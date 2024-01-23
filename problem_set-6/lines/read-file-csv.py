import csv

#script to read a file and print out as a list
family = []
with open("names.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
                family.append({"name": row["name"], "home": row["home"]})


for fam in sorted(family, key=lambda fam: fam["home"], reverse=True): #use a key to set on specific item in a dictionary in sorted function, 'lambda is an anonymos function'
        print(f"{fam['name']} lives in -- {fam['home']}")
