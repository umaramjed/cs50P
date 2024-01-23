#dictionary for each key:value pair
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

#set current price to 0, need a variable to keep adding to total amount
total_amount = 0

# loop forver
while True:
    try:
        item = input("Item: ").title() #titlecased, first letter will be capital the rest lower case
        if item in menu:
            total_amount += menu[item]
            print("Total: ${:.2f}".format(total_amount))

    except EOFError:

       print()
       break

