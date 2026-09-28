print("=== Command-Line Calculator ===")

try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print("Result:", result)
    else:
        print("Error: Invalid operation.")

    if operator in ["+", "-", "*"]:
        print("Result:", result)

except ValueError:
    print("Error: Please enter valid numbers.")