#!/usr/bin/env python3

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def calculator():
    print("Simple Command-Line Calculator")
    print("Operations: +, -, *, /")
    
    while True:
        operation = input("\nEnter operation (+, -, *, /) or 'q' to quit: ").strip()
        
        if operation.lower() == 'q':
            print("Goodbye!")
            break
        
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please try again.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue
        
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        
        if isinstance(result, str):
            print(result)
        else:
            print(f"Result: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    calculator()