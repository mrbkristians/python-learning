import json

filename = "numbers.json" # we make sure to read the same file as write
with open(filename, ) as f: # python needs only to read from file
    numbers = json.load(f) # function to load the information stored somewhere
print(numbers)