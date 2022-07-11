# ROLLING DICES
# the program asks the number of dices to play
# Made by Alessandro Silvestri

import random

class RandomDices:
     def __init__(self) -> None:  
          self.dices = [[
               '+---+',
               '|   |',
               '| o |',
               '|   |',
               '+---+',
               ],
          [
               '+---+',
               '|o  |',
               '|   |',
               '|  o|',
               '+---+',
               ],
          [
               '+---+',
               '|o  |',
               '| o |',
               '|  o|',
               '+---+',
               ],
          [
               '+---+',
               '|o o|',
               '|   |',
               '|o o|',
               '+---+',
               ],
          [
               '+---+',
               '|o o|',
               '| o |',
               '|o o|',
               '+---+',
               ],
          [
               '+---+',
               '|o o|',
               '|o o|',
               '|o o|',
               '+---+',
               ]
               ]

     def rolling(self, num_of_dices):
          dict_chosen_dice = {}

          for i in range(num_of_dices):
               dict_chosen_dice[i] = random.randint(0, 5)

          for i in range(5):
               for j in range(num_of_dices-1):
                    print(self.dices[dict_chosen_dice[j]][i], end=' ')
               print(self.dices[dict_chosen_dice[num_of_dices-1]][i])


roll_dices = RandomDices()
while True:
     a = input("How many dices you want to play? ('x' to exit) > ")
     if a.lower() != 'x':
          roll_dices.rolling(int(a))
     else:
          break

