# coding: utf-8
# this is a example of function in python
def f1(x):
    return x>50
def f2(x):
    return x<50

data_list=[10,20,30,40,50,60,70,80,90,100]
filtered_list=list(filter(f2,data_list)) # using filter function to filter the data_list based on f1 function
print(filtered_list)
