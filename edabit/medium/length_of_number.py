"""
Create a function that takes a number num and returns its length.

Examples
number_length(10) ➞ 2

number_length(5000) ➞ 4

number_length(0) ➞ 1
Notes
The use of the len() function is prohibited.
"""

def number_length(num):
    length = 1
    while (num//(10**length)) >= 1:
        length += 1
    return length


print(number_length(10))
print(number_length(5000))
print(number_length(0))
