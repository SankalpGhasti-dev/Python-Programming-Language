username = input("Enter your username:")

length = len(username)

if(length>=10):
    print(f"your username contains {length} characters.")

else:
    print(f"Your username contains less than 10 characters which is {length}.")