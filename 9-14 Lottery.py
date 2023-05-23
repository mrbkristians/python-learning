import random


lottery_symbols = ("a", "b", "c", "d", "e", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
my_ticket = ("b", "d", 2, "e")
try_count = 0

while True:
    winning_symbols = random.sample(lottery_symbols, 4) # random.sample choose random elements from list, hom much you need
 

    if winning_symbols == my_ticket:
        try_count += 1
        print("You won!")
        print(f"You won win {try_count} try!")
        break
    else:
        try_count += 1
        print(try_count)
        
