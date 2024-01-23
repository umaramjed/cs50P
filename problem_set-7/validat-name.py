import re

name = input("What's your name? ")
name_pattern = r"^\s*([\w'-]+)\s*,\s*([\w'-]+)\s*$"

if matches := re.search(name_pattern, name):
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
    print (f"hello, {name}")
else:
    print("No match")


