"""
Create a function that takes a number num and returns each place value in the number.

Examples
num_split(39) ➞ [30, 9]

num_split(-434) ➞ [-400, -30, -4]

num_split(100) ➞ [100, 0, 0]
"""

def num_split(original_number):
    number = abs(original_number)
    ret = []
    count = len(str(number)) - 1
    for i in range(len(str(number))):
        value = int(str(number)[i]) * (10**count)
        if original_number < 0:
            ret.append((value * -1))
        else:
            ret.append(value)
        count -= 1
    return ret


print(num_split(39))
print(num_split(-434))
print(num_split(100))
