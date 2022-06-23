# SUDOKU CHECK
# This program asks the user to insert a completed sudoku and checks if it's valid
# By Alessandro Silvestri, assignement solved for Python Institute


# I put the string numbers in the sudoku matrix list
def fill_line_numbers(input_string, line_number):
     counter = 0
     for i in input_string:
          sudoku_matrix[line_number][counter] = i
          counter += 1


# check if the numbers are unique in a given string
def check_unic_num_list(list):
     is_unique = False
     for i in list:
          if list.count(i) == 1:
               is_unique = True
          else:
               is_unique = False
               break
     return is_unique


# check if all numbers in a vertical line are different
def check_vertical_line(column):
     a = []
     for i in range(9):
          a.append(sudoku_matrix[i][column])
     return check_unic_num_list(a)


# I create the a square and I check if all numbers inside are different
def create_square(a, b, c, d):
     square = []
     for j in range(a, b):
          for i in range(c, d):
               square.append(sudoku_matrix[j][i])
     return(check_unic_num_list(square))


# compare all the horizontal lines
def check_all_horizontal_numbers():
     is_unique = False
     for i in range(9):
          if check_unic_num_list(sudoku_matrix[i]):
               is_unique = True
          else:
               is_unique = False
               break
     return is_unique


# compare all the vertical numbers
def check_all_vertical_numbers():
     is_unique = False
     for i in range(9):    
          if check_vertical_line(i):
               is_unique = True
          else:
               is_unique = False
               break
     return is_unique


# check if in all the square there are unique numbers
def check_all_squares():
     dict_squares = {
          0: create_square(0, 3, 0, 3),
          1: create_square(0, 3, 3, 6),
          2: create_square(0, 3, 6, 9),
          3: create_square(3, 6, 0, 3),
          4: create_square(3, 6, 3, 6),
          5: create_square(3, 6, 6, 9),
          6: create_square(6, 9, 0, 3),
          7: create_square(6, 9, 3, 6),
          8: create_square(6, 9, 6, 9),
     }
     are_all_squares_ok = False
     for i in dict_squares:
          if dict_squares.get(i):
               are_all_squares_ok = True
          else:
               are_all_squares_ok = False
               break
     return are_all_squares_ok


# check the user's inputs (only digits and 9 numbers)
def input_check(input_txt):
     if input_txt.isdigit() and len(input_txt) == 9:
          return True
     else:
          return False

# input the 9 lines of numbers and check if they are correct
dict_numbers_input = {}
input_num = 0

while input_num < 9:
     while True:
          dict_numbers_input[input_num] = input(f"line {input_num + 1}: > ")
          if input_check(dict_numbers_input[input_num]):
               input_num += 1
               break
          else:
               print('You have to insert only 9 numbers')

# I draw the board
sudoku_matrix = [[i for i in range(9)] for j in range(9)]

# I fill the board with the given numbers
for i in range(9):
     fill_line_numbers(dict_numbers_input[i], i)

# Prints the updated board like a list
for i in sudoku_matrix:
     print(i)

# final comparison
if check_all_horizontal_numbers() and check_all_vertical_numbers() and check_all_squares():
     print('SUDOKU OK!')
else:
     print('SUDOKU NOT SOLVED')

