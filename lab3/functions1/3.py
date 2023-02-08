def solve(numheads, numlegs):
    z=int((l-2*h)/2)
    k=int(h-z)
    print("Number of rabbits:",k)
    print("Number of chickens:",z)

h=int(input("Enter number of heads:"))
l=int(input("Enter number of legs:"))

solve(h,l)