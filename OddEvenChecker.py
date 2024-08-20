def main():
    try:
        # Input a number from the user, with a default value of 0 if no input is provided
        input_str = input("Enter an integer (default is 0): ")
        if not input_str.strip():
            number = 0
        else:
            number = int(input_str)
    except EOFError:
        # Handle cases where input is not possible (like in CI environments)
        number = 0

    # Check if the number is even or odd
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

if __name__ == "__main__":
    main()
