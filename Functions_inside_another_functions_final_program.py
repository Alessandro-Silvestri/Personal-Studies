# Creating 3 functions and using them in a final program
# Made by Alessandro Silvestri for Python Institute
# Checking if a year is leap
# I calculate the day over the whole year

# I check if a year is leap
def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


# I count the days of every month according leap (or not leap) year. I use the is_year_leap() function
def days_in_month(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    # I count the days
    elif month == 2 and is_year_leap(year):
        return 29
    elif month == 2:
        return 28


# I count the day over the whole yaer. I use the days_in_month() function
def day_year(year, month, day):
    count = 0
    if month == 1:
        return day
    for i in range(1, month):
            count += days_in_month(year, i)
    return count + day


# final program
year = int(input('insert year: '))
month = int(input('insert month: '))
day = int(input('insert day: '))

print(day_year(year, month, day))