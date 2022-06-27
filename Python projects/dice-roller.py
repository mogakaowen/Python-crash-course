import random

#Enter the minimum and maximum limits of the dice rolls below

min_val = 1
max_val = 6

#the variable that stores the user’s decision
print('Welcome to the game of rolling dices, what is your name? ')
player=input('My name is: ')
wanna_play=input('Hi {player}, do you want to roll the dices? (Enter Yes/No) '.format(player=player) )


#The dice roll loop if the user wants to continue
while wanna_play.lower() == "yes":
    
    print("Dices rolling...")
    print("The values are :")

    #Printing the randomly generated variable of the first dice
    print(random.randint(min_val, max_val))

    #Printing the randomly generated variable of the second dice
    print(random.randint(min_val, max_val))

    #Here the user enters yes or y to continue and any other input ends the program
    wanna_play = input("Roll the Dices Again? ")

else:
    print("That's cool, have a good one!")