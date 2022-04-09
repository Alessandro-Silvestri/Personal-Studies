# Made by Alessandro Silvestri
# Scissors Paper Rock - Game
# My version of this game
# I created a function that checks which player wins


def paper_scissor_rock(p1, p2):
    if p1 == 's' and p2 == 'p' or p1 == 'p' and p2 == 'r' or p1 == 'r' and p2 == 's':
        print ('Player 1 Won')
    elif p1 == 's' and p2 == 'r' or p1 == 'p' and p2 == 's' or p1 == 'r' and p2 == 'p':
        print ('Player 2 Won')
    else:
        print('Draw')


# Insert:
# 's' for Scissors
# 'p' for Paper
# 'r' for Rock


paper_scissor_rock('p', 'r')
# Player 1 won!
