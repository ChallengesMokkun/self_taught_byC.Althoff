# 1
class Apple:
    def __init__(self,l,c,s,b):
        self.loc = l
        self.color = c
        self.size = s
        self.blix = b
        print("An apple appended!")

App1 = Apple("Aomori","scarlet","M","18")
App2 = Apple("Nagano","yellow red","L","17")
print(App1.loc)
print(App2.loc)

# 2
import math
class Circle:
    def __init__(self,r):
        self.radius = r
        print("Input a circle!")

    def area(self):
        return self.radius ** 2 * math.pi

cir1 = Circle(3)
print(cir1.area())

# 3
class Triangle:
    def __init__(self,b,h):
        self.bottom = b
        self.height = h
        print("Input a triangle!")

    def area(self):
        return self.bottom * self.height / 2

tri1 = Triangle(12,6)
print(tri1.area())

# 4
class Hexagon:
    def __init__(self,a,b,c,d,e,f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        print("Input a hexagon!")

    def calculate_perimeter(self):
        return self.a + self.b + self.c + self.d + self.e + self.f

hex1 = Hexagon(3,5,6,4,8,9)
print(hex1.calculate_perimeter())
