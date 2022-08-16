# TEXT FILE LETTERS COUNTER
# Made by Alessandro Silvestri for Python Institute

# user interface: loop until the file name is correct
while True:
     try:
          input_file_name = input('\nCounting letters in alphabetical order, insert file name: ')
          letters_dict = {}
          reader = open(input_file_name, 'r')
          content = reader.read().lower()
          reader.close()
          break
     except:
          print('error file')



# letters counting
for i in content:
     if i in letters_dict:
          letters_dict[i] += 1
     elif i == ' ' or i == '.' or i == '\n':
          continue
     else:
          letters_dict[i] = 1

# creating a letters_dict keys list in alphabetical order
letters_list =[i for i in letters_dict.keys()]
letters_list.sort()

# print the histogram
for i in letters_list:
     print(f'{i} -> {letters_dict[i]}')

