filename ="programming.txt"

with open(filename, "r+") as file_object:
    new_file = file_object.read()
    file_object.write("i like to programm")
print(new_file)

