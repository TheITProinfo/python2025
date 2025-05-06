# coding:utf-8
# this is a example with as in python
file_name = "example.txt"
with open(file_name, "w+") as f:  # open file in write mode
    f.write("This is a example file.\n")
    f.write("This file is created by python.\n")
    f.write("This file is for testing purpose only.\n") 

with open(file_name, "r") as f: # oprn file in read mode
    content = f.read()
    print(content)
