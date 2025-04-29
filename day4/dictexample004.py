# coding: utf-8
# this is a example of dictionary in python

# creating a dictionary
dict1 = {100:'Aclie',200:'Belle',300:'Chloe',400:'Dave'}
print ('each element of the dictionary is:')

for key in dict1.keys():
    print('key=',key)   # printing the keys of the dictionary

for value in dict1.values():
    print('value=',value)   # printing the values of the dictionary

for stu_id,stu_name in dict1.items():
    # print('key=',key,'value=',value)   # printing the key-value pairs of the dictionary
    print('stunent NO:{0}-student Name:{1}'.format(stu_id,stu_name))
    print ('stunent NO:',stu_id,'student Name:',stu_name)   # printing the key-value pairs of the dictionary



