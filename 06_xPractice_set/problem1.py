a = int(input("Enter No 1:"))
b = int(input("Enter No 2:"))
c = int(input("Enter No 3:"))
d = int(input("Enter No 4:"))

if(a>b and a>c and a>d):
    print("Greatestt no. is a:",a)

elif(b>a and b>c and b>d):
    print("Greatestt no. is b:",b)

elif(c>b and c>a and c>d):
    print("Greatestt no. is c:",c)

elif(d>b and d>c and d>a):
    print("Greatestt no. is d:",d)