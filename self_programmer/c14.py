# 1, 2
class Square:
    square_list = list()
    
    def __init__(self,w):
        self.width = w
        self.square_list.append((self.width,))

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.width,self.width,self.width,self.width)

sq1 = Square(15)
sq2 = Square(6)
sq3 = Square(9)
print(Square.square_list)

print(sq1)

# 3
def s_or_d(x,y):
    print(x is y)

s_or_d("red","red")
s_or_d("blue","green")


