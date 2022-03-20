from math import acos, sqrt
from copy import deepcopy

def dot_product(vec1, vec2):
    return (vec1.x * vec2.x) + (vec1.y * vec2.y)

def calculate_magnitude(vec1):
    return sqrt((vec1.x)**2 + (vec1.y)**2)

def relative_coords(vec1, vec2):
    v1 = deepcopy(vec1)
    v1.x = vec1.x - vec2.x
    v1.y = vec1.y - vec2.y
    return v1

def calculate_angle(vec1, intersection, vec2):
    v1 = relative_coords(vec1, intersection)
    v2 = relative_coords(vec2, intersection)
    return acos((dot_product(v1, v2)) / (calculate_magnitude(v1) * calculate_magnitude(v2)))
