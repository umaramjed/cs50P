import csv

name = input("what name would you like to add? ")
home = input(f"Whats the location of {name}? ")

#this will open a file and allow to write to it. "a" = append
with open("names.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home })
