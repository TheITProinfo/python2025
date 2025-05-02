# coding: utf-8
# this is a example of polymorphism in python

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow!")

class Bird(Animal):
    def speak(self):
        print(f"{self.name} says chirp!")
dog1 = Dog("Buddy")
cat1 = Cat("Whiskers")
bird1 = Bird("Tweety")
print(dog1.speak())
print(cat1.speak())
print(bird1.speak())

