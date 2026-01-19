n = int(input("Enter no:"))

for i in range(2,n):
    if(n%i == 0):
        print(f"Number {n} is not prime number.")
        break

else:
    print(f"Number {n} is prime number.")

# This code will tell 1 is also prime no. but it is false.
