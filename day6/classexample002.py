# coding: utf-8
# this is a example of class in python
# define a class named Account
class Account:      
    interest_rate = 3.75 # class variable
    def __init__(self, account_name, amount):
        self.accout_name = account_name
        self.amount = amount

account1=Account("Tony",10000.0)
print('account_name:{0}'.format(account1.accout_name))
print('the account amount is:{0}'.format(account1.amount)) # call the instance variable amount with instance name
print('the interest rate is:{0}'.format(Account.interest_rate)) # call the class variable interest_rate with class name

# create an instance of the Account class