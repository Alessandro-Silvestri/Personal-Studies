# PASSWORD GENERATOR
# This program generates a string with random characters capital/no capital, numbers and 
# the first character can't be a number.
# In the function you can pass the password lenght.
# Made by Alessandro Silvestri

import random

def password_generator(chrnum):
     # The first character has to be a letter: capital or not
     if random.randint(0, 1) == 0:
          password = chr(random.randint(65, 90))
     else:
          password = chr(random.randint(97, 122))
     # password generator loop
     character = ''
     counter = 1
     while counter <= chrnum - 1:
          character = chr(random.randint(48, 122))
          if not character.isalnum():
               continue
          password += character
          counter += 1
     return password

# in the function I pass the password lenght
for i in range(20):
     print(password_generator(40), password_generator(40), password_generator(40))


