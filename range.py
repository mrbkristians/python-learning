for num in range(1, 6): # generate a series of number from 1 to 6
    print(f"\n{num}\n")

numbers = list(range(1, 100)) # list() makes list from a given value
print(numbers)

even_numbers = list(range(2, 101, 2)) # in this example function range() starts with the value 2 an then adds to to that value. It adds 2 repeatedly until reaches or passes the end value 101, and produces this result
print(f"\n{even_numbers}\n")

squares = []
for value in range(1,102):
    square = value ** 2 # exponent darbība, latviski reizinājums kubā
    '''squares.append(square) # add element to the end of the list'''
    squares.append(value**2) # add element to the end of the list and make value exponent
print(squares)
