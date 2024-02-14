class Bird:
    def speak(self):
        return "chirp"

class Dog:
    def speak(self):
        return "woof!"

# A common interface 
def animal_sound(animal):
    print(animal.speak())

