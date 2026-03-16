"""
Create a function that takes two number strings and returns their sum as a string.

Examples
add("111", "111") ➞ "222"

add("10", "80") ➞ "90"

add("", "20") ➞ "Invalid Operation"


Notes
If any input is "" or None, return "Invalid Operation"
"""

def add(str1, str2):
    if str1 == "":
        return "Invalid Operation"
    if str2 == "":
        return "Invalid Operation"
    if str1 == None:
        return "Invalid Operation"
    if str2 == None:
        return "Invalid Operation"
    ret = 0
    ret += int(str1) + int(str2)
    return str(ret)


print(add("111", "111"))
print(add("10", "80"))
print(add("", "20"))
