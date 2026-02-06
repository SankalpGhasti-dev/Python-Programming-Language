
from random import randint 

class Train:

    def __init__(self, train_no):
        self.train_no = train_no
       

    def book(self,  fro, to):
        print(f"Your train no. is {self.train_no} and you are travelling from {fro} to {to}.")

    def getstatus(self):
        print(f"Train No: {self.train_no} is running on time.")

    def getfare(self,  fro, to):
        print(f"Ticket fare in train No. {self.train_no} from {fro} to {to} is {randint(500, 100000)} Rs.")


t = Train( 543 )

t.book("Delhi", "Mumbai")
t.getstatus()
t.getfare("Delhi", "Mumbai")

