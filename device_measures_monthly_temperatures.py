'''
Device for calculate the average of the temperatures in a month
every hour there is a measurement
Solved by Alessandro Silvestri for Python Institute
'''

# I create an empty matrix list (bidimensional list)
temps = [[0.0 for i in range(24)] for j in range(31)]

# I fill the matrix with measurements at 12.00 pm
for t in range(31):
    temps[t][11] = t

# it calculates the average of the measurements at 12.00 pm
total = 0
for i in range(31):
      total += temps[i][11]
average = total/31

# it prints the whole matrix
for i in temps:
    print(i)
print(f'Average 12.00 of every day: {average}')

# it calculates the highest value about the whole month
highest = -100
for day in temps:
    for hour in day:
        if hour > highest:
            highest = hour
print('the highest value is', highest)


# Also it works in this way (using the indexes):
# highest = -100
# for j in range(24):
#     for i in range(31):
#         if temps[i][j] > highest:
#             highest = temps[i][j]
# print(f'Highest: {highest}')

# it counts all the days that at 12.00 pm were more than 20 degrees
hotdays = 0
for day in temps:   # in this case day is the list
    if day[11] > 20:
        hotdays += 1
print(hotdays)

# # Also it works in this way (using the indexes):
# hotdays = 0
# for i in range(31):
#     if temps[i][11] > 20:
#         hotdays += 1
# print(hotdays, 'Days were really warm')

