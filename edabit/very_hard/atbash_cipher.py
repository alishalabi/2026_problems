"""
The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.

Create a function that takes a string and applies the Atbash cipher to it.

Examples
atbash("apple") ➞ "zkkov"

atbash("Hello world!") ➞ "Svool dliow!"

atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"

Notes
Capitalisation should be retained.
Non-alphabetic characters should not be altered.
"""

lower_cipher = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def atbash(sentence):
    ret = ""
    for letter in sentence:
        if letter in lower_cipher:
            index = lower_cipher.index(letter)
            ret += lower_cipher[25-index]
        elif letter.lower() in lower_cipher:
            index = lower_cipher.index(letter.lower())
            ret += lower_cipher[25-index].upper()
        else:
            ret += letter
    return ret

print(atbash("apple"))
print(atbash("Hello world!"))
print(atbash("Christmas is the 25th of December"))
