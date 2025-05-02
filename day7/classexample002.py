# coding: utf-8
# this is a example of class in python
# define a class named Dog
class Dog:
    def __init__(self, name, age,gender='male'):
        self.name = name
        self.__age = age  # private variable
        self.gender = gender
    def bark(self):
        print(f"{self.name} is barking")

    def run(self):
        print(f"{self.name} is running")

    # defing get method for access the private variable __age
    def get_age(self):
        #temp_age=self.__age
        return self.__age
    def set_age(self, age):
        self.__age = age  # private variable can't be accessed directly

# end of Dog class
# ------------------------------------

# create an object of Dog class
dog1=Dog("Rufus", 3, 'male')
# print('dog age is {} '.format(dog1.__age))  # private variable can't be accessed directly
print('dog age is {} '.format(dog1.get_age()))  # accessing private variable using get method
dog1.bark()
dog1.set_age(10)  # setting private variable using set method
print('dog age is set to {} '.format(dog1.get_age()))  # private variable can't be accessed directly