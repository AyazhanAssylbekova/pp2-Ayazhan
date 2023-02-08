class rectangle():
    def __init__(self):
        len = float(input())
        wid = float(input())
        self.length = len
        self.width = wid

    def area(self):
        print(self.length*self.width)


nrectangle = rectangle()
nrectangle.area()