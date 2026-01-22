# Cesar Cano 
# Lab Extra Credit

# Ask for the first grade
score = float(input("Enter the grade percentage: "))

# Loop until user enters -1
while score != -1:

    # Determine the letter grade using AND conditions
    if score >= 90:
        grade = "A"
    elif score >= 80 and score < 90:
        grade = "B"
    elif score >= 70 and score < 80:
        grade = "C"
    elif score >= 60 and score < 70:
        grade = "D"
    else:
        grade = "F"

    print("You have a " + grade + "!\n")

    # Ask again
    score = float(input("Enter the grade percentage: "))

# End message when user enters -1
print("You have ended the program.")

