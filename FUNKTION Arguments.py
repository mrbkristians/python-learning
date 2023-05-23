print("\n")

# Positional Arguments
def describe(animal_type, pet_name):
    '''Display information about a pet.'''
    print(f"\n\tI have a {animal_type} and his name is {pet_name.title()}.")
    
describe("ddigger", "harry")
describe(animal_type="dog", pet_name="willie")


# Optional Argunments

def get_formatted_name(first_name, last_name, middle_name=""): # middle name is optional, default value is an empty string
    '''Return a full name'''
    if middle_name: # python interprets non-empty string as True
        full_name = f"{first_name} {middle_name} {last_name}"
    else: # if is False
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name("jimi", "hendrix", "lee")
print(f"\nTonight With Us {musician}!")


'''Arbinary number of Arguments'''

def make_pizza(size, *toppings): # asterisk means it takes any number of arguments an maki in tuple
    '''Show whitch pizza are making'''
    print(f"\nMaking a {size} size pizza with the following toppings:")
    for topping in toppings:
        print(f"\t- {topping}")

make_pizza(12, "pepperoni")
make_pizza(7, "mushrooms", "green peppers", "extra cheese")


'''Using Arbinary Keyword Arguments'''
# this function allows to enter key-value pairs as many as you want
def build_profile(first, last, **user_info):
    '''Building user profiles'''
    user_info["first_name"] = first # create dictionary called user_info
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("gustavo", "alstarulsmirus",
                             location= "riga",
                             age= "23",)

print(f"\n{user_profile}")