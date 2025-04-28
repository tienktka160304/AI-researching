class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"

class Dog(Animal):
    def speak(self):
        return f"{self.name} say Woof"

def animal_sound(animal):
    print(animal.speak())
    
dog = Dog("max")

animal_sound(dog)
#max say Woof