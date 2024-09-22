import random
item_list = ["Rock", "Paper","Scissor"]

user_choice = input("enter your move = rock,paper,scissor: ")
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice}, computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("it's a tie")
elif user_choice == "Rock":
    if comp_choice == "paper":
        print("paper covers rock = computer wins")
    else:
        print("user wins")

elif user_choice == "paper":
    if comp_choice == "scissor":
        print("computer wins")
    else:
        print("user wins")

elif user_choice == "scissor":
    if comp_choice == "rock":
        print("computer wins")
    else:
        print("user wins")
        


