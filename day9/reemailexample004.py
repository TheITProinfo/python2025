# coding: utf-8
# this is a example code for validating email address in python
# reference url
# https://houbb.github.io/2022/02/18/safe-01-encryption-email

import re

pattern1 = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' # email pattern created by AI
# paaater1=r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'
email = input("Enter email address: ")

if re.match(pattern1, email):
    print("Valid email address")
else:
    print("Invalid email address")
