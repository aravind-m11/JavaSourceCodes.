def main():
    try:
        number1 = int(input("Enter the first number: "))
    except EOFError:
        number1 = 5  # Default value
    try:
        number2 = int(input("Enter the second number: "))
    except EOFError:
        number2 = 10  # Default value
    result = number1 + number2
    print(f"The sum of {number1} and {number2} is {result}")
    