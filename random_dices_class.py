# Made by Alessandro Silvestri
# Roll 2 dices (using a class), the result is a tuple
# I created function in a class

import random


class Dice:
    def roll(self):                 # I define a function in a class
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        return a, b                 # Python puts 'a' and 'b' in a tuple automatically


dice = Dice()                       # I create an object from the class Dice
print(dice.roll())                  # I call the function 'roll' from the class 'Dice'
