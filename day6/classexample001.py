# coding: utf-8     
# this is a example of class in python
# define a class named Dog
# the class has three instance variables: name, age, and gender
# the class has one instance method: bark
# the class has a constructor method: __init__
class Dog:
    def __init__(self, name, age,gender='male'):  # constructor method
        self.name = name  # instance variable
        self.age = age    # instance variable
        self.gender = gender
    def bark(self):  # instance method
        print(f"{self.name} is barking")
##   
## 
dog1 = Dog("Buddy", 3, "male")  # create an instance of Dog
dog2 = Dog("Max", 5, "female")
dog3 = Dog("Tony", 3)

dog1.bark()  # call the bark method of dog1 
dog2.bark()  # call the bark method of dog2
dog3.bark()  # call the bark method of dog3 
print(dog1.name)  # print the name of dog1
print(dog2.age)   # print the age of dog2
print(dog3.gender)  # print the gender of dog3






