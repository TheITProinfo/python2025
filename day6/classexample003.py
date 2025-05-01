# coding: utf-8
# this is a example of class in python
class Account:
    interest_rate = 4.05  # class variable
    # default constructor
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    # define class method
    @classmethod
    def get_interest_rate(cls,amt):
        return cls.interest_rate * amt
    # ppp 
interest=Account.get_interest_rate(12000.0)
print('the total interest is:{0:.2f}'.format(interest))
