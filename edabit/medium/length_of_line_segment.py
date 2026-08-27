"""
Write a function that takes coordinates of two points on a two-dimensional plane and returns the length of the line segment connecting those two points.

Examples
line_length([15, 7], [22, 11]) ➞ 8.06

line_length([0, 0], [0, 0]) ➞ 0

line_length([0, 0], [1, 1]) ➞ 1.41
"""


def line_length(point1, point2):
    ret = (((point1[0] - point2[0]))**2 + ((point1[1] - point2[1])**2))**(1/2)
    return round(ret, 2)

print(line_length([15, 7], [22, 11]))
print(line_length([0, 0], [0, 0]))
print(line_length([0, 0], [1, 1]))
