"""
Imagine a circle and two squares: a smaller and a bigger one. For the smaller one, the circle is a circumcircle and for the bigger one, an incircle.


Create a function, that takes an integer (radius of the circle) and returns the difference of the areas of the two squares.

Examples
square_areas_difference(5) ➞ 50

square_areas_difference(6) ➞ 72

"""

def square_areas_difference(radius):
    area_large = (2 * radius)**2
    side_small_square = (((radius**2)/2)**(1/2)) * 2
    area_small = (side_small_square)**2
    ret = area_large - area_small
    return round(ret)

print(square_areas_difference(5))
print(square_areas_difference(6))
