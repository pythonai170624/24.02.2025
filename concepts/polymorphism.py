from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Rectangle(Shape):
    def get_area(self):
        return 1 # demo code

class Triangle(Shape):
    def get_area(self):
        return 2 # demo code

class Equal_Sides_Triangle(Triangle):
    def get_area(self):
        return super().get_area() # demo code

def show_area(shape: Shape):
    print(shape.get_area())

show_area(Rectangle())
show_area(Equal_Sides_Triangle())

# a + b -- operator overloading
# __add__