# WEEKDAY COUNTER of a GIVEN YEAR
# This program asks the user to insert an year and a weekday.
# It will calculate how many weehdays there are in the given year
# By Alessandro Silvestri, assignement solved for Python Institute

import calendar

class MyCalendar(calendar.Calendar):
     
     def count_weekday_in_year(self, year, weekday):
          if weekday not in range(7):
               return 'error: weekday has to be between 0 and 6'
          day_result = 0
          for y in range(1, 13):
               for i in cal.monthdays2calendar(year, y):
                    for j in i:
                         if j[1] == weekday and j[0] != 0:
                              day_result +=1
          return day_result


days_list = calendar.weekheader(9).split()
print('\nYEAR WEEKDAY COUNTER')
year = input('Insert the year: ')

print('\nChoose the weekday:')
for i in range(7):
     print(f'{i} for {days_list[i]}')

day = input('\n>: ')
cal = MyCalendar()

try:
     day = int(day)
     year = int(year)
     if day in range(7) and year in range(1, 9999):
          print(f'{cal.count_weekday_in_year(year, day)} {days_list[day]} in {year}')
     else:
          print('Input Error')
except:
     print('Input Error')

