from math import *
class Point():
    def __init__(self):
        x = float(input())
        y = float(input())
        ptx = int(input())
        pty = int(input())
        self.pty = pty
        self.ptx = ptx
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self):
         self.x += self.x
         self.y += self.y
         print(self.x, self.y)

    def dist(self):
        dx = self.ptx - self.x
        dy = self.pty - self.y
        print(sqrt(dx ** 2 + dy ** 2))

nPoi = Point()
nPoi.show()
nPoi.move()
nPoi.dist()