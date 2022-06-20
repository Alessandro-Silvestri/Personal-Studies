# CAESAR CIPHER ENCRYPTION
# This program encrypts a given string by the user following the Caesar Cipher encryption rules
# By Alessandro Silvestri, assignement solved for Python Institute

# function for shifting the code point. (in limit and start I'll put the cod point of 'z', 'Z' and 'a', 'A' 
def lower_code_shift(letter, shift, limit, start):
	code = ord(letter)
	for i in range(shift):
		if code == limit:
			code = start
		code += 1
	return code


txt = input('insert a string: ')

# I ask a string and a number, I check if the number is between 1 and 25 and if he doesn't put a number
while True:
	try:
		shift = int(input('insert a shift number between 1 and 25: '))
		if shift not in range(1, 26):
			print(f'{shift} is not valid')
		else:
			break
	except:
		print('Error: a number is required')

# I inizialize the container variables
code = 0
encryptetd_word = ''

# I hiterate the string
for j in txt:
	# part of code if the character is lowercase
	if j.islower() or not j.isalnum() or j.isnumeric():
		if j.isalpha():
			encryptetd_word += chr(lower_code_shift(j, shift, 122, 96))
		else:
			encryptetd_word += j

	# part of code if the character is upper		
	elif j.isupper() or not j.isalnum() or j.isnumeric():
		if j.isalpha():
			encryptetd_word += chr(lower_code_shift(j, shift, 90, 64))
		else:
			encryptetd_word += j


print(encryptetd_word)


