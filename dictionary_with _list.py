
# Store information about the pizza being ordered.
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"]
    }
# Summaraze the order. 
print(f"\nYou ordered a {pizza['crust']}-crust pizza " "with the following toppings:")

for topping in pizza["toppings"]:
    print(f"\t{topping}")

print("\n")


'''
Second example
'''
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"{name.title()}! I see you like more than one language!")
        print(f"{name.title()}'s favorite languages are:")
        for language in languages: # use variable to hold each value from the list that is in dictionary
            print(f"\t{language.title()}\n")
    elif len(languages) == 1:
        print(f"{name.title()}'s favorite language is:")
        print(f"\t{languages[0].title()}\n")
print("\n")
