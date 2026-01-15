# Cesar Cano
# Lab #9 gethub test

def fahr_to_cels(): #This part was taught from Lab 8
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * (5 / 9) #fahrenheit to celsius
    print("The temperature in Celsius is:", celsius)


# 1. Ask the user to enter their name
name = input("Enter your name: ")

# 2. Create a menu with 5 options
print("\n--- Choose an option,", name, "---")
print("1 - Hear a CS joke")
print("2 - Display your name 15 times")
print("3 - Enter a number and print a famous quote that many times")
print("4 - Play a guessing game")
print("5 - Convert Fahrenheit to Celsius")
print("--------------------")

choice = int(input("Enter your choice (1, 2, 3, 4, or 5): "))

# Option 1: Display a joke
if choice == 1:
    print("--------------------")
    print(f"\nHere's a joke {name}:")
    print("--------------------")
    print("Why is the Macintosh Computer full?")
    print("Because it took a HUGE byte of it's Apple!")
    print("--------------------")

# Option 2: Display user's name 15 times
elif choice == 2:
    print("--------------------")
    print("\nDisplaying your name 15 times:\n")
    for i in range(15):
        print(name)
    print("--------------------")

# Option 3: Famous quote repeated
elif choice == 3:
    number = int(input("Enter a number: "))
    print("--------------------")
    print(f"\n--- Here is your quote {name}: ---\n")
    for i in range(number):
        print("In MATH, Mistakes Allow Thinking to Happen. - Unknown")
    print("--------------------")

# Option 4: Guessing Game
elif choice == 4:
    guessNumber = 5   # number to guess
    guess = int(input("Guess a number between 0 and 100: "))

    while guess != guessNumber:
        if guess < 0 or guess > 100:
            print("Please enter a number within the range 0 to 100.")
        elif guess > guessNumber:
            print(f"Too high {name}! Try again.")
        else:
            print(f"Too low {name}! Try again.")

        guess = int(input("Guess a number between 0 and 100: "))

    print(f"You won {name}! Great job guessing the number!")

# Option 5: Temperature conversion function
elif choice == 5:
    fahr_to_cels()

# If user enters something else
else:
    print("The options are only 1-5. Please run the program again pick from those options.")
