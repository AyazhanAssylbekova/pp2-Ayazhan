class getstring:
    def __init__(self):
        self.s1 = ""

    def get_string(self):
        self.s1 = input()

    def print_string(self):
        print(self.s1.upper())

s1 = getstring()
s1.get_string()
s1.print_string()

