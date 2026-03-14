"""
Create a function that takes a string txt and censors any word from a given list lst. The text removed must be replaced by the given character char.

Examples
censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"

censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")

censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"
"""

def censor_string(message, black_list, censor_tag):
    ret = ""
    black_list_formatted = [s.lower() for s in black_list]
    message_arr = message.split(" ")
    # Sanitize punctuation from last item
    punctuation = message_arr[-1][-1]
    message_arr[-1] = message_arr[-1][:-1]
    for i in range(len(message_arr)):
        if message_arr[i].lower() in black_list_formatted:
            ret += censor_tag * len(message_arr[i])
        else:
            ret += message_arr[i]

        if i < len(message_arr) - 1:
            ret += " "
    # Add punctuation
    ret += punctuation
    return ret

print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))
print(censor_string("The cow jumped over the moon.", ["cow", "over"], "*"))
print(censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*"))
