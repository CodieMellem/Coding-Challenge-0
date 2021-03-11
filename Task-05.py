import math

def area_of_triangle(length_one, length_two, length_three):
    perimeter = (length_one + length_two + length_three)/2
    area = math.sqrt(perimeter * (perimeter - length_one) * (perimeter - length_two) * (perimeter - length_three))
    return area


print(round(area_of_triangle(50, 40, 36), 4))
