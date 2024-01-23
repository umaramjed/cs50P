# ask user for an input
s = input("Input: ").strip()

#output by removing all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
n = s.replace("a", "").replace("e","").replace("i","").replace("o","").replace("u","").replace("O","")

print(f"Output: {n}")





