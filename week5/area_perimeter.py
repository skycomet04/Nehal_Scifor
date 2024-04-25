from abc import *
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class circle(shape):
    def __init__(self):
        self.radius=float(input("Enter radius "))
    def area(self):
        self.area_shape=3.14*(self.radius**2)
        print(f"Circle area is {self.area_shape}")
    
    def perimeter(self):
        self.peri=2*22/7*self.radius
        print(f"perimeter is {self.peri}")
class rectangle(shape):
    def __init__(self):
        self.length=float(input("Enter length "))
        self.breadth=float(input("Enter breadth "))
    def area(self):
        self.area_shape=self.length*self.breadth
        print(f"Rectangle area is {self.area_shape}")
    
    def perimeter(self):
        self.peri=2*(self.length+self.breadth)
        print(f"perimeter is {self.peri}")
class square(shape):
    def __init__(self):
        self.side=float(input("Enter side length "))
    def area(self):
        self.area_shape=self.side*self.side
        print(f"Square area is {self.area_shape}")
    
    def perimeter(self):
        self.peri=4*self.side
        print(f"perimeter is {self.peri}")    
class triangle(shape):
    def __init__(self):
        self.base=float(input("Enter base length "))
        self.a=float(input("Enter first side length"))
        self.c=float(input("Enter third side length"))
        self.height=float(input("Enter height "))
    def area(self):
        self.area_shape=.5*self.base*self.height
        print(f"Triangle area is {self.area_shape}")
    
    def perimeter(self):
        self.peri=self.a+self.base+self.c
        print(f"perimeter is {self.peri}")
c1=circle()
c1.area()
r1=rectangle()
r1.area()
r1.perimeter()
t1=triangle()
t1.perimeter()
t1.area()