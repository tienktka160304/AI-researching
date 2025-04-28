from abc import ABC, abstractmethod

class Shape(ABC):       # define ABC
    @abstractmethod     #đánh dấu các phương thức trừu tượng mà các lớp con phải triển khai
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width,height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self. height)
    
circle = Circle(5)
print(f"area = {circle.area()}")                    #area = 78.5
print(f"perimeter = {circle.perimeter():.2f}")      #perimeter = 31.40 

rectangle = Rectangle(5, 10)
print(f"area = {rectangle.area()}")                 #area = 50
print(f"perimeter = {rectangle.perimeter()}")       #perimeter = 30
