# CALCULATOR APP

operator = input("Enter the operator (+, -, *, /): ")
if operator not in ('+', '-', '*', '/'):
    print("Invalid operator")
else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if operator == '+':
        def add_numbers(num1, num2):
            return num1 + num2
        print("The sum is:", add_numbers(num1, num2))
    elif operator == '-':
        def subtract_numbers(num1, num2):
            return num1 - num2
        print("The difference is:", subtract_numbers(num1, num2))
    elif operator == '*':
        def multiply_numbers(num1, num2):
            return num1 * num2
        print("The product is:", multiply_numbers(num1, num2))
    elif operator == '/':
        def divide_numbers(num1, num2):
            return num1 / num2
        print("The quotient is:", divide_numbers(num1, num2))