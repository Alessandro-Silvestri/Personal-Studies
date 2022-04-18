# GUESS THE NUMBER GAME
# Made by Alessandro Silvestri

# The computer will choose a random number between 1 and 20 and you have to guess it with a random number attempts
# between 1 and 5

import random
print(f'''

 ___                     ___  _         _ _              _             
/  _>  _ _  ___  ___ ___|_ _|| |_  ___ | \ | _ _ ._ _ _ | |_  ___  _ _ 
| <_/\| | |/ ._><_-<<_-< | | | . |/ ._>|   || | || ' ' || . \/ ._>| '_>
`____/`___|\___./__//__/ |_| |_|_|\___.|_\_|`___||_|_|_||___/\___.|_|  
                                                                       
''')
# with while True I created an infinite loop
while True:
    secret_num = random.randint(1, 20)  # it choses a random number between 1 and 20
    attempts = random.randint(1, 5)
    i = 1  # I set the counter

    while i <= attempts:
        print(f'{i} of {attempts} attempts to guess a number between 1 and 20')
        answer = int(input('guess the number: '))

        # here I check the answer
        if answer == secret_num:
            break
        elif answer < secret_num:
            print('go up!')
            print('')
        elif answer > secret_num:
            print('go down!')
            print('')
        i += 1

    # --------------------- OUT OF INTERNAL LOOP ---------------------

    if answer == secret_num:
        print('you won')
    if answer != secret_num:
        print(f'you lost, the number was {secret_num}')
    print('GAME OVER')
    print('')


    # I use and infinite loop for asking the user if he wants to play again (in this case the loop is useful
    # for checking the user answer if he puts a wrong command)
    while True:
        play_again = str(input('Do you want play again? y/n: ')).lower()
        if play_again == 'n':
            break
        elif play_again == 'y':
            print('ok!')
            print('')
            break
        else:
            print('wrong command')

    # if the user press n quit the external loop
    if play_again == 'n':  
        break

