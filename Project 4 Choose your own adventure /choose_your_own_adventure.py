name =input("Type your Name: ")

print("Welcome", name," to this adventure! ")

answer =input("You lost the map in jungle now you have to choose left path or right path, which way would you like to go? ").lower()


if answer=="left":
    answer= input("you come to river where there is your destination, you can walk around ot swim accross? type walk or swim: ")
    if answer== "walk":
        print("You walked many miles but not find destination , unfortunately You Lost.")
    elif answer=="swim":
        print("You swim across and acheive your Destination, YOU WON !!")
    else:
        print("Not a vaild option. You Lost.")


elif answer =="right":
    answer =input("you come to bridge,it look like wobbly, do you want to cross  or back? : ")
    
    if answer== "back":
        print("You walked many miles but not find destination , unfortunately You Lost.")
    elif answer=="cross":
        answer = input("you cross the bridge and meet stranger . do you want to talk to them? (yes/no): ")
        if answer =="yes":
            print("You talked and they give you map. YOU WON!!")
        elif answer=="no":
            print("you ignore the stanger and offened and you lost.")
        else:
            print("Not a vaild option. You Lost.")
    else:
        print("Not a vaild option. You Lost.")


else:
    print("Not a valid option . You Lost.")

print("Thank you for Trying," , name)