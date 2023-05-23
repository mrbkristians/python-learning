
users = ["janis", "peteris", "maks", "juris", "admin", "anna", "maria"]

# cheking if the input is alphabet only
while True:  
    new_user = input("Please enter your user name: ").lower() # save in variable only lowercase name
    if new_user.isalpha():
        break
    else:
        print("Please enter a valid user name")

# check if the new_user choosen user name is free
if new_user in users:
    print(f"Choose another user name:")
else:
    users.append(new_user)

# Print Hello to each user and special welcom for admin
if users:
    for user in users:
        if user == "admin":
            print(f"Hello {user.upper()}, how is your day?")
        else:
            print(f"\n\tWelcom {user.title()}!")
else:
    print("\nNo Users In here")