"""
Given a name, return the letter with the highest index in alphabetical order, with its corresponding index, in the form of a string. You are prohibited to use max() nor is reassigning a value to the alphabet list allowed.

Examples
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


alphabet_index(alphabet, "Flavio") ➞ "22v"

alphabet_index(alphabet, "Andrey") ➞ "25y"

alphabet_index(alphabet, "Oscar") ➞ "19s"
"""

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def alphabet_index(alphabet, string):
    highest = string[0].lower()
    for letter in string[1:]:
        if alphabet.index(letter.lower()) > alphabet.index(highest):
            highest = letter.lower()
    return str(alphabet.index(highest) + 1) + str(highest)

print(alphabet_index(alphabet, "Flavio"))
print(alphabet_index(alphabet, "Andrey"))
print(alphabet_index(alphabet, "Oscar"))
