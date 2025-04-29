# coding: utf-8
# this is a example of dictionary in python
dict1=dict((('name','John'),('age',25),('city','New York'))) # creating a dictionary with tuple
print(dict1)
dict2=dict([('name','John'),('age',25),('city','New York')]) # creating a dictionary with list
print(dict2)
dict3=dict(zip(['name','age','city'],['John',25,'New York'])) # creating a dictionary with zip function

print(dict3)
print(dict3['name'])
print('age=',dict3['age']) # get method to get the value of key
dict3.pop('age')
print(dict3) # pop method to remove the key-value pair


