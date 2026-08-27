import random

choices = ["rock", "paper", "sessor"]
computer = random.choice(choices)

user = input("Enter rock, paper, or scissors: ")

if user == computer:
    print("Draw")
    
elif user == "rock" and computer == "sessor":
    print("you win")

elif user == "rock" and computer == "paper":
    print("you win")  

elif user == "paper" and computer == "sessor":
    print("computer win")

elif user == "paper" and computer == "rock":
    print("computer win")

elif user == "sessor" and computer == "rock":
    print("computer win")
    
elif user == "sessor" and computer == "paper":
    print("you win")
    
else:
    print("invalid")