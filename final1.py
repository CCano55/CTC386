# Cesar Cano
# Final: question #1

# Asking options 1-3
print("Choose an option:")
print("1 - Tell a joke with your name")
print("2 - Display a food name 20 times")
print("3 - Enter numbers until you enter 0")

option = int(input("Enter your choice (1, 2, or 3): "))

# Option 1: Ask for name and print a joke
if option == 1:
    name = input("Enter your name: ")
    print(f"Why did the Samsung smile, {name}?")
    print("Because it had a byte of a macintosh!")

# Option 2
elif option == 2:
    food = input("Enter the name of a food: ")
    for i in range(20):
        print(food)

# Option 3
elif option == 3:
    number = int(input("Enter a number and 0 to end: "))

    while number != 0:
        if number > 0:
            print("Warning! Too high! Try again.")
        else:
            print("Warning! Too low! Try again.")

        number = int(input("Enter a number and 0 to end: "))

    print("Correct! You entered 0. Program ended.")

# If invalid menu option
else:
    print("Invalid option. Please run the program again.")
