# coding: utf-8
# this is a example of regular expression in python -string split
import re
patter1=r'\d+'
string1='AB12CD34EF'
result1=re.split(patter1,string1)
print('the result of re.split(r"\d+", "AB12CD34EF") is:',result1)
result2=re.split(patter1,string1,1)
print('the result of re.split(r"\d+", "AB12CD34EF",1) is:',result2)