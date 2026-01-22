#We are going to create a code to create a guessing game
oldwords = [] #This creates a blank list/array
game = "play"
while game == "play":
    newword = input("Enter a 3-letter word: ")
    if len(newword) > 3 or len(newword) < 3:#We are checking is 3-letters
        print("That's not a 3-letter word.")
    else:
        if newword in oldwords:#If 3-letter word is repeated, game over!
            game="over"
            print("You already said that word. Game over.")
            print("You know", len(oldwords), "3-letter words.")
        else:
            print("Nice one.") #If 3-letter word new, we continue
            oldwords.append(newword)
