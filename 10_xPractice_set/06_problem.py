
from random import randint 

class Train:

    def __init__(slf, train_no):
        slf.train_no = train_no
       

    def book(slf,  fro, to):
        print(f"Your train no. is {slf.train_no} and you are travelling from {fro} to {to}.")

    def getstatus(slf):
        print(f"Train No: {slf.train_no} is running on time.")

    def getfare(slf,  fro, to):
        print(f"Ticket fare in train No. {slf.train_no} from {fro} to {to} is {randint(500, 100000)} Rs.")


t = Train( 543 )

t.book("Delhi", "Mumbai")
t.getstatus()
t.getfare("Delhi", "Mumbai")


# if we put slf or sankalp instead of self it will work fine because it is just a convention to use self as the first parameter in the instance method. we can use any name instead of self but it is recommended to use self for better readability and understanding of the code.

