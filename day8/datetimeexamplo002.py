# coding: utf-8
# this is a example code for datetime module in python
import datetime
d1=datetime.datetime.now()
d2=datetime.datetime(2025,5,2)
d3=datetime.datetime.strptime('2025-05-02','%Y-%m-%d')
print('d1 is {0}'.format(d1))
print('d2 is {0}'.format(d2))
print('d2-d1 is {0}'.format(d2-d1))
print('d3 is {0}'.format(d3))
