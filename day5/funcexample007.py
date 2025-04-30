# coding: utf-8
# this is a example of function in python
data_list = [1, 2, 3, 4, 5]
filtered_list =filter(lambda x : x >=2, data_list)
print(list(filtered_list))

mapped_list = map(lambda x : x*2, data_list)
print(list(mapped_list))    
