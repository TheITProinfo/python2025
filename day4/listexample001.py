# coding: utf-8

# list example
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3=['welcome', 'to', 'python', 'code', '2025',100,200,300,400,500]

print(list1.append(6)) # add 6 at the end of the list
list1.extend(list2) # add list2 elements at the end of list1
print(list1)
list3.insert(2, 'CSTcollege') # insert 'CSTcollege' at index 2 in list3
print(list3)

# print(list3.count('to')) # count the number of times 'to' appears in list3
# print(list3.index('python')) # find the index of 'python' in list3
