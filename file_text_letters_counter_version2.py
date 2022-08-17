# TEXT FILE LETTERS COUNTER Version 2
# the result will be saved in a different file adding .hist extension
# and will be sorted from most frequent letter from the less one
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

# creating a list tuples (key, value)
letters_list = list(letters_dict.items())

# creating a inverted tuples list (value, key)
letters_list_new_ordered = []
for i in letters_list:
    letters_list_new_ordered.append((i[1], i[0]))

# sorting from the highest
letters_list_new_ordered.sort(reverse=True)

# creating the content
content = ''
for i in letters_list_new_ordered:
    content += f'{i[1]} -> {i[0]}\n'

# writing the content
writer = open(input_file_name + '.hist', 'w')
writer.write(content)
writer.close()

