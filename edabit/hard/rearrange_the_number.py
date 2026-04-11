"""
Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits are rearranged.

Examples
rearranged_difference(972882) ➞ 760833
# 988722 - 227889 = 760833

rearranged_difference(3320707) ➞ 7709823
# 7733200 - 23377 = 7709823

rearranged_difference(90010) ➞ 90981
# 91000 - 19 = 90981
"""

def rearranged_difference(number):
    min_number_split = sorted(str(number))
    min_number = int("".join(min_number_split))
    max_number_split = sorted(str(number), reverse=True)
    max_number = int("".join(max_number_split))
    ret = max_number - min_number
    return ret


print(rearranged_difference(972882))
print(rearranged_difference(3320707))
print(rearranged_difference(90010))
