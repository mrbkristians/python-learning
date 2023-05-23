
'''Passing a LIST in to a function'''

def greet_users(names): # define a function that expects input
    '''Print a simple greeting'''
    for name in names: # function loops through the list it receives
        msg = f"Hello, {name.title()}!" # making a greeting form 
        print(msg) # printing out the greeting for each person

usernames = ["anna", "tanja", "lorena"] # we define a list of users
greet_users(usernames) # pass the list of usernames to greet_users() in our function call

print("\n\n")


'''Modifying a List in a Function'''

def print_models(unprinted_models, completed_models):
    '''
    Simulate printing each design, untill no are left.
    Move each design to completed_models after printing.
    '''
    while unprinted_models:
        current_model = unprinted_models.pop()
        print(f"Curentlly printing: {current_model}")
        complited_models.append(current_model)

def show_complete_models(complited_models):
    '''Show all models that are printed'''
    print("Following models been printed: ")
    for complited_model in complited_models:
        print(complited_model)

unprinted_models = ["phone case", "wall paper", "robot pendant", "dj decks"] #Start with some designs that need to printed
complited_models = []

print_models(unprinted_models[:], complited_models,) # The slice notation [:] makes a copy of the list to send to the function
# if there is no specific reason to pass a copy, should use an original list
show_complete_models(complited_models)

print("\n\n")