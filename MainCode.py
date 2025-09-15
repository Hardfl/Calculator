# calculator.py
# basic calculator to practice writing code in python :3

import math

# operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y 

def multiply(x, y):
    return x * y 

def divide(x, y): 
    if y == 0:
        return "Error! Division by zero."
    return x / y

def mod(x, y):
    return x % y 

def mathsqrt(x):
    return math.sqrt(x)

def square(x):
    return x * x


# main loop
while True:
    print("\nPick an operation to perform:")
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    print("5. modulus")
    print("6. square root")
    print("7. square")
    print("Q. quit")

    choice = input("Enter choice (1/2/3/4/5/6/7 or Q): ").lower() #not case-sensitive

    # Exits the condition
    if choice == "q":
        print("Bai-Bai! 👋")
        break

    # Handle single-number operations
    if choice == "6":
        num = float(input("Enter number: "))
        print("√", num, "=", mathsqrt(num))

    elif choice == "7":
        num = float(input("Enter number: "))
        print(num, "² =", square(num))

    # Handles operations with 2 numbers
    elif choice in ["1", "2", "3", "4", "5"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1": 
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == "2": 
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == "3": 
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == "4": 
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == "5": 
            print(num1, "%", num2, "=", mod(num1, num2))

    # Invalid input
    else:
        print("Cannot choose that. Please try again.")
