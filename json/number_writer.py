import json  # import json mudule

numbers = [2, 3, 5, 7, 20, 50] # create list of number to work with

filename = "numbers.json" # choose a filename in witch to store the list of numbers
with open(filename, "w") as file_object: # open file in write mode
    json.dump(numbers, file_object) # function to dump the list of numbers


