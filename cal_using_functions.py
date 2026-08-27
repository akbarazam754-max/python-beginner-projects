print("====== SIMPLE CALCULATOR ======")

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Choose an operation (1-4): ")

if choice == "1":
    result = add(num1, num2)
    print("Result:", result)

elif choice == "2":
    result = subtract(num1, num2)
    print("Result:", result)

elif choice == "3":
    result = multiply(num1, num2)
    print("Result:", result)

elif choice == "4":
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        result = divide(num1, num2)
        print("Result:", result)

else:
    print("Invalid choice!")