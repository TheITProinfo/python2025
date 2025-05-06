# coding: utf-8
# this is a example code for datetime module in python
import datetime
d1=datetime.datetime.today()
print('Today is:{}'.format(d1))
d2=d1.strftime('%Y-%m-%d')
print('Today is:{}'.format(d2))
d3=datetime.datetime.strftime(d1,'%Y-%m-%d %H:%M:%S')
print(' d3 Today is:{}'.format(d3))

str_d4='2025-02-22 19:34:05'
d4=datetime.datetime.strptime(str_d4,'%Y-%m-%d %H:%M:%S')
print(' d4 is:{}'.format(d4))

