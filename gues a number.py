
from random import randint
from random import choice


'''Gues the same nuber as Computer'''

print("\n\t\t\tWelcome to the Number Guessing Game!")
print("\t\tCould you gues the same nuber as Computer from 1 to 5?")

game_on = True
your_choice = 0
pc_chioce = 0

enter_game = input("\n\t\t\tEnter y to continue and n to exit: ")
while game_on:
    if enter_game == "n":
        print("\t\tThanks for playing!")
        print("\t\tPussy Boy!")
        game_on = False
        break
    else:
        your_choice = input("\n\t\t\tGuess a number from 1 to 5: ")
        your_choice = int(your_choice)
        pc_choice = randint(1,5)
        pc_choice = int(pc_choice)
        if your_choice == pc_choice:
            print("\n\t\t\t\tYou a Right!")
            print(f"\t\t\tYou and Maschine choose the same number {your_choice}!")
        else:
            print(f"\n\t\t\t\t\tYou choose {your_choice}")
            print(f"\t\t\t\tMaschine choose {pc_choice}")

    print("\n\t\t\tWould you like to play again?")
    new_game = input("\t\t\t!!! Enter y to play again and n exit: ")
    if new_game == "n":
        print("Thanks for playing!")
        print("This is my first game writen by me!")
        game_on = False
        break



