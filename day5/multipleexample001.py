# -*- coding: UTF-8 -*-
 
# Filename : test.py
# author by : Eric
 
# multiplication Table
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()