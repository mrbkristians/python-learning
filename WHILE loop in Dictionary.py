print("\n")

# Moving Items from One List to Another
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

for unconfirmed in unconfirmed_users:
    print(f"\nUnconfirmed user: {unconfirmed.title()}")

while unconfirmed_users: # while loop runs while the list is not empty
    current_user = unconfirmed_users.pop() # pop() removes user from one list to variable one at the time from the end
    print(f"\nVerifying user: {current_user.title()}") # print user that is working on to move
    confirmed_users.append(current_user) # add user to another list

# Display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users: # for loop true the new list
    print(confirmed_user.title())

print("\n")

# Removing All Instances of Specific Values from a List
pets = ["dog", "cat", "fish", "cat", "spider", "cat"]
print(pets)
while "cat" in pets:
    pets.remove("cat")
print(pets)


print("\n")