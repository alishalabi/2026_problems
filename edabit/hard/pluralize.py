"""
Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.

Examples
pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }
"""

def pluralize(array):
    histogram = {}
    for item in array:
        if item not in histogram:
            histogram[item] = 1
        else:
            histogram[item] += 1
    ret = set()
    for item in histogram:
        if histogram[item] > 1:
            ret.add(f"{item}s")
        else:
            ret.add(item)
    return ret

print(pluralize(["cow", "pig", "cow", "cow"]))
print(pluralize(["table", "table", "table"]))
print(pluralize(["chair", "pencil", "arm"]))
