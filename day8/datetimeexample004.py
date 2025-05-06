# coding: utf-8
# this is a example code for datetime module in python

import datetime
d1=datetime.date(2025,5,1)
d2=datetime.date(2025,5,31)
delta=d2-d1
d4=datetime.date.fromtimestamp(1621510400)

d5=datetime.date.fromtimestamp(1746227353) # timestamp for May 1, 2025 12:00:00 AM
print('d1 is {}'.format(d1))
print('d2 is {}'.format(d2))
print('delta is {}'.format(delta))  
print('d4 is {}'.format(d4))
print('d5 is {}'.format(d5))