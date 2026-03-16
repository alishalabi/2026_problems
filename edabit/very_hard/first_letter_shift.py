"""
Given a sentence, create a function which shifts the first letter of each word to the next word in the sentence (shifting right).

Examples
shift_sentence("create a function") ➞ "freate c aunction"

shift_sentence("it should shift the sentence") ➞ "st ihould shift she tentence"

shift_sentence("the output is not very legible") ➞ "lhe tutput os iot nery vegible"

shift_sentence("edabit") ➞ "edabit"
"""

def shift_sentence(sentence):
    ret = ""
    sentence_array = sentence.split(" ")
    if len(sentence_array) == 1:
        return sentence
    for i in range(len(sentence_array) - 1):
        first_letter = sentence_array[i+1][0]
        ret += first_letter + sentence_array[i][1:] + " "
    last_word = sentence_array[0][0] + sentence_array[-1][1:]
    ret += last_word
    return ret

print(shift_sentence("create a function"))
print(shift_sentence("edabit"))


# WIP! shifting wrong direction
