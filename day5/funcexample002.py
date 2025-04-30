# coding: utf-8
# this is a example of function in python
def mkae_coffe(type='latte'):
    return 'Here is your {}.'.format(type)

coffe1=mkae_coffe('espresso')   
print(coffe1)
coffe2=mkae_coffe()   
print(coffe2)