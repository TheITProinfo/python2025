# coding: utf-8
# this is a example for copyine a file to new file in python
# this is exam file for python code 2025
old_filename=r'd:\code\pythoncode\python_code2025\day9\example.txt' # absolute path of old file
with open(old_filename, 'r', encoding='utf-8') as old_file:
    lines=old_file.readlines()
    new_filename=r'd:\code\pythoncode\python_code2025\day9\new_example.txt' # absolute path of new file
    with open(new_filename, 'w', encoding='utf-8') as new_file:
        new_file.writelines(lines)
        print('File copied successfully')
