dog = {"owner": "eric", "kind": "dog", "name": "willie", "color": "pink"}
cat = {"owner": "anna", "kind": "cat", "name": "billie", "color": "black"}
rat = {"owner": "lorena", "kind": "rat", "name": "pisun", "color": "grey"}
frog = {"owner": "patric", "kind": "frog", "name": "rigdi", "color": "green"}

pets = [dog, cat, rat, frog]

print("\n")

for animal in pets:
    print(f"{animal['name'].title()} is a {animal['color']} {animal['kind']}!")

print("\n")