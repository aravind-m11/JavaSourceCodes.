def main():
    # Input a number from the user
    number = int(input("Enter an integer: "))

    # Check if the number is even or odd
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

if __name__ == "__main__":
    main()