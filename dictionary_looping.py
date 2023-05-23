''''
Looping through a key-valu pairs
'''
user_0 = {
    "username": "emfi",
    "first": "enrico",
    "last": "fermi",
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}\n")

'''

'''

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }
friends = ["phil", "sarah"]

print("\n")
for name, language in favorite_languages.items(): #loop throug esc key-value pair in dictionary. As it works tru each pair the key is assigned to variable "name", and value is assigned to a variable "languages"
    print(f"\t{name.title()}'s favorite language is {language.title()}")
print("\n")


'''
Looping through all Keys in Dictionary
'''
for name in favorite_languages.keys():
    print(f"Hola {name.title()}.")
    if name in friends: # check whether the name is in the list friend. 
        language = favorite_languages[name].title() # if yes we determine the person's favorite language using the name of the dictionary and the current value of name as the key.
        print(f"\t{name.title()}, I see you like {language}")


# use the key() method to find out a particular person was polled. 
if "erin" not in favorite_languages.keys():
    print("Erin, please take a poll!")

print("\n")

'''
Looping Through a Dictionary's Keys in a Particular Order
'''
print("New section")

for name in sorted(favorite_languages.keys()):
    print(f"\t{name.title()}, thank you for taking the poll.")

''''
Looping Through All Values in Dictionary
'''
print("\n")
print("New section")
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

print("\n")