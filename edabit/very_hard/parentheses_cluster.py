"""
Write a function that groups a string into parentheses clusters. Each cluster should be balanced.

Examples
split("()()()") ➞ ["()", "()", "()"]

split("((()))") ➞ ["((()))"]

split("((()))(())()()(()())") ➞ ["((()))", "(())", "()", "()", "(()())"]

split("((())())(()(()()))") ➞ ["((())())", "(()(()()))"]
Notes
All input strings will only contain parentheses.
Balanced: Every opening parens ( must exist with its matching closing parens ) in the same cluster.
"""

# Original method
# def split(string):
#     ret = []
#     current_index = 0
#     count = 0
#     while (current_index + count) < len(string):
#         # One-off case
#         if string[current_index + 1] == ")":
#                 cluster = str(string[current_index:current_index + 2])
#                 ret.append(cluster)
#                 current_index += 2
#         elif string[current_index + count] == ")":
#             target_index = current_index + (2* count) + 1 #Switching shift breaks one of last 2 inputs
#             cluster = str(string[current_index:target_index])
#             ret.append(cluster)
#             current_index = target_index + 1
#             count = 0
#         else:
#             count += 1
#     return ret

# Method inspirted by Carl Kristensen (edabit user)
def split(string):
    score = 0
    current_index = 0
    ret = []
    for i in range(len(string)):
        if string[i] == "(":
            score += 1
        else:
            score -= 1
        # print(score)
        if score == 0:
            cluster = string[current_index:i + 1]
            ret.append(cluster)
            current_index = i + 1
    return ret

print(split("()()()"))
print(split("((()))"))
print(split("((()))(())()()(()())"))
print(split("((())())(()(()()))"))
