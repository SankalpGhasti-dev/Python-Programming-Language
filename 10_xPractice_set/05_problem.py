
from random import randint 

class Train:

    def __init__(self, train_no, fro, to):
        self.book
        self.getstatus
        self.getfare

    def book(self, train_no, fro, to):
        print(f"Your train no. is {train_no} and you are travelling from {fro} to {to}.")

    def getstatus(self, train_no, fro, to):
        pass

    def getfare(self, train_no, fro, to):
        print(f"Ticket fare in train No. {train_no} from {fro} to {to} is {randint(500, 100000)} Rs.")


t = Train( 543 , "Delhi", "Mumbai")

t.book()
t.getstatus()
t.getfare()

print(t.book, t.getstatus, t.getfare)


