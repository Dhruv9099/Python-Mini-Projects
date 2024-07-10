import random

user_wins =0
computer_wins =0

options = ["rock","paper","scissors"]
# options[0]
# options[1]
# options[2]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input =="q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock :0, paper:1, scissors:2.
    computer_pick = options[random_number]
    print("computer Picked", computer_pick + ".")

    if user_input =="rock"and computer_pick=="scissors":
        print("you won !")
        user_wins +=1
    elif user_input =="paper"and computer_pick=="rock":
        print("you won !")
        user_wins +=1
    elif user_input =="scissors"and  computer_pick=="paper":
        print("you won !")
        user_wins +=1
    else:
        print("You Lost!")
        computer_wins+=1


print("You Won ", user_wins," Times.")
print("The Computer Won ", computer_wins," Times.")
print("Good Bye!")
