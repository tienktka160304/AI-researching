class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print(f"{self.name} says: Woof!")
    
    def get_into(self):
        return f"{self.name} is {self.age} years old"
    
dog = Dog("Bull", 2)
dog.bark()
print(dog.get_into())
# Bull says: Woof!
# Bull is 2 years old