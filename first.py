import random
target = random.randint(1, 20)

while True:
    userchoice = input("Guess the Target or Quit the game by pressing Q: ")

    if userchoice == "Q":
        break

    if userchoice.isdigit():
        userchoice = int(userchoice)

        if userchoice == target:
            print("Success: Correct Guess!")
            break
        elif userchoice > target:
            print("You chose a bigger number, choose a smaller one.")
        else:
            print("You chose a smaller number, choose a bigger one.")
    else:
        print("Please enter a valid number between 1 and 20 or 'Q' to quit.")

print("-----GAME OVER-----")




