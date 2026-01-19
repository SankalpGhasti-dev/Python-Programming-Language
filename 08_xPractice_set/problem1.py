
def greatest():
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c


a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

greatest()

print(f"Greatest number of three numbers {a}, {b}, {c} is {greatest()}.")

