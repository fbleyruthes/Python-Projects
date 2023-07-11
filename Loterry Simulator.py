#Lottery

#Libraries
import random
import os

#Arrays
choices = []
drawNumber = []

#Variables
n = 0
numberOfBets = 0
successes = 0
choice = 0

#The user chooses how many numbers he/she want to bet
while ((numberOfBets != 6) and (numberOfBets != 9) and (numberOfBets != 15)):
    try:
        numberOfBets = int(input("How many numbers do you want to bet today? 6, 9 or 15?\n"))
        if numberOfBets not in [6, 9, 15]:
            os.system('cls') #This command clears the terminal while running
            print("Invalid input. Please enter 6, 9, or 15.")
    except ValueError:
        os.system('cls')
        print("Invalid input. Please enter an integer number.")



#Now the user chooses the numbers he/she want to bet
for i in range (0, numberOfBets):
    if (i == 0):
         while ((choice < 1) or (choice > 60)):
            try:
                choice = int(input("Choose your {}o number, from 1 to 60: ".format(i+1)))
            except ValueError:
                print("Invalid input. Please enter an integer number.")  
    else:
        while ((choice < 1) or (choice > 60) or (choice in choices)):
            try:
                choice = int(input("Choose your {}o number, from 1 to 60: ".format(i+1)))
            except ValueError:
                print("Invalid input. Please enter an integer number.")

    choices.append(choice)

os.system('cls')

#Time to drawn the winning numbers
for j in range (0,6):
    drawn = random.randint(1,60)
    if (j > 0):
        while (drawn in drawNumber):
            drawn = random.randint(1,60)
    drawNumber.append(drawn)

#We need to check how many numbers the user got right
for k in range (0,len(drawNumber)):
    for w in range (0, len(choices)):
        if (choices[w] == drawNumber[k]):
            successes += 1

#Final messages 
print("Your choices: {}".format(choices))
print("Drawn numbers: {}".format(drawNumber))

if (successes < 4):
    print("Sorry... Not this time. You only got {} numbers right. Try again next time!".format(successes))
elif (successes == 4):
    print("You got {} numbers right! You deserve a good prize!".format(successes))
elif (successes == 5):
    print("You got {} numbers right! You deserve a great prize!".format(successes))
elif (successes == 6):
    print("You got {} numbers right! You deserve the best prize!".format(successes))

        