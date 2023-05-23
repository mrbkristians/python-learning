magicians = ["alice", "david", "kaspars"]
for magician in magicians: # making for loop on the list
    print(f"\nFor every magician in the list of magicians, print the magician's name: {magician.title()}")
    print(f"\tCan't wait to see your next trick {magician.title()}!\n")

print("Thank you, everyone. Than was a great magic show!\n")

# List comprehensions
squares = [value ** 2 for value in range(1, 200)]
print(squares)

# Slicing a List
players = ["charles", "martina", "michael", "florence", "eli"]
print(f"\nOriginal list of players: {players}")
print(f"Slice of a list: {players[0:3]}") # prints a slice of a list
print(players[:4]) # prints from begining till the index we specify
print(players[2:]) # prints from index 2 till the end
print(players[:-3]) # prints last 2 elements from the end od the list

print(f"\nHere is my first 3 players: ")
for player in players[:3]:   # looping through specifyed slice of a list
    print(f"\n\tPlayer name: {player.title()}")

print(f"\nThank you for the game!\n")

# copying list
my_food = ["pizza", "falafel", "carrot cake"]
friend_food = my_food[:]  # makes a copy of a list in to a new list

my_food.append("cannoli")
friend_food.append("ice cream")

print(f"\nMy favorite food:\n\t{my_food}\n")
print(f"\nMy friends favorite food:\n\t{friend_food}\n")


''''
Checking in an element is in a list
'''
reguested_toppings = ["mushrooms", "pepperoni", "pineapple", "extra cheese"]

"mushrooms" in reguested_toppings # True
"beef" in reguested_toppings # False

#checking an element if tš not in  a list
banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(f"\n\t{user.title()}, you can enter if you want")
else:
    print(f"\n\tStay da fuck out off here\n")