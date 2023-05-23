
file_path = "/Users/djkristians/Documents/GitHub/PYTHON-LEARNING/Reading file/pi_digits.txt"
'''Read o whole '''
with open(file_path) as file:
    file_contents = file.read()
print(file_contents.rstrip())

print("\n")
'''Read line by line'''
with open(file_path) as file_object:
    lines = file_object.readlines() # readline() mehod takes each line from the file and stores it in a list

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
print(f"{pi_string[:10]}")

'''
birthday = input("Enter your birthday (ddmmyy): ")
if birthday in pi_string:
    print("Your birthday appears in the first digits of pi!")
else:
    print("Your birthday does not appear in the pi digit")
'''

''''''
file_path_2 = "/Users/djkristians/Documents/GitHub/PYTHON-LEARNING/Reading file/new_try.txt"
with open(file_path_2) as file_object:
    new_file = file_object.readlines()
    for line in new_file:
        line.replace("i", "you")
        print(line.strip())
print(new_file)