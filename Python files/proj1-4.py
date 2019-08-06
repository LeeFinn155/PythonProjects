
MAX_GUESS = 10

mynum = random.randint(1,100)
guessnum = 0

notyet = True

print("Try to guess my number, you have 10 guesses.")
print("")

while ((notyet) and (guessnum < MAX_GUESS)):
    yourguess = int(input("What is your guess? "))
    guessnum = guessnum + 1
    
    if (yourguess < mynum):
        print("Too low")

    elif (yourguess > mynum):
        print("Too high")

    else:
        print("You got it!")
        notyet = False

if (yourguess == mynum):
    print("You win!")
else:
    print("Sorry, you lose.")
