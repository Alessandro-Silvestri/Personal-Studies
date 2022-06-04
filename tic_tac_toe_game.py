# TIC TAC TOE - Game
# Chose one of the squares and play against the computer! :)
# It always starts first, in the middle
# Made by Alessandro Silvestri

import random
board = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 'X', '6': 6, '7': 7, '8': 8, '9': 9}
not_available_squares = ['5', ]
permitted_choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def draw_board():
    print(f'''
    +-------+-------+-------+
    |       |       |       |
    |   {board['1']}   |   {board['2']}   |   {board['3']}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board['4']}   |   {board['5']}   |   {board['6']}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board['7']}   |   {board['8']}   |   {board['9']}   |
    |       |       |       |
    +-------+-------+-------+
''')


def check_the_winner(player):
    return board['1'] == player and board['2'] == player and board['3'] == player or \
        board['4'] == player and board['5'] == player and board['6'] == player or \
        board['7'] == player and board['8'] == player and board['9'] == player or \
        board['1'] == player and board['4'] == player and board['7'] == player or \
        board['2'] == player and board['5'] == player and board['8'] == player or \
        board['3'] == player and board['6'] == player and board['9'] == player or \
        board['1'] == player and board['5'] == player and board['9'] == player or \
        board['7'] == player and board['5'] == player and board['3'] == player


while True:
    draw_board()

    # checking the winner and if the match is draw
    if check_the_winner('O'):
        print("YOU WIN!")
        break
    elif check_the_winner('X'):
        print('COMPUTER WINS')
        break
    elif len(not_available_squares) == 9:
        print('DRAW!')
        break

    # user move and checking if the choice is valid
    move = input('where? > ')
    if move not in permitted_choices:
        print("You have to insert a number between 1 and 9")
        continue

    if move not in not_available_squares:
        board[move] = 'O'
        not_available_squares.append(move)
    else:
        print("You can't, choose another square")
        continue

    # computer move
    while not check_the_winner('O'):
        move = str(random.randint(1, 9))
        if move not in not_available_squares:
            board[move] = 'X'
            not_available_squares.append(move)
            break

