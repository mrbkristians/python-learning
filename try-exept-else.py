print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

'''ZeroDivisionError
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError: # using exceptions to prevent crashes
        print("You can't divide by zero!")
    else:    
        print(f"{first_number} / {second_number} = {answer}")
'''

'''FileNotFoundError'''
def count_words(filename):
    '''Count the approximate number of words in a file.'''
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        
         # print(f"Sorry, the file {filename} does not exist.")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filename = ["alices.txt", "programming.txt", "art.txt"]
for file in filename:
    count_words(file)


