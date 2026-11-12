
item = input("Enter item you would like to buy: ")
price = float(input(f"Enter price of per {item}: "))
quantity = int(input(f"How many {item} would you lime to buy?: "))   
total = price * quantity

print(f"You have brought {quantity} * {item}")
print(f"You total is ${total}")

import math

pi = 3.14
print(math.ceil(pi))
print(math.floor(pi))