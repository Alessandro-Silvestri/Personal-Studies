# RISK DICE COMPARING
# This program throws 6 dice (3 blue and 3 red), compares them and show the winner
# according the Risko game rules
# Made by Alessandro Silvestri

import random

class Risk():
     def check_win(self, red, blue):
          if red > blue:
               return 'red wins'
          elif red <= blue:
               return 'blue wins'

     def show_dice(self):
          # throwin the dice
          self.dices = [random.randint(1,6) for i in range(6)]
          print(f'\nred dice      {self.dices[0]} {self.dices[1]} {self.dices[2]}')
          print(f'blue dice     {self.dices[3]} {self.dices[4]} {self.dices[5]}')
          print('------------------')

          # checking the winner
          print('{} - {} - {}'.format(self.check_win(self.dices[0], self.dices[3]),
                                      self.check_win(self.dices[1], self.dices[4]),
                                      self.check_win(self.dices[2], self.dices[5])))
          print()


risk = Risk()
risk.show_dice()
