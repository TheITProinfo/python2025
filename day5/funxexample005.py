# coding: utf-8
# this is a example of function in python
def f1(x):
    return x**2
data_list=[1,2,3,4,5]
mapped_list=list(map(f1,data_list))
print(mapped_list)