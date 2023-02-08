class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        depos = float(input())
        self.balance += depos
        print(depos)

    def withdraw(self):
        sum = float(input())
        if self.balance >= sum:
            self.balance -= sum
            print(sum)
        else:
            print("Insufficient balance ")

    def display(self):
        print("\n Net Available Balance=", self.balance)


s = Account()
s.deposit()
s.withdraw()
s.display()