a = int(input("Enter your age:"))

# if-elif-else Ladder 

if (a>=18):
    print("You are above the age of consent.\n")
    print("Good for you!\n")

elif(a<0):
    print("you are entering the invalid age")    

elif(a==18):
    print("You are entering 0. which is also invalid age.\n")

else:
    print("You are below the age of consent.\n")

print("End of the Program.\n")

