# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

# User Interface
def calculator():
    pass
    
while True:
        # Take input from the user
        choice = input("Enter choice (+ ,- ,* , /): ")

        # Check if the choice is one of the four options
        if choice in ('+', '-', '*', '/'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '+':
                print(f"The result is: {add(num1, num2)}")

            elif choice == '-':
                print(f"The result is: {subtract(num1, num2)}")

            elif choice == '*':
                print(f"The result is: {multiply(num1, num2)}")

            elif choice == '/':
                print(f"The result is: {divide(num1, num2)}")
            
            # Ask if the user wants to perform another calculation
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input")

# Call the calculator function
calculator()