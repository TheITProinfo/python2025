# coding: utf-8
# this is a example code for datetime module in python
import datetime
d1=datetime.datetime.now()
print('Current date and time:{0}'.format(d1))
d2=datetime.datetime.today()
print('Current date:{0}'.format(d2))

# -------------timedelta example-
print('-'*50)
print('timedelta example')
d3=datetime.datetime.now()
d4=d3+datetime.timedelta(days=10) # adding 10 days to current date and time
print('10 days after current date and time:{0}'.format(d4))
d5=d3-datetime.timedelta(weeks=10) # subtracting    10 weeks from current date and time
print('10 weeks before current date and time:{0}'.format(d5))

