"""
Write a function that inverts the keys and values of a dictionary.

Examples
invert({ "z": "q", "w": "f" })
➞ { "q": "z", "f": "w" }

invert({ "a": 1, "b": 2, "c": 3 })
➞ { 1: "a", 2: "b", 3: "c" }

invert({ "zebra": "koala", "horse": "camel" })
➞ { "koala": "zebra", "camel": "horse" }
"""

def invert(dict):
    ret = {}
    for item in dict:
        ret[dict[item]] = item
    return ret

print(invert({ "z": "q", "w": "f" }))
print(invert({ "a": 1, "b": 2, "c": 3 }))
print(invert({ "zebra": "koala", "horse": "camel" }))
