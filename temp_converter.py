print("-------Temp converter-------")
print("*" * 50)

print("1. celsius to Fahrenhiet converter")
print("2. Fahrenhiet to Celsius converter")
print("3. Celsius to kalvin converter")
print("4. kalvin to celsius converter")

choice = int(input("Enter a number to select the converter: "))
temp = float(input("Enter the value of Temp: "))

if choice == 1:
    print("{temp} in celsius = ", (temp * 9/5) + 32 , "F")

elif choice == 2:
    print("{temp} in fahrenhiet = ", (temp - 32) * 5/9 , "C")
    
elif choice == 3:
    print("{temp} in celsius = ", (temp + 273.15) , "K")
    
elif choice == 4:
    print("{temp} in kalvin = ", (temp - 273.15) , "C") 
    
else:
    print("INVALID CHOICE")      
    
    