"""
Given the month and year as numbers, return whether that month contains a Friday 13th.

Examples
has_friday_13(3, 2020) ➞ True

has_friday_13(10, 2017) ➞ True

has_friday_13(1, 1985) ➞ False
Notes
January will be given as 1, February as 2, etc ...
"""
import datetime

def has_friday_13(month, year):
    my_date = datetime.datetime(year, month, 13)
    weekday = my_date.strftime("%a")
    if weekday == "Fri":
        return True
    else:
        return False

print(has_friday_13(3, 2020))
print(has_friday_13(10, 2017))
print(has_friday_13(1, 1985))
