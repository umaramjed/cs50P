#In a file called grocery.py, implement a program that prompts the user for items, one per line,
#until the user inputs control-d (which is a common way of ending one’s input to a program).
#Then output the user’s grocery list in all uppercase, sorted alphabetically by item,
#prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

# make a dictionary to capture list

grocery_list = {} #this is a list

#ask user for input and add to grocery_list


#print out grocery_list in UPPERCASE + Sorted alphabeticaly + prefix with a number of times user added

while True:
    try:
        item = input().upper().strip()#get list from user
        if item not in grocery_list:
            grocery_list[item] = 1 # initialise counter
        else:
            grocery_list[item] = grocery_list[item] + 1 #if duplicate product add 1 to counter
    except EOFError:
        sorted_dict = dict(sorted(list(grocery_list.items()))) #sort list
        for item in sorted_dict:
            print(sorted_dict[item], item, sep=" ") # print out item and grocery list
        break
    except KeyError:
        pass




