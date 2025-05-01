# coding: utf-8
# this is a example of private variable in python
# defin a class named Account
class Account:
    __interest_rate = 0.05  # private  class variable
    # default constructor
    def __init__(self, owner, balance):
        self.owner = owner  # public variable
        self.__balance = balance  # private instance variable
    

    def describe_account(self):
        print("Account owner:{0},balance {1}, interest{2} ".format(self.owner, self.__balance, self.__interest_rate))

account1 = Account("John", 90000.0)
account1.describe_account()

print('account name {0}'.format(account1.owner))
# print('account balance {0}'.format(account1.__balance))  # this will give an error because __balance is a private variable
print('interest rate {0}'.format(Account.__interest_rate)) # this will give the value of interest rate




        