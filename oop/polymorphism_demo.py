class Shape:
    def __init__(self):
        pass

    def area(self ):
        raise NotImplementedError ("error")
class Rectangle(Shape):
    def __init__(self, lenght, width):
        super().__init__(self)
        self.lenght = lenght
        self.width = width

    def area():
        return f"Area = {self.length * self.width}"  
    
class Circle(Shape):
    pi = 3.412
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)
