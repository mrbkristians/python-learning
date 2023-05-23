alien_0 = {"color": "green", "points": 5} # store the key-values pairs in a dictionary
# each key is connected to a value
# Key's value can be number, string, list, dictionary, any object that maden in python or you can make in dictionary

print(alien_0["color"])
print(alien_0["points"])

# Adding New Key-Value pair
alien_0["x_position"] = 0 # add a new key-value pair to the dictionary
alien_0["y_position"] = 25

print(alien_0)

'''
Modifying Values in Dictionary
'''

alien_1 = {"color": "pink", "points": 10}
print(alien_1)

alien_1 = {"color": "blue"} # reassign the value of the key
print(alien_1)

alien_1 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"\nOriginal positionw: {alien_1['x_position']}")

# Move the alien to the right.
#Determine how far to move the alien based on it'scurrent speed.
if alien_1["speed"] == "slow":
    x_increment = 1
elif alien_1["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

# The new position is the old position + the increment
alien_1["x_position"] = alien_1["x_position"] + x_increment

print(f"\n\tNew position: {alien_1['x_position']}\n")

'''
Removing Key-Value Pairs
'''

alien_3 = {"color": "pink", "points": 5}

del alien_3["points"] # delete the key-value pair
# Be aware that the deleted key-value pair is removed permanently
print(alien_3)

''''
A dictionary of Similar Objects
'''

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edvard": "ruby",
    "phil": "python"
    }

language = favorite_languages["sarah"].title() # Syntax to pull a key from dictionary

print(f"\n\tSaras favorite programming language is: {language}.\n")

'''
Using get() to access Values
'''
language = favorite_languages.get("janka", "There is no such a person")
# if there is a chance the key your asking might not exist, use better get()
print(f"\n\t{language}\n")

