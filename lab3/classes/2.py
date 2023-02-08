from math import *
class shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class square(shape):
    def __init__(self):
        n = int(input())
        shape.__init__(self)
        self.length = n

    def area(self):
        return self.length * self.length

asquare = square()
print(asquare.area())