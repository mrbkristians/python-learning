from random import randint


class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        self.nr_of_side = 0
        self.total_sum = 0
        
    def roll_die(self):
        print("\n")
        spin_times = input("How many times you want to roll the dice?: ")
        spin_times = int(spin_times)
        while spin_times > 0:
            self.nr_of_side = randint(1, self.sides)
            print(f"\n\t\tYou rolled a {self.nr_of_side}")
            self.total_sum += self.nr_of_side
            print(f"Yout total sum of all roll's is : {self.total_sum}\n")

            spin_times -= 1
        
player_1 = Dice()
player_1.roll_die()