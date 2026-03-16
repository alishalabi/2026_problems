"""
Write a function that returns True if two arrays, when combined, form a consecutive sequence. A consecutive sequence is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.

Examples
consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True

consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False

consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False

consecutive_combo([44, 46], [45]) ➞ True
Notes
The input lists will have unique values.
The input lists can be in any order.
"""


# ***** METHOD 1: Creating A New Array, Sorting Array *****
# def consecutive_combo(arr1, arr2):
#     combined = arr1 + arr2
#     combined.sort()
#     for i in range(1, len(combined)):
#         if combined[i - 1] + 1 != combined[i]:
#             return False
#     return True


# ***** METHOD 2: Seperate Arrays, Using MIN() And A Counter *****
def consecutive_combo(arr1, arr2):
    total_length = len(arr1) + len(arr2)
    counter = 1
    lowest_number = 0
    if min(arr1) < min(arr2):
        lowest_number = min(arr1)
    else:
        lowest_number = min(arr2)
    while counter < (total_length):
        if lowest_number + counter not in arr1 and lowest_number + counter not in arr2:
            return False
        else:
            counter += 1
    return True



print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))
print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))
print(consecutive_combo([44, 46], [45]))
