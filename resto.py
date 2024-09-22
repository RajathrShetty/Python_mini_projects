menu = {
    'Pizza' : 40,
    'Pasta' : 50,
    'Icecream' : 20,
    'Noodles' : 40,
    'Burger' : 60,
    'Salad' : 80,
    'Coffee' : 60
}

print("welcome")
print("Pizza : 40rs\nPasta: 50Rs\nIcecream:20rs\nNoodels: 40rs\nBurger: 60rs\nSalad: 80rs\nCoffee: 60rs")

order_total = 0

Item1 = input("Enter the name of the item you want to order: ")
if Item1 in menu:
    order_total += menu[Item1]
    print("would you like to order anything else: ")
else: 
    print(f"Ordered item {Item1} not available!!!")

another_order = input("do you want to order another item? (Yes/No) ")
if another_order == "Yes":
    Item2 = input("enter the name of the second item: ")
    if Item2 in menu:
         order_total += menu[Item2]
         print(f"your total is: {order_total}")
else: 
    print(f"ordered item {Item2} is not available")
    
    print(f"the total amount of items to pay is {order_total}")