# coding: utf-8 
# this is a example of exception handling in python 
num1=int(input("Enter first number: "))
num2=999
try:
    result=num2/num1
    print("Result is:",result)
    print("{0} device {1}, the result is {2}".format("num1", "num2", result))
# except ZeroDivisionError:
#     print("Error: division by zero")
except Exception as e:
    print("Error message:{}".format(e))