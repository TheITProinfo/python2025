 # coding: utf-8 
# define a parent class Animal 
class Animal: 
    def __init__(self, name):  # default constructor  method 
        self.name = name 
    def show_info(self):
        return "I am an animal and my name is {}".format(self.name)
    def run(self):
        return "I am running"

#defining a child class Dog which inherits from the parent class Animal 
class Dog(Animal): 
    def __init__(self, name,age):  # constructor method with additional parameter name 
        super().__init__(name)  # calling the parent class constructor 
        self.age=age 

dog1=Dog("Rufus",3)  # creating an object of Dog class 
dog1.show_info()  # calling the show_info method of the parent class 
dog1.run()  # calling the run method of the child class 
print(dog1.age)  # accessing the age attribute of the Dog object
print(dog1.show_info())  # calling the show_info method of the Dog object
print(dog1.run())  # calling the run method of the Dog object

