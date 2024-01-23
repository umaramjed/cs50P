#c = name - s = name
#c = firstName - s=first_name,
#c = preferredFirstName - s = preferred_first_name

dict = [
        {"camelCase":"name", "snake_case": "name"},
        {"camelCase":"firstName", "snake_case": "first_name"},
        {"camelCase":"preferredFirstName", "snake_case": "preferred_first_name"},
    ] #this is a dictionary, a collection of values (keys with values)

camel = input("camelCase: ") #get user input
print(" ", end="")

for c in camel:
    if c.islower():
        print(c, end="")
    if c.isupper():
        print("_", c.lower(), end="", sep="")

print()
