# coding: utf-8
# this is a example of function in python
def calcu(opr):
    if opr == '+':
        return lambda x,y: x+y  # return a lambda function
    elif opr == '-':
        return lambda x,y: x-y
    
f1=calcu('+')
print(f1(2,3))  # output: 5
f2=calcu('-')
print(f2(5,3))  # output: 2
