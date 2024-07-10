print("Welcome to Quiz Game !")
  
playing = input("Do you want to Play?")

if playing.lower() != "yes": 
    quit()

print("Okay ! Let's Play :) ")
score = 0
answer = input("what does CPU Stand For ?")
if answer.lower() == "central processing unit":
    print("Correct !")
    score +=1
else:
    print("Incorrect ")


answer = input("What is fullform of api ?").lower()
if answer == "application programming interface":
    print("Correct !")
    score +=1
else:
    print("Incorrect ")
    
answer = input("what does RAM stand for ?").lower()
if answer == "random access memory":
    print("Correct !")
    score +=1
else:
    print("Incorrect ")
    
answer = input("what does GPU stand for ?")
if answer == "graphic processing unit":
    print("Correct !")
    score +=1
else:
    print("Incorrect ")


print("You Got "  +str(score) + " question correct!")
print("You Got "  +str((score/4)*100) + " %.")