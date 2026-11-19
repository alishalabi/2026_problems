"""
"Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower one by one, saying the phrase "Loves me" and "Loves me not" when determining whether the one that they love, loves them back.

Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases.

Examples
loves_me(3) ➞ "Loves me, Loves me not, LOVES ME"

loves_me(6) ➞ "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"

loves_me(1) ➞ "LOVES ME"
"""

def loves_me(num):
    phrase1 = "Loves me"
    phrase2 = "Loves me not"
    ret = ""
    counter = 0

    # Special case: length == 1 -> no commas
    if num == 1:
        return phrase1.upper()

    while counter < (num - 1):
        if counter % 2 == 0:
            ret += phrase1 + ", "
        else:
            ret += phrase2 + ", "
        counter += 1
    if counter % 2 == 0:
        ret += phrase1.upper()
    else:
        ret += phrase2.upper()
    return ret

print(loves_me(3))
print(loves_me(6))
print(loves_me(1))
