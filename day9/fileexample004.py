# coding: utf-8
# this is  a example for copying binary file using python
old_file =r'd:\code\pythoncode\python_code2025\day9\cstlogo.png' # old file path
news_file =r'd:\code\pythoncode\python_code2025\day9\newlogo.png' # new file path

with open(old_file, 'rb') as f1:
     b1=f1.read() # read binary data from old file
     with open(news_file, 'wb') as f2:
          f2.write(b1) # write binary data to new file
          print('File copied successfully')
