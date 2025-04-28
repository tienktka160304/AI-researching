class animal:
    def __init__(self, name, age, say, kind):
        self.name = name
        self.age = age
        self.say = say
        self.kind = kind 
        
    def says(self):
        print(f"{self.name} says: {self.say}!")
    
    def get_into(self):
        return f"{self.name} is a {self.kind} {self.age} years old"
    
Cat = animal('tom', 2, 'Meow', "cat")
Dog = animal('max', 3, "Woof", "dog")

print(Cat.get_into())
print(Dog.get_into())

Cat.says()
Dog.says()

# tom is a cat 2 years old
# max is a dog 3 years old
# tom says: Meow!
# max says: Woof!