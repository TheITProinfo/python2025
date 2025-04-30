# coding: utf-8
# this is a example of function in python
def rectangle_area(length, width):
    area = length * width
    return area
def print_area(length, width):
    area = rectangle_area(length, width)
    print("the lenghth is {0} and the width is {1} and the area is {2}".format(length, width, area))
# calling the function
print_area(5, 10) # output: the lenghth is 5 and the width is 10 and the area is 50
# calling the function
# print(rectangle_area(5, 10)) # output: 50
print_area(10, 5) # output: the lenghth is 10 and the width is 5 and the area is 50