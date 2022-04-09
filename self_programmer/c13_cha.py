# 3
class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape")

# 1, 2
class Rectangle(Shape):
    def __init__(self,w,l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return (self.width + self.length) * 2

class Square(Shape):
    def __init__(self,w):
        self.width = w

    def calculate_perimeter(self):
        return self.width * 4

    def change_size(self,x):
        self.width = self.width + x

rec1 = Rectangle(12,4)
print(rec1.calculate_perimeter())
squ1 = Square(9)
print(squ1.calculate_perimeter())

squ1.change_size(-2)
print(squ1.width)

rec1.what_am_i()
squ1.what_am_i()

# 4
class Horse:
    def __init__(self,n,t,j):
        self.name = n
        self.type = t
        self.jockey = j

class Rider:
    def __init__(self,n):
        self.name = n

Sab = Rider("Saburoh")
Kit = Horse("Kitasan","long distance",Sab)
print(Kit.jockey.name)
