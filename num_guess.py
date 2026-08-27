num = 50
guess = int(input("enter the number : ")) 

if guess < 0:
    print("Invalid number")
    
elif guess <= 10:
    print(" v bad")

elif guess <=20:
    print("bad ")
    
elif guess <= 30:
    print("good")

elif guess <= 40:
    print("v good") 
    
elif guess < 50:
    print("nice try")

# elif guess >= 50:
#     print("EXCELLENT")
    
elif guess == 50:
    print("congratulations u have guessed it right")

else:
    print("invalid num")