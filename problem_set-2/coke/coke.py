#machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
#
#

#prompt the user of the amount due
def main():
      print(f"Amount Due: 50") #print the amount due
      n = int(input("Insert coin: ")) #prompt user to insert coin
      a = 50 #our cost of a coke bottle, quiet cheap!
      while n != 5 and n != 10 and n !=25: #these coins are not allowed to be inserted into coke machine
             print(f"Amount Due: 50")
             n = int(input("Insert coin: "))
      print(f"Amount Due: {a - n}") # minus 50(a) from the amount is inserted in (n)
      calculation(n,a) # execute the calculation function.

def calculation(n,a):
       while a > n: # while coin inserted is less than 50
              a = a - n # minus 50 from coin inserted
              n = int(input("Insert coin: ")) # keep asking for more coins
              if a - n == 0: # if total amount is now 50 no more change is owed
                     print("Change Owed: 0")
              elif a > n:
                     print(f"Amount Due: {a - n}")
       if n > a:
              print(f"Change Owed: {n - a}")
main()




