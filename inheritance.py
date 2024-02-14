# base class or super class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"
    
# derived class or sub class
class Dog(Animal):
    def speak(self):
        return "woof!"
    
class Cat(Animal):
    def speak(self):
        return "meow!"