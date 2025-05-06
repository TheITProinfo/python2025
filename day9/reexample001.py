# coding: utf-8

import re 
patter1=r'Java|java|JAVA'
text='Java is a popular programming language, I like Java and java as well as JAVA'
matches_list=re.findall(patter1,text)
print(matches_list)
