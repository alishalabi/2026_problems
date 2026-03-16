"""
Create a function that counts the number of digits in a number. Conversion of the number to a string is not allowed.

Examples
digits_count(4666) ➞ 4

digits_count(544) ➞ 3

digits_count(121317) ➞ 6

digits_count(0) ➞ 1

digits_count(12345) ➞ 5

digits_count(1289396387328) ➞ 13
"""

def digits_count(number):
    if number == 0:
        return 1
    count = 0
    while number // 10**count > 0:
        count +=1
    return count


print(digits_count(4666))
print(digits_count(544))
print(digits_count(121317))
print(digits_count(0))
print(digits_count(12345))
print(digits_count(1289396387328))
