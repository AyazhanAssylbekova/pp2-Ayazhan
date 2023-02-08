import random
def myfunc():
    b=input("Hello! What is your name?\n")
    print("Well, "+b+", I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    x=random.randrange(1,20)
    i=0
    while True:
        i+=1
        a=int(input())
        if a<x:
            print("Your guess is too low.")
            print("Take a guess.")
        elif a>x:
            print("Your guess is too more.")
            print("Take a guess.")
        elif a==x:
            print("Good job, "+b+" You guessed my number in "+str(i)+" guesses!")

myfunc()
