# this language does not have interface -> use ABC to simulate :
from abc import ABC, abstractmethod

class Drawable(ABC):    #define interface <real is ABC>
    @abstractmethod
    def draw(self):
        pass
    
class Resizable(ABC):
    @abstractmethod
    def resize(self, factor):
        pass
    
class Circle(Drawable, Resizable):
    def __init__(self, radius):
        self.radius = radius
        
    def draw(self):
        print(f"drawing circle : {self.radius}")
        
    def resize(self, factor):
        self.radius *= factor
        print(f"Cicle resized, new readius : {self.radius}")
        
class Square(Drawable, Resizable):
    def __init__(self, side):
        self.side = side
    
    def draw(self):
        print(f"drawing square : {self.side}")
        
    def resize(self, factor):
        self.side *= factor
        print(f"Square resized. newside = {self.side}")
        
def draw_shape(shape : Drawable):
    shape.draw()

def resize_shape(shape: Resizable, factor):
    shape.resize(factor)
    
circle = Circle(5)
square = Square(4)

draw_shape(circle)
resize_shape(circle, 2)


draw_shape(square)
resize_shape(square, 2.5)