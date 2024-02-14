class Bird:
    def speak(self):
        return "chirp"

class Dog:
    def speak(self):
        return "woof!"

# A common interface 
def animal_sound(animal):
    print(animal.speak())

# creating instances of dog and bird
dog = Dog()
bird = Bird()

# passing the instances
animal_sound(dog)
animal_sound(bird)