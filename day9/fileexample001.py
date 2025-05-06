# coding: utf-8

# This is a sample Python code.
file1=open("fileexample001.txt","w+")
file1.write("This is a sample Python code.")
print('File written successfully.')
file1.close()
file2=open("fileexample001.txt","r+")
file2.write("Welcome to Python programming .")
print('File updated successfully.')
file2.close()
file3=open("fileexample001.txt","a")
print(file3.write("Thank you for using Python programming."))
print('File appended successfully.')
file3.close()

