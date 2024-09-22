rent = int(input("Enter the hostel rent: "))
food = int(input("enter the amount of food ordered: "))
electricity_spent = int(input("enter the spend for electricity: "))
charge_per_unit = int(input("enter the charge per unit: "))
persons= int(input("enter the number of persons: "))

total_bill = electricity_spent * charge_per_unit

output = (food + rent + total_bill) // persons

print("each person will pay: ", output)