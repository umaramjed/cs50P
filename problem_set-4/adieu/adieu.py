import inflect # generate plurals, singular nouns, ordinals, indefinite articles; convert numbers to words.

a = inflect.engine() #call on inflect function called engine

n = [] #create a list

#ask user for a name, one per line (loop) until user ctrl+d, need atleast 1 name
while True:
    try:
        name = input("Name: ")
    except EOFError: #handling errors
        print()
        break
#print out Adieu to input names
    else:
        n.append(name) #add user input names to a list in n variable
#seperate two names with one and
#if 3 names should be two , one and
#n names with n - 1 ("Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl)
print(f"Adieu, adieu, to {a.join(n)}")

