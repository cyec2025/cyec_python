number = 3
first = 0

print("The super number game!!\n")

picked = input("Guess a number (1-7)! > ")
print()
picked = int(picked)
if picked == 3:
    print("wow! your amazing!")
    print("you deserve a prize!")
    input("the prize is...")
    print("MMMMMMORE QUESTIONS!!!!")
    first += 1
elif picked > 7 or picked < 1:
    print("PLAY BY THE RULES.")
elif picked < 3:
    print("Tooo LOW!\nguess HIGHER")
elif picked > 3:
    print("You're up in the clouds, buddy!\nGuess LOWER")
print()
if first == 1:
    print("Let's see if your luck persists!")
else:
    print("Let's try a different one...")
print()
picked = int(input("Guess a number (1-7)! > "))
if picked == 5:
    print("wow! your super amazing!")
    print("you deserve a prize!")
    input("the prize is...")
    input("death.")
    goober = 50
    while goober > 1:
        print("HAHAHAHAHAHAHHAHAHAA")
        print("AHAHAHAHHAHAHAAAHAHAHAH")
        goober -= 1
    input("just kidding.")
    print()
    first += 1
elif picked > 7 or picked < 1:
    print("PLAY BY THE RULES.")
elif picked < 5:
    print("Tooo LOW!\nguess HIGHER")
elif picked > 5:
    print("You're up in the clouds, buddy!\nGuess LOWER")
print()
print("final results...")
print()
if first == 0:
    print("you really suck at this...")
elif first == 1:
    print("i guess you did fine")
else: print("you're really good at this.\n\ncome again soon!")
