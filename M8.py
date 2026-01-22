#Cesar Cano
#Midterm #8
number = int(input("Enter a number between 1 and 10: "))
while number < 1 or number > 10:
    print("That number iis not in the range.")
    number = int(input("Enter a number between 1 and 10: "))

print("Your number is in the correct range.")

