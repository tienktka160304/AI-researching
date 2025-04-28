class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Cat(Animal):   #ke thua - inheritance
    def speak(self):
        return f"{self.name} says Meow"

class Dog(Animal):   #ke thua - inheritance
    def speak(self):
        return f"{self.name} says Woof"
    
cat = Cat("tom")
dog = Dog("max")

print(cat.speak())  #tom says Meow
print(dog.speak())  #max says Woof