# coding: utf-8
# this is a sample code for class in python
# define a class named Dog
class Dog:
    # define a method named bark
    def bark(self):
        print("Woof!")

# create an object of Dog class
dog1 = Dog()
dog1.name = "Buddy"
dog1.age = 3
dog1.color = "brown"
dog1.gender = "male"

print("Dog name:", dog1.name)
print("Dog age:", dog1.age)
print("Dog color:", dog1.color) 
print("Dog gender:", dog1.gender) 


dog2 = Dog()
dog2.name = "Max"
dog2.age = 5
dog2.color = "black"
dog2.gender = "male"

dog3=Dog()
dog3.name="Buddy"
dog3.age=3
dog3.color="brown"
dog3.gender="male"

print("Dog name:", dog3.name)
print("Dog age:", dog3.age)
print("Dog color:", dog3.color) 
print("Dog gender:", dog3.gender) 

dog1.bark()
dog2.bark()
dog3.bark()


