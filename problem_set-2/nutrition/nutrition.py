# make a dictionary of nutriotanal facts
s = {
        "Apple":"130",
        "Avocado":"50",
        "Banana":"110",
        "Cantaloupe":"50",
        "Grapefruit":"60",
        "Grapes":"60",
        "Honeydew":"50",
        "Kiwifruit":"90",
        "Lemon":"15",
        "Lime":"20",
        "Nectarine":"60",
        "Orange":"80",
        "Peach":"60",
        "Pear":"100",
        "Pineapple":"50",
        "Plums":"70",
        "Strawberries":"50",
        "Sweet Cherries":"100",
        "Tangerine":"50",
        "WWatermelon":"80"
}



# do the calculation and output calorie information
fruit = input("Item: ").title()
if fruit in s:
    print(f"Calories: {s[fruit]}")


