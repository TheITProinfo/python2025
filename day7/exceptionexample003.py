# coding: utf-8 
# this is a example of exception handling in python 
num1=input("Enter first number: ")
num2=999
try:
    result=num2/int(num1)
    print("Result is:",result)
    print("{0} device {1}, the result is {2}".format("num1", "num2", result))
# except ZeroDivisionError:
#     print("Error: division by zero")
except (ZeroDivisionError, ValueError) as e: # multiple exception handling
    print("Error message:{}".format(e))
finally:
    print("Finally block executed, the resource is released")