class employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute is {cls.a}.")

b = employee()
a = 45

b.show()
