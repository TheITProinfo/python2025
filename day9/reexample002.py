# coding: utf-8
# this is a example of regular expression in python -string substitution
# pattern = r"\d+"
import re
string1='AB12CD34EF56'
pattern = r"\d+"
new_string = re.sub(pattern, " ", string1)
print('the new string after substitution is:', new_string)
new_string1=re.sub(r'\d+',' ',string1,count=1)
print('the new string after substitution one time is:', new_string1)
