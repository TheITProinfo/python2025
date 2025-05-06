# coding: utf-8
# this is a example of regular expression in python
import re

# define a pattern to match a string with a date in the format of 
p=pattern = r'\w+@cstcollege.ca'
email1='ericji@cstcollege.ca'
m=re.match(p,email1)
if m:
    print("Match found")
else:
    print("Match not found")