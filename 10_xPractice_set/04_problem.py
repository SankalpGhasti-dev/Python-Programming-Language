class Calculator:
    print("This is an Calculator.")

    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"squre is {self.n* self.n}. ")

    def cube(self):
        print(f"cube is {self.n * self.n * self.n}.")

    def Square_root(self):
        print(f"Square root is {self.n**1/2}.")
    
    @staticmethod
    def greet():
        print("Hello !!")

a = Calculator(9)

a.greet()
a.square()
a.cube()
a.Square_root()
