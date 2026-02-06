class employee:
    def __init__(self):
        print("constructor of employee.")
    a = 1

class Programmer(employee):
    def __init__(self):
        print("constructor of programmer.")
    b = 2

class manager(Programmer):
    def __init__(self):
        super().__init__()
        print("constructor of manager.")
    c = 3

o = manager()

print(o.a, o.b, o.c)

# super function is basically used to call the constructor of parent class in child class.
