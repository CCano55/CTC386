# Cesar Cano
# Final Question #4

def new_year(guess):
    for i in range(guess):
        print("Happy New Year!")

def message(guess):
    for i in range(guess):
        print("")

guess = int(input("Enter a number between 1 and 10: "))

while guess < 1 or guess > 10:
    print("Please enter a number within the range 1 to 10.")
    guess = int(input("Enter a number between 1 and 10: "))

print("You entered a valid number!")

message(guess)
new_year(guess)

