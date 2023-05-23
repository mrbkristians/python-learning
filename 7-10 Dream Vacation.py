people_chose = []
prompt = "\n\t\tIf  you could visit onee place in the world,"
prompt += "\n\t\tWhere would you go? "
prompt += "\n\t\t(Enter 'quit' when everyone finished.) \n"
active = True
while active:
    place = input(f"\t\t\t{prompt}")
    if place == "quit":
        active = False
    else:
        print(f"\nGood choise {place.title()}!")
        people_chose.append(place)
print("\n\t\tPeople been choosing:")
for chose in people_chose:
    print(f"\t\t{chose.title()}")
