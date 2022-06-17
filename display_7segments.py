# 7 SEGMENTS DISPLAY
# This program shows a numbers string like a 7 segments display
# By Alessandro Silvestri, assignement solved for Python Institute

one = [
     [' ', ' ', '#'],
	[' ', ' ', '#'],
	[' ', ' ', '#'],
	[' ', ' ', '#'],
	[' ', ' ', '#'],
]

two = [
	['#', '#', '#'],
	[' ', ' ', '#'],
	['#', '#', '#'],
	['#', ' ', ' '],
	['#', '#', '#'],
]

three = [
	['#', '#', '#'],
	[' ', ' ', '#'],
	['#', '#', '#'],
	[' ', ' ', '#'],
	['#', '#', '#'],
]

four = [
	['#', ' ', '#'],
	['#', ' ', '#'],
	['#', '#', '#'],
	[' ', ' ', '#'],
	[' ', ' ', '#'],
]

five = [
	['#', '#', '#'],
	['#', ' ', ' '],
	['#', '#', '#'],
	[' ', ' ', '#'],
	['#', '#', '#'],
]

six = [
	['#', '#', '#'],
	['#', ' ', ' '],
	['#', '#', '#'],
	['#', ' ', '#'],
	['#', '#', '#'],
]

seven = [
	['#', '#', '#'],
	[' ', ' ', '#'],
	[' ', ' ', '#'],
	[' ', ' ', '#'],
	[' ', ' ', '#'],
]

eight = [
	['#', '#', '#'],
	['#', ' ', '#'],
	['#', '#', '#'],
	['#', ' ', '#'],
	['#', '#', '#'],
]

nine = [
	['#', '#', '#'],
	['#', ' ', '#'],
	['#', '#', '#'],
	[' ', ' ', '#'],
	['#', '#', '#'],
]

zero = [
	['#', '#', '#'],
	['#', ' ', '#'],
	['#', ' ', '#'],
	['#', ' ', '#'],
	['#', '#', '#'],
]


def print_line(num, numline):
      print(num[numline][0] + num[numline][1] + num[numline][2], end='  ')


txt = input('Insert a number: ')
print()

for j in range(5):
	for i in range(len(txt)):
		if txt[i] == '1':
			print_line(one, j)
		elif txt[i] == '2':
			print_line(two, j)
		elif txt[i] == '3':
			print_line(three, j)
		elif txt[i] == '4':
			print_line(four, j)
		elif txt[i] == '5':
			print_line(five, j)
		elif txt[i] == '6':
			print_line(six, j)
		elif txt[i] == '7':
			print_line(seven, j)
		elif txt[i] == '8':
			print_line(eight, j)
		elif txt[i] == '9':
			print_line(nine, j)
		elif txt[i] == '0':
			print_line(zero, j)
	print()

print()