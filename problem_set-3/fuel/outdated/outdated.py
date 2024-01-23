#programme to print out date in the ISO standard from a range of date inputs.

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
] #this is a list of months


while True:
    date = input("Date: ")
    try:
        if "/" in date:
            mm, dd, yyyy = date.split("/") # extract / from input
        elif "," in date:
            mmdd, yyyy = date.split(", ") # extract , from date input
            mm, dd = mmdd.split(" ") # extract space from input
            mm = (months.index(mm)) + 1
        if int(mm) > 12 or int(dd) > 31: #expect some input error and be ready to handle it.
            raise ValueError
    except (AttributeError, ValueError, NameError, KeyError):
        pass
    else: # if all is good, go ahead and print out the ISO date format of YYYY-MM-DD
        print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
        break
